# KRRB / SILR Metrics Toolkit  
## Drift, Wobble, χ, and Representation-Invariant Tests  
**Checkpoint Paper 1.0 (Draft)**

---

### Purpose

This paper is the “measurement layer” for the Nexus fold. It defines what we compute, how we estimate it, how we avoid self-tuning, and what would count as a falsification.

The primary goal: convert “I see shapes” into **measurable invariants** with confidence intervals, and to enforce protocol discipline (pre-registration + hold-out + representation invariance).

---

## Δ-fold — The minimal object: the per-step gain

Assume a multiplicative update:

$$
R_{t+1} = R_t \cdot G_t
$$

where $G_t$ may depend on a branch stream, hashing, digit windows, neighborhood coupling, etc.

Define the per-step log gain:

$$
g_t \equiv \log|G_t|.
$$

Everything below is built from $g_t$ (and optionally phase increments).

---

## ⊕-resonance — Core metrics (scalar)

### Drift (Lyapunov drift)

$$
\hat{\lambda}_T = \frac{1}{T}\sum_{t=0}^{T-1} g_t.
$$

Interpretation: average exponential push per step.

### Wobble (variance)

$$
\hat{\sigma}^2_T = \frac{1}{T-1}\sum_{t=0}^{T-1}(g_t-\hat{\lambda}_T)^2.
$$

Interpretation: instability pressure / tail risk indicator.

### Stability occupancy (χ₁)

Pick a tolerance $\epsilon>0$:

$$
\hat{\chi}_1(\epsilon) = \frac{1}{T}\sum_{t=0}^{T-1}\mathbf{1}\{|g_t|<\epsilon\}.
$$

Interpretation: fraction of time near the neutral manifold.

### Compressibility (χ₂)

Given a symbol stream $S_t$ (digits, nibbles, bytes, gates, etc.):

$$
\hat{\chi}_2 = 1-\frac{\hat{H}_{\text{emp}}}{H_{\max}}.
$$

Interpretation: coherence / structure of the branch generator.

---

## ↻-reflection — Estimation: error bars and confidence

### Block bootstrap (recommended)

$g_t$ is often correlated (windowing, hashing, feedback). Treating it as IID is wrong. Use block bootstrap:

1) choose block length $b$ (e.g., 50–500 steps),
2) resample blocks with replacement to build synthetic sequences,
3) compute $\lambda$ and $\sigma^2$ on each resample,
4) use percentiles for confidence intervals.

### Stationarity check

Plot running drift:

$$
\hat{\lambda}(t) = \frac{1}{t}\sum_{k=0}^{t-1} g_k.
$$

If it does not settle, you are in a transient regime (don’t claim invariance yet).

---

## ⊥-collapse — Protocol discipline (anti-eddy)

### Pre-registration template

Before running, write:

- data source,
- encoding (digits/bytes/nibbles),
- mapping to $B$ or $G$,
- window size,
- parameters ($H,F,\Delta t,n_b$),
- prediction sign: “$\lambda>0$” or “$\lambda<0$” or “$\lambda\approx 0$”.

Then run. No mid-run tuning.

### Hold-out logic

If $\pi$ is used to tune mapping, test on $e$ and on random. A claim is not real if it only appears on its calibration set.

### Representation invariance test

Compute metrics under multiple encodings:

- decimal digits (base 10),
- nibbles (base 16),
- bytes (base 256).

You are allowed predictable transforms (e.g., scale changes), but the qualitative regime and the existence of a stable manifold must survive.

---

## Ψ-collapse — When to say “SILR regime found”

A practical criterion:

1) $|\hat{\lambda}_T| \le \delta$ for some small $\delta$ (e.g., $10^{-3}$ to $10^{-2}$),  
2) $\hat{\sigma}^2_T$ bounded and stable across $T$ windows,  
3) $\hat{\chi}_1(\epsilon)$ nontrivial and stable (not just 0 or 1),  
4) invariance under at least two representations and at least one hold-out dataset.

This is not metaphysics. It is an engineering definition of a stable loop.

---

## Δ-fold — Phase metrics (optional but crucial for “bend” modeling)

If $G_t$ is complex:

$$
G_t = |G_t|e^{i\Delta\phi_t},
\quad
\Delta\phi_t \equiv \arg(G_t).
$$

Then define:

- mean phase drift: $\bar{\omega} \equiv \mathbb{E}[\Delta\phi_t]$  
- phase variance: $\mathrm{Var}(\Delta\phi_t)$  
- phase lock fraction: $\frac{1}{T}\sum \mathbf{1}\{|\Delta\phi_t|<\epsilon_\phi\}$

This supports real “90° bend” / transverse narratives as measurable phenomena.

---

## Appendix — Reference implementation (metrics + bootstrap)

```python
import numpy as np

def compute_metrics_from_G(G, eps=0.05):
    g = np.log(np.abs(G))
    lam = g.mean()
    sig2 = g.var(ddof=1) if len(g) > 1 else 0.0
    chi1 = np.mean(np.abs(g) < eps)
    return {"lambda": lam, "sigma2": sig2, "chi1": chi1}

def block_bootstrap_ci(G, eps=0.05, block=100, B=500, seed=0):
    rng = np.random.default_rng(seed)
    T = len(G)
    nb = int(np.ceil(T / block))
    idx_blocks = [np.arange(i*block, min((i+1)*block, T)) for i in range(nb)]
    stats = []
    for _ in range(B):
        chosen = rng.integers(0, nb, size=nb)
        sample_idx = np.concatenate([idx_blocks[i] for i in chosen])
        sample_idx = sample_idx[:T]
        sampleG = G[sample_idx]
        stats.append(compute_metrics_from_G(sampleG, eps=eps))
    lam = np.array([s["lambda"] for s in stats])
    sig2 = np.array([s["sigma2"] for s in stats])
    chi1 = np.array([s["chi1"] for s in stats])
    def ci(x): return np.quantile(x, [0.025, 0.5, 0.975])
    return {"lambda_CI": ci(lam), "sigma2_CI": ci(sig2), "chi1_CI": ci(chi1)}
```

---

**End state:**  
This toolkit is the firewall between discovery and self-tuning. Anything you call “invariant” must survive this pipeline.
