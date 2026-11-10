# NEXUS methods v2 (project copy of the notebook) — the ring as instruction set, and the local compiler

*Dean A. Kulik, QuHarmonics Research Group (ORCID 0009-0003-3128-8828) · methods pulled out of the running audit §§ 182–196 · 30 October 2026*

v2 adds § 196 (rings inside rings, the instruction alphabet in closed form, the β-bulge) and corrects v1: the lemma, ℓ(n) and
the centre nesting were already in the record (frame law; *Native Binary Rings* eq. 14; § 135).

One library cell, then checks that re-run every result from it. Everything is an **operation on an operand**, written once,
in one base: a residue is one cell, a word is its bits, and the ring holds every word. No fitted coefficient, no energy, no
global ring phase. To run: put `ecoli_chains.json` and `ecoli_water.json` (or `NEXUS_Fold_Compiler_Notebook (2).zip`)
beside this notebook, or set `NEXUS_DATA` to their folder. Python 3 and NumPy only.

Status words, as in the audit: **STANDS** (proved, or an exact identity), **RUNS** (executed on the stated domain),
**DEAD END** (the calculation landed somewhere else), **OPEN** (a named missing link). *Recovered* marks results the
record or the literature already had.

The notebook *NEXUS_Methods_v2_Ring_ISA_and_Local_Compiler.ipynb* holds exactly these cells, executed. Paste the library block and then the check blocks into one session to run them.

## 1. The methods

**The ring layer is the instruction set. Its instructions are the differences.** A word `x = (b₀ … bₙ₋₁)` splits
into a **face** bit `f = b₀` (the value channel) and a **shape** word `δᵢ = bᵢ ⊕ bᵢ₊₁` (the shape channel). The split
is invertible (*From One Difference to the Shape Channel* § 3.2). Every operation below says which channel it touches.

| layer | operation (library name) | operand → result | channel | where | status |
|---|---|---|---|---|---|
| ring | `J` reversal | word → bits backwards | shape reversed | record | STANDS |
| ring | `C` complement | word → every bit flipped | **value only**: f flips, δ fixed | record; § 185 | STANDS |
| ring | `P` partner = J off palindromes, C on them | fixed-point-free involution | shape reversed for every word | record | STANDS |
| ring | `ring(n)` | rising representatives, seam swap, falling images | `R[N−1−a] = P(R[a])`, `PTP = T⁻¹` | record | STANDS |
| ring | `x ^ P(x)` facing step | the instruction that faces a word | always a nonzero palindrome | record (even n); here all n | STANDS |
| ring | `step_program(n)` | `D_k = R[k] ⊕ R[k+1]` | shape part an exact mirror; corrections only in the face part | **§ 195** | STANDS · RUNS n ≤ 12 |
| ring | `seam_step(n)` | the step across the crease | **one transposition at the word centre** | **§ 195** | STANDS |
| ring | wrap step `R[N−1] ⊕ R[0]` | `1ⁿ` | **C: value only** | **§ 195** | STANDS |
| ring | lemma, nesting `m(n) = 1·m(n−2)·1` | the crease of a wider ring | the narrower crease in a 1…1 shell | recovered: frame law (*NESTED*), § 135 | STANDS |
| ring | `lead_turn(n)`, `ell_formula(n)` | where a forward run stops doubling | `N/2 − ℓ(n)` = the record's C₀(n), `ℓ = 2ⁿ⁻³ − 2^⌊(n−3)/2⌋` | recovered: *Native Binary Rings* eq. 14 (even n) | STANDS |
| ring | `lamps` | shell (b_k, b_{n−1−k}) → 0 on a rail (00, 11), 1 across (01, 10) | fixed by J, C, P | recovered: § 135 check 8 | STANDS |
| ring | `centre_block(n)` | middle of R_{n+2} | **= 1·(R_n minus palindromes)·1, in ring order: rings inside rings** | **§ 196** | STANDS (proof) |
| ring | `alphabet(n)`, `alphabet_closed_form(n)` | the distinct steps | single runs (carries) + crease steps; counts in closed form | **§ 196** | RUNS 6–16 (sealed 13–16) |
| ring | `TP`, `PT` | one step on one side, then facing | the reflections through cells: the β-bulge | **§ 196** | STANDS |
| square | `pair_word`, `mirror_P`, `half_turn_C`, `quarter_rho` | cell (i, j) of the pair square | P = diagonal mirror, C = half-turn, ρ = quarter-turn swaps sum and difference lines | §§ 187, 189 | RUNS |
| chain | `closures` | donor N–H → nearest O ≤ 3.5 Å, \|i−j\| > 2, no Pro donor | directed bonds | § 188 detector | method |
| chain | `hairpins` / `helices` | runs on one sum S / one difference d | 143 hairpins (49 even S), 515 helices | §§ 186–188 | RUNS |
| chain | `WET`, `value_bit` | side chain → water-facing slot count / 0-1 | value channel | *Reading Proteins* § 5; § 194 | RUNS (r = −0.81) |
| compiler | `turn_return` | crease row: e.NH → s.O, r.NH → e.O | one program at every width | § 192 | RUNS (post hoc) |
| compiler | `zipper` | crease row + ladder rows bonded both ways on even t | the shape channel of a hairpin | § 193 | RUNS 887/1062 |
| compiler | `faces`, `dry_face` | t mod 2 → face; dry = lower slot count | the value channel against the shape bit | § 194 | RUNS 111/143 |
| reader | `mirror_scores` | value mirror b(S−i) = b(i) from the centre | crease address from values | § 195 | **DEAD END** |
| land | `seal`, `rank_in_window` | SHA-256 of canonical JSON; midrank in ±8 | — | — | method |

## Library

```python
# ===================================================================================================
# NEXUS methods v2 — library cell. Operations and operands only; every result in the notebook calls these.
# Ring layer (the ISA) · square layer · chain layer · local compiler · seal and land.
# stdlib + NumPy. No fitted coefficient, no energy, no network.
# ===================================================================================================
import collections, hashlib, json, os, random, zipfile
from pathlib import Path
import numpy as np

# ---------------------------------------------------------------- ring layer: n-bit words, b_0 = MSB
def J(x, n):            # reversal: the order of the bits read backwards
    return int(format(x, f'0{n}b')[::-1], 2)

def C(x, n):            # complement: every bit flipped
    return x ^ ((1 << n) - 1)

def is_pal(x, n):
    return J(x, n) == x

def P(x, n):            # native partner: J off the palindromes, C on them (fixed-point-free involution)
    return C(x, n) if is_pal(x, n) else J(x, n)

def ring(n):            # native ring R_n: representatives rising, seam swap, partner images falling
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    return reps[:-1] + [P(m, n), m] + [P(x, n) for x in reversed(reps[:-1])]

def positions(R):
    return {x: k for k, x in enumerate(R)}

def T(x, R, pos):       # native successor: one step along the ring
    return R[(pos[x] + 1) % len(R)]

def face(x, n):         # value channel: the face bit f = b_0
    return x >> (n - 1)

def shape(x, n):        # shape channel: delta_i = b_i xor b_{i+1}, an (n-1)-bit word, delta_0 first
    return (x ^ (x >> 1)) & ((1 << (n - 1)) - 1)

def unsplit(f, d, n):   # inverse of (face, shape): b_0 = f, b_{i+1} = b_i xor delta_i
    b = [f]
    for i in range(n - 1): b.append(b[-1] ^ ((d >> (n - 2 - i)) & 1))
    return int(''.join(map(str, b)), 2)

def step_program(n):    # the ring's instruction stream: D_k = R[k] xor R[k+1] (cyclic) and the palindrome flags
    R = ring(n); N = len(R)
    D = [R[k] ^ R[(k + 1) % N] for k in range(N)]
    flags = [int(is_pal(R[a], n) != is_pal(R[a + 1], n)) for a in range(N - 1)]
    return R, D, flags

def lead_turn(n):       # where a forward run on the listed half stops doubling: first cell with leading bit 1
    R = ring(n); t = [face(x, n) for x in R].index(1)
    return t, len(R) // 2 - t

def ell_formula(n):     # number of representatives with leading bit 1 (n >= 4)
    return (1 << (n - 3)) - (1 << ((n - 3) // 2))

def seam_step(n):       # the step across the seam, and the bit positions it flips
    R = ring(n); h = len(R) // 2; d = R[h - 1] ^ R[h]
    return d, [k for k in range(n) if (d >> (n - 1 - k)) & 1]

def pair_word(i, j, m): # W(i, j) = b(i) || J(b(j)) on R_2m
    return (i << m) | J(j, m)

def lamps(x, n):         # shell lamps g_k = b_k xor b_(n-1-k), outer to inner: 0 = on a rail (00, 11), 1 = across (01, 10)
    return [((x >> (n - 1 - k)) ^ (x >> k)) & 1 for k in range(n // 2)]

def interval(a, k, n):  # the run 0^a 1^k 0^b (b = n - a - k) as an n-bit mask
    return ((1 << k) - 1) << (n - a - k)

def alphabet(n):        # distinct steps of R_n, split: rising (carries), mirror, and all
    R, D, _ = step_program(n); h = len(R) // 2
    return set(D[:h - 2]), set(D[h + 1:len(R) - 1]), set(D)

def alphabet_closed_form(n):   # s 196, n >= 6: the exact step set and the counts (rising, mirror, both, total)
    A = {interval(a, k, n) for a in range(1, n) for k in range(1, n - a + 1)}
    if n % 2: A.discard(interval((n - 1) // 2, 1, n))
    A |= {interval(0, k, n) for k in list(range(1, n // 2 + 1)) + [n - 2, n]}
    if n % 2: A.add(int('0' * ((n - 3) // 2) + '101' + '0' * ((n - 3) // 2), 2))
    else: A |= {int('0' * (n // 2 - 2) + '101' + '0' * (n // 2 - 1), 2), int('0' * (n // 2 - 1) + '101' + '0' * (n // 2 - 2), 2)}
    counts = ((n + 1) ** 2 // 4 - 2, (n + 2) ** 2 // 4 - 4, 3 * ((n - 3) // 2), n * n // 2 + 4 if n % 2 == 0 else (n * n + 3) // 2)
    return A, counts

def centre_block(n):    # s 196: the middle 2^n - 2^ceil(n/2) words of R_{n+2}, and R_n without palindromes wrapped 1.x.1
    R, R2 = ring(n), ring(n + 2); core = [x for x in R if not is_pal(x, n)]
    lo = len(R2) // 2 - len(core) // 2
    return R2[lo:lo + len(core)], [(1 << (n + 1)) | (x << 1) | 1 for x in core]

def TP(x, R, pos, n):   # one step on one side after facing: the reflection through cells (fixes 0^n and m)
    return R[(pos[P(x, n)] + 1) % len(R)]

def PT(x, R, pos, n):   # the other reflection through cells (fixes P(m) and 1^n)
    return P(R[(pos[x] + 1) % len(R)], n)

# ---------------------------------------------------------------- square layer: cells (i, j) of an M x M square
def mirror_P(c, M):     return (c[1], c[0])                       # mirror in the diagonal i = j
def half_turn_C(c, M):  return (M - 1 - c[0], M - 1 - c[1])       # reading from the other end
def quarter_rho(c, M):  return (c[1], M - 1 - c[0])               # reverse one reader only

# ---------------------------------------------------------------- chain layer: residues [index, aa, N, CA, C, O, CB]
def load(name, dirs=None):
    """Find name (ecoli_chains.json / ecoli_water.json) beside the notebook, in NEXUS_DATA, or inside the fold-compiler zip."""
    dirs = [Path(d) for d in (dirs or [])] + [Path(os.environ.get('NEXUS_DATA', '.')), Path('.'), Path('/mnt/data')]
    for d in dirs:
        if (d / name).is_file(): return json.loads((d / name).read_text())
    for d in dirs:
        for z in sorted(d.glob('*.zip')) if d.is_dir() else []:
            with zipfile.ZipFile(z) as zf:
                hit = [x for x in zf.namelist() if x.endswith('/' + name) or x == name]
                if hit: return json.loads(zf.read(hit[0]))
    raise FileNotFoundError(f'{name}: place it (or NEXUS_Fold_Compiler_Notebook (2).zip) beside this notebook')

def closures(ent):
    """Directed backbone closures (donor N-H index i -> acceptor O index j): nearest O within 3.5 A, |i - j| > 2, no Pro donor."""
    R = ent['residues']; L = len(R); seq = [r[1] for r in R]
    N = np.array([r[2] for r in R], float); O = np.array([r[5] for r in R], float)
    dd = np.linalg.norm(N[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    out = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: out.add((i, j))
    return out

def hairpins(directed, L):
    """Counter-moving runs on one sum S = i + j (donors <= 2 apart, >= 3 closures, innermost pair <= 8 apart).
    Returns (e, s, k, S): e, s = innermost pair, k = arm length to the outermost pair (clipped to the chain)."""
    und = {(min(c), max(c)) for c in directed}
    byS = collections.defaultdict(list)
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

def helices(directed):
    """Co-moving runs j = i - k (k = 3, 4) of >= 4 consecutive donors: (first donor, last donor, k)."""
    out = []
    for k in (3, 4):
        don = sorted(i for i, j in directed if j == i - k)
        run = [don[0]] if don else []
        for i in don[1:] + [None]:
            if i is not None and i == run[-1] + 1: run.append(i); continue
            if len(run) >= 4: out.append((run[0], run[-1], k))
            if i is not None: run = [i]
    return out

# Reading Proteins s5 as written: water-facing slots = unshared pairs + H on N or O, side chain only (r = -0.81 to hydropathy)
WET = {'G': 0, 'A': 0, 'V': 0, 'L': 0, 'I': 0, 'F': 0, 'P': 0, 'C': 2, 'M': 2, 'W': 2, 'S': 3, 'T': 3, 'Y': 3,
       'H': 3, 'K': 3, 'N': 5, 'Q': 5, 'D': 5, 'E': 5, 'R': 7}
def value_bit(aa):      # 0 = no water-facing slot (G A V L I F P), 1 otherwise
    return int(WET[aa] > 0)

def sc_point(r):        # side-chain point: CB, or a virtual CB from N, CA, C
    Nn, CA, Cc = (np.array(r[k], float) for k in (2, 3, 4))
    if len(r) > 6 and isinstance(r[6], list): return np.array(r[6], float)
    b = CA - Nn; c = Cc - CA; a = np.cross(b, c)
    return -0.58273431 * a + 0.56802827 * b - 0.54067466 * c + CA

# ---------------------------------------------------------------- local compiler
def turn_return(e, s):  # the returning NH that closes on O(e): s at width 3, s - 1 wider (s 192)
    return s if s - e == 3 else s - 1

def zipper(e, s, k, mode='v2'):
    """Compiler v2 (s 193): crease row e.NH -> s.O and r.NH -> e.O; ladder rows t = 1..k bonded both ways on even t.
    Nulls: 'N1' rails swapped, 'N2' phase swapped (odd t bonded), 'N3' no idle rows."""
    out = {(e, s), (turn_return(e, s), e)}
    for t in range(1, k + 1):
        bonded = (t % 2 == 0) if mode in ('v2', 'N1') else (t % 2 == 1) if mode == 'N2' else True
        if bonded: out |= {(e - t, s + t), (s + t, e - t)}
    return {(a, d) for d, a in out} if mode == 'N1' else out

def faces(e, s, k):     # face A = even rows (t mod 2 = 0) of both arms, face B = odd rows
    return ([x for t in range(0, k + 1, 2) for x in (e - t, s + t)],
            [x for t in range(1, k + 1, 2) for x in (e - t, s + t)])

def dry_face(seq, e, s, k):
    fA, fB = faces(e, s, k)
    if not fB: return None
    wA = np.mean([WET[seq[x]] for x in fA]); wB = np.mean([WET[seq[x]] for x in fB])
    return None if wA == wB else ('A' if wA < wB else 'B')

def mirror_scores(bits):
    """For every centre S: consecutive outward pairs with b(S - i) = b(i), from the centre (even S skips its own cell)."""
    L = len(bits); out = []
    for S in range(2 * L - 1):
        a, b = ((S - 1) // 2, (S + 1) // 2) if S % 2 else (S // 2 - 1, S // 2 + 1)
        n = 0
        while a >= 0 and b < L and bits[a] == bits[b]: n += 1; a -= 1; b += 1
        out.append(n)
    return out

# ---------------------------------------------------------------- seal and land
def seal(obj):
    return hashlib.sha256(json.dumps(obj, separators=(',', ':')).encode()).hexdigest()

def rank_in_window(S, sc, half=8):   # midrank of sc[S] among S-half .. S+half; advantage (n - rank)/(n - 1)
    lo, hi = max(0, S - half), min(len(sc) - 1, S + half); w = sc[lo:hi + 1]; v = sc[S]
    r = 1 + sum(x > v for x in w) + 0.5 * (sum(x == v for x in w) - 1)
    return r, (len(w) - r) / (len(w) - 1)
```

## 2. The ring layer: identities and four short proofs

The cell below asserts every identity on every word of the stated widths. The proofs say why they hold at all widths.

**Lemma** (the (1, 1) clause of the record's frame law, *NESTED*). For n ≥ 4 the representatives (`x < P(x)`) with
leading bit 1 are exactly the words `1·y·1` with `y ∈ B_{n−2}` and `y < J(y)`.
*Proof.* A palindrome with leading bit 1 has `P(x) = C(x)` with leading bit 0, so it is not a representative. Otherwise
`P(x) = J(x)` and its leading bit is the last bit of x; `x < J(x)` forces that bit to be 1, so `x = 1·y·1`,
`J(x) = 1·J(y)·1`, and `x < J(x) ⇔ y < J(y)`. Every such word qualifies. ∎

**Corollary 1 (encapsulation; the record's centre nesting, § 135).** `m(n) = 1·m(n−2)·1` and `P(m(n)) = 1·P(m(n−2))·1` for n ≥ 4, where m is the largest
representative. Leading-1 representatives exist from n = 4 on and outrank every leading-0 word, so `m(n) = 1·y*·1` with
y* the largest `y < J(y)` at width n−2. By the same lemma (and directly at widths 2 and 3), y* = m(n−2). m is never a
palindrome, so P acts on it as J and the shell passes through. The record's observed centre nesting `C_{n+2} = 1C_n1`
(*From One Difference* § 3.3, reading its C_n as the seam pair) therefore holds at every width: the crease of a wider
ring is the narrower crease, encapsulated. ∎

**Corollary 2 (where the forward run stops; the record's C₀(n), *Native Binary Rings* eq. 14).** The listed half is the representatives (without m) followed by P(m).
For n ≥ 4 both m and P(m) lead with 1, so the leading-1 cells of the listed half are exactly the leading-1
representatives, and being the largest they close the rising list. The leading bit turns at `N/2 − ℓ(n)` with
`ℓ(n) = #{y ∈ B_{n−2} : y < J(y)} = (2ⁿ⁻² − 2^⌈(n−2)/2⌉)/2 = 2ⁿ⁻³ − 2^⌊(n−3)/2⌋`. The record proves the even case
(App. A.3), and § 189 should have cited it. Widths 2 and 3 have ℓ = 1 from the seam swap alone. ∎

**Corollary 3 (the crease instruction is one transposition).** The seam step `P(m) ⊕ m` nests as `0·(seam step at
n−2)·0` by Corollary 1. At n = 2 it is `11` on m = `01`; at n = 3 it is `101` on m = `011`. In both the two flipped bits
of m differ, so the step swaps them. At every width the crease is one transposition at the centre of the word: between the
two middle cells when n is even, around the middle cell when n is odd. ∎

**The step program.** From the facing law, `D(N−2−a) = P(R[a+1]) ⊕ P(R[a])`. J is linear over XOR, `C(x) = x ⊕ 1ⁿ`,
and palindromes satisfy `J(x) = x`, so `D(N−2−a) = J(D(a)) ⊕ φ(a)·1ⁿ`, with `φ(a) = 1` exactly when one of `R[a]`,
`R[a+1]` is a palindrome. The shape map sends `1ⁿ` to 0 and J to reversal. So **the ring's program, read in the shape
channel, is its own exact mirror, and every correction rides in the face channel.** The wrap step is `P(0) ⊕ 0 = 1ⁿ`:
the one instruction that changes the value and not the shape. ∎

```python
print('RING LAYER: the instruction set, exact identities')
for n in range(2, 13):
    R = ring(n); N = len(R); pos = positions(R); W = range(N)
    assert sorted(R) == list(W)
    assert all(R[N - 1 - a] == P(R[a], n) for a in W)                                   # facing law
    assert all(P(T(P(x, n), R, pos), n) == R[(pos[x] - 1) % N] for x in R)             # P T P = T^-1
    assert all(unsplit(face(x, n), shape(x, n), n) == x for x in W)                     # (f, delta) bijective
    assert all(shape(C(x, n), n) == shape(x, n) and face(C(x, n), n) != face(x, n) for x in W)   # C: value only
    assert all(shape(P(x, n), n) == J(shape(x, n), n - 1) for x in W)                   # P: shape reversed
    assert all(x ^ P(x, n) and is_pal(x ^ P(x, n), n) for x in W)                       # facing step: nonzero palindrome
print('  n = 2..12  facing law; PTP = T^-1; (f, delta) bijective; C acts on the value only; P reverses the shape;'
      ' every facing step x ^ P(x) is a nonzero palindrome                      ok')
for n in range(4, 15):
    lead1 = {x for x in range(1 << n) if x < P(x, n) and face(x, n)}
    assert lead1 == {(1 << (n - 1)) | (y << 1) | 1 for y in range(1 << (n - 2)) if y < J(y, n - 2)}
    R = ring(n); h = len(R) // 2; Rm = ring(n - 2); hm = len(Rm) // 2
    assert R[h] == (1 << (n - 1)) | (Rm[hm] << 1) | 1 and R[h - 1] == (1 << (n - 1)) | (Rm[hm - 1] << 1) | 1
    assert lead_turn(n)[1] == ell_formula(n) == len(lead1)
print('  n = 4..14  lemma: leading-1 representatives = 1.y.1 with y < J(y); seam pair nests as 1.seam(n-2).1;'
      ' doubling stop l(n) = 2^(n-3) - 2^floor((n-3)/2)                       ok')
for n in range(2, 15):
    d, fl = seam_step(n); m = ring(n)[1 << (n - 1)]
    assert len(fl) == 2 and fl[0] + fl[1] == n - 1 and ((m >> (n - 1 - fl[0])) & 1) != ((m >> (n - 1 - fl[1])) & 1)
    if n <= 5: print(f'  n = {n}: seam step {format(d, f"0{n}b")} = one transposition at the centre, positions {fl}')
print('  n = 2..14  the seam step is one transposition centred in the word (between the middle cells for even n,'
      ' around the middle cell for odd n)                                     ok')
for n in range(2, 13):
    R, D, fl = step_program(n); N = len(R); one = (1 << n) - 1
    assert all(D[N - 2 - a] == J(D[a], n) ^ (fl[a] * one) for a in range(N - 1))
    assert all(shape(D[N - 2 - a], n) == J(shape(D[a], n), n - 1) for a in range(N - 1))
    assert all(face(D[N - 2 - a], n) == (D[a] & 1) ^ fl[a] for a in range(N - 1))
    assert D[N - 1] == one
    if n in (3, 4, 8, 12): print(f'  n = {n:2}: {N} steps, {len(set(D))} distinct instructions, {sum(fl)} palindrome flags, wrap step = 1^n')
print('  n = 2..12  step program: D(N-2-a) = J(D(a)) xor flag(a)*1^n; shape part an exact mirror; every flag in the face part;'
      ' wrap step = C                                                             ok')
M = 12; cells = [(i, j) for i in range(M) for j in range(M)]
same = lambda f, g: all(f(c, M) == g(c, M) for c in cells)
r2 = lambda c, M: quarter_rho(quarter_rho(c, M), M); r3 = lambda c, M: quarter_rho(r2(c, M), M)
assert same(r2, half_turn_C) and same(lambda c, M: r2(r2(c, M), M), lambda c, M: c)
assert same(lambda c, M: quarter_rho(mirror_P(r3(c, M), M), M), lambda c, M: mirror_P(half_turn_C(c, M), M))
assert all(len({quarter_rho(c, M)[1] - quarter_rho(c, M)[0] for c in cells if sum(c) == S}) == 1 for S in range(2 * M - 1))
for m in range(2, 7):
    w = 2 * m; Mm = 1 << m; cell = {pair_word(i, j, m): (i, j) for i in range(Mm) for j in range(Mm)}
    assert all(cell[P(pair_word(i, j, m), w)] == (j, i) for i in range(Mm) for j in range(Mm) if i != j)
    assert all(cell[C(pair_word(i, j, m), w)] == half_turn_C((i, j), Mm) for i in range(Mm) for j in range(Mm))
print('  square: P = mirror in the diagonal and C = half-turn on pair words (m = 2..6); quarter-turn rho: rho^2 = C, rho^4 = I,'
      ' rho P rho^-1 = PC, sum lines -> difference lines                       ok')
```

## 2b. Rings inside rings, the alphabet, and the β-bulge (§ 196)

**Rings inside rings.** The middle 2ⁿ − 2^⌈n/2⌉ words of R_{n+2} are R_n with its palindromes removed, in R_n's own order,
each wrapped as 1·x·1. *Proof.* By the frame law, the leading-1 representatives of width n + 2 are 1·y·1 with y < J(y), the
largest of the rising list. The listed half ends with them, then the seam pair 1·P(m)·1, 1·m·1; the created half opens
with their images 1·J(y)·1. Drop R_n's palindromes and that is R_n. ∎ So ring 2 is the centre of ring 4 (1101, 1011 =
1·[10, 01]·1), and ring 3 the centre of ring 5: two towers, one shell per level. Read outward from the crease, R_n and
R_{n+2} run the same steps (the wider one at twice the value) for exactly ℓ(n) steps, up to R_n's first palindrome. Every
ring continues one crease program outward. Growth across widths runs from the crease out, not along a line.

**The instruction alphabet.** Every rising step adds one power of two, 2^b with b ≤ ⌈n/2⌉ − 1, so its mask is one run of
ones (a carry). For n ≥ 6 the distinct steps are:
- every run 0^a 1^k 0^b with a ≥ 1, except at odd n the lone middle bit;
- the runs with a = 0 of length 1 … ⌊n/2⌋, n − 2 and n;
- the crease steps that are not runs.

Counts: rising ⌊(n+1)²/4⌋ − 2, mirror ⌊(n+2)²/4⌋ − 4, both 3⌊(n−3)/2⌋. The total is n²/2 + 4 at even n and (n² + 3)/2 at odd
n. Sealed in § 196 before R₁₃–R₁₆ were built; 4 of 4 exact.

**The zipper as a word.** Z = τ · Λ₂ · Λ₄ · …: the crease row executes the seam transposition τ, row t's facing step is
the palindromic lamp mask Λ_t = x ⊕ P(x), and between rows the arms take a mirrored pair of carries. Only the seam and the
wrap are both a step and a facing.

**The β-bulge.** A slip to S ± 1 is one reader stepping alone. It turns the facing P (sum N − 1, no fixed cell) into TP
(sum N, fixes 0ⁿ and m) or PT (sum N − 2, fixes P(m) and 1ⁿ): the two reflections through cells. The step is in the
alphabet; a cell facing itself is not in P. That is § 190's fencepost in the ring.

```python
print('RING LAYER II: rings inside rings, the alphabet, the bulge (s 196)')
for n in range(2, 15):
    blk, wrapped = centre_block(n); assert blk == wrapped
    if n >= 4:
        R, R2 = ring(n), ring(n + 2); h, h2 = len(R) // 2, len(R2) // 2; t = 0
        while h - 2 - t >= 0 and ((R[h - 2 - t] ^ R[h - 1 - t]) << 1) == (R2[h2 - 2 - t] ^ R2[h2 - 1 - t]): t += 1
        assert t == ell_formula(n) if n >= 4 else True
print('  n = 2..14  the centre block of R_(n+2) is R_n without its palindromes, each word 1.x.1, in ring order;'
      ' read outward from the crease the two rings share exactly l(n) steps                                ok')
for n in range(6, 17):
    rise, mirr, allD = alphabet(n); A, (cr, cm, cb, ct) = alphabet_closed_form(n)
    assert allD == A and (len(rise), len(mirr), len(rise & mirr), len(allD)) == (cr, cm, cb, ct)
    R, D, _ = step_program(n); h = len(R) // 2
    assert all((R[k + 1] - R[k]) > 0 and (R[k + 1] - R[k]) & (R[k + 1] - R[k] - 1) == 0 for k in range(h - 2))
    if n in (6, 12, 16): print(f'  n = {n:2}: steps (rising, mirror, both, total) = {(cr, cm, cb, ct)}; every rising step one power of two')
print('  n = 6..16  the alphabet equals its closed form (sealed for 13..16 in s 196) and every rising step is +2^b      ok')
for n in range(2, 15):
    R = ring(n); N = len(R); pos = positions(R)
    assert [pos[x] for x in R if TP(x, R, pos, n) == x] == [0, N // 2] and [pos[x] for x in R if PT(x, R, pos, n) == x] == [N // 2 - 1, N - 1]
    assert all(lamps(x, n) == lamps(P(x, n), n) == lamps(C(x, n), n) == lamps(J(x, n), n) for x in range(N))
print('  n = 2..14  TP fixes 0^n and m, PT fixes P(m) and 1^n (the bulge reflections); the lamps are fixed by J, C, P     ok')
```

## 3. The chain layer and the local compiler

Same detector as § 188 (nearest backbone O to each N–H). The cells re-run each landing from the library alone. The
seals printed here reproduce the audit's: § 193 emitted list `17584c67…`, § 195 scores `bd44ddb3…`.

* **§ 189 widths.** The forward-run stop gives `s − e = 2ℓ + 1 ∈ {3, 5}` on the protein lanes; width 3 is the mode.
* **§ 192 turn program.** At every width, e's NH goes to O(s) and a returning NH comes back onto O(e). S parity is the
  loop-length readout, not a second program.
* **§ 193 zipper.** The crease row plus ladder rows bonded both ways on even t. The nulls turn one rule each: N1 rails
  swapped, N2 phase swapped, N3 no idle rows. Swapping rails changes only the crease, because a transposition is its
  own inverse.
* **§ 194 value channel.** The face bit is t mod 2 from the crease; the dry face is the lower mean slot count. Landed
  on burial (Cα within 10 Å) and on crystal water (within 4.5 Å).

```python
chains = load('ecoli_chains.json'); water = {(w['acc'], w['set']): w for w in load('ecoli_water.json')}
DIR, HP, HX = {}, [], 0
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    DIR[ci] = closures(ent); HP += [(ci,) + h for h in hairpins(DIR[ci], L)]; HX += len(helices(DIR[ci]))
print(f'CHAIN LAYER  chains {len(chains)}; hairpins {len(HP)} (S even {sum(h[4] % 2 == 0 for h in HP)}); helices {HX}')
assert len(HP) == 143 and sum(h[4] % 2 == 0 for h in HP) == 49 and HX == 515
W = collections.Counter(s - e for ci, e, s, k, S in HP)
print('  s 189 crease widths s - e:', dict(sorted(W.items())), f' -> width 3 the mode {W[3]}, widths 3 and 5 hold {W[3] + W[5]} of 143')
```

```python
print('LOCAL COMPILER')
tw = collections.defaultdict(collections.Counter)
for ci, e, s, k, S in HP:
    acc = {i: j for i, j in DIR[ci]}; t = tw[s - e]; t['n'] += 1
    t['e->s'] += (e, s) in DIR[ci]; t['back->e'] += any(acc.get(x) == e for x in range(e + 3, s + 1))
print('  s 192 turn program, per width: e.NH -> s.O | some returning NH -> O(e)')
for w in sorted(tw):
    t = tw[w]; print(f'    width {w} (S {"odd" if w % 2 else "even"}): n={t["n"]:3}  {t["e->s"]/t["n"]:.2f} | {t["back->e"]/t["n"]:.2f}')
emitted = [sorted(zipper(e, s, k)) for ci, e, s, k, S in HP]
print('  s 193 emitted-list SHA-256', seal({'hairpins': HP, 'emitted': emitted}))
for mode in ('v2', 'N1', 'N2', 'N3'):
    tp = em = st = ex = 0
    for ci, e, s, k, S in HP:
        D = {(i, j) for i, j in DIR[ci] if e - k <= i <= s + k and e - k <= j <= s + k}; E = zipper(e, s, k, mode)
        tp += len(E & D); em += len(E); st += len(D); ex += E == D
    print(f'    {mode}: emitted {tp}/{em} land ({tp/em:.3f}); stored recovered {tp/st:.3f}; exact hairpins {ex}')
agree = n_call = agree_w = n_w = 0
for ci, e, s, k, S in HP:
    R = chains[ci]['residues']; seq = [r[1] for r in R]; call = dry_face(seq, e, s, k)
    if call is None: continue
    CA = np.array([r[3] for r in R]); SP = np.array([sc_point(r) for r in R]); fA, fB = faces(e, s, k)
    bur = lambda xs: np.mean([(np.linalg.norm(CA - SP[x], axis=1) <= 10).sum() for x in xs])
    buried = 'A' if bur(fA) > bur(fB) else 'B' if bur(fB) > bur(fA) else None
    n_call += 1; agree += buried == call
    Wt = water.get((chains[ci]['acc'], chains[ci]['set'])); WX = np.array([w[:3] for w in Wt['waters']]) if Wt and Wt['waters'] else np.zeros((0, 3))
    wat = lambda xs: np.mean([(np.linalg.norm(WX - SP[x], axis=1) <= 4.5).sum() if len(WX) else 0 for x in xs])
    wa, wb = wat(fA), wat(fB)
    if wa != wb: n_w += 1; agree_w += ('A' if wa < wb else 'B') == call
print(f'  s 194 value channel: dry face from the sequence = buried face {agree}/{n_call} ({agree/n_call:.3f}); fewer crystal waters {agree_w}/{n_w} ({agree_w/n_w:.3f})')
```

## 4. Where it does not work: asking the value channel for the address (§ 195)

The prompt asked whether the crease sits where the value bits mirror, b(S−i) = b(i), scored outward from the centre.
Run independently here and by GPT (its § 195, same numbers: 10 first, 27 in the top 3, mean advantage 0.5299). It does
not beat composition-shuffled sequences or shifted centres: **DEAD END**.

The ring says why, in its own terms: the program's mirror is exact in the **shape** channel and its corrections ride the
**face** channel. A hairpin keeps its mirror in the bond rows (§ 193, 0.835) and its face *averages* (§ 194, 0.776). Its
residue-by-residue values agree across the mirror only 0.58 of the time, against 0.50 for the same residues paired at
random, so a run of consecutive agreements dies within a row or two. The reader asked the value channel for something the shape channel holds.

```python
BITS = {ci: [value_bit(r[1]) for r in chains[ci]['residues']] for ci in range(len(chains))}
SC = {ci: mirror_scores(BITS[ci]) for ci in BITS}
print('MIRROR READER (s 195)  scores SHA-256', seal([SC[ci] for ci in range(len(chains))]))
obs = [rank_in_window(S, SC[ci]) for ci, e, s, k, S in HP]; adv = float(np.mean([a for r, a in obs]))
print(f'  true S first {sum(r == 1 for r, a in obs)}; top 3 {sum(r <= 3 for r, a in obs)}; mean advantage {adv:.4f};'
      f' S even {np.mean([a for (r, a), h in zip(obs, HP) if h[4] % 2 == 0]):.4f}, S odd {np.mean([a for (r, a), h in zip(obs, HP) if h[4] % 2]):.4f}')
rng = random.Random(195); used = sorted({h[0] for h in HP}); sh = []
for rep in range(100):
    SCs = {}
    for ci in used: b = BITS[ci][:]; rng.shuffle(b); SCs[ci] = mirror_scores(b)
    sh.append(np.mean([rank_in_window(S, SCs[ci])[1] for ci, e, s, k, S in HP]))
sh = np.array(sh)
print(f'  composition-shuffle null {sh.mean():.4f} (sd {sh.std():.4f}); P(null >= observed) {(1 + (sh >= adv).sum()) / 101:.2f}')
shift = []
for rep in range(100):
    shift.append(np.mean([rank_in_window(rng.choice([x for x in range(max(0, S - 8), min(len(SC[ci]), S + 9)) if x != S]), SC[ci])[1]
                          for ci, e, s, k, S in HP]))
shift = np.array(shift)
print(f'  shifted-centre null {shift.mean():.4f} (sd {shift.std():.4f}); P(null >= observed) {(1 + (shift >= adv).sum()) / 101:.2f}  -> DEAD END')
rows = [(BITS[ci][e - t] == BITS[ci][s + t]) for ci, e, s, k, S in HP for t in range(k + 1)]
rand = []
for ci, e, s, k, S in HP:
    pool = [BITS[ci][x] for t in range(k + 1) for x in (e - t, s + t)]
    for _ in range(50): rng.shuffle(pool); rand += [pool[2 * t] == pool[2 * t + 1] for t in range(k + 1)]
print(f'  why: value agreement on the ladder rows b(e-t) = b(s+t) is {np.mean(rows):.3f} per row; the same residues paired at random'
      f' {np.mean(rand):.3f}. A run of consecutive agreements dies within a row or two.')
```

## 5. Ledger

| claim | status |
|---|---|
| facing law, PTP = T⁻¹, (f, δ) split, C value-only, P shape-reversing, facing step a nonzero palindrome | STANDS · RUNS n = 2–12 (recovered: record) |
| lemma: leading-1 representatives = 1·y·1 with y < J(y) | recovered (frame law, *NESTED*) · RUNS n = 4–14 |
| encapsulation: the crease of R_{n+2} is the crease of R_n in a 1…1 shell | recovered (§ 135); proof in § 2 |
| doubling stop ℓ(n) = 2ⁿ⁻³ − 2^⌊(n−3)/2⌋, the turn at C₀(n) | recovered (*Native Binary Rings* eq. 14, even n); odd n one line |
| rings inside rings: centre of R_{n+2} = 1·(R_n minus palindromes)·1; crease program shared ℓ(n) steps | STANDS (proof) · RUNS n = 2–14 (§ 196) |
| alphabet in closed form (exact set and counts) | RUNS n = 6–16, sealed 13–16 (§ 196); all-width proof OPEN |
| β-bulge = TP or PT, the reflections through cells | STANDS · RUNS n = 2–14 (§ 196) |
| seam step = one centred transposition, every width | STANDS (proof) · RUNS n = 2–14 |
| step program: shape part an exact mirror, corrections only in the face part; wrap = C | STANDS (one line) · RUNS n = 2–12 |
| square: P mirror, C half-turn, ρ quarter-turn swapping the two line families | RUNS |
| hairpins 143 (49 even S), helices 515; widths {3, 5} hold 89/143 | RUNS (§§ 188–189) |
| turn program e → s and a returning NH → e at every width | RUNS (post hoc, § 192) |
| zipper: 887/1062 emitted bonds land, 21/143 exact; ladder = Pauling–Corey (recovered) | RUNS (§ 193) |
| dry face from the sequence = buried face 111/143, fewer waters 92/129; alternating β faces (recovered) | RUNS (§ 194) |
| value mirror as the crease address | DEAD END (§ 195) |
| reading: the ring's two self-facing steps are the two operations the hairpins isolated (wrap = C on the value; seam = one transposition) | reading, not evidence |
| where the crease sits along a chain; the distant partner | OPEN |
