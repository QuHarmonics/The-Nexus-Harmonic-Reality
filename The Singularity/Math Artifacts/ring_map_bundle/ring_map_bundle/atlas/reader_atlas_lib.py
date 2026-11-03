"""Run of seal_readers.txt (RA1-RA6): the exact best reading order for each thing the ring computes.
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828."""
import sys, os, json, time, hashlib, itertools
from math import factorial
from fractions import Fraction
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'wheels'))
import numpy as np
import wheels as wh

T0 = time.time()
NMAX = int(os.environ.get('NMAX', '16'))


# ----------------------------------------------------------------------------- not-ready counts for every arrived set
def fold_counts(V, n, masks):
    """V: uint64 truth table (bit-packed outputs) indexed by the input word. For every arrived set S (bit i = position
    i arrived) and every output group (mask), the number of not-ready (word, output bit) pairs and of words with any
    output bit of the group not ready. Folding the table along each unarrived position: 3^n work."""
    N = 1 << n
    full = N - 1
    G = len(masks)
    perbit = np.zeros((G, N), np.int64)
    anyc = np.zeros((G, N), np.int64)
    ms = [np.uint64(m) for m in masks]

    def rec(val, und, U, k, start):
        S = full ^ U
        mult = 1 << k
        for gi, m in enumerate(ms):
            um = und & m
            perbit[gi, S] = int(np.bitwise_count(um).sum()) * mult
            anyc[gi, S] = int(np.count_nonzero(um)) * mult
        for b in range(start, n):
            cb = b - k
            v = val.reshape(-1, 2, 1 << cb)
            w = und.reshape(-1, 2, 1 << cb)
            v0 = v[:, 0, :]
            nu = w[:, 0, :] | w[:, 1, :] | (v0 ^ v[:, 1, :])
            rec(np.ascontiguousarray(v0).reshape(-1), np.ascontiguousarray(nu).reshape(-1), U | (1 << b), k + 1, b + 1)

    rec(V.astype(np.uint64), np.zeros(N, np.uint64), 0, 0, 0)
    return perbit, anyc


# ----------------------------------------------------------------------------- exact optimum over all n! orders
def dp(u, n):
    N = 1 << n
    S_all = np.arange(N, dtype=np.int64)
    pc = np.bitwise_count(S_all.astype(np.uint64)).astype(np.int64)
    f = np.zeros(N, np.int64)
    cnt = np.zeros(N, np.int64)
    cnt[N - 1] = 1
    BIG = np.iinfo(np.int64).max // 4
    for k in range(n - 1, -1, -1):
        S = S_all[pc == k]
        cands = []
        for b in range(n):
            T = S | (1 << b)
            has = (S >> b) & 1
            cands.append(np.where(has == 1, BIG, f[T]))
        C = np.stack(cands)
        best = C.min(axis=0)
        c = np.zeros(len(S), np.int64)
        for b in range(n):
            T = S | (1 << b)
            c += np.where(C[b] == best, cnt[T], 0)
        f[S] = u[S] + best
        cnt[S] = c
    return f, cnt


def optimal_orders(n, u, f, limit=5000):
    res = []
    stack = [(0, ())]
    while stack and len(res) < limit:
        S, seq = stack.pop()
        if S == (1 << n) - 1:
            res.append(seq)
            continue
        need = f[S] - u[S]
        for b in range(n - 1, -1, -1):
            if not (S >> b) & 1 and f[S | (1 << b)] == need:
                stack.append((S | (1 << b), seq + (b,)))
    return res


def restricted_count(n, u, f, allowed):
    """number of optimal orders whose every move is allowed(S, b)"""
    from functools import lru_cache
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def g(S):
        if S == full:
            return 1
        need = f[S] - u[S]
        t = 0
        for b in range(n):
            if not (S >> b) & 1 and f[S | (1 << b)] == need and allowed(S, b):
                t += g(S | (1 << b))
        return t
    return g(0)


def cost(order, u):
    S = 0
    c = 0
    for b in order:
        c += int(u[S])
        S |= 1 << b
    return c


def outside_in_variants(n):
    h = n // 2
    vs = set()
    for flips in itertools.product((0, 1), repeat=h):
        seq = []
        for j, fl in enumerate(flips):
            a, b = n - 1 - j, j
            seq += [b, a] if fl else [a, b]
        if n % 2:
            seq.append(h)
        vs.add(tuple(seq))
    return vs


def ref_orders(n):
    h = n // 2
    oi = []
    for j in range(h):
        oi += [n - 1 - j, j]
    if n % 2:
        oi.append(h)
    co = [h] if n % 2 else []
    for j in range(h - 1, -1, -1):
        co += [n - 1 - j, j]
    k = h - 1 if n % 2 else h - 2
    tw = []
    for j in range(max(k, 0)):
        tw += [n - 1 - j, j]
    core = sorted(set(range(n)) - set(tw), reverse=True)
    return {'MSB': tuple(range(n - 1, -1, -1)), 'LSB': tuple(range(n)), 'outside_in': tuple(oi),
            'centre_out': tuple(co), 'two_wheel_by_value': tuple(tw + core)}


def J_arr(x, n):
    r = np.zeros_like(x)
    y = x.copy()
    for _ in range(n):
        r = (r << 1) | (y & 1)
        y >>= 1
    return r


def bits_into(V, arr, off, width):
    for b in range(width):
        V |= (((arr >> b) & 1).astype(np.uint64)) << np.uint64(off + b)
    return off + width


