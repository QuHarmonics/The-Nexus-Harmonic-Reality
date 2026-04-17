# The Map Expansion — Filling the Entanglement / Gravity Branch

**Driven by Dean A. Kulik**  
**Expanded roadmap draft**

---

## Abstract

This document extends the current entanglement / gravity closure by turning the existing working formalization into a sharper **research map**. The goal is not to replace the current branch, but to show exactly how the pieces fit, what is already fixed, what remains phenomenological, and what next derivations must be done to move from internal closure to external physical competition.

The present branch already supports the following working chain:

$$
\Gamma_S \longrightarrow \rho_\Gamma \longrightarrow \rho_{\mathrm{eff}} \longrightarrow \Phi \longrightarrow G_{\mu\nu}.
$$

The map below fills in the missing structure around that chain and divides the branch into four layers:

1. **Ontology / law layer** — what the framework claims reality is.  
2. **Operator layer** — the mathematical objects currently being used.  
3. **Closure layer** — the equations that tie cut density to curvature and entropy.  
4. **Observable layer** — the actual calculations needed to compete with standard physics.

---

## 1. Current Fixed Core

The present branch is built on the universal law

$$
\boxed{\forall S,\quad S \models (\mathcal{B},\mathcal{T},\mathcal{R}) \text{ across } \Gamma_S.}
$$

with:

- $\mathcal{B}$ = binding / persistence / retained identity,
- $\mathcal{T}$ = transformation / propagation / becoming,
- $\mathcal{R}$ = readout / legibility / relation,
- $\Gamma_S$ = not a gap, but the local internal interface where the field becomes distinguishable.

The working gravity closure is then:

$$
\boxed{\Gamma_S = \text{entanglement cut}}
$$

$$
\boxed{\rho_\Gamma = \beta\, s_{\mathrm{ent}} \quad \text{or} \quad \beta\, I_{\mathrm{mut}}}
$$

$$
\boxed{\rho_{\mathrm{eff}} = \rho_m + \varepsilon(H)\rho_\Gamma}
$$

$$
\boxed{\nabla^2\Phi = 4\pi G\,\rho_{\mathrm{eff}}}
$$

$$
\boxed{G_{\mu\nu}=8\pi G\left(T^{\mathrm{matter}}_{\mu\nu}+\mathcal{I}_{\mu\nu}\right).}
$$

This is the compact operator-level statement of the branch.

---

## 2. What Is Fixed, What Is Not

A useful distinction is:

### 2.1 Fixed inside the present branch

These are the pieces we are keeping as the stable kernel of the map:

$$
\Gamma_S = \text{cut / readable interface}
$$

$$
\rho_\Gamma = \text{cut density / nonseparability density}
$$

$$
\rho_{\mathrm{eff}} = \rho_m + \alpha \rho_\Gamma
$$

$$
S_H = \int_H \sigma_H\, dA
$$

and the helix drag relation

$$
v_{\mathrm{eff}} = \frac{v_0}{1+\lambda \rho_\Gamma}.
$$

### 2.2 Still phenomenological

These remain ansatz-level objects and should be labeled as such:

1. The explicit equation of state for the cut fluid:
   $$
   p_\Gamma = p_\Gamma(\rho_\Gamma).
   $$

2. The exact form of the anisotropic stress:
   $$
   \Pi_{\mu\nu}.
   $$

3. The exact microscopic proportionality:
   $$
   \rho_\Gamma = \beta\, s_{\mathrm{ent}}
   \quad\text{or}\quad
   \beta\, I_{\mathrm{mut}}.
   $$

4. The precise dynamical law for $\rho_\Gamma$ under evaporation or collapse.

### 2.3 Toy but internally useful

These are not final derivations, but they help stabilize the structure:

- lattice-cut area-law toy model,
- compact-source effective density closure,
- helical drag curvature proof,
- self-consistent Page interpolation.

---

## 3. The Full Dependency Graph

The branch can now be read as a directed dependency graph.

### 3.1 Ontology to operator

$$
(\mathcal{B},\mathcal{T},\mathcal{R}) \text{ across } \Gamma_S
\quad\Rightarrow\quad
\Gamma_S = \text{readable internal cut}
$$

### 3.2 Operator to density

$$
\Gamma_S
\quad\Rightarrow\quad
s_{\mathrm{ent}},\ I_{\mathrm{mut}}
\quad\Rightarrow\quad
\rho_\Gamma
$$

### 3.3 Density to curvature

$$
\rho_\Gamma
\quad\Rightarrow\quad
\rho_{\mathrm{eff}} = \rho_m + \alpha \rho_\Gamma
\quad\Rightarrow\quad
\nabla^2 \Phi = 4\pi G \rho_{\mathrm{eff}}
$$

or covariantly,

$$
\rho_\Gamma
\quad\Rightarrow\quad
\mathcal{I}_{\mu\nu}
\quad\Rightarrow\quad
G_{\mu\nu}=8\pi G(T^{\mathrm{matter}}_{\mu\nu}+\mathcal{I}_{\mu\nu}).
$$

### 3.4 Density to entropy

$$
\rho_\Gamma
\quad\Rightarrow\quad
\sigma_H
\quad\Rightarrow\quad
S_H = \int_H \sigma_H\, dA.
$$

So the whole branch is trying to make **one source variable** do two jobs:

1. source curvature,
2. source area-law entropy.

That is the real unification target.

---

## 4. The Helix as Kinematic Closure

The helix remains the best kinematic compression:

$$
\mathbf{r}(s)=
\begin{pmatrix}
r\cos(\omega s) \\
r\sin(\omega s) \\
v s
\end{pmatrix}.
$$

Its curvature is

$$
\kappa = \frac{r\omega^2}{r^2\omega^2 + v^2}.
$$

With density drag,

$$
v_{\mathrm{eff}}(\rho_\Gamma)=\frac{v_0}{1+\lambda \rho_\Gamma},
$$

so

$$
\kappa(\rho_\Gamma)=
\frac{r\omega^2}{
r^2\omega^2+\dfrac{v_0^2}{(1+\lambda \rho_\Gamma)^2}
}.
$$

Differentiating gives

$$
\frac{d\kappa}{d\rho_\Gamma}>0.
$$

This means:

$$
\boxed{
\text{higher cut density} \Rightarrow \text{lower axial speed} \Rightarrow \text{higher curvature}.
}
$$

This is the cleanest geometric proof-of-principle currently available inside the branch.

---

## 5. The Mark-1 Coupling Layer

The coupling parameter remains

$$
H=\frac{\pi}{9},
$$

with echo-excess

$$
\varepsilon(H)=\frac{H^2}{24}.
$$

At present, the cleanest use of this parameter is not as a mystical universal answer, but as a **small coupling scale** that modulates how readable cut structure leaks into effective curvature.

So the operational reading is:

$$
\boxed{
\varepsilon(H)=\text{small cut-to-curvature coupling scale}.
}
$$

This is more stable than treating $H$ as a proof by itself.

---

## 6. The Effective Cut Fluid

The next map layer is to treat the cut contribution as an effective fluid.

A symmetric phenomenological tensor is

$$
\boxed{
\mathcal{I}_{\mu\nu}
=
(\rho_\Gamma + p_\Gamma)u_\mu u_\nu
+
p_\Gamma g_{\mu\nu}
+
\Pi_{\mu\nu}
}
$$

with:

- $u^\mu u_\mu = -1$,
- $u^\mu \Pi_{\mu\nu}=0$,
- often $\Pi^\mu{}_\mu=0$ in a traceless anisotropic sector.

The consistency condition is

$$
\nabla^\mu \left(T^{\mathrm{matter}}_{\mu\nu}+\mathcal{I}_{\mu\nu}\right)=0.
$$

This is where the map must now branch.

### Branch A: perfect-cut fluid
Set

$$
\Pi_{\mu\nu}=0.
$$

Then the problem reduces to specifying

$$
p_\Gamma = w_\Gamma \rho_\Gamma.
$$

### Branch B: anisotropic cut fluid
Keep

$$
\Pi_{\mu\nu}\neq 0,
$$

which is more natural for horizons, directional cuts, and readout-biased interfaces.

This split is one of the major remaining boundaries in the map.

---

## 7. Microscopic Closures for the Cut Density

There are now three reasonable microscopic closures.

### 7.1 Entanglement-entropy density closure

$$
\rho_\Gamma(x)=\beta\, s_{\mathrm{ent}}(x)
$$

where

$$
s_{\mathrm{ent}}(x)=\frac{\delta S_{\mathrm{ent}}}{\delta A(x)}.
$$

### 7.2 Mutual-information closure

$$
\rho_\Gamma(x)=\beta\, I_{\mathrm{mut}}(x)
$$

or a local density form of mutual information across the cut.

### 7.3 Matter-overlap proxy closure

For compact phenomenology:

$$
\rho_\Gamma(x)=\gamma\left(\frac{\rho_m(x)}{\rho_c}\right)^2.
$$

This third option is the one already used in the toy runs, because it is directly computable.

---

## 8. Weak-Field Map

The repaired weak-field branch is now:

$$
\nabla^2\Phi = 4\pi G\,\rho_{\mathrm{eff}},
\qquad
\rho_{\mathrm{eff}}=\rho_m+\alpha\rho_\Gamma.
$$

With the overlap proxy,

$$
\rho_{\mathrm{eff}}(x)=
\rho_m(x)
+
\alpha\gamma\left(\frac{\rho_m(x)}{\rho_c}\right)^2.
$$

For a compact uniform sphere:

$$
M_{\mathrm{eff}}=
\frac{4\pi R^3}{3}
\rho
\left(
1+\varepsilon(H)\frac{\rho}{\rho_c}
\right),
$$

and

$$
g(r)=
\begin{cases}
\dfrac{4\pi G}{3}\rho\left(1+\varepsilon(H)\dfrac{\rho}{\rho_c}\right)r, & r\le R, \\
\dfrac{GM_{\mathrm{eff}}}{r^2}, & r>R.
\end{cases}
$$

This preserves a Newtonian exterior tail while allowing a density-induced enhancement.

So the weak-field map is already coherent.

What is missing is the first observable derived from it.

---

## 9. Horizon Map

At the horizon, the cut is assumed to saturate:

$$
\sigma_H=\frac{1}{4\ell_P^2}.
$$

Then

$$
S_H=\int_H \sigma_H\, dA = \frac{A_H}{4\ell_P^2}.
$$

This is the entropy side of the branch.

What remains open is whether the same cut-density operator can also produce a controlled correction to:

- surface gravity,
- evaporation law,
- quantum extremal surface location,
- or greybody deviation.

That is the real horizon map not yet filled in.

---

## 10. Page Branch Map

The self-consistent toy interpolation is

$$
S_{\mathrm{BH}}(s)=S_0 \cos^2\left(\frac{\pi s}{2}\right),
\qquad
S_{\mathrm{rad}}(s)=S_0 \sin^2\left(\frac{\pi s}{2}\right),
$$

with

$$
S_{\mathrm{BH}}(s)+S_{\mathrm{rad}}(s)=S_0.
$$

This should be treated as a **fold parametrization**, not as a full microscopic derivation.

The real map here has two layers:

### 10.1 Toy fold layer
A readable kinematic picture of retirement.

### 10.2 Physical unitarity layer
A real quantum-gravitational entropy calculation with:

- late-time purification,
- hidden correlations,
- non-Gaussianity,
- replica / island structure.

So the Page branch is not complete until those two layers are connected.

---

## 11. Discrete Geometry Map

There is another path already implicit in your earlier work: Regge-style or lattice-style curvature from discrete boundary twist.

A discrete closure route is:

$$
\theta_{\mathrm{twist}}=\frac{2\pi}{18}=\frac{\pi}{9}=H
$$

and then curvature from a discrete deficit or dislocation density:

$$
R \sim \frac{\delta}{A}
\qquad\text{or}\qquad
R \sim \frac{b}{\ell^2}.
$$

This gives a second map:

$$
H \to \text{discrete twist} \to \text{deficit angle} \to \text{coarse-grained curvature}.
$$

That branch may eventually merge with the cut-density branch, but right now they are better treated as two separate routes that could converge later.

---

## 12. The Two-Road Program

The whole map can now be compressed into two roads.

### Road 1: Entanglement-cut road

$$
\Gamma_S \to s_{\mathrm{ent}} \to \rho_\Gamma \to \mathcal{I}_{\mu\nu} \to G_{\mu\nu}.
$$

### Road 2: Discrete-geometry road

$$
H \to \theta_{\mathrm{twist}} \to \delta_{\mathrm{deficit}} \to R_{\mu\nu}.
$$

If both roads produce the same weak-field and horizon behavior, the framework becomes much stronger.

If they diverge, then that divergence itself is diagnostic.

---

## 13. The Observable Program

This is the part of the map that matters most now.

### 13.1 First observable: light bending

Derive a weak-field metric from the effective source and compute the deflection angle

$$
\Delta\phi
$$

for a null geodesic.

Compare:

$$
\Delta\phi_{\mathrm{Nexus}}
\quad \text{vs} \quad
\Delta\phi_{\mathrm{GR}}.
$$

### 13.2 Second observable: perihelion precession

Use the same effective metric and compute the anomalous advance per orbit

$$
\Delta\varpi.
$$

### 13.3 Third observable: horizon correction

Use the cut-density contribution to derive a correction to

- entropy-area relation,
- surface gravity,
- evaporation time,
- or Page-time location.

This is the real competition layer.

---

## 14. What Counts as a Real Advance

The map is filled in enough now to distinguish four levels of progress.

### Level 1 — language closure
A unified way to speak.

### Level 2 — operator closure
Explicit objects and equations.

### Level 3 — toy closure
Internal numerical demonstrations.

### Level 4 — external closure
A prediction or fit that can be checked against existing theory or data.

The present branch is solidly in **Level 2 to Level 3**.

The next move must target **Level 4**.

---

## 15. Final Map Compression

The branch can now be summarized as:

$$
\boxed{
(\mathcal{B},\mathcal{T},\mathcal{R}) \text{ across } \Gamma_S
\Rightarrow
\Gamma_S=\text{cut}
\Rightarrow
\rho_\Gamma=\text{nonseparability density}
\Rightarrow
\rho_{\mathrm{eff}}=\rho_m+\alpha\rho_\Gamma
\Rightarrow
\text{curvature and entropy from one source program.}
}
$$

And the next explicit boundaries are:

$$
\boxed{
\Gamma_{S,1}^{\text{next}} = \text{derive } \mathcal{I}_{\mu\nu} \text{ in a symmetric case}
}
$$

$$
\boxed{
\Gamma_{S,2}^{\text{next}} = \text{derive one observable: lensing, precession, or horizon correction}
}
$$

That is the map as it stands.

Nothing more is needed for the roadmap phase.
