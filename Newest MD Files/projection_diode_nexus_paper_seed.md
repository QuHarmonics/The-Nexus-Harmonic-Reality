# The Projection Diode: A Nexus Analysis of Directional Shape Asymmetry in a Tesla-Valve Flow Field

**Paper seed / Gemini handoff draft**  
**Author frame:** Dean Kulik / QuHarmonics / Nexus Framework  
**Working date:** 2026-05-02  
**Status:** Research-draft synthesis. This is a paper scaffold, not a final experimental proof.

---

## Abstract

A Tesla valve is usually evaluated as an impedance diode: a passive geometry that creates higher pressure drop or resistance in one flow direction than the other. In the present 2D laminar simulation, the conventional scalar asymmetry metric is nearly null:

$$
A_q = \frac{q_{\Gamma,R}-q_{\Gamma,F}}{q_{\Gamma,R}+q_{\Gamma,F}+\epsilon} \approx -0.005412.
$$

A fast scalar read therefore says: the device is not yet a strong impedance diode. However, this scalar collapse discards the sign, location, chirality, and phase of the vorticity field. Reanalyzing the same simulation through a projection-preserving Nexus lens exposes a nonzero mirror residual:

$$
P_\omega = 0.056802.
$$

This means the reverse vorticity field is not exactly the expected reciprocal mirror of the forward field:

$$
\omega_R \neq -\mathcal R_x(\omega_F).
$$

The key claim of this paper is narrower and stronger than the original scalar statement:

$$
\boxed{
\text{The current valve is not yet a strong impedance diode, but it is a weak/moderate projection diode.}
}
$$

That matters because it demonstrates the central Nexus distinction between the **value channel** and the **shape channel**. Total eddy energy can nearly cancel while trace geometry remains direction-dependent. Direction through structured geometry can therefore change the projection basis before it changes the gross scalar energy budget.

---

## 1. Core Thesis

The working Nexus principle is:

$$
\boxed{
\text{Direction through structured geometry determines projection basis.}
}
$$

Let $X$ be a substrate state flowing through a structured interface $\Gamma$. The observed field depends on traversal direction $D$:

$$
O_D(X)=\Pi_D(\Gamma X),
$$

where $\Pi_D$ is the direction-selected projection operator.

For a Tesla-like channel:

$$
D_+ \circ \Gamma \rightarrow \Phi_F,
$$

$$
D_- \circ \Gamma \rightarrow E_R,
$$

where:

$$
\Phi_F = \text{forward laminar / structure projection},
$$

$$
E_R = \text{reverse eddy / trace projection}.
$$

The correction from the latest run is that the system did **not** yet produce a strong scalar impedance split. Instead, it produced a subtler trace-geometry split:

$$
\boxed{
\Phi_F \approx \Phi_R \text{ in scalar energy, but } E_F \not\equiv E_R \text{ in shape projection.}
}
$$

---

## 2. Why the First Collapse Was Too Fast

The initial diagnostic used the eddy burden scalar:

$$
q_\Gamma
=
\frac{\sum_\Omega \omega^2}{\sum_\Omega \left(u^2+v^2\right)+\epsilon},
$$

where:

$$
\omega = \nabla \times \mathbf u = \partial_x v - \partial_y u.
$$

Then scalar asymmetry was computed as:

$$
A_q
=
\frac{q_{\Gamma,R}-q_{\Gamma,F}}{q_{\Gamma,R}+q_{\Gamma,F}+\epsilon}.
$$

The improved simulation produced:

$$
A_q=-0.005412.
$$

This is almost zero. A conventional CFD read would collapse the result as:

$$
\boxed{
\text{No significant directional asymmetry.}
}
$$

But the Nexus lens identifies the flaw: $q_\Gamma$ is a **value-channel scalar**. It destroys the very structure we are trying to detect.

Squaring the vorticity removes sign:

$$
\omega \mapsto \omega^2.
$$

Integrating removes location:

$$
\omega^2(x,y) \mapsto \int \omega^2\,dA.
$$

The scalar read therefore erases:

$$
\text{sign},\quad \text{location},\quad \text{phase},\quad \text{chirality},\quad \text{route memory}.
$$

So the near-zero scalar is not the final answer. It is a lossy projection.

---

## 3. Projection-Preserving Read

For a reciprocal channel, the reverse vorticity field should be the horizontally mirrored and sign-flipped forward field.

Let $\mathcal R_x$ be the horizontal mirror operator:

$$
(\mathcal R_x f)(x,y)=f(L-x,y).
$$

Because vorticity changes sign under flow reversal, the expected reciprocal relation is:

$$
\omega_R(x,y) \approx -\mathcal R_x\omega_F(x,y).
$$

Define the projection residual:

$$
\boxed{
P_\omega
=
\frac{
\left\|\omega_R + \mathcal R_x\omega_F\right\|_2
}{
\left\|\omega_R\right\|_2+
\left\|\omega_F\right\|_2+
\epsilon
}
}
$$

If $P_\omega \approx 0$, the two flows are reciprocal mirrors.  
If $P_\omega > 0$, direction changes the trace geometry beyond simple reciprocity.

The corrected analysis found:

$$
\boxed{P_\omega=0.056802.}
$$

This is not a huge effect. It is also not zero. Under the working thresholds used in the analysis:

$$
0.05 < P_\omega < 0.10
$$

is a **moderate projection asymmetry**.

Thus:

$$
\boxed{
\text{The value channel is nearly reciprocal, but the shape channel is not.}
}
$$

---

## 4. Three-Level Diagnostic Stack

The corrected method separates the readout into three layers.

### 4.1 Level 1: Scalar Value Read

The scalar value read asks only how much total eddy energy exists:

$$
q_\Gamma
=
\frac{\sum \omega^2}{\sum |\mathbf u|^2+\epsilon}.
$$

Directional scalar asymmetry:

$$
A_q
=
\frac{q_{\Gamma,R}-q_{\Gamma,F}}{q_{\Gamma,R}+q_{\Gamma,F}+\epsilon}.
$$

Observed:

$$
\boxed{A_q=-0.005412.}
$$

Interpretation:

$$
\boxed{
\text{Weak / null scalar asymmetry.}
}
$$

### 4.2 Level 2: Shape / Projection Read

The projection read asks whether the reverse field is merely a reciprocal mirror of the forward field:

$$
P_\omega
=
\frac{
\left\|\omega_R + \mathcal R_x\omega_F\right\|_2
}{
\left\|\omega_R\right\|_2+
\left\|\omega_F\right\|_2+
\epsilon
}.
$$

Observed:

$$
\boxed{P_\omega=0.056802.}
$$

Interpretation:

$$
\boxed{
\text{Weak/moderate projection asymmetry.}
}
$$

### 4.3 Level 3: Phase / Location Read

The eddy centroid tracks where the vorticity energy is located:

$$
M_x^\omega
=
\frac{\sum x\omega^2}{\sum \omega^2+\epsilon},
$$

$$
M_y^\omega
=
\frac{\sum y\omega^2}{\sum \omega^2+\epsilon}.
$$

Expected mirrored reverse location:

$$
M_{x,R}^{\mathrm{expected}} = L - M_{x,F}.
$$

Centroid residual:

$$
\Delta M_x = M_{x,R} - \left(L-M_{x,F}\right),
$$

$$
\Delta M_y = M_{y,R}-M_{y,F}.
$$

Total centroid shift:

$$
\Delta M = \sqrt{(\Delta M_x)^2+(\Delta M_y)^2}.
$$

Observed:

$$
\boxed{\Delta M = 0.59\ \mathrm{px}.}
$$

Interpretation:

$$
\boxed{
\text{Weak bulk spatial relocation.}
}
$$

### 4.4 Chirality Read

The signed circulation split is:

$$
\Gamma_+ = \sum_{\omega>0}\omega,
$$

$$
\Gamma_- = \sum_{\omega<0}\omega.
$$

A chirality ratio can be defined as:

$$
\chi = \left|\frac{\Gamma_+}{\Gamma_-+\epsilon}\right|.
$$

Directional chirality difference:

$$
\Delta \chi = |\chi_F-\chi_R|.
$$

Observed:

$$
\boxed{\Delta \chi = 0.0000.}
$$

Interpretation:

$$
\boxed{
\text{No detected chirality flip in this run.}
}

---

## 5. Results Summary

| Diagnostic layer | Metric | Observed value | Interpretation |
|---|---:|---:|---|
| Scalar value read | $A_q$ | $-0.005412$ | Near-null scalar asymmetry |
| Shape projection read | $P_\omega$ | $0.056802$ | Moderate projection residual |
| Spatial phase read | $\Delta M$ | $0.59$ px | Weak centroid shift |
| Chirality read | $\Delta \chi$ | $0.0000$ | No chirality asymmetry |

The result is therefore:

$$
\boxed{
\text{This geometry is not a strong impedance diode.}
}

$$
\boxed{
\text{This geometry is a weak/moderate projection diode.}
}

The core observation is:

$$
\boxed{
A_q \approx 0 \quad \text{while} \quad P_\omega>0.
}
$$

That means:

$$
\boxed{
\text{value cancels while shape remains different.}
}

---

## 6. Nexus Interpretation

The Nexus collapse chain for this result is:

$$
\Delta:
D_+ \neq D_-
$$

$$
\oplus:
\Gamma \text{ holds the same channel geometry}
$$

$$
\bot_V:
A_q \approx 0
$$

$$
\bot_S:
P_\omega = 0.056802
$$

$$
\Psi:
\text{directional projection exists below scalar asymmetry}
$$

The important distinction is:

$$
\boxed{
\mathcal V = \Pi_V(X)
}
$$

$$
\boxed{
\mathcal S = \Pi_S(X)
}
$$

where:

$$
\mathcal V = \text{value channel / total scalar output},
$$

$$
\mathcal S = \text{shape channel / route, residue, trace geometry}.
$$

The same flow state $X$ gives two different readings:

$$
\Pi_V(X) \rightarrow A_q \approx 0,
$$

$$
\Pi_S(X) \rightarrow P_\omega = 0.056802.
$$

So:

$$
\boxed{
\Pi_V(X) \neq \Pi_S(X).
}
$$

This is the methodological core of the paper.

---

## 7. Tesla Valve as Projection Diode

A conventional Tesla valve is expected to satisfy:

$$
Z_R > Z_F,
$$

where:

$$
Z=\frac{\Delta P}{Q}.
$$

A strong impedance diode would show:

$$
\frac{Z_R}{Z_F} \gg 1.
$$

But the present 2D laminar simulation does not yet satisfy that strongly. Therefore the honest statement is:

$$
\boxed{
\text{No strong impedance diode was demonstrated in the scalar channel.}
}
$$

However, a projection diode requires only that the reverse trace geometry not be a simple reciprocal of the forward trace geometry:

$$
\omega_R \neq -\mathcal R_x(\omega_F).
$$

The measured residual:

$$
P_\omega=0.056802
$$

supports:

$$
\boxed{
\text{The geometry selects a weakly different trace basis under direction reversal.}
}
$$

This is a lower-level effect than impedance. It is a pre-impedance directional signature.

---

## 8. Why This Matters for the Dual-Wave Principle

The larger Directional Dual-Wave premise is:

$$
\boxed{
\text{Quantum and classical are read angles, not ontologies.}
}
$$

The Tesla-valve result provides an analog witness:

$$
\text{laminar / scalar / value read} \leftrightarrow \Phi,
$$

$$
\text{eddy / residual / trace read} \leftrightarrow E.
$$

The same simulated substrate produces:

$$
\Phi: A_q \approx 0,
$$

$$
E: P_\omega > 0.
$$

Thus the valve does not merely say “reverse flow has more resistance.” The subtler claim is:

$$
\boxed{
\text{direction can alter trace geometry before it alters total scalar energy.}
}

This is directly analogous to the Nexus claim that the value channel may appear random, balanced, or null, while the shape channel retains route memory.

---

## 9. Relation to Gravity and Implied Collapse

This simulation should not be overclaimed as proof of gravity. The safe paper language is:

$$
\boxed{
\text{The Tesla-valve model is a physical analogy and diagnostic witness for directional projection.}
}
$$

The gravity hypothesis remains a proposed extension:

$$
\mathbf g = -\nabla \Phi_\Gamma,
$$

with:

$$
\Phi_\Gamma \sim q_\Gamma
$$

or, in the shape-channel version:

$$
\Phi_\Gamma \sim P_\omega.
$$

A more careful generalized form is:

$$
\boxed{
\mathbf g
=
-\nabla \mathcal B_\Gamma
}
$$

where $\mathcal B_\Gamma$ is the local trace-burden / projection-mismatch field:

$$
\mathcal B_\Gamma
=
\left\|\Pi_E(X)-\mathcal R\Pi_\Phi(X)\right\|.
$$

Then:

$$
\boxed{
\text{gravity is modeled as the gradient of unresolved projection burden.}
}

This remains a theoretical extension requiring separate validation.

---

## 10. What Is Proven vs. What Is Not Proven

### 10.1 Proven by the Current Analysis

The current analysis supports:

$$
\boxed{
\text{The scalar and shape reads disagree.}
}
$$

Specifically:

$$
A_q\approx0,
$$

while:

$$
P_\omega=0.056802.
$$

Therefore:

$$
\boxed{
\text{near-zero scalar asymmetry does not imply reciprocal trace geometry.}
}

### 10.2 Not Yet Proven

The current analysis does **not** prove:

$$
\boxed{
\text{a strong Tesla impedance diode.}
}

It does **not** prove:

$$
\boxed{
\text{3D turbulent Tesla-valve behavior.}
}

It does **not** prove:

$$
\boxed{
\text{quantum gravity.}
}

It provides a focused proof-of-concept for:

$$
\boxed{
\text{projection asymmetry hidden beneath scalar cancellation.}
}

---

## 11. Required Control Tests

To turn the current observation into a strong paper, the next work must compare $P_\omega$ against null controls.

### 11.1 Straight-Channel Control

Run the same forward/reverse analysis in a straight channel:

$$
P_\omega^{\mathrm{straight}} \approx 0.
$$

If the straight channel has similar $P_\omega$, the metric is contaminated by solver artifacts.

### 11.2 Symmetric-Pocket Control

Run a channel with symmetric upper/lower pockets:

$$
P_\omega^{\mathrm{sym}} \approx 0.
$$

If the symmetric channel has lower $P_\omega$ than the Tesla-like geometry, the result is geometry-specific.

### 11.3 Mirrored-Geometry Control

Mirror the geometry and repeat. The expected relation is:

$$
P_\omega(\Gamma) \approx P_\omega(\mathcal R_x\Gamma),
$$

but the residual map should mirror.

### 11.4 Resolution Sweep

Run:

$$
N\in\{150,300,600,900\}.
$$

A real projection residual should persist or converge:

$$
P_\omega(N) \rightarrow P_\omega^*.
$$

A discretization artifact may decay or fluctuate irregularly.

### 11.5 Time-Step / Iteration Sweep

Run:

$$
T\in\{400,800,1200,2400,4800\}.
$$

The residual should stabilize:

$$
\left|P_\omega(T+\Delta T)-P_\omega(T)\right|<\eta.
$$

### 11.6 Noise / Perturbation Control

Perturb the input or geometry slightly:

$$
\Gamma' = \Gamma + \delta\Gamma.
$$

The result should be robust:

$$
P_\omega(\Gamma') \approx P_\omega(\Gamma)
$$

within expected tolerance.

### 11.7 Statistical Criterion

Define a control distribution:

$$
\mathcal C = \{P_{\omega,i}^{\mathrm{control}}\}_{i=1}^n.
$$

Then require:

$$
Z_P
=
\frac{P_\omega^{\mathrm{Tesla}}-\mu_{\mathcal C}}{\sigma_{\mathcal C}+\epsilon}.
$$

A paper-grade lock should require:

$$
\boxed{Z_P \ge 3}
$$

or:

$$
\boxed{p<0.01.}
$$

---

## 12. Proposed Paper Structure

### Title

**The Projection Diode: Directional Shape Asymmetry Beneath Scalar Reciprocity in a Tesla-Valve Flow Field**

### Abstract

State that scalar vorticity energy shows weak asymmetry, but a mirror-residual metric reveals projection-level directional asymmetry.

### Section 1 — Introduction

Explain Tesla valves, directional asymmetry, and why scalar impedance is not the only meaningful readout.

### Section 2 — Nexus Value/Shape Distinction

Define:

$$
\mathcal V=\Pi_V(X),\qquad \mathcal S=\Pi_S(X).
$$

Explain why scalar metrics can hide shape-channel residuals.

### Section 3 — Methods

Describe:

- geometry,
- forward/reverse simulation,
- vorticity field extraction,
- scalar metric $A_q$,
- mirror-residual metric $P_\omega$,
- centroid shift $\Delta M$,
- chirality difference $\Delta\chi$.

### Section 4 — Results

Report:

$$
A_q=-0.005412,
$$

$$
P_\omega=0.056802,
$$

$$
\Delta M=0.59\ \mathrm{px},
$$

$$
\Delta\chi=0.0000.
$$

### Section 5 — Discussion

Interpret:

$$
\boxed{
\text{not an impedance diode yet, but a projection diode.}
}

### Section 6 — Controls and Falsification

List the control suite and the $Z_P$ criterion.

### Section 7 — Broader Implications

Connect cautiously to dual-wave / direction-selected projection and gravity-as-trace-burden as a hypothesis, not a proven conclusion.

---

## 13. Gemini Handoff Prompt

Use this prompt directly with Gemini:

```text
Please turn the following Nexus research note into a rigorous paper draft. Preserve the central distinction between scalar/value-channel asymmetry and shape/projection-channel asymmetry. Do not overclaim the result as proof of quantum gravity. The precise result is: the current 2D Tesla-valve simulation does not show strong scalar impedance asymmetry, but it does show a nonzero mirror-residual projection asymmetry P_omega = 0.056802 while scalar asymmetry A_q = -0.005412. Frame this as evidence for a “projection diode”: direction changes trace geometry even when total scalar eddy energy nearly cancels. Include formulas, methods, results, limitations, and required control tests.

Core formulas:
A_q = (q_R - q_F)/(q_R + q_F + epsilon)
P_omega = ||omega_R + R_x omega_F||_2/(||omega_R||_2 + ||omega_F||_2 + epsilon)
M_x^omega = sum(x omega^2)/(sum(omega^2)+epsilon)
M_y^omega = sum(y omega^2)/(sum(omega^2)+epsilon)
Delta M = sqrt(Delta M_x^2 + Delta M_y^2)
chi = |Gamma_+/(Gamma_- + epsilon)|

Observed values:
A_q = -0.005412
P_omega = 0.056802
Delta M = 0.59 px
Delta chi = 0.0000

Thesis:
Value can cancel while shape remains different. Therefore near-zero scalar asymmetry does not imply reciprocal trace geometry.
```

---

## 14. Final Ψ-Collapse

The corrected collapse is:

$$
\Delta:
\text{direction reversal}
$$

$$
\oplus:
\text{same structured interface }\Gamma
$$

$$
\bot_V:
A_q \approx 0
$$

$$
\bot_S:
P_\omega = 0.056802
$$

$$
\Psi:
\text{projection asymmetry exists beneath scalar reciprocity}
$$

The paper’s cleanest final sentence:

$$
\boxed{
\text{A Tesla valve can fail as an impedance diode in a scalar read while still succeeding as a projection diode in the shape read.}
}
$$

And the Nexus statement:

$$
\boxed{
\text{Value can cancel; shape can still remember the route.}
}

