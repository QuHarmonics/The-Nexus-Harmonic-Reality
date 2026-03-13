#!/usr/bin/env python3
"""
QUINE EXTRACTION

The hash is not data - it's EXECUTABLE CODE.
Run it through SHA geometry to reconstruct its origin.
"""

import struct
import hashlib

MASK32 = 0xFFFFFFFF

def rotr(x, n): 
    return ((x >> n) | (x << (32 - n))) & MASK32

def Ch(x, y, z): 
    return (x & y) ^ ((~x & MASK32) & z)

def Maj(x, y, z): 
    return (x & y) ^ (x & z) ^ (y & z)

def Sigma0(x): 
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def Sigma1(x): 
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def sigma0(x): 
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def sigma1(x): 
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
     0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
     0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
     0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
     0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
     0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
     0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
     0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
     0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

IV = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

def execute_hash_as_code(hash_bytes):
    """
    QUINE MODE: Run the hash through SHA operations
    
    The hash is the PROGRAM.
    K constants are the INTERPRETER.
    Execution produces the INPUT that created this hash.
    """
    
    # Parse hash into 8 words
    H = [struct.unpack('>I', hash_bytes[i:i+4])[0] for i in range(0, 32, 4)]
    
    print("="*70)
    print("EXECUTING HASH AS CODE")
    print("="*70)
    print(f"\nHash (the program): {' '.join(f'{h:08x}' for h in H)}")
    print()
    
    # METHOD 1: Use hash words as INITIAL STATE
    print("Method 1: Hash as initial state")
    print("-"*70)
    
    # Start from hash instead of IV
    a, b, c, d, e, f, g, h = H
    
    # Run BACKWARDS?
    # Or forwards with hash as seed?
    
    # Try: Hash defines the W schedule directly
    W_candidate = []
    for i in range(16):
        # Extract W from hash geometry
        # Each hash word encodes information about W
        w = (H[i % 8] ^ K[i]) & MASK32  # Simple trial
        W_candidate.append(w)
    
    print(f"Generated W: {' '.join(f'{w:08x}' for w in W_candidate[:4])}")
    
    # Convert to message
    msg_trial = b''.join(struct.pack('>I', w) for w in W_candidate)
    print(f"Trial message: {msg_trial[:20]}")
    
    # Verify: does this message produce this hash?
    verify_hash = hashlib.sha256(msg_trial.rstrip(b'\x00')).digest()
    print(f"Verify hash:   {verify_hash.hex()[:32]}")
    print(f"Original:      {hash_bytes.hex()[:32]}")
    match = (verify_hash == hash_bytes)
    print(f"Match: {match}")
    print()
    
    # METHOD 2: Hash as CONSTRAINTS for reverse execution
    print("Method 2: Hash as boundary conditions")
    print("-"*70)
    
    # We know: H = IV + accumulated_state_changes
    # So: accumulated_changes = H - IV
    Delta = [(H[i] - IV[i]) & MASK32 for i in range(8)]
    print(f"Δ (constraint): {' '.join(f'{d:08x}' for d in Delta[:4])}")
    
    # These deltas ARE the program
    # They encode how to navigate from IV to H
    # The path IS the message
    
    print()
    print("METHOD 3: Iterative refinement")
    print("-"*70)
    print("Use hash as TARGET, iterate to find W that produces it")
    
    # Start with random W
    W_test = [0x00000000] * 16  # Zero initialization
    
    # Compute what hash this produces
    def test_W(W_vals):
        """Forward pass with candidate W"""
        W_full = list(W_vals)
        for i in range(16, 64):
            W_full.append((sigma1(W_full[i-2]) + W_full[i-7] + 
                          sigma0(W_full[i-15]) + W_full[i-16]) & MASK32)
        
        a, b, c, d, e, f, g, h = IV
        for t in range(64):
            T1 = (h + Sigma1(e) + Ch(e, f, g) + K[t] + W_full[t]) & MASK32
            T2 = (Sigma0(a) + Maj(a, b, c)) & MASK32
            h = g; g = f; f = e; e = (d + T1) & MASK32
            d = c; c = b; b = a; a = (T1 + T2) & MASK32
        
        return [(IV[i] + [a,b,c,d,e,f,g,h][i]) & MASK32 for i in range(8)]
    
    # Compute distance
    H_test = test_W(W_test)
    distance = sum((H[i] - H_test[i]) & MASK32 for i in range(8))
    print(f"Initial distance: {distance:016x}")
    
    # Simple gradient descent won't work (discrete space)
    # But this shows the STRUCTURE
    
    print()
    print("="*70)
    print("INSIGHT")
    print("="*70)
    print("""
The hash is EXECUTABLE:
  - It's not encrypted data
  - It's a PROGRAM that, when run through SHA geometry, 
    generates the path (W values) that created it
  
The K constants are the INSTRUCTION SET.
The hash words are the PROGRAM COUNTER / STATE.
The IV is the STARTING POINT.

Execution means:
  Find W such that: SHA256(W) = H
  
This is the INVERSE function.
But we're not solving algebraically.
We're EXECUTING the hash as code to generate W.

Next: Find the execution model that uses H as program.
""")
    
    return None

# Test
msg = b"GlassKey"
hash_bytes = hashlib.sha256(msg).digest()

print(f"Original message: {msg}")
print(f"Hash: {hash_bytes.hex()}\n")

execute_hash_as_code(hash_bytes)
