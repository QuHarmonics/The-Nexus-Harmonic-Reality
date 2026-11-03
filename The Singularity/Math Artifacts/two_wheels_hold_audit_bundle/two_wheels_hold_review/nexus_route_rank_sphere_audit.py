#!/usr/bin/env python3
"""NEXUS E/G route codec, ring-rank, and abstract-sphere audit.

The E/G map is the chosen labeling:
    E_m(x) = canonical(m + x + m)
    G_m(x) = 0 + P(x) + 1 if m else 0 + x + 1
The route code has one side bit plus a canonical code.  At odd widths the
middle bit is appended; at even widths the final two bits are (value m,
outer-pair residual d).  The implementation does not materialize a large ring.
"""
from __future__ import annotations
import hashlib, json, math, random, time
from pathlib import Path

OUT = Path('/mnt/data/nexus_route_rank_sphere_audit_results.json')

def reverse_word(x: str) -> str:
    return x[::-1]

def partner(x: str) -> str:
    r = reverse_word(x)
    if r != x:
        return r
    return ''.join('1' if c == '0' else '0' for c in x)

def canonical(x: str) -> str:
    return min(x, partner(x))

def E(x: str, m: int) -> str:
    return canonical(str(m) + x + str(m))

def G(x: str, m: int) -> str:
    core = partner(x) if m else x
    return '0' + core + '1'

def insert_middle(x: str, m: int) -> str:
    assert len(x) % 2 == 0 and canonical(x) == x
    h = len(x) // 2
    y = x[:h] + str(m) + x[h:]
    assert canonical(y) == y
    return y

def encode_canonical_route(x: str) -> str:
    """Encode a canonical word in L-1 bits under the E/G labeling."""
    L = len(x)
    if canonical(x) != x:
        raise ValueError('canonical word required')
    if L == 2:
        if x == '00': return '0'
        if x == '01': return '1'
        raise AssertionError('unexpected width-two representative')
    if L % 2:
        h = L // 2
        core = x[:h] + x[h+1:]
        m = int(x[h])
        assert canonical(core) == core
        return encode_canonical_route(core) + str(m)

    # Even target: peel the outer frame. The residual d is the final route bit.
    core = x[1:-1]
    d = int(x[0]) ^ int(x[-1])
    if d == 0:
        if x[0] == '1':
            m, parent = 1, core             # ordinary 1-core-1 branch
        elif canonical(core) == core:
            m, parent = 0, core             # 0-core-0 branch
        else:
            m, parent = 1, partner(core)     # palindrome/complement exception
    else:
        # Canonical mixed frame is 0...1. The core face supplies m.
        if canonical(core) == core:
            m, parent = 0, core
        else:
            m, parent = 1, partner(core)
    assert canonical(parent) == parent
    target = E(parent, m) if d == 0 else G(parent, m)
    assert target == x, (x, parent, m, d, target)
    return encode_canonical_route(parent) + str(m) + str(d)

def decode_canonical_route(code: str, L: int) -> str:
    """Invert an (L-1)-bit canonical route code to its word."""
    if len(code) != L - 1:
        raise ValueError(f'route length {len(code)} does not match word width {L}')
    if any(ch not in '01' for ch in code):
        raise ValueError('route code must be binary')
    if L == 2:
        return '00' if code == '0' else '01'
    if L % 2:
        parent = decode_canonical_route(code[:-1], L-1)
        return insert_middle(parent, int(code[-1]))
    parent = decode_canonical_route(code[:-2], L-2)
    m, d = int(code[-2]), int(code[-1])
    return E(parent, m) if d == 0 else G(parent, m)

def encode_route(x: str) -> str:
    """Full L-bit route address: side bit + canonical route code."""
    c = canonical(x)
    side = '0' if x == c else '1'
    return side + encode_canonical_route(c)

def decode_route(route: str) -> str:
    L = len(route)
    if L < 2 or any(ch not in '01' for ch in route):
        raise ValueError('route must be a binary string of width >= 2')
    side = int(route[0])
    c = decode_canonical_route(route[1:], L)
    return partner(c) if side else c

def rank_below(t: int, L: int) -> int:
    """Count canonical representatives x with integer value x < t, any L>=2.

    Mirrored-pair digit DP tracks x<t, x<reverse(x), and the first bit used
    to break the palindrome/complement branch. Odd widths handle the center
    digit explicitly.
    """
    if t <= 0: return 0
    if t >= (1 << L): return 1 << (L-1)
    bound = format(t, f'0{L}b')
    h = L // 2
    # state: (comparison of high prefix, comparison of low suffix,
    #         comparison with reversal, first digit) -> multiplicity
    states = {(0, 0, 0, -1): 1}
    cmp = lambda a, b: (a > b) - (a < b)
    for i in range(h):
        nxt = {}
        for (cl, cr, cj, first), count in states.items():
            for a in (0, 1):
                for c in (0, 1):
                    key = (
                        cl or cmp(a, int(bound[i])),
                        cmp(c, int(bound[L-1-i])) or cr,
                        cj or cmp(a, c),
                        a if i == 0 else first,
                    )
                    nxt[key] = nxt.get(key, 0) + count
        states = nxt
    total = 0
    if L % 2 == 0:
        for (cl, cr, cj, first), count in states.items():
            if (cl or cr) < 0 and (cj < 0 or (cj == 0 and first == 0)):
                total += count
    else:
        center_bound = int(bound[h])
        for (cl, cr, cj, first), count in states.items():
            if not (cj < 0 or (cj == 0 and first == 0)):
                continue
            for m in (0, 1):
                if (cl or cmp(m, center_bound) or cr) < 0:
                    total += count
    return total

def physical_canonical_position(q: int, L: int) -> int:
    M = 1 << (L-1)
    return M if q == 0 else M - 1 - q

def ring_position_from_route(route: str) -> int:
    L = len(route)
    side = int(route[0])
    rep = decode_canonical_route(route[1:], L)
    ascending_rank = rank_below(int(rep, 2), L)
    q = (1 << (L-1)) - 1 - ascending_rank
    p = physical_canonical_position(q, L)
    return ((1 << L) - 1 - p) if side else p

def word_at_rank(rank: int, L: int) -> str:
    """Unrank canonical representative by binary-searching rank_below."""
    M = 1 << (L-1)
    if not (0 <= rank < M): raise ValueError('rank outside representative set')
    lo, hi = 0, (1 << L) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if rank_below(mid + 1, L) > rank:
            hi = mid
        else:
            lo = mid + 1
    word = format(lo, f'0{L}b')
    assert canonical(word) == word
    assert rank_below(lo, L) == rank
    return word

def word_at_physical_position(pos: int, L: int) -> str:
    N, M = 1 << L, 1 << (L-1)
    if not (0 <= pos < N): raise ValueError('position outside ring')
    if pos == M:
        rank, side = M-1, 0       # largest rep moved by center swap
    elif pos == M-1:
        rank, side = M-1, 1       # partner of largest rep
    elif pos < M-1:
        rank, side = pos, 0
    else:
        rank, side = N-1-pos, 1
    rep = word_at_rank(rank, L)
    return partner(rep) if side else rep

def block_offset_even(x: str) -> int:
    """Descending representative offset from the block law, for even L."""
    L = len(x)
    if L % 2: raise ValueError('even width required')
    h = L // 2
    H = 1 << h
    A, B = int(x[:h], 2), int(x[h:], 2)
    K = H - 1 - A
    D = K*(K-1)//2 + max(0, K - H//2)
    def rev_h(b: int) -> int:
        return int(format(b, f'0{h}b')[::-1], 2)
    i = sum(1 for b in range(B+1, H)
            if rev_h(b) > A or (rev_h(b) == A and A < H//2))
    return D + i

def weight(x: str) -> int:
    return x.count('1')

def latitude(x: str) -> float:
    return weight(x) - len(x)/2

def sphere_step_audit() -> dict:
    results = []
    total_odd = total_even = flips = 0
    for L in range(2, 19, 2):
        reps = []
        for v in range(1 << L):
            x = format(v, f'0{L}b')
            if canonical(x) == x:
                reps.append(x)
        odd_count, even_count, fail_odd, fail_even, flip_count = 0, 0, [], [], 0
        for x in reps:
            pal = (x == x[::-1])
            h = L//2
            for m in (0, 1):
                y = insert_middle(x, m)
                pred_odd = latitude(x) + (m - 0.5)
                if abs(latitude(y) - pred_odd) > 1e-12:
                    fail_odd.append((x,m,y,pred_odd,latitude(y)))
                odd_count += 1
                for d in (0, 1):
                    child = E(x,m) if d == 0 else G(x,m)
                    s = -1 if (pal and m == 1) else 1
                    predicted = s * (latitude(y) + (m - 0.5) * ((-1) ** d))
                    if abs(latitude(child) - predicted) > 1e-12:
                        fail_even.append((x,m,d,y,child,predicted,latitude(child),s))
                    even_count += 1
                    flip_count += (s == -1)
        expected_pal_reps = 1 << (L//2 - 1)
        assert not fail_odd, (L, fail_odd[:3])
        assert not fail_even, (L, fail_even[:3])
        assert sum(x == x[::-1] for x in reps) == expected_pal_reps
        assert flip_count == 2 * expected_pal_reps
        results.append({
            'source_even_width': L,
            'canonical_sources': len(reps),
            'odd_step_children_checked': odd_count,
            'odd_step_failures': len(fail_odd),
            'E_G_even_step_children_checked': even_count,
            'E_G_even_step_failures': len(fail_even),
            'canonical_palindrome_cores': expected_pal_reps,
            'sign_flip_transitions': flip_count,
            'all_checks_pass': True,
        })
        total_odd += odd_count
        total_even += even_count
        flips += flip_count
    return {'per_width': results, 'odd_children_total': total_odd,
            'E_G_children_total': total_even, 'sign_flip_transitions_total': flips}

def main() -> dict:
    started = time.perf_counter()
    rng = random.Random(20261020)
    rank_checks, route_checks, position_checks, block_checks = [], [], [], []

    # Exhaustive route codec, canonical code bijection, and rank/position.
    for L in range(2, 19):
        M = 1 << (L-1)
        seen = set()
        canonical_words = []
        for v in range(1 << L):
            x = format(v, f'0{L}b')
            if canonical(x) != x: continue
            code = encode_canonical_route(x)
            assert len(code) == L-1
            assert decode_canonical_route(code, L) == x
            assert code not in seen
            seen.add(code)
            canonical_words.append(x)
            # Each final route bit is a direct value/residual readout.
            if L >= 4 and L % 2 == 0:
                d = int(x[0]) ^ int(x[-1])
                assert int(code[-1]) == d
        assert len(seen) == M
        # Every possible canonical-route code is represented exactly once.
        assert seen == {format(v, f'0{L-1}b') for v in range(M)}
        route_checks.append({'width': L, 'canonical_words': M,
                             'route_code_bits': L-1, 'bijection': True})

        if L <= 12:
            for x in canonical_words:
                numeric = int(x, 2)
                asc_rank = rank_below(numeric, L)
                q = M - 1 - asc_rank
                pos = physical_canonical_position(q, L)
                assert word_at_rank(asc_rank, L) == x
                route = '0' + encode_canonical_route(x)
                assert ring_position_from_route(route) == pos
            # Compare rank DP against independent sorted enumeration.
            for asc_rank, x in enumerate(canonical_words):
                assert rank_below(int(x,2), L) == asc_rank
            rank_checks.append({'width': L, 'canonical_words': M,
                                'rank_count_vs_sorted_list': True,
                                'rank_unrank_roundtrips': M})

        # Physical ring and partner-address reflection; test all words at widths <=10.
        if L <= 10:
            reps = canonical_words
            ring = reps + [partner(x) for x in reps[::-1]]
            ring[M-1], ring[M] = ring[M], ring[M-1]
            assert len(set(ring)) == (1 << L)
            for i, x in enumerate(ring):
                assert ring[(1 << L)-1-i] == partner(x)
                full_route = encode_route(x)
                assert decode_route(full_route) == x
                assert ring_position_from_route(full_route) == i
                assert word_at_physical_position(i, L) == x
            position_checks.append({'width': L, 'all_ring_positions': 1 << L,
                                    'partner_reflection': True,
                                    'route_to_position': True,
                                    'position_to_word': True})

        if L in (2,4,6,8,10,12):
            if L % 2 == 0:
                for x in canonical_words:
                    offset = block_offset_even(x)
                    q = M - 1 - rank_below(int(x,2),L)
                    assert offset == q, (L,x,offset,q)
                block_checks.append({'width':L,'representatives':M,
                                     'mixed_block_formula_matches_rank':True})

    # Direct high-width route and scalar rank queries without ring materialization.
    wide_checks = []
    for L in (64, 256, 512):
        xval = rng.getrandbits(L)
        x = format(xval, f'0{L}b')
        code = encode_route(x)
        assert len(code) == L and decode_route(code) == x
        rep = canonical(x)
        rank = rank_below(int(rep,2),L)
        M = 1 << (L-1)
        q = M - 1 - rank
        pos0 = physical_canonical_position(q,L)
        pos = (1 << L)-1-pos0 if x != rep else pos0
        assert 0 <= rank < M and 0 <= pos < (1 << L)
        # Inverse reader at the route-derived address confirms the round trip.
        assert word_at_physical_position(pos,L) == x
        zroute = latitude(x)
        assert zroute == weight(x)-L/2
        wide_checks.append({'width':L,'route_bits':len(code),'route_roundtrip':True,
                            'rank_computed_without_ring_array':True,
                            'address_roundtrip':True,'latitude_readout':zroute})

    # Literal angular geometry: partner address is reflection, not the antipodal slot.
    geometry = []
    for L in range(2, 9):
        N = 1 << L
        pos = 0
        partner_pos = N-1-pos
        antipode_pos = (pos + N//2) % N
        theta = 2*math.pi*(pos+0.5)/N
        theta_partner = 2*math.pi*(partner_pos+0.5)/N
        assert abs((theta_partner + theta) % (2*math.pi)) < 1e-12 or abs((theta_partner + theta) - 2*math.pi) < 1e-12
        assert partner_pos != antipode_pos
        geometry.append({'width':L,'example_position':pos,
                         'partner_position':partner_pos,
                         'true_half_turn_position':antipode_pos,
                         'partner_is_half_turn':False,
                         'slot_center_angle_maps_to_reflection':True})

    # Partner preserves weight off the palindrome branch and reverses latitude on it.
    partner_checks=[]
    for L in range(2, 13):
        checked = 0
        for v in range(1 << L):
            x = format(v, f'0{L}b')
            p = partner(x)
            assert len(p) == L
            if x == x[::-1]:
                assert abs(latitude(p) + latitude(x)) < 1e-12
            else:
                assert abs(latitude(p) - latitude(x)) < 1e-12
            checked += 1
        partner_checks.append({'width':L,'words':checked,
                               'weight_latitude_law':True})

    sphere = sphere_step_audit()
    result = {
        'title': 'NEXUS E/G route-rank and sphere-lift audit',
        'status': 'PASS for finite checks stated below; geometric interpretation qualified',
        'route_definition': 'Full route = side bit + canonical route. At odd widths append middle value m. At even widths append outer residual d to prior middle-value code; canonical route final pair is (m,d).',
        'route_to_word': route_checks,
        'rank_count_checks': rank_checks,
        'block_offset_checks': block_checks,
        'physical_ring_checks': position_checks,
        'wide_scalar_checks': wide_checks,
        'partner_latitude_checks': partner_checks,
        'sphere_lift': sphere,
        'geometry_qualification': 'With evenly spaced slot-center azimuth theta_i=2*pi*(i+1/2)/2^L and ring law pos(P(x))=2^L-1-pos(x), the partner map acts as theta -> 2*pi-theta (azimuthal reflection), not theta -> theta+pi (a half-turn). Palindrome partners also flip z to -z, but are not generally the geometric sphere antipode unless azimuth convention is redefined.',
        'elapsed_seconds': time.perf_counter()-started,
    }
    OUT.write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
    return result

if __name__ == '__main__':
    main()
