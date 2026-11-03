# Induced map H^q(C^G) -> H^q(C): which classes a symmetry-invariant reader reports are carried by the object (image)
# and which exist only in the reader (kernel). char-0 proxy vs F2.
import itertools, numpy as np, networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

P = 2147483629  # large prime for rational-rank proxy

def rank_mod(M, p):
    M = np.array(M, dtype=np.int64) % p
    if M.size == 0: return 0
    r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = np.nonzero(M[r:, c])[0]
        if piv.size == 0: continue
        i = r + piv[0]
        if i != r: M[[r, i]] = M[[i, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        if nz.size:
            f = M[nz, c][:, None]
            M[nz] = (M[nz] - (f * M[r][None, :]) % p) % p
        r += 1
        if r == rows: break
    return r

def rank_f2(M):
    M = (np.array(M, dtype=np.int64) % 2).astype(bool)
    if M.size == 0: return 0
    r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = np.nonzero(M[r:, c])[0]
        if piv.size == 0: continue
        i = r + piv[0]
        if i != r: M[[r, i]] = M[[i, r]]
        nz = np.nonzero(M[:, c])[0]; nz = nz[nz != r]
        if nz.size: M[nz] ^= M[r]
        r += 1
        if r == rows: break
    return r

def cells(X, K, qmax=3):
    V = sorted(X.nodes()); E = sorted(tuple(sorted(e)) for e in X.edges())
    C = {}
    for q in range(0, qmax + 1):
        lst = []
        for es in itertools.combinations(E, q):
            used = set(v for e in es for v in e)
            if len(used) != 2 * q: continue          # pairwise vertex-disjoint
            if K - q < 0: continue
            rest_pool = [v for v in V if v not in used]
            for R in itertools.combinations(rest_pool, K - q):
                lst.append((es, frozenset(R)))
        C[q] = lst
    return C

def boundary(Cq, Cqm1):
    idx = {c: i for i, c in enumerate(Cqm1)}
    D = np.zeros((len(Cqm1), len(Cq)), dtype=np.int64)
    for j, (es, R) in enumerate(Cq):
        for i, (u, v) in enumerate(es):
            s = (-1) ** i
            others = es[:i] + es[i + 1:]
            D[idx[(others, R | {v})], j] += s
            D[idx[(others, R | {u})], j] -= s
    return D

def act(g, cell):
    es, R = cell; sign = 1; new = []
    for (u, v) in es:
        a, b = g[u], g[v]
        if a > b: a, b = b, a; sign = -sign
        new.append((a, b))
    order = sorted(range(len(new)), key=lambda k: new[k])
    # sign of permutation
    perm = order[:]; vis = [False]*len(perm)
    for i in range(len(perm)):
        if not vis[i]:
            j = i; L = 0
            while not vis[j]: vis[j] = True; j = perm[j]; L += 1
            if L % 2 == 0: sign = -sign
    return (tuple(new[k] for k in order), frozenset(g[v] for v in R)), sign

def automorphisms(X):
    return list(GraphMatcher(X, X).isomorphisms_iter())

def invariant_basis(Cq, G):
    idx = {c: i for i, c in enumerate(Cq)}
    seen = set(); B = []
    for c in Cq:
        if c in seen: continue
        vec = np.zeros(len(Cq)); orbit = set()
        for g in G:
            d, s = act(g, c); vec[idx[d]] += s; orbit.add(d)
        seen |= orbit
        if np.any(vec != 0): B.append(vec / np.abs(vec[vec != 0]).min())
    return np.array(B).T if B else np.zeros((len(Cq), 0))

def table(X, K, name, qmax=3):
    G = automorphisms(X); C = cells(X, K, qmax)
    D = {q: boundary(C[q], C[q-1]) for q in range(1, qmax+1)}
    B = {q: invariant_basis(C[q], G) for q in range(qmax+1)}
    dims = {q: B[q].shape[1] for q in B}
    rk = {}
    for q in range(1, qmax+1):
        # d restricted to invariant chains, expressed in ambient coords
        M = (D[q] @ B[q]).round().astype(np.int64)
        rk[q] = rank_mod(M, P) if M.size else 0
    rk[qmax+1] = 0
    betti = {q: dims[q] - (rk[q] if q >= 1 else 0) - rk[q+1] for q in range(qmax+1)}
    eps = dims[1] - rk[1]
    print(f"{name:10s} K={K} |G|={len(G):3d} sq={len(C[2]):4d} cubes={len(C.get(3,[])):4d} "
          f"dimC1_G={dims[1]:3d} dimC2_G={dims[2]:3d} rk_d0={rk[1]} rk_d1={rk[2]} rk_d2={rk[3]} "
          f"eps={eps} eps_harm={betti[1]} eps2_harm={betti[2]} H3_G={betti[3]}")
    return C, D, G, B, rk



def rref(M, p):
    M = M.copy() % p; rows, cols = M.shape; piv = []; r = 0
    for c in range(cols):
        if r == rows: break
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0: continue
        i = r + nz[0]
        if i != r: M[[r, i]] = M[[i, r]]
        if p != 2: M[r] = (M[r] * pow(int(M[r, c]), p-2, p)) % p
        others = np.nonzero(M[:, c])[0]; others = others[others != r]
        if others.size:
            M[others] = (M[others] - np.outer(M[others, c], M[r])) % p
        piv.append(c); r += 1
    return M[:r], piv

def nullspace(M, p):
    n = M.shape[1]; R, piv = rref(M, p)
    free = [c for c in range(n) if c not in set(piv)]
    N = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        N[f, j] = 1
        for i, pc in enumerate(piv): N[pc, j] = (-R[i, f]) % p
    return N

def colbasis(M, p):
    if M.shape[1] == 0: return M
    _, piv = rref(M, p); return M[:, piv]

def perm_mats(C, G):
    idx = {c: i for i, c in enumerate(C)}; mats = []
    for g in G:
        P = np.zeros((len(C), len(C)), dtype=np.int64)
        for j, c in enumerate(C):
            d, s = act(g, c); P[idx[d], j] = s
        mats.append(P)
    return mats

def inv_basis(C, G, p):
    idx = {c: i for i, c in enumerate(C)}; seen = set(); B = []
    for c in C:
        if c in seen: continue
        val = {}; ok = True
        for g in G:
            d, s = act(g, c)
            if d in val and (val[d] - s) % p != 0: ok = False
            val[d] = s
        seen |= set(val)
        if ok:
            v = np.zeros(len(C), dtype=np.int64)
            for d, s in val.items(): v[idx[d]] = s % p
            B.append(v)
    return np.array(B, dtype=np.int64).T if B else np.zeros((len(C), 0), dtype=np.int64)

def rank(M, p): return len(rref(M, p)[1]) if M.size else 0

def compare(X, K, name, qs=(1, 2)):
    G = automorphisms(X); C = cells(X, K, 3)
    D = {q: boundary(C[q], C[q-1]) for q in (1, 2, 3)}
    delta = {q: D[q+1].T.astype(np.int64) for q in (0, 1, 2)}   # delta_q : C^q -> C^{q+1}
    for p, lab in [(1000003, 'Q '), (2, 'F2')]:
        out = []
        for q in qs:
            # (a) invariant cochains first
            Bq = inv_basis(C[q], G, p); Bm = inv_basis(C[q-1], G, p)
            a = Bq.shape[1] - rank(delta[q] @ Bq % p, p) - rank(delta[q-1] @ Bm % p, p)
            # (b) cohomology first, then invariants
            Z = nullspace(delta[q] % p, p)
            Bim = colbasis(delta[q-1] % p, p)
            R, piv = rref(np.hstack([Bim, Z]), p)
            H = np.hstack([Bim, Z])[:, [c for c in piv if c >= Bim.shape[1]]]
            h = H.shape[1]; nb = Bim.shape[1]
            span = np.hstack([Bim, H])
            conds = []
            Ps = perm_mats(C[q], G)
            T = np.hstack([ (P @ H) % p for P in Ps ])
            Raug, pv = rref(np.hstack([span, T]), p)
            coords = Raug[:, span.shape[1]:]          # rows correspond to pivots of span (all independent)
            for k in range(len(Ps)):
                A = coords[nb:nb+h, k*h:(k+1)*h]
                conds.append((A - np.eye(h, dtype=np.int64)) % p)
            b = h - rank(np.vstack(conds), p) if h else 0
            out.append(f"H^{q}: inv-then-coh={a} coh-then-inv={b} (full={h})")
        print(f"{name:12s} |G|={len(G):3d} {lab}  " + "   ".join(out))




def comparison(X, K, G, p, label, qmax=3):
    C = cells(X, K, qmax); n = {q: len(C[q]) for q in range(qmax+1)}
    delta = {q: (boundary(C[q+1], C[q]).T.astype(np.int64) if q < qmax else np.zeros((0, n[q]), dtype=np.int64)) for q in range(qmax+1)}
    rows = []
    for q in range(qmax+1):
        Bq = inv_basis(C[q], G, p)
        if Bq.shape[1] == 0: rows.append((q, 0, 0, 0)); continue
        M = (delta[q] @ Bq) % p if delta[q].shape[0] else np.zeros((0, Bq.shape[1]), dtype=np.int64)
        N = nullspace(M, p) if M.shape[0] else np.eye(Bq.shape[1], dtype=np.int64)
        Zinv = (Bq @ N) % p
        Bm = inv_basis(C[q-1], G, p) if q > 0 else None
        Binv = colbasis((delta[q-1] @ Bm) % p, p) if q > 0 and Bm.shape[1] else np.zeros((n[q], 0), dtype=np.int64)
        h_inv = Zinv.shape[1] - Binv.shape[1]
        Bfull = colbasis(delta[q-1] % p, p) if q > 0 else np.zeros((n[q], 0), dtype=np.int64)
        img = rank(np.hstack([Bfull, Zinv]) % p, p) - Bfull.shape[1]
        rows.append((q, h_inv, img, h_inv - img))
    print(f"{label:34s} " + "  ".join(f"H^{q}: reader={h} object={i} reader-only={k}" for q, h, i, k in rows))

C8 = nx.cycle_graph(8); half = [{i: i for i in range(8)}, {i: (i+4) % 8 for i in range(8)}]
prism = nx.circular_ladder_graph(3); K33 = nx.complete_bipartite_graph(3, 3)
for p, lab in [(1000003, 'char0'), (2, 'F2')]:
    comparison(C8, 3, half, p, f"C8 K=3 free half-turn  [{lab}]")
    comparison(prism, 3, automorphisms(prism), p, f"prism K=3 Aut  [{lab}]")
    comparison(K33, 3, automorphisms(K33), p, f"K33 K=3 Aut  [{lab}]")
