import os
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
from dataset import get_dataloaders
from model import LogLSTM

def train(model, train_loader, criterion, optimizer, device, epochs=5):
    """
    Trains the LogLSTM model on Normal log sequence sliding windows to predict the next event.
    """
    model.train()
    print("Starting training...")
    for epoch in range(epochs):
        epoch_loss = 0.0
        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            
            optimizer.zero_grad()
            logits = model(inputs)
            loss = criterion(logits, targets)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()
            
        print(f"Epoch {epoch+1}/{epochs} | Loss: {epoch_loss/len(train_loader):.4f}")

def evaluate(model, test_loader, device, window_size=10, top_k=3):
    """
    Evaluates the model block-by-block. Generates sliding windows dynamically for each sequence.
    If ANY predicted window fails to match the true next event in the Top-K, the block is an Anomaly.
    """
    model.eval()
    print(f"\nStarting evaluation (Top-{top_k} Block-Level Anomaly Detection)...")
    
    y_true = []
    y_pred = []
    
    with torch.no_grad():
        for seq, label in test_loader:
            # seq shape: (1, seq_len) because batch_size=1
            seq = seq[0].to(device)
            seq_len = seq.size(0)
            
            is_anomaly = False
            
            # Extract sliding windows dynamically
            inputs_list = []
            targets_list = []
            for i in range(seq_len - window_size):
                inputs_list.append(seq[i:i + window_size])
                targets_list.append(seq[i + window_size])
            
            if len(inputs_list) > 0:
                inputs_batch = torch.stack(inputs_list) # shape: (num_windows, window_size)
                targets_batch = torch.stack(targets_list)
                
                # Pass all windows of this sequence through the model simultaneously
                logits = model(inputs_batch)
                
                # Get Top-K
                top_k_preds = torch.topk(logits, k=top_k, dim=1).indices
                
                # Check if any target is not in top-K
                for i in range(len(targets_batch)):
                    target_event = targets_batch[i].item()
                    predicted_events = top_k_preds[i].tolist()
                    if target_event not in predicted_events:
                        is_anomaly = True
                        break
                        
            # Record result
            y_pred.append(1 if is_anomaly else 0)
            y_true.append(label.item())
            
    # Calculate metrics
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    print("\n--- Evaluation Results ---")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=["Normal", "Anomaly"], zero_division=0))
    
    return precision, recall, f1

def main():
    parser = argparse.ArgumentParser(description="Train and Evaluate LogLSTM")
    parser.add_argument("--seq_csv", type=str, default="../data/HDFS_2k_sequences.csv", help="Path to sequence CSV")
    parser.add_argument("--embeddings_csv", type=str, default="../data/HDFS_2k_template_embeddings.csv", help="Path to embeddings")
    parser.add_argument("--window_size", type=int, default=10, help="Window size used in dataset")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    parser.add_argument("--hidden_size", type=int, default=64, help="LSTM hidden size")
    parser.add_argument("--embedding_dim", type=int, default=384, help="Embedding dimension")
    parser.add_argument("--top_k", type=int, default=3, help="Top-K threshold for anomaly detection")
    args = parser.parse_args()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Initialization
    print("Loading data...")
    if not os.path.exists(args.seq_csv):
        args.seq_csv = args.seq_csv.replace("../", "")
        args.embeddings_csv = args.embeddings_csv.replace("../", "")
        
    train_loader, test_loader, vocab = get_dataloaders(args.seq_csv, window_size=args.window_size, batch_size=args.batch_size)
    vocab_size = len(vocab)
    
    print("Initializing model...")
    model = LogLSTM(
        vocab_size=vocab_size, 
        embedding_dim=args.embedding_dim, 
        hidden_size=args.hidden_size,
        pretrained_embeddings_path=args.embeddings_csv if os.path.exists(args.embeddings_csv) else None,
        vocab=vocab
    ).to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training Loop
    train(model, train_loader, criterion, optimizer, device, epochs=args.epochs)
    
    # Evaluation Loop
    evaluate(model, test_loader, device, window_size=args.window_size, top_k=args.top_k)

if __name__ == "__main__":
    main()
