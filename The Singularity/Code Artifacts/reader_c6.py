"""Reader-side response on the C6 arena.

Two responses compared:
  A_l  = C - C^T  (antisymmetric part of the block-flow table)   -- last run's quantity
  Q_l  = psi_l(y) - psi_l(x),  psi_l(x) = sum_B n_B(x)^2         -- new: a scalar, relabel-invariant

Cut families: balanced (all blocks equal size) vs all set partitions into m blocks.
"""
import itertools, pickle, numpy as np
from collections import defaultdict

D = pickle.load(open("/home/claude/arena/_arena.pkl", "rb"))
verts, dedges, AUT, selfrev = D["verts"], D["dedges"], D["AUT"], D["selfrev"]
orb_of, vorbits = D["orb_of"], D["vorbits"]
N = 6
move_of = {(x, y): (u, v) for x, y, u, v in dedges}


# ---------- set partitions of {0..5} into exactly m blocks ----------
def partitions_into(elems, m):
    elems = list(elems)
    def rec(i, blocks):
        if i == len(elems):
            if len(blocks) == m:
                yield [frozenset(b) for b in blocks]
            return
        e = elems[i]
        for b in blocks:
            b.append(e); yield from rec(i + 1, blocks); b.pop()
        if len(blocks) < m:
            blocks.append([e]); yield from rec(i + 1, blocks); blocks.pop()
    yield from rec(0, [])


def cut_families(m):
    allp = [tuple(sorted(p, key=lambda b: sorted(b))) for p in partitions_into(range(N), m)]
    allp = sorted(set(allp), key=lambda p: [sorted(b) for b in p])
    bal = [p for p in allp if len(set(len(b) for b in p)) == 1]
    return allp, bal


def block_index(cut):
    bi = {}
    for i, b in enumerate(cut):
        for e in b:
            bi[e] = i
    return bi


def flow_table(cut, x, y):
    """C[i][j] = # tokens in block i at x whose image sits in block j at y."""
    bi = block_index(cut)
    m = len(cut)
    u, v = move_of[(x, y)]
    C = np.zeros((m, m))
    for p in x:
        q = v if p == u else p
        C[bi[p], bi[q]] += 1
    return C


def psi(cut, x):
    return sum(len(b & x) ** 2 for b in cut)


def Q(cut, x, y):
    return psi(cut, y) - psi(cut, x)


def stabilizes(g, cut):
    """g fixes the cut as an unordered set partition."""
    img = set(frozenset(g[e] for e in b) for b in cut)
    return img == set(cut)


def oriented(cuts):
    return [tuple(p) for c in cuts for p in itertools.permutations(c)]


print("=" * 72)
for m in (2, 3):
    allp, bal = cut_families(m)
    print(f"m = {m}:  all set partitions = {len(allp)} ({len(oriented(allp))} oriented) | "
          f"balanced = {len(bal)} ({len(oriented(bal))} oriented)")
    sizes = sorted(set(tuple(sorted(len(b) for b in p)) for p in allp))
    print(f"        block-size profiles: {sizes}")
print("=" * 72)


def report(m, cuts, tag):
    ocuts = oriented(cuts)
    # --- matrix response A on self-reversing edges (last run's quantity)
    mags, hit = set(), 0
    for (x, y) in selfrev:
        any_nonzero = False
        for c in ocuts:
            C = flow_table(c, x, y)
            A = C - C.T
            nrm = np.linalg.norm(A)
            if nrm > 1e-9:
                mags.add(round(nrm, 9)); any_nonzero = True
        hit += any_nonzero
    # --- scalar graded response Q
    qvals, qhit = set(), 0
    qforced_pred, qforced_viol = 0, 0
    per_edge_max = {}
    for (x, y) in selfrev:
        best = 0
        revs = [g for g in AUT if frozenset(g[e] for e in x) == y and frozenset(g[e] for e in y) == x]
        for c in cuts:
            q = Q(c, x, y)
            if q != 0:
                qvals.add(abs(q))
            best = max(best, abs(q))
            if any(stabilizes(g, c) for g in revs):
                qforced_pred += 1
                if q != 0:
                    qforced_viol += 1
        per_edge_max[(x, y)] = best
        qhit += best > 0
    print(f"\n--- {tag} (m={m}, {len(cuts)} cuts, {len(ocuts)} oriented) ---")
    print(f"  A = C-C^T : nonzero Frobenius magnitudes  = {sorted(mags)}")
    print(f"              self-reversing edges with some nonzero response = {hit}/24")
    print(f"  Q = d(psi): nonzero |Q| values            = {sorted(qvals)}")
    print(f"              self-reversing edges with some nonzero Q        = {qhit}/24")
    print(f"              symmetry-forced (cut stabilised by a reverser)  = {qforced_pred} pairs, "
          f"violations = {qforced_viol}")
    # stratify by source vertex orbit
    strat = defaultdict(set)
    for (x, y), b in per_edge_max.items():
        strat[orb_of[x]].add(b)
    print(f"              max|Q| by source vertex orbit: "
          f"{ {k: sorted(v) for k, v in sorted(strat.items())} }")
    return qvals


for m in (2, 3):
    allp, bal = cut_families(m)
    report(m, bal, "BALANCED cuts")
    report(m, allp, "ALL cuts (balance dropped)")

# ---------- equivariance check on Q ----------
import random
random.seed(0)
allp3, _ = cut_families(3)
bad = 0
for _ in range(20000):
    x, y, _, _ = random.choice(dedges)
    c = random.choice(allp3)
    g = random.choice(AUT)
    gx = frozenset(g[e] for e in x); gy = frozenset(g[e] for e in y)
    gc = tuple(frozenset(g[e] for e in b) for b in c)
    if Q(c, x, y) != Q(gc, gx, gy):
        bad += 1
print(f"\nequivariance Q_l(x,y) = Q_gl(gx,gy): mismatches = {bad}/20000")
