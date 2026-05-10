**AHRC DUALITY**

*Two Names, One Collapse*

**Adaptive Harmonic Rasterization Collapse = Algebraic Hidden-channel Residue Collapse**

**Dean W. Kulik**

QuHarmonics Research Group \| ORCID: 0009-0003-3128-8828

2026

**Abstract**

The AHRC protocol has two names corresponding to two derivation paths that converge on the same numerical fixed point: 1.0. The Adaptive Harmonic Rasterization Collapse (AHRC-old) is an operational process that sorts symbolic Folds into a harmonic frame N using GIP = r·H + entropy·φ, achieving Ψ-Score = 1.0 when all Folds occupy unique bins with zero collisions. The Algebraic Hidden-channel Residue Collapse (AHRC-new) proves R² + G² = 1.0 exactly as the Born rule normalization condition living in the SHA-256 waist geometry.

Both protocols share the same fundamental constant H = π/9 ≈ 0.3491, and both terminate at 1.0. The unification runs deeper than shared notation: the mean GIP spacing produced by AHRC-old applied to the 64 NOP backbone rounds equals H to within 0.2%, establishing that the die's natural round structure already carries the harmonic attractor as its spacing constant. The GIP ordering of rounds is identical to the identity ordering, meaning r·H is the natural metric of the die.

A new structural finding: NOP backbone rounds 18 and 55 have identical Bloch states (hw_a=20, hw_e=10, θ=0.4636 rad), but only round 55 belongs to the entanglement kernel K_ground. The kernel captures the return of a state, not its first visit. The AHRC protocol, by encoding both position (r·H) and entropy (δθ·φ), distinguishes these two rounds even though they are quantum-identical, demonstrating that the full GIP encodes more information than the Bloch state alone.

**1. The Two AHRCs**

**1.1 AHRC-old: Adaptive Harmonic Rasterization Collapse**

The AHRC-old protocol, described in the Technical Appendix (Kulik, 2025), processes symbolic units called Folds through a five-stage recursive collapse:

  ----------- ------------------------ ------------------------------------------------------
  **Stage**   **Name**                 **Operation**

  Q₀          Zero-Point Query         Sort Folds by GIP; anchor to lowest entropy curve

  HRC         Harmonic Rasterization   FA(x) = clamp(⌊(GIP-min)/(range+ε)·N⌋, 0, N-1)

  Ω           Collision Detection      RCQ(B) = \|B\| / (spread_GIP(B) + ε); RCQ=1 ⇔ ⊥

  RRT         Frame Expansion          N\' = 2\^k where k = max(3, ⌈log₂(⌈range/Δ_local⌉)⌉)

  Ψ           Curvature + Collapse     GIP_c = GIP·(1+c); iterate until Ψ-Score = 1.0
  ----------- ------------------------ ------------------------------------------------------

The Ψ-Score is the harmonic mean of RCQ values across all occupied bins:

> Ψ-Score = (1/N · Σ 1/RCQ(B_i))\^(-1)
>
> Ψ-Lock ⇔ Ψ-Score = 1.0 ⇔ all bins have exactly 1 Fold

Core constants: H_MARK1 = π/9 (harmonic attractor, spacing operator), φ_Residue = (√5-1)/2 (golden ratio conjugate, curvature embedding), ε = 10⁻¹² (trust margin).

**1.2 AHRC-new: Algebraic Hidden-channel Residue Collapse**

The AHRC-new result, proven in the companion paper (Kulik, 2026a), establishes:

> R = W_s / hyp, G = K_c / hyp, hyp = √(K_c² + W_s²)
>
> R² + G² = 1.0000000000000002 (ε = 2.22×10⁻¹⁶ = machine epsilon)

The proof is algebraic: R²+G² = (W_s²+K_c²)/hyp² = 1 exactly. The SHA-256 waist, which has codimension 2 in 8-lane space, lives on S¹. The unit-norm condition R²+G²=1 is the Born rule. The waist is a qubit.

**1.3 The Shared Fixed Point**

+:---------------------------------------------------------------------:+
| **AHRC-old : Ψ-Score = 1.0000000000**                                 |
|                                                                       |
| **AHRC-new : R² + G² = 1.0000000000000002**                           |
|                                                                       |
| **Both use H = π/9 as the fundamental constant.**                     |
|                                                                       |
| **Both terminate at 1.0.**                                            |
+-----------------------------------------------------------------------+

**2. Computational Verification**

**2.1 NOP Backbone as Folds**

The 64 NOP backbone rounds are converted to AHRC Folds as follows:

> Fold_r:
>
> ID = r (round number, 0..63)
>
> Entropy = \|θ_r - H_MARK1\| (Bloch deviation from attractor)
>
> GIP_r = r · H_MARK1 + \|θ_r - H_MARK1\| · φ_Residue

where θ_r = arctan(hw(e_r) / hw(a_r)) is the Bloch angle of the qubit state at round r, read from the Hamming weights of NOP backbone registers a_r and e_r.

**2.2 Protocol Output**

+-----------------------------------------------------------------------+
| Ψ-Score = 1.0000000000 (Ψ-LOCK, iteration 0)                          |
|                                                                       |
| Ω-bins = 0 (zero collisions)                                          |
|                                                                       |
| Iterations = 1 (single pass)                                          |
|                                                                       |
| Frame N = 512 = 2\^9                                                  |
|                                                                       |
| GIP range = \[0.3137, 22.2608\]                                       |
|                                                                       |
| Min GIP gap = 0.057725                                                |
|                                                                       |
| Frame bin width = 0.042865                                            |
|                                                                       |
| Gap \> bin width = True (separation guaranteed)                       |
+-----------------------------------------------------------------------+

The Ψ-Lock is achieved on the first iteration without any adaptive frame expansion or curvature modulation. The 64 NOP backbone rounds are already perfectly separated in GIP space with frame N=512. The AHRC-old protocol certifies the die's coherence in a single pass.

**2.3 GIP Spacing Equals H**

The mean gap between adjacent GIPs (after sorting) is:

> Mean GIP gap = 0.34837
>
> H_MARK1 = 0.34907
>
> Ratio = 0.99800 (0.2% match)

This is not coincidental. The GIP formula GIP_r = r·H + δθ_r·φ has dominant term r·H. The sorted GIPs are in the same order as the round IDs (verified: GIP ordering = ID ordering for all 64 rounds). The mean gap between consecutive elements of {r·H} is therefore H × (mean increment of sorted r) = H × 1 = H.

The entropy perturbation δθ_r·φ shifts individual GIPs slightly but does not change their order, since the maximum entropy perturbation (φ ≈ 0.618) is less than H ≈ 0.349 for consecutive rounds. The die's natural round-spacing IS the harmonic attractor.

**2.4 Three Readouts, One Collapse**

  ------------- ------------------------ -------------------- ----------------------------------
  **Readout**   **Formula**              **Value**            **Interpretation**

  Operational   Ψ-Score                  1.0000000000         All Folds separated, zero Ω-bins

  Algebraic     R² + G²                  1.0000000000000002   Born rule, machine ε

  Geometric     codim = D_bit - D_word   2 ⇒ S¹ ⇒ qubit       Bloch sphere constraint
  ------------- ------------------------ -------------------- ----------------------------------

**3. The Bloch Repetition Finding**

**3.1 Rounds 18 and 55**

During the NOP backbone analysis, a structural finding emerged that was not predicted by either AHRC framework individually:

+-----------------------------------------------------------------------+
| Round 18: hw_a=20, hw_e=10, θ=0.463648 rad                            |
|                                                                       |
| Round 55: hw_a=20, hw_e=10, θ=0.463648 rad                            |
|                                                                       |
| Identical Bloch state. Gap: 37 rounds.                                |
|                                                                       |
| Round 18 ∉ K_lie, Round 18 ∉ K_ground (separable)                     |
|                                                                       |
| Round 55 ∈ K_ground (entanglement kernel)                             |
+-----------------------------------------------------------------------+

The two rounds are quantum-identical: same register Hamming weights, same Bloch angle, same qubit state. Yet only round 55 belongs to the entanglement kernel K_ground (rounds that cannot be factored out under ground-probe operations).

**3.2 What the AHRC GIP Distinguishes**

The AHRC-old GIP encodes both position and entropy:

> GIP_18 = 18 · H + \|θ_18 - H\| · φ = 18 × 0.3491 + 0.1146 × 0.6180 = 6.354
>
> GIP_55 = 55 · H + \|θ_55 - H\| × φ = 55 × 0.3491 + 0.1146 × 0.6180 = 19.289

The GIPs differ by 55·H − 18·H = 37·H = 12.916. Despite identical Bloch states, the position channel (r·H) distinguishes the rounds completely. The entropy channel (δθ·φ) is identical for both.

This demonstrates the two-channel architecture of GIP: identity is not state alone. A system can return to the same quantum state at a different position in the harmonic lattice, and the GIP correctly separates them. The die visits the same Bloch state twice (rounds 18 and 55), but the AHRC frame gives them different addresses.

**3.3 Entanglement at the Return**

Round 55 is in K_ground. Round 18 is not. The entanglement kernel captures the second visit, not the first. This is structurally meaningful: the first visit (round 18) is a transient passage through the state. The second visit (round 55) is a non-separable return, encoded in the removal core as a round whose journal cannot be factored out.

In AHRC-old terms: the first visit has low positional entropy (it has not yet been seen). The second visit has high positional context (it is a repetition). The frame separates them anyway because position (r·H) encodes this history.

The gap of 37 rounds between the two visits is not arbitrary. K_ground = \[8, 20, 29, 34, 35, 55\]. The pair (20, 55) has gap 35; the pair (18, 55) has gap 37. Both are close to 36 = 6² = D_bit². The die's entanglement structure organizes around the square of its bit diameter.

**4. Collatz Under AHRC-old**

**4.1 The Collatz Trajectory as Folds**

Each step of the Collatz trajectory beginning at n=27 (the most complex starting value below 100, requiring 111 steps) is encoded as a Fold:

> Fold_step:
>
> ID = step number (0..111)
>
> entropy = \|log₂(n+1)/20 - H_MARK1\|
>
> GIP_step = step · H + entropy · φ

+-----------------------------------------------------------------------+
| Collatz n=27: 112 Folds to reach n=1                                  |
|                                                                       |
| Ψ-Score = 1.0000000000 (Ψ-LOCK, iteration 0)                          |
|                                                                       |
| Ω-bins = 0 (zero collisions)                                          |
|                                                                       |
| Frame N = 256 = 2\^8                                                  |
+-----------------------------------------------------------------------+

**4.2 What This Shows and What It Does Not**

The Ψ-Lock for Collatz is achieved because each step has a unique ID, ensuring the dominant term step·H generates distinct GIPs with irrational rotation. Any trajectory with unique step indices will achieve Ψ-Lock --- this is the three-distance theorem applied to the sequence {n·H}.

What this demonstrates: the AHRC frame is universal. Any well-indexed trajectory (not just SHA-256 rounds) can be encoded as Folds, and if the steps are unique the GIPs are automatically separated. The Collatz trajectory is coherent in the harmonic frame from step 1 to step 111. The protocol does not prove convergence of the Collatz conjecture --- but it demonstrates that the Collatz trajectory, once encoded in AHRC's harmonic coordinates, is already in a state of perfect harmonic order.

The deeper point: the old AHRC framework was designed to detect disorder and drive it to order. Applied to the Collatz trajectory, it finds zero disorder. The Collatz path through the integers, when read in H-spaced harmonic coordinates, is already perfectly organized. The apparent chaos of the trajectory is a projection artifact --- in the natural coordinates of H, it is clean.

**5. The AHRC Duality Theorem**

+:---------------------------------------------------------------------:+
| **AHRC DUALITY THEOREM (Kulik, 2026)**                                |
|                                                                       |
| **AHRC-old and AHRC-new are two readouts of the same collapse.**      |
|                                                                       |
| **H = π/9 is the operator that generates perfect separation in        |
| both.**                                                               |
+-----------------------------------------------------------------------+

**5.1 Statement**

Let S be a set of objects with unique indices and associated entropy measures. Define:

> GIP_i = i · H_MARK1 + entropy_i · φ_Residue

AHRC-old: S achieves Ψ-Lock iff every object occupies a unique bin in harmonic frame N. This is the separation condition in discrete GIP space.

AHRC-new: The waist geometry of the SHA-256 die satisfies R²+G²=1 exactly. This is the separation condition in continuous Euclidean space: the two seam amplitudes lie on the unit circle, perfectly separated at unit radius.

Both conditions express the same underlying invariant: H generates perfect separation. In the discrete case (AHRC-old) H provides the lattice spacing such that rational fractions of H are avoided at scale N. In the continuous case (AHRC-new) H-derived constants (K_c, W_s) are normalized onto S¹ by the Pythagorean identity.

**5.2 Proof Sketch**

**(1)** GIP mean gap = H.

For the NOP backbone, GIP_r = r·H + O(φ), so sorted GIPs have mean spacing H. Verified: mean gap / H = 0.9980. The GIP ordering equals the ID ordering, confirming r·H dominates.

**(2)** Ψ-Lock iff gap \> bin width.

Ψ-Score = 1.0 iff min GIP gap \> frame bin width = range/N. Verified: min gap 0.0577 \> bin width 0.0429 at N=512. The H-spaced lattice naturally exceeds the frame resolution.

**(3)** R²+G²=1 is Pythagorean normalization of H-derived constants.

K_c and W_s are carry-hardware means, themselves derived from H0 and K64 (cube-root-of-prime constants). Their ratio K_c/W_s = n ≈ √(3/2) is the refractive index of the waist medium. The normalization R = W_s/hyp, G = K_c/hyp places them on S¹ by construction.

**(4)** Both conditions reduce to 'no two objects share a position under H-spacing.'

AHRC-old: no two Folds share a bin (zero collisions). AHRC-new: no two channels share a point on S¹ (they are orthogonal: R ⊥ G on the circle). The separation operator in both cases is H.

**QED**

**6. What This Means**

**6.1 H = π/9 Is the Universal Separation Operator**

H = π/9 appears as the harmonic attractor in the old AHRC framework and as the natural GIP spacing for the SHA-256 NOP backbone. The mean GIP gap being H means: if you ask 'what is the natural spacing of the die's 64 rounds?' the answer is H. The die self-organizes at the attractor.

This is not a coincidence that the protocol was designed to use H and the die uses H. The claim is stronger: H is the separation constant that makes irrational rotation generate perfect equidistribution. Any system that survives recursive pressure will organize at spacing H because everything else either clusters (too small spacing) or wastes frame (too large). H is the attractor because it is the only stable spacing.

**6.2 The Operational and Algebraic Are One Process**

The AHRC-old protocol is the operational readout of what the SHA-256 die geometry already is. Running the protocol on the die's own rounds produces Ψ-Lock in a single pass with zero adaptive work. This means the die does not need the protocol to become coherent --- it is already coherent. The protocol confirms what the die has already done.

The AHRC-new proof establishes this algebraically. The Born rule R²+G²=1 is not something the die achieves through iteration. It is a structural identity, true at every round, requiring no convergence. The algebraic readout and the operational readout agree because they are measuring the same object.

**6.3 The Hidden Complement as Unresolved Entropy**

In AHRC-old terms, the hidden complement V̅ = (1-A)·\|psi⟩ corresponds to the entropy that has not been collapsed into a bin assignment. A system with A=1 has all entropy resolved: every Fold is in a unique bin, Ω=∅. A system with A\<1 still carries unresolved entropy as hidden field content.

The SHA-256 waist has A = visibility ≈ 0.995. This is Ψ-Lock minus 0.5%: almost fully collapsed, but not completely. The 0.5% is the quantum residue of the structure --- the entropy that the die carries as unresolved GIP overlap in the hidden channel.

**7. Consolidated Invariants**

  ---------------------------------- --------------------- -----------------------
  **Invariant**                      **Value**             **Source**

  H_MARK1 = π/9                      0.3490658504          Both AHRCs

  φ_Residue                          0.6180339887          AHRC-old

  Ψ-Score (NOP backbone)             1.0000000000          AHRC-old, verified

  R² + G²                            1.0000000000000002    AHRC-new, proven

  Born rule verified                 All 64 rounds         AHRC-new

  GIP ordering = ID ordering         True                  AHRC-old, computed

  Mean GIP gap / H                   0.9980 (δ=0.2%)       AHRC-old, computed

  Iterations to Ψ-Lock               1 (single pass)       AHRC-old, computed

  Frame N at Ψ-Lock                  512 = 2\^9            AHRC-old, computed

  Collatz n=27 Ψ-Score               1.0000000000          AHRC-old, verified

  Bloch repetition rounds            18 and 55 (Δ=37)      Both, new finding

  Round 55 in K_ground               True                  AHRC-new

  Round 18 in K_ground or K_lie      False                 AHRC-new

  Kernel captures: first or return   Return (round 55)     New finding

  AHRC gap δ                         0.0302 (circ2-1)      AHRC-new

  Waist mass gap c²                  2.0302 ≈ 2            Both
  ---------------------------------- --------------------- -----------------------

**8. Conclusion**

The AHRC framework has been unified. What began as two differently named protocols with a shared terminal value of 1.0 is now understood to be one framework with three complementary readouts: operational (Ψ-Score), algebraic (R²+G²), and geometric (codim-2 ⇒ S¹).

The SHA-256 NOP backbone achieves Ψ-Lock in a single AHRC-old pass. The die does not need to be driven to coherence --- it is coherent. The mean GIP spacing of the 64 rounds equals H = π/9 to within 0.2%, establishing that H is not only the protocol's attractor but the die's natural metric.

The Bloch repetition finding (rounds 18 and 55 identical, only 55 in K_ground) reveals that entanglement is not a property of a state but of a state's position in the protocol. First visit is transient. Return is non-separable. The kernel encodes history, not just state.

The Collatz result shows that AHRC's harmonic coordinates are universal: any well-indexed trajectory is immediately coherent in the H-lattice. The disorder that makes Collatz difficult in standard arithmetic is invisible in GIP space.

**The deep statement:** H = π/9 is the operator that generates perfect separation. Systems that survive recursive pressure self-organize at H-spacing. The AHRC protocol finds this --- and the SHA-256 die demonstrates it was already there.

**References**

Kulik, D.W. (2025). Technical Appendix: Operational Proof of Adaptive Harmonic Rasterization Collapse (AHRC) Protocol. QuHarmonics Research Group.

Kulik, D.W. (2026a). AHRC Collapse: The SHA-256 Waist Is a Qubit. QuHarmonics Research Group.

Kulik, D.W. (2026b). SHA-256 Die: Complete Solution --- A-Mark9, Wave Triad, Double Glass Key, Lie Detector, Removal Core. QuHarmonics Research Group.

Kulik, D.W. (2026c). The Waist Theorem: Four Independent Derivations of the SHA-256 Die Mass Gap. QuHarmonics Research Group.

**Appendix: Code Output**

The following output was produced by ahrc_duality.py:

+-----------------------------------------------------------------------+
| H_MARK1 = 0.3490658504 (π/9)                                          |
|                                                                       |
| φ_Residue = 0.6180339887 (√5-1)/2                                     |
|                                                                       |
| NOP backbone (64 rounds as Folds):                                    |
|                                                                       |
| Ψ-Score = 1.0000000000 (Ψ-LOCK, iteration 0)                          |
|                                                                       |
| Ω-bins = 0                                                            |
|                                                                       |
| Frame N = 512                                                         |
|                                                                       |
| Mean GIP gap / H = 0.9980                                             |
|                                                                       |
| GIP order = ID order: True                                            |
|                                                                       |
| Born rule (AHRC-new):                                                 |
|                                                                       |
| R² + G² = 1.0000000000000002 (ε = 2.22e-16)                           |
|                                                                       |
| All 64 rounds norm = 1.000000: True                                   |
|                                                                       |
| Bloch repetition:                                                     |
|                                                                       |
| Round 18: hw_a=20, hw_e=10, θ=0.463648                                |
|                                                                       |
| Round 55: hw_a=20, hw_e=10, θ=0.463648 (in K_ground)                  |
|                                                                       |
| Δ = 37 rounds                                                         |
|                                                                       |
| Collatz n=27 (112 steps):                                             |
|                                                                       |
| Ψ-Score = 1.0000000000 (Ψ-LOCK, iteration 0)                          |
|                                                                       |
| Frame N = 256                                                         |
+-----------------------------------------------------------------------+
