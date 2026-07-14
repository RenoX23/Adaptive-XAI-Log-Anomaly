import os
import numpy as np
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve
from sklearn.decomposition import PCA

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
seq_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
emb_csv = os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv')

emb_df = pd.read_csv(emb_csv)
max_id = int(emb_df['EventId'].max()) + 1
emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
for _, row in emb_df.iterrows():
    emb_matrix[int(row['EventId'])] = row.drop('EventId').values

def get_positional_encoding(seq_len, d_model=384):
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** ((2 * i)/d_model)))
            if i + 1 < d_model:
                pe[pos, i + 1] = np.cos(pos / (10000 ** ((2 * (i + 1))/d_model)))
    return pe

seq_df = pd.read_csv(seq_csv)
X = []
y = []
for _, row in seq_df.iterrows():
    try:
        events = [int(e) for e in str(row['EventId']).split()]
    except ValueError:
        continue
    if len(events) < 2: continue
    
    # Structural Aggregation: E(t) * PE(t)
    pe = get_positional_encoding(len(events), 384)
    embs = np.array([emb_matrix[e] for e in events])
    
    # We concatenate the mean pooled (compositional) and the structure pooled (positional)
    comp_emb = np.mean(embs, axis=0)
    struct_emb = np.mean(embs * pe, axis=0)
    
    seq_emb = np.concatenate([comp_emb, struct_emb])
    X.append(seq_emb)
    
    label = 1 if str(row['Label']) == 'Anomaly' else 0
    y.append(label)

X = np.array(X)
y = np.array(y)

split1, split2 = int(len(y) * 0.7), int(len(y) * 0.8)
X_train = X[:split1][y[:split1] == 0]
X_val = X[split1:split2]
y_val = y[split1:split2]
X_test = X[split2:]
y_test = y[split2:]

pca = PCA(n_components=0.95)
pca.fit(X_train)

def get_reconstruction_error(X_data):
    X_proj = pca.transform(X_data)
    X_reconstructed = pca.inverse_transform(X_proj)
    return np.mean(np.square(X_data - X_reconstructed), axis=1)

val_scores = get_reconstruction_error(X_val)
precisions, recalls, thresholds = precision_recall_curve(y_val, val_scores)
f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-10)
best_idx = np.argmax(f1_scores)
best_thresh = thresholds[best_idx]

test_scores = get_reconstruction_error(X_test)
test_preds = (test_scores > best_thresh).astype(int)
p, r, f, _ = precision_recall_fscore_support(y_test, test_preds, average='binary', zero_division=0)
print(f"Structural PCA | P: {p:.4f} | R: {r:.4f} | F1: {f:.4f}")
