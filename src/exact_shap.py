import os
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
seq_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
emb_csv = os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv')

def get_positional_encoding(seq_len, d_model=384):
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** ((2 * i)/d_model)))
            if i + 1 < d_model:
                pe[pos, i + 1] = np.cos(pos / (10000 ** ((2 * (i + 1))/d_model)))
    return pe

def main():
    print("Loading Data...")
    emb_df = pd.read_csv(emb_csv)
    max_id = int(emb_df['EventId'].max()) + 1
    emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
    for _, row in emb_df.iterrows():
        emb_matrix[int(row['EventId'])] = row.drop('EventId').values

    seq_df = pd.read_csv(seq_csv)
    X = []
    y = []
    raw_events = []
    for _, row in seq_df.iterrows():
        try:
            events = [int(e) for e in str(row['EventId']).split()]
        except ValueError:
            continue
        if len(events) < 2: continue
        
        embs = np.array([emb_matrix[e] for e in events])
        comp_emb = np.mean(embs, axis=0)
        pe = get_positional_encoding(len(events), 384)
        struct_emb = np.mean(embs * pe, axis=0)
        seq_emb = np.concatenate([comp_emb, struct_emb])
        
        X.append(seq_emb)
        label = 1 if str(row['Label']) == 'Anomaly' else 0
        y.append(label)
        raw_events.append(events)

    X = np.array(X)
    y = np.array(y)
    
    split1 = int(len(y) * 0.7)
    X_train = X[:split1][y[:split1] == 0]
    
    print("Training PCA...")
    pca = PCA(n_components=0.95)
    pca.fit(X_train)
    
    # 1. Choose an anomaly
    anomaly_idx = np.where(y[split1:] == 1)[0][0] + split1
    test_X = X[anomaly_idx]
    events = raw_events[anomaly_idx]
    
    # 2. Compute the exact reconstruction residual
    X_proj = pca.transform([test_X])[0]
    X_reconstructed = pca.inverse_transform([X_proj])[0]
    residual = test_X - X_reconstructed
    
    # Gradient of squared error E = ||residual||^2 w.r.t test_X is 2 * residual
    # Actually, the orthogonal projection matrix P P^T gives reconstructed X.
    # Residual R = (I - P P^T) X. The error E = R^T R.
    # gradient dE/dX = 2 (I - P P^T) X = 2 * residual
    grad = 2 * residual
    
    # 3. Calculate event contributions
    N = len(events)
    embs = np.array([emb_matrix[e] for e in events])
    pe = get_positional_encoding(N, 384)
    
    event_importance = np.zeros(N)
    for i in range(N):
        # The vector V_i that Event i contributes to X
        V_i = np.concatenate([embs[i], embs[i] * pe[i]]) / N
        
        # Exact mathematical contribution to the anomaly error (Taylor expansion dot product)
        contribution = np.dot(V_i, grad)
        event_importance[i] = contribution
        
    # We take absolute value to show magnitude of impact, and normalize to 100%
    event_importance = np.abs(event_importance)
    if np.sum(event_importance) > 0:
        event_importance = (event_importance / np.sum(event_importance)) * 100
        
    print("\n=== Exact Mathematical Gradient XAI ===")
    print(f"Sequence Length: {N}")
    print(f"Total Reconstruction Error: {np.mean(residual**2):.6f}")
    print("Event-Level Importance:")
    for i, (evt, imp) in enumerate(zip(events, event_importance)):
        print(f"Event {i+1} (ID {evt}): {imp:.2f}%")
        
    with open(os.path.join(base_dir, 'xai_report.txt'), 'w') as f:
        f.write("Exact Gradient XAI Explanation for Anomalous Sequence:\n")
        for i, (evt, imp) in enumerate(zip(events, event_importance)):
            f.write(f"Event {i+1} (ID {evt}): Importance = {imp:.2f}%\n")

if __name__ == '__main__':
    main()
