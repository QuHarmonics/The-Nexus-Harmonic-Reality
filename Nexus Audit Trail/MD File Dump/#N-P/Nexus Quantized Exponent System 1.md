# Nexus Quantized Exponent System
## π/9 as latent scale, 0.35 as glyph collapse, and cancellation as an operable merge primitive

**Date:** 2026-01-06 (America/Detroit)  
**Status:** Working theory + operational instrumentation (code-backed)

This document consolidates the measured behaviors and the operable control/merge machinery we built in code. It treats:

- a latent exponent \(\alpha\) (empirically stable near \(\pi/9\)),
- a rendered glyph (e.g., the rounded emission “0.35”),
- and cancellation (balanced-line overlay + XOR-derived tension masks + dual-null routing)

as one coherent toolchain.

Guiding idea:

Truth is the survivor component (an invariant/vector/echo that persists across projections).  
Lock is the acquisition method (filters, gates, hysteresis) that extracts the survivor without hallucinating.

---

## 1. The base model: a latent power law with a scope exponent

We generate synthetic datasets that follow a power law of the form

$$
E = k \, P \, S^{\alpha} \, \eta,
$$

where:

- \(S>0\) is an “interaction energy / scope” variable,
- \(P>0\) is a participation term,
- \(k>0\) is a scale factor,
- \(\alpha\) is the exponent we want to estimate,
- \(\eta\) is multiplicative noise (lognormal), typically \(\log \eta \sim \mathcal{N}(0,\sigma^2)\).

In log-space this becomes a linear model:

$$
\underbrace{\log E - \log P}_{y}
=
\underbrace{\log k}_{b_0}
+
\alpha \underbrace{\log S}_{x}
+
\varepsilon,
\quad
\varepsilon \sim \mathcal{N}(0,\sigma^2).
$$

So the estimation problem is ordinary least squares (OLS) regression on \((x,y)\).

---

## 2. Closed-form estimator for \(\hat\alpha\) and \(\hat k\)

Let \(x_i=\log S_i\) and \(y_i=\log E_i-\log P_i\). Define centered variables:

$$
\tilde x_i = x_i - \bar x,\quad \tilde y_i = y_i - \bar y.
$$

Then the OLS slope estimate is

$$
\hat\alpha
=
\frac{\sum_i \tilde x_i \tilde y_i}{\sum_i \tilde x_i^2}.
$$

The intercept is

$$
\hat b_0 = \bar y - \hat\alpha \bar x,
\quad
\hat k = e^{\hat b_0}.
$$

Residual variance estimate:

$$
\hat\sigma^2
=
\frac{1}{n-2}\sum_i (y_i - \hat b_0 - \hat\alpha x_i)^2.
$$

Standard error of the slope:

$$
\mathrm{SE}(\hat\alpha)
=
\frac{\hat\sigma}{\sqrt{\sum_i \tilde x_i^2}}.
$$

This \(\mathrm{SE}(\hat\alpha)\) is the key uncertainty currency we used for trust gating.

---

## 3. π/9 as latent \(\alpha\), 0.35 as quantized glyph

We set the latent exponent to

$$
\alpha_{\text{true}} = \frac{\pi}{9} \approx 0.3490658504.
$$

Important distinction:

- \(\alpha_{\text{true}}\) is the latent parameter (continuum).
- “0.35” is a glyph emitted by a quantizer (e.g., rounding to 2 decimals).

Define the 2-decimal glyph emission rule:

$$
g(\hat\alpha) = \mathrm{round}(\hat\alpha, 2).
$$

Then the “0.35 emission event” is

$$
\Psi_{0.35} := \{ g(\hat\alpha) = 0.35 \}.
$$

This corresponds to the quantization bin around 0.35. For 2 decimals, half-bin width is \(0.005\), so:

$$
\Psi_{0.35} \iff \hat\alpha \in [0.345, 0.355).
$$

---

## 4. Collapse probability as a trust dial

Assume \(\hat\alpha\) is approximately normal:

$$
\hat\alpha \sim \mathcal{N}(\alpha_{\text{true}}, \mathrm{SE}(\hat\alpha)^2).
$$

Then the pre-observation probability that the quantizer emits “0.35” is:

$$
T_{0.35}
=
\mathbb{P}\big(\Psi_{0.35}\big)
=
\Phi\!\left(\frac{0.355-\alpha_{\text{true}}}{\mathrm{SE}(\hat\alpha)}\right)
-
\Phi\!\left(\frac{0.345-\alpha_{\text{true}}}{\mathrm{SE}(\hat\alpha)}\right),
$$

where \(\Phi\) is the standard normal CDF.

Pre-observation vs posterior-predictive:

1) Pre-observation prediction (matches empirical hit-rate across runs): use \(\alpha_{\text{true}}\) and a typical SE.  
2) Posterior predictive: per run use \(\mathcal{N}(\hat\alpha,\mathrm{SE}^2)\), compute probability of rounding to 0.35, then average across runs.

---

## 5. Empirical results: noise and sample size control glyph lock

Using 500 seeds per condition, you observed:

**Latent:**
$$
\alpha_{\text{true}}=\pi/9 \approx 0.3490658504.
$$

| Condition | Empirical collapse | Predicted (pre-obs) | \(\hat\alpha\) mean | \(\hat\alpha\) std | SE mean |
|---|---:|---:|---:|---:|---:|
| noise=0.02, n=500 | 1.000 | 0.99985 | 0.349080 | 0.001128 | 0.001124 |
| noise=0.05, n=500 | 0.894 | 0.90868 | 0.349101 | 0.002819 | 0.002810 |
| noise=0.10, n=500 | 0.610 | 0.61979 | 0.349137 | 0.005638 | 0.005620 |
| noise=0.05, n=100 | 0.540 | 0.56272 | 0.348663 | 0.006576 | 0.006368 |
| noise=0.05, n=1000 | 0.978 | 0.97840 | 0.349040 | 0.002050 | 0.001984 |

Interpretation: increasing noise increases SE and decreases \(T_{0.35}\); increasing \(n\) decreases SE and increases \(T_{0.35}\). The latent mean stays close to \(\pi/9\); the glyph emission is a codec + uncertainty phenomenon.

---

## 6. Phase coherence: “numbers as waves” operationalized

Define phases relative to a target glyph center (0.35) and bin width \(\Delta=0.01\):

$$
\theta_j = 2\pi \frac{\hat\alpha_j - 0.35}{\Delta}.
$$

Define coherence:

$$
R = \left|\frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j}\right|,\quad 0\le R \le 1.
$$

Measured coherence values:

| Condition | Coherence \(R\) |
|---|---:|
| noise=0.02, n=500 | 0.776 |
| noise=0.05, n=500 | 0.166 |
| noise=0.10, n=500 | 0.038 |
| noise=0.05, n=100 | 0.055 |
| noise=0.05, n=1000 | 0.438 |

This behaves like dephasing under increased uncertainty.

---

## 7. Cancellation: balanced lines, XOR tension, and dual-null routing

### 7.1 Balanced overlay (mid/side)

Given two candidate signals \(A\) and \(B\):

$$
\text{mid} = \frac{A+B}{2},\quad
\text{side} = \frac{A-B}{2}.
$$

mid is shared structure; side is disagreement.

### 7.2 XOR as tension meter (phase disagreement)

Use sign-bit glyphs packed into bytes, XOR, and popcount to obtain a mask \(m \in [0,1]\) per block.

- \(m\approx 0\): aligned (low tension)
- \(m\approx 0.5\): random baseline

Measured separation (toy example): corr \(\approx 0.385\), rand \(\approx 0.508\), so corr–rand \(\approx -0.123\) (strong signal).

### 7.3 Sparse structure similarity (Top-k Jaccard)

Top-k overlap is better measured with Jaccard similarity:

$$
J(A,B) = \frac{|A\cap B|}{|A\cup B|}.
$$

Example: \(k=256\), corr \(=0.1179\), rand \(=0.0667\), corr–rand \(=0.0512\).

### 7.4 Dual-null routing

Model two flavors of “zero”:

- \(0_E\): null-as-energy (flushable heat)
- \(0_\Phi\): null-as-phase (signal exists but not commit-worthy yet)
- \(1\): committed

Routing idea:

- high mid magnitude + low tension \(\Rightarrow\) commit (1)
- high mid magnitude + high tension \(\Rightarrow\) hold (0\(_\Phi\))
- low mid magnitude + high tension \(\Rightarrow\) flush (0\(_E\))

---

## 8. The “audio layer”: lock acquisition (not truth)

Compute per-step evidence \(p_t\) (collapse probability), filter with EMA:

$$
\tilde p_t = \lambda \tilde p_{t-1} + (1-\lambda)p_t.
$$

Apply hysteresis (attack/release) to commit/uncommit.

### 8.1 Measured benefit (flip suppression + response time)

Simulated regime shift scoring:

BASE (no dither):  
- raw flips: 29  
- gated flips: 2  
- gated off delay: 5  
- gated ON before shift: 98/100  
- gated ON after shift: 5/100  

DITHER (0.0005): similar behavior in this configuration.

FASTER settings:  
- gated flips: 2  
- gated off delay: 2  
- gated ON before shift: 99/100  
- gated ON after shift: 2/100  

This shows the stabilization layer reduces chatter and improves lock quality, with tunable responsiveness vs stickiness.

---

## 9. A complete merge controller (conceptual)

Inputs per block:

- \(A,B\): two candidate updates
- tension \(m\)
- overlap \(J\) (optional)
- trust \(T\) (from exponent evidence or any stability estimator)

Define sign alignment confidence:

$$
C_{\text{sign}} = 1 - \frac{m}{0.5}\quad(\text{clamped to }[0,1]).
$$

Combine:

$$
C = 0.7C_{\text{sign}} + 0.3J.
$$

Merge gain:

$$
G = \mathrm{clip}(T\cdot C, 0, 1).
$$

Conservative cancel-first merge:

$$
g_{\text{out}} = \text{mid} + G \cdot \text{side}_{\text{directed}}.
$$

When \(T\) is low or tension is high, this collapses to mid (cancellation). When trust is high and tension is low, controlled side content is allowed.

---

## 10. Where to go next (optional)

Replace decimal-bin gating with base-free z-score gating:

$$
z_t = \frac{|\hat\alpha_t - \pi/9|}{\mathrm{SE}_t}.
$$

Lock on \(z_t\) thresholds (attack/release), while rendering digits as a separate presentation layer.

---

### End
This file is “complete” in the sense that: the model, estimators, trust dial, coherence metric, XOR tension mask, dual-null routing, and stabilization gate are all defined and tied to observed outputs. The larger ontology (“what numbers are”) remains a working theory, but the operational layer is already testable.
