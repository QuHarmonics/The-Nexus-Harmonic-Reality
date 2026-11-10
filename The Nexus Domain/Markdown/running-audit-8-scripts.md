# NEXUS running audit 8 — scripts

Scripts for § 199 of `running-audit-8.md`, printed in full.

## `shape_history.py` — generator, seal, reader (sha `5ef31d96…`)

```python
"""NEXUS s199. The shape is the history.

GENERATOR (no chain data). The native laws run as a linear construction H0 -> H1 -> ... . A write the laws force is
executed. A write they leave open is marked AMBIGUOUS, counted, and carried as a variable; no convention fills it.
A write nothing provides is marked OPEN. Closure is derived from the executed history and the route home is run.
Past closure, every uniform insertion of a new distinction is tried against the closed history.
SEAL. What the generated shape says about chains, with the readout each claim returns through, hashed together with
the generator's whole output.
READER. The chains, opened only after the seal. Nothing read flows back into the generator.

Run: python3 -I shape_history.py [ecoli_chains.json]      (no file: generator and seal only)
"""
import collections, hashlib, io, itertools, json, math, sys

# ---------------------------------------------------------------- native primitives (record: NBR eq. 1; s190-s198)
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2) if n else 0      # reversal
def C(x, n): return x ^ ((1 << n) - 1)                                   # complement
def pal(x, n): return J(x, n) == x
def P(x, n): return C(x, n) if pal(x, n) else J(x, n)                    # partner: J off palindromes, C on them
def bits(x, n): return format(x, f'0{n}b') if n else 'e'               # e: the empty word
def wt(x): return bin(x).count('1')

LAWS = ['L0 cannot hold still: every step, the closing one included, changes the word.',
        'L1 full set: every word of width n is written exactly once.',
        'L2 no rewrite: a written slot never changes.',
        'L3 facing: slot N-1-a holds P(word in slot a).',
        'L4 successor: the history advances one slot at a time; slot N-1 continues to slot 0.',
        "L5 boundary: slot 0 holds 0^n, the word with no distinction marked (the record's rings start there)."]
Q = 'Q = an order on the untouched pairs and a choice of member (the record supplies a ranking convention; not used here)'

GEN = io.StringIO()                         # the generator's whole output, hashed into the seal
def out(*a):
    s = ' '.join(str(x) for x in a); print(s); GEN.write(s + '\n')

def show(c, n):
    k, v = c
    return bits(v, n) if k == 'w' else f'x{v}' if k == 'x' else f'P(x{v})'

def partner(c, n):
    k, v = c
    return ('w', P(v, n)) if k == 'w' else ('Px', v)

def construct(n, loud=True):
    """Execute the laws slot by slot at width n."""
    say = out if loud else (lambda *a: None)
    N = 1 << n
    say(f'\n=== width n = {n}: {N} word{"s" if N > 1 else ""} ===')
    if N == 1:
        say(f'  H1   slot 0   {bits(0, n)}  BOUNDARY  L5. By L4 the successor of slot 0 is slot 0: the step is the identity.')
        say('  L0 fails: one word has nowhere to go. No legal history at n = 0.  OPEN: nothing to move to.')
        return None
    h = N // 2
    slots, owed, untouched, count, forced, amb = [None] * N, {}, h, 1, 0, 0
    for t in range(N):
        mirror = N - 1 - t
        if t == 0:
            c, kind, why = ('w', 0), 'BOUNDARY ', 'L5'
        elif t in owed:
            c, kind, why = owed.pop(t), 'FORCED   ', f'owed by slot {mirror} (L3)'; forced += 1
        else:
            c, kind = ('x', t), 'AMBIGUOUS'
            why = f'{2 * untouched} legal ({untouched} pairs x 2), Q missing'
            count *= 2 * untouched; amb += 1
        slots[t] = c
        if t < h:
            owed[mirror] = partner(c, n); untouched -= 1
            why += f'; owes s{mirror} <- {show(owed[mirror], n)}'
        state = ''
        if n <= 3:
            state = ' | state [' + ' '.join(show(s, n) if s else ('(' + show(owed[a], n) + ')' if a in owed else '.')
                                             for a, s in enumerate(slots)) + ']'
        ret = f'H{t}: unwrite s{t}' + (f', xor m{t}' if t else '')
        say(f'  H{t + 1:<4} s{t:<3} {show(c, n):<7} {kind} {why} | open {untouched} pairs, owed {len(owed)} | ret {ret}{state}')
    last = slots[N - 1]
    wrap = last[1] ^ slots[0][1]
    assert last[0] == 'w' and wrap == (1 << n) - 1
    say(f'  CLOSE  slot {N - 1} -> slot 0 by L4: step = {show(last, n)} xor {bits(0, n)} = {bits(wrap, n)}, all bits: C. '
        f'Derived from L3 at slot 0 and L5 (P(0^n) = 1^n); L0 holds, the step is not the identity.')
    order = ', '.join(map(str, range(N - 1, -1, -1))) if N <= 4 else f'{N - 1}, {N - 2}, ..., 0'
    say(f'  ROUTE HOME from H{N}: unwrite slots {order} in that order; each unwrite returns H(t+1) to H(t) '
        f'exactly, since L2 overwrote nothing. On the ring: forward from slot {N - 1} is one step, C, to slot 0; backward is '
        f'the {N - 1} step masks in reverse order.')
    gaps = collections.Counter(wt(x ^ P(x, n)) for x in range(N) if x < P(x, n))
    npal = sum(1 for x in range(N) if pal(x, n) and x < P(x, n))
    say(f'  SHAPE, forced in every legal history: {h} facing rows (slot a with slot {N - 1}-a), one slot sum {N - 1}, odd, '
        f'so no slot faces itself; crease = edge {h - 1}|{h}, adjacent slots, no loop; open end = edge {N - 1}|0, closed by C.')
    say(f'  On the {n}-cube mesh: facing-row gaps (bits that differ) {dict(sorted(gaps.items()))}: {npal} palindromic rows '
        f'at gap {n}, the rest at even gaps; closing step weight {n}.')
    say(f'  AMBIGUOUS: where each row sits along the fold, hence the crease gap and every step weight but the closing one. '
        f'Writes {N}: boundary 1, forced {forced}, AMBIGUOUS {amb}. Legal histories = product of the AMBIGUOUS counts = {count}.')
    return dict(N=N, h=h, forced=forced, amb=amb, count=count)

# ---------------------------------------------------------------- exhaustive checks (small n)
def legal_bruteforce(n):
    """Every ordering of the N words with 0^n in slot 0, kept if it obeys L0-L5 (independent of the construction)."""
    N = 1 << n; Pt = [P(x, n) for x in range(N)]
    keep = []
    for rest in itertools.permutations(range(1, N)):
        R = (0,) + rest
        if all(R[N - 1 - a] == Pt[R[a]] for a in range(N)) and all(R[a] != R[(a + 1) % N] for a in range(N)):
            keep.append(R)
    return keep

def legal_structured(n):
    """The construction's histories: 0^n, then the untouched pairs in every order and orientation, then the owed images."""
    N = 1 << n; Pt = [P(x, n) for x in range(N)]
    pairs = sorted({(min(x, Pt[x]), max(x, Pt[x])) for x in range(1, N) if Pt[x] != 0})
    for order in itertools.permutations(pairs):
        for flips in itertools.product((0, 1), repeat=len(pairs)):
            first = [0] + [pr[f] for pr, f in zip(order, flips)]
            yield tuple(first + [Pt[x] for x in reversed(first)])

def route_home(R):
    steps = [R[a] ^ R[(a + 1) % len(R)] for a in range(len(R))]
    back = [R[-1]]
    for a in range(len(R) - 1, 0, -1): back.append(back[-1] ^ steps[a - 1])
    return back[::-1] == list(R) and steps[-1] == R[-1] ^ R[0]

def record_ring(n, swap=True):              # the record's builder (NBR eq. 2-3): used only to locate it, never to generate
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    mid = [P(m, n), m] if swap else [m, P(m, n)]
    return tuple(reps[:-1] + mid + [P(x, n) for x in reversed(reps[:-1])])

def mesh(R, n, edges):
    """Measure a closed history on the n-cube mesh: cube edges joining slots 3+ apart around the ring, labelled by run."""
    N = len(R); pos = [0] * N
    for a, w in enumerate(R): pos[w] = a
    cont = []
    for w, v in edges:
        a, b = pos[w], pos[v]
        if a > b: a, b = b, a
        if b - a >= 3 and N - (b - a) >= 3: cont.append((a, b))
    bs = collections.defaultdict(list); bd = collections.defaultdict(list)
    for a, b in cont: bs[a + b].append(a); bd[b - a].append(a)
    opp = com = both = none = 0
    for a, b in cont:
        sr = any(0 < abs(x - a) <= 2 for x in bs[a + b]); dr = any(0 < abs(x - a) <= 2 for x in bd[b - a])
        if sr and dr: both += 1
        elif sr: opp += 1
        elif dr: com += 1
        else: none += 1
    return len(cont), opp, com, both, none

def insertions(n, k):
    """Uniform maps that insert k new bits at fixed places with fixed values (width n -> n + k)."""
    for places in itertools.combinations(range(n + k), k):
        for vals in itertools.product((0, 1), repeat=k):
            def E(x, places=places, vals=vals):
                b = list(bits(x, n)) if n else []
                for p, v in zip(places, vals): b.insert(p, str(v))
                return int(''.join(b), 2)
            yield places, vals, E

# ---------------------------------------------------------------- RUN THE GENERATOR
out('GENERATOR')
for L in LAWS: out(' ', L)
out(' ', Q)
for n in range(0, 6):
    construct(n)
out('\nWIDTHS 6-8, same rules, step lines not printed:')
for n in range(6, 9):
    r = construct(n, loud=False)
    f = 2 ** (r['h'] - 1) * math.factorial(r['h'] - 1)
    out(f'  n={n}: writes {r["N"]}, forced {r["forced"]}, AMBIGUOUS {r["amb"]}, log10(legal histories) = {math.log10(r["count"]):.2f};'
        f' equals 2^(h-1) (h-1)! with h = {r["h"]}: {r["count"] == f}')

out('\nWITHOUT L5 (slot 0 left open): the closing step is P(x) xor x for the word x in slot 0.')
for n in range(1, 9):
    N = 1 << n
    cl = [x for x in range(N) if P(x, n) ^ x == N - 1]
    pals = sum(pal(x, n) for x in cl)
    out(f'  n={n}: slot-0 words that close by C: {len(cl)} of {N} ({pals} palindromes, {len(cl) - pals} anti-palindromes, J(x) = C(x))')

out('\nEXHAUSTIVE CHECK. n = 1-3: every ordering of the words with 0^n first, filtered by L0-L5, against the construction.'
    ' n = 4: the construction only (15! orderings is out of reach).')
for n in range(1, 5):
    rec = {record_ring(n, True): "record ring, seam exchange (P(m) before m)",
           record_ring(n, False): 'record ring, counter order (m before P(m))'}
    found = dict.fromkeys(rec, False); cnt = home = closeC = 0; seen = set()
    for R in legal_structured(n):
        cnt += 1; home += route_home(R); closeC += (R[-1] ^ R[0] == (1 << n) - 1)
        if R in found: found[R] = True
        if n <= 3: seen.add(R)
    if n <= 3:
        B = legal_bruteforce(n)
        out(f'  n={n}: orderings passing L0-L5 {len(B)}; construction {cnt}; same set: {set(B) == seen}')
    else:
        out(f'  n={n}: construction {cnt} histories (= 7! x 2^7: {cnt == math.factorial(7) * 2 ** 7})')
    out(f'        closing step C in {closeC}; route home (step masks undone in reverse) returns to H0 in {home}')
    for R, name in rec.items():
        out(f'        {name}: {" ".join(bits(x, n) for x in R) if n <= 3 else "(16 words)"}  legal: {found[R]}')

out('\nMESH SHAPE OVER ALL LEGAL HISTORIES (cube edges joining slots 3+ apart around the ring; run = another such edge'
    ' 1-2 slots along with the same slot sum (opposed) or the same slot difference (co-moving)):')
for n in (3, 4):
    N = 1 << n
    edges = [(w, w ^ (1 << i)) for w in range(N) for i in range(n) if w < w ^ (1 << i)]
    lo = dict(cont=10 ** 9, com=9.0, opp=9.0); hi = dict(cont=-1, com=-1.0, opp=-1.0); zc = zo = tot = 0
    for R in legal_structured(n):
        c, o, m, b, z = mesh(R, n, edges); tot += 1
        cs, os_ = ((m + b) / c, (o + b) / c) if c else (0.0, 0.0)
        for key, val in (('cont', c), ('com', cs), ('opp', os_)):
            lo[key] = min(lo[key], val); hi[key] = max(hi[key], val)
        zc += (m + b == 0); zo += (o + b == 0)
    out(f'  n={n}: {tot} histories; mesh contacts {lo["cont"]}-{hi["cont"]}; co-moving share {lo["com"]:.2f}-{hi["com"]:.2f} '
        f'({zc} histories with none); opposed share {lo["opp"]:.2f}-{hi["opp"]:.2f} ({zo} with none)')
    for swap, name in ((True, 'seam exchange'), (False, 'counter order')):
        c, o, m, b, z = mesh(record_ring(n, swap), n, edges)
        out(f'        record ring, {name}: contacts {c}, opposed {o}, co-moving {m}, both {b}, none {z}; '
            f'co-moving share {(m + b) / c:.2f}, opposed share {(o + b) / c:.2f}')

out('\nPAST CLOSURE. Every word of width n is written and L4 returns slot N-1 to slot 0: no write remains at width n.')
out('  Continuing needs a new distinction (a new bit). The history does not provide one.  OPEN: the provider of the new bit.')
out('  If one is provided, the closed history must survive (L2) with its facings (L3). Every uniform insertion, tried:')
k1, k2, pal_any = {}, {}, 0
for n in range(1, 7):
    N = 1 << n
    rows = [(x, P(x, n)) for x in range(N) if x < P(x, n)]
    nonpal = [r for r in rows if not pal(r[0], n)]; palr = [r for r in rows if pal(r[0], n)]
    for k in (1, 2):
        keep, maxpal, tried = [], 0, 0
        for places, vals, E in insertions(n, k):
            tried += 1
            if nonpal and all(P(E(x), n + k) == E(y) for x, y in nonpal): keep.append((places, vals))
            maxpal = max(maxpal, sum(P(E(x), n + k) == E(y) for x, y in palr))
        pal_any = max(pal_any, maxpal)
        (k1 if k == 1 else k2)[n] = len(keep)
        desc = ' '.join(''.join(map(str, v)) + '@' + ','.join(map(str, p)) for p, v in keep)
        rec = f"; the record's nesting 1.x.1 (11@0,{n + 1}) among them: {((0, n + 1), (1, 1)) in keep}" if k == 2 and nonpal else ''
        what = (f'keep all {len(nonpal)} non-palindromic rows: {len(keep)} [{desc}]' if nonpal
                else 'no non-palindromic rows to keep')
        out(f'  n={n} -> {n + k}: {tried} insertions; {what}; palindromic rows kept by any insertion: {maxpal} of {len(palr)}{rec}')
if pal_any == 0:
    out('  No uniform insertion keeps any palindromic row: its partner is C, and C flips the new bits too. Those rows have no way'
        ' home through a widening; they are the piece that moves. No uniform insertion keeps the whole closed history.')
if all((k1[n] > 0) == (n % 2 == 0) for n in k1 if n > 1):
    out('  One new bit (n -> n+1) keeps the non-palindromic rows only at even n, only at the centre, either value. At odd n'
        ' every single-bit insertion also breaks a non-palindromic facing: from odd n, n -> n+1 keeps no facing block.')
if all(k2[n] > 0 for n in k2 if n > 1):
    out('  Two new bits (n -> n+2) keep them at every n: mirrored places, equal values. Which pair of places and which value:'
        ' AMBIGUOUS, qualifier missing.')

# ---------------------------------------------------------------- SEAL
GEN_HASH = hashlib.sha256(GEN.getvalue().encode()).hexdigest()
PRED = ("s199 seal. Written after the generator ran, before any chain file is opened in this run. Generator output "
        "SHA-256 " + GEN_HASH + ". Forced by the laws in every legal history, what each says about chains, and the readout "
        "it returns through (s188 detector, ecoli_chains.json): "
        "G1 one register per fold: every facing row shares one slot sum. Readout: stored pairs at S+1 or S-1 inside a "
        "hairpin's span; each hairpin carrying one lies outside the generator. "
        "G2 edge-centred crease: the facing sum is odd and no slot faces itself. Readout: parity of S; even S lies outside. "
        "G3 no loop: the two crease slots are adjacent. Readout: s - e of the crease pair; s - e > 1 lies outside. The laws "
        "hold no provider for a loop width: OPEN. "
        "G4 facing layer: the laws make only opposed facings (one slot sum). Readout: run label of every stored pair in all "
        "160 chains; pairs in co-moving runs lie outside the facing layer. Mesh layer (cube edges between slots 3+ apart): "
        "it depends on the AMBIGUOUS order; at n = 4 every legal order carries co-moving mesh runs (share 0.11-0.96) and "
        "128 orders carry no opposed mesh run, so on the mesh co-moving runs are unavoidable and opposed runs avoidable, at "
        "no fixed share. No chain share is predicted from the mesh layer. "
        "G5 the open end closes by C. Chains are open: no counterpart, not tested. "
        "G6 which word sits in which slot is AMBIGUOUS: no residue-level claim. "
        "Not blind: G1 (s197 census of S-1 and S+1 pairs), G2 and G3 (s188/s197: 94 odd, 49 even; the detector admits "
        "only pairs 3 or more apart). Not run before: G4 on all chains (s198 labelled hairpin rows only); the side note's "
        "i+3 and i+4 counts, read before this seal, bear on it. Checks of the side note, not predictions: directed "
        "contacts, i+3 and i+4 counts, the k = 3 / k = 4 choice where both O lie within 3.5 A.")
out('\nSEAL\n ', PRED)
out('  SHA-256', hashlib.sha256(PRED.encode()).hexdigest())
sys.stdout.flush()

# ---------------------------------------------------------------- READER (the chain file is opened only here)
if len(sys.argv) < 2: sys.exit(0)
import numpy as np
raw = open(sys.argv[1], 'rb').read()
print('\nREADER  chain file raw SHA-256', hashlib.sha256(raw).hexdigest())
chains = json.loads(raw)

def coords(ent):
    R = ent['residues']
    return [r[1] for r in R], np.array([r[2] for r in R], float), np.array([r[5] for r in R], float)

def closures(ent):                          # identical to s188-s198
    seq, Nn, O = coords(ent); L = len(seq)
    dd = np.linalg.norm(Nn[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    res = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: res.add((i, j))
    return res

def hairpins(directed, L):                  # identical to s188-s198
    und = {(min(c), max(c)) for c in directed}
    byS = collections.defaultdict(list)
    for a, b in und: byS[a + b].append((a, b))
    res = []
    for S, pts in byS.items():
        pts = sorted(set(pts)); run = [pts[0]]
        for p in pts[1:] + [None]:
            if p is not None and p[0] - run[-1][0] <= 2: run.append(p); continue
            if len(run) >= 3 and run[-1][1] - run[-1][0] <= 8:
                e, s = run[-1]; res.append((e, s, min(e - run[0][0], e, L - 1 - s), S))
            if p is not None: run = [p]
    return res

ALLD, UND, HP = [], [], []
k3 = k4 = 0; both = picked4 = picked3 = picked_other = near4 = near3 = 0
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    D = closures(ent) if L >= 3 else set()      # reader fix after the seal: one chain has no residues
    ALLD.append(D); UND.append({(min(c), max(c)) for c in D})
    if L >= 30: HP += [(ci,) + hp for hp in hairpins(D, L)]
    seq, Nn, O = coords(ent)
    for i, j in D:
        k3 += (i - j == 3); k4 += (i - j == 4)
    for i in range(4, L):
        if seq[i] == 'P': continue
        d3, d4 = np.linalg.norm(Nn[i] - O[i - 3]), np.linalg.norm(Nn[i] - O[i - 4])
        if d3 <= 3.5 and d4 <= 3.5:
            both += 1; near4 += d4 < d3; near3 += d3 <= d4
            if (i, i - 4) in D: picked4 += 1
            elif (i, i - 3) in D: picked3 += 1
            else: picked_other += 1
print(f'  chains {len(chains)}, residues 0 in {sum(len(e["residues"]) == 0 for e in chains)}, under 30 in {sum(len(e["residues"]) < 30 for e in chains)}')
print(f'  side note check: directed contacts {sum(len(D) for D in ALLD)} (chains of 30+: {sum(len(D) for D, e in zip(ALLD, chains) if len(e["residues"]) >= 30)}); donor i -> O(i-3): {k3}; donor i -> O(i-4): {k4}; '
      f'donors with both O(i-3) and O(i-4) within 3.5 A: {both}; closure rule picks O(i-4) {picked4}, O(i-3) {picked3}, '
      f'another O {picked_other}; nearer of the two: i-4 {near4}, i-3 {near3}')
print(f'  hairpins (L >= 30): {len(HP)}')

hp1 = cr1 = ar1 = 0; pairs_pm = collections.Counter()
for ci, e, s, k, S in HP:
    sec = [(a, b) for a, b in UND[ci] if abs(a + b - S) == 1 and e - k <= a and b <= s + k]
    cr = [p for p in sec if e <= p[0] and p[1] <= s]; ar = [p for p in sec if not (e <= p[0] and p[1] <= s)]
    hp1 += bool(sec); cr1 += bool(cr); ar1 += bool(ar)
    for a, b in sec: pairs_pm['S+1' if a + b == S + 1 else 'S-1'] += 1
print(f'  G1 one register: hairpins carrying a pair at S+-1 in their span {hp1} of {len(HP)} (in the crease {cr1}, on the arms {ar1}); '
      f'pairs {dict(pairs_pm)}  -> outside the generator: {hp1}; single-register hairpins: {len(HP) - hp1}')
odd = sum(h[4] % 2 for h in HP)
print(f'  G2 edge-centred crease: odd S {odd}, even S {len(HP) - odd}  -> outside the generator: {len(HP) - odd}')
sep = collections.Counter(h[2] - h[1] for h in HP)
print(f'  G3 no loop: crease pair s - e {dict(sorted(sep.items()))}  -> outside the generator: '
      f'{sum(v for d, v in sep.items() if d > 1)} of {len(HP)} (the detector admits no pair closer than 3)')
tab = collections.Counter(); comsep = collections.Counter()
for U in UND:
    bs = collections.defaultdict(set); bd = collections.defaultdict(set)
    for a, b in U: bs[a + b].add(a); bd[b - a].add(a)
    for a, b in U:
        sr = any(0 < abs(x - a) <= 2 for x in bs[a + b]); dr = any(0 < abs(x - a) <= 2 for x in bd[b - a])
        lab = 'both' if sr and dr else 'opposed' if sr else 'co-moving' if dr else 'no run'
        tab[lab] += 1
        if dr: comsep[b - a] += 1
tot = sum(tab.values())
print(f'  G4 all 160 chains, {tot} stored pairs: ' + ', '.join(f'{lab} {v} ({v / tot:.2f})' for lab, v in tab.most_common()))
print(f'     pairs in co-moving runs by j - i (top 8): {dict(comsep.most_common(8))}  -> outside what the laws force: '
      f'{tab["co-moving"] + tab["both"]} ({(tab["co-moving"] + tab["both"]) / tot:.2f})')
print('  G5 open end closed by C: chains are open, no counterpart.  G6: no residue-level claim made, none read.')
```

## `side199.py` — the uploads' runnable claims (sha `1346f3bb…`)

```python
"""NEXUS s199, side material: the runnable claims in the six uploads of this prompt.
A  s167 RIS numbers: an independent Flory frame-matrix computation (9 coordinates, built here from the RIS definition),
   against the source values, GPT's transcription of the s167 four-coordinate reader, and LM Studio's substituted numbers.
B  ring identities: delta(Px) = rev(delta(x)); reader-window counts; the sliding two-difference reader; the two-bit token code.
C  signed dihedral under reversal of the atom order and under a mirror.
D  NotebookLM transcript: the 41 hard-coded records, multi-donor acceptors, its steric-lock routine, the O(n) rank formula.
E  the record's ring as a binding of the generator's AMBIGUOUS writes by the counter.
Run: python3 -I side199.py ecoli_chains.json
"""
import collections, itertools, json, math, sys
import numpy as np

print('A. s167 RIS: independent frame-matrix computation')
Rg = 8.314462618
def cinf_frames(sigma, omega, costh=1 / 3):
    """C_inf = 1 + 2 sum_k <[T_1..T_k]_11> over the stationary RIS Markov chain; states t, g+, g- at 0, +120, -120 deg."""
    U = np.array([[1, sigma, sigma], [1, sigma, sigma * omega], [1, sigma * omega, sigma]], float)
    w, V = np.linalg.eig(U); k = int(np.argmax(w.real)); lam = w[k].real; v = np.abs(V[:, k].real)
    wl, Vl = np.linalg.eig(U.T); u = np.abs(Vl[:, int(np.argmax(wl.real))].real)
    pi = u * v / (u @ v); Pm = U * v[None, :] / (lam * v[:, None])
    s = math.sqrt(1 - costh ** 2)
    def T(phi):
        c, sn = math.cos(phi), math.sin(phi)
        return np.array([[costh, s, 0], [s * c, -costh * c, sn], [s * sn, -costh * sn, -c]])
    TT = np.zeros((9, 9))
    for a, ph in enumerate((0, 2 * math.pi / 3, -2 * math.pi / 3)): TT[3 * a:3 * a + 3, 3 * a:3 * a + 3] = T(ph)
    M = np.kron(Pm, np.eye(3)) @ TT
    L = np.kron(pi[None, :], np.eye(3)); Rr = np.kron(np.ones((3, 1)), np.eye(3))
    return 1 + 2 * (L @ TT @ np.linalg.solve(np.eye(9) - M, Rr))[0, 0], M

def gpt_167(sigma, omega):                  # GPT's transcription of the s167 four-coordinate reader (upload 8034d7e7), verbatim
    lam = (1 + sigma * (1 + omega) + math.sqrt((1 - sigma * (1 + omega)) ** 2 + 8 * sigma)) / 2
    a = 1 / lam; q = (lam - 1) / (2 * lam); r = sigma / lam; s = sigma * omega / lam; t = r + s; dif = r - s; d = 1 - t
    alpha = (2 * dif - 1) / (2 - dif); beta = (1 - dif) / (2 - dif)
    A = np.array([[1, -a, 0, -2 * q * alpha], [-a, 1, -2 * q, -2 * q * beta], [0, -d, 1, -t * alpha], [-d, 0, -t, 1 - t * beta]], float)
    u0, v0, u, v = np.linalg.solve(A, np.array([0, 1, 0, 1], float))
    pi0 = d / (d + 2 * q); pig = q / (d + 2 * q)
    return 2 * (pi0 * (u0 / 3 + v0) + 2 * pig * (u / 3 + v)) - 1, A

s413, w413 = math.exp(-2100 / (Rg * 413)), math.exp(-8400 / (Rg * 413))
s300, w300 = math.exp(-2100 / (Rg * 300)), math.exp(-8400 / (Rg * 300))
cases = [('equal weights', 1, 1, '2.000000000'), ('413 K, omega = 1', s413, 1, '3.124392391'),
         ('413 K, both penalties', s413, w413, '6.229676328'), ('300 K, both penalties', s300, w300, '7.200650328'),
         ('413 K, g+g- forbidden (omega = 0)', s413, 0, '6.715345190 (GPT, 04a5f4d1)'),
         ('LM: sigma .543, omega 1', .543, 1, '3.124392391 claimed; GPT: 3.122160835'),
         ('LM: sigma .543, omega .088', .543, .088, '6.229676328 claimed; GPT: 6.219869293'),
         ('LM: sigma .350, omega .020', .350, .020, '7.200650328 claimed; GPT: 8.037816088')]
print(f'  {"case":36} {"sigma":>11} {"omega":>11} {"frames (here)":>14} {"s167 4-coord":>14} {"2(2+s)/3s":>12}  quoted')
for name, sg, om, quoted in cases:
    cf, _ = cinf_frames(sg, om); c4, _ = gpt_167(sg, om)
    print(f'  {name:36} {sg:11.9f} {om:11.9f} {cf:14.9f} {c4:14.9f} {2 * (2 + sg) / (3 * sg):12.9f}  {quoted}')
rng = np.random.default_rng(199); dmax = 0.0
for _ in range(2000):
    sg, om = rng.uniform(0.02, 3), rng.uniform(0, 3)
    dmax = max(dmax, abs(cinf_frames(sg, om)[0] - gpt_167(sg, om)[0]))
print(f'  four-coordinate reader vs nine-coordinate frames, 2000 random (sigma, omega): max |difference| {dmax:.2e}')
_, A1 = gpt_167(s413, w413); _, A2 = gpt_167(s300, w300)
print(f'  one fixed basis of four uncoupled channels would make A(413 K) and A(300 K) commute: ||[A1, A2]|| = {np.linalg.norm(A1 @ A2 - A2 @ A1):.3f}')
_, M = cinf_frames(s413, w413)
S = np.zeros((9, 9)); D = np.diag([1, 1, -1]); perm = [0, 2, 1]
for a in range(3): S[3 * perm[a]:3 * perm[a] + 3, 3 * a:3 * a + 3] = D
ev = np.linalg.eigvalsh((S + S.T) / 2)
print(f'  mirror symmetry (g+ <-> g-, z -> -z) commutes with the 9x9 operator: ||[S, M]|| = {np.linalg.norm(S @ M - M @ S):.1e}; '
      f'sectors: even {int(round(sum(ev > 0)))}, odd {int(round(sum(ev < 0)))} (two blocks, not four scalars)')

print('\nB. ring identities')
def J(x, n): return int(format(x, f'0{n}b')[::-1], 2) if n else 0
def C(x, n): return x ^ ((1 << n) - 1)
def P(x, n): return C(x, n) if J(x, n) == x else J(x, n)
def delta(x, n): b = format(x, f'0{n}b'); return [int(b[k]) ^ int(b[k + 1]) for k in range(n - 1)]
fails = sum(delta(P(x, n), n) != delta(x, n)[::-1] for n in range(1, 14) for x in range(1 << n))
print(f'  delta(P x) = rev(delta(x)), every word n = 1..13 ({sum(1 << n for n in range(1, 14))} words): failures {fails}')
print('  proof: off palindromes P = J and differences of a reversed word are the reversed differences; on palindromes P = C,'
      ' which leaves every difference unchanged, and a palindrome has palindromic differences.')
for w in range(1, 9):
    fixed = sum(J(x, w) == x for x in range(1 << w))
    print(f'  window width {w}: reversal-fixed {fixed} (2^ceil(w/2) = {2 ** math.ceil(w / 2)}), exchanged pairs {((1 << w) - fixed) // 2}', end='')
    print(f' (formula {((1 << w) - 2 ** math.ceil(w / 2)) // 2})')
bad = 0
for n in range(3, 14):
    for x in range(1 << n):
        d, dp = delta(x, n), delta(P(x, n), n); L = n - 1
        s, sp = [d[i + 1] - d[i] for i in range(L - 1)], [dp[i + 1] - dp[i] for i in range(L - 1)]
        bad += any(sp[i] != -s[L - 2 - i] for i in range(L - 1))
print(f'  sliding reader s_i = d_(i+1) - d_i: s_i(Px) = -s_(L-2-i)(x) for every word n = 3..13: failures {bad}')
for L in (4, 6, 8):
    seqs = {tuple(dd[i + 1] - dd[i] for i in range(L - 1)) for dd in itertools.product((0, 1), repeat=L)}
    pp = sum(any(sq[i] == 1 and sq[i + 1] == 1 for i in range(L - 2)) for sq in seqs)
    print(f'  sliding reader over {L} differences: {len(seqs)} distinct readings of {3 ** (L - 1)} ternary sequences; '
          f'readings with +1 followed by +1: {pp}')
code = {'t': (0, 0), '+': (0, 1), '-': (1, 0)}; dec = {v: k for k, v in code.items()}; flip = {'t': 't', '+': '-', '-': '+'}
tot = ok = 0
for m in range(1, 9):
    n = 2 * m + 1
    for q in itertools.product('t+-', repeat=m):
        dd = [b for s_ in q for b in code[s_]]; bits = [0]
        for b in dd: bits.append(bits[-1] ^ b)
        x = int(''.join(map(str, bits)), 2); dp = delta(P(x, n), n)
        got = tuple(dec.get(tuple(dp[2 * i:2 * i + 2]), '?') for i in range(m))
        tot += 1; ok += got == tuple(flip[s_] for s_ in reversed(q))
print(f'  two-bit token code t=00, g+=01, g-=10 under P: {ok} of {tot} ternary histories (m = 1..8) read back reversed with g+ <-> g-')

print('\nC. signed dihedral')
def dihedral(p0, p1, p2, p3):
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1n = b1 / np.linalg.norm(b1); v = b0 - (b0 @ b1n) * b1n; w_ = b2 - (b2 @ b1n) * b1n
    return math.degrees(math.atan2(np.cross(b1n, v) @ w_, v @ w_))
rng = np.random.default_rng(7); same = flipd = 0
for _ in range(10000):
    p = rng.normal(size=(4, 3))
    d1, d2 = dihedral(*p), dihedral(*p[::-1]); d3 = dihedral(*(p * np.array([-1, 1, 1])))
    same += abs(d1 - d2) < 1e-9; flipd += abs(d1 + d3) < 1e-9
print(f'  10000 random atom quadruples: reversed order keeps the dihedral {same}/10000; a mirror flips its sign {flipd}/10000')

print('\nE. the record ring as a binding of the AMBIGUOUS writes by the counter')
def record_ring(n, swap=True):
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    mid = [P(m, n), m] if swap else [m, P(m, n)]
    return reps[:-1] + mid + [P(x, n) for x in reversed(reps[:-1])]
for n in range(2, 13):
    N = 1 << n; h = N // 2; R = [None] * N; R[0], R[N - 1] = 0, P(0, n); used = {0, P(0, n)}; ctr = 0
    for t in range(1, h):                  # AMBIGUOUS writes, bound by reading the counter forward
        while ctr in used or P(ctr, n) < ctr: ctr += 1
        R[t], R[N - 1 - t] = ctr, P(ctr, n); used |= {ctr, P(ctr, n)}
    diff = [a for a in range(N) if R[a] != record_ring(n, True)[a]]
    print(f'  n={n:2d}: counter binding = record ring with counter order: {R == record_ring(n, False)}; '
          f'slots where it differs from the record ring: {diff}')

print('\nD. NotebookLM transcript (upload c6bd5944)')
raw = open(sys.argv[1], 'rb').read(); chains = json.loads(raw)
pdbs = {str(e.get('pdb', '')).upper() for e in chains}
print(f'  Answer 13 PDB ids present in the chain file: {sorted(p for p in ["1ECL", "1A8L", "2I10", "3D10", "1C32", "4I10", "1UBQ"] if p in pdbs)}')
def closures(ent):
    R = ent['residues']; seq = [r[1] for r in R]; L = len(R)
    if L < 3: return set()
    Nn = np.array([r[2] for r in R], float); O = np.array([r[5] for r in R], float)
    dd = np.linalg.norm(Nn[:, None, :] - O[None, :, :], axis=2)
    ix = np.arange(L); dd[np.abs(ix[:, None] - ix[None, :]) <= 2] = np.inf
    res = set()
    for i in range(1, L):
        if seq[i] == 'P': continue
        j = int(dd[i].argmin())
        if dd[i, j] <= 3.5: res.add((i, j))
    return res
multi = 0; chains_multi = 0
for e in chains:
    cnt = collections.Counter(j for i, j in closures(e))
    mm = sum(1 for v in cnt.values() if v > 1); multi += mm; chains_multi += mm > 0
print(f'  O acceptors chosen by more than one donor: {multi}, in {chains_multi} chains (GPT/Dean, Q16: 1,292 in 157)')

def build_3d_chain(face_bit, delta_seq):    # NotebookLM Answer 17, transcribed verbatim
    b = [face_bit]
    for d in delta_seq: b.append(b[-1] ^ d)
    vertices = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)]
    cos_th, sin_th = -0.5, np.sqrt(3) / 2.0
    dir_curr = np.array([cos_th, sin_th, 0.0])
    vertices.append((vertices[-1][0] + dir_curr[0], vertices[-1][1] + dir_curr[1], vertices[-1][2] + dir_curr[2]))
    for idx, d in enumerate(delta_seq):
        phi = np.pi if d == 1 else 0.0
        cos_p, sin_p = np.cos(phi), np.sin(phi)
        new_x = dir_curr[0] * cos_th - dir_curr[1] * sin_th * cos_p
        new_y = dir_curr[0] * sin_th + dir_curr[1] * cos_th * cos_p
        new_z = dir_curr[1] * sin_p
        dir_curr = np.array([new_x, new_y, new_z]); norm = np.linalg.norm(dir_curr)
        if norm > 1e-9: dir_curr = dir_curr / norm
        vertices.append((vertices[-1][0] + dir_curr[0], vertices[-1][1] + dir_curr[1], vertices[-1][2] + dir_curr[2]))
    return np.array(vertices)
def check_min_distance(vertices, threshold=0.1):
    md = 1e9
    for i in range(len(vertices)):
        for j in range(i + 2, len(vertices)): md = min(md, np.linalg.norm(vertices[i] - vertices[j]))
    return md < threshold, md
for hist in ([1, 0, 1, 0], [1, 0, 0, 1], [1, 1]):
    base = build_3d_chain(0, hist)
    r0, r1 = check_min_distance(build_3d_chain(0, hist + [0])), check_min_distance(build_3d_chain(0, hist + [1]))
    print(f'  its routine, history {hist}: history alone d_min {check_min_distance(base)[1]:.4f}; next 0 d_min {r0[1]:.4f}; '
          f'next 1 d_min {r1[1]:.4f}; max |z| {max(abs(build_3d_chain(0, hist + [b])[:, 2]).max() for b in (0, 1)):.1e}')
for d in (1, 0):
    v = build_3d_chain(0, [d]); u1, u2 = v[2] - v[1], v[3] - v[2]
    print(f'  its step for delta = {d}: angle between successive bond vectors {math.degrees(math.acos(np.clip(u1 @ u2, -1, 1))):.1f} deg')

def Jh(x, h): return int(format(x, f'0{h}b')[::-1], 2) if h else 0
def R_rect(u, v, h):                        # R_h(u, v) = sum_j u_j ceil((v - rho_j) / 2^(j+1)), u read MSB first
    tot = rho = 0
    for j in range(h):
        uj = (u >> (h - 1 - j)) & 1
        if uj: tot += -((rho - v) // (1 << (j + 1)))
        rho += uj << j
    return tot
def Delta(p, n):
    h = n // 2; H = 1 << h; B = p & (H - 1)
    if n % 2 == 0:
        A = p >> h; return A * (H - A) + B - 2 * R_rect(B, A, h) - (Jh(A, h) < B)
    A, b = p >> (h + 1), (p >> h) & 1
    return 2 * A * (H - A) + b * (H - 1 - 2 * A) + B - 2 * R_rect(B, A, h) - (Jh(A, h) < B)
def rank(p, n):
    top = p >> (n - (n + 1) // 2)
    pal_below = top + (int(format(top, f'0{(n + 1) // 2}b') + format(top, f'0{(n + 1) // 2}b')[::-1][n % 2:], 2) < p)
    return (p - pal_below + Delta(p, n)) // 2 + min(pal_below, 2 ** ((n + 1) // 2 - 1))
badR = badD = badK = 0
for n in range(2, 15):
    N = 1 << n; h = n // 2
    for B in range(1 << h):
        for A in range(1 << h):
            badR += R_rect(B, A, h) != sum(1 for b2 in range(B) if Jh(b2, h) < A) if n <= 10 else 0
    c = [0] * (N + 1); reps = [0] * (N + 1)
    for x in range(N):
        jx = J(x, n); c[x + 1] = c[x] + (jx > x) - (jx < x); reps[x + 1] = reps[x] + (x < P(x, n))
    for p in range(N + 1):
        badD += Delta(p, n) != c[p]; badK += rank(p, n) != reps[p]
print(f'  O(n) rank formula: rectangle sum vs its definition (n <= 10) failures {badR}; Delta vs direct count (n = 2..14) '
      f'failures {badD}; rank vs direct count of representatives (n = 2..14) failures {badK}')
x = 0x243F6A8885A308D3
print(f'  64-bit pi word: representative {x < P(x, 64)}; address = rank = {rank(x, 64):,} (Answer 3: 2,427,008,858,123,944,441)')
```
