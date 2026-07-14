import os
import math
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
from sentence_transformers import SentenceTransformer
from sklearn.metrics import precision_recall_fscore_support
from river.drift import ADWIN

def parse_bgl(log_file):
    config = TemplateMinerConfig()
    template_miner = TemplateMiner(config=config)
    
    events = []
    labels = []
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            if len(parts) < 2:
                continue
            label_str = parts[0]
            log_content = parts[1]
            
            label = 0 if label_str == '-' else 1
            
            result = template_miner.add_log_message(log_content)
            events.append(result['cluster_id'])
            labels.append(label)
            
    return events, labels, template_miner

def extract_embeddings(template_miner, output_csv):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    clusters = template_miner.drain.clusters
    
    max_cluster_id = max([c.cluster_id for c in clusters]) if clusters else 0
    
    templates = [""] * (max_cluster_id + 1)
    
    for c in clusters:
        templates[c.cluster_id] = c.get_template()
        
    print(f"Encoding {len(templates)} templates (including padding at index 0)...")
    embeddings = model.encode(templates)
    
    df = pd.DataFrame(embeddings)
    df.insert(0, 'cluster_id', range(len(templates)))
    df.insert(1, 'template', templates)
    df.to_csv(output_csv, index=False)
    
    return embeddings

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:, :x.size(1), :]
        return x

class LogTransformer(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, pretrained_embeddings=None, nhead=4, num_layers=2):
        super(LogTransformer, self).__init__()
        self.embedding_dim = embedding_dim
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        if pretrained_embeddings is not None:
            self.embedding.weight.data.copy_(torch.from_numpy(pretrained_embeddings))
            
        self.pos_encoder = PositionalEncoding(embedding_dim)
        
        encoder_layers = nn.TransformerEncoderLayer(d_model=embedding_dim, nhead=nhead, dim_feedforward=hidden_dim, batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_layers=num_layers)
        
        self.fc = nn.Linear(embedding_dim, vocab_size)
        
    def forward(self, x):
        embeds = self.embedding(x) * math.sqrt(self.embedding_dim)
        embeds = self.pos_encoder(embeds)
        
        # Remove causal mask to allow full bidirectional context (BERT-style)
        out = self.transformer_encoder(embeds)
        last_out = out[:, -1, :] 
        
        logits = self.fc(last_out) 
        return logits

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    log_file = os.path.join(data_dir, 'BGL_2k.log')
    embeddings_file = os.path.join(data_dir, 'BGL_2k_embeddings.csv')
    
    print("=== Phase 3: BGL XAI Pipeline ===")
    print(f"Reading from: {log_file}")
    
    print("\n1. Parsing BGL dataset with Drain3...")
    events, labels, template_miner = parse_bgl(log_file)
    print(f"Parsed {len(events)} log lines. Found {len(template_miner.drain.clusters)} unique templates.")
    
    print("\n2. Generating semantic embeddings with sentence-transformers...")
    emb_matrix = extract_embeddings(template_miner, embeddings_file)
    print(f"Embeddings saved to {embeddings_file}. Shape: {emb_matrix.shape}")
    
    print("\n3. Building chronological dataset (Window Size = 10)...")
    window_size = 10
    X = []
    y_event = []
    y_label = []
    
    for i in range(len(events) - window_size):
        X.append(events[i:i+window_size])
        y_event.append(events[i+window_size])
        y_label.append(labels[i+window_size])
        
    X = np.array(X)
    y_event = np.array(y_event)
    y_label = np.array(y_label)
    
    # 70-10-20 Train-Val-Test split
    split1 = int(len(X) * 0.7)
    split2 = int(len(X) * 0.8)
    
    X_train, X_val, X_test = X[:split1], X[split1:split2], X[split2:]
    y_event_train, y_event_val, y_event_test = y_event[:split1], y_event[split1:split2], y_event[split2:]
    y_label_train, y_label_val, y_label_test = y_label[:split1], y_label[split1:split2], y_label[split2:]
    
    train_normal_idx = y_label_train == 0
    X_train = X_train[train_normal_idx]
    y_event_train = y_event_train[train_normal_idx]
    
    val_normal_idx = y_label_val == 0
    X_val = X_val[val_normal_idx]
    y_event_val = y_event_val[val_normal_idx]
    
    print(f"Chronological split complete.")
    print(f"Train size (normal only): {len(X_train)}")
    print(f"Val size (normal only): {len(X_val)}")
    print(f"Test size (all): {len(X_test)} (Anomalies: {np.sum(y_label_test)})")
    
    print("\n4. Initializing LogTransformer model...")
    vocab_size = emb_matrix.shape[0]
    embedding_dim = emb_matrix.shape[1]
    hidden_dim = 64
    
    model = LogTransformer(vocab_size, embedding_dim, hidden_dim, pretrained_embeddings=emb_matrix)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    print(f"Using device: {device}")
    
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.005)
    
    train_dataset = TensorDataset(torch.tensor(X_train, dtype=torch.long), torch.tensor(y_event_train, dtype=torch.long))
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    
    epochs = 10
    print(f"Training for {epochs} epochs...")
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch_X, batch_y in train_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            
            optimizer.zero_grad()
            out = model(batch_X)
            loss = criterion(out, batch_y)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            
        if (epoch + 1) % 2 == 0 or epoch == 0:
            print(f"Epoch {epoch+1}/{epochs} | Loss: {total_loss/len(train_loader):.4f}")
            
    print("\n5. Computing Dynamic Threshold on Validation Set...")
    model.eval()
    val_probs = []
    
    val_dataset = TensorDataset(torch.tensor(X_val, dtype=torch.long), torch.tensor(y_event_val, dtype=torch.long))
    val_loader = DataLoader(val_dataset, batch_size=256, shuffle=False)
    with torch.no_grad():
        for batch_X, batch_y in val_loader:
            batch_X, batch_y = batch_X.to(device), batch_y.to(device)
            out = model(batch_X)
            probs = F.softmax(out, dim=1)
            target_probs = probs[torch.arange(len(batch_y)), batch_y]
            val_probs.extend(target_probs.cpu().tolist())
            
    mu = np.mean(val_probs)
    sigma = np.std(val_probs)
    min_val_prob = min(val_probs) if val_probs else 0.001
    threshold = max(1e-6, min_val_prob * 0.5)
    print(f"Mean normal probability: {mu:.4f}, Std: {sigma:.4f}")
    print(f"Calculated Dynamic Threshold: < {threshold:.4f}")
    
    print("\n6. Evaluating Test Set with Dynamic Thresholding & ADWIN Drift Detection...")
    y_pred = []
    
    test_dataset = TensorDataset(torch.tensor(X_test, dtype=torch.long), torch.tensor(y_event_test, dtype=torch.long))
    
    # Initialize ADWIN drift detector
    adwin = ADWIN(delta=0.002)
    
    drift_alerts = 0
    recent_normal_X = []
    recent_normal_y = []
    
    print("Simulating Online Streaming...")
    
    for i in range(len(X_test)):
        model.eval()
        with torch.no_grad():
            batch_X = torch.tensor([X_test[i]], dtype=torch.long).to(device)
            target = y_event_test[i]
            true_label = y_label_test[i] # 0 for normal, 1 for anomaly
            
            out = model(batch_X)
            probs = F.softmax(out, dim=1)
            target_prob = probs[0, target].item()
            
        # Predict
        is_anomaly = 1 if target_prob < threshold else 0
        y_pred.append(is_anomaly)
        
        # Update ADWIN with error rate
        prediction_error = 1.0 if is_anomaly != true_label else 0.0
        adwin.update(prediction_error)
        
        # Buffer true normal sequences for online adaptation
        if true_label == 0:
            recent_normal_X.append(X_test[i])
            recent_normal_y.append(target)
            if len(recent_normal_X) > 200: # rolling memory buffer
                recent_normal_X.pop(0)
                recent_normal_y.pop(0)
        
        if adwin.drift_detected:
            print(f"  [!] DRIFT DETECTED at sequence {i}! Initiating online fine-tuning...")
            drift_alerts += 1
            
            # Partial retraining mechanism (avoid catastrophic forgetting)
            if len(recent_normal_X) > 0:
                model.train()
                optimizer = optim.Adam(model.parameters(), lr=0.002)
                criterion = nn.CrossEntropyLoss()
                
                tune_X = torch.tensor(recent_normal_X, dtype=torch.long)
                tune_y = torch.tensor(recent_normal_y, dtype=torch.long)
                tune_dataset = TensorDataset(tune_X, tune_y)
                tune_loader = DataLoader(tune_dataset, batch_size=32, shuffle=True)
                
                for epoch in range(5):
                    for b_X, b_y in tune_loader:
                        b_X, b_y = b_X.to(device), b_y.to(device)
                        optimizer.zero_grad()
                        out = model(b_X)
                        loss = criterion(out, b_y)
                        loss.backward()
                        optimizer.step()
                        
                print("      -> Fine-tuning complete. Model adapted to concept drift.")
                
                # Re-evaluate threshold on the newly learned buffer
                model.eval()
                new_probs = []
                with torch.no_grad():
                    for idx in range(len(recent_normal_X)):
                        b_X = torch.tensor([recent_normal_X[idx]], dtype=torch.long).to(device)
                        t_y = recent_normal_y[idx]
                        out = model(b_X)
                        probs = F.softmax(out, dim=1)
                        new_probs.append(probs[0, t_y].item())
                if new_probs:
                    threshold = max(1e-6, min(new_probs) * 0.5)
                    print(f"      -> New Dynamic Threshold: < {threshold:.4f}")
                    
    precision, recall, f1, _ = precision_recall_fscore_support(y_label_test, y_pred, average='binary', zero_division=0)
    
    print("\n=== Online Evaluation Results ===")
    print(f"Final Threshold: < {threshold:.4f}")
    print(f"Total Drift Alerts: {drift_alerts}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print("=================================")
    
    print("\n7. Running XAI module (SHAP)...")
    try:
        import shap
        
        class SHAPWrapper(nn.Module):
            def __init__(self, model):
                super().__init__()
                self.model = model
            def forward(self, embeds):
                embeds = embeds * math.sqrt(self.model.embedding_dim)
                embeds = self.model.pos_encoder(embeds)
                out = self.model.transformer_encoder(embeds)
                last_out = out[:, -1, :]
                return self.model.fc(last_out)

        wrapper = SHAPWrapper(model).to(device)
        wrapper.eval()
        
        anomaly_idx = np.where(np.array(y_pred) == 1)[0]
        if len(anomaly_idx) > 0:
            test_idx = anomaly_idx[0]
            
            bg_x = torch.tensor(X_train[:50], dtype=torch.long).to(device)
            bg_embeds = model.embedding(bg_x)
            
            test_x = torch.tensor([X_test[test_idx]], dtype=torch.long).to(device)
            test_embeds = model.embedding(test_x)
            
            print(f"Explaining Anomaly Sequence (Test Index {test_idx})")
            
            explainer = shap.GradientExplainer(wrapper, bg_embeds)
            shap_values = explainer.shap_values(test_embeds)
            
            target_event = y_event_test[test_idx]
            sv = np.array(shap_values)
            
            if sv.ndim == 4:
                if sv.shape[-1] == embedding_dim:
                    # Shape: (vocab_size, batch, seq_len, embed_dim)
                    sv_class = sv[target_event]
                else:
                    # Shape: (batch, seq_len, embed_dim, vocab_size)
                    sv_class = sv[0, :, :, target_event]
            else:
                sv_class = sv
                
            shap_aggregated = np.abs(sv_class).sum(axis=-1).squeeze()
            print("Successfully extracted SHAP values for the anomalous sequence!")
            print(f"Aggregated SHAP Scores: {np.round(shap_aggregated, 4)}")
            
            artifact_path = os.path.join(base_dir, 'xai_report.md')
            with open(artifact_path, 'w') as f:
                f.write(f"# XAI Explanation for Anomaly\n")
                f.write(f"**Aggregated SHAP Token Importance:**\n")
                f.write(f"```python\n{np.round(shap_aggregated, 4).tolist()}\n```\n")
                f.write("SHAP values successfully calculated via GradientExplainer. The scores represent the summed absolute gradient importance across the embedding dimension for each token in the sequence.\n")
            
            print(f"XAI Report saved to {artifact_path}")
            
    except Exception as e:
        print(f"Error during SHAP extraction: {e}")

if __name__ == "__main__":
    main()
