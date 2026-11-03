#!/usr/bin/env python3
"""
NEXUS Continuation-Graph Countermodel Harness
==============================================

Question:
    Does C0 + C1 + C1a + finite observability + reversible-C2-proxy
    force a K3 subgraph in the transition adjacency graph?

Operationalization:
    * C1  = total map; here permutations, so stronger.
    * C1a = two continuation maps commute.
    * finite observability = finite X.
    * C2  = bijective/reversible proxy, explicitly only a proxy.
    * K3  = triangle in the undirected union of generator edges.

The script:
    1. Constructs exact toroidal countermodels.
    2. Exhaustively enumerates commuting permutation pairs for N=1..4.
    3. Measures cycle rank and triangle presence.
    4. Prints the smallest triangle-free nontrivial model.

No external packages required.
"""

from __future__ import annotations
import itertools
from collections import Counter

Perm = tuple[int, ...]


def compose(p: Perm, q: Perm) -> Perm:
    return tuple(p[q[i]] for i in range(len(p)))


def identity(n: int) -> Perm:
    return tuple(range(n))


def inverse(p: Perm) -> Perm:
    q = [0] * len(p)
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def commutes(p: Perm, q: Perm) -> bool:
    return compose(p, q) == compose(q, p)


def transition_edges(perms: list[Perm]) -> set[tuple[int, int]]:
    n = len(perms[0])
    edges = set()
    for p in perms:
        for x, y in enumerate(p):
            if x != y:
                a, b = sorted((x, y))
                edges.add((a, b))
    return edges


def components(n: int, edges: set[tuple[int, int]]) -> int:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    seen = [False] * n
    c = 0
    for s in range(n):
        if not seen[s]:
            c += 1
            stack = [s]
            seen[s] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
    return c


def has_triangle(n: int, edges: set[tuple[int, int]]) -> bool:
    E = edges
    for a in range(n):
        for b in range(a + 1, n):
            if (a, b) not in E:
                continue
            for c in range(b + 1, n):
                if (a, c) in E and (b, c) in E:
                    return True
    return False


def cycle_rank(n: int, edges: set[tuple[int, int]]) -> int:
    c = components(n, edges)
    return len(edges) - n + c


def torus_perm(n: int, dx: int, dy: int) -> Perm:
    N = n * n
    def idx(x, y):
        return (x % n) * n + (y % n)

    p = [0] * N
    for x in range(n):
        for y in range(n):
            p[idx(x, y)] = idx(x + dx, y + dy)
    return tuple(p)


def torus_test(n: int):
    A = torus_perm(n, 1, 0)
    B = torus_perm(n, 0, 1)
    assert commutes(A, B)
    assert inverse(A)
    assert inverse(B)

    E = transition_edges([A, B])
    c = components(n * n, E)
    beta = cycle_rank(n * n, E)
    tri = has_triangle(n * n, E)

    print(
        f"torus n={n}: |V|={n*n}, |E|={len(E)}, "
        f"components={c}, cycle_rank={beta}, K3={tri}"
    )
    return {
        "n": n,
        "V": n * n,
        "E": len(E),
        "components": c,
        "cycle_rank": beta,
        "K3": tri,
    }


def exhaustive_commuting_pairs(n: int):
    perms = list(itertools.permutations(range(n)))
    total = 0
    triangle_free_nontrivial = 0
    cycle_rank_counter = Counter()
    triangle_counter = Counter()
    examples = []

    for A in perms:
        for B in perms:
            if not commutes(A, B):
                continue

            total += 1
            E = transition_edges([A, B])
            beta = cycle_rank(n, E)
            tri = has_triangle(n, E)

            cycle_rank_counter[beta] += 1
            triangle_counter[tri] += 1

            # Nontrivial = at least one edge and at least one cycle.
            if len(E) > 0 and beta > 0 and not tri:
                triangle_free_nontrivial += 1
                if len(examples) < 3:
                    examples.append((A, B, E, beta))

    print(
        f"N={n}: commuting ordered pairs={total}; "
        f"triangle-free + cycle-rank>0={triangle_free_nontrivial}"
    )
    print(f"    cycle-rank distribution: {dict(sorted(cycle_rank_counter.items()))}")
    print(f"    K3 distribution: {dict(triangle_counter)}")

    if examples:
        A, B, E, beta = examples[0]
        print(f"    example A={A}")
        print(f"    example B={B}")
        print(f"    edges={sorted(E)}")
        print(f"    cycle_rank={beta}, K3=False")

    return {
        "N": n,
        "commuting_pairs": total,
        "triangle_free_nontrivial": triangle_free_nontrivial,
        "cycle_rank_distribution": dict(cycle_rank_counter),
        "K3_distribution": dict(triangle_counter),
    }


def main():
    print("=== EXACT TORUS COUNTERMODELS ===")
    for n in (2, 3, 4):
        torus_test(n)

    print("\n=== EXHAUSTIVE COMMUTING REVERSIBLE PAIRS ===")
    results = []
    for n in range(1, 5):
        results.append(exhaustive_commuting_pairs(n))

    print("\n=== CONCLUSION ===")
    print("Finite + reversible + commuting does not force K3.")
    print("The toroidal Z_n x Z_n construction gives explicit triangle-free")
    print("models with nonzero cycle rank.")
    print("C2 remains under-specified; bijectivity here is only a strong proxy.")


if __name__ == "__main__":
    main()
