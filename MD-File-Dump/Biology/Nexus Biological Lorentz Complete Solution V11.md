
# NEXUS Biological Lorentz Validation — Complete, Locked, Shareable Solution (v11)

> **Scope:** This document is the “paper-ready” *methods + validation* specification for the **locked** Nexus biological pipeline, including the corrected **Lorentz-bridge probe** and the required reporting checks (“what must be true”).  
> **Goal:** provide a complete, reproducible protocol that (i) predicts **two-state folding rate** from **sequence only**, and (ii) cleanly separates what is **validated**, what is **not**, and what is **exploratory**.

---

## 0) Definitions and Notation

Let a protein sequence be
$$
\mathbf{a} = (a_1,a_2,\dots,a_N),\quad a_i\in\{\text{20 amino acids}\}.
$$

Choose an amino-acid **property scale** (locked: Miyazawa–Jernigan burial/contact potential) mapping
$$
w:\{\text{AA}\}\rightarrow\mathbb{R}.
$$

Convert the sequence to a real-valued signal
$$
x_i = w(a_i),\qquad i=1,\dots,N,
$$
and mean-center it
$$
\tilde{x}_i = x_i - \bar{x},\qquad \bar{x}=\frac{1}{N}\sum_{i=1}^N x_i.
$$

Define its energy/normalization
$$
\|\tilde{\mathbf{x}}\|^2 = \sum_{i=1}^N \tilde{x}_i^2.
$$

The measured folding rate is
$$
y = \ln(k_f).
$$

---

## 1) LOCKED Feature (Pre-Registered)

**Primary (pre-registered) sequence feature:**
- **Scale:** MJ burial/contact values.
- **Helix lags:** $L_H=\{3,4\}$ (α-helix ≈ 3.6 residues/turn).
- **Sheet lag:** $L_S=\{2\}$ (β alternation).
- **Shuffle count:** $n_{\mathrm{shuf}}=1000$ per protein.
- **Deterministic shuffling:** seed = `MD5(sequence)` (per-protein reproducibility).
- **Output feature:** **Sarrus Linkage**
$$
S \equiv Z_H - Z_S.
$$

These must not be changed after observing results.

---

## 2) The Observed Autocorrelation (ACF) Measurements

Define lag-$\ell$ normalized autocorrelation:
$$
\mathrm{ACF}(\ell) \equiv
\frac{\sum_{i=1}^{N-\ell}\tilde{x}_i\,\tilde{x}_{i+\ell}}{\sum_{i=1}^N \tilde{x}_i^2}
=
\frac{\sum_{i=1}^{N-\ell}\tilde{x}_i\,\tilde{x}_{i+\ell}}{\|\tilde{\mathbf{x}}\|^2}.
$$

Define:
- **Helix ACF** (locked average of lags 3 and 4):
$$
H \equiv \frac{1}{2}\left(\mathrm{ACF}(3)+\mathrm{ACF}(4)\right).
$$
- **Sheet ACF** (locked lag 2):
$$
B \equiv \mathrm{ACF}(2).
$$

---

## 3) Composition Control via Shuffle Null (Z-scoring)

### 3.1 Null model
Let $\pi(\mathbf{a})$ be a random permutation of the amino acids in the sequence (composition preserved, pattern destroyed).

For each shuffle $j=1,\dots,n_{\mathrm{shuf}}$, compute $H^{(j)}$ and $B^{(j)}$ from the shuffled sequence.

Compute null means and standard deviations:
$$
\mu_H = \frac{1}{n}\sum_{j=1}^{n}H^{(j)},\quad
\sigma_H = \sqrt{\frac{1}{n-1}\sum_{j=1}^{n}\left(H^{(j)}-\mu_H\right)^2},
$$
and similarly $(\mu_B,\sigma_B)$.

### 3.2 Z-scores
Define:
$$
Z_H \equiv \frac{H-\mu_H}{\sigma_H},\qquad
Z_S \equiv \frac{B-\mu_B}{\sigma_B}.
$$

### 3.3 Sarrus Linkage (primary feature)
$$
S \equiv Z_H - Z_S.
$$

**Interpretation (minimal, non-metaphysical):**  
$S$ is a *composition-controlled* differential periodicity index: “helix-like lag structure minus sheet-like lag structure.”

---

## 4) Determinism (Must Be True)

To ensure the same inputs always yield the same outputs:

**Deterministic shuffle seed**
$$
\text{seed} = \mathrm{MD5}(\text{sequence}) \bmod 2^{32}.
$$

This makes the shuffle null reproducible *per protein*, independent of processing order, machine, or run.

---

## 5) Data Hygiene: Domain Match Must Hold

### 5.1 Why
Ivankov-style kinetic measurements often refer to specific **constructs** (domains/fragments), while RCSB FASTA may return:
- full-length proteins with extra domains,
- short peptides / missing chains,
- engineered constructs,
- different chains than the kinetics construct.

If the analyzed sequence does not match the kinetics construct, the metric is not well-defined for that data point.

### 5.2 Policy (locked)
For each protein with expected length $L_{\mathrm{exp}}$:
1. **Override** with a curated construct sequence *if known* (white-list).
2. Otherwise **fetch** from RCSB and select candidate chain/sequence.
3. **Include** only if the used length satisfies:
$$
\left|\;L_{\mathrm{used}}-L_{\mathrm{exp}}\;\right| \le 0.10\,L_{\mathrm{exp}}
$$
unless the item is explicitly **OVERRIDE**.
4. Otherwise **SKIP** with audit reason.

### 5.3 Transparency: audit table
A run is not “good” unless it prints a row-by-row **audit table** stating:
- PDB id, name
- $L_{\mathrm{exp}}$, $L_{\mathrm{used}}$
- status ∈ {FETCH\_MATCH, OVERRIDE, SKIP, MISSING}
- reason (mismatch, chain ambiguity, etc.)
- shuffle stats (e.g., $\sigma_H,\sigma_B>0$ checks)

---

## 6) Primary Statistical Claims (What You Must Report)

Let $(S_i,y_i)$ be the included data (two-state set only) for $i=1,\dots,n$.

### 6.1 Pearson correlation
$$
r = \mathrm{corr}(S,y),\qquad p=\text{two-sided Pearson p-value}.
$$

### 6.2 Permutation test (distribution-free)
Compute
$$
r_{\mathrm{obs}} = |\mathrm{corr}(S,y)|.
$$
For $t=1,\dots,T$ (locked $T=10000$), permute $y$ to $y^{(t)}$ and compute
$$
r_t = |\mathrm{corr}(S,y^{(t)})|.
$$
Then
$$
p_{\mathrm{perm}} = \frac{1}{T}\sum_{t=1}^T \mathbb{I}\{r_t\ge r_{\mathrm{obs}}\}.
$$

### 6.3 Partial correlation controlling for length
Let $c_i=\ln(L_{\mathrm{used},i})$. Regress out $c$:
$$
S^\perp = S - \hat{S}(c),\qquad y^\perp = y - \hat{y}(c),
$$
where $\hat{S}(c)$ and $\hat{y}(c)$ are least-squares linear fits vs $c$.

Partial correlation:
$$
r_{\mathrm{partial}} = \mathrm{corr}(S^\perp, y^\perp),
$$
with a Pearson p-value on residuals.

### 6.4 Generalization: Leave-One-Out Cross-Validation (LOO-CV)
For each $i$:
- fit $y=\alpha+\beta S$ using all points except $i$,
- predict $\hat{y}_i$ for the held-out point.

Report:
- correlation $r_{\mathrm{LOO}}=\mathrm{corr}(y,\hat{y})$
- coefficient of determination
$$
R^2_{\mathrm{LOO}} = 1-\frac{\sum_i (y_i-\hat{y}_i)^2}{\sum_i (y_i-\bar{y})^2}.
$$

**This is required** to prevent “in-sample fit looks good” from being mistaken for predictive value.

---

## 7) Validation B: Mechanism Split (Two-State vs Multi-State)

This is a separate validation question:

- **Primary predictor** is validated on **two-state** proteins (single cooperative transition).
- Multi-state proteins may **break** the relationship because kinetics depend on intermediates not visible to this 1D sequence statistic.

### 7.1 What must be true to interpret a “multi-state failure”
If $r\approx 0$ in multi-state:
- it is consistent with: $S$ measures *cooperative constraint coherence* rather than “anything about all folding.”
- it is **not** evidence that $S$ is useless; it refines the domain of validity.

**Report both, but do not claim mechanism classification unless supported.**

---

## 8) The Lorentz Bridge (Corrected Probe)

### 8.1 What went wrong (bug)
A prior notebook cell used the wrong column index: it used **Contact Order** where it intended **$\ln(k_f)$**.  
So the “Lorentz falsification” was not a real test of the Lorentz mapping.

### 8.2 What is being tested now
We introduce a monotone “entropy load” coordinate $\sigma\in(0,1)$ derived from $S$ by a rank-based map:

Given $S_1,\dots,S_n$, define ranks $r_i\in\{1,\dots,n\}$ (ties averaged), then
$$
\sigma_i = \frac{r_i - 0.5}{n}.
$$

This is **locked** as the operationalization of $\sigma$ for the Lorentz probe (it avoids unit choices and uses only ordering).

### 8.3 Lorentz transform feature
Define the Lorentz factor:
$$
\gamma(\sigma)=\frac{1}{\sqrt{1-\sigma^2}}.
$$

A convenient linearizable “Lorentz term” is
$$
\Lambda(\sigma)=\ln\gamma(\sigma)= -\frac{1}{2}\ln(1-\sigma^2).
$$

**Lorentz probe model (tested):**
$$
y = a + b\,\Lambda(\sigma) + \varepsilon.
$$

Compare against:
1. **Linear in** $\sigma$: $y=a+b\sigma+\varepsilon$  
2. **Linear in** $S$: $y=a+bS+\varepsilon$

### 8.4 What must be true for the Lorentz bridge claim
For a claim like “Lorentz mapping is preferred” to be defensible, the following must hold *on the locked dataset*:

1. **Correct target variable:** all probes use $y=\ln(k_f)$ (not contact order).  
2. **No extra tuning:** once $\sigma(\cdot)$ is fixed (rank map), you do not choose among many $\sigma$ maps after seeing results.  
3. **Out-of-sample advantage:** Lorentz model must improve **LOO-CV** $R^2$ relative to linear alternatives.  
4. **Parsimony:** if you compare models by AIC/BIC, compute them consistently from the same residual likelihood.  
5. **Robustness check:** the improvement should not be driven by one extreme point (check leave-one-out influence or Cook’s distance).  

If these hold, then you may report: “a nonlinear Lorentz-form transform explains slightly more variance than a linear form on this dataset,” while still being careful about generality.

---

## 9) “Multi-fold = Multi-message?” — What Must Be True for the Analogy

You asked:

> “Is multi-fold (multi-state proteins) the same as multi-message in SHA?”

For that to be true in a **scientific** (not poetic) sense, you need an **operational isomorphism**, i.e., a mapping between:

- protein folding pathways with intermediates, and  
- hash-round constraint propagation with multiple competing message-consistent states.

### 9.1 Define the objects on each side
**Protein side:**
- A trajectory over conformations $C(t)$ with multiple metastable basins.
- Multi-state: at least one intermediate basin $I$ with non-negligible occupancy.

**SHA side (conceptual):**
- A constraint-propagation process over internal state bits/words.
- “Multi-message” means: at a given round/position, constraints are compatible with multiple distinct message hypotheses (ambiguity), i.e., more than one satisfying assignment survives.

### 9.2 What must be true (minimal conditions)
To assert “same thing” beyond metaphor, you need:

1. **A shared state representation:** a mapping $\phi$ taking each system’s evolving state to a common constraint-state space:
   $$
   \phi_{\mathrm{bio}}(C(t))\in\mathcal{X},\qquad \phi_{\mathrm{sha}}(H(r))\in\mathcal{X}.
   $$
2. **A shared notion of constraint energy / coherence:** a scalar functional $Q:\mathcal{X}\to\mathbb{R}$ such that
   - two-state folding shows monotone increase in $Q$ (single collapse),
   - multi-state folding shows stalls/plateaus (intermediate trapping),
   - “multi-message” SHA regions show stalls/plateaus in the same $Q$ statistic (ambiguity persists).
3. **The same failure mode signature:** intermediates in proteins must correspond to *ambiguity plateaus* in SHA under the same measurement (e.g., a constraint-coherence differential like Sarrus).
4. **Predictive linkage:** not just “looks similar,” but a prediction:
   - proteins classified multi-state should show lower coherence growth rates (or higher plateau probability) under $Q$,
   - SHA segments identified as multi-message should show the analogous plateau probability under $Q$,
   - and ideally a shared scaling law relating plateau depth/width to measurable rates (folding time or extraction difficulty).
5. **Null rejection:** show that random controls (shuffled sequences; random-message SHA) do not produce the same plateau structure.

If you can’t meet (1–5), you should present the relationship explicitly as an **analogy/hypothesis**, not an equivalence.

---

## 10) The Notebook Error You Hit (Series formatting)

You saw:

> `TypeError: unsupported format string passed to Series.__format__`

This means `r` or `p` is a **pandas Series** rather than a scalar float. Fix patterns:

- If `r,p = stats.pearsonr(...)` but inputs are Series with shape (n,1) or you did a groupby-apply, you may have Series outputs.

**Safe fix:**
```python
r = float(r)
p = float(p)
ax.set_title(f"PRIMARY: r={r:.3f}, p={p:.2e}")
```

Or if `pearsonr` is called on a DataFrame column slice that returns a 2D object, force 1D arrays:
```python
x = np.asarray(x).ravel()
y = np.asarray(y).ravel()
r, p = stats.pearsonr(x, y)
```

---

## 11) Summary: What Is “Good” and What Is Not

### 11.1 “Good” (validated, locked)
A run is “good” if all are true:

1. **Locked feature:** MJ scale; helix lags $\{3,4\}$; sheet lag $\{2\}$; $n_{\mathrm{shuf}}=1000$; MD5 seed.  
2. **Domain match:** included sequences match kinetic constructs (override or within 10% length tolerance).  
3. **Composition control:** Z-scoring against shuffle null with $\sigma_H>0$ and $\sigma_B>0$.  
4. **Determinism:** repeatable outputs independent of run order.  
5. **Generalization reported:** LOO-CV $R^2$ reported (not just Pearson $r$).  
6. **Validation reported:** permutation p-value and partial correlation controlling $\ln(L)$.  
7. **Transparency:** audit table of included/skipped reasons printed.

### 11.2 “Exploratory” (allowed, but label it)
- Mechanism classification by threshold on $S$ (performed poorly in your earlier runs; do not overclaim).
- IDP positioning on the spectrum (interesting but not primary; depends strongly on which IDPs are chosen).
- Lorentz-bridge mapping (now corrected and testable; still needs independent dataset replication).

---

## 12) What to Put in the Paper (Recommended)

**Methods (must include):**
- Definition of MJ signal and ACF lags.
- Shuffle null and Z-score formulas.
- Sarrus Linkage definition.
- Deterministic seeding method.
- Domain-match policy + override table.
- Primary stats: Pearson, permutation p, partial corr controlling $\ln(L)$, LOO-CV.

**Results (two-state primary):**
- Report $r$, $p$, $p_{\mathrm{perm}}$, $r_{\mathrm{partial}}$, and $R^2_{\mathrm{LOO}}$.
- Compare vs Contact Order as a “needs structure” benchmark (clearly different information regime).

**Optional / secondary:**
- Multi-state “failure” as a mechanism-domain statement.
- Lorentz probe results as exploratory unless replicated.

---

## Appendix A — Locked Configuration Block (copy/paste)

- Scale: MJ (Miyazawa–Jernigan burial/contact potential)  
- Helix lags: $[3,4]$  
- Sheet lag: $2$  
- Shuffles per protein: $1000$  
- Shuffle seed: $\mathrm{MD5}(\text{sequence}) \bmod 2^{32}$  
- Permutations for p-value: $10000$  
- Inclusion tolerance (unless override): $|L_{\mathrm{used}}-L_{\mathrm{exp}}| \le 0.1 L_{\mathrm{exp}}$  
- Primary endpoint: two-state proteins only, $y=\ln(k_f)$  

---

## Appendix B — Minimal Pseudocode

1. Fetch/override sequence; verify length and domain match.  
2. Compute $H=\frac12(\mathrm{ACF}(3)+\mathrm{ACF}(4))$, $B=\mathrm{ACF}(2)$.  
3. Shuffle (MD5-seeded) 1000 times to get null means/std.  
4. Compute $Z_H$, $Z_S$, and $S=Z_H-Z_S$.  
5. Fit and report stats on two-state set:
   - Pearson $(S,y)$
   - permutation p-value
   - partial corr controlling $\ln(L)$
   - LOO-CV $R^2$  
6. Print audit table.

---

*Version:* v11 (includes corrected Lorentz probe definition and notebook bug fix guidance)  
*Generated:* 2026-02-15
