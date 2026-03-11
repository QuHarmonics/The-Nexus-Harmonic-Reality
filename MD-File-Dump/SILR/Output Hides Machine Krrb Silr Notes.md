# Output Hides the Machine — KRRB / SILR Closure Notes (Nexus Fold)

This document formalizes the “output hides the machine” claim in the specific context of **KRRB** dynamics and the **SILR** stability hypothesis.  
It is written to be *calibration-first* (skeptic-readable): definitions → invariants → tests → failure modes.

---

## Δ-fold — Interface vs Generator (why “output hides the machine” is structurally normal)

A low-dimensional output can faithfully summarize a high-dimensional generator **without exposing it**, because *compression* is the rule, not the exception:

- A compiled binary hides the compiler IR.
- A hash digest hides the message.
- A thermodynamic macrostate (pressure/temperature) hides the microstate.

So if the Nexus lens is pointed at something real, it should keep rediscovering this asymmetry:

> **Visible interface = low-dimensional projection of a higher-dimensional process.**  
> **Projection is lossy on purpose because that’s what makes it stable.**

That’s the “machine hides behind the output” archetype.

---

## ⊕-resonance — What your KRRB plot is actually saying

From the plot you posted:

- **Magnitude** \(|R(t)|\) rises smoothly on a log scale (near-linear line).
- **Phase** \(\arg(R(t))\) stays pinned near **0 rad**.

This is a strong signature, and it implies two concrete facts.

### 1) Phase pinned ⇒ multiplicative process is effectively real/positive

If \(\arg(R(t)) \approx 0\) for all \(t\), then the update is not “rotating” in the complex plane. You’re multiplying by **positive real scalars** (or complex phases are canceling perfectly).

Operationally:

- Growth/decay can happen.
- **Precession / swirl cannot** (no complex torque).

If you want swirl, you need a complex-valued or signed \(B\) model (details below).

### 2) Straight line on log-magnitude ⇒ constant average log-gain (Lyapunov drift)

If magnitude follows a straight line on a log plot, the system is behaving like:

\[\
R_{t+1} = R_t \cdot G_t,\quad G_t>0
\]

so

\[\
\log |R_{t+1}| = \log|R_t| + \log G_t.
\]

If \(\mathbb{E}[\log G_t] > 0\), you inflate.  
If \(\mathbb{E}[\log G_t] < 0\), you collapse.  
If \(\mathbb{E}[\log G_t] \approx 0\), you can hover in a bounded regime (only if variance is controlled).

This gives a non-poetic closure condition: **SILR is a drift ≈ 0 manifold**.

---

## ↻-reflection — SILR as a stability condition (drift + variance)

Define the per-step log gain:

\[\
g_t \equiv \log G_t
\]

Define the long-run drift (Lyapunov exponent for the multiplicative process):

\[\
\lambda \equiv \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T} g_t.
\]

Then the regimes are:

- \(\lambda > 0\): inflation / divergence  
- \(\lambda < 0\): collapse / evaporation  
- \(\lambda \approx 0\): sustained recursion (the only place SILR can live)

### Mapping to your parameterization

If your update is:

\[\
R_{t+1} = R_t \exp(HF\Delta t)\,\prod_i B_{t,i},
\]

then

\[\
G_t = \exp(HF\Delta t)\,\prod_i B_{t,i}
\]

so

\[\
g_t = HF\Delta t + \sum_i \log B_{t,i},
\]

and therefore

\[\
\lambda = HF\Delta t + \sum_i \mathbb{E}[\log B_{t,i}].
\]

This is the machine-level statement:

> **Stability is a balance of deterministic push** \(HF\Delta t\)  
> **against statistical pull** \(\sum_i \mathbb{E}[\log B_{t,i}]\).

### Variance matters (wobble)

Even if \(\lambda \approx 0\), large variance in \(g_t\) can cause intermittent blowups or extinctions.

Define:

\[\
\sigma^2 \equiv \mathrm{Var}(g_t).
\]

SILR (as an engineering regime) wants:

- Drift near zero: \(\lambda \approx 0\)
- Variance bounded: \(\sigma^2\) “not huge”
- Tail risk controlled (rare extreme \(g_t\))

That’s the *control* view.

---

## ⊥-collapse — “Eddy risk”: when narrative tunes parameters instead of tests

The way to avoid self-made whirlpools is not to suppress intuition—it's to **lock your protocol** before the run.

Here are four brutal filters that separate “real attractor” from “constructed resonance”:

1) **Pre-register predictions**  
   Example:  
   - Using sliding e-digit windows with mapping \(d\mapsto d/9\), \(\lambda<0\).  
   - Using SHA-derived \(B\in[0.9,1.1]\) on Byte1, \(\lambda>0\).  
   Then run blind.

2) **Hold-out data**  
   If \(\pi\) digits were used to tune mapping, use \(e\) digits (or random) as hold-out.

3) **Representation invariance**  
   If a “coherence fraction” is real, it must survive base changes (decimal digits vs bytes vs nibbles), up to predictable transforms.

4) **Sensitivity analysis**  
   Nudge \(H\), window width, digit→\(B\) mapping, and dt.  
   - If the effect only exists on razor-tuned settings: likely artifact.  
   - If it survives a neighborhood of settings: candidate attractor.

This is how you convince skeptics: show the attractor survives hostile conditions.

---

## Ψ-collapse — Making χ rigorous (so it stops doing 7 jobs at once)

Right now “χ” is being asked to mean:
- resonance fraction,
- stability,
- compressibility,
- “flow,”
- and a cosmological ratio.

That’s fine as intuition, but for proof you need a *definition that survives encoding changes*. Two definitions work well and map cleanly to your KRRB machinery.

### χ₁: Stability occupancy (time spent near neutral updates)

Let the “neutral” step be \(g_t=0\). Define:

\[\
\chi_1(\epsilon) \equiv \frac{1}{T}\sum_{t=1}^{T}\mathbf{1}\{|g_t|<\epsilon\}.
\]

Interpretation: **fraction of time near the stability manifold**.  
- High \(\chi_1\): system spends lots of time near SILR.  
- Low \(\chi_1\): system lives in runaway or collapse.

This χ does **not** confuse “tiny final magnitude” with “good coherence.” It measures control.

### χ₂: Compressibility / coherence of the branch stream

Define an empirical Shannon entropy on the branch symbols (digits/nibbles/bytes):

\[\
\chi_2 \equiv 1 - \frac{H_{\text{empirical}}(B)}{H_{\max}}.
\]

Interpretation: **how compressible / structured the branch stream is**.  
This matches your “output hides the machine” intuition: fewer effective degrees of freedom ⇒ stronger interface compression.

---

## Practical read of your posted plot (quick estimate)

From your magnitude plot: log10\(|R|\) increases roughly linearly over 1000 steps. If it rises ~60 decades over 1000 steps, that’s:

\[\
\Delta \log_{10}|R| \approx 60 \quad\Rightarrow\quad \text{per-step } \Delta \log_{10}|R| \approx 0.06
\]

Convert to natural logs (per-step drift estimate):

\[\
\lambda \approx 0.06\ln 10 \approx 0.138.
\]

If you used \(H=\pi/9\approx 0.349\) and \(\Delta t=0.5\) with \(F=1\), then the deterministic push is:

\[\
HF\Delta t \approx 0.349\times 0.5 \approx 0.1745.
\]

So your branches contributed a net negative correction (on average):

\[\
\sum_i \mathbb{E}[\log B_{t,i}] \approx \lambda - HF\Delta t \approx 0.138 - 0.1745 \approx -0.0365.
\]

That’s exactly the “machine hides behind output” point: you can infer the *aggregate branch entropy pressure* without seeing any branch microstructure.

Phase pinned at ~0 rad means the above inference is **purely scalar** (no complex torque).

---

## How to get “90° bend” / swirl (if you want ε-like transverse behavior)

If you want the model to support “bending” and transverse modes, you need **a second degree of freedom** and/or **complex phase**.

Two minimal moves:

### Move A: complex branch factors

Let:

\[\
B_{t,i} = \rho_{t,i}\,e^{i\phi_{t,i}}.
\]

Then:

\[\
g_t = HF\Delta t + \sum_i \log\rho_{t,i} \quad\text{and}\quad \Delta\arg(R)\sim \sum_i \phi_{t,i}.
\]

Now you can have:
- magnitude stability with phase rotation,
- phase-lock vs phase-slip regimes,
- a literal “bend” dynamic.

### Move B: two-field ring (longitudinal + transverse)

Let \(u(x,t)\) be longitudinal and \(v(x,t)\) transverse, coupled at emitters:

\[\
\partial_t^2 u - c^2\partial_x^2 u + \sum_j \gamma\,\delta(x-x_j)\,(u+\eta v)=0
\]

\[\
\partial_t^2 v - c^2\partial_x^2 v + \sum_j \gamma\,\delta(x-x_j)\,(v+\eta u)=0
\]

The coupling \(\eta\) is your “90° bend lever.” In such models, you naturally get mode splitting and **gaps** (which your earlier spectrum work was hinting at).

This is where sparse mass spectra become plausible: gaps arise from coupling + symmetry selection, not from a single scalar field.

---

## Ω-tag (isolate the unresolved attractor)

**Ω:** “χ must equal exactly 0.35 in nature.”  
This is not rejected; it’s simply **not yet well-defined**. χ needs a definition (χ₁ or χ₂ or another) that survives:

- encoding change,
- hold-out datasets,
- parameter perturbations,
- and blind pre-registered predictions.

Once it survives those, 0.35 can be discussed as an emergent fixed point (or not).

---

## Minimal skeptic-proof experiment plan (one page)

1) Choose mapping digits→\(B\) **once** (pre-registered).  
2) Choose datasets: calibration (π) and hold-out (e).  
3) Run KRRB and compute:  
   - \(\lambda\) (drift), \(\sigma^2\) (variance)  
   - χ₁(\(\epsilon\)) (stability occupancy)  
   - χ₂ (compressibility of branch stream)  
4) Repeat with re-encoding: digits → bytes → nibbles.  
5) Report what survives. Survivors are candidates for “invariants.”

That’s your bridge from “shape intuition” to “publishable claim.”

---

## Appendix: tiny reference code (metrics only)

```python
import numpy as np

def metrics_from_G(G, eps=0.05):
    # G: array of positive per-step gains, shape (T,)
    g = np.log(G)
    lam = g.mean()
    sig2 = g.var()
    chi1 = np.mean(np.abs(g) < eps)
    return lam, sig2, chi1

def chi2_from_symbols(symbols, alphabet_size):
    # symbols: array of ints in [0, alphabet_size)
    counts = np.bincount(symbols, minlength=alphabet_size).astype(float)
    p = counts / counts.sum()
    p = p[p>0]
    H_emp = -(p*np.log2(p)).sum()
    H_max = np.log2(alphabet_size)
    return 1 - H_emp/H_max
```

---

### End state

**If the output hides the machine, your job is to infer the machine from invariants.**  
Here, the invariants are not “poetic”: they are \(\lambda\), \(\sigma^2\), χ₁, and χ₂—computed under hostile testing.

