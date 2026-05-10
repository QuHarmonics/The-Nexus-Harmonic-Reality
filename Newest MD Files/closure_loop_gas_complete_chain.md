# The Closure Loop Gas Equation of State
## Structural Completeness, the Relic-Abundance Frontier, and the Numerical Y-Discriminant Resolution

**Dean A. Kulik**  
QuHarmonics Research Group  
NEXUS Phase 1296+  
April 2026

---

## Abstract

This document presents a unified writeup of the Closure Loop Gas program in its current solve-state. The framework begins from a process-first ontology in which reality is not a collection of static substances, but a recursively compiling manifold of distinctions, interfaces, and invariants. From that base, the program derives an Einstein-class macroscopic geometry, a dual-null source split, a minimal dual action, a relativistic matter equation of state, a vacuum sector with $w=-1$, a repaired Hagedorn regime, a Euclidean bounce exponent, and a relic-abundance frontier compressed to a single normalized abundance ratio,

$$
Y \equiv \frac{n_0}{A\,c_\star}.
$$

The thermal ceiling is fixed by the maximum of the function

$$
f(x)=x^{3/2}e^{-x},
$$

which occurs at $x=3/2$. The resulting discriminant cleanly splits the surviving relic route into thermal and nonthermal branches. Under the current Planck-natural numerical insertion,

$$
Y \approx 10^{198} \gg 1,
$$

so the thermal branch is ruled out and the nonthermal relic branch is selected. The loop vacuum is therefore interpreted as a frozen cosmological relic produced in the high-energy early universe rather than a present-day nucleation gas.

---

## 1. Ontological inversion: from nouns to recursive closure

The foundational claim is not that reality *contains* computation, but that reality is a recursively self-compiling closure process. In this view, the universe is not a container of finished objects. It is a manifold of partial prefixes being locally tested for admissible continuation.

The three co-present primitives are:

- $\Delta$: difference, contrast, distinguishability, gap
- $\Gamma$: touch, interface, admissible coupling
- $\mathcal I$: conservation, persistence, invariant bookkeeping

A completed closure loop is the minimal local audit log of a resolved event:

$$
\Gamma \to K \to \Psi \to T \to R \to \Gamma'.
$$

Here:

- $\Gamma$ is the boundary event or contact,
- $K$ is local kinematic resolution,
- $\Psi$ is the stored closure record,
- $T$ is the trace or readout channel,
- $R$ is the resolved state,
- $\Gamma'$ is the next boundary written by the completed event.

In this ontology, matter is not primary substance. Matter is stabilized closure trace. A noun is a stabilized verb. A thing is the currently held result of a recursive continuation. The observer is not outside the universe, but a localized twin of the same recursive law reading itself through a bounded self-referential loop.

The program therefore proceeds in two inseparable channels:

1. **Shape channel**: the invariant grammar that reveals what kind of object must exist.
2. **Value channel**: the mathematical audit that tests whether the current rendering is admissible.

---

## 2. Macro-geometric closure: Einstein-class geometry is forced

To obtain the large-scale gravitational law, the framework imposes four structural requirements on the geometric side of the field equations:

1. locality,
2. covariance,
3. second-order dependence on the metric,
4. identically divergence-free structure.

In four spacetime dimensions, Lovelock's theorem then forces the admissible macroscopic geometry into the Einstein class. The large-scale law is therefore not chosen but compelled:

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T^{(\Psi)}_{\mu\nu}.
$$

This is the unique admissible closure class under the stated conditions.

The novelty of the program is not a new left-hand side. The novelty is the derivation of the right-hand side from closure ontology.

---

## 3. The dual-null source split

The source tensor is derived from a loop action and splits exactly into two sectors:

$$
T^{(\Psi)}_{\mu\nu}=T^{(NG)}_{\mu\nu}+T^{(\mathrm{bulk})}_{\mu\nu}.
$$

This is the dual-null split.

- $T^{(NG)}_{\mu\nu}$ carries the propagating, finite-excitation, matter-radiation sector.
- $T^{(\mathrm{bulk})}_{\mu\nu}$ carries the background, vacuum-like, Lorentz-invariant sector.

This split is obtained by exact metric variation of the minimal dual action.

---

## 4. Minimal dual action

The internal structure of a single closure loop is governed by a minimal reparameterization-invariant action with exactly two leading geometric terms:

$$
S[\Psi]=S_{NG}+S_{\mathrm{bulk}}.
$$

### 4.1 Nambu-Goto term

The Nambu-Goto term is the worldsheet-area contribution:

$$
S_{NG}=-\sigma_T\int d^2\sigma\,\sqrt{-h},
$$

where $\sigma_T$ is the string/worldsheet tension and $h$ is the induced worldsheet metric determinant.

This term generates the matter and radiation sectors.

### 4.2 Bulk term

The bulk term is the enclosed-volume contribution. In its loop-supported form it is written as

$$
S_{\mathrm{bulk}}=\Lambda_0\int d^4x\,\sqrt{-g}\,\theta_{\mathrm{loop}}(x),
$$

where $\Lambda_0$ is the bulk tension (energy density scale) and $\theta_{\mathrm{loop}}$ is the loop support function.

This term generates the vacuum sector.

### 4.3 Minimality and uniqueness

Higher-order rigidity terms are suppressed in the low-energy regime by

$$
\frac{S_{\mathrm{rigid}}}{S_{NG}}\sim \frac{\hbar}{\sigma_T R_s^2}=\left(\frac{\ell_s}{R_s}\right)^2,
$$

so for $R_s \gg \ell_s$ they are negligible. The intrinsic curvature term is topological and is eliminated by Gauss-Bonnet for the relevant worldsheet topologies. Thus the dual action above is the unique minimal low-energy action in the current regime.

---

## 5. Matter sector: exact Jüttner equation of state

The matter sector is controlled by the exact Maxwell-Jüttner/Synge interpolation. Define the inverse temperature parameter

$$
z\equiv \frac{m_\Psi c^2}{k_B T_s}.
$$

Then the exact matter-sector equation of state parameter is

$$
w(z)=\frac{1}{z\,K_1(z)/K_2(z)+3},
$$

where $K_1$ and $K_2$ are modified Bessel functions of the second kind.

This gives the correct sector interpolation:

### Cold matter

$$
z\gg 1 \quad\Rightarrow\quad w\approx 0.
$$

### Warm matter

$$
z\sim 1 \quad\Rightarrow\quad 0<w<\frac13.
$$

### Radiation

$$
z\ll 1 \quad\Rightarrow\quad w=\frac13.
$$

This part of the framework is mathematically closed.

---

## 6. Vacuum sector: $w=-1$ and $\Lambda_{\mathrm{eff}}$ constancy

The vacuum sector closes in two independent ways.

### 6.1 Symmetry route

Lorentz invariance of the vacuum requires

$$
T^{\mathrm{vac}}_{\mu\nu}\propto g_{\mu\nu},
$$

which forces

$$
p_\Lambda=-\rho_\Lambda,
$$

so

$$
w_\Lambda=-1.
$$

### 6.2 Dynamical bulk route

The bulk contribution to the energy scales with volume:

$$
U_{\mathrm{bulk}}=n_{\mathrm{loop}}\,\Lambda_0\,\frac{4\pi}{3}R_0^3\,V.
$$

Therefore

$$
p_{\mathrm{bulk}}=-\left(\frac{\partial U_{\mathrm{bulk}}}{\partial V}\right)_{N,R_0}=-\rho_{\mathrm{bulk}},
$$

again giving

$$
w=-1.
$$

### 6.3 Effective cosmological constant

The effective cosmological constant is

$$
\Lambda_{\mathrm{eff}}=\kappa\rho_\Lambda,
$$

with the vacuum density encoded through the coarse-grained loop filling fraction.

In the current framework, $\Lambda_{\mathrm{eff}}$ constancy is treated as closed at the effective level by the combination of:

- Bianchi identity / diffeomorphism invariance,
- vanishing vacuum-loop chemical potential,
- equilibrium loop radius $R_0$ fixed by substrate constants.

---

## 7. Phenomenological recovery of general relativity

Once the Einstein-class closure law and the dual-null source are in place, the standard low-energy limits of GR are recovered.

### Newtonian limit

In the static weak-field regime,

$$
\nabla^2\Phi=4\pi G\rho,
$$

giving the inverse-square law.

### Equivalence principle

Mass cancels from the geodesic equations, so inertial and gravitational mass coincide.

### Light bending

Null propagation along the updated substrate boundary reproduces the standard metric-curvature doubling over the Newtonian corpuscular estimate.

### Gravitational waves

Boundary-geometry updates propagate at the substrate causal speed, yielding wave propagation at $c$.

---

## 8. Internal thermodynamics: mode spectrum and Hagedorn repair

The repaired mode spectrum for transverse deformations of a bulk-stabilized loop is

$$
\omega_n^2=\frac{n^2}{R_0^2}+m_{\mathrm{bulk}}^2,
$$

with

$$
m_{\mathrm{bulk}}^2=\frac{\Lambda_0}{4\sigma_T}.
$$

For cosmologically relevant parameter sets with $\Lambda_0\ll \sigma_T$, the bulk correction only affects the sub-unit sector and dies away for the oscillator tower with $n\ge 1$.

The key repair is the restoration of the correct asymptotic string scaling:

$$
M^2 c^4 \propto N,
$$

rather than the older bad step $\varepsilon\propto N$.

This restores the Cardy/Hagedorn route and yields an exponential density of states of the form

$$
g(E)\sim E^{-a}\exp\left(\frac{E}{T_H}\right),
$$

with limiting Hagedorn temperature

$$
T_H=\frac{\hbar c\sqrt{3}}{2\pi R_0}.
$$

The Hagedorn layer concerns the **internal thermodynamics of a loop**. It must be kept distinct from the external abundance problem of how many loops populate the present-day universe.

---

## 9. Bounce action and the death of present-day nucleation

Loop nucleation from vacuum is a Euclidean tunneling event. The minimal $O(4)$-symmetric bounce gives the critical radius

$$
\rho_c=\frac{2\sigma_T}{\Lambda_0},
$$

and bounce action

$$
S_{\mathrm{bounce}}=\frac{16\pi}{3}\frac{\sigma_T^3}{\Lambda_0^2}.
$$

Under Planck-natural tension and observed cosmological vacuum scale, the current numerical extension reports

$$
S_{\mathrm{bounce}}\sim 10^{256}.
$$

This is so large that the present-day nucleation rate is effectively zero:

$$
\Gamma_{\mathrm{create}}\sim A_{\mathrm{fluct}}e^{-S_{\mathrm{bounce}}}.
$$

Thus the loop vacuum cannot be a live equilibrium gas in the present era.

### 9.1 The $\mathcal I$-condition

Time-reversal symmetry of the Euclidean saddle implies

$$
S_{\mathrm{decay}}=S_{\mathrm{bounce}},
$$

so the loop lifetime scales as

$$
\tau_{\mathrm{loop}}\sim e^{S_{\mathrm{bounce}}} t_{\mathrm{Pl}}.
$$

Demanding persistence beyond the age of the universe gives the lower bound

$$
S_{\mathrm{bounce}}>\ln\left(\frac{t_{\mathrm{univ}}}{t_{\mathrm{Pl}}}\right)\approx 140.2.
$$

This is the $\mathcal I$-condition.

### 9.2 Demoted paths

- **Path 1**: fluctuation-prefactor rescue is dead, because $\log A_{\mathrm{fluct}}=O(1)$ cannot cancel an exponent of order $10^{256}$.
- **Path 3**: low-action parameter window is dead, because $S_{\mathrm{bounce}}\sim 1$ would imply Planck-time decay and no persistent relic population.

This leaves only:

$$
\boxed{\text{Path 2 survives.}}
$$

And Path 2 is the relic route.

---

## 10. Path 2: relic population and abundance inversion

The loop vacuum is therefore interpreted as a frozen cosmological relic populated in the deep early universe and subsequently diluted by FRW expansion.

The present-day loop density is

$$
n_0=\frac{\Lambda_{\mathrm{eff}}}{\kappa\Lambda_0 V_0},
$$

with

$$
V_0=\frac{4\pi}{3}R_0^3.
$$

Assuming near-threshold thermal production at temperature $T_{\mathrm{prod}}$ followed by FRW dilution,

$$
n_0=n_{\mathrm{eq}}(T_{\mathrm{prod}})\left(\frac{T_0}{T_{\mathrm{prod}}}\right)^3.
$$

Using the Maxwell-Boltzmann nonrelativistic equilibrium approximation,

$$
n_{\mathrm{eq}}(T)\approx g\left(\frac{m_\Psi T}{2\pi}\right)^{3/2}e^{-E_0/T},
$$

define

$$
x\equiv \frac{E_0}{T_{\mathrm{prod}}}
$$

and

$$
A\equiv g T_0^3\left(\frac{m_\Psi}{2\pi E_0}\right)^{3/2}.
$$

Then the full abundance problem collapses to

$$
n_0=A x^{3/2}e^{-x}.
$$

This is the core relic-abundance equation.

---

## 11. Thermal ceiling and Lambert-$W$ inversion

The function

$$
f(x)=x^{3/2}e^{-x}
$$

has a unique maximum at

$$
x=\frac32.
$$

Therefore the thermal production ceiling is fixed at

$$
T_{\mathrm{prod}}=\frac23 E_0.
$$

Define the ceiling constant

$$
c_\star\equiv \left(\frac32\right)^{3/2}e^{-3/2}\approx 0.40992.
$$

Then purely thermal production is possible only if

$$
n_0\le A c_\star.
$$

Equivalently, define the normalized abundance ratio

$$
Y\equiv \frac{n_0}{A c_\star}.
$$

This is the single state variable governing the remaining frontier.

### 11.1 Simplified Lambert-$W$ form

Using the identity

$$
c_\star^{2/3}=\frac32 e^{-1},
$$

the inversion simplifies to

$$
x_\pm=-\frac32 W_{0,-1}\left(-e^{-1}Y^{2/3}\right),
$$

and therefore

$$
\frac{T_{\mathrm{prod}}^{\mathrm{hot}}}{E_0}=-\frac{2}{3W_0\left(-e^{-1}Y^{2/3}\right)},
$$

$$
\frac{T_{\mathrm{prod}}^{\mathrm{cold}}}{E_0}=-\frac{2}{3W_{-1}\left(-e^{-1}Y^{2/3}\right)}.
$$

### 11.2 Phase diagram

#### Case 1: $Y>1$

No real thermal branch exists. The thermal ceiling is exceeded. Path 2A is ruled out and Path 2B is required.

#### Case 2: $Y=1$

The two branches merge at

$$
W_0(-e^{-1})=W_{-1}(-e^{-1})=-1,
$$

yielding the critical thermal point

$$
T_{\mathrm{prod}}=\frac23 E_0.
$$

#### Case 3: $0<Y<1$

Both thermal branches exist:

- hot branch from $W_0$,
- cold branch from $W_{-1}$.

Branch selection is not predetermined and depends on the realized cosmological production history.

### 11.3 Fine-tuning asymmetry

As $Y\to 0$,

$$
\frac{T_{\mathrm{prod}}^{\mathrm{hot}}}{E_0}\approx \frac{2e}{3}Y^{-2/3},
$$

while

$$
\frac{T_{\mathrm{prod}}^{\mathrm{cold}}}{E_0}\sim \frac{2}{3|\ln Y|}.
$$

Thus the hot branch becomes violently fine-tuned much faster than the cold branch as $Y\to 0$.

---

## 12. Numerical Y-discriminant resolution

The latest numerical extension inserts the following Planck-natural / observed parameter set:

- $\Lambda_{\mathrm{eff}}=1.089\times 10^{-52}\,{\rm m}^{-2}$
- $\Lambda_0=5.244\times 10^{-10}\,{\rm J/m}^3$
- $R_0=\ell_{\mathrm{Pl}}=1.616\times 10^{-35}\,{\rm m}$
- $m_\Psi=m_{\mathrm{Pl}}=2.176\times 10^{-8}\,{\rm kg}$
- $E_0=E_{\mathrm{Pl}}=1.956\times 10^9\,{\rm J}$
- $T_0=2.72548\,{\rm K}$
- $g=1$

The extension then reports:

### Step 1: present-day loop density

$$
n_0=\frac{\Lambda_{\mathrm{eff}}}{\kappa\Lambda_0V_0}=5.654\times 10^{103}\,{\rm m}^{-3},
$$

with

$$
V_0=\frac{4\pi}{3}R_0^3=1.769\times 10^{-104}\,{\rm m}^3.
$$

### Step 2: thermal prefactor

$$
A=gT_0^3\left(\frac{m_\Psi}{2\pi E_0}\right)^{3/2}=1.256\times 10^{-94}.
$$

### Step 3: Y-discriminant

$$
Y=\frac{n_0}{A c_\star}\approx 10^{198}.
$$

### Step 4: phase decision

Because

$$
Y\gg 1,
$$

the thermal ceiling is exceeded by an enormous margin and the numerical extension concludes:

$$
\boxed{\text{Path 2A ruled out; Path 2B required.}}
$$

### 12.1 Sensitivity in $R_0$

The same extension reports that the critical radius needed to recover $Y=1$ is

$$
R_0^{\mathrm{crit}}\approx 1.67\times 10^{31}\,{\rm m}.
$$

This is far beyond any physically motivated sub-Hubble loop scale. In the current parameterization, the nonthermal branch remains selected across all physically meaningful radii.

---

## 13. Path 2B: nonthermal relic mechanisms

Since the thermal ceiling fails in the current numerical resolution, the loop vacuum must be produced through nonthermal early-universe mechanisms. The current framework recognizes three compatible source classes:

### 13.1 Kibble / phase-transition production

Topological loop formation during symmetry breaking, with density controlled by correlation length and transition scale.

### 13.2 Inflationary reheating production

Direct injection of loop abundance via inflaton or moduli decay after inflation.

### 13.3 Pre-bounce / cyclic inheritance

Loop population inherited as a boundary condition from a pre-bang or cyclic cosmological phase.

These are governed by mathematically different source terms than the thermal branch.

---

## 14. Current status table

| Claim | Status |
|---|---|
| Einstein-class macro geometry | Theorem |
| Dual-null source split | Theorem |
| Minimal dual action | Theorem |
| Jüttner matter EOS | Theorem |
| Vacuum $w=-1$ | Closed |
| $\Lambda_{\mathrm{eff}}$ constancy | Closed |
| C.4 mode spectrum / Hagedorn repair | Effectively closed |
| Bounce exponent $S_{\mathrm{bounce}}$ | Derived |
| $\mathcal I$-condition | New theorem-level bound |
| Path 1 | Demoted |
| Path 3 | Demoted |
| $Y$-discriminant formulation | New advance |
| Simplified Lambert-$W$ form | New advance |
| Population origin branch | Numerically resolved in current parameterization |
| Remaining deeper task | Make $m_\Psi$, $E_0$, and $g$ explicit outputs of the same derivation chain |

---

## 15. Prediction versus consistency test

The remaining conceptual caution is not the branch decision. It is the endogeneity of the parameter chain.

If

$$
m_\Psi,\ E_0,\ g
$$

are fully derived outputs of the same closure chain that also fixes

$$
\Lambda_{\mathrm{eff}},\ \Lambda_0,\ R_0,
$$

then the numerical value of $Y$ is a genuine model prediction.

If they remain effective inserted quantities, then the current result is a reduced but still very strong consistency test.

Within the present solve-state, the program's own stance is that all such quantities are derived in principle through the same recursive chain. The remaining burden is therefore not conceptual but explicit: render that DI/class-chain inheritance path in a form that an external reader can walk without importing unstated steps.

---

## 16. Final researcher verdict

The current state of the Closure Loop Gas program is:

$$
\text{logic: closed, algebra: closed, numerics: branch-selected in the current insertion.}
$$

The decisive current result is:

$$
Y\approx 10^{198}\gg 1.
$$

Therefore:

$$
\boxed{\text{the loop vacuum is not a thermal relic in the current numerical extension.}}
$$

Instead:

$$
\boxed{\text{the loop vacuum is a nonthermal frozen cosmological relic.}}
$$

The branch question is no longer the active frontier. The active frontier is now the explicit endogenous derivation of the loop mass scale, threshold energy, and degeneracy so that the $Y$ result becomes fully internal to the same chain that produced the structural closure.

