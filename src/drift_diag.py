"""Diagnostic: understand error distributions across drift epochs."""
import os, numpy as np, pandas as pd
from sklearn.decomposition import PCA

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_positional_encoding(seq_len, d_model=384):
    pe = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** ((2 * i) / d_model)))
            if i + 1 < d_model:
                pe[pos, i + 1] = np.cos(pos / (10000 ** ((2 * (i + 1)) / d_model)))
    return pe

def embed_sequence(events, emb_matrix):
    embs = np.array([emb_matrix[e] for e in events])
    comp_emb = np.mean(embs, axis=0)
    pe = get_positional_encoding(len(events), 384)
    struct_emb = np.mean(embs * pe, axis=0)
    return np.concatenate([comp_emb, struct_emb])

emb_df = pd.read_csv(os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv'))
max_id = int(emb_df['EventId'].max()) + 1
emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
for _, row in emb_df.iterrows():
    emb_matrix[int(row['EventId'])] = row.drop('EventId').values

seq_df = pd.read_csv(os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv'))
X_all, y_all = [], []
for _, row in seq_df.iterrows():
    try:
        events = [int(e) for e in str(row['EventId']).split()]
    except ValueError:
        continue
    if len(events) < 2: continue
    X_all.append(embed_sequence(events, emb_matrix))
    y_all.append(1 if str(row['Label']) == 'Anomaly' else 0)

X_all = np.array(X_all)
y_all = np.array(y_all)
n = len(y_all)
s1, s2 = int(n * 0.7), int(n * 0.8)
X_train = X_all[:s1][y_all[:s1] == 0]
X_test, y_test = X_all[s2:], y_all[s2:]

pca = PCA(n_components=min(X_train.shape[0], X_train.shape[1], 100))
pca.fit(X_train)

def recon_error(X):
    X = np.atleast_2d(X)
    return np.mean(np.square(X - pca.inverse_transform(pca.transform(X))), axis=1)

# Apply drift
np.random.seed(42)
test_len = len(X_test)
epoch_size = test_len // 4
normal_std = np.std(X_train, axis=0)

X_drifted = X_test.copy()
for idx in range(test_len):
    epoch = idx // epoch_size
    if y_test[idx] == 0:
        if epoch == 1:
            X_drifted[idx] += np.random.randn(768) * normal_std * 0.5
        elif epoch == 2:
            X_drifted[idx] += np.random.randn(768) * normal_std * 1.0

errors = recon_error(X_drifted)

print("Error Distribution by Epoch and Label:")
print(f"{'Epoch':<8} {'Label':<10} {'Count':>6} {'Min':>12} {'Median':>12} {'Mean':>12} {'Max':>12}")
print("-" * 72)
for ep in range(4):
    start = ep * epoch_size
    end = min((ep + 1) * epoch_size, test_len)
    for label, lname in [(0, "Normal"), (1, "Anomaly")]:
        mask = y_test[start:end] == label
        if mask.sum() == 0: continue
        ep_errors = errors[start:end][mask]
        print(f"{ep:<8} {lname:<10} {len(ep_errors):>6} {ep_errors.min():>12.8f} {np.median(ep_errors):>12.8f} {ep_errors.mean():>12.8f} {ep_errors.max():>12.8f}")
