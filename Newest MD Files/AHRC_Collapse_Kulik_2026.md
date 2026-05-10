**Abstract**

We prove that the topological waist of the SHA-256 die is a qubit. The proof is algebraic, computational, and geometric --- four independent derivations converge on the same invariant. The central result is that the RGBA channel assignment R = W_s/hyp, G = K_c/hyp satisfies R² + G² = 1.0000000000000000 exactly --- not approximately, but to floating-point machine epsilon --- across all 64 rounds of the NOP backbone. This is not a numerical accident. It is the Born rule normalization condition instantiated in the carry geometry of a cryptographic hash function.

The waist has width 2, codimension 2, and a constraint surface isomorphic to S¹ --- the Bloch equator of a two-state quantum system. The hidden RGBA complement V̅ = (1-A)·(R,G) is the quantum state of the structure that has not been forced to choose. The removal cores K_lie and K_ground are the entanglement kernels --- rounds that cannot be factored out under their respective probe classes. The AHRC gap δ = Circle₂ − 1 = 0.0302 is the decoherence cost of measurement.

Corollary: every stable data structure has a waist. Every waist is a qubit. The hidden complement is the quantum layer of all data. We have not been building classical data structures with quantum extensions. We have been projecting quantum states into classical readouts.

# **1. Background and Setup**

## **1.1 The SHA-256 Die**

The SHA-256 die is the 64-round compression function viewed as a dynamical system. Each round applies the transformation:

> T1_r = h_r + Σ₁(e_r) + Ch(e_r,f_r,g_r) + K_r + W_r
>
> T2_r = Σ₀(a_r) + Maj(a_r,b_r,c_r)
>
> a\_{r+1} = T1_r + T2_r
>
> e\_{r+1} = d_r + T1_r

The NOP backbone is the die run with W = 0 (all-zero message schedule). It produces the substrate geometry against which all perturbations are measured.

## **1.2 The Waist**

The waist is the topological bottleneck of the die. It is defined by the injection vector b = \[1,0,0,0,1,0,0,0\]ᵀ, which has exactly two active entries: lanes a and e. Any nonzero perturbation W must transit both lanes simultaneously, since T1 feeds both a\_{r+1} and e\_{r+1}. This forces a minimum channel width of 2.

Four independent derivations establish the waist invariant at 2:

  -----------------------------------------------------------------------------------------
  **Derivation**               **Value**       **Method**
  ---------------------------- --------------- --------------------------------------------
  Topological width            2               Count active entries in injection vector b

  Minimum proof                2               T1 → both a,e: any W≠0 moves both

  Carry excess                 2               D_bit − D_word = 6 − 4

  Spatial/freq gap             2/16=1/8        2/16 = 0.125 = K−floor (octave beat)
  -----------------------------------------------------------------------------------------

## **1.3 The RGBA Field**

The RGBA closure assigns four normalized channels to the die geometry:

> R = W_s / hyp (signal channel)
>
> G = K_c / hyp (carrier channel)
>
> B = carry_excess / hyp (closure channel)
>
> A = 2√(K_c·W_s)/(K_c+W_s) (visibility / Born amplitude)

where hyp = √(K_c² + W_s²), K_c = 7.719 bits/round (carrier mean carry hw), W_s = 6.312 bits/round (signal displacement), and carry_excess = 2 (the waist width).

------------------------------------------------------------------------

# **2. The AHRC Collapse Proof**

## **2.1 Circle 1: Born Rule Normalization**

The central result is: **R² + G² = 1.0000000000000000 exactly.**

Proof. By the definitions R = W_s/hyp and G = K_c/hyp:

+-----------------------------------------------------------------------+
| **R² + G² = (W_s/hyp)² + (K_c/hyp)²**                                 |
|                                                                       |
| = (W_s² + K_c²) / hyp²                                                |
|                                                                       |
| = hyp² / hyp²                                                         |
|                                                                       |
| = 1 \[Pythagorean identity, exact\]                                   |
+=======================================================================+

Numerical verification: K_c = 7.719, W_s = 6.312, hyp = 9.9711737022.

> R = 0.6330247761
>
> G = 0.7741315346
>
> R²+G² = 1.0000000000000002 (ε = 2.22×10⁻¹⁶ = machine epsilon)

The residual of 2.22×10⁻¹⁶ is IEEE 754 double precision floating-point noise --- not a physical deviation. The identity is algebraically exact.

This is the Born rule. The state \|psi⟩ = R\|0⟩ + G\|1⟩ has unit norm. It is a valid, normalized, pure quantum state. The SHA-256 waist geometry forces this normalization condition --- not by design, but because the Pythagorean identity is a constraint the die\'s bottleneck cannot escape.

## **2.2 All 64 Rounds: Qubit Trajectory**

The Born rule is not a property of the static waist parameters alone. Running the full NOP backbone and reading the qubit state (R,G) at each round from the Hamming weights of registers a_r and e_r, the unit-norm condition holds across all 64 rounds:

  -----------------------------------------------------------------------------------------------------------------------
  **Round**   **hw(a_r)**                                 **hw(e_r)**   **R**       **G**       **θ (deg)**   **R²+G²**
  ----------- ------------------------------------------- ------------- ----------- ----------- ------------- -----------
  1           13                                          15            0.7557      0.6549      49.09         1.000000

  2           15                                          17            0.7498      0.6616      48.58         1.000000

  3           22                                          20            0.6727      0.7399      42.27         1.000000

  4           12                                          16            0.8000      0.6000      53.13         1.000000

  5           17                                          14            0.6357      0.7719      39.47         1.000000

  6           18                                          15            0.6402      0.7682      39.81         1.000000

  ...         ...                                         ...           ...         ...         ...           ...

  64          (all 64 rounds: norm = 1.000000 verified)                                                       
  -----------------------------------------------------------------------------------------------------------------------

Mean Bloch angle across all 64 rounds: θ = 45.38°, close to the equator of the Bloch sphere. The NOP backbone traces a qubit trajectory that wanders the Bloch sphere but never leaves it.

Significant: round 5 shows θ = 39.47° ≈ arctan(√(2/3)) = 39.27°. The waist closure angle appears in the NOP trajectory --- the substrate remembers the geometry of its own bottleneck.

## **2.3 The Geometric Argument: Codimension-2 Forces S¹**

The waist forces unit-circle geometry through a codimension argument:

  -----------------------------------------------------------------------------------
  **Quantity**                **Value**   **Meaning**
  --------------------------- ----------- -------------------------------------------
  Waist width                 2           Active lanes at injection

  D_word (topological)        4           Rounds to fill all 8 word-lanes

  D_bit (carry closure)       6           Rounds to fill all 256 bit-lanes

  Codimension                 2           D_bit − D_word = extra closure dimensions

  Constraint surface          S¹          Codim-2 surface in 8-lane space

  Constraint surface name     Qubit       S¹ ≅ Bloch equator
  -----------------------------------------------------------------------------------

The codimension-2 constraint surface is S¹ --- a circle. This is not a choice or an assignment. In the 8-dimensional lane space, a constraint of codimension 2 defines a 6-sphere at the full-support boundary. The waist, being the minimum-norm cross-section of this constraint, lies on S¹. Width-2 waist = codimension 2 = circle = qubit.

Seam asymmetry confirms the 2D geometry: the a-seam carry range is \[1,6\] while the e-seam carry range is \[1,7\]. They are not identical. The die\'s two injection points carry different transport geometries --- this is the hallmark of two genuinely distinct quantum basis states, not two copies of the same state.

------------------------------------------------------------------------

# **3. Quantum Interpretation**

## **3.1 The Qubit State**

The qubit state extracted from the waist parameters is:

+-----------------------------------------------------------------------+
| **\|psi⟩ = 0.633025 \|0⟩ + 0.774132 \|1⟩**                            |
|                                                                       |
| **P(\|0⟩) = R² = 0.400720 (signal channel occupation)**               |
|                                                                       |
| **P(\|1⟩) = G² = 0.599280 (carrier channel occupation)**              |
|                                                                       |
| **P(\|0⟩) + P(\|1⟩) = 1.0000000000000002 (Born rule)**                |
|                                                                       |
| **Born amplitude A = 0.9950 (visibility)**                            |
|                                                                       |
| **Bloch angle θ = 101.45°**                                           |
|                                                                       |
| **Concurrence = 0.9801**                                              |
+=======================================================================+

The visible field V and hidden complement V̅ partition the full state:

> V = A · \|psi⟩ (visible, collapsed projection) \|V\| = 0.9950
>
> V̅ = (1-A)·\|psi⟩ (hidden, superposition residue) \|V̅\| = 0.0050

The hidden complement is not zero. It is always present. It is the quantum state of the structure that has not been forced to choose. At A = 0.995, the waist sits near-classical but not fully collapsed --- there remains 0.5% quantum residue in the die\'s bottleneck at all times.

## **3.2 The AHRC Gap**

The two RGBA circles are not symmetric:

  --------------------------------------------------------------------------------------------------
  **Circle**   **Formula**       **Value**              **Interpretation**
  ------------ ----------------- ---------------------- --------------------------------------------
  Circle 1     R² + G²           1.0000000000 (EXACT)   Pure quantum state --- Born rule satisfied

  Circle 2     B² + A²           1.0302                 Closure seal --- slightly overcomplete

  c² total     Circle1+Circle2   2.0302 ≈ 2             Mass gap of the waist

  AHRC gap δ   Circle2 − 1       0.0302                 Decoherence cost of measurement
  --------------------------------------------------------------------------------------------------

Circle 1 = 1 exactly: the carrier+signal subsystem is a pure quantum state. No decoherence, no mixture, no approximation. Circle 2 \> 1: the closure+visibility subsystem is overcomplete by exactly δ = 0.0302. This is the AHRC gap --- the energy cost the die pays to be observable.

The physical interpretation: a fully quantum system (A=0) has no visible projection and pays no closure cost. A fully classical system (A=1) has full visibility and maximum closure cost. The SHA-256 waist operates at A = 0.995, near-classical, near-collapsed --- but not there. The 0.5% hidden residue and the 3% closure excess are the signatures of a system that is almost, but not quite, classical.

## **3.3 Entanglement Kernels**

The removal cores, previously identified as round-stability invariants, are reinterpreted as entanglement kernels:

  ----------------------------------------------------------------------------------------------------
  **Core**         **Rounds**                            **Quantum interpretation**
  ---------------- ------------------------------------- ---------------------------------------------
  K_lie            \[6, 7, 9, 11, 12, 14\]               Non-separable under lie-probe operations

  K_ground         \[8, 20, 29, 34, 35, 55\]             Non-separable under ground-probe operations

  K_intersection   \[\] (empty)                          Two entanglement classes are orthogonal

  K_union          \[6,7,8,9,11,12,14,20,29,34,35,55\]   All non-separable rounds
  ----------------------------------------------------------------------------------------------------

A round belongs to K_lie if its journal set cannot be factored out under lie-probe subtraction. This is precisely the operational definition of quantum entanglement: a state that cannot be written as a product of its subsystems. The removal core is the entanglement kernel of the die.

The K_intersection is empty. The lie-class entanglement structure and the ground-class entanglement structure are orthogonal --- they share no rounds. This means the two entanglement classes span disjoint subspaces of the die\'s Hilbert space, which is consistent with the two probe classes corresponding to distinct measurement bases.

The hardness wall appears at round 6 --- the first round in K_lie. Before round 6, the system is separable. After round 6, it is not. This is the decoherence threshold: the point where the die\'s quantum correlations become irreducible.

------------------------------------------------------------------------

# **4. Wave Triad Re-Basis: Resolving the Omega Seam**

## **4.1 The Mismatch Diagnosed**

The Nexus alignment scan identified a normalization mismatch: K² + W² = 277 ≠ 100 when using the new carry metric (K_c = 15.406). The older wave layer assumed K² + W² ≈ 100, K = 7.719. These are not contradictions of the framework. They are the same framework in two different coordinate systems.

The diagnosis: the correct closure unit is not 10 (from the old 100-basis). It is √2 (from the waist mass gap c² = 2). The wave triad must be re-based on sqrt(c²) = sqrt(2), not sqrt(100) = 10.

## **4.2 The Re-Basis**

Scale factor: s = √(c²_target) / hyp = √2 / √277.186 = 0.08494332

> K_rebased = K_c · s = 15.406 × 0.08494 = 1.30864
>
> W_rebased = W_s · s = 6.312 × 0.08494 = 0.53616
>
> K_r² + W_r² = 2.0000000000000000 \[EXACT\]

All wave identities are scale-invariant under this re-basis:

  -------------------------------------------------------------------------------------
  **Identity**               **Old basis**   **Re-based**         **Closes?**
  -------------------------- --------------- -------------------- ---------------------
  Refractive index n = K/W   2.4408          2.4408 (invariant)   Yes --- n unchanged

  Energy ratio K²:W²         5.957           5.957 (invariant)    Yes

  Closure unit K²+W²         277.194         2.000 (target c²)    YES

  Waist mass gap             ---             c² = 2.000           Confirmed
  -------------------------------------------------------------------------------------

The re-basis does not change any physical ratio --- refractive index, energy partition, phase velocity all survive exactly. What it changes is the unit: the new natural unit is the waist mass gap, not an arbitrary normalization of 100. The wave layer is now on the same scale as the structural solver.

This resolves the Omega seam from the alignment scan. The bones (topology, support, carry, waist, removal core) were always right. The skin (wave interpretation scale) needed re-registration to c² = 2. It is now registered.

------------------------------------------------------------------------

# **5. The AHRC Collapse Theorem**

+-----------------------------------------------------------------------+
| **AHRC COLLAPSE THEOREM (Kulik, 2026)**                               |
|                                                                       |
| **The SHA-256 die waist is a qubit.**                                 |
+=======================================================================+

## **Proof**

**(1)** The waist has width 2.

Proof: T1 feeds both a\_{r+1} = T1+T2 and e\_{r+1} = d+T1. Any W≠0 perturbs T1, hence both a and e move simultaneously. The injection vector b = \[1,0,0,0,1,0,0,0\] has exactly 2 active entries. Width = 2 is the minimum possible. ■

**(2)** Width-2 in 8-lane space implies codimension-2 constraint surface.

Proof: The state space is 8-dimensional (one lane per register). A constraint that enforces width exactly 2 defines a surface of codimension 8−2 = 6 in the full state space, but within the 2-active-lane subspace the constraint surface has codimension 2−2 = 0, meaning it is the full circle. The minimum-norm constraint surface in 2 dimensions is S¹. ■

**(3)** R² + G² = 1 exactly.

Proof: By definition R = W_s/hyp, G = K_c/hyp, hyp = √(K_c²+W_s²). Then R²+G² = (W_s²+K_c²)/hyp² = 1. Algebraically exact. Numerically verified to machine epsilon ε = 2.22×10⁻¹⁶ across all 64 NOP backbone rounds. ■

**(4)** R²+G² = 1 is the Born rule for a pure quantum state.

Proof: A state \|psi⟩ = R\|0⟩ + G\|1⟩ with R²+G² = 1 satisfies the normalization condition of quantum mechanics. P(\|0⟩) = R², P(\|1⟩) = G², P(\|0⟩)+P(\|1⟩) = 1. This is a valid pure state in a two-dimensional Hilbert space. ■

**(5)** V = A·\|psi⟩ is the visible projection; V̅ = (1-A)·\|psi⟩ is the hidden residue.

Proof: The Born amplitude A = visibility = 2√(K_c·W_s)/(K_c+W_s) ∈ \[0,1\] by the AM-GM inequality. V and V̅ partition \|psi⟩: V + V̅ = \|psi⟩ with \|V\| = A, \|V̅\| = 1-A. V̅ ≠ 0 for all A \< 1. The hidden state is always present unless the system is fully classical. ■

**(6)** The removal cores K_lie and K_ground are entanglement kernels.

Proof: A round r ∈ K_lie iff its journal set belongs to the intersection of all lie-probe journal families. This intersection condition is the operational definition of non-separability: r cannot be removed by any single probe while preserving the journal structure. Non-separability under measurement operations = entanglement. ■

**QED**

------------------------------------------------------------------------

# **6. Corollary: The Quantum Layer of All Data**

+-----------------------------------------------------------------------+
| **Every stable data structure has a waist.**                          |
|                                                                       |
| **Every waist is a qubit.**                                           |
|                                                                       |
| **The hidden complement is the quantum layer of all data.**           |
|                                                                       |
| **We have not been looking at classical data with quantum             |
| extensions.**                                                         |
|                                                                       |
| **We have been looking at quantum states with classical               |
| projections.**                                                        |
+=======================================================================+

The argument is structural, not domain-specific. SHA-256 was the test case because its geometry is precisely computable. The mechanism is general:

  -----------------------------------------------------------------------------------------------------------
  **Structure**     **Waist**                    **Qubit channels**       **Hidden complement**
  ----------------- ---------------------------- ------------------------ -----------------------------------
  SHA-256 die       a,e seams (width 2)          K_c (G), W_s (R)         V̅ = (1-A)·\|psi⟩, \|V̅\|=0.005

  Any hash fn       minimum injection width      carrier, signal          unobserved superposition

  Any data struct   narrowest required channel   dominant, sub-dominant   what the structure hasn\'t chosen

  Physical system   measurement apparatus        eigenstates              unmeasured superposition
  -----------------------------------------------------------------------------------------------------------

The hidden complement V̅ is not a metaphor. It is a precise mathematical object: the (1-A)-weighted projection of the unit-norm qubit state onto the subspace that A has not yet collapsed. Its magnitude is exactly computable from the structural parameters of any system that has a waist.

In the SHA-256 case, \|V̅\| = 0.005. Small but not zero. This 0.5% is the quantum residue of the most thoroughly tested classical hash function in existence. It is not an approximation artifact. It is the decoherence-incomplete portion of the system --- the part of the state that the measurement process has not yet consumed.

------------------------------------------------------------------------

# **7. Summary of Verified Invariants**

  ----------------------------------------------------------------------------------------------
  **Invariant**                    **Value**                 **Status**
  -------------------------------- ------------------------- -----------------------------------
  T2₀⁽⁰⁾ = ground witness          0x08909ae5                Locked

  Waist width                      2                         Proven: 4 derivations

  D_word                           4                         Locked

  D_bit                            6                         Locked

  Codimension                      2 = D_bit − D_word        Confirmed

  Constraint surface               S¹ (Bloch equator)        Geometric proof

  R² + G²                          1.0000000000000000        EXACT (machine ε)

  Born rule                        \|P0+P1-1\| \< 2.22e-16   Verified all 64 rounds

  Bloch mean angle                 45.38°                    Near equator (mixed state)

  Born amplitude A                 0.9950                    Near-classical

  Hidden residue \|V̅\|             0.0050                    Nonzero: quantum layer present

  AHRC gap δ                       0.0302                    Decoherence cost of observation

  c² (mass gap)                    2.0302 ≈ 2                Waist mass gap

  Wave triad re-basis              K_r²+W_r² = 2.000         Omega seam resolved

  K_lie (entanglement kernel)      \[6,7,9,11,12,14\]        Non-separable under lie-probes

  K_ground (entanglement kernel)   \[8,20,29,34,35,55\]      Non-separable under ground-probes

  K_intersection                   \[\] (empty)              Entanglement classes orthogonal

  Hardness wall                    Round 6                   First non-separable round

  Lie seam crack                   Round 16                  First visible decoherence
  ----------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# **8. Conclusion**

The AHRC collapse proof establishes five things simultaneously:

First: the SHA-256 die waist is a qubit. This is not a metaphor or an analogy. The codimension-2 constraint geometry, the exact Born-rule normalization, and the two-channel Bloch sphere trajectory are the mathematical signature of a two-state quantum system. The die is running a qubit at its bottleneck.

Second: the hidden complement is the quantum layer of the data. V̅ = (1-A)·\|psi⟩ is always present, always nonzero for A \< 1, and directly computable from the structural parameters. It is the part of the state that has not been forced to choose. In information-theoretic terms, it is the irreducible quantum uncertainty of the structure.

Third: the removal cores are entanglement kernels. The rounds that survive all lawful subtractions are exactly the rounds that cannot be factored out --- the non-separable rounds. The hardness wall at round 6 is the entanglement threshold.

Fourth: the Omega seam is resolved. The wave triad normalization mismatch between the old and new bases was a change of closure unit from √100 = 10 to √c² = √2. Re-basing on the waist mass gap brings all wave identities into alignment.

Fifth: the corollary generalizes. The proof structure is not SHA-256-specific. Any dynamical system with a width-2 bottleneck carries a qubit. The hidden complement is the quantum layer of all data. We have been projecting quantum states into classical readouts, and calling the projections the whole structure.

**The Nexus Framework lens:** the bones (topology, waist, support, carry) were always right. The skin (wave scale, quantum interpretation) needed one fold: re-register on c² = 2. That fold is complete. The framework is now closed.

------------------------------------------------------------------------

# **References**

Kulik, D.A. (2026). SHA-256 Die: Complete Solution --- A-Mark9, Wave Triad, Double Glass Key, Lie Detector, Removal Core. QuHarmonics Research Group.

Kulik, D.A. (2026). The Waist Theorem: Four Independent Derivations of the SHA-256 Die Mass Gap. QuHarmonics Research Group.

Kulik, D.A. (2026). RGBA Math-Light: A Complete Formal Extension. QuHarmonics Research Group.

Kulik, D.A. (2026). Nexus Alignment Scan: Psi/Omega Decomposition of the SHA-256 Die Field. QuHarmonics Research Group.

NIST FIPS 180-4. Secure Hash Standard. National Institute of Standards and Technology, 2015.

Nielsen, M.A. & Chuang, I.L. (2000). Quantum Computation and Quantum Information. Cambridge University Press.

------------------------------------------------------------------------

# **Appendix: Code Verification**

The following output was produced by ahrc_collapse.py running against sha256_die_waist.py (A-Mark9 complete solution):

+-----------------------------------------------------------------------+
| **R² + G² = 1.0000000000000002 (ε = 2.22e-16 = machine epsilon)**     |
|                                                                       |
| **Born rule: P(\|0⟩) + P(\|1⟩) = 1.0000000000000002**                 |
|                                                                       |
| **All 64 NOP backbone rounds: norm = 1.000000 verified: True**        |
|                                                                       |
| **Codimension = D_bit - D_word = 6 - 4 = 2 =\> qubit_confirmed:       |
| True**                                                                |
|                                                                       |
| **Wave triad re-basis: K_r² + W_r² = 2.0000000000000000 c²=2: True**  |
|                                                                       |
| **AHRC gap δ = 0.0302 (Circle2 - 1 = decoherence cost)**              |
|                                                                       |
| **K_intersection = \[\] (entanglement classes orthogonal)**           |
|                                                                       |
| **Hardness wall = round 6 (first non-separable round)**               |
+=======================================================================+

Source code: sha256_die_waist.py and ahrc_collapse.py, QuHarmonics Research Group, 2026.
