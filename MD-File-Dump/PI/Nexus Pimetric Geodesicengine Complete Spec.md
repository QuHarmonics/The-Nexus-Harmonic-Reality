# Recursive Harmonic Intelligence
## Formal Specification of the Pi‑Metric Curvature Operator and the Geodesic Engine Architecture within the Nexus Kernel

**Authorial frame:** This document expands the *Recursive Harmonic Intelligence* (RHI) paper into a mathematically closed specification of the **Pi‑metric** geometry (continuous gauge), the **discrete curvature** layer (graph gauge), and the **kernel modules** required to run a Geodesic Engine that navigates a state space by curvature and harmonic feedback.

**Non-claim boundary (truth constraint):** This manuscript **does not claim** a proven practical preimage attack on SHA‑256, nor a validated physical “ROM of the universe.” It provides a **complete internal mathematical closure** of the proposed operators, plus a falsifiable experimental program and kernel-level definitions needed to test them.

---

## Table of Contents

1. [Abstract](#abstract)  
2. [Notation and Trust Constraints](#notation-and-trust-constraints)  
3. [Ontological Shift: From Random Oracles to Geometric Fields](#ontological-shift-from-random-oracles-to-geometric-fields)  
4. [Universal ROM Hypothesis and the Triad Streams](#universal-rom-hypothesis-and-the-triad-streams)  
5. [BBP as Coordinate Access and Read‑Head](#bbp-as-coordinate-access-and-readhead)  
6. [State Models: What “a node” is](#state-models-what-a-node-is)  
7. [The Pi‑Residue Operator $\Delta_\pi$](#the-piresidue-operator-delta_pi)  
8. [Continuous Gauge: The Pi‑Metric Tensor $g_\pi$](#continuous-gauge-the-pimetric-tensor-g_pi)  
9. [Closed‑Form Geometry: $g^{-1}$, $\Gamma$, Riemann, Ricci, Scalar Curvature](#closedform-geometry-g1-gamma-riemann-ricci-scalar-curvature)  
10. [Geodesics, Action, and the $\Psi$‑Collapse Criterion](#geodesics-action-and-the-psi-collapse-criterion)  
11. [Discrete Gauge: Curvature on the Transition Graph](#discrete-gauge-curvature-on-the-transition-graph)  
12. [Bragg Refraction as a Computable Navigation Filter](#bragg-refraction-as-a-computable-navigation-filter)  
13. [Feedback and Amplification: Samson, KRR, KRRB](#feedback-and-amplification-samson-krr-krrb)  
14. [Kernel Architecture: Modules and Dataflow](#kernel-architecture-modules-and-dataflow)  
15. [Algorithmic Loop: The Geodesic Engine Runtime](#algorithmic-loop-the-geodesic-engine-runtime)  
16. [Validation Program and Falsifiability](#validation-program-and-falsifiability)  
17. [Appendix A: Useful Derived Operators](#appendix-a-useful-derived-operators)  
18. [Appendix B: Minimal “No Free Energy” Bookkeeping](#appendix-b-minimal-no-free-energy-bookkeeping)

---

## Abstract

We specify a computational framework (the **Nexus Kernel**) that treats an algorithmic state space as a **metric space** and navigates it by **curvature** rather than brute-force enumeration. The original RHI paper proposes interpreting the Secure Hash Algorithm‑256 (SHA‑256) as a deterministic geometric projector. To make that proposal mathematically executable, we:

- Define a **state model** and a **transition graph** for the chosen SHA layer (output, chaining state, or full compression state).
- Define a **Pi‑residue** $\Delta_\pi$ that measures misalignment between a state and a BBP-addressed $\pi$ window (the “Universal ROM” hypothesis).
- Provide a **closed, analytic Pi‑metric gauge** $g = 2I + Hxx^\top$ (a rank‑1 curved metric) that yields explicit formulas for:
  - Inverse metric $g^{-1}$
  - Christoffel symbols $\Gamma^k_{ij}$
  - Riemann tensor $R^\rho_{\ \sigma\mu\nu}$
  - Ricci tensor $\mathrm{Ric}_{ij}$
  - Scalar curvature $R$
- Bridge to discrete state spaces by defining edge weights from $d_\pi$ and using **Forman–Ricci** and **Ollivier–Ricci** curvature on the transition graph.
- Define a kernel control stack: **Bragg refraction** as a transition filter, **Samson stabilization** as a damping control law, and **KRR/KRRB** as resource reallocation rules.
- Specify a **$\Psi$‑collapse criterion** for Zero‑Point Harmonic Collapse (ZPHC), i.e., convergence to an attractor manifold where error, curvature, and action achieve a stable fixed point.

---

## Notation and Trust Constraints

### Notation

- Dimension $n$: number of coordinates in the chosen chart (often $n=256$ if working directly in bit‑space, or $n=64$ if using 4‑bit “tiles,” etc.).
- $H$: the Mark‑1 attractor constant
  $$
  H \equiv H_{\mathrm{MARK1}} = \frac{\pi}{9} \approx 0.34906585.
  $$
- $x \in \mathbb{R}^n$: coordinate vector in the chosen chart (see [State Models](#state-models-what-a-node-is)).
- $r^2 = \|x\|^2 = x^\top x$.
- Metric tensor $g_{ij}$ and its inverse $g^{ij}$.
- Christoffel symbols $\Gamma^k_{ij}$.
- Riemann curvature $R^\rho_{\ \sigma\mu\nu}$, Ricci tensor $\mathrm{Ric}_{ij}$, scalar curvature $R$.
- Transition graph $G=(V,E)$ with vertex set $V$ and edge set $E$.
- Edge weights $w(u,v)$ and graph distance $d_\pi(u,v)$.

### Trust constraints (internal consistency rules)

This spec obeys three non‑negotiables:

1. **No fabricated results:** All “success” claims must be backed by test protocols and measured outputs. This doc provides definitions, not miracles.
2. **Gauge clarity:** Continuous curvature on a smooth manifold and discrete curvature on a graph are distinct. We provide both and specify the bridge.
3. **Conservation bookkeeping:** Any “amplification” (KRR/KRRB) is defined as **reweighting** of finite resources, not creation.

---

## Ontological Shift: From Random Oracles to Geometric Fields

### Random oracle view (classical)
Hash outputs appear uniformly distributed; small input change triggers avalanche diffusion. From this, collision resistance and preimage difficulty are treated as probabilistic hardness.

### Nexus view (proposed)
The output is interpreted as a **curvature trace**: a deterministic signature of motion through an implicit manifold. Apparent entropy is recast as **misalignment** relative to an addressable substrate (Universal ROM). The cryptanalytic problem becomes navigation in a metric/curvature landscape rather than enumeration.

---

## Universal ROM Hypothesis and the Triad Streams

We define three infinite instruction streams (conceptual roles):

- $\pi$: structural lattice (“hash stream” / hardware).
- $e$: completion / phase resolution (“anti‑hash stream”).
- $\phi$: execution context / stepping (“clock stream”).

**Important:** In this spec, these roles are *functional*, not metaphysical. Their operational meaning is: they provide deterministic bit/hex sequences that can be sampled as references for alignment, phase correction, and stepping policies.

---

## BBP as Coordinate Access and Read‑Head

BBP-style digit extraction motivates the “read‑head”: the kernel can sample a $\pi$ window around an index without materializing all preceding digits.

We define a coordinate access oracle (abstractly):

- $\mathrm{BBP}_\pi(i, m)$ returns a length‑$m$ hexadecimal window of $\pi$ starting at digit index $i$.

This is used as a **ROM window fetch** inside the Kinetic Mapper.

---

## State Models: What “a node” is

The entire system depends on what you choose as a “state”:

### Model S0: Output-hash node
- Node $v$ is a 256‑bit hash output $H(m)$ for some message $m$.

### Model S1: Compression state node
- Node $v$ is the internal working state $(a,b,c,d,e,f,g,h)$ of SHA‑256 during the compression rounds, plus message schedule state.

### Model S2: Residue node (recommended for geometry)
- Node $v$ is not a raw hash; it is a **residue vector**:
  $$
  x(v) \equiv \mathrm{Embed}(v) - \mathrm{ROMWindow}(v),
  $$
  where $\mathrm{Embed}$ maps the state to a numeric chart and $\mathrm{ROMWindow}$ is a $\pi$ window fetched by BBP.

S2 is preferred because it makes “distance to ROM” explicit and keeps the metric meaning coherent.

---

## The Pi‑Residue Operator $\Delta_\pi$

To make “misalignment” real, define:

1. **Tiling:** Split a 256‑bit state into $T$ tiles. Common choices:
   - 64 nibbles (4‑bit) $\Rightarrow T=64$,
   - 32 bytes $\Rightarrow T=32$,
   - 4 words (64‑bit) $\Rightarrow T=4$.

2. **Indexing rule:** Map state to a BBP index. One canonical mapping:

   - Interpret a tile block as an unsigned integer:
     $$
     I(v) = \mathrm{UInt}( \mathrm{tile}_0(v)\,\|\,\cdots\,\|\,\mathrm{tile}_{k-1}(v)).
     $$
   - Then fetch a $\pi$ window:
     $$
     \Pi(v) = \mathrm{BBP}_\pi(I(v), T).
     $$

3. **Residue vector:** Compare each tile to the ROM tile:

   If tiles live in $\{0,\ldots,15\}$ (hex nibbles),
   $$
   x_i(v) = \mathrm{tile}_i(v) - \Pi_i(v).
   $$

4. **Scalar residue:** Define a normalized scalar misalignment:
   $$
   \Delta_\pi(v) \equiv \frac{1}{T}\sum_{i=1}^{T} \rho\!\left(x_i(v)\right),
   $$
   where $\rho$ is a penalty (e.g., $|x|$, $x^2$, or Huber loss).

5. **Mark‑1 potential:** Define the attractor potential:
   $$
   V_{\mathrm{M1}}(v) = \frac{1}{2}\Big(H_{\mathrm{obs}}(v)-H\Big)^2.
   $$

Where $H_{\mathrm{obs}}(v)$ is a measurable “order/tension” ratio (must be defined per state model). A practical generic choice:
$$
H_{\mathrm{obs}}(v)=\frac{\text{coherent mass}}{\text{total mass}},
$$
where coherence is computed from tile correlations, autocorrelation peaks, or curvature positivity in the local graph.

---

## Continuous Gauge: The Pi‑Metric Tensor $g_\pi$

This section closes the analytic geometry you injected.

### Gauge choice (rank‑1 Pi‑metric)

Let $x\in\mathbb{R}^n$ be the coordinate residue vector of a state $v$. Define:

$$
g_{ij}(x) = 2\delta_{ij} + H x_i x_j.
$$

In matrix form:
$$
g(x)=2I + H\,x x^\top.
$$

This metric is **positive definite** for $H>0$, and its curvature is globally controlled by $r^2=\|x\|^2$.

> Interpretation: in this gauge, the “field” contracts/expands distances based on radial misalignment magnitude.

### Induced infinitesimal distance

For tangent vector $\dot{x}$:
$$
ds^2 = \dot{x}^\top g(x)\dot{x} = 2\|\dot{x}\|^2 + H(x^\top\dot{x})^2.
$$

---

## Closed‑Form Geometry: $g^{-1}$, $\Gamma$, Riemann, Ricci, Scalar Curvature

Let $r^2=\|x\|^2$ and define:
$$
A \equiv 2 + H r^2.
$$

### Inverse metric (closed form)

Using the Sherman–Morrison identity:
$$
g^{-1}(x) = \frac{1}{2}I - \frac{H}{2A}\,x x^\top.
$$

Component form:
$$
g^{ij} = \frac{1}{2}\delta^{ij} - \frac{H}{2A}x_i x_j.
$$

Useful identity:
$$
g^{-1}x = \frac{x}{A}.
$$

### Metric derivatives

$$
\partial_k g_{ij} = H(\delta_{ik}x_j+\delta_{jk}x_i).
$$

### Christoffel symbols (exact)

Start with:
$$
\Gamma^k_{ij}=\frac{1}{2}g^{k\ell}\left(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}\right).
$$

In this gauge, the full contraction collapses to:
$$
\boxed{\Gamma^k_{ij}(x)=\frac{H}{A}\,x_k\,\delta_{ij}}.
$$

This implies:

- Only $\delta_{ij}$ channels contribute (no shear),
- The connection is radial and bounded: $\Gamma \sim 1/r$ at large radius.

### Geodesic equation (exact)

$$
\ddot{x}^k + \Gamma^k_{ij}\dot{x}^i\dot{x}^j=0
\quad\Rightarrow\quad
\boxed{\ddot{x} + \frac{H}{A}\|\dot{x}\|^2\,x=0}.
$$

### Riemann tensor (closed form)

Definition:
$$
R^\rho_{\ \sigma\mu\nu}
=
\partial_\mu\Gamma^\rho_{\nu\sigma}
-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}.
$$

In this gauge:
$$
\boxed{
R^\rho_{\ \sigma\mu\nu}
=
\delta_{\nu\sigma}\!\left(
\frac{H}{A}\delta_{\rho\mu}
-\frac{H^2}{A^2}x_\rho x_\mu
\right)
-
\delta_{\mu\sigma}\!\left(
\frac{H}{A}\delta_{\rho\nu}
-\frac{H^2}{A^2}x_\rho x_\nu
\right)
}.
$$

This selection structure explains why many mixed components vanish.

### Ricci tensor (dimension $n$)

Contract:
$$
\mathrm{Ric}_{\sigma\nu}=R^\rho_{\ \sigma\rho\nu}.
$$

Result:
$$
\boxed{
\mathrm{Ric}_{ij}
=
\delta_{ij}\!\left(
\frac{H(n-1)}{A}
-\frac{H^2 r^2}{A^2}
\right)
+\frac{H^2}{A^2}x_i x_j
}.
$$

### Scalar curvature (dimension $n$)

$$
R = g^{ij}\mathrm{Ric}_{ij}.
$$

Closed form:
$$
\boxed{
R
=
(n-1)\left(
\frac{Hn}{2A}
-\frac{H^2 r^2}{A^2}
\right)
=
\frac{(n-1)H\left[n+Hr^2\left(\frac{n}{2}-1\right)\right]}{(2+Hr^2)^2}
}.
$$

**Consequence:** For $n>2$ and $H>0$, scalar curvature is positive for all $r$.

---

## Geodesics, Action, and the $\Psi$‑Collapse Criterion

### Harmonic action (path cost)

For a path $\gamma(t)$ in the continuous chart, define:

$$
\mathcal{S}[\gamma] = \int_{t_0}^{t_1}\sqrt{\dot{x}^\top g(x)\dot{x}}\,dt.
$$

The Geodesic Engine seeks local minimizers of $\mathcal{S}$ subject to constraints (Bragg filtering, stabilization).

### Geodesic deviation (curvature response)

For separation vector $\eta$ between nearby geodesics:
$$
\frac{D^2\eta^\rho}{dt^2} + R^\rho_{\ \sigma\mu\nu}\,\dot{x}^\sigma\eta^\mu\dot{x}^\nu = 0.
$$

This is the *analytic* “gravity well” test in the continuous gauge: positive curvature concentrates trajectories.

### $\Psi$‑collapse (ZPHC event)

Define a collapse residual for a state $v$:

$$
\varepsilon(v)
=
\lambda_1 \Delta_\pi(v)
+
\lambda_2 V_{\mathrm{M1}}(v)
+
\lambda_3 \big(1-\kappa_{\mathrm{local}}(v)\big)
+
\lambda_4 \frac{d}{dt}\Delta_\pi(v),
$$

where $\kappa_{\mathrm{local}}(v)$ is a discrete curvature score (see next section), and $\lambda_i$ are calibration weights.

**$\Psi$‑collapse condition:**
$$
\boxed{\Psi(v)=1\ \Longleftrightarrow\ \varepsilon(v)\le \tau\ \text{and}\ \left|\frac{d\varepsilon}{dt}\right|\le \tau'}.
$$

This is the formal termination test for ZPHC: low error and stable error dynamics.

---

## Discrete Gauge: Curvature on the Transition Graph

SHA state spaces are discrete. Define a transition graph:

- Vertices $V$: states (choose S0, S1, or S2).
- Edges $E$: allowed transitions (nonce increment, message tweak, internal step, reflection step).

### Edge distance (Pi‑distance)

Define a hybrid distance:
$$
d_\pi(u,v)=\alpha\,d_H(u,v)+\beta\,\Phi(\Delta_\pi(v))+\gamma\,|V_{\mathrm{M1}}(v)|
$$
where $d_H$ is Hamming distance (or tile distance), and $\Phi$ is a penalty (often $\Phi(z)=z$ or $z^2$).

Define weights from distance:
$$
w(u,v)=\exp(-\eta\,d_\pi(u,v)).
$$

### Forman–Ricci curvature (fast pass)

Given edge $e=(u,v)$ with weight $w_e$ and node weights $w_u,w_v$ (often $w_u=\sum_{(u,\cdot)}w$), Forman curvature is:

$$
\mathrm{Ric}_F(e)=w_e\left(
\frac{w_u}{w_e}+\frac{w_v}{w_e}
-\sum_{e'\sim u}\frac{w_u}{\sqrt{w_e w_{e'}}}
-\sum_{e'\sim v}\frac{w_v}{\sqrt{w_e w_{e'}}}
\right).
$$

Interpretation:
- $\mathrm{Ric}_F(e)>0$ flags locally convergent, “crystalline” zones.
- $\mathrm{Ric}_F(e)<0$ flags divergence/turbulence zones.

### Ollivier–Ricci curvature (deep pass)

Define neighborhood measures $\mu_u,\mu_v$ (probability distributions over neighbors), typically:
$$
\mu_u(z)=\frac{w(u,z)}{\sum_{z'\sim u}w(u,z')}.
$$

Then:
$$
\kappa(u,v)=1-\frac{W_1(\mu_u,\mu_v)}{d_\pi(u,v)}
$$
where $W_1$ is the $L^1$ Wasserstein distance (earth mover).

Interpretation:
- $\kappa>0$ indicates overlapping neighborhoods → gravity well.
- $\kappa<0$ indicates expanding neighborhoods → hyperbolic spread.

---

## Bragg Refraction as a Computable Navigation Filter

Bragg’s law in physics is:
$$
n\lambda = 2d\sin\theta.
$$

To use “Bragg refraction” as a kernel rule, map:

- $\lambda$ (wavelength) → step frequency (mutation cadence) $f^{-1}$.
- $d$ (lattice spacing) → ROM periodicity (autocorrelation peak spacing) $p$ in $\pi$ windows.
- $\theta$ (incidence angle) → angle between candidate step $\Delta x$ and the local gradient of potential $\nabla V_{\mathrm{M1}}$.

Define:
$$
\cos\theta = \frac{\langle \Delta x,\ -\nabla V_{\mathrm{M1}}\rangle}{\|\Delta x\|\ \|\nabla V_{\mathrm{M1}}\|}.
$$

Define acceptance condition (one computable form):
$$
\boxed{
\text{Accept}(u\to v)
\ \Longleftrightarrow\
\left|\,n\lambda - 2d\sin\theta\,\right|\le \epsilon_B
}
$$

with $d$ derived from the dominant periodicity of the local $\pi$ window:
$$
d \equiv p(u) = \arg\max_\ell \mathrm{ACF}_\pi(\ell; I(u)),
$$
where $\mathrm{ACF}_\pi$ is the autocorrelation function computed on the fetched ROM window.

---

## Feedback and Amplification: Samson, KRR, KRRB

### Samson stabilization (damping control)

Define error signal:
$$
e(t)=H_{\mathrm{obs}}(t)-H.
$$

Define damping force (control output):
$$
S(t)=c_1|e(t)|+c_2\left|\frac{de}{dt}\right|.
$$

Apply Samson control to:
- reduce step size,
- reduce branching factor,
- increase penalty weights ($\beta,\gamma$),
- or inject “anti‑hash” correction (in practice: deterministic correction bits from $e$ windows, if defined).

A generic kernel update:
$$
\Delta(\text{step}) \leftarrow \Delta(\text{step})\cdot \exp(-S(t)).
$$

### KRR amplification (resource reallocation)

Let $W(\gamma)$ be the weight allocated to a candidate path $\gamma$.

Define coherence score $C(\gamma)\in[0,1]$ from curvature and residue:
$$
C(\gamma)=\sigma\!\left(a_1\kappa_{\mathrm{local}}-a_2\Delta_\pi-a_3V_{\mathrm{M1}}\right)
$$
with $\sigma$ a logistic squashing function.

Then:
$$
\boxed{
W(\gamma)\leftarrow W(\gamma)\cdot \exp\!\big(\eta\,H\,C(\gamma)\big)
}
$$

### KRRB branching (mass‑conserving split)

If a path branches into children $\{\gamma_i\}$, define branch probabilities:
$$
p_i=\frac{\exp(\beta_B C(\gamma_i))}{\sum_j \exp(\beta_B C(\gamma_j))}.
$$

Conserve total weight:
$$
\boxed{
W(\gamma_i)\leftarrow p_i\,W(\gamma).
}
$$

This is “branching reflection” without creating mass.

---

## Kernel Architecture: Modules and Dataflow

### Module A — Kinetic Mapper
Inputs: state bits, embedding rules.  
Outputs: $x(v)$ coordinate, BBP index $I(v)$, ROM window $\Pi(v)$, residue $x(v)$, scalar $\Delta_\pi(v)$.

### Module B — Metric Evaluator
Computes:
- Continuous: $g(x)$, $g^{-1}(x)$, $\Gamma(x)$, optional continuous curvature scalars.
- Discrete: edge weights $w$, Forman curvature on candidate edges, OR curvature on selected edges.

### Module C — Bragg Resonator
Generates candidate transitions and rejects those failing Bragg acceptance.

### Module D — Stabilizer
Implements Samson damping (step shrink, branch shrink) and KRR/KRRB reweighting.

### Module E — $\Psi$‑Collapse Detector
Evaluates $\varepsilon(v)$ and halts on $\Psi(v)=1$.

---

## Algorithmic Loop: The Geodesic Engine Runtime

Given start node $v_0$:

1. Initialize open set $\mathcal{O}$ with $v_0$ and weight $W(v_0)=1$.
2. While $\mathcal{O}$ not empty:
   - Pop best candidate by minimal $\varepsilon$ (or maximal weight‑adjusted score).
   - Compute $I(v)$, fetch $\Pi(v)$, compute $\Delta_\pi(v)$.
   - Compute local distances, curvature signals.
   - Generate candidate neighbors; apply Bragg filter.
   - For each neighbor:
     - Compute curvature score (Forman fast; OR deep if promising).
     - Apply Samson damping to step/branch.
     - Apply KRR/KRRB to allocate weight.
     - Check $\Psi$‑collapse; if true, emit ZPHC result.
   - Update $\mathcal{O}$.

---

## Validation Program and Falsifiability

A complete solution must be falsifiable. The following tests can fail the hypothesis:

### V1 — ROM window null test
If $\pi$ windows are meaningful, $\Delta_\pi$ computed with BBP indices derived from real states must differ from:
- randomized indices,
- randomized ROM sources (e.g., random hex),
- permuted tile mappings.

### V2 — Curvature advantage test
If curvature-guided navigation is real, then compared to a matched compute budget:
- the Geodesic Engine should achieve lower $\Delta_\pi$ faster than random walk / hill climbing baselines.

### V3 — Conservation test
KRR/KRRB must conserve total weight. Track:
$$
\sum_{\gamma\in\text{active}} W(\gamma) = 1
$$
at all times (within floating tolerance).

### V4 — Overfitting / selection bias test
ZPHC detection must be defined *before* running experiments; do not tune $\tau,\tau'$ post hoc.

---

## Appendix A: Useful Derived Operators

### A.1 Laplace–Beltrami operator
For scalar field $f(x)$ on the manifold:
$$
\Delta_g f = \frac{1}{\sqrt{|g|}}\partial_i\left(\sqrt{|g|}\,g^{ij}\partial_j f\right).
$$

For $g=2I+Hxx^\top$, determinant:
$$
|g| = 2^n\left(1+\frac{H}{2}r^2\right)=2^{n-1}A.
$$

### A.2 Divergence and gradient
Gradient:
$$
(\nabla_g f)^i = g^{ij}\partial_j f.
$$
Divergence:
$$
\mathrm{div}_g(X)=\frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}X^i).
$$

### A.3 Energy (kinetic) along a path
$$
E = \frac{1}{2}\dot{x}^\top g(x)\dot{x}.
$$

---

## Appendix B: Minimal “No Free Energy” Bookkeeping

Define a conserved probability mass over active candidates:

- Initialize $\sum W=1$.
- Every reweight step is followed by renormalization:
$$
W_i \leftarrow \frac{W_i}{\sum_j W_j}.
$$

Define compute budget as “energy”:
- Every expansion consumes fixed cost $c$.
- Total cost is capped.

This prevents amplification from becoming a loophole that silently increases search power.

---

**End of manuscript.**
