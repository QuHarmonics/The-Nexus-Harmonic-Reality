"""State the rule found on (C6, K=3), then falsify it on new arenas.

RULE (candidate):  a graded reader response exists  <=>  m >= 3  AND  max block size >= K.
Below K is the token count; m the number of reader blocks.
Criterion is choice-free: count directional reader type-classes on self-reversing edges.
"""
import itertools
from collections import defaultdict


def build(base_adj, N, K):
    verts = [frozenset(s) for s in itertools.combinations(range(N), K)]
    dedges = []
    for x in verts:
        for u in x:
            for w in base_adj[u]:
                if w not in x:
                    dedges.append((x, frozenset((x - {u}) | {w}), u, w))
    return verts, dedges


def aut_cycle(N):
    return [tuple((i + k) % N for i in range(N)) for k in range(N)] + \
           [tuple((k - i) % N for i in range(N)) for k in range(N)]


def aut_hypercube(n):
    """Aut(Q_n) = hyperoctahedral: coordinate permutations x bit flips, order n! 2^n."""
    V = 1 << n
    g = []
    for perm in itertools.permutations(range(n)):
        for mask in range(V):
            img = []
            for v in range(V):
                w = 0
                for i in range(n):
                    if (v >> i) & 1:
                        w |= 1 << perm[i]
                img.append(w ^ mask)
            g.append(tuple(img))
    return g


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


def selfrev_edges(dedges, AUT):
    out = []
    for (x, y, _, _) in set((a, b, 0, 0) for a, b, _, _ in dedges):
        pass
    seen = set((x, y) for x, y, _, _ in dedges)
    for (x, y) in seen:
        if any(frozenset(g[e] for e in x) == y and frozenset(g[e] for e in y) == x for g in AUT):
            out.append((x, y))
    return out


def directional_classes(cuts, edges):
    cls = set()
    for c in cuts:
        for (x, y) in edges:
            t = tuple(sorted((len(b & x), len(b & y)) for b in c))
            r = tuple(sorted((b, a) for (a, b) in t))
            if t != r:
                cls.add(min(t, r))
    return cls


def run(name, base_adj, N, K, AUT, ms):
    verts, dedges = build(base_adj, N, K)
    sr = selfrev_edges(dedges, AUT)
    print(f"\n### {name}:  N={N} K={K}  V={len(verts)} E_dir={len(dedges)} "
          f"|Aut|={len(AUT)} self-reversing={len(sr)}")
    if not sr:
        print("   no self-reversing edges - skipped")
        return
    for m in ms:
        allp = sorted(set(tuple(sorted(p, key=lambda b: sorted(b)))
                          for p in partitions_into(range(N), m)),
                      key=lambda p: [sorted(b) for b in p])
        byprof = defaultdict(list)
        for c in allp:
            byprof[tuple(sorted(len(b) for b in c))].append(c)
        for prof, cuts in sorted(byprof.items()):
            d = directional_classes(cuts, sr)
            pred = "GRADED" if (m >= 3 and max(prof) >= K) else "SIGN"
            obs = "GRADED" if len(d) >= 2 else "SIGN"
            flag = "ok " if pred == obs else "*** MISMATCH ***"
            print(f"   m={m} profile {str(prof):<14} directional classes={len(d)}  "
                  f"predicted={pred:<6} observed={obs:<6} {flag}")


C6 = {v: {(v - 1) % 6, (v + 1) % 6} for v in range(6)}
C8 = {v: {(v - 1) % 8, (v + 1) % 8} for v in range(8)}
Q3 = {v: {v ^ (1 << i) for i in range(3)} for v in range(8)}

if __name__ == "__main__":

    run("C6 arena, K=3 (calibration)", C6, 6, 3, aut_cycle(6), [2, 3, 4])
    run("C6 arena, K=2 (new)", C6, 6, 2, aut_cycle(6), [2, 3, 4])
    run("C8 arena, K=3 (new)", C8, 8, 3, aut_cycle(8), [3, 4])
    run("Q3 arena, K=3 (new)", Q3, 8, 3, aut_hypercube(3), [3, 4])

    print("\n" + "="*72)
    print("SHARPEST TEST: hold the arena fixed, vary K, and see whether a previously-SIGN")
    print("profile flips to GRADED exactly when max block size reaches K.")
    print("(criterion evaluated on ALL directed edges, since some (X,K) have no self-reversing edges)")
def run_all(name, base_adj, N, K, AUT, ms):
    verts, dedges = build(base_adj, N, K)
    edges = sorted(set((x,y) for x,y,_,_ in dedges), key=lambda p:(sorted(p[0]),sorted(p[1])))
    sr = selfrev_edges(dedges, AUT)
    print(f"\n### {name}: N={N} K={K} V={len(verts)} E_dir={len(dedges)} self-rev={len(sr)}")
    for m in ms:
        allp = sorted(set(tuple(sorted(p, key=lambda b: sorted(b))) for p in partitions_into(range(N), m)),
                      key=lambda p:[sorted(b) for b in p])
        byprof = defaultdict(list)
        for c in allp: byprof[tuple(sorted(len(b) for b in c))].append(c)
        for prof, cuts in sorted(byprof.items()):
            d = directional_classes(cuts, edges)
            pred = "GRADED" if (m>=3 and max(prof)>=K) else "SIGN"
            obs  = "GRADED" if len(d)>=2 else "SIGN"
            print(f"   m={m} profile {str(prof):<14} classes={len(d)} predicted={pred:<6} observed={obs:<6} "
                  f"{'ok ' if pred==obs else '*** MISMATCH ***'}")
    run_all("C8, K=2", C8, 8, 2, aut_cycle(8), [3,4])
    run_all("C8, K=3", C8, 8, 3, aut_cycle(8), [3,4])
    run_all("C8, K=4", C8, 8, 4, aut_cycle(8), [3,4])
