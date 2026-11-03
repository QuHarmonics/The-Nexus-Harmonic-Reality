# Inverted Nyquist on the token arena: every symmetry subgroup of Aut(prism) as a candidate interface,
# three tokens on the once-subdivided prism. Which interface is simplest while still carrying the exchange class?
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

import itertools

prism = nx.circular_ladder_graph(3); Gp = automorphisms(prism)
key = lambda g: tuple(g[i] for i in range(6))
comp = lambda g,h: {i: g[h[i]] for i in range(6)}
def closure(gens):
    S = {key({i:i for i in range(6)}): {i:i for i in range(6)}}
    frontier = list(gens)
    while frontier:
        g = frontier.pop()
        if key(g) in S: continue
        S[key(g)] = g
        for h in list(S.values()): frontier += [comp(g,h), comp(h,g)]
    return list(S.values())
subs = {}
for a,b in itertools.combinations_with_replacement(Gp,2):
    H = closure([a,b]); subs[frozenset(key(h) for h in H)] = H
coords = {i: np.array([np.cos(2*np.pi*i/3), np.sin(2*np.pi*i/3), 1.0]) for i in range(3)}
coords.update({i+3: np.array([np.cos(2*np.pi*i/3), np.sin(2*np.pi*i/3), -1.0]) for i in range(3)})
def det_sign(g):
    A=np.array([coords[i] for i in range(6)]); B=np.array([coords[g[i]] for i in range(6)])
    M,*_=np.linalg.lstsq(A,B,rcond=None); return int(np.sign(np.linalg.det(M)))
Y = nx.Graph(); mid={}; c=6
for u,v in prism.edges():
    e=tuple(sorted((u,v))); mid[e]=c; nx.add_path(Y,[u,c,v]); c+=1
def lift(g):
    h={i:g[i] for i in range(6)}
    for (u,v),m in mid.items(): h[m]=mid[tuple(sorted((g[u],g[v])))]
    return h
C1 = cells(Y,1,1); C3 = cells(Y,3,3)
D1 = {q: boundary(C1[q],C1[q-1]) for q in (1,)}
D3 = {q: boundary(C3[q],C3[q-1]) for q in (1,2,3)}
def inv_b(C,D,G,qmax):
    B={q: invariant_basis(C[q],G) for q in range(qmax+1)}
    rk={q:(rank_mod((D[q]@B[q]).round().astype(np.int64),P) if B[q].shape[1] else 0) for q in range(1,qmax+1)}
    rk[0]=0; rk[qmax+1]=0
    return [B[q].shape[1]-rk[q]-rk[q+1] for q in range(qmax+1)]
rows=[]
for S,H in subs.items():
    L=[lift(g) for g in H]
    one=inv_b(C1,D1,L,1); three=inv_b(C3,D3,L,3)
    rev = sum(1 for g in H if det_sign(g)<0)
    rows.append((len(H), rev, three[1], one[1], three[1]-one[1], three[2]))
print("order  reflections  H1(3 tokens)  H1(1 token)  exchange-excess  H2(3 tokens)")
for r in sorted(set(rows)):
    print(f"{r[0]:5d}  {r[1]:11d}  {r[2]:12d}  {r[3]:11d}  {r[4]:15d}  {r[5]:12d}   x{rows.count(r)}")
