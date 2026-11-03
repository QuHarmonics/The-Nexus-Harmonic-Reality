# Nexus Genlock Notes: SILR, Hot/Cold Folding, 9D + Parity

This document consolidates the *mechanism* behind:

- **SILR** (Scale-Invariant Leakage Regime) as a self-normalizing control phase  
- **GENLOCK** as a tunable leakage target near **$H \approx 0.35$** (often **$H = \pi/9$**)  
- **HOT / COLD / SHIT** as *local folding outcomes* of an invariant 90° leakage stream  
- **9 dimensions + a 10th “parity dimension”** as an XOR-closure / stack-consistency constraint  
- The “residual field” idea: **unmatched truth** that bleeds orthogonally and can be re-consumed when trajectories intersect.

---

## 1) IF/THEN vs IF/WHEN

### Human logic
We experience a conditional world:

- **IF/THEN**: “If X happens, then Y follows.”

This is *computing a branch*.

### Universe geometry
The manifold already contains intersections:

- **IF/WHEN**: “If the vectors cross, *then it happens when the world-line reaches that crossing*.”

No “decision tree” is required by the manifold; the “branching” is an observer’s model of incomplete information.

Let two world-lines be parameterized as:

$$
x_A(t),\; x_B(t)
$$

A collision is an **intersection event**:

$$
\exists\, (t_A,t_B):\quad x_A(t_A)=x_B(t_B)
$$

The event is geometric; “prediction” is epistemic.

---

## 2) SILR: the scale-invariant leakage gate (the actual math)

### 2.1 Variables

- Target / attractor: **$\alpha^*$** (often near **$\pi/9$**)  
- Estimate: **$\hat\alpha_t$**  
- Reported standard error (uncertainty): **$\mathrm{SE}_t$**  
- Normalized deviation (**z-score**):

$$
z_t = \frac{|\hat\alpha_t - \alpha^*|}{\mathrm{SE}_t}
$$

Leakage probability (sigmoid gate):

$$
p_t = \sigma\big(\beta\,(z_t - z_0)\big),
\qquad
\sigma(u)=\frac{1}{1+e^{-u}}
$$

Here **$\beta$** is gain (steepness) and **$z_0$** is the normalized threshold.

### 2.2 The SILR assumption (matched scaling)

Assume the estimator noise *matches* the reported uncertainty:

$$
\hat\alpha_t = \alpha^* + \mathrm{SE}_t\,\varepsilon_t,
\qquad
\varepsilon_t \sim \mathcal N(0,1)
$$

Then:

$$
z_t
= \frac{|\mathrm{SE}_t\varepsilon_t|}{\mathrm{SE}_t}
= |\varepsilon_t|
$$

**The scale cancels.**  
So **$z_t$** follows the **half-normal distribution**, independent of **$\mathrm{SE}_t$**:

$$
f_Z(z)=\sqrt{\frac{2}{\pi}}\,e^{-z^2/2},
\qquad z\ge 0
$$

### 2.3 Consequence (invariance)

Because **$p_t$** depends only on **$z_t$**, and **$z_t$** depends only on **$|\varepsilon_t|$**, we get:

$$
\mathbb E[p_t]
= \int_0^{\infty}
\sigma\big(\beta(z-z_0)\big)
\sqrt{\frac{2}{\pi}}e^{-z^2/2}\,dz
\quad\text{(depends on }\beta,z_0\text{ only)}
$$

So:

$$
\frac{\partial\,\mathbb E[p_t]}{\partial\,\mathrm{SE}} = 0
\quad\text{(SILR phase)}
$$

That’s the *Scale-Invariant Leakage Regime*: the controller “feels” only significance, not magnitude.

### 2.4 The “illusion of stability” (important)

Even if **$\mathbb E[p_t]$** is invariant, *absolute excursions* grow with **$\mathrm{SE}$**.

If “glyph coherence” is defined by a fixed absolute tolerance **$\tau$**:

$$
\text{collapse} = \Pr\left(|\hat\alpha_t-\alpha^*|<\tau\right)
$$

then increasing **$\mathrm{SE}$** decreases collapse even though the controller’s internal gate statistics are unchanged.  
This is the key split:

- **controller-level invariance** (SILR)  
- **world-line consequence** (absolute drift still hurts)

---

## 3) GENLOCK: choosing the leak rate (tuning $z_0$ so the mean leak equals $H$)

If you want SILR to act like a **universal clock / genlock**, you don’t just say “SILR exists.”  
You **choose** the gate parameters so that:

$$
\mathbb E[p_t] = H
$$

### 3.1 Step-gate limit (clean closed form)

As **$\beta\to\infty$**, the sigmoid becomes a step function:

$$
p_t \to \mathbf 1\{z_t>z_0\}
$$

Then:

$$
\mathbb E[p_t]=\Pr(Z>z_0)=1-\operatorname{erf}\left(\frac{z_0}{\sqrt 2}\right)
$$

So to set **$\mathbb E[p_t]=H$**, pick:

$$
z_0(H) = \sqrt 2\,\operatorname{erf}^{-1}(1-H)
$$

Numerics:

- For **$H=\pi/9\approx 0.349066$**:

$$
z_0 \approx 0.936403
$$

- For **$H=0.35$**:

$$
z_0 \approx 0.934589
$$

### 3.2 Finite gain example (common: $\beta=5$)

For **$\beta=5$**, solving the integral numerically gives approximately:

- **$H=\pi/9$**: **$z_0\approx 0.992558$**
- **$H=0.35$**: **$z_0\approx 0.990612$**

So: **GENLOCK = SILR + a chosen target mean leak**.

---

## 4) HOT / COLD / SHIT as what SILR “does for us”

You said it cleanly: **SILR does the hot and cold for us.**

Mechanically:

- The **SILR stream** is the invariant arrival of “potential / noise / novelty.”
- A manifold (observer/system) either *folds it* into structure or lets it pass through.

### 4.1 Decompose the incoming “innovation” into tangent vs normal

Let the incoming increment (stimulus / update / perturbation) be a vector **$u_t$** in a local state space.  
Decompose into:

- tangent component (engages the system’s model / learned manifold): **$u_T$**
- normal component (orthogonal; passes through as residue): **$u_N$**

$$
u_t = u_T + u_N,
\qquad
u_T \perp u_N
$$

Define “engaged fraction”:

$$
\rho_t = \frac{\|u_T\|^2}{\|u_T\|^2 + \|u_N\|^2}
\in [0,1]
$$

Interpretation:

- **COLD**: small **$\rho_t$** (mostly orthogonal pass-through)
- **HOT**: large **$\rho_t$** (mostly absorbed into structure)
- **SHIT**: the system engages ($\rho_t$ moderate/high) but folds incorrectly → wrong projection / wrong attractor basin

SILR gives the invariant *supply*; HOT/COLD describes the local *capture*.

### 4.2 Why “90°” keeps appearing

Orthogonality is the no-interaction channel:

- normal component **$u_N$** is effectively “90°” to the processing surface.
- it is the exhaust / side-effect / residue of mismatch.

A constant stream can be good or bad depending on content:

- air (compatible) → survivable fold  
- poison (incompatible) → lethal fold  

The leak rate (SILR) can be constant while outcomes differ because *content + manifold* differs.

---

## 5) The residual field (unmatched truth, not garbage)

“GIGO” is the wrong metaphor. Under this model:

- **unmatched** does not mean **false**  
- it means **orthogonal to current context**

A minimal reservoir model:

$$
R_{t+1} = (1-\gamma)R_t + \gamma\,u_{N,t}
$$

- **$R_t$** is residual “silt” of orthogonal components
- **$\gamma$** sets how much gets stored

Re-consumption happens if the manifold basis rotates so that yesterday’s normal component becomes today’s tangent component:

$$
\text{reconsume at }t
\iff
\|P_T(t)\,R_t\| \text{ is large}
$$

where **$P_T(t)$** is the projector onto today’s tangent subspace.

---

## 6) 9D + parity (10th as XOR closure)

Let the system state be a 9-bit vector:

$$
s\in\{0,1\}^9
$$

Define the parity bit (10th dimension) as XOR of all 9:

$$
p = \bigoplus_{i=1}^{9} s_i
$$

Then the 10th coordinate is not independent; it is a constraint:

$$
(s,p)\in\{0,1\}^{10}
\quad\text{with}\quad
p = \oplus s
$$

This matches “there is no 10”:

- The 10th “dimension” is stack integrity (closure)
- It can “cancel” because XOR is its own inverse:

$$
x\oplus x = 0
$$

### 6.1 Folding “10 → 5” (a plausible algebraic picture)

If the 10th bit is parity, then pairing a bit with its parity-conjugate can reduce effective degrees of freedom. One simple model:

- group bits into 5 pairs
- treat each pair as a folded unit with a parity constraint

This is not a proof of “10 folds to 5,” but it’s a mathematically consistent meaning of that statement: parity removes one independent DOF and encourages pairwise folding.

---

## 7) Turning the “Gemini punch list” into a paper spine

Gemini’s draft is useful as a map of themes, but it needs a mechanism-first backbone.

Build around three load-bearing theorems:

1. **SILR theorem (self-normalization):**  
   $$z_t=|\varepsilon_t|\Rightarrow\mathbb E[p_t]\text{ independent of }\mathrm{SE}$$

2. **GENLOCK calibration:**  
   $$\mathbb E[p_t]=H\Rightarrow z_0(H)=\sqrt 2\,\operatorname{erf}^{-1}(1-H)\;(\beta\to\infty)$$

3. **Outcome decomposition (HOT/COLD/SHIT):**  
   $$u_t=u_T+u_N,\; u_T\perp u_N,\; \rho_t=\frac{\|u_T\|^2}{\|u_t\|^2}$$

Everything else (Universe 000, ROM metaphor, chemical opcodes, SHA “weird machine”) should be labeled as:

- **Derived** (implied by the mechanism), or  
- **Hypothesis** (interpretation), plus a test plan.

That single change removes the “checklist vibe.”

---

## 8) What to test next (falsifiable, minimal)

1. **SILR invariance test:** sweep $\mathrm{SE}$ under matched noise; confirm the distribution of $z_t$ is invariant.

2. **GENLOCK tuning:** choose $(\beta,z_0)$ so that $\mathbb E[p_t]=\pi/9$ (or the desired band center); verify mean leakage stays fixed across SE scales.

3. **Break symmetry with mismatch factor $\Gamma$:**

$$
\hat\alpha_t = \alpha^* + \Gamma\,\mathrm{SE}\,\varepsilon_t
\quad\Rightarrow\quad
z_t = \Gamma|\varepsilon_t|
$$

Then:

- $\Gamma=1$: SILR (adiabatic / self-normalized)  
- $\Gamma>1$: radiant (over-leak)  
- $\Gamma<1$: condensate (under-leak)

4. **HOT/COLD partition measurement:** define a proxy for $\rho_t$ (projection onto learned subspace, gradient alignment, variance explained). Test whether hot fraction clusters near the attractor band.

---

## 9) Constants in the attractor band (reference)

Numerically:

- $$\frac{\pi}{9}\approx 0.349066$$
- $$\frac{1}{e}\approx 0.367879$$
- $$\frac{1}{\varphi^2}\approx 0.381966,\quad \varphi=\frac{1+\sqrt 5}{2}$$
- $$\frac{2.5}{7}\approx 0.357143$$

A practical band you can operationalize:

$$
\mathcal B = \left[\frac{\pi}{9},\; \frac{1}{\varphi^2}\right]
\approx [0.349,\; 0.382]
$$

Treat “wobble” as drift within $\mathcal B$ when multiple attractors compete.

---

### Closing sentence (mechanism-first)

SILR is the scale-invariant supply of orthogonal novelty; GENLOCK is choosing the mean leak in that regime; HOT/COLD/SHIT are local outcomes of whether the manifold folds the stream, lets it pass, or folds it wrong; and 9D+parity makes “dimension 10” a closure constraint rather than a new degree of freedom.
