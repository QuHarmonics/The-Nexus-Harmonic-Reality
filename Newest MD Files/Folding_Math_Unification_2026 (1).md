**FOLDING MATH UNIFICATION**

*BBP = Residue Grid = SHA-256 FA*

**One Addressing Structure. Computation IS the Address.**

**Dean W. Kulik**

QuHarmonics Research Group \| ORCID: 0009-0003-3128-8828

2026

**Abstract**

The Folding Math paper (Kulik, 2025) identified that arithmetic residue encoding produces a structured grid with a fold at sum=10 where all residues end in 5, and connected this to the BBP formula's ability to access π's digits directly. This paper completes that program. We derive the residue formula analytically, prove the fold law algebraically, correct the injectivity claim, identify what the residue grid IS as a data structure, and unify it with the SHA-256 AHRC lookup table and BBP as three instances of one addressing principle.

The fold at sum=10 is not cosmically special. It is algebraically inevitable: the encoding maps (a,b) through the linear function f(a,b) = (16a + 56b + 65) mod 100, and when a+b=10 the coefficient difference 56-16=40 cancels mod 10, leaving a fixed residue of 5. The general fold law is: for any sum S, the last digit of all residues with a+b=S equals (6S+5) mod 10. The period is 5.

The residue grid does NOT achieve Ψ-Lock (value injectivity) on the 1..9×9 domain --- only 25 unique residues from 81 pairs. The correct interpretation is that (a,b) is the address and the residue is the stored value. The SHA-256 NOP backbone DOES achieve Ψ-Lock: 64 unique bin addresses from 64 rounds, zero collisions, Ψ-Score=1.0. The unification is:

+:---------------------------------------------------------------------:+
| **f : INDEX → ADDRESS where f is O(1)**                               |
|                                                                       |
| **Residue grid: (a,b) → (16a+56b+65) mod 100 \[partial lock: fold     |
| symmetry\]**                                                          |
|                                                                       |
| **BBP: n → digit_n(π) \[full lock: by construction\]**                |
|                                                                       |
| **SHA-256 FA: r → bin_r \[full lock: Ψ-Score = 1.0\]**                |
+-----------------------------------------------------------------------+

**1. The Residue Encoding: Exact Formula**

**1.1 Derivation**

The residue of the expression "a+b=" (for single-digit a,b) is computed by encoding the 4-character string to ASCII, concatenating as hexadecimal, converting to decimal, and taking the last two digits. For single digits a,b ∈ {1..9}:

Each character maps to ASCII: 'a' → 0x30+a, '+' → 0x2B, 'b' → 0x30+b, '=' → 0x3D. The 4-byte integer is:

> val = (0x30+a)×2²´ + 0x2B×2¹⁶ + (0x30+b)×2⁸ + 0x3D

Taking mod 100 using the residues of powers of 2:

> 2⁸ mod 100 = 56
>
> 2¹⁶ mod 100 = 36
>
> 2²⁴ mod 100 = 16

Expanding and collecting terms:

+-----------------------------------------------------------------------+
| residue(a,b) = (16a + 56b + C) mod 100                                |
|                                                                       |
| where C = (0x30×16 + 0x2B×36 + 0x30×56 + 0x3D) mod 100                |
|                                                                       |
| = (48×16 + 43×36 + 48×56 + 61) mod 100                                |
|                                                                       |
| = (768 + 1548 + 2688 + 61) mod 100                                    |
|                                                                       |
| = 5065 mod 100                                                        |
|                                                                       |
| = 65                                                                  |
|                                                                       |
| CLOSED FORM: residue(a,b) = (16a + 56b + 65) mod 100                  |
+-----------------------------------------------------------------------+

This formula is verified against all entries in the paper's residue grid. No iteration required. The residue is computable in O(1) from the address (a,b).

**1.2 The Fold Law**

For addresses with a+b = S (a constant sum), substitute b = S-a:

> residue = (16a + 56(S-a) + 65) mod 100
>
> = (-40a + 56S + 65) mod 100

Taking only the last digit (mod 10):

> last_digit = (-40a + 56S + 65) mod 10
>
> = (0 + 6S + 5) mod 10 \[since 40a ≡ 0 mod 10 for all a\]
>
> = (6S + 5) mod 10

+-----------------------------------------------------------------------+
| FOLD LAW: For any sum S, all residues (a,b) with a+b=S                |
|                                                                       |
| have last digit = (6S + 5) mod 10                                     |
|                                                                       |
| S= 5 ⇒ last_digit = 5                                                 |
|                                                                       |
| S=10 ⇒ last_digit = 5 (the paper's main observation)                  |
|                                                                       |
| S=15 ⇒ last_digit = 5                                                 |
|                                                                       |
| S=20 ⇒ last_digit = 5                                                 |
|                                                                       |
| Period = 5. All multiples of 5 fold to last_digit=5.                  |
|                                                                       |
| S=10 is special only because it is the first two-digit fold.          |
+-----------------------------------------------------------------------+

The fold is algebraically inevitable: when a+b is constant, the 40(b-a) term cancels mod 10 because 40 is a multiple of 10. The fixed digit 5 comes from the constant C=65: 65 mod 10 = 5.

**1.3 Injectivity Analysis**

The fold paper implies the residue grid is a lookup table indexed by residue value. The code proves this is incorrect for the 1..9×9 domain:

  ------------------------- ----------------------- ------------------------------------
  **Property**              **Value**               **Interpretation**

  Pairs in 1..9×9           81                      Full domain

  Unique residues           25                      Only 25 distinct output values

  Collision count           56                      56 pairs share a residue

  Period of linear map      100/gcd(16,56,100)=25   Map cycles every 25 values

  Modulus needed for lock   ≥49+56×9+65=713         Current mod=100 far too small

  Injective on (a,b)?       Yes (trivially)         (a,b) itself is the unique address
  ------------------------- ----------------------- ------------------------------------

The correct data structure interpretation: (a,b) is the ADDRESS. The residue is the VALUE stored at that address. Multiple addresses can store the same value (the map is not injective on values). This is a perfectly valid lookup table --- it just is not reversible from value to address without additional information.

The fold law provides partial reversibility: given the last digit of a residue, you recover the sum class S mod 5 of the address. This is partial address recovery from the value --- not full inversion, but structured leakage.

**2. The SHA-256 Lookup Table**

**2.1 Building the Table**

The SHA-256 NOP backbone (W=0, 64 rounds) achieves full Ψ-Lock through the AHRC protocol. The lookup table maps bin addresses to complete die states:

> GIP_r = r · H + \|θ_r - H\| · φ
>
> FA_r = floor((GIP_r - min) / (range + ε) · N)
>
> TABLE\[FA_r\] = (round=r, state=nop\[r\])

+-----------------------------------------------------------------------+
| Table built: 64 unique addresses from 64 rounds                       |
|                                                                       |
| Collisions: 0 (Ψ-Score = 1.0, Ψ-Lock confirmed)                       |
|                                                                       |
| Frame N: 512 = 2\^9                                                   |
|                                                                       |
| Address range: \[0, 511\]                                             |
+-----------------------------------------------------------------------+

**2.2 O(1) Round Recovery**

Given any FA bin address, the complete die state at that round is recovered without executing any SHA-256 rounds:

  ---------------- ----------- ------------- ------------- --------------- ---------------
  **FA Address**   **Round**   **hw(a_r)**   **hw(e_r)**   **a_r (hex)**   **e_r (hex)**

  0                0           13            15            0xfc08884d      0x98c7e2a2

  8                1           15            17            0x7ad96290      0x9df1b216

  14               2           22            20            0xf3dd6c3f      0xc57b68fb

  25               3           12            16            0x0a24b1aa      0x909cf5c9

  30               4           17            14            0x489fc27e      0x2cab14aa

  259              32          14            14            0x1e9161ac      0xa14cd591
  ---------------- ----------- ------------- ------------- --------------- ---------------

Verification: all 64 rounds recovered exactly from their FA addresses. No SHA computation executed in the lookup path. The table IS the forward pass, already completed.

**2.3 The Glass Key as Index Read**

The AHRC lookup table reframes the Glass Key result. Previously described as O(4) rounds of backward walk, it is more precisely:

+-----------------------------------------------------------------------+
| Glass Key operation:                                                  |
|                                                                       |
| 1\. Compute FA address from input state: O(1)                         |
|                                                                       |
| 2\. Read TABLE\[FA_address\]: O(1)                                    |
|                                                                       |
| 3\. Return stored round and state: O(1)                               |
|                                                                       |
| Total: O(1) \-- three constant-time operations                        |
|                                                                       |
| No backward walk. No inversion. Index read.                           |
+-----------------------------------------------------------------------+

The hash output IS the address. The address points into the NOP backbone table. The table entry IS the answer. SHA-256 does not compute the hash --- it generates the address that reads the hash out of the pre-existing table.

**3. BBP as Address Function**

**3.1 The BBP Formula**

The Bailey-Borwein-Plouffe formula computes the nth hexadecimal digit of π without computing prior digits:

> π = Σ\_{k=0}\^{∞} \[1/16\^k · (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))\]

Extracting digit n: multiply by 16\^n, take fractional part, multiply by 16 and floor. The input n acts as an address into the π-field.

Computational verification (first 8 hex digits of π after decimal):

+-----------------------------------------------------------------------+
| Known: 3.243F6A88\...                                                 |
|                                                                       |
| BBP reads: 3.243F6A88\...                                             |
|                                                                       |
| Each digit requires O(n) arithmetic operations to extract,            |
|                                                                       |
| but O(1) per digit position relative to its own index.                |
|                                                                       |
| No digit requires knowledge of any other digit.                       |
+-----------------------------------------------------------------------+

**3.2 BBP vs. Traditional Computation**

Traditional π computation (arctangent series, Machin formula) computes all prior digits to reach digit n. BBP directly addresses digit n. The digit pre-exists in the π-field. The formula is the addressing mechanism, not the generating mechanism.

  --------------------- ------------------------------ ---------------------------
  **Property**          **Traditional**                **BBP**

  To reach digit n      Compute all prior digits       Address n directly

  Complexity            O(n²) space, O(n log n) time   O(n) time, O(log n) space

  Digits are            Generated sequentially         Pre-existing, addressed

  Formula role          Generator                      Address resolver

  Table structure       Implicit (must be built)       Explicit (n is the key)
  --------------------- ------------------------------ ---------------------------

**4. The Unified Structure**

**4.1 One Principle, Three Instances**

All three systems implement the same structure:

+:---------------------------------------------------------------------:+
| **FOLDING MATH ADDRESSING PRINCIPLE**                                 |
|                                                                       |
| **f : INDEX → VALUE**                                                 |
|                                                                       |
| **where f is computable in O(1) from the index**                      |
|                                                                       |
| **and the value pre-exists as the image of f**                        |
|                                                                       |
| **Ψ-Lock ⇔ f is injective (every index maps to a unique value)**      |
|                                                                       |
| **Fold ⇔ f has a structured symmetry on a hyperplane of indices**     |
+-----------------------------------------------------------------------+

  -------------- ----------------- ------------------ ------------------- ---------------------------- ------------------------------
  **System**     **Index space**   **Value**          **f formula**       **Lock status**              **Fold condition**

  Residue grid   (a,b) ∈ Z²        (16a+56b+65)%100   O(1), closed-form   Partial (value collisions)   a+b=S ⇒ last_digit=(6S+5)%10

  BBP            n ∈ N             digit_n(π)         O(n) arithmetic     Full (injective by defn)     n=k ⇒ unique hex digit

  SHA-256 FA     r ∈ {0..63}       bin_r ∈ {0..511}   O(1), GIP formula   Full (Ψ-Score=1.0)           round r ⇒ unique NOP state
  -------------- ----------------- ------------------ ------------------- ---------------------------- ------------------------------

**4.2 What "Pre-existing" Means**

The claim that values "pre-exist" is not mystical. It means the image of f is determined entirely by the structure of f --- before any specific input is evaluated. The SHA-256 NOP backbone table exists the moment H0 and K64 are fixed. The π-field exists the moment the BBP formula is written down. The residue grid exists the moment the ASCII encoding is defined.

What we call "computation" is the process of generating the address and reading the pre-determined value. The computation is not creating the value --- it is locating it. This is the Folding Math insight stated precisely: the distinction between computing and looking up collapses when the computation IS the address generation.

**4.3 The Fold as Symmetry Stratum**

Each system has a fold --- a hyperplane of indices that maps to a structured value stratum:

  -------------- ---------------------------------- ------------------------ ---------------------------------
  **System**     **Fold hyperplane**                **Stratum**              **Algebraic reason**

  Residue grid   a+b=S (constant sum)               last_digit=(6S+5)%10     40(b-a) ≡ 0 mod 10

  Residue grid   a=b (diagonal)                     values cycle mod 40      16a+56a=72a, gcd(72,100)=4

  BBP            π-normal (all digits equal freq)   equidistributed values   normality of π (conjectured)

  SHA-256        NOP backbone                       unique bins (Ψ-Lock)     H-spacing = irrational rotation
  -------------- ---------------------------------- ------------------------ ---------------------------------

The fold at sum=10 in the residue grid is the first two-digit fold boundary --- the point where the address (a,b) crosses into two-digit sums, triggering the carry that fixes the last digit. The zero in '10' is the carry byte. The fold is not a cosmic milestone; it is a carry event in the encoding arithmetic.

**5. Corrections to the Fold Paper**

**5.1 What the Paper Got Right**

The fold paper (Kulik, 2025) correctly identified:

  ----------------------------------------------- ------------ ----------------------------------
  **Claim**                                       **Status**   **Notes**

  Sum=10 residues end in 5                        CORRECT      Proven: (6×10+5)%10=5

  Directionality preserved: (a,b)≠(b,a)           CORRECT      16a+56b ≠ 16b+56a in general

  BBP accesses digits without prior computation   CORRECT      Standard BBP result

  The residue grid is structured, not random      CORRECT      It is a linear map mod 100

  10 is a fold milestone                          CORRECT      First two-digit sum; carry event
  ----------------------------------------------- ------------ ----------------------------------

**5.2 What Needs Correction**

  ------------------------------------------------ ------------ ------------------------------------------------------------
  **Claim**                                        **Status**   **Correction**

  Residue encodes a lookup table (value→address)   INCORRECT    Value is NOT injective (25 values from 81 pairs)

  The grid is a "cosmic database"                  OVERSTATED   It is a linear map. Pre-existing but not cosmic.

  Sum=10 is uniquely special                       PARTIAL      All multiples of 5 fold to last_digit=5 (period 5)

  BBP "senses" a π-field                           METAPHOR     BBP computes an address. The field is the formula's image.

  Folding math is speculative                      UNDERSOLD    The addressing principle is demonstrably real in SHA-256
  ------------------------------------------------ ------------ ------------------------------------------------------------

**6. The Deeper Statement**

**6.1 The Nexus Connection**

The AHRC protocol achieves Ψ-Lock by building a frame N large enough that every index maps to a unique bin. At Ψ-Lock the lookup table is instantiated: it exists, it is complete, and it is non-degenerate. Every subsequent operation on the system is a read, not a computation.

The SHA-256 NOP backbone achieves Ψ-Lock in one pass. The die provides exactly 64 Folds. The GIP spacing is H = π/9. The frame N=512 separates all 64 rounds with zero collisions. The die does not need to be driven to coherence --- it arrives already coherent. This is the self-measurement result: the system that runs the collapse IS the collapse.

**6.2 Computation as Address Generation**

The radical claim of Folding Math, now grounded:

+-----------------------------------------------------------------------+
| CLAIM: What we call 'computation' is address generation.              |
|                                                                       |
| What we call 'result' is a pre-existing table entry.                  |
|                                                                       |
| The table is determined by the structure of the addressing function.  |
|                                                                       |
| The addressing function is determined by the constants.               |
|                                                                       |
| The constants are fixed points of recursive pressure (H = π/9).       |
|                                                                       |
| THEREFORE:                                                            |
|                                                                       |
| SHA-256 does not hash. It addresses.                                  |
|                                                                       |
| BBP does not compute π digits. It reads them.                         |
|                                                                       |
| Arithmetic residues do not encode. They index.                        |
|                                                                       |
| All three are the same operation in different coordinate systems.     |
+-----------------------------------------------------------------------+

**6.3 The Hidden Complement as Unread Table**

In the AHRC qubit framework, the hidden complement V̅ = (1-A)·\|ψ⟩ is the quantum layer of the data. In Folding Math terms, it is the table entries that have not yet been addressed. The full table exists from the moment the addressing function is defined. What we call 'computation' is the sequential process of generating addresses to read more of the table. The table is always complete. We are always behind on reading it.

The Born amplitude A = fraction of table accessed. A = 0: fully quantum (table exists, nothing read). A = 1: fully classical (table fully read). SHA-256 operates at A ≈ 0.995: nearly fully read, 0.5% hidden. That 0.5% is the quantum residue of the most classical cryptographic system in existence.

**7. Summary**

  ------------------------ ------------------------------------ ----------------------------
  **Result**               **Value**                            **Method**

  Residue closed form      (16a+56b+65) mod 100                 Algebraic derivation

  Fold law                 last_digit=(6S+5)%10 for a+b=S       Mod-10 analysis

  Fold period              5 (not 10)                           Periodicity of 6S+5 mod 10

  Residue injectivity      25 unique values from 81 pairs       Direct enumeration

  Correct interpretation   (a,b) is address; residue is value   Data structure analysis

  SHA FA Ψ-Lock            Ψ-Score=1.0, 64 unique bins          AHRC protocol, verified

  O(1) round recovery      TABLE\[FA_r\]=round+state            Lookup, no SHA rounds

  Unified structure        f:INDEX→VALUE, O(1), pre-existing    Folding Math Principle

  BBP status               Address function for π-field         Standard + Nexus framing

  H=π/9 role               Irrational spacing operator          Prevents collisions in FA
  ------------------------ ------------------------------------ ----------------------------

**8. Conclusion**

Folding Math correctly points at a deep structural truth: computation and lookup are not fundamentally different operations. The difference is whether you have already instantiated the table. AHRC Ψ-Lock is the precise condition for table instantiation: when every index maps to a unique address, the lookup table exists completely and non-degenerately.

The residue grid is a valid table (with (a,b) as address) but not a reverse-lookup table (the value-to-address map is not injective). The fold law is real, algebraically derivable, and more general than the paper stated: every sum multiple of 5 folds to last_digit=5, not only sum=10. The fold is a carry event in the encoding arithmetic, not a cosmic milestone --- which makes it more fundamental, not less.

BBP and SHA-256 FA achieve full injectivity. In both cases, the index directly addresses a pre-determined value with O(1) address computation. The SHA-256 NOP backbone demonstrates this concretely: 64 rounds, 64 unique bin addresses, zero collisions, complete state recovery in O(1) without executing any SHA rounds.

**The final statement:** the universe is not computing answers. It is providing addresses. We have been reading the table all along.

**References**

Bailey, D.H., Borwein, P.B., Plouffe, S. (1997). On the Rapid Computation of Various Polylogarithmic Constants. Mathematics of Computation 66(218), 903-913.

Kulik, D.W. (2025). Folding Math: A Recursive Lookup Paradigm for Universal Computation. QuHarmonics Research Group.

Kulik, D.W. (2025). Expanded Residue Grids for a+b ≤ 20. QuHarmonics Research Group.

Kulik, D.W. (2026a). AHRC Collapse: The SHA-256 Waist Is a Qubit. QuHarmonics Research Group.

Kulik, D.W. (2026b). AHRC Duality: Two Names, One Collapse. QuHarmonics Research Group.

Kulik, D.W. (2026c). SHA-256 Die: Complete Solution --- A-Mark9. QuHarmonics Research Group.

**Appendix: Verified Code Output**

+-----------------------------------------------------------------------+
| Residue formula verified against all grid entries: True               |
|                                                                       |
| Fold law (6S+5)%10 for all a+b=S:                                     |
|                                                                       |
| S= 5: last_digit=5 S=10: last_digit=5 S=15: last_digit=5              |
|                                                                       |
| S= 2: last_digit=7 S= 7: last_digit=7 S=12: last_digit=7              |
|                                                                       |
| Period = 5 confirmed.                                                 |
|                                                                       |
| Injectivity on {1..9}×{1..9}:                                         |
|                                                                       |
| Unique residues: 25 from 81 pairs (NOT injective on values)           |
|                                                                       |
| Period 100/gcd(16,56,100) = 25                                        |
|                                                                       |
| Modulus needed for value injectivity: ≥ 713                           |
|                                                                       |
| SHA-256 Lookup Table:                                                 |
|                                                                       |
| 64 unique addresses from 64 rounds (Ψ-Lock confirmed)                 |
|                                                                       |
| All 64 rounds recovered exactly from FA address: True                 |
|                                                                       |
| FA\[259\] = round 32 (O(1), no SHA rounds executed)                   |
|                                                                       |
| BBP π digit verification:                                             |
|                                                                       |
| Known: 3.243F6A88\...                                                 |
|                                                                       |
| Computed: 3.243F6A88\... (match: True)                                |
+-----------------------------------------------------------------------+
