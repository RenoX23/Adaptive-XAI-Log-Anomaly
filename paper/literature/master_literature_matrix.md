# Literature Review Matrix: Concept Drift and Gap Analysis

| Author | Title | Year | Venue | Problem Solved / Identified | Methodology | Dataset Used | Results | Limitations / Drawbacks | Research Gaps |
|---|---|---|---|---|---|---|---|---|---|
| Jiaqi Zhu, Shaofeng Cai, Fang Deng, Beng Chin Ooi, Wenqiao Zhang | METER: A Dynamic Concept Adaptation Framework for Online Anomaly Detection | 2023 | arXiv / Technical Report | Online anomaly detection is constrained by limited detection capacity and slow adaptation to evolving data streams (concept drift). | Proposes METER, combining a Static Concept-aware Detector (Autoencoder) for central concepts and a Dynamic Shift-aware Detector using a hypernetwork. Uses an Intelligent Evolution Controller (IEC) with evidential deep learning to detect concept drift. | 17 real-world datasets (incl. BGL, NSL, KDD99, INSECTS) and 4 synthetic datasets. | Significantly outperforms existing OAD approaches, achieving high AUCROC while maintaining high computational efficiency. | High dimension hypernetworks might add complexity; parameters of offline update strategy need careful tuning. | Efficiency and interpretability of OAD in the presence of concept drift; providing reliable uncertainty estimates for predictions. |
| Hema Latha Boddupally | Automating Incident Triage and Root Cause Intelligence Through Large Language Model–Driven Correlation of System Logs and Operational Metrics in Large-Scale Distributed Environments | 2023 | IJEETR | Difficulty of timely incident triage and accurate root cause identification due to high volume logs and heterogeneous metrics in distributed systems. | Introduces a novel correlation pipeline leveraging LLM-based contextual abstraction to unify unstructured log streams and structured metrics. Employs temporal analysis, contextual graphs, and hypothesis generation. | Evaluation environment emulating large-scale distributed services (case study on a global SaaS platform). | Observed a 41% reduction in MTTD and a 28% reduction in time-to-mitigation across 37 production incidents. | Empirical evaluation conducted in production-like environments rather than diverse live enterprise deployments. Model outputs influenced by prompt design. | Need for longitudinal studies to assess sustained adoption; integrating LLMs with formal causal techniques (causal inference, dependency graphs). |
| Pei Xiao, Tong Jia, Chiming Duan, Minghua He, Weijie Hong, Xixuan Yang, Yihan Wu, Ying Li, Gang Huang | CLSLog: Collaborating Large and Small Models for Log-based Anomaly Detection | 2025 | FSE Companion '25 | Small models struggle with handling evolutionary logs (concept drift), while LLMs suffer from inefficiency and lack of domain-specific knowledge. | Proposes CLSLog, modeling log anomaly detection as a semantic similarity binary classification task. Uses a small model (BERT-RNN) for non-evolutionary logs and to provide domain knowledge to augment an LLM for evolutionary logs. | BGL, Zookeeper (from LogHub). | Outperforms individual models (F1 score 97.10% on BGL, 99.31% on Zookeeper). Reduces LLM invocation costs by 90.63% on average. | Small models have lower recall with evolutionary logs, and LLMs suffer from high computational cost without small model integration. | Evaluating the method in complex industrial scenarios to assess accuracy and efficiency in real-world environments. |
| Sriram Ghanta | From Observability to Understanding: Automated Incident Triage Using Large Language Model Reasoning Over Logs, Metrics, and Traces | 2023 | IJEETR | Automated incident triage in cloud-native systems. Existing AIOps rely on statistical anomalies/supervised learning, struggling with unseen failure modes and context-dependent faults. | Leverages LLM reasoning over structured logs, metrics, and distributed traces. Integrates LLM-based reasoning atop existing observability pipelines to semantically interpret multi-modal telemetry and generate remediation hypotheses. | Case study on a global SaaS platform operating a 200+ microservice architecture. | 41% reduction in MTTD and a 28% reduction in time-to-mitigation across 37 production incidents. | Prompt stability, hallucination risks, cost and latency considerations. | Hybrid approaches combining LLMs with causal inference models, dependency graphs, and rule-based constraints. |
| Md Shoaib Alam et al. | Consumer Decision Fatigue and Clinical Errors: Behavioral Analysis of EHR Alert Overload in the US Hospitals | 2025 | ICONAT | Irrelevant (Focuses on EHR alert fatigue in healthcare, not Log Anomaly Detection/Concept Drift in software systems). | N/A | N/A | N/A | N/A | N/A |
# Literature Review Matrix: Encoding and Parsing

This document compiles the extracted literature review matrix for the papers in the `encoding-and-parsing` directory.

## Summary Matrix

| Title | Author, Year | Venue | Problem Identified | Methodology | Datasets | Results | Limitations | Gaps |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **Diagnostic Spatio-temporal Transformer with Faithful Encoding** | Jokin Labaien et al., 2023 | Knowledge-Based Systems / arXiv | Limitations of temporal positional encoding in capturing short time scales for complex ST dependencies. | Proposes supervised dependency discovery, using a novel discrete Fourier transform (DFT) based "faithful-Encoding", and DFStrans framework. | Elevator Case Study, SMAP, MSL, SMD | DFStrans achieves competitive anomaly detection and provides local/global diagnostic scores. | Requires labeled data for training (supervised). | Need for improved trust and interpretability in industrial AI systems (avoiding black boxes). |
| **LibreLog: Accurate and Efficient Unsupervised Log Parsing Using Open-Source Large Language Models** | Zeyang Ma et al., 2024 | arXiv (cs.SE) | Time-consuming manual labeling, high parsing costs due to log volume/LLM context limits, and privacy risks of commercial LLMs. | Proposes LibreLog: log grouping by syntactic similarity, RAG to select diverse logs, iterative self-reflection, and a log template memory. | LogHub-2.0 | Achieves 25% higher accuracy and is 2.7x faster than state-of-the-art LLM-based parsers. | Performance heavily depends on pre-grouping step; can be slower than heuristic parsers. | Addressing data leakage and generalization of open-source LLMs on proprietary logs. |
| **System Log Parsing with Large Language Models: A Review** | Viktor Beck et al., 2025 | arXiv (cs.LG) | Lack of structured overview, benchmarking, comparability, and reproducibility in the novel field of LLM-based log parsing. | Systematic literature review of 29 methods and benchmark of 7 open-source LLM-based parsers on public datasets. | LogHub, LogHub-2.0, Corrected LogHub, Custom Audit | ICL with RAG improves accuracy. Caching reduces cost/time. Llama3 performs well but underperforms GPT-3.5. | Inherits limitations of the field: high computational cost, hallucinations, lack of standardized metrics. | Need for standardized benchmarking and more cost-effective real-time processing strategies. |
| **Investigating and Improving Log Parsing in Practice** | Ying Fu et al., 2022 | ESEC/FSE 2022 | Existing parsers struggle in practice due to various separators and various lengths caused by nested objects. | Proposes Drain+: uses statistical-based separator generation and template merging via asymmetric Jaccard similarity. | 10 Ant Group microservices, 16 public datasets | Outperforms 6 state-of-the-art parsers on both industrial applications and public datasets. | Cannot determine candidate separators contextually; relies on statistical thresholds. | Need for adaptive parsers that learn separator contexts incrementally or via fine-tuning. |
| **Demonstration-Free: Towards More Practical Log Parsing with Large Language Models** | Yi Xiao et al., 2024 | ASE 2024 | LLM parsers' heavy reliance on demonstration examples causes substantial overhead and sensitivity to prompt quality. | Proposes LogBatcher: a demonstration-free parser. Partitions logs via DBSCAN, batches diverse logs via DPP sampling, and caches templates. | 16 Loghub-2k datasets | Exceeds accuracy of unsupervised baselines and outperforms supervised LLM parsers (LILAC, DivLog). | Performance relies on the initial DBSCAN clustering; caching depends on batch diversity. | Zero-demonstration log parsing addressing data leakage concerns and practical deployment. |
| **Automatic Parsing and Utilization of System Log Features in Log Analysis: A Survey** | Junchen Ma et al., 2023 | Applied Sciences (MDPI) | Need to synthesize and evaluate recent deep learning-based automated log parsing and feature extraction methodologies. | Classifies log parsing (clustering, heuristic, etc.) and feature extraction (digital, graphical). | N/A (Survey) | Highlights shift from clustering/heuristics to deep learning and semantic features. | Lack of universal parsers for multitype datasets; restrictive accuracy metrics. | Privacy in distributed system logs, sequence flow relational transfer learning, situational awareness. |
| **Enhancing Log Anomaly Detection with Semantic Embedding and Integrated Neural Network Innovations** | Zhanyang Xu et al., 2024 | CMC | Existing models rely on sequence/quantity attributes, ignore semantic info, and struggle to adapt to novel logs. | Proposes LogCEM: uses RoBERTa + enhanced SIF for semantic embeddings; uses 1D-MSCNN, ECA, and Mogrifier GRU for detection. | HDFS, BGL | Outperforms models like DeepLog, LogAnomaly, and LogBERT (F1 > 98.7%). | Offline training; high time and space complexity due to the Transformer model. | Need for online incremental training, model lightweighting, and accelerated gradient methods. |
| **Research on Log Anomaly Detection Based on Sentence-BERT** | Caiping Hu et al., 2023 | Electronics (MDPI) | Traditional methods are too slow; existing deep learning methods do not fully utilize log semantic information. | Proposes LogADSBERT: uses Sentence-BERT to extract semantic features and a Bi-LSTM with attention mechanism for anomaly detection. | HDFS, OpenStack | Achieves higher accuracy than DeepLog and LogAnomaly, showing strong robustness to new log injections. | F1-score may decrease if too many unseen log events are injected simultaneously. | Optimizing log preprocessing efficiency; multimodal log anomaly detection. |
| **A two-stage adversarial Transformer based approach for multivariate industrial time series anomaly detection** | Junfu Chen et al., 2024 | Applied Intelligence | Methods struggle with low-dimensional datasets or sparse variable relationships; absolute PE limits Transformers. | Proposes ATT-TSAAE: embeds an autoregressive TCN before attention, and uses a two-stage adversarial training strategy on the latent space. | SAT, SKAB, NAB-MT | Achieves superior F1 scores compared to advanced works (TranAD, MTAD-GAT). | High training time due to adversarial learning and complex architectures. | Online incremental training, model distillation (lightweighting), accelerated gradient methods. |
| **Enhancing multivariate time-series anomaly detection with positional encoding mechanisms in transformers** | Abdul Amir Alioghli et al., 2024 | J. of Supercomputing | Transformers struggle to determine data point positions. It's unclear which Positional Encoding (PE) is best for time-series data. | Evaluates Absolute PE, Rotary PE, and Relative PE variations (Representative, Global) for multivariate time-series anomaly detection. | 15 diverse datasets (HAI, Sleep, ECG, etc.) | Absolute PE is best for short sequences; Global attention is more effective for longer sequences. | Focuses on binary classification point anomalies, not change point detection. | Evaluating PEs for change point detection and forecasting in encoder-decoder setups. |
| **Positional encoding in transformer-based time series models: a survey** | Habib Irani et al., 2026 | IJMLC | Lack of comprehensive evaluations isolating the effects of positional encoding on time series classification tasks. | Systematic survey of 10 PE techniques evaluated on 15 diverse time series datasets using Time Series Transformer and PatchTST. | 15 diverse datasets | Advanced methods (SPE, TUPE) consistently outperform traditional sinusoidal approaches. Performance scales with sequence length. | Evaluated only on regularly sampled, complete time series in encoder-only architectures. | Handling irregular sampling, missing values, extreme non-stationarity, and encoder-decoder forecasting. |
| **Enhancing Anomaly Detection in Multivariate Time Series with Stacked Transformer Encoders and Adaptive Positional Embeddings** | Kella Sowmya et al., 2024 | Arabian J. for Sci. and Eng. | Traditional methods fail to capture spatio-temporal relationships fully; fixed encoders/PEs restrict adaptability. | Proposes a stacked transformer encoder using separate encoders for time and feature dimensions, combining fixed and learnable PEs. | SMD, SMAP, MSL, SWaT, WADI | Significantly outperforms baseline and SOTA models (e.g., TranAD, MTAD-GAT). | High computational cost and complexity; opacity in the decision-making process. | Enhancing interpretability through attention visualization and explainable AI techniques. |

---

## Detailed Extractions

### 1. Diagnostic Spatio-temporal Transformer with Faithful Encoding
- **Author, Year:** Jokin Labaien, Tsuyoshi Idé, Pin-Yu Chen, Ekhi Zugasti, Xabier De Carlos, 2023
- **Venue:** Knowledge-Based Systems / arXiv
- **Problem Solved / Identified:** Addressing anomaly diagnosis when the underlying data generation process has complex spatio-temporal (ST) dependencies. Highlights the limitation of vanilla temporal positional encoding in capturing higher frequencies (short time scales).
- **Methodology:** Formalizes the problem as supervised dependency discovery. Proposes a new positional encoding algorithm with a theoretical guarantee, based on discrete Fourier transform (DFT), called "faithful-Encoding". Introduces the DFStrans (Diagnostic Fourier-based Spatio-temporal Transformer) framework combining 1D multi-head CNNs and ST Transformers.
- **Dataset used:** Industrial Case Study (elevator control), Soil Moisture Active Passive satellite (SMAP), Mars Science Laboratory rover (MSL), Server Machine Dataset (SMD).
- **Results:** DFStrans achieves competitive results for anomaly detection (best in Elevator and SMD) and demonstrates strong capabilities in anomaly diagnosis by providing local and global diagnostic scores via spatial and temporal attention.
- **Limitations / Drawbacks:** Requires labeled data for training (supervised learning dependency).
- **Research Gaps:** The need to improve trust in AI model decisions, especially in industrial environments where black-box models are often avoided.
- **Abstract:** This paper addresses the task of anomaly diagnosis when the underlying data generation process has a complex spatio-temporal (ST) dependency. The key technical challenge is to extract actionable insights from the dependency tensor characterizing high-order interactions among temporal and spatial indices. We formalize the problem as supervised dependency discovery, where the ST dependency is learned as a side product of multivariate time-series classification. We show that temporal positional encoding used in existing ST transformer works has a serious limitation in capturing higher frequencies (short time scales). We propose a new positional encoding with a theoretical guarantee, based on discrete Fourier transform. We also propose a new ST dependency discovery framework, which can provide readily consumable diagnostic information in both spatial and temporal directions. Finally, we demonstrate the utility of the proposed model, DFStrans (Diagnostic Fourier-based Spatio-temporal Transformer), in a real industrial application of building elevator control.

### 2. LibreLog: Accurate and Efficient Unsupervised Log Parsing Using Open-Source Large Language Models
- **Author, Year:** Zeyang Ma, Dong Jae Kim, Tse-Hsun (Peter) Chen, 2024
- **Venue:** arXiv (cs.SE)
- **Problem Solved / Identified:** LLM-based parsers face challenges such as time-consuming manual labeling, increased parsing costs due to log volume and limited context sizes, and privacy risks when using commercial LLMs on sensitive logs.
- **Methodology:** Proposes LibreLog, an unsupervised log parsing approach leveraging open-source LLMs (Llama3-8B). Employs: 1) log grouping by syntactic similarity, 2) similarity scoring-based Retrieval Augmented Generation (RAG) to select diverse logs, 3) self-reflection to iteratively refine templates, and 4) log template memory to cache templates and reduce LLM queries.
- **Dataset used:** LogHub-2.0 (containing 14 large-scale system datasets).
- **Results:** LibreLog achieves 25% higher parsing accuracy and is 2.7 times faster compared to state-of-the-art LLM-based parsers, while mitigating privacy and cost concerns.
- **Limitations / Drawbacks:** Effectiveness relies heavily on the initial syntactic pre-grouping step. Can still be slower than purely heuristic-based parsers.
- **Research Gaps:** Addressing data leakage, generalizability of open-source LLMs on proprietary logs, and optimizing the selection of demonstrations.
- **Abstract:** Log parsing is a critical step that transforms unstructured log data into structured formats, facilitating subsequent log-based analysis. Traditional syntax-based log parsers are efficient and effective, but they often experience decreased accuracy when processing logs that deviate from the predefined rules. Recently, large language models (LLM) based log parsers have shown superior parsing accuracy. However, existing LLM-based parsers face three main challenges: 1) time-consuming and labor-intensive manual labeling for fine-tuning or in-context learning, 2) increased parsing costs due to the vast volume of log data and limited context size of LLMs, and 3) privacy risks from using commercial models like ChatGPT with sensitive log information. To overcome these limitations, this paper introduces LibreLog, an unsupervised log parsing approach that leverages open-source LLMs (i.e., Llama3-8B) to enhance privacy and reduce operational costs while achieving state-of-the-art parsing accuracy. LibreLog first groups logs with similar static text but varying dynamic variables using a fixed-depth grouping tree. It then parses logs within these groups using three components: i) similarity scoring-based retrieval augmented generation: selects diverse logs within each group based on Jaccard similarity... ii) self-reflection: iteratively query LLMs to refine log templates... and iii) log template memory: stores parsed templates to reduce LLM queries... Our evaluation on LogHub-2.0 shows that LibreLog achieves 25% higher parsing accuracy and processes logs 2.7 times faster compared to state-of-the-art LLM-based parsers.

### 3. System Log Parsing with Large Language Models: A Review
- **Author, Year:** Viktor Beck, Max Landauer, Markus Wurzenberger, Florian Skopik, Andreas Rauber, 2025
- **Venue:** arXiv (cs.LG)
- **Problem Solved / Identified:** There is a lack of structured overviews, standardized benchmarking, comparability, and reproducibility in the newly emerging field of LLM-based log parsing.
- **Methodology:** Systematic literature review of 29 LLM-based log parsing methods. The authors establish feature definitions (supervision, parsing mode, prompting, RAG, caching) and benchmark 7 open-source LLM-based log parsers on public datasets.
- **Dataset used:** LogHub, Corrected LogHub, LogHub-2.0, and a Custom Audit dataset.
- **Results:** Shows that In-Context Learning (ICL) with RAG improves accuracy. Caching significantly reduces cost and time. Open-source models like Llama3 perform well but often underperform proprietary models like GPT-3.5. Also highlights widespread reproducibility issues in the field.
- **Limitations / Drawbacks:** Exposes the field's limitations: high computational costs, LLM hallucinations, interpretability issues, and a lack of standardized benchmarking metrics.
- **Research Gaps:** The need for standardized benchmarking practices, more cost-effective strategies for real-time processing, and addressing reproducibility.
- **Abstract:** Log data provides crucial insights for tasks like monitoring, root cause analysis, and anomaly detection. Due to the vast volume of logs, automated log parsing is essential to transform semi-structured log messages into structured representations. Recent advances in large language models (LLMs) have introduced the new research field of LLM-based log parsing. Despite promising results, there is no structured overview of the approaches in this relatively new research field with the earliest advances published in late 2023. This work systematically reviews 29 LLM-based log parsing methods. We benchmark seven of them on public datasets and critically assess their comparability and the reproducibility of their reported results. Our findings summarize the advances of this new research field, with insights on how to report results, which data sets, metrics and which terminology to use, and which inconsistencies to avoid, with code and results made publicly available for transparency.

### 4. Investigating and Improving Log Parsing in Practice
- **Author, Year:** Ying Fu, Meng Yan, Jian Xu, Jianguo Li, Zhongxin Liu, Xiaohong Zhang, Dan Yang, 2022
- **Venue:** ESEC/FSE 2022
- **Problem Solved / Identified:** Investigates the effectiveness of state-of-the-art log parsers in industrial practice, identifying two major challenges: 1) various separators used across applications, and 2) various lengths of log messages due to nested objects.
- **Methodology:** Conducts an empirical study on 6 SOTA parsers. Proposes an improved log parser, "Drain+", which includes: a statistical-based separator generation component for dynamic log splitting, and a candidate event template merging component using asymmetric Jaccard similarity to merge templates.
- **Dataset used:** 10 microservice applications of Ant Group, 16 public datasets (LogHub).
- **Results:** Drain+ significantly outperforms the six state-of-the-art log parsers on both the industrial microservice applications and the public datasets (e.g., improves average parsing accuracy to 0.846 on industrial data).
- **Limitations / Drawbacks:** Cannot generate separators contextually; it relies on predefined statistical thresholds that might fail on highly irregular data.
- **Research Gaps:** Developing adaptive log parsers capable of determining separator viability based on context information via incremental learning or fine-tuning.
- **Abstract:** Logs are widely used for system behavior diagnosis by automatic log mining. Log parsing is an important data preprocessing step... Currently, many studies are devoted to proposing new log parsers. However, to the best of our knowledge, no previous study comprehensively investigates the effectiveness of log parsers in industrial practice... we conduct an empirical study on the effectiveness of six state-of-the-art log parsers on 10 microservice applications of Ant Group. Our empirical results highlight two challenges for log parsing in practice: 1) various separators... 2) Various lengths due to nested objects... we propose an improved log parser named Drain+ based on a state-of-the-art log parser Drain. Drain+ includes two innovative components to address the above two challenges: a statistical-based separators generation component, which generates separators automatically for log message splitting, and a candidate event template merging component, which merges the candidate event templates by a template similarity method. We evaluate the effectiveness of Drain+ on 10 microservice applications of Ant Group and 16 public datasets. The results show that Drain+ outperforms the six state-of-the-art log parsers...

### 5. Demonstration-Free: Towards More Practical Log Parsing with Large Language Models
- **Author, Year:** Yi Xiao, Van-Hoang Le, Hongyu Zhang, 2024
- **Venue:** 39th IEEE/ACM International Conference on Automated Software Engineering (ASE '24)
- **Problem Solved / Identified:** Existing LLM-based parsers heavily rely on labeled demonstration examples (In-Context Learning), which causes substantial overhead in LLM invocations and is highly sensitive to the quality of the demonstrations.
- **Methodology:** Proposes LogBatcher, a demonstration-free, training-free, and cost-effective LLM-based log parser. It groups logs into partitions via DBSCAN clustering, samples diverse logs using Determinantal Point Process (DPP) to form batches, prompts the LLM with these batches (leveraging latent commonality/variability), and caches results.
- **Dataset used:** 16 public log datasets (Loghub-2k).
- **Results:** LogBatcher outperforms state-of-the-art unsupervised baselines and supervised LLM-based log parsers (like LILAC and DivLog) in Group Accuracy, Message-Level Accuracy, and Edit Distance, while drastically reducing LLM invocation costs (by at least 106%).
- **Limitations / Drawbacks:** Heavily reliant on the initial DBSCAN clustering accuracy; caching effectiveness depends entirely on the diversity of the sampled batch.
- **Research Gaps:** Enabling zero-demonstration parsing to mitigate data leakage concerns and lower inference costs in production environments.
- **Abstract:** Log parsing, the process of converting raw log messages into structured formats, is an important initial step for automated analysis of logs of large-scale software systems. Traditional log parsers often rely on heuristics or handcrafted features... Recently, some log parsers have utilized powerful generative capabilities of large language models (LLMs). However, they heavily rely on demonstration examples, resulting in substantial overhead in LLM invocations. To address these issues, we propose LogBatcher, a cost-effective LLM-based log parser that requires no training process or labeled data. To leverage latent characteristics of log data and reduce the overhead, we divide logs into several partitions through clustering. Then we perform a cache matching process to match logs with previously parsed log templates. Finally, we provide LLMs with better prompt context specialized for log parsing by batching a group of logs from each partition. We have conducted experiments on 16 public log datasets and the results show that LogBatcher is effective and efficient for log parsing.

### 6. Automatic Parsing and Utilization of System Log Features in Log Analysis: A Survey
- **Author, Year:** Junchen Ma, Yang Liu, Hongjie Wan, Guozi Sun, 2023
- **Venue:** Applied Sciences (MDPI)
- **Problem Solved / Identified:** The need to systematically review, classify, and evaluate the myriad of automated log parsing and feature extraction methodologies proposed for log analysis.
- **Methodology:** Systematically surveys literature on log parsing (categorized into clustering, heuristic, utility itemset mining, and others) and feature extraction (digital features like count/index/time, and graphical features).
- **Dataset used:** N/A (Survey paper; analyzes literature on HDFS, BGL, OpenStack, etc.).
- **Results:** Highlights the paradigm shift from simple heuristics to deep learning and semantic-based feature extraction. Notes that highly complex structures (e.g., OpenStack) remain challenging for current parsers.
- **Limitations / Drawbacks:** Identifies limitations in existing literature, such as the absence of universal parsers for multitype datasets and the overly restrictive nature of current parsing accuracy metrics.
- **Research Gaps:** Future work needs to optimize preprocessing, achieve multimodal log anomaly detection, process distributed system logs while ensuring data privacy, and apply sequence flow relational transfer learning.
- **Abstract:** System logs are almost the only data that records system operation information, so they play an important role in anomaly analysis, intrusion detection, and situational awareness. However, it is still a challenge to obtain effective data from massive system logs. On the one hand, system logs are unstructured data, and, on the other hand, system log records cannot be directly analyzed and calculated by computers. In order to deal with these problems, current researchers digitize system logs through two key steps of log parsing and feature extraction. This paper classifies, analyzes, and summarizes the current log analysis research in terms of log parsing and feature extraction by investigating articles in recent years... Finally, in combination with the existing research, the research prospects in the field are elaborated and predicted.

### 7. Enhancing Log Anomaly Detection with Semantic Embedding and Integrated Neural Network Innovations
- **Author, Year:** Zhanyang Xu, Zhe Wang, Jian Xu, Hongyan Shi, Hong Zhao, 2024
- **Venue:** Computers, Materials & Continua (Tech Science Press)
- **Problem Solved / Identified:** Existing log anomaly detection relies predominantly on sequence or quantity attributes using single RNNs, failing to fully exploit semantic information embedded in logs and exhibiting limited adaptability to novel logs.
- **Methodology:** Proposes a hybrid architecture, LogCEM. Uses RoBERTa combined with an improved Smooth Inverse Frequency (SIF) algorithm and POS tagging to generate precise log semantic sentence vectors. Feeds these into a hybrid network fusing 1D Multi-Scale Convolutional Neural Networks (MSCNN), Efficient Channel Attention (ECA), and Mogrifier Gated Recurrent Units (GRU).
- **Dataset used:** HDFS, BGL.
- **Results:** LogCEM achieves excellent accuracy and robustness, outperforming mainstream methods like DeepLog, LogAnomaly, and LogBERT (achieving F1-scores of 98.79% on HDFS and 98.84% on BGL).
- **Limitations / Drawbacks:** High time and space complexity due to the heavy Transformer architecture. Offline training prevents autonomous updates.
- **Research Gaps:** The need for online incremental training, model lightweighting (e.g., model distillation), and accelerated gradient methods to reduce computational overhead.
- **Abstract:** System logs, serving as a pivotal data source for performance monitoring and anomaly detection, play an indispensable role in assuring service stability and reliability. Despite this, the majority of existing log-based anomaly detection methodologies predominantly depend on the sequence or quantity attributes of logs, utilizing solely a single Recurrent Neural Network (RNN) and its variant sequence models for detection. These approaches have not thoroughly exploited the semantic information embedded in logs... this article proposes a hybrid architecture based on a multiscale convolutional neural network, efficient channel attention and mogrifier gated recurrent unit networks (LogCEM)... we employ RoBERTa to extract the original word vectors from each word in the log template. In conjunction with the enhanced Smooth Inverse Frequency (SIF) algorithm, we generate more precise log sentence vectors... these log vector sequences are fed into a hybrid neural network, which fuses 1D Multi-Scale Convolutional Neural Network (MSCNN), Efficient Channel Attention Mechanism (ECA), and Mogrifier Gated Recurrent Unit (GRU)... The experimental results demonstrate that LogCEM not only exhibits excellent accuracy and robustness, but also outperforms the current mainstream log anomaly detection methods.

### 8. Research on Log Anomaly Detection Based on Sentence-BERT
- **Author, Year:** Caiping Hu, Xuekui Sun, Hua Dai, Hangchuan Zhang, Haiqiang Liu, 2023
- **Venue:** Electronics (MDPI)
- **Problem Solved / Identified:** Traditional methods fail to process enormous log data in time, and many deep learning methods do not fully utilize the rich semantic information existing in log data.
- **Methodology:** Proposes LogADSBERT. Adopts the Sentence-BERT model to extract semantic behavior characteristics (vectors) of log events. Implements anomaly detection via a Bidirectional Long Short-Term Memory (Bi-LSTM) network equipped with an attention mechanism.
- **Dataset used:** HDFS, OpenStack.
- **Results:** Achieves superior accuracy and robustness compared to DeepLog and LogAnomaly. Demonstrates strong robustness even under the scenario of new log event injections (F1-score 93.2% on HDFS with injections).
- **Limitations / Drawbacks:** Performance (F1-score) can degrade if an excessively large number of entirely new log events are injected simultaneously.
- **Research Gaps:** Optimizing log preprocessing efficiency; realizing multimodal log anomaly detection that integrates multiple types of log data for joint analysis.
- **Abstract:** Log anomaly detection is crucial for computer systems. By analyzing and processing the logs generated by a system, abnormal events or potential problems in the system can be identified, which is helpful for its stability and reliability. At present, due to the expansion of the scale and complexity of software systems, the amount of log data grows enormously, and traditional detection methods have been unable to detect system anomalies in time. Therefore, it is important to design log anomaly detection methods with high accuracy and strong generalization. In this paper, we propose the log anomaly detection method LogADSBERT, which is based on Sentence-BERT. This method adopts the Sentence-BERT model to extract the semantic behavior characteristics of log events and implements anomaly detection through the bidirectional recurrent neural network, Bi-LSTM. Experiments on the open log data set show that the accuracy of LogADSBERT is better than that of the existing log anomaly detection methods. Moreover, LogADSBERT is robust even under the scenario of new log event injections.

### 9. A two-stage adversarial Transformer based approach for multivariate industrial time series anomaly detection
- **Author, Year:** Junfu Chen, Dechang Pi, Xixuan Wang, 2024
- **Venue:** Applied Intelligence (Springer)
- **Problem Solved / Identified:** Existing multivariate abnormal detection methods struggle with low-dimensional datasets or sparse relationships between variables. Vanilla Transformer's absolute position encoding limits temporal pattern extraction.
- **Methodology:** Proposes ATT-TSAAE, a two-stage adversarial Transformer-based method. Embeds an autoregressive Temporal Convolutional Network (TCN) before the multi-head attention module to capture long-term/local features, replacing vanilla absolute positional encoding. Employs a two-stage adversarial training strategy (latent space discriminator and reconstruction discriminator) to constrain the latent space.
- **Dataset used:** A real-world dataset (SAT) and two public industrial sensor datasets (SKAB, NAB-MT).
- **Results:** Achieves F1 scores of 0.9679 (SAT), 0.7947 (SKAB), and 0.6452 (NAB-MT), demonstrating superior overall anomaly detection performance compared to recent advanced models like TranAD and MTAD-GAT.
- **Limitations / Drawbacks:** High training time and computational overhead due to the complex two-stage adversarial learning and deep network architecture.
- **Research Gaps:** The need for online incremental training frameworks, model lightweighting techniques (e.g., model distillation), and accelerated gradient methods.
- **Abstract:** Sensors in complex industrial systems generate multivariate time series data, frequently leading to diverse abnormal patterns that pose challenges for detection. The existing multivariate abnormal detection methods may encounter difficulties when applied to datasets with low dimensions or sparse relationships between variables. To address these issues, this study proposes a two-stage adversarial Transformer-based anomaly detection method. On the one hand, an autoregressive temporal convolutional network component is embedded before the multi-head attention module to capture features encompassing long-term and local information. Besides, this component utilizes a trainable neural network instead of the vanilla Transformer’s absolute position encoding, resulting in enhanced position information. On the other hand, the proposed two-stage adversarial learning strategy allows the model to effectively learn intricate multivariate data patterns via constraining latent space, thereby enhancing anomaly detection performance. Our method achieves F1 scores of 0.9679, 0.7947, and 0.6452 on a real-world dataset and two public industrial sensor datasets, demonstrating superior overall anomaly detection performance compared to recent advanced works.

### 10. Enhancing multivariate time-series anomaly detection with positional encoding mechanisms in transformers
- **Author, Year:** Abdul Amir Alioghli, Feyza Yıldırım Okay, 2024
- **Venue:** The Journal of Supercomputing (Springer)
- **Problem Solved / Identified:** Transformer networks struggle to accurately determine the position of data points and maintain sequence order. It remains unclear which Positional Encoding (PE) method is best for time-series anomaly detection.
- **Methodology:** Evaluates the potential of various PEs—Absolute PE, Rotary PE, and Relative PE variations (Representative attention and Global attention)—applied specifically to multivariate time-series anomaly detection.
- **Dataset used:** 15 diverse time series datasets (HAI, Sleep, ECG, MSL, SMAP, SMD, WADI, SWaT, etc.).
- **Results:** Absolute PE performs well across different window sizes. Representative attention works best for short sequences (lengths 8, 16, 32); Global attention is more effective for longer sequences (lengths 64, 128). Absolute PE and Global attention are the most time-efficient.
- **Limitations / Drawbacks:** The evaluation focuses solely on point anomaly detection (binary classification), leaving out change point detection. Uses encoder-only setups.
- **Research Gaps:** Need to evaluate PEs for change point detection and to extend PE analysis into forecasting tasks using full encoder-decoder architectures.
- **Abstract:** The surge in automation driven by IoT devices has generated extensive time-series data with highly variable features, posing challenges in anomaly detection. DL, particularly Transformer networks, has shown promise in addressing these issues. However, Transformer networks struggle with accurately determining the position of data points and maintaining the order of data in sequences, leading to the development of Positional Encoding (PE)... This study evaluates the potential of PEs including Absolute PE, Rotary PE, and two modifications of Relative PE methods (Representative attention and Global attention), for multivariate time-series anomaly detection problems. The experimental results indicate that Absolute PE, with a 98% accuracy score, performs well across different window sizes. Representative attention... performs best for short sequences... whereas, Global attention... is more effective for longer sequences... Overall, Absolute PE and Global attention are the most time-efficient; while, Representative attention has significantly higher training times, particularly for long sequences.

### 11. Positional encoding in transformer-based time series models: a survey
- **Author, Year:** Habib Irani, Vangelis Metsis, 2026
- **Venue:** International Journal of Machine Learning and Cybernetics
- **Problem Solved / Identified:** Despite extensive research in transformer architectures, the time series community lacks a comprehensive evaluation isolating the specific effects of positional encoding methods on time series classification tasks.
- **Methodology:** A systematic survey and benchmarking of 10 positional encoding techniques (Absolute PE, Learnable PE, RPE, tAPE, RoPE, eRPE, TUPE, ConvSPE, T-PE, ALiBi). Evaluates effectiveness across 15 diverse datasets using two foundational architectures (Time Series Transformer and PatchTST).
- **Dataset used:** 15 diverse time series datasets (Sleep, CardiacArrhythmia, InsectSound, ElectricDevices, FaceDetection, MelbournePedestrian, SharePriceIncrease, LSST, RacketSports, SelfRegulationSCP1/2, JapaneseVowels, UniMiB-SHAR, RoomOccupancy, EMGGestures).
- **Results:** Validates that positional encoding is essential. Advanced methods like SPE (Stochastic Positional Encoding) and TUPE (Transformer with Untied Positional Encoding) consistently outperform traditional sinusoidal approaches. Performance strongly depends on sequence length and architecture type.
- **Limitations / Drawbacks:** The evaluation is focused on regularly sampled, complete time series, and only uses encoder-only classification architectures.
- **Research Gaps:** How PE methods handle irregular sampling, missing values, and extreme non-stationarity. Extension of the analysis to encoder-decoder architectures for forecasting.
- **Abstract:** Recent advancements in transformer-based models have greatly improved time series analysis, providing robust solutions for tasks such as forecasting, anomaly detection, and classification. A crucial element of these models is positional encoding, which allows transformers to capture the intrinsic sequential nature of time series data. This survey systematically examines existing techniques for positional encoding in transformer-based time series models. We investigate a variety of methods, including fixed, learnable, relative, and hybrid approaches, and evaluate their effectiveness in different time series classification tasks. Our findings indicate that data characteristics like sequence length, signal complexity, and dimensionality significantly influence method effectiveness. Advanced positional encoding methods exhibit performance gains in terms of prediction accuracy, however, they come at the cost of increased computational complexity... By delivering a comprehensive overview and quantitative benchmarking, this survey intends to assist researchers and practitioners in selecting and designing effective positional encoding methods for transformer-based time series models.

### 12. Enhancing Anomaly Detection in Multivariate Time Series with Stacked Transformer Encoders and Adaptive Positional Embeddings
- **Author, Year:** Kella Sowmya, K. Ramesh, 2024
- **Venue:** Arabian Journal for Science and Engineering (Springer)
- **Problem Solved / Identified:** Traditional methods and standard transformer models struggle to fully capture deep, intricate spatio-temporal features. The use of a fixed number of encoders and fixed positional embeddings restricts adaptability across diverse time series contexts.
- **Methodology:** Introduces a stacked transformer encoder architecture using separate encoders for the time and feature dimensions. Enhances contextual understanding by integrating both fixed and learnable positional embeddings (averaging them). Performs joint forecasting and reconstruction.
- **Dataset used:** SMD, SMAP, MSL, SWaT, WADI.
- **Results:** The stacked architecture combined with adaptive embeddings significantly outperforms baseline and state-of-the-art models (such as TranAD, MTAD-GAT) across multiple benchmark datasets.
- **Limitations / Drawbacks:** High computational cost and complexity as the number of stacked layers increases; opacity in the decision-making process limits interpretability.
- **Research Gaps:** Enhancing the interpretability of the model through attention visualization and explainable AI techniques to make the decision process transparent for critical applications.
- **Abstract:** Detecting anomalies in multivariate time series data is a complex task due to the challenges of effectively representing spatio-temporal features and extracting deep, intricate patterns across both time and feature dimensions. Traditional methods often struggle to capture these relationships fully, and even transformer-based models, while promising, face limitations due to their use of a fixed number of encoders and positional embeddings, which restrict their adaptability across diverse time series contexts. In response, this paper introduces a novel approach that employs a stacked transformer encoder architecture combined with learnable positional embeddings. By using separate encoders for time and feature dimensions, the model enhances its ability to represent multivariate time series data more comprehensively... the integration of fixed and learnable positional embeddings offers a versatile, context-sensitive method for encoding positional information... Rigorous evaluations on datasets such as SMD, SMAP, MSL, SWaT, and WADI demonstrate that our approach significantly outperforms baseline and state-of-the-art models...
# Literature Review Matrix: Foundational Papers

## 1. Detecting Large-Scale System Problems by Mining Console Logs
**Author:** Wei Xu, Ling Huang, Armando Fox, David Patterson, Michael I. Jordan
**Title:** Detecting Large-Scale System Problems by Mining Console Logs
**Year:** 2009
**Venue:** SOSP'09
**Problem Solved / Identified:** Console logs rarely help operators detect problems in large-scale datacenter services because they consist of voluminous intermixing of messages from many software components. Existing rule-based or keyword search methods are insufficient.
**Methodology:** The authors propose a general methodology to parse console logs by combining source code analysis with information retrieval to create composite features (state ratio vectors, message count vectors). These features are then analyzed using machine learning (PCA) to detect operational problems. The results are distilled into an operator-friendly decision tree.
**Dataset used:** Darkstar online game server (1,640,985 messages), Hadoop File System (HDFS) (24,396,061 messages).
**Results:** The method achieved high detection accuracy with very few false positives, successfully handling rare message types. The PCA anomaly detection was effective, and the decision tree provided necessary explainability.
**Limitations / Drawbacks:** The method cannot correctly handle all complex cases in source code analysis, requires access to the source code, and being an unsupervised method, it generates some false positives.
**Research Gaps:** Investigating semi-supervised learning techniques that can take operator feedback, extracting log templates from program binaries instead of source code, online detection instead of postmortem analysis, and correlating logs from multiple related applications.
**Abstract:** Surprisingly, console logs rarely help operators detect problems in large-scale datacenter services, for they often consist of the voluminous intermixing of messages from many software components written by independent developers. We propose a general methodology to mine this rich source of information to automatically detect system runtime problems. We first parse console logs by combining source code analysis with information retrieval to create composite features. We then analyze these features using machine learning to detect operational problems. We show that our method enables analyses that are impossible with previous methods because of its superior ability to create sophisticated features. We also show how to distill the results of our analysis to an operator-friendly one-page decision tree showing the critical messages associated with the detected problems. We validate our approach using the Darkstar online game server and the Hadoop File System, where we detect numerous real problems with high accuracy and few false positives. In the Hadoop case, we are able to analyze 24 million lines of console logs in 3 minutes. Our methodology works on textual console logs of any size and requires no changes to the service software, no human input, and no knowledge of the software's internals.

---

## 2. River: machine learning for streaming data in Python
**Author:** Jacob Montiel, Max Halford, Saulo Martiello Mastelini, Geoffrey Bolmier, Raphael Sourty, Robin Vaysse, Adil Zouitine, Heitor Murilo Gomes, Jesse Read, Talel Abdessalem, Albert Bifet
**Title:** River: machine learning for streaming data in Python
**Year:** 2021
**Venue:** Journal of Machine Learning Research
**Problem Solved / Identified:** The need for a unified, comprehensive, and efficient machine learning library for dynamic data streams and continual learning in Python.
**Methodology:** The paper introduces River, a merger of two popular packages for stream learning: Creme and scikit-multiflow. River uses dictionaries for efficient one-dimensional data storage and provides a revamped architecture supporting pipelines, instance-incremental, and batch-incremental learning.
**Dataset used:** Elec2 data set (for benchmarking).
**Results:** River models perform at least as fast but overall faster than equivalent scikit-learn batch implementations. It provides a flexible and easy-to-use API for streaming data.
**Limitations / Drawbacks:** As a library introduction paper, it does not explicitly outline algorithmic limitations, but acknowledges that processing time can be affected by the size of the data to store.
**Research Gaps:** Proposing a canonical way to deploy online models in production environments.
**Abstract:** River is a machine learning library for dynamic data streams and continual learning. It provides multiple state-of-the-art learning methods, data generators/transformers, performance metrics and evaluators for different stream learning problems. It is the result from the merger of two popular packages for stream learning in Python: Creme and scikit-multiflow. River introduces a revamped architecture based on the lessons learnt from the seminal packages. River's ambition is to be the go-to library for doing machine learning on streaming data. Additionally, this open source package brings under the same umbrella a large community of practitioners and researchers.

---

## 3. A Survey on Concept Drift Adaptation
**Author:** Joao Gama, Indre Zliobaite, Albert Bifet, Mykola Pechenizkiy, Abdelhamid Bouchachia
**Title:** A Survey on Concept Drift Adaptation
**Year:** 2014
**Venue:** ACM Computing Surveys
**Problem Solved / Identified:** The phenomenon of concept drift in dynamically changing and nonstationary environments. There was a strong need for a comprehensive summary of research to unify concepts and terminology among researchers and to survey state-of-the-art methodologies.
**Methodology:** A comprehensive literature survey that proposes a new taxonomy for adaptive algorithms. The taxonomy is structured around four main modules: memory, change detection, learning, and loss estimation.
**Dataset used:** N/A (Survey paper).
**Results:** Provided an integrated view on handling concept drift, characterizing adaptive learning algorithms, presenting evaluation methodologies, and discussing illustrative applications.
**Limitations / Drawbacks:** N/A (Survey paper).
**Research Gaps:** Improving scalability, robustness, and reliability; moving from black-box adaptation to more interpretable and explainable adaptation; reducing the dependence on timely and accurate feedback; moving toward adaptive systems that automate the full knowledge discovery process; studying how to integrate expert knowledge.
**Abstract:** Concept drift primarily refers to an online supervised learning scenario when the relation between the input data and the target variable changes over time. Assuming a general knowledge of supervised learning in this article, we characterize adaptive learning processes; categorize existing strategies for handling concept drift; overview the most representative, distinct, and popular techniques and algorithms; discuss evaluation methodology of adaptive algorithms; and present a set of illustrative applications. The survey covers the different facets of concept drift in an integrated way to reflect on the existing scattered state of the art. Thus, it aims at providing a comprehensive introduction to the concept drift adaptation for researchers, industry analysts, and practitioners.

---

## 4. "Why Should I Trust You?" Explaining the Predictions of Any Classifier
**Author:** Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin
**Title:** "Why Should I Trust You?" Explaining the Predictions of Any Classifier
**Year:** 2016
**Venue:** KDD 2016
**Problem Solved / Identified:** Machine learning models remain mostly black boxes. Understanding the reasons behind predictions is important in assessing trust, but many complex models lack interpretability.
**Methodology:** The authors propose LIME (Local Interpretable Model-agnostic Explanations), an algorithm that explains predictions of any classifier in a faithful way by approximating it locally with an interpretable model (like sparse linear models). They also propose SP-LIME, a method that selects a set of representative instances with explanations using submodular optimization to evaluate trust in the model as a whole.
**Dataset used:** Books and DVDs (sentiment analysis), 20 newsgroups dataset, images (Wolves vs. Eskimo Dogs).
**Results:** LIME provides faithful explanations. Simulated and human subject experiments showed that LIME helps users decide which classifier generalizes better, aids non-experts in performing feature engineering to improve models, and helps identify when and why a classifier should not be trusted.
**Limitations / Drawbacks:** The choice of interpretable representations has inherent drawbacks. If the underlying model is highly non-linear even in the locality of the prediction, there may not be a faithful linear explanation.
**Research Gaps:** Exploring a variety of explanation families (such as decision trees), performing the pick step for images, and investigating potential uses in speech, video, medical domains, and recommendation systems.
**Abstract:** Despite widespread adoption, machine learning models remain mostly black boxes. Understanding the reasons behind predictions is, however, quite important in assessing trust, which is fundamental if one plans to take action based on a prediction, or when choosing whether to deploy a new model. Such understanding also provides insights into the model, which can be used to transform an untrustworthy model or prediction into a trustworthy one. In this work, we propose LIME, a novel explanation technique that explains the predictions of any classifier in an interpretable and faithful manner, by learning an interpretable model locally around the prediction. We also propose a method to explain models by presenting representative individual predictions and their explanations in a non-redundant way, framing the task as a submodular optimization problem. We demonstrate the flexibility of these methods by explaining different models for text (e.g. random forests) and image classification (e.g. neural networks). We show the utility of explanations via novel experiments, both simulated and with human subjects, on various scenarios that require trust: deciding if one should trust a prediction, choosing between models, improving an untrustworthy classifier, and identifying why a classifier should not be trusted.

---

## 5. DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning
**Author:** Min Du, Feifei Li, Guineng Zheng, Vivek Srikumar
**Title:** DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning
**Year:** 2017
**Venue:** CCS'17
**Problem Solved / Identified:** Online anomaly detection from massive system logs is challenging. Existing methods (PCA, Invariant Mining) cannot effectively guard against different attacks online, often relying only on log keys and ignoring parameters, or failing to capture complex interleaving execution paths.
**Methodology:** Proposes DeepLog, a deep neural network model utilizing Long Short-Term Memory (LSTM). It treats system logs as a natural language sequence to learn log patterns from normal execution and detects anomalies when incoming logs deviate from the trained model. DeepLog incrementally updates weights online using user feedback. It also constructs workflow models for anomaly diagnosis. It models both execution path anomalies (via log keys) and parameter value anomalies (via multi-variate time series).
**Dataset used:** HDFS log data set, OpenStack log data set, Blue Gene/L supercomputer system logs, VAST Challenge 2011 network security log.
**Results:** DeepLog significantly outperformed existing log-based anomaly detection methods (PCA, IM), achieving an F-measure of 96% on HDFS. It effectively detects execution path anomalies and parameter value anomalies, and the workflow construction aids in diagnosis.
**Limitations / Drawbacks:** Requires a small fraction of normal log entries to train its model. Parameter tuning is required depending on the problem.
**Research Gaps:** Incorporating other types of RNNs into DeepLog to test their efficiency, and integrating log data from different applications and systems to perform more comprehensive system diagnosis.
**Abstract:** Anomaly detection is a critical step towards building a secure and trustworthy system. The primary purpose of a system log is to record system states and significant events at various critical points to help debug system failures and perform root cause analysis. Such log data is universally available in nearly all computer systems. Log data is an important and valuable resource for understanding system status and performance issues; therefore, the various system logs are naturally excellent source of information for online monitoring and anomaly detection. We propose DeepLog, a deep neural network model utilizing Long Short-Term Memory (LSTM), to model a system log as a natural language sequence. This allows DeepLog to automatically learn log patterns from normal execution, and detect anomalies when log patterns deviate from the model trained from log data under normal execution. In addition, we demonstrate how to incrementally update the DeepLog model in an online fashion so that it can adapt to new log patterns over time. Furthermore, DeepLog constructs workflows from the underlying system log so that once an anomaly is detected, users can diagnose the detected anomaly and perform root cause analysis effectively. Extensive experimental evaluations over large log data have shown that DeepLog has outperformed other existing log-based anomaly detection methods based on traditional data mining methodologies.

---

## 6. Robust Log-Based Anomaly Detection on Unstable Log Data
**Author:** Xu Zhang, Yong Xu, Qingwei Lin, Bo Qiao, Hongyu Zhang, Yingnong Dang, Chunyu Xie, Xinsheng Yang, Qian Cheng, Ze Li, Junjie Chen, Xiaoting He, Randolph Yao, Jian-Guang Lou, Murali Chintalapati, Furao Shen, Dongmei Zhang
**Title:** Robust Log-Based Anomaly Detection on Unstable Log Data
**Year:** 2019
**Venue:** ESEC/FSE'19
**Problem Solved / Identified:** Existing log-based anomaly detection methods rely on a close-world assumption (stable log data and known distinct log events). However, real-world log data is unstable due to the evolution of logging statements and processing noise, which significantly hampers the effectiveness of existing approaches.
**Methodology:** The authors propose LogRobust. It extracts semantic information of log events and represents them as fixed-dimension semantic vectors using pre-trained FastText word vectors and TF-IDF weighting. It then utilizes an attention-based Bi-LSTM model to capture contextual information and learn the importance of different log events for anomaly detection.
**Dataset used:** HDFS dataset (original and synthetic unstable versions), and a real-world industrial dataset (Service X) from Microsoft.
**Results:** LogRobust successfully addresses the problem of log instability. It achieves accurate and robust results on both stable and unstable log data, significantly outperforming traditional methods (LR, SVM, IM, PCA) on the unstable Service X dataset (F1-score of 0.81 vs ~0.52).
**Limitations / Drawbacks:** Sudden, drastic changes to the entire code base or logging mechanism would drop performance if the model is not incrementally updated. The synthetic data creation only considers some common types of changes.
**Research Gaps:** Experimenting with LogRobust on a wider variety of datasets and exploring other possible types of changes in real-world systems.
**Abstract:** Logs are widely used by large and complex software-intensive systems for troubleshooting. There have been a lot of studies on log-based anomaly detection. To detect the anomalies, the existing methods mainly construct a detection model using log event data extracted from historical logs. However, we find that the existing methods do not work well in practice. These methods have the close-world assumption, which assumes that the log data is stable over time and the set of distinct log events is known. However, our empirical study shows that in practice, log data often contains previously unseen log events or log sequences. The instability of log data comes from two sources: 1) the evolution of logging statements, and 2) the processing noise in log data. In this paper, we propose a new log-based anomaly detection approach, called LogRobust. LogRobust extracts semantic information of log events and represents them as semantic vectors. It then detects anomalies by utilizing an attention-based Bi-LSTM model, which has the ability to capture the contextual information in the log sequences and automatically learn the importance of different log events. In this way, LogRobust is able to identify and handle unstable log events and sequences. We have evaluated LogRobust using logs collected from the Hadoop system and an actual online service system of Microsoft. The experimental results show that the proposed approach can well address the problem of log instability and achieve accurate and robust results on real-world, ever-changing log data.

---

## 7. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks
**Author:** Nils Reimers, Iryna Gurevych
**Title:** Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks
**Year:** 2019
**Venue:** EMNLP-IJCNLP 2019
**Problem Solved / Identified:** BERT and RoBERTa require both sentences to be fed into the network to compute similarity, causing a massive computational overhead and making them unsuitable for large-scale semantic similarity comparison, clustering, and information retrieval.
**Methodology:** Proposes Sentence-BERT (SBERT), a modification of the pretrained BERT network using siamese and triplet network structures. It adds a pooling operation to the output of BERT to derive fixed-sized, semantically meaningful sentence embeddings that can be efficiently compared using cosine-similarity.
**Dataset used:** SNLI, Multi-Genre NLI, various Semantic Textual Similarity (STS) tasks/datasets, Argument Facet Similarity (AFS) corpus, Wikipedia sections triplets, SentEval transfer tasks.
**Results:** SBERT reduces the time to find the most similar pair in 10,000 sentences from 65 hours to about 5 seconds. It outperforms other state-of-the-art sentence embedding methods on STS tasks and transfer learning tasks.
**Limitations / Drawbacks:** Average BERT embeddings or CLS-token outputs alone yield poor sentence embeddings for cosine-similarity compared to SBERT.
**Research Gaps:** N/A
**Abstract:** BERT (Devlin et al., 2018) and RoBERTa (Liu et al., 2019) has set a new state-of-the-art performance on sentence-pair regression tasks like semantic textual similarity (STS). However, it requires that both sentences are fed into the network, which causes a massive computational overhead: Finding the most similar pair in a collection of 10,000 sentences requires about 50 million inference computations (~65 hours) with BERT. The construction of BERT makes it unsuitable for semantic similarity search as well as for unsupervised tasks like clustering. In this publication, we present Sentence-BERT (SBERT), a modification of the pretrained BERT network that use siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity. This reduces the effort for finding the most similar pair from 65 hours with BERT / RoBERTa to about 5 seconds with SBERT, while maintaining the accuracy from BERT. We evaluate SBERT and SRoBERTa on common STS tasks and transfer learning tasks, where it outperforms other state-of-the-art sentence embeddings methods.

---

## 8. Attention is not Explanation
**Author:** Sarthak Jain, Byron C. Wallace
**Title:** Attention is not Explanation
**Year:** 2019
**Venue:** NAACL-HLT 2019
**Problem Solved / Identified:** Attention mechanisms in neural NLP models are often touted as affording transparency and providing meaningful "explanations" for predictions. The paper investigates whether this assumption holds.
**Methodology:** The authors perform extensive empirical experiments across various NLP tasks to assess the relationship between attention weights, inputs, and outputs. They measure the correlation between attention weights and gradient-based/leave-one-out measures of feature importance. They also generate counterfactual and adversarial attention distributions that yield equivalent predictions.
**Dataset used:** Stanford Sentiment Treebank (SST), IMDB, Twitter Adverse Drug Reaction (ADR), 20 Newsgroups, AG News, MIMIC ICD9 (Diabetes, Anemia), CNN News Articles, bAbI, SNLI.
**Results:** Learned attention weights are frequently uncorrelated with gradient-based measures of feature importance. Furthermore, very different (adversarial) attention distributions can often be identified that nonetheless yield equivalent predictions. Standard attention modules do not provide meaningful explanations.
**Limitations / Drawbacks:** The evaluation is limited to specific types of attention mechanisms (Additive and Scaled Dot-Product) with RNN/CNN encoders and primarily unstructured output spaces (classification, QA, NLI). Sequence-to-sequence tasks were not considered.
**Research Gaps:** Exploring explicit 'high precision' signals in text. Motivating the development of principled attention mechanisms or variants designed explicitly for interpretability.
**Abstract:** Attention mechanisms have seen wide adoption in neural NLP models. In addition to improving predictive performance, these are often touted as affording transparency: models equipped with attention provide a distribution over attended-to input units, and this is often presented (at least implicitly) as communicating the relative importance of inputs. However, it is unclear what relationship exists between attention weights and model outputs. In this work we perform extensive experiments across a variety of NLP tasks that aim to assess the degree to which attention weights provide meaningful "explanations" for predictions. We find that they largely do not. For example, learned attention weights are frequently uncorrelated with gradient-based measures of feature importance, and one can identify very different attention distributions that nonetheless yield equivalent predictions. Our findings show that standard attention modules do not provide meaningful explanations and should not be treated as though they do.

---

## 9. Distributed Representations of Words and Phrases and their Compositionality
**Author:** Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, Jeffrey Dean
**Title:** Distributed Representations of Words and Phrases and their Compositionality
**Year:** 2013
**Venue:** NIPS 2013
**Problem Solved / Identified:** Word representations are indifferent to word order and unable to represent idiomatic phrases. Training the Skip-gram model can also be optimized for speed and quality of infrequent words.
**Methodology:** Proposes several extensions to the continuous Skip-gram model: subsampling of frequent words to speed up training and improve representations of less frequent words; using Negative Sampling (a simplified variant of Noise Contrastive Estimation) instead of hierarchical softmax; and a simple data-driven approach based on unigram and bigram counts to find and represent phrases as single tokens.
**Dataset used:** Internal Google dataset with one billion words (for words) and 33 billion words (for phrases). Analogical reasoning task dataset.
**Results:** Subsampling frequent words results in a 2x-10x speedup and better representations. Negative Sampling is an extremely simple and accurate training method. The learned word and phrase representations exhibit linear structures that make precise analogical reasoning possible, allowing words and phrases to be meaningfully combined by element-wise addition.
**Limitations / Drawbacks:** The approach for learning representations of phrases simply represents phrases with a single token, which might not be as expressive for very long pieces of text compared to recursive operations.
**Research Gaps:** Complementing the proposed approach with techniques that attempt to represent phrases using recursive matrix-vector operations.
**Abstract:** The recently introduced continuous Skip-gram model is an efficient method for learning high-quality distributed vector representations that capture a large number of precise syntactic and semantic word relationships. In this paper we present several extensions that improve both the quality of the vectors and the training speed. By subsampling of the frequent words we obtain significant speedup and also learn more regular word representations. We also describe a simple alternative to the hierarchical softmax called negative sampling. An inherent limitation of word representations is their indifference to word order and their inability to represent idiomatic phrases. For example, the meanings of "Canada" and "Air" cannot be easily combined to obtain "Air Canada". Motivated by this example, we present a simple method for finding phrases in text, and show that learning good vector representations for millions of phrases is possible.

---

## 10. A Unified Approach to Interpreting Model Predictions
**Author:** Scott M. Lundberg, Su-In Lee
**Title:** A Unified Approach to Interpreting Model Predictions
**Year:** 2017
**Venue:** NIPS 2017
**Problem Solved / Identified:** Various methods exist to help users interpret the predictions of complex models, but it is often unclear how these methods are related and when one method is preferable over another.
**Methodology:** Presents SHAP (SHapley Additive exPlanations), a unified framework for interpreting predictions. It defines a class of "additive feature attribution methods" and proves there is a unique solution in this class satisfying three desirable properties (local accuracy, missingness, and consistency), which corresponds to Shapley values. The paper unifies LIME, DeepLIFT, Layer-Wise Relevance Propagation, and other methods. Proposes Kernel SHAP and Deep SHAP for efficient estimation.
**Dataset used:** Simulated experiments, Amazon Mechanical Turk user studies, MNIST digit image classification dataset.
**Results:** SHAP values provide a unique and consistent measure of feature importance. SHAP methods are better aligned with human intuition than existing methods and more effectually discriminate among model output classes.
**Limitations / Drawbacks:** Exact computation of SHAP values is challenging and requires approximations.
**Research Gaps:** Developing faster model-type-specific estimation methods that make fewer assumptions, integrating work on estimating interaction effects from game theory, and defining new explanation model classes.
**Abstract:** Understanding why a model makes a certain prediction can be as crucial as the prediction's accuracy in many applications. However, the highest accuracy for large modern datasets is often achieved by complex models that even experts struggle to interpret, such as ensemble or deep learning models, creating a tension between accuracy and interpretability. In response, various methods have recently been proposed to help users interpret the predictions of complex models, but it is often unclear how these methods are related and when one method is preferable over another. To address this problem, we present a unified framework for interpreting predictions, SHAP (SHapley Additive exPlanations). SHAP assigns each feature an importance value for a particular prediction. Its novel components include: (1) the identification of a new class of additive feature importance measures, and (2) theoretical results showing there is a unique solution in this class with a set of desirable properties. The new class unifies six existing methods, notable because several recent methods in the class lack the proposed desirable properties. Based on insights from this unification, we present new methods that show improved computational performance and/or better consistency with human intuition than previous approaches.

---

## 11. Attention Is All You Need
**Author:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
**Title:** Attention Is All You Need
**Year:** 2017
**Venue:** NIPS 2017
**Problem Solved / Identified:** Sequential computation in recurrent neural networks (RNNs) and convolutional neural networks precludes parallelization within training examples, which is critical for long sequences.
**Methodology:** Proposes the Transformer, a novel network architecture based solely on attention mechanisms (Multi-Head Self-Attention), completely dispensing with recurrence and convolutions.
**Dataset used:** WMT 2014 English-to-German and English-to-French translation datasets.
**Results:** The Transformer establishes a new state-of-the-art on both translation tasks (28.4 BLEU for EN-DE, 41.0 BLEU for EN-FR), offering superior translation quality. It is highly parallelizable, requiring significantly less time to train compared to recurrent/convolutional models.
**Limitations / Drawbacks:** Self-attention can be computationally expensive for very long sequences because its complexity scales quadratically with sequence length.
**Research Gaps:** Extending the Transformer to problems involving input and output modalities other than text (images, audio, video). Investigating local, restricted attention mechanisms to efficiently handle large inputs. Making generation less sequential.
**Abstract:** The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.

---

## 12. Learning from Time-Changing Data with Adaptive Windowing
**Author:** Albert Bifet, Ricard Gavalda
**Title:** Learning from Time-Changing Data with Adaptive Windowing
**Year:** 2006 (or 2007)
**Venue:** SIAM International Conference on Data Mining (SDM)
**Problem Solved / Identified:** Dealing with distribution change and concept drift when learning from data sequences that vary with time, eliminating the need for the user to guess a priori the time-scale of change.
**Methodology:** Presents ADWIN (ADaptive WINdowing), an algorithm that maintains a sliding window whose size is recomputed online according to the rate of change observed. The window grows when data is stationary and shrinks when change occurs. A time- and memory-efficient version, ADWIN2, is also proposed. The algorithm is combined with Naive Bayes and k-means clustering.
**Dataset used:** Synthetic data streams (triangular wavelets, square wavelets, staircase wavelets, k-gaussian distributions) and the Electricity Market Dataset.
**Results:** ADWIN provides rigorous guarantees of performance (bounds on false positives/negatives) and automatically adjusts the window size to the optimal balance point. It outperforms fixed-size window strategies.
**Limitations / Drawbacks:** The method relies on a user-specified confidence parameter $\delta$.
**Research Gaps:** Thorough experimentation with more real-world datasets and combining the method with other learning algorithms, such as decision-tree induction methods.
**Abstract:** We present a new approach for dealing with distribution change and concept drift when learning from data sequences that may vary with time. We use sliding windows whose size, instead of being fixed a priori, is recomputed online according to the rate of change observed from the data in the window itself: The window will grow automatically when the data is stationary, for greater accuracy, and will shrink automatically when change is taking place, to discard stale data. This delivers the user or programmer from having to guess a time-scale for change. Contrary to many related works, we provide rigorous guarantees of performance, as bounds on the rates of false positives and false negatives. In fact, for some change structures, we can formally show that the algorithm automatically adjusts the window to a statistically optimal length. Using ideas from data stream algorithmics, we develop a time- and memory-efficient version of this algorithm, called ADWIN2. We show how to incorporate this strategy easily into two learning algorithms, the Naive Bayes predictor and the k-means clusterer, chosen since it is relatively easy to observe their behaviour under time change. We combine ADWIN2 with the Naive Bayes (NB) predictor, in two ways: one, using it to monitor the error rate of the current model and declare when revision is necessary and, two, putting it inside the NB predictor to maintain up-to-date estimations of conditional probabilities in the data. We test our approach using synthetic and real data streams and compare them to both fixed-size and variable-size window strategies with good results.

---

## 13. On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation
**Author:** Sebastian Bach, Alexander Binder, Gregoire Montavon, Frederick Klauschen, Klaus-Robert Muller, Wojciech Samek
**Title:** On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation
**Year:** 2015
**Venue:** PLoS ONE
**Problem Solved / Identified:** Machine learning methods (like deep networks and non-linear SVMs) often act as black boxes. There is a need to understand and interpret classification decisions by tracing them back to the input pixels.
**Methodology:** The authors propose Layer-Wise Relevance Propagation (LRP), a methodology that decomposes the classification output of non-linear classifiers into pixel-wise relevance scores. The method works by applying a propagation rule that distributes class relevance found at a given layer onto the previous layer, backward from the output to the input.
**Dataset used:** PASCAL VOC 2009 images, synthetic image data containing geometric shapes, MNIST handwritten digits, and the ILSVRC ImageNet data.
**Results:** LRP successfully visualizes the contributions of single pixels to predictions, providing informative heatmaps. It works for kernel-based classifiers over Bag of Words features and multilayered neural networks, allowing experts to verify reasoning and identify data artifacts.
**Limitations / Drawbacks:** Evaluating the quality of a heatmap beyond simple visual assessment is difficult, and the greediness of the layer-wise procedure might encounter dead-ends in lower layers.
**Research Gaps:** Exploring the mathematical properties of the propagation methods, investigating the greediness of the procedure, and proposing a universal metric for quantifying heatmap quality beyond human assessment.
**Abstract:** Understanding and interpreting classification decisions of automated image classification systems is of high value in many applications, as it allows to verify the reasoning of the system and provides additional information to the human expert. Although machine learning methods are solving very successfully a plethora of tasks, they have in most cases the disadvantage of acting as a black box, not providing any information about what made them arrive at a particular decision. This work proposes a general solution to the problem of understanding classification decisions by pixel-wise decomposition of nonlinear classifiers. We introduce a methodology that allows to visualize the contributions of single pixels to predictions for kernel-based classifiers over Bag of Words features and for multilayered neural networks. These pixel contributions can be visualized as heatmaps and are provided to a human expert who can intuitively not only verify the validity of the classification decision, but also focus further analysis on regions of potential interest. We evaluate our method for classifiers trained on PASCAL VOC 2009 images, synthetic image data containing geometric shapes, the MNIST handwritten digits data set and for the pre-trained ImageNet model available as part of the Caffe open source package.

---

## 14. HitAnomaly: Hierarchical Transformers for Anomaly Detection in System Log
**Author:** Shaohan Huang, Yi Liu, Carol Fung, Rong He, Yining Zhao, Hailong Yang, Zhongzhi Luan
**Title:** HitAnomaly: Hierarchical Transformers for Anomaly Detection in System Log
**Year:** 2020
**Venue:** IEEE Transactions on Network and Service Management
**Problem Solved / Identified:** Existing log-based anomaly detection methods primarily use log event indexes, which fail to handle unseen log templates. Methods that do use semantics often ignore the information contained within log parameter values.
**Methodology:** Proposes HitAnomaly, an anomaly detection model utilizing a hierarchical transformer structure to model both log template sequences and parameter values. It includes a log sequence encoder and a parameter value encoder to obtain representations, which are then fed into an attention mechanism for the final classification.
**Dataset used:** HDFS dataset, BGL dataset, OpenStack dataset.
**Results:** HitAnomaly effectively captures semantic information in both template sequences and parameter values. It outperformed existing methods (PCA, IM, LogCluster, SVM, LR, DeepLog, LogRobust) on both stable and unstable log data sets, demonstrating robustness to unseen log events.
**Limitations / Drawbacks:** The model requires a longer prediction time compared to classic machine learning models due to the complexity of the transformer structure.
**Research Gaps:** Incorporating the transformer structure into a log-based anomaly prediction task (predicting anomalies before they occur).
**Abstract:** Enterprise systems often produce a large volume of logs to record runtime status and events. Anomaly detection from system logs is crucial for service management and system maintenance. Most existing log-based anomaly detection methods use log event indexes parsed from log data to detect anomalies. Those methods cannot handle unseen log templates and lead to inaccurate anomaly detection. Some recent studies focused on the semantics of log templates but ignored the information of parameter values. Therefore, their approaches failed to address the abnormal logs caused by parameter values. In this article, we propose HitAnomaly, a log-based anomaly detection model utilizing a hierarchical transformer structure to model both log template sequences and parameter values. We designed a log sequence encoder and a parameter value encoder to obtain their representations correspondingly. We then use an attention mechanism as our final classification model. In this way, HitAnomaly is able to capture the semantic information in both log template sequence and parameter values and handle various types of anomalies. We evaluated our proposed method on three log datasets. Our experimental results demonstrate that HitAnomaly has outperformed other existing log-based anomaly detection methods. We also assess the robustness of our proposed model on unstable log data.

---

## 15. LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs
**Author:** Weibin Meng, Ying Liu, Yichen Zhu, Shenglin Zhang, Dan Pei, Yuqing Liu, Yihao Chen, Ruizhi Zhang, Shimin Tao, Pei Sun, Rong Zhou
**Title:** LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs
**Year:** 2019
**Venue:** IJCAI 2019
**Problem Solved / Identified:** Existing log anomaly detection approaches use indexes rather than semantics, leading to false alarms, especially when new log templates appear between periodic retrainings. Existing methods also typically detect either sequential or quantitative anomalies, but not both simultaneously.
**Methodology:** Proposes LogAnomaly, a framework that models a log stream as a natural language sequence. Introduces `template2vec` to extract semantic information from log templates by considering synonyms and antonyms. It utilizes an LSTM network to automatically detect both sequential and quantitative anomalies. The method also introduces template approximation to handle newly appearing log templates.
**Dataset used:** HDFS dataset, BGL dataset.
**Results:** LogAnomaly outperforms state-of-the-art log-based anomaly detection methods (LogCluster, PCA, Invariant Mining, DeepLog) in terms of accuracy, precision, and recall. It successfully avoids false alarms caused by newly appearing log templates.
**Limitations / Drawbacks:** As an unsupervised method, it relies heavily on the quality of the log parsing and the representational power of the semantic vectors to correctly distinguish normal from abnormal.
**Research Gaps:** Not explicitly outlined in the paper's conclusion, but general gaps imply the need for better handling of parameter values (addressed in later works like HitAnomaly).
**Abstract:** Recording runtime status via logs is common for almost computer system, and detecting anomalies in logs is crucial for timely identifying malfunctions of systems. However, manually detecting anomalies for logs is time-consuming, error-prone, and infeasible. Existing automatic log anomaly detection approaches, using indexes rather than semantics of log templates, tend to cause false alarms. In this work, we propose LogAnomaly, a framework to model a log stream as a natural language sequence. Empowered by template2vec, a novel, simple yet effective method to extract the semantic information hidden in log templates, LogAnomaly can detect both sequential and quantitive log anomalies simultaneously, which has not been done by any previous work. Moreover, LogAnomaly can avoid the false alarms caused by the newly appearing log templates between periodic model retrainings. Our evaluation on two public production log datasets show that LogAnomaly outperforms existing log-based anomaly detection methods.
# Literature Review Matrix: Modern Competitors in Log Anomaly Detection

| Author, Title, Year | Venue | Problem Solved / Identified | Methodology | Dataset used | Results | Limitations / Drawbacks | Research Gaps | Abstract |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Zhuangbin Chen et al.**<br>*Experience Report: Deep Learning-based System Log Analysis for Anomaly Detection*<br>(2021/2022) | arXiv / ICSE '22 (Woodstock '18 template) | Lack of rigorous comparison among representative DL log anomaly detectors; difficult re-implementation and gap between academia and industry. | Comprehensive review and evaluation of 5 popular neural networks used by 6 state-of-the-art methods (DeepLog, LogAnomaly, Logsy, Autoencoder, LogRobust, CNN). Re-implemented as an open-source toolkit. | HDFS, BGL | Supervised methods perform better than unsupervised. Semantic features improve robustness against unseen logs. Anomalies in training data deteriorate forecasting-based methods' performance, but reconstruction-based methods are more resistant. | Industrial deployment challenges: high complexity, threshold re-determination, concept drift, large-volume/low-quality data, and unsatisfactory interpretability. | Need for closer engineering collaboration, better logging practices, and model improvement (online learning, multi-source learning). | Logs have been an imperative resource... we provide a comprehensive review and evaluation of five popular neural networks used by six state-of-the-art methods... |
| **Hongcheng Guo et al.**<br>*TRANSLOG: A Unified Transformer-based Framework for Log Anomaly Detection*<br>(2022) | arXiv | Retraining the whole network for unknown domains is inefficient, especially for low-resource domains. Previous models focus on extracting semantics in the same domain, leading to poor generalization. | TRANSLOG, a unified Transformer-based framework comprising pretraining and adapter-based tuning stages. Model is pretrained on a source domain to obtain shared semantic knowledge, then transferred to target domains via adapter-based tuning. | HDFS, BGL, Thunderbird | Achieves state-of-the-art performance on three benchmarks with fewer trainable parameters and lower training costs. Adapter-based tuning outperforms training from scratch and fine-tuning. | Relies on a large source domain for pretraining; potential adapter tuning overhead. | Semantic migration between log sources for unified multiple sources detection. | Log anomaly detection is a key component... propose a unified Transformer-based framework for Log anomaly detection (TRANSLOG)... pretrained on the source domain... adapter-based tuning. |
| **Runqiang Zang et al.**<br>*MLAD: A Unified Model for Multi-system Log Anomaly Detection*<br>(2024) | arXiv | Current models need specific training for individual systems, leading to high costs and limited scalability. Lack of cognitive reasoning capabilities makes transferability hard. "Identical shortcut" problem in reconstruction networks. | MLAD incorporates semantic relational reasoning across multiple systems. Uses Sentence-BERT to capture similarities and converts them to learnable semantic vectors. Revamps Attention layer formulas (sparsemax/Tsallis entmax) and employs a Gaussian Mixture Model (GMM) to handle rare words. | BGL, HDFS, Thunderbird | Significantly improves performance relative to baselines. Resolves "identical shortcut" problem, separates abnormal samples better, and demonstrates robust transfer learning capability between systems. | Struggles slightly with low-frequency keywords without the GMM component. | Explicitly learning short-distance relationships between similar samples and long-distance relationships between normal/abnormal samples. | In spite of rapid advancements... propose MLAD, a novel anomaly detection model... employs Sentence-bert... revamp Attention layer... Gaussian mixture model. |
| **Wei Guan et al.**<br>*LogLLM: Log-based Anomaly Detection Using Large Language Models*<br>(2024/2025) | arXiv | Traditional DL methods struggle to capture semantic info in logs. Existing LLM-based methods face challenges like limited semantic understanding, suboptimal LLM utilization, and memory overflow due to long input. | LogLLM uses BERT for extracting semantic vectors from log messages and Llama for classifying log sequences. A projector aligns BERT and Llama spaces. Uses regex instead of log parsers. Three-stage training procedure (fine-tuning Llama, training embedder, fine-tuning entire model). | HDFS, BGL, Liberty, Thunderbird | Outperforms state-of-the-art methods with the highest F1-score across datasets. Solves OOM issue by using BERT to summarize logs before feeding into Llama. | Needs labeled data for minority class oversampling. High computational cost and training time compared to simpler models. | Impact of log instability and imbalanced classes on LLM performance. | Software systems often record important runtime information in logs... propose LogLLM... employs BERT for extracting semantic vectors... Llama for classifying log sequences... three-stage procedure. |
| **Jiawei Lu, Chengrong Wu**<br>*TPLogAD: Unsupervised Log Anomaly Detection Based on Event Templates and Key Parameters*<br>(2024) | arXiv | Existing methods use indexes or fixed string embeddings, ignoring rich semantic and structural info in parameters, leading to semantic loss and parameter abandonment. | TPLogAD uses event templates and key parameters. Proposes itemplate2vec (to extract semantic info from templates) and para2vec (to extract info from five types of parameters). Uses BiLSTM and an attention mechanism to learn semantics and associations. | BGL, HDFS, Thunderbird, Spirit | Outperforms existing log anomaly detection methods (DeepLog, LogAnomaly, etc.). Better precision and recall by using both templates and parameters. | Unsupervised approach relies heavily on clustering for parameter sequences, which may miss nuanced anomalies. | Joint modeling of event templates and parameters, and updating templates/parameters online to adapt to dynamic changes. | Log-system is an important mechanism... propose TPLogAD... performs anomaly detection based on event templates and key parameters... itemplate2vec and para2vec... BiLSTM and attention. |
| **Van-Hoang Le, Hongyu Zhang**<br>*Log-based Anomaly Detection with Deep Learning: How Far Are We?*<br>(2022) | ICSE '22 | DL models claim very high detection accuracy, but important aspects are overlooked (training data selection, data grouping, class distribution, data noise, early detection ability). | Systematic evaluation of 5 representative DL models (DeepLog, LogAnomaly, PLELog, LogRobust, CNN). Experiments focus on training data selection, data grouping, class distribution, data noise, and early detection ability. | HDFS, BGL, Spirit, Thunderbird | Training data selection strategies significantly impact semi-supervised models. Highly imbalanced data impedes performance. Small amount of noise/parsing errors downgrades performance. Forecasting models detect earlier. | Not proposing a new anomaly detection method; it is an empirical study. | Need for a variety of datasets, handling limited labeled data, improving early detection, and handling evolving systems. | Software-intensive systems produce logs... conduct an in-depth analysis of five state-of-the-art deep learning-based models... results point out that all these aspects have significant impact... |
| **Yanni Tang et al.**<br>*Unseen Anomaly Detection from System Logs*<br>(2026) | SIGMOD '26 | Most log anomaly detection methods assume anomalous patterns remain consistent. They fail to identify unseen anomalies introduced by software upgrades (anomaly shift). | UnseenLog framework formulates anomaly detection as node-level classification in a log graph. Uses MinMax strategy to select augmented anomaly samples and Recurrent Iterative Selection and Enhancement (RISE) to filter and incorporate pseudo-labeled anomalous samples. | Forum, Halo, Novel | Outperforms state-of-the-art baselines by at least 6% improvement in F1 score. Effective at detecting unseen anomalous code files. | Graph construction requires invocation relationships, which may not always be easily available. | Specifically addressing out-of-distribution (OOD) graph anomalies (unseen anomalies) and anomaly shifts. | Detecting anomalies in system logs effectively is crucial... propose UnseenLog, a novel log anomaly detection framework... MinMax strategy... Recurrent Iterative Selection and Enhancement (RISE). |
| **Liping Liao et al.**<br>*LogBASA: Log Anomaly Detection Based on System Behavior Analysis and Global Semantic Awareness*<br>(2023) | Int. J. of Intelligent Systems | Existing methods mostly consider only sequence patterns or semantic info, leading to high missed and false alarms. | LogBASA constructs a System Log Knowledge Graph (SLKG). Uses a self-attention encoder-decoder transformer for log spatiotemporal association analysis. Extracts spatial features using GCN and temporal features using MLP. Uses adaptive spatial boundary delineation and sequence reconstruction. | HDFS, BGL, Thunderbird | Accuracy rate of 99.3%, 95.1%, and 97.2% on HDFS, BGL, and Thunderbird datasets respectively. | Model complexity is high, leading to potentially longer training time than simpler models. | Combines spatial (GCN on execution path), temporal (MLP on time diffs), and semantic (BERT + Transformer) features for global awareness. | System log anomaly detection is important... proposed an unsupervised log anomaly detection model (LogBASA) based on the system behavior analysis and global semantic awareness... system log knowledge graph (SLKG)... |
| **M. Hariharan et al.**<br>*Detecting log anomaly using subword attention encoder and probabilistic feature selection*<br>(2023) | Applied Intelligence | Current log parsers cannot handle out-of-vocabulary (OOV) tokens effectively. Feature selection is rarely explored in log anomaly detection. | Proposes Subword Encoder Neural network (SEN) to learn semantic-aware embeddings from subword-level granularity using Byte-Pair Encoding + Self-attention. Develops Naive Bayes Feature Selector (NBFS) to extract useful log events. Applies supervised ML for classification. | BGL, HDFS, OpenStack | 0.99 detection F1-score on benchmarked datasets. Robust to OOV words. NBFS improves base classifier efficiency significantly. | Requires labelled data for NBFS and supervised ML. | Focuses on subword embeddings and probabilistic feature selection to improve separability of features for outlier tagging. | Log anomaly is a manifestation of a software system error... propose an enhanced approach to learning semantic-aware embeddings... Subword Encoder Neural network (SEN)... Naive Bayes Feature Selector (NBFS). |
| **Yiyong Chen et al.**<br>*LogLS: Research on System Log Anomaly Detection Method Based on Dual LSTM*<br>(2022) | Symmetry | Poor prediction performance of LSTM on long sequences. Methods usually only consider the impact of the pre-event on the current event while ignoring the post-sequence. | LogLS method based on dual LSTM with symmetric structure. Models logs according to preorder relationship and postorder relationship. Adds manual filtering step on top of Spell parser. Provides a feedback (renewal) mechanism to update the model. | HDFS, BGL | High accuracy (99.84% on HDFS). Outperforms PCA, IM, N-Gram, and DeepLog. The renewal mechanism improves F1-measure significantly when updating with false positives. | Manual filtering of log templates is required. Uses template indexes rather than semantic embeddings. | Exploiting bidirectional context (preorder and postorder) in sequence prediction and providing an update mechanism. | System logs record the status... propose LogLS, a system log anomaly detection method based on dual long short-term memory (LSTM) with symmetric structure... modeled the log according to the preorder relationship and postorder relationship. |
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
