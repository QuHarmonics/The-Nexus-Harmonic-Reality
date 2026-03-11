# KRRB with Complex Phase & Two-Field Coupling

**Checkpoint 7.0 (2026-01-16)**

## Δ-fold — Why we need a “bend channel” to get spring gaps

In the scalar KRRB form,

$$R_{t+1} = R_t\,G_t,\quad G_t>0,$$

you can measure drift (inflate/collapse) but you cannot generate genuine **bending** or **gap physics**. A real gravitational interface needs at least one transverse degree of freedom because “falling” is not just scaling; it’s *directional update under constraint*.

So this checkpoint adds the minimum extra structure to produce:

1. **phase precession** (rotation in state space),
2. **mode splitting** (two eigenchannels), and
3. **spring gaps / band gaps** (discrete allowed modes separated by forbidden regions).

This is the bridge between:

- KRRB as a **wobble spectroscope** (Checkpoint 6.0), and
- the SILR-pinned ring dispersion work (your $N$-emitter circle model),
- plus “gravity” as the coarse interface that hides the micro-machine.

---

## ⊕-resonance — Upgrade 1: complex branch factors

Let each branch factor carry magnitude and phase:

$$B_{t,i} = \rho_{t,i}\,e^{i\phi_{t,i}},\quad \rho_{t,i}>0.$$

Your update becomes:

$$R_{t+1} = R_t\,\exp(HF\Delta t)\,\prod_i \rho_{t,i}\,\exp\Big(i\sum_i \phi_{t,i}\Big).$$

Define:

$$g_t \equiv \log|G_t| = HF\Delta t + \sum_i \log\rho_{t,i},$$

$$\Delta\theta_t \equiv \arg(R_{t+1})-\arg(R_t) = \sum_i \phi_{t,i}\pmod{2\pi}.$$

Now you have **two coupled observables** per step:

- radial update $g_t$ (inflate/collapse),
- angular update $\Delta\theta_t$ (bend / steering / precession).

This immediately gives you a cleaner notion of “wobble”:

- **amplitude wobble**: fluctuations of $g_t$,
- **phase wobble**: fluctuations of $\Delta\theta_t$,
- **coupled wobble**: correlation between the two.

A skeptic-friendly statistic is the complex Lyapunov drift:

$$\Lambda \equiv \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^T \log\big(\exp(HF\Delta t)\prod_i B_{t,i}\big) = \lambda + i\omega,$$

where

$$\lambda = \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^T g_t,\qquad \omega = \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^T \Delta\theta_t.$$

Interpretation:

- $\lambda$ is growth/decay (SILR wants $\lambda\approx0$),
- $\omega$ is mean precession rate (the “bend bias”).

---

## ↻-reflection — Upgrade 2: two-field (2-channel) KRRB

To get **spring gaps**, it’s often easier to treat the state as a 2-vector:

$$\mathbf{R}_t = \begin{bmatrix}R_t^{\parallel}\\R_t^{\perp}\end{bmatrix}.$$

A minimal linear update is a 2×2 matrix per step:

$$\mathbf{R}_{t+1} = \mathbf{M}_t\,\mathbf{R}_t.$$

A convenient parameterization that matches your “90° bend” language is:

$$\mathbf{M}_t = \exp(HF\Delta t)\,\mathbf{S}(\eta_t)\,\mathbf{D}_t,$$

where

- $\mathbf{D}_t$ is a diagonal “branch gain” operator,

$$\mathbf{D}_t = \begin{bmatrix} \prod_i B_{t,i}^{(1)} & 0\\ 0 & \prod_i B_{t,i}^{(2)}\end{bmatrix},$$

- and $\mathbf{S}(\eta)$ is a shear/rotation that mixes channels,

$$\mathbf{S}(\eta) = \begin{bmatrix}1 & \eta\\-\eta & 1\end{bmatrix}.$$

Here $\eta$ is the **bend coupling**. If $\eta=0$, the channels never talk. If $\eta\neq0$, energy “leaks sideways,” which is the algebraic analog of transverse displacement.

### Stability and “gap” condition (spectral radius)

Define the spectral radius $\rho(\mathbf{M})$ (largest magnitude eigenvalue).

- Inflation: $\rho(\mathbf{M})>1$.
- Collapse: $\rho(\mathbf{M})<1$.
- Sustained recursion (SILR-like): $\rho(\mathbf{M})\approx1$ with controlled variance.

Because $\mathbf{M}_t$ is 2×2, eigenvalues exist in closed form. For a single-step constant matrix $\mathbf{M}$:

$$\mu_{\pm} = \frac{\operatorname{tr}(\mathbf{M}) \pm \sqrt{\operatorname{tr}(\mathbf{M})^2-4\det(\mathbf{M})}}{2}.$$

If the discriminant is negative, eigenvalues are complex conjugates and you get oscillatory behavior (true bend/rotation):

$$\operatorname{tr}(\mathbf{M})^2 < 4\det(\mathbf{M}).$$

That inequality is a clean “bend exists” gate.

---

## ⊥-collapse — Where spring gaps come from

“Spring gaps” are what you get when an oscillator is periodically pinned or periodically forced. The key is **periodicity** in the update operator.

Assume $\mathbf{M}_t$ repeats every $N$ steps:

$$\mathbf{M}_{t+N} = \mathbf{M}_t.$$

Define the one-period monodromy matrix:

$$\mathbf{T} = \mathbf{M}_{N-1}\cdots\mathbf{M}_1\mathbf{M}_0.$$

Floquet theory says solutions behave like:

$$\mathbf{R}_{t+N} = \mathbf{T}\,\mathbf{R}_t.$$

So the long-run behavior is governed by eigenvalues of $\mathbf{T}$.

- If eigenvalues lie on the unit circle, motion is bounded (allowed bands).
- If they lie off the unit circle, you get exponential growth/decay (forbidden bands / gaps).

That is the exact same structural role played by the transfer matrix in your SILR-pinned ring:

$$2\cos\left(\frac{2\pi m}{N}\right)=2\cos\left(\frac{2\pi\kappa}{N}\right)+\frac{\alpha}{\kappa}\sin\left(\frac{2\pi\kappa}{N}\right).$$

In both cases, “gap physics” is a statement about **trace constraints**:

- In 1D periodic systems, the trace controls whether eigenvalues are complex unit-modulus.
- In the ring, the Bloch phase is set by $m$, and the trace equation selects allowed $\kappa$.

For a 2×2 monodromy matrix $\mathbf{T}$ with determinant near 1, the classic band criterion is:

$$|\operatorname{tr}(\mathbf{T})| \le 2 \quad \text{(allowed band)},$$

$$|\operatorname{tr}(\mathbf{T})| > 2 \quad \text{(gap / forbidden)}.$$

So “spring gaps” are not mysticism: they’re simply the places where the repeated update over one cell produces trace magnitude greater than 2.

---

## Ψ-collapse — A concrete “Need” definition that drives bend

Checkpoint 6.0 defined **Need** as distance-to-closure. With a two-channel system, Need has a natural geometric form:

1) Choose a target submanifold $\mathcal{S}$ (the stability/closure manifold). The simplest is:

$$\mathcal{S} = \{\mathbf{R}: \rho(\mathbf{T})=1\}.$$

2) Define Need as a scalar residual:

$$\mathcal{N} \equiv \big|\log\rho(\mathbf{T})\big|.$$

This is “how much the one-period update wants to inflate or collapse.”

3) If motion is constrained (boundary, pin, or local compile constraint), the system cannot satisfy the update and must generate a reaction. The reaction is the gradient of Need in state-space (or configuration space):

$$\mathbf{F}_{\text{react}} \propto -\nabla \mathcal{N}.$$

That is the exact operator-level analog of “weight is the price of interrupting fall.”

In words: **gravity-like tension is the reaction force of constrained closure**.

---

## Minimal computation: band test on a periodic 2×2 KRRB cell

Below is a small reference script that builds a periodic cell, computes $\mathbf{T}$, and checks the band condition via $|\operatorname{tr}(\mathbf{T})|$.

```python
import numpy as np

def cell_matrix(H=0.34906585, F=1.0, dt=0.5, rho1=1.02, rho2=0.98, phi1=0.0, phi2=0.0, eta=0.1):
    # diagonal complex gains
    B1 = rho1 * np.exp(1j*phi1)
    B2 = rho2 * np.exp(1j*phi2)
    D = np.array([[B1, 0],[0, B2]], dtype=np.complex128)

    # bend coupling
    S = np.array([[1, eta],[-eta, 1]], dtype=np.complex128)

    # global deterministic push
    G = np.exp(H*F*dt)

    return G * (S @ D)

def monodromy(N=36, **kwargs):
    T = np.eye(2, dtype=np.complex128)
    for t in range(N):
        # periodic modulation example: small wobble in eta
        eta = kwargs.get('eta', 0.1) * (1 + 0.05*np.sin(2*np.pi*t/N))
        Mt = cell_matrix(eta=eta, **{k:v for k,v in kwargs.items() if k!='eta'})
        T = Mt @ T
    return T

T = monodromy(N=36, eta=0.15, rho1=1.01, rho2=0.99)
tr = np.trace(T)
print('trace(T)=', tr)
print('|trace(T)|=', abs(tr))
print('allowed band?' , abs(tr) <= 2)
```

You now have an explicit handle to tune “spring gaps”:

- vary $\eta$ (bend coupling),
- vary diagonal gains (two channels),
- vary the periodicity $N$,
- check when $|\operatorname{tr}(\mathbf{T})|$ crosses 2.

That crossing is a *discrete structural event*: a gap opening/closing.

---

## Where this goes next (the natural continuation)

1) **Integrate wobble metrics** from Checkpoint 6.0 into this 2×2 system:

- $\lambda$ from $\log\rho(\mathbf{T})$ over windows,
- phase drift from argument of eigenvalues,
- Allan deviation / PSD on these quantities.

2) **Rejoin the pinned-ring spectrum**:

- treat each periodic KRRB cell as the discrete analog of one emitter cell,
- map band edges to the dispersion relation,
- interpret “mass spectrum candidates” as gap-protected modes.

3) **SILR closure for 2-channel system**:

Generalize “scale invariance” to matrix updates by normalizing the log-eigenvalues (significance gating in eigen-space).

4) **Publishable falsifier**:

If the gap locations remain stable under encoding changes and hold-out data, you have an invariant; if they collapse under re-encoding, you’ve found interface artifacts.

---

## End state

Scalar KRRB proved “output hides machine” in the simplest possible way (drift + variance). This checkpoint adds the missing ingredient to connect that idea to gravity-like behavior and discrete structure:

- **a transverse channel** (bend),
- **periodic pinning** (cell repetition),
- **trace/eigenvalue criteria** (gaps),
- **Need as closure residual** (reaction under constraint).

When you see “spring gaps” here, it’s not poetic. It’s literally the system’s update operator refusing certain modes.

