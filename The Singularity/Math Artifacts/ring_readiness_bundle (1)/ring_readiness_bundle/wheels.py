"""wheels - the ring compiled the instant a word exists.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.

Two wheels. The counter (the wheel below) runs every value once; the ring (the wheel above) has already assigned
every value a slot. Nothing is searched in either direction:
    slot(x, L)  word -> address   closed rank (Delta digit sum + palindrome count), O(L)
    word(a, L)  address -> word   the path: one integer square root for the front half, one O(1) count per back bit
    N - 1 - a   the partner's slot: no computation at all
The hold (assigned, not yet filled) after the counter has run 0..t-1 is O(t) = 2 r(t) - t = Delta(t) + tent(pi(t)).
Words are MSB-first integers. Exact integer arithmetic throughout (Python ints)."""
from math import isqrt


def J(x, n):
    """bit reversal of an n-bit integer"""
    if n <= 0:
        return 0
    return int(format(x, f'0{n}b')[::-1], 2)


def P(x, n):
    r = J(x, n)
    return r if r != x else ((1 << n) - 1) ^ x


def canon(x, n):
    return min(x, P(x, n))


def _cdiv(a, b):
    return -((-a) // b)


def rect(h, u, v):
    """#{b < u : J_h(b) < v} as a sum of h ceilings (§7)"""
    if u >= 1 << h:
        return v
    s = 0
    rho = 0
    for j in range(h):
        uj = (u >> (h - 1 - j)) & 1
        if uj:
            s += _cdiv(v - rho, 1 << (j + 1))
        rho += uj << j
    return s


def delta(p, n):
    """reversal pairs separated by the cut at p: #{x < p <= J(x)} (§7 closed form)"""
    if p <= 0 or p >= 1 << n:
        return 0
    h = n // 2
    H = 1 << h
    B = p & (H - 1)
    if n % 2 == 0:
        A = p >> h
        return A * (H - A) + B - 2 * rect(h, B, A) - int(J(A, h) < B)
    b = (p >> h) & 1
    A = p >> (h + 1)
    return 2 * A * (H - A) + b * (H - 1 - 2 * A) + B - 2 * rect(h, B, A) - int(J(A, h) < B)


def _palindrome(u, n):
    m = (n + 1) // 2
    return (u << (n - m)) | (J(u, m) if n % 2 == 0 else J(u >> 1, m - 1))


def pal_count(p, n):
    """#{palindromes < p}, 0 <= p <= 2^n"""
    m = (n + 1) // 2
    if p >= 1 << n:
        return 1 << m
    u = p >> (n - m)
    return u + int(_palindrome(u, n) < p)


def rank(p, n):
    """#{representatives < p}, 0 <= p <= 2^n (corrected rank, §10)"""
    m = (n + 1) // 2
    pi = pal_count(p, n)
    return (p - pi + delta(p, n)) // 2 + min(pi, 1 << (m - 1))


def hold(t, n):
    """pairs with exactly one member among 0..t-1"""
    hp = 1 << ((n + 1) // 2 - 1)
    pi = pal_count(t, n)
    return delta(t, n) + min(pi, 2 * hp - pi)


def slot(x, n):
    """ring address of word x (centre swap and partner face included)"""
    if n == 1:
        return x
    N = 1 << n
    M = N >> 1
    c = canon(x, n)
    r = rank(c, n)
    pa = M if r == M - 1 else r
    return pa if x == c else N - 1 - pa


# ----------------------------------------------------------------------------- the path: address -> word
def _Q(f, H):
    """representatives in front-half columns < f (one sheet)"""
    return f * H - f * (f - 1) // 2 - max(0, f - H // 2)


def _theta(f, H):
    return f + (1 if 2 * f >= H else 0)


def _column(y, H):
    """largest f in [0, H-1] with _Q(f) <= y, from the quadratic (one isqrt) and an O(1) correction"""
    if y >= _Q(H // 2, H):
        # Q(f) = f(2H - 1 - f)/2 + H/2  ->  f^2 - (2H-1) f + (2y - H) >= 0, smaller root
        b = 2 * H - 1
        disc = b * b - 4 * (2 * y - H)
    else:
        # Q(f) = f(2H + 1 - f)/2  ->  f^2 - (2H+1) f + 2y >= 0, smaller root
        b = 2 * H + 1
        disc = b * b - 8 * y
    f = (b - isqrt(max(disc, 0))) // 2
    f = max(0, min(f, H - 1))
    while f + 1 <= H - 1 and _Q(f + 1, H) <= y:
        f += 1
    while f > 0 and _Q(f, H) > y:
        f -= 1
    return f


def _back(s, theta, h):
    """the s-th (0-based, increasing) h-bit g with J_h(g) >= theta, one count per bit"""
    p = 0
    a = 0
    for j in range(h):
        free = h - j - 1
        lim = 1 << free
        need = _cdiv(theta - a, 1 << (j + 1))          # y >= need, y over the free bits reversed
        count0 = lim - min(max(need, 0), lim)
        if s < count0:
            p = p << 1
        else:
            s -= count0
            p = (p << 1) | 1
            a += 1 << j
    return p


def rep(r, n):
    """the representative of rank r (0 <= r < 2^(n-1)): no bisection"""
    h = n // 2
    H = 1 << h
    if n % 2 == 0:
        f = _column(r, H)
        s = r - _Q(f, H)
        th = _theta(f, H)
        return f * H + _back(s, th, h)
    f = _column(r // 2, H)
    while f + 1 <= H - 1 and 2 * _Q(f + 1, H) <= r:
        f += 1
    while f > 0 and 2 * _Q(f, H) > r:
        f -= 1
    s = r - 2 * _Q(f, H)
    th = _theta(f, H)
    c = H - th
    mid = 1 if s >= c else 0
    s -= mid * c
    return (f << (h + 1)) | (mid << h) | _back(s, th, h)


def word(a, n):
    """the word at ring address a"""
    if n == 1:
        return a
    N = 1 << n
    M = N >> 1
    if a < M - 1:
        return rep(a, n)
    if a == M - 1:
        return P(rep(M - 1, n), n)
    if a == M:
        return rep(M - 1, n)
    return P(rep(N - 1 - a, n), n)


# ----------------------------------------------------------------------------- materialized rings (checks only)
def ring_arrays(n):
    import numpy as np
    N = 1 << n
    w = np.arange(N, dtype=np.int64)
    r = np.zeros_like(w)
    x = w.copy()
    for _ in range(n):
        r = (r << 1) | (x & 1)
        x >>= 1
    Pw = np.where(r == w, (N - 1) ^ w, r)
    reps = w[w < Pw]
    R = np.concatenate([reps, Pw[reps][::-1]])
    if n > 1:
        R[N // 2 - 1], R[N // 2] = R[N // 2], R[N // 2 - 1]
    loc = np.empty(N, dtype=np.int64)
    loc[R] = np.arange(N)
    return w, r, Pw, R, loc
