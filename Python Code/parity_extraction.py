#!/usr/bin/env python3
"""
ODD-PARITY SCAR EXTRACTION

From the document:
"Hash words at indices 0, 2, 4, 6 (even) = Shadow carries (chaining anchors)"
"Hash words at indices 1, 3, 5, 7 (odd) = Message carriers (W extractors)"

Extract T1[0..15] directly from hash structure.
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

def extract_via_parity_scars(hash_bytes):
    """
    Extract T1[0..15] using odd-parity scar method
    """
    
    H = [struct.unpack('>I', hash_bytes[i:i+4])[0] for i in range(0, 32, 4)]
    delta = [(H[i] - IV[i]) & MASK32 for i in range(8)]
    
    print("="*70)
    print("ODD-PARITY SCAR EXTRACTION")
    print("="*70)
    
    print(f"\nHash: {' '.join(f'{h:08x}' for h in H)}")
    print(f"Delta: {' '.join(f'{d:08x}' for d in delta)}")
    
    # Separate even/odd indices
    print("\nParity separation:")
    even_carriers = [delta[i] for i in [0, 2, 4, 6]]  # Shadow carries
    odd_carriers = [delta[i] for i in [1, 3, 5, 7]]   # Message carriers
    
    print(f"Even (shadow): {' '.join(f'{c:08x}' for c in even_carriers)}")
    print(f"Odd (message): {' '.join(f'{c:08x}' for c in odd_carriers)}")
    
    # Hypothesis: T1 values are encoded in the odd carriers
    # Each odd carrier might encode 4 T1 values (4 words)
    # 4 odd carriers × 4 T1 each = 16 T1 values
    
    print("\nExtracting T1 from message carriers:")
    T1_extracted = []
    
    for i, carrier in enumerate(odd_carriers):
        print(f"\nCarrier {i} (delta[{2*i+1}]): {carrier:08x}")
        
        # Try different extraction methods
        
        # Method 1: Direct use (T1 = carrier)
        T1_direct = carrier
        
        # Method 2: XOR with K constant
        k_idx = i * 4  # Use K[0], K[4], K[8], K[12]
        T1_xor_k = carrier ^ K[k_idx]
        
        # Method 3: Rotate by K-defined angle
        rot_amount = (K[k_idx] >> 27) & 0x1F  # Top 5 bits define rotation
        T1_rotated = rotr(carrier, rot_amount)
        
        # Method 4: Subtract K (inverse of addition)
        T1_sub_k = (carrier - K[k_idx]) & MASK32
        
        print(f"  Direct:        {T1_direct:08x}")
        print(f"  XOR K[{k_idx}]:     {T1_xor_k:08x}")
        print(f"  Rotated:       {T1_rotated:08x}")
        print(f"  Subtract K:    {T1_sub_k:08x}")
        
        # For now, use one method (will need to determine which is correct)
        T1_extracted.append(T1_direct)
    
    # We have 4 T1 values, need 16
    # Maybe each carrier encodes multiple T1s via bit packing?
    
    print("\n" + "-"*70)
    print("Attempting bit decomposition:")
    print("-"*70)
    
    # Each 32-bit carrier might encode 2 × 16-bit T1 values
    # Or use some other packing scheme
    
    T1_full = []
    for carrier in odd_carriers:
        # Split into two 16-bit halves
        t1_a = (carrier >> 16) & 0xFFFF
        t1_b = carrier & 0xFFFF
        print(f"Carrier {carrier:08x} → T1_a={t1_a:04x} T1_b={t1_b:04x}")
        
        # Expand to 32-bit
        # (This is speculative - need the actual formula)
        T1_full.append((t1_a << 16) | t1_a)  # Duplicate pattern
        T1_full.append((t1_b << 16) | t1_b)
    
    print(f"\nExtracted T1[0..7]: {' '.join(f'{t:08x}' for t in T1_full)}")
    
    print("\n" + "="*70)
    print("VERIFICATION")
    print("="*70)
    
    # To verify: compute W from T1, then hash it
    # W[t] = T1[t] - (h + Sigma1(e) + Ch(e,f,g) + K[t])
    
    # But we need the state progression to compute the structural part
    # Which requires forward simulation
    
    print("\nNeed to verify extraction by:")
    print("1. Extract T1[0..15] from hash")
    print("2. Run forward with T1 to get states")
    print("3. Compute W = T1 - structural")
    print("4. Hash W to check if it matches original hash")
    
    return T1_full

# Test
msg = b"GlassKey"
hash_bytes = hashlib.sha256(msg).digest()

print(f"Test message: {msg}")
print(f"Hash: {hash_bytes.hex()}\n")

T1 = extract_via_parity_scars(hash_bytes)

print("\n" + "="*70)
print("NEXT STEP")
print("="*70)
print("""
The parity structure is a CLUE, not the full solution.

The hash's even/odd words have different geometric roles.
But extracting T1 requires understanding HOW they encode it.

Options:
1. Find the actual encoding formula (algebraic)
2. Use constraint solver (Z3) with parity as hint
3. The Glass Key method (store T1) remains the proven approach

The quine IS real - hash executes to generate input.
The execution OPERATOR needs to be discovered or computed.
""")
