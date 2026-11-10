# The running audit, continued (§ 195 –)

Continues `claude/running-audit-5.md` (§§ 192–194). Same rules: live output only; STANDS / RUNS / DEAD END / OPEN, never CONFIRMED; scripts printed in full.

---

## § 195. The ring is the instruction set, in the differences: the crease step is one transposition, the wrap step is C, and the ring's program is an exact mirror in the shape channel with every correction in the face channel; ℓ(n) and the record's centre nesting proved; the value mirror as crease address is a DEAD END; the methods pulled into one notebook — `mirror_centre.py`, `ring_isa.py`, *NEXUS Methods v1*

**Dean (30 Oct).** The § 194 prompt back (score every centre by the value mirror b(S − i) = b(i), seal, rank the true S
within ± 8, nulls), with GPT's run of the same prompt (*NEXUS § 195 Local Face and Mirror Centre*: .md, single-cell
.ipynb, results .json, chat text), and: "start pulling out the code, the methods. and we need to get back to the rings.
that is our ISA in the differences."

### 195.1 The value mirror as the crease address — DEAD END, by two independent runs

```
RULE  SHA-256 5bc9c74246b984c7c5a86d0446a13e0d5df14ffcbceef0b5e7034fd8158216f1
STAGE A  centres scored 38499; scores SHA-256 bd44ddb3786961f6b877178f530843507888b732db8965997fdd2d42ec521729
STAGE B  hairpins 143; true S rank 1: 10; top 3: 27; mean advantage 0.5299; score at true S: {0: 67, 1: 38, 2: 13, 3: 8, 4: 4, 5: 4, 6: 4, 7: 3, 10: 1, 12: 1}
  S even: n=49 mean advantage 0.4962
  S odd: n=94 mean advantage 0.5475
  null shuffle: mean 0.4985 sd 0.0230  P(null >= obs) 0.100
  null shifted centre: mean 0.5014 sd 0.0227  P(null >= obs) 0.119
STAGE C  diagnostic (structure-conditioned: e, s, k from the detector)
  ladder rows: b(e-t) = b(s+t) in 540 of 927 (0.583); same residues paired at random 0.492
  central pair inside the loop: equal in 76 of 143 (0.531); loop residues paired at random 0.473
```

DEAD END. 10 first and 27 in the top 3; mean advantage 0.5299 against 0.4985 (shuffled sequences) and 0.5014 (shifted
centres), P ≈ 0.10 and 0.12. GPT's run gives the same 10 / 27 / 0.5299 (P 0.113, 0.092), so the two agree to the digit.
Even S carries nothing (0.4962); odd S a little (0.5475). Both sealed diagnostic bars miss narrowly. Ladder rows agree on
the value bit 0.583 against the bar of 0.60 (random pairing 0.492). The loop's central pair sits at 0.531 against 0.473,
0.058 apart where the bar allowed 0.05.

**Correction, mine (the prompt).** The prompt scored consecutive agreements outward *from the centre*. That starts inside
the loop, whose residues are on no ladder row, and it multiplies per-row agreement: at 0.58 a row, a run is over within
a row or two. The reader asked the value channel for the address; § 195.3 shows why the ring keeps its mirror in the
other channel.

### 195.2 GPT's § 195, read in full

The notebook's one cell is byte-identical to the .md § 6 code. Its saved output equals the .md § 7 trace, and the .json
summary matches (0.5299 / 0.4997 / 0.5006). It used the same data (the same 143). Three notes:
- **Its slot table is not the record's.** It has C 0, M 0, D/E/N/Q 4, R 5, H 2, W 1. Its remark that "C and M differ"
  between the binary and the slot table is about that table. Under *Reading Proteins* § 5 as written (§ 194: C 2, M 2,
  W 2; r = −0.81), the binary is exactly WET > 0.
- **Its local-normal face geometry is known β-sheet geometry, recovered.** That is 801/822 paired rows on the same local
  face and 1,370/1,404 alternation. Its 112/141 dry-face call needs the finished coordinates, which it says itself.
- **Its next prompt** (a face-coherence score over widths 3–8) is input, not taken here.

### 195.3 The rings: the instruction set lives in the differences

The record's split of a word into a face bit f = b₀ (value channel) and a shape word δᵢ = bᵢ ⊕ bᵢ₊₁ (shape channel) is
invertible (*From One Difference to the Shape Channel* § 3.2). The native partner reverses the shape for every word
(same place). The rest is run here.

```
1  the split and the operators acting on it, all words, n = 2..12
  n=2: (f, delta) bijective True; C keeps delta, flips f True; P reverses delta True   [recovered: From One Difference s 3.2]
  n=3: (f, delta) bijective True; C keeps delta, flips f True; P reverses delta True   [recovered: From One Difference s 3.2]
  n=12: (f, delta) bijective True; C keeps delta, flips f True; P reverses delta True   [recovered: From One Difference s 3.2]
2  lemma: the representatives with leading bit 1 are exactly 1.y.1 with y < J(y), y of width n-2
  n=4: equal True (1 words)
  n=5: equal True (2 words)
  n=14: equal True (2016 words)
   corollaries, checked against the built rings:
  n= 2:                            l(n)=   1 formula None   seam step flips positions [0, 1]: one transposition True, centred True (between two middle cells)
  n= 3:                            l(n)=   1 formula None   seam step flips positions [0, 2]: one transposition True, centred True (around the middle cell)
  n= 4: m(n) = 1.m(n-2).1 True     l(n)=   1 formula 1   seam step flips positions [1, 2]: one transposition True, centred True (between two middle cells)
  n= 5: m(n) = 1.m(n-2).1 True     l(n)=   2 formula 2   seam step flips positions [1, 3]: one transposition True, centred True (around the middle cell)
  n= 6: m(n) = 1.m(n-2).1 True     l(n)=   6 formula 6   seam step flips positions [2, 3]: one transposition True, centred True (between two middle cells)
  n= 7: m(n) = 1.m(n-2).1 True     l(n)=  12 formula 12   seam step flips positions [2, 4]: one transposition True, centred True (around the middle cell)
  n= 8: m(n) = 1.m(n-2).1 True     l(n)=  28 formula 28   seam step flips positions [3, 4]: one transposition True, centred True (between two middle cells)
  n= 9: m(n) = 1.m(n-2).1 True     l(n)=  56 formula 56   seam step flips positions [3, 5]: one transposition True, centred True (around the middle cell)
  n=10: m(n) = 1.m(n-2).1 True     l(n)= 120 formula 120   seam step flips positions [4, 5]: one transposition True, centred True (between two middle cells)
  n=11: m(n) = 1.m(n-2).1 True     l(n)= 240 formula 240   seam step flips positions [4, 6]: one transposition True, centred True (around the middle cell)
  n=12: m(n) = 1.m(n-2).1 True     l(n)= 496 formula 496   seam step flips positions [5, 6]: one transposition True, centred True (between two middle cells)
  n=13: m(n) = 1.m(n-2).1 True     l(n)= 992 formula 992   seam step flips positions [5, 7]: one transposition True, centred True (around the middle cell)
  n=14: m(n) = 1.m(n-2).1 True     l(n)=2016 formula 2016   seam step flips positions [6, 7]: one transposition True, centred True (between two middle cells)
3  the step program: D_k = R[k] XOR R[k+1]; its shape part delta(D_k) and face part f(D_k)
  n= 2: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 2; wrap step = 1^n True; steps with zero shape change [1, 3]; distinct steps 2 of 4
         R = [0, 2, 1, 3]
         D = [2, 3, 2, 3]
  n= 3: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 6; wrap step = 1^n True; steps with zero shape change [7]; distinct steps 6 of 8
         R = [0, 1, 2, 6, 3, 5, 4, 7]
         D = [1, 3, 4, 5, 6, 1, 3, 7]
  n= 4: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 6; wrap step = 1^n True; steps with zero shape change [15]; distinct steps 9 of 16
  n= 6: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 14; wrap step = 1^n True; steps with zero shape change [63]; distinct steps 22 of 64
  n= 8: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 30; wrap step = 1^n True; steps with zero shape change [255]; distinct steps 36 of 256
  n=12: D(N-2-a) = J(D(a)) xor flag*1^n True; shape part exact mirror True; flags only in the face part True; flags 126; wrap step = 1^n True; steps with zero shape change [4095]; distinct steps 76 of 4096
```

(In block 3 the "steps with zero shape change" list gives step *indices* for n ≥ 3 [index N − 1, the wrap] and, at
n = 2, indices 1 and 3: there the seam step `11` is also C.)

**Lemma.** For n ≥ 4 the representatives (x < P(x)) with leading bit 1 are exactly 1·y·1 with y of width n − 2 and
y < J(y). *Proof.* A palindrome with leading 1 has P(x) = C(x) leading 0, so it is no representative. Otherwise P(x) =
J(x), whose leading bit is x's last bit. x < J(x) forces it to 1, so x = 1·y·1, J(x) = 1·J(y)·1, and x < J(x) ⇔
y < J(y). ∎

**Corollary 1 (encapsulation).** m(n) = 1·m(n − 2)·1 and P(m(n)) = 1·P(m(n − 2))·1 for n ≥ 4. Leading-1
representatives exist from n = 4 and outrank all leading-0 words. So m(n) = 1·y*·1 with y* the largest y < J(y) at
width n − 2, and y* = m(n − 2) by the same lemma (directly at widths 2 and 3). m is no palindrome, so P = J passes
through the shell. The crease of a wider ring is the narrower crease wrapped in 1…1. That proves at every width the
centre nesting the record observed with finite checks (*From One Difference* § 3.3: C_{n+2} = 1C_n1, reading C_n as the
seam pair). Read with Dean's (((()))): the crease is built outward, one shell per two bits of width.

**Corollary 2 (the doubling stop, § 189).** For n ≥ 4, m and P(m) both lead with 1. So the leading-1 cells of the
listed half are exactly the leading-1 representatives, the largest of the rising list, closing it. The leading bit turns
at N/2 − ℓ(n) with ℓ(n) = #{y < J(y)} at width n − 2 = (2ⁿ⁻² − 2^⌈(n−2)/2⌉)/2 = 2ⁿ⁻³ − 2^⌊(n−3)/2⌋. § 189 read this
off its table as RUNS n = 4–12; it is now STANDS.

**Corollary 3 (the crease step is one transposition).** The seam step P(m) ⊕ m nests as 0·(seam step at n − 2)·0. It is
11 on m = 01 at n = 2 and 101 on m = 011 at n = 3, and in both the two flipped bits of m differ. So at every width the
crease step swaps two bits placed symmetrically about the word's centre: the two middle cells (even n) or the two cells
around the middle one (odd n).

**The step program.** D(N − 2 − a) = P(R[a + 1]) ⊕ P(R[a]) = J(D(a)) ⊕ φ(a)·1ⁿ, with φ(a) = 1 exactly when one of R[a],
R[a + 1] is a palindrome. That uses J linear over XOR, C(x) = x ⊕ 1ⁿ, and J(x) = x on palindromes. The shape map sends 1ⁿ
to 0 and J to reversal. So the ring's program, read in the shape channel, is its own exact mirror, and every correction
rides in the face channel. The wrap step is P(0) ⊕ 0 = 1ⁿ: C, the one instruction that changes the value and not the
shape. The bit-stream relative is the record's eq. (10) in *Native Binary Rings* (B(S − 1 − t) = B(t) ⊕ χ_pal); the step
form and its channel split are new here, a one-line corollary of the facing law. The facing step x ⊕ P(x) is always a
nonzero palindrome, all widths (the record states it for even n).

**Reading for the chain (not evidence).** The ring's two self-facing steps are the two operations the fold work isolated:
- The wrap is C, a value-only flip. That is § 185 (held ↔ running, the shape kept) and the face bit of § 194.
- The seam is one transposition. That is the zipper's crease row, a transposition of two cells' slots (§ 193).

The ring keeps its mirror in the shape channel and puts its corrections in the face channel. The hairpins split the same
way: the bond-row mirror lands (0.835), face averages land (0.776), the residue-value mirror does not (above). The ring's
two nesting towers put the crease between cells (even n) and around a cell (odd n). § 192 found the hairpin's two
crease parities to be one program; the ring has one instruction in two towers.

### 195.4 The methods pulled out

*NEXUS_Methods_v1_Ring_ISA_and_Local_Compiler.ipynb*: one library cell (ring layer, square layer, chain layer, local
compiler, seal and land) and four check cells that re-run § 195.3 and §§ 188–195 from it. It reproduces the audit's
seals (§ 193 emitted list 17584c67…, § 195 scores bd44ddb3…) and every number above. It finds its data beside the
notebook, in `NEXUS_DATA`, or inside `NEXUS_Fold_Compiler_Notebook (2).zip` (tested both ways), and runs in about
4 s. It carries the method table, the four proofs and the ledger in its markdown cells. The library code is also in
the project as `claude/nexus-methods-v1.md`.

| claim | status |
|---|---|
| value mirror b(S − i) = b(i) as the crease address (two independent runs agree) | DEAD END: 10/143 first, advantage 0.5299 vs 0.4985 / 0.5014 |
| ladder-row value agreement 0.583 (bar 0.60); loop central pair 0.531 vs 0.473 (bar ± 0.05) | both sealed diagnostic bars missed narrowly |
| prompt design: run length from the centre reads the loop and multiplies per-row agreement | correction, mine |
| GPT § 195: notebook = .md; outputs match; its slot table is not the record's § 5 | read; noted |
| (f, δ) split; P reverses δ; C value-only | recovered (*From One Difference* § 3.2) · RUNS n = 2–12 |
| lemma: leading-1 representatives = 1·y·1, y < J(y) | STANDS (proof) · RUNS n = 4–14 |
| encapsulation m(n) = 1·m(n − 2)·1, seam pair nests | STANDS (proof); the record had it observed |
| ℓ(n) = 2ⁿ⁻³ − 2^⌊(n−3)/2⌋ | STANDS (proof); upgrades § 189 |
| seam step = one centred transposition, every width | STANDS (proof) · RUNS n = 2–14 |
| step program: shape mirror exact, flags only in the face channel; wrap = C | STANDS (one line) · RUNS n = 2–12 |
| facing step x ⊕ P(x) a nonzero palindrome, all n | STANDS |
| wrap = C ↔ value channel; seam = transposition ↔ crease row | reading, not evidence |
| methods notebook v1 | RUNS (reproduces §§ 188–195 and the seals) |
| crease address along the chain; distant partner | OPEN |

`mirror_centre.py`

```python
"""§ 195. The value bit as a mirror-centre reader. Run: python3 -I mirror_centre.py <ecoli_chains.json>
Stage A (sequence only): b(i) = 0 for G A V L I F P, else 1; score every centre S of every chain by how far b(S-i) = b(i)
holds outward from the centre (consecutive pairs, stop at the first mismatch or the chain end). Hash all scores.
Stage B: hairpins from undirected closure pairs (the § 188 detector); rank the true S among S-8..S+8 (midrank ties).
Nulls: composition-preserving shuffle of each chain (200 per chain set), and a centre shifted at random within +-8.
Stage C (structure-conditioned diagnostic, bars sealed with the rule): value agreement b(e-t) = b(s+t) on ladder rows
against the same hairpin's residues paired at random, and agreement of the turn's own central pair."""
import hashlib, json, sys, collections, random
import numpy as np

ZERO = set('GAVLIFP')
RULE = ("b(i)=0 iff residue in GAVLIFP. score(S): odd S=2c+1 compares (c,c+1),(c-1,c+2),...; even S=2c compares (c-1,c+1),...; "
        "consecutive equal pairs from the centre until the first unequal pair or a chain end, uncapped. Rank true S in S-8..S+8 "
        "(valid S only), midrank ties, advantage=(n-rank)/(n-1). Nulls: per-chain composition shuffle (200), random shifted "
        "centre within +-8. Diagnostic bars: ladder-row value agreement >= 0.60 and above its within-hairpin random pairing; "
        "central turn pair agreement within 0.05 of random pairing (the turn interior is not on a face).")
print('RULE  SHA-256', hashlib.sha256(RULE.encode()).hexdigest())

def scores(bits):
    L = len(bits); out = []
    for S in range(2 * L - 1):
        a, b = ((S - 1) // 2, (S + 1) // 2) if S % 2 else (S // 2 - 1, S // 2 + 1)
        n = 0
        while a >= 0 and b < L and bits[a] == bits[b]: n += 1; a -= 1; b += 1
        out.append(n)
    return out
chains = json.load(open(sys.argv[1]))
seqs = [''.join(r[1] for r in e['residues']) for e in chains]
BITS = [[0 if a in ZERO else 1 for a in s] for s in seqs]
SC = [scores(b) for b in BITS]
seal = hashlib.sha256(json.dumps(SC, separators=(',', ':')).encode()).hexdigest()
print(f'STAGE A  centres scored {sum(map(len, SC))}; scores SHA-256 {seal}'); sys.stdout.flush()

hp = []
for ci, ent in enumerate(chains):
    R = ent['residues']; L = len(R)
    if L < 30: continue
    seq = seqs[ci]; N = np.array([r[2] for r in R]); O = np.array([r[5] for r in R])
    dd = np.linalg.norm(N[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    und = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: und.add((min(i, j), max(i, j)))
    byS = collections.defaultdict(list)
    for a, b in und: byS[a + b].append((a, b))
    for S, pts in byS.items():
        pts = sorted(set(pts)); run = [pts[0]]
        for p in pts[1:] + [None]:
            if p is not None and p[0] - run[-1][0] <= 2: run.append(p); continue
            if len(run) >= 3 and run[-1][1] - run[-1][0] <= 8:
                e, s = run[-1]; hp.append((ci, e, s, min(e - run[0][0], e, L - 1 - s), S))
            if p is not None: run = [p]
def rank(S, sc):
    lo, hi = max(0, S - 8), min(len(sc) - 1, S + 8); w = sc[lo:hi + 1]; v = sc[S]
    r = 1 + sum(x > v for x in w) + 0.5 * (sum(x == v for x in w) - 1)
    return r, (len(w) - r) / (len(w) - 1)
obs = [rank(S, SC[ci]) for ci, e, s, k, S in hp]
adv = np.mean([a for r, a in obs])
print(f'STAGE B  hairpins {len(hp)}; true S rank 1: {sum(r == 1 for r, a in obs)}; top 3: {sum(r <= 3 for r, a in obs)}; '
      f'mean advantage {adv:.4f}; score at true S: {dict(sorted(collections.Counter(SC[ci][S] for ci, e, s, k, S in hp).items()))}')
for par in (0, 1):
    sub = [a for (r, a), h in zip(obs, hp) if h[4] % 2 == par]
    print(f'  S {"even" if par == 0 else "odd"}: n={len(sub)} mean advantage {np.mean(sub):.4f}')
rng = random.Random(195); sh = []; shift = []
used = sorted({h[0] for h in hp})
for rep in range(200):
    SCs = {}
    for ci in used:
        b = BITS[ci][:]; rng.shuffle(b); SCs[ci] = scores(b)
    sh.append(np.mean([rank(S, SCs[ci])[1] for ci, e, s, k, S in hp]))
    vals = []
    for ci, e, s, k, S in hp:
        cand = [x for x in range(max(0, S - 8), min(len(SC[ci]), S + 9)) if x != S]
        vals.append(rank(rng.choice(cand), SC[ci])[1])
    shift.append(np.mean(vals))
sh, shift = np.array(sh), np.array(shift)
print(f'  null shuffle: mean {sh.mean():.4f} sd {sh.std():.4f}  P(null >= obs) {(1 + (sh >= adv).sum()) / 201:.3f}')
print(f'  null shifted centre: mean {shift.mean():.4f} sd {shift.std():.4f}  P(null >= obs) {(1 + (shift >= adv).sum()) / 201:.3f}')

print('STAGE C  diagnostic (structure-conditioned: e, s, k from the detector)')
row_eq = row_n = 0; row_null = []; turn_eq = turn_n = 0; turn_null = []
for ci, e, s, k, S in hp:
    b = BITS[ci]; arm = [x for t in range(k + 1) for x in (e - t, s + t)]
    for t in range(k + 1): row_eq += b[e - t] == b[s + t]; row_n += 1
    pool = [b[x] for x in arm]
    for _ in range(50):
        rng.shuffle(pool); row_null.append(np.mean([pool[2 * t] == pool[2 * t + 1] for t in range(k + 1)]))
    c1, c2 = ((S - 1) // 2, (S + 1) // 2) if S % 2 else (S // 2 - 1, S // 2 + 1)
    if e < c1 and c2 < s:                                    # the central pair lies inside the loop
        turn_eq += b[c1] == b[c2]; turn_n += 1
        loop = [b[x] for x in range(e + 1, s)]
        turn_null.append(np.mean([loop[i] == loop[j] for i in range(len(loop)) for j in range(i + 1, len(loop))]) if len(loop) > 1 else 0.5)
print(f'  ladder rows: b(e-t) = b(s+t) in {row_eq} of {row_n} ({row_eq/row_n:.3f}); same residues paired at random {np.mean(row_null):.3f}')
print(f'  central pair inside the loop: equal in {turn_eq} of {turn_n} ({turn_eq/turn_n:.3f}); loop residues paired at random {np.mean(turn_null):.3f}')
```

`ring_isa.py`

```python
"""§ 195 (rings). The ring's instruction set in the differences. Run: python3 -I ring_isa.py
Operands: n-bit words x = (b_0 .. b_{n-1}) with b_0 the most significant bit; the face/shape split (f, delta) of the record:
f = b_0, delta_i = b_i XOR b_{i+1} (From One Difference, s 3.2). Operations: J, C, P, the native ring R_n, its steps."""
import collections
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2)
def C(x, n): return x ^ ((1 << n) - 1)
def P(x, n): return C(x, n) if J(x, n) == x else J(x, n)
def ring(n):
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    return reps[:-1] + [P(m, n), m] + [P(x, n) for x in reversed(reps[:-1])]
def face(x, n): return x >> (n - 1)
def shape(x, n): return (x ^ (x >> 1)) & ((1 << (n - 1)) - 1)          # delta word, n-1 bits
def pal(x, n): return J(x, n) == x
popc = lambda x: bin(x).count('1')

print('1  the split and the operators acting on it, all words, n = 2..12')
for n in range(2, 13):
    W = range(1 << n)
    ok_bij = len({(face(x, n), shape(x, n)) for x in W}) == 1 << n
    ok_C = all(shape(C(x, n), n) == shape(x, n) and face(C(x, n), n) == 1 - face(x, n) for x in W)
    ok_P = all(shape(P(x, n), n) == J(shape(x, n), n - 1) for x in W)
    if n in (2, 3, 12): print(f'  n={n}: (f, delta) bijective {ok_bij}; C keeps delta, flips f {ok_C}; P reverses delta {ok_P}   [recovered: From One Difference s 3.2]')

print('2  lemma: the representatives with leading bit 1 are exactly 1.y.1 with y < J(y), y of width n-2')
for n in range(4, 15):
    reps = [x for x in range(1 << n) if x < P(x, n)]
    lead1 = {x for x in reps if face(x, n)}
    built = {(1 << (n - 1)) | (y << 1) | 1 for y in range(1 << (n - 2)) if y < J(y, n - 2)}
    if n in (4, 5, 14) or lead1 != built: print(f'  n={n}: equal {lead1 == built} ({len(lead1)} words)')
print('   corollaries, checked against the built rings:')
for n in range(2, 15):
    R = ring(n); N = len(R); h = N // 2
    m, Pm = R[h], R[h - 1]
    nest = '' if n < 4 else ('m(n) = 1.m(n-2).1 ' + str(m == (1 << (n - 1)) | (ring(n - 2)[(1 << (n - 2)) // 2] << 1) | 1))
    lead = [face(x, n) for x in R]; t = lead.index(1); ell = h - t
    ell_formula = (1 << (n - 3)) - (1 << ((n - 3) // 2)) if n >= 4 else None
    d_seam = Pm ^ m
    bits = [k for k in range(n) if d_seam >> (n - 1 - k) & 1]                 # positions flipped by the seam step
    swap = len(bits) == 2 and ((m >> (n - 1 - bits[0])) & 1) != ((m >> (n - 1 - bits[1])) & 1)
    centred = bits[0] + bits[1] == n - 1
    print(f'  n={n:2}: {nest:26} l(n)={ell:4} formula {ell_formula}   seam step flips positions {bits}: '
          f'one transposition {swap}, centred {centred} ({"between two middle cells" if n % 2 == 0 else "around the middle cell"})')

print('3  the step program: D_k = R[k] XOR R[k+1]; its shape part delta(D_k) and face part f(D_k)')
for n in range(2, 13):
    R = ring(n); N = len(R)
    D = [R[k] ^ R[(k + 1) % N] for k in range(N)]
    flags = [int(pal(R[a], n) != pal(R[a + 1], n)) for a in range(N - 1)]
    law = all(D[N - 2 - a] == J(D[a], n) ^ (flags[a] * ((1 << n) - 1)) for a in range(N - 1))
    shape_mirror = all(shape(D[N - 2 - a], n) == J(shape(D[a], n), n - 1) for a in range(N - 1))
    face_carries = all(face(D[N - 2 - a], n) == (D[a] & 1) ^ flags[a] for a in range(N - 1))
    wrap = D[N - 1]; pure_face = [k for k in range(N) if shape(D[k], n) == 0]
    ops = collections.Counter(D)
    if n <= 4 or n in (6, 8, 12):
        print(f'  n={n:2}: D(N-2-a) = J(D(a)) xor flag*1^n {law}; shape part exact mirror {shape_mirror}; flags only in the face part {face_carries}; '
              f'flags {sum(flags)}; wrap step = 1^n {wrap == (1 << n) - 1}; steps with zero shape change {pure_face}; distinct steps {len(ops)} of {N}'
              + (f'\n         R = {R}\n         D = {D}' if n <= 3 else ''))
```

---

## § 196. Rings inside rings: R_n without its palindromes is the centre of R_{n+2}, so every ring runs the narrower ring's crease program outward; the ring's instruction alphabet in closed form, sealed for n = 13–16 and landed 4 of 4; the zipper as a word; a β-bulge is TP — `ring_alphabet.py`

**Dean (30 Oct).** "again values are relative. like in a circuit. it should match another value like a rail … or be a
difference or if the values change its like moving the multimeter to different parts … if the ring have every difference
per ring something else must be happening too like its folding inward. like ring 2 is in the center of ring 3 words or
ring 4? what i mean is its not a linear progression anywhere. like its anti-linear". Then the § 195 prompt: derive the
alphabet in closed form, seal n = 13–16, build, check; the zipper as a word; the β-bulge.

**Correction, mine (§ 195).** Three things § 195 logged as new proofs were already in the record:
- **The lemma** (leading-1 representatives are 1·y·1 with y < J(y)) is the (1, 1) clause of the record's frame law
  (*NESTED*: "b m c is a representative iff (b, c) = (0, 1), or (0, 0) with m ≤ Jm, or (1, 1) with m < Jm, never
  (1, 0)", RUNS L = 3..14).
- **ℓ(n).** The leading-bit turn at N/2 − ℓ(n) is the record's C₀(n) = 3·2ⁿ⁻³ + 2^(n/2−2), proved for even n
  (*Native Binary Rings* eq. 14, App. A.3, "the 3/8 seam"). § 189's "the stop tends to 3N/8" is that seam, and § 189
  should have cited it. Odd n is a one-line extension (3·2ⁿ⁻³ + 2^((n−3)/2)).
- **Centre nesting.** The centre words nest C_{n+2} = 1·C_n·1 in § 135 (centre words 1, B, 37, EF, …).

The rail reading Dean gives now is also recovered: the shell lamps g_k = b_k ⊕ b_{n−1−k}, fixed by J, C and P (§ 135,
check 8). Of § 195, what remains new is the step form of the facing law with its channel split, and the seam step as one
centred transposition.

```
PREDICTION, sealed before R_13 .. R_16 are built
  For n >= 6 the distinct steps D_k = R[k] xor R[k+1] of R_n are: every single run 0^a 1^k 0^b with a >= 1, except at odd n the lone middle bit; the runs with a = 0 of length k in 1..floor(n/2) and n-2 and n; and the two-run masks: odd n the seam 0^((n-3)/2) 101 0^((n-3)/2), even n the crease-in 0^(n/2-2) 101 0^(n/2-1) and crease-out 0^(n/2-1) 101 0^(n/2-2). Distinct counts: rising (the carries of the rising list) floor((n+1)^2/4) - 2; mirror floor((n+2)^2/4) - 4; rising-and-mirror 3*floor((n-3)/2); total n^2/2 + 4 (even n), (n^2 + 3)/2 (odd n). Every rising step adds one power of two 2^b with b <= ceil(n/2) - 1. Predicted (rising, mirror, overlap, total): n=13: (47, 52, 15, 86); n=14: (54, 60, 15, 102); n=15: (62, 68, 18, 114); n=16: (70, 77, 18, 132).
  SHA-256 3e21796a56aacecfe44f8bda0e91697b4b3ec96a2c86fdf13d491edbc0d333d5

1  built and checked
  n= 6 (derivation set): built (10, 12, 3, 22)  predicted (10, 12, 3, 22)  match True; exact set True; every rising step +2^b True, largest b 2 (bound 2)
  n= 7 (derivation set): built (14, 16, 6, 26)  predicted (14, 16, 6, 26)  match True; exact set True; every rising step +2^b True, largest b 3 (bound 3)
  n= 8 (derivation set): built (18, 21, 6, 36)  predicted (18, 21, 6, 36)  match True; exact set True; every rising step +2^b True, largest b 3 (bound 3)
  n= 9 (derivation set): built (23, 26, 9, 42)  predicted (23, 26, 9, 42)  match True; exact set True; every rising step +2^b True, largest b 4 (bound 4)
  n=10 (derivation set): built (28, 32, 9, 54)  predicted (28, 32, 9, 54)  match True; exact set True; every rising step +2^b True, largest b 4 (bound 4)
  n=11 (derivation set): built (34, 38, 12, 62)  predicted (34, 38, 12, 62)  match True; exact set True; every rising step +2^b True, largest b 5 (bound 5)
  n=12 (derivation set): built (40, 45, 12, 76)  predicted (40, 45, 12, 76)  match True; exact set True; every rising step +2^b True, largest b 5 (bound 5)
  n=13 (sealed        ): built (47, 52, 15, 86)  predicted (47, 52, 15, 86)  match True; exact set True; every rising step +2^b True, largest b 6 (bound 6)
  n=14 (sealed        ): built (54, 60, 15, 102)  predicted (54, 60, 15, 102)  match True; exact set True; every rising step +2^b True, largest b 6 (bound 6)
  n=15 (sealed        ): built (62, 68, 18, 114)  predicted (62, 68, 18, 114)  match True; exact set True; every rising step +2^b True, largest b 7 (bound 7)
  n=16 (sealed        ): built (70, 77, 18, 132)  predicted (70, 77, 18, 132)  match True; exact set True; every rising step +2^b True, largest b 7 (bound 7)

2  rings inside rings: the centre block of R_{n+2} is R_n without its palindromes, each word wrapped 1..1
  n= 2 ->  4: centre block     2 words = 1.(R_2 minus palindromes).1  True;  crease program shared for 0 steps outward (l(n) + 1 = 2)
  n= 3 ->  5: centre block     4 words = 1.(R_3 minus palindromes).1  True;  crease program shared for 0 steps outward (l(n) + 1 = 2)
  n= 4 ->  6: centre block    12 words = 1.(R_4 minus palindromes).1  True;  crease program shared for 1 steps outward (l(n) + 1 = 2)
  n= 5 ->  7: centre block    24 words = 1.(R_5 minus palindromes).1  True;  crease program shared for 2 steps outward (l(n) + 1 = 3)
  n= 6 ->  8: centre block    56 words = 1.(R_6 minus palindromes).1  True;  crease program shared for 6 steps outward (l(n) + 1 = 7)
  n= 7 ->  9: centre block   112 words = 1.(R_7 minus palindromes).1  True;  crease program shared for 12 steps outward (l(n) + 1 = 13)
  n= 8 -> 10: centre block   240 words = 1.(R_8 minus palindromes).1  True;  crease program shared for 28 steps outward (l(n) + 1 = 29)
  n= 9 -> 11: centre block   480 words = 1.(R_9 minus palindromes).1  True;  crease program shared for 56 steps outward (l(n) + 1 = 57)
  n=10 -> 12: centre block   992 words = 1.(R_10 minus palindromes).1  True;  crease program shared for 120 steps outward (l(n) + 1 = 121)
  n=11 -> 13: centre block  1984 words = 1.(R_11 minus palindromes).1  True;  crease program shared for 240 steps outward (l(n) + 1 = 241)
  n=12 -> 14: centre block  4032 words = 1.(R_12 minus palindromes).1  True;  crease program shared for 496 steps outward (l(n) + 1 = 497)
  n=13 -> 15: centre block  8064 words = 1.(R_13 minus palindromes).1  True;  crease program shared for 992 steps outward (l(n) + 1 = 993)
  n=14 -> 16: centre block 16256 words = 1.(R_14 minus palindromes).1  True;  crease program shared for 2016 steps outward (l(n) + 1 = 2017)

3  the zipper as a word (R_8): crease row = seam step; row t pairs R[h-1-t] and R[h+t]; the arms advance by mirrored steps
  t=0: 11110111 | 11101111  facing step 00011000 = seam step 00011000, a transposition
  t=1: 11011111 | 11111011  facing step 00100100 (palindrome True);  arm steps 00101000 | 00010100  mirror pair True
  t=2: 11010111 | 11101011  facing step 00111100 (palindrome True);  arm steps 00001000 | 00010000  mirror pair True
  t=3: 11001111 | 11110011  facing step 00111100 (palindrome True);  arm steps 00011000 | 00011000  mirror pair True
  t=4: 11001011 | 11010011  facing step 00011000 (palindrome True);  arm steps 00000100 | 00100000  mirror pair True
  t=5: 11000111 | 11100011  facing step 00100100 (palindrome True);  arm steps 00001100 | 00110000  mirror pair True
  t=6: 10111111 | 11111101  facing step 01000010 (palindrome True);  arm steps 01111000 | 00011110  mirror pair True
  steps that are also facings (the self-reflected edges): positions [127, 255] of 256

4  the beta-bulge: S -> S + 1 is one step taken by one reader; the facing becomes TP (or PT), not P
  n= 2: P fixes nothing, position sum {3}; TP fixes positions [0, 2] (0^n and m), sum {0}; PT fixes [1, 3] (P(m) and 1^n), sum {2}
  n= 3: P fixes nothing, position sum {7}; TP fixes positions [0, 4] (0^n and m), sum {0}; PT fixes [3, 7] (P(m) and 1^n), sum {6}
  n= 4: P fixes nothing, position sum {15}; TP fixes positions [0, 8] (0^n and m), sum {0}; PT fixes [7, 15] (P(m) and 1^n), sum {14}
  n= 8: P fixes nothing, position sum {255}; TP fixes positions [0, 128] (0^n and m), sum {0}; PT fixes [127, 255] (P(m) and 1^n), sum {254}
  n=14: P fixes nothing, position sum {16383}; TP fixes positions [0, 8192] (0^n and m), sum {0}; PT fixes [8191, 16383] (P(m) and 1^n), sum {16382}
```

### 196.1 Ring 2 is in the centre of ring 4 — the whole ring, minus its palindromes

**Theorem.** The centre block of R_{n+2} — its 2^n − 2^⌈n/2⌉ middle words — is R_n with its palindromes removed, in R_n's
own order, every word wrapped as 1·x·1. *Proof.* By the frame law the leading-1 representatives of width n + 2 are
1·y·1 with y < J(y), the largest of the rising list. So the listed half ends with them in rising order, then P(m′) and
m′ = 1·m·1 (§ 135). The created half opens with their images 1·J(y)·1 falling. Removing R_n's palindromes leaves exactly
[y < J(y) rising without m, J(m), m, J(y) falling]. ∎ Run n = 2..14 into 4..16 above: every block equal.

So ring 2 sits in the centre of ring 4 (R₄'s middle pair 1101, 1011 = 1·[10, 01]·1), and ring 3 in the centre of ring 5.
Wrapping again puts ring 2 in the centre of 6, 8, … and ring 3 in 7, 9, …: two towers, one shell (two bits) per level.
Read outward from the crease, R_n and R_{n+2} execute the same steps (the wider one padded by its 0-shell) for exactly ℓ(n)
steps, up to R_n's first palindrome, which the wider ring skips. In the run, 120 shared steps at n = 10 and 2,016 at
n = 14. (The script's printed guess "ℓ(n) + 1" was off by one; the count is ℓ(n).)

So each wider ring continues one **crease program** outward, at twice the value: the 1·x·1 shell doubles every increment.
That is the anti-linear progression Dean describes. The ring is linear in value only within each half; across widths it
is built from the crease out, the narrower ring inside, the new words added on the outside.

### 196.2 The instruction alphabet in closed form

**Derivation (from the frame law).**
- **The rising list.** It is the representatives in value order: 0·z·1 for every core z, 0·z·0 for cores z ≤ J(z),
  then 1·y·1 for y < J(y). The leading-0 words come core by core, 0·z·0 just before 0·z·1. Each step is +1 (0z0 → 0z1;
  0z1 → 0(z+1)0) or +2 (0z1 → 0(z+1)1 when 0(z+1)0 is absent), then one +4 step into the 1·y·1 block. Inside that block
  the steps are the y-list's, one shell in, doubled.
- **Every rising step adds one power of two** (run: all n = 6–16), so its mask is one run 0^a 1^k 0^b: the increment
  2^b with a k-bit carry. b never exceeds ⌈n/2⌉ − 1. In value the rising half moves by only ⌈n/2⌉ distinct amounts.
- **Collected depth by depth, the rising list's carries are three kinds:**
  - (R1) every run with a ≥ b ≥ 1, except at odd n the lone middle bit: the list's last step, which the ring hands to
    the crease;
  - (R2) the +1 runs (b = 0) of length 1 … ⌈n/2⌉;
  - (R3) one +4 step per depth, 0^d 1^(n−2d−2) 0^(d+2), ⌊(n−3)/2⌋ of them (at even n the deepest one is the list's
    last step, handed to the crease, and is not counted).
- **The created half runs J of these**, complemented where a step crosses a palindrome boundary (§ 195). That sends the
  b = 0 runs to a = 0 runs of length ≤ ⌊n/2⌋, and to b = 0 runs of length ≥ n/2.
- **Distinct counts.**
  - Rising ⌊(n+1)²/4⌋ − 2.
  - Mirror ⌊(n+2)²/4⌋ − 4.
  - Both 3⌊(n−3)/2⌋ (the centred runs a = b, the middle b = 0 run or runs, the +4 steps and their mirrors).
  - Then the wrap 1ⁿ, and the crease steps that are not already runs: at even n the crease-in and crease-out, which
    straddle the centre (0…0101 0…0); at odd n the seam 0…0101 0…0.
- **Total.** n²/2 + 4 at even n, (n² + 3)/2 at odd n, for n ≥ 6. The small rings sit below the regime: 9 at n = 4,
  12 at n = 5, and 6 at n = 3, which the odd formula happens to hit.

**Sealed, then built.** The prediction (exact set and the four counts) was hashed before R₁₃–R₁₆'s alphabets were built:
- 4 of 4 widths match on all four counts and on the exact set.
- R₁₅ and R₁₆ had never been built; R₁₃ and R₁₄ were built in § 195 for other checks, but their alphabets were not
  computed.
- The closed form was read from the structure on n = 6–12. The derivation above is an outline whose existence steps the
  run checks at n = 6–16; a written all-width proof is OPEN.

### 196.3 The zipper as a word

- **The crease row executes τ, the seam step.** That is one transposition: the two middle cells at even width, the two
  around the middle at odd width.
- **Row t is the facing pair (R[h−1−t], R[h+t]).** Its facing instruction Λ_t = x ⊕ P(x) is a palindromic mask: the
  lamps.
- **Between rows the two arms execute a mirrored pair of steps** (d, J(d) ⊕ φ), 6 of 6 rows in R₈. Only two edges of
  the ring are both a step and a facing: the seam (τ) and the wrap (C), positions 127 and 255 of 256.

So § 193's zipper in the ring's alphabet is Z = τ · Λ₂ · Λ₄ · …, with the arms advancing by mirrored carries. The protein
executes the even facings (bonded rows) and idles the odd ones; the ring faces every row.

### 196.4 The β-bulge

A slip to S ± 1 pairs positions summing to N or N − 2 instead of N − 1: one reader takes a step the other does not. In
the ring that turns the facing P into TP (sum N) or PT (sum N − 2). These are the dihedral reflections whose axes pass
through cells: TP fixes 0ⁿ and m, PT fixes P(m) and 1ⁿ, at every width 2–14. So the bulge is not a new opcode. The step it
takes is in the alphabet (every carry is), but one reader takes it alone. What the word partner never does is face a cell
with itself; TP and PT do, once at the crease (m or P(m)) and once at a rail (0ⁿ or 1ⁿ). That is § 190's fencepost seen
from the ring: the even crease has a cell that faces itself, and the ring has exactly two reflections that allow it. The
§ 193 census (30 stored bonds on S + 1, 11 on S − 1) is where TP and PT could be told apart; not tested here.

**Dean's circuit reading, in the ring's own terms.**
- **Rails.** Every word is a stack of shells (b_k, b_{n−1−k}). Each shell is an R₂ word, either on a rail (00, 11: the
  two probes read the same) or across the rails (01, 10: a difference, with a direction). The lamps say which, and J, C
  and P never change them (§ 135); the partner changes the readings, not the rail pattern.
- **Relative values.** The steps are relative too. Every rising step is one power of two, and R_{n+2} runs R_n's crease
  program at twice the value: the values move, the program does not.

| claim | status |
|---|---|
| § 195's lemma, ℓ(n), centre nesting, lamps | recovered (frame law; *Native Binary Rings* eq. 14; § 135); **correction, mine** |
| centre block of R_{n+2} = 1·(R_n minus palindromes)·1, in ring order | STANDS (proof) · RUNS n = 2–14; new as stated |
| crease program: R_n and R_{n+2} share exactly ℓ(n) steps outward from the crease | RUNS n = 4–14 |
| every rising step adds one power of two, b ≤ ⌈n/2⌉ − 1 | RUNS n = 6–16 |
| alphabet: exact set; rising ⌊(n+1)²/4⌋ − 2, mirror ⌊(n+2)²/4⌋ − 4, both 3⌊(n−3)/2⌋, total n²/2 + 4 / (n² + 3)/2 | RUNS: sealed (SHA-256 3e21796a…), n = 13–16 landed 4/4 exact; derivation outlined; all-width proof OPEN |
| zipper = τ · Λ₂ · Λ₄ · … with mirrored arm steps; seam and wrap the only step-facings | RUNS (R₈; positions 127, 255) |
| β-bulge = TP or PT: the step is in the alphabet, the self-facing cell is not in P | STANDS (one line) · RUNS n = 2–14 |
| TP vs PT on the 30 / 11 split of slips | OPEN |

**Methods.** *NEXUS_Methods_v2_Ring_ISA_and_Local_Compiler.ipynb* adds the § 196 operations (`lamps`, `alphabet`,
`alphabet_closed_form`, `centre_block`, `TP`, `PT`) and one check cell, and corrects v1's markdown, which carried the
overclaims corrected above. Its project copy `claude/nexus-methods-v2.md` replaces `claude/nexus-methods-v1.md`.

`ring_alphabet.py`

```python
"""§ 196. The ring's instruction alphabet in closed form, sealed for n = 13..16 before those rings are built; the nesting
of rings (R_n inside R_{n+2}); the crease program read outward; the zipper as a word; the beta-bulge.
Run: python3 -I ring_alphabet.py"""
import hashlib, re, sys

def J(x, n): return int(format(x, f'0{n}b')[::-1], 2)
def C(x, n): return x ^ ((1 << n) - 1)
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)
def ring(n):
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    return reps[:-1] + [P(m, n), m] + [P(x, n) for x in reversed(reps[:-1])]
def interval(a, k, n):          # 0^a 1^k 0^b as an n-bit mask (b = n - a - k)
    return ((1 << k) - 1) << (n - a - k)
def mask(s): return int(s, 2)

# ---------------------------------------------------------------- closed forms (derived from the frame law, see the audit)
def alphabet_pred(n):
    A = {interval(a, k, n) for a in range(1, n) for k in range(1, n - a + 1)}
    if n % 2: A.discard(interval((n - 1) // 2, 1, n))                        # odd n: no lone middle bit
    A |= {interval(0, k, n) for k in list(range(1, n // 2 + 1)) + [n - 2, n]}
    if n % 2:
        A.add(mask('0' * ((n - 3) // 2) + '101' + '0' * ((n - 3) // 2)))       # the seam
    else:
        A.add(mask('0' * (n // 2 - 2) + '101' + '0' * (n // 2 - 1)))           # crease-in
        A.add(mask('0' * (n // 2 - 1) + '101' + '0' * (n // 2 - 2)))           # crease-out
    return A
def counts_pred(n):
    rise = (n + 1) ** 2 // 4 - 2; mirr = (n + 2) ** 2 // 4 - 4; over = 3 * ((n - 3) // 2)
    total = n * n // 2 + 4 if n % 2 == 0 else (n * n + 3) // 2
    return rise, mirr, over, total

PRED = ("For n >= 6 the distinct steps D_k = R[k] xor R[k+1] of R_n are: every single run 0^a 1^k 0^b with a >= 1, except at odd "
        "n the lone middle bit; the runs with a = 0 of length k in 1..floor(n/2) and n-2 and n; and the two-run masks: odd n the seam "
        "0^((n-3)/2) 101 0^((n-3)/2), even n the crease-in 0^(n/2-2) 101 0^(n/2-1) and crease-out 0^(n/2-1) 101 0^(n/2-2). "
        "Distinct counts: rising (the carries of the rising list) floor((n+1)^2/4) - 2; mirror floor((n+2)^2/4) - 4; "
        "rising-and-mirror 3*floor((n-3)/2); total n^2/2 + 4 (even n), (n^2 + 3)/2 (odd n). Every rising step adds one power of "
        "two 2^b with b <= ceil(n/2) - 1. Predicted (rising, mirror, overlap, total): "
        + '; '.join(f'n={n}: {counts_pred(n)}' for n in range(13, 17)) + '.')
print('PREDICTION, sealed before R_13 .. R_16 are built\n ', PRED)
print('  SHA-256', hashlib.sha256(PRED.encode()).hexdigest()); sys.stdout.flush()

print('\n1  built and checked')
for n in range(6, 17):
    R = ring(n); N = len(R); h = N // 2
    D = [R[k] ^ R[(k + 1) % N] for k in range(N)]
    rise, mirr = set(D[:h - 2]), set(D[h + 1:N - 1])
    got = (len(rise), len(mirr), len(rise & mirr), len(set(D)))
    carries = all(R[k + 1] - R[k] > 0 and (R[k + 1] - R[k]) & (R[k + 1] - R[k] - 1) == 0 for k in range(h - 2))
    bmax = max((R[k + 1] - R[k]).bit_length() - 1 for k in range(h - 2))
    tag = 'sealed' if n >= 13 else 'derivation set'
    print(f'  n={n:2} ({tag:14}): built {got}  predicted {counts_pred(n)}  match {got == counts_pred(n)}; exact set {set(D) == alphabet_pred(n)}; '
          f'every rising step +2^b {carries}, largest b {bmax} (bound {-(-n // 2) - 1})')

print('\n2  rings inside rings: the centre block of R_{n+2} is R_n without its palindromes, each word wrapped 1..1')
for n in range(2, 15):
    R, R2 = ring(n), ring(n + 2); N2 = len(R2)
    core = [x for x in R if not pal(x, n)]
    w = len(core); lo = N2 // 2 - w // 2
    block = R2[lo:lo + w]
    ok = block == [(1 << (n + 1)) | (x << 1) | 1 for x in core]
    # the crease program: steps read outward from the crease on the outgoing arm, R_n against R_{n+2} (one 0-shell of padding)
    hn, hm = len(R) // 2, N2 // 2
    agree = 0
    while hn - 2 - agree >= 0 and ((R[hn - 2 - agree] ^ R[hn - 1 - agree]) << 1) == (R2[hm - 2 - agree] ^ R2[hm - 1 - agree]): agree += 1
    ell = (1 << (n - 3)) - (1 << ((n - 3) // 2)) if n >= 4 else 1
    print(f'  n={n:2} -> {n + 2:2}: centre block {w:5} words = 1.(R_{n} minus palindromes).1  {ok};  crease program shared for {agree} steps outward (l(n) + 1 = {ell + 1})')

print('\n3  the zipper as a word (R_8): crease row = seam step; row t pairs R[h-1-t] and R[h+t]; the arms advance by mirrored steps')
n = 8; R = ring(n); N = len(R); h = N // 2; f = lambda v: format(v, f'0{n}b')
print(f'  t=0: {f(R[h-1])} | {f(R[h])}  facing step {f(R[h-1] ^ R[h])} = seam step {f(R[h-1] ^ R[h])}, a transposition')
for t in range(1, 7):
    a, b = h - 1 - t, h + t; o = R[a] ^ R[a + 1]; r = R[b - 1] ^ R[b]
    phi = int(pal(R[a], n) != pal(R[a + 1], n))
    print(f'  t={t}: {f(R[a])} | {f(R[b])}  facing step {f(R[a] ^ R[b])} (palindrome {pal(R[a] ^ R[b], n)});  '
          f'arm steps {f(o)} | {f(r)}  mirror pair {r == J(o, n) ^ (phi * ((1 << n) - 1))}')
both = [k for k in range(N) if (R[k] ^ R[(k + 1) % N]) == (R[k] ^ P(R[k], n))]
print(f'  steps that are also facings (the self-reflected edges): positions {both} of {N}')

print('\n4  the beta-bulge: S -> S + 1 is one step taken by one reader; the facing becomes TP (or PT), not P')
for n in range(2, 15):
    R = ring(n); N = len(R); pos = {x: k for k, x in enumerate(R)}
    TP = lambda x: R[(pos[P(x, n)] + 1) % N]; PT = lambda x: P(R[(pos[x] + 1) % N], n)
    fixTP = [pos[x] for x in R if TP(x) == x]; fixPT = [pos[x] for x in R if PT(x) == x]
    sums = ({(pos[x] + pos[TP(x)]) % N for x in R}, {(pos[x] + pos[PT(x)]) % N for x in R}, {(pos[x] + pos[P(x, n)]) % N for x in R})
    if n <= 4 or n in (8, 14):
        print(f'  n={n:2}: P fixes nothing, position sum {sums[2]}; TP fixes positions {fixTP} (0^n and m), sum {sums[0]}; '
              f'PT fixes {fixPT} (P(m) and 1^n), sum {sums[1]}')
```
