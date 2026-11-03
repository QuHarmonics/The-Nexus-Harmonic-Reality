"""
Canonical arena generator.  Standard library only.  No special case for any graph.

A arena spec is the 7-tuple  A(X, k, labelled, exclusion, move, admit, cell)
and the generator emits (V, E_dir, E, F2, F3, beta1) plus the Aut(X) fingerprints
(self-reversing directed edges, orbit counts) from that tuple alone.

Reproduction test:  one spec must yield
    C_6      -> (V,E,F2) = (20, 36, 18)      [locked; also 72 directed, 24 self-reversing]
    Q_3      -> E = 1032, F2 = 1248          [locked; 2064 directed, 48 self-reversing]
    Z_3^2    -> E = 5121, F2 = 9612          [locked; 10242 directed, 378 self-reversing]
If it does not reproduce all three, nothing above the graph layer is admissible.
"""
from itertools import combinations, permutations, product, combinations_with_replacement

# ---------------- 1. ambient graph X ----------------
def graph(name):
    if name.startswith("C_"):
        n = int(name[2:]); V = list(range(n)); E = [(i, (i+1) % n) for i in range(n)]
    elif name.startswith("P_"):
        n = int(name[2:]); V = list(range(n)); E = [(i, i+1) for i in range(n-1)]
    elif name.startswith("K_"):
        n = int(name[2:]); V = list(range(n)); E = list(combinations(range(n), 2))
    elif name == "Q_3":
        V = list(range(8)); E = [(v, v ^ (1 << b)) for v in range(8) for b in range(3) if v < v ^ (1 << b)]
    elif name == "Z3^2_deg4":
        V = [(i, j) for i in range(3) for j in range(3)]
        E = sorted({tuple(sorted((p, ((p[0]+d[0]) % 3, (p[1]+d[1]) % 3))))
                    for p in V for d in ((1, 0), (0, 1))})
    elif name == "Z3^2_deg8":
        V = [(i, j) for i in range(3) for j in range(3)]; E = list(combinations(V, 2))
    else:
        raise ValueError(name)
    return V, E

def adjacency(V, E):
    A = {v: set() for v in V}
    for u, v in E:
        A[u].add(v); A[v].add(u)
    return A

def automorphisms(V, E):
    """Brute force Aut(X).  Fine for |V| <= 9."""
    Es = {frozenset(e) for e in E}
    out = []
    for p in permutations(V):
        g = dict(zip(V, p))
        if all(frozenset((g[u], g[v])) in Es for u, v in E):
            out.append(g)
    return out

# ---------------- 2-4. states ----------------
def states(V, k, labelled, exclusion, admit, A):
    if labelled and exclusion:   raw = list(permutations(V, k))
    elif labelled:               raw = list(product(V, repeat=k))
    elif exclusion:              raw = [tuple(c) for c in combinations(V, k)]
    else:                        raw = [tuple(c) for c in combinations_with_replacement(V, k)]
    return [s for s in raw if admissible(s, A, admit)]

def admissible(s, A, admit):
    occ = set(s)
    if admit == "all":         return True
    if admit == "connected":                      # occupied set induces a connected subgraph
        seen, st = {next(iter(occ))}, [next(iter(occ))]
        while st:
            x = st.pop()
            for y in A[x] & occ:
                if y not in seen: seen.add(y); st.append(y)
        return seen == occ
    if admit == "independent": return all(v not in A[u] for u, v in combinations(occ, 2))
    raise ValueError(admit)

# ---------------- 5-6. moves ----------------
def normalise(t, labelled):
    return tuple(t) if labelled else tuple(sorted(t, key=repr))

def moves(s, A, labelled, exclusion, admit, move):
    """Returns list of (support, target_state).  support is the vertex set the move touches."""
    out, occ = [], set(s)
    for i, u in enumerate(s):
        for v in A[u]:
            if exclusion and v in occ: continue
            t = list(s); t[i] = v; t = normalise(t, labelled)
            if admissible(t, A, admit): out.append((frozenset((u, v)), t))
    if move == "step_swap" and labelled and exclusion:
        for i, j in combinations(range(len(s)), 2):
            if s[j] in A[s[i]]:
                t = list(s); t[i], t[j] = t[j], t[i]; t = normalise(t, labelled)
                if admissible(t, A, admit): out.append((frozenset((s[i], s[j])), t))
    return out

# ---------------- 7. relation predicate (2-cells) ----------------
def build(name, k, labelled, exclusion, move="step", admit="all", cell="disjoint", want_aut=True):
    V, E = graph(name); A = adjacency(V, E)
    S = states(V, k, labelled, exclusion, admit, A)
    if not S or len(S) > 6000: return None
    si = {s: i for i, s in enumerate(S)}
    mv, und, ndir = {}, set(), 0
    for s in S:
        ms = [(sup, t) for sup, t in moves(s, A, labelled, exclusion, admit, move) if t != s]
        mv[si[s]] = [(sup, si[t]) for sup, t in ms]
        ndir += len(ms)
        for sup, t in ms: und.add(frozenset((si[s], si[t])))
    nbr = {i: set() for i in range(len(S))}
    for e in und:
        a, b = tuple(e); nbr[a].add(b); nbr[b].add(a)

    if cell == "four_cycle":
        F2 = 0
        for a in range(len(S)):
            for b in range(a+1, len(S)):
                c = [x for x in nbr[a] & nbr[b] if x > a]
                F2 += len(c)*(len(c)-1)//2
        F3 = None
    else:
        ok = (lambda p, q: p.isdisjoint(q)) if cell == "disjoint" else (lambda p, q: True)
        P = T = 0
        for i in range(len(S)):
            ms = mv[i]
            for (p, a), (q, b) in combinations(ms, 2):
                if ok(p, q) and a != b: P += 1
            for (p, a), (q, b), (r, c) in combinations(ms, 3):
                if ok(p, q) and ok(p, r) and ok(q, r) and len({a, b, c}) == 3: T += 1
        F2, F3 = P // 4, T // 8

    res = dict(spec=(name, k, labelled, exclusion, move, admit, cell),
               V=len(S), E_dir=ndir, E=len(und), F2=F2, F3=F3,
               beta1=len(und) - len(S) + components(nbr, len(S)))
    if want_aut and len(V) <= 9:
        G = automorphisms(V, E)
        def act(g, s): return normalise(tuple(g[x] for x in s), labelled)
        D = [(a, b) for e in und for a, b in (tuple(e), tuple(e)[::-1])]
        sr = sum(1 for a, b in D
                 if any(si[act(g, S[a])] == b and si[act(g, S[b])] == a for g in G))
        vo, seen = 0, set()
        for i in range(len(S)):
            if i in seen: continue
            vo += 1
            for g in G: seen.add(si[act(g, S[i])])
        res.update(aut=len(G), self_reversing=sr, vertex_orbits=vo)
    return res

def components(nbr, n):
    seen, c = set(), 0
    for s in range(n):
        if s in seen: continue
        c += 1; st = [s]; seen.add(s)
        while st:
            x = st.pop()
            for y in nbr[x]:
                if y not in seen: seen.add(y); st.append(y)
    return c

def rank(M, tol=1e-9):
    """Absolute-tolerance rank.  Never use numpy's relative default on an exact-zero operator."""
    import numpy as np
    return int((np.linalg.svd(np.asarray(M, float), compute_uv=False) > tol).sum())
