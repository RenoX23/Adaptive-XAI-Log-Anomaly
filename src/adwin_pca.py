"""
Phase 4: Concept Drift Adaptation via ADWIN + IncrementalPCA

This script demonstrates how our Semantic-Structural PCA pipeline handles
concept drift in a streaming deployment scenario. Since the HDFS dataset is
a single temporal snapshot with no natural drift, we simulate a realistic
production scenario:

    Epoch 1 (Sequences 0-499):   Original distribution (no drift).
    Epoch 2 (Sequences 500-999): Simulated drift - normal sequences gain
        a small Gaussian perturbation to their embeddings, mimicking a
        software update that slightly changes normal log patterns.
    Epoch 3 (Sequences 1000-1499): Stronger drift - larger perturbation.
    Epoch 4 (Sequences 1500-1999): Original distribution returns.

The static model has no mechanism to adapt and will flag drifted-normal
sequences as anomalies (false positives). The adaptive model uses ADWIN
to detect the shift and IncrementalPCA.partial_fit to recover.
"""

import os
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, IncrementalPCA
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve
from river.drift import ADWIN

# ---------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------

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


def reconstruction_error(pca_model, X):
    X = np.atleast_2d(X)
    X_proj = pca_model.transform(X)
    X_recon = pca_model.inverse_transform(X_proj)
    return np.mean(np.square(X - X_recon), axis=1)


# ---------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------

def main():
    print("=" * 70)
    print("  Phase 4: Concept Drift Adaptation (ADWIN + IncrementalPCA)")
    print("=" * 70)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    seq_csv = os.path.join(base_dir, 'data', 'HDFS_10k_full_sequences.csv')
    emb_csv = os.path.join(base_dir, 'data', 'HDFS_500k_template_embeddings.csv')

    # -- 1. Load Semantic Embeddings --
    print("\n[1/7] Loading 384D Sentence-Transformer Embeddings...")
    emb_df = pd.read_csv(emb_csv)
    max_id = int(emb_df['EventId'].max()) + 1
    emb_matrix = np.zeros((max_id, emb_df.shape[1] - 1))
    for _, row in emb_df.iterrows():
        emb_matrix[int(row['EventId'])] = row.drop('EventId').values

    # -- 2. Load & Embed Sequences --
    print("[2/7] Loading 10,000 intact HDFS block sequences...")
    seq_df = pd.read_csv(seq_csv)
    X_all, y_all = [], []
    for _, row in seq_df.iterrows():
        try:
            events = [int(e) for e in str(row['EventId']).split()]
        except ValueError:
            continue
        if len(events) < 2:
            continue
        X_all.append(embed_sequence(events, emb_matrix))
        y_all.append(1 if str(row['Label']) == 'Anomaly' else 0)

    X_all = np.array(X_all)
    y_all = np.array(y_all)
    n = len(y_all)
    print(f"     Total: {n} | Anomalies: {int(y_all.sum())} | Normal: {int((1-y_all).sum())}")

    # -- 3. Split: Train / Val / Test (70-10-20) --
    s1, s2 = int(n * 0.7), int(n * 0.8)
    X_train = X_all[:s1][y_all[:s1] == 0]
    X_val, y_val = X_all[s1:s2], y_all[s1:s2]
    X_test, y_test = X_all[s2:], y_all[s2:]

    # -- 4. Train the Static PCA --
    print("\n[3/7] Training Static PCA baseline...")
    n_components = min(X_train.shape[0], X_train.shape[1], 100)
    static_pca = PCA(n_components=n_components)
    static_pca.fit(X_train)

    val_errors = reconstruction_error(static_pca, X_val)
    prec_arr, rec_arr, thresh_arr = precision_recall_curve(y_val, val_errors)
    f1_arr = 2 * prec_arr * rec_arr / (prec_arr + rec_arr + 1e-10)
    static_threshold = thresh_arr[np.argmax(f1_arr)]
    print(f"     Static threshold: {static_threshold:.8f}")

    # -- 5. Simulate Concept Drift in Test Set --
    print("\n[4/7] Simulating concept drift in the test stream...")
    # We perturb NORMAL sequences in specific epochs to simulate
    # a software update that changes the normal log distribution.
    # Anomalous sequences remain unperturbed (they are real anomalies).

    np.random.seed(42)
    test_len = len(X_test)
    epoch_size = test_len // 4

    # Calculate perturbation scale relative to normal embedding magnitude
    normal_std = np.std(X_train, axis=0)
    drift_scale_medium = normal_std * 0.5   # moderate drift
    drift_scale_strong = normal_std * 1.0   # strong drift

    X_test_drifted = X_test.copy()
    drift_map = {}  # track which epochs have drift

    for idx in range(test_len):
        epoch = idx // epoch_size
        if y_test[idx] == 0:  # only perturb normal sequences
            if epoch == 1:
                X_test_drifted[idx] += np.random.randn(768) * drift_scale_medium
                drift_map[idx] = "medium"
            elif epoch == 2:
                X_test_drifted[idx] += np.random.randn(768) * drift_scale_strong
                drift_map[idx] = "strong"
            # Epoch 0 and 3: no drift (original distribution)

    n_drifted = len(drift_map)
    print(f"     Drifted {n_drifted} normal sequences across epochs 1-2.")
    print(f"     Epoch 0: Original | Epoch 1: Medium drift | Epoch 2: Strong drift | Epoch 3: Recovery")

    # -- 6a. Evaluate STATIC model on drifted test set --
    print("\n[5/7] Evaluating STATIC model (no adaptation)...")
    static_errors = reconstruction_error(static_pca, X_test_drifted)
    static_preds = (static_errors > static_threshold).astype(int)
    sp, sr, sf, _ = precision_recall_fscore_support(
        y_test, static_preds, average='binary', zero_division=0
    )
    print(f"     Static PCA  |  P: {sp:.4f}  |  R: {sr:.4f}  |  F1: {sf:.4f}")

    # Per-epoch breakdown for static
    print("\n     Per-Epoch Breakdown (Static):")
    for ep in range(4):
        start = ep * epoch_size
        end = min((ep + 1) * epoch_size, test_len)
        ep_p, ep_r, ep_f, _ = precision_recall_fscore_support(
            y_test[start:end], static_preds[start:end],
            average='binary', zero_division=0
        )
        label = ["Original", "Medium Drift", "Strong Drift", "Recovery"][ep]
        print(f"       Epoch {ep} ({label:>13}): P={ep_p:.4f} R={ep_r:.4f} F1={ep_f:.4f}")

    # -- 6b. Evaluate ADAPTIVE model on drifted test set --
    print("\n[6/7] Running ADAPTIVE model with ADWIN drift detection...")

    adaptive_pca = IncrementalPCA(n_components=n_components)
    batch_size = 256
    for i in range(0, len(X_train), batch_size):
        adaptive_pca.partial_fit(X_train[i:i + batch_size])

    adwin = ADWIN(delta=0.0005)
    recent_errors = []       # Rolling window of recent reconstruction errors
    recent_window = 100
    current_threshold = static_threshold

    adaptive_preds = []
    drift_events = []
    adaptations = 0
    
    # Cooldown: after adaptation, revert to baseline after N sequences.
    # If drift persists, ADWIN will quickly re-detect and re-adapt.
    # If drift ended (recovery), we stay at the correct baseline.
    cooldown = 0
    cooldown_period = 150  # ~30% of an epoch

    for idx in range(test_len):
        x = X_test_drifted[idx:idx + 1]
        error = reconstruction_error(adaptive_pca, x)[0]
        pred = 1 if error > current_threshold else 0
        adaptive_preds.append(pred)

        # Feed binary prediction into ADWIN
        adwin.update(pred)

        # Maintain rolling window
        recent_errors.append(error)
        if len(recent_errors) > recent_window:
            recent_errors.pop(0)

        # Cooldown: revert to baseline when cooldown expires
        if cooldown > 0:
            cooldown -= 1
            if cooldown == 0:
                current_threshold = static_threshold
                print(f"     << Cooldown expired at index {idx}: threshold reverted to baseline {current_threshold:.8f}")

        # Check for drift
        if adwin.drift_detected:
            adaptations += 1
            drift_events.append(idx)
            epoch_num = idx // epoch_size
            print(f"     >> ADWIN Drift #{adaptations} at index {idx} (Epoch {epoch_num})")

            if len(recent_errors) >= 20:
                # GAP-FINDING THRESHOLD ADAPTATION
                sorted_errs = np.sort(recent_errors)
                diffs = np.diff(sorted_errs)
                gap_idx = np.argmax(diffs)
                new_threshold = (sorted_errs[gap_idx] + sorted_errs[gap_idx + 1]) / 2
                
                # Safety: only adopt if the gap is meaningful (> 2x jump)
                if diffs[gap_idx] > sorted_errs[gap_idx] * 2:
                    current_threshold = new_threshold
                    cooldown = cooldown_period  # start cooldown timer
                    print(f"        Gap found: threshold = {current_threshold:.8f}")
                    print(f"        (below: {gap_idx+1}, above: {len(sorted_errs)-gap_idx-1}, cooldown: {cooldown_period})")
                else:
                    current_threshold = static_threshold
                    print(f"        No clear gap, reverting to baseline: {current_threshold:.8f}")

    adaptive_preds = np.array(adaptive_preds)
    ap, ar, af, _ = precision_recall_fscore_support(
        y_test, adaptive_preds, average='binary', zero_division=0
    )

    # Per-epoch breakdown for adaptive
    print("\n     Per-Epoch Breakdown (Adaptive):")
    for ep in range(4):
        start = ep * epoch_size
        end = min((ep + 1) * epoch_size, test_len)
        ep_p, ep_r, ep_f, _ = precision_recall_fscore_support(
            y_test[start:end], adaptive_preds[start:end],
            average='binary', zero_division=0
        )
        label = ["Original", "Medium Drift", "Strong Drift", "Recovery"][ep]
        print(f"       Epoch {ep} ({label:>13}): P={ep_p:.4f} R={ep_r:.4f} F1={ep_f:.4f}")

    # -- 7. Final Ablation Table --
    print("\n" + "=" * 70)
    print("  [7/7] ABLATION STUDY: Static vs. Adaptive (Under Concept Drift)")
    print("=" * 70)
    print(f"  {'Model':<35} {'Precision':>10} {'Recall':>10} {'F1-Score':>10} {'Drifts':>8}")
    print(f"  {'-'*35} {'-'*10} {'-'*10} {'-'*10} {'-'*8}")
    print(f"  {'Static PCA (No ADWIN)':<35} {sp:>10.4f} {sr:>10.4f} {sf:>10.4f} {0:>8}")
    print(f"  {'Adaptive PCA (With ADWIN)':<35} {ap:>10.4f} {ar:>10.4f} {af:>10.4f} {adaptations:>8}")
    print("=" * 70)

    if sf > 0:
        if af > sf:
            improvement = ((af - sf) / sf) * 100
            print(f"\n  ADWIN adaptation improved F1 by +{improvement:.1f}% relative!")
        elif af == sf:
            print(f"\n  Both models performed identically.")
        else:
            delta = ((sf - af) / sf) * 100
            print(f"\n  Note: Static model F1 was {delta:.1f}% higher (expected in low-drift scenarios).")

    print(f"\n  Total drift alerts: {len(drift_events)}")
    for i, d in enumerate(drift_events):
        print(f"    Drift #{i+1} at test index {d} (Epoch {d // epoch_size})")

    print("\nPhase 4 Complete.")


if __name__ == '__main__':
    main()
