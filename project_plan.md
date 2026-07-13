# Adaptive Explainable Log Anomaly Detection: Project Plan & Checklist

## Core Objectives
1. **Explainability:** Identify anomalous log tokens using Attention/SHAP.
2. **Concept Drift Resilience:** Adapt to evolving log formats via ADWIN.
3. **Benchmarking:** Rigorous evaluation on HDFS/BGL datasets.

## Development Workflow
*   **Step-by-Step:** Complete one phase entirely before moving to the next.
*   **Audit Checkpoint:** The `ruthless_auditor` must review and pass a verdict on the results of each phase.
*   **Git Commit:** Only upon passing the audit, the phase is marked complete, and all changes are pushed to Git.

---

## Phase 1: Data Preparation & Parsing Baseline
- [x] Implement/Refine `data_prep.py` for downloading HDFS/BGL datasets.
- [x] Set up **Drain3** for log parsing and template extraction.
- [x] Convert parsed templates into structured numerical sequences (e.g., event ID sequences).
- [x] **Audit Checkpoint 1:** Validate parsing accuracy and dataset integrity. 
- [x] Git Commit Phase 1.

## Phase 2: Sequence Modeling (The Backbone)
- [ ] Implement baseline Sequence Model (LSTM or Transformer).
- [ ] Train the model on the normal log sequences.
- [ ] Evaluate baseline anomaly detection metrics (Precision, Recall, F1).
- [ ] **Audit Checkpoint 2:** Ensure the baseline model is competitive with existing literature (DeepLog, etc.).
- [ ] Git Commit Phase 2.

## Phase 3: Explainability (XAI Integration)
- [ ] Integrate Attention mechanisms into the sequence model.
- [ ] Apply **SHAP** (DeepExplainer) to extract feature importance scores.
- [ ] Generate visualizations showing exactly which tokens triggered anomalies.
- [ ] **Audit Checkpoint 3:** Verify that SHAP values are mathematically sound and the explanations are intuitive and robust.
- [ ] Git Commit Phase 3.

## Phase 4: Concept Drift Adaptation
- [ ] Simulate or identify concept drift in the test dataset (e.g., using BGL's temporal nature).
- [ ] Integrate River ML's **ADWIN** algorithm to monitor the model's loss/error rate.
- [ ] Implement an online learning loop to update the model when drift is detected.
- [ ] **Audit Checkpoint 4:** Prove that the model recovers from drift faster/better than a static baseline.
- [ ] Git Commit Phase 4.

## Phase 5: Final Evaluation & Paper Preparation
- [ ] Run comprehensive ablation studies (e.g., Model without ADWIN vs. Model with ADWIN).
- [ ] Finalize all plots, charts, and metrics tables.
- [ ] **Audit Checkpoint 5:** Final review of the entire experimental methodology and results.
- [ ] Git Commit Phase 5.
