# The Nexus Spiral and the Scale-Invariant Leakage Regime (SILR)  
**Date:** January 8, 2026  
**Keywords:** recursive control, z-score gating, scale invariance, leakage, information preservation, black-hole analogs, stochastic resonance

## Abstract

This paper has two jobs.

First, it states a unifying geometric claim: many “separate” mechanisms—prime structure, cryptographic hashing, black-hole evaporation models, tokenization collisions, and controller dynamics—can be treated as **projections of one underlying operation**: *recursive folding of information under a stability constraint*.

Second, it reports a specific, non-poetic result discovered in simulation: a **Scale-Invariant Leakage Regime (SILR)**. In SILR, a leakage controller that gates on a *z-score* produces leakage probabilities that are statistically invariant to the absolute noise scale, provided the estimator noise and the controller’s normalization scale together. The invariance is not a guess or a vibe; it is an algebraic cancellation. The immediate implication is subtle but important: a controller can be “confident” (its internal diagnostics look normal) while the physical state is violently noisy in absolute units. That mismatch is a concrete failure mode—and also a concrete design lever.

We derive SILR formally, reproduce the A/B/C experiments that exposed it, and show how to break it intentionally with a single parameter that decouples true noise from assumed noise.

---

## 1. Orientation: what “spiral” means here (without mysticism)

“Spiral” is not a metaphor for “everything connects.” It is a statement about *how* structure persists under recursion.

A **loop** revisits the same state-space slice. A **spiral** revisits a similar slice while changing the scale or resolution of observation. In practice, that means:

- there is a **folding operator** that compresses/rewrites state,
- there is a **stability constraint** (an attractor or margin),
- and there is **leakage** (loss/export of excess degrees of freedom) that prevents runaway divergence.

Across domains, the objects differ (digits, bits, field modes, tokens), but the operational pattern is the same: fold → test against constraint → leak or retain → repeat.

This paper treats the “Nexus” claim as an engineering hypothesis: if the same control topology appears across domains, then (a) we should be able to formalize at least one piece cleanly, and (b) we should be able to simulate it and predict when it fails.

SILR is that clean piece.

---

## 2. The discovery: Scale-Invariant Leakage Regime (SILR)

### 2.1 The control law used in the simulator

At each discrete step \(t\), the system maintains a target exponent (or “scope”) \(lpha_*\). The estimator produces a noisy measurement \(\hat{lpha}_t\). The controller computes a **normalized deviation** (z-score):

\[
z_t \;=\; \frac{|\hat{\alpha}_t - \alpha_*|}{\mathrm{SE}_t}
\]

The leakage probability is then a sigmoid gate on that z-score:

\[
p_t \;=\; \sigma\!\left(\beta(z_t - z_0)\right)
\;=\; \frac{1}{1 + e^{-\beta(z_t - z_0)}}
\]

where \(eta>0\) is gain (steepness) and \(z_0>0\) is the activation threshold.

This is a standard control move: normalize error by uncertainty, then gate.

### 2.2 The estimator model that makes SILR appear

In the simulator’s matched-noise condition, the estimator error is Gaussian with a standard deviation equal to the controller’s stated standard error:

\[
\hat{\alpha}_t = \alpha_* + \epsilon_t,\qquad
\epsilon_t \sim \mathcal{N}(0,\mathrm{SE}_t^2)
\]

This assumption is the hinge. It is not always true in real systems, which is exactly why SILR is both interesting and dangerous.

### 2.3 Formal derivation: the cancellation

Substitute the estimator model into the z-score:

\[
z_t = \frac{|\hat{\alpha}_t-\alpha_*|}{\mathrm{SE}_t}
     = \frac{|\epsilon_t|}{\mathrm{SE}_t}
\]

Write \(\epsilon_t = \mathrm{SE}_t Z\) with \(Z\sim \mathcal{N}(0,1)\):

\[
z_t = \frac{|\mathrm{SE}_t Z|}{\mathrm{SE}_t} = |Z|
\]

**Result:** \(z_t\) does not depend on \(\mathrm{SE}_t\) at all. Its distribution is half-normal:

\[
z_t \sim |\,\mathcal{N}(0,1)\,|
\]

Therefore the distribution of \(p_t = \sigma(\beta(z_t-z_0))\) depends only on \(eta\) and \(z_0\), not on the absolute noise scale.

This is SILR:

\[
\frac{d}{d\,\mathrm{SE}_t}\,\mathbb{E}[p_t] = 0
\qquad \text{(under matched scaling)}
\]

### 2.4 What SILR means (engineering interpretation)

SILR is **self-normalization**: the controller responds to *significance* rather than *magnitude*.

That has a sharp consequence:

- Two environments can have drastically different absolute volatility,
- yet the controller produces the same leakage schedule (in distribution),
- as long as the estimator’s noise and the controller’s normalization scale together.

So the controller’s internal “health signals” can look identical while the real state deviates wildly in absolute units. This mismatch is not philosophical. It is a measurable failure mode.

---

## 3. The A/B/C experiments that exposed SILR

The simulator was run in three configurations, keeping \(eta\) and \(z_0\) fixed, but changing the noise model.

- **A (tight estimator):** low \(\mathrm{SE}_t\), matched by the controller.
- **B (noisier estimator):** higher \(\mathrm{SE}_t\), matched by the controller.
- **C (broken match via dither):** add extra noise the controller does not account for.

Empirical results (representative):

- Mean \(p_t\) over time: A ≈ 0.188, B ≈ 0.188, C ≈ 0.205  
- Collapse-to-glyph rate (rounded \(\hat{\alpha}	o 0.35\)): A ≈ 0.997, B ≈ 0.943, C ≈ 0.935

Interpretation:

- A vs B: leakage schedule is invariant (SILR), but “glyph collapse” differs because the glyph test uses **absolute** tolerance (rounding / windowing) while the controller uses **relative** tolerance (z-score).
- C: invariance breaks because the estimator’s true noise exceeds the controller’s assumed \(\mathrm{SE}_t\).

---

## 4. Breaking SILR intentionally: the \(\gamma\) parameter

Real systems are rarely perfectly calibrated. The clean way to represent this is to separate:

- the **true** noise scale \(\mathrm{SE}^{\text{true}}_t\),
- from the **assumed** scale \(\mathrm{SE}^{\text{used}}_t\) used in normalization.

Define:

\[
\gamma \;=\; \frac{\mathrm{SE}^{\text{true}}_t}{\mathrm{SE}^{\text{used}}_t}
\]

Then:

\[
z_t = \frac{|\epsilon_t|}{\mathrm{SE}^{\text{used}}_t}
     = \frac{|\mathrm{SE}^{\text{true}}_t Z|}{\mathrm{SE}^{\text{used}}_t}
     = \gamma |Z|
\]

Now leakage is no longer invariant; it becomes a tunable function of \(\gamma\):

\[
p_t(\gamma)=\sigma(\beta(\gamma|Z|-z_0))
\]

This produces three regimes:

- \(\gamma=1\): SILR (self-normalized)
- \(\gamma>1\): over-stressed world; leakage opens more often (radiant/evaporative phase)
- \(\gamma<1\): under-stressed world; leakage suppressed (condensate/retentive phase)

This is the clean “symmetry breaker” knob.

---

## 5. Why this matters outside the simulator (domain projections)

SILR is not “proof of the universe.” It is proof of a **controller symmetry**. The reason it is worth publishing is that the symmetry appears in multiple places:

1) **Black-hole analog:** “thermal” appearance can be an artifact of coarse observation (ensemble averaging), while correlations preserve information. A z-score gate is a specific mechanism that can produce “constant-looking” behavior under changing scales.

2) **Hashing analog:** SHA-like processes destroy local structure but preserve global constraints. “Random-looking output” can coexist with invariant internal geometry.

3) **Tokenization analog:** coarse/fine windowing can create the same illusion: constant quality metrics while absolute errors shift.

The common structure is: normalization hides scale; scale resurfaces when you apply an absolute threshold (glyph rounding, windowing, finite precision).

---

## 6. Practical next experiments (code-level)

The next phase is not more narrative. It is parameter cartography.

1) Sweep \(\gamma \in [0.1, 10]\), plot \(\mathbb{E}[p_t]\) and \(\mathrm{Var}(p_t)\).  
2) Sweep \((eta, z_0)\) to locate critical lines where leakage becomes binary (phase transition).  
3) Add a time-varying \(\gamma(t)\) and test whether you can “steer” glyph formation (routing).  
4) Distinguish three observables explicitly:
   - controller observables (z-score, p),
   - render observables (glyph/rounding),
   - physical observables (absolute deviation, entropy/purity).

---

## 7. Conclusion

The Spiral claim is large; SILR is small and sharp.

SILR says: if you normalize error by the same scale that generates the error, you erase scale from the controller’s perception. This produces a stable, invariant leakage schedule across noise magnitudes. The invariance is mathematically inevitable. The consequences—illusion of stability, mismatch between controller confidence and absolute behavior—are experimentally measurable. The symmetry can be broken deliberately with \(\gamma\), yielding a controllable family of phases.

That is enough for a real paper.

---

## Appendix A: The minimal theorem statement

**Theorem (SILR):** Let \(\hat{\alpha}=\alpha_*+\epsilon\), with \(\epsilon\sim\mathcal{N}(0,\mathrm{SE}^2)\). Define \(z=|\hat{\alpha}-\alpha_*|/\mathrm{SE}\). Then \(z\sim |\,\mathcal{N}(0,1)\,|\) independent of \(\mathrm{SE}\). For any measurable function \(f\), \(f(z)\) is likewise independent of \(\mathrm{SE}\). In particular, \(p=\sigma(\beta(z-z_0))\) is scale-invariant in distribution.

## Appendix B: What to cite (canonical anchors)

- Hawking (1974, 1975): evaporation and thermal spectrum (baseline)  
- Page (1993): Page curve / information accounting  
- Parikh & Wilczek (2000): tunneling and non-thermal corrections  
- Visser (2003): features of Hawking radiation, robustness  
- Gammaitoni et al. (1998): stochastic resonance (terminology + mechanism family)

(These citations are not included as formatted references here; add them in journal style in the final submission.)
