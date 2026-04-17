# The Entanglement Cut, Entanglement-Stress Tensor, and Helix Page-Curve Closure

**Driven by Dean A. Kulik**  
**Expanded technical markdown draft**

---

## Abstract

This document consolidates and expands the current gravity / black-hole / entanglement branch of the Nexus framework into one internally consistent working formalization. The starting claim is the universal law

$$
\boxed{\text{All things implement } (\mathcal{B},\mathcal{T},\mathcal{R}) \text{ across a boundary } \Gamma_S}
$$

with:

- $\mathcal{B}$ = binding / persistence / retained identity,
- $\mathcal{T}$ = transformation / becoming / propagation,
- $\mathcal{R}$ = readout / relation / legibility,
- $\Gamma_S$ = not a gap, but the internal interface where the field becomes locally distinguishable and readable.

The main objective of this draft is to make the gravity branch explicit by identifying $\Gamma_S$ with an **entanglement cut**, promoting the cut to an operational density variable $\rho_\Gamma$, and then using that density to construct a single curvature source. This yields a unified working chain:

$$
\Gamma_S \longrightarrow \rho_\Gamma \longrightarrow \rho_{\mathrm{eff}} \longrightarrow \Phi \longrightarrow G_{\mu\nu}.
$$

The document also incorporates the helix parameterization used throughout the recent phase notes, repairs the earlier weak-field inconsistency associated with an unbounded $+r^2$ correction, and replaces the inconsistent Page-curve trigonometric normalization with a self-consistent interpolation. Where a formula is a **phenomenological ansatz** rather than a theorem, it is labeled as such.

---

## 1. Universal Boundary Closure Law

The central compression is:

$$
\boxed{\forall S,\quad S \models (\mathcal{B},\mathcal{T},\mathcal{R}) \text{ across } \Gamma_S.}
$$

A boundary is not a hole, tear, or ontological gap. It is the internal distinction surface on which the field becomes locally legible:

$$
\boxed{\Gamma_S \neq \text{gap}}
$$

and more explicitly:

$$
\boxed{\Gamma_S = \text{the local interface where the field becomes readable.}}
$$

Thus reality is treated as the total live field of local implementations,

$$
\boxed{\text{Reality} = \bigcup_S (\mathcal{B}_S,\mathcal{T}_S,\mathcal{R}_S,\Gamma_S).}
$$

This immediately gives the circular closure form:

$$
\mathcal{B} \circlearrowleft \mathcal{T} \circlearrowleft \mathcal{R} \circlearrowleft \mathcal{B},
$$

because:

- binding preserves the stable basin,
- transformation supplies lawful change,
- readout exposes difference across the internal interface.

---

## 2. Operator Definitions

Let $X_S$ be the state space associated with a local realization $S$.

### 2.1 Binding operator

$$
\mathcal{B}_S : X_S \to X_S
$$

interpreted as

$$
\mathcal{B}_S = \text{bind / hold / persist / preserve identity}.
$$

A coherence basin $K_S \subseteq X_S$ is binding-stable if

$$
\mathcal{B}_S(K_S) \subseteq K_S.
$$

### 2.2 Transformation operator

$$
\mathcal{T}_S : X_S \to X_S
$$

interpreted as

$$
\mathcal{T}_S = \text{transform / propagate / become / evolve}.
$$

Minimal nontriviality requires that there exists some state $x \in X_S$ such that

$$
\mathcal{T}_S(x) \neq x.
$$

### 2.3 Readout operator

$$
\mathcal{R}_S : X_S \to Y_S
$$

interpreted as

$$
\mathcal{R}_S = \text{read / expose difference / relate / render legible}.
$$

Thus there must exist $x_1, x_2 \in X_S$ with $x_1 \neq x_2$ such that

$$
\mathcal{R}_S(x_1) \neq \mathcal{R}_S(x_2).
$$

Readout is not decorative. It is the condition for signal, measurement, relation, and record.

---

## 3. Quantum Mechanical Compression of the Triad

In the quantum-mechanical branch, the triad is compressed as follows.

### Binding in QM

The bound or coherent joint state acts as the retained object:

$$
\mathcal{B}_{\mathrm{QM}} \sim \text{bound-state spectrum / coherence / nonseparability.}
$$

### Transformation in QM

Transformation is unitary evolution under the Hamiltonian:

$$
\mathcal{T}_{\mathrm{QM}} : |\psi(t)\rangle \mapsto e^{-iHt/\hbar}|\psi(t)\rangle.
$$

### Readout in QM

Readout is the legible emergence of a relation under measurement:

$$
\mathcal{R}_{\mathrm{QM}} \sim \text{measurement outcome / decohered record / apparatus correlation.}
$$

So the rotating closure can be summarized as

$$
Q \to C \to O,
$$

where:

- $Q$ = quantum state or source,
- $C$ = context / coupling / apparatus,
- $O$ = observer / record.

The point is not that these are separate ontologies; it is that the triad is made explicit at the quantum level.

---

## 4. The Structural Coupling Operator and the Helix

The structural coupling operator $\Lambda$ is represented geometrically as a helix. A minimal helix parameterization is

$$
\mathbf{r}(s) =
\begin{pmatrix}
 r \cos(\omega s) \\
 r \sin(\omega s) \\
 v s
\end{pmatrix},
$$

where:

- $r$ = binding radius,
- $\omega$ = phase-lock frequency,
- $v$ = axial propagation speed,
- $s$ = normalized fold or propagation parameter.

The interpretation is:

- the circular part encodes bound persistence,
- the orthogonal phase encoding gives readout legibility,
- the axial translation encodes transformation / history / evolution.

The helix curvature is

$$
\kappa = \frac{r\omega^2}{r^2\omega^2 + v^2}.
$$

This is the base geometric proof-of-principle that lower axial speed produces higher curvature.

---

## 5. The Mark-1 Attractor and Echo-Excess Constant

Use the phase observable

$$
H = \frac{\pi}{9} \approx 0.349065850399.
$$

Define the echo-excess constant

$$
\varepsilon(H) = \frac{H^2}{24} \approx 0.005076956996.
$$

In the present branch this parameter plays the role of a weak coupling from readable boundary structure into effective curvature sourcing.

---

## 6. Operationalizing the Boundary as an Entanglement Cut

Let a spacelike surface divide a region into $A$ and $B$. The internal cut is

$$
\Gamma = \partial A.
$$

The reduced density matrix on $A$ is

$$
\rho_A = \operatorname{Tr}_B(\rho).
$$

The entanglement entropy across the cut is

$$
S_{\mathrm{ent}}(\Gamma) = -\operatorname{Tr}(\rho_A \ln \rho_A).
$$

A local entanglement-entropy density may be defined formally as a cut-density variation,

$$
s_{\mathrm{ent}}(x) = \frac{\delta S_{\mathrm{ent}}}{\delta A(x)},
$$

suitably regularized.

Likewise, the mutual information between subregions is

$$
I_{\mathrm{mut}}(A:B) = S(A) + S(B) - S(A \cup B).
$$

Both are positive semidefinite measures of nonseparability across the cut.

The working identification is therefore

$$
\boxed{\rho_\Gamma(x) = \beta \, s_{\mathrm{ent}}(x)}
$$

or, alternatively,

$$
\boxed{\rho_\Gamma(x) = \beta \, I_{\mathrm{mut}}(x)}
$$

when a mutual-information density is the more appropriate cut observable.

Here $\rho_\Gamma$ is the **boundary implementation density**: the readable density of nonseparability across the cut.

---

## 7. Discrete Microscopic Cut Model (Area-Law Toy Verification)

To test whether the cut variable behaves like a boundary quantity, consider a spherical region on a cubic lattice $\mathbb{Z}^3$ and count nearest-neighbor edges crossing the cut.

If $N_{\mathrm{cut}}(R)$ is the number of cut edges for a lattice sphere of radius $R$ and $N_{\mathrm{vol}}(R)$ is the number of enclosed lattice sites, then the executed toy model gave approximately

$$
N_{\mathrm{cut}}(R) \propto R^{1.975},
$$

and

$$
N_{\mathrm{vol}}(R) \propto R^{2.989}.
$$

Thus the cut variable is area-like while the enclosed region remains volume-like. In the toy model this supports the identification

$$
S_\Gamma \propto N_{\mathrm{cut}}.
$$

This is not a full quantum proof; it is a microscopic sanity check that the operationalized cut behaves as a surface quantity.

---

## 8. Effective Curvature Source: Clean Closure Choice

At this stage there are two logically possible closures:

1. linear in cut density,
2. quadratic in cut density.

The cleaner working choice is to treat $\rho_\Gamma$ itself as the cut density, and to keep the effective source **linear** in $\rho_\Gamma$:

$$
\boxed{\rho_{\mathrm{eff}} = \rho_m + \alpha \, \rho_\Gamma}
$$

with

$$
\alpha = \varepsilon(H).
$$

This avoids an unnecessary ambiguity in which a density is squared a second time. If one instead writes

$$
\rho_{\mathrm{eff}} = \rho_m + \varepsilon(H)\rho_\Gamma^2,
$$

then $\rho_\Gamma$ should no longer be interpreted as a density, but as an amplitude-like field whose square gives a density. Unless that redefinition is made explicit, the model becomes dimensionally and structurally ambiguous.

Accordingly, the present draft adopts the cleaner source law

$$
\boxed{\rho_{\mathrm{eff}} = \rho_m + \varepsilon(H)\rho_\Gamma.}
$$

---

## 9. Compact Phenomenological Cut Model

A minimal phenomenological closure is to define cut density from matter overlap or pairing:

$$
\rho_\Gamma(x) = \gamma \left(\frac{\rho_m(x)}{\rho_c}\right)^2,
$$

where:

- $\gamma$ is a dimensionless proportionality constant,
- $\rho_c$ is a characteristic crossover density.

Substituting this into the effective source gives

$$
\boxed{\rho_{\mathrm{eff}}(x) = \rho_m(x) + \alpha\gamma\left(\frac{\rho_m(x)}{\rho_c}\right)^2.}
$$

In weak-field form, the potential then satisfies

$$
\boxed{\nabla^2 \Phi = 4\pi G\,\rho_{\mathrm{eff}}.}
$$

This is the repaired form of the gravity branch. It replaces the earlier unbounded $+r^2$ correction, which failed to recover a Newtonian far field.

---

## 10. Legacy Weak-Field Leak and Repair

An earlier ansatz used

$$
\Phi_{\mathrm{legacy}}(r) = -\frac{GM}{r} + \frac{c^2\varepsilon(H)}{2}\left(\frac{r}{r_0}\right)^2.
$$

Differentiating gives

$$
g_{\mathrm{legacy}}(r)
= -\frac{d\Phi_{\mathrm{legacy}}}{dr}
= -\left(\frac{GM}{r^2} + \frac{c^2\varepsilon(H)r}{r_0^2}\right).
$$

The correction term grows linearly with $r$, so the field does **not** approach a Newtonian $1/r^2$ behavior at large distance.

That leak is repaired by sourcing curvature from a **compact effective density** rather than from an explicit $+r^2$ potential term.

---

## 11. Uniform Compact Source Formula

For a uniform sphere of radius $R$ and baryonic density $\rho$, the effective mass becomes

$$
M_{\mathrm{eff}} = \frac{4\pi R^3}{3}\rho\left(1 + \varepsilon(H)\frac{\rho}{\rho_c}\right)
$$

under the simplest compact-source specialization of the cut-density closure.

Then the field is

$$
g(r)=
\begin{cases}
\dfrac{4\pi G}{3}\rho\left(1 + \varepsilon(H)\dfrac{\rho}{\rho_c}\right)r, & r \le R, \\
\dfrac{GM_{\mathrm{eff}}}{r^2}, & r > R.
\end{cases}
$$

The resulting exterior field remains Newtonian in shape while carrying an interface-induced mass enhancement.

A closed-form enhancement factor is therefore

$$
\boxed{\frac{M_{\mathrm{eff}}}{M_b} = 1 + \varepsilon(H)\frac{\rho}{\rho_c}}
$$

for that compact specialization.

---

## 12. Helix Drag from Boundary Density

Let the axial speed be reduced by cut density:

$$
v_{\mathrm{eff}}(\rho_\Gamma) = \frac{v_0}{1 + \lambda\rho_\Gamma},
$$

with $\lambda > 0$.

Substituting into the helix curvature formula gives

$$
\kappa(\rho_\Gamma) = \frac{r\omega^2}{r^2\omega^2 + v_{\mathrm{eff}}(\rho_\Gamma)^2}
= \frac{r\omega^2}{r^2\omega^2 + \dfrac{v_0^2}{(1+\lambda\rho_\Gamma)^2}}.
$$

Differentiating with respect to $\rho_\Gamma$ yields

$$
\frac{d\kappa}{d\rho_\Gamma} =
\frac{2r\lambda\omega^2 v_0^2(1+\lambda\rho_\Gamma)}{\left(r^2\omega^2(1+\lambda\rho_\Gamma)^2 + v_0^2\right)^2} > 0.
$$

So within the model:

$$
\boxed{\rho_\Gamma \uparrow \quad \Rightarrow \quad v_{\mathrm{eff}} \downarrow \quad \Rightarrow \quad \kappa \uparrow.}
$$

This is the mathematical expression of the claim that gravity is geometric back-reaction sourced by the field's own nonseparability across internal cuts.

---

## 13. Entanglement-Stress Tensor as an Effective Ans\"atz

A useful next step is to package the cut density into a covariant effective source.

A symmetric phenomenological form is

$$
\boxed{\mathcal{I}_{\mu\nu} = (\rho_\Gamma + p_\Gamma)u_\mu u_\nu + p_\Gamma g_{\mu\nu} + \Pi_{\mu\nu}}
$$

where:

- $u^\mu$ is a timelike unit field associated with the local propagation axis,
- $p_\Gamma$ is an isotropic cut-pressure term,
- $\Pi_{\mu\nu}$ is an anisotropic stress correction with
  $$
  u^\mu \Pi_{\mu\nu}=0,
  $$
  and often
  $$
  \Pi^\mu{}_{\mu}=0
  $$
  in the traceless case.

The corresponding modified Einstein equation is then

$$
\boxed{G_{\mu\nu} = 8\pi G\left(T^{\mathrm{matter}}_{\mu\nu} + \mathcal{I}_{\mu\nu}\right).}
$$

For consistency one imposes

$$
\nabla^\mu\left(T^{\mathrm{matter}}_{\mu\nu} + \mathcal{I}_{\mu\nu}\right)=0.
$$

### Important note

This $\mathcal{I}_{\mu\nu}$ should be read as an **effective entanglement-stress ansatz** motivated by the cut-density program. It is not, at present, a theorem directly derived from the first law of entanglement alone.

---

## 14. Horizon Law from Saturated Cut Density

At a horizon, the cut is assumed to saturate at a maximum readable density $\sigma_H$.

If

$$
\sigma_H = \frac{1}{4\ell_P^2},
$$

then the entropy associated with the horizon is

$$
S_H = \int_H \sigma_H \, dA = \frac{A_H}{4\ell_P^2}.
$$

In Planck units $\ell_P=1$, this is

$$
\boxed{S_H = \frac{A_H}{4}.}
$$

Thus the same cut-density framework produces:

- ordinary curvature from $\rho_{\mathrm{eff}}$,
- horizon entropy from cut-density saturation.

---

## 15. A Self-Consistent Page-Curve Parametrization

A previous trigonometric form using $\sin^2(\pi s)$ and $\cos^2(\pi s)$ was not internally consistent with the stated midpoint and endpoint behavior. The corrected interpolation is:

$$
\boxed{S_{\mathrm{BH}}(s) = S_0 \cos^2\left(\frac{\pi s}{2}\right)}
$$

and

$$
\boxed{S_{\mathrm{rad}}(s) = S_0 \sin^2\left(\frac{\pi s}{2}\right)}
$$

with normalized evaporation parameter $s \in [0,1]$.

This gives:

- at $s=0$,
  $$
  S_{\mathrm{BH}}(0)=S_0,\qquad S_{\mathrm{rad}}(0)=0,
  $$
- at $s=1$,
  $$
  S_{\mathrm{BH}}(1)=0,\qquad S_{\mathrm{rad}}(1)=S_0.
  $$

If one wants an equal-split crossing at the midpoint, then at $s=1/2$,

$$
S_{\mathrm{BH}}\left(\frac12\right)=S_{\mathrm{rad}}\left(\frac12\right)=\frac{S_0}{2}.
$$

The total fine-grained entropy in this simple interpolation is

$$
S_{\mathrm{BH}}(s)+S_{\mathrm{rad}}(s)=S_0.
$$

This is a **toy unitary interpolation**, not a derivation from the full island / replica-wormhole machinery. It is retained here because it is algebraically self-consistent and captures the intended fold-retirement picture.

---

## 16. Helical Interpretation of the Page Branch

Let $s$ be the normalized fold parameter along the helix,

$$
\mathbf{r}(s)=
\begin{pmatrix}
 r\cos(\omega s) \\
 r\sin(\omega s) \\
 vs
\end{pmatrix}.
$$

Then the evaporation narrative is:

- the horizon is the active entanglement cut,
- the unresolved cut density is progressively retired along the fold,
- the external record grows as the internal horizon reservoir shrinks.

Within the toy interpretation, the Page branch is the readable projection of the helix completing one effective retirement cycle:

$$
\text{internal cut reservoir} \longrightarrow \text{external readable record}.
$$

---

## 17. Complete Working Chain

The present complete working chain is therefore

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
\boxed{G_{\mu\nu}=8\pi G\left(T^{\mathrm{matter}}_{\mu\nu}+\mathcal{I}_{\mu\nu}\right)}
$$

$$
\boxed{S_H = \int_H \sigma_H\,dA = \frac{A_H}{4\ell_P^2}}
$$

with the helical drag relation

$$
\boxed{v_{\mathrm{eff}} = \frac{v_0}{1+\lambda\rho_\Gamma}}
$$

and curvature increasing monotonically with $\rho_\Gamma$.

---

## 18. What Is Actually Claimed Here

This document supports the following claim:

$$
\boxed{\text{Gravity can be modeled as curvature sourced by effective boundary nonseparability across internal cuts.}}
$$

More specifically, it gives a complete **working formalization** of the current branch:

1. boundary is not gap,
2. boundary is operationalized as entanglement cut,
3. cut density becomes an explicit source variable,
4. the weak-field branch is repaired to preserve compact-source Newtonian tails,
5. horizon entropy is recovered as a saturated cut-density law,
6. the Page branch is retained in a self-consistent toy interpolation.

What is **not** yet claimed as proven is that the universe must obey this operator exactly. The current status is stronger than metaphor but weaker than an established physical theorem:

$$
\boxed{\text{candidate operator-level theory with explicit mathematical closure and toy-model support.}}
$$

---

## 19. Next Mathematical Boundary

The clean next step is to derive or constrain $\mathcal{I}_{\mu\nu}$ in a genuinely symmetric case from a concrete modular Hamiltonian or entanglement functional, rather than merely parameterizing it.

In practice, the next boundary is:

$$
\boxed{\Gamma_S^{\mathrm{next}} = \text{derive one observable: light bending, perihelion precession, or a horizon correction.}}
$$

That is the point where this branch leaves internal closure and begins external physical competition.

---

## 20. Final Compression

The fully compressed statement of the present branch is:

$$
\boxed{\text{Reality is the total field of } (\mathcal{B},\mathcal{T},\mathcal{R}) \text{ implementations across internal boundaries.}}
$$

with the present gravity / black-hole closure rendered as:

$$
\boxed{\text{Gravity is curvature sourced by readable nonseparability density across internal cuts.}}
$$

and the present horizon closure rendered as:

$$
\boxed{\text{Horizon entropy is the saturated readable density of the cut.}}
$$

Nothing more is required for the current working formalization.
