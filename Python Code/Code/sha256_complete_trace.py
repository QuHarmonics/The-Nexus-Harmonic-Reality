#!/usr/bin/env python3
"""
SHA-256 COMPLETE TRACE: "hello"
===============================
Every single step. No black boxes.
This is the probe.

We trace:
1. Input → bytes → padding
2. Message schedule (W expansion)
3. All 64 rounds with every operation
4. Final hash

Looking for:
- Where does the 90° turn happen?
- Where does H appear?
- What is the cross-collapse doing mechanically?
"""

import struct
import hashlib

# ═══════════════════════════════════════════════════════════════════════════
# SHA-256 CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════

# Initial hash values (H0-H7): first 32 bits of fractional parts of √(first 8 primes)
H_INIT = [
    0x6a09e667,  # √2
    0xbb67ae85,  # √3
    0x3c6ef372,  # √5
    0xa54ff53a,  # √7
    0x510e527f,  # √11
    0x9b05688c,  # √13
    0x1f83d9ab,  # √17
    0x5be0cd19,  # √19
]

# Round constants (K0-K63): first 32 bits of fractional parts of ∛(first 64 primes)
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
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# ═══════════════════════════════════════════════════════════════════════════
# PRIMITIVE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════

def rotr(x, n):
    """Rotate right by n bits (32-bit)"""
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def shr(x, n):
    """Shift right by n bits"""
    return x >> n

def Ch(e, f, g):
    """Choice: if e then f else g (bitwise)"""
    return (e & f) ^ (~e & g) & 0xFFFFFFFF

def Maj(a, b, c):
    """Majority: bitwise majority of a, b, c"""
    return (a & b) ^ (a & c) ^ (b & c)

def Sigma0(a):
    """Big sigma 0: used on 'a' register (noun)"""
    return rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)

def Sigma1(e):
    """Big sigma 1: used on 'e' register (verb)"""
    return rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)

def sigma0(x):
    """Small sigma 0: used in message schedule"""
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def sigma1(x):
    """Small sigma 1: used in message schedule"""
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def add(*args):
    """Addition mod 2^32"""
    result = 0
    for x in args:
        result = (result + x) & 0xFFFFFFFF
    return result

# ═══════════════════════════════════════════════════════════════════════════
# STEP 1: INPUT AND PADDING
# ═══════════════════════════════════════════════════════════════════════════

def pad_message(message):
    """
    Pad message to multiple of 512 bits (64 bytes).
    
    Format:
    - Original message
    - Single '1' bit
    - Zeros to fill
    - 64-bit length (big endian)
    """
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    original_len = len(message)
    original_bit_len = original_len * 8
    
    # Add the '1' bit (0x80 = 10000000)
    message += b'\x80'
    
    # Add zeros until length ≡ 448 (mod 512), i.e., 56 bytes (mod 64)
    while (len(message) % 64) != 56:
        message += b'\x00'
    
    # Add the original length as 64-bit big-endian
    message += struct.pack('>Q', original_bit_len)
    
    return message

def show_padding(original, padded):
    """Visualize the padding."""
    print("=" * 70)
    print("STEP 1: INPUT AND PADDING")
    print("=" * 70)
    
    print(f"\nOriginal message: \"{original}\"")
    print(f"As bytes: {original.encode('utf-8').hex()}")
    print(f"Length: {len(original)} bytes = {len(original) * 8} bits")
    
    print(f"\nPadded message ({len(padded)} bytes = {len(padded) * 8} bits):")
    
    # Show in 16-byte rows
    for i in range(0, len(padded), 16):
        chunk = padded[i:i+16]
        hex_str = ' '.join(f'{b:02x}' for b in chunk)
        ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"  {i:3d}: {hex_str:48s} |{ascii_str}|")
    
    print(f"\nBreakdown:")
    print(f"  Bytes 0-4:   \"{original}\" (original message)")
    print(f"  Byte 5:      0x80 (the '1' bit + 7 zeros)")
    print(f"  Bytes 6-55:  0x00 × 50 (padding zeros)")
    print(f"  Bytes 56-63: 0x00000028 = 40 bits (original length in big-endian)")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 2: MESSAGE SCHEDULE
# ═══════════════════════════════════════════════════════════════════════════

def create_message_schedule(block):
    """
    Expand 16-word (512-bit) block to 64-word schedule.
    
    W[0..15] = block words
    W[16..63] = σ1(W[t-2]) + W[t-7] + σ0(W[t-15]) + W[t-16]
    """
    W = []
    
    # First 16 words: directly from block
    for i in range(16):
        word = struct.unpack('>I', block[i*4:(i+1)*4])[0]
        W.append(word)
    
    # Words 16-63: computed from previous words
    for i in range(16, 64):
        s0 = sigma0(W[i-15])
        s1 = sigma1(W[i-2])
        W.append(add(s1, W[i-7], s0, W[i-16]))
    
    return W

def show_message_schedule(W):
    """Show the message schedule expansion."""
    print("\n" + "=" * 70)
    print("STEP 2: MESSAGE SCHEDULE (W[0..63])")
    print("=" * 70)
    
    print("\nW[0..15] (directly from padded block):")
    for i in range(16):
        print(f"  W[{i:2d}] = 0x{W[i]:08x}")
    
    print("\nW[16..23] (first computed words - showing formula):")
    for i in range(16, 24):
        print(f"  W[{i:2d}] = σ1(W[{i-2}]) + W[{i-7}] + σ0(W[{i-15}]) + W[{i-16}]")
        print(f"        = σ1(0x{W[i-2]:08x}) + 0x{W[i-7]:08x} + σ0(0x{W[i-15]:08x}) + 0x{W[i-16]:08x}")
        print(f"        = 0x{W[i]:08x}")
    
    print("\nW[24..63] (remaining computed words):")
    for i in range(24, 64, 4):
        row = [f"W[{j:2d}]=0x{W[j]:08x}" for j in range(i, min(i+4, 64))]
        print(f"  {', '.join(row)}")

# ═══════════════════════════════════════════════════════════════════════════
# STEP 3: COMPRESSION ROUNDS
# ═══════════════════════════════════════════════════════════════════════════

def compression_round(state, W, round_num, verbose=False):
    """
    One round of SHA-256 compression.
    
    This is WHERE THE MAGIC HAPPENS.
    """
    a, b, c, d, e, f, g, h = state
    
    # The key operations:
    S1 = Sigma1(e)       # Verb path: particle collapse (contains 11/32 ≈ H)
    ch = Ch(e, f, g)     # Decision: e chooses between f and g
    
    S0 = Sigma0(a)       # Noun path: wave collapse (contains 22/32 ≈ 1-H)
    maj = Maj(a, b, c)   # Consensus: majority of a, b, c
    
    # Combine:
    temp1 = add(h, S1, ch, K[round_num], W[round_num])  # Verb contribution
    temp2 = add(S0, maj)                                 # Noun contribution
    
    # Update state:
    new_a = add(temp1, temp2)  # THE CROSS-COLLAPSE: verb + noun
    new_e = add(d, temp1)      # Verb path continues
    
    new_state = [new_a, a, b, c, new_e, e, f, g]
    
    if verbose:
        print(f"\n  Round {round_num:2d}:")
        print(f"    Input:  a={a:08x} b={b:08x} c={c:08x} d={d:08x}")
        print(f"            e={e:08x} f={f:08x} g={g:08x} h={h:08x}")
        print(f"    Σ1(e)={S1:08x}  Ch(e,f,g)={ch:08x}  [VERB PATH - particle collapse]")
        print(f"    Σ0(a)={S0:08x}  Maj(a,b,c)={maj:08x}  [NOUN PATH - wave collapse]")
        print(f"    temp1 (h+Σ1+Ch+K+W) = {temp1:08x}  [verb contribution]")
        print(f"    temp2 (Σ0+Maj)      = {temp2:08x}  [noun contribution]")
        print(f"    new_a = temp1+temp2 = {new_a:08x}  [CROSS-COLLAPSE]")
        print(f"    new_e = d+temp1     = {new_e:08x}")
        print(f"    Output: a={new_state[0]:08x} e={new_state[4]:08x}")
    
    return new_state

def run_compression(H, W, verbose_rounds=None):
    """Run all 64 rounds of compression."""
    print("\n" + "=" * 70)
    print("STEP 3: COMPRESSION (64 ROUNDS)")
    print("=" * 70)
    
    if verbose_rounds is None:
        verbose_rounds = [0, 1, 2, 31, 32, 62, 63]
    
    state = list(H)
    
    print(f"\nInitial state (H[0..7]):")
    print(f"  a={state[0]:08x} b={state[1]:08x} c={state[2]:08x} d={state[3]:08x}")
    print(f"  e={state[4]:08x} f={state[5]:08x} g={state[6]:08x} h={state[7]:08x}")
    
    print(f"\nRunning 64 rounds (showing rounds {verbose_rounds})...")
    
    for i in range(64):
        verbose = i in verbose_rounds
        state = compression_round(state, W, i, verbose=verbose)
        
        if i not in verbose_rounds and (i == 15 or i == 47):
            print(f"\n  ... (rounds {i-13}-{i} completed) ...")
    
    print(f"\nFinal working state:")
    print(f"  a={state[0]:08x} b={state[1]:08x} c={state[2]:08x} d={state[3]:08x}")
    print(f"  e={state[4]:08x} f={state[5]:08x} g={state[6]:08x} h={state[7]:08x}")
    
    return state

# ═══════════════════════════════════════════════════════════════════════════
# STEP 4: FINAL HASH
# ═══════════════════════════════════════════════════════════════════════════

def compute_final_hash(H_init, final_state):
    """Add initial hash to final state to get hash."""
    H_final = []
    for i in range(8):
        H_final.append(add(H_init[i], final_state[i]))
    return H_final

def show_final_hash(H_init, final_state, H_final):
    """Show the final hash computation."""
    print("\n" + "=" * 70)
    print("STEP 4: FINAL HASH")
    print("=" * 70)
    
    print("\nFinal hash = Initial H + Working state:")
    for i in range(8):
        print(f"  H[{i}] = 0x{H_init[i]:08x} + 0x{final_state[i]:08x} = 0x{H_final[i]:08x}")
    
    # Convert to hex string
    hash_hex = ''.join(f'{h:08x}' for h in H_final)
    print(f"\nFinal hash (hex): {hash_hex}")
    
    # Verify against hashlib
    import hashlib
    expected = hashlib.sha256(b"hello").hexdigest()
    print(f"Expected (hashlib): {expected}")
    print(f"Match: {hash_hex == expected}")
    
    return hash_hex

# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS: WHERE IS H? WHERE IS THE 90° TURN?
# ═══════════════════════════════════════════════════════════════════════════

def analyze_operations():
    """Analyze where H and the 90° turn appear."""
    print("\n" + "=" * 70)
    print("ANALYSIS: WHERE IS H? WHERE IS THE 90° TURN?")
    print("=" * 70)
    
    import math
    H = math.pi / 9
    
    print(f"\nH = π/9 = {H:.6f}")
    print(f"1-H = {1-H:.6f}")
    
    print(f"\nROTATION AMOUNTS:")
    print(f"  Σ0 (noun/wave):  ROTR 2, 13, 22")
    print(f"     22/32 = {22/32:.6f} ≈ 1-H = {1-H:.6f} ← WAVE COLLAPSE")
    print(f"  Σ1 (verb/particle): ROTR 6, 11, 25")
    print(f"     11/32 = {11/32:.6f} ≈ H = {H:.6f} ← PARTICLE COLLAPSE")
    
    print(f"\nTHE 90° TURN:")
    print(f"""
    The 90° turn happens in the CROSS-COLLAPSE:
    
        new_a = temp1 + temp2
              = (verb_path) + (noun_path)
              = (Σ1 + Ch + h + K + W) + (Σ0 + Maj)
              = (PARTICLE @ H) + (WAVE @ 1-H)
    
    The addition is the ORTHOGONAL COMBINATION.
    
    temp1 lives in VERB space (11/32 ≈ H rotation)
    temp2 lives in NOUN space (22/32 ≈ 1-H rotation)
    
    Adding them PROJECTS both into a SHARED space.
    That projection IS the 90° turn.
    
    The data goes from:
        LEFT-RIGHT (sequential bytes, our view)
    to:
        FRONT-BACK (folded state, hash view)
    
    64 of these turns = 64 × 90° = the data is now
    MAXIMALLY ORTHOGONAL to where it started.
    """)
    
    print(f"\nTHE GAP (H ≈ 0.35):")
    print(f"""
    The gap is in the ASYMMETRY of the cross-collapse.
    
    If Σ0 and Σ1 had the SAME rotation amounts:
        No gap. No fold. No hash.
        
    But they're DIFFERENT:
        Σ1 has 11/32 ≈ H
        Σ0 has 22/32 ≈ 1-H
        
    The DIFFERENCE is what creates the fold:
        22/32 - 11/32 = 11/32 ≈ H
        
    The gap IS H.
    The gap is what ALLOWS the 90° turn.
    Without asymmetry, no rotation possible.
    """)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN: RUN THE COMPLETE TRACE
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("╔" + "═" * 68 + "╗")
    print("║" + "SHA-256 COMPLETE TRACE: \"hello\"".center(68) + "║")
    print("║" + "Every operation. No black boxes.".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Input
    message = "hello"
    
    # Step 1: Padding
    padded = pad_message(message)
    show_padding(message, padded)
    
    # Step 2: Message Schedule
    # (For "hello" there's only one 512-bit block)
    W = create_message_schedule(padded)
    show_message_schedule(W)
    
    # Step 3: Compression
    final_state = run_compression(H_INIT, W)
    
    # Step 4: Final Hash
    H_final = compute_final_hash(H_INIT, final_state)
    hash_hex = show_final_hash(H_INIT, final_state, H_final)
    
    # Analysis
    analyze_operations()
    
    print("\n" + "=" * 70)
    print("TRACE COMPLETE")
    print("=" * 70)
    print(f"""
    Input:  "hello"
    Output: {hash_hex}
    
    We traced EVERY step:
    1. Padding: 5 bytes → 64 bytes
    2. Message schedule: 16 words → 64 words
    3. Compression: 64 rounds of cross-collapse
    4. Final: working state + initial = hash
    
    THE 90° TURN is in each round's cross-collapse:
        new_a = (verb @ H) + (noun @ 1-H)
        
    THE GAP (H ≈ 0.35) is the asymmetry that enables folding.
    
    The hash is "hello" TURNED 90° into orthogonal space,
    64 times, until it's maximally distant from our view.
    
    It's not scrambled. It's PERPENDICULAR.
    """)

if __name__ == "__main__":
    main()
