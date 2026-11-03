# Register -> counter/adder rung.  States: n-bit words.  Moves: "add 2^i" (with carry, mod 2^n)
# versus register moves "flip bit i" (no carry).  2-cell predicates:
#   none | disjoint-support squares (bits changed by the two moves are disjoint) |
#   all commuting squares | all squares + carry triangles (2^i + 2^i = 2^{i+1})
import numpy as np, itertools
P = 2147483629
def rank_mod(M, p=P):
    M = np.array(M, dtype=np.int64) % p
    if M.size == 0: return 0
    r = 0; rows, cols = M.shape
    for c in range(cols):
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0: continue
        i = r + nz[0]; M[[r, i]] = M[[i, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p-2, p)) % p
        o = np.nonzero(M[:, c])[0]; o = o[o != r]
        if o.size: M[o] = (M[o] - np.outer(M[o, c], M[r])) % p
        r += 1
        if r == rows: break
    return r

def complex_betti(n, kind, predicate):
    N = 2**n; V = list(range(N))
    step = (lambda x, i: (x + 2**i) % N) if kind == 'add' else (lambda x, i: x ^ (1 << i))
    supp = lambda x, i: x ^ step(x, i)
    E = {}
    for x in V:
        for i in range(n):
            e = frozenset((x, step(x, i)))
            if len(e) == 2 and e not in E: E[e] = len(E)
    def edge(a, b): return E[frozenset((a, b))]
    def orient(a, b):  # +1 if stored orientation is min->max
        return 1 if a < b else -1
    cells2 = {}
    for x in V:
        for i, j in itertools.combinations(range(n), 2):
            a, b, c = x, step(x, i), step(step(x, i), j)
            d = step(x, j)
            if step(step(x, j), i) != c or len({a, b, c, d}) < 4: continue
            if predicate in ('disjoint',) and (supp(x, i) & supp(x, j)): continue
            if predicate in ('disjoint', 'squares', 'squares+carry'):
                loop = [a, b, c, d]
                key = frozenset(edge(loop[k], loop[(k+1) % 4]) for k in range(4))
                cells2.setdefault(key, loop)
        if kind == 'add' and predicate == 'squares+carry':
            for i in range(n-1):
                a, b, c = x, step(x, i), step(step(x, i), i)   # c == x + 2^{i+1}
                if len({a, b, c}) < 3: continue
                loop = [a, b, c]
                key = frozenset(edge(loop[k], loop[(k+1) % 3]) for k in range(3))
                cells2.setdefault(key, loop)
    D1 = np.zeros((N, len(E)), dtype=np.int64)
    for e, k in E.items():
        a, b = sorted(e); D1[b, k] += 1; D1[a, k] -= 1
    D2 = np.zeros((len(E), len(cells2)), dtype=np.int64)
    for col, loop in enumerate(cells2.values()):
        L = len(loop)
        for k in range(L):
            a, b = loop[k], loop[(k+1) % L]
            D2[edge(a, b), col] += orient(a, b)
    r1 = rank_mod(D1); r2 = rank_mod(D2) if cells2 else 0
    return N - r1, len(E) - r1 - r2, len(cells2) - r2, len(cells2)

for kind in ('flip', 'add'):
    for n in (3, 4, 5):
        row = []
        preds = ('none', 'disjoint', 'squares') + (('squares+carry',) if kind == 'add' else ())
        for pr in preds:
            b0, b1, b2, c2 = complex_betti(n, kind, pr)
            row.append(f"{pr}: b1={b1} b2={b2} (cells {c2})")
        print(f"{'register (flip)' if kind=='flip' else 'counter (add 2^i)':18s} n={n}  " + " | ".join(row))
