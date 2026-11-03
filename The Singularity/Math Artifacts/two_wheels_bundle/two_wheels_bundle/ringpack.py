"""ringpack - using the ring of all binary words as an index and as a transform.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.

What the ring gives for free is the partner of every word and the mirror difference of every pair.
So it can (1) halve any table or set that respects the partner, with a collision-free O(n) index at any width,
and (2) remove mirror redundancy from data, at whatever scale the data holds its mirror.
It cannot shorten an arbitrary word: every coordinate here is a bijection on n bits.

Words are MSB-first: x_0 is the most significant bit. All arithmetic is exact (Python ints, numpy int64)."""
import numpy as np

# ----------------------------------------------------------------------------- the pairing
def J(x, n):
    """bit reversal of an n-bit integer"""
    r = 0
    for _ in range(n):
        r = (r << 1) | (x & 1); x >>= 1
    return r

def partner(x, n):
    r = J(x, n)
    return r if r != x else ((1 << n) - 1) ^ x

def canon(x, n):
    return min(x, partner(x, n))

# ----------------------------------------------------------------------------- the closed address (Theorem 1)
def _cdiv(a, b):
    return -((-a) // b)

def rect(h, u, v):
    """#{b < u : J_h(b) < v} as a sum of h ceilings"""
    if u >= 1 << h:
        return v
    s = 0; rho = 0
    for j in range(h):
        uj = (u >> (h - 1 - j)) & 1
        if uj:
            s += _cdiv(v - rho, 1 << (j + 1))
        rho += uj << j
    return s

def delta(p, n):
    """number of reversal pairs the cut at p separates"""
    h = n // 2; H = 1 << h
    if p >= 1 << n:
        return 0
    B = p & (H - 1)
    if n % 2 == 0:
        A = p >> h
        return A * (H - A) + B - 2 * rect(h, B, A) - int(J(A, h) < B)
    b = (p >> h) & 1; A = p >> (h + 1)
    return 2 * A * (H - A) + b * (H - 1 - 2 * A) + B - 2 * rect(h, B, A) - int(J(A, h) < B)

def _palindrome(u, n):
    m = (n + 1) // 2
    return (u << (n - m)) | (J(u, m) if n % 2 == 0 else J(u >> 1, m - 1))

def rank(p, n):
    """number of representatives below p"""
    m = (n + 1) // 2; u = p >> (n - m)
    pi = u + int(_palindrome(u, n) < p)
    return (p - pi + delta(p, n)) // 2 + min(pi, 1 << (m - 1))

def address(x, n):
    """ring address of x (centre swap and partner face included)"""
    N = 1 << n; M = N >> 1; a = canon(x, n); r = rank(a, n)
    pa = M if r == M - 1 else r
    return pa if x == a else N - 1 - pa

# ----------------------------------------------------------------------------- 1. the half that builds itself
def half_index(x, n):
    """collision-free index of the pair {x, P(x)} in [0, 2^(n-1))"""
    return rank(canon(x, n), n)

def half_unindex(r, n):
    """canonical word with half_index r (bisection on the monotone rank)"""
    lo, hi = 0, (1 << n) - 1
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        if rank(mid, n) <= r:
            lo = mid
        else:
            hi = mid - 1
    return lo

class HalfTable:
    """A table over all n-bit words whose values respect the partner: T[x] == T[P(x)] (symmetric)
    or T[x] == -T[P(x)] (antisymmetric). Stores 2^(n-1) entries, indexed by half_index."""
    def __init__(self, n, antisymmetric=False, dtype=np.int64):
        self.n = n; self.anti = antisymmetric
        self.v = np.zeros(1 << (n - 1), dtype=dtype)
    def _sign(self, x):
        return -1 if (self.anti and x != canon(x, self.n)) else 1
    def __setitem__(self, x, val):
        self.v[half_index(x, self.n)] = self._sign(x) * val
    def __getitem__(self, x):
        return self._sign(x) * self.v[half_index(x, self.n)]

# ----------------------------------------------------------------------------- 2. word coordinates (w <= 16, tables)
def _revarr(w, n):
    r = np.zeros_like(w)
    for b in range(n):
        r |= ((w >> b) & 1) << (n - 1 - b)
    return r

def ring_table(n):
    N = 1 << n; w = np.arange(N, dtype=np.int64); Jw = _revarr(w, n)
    Pw = np.where(Jw == w, (N - 1) ^ w, Jw)
    reps = w[w < Pw]; R = np.concatenate([reps, Pw[reps][::-1]])
    if n > 1:
        R[N // 2 - 1], R[N // 2] = R[N // 2], R[N // 2 - 1]
    loc = np.empty(N, dtype=np.int64); loc[R] = np.arange(N)
    return R, loc            # R: address -> word, loc: word -> address

def lift_table(n):
    """word -> (values of the h pairs, then their differences); middle bit last at odd n"""
    N = 1 << n; h = n // 2; w = np.arange(N, dtype=np.int64)
    bit = lambda j: (w >> (n - 1 - j)) & 1
    v = np.zeros(N, dtype=np.int64); d = np.zeros(N, dtype=np.int64)
    for j in range(h):
        v = (v << 1) | bit(j); d = (d << 1) | (bit(j) ^ bit(n - 1 - j))
    code = (v << h) | d
    if n % 2:
        code = (code << 1) | bit(h)
    return code

def _route_bits(x, n):
    """E/G route code (n-1 route bits then the side bit) as an n-bit integer"""
    s = format(x, f'0{n}b')
    Ps = lambda w: w[::-1] if w[::-1] != w else ''.join('1' if c == '0' else '0' for c in w)
    cn = lambda w: min(w, Ps(w))
    Cs = lambda w: ''.join('1' if c == '0' else '0' for c in w)
    ins = lambda y, m: y[:len(y) // 2] + m + y[len(y) // 2:]
    a = cn(s); e = int(s != a); back = []
    while len(a) > 1:
        L = len(a)
        if L == 2:
            back.append(a[1]); a = '0'
        elif L % 2:
            hh = L // 2; back.append(a[hh]); a = a[:hh] + a[hh + 1:]
        else:
            f, c, u = a[0], a[-1], a[1:-1]
            if f != c:
                back.append('1'); a = ins(cn(u), '1' if u != cn(u) else '0')
            elif f == '1':
                back.append('0'); a = ins(u, '1')
            elif u == u[::-1] and u[0] == '1':
                back.append('0'); a = ins(Cs(u), '1')
            else:
                back.append('0'); a = ins(u, '0')
    return int(''.join(reversed(back)) + str(e), 2)

def route_table(n):
    return np.array([_route_bits(x, n) for x in range(1 << n)], dtype=np.int64)

def inverse(table):
    inv = np.empty_like(table); inv[table] = np.arange(len(table)); return inv

# ----------------------------------------------------------------------------- 3. mirror lift at the data's own scale
def block_lift(blocks):
    """rows of int16 samples -> (first half and centre, then mirror differences mod 2^16); exact inverse below"""
    b = blocks.astype(np.int64); L = b.shape[1]; k = L // 2
    first = b[:, :L - k]                                   # includes the centre at odd L
    diff = (b[:, :k] - b[:, ::-1][:, :k]) & 0xFFFF          # h[j] - h[L-1-j], wrapped
    return first, diff

def block_unlift(first, diff, L):
    k = L // 2; out = np.zeros((first.shape[0], L), dtype=np.int64)
    out[:, :L - k] = first
    tail = ((first[:, :k] - diff) + 0x8000) % 0x10000 - 0x8000   # back to signed 16-bit
    out[:, L - k:] = tail[:, ::-1]
    return out

def triangle_lift(C):
    """symmetric-in-structure matrix -> upper triangle (with diagonal) and lower-minus-upper differences mod 2^16"""
    C = C.astype(np.int64); iu = np.triu_indices(C.shape[0]); il = np.triu_indices(C.shape[0], 1)
    upper = C[iu]; diff = (C.T[il] - C[il]) & 0xFFFF
    return upper, diff

def triangle_unlift(upper, diff, n):
    C = np.zeros((n, n), dtype=np.int64); iu = np.triu_indices(n); il = np.triu_indices(n, 1)
    C[iu] = upper
    low = ((C[il] + diff) + 0x8000) % 0x10000 - 0x8000
    C.T[il] = low
    return C
