# Literature Review & References Blueprint

This document outlines the ~20 core research papers that form the literature review for our manuscript. These are grouped by theme and map directly to the pain points our methodology solves.

## 1. Deep Learning Baselines (The Computational Bottleneck)
*We cite these to prove that while LSTMs/Transformers are highly accurate, their $O(N)$ sequential nature makes them too slow and expensive for real-time CI/CD deployment.*

1. **[DeepLog]** Du, M., Li, F., Zheng, G., & Srikumar, V. (2017). DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning. *ACM SIGSAC Conference on Computer and Communications Security (CCS)*. DOI: [10.1145/3133956.3134015](https://doi.org/10.1145/3133956.3134015)
2. **[LogAnomaly]** Meng, W., Liu, Y., Zhu, Y., Zhang, S., Pei, D., et al. (2019). LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs. *IJCAI*. DOI: [10.24963/ijcai.2019/658](https://doi.org/10.24963/ijcai.2019/658)
3. **[LogRobust]** Zhang, X., Xu, Y., Lin, Q., Qiao, B., Zhang, H., et al. (2019). Robust log-based anomaly detection on unstable log data. *FSE*.
4. **[HitAnomaly]** Huang, S., Liu, Y., Fung, C., He, R., Zhao, Y., et al. (2020). HitAnomaly: Hierarchical Transformers for Anomaly Detection in System Logs. *IEEE TNSM*.
5. **[Standard PCA]** Shlens, J. (2014). A tutorial on principal component analysis. *arXiv preprint*.

## 2. Concept Drift & Alert Fatigue (The Robustness Gap)
*We cite these to explain why models suffer from Alert Fatigue when software updates happen, and how ADWIN solves this.*

6. **[ADWIN]** Bifet, A., & Gavaldà, R. (2007). Learning from Time-Changing Data with Adaptive Windowing. *SIAM International Conference on Data Mining (SDM)*. DOI: [10.1137/1.9781611972771.42](https://doi.org/10.1137/1.9781611972771.42)
7. **[Concept Drift Review]** Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., & Bouchachia, A. (2014). A survey on concept drift adaptation. *ACM computing surveys (CSUR)*.
8. **[Online Log Drift]** Zhang, H., et al. (2021). Adaptive Anomaly Detection for Internet Services. *IEEE/ACM ICSE*.
9. **[River ML]** Montiel, J., et al. (2021). River: machine learning for streaming data in Python. *JMLR*.

## 3. Explainability (The XAI Noise Gap)
*We cite these to prove that current stochastic XAI methods (SHAP/LIME) are too slow and noisy for incident response, setting up our Exact Euler Gradient contribution.*

10. **[SHAP]** Lundberg, S. M., & Lee, Su-In. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS*. DOI: [10.48550/arXiv.1705.07874](https://doi.org/10.48550/arXiv.1705.07874)
11. **[LIME]** Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?" Explaining the predictions of any classifier. *KDD*.
12. **[Euler's Theorem in Networks]** Bach, S., Binder, A., Montavon, G., Klauschen, F., Müller, K. R., & Samek, W. (2015). On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. *PLOS One*.
13. **[Attention as Explanation]** Jain, S., & Wallace, B. C. (2019). Attention is not Explanation. *NAACL*.

## 4. Datasets, Parsing, and Semantic Encodings
*We cite these to validate our empirical data sources (HDFS), our fast parser (Drain), and our use of Sentence-Transformers over standard Word2Vec.*

14. **[HDFS Dataset]** Xu, W., Huang, L., Fox, A., Patterson, D., & Jordan, M. I. (2009). Detecting Large-Scale System Problems by Mining Console Logs. *SOSP*. DOI: [10.1145/1629575.1629587](https://doi.org/10.1145/1629575.1629587)
15. **[BGL Dataset]** Oliner, A., & Stearley, J. (2007). What supercomputers say: A study of five system logs. *IEEE DSN*.
16. **[Drain Parser]** He, P., Zhu, J., Zheng, Z., & Lyu, M. R. (2017). Drain: An Online Log Parsing Approach with Fixed Depth Tree. *IEEE ICWS*.
17. **[Loghub Benchmarks]** He, P., Zhu, J., Zheng, Z., & Lyu, M. R. (2020). Loghub: A large collection of system log datasets towards automated log analytics. *arXiv*.
18. **[Sentence-BERT]** Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *EMNLP*.
19. **[Word2Vec]** Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. *NeurIPS*.
20. **[Positional Encodings]** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *NeurIPS*.
