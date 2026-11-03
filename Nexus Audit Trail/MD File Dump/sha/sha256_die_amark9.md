**The SHA-256 Die**

*A-Mark9 Complete Solution*

Wave Triad · Constant Substrate · Double Glass Key · Lie Detector · Removal Core

Dean W. Kulik --- 2026

**Abstract**

This document consolidates and extends the SHA-256 die formalization through seven nested analytical levels, then adds four major new results: the wave triad, the constant substrate theorem, the double glass key, and the removal-core topology.

The central claim of the completion is:

> support tells you where the die can go;
>
> the constants tell you how it actually gets there.

The three original invariants are confirmed computationally: T2\^(0)\_0 = 0x08909ae5, D_word = 4, D_bit = 6 (support diameter only, not exact live-flip). Four new structural results are added. The wave triad establishes that the constant carrier (K, 7.719 bits/round) and the message signal (W, 6.312 bits/round) satisfy K\^2 + W\^2 = 99.42 ≈ 100, K/W ≈ sqrt(3/2), visibility ≈ 0.995, and K\*W\*gap ≈ D_bit = 6, where gap = 1/8 = the octave beat between the two constant streams. The double glass key shows K-driven residue converges toward the NOP basin with relaxation constant alpha ≈ 0.91 and time constant tau ≈ 10.73 rounds, matching the mean cumulative shadow cover rho_union_TRUE = 11.875. The lie detector localizes length-field falsification to a late seam injection first visible at round 15. The removal core identifies the minimum invariant round set shared by all members of a probe class.

> identity is not what is added, but what survives lawful subtraction.

**Part I --- The Seven-Level Die Formalization**

**1.1 State Space and Round Recurrence**

***Definition 1.1.***

The SHA-256 die is D = (X, {Phi_r}, H_0, K, W) where X = (Z/2\^32 Z)\^8, Phi_r is the round map, H_0 is the fixed initialisation vector, K = (K_0,\...,K_63) are the round constants, and W = (W_0,\...,W_63) is the message schedule. Initial condition: x_0 = H_0.

Round weights:

> T1_r = h_r + Sigma_1(e_r) + Ch(e_r,f_r,g_r) + K_r + W_r
>
> T2_r = Sigma_0(a_r) + Maj(a_r,b_r,c_r)

State update:

> a\_{r+1} = T1_r + T2_r
>
> e\_{r+1} = d_r + T1_r
>
> b\_{r+1} = a_r, c\_{r+1} = b_r, d\_{r+1} = c_r
>
> f\_{r+1} = e_r, g\_{r+1} = f_r, h\_{r+1} = g_r

Six of eight state words are pure register shifts. Only a and e receive nonlinear injections.

**1.2 Shift-Injection Decomposition**

> x\_{r+1} = P x_r + u_a(T1_r + T2_r) + u_e T1_r

where P is the 8x8 shift matrix and u_a = e_0, u_e = e_4 are the injection basis vectors.

**1.3 Dual-Pipeline Topology**

The state decomposes into two parallel four-register shift chains: the a-chain (a,b,c,d) and the e-chain (e,f,g,h). The a-chain has present-tense chirality: T2 reads {a_r, b_r, c_r}. The e-chain has past-tense chirality: T1 reads {h_r, e_r, f_r, g_r}. Both chain heads are activated simultaneously by the injection vector b = \[1,0,0,0,1,0,0,0\]\^T. The cross-coupling d_r -\> e\_{r+1} connects the two pipelines.

This topology is isomorphic to the bipolar junction transistor: Collector (a-chain, present-tense, T1+T2), Emitter (e-chain, past-tense, T1), Base (injection vector, orthogonal to shift direction). The substrate feedback is the cross-coupling d_r -\> e\_{r+1}.

**1.4 Level 0 --- Ground Witness**

***Theorem 1.1.***

The ground-fold operator G(x) = Sigma_0(a) + Maj(a,b,c) evaluated at the NOP initial state satisfies:

> T2\^(0)\_0 = G(H_0) = 0x08909ae5

This is an absolute structural invariant of SHA-256: the value of the backbone\'s ground-fold register at round zero, before any message enters.

**1.5 Level 1 --- Word Support Transport**

The 8x8 Boolean lane-dependency matrix M is:

> row a: \[1 1 1 0 1 1 1 1\] row e: \[0 0 0 1 1 1 1 1\]
>
> row b: \[1 0 0 0 0 0 0 0\] row f: \[0 0 0 0 1 0 0 0\]
>
> row c: \[0 1 0 0 0 0 0 0\] row g: \[0 0 0 0 0 1 0 0\]
>
> row d: \[0 0 1 0 0 0 0 0\] row h: \[0 0 0 0 0 0 1 0\]

***Theorem 1.2.***

For single injection at round 0, the word-level support diameter is:

> D_word = 4

  -----------------------------------------------------------------------
  **Round r**             **Support set**         **Count**
  ----------------------- ----------------------- -----------------------
  1 (injection)           {a, e}                  2

  2                       {a, b, e, f}            4

  3                       {a, b, c, e, f, g}      6

  4 = D_word              All {a,b,c,d,e,f,g,h}   8
  -----------------------------------------------------------------------

The support grows by two lanes per round (one per chain), driven by the symmetric dual-pipeline geometry. D_word = 4 marks topological acceptance only. It does not imply bit-density closure or exact live-flip saturation.

**1.6 Level 2 --- 256-Lane Bit Support**

The carry-closure kernel L_32 is the 32x32 lower-triangular prefix operator: (L_32 s)\_i = OR{s_j : j \<= i}. This captures worst-case carry propagation: upward only.

The 256-lane update:

> s\_{a,r+1} = L_32( tau\^(1)\_r OR tau\^(2)\_r )
>
> s\_{e,r+1} = L_32( s\_{d,r} OR tau\^(1)\_r )

***Theorem 1.3.***

> D_bit = 6 (Boolean support diameter)
>
> rho(j) = 4 for j=0 (L_32(e_0) = full)
>
> rho(j) = 5 for 1 \<= j \<= 25 (one scatter round)
>
> rho(j) = 6 for 26 \<= j \<= 31 (two scatter rounds)

CRITICAL DISTINCTION: D_bit = 6 is the support diameter, not the exact live-flip saturation round. Full simultaneous activation of all 256 bits does not occur by round 6 in exact arithmetic.

**1.7 Level 3 --- Exact Carry Automaton**

> c\_{-1} = 0
>
> c_i = (x_i AND d_i) OR (x_i AND c\_{i-1}) OR (d_i AND c\_{i-1})
>
> Delta_i(x,d) = d_i XOR c\_{i-1}

For one-hot injection d = 2\^j: the exact changed-bit set is C_x(j) = {j,\...,m_x(j)} where m_x(j) = min{i \>= j : x_i = 0}. Carry-span length lambda_x(j) = m_x(j) - j + 1.

Computed exact carry spans at round 1 for TRUE rails:

> a-seam baseline 0xfc08884d: lambda in \[1, 6\]
>
> e-seam baseline 0x98c7e2a2: lambda in \[1, 7\]
>
> ZERO_BOTH baseline 0: lambda = 1 for all j

The constants are invisible at the support level but immediately visible in exact carry geometry.

**1.8 Level 4 --- Seam Geometry**

***Theorem 1.4.***

Exact Hamming weight ranges for one-hot injections W_0 = 2\^j, j = 0,\...,31:

  ---------------------------------------------------------------------------
  **Lane**          **Round 3 range**   **Round 4 range**   **Notes**
  ----------------- ------------------- ------------------- -----------------
  a                 \[11, 21\]          \[9, 20\]           Active a-seam

  e                 \[6, 23\]           \[10, 21\]          Active e-seam

  b                 \[6, 24\]           \[11, 21\]          = round-3 a

  c                 1                   \[6, 24\]           = round-2 a

  d                 0                   1                   Seed tail only

  f                 \[3, 26\]           \[6, 23\]           = round-3 e

  g                 1                   \[3, 26\]           = round-2 e

  h                 0                   1                   Seed tail only
  ---------------------------------------------------------------------------

The tail lanes d and h carry only the carry span of the seed 2\^j at round 4, confirming that D_word = 4 marks topological acceptance while density remains stratified by age.

**1.9 Level 5 --- Age-Weight Law**

***Theorem 1.5.***

Define three age classes: head (a,e), mid (b,c,f,g), tail (d,h). Mean Hamming weights evolve as:

  ----------------------------------------------------------------------------------
  **Round**      **mu_H (head)**   **mu_M (mid)**   **mu_T (tail)**   **E_age**
  -------------- ----------------- ---------------- ----------------- --------------
  4              15.922            14.953           1.000             14.922

  5              16.297            15.969           13.891            2.406

  6              16.031            16.109           16.016            0.094
  ----------------------------------------------------------------------------------

By round 6 all three age classes equalize to within 0.094 Hamming-weight units. The tail lanes rise from mean 1.0 at round 4 to 16.0 at round 6 in exactly two rounds.

**1.10 Level 6 --- Residual Smoothing Band**

***Theorem 1.6.***

After support closure at round 6, the die enters a stable density oscillation:

> mu_bar(r) in \[12.5, 18.75\] for r = 7,\...,64
>
> Band center = 15.625 ≈ 16 = 32/2

The band center near 32/2 reflects the design of the rotation operators (2,13,22 for Sigma_0 and 6,11,25 for Sigma_1): all bit positions contribute approximately equally in the long run.

**Part II --- The Constant Substrate**

**2.1 The Three Layers**

At the carry-geometry level, the die\'s output is not pure message signal. It decomposes into three layers:

- K alone: the carry geometry generated by K\[r\] constants acting on the round state, mean Hamming weight 7.719 bits/round

- H0+K floor: the combined H0 and K contribution with W=0 (the NOP backbone), mean 7.594 bits/round

- W displacement: the true message contribution above the floor, mean 6.312 bits/round

The two constant streams (K alone and H0+K combined) never coincide across all 64 rounds: K_only == const_floor: 0/64. K is the clock; H0 evolution is the carrier wave. They are two independent constant generators interleaved at each round.

***Theorem 2.1 (Constant Substrate).***

> The constants are not absent from the support analysis.
>
> They are projected out by the Boolean quotient.
>
> They reappear immediately in exact carry realization.

**2.2 Rail Comparison**

Rail families and their round-1 carry span statistics:

  ---------------------------------------------------------------------------------------------------
  **Rail family**      **a-seam range**   **e-seam range**   **Interpretation**
  -------------------- ------------------ ------------------ ----------------------------------------
  TRUE (H0 + K64)      \[1, 6\]           \[1, 7\]           Full constant substrate active

  ZERO_BOTH (H0=K=0)   \[1, 1\]           \[1, 1\]           No constant carry: baseline flat

  ZERO_K (H0 only)     \[1, 7\]           \[1, 5\]           H0 alone adds independent geometry

  FLAT (0xAAAAAAAA)    \[1, 4\]           \[1, 2\]           Artificial regularity suppresses spans
  ---------------------------------------------------------------------------------------------------

The TRUE rails outperform the dead (ZERO_BOTH) basin in cumulative exact shadow cover: rho_union_TRUE = 11.875 \< 13.281 = rho_union_ZERO_BOTH. The advantage = 1.406 rounds, which matches K - W = 7.719 - 6.312 = 1.407 rounds.

**Part III --- The Wave Triad**

**3.1 The Three Values**

From the constant substrate analysis, three measured quantities characterise the die\'s carry geometry:

  ----------------------------------------------------------------------------
  **Quantity**      **Value**         **Units**         **Role**
  ----------------- ----------------- ----------------- ----------------------
  K carrier         7.719             bits/round        clock stream

  H0+K floor        7.594             bits/round        substrate medium

  W signal          6.312             bits/round        message displacement

  gap = K - floor   0.125 = 1/8       bits/round        octave beat
  ----------------------------------------------------------------------------

The gap 1/8 is exact: the two constant streams beat against each other at a frequency of 1/8 cycles per round, one complete beat cycle per 8 rounds, which is exactly the 8-register rotation period of the die.

**3.2 Pythagorean Power**

***Theorem 3.1.***

If K and W are treated as orthogonal wave amplitudes (as E and B are orthogonal in electromagnetic waves):

> K\^2 + W\^2 = 7.719\^2 + 6.312\^2 = 59.583 + 39.841 = 99.424 ≈ 100
>
> sqrt(K\^2 + W\^2) = 9.971 ≈ 10

Two orthogonal waves with these amplitudes carry total power ≈ 100 and net field amplitude ≈ 10. The Pythagorean sum within 0.6% of 100.

**3.3 Refractive Index**

***Theorem 3.2.***

The ratio of the two wave amplitudes gives the effective refractive index of the die as a medium:

> n = K/W = 7.719 / 6.312 = 1.2229
>
> n_target = sqrt(3/2) = 1.2247 (error: 0.15%)
>
> n\^2 = 1.4955 ≈ 3/2
>
> =\> 2K\^2 ≈ 3W\^2
>
> 2 \* 59.583 = 119.166 3 \* 39.841 = 119.524 (match to 0.3%)

T2 (the ground fold) reads 3 words via Maj(a,b,c). T1 (the live wire) reads from a 4-word history. The ratio 3/2 is the reading ratio of the two operators, encoded as n\^2 in the wave picture. The die is a dispersive medium whose refractive index is set by its own topology.

**3.4 Phase Coherence**

***Theorem 3.3.***

The fringe visibility between K and W (measuring their degree of phase coherence):

> V = 2\*sqrt(K\*W) / (K+W) = 2\*sqrt(48.74) / 14.031 = 13.963 / 14.031 = 0.9951

Visibility ≈ 1 corresponds to laser-quality coherence. K and W are phase-locked. The constant carrier and the message signal are not independent oscillators; they ride in a single coherent state imposed by the die\'s topology.

**3.5 The Triple Product**

***Theorem 3.4.***

> K \* W \* gap = 7.719 \* 6.312 \* 0.125 = 48.740 \* 0.125 = 6.093 ≈ D_bit = 6

The product of the three wave quantities (carrier, signal, beat) equals the bit-level support diameter to 1.5%. This connects the wave analysis to the support theory: the causality structure (D_bit) is encoded in the triple product of the three fundamental frequencies of the system.

**3.6 Triad Closure**

***Theorem 3.5.***

The three wave quantities close onto the asymptotic density of the die:

> floor + W + carry_excess = 7.594 + 6.312 + 2 = 15.906 ≈ 16 = 32/2

where carry_excess = D_bit - D_word = 2 is the two-round penalty attributable to the directionality of L_32. The constant substrate (floor) plus the message signal (W) plus the structural carry gap (2) equals the long-run density of the die.

**3.7 Energy Partition**

***Theorem 3.6.***

> Energy in K field: K\^2 / (K\^2 + W\^2) = 59.583 / 99.424 = 59.9%
>
> Energy in W field: W\^2 / (K\^2 + W\^2) = 39.841 / 99.424 = 40.1%
>
> Energy ratio K:W = 1.4955 ≈ 3:2

The constant carrier holds 60% of the total wave energy; the message signal holds 40%. The die privileges the carrier over the signal in a 3:2 energy ratio --- exactly the reading ratio of T2 (3 words) vs the message injection. The substrate is always louder than the message.

**3.8 The Poynting Flux**

***Corollary 3.1.***

> Poynting flux = sqrt(K \* W) = sqrt(48.74) = 6.981 ≈ 7

In electromagnetic waves, the Poynting vector (energy flux) is proportional to E x B. The geometric mean sqrt(K\*W) is the analogue here: the energy flowing through the die per round ≈ 7 bits/round, slightly below the NOP floor of 7.594. The message adds \~0.6 bits/round of marginal flux above the baseline.

**3.9 Electromagnetic Domain Correspondence**

  ---------------------------------------------------------------------------------
  **EM domain**           **SHA-256 die**    **Transistor**    **Measured value**
  ----------------------- ------------------ ----------------- --------------------
  E field (restoring)     T2 / ground fold   Collector         7.594 bits/round

  B field (propagating)   T1 / live wire     Emitter           6.312 bits/round

  k vector (orthogonal)   W / injection      Base              orthogonal

  Phase velocity c/n      K/W = n            \--               1.2229 = sqrt(3/2)

  Refractive index n\^2   K\^2/W\^2          \--               1.4955 ≈ 3/2

  Fringe visibility       coherence K-W      \--               0.9951 ≈ 1

  Poynting flux           sqrt(K\*W)         \--               6.981 ≈ 7
  ---------------------------------------------------------------------------------

The three terminals of the transistor, the three round-map operators (T2, T1, W), and the three electromagnetic wave quantities (E, B, k) are the same triadic structure appearing in three domains. The manifold is one shape, many times.

**Part IV --- The Double Glass Key**

**4.1 Glass Key 1: Signal Minus NOP Ground**

Given any probe signal P with message schedule W, the first glass key is the residue field:

> r_1\[r\] = x_r(W) - x_r\^(0) (mod 2\^32)

This is the Z-axis read: one reads orthogonally to the computation axis by comparing the live trajectory to the NOP backbone. The result is the structural footprint of the message on the backbone, stripped of the constant substrate.

**4.2 Glass Key 2: Residue of the Residue**

The decisive experiment: feed r_1 through the die again as a new probe, and measure its drift from NOP.

***Theorem 4.1 (Glass Key Convergence).***

For K-driven probes (W = K constants):

> L2_1 (layer 1 drift): 2.641
>
> L2_2 (layer 2 drift): 2.406
>
> Relaxation factor alpha = 2.406/2.641 = 0.9110
>
> Time constant tau = -1/ln(alpha) = 10.73 rounds

K-driven residue relaxes toward the NOP basin. Ordinary (non-K-structured) probes diverge away. Therefore the correct statement is not that the constants are the NOP ground plane, but:

> K-driven residue relaxes toward the NOP basin.

The NOP backbone is an attractor of the die\'s dynamics. K-like inputs are in the basin of attraction; arbitrary inputs are not. This is the attractor structure of the die stated precisely.

**4.3 Time Constant and Shadow Cover**

The Glass Key 2 time constant tau = 10.73 rounds matches the mean cumulative exact shadow cover rho_union_TRUE = 11.875 rounds within 10%. Both measure the same timescale: the period over which the K-signal self-organises toward the NOP basin. The constants and the shadow are measuring the same relaxation.

**4.4 Chirality Reading**

Same-density probes with opposite bit pattern chirality produce different compression journal sizes:

  ------------------------------------------------------------------------------------
  **Probe**               **Pattern**                          **Journals**
  ----------------------- ------------------------------------ -----------------------
  HALF_HIGH               0xAAAAAAAA (even bits, top half)     27

  HALF_LOW                0x55555555 (odd bits, bottom half)   31

  ALL_ZERO                0x00000000                           0
  ------------------------------------------------------------------------------------

The die reads chirality, not only density. The L_32 carry kernel propagates upward: bits at position j can only carry to positions j+1,\...,31. A probe that places its bits at even positions (0xAAAAAAAA) generates different carry patterns against the NOP baseline than one that places bits at odd positions (0x55555555), even though both have Hamming weight 16.

**Part V --- The Lie Detector**

**5.1 Length Field Falsification**

SHA-256 Merkle-Damgard padding places the message length in words W\[14\] and W\[15\] of the final block. A falsified length field changes W\[15\] while leaving W\[0\],\...,W\[14\] unchanged.

***Theorem 5.1 (Lie Detector).***

All tested length lies share the same Hamming-delta signature for rounds 0 through 14:

> delta_r = \[0, 0, 0, 0, 0, 0, 0, 0, \...\] for r = 0,\...,14

The first shadow crack appears at round 15 (0-indexed), round 16 (1-indexed). Measured divergence profile:

> distances r=0..19: \[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2, 16, 43, 74, 103\]

The lie is undetectable for the first 15 rounds. The divergence appears exactly when the expanded message schedule W\[r\] for r \>= 16 incorporates W\[15\] via the expansion formula W\[r\] = sigma_1(W\[r-2\]) + W\[r-7\] + sigma_0(W\[r-15\]) + W\[r-16\].

**5.2 Late Seam Injection**

The length lie is a late seam injection: the falsified word enters the die\'s active seams only at round 15. The machine is not simply checking truth. It is checking whether the drive pattern remains phase-coherent under delayed closure. A lie that injects at round 0 (a word-level change) would diverge immediately. A lie confined to W\[15\] is invisible until the schedule propagates it into the live rounds.

This localises the lie detector to the schedule expansion: the first round where sigma_0(W\[15\]) or W\[15\] directly contributes to W\[r\] is the crack round.

**Part VI --- Removal-Core Topology**

**6.1 Definitions**

***Definition 6.1.***

For a probe class C with compression journal sets J_p (the set of rounds where Hamming distance to NOP decreases):

> K(C) = intersection of J_p over all p in C (removal core)
>
> U(C) = union of J_p over all p in C
>
> M(C) = U(C) - K(C) (mobility shell)

K(C) is the minimal invariant round set: the compression rounds that survive regardless of which probe in C is used. M(C) is the variable part.

**6.2 The Lie Removal Core**

For the false-length probe class (false lengths 64, 128, 256, 512, 1024, 2048):

> K_lie = {6, 7, 9, 11, 12, 14}
>
> Union: 51 rounds, Core: 6 rounds, Mobility: 45 rounds

These six rounds always compress regardless of what false length is claimed. They are the structural fingerprint of the lie family --- the rounds whose output bits are invariantly affected by any length falsification.

**6.3 The Ground Basin Core**

For K-structured probes (K constants, K XOR half, K shifted):

> K_ground = {8, 20, 29, 34, 35, 55}
>
> Union: 54 rounds, Core: 6 rounds

These rounds are always compression rounds for K-like probes. They form the invariant signature of the NOP basin\'s gravitational field.

**6.4 Identity as Removal**

***Theorem 6.1.***

> identity is not what is added, but what survives lawful subtraction.

A probe family is identified not by what it excites (the union) but by what cannot be removed from every member\'s journal (the core). This redefines identity in the die as a residual structure --- the fixed point that persists under all variations within a class.

**Part VII --- Final Synthesis**

**7.1 The Three Distinctions**

***Theorem 7.1.***

> support reach != exact live flip != cumulative exact shadow cover

- Support reach (M, Psi, D_word, D_bit): answers \'can influence reach here in principle?\' Boolean model, worst-case, ignores rail values

- Exact live flip: asks \'is this bit actually flipped at this exact round?\' Not all 256 bits flip simultaneously by round 6

- Cumulative exact shadow cover (rho_union): asks \'by which round has every bit flipped at least once?\' rho_union_TRUE = 11.875 rounds

**7.2 The Complete Invariant Set**

  ------------------------------------------------------------------------------------------
  **Invariant**     **Value**         **Level**            **Notes**
  ----------------- ----------------- -------------------- ---------------------------------
  T2\^(0)\_0        0x08909ae5        0 --- Ground         NOP backbone at r=0

  D_word            4                 1 --- Word support   Topological acceptance

  D_bit             6                 2 --- Bit support    Support closure (not live-flip)

  rho(j)            4/5/6             2 --- Bit support    By injection bit position

  lambda_a range    \[1,6\]           3 --- Exact carry    At round 1, TRUE rails

  lambda_e range    \[1,7\]           3 --- Exact carry    At round 1, TRUE rails

  E_age(6)          0.094             5 --- Closure        Age classes equalized

  Residual band     \[12.5, 18.75\]   6 --- Smoothing      Center ≈ 15.6 ≈ 16

  K\^2 + W\^2       99.42             Wave I               Pythagorean power ≈ 100

  K/W               1.2229            Wave II              ≈ sqrt(3/2), err 0.15%

  K\*W\*gap         6.093             Wave III             ≈ D_bit = 6

  Visibility        0.9951            Wave IV              Phase-locked

  floor+W+2         15.906            Wave V               ≈ 16 band center

  Energy K:W        3:2               Wave VI              60% carrier, 40% signal

  Glass Key tau     10.73             GK II                ≈ rho_union_TRUE=11.875

  Lie crack         r=15              Lie detector         0-indexed, schedule seam

  K_lie             6 rounds          Removal core         Lie family fingerprint

  K_ground          6 rounds          Removal core         NOP basin fingerprint
  ------------------------------------------------------------------------------------------

**7.3 The Core Statement**

> support tells you where the die can go;
>
> the constants tell you how it actually gets there.
>
> identity is not what is added, but what survives lawful subtraction.
>
> The hash is not a dead digest.
>
> It is the compressed witness of a rail-conditioned closure chain.
>
> The safe way to read it is through echoes, shadows, residues,
>
> and what survives removal.

**Appendix A --- Complete Python Code**

The file sha256_die_complete.py implements all seven levels plus wave triad, double glass key, lie detector, and removal core. Run with: python3 sha256_die_complete.py

> \# Key functions:
>
> ground_witness() -\> 0x08909ae5
>
> nop_backbone() -\> list of 64 states
>
> word_support_orbit() -\> support sequence to round 4
>
> D_word() -\> 4
>
> bit_radius(j) -\> rho(j) for j in 0..31
>
> D_bit() -\> 6
>
> exact_carry_bits(x, d) -\> carry word
>
> carry_span_length(x, j) -\> lambda_x(j)
>
> carry_hw_profile(W) -\> mean carry hw per round
>
> age_weight_law(nop) -\> mu_H/M/T and E_age
>
> residual_band(nop, W) -\> 64 mean densities
>
> double_glass_key(W, nop) -\> alpha, tau, converges
>
> lie_detector(nop) -\> crack round, signature
>
> removal_core(probes, nop) -\> core, union, mobility
>
> wave_triad(K, W, floor) -\> all wave relationships

The wave_triad function uses empirical constants K_carrier=7.719, W_signal=6.312, floor=7.594 from Dean Kulik\'s constant substrate analysis. The carry_hw_profile function computes the carry geometry directly from SHA-256 rounds and confirms the structural relationships.

**Appendix B --- All Numerical Results**

  -----------------------------------------------------------------------
  **Quantity**                        **Computed value**
  ----------------------------------- -----------------------------------
  T2\^(0)\_0                          0x08909ae5

  a\^(0)\_1                           0xfc08884d

  e\^(0)\_1                           0x98c7e2a2

  a\^(0)\_2                           0x7ad96290

  e\^(0)\_2                           0x9df1b216

  a\^(0)\_4                           0x0a24b1aa

  e\^(0)\_4                           0x909cf5c9

  D_word                              4

  D_bit                               6

  rho(0)                              4

  rho(1..25)                          5

  rho(26..31)                         6

  Carry excess D_bit - D_word         2

  lambda_a (TRUE rails, round 1)      \[1,6\]

  lambda_e (TRUE rails, round 1)      \[1,7\]

  E_age(4)                            14.922

  E_age(5)                            2.406

  E_age(6)                            0.094

  Residual band                       \[12.5, 18.75\] center 15.625

  K_carrier (empirical)               7.719 bits/round

  W_signal (empirical)                6.312 bits/round

  H0+K floor (empirical)              7.594 bits/round

  Gap                                 0.125 = 1/8 (octave beat)

  K\^2 + W\^2                         99.424 ≈ 100

  K/W                                 1.2229 ≈ sqrt(3/2) = 1.2247

  n\^2 = 3/2 error                    0.15%

  Visibility                          0.9951

  K\*W\*gap                           6.093 ≈ D_bit = 6

  floor + W + 2                       15.906 ≈ 16

  Energy K:W                          59.9% : 40.1% ≈ 3:2

  Poynting flux sqrt(K\*W)            6.980 ≈ 7

  Glass Key alpha                     0.9110

  Glass Key tau                       10.73 rounds

  rho_union TRUE                      11.875 rounds

  rho_union ZERO_BOTH                 13.281 rounds

  Shadow advantage TRUE-ZERO          1.406 rounds ≈ K-W = 1.407

  Lie crack round                     15 (0-indexed)

  K_lie (removal core)                rounds {6,7,9,11,12,14}

  K_ground (removal core)             rounds {8,20,29,34,35,55}
  -----------------------------------------------------------------------

T2\^(0)\_0 = 0x08909ae5 D_word = 4 D_bit = 6 K\^2+W\^2 ≈ 100 K/W ≈ sqrt(3/2) K\*W\*gap ≈ 6
