"""Derive across-read forbidden prefixes from exact angular slice overlap.

Unlike global-cut/midpoint enumeration, this propagates the admissible angular
intervals for each reachable profile prefix, one ring at a time. A child bit is
forbidden exactly when none of that ring's half-open slice intervals overlaps
any interval admitted by its parent prefix.
"""
from fractions import Fraction
from math import ceil


def partner(x):
    r = x[::-1]
    return r if r != x else ''.join('1' if c == '0' else '0' for c in x)


def grow(L):
    seen, pairs = set(), []
    for w in range(1 << L):
        x = format(w, f'0{L}b')
        if x in seen:
            continue
        p = partner(x)
        seen |= {x, p}
        pairs.append((x, p))
    seq = []
    for i, (a, b) in enumerate(pairs):
        if i == len(pairs) - 1 and len(pairs) > 1:
            a, b = b, a
        m = len(seq) // 2
        seq = seq[:m] + [a, b] + seq[m:]
    return seq


def merge(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals)
    out = [list(intervals[0])]
    for a, b in intervals[1:]:
        if a <= out[-1][1]:
            if b > out[-1][1]:
                out[-1][1] = b
        else:
            out.append([a, b])
    return [(a, b) for a, b in out]


def exact_boundary_derivation(top=10):
    rings = [''.join(grow(L)) for L in range(1, top + 1)]
    # Prefix -> disjoint half-open angular intervals on which that prefix occurs.
    live = {'': [(Fraction(0), Fraction(1))]}
    minimal_forbidden = []
    counts = []

    for depth, bits in enumerate(rings, start=1):
        S = len(bits)
        nxt = {}
        for prefix, intervals in live.items():
            observed = set()
            for a, b in intervals:
                # Positive-width overlaps only. Slice j is [j/S, (j+1)/S).
                first = (a.numerator * S) // a.denominator
                last_exclusive = (b.numerator * S + b.denominator - 1) // b.denominator
                for j in range(first, min(last_exclusive, S)):
                    left = max(a, Fraction(j, S))
                    right = min(b, Fraction(j + 1, S))
                    if left >= right:
                        continue
                    bit = bits[j]
                    observed.add(bit)
                    nxt.setdefault(prefix + bit, []).append((left, right))
            # Any missing child has no overlap with this ring's slice boundaries.
            for bit in '01':
                if bit not in observed:
                    minimal_forbidden.append(prefix + bit)
        live = {p: merge(iv) for p, iv in nxt.items()}
        counts.append((depth, len(live), 2**depth - len(live), sum(map(len, live.values()))))
    return rings, live, minimal_forbidden, counts


def independent_global_cut_check(rings):
    cuts = sorted({Fraction(k, len(s)) for s in rings for k in range(len(s))} | {Fraction(1)})
    profiles = set()
    for a, b in zip(cuts[:-1], cuts[1:]):
        t = (a + b) / 2
        profiles.add(''.join(s[(t.numerator * len(s)) // t.denominator] for s in rings))
    return profiles, len(cuts) - 1

if __name__ == '__main__':
    rings, live, minimal, counts = exact_boundary_derivation(10)
    minimal = sorted(minimal, key=lambda p: (len(p), p))
    print('EXACT BOUNDARY-OVERLAP DERIVATION')
    print('No global union of all ring cuts is built. Prefix intervals are propagated one ring at a time.')
    print('depth | reachable prefixes | absent prefixes | live interval pieces')
    for d, n, absent, pieces in counts:
        print(f'{d:5d} | {n:18d} | {absent:15d} | {pieces:19d}')
    print(f'Final reachable profiles: {len(live)} of {2**len(rings)}')
    print(f'Minimal forbidden prefixes (derived at first empty child overlap): {len(minimal)}')
    for p in minimal:
        print(f'{p:10s} depth={len(p)}')
    scanned, cells = independent_global_cut_check(rings)
    derived_full = set(live)
    expected_minimal = []
    for p in sorted({format(i, f'0{len(rings)}b') for i in range(2**len(rings))} - scanned, key=lambda p:(len(p),p)):
        if p[:-1] in {''} or p[:-1] in {q[:len(p)-1] for q in scanned}:
            expected_minimal.append(p)
    print(f'Independent global-cut check: {len(cells) if isinstance(cells, list) else cells} angular cells, {len(scanned)} profiles')
    print(f'All final profiles agree with independent check: {derived_full == scanned}')
    # Minimal forbidden prefixes from independent profile inventory.
    prefix_sets = [{p[:d] for p in scanned} for d in range(1, len(rings)+1)]
    prev = {''}
    min2 = []
    for d, have in enumerate(prefix_sets, start=1):
        for p in sorted({format(i, f'0{d}b') for i in range(2**d)} - have):
            if p[:-1] in prev:
                min2.append(p)
        prev = have
    print(f'All minimal forbidden prefixes agree with independent check: {set(minimal) == set(min2)}')
