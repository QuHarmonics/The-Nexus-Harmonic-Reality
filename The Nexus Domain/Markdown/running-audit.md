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
