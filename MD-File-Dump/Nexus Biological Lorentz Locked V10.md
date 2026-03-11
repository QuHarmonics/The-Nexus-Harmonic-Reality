# NEXUS Biological Lorentz — Locked Pipeline (v10 “Diamond” build)

**Goal.** Provide a *reproducible, pre-registered, sequence-only* test of whether a single fixed feature—**Sarrus Linkage**—predicts **two-state protein folding rates** (ln(k_f)) and how it behaves across **two-state**, **multi-state**, and **IDP** controls.

This document is written to be dropped into a paper’s Methods/Results/Supplement, including all required formulas and the “what must be true” audit logic.

---

## 1. Locked feature and invariants (“What must be true”)

We declare these **locked** *before* looking at outcomes:

- Property scale: **Miyazawa–Jernigan burial/contact energy** (MJ), mapping residues $a_i \mapsto x_i$.
- Helix lags: $L_H = \{3,4\}$
- Sheet lag: $L_S = 2$
- Shuffled baseline size: $N_\text{shuf}=1000$
- Permutation test: $N_\text{perm}=10000$
- Determinism: **stable shuffle seed** per sequence via $\text{MD5}(\text{seq})$.

### 1.1 What must be true for the analysis to be “good”

1. **Domain match**  
   The sequence analyzed must match the kinetic construct (domain, chain, fragment) used to measure $k_f$.  
   Operationally: use **whitelist overrides** for known multi-domain/fragment PDB IDs; otherwise choose an RCSB chain whose length matches expected length within tolerance; otherwise **skip**.

2. **Composition control**  
   The feature must be a **pattern-above-composition** statistic. We enforce this by Z-scoring against shuffled sequences that preserve composition. The shuffle baseline must have nonzero variance:
   $$\operatorname{sd}(\text{shuffle}) > 0.$$

3. **Pre-registered**  
   No changing **scale / lags / shuffle count / tolerance** after viewing correlation $r$.

4. **Deterministic**  
   The null model is reproducible: for each protein sequence, shuffling uses a deterministic RNG seed:
   $$\text{seed}(\text{seq}) = \text{MD5}(\text{seq}) \bmod 2^{32}.$$

5. **Generalization**  
   Report **leave-one-out cross-validated** performance ($R^2_\text{LOO}$).

6. **Validation**  
   Report:
   - Permutation $p$-value ($N_\text{perm}$),
   - Partial correlation controlling for length (using $\ln L$).

7. **Transparency**  
   Print and retain an **audit table** of included/excluded proteins and why.

---

## 2. Data

### 2.1 Two-state folding dataset (primary)

Primary kinetic targets are the **two-state** set (e.g., Ivankov-style compendium): for each protein $i$ we have:

- expected length $L_i^\text{exp}$
- folding rate $k_{f,i}$, analyzed as $y_i = \ln k_{f,i}$
- (optional benchmark) contact order $\text{CO}_i$ (structure-based reference, not sequence-only)

### 2.2 Multi-state dataset (secondary / spectrum context)

A multi-state set is included **only** to evaluate whether the same feature generalizes across a different folding mechanism. It is **not** the primary endpoint.

### 2.3 IDP controls (non-primary horizon)

A small set of intrinsically disordered proteins (IDPs) is included as qualitative controls. Their kinetics are not comparable in the same way as two-state folders, so they are treated as **non-primary**.

---

## 3. Feature definition: Sarrus Linkage

### 3.1 Convert sequence to a numeric “carrier wave”

Let the amino-acid sequence be $(a_1,\dots,a_L)$ and MJ map each residue to $x_t$:

$$x_t = \text{MJ}(a_t).$$

Center the signal:

$$s_t = x_t - \bar{x}, \qquad \bar{x} = \frac{1}{L}\sum_{t=1}^L x_t.$$

Normalize energy:

$$\|s\|^2 = \sum_{t=1}^L s_t^2.$$

We require $\|s\|^2>0$.

### 3.2 Autocorrelation at locked lags

Define normalized lag autocorrelation:

$$A(\ell) = \frac{\sum_{t=1}^{L-\ell} s_t s_{t+\ell}}{\sum_{t=1}^{L} s_t^2} = \frac{\sum_{t=1}^{L-\ell} s_t s_{t+\ell}}{\|s\|^2}.$$

Locked helix autocorrelation:

$$A_H = \frac{1}{|L_H|}\sum_{\ell \in L_H} A(\ell) = \frac{A(3)+A(4)}{2}.$$

Locked sheet autocorrelation:

$$A_S = A(L_S)=A(2).$$

### 3.3 Shuffle-null Z-scores (composition control)

Construct a shuffle null by permuting the residue multiset (composition preserved). For shuffle draw $j$ we compute:

$$A_H^{(j)},\quad A_S^{(j)}, \qquad j=1,\dots,N_\text{shuf}.$$

Then:

$$Z_H = \frac{A_H - \mu_H}{\sigma_H}, \qquad \mu_H = \frac{1}{N_\text{shuf}}\sum_{j} A_H^{(j)}, \quad \sigma_H = \operatorname{sd}\{A_H^{(j)}\},$$

$$Z_S = \frac{A_S - \mu_S}{\sigma_S}, \qquad \mu_S = \frac{1}{N_\text{shuf}}\sum_{j} A_S^{(j)}, \quad \sigma_S = \operatorname{sd}\{A_S^{(j)}\}.$$

We require $\sigma_H>0$ and $\sigma_S>0$.

### 3.4 Sarrus Linkage (locked primary feature)

The **single pre-registered feature** is:

$$
\boxed{
\text{Sarrus} \equiv Z_H - Z_S
}
$$

Interpretation: net “helical periodicity excess” over “sheet periodicity excess” **above composition-only expectation**.

---

## 4. Statistical tests (locked)

### 4.1 Primary association test (two-state only)

Let $x_i=\text{Sarrus}_i$ and $y_i=\ln(k_{f,i})$ for included two-state proteins. Report Pearson correlation:

$$r = \frac{\sum_i (x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_i(x_i-\bar{x})^2\sum_i(y_i-\bar{y})^2}}.$$

We report $(r,p)$.

### 4.2 Permutation test (distribution-free)

Compute $r_\text{obs}=|r(x,y)|$. For $b=1,\dots,N_\text{perm}$:

- permute targets: $y^{(b)}=\pi_b(y)$
- compute $r^{(b)}=|r(x,y^{(b)})|$

Permutation $p$-value:

$$
p_\text{perm} = \frac{1}{N_\text{perm}}\sum_{b=1}^{N_\text{perm}}\mathbf{1}\{r^{(b)} \ge r_\text{obs}\}.
$$

### 4.3 Partial correlation controlling length

Let covariate $c_i = \ln(L_i^\text{used})$ where $L_i^\text{used}$ is the actual analyzed sequence length.

Residualize:

$$x_i^\perp = x_i - \hat{\alpha}_x - \hat{\beta}_x c_i,$$
$$y_i^\perp = y_i - \hat{\alpha}_y - \hat{\beta}_y c_i.$$

Then compute:

$$r_\text{partial} = r(x^\perp, y^\perp).$$

### 4.4 Leave-one-out cross-validation (LOO-CV)

For each $i$, fit a linear model on all points except $i$:

$$\hat{y}^{(-i)} = \hat{a}^{(-i)} + \hat{b}^{(-i)} x,$$

then predict:

$$\hat{y}_i = \hat{a}^{(-i)} + \hat{b}^{(-i)} x_i.$$

Report:

- LOO correlation $r_\text{LOO}=r(\hat{y},y)$
- LOO coefficient of determination:
$$
R^2_\text{LOO} = 1 - \frac{\sum_i (y_i-\hat{y}_i)^2}{\sum_i (y_i-\bar{y})^2}.
$$

### 4.5 Benchmark (structure-based, non-primary)

If contact order $\text{CO}_i$ is available, report:

$$r_\text{CO} = r(\text{CO}, \ln k_f).$$

This is a “gold standard” comparison that *requires 3D structure* and is therefore not directly comparable to a sequence-only predictor.

---

## 5. Domain matching and audit logic

### 5.1 Why domain matching matters

Many PDB IDs correspond to constructs that differ from kinetic measurements:

- multi-domain proteins where the kinetic experiment used a single domain
- fragmented entries
- alternative chains / engineered constructs

To avoid “garbage in,” we define an audit policy:

1. **Override** if a curated construct sequence exists (whitelist).
2. Otherwise, **select** an RCSB candidate chain whose length matches expected within tolerance.
3. Otherwise **skip**, and record why.

### 5.2 Transparency requirement

The run must emit a table containing, per protein:

- PDB id, name
- expected length $L^\text{exp}$ and used length $L^\text{used}$
- status: `OVERRIDE`, `FETCH_MATCH`, `SKIP`
- rationale (mismatch, missing, etc.)
- shuffle baseline diagnostics: $(\sigma_H,\sigma_S)$ to confirm composition-control validity

---

## 6. Results summary (v10 “Diamond” build)

### 6.1 Two-state (primary)

A representative locked run reported approximately:

- $n \approx 26$ (after domain/mismatch hygiene)
- Pearson $r \approx 0.55$ with $p \approx 0.004$
- Permutation $p_\text{perm} \approx 0.004$
- Partial $r$ controlling $\ln L$ remains similar ($\approx 0.54$–$0.56$)
- LOO-CV $R^2_\text{LOO}\approx 0.17$

**Interpretation (strictly within the test’s scope):**  
Sarrus Linkage contains **sequence-level predictive information** about two-state folding rates above compositional chance, and this survives length control, permutation testing, and LOO evaluation.

### 6.2 Multi-state (mechanism contrast)

The same feature typically shows *weaker or inconsistent* relationships in multi-state proteins, consistent with the idea that intermediates/kinetic traps add degrees of freedom not captured by a single sequence periodicity differential.

### 6.3 “Spectrum” context (means)

The “diamond” summary reported mean Sarrus values roughly:

- Two-state mean $Z \sim 0.06$
- Multi-state mean $Z \sim 0.82$
- IDP mean $Z \sim 0.77$ (with small $n$)

These means are **descriptive**. They are *not* the primary hypothesis test unless pre-registered as such.

---

## 7. Allocation interpretation and Lorentz-style probe (optional, clearly labeled)

This section is a **modeling proposal**, not required to validate the locked correlation.

### 7.1 The “Allocate” primitive (concept)

Assume a finite system has a constrained budget that must be allocated between:

- **Exploration** (search / entropy production / sampling)
- **Collapse** (constraint satisfaction / structure formation)

Let $\sigma \in [0,1]$ denote the fraction allocated to exploration.

### 7.2 A Lorentz-like remainder

A minimal mathematical form for a remainder (collapse-capable budget) is:

$$\rho(\sigma)=\sqrt{1-\sigma^2}.$$

If folding speed is proportional to collapse remainder:

$$k_f \propto \rho(\sigma) = \sqrt{1-\sigma^2}.$$

Then:

$$\ln k_f = \ln k_0 + \frac{1}{2}\ln(1-\sigma^2).$$

### 7.3 Operationalizing $\sigma$ from Sarrus

A future (non-locked) step is to map Sarrus to an allocation coordinate, e.g.:

$$\sigma = g(\text{Sarrus}, L),$$

with $g$ chosen/learned on a training set and validated on an external dataset. This is *not* established by the current locked linear correlation; it is an explicitly proposed next test.

---

## 8. Reporting checklist (for the paper)

To make this publication-grade and reviewer-proof, include:

- The **locked configuration** block verbatim (scale, lags, $N_\text{shuf}$, $N_\text{perm}$, deterministic seeding).
- The **audit table** as a supplement.
- The exact definitions of $A(\ell)$, $Z_H$, $Z_S$, and $\text{Sarrus}$.
- Primary: $(r,p)$, $p_\text{perm}$, $r_\text{partial}$, $(r_\text{LOO}, R^2_\text{LOO})$.
- Benchmark: $r_\text{CO}$ (optional).
- A clear note that multi-state/IDP analyses are **secondary / descriptive** unless explicitly pre-registered as additional endpoints.

---

## 9. Minimal pseudocode (for Methods)

1. For each protein $i$:
   1. Obtain sequence matching kinetic construct (override / chain-select / skip).
   2. Compute $A_H$ and $A_S$ from MJ signal.
   3. Shuffle composition-preserving sequences $N_\text{shuf}$ times with MD5-seeded RNG and compute $Z_H$, $Z_S$.
   4. Compute $\text{Sarrus}_i = Z_H - Z_S$.
2. On included two-state proteins:
   1. Compute Pearson $r(\text{Sarrus}, \ln k_f)$.
   2. Compute $p_\text{perm}$ with $N_\text{perm}$ shuffles of $y$.
   3. Compute partial $r$ controlling $\ln L$ via residualization.
   4. Compute LOO-CV predictions and $R^2_\text{LOO}$.
3. Output:
   - audit table
   - summary scoreboard
   - figures (scatter + spectrum plot)

---

## Appendix A. Notation

- $a_t$: amino acid at position $t$
- $x_t$: MJ-mapped numeric value
- $s_t$: centered signal
- $A(\ell)$: normalized autocorrelation at lag $\ell$
- $A_H, A_S$: helix/sheet autocorrelation summaries
- $Z_H, Z_S$: shuffle-null Z-scores
- $\text{Sarrus}$: $Z_H - Z_S$
- $L^\text{exp}$: expected length (kinetic construct)
- $L^\text{used}$: analyzed sequence length
- $y=\ln k_f$: target variable
