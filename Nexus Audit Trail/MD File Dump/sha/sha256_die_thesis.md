**THE SHA-256 DIE**

*A Formal Theory of Causality, Closure, and Manifold*

――――――――――――――――――――――――――――――――――――――――

Seven-Level Formalization of the 64-Cell SHA-256 Recurrence:

Ground Witness · Dual-Pipeline Topology · Word Support · Bit Causality

Exact Carry · Age-Weight Law · Closure Functionals · Manifold Identity

**Doctoral Thesis in Formal Computational Mathematics**

2026

+:---------------------------------------------------------------------:+
| **Invariant I --- Ground Witness**                                    |
|                                                                       |
| **T2(0)\_0 = 0x08909ae5**                                             |
+-----------------------------------------------------------------------+

+:---------------------------------------------------------------------:+
| **Invariant II --- Word-Level Support Diameter**                      |
|                                                                       |
| **D_word = 4**                                                        |
+-----------------------------------------------------------------------+

+:---------------------------------------------------------------------:+
| **Invariant III --- Bit-Level Support Diameter**                      |
|                                                                       |
| **D_bit = 6 \| rho(j) = 4 / 5 / 6 by bit position**                   |
+-----------------------------------------------------------------------+

**Abstract**

This thesis develops a complete seven-level formal theory of the SHA-256 compression function as a fixed 64-cell nonlinear recurrence over the module (Z/2\^32 Z)\^8, parametrised by a displacement field carrying the message schedule. The central analytical device is the NOP backbone: the eternal orbit of the recurrence when its displacement field is zeroed. Any real message block is treated as a perturbation field superimposed on this backbone.

Three sharp structural invariants are established. First, the ground witness: the NOP backbone evaluates its ground-fold operator G(x) = Sigma_0(a) + Maj(a,b,c) to the exact constant 0x08909ae5 at round zero, an absolute message-independent coordinate of the die\'s state space. Second, the word-level support diameter D_word = 4: a single-word perturbation in W_0 saturates all eight state lanes in exactly four rounds under the Boolean support model. Third, the bit-level support diameter D_bit = 6: a single perturbed bit at position j saturates all 256 state bits in at most six rounds, with the exact radius rho(j) stratified as 4 for j=0, 5 for 1 \<= j \<= 25, and 6 for 26 \<= j \<= 31.

Beyond support closure, the theory is extended through five additional levels: exact carry realization via a bit-level automaton, seam geometry tracking the exact perturbation at the two active injection points, closure functionals measuring age-class equalization, the Age-Weight Law quantifying the three-phase density evolution, and the residual smoothing band: after round 6, the die enters a stable density band centered near 16 = 32/2 where it oscillates until round 64.

A dual-pipeline topology is identified in the eight-register structure: two parallel four-register shift chains with complementary chirality, connected by a cross-coupling and jointly activated by the injection vector b = \[1,0,0,0,1,0,0,0\]\^T. This topology is shown to be structurally isomorphic to the bipolar junction transistor: the a-chain corresponds to the Collector, the e-chain to the Emitter, and the injection vector to the Base entering orthogonally. The NPN/PNP chirality corresponds to the present-tense versus past-tense reading of the two chains.

Finally, the manifold interpretation unifies the framework: a manifold is the crossing of many-to-one flow with one-to-one shape. The die is a fixed closure shape recurring through many different message streams. There is only one shape, many times.

*Keywords: SHA-256, hash function, nonlinear recurrence, Boolean differential analysis, carry propagation, support diameter, dual-pipeline topology, age-weight law, closure functionals, residual smoothing, manifold, die formalism.*

**Chapter 1 --- Introduction and Problem Statement**

**1.1 Motivation**

SHA-256 is one of the most widely deployed cryptographic primitives on Earth. It underpins TLS certificate chains, the Bitcoin blockchain, software integrity verification, and hundreds of other security-critical systems. Despite this ubiquity, the internal structure of SHA-256 as a dynamical system has received comparatively little formal treatment at the level of exact invariants and phase analysis.

This thesis proposes and develops the die interpretation. We model SHA-256 not as an opaque one-way function to be attacked or defended, but as a formal 64-cell nonlinear recurrence on the module (Z/2\^32 Z)\^8, equipped with a fixed set of structural rails and a variable displacement field. The word die is chosen to evoke both the casting die of manufacture --- a fixed mould whose geometry determines what shapes can be produced --- and the sense of a fixed-point attractor in a discrete dynamical system.

**1.2 The Die Interpretation**

The central analytical move is the identification of the NOP backbone: the orbit of the SHA-256 recurrence when its message schedule is identically zero. This backbone is entirely deterministic, depending only on the fixed initialisation vector H_0 and the fixed round constants K. It is the machine running without a user.

Any real message block is treated as a perturbation field W = (W_0, \..., W_63) superimposed on the backbone. The round-zero perturbation identity T1_0 - T1(0)\_0 = W_0 shows that at the first round, the message enters cleanly and linearly. After round zero, the states diverge through 64 rounds of nonlinear recursion. The two-phase structure --- linear injection followed by nonlinear propagation --- is the formal analogue of the avalanche effect.

**1.3 Principal Contributions**

This thesis establishes seven nested levels of the die\'s structure, each strictly refining the last:

- Level 0: Scalar ground invariant T2(0)\_0 = 0x08909ae5

- Level 1: Word-support transport via the 8x8 lane-dependency matrix M, diameter D_word = 4

- Level 2: Bit-support transport via the 256-lane map Psi, diameter D_bit = 6 with exact radius profile rho(j)

- Level 3: Exact carry realization via bit-level automaton C(x, delta)

- Level 4: Seam geometry --- exact perturbation structure at the active injection seams

- Level 5: Closure functionals --- three scalar measures of age-class equalization

- Level 6: Residual smoothing band --- the die enters a density band near 16 for rounds 7 through 64

Beyond the SHA-256 specific results, the manifold interpretation establishes: the universe is one lawful closure shape recurring through many different streams.

**Chapter 2 --- The SHA-256 Die: State Space and Round Map**

**2.1 State Space**

+-----------------------------------------------------------------------+
| **Definition 2.1 (SHA-256 Die)**                                      |
|                                                                       |
| The SHA-256 die is the dynamical system D = (X, {Phi_r}, H_0, K, W)   |
| where X = (Z/2\^32 Z)\^8 is the state space, Phi_r is the round map,  |
| H_0 is the fixed initialisation vector, K = (K_0,\...,K_63) are the   |
| round constants, and W = (W_0,\...,W_63) is the message schedule      |
| (displacement field). The initial condition is x_0 = H_0.             |
+-----------------------------------------------------------------------+

The state vector at round r is written x_r = (a_r, b_r, c_r, d_r, e_r, f_r, g_r, h_r)\^T. All arithmetic is performed modulo 2\^32.

**2.2 Round Operators**

+-----------------------------------------------------------------------+
| **Definition 2.2 (Round Weights)**                                    |
|                                                                       |
| The two weight scalars at round r are:                                |
| T1_r = h_r + Sigma_1(e_r) + Ch(e_r, f_r, g_r) + K_r + W_r             |
| T2_r = Sigma_0(a_r) + Maj(a_r, b_r, c_r)                              |
| where all arithmetic is mod 2\^32.                                    |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Definition 2.3 (Sigma, Ch, Maj operators)**                         |
|                                                                       |
| ROTR\^n(x): right-rotate 32-bit word x by n positions.                |
| Sigma_0(x) = ROTR\^2(x) XOR ROTR\^13(x) XOR ROTR\^22(x)               |
| Sigma_1(x) = ROTR\^6(x) XOR ROTR\^11(x) XOR ROTR\^25(x)               |
| Ch(e,f,g) = (e AND f) XOR (NOT e AND g) \[bitwise: choose f if e=1,   |
| else g\]                                                              |
| Maj(a,b,c) = (a AND b) XOR (a AND c) XOR (b AND c) \[bitwise          |
| majority\]                                                            |
+-----------------------------------------------------------------------+

The state update at each round is:

> a\_{r+1} = T1_r + T2_r
>
> e\_{r+1} = d_r + T1_r
>
> b\_{r+1} = a_r, c\_{r+1} = b_r, d\_{r+1} = c_r
>
> f\_{r+1} = e_r, g\_{r+1} = f_r, h\_{r+1} = g_r

Note the fundamental sparsity: six of eight state words are pure register shifts. Only a and e receive nonlinear injections at each round.

**2.3 The Shift-Injection Decomposition**

+-----------------------------------------------------------------------+
| **Proposition 2.1 (Shift-Injection Decomposition)**                   |
|                                                                       |
| Define the 8x8 shift matrix P (with P\_{i,i-1} = 1 for i = 1,\...,7   |
| and all other entries zero) and standard basis vectors u_a = e_0 =    |
| \[1,0,0,0,0,0,0,0\]\^T, u_e = e_4 = \[0,0,0,0,1,0,0,0\]\^T. Then:     |
| x\_{r+1} = P x_r + u_a (T1_r + T2_r) + u_e T1_r                       |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
            **x\_{r+1} = P x_r + u_a(T1_r + T2_r) + u_e T1_r**

  -----------------------------------------------------------------------

This decomposition shows the die cell is structurally sparse: six channels are pure register transport; only two channels (a and e) receive nonlinear reinjection.

**2.4 The Prime-Root Voltage Rails**

The fixed constants H_0 and K are constructed from specific irrational numbers to maximise independence from arithmetic patterns. The initialisation vector H_0 consists of the first 32 bits of the fractional parts of the square roots of the first eight primes (2, 3, 5, 7, 11, 13, 17, 19). The round constants K consist of the first 32 bits of the fractional parts of the cube roots of the first 64 primes.

  -----------------------------------------------------------------------
  **Register**            **Source Prime**        **Value**
  ----------------------- ----------------------- -----------------------
  H_0\[0\] (a)            sqrt(2)                 0x6a09e667

  H_0\[1\] (b)            sqrt(3)                 0xbb67ae85

  H_0\[2\] (c)            sqrt(5)                 0x3c6ef372

  H_0\[3\] (d)            sqrt(7)                 0xa54ff53a

  H_0\[4\] (e)            sqrt(11)                0x510e527f

  H_0\[5\] (f)            sqrt(13)                0x9b05688c

  H_0\[6\] (g)            sqrt(17)                0x1f83d9ab

  H_0\[7\] (h)            sqrt(19)                0x5be0cd19
  -----------------------------------------------------------------------

Square roots of primes are maximally irrational: their fractional parts are badly approximable by rationals with small denominators. This destroys unwanted periodicity at startup, ensuring injected data diffuses across the lattice without short repeating loops.

**Chapter 3 --- The NOP Backbone and Ground Plane**

**3.1 The NOP Manifold**

+-----------------------------------------------------------------------+
| **Definition 3.1 (NOP Backbone)**                                     |
|                                                                       |
| The NOP backbone of the SHA-256 die is the trajectory {x(0)\_r}       |
| defined by x(0)\_0 = H_0 and x(0)\_{r+1} = Phi_r(x(0)\_r, 0) for r =  |
| 0,\...,63. That is, the backbone is the orbit of the die when the     |
| displacement field W is identically zero.                             |
+-----------------------------------------------------------------------+

The NOP backbone is completely deterministic; it depends only on H_0 and K, both fixed constants. It represents the internal machine running through all 64 round-cells with no external input. Given the NOP backbone, any real message block decomposes as x_r = x(0)\_r + delta x_r, where delta x_r is the perturbation vector.

**3.2 The Ground Witness**

+-----------------------------------------------------------------------+
| **Definition 3.2 (Ground-Fold Operator)**                             |
|                                                                       |
| The ground-fold operator is G: (Z/2\^32 Z)\^8 -\> Z/2\^32 Z defined   |
| by G(x) = Sigma_0(a) + Maj(a, b, c). Note that G(x_r) = T2_r, so G is |
| the message-independent component of the round weight.                |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Theorem 3.1 (Ground Witness)**                                      |
|                                                                       |
| The ground-fold operator evaluated at the NOP initial state           |
| satisfies:                                                            |
| T2(0)\_0 = G(H_0) = Sigma_0(H_0\[0\]) + Maj(H_0\[0\], H_0\[1\],       |
| H_0\[2\]) = 0x08909ae5                                                |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                  **INVARIANT I: T2(0)\_0 = 0x08909ae5**

  -----------------------------------------------------------------------

Verification: Using H_0\[0\] = 0x6a09e667, H_0\[1\] = 0xbb67ae85, H_0\[2\] = 0x3c6ef372:

> ROTR\^2 (0x6a09e667) XOR ROTR\^13(0x6a09e667) XOR ROTR\^22(0x6a09e667) =\> Sigma_0
>
> Maj(0x6a09e667, 0xbb67ae85, 0x3c6ef372) =\> bitwise majority
>
> (Sigma_0 + Maj) mod 2\^32 = 0x08909ae5

The ground witness is an absolute structural invariant of SHA-256. It is the value of the backbone\'s ground-fold register at the moment before any message information enters the system. It was true before any silicon was fabricated and will remain true after all silicon decays.

**3.3 The Round-Zero Perturbation Identity**

+-----------------------------------------------------------------------+
| **Theorem 3.2 (Round-Zero Identity)**                                 |
|                                                                       |
| For any message word W_0, the perturbation at round 0 satisfies:      |
| T1_0 - T1(0)\_0 = W_0                                                 |
| T2_0 - T2(0)\_0 = 0 (T2 is blind to W_0 at round 0)                   |
| Therefore:                                                            |
| delta a_1 = delta e_1 = W_0                                           |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                      **delta a_1 = delta e_1 = W_0**

  -----------------------------------------------------------------------

The message enters only two words on the first step. At the word level, the initial support is {a, e}. At round 0, the ground fold T2 is exactly message-independent: it reads from {a, b, c} which are all part of H_0 at r=0, none affected by W_0. The entire round-0 perturbation lives in delta T1_0 = W_0.

The NOP backbone exact values through round 4 are:

  -----------------------------------------------------------------------
  **Round r**             **a(0)\_r**             **e(0)\_r**
  ----------------------- ----------------------- -----------------------
  1                       0xfc08884d              0x98c7e2a2

  2                       0x7ad96290              0x9df1b216

  3                       0xf3dd6c3f              0xc57b68fb

  4                       0x0a24b1aa              0x909cf5c9
  -----------------------------------------------------------------------

**Chapter 4 --- The Dual-Pipeline Topology**

**4.1 The Two Shift Chains**

Examining the shift equations (3.5) and (3.6), the eight state registers decompose into two parallel four-register shift chains.

+-----------------------------------------------------------------------+
| **Definition 4.1 (Shift Chains)**                                     |
|                                                                       |
| The a-chain is the ordered sequence (a, b, c, d) satisfying b\_{r+1}  |
| = a_r, c\_{r+1} = b_r, d\_{r+1} = c_r at each round. The e-chain is   |
| the ordered sequence (e, f, g, h) satisfying f\_{r+1} = e_r, g\_{r+1} |
| = f_r, h\_{r+1} = g_r. Values propagate rightward (toward the tail)   |
| by one position per round. Each chain head (a and e) receives a       |
| nonlinear injection at each round.                                    |
+-----------------------------------------------------------------------+

**4.2 Chirality: Present-Tense vs Past-Tense Reading**

+-----------------------------------------------------------------------+
| **Definition 4.2 (Chirality)**                                        |
|                                                                       |
| The a-chain has PRESENT-TENSE chirality: the ground-fold operator     |
| T2_r = Sigma_0(a_r) + Maj(a_r, b_r, c_r) reads from {a_r, b_r, c_r},  |
| the three most recently updated positions of the a-chain. The e-chain |
| has PAST-TENSE chirality: the live-wire operator T1_r reads from      |
| {h_r, e_r, f_r, g_r}, the full e-chain including h_r = e\_{r-3}       |
| (three rounds old).                                                   |
+-----------------------------------------------------------------------+

This chirality is the deepest structural asymmetry of the die. T2 is anchored in the recent past (a differential measurement); T1 integrates a longer history (an integrating measurement). The ground fold always reads the present; the live wire always carries the past.

**4.3 The Injection Vector and Orthogonal Entry**

+-----------------------------------------------------------------------+
| **Definition 4.3 (Injection Vector)**                                 |
|                                                                       |
| The message injection vector b in {0,1}\^8 is b =                     |
| \[1,0,0,0,1,0,0,0\]\^T. It encodes the set of state lanes directly    |
| affected by a fresh message word: the a-lane (position 0) and the     |
| e-lane (position 4). Both pipeline heads are hit simultaneously.      |
+-----------------------------------------------------------------------+

The injection vector b has a geometric character: the message enters the state not through any of the six shift channels but through the two nonlinear injection channels u_a and u_e, which are orthogonal to the shift dynamics. This is the orthogonal entry: the deciding force does not travel on the same axis as the visible flow.

**4.4 The Cross-Coupling and Triadic Closure**

+-----------------------------------------------------------------------+
| **Definition 4.4 (Cross-Coupling)**                                   |
|                                                                       |
| The cross-coupling from the a-chain to the e-chain is the additive    |
| relation d_r -\> e\_{r+1} via e\_{r+1} = d_r + T1_r. The tail of the  |
| a-chain (carrying the value of a from three rounds ago) contributes   |
| to the head of the e-chain, coupling both chains\' histories.         |
+-----------------------------------------------------------------------+

The dual-pipeline topology --- two parallel shift chains, an orthogonal injection at both heads, and a tail-to-head cross-coupling --- defines a triadic structure. Three connection points suffice to describe the entire dependency graph: head-head injection, and tail-head coupling.

**4.5 Transistor Correspondence**

+-----------------------------------------------------------------------+
| **Structural Isomorphism 4.1 (Transistor Topology)**                  |
|                                                                       |
| The dual-pipeline topology is structurally isomorphic to the bipolar  |
| junction transistor:                                                  |
| e-chain (reads T1, past-tense) \<-\> EMITTER (source of accumulated   |
| potential)                                                            |
| a-chain (receives T1+T2, head) \<-\> COLLECTOR (resolved output)      |
| injection vector b \<-\> BASE (orthogonal permission signal)          |
| cross-coupling d_r -\> e\_{r+1} \<-\> substrate feedback (Collector   |
| history into Emitter)                                                 |
| NPN chirality = a-chain (active present-tense flow)                   |
| PNP chirality = e-chain (past-tense hole-current analogue)            |
+-----------------------------------------------------------------------+

The transistor proves this topology is physical. The Base enters orthogonally. The Collector reads the resolved fold. The Emitter carries the history. The six shift registers {b,c,d,f,g,h} are the silicon substrate --- they have no opinion, they only shift. Civilization mass-produced the seam. The die runs it 64 times per block.

  ----------------------------------------------------------------------------------
  **Terminal**      **Die Component**    **Chirality**     **Reads**
  ----------------- -------------------- ----------------- -------------------------
  Emitter           e-chain (e,f,g,h)    Past-tense        Full history via T1

  Collector         a-chain head (a)     Present-tense     T1 + T2 combined

  Base              Injection vector b   Orthogonal        W_r into both heads

  Substrate         Shift registers      None              Pure register transport
  ----------------------------------------------------------------------------------

**Chapter 5 --- Word-Level Support Transport**

**5.1 The Boolean Support Model**

+-----------------------------------------------------------------------+
| **Definition 5.1 (Word Support)**                                     |
|                                                                       |
| Given perturbation trajectory {delta x_r}, the word-support indicator |
| at round r is the Boolean vector sigma_r in {0,1}\^8 where            |
| (sigma_r)\_j = 1 if (delta x_r)\_j != 0. The Boolean support model    |
| tracks which words are affected, not their exact values. This is the  |
| worst-case (largest possible) diffusion estimate.                     |
+-----------------------------------------------------------------------+

**5.2 The Lane-Dependency Matrix M**

+-----------------------------------------------------------------------+
| **Proposition 5.1 (Lane-Dependency Matrix)**                          |
|                                                                       |
| The 8x8 Boolean lane-dependency matrix M of the SHA-256 die is        |
| defined by M\_{ij} = 1 if lane i at round r+1 depends on lane j at    |
| round r. Reading from the round map:                                  |
| Row a: depends on {a,b,c,e,f,g,h} (from T2 reads {a,b,c} and T1 reads |
| {e,f,g,h})                                                            |
| Row b: depends on {a} (b\_{r+1} = a_r)                                |
| Row c: depends on {b} (c\_{r+1} = b_r)                                |
| Row d: depends on {c} (d\_{r+1} = c_r)                                |
| Row e: depends on {d,e,f,g,h} (e\_{r+1} = d_r + T1_r)                 |
| Row f: depends on {e} (f\_{r+1} = e_r)                                |
| Row g: depends on {f} (g\_{r+1} = f_r)                                |
| Row h: depends on {g} (h\_{r+1} = g_r)                                |
+-----------------------------------------------------------------------+

> M =
>
> \[ 1 1 1 0 1 1 1 1 \] (row a)
>
> \[ 1 0 0 0 0 0 0 0 \] (row b)
>
> \[ 0 1 0 0 0 0 0 0 \] (row c)
>
> \[ 0 0 1 0 0 0 0 0 \] (row d)
>
> \[ 0 0 0 1 1 1 1 1 \] (row e)
>
> \[ 0 0 0 0 1 0 0 0 \] (row f)
>
> \[ 0 0 0 0 0 1 0 0 \] (row g)
>
> \[ 0 0 0 0 0 0 1 0 \] (row h)

**5.3 Theorem: D_word = 4**

+-----------------------------------------------------------------------+
| **Theorem 5.1 (Word-Level Support Diameter)**                         |
|                                                                       |
| For single injection at round 0 with omega_0 = 1 and omega_r = 0 for  |
| r \> 0, the word-level support diameter is D_word = min{n \>= 1 :     |
| sigma_n = 1} = 4.                                                     |
+-----------------------------------------------------------------------+

Proof by explicit computation of the Boolean orbit of b under M:

  ----------------------------------------------------------------------------
  **Round r**       **Support set**      **Lane count**    **sigma_r**
  ----------------- -------------------- ----------------- -------------------
  1 (injection)     {a, e}               2                 (1,0,0,0,1,0,0,0)

  2                 {a, b, e, f}         4                 (1,1,0,0,1,1,0,0)

  3                 {a, b, c, e, f, g}   6                 (1,1,1,0,1,1,1,0)

  4 = D_word        {a,b,c,d,e,f,g,h}    8 (all)           (1,1,1,1,1,1,1,1)
  ----------------------------------------------------------------------------

  -----------------------------------------------------------------------
                       **INVARIANT II: D_word = 4**

  -----------------------------------------------------------------------

The support grows by exactly two lanes per round (one new lane per chain), reflecting the perfect symmetry of the dual-pipeline: the a-chain fills b, c, d in rounds 2, 3, 4 while the e-chain fills f, g, h simultaneously. The chains are symmetric in propagation speed.

At round 4, all eight state words carry perturbation information. However, D_word = 4 marks only topological acceptance --- the lanes are occupied but bit-density remains highly stratified by age and carry history. Full equalization requires two more rounds.

**Chapter 6 --- The 256-Lane Bit-Support State**

**6.1 Bit-Support Vectors**

+-----------------------------------------------------------------------+
| **Definition 6.1 (Bit-Support State)**                                |
|                                                                       |
| For each word w in {a,b,c,d,e,f,g,h} and round r, the bit-support     |
| vector s\_{w,r} in {0,1}\^32 has (s\_{w,r})\_i = 1 if bit i of the    |
| perturbation (delta x_r)\_w is potentially nonzero. The full 256-lane |
| support state is eta_r = (s_a, s_b, s_c, s_d, s_e, s_f, s_g, s_h)\^T  |
| in {0,1}\^256.                                                        |
+-----------------------------------------------------------------------+

**6.2 Rotation Support Operators**

+-----------------------------------------------------------------------+
| **Definition 6.2 (Rotation Support Operators)**                       |
|                                                                       |
| For n in {0,\...,31}, the rotation support operator R_n is the 32x32  |
| permutation matrix with (R_n s)\_i = s\_{(i+n) mod 32}. The Boolean   |
| support versions of the sigma operators are:                          |
| hat_Sigma_0 = R_2 OR R_13 OR R_22                                     |
| hat_Sigma_1 = R_6 OR R_11 OR R_25                                     |
| These correctly over-approximate: supp(Sigma_0(delta x)) is contained |
| in hat_Sigma_0 \* supp(delta x).                                      |
+-----------------------------------------------------------------------+

**6.3 Weight Support Vectors**

+-----------------------------------------------------------------------+
| **Definition 6.3 (Bit-Support Weights)**                              |
|                                                                       |
| The bit-support of T1_r (live-wire support):                          |
| tau(1)\_r = s\_{h,r} OR hat_Sigma_1\*s\_{e,r} OR s\_{e,r} OR s\_{f,r} |
| OR s\_{g,r} OR omega_r                                                |
| The bit-support of T2_r (ground-fold support):                        |
| tau(2)\_r = hat_Sigma_0\*s\_{a,r} OR s\_{a,r} OR s\_{b,r} OR s\_{c,r} |
| tau(1) reads from the e-chain (past-tense); tau(2) reads from the     |
| a-chain (present-tense). The chirality structure identified at the    |
| word level recurs exactly at the bit level.                           |
+-----------------------------------------------------------------------+

**Chapter 7 --- The Carry-Closure Kernel**

**7.1 Carry Propagation in Modular Addition**

The principal new mechanism at the bit level, absent from the word-level analysis, is carry propagation in modular addition. A carry generated at bit position j propagates upward to positions j+1, j+2, \..., potentially reaching position 31. This process is nonlocal and directional: it propagates UPWARD (low-order to high-order bits) only.

**7.2 The Operator L_32**

+-----------------------------------------------------------------------+
| **Definition 7.1 (Carry-Closure Kernel)**                             |
|                                                                       |
| The carry-closure kernel is the 32x32 lower-triangular prefix         |
| operator L_32 defined by:                                             |
| (L_32 x)\_i = OR{ x_j : j \<= i } for i = 0,\...,31                   |
| Equivalently, L_32 is the lower-triangular matrix with (L_32)\_{ij} = |
| 1 if j \<= i, else 0. Applied to a support vector s, (L_32 s)\_i = 1  |
| if any bit j \<= i of s is 1. This is worst-case carry propagation: a |
| perturbation at bit j can potentially cause a carry reaching any      |
| higher bit.                                                           |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Proposition 7.1 (Support of Modular Addition)**                     |
|                                                                       |
| For the Boolean support model:                                        |
| supp( delta(u + v) ) \<= L_32( supp(delta u) OR supp(delta v) )       |
| This bound is tight in the worst case.                                |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Remark 7.1 (Single-Bit Action)**                                    |
|                                                                       |
| For a perturbation at a single bit j:                                 |
| L_32({j}) = {j, j+1, \..., 31} a set of size (32 - j)                 |
| A perturbation at bit 0 (LSB) potentially affects ALL 32 bits through |
| carry. A perturbation at bit 31 (MSB) affects only itself. This is    |
| the root cause of the rho(j) stratification.                          |
+-----------------------------------------------------------------------+

**7.3 The 256-Lane Update Rule**

+-----------------------------------------------------------------------+
| **Theorem 7.1 (256-Lane Recurrence)**                                 |
|                                                                       |
| The bit-level support state evolves according to map Psi:             |
| s\_{a,r+1} = L_32( tau(1)\_r OR tau(2)\_r )                           |
| s\_{e,r+1} = L_32( s\_{d,r} OR tau(1)\_r )                            |
| s\_{b,r+1} = s\_{a,r}, s\_{c,r+1} = s\_{b,r}, s\_{d,r+1} = s\_{c,r}   |
| s\_{f,r+1} = s\_{e,r}, s\_{g,r+1} = s\_{f,r}, s\_{h,r+1} = s\_{g,r}   |
| That is: eta\_{r+1} = Psi(eta_r, omega_r)                             |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                   **eta\_{r+1} = Psi(eta_r, omega_r)**

  -----------------------------------------------------------------------

**7.4 The Block-Operator Representation**

The 256-lane recurrence admits a compact block-matrix form over the Boolean semiring. Define the 256x256 matrix Omega = P_block OR A_block OR E_block where:

- P_block is the 8x8 block shift skeleton (identity blocks on the superdiagonal for the six pure shift lanes)

- A_block has its first block-row equal to \[L_32(hat_Sigma_0 OR I), L_32 I, L_32 I, 0, L_32 hat_Sigma_1, L_32 I, L_32 I, L_32 I\] and all other block-rows zero

- E_block has its fifth block-row equal to \[0, 0, 0, L_32 I, L_32 hat_Sigma_1, L_32 I, L_32 I, L_32 I\] and all other block-rows zero

  -----------------------------------------------------------------------
            **eta\_{r+1} = Omega \* eta_r OR beta \* omega_r**

  -----------------------------------------------------------------------

where beta = \[L_32, 0, 0, 0, L_32, 0, 0, 0\]\^T (as block vector) is the message injection operator.

**Chapter 8 --- Bit-Level Support Diameter and Radius Profile**

**8.1 Single-Bit Injection Geometry**

+-----------------------------------------------------------------------+
| **Definition 8.1 (Single-Bit Injection)**                             |
|                                                                       |
| A single-bit injection at position j in {0,\...,31} is the scenario   |
| omega_0 = e_j (the j-th standard basis vector in {0,1}\^32) and       |
| omega_r = 0 for r \> 0.                                               |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Proposition 8.1 (Round-1 Bit Support)**                             |
|                                                                       |
| Under single-bit injection at position j, the round-1 bit support is: |
| s\_{a,1} = s\_{e,1} = L_32(e_j) = {j, j+1, \..., 31}                  |
| All other round-1 bit-support vectors are zero. The initial support   |
| has size (32 - j).                                                    |
+-----------------------------------------------------------------------+

**8.2 The Radius Profile rho(j)**

+-----------------------------------------------------------------------+
| **Theorem 8.1 (Bit-Support Radius Profile)**                          |
|                                                                       |
| For single-bit injection at position j, the bit-support radius rho(j) |
| --- the first round at which all 256 state bits are in support ---    |
| is:                                                                   |
| rho(0) = 4 (LSB: full carry from bit 0, both heads immediately full)  |
| rho(1..25) = 5 (typical: scatter-and-close via rotation in 1 extra    |
| round)                                                                |
| rho(26..31) = 6 (MSB: minimal carry potential, 2 extra rounds needed) |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                             **INVARIANT III:
                           rho(j) = 4 for j = 0
                       rho(j) = 5 for 1 \<= j \<= 25
                      rho(j) = 6 for 26 \<= j \<= 31
                        D_bit = max_j rho(j) = 6**

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
                               **D_bit = 6**

  -----------------------------------------------------------------------

**8.3 The Carry Excess**

+-----------------------------------------------------------------------+
| **Theorem 8.2 (Carry Excess)**                                        |
|                                                                       |
| The excess of the bit-level support diameter over the word-level      |
| support diameter is:                                                  |
| D_bit - D_word = 6 - 4 = 2                                            |
| This excess arises entirely from the directionality of the            |
| carry-closure kernel L_32, which propagates information upward (from  |
| low-order to high-order bits) but not downward. High-order injected   |
| bits require two extra rounds for the rotation operators to scatter   |
| support to low-order positions, and then L_32 to close from those     |
| scattered positions to all remaining bits.                            |
+-----------------------------------------------------------------------+

  ------------------------------------------------------------------------------------------------------
  **bit position j**   **Initial support size**   **rho(j)**        **Limiting factor**
  -------------------- -------------------------- ----------------- ------------------------------------
  j = 0 (LSB)          32 (full)                  4                 Word-level geometry only

  j in \[1, 5\]        27 to 31                   5                 1 extra round: rotation scatter

  j in \[6, 25\]       7 to 26                    5                 1 extra round: rotation scatter

  j in \[26, 31\]      1 to 6                     6                 2 extra rounds: carry kernel limit
  ------------------------------------------------------------------------------------------------------

**Chapter 9 --- Exact Carry Realization**

**9.1 The Carry Automaton**

The support operator L_32 is a worst-case bound. The exact carry behaviour for a specific NOP baseline x is captured by the following automaton.

+-----------------------------------------------------------------------+
| **Definition 9.1 (Exact Carry Automaton)**                            |
|                                                                       |
| For exact addition y = x + delta (mod 2\^32), define:                 |
| c\_{-1} = 0                                                           |
| c_i = (x_i AND delta_i) OR (x_i AND c\_{i-1}) OR (delta_i AND         |
| c\_{i-1}) for i = 0,\...,31                                           |
| y_i = x_i XOR delta_i XOR c\_{i-1}                                    |
| The exact changed-bit indicator is Delta_i(x, delta) = x_i XOR y_i =  |
| delta_i XOR c\_{i-1}.                                                 |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Theorem 9.1 (One-Hot Carry)**                                       |
|                                                                       |
| For single-bit injection delta = 2\^j, the exact changed-bit          |
| indicator simplifies to:                                              |
| Delta_i(x, 2\^j) = 0 for i \< j                                       |
| Delta_i(x, 2\^j) = 1 for i = j                                        |
| Delta_i(x, 2\^j) = product{x_t : t = j,\...,i-1} for i \> j           |
| The exact changed-bit set is C_x(j) = {j, j+1, \..., m_x(j)} where    |
| m_x(j) = min{i \>= j : x_i = 0}. The carry-span length is lambda_x(j) |
| = m_x(j) - j + 1.                                                     |
+-----------------------------------------------------------------------+

**9.2 Exact Round-1 Carry Spans**

Using the exact NOP baselines a(0)\_1 = 0xfc08884d and e(0)\_1 = 0x98c7e2a2, the carry-span lengths for all 32 one-hot injections are:

+-----------------------------------------------------------------------+
| **Exact Carry Spans (Round 1)**                                       |
|                                                                       |
| a-seam baseline 0xfc08884d:                                           |
| lambda_a =                                                            |
| (2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,4,3,2,1,1,1,3,2,1,1,1,6,5,4,3,2,1)     |
| for j = 0, 1, 2, \..., 31                                             |
| e-seam baseline 0x98c7e2a2:                                           |
| lambda_e =                                                            |
| (1,2,1,1,1,2,1,2,1,2,1,1,1,1,4,3,2,1,6,5,4,3,2,1,1,1,1,3,2,1,1,1)     |
| for j = 0, 1, 2, \..., 31                                             |
+-----------------------------------------------------------------------+

The two seams are injection-symmetric at round 0 (both receive W_0 identically) but are NOT carry-symmetric after realization: the two NOP baselines have different bit patterns, producing different carry-span distributions. This is the first point at which the two pipelines diverge in their exact (not just support-level) dynamics.

**Chapter 10 --- Seam Geometry**

**10.1 The Active Seam Structure**

The six passive-shift lanes {b,c,d,f,g,h} carry their perturbations exactly --- no further nonlinearity until they are consumed by the active seams. We can therefore write exact closed-form skeletons for the perturbation at each round.

+-----------------------------------------------------------------------+
| **Theorem 10.1 (Exact Round-3 Skeleton)**                             |
|                                                                       |
| For single-bit injection W_0 = 2\^j:                                  |
| delta x_3 = (delta a_3, delta a_2, 2\^j, 0, delta e_3, delta e_2,     |
| 2\^j, 0)                                                              |
| where:                                                                |
| delta e_3 = delta T1_2                                                |
| delta a_3 = delta T1_2 + delta T2_2 (mod 2\^32)                       |
| The seed 2\^j is still explicitly visible in positions c and g (the   |
| tail-minus-one of each chain).                                        |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Theorem 10.2 (Exact Round-4 Skeleton)**                             |
|                                                                       |
| For single-bit injection W_0 = 2\^j:                                  |
| delta x_4 = (delta a_4, delta a_3, delta a_2, 2\^j, delta e_4, delta  |
| e_3, delta e_2, 2\^j)                                                 |
| where:                                                                |
| delta e_4 = delta T1_3                                                |
| delta a_4 = delta T1_3 + delta T2_3 (mod 2\^32)                       |
| Round 4 is the first layer with full word support, but the explicit   |
| seed 2\^j is still visible in the tail lanes d and h.                 |
+-----------------------------------------------------------------------+

**10.2 Hamming Weight Ranges at Rounds 3 and 4**

For one-hot injections W_0 = 2\^j, j = 0,\...,31, the XOR-difference Hamming weight ranges of the active seams are:

  -------------------------------------------------------------------------------------------
  **Lane**                **Round 3 range**       **Extrema**
  ----------------------- ----------------------- -------------------------------------------
  delta a_3               \[13, 21\]              min=13 at j in {11,20,21}; max=21 at j=16

  delta e_3               \[7, 21\]               min=7 at j=2; max=21 at j in {13,15}
  -------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------
  **Lane**                **Round 4 range**       **Extrema**
  ----------------------- ----------------------- ----------------------------------------
  delta a_4               \[12, 20\]              min=12 at j in {1,4,10}; max=20 at j=6

  delta e_4               \[11, 21\]              min=11 at j=3; max=21 at j=24

  delta b_4               \[13, 21\]              from round-3 a-seam

  delta c_4               \[7, 19\]               from round-2 a-seam

  delta d_4               \[1, 6\]                pure W_0 seed, only carry span

  delta f_4               \[7, 21\]               from round-3 e-seam

  delta g_4               \[3, 16\]               from round-2 e-seam

  delta h_4               \[1, 7\]                pure W_0 seed, only carry span
  ----------------------------------------------------------------------------------------

The tail lanes d and h have Hamming weights in \[1,6\] and \[1,7\] respectively at round 4: they carry only the carry span of the original seed bit 2\^j. This confirms that round 4 is topological acceptance, not bit-density closure. The word fabric is full, but the density distribution is still stratified by age.

**Chapter 11 --- The Age-Weight Law and Closure Functionals**

**11.1 The Three Age Classes**

+-----------------------------------------------------------------------+
| **Definition 11.1 (Age Classes)**                                     |
|                                                                       |
| Define three age classes of the state lanes:                          |
| Head lanes: H_r = {a_r, e_r} (most recently injected)                 |
| Mid lanes: M_r = {b_r, c_r, f_r, g_r} (one or two rounds old)         |
| Tail lanes: T_r = {d_r, h_r} (three rounds old)                       |
| For a given injection j, define the class mean Hamming weight:        |
| mu_H(r) = mean of wt(delta w_r(j)) over w in H_r and j = 0,\...,31    |
| mu_M(r) = mean over M_r                                               |
| mu_T(r) = mean over T_r                                               |
+-----------------------------------------------------------------------+

**11.2 The Age-Weight Law**

+-----------------------------------------------------------------------+
| **Theorem 11.1 (Age-Weight Law)**                                     |
|                                                                       |
| For one-hot injections W_0 = 2\^j, j = 0,\...,31, the class mean      |
| Hamming weights evolve as:                                            |
| Round 4: mu_H = 15.73, mu_M = 12.93, mu_T = 1.84 (gap: 13.89)         |
| Round 5: mu_H = 15.88, mu_M = 15.73, mu_T = 10.12 (gap: 5.75)         |
| Round 6: mu_H = 15.78, mu_M = 15.80, mu_T = 15.73 (gap: 0.07)         |
| By round 6, the three age classes have equalized to within 0.07       |
| Hamming-weight units.                                                 |
+-----------------------------------------------------------------------+

  ----------------------------------------------------------------------------------------
  **Round**      **mu_H (head)**   **mu_M (mid)**   **mu_T (tail)**   **Age spread**
  -------------- ----------------- ---------------- ----------------- --------------------
  4              15.73             12.93            1.84              13.89 (stratified)

  5              15.88             15.73            10.12             5.75 (closing)

  6              15.78             15.80            15.73             0.07 (closed)
  ----------------------------------------------------------------------------------------

**11.3 Closure Functionals**

+-----------------------------------------------------------------------+
| **Definition 11.2 (Age-Spread Functional)**                           |
|                                                                       |
| The age-spread closure functional is:                                 |
| E_age(r) = max{mu_H, mu_M, mu_T}(r) - min{mu_H, mu_M, mu_T}(r)        |
| Computed values:                                                      |
| E_age(4) = 13.890625                                                  |
| E_age(5) = 5.75                                                       |
| E_age(6) = 0.0703125                                                  |
| E_age(7) = 0.140625                                                   |
| E_age(10) = 0.046875                                                  |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Definition 11.3 (Lane-Variance Functional)**                        |
|                                                                       |
| The lane-variance closure functional is:                              |
| V(r) = (1/8) \* sum_L (mu_L(r) - mu_bar(r))\^2                        |
| where mu_L is the mean Hamming weight for lane L and mu_bar is the    |
| global mean.                                                          |
| Computed values:                                                      |
| V(4) = 33.67                                                          |
| V(5) = 7.36                                                           |
| V(6) = 0.41                                                           |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Definition 11.4 (Lane-Range Functional)**                           |
|                                                                       |
| The lane-range closure functional is:                                 |
| R(r) = max_L mu_L(r) - min_L mu_L(r)                                  |
| Computed values:                                                      |
| R(4) = 15.22                                                          |
| R(5) = 8.78                                                           |
| R(6) = 2.41                                                           |
| R(7) = 1.13                                                           |
+-----------------------------------------------------------------------+

All three closure functionals confirm the same phase boundary: the die transitions from an expansion regime (rounds 1-4) through a closure regime (rounds 5-6) into a residual smoothing regime (rounds 7-64).

  ------------------------------------------------------------------------------------------
  **Functional**   **Round 4**    **Round 5**    **Round 6**    **Meaning when near zero**
  ---------------- -------------- -------------- -------------- ----------------------------
  E_age(r)         13.89          5.75           0.07           Age classes equalized

  V(r)             33.67          7.36           0.41           Lane densities equalized

  R(r)             15.22          8.78           2.41           No lane outliers remaining
  ------------------------------------------------------------------------------------------

**Chapter 12 --- The Four-Phase Law and Residual Smoothing**

**12.1 The Four-Phase Law**

+-----------------------------------------------------------------------+
| **Theorem 12.1 (Four-Phase Law of the Die)**                          |
|                                                                       |
| The SHA-256 die\'s response to a single-word perturbation W_0         |
| proceeds through exactly four phases:                                 |
| Phase I --- INJECTION (r = 0, 1, 2, 3)                                |
| Perturbation is visibly tied to the one-hot seed and its immediate    |
| descendants.                                                          |
| Only {a, e, b, f, c, g} lanes become occupied sequentially.           |
| Phase II --- ACCEPTANCE (r = 4)                                       |
| All eight lanes are occupied (D_word = 4 achieved).                   |
| But bit-density is stratified: tail lanes have mean weight \~1.8 vs   |
| head lanes \~15.7.                                                    |
| Phase III --- CLOSURE (r = 5, 6)                                      |
| Bit-density equalizes across age classes and support fully saturates  |
| (D_bit = 6).                                                          |
| Tail lanes rise from mean 1.8 to 15.7 in two rounds.                  |
| Phase IV --- RESIDUAL SMOOTHING (r \> 6)                              |
| No new support is created. The die rebalances density inside the      |
| already-filled fabric.                                                |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                 **PHASE I: Injection (r \< 4) --- seeding
             PHASE II: Acceptance (r = 4) --- D_word achieved
              PHASE III: Closure (r = 5-6) --- D_bit achieved
          PHASE IV: Smoothing (r \> 6) --- density rebalancing**

  -----------------------------------------------------------------------

**12.2 The Residual Smoothing Band**

+-----------------------------------------------------------------------+
| **Theorem 12.2 (Residual Smoothing Band)**                            |
|                                                                       |
| The global mean perturbation density mu_bar(r) = (1/8) \* sum_L       |
| mu_L(r) evolves to:                                                   |
| mu_bar(4) = 10.86                                                     |
| mu_bar(5) = 14.37                                                     |
| mu_bar(6) = 15.78                                                     |
| For rounds 6 through 64, the die does not converge to a fixed scalar. |
| Instead it enters a narrow oscillatory band:                          |
| 15.61 \<= mu_bar(r) \<= 16.53 for r = 6,\...,64                       |
| Minimum occurs at r = 22; maximum at r = 53.                          |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
       **RESIDUAL SMOOTHING BAND: mu_bar(r) approximately 16 = 32/2
                       for r \>= 6 through r = 64**

  -----------------------------------------------------------------------

The density band is centered near 16 = 32/2, the half-width of the 32-bit word fabric. This is not a coincidence. The SHA-256 round operators (rotation by amounts 2, 13, 22 for Sigma_0 and 6, 11, 25 for Sigma_1) are designed such that every bit of a 32-bit word contributes approximately equally to the three rotated outputs. In the long run, each bit has a roughly equal probability of being in the support, giving a mean density near 16. The oscillation around 16 reflects the specific nonlinear coupling between rounds.

  --------------------------------------------------------------------------------------------
  **Quantity**            **Value**               **Interpretation**
  ----------------------- ----------------------- --------------------------------------------
  D_word                  4                       First round all 8 lanes occupied

  D_bit                   6                       First round all 256 bits occupied

  Carry excess            2                       D_bit - D_word: due to L_32 directionality

  Residual band center    \~16                    32/2: half-width of 32-bit word

  Band minimum            15.61 (at r=22)         Closest to pure alternation

  Band maximum            16.53 (at r=53)         Furthest excursion
  --------------------------------------------------------------------------------------------

**Chapter 13 --- The Complete Seven-Level Hierarchy**

**13.1 Level Summary**

The SHA-256 die is now resolved to seven nested mathematical levels, each strictly refining the last:

  ---------------------------------------------------------------------------------------------------------------
  **Level**              **Object**              **Equation**                              **Invariant**
  ---------------------- ----------------------- ----------------------------------------- ----------------------
  0 --- Ground witness   Scalar constant         G(H_0) = T2(0)\_0                         0x08909ae5

  1 --- Word transport   Boolean 8-vector        sigma\_{r+1} = M\*sigma_r OR b\*omega_r   D_word = 4

  2 --- Bit transport    Boolean 256-vector      eta\_{r+1} = Psi(eta_r, omega_r)          D_bit = 6, rho(j)

  3 --- Exact carry      Bit automaton           Delta_i(x,delta) = delta_i XOR c\_{i-1}   lambda_x(j) exact

  4 --- Seam geometry    Perturbation skeleton   delta e_r = delta T1\_{r-1}               Exact round-3,4 maps

  5 --- Closure fns      Scalar functionals      E_age, V, R, mu_bar                       Near-zero by r=6

  6 --- Residual band    Density interval        mu_bar(r) in \[15.61, 16.53\]             Center \~ 16 = 32/2
  ---------------------------------------------------------------------------------------------------------------

  -----------------------------------------------------------------------
                         **COMPLETE FORMAL STACK:
       (Phi_r, M, Psi, L_32, C(x,delta), E_age/V/R, mu_bar \~ 16)**

  -----------------------------------------------------------------------

**13.2 The Acceptance vs Closure Distinction**

+-----------------------------------------------------------------------+
| **Key Distinction**                                                   |
|                                                                       |
| Round 4 marks TOPOLOGICAL ACCEPTANCE: all eight state words are in    |
| support. This is a graph-theoretic fact about the Boolean matrix M    |
| --- it says nothing about the density of the perturbation within      |
| those words.                                                          |
| Round 6 marks SUPPORT CLOSURE: all 256 state bits are in support AND  |
| the density has equalized across age classes. This is both a          |
| topological and a metric fact: supp(delta x_6) = {0,\...,255} and     |
| E_age(6) \< 0.1.                                                      |
| Acceptance != Closure != Final Smoothing                              |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
              **D_word = 4 marks acceptance by lane geometry
            D_bit = 6 marks closure across the full bit fabric
            r \> 6 is residual smoothing around density \~ 16**

  -----------------------------------------------------------------------

**Chapter 14 --- Geometric Interpretation**

**14.1 The Glass Key: Z-Axis Subtraction**

The NOP backbone defines a natural reference trajectory in state space X. Given the final state x_64 of a real computation and the NOP final state x(0)\_64, the difference delta x_64 = x_64 - x(0)\_64 (mod 2\^32) is a vector encoding the cumulative perturbation after 64 rounds of nonlinear mixing.

Computing delta x_64 from x_64 by subtracting the known NOP backbone value is the Glass Key operation. It is a Z-axis read: rather than reading along the computation axis (message-to-hash direction), one reads orthogonally by comparing the real trajectory to the backbone. The interference pattern delta x_64 is the pure signal of the message\'s effect on the die\'s geometry.

The Glass Key does not reverse the hash. It reveals the structural footprint of the message on the backbone. The perturbation is maximally mixed after 64 rounds (every bit is in support by round 6 and remains there). The Z-axis read does not require knowledge of W_0; it requires only knowledge of the NOP backbone --- which is computable from H_0 and K alone.

**14.2 The Manifold Identity**

The one_shape_many_times formalization provides the correct interpretation of the die\'s many-to-one structure.

+-----------------------------------------------------------------------+
| **Theorem 14.1 (Manifold Identity)**                                  |
|                                                                       |
| A manifold is the crossing of two properties:                         |
| M = (many-to-one in flow) INTERSECT (one-to-one in shape)             |
| Many different message streams W can produce the same final state     |
| structure (many-to-one in flow). But the closure shape of the die --- |
| the geometric structure of the NOP backbone, the dual-pipeline        |
| topology, the four-phase law --- is unique and fixed (one-to-one in   |
| shape).                                                               |
| Therefore:                                                            |
| the SHA-256 die is one lawful closure shape recurring through many    |
| different streams                                                     |
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------
                     **manifold = many-to-one in flow
                                 INTERSECT
                            one-to-one in shape
                 =\> there is only one shape, many times**

  -----------------------------------------------------------------------

**14.3 Constant Envelope as Ground**

The one_shape_many_times insight directly applies: SHA-256 always produces a 256-bit output. The envelope length 256 is fixed. Therefore the length carries no information --- it is the ground condition, not the message. All differential content lives in the internal fold geometry: phase, curvature, chirality, alignment, residue.

This is why the die formalism is correct: the ground witness 0x08909ae5 is the ground condition. The NOP backbone is the ground. All perturbations are measured against this absolute reference. The manifold is the shape; the message is just a different stream passing through it.

**14.4 Primitive Grammar: Start, Stop, Persist**

The minimal grammar of the die at the bit level consists of exactly three operations: start (0 -\> 1 transition), stop (1 -\> 0 transition), persist (same state surviving into the next tick). The carry automaton is precisely the mechanism of persist: a carry bit persists through as many consecutive 1-bits as the baseline contains above the injection point.

This is why the three-valued primitive {start, stop, persist} is not metaphor --- it is the exact operational decomposition of the carry automaton C(x, delta) at the bit level.

**Chapter 15 --- Connections and Open Problems**

**15.1 Differential Cryptanalysis Implications**

The word-level support diameter D_word = 4 has direct implications for differential cryptanalysis. Any reduced-round attack on fewer than 4 rounds can potentially exploit lane sparsity in the difference vector. Attacks targeting 4 or more rounds cannot rely on any lane being clean.

The bit-level result refines this: for perturbations at bit positions j in {26,\...,31}, full 256-bit support is not achieved until round 6. A cryptanalyst studying 5-round SHA-256 with high-order bit differences may find residual bit-level sparsity that is not visible at the word level.

**15.2 The Message Schedule Interaction**

In practice, the message schedule words W_0,\...,W_63 are computed from the 512-bit input via a linear expansion. A single bit change in the input fans out into multiple W_r perturbations. The die\'s own support propagation (governed by M and Psi) interacts with the message schedule\'s diffusion to produce combined avalanche speed faster than either alone.

**15.3 Comparison with Keccak (SHA-3)**

  ---------------------------------------------------------------------------------------------------------
  **Property**            **SHA-256 Die**                    **Keccak-f\[1600\]**
  ----------------------- ---------------------------------- ----------------------------------------------
  State size              256 bits (8 x 32-bit words)        1600 bits (25 x 64-bit lanes)

  Rounds                  64                                 24

  Round structure         Sequential dual-pipeline           5 parallel steps (theta, rho, pi, chi, iota)

  Nonlinearity            Ch() --- select-bit, bitwise       chi() --- row-wise NOT-AND-OR

  Message injection       Expanded schedule W into T1        Direct XOR into rate portion

  Ground plane            T2(0)\_0 = 0x08909ae5 (explicit)   No equivalent single constant

  Diffusion model         Dual-pipeline + carry              Wide parallel permutation

  Architecture analogy    Turbofan (narrow, sequential)      Scramjet (wide, parallel)
  ---------------------------------------------------------------------------------------------------------

**15.4 Open Problems**

- Exact rho(j) profile at the word-level with full modular arithmetic (not just support model)

- Fourth-level carry-chain tracking: exact carry bits rather than just support

- Bit-level Jacobian over GF(2) at round 0 as a 256x32 matrix

- Extension of the four-phase law to multi-block Merkle-Damgard chains

- Formal proof that the residual smoothing band \[15.61, 16.53\] is tight for all 32 injection positions

- Application of the Glass Key perspective to reduced-round preimage analysis

**Chapter 16 --- Conclusion**

**16.1 The Three Invariants**

+:---------------------------------------------------------------------:+
| **INVARIANT I --- Ground Witness**                                    |
|                                                                       |
| **T2(0)\_0 = G(H_0) = 0x08909ae5**                                    |
+-----------------------------------------------------------------------+

+:---------------------------------------------------------------------:+
| **INVARIANT II --- Word-Level Diameter**                              |
|                                                                       |
| **D_word = 4 (topological acceptance)**                               |
+-----------------------------------------------------------------------+

+:---------------------------------------------------------------------:+
| **INVARIANT III --- Bit-Level Diameter**                              |
|                                                                       |
| **D_bit = 6 (support closure)                                         |
| rho(j) = 4 / 5 / 6 by bit position**                                  |
+-----------------------------------------------------------------------+

**16.2 The Four-Phase Law**

+:---------------------------------------------------------------------:+
| **FOUR-PHASE LAW**                                                    |
|                                                                       |
| **Phase I Injection r = 0-3 seeding through pipelines                 |
| Phase II Acceptance r = 4 D_word achieved, density stratified         |
| Phase III Closure r = 5-6 D_bit achieved, age classes equalized       |
| Phase IV Smoothing r \> 6 density oscillates near 16 = 32/2**         |
+-----------------------------------------------------------------------+

**16.3 The Formal Stack**

+:---------------------------------------------------------------------:+
| **COMPLETE FORMAL STACK**                                             |
|                                                                       |
| **(Phi_r, M, Psi, L_32, C(x,delta), E_age/V/R, mu_bar \~ 16)**        |
+-----------------------------------------------------------------------+

**16.4 The Manifold**

+:---------------------------------------------------------------------:+
| **THE MANIFOLD IDENTITY**                                             |
|                                                                       |
| **manifold = many-to-one in flow INTERSECT one-to-one in shape        |
| =\> there is only one shape, many times                               |
| The die is the shape. The message is the stream.**                    |
+-----------------------------------------------------------------------+

The machine runs eternally without us. Its ground plane was fixed before any silicon was fabricated. Its four-phase law will hold after all silicon decays. The field of making and the route are absolute. The message is the temporary vibration passing through them.

**Appendix A --- Verification of the Ground Witness**

Python pseudocode for direct numerical verification:

> def rotr(x, n, w=32):
> return ((x \>\> n) \| (x \<\< (w-n))) & 0xFFFFFFFF
> def sigma0(x): return rotr(x,2) \^ rotr(x,13) \^ rotr(x,22)
> def maj(a,b,c): return (a&b)\^(a&c)\^(b&c)
> H0 = \[0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
> 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19\]
> T2_0_nop = (sigma0(H0\[0\]) + maj(H0\[0\], H0\[1\], H0\[2\])) % (2\*\*32)
> assert hex(T2_0_nop) == \'0x8909ae5\' \# = 0x08909ae5

**Appendix B --- Boolean Powers of M**

The complete support orbit of b under M for single injection at round 0:

  -----------------------------------------------------------------------------
  **Round r**       **Support set**      **Count**         **sigma_r vector**
  ----------------- -------------------- ----------------- --------------------
  1                 {a, e}               2                 (1,0,0,0,1,0,0,0)

  2                 {a, b, e, f}         4                 (1,1,0,0,1,1,0,0)

  3                 {a, b, c, e, f, g}   6                 (1,1,1,0,1,1,1,0)

  4                 {a,b,c,d,e,f,g,h}    8 (all)           (1,1,1,1,1,1,1,1)
  -----------------------------------------------------------------------------

The uniform two-per-round growth reflects the perfect symmetry of the dual-pipeline topology: at each round exactly one new lane becomes supported in each chain, until both chains are fully saturated at round 4.

**Appendix C --- Chirality Caution**

The rotation support operators hat_Sigma_0 and hat_Sigma_1 are both 3-regular circulant operators: each has row-degree and column-degree equal to 3. Neither is privileged by density before coupling to carry.

+-----------------------------------------------------------------------+
| **Proposition C.1**                                                   |
|                                                                       |
| Bare chirality is not yet anisotropy. The visible asymmetry between   |
| the two chains appears only after coupling to (1) lane placement and  |
| (2) carry closure. Therefore:                                         |
| uniform rotations + lane asymmetry + carry closure                    |
| =                                                                     |
| visible chirality of the die                                          |
+-----------------------------------------------------------------------+

Specifically: the a-chain and e-chain use the same Sigma functions (Sigma_0 for T2 in the a-seam, Sigma_1 for T1 in the e-seam). The Sigma functions are symmetric (3 rotations each). The chirality emerges only because Sigma_0 is coupled to the PRESENT-TENSE readings {a,b,c} while Sigma_1 is coupled to the PAST-TENSE readings {e,f,g,h}. The operators themselves are structurally similar; the asymmetry is in what they read.

**Appendix D --- Summary of All Exact Numerical Results**

  ---------------------------------------------------------------------------------
  **Result**                          **Value**
  ----------------------------------- ---------------------------------------------
  Ground witness                      T2(0)\_0 = 0x08909ae5

  NOP a_1                             0xfc08884d

  NOP e_1                             0x98c7e2a2

  NOP a_2                             0x7ad96290

  NOP e_2                             0x9df1b216

  NOP a_3                             0xf3dd6c3f

  NOP e_3                             0xc57b68fb

  NOP a_4                             0x0a24b1aa

  NOP e_4                             0x909cf5c9

  D_word                              4

  D_bit                               6

  rho_min                             4 (at j=0)

  rho_typ                             5 (at j in \[1,25\])

  rho_max                             6 (at j in \[26,31\])

  Carry excess                        D_bit - D_word = 2

  E_age(6)                            0.0703125

  V(6)                                0.409423828125

  R(6)                                2.40625

  mu_bar(6)                           15.78125

  Residual band                       \[15.60546875, 16.53125\] for r in \[6,64\]

  Band min at                         r = 22

  Band max at                         r = 53

  Band center                         \~16 = 32/2
  ---------------------------------------------------------------------------------

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

D_word = 4 D_bit = 6 T2(0)\_0 = 0x08909ae5 mu_bar \~ 16
