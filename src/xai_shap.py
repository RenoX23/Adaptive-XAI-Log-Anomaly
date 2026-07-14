import os
import numpy as np
import pandas as pd
import shap
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
    
    def get_reconstruction_error(X_data):
        X_proj = pca.transform(X_data)
        X_reconstructed = pca.inverse_transform(X_proj)
        return np.mean(np.square(X_data - X_reconstructed), axis=1)
        
    print("Initializing SHAP KernelExplainer...")
    # Use a small background dataset for speed
    background = shap.kmeans(X_train, 10)
    explainer = shap.KernelExplainer(get_reconstruction_error, background)
    
    # Find an anomaly to explain
    anomaly_idx = np.where(y[split1:] == 1)[0][0] + split1
    test_X = X[anomaly_idx:anomaly_idx+1]
    events = raw_events[anomaly_idx]
    
    print(f"Explaining Anomaly Sequence (Length: {len(events)})...")
    shap_values = explainer.shap_values(test_X)
    
    # shap_values is an array of shape (1, 768)
    sv = shap_values[0]
    
    # Map the 768D SHAP values back to the individual events
    # We distribute the SHAP value of feature d proportionally to each event's contribution
    # For feature d, the total value is mean(E_i,d). 
    # To be mathematically rigorous without sign-flipping, we can simply weight the absolute SHAP importance
    # by the absolute contribution of the event to that feature.
    
    embs = np.array([emb_matrix[e] for e in events])
    pe = get_positional_encoding(len(events), 384)
    event_features = np.concatenate([embs, embs * pe], axis=1) # shape: (seq_len, 768)
    
    # Calculate each event's share of the absolute magnitude for each feature
    abs_event_features = np.abs(event_features)
    feature_totals = np.sum(abs_event_features, axis=0) + 1e-10
    
    event_importance = np.zeros(len(events))
    for i in range(len(events)):
        # Proportion of feature d belonging to event i
        prop = abs_event_features[i] / feature_totals
        # Multiply by the absolute SHAP value for feature d and sum across all dimensions
        event_importance[i] = np.sum(prop * np.abs(sv))
        
    # Normalize event importances to sum to 100%
    if np.sum(event_importance) > 0:
        event_importance = (event_importance / np.sum(event_importance)) * 100
        
    print(f"\n=== SHAP Event Importance (Total Reconstruction Error: {explainer.expected_value + np.sum(sv):.6f}) ===")
    for i, (evt, imp) in enumerate(zip(events, event_importance)):
        print(f"Event {i+1} (ID {evt}): {imp:.2f}%")
        
    # Save the explainer and an example report
    with open(os.path.join(base_dir, 'xai_report.txt'), 'w') as f:
        f.write("SHAP Explanation for Anomalous Sequence:\n")
        for i, (evt, imp) in enumerate(zip(events, event_importance)):
            f.write(f"Event {i+1} (ID {evt}): Importance = {imp:.2f}%\n")
    print("Saved xai_report.txt")

if __name__ == '__main__':
    main()
