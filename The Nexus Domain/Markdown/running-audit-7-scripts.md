# NEXUS running audit 7, scripts for § 197

Companion to `claude/running-audit-7.md`. Every script below ran as printed, with `python3 -I`, on `ecoli_chains.json` (raw SHA-256 f5266a44…); their live output is in § 197.

`tp_pt.py`

```python
"""§ 197. TP and PT on the chain, from the ring: assignment, location and split sealed; landed on the full census.
Run: python3 -I tp_pt.py <ecoli_chains.json>"""
import hashlib, json, sys, collections, math
import numpy as np

def J(x, n): return int(format(x, f'0{n}b')[::-1], 2)
def C(x, n): return x ^ ((1 << n) - 1)
def P(x, n): return C(x, n) if J(x, n) == x else J(x, n)
def ring(n):
    reps = sorted(x for x in range(1 << n) if x < P(x, n)); m = reps[-1]
    return reps[:-1] + [P(m, n), m] + [P(x, n) for x in reversed(reps[:-1])]

print('PART 1  the ring alone (positions: P a -> N-1-a, T a -> a+1; TP = T after P, PT = P after T)')
for n in range(2, 15):
    R = ring(n); N = len(R); h = N // 2; m = R[h]
    Pp = lambda a: N - 1 - a
    Tt = lambda a: (a + 1) % N
    Ti = lambda a: (a - 1) % N
    TP = lambda a: Tt(Pp(a))
    PT = lambda a: Pp(Tt(a))
    fTP = [a for a in range(N) if TP(a) == a]; fPT = [a for a in range(N) if PT(a) == a]
    conjT = all(TP(a) == Tt(PT(Ti(a))) for a in range(N))        # TP = T.PT.T^-1
    conjP = all(PT(a) == Pp(TP(Pp(a))) for a in range(N))        # PT = P.TP.P
    rot2 = all(TP(PT(a)) == (a + 2) % N for a in range(N))       # TP.PT = T^2: a rotation, no facing
    face = all(R[N - 1 - a] == P(R[a], n) for a in range(N))
    wTP = [bin(R[a]).count('1') for a in fTP]; wPT = [bin(R[a]).count('1') for a in fPT]
    ok = fTP == [0, h] and fPT == [h - 1, N - 1] and R[0] == 0 and R[h - 1] == P(m, n) and R[N - 1] == (1 << n) - 1
    if n <= 4 or n in (8, 14):
        print(f'  n={n:2}: facing law {face}; Fix(TP) {fTP} words 0^n, m  weights {wTP}; Fix(PT) {fPT} words P(m), 1^n  weights {wPT}; '
              f'TP = T.PT.T^-1 {conjT}; PT = P.TP.P {conjP}; TP.PT = T^2 {rot2}; layout {ok}')
    assert face and conjT and conjP and rot2 and ok
print('  n = 2..14 all hold')

print('\n  chain to ring: a stored pair (i < j) at sum S + d goes to cells (i - e + h - 1, j - s + h), ring sum N - 1 + d;')
print('  it is self-facing (one cell) iff j - i = w - 1.  Crease-region pairs (e <= i < j <= s, j - i >= 3) at S +- 1:')
for w in range(3, 9):
    e = 20; s = e + w; S = e + s
    for d, name in ((+1, 'TP'), (-1, 'PT')):
        rows = [(i, S + d - i) for i in range(e, s + 1) if e <= i < S + d - i <= s and (S + d - i) - i >= 3]
        tag = [('(e%+d, s%+d)' % (i - e, j - s)) + (' SELF' if j - i == w - 1 else '') for i, j in rows]
        print(f'    w={w} {name}: {", ".join(tag) if tag else "none (all within |i-j| <= 2)"}')

PRED = ("s197, sealed before this script opens ecoli_chains.json. NOT BLIND, stated: the s193 residual (62/11/30/33), GPT's 41-slip "
        "trace and the side run's +-1 breakdown (parity, location, donor side) were read before this seal; the full census with emitted "
        "closures, mutual vs one-way per pair, and the anchor status of the inward PT pairs were not printed there. "
        "Orientation: T = N->C, listed half = outgoing strand. A stored pair (i<j) at sum S+d maps to ring cells (i-e+h-1, j-s+h), "
        "ring sum N-1+d. "
        "(1) Assignment: S+1 is TP (sum N); S-1 is PT (sum N-2). "
        "(2) Location: a pair is self-facing iff its two cells coincide, j-i = w-1. TP's is (e+1,s): cell h, the word m, first cell past "
        "the break; s faces e and e+1, so the outgoing strand holds the extra residue; inward TP rows (e+1+u, s-u). PT's is (e,s-1): "
        "cell h-1, the word P(m), last cell of the rise; e faces s-1 and s, so the returning strand holds the extra residue; inward PT "
        "rows (e+u, s-1-u). The other fixed cells (0^n for TP, 1^n for PT) lie on the wrap, off any hairpin; not tested. "
        "(3) Split: the ring gives none. TP = T.PT.T^-1 and PT = P.TP.P; the fixed sets differ by one step of T, and in value only by "
        "the rail held (0^n against 1^n). A facing is mutual (P is an involution), so the ring's 1:1 is a claim about facings, pairs "
        "stored in both directions. A one-way bond is not a facing; the ring makes no count claim for it, and an excess there is the "
        "bond's direction, which P does not carry. "
        "(4) One reflection per crease: TP.PT = T^2 is a rotation, so no crease holds a TP facing and a PT facing. "
        "(5) A register is anchored at its fixed cell: every hairpin with an inward facing (u >= 1) stores its anchor, (e+1,s) or "
        "(e,s-1), in at least one direction. "
        "(6) The s193 zipper emits (s-1 -> e) at every width above 3, so the residual 30/11 is no TP:PT census; with emitted closures "
        "counted, S-1 outnumbers S+1. "
        "Bars, on the crease region (both residues in e..s): B1 hairpins with a TP facing only against a PT facing only, two-sided "
        "binomial p >= 0.05 against 1:1; B2 hairpins with both facings = 0; B3 one-way bonds: PT at least twice TP and at least 90 % "
        "donated by the later residue (seen; a check); B4 every inward facing has its anchor stored; B5 full window census "
        "S-1 > S+1 (seen; a check). "
        "Water: not opened. Its address would be the rail: TP's and PT's fixed sets differ in value only by 0^n against 1^n (value bit "
        "1 = wet), and those cells lie on the wrap, off the hairpins; with the facings this few, a water comparison could not land.")
print('\nPART 2  sealed prediction\n ', PRED)
print('  SHA-256', hashlib.sha256(PRED.encode()).hexdigest()); sys.stdout.flush()

# ---------------------------------------------------------------- PART 3: the chains (s188 detector, s193 zipper v2)
raw = open(sys.argv[1], 'rb').read()
print('\nPART 3  data  raw SHA-256', hashlib.sha256(raw).hexdigest())
chains = json.loads(raw)

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

def zipv2(e, s, k):
    ret = s if s - e == 3 else s - 1
    out = {(e, s), (ret, e)}
    for t in range(1, k + 1):
        if t % 2 == 0: out |= {(e - t, s + t), (s + t, e - t)}
    return out

def binom_two_sided(x, n):
    pr = [math.comb(n, i) / 2 ** n for i in range(n + 1)]
    return min(1.0, sum(p for p in pr if p <= pr[x] * (1 + 1e-12)))

HP = []; DIR = {}
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    DIR[ci] = closures(ent)
    HP += [(ci,) + h for h in hairpins(DIR[ci], L)]
print(f'  hairpins {len(HP)}, even S {sum(h[4] % 2 == 0 for h in HP)}')

# (a) the s193 residual, as GPT and s193 counted it
resid = collections.Counter(); slips = []
for ci, e, s, k, S in HP:
    D = DIR[ci]; stored = {(i, j) for i, j in D if e - k <= i <= s + k and e - k <= j <= s + k}
    for i, j in sorted(stored - zipv2(e, s, k)):
        d = i + j - S
        resid['S' if d == 0 else 'S-1' if d == -1 else 'S+1' if d == 1 else 'other'] += 1
        if abs(d) == 1: slips.append((ci, e, s, k, S, i, j, d))
print(f'\n  (a) s193 residual (stored, not emitted, inside the window): {dict(resid)}  slips {len(slips)}: '
      f'S+1 {sum(x[7] == 1 for x in slips)}, S-1 {sum(x[7] == -1 for x in slips)}')
hp_sl = {x[:5] for x in slips}; und_sl = {(x[0], min(x[5], x[6]), max(x[5], x[6]), x[7]) for x in slips}
loop = lambda x: x[1] < x[5] < x[2]
print(f'      GPT\'s description checked: hairpins {len(hp_sl)}, chains {len({x[0] for x in hp_sl})}, undirected pairs {len(und_sl)} '
      f'(+1: {sum(u[3] == 1 for u in und_sl)}, -1: {sum(u[3] == -1 for u in und_sl)}); donors inside the loop: '
      f'-1 {sum(loop(x) for x in slips if x[7] == -1)}/{sum(x[7] == -1 for x in slips)}, +1 {sum(loop(x) for x in slips if x[7] == 1)}/{sum(x[7] == 1 for x in slips)}')
print('      slip hairpins by S parity: even', sum(h[4] % 2 == 0 for h in hp_sl), 'odd', sum(h[4] % 2 == 1 for h in hp_sl),
      '| all hairpins: even', sum(h[4] % 2 == 0 for h in HP), 'odd', sum(h[4] % 2 == 1 for h in HP))

# (b) the full census: every stored bond in the window at S +- 1, emitted or not
full = collections.Counter(); rows = []
for ci, e, s, k, S in HP:
    D = DIR[ci]; Z = zipv2(e, s, k)
    for i, j in D:
        if not (e - k <= i <= s + k and e - k <= j <= s + k): continue
        d = i + j - S
        if abs(d) != 1: continue
        a, b = min(i, j), max(i, j)
        region = 'crease' if e <= a and b <= s else 'arm'
        mutual = (j, i) in D
        later = i > j                       # the donor is the later residue
        rows.append(dict(ci=ci, e=e, s=s, k=k, S=S, w=s - e, i=i, j=j, d=d, a=a, b=b, region=region,
                         mutual=mutual, later=later, emitted=(i, j) in Z))
        full[(d, region)] += 1
print(f'\n  (b) full window census at S +- 1 (directed bonds): S-1 {sum(r["d"] == -1 for r in rows)} '
      f'(crease {full[(-1, "crease")]}, arm {full[(-1, "arm")]}; emitted by the zipper {sum(r["d"] == -1 and r["emitted"] for r in rows)}), '
      f'S+1 {sum(r["d"] == 1 for r in rows)} (crease {full[(1, "crease")]}, arm {full[(1, "arm")]}; emitted {sum(r["d"] == 1 and r["emitted"] for r in rows)})')
for d in (-1, 1):
    for reg in ('crease', 'arm'):
        sel = [r for r in rows if r['d'] == d and r['region'] == reg]
        if not sel: continue
        print(f'      S{d:+d} {reg:6}: mutual {sum(r["mutual"] for r in sel):2}  one-way {sum(not r["mutual"] for r in sel):2}  '
              f'later residue donates {sum(r["later"] for r in sel):2}/{len(sel)}  pairs: '
              + collections.Counter(f'(e{r["a"] - r["e"]:+d},s{r["b"] - r["s"]:+d})' for r in sel).most_common().__repr__())

# (c) hairpin classes on the crease region
cls = []
for ci, e, s, k, S in HP:
    sel = [r for r in rows if r['ci'] == ci and r['e'] == e and r['s'] == s and r['region'] == 'crease']
    tpf = {(r['a'], r['b']) for r in sel if r['d'] == 1 and r['mutual']}
    ptf = {(r['a'], r['b']) for r in sel if r['d'] == -1 and r['mutual']}
    tp1 = {(r['a'], r['b']) for r in sel if r['d'] == 1 and not r['mutual']}
    pt1 = {(r['a'], r['b']) for r in sel if r['d'] == -1 and not r['mutual']}
    und = {(min(x), max(x)) for x in DIR[ci]}
    cls.append(dict(ci=ci, e=e, s=s, k=k, S=S, w=s - e, tpf=tpf, ptf=ptf, tp1=tp1, pt1=pt1,
                    tp_anchor=(e + 1, s) in und, pt_anchor=(e, s - 1) in und))
tp_only = [c for c in cls if c['tpf'] and not c['ptf']]; pt_only = [c for c in cls if c['ptf'] and not c['tpf']]
both = [c for c in cls if c['tpf'] and c['ptf']]
n1 = len(tp_only) + len(pt_only); p1 = binom_two_sided(len(tp_only), n1) if n1 else float('nan')
print(f'\n  (c) crease facings (mutual pairs, both residues in e..s), by hairpin: TP only {len(tp_only)}, PT only {len(pt_only)}, both {len(both)}')
print(f'      B1  TP {len(tp_only)} : PT {len(pt_only)}, two-sided binomial p = {p1:.3f} against 1:1  -> {"lands" if p1 >= 0.05 else "DEAD END"}')
print(f'      B2  creases holding both facings: {len(both)}  -> {"lands" if not both else "DEAD END"}')
acc = {ci: chains[ci].get('pdb', chains[ci].get('acc')) for ci in DIR}
for c in tp_only + pt_only + both:
    print(f'        {acc[c["ci"]]:6} e={c["e"]:3} s={c["s"]:3} w={c["w"]} S {"even" if c["S"] % 2 == 0 else "odd "}  '
          f'TP facings {sorted((a - c["e"], b - c["s"]) for a, b in c["tpf"])}  PT facings {sorted((a - c["e"], b - c["s"]) for a, b in c["ptf"])}  '
          f'one-way TP {sorted((a - c["e"], b - c["s"]) for a, b in c["tp1"])}  one-way PT {sorted((a - c["e"], b - c["s"]) for a, b in c["pt1"])}')
ow = [r for r in rows if r['region'] == 'crease' and not r['mutual']]
owp, owt = sum(r['d'] == -1 for r in ow), sum(r['d'] == 1 for r in ow)
lat = sum(r['later'] for r in ow)
print(f'      B3  one-way crease bonds: PT {owp}, TP {owt}; later residue donates {lat}/{len(ow)} ({lat/len(ow):.2f})  -> '
      f'{"lands" if owp >= 2 * owt and lat >= 0.9 * len(ow) else "DEAD END"}')
inward = []
for c in cls:
    for (a, b) in c['tpf']:
        if (a, b) != (c['e'] + 1, c['s']): inward.append((c, 'TP', (a, b), c['tp_anchor']))
    for (a, b) in c['ptf']:
        if (a, b) != (c['e'], c['s'] - 1): inward.append((c, 'PT', (a, b), c['pt_anchor']))
print(f'      B4  inward facings (u >= 1) and their anchors: {sum(x[3] for x in inward)}/{len(inward)} anchored  -> '
      f'{"lands" if inward and all(x[3] for x in inward) else "DEAD END" if inward else "no inward facings"}')
for c, kind, (a, b), anc in inward:
    an = (c['e'] + 1, c['s']) if kind == 'TP' else (c['e'], c['s'] - 1)
    st = [x for x in ((an[0], an[1]), (an[1], an[0])) if x in DIR[c['ci']]]
    print(f'        {acc[c["ci"]]:6} e={c["e"]:3} s={c["s"]:3} w={c["w"]} {kind} inward (e{a - c["e"]:+d},s{b - c["s"]:+d})  anchor '
          f'(e{an[0] - c["e"]:+d},s{an[1] - c["s"]:+d}) stored as {["%d->%d" % x for x in st] or "absent"}')
sm, sp = sum(r['d'] == -1 for r in rows), sum(r['d'] == 1 for r in rows)
print(f'      B5  full window census S-1 {sm} against S+1 {sp}  -> {"lands" if sm > sp else "DEAD END"}')

# (d) the crease classes by width and parity (one-way included), for the record
tab = collections.Counter()
for c in cls:
    t = 'TPf' if c['tpf'] else 'TP1' if c['tp1'] else ''
    p = 'PTf' if c['ptf'] else 'PT1' if c['pt1'] else ''
    tab[(c['w'], (t + '+' + p).strip('+') or 'none')] += 1
print('\n  (d) crease classes by width (f = facing, 1 = one-way only):')
for w in range(3, 9):
    print(f'      w={w}: ' + ', '.join(f'{k[1]} {v}' for k, v in sorted(tab.items()) if k[0] == w))
```

`tp_pt_readings.py`

```python
"""§ 197, second reading: § 192's R2 turn (e = 00, e+1 = 10 = P(m), e+2 = 01 = m, s = 11) against the chain-to-ring map; and GPT's slip-rule hash.
Run: python3 -I tp_pt_readings.py"""
import hashlib
R2 = ['00', '10', '01', '11']; N = 4; name = ['e', 'e+1', 'e+2 (= s-1 at w = 3)', 's']
for label, sigma in (('P ', N - 1), ('TP', N), ('PT', N - 2)):
    pairs = sorted({tuple(sorted((a, (sigma - a) % N))) for a in range(N)})
    print(f'  {label} (sum {sigma % N} mod 4): ' + ', '.join(
        (f'{name[a]} faces itself [{R2[a]}]' if a == b else f'{name[a]} <-> {name[b]} [{R2[a]}, {R2[b]}]') for a, b in pairs))
RULE = ('NEXUS slip/readback v1; ring address a in Z_2^n, P(a)=N-1-a, T(a)=a+1; '
        'S+1 pairs on sum N => TP=T o P, fixed {0,N/2}; '
        'S-1 pairs on sum N-2 => PT=P o T, fixed {N/2-1,N-1}; '
        'no intrinsic sign multiplicity predicted by two conjugate reflections; '
        'readback: original 188 nearest N to O detector, 193 emitted bonds v2, '
        'only D\\E in each hairpin window, classify stored i+j-S in {+1,-1}, '
        'one row per stored slip; source hash and all failures reported.')
print('  GPT slip rule SHA-256', hashlib.sha256(RULE.encode()).hexdigest())
```

`tp_pt_check.py`

```python
"""§ 197, post hoc (after the sealed run): the anchors' directions and the crease row's slots.
Run: python3 -I tp_pt_check.py <ecoli_chains.json>"""
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
tab = collections.Counter()
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    D = closures(ent)
    for e, s, k, S in hairpins(D, L):
        pt = ((s - 1, e) in D, (e, s - 1) in D); tp = ((s, e + 1) in D, (e + 1, s) in D)
        row = ((e, s) in D, (s, e) in D)
        if s - e < 4: tab['w3'] += 1; continue
        if pt[0] or pt[1]:
            tab[('PT anchor', 'later s-1->e' if pt[0] else '', 'earlier e->s-1' if pt[1] else '', 'e->s' if row[0] else 'no e->s', 's->e' if row[1] else 'no s->e')] += 1
        if tp[0] or tp[1]:
            tab[('TP anchor', 'later s->e+1' if tp[0] else '', 'earlier e+1->s' if tp[1] else '', 'e->s' if row[0] else 'no e->s', 's->e' if row[1] else 'no s->e')] += 1
        if not (pt[0] or pt[1] or tp[0] or tp[1]):
            tab[('no anchor', 'e->s' if row[0] else 'no e->s', 's->e' if row[1] else 'no s->e')] += 1
for key, v in sorted(tab.items(), key=lambda kv: str(kv[0])): print(f'  {v:3}  {key}')
```

`turn_arrows.py`

```python
"""§ 197, post hoc: every stored bond inside the crease region (both residues in e..s, the crease row excluded),
by its separation |i - j| and its register offset i + j - S, mutual or one-way.
Run: python3 -I turn_arrows.py <ecoli_chains.json>"""
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
one = collections.Counter(); mut = collections.Counter(); lat = collections.Counter()
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    D = closures(ent)
    for e, s, k, S in hairpins(D, L):
        for i, j in D:
            a, b = min(i, j), max(i, j)
            if not (e <= a and b <= s) or (a, b) == (e, s): continue
            key = (b - a, a + b - S)
            if (j, i) in D:
                if i < j: mut[key] += 1          # count each mutual pair once
            else:
                one[key] += 1; lat[key] += int(i > j)
print('  one-way bonds in the crease region, by (separation, register offset): count (later residue donates)')
for key in sorted(one): print(f'    sep {key[0]}, offset {key[1]:+d}: {one[key]:3} ({lat[key]})')
print('  mutual pairs in the crease region, by (separation, register offset):')
for key in sorted(mut): print(f'    sep {key[0]}, offset {key[1]:+d}: {mut[key]:3}')
print(f'  totals: one-way {sum(one.values())} (separation 3 or 4: {sum(v for k, v in one.items() if k[0] in (3, 4))}); '
      f'mutual pairs {sum(mut.values())} (offset +-1: {sum(v for k, v in mut.items() if abs(k[1]) == 1)})')
```

`side197.py`

```python
"""§ 197, side runs: re-execute the two readers handed in this round, unchanged in rule, on the original chain file.
A  GPT's sequence face-coherence reader (rule SHA-256 d98925c9...), Stage A seal, ranks, shuffles, shifts, decoys (its bootstrap not re-run).
B  the side run's parity-balanced shape-channel crease reader (route tokens t = GSPDN, e = TVIFYWH), shuffles and shifts.
Run: python3 -I side197.py <ecoli_chains.json>"""
import collections, hashlib, json, random, sys
import numpy as np

raw = open(sys.argv[1], 'rb').read(); chains = json.loads(raw)
sha = lambda v: hashlib.sha256(v).hexdigest()
print('data raw SHA-256', sha(raw))

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

# ============================================================== A  GPT's face-coherence reader, as written
WET = {'G':0,'A':0,'V':0,'L':0,'I':0,'F':0,'P':0,'C':2,'M':2,'W':2,'S':3,'T':3,'Y':3,'H':3,'K':3,'N':5,'Q':5,'D':5,'E':5,'R':7}
MAX_H = 8
RULE = ('NEXUS196/v1; sequence WET table from Reading Proteins s5 as recorded s195; '
        'candidate width w=3..8; e=(S-w)/2,s=(S+w)/2 integers; full t=0..8; '
        'r_t=(WET[e-t]+WET[s+t])/2; for h=3..8 let Delta_h=mean_even_rows_0..h(r)-mean_odd_rows_0..h(r); '
        'D_h=1440*Delta_h exact integer; Q(S,w)=abs(sum_h D_h) integer in [0,60480]; '
        'Q(S)=max_w Q(S,w), ties smaller w; physical A/B orientation deliberately unknown; '
        'way home: original s188 N-to-nearest-O hairpin detector run only after candidate score seal, observed S=e+s and true ranks; '
        'midrank +-8 among valid candidate centres; chain composition shuffles seed 196 200 reps; '
        'shift +-2,+-4,+-6,+-8 with matching parity; decoy same chain, centre parity, '
        'outside +-16 of every hairpin centre, 25-position 20aa-composition L1 minimum, then centre ascending; '
        'chain block bootstrap seed 196196 2000 reps; no fitted weights, energy, or ring phase.')
def canon(x): return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
print('\nA  RULE SHA-256', sha(RULE.encode()))

def score_sequence(seq):
    v = np.fromiter((WET[a] for a in seq), dtype=np.int64, count=len(seq)); L = len(v); entries = []; best = {}
    for w in range(3, 9):
        e = np.arange(MAX_H, L - w - MAX_H, dtype=np.int64)
        if len(e) == 0: continue
        s = e + w
        rows = np.stack([v[e - t] + v[s + t] for t in range(MAX_H + 1)])
        even = np.zeros(len(e), dtype=np.int64); odd = np.zeros(len(e), dtype=np.int64); ec = oc = 0; ds = []
        for h in range(MAX_H + 1):
            if h % 2 == 0: even += rows[h]; ec += 1
            else: odd += rows[h]; oc += 1
            if h >= 3: ds.append((even * oc - odd * ec) * (1440 // (2 * ec * oc)))
        D = np.stack(ds).T; Q = np.abs(D.sum(axis=1))
        for j in range(len(e)):
            S = int(e[j] * 2 + w); d = tuple(map(int, D[j])); q = int(Q[j]); row = (S, w, q, d); entries.append(row)
            if S not in best or q > best[S][2] or (q == best[S][2] and w < best[S][1]): best[S] = row
    entries.sort(key=lambda z: (z[0], z[1]))
    return entries, best

def rank(S, best):
    win = [(a, best[a][2]) for a in range(S - 8, S + 9) if a in best]
    if S not in best or len(win) < 2: return None
    q = best[S][2]; gt = sum(x > q for _, x in win); eq = sum(x == q for _, x in win); rk = 1 + gt + (eq - 1) / 2
    return (rk, (len(win) - rk) / (len(win) - 1), len(win))

seqs = [''.join(r[1] for r in ent['residues']) for ent in chains]
ledger = []; bests = []; nc = 0
for ci, seq in enumerate(seqs):
    entries, best = score_sequence(seq); bests.append(best)
    ledger.append({'chain': ci, 'sequence_sha256': sha(seq.encode()), 'candidates': entries}); nc += len(entries)
print('A  Stage A rows', nc, 'centres', sum(map(len, bests)), 'score SHA-256', sha(canon({'rule_hash': sha(RULE.encode()), 'score_ledger': ledger})))
del ledger
hp = []
for ci, ent in enumerate(chains):
    if len(ent['residues']) >= 30: hp.extend([(ci, e, s, k, S) for e, s, k, S in hairpins(closures(ent), len(ent['residues']))])
hp.sort(key=lambda a: (a[0], a[4], a[1], a[2]))
hcent = collections.defaultdict(list)
for ci, e, s, k, S in hp: hcent[ci].append(S)
ALPH = 'ACDEFGHIKLMNPQRSTVWY'
def hist25(seq, S):
    c0 = S // 2; lo = max(0, c0 - 12); hi = min(len(seq), c0 + 13); c = collections.Counter(seq[lo:hi]); return tuple(c[a] for a in ALPH)
used_d = collections.defaultdict(set)
def decoy(ci, S):
    tar = hist25(seqs[ci], S); H = hcent[ci]
    cand = [c for c in bests[ci] if c % 2 == S % 2 and all(abs(c - q) > 16 for q in H)]
    if not cand: return None
    uq = [c for c in cand if c not in used_d[ci]]
    if uq: cand = uq
    v = min(cand, key=lambda c: (sum(abs(x - y) for x, y in zip(hist25(seqs[ci], c), tar)), c)); used_d[ci].add(v); return v
res = []
for num, (ci, e, s, k, S) in enumerate(hp, 1):
    r = rank(S, bests[ci]); dS = decoy(ci, S); res.append(dict(num=num, ci=ci, S=S, w=s - e, r=r, dr=rank(dS, bests[ci]) if dS is not None else None,
                                                              wp=bests[ci][S][1] if S in bests[ci] else None))
use = [x for x in res if x['r'] is not None]
print(f'A  true centres {len(use)}/{len(res)} evaluable; first {sum(x["r"][0] == 1 for x in use)}, top 3 {sum(x["r"][0] <= 3 for x in use)}, '
      f'mean advantage {np.mean([x["r"][1] for x in use]):.6f}; width exact {sum(x["wp"] == x["w"] for x in use)}')
rng = np.random.default_rng(196); shr = []; str_ = []
def best_only(seq): return score_sequence(seq)[1]
for rep in range(200):
    sh = {}
    for ci in sorted(set(x['ci'] for x in use)):
        a = np.array(list(seqs[ci]), dtype='U1'); rng.shuffle(a); sh[ci] = best_only(''.join(a))
    sv = {}; tv = {}
    for x in use:
        rr = rank(x['S'], sh[x['ci']])
        if rr: sv[x['num']] = rr[1]
        opts = [q for off in (-8, -6, -4, -2, 2, 4, 6, 8) if (q := x['S'] + off) in bests[x['ci']] and rank(q, bests[x['ci']]) is not None]
        if opts: v = int(rng.choice(opts)); tv[x['num']] = rank(v, bests[x['ci']])[1]
    shr.append(sv); str_.append(tv)
for reps, title in ((shr, 'shuffle'), (str_, 'shifted')):
    keys = sorted(set.intersection(*[set(r) for r in reps]) & {x['num'] for x in use})
    obs = np.mean([x['r'][1] for x in use if x['num'] in keys]); dist = np.array([np.mean([r[i] for i in keys]) for r in reps])
    print(f'A  {title:7} null mean {dist.mean():.6f} sd {dist.std():.6f}  observed {obs:.6f}  P(null >= obs) {(1 + (dist >= obs).sum()) / 201:.5f}')
dec = [x for x in use if x['dr'] is not None]
print(f'A  matched decoys n {len(dec)} mean {np.mean([x["dr"][1] for x in dec]):.6f}')

# ============================================================== B  the side run's parity-balanced shape reader, as written
print('\nB  shape-channel crease reader (parity-balanced), rank_in_window +-8, random.Random(195), 200 reps')
TURN_SET = frozenset('GSPDN'); STRAND_SET = frozenset('TVIFYWH')
def shape_crease_fair(seq, arm_k=4):
    L = len(seq); t_bit = [1.0 if a in TURN_SET else 0.0 for a in seq]; e_bit = [1.0 if a in STRAND_SET else 0.0 for a in seq]; out = []
    for S in range(2 * L - 1):
        if S % 2 == 1: c = (S - 1) // 2; e, s = c - 1, c + 2; loop = (c, c + 1)
        else: c = S // 2; e, s = c - 2, c + 2; loop = (c - 1, c, c + 1)
        if e - arm_k < 0 or s + arm_k >= L: out.append(-999.0); continue
        lm = sum(t_bit[x] for x in loop) / len(loop)
        am = sum((e_bit[e - t] - t_bit[e - t]) + (e_bit[s + t] - t_bit[s + t]) for t in range(arm_k)) / (2 * arm_k)
        out.append(round(lm + am, 6))
    return out
def rank_in_window(S, sc, half=8):
    lo, hi = max(0, S - half), min(len(sc) - 1, S + half); w = sc[lo:hi + 1]; v = sc[S]
    r = 1 + sum(x > v for x in w) + 0.5 * (sum(x == v for x in w) - 1)
    return r, (len(w) - r) / (len(w) - 1)
DIR = {}; HP = []
for ci, ent in enumerate(chains):
    L = len(ent['residues'])
    if L < 30: continue
    DIR[ci] = closures(ent); HP += [(ci,) + h for h in hairpins(DIR[ci], L)]
SEQS = {ci: ''.join(r[1] for r in chains[ci]['residues']) for ci in range(len(chains))}
SC = {ci: shape_crease_fair(SEQS[ci]) for ci in SEQS}
obs = [rank_in_window(S, SC[ci]) for ci, e, s, k, S in HP]
adv = float(np.mean([a for r, a in obs]))
inval = sum(SC[ci][S] == -999.0 for ci, e, s, k, S in HP)
print(f'B  scores SHA-256 {sha(json.dumps([SC[ci] for ci in range(len(chains))], separators=(",", ":")).encode())}')
print(f'B  true S first {sum(r == 1 for r, a in obs)}/143, top 3 {sum(r <= 3 for r, a in obs)}/143, mean advantage {adv:.4f} '
      f'(S even {np.mean([a for (r, a), h in zip(obs, HP) if h[4] % 2 == 0]):.4f}, S odd {np.mean([a for (r, a), h in zip(obs, HP) if h[4] % 2 == 1]):.4f}); '
      f'true centres scored -999 (arm off the chain): {inval}')
rng2 = random.Random(195); used = sorted({h[0] for h in HP}); shf = []; sft = []
for _ in range(200):
    SCs = {}
    for ci in used:
        b = list(SEQS[ci]); rng2.shuffle(b); SCs[ci] = shape_crease_fair(''.join(b))
    shf.append(np.mean([rank_in_window(S, SCs[ci])[1] for ci, e, s, k, S in HP]))
    sft.append(np.mean([rank_in_window(rng2.choice([x for x in range(max(0, S - 8), min(len(SC[ci]), S + 9)) if x != S]), SC[ci])[1]
                        for ci, e, s, k, S in HP]))
shf = np.array(shf); sft = np.array(sft)
print(f'B  shuffle null {shf.mean():.4f} (sd {shf.std():.4f}, P {(1 + (shf >= adv).sum()) / 201:.4f}); '
      f'shifted null {sft.mean():.4f} (sd {sft.std():.4f}, P {(1 + (sft >= adv).sum()) / 201:.4f})')
# the same reader with invalid candidates removed from every window (they rank last by construction)
def rank_valid(S, sc, half=8):
    lo, hi = max(0, S - half), min(len(sc) - 1, S + half); w = [x for x in sc[lo:hi + 1] if x != -999.0]; v = sc[S]
    if v == -999.0 or len(w) < 2: return None
    r = 1 + sum(x > v for x in w) + 0.5 * (sum(x == v for x in w) - 1); return r, (len(w) - r) / (len(w) - 1)
ov = [rank_valid(S, SC[ci]) for ci, e, s, k, S in HP]; ov = [x for x in ov if x]
print(f'B  invalid candidates dropped from the windows: n {len(ov)}, first {sum(r == 1 for r, a in ov)}, top 3 {sum(r <= 3 for r, a in ov)}, '
      f'mean advantage {np.mean([a for r, a in ov]):.4f}')
```

