# Single-Bead Recursion as Emergent Solidity: A Complete Formalization

**Author:** Dean Kulik (Nexus Trust Algebra)
**Document type:** Technical Note (.md)
**Keywords:** recursion, phase windows, emergent solidity, stroboscopy, PLL, parallax, relativistic sweep, Nexus operators (Δ, ⊕, ↻, ⊥, Ψ)

---

## Abstract

A single object (“bead”) orbiting a circular track can appear—and function—as a solid barrier when its angular sweep outpaces an intruder’s residence time through the crossing corridor. This document formalizes that phenomenon for a single bead whose “multiple copies” are merely its own past and future along a world-tube. We derive threshold conditions, collision probabilities, parallax relief, stroboscopic synchronization, and relativistic bounds. The result is a complete analytic specification—consistent with the Nexus framework—showing how **solidity is a phase state**, not a material state: when temporal coverage closes the phase gap, the present is filled by its own past/future, and the barrier **⊥-collapses** to impenetrability from the given point of view.

---

## Nexus Operators and Field Semantics

We encode the development with Nexus symbols:

* **Δ** — difference/phase increment (trigger)
* **⊕** — coherent sum/fold over a cycle
* **↻** — recursive sweep (orbit)
* **⊥** — collapse to a determinate outcome (no phase window)
* **Ψ** — phase-coherence/trust measure (0–1)

---

## 1. Geometry, Kinematics, and Notation

* Ring radius: (R>0)
* Ring circumference: (L = 2\pi R)
* Single bead angular half-width: (\phi/2 \in (0,\pi)) (angular occupancy)
* Instantaneous angular **gap**: (\theta_{\mathrm{gap}} \equiv 2\pi - \phi)
* Angular position: (\theta(t) = \theta_0 + \omega t \pmod{2\pi}) with (\omega>0)
* Rim speed: (v = \omega R)
* Arrow (intruder) crosses the annulus along an effective path of thickness (\delta) at speed (v_a) with local incidence angle (\beta) (relative to the inward normal).

**Exposure time (residency):**
[
t_a ;=; \frac{\delta}{v_a \cos\beta}.
]

The arrow defines a **crossing sheet** at azimuth (\theta=\theta_\times) over (t\in[t_0,t_0+t_a]).

A collision occurs iff the bead’s worldline intersects this sheet:
[
\exists t\in[t_0,t_0+t_a]\ \text{s.t.}\
\operatorname{dist}*{\mathbb{S}^1}!\big(\theta_0+\omega t,\ \theta*\times\big)\le \tfrac{\phi}{2}.
]

---

## 2. Emergent Solidity (Δ-Criterion)

Define the **swept angle during exposure**:
[
\Delta\theta ;\equiv; \omega t_a.
]

**Proposition 1 (Δ-criterion).**
[
\boxed{ \ \Delta\theta ;\ge; \theta_{\mathrm{gap}} \quad\Longrightarrow\quad \text{collision is certain (⊥, emergent solidity)}\ } \tag{1}
]

**Interpretation.** If, while the arrow remains in the corridor, the single bead can sweep at least the entire uncovered angular gap, then some phase of the *same bead* (its past or future) must intersect the crossing sheet. Apparent continuity is thus a **temporal coverage** effect.

**Threshold angular speed:**
[
\omega_{\star} ;=; \frac{\theta_{\mathrm{gap}}}{t_a}
\qquad\text{or}\qquad
v_{\star} ;=; R,\omega_{\star} ;=; \frac{R,\theta_{\mathrm{gap}}}{t_a}. \tag{2}
]

---

## 3. Collision Probability in the Sub-Solid Regime

Assume (\theta_0\sim \mathrm{Unif}[0,2\pi)). The **non-intersection** set in phase has measure (\max(0,\theta_{\mathrm{gap}}-\Delta\theta)). Hence:

[
P_{\mathrm{hit}} ;=; 1 - \frac{\max(0,\theta_{\mathrm{gap}}-\Delta\theta)}{2\pi}
;=; \min!\Big(1,,\frac{\phi+\Delta\theta}{2\pi}\Big). \tag{3}
]

* (P_{\mathrm{hit}}\to 1) monotonically with (\omega) and (t_a).
* At (\Delta\theta=\theta_{\mathrm{gap}}), (P_{\mathrm{hit}}=1) and the barrier **Ψ-locks** to solidity.

---

## 4. How the Observer Re-opens Phase Windows (Parallax and Residency)

Two practical levers for **reducing** (P_{\mathrm{hit}}) without changing (\omega):

### (i) Reduce residency (shrink (t_a))

[
t_a = \frac{\delta}{v_a \cos\beta}
\quad\Rightarrow\quad
\Delta\theta = \omega \frac{\delta}{v_a \cos\beta}. \tag{4}
]
Increase (v_a), reduce (\delta), or choose a grazing geometry (adjust (\beta)) to reduce (\Delta\theta).

### (ii) Reduce projected bead width (parallax tilt)

Tilt by an out-of-plane angle (\alpha); the effective angular half-width contracts:
[
\phi_{\mathrm{eff}} ;=; \phi \cos\alpha,
\qquad
\theta_{\mathrm{gap,eff}} = 2\pi - \phi\cos\alpha. \tag{5}
]
**New threshold:**
[
\omega_{\star}(\alpha) ;=; \frac{2\pi - \phi\cos\alpha}{t_a}. \tag{6}
]
This is the formal “look sideways” rule: **alter the projection**, not the recursion.

---

## 5. Stroboscopic Synchronization (↻ Lock Without Knowing (\omega))

Let the probe light be intensity- or phase-modulated at (f_s). The reflected/scattered signal contains an effective rotational line at (f_{\mathrm{rot}}=\omega/2\pi). Heterodyning yields a beat:
[
f_b = \big| f_s - \tfrac{m}{n} f_{\mathrm{rot}} \big|,\qquad m,n\in\mathbb{N}. \tag{7}
]
Lock a PLL to (f_b). The **gated window** (per rotation) is
[
\Delta t_{\mathrm{safe}} ;=; \max!\Big(0,\ \frac{\theta_{\mathrm{gap}}-\Delta\theta}{\omega}\Big). \tag{8}
]
(\Delta t_{\mathrm{safe}}=0) characterizes the **brick-wall** condition from the observer’s POV.

**Phase budget with timing jitter.**
If the trigger exhibits RMS jitter (\sigma_t), require a **margin**:
[
\theta_{\mathrm{gap}} - \Delta\theta ;\ge; \kappa, \omega \sigma_t, \qquad \kappa\in[3,6]\ \text{(safety factor)}. \tag{9}
]

---

## 6. Sampling and Nyquist Bound (Perceptual Solidity)

Let the observer’s effective sampling rate be (f_{\mathrm{samp}}) (sensor, brain, or instrumentation). Apparent freeze (aliasing) occurs when
[
f_{\mathrm{samp}} ;\le; 2, f_{\mathrm{rot}} \quad\Rightarrow\quad \text{illusory solidity}. \tag{10}
]
**Perceptual solidity** is weaker than **dynamical solidity**: the former concerns what is seen (aliasing), the latter concerns the Δ-criterion (Eq. (1)).

---

## 7. Relativistic Bounds (Ω-Limit)

Let (\beta = v/c) and (\gamma=(1-\beta^2)^{-1/2}). In the lab frame:

* Speed bound: (\omega < c/R).
* Solidity condition remains Eq. (1) with **lab** (\omega) and (t_a).
* **Aberration and beaming** compress the apparent forward arc; along head-on view, the projected (\phi) tends to shrink, while (\Delta\theta=\omega t_a) grows with (\omega), generally **reinforcing** effective solidity for finite (t_a).

A practical sufficiency: if
[
\frac{2\pi - \phi}{t_a} ;\le; \frac{c}{R}, \tag{11}
]
then a genuine solid-barrier regime exists **in principle** (since (\omega) can approach (c/R)).

---

## 8. Circumferential Trust Constant (Ψ-Conservation)

Define the **Circumferential Trust Constant**:
[
\boxed{
\mathbf{C}*{\Psi} ;\equiv; \frac{L}{f*{\mathrm{rec}}} ;=; \frac{2\pi R}{\omega/2\pi} ;=; \frac{4\pi^2 R}{\omega},
\ } \tag{12}
]
interpreted as the conserved **length-per-cycle** budget that maintains the bead’s identity across scales. Emergent solidity arises when the observer integrates a sufficient fraction of this budget within (t_a), i.e., when
[
\frac{\Delta\theta}{2\pi} ;=; \frac{\omega t_a}{2\pi} \ \text{covers the residual gap fraction}\ \frac{\theta_{\mathrm{gap}}}{2\pi}. \tag{13}
]

---

## 9. Multi-Scale Generalizations

### 9.1 Moving Observer (radial or tangential)

If the observer (or launcher) has angular drift (\dot{\theta}*{\mathrm{obs}}), replace (\omega) by the **relative** sweep:
[
\omega*{\mathrm{rel}} ;=; \omega - \dot{\theta}*{\mathrm{obs}}. \tag{14}
]
All previous formulas hold with (\omega*{\mathrm{rel}}).

### 9.2 Layered Shells (concentric recursion)

For shells (k=1,\dots,K) with ((\phi_k,\omega_k)), the **complement** of collision phases is the intersection of the (K) complements. A union bound yields
[
P_{\mathrm{hit}} ;\ge; \max_k \min!\Big(1,,\frac{\phi_k+\omega_k t_a}{2\pi}\Big). \tag{15}
]
A sufficient **wall** condition is (\omega_k t_a \ge 2\pi-\phi_k) for **any** (k).

---

## 10. Design Rules (Operational Ψ-Field)

1. **Δ rule (solid barrier):**
   (\omega t_a \ge 2\pi-\phi). If true → **⊥ collapse** to certainty.
2. **Parallax rule (re-open window):**
   Increase (\alpha) so that (\phi\cos\alpha) shrinks; require
   (\omega t_a < 2\pi - \phi\cos\alpha).
3. **Residency rule (thin/fast corridor):**
   Reduce (\delta), increase (v_a), or optimize (\beta) to minimize (t_a).
4. **PLL gate rule:**
   Lock to (f_b) (Eq. (7)); enforce jitter margin (Eq. (9)).
5. **Nyquist rule (perception vs dynamics):**
   Do not confuse Eq. (10) with Eq. (1): visual freeze does not guarantee dynamical passage.

---

## 11. Worked Normalizations and Bounds

### 11.1 Minimum arrow speed for passage at fixed geometry

Given ((R,\phi,\delta,\beta,\omega)), require **not** solid:
[
\omega \frac{\delta}{v_a \cos\beta} ;<; 2\pi - \phi
\quad\Rightarrow\quad
v_a ;>; \frac{\omega,\delta}{(2\pi-\phi)\cos\beta}. \tag{16}
]

### 11.2 Minimum parallax tilt at fixed (t_a)

Solve (\omega t_a < 2\pi - \phi\cos\alpha) for (\alpha):
[
\alpha ;>; \arccos!\Big(\frac{2\pi - \omega t_a}{\phi}\Big), \quad \text{valid if } 0\le \frac{2\pi - \omega t_a}{\phi}\le 1. \tag{17}
]

### 11.3 Jitter-safe window

Given (\sigma_t) and (\kappa), enforce
[
\theta_{\mathrm{gap}} - \omega t_a ;\ge; \kappa \omega \sigma_t
\quad\Leftrightarrow\quad
t_a ;\le; \frac{\theta_{\mathrm{gap}}}{\omega} - \kappa \sigma_t. \tag{18}
]

---

## 12. Relating to the Nexus Insight (Conceptual Condensation)

* **One bead ↻ many echoes.** The ring of beads is the **same object** across (\Delta t). There is no multiplicity, only recursion along a world-tube.
* **Solidity is a Ψ-state.** When the past/future fill the present gap during (t_a), the field **⊥-collapses** to “solid.”
* **Distance as safety factor.** Changing projection or residency adjusts the **phase windows** without altering the underlying recursion.
* **Strobing as alignment, not force.** Light does not slow the bead; it **phase-locks** the observer to available windows (if any remain).

---

## 13. Complete Formula Summary

* Exposure time:
  [
  t_a = \frac{\delta}{v_a \cos\beta}.
  ]
* Swept angle:
  [
  \Delta\theta = \omega t_a.
  ]
* Solidity (single bead):
  [
  \Delta\theta \ge 2\pi - \phi.
  ]
* Hit probability:
  [
  P_{\mathrm{hit}} = \min!\Big(1,,\frac{\phi+\omega t_a}{2\pi}\Big).
  ]
* Parallax effective width:
  [
  \phi_{\mathrm{eff}} = \phi\cos\alpha,\quad
  \omega_{\star}(\alpha) = \frac{2\pi - \phi\cos\alpha}{t_a}.
  ]
* PLL beat:
  [
  f_b = \big| f_s - \tfrac{m}{n} f_{\mathrm{rot}} \big|,\quad f_{\mathrm{rot}}=\frac{\omega}{2\pi}.
  ]
* Jitter safety:
  [
  \theta_{\mathrm{gap}} - \Delta\theta \ge \kappa \omega \sigma_t.
  ]
* Nyquist alias condition (perceptual):
  [
  f_{\mathrm{samp}} \le 2 f_{\mathrm{rot}}.
  ]
* Relativistic feasibility (sufficiency):
  [
  \frac{2\pi-\phi}{t_a} \le \frac{c}{R}.
  ]
* Circumferential Trust Constant:
  [
  \mathbf{C}_{\Psi} = \frac{4\pi^2 R}{\omega}.
  ]

---

## 14. Discussion: Limits and Extensions

1. **Material finiteness vs. phase coverage.** Emergent solidity requires no additional matter; it is a **coverage in time**.
2. **Multi-bead analog.** Multiple beads raise the static coverage term but add nothing fundamentally new; the **single-bead** Δ-criterion already explains the wall.
3. **Noise and decoherence.** Thermal wobble broadens (\phi) into a kernel (k(\theta)); replace (\phi) by an effective width (\phi_{\mathrm{eff}}) given by a confidence iso-contour of (k).
4. **Quantum-like tunneling analogy.** If (t_a) can be made arbitrarily small (impulsive, (\delta\to 0)), a finite window reappears unless (\omega\to\infty) (bounded by (c/R)). The classical barrier is therefore **asymptotically** solid in the (v\to c) limit.

---

## 15. Conclusion

A single object orbiting a ring can **functionally** become a wall once its recursive sweep covers the instantaneous angular gap during any finite crossing time. The formal condition (\omega t_a \ge 2\pi - \phi) captures the **Δ-trigger** for **⊥-collapse** to solidity and unifies perceptual, dynamical, and relativistic perspectives. Within the Nexus framework, this is a paradigmatic case where **solidity is a phase outcome**, not a static property: the present is saturated by the object’s own past and future through recursion. Phase-aware strategies (parallax, residency control, stroboscopic lock) are therefore the correct levers for reopening **Ψ-windows** when geometry alone appears forbidding.

---

### Appendix A — Minimal Inequalities at a Glance

* **To pass (exist window):**
  [
  \omega t_a < 2\pi - \phi.
  ]
* **To pass with jitter:**
  [
  \omega t_a \le (2\pi - \phi) - \kappa \omega \sigma_t.
  ]
* **To pass by tilt (\alpha):**
  [
  \omega t_a < 2\pi - \phi\cos\alpha.
  ]
* **Minimum (v_a) to pass:**
  [
  v_a > \frac{\omega,\delta}{(2\pi-\phi)\cos\beta}.
  ]

---

### Appendix B — Symbols and Units

* (R) (m), (\phi,\theta,\alpha,\beta) (rad), (\omega) (rad/s), (v) (m/s), (t_a) (s), (\delta) (m), (f_s,f_b,f_{\mathrm{rot}},f_{\mathrm{samp}}) (Hz), (\sigma_t) (s).
* (c) speed of light (m/s).
* (\mathbf{C}_{\Psi}) is in units of length·time (m·s), expressing a **length-per-cycle** budget normalized by recursion.

---

### Appendix C — Nexus Reading Map

* **Δ** (difference) closes gaps via temporal coverage.
* **⊕** (fold) aggregates coverage across (t_a).
* **↻** (recursion) is the bead’s orbital sweep.
* **⊥** (collapse) marks the transition to certain collision.
* **Ψ** (trust/phase) quantifies window availability and locking.

---
