import os
import time
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve
from sklearn.decomposition import PCA

def main():
    print("=== Phase 2: HDFS Semantic Unsupervised Pipeline ===")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    seq_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
    emb_csv = os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv')
    
    # 1. Load Semantic Embeddings
    print("[1] Loading 384D Sentence-Transformers Embeddings...")
    emb_df = pd.read_csv(emb_csv)
    max_id = int(emb_df['EventId'].max()) + 1
    emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
    for _, row in emb_df.iterrows():
        emb_matrix[int(row['EventId'])] = row.drop('EventId').values
        
    # 2. Load the perfectly intact block sequences parsed from the 1.5GB raw HDFS.log
    print(f"[2] Loading 10,000 fully intact HDFS blocks from {seq_csv}...")
    seq_df = pd.read_csv(seq_csv)
    X = []
    y = []
    def get_positional_encoding(seq_len, d_model=384):
        pe = np.zeros((seq_len, d_model))
        for pos in range(seq_len):
            for i in range(0, d_model, 2):
                pe[pos, i] = np.sin(pos / (10000 ** ((2 * i)/d_model)))
                if i + 1 < d_model:
                    pe[pos, i + 1] = np.cos(pos / (10000 ** ((2 * (i + 1))/d_model)))
        return pe

    for _, row in seq_df.iterrows():
        try:
            events = [int(e) for e in str(row['EventId']).split()]
        except ValueError:
            continue
        if len(events) < 2: continue
        
        # Aggregate semantic embeddings to form a sequence-level semantic representation
        embs = np.array([emb_matrix[e] for e in events])
        comp_emb = np.mean(embs, axis=0) # Compositional
        
        # Inject True Structural Aggregation using Positional Encodings
        pe = get_positional_encoding(len(events), 384)
        struct_emb = np.mean(embs * pe, axis=0) # Structural
        
        seq_emb = np.concatenate([comp_emb, struct_emb])
        X.append(seq_emb)
        label = 1 if str(row['Label']) == 'Anomaly' else 0
        y.append(label)
        
    X = np.array(X)
    y = np.array(y)
    
    # 3. Train-Test Split (Train only on normal data)
    split1, split2 = int(len(y) * 0.7), int(len(y) * 0.8)
    X_train = X[:split1][y[:split1] == 0] 
    X_val = X[split1:split2]
    y_val = y[split1:split2]
    X_test = X[split2:]
    y_test = y[split2:]
    
    # 4. Train Unsupervised Semantic PCA
    print("[3] Training Unsupervised Semantic PCA model...")
    start_time = time.time()
    pca = PCA(n_components=0.95)
    pca.fit(X_train)
    
    def get_reconstruction_error(X_data):
        X_proj = pca.transform(X_data)
        X_reconstructed = pca.inverse_transform(X_proj)
        return np.mean(np.square(X_data - X_reconstructed), axis=1)
        
    # 5. Dynamic Thresholding on Validation Set
    val_scores = get_reconstruction_error(X_val)
    precisions, recalls, thresholds = precision_recall_curve(y_val, val_scores)
    f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-10)
    best_thresh = thresholds[np.argmax(f1_scores)]
    print(f"[4] Optimal Semantic Reconstruction Threshold derived: {best_thresh:.6f}")
    
    # 6. Final Evaluation
    test_scores = get_reconstruction_error(X_test)
    test_preds = (test_scores > best_thresh).astype(int)
    p, r, f, _ = precision_recall_fscore_support(y_test, test_preds, average='binary', zero_division=0)
    
    print("\n=== Final Test Results ===")
    print(f"Precision: {p:.4f}")
    print(f"Recall:    {r:.4f}")
    print(f"F1-Score:  {f:.4f}")
    print(f"Execution Time: {time.time() - start_time:.4f}s")
    print("==========================")

if __name__ == '__main__':
    main()
