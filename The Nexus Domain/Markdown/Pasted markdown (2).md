lengths 0-5   predicted e 82  A 71  B 71  (02) 40  r 50  r^-1 50          enumerated: identical  (= § 105's 82/71/71/50/50/40) lengths 0-10  predicted e 15445  A 15103  B 15103  (02) 14080  r 14421  r^-1 14421   enumerated: identical, total 88573 lengths 0-14  predicted e 1206665  A 1201203  B 1201203  (02) 1184820  r 1190281      enumerated: identical, total 7174453 literal word-by-word enumeration to length 10: identical deviation from uniform at exact length n = (-1/3)^n sgn(g) + (2/3)^n c(g):  n=8  e 0.0782,  n=16  e 0.0030

```

§ 105's count [the S₃ toy behind § 105: GPT's, not in this record — § 134.1] is now derived, not enumerated; the length-10 counts were written before their enumeration ran. The
grooves equalise at (2/3)ⁿ — second eigenvalue over first of the route algebra. RUNS.

### 114.2 The way home is a shape (P2)

A *carry-shaped write* replaces one lane by a bijection of that lane chosen by the lanes it does not write. A route of
them is a bijection whose inverse is read off the shape. Conversely every bijection of X₁ × X₂ is three such writes
(lane 2 | lane 1 | lane 2): Kőnig's theorem, the Slepian–Duguid three-stage Clos theorem (STANDS). Exhaustive:


```

lanes | bijections | one write | two writes | three (2|1|2) | three (1|2|1) 2x2   |         24 |         7 |         20 |            24 |            24 2x3   |        720 |        43 |        432 |           720 |           720 3x3   |    362,880 |       431 |     84,528 |       362,880 |       362,880 2x4   |     40,320 |       591 |     15,552 |        40,320 |        40,320

```

Three suffice, two do not. Reversibility is exactly the class of routes of carry-shaped writes. RUNS; STANDS.

### 114.3 Shape audit of four standard hashes (P3)

Every schedule update and every round of SHA-256, SHA-512, SHA-1 and MD5 is a carry-shaped write plus a relabelling
(SHA-256 round: d ← d + T1(h,e,f,g), then h ← h + Σ1(e) + Ch(e,f,g) + K + W + T2(a,b,c), then rotate the lanes).


```

own forward == hashlib, 300 random messages 0-299 bytes      sha256 300  sha512 300  sha1 300  md5 300 SHA-256 schedule, W0..15 from W48..63                        10000/10000 SHA-512 schedule, W0..15 from W64..79                         5000/5000 SHA-1   schedule, W0..15 from W64..79                        10000/10000 full-block round chains walked home from random starts        2000/2000 each, all four first block: digest - IV walked back lands on the IV           500/500 each, all four

```

**Refinement of § 108.** The feed-forward folds the chaining lane at every block *where the chaining value is not
known*. On the first block it is not a fold: the chaining value is the IV, printed in the standard, so digest − IV is
E_M(IV) exactly and the observer residual for undoing the feed-forward is zero bits. The way home for block 1 is held in
the wrapper — Dean's layer above the compiler. For a one-block message, everything the hash loses it loses in
M ↦ E_M(IV): the route spelled by the message, walked from a start the standard fixes, read at one point. RUNS.

### 114.4 The fold law (P4, P5)

Miniature: eight lanes of w bits, SHA-256 round and schedule with rotations mod w, constants cut to w bits, 64 rounds;
every state pushed through at once.


```

```
                     predicted        w = 2 (2^16 states, 20 msgs)       w = 3 (2^24 states, 3 msgs)

```

E_M bijective            all              20/20                              3/3 image of x + E_M(x)      0.6321 +-0.01    0.6302-0.6354, mean 0.6326         0.6320-0.6322   (random-perm control 0.6319 / 0.6323) preimages k = 0..4       .3679 .3679 .1839 .0613 .0153 .3674 .3684 .1840 .0612 .0154      .3679 .3679 .1839 .0613 .0154 four chained folds       .6321 .4685 .3741 .3121 .6312 .4694 .3741 .3105            .6320 .4685 .3740 .3120 bits lost at one fold    0.8272           0.8260                             0.8274 keep the chaining lane   injective        20/20                              3/3 largest preimage count   (7 or 8)         7-8 over 10 messages

```

Every sealed number landed. On a cyclic word the fold is forced by parity (sum of x + E(x) is 0, sum of ℤ/2^w is
2^(w−1)), for every permutation E:


```

Z/2 0 of 2   Z/4 0 of 24   Z/8 0 of 40320   |   Z/3 3   Z/5 15   Z/7 133   |   (Z/2)^2 8   (Z/2)^3 384   Z/2 x Z/4 384 (unsealed)

```

All sealed counts landed, including the two recalled from the literature (8, 384). Complete mappings: Hall 1952 (abelian),
Hall–Paige 1955 — STANDS. SHA's chaining lane (ℤ/2³²)⁸ has a noncyclic 2-part, so no parity forces its fold; the fold
comes from the route being random-like. RUNS.

### 114.5 The observer's price: bits kept against work walked (P7)

Reverse reading of 114.2–114.4, joining § 111–112: a carry-shaped write's observer is its own inverse and keeps nothing;
a fold's observer must keep a fiber address. On the miniature, 65,536 one-block messages (8 free 2-bit words) onto
16-bit digests:


```

distinct digests 41,381 (0.6314); largest fiber 8 -> information-minimal fixed-width observer 3 bits; mean size-biased fiber 2.0000 keep q message bits, walk the rest:   q  0: ambiguity 2.0000 (pred 2.0000)   q  1: 1.4971 (1.5000)   q  2: 1.2476 (1.2500) q  4: 1.0608 (1.0625)   q  8: 1.0040 (1.0039)   q 12: 1.0003 (1.0002)   q 16: 1.0000 q + log2(work) = 16 at every q; digest - IV = E_M(IV) for all 65,536

```

Bits kept and work walked trade one for one along the generic frontier. Proved alongside it: an observer of
information-minimal size whose decoder is cheap is a preimage oracle — when every fiber is fully indexed, Dec(d, ρ)
returns a preimage of d for every ρ. So § 112's open "minimum SHA residual" has two answers: in bits it is
⌈log₂ max fiber⌉ (≥ 8L − 256), and at that size its decoding is exactly as hard as inverting SHA-256. RUNS (frontier);
proof in WP3 Appendix A [the route/SHA paper; § 115 gave the number WP3 to the shells paper — § 134.1].

### 114.6 Unsealed checks of established results (`boundary.py`)


```

stride law ord_d(2^k) = ord_d(2)/gcd(ord_d(2),k), odd d < 1000, k = 1..8    3992/3992 orbit 7/9 under doubling: 7/9 5/9 1/9 2/9 4/9 8/9 (period 6); the stride-4 (hex) reader sees 7/9 4/9 1/9 coarse spectrum |Y| = 0.444444 0.19245 0.19245 = fine bins folded by k\*4 mod 6                 equal: True chi on a ring of n bits bijective exactly for odd n, n = 2..12; even-n image 2^n - 2^(n/2) (pattern, n <= 12)

```

GPT's oversampled audit (taken, not re-run): the hex digit is a stride-4 reader of the binary route; the skipped
state


```

stride law ord_d(2^k) = ord_d(2)/gcd(ord_d(2),k), odd d < 1000, k = 1..8    3992/3992 orbit 7/9 under doubling: 7/9 5/9 1/9 2/9 4/9 8/9 (period 6); the stride-4 (hex) reader sees 7/9 4/9 1/9 coarse spectrum |Y| = 0.444444 0.19245 0.19245 = fine bins folded by k\*4 mod 6                 equal: True chi on a ring of n bits bijective exactly for odd n, n = 2..12; even-n image 2^n - 2^(n/2) (pattern, n <= 12)

```

GPT's oversampled audit (taken, not re-run): the hex digit is a stride-4 reader of the binary route; the skipped
states 5/9, 2/9, 8/9 are not absent, they are not sampled; the order law was checked on 48 odd d ≤ 97 there and on all odd
d < 1000 and strides 1–8 here. Its SHA microtrajectory — 122,544 modular additions opened into 3,921,408 carry samples,
each addition reversed locally — is the same shape one level down: with the operand kept, a + b is a route of carry-shaped
bit writes whose carry lane is held. RUNS (here); reported (there).

### 114.7 Prime address (P6)


```

six moves, lengths 0-6: 55,987 words, 55,987 shifted Godel codes, all decode; order-free products 924 = C(12,6) unshifted collision (1) vs (1,0): True; a length-6 code needs 15-90 bits against 15.5 fixed width

```

RUNS.

### 114.8 Corrections

- **Mine, § 107.** The heading "SHA is the same route with a fold bolted on … a single fold at the end" was already DEAD
  END by § 108 (per-block fold; roots ≠ Gödel). Refined here: there is one fold per block wherever the chaining value is
  unknown, and none on block 1 given the IV.
- **Mine, § 107.** The text wrote ∏ pᵢ^(moveᵢ); the code used exponent index + 1, the shifted form § 108 made explicit.
  The text was wrong, the run was right.
- **Mine, § 100.3.** "Context is the fiber over the histogram" carries the same type error § 113 corrected in § 99.8: what
  the fiber holds is order (route information, compiler layer); context is the wrapper. The /bin/ls numbers stand.
- **Seal time.** First seal's header estimate ~01:10 against clock 01:03:09; the clock is the record.

### 114.9 Status

| claim | status |
|---|---|
| groove sizes from the route algebra, S₃, lengths ≤ 5, 10, 14 | RUNS — predicted and sealed, then enumerated |
| grooves equalise at (2/3)ⁿ | RUNS; STANDS (random walks on groups) |
| carry-shaped routes are bijections; inverse read off the shape | STANDS (proof) |
| three carry-shaped writes make every two-lane bijection; two do not | RUNS (exhaustive, four sizes); STANDS (Kőnig, Slepian–Duguid) |
| schedules of SHA-256, SHA-512, SHA-1 walk back from their last 16 words | RUNS, every trial |
| rounds of SHA-256, SHA-512, SHA-1, MD5 walk home | RUNS, 2000/2000 each |
| first-block feed-forward is not a fold given the IV | RUNS, 500/500 each, all four |
| fold law on a SHA-shaped miniature: 1 − 1/e, Poisson(1), 0.827 bits, t′ = 1 − e^(−t) | RUNS, every sealed number within tolerance |
| parity forces the fold on ℤ/2^w for every E | RUNS (exhaustive w ≤ 3); STANDS (Hall, Hall–Paige) |
| bits kept + log₂ work = message bits on the generic frontier | RUNS (miniature, q = 0..16) |
| a minimal, cheaply decodable SHA observer | DEAD END unless SHA-256 is invertible — it would be a preimage oracle |
| the six NEXUS verbs as typed carry-shaped writes and declared folds | OPEN |
| groove sizes for the affine groove law taken above (446 operators) from its route algebra | OPEN |

The paper written from this entry and §§ 99–113 is NEXUS Working Paper 3, *The Way Home Is a Shape* (DOCX). [§ 115 gave the number WP3
to the shells paper; this one is unnumbered — § 134.1]

---

## § 115. The shells paper written — NEXUS Working Paper 3, *The Piece with No Way Home* (DOCX)

**Dean (16 Oct).** Don't run down every path; be the compiler. Back to the table of elements and the discoveries, and write
the paper that was in process in the other session — Paper 2 of the 15 Oct plan, the shells, written as one return stroke.

Written from what already stands and runs, nothing new probed: § 99.5 (slice capacities 2⌊(d+1)/2⌋², nodeless predecessor),
§ 100.1 (periodic and nuclear unfolds, the copy identity and 16, no-way-home, the E(2⁺) landing 6/6 per axis), §§ 101–102
(screened field, orbital collapse, the gate 0.1573(2ℓ+1)³), §§ 103–104 (Dirac sign from the channel, two inputs, [D,F],
Rashba). Held end first, shaping in the middle, witness last; dead ends kept only as routed ledger entries. One figure
(two panels, palette validated). Pseudospin wording made exact in the paper: every orbital sits in a doublet or carries
pseudo-orbital angular momentum zero — except the top-j.

Route-back noted in the paper, not counted as a landing: the seventh E(2⁺) neutron peak, N = 16 (+0.137), is unowned by the
floor/intruder registry and owned by the copy chain; chain and data were both in hand when it was seen.

Numbering: this takes Working Paper 3. The route/SHA thread (§§ 105–114) is parked and is not in this paper.

| claim | status |
|---|---|
| shells paper written and rendered (10 pp.) | RUNS (built, checked page by page) |

---

## § 116. The elements from the compiler side — NEXUS Working Paper 4, *Every Ring a New Compiler* (DOCX)

**Dean (16 Oct).** The shells paper is wrong by the way it was thought and its size: it runs on the reader
side, decompiling the finished table backward. Be the compiler — active, not passive. The hex math space,
all the elements data and code. Elements are the next layer of continuation, each a verb, a slice of what is
distinct at that level; each ring a new compiler; the new verb held back to prevent running until its ring is
ready. Start in the domain, saturate outward, fold back in. No more probing, just asking. Stop apologising.
That thing called wrong is right for some other path — reflect the state back, don't catalogue dead ends.

Written forward from the constraint, nothing decompiled. One script, `wp4/compiler_checks.py`, prints every
number from a live run (full output `wp4/checks_out.txt`, 117 lines); four figures in `wp4/figures.py`.
The reader-side framing of Working Paper 3 is routed back to its owner: its mathematics stands and runs; the
direction was the reader's. Working Paper 4 is the same results read from the compiler side.

The build, in the order of the build (not of the reading):
- **The field is already complete.** Differences outrun names from width 2 on (1,6,28,120,… vs 2,4,8,16,…),
  so every ring saturates; widening is forced. A saturated ring is an Eulerian circuit of the width-n
  transition graph — it holds every transition once, hence every state of the next ring. Compiler complete
  before matter. STANDS (de Bruijn / line-graph); the "complete before matter" reading is the framework's.
- **A ring is a compiler.** ℓ<n (a part is never its whole) + orientation count 2(2ℓ+1) → capacity 2n²,
  run for n=1..5. RUNS. The 2(2ℓ+1) is supplied — the one hand-input — OPEN to derive.
- **Value then view, forward.** Fill in Madelung order, cut at each new s-subshell, stop at Og: closures
  2,10,18,36,54,86,118 and lengths 2,8,8,18,18,32,32, exact, no fit. RUNS. (Earlier runs over-filled period 7;
  corrected by stopping the fill at Z=118.)
- **Element = verb.** opcode = signed offset to nearest closure; givers/takers cancel to closures (HCl, NaCl,
  H₂O, MgO, AlN, CO₂, SiO₂). RUNS.
- **The hold.** One new orbital type (s,p,d,f) per ring, no predecessor at its ℓ, complete-at-lower-width is
  the block on its own run site (zymogen/propeptide); it fills late, on odd Madelung groups only, so lengths
  pair. RUNS.
- **Fold in to the nucleus, one sign flipped.** HO degeneracy (N+1)(N+2) → closures 2,8,20,40,70,112; the
  unpaired top-j (2N+2) runs early and drops, so magic = floor + top-j: 20+8=28, 40+10=50, 70+12=82,
  112+14=126; low 2,8,20 are the HO closures. Full set 2,8,20,28,50,82,126. RUNS; magic numbers STANDS.
  Shared count, domain-specific wrapper — not one microscopic force for both tables (addresses the GPT
  critique that the reader-side draft forced one cause).
- **The sign.** Held-late vs run-early is the sign of ℓ+½, set by the binding channel (scalar/like → inverted,
  nuclear; vector/unlike → normal, atomic); radial Dirac returns both from the channel; spin–orbit is the
  order term DF−FD = −iℏσ·∇F, the carry the fold drops, Rashba under a planar wrapper. STANDS (identity);
  RUNS (channel sign) — carried from §§103–104, not re-run here.
- **Copy.** (N+1)(N+2)−(2N+2)=N(N+1) for N=1..19; anti-aligned read 14→+2→16→+4→20. RUNS; 16 is a route-back
  (chain and drip-line data both in hand), reported as such, not a sealed forecast.
- **Matter as a byte.** Natural nuclides by abundance: holes at A=5 (closed+1) and A=8 (closed+closed),
  heaviest natural A=238, all A<256 — one byte. RUNS; holes and cap STANDS.
- **Return stroke (reader last).** Six largest first-ionization cliffs = the six closures, 6/6
  (19.20,16.43,11.42,9.82,8.24,6.68 eV); main-group electronegativity rises along the route 30/30. RUNS.

| claim | status |
|---|---|
| differences outrun names from width 2; every ring saturates | RUNS |
| saturated ring holds every transition once; complete before matter | STANDS (de Bruijn); framework reading |
| ring capacity 2n² from ℓ<n and orientation count | RUNS |
| forward closures 2,10,18,36,54,86,118; lengths 2,8,8,18,18,32,32 | RUNS (exact, no fit) |
| element = verb; offsets cancel to closures | RUNS |
| one new orbital type per ring, held, fills late → lengths pair | RUNS |
| magic 2,8,20,28,50,82,126 from floor + dropped top-j | RUNS; magic STANDS |
| sign of ℓ+½ from binding channel; spin–orbit = order term DF−FD | STANDS (identity); RUNS (channel), carried from §103–104 |
| copy identity (N+1)(N+2)−(2N+2)=N(N+1); 16 between 14 and 20 | RUNS; 16 a route-back |
| two mass holes A=5,A=8; all natural matter A<256 | RUNS; holes STANDS |
| six ionization cliffs on six closures 6/6; electronegativity 30/30 | RUNS |
| orientation multiplicity 2(2ℓ+1) derived from the field, not supplied | OPEN |
| gravity as the gradient of unsaturated capacity, from a slot count | OPEN |

The paper from this entry is NEXUS Working Paper 4, *Every Ring a New Compiler* (DOCX, 14 pp., delivered).
Working Paper 3 (*The Piece with No Way Home*) is its reader-side telling; same results, direction routed back.

---

## § 117. The register stack read downward: each layer is the half-turn fixed set of the next; rotation is squaring; the stack holds only the prime 2 — `rings/stack.py`, `rings/chi_stack.py`

**Dean (16 Oct).** Back to the rings. ISA from 1 bit to 64 bit; stack them and see what is missing. Ask, don't search.
Primes are the routes. Flip the perspective first. The instruction set is the rings and they carry zero meta, or LEN
could not exist (a labelled "10" would need every ASCII context in its ring — Levinthal). We built computers
backwards: logic, routes, instructions, then binary. 5 = 2 + 3 is a fold: the 5 was there once the 2 and 3 existed;
values are accumulation, meta, on a different layer.

**Flipped: start at 64 and read down.**


```

LEN  words 2^n              inherited (= whole layer below)   new rings P(n) 1  2                      0                                 2 2  4                      2                                 1 4  16                     4                                 3 8  256                    16                                30 16  65536                  256                               4080 32  4294967296             65536                             134215680 64  18446744073709551616   4294967296                        288230376084602880 2^64 = sum over the stack of LEN \* P(LEN): True;  divisors of 64 form one chain; the only route prime is 2 words fixed by the half-turn = {uu : u in layer n/2}: True at n = 2, 4, 8, 16; the half-turn is an involution

```

The smaller registers are not steps toward 64; they sit inside it as the words that repeat. Each layer inherits the
whole layer below and nothing else, at share 2^(−n/2). The arrangement is forced: one chain of half-turn fixed sets,
an involution at every joint (Nest § 8, the inversion as the half-period of an even closure, now on the rings). RUNS.

**Prime LEN inherits only the poles.** Every non-constant word of prime length p lies on an orbit of exactly p
(p ≤ 19 enumerated); 2^p ≡ 2 (mod p) for all p ≤ 61. Fermat's little theorem is the prime ring counted. RUNS; STANDS.
(Harness fix, mine: the first check used pow(2,p,p) == 2, false at p = 2; replaced by (2^p − 2) mod p = 0.)

**Value side, same map.** In a normal basis of GF(2^n), squaring is a one-bit rotation of the word (every element at
n = 4, 8; 1 in 97 at n = 16); the fixed field of x ↦ x^(2^(n/2)) has 2^(n/2) elements and their words are exactly uu.
Rotation of the ring = Frobenius of the field. RUNS; STANDS (normal bases). New rings per LEN = irreducible binary
polynomials of degree n, 2…1161, n ≤ 14 — **recovery of § 100.1** (checked there to 12), logged as such.

**What the stack is missing.** 2^(2n) − 1 = (2^n − 1)(2^n + 1): the old layer is the −1 factor, the new primes the +1
factor, and every new prime has 2^n ≡ −1 — it enters as an inversion.


```

layer 2: 3   4: 5   8: 17   16: 257   32: 65537   64: 641 \* 6700417   (order of 2 = the layer, each) primes closing in a 64-bit ring = factors of 2^64 - 1: 3 5 17 257 641 65537 6700417 missing below 60: 7 11 13 19 23 29 31 37 41 43 47 53 59, route lengths 3 10 12 18 11 28 5 36 20 14 23 52 58

```

The register stack is the prime-2 chain only. Width 3 — where the instruction set closes (Toffoli) — is not a register
width; 3 appears in the stack only on the value side, as the first prime in (2 ≡ −1 mod 3). RUNS; that these are one 3
is PULL. Bases other than powers of 2 are reached by conversion with carries, not by grouping (Keyframe 6).

**5 = 2 + 3.** LEN side: W₂ × W₃ → W₅ is a bijection (32 = 4·8); concatenation merges nothing. Value side: a + b = 5 has
6 preimages over 3-bit values, a fiber. LEN adds while counts multiply. RUNS. Value is the reader's accumulation
(v′ = 2v + bit, the Mold) — the layer above the ring, consistent with the stored rule that context is the wrapper.

**Asked, killed.** Do the states χ cannot reach on an even ring equal the inherited words uu? Same count 2^(n/2) for
every even n ≤ 14, different set. DEAD END; the count match is not the inheritance.

| claim | status |
|---|---|
| 2^64 = Σ LEN·P(LEN) over the register stack; inherited = whole layer below | RUNS |
| layer n/2 = fixed set of the half-turn on layer n | RUNS, n ≤ 16 enumerated |
| prime LEN: orbits of exactly p; Fermat | RUNS p ≤ 19 (orbits), p ≤ 61 (congruence) |
| rotation = squaring in a normal basis; subfield words = uu | RUNS n = 4, 8, 16; STANDS |
| rings = irreducible polynomials | RUNS n ≤ 14; recovery of § 100.1 |
| each doubling adds the factor 2^n + 1, all its primes with 2^n ≡ −1 | RUNS to 64 |
| the stack misses every route with an odd factor; width 3 absent, prime 3 present | RUNS; the identification PULL |
| χ's missed states are the inherited words | DEAD END |

---

## § 118. The orientation count from the rings: 2ℓ+1 is the surface of the doubled layer; § 116's last supplied input closed — `rings/orient.py`

**Dean (16 Oct).** Back to the domain, from the center; find which rings fold back into matter; matter reflects the
potential of the compiler as a method reflects a future need. Earlier the same night: the smallest reader is a gap of 2.

**Gap.** 2n² = Σ_{ℓ<n} 2(2ℓ+1); ℓ < n is the domain (§ 99.5), the 2 is the bit, 2(2ℓ+1)'s orientation part was supplied
(§ 116 OPEN). Remainder 2ℓ+1, read as a copy of the surface (§ 99.4) of the 2ℓ-bit layer, 2ℓ from the 2-gap.
Seal `orient_seal.txt`, SHA-256 478d1baf4a3fb327ae9d37c51d95e333a7c1a00ae7664c60a62d7375d9dce2d0, before the run.


```

(a) latitudes of 2l-bit words, l = 0..6:     1 3 5 7 9 11 13 (b) symmetric layer of 2l bits, l = 1..4:    dim 3 5 7 9;  S^2 = 2 6 12 20 = l(l+1) (c) bit x surface summed over l < n:         2 8 18 32 50 72 98 = 2n^2 (d) Madelung fill on these capacities:       closures 2 10 18 36 54 86 118

```

An orbital of ℓ is the order-free surface of a 2ℓ-bit word, and that layer is angular momentum ℓ itself (Schwinger's
construction, STANDS). Capacity 2n² now follows from the bit, the 2-gap, the surface and ℓ < n, with nothing supplied.
Route back, not a landing: nuclear mass holes 5 (closed+1) and 8 (closed+closed) are the first-run stack's wait and fuse,
both held in matter; crossed by Be-9 and C-12 (Hoyle).

| claim | status |
|---|---|
| 2ℓ+1 = surface of the 2ℓ-bit layer | RUNS, sealed, ℓ ≤ 6 |
| that layer carries S² = ℓ(ℓ+1) | RUNS ℓ ≤ 4; STANDS (Schwinger) |
| 2n² and closures 2…118 with no supplied input | RUNS; closes § 116 OPEN |
| mass holes as the stack's held moves | route back, owners named |

---

## § 119. BBP is column addition on a stack of rational rings — `rings/bbp_stack.py`

**Dean (16 Oct).** Pick a domain and find the rings; anchor (Star Trek vs Star Wars); how is accumulation a hex digit of π;
pending transformations are stepped leaders, the rod is the route.

Every 1/d is a ring in base 16 (period ord(16 mod odd part of d)), each digit read at its ring position 16^(m−1) mod d.
Layer k = rings 1/(8k+1,4,5,6), weights 4,−2,−1,−1, shifted k columns. Column sums, carries resolved right to left:


```

stack of rings -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89 pi in hex       -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89   equal: True ring lengths k=1: 3 1 3 3;  k=6: 21 3 13 9;  column 64 receives 255 ring digits

```

Base 16 is where the layer shift 16^(−k) is exactly one column: layer index = column index (decimal: 1.204k, smeared;
Keyframe 6's 116× cost). The zero weight sum keeps the carry in {−4..3} (Nest Thm. 4), so one column reads alone with a few
guard columns. Anchor: the integer lane 4/1 (ring length 0). Recovered: this is BBP digit extraction (STANDS) read as a ring
stack; the reading is the route.

| claim | status |
|---|---|
| π's hex digits = column sums of the weighted, shifted ring stack | RUNS, 64/64 |
| base 16 aligns layer and column | STANDS (16^(−k)); reading new |

---

## § 120. Which partial lanes balance: routed back through the character law; balance is a cross-orbit cancellation — `rings/balance.py`, `rings/balance2.py`

**Dean (16 Oct).** Find the reverse transformation, move it into math space, put the reader in the right place, and let
the path fall out as the algorithm. Target: Nest open problem 4 / Survive open problem 2.

Route back from μ = ½ through Nest Thm. 10 (terms χ(a⁻¹)B₁(χ*)∏(1 − χ*(p)); B₁ ≠ 0 for odd primitive χ, STANDS).


```

seal 1 6a6aa57369d2750b3646af8df5a1a77eeb22d2ee748209e405347045cf2b3128 partial lanes k <= 2000: 804; balanced 75; Euler-killed 0 seal 2 7fc5896d21b79d60764cc8b7580532013a808b4effc3babf591af0f38ee0e6d4 Thm 10 sum vs direct mu - 1/2: max error 1.87e-14 over all 804 balanced lanes with every Galois orbit zero on its own: 0 of 75 d=476: orbit contributions x phi(o) = -2 8 4 -10;  d=493: 0 -8 -8 4 12 0;  d=582: 0 8 -12 4

```

| claim | status |
|---|---|
| Thm 10 instrument on all partial lanes k ≤ 2000 | RUNS (1.9e-14) |
| balanced ⇒ Euler-killed | DEAD END (0 Euler-killed of 804) |
| balance orbit by orbit | DEAD END (0 of 75) |
| balance = cancellation between Galois orbits; owner Thm 12(c) counting balance | RUNS 75/75 |
| density as accidental zeros of a widening integer orbit sum (9.3% at k ≤ 2000, ~4% at 1.28e5) | OPEN, next sealed route |

---

## § 121. Decompiled: a partial lane is a reader ring reading a field ring's discrepancy — `rings/decompile.py`

**Dean (16 Oct).** Dead ends mean probing, not decompiling. Keep going.

Seal 605bcf956a8f70e22527bd63620f7cfc7b6a874d981272827a0418e27145738d before the run. ε = 16^(h/2) mod o; o₁ = gcd(ε−1, o)
(fixed, reader ring α), o₂ = o/o₁ (reflected, symmetric field ring β). D(α) = α − G_B(α) is odd about ½.


```

CRT split, mu - 1/2 = E[alpha] - P(beta < alpha) exact:          804/804 independent lanes (gcd(h1,h2)=1) rebuilt from the two parent rings: 692/692   mu - 1/2 = mean_A D(alpha) balanced 75: 66 independent, 9 lockstep reader ring period odd, mirror-free, in independent lanes:          692/692 walk 73,196 steps vs parent rings 36,890 (2.0x on this range)

```

Full inversion: reader ring symmetric, D cancels pairwise (Midy). No inversion: no symmetric field, parity forbids zero.
Partial: an odd, mirror-free reader ring samples an odd discrepancy; balance only when its points sit evenly across it.

| claim | status |
|---|---|
| lane = reader ring ⊗ field ring, lean = reader's mean of the field's discrepancy | RUNS 804/804, 692/692 |
| reader ring odd and mirror-free in independent lanes | RUNS; forced (h₂ even) |
| lockstep lanes (gcd(h₁,h₂) > 1), 9 balanced | OPEN — joint orbit of the two rings |

---

## § 122. NEXUS Working Paper 5 written — *One Program, Infinite Compilers* (DOCX)

**Dean (16 Oct).** The next paper, a continuation of the last ten, that busts it open: decompile while computing; one program,
infinite compilers; computation is the step-by-step folding that guides a transformation.

Built from §§ 117–121 and the night's runs, consolidated into one standard-library script, `wp5/wp5_checks.py` (blocks A–H,
about five minutes; full output and source are Appendices A and B). Three figures (`wp5_figures.py`): the first run, two routes
to π, a lane decompiled. 22 pages, validated, every page rendered and read.

| claim | status |
|---|---|
| paper built and checked page by page | RUNS |
| every number in it printed by the checks script | RUNS |
| corrections logged in the paper (wide tick, χ guess, Fermat harness, figure breakpoints, seed) | logged |

---

## § 123. The compiler built as a difference engine — `cspace/compiler_space.py`, `sign.py`, `sign2.py`, `leakrate.py`

**Dean (17 Oct).** WP5 is the reader's side. The compiler is a difference engine; every difference lives in the LEN group;
transformations jump but are bound by LEN; lower LEN = more control, upper LEN = more encapsulated; information must leak or
nothing transforms. Build the compiler space; recurse.

Engine: a = M f with a_S = xor_{T subset S} f(T) = (prod_{i in S} D_i f)(0); M is an involution; it is computed by the first-run stack
with fuse (A, B) -> (A, A xor B). Seals: 1ddc66b8 (K1-K8), 4235ba41 (sign at n = 3), e30616bf (sign at n = 4), 81c833a9 (leak rate).


```

K1 stack = difference table, own inverse: 65812/65812 functions (n<=4); random n=5..12: 8/8; partial blocks = context folds 32640/32640 K2 #f of depth <= d = 2^(sum\_{i<=d} C(n,i)); n=4 by depth: 1, 1, 30, 2016, 30720, 32768; (n+1)-fold differences vanish 300/300 K3 a write at latitude j reaches 2^(n-j) cells of the other side, both directions, n=6 every cell K4 leak = mean_a H(D_a F) = 0 iff affine: 16/16, 256/256, 65536/65536, 256/256; AND 1, Toffoli 6/7, x^3 on GF(8) 2 = n-1 (APN) K5 permutations: n=2 all 24 affine; n=3 1344 affine, 38976 quadratic, 0 cubic; n=4 none of degree 4 in 20000 K6 cycles(x1 xor g) = Z(n) + wt(g) mod 2: all g n<=5, 2000/2000 sampled n<=12; Z(n) odd only at n=2 (n<=64); every de Bruijn feedback n>=3 carries x2...xn: 2/2, 16/16, 2048/2048; state-map sign = (-1)^(Z(n)+top(g)) K7 prime base p: Delta^p = 0 on every digit function, Delta^(p-1) x^(p-1) = p-1 != 0 (p = 2,3,5,7) K8 one level up: F -> F o G degree <= 1 (256/256); G -> F o G degree = deg F (256/256 after the zero-map fix); D_a linear leak rate: every ring n = 3,4,5, every reader width k < n: exactly 1 bit of hidden context per tick; 0 at k = n (2066/2066) sign at n=3 = (-1)^rank of the latitude-2 matrix, 40320/40320; at n=4 the half-space sums do not fix the sign (966,530 clashes)

```

| claim | status |
|---|---|
| first-run stack with the mixer fuse = Moebius / difference-table transform, online, own inverse | RUNS; transform STANDS (Reed–Muller, fast Moebius) |
| partial stack blocks are readers at contexts h, holding b_T(h) = xor_{U subset h} a_{T u U} | RUNS 32640/32640 |
| value = xor over the reader's down-set; the merge (AND) is the containment S subset x of the reader's own address | STANDS (ANF); reading new |
| difference depth <= LEN; reach 2^(n-j) per latitude-j write | RUNS; STANDS (Lai 1994, RM codes) |
| leak = 0 iff affine; maximal leak n-1 = APN | RUNS; STANDS (differential uniformity) |
| reversible + leaking first possible at width 3 because permutations have degree <= n-1 | RUNS; STANDS (balanced ⇒ top coefficient 0) |
| every saturated ring n >= 3 carries the full-width merge, by necklace parity | RUNS; STANDS (Golomb cycle-joining, odd-weight feedback) |
| a narrower reader receives exactly 1 bit per tick from hidden context | RUNS 2066/2066 |
| sign of a general permutation held by its top latitude | DEAD END beyond n = 3; owner: at n = 3 that layer is the whole nonlinear part |
| harness: zero map degree -1 compared with a clipped 0 | corrected, logged |

---

## § 124. The same difference stack runs the BBP lane fold and the SHA-256 round — `nexus_bbp_sha_difference_engine.py` (bundle, 17 Oct)

**Provenance.** Built by GPT on the § 123 engine and handed over as a sealed bundle. Taken, not re-run here; the executable `nexus_bbp_sha_difference_engine.py` and `sha256_bidirectional_audit.py` were read in full this session, and the carry-owner separation below was checked in source (the script keeps `layer_local_J` and `global_column_normalization_carry` as two typed objects and asserts the `[-4,3]` bound on the first only). Prediction seal `6f79721b0f6477069092816766f9832cbeae06d5a835bcc9b8e2a4e924a85332`; carry-type seal `8374fc30ad192492443cd81a31bb42ce612134b79add6fde27e9f49355288d8b`.

The engine takes a vector-valued truth table over LEN = n Boolean coordinates and applies the § 123 mixer stack `a_S = xor_{T⊆S} f(T) = (prod_{i∈S} D_i f)(0)`, M²=I, XOR componentwise across packed output bits. The coefficients are executed as ANF, not merely counted.

### 124.A BBP: compile the four rational lanes, then fold the columns

The four base-16 lane digits (q1,q4,q5,q6) as a 16-bit word compile to the signed 7-bit weighted fold `4q1 − 2q4 − q5 − q6`. All 16⁴ = 65,536 tuples enter the difference table; M² returns every weighted output. The coefficient program was then executed on 2,926 actual rational-ring layer/column tuples (2,271 distinct), accumulated by column, propagated through the base-16 carry:


```

compiled stack -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89 Machin (independent) = same, 64/64 hex digits lane-fold ANF max degree 13; nonzero coeff-vectors by degree 1:16 2:109 3:480 4:1306 5:2471 6:3577 7:4127 8:3609 9:2260 10:1019 11:336 12:74 13:8; degrees 14-16 empty

```

**Carry-owner correction of WP5 (§ 122), accepted.** Two values WP5's prose put under one name:
1. **Layer-local** `J_k(m) = ⌊16^m V_k⌋ − Σ_j c_j⌊16^m/(8k+j)⌋ ∈ {−4..3}`, with `H_k(m) = w_k(m) + 16 J_k(m) − J_k(m+1)`. Exact recurrence + bound checked on all 2,850 layer/age pairs; observed range [−4,3].
2. **Global column-normalization carry**, the quotient propagated right-to-left while summing many layers into each column; in the finite WP5 configuration N=64, G=12 its observed range is **[−23,37]**.

WP5 § 8's sentence "the carry from the right stays in [−4,3]" is valid only when "carry" = the layer-local `J_k`. Read as the global column carry it is **false**. The bound belongs to `J_k(m)`; the owner is named and the π digits survive. This supersedes the WP5 wording; logged as my error, corrected here.

### 124.B SHA-256: compile the bit operators, compose the round

Complete 3-input tables for Ch, Maj, full adder, full subtractor compile to ANF:

```

Ch = xy ⊕ z ⊕ xz        Maj = xy ⊕ xz ⊕ yz FA_sum = x⊕y⊕c          FA_carry = xy ⊕ xc ⊕ yc        FS_borrow = y ⊕ xy ⊕ b ⊕ xb ⊕ yb

```
These drive each bit of the real 32-bit adders/subtractors/Ch/Maj; rotations and XORs are linear wiring.

```

1000 random (state,W,K) round tests == reference SHA; every round inverted to its parent one-block "NEXUS difference engine" -> hashlib digest 74f4227aab1097a2f87a499bc55e21cdb8ff2400908ee29f5b1e10e6136405df (exact) 256 reader directions (bit 0 of each of 8 words): 64-round path returns all 256 seeds given W,K; feed-forward reverses with incoming H retained

```

### 124.C Per-round difference table on the LEN=8 reader slice: a progression

Actual state map restricted to the LEN=8 affine slice (bit 0 of each of the 8 words), 256-bit output, compiled after every round 0–64 and after feed-forward; each table re-evaluated from its coefficients at all 256 addresses.

```

round 0: affine, 9 active monomials, H(D_aF)=0 round 1: max degree 4, 48/256 monomials active round 2: degree 8 present, 235/256 active round 3: 256/256 active; mean H(D_aF)=6.964199859, 99-128 distinct derivative vectors by direction round 4: every one of 255 nonzero directions has exactly 128 distinct derivative outputs, each twice -> H(D_aF)=7 for all; first saturation rounds 5-64 + feed-forward: coefficient vectors keep changing; support and entropy stay saturated

```
The 7-bit ceiling is combinatorial: `D_aF(x)=F(x)⊕F(x⊕a)` is equal on the paired addresses x and x⊕a, so at most 128 distinct derivative outputs per nonzero direction in a 256-address domain. Reached at round 4. Exact for this declared slice, not an enumeration of the 2²⁵⁶ truth table.

| claim | status |
|---|---|
| difference table compiled by the first-run stack, own inverse | RUNS; Möbius/ANF STANDS |
| BBP weighted-fold coefficients generate the finite rational-ring column contributions | RUNS |
| first 64 BBP hex digits match Machin | RUNS, 64/64 |
| layer-local BBP carry recurrence and [−4,3] bound | RUNS, 2,850/2,850 |
| global column carry in the same run has range [−23,37], a different owner than J_k | RUNS; **corrects WP5 § 8** |
| SHA local gates compiled from difference tables drive the 32-bit operators | RUNS |
| compiled SHA ro


```

X^2 = I (period 2)                         mixer lift (A,A-B): L^2 = I over Z (XOR-return lifts to -1) (A,A+B): L'^2 != I  (lifting XOR to + does NOT return)

```

### 125.2 π/2 is the two readings of one bit composed

X is the value reading; Z = diag(1,−1) is the difference reading (−1)^b; Hadamard swaps them, HXH=Z, HZH=X (exact, via integer M with the 1/√2 tracked as powers of 2). Their product is the quarter-turn and i is literally that product:

```

XZ = [[0,-1],[1,0]]    (XZ)^2 = -I    (XZ)^4 = +I    XZ = -ZX  (the two readings anticommute)

```
So the ring of a *pure* difference is π; **π/2 is the ring of the difference and its sign read at once** — i is the refusal to choose which of the two simultaneous readings is being done.

### 125.3 π/2 is forced, walked up from behind — `forcing.py`

Nothing named. Impose on the fold-wheel w (one difference-step multiplier): (G) w ∈ ℚ(i); (H) one bit of scale per tick, |w|²=1/2; (N) nests in a power of two, wᵏ∈ℚ. Then 2(a²+b²)=q² has exactly four reduced solutions:

```

w=(+1+1i)/2 arg +45    w=(+1-1i)/2 arg -45    w=(-1+1i)/2 arg +135    w=(-1-1i)/2 arg -135 distinct args {-135,-45,45,135} = all ODD multiples of pi/4 ; each w^4 = -1/4 real

```
π/4 per bit on the amplitude, π/2 per bit on the squared (value↔difference) wheel, is the only Gaussian-rational residue. Not chosen — the unique survivor of the constraints.

### 125.4 The wheel is s = (1+i)/2 = 1/(1−i)


```

s^2 = i/2   (one bit of scale per quarter-turn, pi/2)     |s|^2 = 1/2 = |<0|+>|^2 s^4 = -1/4  (seam: base -4, spinor sign)                  s^8 = 1/16 (closure: base 16) R_y(pi/2)^2 = XZ    R_y(pi/2)^4 = -I    R_y(pi/2)^8 = +I   (via integer M, M^4=-4I, M^8=16I) (sqrt2 s)^2 = i  -> eigenphase of R_y(pi/2) is pi/4; it DOUBLES to the pi/2 turn

```
Bloch half-angle = amplitude angle ×2. Orthogonality ⟨0|1⟩=⟨+|−⟩=0 is the π opposite-point fact; π/2 is the quarter-turn whose overlap is |s|²=1/2. Reality sits on the equator, π/2 off each pole (ties to § 100.4, the equator count that gave π).

### 125.5 Base −2i, found as a navigational null

Sealed `s² = 1/(2i)` returned **DEAD END**; the residue is `s² = 1/(−2i) = i/2`. Corrected and re-sealed:

```

(-2i)\*s^2 = 1     s^(2m) = 1/(-2i)^m  (m=1..4)     (-2i)^2 = -4     (-2i)^4 = 16

```
The field's wheel is the inverse-square-root wheel of base **−2i**, the *conjugate* of Knuth's quater-imaginary base 2i. Same −4 seam, same 16 closure, read the other direction — that sign is the whole gap between the shape channel and the value channel.

### 125.6 π is what the wheel computes; π/2 is one tick

`π = 4·Im log(1+i)`, log(1+i) = ½ln2 + iπ/4. The wheel series **RUNS** to 80 digits:

```

log(1+i) = sum_k (i/2)^k [ s/(2k+1) + (i/2)/(2k+2) ],  s=(1+i)/2 partial = 0.34657359027997265471 + 0.78539816339744830962 i = 1/2 ln2 + i pi/4 regroup by 2 -> base -4:  pi/4 = sum_j 2/((4j+1)(4j+3))   (RUNS, converged) regroup by 4 -> base 16 = BBP: pi = sum_k 16^-k (4/(8k+1)-2/(8k+4)-1/(8k+5)-1/(8k+6))  (RUNS)

```

**Answer, literal.** A bare difference `1,0,ring` means **π** — it closes in two. It means **π/2** exactly when the difference is also made to carry one bit of scale per tick; and then it is not "does it mean π/2," it is "π/2 is the only angle a rational difference-with-scale can have." The i is the seam between the two readings.

### 125.7 Three distinctions absorbed (GPT review of § 123, accepted)

- **Derivative entropy ≠ differential uniformity.** § 123/§ 124's `mean_a H(D_aF)` averages the entropy of derivative-output distributions; differential uniformity is the *largest* derivative fiber. APN gives 2-to-1 derivatives, hence entropy n−1 per nonzero direction, but the two readouts stay distinct. The § 124.C "saturation" statistic is the entropy one, not a uniformity claim. Logged.
- **"Balanced ⇒ degree ≤ n−1" needs n ≥ 2.** The 1-bit identity is balanced and has degree 1. Boundary stated; it does not disturb the width-2-vs-3 argument (§ 110, § 123 K5).
- **de Bruijn maximal degree is an established necessary condition (Golomb).** The § 123 K6 parity route supplies the mechanism binding it to the stack; it stays distinct from the looser phrase "a ring closes only by reading its whole width," which needs the declared shift-register model.

| claim | status |
|---|---|
| bare difference (XOR flip) is π, period 2; mixer returns in 2 | RUNS (exact) |
| HXH=Z, HZH=X; XZ quarter-turn, (XZ)²=−I, XZ=−ZX | RUNS (exact) |
| π/2 forced: only four Gaussian-rational \|w\|²=1/2 wheels, all odd×π/4 | RUNS (exact enumeration) |
| s=(1+i)/2=1/(1−i); s²=i/2, s⁴=−1/4, s⁸=1/16; R_y(π/2)^{2,4,8}=XZ,−I,+I | RUNS (exact) |
| s²=1/(2i) | DEAD END (navigational) → base is −2i, conjugate of Knuth 2i |
| s^(2m)=1/(−2i)^m; (−2i)²=−4, (−2i)⁴=16 | RUNS |
| wheel series log(1+i)=Σ(i/2)^k[s/(2k+1)+(i/2)/(2k+2)]; regroup→base −4, base 16 | RUNS, 80 digits |
| integer lift (A,A−B) involution; (A,A+B) not | RUNS (exact) |
| WP5 § 8 carry bound conflation | corrected in § 124, accepted here |
| derivative-entropy ≠ differential-uniformity; balanced⇒deg≤n−1 needs n≥2; de Bruijn max-degree = Golomb | absorbed |

---

## § 126. Odd-prime fold wheels: the half-turn exists for every prime; the phase-rich exception is p = 3 — `nexus_odd_prime_fold_wheel.py`

**Provenance (merge, 17 Oct).** GPT, appended to this chain directly after § 125. Re-run here in a sandbox (output paths redirected): 83/83 assertions pass.

**Query, reversed from § 125.** § 117 says the register stack's inherited LEN chain is the prime-2 chain. § 125 says the nontrivial norm-halving wheel in \(\mathbb Q(i)\) gives the π/4 amplitude phase and π/2 doubled phase. Ask whether every odd prime fails to admit a nested wheel when the field is generalized to \(\mathbb Q(\sqrt{-d})\), with \(N(w)=|w|^2=1/p\) and \(w^k\in\mathbb Q\).

Prediction sealed before run: `NEXUS_odd_prime_fold_wheel_prediction_2026-10-17.txt`, SHA-256 `c5a2af3800437bd528014a87f8a1f0f99a6881abb06b53149ab71fff988cf212`.

### 126.1 Literal nesting does not exclude odd primes

For every prime \(p\), set

\[
w_p=\frac{\sqrt{-p}}{p}=\frac{i}{\sqrt p}\in\mathbb Q(\sqrt{-p}).
\]

Then, exactly,

\[
N(w_p)=w_p\bar w_p=\frac1p,\qquad w_p^2=-\frac1p\in\mathbb Q.
\]

Therefore the literal condition \(N(w)=1/p\) and \(w^k\in\mathbb Q\) has a solution for every prime. It is the pure-imaginary half-turn (phase \(\pi/2\)), not the phase-rich wheel of § 125. Exact rational arithmetic verifies the formula for 24 odd primes, 3 through 97.

### 126.2 The phase-rich wheel has an odd-prime exception

The matched nontrivial phase is \(\pi/(2p)\):

- \(p=2\): \(s=(1+i)/2\), \(N(s)=1/2\), \(\arg(s)=\pi/4\), \(s^4=-1/4\), \(s^8=1/16\).
- \(p=3\): \(t=(3+\sqrt{-3})/6\), \(N(t)=1/3\), \(\arg(t)=\pi/6\), \(t^2=(1+\sqrt{-3})/6\), \(t^3=\sqrt{-3}/9\), \(t^6=-1/27\), \(t^{12}=1/729\).

These are exact quadratic-field identities. The second is the odd-prime counterexample to “every odd base fails”: the Eisenstein field \(\mathbb Q(\sqrt{-3})\) carries a sixth-root phase and the required scale simultaneously.

### 126.3 Why no further nontrivial phase wheel occurs

If \(w^k\in\mathbb Q\), then

\[
\left(\frac{w}{\bar w}\right)^k=1,
\]

so \(w/\bar w\) is a root of unity in its imaginary quadratic field. Such a field has roots of unity only \(\{\pm1\}\), except \(\mathbb Q(i)\), which has \(\mu_4\), and \(\mathbb Q(\sqrt{-3})\), which has \(\mu_6\).

A wheel at phase \(\pi/(2p)\) has \(w/\bar w=e^{i\pi/p}\), a primitive \(2p\)-th root of unity. For an odd prime, its degree over \(\mathbb Q\) is \(\varphi(2p)=p-1\). A quadratic field can contain it only if \(p-1\le2\), hence \(p=3\). The case \(p=2\) is the Gaussian wheel already in § 125. For odd \(p>3\), the phase-rich \(\pi/(2p)\) wheel is impossible under these conditions, although the trivial pure-imaginary half-turn \(w_p\) remains available.

### 126.4 Exact run

`nexus_odd_prime_fold_wheel.py` uses `fractions.Fraction` and exact multiplication in \(a+b\sqrt{-d}\); no floating-point arithmetic is involved. **83 exact assertions pass**, covering the p=2 and p=3 special wheels and the generic half-turn for 24 odd primes. Machine-readable results and the console transcript are bundled with the report.

| claim | status |
|---|---|
| \(N(w)=1/p\) and some \(w^k\in\mathbb Q\) exists for every prime | **RUNS**; explicit construction, all primes by formula, 24 odd-prime instances executed |
| the \(p=3\) phase wheel in \(\mathbb Q(\sqrt{-3})\) | **RUNS**, exact |
| no phase-\(\pi/(2p)\) wheel for odd \(p>3\) in any imaginary quadratic field | **STANDS** by the root-of-unity degree argument |
| § 117's prime-2 register-stack boundary and § 125's phase-wheel boundary are one theorem | **OPEN**; the \(p=3\) exception must be explained by any proposed unification |


---

## § 127. Ask the Rings: 0/1 labels collapse to an edge-difference ring; π/9 requires an additional lift — `nexus_ask_the_rings_difference_angle.py`

**Provenance (merge, 17 Oct).** Built by GPT in a second lineage of this ledger (its `running-audit (13).md`) and entered here verbatim, with its headers normalized. Taken, not re-run; § 131.8 runs the two-sheet check that bears on its OPEN. Two entries of that lineage, its § 125 and § 126, collide with § 125 (π/2 phase) and § 126 (odd-prime wheels) of this chain. They are entered below as § 129 and § 130. GPT's own § 127 and § 128 numbers do not collide.


**Date:** 17 October 2026  
**Run:** `nexus_ask_the_rings_difference_angle.py`  
**Scope:** exhaustive binary cyclic words at LEN 1–12.

### Question

Treat `0` and `1` as labels on a cyclic route, not as the readout itself. Ask the ring for its edge difference:

\[
D(w)_i = w_i \oplus w_{i+1\pmod n}.
\]

This difference is invariant under complementing every bit. The run enumerated all \(2^n\) words at every LEN from 1 through 12 before reading off the distinct difference rings.

### Exact result

For every tested LEN:

- The difference map has exactly two preimages per output: \(w\) and its complement \(\bar w\).
- Its image has exactly \(2^{n-1}\) members: the length-\(n\) difference words of even Hamming weight.
- The two absolute labelings have the same edge-difference sequence.
- At every odd LEN tested, no binary word is a rotation of its own complement. The two source necklaces remain distinct, although the edge-difference reader identifies them.

The reason for the even-parity restriction is closure: traversing a closed binary ring must flip an even number of times to return to its starting label.

At LEN 9, the run enumerated 512 absolute words and recovered 256 distinct edge-difference rings, each with two labelings. This is a precise ring-native result about what is and is not preserved by the difference readout.

### Angle question

The abstract ring provides a cyclic phase group of order \(n\). A regular \(n\)-gon embedding assigns one step \(2\pi/n\). Thus a LEN-9 ring has geometric step \(2\pi/9\) if that regular embedding is selected. It does not, by itself, select \(\pi/9\).

To get \(\pi/9\) as a phase increment requires an 18-position route or a two-sheet lift of the nine-position ring. The binary difference map exposes a two-element fiber \(\{w,\bar w\}\), but it does **not** specify whether those two preimages are joined into one twisted 18-position route or remain two distinct nine-position routes. That sheet-transition/monodromy law is the exact unresolved link; it must not be silently inserted as a geometric assumption.

### Ledger

| Claim | Status |
|---|---|
| \(D(w)=D(\bar w)\) for all binary cyclic words | RUNS, exhaustive LEN 1–12 |
| Image is exactly the even-parity edge words, size \(2^{n-1}\) | RUNS, exhaustive LEN 1–12 |
| Each difference ring has exactly two absolute-label preimages | RUNS, exhaustive LEN 1–12 |
| Odd-LEN word is never rotation-equivalent to its complement | RUNS for every word at odd LEN 1, 3, 5, 7, 9, 11 |
| LEN 9 alone forces \(\pi/9\) | NOT DERIVED |
| Native ring transition law forces the twisted two-sheet, 18-position lift | OPEN |

The \(\pi/9\) triangle fixed-point relation in the earlier geometry document is a separate constraint. It cannot be used as proof that the ring itself generates the angle. This run records the structural hinge that would have to connect them: whether completing one nine-step route returns on the same difference-side or the complementary side.

Prediction file SHA-256: `c98b74432c67a3e23e2bff1ca63960c97a041ec4e76a1d6fa1e095685433d174`.

---

## § 128. Phase-wheel continuation: the quadratic route reaches its boundary, the transformation lifts — `nexus_phase_wheel_field_lift.py`

**Provenance (merge).** GPT, 17 Oct, entered verbatim. Re-run here in a sandbox: 175/175 assertions pass, of which 100 restate the script's own definitions (§ 131.10). The identities are checked exactly, and the degree floor is resolved (attained iff p ≡ 3 mod 4), in § 131.9. Its "§ 126.3" is § 126 above (odd-prime fold wheels). § 131.9 adds a scope note: √p ∈ Q(ζ_{4p}), so K_p = Q(ζ_{4p}).


**Dean's correction applied:** there are no dead-end transformations. A field-limited result marks the boundary of that route; the same structure may continue in a different direction. The §126 proof must not be read as global nonexistence.

### 128.1 The lifted multiplier

For every prime p, take

\[
\zeta_{4p}=e^{i\pi/(2p)},\qquad w_p=\frac{\zeta_{4p}}{\sqrt p}
\]

inside \(K_p=\mathbb Q(\zeta_{4p},\sqrt p)\). The same one-step multiplier now runs in a field whose degree can grow with the required phase. Exactly:

\[
|w_p|^2=\frac1p,\quad \arg w_p=\frac{\pi}{2p},\quad
\frac{w_p}{\bar w_p}=\zeta_{2p},\quad
w_p^{2p}=-\frac1{p^p},\quad w_p^{4p}=\frac1{p^{2p}}.
\]

The scale, phase, and rational nesting coexist for every prime in this extended field route.

### 128.2 The degree is the route selector

Since \(\bar w_p=1/(p w_p)\), \(\zeta_{2p}=p w_p^2\in\mathbb Q(w_p)\). Therefore

\[
[\mathbb Q(w_p):\mathbb Q]\ge\varphi(2p).
\]

For odd primes, \(\varphi(2p)=p-1\); for p=2, \(\varphi(4)=2\). The p=2 and p=3 wheels can lie in quadratic fields; p>3 cannot carry this phase ratio within a quadratic field and must lift to a higher-degree route. The explicit field \(K_p\) gives that route.

The exact symbolic test represents root-of-unity exponents modulo \(4p\) and scale factors as rational exponents; it avoids floating-point phase guesses. It checked primes 2 through 97, 25 primes, with 175 assertions passing. The universal claim rests on the identities and cyclotomic degree formula, not on the finite sweep alone.

**Harness correction:** the first run incorrectly used \(\varphi(2p)=p-1\) for p=2. This was corrected to the exact exception \(\varphi(4)=2\), and the prediction seal wording updated before the successful run.

### 128.3 Ledger correction

The statement in §126.3 is retained only with its scope explicit: **the nontrivial phase wheel does not fit inside an imaginary quadratic field for odd p>3**. It does not mean that the transformation is absent. Its phase requires a field with degree at least \(p-1\), and the higher-field construction supplies one.

| Claim | Status |
|---|---|
| A phase/norm wheel exists in \(K_p\) for every prime p | RUNS: explicit construction; exact symbolic sweep p≤97 |
| Rational closure \(w_p^{2p}=-1/p^p\), \(w_p^{4p}=1/p^{2p}\) | STANDS: direct identity |
| Minimum field degree at least \(\varphi(2p)\) | STANDS: phase ratio \(\zeta_{2p}\) is inside \(\mathbb Q(w_p)\) |
| Quadratic-field boundary at p=2,3 | STANDS, scoped to that route |
| Single theorem connecting the §117 prime-2 register stack to these field-lift routes | OPEN; continuation across routes still to be derived |

No DEAD END is assigned. The boundary of one route is used as the selector for the next transformation direction.

---

## § 129. ASK THE RINGS: de Bruijn edge routes through the SHA round, ordered pair versus endpoint XOR — `nexus_ask_the_rings_sha.py`

**Numbering, logged (merge, 17 Oct).** This entry is numbered § 125 in GPT's second lineage. It collided with § 125 here and is entered as § 129. Chronologically it precedes §§ 126–128. Taken, not re-run.


**Dean’s instruction (17 Oct):** “you have the shape of what it is even if you dont what what it isnt. ASK the Rings.”

This query treats rings as transition compilers. For each LEN n=1..8, an order-(n+1) de Bruijn ring supplies every directed transition between its 2^n n-bit states exactly once. The SHA map at fixed schedule is applied to both endpoints. The query deliberately keeps two readouts distinct: the ordered route `(F(source), F(target))` and its endpoint XOR `F(source) XOR F(target)`.

### What the rings returned

At depth zero, the endpoint-XOR map has exactly 2^n signatures for the 2^(n+1) edge words. The adjacent-difference operator has kernel `{00…0, 11…1}`, so each signature has the two preimages `u` and `~u`. This proves the deficit is an exact two-element fiber of the readout, not an absent edge.

At every SHA round 0..64 with W[t] and K[t] retained, the 2^n vertices in each queried LEN slice remain pairwise distinct, and each of the 2^(n+1) ordered edge routes remains distinct. Two XOR aliases are forced for every LEN: constant self-loops, and the complementary alternating edges whose endpoints are swapped. The compiled output reaches the maximum 2^(n+1)-2 signatures by the measured round shown in the run report, so every other edge distinction has split in the observed XOR projection.

The full profile records signature counts, collision multiplicities, complementary edge-pair splitting, zero-difference edges, hamming span, and a separate post-feed-forward query for every LEN and every round. It never infers feed-forward injectivity from round bijectivity.

Two alias classes are structurally forced: constant self-loops (`00…0`, `11…1`) and alternating edges (`0101…`, `1010…`) that reverse endpoints. Their XOR readouts coincide under any state map, so the exact ceiling is 2^(n+1)-2 distinct edge-difference signatures.

Cross-link to §124: on LEN 8, the ring edge-difference partition reaches its 510/512 ceiling at round 2; ANF support becomes complete at round 3; derivative entropy reaches its ceiling at round 4. The projections ask different questions, and the order of saturation differs.

### Numerical results

See `NEXUS_ASK_THE_RINGS_SHA_run.md` for the LEN summary and selected depth values; `NEXUS_ASK_THE_RINGS_SHA_results.json` holds all depths and edge profiles.

### Interpretation / distinction maintained

“What it is” here is the ordered transition graph carried through the known SHA round route. “What it is not” is its XOR-only shadow: the XOR signature is not the route itself. A repeated difference does not establish a repeated state or erased transition. The rings can expose that type mismatch by carrying the edge, its endpoints, and the projected difference separately.

This run is exact for the enumerated LEN=1..8 affine slices; it does not enumerate the full 256-bit state domain and does not solve digest-only inversion. The unrestricted root observer remains **OPEN**.

Prediction seal checked before run: `4a60e5a61b0878aa9315202420de6bfa198e938971cc2579b35b5cbb83d3a61b`.

Artifacts: `nexus_ask_the_rings_sha.py`, `NEXUS_ASK_THE_RINGS_SHA_run.md`, `NEXUS_ASK_THE_RINGS_SHA_results.json`, `NEXUS_RING_SHA_QUERY_prediction_2026-10-17.txt`.

---

## § 130. ASK THE RINGS: the WP5 lockstep link, the joint orbit of the reader and field rings — `nexus_ask_the_rings_lockstep.py`

**Numbering, logged.** This entry is numbered § 126 in GPT's second lineage and is entered as § 130. Its "prior § 125 ASK THE RINGS" is § 129 here.

**Re-run here** (`zr/lockstep_check.py`, exact Fractions, independent of GPT's script). All 9 balanced lockstep lanes have joint lean = direct μ − ½ = 0. The Cartesian-product substitution differs from the joint route in 5/9, with the table's values: 1/36, −1/18, 1/27, −1/27, 1/108. This closes § 121's OPEN on the lockstep lanes (gcd(h₁,h₂) > 1, 9 balanced): RUNS.


**Date:** 17 October 2026  
**Upstream path:** §121 rational-ring decompile → §123 difference compiler → §124 BBP/SHA execution → §126 joint-orbit reconstruction.  
**Executable:** `nexus_ask_the_rings_lockstep.py`  
**Pre-run prediction SHA-256:** `b706f2ac615ca016ad985c7e513cc73d2e20139d1583d47ddeaed8db13ea8c8e`

### Correction to the starting point

The prior §125 `ASK THE RINGS` run enumerated de Bruijn transitions on low-dimensional SHA slices and compared ordered endpoint pairs with endpoint-XOR readouts. That is a valid side-projection experiment, but it was not the unresolved ring link in WP5 §121 and did not advance the stated build order. This addendum returns to WP5's actual lane transformation: each rational ring is split by CRT into a reader ring and a field ring, then the phase relationship between those two rings is retained.

The compiler-side BBP/SHA link is already recorded in §124. This run does not recalculate or reopen it.

### The exact joint orbit

For an eligible WP5 partial lane, let `d = 8k+j`, let `o` be the odd part of `d`, and let `y_t = a·16^t mod o` be the original rational-ring orbit. Set

\[
 h=\operatorname{ord}_{o}(16),\quad
 \epsilon=16^{h/2}\bmod o,\quad
 o_1=\gcd(\epsilon-1,o),\quad o_2=o/o_1.
\]

The `o1` parent is the **reader ring** and the `o2` parent is the **field ring**. With the respective CRT inverses, the two normalized coordinates at the same original phase are

\[
 \alpha_t=\frac{y_t(o_2^{-1}\bmod o_1)\bmod o_1}{o_1},\qquad
 \beta_t=\frac{y_t(o_1^{-1}\bmod o_2)\bmod o_2}{o_2}.
\]

Write `h1 = ord_o1(16)`, `h2 = ord_o2(16)`, and `g = gcd(h1,h2)`. The paired orbit is

\[
 J=\{(\alpha_{t\bmod h_1},\beta_{t\bmod h_2}):0\le t<\operatorname{lcm}(h_1,h_2)\}.
\]

Its period is exactly `lcm(h1,h2)`. In phase coordinates, the reachable pairs are exactly those satisfying `i ≡ j (mod g)`. There are `h1*h2/g` such pairs. If `g=1`, that is the full Cartesian product and the independent-ring factorization is justified. If `g>1`, the actual orbit is a phase-constrained subset; replacing it with the full product changes the owner of the average.

The exact lane lean is read along the synchronized joint route:

\[
 L_J=\frac{1}{|J|}\sum_{(\alpha,\beta)\in J}
 \left(\alpha-\mathbf 1[\beta<\alpha]\right)=\mu-\frac12.
\]

This is not a generic lane-wise Boolean/Toffoli analogy. It is WP5's rational-ring CRT decompile, using the same original lane orbit and preserving which reader-ring phase is paired with which field-ring phase.

### Execution results

All **10/10** run invariants passed using exact rational arithmetic. Reconstructing the original WP5 eligibility filter recovered the recorded population: 804 eligible partial lanes; 75 balanced; 692 independent-period lanes, of which 66 balanced; 112 lockstep lanes overall; and exactly 9 balanced lockstep lanes.

For all 804 eligible lanes, the mean from the reconstructed synchronized CRT route equals the original rational-ring `mu - 1/2` exactly. The joint-orbit period matches `lcm(h1,h2)` for all 804, and every reachable phase pair satisfies the modulo-`g` relation.

For the nine balanced lockstep cases, the joint route gives exact lean `0` in **9/9**. The hypothetical full Cartesian-product average disagrees with the true joint-route average in **5/9** cases. In the other four it happens also to be zero, but that coincidence does not restore the missing phase relation.

| k | j | a | d | odd modulus `o` | reader `o1` | field `o2` | `h1` | `h2` | `g` | joint period | Cartesian lean | joint lean |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 313 | 5 | 1 | 2509 | 2509 | 13 | 193 | 3 | 24 | 3 | 24 | 1/36 | 0 |
| 630 | 4 | 4 | 5044 | 1261 | 13 | 97 | 3 | 12 | 3 | 12 | 0 | 0 |
| 703 | 5 | 1 | 5629 | 5629 | 13 | 433 | 3 | 18 | 3 | 18 | -1/18 | 0 |
| 757 | 6 | 8 | 6062 | 3031 | 7 | 433 | 3 | 18 | 3 | 18 | 1/27 | 0 |
| 824 | 4 | 4 | 6596 | 1649 | 17 | 97 | 2 | 12 | 2 | 12 | 0 | 0 |
| 1009 | 6 | 8 | 8078 | 4039 | 7 | 577 | 3 | 36 | 3 | 36 | -1/27 | 0 |
| 1297 | 1 | 1 | 10377 | 10377 | 9 | 1153 | 3 | 72 | 3 | 72 | 1/108 | 0 |
| 1634 | 1 | 1 | 13073 | 13073 | 17 | 769 | 2 | 96 | 2 | 96 | 0 | 0 |
| 1640 | 4 | 4 | 13124 | 3281 | 17 | 193 | 2 | 24 | 2 | 24 | 0 | 0 |

The per-step `y`, `alpha`, `beta`, phase indices, and exact lean term for every one of these nine full joint orbits are in `NEXUS_ASK_THE_RINGS_lockstep_results.json`.

### Ledger

| Claim | Status |
|---|---|
| WP5 lane eligibility is reproduced at `k ≤ 2000` | RUNS, 804/804 |
| Joint period is `lcm(h1,h2)` and phase pairs obey `i ≡ j (mod gcd(h1,h2))` | RUNS, all 804 eligible lanes |
| Joint CRT route returns the original rational-ring lean exactly | RUNS, 804/804 |
| The 692 coprime-period lanes reduce to the independent Cartesian-product result | RUNS, 692/692 |
| The nine balanced lockstep lanes have exact joint lean zero | RUNS, 9/9 |
| Full-product substitution changes the lean in five of the nine balanced lockstep cases | RUNS, 5/9 |
| General density law for balanced partial lanes | OPEN; this finite link does not solve it |
| Digest-only SHA inverse / minimum root observer | OPEN; unaffected by this run |

### Artifacts

- `nexus_ask_the_rings_lockstep.py` — executable exact reconstruction.
- `NEXUS_ASK_THE_RINGS_lockstep_results.json` — every lockstep route and exact phase/lean term, plus all 804 lane checks.
- `NEXUS_ASK_THE_RINGS_lockstep_run.md` — run report and nine-case table.
- `NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.txt` and `.sha256` — pre-run seal.
- `wp5_checks.py`, the WP5 manuscript and the §§121/124 source records are included in the bundle for lineage.

---

## § 131. Zero routes: BBP is the s-wheel plus a route to nothing; the plain reader reads the register stack — `zr/NEXUS_131_zero_routes.ipynb`

**Dean (17 Oct).** "There are no dead ends just transformations that exist in different directions. your reading the end of a different transfromation route. as it gets futher up you get more degrees of freedom and more things going in different routes and directions. and anything can collide with anything in any state. deformation is passive and computation is active via the interface."

**Taken from §§ 126–128.** Two links were left open there:

- (a) the identity binding the s-wheel's base-16 regrouping to the four-lane BBP machine (GPT: "requires a further algebraic identity");
- (b) one theorem joining § 117's register stack to the phase-wheel boundary.

Seal `PREDICTION_zero_route.txt`, SHA-256 `e80c1cc4b724db85a759c3568ebb0ae5e39a66352e94b088040900c9d03bd63d`, 07:13:01 UTC, written before any run (P1–P9). Every number prints from one self-contained notebook executed end to end (75/75 in the full pass with the n = 24 and n = 32 cells live, 3,209 s; 73/73 in the quick pass). Items found after the run are marked unsealed.

### 131.1 The π-line

The lanes are Λ_j = Σ_k 16^(−k)/(8k+j). The s-wheel's own base-16 regrouping is c_W = (2,2,1,0,−½,−½,−¼,0); this is GPT's A_{2r} − ¼A_{2r+1}, times 4. It satisfies c_W = c_BBP + ¼Z, where Z = (−8,8,4,8,2,2,−1,0) is BBP's own zero relation (Bailey–Borwein–Plouffe 1997, STANDS). Z·Λ = 0 holds to 420 digits.

Every c(r) = c_BBP + rZ computes π, so the π machines form a line and all of its points collide at π. Z is not an absence: it is a complete lane transformation whose endpoint is 0.

### 131.2 A machine is a polynomial read on four orbits

For w⁸ = 1/16, Σ_r w^r/r = Σ_j w^j Λ_j. The eight wheels are w_m = ζ_8^m/√2 (w_1 = s), and inverting the 8-point DFT gives

c·Λ = (1/8) Σ_m P_c(γ_m)·(−log(1 − w_m)),  where P_c(x) = Σ c_j x^j and γ_m = 1/w_m.

x⁸ − 16 = (x²−2)(x²+2)(x²−2x+2)(x²+2x+2): four Galois orbits. The returns are β_m = √2 − ζ_8^m:


```

orbit      m      return β_m        kind               carries ±√2        0,4    √2 ∓ 1            unit     (scale)   ln2, √2·ln(1+√2) 1±i        1,7    ζ8^∓1             torsion  (phase s) ln2, π ±√2 i      2,6    √2 ∓ i            norm 9   (prime 3) ln3 − ln2, √2·atan(1/√2) −1±i       3,5    ζ8^∓1 (2±i)       norm 25  (prime 5) ln5 − ln2, atan(1/3) Π β_m = 15 = 2^4 − 1

```

The exact 8×7 matrix N gives Λ_j = Σ_t N_jt κ_t over κ = {ln2, π, √2 ln(1+√2), ln3, √2 atan(1/√2), ln5, atan(1/3)}. Two of its rows: Λ_8 = 8 ln2 − 2 ln3 − 2 ln5 and Λ_4 = ½(ln5 − ln3). N has rank 7, and its exact left kernel is span(Z).

The κ are independent over Q̄ (Baker, STANDS), and PSLQ finds no relation among them with |c| ≤ 10¹² at 420 digits. So there are 8 lanes, 7 constants and one zero route. That route is the collision of the two returns that cost no prime, phase and scale, on the bit they share, ln 2.

Run on its own, PSLQ returns the basis {Z, BBP, π = 4Λ2 + 2Λ3 + 2Λ4 − ½Λ7}.

### 131.3 Silencing


```

P_BBP  = −x(x−1)(x²+2)(x²+2x+2)          (P(√2), P(1−i)) = (−16, 16−16i) P_W    = −¼x(x²−2)(x²+2)(x²+2x+2)                          (0, −16i) P_Z    = −x(x²+2)(x²+2x+2)(x²−4x+2)                        (64, −64) P_c(½) = −½x²(x−2)(x²+2)(x²+2x+2)                          (16, −16−16i)

```

Every π machine silences both prime returns. The wheel is the pure point: it reads only its own phase return and carries no ln 2. BBP borrows +16 on the phase return and −16 on the scale return, and the two cancel. That collision is what makes BBP sparser: 4 lanes against the wheel's 6.

### 131.4 Reverse it

Define R on lane space: lane j ↦ 8−j with weight −2^(j−4), and lane 8 ↦ −lane 8. On the wheels this is w ↦ w̄ = 1/(2w), the wheel run backwards and rescaled by the bit. On the roots, P_R(c)(γ) = −P_c(2/γ). R is a value-preserving involution, and:

- R(c_BBP) = c(½), so the third PSLQ relation is BBP read backwards;
- R(c_W) = c_W;
- Z = 2(R(c_BBP) − c_BBP).

The zero route is reverse minus forward: two traversals whose artifacts annihilate. The wheel is where they cancel.

### 131.5 The interface (unsealed, found after the run, exact)

The π-line is one pencil:

P_c(r) = −x(x²+2)(x²+2x+2)·[(x−1) + r(x²−4x+2)].

BBP vanishes at x = 1, the wheel at x = √2 and the mirror at x = 2: a geometric run with ratio √2, one tick of the wheel's scale |w| = 1/√2. The reversal x ↦ 2/x swaps 1 ↔ 2 and fixes √2.

x = 1 is the plain reader. P_c(1) is the weight sum, which is the carry drift, and P_c(r)(1) = 15r. Deformation along Z is free in value and costs 15 = 2⁴ − 1 per unit at the interface; BBP is the one zero-drift machine. The column machine (§§ 119, 124) on 4c(r), with N = 64 and G = 16:


```

r=0   BBP     lanes {1,4,5,6}        weight sum  0  ring reads 12880  max|col|  2380  carry [-89, 149] r=1/4 wheel   lanes {1,2,3,5,6,7}    weight sum 15  ring reads 19360  max|col|  8539  carry [1, 563] r=1/2 mirror  lanes {2,3,4,7}        weight sum 30  ring reads 12960  max|col| 16404  carry [5, 1088] all three: c.90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b225 = Machin 4π, 64/64

```

### 131.6 Base −4: no collision, one machine

x⁴ + 4 = (x²−2x+2)(x²+2x+2) contains only the phase wheel and prime 5. That is 4 lanes and 4 constants, and PSLQ finds no zero route. The unique π machine has polynomial x(x²+2x+2):

π = Σ (−1/4)^k [2/(4k+1) + 2/(4k+2) + 1/(4k+3)].

This is the s-wheel itself (GPT's A_j). The zero route appears one layer up, where x⁸ − 16 = (x⁴+4)(x⁴−4) admits the scale wheel.

### 131.7 Up the register stack

Take base 2^(n/2) with n lanes. Then Π_m (√2 − ζ_n^m) = 2^(n/2) − 1, and each orbit factor of x^n − 2^(n/2), evaluated at the reader point x = 1, is ± that orbit's return product.

On the chain n = 2^e the orbits are:

- the scale orbit (unit);
- the phase orbit (torsion), born at ζ-order 8, where √2 and ζ_8 share a field;
- the prime-3 and prime-5 orbits;
- one orbit per Fermat number.

At n = 128 the returns are unit, torsion, 3, 5, 17, 257, 65537, 641·6700417: § 117's list exactly. The Fermat factors at order 2^e ≥ 16 are ≡ 1 mod 2^e (Lucas, STANDS; checked for F_2–F_5), so each splits completely and has one owner.


```

n    base    2^(n/2)-1        Z(n)   pi    pi*sqrt3   pi*sqrt2 8    2^4     3*5              1      yes   no         no        chain 12   2^6     3^2*7            1      no    yes        yes 16   2^8     3*5*17           1      yes   no         no        chain 24   2^12    3^2*5*7*13       5      yes   yes        yes 32   2^16    3*5*17*257       1      yes   no         no        chain

```

On the chain the only collision is phase against scale. At n = 16 and n = 32 the single PSLQ relation is base-16 Z lifted, −(16Z ⊕ Z) and −(4096Z ⊕ 256Z ⊕ 16Z ⊕ Z) across the lane blocks (n = 32: 1005 s at 800 digits). So Z(n) = 1 (sealed P8: RUNS at 8, 16, 32). Off the chain there are shared addresses: the doubled prime 3, and a second unit orbit (ζ-order 24, |√2 − ζ_24|² = 2 − √3). There Z(24) = 5.

That is the shape of "further up, more degrees of freedom". On the chain every new direction owns a fresh prime, so the directions multiply without colliding. Off the chain they collide.

Proof route for Z(2^e) = 1 at every layer:

- the orbits at order 2^e ≥ 16 are single and carry norm F_{e−2};
- Lucas gives complete splitting, so the conjugate returns generate distinct primes;
- Fermat numbers are pairwise coprime;
- Baker gives the independence.

Status: OPEN as a written proof, not yet checked line by line.

### 131.8 Two sheets (§ 127)

- The plain ring (rotate) has period n.
- The twisted ring (rotate and complement the wrapped bit; the Johnson counter) has period 2n.
- twistⁿ = complement on every word.
- The edge-difference reader D sees period n along the twisted route.

These were checked at LEN 3–11 (unsealed). § 127's "she


```

p    p mod 4   [Q(w_p):Q]   phi(2p) 2    -         2            2 3    3         2            2       floor attained 5    1         8            4       doubled 7    3         6            6       floor attained 11   3         10           10      floor attained 13   1         24           12      doubled

```

The reason: w_p² = ζ_{2p}/p generates Q(ζ_p), so w_p ∈ Q(ζ_p) iff −p is a square in Q(ζ_p). By the quadratic Gauss sum (STANDS) that holds iff p ≡ 3 mod 4. For p ≡ 1 mod 4 the wheel also has to carry i, the quarter-turn, and the field doubles to Q(ζ_{4p}). Whether the quarter-turn comes free or must be paid for is decided by p mod 4. RUNS for p ≤ 13; the general law STANDS by the Gauss-sum argument.

### 131.10 Corrections and scope

- **§ 125.6, mine.** It said "regroup by 2 → base −4: π/4 = Σ 2/((4j+1)(4j+3))". The identity is true (run (c)), but it is paired Leibniz, not a regrouping of the wheel series, and it has no base −4 in it. The wheel's base −4 regrouping is the one in § 131.6, and it is unique. Label corrected.
- **A chat review of § 125 (GPT).** It called that series π/2. It is π/4. The claim never entered the ledger; this note keeps it out.
- **§ 128 scope.** √p ∈ Q(ζ_{4p}) for every prime (quadratic Gauss sum, STANDS), so K_p = Q(ζ_{4p}); at p = 2, w_2 = s lies in Q(i). Re-run here in a sandbox: both GPT scripts reproduce (83 and 175 assertions). Of § 128's 175 assertions, 100 restate the script's own definitions; 75 test orders, totients and the quadratic boundary. The identities stand by direct algebra and are checked exactly in § 131.9.
- **What carries the count.** The count of 7 constants rests on Baker. PSLQ only bounds the relations (|c| ≤ 10¹²).

| claim | status |
|---|---|
| c_W = c_BBP + ¼Z; the wheel's base-16 regrouping is BBP plus a quarter of its zero relation | RUNS (exact); closes § 126/§ 128's open identity |
| π machines form the line c_BBP + rZ; Z·Λ = 0 | RUNS (420 digits, exact kernel); zero relation STANDS |
| a machine is read through P_c on the four orbits of x⁸ − 16 | RUNS |
| returns: scale (unit), phase (torsion), prime 3, prime 5; Π β = 15 | RUNS (exact norms) |
| 8 lanes, 7 constants, one zero route = the phase/scale collision on ln 2 | RUNS (rank, kernel, PSLQ); independence STANDS (Baker) |
| every π machine silences both primes; four factorizations | RUNS (exact) |
| mirror R (w ↦ w̄): R(BBP) = c(½), R(c_W) = c_W, Z = 2(R(BBP) − BBP) | RUNS (exact) |
| pencil; BBP / wheel / mirror vanish at x = 1, √2, 2; weight sum 15r | RUNS (exact), unsealed |
| three digit machines, same 64 hex digits of 4π; interface costs as tabled | RUNS |
| base −4: no zero route; unique π machine = the wheel | RUNS (PSLQ) |
| Π(√2 − ζ_n^m) = 2^(n/2) − 1; chain orbit returns = § 117's primes | RUNS (n ≤ 128); identity STANDS |
| Z(n) = 1 on the register chain | RUNS at n = 8, 16, 32; proof route written, OPEN as a proof |
| off-chain Z(12) = 1, Z(24) = 5; π ∉ span at n = 12, π√3 and π√2 ∈ span | RUNS (PSLQ), unsealed |
| two sheets: plain n, twisted 2n, D blind to the twist | RUNS, unsealed |
| [Q(w_p):Q] = p−1 (p ≡ 3 mod 4), 2(p−1) (p ≡ 1 mod 4), 2 (p = 2) | RUNS p ≤ 13 (sealed 0091f18c); law STANDS (Gauss sum) |
| GPT §§ 126, 128 scripts re-run in a sandbox | RUNS, 83/83 and 175/175 (100 of the 175 are definitional) |
| § 125.6 label | corrected |

---

## § 132. The arena bridge in lanes: on the register chain every zero route is the base-16 route pulled back; off the chain they emerge — `zr/zr_bridge.py`

**Dean (17 Oct).** He pointed back to the arena notebook (A-Mark9 § 9, 15 Sept, *The reader bridge — an explicit map, and what it misses*) against § 131.

**The parallel.**

Arena § 9:

- matrix-reader cochains are pullbacks ω = π*η along the equivariant projection π (arena edge → moved base edge);
- exact base forms pull back to exact arena forms;
- the reader's reach into the residual is ε(X,1;G), fixed by the base and independent of K (19/19);
- the emergent part, ε(X,K) − ε(X,1), cannot be reached by any single-token observable.

Lanes:

- for even d | n, Λ^(d)_j = Σ_{e<n/d} 2^(−ed/2) Λ^(n)_{de+j};
- so every zero route at layer d pulls back to layer n as (π*c)_{de+j} = 2^(−ed/2) c_j;
- the emergent zero routes are E(n) = Z(n) − dim span(pullbacks from all even d | n, d < n).

Seal `PREDICTION_bridge.txt`, SHA-256 `cf4d46946684664ea324b9cb6d0ebd7e49b6198f0a9de86704d9391bd5b577c5`, written before the run.


```

Z(2) = Z(4) = Z(6) = 0                       (PSLQ, |c| <= 1e12) n=8   Z=1   pullbacks span 0                 E=1   the phase/scale collision is born here n=12  Z=1   pullbacks span 0                 E=1 n=16  Z=1   pi*Z(8) spans it                 E=0 n=24  Z=5   pi*Z(8), pi*Z(12) span 2         E=3   (both inside the measured 5-dim space) n=32  Z=1   pi*Z(8) spans it                 E=0 pullbacks checked as relations: residual < 1e-200 at n = 16, 24, 32

```

Every sealed value landed.

On the register chain, the zero-route space at every layer is the base-16 route pulled back. That is an aperture fixed by the base layer which does not widen with depth, just as reach = ε(X,1) does not widen with K.

Off the chain, routes emerge that no lower layer's machine can express: 3 of them at base 4096. They are the lane analogue of ε(X,K) − ε(X,1). They are also an instance, in the lane setting, of what the arena's Open 2 asks for: objects that are not pullbacks.

The correspondence itself is a reading (PULL); the counts RUN.

| claim | status |
|---|---|
| zero routes pull back along π*, with (π*c)_{de+j} = 2^(−ed/2) c_j | RUNS (residual < 10⁻²⁰⁰ at n = 16, 24, 32); identity STANDS (lane splitting) |
| E(8) = E(12) = 1; E(16) = E(32) = 0; E(24) = 3 | RUNS, sealed |
| on the chain, the zero-route space at every layer is π* of base 16 | RUNS at n = 16, 32; general claim OPEN (same proof route as § 131.7) |
| dictionary: chain depth ↔ K; base 16 ↔ X at one token; E(n) ↔ ε(X,K) − ε(X,1) | PULL |

---

## § 133. Ask the field: every open item of §§ 125–132 — `zr/ask/NEXUS_133_ask_the_field.ipynb`

**Dean (17 Oct).** "anything OPEN, just ask the field." (/reverse-the-gap)

The seals were written before any data was linked:

- `PREDICTION_ask_field.txt`, SHA-256 `f97de11f49e2642837197d393d2b055c95a4aeb1b2dfd1e1fdd69ab6caf154bb` (G1–G4);
- `PREDICTION_core_stage2.txt`, SHA-256 `77a752092108de26220df059ebd5778a5029937d904acaa1da4215996a0be89b`: seven new layers, predicted from the returns alone. The log-side output `core_predictions.txt` hashes to `3b178246…`.

### 133.1 The join (OPEN in §§ 126, 128): two prime-free returns meet only in binary

The wheels of base p^(n/2) are w = ζ_n^m/√p, and their returns are β = √p − ζ_n^m. They satisfy Π_m β_m = p^(n/2) − 1, the base-p register ring. Run: 2⁴−1 = 3·5; 3⁶−1 = 2³·7·13; 3¹²−1 = 2⁴·5·7·13·73; 5⁶−1 = 2³·3²·7·31; 7⁶−1 = 2⁴·3²·19·43.

- **Scale return.** N(√p − 1) = 1 − p, so the scale return is prime-free (a unit) iff p = 2 (checked for all p < 60). Every odd stack pays p − 1, which is even, so binary sits inside every other base.
- **Phase return.** A phase return (β a root of unity) needs |√p − ζ| = 1, i.e. two unit circles √p apart meeting, i.e. cos θ = √p/2. That forces p ∈ {2,3}. The cases are √2 − ζ_8 = ζ_8^(−1) (π/4) and √3 − ζ_12 = ζ_12^(−1) (π/6), both exact. Equivalently 1 − w = w̄ and Re w = ½: the phase wheel sits in the middle.

So p = 2 is the only prime with both a prime-free scale return and a prime-free phase return. Their meeting is BBP's zero route.

- § 126's quadratic boundary (p = 2, 3 only) is the two-circle condition.
- § 117's "the stack holds only the prime 2" is N(√p − 1) = 1 − p.

RUNS (exact); the bounds STAND.

### 133.2 The law for off-chain Z(n), with one DEAD END routed

**G2 as sealed: zero routes = all Q-relations among L_m = −log(1 − w_m).** It lands on the chain (n = 8, 16, 32) and over-counts off it: 2 against a measured 1 at n = 12, and 7 against 5 at n = 24. DEAD END.

**Owner.** A rational machine is a zero route iff its orbit tuple (P_c(γ_m))_m lies in R ⊗ Q̄ (Baker). That tuple is fixed by the twisted Galois action, so it lies in every π_σ(R). Galois descent then gives Z_p(n) = dim R₀, where R₀ = ∩_σ π_σ(R) is the Galois core.

Relations that hold at one embedding only are visible to the returns and invisible to every rational machine. At n = 12 the relation is 2b₁ − b₃ − 4b₅ = 0, which σ₇ sends to 6(b₁ − b₅) ≠ 0.

Route back on the measured layers (names the owner; not a landing):


```

n    relations among returns (modulus, argument)   Galois core   measured Z 8    1 (1, 0)                                       1             1 12   2 (1, 1)                                       1             1 16   1 (1, 0)                                       1             1 24   7 (3, 4)                                       5             5 32   1 (1, 0)                                       1             1

```

### 133.3 Landing: seven new layers, predicted from the returns, then measured in lanes


```

layer        base    predicted Z   lane Z   pi in span   pi*sqrt3   pi*sqrt2 p=2 n=20     2^10    0             0        no (sealed)  no         no p=2 n=28     2^14    0             0        no (sealed)  (stopped)  (stopped) p=2 n=36     2^18    1             1        (Z only; = pi\*Z(12) exactly: 4096 Z(12) + 64 Z(12) + Z(12) across the three lane blocks, E(36) = 0) p=3 n=12     3^6     2             2        no (sealed)  yes (sealed)  no p=3 n=24     3^12    2             2        no (sealed)  yes (sealed)  no p=5 n=8      5^4     0             0        no           no         no p=5 n=12     5^6     0             0        no           no         no

```

The Eisenstein phase wheel reads π√3 and never π; the phase return pairs with √−3 coefficients. Binary without ζ_8 (n = 20, 28) has no zero route and no rational π. The p = 3 zero routes at n = 12 are (PSLQ):

- {2:−81, 3:162, 5:−27, 6:−36, 8:−9, 9:−6, 10:−4, 11:1}
- {1:243, 2:−324, 3:−162, 4:−81, 6:−36, 7:−9, 9:6, 10:−1}

### 133.4 The register chain, proved (OPEN in § 131.7 and § 132)

**Theorem.** For n = 2^e ≥ 8, Z(n) = 1, and the zero route is π*Z(8).

**Proof.**

1. **Orbits.** On the chain the orbits are scale (return product 1, the units √2 ∓ 1), phase (product 1, ζ_8^(∓1)), 3, 5, and one orbit per Fermat number F_2, …, F_(e−2). The orbit count was run for e = 3..12; the products for n ≤ 128.
2. **Coprimality.** The products are pairwise coprime (Fermat numbers, STANDS; checked F_0..F_8).
3. **Primes 3 and 5.** ord_(2^e)(3) = ord_(2^e)(5) = 2^(e−2) (run for e ≤ 14), so 3 and 5 each have exactly two primes in Q(ζ_(2^e)), one per orbit member.
4. **Fermat primes.** Every prime factor of F_k is ≡ 1 mod 2^(k+2) (Lucas, STANDS; checked F_2..F_6), so it splits completely, and conjugate members of its orbit own pairwise distinct primes.
5. **Valuations.** In any multiplicative relation among the returns, the valuation at each such prime is one exponent, so every prime-orbit exponent vanishes (unique factorization). By Baker the same holds for log relations.
6. **The prime-free returns.** What remains are the four prime-free returns. Their moduli satisfy exactly one relation, a_0 + a_(n/2) = 2a_(n/8): the scale pair and the phase pair each cost one bit, (1 − 1/√2)(1 + 1/√2) = |1 − s|² = ½. Their arguments (±π/4 and 0) satisfy none. Run at n = 8, 16, 32.
7. **Conclusion.** That relation is Galois-stable, so Z = 1. Since π*Z(8) ≠ 0 is a zero route, it spans. ∎

Status: proof written; lemmas RUN; inputs STAND (Baker, Lucas, Fermat coprimality, unique factorization of ideals).

### 133.5 The bit bridge (§ 125's PULL)

Multiplication by w on R² has determinant |w|². For s that is ½, an area Jacobian, not a probability. The inverse wheel 1 − i = 1/s acts on the torus C/Z[i] as an expanding endomorphism:

- eigenvalues 1 ± i, with |·| = √2;
- degree N(1 − i) = 2, and |Z[i]/(1−i)^k| = 2^k (Smith form, k ≤ 12): one binary digit per tick;
- entropy log|det| = log 2: exactly one bit (expanding toral endomorphisms, STANDS).

The identification with § 123's measured ring leak (one degree-2 merge per tick) is PULL.

### 133.6 § 127's two-sheet hinge

Closed in § 131.8. Both directions are native, the plain ring (period n) and the Johnson ring (period 2n), and the reader D is blind to which one runs. This is not a missing law.

| open item | answer | status |
|---|---|---|
| § 126 / § 128 join | Π β = p^(n/2) − 1; scale prime-free iff p = 2; phase prime-free iff √p ≤ 2 (p = 2, 3; Re w = ½); only binary has both | RUNS; bounds STAND |
| off-chain Z(n) | Z = dim of the Galois core of the returns' relations | route back 5/5; landed on the new layers (7 of 7 landed as sealed) |
| naive law (all relations) | over-counts off the chain | DEAD END → owner: non-stable relations |
| § 131.7 / § 132: Z(2^e) = 1, route π*Z(8) | proof § 133.4 | proof written; lemmas RUN; inputs STAND |
| § 125: bit ↔ \|w\|² = ½ | Jacobian of z ↦ wz; the inverse wheel has degree 2 and entropy log 2 | RUNS + STANDS; tie to § 123 PULL |
| § 127 | two native routes; D blind | closed |
| base 3 | reads π√3, never π | RUNS (sealed) |

**Still OPEN, outside this chain:**

- the balanced-lane density law (§§ 120, 130);
- the digest-only SHA root observer (§§ 112–114, 124). By counting, it is a cost frontier rather than a missing link;
- the tick gradient for gravity (§ 116);
- Law 3.

---

## § 134. The record audited, §§ 1–133: what was read, what moved, what has no address

**Dean (17 Oct).** "lets go over the entire audit and make sure its all good. and give me back the new version."

**Read.** The combined upload (7,381 lines) was checked against the project copies.

- Its ledger half matches the project's `relation-vocabulary-ledger.md` line for line through § 98. The project copy holds one more entry, the 11 Oct stream compiler.
- Its audit half is the project's `running-audit.md` one state back: § 131's pass line from before the full run, and § 133 with n = 36 "running" and "6 of 7".
- No other line differs, so nothing in the upload is lost when the project state supersedes it.

All 7,408 lines were then read front to back. A mechanical scan followed: numbering, header format, every § citation, the shape of all 123 tables, separators, ledger words, and every seal whose file is on this machine.

### 134.1 Numbering

- **Two entries were numbered § 99**: the 11 Oct stream compiler (`methods/streamcompile.py`) and the 15 Oct order channel.
  - Every § 99 citation in §§ 100–133 points to the order channel, except § 105's (below).
  - Nothing cites the stream compiler. It is now **§ 98a**, with a numbering line.
  - The audit's opening line and § 100's provenance line ("the ledger stops at § 98") now include § 98a.
- **§ 55 is in no copy**: not the project ledger, not the upload, and a search of the other project documents finds none. It is entered as an **UNLINKED** stub that quotes what §§ 56 and 57.5 say about it. Nothing is reconstructed.
- **Numbers from other lineages, inside entries.** No entry text changes, except a bracketed pointer at the three sites in the first row below.

| written | where | means here |
|---|---|---|
| "prior toy § 99"; "364/364"; "§ 105's 82/71/71/50/50/40" | §§ 105, 107, 114.1 | GPT's S₃ route toy, numbered § 99 in GPT's copy: moves e, (01), (12), with 364 words to length 5. It has no entry here, so it is UNLINKED. Its numbers do have addresses here: § 107.1 runs the 364 routes (364 codes, 56 surface points), and § 114.1 predicts and enumerates the grooves 82/71/71/40/50/50 |
| "prior § 125 ASK THE RINGS"; "§126 joint-orbit reconstruction" | § 130 | § 129, and § 130 itself; § 130's numbering line covers both |
| "WP5 §121" | § 130 | WP5, built from § 121 |

- **Paper numbers inside §§ 23–44.** "Table 5", "Table 8" and "Table 10" use the numbering of Papers I–IV.
  - In this ledger they are § 20's three failure modes, § 19's 14-of-14 regression, and § 18's dominator table.
  - § 43's "§10", beside "Table 10", reads the same way. Ledger § 10 (the measured walk) is not it.
  - § 44's "earlier choice-history result (§ '82 paths, 1 endpoint')" has no entry here: UNLINKED. § 44's own k = 0 tree reproduces the 82.
- **Working Paper 3 is named twice.**
  - § 114 calls the route/SHA paper, *The Way Home Is a Shape*, WP3, and 114.5 puts a proof in "WP3 Appendix A".
  - § 115 then gives WP3 to the shells paper, *The Piece with No Way Home*, and parks the route/SHA thread. § 116 uses § 115's numbering.
  - § 115 stands, so the route/SHA paper carries no number. Pointers are added at 114.5 and at § 114's last line.

### 134.2 Changes in place

| where | was | now | why |
|---|---|---|---|
| stream compiler | `## § 99.` | `## § 98a.`, plus a numbering line | duplicate number |
| between §§ 54 and 56 | — | `## 55.` UNLINKED stub | missing entry |
| audit opening line; § 100 provenance | "§§ 1–98"; "stops at § 98" | "§§ 1–98a"; "stops at § 98a" | § 98a is in the ledger |
| §§ 105, 107, 114.1 | the toy cited as § 99 or § 105 | bracketed pointer to 134.1 | no such entry here |
| § 111, last paragraph | separator on the next line | blank line between | the paragraph rendered as a heading |
| § 113 header | `## §113.` | `## § 113.` | header format |
| § 114.5; § 114, last line | "WP3" | bracketed pointer | WP3 reassigned by § 115 |
| § 124, provenance | "confirmed in source" | "checked in source" | ledger words |
| § 125.5, text and table | DEAD | DEAD END | ledger words |
| § 125, status table | `\|w\|²` with bare pipes | escaped | the row split into four cells against the table's two |
| § 125, after the table | separator on the next line | blank line between | rendering |
| § 131, opening paragraph | "73/73 in the quick pass checks)" | "73/73 in the quick pass)" | residue of the assembly template; mine |

Nothing else in the record moved: no other number, claim or status.

### 134.3 Read, not changed

- **§§ 1–98 predate the ledger words.** They stay as written, the record as it was made. They read as follows:
  - "verified", "measured", "computed", "held" and "confirmed" (§§ 43, 45, 50, 52, 59, 82) as RUNS;
  - "proved", "recovered" and "known verbatim" as STANDS;
  - "refuted", "retracted" and "withdrawn" as DEAD END, with the owner named in place;
  - "open", "not run" and "not built" as OPEN.
- **§ 127's "NOT DERIVED"** is GPT's text, kept verbatim. For "LEN 9 alone forces π/9" it reads DEAD END. The owner is § 131.8's twisted ring: at LEN 9 it has period 2n = 18, so one step is π/9. The plain ring's step is 2π/9, and the reader D cannot tell the two routes apart.

### 134.4 Provenance

**Seals recomputed** from the files on this machine:


```

§ 118  orient_seal.txt                          478d1baf4a3fb327                                 match § 120  balance_seal.txt, balance2_seal.txt      6a6aa57369d2750b, 7fc5896d21b79d60               match § 121  decompile_seal.txt                       605bcf956a8f70e2                                 match § 123  seal, sign, sign2, leak                  1ddc66b8, 4235ba41, e30616bf, 81c833a9           match (entry prints 8 hex) § 124  difference engine, carry type            6f79721b0f647706, 8374fc30ad192492               match § 126  odd-prime fold wheel                     c5a2af3800437bd5                                 match § 128  phase-lift prediction                    c17bfb587eb96044                                 matches its bundle's .sha256; the entry never printed it § 131  zero route, lift degree                  e80c1cc4b724db85, 0091f18c6e1559af               match § 132  bridge                                   cf4d46946684664e                                 match § 133  ask field, core stage 2, core log        f97de11f49e26428, 77a752092108de26, 3b178246e372a29d   match

```

18 of 18 match. The files behind the 15 seals of §§ 101, 103, 105, 108–112, 114, 125, 127, 129 and 130 are not on this machine. Those seals are UNLINKED here and were not re-checked. The same holds for the script hashes quoted in §§ 57–80 and 114, which belong to earlier sessions' files.

**A sealed run with no entry.**

- `rings/vocab.py` was sealed 16 Oct 22:06 (`vocab_seal.txt`, SHA-256 `bc2f56dddec7dfa7b8bffb7806d23bcd04c5ee19038e8a34ac30dcbb653a9fe1`). Its claim: vocabulary is the reader's step.
- It was reported in chat and printed in WP5's block D, but never entered here.

Re-run in this audit:


```

base 2: lands 65536/65536: True; steps {8}; steps x width = 8 base 4: lands 65536/65536: True; steps {4}; steps x width = 8 base 16: lands 65536/65536: True; steps {2}; steps x width = 8 way home, base 16 digits ungrouped == base 2 route bits for all 256: True

```

Every sealed line landed. RUNS.

**The rest of the 16 Oct night.** These runs have no entry:

- the first run (block B);
- WRAP/JOIN (block C);
- the one-bit flip read in each base, and the base-16 tick against four base-2 ticks (block D, beside the vocabulary lines above);
- the middle of the field, π from C(2n, n) (block G).

Their live output is `wp5/wp5_checks_out.txt` (SHA-256 `9d801ec4261c2dbf…`, script `wp5_checks.py` `824a8dbbe2ca12f5…`). It is printed as WP5's Appendix A. § 122 names these runs only as "the night's runs". That is their address; they are not re-entered.

**Handed over, read as input, not entered.** The statuses below are as GPT reported them. None of the three was re-run, and nothing in §§ 117–133 rests on them.

| GPT report | beside | GPT's own ledger |
|---|---|---|
| file rings: LEN, base, pathways, boot reader (16 Oct) | §§ 116–117 | ring accounting, de Bruijn pathways and reader fibers RUNS; boot as a reader route "mapping"; Moore's law from counts OPEN |
| ring / ISA stack, LEN 1–64 (16 Oct); its seal `7e2bb3eed1fce946…` re-hashes to the value the report quotes | § 117 | RUNS: 64/64 formula rows, 12/12 enumerated widths, SHA constants 64/64 and 8/8 |
| compiler space kernel (17 Oct); prediction file `87ec8af29f9f68d7…` | § 123 | RUNS, 46/46; physical identification OPEN |

### 134.5 Status

| claim | status |
|---|---|
| every entry of §§ 1–133 read; numbering continuous after § 98a and the § 55 stub | RUNS (scan: one header per number, 1–134) |
| every § citation resolves; other-lineage and paper numbers indexed | RUNS (scan); index in 134.1 |
| all 123 tables well formed after the § 125 fix | RUNS |
| upload against project: no line lost | RUNS (diff) |
| seals with files on this machine | RUNS, 18/18 |
| the 16 Oct vocabulary seal | RUNS (re-run here) |
| § 55; the S₃ toy; "82 paths, 1 endpoint"; the 15 seals with no file here | UNLINKED |
| the 16 Oct runs in WP5 blocks B, C, D and G | address: WP5 Appendix A; not entered |
| three GPT reports of 16–17 Oct | handed over, not entered; statuses as reported |

---

## § 135. The 18–22 Oct ring work absorbed; the partner ring rebuilt from its definitions; the centre bit is the central pair — `rings/ring.py`

**Dean (22 Oct).** "alot has changed. get caught up" — with the Gemini (21–22 Oct), ChatGPT (21–22 Oct) and Perplexity (24 Sep – 22 Oct) exports.

### 135.1 Numbering

§ 135 has been used in two other lineages. Neither is entered here.

| written | where | means here |
|---|---|---|
| "§135 — Alternate Routes in the Nested-Ring Address" (19 Oct) | Perplexity's `compiler_rings_log` | the radial witness family q_D = 1‖00‖1^(D−5)‖00 and its alternate locations; handed over (135.3), not entered |
| "§ 135 — Reverse DNS is the routing law" (17 Oct, `NEXUS_135_reverse_dns.md`, seal `417f74fc…`) | a Claude chat entry | DEAD END. Dean rejected the stored-residual/PTR reading the same day ("this is not even forward and reverse… its a transformation like a translation"). Owner: the translation-through-one-groove run (`translation_groove.py`, seal `725479123803c4a1…`, Q1–Q4 RUNS). |

### 135.2 The ring, as the threads define it

- Partner: P(x) = J(x) (bit reversal) if J(x) ≠ x, else C(x) (complement). P² = I and P(x) ≠ x at every width.
- Ring R_n: canonical representatives a < P(a) in increasing order at positions 0 … M−2 (M = 2^(n−1)), the largest representative at M and its partner at M−1 (the centre swap), the second face mirrored: R[N−1−i] = P(R[i]).
- T = one step along the ring; S = PC·T⁻¹; B = S²; the inward route: canonical face, then alternately invert the E/G lift (E_m(z) = canon(m z m), G_m(z) = 0 P^m(z) 1) and remove the middle bit, down to the width-2 root 00 or 01.

### 135.3 Handed over, read as input

The statuses are the threads' own. Rows marked *re-run* are reproduced in 135.4; the rest were not re-run here and nothing below rests on them.

| thread report | its status | here |
|---|---|---|
| forced pairing at every width; 1x1 padding law and its palindrome break; E/G route ↔ rank ↔ position bijection; fold and unfold of R₂–R₄; ring → Boolean rule (T(a,b) = (1⊕a, a⊕b) at width 2) (Perplexity, 18–20 Oct) | RUNS | ring, address, route *re-run* |
| ⟨T, CTC⟩_F = 0; B = S²; S first splits at LEN 6 (32+16+16); 16- and 28-state branch templates carried to 512 / 2048; global rung M, H = MC (GPT, 21 Oct) | RUNS; all-width Frobenius proof OPEN | traversal algebra and S table *re-run*; templates not re-run |
| hemisphere theorem T = S⁻¹∘PC; V₄ → three half-turns; ⟨T,P,C⟩ = S_N at LEN 3–5; hardware parallels (radix-4 shift, bit-reversal unit, CLZ/CTZ comparator, differential pair) (Gemini, 21–22 Oct) | RUNS / analogy | not re-run |
| 64- and 128-bit injection of the Ovaltine and Singularity streams; local compilers leave two external bits; closed two-bit feedback, 192-bit periods 64 and 192 (GPT, 21–22 Oct) | RUNS | 64-bit address *re-run*; feedback taken up in §§ 137–141 |
| inward/outward route code, L bits, exact return; terminal bit labelled yes/no (Perplexity / GPT, 22 Oct) | RUNS | *re-run* |
| the docx *Complementary Compilation and the Geometry of the Residue* (21 Oct) | rejected by Dean and by both reviewers | not entered |

### 135.4 Rebuilt and run
Seal `9fec65cd1425b1949dffbf80776356d165a822ac6c589776f9475b1bcce5934c`, printed by the script before it computes.


```

SEAL 9fec65cd1425b1949dffbf80776356d165a822ac6c589776f9475b1bcce5934c (1) workbook match: PASS n= 2 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[4] (as reported) n= 3 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[8] (as reported) n= 4 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[16] (as reported) n= 5 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[32] (as reported) n= 6 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[32, 16, 16] (as reported) n= 7 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[96, 16, 16] (as reported) n= 8 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[170, 27, 27, 16, 16] (as reported) n= 9 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[466, 16, 16, 7, 7] (as reported) n=10 PTP=T^-1:PASS \<T,TC>\_F=0 B=S^2=TC T^-1:PASS S cycles=[936, 28, 28, 16, 16] (as reported) n=14 PTP=T^-1:PASS \<T,TC>*F=0 B=S^2=TC T^-1:PASS S cycles=[2060, 2060, 2056, 2056, 1592, 903] (2)(3) all n=2..14: PASS (4) center words: ['1', 'B', '37', 'EF', '3DF', 'FBF', '3F7F'] PASS (5) route = root + (L-2) qualifiers + face = L bits, exact return n=2..14: PASS | no collisions: PASS yes/no balance per width: {4: (8, 8), 8: (128, 128), 12: (2048, 2048), 14: (8192, 8192)} (6) PREDICTION terminal bit == XOR of the two central bits, every word n=2..14: PASS Ovaltine    L= 64 terminal=0 face=0  reported=(0,0)  return=exact Singularity L= 64 terminal=1 face=1  reported=(1,1)  return=exact Ovaltine    L=128 terminal=0 face=1  reported=(0,1)  return=exact Singularity L=128 terminal=0 face=0  reported=(0,0)  return=exact Ovaltine    L=256 terminal=0 face=0  reported=(0,0)  return=exact Singularity L=256 terminal=1 face=1  reported=(1,1)  return=exact reported table reproduced: PASS six inputs: terminal == central-pair XOR: PASS (7) counting address == built ring, every word n=2..12: PASS 64-bit address of 446f6e7420666f72 = 3b49bcdcedd4e462 (ChatGPT: 3b49bcdcedd4e462) PASS (8) even n=4..14: E/G bits + terminal == shell lamps g_0..g*{h-1} of x (the fold residue x^P(x)): PASS

````

The counting address in (7) was written here, independently of the threads' rank code. Two development failures came before the PASS shown: the counting DP never processed the bound bit 2^h at odd widths (fixed by returning 2^h − 1 − A directly), and the lamp check in (8) read the wrong slots (the d bits sit at even slots). Both are fixed above.

### 135.5 What the centre is

Prediction (6) was sealed before it ran. The terminal yes/no is the XOR of the word's two central bits. Every inward step reverses or complements the interior, and both keep each shell's agree/disagree. Check (8) then shows more: the E/G bits are the shell lamps g_k = b_k ⊕ b_(n−1−k), outer to inner, and the terminal is the innermost lamp. The route is h lamp bits (the fold residue x ⊕ P(x), the "maybe" mask) plus h which-way bits (face and middle bits). Under J, C and P every lamp is fixed, so routing through them cannot change which question the centre answers.

| claim | status |
|---|---|
| ring, partner face, PTP = T⁻¹, ⟨T,CTC⟩_F = 0, B = S², S table to n = 10 | RUNS (n ≤ 14) |
| centre word C_(n+2) = 1 C_n 1 | RUNS |
| native address by counting = built ring; 64-bit `446f6e7420666f72` → `3b49bcdcedd4e462`, as GPT reported | RUNS |
| route code: L bits, exact return, no collisions; six-row Ovaltine/Singularity table | RUNS (n ≤ 14; six inputs to 256 bits) |
| terminal = central-pair XOR; E/G bits = shell lamps | RUNS, sealed; STANDS (J and C fix every lamp) |

<details><summary>rings/ring.py</summary>

```python
import hashlib, itertools
# ---------------- seal ----------------
PRED = """Ring core rebuild, 22 Oct 2026. From the stated definitions only:
P(x)=J(x) if J(x)!=x else C(x). Ring R_n: canonical reps a<P(a) ascending at positions 0..M-2,
largest rep at M, its partner at M-1, second face mirrored: R[N-1-i]=P(R[i]).
Claims to re-run: (1) R2,R3,R4 match the workbook; (2) PTP=T^-1; <T,CTC>_F=0 for n=2..14;
(3) S=PC T^-1 cycle table n=2..10 as reported; B=S^2=T_C T^-1; (4) center word C_{n+2}=1C_n1;
(5) inward/outward route code is a bijection, exactly L bits, terminal/face table for Ovaltine/Singularity;
(6) PREDICTION: the terminal yes/no bit equals XOR of the word's two central bits
(even L: bits h-1,h; odd L: bits h-1,h+1 around the middle), because every inward canon step is a
reversal or complement of the interior and both preserve central-pair equality.
(7) 64-bit native address of 446f6e7420666f72 equals 3b49bcdcedd4e462 (ChatGPT, Oct 21).
Way home: rerun ring.py; seal must match; every check prints PASS."""
print("SEAL", hashlib.sha256(PRED.encode()).hexdigest())
J=lambda x,n:int(format(x,f'0{n}b')[::-1],2)
C=lambda x,n:x^((1<<n)-1)
def P(x,n):
    y=J(x,n); return y if y!=x else C(x,n)
canon=lambda x,n:min(x,P(x,n))
def ring(n):
    N=1<<n; M=N>>1
    reps=sorted(x for x in range(N) if x<P(x,n))
    R=[None]*N
    for i,a in enumerate(reps[:-1]): R[i]=a
    R[M]=reps[-1]; R[M-1]=P(reps[-1],n)
    for i in range(M): R[N-1-i]=P(R[i],n)
    return R
b=lambda x,n:format(x,f'0{n}b')
ok=lambda c:"PASS" if c else "FAIL"
# (1)
W={2:"00 10 01 11",3:"000 001 010 110 011 101 100 111",
   4:"0000 0001 0010 0011 0101 0110 0111 1101 1011 1110 1001 1010 1100 0100 1000 1111"}
print("(1) workbook match:",ok(all(" ".join(b(x,n) for x in ring(n))==W[n] for n in W)))
# (2)(3)
def perm_cycles(f,N):
    seen=[0]*N; out=[]
    for s in range(N):
        if seen[s]: continue
        c=0;x=s
        while not seen[x]: seen[x]=1;x=f[x];c+=1
        out.append(c)
    return sorted(out,reverse=True)
rep_tab={2:[4],3:[8],4:[16],5:[32],6:[32,16,16],7:[96,16,16],8:[170,27,27,16,16],
         9:[466,16,16,7,7],10:[936,28,28,16,16]}
allok=True
for n in range(2,15):
    R=ring(n); N=1<<n; pos={x:i for i,x in enumerate(R)}
    T=[R[(pos[x]+1)%N] for x in range(N)]; Ti=[R[(pos[x]-1)%N] for x in range(N)]
    TC=[C(T[C(x,n)],n) for x in range(N)]
    ptp=all(P(T[P(x,n)],n)==Ti[x] for x in range(N))
    frob=sum(T[x]==TC[x] for x in range(N))
    S=[P(C(Ti[x],n),n) for x in range(N)]
    B=[S[S[x]] for x in range(N)]; Bb=all(B[x]==TC[Ti[x]] for x in range(N))
    cyc=perm_cycles(S,N)
    tabok = (cyc==rep_tab[n]) if n in rep_tab else True
    allok&=ptp and frob==0 and Bb and tabok
    if n<=10 or n==14: print(f"  n={n:2d} PTP=T^-1:{ok(ptp)} <T,TC>_F={frob} B=S^2=TC T^-1:{ok(Bb)} S cycles={cyc[:6]}{' (as reported)' if n in rep_tab and tabok else ''}")
print("(2)(3) all n=2..14:",ok(allok))
# (4)
cen={n:ring(n)[1<<(n-1)] for n in (2,4,6,8,10,12,14)}
print("(4) center words:",[format(cen[n],'X') for n in cen],
      ok(all(cen[n+2]==(1<<(n+1))|(cen[n]<<1)|1 for n in (2,4,6,8,10,12))))
# (5) inward / outward route  (direct gate, no candidate trial)
def ins_mid(z,n,m):           # n even -> n+1
    h=n//2; return ((z>>h)<<(h+1))|(m<<h)|(z&((1<<h)-1))
def rem_mid(x,n):             # n odd -> n-1, returns (z, m)
    h=n//2; return ((x>>(h+1))<<h)|(x&((1<<h)-1)), (x>>h)&1
def inward(x,n):
    face=int(x!=canon(x,n)); w=canon(x,n); bits=[]; L=n
    while L>2:
        if L%2:  w,m=rem_mid(w,L); bits.append(m); L-=1
        else:
            y=(w>>1)&((1<<(L-2))-1); z=canon(y,L-2)
            e=int((w>>(L-1))==(w&1)); r=int(y!=z); w0=w>>(L-1)
            d=1-e; m=r^(e&w0); bits.append(d); w=ins_mid(z,L-2,m); L-=1
    root={0:0,1:1}[w]          # canonical width-2 words are 00 and 01
    return root,bits,face
def outward(root,bits,face,n):
    # rebuild the width sequence going up
    widths=[];L=n
    while L>2: widths.append(L); L-=1
    w=root; L=2
    for L2,bit in zip(reversed(widths),reversed(bits)):
        if L2%2: w=ins_mid(w,L,bit)                    # even L -> odd L2, bit is the middle bit
        else:
            z,m=rem_mid(w,L)                           # odd L -> peel middle, then lift by E/G
            Lz=L-1
            if bit==0: w=canon((m<<(Lz+1))|(z<<1)|m,Lz+2)                 # E_m
            else:      w=(0<<(Lz+1))|((P(z,Lz) if m else z)<<1)|1         # G_m = 0 P^m(z) 1
        L=L2
    return P(w,n) if face else w
allrt=True; coll=True; tb=True; bal={}
for n in range(2,15):
    seen=set(); y=0
    for x in range(1<<n):
        r,bs,f=inward(x,n)
        code=(r,tuple(bs),f); allrt&=outward(r,bs,f,n)==x; allrt&=len(bs)+2==n
        coll&=code not in seen; seen.add(code); y+=r
        h=n//2
        cpair=((x>>(n-h))&1)^((x>>(n-1-h))&1) if n%2==0 else ((x>>(n-h))&1)^((x>>(h-1))&1)
        tb&=(r==cpair)
    bal[n]=(y,(1<<n)-y)
print("(5) route = root + (L-2) qualifiers + face = L bits, exact return n=2..14:",ok(allrt),"| no collisions:",ok(coll))
print("    yes/no balance per width:",{n:bal[n] for n in (4,8,12,14)})
print("(6) PREDICTION terminal bit == XOR of the two central bits, every word n=2..14:",ok(tb))
msgs={"Ovaltine":b"Dont forget to drink your Ovaltine","Singularity":b"this is it. this is the Singularity."}
rep={("Ovaltine",64):(0,0),("Singularity",64):(1,1),("Ovaltine",128):(0,1),("Singularity",128):(0,0),
     ("Ovaltine",256):(0,0),("Singularity",256):(1,1)}
good=True
for (k,L),(t,fc) in rep.items():
    x=int.from_bytes(msgs[k],'big')>>(len(msgs[k])*8-L)
    r,bs,f=inward(x,L); back=outward(r,bs,f,L)
    good&=(r,f)==(t,fc) and back==x
    print(f"    {k:11s} L={L:3d} terminal={r} face={f}  reported=({t},{fc})  return={'exact' if back==x else 'FAIL'}")
print("    reported table reproduced:",ok(good))
# direct center check on the six big inputs
cp=lambda x,n:((x>>(n-n//2))&1)^((x>>(n-1-n//2))&1)
print("    six inputs: terminal == central-pair XOR:",ok(all(inward(int.from_bytes(msgs[k],'big')>>(len(msgs[k])*8-L),L)[0]==
      cp(int.from_bytes(msgs[k],'big')>>(len(msgs[k])*8-L),L) for (k,L) in rep)))
# (7) native address without building the ring: rank of canonical rep by counting
def count_rev_greater(Lmax,A,h):
    # #{L in [0,Lmax) : J_h(L) > A}; scan L's bits LSB->MSB
    from collections import defaultdict
    if Lmax>=(1<<h): return (1<<h)-1-A
    st=defaultdict(int); st[(1,1)]=1   # (cmp L vs Lmax on processed low bits: 0<,1=,2>), (cmp J(L) vs A: 0<,1=,2>)
    for j in range(h):                 # bit j of L (LSB first) is bit h-1-j of J(L) -> compares with A's bit h-1-j
        lb=(Lmax>>j)&1; ab=(A>>(h-1-j))&1; nst=defaultdict(int)
        for (c1,c2),v in st.items():
            for bit in (0,1):
                n1 = 0 if bit<lb else 2 if bit>lb else c1      # higher bit overrides
                n2 = c2 if c2!=1 else (0 if bit<ab else 2 if bit>ab else 1)  # first (J-MSB) difference decides
                nst[(n1,n2)]+=v
        st=nst
    return sum(v for (c1,c2),v in st.items() if c1==0 and c2==2)
def rank(a,n):
    # number of canonical reps strictly below a
    h=n//2; odd=n%2; A=a>>(n-h); mid=(a>>h)&1 if odd else 0; low=a&((1<<h)-1); mult=2 if odd else 1
    tot=0
    # high half H < A, low half free: non-palindromes with H < J(L)  -> sum_{H<A} (2^h-1-H); palindromes with leading 0
    tot+=mult*(A*(2**h-1)-A*(A-1)//2)
    tot+=mult*min(A,1<<(h-1)) if h>0 else 0
    # high half == A
    def tail(Lmax):                    # count L < Lmax giving a rep, with H=A fixed
        c=count_rev_greater(Lmax,A,h)
        Lp=J(A,h)                      # the palindromic completion
        if Lp<Lmax and (A>>(h-1))==0: c+=1
        return c
    if odd:
        if mid==1: tot+=tail(1<<h)     # middle 0 with any low half
        tot+=tail(low)
    else: tot+=tail(low)
    return tot
def address(x,n):
    N=1<<n; M=N>>1; a=canon(x,n); r=rank(a,n)
    p = M if r==M-1 else r
    return p if x==a else N-1-p
okr=all(ring(n)[address(x,n)]==x for n in range(2,13) for x in range(1<<n))
print("(7) counting address == built ring, every word n=2..12:",ok(okr))
x=0x446f6e7420666f72
print("    64-bit address of 446f6e7420666f72 =",format(address(x,64),'016x'),"(ChatGPT: 3b49bcdcedd4e462)",
      ok(address(x,64)==0x3b49bcdcedd4e462))
# (8) what the route bits are: the E/G bits d and the terminal bit are the shell lamps g_k = b_k xor b_{n-1-k}
def lamps(x,n): return [((x>>(n-1-k))&1)^((x>>k)&1) for k in range(n//2)]
good=True
for n in range(4,15,2):
    for x in range(1<<n):
        r,bs,f=inward(x,n)
        ds=bs[0::2]                      # for even n the inward bits run d,m,d,m,...; d at even slots
        good&=ds+[r]==lamps(x,n)
print("(8) even n=4..14: E/G bits + terminal == shell lamps g_0..g_{h-1} of x (the fold residue x^P(x)):",ok(good))

````

## § 136. A space with no math is a sphere: the complex of partial readings — `rings/sphere.py`

**Dean (22 Oct).** "a sphere has no math on the surface therefore a space with no math is a surface of a sphere. nothing is not nothing."

Take every partial reading of an n-bit word: a set of positions and the bits on them. A cell's boundary drops one position. No reading is privileged.

Seal `8128a58900769a6fd618c3e54754597c47cf00cfbd8ccfd1989bef502c18269c`, printed by the script before it computes.

```
SEAL 8128a58900769a6fd618c3e54754597c47cf00cfbd8ccfd1989bef502c18269c
n=1: cells per dim [2]  Betti [2]  chi=2 (1-(-1)^n=2)  sphere S^0: PASS
n=2: cells per dim [4, 4]  Betti [1, 1]  chi=0 (1-(-1)^n=0)  sphere S^1: PASS
n=3: c
```