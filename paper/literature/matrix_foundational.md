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
