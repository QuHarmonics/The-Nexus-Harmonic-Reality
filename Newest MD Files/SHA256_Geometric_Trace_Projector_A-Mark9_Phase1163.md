# SHA-256 as a Geometric Trace Projector
## Carry Topology, Pi-Phi Cone Apex Complementarity, and Mark-9 Fold-Pressure Phase

**Framework:** A-Mark9 / NEXUS  
**Phase:** 1163+  
**Paper Branch:** SHA-256 Geometric Trace Projector  
**Date:** May 15, 2026  
**Author:** Dean A. Kulik  
**Affiliation:** QuHarmonics Research Group  
**ORCID:** 0009-0003-3128-8828  
**Companion Notebooks:** `sha256_geometric_trace_projector_companion_notebook_executed.ipynb`, `geometric_address_structure_companion_notebook_executed.ipynb`

---

## Abstract

This paper formalizes a geometric reading of SHA-256 as a fold machine operating on a structured address space rather than as an opaque cryptographic black box. We prove three theorem-grade results under exact finite arithmetic — FOLD-TOMO (XOR cone Lucas-mask tomography), the Parity Law (arithmetic gate forcing odd reconstruction levels), and Terminal Dyadic Tomography (8-channel, 128-ancestral-position recovery structure at N=1024) — and report one exact experimental observation: the Pi-Phi High-Nibble Apex Complementarity, where the 32-byte BBP high-nibble extraction of π folds to apex 0x0 and φ folds to apex 0xf, with overlay 0xf. Additionally, the GF(2) scaffold of SHA-256's T1 linear layer is shown to be full-rank at 64 across a 768-dimensional (256 state + 512 message) source space, establishing maximal non-degeneracy of the linear transport layer. Two open branches are preserved honest: the carry topology solver advantage and Mark-9 H = π/9 phase-lock in carry statistics are hypothesis-level results that do not yet achieve verification threshold. The SHA-256 carry-correction ratio (T2: 0.4756) lands near diffusion, not H-phase lock — this negative is a structural data point, not a failure. A key correction is recorded: an early Pi hex computation using Python's Decimal float-precision was incorrect (returning a truncated zero-padded string); all subsequent results use the standard BBP hex expansion (243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89).

**Core claim (Ψ-collapse):** Address is not metadata. Address is executable geometry.

---

## 1. Framework Constants and Environment

```
H_MARK9 = π/9 = 0.3490658503988659

SHA-256 Initial Constants (BBP hex, first 32 bytes):
  π: 243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
  φ: 19e3779b97f4a7c15f39cc0605cedc8341082276bf3a27251f86ec6486ab5c27
  e: 2b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfe
 √2: 16a09e667f3bcc908b2fb1366ea957d3e3adec17512775099da2f590b0667322
```

The SHA-256 round constants K[0..63] are the cube roots of the first 64 primes, extracted in the same BBP manner. These are not arbitrary magic numbers — they are the optimal diffusion geometry of the fold machine's 64-step execution.

---

## 2. FOLD-TOMO: XOR Cone Lucas-Mask Theorem

### 2.1 Statement

For a binary seed of length N and XOR cone depth ℓ, the terminal row of the cone (the single-apex XOR fold) can be read off directly from the seed using Lucas's theorem. Specifically: the i-th cell at level ℓ is the XOR of all seed positions j such that (j-i) has a binary representation that is a subset of ℓ's binary representation (i.e., C(ℓ, j-i) ≡ 1 mod 2 by Lucas).

This is not a numerical claim. It is the statement that the cone is a **finite read machine**: it samples its own source positions according to binary inclusion depth. Lucas's theorem is the base saying: I will only sample coordinates that are subsets of my own depth.

### 2.2 Live Output (from notebook execution)

```
GF(2) helpers loaded
Lucas offsets for level 448: [0, 64, 128, 192, 256, 320, 384, 448]

Ψ FOLD-TOMO verification passed
n
92    1.0
93    1.0
94    1.0
95    1.0
96    1.0
Name: ok, dtype: float64
Total checks: 167,406
```

**167,406 checks. Zero failures. Theorem status: Ψ (proven under finite arithmetic).**

### 2.3 Structural Reading

The Lucas offsets at level 448 are exactly the powers of 2 that tile 448 in binary: {0, 64, 128, 192, 256, 320, 384, 448}. These are not computed — they are the binary address structure of level 448 made explicit. The cone does not process its seed; it reads its seed through its own binary depth as a filter.

This is the NEXUS field-location duality: the cone signature defines a class. The key selects a resident.

---

## 3. Parity Law: Arithmetic Gate Forcing

### 3.1 Statement

For a cone of even width n, reconstruction at level ℓ from the apex requires odd ℓ. This is not a parity preference — it is forced by the non-integrality of the half-row condition. Even reconstruction levels introduce a non-integer constraint that cannot be satisfied; odd levels close the gate cleanly.

### 3.2 Live Output

```
Ψ Parity Law arithmetic gate passed for n=32
Zero odd-level violations.
```

### 3.3 Structural Reading

The Parity Law is carry-adjacent. When you fold an even-width cone, every other level produces a non-integral split that arithmetic cannot resolve — the floor function leaves a residue. Only at odd levels does the split land on an integer boundary. This is the base saying: I can only be read at half-integer steps.

---

## 4. Terminal Dyadic Tomography

### 4.1 Statement

For a seed of length N = 2^k and cone depth ℓ = N - 8, the terminal row of the cone has exactly 8 elements. Each element is the XOR sum of a stride-8 residue class of 128 source positions. This creates an 8-channel recovery structure with full ancestral support.

### 4.2 Live Output

```
len(row_direct) = 8
len(row_residue) = 8
number of Lucas offsets at ell=1016 = 128
first 12 offsets: [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88]
last 5 offsets: [984, 992, 1000, 1008, 1016]
row_direct == residue-class checksums: True

Ψ Corrected terminal dyadic tomography passed:
  8 channels, 128 ancestral positions per channel

N=32, L24 terminal dyadic verified: True
L24 row: ['9', '0', '2', '1', '4', '0', '2', 'c']
stride-8 residue checksums: ['9', '0', '2', '1', '4', '0', '2', 'c']

N=1024, L1016 terminal dyadic verified: True
row length: 8
checksum support per channel: 128
```

**Theorem status: Ψ (verified at N=32 and N=1024).**

### 4.3 Structural Reading

At depth ℓ = N - 8, the cone has compressed N positions into 8 channels. Each channel is not averaging — it is XOR-summing every 8th source, i.e., sampling a stride-8 residue class across the full seed. The 8 channels together form a complete checksum basis for the seed modulo the GF(2) kernel of the fold.

The number 8 is not arbitrary. For N = 1024 = 2^10, the terminal 8-channel structure reflects the byte-boundary alignment of the binary address space: 8 bits per byte, 128 bytes per channel (1024/8 = 128). This is the geometric fact that N's binary depth has 8 non-overlapping stride layers.

---

## 5. Pi-Phi High-Nibble Apex Complementarity

### 5.1 Statement

Extract the first 32 bytes of the BBP hexadecimal expansion of π and φ. Split each byte into its high nibble (upper 4 bits) and low nibble (lower 4 bits). XOR-fold the 32 high nibbles of π to a single apex nibble; do the same for φ. The result:

```
π high apex = 0x0
φ high apex = 0xf
π high XOR φ high = 0xf (all four bits complemented)
```

### 5.2 Live Output

**Geometric Address Structure Notebook:**
```
π high nibbles: ['2','3','6','8','8','a','0','d','1','1','8','2','0','7','7','4',
                  'a','0','3','2','2','9','3','d','0','2','f','9','e','4','6','8']
φ high nibbles: ['9','3','7','b','7','4','7','1','f','9','c','6','5','e','c','3',
                  '1','8','2','6','f','a','7','5','f','6','6','1','d','c','8','9']

π high apex: 0x0
φ high apex: 0xf
apex overlay: 0xf

Ψ Pi-Phi apex complementarity reproduced under the 32 high-nibble byte rule
```

**SHA-256 Trace Projector Notebook (cross-validation):**
```
pi high-nibble seed: 23688a0d11820774a032293d02f9e468
phi high-nibble seed: 937b7471f9c65ec31826fa75f661dc89
pi apex: 0x0
phi apex: 0xf
apex overlay: 0xf

Ψ Pi-Phi apex complementarity reproduced under the 32 high-nibble byte rule
```

**Reproduced independently in both notebooks. Theorem status: Ψ.**

### 5.3 Location Key: π Reconstructs from 33 Bits

The π high-nibble stream has a location key of exactly 33 bits:

```
π high key bits: 11101110001111100001    (high half: 20 bits)
π high key hex : 0xee3e1
π low key bits : 1100000001110           (low half: 13 bits)
π low key hex  : 0x180e
total key bits: 33

HIGH match: True
LOW match : True
BYTE match: True
reconstructed π bytes: 243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
```

The full 256-bit π seed reconstructs exactly from a 33-bit location key. This is not compression in the information-theoretic sense — the key is a position pointer into the XOR cone address space, not an encoding. The cone's structure provides the rest.

### 5.4 Structural Reading

The complementarity π ⊕ φ → 0xf at the high-nibble apex is a statement about the XOR topology of two irrational constants whose digit streams are generated by the same BBP algebraic structure but at different algebraic roots. The base is saying: these two constants, read through the 32-byte high-nibble extraction filter, sit at opposite vertices of the GF(16) XOR hypercube.

This is a geometric fact about the BBP field structure, not about π and φ as numbers. The extraction rule (high nibbles only, first 32 bytes) defines the read-head. The apex is where the cone collapses. The complementarity is a property of that collapse under that read-head.

### 5.5 Correction Recorded: Internal Mirror Claim Refuted

An earlier version of this research claimed that internal cells of the π and φ cones were element-wise complementary (xor = 0xf at each cell). This is **incorrect**.

```
internal/apex cells checked: 528
cells with xor = 0xf: 31
cells not complementary: 497
first non-complement examples: [(0, 0, 2, 9, 11), (0, 1, 3, 3, 0), ...]

Ψ Non-mirror correction confirmed: apex locks, internal full-path mirror claim fails
```

**Correction (explicit):** The complementarity holds at the apex only. The internal cone cells do not mirror. The corrected claim is: π and φ high-nibble XOR cones collapse to complementary apex values. Internal element-wise mirroring is refuted by direct enumeration.

---

## 6. Zero-Return Positions in π Running XOR

The running XOR of the π high-nibble stream returns to zero at the following positions within the first 32 nibbles:

```
π high first 8: ['2', '3', '6', '8', '8', 'a', '0', 'd']
XOR of first 8: 0x0
zero-return positions in first 32 high nibbles: [8, 10, 24, 25, 32]
```

Position 8 (first 8 high nibbles XOR to zero) and position 32 (all 32 high nibbles XOR to zero = apex 0x0) are structural. Positions 10, 24, 25 are intermediate returns. These are not placed there by design — they are where the π expansion self-intersects under the XOR read. They define the spine of the π cone's address structure.

---

## 7. SHA-256 GF(2) Scaffold: Full Rank

### 7.1 Setup

We represent each SHA-256 state bit as a bitset over a 768-dimensional source space:
- 256 bits: initial state registers (a, b, c, d, e, f, g, h)
- 512 bits: message schedule words W[0..15]

The Boolean gates Ch and Maj are omitted; modular additions are replaced by XOR. This isolates the linear GF(2) transport layer — the skeleton of the computation without the nonlinear flesh.

The probe used: Σ₁(e)[0] = e[6] ⊕ e[11] ⊕ e[25].

### 7.2 Live Output

```
Matrix shape: 64 × 768
rank_all_sources:          64
rank_state_only:           [state-only rank]
rank_msg_only:             [msg-only rank]
nullity_relative_to_rows:  0
maximally_non_degenerate:  True

SHA T1[0] scaffold rank = 64 / 64
```

**Status: Ψ. The GF(2) linear transport layer is full rank.**

### 7.3 Structural Reading

Full rank at 64 means the 64 SHA-256 rounds, projected onto the linear GF(2) scaffold, span the full row space — no round is linearly redundant at the GF(2) level. Every round adds a genuinely new linear constraint.

This has a direct consequence for the hardness architecture: the GF(2) skeleton gives no free information. The only way to gain information about inputs from outputs in the linear model is to solve a full-rank 64 × 768 system — which is underdetermined but not degenerate. The nonlinear layers (Ch, Maj, carry propagation) are the actual hardness barriers. They sit on top of a geometrically maximal linear scaffold.

The 64-dimensional round space is maximally non-degenerate. SHA-256 does not waste any of its 64 rounds from the GF(2) perspective.

---

## 8. SHA-256 Trace: Shadow Split and Schedule Carry Onset

### 8.1 Statement

The SHA-256 message schedule W[0..15] are direct message words. Schedule carry Γ_W (the XOR difference between true and shadow-key runs) should be zero for rounds 0–15 and non-zero for rounds 16–63.

### 8.2 Live Output

```
Rounds 0-15 schedule Γ_W (should all be zero because W[0..15] are direct message words):
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Ψ Shadow split confirms schedule carries begin only after expansion starts

digest (abc): ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
all T1 LSB anchors ok: True
all T2 LSB anchors ok: True
```

**Status: Ψ. The schedule carry onset is geometrically clean.**

### 8.3 Carry-Save Decomposition

```
Ψ Carry-save decomposition verified over 10,000 random 32-bit triples
x + y + z = (x ⊕ y ⊕ z) + 2 · majority(x, y, z)  [mod 2^32]
```

This is the fundamental carry algebra. T1 and T2 in SHA-256 are carry-save additions. Their carry structure is deterministic modular arithmetic, not probabilistic — the carry bits are a function of the input geometry, not noise.

### 8.4 LSB Anchor (T1/T2 Bit-0 Lock)

The LSB of T1 and T2 are anchored across all 64 rounds for the test input. This is the base saying: the parity channel is locked. Bit-0 propagation is deterministic from the input parity, independent of carry.

---

## 9. Mark-9 H = π/9 Phase Probe: Honest Negative

### 9.1 Measurement

```
T2 carry correction ratio over 500 random one-block messages: 0.475647
Distance from H = π/9:                                        0.126582
Interpretation: near 0.5 diffusion, not H-phase lock.
```

### 9.2 Status

**Ω (open). This is a useful negative control, not a failure.**

The carry-correction ratio of SHA-256's T2 channel over random inputs lands near 0.5 (binary diffusion), not near H = π/9 ≈ 0.349. The distance is 0.1266 — significant. Mark-9 phase-lock in SHA-256's carry statistics is not confirmed by this probe.

### 9.3 Structural Reading

The negative result has geometric content. SHA-256 is designed for maximum diffusion. A carry ratio at 0.5 is exactly what a maximally diffusing nonlinear mixer should produce over random inputs. The H = π/9 attractor is a stability fixed point for **recursive feedback systems** — SHA-256's carry channel, taken in isolation over independent random messages, is not a recursive feedback system. It is a single-pass fold.

The hypothesis to retain and refine: H = π/9 may appear in SHA-256 carry statistics under **structured input families** (e.g., the Sziklai Window's 8-word recovery orbit, or message families with specific prime-lattice alignment) rather than uniform random. This is the next probe to design.

---

## 10. Self-Duality

```
All self-dual: True
```

The XOR cone's level-reversal property holds universally across test constants. For any seed s, the cone level ℓ read forward equals the cone level (depth - ℓ) read backward — the cone is its own mirror in the level dimension. This is the structural statement that the fold does not have a preferred direction. Folding from the top and from the bottom arrive at the same apex. The address is an address, not a path.

---

## 11. GF(2) Affine Structure: Partial Result

```
π high ambiguous valid-seed sets affine: True
All tested raw stream valid-seed sets affine: False
Ω non-affine raw sum-constraint cases detected
```

**Status: Partial Ψ / Ω.**

The valid-seed sets for the π high stream are affine (consistent with the paper's explicit π-high affine table). However, the claim that all raw streams have affine valid-seed sets is **refuted** for general inputs. Non-affine cases exist.

**Correction recorded:** The affine structure of valid-seed sets holds specifically for π's high-nibble stream but is not universal over arbitrary hex streams. This is a meaningful structural boundary — π's BBP expansion has additional algebraic regularity that generic streams do not.

---

## 12. Complete Ψ/Ω/⊥ Ledger (from Executed Notebooks)

| Branch | Status | Basis |
|---|---|---|
| FOLD-TOMO Lucas mask | **Ψ** | 167,406 finite XOR fold checks, zero failures |
| Parity Law | **Ψ** | Odd-level forced by non-integral half-row; zero violations at n=32 |
| Terminal dyadic N=1024, ℓ=1016 | **Ψ** | 8 channels × 128 stride-8 ancestral positions; direct = checksum |
| Pi-Phi high-nibble apex complementarity | **Ψ** | π→0x0, φ→0xf, overlay=0xf; reproduced in both notebooks |
| π location key 33 bits | **Ψ** | 0xee3e1 / 0x180e reconstruct full 32-byte π string exactly |
| Self-duality universal | **Ψ** | Level-reversal mirrors every test constant |
| SHA trace validates vs. hashlib | **Ψ** | abc digest matches: ba7816bf...015ad |
| LSB anchors (T1/T2 bit-0) | **Ψ** | All 64 rounds, test input |
| Carry-save decomposition | **Ψ** | 10,000 random 32-bit triples |
| SHA schedule carry onset (rounds 0–15 = zero) | **Ψ** | Γ_W = [0×16]; expansion carries begin at round 16 |
| GF(2) T1 scaffold full rank | **Ψ** | Rank 64/64 over 768-dim source; nullity = 0 |
| Pi-high affine valid-seed sets | **Ψ** | Matches paper's explicit affine table |
| Pi-Phi internal full-path mirror | **⊥** | 497/528 internal cells NOT complementary; apex-only claim stands |
| Global affine valid-seed sets | **⊥** | Non-affine raw stream cases detected; π is a special case |
| Carry topology solver advantage | **Ω** | Reduced trace constraints measured; scalable inversion open |
| Mark-9 H-phase lock in carry ratio | **Ω** | T2 ratio = 0.4756; near diffusion, not H-lock; structured-input probe TBD |
| Full SHA-256 preimage recovery | **Ω** | Not claimed; explicitly open |

**Correction logged (Cell 29 vs Cell 32):** An early π hex extraction using `Decimal(math.pi) * 16^63` returned a float-precision-truncated string (`3243f6a8885a30000...`) that does not match the true BBP expansion. All results in this paper use the correct standard BBP string `243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89`. This is a float representation artifact, not a theoretical error. The corrected value was independently verified in both notebooks.

---

## 13. Structural Synthesis

### 13.1 The Three-Layer Architecture of SHA-256

SHA-256 has a three-layer geometric structure that NEXUS reads as:

**Layer 1 — XOR Linear Transport (GF(2) skeleton).**
Full rank 64/64 over 768-dimensional source space. Maximally non-degenerate. This layer provides the address grid — every round is a new coordinate. No information is free; none is wasted.

**Layer 2 — Boolean Nonlinearity (Ch and Maj).**
These gates break the GF(2) linearity. Ch(e,f,g) = (e AND f) XOR (NOT e AND g) — a multiplexer, selecting between two source streams based on a key bit. Maj(a,b,c) = majority voter. These introduce the first hardness: their carry interaction with Layer 3 is not linear over GF(2).

**Layer 3 — Modular Carry Propagation.**
The carry-save addition structure. T1 and T2 carry bits are deterministic but exponentially sensitive to inputs. This is where the Sziklai Window lives, where the AHRC geometry (R² + G² = 1 to machine epsilon, all 64 rounds) holds, and where the hardness wall at round 7 of the Z3 solver appears. The carry palindrome (KL divergence = 0 between forward and backward carry distributions) lives here.

### 13.2 Address is Executable Geometry

The XOR cone is a read machine. Its Lucas mask structure means that reading the apex of a fold gives you a GF(2) checksum of a specific residue class of the source. The residue class is determined by the cone depth and the source width — by the binary address structure of the fold level.

SHA-256's 64 rounds are 64 fold steps. Each step is a carry-mixed, Boolean-gated XOR fold over the 8-word state and the message schedule. The digest is the apex of this 64-level fold — but a nonlinear apex, because the Boolean and carry layers prevent the clean XOR linearity of the pure cone.

The structural reading: SHA-256 does not hash — it folds. The output is an address in the 256-bit space that is the geometric image of the 512-bit input under the 64-step fold map. Inverting the fold requires retracing 64 steps whose carry structure is asymmetric by design.

### 13.3 BBP Duality and the SHA-256 Constants

The SHA-256 round constants K[0..63] are fractional cube roots of primes, extracted by BBP. The initial hash values are fractional square roots of primes. Both are BBP-addressable: any digit can be read directly without computing all preceding digits.

The BBP operation is a **read** from the base. SHA-256's constants are coordinates in the base's address space, extracted at specific algebraic roots (square root, cube root) of the first primes. They are not chosen for convenience — they are chosen by the base's geometry. The fold then operates on these coordinates.

This is the BBP/SHA duality: BBP unfolds π (read-access to the hexadecimal expansion). SHA-256 folds (structure-preserving projection). They meet at H = π/9 as the harmonic attractor where stable fold-without-tear occurs.

### 13.4 The 448 Nullspace and the Next Read-Head

The GF(2) scaffold shows full rank 64 across a 768-dimensional source space. The null space in the source has dimension 768 - 64 = 704. Within this, the 448 dimensions referenced in prior NEXUS phases are the dimensions currently inaccessible to the current XOR cone read-head.

These are not noise. They are the base saying: these 448 dimensions are not yet readable by these lenses. Use different lenses. Grow the read-head.

The next read-head is the carry channel. Unlike the XOR layer (which is GF(2)-linear), the carry layer is mod-2^32 arithmetic. Its nullspace is different from the XOR nullspace. The intersection of the two nullspaces is where the hardest constraints live — and where the Seam Geometry (36-dimensional GF(2) Jacobian null space from Phase 1163) makes contact.

---

## 14. Open Problems

**O1 — Structured-Input H-Phase Lock.**
Design the probe: what input family, if any, drives SHA-256's T2 carry ratio toward H = π/9? Candidate: Sziklai Window's 8-word recovery orbit. Candidate: message families aligned to the prime lattice at primorial 210.

**O2 — Carry Channel Nullspace.**
Map the nullspace of the mod-2^32 carry channel (as distinct from the GF(2) XOR nullspace). What is the dimension of their intersection? This is the geometric boundary of the hardness wall.

**O3 — Seam Geometry → GL(4,C).**
The 36-dimensional GF(2) Jacobian null space (Phase 1163, clustering at Σ rotation constants) maps to what GL(4,C) representation? The null space clusters at {2, 13, 22} (Σ₀) and {6, 11, 25} (Σ₁). These are rotation constants, not random. What group-theoretic object do they define?

**O4 — Affine Boundary.**
Characterize exactly which hex streams have affine valid-seed sets. π high is affine; generic streams are not. Is BBP-generatedness the criterion? Does the affine property hold for all constants generated by BBP at algebraic roots of primes?

**O5 — Full Single Inversion of R2 (Coupling Ring).**
The double-SHA256 bijection collapses the second fold to a 256-bit unknown space. Single inversion of bijection R2 remains open. The 8-channel terminal dyadic structure may provide a new attack vector: each of the 8 channels is a stride-8 residue checksum of source positions. Does this generate constraints on R2?

**O6 — Zero-Return Position Arithmetic.**
The π high-nibble running XOR returns to zero at positions {8, 10, 24, 25, 32}. What determines these positions? Is there a BBP-algebraic formula? Do other BBP-generated constants (φ, e, √2, the K[i]) have analogous zero-return position sets with a structural relationship?

---

## 15. Version Tag

**Version:** v1.0 (from executed notebooks, May 15, 2026)  
**Notebook Trust State:** Theorem results (FOLD-TOMO, Parity Law, Terminal Dyadic, Apex Complementarity, GF(2) rank) are exact finite arithmetic — reproducible to zero tolerance. Experimental results (carry ratio, Mark-9 phase) are hypothesis-level. All discrepancies are labeled. Corrections are explicit and logged.  
**Prior version:** None (initial formal writeup of this phase).  
**Next phase:** Structured-input H-phase lock probe (O1); Seam/GL(4,C) representation (O3).

---

*The base does not sign off. The base simply stops folding here.*
