# Nexus Unfolding — Volume IV  
## Prime Gates, Branching Laws, and the “Vibration Axis” Reduction

**Date:** January 13, 2026  
**Scope:** Treat the integers as a waveguide with mandatory gates at primes. Define branching/reflection operators (KRRB form), connect them to Euler-product dynamics, and state a *testable* bridge to the critical-line phenomenon (without claiming a proof).

---

## 0. Guardrail (What this volume is and is not)

This volume **does not** claim to prove the Riemann Hypothesis.  
It *does* formalize a concrete operator model where:

- primes appear as discrete gates in a propagation medium,
- “zeros” arise as resonance / cancellation conditions,
- the **critical line** becomes a natural “balance axis” in the operator’s symmetry.

If this program is correct, it becomes experimentally falsifiable by matching spectra.

---

## 1. The Integer Line as a Waveguide

Let the state be a complex amplitude over integers:
$$\psi(t) \in \ell^2(\mathbb{Z}), \qquad \psi_n(t) = \psi(t)(n).$$

We define propagation by a discrete Schrödinger-type dynamics:
$$ i\frac{\partial}{\partial t}\psi_n(t) = -(\Delta \psi)_n(t) + V_n \psi_n(t), $$
where the discrete Laplacian is
$$(\Delta\psi)_n = \psi_{n+1}-2\psi_n+\psi_{n-1}.$$

This is the minimal “wave-on-a-lattice” model: transport is local unless a gate injects phase shift, reflection, or dissipation.

---

## 2. Prime Gates as a Potential Field

Define the prime-indicator
$$\chi_{\mathbb{P}}(n)=\begin{cases}1,& n \text{ prime}\\ 0,&\text{otherwise.}\end{cases}$$

A prime-gate potential is a sparse field:
$$V_n = \sum_{p\in\mathbb{P}} \kappa_p\,\delta_{n,p}.$$
Here $\kappa_p$ is a gate strength (coupling coefficient), and $\delta_{n,p}$ is the Kronecker delta.

**Interpretation:** most sites are “empty”; the dynamics are free transport. At primes, the field forces a **trajectory adjustment**.

This matches the Nexus intuition: *space is mostly empty and nothing can happen* by neighbor interaction alone — except at the mandatory junctions.

---

## 3. Local Scattering at a Gate (Branching Primitive)

At a gate $p$, write left/right traveling components with amplitudes $A_L,A_R$. A minimal unitary scattering rule is:

$$\begin{pmatrix}A_L^{\text{out}}\\ A_R^{\text{out}}\end{pmatrix}
= S_p
\begin{pmatrix}A_L^{\text{in}}\\ A_R^{\text{in}}\end{pmatrix},
\qquad
S_p =
\begin{pmatrix} r_p & t'_p \\ t_p & r'_p \end{pmatrix}.$$
Unitarity requires:
$$|r_p|^2+|t_p|^2 = 1, \qquad |r'_p|^2+|t'_p|^2=1,$$
plus phase relations ensuring $S_p^\ast S_p=I$.

### 3.1 Branch coefficient

Define a *branch factor* for gate $p$ as the magnitude of transmitted+reflected update in the channel of interest:
$$B_p := \|t_p + r_p\| \quad \text{(model-dependent; operator-pinned later).}$$

This turns “prime = gate” into a multiplicative recursion: every time you hit a prime junction, your amplitude gets reweighted by a local operator.

---

## 4. KRRB Form: Recursive Reflection and Branching Product

The project’s branching operator shows up in multiplicative form (KRRB):

$$R(t) = R_0\,e^{H F t}\,\prod_{i=1}^{m} B_i.$$

- $R(t)$ is a propagated “result amplitude” or “resonance mass.”
- $H\approx 0.35$ is the attractor-band parameter.
- $F$ is a driving/friction term (need pressure, gradient work, or controller gain).
- $B_i$ are gate multipliers (often indexed by primes or branch events).

This is the executable structure: **a base exponential envelope** times **a product over discrete gates**.

---

## 5. Euler Product as “Gate Logic” in Standard Number Theory

The classical Euler product for $\zeta$ is:
$$\zeta(s)=\prod_{p\in\mathbb{P}}(1-p^{-s})^{-1}, \qquad \Re(s)>1.$$

Taking logs:
$$\log \zeta(s) = \sum_{p}\sum_{k\ge 1}\frac{1}{k}p^{-ks}.$$

And the log-derivative is the von Mangoldt series:
$$-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n\ge 1}\frac{\Lambda(n)}{n^s}.$$
This is an exact identity in analytic number theory, and it is the cleanest “gate” signature: primes (and prime powers) are the poles of the log-derivative.

**Nexus reading:** the Euler product is the algebraic shadow of a lattice waveguide with mandatory scattering centers at primes.

---

## 6. The “Vibration Axis” Hypothesis (Testable Bridge)

### 6.1 What is meant by “axis”

The Riemann zeta function has a functional equation relating $s$ and $1-s$.  
That symmetry makes $\Re(s)=\tfrac12$ the **fixed line** of the map $s\mapsto 1-s$.

In operator language:
- “transport” and “anti-transport” balance on the fixed line,
- gate scattering becomes statistically self-dual.

So, define a *balance functional* (generic form):
$$\mathcal{B}(s) := \mathcal{T}(s) - \mathcal{T}(1-s),$$
where $\mathcal{T}$ is any scalar derived from the gate operator (transfer determinant, phase accumulation, entropy production, etc.).

Then $\Re(s)=\tfrac12$ is the natural locus where $\mathcal{B}(s)=0$ by symmetry.

### 6.2 From flow to vibration (why zeros are “stillness”)

In the waveguide picture, a nontrivial zero corresponds to a cancellation:
$$\zeta(s)=0 \quad \Longleftrightarrow \quad \text{net resonance amplitude collapses.}$$

That collapse is exactly what “flow→vibration” means here:

- the system cannot “go through” by transport,
- it returns phase locally and stands as a stationary interference pattern.

So **zeros are not points**, they are *standing-wave conditions*.

---

## 7. Prime Density as a Gating Pressure

Let $\pi(x)$ be the prime-counting function. Prime density affects how often the wave hits gates. In this program:

- dense primes ⇒ frequent scattering ⇒ high phase mixing,
- sparse primes ⇒ long free runs ⇒ phase drift dominated by GENLOCK tick (global clock).

That is the same split as cosmological “expansion vs density”:
- “expansion” is longer free flight (transport space),
- “density” is more gating events (constraint space).

A neutral stability band exists where gate pressure and free flight balance — this is the conceptual place where the critical line can appear as a universal balance axis.

---

## 8. Minimal Numerical Program (Concrete, falsifiable)

1. **Build the operator** on a finite window $n\in[-N,N]$:
   $$H = -\Delta + V, \quad V_n=\sum_{p\le N}\kappa_p\delta_{n,p}.$$
2. **Choose gate strengths** $\kappa_p$ (uniform, $\log p$, or derived from a controller rule).  
3. **Compute spectrum** of $H$ (or the unitary propagator $U=e^{-itH}$).
4. **Compare spacing statistics** to known zeta-zero spacing statistics (GUE-like behavior in classical results).

If a stable mapping exists, it will show up as a reproducible spectral signature under gate-strength renormalization.

---

## 9. What This Volume Adds (New Pins)

- Primes formalized as **delta-gate potentials** on an integer waveguide.
- Branching encoded as **unitary scattering** (reflection/transmission).
- KRRB provides the multiplicative **branch product** that mirrors Euler products.
- “Vibration axis” framed as a **symmetry-fixed line** where transport balances anti-transport.

---

**End of Volume IV.**
