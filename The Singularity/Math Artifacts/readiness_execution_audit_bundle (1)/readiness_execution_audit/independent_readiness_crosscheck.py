"""Independent finite audit of readiness-first claims.

Reads the R2/R3/R4 flattened streams captured from the uploaded workbook and
uses a separate subset-XOR transform plus explicit observed-signature grouping.
The original sealed audit is retained alongside this independent verifier.
"""
from __future__ import annotations
import hashlib, json, math, os, statistics, time
from collections import Counter
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
ORBITS = json.load(open(os.path.join(BASE, 'workbook_orbits.json'), encoding='utf-8'))['sheets_and_cells']


def partner(w: str) -> str:
    r = w[::-1]
    return r if r != w else ''.join('1' if x == '0' else '0' for x in w)

def grow(n: int) -> list[str]:
    words = [format(i, f'0{n}b') for i in range(1 << n)]
    representatives = [w for w in words if w < partner(w)]
    ring = representatives + [partner(w) for w in reversed(representatives)]
    if n > 1:
        mid = len(ring) // 2
        ring[mid - 1], ring[mid] = ring[mid], ring[mid - 1]
    return ring

def direct_subset_xor(bits: list[int]) -> list[int]:
    """Möbius transform: out[i] = XOR_{j subset-of i} bits[j]."""
    n = len(bits)
    if n == 0 or n & (n - 1):
        raise ValueError('power-of-two block length required')
    out = [0] * n
    for mask in range(n):
        v = 0
        sub = mask
        while True:
            v ^= int(bits[sub])
            if sub == 0:
                break
            sub = (sub - 1) & mask
        out[mask] = v
    return out

def online_compile(bits: list[int]):
    stack, events = [], []
    for arrival, bit in enumerate(bits, 1):
        stack.append({'width': 1, 'coeff': [int(bit)], 'first': arrival, 'last': arrival})
        while len(stack) >= 2 and stack[-2]['width'] == stack[-1]['width']:
            right, left = stack.pop(), stack.pop()
            w = left['width']
            block = {'width': 2*w,
                     'coeff': left['coeff'] + [a ^ b for a, b in zip(left['coeff'], right['coeff'])],
                     'first': left['first'], 'last': right['last']}
            events.append({'arrival': arrival, 'width': 2*w, 'first': left['first'],
                           'dependency_last': right['last'],
                           'extra_wait': arrival - right['last']})
            stack.append(block)
        expected = [1 << j for j in range(arrival.bit_length()-1, -1, -1) if arrival >> j & 1]
        assert [b['width'] for b in stack] == expected
    # Verify every remaining block independently, rather than calling the source verifier.
    for b in stack:
        raw = list(map(int, bits[b['first']-1:b['last']]))
        assert b['coeff'] == direct_subset_xor(raw)
        assert direct_subset_xor(b['coeff']) == raw
    return stack, events

def readiness_grouped(order, n=8):
    """Readiness by explicit grouping of all completions sharing observations."""
    domain = 1 << (2*n)
    source = np.arange(domain, dtype=np.uint32)
    a = source & ((1 << n)-1)
    b = source >> n
    sums = (a + b).astype(np.uint16)
    outmask = (1 << (n+1))-1
    codes = np.zeros(domain, dtype=np.uint32)
    codes_by_event = [codes.copy()]
    for q, (operand, bitpos) in enumerate(order):
        source_bit = bitpos + n*operand
        codes |= ((source >> source_bit) & 1).astype(np.uint32) << q
        codes_by_event.append(codes.copy())
    ready = np.full((domain, n+1), -1, dtype=np.int16)
    for event, sigs in enumerate(codes_by_event):
        ngroups = 1 << event
        # Dictionary/list grouping is independent from the sealed audit's numpy.at approach.
        andout = [outmask] * ngroups
        orout = [0] * ngroups
        for idx, sig in enumerate(sigs):
            key = int(sig)
            y = int(sums[idx])
            andout[key] &= y
            orout[key] |= y
        masks = [((~(andout[g] ^ orout[g])) & outmask) for g in range(ngroups)]
        fixed_values = np.asarray(andout, dtype=np.uint16)
        settled = np.fromiter((masks[int(sig)] for sig in sigs), dtype=np.uint16, count=domain)
        fixed_per_source = fixed_values[sigs]
        for bit in range(n+1):
            pending = ready[:, bit] < 0
            newly = pending & (((settled >> bit) & 1) != 0)
            ready[newly, bit] = event
            # Every emitted bit equals the group's fixed output value, not merely the mask bit.
            assert np.all((sums[newly] & settled[newly]) == (fixed_per_source[newly] & settled[newly]))
    assert np.all(ready >= 0)
    summaries = []
    for bit in range(n+1):
        vals, counts = np.unique(ready[:, bit], return_counts=True)
        summaries.append({'output': 'carry_out' if bit == n else f'sum_bit_{bit}',
                          'min_event': int(ready[:, bit].min()),
                          'mean_event': float(ready[:, bit].mean()),
                          'max_event': int(ready[:, bit].max()),
                          'ready_before_final_input_cases': int(np.count_nonzero(ready[:, bit] < 2*n)),
                          'event_histogram': {str(int(v)): int(c) for v, c in zip(vals, counts)}})
    return ready, summaries

def main():
    start = time.perf_counter()
    # Check workbook orbit strings against the established partner/grow provider.
    orbit_checks = []
    for n, sheet in [(2, 'Ring 2!B3'), (3, 'Ring 3!B3'), (4, 'Ring 4!B3')]:
        from_workbook = ORBITS[sheet]
        generated = ''.join(grow(n))
        assert generated == from_workbook
        orbit_checks.append({'sheet_cell': sheet, 'width': n, 'length': len(from_workbook),
                             'exact_match': True, 'sha256': hashlib.sha256(from_workbook.encode()).hexdigest()})

    # All bytes round-trip via an independently implemented subset-XOR transform.
    for value in range(256):
        source_bits = [int(x) for x in format(value, '08b')]
        coded = direct_subset_xor(source_bits)
        assert direct_subset_xor(coded) == source_bits
    byte_roundtrips = 256

    # All phases/directions and permitted lengths over workbook R2/R3/R4 orbits.
    ring_spec = [('Ring 2', ORBITS['Ring 2!B3'], [8,16,32,64]),
                 ('Ring 3', ORBITS['Ring 3!B3'], [8,16,24]),
                 ('Ring 4', ORBITS['Ring 4!B3'], [8,16,32,64])]
    stream_runs = []
    for ring_name, orbit, lengths in ring_spec:
        period = len(orbit)
        for phase in range(period):
            for direction in (1, -1):
                for length in lengths:
                    bits = [int(orbit[(phase + direction*j) % period]) for j in range(length)]
                    stack, events = online_compile(bits)
                    assert all(e['extra_wait'] == 0 for e in events)
                    # Any available complete 8-bit block closes when its eighth bit arrives.
                    width8 = [e for e in events if e['width'] == 8]
                    assert width8 and width8[0]['arrival'] == 8
                    # A whole power-of-two stream has a root exactly at its final arrival.
                    if length & (length-1) == 0:
                        assert len(stack) == 1 and stack[0]['width'] == length and events[-1]['arrival'] == length
                    stream_runs.append({'ring': ring_name, 'phase': phase, 'direction': direction,
                                        'length': length, 'first_width8_closure': width8[0]['arrival'],
                                        'frontier_widths': [b['width'] for b in stack],
                                        'closure_events': len(events)})

    n = 8
    position_orders = {'LSB_first': list(range(n)),
                       'MSB_first': list(range(n))[::-1],
                       'center_out': sorted(range(n), key=lambda j: (abs(j-(n-1)/2), j))}
    arithmetic = []
    for name, positions in position_orders.items():
        order = [(operand, bitpos) for bitpos in positions for operand in (0,1)]
        ready, summaries = readiness_grouped(order, n)
        assert ready.shape == (65536, 9)
        if name == 'LSB_first':
            assert all(np.all(ready[:, bit] == 2*bit+2) for bit in range(n))
        if name == 'MSB_first':
            assert int(np.count_nonzero(ready[:, n] == 2)) == 32768
        arithmetic.append({'order': name, 'tested_pairs': 65536,
                           'mean_first_ready_event': float(ready.mean()),
                           'mean_avoidable_barrier_wait': float(2*n-ready.mean()),
                           'outputs': summaries,
                           'lsb_rule_passed': (name != 'LSB_first' or all(np.all(ready[:, bit] == 2*bit+2) for bit in range(n))),
                           'msb_carry_at_event2_cases': int(np.count_nonzero(ready[:, n] == 2))})

    result = {'scope': 'Independent exact re-run plus Ring 2/3/4 workbook orbit cross-check. Readiness uses explicit observation-signature groups over the full operand-pair domain; event count is not physical time.',
              'orbit_checks': orbit_checks,
              'byte_roundtrips': byte_roundtrips,
              'stream_runs': len(stream_runs),
              'stream_run_counts_by_ring': {name: sum(1 for row in stream_runs if row['ring']==name) for name in ['Ring 2','Ring 3','Ring 4']},
              'stream_runs': stream_runs,
              'arithmetic_orders': arithmetic,
              'seconds': time.perf_counter()-start}
    out = os.path.join(BASE, 'independent_readiness_results.json')
    with open(out, 'w', encoding='utf-8') as f: json.dump(result, f, indent=2)
    print(json.dumps({'orbit_checks': orbit_checks, 'byte_roundtrips': byte_roundtrips,
                      'stream_runs': len(stream_runs),
                      'stream_run_counts_by_ring': result['stream_run_counts_by_ring'],
                      'arithmetic': [{'order': r['order'], 'mean_first_ready_event': r['mean_first_ready_event'],
                                      'mean_avoidable_barrier_wait': r['mean_avoidable_barrier_wait'],
                                      'carry_event2': r['msb_carry_at_event2_cases']} for r in arithmetic],
                      'seconds': result['seconds']}, indent=2))
if __name__ == '__main__': main()
