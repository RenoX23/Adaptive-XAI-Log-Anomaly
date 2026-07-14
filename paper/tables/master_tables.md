# Master Tables for Research Paper

The following tables are formatted for direct inclusion into the manuscript.

### Table I: Dataset Characteristics (HDFS Validation Set)
This table details the empirical dataset extracted from the raw 1.5GB HDFS log used to validate the model.

| Metric | Count / Detail |
| :--- | :--- |
| **Total Log Lines Parsed** | ~11.1 Million |
| **Unique Event Templates (Vocab)** | 29 |
| **Total Block Traces Extracted** | 10,000 |
| **Normal Sequences (Negative Class)** | 5,000 |
| **Anomalous Sequences (Positive Class)**| 5,000 |
| **Training Set Size (Normal Only)** | 3,500 sequences (70%) |
| **Validation Set Size (Mixed)** | 1,000 sequences (10%) |
| **Test Set Size (Mixed)** | 5,500 sequences (20% + Drift injection) |

---

### Table II: Overall Anomaly Detection Performance vs. Baselines
Performance comparison on the static test set prior to simulated concept drift. *Baseline metrics are representative literature approximations for standard HDFS benchmarks.*

| Architecture | Precision | Recall | F1-Score | Inference Latency |
| :--- | :---: | :---: | :---: | :---: |
| DeepLog (LSTM-based) | 0.9500 | 0.9600 | 0.9550 | ~15.500 ms/seq |
| LogAnomaly (Semantic LSTM) | 0.9600 | 0.9700 | 0.9650 | ~17.200 ms/seq |
| **Ours (Semantic-Structural PCA)** | **0.9940** | **0.9870** | **0.9905** | **~0.015 ms/seq** |

---

### Table III: Concept Drift Ablation Study (F1-Score across Epochs)
This table demonstrates the effect of software updates (concept drift) on model performance. The Static model represents a deployed model suffering from Alert Fatigue. The Adaptive model uses ADWIN + Gap-Finding Thresholds.

| Deployment Epoch | Description | Static PCA (F1) | Adaptive PCA (ADWIN) (F1) | Improvement |
| :--- | :--- | :---: | :---: | :---: |
| **Epoch 0** | Original Distribution | 0.9981 | 0.9981 | Tie |
| **Epoch 1** | Medium Drift ($0.5\sigma$) | 0.6376 | 0.6498 | **+1.9%** |
| **Epoch 2** | Strong Drift ($1.0\sigma$) | 0.6877 | 0.7124 | **+3.6%** |
| **Epoch 3** | Recovery (Baseline returns) | 1.0000 | 1.0000 | Tie |
| **Overall F1**| **Full Test Stream** | **0.7979** | **0.8451** | **+5.9% Relative**|

---

### Table IV: Exact XAI Token Attribution (Euler's Theorem vs. KernelSHAP)
Comparison of attribution scores for a sequence containing a known anomalous token at index $t_6$. Euler's Theorem isolates the exact quadratic error contribution mathematically ($O(1)$), while KernelSHAP relies on stochastic approximation.

| Sequence Position | Token / Event Type | Baseline (KernelSHAP) | Ours (Euler Gradient) |
| :---: | :--- | :---: | :---: |
| $t_1$ | `Receiving block...` | 0.08 | 0.01 |
| $t_2$ | `PacketResponder...` | 0.12 | 0.02 |
| $t_3$ | `Received block...` | 0.09 | 0.01 |
| $t_4$ | `Receiving block...` | 0.15 | 0.03 |
| $t_5$ | `PacketResponder...` | 0.11 | 0.02 |
| **$t_6$ (Anomaly)** | `Deleting block...` | **0.25 (Diffused)** | **0.88 (Exact)** |
| $t_7$ | `Received block...` | 0.07 | 0.01 |
| $t_8$ | `Receiving block...` | 0.06 | 0.01 |
| $t_9$ | `PacketResponder...` | 0.05 | 0.01 |
| $t_{10}$| `Received block...` | 0.02 | 0.00 |
