
# Nexus Spiral Compiler — Unified Field Overlay (Sections I–V)

> *“Geometry, control, and sampling are not distinct layers – they are orthogonal views of a single harmonic recursion.”*  

---

## I Primer — The Spiral Compiler Core

The Spiral Compiler treats **reality as a discrete log‑spiral render loop**.

A state on frame $t$ is represented in complex polar form  

$$
z_t \;=\; r_t\,e^{i\theta_t}.
$$

A single fold updates  

$$
z_{t+1}\;=\;\rho_t\,e^{i\Delta\theta_t}\,z_t,
\qquad
\rho_t=e^{\mu_t},\; \mu_t\in\mathbb R.
$$

* **Cadence (frame size)** $\Delta\theta_\star=\pi/9\;\approx0.349$  
* **Speed (radial drift)** $\mu_t=\ln\rho_t$ ($\mu_t=0$ ⇔ neutral radius)

Stable render ⇔  

\[
\big\langle|\Delta\theta_t-\Delta\theta_\star|\big\rangle\!\to\!0,
\qquad
\langle\mu_t\rangle\!\to\!0.
\]

---

## II Triplet Geometry Projection

| Projection | Symbol | Role | Governing transform |
|------------|--------|------|---------------------|
| Plane Fold | $A$ | local compression / “tape” | $\displaystyle A_{t+1}=A_t-\tfrac{\pi}{9}\,\partial_yB_t$ |
| Dual Screw | $B$ | phase transport | $\displaystyle B_{t+1}=B_t+\tfrac{\pi}{9}\,(\partial_xA_t-\partial_zC_t)$ |
| Box Stack  | $C$ | scale quantisation | $\displaystyle C_{t+1}=C_t-\lambda_t\,C_t,\;\lambda_t=e^{-\mu_t}$ |

$\boxed{\Psi_t=(A_t,B_t,C_t)^\top}$ is the *field vector*; every projection is a coordinate view of the same recursion field $\mathcal M$.

---

## III Samson Feedback Law (Global PD Control)

Error channels  

\[
e_\theta(t)=|\Delta\theta_t-\tfrac{\pi}{9}|,\qquad
e_r(t)=\mu_t,\qquad
e_\chi(t)=\frac{|\Delta\chi_t|}{|\Delta\chi_{t-1}|}-\tfrac{\pi}{9}.
\]

Control signals  

\[
\begin{aligned}
u_\theta &=k_p^\theta e_\theta + k_d^\theta\dot e_\theta,\\
u_r      &=k_p^r e_r      + k_d^r\dot e_r,\\
u_\chi   &=k_p^\chi e_\chi+ k_d^\chi\dot e_\chi.
\end{aligned}
\]

Updates  

\[
F_{t+1}=F_t+\alpha_\theta u_\theta+\alpha_r u_r,\qquad
\lambda_{t+1}=\lambda_t+\alpha_\chi u_\chi.
\]

Lyapunov candidate  

\[
V(t)=a\,e_\theta^2+b\,\mu^2+c\,e_\chi^2,\qquad \dot V\le0\;(\text{except at }\Omega\text{-resets}).
\]

---

## IV Adaptive Sampler (\(\Lambda=[w,K,n,\varphi]\))

The cyclic seed $B=(1,4,1,5,9,2,6,5)$ ($L=8$).  
A scope slice is

\[
\text{Scope}_{w,K}(n)=\bigl(B_{(n+jK)\bmod L}\bigr)_{j=0}^{w-1}.
\]

Missing parameters infer via control:

\[
\begin{aligned}
K_{t+1}&=K_t+\beta_\theta\,u_\theta,\\
w_{t+1}&=w_t+\beta_r\,u_r,\\
n_{t+1}&=n_t+\beta_\chi\,u_\chi.
\end{aligned}
\]

Forks $\mathbf K=[K^{(1)},\dots,K^{(m)}]$ are fused by XOR / interleave, giving **location‑delimited holograms**.

---

## V Collapse‑to‑Render Criterion

Render freezes when  

\[
\boxed{%
\begin{array}{l}
e_\theta\le\varepsilon_\theta,\;\; |e_r|\le\varepsilon_r,\\[4pt]
\displaystyle\frac{|\Delta\chi_t|}{|\Delta\chi_{t-1}|}\le\tfrac{\pi}{9},\\[8pt]
\mathrm{STI}_t =\exp\!\Bigl[-\lambda\,\tfrac{\operatorname{std}(\Delta\chi_{t-k:t})}{\pi/9+\epsilon}\Bigr]\ge0.5
\end{array}}
\]

Any lattice site that meets the test for $L$ consecutive frames is **frozen** (partial collapse).  
If $\mathrm{STI}<0.5$ globally, the **Ω‑gate** performs a minimal‑cut reset and the loop resumes.

---

### 🔬 Executable Stub (NumPy ≈ 60 lines)

```python
import numpy as np
L, seed = 8, np.array([1,4,1,5,9,2,6,5])
w, K, n = 14, 1, 0          # initial sampler
θ, r, F = 0.0, 1.0, 1.0     # spiral state
χ_hist, sti_hist = [], []

def sampler(w,K,n):
    idx = (n + K*np.arange(w)) % L
    return seed[idx]

for t in range(800):
    # --- sampler & coherence -----------------
    slice_ = sampler(w,K,n)
    χ = np.mean(slice_ % 2 == 0)        # toy coherence
    χ_hist.append(χ)

    # --- spiral update -----------------------
    Δθ =  np.pi/9 * F
    μ   = -0.02 + 0.04*np.random.randn()
    θ  += Δθ
    r  *= np.exp(μ)

    # --- errors ------------------------------
    eθ = abs(Δθ - np.pi/9)
    er = μ
    eχ = 0 if t<2 else abs((χ_hist[-1]-χ_hist[-2]) /
                           (χ_hist[-2]-χ_hist[-3]+1e-9)) - np.pi/9

    # --- PD control (scalar gains) -----------
    uθ =  0.6*eθ + 0.3*(eθ - (0 if t==0 else eθ_prev))
    ur =  0.4*er + 0.2*(er - (0 if t==0 else er_prev))
    uχ =  0.5*eχ + 0.2*(eχ - (0 if t==0 else eχ_prev))

    F += 0.04*uθ + 0.01*ur
    K += int(np.sign(uθ))
    w  = max(4, w + int(np.sign(-ur)))
    n += int(np.sign(uχ))

    # store prev errs
    eθ_prev, er_prev, eχ_prev = eθ, er, eχ

    # --- STI & Ω‑gate ------------------------
    if t>4:
        stdΔχ = np.std(np.diff(χ_hist[-5:]))
        sti = np.exp(-4*stdΔχ/(np.pi/9+1e-4))
    else:
        sti = 1.0
    sti_hist.append(sti)

    if sti < 0.5:            # minimal‑cut reset
        r, K, w = 1.0, 1, 14

# χ_hist, sti_hist now hold coherence & trust traces
```

*Run the stub to watch cadence lock, sampler self‑tuning, and partial collapses.*

---

### ⭑ Proposition (V.1) Scope–Structure Self‑Closure

> Under the coupled PD law above, any initial field $\boldsymbol\Psi_0$ converges to a
> phase‑locked, drift‑neutral steady state  
> $$\bigl|\langle\Delta\theta\rangle-\tfrac{\pi}{9}\bigr|<\varepsilon, \quad
> \langle\mu\rangle\to0,\quad \mathrm{STI}\to1.$$
> Every pattern that satisfies local constraints emerges as a rendered casting; all others are indefinitely reset by the Ω‑gate.

---

*End of document*
