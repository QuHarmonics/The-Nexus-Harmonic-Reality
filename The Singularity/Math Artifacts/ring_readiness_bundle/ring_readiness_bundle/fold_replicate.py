"""Run of seal_folds.txt (U1-U5). Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import numpy as np
import wheels as wh

T0 = time.time()
out = {'seal': hashlib.sha256(open(os.path.join(here, 'seal_folds.txt'), 'rb').read()).hexdigest()}
print('seal', out['seal'])


def hx(bits):
    return format(int(bits, 2), f'0{(len(bits) + 3) // 4}X')


def tape(L):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    return ''.join(format(int(x), f'0{L}b') for x in R), R, Pw, loc


def xor(a, b):
    return ''.join('1' if p != q else '0' for p, q in zip(a, b))


def fold_once(s):
    h = len(s) // 2
    return s[:h], xor(s[:h], s[h:][::-1])


def fold_all(s):
    refs = []
    cur = s
    while len(cur) > 1 and len(cur) % 2 == 0:
        A, D = fold_once(cur)
        refs.append(A)
        cur = D
    return cur, refs


def unfold_all(root, refs):
    cur = root
    chain = [cur]
    for A in reversed(refs):
        cur = A + xor(A, cur)[::-1]
        chain.append(cur)
    return cur, chain


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


# U1, U2
u1 = {}
u2 = {}
ok1 = ok2 = True
peer = {2: ['0', '3', 'C', '27'], 3: ['000', '3F', 'E38', '056767'],
        4: ['0', '0', '0', 'FF', 'F0F0', 'F0000F00', '0123567DBE9AC48F']}
for L in range(1, 17):
    S, R, Pw, loc = tape(L)
    N = 1 << L
    M = N // 2
    A, D = fold_once(S)
    mask = ''.join(('1' * L) if wh.J(int(R[i]), L) == int(R[i]) else ('0' * L) for i in range(M))
    good = (D == mask)
    ok1 &= good
    u1[L] = dict(ok=good, D_hex=hx(D) if L <= 6 else None)
    if L <= 14:
        root, refs = fold_all(S)
        back, chain = unfold_all(root, refs)
        nf = len(refs)
        odd = L >> v2(L)
        # residual after L folds
        cur = S
        for _ in range(L):
            cur = fold_once(cur)[1]
        DL = cur
        ext = (nf == L + v2(L) and len(root) == odd and (L < 2 or set(root) <= {'0'}) and
               ((L >= 3 and DL == '0' * L) or (L == 2 and DL == '11') or L == 1))
        chain_hex = [hx(c) for c in chain]
        peer_ok = (L not in peer) or chain_hex == peer[L]
        good2 = (back == S) and ext and peer_ok
        ok2 &= good2
        u2[L] = dict(ok=good2, inverse=back == S, folds=nf, predicted_folds=L + v2(L), terminal=root if len(root) <= 16 else root[:16] + '…',
                     D_L=DL if len(DL) <= 16 else DL[:16], chain_hex=chain_hex if L <= 4 else None, peer_match=peer_ok)
    print('U1/U2 L=%2d' % L, u1[L], u2.get(L))
out['U1'] = dict(ok=ok1, by_L=u1)
out['U2'] = dict(ok=ok2, by_L=u2)

# U3
ok3 = True
for L in range(1, 17):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    N = 1 << L
    T = np.empty(N, dtype=np.int64)
    T[R] = R[(np.arange(N) + 1) % N]
    Tinv = np.empty(N, dtype=np.int64)
    Tinv[T] = np.arange(N)
    x = np.arange(N)
    cyc = x.copy()
    # T is one N-cycle: following it from 0 visits every word once
    seen = np.zeros(N, dtype=bool)
    cur = 0
    for _ in range(N):
        seen[cur] = True
        cur = T[cur]
    good = bool(seen.all() and cur == 0 and np.array_equal(Pw[Pw], x) and np.array_equal(Pw[T[Pw]], Tinv))
    ok3 &= good
print('U3 dihedral', ok3)
out['U3'] = dict(ok=ok3)


# U4 ANF degrees
def anf_degree(f, L):
    a = f.astype(np.uint8).copy()
    for i in range(L):
        a = a.reshape(-1, 2, 1 << i)
        a[:, 1, :] ^= a[:, 0, :]
        a = a.reshape(-1)
    idx = np.flatnonzero(a)
    if len(idx) == 0:
        return -1
    pc = np.zeros(len(idx), dtype=np.int64)
    y = idx.copy()
    while np.any(y):
        pc += y & 1
        y >>= 1
    return int(pc.max())


def map_degree(F, L):
    return max(anf_degree((F >> b) & 1, L) for b in range(L))


u4 = {}
ok4 = True
for L in range(2, 17):
    _, _, Pw, R, loc = wh.ring_arrays(L)
    N = 1 << L
    dP = map_degree(Pw, L)
    rec = dict(partner=dP, partner_pred=L // 2)
    good = (dP == L // 2)
    if L <= 12:
        T = np.empty(N, dtype=np.int64)
        T[R] = R[(np.arange(N) + 1) % N]
        Tinv = np.empty(N, dtype=np.int64)
        Tinv[T] = np.arange(N)
        dT = map_degree(T, L)
        dTi = map_degree(Tinv, L)
        rec.update(forward=dT, inverse=dTi, pred=L - 1)
        good = good and dT == L - 1 and dTi == L - 1
        if L == 3:
            # peer's T_3 with (a,b,c) = (MSB, middle, LSB)
            def peerT3(x):
                a, b, c = (x >> 2) & 1, (x >> 1) & 1, x & 1
                return ((a ^ b) << 2) | ((a ^ b ^ c ^ (a & b)) << 1) | (1 ^ b ^ c ^ (a & b))
            rec['peer_T3_match'] = all(peerT3(x) == int(T[x]) for x in range(8))
            good = good and rec['peer_T3_match']
    rec['ok'] = good
    ok4 &= good
    u4[L] = rec
    print('U4 L=%2d' % L, rec)
out['U4'] = dict(ok=ok4, by_L=u4)

# U5 frames
u5 = {}
ok5 = True
for L in range(2, 17):
    S, R, Pw, loc = tape(L)
    N = 1 << L
    C = len(S)
    SS = S + S
    counts = []
    for f in range(L):
        ws = {SS[i * L + f:i * L + f + L] for i in range(N)}
        counts.append(len(ws))
    comp = [c == N for c in counts]
    frames_ok = comp[0] and comp[1] and (L < 3 or not any(comp[2:]))
    top = (R >> (L - 1)) & 1
    nxt = np.roll(R, -1)
    g = (top != ((nxt >> (L - 1)) & 1))
    change = set(int(v) for v in R[g])
    pred = None
    owner_ok = True
    if L >= 4:
        a_set = [a for a in range(1 << (L - 2)) if a < wh.J(a, L - 2)]          # non-palindromic representatives
        pred = {(1 << (L - 1)) - 1, (1 << L) - 1}
        for a in a_set:
            ja = wh.J(a, L - 2)
            pred.add(ja << 1)
            pred.add((1 << (L - 1)) | (ja << 1))
        owner_ok = (change == pred)
    rot = lambda y: ((y << 1) & (N - 1)) | (y >> (L - 1))
    f1 = [int(SS[i * L + 1:i * L + 1 + L], 2) for i in range(N)]
    form_ok = all(f1[i] == rot(int(R[i]) ^ (int(g[i]) << (L - 1))) for i in range(N))
    closed = all((c ^ (1 << (L - 1))) in change for c in change)
    good = frames_ok and owner_ok and form_ok and closed
    ok5 &= good
    u5[L] = dict(ok=good, distinct_by_frame=counts, change_words=len(change), owner_match=owner_ok, frame1_form=form_ok, closed_under_top_flip=closed)
    print('U5 L=%2d' % L, u5[L])
out['U5'] = dict(ok=ok5, by_L=u5)
out['ledger'] = dict(U1=ok1, U2=ok2, U3=ok3, U4=ok4, U5=ok5)
out['seconds'] = time.time() - T0
out['seal_after'] = hashlib.sha256(open(os.path.join(here, 'seal_folds.txt'), 'rb').read()).hexdigest()
print('ledger', out['ledger'], 'seconds %.1f' % out['seconds'])
json.dump(out, open(os.path.join(here, 'fold_results.json'), 'w'), indent=1, default=str)
