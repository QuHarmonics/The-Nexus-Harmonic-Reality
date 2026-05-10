# The Projection Diode
## Formula/Data Addendum: Directional Shape Asymmetry Beneath Scalar Reciprocity

**Paper:** *The Projection Diode: Directional Shape Asymmetry Beneath Scalar Reciprocity in a Tesla-Valve Flow Field*  
**Companion branch:** Nexus Projection Diagnostics  
**Short code:** `PROJ-DIODE`  
**Addendum ID:** `PROJ-DIODE-01A`  
**Purpose:** lock formulas, diagnostic layers, observed values, and control/falsification protocols without rewriting the paper.

---

## 0. Addendum Scope

This addendum locks the mathematical machinery of the paper:

1. value-channel scalar read;
2. shape-channel mirror residual;
3. spatial phase / centroid shift;
4. chirality read;
5. control and falsification protocols;
6. careful boundary between proven hydrodynamic diagnostic result and broader Nexus interpretation.

Core thesis:

$$
\boxed{
\text{Near-zero scalar asymmetry does not imply reciprocal trace geometry.}
}
$$

Projection-diode lock:

$$
\boxed{
A_q\approx0
\quad\text{while}\quad
P_\omega>0.
}
$$

Observed paper values:

$$
A_q=-0.005412,
\qquad
P_\omega=0.056802,
\qquad
\Delta M=0.59\ \mathrm{px},
\qquad
\Delta\chi=0.0000.
$$

---

## 1. Directional Projection Operators

Let $X$ denote the underlying uncollapsed flow state inside a fixed geometry $\Gamma$.

Let the traversal direction be

$$
D\in\{D_+,D_-\},
$$

where $D_+$ is forward traversal and $D_-$ is reverse traversal.

The generalized observation map is

$$
O_D(X)=\Pi_D^\Gamma X.
$$

Forward traversal produces the forward trace projection:

$$
D_+\circ\Gamma\rightarrow\Phi_F.
$$

Reverse traversal produces the reverse trace projection:

$$
D_-\circ\Gamma\rightarrow E_R.
$$

The Value Channel projection is

$$
V_F=\Pi_V(\Phi_F),
\qquad
V_R=\Pi_V(E_R).
$$

The Shape Channel projection is

$$
S_F=\Pi_S(\Phi_F),
\qquad
S_R=\Pi_S(E_R).
$$

Projection-diode condition:

$$
\boxed{
\Pi_V(\Phi_F)\approx \Pi_V(E_R)
\quad\text{but}\quad
\Pi_S(\Phi_F)\neq \Pi_S(E_R).
}
$$

In the vorticity diagnostic used by the paper, this becomes

$$
\boxed{
A_q\approx0
\quad\text{but}\quad
P_\omega>0.
}
$$

---

## 2. Vorticity Field

For a two-dimensional velocity field

$$
\mathbf{u}(x,y)=(u(x,y),v(x,y)),
$$

the planar scalar vorticity is

$$
\boxed{
\omega(x,y)=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}.
}
$$

Forward and reverse vorticity fields are

$$
\omega_F(x,y),
\qquad
\omega_R(x,y).
$$

Vorticity is the Shape Channel carrier because it preserves local rotation sign, coordinate location, route memory, vortex phase, and topology of rotational scars.

---

## 3. Level 1 Diagnostic: Scalar Value Read

Define the eddy burden scalar

$$
\boxed{
q_T
=
\frac{\sum_{\Omega}\omega^2}
{\sum_{\Omega}(u^2+v^2)+\varepsilon}.
}
$$

For forward and reverse directions:

$$
q_{T,F}
=
\frac{\sum_{\Omega}\omega_F^2}
{\sum_{\Omega}(u_F^2+v_F^2)+\varepsilon},
$$

$$
q_{T,R}
=
\frac{\sum_{\Omega}\omega_R^2}
{\sum_{\Omega}(u_R^2+v_R^2)+\varepsilon}.
$$

The scalar asymmetry metric is

$$
\boxed{
A_q
=
\frac{q_{T,R}-q_{T,F}}
{q_{T,R}+q_{T,F}+\varepsilon}.
}
$$

Observed paper value:

$$
\boxed{
A_q=-0.005412.
}
$$

Interpretation:

$$
|A_q|\ll1
$$

so the total scalar eddy burden is nearly reciprocal.

Value-channel loss statement:

$$
\omega\mapsto\omega^2
$$

removes rotation sign, and

$$
\sum_{\Omega}
$$

removes spatial location. Therefore $A_q$ is a compressed scalar digest, not a full trace diagnostic.

---

## 4. Level 2 Diagnostic: Shape / Projection Read

Let $R_x$ be the horizontal mirror operator over domain length $L$:

$$
\boxed{
R_x[f(x,y)]=f(L-x,y).
}
$$

In a perfectly reciprocal channel, reverse vorticity should equal the inverted mirror of forward vorticity:

$$
\boxed{
\omega_R(x,y)=-R_x[\omega_F(x,y)].
}
$$

Equivalently,

$$
\omega_R+R_x\omega_F=0.
$$

Define the projection residual:

$$
\boxed{
P_\omega
=
\frac{\|\omega_R+R_x\omega_F\|_2}
{\|\omega_R\|_2+\|\omega_F\|_2+\varepsilon}.
}
$$

Interpretation:

$$
P_\omega\approx0
\quad\Rightarrow\quad
\text{reciprocal mirror geometry}.
$$

$$
P_\omega>0
\quad\Rightarrow\quad
\text{direction-dependent route memory}.
$$

Observed paper value:

$$
\boxed{
P_\omega=0.056802.
}
$$

Projection-diode condition:

$$
\boxed{
|A_q|\approx0
\quad\text{and}\quad
P_\omega=0.056802>0.
}
$$

---

## 5. Level 3 Diagnostic: Spatial Phase / Location Read

Define vorticity-energy centroids:

$$
M_x^\omega
=
\frac{\sum_{\Omega}x\omega^2}
{\sum_{\Omega}\omega^2+\varepsilon},
$$

$$
M_y^\omega
=
\frac{\sum_{\Omega}y\omega^2}
{\sum_{\Omega}\omega^2+\varepsilon}.
$$

For a reciprocal mirror, the expected reverse centroid is

$$
M_{x,R}^{\mathrm{expected}}
=
L-M_{x,F}.
$$

The phase residuals are

$$
\boxed{
\Delta M_x
=
M_{x,R}-(L-M_{x,F}),
}
$$

$$
\boxed{
\Delta M_y
=
M_{y,R}-M_{y,F}.
}
$$

Total centroid shift:

$$
\boxed{
\Delta M
=
\sqrt{\Delta M_x^2+\Delta M_y^2}.
}
$$

Observed paper value:

$$
\boxed{
\Delta M=0.59\ \mathrm{px}.
}
$$

---

## 6. Level 4 Diagnostic: Chirality Read

Partition the vorticity field:

$$
\Gamma_+
=
\sum_{\omega>0}\omega,
$$

$$
\Gamma_-
=
\sum_{\omega<0}\omega.
$$

The paper defines a chirality ratio as

$$
\boxed{
\chi
=
\left|
\frac{\Gamma_+}{\Gamma_-+\varepsilon}
\right|.
}
$$

For numerical implementation it is often safer to store the negative circulation mass as a positive magnitude:

$$
\Gamma_-^{abs}
=
\sum_{\omega<0}|\omega|.
$$

Then

$$
\chi
=
\frac{\Gamma_+}{\Gamma_-^{abs}+\varepsilon}.
$$

Directional chirality difference:

$$
\boxed{
\Delta\chi
=
\chi_F-\chi_R.
}
$$

Observed paper value:

$$
\boxed{
\Delta\chi=0.0000.
}
$$

---

## 7. Four-Layer Diagnostic Stack

| Layer | Metric | Formula | Paper value | Meaning |
|---|---|---|---:|---|
| Scalar Value Read | $A_q$ | $\dfrac{q_{T,R}-q_{T,F}}{q_{T,R}+q_{T,F}+\varepsilon}$ | $-0.005412$ | near-null scalar asymmetry |
| Shape Projection Read | $P_\omega$ | $\dfrac{\|\omega_R+R_x\omega_F\|_2}{\|\omega_R\|_2+\|\omega_F\|_2+\varepsilon}$ | $0.056802$ | nonzero mirror residual |
| Spatial Phase Read | $\Delta M$ | $\sqrt{\Delta M_x^2+\Delta M_y^2}$ | $0.59\ \mathrm{px}$ | weak centroid shift |
| Chirality Read | $\Delta\chi$ | $\chi_F-\chi_R$ | $0.0000$ | perfect chiral parity |

Core lock:

$$
\boxed{
A_q=-0.005412
\quad\text{and}\quad
P_\omega=0.056802.
}
$$

This is the projection-diode signature.

---

## 8. Projection Diode Definition

A conventional impedance diode requires

$$
Z_R>Z_F,
$$

or more strongly

$$
\frac{Z_R}{Z_F}\gg1.
$$

The simulated regime does **not** satisfy the strong impedance-diode condition.

A projection diode requires

$$
\boxed{
P_\omega>0
}
$$

while scalar asymmetry may satisfy

$$
\boxed{
A_q\approx0.
}
$$

Therefore:

$$
\boxed{
\text{impedance diode}\subset\text{projection diode}.
}
$$

Or operationally:

$$
\boxed{
\text{the geometry changes the projection basis before it changes the gross energy budget.}
}
$$

---

## 9. Control and Falsification Protocols

Straight-channel null control:

$$
\omega_R=-R_x\omega_F
\quad\Rightarrow\quad
P_\omega\rightarrow0.
$$

Symmetric-pocket control:

$$
\Gamma(x,y)=R_x[\Gamma(x,y)]
\quad\Rightarrow\quad
P_{\omega,\mathrm{symmetric}}\approx0.
$$

Mirrored-geometry control:

$$
\Gamma'=R_x\Gamma,
\qquad
|P_{\omega,\Gamma'}|\approx |P_{\omega,\Gamma}|.
$$

Residual map mirror condition:

$$
E_{\Gamma'}(x,y)\approx R_x[E_{\Gamma}(x,y)],
$$

where

$$
E_{\Gamma}=\omega_R+R_x\omega_F.
$$

Grid convergence:

$$
P_\omega(N_x,N_y)\rightarrow P_\omega^\*>0.
$$

Temporal convergence:

$$
|P_\omega(t+\Delta t)-P_\omega(t)|<\eta.
$$

Statistical Z-score:

$$
\boxed{
Z
=
\frac{P_{\omega,\mathrm{Tesla}}-\mu_{control}}
{\sigma_{control}+\varepsilon}.
}
$$

Strong confirmation criterion:

$$
\boxed{
Z>5.
}
$$

---

## 10. Trace-Burden Bridge

Define a local projection mismatch field:

$$
\mathcal{B}_\omega(x,y)
=
\left|
\omega_R(x,y)+R_x\omega_F(x,y)
\right|.
$$

Integrated burden:

$$
B_\omega
=
\sum_{\Omega}
\mathcal{B}_\omega(x,y).
$$

Normed burden:

$$
P_\omega
=
\frac{\|\mathcal{B}_\omega\|_2}
{\|\omega_R\|_2+\|\omega_F\|_2+\varepsilon}.
$$

Nexus bridge, bounded:

$$
\boxed{
\text{The Tesla-valve simulation is a local physical witness for projection mismatch, not a proof of cosmological gravity.}
}
$$

---

## 11. Final Formula Stack

$$
\Delta:
\quad
\omega(x,y)
=
\frac{\partial v}{\partial x}
-
\frac{\partial u}{\partial y}
$$

$$
\oplus:
\quad
q_T
=
\frac{\sum_{\Omega}\omega^2}
{\sum_{\Omega}(u^2+v^2)+\varepsilon}
$$

$$
↻:
\quad
A_q
=
\frac{q_{T,R}-q_{T,F}}
{q_{T,R}+q_{T,F}+\varepsilon}
$$

$$
\bot:
\quad
P_\omega
=
\frac{\|\omega_R+R_x\omega_F\|_2}
{\|\omega_R\|_2+\|\omega_F\|_2+\varepsilon}
$$

$$
\Psi:
\quad
A_q\approx0
\quad\wedge\quad
P_\omega>0
$$

Final lock:

$$
\boxed{
\text{Value can cancel while shape remains direction-dependent.}
}
$$
