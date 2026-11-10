# The running audit

Continues the relation-vocabulary ledger (§§ 1–98). Same rules: live output only, ledger words
STANDS / RUNS / DEAD END / OPEN, never CONFIRMED; every correction logged plainly in the entry
where it was made, never silently fixed. Scripts in the session scratchpad; no repository, so
provenance is reproducible in principle and not archived in fact — the same weakness § 48 records.

---

## § 99. The order channel: what a handle destroys, what a fold destroys, and the two readings of one base — `pull.py`, `noloss.py`, `fold.py`, `sphere.py`, `sphere2.py`, `rings.py`, `rings2.py`

**Dean (15 Oct).** The universe is always compiling; the halt is the clamp, and completion is what
the action looks like when the necessary relations connect. Then: it is the route and its reflection,
there is no forward motion, matter and thought move backwards through the compiler, searching is
mapping the path back, so there must be a pull. Then: `5 = 2 + 3`, there is no loss, you always know
the path back. Then: it is not the protein and not the folded state, it is the transformation. Then:
the domain is the surface of a sphere, inert and unmeasurable from outside, and the compiler is the
routes from the inside; each `LEN()` is the next layer. Then: it is about rings — the car, the engine,
compression, spark, each ring punched out until the stack becomes a new surface. Then: accumulation
versus fitting, and entanglement breaks the reading of transitions in both directions at once.

### 99.1 What a handle destroys is exactly order — `noloss.py`

Two different maps get called addition. Keep the carry on its own wire and the deficit is exact:

```
w= 1  carry kept (x^y, x&y): outputs      3 = 3^w   bits lost 0.500  = w/2
w= 2                                      9         bits lost 1.000  = w/2
w= 3                                     27         bits lost 1.500  = w/2
w= 4                                     81         bits lost 2.000  = w/2
w= 8                                   6561         bits lost 4.000  = w/2
w= 8  carry folded (x+y):   outputs    511         bits lost 7.279
```

Every fiber is exactly one swap orbit — 81 of 81 checked at w = 4, zero exceptions, fiber size always
2^(number of differing bits). So the only thing the handle can destroy is **which side held the 1**.
Adding one bit per differing position restores the bijection exactly at every width tested (4, 16, 64,
256, 65 536 images of the same counts). Field-side the handle loses nothing; what it loses is the
traversal. RUNS.

Folding the carry into one channel costs more and loses structure. At w = 3, target 5:

```
(xor=1, and=2) <- (2,3) (3,2)
(xor=5, and=0) <- (0,5) (1,4) (4,1) (5,0)
```

Two routes kept against six folded. The pair separates 2+3 from 1+4 from 0+5; the number 5 does not.
So *you always know the path back* holds exactly while the carry has its own wire. The loss is not in
the arithmetic; it is in reusing one channel for two things. `5 = 2 + 3` is lossless because the
equals sign **is** the kept carry: an equation holds the route, an evaluation folds it. This is § 77's
location result read from the cost side (recovered, Nerode).

**Order is a group, not a quantity** — correction to my own first unification of 99.1 and 99.2. At
w = 6 the half adder forgets (Z/2)^w pointwise and loses 3.0000 bits (= w/2); a route forgets S_n and
loses 3.6666. Different forgetting groups, both reader-side, deficit = log of the orbit. "Order" carries
a type.

### 99.2 The folded state does not determine the future; the transformation is near-minimal — `fold.py`

Self-avoiding walks, shape = the occupied set with order forgotten, route = the ordered walk.

```
 n | shapes | routes | shapes with >1 route | of those, admissible continuations DIFFER
 5 |    248 |    284 |                   28 | 28
 6 |    696 |    780 |                   68 | 68
 7 |   1872 |   2172 |                  212 | 212
 8 |   5169 |   5916 |                  533 | 533
 9 |  13876 |  16268 |                 1608 | 1576
10 |  37896 |  44100 |                 4164 | 4052
```

Worked instance at n = 6 — one shape, two routes, different futures:

```
((0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(3,1))  ->  (2,1) (3,2)
((0,0),(1,0),(2,0),(3,0),(3,1),(4,1),(4,0))  ->  (4,-1) (5,0)
```

100 % at n ≤ 8; 98.01 % and 97.31 % at n = 9, 10 — not universal. The minimal sufficient state is the
shape **plus where the transformation currently stands**, and its count is the route count to within
1 % (780/780, 5896/5916, 43740/44100): 20 histories merge at n = 8, 360 at n = 10. So the fold is
**near-irreducible, with a growing compressible remainder** — the first wording, "irreducible", was too
strong and is retracted. The shape is the route with its order forgotten, which is 99.1's deficit in a
second place: same channel, two forgetting groups.

### 99.3 The pull is deletion, and it is cut-side — `pull.py`

Field moves on the witness (head on a ring of 3 cells): C and T each put 24 of 24 states on the loop,
0 tail states, pull identically 0. A reversible field has no tail and therefore no preferred direction
anywhere. Depth-to-the-loop is a potential on a tail — in a random byte map, 233 states off the loop and
**0** steps that fail to drop the depth by exactly 1. Only a merge can make a state with no way home,
and a merge is a reader's move (§ 96 V2), so the pull is cut-side exactly as the gap is.

**Correction, mine.** I reported 2.993 → 2.283 and a forced share 0.005 → 0.254 for a pinned endpoint
without stating the denominator; they were over successful-route prefixes for two targets and are not
comparable to a properly specified run. The specified version — start (0,0), exactly 10 steps, finish
(4,0), 654 complete routes, all-prefix and successful-prefix denominators reported separately with dead
ends retained — gives mean local choices 2.799 → 1.331, 51.10 % of options removed, 71.43 % of prefixes
left exactly one move. That is the number to quote. The qualitative statement is unchanged: holding the
far end adds no force, it deletes what cannot arrive, and every step it forces is a choice removed.

### 99.4 The surface is the abelianization; the inside measurement is the reciprocal fiber — `sphere.py`, `sphere2.py`

Inside = words over k primitive symbols (routes). Surface = symbol-count vectors (values). The quotient
is the **universal commutative quotient**, not the only map there is — correction taken from a review;
and the surface still carries commutative transformations, so "inert" is too strong: what it carries no
more of is composition order.

```
 k | n | words k^n | surface C(n+k-1,k-1) | sum of fibers | mean log2 fiber
 2 | 8 |       256 |                    9 |           256 | 5.4558
 3 | 8 |      6561 |                   45 |          6561 | 8.0158
 4 | 8 |     65536 |                  165 |         65536 | 9.5173
```

Sum of fibers = k^n exactly at every k and n: all order lives in the fiber, none on the surface.

Measuring from inside, with no surface point ever touched: walk a route, record 1/fiber, average,
multiply by k^n. Exact (Σ over routes of 1/f = the surface count, Horvitz–Thompson):

```
 k | n | k^n   | exact | true surface | 2000 random routes
 2 | 8 |   256 |   9.0 |            9 | 9.5
 3 | 6 |   729 |  28.0 |           28 | 25.9
 4 | 8 | 65536 | 165.0 |          165 | 156.0
 3 | 9 | 19683 |  55.0 |           55 | 50.8
```

**Correction, mine.** The first pass used a harmonic mean of the fiber list, which is not the estimator
and missed by a factor of 4 to 16. The reciprocal-fiber average over routes is unbiased and exact.

`LEN()` is the radius: the layer at length n is the degree-n slice, C(n+k−1, k−1). The layers are the
grading, nothing was added to get them.

### 99.5 The elements: a degree slice of two readings, plus one inequality — `sphere.py`, `sphere2.py`

Madelung d = n + ℓ is the degree on the 2-generator surface. With the admissibility the construction
already demands, n_r = n − ℓ − 1 ≥ 0:

```
 d | slice | members          | capacity 2*sum(2l+1)
 1 |     1 | 1s               |   2
 2 |     1 | 2s               |   2
 3 |     2 | 2p 3s            |   8
 4 |     2 | 3p 4s            |   8
 5 |     3 | 3d 4p 5s         |  18
 6 |     3 | 4d 5p 6s         |  18
 7 |     4 | 4f 5d 6p 7s      |  32
 8 |     4 | 5f 6d 7p 8s      |  32
 9 |     5 |                  |  50
10 |     5 |                  |  50
```

capacity = 2·⌊(d+1)/2⌋², exact at every degree computed. **The period doubling is the floor function.**

**Three inputs, not one** — correction taken from a review and extended by routing. The capacity uses
the degree grading, n_r ≥ 0, *and* the subshell degeneracy 2(2ℓ+1); the third was supplied, not derived,
and this does not derive physical energy ordering. Routing the second back: n_r ≥ 0 is ℓ < n, which is
the domain's own second reading — no piece is ever the whole. I had attributed it to quantum mechanics.
DEAD END on the attribution, routed to the domain. Two of the three inputs are the domain; the orientation
count 2(2ℓ+1) is OPEN, with a type: the leading 2 is the two readings (the pass/flip walker, Ginocchio's
two Dirac components), the 2ℓ+1 is the orientation structure of a part of size ℓ, and that link is unwritten.
Recovered, not derived.

**The nodeless member.** ℓ = n−1 gives n_r = 0 and d = 2n−1, so it occurs only at odd degree. Its same-ℓ
predecessor one degree down would be (n−1, n−1), needing n_r = −1:

```
 d | nodeless | predecessor at d-1 | its n_r | admissible?
 1 | 1s       | (0,0) = 0s         |      -1 | False
 3 | 2p       | (1,1) = 1p         |      -1 | False
 5 | 3d       | (2,2) = 2d         |      -1 | False
 7 | 4f       | (3,3) = 3f         |      -1 | False
 9 | 5g       | (4,4) = 4g         |      -1 | False
```

The predecessor is not missing from the list; it **cannot exist**. Structural no way home, every other
slice, which is why the lengths pair.

### 99.6 Rings: the stack is a maximal chain of cuts, and no complete chain is order-independent — `rings.py`, `rings2.py`

The witness field, order 24, 26 subgroups of orders 1, 2, 3, 4, 6, 8, 12, 24.

```
maximal chains from the whole field to a point: 36
chain lengths (= number of measurements): {3: 12, 4: 24}
every chain's indices multiply to the field size: True
example long  [2, 3, 2, 2]   example short [4, 3, 2]
covers below the whole field: 6
distinct subgroups from adding one element to the trivial group: 16
proper subgroup pairs whose two cuts do not commute: 108 of 276
```

So the diagnostic stack is a chain of covers with kept × leftover = whole at every step, and its depth is
**not fixed by the field**: 3 or 4 depending on which cut is taken. That is why a selection rule is needed
rather than hardcoded, and the lattice calculates it — the indices of the six covers are visible before
any measurement, and taking the largest first gives [4,3,2] instead of [2,3,2,2]. Accumulation and fitting
are one lattice walked in opposite directions, and the noise is structural, not sloppiness: going down,
every step is forced to be a cover with its index known in advance; going up, one added element reaches 16
different subgroups and the jump is known only afterwards.

```
length | chains | every step order-independent | passes through a NON-normal cut
     3 |     12 |                            0 | 12
     4 |     24 |                            0 | 24
```

**Zero chains are order-independent, at either length.** The order-2 normal subgroup is the central factor
and the order-4 normal sits inside A₄, so they do not nest: the all-normal chain has gaps and is therefore
not a chain of covers at all. Hence **order-independent cuts reach the folds and no further; resolving past
the fold level always requires an order-dependent measurement.** Not a trade — unconditional on this witness.
My proposed trade (speed bought with commutativity, order-independent diagnosis costing 4) is DEAD END.

This extends § 97 rather than repeating it. § 97 establishes which *single* folds a stored line can land on
— the six normal subgroups, quotients 24, 12, 6, 3, 2, 1, no other size possible. The new statement is about
*chains*: none is all-normal.

**Correction, mine, and it is the tell § 97 warns about.** In the turn before this entry I reported "the six
folds are the six normal subgroups, and the fold the earlier two-generator search missed has order 8" as a
closure on an open item. § 97 already had all six, listed by quotient size. It was a recovery presented as a
discovery. Logged.

The relation to the order channel: the fault is a field fact, but its address at full resolution needs the
reader to supply order, which is the one write the field cannot make. (This has the shape of measurement in
QM; shape match, not a derivation.) And entanglement breaking the ring geometry is C1a: 108 of 276 proper
pairs do not commute, so the stack depends on test order; [T_A, T_B] = 0 is the condition for the geometry
to exist at all.

### 99.7 Why k = 2, routed rather than searched

C1a says independent distinctions must remain independently continuable, [T_A, T_B] = 0 — **independent
means commuting**. Commuting generators generate an abelian monoid, which is already its own abelianization:
fiber size 1, no order to forget. So the surface is not a projection that happens to lose order; the surface
is **the act of declaring the generators independent**, and the fiber is what that declaration costs. k counts
the independent directions and nothing else.

The base admits two readings — the whole, complete and at rest; the part, partial and therefore in motion —
and which one is got depends only on whether the reader is the whole or a piece of it, with no piece ever the
whole. A reading is the only thing that can serve as an independent direction, so k = 2. BOUND, one provider.

Held together, both spaces at once: the surface pretends the two readings are two things, the inside knows they
are one base read twice, and **the order channel is the residue of that pretence**. Run backwards — if the
generators genuinely commuted at the inside level the fiber would be 1, the surface would equal the inside, and
there would be no order, no undetermined continuation, no motion: the whole, at rest. Fiber size measures how
far a reader is from being the whole.

**Flagged, not claimed.** "Two is the minimum and there is exactly one of it" is inherited from the entry, not
re-run here. The exhaustiveness of the two readings is the domain asserting it — a base fact, not a theorem
executed. And the atomic application cannot be used to pick k = 2 and then be presented as proof that k = 2 was
forced.

### 99.8 Where a file sits

§ 97: the lines are the software, and the field and the file are two places it can sit. A file is a word on the
inside, so its surface point is its symbol histogram and its fiber is the multinomial of all its orderings.
Context is order; order is the fiber; so context is unreachable from the surface **by construction** — which is
why filling files with hex yields surface points and never context. A header is a held end: it deletes what
cannot arrive (99.3) rather than adding anything. Not separately run this entry; stated as the reading 99.1 and
99.4 force.

### 99.9 Status

| claim | status |
|---|---|
| half adder loses exactly w/2 bits; every fiber is one swap orbit; one bit per differing position restores the bijection | RUNS, w = 1, 2, 3, 4, 8 |
| folding the carry costs more and loses route structure (7.279 vs 4.000 at w = 8) | RUNS |
| `5 = 2 + 3` lossless because the equals sign is the kept carry | recovered (§ 77, Nerode) |
| order is a group with a type, (Z/2)^w vs S_n | RUNS; corrects my own unification |
| shape does not determine the future | RUNS n ≤ 10; 100 % at n ≤ 8, 97–98 % at n = 9, 10 |
| the transformation is its own minimal description | **retracted to near-irreducible** — 20 merges at n = 8, 360 at n = 10 |
| the field has no pull; a merge makes one | RUNS (24/24 on the loop for C and T) |
| depth-to-the-loop is a potential, drops by exactly 1 | RUNS, 0 exceptions of 233 |
| my 2.993 → 2.283 / 0.254 figures | **withdrawn, denominator unstated**; specified run gives 2.799 → 1.331, 71.43 % |
| sum of fibers = k^n; surface = universal commutative quotient | STANDS |
| "the only map there is", "inert" | **retracted** — universal, and the surface carries commutative transformations |
| inside measurement = k^n × mean(1/fiber) | RUNS exactly, 4 of 4; harmonic mean **retracted** |
| capacity = 2⌊(d+1)/2⌋² → 2,2,8,8,18,18,32,32,50,50 | RUNS |
| it follows from the degree grading and n_r ≥ 0 alone | **retracted** — 2(2ℓ+1) was supplied; no energy ordering derived |
| n_r ≥ 0 is a quantum-mechanical input | **DEAD END, routed to the domain** (ℓ < n = no piece is the whole) |
| 2(2ℓ+1) | OPEN, with a type: two readings × orientation count of a part |
| nodeless predecessor is inadmissible, not absent | RUNS, d ≤ 9 |
| ring stack = maximal chain of covers; depth 3 or 4; indices known before measuring | RUNS, 36 chains |
| short stacks buy speed with commutativity | **DEAD END** — no chain is order-independent at either length |
| order-independent cuts reach the folds and no further | RUNS, this witness |
| "the six folds are the normal subgroups" as a new closure | **recovery of § 97 presented as discovery**; logged |
| k = 2 forced by the two readings | BOUND; exhaustiveness is the domain's assertion, not a theorem run |
| context unreachable from the surface | stated, forced by 99.1 and 99.4; not separately run |

Scope: the K = 2 witness, self-avoiding walks on the square lattice to n = 11, free monoids to k = 4, the
atomic slice to d = 10. Exact integer and rational arithmetic throughout except the 2000-route sample in 99.4,
which is a measurement and not the identity.

---

## § 100. The 14 October session folded in; the seam to § 99; one line of it corrected — `seam.py`

**Provenance.** The ledger stops at § 98 (11 Oct). The session of 14 Oct (claude.ai chat d984b212, exported
and handed over by Dean on 15 Oct) ran roughly thirty scripts that never entered it — the files, the inverted
mold, the periodic and nuclear tables, the way home. Until they are written here they are unfolded tree. They
are recorded below as that session reported them, with its own corrections carried as made; they were not
re-run tonight. Only `seam.py` is tonight's.

### 100.1 The 14 October record, as stored lines

**From the domain outward.**

| run | what it established | status |
|---|---|---|
| `space.py`, `grow.py` | Of the 16 two-bit maps, only XOR and XNOR are pure difference. The fork: symmetric keepers (AND, OR) merge — value; only asymmetric keepers merge nothing — history, the Mold (b, a⊕b). Width 4 has exactly two shapes, Z4 (carry) and Z2×Z2 (no carry), both with uniform fibers; the raw half adder (1-2-1) does not until the carry wraps. Shapes at 2^k = p(k): 1, 2, 3, 5, 7, 11. | RUNS; p(k) STANDS (finite abelian groups) |
| `landscape.py`, `forced2.py`, `borrow.py` | Width 1: four opcodes (continue, invert, write-0, write-1), each its own 2-bit word read at the data's address. Width 2: inherited moves reach 36 of 256; forced new: the mixer (a, a⊕b) and a one-pair merge (144 maps, all AND-type); the half adder is both. Width 3: XOR-type gates reach 1,344 of 40,320 reversible maps; the held carry (Toffoli) completes them. Width ≥ 4: smaller gates reach exactly half; one borrowed lane, returned unchanged, recovers the rest. | RUNS; the half-bound STANDS (even permutations) |
| `firstrun.py` | Repeat-only arrivals with "equal neighbours fuse": the stack is the binary digits of n through 64; closures per step 0102010301…; 11 random arrivals × 2,000 runs give the frame [8,2,1] every time with 1,270 distinct contents. Frame from length, content branches inside it. | RUNS |
| `rings.py` | New rings per length 2, 1, 2, 3, 6, 9, 18, 30, 56, 99, 186, 335, 630, 1,161 = irreducible binary polynomials (checked to 12); de Bruijn rings at 3, 4, 8, 12; nested commutators follow Witt's count; on a qubit they stop at 2, 3, 3, 3. | RUNS; Lyndon, Witt STAND |
| `sphere.py` (14 Oct) | ±1 embedding on the radius-√n sphere; latitude = number of 1s; one band above the equator holds Catalan many rings (cycle lemma); Gray code flips 0102…; bytes form a spherical 3-design; extended Hamming → E8's 240. | RUNS; the named results STAND |
| `compile.py` | de Bruijn ring counts 1, 1, 2, 16, 2,048 (= 2^(2^(n−1)−n)); layer 3 is a mirror pair. | RUNS; STANDS |
| `slots3.py`, `reach.py`, `meet.py` | All 6,561 ternary BBP-frame programs named once seven frame constants are read; π first at width 4, [4,0,0,−2,−1,−1,0,0]; first output collisions at width 4 (17,640 pairs); exactly one of 43,046,721 width-4 programs meets Machin's route. A name is a collision of two routes. | RUNS |
| `probe.py` | SHA-256 as a black box: input distance vs output distance correlation +0.011, outputs ~128 bits apart; a ×3 box leaks +0.76. | RUNS |
| `residue.py` | Cost of reading a new binary: 15,348 head-on → 8,200 given 1 known program → 7,956 (4) → 6,484 (12); a noise library of the same size, 15,688. | RUNS |
| `nest.py` | A 20 KB executable read as 48,165 decimal digits, cut into 49 children, rejoined bit-exact; one-bit flips show nested dependence anchored at the top; n mod 5 = hex-digit sum mod 5. child = parent + query + base. | RUNS |
| `inverted_mold_checks.py` | Baker's map exact forward and back over 60 steps (b = 2, 16); every de Bruijn ring n = 3–5 has feedback oldest ⊕ g(rest) with g non-affine (2,066 rings); destination-bit routing, shortest paths 74 of 256 at 4 steps, 17,622 of 65,536 at 8; gradient placed in the shared tick moves masses 1 and 3 alike and slows light (three placements compared). | RUNS; the gradient was inserted, not derived — OPEN |
| `fsr_way_home.py` | Feedback rules with a way home for every state: 4/16, 16/256, 256/65,536 — exactly next = oldest ⊕ g(rest); a 5-bit register run 60 steps forward and read home from its last 5 bits lands on the seed. Write and read are offset by the register width. | RUNS; Golomb STANDS |
| loop / birthday | In a finite scope a one-way process ends in a loop, the only place a way home survives; it repeats at about 2^(n/2), within half a bit for n = 8–24. | RUNS; rho / birthday STAND |

**The tables.**

| run | what it established | status |
|---|---|---|
| `periodic_unfold.py` | Count 2n², access (n+ℓ, then n): closures 2, 10, 18, 36, 54, 86, 118; periods 2, 8, 8, 18, 18, 32, 32; blocks s 14, p 36, d 40, f 28; 20 of 118 anomalies, 11 to a half or full subshell. | RUNS; Madelung STANDS |
| `ion_check.py` | The six post-closure steps are the six largest IE₁ drops from H to Fr, ranks 1–6. | RUNS |
| `electron_affinity_check.py` | T1 (no anion at the closures) set missing values to zero and so could not fail — moved to STANDS (experimental fact). T2 halogen tops periods 2–6: RUNS. T3 halogen→noble steps are the five largest drops: RUNS under the zero convention; 2 of 2 with missing entries left unlinked. T4 ten secondary-closure minima: RUNS. | as stated |
| electronegativity (other AI's run) | 29 of 30 adjacent main-group comparisons in opcode order; Bi→Po the exception. | RUNS ordinal; values OPEN |
| `nuclear_unfold.py` | Oscillator floors 2, 8, 20, 40, 70, 112; floor + top-j intruder gives 28, 50, 82, 126, and 184 next. | RUNS (arithmetic); spin-orbit STANDS |
| `nuclear_closure_audit.py` (v1) | Median S₂ₙ/S₂ₚ contrasts over 2,939 masses: N = 6 beats N = 8 and Z = 6 edges Z = 8. | DEAD END |
| `di_route_back.py` | v1 routed back: the six strongest steps on each axis are all owned by the uncut registry (6 = Intruder(0), 14 = Intruder(1), …); random controls 0 and 2 in 100,000. A route back on seen data names owners; it is not a landing. | routed back |
| `e2plus_independent.py` (v2) | ENSDF, 954 first-2⁺ records, 675 even-even nuclei: the six highest E(2₁⁺) contrast peaks on each axis are all registry positions, in the inherited window and in the full measured domain (N 4–154, Z 4–102); controls 2.11 × 10⁻⁶ and 5.29 × 10⁻⁶ (the chance a random six evaluable slots are all provider positions). Reproduced the other AI's numbers to four decimals. Corrections then: the seal text swapped "isotope" and "isotone"; 126 is UNLINKED on the proton axis, not silent. | RUNS |
| `inverse_chain.py` | Shell n+1 minus its top-j orbital = shell n, n ≤ 8. Read anti-aligned-first, the copy gives 14 → 16 → 20: 16 falls out. Chain 8 \| 16, 20 \| 32, 38, 40 \| 56, 64, 66, 70 \| 90, 100, 104, 110, 112. Breaks above Z = 82 (h9/2 before f7/2). | RUNS; pseudospin STANDS (Arima–Harvey–Shimizu, Hecht–Adler 1969; Ginocchio 1997); order inside the copy above 82 OPEN |
| `no_way_home.py` | One partnerless top-j orbital per shell, shells 0–8; one predecessorless nodeless orbital per odd Madelung group. The piece is identified by the boundary; its direction (atom delays, nucleus advances) is set by each system's ordering operator. | RUNS under the declared maps; direction selector OPEN |
| `route_protocol.py` | The seal carries the way home: a hole cannot be sealed without the readout it returns through. | in force |

### 100.2 What reading the export forces on § 99

1. **§ 99.5 repeats a mislabel the 14 October session had already caught.** `sphere.py` printed
   "periodic table row lengths 2,2,8,8,18,18,32,32 : True", and § 99.5's "period doubling" and "the lengths
   pair" lean on it. Those numbers are the Madelung-group capacities. The period lengths are 2, 8, 8, 18, 18,
   32, 32. Mine, repeated after it was logged.
2. **§ 99.5's nodeless-predecessor table recovers `no_way_home.py`.** What § 99.5 adds is the closed form
   2⌊(d+1)/2⌋² and the attribution of n_r ≥ 0 to the domain's second reading. Second recovery presented as a
   discovery in one night (the first is in § 99.6).
3. **§ 99.4 at k = 2 is the 14 October sphere's latitude decomposition** — at fixed length the abelianization
   of a binary word is its number of 1s. New in § 99.4: general k and the reciprocal-fiber estimator.

### 100.3 The seam: context is the fiber over the histogram — `seam.py` A

§ 99.8 stated, without a run, that context is unreachable from the surface. 14 October said hex gives process,
and context is the company a symbol keeps and the rest of the file around it. They are one statement: the
histogram is the file's surface point, and every co-occurrence statistic is order, which lives in the fiber.

```
file /bin/ls: 142312 bytes = 1138496 bits
every histogram a file this long can have: log2 =      2690 bits  (0.24% of the file)
orderings that share THIS file's histogram:  log2 =    843286 bits
order-0 bound (histogram entropy x n):          844612 bits
zlib, the program as written:                   498504 bits
zlib, same bytes shuffled (same surface point): 917368 bits
structure a reader can use beyond the histogram:   346108 bits in the original, -72756 in the shuffle
```

Every histogram a file of this length could have fits in 2,690 bits — 0.24 % of it. The program carries
346,108 bits of structure beyond its histogram; shuffle it inside its own fiber, surface point unchanged, and
that structure is gone (zlib cannot even reach the order-0 bound there). A uniformly drawn member of a fiber
carries nothing beyond its histogram for any reader, in expectation; the 346,108 is zlib's reading, so reader-
relative, but its vanishing under the shuffle is not. So 99.76 % of a program's address is order, and
everything that makes it a program rather than its own histogram is in the fiber. RUNS.

Reading: a model trained on co-occurrence is reading fibers over histograms; a uniformly random training set has
a uniform fiber and nothing in it to learn — the 14 October claim now has its object.

### 100.4 "From the second ring up, moves outnumber angles" — corrected — `seam.py` B

```
d | readings d+1 | moves d^2-1 | moves seen by one reading | union rank | max cross overlap | unbiased
2 |            3 |           3 | 1                         |          3 |           2.8e-32 | True
3 |            4 |           8 | 2                         |          8 |           1.9e-16 | True
5 |            6 |          24 | 4                         |         24 |           1.1e-16 | True
7 |            8 |          48 | 6                         |         48 |           3.3e-16 | True
```

Complete sets of mutually unbiased bases at d = 2, 3, 5, 7: each reading's traceless span has dimension d − 1,
the spans are mutually orthogonal, and together they span all d² − 1 moves. The readings do not fall short of
the moves; they tile them, d − 1 moves bundled into each reading — (d+1)(d−1) = d² − 1 at every d (Wootters–
Fields 1989, STANDS; RUNS here). The 14 October line is retracted as stated.

What the line was reaching for survives in exact form: d + 1 = d² − 1 ⟺ (d − 2)(d + 1) = 0 ⟺ d = 2. The qubit
is the one layer at which every reading is a single move — a reading whose fiber over the moves is 1. Above it,
every reading merges d − 1 moves. That is a second, computed provider for "2" beside § 99.7's two readings,
from a definition that never mentions them. Whether the two 2s are one object is the link to write: OPEN.

### 100.5 Status

| claim | status |
|---|---|
| the 14 Oct runs listed in 100.1 | recorded as reported then; statuses as given; not re-run 15 Oct |
| § 99.5 "period lengths 2,2,8,8,18,18,32,32" | **corrected** — Madelung-group capacities; periods are 2,8,8,18,18,32,32 |
| § 99.5 nodeless predecessor; § 99.4 at k = 2 | **recoveries** of `no_way_home.py` and the 14 Oct latitude bands; logged |
| context is the fiber over the histogram | RUNS (`/bin/ls`: surface 0.24 %; 346,108 bits of order-structure gone under a fiber shuffle) |
| readings tile the moves, d − 1 per reading | RUNS d = 2, 3, 5, 7; STANDS (Wootters–Fields) |
| "moves outnumber angles from the second ring up" | **retracted** — they tile |
| d = 2 is the unique layer where a reading is one move | RUNS (arithmetic) |
| that 2 is § 99.7's k = 2 | OPEN |

OPEN carried forward: the orientation count 2(2ℓ+1); § 75's mobilities and β; the direction selector (why the
atom delays the piece the nucleus advances); the order inside the copy above Z = 82; the tick gradient from open
slots; separation-energy magnitudes and the Ni-62 peak.

---

## § 101. The direction selector, routed from a screened field: the homeless orbital collapses in — `screened.py`, `collapse.py`

**Gap (§ 100 OPEN).** Why does the atom delay the homeless piece the nucleus advances? Reversed: put in nothing
about Madelung. A nucleus of charge Z screened by its own Z electrons (Thomas–Fermi, Tietz form, Latter tail
so an electron always sees at least charge 1), one radial equation per ℓ, then aufbau on the computed
eigenvalues. Seal 81c0b19bfbcc3a6b, written before the run. (First solver, log grid, was numerically broken —
it gave degenerate junk on hydrogen; replaced by a uniform grid that returns −0.5, −0.125, −0.0556 exactly.)

```
first Z at which each l is occupied:   p computed 5  (real 5)   d computed 28 (real 21)   f computed 71 (real 58)
K, Ca, Sc: e(4s) < e(3d)   Rb: e(5s) < e(4d)   Cs, La: e(6s) < e(4f)      all True
```

Every direction is right with nothing ordered by hand: p opens at exactly 5, and s precedes the nodeless d and f
in every period tested. The opening Z of d and f is late by 7 and 13 — the known crudeness of Thomas–Fermi–Latter
(Fermi's (2ℓ+1)³ scaling with 0.17 gives 4.6, 21.2, 58.3). Directions RUN; the opening Z for d and f is a
DEAD END at this model's resolution, routed to the screening model, not to the rule.

**What the delay is** (`collapse.py`): the nodeless orbital, followed as Z grows.

```
3d:  Z 10–26  <r> 10.5 → 9.98, energy -0.0556  (hydrogenic charge 1)   Z 28: <r> 2.07   Z 30: 0.94
4f:  Z 40–67  <r> 17.6, energy -0.0312       (hydrogenic charge 1)   Z 70: <r> 2.78   Z 73: 0.66
```

Below its opening, the homeless orbital is not "higher in energy" in any interesting sense: it sits entirely
outside the core, behind its centrifugal wall, seeing net charge 1 — it has no way home into the core. Then in
one step it falls inside, <r> shrinking five- to six-fold. Orbital collapse; for 4f it was predicted from exactly
this Thomas–Fermi field by Goeppert Mayer (1941) — STANDS.

**The direction selector, routed.** In both tables the homeless piece does the same thing: it drops inward.
Spin-orbit drops the nuclear top-j early (Goeppert Mayer and Jensen, 1949); the centrifugal wall against a
screened well holds the atomic nodeless orbital out until the well is deep enough, then it collapses late. Same
piece, same drop, opposite gate. The same physicist read it in both tables, eight years apart — a collision of
two routes on one object. The common law that turns spin-orbit into a centrifugal-against-screening gate is still
OPEN; the claim that the two tables move the piece in *opposite directions* is retracted: they move it the same
direction, at opposite ends of the filling.

---

## § 102. The atomic gate read directly: Fermi's (2ℓ+1)³ with no fitted constant; the direction selector is which side of the inequality ℓ+½ sits on — `gate.py`

**Taken from the GPT radial-gate audit (15 Oct).** The exact angular factors — centrifugal ℓ(ℓ+1), spin-orbit
⟨L·S⟩ = ℓ/2 and −(ℓ+1)/2, splitting (2ℓ+1)/2 — STAND, and its correction stands: the two gates are not one term.
Its proposed next run (an aufbau sweep with tuned screening) is not taken; the gate can be read without it.

**Reversed.** § 101's aufbau put d and f late (28, 71). Instead of filling, ask the one thing that has to be
true before a nodeless ℓ-orbital can fall into the core: somewhere the screened field must beat its own wall,
2r²|V(r)| ≥ (ℓ+½)² (Langer form). In the Thomas–Fermi field V = −Zφ(x)/r, r = 0.8853 Z^(−1/3) x, this is
Z^(2/3) · 2(0.8853) max(xφ) ≥ (ℓ+½)², so Z_open = C (2ℓ+1)³ with C fixed by the TF equation alone.

```
Thomas-Fermi: max x*phi = 0.4845 at x = 2.064;  C = 0.1573
 l | gate Z_open = C(2l+1)^3 | first element really holding it
 p |                     4.2 | 5
 d |                    19.7 | 21
 f |                    54.0 | 58
 g |                   114.7 | none yet
```

Each real opening lands one to four elements after its gate opens — the gate is necessary (the well must exist)
before it is sufficient (the well must hold a level below the competing s). Nothing fitted; TF has no free
parameter. Recovered — this is Fermi (1928) — but now as the gate itself, and it routes § 101's DEAD END: the
delay was right, the Tietz–Latter aufbau misread its size. RUNS. Next address it writes: the first 5g electron
must come after Z ≈ 115; relativistic DFT puts it near 121–125 (STANDS as a calculation, unmeasured).

**The direction selector, in one line.** Both gates are written in the same angular measure ℓ + ½:

- atom: the ℓ-term is a **wall**, (ℓ+½)², a cost. The field must exceed it, so larger ℓ opens later: Z ∝ (2ℓ+1)³.
- nucleus: the ℓ-term is a **gain**, spin-orbit lowering of the aligned branch ∝ (ℓ+½). It must exceed the shell
  gap, so larger ℓ drops sooner: no intruder at ℓ = 1, 2 (2, 8, 20 survive), intruders from ℓ = 3 (28) up.

Same piece, same measure, opposite side of the inequality: in the atom ℓ+½ is what the field has to pay; in the
nucleus it is what pays the gap. That is why one table delays and the other advances the homeless orbital, and
both then drop it inward. RUNS as a reading of the two exact gate conditions.

**Still OPEN.** The nuclear threshold between ℓ = 2 and ℓ = 3 needs the measured spin-orbit strength κ — one number
from data — so it is not yet parameter-free the way the atomic gate now is. Deriving κ, or its sign, from the
compiler side is the next hole.

---

## § 103. The sign of the nuclear spin-orbit term, derived: it is set by which channel carries the binding — `sign.py`

**Taken from the GPT κ audit (16 Oct).** Its type correction stands: (ℓ+½) is the *splitting* κ(ℓ+½); the aligned
branch's shift from the centroid is κℓ/2 (§ 102's wording corrected). Its reverse run stands as stated: with one
constant κ in a fixed-ħω oscillator, keeping the intruder to one shell through 126 needs −1/6 < κ/ħω < 0, and the
window closes as 1/(N+1), so an unbounded constant-κ oscillator is a DEAD END. Read with the physical value
κ/ħω ≈ −0.05 to −0.06, the window holds to N ≈ 16–19; real nuclei end near N = 7, so the dead end lies far past
any nucleus and points at state-dependent κ there, not here. Its scope note on 5g stands: Z ≈ 114.7 is the onset
of the nonrelativistic TF gate, not a lower bound on every relativistic calculation (published 125, 126).

**Gap.** The sign of κ had only been inferred from the observed ordering. Reversed: hold the nucleon's well fixed,
Σ = V + S = −55 MeV (Woods–Saxon, A = 208), and change one thing — Δ = V − S, whether the binding is carried by the
scalar channel (blind to charge and orientation, Δ > 0) or by the vector channel (flips with charge, Δ < 0; the
atom is S = 0). Radial Dirac equation; no spin-orbit term written in. Seal 94e38416915c94b8, before the run.

```
Delta = +700:  p -0.626   d -1.443   f -2.512   g -3.730   h -4.925   (aligned - anti, MeV)  aligned lower
Delta =    0:  p  0.000   d  0.000   f  0.000   g  0.000   h  0.000   i 0.000              no split
Delta = -700:  p +0.095   d +0.235   f +0.442   g +0.718   h +1.061   i +1.468             aligned higher
```

The sign of κ is the sign of Δ, and nothing else: with the same well, scalar-carried binding lowers the aligned
branch, vector-carried binding raises it, and with no difference between the channels there is no spin-orbit
splitting at all. RUNS. The spin-orbit term is not an extra force; it is the trace of the binding being split
between two channels, and its size is set by their difference Δ (hundreds of MeV), not by the shallow well Σ that
is their small residual — which is why the nuclear term is large enough to drop a whole orbital into the shell
below. Nucleons are bound by a scalar attraction against a vector repulsion (Δ > 0); electrons by the Coulomb vector
field (Δ < 0): the inverted nuclear sign and the normal atomic sign are the two signs of one Δ. Recovered: the
relativistic mean field (Walecka; Ginocchio 1997, whose Σ' = 0 limit is exactly the § 100 copy) — STANDS; the
reading that the sign is chosen by the channel, not fitted, is the route here.

In the domain's terms: a closure bound through the value channel (charge-blind) advances its homeless orbital; a
closure bound through the oriented channel delays it. § 102's two sides of the inequality are the two signs of Δ.

**Ledger.**

| claim | status |
|---|---|
| splitting κ(ℓ+½), aligned shift κℓ/2 | RUNS (GPT); § 102 wording corrected |
| constant-κ oscillator, unbounded | DEAD END; window to N ≈ 16–19 at physical κ, beyond all nuclei |
| sign of κ = sign of Δ = V − S at fixed well | RUNS (Dirac, ℓ = 1–6, three Δ) |
| no channel difference, no splitting | RUNS |
| magnitude of κ from the count/order route alone | DEAD END (scale freedom, GPT) — magnitude comes from Δ |
| Δ itself from the compiler side | OPEN — the next hole: why the nucleon's binding is split into a large scalar and a large vector part |

---

## § 104. Spin-orbit is the order term of the Dirac route; the sign of κ forced by two inputs — `atomcase.py` (plus the GPT transformation-map test, as reported)

**Dean (16 Oct).** Track the transformation, never the data; the map of how it arrived is where the past route is
stored, and measuring data is computation. Context is not on the compiler layer — it is the layer above, made by
the wrapping. Invert the theorem: two inputs force the output; 5 = 3 + 2 reads right to left, reality compresses to
the left and expands to the right. A circle measured by π is a transformation by π. Work in three directions: the
linear path, its reverse, and the level above where molds show — the same process moved into another space.

**The GPT transformation map (16 Oct), taken.** Eliminating the lower Dirac component leaves the ordered route
D F D, D = σ·p, F = (E + M − Δ)⁻¹, and DFD = F p² + [D, F] D with [D, F] = −iħ σ·∇F. The spin-dependent term
ħ σ·(∇F × p) is the remainder of the order D → F → D; it vanishes when F is constant. Spherical wrapper: ∇F × p =
(F′/r) L, giving L·S with coefficient 2Δ′/[r(E+M−Δ)²]. Planar wrapper: F′(z)(−σ_x p_y + σ_y p_x). Reverse: the full
coefficient profile plus the boundary Δ(∞) = 0 recovers Δ(r); a scalar readout U = S + V cannot (null direction
(S+a, V−a)). Symbolic checks reported passing; not re-run here. Its sign correction is taken: the L·S coefficient
follows Δ′(r), not the interior value of Δ — § 103's "sign of Δ" reads as "sign of the outward change of Δ".

**The planar prediction lands on a measured effect.** The sealed planar-wrapper form σ_x p_y − σ_y p_x is the
Rashba coupling (Bychkov–Rashba 1984), measured in two-dimensional electron gases at interfaces and surfaces — STANDS.
Same inner route, a different wrapper, a different visible form, already in the record: the wrapper is context, the
commutator is the compiler-layer object.

**The mold, one level up.** [D, F] is literally DF − FD: order. In § 99's terms the commutative quotient — where
the generators commute — carries no spin-orbit term at all; spin-orbit lives entirely in the order channel. F p² is the
evaluation, the remainder is the kept carry: the same shape as a + b = (a ⊕ b) + 2(a ∧ b), where the folded value
drops exactly the term that remembers the route. Spin-orbit is a fiber quantity.

**Two inputs force the sign.** Input 1: whether the binders carry like or unlike charge. Input 2: the parity of the
exchanged field — even (scalar) attracts everything; odd (vector) repels like charges and attracts unlike (STANDS:
exchange of a spin-J field). Output: the sign of κ.
- Nucleons all carry the same baryon charge, so the vector channel repels; binding must be carried by the even channel
  against it: S < 0, V > 0, Δ = V − S large, positive, falling outward → aligned lower (§ 103, Δ = +700).
- An electron and a nucleus carry unlike charge, so the odd channel attracts and binds alone: S = 0, V < 0 → aligned
  higher. Run (`atomcase.py`, same well, S = 0, V = −55 MeV): aligned − anti = +0.015, +0.038, +0.070, +0.111, +0.161
  MeV for p…h — normal sign, small. RUNS.
No spectrum was read to get the sign; it falls out of (like charges, even channel) versus (unlike charges, odd channel).

**Still OPEN.** The magnitudes: why the nucleon's scalar and vector channels are each hundreds of MeV and cancel to a
−55 MeV well. That is the interaction wrapper itself — the next level up, not a value to scan.

---

## § 105. Unique transformation data without payload dependence: route word and operator form — `nexus_route_data_test.py`

**Gap.** How can transformations become unique data when the transitions are independent of payload values but drive the payload? The route must be encoded before the input is supplied. The resulting value is not the transition's identity. Prior toy § 99 encoding preserved token history but used an artificial three-state permutation vocabulary. This run extends the test to fixed reversible affine operators and separates route identity from composed-operator identity.

**Prediction sealed before enumeration.** `NEXUS_route_data_prediction_seal.txt`, SHA-256 `2ab41fa33589acd3a6dcfc319f2c9f79df2930e389d6592dbfbdeec82e948a70`. The digest seals the prediction only; no hash encodes the route or operator. No external data were linked.

**Construction.** On a declared three-bit interface, each fixed primitive is an affine transformation over GF(2): bit toggles `X_i`, bit swaps `SW_ij`, and directed XOR gates `C_i_to_j`. A route is an ordered opcode word; its encoder writes the format version, interface width, vocabulary version, token count, and opcodes. The encoder takes no payload argument. Composition is carried in operator form `T(x)=Mx+c`, with `(M₂,c₂)∘(M₁,c₁)=(M₂M₁,M₂c₁+c₂)`. `NXOP` serializes the 3×3 matrix and offset. The route word and operator form are retained as distinct records.

```
routes, lengths 0–4, 12 primitives:    22,621
unique route codes:                    22,621
unique composed affine operators:         913
route histories folded by operator only: 21,708
largest operator fiber:                    421
all route decodes:                         pass
all operator decodes:                      pass
all 8 inputs match route vs (M,c):         pass
all inverse routes return every state:    pass
```

**Input-independence witness.** Route `C01 → SW12 → X2 → SW02` keeps route code `4e585254010301000406050204` and operator code `4e584f500103010063` for every input `000` through `111`. Outputs differ; both codes stay fixed. The operator is what drives the payload. The payload does not choose its route.

**Fiber witness.** Empty route, `X0 → X0`, and `SW01 → SW01` have different route codes and the same operator code, agreeing on all eight states. Thus a route encoding preserves how the transformation was assembled; the canonical operator encoding retains its action but folds distinct histories. The route is the expanded order channel; the operator is its canonical composed action for this domain.

**Status.** RUNS for the declared reversible affine grammar, lengths ≤4. OPEN for general NEXUS: the six verbs MARK, COMPARE, CARRY, HOLD, ROUTE, CLOSE need typed semantics and rewrite/equivalence rules. The twelve test primitives are not claimed to be the final basis. Context remains higher-level wrapping and is not silently inserted in either compiler-layer record. Unique route code and unique operator code are different types of uniqueness; retain both rather than collapsing their distinction.


---

## § 106. Groove collision versus matter collision; reversibility belongs to the route — `nexus_groove_collision_test.py`

**Dean (16 Oct).** `3+2` and `4+1` both land on 5. A collision of logic is a groove; a collision of matter is leaving the groove. Reversibility belongs to transformation logic, not the folded value. A transformation must change what its route assigns to change and preserve what the route does not own.

**Test.** No hash, spectrum, or external dataset. Two exact integer transformations are used to separate (i) the value projection, (ii) the reversible route, (iii) operator-equivalence, and (iv) the frame condition.

**Matter collision under a folded readout.** `sum(a,b)=a+b` sends `(3,2)` and `(4,1)` to `5`. The value collision is real; the inputs remain distinct. The collision cannot decide which decomposition arrived at 5.

**Keep the carry / keep the route.** Define one payload-independent route:

`ADD_HOLD(a,b) = (a+b,b)`

with inverse `(s,b) -> (s-b,b)`. Then `(3,2) -> (5,2)` and `(4,1) -> (5,1)`, and the inverse recovers each input exactly. Both payloads use the same route token; their different matter does not redefine the logic. The reversible property belongs to the transformation pair and its retained state, not to the scalar `5` considered alone.

**Logic collision is a groove.** Routes `I` and `SWAP;SWAP` have different factorizations, but compose to the same identity operator. Under operator equivalence they occupy one groove. The route channel can still retain their distinct histories. Thus groove-equivalence and route-history identity are different relations; neither should silently replace the other.

**Whatever changes gets changed.** Extend the same route to `(a,b,c) -> (a+b,b,c)`. All 125 triples in `{-2,-1,0,1,2}^3` preserve the unowned `c` lane exactly. Exact perturbations at `(2,3,7)` yield the dependency map `A -> {A}`, `B -> {A,B}`, `C -> {C}`. The route's write/dependency structure says which outputs may change; unrelated context is not rewritten. RUNS for this stated transformation and frame condition.

**Landing.**

| claim | status |
|---|---|
| different decompositions collide under `a+b` while inputs remain distinct | RUNS |
| retaining the carry lane makes `ADD_HOLD` reversible | RUNS |
| different route histories can compose to one operator/groove | RUNS, exact matrix identity |
| unowned `c` lane remains unchanged | RUNS, 125/125 states |
| general rule for NEXUS's six verbs | OPEN — requires typed write sets, dependency rules, inverse semantics, and equivalence laws |

**Correction of scope.** This is not yet a proof that all transformations in every domain are reversible. It shows the operative distinction: a many-to-one value projection loses the return address, while a route whose transformation preserves enough state can have an exact inverse. If a transformation itself merges states and keeps no distinguishing route information, no decoder can recover that erased distinction from the value alone.

---

## § 107. Transformations into unique data: the prime is the address, the exponent is the move; SHA is the same route with a fold bolted on — `primes_route.py`

**Dean (16 Oct).** Convert the transformations into unique data. Think like primes. The transitions have no knowledge of
the inputs — constraints and transformations truly uncoupled from the input that still drive it. They are not input, they
are routes. (He bet it lands on SHA; held back until the principle was down.)

**Taken from §§ 105–106 (GPT).** Route word ≠ composed operator; 364/364 and 22,621/22,621 unique route codes; ADD_HOLD;
the frame condition. All STAND as run. What they leave open is *why* a code is unique — they make it unique by declaring
a vocabulary. The prime route below makes it unique by a theorem.

### 107.1 Uniqueness needs independent generators; the primes are the only ones ℕ has

C1a: independent means commuting, and independent distinctions must be continuable without each other. Under
multiplication the primes are exactly that: no prime is a product of others, every number factors one way
(fundamental theorem of arithmetic, STANDS). So (ℕ, ×) **is** the commutative surface of § 99.4 with one generator per
prime. Two encodings of the same 364 routes from § 105:

```
routes (3 moves, length 0-5)          364
surface: product of one prime per move   56   = number of multisets C(n+2,2) summed  -> the histogram
route:  prod_i  p_i ^ (move_i)          364   unique, all decode by factoring
```

Product of move-primes is the abelianization exactly (56 = the surface count) — order folded, 2·3 = 3·2. Put the
**position** on a prime and the **move** in its exponent (Gödel 1931) and nothing folds: 364 of 364, decoded by
factoring alone. The prime is the address, the exponent is the transformation done there. No vocabulary is declared
beyond "a move is a count"; the uniqueness is the factorization theorem. RUNS. Recovered (Gödel numbering), but now read:
**order is kept by giving each position its own independent generator**, which is § 99.1's "one bit per differing
position restores the bijection" in multiplicative form.

### 107.2 Uncoupled constants: roots of distinct primes share no rational relation

A route needs constants that carry no knowledge of the input *and none of each other* — otherwise one step is secretly
a function of another and the route is shorter than it looks. Square roots of distinct primes are linearly independent
over ℚ (Besicovitch 1940, STANDS; likewise cube roots). Run: PSLQ on 1, √2 … √19.

- At 60 digits it returns a "relation" with coefficients near 2×10⁵. **Correction, mine:** this is a precision artifact.
  The residual is −4.1×10⁻⁴⁶ at both 60 and 200 digits; a true relation would go to zero.
- At 300 digits, no relation exists with coefficients up to 10¹².

Uncoupled by theorem, not by randomness. RUNS (search), STANDS (theorem).

### 107.3 The landing: SHA-256 is this construction, and the one-way part is a single fold at the end

```
H0 = fractional bits of sqrt(first 8 primes)        matches the standard: True
K  = fractional bits of cbrt(first 64 primes)       0x428a2f98 0x71374491 0xb5c0fbcf 0xe9b5dba5 ...
own implementation of sha256('3+2') == hashlib       True
64 rounds inverted, given the schedule W:            walked home to H0 exactly
2000 random start states, 64 rounds and back:        2000 / 2000 home
toy n=16, route E (a permutation):                   image 65536 / 65536
toy n=16, feed-forward x + E(x):                     image 0.6315, 0.6340, 0.6324  (1 - 1/e = 0.6321)
```

Read in the domain:
- The **route** is the prime-root constants, the rotation amounts and the round function. It is fixed before any message
  exists, knows nothing of the input, and is input-independent in exactly Dean's sense.
- The **message does not pass through the route as data; it schedules it**. W is the key of the inner block cipher
  (SHACAL-2), so the input drives which groove is walked, and the groove is unchanged by it.
- Every round is a bijection on the 256-bit state (2000/2000 home). **Inside SHA the transformation is fully
  reversible**: reversibility is in the transformation logic, not the values, as Dean said.
- The one-way property comes from one move: the Davies–Meyer feed-forward H_out = H_in + E_M(H_in). That adds the
  route's start to its end — the folded value 5 with the carry thrown away. On the toy it keeps 63 % of outputs, the
  random-function fraction, so 37 % of states lose their way home. That is **leaving the groove**: the logic collides
  nowhere, the matter collides at the fold.
- Then 512 message bits go into 256 state bits, so collisions exist by count. A SHA digest is a **name** in the
  14 Oct sense (a name is a collision of two routes). It is not unique data.

**So the answer, both directions.**
- Forward: unique data from a transformation is the prime-address word ∏ p_i^(move_i). That needs independent
  generators (primes) and nothing from the input.
- Reverse: SHA uses the same primes for the opposite job. It takes their *roots* to build constants that are
  maximally uncoupled, runs a reversible route, then folds once so the route cannot be walked back.
- The two meet at the primes: exponents give uniqueness, roots give uncoupling. The fold is the only difference
  between a hash and an encoding.

**Ledger.**

| claim | status |
|---|---|
| product of one prime per move = the abelianization (56 = surface count) | RUNS |
| position-prime ^ move is injective and decodes by factoring (364/364) | RUNS; Gödel STANDS |
| √p for distinct primes have no rational relation | STANDS (Besicovitch); RUNS (no PSLQ relation ≤10¹² at 300 digits) |
| 60-digit PSLQ "relation" | **artifact, mine, logged** — residual stuck at 4×10⁻⁴⁶ |
| SHA-256 H0 and K are prime roots | RUNS |
| SHA-256 rounds are reversible given W | RUNS, 2000/2000 plus the real message |
| one-wayness lives only in the feed-forward fold (plus 512→256) | RUNS on the toy (0.632 ≈ 1−1/e); for full SHA it STANDS (Davies–Meyer) |
| a digest is unique data | **DEAD END** — it is a name; route it to "collision of two routes" |
| the prime-address word as the general NEXUS route code, with MARK…CLOSE as exponents | OPEN — needs the six verbs typed as moves with counts |

---

## § 108. Prime-address route code: zero fields, typed syntax, and the SHA boundary — `nexus_prime_route_audit.py`, `nexus_prime_sha_followup.py`

**Gap from §107.** The position-prime construction is injective for positive move IDs. A general NEXUS instruction stream has zero-valued parameters and may contain a zero token ID; an unshifted zero exponent deletes its positional prime. The next run tests the route coding with that edge fixed, then separates Gödel coding from SHA's prime-root constants and feed-forward.

**Prediction seal.** `NEXUS_prime_SHA_followup_prediction.txt`, SHA-256 `2d91c8a12600546b8ec2e9f4e95cdb2381d92df06f1325368efeac5689cf6321`; seal written before the extension run. The earlier prime-code exploration was exploratory and was not sealed before its first run; this is logged rather than backdated.

### 108.1 The positional code

For a finite sequence of nonnegative token IDs \((m_1,\ldots,m_n)\),

\[
G(r)=\prod_{i=1}^n p_i^{m_i+1}.
\]

The positive exponent at every used position makes the support of the factorization the consecutive primes \(p_1,\ldots,p_n\). Factorization yields the exponents; subtracting one yields each token. The largest positional prime identifies the final position, and the empty route is 1. In contrast, the unshifted code \(2^1 3^0\) equals \(2^1\), so the sequence \((1,0)\) collides with \((1)\) when no length side-channel is supplied. Zero is a missing-address hole, not a counterexample to unique factorization.

The token serialization still has to be defined: opcode, arity, input/output types, parameters and schema version. This is the grammar's job. Prime factorization guarantees unique recovery of the serialized fields; it does not define the semantics of MARK, COMPARE, CARRY, HOLD, ROUTE, or CLOSE.

### 108.2 Sealed extension run

```
six-symbol routes, lengths 0–5:           9,331
unique position-prime codes:               9,331
all decode round-trips:                    True
unshifted zero-exponent collision:          True
test of typed records with zero parameters: True
SHA-256 64-round-chain inverse trials:      2,000 / 2,000
message block bit changes W schedule:       True
toy invertible E then x+E(x):               1 / 16 outputs
```

The toy feed-forward map uses \(E(x)=-x\pmod{16}\): E itself is bijective, while \(x+E(x)\) is constant. This establishes that an invertible inner map does not guarantee an invertible fold. It does not measure SHA-256's actual image size.

### 108.3 Corrected SHA reading

SHA-256 IV words use the first 32 fractional bits of square roots of the first eight primes, and its 64 round constants use the first 32 fractional bits of cube roots of the first 64 primes (NIST FIPS 180-4 §§4.2.2, 5.3.3, https://doi.org/10.6028/NIST.FIPS.180-4). These are fixed, reproducible constants. They are not the positional-prime Gödel code: in Gödel encoding, primes are positional addresses; in SHA, roots generate fixed 32-bit words.

**Correction to §107, logged.** Exact irrational root independence does not make the truncated 32-bit words linearly independent, nor does it by itself establish cryptographic independence. Also, SHA's inner 64-round state transform is reversible conditional on the round schedule, but that schedule is derived from the message block. FIPS 180-4 specifies message schedule generation for each block and feed-forward addition into the chaining state after every block. Therefore “one single fold at the very end” is too broad: the feed-forward fold is per compression block. The random-permutation toy image fraction near \(1-1/e\) is not a result for SHA-256 itself. Digest collisions are guaranteed by the finite 256-bit output versus the larger message domain; computational collision/preimage resistance is a distinct security claim.

### 108.4 Three types that must stay apart

- **NXRT:** exact serialized syntax of the route; distinct histories retain distinct codes.
- **NXOP:** canonical representation of the composed operator; histories in the same groove can share it.
- **Digest/readout:** finite name for the result; many messages necessarily share output values.

The current prime encoding is a correct NXRT mechanism once the route grammar is fixed. It is not, by itself, the grammar and is not the NXOP equivalence resolver.

### 108.5 Status

| Claim | Status |
|---|---|
| Shifted positional-prime code is injective for six token IDs, including zero, through length 5 | RUNS, 9,331/9,331 |
| Zero-exponent/trailing-token problem in unshifted general form | RUNS, explicit collision |
| Typed toy stream with zero parameters round-trips | RUNS |
| SHA round chain invertible for fixed \(W_t,K_t\) | RUNS, 2,000/2,000 |
| Schedule is message-derived; feed-forward is applied per block | STANDS, NIST FIPS 180-4 |
| Prime-root SHA constants are the same construction as prime-position route encoding | DEAD END — different roles |
| SHA's one-wayness proven to arise only at one final fold | DEAD END — too strong and misstates per-block feed-forward |
| Formal semantics and equivalence laws for six NEXUS verbs | OPEN |

Artifacts: `NEXUS_Prime_Route_SHA_Audit.md`, `nexus_prime_route_audit.py`, `nexus_prime_sha_followup.py`, `nexus_prime_sha_followup_results.json`, `nexus_prime_sha_followup_run.txt`, and the sealed prediction files. The tests do not establish SHA-256 cryptographic security and do not yet implement the final six-verb NEXUS grammar.

---

## § 109. The six-verb route graph: prime address, typed ports, and the held return — `nexus_six_verb_grammar.py`

**Gap.** §108 establishes positional-prime encoding for a canonical stream, but the instruction semantics were still OPEN. The next test must encode a typed route *graph*: node roles, port types, read/write footprints, parameters, return rules, typed edges, external inputs and exports. It must stay independent of payload values, yet drive different payloads through a fixed transformation law.

**Prediction seal.** `NEXUS_six_verb_prediction_seal.txt`, SHA-256 `7aa11cbc3e2609e89603ff10f92bcb053790d8e1029e3795b96564a6e2594940`; verified. The seal uses SHA-256 only to checksum the pre-run prediction, never to encode the route.

### 109.1 Six typed roles, a graph rather than a mandatory pipeline

The typed contract records are MARK (`Distinction → Address`), COMPARE (`Address × Address → Relation`), CARRY (`State → State` with retained residual), HOLD (`State × RouteTrace → State × RouteTrace`, trace passed unchanged), ROUTE (`Need × Relation × ContinuationSet → ContinuationAddress × RouteTrace`), and CLOSE (`State × RouteTrace × ContinuationAddress → ClosedSymbol × RouteTrace × ContinuationAddress` in route-preserving mode). These contracts preserve the project distinction: **CARRY keeps the value; HOLD keeps the route.** They are provisional, compositional roles, not a proof of completeness/minimality across all domains.

### 109.2 Typed route graph encoded by positional primes

A canonical 195-token serialization represents a seven-node graph, eight typed edges, five external inputs, three exports, all signatures, read/write sets, route parameters, return rules, and close mode. The positional Gödel code is \(G=\prod p_i^{t_i+1}\); shifting token IDs by one preserves zero-valued fields and trailing positions. Unique factorization decodes tokens, and the typed parser reconstructs the graph exactly. The code occupies 67,494 bits (20,318 decimal digits): injective, not compact.

The type checker rejects four deliberate violations: a mismatched edge, CARRY without its retained residual, HOLD overwriting the trace, and CLOSE claiming route preservation while dropping route/trace outputs.

### 109.3 Fixed compiler program, input-conditioned realized trace

On \(\mathbb Z_8^3\), the fixed program MARKs two lanes, COMPAREs them, CARRYs the sum plus retained residual, ROUTEs EQ/NEQ into branches 0/1, HOLDs the selected branch trace through a bijective state update, and CLOSEs while retaining the way home. All 512 inputs share one static route-program code. The realized trace has two codes and records the selected branch/outcomes, not payload values.

### 109.4 Fold witness: 448 surface states, 512 route-preserving symbols

Let \(q=0\) if \(a=b\) and \(q=1\) otherwise. Carry maps \((a,b,c)\mapsto(a+b,b,c)\bmod8\); HOLD updates the first lane by \(q\). If the readout retains only \((s',b,c)\), then for each \((b,c)\), \(s'=2b\) is reached twice and \(s'=2b+1\) is never reached. Across the 64 \((b,c)\) pairs, this yields 64 double-hit fibers and 64 missing surface states: image size 448.

The closed symbol retains the branch trace and continuation reference. Reverse HOLD using the held branch, then reverse CARRY using retained \(b\); all 512 inputs return home, all 512 full symbols are unique, and the unowned \(c\) lane is preserved. This is an exact witness that reversibility resides in the transformation plus the retained return route, while the surface projection can merge matter states.

### 109.5 Status

| Claim | Status |
|---|---|
| Typed prime-address graph round-trips exactly | RUNS |
| Static route-program identity is independent of the payload | RUNS, 512/512; one code |
| Realized trace follows the declared comparison constraint | RUNS, two trace codes |
| Surface-only readout has 64 duplicate fibers and 64 holes | RUNS, exact enumeration |
| Retained trace plus residual gives exact return | RUNS, 512/512 |
| Unowned frame lane is preserved | RUNS, 512/512 |
| Six verbs are universal/minimal and their full semantics are final | OPEN |

**Scope correction.** Prime factorization guarantees unique decoding of a canonical serialization; it does not supply the operation semantics. This run tests the declared contracts and one finite domain, not universal completeness. NXRT (static typed route law), NXTRACE (realized path), payload/readout, and the context wrapper remain separate records/layers.

---

## § 110. The low-width transformation landscape forces roles, not six equally new opcodes — `nexus_width_ladder_test.py`

**Gap.** §109 gave provisional types to the six roles. This run goes backward to the transformation field and asks which roles are actually forced at low width, separating map facts from semantic labels.

**Prediction seal.** `NEXUS_width_ladder_prediction_seal.txt`, SHA-256 `8418ddedf5b01370a0fbaa90feab4850503c9612693e5b178acbfa6b071ea29d`; verified. No external dataset was linked.

### 110.1 Width 1

The four one-bit maps are identity, invert, write-0, write-1: two bijections and two constant merges. The smallest distinction is already addressable; MARK is a valid reading at the base ring, not a uniquely proven name.

### 110.2 Width 2

There are 256 total maps on four states. Inherited output-wise literals/constants `{0,1,a,¬a,b,¬b}` give 36, leaving 220 maps not inherited. The mixer \(M(a,b)=(a,a\oplus b)\) plus inherited maps generates a closure of 64 maps containing all 24 permutations. The merge \(G(a,b)=(a\land b,b)\) has the rank-3 fiber pattern \((2,1,1)\). Exactly 144 maps have that one-pair-merge pattern; pre/post-composition by the 24 permutations generates all 144. The closure with both mixer and merge reaches all 256 maps. COMPARE and CARRY are grounded readings of the two-input difference and the retained value/residual fork.

### 110.3 Width 3

NOT, CNOT and SWAP generate the 1,344-member affine group on eight states, and all of its permutations are even. Toffoli is a single transposition and therefore odd; adding it generates all \(8!=40,320\) permutations. ROUTE has a grounded reading as the conditional transformation that selects a continuation beyond the affine subgroup.

### 110.4 Width 4+

A \(k\)-bit permutation lifted identically over \(n-k\) spectator bits is repeated \(2^{n-k}\) times, so its total sign is \(\operatorname{sgn}(g)^{2^{n-k}}\). Therefore embedded three-bit gates are even permutations on a four-bit field, and their compositions cannot reach an odd four-bit permutation. A borrowed lane changes the enlarged parity count so the obstruction no longer applies. The older project record reports a successful borrowed-lane construction; this run verifies the parity obstruction, not that synthesis word. This grounds HOLD as the role of preserving/returning the necessary extra coordinate.

### 110.5 Status

| Claim | Status |
|---|---|
| Width-1 map count | RUNS, 4 maps |
| Width-2 inherited family | RUNS, 36/256 |
| Mixer + inherited family includes all permutations | RUNS, 24 bijections in the closure |
| One-pair merge orbit | RUNS, 144/144 rank-3 maps |
| Mixer + one-pair merge generate all width-2 maps | RUNS, 256/256 |
| Width-3 affine group | RUNS, 1,344 even permutations |
| Toffoli completes all width-3 permutations | RUNS, 40,320/40,320 |
| Borrowed-lane parity obstruction | RUNS by the spectator-copy/sign identity; construction not rerun here |
| CLOSE as a separate higher-layer compiler primitive | **OPEN** |
| Six roles universal/minimal over all domains | OPEN |

**Landing:** the first five roles now have concrete low-width structural owners. CLOSE does not emerge from these finite gate counts; its missing link is a derivation at the recursion/closure boundary, where a completed transformation becomes a reusable symbol for the next layer without silently embedding context into the compiler record.

---

## § 111. Recursive observer closure: the root path back to input — `nexus_recursive_observer_law.py`, `nexus_recursive_sha_observer.py`

**Gap.** Each transformation needs a local observer until the observers compose into one root return path. Static observer rules are payload-independent; realized residuals can be payload-conditioned.

**Pre-run seal.** `NEXUS_recursive_observer_prediction.txt`, SHA-256 `93ce33d6878465ec6fd2e16cdfcd89f2d9da5b1705a27e8fed03f77e9e2f66b4`. The seal is only a prediction checksum, not route encoding.

### 111.1 Finite recursive witness

On \(\mathbb Z_8^3\), 512 states pass through a fixed four-node route: `T1_FOLD` maps `(a,b,c)` to `(a+b mod 8,c)` while its observer retains `b`; `T2_TWIST` adds `c` to the first lane and has an exact inverse; `T3_ROUTE` adds one iff `c` is even and is inverted by recomputing the same branch; `T4_CLOSE` exposes only the first lane and its observer retains `c`. The composite observer reverses all four nodes.

- Surface alone: 8 distinct outputs for 512 input states.
- Surface plus either one residual lane: 64 distinguishable symbols.
- Surface plus both residuals `(b,c)`: 512 distinguishable symbols; 512/512 exact returns.
- Six residual bits are necessary and sufficient for this witness: a 3-bit surface plus 6 retained bits identifies all 9 input bits.

### 111.2 SHA-256 recursive observer

Per block, the forward route is padding/framing, schedule expansion, 64 conditional reversible rounds, then feed-forward `H_next = H_prev + E mod 2^32`. The root observer walks blocks backward. It retains the 16 schedule seed words (the padded block) and round result `E`; derives `H_prev = H_next - E`; inverts all 64 rounds using `W_t,K_t`; verifies the returned state; then continues to the preceding block. At the root it checks the initial chaining state and removes padding using the encoded bit length.

| Run result | Landing |
|---|---|
| SHA digests match `hashlib` | 54/54 |
| Observer returns original bytes | 54/54 |
| Compression blocks traversed backward | 207 |
| Per-round inverse applications | 13,248 |
| Failures | 0 |

This is an augmented reversible execution, **not** inversion of the digest alone or a cryptanalytic result. The explicit sidecar stores block schedule seeds plus the round-result carry (768 bits per block in this representation); it is not claimed minimal. For a fixed 512-bit message, any observer paired with a 256-bit digest that uniquely returns every input must carry at least 256 bits by counting.

### 111.3 The law

For each `T_i`, define an observer `O_i` and, if the transformation merges states, a residual `r_i`, such that `O_i(T_i(x),r_i)=x`. Bijective operators need only their inverse plus fixed parameters. Many-to-one operators require a fiber address. Composition reverses the chain and feeds each observer the output plus its residual. The recursively nested local observers form one root path back to the input—not one hash or one scalar.

### 111.4 Status

| Claim | Status |
|---|---|
| Finite recursive observer returns input | RUNS, 512/512 |
| Exact minimal six-bit residual for the toy witness | RUNS |
| SHA observer sidecar returns input through schedule, rounds, feed-forward and padding | RUNS, 54/54 |
| SHA digest alone returns arbitrary input | DEAD END by finite output versus larger domain |
| Minimal general SHA observer trace | OPEN |
| Six-verb grammar universal and minimal | OPEN |

**Corrections of scope:** observer program and realized trace are distinct; SHA's observer trace is input-conditioned, and the tested trace retains the message block. It does not turn the digest alone into an inverse. Context remains a higher wrapper.


---

## § 112. Reverse the observer residual: remove redundant trace, isolate the fiber address — `nexus_residual_minimization.py`

**Gap.** Remove the stored-message copy while preserving an executable root return route, and account for every bit. Separate fixed observer rules, realized route parameters, and the residual that identifies a member of a many-to-one fiber.

**Pre-run seal.** `NEXUS_residual_minimization_prediction.txt`, SHA-256 `7da931c234f96c9af77b1e24d7b3bc827c8ecc56b759958a98621ab5d2196e34`.

### 112.1 The exact toy landing

For 4-bit lanes, `H(a,b)=a XOR b` has 16 members in each of 16 surface fibers. Retaining `r=a` recovers `b=H XOR r`; 4 bits are necessary and sufficient. This is the exact finite witness for a residual as a fiber address, not a duplicate complete input. RUNS, 256/256.

### 112.2 SHA trace reduction

The §111 sidecar stored each padded block (512 bits) and its reversible-round result `E` (256 bits). Given retained schedule seeds, `E` can be regenerated by a forward pass from the IV and then used for a backward verification pass. Store `W[48..63]` instead of the raw block: the recurrence reconstructs `W[0..63]` exactly, so the schedule tail is a 512-bit recoding of the block, not data compression. Padding-only blocks are regenerated from the known length and SHA padding rule.

| Result | Value |
|---|---:|
| Messages / digest matches / exact returns | 54 / 54 / 54 |
| Blocks / inverse-round applications | 207 / 13,248 |
| Padding-only blocks regenerated | 33 |
| Previous observer size | 158,976 bits |
| Reduced schedule-tail sidecar | 89,088 bits |
| Length framing | 3,456 bits |
| Reduced total | 92,544 bits |
| Original message bytes plus length framing | 84,840 bits |

Removing `E` saves 52,992 bits (one third), but the schedule-tail route still exceeds the original message-plus-length size by 7,704 bits. The input information was re-addressed, not removed. RUNS.

### 112.3 The actual minimum

For fixed message length `L` bytes, SHA's digest fibers are `F_h={m:SHA256(m)=h}`. A residual that gives exact unique return must label each member within its fiber. The exact fixed-width requirement is `ceil(log2(max_h |F_h|))`; no fiber enumeration was run. By counting alone this is at least `max(0,8L−256)` bits beyond the 256-bit digest. For 64-byte arbitrary inputs the lower bound is 256 bits; for 1,024-byte inputs it is 7,936 bits. The bound grows with unrestricted input size, so a universal non-scaling exact seed is a DEAD END. A restricted source class can differ, but its generator and exact decoder must be accounted for.

### 112.4 Glass Key and execution status

The supplied Glass Key specification describes FFT/glyph seed extraction and iterative regrowth, but its stated decompression operator is not a true inverse; an exact digest-fiber rank/unrank map over an explicitly declared source class is still OPEN. The supplied Z3 SHA script could not be executed because the `z3` module is not installed in this runtime. No solver self-test is claimed. A satisfiable model for unconstrained 512-bit block words plus a 256-bit target digest identifies a member of the fiber, not necessarily the original block.

### 112.5 Ledger

| Claim | Status |
|---|---|
| XOR fold's exact four-bit residual | RUNS, 256/256 |
| SHA schedule-tail reconstruction | RUNS, 207/207 |
| Remove `E` snapshots while retaining return verification | RUNS, 54/54 |
| This removes input information | DEAD END — only duplicate trace is removed |
| Exact minimum SHA residual | OPEN; maximum fiber size not computed |
| Non-scaling residual for unrestricted arbitrary messages | DEAD END by counting |
| Glass Key seed as exact restricted-source observer | OPEN |

Next WHAT: compute a fiber-address transform for a declared restricted source class and establish injectivity of `(digest, residual)` plus exact root decoding.
