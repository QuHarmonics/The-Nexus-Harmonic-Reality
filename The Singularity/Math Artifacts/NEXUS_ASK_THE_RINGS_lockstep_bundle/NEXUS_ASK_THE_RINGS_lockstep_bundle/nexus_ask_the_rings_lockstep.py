#!/usr/bin/env python3
"""NEXUS §126: ask the WP5 reader/field rings for the lockstep joint orbit.

Standard-library only. Reconstructs the WP5 partial-lane eligibility and CRT split;
then compares the original rational-ring lean with the paired (alpha,beta) orbit and
with the counterfactual full Cartesian product. No SHA/de Bruijn edge readout is used.
"""
from __future__ import annotations
import hashlib, json, math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
PRED_FILE = HERE / 'NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.txt'
PRED_SHA_FILE = HERE / 'NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.sha256'
PRED_SHA = hashlib.sha256(PRED_FILE.read_bytes()).hexdigest()
expected_sha = PRED_SHA_FILE.read_text().split()[0]
if PRED_SHA != expected_sha:
    raise SystemExit('prediction seal mismatch before run')


def odd_part(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def ring_orbit(x0: int, m: int) -> list[int]:
    """Orbit under multiplication by 16 mod m, preserving exact start and order."""
    if m <= 1:
        return [0]
    x = x0 % m
    out = []
    seen = set()
    while x not in seen:
        seen.add(x)
        out.append(x)
        x = (x * 16) % m
    if x != x0 % m:
        raise AssertionError('orbit entered a cycle not containing its start')
    return out


def ord16(m: int) -> int:
    """Multiplicative order of 16 in Z/mZ for odd m>1; trivial ring period is 1."""
    if m <= 1:
        return 1
    x = 16 % m
    k = 1
    while x != 1:
        x = (x * 16) % m
        k += 1
        if k > 10_000_000:
            raise RuntimeError(f'order search exceeded limit at modulus {m}')
    return k


def frac(x: Fraction) -> str:
    return f'{x.numerator}/{x.denominator}' if x.denominator != 1 else str(x.numerator)


def make_lane(k: int, j: int, a: int) -> dict | None:
    d = 8 * k + j
    o = odd_part(d)
    if o <= 1:
        return None
    h = ord16(o)
    orbit_o = ring_orbit(1, o)
    # WP5's partial-inversion eligibility filter.
    if h % 2 or (o - 1) in orbit_o:
        return None
    eps = pow(16, h // 2, o)
    o1 = math.gcd(eps - 1, o)
    o2 = o // o1
    if o1 <= 1 or o2 <= 1:
        # Keep the typing explicit; the current WP5 set should not reach this case.
        return None
    h1, h2 = ord16(o1), ord16(o2)
    g = math.gcd(h1, h2)
    y_orbit = ring_orbit(a % o, o)
    mu = Fraction(sum(y_orbit), len(y_orbit) * o)

    inv_o2_mod_o1 = pow(o2, -1, o1)
    inv_o1_mod_o2 = pow(o1, -1, o2)
    joint = []
    for t, y in enumerate(y_orbit):
        alpha = Fraction((y * inv_o2_mod_o1) % o1, o1)
        beta = Fraction((y * inv_o1_mod_o2) % o2, o2)
        joint.append({'t': t, 'y': y, 'alpha': alpha, 'beta': beta})
    joint_lean = sum((z['alpha'] - (1 if z['beta'] < z['alpha'] else 0) for z in joint), Fraction(0)) / len(joint)
    target_lean = mu - Fraction(1, 2)

    # Marginals and the counterfactual Cartesian-product readout.
    alpha_ring = [Fraction((x * inv_o2_mod_o1) % o1, o1) for x in ring_orbit(a % o1, o1)]
    beta_ring = [Fraction((x * inv_o1_mod_o2) % o2, o2) for x in ring_orbit(a % o2, o2)]
    # ring_orbit(a,o1) is equivalent to a*i2 mod o1 under multiplication by 16;
    # similarly for beta. The CRT inverses re-scale the residue to alpha,beta.
    if len(alpha_ring) != h1 or len(beta_ring) != h2:
        raise AssertionError(f'parent period mismatch for d={d}: {len(alpha_ring)}/{h1}, {len(beta_ring)}/{h2}')
    product_lean = sum((aa - (1 if bb < aa else 0) for aa in alpha_ring for bb in beta_ring), Fraction(0)) / (len(alpha_ring) * len(beta_ring))

    # Phase-state reconstruction. The reachable phase pairs are (t mod h1,t mod h2).
    phase_pairs = [(z['t'] % h1, z['t'] % h2) for z in joint]
    expected_joint_period = math.lcm(h1, h2)
    unique_phase_pairs = set(phase_pairs)
    phase_residue_counts = Counter(i % g for i, _ in phase_pairs)
    reachable_alpha_beta_pairs = {(z['alpha'], z['beta']) for z in joint}
    full_product_pairs = {(aa, bb) for aa in alpha_ring for bb in beta_ring}
    phase_relation_ok = all((i - j) % g == 0 for i, j in phase_pairs)
    all_compatible_phase_pairs = {(i, j) for i in range(h1) for j in range(h2) if (i - j) % g == 0}

    return {
        'k': k, 'j': j, 'a': a, 'd': d, 'o_odd_part': o, 'h_full': h,
        'o1_reader_modulus': o1, 'o2_field_modulus': o2,
        'h1_reader_period': h1, 'h2_field_period': h2, 'shared_period_factor': g,
        'classification': 'lockstep' if g > 1 else 'independent',
        'balanced': mu == Fraction(1, 2),
        'rational_ring_orbit_length': len(y_orbit),
        'joint_orbit_period_lcm': expected_joint_period,
        'joint_orbit_length_actual': len(joint),
        'joint_period_matches_lcm': len(joint) == expected_joint_period,
        'unique_phase_pairs': len(unique_phase_pairs),
        'phase_pair_relation_i_mod_g_equals_j_mod_g': phase_relation_ok,
        'compatible_phase_pairs_expected': len(all_compatible_phase_pairs),
        'phase_residue_counts_mod_g': {str(key): phase_residue_counts[key] for key in sorted(phase_residue_counts)},
        'joint_pairs_count': len(reachable_alpha_beta_pairs),
        'full_cartesian_pairs_count': len(full_product_pairs),
        'missing_cartesian_pairs': len(full_product_pairs - reachable_alpha_beta_pairs),
        'mu': frac(mu), 'direct_lean_mu_minus_half': frac(target_lean),
        'joint_orbit_lean': frac(joint_lean),
        'joint_equals_original_exactly': joint_lean == target_lean,
        'full_cartesian_counterfactual_lean': frac(product_lean),
        'cartesian_equals_joint': product_lean == joint_lean,
        'lean_difference_joint_minus_cartesian': frac(joint_lean - product_lean),
        'alpha_ring_values': [frac(x) for x in alpha_ring],
        'beta_ring_values': [frac(x) for x in beta_ring],
        'joint_orbit': [
            {'t': z['t'], 'y': z['y'], 'alpha': frac(z['alpha']), 'beta': frac(z['beta']),
             'beta_less_alpha': z['beta'] < z['alpha'],
             'lean_term': frac(z['alpha'] - (1 if z['beta'] < z['alpha'] else 0)),
             'phase_alpha': z['t'] % h1, 'phase_beta': z['t'] % h2}
            for z in joint
        ],
    }


def main() -> None:
    lane_types = ((1, 1), (4, 4), (5, 1), (6, 8))
    eligible = []
    for k in range(2001):
        for j, a in lane_types:
            lane = make_lane(k, j, a)
            if lane is not None:
                eligible.append(lane)

    balanced = [x for x in eligible if x['balanced']]
    independent = [x for x in eligible if x['shared_period_factor'] == 1]
    lockstep = [x for x in eligible if x['shared_period_factor'] > 1]
    balanced_lockstep = [x for x in balanced if x['shared_period_factor'] > 1]

    # Entire-source reconciliation and the exact claims sealed above.
    checks = {
        'eligible_partial_lanes_804': len(eligible) == 804,
        'balanced_lanes_75': len(balanced) == 75,
        'independent_lanes_692': len(independent) == 692,
        'independent_balanced_66': sum(x['balanced'] for x in independent) == 66,
        'balanced_lockstep_9': len(balanced_lockstep) == 9,
        'joint_lean_equals_original_on_all_804': all(x['joint_equals_original_exactly'] for x in eligible),
        'joint_period_equals_lcm_on_all_804': all(x['joint_period_matches_lcm'] for x in eligible),
        'phase_compatibility_formula_on_all_804': all(x['phase_pair_relation_i_mod_g_equals_j_mod_g'] and x['unique_phase_pairs'] == x['compatible_phase_pairs_expected'] for x in eligible),
        'independent_cartesian_matches_joint_on_all_independent': all(x['cartesian_equals_joint'] for x in independent),
        'balanced_lockstep_joint_lean_zero': all(Fraction(x['joint_orbit_lean']) == 0 for x in balanced_lockstep),
    }
    if not all(checks.values()):
        raise AssertionError('run invariant failed: ' + repr({k:v for k,v in checks.items() if not v}))

    result = {
        'title': 'NEXUS §126 — ASK THE RINGS: WP5 lockstep joint-orbit reconstruction',
        'prediction_sha256': PRED_SHA,
        'question': 'Do the exact paired reader/field ring orbits resolve the 9 balanced lockstep lanes left OPEN in §121?',
        'source_transformations': {
            'lane_parent': 'd=8k+j; o=odd part of d; y_t=a*16^t mod o',
            'eligibility': 'h=ord_o(16) even and o-1 is not in orbit(1,o)',
            'CRT_split': 'epsilon=16^(h/2) mod o; o1=gcd(epsilon-1,o) (reader ring), o2=o/o1 (field ring)',
            'joint_route': 'alpha_t=(y_t*(o2^-1 mod o1) mod o1)/o1; beta_t=(y_t*(o1^-1 mod o2) mod o2)/o2',
            'joint_lean': 'mean_t(alpha_t - 1[beta_t < alpha_t])',
            'period_relation': 'joint period=lcm(h1,h2); reachable phase pairs satisfy i=j mod gcd(h1,h2)',
        },
        'checks': checks,
        'counts': {
            'eligible_lanes': len(eligible), 'balanced': len(balanced),
            'independent': len(independent), 'independent_balanced': sum(x['balanced'] for x in independent),
            'lockstep_all': len(lockstep), 'balanced_lockstep': len(balanced_lockstep),
        },
        'balanced_lockstep_cases': balanced_lockstep,
        'all_lockstep_cases': lockstep,
        'balanced_independent_cases': [x for x in independent if x['balanced']],
        'aggregate': {
            'balanced_lockstep_cartesian_also_zero': sum(x['cartesian_equals_joint'] and Fraction(x['joint_orbit_lean']) == 0 for x in balanced_lockstep),
            'balanced_lockstep_cartesian_differs_from_joint': sum(not x['cartesian_equals_joint'] for x in balanced_lockstep),
            'balanced_lockstep_cartesian_lean_values': dict(Counter(x['full_cartesian_counterfactual_lean'] for x in balanced_lockstep)),
            'balanced_lockstep_joint_periods': sorted(set(x['joint_orbit_length_actual'] for x in balanced_lockstep)),
            'balanced_lockstep_shared_factors': dict(Counter(str(x['shared_period_factor']) for x in balanced_lockstep)),
        },
        'ledger': {
            'CRT pair split and exact direct mean relation': 'RUNS, 804/804',
            'independent ring-product factorization': 'RUNS, 692/692',
            'lockstep joint-phase rule': 'RUNS, all observed lockstep cases',
            'nine balanced lockstep lane cases via their actual joint orbit': 'RUNS, exact zero lean in all 9',
            'general density law for balanced partial lanes': 'OPEN; not claimed by this finite run',
        },
        'scope': 'Exact rational arithmetic for the WP5 lane family k<=2000 and four (j,a) lane types. This resolves the finite §121 lockstep link, not the separate density-of-balance problem.',
    }
    out_json = HERE / 'NEXUS_ASK_THE_RINGS_lockstep_results.json'
    out_json.write_text(json.dumps(result, indent=2) + '\n')

    lines = [
        '# NEXUS §126 — ASK THE RINGS: the WP5 lockstep link', '',
        f'Prediction SHA-256: `{PRED_SHA}`', '',
        '## Question',
        '§121 left nine balanced lanes OPEN because the reader-ring and field-ring periods share a factor. This run does not revisit §124. It reconstructs the two actual CRT parent rings and their phase-compatible joint orbit.', '',
        '## Result',
        f'Exact reconstruction passes: {sum(checks.values())}/{len(checks)} invariants.',
        f'Eligible partial lanes: {len(eligible)}; balanced: {len(balanced)}; independent: {len(independent)}; independent balanced: {sum(x["balanced"] for x in independent)}; lockstep of all kinds: {len(lockstep)}; balanced lockstep: {len(balanced_lockstep)}.',
        'The paired orbit has period `lcm(h1,h2)`, and reachable phase addresses satisfy `i ≡ j (mod gcd(h1,h2))`. Thus the joint orbit is a phase-constrained subset of the Cartesian product when the periods share a factor.',
        f'All nine balanced lockstep cases have joint lean exactly zero and exactly reproduce their original rational-ring `mu - 1/2`: {sum(x["joint_equals_original_exactly"] and Fraction(x["joint_orbit_lean"]) == 0 for x in balanced_lockstep)}/9.',
        f'Among the nine, Cartesian-product lean differs from the joint route in {sum(not x["cartesian_equals_joint"] for x in balanced_lockstep)}/9 cases. The joint phase is therefore needed for those cases; the marginal rings alone do not specify the realized pairing.', '',
        '## Nine cases',
        '| k | j | a | d | odd modulus o | o1 reader | o2 field | h1 | h2 | gcd | joint period | Cartesian lean | joint lean |',
        '|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]
    for x in balanced_lockstep:
        lines.append('| {k} | {j} | {a} | {d} | {o_odd_part} | {o1_reader_modulus} | {o2_field_modulus} | {h1_reader_period} | {h2_field_period} | {shared_period_factor} | {joint_orbit_length_actual} | {full_cartesian_counterfactual_lean} | {joint_orbit_lean} |'.format(**x))
    lines += ['', '## Route / ownership',
        'The original rational-ring orbit `y_t` is the route home. CRT projects each visited `y_t` into both parents at the same phase. For coprime periods, that synchronized walk covers every pair in the Cartesian product and the independent-ring factorization applies. For non-coprime periods, it visits only compatible phase pairs; replacing it with the full product changes the owner of the average.', '',
        'This is not an assertion that the two rings independently predict balance. The exact paired route accounts for it. The broader density-of-balance problem remains OPEN.', '',
        '## Reproduction',
        'Run `python nexus_ask_the_rings_lockstep.py` in a directory containing the two prediction seal files. Exact output is in `NEXUS_ASK_THE_RINGS_lockstep_results.json`.']
    report = HERE / 'NEXUS_ASK_THE_RINGS_lockstep_run.md'
    report.write_text('\n'.join(lines) + '\n')
    print(report.read_text())

if __name__ == '__main__':
    main()
