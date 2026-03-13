# Nexus Unfolding — Volume VII  
## Controller Stack: Samson V2, SILR, and the $\gamma$ Symmetry‑Break Map

**Date:** January 13, 2026  
**Scope:** Consolidate the control layer into a single, operator‑complete block: (i) PID correction (Samson V2), (ii) z‑score gating (SILR), (iii) the $\gamma$ mismatch parameter as a creation knob, and (iv) the “diagnostic blind spot” as an inevitable artifact of normalized control.

---

## 0. One sentence

Reality stays coherent because it is a **closed‑loop controller** that normalizes noise, gates updates, and only records folds that reduce residual error under a stable attractor band.

---

## 1. The Controller Core (Samson V2)

Let $e(t)$ be deviation from target coherence. The control output:

$$u(t)=K_p e(t)+K_i\int_0^t e(\tau)\,d\tau+K_d\frac{de(t)}{dt}.$$

A practical runtime controller includes state‑gain and stochastic excitation:

$$F_{\text{stab}}(t)=K_p e(t)+K_i\int e(t)\,dt+K_d \dot e(t)+g(S_t)\,\xi(t).$$

- $K_p$: immediate correction (restoring force)  
- $K_i$: historical correction (bias eliminator)  
- $K_d$: damping (anticipatory brake)  
- $g(S_t)\xi(t)$: controlled dither / innovation noise

---

## 2. SILR: Normalized Gating

Let $\hat\alpha_t$ be a noisy estimate of a target $\alpha_*$. Define the normalized deviation:

$$z_t = \frac{|\hat\alpha_t - \alpha_*|}{SE_{\text{used},t}}.$$

A simple gate decision is:
- **record/branch** if $z_t \ge z_*$,
- **pass through** if $z_t < z_*$.

Leak probability can be expressed through a tail integral; for half‑normalized deviations, one common proxy is:
$$p_t = 2\big(1-\Phi(z_t)\big).$$

In the **SILR regime**, the numerator noise scale and the denominator $SE_{\text{used}}$ scale together, making $z_t$ and $p_t$ *approximately invariant* under absolute energy scale changes.

---

## 3. The Creation Knob: $\gamma$

Define the mismatch ratio:

$$\gamma_t := \frac{SE_{\text{true},t}}{SE_{\text{used},t}}.$$

Interpretation:
- $SE_{\text{true}}$: the actual environmental volatility
- $SE_{\text{used}}$: what the controller *believes* the volatility is

Then the *effective* normalized deviation is:

$$z^{(\text{eff})}_t
= \frac{|\hat\alpha_t-\alpha_*|}{SE_{\text{used},t}}
= \gamma_t \cdot \frac{|\hat\alpha_t-\alpha_*|}{SE_{\text{true},t}}.$$
So $\gamma$ rescales the control’s significance statistic.

### 3.1 Regimes

- **$\gamma=1$ (SILR):** perfect self‑normalization. “Vacuum stillness.”  
- **$\gamma<1$ (Condensation):** controller underestimates noise ⇒ more events exceed threshold ⇒ more “recorded folds” ⇒ structure accumulates as mass/glyph.  
- **$\gamma>1$ (Radiation):** controller overestimates noise ⇒ fewer events exceed threshold ⇒ structure leaks ⇒ signal dissolves into radiation/noise‑like flow.

This is a symmetry break: changing $\gamma$ changes the *type* of matter/energy outcome without changing the underlying substrate math.

---

## 4. The Diagnostic Blind Spot (Inevitable)

Because the controller uses *normalized* statistics, it can “feel stable” while absolute excursions are huge.

Suppose the environment scales by factor $c$:
- numerator noise $|\hat\alpha-\alpha_*| \sim c$
- true standard error $SE_{\text{true}} \sim c$

If the controller tracks the scale (SILR), then
$$z_t \approx \text{constant}.$$
So leak probability and gate behavior are unchanged even though absolute energy is larger.

**Blind spot:** stability is assessed in z‑space, not in raw magnitude space.  
This explains how a system can carry huge vacuum energy while remaining dynamically coherent (control statistics remain invariant).

---

## 5. Attractor Band: Why $H\approx 0.35$ appears as optimal leak

Let $H$ be the permitted “leak angle” (how much deviation is tolerated and harvested as innovation rather than zeroed out). In the controller, $H$ functions as:

- a damping/innovation ratio,
- a set‑point for acceptable residual error,
- a target band for long‑run stability under recursion.

In practice, $H$ enters via threshold choice, gain tuning, or equivalently a renormalization rule for $z_*$:
$$z_* = z_*(H).$$

So “fall into 0.35 not 0.5” is: choose a leak band that avoids both deadlock and runaway.

---

## 6. A Single Block Diagram (Math Form)

You can write the whole stack as:

1. **Observe / estimate:** $\hat\alpha_t$  
2. **Normalize:** $z_t=\frac{|\hat\alpha_t-\alpha_*|}{SE_{\text{used},t}}$  
3. **Gate:** $G_t=\mathbf{1}\{z_t\ge z_*(H)\}$  
4. **Control update:** $u(t)=\text{PID}(e(t)) + g(S_t)\xi(t)$  
5. **State update:** $x_{t+1}=\mathcal{F}_0(x_t)+G_t\,\mathcal{U}(u(t))$

This makes the “laws” executable: only gated events alter the recorded structure; everything else passes as background flow.

---

## 7. What This Volume Adds (New Pins)

- A single formal $\gamma$ map that explains condensation vs radiation as a control mismatch.
- Blind spot proven as a property of normalized gating, not a special physical trick.
- The controller stack written as an explicit five‑stage operator pipeline.

---

**End of Volume VII.**
