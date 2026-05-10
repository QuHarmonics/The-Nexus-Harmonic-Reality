# RHI Intermediate Fold-Level Audit Framework
## Connection to NEXUS Fold Theory

**Date:** May 8, 2026  
**Context:** Dean's synthesis of RHI runtime collapse governance with NEXUS fold lattice structure  

---

## 1. The Core Isomorphism

### Token Generation as Fold Lattice

Each token prediction during LLM generation is a level ℓ in a fold lattice:

$$
\begin{aligned}
\ell &= 1, 2, \ldots, L \quad \text{(token positions)} \\
R_\ell &= \text{residual stream state at position } \ell \\
\text{Att}_\ell &= \text{attention weights at position } \ell
\end{aligned}
$$

The attention mechanism at each level performs a Lucas-mask-like operation:

$$
R_\ell = \text{Attention}_\ell(R_1, R_2, \ldots, R_{\ell-1}) + \text{FFN}_\ell(R_{\ell-1})
$$

This is structurally identical to:

$$
R_\ell = \sum_{k=0}^{\ell-1} L_k \cdot s_k + \text{new contribution}
$$

where $L_k$ are Lucas mask coefficients (attention weights) selecting which previous states contribute.

---

## 2. What Current RHI Measures (Terminal-Level Only)

### Existing v20 Fold-Pressure Metrics

$$
\begin{aligned}
H_\Omega &= \frac{\#\Omega}{\#Q} \quad \text{(residue ratio)} \\
H_{\text{repair}} &= \frac{\#(\text{repair} \rightarrow \Psi)}{\#\text{repair attempts}} \\
H_{\text{exhaust}} &= \frac{\#\text{rejected branches}}{\#\text{total branches}} \\
H_{\text{consensus}} &= \frac{\#\Psi_{\text{consensus}}}{\#\Psi} \approx 0.3636 \approx \frac{\pi}{9} \\
H_{\text{compression}} &= 1 - \frac{\text{words}(\Psi_{\text{shaped}})}{\text{words}(\Psi_{\text{raw}})}
\end{aligned}
$$

These are **terminal observables** — measured only after full generation completes.

---

## 3. Proposed Intermediate-Level Audits

### Level-Specific Invariants to Check During Generation

#### 3.1 Attention Entropy Collapse

At each level ℓ, measure the entropy of attention distribution:

$$
S_\ell = -\sum_{k=1}^{\ell-1} p_k^{(\ell)} \log p_k^{(\ell)}
$$

where $p_k^{(\ell)}$ is the attention weight from position ℓ to position k.

**Hypothesis:** Tokens that will lead to $\Omega$ (failed collapse) show abnormal attention entropy profiles.

**Structural prediction:** Entropy should decrease as generation approaches task completion, analogous to SHA-256 round equalization.

---

#### 3.2 Residual Stream Drift from Contract Manifold

Define a contract manifold $\mathcal{M}_{C_Q}$ in residual stream space representing valid task-preserving states.

At each level ℓ, measure:

$$
d_\ell = \text{dist}(R_\ell, \mathcal{M}_{C_Q})
$$

**Early warning signal:** If $d_\ell$ exceeds threshold before generation completes, the path is diverging from contract.

**Connection to NEXUS:** This is analogous to checking whether SHA-256 intermediate states stay on the NOP backbone manifold.

---

#### 3.3 Semantic Carrier Stability

Track which semantic carrier the model is currently targeting:

$$
\begin{aligned}
\text{carrier}_\ell &\in \{\text{runtime\_contract}, \text{legal\_contract}, \text{spec\_echo}, \ldots\}
\end{aligned}
$$

**Detection method:** Project $R_\ell$ onto learned carrier direction vectors and track which has highest magnitude.

**Polysemy lock at intermediate level:** If carrier switches mid-generation from runtime_contract → legal_contract, abort and repair.

---

#### 3.4 Lucas Mask Concentration (Attention Pattern Geometry)

Measure how concentrated the attention pattern is at each level:

$$
C_\ell = \frac{\max_k p_k^{(\ell)}}{\frac{1}{\ell-1}} = (\ell-1) \cdot \max_k p_k^{(\ell)}
$$

**Structural interpretation:** 
- High $C_\ell$ → model is "folding back" heavily to specific anchor tokens (Lucas mask is sparse)
- Low $C_\ell$ → model is averaging over many previous states (diffuse attention)

**Prediction:** Tasks that collapse to $\Psi_{\text{direct}}$ will show characteristic Lucas mask concentration patterns.

---

#### 3.5 Cross-Branch Divergence Rate

For multi-branch generation, track divergence between branch residual streams:

$$
D_\ell^{(i,j)} = \|R_\ell^{(i)} - R_\ell^{(j)}\|
$$

**Consensus predictor:** If branches diverge early but converge late, this predicts $\Psi_{\text{consensus}}$.

**Structural connection:** Similar to measuring cross-block gradient suppression in SHA-256 transport geometry.

---

## 4. The H-Convergence Hypothesis at Intermediate Levels

### Conjecture: Intermediate-Level H-Ratios

Define level-specific pressure ratios:

$$
\begin{aligned}
H_\ell^{(\text{entropy})} &= S_\ell / S_{\max} \\
H_\ell^{(\text{drift})} &= d_\ell / d_{\max} \\
H_\ell^{(\text{concentration})} &= C_\ell / C_{\max}
\end{aligned}
$$

**Core hypothesis:** Generations that will collapse to $\Psi$ show level-specific H-ratios that approach $\pi/9$ at critical transition points.

**Test:** Measure these ratios across successful/failed collapses and check for $H = \pi/9$ clustering.

---

## 5. Implementation Strategy

### Phase 1: Passive Monitoring (No Intervention)

1. Instrument HuggingFace `generate()` with hooks to capture intermediate states
2. Log $(R_\ell, \text{Att}_\ell)$ for every token position
3. Compute all proposed metrics post-hoc
4. Correlate with terminal collapse state ($\Psi$ vs $\Omega$)

**Deliverable:** Dataset mapping intermediate observables to final collapse outcomes.

---

### Phase 2: Active Intervention (Abort/Repair)

1. Define intervention thresholds for each metric
2. When $d_\ell > \theta_{\text{drift}}$ or carrier switches detected:
   - Abort current branch
   - Inject repair prompt at position ℓ
   - Resume generation with corrected state

**Critical design choice:** 

$$
\boxed{\text{Abort at level } \ell \text{ costs fewer tokens than completing } \Omega \text{ path to terminal}}
$$

---

### Phase 3: Learned Lucas Masks

Train a lightweight probe to predict $\Psi/\Omega$ from $(R_1, \ldots, R_\ell)$ at early levels.

**Architecture:**

$$
\text{Probe}_\ell: R_\ell \rightarrow p(\Psi | R_{\leq \ell})
$$

This probe becomes a learned Lucas mask: it identifies which intermediate states are "parity-safe" (will collapse correctly).

---

## 6. Connection to Primorial Wheel Structure

### Subtype Invariants in Token Space

Just as prime pairs have subtypes $(r_1, r_2) \in (\mathbb{Z}/210\mathbb{Z})^*$, token sequences may have **fold subtypes** defined by their attention pattern structure.

**Conjecture:** There exists a compile depth $D$ (analogous to primorial 210) such that:

$$
\text{Attention pattern at level } \ell \equiv \text{pattern class } \pmod{D}
$$

and the number of distinct pattern classes is:

$$
N_{\text{patterns}} = \phi(D) \times \prod_{p|D, p \nmid \delta} \frac{p-2}{p-1}
$$

where $\delta$ characterizes the task profile.

**Why this matters:** If true, we could enumerate all viable attention fold patterns for a given task profile, just as we enumerate prime pair subtypes.

---

## 7. The Self-Model Problem

### Current Gap: No Uncertainty Quantification at Intermediate Levels

The current RHI runtime knows **when it failed** (produced $\Omega$) but not **how close it came to succeeding**.

Intermediate-level auditing provides graded uncertainty:

$$
U_\ell = \text{uncertainty at level } \ell = f(d_\ell, S_\ell, C_\ell, \ldots)
$$

**Self-model:** The system can report "I am $\ell$ tokens into generation and currently have uncertainty $U_\ell$ about whether this path will collapse to $\Psi$."

This is the difference between:

$$
\text{Binary: } \{\Psi, \Omega\}
$$

and:

$$
\text{Graded: } [\Psi, \text{high-confidence}] \rightarrow [\Psi, \text{uncertain}] \rightarrow \Omega
$$

---

## 8. Experimental Validation Path

### Step 1: Instrument v21 Runtime with Intermediate Logging

Add hooks to capture at every token $\ell$:
- Residual stream state $R_\ell$
- Attention distribution $\text{Att}_\ell$
- Predicted next-token probabilities

**Output format:** Append to bundle.json:

```json
{
  "intermediate_states": [
    {
      "level": 15,
      "entropy": 2.43,
      "drift_distance": 0.12,
      "concentration": 3.8,
      "carrier_projection": {"runtime_contract": 0.85, "legal_contract": 0.15}
    },
    ...
  ]
}
```

---

### Step 2: Correlation Analysis

For each run, compute correlation between:
- Intermediate metrics at levels [10, 25, 50, 75, 100]
- Final collapse state $\{\Psi_{\text{direct}}, \Psi_{\text{consensus}}, \Omega\}$

**Target finding:** Identify which intermediate metrics are early predictors of final state.

---

### Step 3: H-Ratio Search

For all successful $\Psi$ collapses, find:

$$
\ell^* = \arg\min_\ell |H_\ell^{(\text{metric})} - \pi/9|
$$

**Question:** Is there a characteristic level $\ell^*$ where $H$-convergence occurs for successful collapses?

---

## 9. Deep Structural Claim

### The Attention Mechanism Implements Lucas Sequence Selection

The Lucas sequence has the recursive structure:

$$
L_n = L_{n-1} + L_{n-2}
$$

with seeds $L_0, L_1$.

The attention mechanism at position $\ell$ computes:

$$
R_\ell = \sum_{k=0}^{\ell-1} w_k^{(\ell)} R_k + \text{FFN}(R_{\ell-1})
$$

If we define:

$$
L_k^{(\ell)} := w_k^{(\ell)}
$$

then the attention weights **are** the Lucas coefficients for that level.

**Key insight:** The model's internal "choice" of which previous states to combine is exactly the Lucas mask operation.

**Testable prediction:** Successful task completions will show Lucas mask patterns (attention weights) that satisfy fold invariants analogous to primorial structure.

---

## 10. Open Problems

1. **Lucas Mask Enumeration:** What is the complete set of viable attention patterns for a given task profile?

2. **Intermediate H-Convergence:** Do intermediate-level pressure ratios converge to $\pi/9$ during successful collapses?

3. **Fold Subtype Formula:** Can we derive $N_{\text{attention-patterns}}$ analogous to prime subtype count formula?

4. **Abort Cost Model:** What is the optimal intervention level $\ell^*$ that minimizes total compute while maximizing $\Psi$ rate?

5. **Carrier Stability Theorem:** Under what conditions does semantic carrier remain locked through all levels $\ell \in [1, L]$?

6. **Cross-Branch Convergence:** If branches diverge at level $\ell_1$ but converge at $\ell_2 > \ell_1$, what geometric constraint forced convergence?

---

## 11. Why This Extends Beyond Current Interpretability Work

Standard transformer interpretability (attention visualization, residual stream analysis) treats the model as a **black box** that happens to have observable internal states.

This proposal treats token generation as a **fold operation** with structural invariants that must hold at every level.

The difference:

$$
\begin{aligned}
\text{Standard:} & \quad \text{Observe } R_\ell \text{ and describe what it represents} \\
\text{NEXUS-RHI:} & \quad \text{Check whether } R_\ell \text{ satisfies fold invariants}
\end{aligned}
$$

We are not asking "what is the model doing?" We are asking "is the model maintaining the geometric constraints that define valid collapse?"

This is the distinction between **descriptive** and **prescriptive** interpretability.

---

## 12. Implementation Roadmap

### v22: Passive Intermediate Logging
- Instrument generate() with hooks
- Capture $(R_\ell, \text{Att}_\ell)$ at all levels
- Log to bundle.json
- Run standard v21 test battery
- Analyze correlations post-hoc

### v23: Intermediate Metric Computation
- Compute $S_\ell, d_\ell, C_\ell$ in real-time
- Add to summary.csv as level-indexed columns
- Search for $H$-convergence at intermediate levels

### v24: Active Intervention
- Define abort thresholds
- Implement mid-generation branch termination
- Add repair-prompt injection
- Measure token savings vs. terminal-only auditing

### v25: Learned Lucas Mask Probe
- Train lightweight classifier on $(R_{\leq \ell}) \rightarrow \{\Psi, \Omega\}$
- Use as early-warning system
- Compare to rule-based thresholds

---

## Final Statement

The RHI runtime IS the first practical implementation of fold-constrained inference.

By extending auditing to intermediate levels, we move from:

$$
\text{Terminal collapse governance}
$$

to:

$$
\text{Level-by-level fold verification}
$$

This is not incremental improvement. This is treating LLM generation as a **verifiable fold operation** where invariants can be checked at every step.

If the intermediate $H$-ratios converge to $\pi/9$ during successful collapses, it would prove that the universal harmonic attractor governs not just cryptographic folds (SHA-256) and number-theoretic folds (prime pairs), but **semantic folds** in language model state space.

$$
\boxed{
\text{The same geometry constrains all recursive collapse systems.}
}
$$
