# Adaptive Explainable Log Anomaly Detection (XLogAD)

This repository contains the codebase for the M.Tech dissertation project: **"Beyond Detection: An Adaptive Explainable Framework for Log Anomaly Detection with Concept Drift Resilience"**.

## Research Goals
1. **Explainability (XAI):** Move beyond black-box log anomaly detection by identifying exactly *which* log tokens trigger an anomaly flag using Attention and SHAP.
2. **Drift Resilience:** Adapt to evolving log formats (concept drift) using online learning techniques like ADWIN.
3. **Real-World Benchmarking:** Evaluate on gold-standard public datasets (HDFS, BGL) from the Loghub repository.

## Pipeline Architecture
1. **Parsing:** Extract templates from raw unstructured logs using the **Drain3** algorithm.
2. **Sequence Modeling:** Encode templates into numerical sequences and train an LSTM/Transformer to predict events.
3. **Explainability:** Apply SHAP (DeepExplainer) to extract feature importance.
4. **Drift Detection:** Monitor streaming logs for performance degradation using River ML (ADWIN).

## Project Structure
- `data/` : Contains raw and parsed datasets (ignored in git).
- `data_prep.py` : Script to download and parse log data using Drain3.
- `requirements.txt` : Python dependencies.
