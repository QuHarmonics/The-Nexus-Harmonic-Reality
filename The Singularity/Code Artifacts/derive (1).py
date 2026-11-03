"""Derived predictor for the number of directional reader type-classes.

A single-token move takes block i from a to a-1 and block j from b to b+1 (i != j);
spectator blocks are unchanged.  Reversal sends (a,b) -> (b+1, a-1), which preserves
t = a+b, so classes live inside each (t, spectator-multiset) bucket, and inside a bucket
reversal acts as  a -> t+1-a.

  * directional  <=>  b != a-1  <=>  a != (t+1)/2
  * #classes(t,S) = #orbits of  a -> t+1-a  on the realizable a

Realizability from caps only: 1<=a<=s_i, 0<=b<=s_j-1, spectator n_k<=s_k.
Graph adjacency is NOT imposed here - any place the derived count exceeds the measured
count is exactly where the base graph forbids an occupancy pattern the caps allow.
"""
import itertools
from collections import defaultdict
from predict_c6 import (build, aut_cycle, aut_hypercube, partitions_into,
                        selfrev_edges, directional_classes, C6, C8, Q3)


def derived_classes(profile, K):
    m = len(profile)
    types = set()
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            spec = [profile[k] for k in range(m) if k not in (i, j)]
            for a in range(1, profile[i] + 1):
                for b in range(0, profile[j]):
                    rest = K - a - b
                    if rest < 0 or rest > sum(spec):
                        continue
                    for occ in itertools.product(*[range(s + 1) for s in spec]):
                        if sum(occ) != rest:
                            continue
                        tau = tuple(sorted([(a, a - 1), (b, b + 1)] + [(o, o) for o in occ]))
                        rev = tuple(sorted((y, x) for (x, y) in tau))
                        if tau != rev:
                            types.add(min(tau, rev))
    return types


def compare(name, base_adj, N, K, AUT, ms):
    verts, dedges = build(base_adj, N, K)
    edges = sorted(set((x, y) for x, y, _, _ in dedges),
                   key=lambda p: (sorted(p[0]), sorted(p[1])))
    print(f"\n### {name}  N={N} K={K}  V={len(verts)} E_dir={len(dedges)}")
    ok = bad = 0
    for m in ms:
        allp = sorted(set(tuple(sorted(p, key=lambda b: sorted(b)))
                          for p in partitions_into(range(N), m)),
                      key=lambda p: [sorted(b) for b in p])
        byprof = defaultdict(list)
        for c in allp:
            byprof[tuple(sorted(len(b) for b in c))].append(c)
        for prof, cuts in sorted(byprof.items()):
            meas = len(directional_classes(cuts, edges))
            pred = len(derived_classes(prof, K))
            tag = "ok " if meas == pred else "*** differs ***"
            ok += meas == pred
            bad += meas != pred
            print(f"   m={m} profile {str(prof):<14} measured={meas}  derived={pred}  {tag}")
    return ok, bad


tot_ok = tot_bad = 0
for args in [("C6", C6, 6, 2, aut_cycle(6), [2, 3, 4]),
             ("C6", C6, 6, 3, aut_cycle(6), [2, 3, 4]),
             ("C8", C8, 8, 2, aut_cycle(8), [3, 4]),
             ("C8", C8, 8, 3, aut_cycle(8), [3, 4]),
             ("C8", C8, 8, 4, aut_cycle(8), [3, 4]),
             ("Q3", Q3, 8, 3, aut_hypercube(3), [3, 4]),
             ("Q3", Q3, 8, 4, aut_hypercube(3), [3, 4])]:
    a, b = compare(*args)
    tot_ok += a; tot_bad += b
print(f"\n=== derived formula vs measurement: {tot_ok} agree, {tot_bad} differ ===")

print("\nK=2 theorem check: derived class count for every profile up to m=4, sizes<=6")
vals = set()
for m in (2, 3, 4):
    for prof in itertools.combinations_with_replacement(range(1, 7), m):
        vals.add(len(derived_classes(prof, 2)))
print("   distinct derived class counts at K=2 over all profiles:", sorted(vals))
