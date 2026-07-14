# 4. The AXEL Framework

This section details the architecture of the AXEL framework. The pipeline consists of four distinct components: Semantic-Structural Embeddings, a Constant-Time PCA Manifold, Exact Euler Feature Attribution, and Dynamic Threshold Adaptation.

## 4.1 Semantic-Structural Embeddings
Traditional log anomaly detection models encode events using primitive Term Frequency (TF-IDF) or Word2Vec \cite{mikolov2013distributed} matrices, which fail to capture the deep contextual semantics of the log template. AXEL utilizes a pre-trained Sentence-BERT model (`all-MiniLM-L6-v2`) \cite{reimers2019sentence} to transform the raw, parsed log templates into dense 384-dimensional semantic vectors. 

To circumvent the necessity of recurrent models (like LSTMs) for learning sequential transition patterns, AXEL injects deterministic Sinusoidal Positional Encodings \cite{vaswani2017attention} directly into the semantic vectors. For an event at position $pos$ and dimension $i$, the positional encoding $PE$ is defined as:
$$ PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d}) $$
$$ PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d}) $$

By aggregating these positional signals into a single average sequence embedding, AXEL flattens temporal order into a spatial dimension. This guarantees that two identical events occurring in different sequential orders will project to distinctly different points in the $d$-dimensional space, allowing a linear matrix to detect sequence transition anomalies.

## 4.2 Constant-Time Anomaly Scoring
With the chronological sequence flattened into a single spatial vector $x \in \mathbb{R}^d$, AXEL eliminates the need for sequential token-by-token evaluation. During the offline training phase, AXEL computes the covariance matrix of the normal structural embeddings and extracts the top $k$ principal components to form the projection matrix $P$. The orthogonal residual matrix is defined as $C = I - P P^T$.

During online inference, classifying a new sequence requires only a single vector-matrix multiplication to calculate the Squared Prediction Error (SPE):
$$ y = x^T C x $$

Because $C$ is a pre-computed, constant matrix of size $d \times d$, this calculation scales strictly with $O(d^2)$. Since $d$ (embedding dimension) is a fixed constant, the theoretical time complexity of anomaly inference in AXEL is exactly $O(1)$ relative to the sequence length $N$. In contrast, LSTMs \cite{du2017deeplog} and Transformers \cite{huang2020hitanomaly} strictly require $O(N)$ and $O(N^2)$ computations respectively. 

## 4.3 Exact Feature Attribution via Euler’s Theorem
When AXEL flags a sequence as anomalous, operators require immediate localization of the offending log event. Instead of relying on computationally exorbitant stochastic approximations like SHAP \cite{lundberg2017unified} or LIME \cite{ribeiro2016should}, AXEL exploits the inherent algebraic properties of its reconstruction manifold.

The anomaly score $y = x^T C x$ is mathematically defined as a quadratic form. By definition, a quadratic form is a homogeneous function of degree $k = 2$. Therefore, according to Euler's Homogeneous Function Theorem:
$$ k \cdot y = \sum_{i=1}^{d} x_i \frac{\partial y}{\partial x_i} $$

Given that the gradient of the quadratic form is $\nabla y = 2 C x$, we can substitute this back into Euler's Theorem to extract the exact, analytical contribution $c_i$ of each specific feature dimension:
$$ c_i = x_i \cdot (C x)_i $$

AXEL projects these exact dimensional attributions back onto the original sequence tokens, delivering mathematically flawless root-cause analysis instantly during the $O(1)$ forward pass without requiring a single perturbation or Monte Carlo sampling step.

## 4.4 Dynamic Threshold Adaptation (ADWIN)
Industrial systems continuously evolve, causing the baseline distribution of the SPE scores to shift over time (Concept Drift). Statically defined anomaly thresholds eventually trigger cascading false positives (Alert Fatigue).

Instead of triggering costly neural weight retraining \cite{zhang2021adaptive}, AXEL employs a zero-retraining adaptation mechanism. We apply the ADaptive WINdowing (ADWIN) \cite{bifet2007learning} algorithm to monitor the streaming SPE scores. ADWIN maintains a dynamic memory window that automatically shrinks when a statistically significant shift in the mean SPE is detected.

When ADWIN flags a distributional shift, AXEL triggers a 1D Gap-Finding subroutine. The subroutine analyzes the histogram of SPE scores within the new operational window, scanning for the widest empty margin (gap) between the dense cluster of normal predictions and the sparse tail of true anomalies. AXEL autonomously snaps the anomaly threshold $\tau$ to the center of this gap, healing the decision boundary instantly and restoring precision without interrupting the CI/CD pipeline.
