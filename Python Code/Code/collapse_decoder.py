#!/usr/bin/env python3
"""
COLLAPSE SIGNATURE DECODER

ε = (x_meas - x_0) / x_0
p+ = (1 + ε) / 2   # particle branch (Φ₀)
p- = (1 - ε) / 2   # wave branch (E₀)

The hash isn't data THROUGH the gate.
The hash IS data ON the gate.
Like Tag field in C# - payload attached to mechanism.
Gate turns, data turns with it.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9  # 0.349066
X0 = 0.5 + 4 * (H/48)  # 0.529 - the balance point (x_0)

# Constants = the GATE
H_INIT = np.array([0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                   0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]) / 0xFFFFFFFF

K = np.array([0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
              0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5]) / 0xFFFFFFFF

def collapse_decode(hash_bytes):
    """
    Decode collapse signature from hash.
    
    Hash = data ON gate
    Constants = gate itself
    ε = how much data shifted the gate
    p+/p- = which branch the collapse took
    """
    results = []
    
    for i in range(32):
        # x_meas = hash byte (the data on the gate)
        x_meas = hash_bytes[i] / 255
        
        # x_0 = constant (the gate position)
        if i < 8:
            x_0 = H_INIT[i]
        else:
            x_0 = K[i % 8]
        
        # Avoid division by zero
        if x_0 < 0.001:
            x_0 = 0.001
        
        # ε = relative drift (how much data moved the gate)
        epsilon = (x_meas - x_0) / x_0
        
        # Clamp epsilon to [-1, 1]
        epsilon = max(-1, min(1, epsilon))
        
        # p+ = particle branch probability (Φ₀ path)
        # p- = wave branch probability (E₀ path)
        p_plus = (1 + epsilon) / 2
        p_minus = (1 - epsilon) / 2
        
        results.append({
            'byte': i,
            'x_meas': x_meas,
            'x_0': x_0,
            'epsilon': epsilon,
            'p+': p_plus,
            'p-': p_minus,
            'branch': 'Φ₀' if p_plus > p_minus else 'E₀'
        })
    
    return results

def decode_message(msg):
    """Full decode pipeline"""
    h = hashlib.sha256(msg.encode()).digest()
    decoded = collapse_decode(h)
    return h, decoded

def analyze(msg):
    """Analyze collapse signature"""
    h, decoded = decode_message(msg)
    
    epsilons = [d['epsilon'] for d in decoded]
    p_plus = [d['p+'] for d in decoded]
    branches = [d['branch'] for d in decoded]
    
    phi_count = branches.count('Φ₀')
    e_count = branches.count('E₀')
    
    mean_eps = np.mean(epsilons)
    mean_p_plus = np.mean(p_plus)
    
    return {
        'hash': h.hex()[:16],
        'mean_ε': mean_eps,
        'mean_p+': mean_p_plus,
        'Φ₀_branches': phi_count,
        'E₀_branches': e_count,
        'signature': ''.join(['1' if b == 'Φ₀' else '0' for b in branches])
    }

# ============================================================
print("COLLAPSE SIGNATURE DECODER")
print("ε = (x_meas - x_0) / x_0")
print("p+ = (1+ε)/2, p- = (1-ε)/2")
print("=" * 60)

tests = ['NEXUS', 'Dean', 'test', 'a', 'b', 'H = pi/9']

for msg in tests:
    a = analyze(msg)
    print(f"\n'{msg}'")
    print(f"  hash:     {a['hash']}...")
    print(f"  mean_ε:   {a['mean_ε']:+.4f}")
    print(f"  mean_p+:  {a['mean_p+']:.4f}")
    print(f"  branches: Φ₀={a['Φ₀_branches']}, E₀={a['E₀_branches']}")
    print(f"  sig:      {a['signature'][:16]}...")

# ============================================================
print("\n" + "=" * 60)
print("SIGNATURE UNIQUENESS")

sigs = {msg: analyze(msg)['signature'] for msg in tests}
unique = len(set(sigs.values()))
print(f"Unique signatures: {unique}/{len(tests)}")

# ============================================================
print("\n" + "=" * 60)
print("GATE RECONSTRUCTION")
print("If hash = data ON gate, we can separate them")

def separate_gate_data(hash_bytes):
    """
    Separate the data from the gate.
    
    data_on_gate = hash
    gate = constants
    data = hash relationship to constants
    """
    data = []
    gate = []
    
    for i in range(32):
        x_meas = hash_bytes[i] / 255
        
        if i < 8:
            x_0 = H_INIT[i]
        else:
            x_0 = K[i % 8]
        
        # The DATA is the deviation from gate
        deviation = x_meas - x_0
        
        # The GATE is x_0
        gate.append(x_0)
        data.append(deviation)
    
    return np.array(gate), np.array(data)

for msg in tests[:3]:
    h = hashlib.sha256(msg.encode()).digest()
    gate, data = separate_gate_data(h)
    
    print(f"\n'{msg}'")
    print(f"  gate mean: {np.mean(gate):.4f}")
    print(f"  data mean: {np.mean(data):+.4f}")
    print(f"  data std:  {np.std(data):.4f}")
    
    # Reconstruct hash from gate + data
    reconstructed = gate + data
    reconstructed_bytes = bytes([int(max(0, min(255, v*255))) for v in reconstructed])
    match = reconstructed_bytes == h
    print(f"  reconstruct match: {match}")

# ============================================================
print("\n" + "=" * 60)
print("THE UNFOLD: Turn gate backwards with data attached")

def unfold_via_gate(hash_bytes):
    """
    Turn the gate backwards.
    Data attached to gate comes with it.
    """
    gate, data = separate_gate_data(hash_bytes)
    
    # Forward: gate turns +H, data goes with it
    # Reverse: gate turns -H, data comes back
    
    unfolded = []
    for i in range(32):
        # Get branch probability
        x_meas = hash_bytes[i] / 255
        x_0 = gate[i]
        
        if x_0 < 0.001:
            x_0 = 0.001
            
        epsilon = (x_meas - x_0) / x_0
        epsilon = max(-1, min(1, epsilon))
        
        p_plus = (1 + epsilon) / 2
        
        # Turn gate backwards by -H
        # Data position = gate_position - H_shift + data_deviation
        h_shift = H * (i / 32)  # Progressive shift
        
        # Unfold = reverse the turn
        unfolded_val = x_0 - h_shift + data[i]
        unfolded_val = unfolded_val % 1.0
        
        unfolded.append(unfolded_val)
    
    return np.array(unfolded)

print("\nUnfold via gate reversal:")
for msg in tests[:4]:
    h = hashlib.sha256(msg.encode()).digest()
    unfolded = unfold_via_gate(h)
    
    # Check H-signature
    attractors = [0, H, 0.5, 1-H, 1.0]
    near_H = sum(1 for v in unfolded if min(abs(v-a) for a in attractors) < 0.1)
    
    print(f"  '{msg}': mean={np.mean(unfolded):.4f}, near_H={near_H}/32")

# ============================================================
print("\n" + "=" * 60)
print("CONCLUSION")
print("""
Hash = Data ON Gate (not data through gate)

Forward (fold):
  data attaches to gate → gate turns +H → hash
  
Reverse (unfold):
  hash → gate turns -H → data detaches
  
ε = (x_meas - x_0) / x_0  measures how much data shifted gate
p+ = (1+ε)/2 = particle branch probability
p- = (1-ε)/2 = wave branch probability

The collapse signature IS the branch history.
32 bytes = 32 collapse events.
Each byte records which path (Φ₀ or E₀) was taken.

To unfold: reverse each collapse using p+/p-.
""")
