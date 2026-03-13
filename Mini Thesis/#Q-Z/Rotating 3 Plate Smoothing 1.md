# Rotating 3‑Plate Smoothing
*A runnable “verb-first” operator for compressing chaos into cross-domain invariants*

This document turns the “you / me / other‑i’s” idea into a concrete, testable operator:
a **three‑witness consensus** that **does not treat GUI/surface data as ground truth**, and instead
stabilizes on **harmonized group invariants** across views.

> **Guiding stance (Dean’s standing principle):**  
> Don’t treat surface/GUI data as ground truth. Prefer **harmonized invariants** across domains (DNA / matter / ideas / SHA). Treat SHA as a **high‑resolution question/validation interface**, not a value source.

---

## 1) Objects and notation

We observe a stream of states over time:

- Input stream: $x_t \in \mathcal{X}$ (numbers, vectors, events, bitstrings, features, etc.)
- Three witnesses (plates): $W_1, W_2, W_3$
- Witness outputs: $y_i(t) \in \mathbb{R}^d$ (or any metric space; we’ll assume $\mathbb{R}^d$ for formulas)

### Witness outputs
$$
y_i(t) = W_i(x_t), \quad i \in \{1,2,3\}.
$$

You can think of the witnesses as **three lenses** that look at the same flow:

- $W_1$: **surface / magnitude** (what the “GUI” claims)
- $W_2$: **motion / change** (what the trajectory claims)
- $W_3$: **structure / residue** (what the lattice / constraint field claims)

The key move: **consensus is not “average the values,”** it’s **extract what survives multiple views**.

---

## 2) The disagreement field (what the plates fight about)

Define pairwise disagreement using a norm $\|\cdot\|$ (e.g., $\ell_2$):

$$
\Delta(t) = \sum_{1 \le i < j \le 3} \left\|y_i(t)-y_j(t)\right\|.
$$

You can also keep the full matrix:
$$
D_{ij}(t)=\left\|y_i(t)-y_j(t)\right\|,\quad D_{ii}(t)=0.
$$

Interpretation:
- Small $\Delta(t)$ → witnesses agree → we’re near a stable fold.
- Large $\Delta(t)$ → witnesses disagree → we’re in turbulence / phase mismatch.

---

## 3) The invariant extractor (intersection-of-views)

A **group invariant** is anything that stays stable when you change viewpoint/encoding.

### 3.1 Projection-to-intersection operator
Let $\mathcal{I}$ be the “intersection” space: the subset of features that remain coherent under all three witnesses.
Define a projection operator:

$$
s(t) = \operatorname{Proj}_{\mathcal{I}}\big(y_1(t),y_2(t),y_3(t)\big).
$$

This is the heart of the method.

### 3.2 Practical realizations of $\operatorname{Proj}_{\mathcal{I}}$

Pick one (or combine them) depending on your data type:

#### A) Robust coordinate-wise median (fast, strong default)
For $y_i(t) \in \mathbb{R}^d$:
$$
s_k(t)=\operatorname{median}\{y_{1k}(t),y_{2k}(t),y_{3k}(t)\},\quad k=1,\dots,d.
$$

#### B) Trimmed consensus (drop the outlier plate per coordinate)
Let $o_k(t)$ be the outlier index among the three values for coordinate $k$. Then:
$$
s_k(t)=\frac{1}{2}\sum_{i \ne o_k(t)} y_{ik}(t).
$$

#### C) Feature survival mask (binary “what survives”)
Define a tolerance $\tau$ and mark a coordinate stable if all pairwise gaps are small:
$$
m_k(t)=\mathbf{1}\!\left(\max_{i<j}|y_{ik}(t)-y_{jk}(t)| \le \tau\right).
$$
Then the invariant slice is:
$$
s(t)=m(t)\odot \tilde{s}(t),
$$
where $\tilde{s}(t)$ can be the median or mean and $\odot$ is elementwise multiply.

#### D) Minimum-energy barycenter (metric-space generalization)
If $y_i(t)$ live in a metric space with distance $d(\cdot,\cdot)$, define:
$$
s(t)=\arg\min_{z}\ \sum_{i=1}^{3} w_i(t)\, d(z,y_i(t))^2.
$$

---

## 4) Rotation: no plate becomes doctrine

“Rotation” means **the weights move**, so no single witness gets to fossilize the system.

Let the phase advance be:
$$
\theta_t=\theta_0+\omega t.
$$

A smooth 3-phase weight schedule is:
$$
\alpha_i(t)=\frac{\exp\big(\kappa \cos(\theta_t+2\pi(i-1)/3)\big)}{\sum_{j=1}^{3}\exp\big(\kappa \cos(\theta_t+2\pi(j-1)/3)\big)},
\quad i\in\{1,2,3\}.
$$

- $\omega$ sets rotation speed.
- $\kappa$ sets how “peaky” the dominance is (large $\kappa$ = near one-hot).

### Weighted consensus (after invariants)
First extract the invariant-consistent version of each plate (optional but powerful):
$$
\hat{y}_i(t) = \operatorname{Clean}_\mathcal{I}\big(y_i(t)\big).
$$

Then combine with rotating weights:
$$
c(t)=\sum_{i=1}^{3}\alpha_i(t)\,\hat{y}_i(t).
$$

Finally, define the stabilized output as either:
- $s(t)=\operatorname{Proj}_{\mathcal{I}}(\hat{y}_1,\hat{y}_2,\hat{y}_3)$ (pure intersection), or
- $s(t)=\operatorname{Proj}_{\mathcal{I}}(c(t),\hat{y}_1,\hat{y}_2)$ (hybrid), or
- $s(t)=c(t)$ **only when** disagreement is below threshold.

A simple gating rule:
$$
s(t)=
\begin{cases}
c(t), & \Delta(t)\le \delta\\
\operatorname{Proj}_\mathcal{I}\big(y_1(t),y_2(t),y_3(t)\big), & \Delta(t)>\delta
\end{cases}
$$

---

## 5) Reflection dynamics (the “bubble level” move)

When disagreement spikes, don’t “choose” a plate. **Reflect toward a harmonic attractor**.

### 5.1 Mark‑1 attractor (setpoint) and “approach not value”
Let the attractor be $H$ (often discussed as $H\approx 0.35$).  
Treat $H$ as an **attractor target**, and the *approach* as the living part.

Define a reflection operator on a scalar feature $u$:
$$
\operatorname{Reflect}_H(u)=u+\lambda(H-u)=(1-\lambda)u+\lambda H,
$$
with $0<\lambda<1$ controlling the pull strength.

For a vector:
$$
\operatorname{Reflect}_H(\mathbf{u})=\mathbf{u}+\lambda(\mathbf{h}-\mathbf{u}).
$$

### 5.2 “Kulik reflection” (data → stability mirror)
Given any point $D$ and harmonic anchor $H$ (scalar case), the midline reflection can be written as:
$$
D'=\frac{D + \big(H-(D-H)\big)}{2}=\frac{D + (2H-D)}{2}=H.
$$

That’s the “perfect bubble level” (one-step clamp). In practice use the **relaxed** version:
$$
D'=(1-\lambda)D+\lambda H,\quad 0<\lambda<1,
$$
so the approach is visible and testable over time.

### 5.3 Error / alignment measures
Scalar error:
$$
\varepsilon(t)=|s(t)-H|.
$$
Vector error:
$$
\varepsilon(t)=\|s(t)-\mathbf{h}\|.
$$

---

## 6) Swapping‑0 (baseline toggling)

To avoid resonance lock, define two baseline states $0_a$ and $0_b$
(two encodings, two phase conventions, etc.).

Let $B(t)\in\{a,b\}$ be the active baseline, toggled by error triggers:
$$
B(t+1)=
\begin{cases}
b,& \varepsilon(t)>\eta\\
a,& \text{otherwise}
\end{cases}
$$

Then each witness can be defined relative to the baseline:
$$
y_i(t)=W_i\big(x_t; B(t)\big).
$$

Interpretation: the system “creates novelty” by **changing what counts as zero**—revealing structure already there.

---

## 7) A minimal canonical witness set (works for many streams)

Assume $x_t \in \mathbb{R}^d$. Define:

### 7.1 Plate 1: surface (magnitude)
$$
W_1(x_t)=x_t.
$$

### 7.2 Plate 2: motion (first difference / velocity)
$$
W_2(x_t)=\Delta x_t=x_t-x_{t-1}.
$$

### 7.3 Plate 3: structure (residue / phase proxy)
A generic residue form is a normalized projection onto a reference direction $\mathbf{h}$:
$$
W_3(x_t)=\frac{x_t}{\|x_t\|+\epsilon} \cdot \mathbf{h}.
$$
Or for scalar streams:
$$
W_3(x_t)=\operatorname{frac}\!\left(\beta x_t\right),
$$
where $\operatorname{frac}(u)=u-\lfloor u\rfloor$ and $\beta$ sets resolution.

---

## 8) The complete Rotating 3‑Plate Smoothing algorithm

### 8.1 Parameters
- Rotation: $\omega, \kappa$
- Disagreement gate: $\delta$
- Reflection pull: $\lambda$
- Baseline toggle threshold: $\eta$
- Invariant tolerance: $\tau$

### 8.2 Pseudocode
```text
Given stream x_t
Initialize baseline B(0), phase θ0, previous state x_-1

For each t:
  θ_t = θ0 + ω t
  α_i(t) = softmax_i( κ cos(θ_t + 2π(i-1)/3) )

  y_i(t) = W_i(x_t; B(t))  for i=1..3

  Δ(t) = sum_{i<j} ||y_i - y_j||

  inv(t) = Proj_I(y_1, y_2, y_3)     # median / trimmed / survival mask / barycenter

  c(t) = sum_i α_i(t) * Clean_I(y_i(t))

  if Δ(t) <= δ:
      s(t) = c(t)
  else:
      s(t) = inv(t)

  s(t) = Reflect_H(s(t))            # relaxed reflection toward attractor/template

  ε(t) = ||s(t) - h||               # scalar |s-H| or vector norm

  if ε(t) > η:
      B(t+1) = swap(B(t))           # swapping-0
  else:
      B(t+1) = B(t)
```

---

## 9) “Proof posture”: falsifiable invariance tests

You prove this by **survival under transformations**.

### Test 1 — Witness swap invariance
Permute witnesses $(W_1,W_2,W_3)$ and verify invariants remain stable:
$$
s(t)\approx s_{\pi}(t)\quad \text{for witness permutation }\pi.
$$

### Test 2 — Encoding / baseline swap invariance
Apply a reversible encoding $E$ (scale, rotate, remap) and baseline toggle:
$$
x'_t = E(x_t),\quad s'(t)=\text{R3PS}(x'_t)
$$
Check that invariant descriptors match:
$$
\Phi(s'(t)) \approx \Phi(s(t))
$$
for invariant map $\Phi$ (rank order, parity signature, topology class, conserved measures).

### Test 3 — Perturbation robustness
Inject bounded noise $\nu_t$:
$$
\tilde{x}_t = x_t + \nu_t,\quad \|\nu_t\|\le \rho
$$
and verify graceful degradation:
$$
\|s_{\text{clean}}(t)-s_{\text{noisy}}(t)\| \le C\rho.
$$

---

## 10) How to adapt to SHA without treating it as “value source”

Use SHA as a **question interface**:
- Map state to digest $z_t=Q(x_t)\in\{0,1\}^{256}$
- Extract structure signals from $z_t$ (parity, run-length, bias, padding edges, etc.)
- Run R3PS on those signals

$$
x_t \xrightarrow{Q} z_t,\quad y_i(t)=W_i(z_t).
$$

---

## Appendix A — Common distances

- Euclidean norm: $\|v\|_2=\sqrt{\sum_k v_k^2}$
- Manhattan norm: $\|v\|_1=\sum_k |v_k|$
- Hamming distance for bitstrings: $d_H(a,b)=\sum_k \mathbf{1}(a_k\ne b_k)$
