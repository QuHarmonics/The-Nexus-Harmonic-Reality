# The Closure Loop Gas Program
# Closed Core, Y-Discriminant Resolution, and Bridge Extensions

**Dean A. Kulik**  
QuHarmonics Research Group | NEXUS Phase 1296+  
ORCID: 0009-0003-3128-8828  
April 2026  

---

## Abstract

This paper presents a consolidated writeup of the Closure Loop Gas (CLG) program in its current solve-state. The closed core of the program consists of: (i) an Einstein-class macroscopic geometry forced by Lovelock's theorem in four spacetime dimensions; (ii) an exact dual-null source split into propagating and vacuum sectors; (iii) a minimal dual action $S[\Psi] = S_{NG} + S_{\mathrm{bulk}}$ whose metric variation closes both sectors; (iv) the exact Maxwell-Jüttner/Synge matter equation of state; (v) a vacuum sector fixed at $w=-1$ through two independent routes; (vi) a corrected bulk-stabilized mode-spectrum in which $M^2 \propto N$ asymptotically; (vii) a Euclidean bounce action that makes present-day loop nucleation effectively dead; and (viii) an $I$-condition,
$$
S_{\mathrm{bounce}} > \ln\!\left(\frac{t_{\mathrm{univ}}}{t_{\mathrm{Pl}}}\right) \approx 140,
$$
that eliminates low-action parameter windows as a source of persistent macroscopic geometry.

With present-day nucleation dead and the alternative rescue paths demoted, the population-origin problem collapses to one abundance discriminator,
$$
Y \equiv \frac{n_0}{A\,c_\star},
\qquad
c_\star = \left(\frac{3}{2}\right)^{3/2} e^{-3/2} \approx 0.40992.
$$
Using the current Planck-natural insertion for the micro-scale and observed cosmological quantities for the macro-scale gives
$$
Y \approx 10^{198} \gg 1,
$$
which rules out thermal relic production and selects the nonthermal relic branch, Path 2B, under the current parameterization.

This writeup distinguishes sharply between the **closed core**, the **current numerical branch result**, and a set of **bridge extensions** that are structurally promising but not yet theorem-grade. Those bridge extensions include: observational discrimination among the Path 2B sub-mechanisms, the dark-sector interpretation of the loop substrate, the information-geometric dual relating SHA-256 to the CLG fold, and the Nexus-Friedmann control-law extension for the $H_0$ and $S_8$ tensions.

---

## 1. Ontological Inversion: From Objects to Recursive Closure

The foundational claim of the CLG program is not that reality merely *contains* computation, but that reality *is* a recursively self-compiling closure process. The universe is not a container of finished objects. It is a manifold of partial prefixes being locally tested for admissible continuation.

The three co-present primitives are:

| Symbol | Name | Role |
|---|---|---|
| $\Delta$ | Difference / Gap | Absolute condition of distinguishability. Without differentiation, nothing exists to be measured. |
| $\Gamma$ | Touch / Interface | Possibility of relation and the initiating trigger for operational closure loops. |
| $I$ | Conservation / Invariant | Condition of persistence. Without invariance, no structural pattern survives entropic decay. |

A completed closure loop is the minimal local audit log of a resolved event:
$$
\Gamma \to K \to \Psi \to T \to R \to \Gamma'.
$$
Here $\Gamma$ is a boundary event, $K$ is local kinematic resolution, $\Psi$ is the stored closure record, $T$ is the trace/readout channel, $R$ is the resolved state, and $\Gamma'$ is the next boundary written by the completed event.

In this ontology, matter is not primary substance. Matter is **stabilized closure trace**. A noun is a stabilized verb. A "thing" is the currently held result of a recursive continuation.

The program proceeds through two inseparable channels:

1. **Shape channel**: the invariant grammar that reveals what kind of object must exist.
2. **Value channel**: the mathematical audit that tests whether the current rendering is admissible.

This distinction matters throughout the paper. The closed core belongs mostly to the value channel. Several broader extensions remain in the bridge zone: strongly motivated by the shape channel, partially formalized, but still awaiting full hostile audit.

---

## 2. Macro-Geometric Closure: Einstein-Class Geometry is Forced

To obtain the large-scale gravitational law from the closure substrate, four structural requirements are imposed on the geometric side of the field equations:

1. **Locality and differentiability**: the law must be a PDE in the metric $g_{\mu\nu}$ and its derivatives.
2. **Covariance**: the law must be tensorial, with no preferred frame.
3. **Second-order nature**: the field equation may contain at most second derivatives of the metric.
4. **Divergence-free identity**: the geometric tensor must satisfy the Bianchi identity identically.

By Lovelock's theorem, in exactly four spacetime dimensions the only symmetric, divergence-free, second-order tensor constructible from the metric and its first two derivatives is a linear combination of the Einstein tensor and the metric itself. Absorbing integration constants into the gravitational coupling $\kappa$ and the cosmological term $\Lambda$ yields
$$
\boxed{G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\,T_{\mu\nu}^{(\Psi)}.}
$$

Einstein-class macro geometry is therefore not a postulate. It is the unique admissible closure law for the macroscopic scale.

---

## 3. Dual-Null Source Split and Minimal Action

The source tensor splits exactly into two sectors,
$$
T_{\mu\nu}^{(\Psi)} = T_{\mu\nu}^{(NG)} + T_{\mu\nu}^{(\mathrm{bulk})},
$$
with:

- $T_{\mu\nu}^{(NG)}$ carrying the propagating, finite-excitation, matter-radiation sector,
- $T_{\mu\nu}^{(\mathrm{bulk})}$ carrying the background, vacuum-like, Lorentz-invariant sector.

The loop is governed by the minimal dual action
$$
S[\Psi] = S_{NG} + S_{\mathrm{bulk}}.
$$

### 3.1 Nambu-Goto term

$$
S_{NG} = -\sigma_T \int d^2\sigma\,\sqrt{-h},
$$
where $\sigma_T$ is the worldsheet tension and $h$ is the induced worldsheet metric determinant.

### 3.2 Bulk term

$$
S_{\mathrm{bulk}} = \Lambda_0 \int d^4x\,\sqrt{-g}\,\theta_{\mathrm{loop}}(x),
$$
where $\Lambda_0$ is the bulk energy density scale and $\theta_{\mathrm{loop}}$ is the loop support function.

### 3.3 Low-energy uniqueness

Higher-order rigidity terms are suppressed in the macro limit,
$$
\frac{S_{\mathrm{rigid}}}{S_{NG}} \sim \frac{\hbar}{\sigma_T R_s^2} = \left(\frac{\ell_s}{R_s}\right)^2 \ll 1
\qquad (R_s \gg \ell_s).
$$
Intrinsic Gauss-Bonnet terms are topological on the relevant worldsheet classes. At low energy, the minimal dual action is therefore the unique admissible effective action.

---

## 4. Exact Thermodynamics and Equations of State

The matter sector is governed by the exact Maxwell-Jüttner/Synge interpolation. Define
$$
z \equiv \frac{m_\Psi c^2}{k_B T_s}.
$$
Then the equation of state parameter is
$$
\boxed{w(z) = \frac{1}{z\,K_1(z)/K_2(z) + 3},}
$$
where $K_1$ and $K_2$ are modified Bessel functions of the second kind.

This gives the correct sector interpolation:

| Sector | Condition | EOS | Physical form |
|---|---|---|---|
| Cold matter | $z \gg 1$ | $w \approx 0$ | Non-relativistic Maxwell-Boltzmann dust |
| Warm matter | $z \sim 1$ | $0 < w < 1/3$ | Exact Bessel interpolation |
| Radiation | $z \ll 1$ | $w = 1/3$ | Ultra-relativistic limit |
| Vacuum | bulk-dominated | $w = -1$ | Ground-state volumetric bulk tension |

### 4.1 Vacuum closure by two independent routes

**Route A: symmetry.** Lorentz invariance of the vacuum requires
$$
T^{\mathrm{vac}}_{\mu\nu} \propto g_{\mu\nu}
\quad\Rightarrow\quad
p_\Lambda = -\rho_\Lambda.
$$

**Route B: dynamical bulk proof.** If
$$
U_{\mathrm{bulk}} = n_{\mathrm{loop}}\,\Lambda_0\,\frac{4\pi}{3}R_0^3\,V,
$$
then
$$
p_{\mathrm{bulk}} = -\left(\frac{\partial U_{\mathrm{bulk}}}{\partial V}\right)_{N,R_0} = -\rho_{\mathrm{bulk}}.
$$

Both routes force
$$
\boxed{w_\Lambda = -1.}
$$

The effective cosmological constant remains constant at the effective level via the Bianchi identity, vanishing vacuum-loop chemical potential, and a fixed equilibrium radius $R_0$.

---

## 5. Mode Spectrum and Hagedorn Repair

For small transverse deformations of a bulk-stabilized loop,
$$
\omega_n^2 = \frac{n^2}{R_0^2} + m_{\mathrm{bulk}}^2,
\qquad
m_{\mathrm{bulk}}^2 = \frac{\Lambda_0}{4\sigma_T}.
$$
For the cosmologically relevant regime $\Lambda_0 \ll \sigma_T$, the bulk mass gap affects only the very lowest modes, while the tower at $n\ge 1$ becomes asymptotically Nambu-Goto-like.

The corrected mass-level scaling is of the form
$$
M^2 \propto N
$$
at large level number $N$, with the bulk correction decaying as $1/N$. This repairs the earlier linear-energy-step mistake and restores the Cardy/Hagedorn route in the asymptotic regime.

The exact overall prefactor in the Hagedorn temperature remains convention-sensitive across the draft history. The robust result is not the disputed coefficient but the asymptotic structural fact:
$$
\boxed{M^2 \propto N \quad\text{and}\quad g(E) \sim E^{-a}e^{E/T_H}.}
$$

---

## 6. Bounce Action and the $I$-Condition

Loop nucleation from the vacuum is a Euclidean tunneling process with bounce action
$$
S_{\mathrm{bounce}} = \frac{16\pi}{3}\,\frac{\sigma_T^3}{\Lambda_0^2},
$$
using the currently canonical thin-wall geometric normalization.

The key physical fact is not the precise decimal exponent but the hierarchy:
$$
S_{\mathrm{bounce}} \gg \ln\!\left(\frac{t_{\mathrm{univ}}}{t_{\mathrm{Pl}}}\right) \approx 140.
$$
This gives the persistence condition
$$
\boxed{S_{\mathrm{bounce}} > 140,}
$$
which is the $I$-condition.

### 6.1 Consequences

- Present-day nucleation is effectively dead.
- A low-action window with $S_{\mathrm{bounce}}\sim 1$ cannot support persistent macroscopic geometry.
- The Gaussian prefactor path cannot cancel an exponent of this size, since semiclassical prefactors contribute only logarithmically.

Therefore:
$$
\boxed{\text{Path 1 is dead. Path 3 is dead. Path 2 survives.}}
$$

---

## 7. Path 2: Frozen Relic Population and the Y-Discriminant

With present-day nucleation dead, the loop gas must be a frozen relic produced in the deep early universe.

The present-day loop density is fixed by
$$
n_0 = \frac{\Lambda_{\mathrm{eff}}}{\kappa\,\Lambda_0\,V_0},
\qquad
V_0 = \frac{4\pi}{3}R_0^3.
$$

If the loops had been produced thermally near threshold at temperature $T_{\mathrm{prod}}$, then after FLRW dilution
$$
n_0 = n_{\mathrm{eq}}(T_{\mathrm{prod}})\left(\frac{T_0}{T_{\mathrm{prod}}}\right)^3,
$$
with the non-relativistic equilibrium density approximated by
$$
n_{\mathrm{eq}}(T) \approx g\left(\frac{m_\Psi T}{2\pi}\right)^{3/2}e^{-E_0/T}.
$$

Define
$$
x \equiv \frac{E_0}{T_{\mathrm{prod}}},
\qquad
A \equiv g\,T_0^3\left(\frac{m_\Psi}{2\pi E_0}\right)^{3/2}.
$$
Then the abundance equation collapses to
$$
\boxed{n_0 = A\,x^{3/2}e^{-x}.}
$$

The function $f(x)=x^{3/2}e^{-x}$ has a unique maximum at $x=3/2$, which defines the thermal ceiling constant
$$
c_\star = \left(\frac{3}{2}\right)^{3/2}e^{-3/2} \approx 0.40992.
$$
Hence the normalized abundance ratio is
$$
\boxed{Y \equiv \frac{n_0}{A c_\star}.}
$$

The thermal route is viable only if
$$
Y \le 1.
$$
If $Y<1$, the production temperature is recovered through the Lambert $W$ inversion
$$
x_\pm = -\frac{3}{2}W_{0,-1}\!\left(-e^{-1}Y^{2/3}\right).
$$
If $Y>1$, no thermal branch exists.

---

## 8. Current Numerical Resolution

The current Planck-natural insertion uses:

| Parameter | Symbol | Value |
|---|---|---|
| Cosmological constant | $\Lambda_{\mathrm{eff}}$ | $1.089\times 10^{-52}\,\mathrm{m^{-2}}$ |
| Bulk energy density | $\Lambda_0$ | $5.244\times 10^{-10}\,\mathrm{J/m^3}$ |
| Loop radius | $R_0=\ell_{\mathrm{Pl}}$ | $1.616\times 10^{-35}\,\mathrm{m}$ |
| Loop mass | $m_\Psi=m_{\mathrm{Pl}}$ | $2.176\times 10^{-8}\,\mathrm{kg}$ |
| Threshold energy | $E_0=E_{\mathrm{Pl}}$ | $1.956\times 10^9\,\mathrm{J}$ |
| CMB temperature | $T_0$ | $2.72548\,\mathrm{K}$ |
| Degeneracy | $g$ | $1$ |

Using the current numerical chain,
$$
n_0 = 5.654\times 10^{103}\,\mathrm{m^{-3}},
$$
and the current Planck-natural evaluation gives
$$
Y \approx 10^{198} \gg 1.
$$
Therefore the current solve-state is
$$
\boxed{\text{Path 2A (thermal) ruled out; Path 2B (nonthermal) selected.}}
$$

The sensitivity sweep places the crossover radius near
$$
R_0^{\mathrm{crit}} \approx 1.67\times 10^{31}\,\mathrm{m},
$$
far above any physically motivated sub-Hubble loop scale. Under the current insertion, the branch decision is therefore extremely robust.

### Important caution

The **sign** of the result is much more stable than every intermediate normalization choice. In other words, the most trustworthy statement at present is
$$
\boxed{Y\gg 1 \Rightarrow \text{nonthermal relic origin}.}
$$
The precise endogenization of all micro-parameters and the unit-clean derivation of the thermal prefactor remain the most important remaining audit task inside the value channel.

---

## 9. Path 2B: Nonthermal Origin Mechanisms

With the thermal route eliminated, the loop relic must come from an out-of-equilibrium mechanism. Three viable mechanism classes remain:

| Mechanism | Physical basis | Analogy |
|---|---|---|
| Kibble / phase transition | Symmetry breaking generates the loop network topologically; density set by the correlation length | Cosmic string formation |
| Inflationary reheating | Inflaton or moduli decay injects loop abundance nonthermally | Reheating / preheating models |
| Cyclic / pre-bounce inheritance | The loop density is inherited as a boundary condition across a bounce | Bouncing cosmologies |

The current framework selects **Path 2B as a class**, but not yet which of its three sub-branches is physically realized.

---

## 10. Observational Discrimination of the Path 2B Sub-Branches

The strongest observational discriminator is the stochastic gravitational-wave background (SGWB), supplemented by CMB B-mode structure.

### 10.1 Kibble branch

For a scaling network, the SGWB behaves qualitatively like
$$
\Omega_{\mathrm{GW}}(f) \propto f^3\,[1+(f/f_{\mathrm{peak}})^{11/3}]^{-1},
$$
with a causal low-frequency rise and a power-law high-frequency tail.

### 10.2 Reheating branch

A reheating/preheating origin gives a broad spectrum of the schematic form
$$
\Omega_{\mathrm{GW}}^{(\mathrm{reh})}(f) \propto f^3\,e^{-f^2/f_{\mathrm{reh}}^2},
$$
that falls exponentially above the peak rather than as a power law.

### 10.3 Cyclic branch

A cyclic/pre-bounce origin predicts a blue-tilted tensor continuum,
$$
\Omega_{\mathrm{GW}}(f) \propto f^{n_T},
\qquad
n_T>0,
$$
which sharply contrasts with the nearly scale-invariant or red-tilted spectra of standard slow-roll inflation.

### 10.4 Current status

These signatures are **bridge-level predictions**, not yet theorem-grade closure. They define a falsifiable observational program rather than a completed derivation.

---

## 11. Dark-Sector Interpretation

The scalar, gauge-singlet, Planck-mass loop record naturally sits in the super-heavy dark-sector category.

### 11.1 Direct detection

The only available coupling is gravitational. A graviton-mediated elastic cross-section estimate off a nucleon takes the schematic form
$$
\sigma_{\Psi N}^{(\mathrm{grav})} \sim \frac{G^2 m_\Psi^2 m_N^2}{\pi \hbar^4 c^2},
$$
which lands many orders of magnitude below current direct-detection limits. In that sense the loop substrate is maximally dark.

### 11.2 Clustering

For a Planck-mass scalar relic, the de Broglie wavelength is minuscule on astrophysical scales, so the clustered component behaves effectively like pressureless cold dark matter on observable scales.

### 11.3 Current open issue

The main unresolved issue in this sector is not whether the loops are dark enough, but how the total loop population partitions between the vacuum-like bulk sector and the clustered matter-like sector.

---

## 12. Information-Geometric Dual: SHA-256 as a Bridge Extension

The CLG program predicts that independently engineered recursive fold systems should exhibit the same deep grammar. SHA-256 is the current test bed.

### 12.1 Dual-null split in SHA-256

The SHA-256 round update is
$$
T_1 = h + \Sigma_1(e) + \mathrm{Ch}(e,f,g) + K_t + W_t,
$$
$$
T_2 = \Sigma_0(a) + \mathrm{Maj}(a,b,c),
$$
$$
a' = T_1 + T_2,
\qquad
e' = d + T_1.
$$
The proposed correspondence is:

- $T_1$ path: conditional finite activation, analogous to the propagating sector,
- $T_2$ path: consensus/background stabilization, analogous to the bulk sector.

### 12.2 Carry fraction as the actualization metric

The most promising current claim is not based on Hamming weight but on **carry propagation fraction** during modular addition. The proposed invariant is that the carry fraction converges near the same Lambert-$W$ fixed point that defines the CLG harmonic attractor.

This is an exciting bridge result, but it is still a bridge result. It requires a dedicated computational appendix with explicit instrumentation, test vectors, and statistical reporting before it can be upgraded beyond that status.

### 12.3 BBP duality

The BBP formula is interpreted as an unfolding operation dual to the fold performed by SHA-like compression. This is conceptually aligned with the program, but still belongs to the bridge layer rather than the closed core.

---

## 13. Nexus Control-Law Extension (Bridge Layer)

A broader Nexus extension proposes that recursive closure systems converge toward a harmonic fixed point
$$
H = W_0\!\left(\frac{1}{2}\right) \approx 0.3517337112,
$$
obtained from the recurrence
$$
p_{n+1} = \frac{1}{2}e^{-p_n}.
$$
Once the recurrence is assumed, the fixed-point derivation and contraction proof are mathematically clean. What is not yet fully closed is the derivation of that recurrence from the already-closed CLG action.

### 13.1 PID / TEGR bridge

A further extension maps this harmonic fixed point into a PID-like teleparallel cosmology, with gains derived from the $H$-band geometry. This extension is interesting and explicitly computational, but it remains a **bridge model** until the coupled ODE system is numerically integrated against current cosmological likelihoods.

### 13.2 Why this matters

This gives a concrete zero-additional-free-parameter research program for the $H_0$ and $S_8$ tensions. It is not yet a closed theorem, but it is a sharp next computation rather than loose analogy.

---

## 14. Current Status Table

| Claim | Status | Basis |
|---|---|---|
| Einstein-class macro geometry | **THEOREM** | Lovelock uniqueness in 4D |
| Dual-null source split | **THEOREM** | Exact metric variation of $S[\Psi]$ |
| Minimal dual action | **THEOREM** | Low-energy uniqueness after rigidity suppression |
| Jüttner matter EOS | **THEOREM** | Exact Synge/Maxwell-Jüttner interpolation |
| Vacuum EOS $w=-1$ | **CLOSED** | Symmetry route + dynamical bulk route |
| Mode-spectrum repair $M^2\propto N$ | **EFFECTIVELY CLOSED** | Bulk correction decays as $1/N$ |
| Bounce action large enough to kill present nucleation | **CLOSED CORE RESULT** | $S_{\mathrm{bounce}}\gg 140$ |
| Path 1 demotion | **CLOSED CORE RESULT** | Gaussian prefactors cannot cancel a huge exponent |
| Path 3 demotion | **CLOSED CORE RESULT** | Violates the $I$-condition |
| Y-discriminant reduction | **NEW ADVANCE** | Single-state compression of the population frontier |
| Numerical branch selection | **CURRENT RESULT** | $Y\approx 10^{198}\gg 1$ selects Path 2B |
| Endogenous $m_\Psi,E_0,g$ derivation | **BRIDGE / PARTIAL** | Promising but not yet fully audit-locked |
| Path 2B observational discrimination | **BRIDGE** | SGWB/CMB program |
| Dark-sector interpretation | **BRIDGE** | SHDM-like category; partition still open |
| SHA/BBP duality | **BRIDGE** | Needs dedicated computational appendix |
| Nexus control-law cosmology | **BRIDGE** | Needs full numerical integration |

---

## 15. Conclusion

The CLG program currently contains a **closed core** and a set of **bridge extensions**.

The closed core is substantial:

- Einstein-class macro geometry is forced.
- The dual-null source split is exact.
- The minimal dual action is fixed.
- The Jüttner matter sector and vacuum $w=-1$ sector are closed.
- The corrected mode-spectrum restores the asymptotic Hagedorn route.
- The bounce action and $I$-condition kill present-day nucleation and low-action rescue windows.
- The relic-abundance problem compresses to the Y-discriminant.

The current numerical branch result is clear:
$$
\boxed{Y\approx 10^{198}\gg 1 \Rightarrow \text{Path 2B nonthermal relic.}}
$$
This is the strongest current conclusion of the program.

What is still open is not the branch, but the final degree of endogeneity and several outward-facing extensions. The key remaining tasks are:

1. make the derivation of $m_\Psi$, $E_0$, and $g$ fully unit-clean and externally auditable,
2. determine which Path 2B mechanism generated the relic population,
3. compute the vacuum/matter partition of the total loop abundance,
4. audit the SHA carry-fraction claim with a dedicated notebook,
5. integrate the Nexus-Friedmann system against current cosmological likelihoods.

The result is therefore not “everything is done.” It is more precise:
$$
\boxed{
\text{the CLG core is solved enough that the remaining open set is explicit, small, and computationally attackable.}
}
$$

---

## References

1. Lovelock, D. (1971). *The Einstein tensor and its generalizations.*
2. Synge, J. L. (1957). *The Relativistic Gas.*
3. Corless, R. M. et al. (1996). *On the Lambert W Function.*
4. Trodden, M. & Carroll, S. M. *TASI Lectures: Introduction to Cosmology* — thermal relics.
5. QuHarmonics internal corpus: current CLG, Y-discriminant, Path 2B, and Nexus extension documents.
