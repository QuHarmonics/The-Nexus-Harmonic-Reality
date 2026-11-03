"""Three things:
  (A) the named falsifier: K=5 on C8, plus K=5 on Q3 and a NON-vertex-transitive base (path P8)
  (B) is choice ever forced? minimum out-degree on the arena
  (C) what does a locally-perpetual orbit cost? Q and acceleration around closed one-way cycles
"""
import itertools
from collections import defaultdict
from predict_c6 import build, aut_cycle, aut_hypercube, partitions_into, directional_classes, C6, C8, Q3
from derive import derived_classes

P8 = {v: {w for w in (v - 1, v + 1) if 0 <= w <= 7} for v in range(8)}   # path, NOT vertex-transitive


def compare(name, base_adj, N, K, ms):
    verts, dedges = build(base_adj, N, K)
    edges = sorted(set((x, y) for x, y, _, _ in dedges), key=lambda p: (sorted(p[0]), sorted(p[1])))
    print(f"\n### {name}  N={N} K={K}  V={len(verts)} E_dir={len(dedges)}")
    ok = bad = 0
    for m in ms:
        allp = sorted(set(tuple(sorted(p, key=lambda b: sorted(b))) for p in partitions_into(range(N), m)),
                      key=lambda p: [sorted(b) for b in p])
        byprof = defaultdict(list)
        for c in allp:
            byprof[tuple(sorted(len(b) for b in c))].append(c)
        for prof, cuts in sorted(byprof.items()):
            meas, pred = len(directional_classes(cuts, edges)), len(derived_classes(prof, K))
            ok += meas == pred; bad += meas != pred
            print(f"   m={m} profile {str(prof):<14} measured={meas:<2} derived={pred:<2} "
                  f"{'ok ' if meas == pred else '*** KILLED ***'}")
    return ok, bad


print("=" * 72)
print("(A) FALSIFIER: derived count uses (K, profile) only. Graph must not matter.")
tot = [0, 0]
for args in [("C8 (named falsifier)", C8, 8, 5, [3, 4]),
             ("Q3", Q3, 8, 5, [3, 4]),
             ("P8 path - NOT vertex-transitive", P8, 8, 3, [3, 4]),
             ("P8 path - NOT vertex-transitive", P8, 8, 4, [3, 4])]:
    a, b = compare(*args); tot[0] += a; tot[1] += b
print(f"\n   >>> {tot[0]} agree, {tot[1]} killed")

print("\n" + "=" * 72)
print("(B) Is choice ever forced?  out-degree of every arena state")
for name, adj, N, K in [("C6", C6, 6, 3), ("C8", C8, 8, 3), ("Q3", Q3, 8, 3), ("P8", P8, 8, 3)]:
    verts, dedges = build(adj, N, K)
    out = defaultdict(int)
    for x, y, _, _ in dedges:
        out[x] += 1
    d = sorted(set(out.values()))
    print(f"   {name:3} K={K}: out-degrees {d}   min={min(out.values())}  "
          f"states with a unique continuation: {sum(1 for v in out.values() if v == 1)}")

print("\n" + "=" * 72)
print("(C) Locally-perpetual motion: the one-way (+1 only) subgraph on a cycle base")


def oneway(N, K):
    verts = [frozenset(s) for s in itertools.combinations(range(N), K)]
    succ = defaultdict(list)
    for x in verts:
        for u in x:
            w = (u + 1) % N
            if w not in x:
                succ[x].append(frozenset((x - {u}) | {w}))
    return verts, succ


def psi(cut, x):
    return sum(len(b & x) ** 2 for b in cut)


for N, K in [(6, 3), (8, 3)]:
    verts, succ = oneway(N, K)
    od = sorted(set(len(succ[x]) for x in verts))
    # every state has a successor -> infinite one-way paths exist; find the simple cycles reachable
    # by always taking the lowest-index successor (a deterministic policy) and by exhaustive short search
    cycles = set()
    for start in verts:
        path, seen = [start], {start: 0}
        x = start
        while True:
            if not succ[x]:
                break
            x = sorted(succ[x], key=lambda s: sorted(s))[0]
            if x in seen:
                cycles.add(tuple(path[seen[x]:]))
                break
            seen[x] = len(path); path.append(x)
    print(f"\n   C{N}, K={K}: one-way out-degrees {od}, states with no one-way move: "
          f"{sum(1 for x in verts if not succ[x])}")
    print(f"      deterministic-policy limit cycles: {len(cycles)}, lengths {sorted(set(len(c) for c in cycles))}")
    # cost of running a limit cycle, for one fixed reader
    cut = (frozenset({0}), frozenset({1, 2}), frozenset(range(3, N)))
    for c in sorted(cycles, key=len)[:3]:
        L = len(c)
        Qs = [psi(cut, c[(i + 1) % L]) - psi(cut, c[i]) for i in range(L)]
        acc = [Qs[(i + 1) % L] - Qs[i] for i in range(L)]
        print(f"      cycle len {L}: sum Q = {sum(Qs)}, sum a = {sum(acc)}, "
              f"sum|Q| = {sum(abs(q) for q in Qs)}, sum|a| = {sum(abs(a) for a in acc)}")
