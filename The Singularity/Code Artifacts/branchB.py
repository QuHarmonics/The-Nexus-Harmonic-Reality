"""C6 and Z3^2 have (C^1)^G = (im d0)^G, so every invariant 1-form there is exact.
Q3 does not: (C^1)^G = 3 but (im d0)^G = 2.  Does the extra invariant direction
actually charge a closed orbit, or is its circulation zero anyway?
"""
import itertools, numpy as np
from hodge import (arena, cells_disjoint, cells_fourcycle, d0_matrix, d1_matrix,
                   edge_action, colspace, rank_abs, aut_hypercube, aut_cycle, agl23,
                   C6, Q3, Z32, ATOL)


def invariant_forms(base_adj, N, K, AUT, predicate, name):
    verts, vi, edges, ei, nbr = arena(base_adj, N, K)
    cells = cells_disjoint(verts, nbr, base_adj, K) if predicate == "disjoint" \
        else cells_fourcycle(verts, nbr)
    D0 = d0_matrix(verts, vi, edges, ei)
    Pi = sum(edge_action(g, edges, ei) for g in AUT) / len(AUT)
    Inv = colspace(Pi)                       # basis of (C^1)^G
    ExInv = colspace(Pi @ colspace(D0))      # basis of (im d0)^G
    # component of Inv orthogonal to ExInv
    if ExInv.shape[1]:
        R = Inv - ExInv @ (ExInv.T @ Inv)
    else:
        R = Inv
    NonEx = colspace(R)
    print(f"\n### {name} [{predicate}]  (C^1)^G={Inv.shape[1]}  (im d0)^G={ExInv.shape[1]}  "
          f"invariant non-exact directions = {NonEx.shape[1]}")

    # self-reversing edges: every invariant form must vanish there
    sr = []
    for k, (a, b) in enumerate(edges):
        if any(frozenset(g[e] for e in a) == b and frozenset(g[e] for e in b) == a for g in AUT):
            sr.append(k)
    if Inv.shape[1]:
        print(f"    undirected self-reversing edges: {len(sr)};  "
              f"max |invariant form| there = {np.abs(Inv[sr, :]).max() if sr else 0:.2e}")

    if NonEx.shape[1] == 0:
        print("    -> every invariant 1-form is EXACT. Closed-orbit price is 0 by construction.")
        return
    # circulation of the non-exact invariant form around cycles of the arena
    nbrl = {x: sorted(nbr[x], key=lambda s: sorted(s)) for x in verts}
    def circ(w, cyc):
        t = 0.0
        for i in range(len(cyc)):
            j, s = ei[(cyc[i], cyc[(i + 1) % len(cyc)])]
            t += s * w[j]
        return t
    w = NonEx[:, 0]
    best, found = 0.0, 0
    for x in verts:                     # all simple 4- and 6-cycles through a DFS bound
        stack = [(x, [x])]
        while stack:
            v, path = stack.pop()
            if len(path) > 6:
                continue
            for u in nbrl[v]:
                if u == x and len(path) >= 3:
                    c = abs(circ(w, path))
                    if c > 1e-9:
                        found += 1; best = max(best, c)
                elif u not in path and sorted(u) > sorted(x):
                    stack.append((u, path + [u]))
    print(f"    cycles (len<=6) with nonzero circulation: {found};  max |circulation| = {best:.6f}")
    print("    -> a non-exact invariant price EXISTS and charges closed orbits." if found
          else "    -> invariant non-exact direction exists but all short-cycle circulation vanishes.")


invariant_forms(C6, 6, 3, aut_cycle(6), "four_cycle", "C6 arena")
invariant_forms(Q3, 8, 3, aut_hypercube(3), "disjoint", "Q3 arena (frozen spec)")
invariant_forms(Q3, 8, 3, aut_hypercube(3), "four_cycle", "Q3 arena (frozen spec)")
invariant_forms(Z32, 9, 3, agl23(), "disjoint", "Z3^2 arena (K9)")
