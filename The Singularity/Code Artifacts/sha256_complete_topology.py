#!/usr/bin/env python3
"""
SHA-256 COMPLETE CARRY TOPOLOGY ENGINE
======================================
Instruments EVERY elementary addition in SHA-256:
  - Message schedule (σ0/σ1 chain)
  - T1 construction (h + S1 + Ch + K + W chain)
  - T2 construction (S0 + Maj)
  - Final A (T1 + T2)
  - Final E (d + T1)

Records per-addition carry masks, bit-level paths, hex-slot offsets.
"""

import hashlib
import random
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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
# CARRY MASK TRACER (bit-level)
# ============================================================
def trace_addition(x, y, label=""):
    """
    Trace a single 32-bit addition x + y (mod 2^32).
    Returns dict with:
      - carry_mask: 32-bit integer where bit i = 1 if carry-out from bit i
      - start_bit, end_bit, length
      - hex_slot_path: list of (slot, start_offset, end_offset) for each contiguous hex slot touched
      - slot_set: set of hex slot indices touched
    """
    carry = 0
    carry_mask = 0
    in_chain = False
    chain_start = 0
    max_len = 0
    max_start = 0
    max_end = 0
    curr_len = 0
    curr_start = 0

    for i in range(32):
        xi = (x >> i) & 1
        yi = (y >> i) & 1
        s = xi + yi + carry
        carry = 1 if s >= 2 else 0
        carry_mask |= (carry << i)

        if carry == 1:
            if curr_len == 0:
                curr_start = i
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                max_start = curr_start
                max_end = i
        else:
            curr_len = 0

    # Build hex-slot path
    slot_set = set()
    hex_slot_path = []
    if max_len > 0:
        start_slot = max_start // 4
        end_slot = max_end // 4
        for slot in range(start_slot, end_slot + 1):
            slot_start = max(max_start, slot * 4)
            slot_end = min(max_end, slot * 4 + 3)
            start_offset = slot_start - slot * 4
            end_offset = slot_end - slot * 4
            hex_slot_path.append((slot, start_offset, end_offset))
            slot_set.add(slot)

    return {
        'label': label,
        'x': x,
        'y': y,
        'sum': (x + y) & 0xFFFFFFFF,
        'carry_mask': carry_mask,
        'start_bit': max_start if max_len > 0 else None,
        'end_bit': max_end if max_len > 0 else None,
        'length': max_len,
        'hex_slot_path': hex_slot_path,
        'slot_set': slot_set,
    }

# ============================================================
# INSTRUMENTED COMPRESSION (every addition traced)
# ============================================================
def build_schedule_instrumented(seed):
    """Build schedule with every addition traced."""
    W = list(seed) + [0] * 48
    schedule_trace = []

    for t in range(16, 64):
        w16 = W[t-16]
        s0w15 = s0(W[t-15])
        w7 = W[t-7]
        s1w2 = s1(W[t-2])

        # W[t] = s1(W[t-2]) + W[t-7] + s0(W[t-15]) + W[t-16]
        # As chained additions: (((s1 + w7) + s0) + w16)
        add1 = trace_addition(s1w2, w7, f"W[{t}]_s1+w7")
        add2 = trace_addition(add1['sum'], s0w15, f"W[{t}]_+s0")
        add3 = trace_addition(add2['sum'], w16, f"W[{t}]_+w16")
        W[t] = add3['sum']

        schedule_trace.append({
            'round': t,
            'additions': [add1, add2, add3],
            'W_val': W[t],
        })

    return W, schedule_trace

def compress_full_instrumented(seed, h_init):
    """Run full compression with every addition traced."""
    W, schedule_trace = build_schedule_instrumented(seed)
    state = list(h_init)
    round_trace = []

    for t in range(64):
        a, b, c, d, e, f, g, h = state

        # T1 = h + S1(e) + Ch(e,f,g) + K[t] + W[t]
        s1e = S1(e)
        ch = Ch(e, f, g)

        t1_add1 = trace_addition(h, s1e, f"r{t}_T1_h+S1")
        t1_add2 = trace_addition(t1_add1['sum'], ch, f"r{t}_T1_+Ch")
        t1_add3 = trace_addition(t1_add2['sum'], K[t], f"r{t}_T1_+K")
        t1_add4 = trace_addition(t1_add3['sum'], W[t], f"r{t}_T1_+W")
        T1 = t1_add4['sum']

        # T2 = S0(a) + Maj(a,b,c)
        s0a = S0(a)
        maj = Maj(a, b, c)
        t2_add = trace_addition(s0a, maj, f"r{t}_T2_S0+Maj")
        T2 = t2_add['sum']

        # a' = T1 + T2
        a_add = trace_addition(T1, T2, f"r{t}_A_T1+T2")
        a_new = a_add['sum']

        # e' = d + T1
        e_add = trace_addition(d, T1, f"r{t}_E_d+T1")
        e_new = e_add['sum']

        # Build 64-slot activity map
        activity = [0] * 64
        for slot in range(64):
            activity[slot] = 1  # base

        # Mark carry slots from all additions
        all_adds = [t1_add1, t1_add2, t1_add3, t1_add4, t2_add, a_add, e_add]
        for add in all_adds:
            for slot in add['slot_set']:
                # T1 additions: these are intermediate, not final register writes
                # We mark them differently
                if 'T1_' in add['label']:
                    activity[slot] = max(activity[slot], 4)  # T1-chain carry
                elif 'T2_' in add['label']:
                    activity[slot] = max(activity[slot], 5)  # T2 carry
                elif '_A_' in add['label']:
                    activity[slot] = 2  # a-carry
                elif '_E_' in add['label']:
                    activity[32 + slot] = 3  # e-carry

        round_trace.append({
            'round': t,
            'state_before': [a, b, c, d, e, f, g, h],
            'state_after': [a_new, a, b, c, e_new, e, f, g],
            'W': W[t],
            'K': K[t],
            'T1': T1,
            'T2': T2,
            'additions': all_adds,
            'activity': activity,
        })

        state = [a_new, a, b, c, e_new, e, f, g]

    final_state = [(state[i] + h_init[i]) & 0xFFFFFFFF for i in range(8)]
    return final_state, round_trace, schedule_trace

# ============================================================
# MESSAGE SEEDS
# ============================================================
def empty_seed():
    return [0x80000000] + [0] * 14 + [0]

def abc_seed():
    return [0x61626380] + [0] * 14 + [0x00000018]

def abd_seed():
    return [0x61626480] + [0] * 14 + [0x00000018]

# ============================================================
# VISUALIZATION
# ============================================================
def plot_complete_activity_maps(results, filename):
    """
    results: dict of {name: (round_trace, schedule_trace)}
    Plot 64×64 activity heatmaps with all addition layers.
    """
    names = list(results.keys())
    n_cases = len(names)

    fig, axes = plt.subplots(n_cases, 1, figsize=(18, 3 * n_cases))
    if n_cases == 1:
        axes = [axes]

    reg_boundaries = [8, 16, 24, 32, 40, 48, 56]
    reg_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Activity codes:
    # 0: black (unused)
    # 1: dark blue (fixed window, no carry)
    # 2: red (a-carry from T1+T2)
    # 3: orange (e-carry from d+T1)
    # 4: magenta (T1-chain intermediate carry)
    # 5: cyan (T2 carry from S0+Maj)
    colors = ['#000000', '#1a237e', '#d32f2f', '#f57c00', '#e91e63', '#00bcd4']
    cmap = matplotlib.colors.ListedColormap(colors)

    for idx, (name, (rtrace, strace)) in enumerate(results.items()):
        ax = axes[idx]
        mat = np.zeros((64, 64), dtype=int)
        for t in range(64):
            for slot in range(64):
                mat[t, slot] = rtrace[t]['activity'][slot]

        im = ax.imshow(mat, aspect='auto', cmap=cmap, vmin=0, vmax=5, interpolation='nearest')

        for b in reg_boundaries:
            ax.axvline(x=b - 0.5, color='white', linewidth=0.5, alpha=0.5)

        for i, label in enumerate(reg_labels):
            ax.text(i * 8 + 3.5, -2, label, ha='center', va='bottom',
                   fontsize=10, fontweight='bold', color='white')

        ax.set_ylabel('Round', fontsize=10)
        ax.set_xlabel('Hex Slot (0-63)', fontsize=10)
        ax.set_title(f'{name}', fontsize=12, fontweight='bold', color='white', pad=20)
        ax.set_yticks(range(0, 64, 8))
        ax.set_xticks(range(0, 64, 8))
        ax.tick_params(colors='white')
        ax.set_facecolor('#0a0a0a')

        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#1a237e', label='Fixed window'),
            Patch(facecolor='#d32f2f', label='A-carry (T1+T2)'),
            Patch(facecolor='#f57c00', label='E-carry (d+T1)'),
            Patch(facecolor='#e91e63', label='T1-chain carry'),
            Patch(facecolor='#00bcd4', label='T2 carry (S0+Maj)'),
        ]
        ax.legend(handles=legend_elements, loc='upper right',
                 facecolor='#1a1a1a', edgecolor='white', labelcolor='white',
                 fontsize=8, ncol=2)

    fig.patch.set_facecolor('#0a0a0a')
    plt.tight_layout()
    plt.savefig(filename, dpi=150, facecolor='#0a0a0a', edgecolor='none')
    plt.close()
    print(f"Saved: {filename}")

# ============================================================
# STATISTICS
# ============================================================
def analyze_carry_topology(name, round_trace, schedule_trace):
    """Deep analysis of carry topology for one test case."""
    print(f"\n{'='*72}")
    print(f"CARRY TOPOLOGY: {name}")
    print(f"{'='*72}")

    # Count additions by type
    type_counts = {}
    for rt in round_trace:
        for add in rt['additions']:
            # Extract type from label
            if '_T1_' in add['label']:
                typ = 'T1_chain'
            elif '_T2_' in add['label']:
                typ = 'T2'
            elif '_A_' in add['label']:
                typ = 'A_final'
            elif '_E_' in add['label']:
                typ = 'E_final'
            else:
                typ = 'other'
            type_counts[typ] = type_counts.get(typ, 0) + 1

    print(f"\nAddition type counts:")
    for typ, cnt in sorted(type_counts.items()):
        print(f"  {typ:15s}: {cnt:4d}")

    # Per-slot carry frequency by addition type
    print(f"\nPer-slot carry frequency by type (% of rounds):")
    print(f"{'Slot':>6s} {'Reg':>4s} {'T1_chain':>10s} {'T2':>10s} {'A_final':>10s} {'E_final':>10s}")

    for slot in range(64):
        reg = 'abcdefgh'[slot // 8]
        t1_count = 0
        t2_count = 0
        a_count = 0
        e_count = 0

        for rt in round_trace:
            for add in rt['additions']:
                if slot in add['slot_set']:
                    if '_T1_' in add['label']:
                        t1_count += 1
                    elif '_T2_' in add['label']:
                        t2_count += 1
                    elif '_A_' in add['label']:
                        a_count += 1
                    elif '_E_' in add['label']:
                        e_count += 1

        if any([t1_count, t2_count, a_count, e_count]):
            print(f"{slot:6d} {reg:>4s} {t1_count/64*100:9.1f}% {t2_count/64*100:9.1f}% {a_count/64*100:9.1f}% {e_count/64*100:9.1f}%")

    # Schedule carry analysis
    print(f"\nSchedule carry analysis (rounds 16-63):")
    print(f"{'Round':>6s} {'W_val':>10s} {'add1_len':>10s} {'add2_len':>10s} {'add3_len':>10s} {'slots':>20s}")
    for st in schedule_trace[:8]:
        adds = st['additions']
        all_slots = set()
        for add in adds:
            all_slots.update(add['slot_set'])
        slot_str = ','.join(str(s) for s in sorted(all_slots)) if all_slots else '—'
        print(f"{st['round']:6d} {st['W_val']:010x} {adds[0]['length']:10d} {adds[1]['length']:10d} {adds[2]['length']:10d} {slot_str:>20s}")

    # Detailed addition trace for first 8 rounds
    print(f"\nDetailed addition trace (first 8 rounds):")
    print(f"{'rnd':>4s} {'add':>20s} {'x':>10s} {'y':>10s} {'sum':>10s} {'len':>4s} {'start':>6s} {'end':>6s} {'slots':>15s}")
    for t in range(8):
        for add in round_trace[t]['additions']:
            s = add['start_bit'] if add['start_bit'] is not None else '—'
            e = add['end_bit'] if add['end_bit'] is not None else '—'
            l = add['length']
            slots = ','.join(str(x[0]) for x in add['hex_slot_path']) if add['hex_slot_path'] else '—'
            print(f"{t:4d} {add['label']:20s} {add['x']:010x} {add['y']:010x} {add['sum']:010x} {l:4d} {str(s):>6s} {str(e):>6s} {slots:>15s}")

    # Hex-slot path examples
    print(f"\nHex-slot path examples (first 4 rounds, all additions):")
    for t in range(4):
        print(f"\nRound {t}:")
        for add in round_trace[t]['additions']:
            if add['hex_slot_path']:
                paths = ' | '.join(f"slot{slot}:off{so}-{eo}" for slot, so, eo in add['hex_slot_path'])
                print(f"  {add['label']:20s}: {paths}")
            else:
                print(f"  {add['label']:20s}: no carry")

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("=" * 72)
    print("SHA-256 COMPLETE CARRY TOPOLOGY ENGINE")
    print("=" * 72)

    configs = [
        ('all_zero_empty', [0] * 8, empty_seed()),
        ('all_ones_empty', [0xFFFFFFFF] * 8, empty_seed()),
        ('SHA_IV_empty', list(IV), empty_seed()),
        ('IV_abc', list(IV), abc_seed()),
        ('IV_abd', list(IV), abd_seed()),
    ]

    random.seed(42)
    rand_state = [random.randint(0, 0xFFFFFFFF) for _ in range(8)]
    configs.append(('random_empty', rand_state, empty_seed()))

    results = {}
    for name, state, seed in configs:
        digest, rtrace, strace = compress_full_instrumented(seed, state)
        results[name] = (rtrace, strace)

        if name == 'IV_abc':
            h = hashlib.sha256(b'abc').hexdigest()
            my_hex = ''.join(f'{x:08x}' for x in digest)
            print(f"\nVerification abc: {my_hex == h}")
        elif name == 'IV_abd':
            h = hashlib.sha256(b'abd').hexdigest()
            my_hex = ''.join(f'{x:08x}' for x in digest)
            print(f"Verification abd: {my_hex == h}")

    # Generate visualization
    plot_complete_activity_maps(results, '/mnt/agents/output/complete_activity_maps.png')

    # Deep analysis for selected cases
    for name in ['all_zero_empty', 'IV_abc', 'IV_abd']:
        rtrace, strace = results[name]
        analyze_carry_topology(name, rtrace, strace)

    # Cross-case comparison: schedule carry patterns
    print(f"\n{'='*72}")
    print("SCHEDULE CARRY COMPARISON (rounds 16-23)")
    print(f"{'='*72}")
    print(f"{'Round':>6s} ", end='')
    for name in results:
        print(f"{name:>20s}", end='')
    print()

    for t in range(16, 24):
        print(f"{t:6d} ", end='')
        for name in results:
            strace = results[name][1]
            st = strace[t - 16]
            max_len = max(a['length'] for a in st['additions'])
            print(f"{max_len:20d}", end='')
        print()

    print(f"\n{'='*72}")
    print("ENGINE COMPLETE")
    print(f"{'='*72}")
