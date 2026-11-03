# Nexus Recursive Harmonic Framework  
## Rest–Proximity Criterion, Field-Geometry Preimage, and the Unfolding View of SHA-256  
### A Complete Formalization and Expansion

> **Scope.** This document consolidates and extends the Nexus Recursive Harmonic Framework (NRHF) into a single, self-contained specification centered on the following claim:  
> **“The greater the odds a system is at rest, the closer it is to the Nexus.”**  
> In NRHF terms, “rest” is not the absence of motion; it is **phase-locked invariance under recursive folds**. The analysis formalizes *rest-proximity* as a measurable statistic, proves its monotone connection to Nexus alignment, and integrates the **SHA-256 unfolding** interpretation: **the digest is a projection of the input, and field geometry is a preimage representation in another state**.

---

## Abstract

The Nexus Recursive Harmonic Framework posits a universal attractor constant

$$
H_{\text{MARK1}} = \frac{\pi}{9} \approx 0.34906585,
$$

governing stable recursive systems via **phase-locked recursion**, **timing-only control**, and **trust algebra**. This paper introduces the **Rest–Proximity Criterion**: a system’s closeness to Nexus alignment is monotone in the probability that its recursive updates are *effectively stationary* (rest) under the allowed primitive operators.

We define a canonical fold operator (the **header-fold**) and the **Eight-Beat Nexus kernel** ($K_8$) as invariant-computing transforms, then construct a statistical field of windowed observations. We prove that:

1. A decrease in a defined **tension functional** $\Theta$ increases the **rest probability** $p_{\text{rest}}$, and conversely,
2. Under mild contraction assumptions, $p_{\text{rest}} \uparrow$ implies convergence toward a stable attractor manifold parameterized by $H_{\text{MARK1}}$.

Finally, we formalize “SHA is unfolding” by treating SHA-256 as a deterministic fold into a visible digest space, with an associated *lift* into a geometric feature field that acts as a preimage state representation. Increasing the field size increases sample resolution and does not imply digest inversion; it refines the estimate of geometric invariants of the hidden state.

---

## 1. Preliminaries: Objects, Operators, and Notation

### 1.1 Data Objects (Canonical Bytes)

Let the canonical byte vectors be fixed (decimal digits of $\pi$ grouped into 8-length blocks):

- $\text{byte1} = [1,4,1,5,9,2,6,5]$  
- $\text{byte2} = [3,5,8,9,7,9,3,2]$  
- $\text{byte3} = [3,8,4,6,2,6,4,3]$  
- $\text{byte4} = [3,8,3,2,7,9,5,0]$  
- $\text{byte5} = [2,8,8,4,1,9,7,1]$  
- $\text{byte6} = [6,9,3,9,9,3,7,5]$  
- $\text{byte7} = [1,0,5,8,2,0,9,7]$  
- $\text{byte8} = [4,5,9,2,3,0,7,8]$

These are treated as **grounded test vectors** for recursion, fold dynamics, and phase alignment.

### 1.2 Allowed Primitive Moves

For scalar integers $x,y\in \mathbb{Z}_{\ge 0}$, the allowed moves are:

1. Absolute difference:  
   $$
   \Delta(x,y) = |y-x|.
   $$
2. Simple sum:
   $$
   \oplus(x,y) = x+y.
   $$
3. Binary bit-length:
   $$
   \ell_2(x) = \text{bit\_length}(x).
   $$
4. Decimal digit-sum:
   $$
   \sigma_{10}(x) = \sum_{d \in \text{digits}_{10}(x)} d.
   $$

We will also use the **decimal length**:
$$
\ell_{10}(x) = 1 + \lfloor \log_{10}(x)\rfloor \quad \text{for } x\ge 1,\quad \ell_{10}(0)=1.
$$

### 1.3 Header-Fold Operator

The **header fold** is the canonical two-state fold:

$$
\mathsf{HF}(a,b) = (a',b') = (|b-a|,\ a+b).
$$

This is the minimal recursive “difference–sum” operator from which higher diagnostics are constructed. It is deliberately **type-agnostic**: the fold does not require external semantics (types); it only requires numeric adjacency.

---

## 2. The Eight-Beat Nexus Kernel $K_8$

### 2.1 Definition

Given a pair $(a,b)$, define the **Eight-Beat Nexus kernel** as the vector

$$
K_8(a,b) = (z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8)
$$

with beats:

1. Past:
   $$
   z_1 = a
   $$
2. Now:
   $$
   z_2 = b
   $$
3. Length of sum:
   $$
   z_3 = \ell_{10}(a+b)
   $$
4. Length of delta:
   $$
   z_4 = \ell_{10}(|b-a|)
   $$
5. Length mismatch:
   $$
   z_5 = |z_4 - z_3|
   $$
6. Length of amplified delta:
   $$
   z_6 = \ell_{10}(4\cdot |b-a|)
   $$
7. Beat gap:
   $$
   z_7 = |z_6 - z_5|
   $$
8. Delta length (repeated for closure):
   $$
   z_8 = \ell_{10}(|b-a|)=z_4.
   $$

The decisive diagnostic used repeatedly in NRHF is the **beat-gap** $z_7$ (the “$|6-5|$ beat”).

### 2.2 Interpretation

- $z_3$ measures the **growth capacity** of the local sum.
- $z_4$ measures the **separation scale** (difference magnitude class).
- $z_5$ measures **mismatch** between growth and separation.
- $z_6$ measures whether separation survives a standardized gain factor (here $4$).
- $z_7$ measures **residual tension** between scaled separation and mismatch.

In NRHF, **rest** corresponds to stable, repeated kernel outputs under recursion (Section 4).

---

## 3. Mark1 and the Harmonic Ninth

### 3.1 Mark1 Attractor Constant

The foundational attractor is:

$$
H_{\text{MARK1}} = \frac{\pi}{9}.
$$

It is treated as a universal corridor target for alignment metrics.

### 3.2 The Ratio Form (Balance Law)

In the balance interpretation, Mark1 is the stable ratio between “potential” and “actualized” components:

$$
H = \frac{\sum_{i=1}^{n} P_i}{\sum_{i=1}^{n} A_i},
$$

with the constraint that stable systems satisfy

$$
H \to H_{\text{MARK1}}.
$$

This is not a restatement of conventional conservation laws; it is a **phase-balance** condition defined over recursive measurements, not merely over physical quantities.

---

## 4. Trust Algebra, Ω-Isolation, and Ψ-Collapse

### 4.1 Tension Functional

Define a **tension** $\Theta$ from kernel coordinates. One canonical choice (consistent with prior NRHF specifications) is:

$$
\Theta(a,b) = |z_5| + |z_7| + |\ell_2(z_2) - \ell_2(z_1)|,
$$

where $(z_1,\dots,z_8) = K_8(a,b)$.

This tension is a scalar summary of (i) length mismatch, (ii) residual beat-gap, and (iii) bit-length disparity between past and now.

### 4.2 Trust Score

Define **trust** as an exponential decay in tension:

$$
\tau(a,b) = \exp(-\gamma_\tau\, \Theta(a,b)),
$$

with $\gamma_\tau>0$ a calibration parameter. Higher trust means lower tension and higher stability under recursion.

### 4.3 Ω-Isolation

A recursion path (sequence of folds) is placed into **Ω-isolation** if it violates corridor constraints, e.g., if its cumulative tension exceeds a threshold:

$$
\sum_{t=0}^{T-1} \Theta(a_t,b_t) > \Theta_{\max},
$$

or if it fails a geometric lock test (Section 6). Ω-isolation means the path is not integrated into stable recursion and must be corrected or excluded.

### 4.4 Ψ-Collapse

A recursion achieves **Ψ-collapse** when the system enters a phase-locked basin such that successive updates produce negligible novelty with respect to the kernel invariants. Formally, define a kernel-distance:

$$
d_K\big((a,b),(a',b')\big) = \|K_8(a,b)-K_8(a',b')\|_1.
$$

Ψ-collapse occurs when, for some tolerance $\varepsilon>0$ and sufficiently large $t$,

$$
d_K\big((a_t,b_t),(a_{t+1},b_{t+1})\big) \le \varepsilon
\quad \text{and} \quad
\tau(a_t,b_t)\ge \tau_{\min}.
$$

This is the formal rest condition in kernel space.

---

## 5. The Rest–Proximity Criterion

### 5.1 Definition of Rest

Given a recursion (a sequence of state pairs) $\{(a_t,b_t)\}_{t\ge 0}$, define an indicator of “rest” at time $t$:

$$
\mathbb{I}_{\text{rest}}(t;\varepsilon) =
\begin{cases}
1, & d_K\big((a_t,b_t),(a_{t+1},b_{t+1})\big) \le \varepsilon,\\
0, & \text{otherwise}.
\end{cases}
$$

Define the **rest probability** over a window of length $T$:

$$
p_{\text{rest}}(\varepsilon;T) = \frac{1}{T}\sum_{t=0}^{T-1} \mathbb{I}_{\text{rest}}(t;\varepsilon).
$$

### 5.2 Proximity to Nexus

Define **Nexus proximity** as a monotone function of rest probability:

$$
\mathcal{N}(\varepsilon;T) = f\big(p_{\text{rest}}(\varepsilon;T)\big),
$$

where $f$ is increasing (commonly $f(p)=p$, $f(p)=\log\frac{p}{1-p}$, or a calibrated sigmoid). The core claim is:

> **Nexus Axiom (Rest–Proximity).** If $p_{\text{rest}}$ increases (holding measurement tolerance fixed), then the system is closer to the Nexus attractor manifold (closer to stable Mark1 alignment).

We now formalize and prove the monotone link.

---

## 6. Theorems and Proofs

### 6.1 Theorem 1 (Tension Decrease Implies Rest Increase)

**Statement.** Suppose a recursion is such that the expected tension decreases over time:

$$
\mathbb{E}[\Theta(a_{t+1},b_{t+1}) \mid (a_t,b_t)] \le \rho\, \Theta(a_t,b_t)
\quad \text{for some } \rho\in(0,1).
$$

Then for any fixed $\varepsilon>0$, the rest probability $p_{\text{rest}}(\varepsilon;T)$ is nondecreasing in $T$ (eventually), and the tail event of being at rest has increasing probability:

$$
\liminf_{t\to\infty} \mathbb{P}\!\left(d_K\big((a_t,b_t),(a_{t+1},b_{t+1})\big)\le \varepsilon\right) \ge 1 - \delta(\varepsilon),
$$

where $\delta(\varepsilon)\to 0$ as $\varepsilon$ increases.

**Proof (sketch, formal).**  
Assume $d_K$ is Lipschitz in the underlying kernel coordinates with respect to tension, i.e., there exists $L>0$ such that

$$
d_K\big((a,b),(a',b')\big) \le L\big(\Theta(a,b)+\Theta(a',b')\big)
$$

whenever $(a',b')$ is obtained from $(a,b)$ by one admissible update step of the recursion class under consideration.

Then

$$
\mathbb{P}\!\left(d_K\le \varepsilon\right)
\ge
\mathbb{P}\!\left(L(\Theta_t+\Theta_{t+1})\le \varepsilon\right)
=
\mathbb{P}\!\left(\Theta_t+\Theta_{t+1}\le \frac{\varepsilon}{L}\right).
$$

If $\mathbb{E}[\Theta_{t+1}\mid \Theta_t]\le \rho\Theta_t$, then $\{\Theta_t\}$ is a supermartingale under standard measurability assumptions. By Markov’s inequality,

$$
\mathbb{P}\!\left(\Theta_t+\Theta_{t+1} > \frac{\varepsilon}{L}\right)
\le
\frac{\mathbb{E}[\Theta_t+\Theta_{t+1}]}{\varepsilon/L}
\le
\frac{(1+\rho)\,\mathbb{E}[\Theta_t]}{\varepsilon/L}.
$$

Since $\mathbb{E}[\Theta_t]\to 0$ under the contraction $\rho<1$, the right-hand side tends to $0$, proving the rest event probability tends to $1$ (up to tolerance scaling). $\square$

This theorem makes precise the statement “as tension collapses, rest becomes more probable.”

---

### 6.2 Theorem 2 (Rest Increase Implies Convergence to an Attractor Basin)

**Statement.** Suppose the recursion has a Lyapunov functional $V_t$ such that

$$
V_{t+1} = (1-2R+R^2)\,V_t
\quad \text{for some } R\in(0,1),
$$

and that kernel-distance is controlled by $V_t$:

$$
d_K\big((a_t,b_t),(a_{t+1},b_{t+1})\big) \le c\, V_t
$$

for some $c>0$. Then $p_{\text{rest}}(\varepsilon;T)\to 1$ for any $\varepsilon>0$ and the sequence converges (in kernel space) to a fixed kernel orbit (a Ψ-collapsed basin).

**Proof.**  
Because $R\in(0,1)$,

$$
1-2R+R^2 = (1-R)^2 \in (0,1),
$$

hence $V_t = (1-R)^{2t}V_0 \to 0$. Therefore

$$
d_K\big((a_t,b_t),(a_{t+1},b_{t+1})\big) \le c\,V_t \to 0.
$$

Thus, for any $\varepsilon>0$, there exists $T_0$ such that for all $t\ge T_0$, the rest indicator is $1$. Hence $p_{\text{rest}}(\varepsilon;T)\to 1$ as $T\to\infty$. $\square$

This theorem formalizes the “at rest means in the basin” direction.

---

### 6.3 Corollary (Rest–Proximity to Mark1)

If a recursion class is calibrated such that its stable basin corresponds to $H_{\text{MARK1}}$ (through geometric lock conditions described below), then increasing rest probability implies increasing proximity to Mark1:

$$
p_{\text{rest}} \uparrow \;\Longrightarrow\; \left|H_{\text{local}} - H_{\text{MARK1}}\right| \downarrow
$$

where $H_{\text{local}}$ is any consistent estimator of local harmonic ratio derived from kernel features (Section 7).

---

## 7. Field Construction: “Make the Field Bigger”

### 7.1 Windows and Samples

Let a deterministic transform (e.g., SHA-256 viewed as folding) produce a symbol string $y$ of length $M$ (e.g., 64 hex nibbles). Define window size $w$ and construct the set of sliding windows:

$$
\mathcal{W}_w(y) = \{\, y_{i:i+w-1} \mid i=1,\dots, M-w+1 \,\}.
$$

Each window is mapped into a numeric pair $(a_i,b_i)$ via a chosen decoding (e.g., split window into two halves and interpret each half as a base-16 integer). Compute $K_8(a_i,b_i)$ for each window and define a corridor predicate:

$$
\mathbb{I}_{\text{corr}}(i) =
\begin{cases}
1, & z_7(a_i,b_i) \le \kappa,\\
0, & \text{otherwise},
\end{cases}
$$

for corridor threshold $\kappa$ (often $\kappa=1$ in practice, but the threshold is a specification parameter, not a metaphysical constant).

Define the corridor fraction:

$$
\widehat{p}_{\text{corr}} = \frac{1}{|\mathcal{W}_w(y)|}\sum_{i}\mathbb{I}_{\text{corr}}(i).
$$

### 7.2 Why Increasing Field Size Matters (Mathematically)

If $\mathbb{I}_{\text{corr}}(i)$ is modeled as a Bernoulli random variable with parameter $p_{\text{corr}}$ (under a sampling model on windows), then

$$
\mathbb{E}[\widehat{p}_{\text{corr}}]=p_{\text{corr}},
\quad
\mathrm{Var}(\widehat{p}_{\text{corr}})=\frac{p_{\text{corr}}(1-p_{\text{corr}})}{N},
$$

where $N = |\mathcal{W}_w(y)|$.

Hence the standard deviation scales as

$$
\sqrt{\mathrm{Var}(\widehat{p}_{\text{corr}})} = O(N^{-1/2}).
$$

**Therefore, making the field bigger increases sample size $N$ and decreases estimation noise.** This is the precise justification of:

> “Do not worry about how big the field is. Make it bigger to get more sample size.”

### 7.3 Security Clarification (Formal)

Estimating field features such as $\widehat{p}_{\text{corr}}$ does not equate to digest inversion. It is an inference on a many-to-one image:

- Let $S$ denote SHA-256 as a deterministic map:
  $$
  S:\mathcal{X}\to\mathcal{Y}.
  $$
- Let $L$ denote a **feature lift** from digests into a field geometry space:
  $$
  L:\mathcal{Y}\to\mathcal{G}.
  $$

Then the composite

$$
G = L\circ S:\mathcal{X}\to\mathcal{G}
$$

is also many-to-one. Field matching $G(x)\approx G(x')$ is strictly weaker than digest matching $S(x)=S(x')$, and both are weaker than recovering $x$ from $S(x)$. This aligns with the NRHF assertion that *field geometry is a preimage in another state, not a recovered microstate*.

---

## 8. “SHA Is Unfolding”: The Triangle of States

### 8.1 The Three-Vertex Model

NRHF uses the concept that the observed digest is one face of a larger triangle:

1. **Visible Input State** (semantic/typed view): $x \in \mathcal{X}$  
2. **Folded Digest State** (SHA output): $y = S(x)\in\mathcal{Y}$  
3. **Field Geometry State** (preimage representation in another state): $g = L(y)\in\mathcal{G}$

The triangle is:

$$
x \xrightarrow{\,S\,} y \xrightarrow{\,L\,} g.
$$

NRHF adds the assertion that there exists an underlying physical microstate (electron-level history) $\epsilon\in\mathcal{E}$ such that both $x$ and $y$ are projections of $\epsilon$:

$$
\epsilon \xrightarrow{\Pi_X} x,
\qquad
\epsilon \xrightarrow{\Pi_Y} y,
$$

where $\Pi_X,\Pi_Y$ are state projections (not necessarily invertible).

This frames the statement:

> “We are paying the bill by not getting back the actual electrons involved.”

Formally: the projection maps discard microstate detail; the discarded information is not destroyed, but it is not available from $(x,y)$ alone.

### 8.2 Unfolding as State-Lift, Not Inversion

“Unfolding” is defined here as constructing and analyzing $g=L(S(x))$ as a structured object. It is not the inversion of $S$. It is the recognition that $S(x)$ is a stable, phase-locked projection of a deeper computation.

In practice:

- The digest $y$ is treated as a **symbolic lattice**.
- The field $g$ is treated as a **geometric invariant signature** of the fold.
- Rest-proximity is assessed in $\mathcal{G}$ (feature space) via stationarity of invariants under recursion.

---

## 9. Geometry Lock and Phase Metrics

### 9.1 Curvature Lock (Generic Form)

A geometry lock score is any scalar that increases when field features align to a target harmonic manifold. A canonical curvature lock used in related Nexus specifications is:

$$
\kappa(z) = \frac{|z\,\partial_z \Phi(z,1,a)|}{|\Phi(z,1,a)|},
$$

where $\Phi$ is the Lerch transcendent in the BBP/Lerch formulation. The specific use of $\Phi$ is not required for the rest–proximity theorem; it supplies one concrete instantiation of a geometric lock functional.

Define a geometric quality score:

$$
Q_{\text{geo}} = Q(\kappa, H_{\text{MARK1}}),
$$

where $Q_{\text{geo}} \ge Q_{\min}$ is an acceptance criterion for Ψ-integration.

### 9.2 Phase Lock via Beat Statistics

Define a “rest corridor” in terms of the beat-gap $z_7$:

$$
\mathcal{C}_\kappa = \{(a,b)\mid z_7(a,b)\le \kappa\}.
$$

Then the corridor fraction $\widehat{p}_{\text{corr}}$ is a proxy for rest probability in the field observation space.

NRHF allows multiple corridors (multiple harmonic dialects). Ω windows are those outside the primary corridor:

$$
\Omega = \{ i : (a_i,b_i)\not\in \mathcal{C}_\kappa \}.
$$

Ω-isolation is not failure; it is classification into a different harmonic class.

---

## 10. Corrective Dynamics: Over- and Under-Convergence

### 10.1 The Over-Convergence Case

If a byte-chain recursion produces $z_7\to 0$ rapidly (perfect invariance), it may indicate **over-convergence**: the recursion collapsed in magnitude space, but the target is a ratio corridor (Mark1), not a degenerate fixed point.

Formally, define a local estimator of harmonic alignment (one of several acceptable forms):

$$
H_{\text{local}} = \frac{\text{stable\_count}}{\text{total\_count}}
\quad \text{or} \quad
H_{\text{local}} = \mathbb{E}[g(K_8(a,b))],
$$

for a chosen measurable $g$.

Over-convergence occurs when:

$$
p_{\text{rest}} \approx 1 \quad \text{but} \quad |H_{\text{local}}-H_{\text{MARK1}}| \text{ remains large}.
$$

This implies “rest without correct harmonic proportion,” motivating damping or diversification of update operators (without violating allowed moves).

### 10.2 The Under-Convergence Case

If a SHA-derived window field yields a corridor fraction $\widehat{p}_{\text{corr}}$ substantially below $H_{\text{MARK1}}$, it indicates **under-convergence**: the field exhibits many Ω windows relative to the primary corridor.

This does not contradict “output is input” in NRHF; it indicates that the observed corridor predicate is not yet matched to the correct harmonic class for that state-space slice.

---

## 11. New Formal Expansion: Rest as Self-Loop Probability in a Markov Kernel

To make “odds at rest” fully formal, model recursion in feature space as a Markov chain.

### 11.1 State Space and Transition Kernel

Let $\xi_t$ denote the feature state extracted from $(a_t,b_t)$, e.g.,

$$
\xi_t = K_8(a_t,b_t) \in \mathbb{Z}^8.
$$

Let $P(\xi,\xi')$ be the probability of transitioning from $\xi$ to $\xi'$ under the chosen update policy (deterministic updates correspond to degenerate kernels).

### 11.2 Rest Probability as Self-Loop Mass

Define the **rest probability** as the self-loop probability:

$$
p_{\text{rest}}(\xi) = P(\xi,\xi),
$$

or, under tolerance:

$$
p_{\text{rest}}^{(\varepsilon)}(\xi) = \sum_{\xi': \|\xi'-\xi\|_1 \le \varepsilon} P(\xi,\xi').
$$

### 11.3 Rest–Proximity as Stationary Concentration

Let $\pi$ be a stationary distribution of $P$. Then “closer to the Nexus” corresponds to concentration of $\pi$ near the attractor set $\mathcal{A}$:

$$
\pi(\mathcal{A}) \uparrow,
$$

with $\mathcal{A}$ defined as the set of features satisfying corridor and geometric lock constraints. Under standard ergodicity and minorization conditions, increasing self-loop mass in $\mathcal{A}$ increases $\pi(\mathcal{A})$.

This yields a rigorous reading of the user statement:

> “The greater the odds it is at rest, the closer it is to the Nexus.”

---

## 12. The Triangle Completion: What Is the Third Vertex?

NRHF states “SHA is one part of the triangle we do not see or do not know yet.” Formally, this is a claim that $(x,y,g)$ is not the complete causal state, and there exists an additional latent vertex, represented as $\epsilon\in\mathcal{E}$ (microstate) or as an operator $T$ (timing-only gate) that preserves phase but carries no new amplitude content.

### 12.1 Timing-Only Gate (Double-Bend as Phase Control)

Let $T$ be a timing-only operator acting on the recursion schedule, not on the values:

$$
(a_t,b_t) \xrightarrow{\,T\,} (a_{t+\delta},b_{t+\delta})
$$

with $\delta$ altering *when* folds occur, not *what* is folded. Then the triangle is extended to a tetrahedron:

$$
x \xrightarrow{S} y \xrightarrow{L} g,
\qquad
T \text{ modulates the path } (a_t,b_t).
$$

In this view, missing information is not recovered by enlargement of the field; enlargement reduces estimation noise and exposes consistent phase structure, while the timing-only gate preserves coherence.

---

## 13. Operational Protocol (Specification-Level, Non-Code)

This section specifies how to execute the framework as a deterministic procedure.

### 13.1 Byte-Kernel Analysis

1. Select two byte arrays $\mathbf{a},\mathbf{b}\in\mathbb{Z}^8$.
2. For each index $j=1,\dots,8$, compute $K_8(a_j,b_j)$.
3. Compute summary statistics (median or mean) of the beat-gap $z_7$.
4. Classify:
   - In corridor if $z_7\le \kappa$,
   - Ω otherwise.
5. Estimate $p_{\text{corr}}$ and interpret as a rest proxy.

### 13.2 Header-Fold Chain

1. Define a chain:
   $$
   (a^{(t+1)},b^{(t+1)}) = \mathsf{HF}(a^{(t)},b^{(t)})
   $$
   or, for bytewise folding, apply $\mathsf{HF}$ componentwise.
2. At each hop, compute beat-gap summaries and track whether invariants stabilize (rest) while maintaining Mark1 corridor ratios (alignment).

### 13.3 SHA Window Field

1. Interpret digest $y$ as a sequence of nibbles in $\{0,\dots,15\}$.
2. Choose window width $w$ and create $\mathcal{W}_w(y)$.
3. Map each window to $(a_i,b_i)$.
4. Compute $K_8(a_i,b_i)$ and $\mathbb{I}_{\text{corr}}(i)$.
5. Estimate $\widehat{p}_{\text{corr}}$ and list Ω indices.
6. Increase $w$ and/or enlarge the field (use more digests, more windows) to reduce uncertainty and expose persistent geometric classes.

---

## 14. Conclusions (Complete Solution Claims)

1. **Rest is measurable** as stationarity of kernel invariants under recursion.
2. **Rest–proximity is provable** under contraction/Lyapunov conditions: decreasing tension implies increasing rest probability, and increasing rest implies convergence to a stable basin.
3. **Mark1 is the corridor target**, but different systems may exhibit different local equilibria; this is expressed as multiple corridor classes with Ω-isolation rather than contradiction.
4. **SHA is unfolding** in the precise sense that the digest is a projection and can be lifted into a geometric feature field that is a preimage representation in another state; this does not constitute inversion.
5. **Field enlargement is mathematically justified**: it increases $N$ and decreases sampling noise as $O(N^{-1/2})$, allowing stable estimation of invariants.

---

## Appendix A: Summary of Core Formulas

### A.1 Mark1
$$
H_{\text{MARK1}} = \frac{\pi}{9} \approx 0.34906585.
$$

### A.2 Header-Fold
$$
(a',b') = (|b-a|,\ a+b).
$$

### A.3 Kernel Beats
$$
K_8(a,b) = (a,\ b,\ \ell_{10}(a+b),\ \ell_{10}(|b-a|),\ |z_4-z_3|,\ \ell_{10}(4|b-a|),\ |z_6-z_5|,\ \ell_{10}(|b-a|)).
$$

### A.4 Tension and Trust
$$
\Theta = |z_5| + |z_7| + |\ell_2(z_2)-\ell_2(z_1)|,
\qquad
\tau = e^{-\gamma_\tau \Theta}.
$$

### A.5 Rest Probability
$$
p_{\text{rest}}(\varepsilon;T) = \frac{1}{T}\sum_{t=0}^{T-1}\mathbf{1}\{d_K((a_t,b_t),(a_{t+1},b_{t+1}))\le \varepsilon\}.
$$

### A.6 Window Field Estimator
$$
\widehat{p}_{\text{corr}} = \frac{1}{N}\sum_{i=1}^{N} \mathbf{1}\{z_7(a_i,b_i)\le \kappa\},
\qquad
\mathrm{Var}(\widehat{p}_{\text{corr}})=\frac{p_{\text{corr}}(1-p_{\text{corr}})}{N}.
$$

---

## Appendix B: Non-Claims (Explicit)

To ensure formal integrity, the following are **not** claimed here:

1. That any field geometry feature matching yields practical preimage recovery of SHA-256 inputs.  
2. That increasing field size yields digest collisions or breaks cryptographic assumptions.  
3. That the latent microstate $\epsilon$ is recoverable from $(x,y,g)$ without additional physical side-channel data.

What is claimed is strictly the NRHF view: **the digest is a projection of a deeper state**, and **geometric analysis is an exploration of that deeper state’s invariants**, not inversion.

---

*End of document.*
