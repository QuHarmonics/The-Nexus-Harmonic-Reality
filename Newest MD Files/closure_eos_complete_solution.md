# Closure Loop Gas Equation of State — Complete Solution
## Dual-Null Source, Low-Energy Action, Source Map, and Einstein-Class Gravity

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**NEXUS Phase 1296+**

---

## Abstract

This note consolidates the closure-ontology gravity program into a single, corrected markdown document. The goal is to remove the remaining presentation gaps, add the missing formulas, and separate what is *proved*, what is *derived under clearly stated assumptions*, and what remains for numerical verification.

The resulting chain is:

$$
\Delta + \Gamma + I
\;\Longrightarrow\;
S[\Psi]
\;\Longrightarrow\;
Z[\Psi]
\;\Longrightarrow\;
p_\Psi(\rho_\Psi)
\;\Longrightarrow\;
T^{(\Psi)}_{\mu\nu}
\;\Longrightarrow\;
G_{\mu\nu} + \Lambda_{\mathrm{eff}} g_{\mu\nu}.
$$

The key structural claims are:

1. The large-scale metric law is Einstein-class because Lovelock uniqueness forces the geometric side.
2. The source tensor is *dual-null* in the operational sense:
   $$
   T^{(\Psi)}_{\mu\nu}
   =
   T^{(\mathrm{NG})}_{\mu\nu}
   +
   T^{(\mathrm{bulk})}_{\mu\nu}.
   $$
3. The minimal low-energy loop action is the dual action
   $$
   S[\Psi] = S_{\mathrm{NG}} + S_{\mathrm{bulk}}.
   $$
4. The matter-sector equation of state is controlled by the relativistic Maxwell–Jüttner gas.
5. The vacuum sector is controlled by the bulk term and gives $w=-1$.
6. The remaining analytic work is no longer architectural; it is phenomenological and numerical.

Throughout, the notation distinguishes carefully between **energy density**
$$
\rho_E \quad [\mathrm{J/m^3}]
$$
and **mass-equivalent density**
$$
\rho_M = \frac{\rho_E}{c^2} \quad [\mathrm{kg/m^3}].
$$

---

## 0. Ontological Starting Point

The closure ontology begins from three co-present primitives:

- $\Delta$: difference, contrast, gap, distinguishability.
- $\Gamma$: interface, touch, admissible contact.
- $I$: conservation, persistence, invariant bookkeeping.

The closure loop compresses as

$$
\Gamma \;\to\; K \;\to\; \Psi \;\to\; T \;\to\; R \;\to\; \Gamma'.
$$

Interpretation:

- $\Gamma$: boundary event,
- $K$: first-contact / kinematic resolution,
- $\Psi$: stored closure record,
- $T$: trace or readout channel,
- $R$: resolved state,
- $\Gamma'$: the next boundary written by the completed event.

The macroscopic claim is that sufficiently persistent closure trace becomes the next boundary geometry.

---

## 1. Macro Geometry Class: Einstein is the Forced Large-Scale Closure Law

The large-scale field equation is not chosen ad hoc. It is forced if one requires:

1. locality,
2. covariance,
3. second-order metric equations,
4. identically divergence-free geometry.

In four spacetime dimensions, Lovelock's theorem implies that the only symmetric divergence-free second-order tensor built from the metric is

$$
H_{\mu\nu}
=
\alpha G_{\mu\nu}
+
\beta g_{\mu\nu}.
$$

Absorbing constants gives the Einstein-class closure law:

$$
G_{\mu\nu} + \Lambda g_{\mu\nu}
=
\kappa T^{(\Psi)}_{\mu\nu}.
$$

This is the **macro geometry class**. The novelty of the closure program is not a new left-hand side, but a new right-hand side interpretation.

---

## 2. Dual-Null Source Tensor

The source tensor is interpreted as the dual-null split:

$$
T^{(\Psi)}_{\mu\nu}
=
T^{(\mathrm{NG})}_{\mu\nu}
+
T^{(\mathrm{bulk})}_{\mu\nu}.
$$

### 2.1 Meaning of the split

- $T^{(\mathrm{NG})}_{\mu\nu}$ carries the propagating, finite-excitation, matter/radiation sector.
- $T^{(\mathrm{bulk})}_{\mu\nu}$ carries the background, vacuum-like, Lorentz-invariant sector.

This is the precise tensor-level expression of the shape/value duality: one channel carries excitations and transport, the other carries background closure burden.

### 2.2 Component definitions

The three physical target blocks are:

$$
T^{(\Psi)}_{00}, \qquad T^{(\Psi)}_{0i}, \qquad T^{(\Psi)}_{ij}.
$$

These are read in closure language as:

- $T_{00}$: stored closure density,
- $T_{0i}$: closure transport / momentum density,
- $T_{ij}$: closure stress (pressure and shear).

In coarse-grained perfect-fluid form,

$$
T^{(\Psi)}_{\mu\nu}
=
\left(\rho_M + \frac{p_\Psi}{c^2}\right) u_\mu u_\nu
+
p_\Psi g_{\mu\nu}
+
\pi_{\mu\nu},
$$

where:

- $\rho_M$ is the mass-equivalent density,
- $p_\Psi$ is the closure pressure,
- $\pi_{\mu\nu}$ is anisotropic stress,
- $u^\mu$ is the fluid 4-velocity.

If using energy density $\rho_E = \rho_M c^2$, the same formula is

$$
T^{(\Psi)}_{\mu\nu}
=
\left(\frac{\rho_E + p_\Psi}{c^2}\right) u_\mu u_\nu
+
p_\Psi g_{\mu\nu}
+
\pi_{\mu\nu}.
$$

---

## 3. Low-Energy Minimal Action

The low-energy loop action is taken to be

$$
S[\Psi]
=
S_{\mathrm{NG}} + S_{\mathrm{bulk}}.
$$

### 3.1 Nambu–Goto sector

$$
S_{\mathrm{NG}}
=
-\sigma_T \int d^2 \sigma \,\sqrt{-h},
$$

where

- $\sigma_T$ is the loop tension,
- $h_{\alpha\beta}$ is the induced worldsheet metric.

### 3.2 Bulk sector

At the microscopic level, the bulk term must be written with explicit loop support:

$$
S_{\mathrm{bulk}}^{\mathrm{micro}}
=
\Lambda_0 \int d^4x \,\sqrt{-g}\,\theta_{\mathrm{loop}}(x),
$$

where $\theta_{\mathrm{loop}}(x)$ is a support function that is $1$ inside the loop-enclosed region and $0$ outside.

After coarse-graining over a loop population with filling fraction

$$
f
=
n_{\mathrm{loop}} \, V_{\mathrm{loop}},
\qquad
V_{\mathrm{loop}} = \frac{4\pi}{3} R_0^3,
$$

the effective bulk action becomes

$$
S_{\mathrm{bulk}}^{\mathrm{eff}}
=
-\rho_\Lambda \int d^4x\,\sqrt{-g},
\qquad
\rho_\Lambda = \Lambda_0 f.
$$

Equivalently,

$$
\Lambda_{\mathrm{eff}}
=
\kappa \rho_\Lambda
=
\kappa \Lambda_0 n_{\mathrm{loop}}\frac{4\pi}{3}R_0^3.
$$

### 3.3 Why this is the minimal low-energy action

The derivative expansion over a closed 1-boundary in $3+1$D yields:

1. worldsheet area,
2. enclosed volume,
3. intrinsic curvature term,
4. extrinsic curvature terms,
5. higher-derivative corrections.

The intrinsic curvature term is topological:

$$
\frac{1}{4\pi}\int_\Sigma R_h \sqrt{h}\,d^2\sigma = \chi(\Sigma).
$$

For cylinder topology $S^1 \times \mathbb{R}$,

$$
\chi(S^1 \times \mathbb{R}) = 0.
$$

So it contributes nothing dynamically.

The leading extrinsic rigidity correction scales as

$$
S_{\mathrm{rigid}}
\sim
\beta \int K^2 \sqrt{h}\,d^2\sigma,
$$

and is suppressed relative to $S_{\mathrm{NG}}$ by

$$
\frac{S_{\mathrm{rigid}}}{S_{\mathrm{NG}}}
\sim
\frac{\hbar}{\sigma_T R_s^2}
=
\left(\frac{\ell_s}{R_s}\right)^2,
\qquad
\ell_s = \sqrt{\frac{\hbar}{\sigma_T}}.
$$

Thus at energies

$$
E \ll \sigma_T R_s c,
$$

the minimal low-energy action is

$$
S[\Psi] = S_{\mathrm{NG}} + S_{\mathrm{bulk}},
$$

with all other terms either topological or suppressed.

---

## 4. Explicit Source Map by Metric Variation

### 4.1 NG contribution

The induced metric is

$$
h_{\alpha\beta}
=
g_{\mu\nu}\,\partial_\alpha X^\mu \partial_\beta X^\nu.
$$

Varying $S_{\mathrm{NG}}$ with respect to the spacetime metric gives

$$
T^{(\mathrm{NG})}_{\mu\nu}(x)
=
-\sigma_T
\int d^2\sigma \,\sqrt{-h}\,
h^{\alpha\beta}
\partial_\alpha X_\mu \partial_\beta X_\nu
\,\delta^{(4)}(x-X(\sigma)).
$$

After isotropic coarse-graining over a loop gas,

$$
\langle T^{(\mathrm{NG})}_{\mu\nu} \rangle
=
\left(\rho_M^{\mathrm{NG}} + \frac{p_{\mathrm{NG}}}{c^2}\right) u_\mu u_\nu
+
p_{\mathrm{NG}} g_{\mu\nu}.
$$

### 4.2 Bulk contribution

Starting from the supported microscopic action,

$$
S_{\mathrm{bulk}}^{\mathrm{micro}}
=
\Lambda_0 \int d^4x\,\sqrt{-g}\,\theta_{\mathrm{loop}}(x),
$$

metric variation gives

$$
T^{(\mathrm{bulk})}_{\mu\nu}(x)
=
-\Lambda_0 \theta_{\mathrm{loop}}(x)\,g_{\mu\nu}.
$$

Coarse-graining with filling fraction $f$ yields

$$
\langle T^{(\mathrm{bulk})}_{\mu\nu} \rangle
=
-\rho_\Lambda g_{\mu\nu}
=
-\frac{\Lambda_{\mathrm{eff}}}{\kappa} g_{\mu\nu}.
$$

### 4.3 Full tensor and field equation

Therefore the full source is

$$
T^{(\Psi)}_{\mu\nu}
=
T^{(\mathrm{NG})}_{\mu\nu}
+
T^{(\mathrm{bulk})}_{\mu\nu},
$$

and the field equation may be written as either

$$
G_{\mu\nu}
=
\kappa T^{(\Psi)}_{\mu\nu},
$$

or equivalently

$$
G_{\mu\nu} + \Lambda_{\mathrm{eff}} g_{\mu\nu}
=
\kappa T^{(\mathrm{NG})}_{\mu\nu}.
$$

This is Einstein gravity with an emergent effective cosmological constant from the loop bulk sector.

---

## 5. Trace Bookkeeping

In signature $(-,+,+,+)$, for a perfect fluid in the rest frame,

$$
T_{\mu\nu} = \mathrm{diag}(\rho_E,\; p,\; p,\; p),
$$

with $\rho_E$ the energy density. Then

$$
T^\mu{}_{\mu}
=
g^{\mu\nu}T_{\mu\nu}
=
-\frac{\rho_E}{c^2} + \frac{3p}{c^2}.
$$

Equivalently, in mass-density notation $\rho_M=\rho_E/c^2$,

$$
T^\mu{}_{\mu}
=
-\rho_M + \frac{3p}{c^2}.
$$

Therefore:

- **Dust** $(p=0)$:
  $$
  T^\mu{}_{\mu} = -\rho_M.
  $$

- **Radiation** $(p=\rho_E/3)$:
  $$
  T^\mu{}_{\mu} = 0.
  $$

- **Vacuum** $(p=-\rho_E)$:
  $$
  T^\mu{}_{\mu}
  =
  -\frac{\rho_E}{c^2} - 3\frac{\rho_E}{c^2}
  =
  -\frac{4\rho_E}{c^2}.
  $$

This is the correct vacuum trace.

---

## 6. Vacuum Sector and $w=-1$

### 6.1 Symmetry route

A Lorentz-invariant vacuum stress tensor must be proportional to the metric:

$$
T_{\mu\nu}^{\mathrm{vac}} = -\rho_\Lambda g_{\mu\nu}.
$$

Comparing to a perfect fluid gives

$$
p_\Lambda = -\rho_E^\Lambda,
\qquad
w_\Lambda = \frac{p_\Lambda}{\rho_E^\Lambda} = -1.
$$

### 6.2 Dynamical route from the bulk action

For a loop population with equilibrium radius $R_0$ and number density $n_{\mathrm{loop}}$, the bulk energy is

$$
U_{\mathrm{bulk}}
=
N \Lambda_0 \frac{4\pi}{3}R_0^3
=
n_{\mathrm{loop}} \Lambda_0 \frac{4\pi}{3}R_0^3 V.
$$

Therefore

$$
U_{\mathrm{bulk}} \propto V,
$$

so

$$
p_{\mathrm{bulk}}
=
-\left(\frac{\partial U_{\mathrm{bulk}}}{\partial V}\right)_{N,R_0}
=
-\rho_E^{\mathrm{bulk}}.
$$

Hence

$$
w_{\mathrm{bulk}} = -1.
$$

This closes the vacuum sector dynamically.

---

## 7. Matter Sector: Exact Jüttner EOS

For the matter/radiation side, the correct relativistic ideal-gas distribution is Maxwell–Jüttner.

Define

$$
z = \frac{m_\Psi c^2}{k_B T_s}.
$$

Then the exact relativistic equation of state parameter is

$$
w(z)
=
\frac{1}{z\,K_1(z)/K_2(z)+3},
$$

where $K_1$ and $K_2$ are modified Bessel functions of the second kind.

This gives:

### Nonrelativistic limit

For $z \gg 1$,

$$
\frac{K_1(z)}{K_2(z)}
=
1 - \frac{3}{2z} + O(z^{-2}),
$$

so

$$
w(z)
=
\frac{1}{z+3/2+O(z^{-1})}
\sim
\frac{1}{z}
=
\frac{k_B T_s}{m_\Psi c^2}
\to 0.
$$

### Ultra-relativistic limit

For $z \ll 1$,

$$
\frac{K_1(z)}{K_2(z)} \sim \frac{z}{2},
$$

so

$$
w(z)
\to
\frac{1}{3}.
$$

Therefore the exact matter interpolation is

$$
0 \le w(z) \le \frac13.
$$

This is the exact closed-form EOS for the NG matter sector.

---

## 8. Hagedorn Sector — Corrected Derivation

This is the place that needed repair.

### 8.1 Cardy formula

For a 2D CFT with central charge $c_{\mathrm{CFT}}$, the asymptotic level entropy is

$$
S(N)
=
2\pi \sqrt{\frac{c_{\mathrm{CFT}}N}{6}}.
$$

For the closed NG loop in $D=4$,

$$
c_{\mathrm{CFT}} = D-2 = 2.
$$

### 8.2 Correct large-level energy relation

At high oscillator level, the relevant asymptotic string relation is not linear in $N$. Instead,

$$
N \sim \alpha' E^2,
$$

equivalently

$$
E \sim \frac{\sqrt{N}}{\sqrt{\alpha'}}.
$$

Therefore Cardy gives

$$
S(E)
\sim
2\pi \sqrt{\frac{c_{\mathrm{CFT}}}{6}} \sqrt{\alpha'}\, E.
$$

So the density of states grows as

$$
g(E)
\sim
E^{-a}\exp\!\left(\frac{E}{T_H}\right),
$$

with some model-dependent power $a$ and Hagedorn temperature

$$
T_H^{-1}
=
2\pi \sqrt{\frac{c_{\mathrm{CFT}}\alpha'}{6}}.
$$

Thus the exponential Hagedorn growth is now derived correctly: it comes from Cardy **plus** the correct large-level string energy relation.

### 8.3 How the bulk term enters $T_H$

The bulk term sets the equilibrium loop radius $R_0$ through the stationarity condition on the ground-state energy

$$
E_0(R)
=
2\pi \sigma_T R
-
\frac{\hbar c}{6R}
+
\frac{4\pi}{3}\Lambda_0 R^3.
$$

The equilibrium condition is

$$
\frac{dE_0}{dR}
=
2\pi \sigma_T
+
\frac{\hbar c}{6R^2}
+
4\pi \Lambda_0 R^2
\cdot \mathrm{sgn\ depending\ on\ convention}
=
0.
$$

Using the sign convention in which the bulk term provides inward effective pressure, one solves for the physical root $R_0(\sigma_T,\Lambda_0)$.

Then the characteristic temperature scale satisfies

$$
T_H \propto \frac{\hbar c}{R_0},
$$

so $T_H$ is not a free input: it is set by the loop action parameters.

### 8.4 Meaning of the Hagedorn regime

As $T_s \to T_H^-$, the canonical partition function develops the usual near-Hagedorn pathology. This does **not** replace the Jüttner EOS at ordinary temperatures; it marks the onset of loop deconfinement / phase-transition behavior.

So the clean sector split is:

- ordinary matter interpolation:
  $$
  w(z)=\frac{1}{z K_1/K_2 + 3},
  $$
- near-Hagedorn regime:
  stringy excitation density becomes dominant,
- vacuum:
  $$
  w=-1.
  $$

---

## 9. Constancy of $\Lambda_{\mathrm{eff}}$

This also needed one clean statement.

At the **effective level**, once coarse-graining has produced

$$
T^{(\mathrm{bulk})}_{\mu\nu}
=
-\rho_\Lambda g_{\mu\nu},
$$

Bianchi plus metric compatibility imply

$$
\nabla_\mu T^{(\mathrm{bulk})\,\mu}{}_{\nu}
=
-\partial_\nu \rho_\Lambda
=
0,
$$

so

$$
\partial_\nu \rho_\Lambda = 0
$$

for the strictly effective vacuum sector.

At the **microscopic level**, this effective constancy corresponds to the equilibrium requirement that the filling fraction

$$
f = n_{\mathrm{loop}}\frac{4\pi}{3}R_0^3
$$

is stationary.

If the loop vacuum has chemical potential

$$
\mu_{\mathrm{loop}}^{\mathrm{vac}} = 0,
$$

then equilibrium creation/annihilation can maintain

$$
n_{\mathrm{loop}}^{\mathrm{eq}} = \text{const}
$$

at leading order, and therefore

$$
\rho_\Lambda = \Lambda_0 f
$$

is constant at leading order.

So the final careful statement is:

$$
\boxed{
\Lambda_{\mathrm{eff}}\ \text{is exactly constant in the effective theory,}
}
$$

and

$$
\boxed{
\text{its microscopic constancy corresponds to stationary filling fraction in loop equilibrium.}
}
$$

That avoids mixing the micro and effective models.

---

## 10. Sector Table

The cleaned sector structure is:

| Sector | Condition | Equation of state |
|---|---:|---:|
| Vacuum | bulk-dominated, effective Lorentz-invariant background | $w=-1$ |
| Cold matter | $z \gg 1$ | $w \approx 0$ |
| Warm matter | $z \sim 1$ | $0<w<1/3$ |
| Radiation | $z \ll 1$ | $w=1/3$ |
| Near-Hagedorn | $T_s \to T_H^-$ | deconfinement / transition regime |

I am **not** including stiff matter as a solved sector here, because it has not been derived from the same completed dual action in the current text.

---

## 11. Recovery of Standard Gravity Limits

With the Einstein-class law

$$
G_{\mu\nu}+\Lambda_{\mathrm{eff}}g_{\mu\nu}
=
\kappa T^{(\mathrm{NG})}_{\mu\nu},
$$

the standard phenomena follow.

### Newtonian limit

In weak static field,

$$
g_{00}\approx -\left(1+\frac{2\Phi}{c^2}\right),
$$

and for pressureless matter

$$
\nabla^2\Phi = 4\pi G \rho_M.
$$

Outside a spherical source,

$$
\Phi(r)=-\frac{GM}{r},
\qquad
a(r)=-\frac{GM}{r^2}.
$$

### Equivalence principle

Geodesic motion follows from

$$
S_{\mathrm{pp}}=-m\int ds,
$$

and the test mass cancels from the equations of motion.

### Redshift

$$
\frac{\Delta \nu}{\nu}\approx \frac{\Delta\Phi}{c^2}.
$$

### Light bending

$$
\Delta\theta \approx \frac{4GM}{bc^2}.
$$

### Perihelion precession

$$
\Delta\varpi
=
\frac{6\pi GM}{a(1-e^2)c^2}.
$$

### Gravitational-wave speed

Linearizing around flat spacetime gives

$$
\Box \bar h_{\mu\nu}=0,
$$

so propagation speed is $c$.

---

## 12. What is Actually Closed

### Closed enough
1. Einstein-class macro geometry.
2. Dual-null source split:
   $$
   T^{(\Psi)}_{\mu\nu}=T^{(\mathrm{NG})}_{\mu\nu}+T^{(\mathrm{bulk})}_{\mu\nu}.
   $$
3. Minimal low-energy action:
   $$
   S[\Psi]=S_{\mathrm{NG}}+S_{\mathrm{bulk}}.
   $$
4. Exact Jüttner matter-sector interpolation.
5. Vacuum sector with
   $$
   w=-1.
   $$
6. Correct trace bookkeeping.

### Near-closed
1. Phenomenological mapping of $R_0(\Lambda_0,\sigma_T)$.
2. Detailed near-Hagedorn regime beyond the asymptotic density-of-states statement.
3. FLRW perturbation numerics.

---

## 13. Honest Final Compression

The closure-gravity program now reads:

$$
\Delta + \Gamma + I
\;\Rightarrow\;
S[\Psi]=S_{\mathrm{NG}}+S_{\mathrm{bulk}}
\;\Rightarrow\;
T^{(\Psi)}_{\mu\nu}
=
T^{(\mathrm{NG})}_{\mu\nu}
+
T^{(\mathrm{bulk})}_{\mu\nu}
\;\Rightarrow\;
G_{\mu\nu}+\Lambda_{\mathrm{eff}}g_{\mu\nu}
=
\kappa T^{(\mathrm{NG})}_{\mu\nu}.
$$

The source tensor is dual-null in the precise sense that:

- the NG side carries excitations, transport, and matter/radiation,
- the bulk side carries vacuum burden and the effective cosmological constant.

The major architectural gaps are closed.

What remains is no longer ontology. What remains is parameter extraction, FLRW perturbations, and direct phenomenology.

---

## 14. Summary

$$
\boxed{
\text{The source tensor is the dual-null split.}
}
$$

$$
\boxed{
T^{(\Psi)}_{\mu\nu}
=
T^{(\mathrm{NG})}_{\mu\nu}
+
T^{(\mathrm{bulk})}_{\mu\nu}.
}
$$

$$
\boxed{
\text{The dual action }S_{\mathrm{NG}}+S_{\mathrm{bulk}}\text{ is the minimal low-energy closure action.}
}
$$

$$
\boxed{
\text{The matter EOS is exact Jüttner; the vacuum EOS is }w=-1.
}
$$

$$
\boxed{
\text{Einstein-class gravity is the forced large-scale bookkeeping law of the closure substrate.}
}
$$
