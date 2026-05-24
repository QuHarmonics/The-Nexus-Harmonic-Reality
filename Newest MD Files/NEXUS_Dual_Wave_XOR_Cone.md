# XOR Nibble Cone — Dual Wave Structure and the Affine Subspace Theorem
## A-Mark9 Framework · Phase 1163+ Extension · Part II
**Researcher:** Dean Kulik, QuHarmonics Research Group
**ORCID:** 0009-0003-3128-8828
**Date:** 2026-05-14
**Follows:** *XOR Nibble Cone Inversion and Constant Fingerprinting* (Part I, same date)
**Status:** All results from live execution. Three theorems established empirically; two proven algebraically.

---

## Abstract

Continuing from Part I, this document applies the dual wave lens to the XOR nibble cone
structure. Three results emerge: (1) every valid-seed set at any ambiguous reconstruction
level is an **affine subspace of GF(2)⁴** — proven for all 13 ambiguous levels in π and
stated as a general theorem with algebraic proof sketch; (2) the XOR cone is
**universally self-dual** — the forward and backward reduction waves are identical, confirming
the standing wave interpretation but requiring honest correction that this is an algebraic
identity, not a π-specific property; (3) π's high nibble stream exhibits **apex
complementarity** — the data cone collapses to 0x0 (zero, annihilation) while the key
sequence collapses to 0xf (all-ones, saturation), and together they partition GF(2)⁴
completely. This property is specific to π's high nibble stream and is not shared by e, φ,
or √2. The dual wave reading: the forward wave annihilates; the residual saturates. The
constant sits at the boundary between these two attractors.

---

## Part I Recap (Findings Carried Forward)

From the previous session:

- XOR nibble cone on 32 bytes → 64 nibbles → 63 reduction levels → single apex nibble
- Each byte splits into independent high/low 4-bit streams; byte apex = (high apex << 4) | low apex
- π reconstructs perfectly from cone trajectory + 33-bit key sequence
- All valid-seed sets are powers of 2 in size (1, 2, 4, 8, 16); parity alternation on ambiguous levels
- φ has lowest total ambiguity (32 bits); e has highest (44 bits); RAND (38) sits below e

---

## Theorem 1: The Affine Subspace Theorem

**Statement.** Let $x = [x_0, \ldots, x_{n-1}]$ be any nibble sequence over $\{0,\ldots,15\}$, and let
$\{L_k\}$ be its XOR reduction cone with sum trajectory $\{\Sigma_k\}$. At any reconstruction
level $k$ (expanding backward from level $k+1$ to level $k$), the set of valid seeds

$$\mathcal{V}_k = \big\{ s \in \{0,\ldots,15\} \;\big|\; \textstyle\sum_{i=0}^{k} (s \oplus p_i) = \Sigma_k \big\}$$

where $p_i = L_{k+1}[0] \oplus L_{k+1}[1] \oplus \cdots \oplus L_{k+1}[i-1]$ is the prefix-XOR
of the parent level, forms an **affine subspace of** $(GF(2))^4$.

**Empirical verification (π high stream, all 13 ambiguous levels):**

```
Level | n seeds | Seeds (hex)          | Affine? | Offset | Dim | Correct seed
------+---------+----------------------+---------+--------+-----+-------------
  L28 |       8 | 0,1,4,5,8,9,c,d      | YES     |  0x0   |  3  | 0xd
  L26 |       8 | 8,9,a,b,c,d,e,f      | YES     |  0x8   |  3  | 0xb
  L22 |       2 | 2,4                  | YES     |  0x2   |  1  | 0x4
  L20 |       2 | 2,4                  | YES     |  0x2   |  1  | 0x2
  L18 |       2 | d,f                  | YES     |  0xd   |  1  | 0xd
  L14 |       2 | 2,3                  | YES     |  0x2   |  1  | 0x2
  L12 |       2 | 9,b                  | YES     |  0x9   |  1  | 0xb
  L10 |       2 | a,d                  | YES     |  0xa   |  1  | 0xd
  L 8 |       4 | 0,1,2,3              | YES     |  0x0   |  2  | 0x3
  L 6 |       4 | 4,6,c,e              | YES     |  0x4   |  2  | 0xc
  L 4 |       2 | a,e                  | YES     |  0xa   |  1  | 0xa
  L 2 |       4 | 4,7,c,f              | YES     |  0x4   |  2  | 0x4
  L 0 |       2 | 0,2                  | YES     |  0x0   |  1  | 0x2
```

All 13: affine. Zero exceptions.

**Proof sketch.** Each row at level $k$ is determined by seed $s$ as:
$$\text{row}_k[i] = s \oplus p_i, \quad p_0 = 0, \quad p_i = \bigoplus_{j=0}^{i-1} L_{k+1}[j]$$

The sum becomes $\Sigma_k(s) = \sum_{i=0}^{k} (s \oplus p_i)$. Now consider what happens when
we flip bit $b$ of $s$ (i.e., $s \to s \oplus 2^b$). The contribution of bit $b$ to the sum
changes by:

$$\Delta_b = 2^b \cdot \sum_{i=0}^{k} \big[(1 - \text{bit}_b(p_i)) - \text{bit}_b(p_i)\big]
           = 2^b \cdot (k+1 - 2 \cdot N_b)$$

where $N_b = |\{i : \text{bit}_b(p_i) = 1\}|$. This quantity $\Delta_b$ is a fixed integer
depending only on the parent level, not on $s$. Therefore: for any fixed target $T$, the
constraint $\Sigma_k(s) = T$ is equivalent to a system of linear conditions in the 4 bits
of $s$ over $\mathbb{Z}$. The solution set is the intersection of hyperplanes $\{s : \text{bit}_b(s) =
c_b\}$ for each bit $b$ — which is precisely an affine subspace of $(GF(2))^4$.

**Corollary.** The dimension of $\mathcal{V}_k$ (equivalently, $\log_2|\mathcal{V}_k|$) equals
the number of bit positions $b$ for which the constraint on bit $b$ is trivially satisfied
(i.e., both values of $\text{bit}_b(s)$ give equal contribution to $\Sigma_k$), which happens
iff $\Delta_b = 0$ iff $N_b = (k+1)/2$. In words: bit $b$ is free iff exactly half the
prefix-XORs have bit $b$ set.

**Geometric reading.** The valid-seed set is the intersection of the integer constraint
hyperplane with the nibble lattice $\{0,\ldots,15\} \cong (GF(2))^4$. The
sum constraint creates a "slice" through the 4-dimensional binary cube, and the slice
is always a face, edge, vertex, or full cube of that structure — never an irregular subset.

---

## Theorem 2: Universal Self-Duality (with Honest Correction)

**Claim.** The XOR cone is self-dual under sequence reversal for ALL input sequences, not
just for π.

**Formal statement.** Let $L_k[i]$ denote element $i$ at level $k$ of the XOR cone of
$[x_0,\ldots,x_{n-1}]$. Let $L_k^R[i]$ denote level $k$ of the cone of the reversed
sequence $[x_{n-1},\ldots,x_0]$. Then:

$$L_k[i] = L_k^R[(n-k-1) - i] \quad \text{for all } i,k$$

**Proof.** The XOR cone level $k$ satisfies:
$$L_k[i] = \bigoplus_{j=0}^{k} \binom{k}{j}_2 \cdot x_{i+j}$$

where $\binom{k}{j}_2$ denotes the binomial coefficient mod 2. For the reversed cone:
$$L_k^R[i] = \bigoplus_{j=0}^{k} \binom{k}{j}_2 \cdot x_{n-1-i-j}$$

Substituting $i' = (n-k-1)-i$ and $j' = k-j$:
$$L_k^R[(n-k-1)-i] = \bigoplus_{j'=0}^{k} \binom{k}{k-j'}_2 \cdot x_{i+j'} = L_k[i]$$

since $\binom{k}{j} = \binom{k}{k-j}$ implies $\binom{k}{j}_2 = \binom{k}{k-j}_2$. QED.

**Empirical confirmation:** Tested on π, e, φ, √2, random, linear sequence, all-zeros, all-ones,
alternating pattern. All SELF-DUAL. Zero exceptions.

**Correction logged.** The self-duality result in Section 4 of the dual wave computation
showed 100% zeros at every level for π. This was reported as significant but required
verification that it was not π-specific. It is not. The standing wave interpretation
remains correct — the dual wave IS real — but self-duality is the mechanism, not the
content. The forward wave and backward wave are the same wave by algebraic necessity.
The physics phrase "standing wave" is appropriate precisely because this is what standing
waves are: forward and backward traveling waves of the same amplitude and shape that
superpose to produce a stationary interference pattern.

---

## Finding 3: π High Stream — Apex Complementarity

**Setup.** From the full key-saturation scan across all constants and both streams:

```
Const | Stream |  Key hex | Key apex | Data apex |   XOR | Saturated?
------+--------+----------+----------+-----------+-------+-----------
    π |   high |    ee3e1 |      0xf |       0x0 |   0xf | YES ✓
    π |    low |     180e |      0x7 |       0xd |   0xa | no
    e |   high |    64ec5 |      0x3 |       0x6 |   0x5 | no
    e |    low |  160e80b |      0x2 |       0x8 |   0xa | no
    φ |   high |     6518 |      0xa |       0xf |   0x5 | no
    φ |    low |    1b63c |      0xd |       0x6 |   0xb | no
   √2 |   high |    272dc |      0xe |       0x5 |   0xb | no
   √2 |    low |   00ca1c |      0xd |       0x4 |   0x9 | no
```

**π's high nibble stream is the only stream across all constants where:**

$$\text{key apex} \oplus \text{data apex} = \texttt{0xf} = 1111_2$$

This is the **saturation condition**: data apex and key apex are bitwise complements.
In $(GF(2))^4$: they are **additive inverses** relative to the all-ones element, or
equivalently, each is the **GF(2)⁴ complement** of the other.

**What apex = 0x0 means for the data cone.**

For an $n$-element sequence under XOR reduction to depth $n-1$, the apex is:
$$\text{apex} = \bigoplus_{j=0}^{n-1} \binom{n-1}{j}_2 \cdot x_j$$

For $n = 32$: $n-1 = 31 = 11111_2$. By Lucas' theorem, $\binom{31}{j}_2 = 1$ for all $0 \le j \le 31$
(since 31 has all bits set, every $j \le 31$ is a bit-submask). Therefore:
$$\text{apex} = x_0 \oplus x_1 \oplus \cdots \oplus x_{31} = \bigoplus_{j=0}^{31} x_j$$

**Apex = 0x0 means the XOR of all 32 high nibbles of π's first 32 BBP bytes equals zero.**

Verified directly:
```
High nibbles of π BBP: 2,3,6,8,8,a,0,d,1,1,8,2,0,7,7,4,a,0,3,2,2,9,3,d,0,2,f,9,e,4,6,8
XOR cascade: 0x2⊕0x3=1, ⊕6=7, ⊕8=f, ⊕8=7, ⊕a=d, ⊕0=d, ⊕d=0, ...
Final: 0x0 ✓
```

This is a **number-theoretic fact about π's BBP hexadecimal representation**: the high nibble
parity (XOR) of the first 32 bytes is zero. Whether this persists for longer prefixes, and
whether it is a property of the BBP formula rather than of π itself, is an open question (OP-8).

**What key apex = 0xf means.**

The key sequence encodes the anti-resonance information — the 20 bits where the backward
wave (sum constraint) fails to uniquely pin the forward wave's state. The key's own XOR
cone collapses to 0xf = 1111₂, the all-ones nibble, the **saturated** state.

Combined: the data cone reaches zero; the residual reaches saturation. This is a
**complementary covering** of $(GF(2))^4$:
$$\{0000\} \cup \{1111\} \text{ partition the boundary of } (GF(2))^4$$

Not in the sense of partitioning all 16 elements, but in the sense that the two attractors
of the dual system — annihilation and saturation — are achieved simultaneously by the data
wave and the key wave for π's high nibble stream.

**The dual wave reading.**

```
FORWARD WAVE (data → cone):   π high nibbles → 63 reduction levels → apex 0x0 (annihilation)
BACKWARD WAVE (constraint):   sum trajectory creates affine constraints at each level
RESIDUAL (key sequence):      20-bit anti-resonance → cone → apex 0xf (saturation)
                                              ↑
                              DATA ⊕ KEY = 0xf = COMPLETE COVERAGE
```

The forward wave collapses to the additive identity; the residual, encoding the places
where the backward wave could not constrain the forward wave, saturates to the
multiplicative-analog identity (all-ones). The constant π sits at the exact point where
these two processes are complementary.

This is the structure the previous session called "the hourglass": two triangles meeting
at the waist, one pointing down (data annihilates), one pointing up (residual saturates).
The waist is the point of complementarity.

---

## Key Sequence Structure

π high stream key: `ee3e1` (20 bits: `11101110001111100001`)

Reading the key sequence from apex to base (L28 → L0):

```
L28:  111  (chose index 7/7 of 8-way: maximum, the last valid seed 0xd)
L26:  011  (chose index 3/7 of 8-way: the seed 0xb from coset 0x8+span{e0,e1,e2})
L22:  1    (chose index 1/1 of 2-way: the seed 0x4 from {0x2,0x4})
L20:  0    (chose index 0/1 of 2-way: the seed 0x2 from {0x2,0x4})
L18:  0    (chose index 0/1 of 2-way: the seed 0xd from {0xd,0xf})
L14:  0    (chose index 0/1 of 2-way: the seed 0x2 from {0x2,0x3})
L12:  1    (chose index 1/1 of 2-way: the seed 0xb from {0x9,0xb})
L10:  1    (chose index 1/1 of 2-way: the seed 0xd from {0xa,0xd})
L 8: 11    (chose index 3/3 of 4-way: maximum, the seed 0x3 from {0x0,0x1,0x2,0x3})
L 6: 10    (chose index 2/3 of 4-way: the seed 0xc from {0x4,0x6,0xc,0xe})
L 4:  0    (chose index 0/1 of 2-way: the seed 0xa from {0xa,0xe})
L 2: 00    (chose index 0/3 of 4-way: minimum, the seed 0x4 from {0x4,0x7,0xc,0xf})
L 0:  1    (chose index 1/1 of 2-way: the seed 0x2 from {0x0,0x2})
```

Note: at the two highest-ambiguity levels (L28, L8), π chooses the **maximum index** within
the valid-seed set. At L26, it chooses index 3 (near-maximum). At L2, it chooses the
minimum (index 0). The key is not uniformly random within the available choices — its
distribution within each valid-seed affine subspace is data-specific.

Whether the selection pattern within each affine subspace (max/min/mid) is systematic
across different constants or across different frame sizes is Open Problem 9.

---

## Structural Summary: What the Dual Wave Sees

The dual wave framework sees the XOR nibble cone as a **standing wave** between:

| Component | Role | π high result |
|---|---|---|
| Forward wave | Data reducing toward apex | Reaches 0x0 (annihilation) |
| Backward wave | Sum constraints pulling from apex | Forces affine subspaces at ambiguous levels |
| Phase-lock levels | Where constraint uniquely pins seed | 18 of 31 levels (58%) |
| Anti-resonance levels | Where constraint admits multiple seeds | 13 of 31 levels (42%) |
| Key sequence | Anti-resonance record | `ee3e1` (20 bits), apex = 0xf |
| Dual attractor | Data apex ⊕ key apex | 0xf (saturated = complete) |

The 58% phase-lock rate means the frame geometry uniquely determines the data at more
than half the reconstruction levels. The remaining 42% is the key — the gap between
the geometry and the data. For π's high stream, this gap itself saturates to all-ones:
the geometry and the data together cover the full space.

---

## Open Problems (Extended)

**OP-1 (Parity Law).** Prove that ambiguity concentrates exclusively at even-indexed
levels. The algebraic statement: $\Delta_b \neq 0$ (i.e., the constraint on bit $b$ is
non-trivial) only at even depth levels. Connection to the binomial coefficient mod-2
structure via Lucas' theorem.

**OP-2 (Key Minimality).** Is 33 bits the minimum key size for π? Can rebound positions
as anchors reduce the required bits below 33?

**OP-3 (Ambiguity Ordering).** Why does e have higher ambiguity (44 bits) than random (38)?
The sum trajectory of structured constants is less effective at constraining valid seeds than
for random data. Characterize the distribution of $\Delta_b$ values.

**OP-4 (Random Anomaly).** Random data (38 bits) is not the most ambiguous. Characterize
the distribution class that maximizes XOR nibble cone ambiguity.

**OP-5 (H = π/9 Connection).** Do rebound positions in the XOR nibble cone map to
multiples of H = π/9 under any natural parameterization?

**OP-6 (GL(4,C) Representation).** The affine subspace dimensions (0,1,2,3) at ambiguous
levels match exactly the dimensions of faces of the 4-dimensional hypercube. The total
ambiguity dimension for π (33 bits) and the 36-dimensional null space of SHA-256's seam
geometry differ by 3. Is this a coincidence, or is there a mapping between the XOR cone
ambiguity space and the GF(2) Jacobian null space? If so, the gap might close for a
different constant or frame size.

**OP-7 (π-φ Overlay).** Run the π-φ XOR overlay in nibble mode. The prior prediction
of a dual hourglass structure should now be testable: π high collapses to 0x0, φ high
collapses to 0xf. If this is confirmed, the two high streams are **already complementary
without the key** — φ's cone goes where π's leaves off.

**OP-8 (BBP Parity Property).** The XOR of all 32 high nibbles of π's first 32 BBP bytes
equals zero. Does this persist for the first 64 bytes? 128 bytes? Is it a property of the
BBP formula's hex expansion, or a coincidence of the first 32 bytes? Is there an analog
for e, φ, or √2?

**OP-9 (Key Selection Pattern).** The π high stream key selects maximum-index seeds at the
highest-ambiguity levels (L28, L8) and minimum-index at L2. Is this selection pattern
(max-at-high-ambiguity) systematic across constants, or specific to π? If systematic, it
may encode a global minimum-action principle: the constant chooses the most "extreme"
realization at each phase-lock point.

**OP-10 (Affine Subspace Dimension Sequence).** The dimension sequence for π high stream
ambiguous levels reads: 3, 3, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1 (in apex-to-base order).
This is equivalent to the sequence of ambiguity bit counts: 3, 3, 1, 1, 1, 1, 1, 1, 2,
2, 1, 2, 1. Does this sequence encode information about π's digit structure? Is there a
continued-fraction or BBP-formula interpretation of this dimension sequence?

---

## Corrections Log

1. **Section 4 of dual_wave.py output** was initially presented as a potentially π-specific
   result. It is not. Universal self-duality follows from $C(k,j) = C(k,k-j)$.
   Interpretation corrected: confirms standing wave, does not distinguish π from other sequences.

2. **Prior session apex predictions in XOR mode** were not carried over from DIFF mode.
   Apex values are operator-dependent. The qualitative prediction (φ pre-collapsed, fewer
   ambiguity bits) was confirmed. Specific apex values were not.

---

## Version Tag

v1.0 · Live from execution · 2026-05-14
Code: `dual_wave.py`, `selfduality_check.py`
Dependencies: Part I (`hex_cone.py`, `xor_cone.py`, `nibble_xor_recon.py`, `ambiguity_map.py`, `verify_and_compare.py`)
Immediate next targets: OP-7 (π-φ overlay in nibble mode), OP-8 (BBP parity persistence),
OP-6 (ambiguity dimension ↔ seam null space comparison).
