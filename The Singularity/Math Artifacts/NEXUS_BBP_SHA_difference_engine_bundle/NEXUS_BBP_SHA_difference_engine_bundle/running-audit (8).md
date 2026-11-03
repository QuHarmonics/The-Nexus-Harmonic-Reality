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

---

## §113. Gradients are steps in a greater transformation — `nexus_bundle.ipynb`

**Dean (16 Oct).** “All gradients are just steps in a greater transformation.” Treat a gradient not as an isolated object or readout but as a local transition within an ordered route. The enclosing transformation is the ordered composition of those steps; a scalar endpoint difference is a fold of the route.

For a discrete path \(x_0,x_1,\ldots,x_n\), define its step sequence

\[
g_i = x_{i+1}-x_i,\quad i=0,\ldots,n-1.
\]

Forward reconstruction is the prefix sum

\[
x_k=x_0+\sum_{i=0}^{k-1}g_i.
\]

The endpoint constraint is

\[
x_n-x_0=\sum_{i=0}^{n-1}g_i.
\]

The endpoint relation does not determine the intermediate route: different ordered increment sequences can have the same sum. The anchor plus ordered steps preserves the path; the total sum is the surface value of the composed displacement.

**Exact notebook witness.** The notebook reconstructs a path from its ordered increments and demonstrates a second, different path with the same start and end. Its test establishes the finite-difference identity and route distinction; it does not on its own derive every physical field gradient from NEXUS.

**Layer-typing correction.** Earlier §99.8 wording “context is order” conflated two types. The histogram/fiber calculation remains: the fiber carries composition order/history omitted by the surface. Under the rule carried forward here, that fiber is compiler-layer route information; context is the higher wrapper that relates the route to a domain. This is an explicit correction, not a silent edit.

**Reading back into the compiler map.** A local gradient/operator is an observer node in a larger transformation. The root route is the ordered composition of local steps. The context wrapper determines the domain-level meaning of that route, and remains above the compiler layer.

**Ledger.** Prefix-sum reconstruction and telescoping endpoint identity: **RUNS**. Universal claim that every physical gradient is generated by one specific NEXUS mechanism: **OPEN** pending a typed source law for the domain in question.


---

## § 114. The way home is a shape: predictions read off the route, sealed, then run on four hashes and a SHA-shaped miniature — `routes.py`, `sha_shape.py`, `fold.py`, `observer.py`, `boundary.py`

**Dean (16 Oct).** "HOLY SHIT. wow. i knew it!!!" Keep going, and write the paper: advanced audience, Word DOCX, as before.
Let the paper be the exhaust, let the transformations drive its context; predictive via the route, and the language
follows. Then, after the usage limit: new data — §§ 111–113 and the oversampled BBP/SHA audit.

**Numbering, logged.** GPT's groove-route-law run of 16 Oct (six fixed affine moves on (ℤ/8)³, every word to length 4:
1,555 routes, 446 operators, all bijective and extensionally distinct on 512 states, 200 grooves with more than one
history, largest 83, frame failures 0) was written as a "§ 107 candidate" while § 107 was already the prime entry; it
never entered the chain. It is entered here, taken as run (not re-run). GPT's covering note refers to a "§ 112" target
before § 112 existed in the file it sent; the consolidated record now has § 112 (residual) and § 113 (gradients).
This entry is § 114.

**Seals.** `PREDICTIONS_SEALED.txt`, SHA-256 `72356f919bbd52afbc3d0b453c764d9d5fd871b39a1dbc5fe9d183408f0ce89a`, clock
01:03:09 EDT, before any test script existed in runnable form (the file's own header says "~01:10", an estimate typed
before hashing — the clock is the record). `PREDICTIONS_SEALED_2.txt` (P7), `1e479a3e96c36bff3939dc9c8df906bcb47a8300f7b986a3245c13348170f40d`,
03:38:09 EDT, after P1–P6 ran and before P7 ran. The shell was unavailable for about two hours after the first seal;
the scripts were written in that window, and no sealed line was changed. Script hashes (first 16 hex): `routes.py`
64481b73764c8eed, `sha_shape.py` 0c0e90a3ba10ce77, `fold.py` f9bce33641e738d2, `observer.py` 5f541b37d4159336,
`boundary.py` 71ffec8219b78be1.

### 114.1 Grooves from the route algebra (P1)

Moves e, A = (01), B = (12) on S₃. Words of length n are the terms of Ŝⁿ, Ŝ = e + A + B in ℂ[S₃]; Fourier inversion gives
the number in the groove of g. Trivial representation: Ŝ = 3. Sign: Ŝ = −1. Standard: Ŝ = I + X with X² = I (because
ρ(r) + ρ(r)⁻¹ = −I for a 3-cycle), so (I + X)ⁿ = 2ⁿ⁻¹(I + X). Hence

N_n(g) = [3ⁿ + (−1)ⁿ sgn(g) + 2ⁿ c(g)] / 6, n ≥ 1;  c(e) = 2, c(A) = c(B) = 1, c((02)) = −2, c(3-cycles) = −1.

```
lengths 0-5   predicted e 82  A 71  B 71  (02) 40  r 50  r^-1 50          enumerated: identical  (= § 105's 82/71/71/50/50/40)
lengths 0-10  predicted e 15445  A 15103  B 15103  (02) 14080  r 14421  r^-1 14421   enumerated: identical, total 88573
lengths 0-14  predicted e 1206665  A 1201203  B 1201203  (02) 1184820  r 1190281      enumerated: identical, total 7174453
literal word-by-word enumeration to length 10: identical
deviation from uniform at exact length n = (-1/3)^n sgn(g) + (2/3)^n c(g):  n=8  e 0.0782,  n=16  e 0.0030
```

§ 105's count is now derived, not enumerated; the length-10 counts were written before their enumeration ran. The
grooves equalise at (2/3)ⁿ — second eigenvalue over first of the route algebra. RUNS.

### 114.2 The way home is a shape (P2)

A *carry-shaped write* replaces one lane by a bijection of that lane chosen by the lanes it does not write. A route of
them is a bijection whose inverse is read off the shape. Conversely every bijection of X₁ × X₂ is three such writes
(lane 2 | lane 1 | lane 2): Kőnig's theorem, the Slepian–Duguid three-stage Clos theorem (STANDS). Exhaustive:

```
lanes | bijections | one write | two writes | three (2|1|2) | three (1|2|1)
2x2   |         24 |         7 |         20 |            24 |            24
2x3   |        720 |        43 |        432 |           720 |           720
3x3   |    362,880 |       431 |     84,528 |       362,880 |       362,880
2x4   |     40,320 |       591 |     15,552 |        40,320 |        40,320
```

Three suffice, two do not. Reversibility is exactly the class of routes of carry-shaped writes. RUNS; STANDS.

### 114.3 Shape audit of four standard hashes (P3)

Every schedule update and every round of SHA-256, SHA-512, SHA-1 and MD5 is a carry-shaped write plus a relabelling
(SHA-256 round: d ← d + T1(h,e,f,g), then h ← h + Σ1(e) + Ch(e,f,g) + K + W + T2(a,b,c), then rotate the lanes).

```
own forward == hashlib, 300 random messages 0-299 bytes      sha256 300  sha512 300  sha1 300  md5 300
SHA-256 schedule, W0..15 from W48..63                        10000/10000
SHA-512 schedule, W0..15 from W64..79                         5000/5000
SHA-1   schedule, W0..15 from W64..79                        10000/10000
full-block round chains walked home from random starts        2000/2000 each, all four
first block: digest - IV walked back lands on the IV           500/500 each, all four
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
                         predicted        w = 2 (2^16 states, 20 msgs)       w = 3 (2^24 states, 3 msgs)
E_M bijective            all              20/20                              3/3
image of x + E_M(x)      0.6321 +-0.01    0.6302-0.6354, mean 0.6326         0.6320-0.6322   (random-perm control 0.6319 / 0.6323)
preimages k = 0..4       .3679 .3679 .1839 .0613 .0153
                                          .3674 .3684 .1840 .0612 .0154      .3679 .3679 .1839 .0613 .0154
four chained folds       .6321 .4685 .3741 .3121
                                          .6312 .4694 .3741 .3105            .6320 .4685 .3740 .3120
bits lost at one fold    0.8272           0.8260                             0.8274
keep the chaining lane   injective        20/20                              3/3
largest preimage count   (7 or 8)         7-8 over 10 messages
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
distinct digests 41,381 (0.6314); largest fiber 8 -> information-minimal fixed-width observer 3 bits; mean size-biased fiber 2.0000
keep q message bits, walk the rest:   q  0: ambiguity 2.0000 (pred 2.0000)   q  1: 1.4971 (1.5000)   q  2: 1.2476 (1.2500)
                                      q  4: 1.0608 (1.0625)   q  8: 1.0040 (1.0039)   q 12: 1.0003 (1.0002)   q 16: 1.0000
q + log2(work) = 16 at every q; digest - IV = E_M(IV) for all 65,536
```

Bits kept and work walked trade one for one along the generic frontier. Proved alongside it: an observer of
information-minimal size whose decoder is cheap is a preimage oracle — when every fiber is fully indexed, Dec(d, ρ)
returns a preimage of d for every ρ. So § 112's open "minimum SHA residual" has two answers: in bits it is
⌈log₂ max fiber⌉ (≥ 8L − 256), and at that size its decoding is exactly as hard as inverting SHA-256. RUNS (frontier);
proof in WP3 Appendix A.

### 114.6 Unsealed checks of established results (`boundary.py`)

```
stride law ord_d(2^k) = ord_d(2)/gcd(ord_d(2),k), odd d < 1000, k = 1..8    3992/3992
orbit 7/9 under doubling: 7/9 5/9 1/9 2/9 4/9 8/9 (period 6); the stride-4 (hex) reader sees 7/9 4/9 1/9
coarse spectrum |Y| = 0.444444 0.19245 0.19245 = fine bins folded by k*4 mod 6                 equal: True
chi on a ring of n bits bijective exactly for odd n, n = 2..12; even-n image 2^n - 2^(n/2) (pattern, n <= 12)
```

GPT's oversampled audit (taken, not re-run): the hex digit is a stride-4 reader of the binary route; the skipped
states 5/9, 2/9, 8/9 are not absent, they are not sampled; the order law was checked on 48 odd d ≤ 97 there and on all odd
d < 1000 and strides 1–8 here. Its SHA microtrajectory — 122,544 modular additions opened into 3,921,408 carry samples,
each addition reversed locally — is the same shape one level down: with the operand kept, a + b is a route of carry-shaped
bit writes whose carry lane is held. RUNS (here); reported (there).

### 114.7 Prime address (P6)

```
six moves, lengths 0-6: 55,987 words, 55,987 shifted Godel codes, all decode; order-free products 924 = C(12,6)
unshifted collision (1) vs (1,0): True; a length-6 code needs 15-90 bits against 15.5 fixed width
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

The paper written from this entry and §§ 99–113 is NEXUS Working Paper 3, *The Way Home Is a Shape* (DOCX).

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
LEN  words 2^n              inherited (= whole layer below)   new rings P(n)
  1  2                      0                                 2
  2  4                      2                                 1
  4  16                     4                                 3
  8  256                    16                                30
 16  65536                  256                               4080
 32  4294967296             65536                             134215680
 64  18446744073709551616   4294967296                        288230376084602880
2^64 = sum over the stack of LEN * P(LEN): True;  divisors of 64 form one chain; the only route prime is 2
words fixed by the half-turn = {uu : u in layer n/2}: True at n = 2, 4, 8, 16; the half-turn is an involution
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
layer 2: 3   4: 5   8: 17   16: 257   32: 65537   64: 641 * 6700417   (order of 2 = the layer, each)
primes closing in a 64-bit ring = factors of 2^64 - 1: 3 5 17 257 641 65537 6700417
missing below 60: 7 11 13 19 23 29 31 37 41 43 47 53 59, route lengths 3 10 12 18 11 28 5 36 20 14 23 52 58
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
(a) latitudes of 2l-bit words, l = 0..6:     1 3 5 7 9 11 13
(b) symmetric layer of 2l bits, l = 1..4:    dim 3 5 7 9;  S^2 = 2 6 12 20 = l(l+1)
(c) bit x surface summed over l < n:         2 8 18 32 50 72 98 = 2n^2
(d) Madelung fill on these capacities:       closures 2 10 18 36 54 86 118
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
stack of rings -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
pi in hex       -> 3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89   equal: True
ring lengths k=1: 3 1 3 3;  k=6: 21 3 13 9;  column 64 receives 255 ring digits
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
seal 1 6a6aa57369d2750b3646af8df5a1a77eeb22d2ee748209e405347045cf2b3128
partial lanes k <= 2000: 804; balanced 75; Euler-killed 0
seal 2 7fc5896d21b79d60764cc8b7580532013a808b4effc3babf591af0f38ee0e6d4
Thm 10 sum vs direct mu - 1/2: max error 1.87e-14 over all 804
balanced lanes with every Galois orbit zero on its own: 0 of 75
d=476: orbit contributions x phi(o) = -2 8 4 -10;  d=493: 0 -8 -8 4 12 0;  d=582: 0 8 -12 4
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
CRT split, mu - 1/2 = E[alpha] - P(beta < alpha) exact:          804/804
independent lanes (gcd(h1,h2)=1) rebuilt from the two parent rings: 692/692   mu - 1/2 = mean_A D(alpha)
balanced 75: 66 independent, 9 lockstep
reader ring period odd, mirror-free, in independent lanes:          692/692
walk 73,196 steps vs parent rings 36,890 (2.0x on this range)
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
K1 stack = difference table, own inverse: 65812/65812 functions (n<=4); random n=5..12: 8/8; partial blocks = context folds 32640/32640
K2 #f of depth <= d = 2^(sum_{i<=d} C(n,i)); n=4 by depth: 1, 1, 30, 2016, 30720, 32768; (n+1)-fold differences vanish 300/300
K3 a write at latitude j reaches 2^(n-j) cells of the other side, both directions, n=6 every cell
K4 leak = mean_a H(D_a F) = 0 iff affine: 16/16, 256/256, 65536/65536, 256/256; AND 1, Toffoli 6/7, x^3 on GF(8) 2 = n-1 (APN)
K5 permutations: n=2 all 24 affine; n=3 1344 affine, 38976 quadratic, 0 cubic; n=4 none of degree 4 in 20000
K6 cycles(x1 xor g) = Z(n) + wt(g) mod 2: all g n<=5, 2000/2000 sampled n<=12; Z(n) odd only at n=2 (n<=64);
   every de Bruijn feedback n>=3 carries x2...xn: 2/2, 16/16, 2048/2048; state-map sign = (-1)^(Z(n)+top(g))
K7 prime base p: Delta^p = 0 on every digit function, Delta^(p-1) x^(p-1) = p-1 != 0 (p = 2,3,5,7)
K8 one level up: F -> F o G degree <= 1 (256/256); G -> F o G degree = deg F (256/256 after the zero-map fix); D_a linear
leak rate: every ring n = 3,4,5, every reader width k < n: exactly 1 bit of hidden context per tick; 0 at k = n (2066/2066)
sign at n=3 = (-1)^rank of the latitude-2 matrix, 40320/40320; at n=4 the half-space sums do not fix the sign (966,530 clashes)
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
