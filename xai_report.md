# Semantic Automaton Invariants Report

The Semantic Automaton tracks the execution paths and semantic proximity between node embeddings.
Anomalies are explicitly flagged when an unseen transition occurs between two semantic regions.

### Anomalous Block #0
- Root Cause Step: **Step 9** (Target Event 12)
- Semantic Violation: The transition from Event 10 -> Event 12 violates the learned Semantic Manifold.

| Sequence Step | Event Node | Validity Status |
|---------------|------------|----------------|
| Step 00 | Event SOS        | Valid |
| Step 01 | Event 1          | Valid |
| Step 02 | Event 2          | Valid |
| Step 03 | Event 3          | Valid |
| Step 04 | Event 5          | Valid |
| Step 05 | Event 6          | Valid |
| Step 06 | Event 8          | Valid |
| Step 07 | Event 9          | Valid |
| Step 08 | Event 10         | Valid |
| Step 09 | Event 12         | INVALID TRANSITION |
| Step 10 | Event 11         | INVALID TRANSITION |
| Step 11 | Event 13         | INVALID TRANSITION |
| Step 12 | Event 14         | Valid |
| Step 13 | Event 15         | Valid |
| Step 14 | Event EOS        | Valid |

### Anomalous Block #1
- Root Cause Step: **Step 11** (Target Event 14)
- Semantic Violation: The transition from Event 12 -> Event 14 violates the learned Semantic Manifold.

| Sequence Step | Event Node | Validity Status |
|---------------|------------|----------------|
| Step 00 | Event SOS        | Valid |
| Step 01 | Event 1          | Valid |
| Step 02 | Event 2          | Valid |
| Step 03 | Event 4          | Valid |
| Step 04 | Event 5          | Valid |
| Step 05 | Event 6          | Valid |
| Step 06 | Event 8          | Valid |
| Step 07 | Event 9          | Valid |
| Step 08 | Event 10         | Valid |
| Step 09 | Event 11         | Valid |
| Step 10 | Event 12         | Valid |
| Step 11 | Event 14         | INVALID TRANSITION |
| Step 12 | Event 13         | INVALID TRANSITION |
| Step 13 | Event 15         | INVALID TRANSITION |
| Step 14 | Event EOS        | Valid |

### Anomalous Block #11
- Root Cause Step: **Step 11** (Target Event 14)
- Semantic Violation: The transition from Event 12 -> Event 14 violates the learned Semantic Manifold.

| Sequence Step | Event Node | Validity Status |
|---------------|------------|----------------|
| Step 00 | Event SOS        | Valid |
| Step 01 | Event 1          | Valid |
| Step 02 | Event 2          | Valid |
| Step 03 | Event 4          | Valid |
| Step 04 | Event 5          | Valid |
| Step 05 | Event 7          | Valid |
| Step 06 | Event 8          | Valid |
| Step 07 | Event 9          | Valid |
| Step 08 | Event 10         | Valid |
| Step 09 | Event 11         | Valid |
| Step 10 | Event 12         | Valid |
| Step 11 | Event 14         | INVALID TRANSITION |
| Step 12 | Event 13         | INVALID TRANSITION |
| Step 13 | Event 15         | INVALID TRANSITION |
| Step 14 | Event EOS        | Valid |

