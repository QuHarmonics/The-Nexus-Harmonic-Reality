# NEXUS running audit 8

Continues `running-audit-7.md` (§§ 197–198). The scripts for § 199 are printed in full in `running-audit-8-scripts.md`.

## § 199. The shape is the history: the laws run as a construction, force the fold and leave its order; past closure the next bit has no provider; on the chains they account for one register and nothing else — `shape_history.py`, `side199.py`

**Dean (29–30 Oct).** "shape is the Object. in the same way the rings are endless shape is also and its a full set too think meshes. your leaving that out instead seaching for values. well values COME from measuring shapes."
- It came with the prompt *THE SHAPE IS THE HISTORY*. Write and run the construction H₀ → H₁ → …:
  - execute a forced write;
  - mark several legal writes AMBIGUOUS, and a write with no provider OPEN;
  - fill no gap by convention;
  - derive the closure and the route home;
  - seal before the chains are read.
- Then (30 Oct) "continue", with a GPT note: a history fixes what can happen next; an interface with another history makes it happen (HISTORY → POTENTIAL → INTERFACE → TRANSFORMATION).
- Also attached: a NotebookLM transcript (*Universal Admissibility and Relational Topology*), three GPT audits of LM Studio's §167 RIS work, GPT's script for them, and a GPT note on reader-window widths. All read in full; their runnable claims are checked below.

**The laws.** All come from the record; nothing else enters.
- L0 cannot hold still: every step changes the word, the closing step included (C1).
- L1 full set.
- L2 no rewrite.
- L3 facing: slot N−1−a holds P(slot a).
- L4 successor: one slot at a time, and slot N−1 continues to slot 0.
- L5 boundary: slot 0 holds 0ⁿ. This is where the record's rings start. It is a choice, and the run shows what it decides.

**The run** (generator only; no chain data).
- n = 0: there is one word, and its only step is the identity, so L0 fails. No legal history exists. OPEN: nothing to move to.
- n ≥ 1 runs the same way at every width. The trace is printed for n = 0–5 and counted for n = 6–8.
  - Slot 0 is the boundary write.
  - Slots 1 … h−1 are AMBIGUOUS, with 2(h−1), 2(h−2), …, 2 legal words. The missing qualifier Q is an order on the untouched pairs and a choice of member.
  - Slots h … N−1 are FORCED, each owed by its facing slot.
  - Legal histories number 2^(h−1)·(h−1)!: 1, 2, 48 and 645,120 for n = 1–4.
  - For n ≤ 3, every ordering of the words with 0ⁿ first was filtered by the laws. The survivors are exactly the construction's set.
- **Closure is derived.** Slot N−1 is owed P(0ⁿ) = 1ⁿ, so the closing step is C.
  - Without L5 the closing step is C only when slot 0 holds a palindrome or an anti-palindrome (J(x) = C(x)): 4 of 8 words at n = 3, 8 of 16 at n = 4.
- **Route home:** unwrite slots N−1, …, 0 in that order; L2 makes every unwrite exact.
  - On the ring, forward from slot N−1 is one step, C; backward is the step masks in reverse.
  - Run on every history for n ≤ 4.
- **The forced shape**, the same in every legal history:
  - h facing rows share one slot sum, N−1. It is odd, so no slot faces itself.
  - The crease is two adjacent slots: no loop.
  - The open end closes by C.
  - On the n-cube mesh the gaps across the rows are fixed as a multiset: palindromic rows at gap n, the rest even (n = 5: {2: 8, 4: 4, 5: 4}).
- **Left open:** where each row sits. That makes the crease gap AMBIGUOUS, and every step weight except the closing one.
- **The record's rings, located.**
  - n ≥ 2: both seam branches are legal: the record's exchange (P(m), m) and the counter order (m, P(m)).
  - n = 1: the record's seam exchange writes 1 at slot 0, outside L5. Its only representative is 0, so its seam is its boundary.
- **The mesh layer**, measured over every legal history.
  - A mesh contact is a cube edge joining slots 3 or more apart around the ring.
  - A run is another such edge 1–2 slots along with the same slot sum (opposed) or the same slot difference (co-moving).
  - n = 3, 48 histories: co-moving share 0–1.00, and 4 histories have none.
  - n = 4, 645,120 histories: co-moving share 0.11–0.96, and **every history has a co-moving run**. Opposed share 0–0.96, and 128 have none.
  - So on the mesh a co-moving run is unavoidable at n = 4 and an opposed run is not. Neither share is fixed.
- **Past closure.**
  - Every word is written and L4 returns to slot 0, so no write remains. OPEN: the provider of a new bit.
  - If a new bit is provided, the closed history has to survive with its facings. Every uniform insertion of one or two bits was tried, n = 1–6.
  - No insertion keeps any palindromic row. Its partner is C, and C flips the new bits too, so these rows have no way home through a widening. They are the piece that moves.
  - One new bit keeps the other rows only at even n: at the centre, with either value. At odd n it keeps none.
  - Two new bits keep them at every n: mirrored places with equal values, ⌊n/2⌋ + 1 pairs of places × 2 values. The record's nesting 1·x·1 is one of them. Which one applies is AMBIGUOUS.

**Seal.**
- Generator output SHA-256 `7449637f07d5761df36c1336946b245cbbfc4e95abeed8b865f241dc8aa25973`. Seal text SHA-256 `28e2ea9c147549e074e4fe54228849e273e71c051b3cf853f780d1c2ace10178`.
- Both are printed before the chain file is opened. The full run's first 173 lines are byte-identical to the sealed run.
- **Revised before the read, mine.** My first G4 said co-moving contacts come only from the AMBIGUOUS order. The generator's dry run found no n = 4 history without a co-moving mesh run. So G4 was split before any chain read: a facing layer, tested, and a mesh layer, from which no chain number is predicted. The dry-run seal `a2ccd08d…` is superseded.
- Not blind: G1–G3 (seen in §§ 188 and 197).
- One reader fix after the seal: a chain with no residues crashed the reader and is now skipped. The generator and the seal are untouched.

**Read** (ecoli_chains.json, sha `f5266a44…`).

```
READER  chain file raw SHA-256 f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145
  chains 160, residues 0 in 1, under 30 in 2
  side note check: directed contacts 11747 (chains of 30+: 11747); donor i -> O(i-3): 2446; donor i -> O(i-4): 4902; donors with both O(i-3) and O(i-4) within 3.5 A: 4525; closure rule picks O(i-4) 3884, O(i-3) 641, another O 0; nearer of the two: i-4 3884, i-3 641
  hairpins (L >= 30): 143
  G1 one register: hairpins carrying a pair at S+-1 in their span 63 of 143 (in the crease 60, on the arms 4); pairs {'S-1': 56, 'S+1': 19}  -> outside the generator: 63; single-register hairpins: 80
  G2 edge-centred crease: odd S 94, even S 49  -> outside the generator: 49
  G3 no loop: crease pair s - e {3: 58, 4: 33, 5: 31, 6: 4, 7: 5, 8: 12}  -> outside the generator: 143 of 143 (the detector admits no pair closer than 3)
  G4 all 160 chains, 10583 stored pairs: co-moving 6623 (0.63), opposed 2090 (0.20), no run 1817 (0.17), both 53 (0.01)
     pairs in co-moving runs by j - i (top 8): {4: 4715, 3: 1211, 32: 31, 28: 29, 29: 28, 30: 25, 5: 24, 34: 24}  -> outside what the laws force: 6676 (0.63)
  G5 open end closed by C: chains are open, no counterpart.  G6: no residue-level claim made, none read.
```

- The last prompt's side note (GPT on LM Studio) reproduces exactly:
  - 11,747 directed contacts;
  - i+3 → i: 2,446; i+4 → i: 4,902;
  - both O within 3.5 Å at 4,525 donors, where the closure rule takes O(i−4) in 3,884 and O(i−3) in 641.
- **G1, one register:** 80 of 143 hairpins.
  - 63 carry a pair at S ± 1 in their span: 60 in the crease, 4 on the arms.
  - That is 56 pairs at S−1 and 19 at S+1, counted undirected. § 197 counted directed bonds: 60 and 30.
- **G2, odd S:** 94 hairpins; the 49 with even S lie outside.
- **G3, no loop:** every crease pair is 3–8 apart, so all 143 lie outside. The detector cannot see a closer pair, so this test could not land the other way.
- **G4, all 10,583 stored pairs in all chains:**
  - 0.63 co-moving (j − i = 4: 4,715; j − i = 3: 1,211);
  - 0.20 opposed; 0.01 both; 0.17 in no run.
  - The facing layer accounts for 0.21 at most.

**What the run says.**
- The laws build one closed fold. They bind through the one interface they carry, the mirror reader at slot sum N−1: every second-half write is that reader binding a first-half write.
- Everything else the run left open is interface data, not history:
  - **The order Q.** Read with the counter, the AMBIGUOUS writes give the record's counter-order ring exactly, n = 2–12. The record's own ring differs from that only at the seam pair (slots h−1 and h), which the record exchanges against the counter.
  - **The new bit past closure.**
  - **On the chains:** the facing offset S and its parity, the loop width, and a second register.
- A second facing offset cannot exist inside one closed history: R[S′ − a] = P(R[a]) = R[N − 1 − a] puts one word in two slots, against L1. So S ± 1 pairs, even creases and loops cannot come from one ring's history. They need a second history or an outside reader.
- That is GPT's HISTORY → POTENTIAL → INTERFACE → TRANSFORMATION, read off the run. The trace prints the potential at every write (the legal-set sizes); the interface is wherever the trace says Q or OPEN.
- Dean's mesh point lands as a measurement with a limit.
  - The shape on the cube fixes the gap multiset, and at n = 4 it makes co-moving runs unavoidable.
  - The share is a property of the order, which the laws leave open.
  - Values come from measuring a shape, and the laws give the shape's class, not the one shape.

**Side material** (`side199.py`; GPT's uploaded audit script run unchanged, in isolation).
- **§167 RIS, polyethylene C∞.** I built an independent nine-coordinate frame computation from the RIS definition (states t, g±; tetrahedral cos θ = 1/3).
  - It gives 2.000000000, 3.124392391, 6.229676328 and 7.200650328, and 6.715345190 with g+g− forbidden. These are the source's values to nine digits.
  - GPT's transcription of the §167 four-coordinate reader agrees with it to 1.1 × 10⁻¹² over 2,000 random (σ, ω). The reduction is exact.
  - LM Studio's numbers do not belong to its own parameters: they come out 3.122160835, 6.219869293 and 8.037816088, as GPT found.
- **2(2+σ)/(3σ) is C∞ only at ω = 1.** With both penalties at 413 K it gives 3.124 against 6.230. NotebookLM's Answers 18–20 present it as C∞ in general: DEAD END.
- **"C₂ splits the RIS operator into four uncoupled scalar channels"** (LM Studio; NotebookLM 18–20): DEAD END.
  - The mirror (g+ ↔ g−, z → −z) commutes with the 9 × 9 operator (‖[S, M]‖ = 6 × 10⁻¹⁶). It splits the operator into two blocks, of 5 and 4.
  - The four-coordinate matrices at 413 K and at 300 K do not commute (‖[A₁, A₂]‖ = 0.124), so no fixed basis of four uncoupled channels exists.
- **δ(Px) = rev(δ(x)):** 0 failures over 16,382 words, n = 1–13. STANDS, with a two-line proof:
  - off palindromes P = J, and the differences of a reversed word are the reversed differences;
  - on palindromes P = C, which changes no difference, and a palindrome's differences are palindromic.
- **Reader-window counts** (2^⌈w/2⌉ fixed, (2^w − 2^⌈w/2⌉)/2 exchanged) are exact for w = 1–8. They count palindromes: STANDS.
- **Sliding two-difference reader:** s_i(Px) = −s_(L−2−i)(x) with 0 failures.
  - It gives only 2^L − 1 of the 3^(L−1) ternary readings, and never +1 after +1. So it cannot write g+g+, a legal RIS pair.
  - As the torsion alphabet it is a DEAD END.
  - The disjoint two-bit code survives: 9,840 of 9,840 histories read back reversed with g+ ↔ g−. That is GPT's result, rerun independently.
- **What that code makes P mean physically.** Over 10,000 random atom quadruples, reversing the atom order keeps the signed dihedral (10,000 / 10,000), and a mirror flips it (10,000 / 10,000).
  - So under the two-bit code P is chain reversal composed with a mirror, not chain reversal. GPT's caution stands.
  - Where the tokens start (which differences pair) is the reader's offset: AMBIGUOUS, qualifier missing.
- **NotebookLM transcript.**
  - Answer 13's 41 records: none of its seven PDB ids is in the chain file. Its own Answer 14 already retracted them. DEAD END.
  - Q16's multi-donor count reproduces: 1,292 O acceptors chosen by more than one donor, in 157 chains. Its "11.00 % of all directed contacts" divides acceptors by contacts.
  - Answer 17's steric routine, run as printed, is planar (|z| ≤ 3.2 × 10⁻¹⁶), not 3D.
    - For [1,0,1,0] it gives next-0 collides and next-1 clear, as claimed.
    - [1,0,0,1] already self-intersects, so GPT's finding holds on this routine too.
    - For its own Case B, [1,1], next-0 collides (d_min 0), so the routine binds δ₃ = 1. The claimed "both clear, OPEN" was never run. DEAD END.
  - Answer 17's "route home" is the twisted-clock orbit of the finished word (011001 → 110011 → 100110 → 001100, length 4). It is not the inverse of the append; that inverse is unwriting δ₅. DEAD END as an inverse.
  - The O(n) rank formula and rectangle digit sum (Answers 3, 6, 9) show 0 failures against direct counts, n = 2–14. The 64-bit π word's address is 2,427,008,858,123,944,441, as stated. RUNS, as a rerun of the record.
  - The rest of the transcript restates the record (TP / PT conjugacy, run signatures, the C₀–C₅ chain, PULL items). H = π/9 is parked and not touched.

| claim | status |
|---|---|
| the laws as a history: boundary 1, AMBIGUOUS h−1 (qualifier Q), FORCED h, closure by C, route home | RUNS: n = 0–8, and n ≤ 3 against every ordering |
| legal histories 2^(h−1)·(h−1)! | RUNS: the product of the AMBIGUOUS counts |
| n = 0 is inadmissible (L0) | RUNS |
| closure by C is decided by L5 (a palindrome or anti-palindrome at slot 0) | RUNS |
| the record's ring is the counter binding of Q plus the seam exchange | RUNS, n = 2–12 |
| the record's builder at n = 1 sits outside L5 | RUNS; a note for the record |
| mesh layer: co-moving runs unavoidable at n = 4, share open | RUNS, 645,120 histories |
| past closure: the provider of a new bit | OPEN |
| palindromic rows: no uniform widening keeps them | RUNS, n = 1–6 |
| one new bit: even n only, at the centre; two: every n, mirrored and equal | RUNS, n = 1–6; which one is AMBIGUOUS |
| no second facing offset inside one history | STANDS (L1) |
| G1 one register | 80 / 143; 63 outside (not blind) |
| G2 odd crease | 94 / 143; 49 outside (not blind) |
| G3 no loop | 0 / 143; the loop width has no provider: OPEN (not blind) |
| G4 facing layer | 0.21 of stored pairs at most; 0.63 co-moving lie outside |
| history → potential → interface (GPT) | the run bears it out: the trace's Q and OPEN are the interface slots; the operator is not built: OPEN, next |
| the side note's counts (GPT on LM Studio) | RUNS, reproduced exactly |
| §167 C∞ values; the four-coordinate reduction is exact | RUNS, by an independent nine-coordinate computation |
| C∞ = 2(2+σ)/(3σ) in general; four uncoupled scalar channels | DEAD END |
| δ(Px) = rev(δ(x)); window counts | STANDS |
| the sliding reader as the RIS alphabet | DEAD END (no g+g+) |
| the two-bit code: P is reversal plus mirror on signed torsions | RUNS; a physical reading of P as chain reversal: OPEN |
| NotebookLM: Answer 13's landing, Answer 17's Case B, its τ route home | DEAD END |
| the O(n) rank formula and the π address | RUNS (rerun) |

**Generator output, sealed run** (`python3 -I shape_history.py`; script sha `5ef31d96…`, which includes the reader fix).

```
GENERATOR
  L0 cannot hold still: every step, the closing one included, changes the word.
  L1 full set: every word of width n is written exactly once.
  L2 no rewrite: a written slot never changes.
  L3 facing: slot N-1-a holds P(word in slot a).
  L4 successor: the history advances one slot at a time; slot N-1 continues to slot 0.
  L5 boundary: slot 0 holds 0^n, the word with no distinction marked (the record's rings start there).
  Q = an order on the untouched pairs and a choice of member (the record supplies a ranking convention; not used here)

=== width n = 0: 1 word ===
  H1   slot 0   e  BOUNDARY  L5. By L4 the successor of slot 0 is slot 0: the step is the identity.
  L0 fails: one word has nowhere to go. No legal history at n = 0.  OPEN: nothing to move to.

=== width n = 1: 2 words ===
  H1    s0   0       BOUNDARY  L5; owes s1 <- 1 | open 0 pairs, owed 1 | ret H0: unwrite s0 | state [0 (1)]
  H2    s1   1       FORCED    owed by slot 0 (L3) | open 0 pairs, owed 0 | ret H1: unwrite s1, xor m1 | state [0 1]
  CLOSE  slot 1 -> slot 0 by L4: step = 1 xor 0 = 1, all bits: C. Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.
  ROUTE HOME from H2: unwrite slots 1, 0 in that order; each unwrite returns H(t+1) to H(t) exactly, since L2 overwrote nothing. On the ring: forward from slot 1 is one step, C, to slot 0; backward is the 1 step masks in reverse order.
  SHAPE, forced in every legal history: 1 facing rows (slot a with slot 1-a), one slot sum 1, odd, so no slot faces itself; crease = edge 0|1, adjacent slots, no loop; open end = edge 1|0, closed by C.
  On the 1-cube mesh: facing-row gaps (bits that differ) {1: 1}: 1 palindromic rows at gap 1, the rest at even gaps; closing step weight 1.
  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. Writes 2: boundary 1, forced 1, AMBIGUOUS 0. Legal histories = product of the AMBIGUOUS counts = 1.

=== width n = 2: 4 words ===
  H1    s0   00      BOUNDARY  L5; owes s3 <- 11 | open 1 pairs, owed 1 | ret H0: unwrite s0 | state [00 . . (11)]
  H2    s1   x1      AMBIGUOUS 2 legal (1 pairs x 2), Q missing; owes s2 <- P(x1) | open 0 pairs, owed 2 | ret H1: unwrite s1, xor m1 | state [00 x1 (P(x1)) (11)]
  H3    s2   P(x1)   FORCED    owed by slot 1 (L3) | open 0 pairs, owed 1 | ret H2: unwrite s2, xor m2 | state [00 x1 P(x1) (11)]
  H4    s3   11      FORCED    owed by slot 0 (L3) | open 0 pairs, owed 0 | ret H3: unwrite s3, xor m3 | state [00 x1 P(x1) 11]
  CLOSE  slot 3 -> slot 0 by L4: step = 11 xor 00 = 11, all bits: C. Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.
  ROUTE HOME from H4: unwrite slots 3, 2, 1, 0 in that order; each unwrite returns H(t+1) to H(t) exactly, since L2 overwrote nothing. On the ring: forward from slot 3 is one step, C, to slot 0; backward is the 3 step masks in reverse order.
  SHAPE, forced in every legal history: 2 facing rows (slot a with slot 3-a), one slot sum 3, odd, so no slot faces itself; crease = edge 1|2, adjacent slots, no loop; open end = edge 3|0, closed by C.
  On the 2-cube mesh: facing-row gaps (bits that differ) {2: 2}: 1 palindromic rows at gap 2, the rest at even gaps; closing step weight 2.
  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. Writes 4: boundary 1, forced 2, AMBIGUOUS 1. Legal histories = product of the AMBIGUOUS counts = 2.

=== width n = 3: 8 words ===
  H1    s0   000     BOUNDARY  L5; owes s7 <- 111 | open 3 pairs, owed 1 | ret H0: unwrite s0 | state [000 . . . . . . (111)]
  H2    s1   x1      AMBIGUOUS 6 legal (3 pairs x 2), Q missing; owes s6 <- P(x1) | open 2 pairs, owed 2 | ret H1: unwrite s1, xor m1 | state [000 x1 . . . . (P(x1)) (111)]
  H3    s2   x2      AMBIGUOUS 4 legal (2 pairs x 2), Q missing; owes s5 <- P(x2) | open 1 pairs, owed 3 | ret H2: unwrite s2, xor m2 | state [000 x1 x2 . . (P(x2)) (P(x1)) (111)]
  H4    s3   x3      AMBIGUOUS 2 legal (1 pairs x 2), Q missing; owes s4 <- P(x3) | open 0 pairs, owed 4 | ret H3: unwrite s3, xor m3 | state [000 x1 x2 x3 (P(x3)) (P(x2)) (P(x1)) (111)]
  H5    s4   P(x3)   FORCED    owed by slot 3 (L3) | open 0 pairs, owed 3 | ret H4: unwrite s4, xor m4 | state [000 x1 x2 x3 P(x3) (P(x2)) (P(x1)) (111)]
  H6    s5   P(x2)   FORCED    owed by slot 2 (L3) | open 0 pairs, owed 2 | ret H5: unwrite s5, xor m5 | state [000 x1 x2 x3 P(x3) P(x2) (P(x1)) (111)]
  H7    s6   P(x1)   FORCED    owed by slot 1 (L3) | open 0 pairs, owed 1 | ret H6: unwrite s6, xor m6 | state [000 x1 x2 x3 P(x3) P(x2) P(x1) (111)]
  H8    s7   111     FORCED    owed by slot 0 (L3) | open 0 pairs, owed 0 | ret H7: unwrite s7, xor m7 | state [000 x1 x2 x3 P(x3) P(x2) P(x1) 111]
  CLOSE  slot 7 -> slot 0 by L4: step = 111 xor 000 = 111, all bits: C. Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.
  ROUTE HOME from H8: unwrite slots 7, 6, ..., 0 in that order; each unwrite returns H(t+1) to H(t) exactly, since L2 overwrote nothing. On the ring: forward from slot 7 is one step, C, to slot 0; backward is the 7 step masks in reverse order.
  SHAPE, forced in every legal history: 4 facing rows (slot a with slot 7-a), one slot sum 7, odd, so no slot faces itself; crease = edge 3|4, adjacent slots, no loop; open end = edge 7|0, closed by C.
  On the 3-cube mesh: facing-row gaps (bits that differ) {2: 2, 3: 2}: 2 palindromic rows at gap 3, the rest at even gaps; closing step weight 3.
  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. Writes 8: boundary 1, forced 4, AMBIGUOUS 3. Legal histories = product of the AMBIGUOUS counts = 48.

=== width n = 4: 16 words ===
  H1    s0   0000    BOUNDARY  L5; owes s15 <- 1111 | open 7 pairs, owed 1 | ret H0: unwrite s0
  H2    s1   x1      AMBIGUOUS 14 legal (7 pairs x 2), Q missing; owes s14 <- P(x1) | open 6 pairs, owed 2 | ret H1: unwrite s1, xor m1
  H3    s2   x2      AMBIGUOUS 12 legal (6 pairs x 2), Q missing; owes s13 <- P(x2) | open 5 pairs, owed 3 | ret H2: unwrite s2, xor m2
  H4    s3   x3      AMBIGUOUS 10 legal (5 pairs x 2), Q missing; owes s12 <- P(x3) | open 4 pairs, owed 4 | ret H3: unwrite s3, xor m3
  H5    s4   x4      AMBIGUOUS 8 legal (4 pairs x 2), Q missing; owes s11 <- P(x4) | open 3 pairs, owed 5 | ret H4: unwrite s4, xor m4
  H6    s5   x5      AMBIGUOUS 6 legal (3 pairs x 2), Q missing; owes s10 <- P(x5) | open 2 pairs, owed 6 | ret H5: unwrite s5, xor m5
  H7    s6   x6      AMBIGUOUS 4 legal (2 pairs x 2), Q missing; owes s9 <- P(x6) | open 1 pairs, owed 7 | ret H6: unwrite s6, xor m6
  H8    s7   x7      AMBIGUOUS 2 legal (1 pairs x 2), Q missing; owes s8 <- P(x7) | open 0 pairs, owed 8 | ret H7: unwrite s7, xor m7
  H9    s8   P(x7)   FORCED    owed by slot 7 (L3) | open 0 pairs, owed 7 | ret H8: unwrite s8, xor m8
  H10   s9   P(x6)   FORCED    owed by slot 6 (L3) | open 0 pairs, owed 6 | ret H9: unwrite s9, xor m9
  H11   s10  P(x5)   FORCED    owed by slot 5 (L3) | open 0 pairs, owed 5 | ret H10: unwrite s10, xor m10
  H12   s11  P(x4)   FORCED    owed by slot 4 (L3) | open 0 pairs, owed 4 | ret H11: unwrite s11, xor m11
  H13   s12  P(x3)   FORCED    owed by slot 3 (L3) | open 0 pairs, owed 3 | ret H12: unwrite s12, xor m12
  H14   s13  P(x2)   FORCED    owed by slot 2 (L3) | open 0 pairs, owed 2 | ret H13: unwrite s13, xor m13
  H15   s14  P(x1)   FORCED    owed by slot 1 (L3) | open 0 pairs, owed 1 | ret H14: unwrite s14, xor m14
  H16   s15  1111    FORCED    owed by slot 0 (L3) | open 0 pairs, owed 0 | ret H15: unwrite s15, xor m15
  CLOSE  slot 15 -> slot 0 by L4: step = 1111 xor 0000 = 1111, all bits: C. Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.
  ROUTE HOME from H16: unwrite slots 15, 14, ..., 0 in that order; each unwrite returns H(t+1) to H(t) exactly, since L2 overwrote nothing. On the ring: forward from slot 15 is one step, C, to slot 0; backward is the 15 step masks in reverse order.
  SHAPE, forced in every legal history: 8 facing rows (slot a with slot 15-a), one slot sum 15, odd, so no slot faces itself; crease = edge 7|8, adjacent slots, no loop; open end = edge 15|0, closed by C.
  On the 4-cube mesh: facing-row gaps (bits that differ) {2: 4, 4: 4}: 2 palindromic rows at gap 4, the rest at even gaps; closing step weight 4.
  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. Writes 16: boundary 1, forced 8, AMBIGUOUS 7. Legal histories = product of the AMBIGUOUS counts = 645120.

=== width n = 5: 32 words ===
  H1    s0   00000   BOUNDARY  L5; owes s31 <- 11111 | open 15 pairs, owed 1 | ret H0: unwrite s0
  H2    s1   x1      AMBIGUOUS 30 legal (15 pairs x 2), Q missing; owes s30 <- P(x1) | open 14 pairs, owed 2 | ret H1: unwrite s1, xor m1
  H3    s2   x2      AMBIGUOUS 28 legal (14 pairs x 2), Q missing; owes s29 <- P(x2) | open 13 pairs, owed 3 | ret H2: unwrite s2, xor m2
  H4    s3   x3      AMBIGUOUS 26 legal (13 pairs x 2), Q missing; owes s28 <- P(x3) | open 12 pairs, owed 4 | ret H3: unwrite s3, xor m3
  H5    s4   x4      AMBIGUOUS 24 legal (12 pairs x 2), Q missing; owes s27 <- P(x4) | open 11 pairs, owed 5 | ret H4: unwrite s4, xor m4
  H6    s5   x5      AMBIGUOUS 22 legal (11 pairs x 2), Q missing; owes s26 <- P(x5) | open 10 pairs, owed 6 | ret H5: unwrite s5, xor m5
  H7    s6   x6      AMBIGUOUS 20 legal (10 pairs x 2), Q missing; owes s25 <- P(x6) | open 9 pairs, owed 7 | ret H6: unwrite s6, xor m6
  H8    s7   x7      AMBIGUOUS 18 legal (9 pairs x 2), Q missing; owes s24 <- P(x7) | open 8 pairs, owed 8 | ret H7: unwrite s7, xor m7
  H9    s8   x8      AMBIGUOUS 16 legal (8 pairs x 2), Q missing; owes s23 <- P(x8) | open 7 pairs, owed 9 | ret H8: unwrite s8, xor m8
  H10   s9   x9      AMBIGUOUS 14 legal (7 pairs x 2), Q missing; owes s22 <- P(x9) | open 6 pairs, owed 10 | ret H9: unwrite s9, xor m9
  H11   s10  x10     AMBIGUOUS 12 legal (6 pairs x 2), Q missing; owes s21 <- P(x10) | open 5 pairs, owed 11 | ret H10: unwrite s10, xor m10
  H12   s11  x11     AMBIGUOUS 10 legal (5 pairs x 2), Q missing; owes s20 <- P(x11) | open 4 pairs, owed 12 | ret H11: unwrite s11, xor m11
  H13   s12  x12     AMBIGUOUS 8 legal (4 pairs x 2), Q missing; owes s19 <- P(x12) | open 3 pairs, owed 13 | ret H12: unwrite s12, xor m12
  H14   s13  x13     AMBIGUOUS 6 legal (3 pairs x 2), Q missing; owes s18 <- P(x13) | open 2 pairs, owed 14 | ret H13: unwrite s13, xor m13
  H15   s14  x14     AMBIGUOUS 4 legal (2 pairs x 2), Q missing; owes s17 <- P(x14) | open 1 pairs, owed 15 | ret H14: unwrite s14, xor m14
  H16   s15  x15     AMBIGUOUS 2 legal (1 pairs x 2), Q missing; owes s16 <- P(x15) | open 0 pairs, owed 16 | ret H15: unwrite s15, xor m15
  H17   s16  P(x15)  FORCED    owed by slot 15 (L3) | open 0 pairs, owed 15 | ret H16: unwrite s16, xor m16
  H18   s17  P(x14)  FORCED    owed by slot 14 (L3) | open 0 pairs, owed 14 | ret H17: unwrite s17, xor m17
  H19   s18  P(x13)  FORCED    owed by slot 13 (L3) | open 0 pairs, owed 13 | ret H18: unwrite s18, xor m18
  H20   s19  P(x12)  FORCED    owed by slot 12 (L3) | open 0 pairs, owed 12 | ret H19: unwrite s19, xor m19
  H21   s20  P(x11)  FORCED    owed by slot 11 (L3) | open 0 pairs, owed 11 | ret H20: unwrite s20, xor m20
  H22   s21  P(x10)  FORCED    owed by slot 10 (L3) | open 0 pairs, owed 10 | ret H21: unwrite s21, xor m21
  H23   s22  P(x9)   FORCED    owed by slot 9 (L3) | open 0 pairs, owed 9 | ret H22: unwrite s22, xor m22
  H24   s23  P(x8)   FORCED    owed by slot 8 (L3) | open 0 pairs, owed 8 | ret H23: unwrite s23, xor m23
  H25   s24  P(x7)   FORCED    owed by slot 7 (L3) | open 0 pairs, owed 7 | ret H24: unwrite s24, xor m24
  H26   s25  P(x6)   FORCED    owed by slot 6 (L3) | open 0 pairs, owed 6 | ret H25: unwrite s25, xor m25
  H27   s26  P(x5)   FORCED    owed by slot 5 (L3) | open 0 pairs, owed 5 | ret H26: unwrite s26, xor m26
  H28   s27  P(x4)   FORCED    owed by slot 4 (L3) | open 0 pairs, owed 4 | ret H27: unwrite s27, xor m27
  H29   s28  P(x3)   FORCED    owed by slot 3 (L3) | open 0 pairs, owed 3 | ret H28: unwrite s28, xor m28
  H30   s29  P(x2)   FORCED    owed by slot 2 (L3) | open 0 pairs, owed 2 | ret H29: unwrite s29, xor m29
  H31   s30  P(x1)   FORCED    owed by slot 1 (L3) | open 0 pairs, owed 1 | ret H30: unwrite s30, xor m30
  H32   s31  11111   FORCED    owed by slot 0 (L3) | open 0 pairs, owed 0 | ret H31: unwrite s31, xor m31
  CLOSE  slot 31 -> slot 0 by L4: step = 11111 xor 00000 = 11111, all bits: C. Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.
  ROUTE HOME from H32: unwrite slots 31, 30, ..., 0 in that order; each unwrite returns H(t+1) to H(t) exactly, since L2 overwrote nothing. On the ring: forward from slot 31 is one step, C, to slot 0; backward is the 31 step masks in reverse order.
  SHAPE, forced in every legal history: 16 facing rows (slot a with slot 31-a), one slot sum 31, odd, so no slot faces itself; crease = edge 15|16, adjacent slots, no loop; open end = edge 31|0, closed by C.
  On the 5-cube mesh: facing-row gaps (bits that differ) {2: 8, 4: 4, 5: 4}: 4 palindromic rows at gap 5, the rest at even gaps; closing step weight 5.
  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. Writes 32: boundary 1, forced 16, AMBIGUOUS 15. Legal histories = product of the AMBIGUOUS counts = 42849873690624000.

WIDTHS 6-8, same rules, step lines not printed:
  n=6: writes 64, forced 32, AMBIGUOUS 31, log10(legal histories) = 43.25; equals 2^(h-1) (h-1)! with h = 32: True
  n=7: writes 128, forced 64, AMBIGUOUS 63, log10(legal histories) = 106.26; equals 2^(h-1) (h-1)! with h = 64: True
  n=8: writes 256, forced 128, AMBIGUOUS 127, log10(legal histories) = 251.71; equals 2^(h-1) (h-1)! with h = 128: True

WITHOUT L5 (slot 0 left open): the closing step is P(x) xor x for the word x in slot 0.
  n=1: slot-0 words that close by C: 2 of 2 (2 palindromes, 0 anti-palindromes, J(x) = C(x))
  n=2: slot-0 words that close by C: 4 of 4 (2 palindromes, 2 anti-palindromes, J(x) = C(x))
  n=3: slot-0 words that close by C: 4 of 8 (4 palindromes, 0 anti-palindromes, J(x) = C(x))
  n=4: slot-0 words that close by C: 8 of 16 (4 palindromes, 4 anti-palindromes, J(x) = C(x))
  n=5: slot-0 words that close by C: 8 of 32 (8 palindromes, 0 anti-palindromes, J(x) = C(x))
  n=6: slot-0 words that close by C: 16 of 64 (8 palindromes, 8 anti-palindromes, J(x) = C(x))
  n=7: slot-0 words that close by C: 16 of 128 (16 palindromes, 0 anti-palindromes, J(x) = C(x))
  n=8: slot-0 words that close by C: 32 of 256 (16 palindromes, 16 anti-palindromes, J(x) = C(x))

EXHAUSTIVE CHECK. n = 1-3: every ordering of the words with 0^n first, filtered by L0-L5, against the construction. n = 4: the construction only (15! orderings is out of reach).
  n=1: orderings passing L0-L5 1; construction 1; same set: True
        closing step C in 1; route home (step masks undone in reverse) returns to H0 in 1
        record ring, seam exchange (P(m) before m): 1 0  legal: False
        record ring, counter order (m before P(m)): 0 1  legal: True
  n=2: orderings passing L0-L5 2; construction 2; same set: True
        closing step C in 2; route home (step masks undone in reverse) returns to H0 in 2
        record ring, seam exchange (P(m) before m): 00 10 01 11  legal: True
        record ring, counter order (m before P(m)): 00 01 10 11  legal: True
  n=3: orderings passing L0-L5 48; construction 48; same set: True
        closing step C in 48; route home (step masks undone in reverse) returns to H0 in 48
        record ring, seam exchange (P(m) before m): 000 001 010 110 011 101 100 111  legal: True
        record ring, counter order (m before P(m)): 000 001 010 011 110 101 100 111  legal: True
  n=4: construction 645120 histories (= 7! x 2^7: True)
        closing step C in 645120; route home (step masks undone in reverse) returns to H0 in 645120
        record ring, seam exchange (P(m) before m): (16 words)  legal: True
        record ring, counter order (m before P(m)): (16 words)  legal: True

MESH SHAPE OVER ALL LEGAL HISTORIES (cube edges joining slots 3+ apart around the ring; run = another such edge 1-2 slots along with the same slot sum (opposed) or the same slot difference (co-moving)):
  n=3: 48 histories; mesh contacts 3-7; co-moving share 0.00-1.00 (4 histories with none); opposed share 0.00-0.57 (28 with none)
        record ring, seam exchange: contacts 5, opposed 0, co-moving 5, both 0, none 0; co-moving share 1.00, opposed share 0.00
        record ring, counter order: contacts 3, opposed 0, co-moving 2, both 0, none 1; co-moving share 0.67, opposed share 0.00
  n=4: 645120 histories; mesh contacts 14-32; co-moving share 0.11-0.96 (0 histories with none); opposed share 0.00-0.96 (128 with none)
        record ring, seam exchange: contacts 21, opposed 5, co-moving 10, both 4, none 2; co-moving share 0.67, opposed share 0.43
        record ring, counter order: contacts 21, opposed 2, co-moving 14, both 4, none 1; co-moving share 0.86, opposed share 0.29

PAST CLOSURE. Every word of width n is written and L4 returns slot N-1 to slot 0: no write remains at width n.
  Continuing needs a new distinction (a new bit). The history does not provide one.  OPEN: the provider of the new bit.
  If one is provided, the closed history must survive (L2) with its facings (L3). Every uniform insertion, tried:
  n=1 -> 2: 4 insertions; no non-palindromic rows to keep; palindromic rows kept by any insertion: 0 of 1
  n=1 -> 3: 12 insertions; no non-palindromic rows to keep; palindromic rows kept by any insertion: 0 of 1
  n=2 -> 3: 6 insertions; keep all 1 non-palindromic rows: 2 [0@1 1@1]; palindromic rows kept by any insertion: 0 of 1
  n=2 -> 4: 24 insertions; keep all 1 non-palindromic rows: 4 [00@0,3 11@0,3 00@1,2 11@1,2]; palindromic rows kept by any insertion: 0 of 1; the record's nesting 1.x.1 (11@0,3) among them: True
  n=3 -> 4: 8 insertions; keep all 2 non-palindromic rows: 0 []; palindromic rows kept by any insertion: 0 of 2
  n=3 -> 5: 40 insertions; keep all 2 non-palindromic rows: 4 [00@0,4 11@0,4 00@1,3 11@1,3]; palindromic rows kept by any insertion: 0 of 2; the record's nesting 1.x.1 (11@0,4) among them: True
  n=4 -> 5: 10 insertions; keep all 6 non-palindromic rows: 2 [0@2 1@2]; palindromic rows kept by any insertion: 0 of 2
  n=4 -> 6: 60 insertions; keep all 6 non-palindromic rows: 6 [00@0,5 11@0,5 00@1,4 11@1,4 00@2,3 11@2,3]; palindromic rows kept by any insertion: 0 of 2; the record's nesting 1.x.1 (11@0,5) among them: True
  n=5 -> 6: 12 insertions; keep all 12 non-palindromic rows: 0 []; palindromic rows kept by any insertion: 0 of 4
  n=5 -> 7: 84 insertions; keep all 12 non-palindromic rows: 6 [00@0,6 11@0,6 00@1,5 11@1,5 00@2,4 11@2,4]; palindromic rows kept by any insertion: 0 of 4; the record's nesting 1.x.1 (11@0,6) among them: True
  n=6 -> 7: 14 insertions; keep all 28 non-palindromic rows: 2 [0@3 1@3]; palindromic rows kept by any insertion: 0 of 4
  n=6 -> 8: 112 insertions; keep all 28 non-palindromic rows: 8 [00@0,7 11@0,7 00@1,6 11@1,6 00@2,5 11@2,5 00@3,4 11@3,4]; palindromic rows kept by any insertion: 0 of 4; the record's nesting 1.x.1 (11@0,7) among them: True
  No uniform insertion keeps any palindromic row: its partner is C, and C flips the new bits too. Those rows have no way home through a widening; they are the piece that moves. No uniform insertion keeps the whole closed history.
  One new bit (n -> n+1) keeps the non-palindromic rows only at even n, only at the centre, either value. At odd n every single-bit insertion also breaks a non-palindromic facing: from odd n, n -> n+1 keeps no facing block.
  Two new bits (n -> n+2) keep them at every n: mirrored places, equal values. Which pair of places and which value: AMBIGUOUS, qualifier missing.

SEAL
  s199 seal. Written after the generator ran, before any chain file is opened in this run. Generator output SHA-256 7449637f07d5761df36c1336946b245cbbfc4e95abeed8b865f241dc8aa25973. Forced by the laws in every legal history, what each says about chains, and the readout it returns through (s188 detector, ecoli_chains.json): G1 one register per fold: every facing row shares one slot sum. Readout: stored pairs at S+1 or S-1 inside a hairpin's span; each hairpin carrying one lies outside the generator. G2 edge-centred crease: the facing sum is odd and no slot faces itself. Readout: parity of S; even S lies outside. G3 no loop: the two crease slots are adjacent. Readout: s - e of the crease pair; s - e > 1 lies outside. The laws hold no provider for a loop width: OPEN. G4 facing layer: the laws make only opposed facings (one slot sum). Readout: run label of every stored pair in all 160 chains; pairs in co-moving runs lie outside the facing layer. Mesh layer (cube edges between slots 3+ apart): it depends on the AMBIGUOUS order; at n = 4 every legal order carries co-moving mesh runs (share 0.11-0.96) and 128 orders carry no opposed mesh run, so on the mesh co-moving runs are unavoidable and opposed runs avoidable, at no fixed share. No chain share is predicted from the mesh layer. G5 the open end closes by C. Chains are open: no counterpart, not tested. G6 which word sits in which slot is AMBIGUOUS: no residue-level claim. Not blind: G1 (s197 census of S-1 and S+1 pairs), G2 and G3 (s188/s197: 94 odd, 49 even; the detector admits only pairs 3 or more apart). Not run before: G4 on all chains (s198 labelled hairpin rows only); the side note's i+3 and i+4 counts, read before this seal, bear on it. Checks of the side note, not predictions: directed contacts, i+3 and i+4 counts, the k = 3 / k = 4 choice where both O lie within 3.5 A.
  SHA-256 28e2ea9c147549e074e4fe54228849e273e71c051b3cf853f780d1c2ace10178
```

**Side checks** (`python3 -I side199.py ecoli_chains.json`; script sha `1346f3bb…`).

```
A. s167 RIS: independent frame-matrix computation
  case                                       sigma       omega  frames (here)   s167 4-coord    2(2+s)/3s  quoted
  equal weights                        1.000000000 1.000000000    2.000000000    2.000000000  2.000000000  2.000000000
  413 K, omega = 1                     0.542506969 1.000000000    3.124392391    3.124392391  3.124392391  3.124392391
  413 K, both penalties                0.542506969 0.086620620    6.229676328    6.229676328  3.124392391  6.229676328
  300 K, both penalties                0.430888258 0.034471377    7.200650328    7.200650328  3.761049745  7.200650328
  413 K, g+g- forbidden (omega = 0)    0.542506969 0.000000000    6.715345190    6.715345190  3.124392391  6.715345190 (GPT, 04a5f4d1)
  LM: sigma .543, omega 1              0.543000000 1.000000000    3.122160835    3.122160835  3.122160835  3.124392391 claimed; GPT: 3.122160835
  LM: sigma .543, omega .088           0.543000000 0.088000000    6.219869293    6.219869293  3.122160835  6.229676328 claimed; GPT: 6.219869293
  LM: sigma .350, omega .020           0.350000000 0.020000000    8.037816088    8.037816088  4.476190476  7.200650328 claimed; GPT: 8.037816088
  four-coordinate reader vs nine-coordinate frames, 2000 random (sigma, omega): max |difference| 1.12e-12
  one fixed basis of four uncoupled channels would make A(413 K) and A(300 K) commute: ||[A1, A2]|| = 0.124
  mirror symmetry (g+ <-> g-, z -> -z) commutes with the 9x9 operator: ||[S, M]|| = 6.0e-16; sectors: even 5, odd 4 (two blocks, not four scalars)

B. ring identities
  delta(P x) = rev(delta(x)), every word n = 1..13 (16382 words): failures 0
  proof: off palindromes P = J and differences of a reversed word are the reversed differences; on palindromes P = C, which leaves every difference unchanged, and a palindrome has palindromic differences.
  window width 1: reversal-fixed 2 (2^ceil(w/2) = 2), exchanged pairs 0 (formula 0)
  window width 2: reversal-fixed 2 (2^ceil(w/2) = 2), exchanged pairs 1 (formula 1)
  window width 3: reversal-fixed 4 (2^ceil(w/2) = 4), exchanged pairs 2 (formula 2)
  window width 4: reversal-fixed 4 (2^ceil(w/2) = 4), exchanged pairs 6 (formula 6)
  window width 5: reversal-fixed 8 (2^ceil(w/2) = 8), exchanged pairs 12 (formula 12)
  window width 6: reversal-fixed 8 (2^ceil(w/2) = 8), exchanged pairs 28 (formula 28)
  window width 7: reversal-fixed 16 (2^ceil(w/2) = 16), exchanged pairs 56 (formula 56)
  window width 8: reversal-fixed 16 (2^ceil(w/2) = 16), exchanged pairs 120 (formula 120)
  sliding reader s_i = d_(i+1) - d_i: s_i(Px) = -s_(L-2-i)(x) for every word n = 3..13: failures 0
  sliding reader over 4 differences: 15 distinct readings of 27 ternary sequences; readings with +1 followed by +1: 0
  sliding reader over 6 differences: 63 distinct readings of 243 ternary sequences; readings with +1 followed by +1: 0
  sliding reader over 8 differences: 255 distinct readings of 2187 ternary sequences; readings with +1 followed by +1: 0
  two-bit token code t=00, g+=01, g-=10 under P: 9840 of 9840 ternary histories (m = 1..8) read back reversed with g+ <-> g-

C. signed dihedral
  10000 random atom quadruples: reversed order keeps the dihedral 10000/10000; a mirror flips its sign 10000/10000

E. the record ring as a binding of the AMBIGUOUS writes by the counter
  n= 2: counter binding = record ring with counter order: True; slots where it differs from the record ring: [1, 2]
  n= 3: counter binding = record ring with counter order: True; slots where it differs from the record ring: [3, 4]
  n= 4: counter binding = record ring with counter order: True; slots where it differs from the record ring: [7, 8]
  n= 5: counter binding = record ring with counter order: True; slots where it differs from the record ring: [15, 16]
  n= 6: counter binding = record ring with counter order: True; slots where it differs from the record ring: [31, 32]
  n= 7: counter binding = record ring with counter order: True; slots where it differs from the record ring: [63, 64]
  n= 8: counter binding = record ring with counter order: True; slots where it differs from the record ring: [127, 128]
  n= 9: counter binding = record ring with counter order: True; slots where it differs from the record ring: [255, 256]
  n=10: counter binding = record ring with counter order: True; slots where it differs from the record ring: [511, 512]
  n=11: counter binding = record ring with counter order: True; slots where it differs from the record ring: [1023, 1024]
  n=12: counter binding = record ring with counter order: True; slots where it differs from the record ring: [2047, 2048]

D. NotebookLM transcript (upload c6bd5944)
  Answer 13 PDB ids present in the chain file: []
  O acceptors chosen by more than one donor: 1292, in 157 chains (GPT/Dean, Q16: 1,292 in 157)
  its routine, history [1, 0, 1, 0]: history alone d_min 1.0000; next 0 d_min 0.0000; next 1 d_min 1.0000; max |z| 3.2e-16
  its routine, history [1, 0, 0, 1]: history alone d_min 0.0000; next 0 d_min 0.0000; next 1 d_min 0.0000; max |z| 1.1e-16
  its routine, history [1, 1]: history alone d_min 1.0000; next 0 d_min 0.0000; next 1 d_min 1.0000; max |z| 2.1e-16
  its step for delta = 1: angle between successive bond vectors 120.0 deg
  its step for delta = 0: angle between successive bond vectors 120.0 deg
  O(n) rank formula: rectangle sum vs its definition (n <= 10) failures 0; Delta vs direct count (n = 2..14) failures 0; rank vs direct count of representatives (n = 2..14) failures 0
  64-bit pi word: representative True; address = rank = 2,427,008,858,123,944,441 (Answer 3: 2,427,008,858,123,944,441)
```

**GPT's uploaded audit script, run unchanged** (`NEXUS_RIS_Reverse_Gap_Independent_Audit.py`, isolated copy, `python3 -I`).

```
SOURCE equal sigma=1.000000000 omega=1.000000000 C=2.000000000
SOURCE sigma .543 w 1 sigma=0.543000000 omega=1.000000000 C=3.122160835
SOURCE sigma .543 w .088 sigma=0.543000000 omega=0.088000000 C=6.219869293
SOURCE sigma .543 w 0 sigma=0.543000000 omega=0.000000000 C=6.712987755
SOURCE sigma .350 w .020 sigma=0.350000000 omega=0.020000000 C=8.037816088
SOURCE 413K exact sigma=0.542506969 omega=0.086620620 C=6.229676328
SOURCE 300K exact sigma=0.430888258 omega=0.034471377 C=7.200650328
LM equal eig 2.999999999999999 avg-vector [0.22222222 0.22222222 0.22222222] C-vector [3.14285714 3.14285714 3.14285714]
LM sigma .543 w 1 eig 2.086 avg-vector [0.45962261 0.24957508 0.24957508] C-vector [5.40223425 3.33031338 3.33031338]
LM sigma .543 w .088 eig 1.8574016203255408 avg-vector [0.64211269 0.21733018 0.21733018] C-vector [9.17670259 3.11071193 3.11071193]
LM sigma .543 w 0 eig 1.838370306082234 avg-vector [0.66046425 0.21372792 0.21372792] C-vector [9.78079177 3.08729754 3.08729754]
LM sigma .350 w .020 eig 1.574804775174159 avg-vector [0.86277041 0.20361414 0.20361414] C-vector [27.1482315  3.0226909  3.0226909]
LM 413K exact eig 1.8564189057808274 avg-vector [0.6428118  0.21726562 0.21726562] C-vector [9.19857816 3.11029044 3.11029044]
LM 300K exact eig 1.691672682642311 avg-vector [0.76022599 0.21101791 0.21101791] C-vector [14.68237533  3.06982355  3.06982355]
EXACT 2-bit token 1 3 all pass
EXACT 2-bit token 2 9 all pass
EXACT 2-bit token 3 27 all pass
EXACT 2-bit token 4 81 all pass
EXACT 2-bit token 5 243 all pass
EXACT 2-bit token 6 729 all pass
EXACT 2-bit token 7 2187 all pass
EXACT 2-bit token 8 6561 all pass
```
