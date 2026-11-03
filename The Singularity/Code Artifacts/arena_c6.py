"""C6 arena: unlabelled 3-token configuration space over C6, exclusion, single-token step moves.
Rebuilt from the frozen parameters 1-6 of the canonical arena spec.
"""
import itertools, numpy as np
from fractions import Fraction

N = 6
K = 3
base_adj = {v: {(v - 1) % N, (v + 1) % N} for v in range(N)}

# ---- arena vertices: unlabelled k-token configurations with exclusion = k-subsets
verts = sorted(frozenset(s) for s in itertools.combinations(range(N), K))
vidx = {v: i for i, v in enumerate(verts)}
V = len(verts)

# ---- directed edges: one token steps to an adjacent empty vertex
dedges = []          # (x, y, u, v) moved token from u to v
for x in verts:
    for u in x:
        for w in base_adj[u]:
            if w in x:
                continue
            y = frozenset((x - {u}) | {w})
            dedges.append((x, y, u, w))
E_dir = len(dedges)
undirected = set(frozenset((x, y)) for x, y, _, _ in dedges)

# ---- Aut(C6) = dihedral of order 12 acting on Z6
def rot(k):
    return tuple((i + k) % N for i in range(N))
def ref(k):
    return tuple((k - i) % N for i in range(N))
AUT = [rot(k) for k in range(N)] + [ref(k) for k in range(N)]
assert len(set(AUT)) == 12

def act_v(g, x):
    return frozenset(g[i] for i in x)

# vertex orbits
seen, vorbits = set(), []
for x in verts:
    if x in seen:
        continue
    o = set(act_v(g, x) for g in AUT)
    seen |= o
    vorbits.append(sorted(o, key=lambda s: sorted(s)))
orb_of = {}
for i, o in enumerate(vorbits):
    for x in o:
        orb_of[x] = i

# directed edge orbits
de_set = set((x, y) for x, y, _, _ in dedges)
seen, deorbits = set(), []
for (x, y) in sorted(de_set, key=lambda p: (sorted(p[0]), sorted(p[1]))):
    if (x, y) in seen:
        continue
    o = set((act_v(g, x), act_v(g, y)) for g in AUT)
    seen |= o
    deorbits.append(o)

# self-reversing directed edges: exists g with gx=y and gy=x
def reversers(x, y):
    return [g for g in AUT if act_v(g, x) == y and act_v(g, y) == x]
selfrev = [(x, y) for (x, y) in de_set if reversers(x, y)]

print("=== C6 arena, frozen params 1-6 ===")
print("V                    :", V)
print("E_dir                :", E_dir)
print("E_undirected         :", len(undirected))
print("|Aut|                :", len(AUT))
print("vertex orbits        :", len(vorbits), [len(o) for o in vorbits])
print("directed edge orbits :", len(deorbits), [len(o) for o in deorbits])
print("self-reversing dir E :", len(selfrev), f"({100*len(selfrev)/E_dir:.1f}%)")
print("orbit gap types      :", [sorted(o[0]) for o in vorbits])

# ---- object side control: Aut-invariant state functions have zero gradient on self-reversing edges
maxgrad = 0.0
for i in range(len(vorbits)):
    f = {x: (1.0 if orb_of[x] == i else 0.0) for x in verts}
    for (x, y) in selfrev:
        maxgrad = max(maxgrad, abs(f[y] - f[x]))
print("\nobject-side: max |invariant-potential gradient| over self-reversing edges =", maxgrad)

np.save("/home/claude/arena/_verts.npy", np.array([sorted(v) for v in verts]))
import pickle
pickle.dump(dict(verts=verts, dedges=dedges, AUT=AUT, selfrev=selfrev,
                 vorbits=vorbits, orb_of=orb_of, deorbits=deorbits),
            open("/home/claude/arena/_arena.pkl", "wb"))
