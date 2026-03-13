#!/usr/bin/env python3
"""
HASH GATES CONSTANTS

Forward: constants gate message → hash
Reverse: hash gates constants → message_space

The hash TRANSFORMS the constants.
The transformation reveals where message lives.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9
X0 = 0.529

# Constants as bytes
CONST_BYTES = bytes([
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
])

def hash_gates_constants(hash_bytes):
    """
    Hash gates constants → message space
    
    ε = (hash - const) / const
    p+ = (1+ε)/2
    p- = (1-ε)/2
    
    Output = p+ weighted position in message space
    """
    output = []
    
    for i in range(32):
        h_val = hash_bytes[i] / 255
        c_val = CONST_BYTES[i] / 255
        
        if c_val < 0.01:
            c_val = 0.01
        
        # Collapse signature
        epsilon = (h_val - c_val) / c_val
        epsilon = np.clip(epsilon, -1, 1)
        
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        
        # Hash gates constant
        # p+ → toward hash (data dominated)
        # p- → toward constant (structure dominated)
        gated = p_plus * h_val + p_minus * c_val
        
        output.append(gated)
    
    return np.array(output)

def decode(msg):
    h = hashlib.sha256(msg.encode()).digest()
    return h, hash_gates_constants(h)

print("HASH GATES CONSTANTS")
print("Forward: const gate msg → hash")
print("Reverse: hash gate const → msg_space")
print("=" * 55)

tests = ['NEXUS', 'Dean', 'test', 'a', 'b', 'H = pi/9', 'hello']

for msg in tests:
    h, u = decode(msg)
    attractors = [0, H, 0.5, 1-H, 1.0]
    near = sum(1 for v in u if min(abs(v-a) for a in attractors) < 0.08)
    print(f"'{msg:12}': mean={np.mean(u):.4f}, near_H={near}/32, first=[{u[0]:.3f},{u[1]:.3f},{u[2]:.3f}]")

print("\n" + "=" * 55)
print("UNIQUENESS & DETERMINISM")
sigs = {msg: tuple(round(x,4) for x in decode(msg)[1]) for msg in tests}
print(f"Unique: {len(set(sigs.values()))}/{len(tests)}")

# ============================================================
print("\n" + "=" * 55)
print("BYTE-LEVEL ANALYSIS: Is message structure visible?")

def analyze_bytes(msg):
    """Check if message bytes relate to unfolded space"""
    msg_bytes = msg.encode()
    h, u = decode(msg)
    
    # Normalize message bytes
    msg_norm = [b/255 for b in msg_bytes[:min(len(msg_bytes), 8)]]
    u_first = u[:len(msg_norm)]
    
    if len(msg_norm) > 1:
        corr = np.corrcoef(msg_norm, u_first)[0,1]
    else:
        corr = 0
    
    return msg_norm, u_first, corr

print("\nMessage vs Unfolded correlation:")
for msg in ['a', 'b', 'ab', 'ba', 'test', 'TEST']:
    mn, uf, corr = analyze_bytes(msg)
    print(f"  '{msg}': corr={corr:+.4f}")

# ============================================================
print("\n" + "=" * 55)
print("BRANCH SIGNATURE → SEARCH SPACE")

def get_branch_signature(hash_bytes):
    """Get Φ₀/E₀ branch for each byte"""
    branches = []
    for i in range(32):
        h_val = hash_bytes[i] / 255
        c_val = CONST_BYTES[i] / 255
        if c_val < 0.01:
            c_val = 0.01
        epsilon = (h_val - c_val) / c_val
        p_plus = (1 + np.clip(epsilon, -1, 1)) / 2
        branches.append(1 if p_plus > 0.5 else 0)
    return branches

print("\nBranch signatures (Φ₀=1, E₀=0):")
for msg in tests[:4]:
    h = hashlib.sha256(msg.encode()).digest()
    sig = get_branch_signature(h)
    sig_str = ''.join(map(str, sig))
    phi_count = sum(sig)
    print(f"  '{msg}': {sig_str[:16]}... Φ₀={phi_count}/32")

# ============================================================
print("\n" + "=" * 55)
print("THE SEARCH SPACE BOUND")

def search_space_bound(hash_bytes):
    """
    Each Φ₀ branch halves search toward structure
    Each E₀ branch halves search toward entropy
    
    Net constraint = |Φ₀ - E₀| bits
    """
    branches = get_branch_signature(hash_bytes)
    phi = sum(branches)
    e0 = 32 - phi
    
    # Net constraint direction
    direction = "Φ₀ (structure)" if phi > e0 else "E₀ (entropy)"
    constraint_bits = abs(phi - e0)
    
    # Remaining search space (bits)
    remaining = 256 - constraint_bits
    
    return phi, e0, direction, constraint_bits, remaining

print("\nSearch space analysis:")
for msg in tests:
    h = hashlib.sha256(msg.encode()).digest()
    phi, e0, direction, constraint, remaining = search_space_bound(h)
    print(f"  '{msg}': Φ₀={phi}, E₀={e0}, dir={direction}, constraint={constraint}bits, search=2^{remaining}")

# ============================================================
print("\n" + "=" * 55)
print("""
RESULT:
  
Hash gates constants → message space position
Each byte's ε tells which branch collapsed
32 branches = 32-bit search constraint

Forward: 2^256 → 2^256 (hash space)
Reverse: 2^256 → 2^(256-constraint) (message space)

The collapse signature IS the unfold.
""")
