"""
Z3 SHA-256 PREIMAGE: CONSTRAINT SATISFACTION, NOT BRUTE FORCE
==============================================================
The backward walk proved the geometry is invertible.
Now: let Z3 propagate constraints through the algebraic structure
instead of testing candidates.

Key structural advantages over generic SHA-256 SAT:
1. W[1..14] = 0 for short messages (massive constraint reduction)
2. W[16] = W[0] (schedule echo — solver sees the redundancy)
3. 6/8 state_1 words are H0 constants (192-bit early checkpoint)
4. T1_round0 = CONST + W[0] (linear leverage at round 0)

The solver doesn't iterate. It propagates.
"""

from z3 import *
import hashlib
import struct
import time
import sys

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

M32 = 0xFFFFFFFF

def ror32(x, n):
    return RotateRight(x, n)

def z3_Sigma0(x): return ror32(x,2) ^ ror32(x,13) ^ ror32(x,22)
def z3_Sigma1(x): return ror32(x,6) ^ ror32(x,11) ^ ror32(x,25)
def z3_gamma0(x): return ror32(x,7) ^ ror32(x,18) ^ LShR(x,3)
def z3_gamma1(x): return ror32(x,17) ^ ror32(x,19) ^ LShR(x,10)
def z3_Ch(e,f,g): return (e & f) ^ (~e & g)
def z3_Maj(a,b,c): return (a & b) ^ (a & c) ^ (b & c)

BV = lambda name: BitVec(name, 32)
BVC = lambda val: BitVecVal(val, 32)


def build_sha256_z3(msg_len, target_hex, timeout_sec=120):
    """
    Encode SHA-256 as Z3 constraints. Solve for unknown message bytes.
    
    Every intermediate value gets its own Z3 variable to prevent
    expression tree explosion. This is critical for performance.
    """
    # Parse target
    target_bytes = bytes.fromhex(target_hex)
    target_words = [struct.unpack('>I', target_bytes[i:i+4])[0] 
                    for i in range(0, 32, 4)]
    
    s = Solver()
    s.set("timeout", timeout_sec * 1000)
    
    # ── MESSAGE BYTES (the unknowns) ──
    msg_vars = [BitVec(f'm{i}', 8) for i in range(msg_len)]
    
    # ── BUILD PADDED BYTE ARRAY ──
    # message bytes + 0x80 + zeros + 8-byte length
    padded_bytes = []
    for i in range(msg_len):
        padded_bytes.append(msg_vars[i])
    padded_bytes.append(BitVecVal(0x80, 8))
    while len(padded_bytes) < 56:
        padded_bytes.append(BitVecVal(0, 8))
    # 8-byte big-endian length
    length_bits = msg_len * 8
    for shift in [56, 48, 40, 32, 24, 16, 8, 0]:
        padded_bytes.append(BitVecVal((length_bits >> shift) & 0xFF, 8))
    
    # ── PACK INTO W[0..15] ──
    W = []
    for i in range(16):
        w_var = BV(f'W{i}')
        s.add(w_var == Concat(padded_bytes[i*4], padded_bytes[i*4+1],
                              padded_bytes[i*4+2], padded_bytes[i*4+3]))
        W.append(w_var)
    
    # ── MESSAGE SCHEDULE W[16..63] ──
    # Each gets its own named variable (prevents expression blowup)
    for i in range(16, 64):
        w_var = BV(f'W{i}')
        s.add(w_var == z3_gamma1(W[i-2]) + W[i-7] + z3_gamma0(W[i-15]) + W[i-16])
        W.append(w_var)
    
    # ── 64-ROUND COMPRESSION ──
    # Each round's a and e get named variables
    # b=prev_a, c=prev_b, etc. — these are just pointer shifts
    a, b, c, d = BVC(H0[0]), BVC(H0[1]), BVC(H0[2]), BVC(H0[3])
    e, f, g, h = BVC(H0[4]), BVC(H0[5]), BVC(H0[6]), BVC(H0[7])
    
    for i in range(64):
        # Named intermediates for T1 components
        t1_var = BV(f'T1_{i}')
        s.add(t1_var == h + z3_Sigma1(e) + z3_Ch(e,f,g) + BVC(K[i]) + W[i])
        
        t2_var = BV(f'T2_{i}')
        s.add(t2_var == z3_Sigma0(a) + z3_Maj(a,b,c))
        
        # New state variables
        new_a = BV(f'a_{i}')
        new_e = BV(f'e_{i}')
        s.add(new_a == t1_var + t2_var)
        s.add(new_e == d + t1_var)
        
        # Shift: h=g, g=f, f=e, e=new_e, d=c, c=b, b=a, a=new_a
        h, g, f = g, f, e
        e = new_e
        d, c, b = c, b, a
        a = new_a
    
    # ── LOCK OUTPUT: hash must equal target ──
    final_state = [a, b, c, d, e, f, g, h]
    for j in range(8):
        target_val = (target_words[j] - H0[j]) & M32
        s.add(final_state[j] == BVC(target_val))
    
    # ── SOLVE ──
    print(f"  Z3 variables: {len(s.assertions())} constraints")
    sys.stdout.flush()
    
    t0 = time.time()
    result = s.check()
    elapsed = time.time() - t0
    
    if result == sat:
        model = s.model()
        recovered = bytes([model.eval(mv, model_completion=True).as_long() 
                          for mv in msg_vars])
        return recovered, elapsed
    elif result == unsat:
        return "UNSAT", elapsed
    else:
        return None, elapsed


def main():
    print("=" * 70)
    print("Z3 SHA-256 PREIMAGE — CONSTRAINT SATISFACTION")
    print("No for loop. No brute force. Pure algebraic propagation.")
    print("=" * 70)
    
    # ── 1-BYTE: 8 unknown bits ──
    print(f"\n--- 1-BYTE (8 unknown bits) ---")
    for msg in [b"A", b"N", b"Z"]:
        h = hashlib.sha256(msg).hexdigest()
        print(f"  Target: SHA256('{msg.decode()}') = {h[:16]}...")
        sys.stdout.flush()
        
        result, elapsed = build_sha256_z3(1, h, timeout_sec=120)
        
        if isinstance(result, bytes):
            ok = result == msg
            c = result.decode() if all(32 <= x < 127 for x in result) else result.hex()
            print(f"  SOLVED: '{c}' {'✓' if ok else '✗'} ({elapsed:.2f}s)")
        elif result == "UNSAT":
            print(f"  UNSAT ({elapsed:.2f}s)")
        else:
            print(f"  TIMEOUT ({elapsed:.1f}s)")
        sys.stdout.flush()
    
    # ── 2-BYTE: 16 unknown bits ──
    print(f"\n--- 2-BYTE (16 unknown bits) ---")
    for msg in [b"Hi", b"OK"]:
        h = hashlib.sha256(msg).hexdigest()
        print(f"  Target: SHA256('{msg.decode()}') = {h[:16]}...")
        sys.stdout.flush()
        
        result, elapsed = build_sha256_z3(2, h, timeout_sec=300)
        
        if isinstance(result, bytes):
            ok = result == msg
            c = result.decode() if all(32 <= x < 127 for x in result) else result.hex()
            print(f"  SOLVED: '{c}' {'✓' if ok else '✗'} ({elapsed:.2f}s)")
        elif result == "UNSAT":
            print(f"  UNSAT ({elapsed:.2f}s)")
        else:
            print(f"  TIMEOUT ({elapsed:.1f}s)")
        sys.stdout.flush()

    # ── 3-BYTE: 24 unknown bits ──
    print(f"\n--- 3-BYTE (24 unknown bits, 16.7M brute-force equiv) ---")
    for msg in [b"DNA"]:
        h = hashlib.sha256(msg).hexdigest()
        print(f"  Target: SHA256('{msg.decode()}') = {h[:16]}...")
        sys.stdout.flush()
        
        result, elapsed = build_sha256_z3(3, h, timeout_sec=600)
        
        if isinstance(result, bytes):
            ok = result == msg
            c = result.decode() if all(32 <= x < 127 for x in result) else result.hex()
            print(f"  SOLVED: '{c}' {'✓' if ok else '✗'} ({elapsed:.2f}s)")
            # Compare to brute force time
            bf_time = 16777216 / 3500000  # from C benchmark
            print(f"  Brute force: ~{bf_time:.1f}s | Z3: {elapsed:.1f}s | "
                  f"ratio: {bf_time/elapsed:.1f}x" if elapsed > 0.01 else "")
        elif result == "UNSAT":
            print(f"  UNSAT ({elapsed:.2f}s)")
        else:
            print(f"  TIMEOUT ({elapsed:.1f}s)")
        sys.stdout.flush()

    # ── 4-BYTE: 32 unknown bits ──
    print(f"\n--- 4-BYTE (32 unknown bits, 4.3B brute-force equiv) ---")
    for msg in [b"DEAN"]:
        h = hashlib.sha256(msg).hexdigest()
        print(f"  Target: SHA256('{msg.decode()}') = {h[:16]}...")
        sys.stdout.flush()
        
        result, elapsed = build_sha256_z3(4, h, timeout_sec=600)
        
        if isinstance(result, bytes):
            ok = result == msg
            c = result.decode() if all(32 <= x < 127 for x in result) else result.hex()
            print(f"  SOLVED: '{c}' {'✓' if ok else '✗'} ({elapsed:.2f}s)")
            print(f"  Brute force: ~1200s | Z3: {elapsed:.1f}s | "
                  f"ratio: {1200/elapsed:.0f}x" if elapsed > 0.01 else "")
        elif result == "UNSAT":
            print(f"  UNSAT ({elapsed:.2f}s)")
        else:
            print(f"  TIMEOUT ({elapsed:.1f}s) — Z3 hit the wall")
            print(f"  This is where carry_T1 hints would narrow the search")
        sys.stdout.flush()

    print(f"\n{'='*70}")
    print("STATUS")
    print(f"{'='*70}")
    print("""
  The Z3 encoding replaces the brute-force loop with
  algebraic constraint propagation through 64 rounds of
  SHA-256. No candidate testing. The solver follows the
  SHAPE of the constraint manifold.
  
  Each round creates named intermediate variables (T1_i, T2_i,
  a_i, e_i, W_i) to prevent expression tree blowup.
  
  The structural advantages for short messages:
    - W[1..14] = 0 → most schedule words are constant-derived
    - W[16] = W[0] → the echo constrains from both ends
    - 6/8 state_1 words are H0 constants → 192-bit checkpoint
    - T1_round0 = 0xf377ed68 + W[0] → linear leverage
  
  Z3 uses ALL of these simultaneously. That's the T-bone.
""")


if __name__ == "__main__":
    main()
