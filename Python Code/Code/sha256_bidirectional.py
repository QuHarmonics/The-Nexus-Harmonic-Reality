#!/usr/bin/env python3
"""
SHA-256 COMPLETE IMPLEMENTATION
===============================

Full SHA-256 with:
- Forward hashing (standard)
- Round-by-round state tracking
- Individual round reversal
- Meet-in-the-middle support

The constants ARE the computer.
The data flows through.
The CPU runs both directions.

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
"""

import struct
from typing import List, Tuple, Optional
from constants import H_INIT, K, MASK_32

# ============================================================================
# PRIMITIVE OPERATIONS
# ============================================================================

def rotr(x: int, n: int) -> int:
    """Rotate right (32-bit)"""
    return ((x >> n) | (x << (32 - n))) & MASK_32

def rotl(x: int, n: int) -> int:
    """Rotate left (32-bit) - INVERSE of rotr"""
    return ((x << n) | (x >> (32 - n))) & MASK_32

def shr(x: int, n: int) -> int:
    """Shift right (logical)"""
    return x >> n

def add32(*args) -> int:
    """Add multiple values mod 2^32"""
    result = 0
    for a in args:
        result = (result + a) & MASK_32
    return result

def sub32(a: int, b: int) -> int:
    """Subtract mod 2^32 - INVERSE of add"""
    return (a - b) & MASK_32

# ============================================================================
# SHA-256 FUNCTIONS
# ============================================================================

def ch(e: int, f: int, g: int) -> int:
    """Choice function: if e then f else g"""
    return (e & f) ^ (~e & g) & MASK_32

def maj(a: int, b: int, c: int) -> int:
    """Majority function"""
    return (a & b) ^ (a & c) ^ (b & c)

def Sigma0(x: int) -> int:
    """Big sigma 0 (compression)"""
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def Sigma1(x: int) -> int:
    """Big sigma 1 (compression)"""
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def sigma0(x: int) -> int:
    """Small sigma 0 (message schedule)"""
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def sigma1(x: int) -> int:
    """Small sigma 1 (message schedule)"""
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

# ============================================================================
# MESSAGE SCHEDULE
# ============================================================================

def create_message_schedule(block: bytes) -> List[int]:
    """
    Create message schedule W[0..63] from 512-bit block.
    
    W[0..15] = message block words (direct from input)
    W[16..63] = derived from W[0..15] via recurrence
    """
    assert len(block) == 64, f"Block must be 64 bytes, got {len(block)}"
    
    # W[0..15] from block
    W = list(struct.unpack('>16I', block))
    
    # W[16..63] via recurrence
    for i in range(16, 64):
        w = add32(
            sigma1(W[i-2]),
            W[i-7],
            sigma0(W[i-15]),
            W[i-16]
        )
        W.append(w)
    
    return W

def expand_W16(W16: List[int]) -> List[int]:
    """Expand W[0..15] to W[0..63]"""
    assert len(W16) == 16, f"Need 16 words, got {len(W16)}"
    
    W = list(W16)
    for i in range(16, 64):
        w = add32(
            sigma1(W[i-2]),
            W[i-7],
            sigma0(W[i-15]),
            W[i-16]
        )
        W.append(w)
    
    return W

# ============================================================================
# PADDING
# ============================================================================

def pad_message(message: bytes) -> bytes:
    """
    SHA-256 padding:
    1. Append bit '1' (0x80)
    2. Append zeros until length ≡ 448 (mod 512)
    3. Append original length as 64-bit big-endian
    """
    ml = len(message) * 8  # Message length in bits
    
    # Append 0x80
    padded = message + b'\x80'
    
    # Append zeros until length ≡ 56 (mod 64)
    while len(padded) % 64 != 56:
        padded += b'\x00'
    
    # Append length as 64-bit big-endian
    padded += struct.pack('>Q', ml)
    
    return padded

def unpad_message(padded: bytes, original_length: int) -> bytes:
    """Remove SHA-256 padding"""
    return padded[:original_length]

# ============================================================================
# SINGLE ROUND - FORWARD
# ============================================================================

def sha256_round_forward(
    state: Tuple[int, ...],
    k: int,
    w: int
) -> Tuple[int, ...]:
    """
    One forward SHA-256 compression round.
    
    State: (a, b, c, d, e, f, g, h)
    Returns: new state after round
    """
    a, b, c, d, e, f, g, h = state
    
    # Compute intermediate values
    S1 = Sigma1(e)
    ch_val = ch(e, f, g)
    temp1 = add32(h, S1, ch_val, k, w)
    
    S0 = Sigma0(a)
    maj_val = maj(a, b, c)
    temp2 = add32(S0, maj_val)
    
    # New state (registers shift down, new values enter at a and e)
    new_a = add32(temp1, temp2)
    new_b = a
    new_c = b
    new_d = c
    new_e = add32(d, temp1)
    new_f = e
    new_g = f
    new_h = g
    
    return (new_a, new_b, new_c, new_d, new_e, new_f, new_g, new_h)

# ============================================================================
# SINGLE ROUND - REVERSE
# ============================================================================

def sha256_round_reverse(
    state_after: Tuple[int, ...],
    k: int,
    w: int
) -> Tuple[int, ...]:
    """
    Reverse one SHA-256 compression round.
    
    Given state AFTER round and W value, recover state BEFORE.
    
    This is the key insight: THE CPU RUNS BOTH DIRECTIONS.
    """
    a_new, b_new, c_new, d_new, e_new, f_new, g_new, h_new = state_after
    
    # Reverse the simple register shifts
    # From forward: new_b = a_old, new_c = b_old, etc.
    a_old = b_new
    b_old = c_new
    c_old = d_new
    e_old = f_new
    f_old = g_new
    g_old = h_new
    
    # Compute temp2 (we know a_old, b_old, c_old)
    S0 = Sigma0(a_old)
    maj_val = maj(a_old, b_old, c_old)
    temp2 = add32(S0, maj_val)
    
    # Recover temp1: new_a = temp1 + temp2
    temp1 = sub32(a_new, temp2)
    
    # Recover d_old: new_e = d_old + temp1
    d_old = sub32(e_new, temp1)
    
    # Recover h_old: temp1 = h_old + S1 + ch + k + w
    S1 = Sigma1(e_old)
    ch_val = ch(e_old, f_old, g_old)
    h_old = sub32(sub32(sub32(sub32(temp1, S1), ch_val), k), w)
    
    return (a_old, b_old, c_old, d_old, e_old, f_old, g_old, h_old)

# ============================================================================
# EXTRACT W FROM STATES
# ============================================================================

def extract_W(
    state_before: Tuple[int, ...],
    state_after: Tuple[int, ...],
    k: int
) -> int:
    """
    Extract W value given states before and after a round.
    
    This is the inverse of the round function with respect to W.
    """
    a_old, b_old, c_old, d_old, e_old, f_old, g_old, h_old = state_before
    a_new, b_new, c_new, d_new, e_new, f_new, g_new, h_new = state_after
    
    # Compute temp2
    S0 = Sigma0(a_old)
    maj_val = maj(a_old, b_old, c_old)
    temp2 = add32(S0, maj_val)
    
    # Compute temp1
    temp1 = sub32(a_new, temp2)
    
    # W = temp1 - h_old - S1 - ch - K
    S1 = Sigma1(e_old)
    ch_val = ch(e_old, f_old, g_old)
    W = sub32(sub32(sub32(sub32(temp1, h_old), S1), ch_val), k)
    
    return W

# ============================================================================
# FULL COMPRESSION
# ============================================================================

def sha256_compress(
    state: Tuple[int, ...],
    W: List[int],
    track_states: bool = False
) -> Tuple[int, ...]:
    """
    Full SHA-256 compression (64 rounds).
    
    If track_states=True, returns list of all intermediate states.
    """
    if track_states:
        states = [state]
    
    for i in range(64):
        state = sha256_round_forward(state, K[i], W[i])
        if track_states:
            states.append(state)
    
    if track_states:
        return states
    return state

def sha256_compress_reverse(
    final_state: Tuple[int, ...],
    W: List[int]
) -> Tuple[int, ...]:
    """
    Reverse full SHA-256 compression (64 rounds backward).
    
    Given final state and W, recover initial state.
    """
    state = final_state
    
    for i in range(63, -1, -1):
        state = sha256_round_reverse(state, K[i], W[i])
    
    return state

# ============================================================================
# FULL HASH
# ============================================================================

def sha256_hash(message: bytes) -> bytes:
    """
    Complete SHA-256 hash.
    
    Returns 32-byte digest.
    """
    # Pad message
    padded = pad_message(message)
    
    # Initialize state
    state = tuple(H_INIT)
    
    # Process each 64-byte block
    for i in range(0, len(padded), 64):
        block = padded[i:i+64]
        W = create_message_schedule(block)
        
        # Compress
        new_state = sha256_compress(state, W)
        
        # Add to current state
        state = tuple(add32(s, h) for s, h in zip(new_state, state))
    
    # Pack as bytes
    return struct.pack('>8I', *state)

def sha256_hex(message: bytes) -> str:
    """SHA-256 hash as hex string"""
    return sha256_hash(message).hex()

# ============================================================================
# MEET IN THE MIDDLE
# ============================================================================

def forward_half(W16: List[int], rounds: int = 32) -> Tuple[int, ...]:
    """
    Forward from H_INIT for specified number of rounds.
    Returns intermediate state.
    """
    W = expand_W16(W16)
    state = tuple(H_INIT)
    
    for i in range(rounds):
        state = sha256_round_forward(state, K[i], W[i])
    
    return state

def backward_half(
    final_internal: Tuple[int, ...],
    W16: List[int],
    start_round: int = 63,
    end_round: int = 32
) -> Tuple[int, ...]:
    """
    Backward from final state for specified rounds.
    Returns intermediate state.
    
    Note: final_internal should be (hash - H_INIT), not the hash itself.
    """
    W = expand_W16(W16)
    state = final_internal
    
    for i in range(start_round, end_round - 1, -1):
        state = sha256_round_reverse(state, K[i], W[i])
    
    return state

def meet_in_middle_verify(
    target_hash: bytes,
    W16: List[int],
    meet_round: int = 32
) -> bool:
    """
    Verify that W16 produces target_hash using meet-in-the-middle.
    
    Forward rounds 0 to meet_round should equal
    Backward rounds 63 to meet_round.
    """
    # Get internal final state
    hash_words = struct.unpack('>8I', target_hash)
    internal_final = tuple(sub32(h, hi) for h, hi in zip(hash_words, H_INIT))
    
    # Forward and backward
    fwd_state = forward_half(W16, meet_round)
    bwd_state = backward_half(internal_final, W16, 63, meet_round)
    
    return fwd_state == bwd_state

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def bytes_to_W16(message: bytes) -> List[int]:
    """Convert padded message to W[0..15]"""
    padded = pad_message(message)
    return list(struct.unpack('>16I', padded[:64]))

def W16_to_bytes(W16: List[int], original_length: int) -> bytes:
    """Convert W[0..15] back to message bytes"""
    data = struct.pack('>16I', *W16)
    return data[:original_length]

def state_to_hex(state: Tuple[int, ...]) -> str:
    """Convert state tuple to hex string"""
    return ''.join(f'{w:08x}' for w in state)

def hex_to_state(hex_str: str) -> Tuple[int, ...]:
    """Convert hex string to state tuple"""
    words = [int(hex_str[i:i+8], 16) for i in range(0, 64, 8)]
    return tuple(words)

# ============================================================================
# VERIFICATION
# ============================================================================

def verify_implementation():
    """Verify SHA-256 implementation against standard"""
    import hashlib
    
    print("Verifying SHA-256 implementation...")
    
    test_cases = [
        b"",
        b"a",
        b"abc",
        b"NEXUS",
        b"The quick brown fox jumps over the lazy dog",
        b"A" * 64,  # Exactly one block
        b"B" * 65,  # Crosses block boundary
    ]
    
    for msg in test_cases:
        our_hash = sha256_hex(msg)
        std_hash = hashlib.sha256(msg).hexdigest()
        
        match = "✓" if our_hash == std_hash else "✗"
        print(f"  {match} '{msg[:20].decode() if len(msg) <= 20 else msg[:20].decode() + '...'}': {our_hash[:16]}...")
        
        if our_hash != std_hash:
            print(f"    Expected: {std_hash}")
            print(f"    Got:      {our_hash}")
    
    print("\nVerifying round reversal...")
    
    # Test round reversal
    msg = b"TEST"
    W16 = bytes_to_W16(msg)
    W = expand_W16(W16)
    
    state0 = tuple(H_INIT)
    state1 = sha256_round_forward(state0, K[0], W[0])
    state0_rev = sha256_round_reverse(state1, K[0], W[0])
    
    print(f"  Round 0 forward then reverse: {'✓' if state0 == state0_rev else '✗'}")
    
    # Test full reversal
    states = sha256_compress(tuple(H_INIT), W, track_states=True)
    state_recovered = sha256_compress_reverse(states[64], W)
    
    print(f"  Full 64-round reversal: {'✓' if states[0] == state_recovered else '✗'}")
    
    # Test meet in the middle
    target_hash = sha256_hash(msg)
    mitm_ok = meet_in_middle_verify(target_hash, W16)
    
    print(f"  Meet-in-the-middle: {'✓' if mitm_ok else '✗'}")
    
    print("\nAll verifications complete.")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    verify_implementation()
    
    print(f"\n{'='*60}")
    print("SHA-256 AS CPU")
    print(f"{'='*60}")
    print("""
The SHA-256 compression function is a CPU:
- 8 registers (a, b, c, d, e, f, g, h)
- 64 clock cycles (rounds)
- Instruction set: ROTR, XOR, ADD, AND, NOT
- Opcodes: K[0..63] constants

The CPU runs BOTH DIRECTIONS:
- Forward: sha256_round_forward()
- Reverse: sha256_round_reverse()

Given W, any round can be reversed.
Given states, W can be extracted.

The constants ARE the computer.
The data flows through.
The mixing is deterministic ROUTING.
""")
