"""Is the reader's response graded, independent of which functional we pick?

Choice-free criterion.  The reader's complete observable at a state is the block-occupancy
vector n_l(x).  For a directed arena edge e=(x,y) the reader sees the type

    tau(e) = multiset over blocks B of ( n_B(x), n_B(y) )      [block labels are not observable]

Reversal acts by swapping the two coordinates.  An antisymmetric response can take two
distinct nonzero magnitudes iff there are >= 2 directional type-classes (classes with
tau != rev(tau)) that are not related by reversal.  One class => the response is a sign.
"""
import itertools, pickle
from collections import defaultdict, Counter

D = pickle.load(open("/home/claude/arena/_arena.pkl", "rb"))
verts, dedges, AUT, selfrev = D["verts"], D["dedges"], D["AUT"], D["selfrev"]
orb_of = D["orb_of"]
N, K = 6, 3
selfrev_set = set(selfrev)

exec(open("/home/claude/arena/reader_c6.py").read().split("print(\"=\" * 72)")[0]
     .replace('D = pickle.load(open("/home/claude/arena/_arena.pkl", "rb"))', 'pass')
     .replace('verts, dedges, AUT, selfrev = D["verts"], D["dedges"], D["AUT"], D["selfrev"]', 'pass')
     .replace('orb_of, vorbits = D["orb_of"], D["vorbits"]', 'pass'))


def tau(cut, x, y):
    return tuple(sorted((len(b & x), len(b & y)) for b in cut))


def rev(t):
    return tuple(sorted((b, a) for (a, b) in t))


def analyse(m, cuts, tag, edges, edgename):
    classes = defaultdict(int)
    for c in cuts:
        for (x, y) in edges:
            t = tau(c, x, y)
            key = min(t, rev(t))
            classes[(key, t == rev(t))] += 1
    directional = sorted(k for (k, sym) in classes if not sym)
    symmetric = sorted(k for (k, sym) in classes if sym)
    print(f"\n{tag}  [m={m}, {len(cuts)} cuts, {edgename}]")
    print(f"   directional type-classes : {len(directional)}   -> "
          f"{'GRADED possible' if len(directional) >= 2 else 'SIGN only'}")
    for k in directional:
        print(f"      {k}   count={classes[(k, False)]}")
    print(f"   symmetric (forced 0) classes: {len(symmetric)}")
    return len(directional)


for m in (2, 3, 4):
    allp, bal = cut_families(m)
    for cuts, tag in ((bal, "BALANCED"), (allp, "ALL")):
        if not cuts:
            continue
        analyse(m, cuts, tag, selfrev, "self-reversing edges (24)")

print("\n" + "=" * 72)
print("Which m=3 block-size profiles produce the graded (|Q|=4) response?")
allp3, _ = cut_families(3)
prof_vals = defaultdict(set)
for c in allp3:
    prof = tuple(sorted(len(b) for b in c))
    for (x, y) in selfrev:
        q = Q(c, x, y)
        if q:
            prof_vals[prof].add(abs(q))
for p, v in sorted(prof_vals.items()):
    print(f"   profile {p}: |Q| values on self-reversing edges = {sorted(v)}")

print("\n" + "=" * 72)
print("Source-orbit stratification over ALL 72 directed edges (m=3, all cuts):")
strat = defaultdict(set)
cnt = defaultdict(Counter)
for (x, y, u, v) in dedges:
    for c in allp3:
        q = Q(c, x, y)
        strat[orb_of[x]].add(abs(q))
        cnt[orb_of[x]][abs(q)] += 1
for k in sorted(strat):
    print(f"   source orbit {k}: |Q| values {sorted(strat[k])}   counts {dict(sorted(cnt[k].items()))}")

print("\nsource-orbit membership of the 24 self-reversing edges:",
      dict(Counter(orb_of[x] for (x, y) in selfrev)))

print("\n" + "=" * 72)
print("Acceleration: second difference of Q along 2-step directed paths (m=3, all cuts)")
out = defaultdict(int)
succ = defaultdict(list)
for (x, y, u, v) in dedges:
    succ[x].append(y)
paths = [(x, y, z) for (x, y, _, _) in dedges for z in succ[y] if z != x]
acc_vals = set()
for c in allp3:
    for (x, y, z) in paths:
        a = Q(c, y, z) - Q(c, x, y)
        acc_vals.add(a)
        out[a] += 1
print(f"   2-step paths: {len(paths)}   distinct acceleration values: {sorted(acc_vals)}")
print(f"   distribution: {dict(sorted(out.items()))}")
