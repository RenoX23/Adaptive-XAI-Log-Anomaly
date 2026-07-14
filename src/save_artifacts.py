import os
import json
import numpy as np
import pandas as pd
import joblib
from sklearn.decomposition import PCA
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve

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

def main():
    print("Saving Final Production Artifacts...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models')
    results_dir = os.path.join(base_dir, 'results')
    
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    seq_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
    emb_csv = os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv')

    # Load Embeddings
    emb_df = pd.read_csv(emb_csv)
    max_id = int(emb_df['EventId'].max()) + 1
    emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
    for _, row in emb_df.iterrows():
        emb_matrix[int(row['EventId'])] = row.drop('EventId').values

    # Load Sequences
    seq_df = pd.read_csv(seq_csv)
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
    X_val, y_val = X_all[s1:s2], y_all[s1:s2]
    X_test, y_test = X_all[s2:], y_all[s2:]

    # Train PCA
    pca = PCA(n_components=min(X_train.shape[0], X_train.shape[1], 100))
    pca.fit(X_train)

    def get_recon_error(pca_model, X_data):
        X_proj = pca_model.transform(X_data)
        X_recon = pca_model.inverse_transform(X_proj)
        return np.mean(np.square(X_data - X_recon), axis=1)

    val_errors = get_recon_error(pca, X_val)
    p_arr, r_arr, t_arr = precision_recall_curve(y_val, val_errors)
    f1_arr = 2 * (p_arr * r_arr) / (p_arr + r_arr + 1e-10)
    best_thresh = float(t_arr[np.argmax(f1_arr)])

    # Save Model and Threshold
    model_path = os.path.join(models_dir, 'semantic_structural_pca.pkl')
    thresh_path = os.path.join(models_dir, 'threshold.json')
    joblib.dump(pca, model_path)
    with open(thresh_path, 'w') as f:
        json.dump({"best_reconstruction_threshold": best_thresh}, f, indent=4)
    print(f"Model saved to: {model_path}")

    # Evaluate
    test_errors = get_recon_error(pca, X_test)
    test_preds = (test_errors > best_thresh).astype(int)
    p, r, f, _ = precision_recall_fscore_support(y_test, test_preds, average='binary', zero_division=0)

    # Save Results
    results_path = os.path.join(results_dir, 'final_metrics.csv')
    pd.DataFrame([{
        "Architecture": "Semantic-Structural PCA",
        "Precision": round(p, 4),
        "Recall": round(r, 4),
        "F1_Score": round(f, 4)
    }]).to_csv(results_path, index=False)
    print(f"Metrics saved to: {results_path}")

if __name__ == '__main__':
    main()
