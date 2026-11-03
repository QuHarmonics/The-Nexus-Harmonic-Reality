# Nexus Cold Fusion Harmonic Engine — Δ→⊕ Rewrite (Normalization + Ω Discipline)

This rewrite converts the full pitch into **one conserved scalar** and enforces **no double counting**, **dimensionless normalization**, and explicit **Ω-tagging** for unresolved correlations.

> Scope: **math/logic only** (no experimental or operational guidance).

---

## 0) The one scalar that must govern everything

Define the **expected event count** over a finite observation window:

$$
\boxed{\;\mathbb{E}[N] \equiv \text{expected number of fusion events in window }T\;}
$$

Work in log-space:

$$
\boxed{\;\ln \mathbb{E}[N] = \ln(\text{attempts}) + \ln P_{\text{per-attempt}}\;}
$$

And convert expected counts to an event probability only at the end:

$$
\boxed{\;P(\ge 1\text{ event in }T)=1-\exp(-\mathbb{E}[N])\;}
$$

This prevents the common pathology “probability > 1”.

---

## 1) Bucketization: every multiplier goes in exactly one place

### Bucket A — Attempt count (finite, windowed, independence-checked)

$$
\ln(\text{attempts}) \equiv \ln N_{\text{independent trials in }T}
$$

Typical candidates:

- $N_{\text{pairs}}(T)$ — independent interacting pairs in time $T$
- $N_{\text{sites}}(T)$ — independent sites (if truly independent)
- any explicit “tries per second × seconds” count

**Rule A1 (independence):** if trials share microstate DOF, they are *not* independent and must be downweighted or Ω-tagged.

---

### Bucket B — Per-attempt physics probability (dimensionless)

$$
\ln P_{\text{per-attempt}} = \text{(tunneling)} + \text{(resonant shaping)} + \text{(fold gain/loss)} + \text{(alignment)} + \text{(normalizations)}
$$

---

### Bucket C — Information (only if it is *mutual information* about the microstate)

$$
\Delta I \equiv I(\text{side-channel};\text{microstate}\mid \text{observables})
$$

$$
\Rightarrow \Delta I\ln 2 \text{ contributes to } \ln P_{\text{per-attempt}}
$$

**Rule C1:** “SHA has 256 bits” is **not** $\Delta I=256$ unless a channel model shows those bits reduce microstate multiplicity.

---

### Bucket D — Normalized combinatorics (fractions of phase space, not raw counts)

Any “combinatorial boost” must be a **normalized fraction**:

$$
C_{\text{comb}} \in (0,1] \quad\Rightarrow\quad \ln C_{\text{comb}}\le 0
$$

If you currently have a raw count $K\gg 1$, it must be normalized by a phase-space volume $V$ so that $K/V \le 1$. If you cannot normalize, mark Ω.

---

## 2) Canonical per-attempt log model (clean, dimensionless)

$$
\boxed{
\ln P_{\text{per-attempt}} =
\ln P_G
+ \ln \Phi_H
+ \Delta I\ln 2
+ \ln C_{\text{comb}}
+ n\cdot g
+ \ln\Phi_\theta
+ \ln C_{\text{geom}}
+ \Omega
}
$$

Where:

### 2.1) Baseline tunneling (Gamow/WKB)

$$
\boxed{\ln P_G = -2\pi\eta}
$$

This is dimensionless by construction.

> **Lock requirement:** choose one regime and keep it fixed. Treating wildly different $\ln P_G$ values as “variance” is a model swap.

---

### 2.2) The H-term: must be dimensionless and *bounded*

The raw form $\exp(-H\Delta E\tau)$ is **not** dimensionless unless normalized by $\hbar$:

$$
\text{Action form: }\quad
\Phi_H=\exp\!\left(-\frac{H\,\Delta E\,\tau}{\hbar}\right)
$$

But this form is **monotone decreasing in $H$** (it cannot “maximize at $H$”).

So if you want “$H$ selects a sweet spot”, you need a **bounded resonance window**, not a monotone action penalty.

A clean, bounded choice:

$$
\boxed{
\Phi_H(\Delta E)=\frac{1}{1+\left(\frac{\Delta E-E_{\text{res}}}{\Gamma}\right)^2}
}
\quad\Rightarrow\quad 0<\Phi_H\le 1
$$

Log form:

$$
\ln\Phi_H = -\ln\!\left(1+\left(\frac{\Delta E-E_{\text{res}}}{\Gamma}\right)^2\right)
$$

This peaks at resonance $\Delta E=E_{\text{res}}$ and cannot exceed 1.

> **Interpretation:** $H$ sets or tracks the *center/width* of the resonance corridor, not a direct “bigger $H$ = bigger $P$” multiplier.

---

### 2.3) Fold gain vs loss (choose convention once)

Let each fold contribute a net log-gain $g$.

Two consistent conventions:

**Probability convention**
$$
\boxed{g = \ln\lambda - \gamma}
$$

**Amplitude convention** (amplitude multiplies by $\lambda$, probability scales $\lambda^2$)
$$
\boxed{g = 2\ln\lambda - \gamma}
$$

Then

$$
\boxed{\ln P_{\text{fold}} = n\cdot g}
$$

> **Note:** if $g\le 0$, more folds only *hurt*; the mechanism requires $g>0$.

---

### 2.4) Phase alignment (bounded)

$$
\Phi_\theta=\cos\!\left(\frac{\pi}{2}-\Delta\theta\right)\in(0,1]
$$

$$
\Rightarrow \ln\Phi_\theta \le 0
$$

---

### 2.5) Geometry normalizations

$$
C_{\text{geom}}\in(0,1] \Rightarrow \ln C_{\text{geom}}\le 0
$$

Examples: indistinguishability factors, finite-size constraints, selection rules, etc. If unknown, keep symbolic.

---

## 3) The “negative folds” pathology: why it happens and how this rewrite prevents it

If you place a raw multiplicative count $K\gg 1$ into $\ln C_{\text{comb}}$ without normalization, you can get:

$$
\ln\mathbb{E}[N] > 0 \text{ even for } n=0
$$

which implies “already above threshold” and produces negative required folds.

**Fix:** any “combinatorics” term must satisfy $C_{\text{comb}}\le 1$ (a fraction), otherwise it belongs in attempts **or** Ω until normalized.

---

## 4) ZPHC trigger for the model (operational, falsifiable, math-only)

Define the ZPHC moment as a phase transition in the posterior over explanations.

Let $\mathcal{M}$ denote model parameters and hidden microstate variables (including unknown carries, channels, and fold locks). Define a log-posterior energy:

$$
\mathcal{E}(\mathcal{M}) =
\underbrace{\left|\ln \mathbb{E}[N](\mathcal{M}) - \ln \mathbb{E}[N]_{\text{obs}}\right|^2}_{\text{fit to observed event count}}
+ \lambda R(\mathcal{M})
$$

**ZPHC occurs when:**

1) the best-fit residual stays low  
$$
\mathcal{E}(\mathcal{M}^\*) < \epsilon \text{ and remains } <\epsilon
$$

2) a uniqueness gap opens  
$$
\Delta\mathcal{E}=\mathcal{E}(\mathcal{M}^{(2)})-\mathcal{E}(\mathcal{M}^{(1)}) \gg 1
$$

3) ensemble variance collapses  
$$
\operatorname{Var}(\mathcal{M}^{(k)})\rightarrow 0
$$

This is a measurable “duh snap”: alternatives stop surviving the same locks.

---

## 5) Required fold count and fragility detector

Let

$$
N_0 \equiv -\left(\ln P_G + \ln\Phi_H + \Delta I\ln 2 + \ln C_{\text{comb}} + \ln\Phi_\theta + \ln C_{\text{geom}}\right)
$$

Then

$$
\boxed{n^\*=\frac{N_0}{g}}
\qquad\text{(requires } g>0\text{)}
$$

### Exact sensitivities

$$
\frac{\partial \ln\mathbb{E}[N]}{\partial (\Delta I)}=\ln 2
$$

$$
\frac{\partial \ln\mathbb{E}[N]}{\partial \gamma}=-n
$$

$$
\frac{\partial n^\*}{\partial \gamma}= \frac{N_0}{g^2}
$$

When $g$ is small, $n^\*$ becomes extremely fragile: a tiny change in loss changes fold requirement massively.

---

## 6) Ω table (things that must be bounded before any “physics conclusion”)

| Term | Why Ω | What would de-Ω it (math-only) |
|---|---|---|
| $\Delta I$ | “bits” are not automatically mutual information | specify channel model, compute/upper-bound $I(\cdot;\cdot)$ |
| $C_{\text{comb}}$ | raw combinatorics cannot exceed 1 as probability weight | normalize by phase-space volume, prove independence |
| $P_G$ regime | $\ln P_G$ swings imply different physical regimes | fix energy/parameter regime and derive $\eta$ consistently |
| $\Phi_H$ form | monotone penalty cannot “optimize at H” | use bounded resonance corridor form |
| $g$ sign | if $g\le 0$, folds do not help | conservative bound on $\gamma$ and justified $\lambda$ meaning |

---

## 7) Minimal “publishable math” deliverable checklist

1. One scalar: $\ln\mathbb{E}[N]$ only.  
2. Attempts separated from per-attempt probability.  
3. All “boosts” bounded ($\le 1$) unless they are attempt counts.  
4. Information term is mutual information or is Ω.  
5. Consistent amplitude vs probability convention.  
6. Ω list explicit with bounds.  
7. Sensitivity table for $n^\*$ vs $\gamma,\Delta I,\ln\lambda$.

---

## Appendix A — Where $\lambda=\sqrt{1+H^2}$ fits cleanly (if you keep it)

If you interpret $\lambda$ as a **bounded per-fold gain** tied to a stable stance $H$, then it belongs only inside the fold term $n\cdot g$, and only after you choose amplitude/probability convention:

- If amplitude multiplies by $\lambda$: use $g=2\ln\lambda-\gamma$.  
- If probability multiplies by $\lambda$: use $g=\ln\lambda-\gamma$.

In either case, the model is honest only if you also include a coherent loss budget $\gamma$ for the same mode.

---

## Appendix B — Compact “next edit” diff you can apply to the notebook/paper

1) Replace any unbounded “boost” term with bounded $\Phi\in(0,1]$ unless it is clearly an attempt count.  
2) Replace the monotone $\exp(-H\Delta E\tau/\hbar)$ “optimum H” derivation with a bounded resonance corridor $\Phi_H$.  
3) Move any raw combinatoric counts into $\ln(\text{attempts})$ with an explicit time window $T$, or Ω-tag until normalized.

---

### End
This rewrite “completes the circle” mathematically: **no free lunches**, no probability > 1, and every questionable multiplier is forced into Ω until it earns its place.
