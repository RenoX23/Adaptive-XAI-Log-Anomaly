# 3. Background & Problem Formulation

## 3.1 Log Parsing and Sequence Representation
Raw system logs are unstructured, free-text streams heavily interleaved by concurrent processes. To perform automated analysis, these raw strings must first be standardized into structured formats. This is typically achieved using automated log parsers like Drain \cite{he2017drain}, which apply fixed-depth parse trees to separate static template text (the structural behavior) from dynamic variables (e.g., timestamps, IP addresses). Each unique template is assigned an Event ID. 

Once parsed, the chronological stream of events is partitioned into finite sequences. In systems like HDFS, logs can be grouped explicitly by a unique `BlockId`, resulting in a variable-length sequence of events $S = [e_1, e_2, \dots, e_L]$ corresponding to a specific operational lifecycle. For systems without explicit identifiers, a sliding window of fixed length $L$ is employed. The anomaly detection objective is to design a mapping function $f(S) \rightarrow \{0, 1\}$, where $1$ denotes a structural or contextual deviation from normal execution patterns.

## 3.2 PCA Anomaly Detection
Principal Component Analysis (PCA) \cite{shlens2014tutorial} is a fundamental dimensionality reduction technique utilized extensively in early log anomaly detection. Given a matrix $X \in \mathbb{R}^{n \times d}$ representing $n$ normal log sequences encoded into $d$-dimensional count vectors, PCA computes the sample covariance matrix $\Sigma = \frac{1}{n} X^T X$. The matrix $\Sigma$ is diagonalized to extract the principal eigenvectors, forming a projection matrix $P \in \mathbb{R}^{d \times k}$ containing the top $k$ principal components that capture the majority of normal variance.

The residual (anomalous) variance is captured by the orthogonal complement projection matrix $C = I - P P^T$. For any new log sequence vector $x \in \mathbb{R}^d$, the anomaly score is defined as the Squared Prediction Error (SPE), or reconstruction error:
$$ y = x^T C x = x^T (I - P P^T) x $$

If the SPE $y$ exceeds a predefined statistical threshold $\tau$, the sequence is flagged as anomalous. Because computing $y$ is a static, linear algebraic operation, PCA achieves constant-time $O(1)$ inference. However, traditional PCA relies purely on event-count vectors (Term Frequency), completely ignoring both the *semantics* of the log text and the chronological *order* of events. Consequently, standard PCA fails to detect transition anomalies (where valid events occur in an invalid order), necessitating the heavy $O(N)$ sequential processing of LSTMs.

Our framework formulates a solution to this dilemma: by injecting temporal positional encodings into semantic event vectors, we can map complex transition probabilities into a flat spatial matrix, allowing the $O(1)$ speed of PCA to rival the sequential accuracy of Deep Learning.
