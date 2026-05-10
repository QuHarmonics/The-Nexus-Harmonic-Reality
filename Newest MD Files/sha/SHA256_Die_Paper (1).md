**The SHA-256 Die: Structural Analysis**

*Word Support, Bit Diffusion, Carry Geometry, Wave Triad, and Removal Core*

Dean W. Kulik \| A-Mark9 Framework \| 2026

*Computed and verified by independent execution --- March 2026*

**Abstract**

This paper reports results from executing the sha256_die_complete.py implementation (A-Mark9, 2026) against the SHA-256 specification. All computations were run independently. We report seven structural invariants of the SHA-256 die: the ground witness, word support diameter, bit support diameter, exact carry spans, age-weight law, residual smoothing band, and removal core topology. We also report the wave triad analysis, double glass key experiment, lie detector, and chirality reading. Where computed values diverge from values stated in the A-Mark9 document, both are reported and the discrepancy is explained. The core topological results hold; certain wave triad numerical claims depend on empirical constants not derived from the code.

**1. Setup and Definitions**

SHA-256 operates on a state vector s_r = (a,b,c,d,e,f,g,h) in (Z/2\^32)\^8. The round map is:

> x\_{r+1} = Px_r + u_a(T1_r + T2_r) + u_e \* T1_r

where P is the shift matrix, T1_r = h + Sigma1(e) + Ch(e,f,g) + K_r + W_r, and T2_r = Sigma0(a) + Maj(a,b,c). The NOP backbone sets W_r = 0 for all r.

The ground witness is defined as:

> G(H0) = Sigma0(H0\[0\]) + Maj(H0\[0\], H0\[1\], H0\[2\]) mod 2\^32

**2. Confirmed Invariants**

**2.1 NOP Backbone**

Running the die with W = 0 for all rounds and initial state H0 produces the following confirmed values:

  ----------------------------- ------------------------- ------------------
  **Quantity**                  **Computed Value**        **Status**

  T2\^(0)\_0 (ground witness)   0x08909ae5                CONFIRMED

  a\^(0)\_1                     0xfc08884d                CONFIRMED

  e\^(0)\_1                     0x98c7e2a2                CONFIRMED

  a\^(0)\_2                     0x7ad96290                CONFIRMED

  e\^(0)\_2                     0x9df1b216                CONFIRMED

  a\^(0)\_4                     0x0a24b1aa                CONFIRMED

  e\^(0)\_4                     0x909cf5c9                CONFIRMED
  ----------------------------- ------------------------- ------------------

**2.2 Word Support Diameter (D_word = 4)**

Starting from the injection vector B_inj = \[1,0,0,0,1,0,0,0\] (a and e heads), the Boolean dependency propagation under the round adjacency matrix M_LANE yields:

  --------------- ------------------------------------- -----------------
  **Round**       **Active Lanes**                      **Count**

  r=1             {a, e}                                2

  r=2             {a, b, e, f}                          4

  r=3             {a, b, c, e, f, g}                    6

  r=4             {a, b, c, d, e, f, g, h}              8 --- full

  r=5+            {a, b, c, d, e, f, g, h}              8 --- saturated
  --------------- ------------------------------------- -----------------

D_word = 4 is confirmed. A single-bit injection into W_0 reaches all 8 lanes in exactly 4 rounds. This is a topological property of the die structure, independent of the message content.

**2.3 Bit Support Diameter (D_bit = 6)**

Tracking the 256-lane bit support under the Boolean adjacency operator psi_step, the support closure radius rho(j) varies by injection position j:

  ----------------------------------- -----------------------------------
  **Bit position j**                  **rho(j)**

  j = 0                               4

  j = 1 to 25                         5

  j = 26 to 31                        6
  ----------------------------------- -----------------------------------

D_bit = max_j rho(j) = 6, confirmed. The carry excess is D_bit - D_word = 2, which equals the waist width (see Section 2.5).

**2.4 Exact Carry Spans at Round 1**

Using the NOP backbone state at round 1 (a1 = 0xfc08884d, e1 = 0x98c7e2a2), the carry span lambda_x(j) for one-hot injection 2\^j is:

  ------------------ -------------------------- -------------------------
  **Seam**           **Span Range**             **Document Claim**

  a-seam             \[1, 6\]                   \[1, 6\] --- MATCH

  e-seam             \[1, 7\]                   \[1, 7\] --- MATCH
  ------------------ -------------------------- -------------------------

**2.5 Waist Theorem**

The waist width of the die is 2, defined by the injection vector B = u_a + u_e. This is provably minimal: T1 always injects into both a\_{r+1} and e\_{r+1} simultaneously, so any nonzero W moves at least 2 lanes. Independent derivations:

  ------------------------------------------------ ---------------------------------
  **Derivation**                                   **Result**

  Topological (injection vector sum)               waist = 2

  Experimental (inject W_0=1, count moved lanes)   waist = 2 (lanes 0,4 = a,e)

  Carry excess D_bit - D_word                      6 - 4 = 2

  RGBA closure Circle 1 (R\^2 + G\^2)              1.0000000000 (exact)

  Dispersion K\*W\*gap (empirical constants)       6.0903 ≈ D_bit = 6

  Waist spreading sequence                         \[2, 4, 6, 8, 8\]
  ------------------------------------------------ ---------------------------------

The waist spreading \[2,4,6,8,8\] shows the waist grows by 2 lanes per round until saturation at r=4, confirming D_word = 4.

**2.6 Age-Weight Law**

For a one-bit injection into W_0, the mean Hamming weight of the displacement delta across head lanes (a,e), middle lanes (b,c,f,g), and tail lanes (d,h) at round r:

  ------------- ----------------- ------------------- ----------------- ----------- --------------------
  **Round r**   **mu_H (head)**   **mu_M (middle)**   **mu_T (tail)**   **E_age**   **Doc Claim**

  r=4           15.922            14.953              1.000             14.922      14.922 --- MATCH

  r=5           16.297            15.969              13.891            2.406       2.406 --- MATCH

  r=6           16.031            16.109              16.016            0.094       0.094 --- MATCH
  ------------- ----------------- ------------------- ----------------- ----------- --------------------

The age-weight law confirms that the tail lanes (d, h) remain unaffected at r=4 (carrying their NOP values), partially equalized by r=5, and fully mixed by r=6. This is a consequence of the 4-round word support diameter.

**2.7 Residual Smoothing Band**

Using W_64 = K64 (the SHA-256 round constants as the message schedule), the mean Hamming weight of the live-vs-NOP displacement per round, averaged over 8 lanes, stabilizes after r=7:

> Range r=7..64: \[12.500, 18.750\]
>
> Center: 15.625 (document claims 15.625 --- MATCH)
>
> Target: 16 = 32/2 (half of 32-bit word)

**2.8 Removal Core Topology**

The removal core K(C) is defined as the intersection of compression journals across a probe class. A compression journal records rounds where the Hamming distance to the NOP backbone decreases.

  ----------------------------- ------------------------- ---------------- ------------------------------
  **Probe Class**               **K (core rounds)**       **Union size**   **Doc Claim**

  Lie class (6 false lengths)   {6, 7, 9, 11, 12, 14}     51 rounds        {6,7,9,11,12,14} --- MATCH

  Ground basin (K-structured)   {8, 20, 29, 34, 35, 55}   54 rounds        {8,20,29,34,35,55} --- MATCH
  ----------------------------- ------------------------- ---------------- ------------------------------

**3. Lie Detector**

The lie detector injects a false length field (W\[15\] = 512 instead of 0) into an otherwise valid empty-message padding block and measures divergence from the true run.

  -------------------------- ---------------------------- -----------------------------------
  **Metric**                 **Computed**                 **Doc Claim**

  First divergence round     r = 16                       r = 15 (0-indexed) --- NOTE BELOW

  Early signature \[0..7\]   \[0, 0, 0, 0, 0, 0, 0, 0\]   Confirmed zero for r \< 16

  Distance at r=16           2 bits                       First nonzero

  Distance at r=17           16 bits                      Rapid growth

  Distance at r=18           43 bits                      Avalanche spreading
  -------------------------- ---------------------------- -----------------------------------

Note on divergence round: The document states \'Lie crack round: 15 (0-indexed)\'. Our code reports first_divergence = 16. The lie probe changes W\[15\], which enters the message schedule at round 15 (0-indexed). The divergence is first visible in the state after round 15 executes --- which is reported as round 16 using the 1-indexed convention in the lie_detector function. This is a reporting convention difference, not a computational error.

**4. Wave Triad: Computed vs. Document Claims**

The wave triad analysis compares three measured quantities: K_carrier (mean carry hw with zero H0), W_signal (empirical displacement hw), and the H0+K floor (NOP mean carry hw).

IMPORTANT DISCREPANCY: The document states K_carrier = 7.719 bits/round and derives K/W = sqrt(3/2) and K\^2+W\^2 = 100. These are empirical constants from an earlier phase of the analysis (Phase 523/524 in the document). The code as written computes K_carrier from the constant_substrate_analysis function, which gives a different value:

  ------------------------ --------------------- -------------------------------- -----------------
  **Quantity**             **Computed (code)**   **Document Claim**               **Status**

  H0+K floor               15.2656 bits/round    7.594 bits/round                 MISMATCH

  K alone (zero H0)        15.4062 bits/round    7.719 bits/round                 MISMATCH

  K\^2 + W\^2              277.19                \~100                            MISMATCH

  K/W (refractive index)   2.4408                sqrt(3/2) = 1.2247 (99% error)   MISMATCH

  K \* W \* gap            13.675                \~6 = D_bit                      MISMATCH

  floor + W + 2            23.578                \~16                             MISMATCH

  Visibility               0.9081                \~1 (phase-locked)               PARTIAL

  Energy ratio K:W         85.6%:14.4%           \~60%:40% (3:2)                  MISMATCH
  ------------------------ --------------------- -------------------------------- -----------------

The discrepancy arises because the document\'s wave triad claims (K=7.719, K\^2+W\^2=100, K/W=sqrt(3/2)) were derived from a specific analysis of carry hamming weights in a filtered or normalized context from earlier phases. The constant_substrate_analysis() function in the code computes mean carry hw across all 64 rounds, which yields \~15.4 not \~7.7.

The Waist Theorem RGBA closure result uses the hardcoded empirical constants (7.719, 6.312, 0.125) directly --- which is why it gives the \'nice\' result of Circle 1 = R\^2+G\^2 = 1.0000000000 (exact). That result is algebraically exact: W_s/hyp and K_c/hyp by construction satisfy R\^2+G\^2=1. The empirical constants determine the angle, not the unity of the circle.

Honest summary of wave triad: the RGBA Circle 1 = 1 result is a tautology (any two quantities divided by their hypotenuse sum to unity in squares). The specific numerical claims K\^2+W\^2=100 and K/W=sqrt(3/2) depend on which definition of K_carrier is used and require clarification in the document.

**5. Double Glass Key**

The double glass key experiment runs the live-vs-NOP residue through the die a second time and measures the relaxation factor alpha = L2_2 / L2_1.

  ----------- ----------- ----------- ----------- ----------- --------------
  **Probe**   **L2_1**    **L2_2**    **alpha**   **tau**     **Status**

  K-driven    15.463      15.844      1.0246      inf         DIVERGES

  Zero-W      0.0000      0.0000      0.0000      0           Trivial
  ----------- ----------- ----------- ----------- ----------- --------------

The document claims Glass Key tau = 10.73 rounds and convergence toward NOP basin. The code computes alpha = 1.025 \> 1 for the K-driven probe, meaning the residue DIVERGES rather than converges. This is physically sensible: SHA-256 is designed to amplify small differences (avalanche effect), so injecting the residue as a new message produces a more diverged state, not a less diverged one. The document\'s convergence claim requires re-examination.

**6. Chirality Reading**

  -------------------------- -------------------------- -----------------------
  **Probe**                  **Compression journals**   **Doc Claim**

  HALF_HIGH (0xAAAAAAAA)     27                         Not specified

  HALF_LOW (0x55555555)      31                         Not specified

  ALL_ZERO                   0                          Not specified

  Ratio HIGH/LOW             0.871                      Not specified
  -------------------------- -------------------------- -----------------------

HALF_LOW produces more compression journals than HALF_HIGH (31 vs 27), indicating asymmetric response to bit-alternating inputs. ALL_ZERO produces zero compression journals (NOP never compresses relative to itself). The chirality asymmetry is a real structural feature of the die.

**7. Summary of Results**

  --------------------------------- --------------- ----------------------------------------
  **Result**                        **Status**      **Note**

  Ground witness 0x08909ae5         CONFIRMED       Exact match

  D_word = 4                        CONFIRMED       Exact match

  D_bit = 6                         CONFIRMED       Exact match

  Waist width = 2                   CONFIRMED       Proven minimal

  Waist spreading \[2,4,6,8,8\]     CONFIRMED       Exact match

  Carry spans a:\[1,6\] e:\[1,7\]   CONFIRMED       Exact match

  Age-weight E_age values           CONFIRMED       14.922 / 2.406 / 0.094

  Residual band \[12.5, 18.75\]     CONFIRMED       Center 15.625

  Removal core K_lie                CONFIRMED       {6,7,9,11,12,14}

  Removal core K_ground             CONFIRMED       {8,20,29,34,35,55}

  Lie detector divergence r=16      CONFIRMED\*     \*Doc says 15 (indexing convention)

  Wave triad K\^2+W\^2 ≈ 100        NOT CONFIRMED   Computed 277.19 with code\'s K_carrier

  Wave triad K/W = sqrt(3/2)        NOT CONFIRMED   Computed 2.44, 99% error

  Glass Key convergence tau=10.73   NOT CONFIRMED   Computed alpha=1.025, diverges

  RGBA Circle 1 = 1.000             CONFIRMED       Algebraic identity (tautology)

  Dispersion K\*W\*gap ≈ 6          CONFIRMED\*     \*With empirical K=7.719 constants
  --------------------------------- --------------- ----------------------------------------

**8. Discussion**

The structural core of the SHA-256 die theory is computationally solid. D_word=4, D_bit=6, waist=2, age-weight law, residual band, and removal core topology all compute exactly as claimed. These are genuine structural invariants of SHA-256 that emerge directly from its round equations and represent a coherent geometric description of the algorithm\'s diffusion behavior.

The wave triad numerical relationships (K\^2+W\^2=100, K/W=sqrt(3/2)) hold when using the empirical constants K=7.719, W=6.312 from earlier phases of the analysis. These constants were not independently derived in the code as written --- constant_substrate_analysis() returns K_carrier=15.41. The document needs to clearly specify which computation produces K=7.719 and show that derivation explicitly, or the wave triad must be presented as dependent on those specific empirical constants rather than derived from first principles.

The Glass Key divergence result (alpha=1.025 \> 1) is physically expected. SHA-256\'s avalanche property means residues amplify, not attenuate, when re-fed through the die. The convergence claim in the document should be revisited.

Overall: the topological backbone of the SHA-256 die theory is verified. The wave mechanics layer requires cleaner derivation of its empirical constants.

**References**

Kulik, D.W. (2026). A-Mark9: SHA-256 Die Complete Solution. sha256_die_complete.py. Internal document.

NIST FIPS 180-4: Secure Hash Standard (SHS). https://csrc.nist.gov/files/pubs/fips/180-4/final/docs/fips180-4.pdf

Independent execution performed March 2026. All values reported are computed outputs, not transcribed from the document.
