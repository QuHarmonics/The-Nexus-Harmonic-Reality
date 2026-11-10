# NEXUS running audit 7

Continues `claude/running-audit-6.md` (§§ 195–196). Same rules: live output only; STANDS / RUNS / DEAD END / OPEN, never CONFIRMED; scripts printed in full.

---

## § 197. TP and PT on the chain: S + 1 is TP with its self-facing pair at (e + 1, s), S − 1 is PT at (e, s − 1); as facings they stand 8 to 4 and the ring's 1 : 1 is not rejected; PT's excess is the turn's own arrow (i ← i + 3 / i + 4), not a reflection; the 30 / 11 was a residual — `tp_pt.py`

**Dean (30 Oct).** The § 196 prompt asked six things:
- From the ring alone, say which reflection an S + 1 slip is and which an S − 1 slip is.
- Say where the self-facing cell sits in each.
- Say why one should outnumber the other.
- Seal the assignment and the split.
- Land them on the 41 slips.
- Use the water only if the ring can't separate them, and name its address first.

Three side files came with it:
- GPT's *§ 196 face coherence, data linked*: a parallel § 196, with its own numbering.
- A side run of a shape-channel crease reader.
- A side run that splits the stored S ± 1 bonds by offset, parity, location and donor.

**Correction, mine (§ 196.4 and the prompt I wrote).**
- **The 30 / 11 is the § 193 residual,** the stored bonds the zipper doesn't emit.
  - The zipper emits (s − 1 → e) at every width above 3 (§ 192, line 2), so 49 of the 60 S − 1 bonds were removed before the count.
  - Counted whole, the windows hold 60 bonds at S − 1 and 30 at S + 1.
  - The prompt asked why TP outnumbers PT. In the full census PT outnumbers TP, 60 to 30.
- **"β-bulges" was too broad a label** for the 41, as GPT says. 84 of the 90 stored S ± 1 bonds lie inside the crease region (both residues in e … s); 6 lie on the arms.
- **§ 191 had already landed the crease split:** 24 at (e, s − 1) against 9 at (e + 1, s) on even S, with my sealed TP side the DEAD END. It also left open the question this section answers: is the lean the seam, or the turn's own bond?

### 197.1 The side files, re-executed on the original chain file

```
data raw SHA-256 f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145

A  RULE SHA-256 d98925c95f2b01c4818eb7894f91e80ce01a84146642fcf2df69b4e79530ff9a
A  Stage A rows 95496 centres 32464 score SHA-256 ef20a128123d1e20460a0821865f4f162799e76f84f41e9be2859b247750758c
A  true centres 132/143 evaluable; first 12, top 3 38, mean advantage 0.634060; width exact 54
A  shuffle null mean 0.498424 sd 0.024366  observed 0.634060  P(null >= obs) 0.00498
A  shifted null mean 0.513876 sd 0.021895  observed 0.634060  P(null >= obs) 0.00498
A  matched decoys n 132 mean 0.475469

B  shape-channel crease reader (parity-balanced), rank_in_window +-8, random.Random(195), 200 reps
B  scores SHA-256 e16e281b586efcf123278a8c306b04de1e708d16f425faf0b95ca660898482f9
B  true S first 17/143, top 3 58/143, mean advantage 0.6731 (S even 0.7443, S odd 0.6360); true centres scored -999 (arm off the chain): 0
B  shuffle null 0.5131 (sd 0.0250, P 0.0050); shifted null 0.4998 (sd 0.0235, P 0.0050)
B  invalid candidates dropped from the windows: n 143, first 17, top 3 58, mean advantage 0.6661
```

| reader | reproduced | status |
|---|---|---|
| GPT's face coherence (rule d98925c9…) | Stage A ef20a128…; 132 / 143 evaluable; 12 first, 38 in the top 3; advantage 0.634060 against shuffle 0.498424 and shift 0.513876 (p = 0.00498 each); decoys 0.475469 | RUNS, exact |
| side run's parity-balanced shape reader | scores e16e281b…; 17 first, 58 in the top 3; advantage 0.6731 (S even 0.7443, odd 0.6360) against 0.5131 and 0.4998 (p = 0.005 each) | RUNS, exact |
| side run's split of the S ± 1 bonds | 60 / 30, 49 of the 60 emitted | RUNS (§ 197.3) |
| GPT's slip rule (4c95489d…), its 41-slip trace, "20 hairpins, 18 chains, 26 pairs" | hash and counts reproduced | RUNS |

- **Neither reader addresses the crease.** Both rank true centres above shuffled and shifted ones, but only 12 and 17 centres come first.
- **The shape reader's classes are recovered.** Its turn tokens (G S P D N) and strand tokens (T V I F Y W H) are the *Reading Proteins* § 4 route words, and they match the standard turn and strand propensity classes.
- **Its "seam cells" are loop residues by geometry,** not the word-level transposition of § 195: τ acts on bit positions inside one word.
- **Off-chain candidates rank last in its windows.** Dropping them moves 0.6731 to 0.6661; the nulls weren't recomputed.
- **GPT's sealed slip rule** already says two conjugate reflections predict no sign excess. § 197.2 agrees.

### 197.2 From the ring, sealed before the chain file is opened

```
PART 1  the ring alone (positions: P a -> N-1-a, T a -> a+1; TP = T after P, PT = P after T)
  n= 2: facing law True; Fix(TP) [0, 2] words 0^n, m  weights [0, 1]; Fix(PT) [1, 3] words P(m), 1^n  weights [1, 2]; TP = T.PT.T^-1 True; PT = P.TP.P True; TP.PT = T^2 True; layout True
  n= 3: facing law True; Fix(TP) [0, 4] words 0^n, m  weights [0, 2]; Fix(PT) [3, 7] words P(m), 1^n  weights [2, 3]; TP = T.PT.T^-1 True; PT = P.TP.P True; TP.PT = T^2 True; layout True
  n= 4: facing law True; Fix(TP) [0, 8] words 0^n, m  weights [0, 3]; Fix(PT) [7, 15] words P(m), 1^n  weights [3, 4]; TP = T.PT.T^-1 True; PT = P.TP.P True; TP.PT = T^2 True; layout True
  n= 8: facing law True; Fix(TP) [0, 128] words 0^n, m  weights [0, 7]; Fix(PT) [127, 255] words P(m), 1^n  weights [7, 8]; TP = T.PT.T^-1 True; PT = P.TP.P True; TP.PT = T^2 True; layout True
  n=14: facing law True; Fix(TP) [0, 8192] words 0^n, m  weights [0, 13]; Fix(PT) [8191, 16383] words P(m), 1^n  weights [13, 14]; TP = T.PT.T^-1 True; PT = P.TP.P True; TP.PT = T^2 True; layout True
  n = 2..14 all hold

  chain to ring: a stored pair (i < j) at sum S + d goes to cells (i - e + h - 1, j - s + h), ring sum N - 1 + d;
  it is self-facing (one cell) iff j - i = w - 1.  Crease-region pairs (e <= i < j <= s, j - i >= 3) at S +- 1:
    w=3 TP: none (all within |i-j| <= 2)
    w=3 PT: none (all within |i-j| <= 2)
    w=4 TP: (e+1, s+0) SELF
    w=4 PT: (e+0, s-1) SELF
    w=5 TP: (e+1, s+0) SELF
    w=5 PT: (e+0, s-1) SELF
    w=6 TP: (e+1, s+0) SELF, (e+2, s-1)
    w=6 PT: (e+0, s-1) SELF, (e+1, s-2)
    w=7 TP: (e+1, s+0) SELF, (e+2, s-1)
    w=7 PT: (e+0, s-1) SELF, (e+1, s-2)
    w=8 TP: (e+1, s+0) SELF, (e+2, s-1), (e+3, s-2)
    w=8 PT: (e+0, s-1) SELF, (e+1, s-2), (e+2, s-3)

PART 2  sealed prediction
  s197, sealed before this script opens ecoli_chains.json. NOT BLIND, stated: the s193 residual (62/11/30/33), GPT's 41-slip trace and the side run's +-1 breakdown (parity, location, donor side) were read before this seal; the full census with emitted closures, mutual vs one-way per pair, and the anchor status of the inward PT pairs were not printed there. Orientation: T = N->C, listed half = outgoing strand. A stored pair (i<j) at sum S+d maps to ring cells (i-e+h-1, j-s+h), ring sum N-1+d. (1) Assignment: S+1 is TP (sum N); S-1 is PT (sum N-2). (2) Location: a pair is self-facing iff its two cells coincide, j-i = w-1. TP's is (e+1,s): cell h, the word m, first cell past the break; s faces e and e+1, so the outgoing strand holds the extra residue; inward TP rows (e+1+u, s-u). PT's is (e,s-1): cell h-1, the word P(m), last cell of the rise; e faces s-1 and s, so the returning strand holds the extra residue; inward PT rows (e+u, s-1-u). The other fixed cells (0^n for TP, 1^n for PT) lie on the wrap, off any hairpin; not tested. (3) Split: the ring gives none. TP = T.PT.T^-1 and PT = P.TP.P; the fixed sets differ by one step of T, and in value only by the rail held (0^n against 1^n). A facing is mutual (P is an involution), so the ring's 1:1 is a claim about facings, pairs stored in both directions. A one-way bond is not a facing; the ring makes no count claim for it, and an excess there is the bond's direction, which P does not carry. (4) One reflection per crease: TP.PT = T^2 is a rotation, so no crease holds a TP facing and a PT facing. (5) A register is anchored at its fixed cell: every hairpin with an inward facing (u >= 1) stores its anchor, (e+1,s) or (e,s-1), in at least one direction. (6) The s193 zipper emits (s-1 -> e) at every width above 3, so the residual 30/11 is no TP:PT census; with emitted closures counted, S-1 outnumbers S+1. Bars, on the crease region (both residues in e..s): B1 hairpins with a TP facing only against a PT facing only, two-sided binomial p >= 0.05 against 1:1; B2 hairpins with both facings = 0; B3 one-way bonds: PT at least twice TP and at least 90 % donated by the later residue (seen; a check); B4 every inward facing has its anchor stored; B5 full window census S-1 > S+1 (seen; a check). Water: not opened. Its address would be the rail: TP's and PT's fixed sets differ in value only by 0^n against 1^n (value bit 1 = wet), and those cells lie on the wrap, off the hairpins; with the facings this few, a water comparison could not land.
  SHA-256 89e41fae06b2b3d1152db96485243483dd4445bee77903fb9db3317c986e5513
```

- **Orientation.** T runs N → C, and the listed half is the outgoing strand. A stored pair (i < j) at sum S + d goes to ring cells (i − e + h − 1, j − s + h), with ring sum N − 1 + d.
- **Assignment.** S + 1 is TP (sum N). S − 1 is PT (sum N − 2).
- **Where the self-facing cell sits.** A pair lands on one cell iff j − i = w − 1.
  - **TP's pair is (e + 1, s):** cell h, the word m, the first cell past the break. s faces e and e + 1, so the outgoing strand holds the extra residue.
  - **PT's pair is (e, s − 1):** cell h − 1, the word P(m), the last cell of the rise. e faces s − 1 and s, so the returning strand holds the extra residue.
  - **The loop crosses the seam twice** on this map: going out e (h − 1) → e + 1 (h), and coming back s − 1 (h − 1) → s (h). Each fixed cell is where the two passes meet.
  - **The other fixed cells,** 0ⁿ for TP and 1ⁿ for PT, lie on the wrap, off any hairpin.
- **The split.** The ring gives none.
  - TP = T·PT·T⁻¹ and PT = P·TP·P (n = 2–14). The two fixed sets differ by one step of T, and in value only by the rail each holds.
  - P is an involution, so a facing is mutual, and the ring's 1 : 1 is a statement about facings.
  - A one-way bond isn't a facing, and the ring makes no count claim for it.
- **The water.** Its address would be the rail: 0ⁿ against 1ⁿ, with value bit 1 = wet. Those cells lie on the wrap, and the facings are too few to compare. Not opened.

**A second reading.** § 192's R₂ turn puts the four residues of a width-3 turn on the whole of R₂: e = 00, e + 1 = 10 = P(m), e + 2 = 01 = m, s = 11.

```
  P  (sum 3 mod 4): e <-> s [00, 11], e+1 <-> e+2 (= s-1 at w = 3) [10, 01]
  TP (sum 0 mod 4): e faces itself [00], e+1 <-> s [10, 11], e+2 (= s-1 at w = 3) faces itself [01]
  PT (sum 2 mod 4): e <-> e+2 (= s-1 at w = 3) [00, 01], e+1 faces itself [10], s faces itself [11]
  GPT slip rule SHA-256 4c95489dee5c731649f60fed669b81b606ef9a7876d59c11440782a6515b2264
```

- **The two readings make the same pairs:** TP pairs e + 1 with s, and PT pairs e with s − 1.
- **On R₂, the self-facing cells are the residues each register leaves unpaired.** TP leaves e, on the outgoing side. PT leaves s, on the returning side.
- **What survives both readings:** the anchor pair, and the side of the extra residue (outgoing for TP, returning for PT).

### 197.3 Landed

```
PART 3  data  raw SHA-256 f5266a447a4342955936966ff46df15823da5c55508540d78f316bf3f4d2e145
  hairpins 143, even S 49

  (a) s193 residual (stored, not emitted, inside the window): {'S-1': 11, 'S': 62, 'S+1': 30, 'other': 33}  slips 41: S+1 30, S-1 11
      GPT's description checked: hairpins 20, chains 18, undirected pairs 26 (+1: 19, -1: 7); donors inside the loop: -1 9/11, +1 16/30
      slip hairpins by S parity: even 19 odd 1 | all hairpins: even 49 odd 94

  (b) full window census at S +- 1 (directed bonds): S-1 60 (crease 58, arm 2; emitted by the zipper 49), S+1 30 (crease 26, arm 4; emitted 0)
      S-1 crease: mutual  8  one-way 50  later residue donates 53/58  pairs: [('(e+0,s-1)', 49), ('(e+2,s-3)', 9)]
      S-1 arm   : mutual  0  one-way  2  later residue donates  1/2  pairs: [('(e-5,s+4)', 1), ('(e-2,s+1)', 1)]
      S+1 crease: mutual 18  one-way  8  later residue donates 13/26  pairs: [('(e+1,s+0)', 17), ('(e+3,s-2)', 8), ('(e+2,s-1)', 1)]
      S+1 arm   : mutual  4  one-way  0  later residue donates  2/4  pairs: [('(e-2,s+3)', 2), ('(e+0,s+1)', 2)]

  (c) crease facings (mutual pairs, both residues in e..s), by hairpin: TP only 8, PT only 4, both 0
      B1  TP 8 : PT 4, two-sided binomial p = 0.388 against 1:1  -> lands
      B2  creases holding both facings: 0  -> lands
        4K4C   e=104 s=112 w=8 S even  TP facings [(1, 0)]  PT facings []  one-way TP [(3, -2)]  one-way PT []
        1QYN   e= 42 s= 46 w=4 S even  TP facings [(1, 0)]  PT facings []  one-way TP []  one-way PT []
        5Z38   e= 22 s= 30 w=8 S even  TP facings [(3, -2)]  PT facings []  one-way TP [(1, 0)]  one-way PT []
        5E1L   e=127 s=135 w=8 S even  TP facings [(1, 0)]  PT facings []  one-way TP [(3, -2)]  one-way PT []
        2FS2   e= 99 s=107 w=8 S even  TP facings [(1, 0)]  PT facings []  one-way TP [(3, -2)]  one-way PT []
        1NJK   e= 76 s= 84 w=8 S even  TP facings [(1, 0), (3, -2)]  PT facings []  one-way TP []  one-way PT []
        1VH5   e=103 s=111 w=8 S even  TP facings [(1, 0)]  PT facings []  one-way TP [(3, -2)]  one-way PT []
        4Q2U   e= 61 s= 65 w=4 S even  TP facings [(1, 0)]  PT facings []  one-way TP []  one-way PT []
        1FS0   e=  7 s= 15 w=8 S even  TP facings []  PT facings [(2, -3)]  one-way TP []  one-way PT [(0, -1)]
        1JKE   e= 12 s= 20 w=8 S even  TP facings []  PT facings [(2, -3)]  one-way TP []  one-way PT [(0, -1)]
        4KEH   e=146 s=154 w=8 S even  TP facings []  PT facings [(2, -3)]  one-way TP []  one-way PT [(0, -1)]
        5LS7   e= 41 s= 49 w=8 S even  TP facings []  PT facings [(2, -3)]  one-way TP []  one-way PT [(0, -1)]
      B3  one-way crease bonds: PT 50, TP 8; later residue donates 53/58 (0.91)  -> lands
      B4  inward facings (u >= 1) and their anchors: 6/6 anchored  -> lands
        1FS0   e=  7 s= 15 w=8 PT inward (e+2,s-3)  anchor (e+0,s-1) stored as ['14->7']
        1JKE   e= 12 s= 20 w=8 PT inward (e+2,s-3)  anchor (e+0,s-1) stored as ['19->12']
        4KEH   e=146 s=154 w=8 PT inward (e+2,s-3)  anchor (e+0,s-1) stored as ['153->146']
        5LS7   e= 41 s= 49 w=8 PT inward (e+2,s-3)  anchor (e+0,s-1) stored as ['48->41']
        5Z38   e= 22 s= 30 w=8 TP inward (e+3,s-2)  anchor (e+1,s+0) stored as ['30->23']
        1NJK   e= 76 s= 84 w=8 TP inward (e+3,s-2)  anchor (e+1,s+0) stored as ['77->84', '84->77']
      B5  full window census S-1 60 against S+1 30  -> lands

  (d) crease classes by width (f = facing, 1 = one-way only):
      w=3: none 58
      w=4: PT1 20, TP1 2, TPf 2, none 9
      w=5: PT1 23, none 8
      w=6: TP1 1, none 3
      w=7: PT1 1, none 4
      w=8: PT1 1, PTf 4, TPf 6, none 1
```

- **B1 lands.** Crease facings stand 8 TP to 4 PT, two-sided p = 0.388. Twelve hairpins give the test little power: 1 : 1 is not rejected, but it isn't shown either.
- **B2 lands.** No crease holds both facings, and no hairpin stores both anchors (§ 197.4).
- **B4 lands, and it was blind.** The four inward PT facings (e + 2 ↔ s − 3, all at width 8) each store their anchor, always as s − 1 → e. The two inward TP facings store theirs too.
- **B3 and B5 land as checks** on numbers the side run had already printed: 50 one-way PT bonds against 8 TP, and 60 against 30.
- **Widths.** Facings occur only at w = 4 (TP 2) and w = 8 (TP 6, PT 4). One-way PT anchors occur at w = 4, 5, 7 and 8.

### 197.4 Post hoc: what the PT excess is

```
   33  ('PT anchor', 'later s-1->e', '', 'e->s', 'no s->e')
   16  ('PT anchor', 'later s-1->e', '', 'e->s', 's->e')
    3  ('TP anchor', 'later s->e+1', '', 'e->s', 'no s->e')
    7  ('TP anchor', 'later s->e+1', 'earlier e+1->s', 'e->s', 'no s->e')
   18  ('no anchor', 'e->s', 'no s->e')
    6  ('no anchor', 'e->s', 's->e')
    2  ('no anchor', 'no e->s', 's->e')
   58  w3
```

```
  one-way bonds in the crease region, by (separation, register offset): count (later residue donates)
    sep 3, offset -4:   2 (2)
    sep 3, offset -3:   2 (2)
    sep 3, offset -2:  16 (16)
    sep 3, offset -1:  21 (20)
    sep 3, offset +1:   7 (3)
    sep 3, offset +2:   4 (4)
    sep 3, offset +3:   2 (2)
    sep 4, offset -3:   1 (1)
    sep 4, offset -1:  23 (23)
    sep 6, offset -1:   1 (1)
    sep 7, offset -1:   5 (5)
    sep 7, offset +1:   1 (1)
  mutual pairs in the crease region, by (separation, register offset):
    sep 3, offset -2:   1
    sep 3, offset -1:   4
    sep 3, offset +1:   4
    sep 7, offset +1:   5
  totals: one-way 85 (separation 3 or 4: 78); mutual pairs 14 (offset +-1: 13)
```

- **Line 1 holds wherever an anchor does.** Every hairpin that stores an anchor also stores e → s, 59 of 59: e's NH goes to O(s) (§ 192, line 1).
- **That leaves PT one way in.** With e's donor spent, PT can enter only through O(e), from the returning side's earlier NH, s − 1. It does in 49 of the 85 hairpins wider than 3. The reverse, e → s − 1, never occurs.
- **TP enters through s's NH landing one cell late,** on O(e + 1), in 10 of 10 TP hairpins.
  - In 7 of them e + 1 answers (e + 1 → s), and that makes a facing.
  - In all 10, s → e is absent.
- **The two anchors behave differently.** No hairpin stores both. PT's anchor is never a facing: 0 of 49 are mutual. TP's anchor is a facing in 7 of 10.
- **The crease region holds two kinds of bond.**
  - **Arrows.** 85 one-way bonds, 78 of them at separation 3 or 4. Their register offsets spread from −4 to +3, and the later residue donates in 80 of them. This is the turn's own i ← i + 3 / i + 4 bond; the width sets its register offset.
  - **Facings.** 14 mutual pairs, 13 of them at offset ±1. These are the slipped registers.
  - The S − 1 excess is the arrow landing at offset −1 whenever s − 1 is e + 3 (w = 4) or e + 4 (w = 5).
- **In the ring's terms,** an arrow keeps a fixed separation, which makes it a power of T. A facing keeps a fixed sum: P, or P slipped by T.
  - § 192's two program lines are one facing (line 1, the crease row) and one arrow (line 2, the turn bond).
  - The ring's 1 : 1 is about facings, and the facings don't contradict it.
- **Recovered, not new:**
  - the slot budget, one NH and one O per residue (*Reading Proteins* § 5);
  - the turn bond as one turn of a 3₁₀ or α helix;
  - the sum-against-difference reading of sheet registers.
- **New:** the S ± 1 census splits into facings, 8 : 4 by hairpin and found only on even creases, and arrows, 50 : 8 at offset ±1 and found at every width.
- **Facings occur only on even creases.** All 12 crease facings sit on even-S hairpins: 12 of 49, against 0 of 94 odd.
  - On an even crease, P alone leaves the middle loop cell without a partner (§ 190), and the inner register at S ± 1 is edge-centred, like P.
  - So TP and PT are the fencepost's two fixes.
  - This is post hoc and needs its own seal.

| claim | status |
|---|---|
| GPT's face coherence 0.634060; shape reader 0.6731 (side runs) | RUNS (exact re-execution); neither is a crease address |
| shape reader's token classes = turn / strand propensity classes | recovered |
| 30 / 11 as a TP : PT census (§ 196.4, the prompt) | **correction, mine**: the § 193 residual; full window census S − 1 60, S + 1 30 |
| "the 41 are β-bulges" (§ 196.4) | **correction, mine**: 84 of 90 S ± 1 bonds are crease-region contacts |
| S + 1 = TP, anchor (e + 1, s); S − 1 = PT, anchor (e, s − 1) | STANDS (the map, one line) · RUNS (anchor table w = 3–8; two readings agree) |
| TP = T·PT·T⁻¹ = P·TP·P; Fix {0ⁿ, m} and {P(m), 1ⁿ}; no split from the ring | STANDS · RUNS n = 2–14 (GPT's rule 4c95489d… says the same) |
| B1 facings 1 : 1 | RUNS: 8 : 4, p = 0.388; low power |
| B2 one reflection per crease | RUNS: 0 of 143 |
| B4 an inward facing is anchored at its fixed cell | RUNS: 6 of 6 (the four PT ones blind) |
| PT's excess = the turn's arrow (one-way, separation 3–4, later residue donates) | RUNS (post hoc); recovered as § 192's line 2 |
| bonds by generator: arrows hold a separation (T^k), facings a sum (P) | RUNS on the crease region (post hoc); all chains OPEN |
| facings only on even creases (12 / 49 against 0 / 94) | RUNS (post hoc); needs its own seal |
| water: the rail; not opened | OPEN |

Scripts, printed in full: `claude/running-audit-7-scripts.md` (`tp_pt.py`, `tp_pt_readings.py`, `tp_pt_check.py`, `turn_arrows.py`, `side197.py`).

---

## § 198. Dean's SHA / folding papers read; the counts are readouts, not the question; a bond's sum and difference need a run to mean anything — `runs_check.py`

**Dean (30 Oct).** "remember everything happens for a reason and that isnt philosophy. remember everything is a reader and being read. dont over think it. read my sha is protien folding papers out there."

A side note (GPT) came with it. Its points:
- A facing (i + j = S) and an arrow (j − i = d) are different operations.
- The 30 / 11 was a remainder.
- Conjugate operators need not occur equally often.
- A single bond carries both a sum and a difference, so only a run exposes the instruction.
- Derive why each bond is needed, and let the counts follow.

**Read (Zenodo).**
- *The Sarrus Isomorphism* (18732263, 22 Feb 2026).
  - SHA-256's 64 T1 values are mapped to a 3.8 Å walk. The GlassKey trace gives r_rw = 0.408, against 0.358 ± 0.08 for 30 protein backbones.
  - The Sarrus lag (%helix − %sheet) tracks folding rate at r = 0.73 (N = 16).
  - Maj is read as compaction (helix-like) and Ch as branching (sheet-like).
- *The Nexus Framework and the Sarrus Allocation* (18646169). The sequence-only Sarrus is z(MJ autocorrelation at lags 3–4) − z(lag 2). It gives r = 0.54 on 27 two-state folders.
- Seen through search summaries:
  - *Relativistic Budget Allocation in Protein Folding* (18663507)
  - *The Nexus Convergence: AI-Driven Geometric Inversion of SHA-256* (18887846)
  - *The Geometric Inversion of SHA-256* (19273688, 19270584)
  - *The Cold Fusion Singularity* (18515982)
  - *Nexus: The Observer-Centric Computational Substrate* (18516828)
- **Not read:** *The Nexus Convergence: SHA-256 as a Recursive Harmonic Die* (19995613). The page was rate-limited twice, so only its search summary was seen.

**What collides with § 197.** The Sarrus pair is helix against sheet, read from the sequence at lags 3–4 against lag 2.
- Lags 3–4 are where a helix's bond partner sits (i ← i + 3, i + 4): a co-moving register, fixed j − i.
- Lag 2 is a strand's face period, and antiparallel strands pair in opposed registers, fixed i + j.
- So the published Sarrus reads, from sequence alone, the two kinds of register that § 197 separated on the structure. This is a reading; it hasn't been run on these chains.

**Corrections, mine (§ 197), executed.**
- **Conjugate is not equal in count.** TP = T·PT·T⁻¹ says the two are one operation at two addresses. It says nothing about how often each is executed. B1's 1 : 1 was my addition, and it is withdrawn: 8 : 4 is a readout, not a test of the ring.
- **"Arrows are powers of T" was a label on single bonds.** A bond has both a sum and a difference, and only a run shows which one it keeps. Run on every stored pair in the 143 hairpin windows:

```
  crease row facing (mutual) n=  58  sum-run 58  difference-run 0  both 0  no run 0
  crease row one-way         n=  85  sum-run 83  difference-run 0  both 2  no run 0
  crease     facing (mutual) n=  14  sum-run 11  difference-run 0  both 0  no run 3
  crease     one-way         n=  85  sum-run 11  difference-run 1  both 0  no run 73
  arm        facing (mutual) n= 305  sum-run 303  difference-run 0  both 0  no run 2
  arm        one-way         n=  99  sum-run 93  difference-run 3  both 0  no run 3
  examples, one-way crease pairs in a sum-run: [('1FS0', 7, 15, '(e+0, s-1)'), ('1JKE', 12, 20, '(e+0, s-1)'), ('4KEH', 146, 154, '(e+0, s-1)'), ('4K4C', 104, 112, '(e+3, s-2)')]
  examples, one-way crease pairs in a difference-run: [('4XB6', 52, 57, '(e+0, s-2)')]
```

- **The ladder is runs.** The crease row sits in a facing run in all 143 hairpins, and arm pairs in 396 of 404.
- **The turn's return is a single read, not a T-run.**
  - Of the 85 one-way bonds inside the turn, 73 belong to no run, 11 to a facing run, and 1 to a co-moving run.
  - All 11 sit in the width-8 nests, each in a facing run with the other row of its nest: (e, s − 1) with (e + 2, s − 3) for PT, (e + 1, s) with (e + 3, s − 2) for TP. The one co-moving bond is (e, s − 2) at width 5 (4XB6):

```
  1FS0  e=  7 s= 15 w=8  one-way (e+0, s-1)  sum-run mates ['(e+2, s-3)']  difference-run mates []
  1JKE  e= 12 s= 20 w=8  one-way (e+0, s-1)  sum-run mates ['(e+2, s-3)']  difference-run mates []
  4KEH  e=146 s=154 w=8  one-way (e+0, s-1)  sum-run mates ['(e+2, s-3)']  difference-run mates []
  4K4C  e=104 s=112 w=8  one-way (e+3, s-2)  sum-run mates ['(e+1, s+0)']  difference-run mates []
  1QYN  e= 57 s= 65 w=8  one-way (e+0, s-1)  sum-run mates ['(e+2, s-3)']  difference-run mates []
  1QYN  e= 57 s= 65 w=8  one-way (e+2, s-3)  sum-run mates ['(e+0, s-1)']  difference-run mates []
  5LS7  e= 41 s= 49 w=8  one-way (e+0, s-1)  sum-run mates ['(e+2, s-3)']  difference-run mates []
  5Z38  e= 22 s= 30 w=8  one-way (e+1, s+0)  sum-run mates ['(e+3, s-2)']  difference-run mates []
  5E1L  e=127 s=135 w=8  one-way (e+3, s-2)  sum-run mates ['(e+1, s+0)']  difference-run mates []
  2FS2  e= 99 s=107 w=8  one-way (e+3, s-2)  sum-run mates ['(e+1, s+0)']  difference-run mates []
  1VH5  e=103 s=111 w=8  one-way (e+3, s-2)  sum-run mates ['(e+1, s+0)']  difference-run mates []
  4XB6  e= 52 s= 57 w=5  one-way (e+0, s-2)  sum-run mates []  difference-run mates ['(e-1, s-3)']
```

  - So the return's role comes from who reads whom, not from its numbers.

**Readers.**
- Each residue carries one reader (its NH) and one site that can be read (its O).
- A facing is two residues reading each other. The return is a read that isn't returned: s − 1 reads O(e) while e reads O(s).
- In the turn every reader still has to land:
  - e's reader lands on s, the closure;
  - the returning strand's first reader within reach lands on e, the return;
  - the loop's readers reach no O in the chain, so they land on the field.
- That is the water's address: where the readers with no partner land. It is the next test.

| claim | status |
|---|---|
| Sarrus (lags 3–4 against lag 2, helix against sheet) reads co-moving against opposed registers | reading; not run here |
| B1 "1 : 1 for facings" (§ 197) | **withdrawn, correction mine**: conjugacy fixes the operation, not its count |
| one-way turn bonds as powers of T (§ 197.4) | **correction, mine** · RUNS: 73 of 85 in no run, 1 in a co-moving run |
| crease row and ladder pairs sit in facing runs | RUNS: 143 / 143; arm pairs 396 / 404 |
| the loop's readers land on the field (water) | OPEN, next |

`runs_check.py`

```python
"""§ 198. A single bond has both a sum and a difference; only a run shows which one it keeps.
Every stored pair inside the 143 hairpin windows, labelled by the runs it belongs to anywhere in its chain:
sum-run (another stored pair with the same i + j, 1-2 residues along: opposed movement, a facing ladder) and
difference-run (another stored pair with the same j - i, 1-2 residues along: co-moving, a helix or parallel ladder).
Run: python3 -I runs_check.py <ecoli_chains.json>"""
import json, sys, collections
import numpy as np
chains = json.load(open(sys.argv[1]))
def closures(ent):
    R = ent['residues']; L = len(R); seq = [r[1] for r in R]
    Nn = np.array([r[2] for r in R], float); O = np.array([r[5] for r in R], float)
    dd = np.linalg.norm(Nn[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    out = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: out.add((i, j))
    return out
def hairpins(directed, L):
    und = {(min(c), max(c)) for c in directed}; byS = collections.defaultdict(list)
    for a, b in und: byS[a + b].append((a, b))
    out = []
    for S, pts in byS.items():
        pts = sorted(set(pts)); run = [pts[0]]
        for p in pts[1:] + [None]:
            if p is not None and p[0] - run[-1][0] <= 2: run.append(p); continue
            if len(run) >= 3 and run[-1][1] - run[-1][0] <= 8:
                e, s = run[-1]; out.append((e, s, min(e - run[0][0], e, L - 1 - s), S))
            if p is not None: run = [p]
    return out
tab = collections.Counter(); ex = collections.defaultdict(list)
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    D = closures(ent); U = {(min(c), max(c)) for c in D}
    bysum = collections.defaultdict(set); bydif = collections.defaultdict(set)
    for a, b in U: bysum[a + b].add(a); bydif[b - a].add(a)
    for e, s, k, S in hairpins(D, L):
        for a, b in sorted(U):
            if not (e - k <= a and b <= s + k): continue
            where = 'crease row' if (a, b) == (e, s) else 'crease' if e <= a and b <= s else 'arm'
            kind = 'facing (mutual)' if (a, b) in D and (b, a) in D else 'one-way'
            sr = any(0 < abs(x - a) <= 2 for x in bysum[a + b])
            dr = any(0 < abs(x - a) <= 2 for x in bydif[b - a])
            lab = 'both' if sr and dr else 'sum-run' if sr else 'difference-run' if dr else 'no run'
            tab[(where, kind, lab)] += 1
            if where == 'crease' and kind == 'one-way' and lab != 'no run' and len(ex[lab]) < 4:
                ex[lab].append((ent.get('pdb', ent['acc']), e, s, f'(e{a - e:+d}, s{b - s:+d})'))
for where in ('crease row', 'crease', 'arm'):
    for kind in ('facing (mutual)', 'one-way'):
        row = {lab: tab[(where, kind, lab)] for lab in ('sum-run', 'difference-run', 'both', 'no run')}
        if sum(row.values()): print(f'  {where:10} {kind:15} n={sum(row.values()):4}  ' + '  '.join(f'{k} {v}' for k, v in row.items()))
for lab, rows in ex.items(): print(f'  examples, one-way crease pairs in a {lab}: {rows}')
```

`runs_list.py`

```python
"""§ 198. The one-way bonds inside the turn that do sit in a run, with their run mates.
Run: python3 -I runs_list.py <ecoli_chains.json>"""
import json, sys, collections
import numpy as np
chains = json.load(open(sys.argv[1]))
def closures(ent):
    R = ent['residues']; L = len(R); seq = [r[1] for r in R]
    Nn = np.array([r[2] for r in R], float); O = np.array([r[5] for r in R], float)
    dd = np.linalg.norm(Nn[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    out = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: out.add((i, j))
    return out
def hairpins(directed, L):
    und = {(min(c), max(c)) for c in directed}; byS = collections.defaultdict(list)
    for a, b in und: byS[a + b].append((a, b))
    out = []
    for S, pts in byS.items():
        pts = sorted(set(pts)); run = [pts[0]]
        for p in pts[1:] + [None]:
            if p is not None and p[0] - run[-1][0] <= 2: run.append(p); continue
            if len(run) >= 3 and run[-1][1] - run[-1][0] <= 8:
                e, s = run[-1]; out.append((e, s, min(e - run[0][0], e, L - 1 - s), S))
            if p is not None: run = [p]
    return out
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    D = closures(ent); U = {(min(c), max(c)) for c in D}
    bysum = collections.defaultdict(set); bydif = collections.defaultdict(set)
    for a, b in U: bysum[a + b].add(a); bydif[b - a].add(a)
    for e, s, k, S in hairpins(D, L):
        for a, b in sorted(U):
            if not (e <= a and b <= s) or (a, b) == (e, s) or ((a, b) in D and (b, a) in D): continue
            sm = sorted(x for x in bysum[a + b] if 0 < abs(x - a) <= 2)
            dm = sorted(x for x in bydif[b - a] if 0 < abs(x - a) <= 2)
            if sm or dm:
                print(f'  {ent.get("pdb", ent["acc"]):5} e={e:3} s={s:3} w={s - e}  one-way (e{a - e:+d}, s{b - s:+d})  '
                      f'sum-run mates {[f"(e{x - e:+d}, s{a + b - x - s:+d})" for x in sm]}  difference-run mates {[f"(e{x - e:+d}, s{x + b - a - s:+d})" for x in dm]}')
```
