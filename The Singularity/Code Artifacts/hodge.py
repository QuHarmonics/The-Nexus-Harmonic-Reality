"""Invariant Hodge decomposition of arena 1-forms.

C0 --d0--> C1 --d1--> C2      (C2 = 2-cells; predicate is the open parameter 7)

  C1 = im d0  (+)  H1  (+)  im d1^T
  H1 = ker d1 (^) ker d0^T

Reported SEPARATELY, never inferred from one another:
  dim C1, dim im d0, rank d1, dim H1, and the Aut-invariant dimension of each.
All ranks use an ABSOLUTE singular-value tolerance (the locked correction).
"""
import itertools, numpy as np
from collections import defaultdict

ATOL = 1e-9


def rank_abs(M, atol=ATOL):
    if M.size == 0 or min(M.shape) == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > atol).sum())


def colspace(M, atol=ATOL):
    if M.size == 0 or min(M.shape) == 0:
        return np.zeros((M.shape[0], 0))
    U, s, _ = np.linalg.svd(M, full_matrices=False)
    return U[:, s > atol]


def nullspace(M, n, atol=ATOL):
    if M.size == 0 or min(M.shape) == 0:
        return np.eye(n)
    _, s, Vt = np.linalg.svd(M, full_matrices=True)
    s_full = np.zeros(Vt.shape[0]); s_full[:len(s)] = s
    return Vt[s_full <= atol].T


# ---------------- arena ----------------
def arena(base_adj, N, K):
    verts = sorted((frozenset(s) for s in itertools.combinations(range(N), K)),
                   key=lambda s: sorted(s))
    vi = {v: i for i, v in enumerate(verts)}
    und = set()
    nbr = defaultdict(set)
    for x in verts:
        for u in x:
            for w in base_adj[u]:
                if w not in x:
                    y = frozenset((x - {u}) | {w})
                    und.add(frozenset((x, y))); nbr[x].add(y); nbr[y].add(x)
    edges = sorted((tuple(sorted(e, key=lambda s: sorted(s))) for e in und),
                   key=lambda p: (sorted(p[0]), sorted(p[1])))
    ei = {}
    for i, (a, b) in enumerate(edges):
        ei[(a, b)] = (i, 1); ei[(b, a)] = (i, -1)
    return verts, vi, edges, ei, nbr


def cells_disjoint(verts, nbr, base_adj, K):
    """Abrams-Ghrist: two applicable moves with disjoint support commute and close a square."""
    out, seen = set(), set()
    for x in verts:
        moves = [(u, w) for u in x for w in base_adj[u] if w not in x]
        for (u1, w1), (u2, w2) in itertools.combinations(moves, 2):
            if {u1, w1} & {u2, w2}:
                continue
            x1 = frozenset((x - {u1}) | {w1})
            x2 = frozenset((x - {u2}) | {w2})
            x12 = frozenset((x - {u1, u2}) | {w1, w2})
            corners = tuple(sorted([tuple(sorted(v)) for v in (x, x1, x12, x2)]))
            if corners in seen:
                continue
            seen.add(corners)
            out.add((x, x1, x12, x2) if sorted(x1) < sorted(x2) else (x, x2, x12, x1))
    return sorted(out, key=lambda c: [sorted(v) for v in c])


def cells_fourcycle(verts, nbr):
    out = set()
    for x, z in itertools.combinations(verts, 2):
        common = sorted(nbr[x] & nbr[z], key=lambda s: sorted(s))
        for a, b in itertools.combinations(common, 2):
            key = tuple(sorted([tuple(sorted(x)), tuple(sorted(a)), tuple(sorted(z)), tuple(sorted(b))]))
            if key in out:
                continue
            out.add(key)
    res = []
    for key in sorted(out):
        s = [frozenset(k) for k in key]
        # recover a cyclic order
        for perm in itertools.permutations(s[1:]):
            c = [s[0]] + list(perm)
            if all(c[(i + 1) % 4] in nbr[c[i]] for i in range(4)):
                res.append(tuple(c)); break
    return res


def d0_matrix(verts, vi, edges, ei):
    D = np.zeros((len(edges), len(verts)))
    for (a, b) in edges:
        i, _ = ei[(a, b)]
        D[i, vi[b]] += 1; D[i, vi[a]] -= 1
    return D


def d1_matrix(cells, edges, ei):
    D = np.zeros((len(cells), len(edges)))
    for r, c in enumerate(cells):
        for k in range(4):
            i, s = ei[(c[k], c[(k + 1) % 4])]
            D[r, i] += s
    return D


def edge_action(g, edges, ei):
    P = np.zeros((len(edges), len(edges)))
    for (a, b) in edges:
        i, _ = ei[(a, b)]
        ga = frozenset(g[e] for e in a); gb = frozenset(g[e] for e in b)
        j, s = ei[(ga, gb)]
        P[j, i] = s
    return P


def report(name, base_adj, N, K, AUT, predicate):
    verts, vi, edges, ei, nbr = arena(base_adj, N, K)
    cells = cells_disjoint(verts, nbr, base_adj, K) if predicate == "disjoint" \
        else cells_fourcycle(verts, nbr)
    D0 = d0_matrix(verts, vi, edges, ei)
    D1 = d1_matrix(cells, edges, ei)
    nE = len(edges)
    assert rank_abs(D1 @ D0) == 0, "d1 d0 != 0"

    im_d0 = colspace(D0)
    r_d1 = rank_abs(D1)
    H = nullspace(np.vstack([D1, D0.T]), nE)        # ker d1 (^) ker d0^T
    im_delta = colspace(D1.T)

    Pi = sum(edge_action(g, edges, ei) for g in AUT) / len(AUT)
    inv = lambda B: rank_abs(Pi @ B) if B.shape[1] else 0

    print(f"\n### {name}  [2-cell predicate: {predicate}]")
    print(f"    V={len(verts)}  E={nE}  cells={len(cells)}  |Aut|={len(AUT)}  "
          f"beta1={nE - len(verts) + 1}")
    print(f"    dim C^1        = {nE:<5}   invariant = {rank_abs(Pi)}")
    print(f"    dim im d0      = {im_d0.shape[1]:<5}   invariant = {inv(im_d0)}")
    print(f"    rank d1        = {r_d1:<5}   dim im d1^T invariant = {inv(im_delta)}")
    print(f"    dim H^1        = {H.shape[1]:<5}   invariant = {inv(H)}")
    tot = im_d0.shape[1] + H.shape[1] + im_delta.shape[1]
    print(f"    split check    : {im_d0.shape[1]} + {H.shape[1]} + {im_delta.shape[1]} "
          f"= {tot}  (dim C^1 = {nE})  {'ok' if tot == nE else '*** MISMATCH ***'}")
    return H.shape[1], inv(H)


C6 = {v: {(v - 1) % 6, (v + 1) % 6} for v in range(6)}
Q3 = {v: {v ^ (1 << i) for i in range(3)} for v in range(8)}
Z32 = {v: set(range(9)) - {v} for v in range(9)}          # Cayley(Z_3^2, all 8 non-identity) = K9


def aut_cycle(N):
    return [tuple((i + k) % N for i in range(N)) for k in range(N)] + \
           [tuple((k - i) % N for i in range(N)) for k in range(N)]


def aut_hypercube(n):
    V = 1 << n; g = []
    for perm in itertools.permutations(range(n)):
        for mask in range(V):
            g.append(tuple((sum(((v >> i) & 1) << perm[i] for i in range(n))) ^ mask
                           for v in range(V)))
    return g


def agl23():
    """AGL(2,3): affine maps of Z_3^2, order 432. Points indexed 3*a+b."""
    pts = [(a, b) for a in range(3) for b in range(3)]
    idx = {p: i for i, p in enumerate(pts)}
    out = []
    for M in itertools.product(range(3), repeat=4):
        a, b, c, d = M
        if (a * d - b * c) % 3 == 0:
            continue
        for t in pts:
            out.append(tuple(idx[(((a * p[0] + b * p[1]) + t[0]) % 3,
                                  ((c * p[0] + d * p[1]) + t[1]) % 3)] for p in pts))
    return out


for pred in ("disjoint", "four_cycle"):
    report("C6 arena, K=3", C6, 6, 3, aut_cycle(6), pred)
for pred in ("disjoint", "four_cycle"):
    report("Q3 arena (frozen spec), K=3", Q3, 8, 3, aut_hypercube(3), pred)
A = agl23()
print(f"\n|AGL(2,3)| = {len(A)}")
for pred in ("disjoint", "four_cycle"):
    report("Z3^2 arena (deg-8 Cayley = K9), K=3", Z32, 9, 3, A, pred)
