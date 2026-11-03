# Mathematical foundations for dual-null ontology

**Established mathematics and physics provide substantial—though not complete—support for a framework built on two orthogonal null states generating dynamics through phase relationship.** The strongest support comes from split-complex numbers (two genuinely distinct null elements), general relativity's double-null formalism (asymmetric null directions), and the ubiquitous Φ² + E² = 1 constraint appearing across physics. The concept of "gaps as phase relationships" finds rigorous expression in Berry phase, complementarity, and action-angle variables. However, **π/9 ≈ 0.35 does not appear as a known stability threshold** in dynamical systems literature.

---

## Split-complex numbers provide the clearest "two types of zero"

The most direct mathematical realization of "two orthogonal null states with distinct properties" appears in **split-complex numbers**, an extension of real numbers by element j where j² = +1 (but j ≠ ±1). This algebra contains two idempotent elements:

**e₊ = (1+j)/2** and **e₋ = (1-j)/2**

These satisfy remarkable properties: **e₊² = e₊** and **e₋² = e₋** (idempotent), **e₊ · e₋ = 0** (orthogonal), and **e₊ + e₋ = 1** (they span the algebra). Both lie on the "light cone" where the indefinite norm |z|² = x² - y² = 0, yet neither equals zero. Any element z can be decomposed as z = ae₊ + be₋, with the two null directions serving as orthogonal projections.

The physical interpretation connects directly to spacetime: split-complex numbers naturally model **1+1 dimensional Minkowski space**, where e₊ and e₋ correspond to future and past light cone directions. Evolution (hyperbolic rotation) mixes these null components, and the "drive" or dynamics emerges from asymmetry between them. This provides exactly the mathematical structure where two distinct nulls generate physical content through their relationship.

Related algebraic structures include **dual numbers** (where ε² = 0 creates a single nilpotent direction), **hyper-dual numbers** (two nilpotent elements ε₁ and ε₂ with ε₁² = ε₂² = 0 but ε₁ε₂ ≠ 0), and **Belnap's four-valued logic** with two distinct indeterminate values (⊥ = "neither true nor false" and ⊤ = "both true and false").

---

## Double-null coordinates in general relativity encode asymmetric causal structure

General relativity's **double-null formalism** provides physical embodiment of dual null states. Defining null coordinates u = t − r (retarded/outgoing) and v = t + r (advanced/ingoing), the metric takes the form ds² = −Ω²dudv + r²dΩ². These coordinates are **not symmetric**—u labels outgoing light cones while v labels ingoing ones, encoding fundamentally different causal directions.

The mathematical behavior when null coordinates vanish reveals distinct collapse modes:
- **u = 0 alone**: defines a 3-dimensional null hypersurface (future light cone through origin)
- **v = 0 alone**: defines a different 3-dimensional null hypersurface (past light cone)  
- **u = 0 AND v = 0**: reduces to a 2-sphere or point—the **bifurcation surface** where both null directions intersect

This distinction becomes physically crucial for **trapped surfaces**, defined by the signs of null expansions θ⁺ (outgoing) and θ⁻ (ingoing). A marginally outer trapped surface (MOTS) has θ⁺ = 0 with θ⁻ ≤ 0—one null direction "frozen" while the other converges. A fully trapped surface has **both θ⁺ < 0 and θ⁻ < 0**. The extremal case θ⁺ = θ⁻ = 0 defines the bifurcation surface of Killing horizons, a topologically special configuration.

Key references include Penrose's 1964 conformal treatment of infinity, Christodoulou and Klainerman's work on double-null stability of Minkowski space, and Hayward's analysis of how advanced and retarded conformal factors "vanish at past and future null infinity respectively, with both vanishing at spatial infinity."

---

## The constraint Φ² + E² = 1 pervades physics as circular conservation

The mathematical structure of "two orthogonal modes trading amplitude" appears throughout physics under the fundamental identity **sin²θ + cos²θ = 1**. This constraint manifests as:

| System | Conservation Form | Orthogonal Components |
|--------|------------------|----------------------|
| Simple harmonic oscillator | E = ½mv² + ½kx² | Kinetic and potential energy |
| Qubit state (Bloch sphere) | \|α\|² + \|β\|² = 1 | Amplitudes for \|0⟩ and \|1⟩ |
| Polarization (Poincaré sphere) | S₀² = S₁² + S₂² + S₃² | Stokes parameters |
| Electromagnetic wave | u ∝ ε₀E² + B²/μ₀ | Electric and magnetic energy |
| Phase space | H = (p² + ω²q²)/2m | Momentum and position |

The transformation to **action-angle variables** (θ, I) in Hamiltonian mechanics makes this structure explicit: the action I remains constant while the angle θ advances uniformly, with original coordinates becoming projections x = √(2I/mω)sin(θ) and p = √(2mωI)cos(θ). All periodic motion is circular motion viewed through different projections.

**Berry phase** provides the deepest vindication of "gaps as phase relationships, not absences." When a quantum system traverses a closed loop in parameter space, it accumulates geometric phase γ = i∮⟨ψ|∇|ψ⟩·dR even when returning to its initial state. This phase—**not zero despite the apparent "gap" of returning to the start**—encodes the solid angle subtended and produces observable effects (Aharonov-Bohm, Pancharatnam phase). Similarly, holonomy in differential geometry shows a vector parallel-transported around a closed curve returns rotated, with the rotation angle measuring enclosed curvature.

The complementarity principle formalizes this reciprocity: a "gap" (zero spread) in one variable requires infinite spread in the conjugate variable. A node in a standing wave has zero amplitude but maximum slope; destructive interference shows zero intensity but maximum phase information.

---

## Pythagorean geometry distinguishes two collapse modes

The Pythagorean constraint a² + b² = c² creates **asymmetric collapse behaviors** when different components vanish:

**Leg collapse (a → 0 or b → 0)**: The triangle degenerates to a line segment with **b = c** or **a = c**. One degree of freedom remains—a 1-dimensional residue with zero area but finite length.

**Hypotenuse collapse (c → 0)**: The constraint becomes a² + b² = 0, which for positive reals forces **a = b = 0**—total collapse to a point. This is a **0-dimensional residue**, topologically distinct from leg collapse.

This asymmetry has profound implications in non-Euclidean geometry. The Minkowski metric ds² = dx² − c²dt² (signature +,−) allows **c² = 0 with non-zero spatial and temporal separations**—the lightlike interval. In Euclidean geometry, the "hypotenuse" (interval) vanishing forces all components to vanish; in Minkowski geometry, the null cone permits non-trivial solutions. This is precisely "two types of zero" manifesting in the metric signature.

The **Theodorus spiral** demonstrates how Pythagorean constraints generate indexing: starting with a 1-1-√2 triangle, each step attaches a new right triangle with unit leg, producing hypotenuses √1, √2, √3, √4... The constraint **self-validates** at each step, creating an enumeration of all square roots through pure geometry.

---

## Frame-dependent irreversibility has rigorous mathematical foundations

The distinction between "non-invertible globally" and "non-invertible relative to frame" appears across mathematics and physics, though not under a single unified name:

**Coordinate singularities vs. true singularities**: The Schwarzschild metric appears singular at r = 2GM, where coordinates break down and crossing the horizon seems to require infinite time. However, transforming to **Kruskal-Szekeres coordinates** reveals this as a coordinate artifact—the Kretschmann scalar K = 48G²M²/r⁶ remains finite there. The "irreversibility" of horizon crossing in Schwarzschild coordinates becomes regular evolution in Kruskal coordinates. Only at r = 0, where curvature invariants diverge, does genuine irreversibility occur.

**Local vs. global invertibility**: The complex exponential exp(z) has non-vanishing Jacobian everywhere (locally invertible) but is globally non-invertible due to periodicity. Multi-valued functions like √z appear "irreversible" on the complex plane but become single-valued on the appropriate **Riemann surface**—a covering space that resolves the apparent multi-valuedness.

**Observer-dependent entropy**: Recent work (Physical Review Letters 134, 2024) demonstrates that "entropy production is strongly observer dependent and deeply connects the arrow of time with the causal structure of spacetime." Using Fermi normal coordinates and quantum fluctuation theorems, researchers showed different families of observers disagree on entropy production magnitude, though not direction.

**Category-theoretic formalization**: In certain categories, morphisms can be both **monic** (injective) and **epic** (surjective) without being isomorphisms. The inclusion ℤ ↪ ℚ is both monic and epic but not an isomorphism—"irreversibility" depends on categorical context.

---

## Stability thresholds involve universal constants but not π/9

**No established dynamical systems literature identifies π/9 ≈ 0.349 as a stability threshold.** The value 40° (one-ninth of a circle) does not appear as a special angle in mode-locking, bifurcation theory, or control systems.

The closest values with mathematical significance include **1/e ≈ 0.368** (natural decay constant, representing 37% remaining after one time constant) and **1/3 ≈ 0.333** (a significant mode-locking rotation number). Neither matches π/9 precisely.

Established universal thresholds in nonlinear dynamics include:

- **Feigenbaum δ ≈ 4.669**: Ratio of successive bifurcation intervals in period-doubling cascades, universal across systems with quadratic maxima
- **Feigenbaum α ≈ 2.502**: Spatial scaling factor in period-doubled attractors
- **Golden ratio φ ≈ 1.618**: The "most irrational" number, corresponding to the last KAM torus to break under perturbation
- **Critical damping ζ = 1**: Boundary between oscillatory and overdamped response
- **λ = 0** (Lyapunov exponent): The edge of chaos separating stable from chaotic dynamics

**Arnold tongues** describe mode-locking regions where driven oscillators synchronize to rational rotation numbers p/q. The largest tongues occur at Farey fractions (1/2, 1/3, 2/3...), with 1/9 producing a tongue but not a specially privileged one. KAM theory shows that orbits with golden-ratio frequency relationships exhibit maximum stability against perturbation.

---

## Key papers and frameworks supporting dual-null ontology

**Split-complex algebra and spacetime structure:**
- Yaglom, I.M. "A Simple Non-Euclidean Geometry and Its Physical Basis" (1979)
- Catoni et al. "The Mathematics of Minkowski Space-Time" (2008)

**Double-null formalism in general relativity:**
- Newman & Penrose (1962) "An Approach to Gravitational Radiation by a Method of Spin Coefficients"
- Christodoulou & Klainerman "The Global Nonlinear Stability of the Minkowski Space" (1993)
- Hayward (gr-qc/0307028) "Spatial and null infinity via advanced and retarded conformal factors"

**Berry phase and geometric phase:**
- Berry, M.V. (1984) "Quantal phase factors accompanying adiabatic changes" Proc. Roy. Soc. A392
- Shapere & Wilczek "Geometric Phases in Physics" (1989)

**Phase space and action-angle methods:**
- Arnold, V.I. "Mathematical Methods of Classical Mechanics" (1978)
- Goldstein, Poole, Safko "Classical Mechanics" (2002)

**Observer-dependent irreversibility:**
- Phys. Rev. Lett. 134, 050406 (2024) "Quantum Detailed Fluctuation Theorem in Curved Spacetimes"

---

## Conclusion

The proposed framework finds substantial mathematical grounding in existing structures. **Split-complex numbers** provide genuine "two types of null" with orthogonal properties and connection to spacetime causal structure. **General relativity's double-null formalism** shows how asymmetric null directions generate physical structure including horizons and trapped surfaces. The **Φ² + E² = 1 constraint** pervading physics confirms that orthogonal modes trade amplitude under circular conservation, with **Berry phase** rigorously demonstrating that apparent "gaps" encode geometric relationships. **Pythagorean geometry** distinguishes leg-collapse from hypotenuse-collapse as topologically distinct degenerations, a distinction amplified by Minkowski signature.

The weakest support concerns π/9 ≈ 0.35 as a stability threshold—this specific value does not appear in established dynamical systems theory. If this constant plays a role in the framework, it may arise from domain-specific constraints rather than universal mathematics.

The mathematical infrastructure for a "three-way switch" with dual orthogonal nulls generating drive through phase relationship exists and is well-developed, scattered across relativity, algebra, quantum mechanics, and geometry. What the literature lacks is a unified treatment synthesizing these structures into a single ontological framework—precisely the gap the proposed model aims to fill.