"""Run of seal_wheels.txt (W1-W8). Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.
Usage: python3 -I run_wheels.py <path to nested_ring_beyond_2bit.xlsx>"""
import sys, os, json, time, random, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import wheels as wh

XLSX = sys.argv[1]
T0 = time.time()
out = {}
here = os.path.dirname(os.path.abspath(__file__))
seal = open(os.path.join(here, 'seal_wheels.txt'), 'rb').read()
out['seal'] = hashlib.sha256(seal).hexdigest()
print('seal', out['seal'])


def say(*a):
    print(*a, flush=True)


# ----------------------------------------------------------------------------- vectorized closed forms
def rev_arr(x, k):
    r = np.zeros_like(x)
    y = x.copy()
    for _ in range(k):
        r = (r << 1) | (y & 1)
        y >>= 1
    return r


def cdiv(a, b):
    return -((-a) // b)


def rect_arr(h, u, v):
    s = np.zeros_like(u)
    rho = np.zeros_like(u)
    for j in range(h):
        uj = (u >> (h - 1 - j)) & 1
        s += uj * cdiv(v - rho, 1 << (j + 1))
        rho += uj << j
    return s


def delta_arr(p, n):
    h = n // 2
    H = 1 << h
    B = p & (H - 1)
    if n % 2 == 0:
        A = p >> h
        d = A * (H - A) + B - 2 * rect_arr(h, B, A) - (rev_arr(A & (H - 1), h) < B).astype(np.int64)
    else:
        b = (p >> h) & 1
        A = p >> (h + 1)
        d = 2 * A * (H - A) + b * (H - 1 - 2 * A) + B - 2 * rect_arr(h, B, A) - (rev_arr(A & (H - 1), h) < B).astype(np.int64)
    d = np.where((p <= 0) | (p >= (1 << n)), 0, d)
    return d


def pal_arr(p, n):
    m = (n + 1) // 2
    u = p >> (n - m)
    if n % 2 == 0:
        Bu = (u << (n - m)) | rev_arr(u & ((1 << m) - 1), m)
    else:
        Bu = (u << (n - m)) | rev_arr((u >> 1) & ((1 << (m - 1)) - 1), m - 1)
    pi = u + (Bu < p).astype(np.int64)
    return np.where(p >= (1 << n), 1 << m, pi)


# ----------------------------------------------------------------------------- W1 - W5: one counter through R_L
W = {k: {} for k in ('W1', 'W2', 'W3', 'W5')}
okW1 = okW2 = okW3 = okW5 = True
profiles = {}
for L in range(2, 21):
    N = 1 << L
    M = N // 2
    hp = 1 << ((L + 1) // 2 - 1)
    h = L // 2
    w, Jw, Pw, R, loc = wh.ring_arrays(L)
    is_rep = w < Pw
    # W1: frontier and facing
    reps = w[is_rep]
    frontier = np.arange(len(reps))
    exc = np.flatnonzero(loc[reps] != frontier)
    exc_words = reps[exc]
    largest = reps[-1]
    w1_ok = (len(exc) == 1 and exc_words[0] == largest and loc[largest] == M and R[M - 1] == Pw[largest])
    parts = w[~is_rep]
    facing_ok = bool(np.all(loc[parts] == N - 1 - loc[Pw[parts]]) and np.all(Pw[parts] < parts))
    w1 = bool(w1_ok and facing_ok)
    okW1 &= w1
    W['W1'][L] = dict(frontier_exceptions=int(len(exc)), exception_word=int(exc_words[0]) if len(exc) else None,
                      lands_at=int(loc[largest]), facing_always_filled=facing_ok, ok=w1)
    # W2: hold
    step = np.where(is_rep, 1, -1)
    O = np.concatenate([[0], np.cumsum(step)])
    r = np.concatenate([[0], np.cumsum(is_rep.astype(np.int64))])
    t = np.arange(N + 1, dtype=np.int64)
    pi = pal_arr(t, L)
    closed = delta_arr(t, L) + np.minimum(pi, 2 * hp - pi)
    # direct open-pair count (independent of step accounting): pairs with min < t <= max
    lo = np.minimum(w, Pw)[is_rep]
    hi = np.maximum(w, Pw)[is_rep]
    opens = np.zeros(N + 2, dtype=np.int64)
    np.add.at(opens, lo + 1, 1)
    np.add.at(opens, hi + 1, -1)
    direct = np.cumsum(opens)[:N + 1]
    w2 = bool(np.array_equal(O, 2 * r - t) and np.array_equal(O, closed) and np.array_equal(O, direct))
    okW2 &= w2
    W['W2'][L] = dict(ok=w2, mismatches=int(np.count_nonzero(O != closed)))
    # W3: peak
    mx = int(O.max())
    arg = np.flatnonzero(O == mx)
    w3 = bool(mx == (1 << (L - 2)) + hp and len(arg) == 1 and arg[0] == M)
    okW3 &= w3
    W['W3'][L] = dict(max=mx, predicted=(1 << (L - 2)) + hp, argmax=[int(a) for a in arg[:5]], ok=w3)
    # W5: total and mean hold
    total = int(O[1:].sum())
    pair_sum = int((hi - lo).sum())
    SJ = (N * (N - 1)) // 3 - h * N // 2 if L % 2 == 0 else (N * (N - 2)) // 3 - h * N // 2
    SJ_direct = int(np.abs(Jw - w).sum())
    pred = SJ // 2 + hp * (N // 2 + 1)
    w5 = bool(total == pair_sum == pred and SJ == SJ_direct)
    okW5 &= w5
    mean_over_N = pair_sum / (N // 2) / N
    W['W5'][L] = dict(total=total, pairs=pair_sum, predicted=pred, S_J=SJ, S_J_direct=SJ_direct, mean_hold_over_N=mean_over_N, ok=w5)
    if L <= 20:
        profiles[L] = O
    say(f'L={L:2d} W1 {w1} W2 {w2} W3 {w3} (max {mx} at {list(arg[:3])}) W5 {w5} mean/N {mean_over_N:.6f}')
out['W1'] = dict(ok=okW1, by_L=W['W1'])
out['W2'] = dict(ok=okW2, by_L=W['W2'])
out['W3'] = dict(ok=okW3, by_L=W['W3'])
out['W5'] = dict(ok=okW5, by_L=W['W5'])

# ----------------------------------------------------------------------------- W4 cascade and W4b counter prefix
w4_rows = []
okW4 = True
for L in range(2, 13):
    ns = list(range(L, 2 * L + 5)) + [64, 128]
    row = {}
    for n in ns:
        o = wh.hold(1 << L, n)
        if n <= 20:
            assert o == int(profiles[n][1 << L]), (L, n)
        row[n] = o
        if n == L:
            ok = (o == 0)
        elif n == L + 1:
            ok = (o == (1 << (L - 1)) + (1 << ((L + 2) // 2 - 1)))
            if n <= 2 * L - 2:
                ok = ok and 0 < o < (1 << L)
            if n >= 2 * L - 1:
                ok = ok and o == (1 << L)
        elif n <= 2 * L - 2:
            ok = 0 < o < (1 << L)
        else:
            ok = (o == (1 << L))
        okW4 &= ok
        if not ok:
            say('W4 fail', L, n, o)
    w4_rows.append(dict(L=L, holds={str(k): v for k, v in row.items()}))
    say(f'W4 L={L:2d} t=2^L holds by ring n: ' + ' '.join(f'{n}:{row[n]}' for n in ns))
okW4b = True
w4b = {}
for n in range(4, 65):
    lim = 1 << ((n + 1) // 2)
    if n <= 20:
        _, _, _, R, _ = wh.ring_arrays(n)
        pref = bool(np.array_equal(R[:lim], np.arange(lim)))
        nxt = int(R[lim])
        cov = 'exhaustive'
    else:
        rng = random.Random(n)
        idx = list(range(min(lim, 4096))) + [lim - 1, lim - 2] + [rng.randrange(lim) for _ in range(500)]
        pref = all(wh.word(i, n) == i for i in idx)
        nxt = wh.word(lim, n)
        cov = f'sampled {len(idx)}'
    ok = pref and nxt == lim + 1
    okW4b &= ok
    w4b[n] = dict(prefix_is_counter=pref, next=nxt, ok=ok, coverage=cov)
say('W4b counter prefix ok', okW4b, '| ring 15 next', w4b[15]['next'], 'ring 16 next', w4b[16]['next'])
out['W4'] = dict(ok=okW4, rows=w4_rows)
out['W4b'] = dict(ok=okW4b, by_n=w4b)

# ----------------------------------------------------------------------------- W6 sheets beyond two bits
def tape_bits(L):
    if L <= 16:
        _, _, _, R, _ = wh.ring_arrays(L)
        words = [int(x) for x in R]
    else:
        words = [wh.word(a, L) for a in range(1 << L)]
    s = ''.join(format(x, f'0{L}b') for x in words)
    pal = [wh.J(x, L) == x for x in words]
    return s, words, pal


def sheet_of(L):
    T, words, pal = tape_bits(L)
    S = ''.join('1' if c == '0' else '0' for c in T[::-1])
    C = len(S)
    # palindromic sheet words, read off the sheet itself
    Mk = []
    for k in range(C // L):
        wd = S[k * L:(k + 1) * L]
        Mk.append(wd == wd[::-1])
    mask = ''.join(('1' * L) if m else ('0' * L) for m in Mk)
    return S, mask


okW6 = True
w6 = {}
for L in range(1, 15):
    S, mask = sheet_of(L)
    C = len(S)
    s = [int(c) for c in S]
    mk = [int(c) for c in mask]
    entry = {}
    if L <= 12:
        twist_ok = True
        for Wd in range(1, min(C, 64) + 1):
            full = (1 << Wd) - 1
            # clockwise windows from row 0
            cw = 0
            ccw = 0
            mw = 0
            for k in range(Wd):
                cw = (cw << 1) | s[k % C]
                ccw = (ccw << 1) | s[(C - 1 - k) % C]
                mw = (mw << 1) | mk[k % C]
            for i in range(C):
                if ccw != cw ^ mw:
                    twist_ok = False
                    break
                # step row i -> i+1
                cw = ((cw << 1) & full) | s[(i + Wd) % C]
                mw = ((mw << 1) & full) | mk[(i + Wd) % C]
                ccw = ((ccw << 1) & full) | s[(C - 1 - (i + Wd)) % C]
            if not twist_ok:
                break
        entry['twist_zero_offset_all_widths'] = twist_ok
        okW6 &= twist_ok
    rev = S[::-1]
    d = (S + S).find(rev)
    entry['reversal_is_rotation'] = d >= 0
    entry['rotation'] = d if d >= 0 else None
    if L >= 3:
        okW6 &= (d < 0)
    else:
        okW6 &= (d >= 0)
    if L >= 2:
        off = S.find('1' * L)
        pred = 3 if L == 2 else L * (1 << L) - 2 * L + 1
        entry['first_1L'] = off
        entry['predicted'] = pred
        entry['landing'] = L >= 5
        okW6 &= (off == pred)
    w6[L] = entry
    say(f'W6 L={L:2d} C={C:7d}', entry)
out['W6'] = dict(ok=okW6, by_L=w6)

# ----------------------------------------------------------------------------- W7 workbook rebuild
import openpyxl
wbv = openpyxl.load_workbook(XLSX, data_only=True)
mism = []
cells = 0
agree = {}


def cmp(sheet, coord, cached, rebuilt):
    global cells
    cells += 1
    if isinstance(cached, float) or isinstance(rebuilt, float):
        same = cached is not None and rebuilt is not None and abs(float(cached) - float(rebuilt)) < 1e-9
    else:
        same = (cached == rebuilt) or (str(cached) == str(rebuilt) and cached is not None)
    if not same:
        mism.append((sheet, coord, cached, rebuilt))


def notbits(a):
    return ''.join('1' if c == '0' else '0' for c in a)


for title, L in (('Ring 2', 2), ('Ring 3', 3), ('Ring 4', 4)):
    ws = wbv[title]
    circle = ws['B3'].value
    T, words, pal = tape_bits(L)
    cmp(title, 'B3', circle, T)
    for k in range(1 << L):
        cmp(title, f'B{4 + k}', ws.cell(4 + k, 2).value, circle[k * L:(k + 1) * L])
    base = 4 + (1 << L)                     # 'Reading' row
    S = ''.join('1' if c == '0' else '0' for c in circle[::-1])
    cmp(title, f'B{base + 1}', ws.cell(base + 1, 2).value, S)
    C = len(S)
    cmp(title, f'B{base + 2}', ws.cell(base + 2, 2).value, C)
    off = ws.cell(base + 3, 2).value
    S3 = S * 3
    ok_ag = []
    r = base + 4
    while r <= ws.max_row:
        if ws.cell(r, 1).value == 'Sample size (bits)':
            Wd = ws.cell(r, 2).value
            r0 = r + 2
            vals = []
            for k in range(C):
                rr = r0 + k
                a = S3[k:k + Wd]
                f = S3[(k + off) % C:(k + off) % C + Wd]
                b = int(a, 2)
                g = int(f, 2)
                vals.append((rr, a, b, f, g))
            for k, (rr, a, b, f, g) in enumerate(vals):
                cmp(title, f'A{rr}', ws.cell(rr, 1).value, a)
                cmp(title, f'B{rr}', ws.cell(rr, 2).value, b)
                cmp(title, f'C{rr}', ws.cell(rr, 3).value, format(b, 'X'))
                cmp(title, f'D{rr}', ws.cell(rr, 4).value, format(b, 'o'))
                e = (format(b, 'X') + format(vals[k + 1][2], 'X')) if k % 2 == 0 else None
                cmp(title, f'E{rr}', ws.cell(rr, 5).value, e)
                cmp(title, f'F{rr}', ws.cell(rr, 6).value, f)
                cmp(title, f'G{rr}', ws.cell(rr, 7).value, g)
                cmp(title, f'H{rr}', ws.cell(rr, 8).value, format(g, 'X'))
                cmp(title, f'I{rr}', ws.cell(rr, 9).value, format(g, 'o'))
                jn = (format(g, 'X') + format(vals[(k + 1) % C][4], 'X')) if k % 2 == 1 else None
                cmp(title, f'J{rr}', ws.cell(rr, 10).value, jn)
                ones = a.count('1')
                for col, v in zip('KLMNOPQ', (notbits(a), int(ones == Wd), int(ones != Wd), int(ones > 0), int(ones == 0), ones % 2, int(ones % 2 == 0))):
                    cmp(title, f'{col}{rr}', ws.cell(rr, 'ABCDEFGHIJKLMNOPQ'.index(col) + 1).value, v)
                # true counter-clockwise window from slice C-1-k, read backwards
                tcw = ''.join(S[(C - 1 - k - q) % C] for q in range(Wd))
                ok_ag.append((Wd, tcw == f))
            r = r0 + C
        else:
            r += 1
    byw = {}
    for Wd, ok in ok_ag:
        byw.setdefault(Wd, []).append(ok)
    agree[title] = {str(Wd): sum(v) / len(v) for Wd, v in sorted(byw.items())}

# DI chain
ws = wbv['DI chain']
rings = {}
for L in range(1, 11):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    rings[L] = (Pw, R, loc)


def bits(x, L):
    return format(x, f'0{L}b')


def is_rep(x, L):
    return x < wh.P(x, L)


def depth_root(x, L):
    """continuation: strip F frames from the outside; x a representative"""
    d = 0
    while L >= 3:
        b = x >> (L - 1)
        c = x & 1
        m = (x >> 1) & ((1 << (L - 2)) - 1)
        if b == 1 and c == 1:                  # reversal branch, m a non-palindromic rep
            x, L, d = m, L - 2, d + 1
            continue
        if b == 0 and c == 0 and wh.J(m, L - 2) == m and not is_rep(m, L - 2):
            x, L, d = ((1 << (L - 2)) - 1) ^ m, L - 2, d + 1     # complement branch, a = C(m)
            continue
        break
    return d, x, L


for rr in range(5, ws.max_row + 1):
    L = ws.cell(rr, 1).value
    if L is None:
        continue
    i = ws.cell(rr, 2).value
    Pw, R, loc = rings[L]
    x = int(R[i])
    px = wh.P(x, L)
    rep_ = x < px
    exp = {}
    exp['C'] = bits(x, L)
    exp['D'] = 'rep' if rep_ else 'partner'
    exp['E'] = (1 << L) - 1 - i
    exp['F'] = bits(px, L)
    exp['G'] = 'yes' if wh.J(x, L) == x else 'no'
    exp['H'] = (bits(x, L)[0] + bits(x, L)[-1]) if L >= 2 else None
    exp['I'] = bits(x, L)[1:-1] if L >= 3 else None
    if L <= 2:
        exp['J'], exp['K'] = None, None
    elif not rep_:
        exp['J'], exp['K'] = 'reflection of the facing rep', None
    else:
        b, c = x >> (L - 1), x & 1
        m = (x >> 1) & ((1 << (L - 2)) - 1)
        Pl, Rl, locl = rings[L - 2] if L - 2 >= 1 else (None, None, None)
        if (b, c) == (0, 1):
            exp['J'], exp['K'] = '0.m.1 (any word of ring L-2)', int(locl[m])
        elif (b, c) == (0, 0) and is_rep(m, L - 2):
            exp['J'], exp['K'] = '0.a.0 (rep of ring L-2)', int(locl[m])
        elif (b, c) == (0, 0):
            a = ((1 << (L - 2)) - 1) ^ m
            exp['J'], exp['K'] = 'F complement branch: 0 C(a) 0', int(locl[a])
        else:
            exp['J'], exp['K'] = 'F reversal branch: 1 a 1', int(locl[m])
    exp['L'] = bits(x ^ px, L)
    exp['M'] = bin(x ^ px).count('1')
    rx = x if rep_ else px
    d, root, rw = depth_root(rx, L)
    exp['N'] = d
    exp['O'] = bits(root, rw)
    exp['P'] = rw
    exp['Q'] = i / (1 << L)
    exp['R'] = x / (1 << L)
    tv = x / (1 << L)
    exp['S'] = (tv - tv * tv / 2) if rep_ else None
    exp['T'] = (i / (1 << L) - (tv - tv * tv / 2)) if rep_ else None
    for col, v in exp.items():
        cmp('DI chain', f'{col}{rr}', ws.cell(rr, 'ABCDEFGHIJKLMNOPQRST'.index(col) + 1).value, v)

okW7 = (len(mism) == 0)
say('W7 cells compared', cells, 'mismatches', len(mism))
for m in mism[:20]:
    say('  mismatch', m)
say('workbook G vs true counter-clockwise window, share of rows agreeing by width:')
for title, d in agree.items():
    say(' ', title, ' '.join(f'{k}:{v:.3f}' for k, v in d.items()))
out['W7'] = dict(ok=okW7, cells=cells, mismatches=len(mism), first=[list(map(str, m)) for m in mism[:20]])
out['workbook_G_vs_true_ccw'] = agree

# ----------------------------------------------------------------------------- W8 the path
okW8 = True
w8 = {}
for L in range(1, 17):
    _, _, _, R, _ = wh.ring_arrays(L)
    ok = all(wh.word(a, L) == int(R[a]) for a in range(1 << L))
    w8[L] = ok
    okW8 &= ok
say('W8 exhaustive L=1..16', okW8)
sys.path.insert(0, '/home/claude/compress')
import ringpack as rp
tim = {}
for L in (64, 256, 1024, 4096):
    rng = random.Random(L)
    N = 1 << L
    t1 = time.time()
    ok = True
    for _ in range(2000):
        a = rng.randrange(N)
        x = wh.word(a, L)
        if wh.slot(x, L) != a:
            ok = False
            break
    dt = time.time() - t1
    okW8 &= ok
    w8[L] = ok
    # timing against bisection (ringpack.half_unindex) on representative ranks
    k = 20 if L <= 256 else 5
    rs = [rng.randrange(N // 2) for _ in range(k)]
    t2 = time.time()
    for r_ in rs:
        wh.rep(r_, L)
    path_t = (time.time() - t2) / k
    if L <= 1024:
        t3 = time.time()
        for r_ in rs[:3]:
            assert rp.half_unindex(r_, L) == wh.rep(r_, L)
        bis_t = (time.time() - t3) / 3
    else:
        bis_t = None
    tim[L] = dict(roundtrip_2000_s=dt, path_ms=path_t * 1e3, bisection_ms=None if bis_t is None else bis_t * 1e3)
    say(f'W8 L={L} round trip {ok} ({dt:.1f}s for 2000)  path {path_t*1e3:.3f} ms', '' if bis_t is None else f' bisection {bis_t*1e3:.1f} ms')
out['W8'] = dict(ok=okW8, by_L={str(k): v for k, v in w8.items()}, timing=tim)

out['ledger'] = dict(W1=okW1, W2=okW2, W3=okW3, W4=okW4, W4b=okW4b, W5=okW5, W6=okW6, W7=okW7, W8=okW8)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_wheels.txt'), 'rb').read()).hexdigest()
say('ledger', out['ledger'], 'seconds %.1f' % out['seconds'])
json.dump(out, open(os.path.join(here, 'wheels_results.json'), 'w'), indent=1, default=str)
