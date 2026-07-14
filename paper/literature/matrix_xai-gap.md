# Literature Review Matrix: XAI Gap

## 1. Performance Bottleneck Detection and Root Cause Analysis Using Explainable AI
- **Author:** SHANMUGASUNDARAM SIVAKUMAR
- **Year:** 2023
- **Venue:** IRE Journals
- **Problem Solved / Identified:** Performance bottlenecks in complex systems can significantly hinder operational efficiency. Traditional performance management approaches fall short in providing clear insights into the underlying causes of performance issues.
- **Methodology:** Explores the integration of Explainable Artificial Intelligence (XAI) in identifying and addressing the root causes of performance bottlenecks. Uses Decision Trees and Support Vector Machines incorporated with LIME and SHAP for explainability.
- **Dataset used:** Data from diverse sources including system logs, application performance monitoring tools, and user feedback (real-world case studies across IT, healthcare, and finance sectors).
- **Results:** XAI significantly improves detection accuracy (Decision Tree with XAI achieved 92% accuracy, SVM 89%, traditional monitoring 75%). Provided actionable insights and better understanding of bottleneck causes.
- **Limitations / Drawbacks:** Computational demands of XAI methods (particularly SHAP) can be high, potentially slowing down real-time analysis in resource-constrained environments. Integrating XAI into legacy systems requires substantial investment in time and resources.
- **Research Gaps:** Exploring ways to optimize XAI algorithms for real-time analysis without compromising interpretability. Creating standardized frameworks for adopting XAI in performance monitoring.
- **Abstract:** Performance bottlenecks in complex systems can significantly hinder operational efficiency and user satisfaction. These bottlenecks often result from various factors, including resource limitations, inefficient algorithms, or suboptimal system configurations...

## 2. Experience Report: Deep Learning-based System Log Analysis for Anomaly Detection
- **Author:** Zhuangbin Chen, Jinyang Liu, Wenwei Gu, Yuxin Su, Jieming Zhu, Yongqiang Yang, Michael R. Lyu
- **Year:** 2022
- **Venue:** IEEE/ACM ICSE '22 (arXiv version)
- **Problem Solved / Identified:** Lack of rigorous comparison among representative log-based anomaly detectors that resort to neural networks. Moreover, re-implementation demands non-trivial efforts.
- **Methodology:** Comprehensive review and evaluation of five popular neural networks used by six state-of-the-art DL-based log anomaly detectors (DeepLog, LogAnomaly, Logsy, Autoencoder, LogRobust, CNN).
- **Dataset used:** HDFS and BGL datasets.
- **Results:** Supervised methods generally achieve better performance than unsupervised methods. Logs' semantics contribute to detection, especially for unsupervised methods. Autoencoder exhibits great resilience against noisy training data.
- **Limitations / Drawbacks:** Existing studies carry a closed-world assumption (log data is stable, identical set of distinct log events).
- **Research Gaps:** Unprecedented logs have a significant impact on anomaly detection. Need for closer engineering collaboration, better logging practices, and model improvements (online learning, human-in-the-loop).
- **Abstract:** Logs have been an imperative resource to ensure the reliability and continuity of many software systems, especially large-scale distributed systems. They faithfully record runtime information to facilitate system troubleshooting...

## 3. TRANSLOG: A Unified Transformer-based Framework for Log Anomaly Detection
- **Author:** Hongcheng Guo, Xingyu Lin, Jian Yang, Yi Zhuang, Jiaqi Bai, Tieqiao Zheng, Liangfan Zheng, Weichao Hou, Bo Zhang, Zhoujun Li
- **Year:** 2022
- **Venue:** arXiv
- **Problem Solved / Identified:** Retraining whole network for unknown domains is inefficient in real industrial scenarios, especially for low-resource domains. Previous deep models focus on single domains, leading to poor generalization on multi-domain logs.
- **Methodology:** TRANSLOG, a unified Transformer-based framework comprised of a pretraining and adapter-based tuning stage. Pretrained on source domain and transferred to target domain via adapter-based tuning.
- **Dataset used:** HDFS, BGL, Thunderbird.
- **Results:** TRANSLOG achieves state-of-the-art performance with fewer trainable parameters and lower training costs in the target domain. F1 score 0.99 on HDFS, 0.98 on BGL, 0.99 on Thunderbird.
- **Limitations / Drawbacks:** The gap between different pretrained log models can influence the performance, requiring further analysis.
- **Research Gaps:** Semantic migration between log sources for a unified multiple sources detection.
- **Abstract:** Log anomaly detection is a key component in the field of artificial intelligence for IT operations (AIOps). Considering log data of variant domains, retraining the whole network for unknown domains is inefficient in real industrial scenarios...

## 4. MLAD: A Unified Model for Multi-system Log Anomaly Detection
- **Author:** Runqiang Zang, Hongcheng Guo, Jian Yang, Jiaheng Liu, Zhoujun Li, Tieqiao Zheng, Xu Shi, Liangfan Zheng, Bo Zhang
- **Year:** 2024
- **Venue:** arXiv
- **Problem Solved / Identified:** Mainstream models necessitate specific training for individual system datasets. Models lack cognitive reasoning capabilities for direct transferability. Encounter "identical shortcut" predicament where anomalous logs are classified as normal due to reconstruction errors.
- **Methodology:** MLAD, a unified model incorporating semantic relational reasoning across multiple systems. Employs Sentence-bert for semantic vectors. Revamps Attention layer with a sparse transformation (α-entmax). Uses a Gaussian Mixture Model (GMM) as a decoder to highlight the uncertainty of rare words.
- **Dataset used:** BGL, HDFS, Thunderbird.
- **Results:** MLAD demonstrates superiority on the datasets (F1: 0.9184 on BGL, 0.8946 on HDFS, 0.8962 on Thunderbird). Improved transfer learning capabilities.
- **Limitations / Drawbacks:** Need a more systematic and universal log extraction method.
- **Research Gaps:** Designing a more systematic and universal log extraction method to obtain better performance.
- **Abstract:** In spite of the rapid advancements in unsupervised log anomaly detection techniques, the current mainstream models still necessitate specific training for individual system datasets, resulting in costly procedures and limited scalability...

## 5. LogRCA: Log-based Root Cause Analysis for Distributed Services
- **Author:** Thorsten Wittkopp, Philipp Wiesner, and Odej Kao
- **Year:** 2024
- **Venue:** arXiv
- **Problem Solved / Identified:** Faults often propagate extensively within systems, which can result in a large number of anomalies being detected. Remaining challenging for users to quickly identify the actual root cause of a failure.
- **Methodology:** LogRCA uses a semi-supervised learning approach (PU learning) with a transformer model and a custom objective function to deal with rare and unknown errors. Employs a data balancing approach through automatic clustering to improve performance on rare failures.
- **Dataset used:** A large-scale production log dataset produced by 46666 different services, with 44.3 million log lines.
- **Results:** Outperforms baselines (Decision Tree, Random Forest, SVM, FNN). LogRCA covered all root cause log lines in 65 out of 80 cases.
- **Limitations / Drawbacks:** Does not automatically decide on a threshold for how many log lines should be presented to the user.
- **Research Gaps:** Investigating how many log lines are actually needed to provide sufficient context. Exploring how the investigation time window size can be derived automatically from context.
- **Abstract:** To assist IT service developers and operators in managing their increasingly complex service landscapes, there is a growing effort to leverage artificial intelligence in operations. To speed up troubleshooting, log anomaly detection has received much attention...

## 6. LogLLM: Log-based Anomaly Detection Using Large Language Models
- **Author:** Wei Guan, Jian Cao, Shiyou Qian, Jianqi Gao, Chun Ouyang
- **Year:** 2024
- **Venue:** arXiv
- **Problem Solved / Identified:** Traditional deep learning methods struggle to capture the semantic information embedded in log data. Prompt engineering methods struggle to customize solutions. Fine-tuning methods encounter challenges such as limited semantic understanding and memory overflow.
- **Methodology:** LogLLM framework leveraging LLMs. Employs BERT for extracting semantic vectors, and Llama for classifying log sequences. Introduces a projector to align vector representation spaces. Trained through a novel three-stage procedure.
- **Dataset used:** HDFS, BGL, Liberty, Thunderbird.
- **Results:** Outperforms state-of-the-art methods (DeepLog, LogAnomaly, PLELog, FastLogAD, LogBERT, LogRobust, CNN, NeuralLog, RAPID) across the datasets. Average F1 0.959.
- **Limitations / Drawbacks:** High computational cost (longest training time among all compared methods).
- **Research Gaps:** N/A
- **Abstract:** Software systems often record important runtime information in logs to help with troubleshooting. Log-based anomaly detection has become a key research area that aims to identify system issues through log data. Traditional deep learning methods often struggle to capture the semantic information...

## 7. TPLogAD: Unsupervised Log Anomaly Detection Based on Event Templates and Key Parameters
- **Author:** Jiawei Lu, Chengrong Wu
- **Year:** 2024
- **Venue:** arXiv
- **Problem Solved / Identified:** Semantic loss (existing methods ignore the richer semantic and structural information in parameters). Parameter abandonment. Difficulty in adapting to diversity and dynamics of logs.
- **Methodology:** TPLogAD, a universal unsupervised method. Performs anomaly detection based on event templates and key parameters. Uses itemplate2vec and para2vec for semantic representation. BiLSTM and attention mechanism to learn semantic and association information.
- **Dataset used:** BGL, Thunderbird, HDFS, Spirit.
- **Results:** Outperforms existing log anomaly detection methods. Average F1 0.95 and 0.96 for BGL and ThunderBird, 0.95 and 0.97 for HDFS and Spirit.
- **Limitations / Drawbacks:** N/A
- **Research Gaps:** N/A
- **Abstract:** Log-system is an important mechanism for recording the runtime status and events of Web service systems, and anomaly detection in logs is an effective method of detecting problems. However, manual anomaly detection in logs is inefficient...

## 8. LogSemFuse: Semantic Evidence Fusion for Explainable Log Anomaly Detection
- **Author:** Hassan Jabri, Zeyang Ma, Zhijie Wang, Tse-Hsun (Peter) Chen
- **Year:** 2026
- **Venue:** arXiv
- **Problem Solved / Identified:** Existing model-based detectors typically expose only scores or labels rather than operational semantics behind a decision, lacking semantic evidence for explainability. LLMs can recover richer log semantics, but using them as standalone detectors can be costly.
- **Methodology:** LogSemFuse, a plug-in semantic augmentation framework. Combines backbone predictions with reusable semantic evidence from local event patterns, LLM-based semantic reasoning, and cluster-derived executable rules to produce both anomaly decisions and evidence-based explanations.
- **Dataset used:** HDFS, BGL, Liberty.
- **Results:** Improves every non-perfect baseline, preserves the already perfect case, recovers 98.8% of backbone false negatives, and produces explanations preferred over direct LLM explanations. Modest inference-time overhead.
- **Limitations / Drawbacks:** Results may be affected by preprocessing, session construction, clustering, prompting.
- **Research Gaps:** N/A
- **Abstract:** Log anomaly detection is critical for reliability monitoring and failure diagnosis in modern software systems. Existing model-based detectors provide useful anomaly signals, but they can still miss anomalous sessions and typically expose only scores or labels rather than the operational semantics behind a decision...

## 9. Log-based Anomaly Detection with Deep Learning: How Far Are We?
- **Author:** Van-Hoang Le, Hongyu Zhang
- **Year:** 2022
- **Venue:** ICSE '22
- **Problem Solved / Identified:** Existing DL models for log-based anomaly detection claim very high accuracy but overlook important aspects associated with experimental datasets, evaluation metrics, and experimental settings. The problem has not been solved yet.
- **Methodology:** In-depth analysis of five state-of-the-art DL models (DeepLog, LogAnomaly, PLELog, LogRobust, CNN) focusing on training data selection, data grouping, class distribution, data noise, and early detection ability.
- **Dataset used:** HDFS, BGL, Spirit, Thunderbird.
- **Results:** Training data selection strategies (random vs chronological) have significant impact. Random selection causes data leakage. Grouping methods influence performance. Models lose accuracy with shorter sequences. Imbalanced class distribution affects effectiveness. Data noise (mislabeled logs, parsing errors) downgrades performance.
- **Limitations / Drawbacks:** DL models perform poorly with imbalanced data, parsing errors, and mislabeled logs.
- **Research Gaps:** Need for a variety of datasets for evaluation. Improving accuracy of semi-supervised models. Building effective models for early detection. Handling log parsing errors and evolving systems.
- **Abstract:** Software-intensive systems produce logs for troubleshooting purposes. Recently, many deep learning models have been proposed to automatically detect system anomalies based on log data. These models typically claim very high detection accuracy...

## 10. Unseen Anomaly Detection from System Logs
- **Author:** Yanni Tang, Zhuoxing Zhang, Lanting Fang, Sebastian Link, Wu Chen, Kaiqi Zhao
- **Year:** 2026
- **Venue:** SIGMOD
- **Problem Solved / Identified:** Existing log anomaly detection methods operate under the assumption that anomalous patterns remain consistent between training and testing. They fail to identify unseen anomalies introduced by software upgrades (anomaly shift).
- **Methodology:** UnseenLog, a novel framework for unseen anomaly detection. Introduces a MinMax strategy to select augmented anomaly samples (balancing reliability and novelty). Proposes Recurrent Iterative Selection and Enhancement (RISE) training scheme for progressive graph model optimization.
- **Dataset used:** Forum, Halo, Novel.
- **Results:** UnseenLog significantly outperforms state-of-the-art baselines, achieving at least a 6% improvement in F1 score.
- **Limitations / Drawbacks:** High computational complexity for training due to iterative process.
- **Research Gaps:** N/A
- **Abstract:** Detecting anomalies in system logs effectively is crucial for ensuring software reliability. However, most existing log anomaly detection methods operate under the assumption that anomalous patterns remain consistent between the training and testing phases...

## 11. GAL-MAD: Towards Explainable Anomaly Detection in Microservice Applications Using Graph Attention Networks
- **Author:** Lahiru Akmeemana, Chamodya Attanayake, Husni Faiz, Sandareka Wickramanayake
- **Year:** 2026
- **Venue:** ACSW
- **Problem Solved / Identified:** Existing methods fail to capture high-dimensional dependencies and complex interactions in microservices. Public datasets lack multivariate performance metrics. Need for explainable anomaly detection.
- **Methodology:** GAL-MAD, leveraging Graph Attention and LSTM architectures to capture spatial and temporal dependencies. Uses SHAP for anomaly localization to enhance explainability. Introduces the RS-Anomic dataset.
- **Dataset used:** RS-Anomic dataset (generated using RobotShop microservice application).
- **Results:** GAL-MAD outperforms state-of-the-art models (GDN, MAD-GAN, KitNET, Transformer) on the RS-Anomic dataset, achieving higher accuracy and recall.
- **Limitations / Drawbacks:** Computational overhead during GCN training on large graphs (>1000 nodes) requires significant GPU resources. Evaluated on a simulated dataset.
- **Research Gaps:** Integration with Apache Kafka for real-time streaming data ingestion. Development of dynamic graph adaptation mechanisms. Incorporation of data drift detection and automated model retraining.
- **Abstract:** The distributed and dynamic nature of microservices poses significant challenges to maintaining system reliability, highlighting the need for effective anomaly detection. Existing statistical and classical machine learning methods often fail to capture the high-dimensional dependencies...

## 12. Automated Root Cause Analysis in Distributed Micro services Systems Using Hybrid AI Techniques
- **Author:** Krishna Veni Ampolu, G. Siva Surya Naidu, B. Devi, S. Triveni, P. Vaikunta Rao, S. Hemanth Kumar, Penta Rupavathi, Prasanth Chintada
- **Year:** 2026
- **Venue:** IJIRT
- **Problem Solved / Identified:** Manual RCA is nearly impossible. Traditional rule-based methods fail to capture dynamic and temporal dependencies, resulting in prolonged downtimes and high MTTR. 'Black-box' limitation of deep AI models.
- **Methodology:** Intelligent RCA System leveraging a hybrid AI pipeline: Isolation Forest for anomaly detection, LSTM for failure prediction, GCN for fault localization, and SHAP for explainability.
- **Dataset used:** Simulated microservices environment dataset.
- **Results:** Achieves 94% accuracy in anomaly detection and significantly reduces MTTR (from 52 minutes to under 10 seconds).
- **Limitations / Drawbacks:** Computational overhead during GCN training on large graphs.
- **Research Gaps:** Integration with Apache Kafka. Development of dynamic graph adaptation mechanisms. Data drift detection.
- **Abstract:** Modern distributed systems and cloud-native microservices architectures generate massive volumes of log data and telemetry metrics daily, making manual Root Cause Analysis (RCA) nearly impossible for operations teams...

## 13. Deep Learning for Root Cause Detection in Distributed Systems with Structural Encoding and Multi-modal Attention
- **Author:** Yaokun Ren
- **Year:** 2024
- **Venue:** Journal of Computer Technology and Software
- **Problem Solved / Identified:** Challenges in root cause identification within microservice architectures, focusing on limited structural modeling capabilities and insufficient integration of multi-dimensional features.
- **Methodology:** Transformer-based model with Structure-Aware Trace Encoding (SATE) and Multi-dimensional Attention Fusion (MAF).
- **Dataset used:** Alibaba Trace Open Dataset.
- **Results:** The model maintains high discriminative power under service topology perturbations. Achieves 93.6% accuracy, 89.4% AUC, 91.0% F1-score.
- **Limitations / Drawbacks:** High computational overhead and sensitivity to completeness of structural information.
- **Research Gaps:** Improving inference efficiency and model lightweighting. Combining graph and sequence learning for incomplete trace data. Federated learning for privacy.
- **Abstract:** This paper addresses key challenges in root cause identification within microservice architectures, focusing on limited structural modeling capabilities and insufficient integration of multi-dimensional features...

## 14. LogBASA: Log Anomaly Detection Based on System Behavior Analysis and Global Semantic Awareness
- **Author:** Liping Liao, Ke Zhu, Jianzhen Luo, and Jun Cai
- **Year:** 2023
- **Venue:** International Journal of Intelligent Systems (Hindawi)
- **Problem Solved / Identified:** Existing methods mostly consider only sequence patterns or semantic info, leading to high rate of missed and false alarms.
- **Methodology:** LogBASA. Constructs a system log knowledge graph (SLKG). Uses a self-attention encoder-decoder transformer model. Combines adaptive spatial boundary delineation and sequence reconstruction objective functions.
- **Dataset used:** HDFS, BGL, Thunderbird.
- **Results:** Accuracy rate of 99.3%, 95.1%, and 97.2% on HDFS, BGL, and Thunderbird datasets respectively.
- **Limitations / Drawbacks:** High model complexity due to GCN, MLP, and transformer models.
- **Research Gaps:** Addressing the problems of poor feature recognition and unstable performance in existing methods.
- **Abstract:** System log anomaly detection is important for ensuring stable system operation and achieving rapid fault diagnosis. System log sequences include data on the execution paths and time stamps of system tasks in addition to a large amount of semantic information...

## 15. SXAD: Shapely eXplainable AI-Based Anomaly Detection Using Log Data
- **Author:** KASHIF ALAM, KASHIF KIFAYAT, GABRIEL AVELINO SAMPEDRO, VINCENT KAROVIČ JR., AND TARIQ NAEEM
- **Year:** 2024
- **Venue:** IEEE Access
- **Problem Solved / Identified:** AI models work as a black-box, making it challenging to provide reasoning behind judgments in LAD.
- **Methodology:** SXAD (Shapely eXplainable Anomaly Detection) framework. Utilizes Kernel SHAP approach. Employs several ML models: Decision Tree (DT), Random Forest (RF), and Gradient Boosting (GB).
- **Dataset used:** HDFS.
- **Results:** Accuracy rates of 99.99%, 99.85%, and 99.99% for DT, RF, and GB respectively. Provides interpretable and dependable results using SHAP.
- **Limitations / Drawbacks:** Need for fairness and bias reduction.
- **Research Gaps:** Extending contribution to reduction in fairness and biasness in XAI models for ethical consideration.
- **Abstract:** Artificial Intelligence (AI) has made tremendous progress in anomaly detection. However, AI models work as a black-box, making it challenging to provide reasoning behind their judgments in a Log Anomaly Detection (LAD)...

## 16. TrustGraph: A Heterogeneous GNN for Dynamic Zero-Trust Policy Enforcement in Microservices
- **Author:** Nurmyrat Amanmadov, Jemshit Iskanderov, Tarlan Abdullayev
- **Year:** 2025
- **Venue:** International Journal of Advanced Computer Science and Applications (IJACSA)
- **Problem Solved / Identified:** Gap between security requirements and available detection methods in microservices. Isolated tools struggle to capture the combined effect of operational behaviors, access flows, and trust decisions.
- **Methodology:** TrustGraph, a heterogeneous graph-based Zero-Trust framework. Represents microservices using multi-modal telemetry embedded into graph nodes and edges. GNN architecture with attention. Joint anomaly detection and trust computation mechanism.
- **Dataset used:** TrainTicket, Sock Shop, DeathStarBench.
- **Results:** 97.2% accuracy, 98.1% recall, and 0.987 AUC on TrainTicket. Latency overhead below 3.2 ms.
- **Limitations / Drawbacks:** System-wide failure of telemetry agents would disable the protection mechanism. Deployment in highly ephemeral production environments might require periodic fine-tuning.
- **Research Gaps:** Exploring adaptive thresholding techniques. Extending the framework with Federated Learning capabilities. Integrating hardware-level telemetry.
- **Abstract:** Securing cloud microservices requires a unified understanding of how services behave, authenticate, and interact in real time. Unlike existing methods that analyze telemetry signals in isolation, this work presents a heterogeneous graph-based Zero-Trust framework...

## 17. Systematic Literature Review of AI-Driven Multi-Cloud Anomaly Detection in Zero-Trust Frameworks
- **Author:** Ziad Almulla, Abdullah Albuali
- **Year:** 2026
- **Venue:** Applied Sciences
- **Problem Solved / Identified:** Multi-cloud is challenging to secure. Need to assess security, performance, and compliance with respect to technical challenges like secure identity management, segmentation, continuous policy optimization.
- **Methodology:** Systematic Literature Review (SLR).
- **Dataset used:** N/A (SLR).
- **Results:** N/A (SLR).
- **Limitations / Drawbacks:** N/A
- **Research Gaps:** Lack of attention to regulations such as GDPR and HIPAA in multi-cloud anomaly detection. Lack of implementation of basic zero-trust components.
- **Abstract:** Multi-cloud is becoming more challenging to secure as traditional perimeter-based security models have a hard time protecting workloads running across multiple cloud platforms, identities, and services...

## 18. Explainable AI Techniques for Root Cause Analysis in Complex Systems
- **Author:** Tobiloba Kollawole Adenekan
- **Year:** 2024
- **Venue:** Independent publication / Review
- **Problem Solved / Identified:** Traditional RCA techniques fall short with vast amounts of data and intricate relationships. "Black-box" nature of AI models limits trust.
- **Methodology:** Conceptual review of XAI techniques (SHAP, LIME, saliency maps) for RCA.
- **Dataset used:** N/A (Review).
- **Results:** N/A
- **Limitations / Drawbacks:** N/A
- **Research Gaps:** N/A
- **Abstract:** Root Cause Analysis (RCA) is an essential method used across various industries to identify the underlying causes of issues, inefficiencies, and failures in complex systems...

## 19. X-HEART: eXplainable heterogeneous log anomaly detection using robust transformers
- **Author:** Paul K. Mvula, Paula Branco, Guy-Vincent Jourdan, Herna L. Viktor
- **Year:** 2025
- **Venue:** Knowledge and Information Systems
- **Problem Solved / Identified:** Traditional log anomaly detection approaches struggle with the variety of log formats and structures due to reliance on log parsing.
- **Methodology:** X-HEART, a parsing-independent, end-to-end methodology. Leverages Transfer Learning (TL) and Transformer models (LogAnBERT, LogBERTa). Incorporates SHAP for explainability handling tokenized log events.
- **Dataset used:** BGL, Hadoop, HDFS, OpenStack, AIT, Hades, Thunderbird.
- **Results:** Models achieve near-perfect performance on most intra-system datasets. Domain-specific models (LogAnBERT, LogBERTa) are competitive with BERT/RoBERTa in intra-system setting and more computationally efficient.
- **Limitations / Drawbacks:** Cross-system scenarios present significant difficulties (negative transfer). SHAP can be computationally expensive.
- **Research Gaps:** Incorporating heterogeneous transfer techniques (HTL). Exploring more computationally efficient variants of SHAP like Tree SHAP, or LIME, DeepLIFT, Anchors.
- **Abstract:** Logs produced by heterogeneous systems are essential for analysing system behaviour and ensuring operational efficiency and security. Traditional log anomaly detection approaches often struggle with the variety of log formats and structures...

## 20. Detecting log anomaly using subword attention encoder and probabilistic feature selection
- **Author:** M. Hariharan, Abhinesh Mishra, Sriram Ravi, Ankita Sharma, Anshul Tanwar, Krishna Sundaresan, Prasanna Ganesan, R. Karthik
- **Year:** 2023
- **Venue:** Applied Intelligence
- **Problem Solved / Identified:** Representability of out-of-vocabulary (OOV) tokens. Need to eliminate noisy and less useful logs.
- **Methodology:** Subword Encoder Neural network (SEN) to learn word vectors from subword-level granularity using an attention encoder strategy. Naive Bayes Feature Selector (NBFS) to extract useful log events based on occurrence pattern.
- **Dataset used:** BGL, HDFS, OpenStack.
- **Results:** Achieves a 0.99 detection F1-score on BGL, HDFS and OpenStack log datasets.
- **Limitations / Drawbacks:** N/A
- **Research Gaps:** Model can be expanded to more kinds of logs. Explainability of target predictions can be back-traced to features on the logfile, opening pathways to self-healing workflows.
- **Abstract:** Log anomaly is a manifestation of a software system error or security threat. Detecting such unusual behaviours across logs in real-time is the driving force behind large-scale autonomous monitoring technology...

## 21. LogLS: Research on System Log Anomaly Detection Method Based on Dual LSTM
- **Author:** Yiyong Chen, Nurbol Luktarhan, Dan Lv
- **Year:** 2022
- **Venue:** Symmetry
- **Problem Solved / Identified:** Log anomaly detection methods using deep learning ignore the log time correlation. Poor prediction performance of LSTM on long sequences.
- **Methodology:** LogLS, a method based on dual LSTM with symmetric structure (preorder and postorder relationships). Adds a filter step on Spell for log parsing. Provides an online update mechanism using false positives.
- **Dataset used:** HDFS, BGL.
- **Results:** Accuracy of 99.84% on HDFS. Improves F1-measure after online updating.
- **Limitations / Drawbacks:** Not suitable for detecting parameters in the log.
- **Research Gaps:** Improving the model to detect each parameter in the log. Solving the problem that LSTM cannot predict unseen log execution paths.
- **Abstract:** System logs record the status and important events of the system at different time periods. They are important resources for administrators to understand and manage the system. Detecting anomalies in logs is critical to identifying system faults in time...
