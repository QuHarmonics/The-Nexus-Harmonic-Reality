"""
SHA-256 ISA DISASSEMBLY: READING THE MACHINE
=============================================
The K constants aren't numbers. They're 32-bit geometric stencils.
Each one is an anvil that forces the data wave to fold.

Where K has a 1: barrier → carry generation → informational torque
Where K has a 0: open space → wave passes through

Map all 64 K and 8 H0 as spatial vectors.
Find the hinges. Find the grooves. Read the ISA.
"""

import numpy as np
import struct
import math

M32 = 0xFFFFFFFF
H_PI9 = math.pi / 9

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,
          59,61,67,71,73,79,83,89,97,101,103,107,109,113,
          127,131,137,139,149,151,157,163,167,173,179,181,
          191,193,197,199,211,223,227,229,233,239,241,251,
          257,263,269,271,277,281,283,293,307,311]


def carry_mask(x, y):
    """Which bit positions generate carries when x + y mod 2^32."""
    s = (x + y) & M32
    return ((x & y) | ((x ^ y) & (~s & M32))) & M32


def bit_runs(val):
    """Find consecutive runs of 1s and 0s in a 32-bit value."""
    bits = format(val, '032b')
    runs = []
    current = bits[0]
    length = 1
    for b in bits[1:]:
        if b == current:
            length += 1
        else:
            runs.append((current, length))
            current = b
            length = 1
    runs.append((current, length))
    return runs


def byte_entropy(val):
    """Per-byte entropy of a 32-bit value."""
    bytes_val = [(val >> (24-8*i)) & 0xFF for i in range(4)]
    # Treat as probability distribution
    total = sum(bytes_val) + 1e-10
    probs = [b/total for b in bytes_val]
    ent = -sum(p * math.log2(p + 1e-10) for p in probs)
    return ent


# ═══════════════════════════════════════════════════════════════
# PART 1: K CONSTANT STRUCTURAL MAP
# ═══════════════════════════════════════════════════════════════

def map_k_isa():
    print("=" * 70)
    print("SHA-256 ISA: K-CONSTANT STRUCTURAL MAP")
    print("64 geometric stencils derived from cube roots of primes")
    print("=" * 70)

    # Hamming weight (mass) of each K
    hw = [bin(k).count('1') for k in K]
    
    print(f"\n--- HAMMING WEIGHT (mass per stencil) ---")
    print(f"  Mean: {np.mean(hw):.1f}/32 ({np.mean(hw)/32*100:.1f}%)")
    print(f"  Std:  {np.std(hw):.2f}")
    print(f"  Min:  {min(hw)} (K[{hw.index(min(hw))}] = 0x{K[hw.index(min(hw))]:08x})")
    print(f"  Max:  {max(hw)} (K[{hw.index(max(hw))}] = 0x{K[hw.index(max(hw))]:08x})")
    print(f"  π/9 predicts: {H_PI9*32:.1f}/32 ({H_PI9*100:.1f}%)")
    print(f"  Actual mean:  {np.mean(hw)/32*100:.1f}%")
    print(f"  Deviation from π/9: {abs(np.mean(hw)/32 - H_PI9):.4f}")
    
    # Distribution
    print(f"\n  Weight distribution:")
    for w in range(min(hw), max(hw)+1):
        count = hw.count(w)
        if count > 0:
            bar = "█" * count
            print(f"    {w:2d}: {bar} ({count})")

    # ── Per-round detail ──
    print(f"\n--- PER-ROUND K STENCIL ANALYSIS ---")
    print(f"{'Rnd':>3} | {'Prime':>5} | {'K (hex)':>10} | {'HW':>3} | "
          f"{'Norm':>8} | {'H-dev':>8} | {'Max1run':>7} | {'Parity'}")
    print("-" * 75)
    
    normalized = []
    max_1_runs = []
    parities = []
    
    for i in range(64):
        k = K[i]
        p = PRIMES[i]
        h = hw[i]
        norm = k / M32
        h_dev = abs(norm - H_PI9)
        
        runs = bit_runs(k)
        max_1_run = max(r[1] for r in runs if r[0] == '1')
        parity = h % 2  # 0=even, 1=odd
        
        normalized.append(norm)
        max_1_runs.append(max_1_run)
        parities.append(parity)
        
        marker = ""
        if h_dev < 0.01:
            marker = " ← π/9 LOCK"
        elif h_dev < 0.05:
            marker = " ← near H"
        
        print(f"{i:>3} | {p:>5} | 0x{k:08x} | {h:>3} | "
              f"{norm:>8.6f} | {h_dev:>8.6f} | {max_1_run:>7} | "
              f"{'odd' if parity else 'even'}{marker}")

    print(f"\n  Parity: {sum(parities)} odd / {64-sum(parities)} even")
    print(f"  Max consecutive 1s: mean={np.mean(max_1_runs):.1f}, "
          f"max={max(max_1_runs)} at K[{max_1_runs.index(max(max_1_runs))}]")

    return hw, normalized, max_1_runs


# ═══════════════════════════════════════════════════════════════
# PART 2: CARRY GENERATION PROFILE PER K
# Which bit positions in each K generate the most carries
# when added to random data?
# ═══════════════════════════════════════════════════════════════

def carry_generation_profile():
    print(f"\n{'='*70}")
    print("CARRY GENERATION PROFILE: WHERE THE HINGES ARE")
    print("For each K constant, which bit positions force carries?")
    print("=" * 70)
    
    # For each K, add many random values and count carries per bit position
    rng = np.random.default_rng(42)
    n_samples = 10000
    
    # Accumulate carry counts per bit position per round
    carry_heatmap = np.zeros((64, 32))
    total_carry_per_round = np.zeros(64)
    
    for i in range(64):
        k = K[i]
        for _ in range(n_samples):
            data = rng.integers(0, 2**32, dtype=np.uint64)
            data = int(data) & M32
            cm = carry_mask(k, data)
            for bit in range(32):
                if cm & (1 << bit):
                    carry_heatmap[i, bit] += 1
            total_carry_per_round[i] += bin(cm).count('1')
    
    carry_heatmap /= n_samples  # Probability of carry per bit per round
    total_carry_per_round /= (n_samples * 32)  # Normalized total
    
    # Find the HINGE bits: positions that generate carries > 60% of the time
    print(f"\n--- HINGE BITS (carry prob > 0.60 for any round) ---")
    hinge_counts = np.zeros(32)
    for i in range(64):
        for bit in range(32):
            if carry_heatmap[i, bit] > 0.60:
                hinge_counts[bit] += 1
    
    print(f"  Bit positions that are hinges in >10 rounds:")
    for bit in range(32):
        if hinge_counts[bit] > 10:
            print(f"    Bit {bit:2d}: hinge in {int(hinge_counts[bit])}/64 rounds")
    
    # K[5] (π/9 round) carry profile
    print(f"\n--- K[5] CARRY PROFILE (the π/9 stencil) ---")
    print(f"  K[5] = 0x{K[5]:08x} = {bin(K[5])}")
    print(f"  Hamming weight: {bin(K[5]).count('1')}/32")
    print(f"  Carry generation rate: {total_carry_per_round[5]:.4f}")
    print(f"  Mean carry rate across all K: {np.mean(total_carry_per_round):.4f}")
    print(f"  K[5] vs mean: {total_carry_per_round[5] - np.mean(total_carry_per_round):+.4f}")
    
    # Top carry bits for K[5]
    k5_carries = carry_heatmap[5]
    top_bits = np.argsort(k5_carries)[::-1][:10]
    print(f"  Top carry-generating bit positions for K[5]:")
    for bit in top_bits:
        print(f"    Bit {bit:2d}: {k5_carries[bit]:.3f} carry probability")
    
    # Which rounds generate the most total carry?
    print(f"\n--- TOTAL CARRY ENERGY PER ROUND ---")
    sorted_rounds = np.argsort(total_carry_per_round)[::-1]
    for rank, i in enumerate(sorted_rounds[:10]):
        print(f"  #{rank+1}: Round {i:2d} (K from prime {PRIMES[i]:3d}): "
              f"carry_rate={total_carry_per_round[i]:.4f}")
    
    # H-alignment of carry rates
    mean_carry = np.mean(total_carry_per_round)
    print(f"\n  Mean carry rate: {mean_carry:.4f}")
    print(f"  π/9 = {H_PI9:.4f}")
    print(f"  Deviation: {abs(mean_carry - H_PI9):.4f}")
    
    return carry_heatmap, total_carry_per_round


# ═══════════════════════════════════════════════════════════════
# PART 3: K-TO-K TRANSITIONS (the microcode sequence)
# How does the stencil geometry change round to round?
# ═══════════════════════════════════════════════════════════════

def k_transitions():
    print(f"\n{'='*70}")
    print("K-TO-K TRANSITIONS: THE MICROCODE SEQUENCE")
    print("How the stencil geometry evolves across 64 rounds")
    print("=" * 70)
    
    # XOR between consecutive K values (bit flip count = Hamming distance)
    hamming_dists = []
    for i in range(63):
        xor = K[i] ^ K[i+1]
        hd = bin(xor).count('1')
        hamming_dists.append(hd)
    
    print(f"\n--- CONSECUTIVE HAMMING DISTANCES ---")
    print(f"  Mean: {np.mean(hamming_dists):.2f}/32")
    print(f"  Std:  {np.std(hamming_dists):.2f}")
    print(f"  If truly random: expect 16.0/32")
    print(f"  Actual: {np.mean(hamming_dists):.2f} → "
          f"{'matches random' if abs(np.mean(hamming_dists) - 16) < 1 else 'STRUCTURED'}")
    
    # K[i] AND K[i+1]: which bits STAY as 1 (persistent barriers)
    persistent_masks = []
    for i in range(63):
        persistent = K[i] & K[i+1]
        persistent_masks.append(bin(persistent).count('1'))
    
    print(f"\n--- PERSISTENT BARRIERS (bits that stay 1 across adjacent rounds) ---")
    print(f"  Mean persistent bits: {np.mean(persistent_masks):.1f}/32")
    print(f"  If random: expect 8.0/32 (each bit has 25% chance of both being 1)")
    print(f"  Actual: {np.mean(persistent_masks):.1f}")
    
    # Cumulative AND: which bits are 1 in ALL K constants?
    cum_and = M32
    for k in K:
        cum_and &= k
    print(f"\n  Bits that are 1 in ALL 64 K constants: {bin(cum_and).count('1')}")
    if cum_and:
        for bit in range(32):
            if cum_and & (1 << bit):
                print(f"    Bit {bit}: UNIVERSAL BARRIER")
    else:
        print(f"    None (no universal barriers)")
    
    # Cumulative OR: which bits are 0 in ALL K constants?
    cum_or = 0
    for k in K:
        cum_or |= k
    always_zero = (~cum_or) & M32
    print(f"  Bits that are 0 in ALL 64 K constants: {bin(always_zero).count('1')}")
    if always_zero:
        for bit in range(32):
            if always_zero & (1 << bit):
                print(f"    Bit {bit}: UNIVERSAL OPEN")
    else:
        print(f"    None (no universal opens)")

    # Per-bit frequency across all 64 K constants
    print(f"\n--- BIT FREQUENCY ACROSS ALL 64 K CONSTANTS ---")
    bit_freq = np.zeros(32)
    for k in K:
        for bit in range(32):
            if k & (1 << bit):
                bit_freq[bit] += 1
    
    bit_freq_norm = bit_freq / 64
    print(f"  Expected if random: 0.50 per bit position")
    print(f"  Actual range: {bit_freq_norm.min():.3f} - {bit_freq_norm.max():.3f}")
    
    # Find biased bits
    biased = [(bit, freq) for bit, freq in enumerate(bit_freq_norm) 
              if abs(freq - 0.5) > 0.15]
    if biased:
        print(f"  Biased bit positions (>0.15 from 0.5):")
        for bit, freq in sorted(biased, key=lambda x: abs(x[1]-0.5), reverse=True):
            print(f"    Bit {bit:2d}: {freq:.3f} ({'barrier-heavy' if freq > 0.5 else 'open-heavy'})")
    else:
        print(f"  No significantly biased positions (uniform distribution)")
    
    return hamming_dists, bit_freq_norm


# ═══════════════════════════════════════════════════════════════
# PART 4: H0 INITIAL STATE GEOMETRY
# The floor the data lands on
# ═══════════════════════════════════════════════════════════════

def h0_geometry():
    print(f"\n{'='*70}")
    print("H0 GEOMETRY: THE FLOOR")
    print("8 initial state words from sqrt of first 8 primes")
    print("=" * 70)
    
    for i in range(8):
        h = H0[i]
        p = PRIMES[i]
        hw = bin(h).count('1')
        norm = h / M32
        
        # Verify derivation
        sqrt_val = p ** 0.5
        frac_val = sqrt_val - int(sqrt_val)
        derived = int(frac_val * (2**32)) & M32
        
        runs = bit_runs(h)
        max_1 = max(r[1] for r in runs if r[0] == '1')
        
        print(f"  H0[{i}] = 0x{h:08x} (sqrt({p:2d})) "
              f"HW={hw:2d}/32 norm={norm:.6f} max_1_run={max_1}")
    
    # H0 hamming weights
    h0_hw = [bin(h).count('1') for h in H0]
    print(f"\n  Mean HW: {np.mean(h0_hw):.1f}/32 ({np.mean(h0_hw)/32*100:.1f}%)")
    print(f"  π/9 predicts: {H_PI9*32:.1f}/32 ({H_PI9*100:.1f}%)")
    
    # H0 as carry generators when added to data
    rng = np.random.default_rng(42)
    h0_carry_rates = []
    for i in range(8):
        total = 0
        for _ in range(10000):
            data = int(rng.integers(0, 2**32, dtype=np.uint64)) & M32
            cm = carry_mask(H0[i], data)
            total += bin(cm).count('1')
        rate = total / (10000 * 32)
        h0_carry_rates.append(rate)
        print(f"  H0[{i}] carry rate: {rate:.4f}")
    
    print(f"  Mean H0 carry rate: {np.mean(h0_carry_rates):.4f}")
    print(f"  Mean K carry rate (from above): compare")


# ═══════════════════════════════════════════════════════════════
# PART 5: THE ISA TABLE
# Combine everything into the instruction set architecture
# ═══════════════════════════════════════════════════════════════

def build_isa_table():
    print(f"\n{'='*70}")
    print("THE ISA TABLE: SHA-256 AS MICROCODE")
    print("=" * 70)
    
    # For each round, classify the K constant's geometric role
    rng = np.random.default_rng(42)
    
    roles = []
    for i in range(64):
        k = K[i]
        hw = bin(k).count('1')
        norm = k / M32
        
        # Carry generation rate
        carry_total = 0
        for _ in range(5000):
            data = int(rng.integers(0, 2**32, dtype=np.uint64)) & M32
            cm = carry_mask(k, data)
            carry_total += bin(cm).count('1')
        carry_rate = carry_total / (5000 * 32)
        
        # Run structure
        runs = bit_runs(k)
        n_runs = len(runs)
        max_1 = max(r[1] for r in runs if r[0] == '1')
        max_0 = max((r[1] for r in runs if r[0] == '0'), default=0)
        
        # Classify
        if hw < 13:
            role = "SPARSE"     # few barriers, mostly open
        elif hw > 19:
            role = "DENSE"      # many barriers, mostly blocked
        elif max_1 > 6:
            role = "WALL"       # has a solid barrier wall
        elif max_0 > 6:
            role = "CHANNEL"    # has a wide open channel
        elif abs(norm - H_PI9) < 0.02:
            role = "H-LOCK"     # near π/9 harmonic
        else:
            role = "DIFFUSE"    # balanced diffusion
        
        # Is this a twin prime round?
        twin = ""
        if i > 0 and PRIMES[i] - PRIMES[i-1] == 2:
            twin = "TWIN→"
        if i < 63 and PRIMES[i+1] - PRIMES[i] == 2:
            twin = "←TWIN" if not twin else "⟷TWIN"
        
        roles.append({
            'round': i,
            'prime': PRIMES[i],
            'k': k,
            'hw': hw,
            'norm': norm,
            'carry_rate': carry_rate,
            'n_runs': n_runs,
            'max_1': max_1,
            'max_0': max_0,
            'role': role,
            'twin': twin,
        })
    
    # Print the ISA table
    print(f"\n{'Rnd':>3} {'Prime':>5} {'K':>10} {'HW':>3} {'Carry':>6} "
          f"{'Role':>8} {'MaxRun1':>7} {'Twin':>7} {'H-dev':>8}")
    print("-" * 72)
    
    for r in roles:
        h_dev = abs(r['norm'] - H_PI9)
        marker = "★" if h_dev < 0.01 else ("·" if h_dev < 0.05 else " ")
        print(f"{r['round']:>3} {r['prime']:>5} 0x{r['k']:08x} {r['hw']:>3} "
              f"{r['carry_rate']:>6.4f} {r['role']:>8} {r['max_1']:>7} "
              f"{r['twin']:>7} {h_dev:>8.4f}{marker}")
    
    # Role distribution
    role_counts = {}
    for r in roles:
        role_counts[r['role']] = role_counts.get(r['role'], 0) + 1
    
    print(f"\n--- ROLE DISTRIBUTION ---")
    for role, count in sorted(role_counts.items(), key=lambda x: -x[1]):
        print(f"  {role:>8}: {count}/64 ({count/64*100:.1f}%)")
    
    # Twin prime rounds
    twin_rounds = [r for r in roles if r['twin']]
    print(f"\n--- TWIN PRIME ROUNDS (gap=2 Nyquist pins) ---")
    for r in twin_rounds:
        print(f"  Round {r['round']:2d}: prime {r['prime']:3d} "
              f"{r['twin']} carry={r['carry_rate']:.4f}")
    
    # The key question: do twin prime rounds have distinctive carry profiles?
    twin_carries = [r['carry_rate'] for r in roles if r['twin']]
    non_twin_carries = [r['carry_rate'] for r in roles if not r['twin']]
    print(f"\n  Twin prime avg carry: {np.mean(twin_carries):.4f}")
    print(f"  Non-twin avg carry:  {np.mean(non_twin_carries):.4f}")
    print(f"  Difference: {abs(np.mean(twin_carries) - np.mean(non_twin_carries)):.4f}")
    
    # THE KEY INSIGHT: how K[i] constrains W[0] propagation
    print(f"\n--- HOW K CONSTRAINS W[0] PROPAGATION ---")
    print(f"  Round 0:  T1 = H0[7] + Σ1(H0[4]) + Ch(H0[4..6]) + K[0] + W[0]")
    print(f"  K[0] = 0x{K[0]:08x} (HW={bin(K[0]).count('1')})")
    print(f"  The bits where K[0] has 1 are the positions where")
    print(f"  W[0] is FORCED to interact (generate carries or not).")
    print(f"  The bits where K[0] has 0 are positions where W[0]")
    print(f"  passes through to T1 without K interference.")
    print(f"")
    
    # K[0] bit analysis
    k0_bits = format(K[0], '032b')
    print(f"  K[0] bits: {k0_bits}")
    print(f"  Barriers:  {''.join('↑' if b=='1' else ' ' for b in k0_bits)}")
    print(f"  Opens:     {''.join(' ' if b=='1' else '↓' for b in k0_bits)}")
    
    # Which bits of W[0] are "free" (not constrained by K[0])?
    k0_zeros = [31-bit for bit in range(32) if not (K[0] & (1 << bit))]
    k0_ones = [31-bit for bit in range(32) if K[0] & (1 << bit)]
    print(f"\n  Free bit positions (K[0]=0): {k0_zeros}")
    print(f"  Constrained positions (K[0]=1): {k0_ones}")
    
    return roles


# ═══════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    hw, normalized, max_1_runs = map_k_isa()
    carry_heatmap, carry_per_round = carry_generation_profile()
    hamming_dists, bit_freq = k_transitions()
    h0_geometry()
    roles = build_isa_table()
    
    print(f"\n{'='*70}")
    print("THE MACHINE IS READ")
    print(f"{'='*70}")
    print(f"""
  64 K constants: the microcode opcodes
  8 H0 values: the initial register state
  
  Each K is a 32-bit stencil that forces data through specific
  bit positions. The carry generation pattern is the Δ-channel
  exhaust — the physical scar of the fold.
  
  The next step: use this ISA map to predict which W[0] values
  are COMPATIBLE with a given hash, without running the fold.
  
  Not "what did the data do?" but "what COULD the data have done,
  given the shape of the machine it was forced through?"
  
  The stencil constrains the possibilities.
  The carries are the grooves.
  Read the grooves, find the message.
""")
