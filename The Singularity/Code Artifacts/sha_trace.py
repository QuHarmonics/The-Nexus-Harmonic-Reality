import hashlib

MASK = 0xFFFFFFFF
def rotr(x, n): return ((x >> n) | (x << (32 - n))) & MASK

K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2,
]
H0 = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

def pad(msg: bytes) -> bytes:
    ml = len(msg) * 8
    msg = msg + b'\x80'
    while len(msg) % 64 != 56:
        msg += b'\x00'
    return msg + ml.to_bytes(8, 'big')

def carry_ripple(x, y):
    """Longest run of consecutive carry propagation in a 32-bit x+y."""
    c = 0; run = 0; longest = 0
    for i in range(32):
        xi, yi = (x >> i) & 1, (y >> i) & 1
        c = (xi & yi) | (xi & c) | (yi & c)
        run = run + 1 if c else 0
        longest = max(longest, run)
    return longest

def sha256_trace(msg: bytes):
    msg = pad(msg)
    Hh = H0[:]
    topologies, ripples_a, ripples_e = [], [], []
    for off in range(0, len(msg), 64):
        block = msg[off:off+64]
        W = [int.from_bytes(block[i:i+4], 'big') for i in range(0, 64, 4)]
        for t in range(16, 64):
            s0 = rotr(W[t-15],7) ^ rotr(W[t-15],18) ^ (W[t-15] >> 3)
            s1 = rotr(W[t-2],17) ^ rotr(W[t-2],19) ^ (W[t-2] >> 10)
            W.append((W[t-16] + s0 + W[t-7] + s1) & MASK)
        a,b,c,d,e,f,g,h = Hh
        for t in range(64):
            S1 = rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)
            ch = (e & f) ^ ((~e & MASK) & g)
            T1 = (h + S1 + ch + K[t] + W[t]) & MASK
            S0 = rotr(a,2) ^ rotr(a,13) ^ rotr(a,22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            T2 = (S0 + maj) & MASK
            topologies.append("a'=T1+T2 | e'=d+T1 | (b..h) shift-down-1")
            ripples_a.append(carry_ripple(T1, T2))
            ripples_e.append(carry_ripple(d, T1))
            new_a, new_e = (T1 + T2) & MASK, (d + T1) & MASK
            h,g,f,e,d,c,b,a = g,f,e,new_e,c,b,a,new_a
        Hh = [(x + y) & MASK for x, y in zip(Hh, [a,b,c,d,e,f,g,h])]
    digest = b''.join(v.to_bytes(4,'big') for v in Hh)
    return digest, topologies, ripples_a, ripples_e

print("=== register-level topology vs bit-level carry depth ===\n")
for msg in [b"abc", b"abd", b"The quick brown fox"]:
    digest, topo, ra, re_ = sha256_trace(msg)
    ref = hashlib.sha256(msg).digest()
    print(f"msg={msg!r}  matches hashlib.sha256: {digest == ref}")
    print(f"  distinct topology strings across all {len(topo)} rounds: {len(set(topo))}")
    print(f"  carry-ripple(a) min/mean/max: {min(ra)}/{sum(ra)/len(ra):.2f}/{max(ra)}")
    print(f"  carry-ripple(e) min/mean/max: {min(re_)}/{sum(re_)/len(re_):.2f}/{max(re_)}")
    print(f"  first 12 ripple(a) values: {ra[:12]}")
    print()

rots = {"Sigma0":[2,13,22], "Sigma1":[6,11,25], "sigma0":[7,18], "sigma1":[17,19]}
print("rotation constants:", rots)
flat = [n for v in rots.values() for n in v]
print("any multiple of 4 (i.e. aligned to a 4-bit hex slot boundary)?", any(n % 4 == 0 for n in flat))
