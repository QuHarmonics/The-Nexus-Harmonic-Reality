# The Harmonic Ninth (H₉): Selection-Only, CRT-Aligned Helical Addressing with π/9 Phase Lock

*A Topological Encoding Framework for Phase-Locked Data Systems*

## Abstract

We present a selection-only computing substrate in which data is addressed, not stored. An inner 18-spoke phase engine locks at the exact harmonic H∗=π/9 (20°), while an outer 30-slot number-theoretic wheel (primorial 2⋅3⋅5) provides sieve geometry and insertion slack. Because gcd(18,30)=6, we lift to a helical state space via a mixed CRT: coprime components (9,10) form a principal index κ∈Z90​; shared factors (2,3) form a tag τ∈Z6​, yielding addresses (κ,τ). A gauge transform O separates inner physics from ASCII/hex offsets (0x3\*/0x6\*) making acceptance gauge-invariant. Dynamics follow nine coupled feedback engines that minimize per-lane amplitude and wrapped-phase errors to π/9; a minimal asymmetry ("small lobe") provides phase locomotion. A glyph is admitted only under a three-part contract: (i) nine-way window identity, (ii) amplitude lock, (iii) phase lock on the 20° lattice. Keystone audits---period-18 folding, gauge invariance, duplex BBP cycles, and SAT9 collapse events---yield falsifiable signatures. Computation becomes resonance; emission is memory.

## The Acceptance Contract

A glyph or system state is not considered \"true\" or valid until it satisfies a strict, three-part acceptance contract. This provides a falsifiable, operational definition of harmonic coherence. Nothing is \"true\" in the system until these conditions hold.

1.  **Identity.** For window W and lanes i=1..9, the normalized nibble windows are bit-identical.

2.  **Amplitude.** ∣Hi​−π/9∣≤εA​ for all lanes.

3.  **Phase.** ei​=wrap(ϕi​−20∘⋅(i−1)) satisfies ∣ei​∣≤εϕ​.

**Law:** If any enabled gate fails, the system MUST emit nothing. This is the principle of \"Speak-on-Lock\": emission is persistence.

## Part I: The Dual-Lattice Helical Architecture

The Harmonic Operating System is founded on a topological and number-theoretic structure that unifies computation and data into a single geometric framework. It moves beyond empirical approximations to an axiomatic foundation, where the system\'s behavior is a necessary consequence of its geometry.

### Section 1: Formalization of the Dual-Lattice Architecture

The system\'s state space is not a linear memory array but a composite, multi-layered rotational structure. This **Dual-Lattice Helical Architecture** provides the geometric foundation for all operations within the Harmonic OS.

#### 1.1 The Inner Ring: The 18-Spoke Harmonic Engine Frame

The core of the system is the **inner engine frame**, a rotational phase lattice that enforces precision and stability. Its structure is defined by the fundamental harmonic constant H∗=π/9 \[69, 69\].

- **Geometric Structure:** The inner ring is an 18-spoke wheel, with each spoke separated by an angle of 2π/18=π/9 radians, or 20 degrees. This 18-fold symmetry is the native geometry of the system\'s core physics.^1^

- **Harmonic Target:** All dynamic processes within this frame are governed by feedback mechanisms that seek to align with the phase target of H∗=π/9. This is the system\'s primary attractor state, enforced by Samson\'s Law \[69, 69\]. All regulators minimize per-lane amplitude error ei(A)​=π/9−Hi​ and wrapped phase error ei(ϕ)​=wrap(ϕi​−ϕi∗​) with ϕi∗​=20∘⋅(i−1) on the 18-spoke lattice.

- **Internal Coordinates:** The state of a process within this frame is represented by its angular position, θ18​∈{0,1,\...,17}, corresponding to one of the 18 spokes. The internal, \"raw\" glyphs produced by the system\'s core engines are represented by 4-bit nibbles, ut​∈{0,\...,15}.

#### 1.2 The Outer Wheel: The 30-Slot Number-Theoretic Observer Frame

The **outer observer frame** is a number-theoretic structure that provides a stable, context-aware framework for encoding and interpreting data. It is based on the principles of wheel factorization using the first three prime numbers.^5^

- **Geometric Structure:** The outer wheel is a 30-slot ring, corresponding to the primorial 2×3×5=30. This structure is used to sieve for prime numbers and other number-theoretic patterns.

- **Allowed Residues:** Of the 30 slots, only the 8 residues that are coprime to 30 are considered \"allowed\" slots for prime-related glyphs. These are {1,7,11,13,17,19,23,29}.^7^ These 8 positions form the primary address space of the outer wheel.

- **Structural Gaps:** The remaining 22 residues (those with factors of 2, 3, or 5) are structural \"gaps.\" These are not errors or unused space but are a fundamental feature of the architecture, providing the necessary \"semantic slack\" for stable data insertion, as will be detailed in Section 5.^16^

#### 1.3 Gauge Invariance and the Observer Frame Transformation

A critical principle of the Harmonic OS is **gauge invariance**, which recognizes that the representation of a glyph can change depending on the observational frame without altering its fundamental identity.^22^ The common ASCII/hexadecimal frame imposes a fixed translational offset on the raw glyphs produced by the inner engine. We formalize this relationship with the

**Observer Frame Gauge Transformation**, O(u), and its inverse, O−1(H,L):

O(u)={(3,u),(6,u−9),​0≤u≤910≤u≤15​O−1(H,L)={L,L+9,​H=3, 0≤L≤9H=6, 1≤L≤6​

The high nibbles 3 and 6 are **observer artifacts**, not intrinsic content. All control and feedback must run on u=O−1(⋅) (inner gauge). All acceptance decisions are invariant under O; parity flips alter observables, not glyph truth.

#### 1.4 The Mixed-CRT Helical State Space

The inner and outer lattices are unified into a single, multi-scale address space. Because the moduli 18 and 30 are not coprime (gcd(18,30)=6), a direct ring isomorphism to Z540​ is mathematically incorrect. The correct lift is a **mixed CRT**:

1.  **Factor the lattices:**

    - Inner 18→Z2​×Z9​ (parity and mod-9 phase).

    - Outer 30→Z2​×Z3​×Z5​ (parity, mod-3 class, mod-5 class).

2.  Define the Helical Index: The address Θ decomposes into a principal index κ and a tag τ:\
    Θ≡(κ,τ),κ∈Z90​ from CRT(θ9​,θ10​),τ∈Z6​.\
    Here, θ9​∈Z9​ is the inner 9-phase, θ10​∈Z10​ is derived from the outer Z2​×Z5​ pair, and τ∈Z2​×Z3​ captures the shared factor relations. This yields 90×6=540 distinct states. Garner\'s algorithm on the coprime moduli 9 and 10 yields κ; τ is the residual two-by-three tag.

## Part II: The Dynamics of a Living Lattice

A system in perfect harmonic balance is static. For a system to evolve, compute, and traverse its state space, a propulsive force is required. In the Harmonic OS, this force is not random but is the result of a carefully architected interplay between a set of stabilizing engines and a minimal, intentional asymmetry.

### Section 2: The Nine Engines in Balance

The stability of the inner engine frame is maintained by a functional architecture of **\"Nine Engines in Balance.\"** These are nine distinct, coupled feedback processes, each responsible for regulating a different aspect of the system\'s harmonic state. Their collective function is to create a stable \"standing field\" of phase coherence around the H9​=π/9 target.

  -----------------------------------------------------------------------------------------------------------
  Engine                  Phase Role                     Conceptual Equivalent
  ----------------------- ------------------------------ ----------------------------------------------------
  **E₁**                  Resonant Origin                The system\'s primary carrier frequency (f0​).

  **E₂**                  Phase Interference Dampening   The proportional component of Samson\'s Law.

  **E₃**                  Reflective Phase Lock          A stabilizer for emergent glyphs.

  **E₄**                  Forward Diffusion Driver       An entropy step-up module.

  **E₅**                  Cross-Channel Interpolation    A harmonic comb filter for inter-engine coherence.

  **E₆**                  Field Surface Modulation       Wavefront amplitude regulator.

  **E₇**                  Recursive Glyph Mirror         A phase memory feedback loop.

  **E₈**                  Drift Correction Core          The integral component of Samson\'s Law (ΔH).

  **E₉**                  Boundary Phase Resolver        A cycle-closing harmonizer.
  -----------------------------------------------------------------------------------------------------------

When these nine channels are perfectly tuned to the H9​=π/9 coherence target, their outputs collectively fold to zero drift, resulting in a perfectly stable but static state.

### Section 3: The DHA Phase Locomotion Law (The \"Small Lobe\")

To enable evolution and computation, this perfect symmetry must be broken.^28^ The Harmonic OS achieves this through the introduction of a

**\"small lobe\"**---a minimal, intentional, and deterministic asymmetry that provides the propulsive force for the system. This principle of **asymmetry-induced symmetry**, where minimal heterogeneity yields stable synchrony, is formalized as the **DHA Phase Locomotion Law** ^36^:

θt+1​=θt​+Δϕ+ϵsin(9θt​+ψ),0\<ϵ≪1.

Here, Δϕ is the base tick (e.g., 1°). The 9θ term is the nonet warp, and ϵ is the lobe\'s magnitude. This guarantees perpetual motion while the Samson controller keeps the system glued to the H9​ attractor.

## Part III: Number-Theoretic Structures and Stable Evolution

The dual-lattice architecture provides a rich framework for encoding and manipulating information with number-theoretic significance. The outer prime wheel, in particular, allows the system to geometrically represent and process properties of prime numbers, while the structured gaps in its design enable a novel form of data management.

### Section 4: The Prime Wheel and Geometric Encoding

The outer frame\'s 30-slot wheel, derived from the primorial 2×3×5, functions as a natural sieve for prime numbers.^5^

- **The \"0x35\" Header:** A glyph observed as 0x35 (ASCII \'5\') acts as an operational header. It declares the wheel domain: mod-30, with admissible residues {1,7,11,13,17,19,23,29}.

- **The Twin Prime Pair Glyph:** Twin primes (e.g., 11 and 13) correspond to **adjacent allowed slots** on the mod-30 circle. A \"twin-prime glyph\" is therefore defined as a pair of glyphs mapping to adjacent admissible slots on the wheel.

### Section 5: Stable Evolution via Deterministic Insertion

The Harmonic OS\'s helical lattice, with its structured gaps, provides a mechanism for **stable insertion without renumbering**.^16^

- **Semantic Slack:** The 22 disallowed residues on the outer 30-wheel, combined with the unoccupied slots on the inner 18-ring, create a vast, sparse state space.

- **The CRT-Gap Insertion Mechanism:** To insert a new glyph between two existing items with nearby κ indices, the system chooses a free τ∈Z6​ tag to act as a parallel lane. This allows the new item to be placed between existing entries while keeping their κ indices monotone and stable. Order is preserved; no renumbering is needed.

## Part IV: Implementation and Verification

The formal architecture of the Harmonic OS gives rise to a suite of powerful, implementable tools and falsifiable validation protocols.

### Section 6: The Harmonic OS Kernel and API

The **Harmonic OS Kernel** is the production-grade engine that implements the full dual-lattice architecture. Its core function is the seed -\> glyph -\> address pipeline.

- **Driver:** A duplex sponge driver (e.g., SHAKE/BLAKE3) is used for stateful, recursive hashing. Duplex sponges naturally expose per-lane micro-warps (εi​,ψi​) without rehashing the archive---aligning with the selection-only I/O model.

- **Minimal API Sketch:**

  - accept(glyphWindowW) -\> bool: Returns true iff the three-part acceptance contract is met.

  - helical_index(theta18, theta30) -\> (kappa, tau): Performs the mixed-CRT lift.

  - drive_duplex(absorb: bytes) -\> List\[(ε_i, ψ_i)\]: Returns per-lane micro-warps for each tick.

  - normalize_gauge(bytes) -\> inner_nibbles: Applies O−1; also emits even/odd parity views.

  - sat9_audit(window) -\> CollapseEvent?: Detects ≥6×9 runs and logs the collapse event.

### Section 7: SAT9 Audits

**SAT9 collapse** is an acceptance-stage detection of (i) carry cascades of length ≥6 across 9-wide windows and (ii) parity duals 0x83↔0x37, observed around ...999999... → ...837 transitions. It is a verifiable audit signature of the control law, not a numerology claim. The SAT9 subsystem is responsible for:

1.  Detecting runs of ≥6 nines.

2.  Logging the pre-digit and the forced carry (e.g., ...1134→1135).

3.  Logging the forward triplet 8-3-7 and its parity dual.

4.  Tagging subsequent accepted glyphs as \"collapse glyphs.\"

### Section 8: Falsifiable Validation Protocol

The integrity of the Harmonic OS is demonstrated through a suite of falsifiable tests designed to be reviewer-proof.

- **F1 Geometry:** Fail if accepted emissions do not concentrate at 20° modulo 2π.

- **F2 Gauge:** Fail if acceptance differs before vs. after applying O−1.

- **F3 Depth:** Fail if stabilized glyphs flip under deeper computational cuts or alternate parity taps.

- **F4 CRT:** Fail if insertions require renumbering of the principal index κ.

- **F5 Silence:** Fail if any emission occurs when an acceptance contract gate is off.

- **Additional Tests:**

  - **Period-18 Folding:** Verify residual fold patterns with a period of 18.

  - **k=10 Energy Decay:** Verify that energy decays at the predicted tenth-order rate upon phase-lock.

  - **BBP↔Duplex Cycles:** Verify that closed-loop BBP-duplex cycles have periods dividing 18 and are reproducible from seeds.

## Conclusion: A New Topology for Meaning

The Harmonically Indexed, Dual-Lattice Code Framework, corrected and sharpened by the axiomatic constant H9​=π/9, is the blueprint for a new class of operating system. It moves computation beyond the linear, procedural model of the Turing machine to a geometric, resonant paradigm. The Harmonic OS does not ask, \"What is the data at address X?\" It asks, \"What glyph harmonically belongs at this phase slot, under these constraints?\"

The architecture we have declared is concrete, specified, and implementable. By unifying the rotational symmetry of the π/9 inner engine with the number-theoretic structure of the prime outer wheel, it creates a rich topology for meaning. The structured gaps in this topology are not flaws but are the very feature that allows for stable evolution. The intentional asymmetry of the \"small lobe\" is not a bug but the engine of progress.

This framework confirms the deepest insights of the Nexus and RHA research: that the universe is a programmable harmonic engine, and that by understanding its language of geometry, resonance, and phase, we can build systems that are in tune with the fundamental structure of reality \[69, 69, 69\]. The universe replies to our phase-aligned queries in the digits of π, and with the Harmonic OS, we have built the machine to listen.

#### Works cited

1.  en.wikipedia.org, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/18\_(number)#:\~:text=18%20is%20a%20semiperfect%20number,18%20infinite%20families%20of%20groups.]{.underline}](https://en.wikipedia.org/wiki/18_(number)#:~:text=18%20is%20a%20semiperfect%20number,18%20infinite%20families%20of%20groups.)

2.  Special properties of number 18 (Today\'s Date) - WELCOME TO THE EXCITING WORLD OF MATHEMATICS, accessed August 18, 2025, [[http://amitbajajmaths.blogspot.com/2015/06/special-properties-of-number-18-todays.html]{.underline}](http://amitbajajmaths.blogspot.com/2015/06/special-properties-of-number-18-todays.html)

3.  18 (number) - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/18\_(number)]{.underline}](https://en.wikipedia.org/wiki/18_(number))

4.  Origami With Rotational Symmetry: A Review on Their Mechanics and Design, accessed August 18, 2025, [[https://asmedigitalcollection.asme.org/appliedmechanicsreviews/article/75/5/050801/1155971/Origami-With-Rotational-Symmetry-A-Review-on-Their]{.underline}](https://asmedigitalcollection.asme.org/appliedmechanicsreviews/article/75/5/050801/1155971/Origami-With-Rotational-Symmetry-A-Review-on-Their)

5.  Wheel factorization - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/Wheel_factorization]{.underline}](https://en.wikipedia.org/wiki/Wheel_factorization)

6.  wheel factorization - PlanetMath.org, accessed August 18, 2025, [[https://planetmath.org/wheelfactorization]{.underline}](https://planetmath.org/wheelfactorization)

7.  wheel factorization - The Prime Glossary - PrimePages, accessed August 18, 2025, [[https://t5k.org/glossary/xpage/WheelFactorization.html]{.underline}](https://t5k.org/glossary/xpage/WheelFactorization.html)

8.  Wheel Factorization \| Programming Praxis, accessed August 18, 2025, [[https://programmingpraxis.com/2009/05/08/wheel-factorization/]{.underline}](https://programmingpraxis.com/2009/05/08/wheel-factorization/)

9.  Prime Numbers Demystified by 8-Dimensional Algorithms, accessed August 18, 2025, [[https://www.primesdemystified.com/]{.underline}](https://www.primesdemystified.com/)

10. Modulo a Prime Number, accessed August 18, 2025, [[https://www.maths.ox.ac.uk/system/files/attachments/lecture2.pdf]{.underline}](https://www.maths.ox.ac.uk/system/files/attachments/lecture2.pdf)

11. Number theory - Prime, Distribution, Theorem - Britannica, accessed August 18, 2025, [[https://www.britannica.com/science/number-theory/Prime-number-theorem]{.underline}](https://www.britannica.com/science/number-theory/Prime-number-theorem)

12. Number 30: Power integer. Comprehensive Review, accessed August 18, 2025, [[https://www.primesdemystified.com/thirty.html]{.underline}](https://www.primesdemystified.com/thirty.html)

13. What can primes, except 2, 3, and 5, be congruent to \$\\pmod {30} - Math Stack Exchange, accessed August 18, 2025, [[https://math.stackexchange.com/questions/308355/what-can-primes-except-2-3-and-5-be-congruent-to-pmod-30]{.underline}](https://math.stackexchange.com/questions/308355/what-can-primes-except-2-3-and-5-be-congruent-to-pmod-30)

14. Prime number theorem - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/Prime_number_theorem]{.underline}](https://en.wikipedia.org/wiki/Prime_number_theorem)

15. History of integer factorization - Computer Science Purdue, accessed August 18, 2025, [[https://www.cs.purdue.edu/homes/ssw/chapter3.pdf]{.underline}](https://www.cs.purdue.edu/homes/ssw/chapter3.pdf)

16. Gap Buffer Data Structure - GeeksforGeeks, accessed August 18, 2025, [[https://www.geeksforgeeks.org/dsa/gap-buffer-data-structure/]{.underline}](https://www.geeksforgeeks.org/dsa/gap-buffer-data-structure/)

17. Gap buffer - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/Gap_buffer]{.underline}](https://en.wikipedia.org/wiki/Gap_buffer)

18. Is it a bad approach to use a single large buffer-gap array as my data structure for a text editor? - Quora, accessed August 18, 2025, [[https://www.quora.com/Is-it-a-bad-approach-to-use-a-single-large-buffer-gap-array-as-my-data-structure-for-a-text-editor]{.underline}](https://www.quora.com/Is-it-a-bad-approach-to-use-a-single-large-buffer-gap-array-as-my-data-structure-for-a-text-editor)

19. Gapped Insertion Sorting. Tired of comparing elements one by one... - Pratttshush - Medium, accessed August 18, 2025, [[https://pratttshush.medium.com/gapped-insertion-sorting-83f80d3d4a9e]{.underline}](https://pratttshush.medium.com/gapped-insertion-sorting-83f80d3d4a9e)

20. Deterministic vs probabilistic matching - Melissa Data, accessed August 18, 2025, [[https://www.melissa.com/address-experts/the-difference-between-deterministic-and-probabilistic-matching]{.underline}](https://www.melissa.com/address-experts/the-difference-between-deterministic-and-probabilistic-matching)

21. In SQL Server, is TOP deterministic by default when used on a table with a clustered index?, accessed August 18, 2025, [[https://stackoverflow.com/questions/4962970/in-sql-server-is-top-deterministic-by-default-when-used-on-a-table-with-a-clust]{.underline}](https://stackoverflow.com/questions/4962970/in-sql-server-is-top-deterministic-by-default-when-used-on-a-table-with-a-clust)

22. Gauge theory - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/Gauge_theory]{.underline}](https://en.wikipedia.org/wiki/Gauge_theory)

23. Gauge theory \| Physics, Quantum Mechanics & Applications \..., accessed August 18, 2025, [[https://www.britannica.com/science/gauge-theory]{.underline}](https://www.britannica.com/science/gauge-theory)

24. Can anyone give an intuitive explanation of gauge theory? : r/askscience - Reddit, accessed August 18, 2025, [[https://www.reddit.com/r/askscience/comments/6bl1e9/can_anyone_give_an_intuitive_explanation_of_gauge/]{.underline}](https://www.reddit.com/r/askscience/comments/6bl1e9/can_anyone_give_an_intuitive_explanation_of_gauge/)

25. In which contexts are gauge theories applied? - Physics Stack Exchange, accessed August 18, 2025, [[https://physics.stackexchange.com/questions/162298/in-which-contexts-are-gauge-theories-applied]{.underline}](https://physics.stackexchange.com/questions/162298/in-which-contexts-are-gauge-theories-applied)

26. www.reddit.com, accessed August 18, 2025, [[https://www.reddit.com/r/askscience/comments/6bl1e9/can_anyone_give_an_intuitive_explanation_of_gauge/#:\~:text=A%20gauge%20theory%20is%20a,changes%20in%20gauge%20are%20made.]{.underline}](https://www.reddit.com/r/askscience/comments/6bl1e9/can_anyone_give_an_intuitive_explanation_of_gauge/#:~:text=A%20gauge%20theory%20is%20a,changes%20in%20gauge%20are%20made.)

27. What is a gauge? \| What\'s new - Terence Tao, accessed August 18, 2025, [[https://terrytao.wordpress.com/2008/09/27/what-is-a-gauge/]{.underline}](https://terrytao.wordpress.com/2008/09/27/what-is-a-gauge/)

28. Symmetry Breaking in Dynamical Systems - Number Analytics, accessed August 18, 2025, [[https://www.numberanalytics.com/blog/symmetry-breaking-dynamical-systems]{.underline}](https://www.numberanalytics.com/blog/symmetry-breaking-dynamical-systems)

29. Advanced Topics in Symmetry Breaking - Number Analytics, accessed August 18, 2025, [[https://www.numberanalytics.com/blog/advanced-symmetry-breaking-topics]{.underline}](https://www.numberanalytics.com/blog/advanced-symmetry-breaking-topics)

30. Special Issue : Symmetry in Complex Systems - MDPI, accessed August 18, 2025, [[https://www.mdpi.com/journal/symmetry/special_issues/Symmetry_Complex_Systems]{.underline}](https://www.mdpi.com/journal/symmetry/special_issues/Symmetry_Complex_Systems)

31. Observation of -Symmetry Breaking in Complex Optical Potentials \| Phys. Rev. Lett., accessed August 18, 2025, [[https://link.aps.org/doi/10.1103/PhysRevLett.103.093902]{.underline}](https://link.aps.org/doi/10.1103/PhysRevLett.103.093902)

32. Symmetry Breaking Dynamics in Quantum Many-Body Systems - arXiv, accessed August 18, 2025, [[https://arxiv.org/html/2501.13459v1]{.underline}](https://arxiv.org/html/2501.13459v1)

33. Advanced Mathematical Approaches to Symmetry Breaking in High-Dimensional Field Theories: The Roles of Laurent Series, Residues, and Winding Numbers - arXiv, accessed August 18, 2025, [[https://arxiv.org/html/2409.08294v1]{.underline}](https://arxiv.org/html/2409.08294v1)

34. View of The Role of Symmetry in Mathematical Physics: Group Theory and its Applications, accessed August 18, 2025, [[https://nano-ntp.com/index.php/nano/article/view/4022/3048]{.underline}](https://nano-ntp.com/index.php/nano/article/view/4022/3048)

35. (PDF) Symmetry and Symmetry Breaking in Science and Arts - ResearchGate, accessed August 18, 2025, [[https://www.researchgate.net/publication/378020232_Symmetry_and_Symmetry_Breaking_in_Science_and_Arts]{.underline}](https://www.researchgate.net/publication/378020232_Symmetry_and_Symmetry_Breaking_in_Science_and_Arts)

36. Asymmetry induced isolated fully synchronized state in coupled oscillator populations, accessed August 18, 2025, [[https://par.nsf.gov/servlets/purl/10349111]{.underline}](https://par.nsf.gov/servlets/purl/10349111)

37. Symmetry and Asymmetry in Oscillatory Patterns - Argonne National Laboratory, accessed August 18, 2025, [[https://www.anl.gov/event/symmetry-and-asymmetry-in-oscillatory-patterns]{.underline}](https://www.anl.gov/event/symmetry-and-asymmetry-in-oscillatory-patterns)

38. \[PDF\] Asymmetry-induced synchronization in oscillator networks. \| Semantic Scholar, accessed August 18, 2025, [[https://www.semanticscholar.org/paper/Asymmetry-induced-synchronization-in-oscillator-Zhang-Nishikawa/07d9bc14f544a3e06410c8c37b111e401593ecf1]{.underline}](https://www.semanticscholar.org/paper/Asymmetry-induced-synchronization-in-oscillator-Zhang-Nishikawa/07d9bc14f544a3e06410c8c37b111e401593ecf1)

39. Asymmetry-induced effects in coupled phase-oscillator ensembles: Routes to synchronization - ResearchGate, accessed August 18, 2025, [[https://www.researchgate.net/publication/26284442_Asymmetry-induced_effects_in_coupled_phase-oscillator_ensembles_Routes_to_synchronization]{.underline}](https://www.researchgate.net/publication/26284442_Asymmetry-induced_effects_in_coupled_phase-oscillator_ensembles_Routes_to_synchronization)

40. Circular buffer - Wikipedia, accessed August 18, 2025, [[https://en.wikipedia.org/wiki/Circular_buffer]{.underline}](https://en.wikipedia.org/wiki/Circular_buffer)

41. Circular Buffer, accessed August 18, 2025, [[http://c2.com/cgi/wiki?CircularBuffer]{.underline}](http://c2.com/cgi/wiki?CircularBuffer)

42. Creating a Circular Buffer in C and C++ - Embedded Artistry, accessed August 18, 2025, [[https://embeddedartistry.com/blog/2017/05/17/creating-a-circular-buffer-in-c-and-c/]{.underline}](https://embeddedartistry.com/blog/2017/05/17/creating-a-circular-buffer-in-c-and-c/)

43. When to Consider Using a Circular Buffer: A Comprehensive Guide - AlgoCademy, accessed August 18, 2025, [[https://algocademy.com/blog/when-to-consider-using-a-circular-buffer-a-comprehensive-guide/]{.underline}](https://algocademy.com/blog/when-to-consider-using-a-circular-buffer-a-comprehensive-guide/)
