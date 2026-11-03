#!/usr/bin/env python3
"""
SHA-256 64-WHEEL TRANSITION ENGINE
==================================
Maps carry trajectories into 64-slot global coordinates.
Tests wheel motion models against actual SHA execution.
"""

import hashlib
import random
import math

# ============================================================
# SHA-256 CONSTANTS
# ============================================================
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

IV = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

# ============================================================
# PRIMITIVES
# ============================================================
def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def S0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def S1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def s0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def s1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

def Ch(x, y, z):
    return (x & y) ^ (~x & z) & 0xFFFFFFFF

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

# ============================================================
# CARRY RIPPLE MEASUREMENT
# ============================================================
def measure_carry_ripple(x, y):
    """
    Measure longest consecutive carry chain in x + y (mod 2^32).
    Returns dict with start_bit, end_bit, length, start_hex, end_hex.
    Returns None if no carry chain (length 0).
    """
    carry = 0
    carry_out = []
    for i in range(32):
        xi = (x >> i) & 1
        yi = (y >> i) & 1
        s = xi + yi + carry
        carry = 1 if s >= 2 else 0
        carry_out.append(carry)

    max_len = 0
    max_start = 0
    max_end = 0
    curr_len = 0
    curr_start = 0

    for i in range(32):
        if carry_out[i] == 1:
            if curr_len == 0:
                curr_start = i
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                max_start = curr_start
                max_end = i
        else:
            curr_len = 0

    if max_len == 0:
        return None

    return {
        'start_bit': max_start,
        'end_bit': max_end,
        'length': max_len,
        'start_hex': max_start // 4,
        'end_hex': max_end // 4
    }

# ============================================================
# INSTRUMENTED SHA-256 COMPRESSION
# ============================================================
def build_schedule(seed):
    """Build 64-word schedule from 16-word seed."""
    W = list(seed) + [0] * 48
    for t in range(16, 64):
        W[t] = (s1(W[t-2]) + W[t-7] + s0(W[t-15]) + W[t-16]) & 0xFFFFFFFF
    return W

def compress_instrumented(seed, h_init, custom_K=None, custom_W=None):
    """
    Run full 64-round SHA-256 compression with full instrumentation.
    custom_K: if provided, use these constants instead of K
    custom_W: if provided, use these schedule words instead of computing from seed
    """
    W = custom_W if custom_W is not None else build_schedule(seed)
    Kt = custom_K if custom_K is not None else K

    state = list(h_init)
    trace = []

    for t in range(64):
        a, b, c, d, e, f, g, h = state

        # Compute T1 and T2
        s1e = S1(e)
        ch_efg = Ch(e, f, g)
        T1 = (h + s1e + ch_efg + Kt[t] + W[t]) & 0xFFFFFFFF

        s0a = S0(a)
        maj_abc = Maj(a, b, c)
        T2 = (s0a + maj_abc) & 0xFFFFFFFF

        # Register updates
        a_new = (T1 + T2) & 0xFFFFFFFF
        e_new = (d + T1) & 0xFFFFFFFF

        # Measure carry ripples in the register-update additions
        ripple_a = measure_carry_ripple(T1, T2)
        ripple_e = measure_carry_ripple(d, T1)

        # Global coordinates: a=slots 0-7, e=slots 32-39
        if ripple_a:
            ripple_a['global_start'] = ripple_a['start_hex']
            ripple_a['global_end'] = ripple_a['end_hex']
        if ripple_e:
            ripple_e['global_start'] = 32 + ripple_e['start_hex']
            ripple_e['global_end'] = 32 + ripple_e['end_hex']

        trace.append({
            'round': t,
            'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h,
            'W': W[t],
            'K': Kt[t],
            'T1': T1,
            'T2': T2,
            'a_new': a_new,
            'e_new': e_new,
            'ripple_a': ripple_a,
            'ripple_e': ripple_e,
        })

        # Update state: [a_new, a, b, c, e_new, e, f, g]
        state = [a_new, a, b, c, e_new, e, f, g]

    # Final addition
    final_state = [(state[i] + h_init[i]) & 0xFFFFFFFF for i in range(8)]
    digest = final_state

    return digest, trace

# ============================================================
# WHEEL MODEL TESTER
# ============================================================
def test_wheel_models(trace, ripple_key, rho):
    """
    Test models A-E against actual wheel trajectory.
    ripple_key: 'ripple_a' or 'ripple_e'
    rho: rotation displacement for model E
    """
    # Extract actual global end positions for each round
    actual = [entry[ripple_key]['global_end'] if entry[ripple_key] else None 
              for entry in trace]

    models = {
        'A_length': lambda prev, curr: (prev + curr['length']) % 64 if curr else prev,
        'B_start': lambda prev, curr: (prev + curr['start_bit']) % 64 if curr else prev,
        'C_end': lambda prev, curr: (prev + curr['end_bit']) % 64 if curr else prev,
        'D_window': lambda prev, curr: (prev + (curr['end_bit'] - curr['start_bit'] + 1)) % 64 if curr else prev,
        'E_rot': lambda prev, curr: (prev + curr['length'] + rho) % 64 if curr else prev,
    }

    results = {}
    for model_name, model_fn in models.items():
        last_P = 0
        hits = 0
        total = 0

        for t in range(63):
            # Update last known position
            if actual[t] is not None:
                last_P = actual[t]

            driver = trace[t][ripple_key]
            pred_next = model_fn(last_P, driver)

            actual_next = actual[t + 1]
            if actual_next is not None:
                total += 1
                if pred_next == actual_next:
                    hits += 1
                last_P = actual_next  # update for next iteration

        results[model_name] = {
            'accuracy': hits / total if total > 0 else 0,
            'hits': hits,
            'total': total
        }

    return results

# ============================================================
# MESSAGE BLOCK BUILDERS
# ============================================================
def empty_message_seed():
    """Empty message: padding bit at W[0], length 0 in W[15]."""
    return [0x80000000] + [0] * 14 + [0]

def abc_message_seed():
    """'abc' message: 3 bytes, padded."""
    return [0x61626380] + [0] * 14 + [0x00000018]

def abd_message_seed():
    """'abd' message: 3 bytes, padded."""
    return [0x61626480] + [0] * 14 + [0x00000018]

# ============================================================
# COORDINATE VECTOR & DISTANCE
# ============================================================
def build_coordinate_vector(trace, use_a=True, use_e=True):
    """
    Build coordinate vector from trace.
    If use_a: include a-carry start and end bits.
    If use_e: include e-carry start and end bits.
    """
    vec = []
    for entry in trace:
        ra = entry['ripple_a']
        re = entry['ripple_e']
        if use_a:
            vec.append(ra['start_bit'] if ra else -1)
            vec.append(ra['end_bit'] if ra else -1)
        if use_e:
            vec.append(re['start_bit'] if re else -1)
            vec.append(re['end_bit'] if re else -1)
    return vec

def euclidean_distance(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

# ============================================================
# MAIN EXECUTION
# ============================================================
if __name__ == '__main__':
    print("=" * 72)
    print("SHA-256 64-WHEEL TRANSITION ENGINE")
    print("=" * 72)

    # Verify against hashlib
    def verify(msg, seed):
        h = hashlib.sha256(msg).hexdigest()
        digest, _ = compress_instrumented(seed, IV)
        my_hex = ''.join(f'{x:08x}' for x in digest)
        return h == my_hex

    print("\n--- Verification ---")
    print(f"empty message: {verify(b'', empty_message_seed())}")
    print(f"abc message:   {verify(b'abc', abc_message_seed())}")
    print(f"abd message:   {verify(b'abd', abd_message_seed())}")

    # Configuration: state variants and message variants
    configs = []

    # Empty message with different initial states
    for state_name, state in [
        ('all_zero', [0] * 8),
        ('all_ones', [0xFFFFFFFF] * 8),
        ('SHA_IV', list(IV)),
    ]:
        configs.append((f'{state_name}_empty', state, empty_message_seed()))

    # Random state (fixed seed for reproducibility)
    random.seed(42)
    rand_state = [random.randint(0, 0xFFFFFFFF) for _ in range(8)]
    configs.append(('random_empty', rand_state, empty_message_seed()))

    # Standard IV with different messages
    configs.append(('IV_abc', list(IV), abc_message_seed()))
    configs.append(('IV_abd', list(IV), abd_message_seed()))

    # Run all configurations with normal, K=0, W=0
    all_results = {}
    for cfg_name, state, seed in configs:
        families = {}

        # Normal
        d, tr = compress_instrumented(seed, state)
        families['normal'] = {'digest': d, 'trace': tr}

        # K = 0
        d_k0, tr_k0 = compress_instrumented(seed, state, custom_K=[0]*64)
        families['K_zero'] = {'digest': d_k0, 'trace': tr_k0}

        # W = 0
        d_w0, tr_w0 = compress_instrumented(seed, state, custom_W=[0]*64)
        families['W_zero'] = {'digest': d_w0, 'trace': tr_w0}

        all_results[cfg_name] = families

    # Print ripple statistics for normal families
    print("\n" + "=" * 72)
    print("RIPPLE STATISTICS (normal families)")
    print("=" * 72)

    for cfg_name in ['all_zero_empty', 'all_ones_empty', 'random_empty', 'SHA_IV_empty', 'IV_abc', 'IV_abd']:
        if cfg_name not in all_results:
            continue
        tr = all_results[cfg_name]['normal']['trace']
        ra_lens = [e['ripple_a']['length'] if e['ripple_a'] else 0 for e in tr]
        re_lens = [e['ripple_e']['length'] if e['ripple_e'] else 0 for e in tr]

        print(f"\n{cfg_name}:")
        print(f"  ripple(a) min/mean/max: {min(ra_lens)}/{sum(ra_lens)/64:.2f}/{max(ra_lens)}")
        print(f"  ripple(e) min/mean/max: {min(re_lens)}/{sum(re_lens)/64:.2f}/{max(re_lens)}")
        print(f"  first 12 ripple(a): {ra_lens[:12]}")
        print(f"  first 12 ripple(e): {re_lens[:12]}")

    # Wheel model testing
    print("\n" + "=" * 72)
    print("WHEEL MODEL PREDICTION ACCURACY")
    print("=" * 72)

    test_cases = [
        ('all_zero_empty', 'ripple_a', 37, 'Wheel-A (slots 0-7)'),
        ('all_zero_empty', 'ripple_e', 42, 'Wheel-E (slots 32-39)'),
        ('all_ones_empty', 'ripple_a', 37, 'Wheel-A (all_ones)'),
        ('IV_abc', 'ripple_a', 37, 'Wheel-A (abc)'),
        ('IV_abd', 'ripple_a', 37, 'Wheel-A (abd)'),
    ]

    for cfg_name, rkey, rho, label in test_cases:
        tr = all_results[cfg_name]['normal']['trace']
        res = test_wheel_models(tr, rkey, rho)
        print(f"\n{label}:")
        for mname, mres in res.items():
            print(f"  {mname:12s}: {mres['accuracy']:.3f} ({mres['hits']}/{mres['total']})")

    # Pairwise distances between coordinate vectors
    print("\n" + "=" * 72)
    print("PAIRWISE DISTANCES: 128-element coordinate vectors (a-carry only)")
    print("=" * 72)

    names = ['all_zero_empty', 'all_ones_empty', 'random_empty', 'SHA_IV_empty', 'IV_abc', 'IV_abd']
    vectors = {n: build_coordinate_vector(all_results[n]['normal']['trace'], use_a=True, use_e=False) 
               for n in names if n in all_results}

    name_list = list(vectors.keys())
    print(f"\n{'':20s}", end='')
    for n in name_list:
        print(f"{n:18s}", end='')
    print()

    for n1 in name_list:
        print(f"{n1:20s}", end='')
        for n2 in name_list:
            d = euclidean_distance(vectors[n1], vectors[n2])
            print(f"{d:18.2f}", end='')
        print()

    # Detailed trace: all_zero, first 8 rounds
    print("\n" + "=" * 72)
    print("DETAILED TRACE: all_zero_empty, normal, first 8 rounds")
    print("=" * 72)
    print(f"{'rnd':>4s} {'a_carry':>12s} {'e_carry':>12s} {'a_glob':>8s} {'e_glob':>8s} {'T1':>10s} {'T2':>10s}")

    tr = all_results['all_zero_empty']['normal']['trace']
    for entry in tr[:8]:
        ra = entry['ripple_a']
        re = entry['ripple_e']
        ra_str = f"{ra['start_bit']}→{ra['end_bit']}({ra['length']})" if ra else "—"
        re_str = f"{re['start_bit']}→{re['end_bit']}({re['length']})" if re else "—"
        ra_glob = f"{ra['global_start']}→{ra['global_end']}" if ra else "—"
        re_glob = f"{re['global_start']}→{re['global_end']}" if re else "—"
        print(f"{entry['round']:4d} {ra_str:>12s} {re_str:>12s} {ra_glob:>8s} {re_glob:>8s} {entry['T1']:010x} {entry['T2']:010x}")

    # Transition table for all_zero_empty, Wheel A
    print("\n" + "=" * 72)
    print("TRANSITION TABLE: all_zero_empty, Wheel A (first 16 rounds)")
    print("=" * 72)
    print(f"{'t':>3s} {'P_t':>4s} {'s_t':>4s} {'e_t':>4s} {'L_t':>4s} {'P_next':>6s} {'pred_A':>6s} {'pred_E':>6s}")

    actual = [e['ripple_a']['global_end'] if e['ripple_a'] else None for e in tr]
    last_P = 0
    for t in range(16):
        if actual[t] is not None:
            last_P = actual[t]
        driver = tr[t]['ripple_a']
        s = driver['start_bit'] if driver else 0
        e = driver['end_bit'] if driver else 0
        L = driver['length'] if driver else 0
        pred_A = (last_P + L) % 64 if driver else last_P
        pred_E = (last_P + L + 37) % 64 if driver else last_P
        actual_next = actual[t+1] if t+1 < 64 else None
        pn_str = str(actual_next) if actual_next is not None else "—"
        print(f"{t:3d} {last_P:4d} {s:4d} {e:4d} {L:4d} {pn_str:>6s} {pred_A:6d} {pred_E:6d}")

    # Controlled family comparison: all_zero with K=0 and W=0
    print("\n" + "=" * 72)
    print("CONTROLLED FAMILY COMPARISON: all_zero_empty")
    print("=" * 72)

    for fam in ['normal', 'K_zero', 'W_zero']:
        tr = all_results['all_zero_empty'][fam]['trace']
        ra_lens = [e['ripple_a']['length'] if e['ripple_a'] else 0 for e in tr]
        re_lens = [e['ripple_e']['length'] if e['ripple_e'] else 0 for e in tr]
        print(f"\n{fam}:")
        print(f"  ripple(a) min/mean/max: {min(ra_lens)}/{sum(ra_lens)/64:.2f}/{max(ra_lens)}")
        print(f"  ripple(e) min/mean/max: {min(re_lens)}/{sum(re_lens)/64:.2f}/{max(re_lens)}")
        print(f"  first 8 ripple(a): {ra_lens[:8]}")

    print("\n" + "=" * 72)
    print("ENGINE COMPLETE")
    print("=" * 72)
