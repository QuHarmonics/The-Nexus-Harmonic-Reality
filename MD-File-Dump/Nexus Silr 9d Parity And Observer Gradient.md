# Nexus: SILR, 9-Dimensional Base, and Parity as Folding

This document consolidates the current Nexus thread into a **math-first** statement:

- **SILR** is a self-normalizing leakage law (a *genlock*).
- The **9-state base** is where the “~0.35” ratio emerges combinatorially.
- The **10th “dimension” is parity**: not an independent axis, but an **identification/fold** (XOR / anti-phase pairing).
- **HOT / COLD / SHIT** are *decision-regimes* of the same gate: how much of the stream is *actually assimilated* vs *passes through* vs *mis-collapses*.

---

## 1) Interface vs implementation (so we don’t get trapped in nouns)

- **Interface**: what a subsystem *advertises* (what it can couple to). Think ports/types/compatibility.
- **Implementation**: what actually happens once coupled.

“Need” lives at the interface: it is a **gradient** in “what would reduce mismatch”.

---

## 2) Two flows: universal leakage vs local processing

### 2.1 Universal stream (SILR)

Let the universe deliver a base stream:

$$U(t)$$

This stream is **always present**.

### 2.2 Local processing is gradient pressure

Let an observer have state $s(t)$ and mismatch functional $J(s)$.

Passive:
$$\nabla J(s) \approx 0$$

Active (trying to solve / compute):
$$\nabla J(s) \neq 0$$

A minimal dynamical form:

$$\dot s(t) = -\nabla J(s(t)) + \eta(t)$$

This is the clean version of:

> “We don’t move; data flows and we put pressure in directions.”

Same physics, two frames: you moving through the field vs the field moving relative to you.

---

## 3) SILR theorem (Scale-Invariant Leakage under Z-score gating)

### 3.1 Gate definition

Let $\alpha_*=\pi/9$ be the attractor target.

With estimate $\hat\alpha_t$ and standard error $SE_t$:

$$z_t=\frac{|\hat\alpha_t-\alpha_*|}{SE_t}$$

Leakage probability:

$$p_t=\sigma\big(\beta(z_t-z_0)\big),\qquad \sigma(x)=\frac{1}{1+e^{-x}}$$

### 3.2 Calibration assumption

Assume the estimator noise matches the reported uncertainty:

$$\hat\alpha_t=\alpha_*+\varepsilon_t,\qquad \varepsilon_t\sim\mathcal N(0,SE_t^2)$$

Then:

$$z_t=\frac{|\varepsilon_t|}{SE_t}$$

Write $\varepsilon_t=SE_t Z$ with $Z\sim\mathcal N(0,1)$:

$$z_t=\frac{|SE_tZ|}{SE_t}=|Z|$$

**Scale cancels.** Therefore:

$$z_t\sim\text{HalfNormal}(0,1)$$

and the full distribution of $p_t$ depends only on $(\beta,z_0)$, not on the scale of $SE_t$.

---

## 4) “SILR does HOT and COLD for us” (made explicit)

Pick a “hot” threshold $p_{\text{hot}}$ (anything you like).

Because $p_t$ is monotone in $z_t$:

$$p_t\ge p_{\text{hot}}
\iff
z_t \ge z_0+\frac{1}{\beta}\ln\left(\frac{p_{\text{hot}}}{1-p_{\text{hot}}}\right)$$

So:

$$\Pr(\text{HOT})=\Pr\left(|Z|\ge z_0+\frac{1}{\beta}\ln\left(\frac{p_{\text{hot}}}{1-p_{\text{hot}}}\right)\right)$$

This probability is **independent of noise scale** when the system is calibrated.

That’s the precise meaning of:

> SILR partitions the stream into hot/cold in a scale-invariant way.

---

## 5) Breaking SILR (camouflage as “lying to the gate”)

Define the mismatch factor:

$$\gamma=\frac{SE_{\text{true}}}{SE_{\text{used}}}$$

Then:

$$z_t=\gamma|Z|$$

and:

$$p_t(\gamma)=\sigma\big(\beta(\gamma|Z|-z_0)\big)$$

Interpretation:

- **Hide/protect**: increase $SE_{\text{used}}$ so $\gamma<1$ → your deviations look insignificant.
- **Strike/reveal**: decrease $SE_{\text{used}}$ so $\gamma>1$ → deviations look significant.

This matches your “camo can protect to hide or protect to strike” intuition:
it is the same mechanism viewed from different frames.

---

## 6) Three interaction states (ports + compilation)

Let $x$ be an incoming pattern (radon, x-ray, saw, food, message) and $s$ the observer state.

Coupling (type/port match):
$$C(x,s)\in[0,1]$$

Compilation / assimilation (integrates into internal stable structure):
$$A(x,s)\in[0,1]$$

Then:

1. **No coupling** (invisible/out-of-phase): $C\approx0$
2. **Coupling without compilation** (tool-like): $C>0,\ A\approx0$
3. **Coupling and compilation** (folds into you): $C>0,\ A>0$

Radon is the reminder that you can be “passive” and still get compiled against your will if the port exists.

---

## 7) Base-9 combinatorics: where ~0.35 shows up

Treat side lengths as base-9 digits:

$$a,b,c\in\{0,1,2,3,4,5,6,7,8\}$$

Total ordered triples:

$$9^3 = 729$$

Count valid triangles (positive sides, triangle inequality) by enumeration:

$$N_{\triangle} = 260$$

So:

$$H_{\triangle}=\frac{260}{729}\approx 0.356653$$

Degenerate (flat) cases in the same cube:

$$N_{\text{deg}} = 84$$

Reference constant band (common candidates you’ve been using):

$$\pi/9 \approx 0.349066,\quad 2.5/7 \approx 0.357143,\quad 1/e \approx 0.367879,\quad 1/\varphi^2 \approx 0.381966$$

So an attractor band is:

$$H\in[0.343,0.382]$$

---

## 8) Parity as the “10th dimension” (fold, not a free axis)

Parity is derived:

$$p=x_1\oplus x_2\oplus\cdots\oplus x_9$$

Geometrically, parity often behaves like identifying opposite phases:

$$\theta\sim\theta+\pi\quad\Rightarrow\quad \theta\mapsto \theta\bmod\pi$$

That is the “fold”.

---

## 9) SHA fold evidence (10D folded promotes 20° = π/9)

From `sha_periods.csv`:

- In **10D folded (mod $\pi$)**, the dominant period is:

$$20^\circ=\frac{\pi}{9}$$

In the dataset:

- 10D folded: rank **#1** at $20^\circ$ (top).
- 10D raw: rank **#5** at $20^\circ$.
- 9D raw: nearest peak at 21.176° is rank **#5**.

This is exactly what the fold predicts: the $\bmod\pi$ identification boosts the $\pi/9$ harmonic.

---

## Appendix: exact numbers used here

- Triangle cube: total 729, valid 260, degenerate 84
- $H_{\triangle}=0.356653$
- Band: $0.343 \le H \le 0.382$
