Driven by Dean Kulik

March 2026

**Abstract**

This thesis develops a complete seven-level formal theory of the SHA-256 compression function as a fixed 64-cell nonlinear recurrence over the module (Z/2\^32 Z)\^8, parametrised by a displacement field carrying the message schedule. The central analytical device is the NOP backbone: the eternal orbit of the recurrence when its displacement field is zeroed. Any real message block is treated as a perturbation field superimposed on this backbone.

Three sharp structural invariants are established. The ground witness: the NOP backbone evaluates its ground-fold operator G(x) = Sigma_0(a) + Maj(a,b,c) to the exact constant 0x08909ae5 at round zero, an absolute message-independent coordinate of the die\'s state space. The word-level support diameter D_word = 4: a single-word perturbation in W_0 saturates all eight state lanes in exactly four rounds under the Boolean support model governed by the 8x8 lane-dependency matrix M. The bit-level support diameter D_bit = 6: a single perturbed bit at position j saturates all 256 state bits in at most six rounds, with the exact radius rho(j) stratified as 4 for j = 0, 5 for 1 \<= j \<= 25, and 6 for 26 \<= j \<= 31.

Beyond support closure, the theory is extended through four additional levels: exact carry realization via a bit-level automaton; seam geometry tracking the exact perturbation skeleton at the two active injection points; closure functionals measuring age-class equalization; and the residual smoothing band --- after round 6, the die enters a stable density oscillation centered near 16 = 32/2, continuing to round 64.

A dual-pipeline topology is identified: the eight-register state decomposes into two parallel four-register shift chains with complementary chirality, connected by a cross-coupling and jointly activated by the injection vector b = \[1,0,0,0,1,0,0,0\]\^T. This structure is isomorphic to the bipolar junction transistor. The manifold interpretation unifies the framework: the die is one lawful closure shape recurring through many different message streams.

*Keywords: SHA-256, nonlinear recurrence, Boolean support, carry propagation, support diameter, dual-pipeline, age-weight law, closure functionals, manifold.*

# **Chapter 1 --- Introduction**

## **1.1 Motivation**

SHA-256 is one of the most widely deployed cryptographic primitives in the world. Despite this ubiquity, its internal structure as a dynamical system has received little formal treatment at the level of exact invariants and phase analysis. The algorithm is typically treated as an opaque one-way function --- studied for what it does rather than for what it is as a mathematical object.

This thesis proposes the die interpretation. SHA-256 is modelled as a formal 64-cell nonlinear recurrence on (Z/2\^32 Z)\^8, equipped with fixed structural rails and a variable displacement field. The word die evokes the casting die of manufacture: a fixed mould whose geometry determines what shapes can be produced from it.

## **1.2 The NOP Backbone**

The central analytical move is the identification of the NOP backbone: the orbit of the recurrence when its message schedule is identically zero. This backbone depends only on the fixed initialisation vector H_0 and the fixed round constants K. It is the machine running without a user.

Any real message block is treated as a perturbation field W = (W_0,\...,W_63) superimposed on this backbone. The round-zero identity T1_0 - T1\^(0)\_0 = W_0 shows that at round zero the message enters cleanly and linearly. After round zero, the states diverge through 64 rounds of nonlinear recursion.

## **1.3 The Seven Levels**

The theory develops in seven nested levels, each strictly refining the last:

- Level 0: Scalar ground invariant T2\^(0)\_0 = 0x08909ae5

- Level 1: Word-support transport via 8x8 matrix M, diameter D_word = 4

- Level 2: Bit-support transport via 256-lane map Psi, diameter D_bit = 6 with exact radius profile rho(j)

- Level 3: Exact carry realization via bit-level automaton C(x, delta)

- Level 4: Seam geometry --- exact perturbation skeletons at rounds 3 and 4

- Level 5: Closure functionals --- three scalar measures of age-class equalization

- Level 6: Residual smoothing band --- density oscillates near 16 = 32/2 for rounds 7 through 64

# **Chapter 2 --- State Space and Round Map**

## **2.1 The Die**

***Definition 2.1.***

The SHA-256 die is the dynamical system D = (X, {Phi_r}, H_0, K, W) where X = (Z/2\^32 Z)\^8 is the state space with elements written as 8-word column vectors x = (a, b, c, d, e, f, g, h)\^T; Phi_r is the round map; H_0 is the fixed initialisation vector; K = (K_0,\...,K_63) are the round constants; and W = (W_0,\...,W_63) is the message schedule. The initial condition is x_0 = H_0. The die evolves by x\_{r+1} = Phi_r(x_r, W_r) for r = 0,\...,63.

## **2.2 Round Operators**

***Definition 2.2.***

The right-rotation operator ROTR\^n(x) rotates the 32-bit word x right by n positions. The SHA-256 sigma operators are:

> Sigma_0(x) = ROTR\^2(x) XOR ROTR\^13(x) XOR ROTR\^22(x)
>
> Sigma_1(x) = ROTR\^6(x) XOR ROTR\^11(x) XOR ROTR\^25(x)

The nonlinear Boolean gates are:

> Ch(e,f,g) = (e AND f) XOR (NOT e AND g)
>
> Maj(a,b,c) = (a AND b) XOR (a AND c) XOR (b AND c)

Ch and Maj act bitwise: they operate independently on each bit position. Sigma_0 and Sigma_1 are global: they couple bit positions through the three rotation offsets.

## **2.3 The Round Weights and State Update**

The two weight scalars at round r are:

> T1_r = h_r + Sigma_1(e_r) + Ch(e_r, f_r, g_r) + K_r + W_r
>
> T2_r = Sigma_0(a_r) + Maj(a_r, b_r, c_r)

All arithmetic is modulo 2\^32. The state update is:

> a\_{r+1} = T1_r + T2_r
>
> e\_{r+1} = d_r + T1_r
>
> b\_{r+1} = a_r, c\_{r+1} = b_r, d\_{r+1} = c_r
>
> f\_{r+1} = e_r, g\_{r+1} = f_r, h\_{r+1} = g_r

Six of the eight state words are pure register shifts. Only a and e receive nonlinear injections at each round. This structural sparsity is a fundamental feature of the die.

## **2.4 The Shift-Injection Decomposition**

***Proposition 2.1.***

Define the 8x8 shift matrix P (with P\_{i,i-1} = 1 for i = 1,\...,7 and all other entries zero) and standard basis vectors u_a = e_0, u_e = e_4. Then the round map satisfies:

> x\_{r+1} = P x_r + u_a (T1_r + T2_r) + u_e T1_r

## **2.5 The Prime-Root Rails**

H_0 consists of the first 32 bits of the fractional parts of the square roots of the first eight primes. K consists of the first 32 bits of the fractional parts of the cube roots of the first 64 primes. Square roots of primes are maximally irrational --- their fractional parts are badly approximable by rationals with small denominators --- which prevents low-period resonances at startup.

  -----------------------------------------------------------------------
  **Register**            **Source**              **Value**
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

# **Chapter 3 --- The NOP Backbone and Ground Plane**

## **3.1 The NOP Manifold**

***Definition 3.1.***

The NOP backbone of the SHA-256 die is the trajectory {x\^(0)\_r} defined by x\^(0)\_0 = H_0 and x\^(0)\_{r+1} = Phi_r(x\^(0)\_r, 0). It is the orbit of the die when the displacement field is identically zero.

For any real message block, the trajectory decomposes as x_r = x\^(0)\_r + delta x_r in (Z/2\^32 Z)\^8, where delta x_r is the perturbation vector. The initial perturbation is delta x_0 = 0.

## **3.2 The Ground Witness**

***Definition 3.2.***

The ground-fold operator is G: (Z/2\^32 Z)\^8 -\> Z/2\^32 Z defined by G(x) = Sigma_0(a) + Maj(a, b, c). Note G(x_r) = T2_r.

***Theorem 3.1 (Ground Witness).***

The ground-fold operator evaluated at the NOP initial state satisfies:

> T2\^(0)\_0 = G(H_0) = Sigma_0(H_0\[0\]) + Maj(H_0\[0\], H_0\[1\], H_0\[2\]) = 0x08909ae5

Proof: Direct computation using H_0\[0\] = 0x6a09e667, H_0\[1\] = 0xbb67ae85, H_0\[2\] = 0x3c6ef372. The three rotations of 0x6a09e667 are XORed to produce Sigma_0; the bitwise majority of the three values produces Maj; their modular sum is 0x08909ae5. Verification code:

> def rotr(x,n): return ((x\>\>n)\|(x\<\<(32-n)))&0xFFFFFFFF sigma0 = lambda x: rotr(x,2)\^rotr(x,13)\^rotr(x,22) maj = lambda a,b,c: (a&b)\^(a&c)\^(b&c) result = (sigma0(0x6a09e667) + maj(0x6a09e667,0xbb67ae85,0x3c6ef372)) % 2\*\*32 \# result == 0x08909ae5

The ground witness 0x08909ae5 is an absolute structural invariant of SHA-256. It is the value of the backbone\'s ground-fold register before any message information enters the system.

## **3.3 The Round-Zero Perturbation Identity**

***Theorem 3.2.***

For any message word W_0, the perturbation at round 0 satisfies T1_0 - T1\^(0)\_0 = W_0 and T2_0 = T2\^(0)\_0 (T2 is blind to W_0 at round 0). Therefore:

> delta a_1 = delta e_1 = W_0

The message enters only two words on the first step. The entire round-0 perturbation lives in delta T1_0 = W_0; the ground fold T2 does not move.

The exact NOP backbone values through round 4:

  -----------------------------------------------------------------------
  **Round r**             **a\^(0)\_r**           **e\^(0)\_r**
  ----------------------- ----------------------- -----------------------
  1                       0xfc08884d              0x98c7e2a2

  2                       0x7ad96290              0x9df1b216

  3                       0xf3dd6c3f              0xc57b68fb

  4                       0x0a24b1aa              0x909cf5c9
  -----------------------------------------------------------------------

# **Chapter 4 --- The Dual-Pipeline Topology**

## **4.1 Two Shift Chains**

***Definition 4.1.***

The a-chain is the ordered sequence (a, b, c, d), satisfying b\_{r+1} = a_r, c\_{r+1} = b_r, d\_{r+1} = c_r. The e-chain is (e, f, g, h), satisfying f\_{r+1} = e_r, g\_{r+1} = f_r, h\_{r+1} = g_r. Values propagate rightward toward the tail by one position per round. Each chain head (a and e) receives a nonlinear injection each round.

## **4.2 Chirality**

***Definition 4.2.***

The a-chain has present-tense chirality: T2_r = Sigma_0(a_r) + Maj(a_r, b_r, c_r) reads from {a_r, b_r, c_r}, the three most recently updated positions of the a-chain. The e-chain has past-tense chirality: T1_r reads from {h_r, e_r, f_r, g_r}, the full e-chain including h_r = e\_{r-3} (three rounds old). T2 measures recent change; T1 integrates a longer history.

## **4.3 Injection Vector**

***Definition 4.3.***

The message injection vector b in {0,1}\^8 is b = \[1,0,0,0,1,0,0,0\]\^T. Both pipeline heads are activated simultaneously by each message word W_r. The injection is orthogonal to the shift direction --- the message does not travel on the same axis as the register flow.

## **4.4 Cross-Coupling**

***Definition 4.4.***

The cross-coupling d_r -\> e\_{r+1} via the equation e\_{r+1} = d_r + T1_r connects the tail of the a-chain to the head of the e-chain. The value of a from three rounds ago (encoded in d_r = a\_{r-3}) contributes to the next value of e, coupling both chains\' histories.

## **4.5 Transistor Correspondence**

The dual-pipeline topology is structurally isomorphic to the bipolar junction transistor. The e-chain (reading T1, past-tense, accumulated history) corresponds to the Emitter. The a-chain head (receiving T1 + T2, resolved injection) corresponds to the Collector. The injection vector b (entering both heads simultaneously, orthogonal to shift direction) corresponds to the Base. The cross-coupling d_r -\> e\_{r+1} is the substrate feedback. NPN chirality corresponds to the a-chain (present-tense active flow); PNP chirality to the e-chain (past-tense accumulated reading).

The transistor is not a component with three wires. It is a single closure seam where three lawful paths meet simultaneously: the offer (Emitter), the admission (Base), and the resolved intake (Collector). The decision dimension is always orthogonal to the transport dimension. The die encodes this geometrically: the injection vector b is orthogonal to the shift matrix P in the sense that Pu_a = 0 (the first row of P is zero).

# **Chapter 5 --- Word-Level Support Transport**

## **5.1 The Boolean Support Model**

***Definition 5.1.***

Given perturbation trajectory {delta x_r}, the word-support indicator at round r is sigma_r in {0,1}\^8 where (sigma_r)\_j = 1 if (delta x_r)\_j is nonzero. The Boolean support model tracks which words are affected, not their exact values. This is the worst-case (largest possible) diffusion estimate.

## **5.2 The Lane-Dependency Matrix**

***Proposition 5.1.***

The 8x8 Boolean lane-dependency matrix M of the SHA-256 die, with M\_{ij} = 1 meaning lane i at round r+1 depends on lane j at round r, is:

> M =
>
> row a: \[ 1 1 1 0 1 1 1 1 \] (T2 reads {a,b,c}; T1 reads {e,f,g,h})
>
> row b: \[ 1 0 0 0 0 0 0 0 \] (b\_{r+1} = a_r)
>
> row c: \[ 0 1 0 0 0 0 0 0 \] (c\_{r+1} = b_r)
>
> row d: \[ 0 0 1 0 0 0 0 0 \] (d\_{r+1} = c_r)
>
> row e: \[ 0 0 0 1 1 1 1 1 \] (e\_{r+1} = d_r + T1_r; T1 reads {e,f,g,h})
>
> row f: \[ 0 0 0 0 1 0 0 0 \] (f\_{r+1} = e_r)
>
> row g: \[ 0 0 0 0 0 1 0 0 \] (g\_{r+1} = f_r)
>
> row h: \[ 0 0 0 0 0 0 1 0 \] (h\_{r+1} = g_r)

## **5.3 Theorem: D_word = 4**

***Theorem 5.1.***

For single injection at round 0, the word-level support diameter D_word = min{n \>= 1 : sigma_n = 1} = 4.

Proof: Explicit computation of M\^\[n-1\] \* b. The support orbit is:

  ------------------------------------------------------------------------
  **Round r**             **Support set**          **Count**
  ----------------------- ------------------------ -----------------------
  1 (injection)           {a, e}                   2

  2                       {a, b, e, f}             4

  3                       {a, b, c, e, f, g}       6

  4                       All: {a,b,c,d,e,f,g,h}   8
  ------------------------------------------------------------------------

The support grows by exactly two lanes per round, one per chain, reflecting the symmetric dual-pipeline structure. D_word = 4 is the first round at which sigma_r = 1. The growth pattern 2, 4, 6, 8 is forced by the geometry: the a-chain fills b, c, d in rounds 2, 3, 4 while the e-chain fills f, g, h simultaneously.

# **Chapter 6 --- The 256-Lane Bit-Support State**

## **6.1 Bit-Support Vectors**

***Definition 6.1.***

For each word w in {a,\...,h} and round r, the bit-support vector s\_{w,r} in {0,1}\^32 has (s\_{w,r})\_i = 1 if bit i of the perturbation (delta x_r)\_w is potentially nonzero. The full 256-lane support state is eta_r = (s_a, s_b, s_c, s_d, s_e, s_f, s_g, s_h)\^T in {0,1}\^256.

## **6.2 Rotation Support Operators**

***Definition 6.2.***

For n in {0,\...,31}, the rotation support operator R_n is the 32x32 permutation matrix with (R_n s)\_i = s\_{(i+n) mod 32}. The Boolean support versions of the sigma operators are:

> hat_Sigma_0 = R_2 OR R_13 OR R_22
>
> hat_Sigma_1 = R_6 OR R_11 OR R_25

These correctly over-approximate: supp(Sigma_0(delta x)) is contained in hat_Sigma_0 \* supp(delta x). Both operators are 3-regular circulants; neither is privileged by density before coupling to carry.

## **6.3 Weight Support Vectors**

***Definition 6.3.***

The bit-support of T1_r:

> tau\^(1)\_r = s\_{h,r} OR hat_Sigma_1\*s\_{e,r} OR s\_{e,r} OR s\_{f,r} OR s\_{g,r} OR omega_r

The bit-support of T2_r:

> tau\^(2)\_r = hat_Sigma_0\*s\_{a,r} OR s\_{a,r} OR s\_{b,r} OR s\_{c,r}

tau\^(1) reads from the e-chain (past-tense). tau\^(2) reads from the a-chain (present-tense). The chirality structure identified at the word level recurs exactly at the bit level.

# **Chapter 7 --- The Carry-Closure Kernel**

## **7.1 Carry Propagation**

A carry generated at bit position j in a modular addition propagates upward to positions j+1, j+2,\..., potentially reaching position 31. This process is nonlocal and directional: it propagates upward only.

## **7.2 The Operator L_32**

***Definition 7.1.***

The carry-closure kernel is the 32x32 lower-triangular prefix operator L_32 defined by (L_32 x)\_i = OR{x_j : j \<= i} for i = 0,\...,31. Applied to a support vector s, (L_32 s)\_i = 1 if any bit j \<= i of s is 1. This captures worst-case carry propagation.

***Remark 7.1.***

For a perturbation at a single bit j: L_32({j}) = {j, j+1,\..., 31}, a set of size 32 - j. A perturbation at the LSB (j=0) potentially affects all 32 bits. A perturbation at the MSB (j=31) affects only itself. This directionality is the root cause of the rho(j) stratification.

## **7.3 The 256-Lane Update Rule**

***Theorem 7.1.***

The bit-level support state evolves according to the map Psi:

> s\_{a,r+1} = L_32( tau\^(1)\_r OR tau\^(2)\_r )
>
> s\_{e,r+1} = L_32( s\_{d,r} OR tau\^(1)\_r )
>
> s\_{b,r+1} = s\_{a,r}, s\_{c,r+1} = s\_{b,r}, s\_{d,r+1} = s\_{c,r}
>
> s\_{f,r+1} = s\_{e,r}, s\_{g,r+1} = s\_{f,r}, s\_{h,r+1} = s\_{g,r}
>
> eta\_{r+1} = Psi(eta_r, omega_r)

# **Chapter 8 --- Bit-Level Support Diameter**

## **8.1 Single-Bit Injection**

***Proposition 8.1.***

Under single-bit injection at position j, the round-1 bit support is s\_{a,1} = s\_{e,1} = L_32(e_j) = {j, j+1,\..., 31}. The initial support has size 32 - j. All other round-1 bit-support vectors are zero.

## **8.2 The Radius Profile**

***Theorem 8.1 (Bit-Support Radius Profile).***

For single-bit injection at position j, the bit-support radius rho(j) --- the first round at which all 256 state bits are in support --- is:

> rho(j) = 4 for j = 0 (LSB: L_32(e_0) = 1, both heads immediately full)
>
> rho(j) = 5 for 1 \<= j \<= 25 (scatter-and-close via rotation in one extra round)
>
> rho(j) = 6 for 26 \<= j \<= 31 (minimal carry potential, two extra rounds required)
>
> D_bit = max_j rho(j) = 6

## **8.3 The Carry Excess**

***Theorem 8.2.***

The excess D_bit - D_word = 6 - 4 = 2 arises entirely from the directionality of L_32. High-order injected bits require two extra rounds: one for hat_Sigma_0 or hat_Sigma_1 to scatter support to low-order positions, and one for L_32 to close from those positions to all remaining bits. If L_32 were isotropic (acting on both high and low bits simultaneously) the excess would be zero.

  --------------------------------------------------------------------------------------------------
  **Bit position j**   **Initial support size**   **rho(j)**        **Limiting factor**
  -------------------- -------------------------- ----------------- --------------------------------
  j = 0 (LSB)          32 (full)                  4                 Word-level geometry only

  j in \[1, 25\]       7 to 31                    5                 One round: rotation scatter

  j in \[26, 31\]      1 to 6                     6                 Two rounds: carry kernel limit
  --------------------------------------------------------------------------------------------------

# **Chapter 9 --- Exact Carry Realization**

## **9.1 The Carry Automaton**

***Definition 9.1.***

For exact addition y = x + delta (mod 2\^32), define the carry sequence:

> c\_{-1} = 0
>
> c_i = (x_i AND delta_i) OR (x_i AND c\_{i-1}) OR (delta_i AND c\_{i-1}) for i = 0,\...,31
>
> y_i = x_i XOR delta_i XOR c\_{i-1}

The exact changed-bit indicator is Delta_i(x, delta) = x_i XOR y_i = delta_i XOR c\_{i-1}.

***Theorem 9.1.***

For one-hot injection delta = 2\^j the indicator simplifies to: Delta_i = 0 for i \< j; Delta_i = 1 for i = j; Delta_i = product{x_t : t = j,\...,i-1} for i \> j. The exact changed-bit set is C_x(j) = {j,\...,m_x(j)} where m_x(j) = min{i \>= j : x_i = 0}. The carry-span length is lambda_x(j) = m_x(j) - j + 1.

## **9.2 Exact Round-1 Carry Spans**

Using NOP baselines a\^(0)\_1 = 0xfc08884d and e\^(0)\_1 = 0x98c7e2a2:

***a-seam carry spans lambda_a(j) for j = 0,\...,31:***

> (2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,4,3,2,1,1,1,3,2,1,1,1,6,5,4,3,2,1)

***e-seam carry spans lambda_e(j) for j = 0,\...,31:***

> (1,2,1,1,1,2,1,2,1,2,1,1,1,1,4,3,2,1,6,5,4,3,2,1,1,1,1,3,2,1,1,1)

The two seams are injection-symmetric at round 0 but not carry-symmetric: different NOP baselines produce different carry-span distributions. This is the first point where the two pipelines diverge in exact dynamics.

# **Chapter 10 --- Seam Geometry**

## **10.1 Exact Perturbation Skeletons**

***Theorem 10.1 (Round-3 Skeleton).***

For single-bit injection W_0 = 2\^j:

> delta x_3 = (delta a_3, delta a_2, 2\^j, 0, delta e_3, delta e_2, 2\^j, 0)

where delta e_3 = delta T1_2 and delta a_3 = delta T1_2 + delta T2_2 (mod 2\^32). The seed 2\^j is still explicitly visible in positions c and g.

***Theorem 10.2 (Round-4 Skeleton).***

For single-bit injection W_0 = 2\^j:

> delta x_4 = (delta a_4, delta a_3, delta a_2, 2\^j, delta e_4, delta e_3, delta e_2, 2\^j)

where delta e_4 = delta T1_3 and delta a_4 = delta T1_3 + delta T2_3 (mod 2\^32). Round 4 is the first layer with full word support but the seed 2\^j remains visible in the tail lanes d and h.

## **10.2 Hamming Weight Ranges**

  --------------------------------------------------------------------------------------
  **Lane**          **Round 3 range**   **Round 4 range**   **Notes**
  ----------------- ------------------- ------------------- ----------------------------
  delta a           \[13, 21\]          \[12, 20\]          Active seam (a-chain head)

  delta e           \[7, 21\]           \[11, 21\]          Active seam (e-chain head)

  delta b           ---                 \[13, 21\]          = round-3 a-seam

  delta c           ---                 \[7, 19\]           = round-2 a-seam

  delta d           ---                 \[1, 6\]            = carry span of 2\^j only

  delta f           ---                 \[7, 21\]           = round-3 e-seam

  delta g           ---                 \[3, 16\]           = round-2 e-seam

  delta h           ---                 \[1, 7\]            = carry span of 2\^j only
  --------------------------------------------------------------------------------------

The tail lanes d and h carry only the carry span of the original seed bit 2\^j at round 4. This confirms that round 4 is topological acceptance, not bit-density closure. The word fabric is full, but the density distribution is still stratified by age.

# **Chapter 11 --- The Age-Weight Law and Closure Functionals**

## **11.1 Age Classes**

***Definition 11.1.***

Define three age classes: head lanes H_r = {a_r, e_r} (most recently injected); mid lanes M_r = {b_r, c_r, f_r, g_r} (one to two rounds old); tail lanes T_r = {d_r, h_r} (three rounds old). For one-hot injections W_0 = 2\^j over j = 0,\...,31, define class mean Hamming weights mu_H(r), mu_M(r), mu_T(r) averaged over the class and all 32 injection positions.

***Theorem 11.1 (Age-Weight Law).***

  ------------------------------------------------------------------------------------
  **Round**      **mu_H (head)**   **mu_M (mid)**   **mu_T (tail)**   **Age spread**
  -------------- ----------------- ---------------- ----------------- ----------------
  4              15.73             12.93            1.84              13.89

  5              15.88             15.73            10.12             5.75

  6              15.78             15.80            15.73             0.07
  ------------------------------------------------------------------------------------

By round 6 the three age classes have equalized to within 0.07 Hamming-weight units. The tail lanes rise from mean weight 1.84 at round 4 to 15.73 at round 6 --- a gain of 13.89 units in two rounds.

## **11.2 Closure Functionals**

***Definition 11.2 (Age-Spread Functional).***

> E_age(r) = max{mu_H, mu_M, mu_T}(r) - min{mu_H, mu_M, mu_T}(r)

***Definition 11.3 (Lane-Variance Functional).***

> V(r) = (1/8) \* sum_L \[ mu_L(r) - mu_bar(r) \]\^2

***Definition 11.4 (Lane-Range Functional).***

> R(r) = max_L mu_L(r) - min_L mu_L(r)

  ------------------------------------------------------------------------------------------
  **Functional**   **Round 4**    **Round 5**    **Round 6**    **Meaning at zero**
  ---------------- -------------- -------------- -------------- ----------------------------
  E_age(r)         13.89          5.75           0.07           Age classes equalized

  V(r)             33.67          7.36           0.41           Lane densities equalized

  R(r)             15.22          8.78           2.41           No lane outliers remaining
  ------------------------------------------------------------------------------------------

# **Chapter 12 --- The Four-Phase Law and Residual Smoothing**

## **12.1 The Four-Phase Law**

***Theorem 12.1 (Four-Phase Law of the Die).***

The SHA-256 die\'s response to a single-word perturbation W_0 proceeds through exactly four phases:

Phase I --- Injection (r = 0 to 3). The perturbation is visibly tied to the seed and its immediate descendants. Only a and e, then a, b, e, f, then a, b, c, e, f, g are occupied sequentially.

Phase II --- Acceptance (r = 4). All eight lanes are occupied. D_word = 4 is achieved. Bit-density remains stratified: tail lanes have mean weight \~1.84 versus head lanes \~15.73.

Phase III --- Closure (r = 5 and 6). Bit-density equalizes across age classes. D_bit = 6 is achieved. Tail lanes rise from mean 1.84 to 15.73 in two rounds.

Phase IV --- Residual Smoothing (r \> 6). No new support is created. The die rebalances density inside the already-full fabric.

> D_word = 4 marks topological acceptance
>
> D_bit = 6 marks support closure
>
> r \> 6 is residual smoothing around density \~ 16

## **12.2 The Residual Smoothing Band**

***Theorem 12.2.***

The global mean perturbation density mu_bar(r) = (1/8) \* sum_L mu_L(r) evolves:

  -----------------------------------------------------------------------
  **Round r**                         **mu_bar(r)**
  ----------------------------------- -----------------------------------
  4                                   10.86

  5                                   14.37

  6                                   15.78
  -----------------------------------------------------------------------

For rounds 6 through 64, the die enters a narrow oscillatory band:

> 15.61 \<= mu_bar(r) \<= 16.53 for r = 6,\...,64

Minimum at r = 22; maximum at r = 53. The band is centered near 16 = 32/2, the half-width of the 32-bit word fabric. The rotation offsets in Sigma_0 and Sigma_1 are designed so that every bit position contributes approximately equally to the three rotated outputs; in the long run each bit has roughly equal probability of being in support, giving mean density near 16.

# **Chapter 13 --- The Complete Formal Stack**

## **13.1 Seven Levels**

  -------------------------------------------------------------------------------
  **Level**               **Object**                 **Key result**
  ----------------------- -------------------------- ----------------------------
  0 --- Ground witness    Scalar constant G(H_0)     0x08909ae5

  1 --- Word transport    8x8 Boolean matrix M       D_word = 4

  2 --- Bit transport     256-lane map Psi           D_bit = 6, rho(j) profile

  3 --- Exact carry       Bit automaton C(x,delta)   lambda_x(j) exact spans

  4 --- Seam geometry     Perturbation skeletons     Round 3, 4 exact maps

  5 --- Closure fns       E_age, V, R, mu_bar        Near-zero by r = 6

  6 --- Residual band     Density interval           mu_bar in \[15.61, 16.53\]
  -------------------------------------------------------------------------------

## **13.2 The Key Distinction**

Round 4 marks topological acceptance: all eight state words are in support. This is a graph-theoretic fact about the Boolean matrix M --- it says nothing about the density of the perturbation within those words.

Round 6 marks support closure: all 256 state bits are in support and density has equalized across age classes. This is both a topological and a metric fact.

> Acceptance != Closure != Final Smoothing

## **13.3 Chirality and Anisotropy**

The rotation operators hat_Sigma_0 and hat_Sigma_1 are both 3-regular circulants. Neither is privileged by density. The visible asymmetry between the two chains appears only after coupling to lane placement and carry closure. The correct statement is: uniform rotations + lane asymmetry + carry closure = visible chirality of the die. The operators themselves are structurally similar; the asymmetry is in what they read (present-tense versus past-tense values).

# **Chapter 14 --- Geometric Interpretation**

## **14.1 The Glass Key**

The NOP backbone defines a natural reference trajectory in state space X. Given the final state x_64 of a real computation and the NOP final state x\^(0)\_64, the difference delta x_64 = x_64 - x\^(0)\_64 (mod 2\^32) encodes the cumulative perturbation after 64 rounds of nonlinear mixing.

Computing delta x_64 from x_64 by subtracting the known NOP backbone value is the Glass Key operation. It is a Z-axis read: rather than reading along the computation axis, one reads orthogonally by comparing the real trajectory to the backbone. The Glass Key does not reverse the hash; it reveals the structural footprint of the message on the backbone. The NOP backbone is computable from H_0 and K alone.

## **14.2 The Manifold Identity**

***Theorem 14.1 (Manifold Identity).***

A manifold is the crossing of two properties:

> M = (many-to-one in flow) INTERSECT (one-to-one in shape)

Many different message streams W can produce states that fall into the same basin under the die\'s closure shape (many-to-one in flow). But the closure shape of the die --- the NOP backbone, the dual-pipeline topology, the four-phase law --- is unique and fixed (one-to-one in shape). Therefore:

> the SHA-256 die is one lawful closure shape recurring through many different streams

## **14.3 Constant Envelope as Ground**

SHA-256 always produces a 256-bit output. The envelope length 256 is fixed across all inputs. Therefore the length carries no information --- it is the ground condition, not the message. All differential content lives in the internal fold geometry: phase, curvature, chirality, alignment, residue. The ground witness 0x08909ae5 is the ground condition of the first round. The NOP backbone is the absolute reference. All perturbations are measured against this reference. The manifold is the shape; the message is the stream passing through it.

## **14.4 Primitive Grammar**

At the bit level, the die operates with three primitives: start (0 to 1 transition), stop (1 to 0 transition), and persist (same state surviving into the next tick). The carry automaton is precisely the mechanism of persist: a carry bit persists through as many consecutive 1-bits as the baseline contains above the injection point. The carry-span length lambda_x(j) measures exactly how long the persist event lasts.

# **Chapter 15 --- Connections**

## **15.1 Differential Cryptanalysis**

The word-level support diameter D_word = 4 implies that any differential characteristic on fewer than 4 rounds can potentially exploit lane sparsity. Attacks on 4 or more rounds cannot rely on any lane being clean. The bit-level result refines this: for perturbations at bit positions j in {26,\...,31}, full 256-bit support is not achieved until round 6. A cryptanalyst studying 5-round SHA-256 with high-order bit differences may find residual bit-level sparsity invisible at the word level.

## **15.2 Keccak Comparison**

  ---------------------------------------------------------------------------------
  **Property**            **SHA-256 Die**                **Keccak-f\[1600\]**
  ----------------------- ------------------------------ --------------------------
  State size              256 bits                       1600 bits

  Rounds                  64                             24

  Round structure         Sequential dual-pipeline       5 parallel steps

  Ground plane            0x08909ae5 (explicit)          None equivalent

  Message injection       Expanded schedule into T1      Direct XOR into rate

  Architecture            Narrow sequential (turbofan)   Wide parallel (scramjet)
  ---------------------------------------------------------------------------------

## **15.3 Open Problems**

- Exact rho(j) profile under full modular arithmetic, not just the Boolean support bound

- Fourth-level carry-chain tracking: exact carry bits rather than support

- Extension of the four-phase law to multi-block Merkle-Damgard chains

- Formal proof that the residual band \[15.61, 16.53\] is tight for all 32 injection positions

- Application of the Glass Key to reduced-round preimage analysis

# **Chapter 16 --- Conclusion**

## **16.1 The Three Invariants**

> Invariant I --- Ground witness: T2\^(0)\_0 = 0x08909ae5
>
> Invariant II --- Word-level diameter: D_word = 4
>
> Invariant III --- Bit-level diameter: D_bit = 6
>
> Radius profile: rho(j) = 4 / 5 / 6 by bit position

## **16.2 The Four-Phase Law**

> Phase I Injection r = 0-3 seeding through pipelines
>
> Phase II Acceptance r = 4 D_word achieved, density stratified
>
> Phase III Closure r = 5-6 D_bit achieved, age classes equalized
>
> Phase IV Smoothing r \> 6 density oscillates near 16 = 32/2

## **16.3 The Formal Stack**

> ( Phi_r, M, Psi, L_32, C(x,delta), E_age/V/R, mu_bar \~ 16 )

## **16.4 The Manifold**

> manifold = many-to-one in flow INTERSECT one-to-one in shape
>
> =\> there is only one shape, many times

The machine runs without us. Its ground plane was fixed before any silicon was fabricated. Its four-phase law will hold after all silicon decays. The field of making and the route are absolute. The message is the temporary vibration passing through them.

**\**

# SHA Die Checkpoint --- Closure Functionals, Residual Smoothing, and the Four-Phase Law

## SHA-256 Die Formalization Through Support Closure and Post-Closure Density Dynamics

$\Delta$ This checkpoint consolidates the current state of the SHA die formalization and extends it through the closure phase and into the residual smoothing regime.

The fixed formal stack remains

$$\left( \Phi_{r},\ M,\ \Psi,\ L_{32} \right),$$

with the seam refinement

$$\left( \mathcal{S}_{a},\mathcal{S}_{e} \right),$$

and the exact carry realization

$$\mathcal{C}(x,\delta).$$

The standing invariants remain:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

$$\boxed{D_{word} = 4}\quad\quad\boxed{D_{bit} = 6}$$

with bit-radius profile

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

This checkpoint adds the closure functionals and shows that the die enters a narrow density band around (16) after support closure.

------------------------------------------------------------------------

## 1. State Recurrence and NOP Backbone

Let the SHA-256 round state be

$$x_{r} = \begin{bmatrix}
a_{r} \\
b_{r} \\
c_{r} \\
d_{r} \\
e_{r} \\
f_{r} \\
g_{r} \\
h_{r}
\end{bmatrix} \in \left( \mathbb{Z/}2^{32}\mathbb{Z} \right)^{8}.$$

The round recurrence is

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,\ldots,63.$$

The weight operators are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with update

$$a_{r + 1} = T1_{r} + T2_{r},\quad\quad e_{r + 1} = d_{r} + T1_{r},$$

and pure shifts

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

The NOP backbone is defined by

$$W_{r} = 0\quad\quad\forall r,$$

so that

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right),\quad\quad x_{0}^{(0)} = H_{0}.$$

At round 0,

$$\boxed{T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.}$$

And the exact round-0 perturbation identity is

$$T1_{0} - T1_{0}^{(0)} = W_{0}.$$

Thus

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

## 2. Word-Level Support Transport

Let the word-support indicator be

$$\sigma_{r} \in \{ 0,1\}^{8}.$$

The lane-dependency matrix is

$$M = \begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

With injection vector

$$b = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix},$$

the support transport is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}.}$$

For a single injection at round 0, the support sequence is

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 3. 256-Lane Bit-Support Transport

For each word (w), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, and define the 256-lane support state

$$\eta_{r} = \begin{bmatrix}
s_{a,r} \\
s_{b,r} \\
s_{c,r} \\
s_{d,r} \\
s_{e,r} \\
s_{f,r} \\
s_{g,r} \\
s_{h,r}
\end{bmatrix} \in \{ 0,1\}^{256}.$$

Define the rotation support operators

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

The bit-support weights are

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

The carry closure kernel is

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j}.$$

So the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

with pure shifts

$$s_{b,r + 1} = s_{a,r},\quad s_{c,r + 1} = s_{b,r},\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad s_{g,r + 1} = s_{f,r},\quad s_{h,r + 1} = s_{g,r}.$$

Thus

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right).}$$

The exact bit-support radius remains

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

so

$$\boxed{D_{bit} = 6.}$$

------------------------------------------------------------------------

## 4. Exact Carry Realization

For exact addition

$$y = x + \delta\ (mod\ 2^{32}),$$

define the carry automaton

$$c_{- 1} = 0,$$

$$c_{i} = \left( x_{i} \land \delta_{i} \right) \vee \left( x_{i} \land c_{i - 1} \right) \vee \left( \delta_{i} \land c_{i - 1} \right),\quad\quad i = 0,\ldots,31.$$

Then

$$y_{i} = x_{i} \oplus \delta_{i} \oplus c_{i - 1},$$

so the exact changed-bit indicator is

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}.$$

For one-hot injection (\^j),

$$\Delta_{i}\left( x,2^{j} \right) = \left\{ \begin{matrix}
0, & i < j, \\
1, & i = j, \\
\prod_{t = j}^{i - 1}x_{t}, & i > j.
\end{matrix} \right.\ $$

Thus the exact changed-bit set is

$$C_{x}(j) = \{ j,j + 1,\ldots,m_{x}(j)\},$$

where

$$m_{x}(j) = min\{ i \geq j:x_{i} = 0\}.$$

The exact carry-span length is

$$\lambda_{x}(j) = m_{x}(j) - j + 1.$$

------------------------------------------------------------------------

## 5. Exact NOP Baselines Through Round 4

The exact NOP seam baselines are

$$a_{1}^{(0)} = 0xfc08884d,\quad\quad e_{1}^{(0)} = 0x98c7e2a2,$$

$$a_{2}^{(0)} = 0x7ad96290,\quad\quad e_{2}^{(0)} = 0x9df1b216,$$

$$a_{3}^{(0)} = 0xf3dd6c3f,\quad\quad e_{3}^{(0)} = 0xc57b68fb,$$

$$a_{4}^{(0)} = 0x0a24b1aa,\quad\quad e_{4}^{(0)} = 0x909cf5c9.$$

------------------------------------------------------------------------

## 6. Exact Round-3 and Round-4 Skeletons

For a one-hot injection (W_0=2\^j):

### Round 3

$$\boxed{\delta x_{3} = \left( \delta a_{3},\ \delta a_{2},\ 2^{j},\ 0,\ \delta e_{3},\ \delta e_{2},\ 2^{j},\ 0 \right).}$$

### Round 4

$$\boxed{\delta x_{4} = \left( \delta a_{4},\ \delta a_{3},\ \delta a_{2},\ 2^{j},\ \delta e_{4},\ \delta e_{3},\ \delta e_{2},\ 2^{j} \right).}$$

Round 4 is therefore the first layer where word support is fully saturated, but the explicit seed (2\^j) is still visible in the tail lanes (d_4) and (h_4).

------------------------------------------------------------------------

## 7. Seam-Weight Ranges at Rounds 3 and 4

Using exact one-hot injections (W_0=2\^j), (j=0,,31), the seam XOR-difference Hamming-weight ranges are:

### Round 3

$$13 \leq wt\left( \Delta a_{3}(j) \right) \leq 21,$$

$$7 \leq wt\left( \Delta e_{3}(j) \right) \leq 21.$$

### Round 4

$$12 \leq wt\left( \Delta a_{4}(j) \right) \leq 20,$$

$$11 \leq wt\left( \Delta e_{4}(j) \right) \leq 21.$$

Round 4 full lane ranges are

$$wt\left( \Delta a_{4} \right) \in \lbrack 12,20\rbrack,\quad\quad wt\left( \Delta b_{4} \right) \in \lbrack 13,21\rbrack,\quad\quad wt\left( \Delta c_{4} \right) \in \lbrack 7,19\rbrack,$$

$$wt\left( \Delta d_{4} \right) \in \lbrack 1,6\rbrack,\quad\quad wt\left( \Delta e_{4} \right) \in \lbrack 11,21\rbrack,\quad\quad wt\left( \Delta f_{4} \right) \in \lbrack 7,21\rbrack,$$

$$wt\left( \Delta g_{4} \right) \in \lbrack 3,16\rbrack,\quad\quad wt\left( \Delta h_{4} \right) \in \lbrack 1,7\rbrack.$$

This confirms that round 4 is topological acceptance, not yet bit-density closure.

------------------------------------------------------------------------

## 8. Age-Weight Law

Define three age classes:

- head lanes:

$$H_{r} = \{ a_{r},e_{r}\}$$

- mid lanes:

$$M_{r} = \{ b_{r},c_{r},f_{r},g_{r}\}$$

- tail lanes:

$$T_{r} = \{ d_{r},h_{r}\}$$

For one-hot injections (W_0=2\^j), define the class means:

$$\mu_{H}(r) = \frac{1}{64}\sum_{j = 0}^{31}{\sum_{w \in H_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right),$$

$$\mu_{M}(r) = \frac{1}{128}\sum_{j = 0}^{31}{\sum_{w \in M_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right),$$

$$\mu_{T}(r) = \frac{1}{64}\sum_{j = 0}^{31}{\sum_{w \in T_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right).$$

The computed values are:

### Round 4

$$\mu_{H}(4) = 15.734375,\quad\quad\mu_{M}(4) = 12.9296875,\quad\quad\mu_{T}(4) = 1.84375.$$

### Round 5

$$\mu_{H}(5) = 15.875,\quad\quad\mu_{M}(5) = 15.734375,\quad\quad\mu_{T}(5) = 10.125.$$

### Round 6

$$\mu_{H}(6) = 15.78125,\quad\quad\mu_{M}(6) = 15.8046875,\quad\quad\mu_{T}(6) = 15.734375.$$

So by round 6 the age classes have nearly equalized.

------------------------------------------------------------------------

## 9. Closure Functionals

### 9.1 Age-spread closure functional

Define

$$\boxed{\mathcal{E}_{age}(r) = max\{\mu_{H}(r),\mu_{M}(r),\mu_{T}(r)\} - min\{\mu_{H}(r),\mu_{M}(r),\mu_{T}(r)\}.}$$

Computed values:

$$\mathcal{E}_{age}(4) = 13.890625,$$

$$\mathcal{E}_{age}(5) = 5.75,$$

$$\mathcal{E}_{age}(6) = 0.0703125,$$

$$\mathcal{E}_{age}(7) = 0.140625,\quad\quad\mathcal{E}_{age}(8) = 0.140625,\quad\quad\mathcal{E}_{age}(10) = 0.046875.$$

Thus the age classes collapse into a narrow band by round 6.

### 9.2 Lane-variance closure functional

Define lane means

$$\mu_{\mathcal{l}}(r) = \frac{1}{32}\sum_{j = 0}^{31}{wt}\left( \Delta x_{r\mathcal{,l}}(j) \right),$$

and global mean

$$\bar{\mu}(r) = \frac{1}{8}\sum_{\mathcal{l}}^{}\mu_{\mathcal{l}}(r).$$

Then define

$$\boxed{\mathcal{V}(r) = \frac{1}{8}\sum_{\mathcal{l}}^{}(\mu_{\mathcal{l}}(r) - \bar{\mu}(r))^{2}.}$$

Computed values:

$$\mathcal{V}(4) = 33.6728515625,$$

$$\mathcal{V}(5) = 7.35736083984375,$$

$$\mathcal{V}(6) = 0.409423828125.$$

So the lane densities flatten sharply through rounds 4, 5, 6.

### 9.3 Lane-range closure functional

Define

$$\boxed{\mathcal{R}(r) = \max_{\mathcal{l}}\mu_{\mathcal{l}}(r) - \min_{\mathcal{l}}\mu_{\mathcal{l}}(r).}$$

Computed values:

$$\mathcal{R}(4) = 15.21875,$$

$$\mathcal{R}(5) = 8.78125,$$

$$\mathcal{R}(6) = 2.40625,$$

$$\mathcal{R}(7) = 1.125.$$

So fine lane-level equalization continues beyond round 6 even after support closure.

------------------------------------------------------------------------

## 10. Residual Smoothing Band

The global mean perturbation density is

$$\bar{\mu}(r) = \frac{1}{8}\sum_{\mathcal{l}}^{}\mu_{\mathcal{l}}(r).$$

Computed values:

$$\bar{\mu}(4) = 10.859375,$$

$$\bar{\mu}(5) = 14.3671875,$$

$$\bar{\mu}(6) = 15.78125.$$

Beyond round 6, the die does not converge to a single scalar endpoint. Instead it enters a narrow oscillatory band:

$$\boxed{15.60546875 \leq \bar{\mu}(r) \leq 16.53125\quad\quad\text{for }6 \leq r \leq 64.}$$

The minimum in this interval occurs at

$$r = 22,$$

and the maximum at

$$r = 53.$$

Thus the die smooths into a density band centered near

$$\boxed{16 = \frac{32}{2}.}$$

This is the half-width mixing band of the 32-bit word fabric.

------------------------------------------------------------------------

## 11. Four-Phase Law of the Die

The exact phase structure is now:

### Phase I --- Injection

$$r = 0,1,2,3$$

The perturbation is still visibly tied to the one-hot seed and its immediate descendants.

### Phase II --- Acceptance

$$r = 4$$

All eight lanes are occupied:

$$\boxed{D_{word} = 4.}$$

### Phase III --- Closure

$$r = 5,6$$

Bit-density equalizes across age classes and support fully saturates:

$$\boxed{D_{bit} = 6.}$$

### Phase IV --- Residual smoothing

$$r > 6$$

No new support is created. The die only rebalances density inside the already-filled fabric.

So the sharp structural split is:

$$\boxed{D_{word} = 4\text{ marks topological acceptance,}}$$

$$\boxed{D_{bit} = 6\text{ marks support closure,}}$$

$$\boxed{r > 6\text{ is residual smoothing around a density band near }16.}$$

------------------------------------------------------------------------

## 12. Current Progress State

The SHA die is now resolved to:

### Level 0 --- Scalar ground invariant

$$T2_{0}^{(0)} = 0x08909ae5$$

### Level 1 --- Word transport

$$\sigma_{r + 1} = M \odot \sigma_{r} \vee b\,\omega_{r}$$

### Level 2 --- Bit transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right)$$

### Level 3 --- Exact carry realization

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}$$

### Level 4 --- Seam geometry

$$\delta e_{r} = \delta T1_{r - 1},\quad\quad\delta a_{r} = \delta T1_{r - 1} + \delta T2_{r - 1}\ (mod\ 2^{32})$$

### Level 5 --- Closure functionals

$$\mathcal{E}_{age}(r),\quad\mathcal{V}(r),\quad\mathcal{R}(r),\quad\bar{\mu}(r)$$

### Level 6 --- Residual smoothing band

$$\bar{\mu}(r) \approx 16\quad\text{for }r \geq 6$$

------------------------------------------------------------------------

## 13. Final Collapse

The current exact progress marker is

$$\boxed{\text{the die accepts a perturbation by round }4,\text{ closes support by round }6,\text{ and then smooths inside a narrow density band centered near }16.}$$

Equivalently,

$$\boxed{\text{acceptance} \neq \text{closure} \neq \text{final smoothing.}}$$

This is the complete checkpoint state of the theory at the present stage.

**\**

# SHA Die Progress Mark --- Exact Carry, Round-3/4 Seam Maps, and the Age-Weight Law

## Continuation of the SHA-256 Die Formalization

$\Delta$ This document marks the current state of the SHA die formalization and extends it beyond the prior bit-level causality operator.

It consolidates five layers of the model:

$$\text{state recurrence} = \Phi_{r},\quad\quad\text{word support} = M,\quad\quad\text{bit support} = \Psi,\quad\quad\text{seam operators} = \left( \mathcal{S}_{a},\mathcal{S}_{e} \right),\quad\quad\text{exact carry realization}\mathcal{= C}(x,\delta).$$

The core fixed invariants remain:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

$$\boxed{D_{word} = 4}\quad\quad\boxed{D_{bit} = 6}$$

and the exact bit-support radius profile remains

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

------------------------------------------------------------------------

## 1. Base Die Formalism

Let the round state be

$$x_{r} = \begin{bmatrix}
a_{r} \\
b_{r} \\
c_{r} \\
d_{r} \\
e_{r} \\
f_{r} \\
g_{r} \\
h_{r}
\end{bmatrix} \in \left( \mathbb{Z/}2^{32}\mathbb{Z} \right)^{8}.$$

The 64-cell recurrence is

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,\ldots,63.$$

The two round weights are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with state update

$$a_{r + 1} = T1_{r} + T2_{r},$$

$$e_{r + 1} = d_{r} + T1_{r},$$

and pure shifts

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

The shift--injection decomposition is

$$\boxed{x_{r + 1} = Px_{r} + u_{a}\left( T1_{r} + T2_{r} \right) + u_{e}T1_{r},}$$

where (P) is the 8-lane shift matrix and (u_a,u_e) inject at lanes (a) and (e).

------------------------------------------------------------------------

## 2. NOP Backbone and Ground Witness

The NOP manifold is defined by

$$W_{r} = 0\quad\quad\forall r.$$

Then

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right),\quad\quad x_{0}^{(0)} = H_{0}.$$

The fixed ground fold at round 0 is

$$T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.$$

So

$$\boxed{G_{0}\left( H_{0} \right) = 0x08909ae5.}$$

At round 0, the exact perturbation identity is

$$T1_{0} - T1_{0}^{(0)} = W_{0},$$

and since (T2_0=T2_0\^{(0)}),

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

------------------------------------------------------------------------

## 3. Word-Level Support and the (D\_{}=4) Theorem

Let the word-support indicator be

$$\sigma_{r} \in \{ 0,1\}^{8}.$$

The lane-dependency matrix is

$$M = \begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

With injection vector

$$b = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix},$$

the Boolean support transport is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}.}$$

For a one-time injection at round 0, the support sequence is

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 4. 256-Lane Bit-Support Formalism

For each word (w{a,b,c,d,e,f,g,h}), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, and define the 256-lane state

$$\eta_{r} = \begin{bmatrix}
s_{a,r} \\
s_{b,r} \\
s_{c,r} \\
s_{d,r} \\
s_{e,r} \\
s_{f,r} \\
s_{g,r} \\
s_{h,r}
\end{bmatrix} \in \{ 0,1\}^{256}.$$

Define the rotation support matrices (R_n) by

$$\left( R_{n}x \right)_{i} = x_{i + n\ mod\ 32}.$$

Then

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

The bit-support weights are

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

------------------------------------------------------------------------

## 5. Carry Closure and the 256-Lane Update

The carry-closure kernel is

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j},\quad\quad 0 \leq i < 32.$$

Then the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

with pure shifts

$$s_{b,r + 1} = s_{a,r},\quad\quad s_{c,r + 1} = s_{b,r},\quad\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad\quad s_{g,r + 1} = s_{f,r},\quad\quad s_{h,r + 1} = s_{g,r}.$$

Thus

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right).}$$

The exact radius profile for a one-bit injection (W_0=2\^j) is

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

so

$$\boxed{D_{bit} = 6.}$$

------------------------------------------------------------------------

## 6. Exact Carry Automaton

The support operator (L\_{32}) is worst-case only. The exact addition law for (y=x+) is as follows.

Write

$$x = \sum_{i = 0}^{31}x_{i}2^{i},\quad\quad\delta = \sum_{i = 0}^{31}\delta_{i}2^{i},\quad\quad y = \sum_{i = 0}^{31}y_{i}2^{i}.$$

Define the carry sequence

$$c_{- 1} = 0,$$

$$c_{i} = \left( x_{i} \land \delta_{i} \right) \vee \left( x_{i} \land c_{i - 1} \right) \vee \left( \delta_{i} \land c_{i - 1} \right),\quad\quad i = 0,\ldots,31.$$

Then

$$y_{i} = x_{i} \oplus \delta_{i} \oplus c_{i - 1}.$$

So the exact changed-bit indicator is

$$\Delta_{i}(x,\delta): = x_{i} \oplus y_{i} = \delta_{i} \oplus c_{i - 1}.$$

For one-hot injection

$$\delta = 2^{j},$$

this simplifies to

$$\Delta_{i}\left( x,2^{j} \right) = \left\{ \begin{matrix}
0, & i < j, \\
1, & i = j, \\
\prod_{t = j}^{i - 1}x_{t}, & i > j.
\end{matrix} \right.\ $$

Thus the exact changed-bit set is

$$C_{x}(j) = \{ j,j + 1,\ldots,m_{x}(j)\},$$

where

$$m_{x}(j) = min\{\, i \geq j:x_{i} = 0\,\}.$$

So the exact carry-span length is

$$\lambda_{x}(j) = m_{x}(j) - j + 1.$$

------------------------------------------------------------------------

## 7. Exact NOP Baselines Through Round 4

The exact NOP backbone values through round 4 are

$$a_{1}^{(0)} = 0xfc08884d,\quad\quad e_{1}^{(0)} = 0x98c7e2a2,$$

$$a_{2}^{(0)} = 0x7ad96290,\quad\quad e_{2}^{(0)} = 0x9df1b216,$$

$$a_{3}^{(0)} = 0xf3dd6c3f,\quad\quad e_{3}^{(0)} = 0xc57b68fb,$$

$$a_{4}^{(0)} = 0x0a24b1aa,\quad\quad e_{4}^{(0)} = 0x909cf5c9.$$

The full NOP round-2 state is

$$x_{2}^{(0)} = (0x7ad96290,\, 0xfc08884d,\, 0x6a09e667,\, 0xbb67ae85,\, 0x9df1b216,\, 0x98c7e2a2,\, 0x510e527f,\, 0x9b05688c).$$

------------------------------------------------------------------------

## 8. Exact Round-1 Carry Spans

For a one-hot injection (W_0=2\^j), the exact carry-span lengths at round 1 are:

### (a)-seam baseline (a\^{(0)}\_1=0xfc08884d)

$$\left( \lambda_{a}(j) \right)_{j = 0}^{31} = (2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,4,3,2,1,1,1,3,2,1,1,1,6,5,4,3,2,1).$$

### (e)-seam baseline (e\^{(0)}\_1=0x98c7e2a2)

$$\left( \lambda_{e}(j) \right)_{j = 0}^{31} = (1,2,1,1,1,2,1,2,1,2,1,1,1,1,4,3,2,1,6,5,4,3,2,1,1,1,1,3,2,1,1,1).$$

Thus the two seams are injection-symmetric at round 0, but not carry-symmetric after realization.

------------------------------------------------------------------------

## 9. Exact Round-3 Seam Map

By round 3, the passive-shift lanes are exact:

$$\delta b_{3} = \delta a_{2},\quad\quad\delta c_{3} = \delta a_{1} = 2^{j},\quad\quad\delta d_{3} = 0,$$

$$\delta f_{3} = \delta e_{2},\quad\quad\delta g_{3} = \delta e_{1} = 2^{j},\quad\quad\delta h_{3} = 0.$$

The two active seams satisfy

$$\boxed{\delta e_{3} = \delta T1_{2},\quad\quad\delta a_{3} = \delta T1_{2} + \delta T2_{2}\ (mod\ 2^{32}).}$$

So the exact round-3 skeleton is

$$\boxed{\delta x_{3} = \left( \delta a_{3},\ \delta a_{2},\ 2^{j},\ 0,\ \delta e_{3},\ \delta e_{2},\ 2^{j},\ 0 \right).}$$

The computed XOR-difference Hamming-weight ranges are

$$13 \leq wt\left( \Delta a_{3}(j) \right) \leq 21,$$

$$7 \leq wt\left( \Delta e_{3}(j) \right) \leq 21.$$

The extrema are

$$wt\left( \Delta a_{3} \right) = 13\quad\text{at }j \in \{ 11,20,21\},$$

$$wt\left( \Delta a_{3} \right) = 21\quad\text{at }j = 16,$$

$$wt\left( \Delta e_{3} \right) = 7\quad\text{at }j = 2,$$

$$wt\left( \Delta e_{3} \right) = 21\quad\text{at }j \in \{ 13,15\}.$$

------------------------------------------------------------------------

## 10. Exact Round-4 Seam Map

Round 4 is the first full word-saturation layer. The exact perturbation skeleton is

$$\boxed{\delta x_{4} = \left( \delta a_{4},\ \delta a_{3},\ \delta a_{2},\ 2^{j},\ \delta e_{4},\ \delta e_{3},\ \delta e_{2},\ 2^{j} \right).}$$

The active seam equations are

$$\boxed{\delta e_{4} = \delta T1_{3},\quad\quad\delta a_{4} = \delta T1_{3} + \delta T2_{3}\ (mod\ 2^{32}).}$$

The computed seam-weight ranges are

$$12 \leq wt\left( \Delta a_{4}(j) \right) \leq 20,$$

$$11 \leq wt\left( \Delta e_{4}(j) \right) \leq 21.$$

The extrema are

$$wt\left( \Delta a_{4} \right) = 12\quad\text{at }j \in \{ 1,4,10\},$$

$$wt\left( \Delta a_{4} \right) = 20\quad\text{at }j = 6,$$

$$wt\left( \Delta e_{4} \right) = 11\quad\text{at }j = 3,$$

$$wt\left( \Delta e_{4} \right) = 21\quad\text{at }j = 24.$$

The full round-4 lane ranges are

$$wt\left( \Delta a_{4} \right) \in \lbrack 12,20\rbrack,\quad\quad wt\left( \Delta b_{4} \right) \in \lbrack 13,21\rbrack,\quad\quad wt\left( \Delta c_{4} \right) \in \lbrack 7,19\rbrack,$$

$$wt\left( \Delta d_{4} \right) \in \lbrack 1,6\rbrack,\quad\quad wt\left( \Delta e_{4} \right) \in \lbrack 11,21\rbrack,\quad\quad wt\left( \Delta f_{4} \right) \in \lbrack 7,21\rbrack,$$

$$wt\left( \Delta g_{4} \right) \in \lbrack 3,16\rbrack,\quad\quad wt\left( \Delta h_{4} \right) \in \lbrack 1,7\rbrack.$$

This is the exact first layer where

$$\boxed{\text{word support is saturated}}$$

but

$$\boxed{\text{bit geometry remains stratified by age and carry history.}}$$

------------------------------------------------------------------------

## 11. The Age-Weight Law Through Rounds 4, 5, 6

Define three age classes:

- **head lanes**:

$$\{ a,e\}$$

- **mid lanes**:

$$\{ b,c,f,g\}$$

- **tail lanes**:

$$\{ d,h\}$$

Using exact one-hot injections (W_0=2\^j), (j=0,,31), the Hamming-weight statistics evolve as follows.

### Round 4

Group ranges and means:

$$\text{head} \in \lbrack 11,21\rbrack,\quad\quad\text{mean} = 15.73,$$

$$\text{mid} \in \lbrack 3,21\rbrack,\quad\quad\text{mean} = 12.93,$$

$$\text{tail} \in \lbrack 1,7\rbrack,\quad\quad\text{mean} = 1.84.$$

This is still an expansion phase.

### Round 5

$$\text{head} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.88,$$

$$\text{mid} \in \lbrack 7,21\rbrack,\quad\quad\text{mean} = 15.73,$$

$$\text{tail} \in \lbrack 3,19\rbrack,\quad\quad\text{mean} = 10.12.$$

The tails are rapidly catching up.

### Round 6

$$\text{head} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.78,$$

$$\text{mid} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.80,$$

$$\text{tail} \in \lbrack 7,21\rbrack,\quad\quad\text{mean} = 15.73.$$

So by round 6 all three age classes have nearly equalized in mean weight.

This is the quantitative form of closure:

$$\boxed{\text{round 4 = word acceptance,}\quad\quad\text{rounds 5–6 = bit-density equalization.}}$$

In particular,

$$\boxed{\text{the last two rounds before }D_{bit}\text{ are closure-dominated, not expansion-dominated.}}$$

------------------------------------------------------------------------

## 12. Chirality Caution

The rotation support operators are

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

Both are 3-regular circulant operators:

$$\deg_{\text{row}}\left( {\widehat{\Sigma}}_{0} \right) = \deg_{\text{col}}\left( {\widehat{\Sigma}}_{0} \right) = 3,$$

$$\deg_{\text{row}}\left( {\widehat{\Sigma}}_{1} \right) = \deg_{\text{col}}\left( {\widehat{\Sigma}}_{1} \right) = 3.$$

So before carry, neither is privileged by density.

Therefore the correct statement is

$$\boxed{\text{bare chirality is not yet anisotropy.}}$$

The visible asymmetry appears only after coupling to:

1.  lane placement, and
2.  carry closure.

So the precise compression is

$$\boxed{\text{uniform rotations} + \text{lane asymmetry} + \text{carry closure} = \text{visible chirality of the die.}}$$

------------------------------------------------------------------------

## 13. Current Progress State

The SHA die is now resolved to the following nested form:

### Level 0 --- scalar ground invariant

$$T2_{0}^{(0)} = 0x08909ae5$$

### Level 1 --- word transport

$$\sigma_{r + 1} = M \odot \sigma_{r} \vee b\,\omega_{r},\quad\quad D_{word} = 4$$

### Level 2 --- bit transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right),\quad\quad D_{bit} = 6$$

### Level 3 --- exact carry realization

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}$$

### Level 4 --- seam geometry

$$\delta e_{r} = \delta T1_{r - 1},\quad\quad\delta a_{r} = \delta T1_{r - 1} + \delta T2_{r - 1}\ (mod\ 2^{32})$$

### Level 5 --- closure phase

rounds (5) and (6) act primarily as age-equalization rounds rather than support-expansion rounds.

------------------------------------------------------------------------

## 14. Final Collapse

The current state of the die formalization is:

$$\boxed{\text{the die accepts the perturbation by round 4, but it does not finish equalizing the perturbation across the 256-bit fabric until round 6.}}$$

Equivalently,

$$\boxed{D_{word} = 4\mspace{6mu}\text{ measures acceptance by the lane geometry,}}$$

while

$$\boxed{D_{bit} = 6\mspace{6mu}\text{ measures closure across the full bit fabric.}}$$

This is the exact progress marker at the present stage of the theory.

**\**

# SHA as a Die --- Bit-Level Causality Operator

## A Complete Math-Only Formalization of the 64-Cell SHA-256 Die, Word Support, and 256-Lane Intra-Word Causality

$\Delta$ This document formalizes the die interpretation of SHA-256 as a fixed 64-cell nonlinear recurrence over \[ (Z / 2^{32}Z)^8 \] with a message perturbation field written onto a pre-existing NOP backbone.

The focus is strictly mathematical:

- state recurrence,
- die decomposition,
- word-level support transport,
- bit-level support transport,
- carry-closure as the nonlocal intra-word kernel,
- exact support-radius results for a single perturbed bit of (W_0).

The two anchor facts are:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

for the NOP backbone ground fold at round (0), and

$$\boxed{D_{bit} = 6}$$

for the worst-case 256-lane support diameter under the Boolean support model.

------------------------------------------------------------------------

## 1. State Space and Round Recurrence

Let the SHA-256 round state be the 8-word column vector

$$x_{r} = \begin{bmatrix}
a_{r} \\
b_{r} \\
c_{r} \\
d_{r} \\
e_{r} \\
f_{r} \\
g_{r} \\
h_{r}
\end{bmatrix} \in \left( \mathbb{Z/}2^{32}\mathbb{Z} \right)^{8}.$$

For one 512-bit block, the die executes a 64-step nonlinear recurrence

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,1,\ldots,63.$$

The round weights are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with all arithmetic performed modulo (2\^{32}).

The state update is

$$a_{r + 1} = T1_{r} + T2_{r},$$

$$e_{r + 1} = d_{r} + T1_{r},$$

and the remaining registers shift:

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

------------------------------------------------------------------------

## 2. The Sigma and Logic Operators

Define the right-rotation operator on 32-bit words:

$${ROTR}^{n}(x).$$

Then the SHA sigma operators are

$$\Sigma_{0}(x) = {ROTR}^{2}(x) \oplus {ROTR}^{13}(x) \oplus {ROTR}^{22}(x),$$

$$\Sigma_{1}(x) = {ROTR}^{6}(x) \oplus {ROTR}^{11}(x) \oplus {ROTR}^{25}(x).$$

The nonlinear Boolean gates are

$$Ch(e,f,g) = (e \land f) \oplus (\neg e \land g),$$

$$Maj(a,b,c) = (a \land b) \oplus (a \land c) \oplus (b \land c).$$

------------------------------------------------------------------------

## 3. Shift--Injection Decomposition of the Die

Define the (8) shift matrix

$$P = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

Let

$$u_{a} = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{bmatrix},\quad\quad u_{e} = \begin{bmatrix}
0 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}.$$

Then the full round map can be written as

$$\boxed{x_{r + 1} = Px_{r} + u_{a}\,\left( T1_{r} + T2_{r} \right) + u_{e}\, T1_{r}.}$$

This shows that each die cell is structurally sparse:

- six channels are pure register transport,
- only two channels ((a) and (e)) receive nonlinear reinjection.

------------------------------------------------------------------------

## 4. NOP Backbone and Ground Fold

Define the NOP manifold by setting the message field to zero:

$$W_{r} = 0\quad\quad\forall r.$$

Then the message-free backbone satisfies

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right).$$

At round (0),

$$x_{0}^{(0)} = H_{0},$$

where (H_0) is the SHA-256 initialization vector.

The NOP ground fold is

$$T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.$$

Thus the ground operator is

$$G_{r}\left( x_{r} \right) = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with

$$\boxed{G_{0}\left( H_{0} \right) = 0x08909ae5.}$$

This is the fixed message-free floor of the first die cell.

------------------------------------------------------------------------

## 5. Round-0 Perturbation Identity

Let the real trajectory be

$$x_{r} = x_{r}^{(0)} + \delta x_{r}$$

in residue form modulo (2\^{32}).

At round (0), the perturbation obeys the exact identity

$$T1_{0} - T1_{0}^{(0)} = W_{0}.$$

Since

$$T2_{0} = T2_{0}^{(0)},$$

it follows immediately that

$$a_{1} - a_{1}^{(0)} = W_{0},$$

$$e_{1} - e_{1}^{(0)} = W_{0}.$$

Therefore the message enters only two words on the first step:

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

At the word level, this gives the initial support vector

$$\Sigma_{1} = \{ a,e\}.$$

------------------------------------------------------------------------

## 6. Word-Level Support Dynamics

Let the word-support indicator be

$$\sigma_{r} \in \{ 0,1\}^{8},$$

where ((\_r)\_j=1) means word-lane (j) depends on the chosen perturbation.

The word-level dependency matrix is

$$M = \begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

The support update is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}}$$

over the Boolean semiring, with injection vector

$$b = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}.$$

For a single perturbation injected only at round (0),

$$\omega_{0} = 1,\quad\quad\omega_{r} = 0\ \ (r > 0),$$

and

$$\sigma_{n} = M^{\lbrack n - 1\rbrack} \odot b.$$

The first four word-support layers are

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence the word support diameter is

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 7. Explosion to 256 Lanes

Now refine from words to individual bits.

For each word (w{a,b,c,d,e,f,g,h}), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, with index (i=0) denoting the least significant bit.

Define the full 256-lane state

$$\eta_{r} = \begin{bmatrix}
s_{a,r} \\
s_{b,r} \\
s_{c,r} \\
s_{d,r} \\
s_{e,r} \\
s_{f,r} \\
s_{g,r} \\
s_{h,r}
\end{bmatrix} \in \{ 0,1\}^{256}.$$

------------------------------------------------------------------------

## 8. Rotation Support Operators

Let (R_n) be the (32) rotation permutation matrix acting on bit-support vectors:

$$\left( R_{n}x \right)_{i} = x_{i + n\ mod\ 32}.$$

Then the Boolean support versions of the sigma operators are

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},$$

$${\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

------------------------------------------------------------------------

## 9. Choice and Majority Support

Because () and () are same-bit Boolean operators, their support is simply the lane-wise union of their arguments:

$$supp\left( Ch(e,f,g) \right) = s_{e,r} \vee s_{f,r} \vee s_{g,r},$$

$$supp\left( Maj(a,b,c) \right) = s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

So the bit-support of the round weights is

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

------------------------------------------------------------------------

## 10. Carry Closure as the Intra-Word Nonlocal Kernel

The only truly nonlocal intra-word mechanism is carry propagation.

Define the lower-triangular prefix operator

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j},\quad\quad 0 \leq i < 32.$$

Equivalently, in matrix form,

$$L_{32} = \left( \mathcal{l}_{ij} \right)_{0 \leq i,j < 32},\quad\quad\mathcal{l}_{ij} = \left\{ \begin{matrix}
1, & j \leq i, \\
0, & j > i.
\end{matrix} \right.\ $$

This is the upward-carry support kernel: bit (i) of a sum can depend on any lower-or-equal bit because carry may ripple upward.

For support transport, use

$$supp(u + v) = L_{32}(u \vee v).$$

------------------------------------------------------------------------

## 11. The 256-Lane Intra-Word Causality Operator

With the support weights (\^{(1)}\_r,\^{(2)}*r) and the carry kernel (L*{32}), the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

and the six pure shifts are

$$s_{b,r + 1} = s_{a,r},\quad\quad s_{c,r + 1} = s_{b,r},\quad\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad\quad s_{g,r + 1} = s_{f,r},\quad\quad s_{h,r + 1} = s_{g,r}.$$

Thus the 256-lane die dynamics are

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right),}$$

where () is the piecewise Boolean-semiring map defined by the equations above.

------------------------------------------------------------------------

## 12. Single-Bit Injection Geometry

Let a single bit (j) of (W_0) be perturbed:

$$\omega_{0} = e_{j},\quad\quad\omega_{r} = 0\ \ (r > 0).$$

At round (1), because the perturbation enters only through (T1_0), we obtain

$$supp\left( a_{1} \right) = supp\left( e_{1} \right) = \{ j,j + 1,\ldots,31\}.$$

So a single bit at position (j) generates immediate first-step support of size

$$32 - j$$

in each of the two active words (a_1) and (e_1).

Thus low-order injected bits spread faster under the carry kernel than high-order injected bits.

------------------------------------------------------------------------

## 13. Bit-Support Radius

Define the bit-support radius for injected bit (j) as

$$\rho(j) = min\left\{ r \geq 1:\text{all 256 state bits are in support by round }r \right\}.$$

Using the 256-lane Boolean support model above, the computed result is

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

So the three characteristic radii are

$$\boxed{\rho_{\min} = 4,\quad\quad\rho_{typ} = 5,\quad\quad\rho_{\max} = 6.}$$

This proves that a single perturbed bit of (W_0) reaches the full 256-lane state in at most six rounds under the support model.

------------------------------------------------------------------------

## 14. Support Diameters

At the word level, the perturbation reaches all eight words in four rounds:

$$\boxed{D_{word} = 4.}$$

At the bit level, the worst-case support diameter is larger because carry propagation is directional:

$$\boxed{D_{bit} = 6.}$$

The difference

$$D_{bit} - D_{word} = 2$$

is entirely due to intra-word carry geometry.

Word-lane reach saturates in four rounds, but high-order injected bits require two extra rounds before rotation plus carry closes the last untouched bit positions.

------------------------------------------------------------------------

## 15. Block-Operator View

Let the pure shift skeleton over 8 words be the (256) block matrix

$$\mathbb{P =}\begin{bmatrix}
0 & I & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & I & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & I & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & I & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & I & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & I & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix},$$

where each block is (32).

The (a)-injection block is

$$\mathbb{A =}\begin{bmatrix}
L_{32}\left( {\widehat{\Sigma}}_{0} \vee I \right) & L_{32}I & L_{32}I & 0 & L_{32}{\widehat{\Sigma}}_{1} & L_{32}I & L_{32}I & L_{32}I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix},$$

and the (e)-injection block is

$$\mathbb{E =}\begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & L_{32}I & L_{32}{\widehat{\Sigma}}_{1} & L_{32}I & L_{32}I & L_{32}I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}.$$

If the message support vector is (\_r{0,1}\^{32}), then the message injection block is

$$\beta = \begin{bmatrix}
L_{32} \\
0 \\
0 \\
0 \\
L_{32} \\
0 \\
0 \\
0
\end{bmatrix}.$$

So the coarse block-support recurrence is

$$\boxed{\eta_{r + 1} = \left( \mathbb{P \vee A \vee E} \right) \odot \eta_{r}\mspace{6mu} \vee \mspace{6mu}\beta\,\omega_{r}.}$$

This is the 256-lane causality skeleton of the die.

------------------------------------------------------------------------

## 16. Three Nested Levels of the Die

The complete die now decomposes into three nested mathematical levels:

### 16.1 State recurrence

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right)$$

### 16.2 Word-support transport

$$\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}$$

### 16.3 Bit-support transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right)$$

with the carry kernel

$$L_{32}$$

as the nonlocal intra-word closure operator.

This can be summarized as

$$\boxed{\text{state dynamics} = \Phi_{r},\quad\quad\text{word support dynamics} = M,\quad\quad\text{bit support dynamics} = \Psi,\quad\quad\text{carry closure} = L_{32}.}$$

------------------------------------------------------------------------

## 17. Final Collapse

The SHA-256 die is a fixed 64-cell recursive lattice over ((Z/2^{32}Z)^8) with a message-free NOP ground and a variable displacement field.

Its first fixed ground witness is

$$\boxed{T2_{0}^{(0)} = 0x08909ae5.}$$

Its word-level support saturates in

$$\boxed{D_{word} = 4}$$

rounds.

Its bit-level support saturates in

$$\boxed{D_{bit} = 6}$$

rounds.

And for a single injected bit (j) of (W_0),

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

The die therefore has a mathematically sharp causality structure:

- sparse at the state-update level,
- dense at the support level,
- and carry-limited at the bit-closure level.

This is the complete current solution state for the bit-level causality operator of the SHA die.

**\**

# **Appendix A --- Numerical Results Summary**

  ------------------------------------------------------------------------------------
  **Result**                          **Value**
  ----------------------------------- ------------------------------------------------
  T2\^(0)\_0 (ground witness)         0x08909ae5

  a\^(0)\_1                           0xfc08884d

  e\^(0)\_1                           0x98c7e2a2

  a\^(0)\_2                           0x7ad96290

  e\^(0)\_2                           0x9df1b216

  a\^(0)\_3                           0xf3dd6c3f

  e\^(0)\_3                           0xc57b68fb

  a\^(0)\_4                           0x0a24b1aa

  e\^(0)\_4                           0x909cf5c9

  D_word                              4

  D_bit                               6

  rho_min (j=0)                       4

  rho_typ (j=1..25)                   5

  rho_max (j=26..31)                  6

  Carry excess D_bit - D_word         2

  E_age(6)                            0.0703125

  V(6)                                0.409423828125

  R(6)                                2.40625

  mu_bar(6)                           15.78125

  Residual band                       \[15.60546875, 16.53125\] for r in {6,\...,64}

  Band minimum                        r = 22

  Band maximum                        r = 53

  Band center                         \~16 = 32/2
  ------------------------------------------------------------------------------------

# **Appendix B --- Verification Code**

> def rotr(x, n, w=32): return ((x \>\> n) \| (x \<\< (w-n))) & 0xFFFFFFFF sigma0 = lambda x: rotr(x,2) \^ rotr(x,13) \^ rotr(x,22) sigma1 = lambda x: rotr(x,6) \^ rotr(x,11) \^ rotr(x,25) ch = lambda e,f,g: (e&f)\^(\~e&g)&0xFFFFFFFF maj = lambda a,b,c: (a&b)\^(a&c)\^(b&c) H0 = \[0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19\] T2_0_nop = (sigma0(H0\[0\]) + maj(H0\[0\], H0\[1\], H0\[2\])) % 2\*\*32 assert hex(T2_0_nop) == \'0x8909ae5\' \# 0x08909ae5

D_word = 4 D_bit = 6 T2\^(0)\_0 = 0x08909ae5 residual \~ 16
