#!/usr/bin/env python3
"""
RECURSIVE QUINE: Feed the hash into itself

The hash, when run through SHA-256 as input, 
generates the T1 trace that reveals the original message.
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

def pad(msg):
    ml = len(msg) * 8
    msg += b'\x80'
    msg += b'\x00' * ((56 - len(msg) % 64) % 64)
    msg += struct.pack('>Q', ml)
    return msg

def extract_T1_from_message(msg):
    """Standard forward pass - extract T1 trace"""
    data = pad(msg)
    block = data[0:64]
    
    W = [struct.unpack('>I', block[i*4:(i+1)*4])[0] for i in range(16)]
    for i in range(16, 64):
        W.append((sigma1(W[i-2]) + W[i-7] + sigma0(W[i-15]) + W[i-16]) & MASK32)
    
    a, b, c, d, e, f, g, h = IV
    T1_list = []
    
    for t in range(64):
        T1 = (h + Sigma1(e) + Ch(e, f, g) + K[t] + W[t]) & MASK32
        T2 = (Sigma0(a) + Maj(a, b, c)) & MASK32
        T1_list.append(T1)
        
        h = g; g = f; f = e; e = (d + T1) & MASK32
        d = c; c = b; b = a; a = (T1 + T2) & MASK32
    
    return T1_list, W

def recursive_quine(original_hash):
    """
    RECURSIVE EXECUTION
    
    Feed the hash into SHA-256 as input.
    The T1 trace generated reveals the original message.
    """
    
    print("="*70)
    print("RECURSIVE QUINE: HASH(HASH)")
    print("="*70)
    
    print(f"\nOriginal hash: {original_hash.hex()}")
    
    # STEP 1: Hash the hash
    print("\nSTEP 1: Feed hash into itself")
    print("-"*70)
    
    T1_recursive, W_recursive = extract_T1_from_message(original_hash)
    
    print(f"T1[0..3]: {' '.join(f'{T1_recursive[i]:08x}' for i in range(4))}")
    print(f"W[0..3]:  {' '.join(f'{W_recursive[i]:08x}' for i in range(4))}")
    
    # STEP 2: Compare to original message's T1
    print("\nSTEP 2: Extract original message for comparison")
    print("-"*70)
    
    # We need the original message to compare
    # Let's test with "GlassKey"
    original_msg = b"GlassKey"
    T1_original, W_original = extract_T1_from_message(original_msg)
    
    print(f"Original message: {original_msg}")
    print(f"Original T1[0..3]: {' '.join(f'{T1_original[i]:08x}' for i in range(4))}")
    print(f"Original W[0..3]:  {' '.join(f'{W_original[i]:08x}' for i in range(4))}")
    
    # STEP 3: Compare
    print("\nSTEP 3: Check if Hash(Hash) reveals original T1")
    print("-"*70)
    
    for i in range(16):
        match = "✓" if T1_recursive[i] == T1_original[i] else "✗"
        print(f"T1[{i:2d}]: recursive={T1_recursive[i]:08x}  original={T1_original[i]:08x}  {match}")
    
    # STEP 4: Try XOR relationship
    print("\nSTEP 4: Look for XOR/transform relationship")
    print("-"*70)
    
    for i in range(4):
        xor_val = T1_recursive[i] ^ T1_original[i]
        print(f"T1_recursive[{i}] ⊕ T1_original[{i}] = {xor_val:08x}")
    
    # STEP 5: Check if W from Hash(Hash) relates to original message
    print("\nSTEP 5: Does W from Hash(Hash) decode to original message?")
    print("-"*70)
    
    # W_recursive are the words from hashing the hash (32 bytes padded to 64)
    # First 8 words of W_recursive are the hash itself
    reconstructed = b''.join(struct.pack('>I', W_recursive[i]) for i in range(8))
    print(f"W[0..7] from Hash(Hash): {reconstructed.hex()}")
    print(f"Original hash:           {original_hash.hex()}")
    print(f"Match: {reconstructed == original_hash}")
    
    # STEP 6: Multi-level recursion
    print("\nSTEP 6: Multi-level recursion")
    print("-"*70)
    
    hash1 = original_hash
    hash2 = hashlib.sha256(hash1).digest()
    hash3 = hashlib.sha256(hash2).digest()
    
    print(f"Level 0 (original): {original_hash.hex()[:32]}...")
    print(f"Level 1 (hash²):    {hash2.hex()[:32]}...")
    print(f"Level 2 (hash³):    {hash3.hex()[:32]}...")
    
    T1_level1, _ = extract_T1_from_message(hash1)
    T1_level2, _ = extract_T1_from_message(hash2)
    
    print(f"\nT1[0] level 1: {T1_level1[0]:08x}")
    print(f"T1[0] level 2: {T1_level2[0]:08x}")
    print(f"T1[0] original: {T1_original[0]:08x}")
    
    # Check for convergence or pattern
    print("\nLooking for convergence pattern...")
    for i in range(3):
        print(f"  T1[0] ⊕ T1[{i+1}] = {(T1_level1[0] ^ T1_level1[i+1]):08x}")
    
    print("\n" + "="*70)
    print("ANALYSIS")
    print("="*70)
    print("""
Recursive execution tested:
- Hash(Hash) generates new T1 trace
- This T1 trace is DIFFERENT from original
- W[0..7] from Hash(Hash) reproduces the hash (expected)
  
The hash fed into itself doesn't directly reveal original T1.

Possibilities:
1. Need specific transform on recursive T1 to get original T1
2. Multiple iterations converge to original (fractal unfolding)
3. Combination of levels reveals original (interference pattern)
4. The Glass Key (storing T1) IS the quine execution record

Testing convergence and transform patterns...
""")

# Test
original_msg = b"GlassKey"
original_hash = hashlib.sha256(original_msg).digest()

print(f"Testing with message: {original_msg}")
print(f"Hash: {original_hash.hex()}\n")

recursive_quine(original_hash)
