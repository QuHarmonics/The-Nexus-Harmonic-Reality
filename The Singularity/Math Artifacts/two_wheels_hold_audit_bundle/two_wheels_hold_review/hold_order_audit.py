#!/usr/bin/env python3
"""Finite audit of order-dependent partner-pair hold and the tower mirror.

Uses wheels.py for the sealed partner/rank/hold provider, and the corpus E/G
route-code implementation. Generic order profiles are checked by a separate
streaming seen/unseen-pair counter, not by wheels.hold().
"""
from __future__ import annotations
import csv, hashlib, importlib.util, json, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT))
import wheels as wh
spec = importlib.util.spec_from_file_location('routeaudit', ROOT / 'nexus_route_rank_sphere_audit.py')
routeaudit = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = routeaudit
spec.loader.exec_module(routeaudit)

start = time.perf_counter()

def partner(x: int, n: int) -> int:
    return wh.P(x, n)

def is_pal(x: int, n: int) -> bool:
    return wh.J(x, n) == x

def canonical(x: int, n: int) -> int:
    return min(x, partner(x, n))

def hold_profile(order: list[int], n: int) -> tuple[list[int], dict]:
    N = 1 << n
    assert len(order) == N and set(order) == set(range(N)), f'not a permutation n={n}'
    seen = bytearray(N)
    h = 0
    prof = [0]
    for x in order:
        p = partner(x, n)
        if seen[p]:
            h -= 1
        else:
            h += 1
        seen[x] = 1
        prof.append(h)
    assert h == 0 and all(seen), f'not closed n={n}, final={h}'
    mx = max(prof)
    meta = {
        'width': n, 'items': N, 'max_hold': mx,
        'first_t_at_max': prof.index(mx),
        'all_t_at_max': [i for i, v in enumerate(prof) if v == mx],
        'hold_at_seam_t_N_over_2': prof[N // 2],
        'sum_H_t_t1_to_N': sum(prof[1:]),
        'mean_over_N': sum(prof[1:]) / N,
    }
    return prof, meta

all_profiles = []
order_profile_values = {}
summary = {'status': 'RUNS', 'orders': {}, 'scope': {}, 'checks': {}, 'tower_mirror': {}}
order_defs = {
    'address': 'R_n[address]',
    'value_counter': 'integer values 0..2^n-1',
    'sheet': 'fixed-width words after reverse(all bits of address tape) then complement',
    'route_code': 'sort by side-bit || canonical E/G route code',
    'half_table_pair_lift': 'increasing canonical half_index; emit representative then partner',
}
for n in range(2, 13):
    N = 1 << n
    _, _, _, R_np, loc = wh.ring_arrays(n)
    R = [int(x) for x in R_np]
    orders = {}
    orders['address'] = R
    orders['value_counter'] = list(range(N))
    tape = ''.join(format(x, f'0{n}b') for x in R)
    sheet_bits = ''.join('1' if bit == '0' else '0' for bit in tape[::-1])
    orders['sheet'] = [int(sheet_bits[i:i+n], 2) for i in range(0, len(sheet_bits), n)]
    route_pairs = [(int(routeaudit.encode_route(format(x, f'0{n}b')), 2), x) for x in range(N)]
    route_pairs.sort()
    assert len({code for code, _ in route_pairs}) == N, f'route-code collision width {n}'
    orders['route_code'] = [x for _, x in route_pairs]
    reps = [x for x in range(N) if x < partner(x, n)]
    # Increasing representative numeric value is increasing half-index/rank.
    pair_lift = []
    for x in reps:
        pair_lift.extend([x, partner(x, n)])
    orders['half_table_pair_lift'] = pair_lift

    for name, seq in orders.items():
        prof, meta = hold_profile(seq, n)
        order_profile_values[(n, name)] = prof
        # Every prefix is also independently checked against membership of each pair.
        # hold_profile implements that direct criterion incrementally.
        meta['order_definition'] = order_defs[name]
        if name == 'address':
            meta['address_seam_equals_half_ring'] = (prof[N//2] == N//2 and meta['max_hold'] == N//2)
            assert meta['address_seam_equals_half_ring'], (n, meta)
        elif name == 'value_counter':
            provider = [wh.hold(t, n) for t in range(N + 1)]
            meta['matches_wheels_hold_every_prefix'] = (prof == provider)
            hp = 1 << ((n + 1)//2 - 1)
            pred_peak = (1 << (n - 2)) + hp
            meta['peak_prediction'] = pred_peak
            meta['matches_sealed_peak'] = (meta['max_hold'] == pred_peak and meta['first_t_at_max'] == N//2)
            assert meta['matches_wheels_hold_every_prefix'] and meta['matches_sealed_peak'], (n, meta)
        elif name == 'route_code':
            meta['route_code_seam_equals_half_ring'] = (prof[N//2] == N//2 and meta['max_hold'] == N//2)
            assert meta['route_code_seam_equals_half_ring'], (n, meta)
        elif name == 'half_table_pair_lift':
            meta['adjacent_pair_peak_is_one'] = (meta['max_hold'] == 1 and prof[1::2] == [1] * (N//2) and prof[2::2] == [0] * (N//2))
            assert meta['adjacent_pair_peak_is_one'], (n, meta)
        summary['orders'].setdefault(name, []).append(meta)
        for t, hold in enumerate(prof):
            all_profiles.append({'width': n, 'order': name, 't': t, 'hold': hold})
profile_equivalence = {'address_sheet_equal': True, 'address_route_equal': True, 'address_is_triangular': True, 'widths_checked': []}
for n in range(2, 13):
    N = 1 << n
    a = order_profile_values[(n, 'address')]
    sh = order_profile_values[(n, 'sheet')]
    rt = order_profile_values[(n, 'route_code')]
    tri = [min(t, N-t) for t in range(N+1)]
    profile_equivalence['address_sheet_equal'] &= (a == sh)
    profile_equivalence['address_route_equal'] &= (a == rt)
    profile_equivalence['address_is_triangular'] &= (a == tri)
    profile_equivalence['widths_checked'].append(n)
assert profile_equivalence['address_sheet_equal'] and profile_equivalence['address_route_equal'] and profile_equivalence['address_is_triangular'], profile_equivalence
summary['checks']['address_sheet_full_profile_equal'] = profile_equivalence['address_sheet_equal']
summary['checks']['address_route_full_profile_equal'] = profile_equivalence['address_route_equal']
summary['checks']['address_sheet_route_profile_exactly_triangular'] = profile_equivalence['address_is_triangular']
summary['profile_equivalence'] = profile_equivalence
summary['scope']['order_profiles'] = {'widths': '2..12 exhaustive', 'order_count': 5, 'profile_rows': len(all_profiles), 'orders': order_defs}

with (OUT / 'hold_order_profiles.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['width','order','t','hold'])
    w.writeheader(); w.writerows(all_profiles)

# Full tower-mirror profiles. C_w(q) is counted from the partner side, excluding
# palindrome/complement pairs. For each low width, cache the cumulative count.
tower_rows = []
tower_check_count = 0
tower_formula_misses = []
tower_direct_count = 0
tower_direct_misses = []
low_prefix = {}
for w in range(1, 17):
    arr = [0]
    c = 0
    for x in range(1 << w):
        if x > partner(x, w) and not is_pal(x, w):
            c += 1
        arr.append(c)
    low_prefix[w] = arr
low_prefix[0] = [0, 0]

# Independent direct counter-order profiles for high rings up to width 16.
direct_profiles = {}
for n in range(2, 17):
    N = 1 << n
    h = 0
    p = [0]
    for x in range(N):
        h += 1 if x < partner(x, n) else -1
        p.append(h)
    direct_profiles[n] = p

for L in range(2, 17):
    T = 1 << L
    for k in range(1, L+1):
        n = L + k
        low = L - k
        counts = low_prefix[low] if low >= 1 else low_prefix[0]
        for t in range(T+1):
            q = (t + (1 << k) - 1) // (1 << k)
            c = counts[q]
            pred = t - 2*c
            got = wh.hold(t, n)
            tower_check_count += 1
            direct_match = None
            if n in direct_profiles:
                direct_match = (direct_profiles[n][t] == pred)
                tower_direct_count += 1
                if not direct_match:
                    tower_direct_misses.append({'L':L,'k':k,'n':n,'t':t,'predicted':pred,'direct':direct_profiles[n][t]})
            if got != pred:
                tower_formula_misses.append({'L':L,'k':k,'n':n,'low_width':low,'t':t,'q':q,'predicted':pred,'wheels_hold':got})
            if t in (0, 1, T//4, T//2, 3*T//4, T):
                tower_rows.append({'L':L,'k':k,'n':n,'low_width':low,'t':t,'q':q,'partner_side_count':c,'predicted':pred,'wheels_hold':got,'direct_profile_checked': direct_match is not None})
summary['tower_mirror'] = {
    'formula': 'H_(L+k)(t) = t - 2*C_(L-k)(ceil(t/2^k)); C_w(q)=#{0<=x<q: x>P_w(x), J_w(x)!=x}; C_0=0',
    'L_range': '2..16 exhaustive', 'k_range': '1..L',
    'full_profile_points_compared_to_wheels_hold': tower_check_count,
    'full_profile_points_also_compared_to_independent_stream_counter': tower_direct_count,
    'formula_misses': len(tower_formula_misses), 'direct_misses': len(tower_direct_misses),
    'formula_examples_of_misses': tower_formula_misses[:10],
    'direct_examples_of_misses': tower_direct_misses[:10],
    'sparse_rows_file': 'tower_mirror_profile_samples.csv',
}
summary['checks'] = {
    'all_order_streams_permutations': True,
    'generic_order_hold_direct_seen_partner_counter': True,
    'value_order_matches_native_hold_all_prefixes': True,
    'address_order_peak_and_seam_are_half_ring': True,
    'route_code_order_peak_and_seam_are_half_ring': True,
    'half_table_pair_lift_peak_is_one': True,
    'tower_mirror_formula_no_misses': len(tower_formula_misses) == 0,
    'tower_mirror_independent_direct_no_misses': len(tower_direct_misses) == 0,
}
summary['scope']['tower_mirror'] = {'L': '2..16', 'k': '1..L', 't': 'every integer 0..2^L', 'points': tower_check_count}
summary['seconds'] = time.perf_counter() - start
with (OUT / 'hold_order_summary.json').open('w') as f:
    json.dump(summary, f, indent=2)
with (OUT / 'tower_mirror_profile_samples.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['L','k','n','low_width','t','q','partner_side_count','predicted','wheels_hold','direct_profile_checked'])
    w.writeheader(); w.writerows(tower_rows)
print(json.dumps({
    'status': summary['status'], 'seconds': summary['seconds'],
    'order_widths': '2..12', 'order_profile_rows': len(all_profiles),
    'order_summary': {name: [{'width':x['width'],'max_hold':x['max_hold'],'first_t_at_max':x['first_t_at_max'],'seam':x['hold_at_seam_t_N_over_2'],'mean':round(x['mean_over_N'],6)} for x in entries] for name,entries in summary['orders'].items()},
    'tower_mirror': summary['tower_mirror'], 'checks': summary['checks']
}, indent=2))
if any(not v for v in summary['checks'].values()):
    raise SystemExit('AUDIT FAILED')
