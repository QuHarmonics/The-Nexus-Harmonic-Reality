```python
# Single-cell: custom SHA-256 with parameterized K array + experiments
# Paste into a Jupyter cell and run. Uses only Python stdlib.

import struct
import math
import itertools
import random
from typing import List, Tuple

# --- Utilities --------------------------------------------------------------
def _rotr(x: int, n: int) -> int:
    return ((x >> n) | ((x & ((1 << n) - 1)) << (32 - n))) & 0xFFFFFFFF

def _ch(x, y, z): return (x & y) ^ (~x & z)
def _maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def _bsig0(x): return (_rotr(x, 2) ^ _rotr(x, 13) ^ _rotr(x, 22)) & 0xFFFFFFFF
def _bsig1(x): return (_rotr(x, 6) ^ _rotr(x, 11) ^ _rotr(x, 25)) & 0xFFFFFFFF
def _ssig0(x): return (_rotr(x, 7) ^ _rotr(x, 18) ^ (x >> 3)) & 0xFFFFFFFF
def _ssig1(x): return (_rotr(x, 17) ^ _rotr(x, 19) ^ (x >> 10)) & 0xFFFFFFFF

def _pad_message(msg: bytes) -> bytes:
    L = len(msg) * 8
    msg = msg + b'\x80'
    # pad with zeros until length ≡ 448 mod 512
    while ((len(msg) * 8) % 512) != 448:
        msg += b'\x00'
    msg += struct.pack('>Q', L)
    return msg

def _hamming(a: bytes, b: bytes) -> int:
    # Hamming distance in bits
    assert len(a) == len(b)
    dist = 0
    for x, y in zip(a, b):
        dist += bin(x ^ y).count('1')
    return dist

# --- Default K constants (first 32-bit words of fractional cube roots of 2..67) ---
K_DEFAULT = [
0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

# --- SHA-256 core with parameterized K -------------------------------------
def sha256_custom(msg: bytes, K: List[int]) -> bytes:
    """Return 32-byte digest for message using provided K array (length 64)."""
    assert len(K) == 64
    # initial hash values (standard)
    H = [
        0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
        0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
    ]
    padded = _pad_message(msg)
    for i in range(0, len(padded), 64):
        block = padded[i:i+64]
        w = list(struct.unpack('>16I', block)) + [0]*48
        for t in range(16, 64):
            s0 = _ssig0(w[t-15])
            s1 = _ssig1(w[t-2])
            w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
        a,b,c,d,e,f,g,h = H
        for t in range(64):
            T1 = (h + _bsig1(e) + _ch(e,f,g) + K[t] + w[t]) & 0xFFFFFFFF
            T2 = (_bsig0(a) + _maj(a,b,c)) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + T1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xFFFFFFFF
        H = [(x+y) & 0xFFFFFFFF for x,y in zip(H, [a,b,c,d,e,f,g,h])]
    return b''.join(struct.pack('>I', h) for h in H)

# --- Experiment helpers -----------------------------------------------------
def rotate_K(K: List[int], shift: int) -> List[int]:
    n = len(K)
    s = shift % n
    return K[s:] + K[:s]

def permute_K_random(K: List[int], rng: random.Random) -> List[int]:
    Kp = K.copy()
    rng.shuffle(Kp)
    return Kp

def chain_hash_rotate(msg: bytes, rounds: int, leak_style='rotate') -> Tuple[List[bytes], List[int]]:
    """
    Start with msg, compute digest0 = sha(msg, K0).
    For i in 1..rounds-1:
      - if leak_style == 'rotate': Ki = rotate(K0, i)
      - if leak_style == 'permute': Ki = random permutation each round
      - digest_i = sha(digest_{i-1}, Ki)
    Returns list of digests and list of hamming distances between successive digests.
    """
    digests = []
    hamming = []
    rng = random.Random(0xC0FFEE)
    K0 = K_DEFAULT
    cur = sha256_custom(msg, K0)
    digests.append(cur)
    for i in range(1, rounds):
        if leak_style == 'rotate':
            Ki = rotate_K(K0, i)
        elif leak_style == 'permute':
            Ki = permute_K_random(K0, rng)
        else:
            raise ValueError("leak_style must be 'rotate' or 'permute'")
        nxt = sha256_custom(cur, Ki)
        digests.append(nxt)
        hamming.append(_hamming(cur, nxt))
        cur = nxt
    return digests, hamming

# --- Demo run and analysis --------------------------------------------------
if __name__ == "__main__":
    # Example message
    msg = b"Test message for Nexus spiral SHA experiment"
    rounds = 20

    print("Experiment A: rotate K each iteration (stack-pop chaining)")
    digA, hamA = chain_hash_rotate(msg, rounds, leak_style='rotate')
    for i, d in enumerate(digA):
        print(f"  round {i:02d} digest: {d.hex()}")
    print("Hamming distances between successive digests (bits):")
    print(hamA)
    print("Stats: mean {:.2f}, std {:.2f}".format(
        sum(hamA)/len(hamA), (sum((x - sum(hamA)/len(hamA))**2 for x in hamA)/len(hamA))**0.5 if len(hamA)>1 else 0.0
    ))

    print("\nExperiment B: random-permute K each iteration (stack-pop chaining)")
    digB, hamB = chain_hash_rotate(msg, rounds, leak_style='permute')
    for i, d in enumerate(digB):
        print(f"  round {i:02d} digest: {d.hex()}")
    print("Hamming distances between successive digests (bits):")
    print(hamB)
    print("Stats: mean {:.2f}, std {:.2f}".format(
        sum(hamB)/len(hamB), (sum((x - sum(hamB)/len(hamB))**2 for x in hamB)/len(hamB))**0.5 if len(hamB)>1 else 0.0
    ))

    # Quick visualization (requires matplotlib)
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8,3))
        plt.plot(range(1, len(hamA)+1), hamA, marker='o', label='rotate')
        plt.plot(range(1, len(hamB)+1), hamB, marker='x', label='permute')
        plt.xlabel('iteration')
        plt.ylabel('Hamming distance (bits)')
        plt.title('Hamming distance between successive chained digests')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception:
        pass

# End of cell

```

    Experiment A: rotate K each iteration (stack-pop chaining)
      round 00 digest: 83e3665b8d3b7994f6c171c0f41a47cdfd97966fe5a46b066174973eac4f528b
      round 01 digest: 45ebefd6288c38ce0b4131e39dce6bf15eb3249187a494d96097b431cd2a54b5
      round 02 digest: 936f4b5cf8f5a9c9d8ea086e30d8267e61e67cdf586975ef320e370e8e056a05
      round 03 digest: c6f0c4a9adc2ad606a135c09102ddac5c529b58e6d118d53ec08d8bfb9ff06c6
      round 04 digest: b8e779ae65505559d28bd003164271de0bd146486daa0afba72aceb57b55acca
      round 05 digest: 7bb47c163a4a8964da0ca3786dca46fea2bcdc8c8e4ddd2cf0d777ffebf56beb
      round 06 digest: ad5dd2e804b43d04ce0645d963294490b898c95b8ac64bbaa19bfa22968c20a8
      round 07 digest: f60adb5ab0ffcc39ea41be843045ad42e85c9eac90735b54fc362b3112aedc7b
      round 08 digest: ea2c6e1e2d34cb2c9af1d6b4a3acc588533bb2752cff7886401b092869e4bc05
      round 09 digest: 23e71efb380e52b588ab2053b1d3215e492179ef84d9c2aab135d5dad422f790
      round 10 digest: 10d903db0b11c7e6de292112bb0cea6edb7f30bbfa0bad5a833909a0e937fe46
      round 11 digest: e0a6bc307d59767080ccaafc2837454ee83e567f6059d58b47d807f8d25ffadb
      round 12 digest: 9d87539a37b508c906e8151103880a3140f18daf0ef25b5cdce9b5bc6936d20f
      round 13 digest: 0b06d7a639fcdde0e14672d6c3f91aca1ef4a06cc7e8f98025fc0cc9ba593a58
      round 14 digest: d8e90ac232cf4a8bb1d39d2c1e12bf3ee7f54542f78a51746e4705b0fff698fc
      round 15 digest: 13d663e5f8334e072e98e2e46c40cd0f5a0200d0a37bd8cd03f150aa0cb5ccc9
      round 16 digest: 81e17b30cb1f5fe02df7421f8f79f9f0e007db934af23f7e5060c293703233a7
      round 17 digest: b6444187e4cc52b0ab9d507abd0fd7f8e9cd324b185d54bc5a336acc00b61717
      round 18 digest: 398208bcbbe7a10ca683173b8a74cfdbc23197232c49ccce66ea67450be31ccd
      round 19 digest: 38fda81b4530a4a1b56f1aa731a64e20e3dc17249941f6b5d049982c9830db1e
    Hamming distances between successive digests (bits):
    [117, 131, 144, 120, 133, 127, 133, 121, 134, 120, 130, 147, 130, 139, 135, 138, 117, 126, 137]
    Stats: mean 130.47, std 8.52
    
    Experiment B: random-permute K each iteration (stack-pop chaining)
      round 00 digest: 83e3665b8d3b7994f6c171c0f41a47cdfd97966fe5a46b066174973eac4f528b
      round 01 digest: 3e5dcaa67739427dfdc3f1592592d5fb2fc1cd38e79b75db18a36eb8eaa83faf
      round 02 digest: 9afb3411e63c086517e52e0683893b9aa2bbc8a88c6bec47ab3bc95cb7564185
      round 03 digest: bb96247f5b6d1f6dcff68c8e50e01882a8f07819710ddb50909e0a64028a607c
      round 04 digest: 1067e6c659848a43fee17f2b7e1c7e1eeb60c9928903f4cad7664514a2476b62
      round 05 digest: 8c62c580898454b6197ff841d0f668b18bdde8615fa6bb05e6c816ee528e909a
      round 06 digest: 5e62afde3eca26e7909811a550976c28ba933369395c7af4c9585b9835cd64e4
      round 07 digest: 825937515b2cfd3bfe51a627f74f62905a70e4d702d862b8f8736d49ffa10e0e
      round 08 digest: 937b0b2ecae47f94bb24e997639c50fbfd51f742dc5bc337483be8589852d9b9
      round 09 digest: 10f4ae9ad61cca1dc23d5e861edae261d776b8a85f671ed563f591820adf60f4
      round 10 digest: 60abddb560ee1517ec4281d651e5da81fc01be8360b64fd3531ee02400c13dad
      round 11 digest: 32d9764898fda2c55ac4e5cc0592b4c15f531e3672bdffade881f3a9c6941a4f
      round 12 digest: fc903a6d29442cbfa4aa400318afc8e65d914ea5046db77176eb442ada5c7787
      round 13 digest: 3a3f32b3fc78c29a93200a38891a1aaa08e64b38bb7e2bd659e182aea18c4f52
      round 14 digest: cd2366b7c00f27e90bfc14bcb56076664166503591bd92b4c5ec74242a2c6c3e
      round 15 digest: b378475ec0061d917a50cb3130ac4f76ba65ffd28ca2c71df002dad60ac8ae73
      round 16 digest: 06d9d256efabccf8e5efb8735c2ce923e0ee997d1a81253460d2738bc3e2b0b8
      round 17 digest: 909a82b5aded6b63a1c59255e192d1b849e86ebcd6e1e166b40644cdb6212d55
      round 18 digest: 7bb6464d3657d671312a7a1d8b4096e2d75b3331b0d097ffdc87597bec4ba51a
      round 19 digest: a6b1d5d0e8694dc5506c468f6f65e33f4d381893012a75d0f304340019b08a61
    Hamming distances between successive digests (bits):
    [133, 136, 120, 128, 139, 124, 135, 125, 134, 137, 129, 129, 132, 120, 129, 126, 124, 130, 146]
    Stats: mean 130.32, std 6.46
    


    
![png](output_0_1.png)
    



```python
# SHA-256 K-as-opcode experiments
# Paste into a Jupyter cell. Requires numpy and matplotlib. scipy optional.
import struct, random, math, itertools
import numpy as np
import matplotlib.pyplot as plt

# Optional: for nicer colormaps
try:
    import seaborn as sns
    sns.set()
except Exception:
    pass

# --- SHA helpers (same as before) ---
def _rotr(x, n): return ((x >> n) | ((x & ((1 << n) - 1)) << (32 - n))) & 0xFFFFFFFF
def _ch(x,y,z): return (x & y) ^ (~x & z)
def _maj(x,y,z): return (x & y) ^ (x & z) ^ (y & z)
def _bsig0(x): return (_rotr(x,2) ^ _rotr(x,13) ^ _rotr(x,22)) & 0xFFFFFFFF
def _bsig1(x): return (_rotr(x,6) ^ _rotr(x,11) ^ _rotr(x,25)) & 0xFFFFFFFF
def _ssig0(x): return (_rotr(x,7) ^ _rotr(x,18) ^ (x >> 3)) & 0xFFFFFFFF
def _ssig1(x): return (_rotr(x,17) ^ _rotr(x,19) ^ (x >> 10)) & 0xFFFFFFFF

def _pad_message(msg: bytes) -> bytes:
    L = len(msg) * 8
    msg = msg + b'\x80'
    while ((len(msg) * 8) % 512) != 448:
        msg += b'\x00'
    msg += struct.pack('>Q', L)
    return msg

def _hamming_bytes(a: bytes, b: bytes) -> int:
    assert len(a) == len(b)
    return sum(bin(x ^ y).count('1') for x,y in zip(a,b))

def bytes_to_bitvec(b: bytes) -> np.ndarray:
    # returns length 256 array of 0/1 (MSB-first per byte)
    bits = np.unpackbits(np.frombuffer(b, dtype=np.uint8))
    return bits.astype(np.uint8)

# --- K default ---
K_DEFAULT = [
0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

# --- SHA core with parameterized K ---
def sha256_custom(msg: bytes, K: list) -> bytes:
    assert len(K) == 64
    H = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]
    padded = _pad_message(msg)
    for i in range(0, len(padded), 64):
        block = padded[i:i+64]
        w = list(struct.unpack('>16I', block)) + [0]*48
        for t in range(16,64):
            s0 = _ssig0(w[t-15]); s1 = _ssig1(w[t-2])
            w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
        a,b,c,d,e,f,g,h = H
        for t in range(64):
            T1 = (h + _bsig1(e) + _ch(e,f,g) + K[t] + w[t]) & 0xFFFFFFFF
            T2 = (_bsig0(a) + _maj(a,b,c)) & 0xFFFFFFFF
            h,g,f,e,d,c,b,a = g,f,e,(d+T1)&0xFFFFFFFF,c,b,a,(T1+T2)&0xFFFFFFFF
        H = [(x+y)&0xFFFFFFFF for x,y in zip(H, [a,b,c,d,e,f,g,h])]
    return b''.join(struct.pack('>I', h) for h in H)

# --- K manipulations ---
def rotate_K(K, shift): 
    s = shift % len(K)
    return K[s:] + K[:s]

def swap_adjacent(K, i):
    Kp = K.copy()
    Kp[i], Kp[i+1] = Kp[i+1], Kp[i]
    return Kp

def swap_block(K, i, j, block=4):
    Kp = K.copy()
    Kp[i:i+block], Kp[j:j+block] = Kp[j:j+block], Kp[i:i+block]
    return Kp

# --- Experiment parameters ---
BASE_MSG = b'\xAA' * 64   # inert baseline (0xAA pattern, visually like #aaaaaa)
N_TRIALS = 200            # trials per shift (increase for stability)
SHIFTS = list(range(64))  # rotation offsets
CHAIN_LEN = 50            # chain depth for autocorr / drift
SEED = 0
random.seed(SEED)
np.random.seed(SEED)

# --- Precompute a set of baseline digests (seeds) to use across shifts for stability ---
# We'll use the same initial digest for all shifts to isolate K effects.
base_digest = sha256_custom(BASE_MSG, K_DEFAULT)

# --- Rotation sweep: for each shift compute mean & std Hamming between digest and digest(K_rot) ---
means = []
stds = []
perbit_counts = np.zeros((len(SHIFTS), 256), dtype=int)  # counts of flips per bit per shift
for idx, s in enumerate(SHIFTS):
    Ks = rotate_K(K_DEFAULT, s)
    hs = []
    for t in range(N_TRIALS):
        # keep input same: chain from base_digest
        d0 = base_digest
        d1 = sha256_custom(d0, Ks)
        hs.append(_hamming_bytes(d0, d1))
        # accumulate per-bit flips
        xor = bytes(x ^ y for x,y in zip(d0, d1))
        bits = np.unpackbits(np.frombuffer(xor, dtype=np.uint8))
        perbit_counts[idx] += bits
    means.append(np.mean(hs))
    stds.append(np.std(hs))

means = np.array(means)
stds = np.array(stds)
perbit_probs = perbit_counts / N_TRIALS  # probability each bit flips for each shift

# --- Plot mean Hamming vs shift ---
plt.figure(figsize=(10,4))
plt.plot(SHIFTS, means, marker='o')
plt.fill_between(SHIFTS, means-stds, means+stds, alpha=0.2)
plt.xlabel('Rotation shift (K rotated by s)')
plt.ylabel('Mean Hamming distance (bits)')
plt.title('Mean Hamming vs K rotation shift (baseline inert message)')
plt.grid(True)
plt.show()

# --- Heatmap: per-bit flip probability (shifts on y, bit index on x) ---
plt.figure(figsize=(12,6))
plt.imshow(perbit_probs, aspect='auto', cmap='viridis', interpolation='nearest')
plt.colorbar(label='flip probability')
plt.xlabel('output bit index (0..255)')
plt.ylabel('rotation shift s')
plt.title('Per-bit flip probability for each rotation shift')
plt.show()

# --- Small-swap search: adjacent swaps and block swaps ---
# Use a smaller trial set for speed
SWAP_TRIALS = 100
adj_results = []
for i in range(63):
    Kp = swap_adjacent(K_DEFAULT, i)
    hs = []
    for _ in range(SWAP_TRIALS):
        d0 = base_digest
        d1 = sha256_custom(d0, Kp)
        hs.append(_hamming_bytes(d0, d1))
    adj_results.append((i, np.mean(hs), np.std(hs)))
adj_results_sorted = sorted(adj_results, key=lambda x: x[1])
print("Top 8 adjacent swaps that minimize mean Hamming (index, mean, std):")
for r in adj_results_sorted[:8]:
    print(r)
print("Top 8 adjacent swaps that maximize mean Hamming:")
for r in adj_results_sorted[-8:]:
    print(r)

# Block swap search (block size 4)
block_results = []
for i in range(0, 64-4, 4):
    for j in range(i+4, 64-4, 4):
        Kp = swap_block(K_DEFAULT, i, j, block=4)
        hs = []
        for _ in range(40):
            d0 = base_digest
            d1 = sha256_custom(d0, Kp)
            hs.append(_hamming_bytes(d0, d1))
        block_results.append(((i,j), np.mean(hs)))
block_results_sorted = sorted(block_results, key=lambda x: x[1])
print("Block-swap (4) top 6 min mean Hamming (i,j,mean):")
for r in block_results_sorted[:6]:
    print(r)
print("Block-swap (4) top 6 max mean Hamming:")
for r in block_results_sorted[-6:]:
    print(r)

# --- Chain depth & autocorrelation: rotate by a chosen shift and chain many times ---
chosen_shift = int(np.argmin(means))  # pick shift with smallest mean as interesting candidate
Ks_chosen = rotate_K(K_DEFAULT, chosen_shift)
chain = [base_digest]
for i in range(CHAIN_LEN-1):
    chain.append(sha256_custom(chain[-1], Ks_chosen))
# compute successive Hamming distances
chain_hams = [_hamming_bytes(chain[i], chain[i+1]) for i in range(len(chain)-1)]
print(f"Chosen shift {chosen_shift} (min mean). Chain mean Hamming:", np.mean(chain_hams))

# autocorrelation of chain_hams
def autocorr(x, lag):
    x = np.array(x)
    x = x - x.mean()
    denom = np.sum(x*x)
    if denom == 0: return 0.0
    return np.sum(x[:-lag]*x[lag:]) / denom

lags = list(range(1, min(20, len(chain_hams))))
ac = [autocorr(chain_hams, l) for l in lags]
plt.figure(figsize=(8,3))
plt.stem(lags, ac, use_line_collection=True)
plt.xlabel('lag')
plt.ylabel('autocorrelation')
plt.title('Autocorrelation of chain Hamming distances (chosen shift)')
plt.grid(True)
plt.show()

# --- PCA on digest bit vectors across shifts (to see low-dim structure) ---
# For each shift, compute one digest (or average bit vector across trials)
bit_matrix = np.zeros((len(SHIFTS), 256), dtype=float)
for idx in range(len(SHIFTS)):
    # average bit vector across trials
    bit_matrix[idx] = perbit_probs[idx]

# center
X = bit_matrix - bit_matrix.mean(axis=0)
# SVD for PCA
U, Svals, Vt = np.linalg.svd(X, full_matrices=False)
pc = U @ np.diag(Svals)
explained = (Svals**2) / np.sum(Svals**2)
print("Explained variance by first 6 PCs:", explained[:6])
plt.figure(figsize=(8,3))
plt.plot(np.cumsum(explained[:10]), marker='o')
plt.xlabel('num PCs')
plt.ylabel('cumulative explained variance')
plt.title('PCA on per-bit flip probabilities across shifts')
plt.grid(True)
plt.show()

# scatter first two PCs
plt.figure(figsize=(6,5))
plt.scatter(pc[:,0], pc[:,1], c=SHIFTS, cmap='tab20')
for i,s in enumerate(SHIFTS):
    if i % 8 == 0:
        plt.text(pc[i,0], pc[i,1], str(s), fontsize=8)
plt.colorbar(label='shift s')
plt.xlabel('PC1'); plt.ylabel('PC2'); plt.title('Shifts in PC space (per-bit flip patterns)')
plt.grid(True)
plt.show()

# --- Summary prints ---
print("\nSummary:")
print("Shift with minimum mean Hamming:", int(np.argmin(means)), "mean", float(means.min()))
print("Shift with maximum mean Hamming:", int(np.argmax(means)), "mean", float(means.max()))
print("Overall mean Hamming across shifts:", float(means.mean()), "std of means:", float(means.std()))

# Save arrays to variables for further inspection
RESULTS = {
    'shifts': SHIFTS,
    'means': means,
    'stds': stds,
    'perbit_probs': perbit_probs,
    'adj_results_sorted': adj_results_sorted,
    'block_results_sorted': block_results_sorted,
    'chain_hams': chain_hams,
    'pc': pc,
    'explained': explained
}

print("\nDone. RESULTS dict contains arrays for further analysis.")

```


    
![png](output_1_0.png)
    



    
![png](output_1_1.png)
    


    Top 8 adjacent swaps that minimize mean Hamming (index, mean, std):
    (60, np.float64(110.0), np.float64(0.0))
    (14, np.float64(111.0), np.float64(0.0))
    (35, np.float64(112.0), np.float64(0.0))
    (39, np.float64(114.0), np.float64(0.0))
    (19, np.float64(115.0), np.float64(0.0))
    (34, np.float64(115.0), np.float64(0.0))
    (58, np.float64(116.0), np.float64(0.0))
    (1, np.float64(117.0), np.float64(0.0))
    Top 8 adjacent swaps that maximize mean Hamming:
    (50, np.float64(137.0), np.float64(0.0))
    (57, np.float64(137.0), np.float64(0.0))
    (51, np.float64(139.0), np.float64(0.0))
    (56, np.float64(139.0), np.float64(0.0))
    (15, np.float64(140.0), np.float64(0.0))
    (30, np.float64(141.0), np.float64(0.0))
    (59, np.float64(141.0), np.float64(0.0))
    (26, np.float64(144.0), np.float64(0.0))
    Block-swap (4) top 6 min mean Hamming (i,j,mean):
    ((24, 36), np.float64(107.0))
    ((8, 52), np.float64(113.0))
    ((16, 20), np.float64(113.0))
    ((0, 44), np.float64(114.0))
    ((28, 56), np.float64(114.0))
    ((0, 12), np.float64(115.0))
    Block-swap (4) top 6 max mean Hamming:
    ((28, 40), np.float64(141.0))
    ((12, 16), np.float64(143.0))
    ((24, 28), np.float64(144.0))
    ((4, 40), np.float64(145.0))
    ((24, 56), np.float64(145.0))
    ((16, 24), np.float64(147.0))
    Chosen shift 5 (min mean). Chain mean Hamming: 127.46938775510205
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[4], line 201
        199 ac = [autocorr(chain_hams, l) for l in lags]
        200 plt.figure(figsize=(8,3))
    --> 201 plt.stem(lags, ac, use_line_collection=True)
        202 plt.xlabel('lag')
        203 plt.ylabel('autocorrelation')
    

    TypeError: stem() got an unexpected keyword argument 'use_line_collection'



    <Figure size 800x300 with 0 Axes>



```python
#!/usr/bin/env python3
# optcode_trace.py
# Self-contained SHA-256 with configurable round constants K for experimentation.

import struct
import math
import hashlib
import random
from typing import List, Tuple
import statistics
import sys

# --- Utilities --------------------------------------------------------------

def rotr(x: int, n: int) -> int:
    return ((x >> n) | ((x & 0xffffffff) << (32 - n))) & 0xffffffff

def ch(x, y, z): return (x & y) ^ (~x & z)
def maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def big_sigma0(x): return (rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)) & 0xffffffff
def big_sigma1(x): return (rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)) & 0xffffffff
def small_sigma0(x): return (rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)) & 0xffffffff
def small_sigma1(x): return (rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)) & 0xffffffff

# --- Default SHA-256 K constants (first 32-bit words of cube roots of primes) ---
DEFAULT_K = [
  0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
  0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
  0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
  0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
  0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
  0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
  0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
  0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

# --- Pure-Python SHA-256 compression with configurable K -------------------

def sha256_custom(message: bytes, K_override: List[int] = None) -> bytes:
    """
    Compute SHA-256 digest of message using optionally overridden K constants.
    This is a straightforward implementation (not optimized) for experimentation.
    """
    K = K_override if K_override is not None else DEFAULT_K

    # Initial hash values (first 32 bits of fractional parts of sqrt of primes)
    H = [
        0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
        0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
    ]

    # Pre-processing (padding)
    ml = len(message) * 8
    msg = bytearray(message)
    msg.append(0x80)
    while ((len(msg) * 8) + 64) % 512 != 0:
        msg.append(0)
    msg += struct.pack('>Q', ml)

    # Process the message in successive 512-bit chunks
    for chunk_start in range(0, len(msg), 64):
        chunk = msg[chunk_start:chunk_start+64]
        w = list(struct.unpack('>16I', bytes(chunk))) + [0]*48
        for t in range(16, 64):
            s0 = small_sigma0(w[t-15])
            s1 = small_sigma1(w[t-2])
            w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xffffffff

        a,b,c,d,e,f,g,h = H
        for t in range(64):
            T1 = (h + big_sigma1(e) + ch(e,f,g) + K[t] + w[t]) & 0xffffffff
            T2 = (big_sigma0(a) + maj(a,b,c)) & 0xffffffff
            h = g
            g = f
            f = e
            e = (d + T1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xffffffff

        H = [(H[i] + v) & 0xffffffff for i,v in enumerate([a,b,c,d,e,f,g,h])]

    return b''.join(struct.pack('>I', h) for h in H)

# --- Bit / Hamming helpers --------------------------------------------------

def bytes_to_bits(b: bytes) -> List[int]:
    bits = []
    for byte in b:
        for i in range(8):
            bits.append((byte >> (7-i)) & 1)
    return bits

def hamming_distance_bytes(a: bytes, b: bytes) -> int:
    return sum(x != y for x,y in zip(bytes_to_bits(a), bytes_to_bits(b)))

# --- Experiment primitives -------------------------------------------------

def chain_with_transform(base_msg: bytes, transform_fn, rounds: int, K0: List[int]):
    """
    Run a chain: at each round, transform K via transform_fn(round_index, K_prev),
    compute digest = sha256_custom(prev_digest_or_base, K_transformed).
    Returns list of hex digests and list of bytes digests.
    """
    digests = []
    digest_bytes = sha256_custom(base_msg, K_override=K0)
    digests.append(digest_bytes)
    K_current = K0.copy()
    for r in range(1, rounds):
        K_current = transform_fn(r, K_current)
        digest_bytes = sha256_custom(digest_bytes, K_override=K_current)
        digests.append(digest_bytes)
    return digests

# --- Example transforms ----------------------------------------------------

def rotate_transform(step: int, K_prev: List[int], shift_by=1) -> List[int]:
    s = (step * shift_by) % len(K_prev)
    return K_prev[s:] + K_prev[:s]

def random_permute_transform(step: int, K_prev: List[int], rng=None) -> List[int]:
    rng = rng or random
    K_new = K_prev.copy()
    rng.shuffle(K_new)
    return K_new

def adjacent_swap_transform_factory(index_to_swap: int):
    def fn(step, K_prev):
        K_new = K_prev.copy()
        i = index_to_swap % (len(K_new)-1)
        K_new[i], K_new[i+1] = K_new[i+1], K_new[i]
        return K_new
    return fn

def block_swap_transform_factory(i,j,block_size=4):
    def fn(step, K_prev):
        K_new = K_prev.copy()
        n = len(K_new)
        i0 = i % n
        j0 = j % n
        # swap blocks of length block_size (wrap-around)
        for k in range(block_size):
            K_new[(i0+k)%n], K_new[(j0+k)%n] = K_new[(j0+k)%n], K_new[(i0+k)%n]
        return K_new
    return fn

# --- Diagnostics -----------------------------------------------------------

def compute_chain_hamming_stats(digests: List[bytes]) -> Tuple[List[int], float, float]:
    hams = []
    for a,b in zip(digests, digests[1:]):
        hams.append(hamming_distance_bytes(a,b))
    mean = statistics.mean(hams) if hams else 0.0
    stdev = statistics.pstdev(hams) if hams else 0.0
    return hams, mean, stdev

def per_bit_flip_prob(digests: List[bytes]) -> List[float]:
    nbits = len(digests[0]) * 8
    counts = [0]*nbits
    for a,b in zip(digests, digests[1:]):
        bits_a = bytes_to_bits(a)
        bits_b = bytes_to_bits(b)
        for i,(ba,bb) in enumerate(zip(bits_a,bits_b)):
            if ba != bb:
                counts[i] += 1
    total_pairs = max(1, len(digests)-1)
    return [c/total_pairs for c in counts]

# --- Example experiments ---------------------------------------------------

def experiment_rotate(base_msg: bytes, rounds=20, shift_by=1):
    print("Experiment: rotate K each iteration (shift_by=%d)" % shift_by)
    digests = chain_with_transform(base_msg, lambda r,K: rotate_transform(r,K,shift_by), rounds, DEFAULT_K.copy())
    for i,d in enumerate(digests):
        print(f"  round {i:02d} digest: {d.hex()}")
    hams, mean, stdev = compute_chain_hamming_stats(digests)
    print("Hamming distances between successive digests (bits):")
    print(hams)
    print("Stats: mean %.2f, std %.2f" % (mean, stdev))
    return digests, hams

def experiment_permute(base_msg: bytes, rounds=20, seed=0):
    print("Experiment: random-permute K each iteration (seed=%d)" % seed)
    rng = random.Random(seed)
    digests = chain_with_transform(base_msg, lambda r,K: random_permute_transform(r,K,rng), rounds, DEFAULT_K.copy())
    for i,d in enumerate(digests):
        print(f"  round {i:02d} digest: {d.hex()}")
    hams, mean, stdev = compute_chain_hamming_stats(digests)
    print("Hamming distances between successive digests (bits):")
    print(hams)
    print("Stats: mean %.2f, std %.2f" % (mean, stdev))
    return digests, hams

# --- CLI demo --------------------------------------------------------------

if __name__ == "__main__":
    BASE_MSG = b'\xAA' * 16  # inert baseline message (0xAA pattern)
    rounds = 20

    # Run rotate experiment
    digests_rot, hams_rot = experiment_rotate(BASE_MSG, rounds=rounds, shift_by=1)
    print("\n" + "-"*60 + "\n")
    # Run permute experiment
    digests_perm, hams_perm = experiment_permute(BASE_MSG, rounds=rounds, seed=42)

    # Compute per-bit flip probability heatmap data (example)
    probs = per_bit_flip_prob(digests_rot)
    print("\nPer-bit flip probabilities (first 64 bits shown):")
    print([round(p,3) for p in probs[:64]])

    # Example: compute adjacent-swap candidates and their chain means
    print("\nTesting adjacent swaps (indices 0..63) for mean Hamming (single-swap experiments):")
    results = []
    for idx in range(64):
        fn = adjacent_swap_transform_factory(idx)
        dig, _ = chain_with_transform(BASE_MSG, fn, rounds=rounds, K0=DEFAULT_K.copy())
        _, mean, _ = compute_chain_hamming_stats(dig)
        results.append((idx, mean))
    results_sorted = sorted(results, key=lambda x: x[1])
    print("Top 8 adjacent swaps that minimize mean Hamming (index, mean):")
    for t in results_sorted[:8]:
        print(t)
    print("Top 8 adjacent swaps that maximize mean Hamming (index, mean):")
    for t in results_sorted[-8:]:
        print(t)

```

    Experiment: rotate K each iteration (shift_by=1)
      round 00 digest: bc1443a0d17aab2db1ea0302ef280717ac9a2f23355c5b649ea87d605430458d
      round 01 digest: d41fb84e7c7b57882ca2784f3af3e813fd3e34fd1e156e2770103424f5de0ad7
      round 02 digest: c11c4d4fc6ccc5225f2cb3857dd115133065c636168bd836ef819ac6597a2456
      round 03 digest: d8213310addef3ae7be0304bc629e47a4bcd22412f8560646644c8f9d5ea4f65
      round 04 digest: 01f0d7a1da5b56f488cfe811f3513478e4be3bfac28951ee97f89c63bff99c51
      round 05 digest: cd483c628cb07dec1ebd09a4b49f6831f240ca8d13e400681f7dbe58cd69c377
      round 06 digest: 617614a545882a56a0391fbe2419796d95ffbf5e0592c4f27dca3ce60e558af2
      round 07 digest: 0ba3c4b439edf2a7d6da999e804ff49c5062a475e6cc88458b767c7dd1e00bbc
      round 08 digest: 0565bc1be683c1c8099656fedcbcae874585bf727747524dfb9936e117f646fa
      round 09 digest: 8990a7b40e471eac492a5633b67a813c8fa1941fde1516083e2cd042f91ee421
      round 10 digest: bf4723fb466a8a7a19bd4953b4460c9cad5e1ce80f0a9048cf998d2ced141d19
      round 11 digest: 58beeee26a4a82151b0c318d9c1a80967ab3bd78e92d2a5c5f7f8e412228d10b
      round 12 digest: e222a0581d807a4c0455873a42b96a6d7991aa63d0c3573fc1931e153d7df62d
      round 13 digest: 0764d2934a60cadd890f15ae2fa87ac6ae7515466ef3161fb9285442d3620b5d
      round 14 digest: 9bad4838d6ec754e12239aca82761982cf8f530a87d9bfb08985a1af6a7197df
      round 15 digest: e1dcc723f171657f204f800c906d90d9188ad69ca98bfe30807411b7e2324c2c
      round 16 digest: 3238c7011c496b4320cc53b5b1b1d2b86f05383e269bd0ca7bd36890c43e3a37
      round 17 digest: f0bf65d73b3fa018e14ea7173728872908750bd3cd774d113ebd3239e79f1602
      round 18 digest: 3b38c22f6e1c371f30af7167778c574042e4752bbeb47538a35bc9fde4d259ff
      round 19 digest: 77cba3b8acb3a54054ddb8123ba550f7e01229ce48dc603c5cca1c4d2a63d3e3
    Hamming distances between successive digests (bits):
    [134, 125, 131, 131, 130, 126, 133, 135, 130, 121, 120, 142, 128, 134, 113, 123, 130, 131, 131]
    Stats: mean 128.84, std 6.29
    
    ------------------------------------------------------------
    
    Experiment: random-permute K each iteration (seed=42)
      round 00 digest: bc1443a0d17aab2db1ea0302ef280717ac9a2f23355c5b649ea87d605430458d
      round 01 digest: cf17b89564883e2751b050aaf03b46211474b8b68a7af683f964c42df943e519
      round 02 digest: 5775ce4e55d767864026ab5b53f2a63163db92a7a7745bc61a4b962db5b4fec4
      round 03 digest: e84e61bb1b04d27e0f011ecfea5fe5db2a1775cef839e584f60884c728a173cf
      round 04 digest: a9aa4a7ffdcfe5fb301e3d53c7cb8f28073e557f5a4b5bea17718c1b168caf3a
      round 05 digest: 34a5112f6163a883ad6cc4fbbdce878f8a05eaf6bd9266354c3b1cf8894dfe81
      round 06 digest: 266c9c7821d8a352180b55620ddafacf250c08fd21e72055f52e5fd60c8abf07
      round 07 digest: fd52b641a388a554beb4c4d1910b9c33859e7b31d5f13d7499ef942ba047e968
      round 08 digest: 214d680c997639804b05096c0feaa2d096434d52c4c636d5ca1a8bd397acf5d2
      round 09 digest: bdc8f3221ae32dd3e88d36657cf80b426224a330bbecbb4ccdc09ad0235d5ae2
      round 10 digest: 3e2a15e55a98bc0f215b46e52a12cd549bae5b96214b371f21feb787d931d8b7
      round 11 digest: c2a907c5a5a6ef3d1d10dcbcc9fe213e9d1f7a306c9e4b758903efd5293a86de
      round 12 digest: 88c99e374dcedcf19fe2219ee75787d57de037b1a04cc3db01e1f772f2977eef
      round 13 digest: 494d8dc24a24a686c8cad7018c310f7202d8cc4e13a894b0aec4f831d37d229b
      round 14 digest: 6690ee347277ade815f90180790609d32ea8ef4877a61797af6f9437867dab7a
      round 15 digest: fac498a1cee2040421fc7db102c13fe35b3214f8b7938bec1c0e9a7be2eda2c2
      round 16 digest: 982fa7a343c84cf3c81a333ab45f65ed465d1617d033d7d8bdc4d04270d785d8
      round 17 digest: 04886060329153c5235d156d3c0c09ab8d55269ec0196a680aa696e95faffe96
      round 18 digest: 8f8d1547b80702045dbc63fcbf1c1b96d16c08785b51b886a38c2d9848465196
      round 19 digest: db1f6a7508d41a93789891fc30607b47af84aa5275c304c79de23eeb96cf356b
    Hamming distances between successive digests (bits):
    [135, 128, 143, 131, 138, 115, 129, 148, 123, 130, 129, 127, 143, 116, 124, 127, 126, 123, 124]
    Stats: mean 129.42, std 8.51
    
    Per-bit flip probabilities (first 64 bits shown):
    [0.579, 0.579, 0.421, 0.421, 0.684, 0.526, 0.474, 0.368, 0.684, 0.579, 0.421, 0.579, 0.368, 0.579, 0.474, 0.684, 0.579, 0.579, 0.579, 0.421, 0.526, 0.421, 0.526, 0.421, 0.632, 0.421, 0.421, 0.474, 0.579, 0.421, 0.737, 0.737, 0.421, 0.684, 0.579, 0.474, 0.579, 0.684, 0.526, 0.579, 0.474, 0.368, 0.632, 0.316, 0.474, 0.526, 0.421, 0.474, 0.632, 0.316, 0.421, 0.737, 0.474, 0.474, 0.579, 0.421, 0.421, 0.474, 0.474, 0.632, 0.579, 0.474, 0.526, 0.579]
    
    Testing adjacent swaps (indices 0..63) for mean Hamming (single-swap experiments):
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[5], line 217
        215 for idx in range(64):
        216     fn = adjacent_swap_transform_factory(idx)
    --> 217     dig, _ = chain_with_transform(BASE_MSG, fn, rounds=rounds, K0=DEFAULT_K.copy())
        218     _, mean, _ = compute_chain_hamming_stats(dig)
        219     results.append((idx, mean))
    

    ValueError: too many values to unpack (expected 2)



```python
# Notebook cell: decompile_constants.ipynb
# Requirements: pip install capstone unicorn (unicorn optional)
import struct
import binascii
from textwrap import indent

# Optional libs
try:
    from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CS_MODE_32, CS_ARCH_ARM, CS_MODE_ARM, CS_ARCH_ARM64, CS_ARCH_MIPS, CS_MODE_MIPS32, CS_ARCH_RISCV, CS_MODE_RISCV32
    CAPSTONE_AVAILABLE = True
except Exception as e:
    CAPSTONE_AVAILABLE = False
    print("Capstone not available:", e)

try:
    from unicorn import Uc, UC_ARCH_X86, UC_MODE_64, UC_ARCH_ARM, UC_MODE_ARM, UC_ARCH_ARM64, UC_ARCH_MIPS, UC_MODE_MIPS32, UC_ARCH_RISCV, UC_MODE_RISCV32
    UNICORN_AVAILABLE = True
except Exception as e:
    UNICORN_AVAILABLE = False
    print("Unicorn not available:", e)

# Full SHA-256 K constants (32-bit words)
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

# Utility: convert words to bytes with chosen endianness
def words_to_bytes(words, endian='big'):
    b = bytearray()
    for w in words:
        if endian == 'big':
            b.extend(struct.pack('>I', w))
        else:
            b.extend(struct.pack('<I', w))
    return bytes(b)

# Hexdump helper
def hexdump(b, width=16):
    lines = []
    for i in range(0, len(b), width):
        chunk = b[i:i+width]
        hexpart = ' '.join(f'{x:02x}' for x in chunk)
        asciipart = ''.join(chr(x) if 32 <= x < 127 else '.' for x in chunk)
        lines.append(f'{i:04x}  {hexpart:<{width*3}}  {asciipart}')
    return '\n'.join(lines)

# Disassembly harness using Capstone
def disassemble_bytes(code_bytes, arch='x86_64', mode_hint=None):
    if not CAPSTONE_AVAILABLE:
        return "Capstone not installed"
    # Map arch names to capstone params
    if arch == 'x86_64':
        md = Cs(CS_ARCH_X86, CS_MODE_64)
    elif arch == 'x86_32':
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif arch == 'arm':
        md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
    elif arch == 'arm64':
        md = Cs(CS_ARCH_ARM64, 0)
    elif arch == 'mips':
        md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32)
    elif arch == 'riscv':
        md = Cs(CS_ARCH_RISCV, CS_MODE_RISCV32)
    else:
        return f"Unsupported arch {arch}"
    md.detail = True
    out = []
    addr = 0x1000
    for i in md.disasm(code_bytes, addr):
        out.append(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")
    return '\n'.join(out) if out else "(no instructions decoded)"

# Optional: attempt lightweight emulation with Unicorn (very limited, for short snippets)
def emulate_bytes(code_bytes, arch='x86_64', start_addr=0x1000, timeout=1000):
    if not UNICORN_AVAILABLE:
        return "Unicorn not installed"
    # This is intentionally conservative: we map a small memory region and try to run a few instructions.
    try:
        if arch == 'x86_64':
            uc = Uc(UC_ARCH_X86, UC_MODE_64)
            mem_size = 0x2000
            uc.mem_map(start_addr, mem_size)
            uc.mem_write(start_addr, code_bytes)
            # set RIP to start
            uc.reg_write(0x0000000000000000 + 0x10, 0)  # placeholder if needed
            # We won't actually run arbitrary bytes by default; return a note
            return "Emulation available but disabled by default for safety. Enable and adapt if you know the ISA."
        else:
            return "Emulation for this ISA not implemented in this helper"
    except Exception as e:
        return f"Emulation error: {e}"

# Experiment runner: try multiple ISAs and endianness
def run_experiments(words, try_endians=('big','little'), archs=('x86_64','arm','arm64','mips','riscv')):
    results = {}
    for endian in try_endians:
        b = words_to_bytes(words, endian=endian)
        results[endian] = {
            'hexdump': hexdump(b),
            'disasm': {}
        }
        for arch in archs:
            results[endian]['disasm'][arch] = disassemble_bytes(b, arch=arch)
    return results

# Example usage
if __name__ == "__main__":
    print("Converting SHA-256 K constants to bytes and disassembling across ISAs...\n")
    res = run_experiments(K)
    for endian, data in res.items():
        print(f"\n=== Endian: {endian} ===\n")
        print("Hexdump (first 128 bytes):")
        print(indent('\n'.join(data['hexdump'].splitlines()[:8]), '  '))
        for arch, dis in data['disasm'].items():
            print(f"\n-- Disassembly as {arch} --")
            print(indent(dis if dis else "(none)", '  '))

```

    Converting SHA-256 K constants to bytes and disassembling across ISAs...
    
    
    === Endian: big ===
    
    Hexdump (first 128 bytes):
      0000  42 8a 2f 98 71 37 44 91 b5 c0 fb cf e9 b5 db a5   B./.q7D.........
      0010  39 56 c2 5b 59 f1 11 f1 92 3f 82 a4 ab 1c 5e d5   9V.[Y....?....^.
      0020  d8 07 aa 98 12 83 5b 01 24 31 85 be 55 0c 7d c3   ......[.$1..U.}.
      0030  72 be 5d 74 80 de b1 fe 9b dc 06 a7 c1 9b f1 74   r.]t...........t
      0040  e4 9b 69 c1 ef be 47 86 0f c1 9d c6 24 0c a1 cc   ..i...G.....$...
      0050  2d e9 2c 6f 4a 74 84 aa 5c b0 a9 dc 76 f9 88 da   -.,oJt..\...v...
      0060  98 3e 51 52 a8 31 c6 6d b0 03 27 c8 bf 59 7f c7   .>QR.1.m..'..Y..
      0070  c6 e0 0b f3 d5 a7 91 47 06 ca 63 51 14 29 29 67   .......G..cQ.))g
    
    -- Disassembly as x86_64 --
      0x1000:	mov	bpl, byte ptr [rdi]
      0x1003:	cwde	
      0x1004:	jno	0x103d
      0x1006:	xchg	ecx, eax
      0x1008:	mov	ch, 0xc0
      0x100a:	sti	
      0x100b:	iretd	
      0x100c:	jmp	0x39a5ebc6
      0x1011:	push	rsi
      0x1012:	ret	0x595b
      0x1015:	int1	
      0x1016:	adc	ecx, esi
      0x1018:	xchg	edx, eax
    
    -- Disassembly as arm --
      0x1000:	stmdals	pc!, {r1, r6, sb, fp, pc}
      0x1004:	hvc	#0x4371
      0x1008:	svcgt	#0xfbc0b5
      0x100c:	ldrbge	fp, [fp, #0x5e9]
      0x1010:	blpl	#0xff0968fc
    
    -- Disassembly as arm64 --
      0x1000:	ldrsw	x2, #0x60148
      0x1004:	add	x17, x27, #0x10d, lsl #12
    
    -- Disassembly as mips --
      0x1000:	lwr	$t7, -0x75be($at)
      0x1004:	lbu	$a0, 0x3771($t2)
      0x1008:	pref	0x1b, -0x3f4b($ra)
      0x100c:	sh	$k1, -0x4a17($t6)
    
    -- Disassembly as riscv --
      (no instructions decoded)
    
    === Endian: little ===
    
    Hexdump (first 128 bytes):
      0000  98 2f 8a 42 91 44 37 71 cf fb c0 b5 a5 db b5 e9   ./.B.D7q........
      0010  5b c2 56 39 f1 11 f1 59 a4 82 3f 92 d5 5e 1c ab   [.V9...Y..?..^..
      0020  98 aa 07 d8 01 5b 83 12 be 85 31 24 c3 7d 0c 55   .....[....1$.}.U
      0030  74 5d be 72 fe b1 de 80 a7 06 dc 9b 74 f1 9b c1   t].r........t...
      0040  c1 69 9b e4 86 47 be ef c6 9d c1 0f cc a1 0c 24   .i...G.........$
      0050  6f 2c e9 2d aa 84 74 4a dc a9 b0 5c da 88 f9 76   o,.-..tJ...\...v
      0060  52 51 3e 98 6d c6 31 a8 c8 27 03 b0 c7 7f 59 bf   RQ>.m.1..'....Y.
      0070  f3 0b e0 c6 47 91 a7 d5 51 63 ca 06 67 29 29 14   ....G...Qc..g)).
    
    -- Disassembly as x86_64 --
      0x1000:	cwde	
    
    -- Disassembly as arm --
      0x1000:	addmi	r2, sl, #152, #30
    
    -- Disassembly as arm64 --
      (no instructions decoded)
    
    -- Disassembly as mips --
      (no instructions decoded)
    
    -- Disassembly as riscv --
      (no instructions decoded)
    


```python
# SHA256_K_disasm_probe.py
# Purpose: convert SHA-256 K constants to bytes, show hexdumps, and attempt disassembly across ISAs.
# Requirements: Python 3.8+, capstone (pip install capstone), binascii
# Usage: run in a notebook or python interpreter. Outputs printed to stdout.

import struct
import binascii
import textwrap
import sys

# Try to import capstone for disassembly; if not present, report and continue.
try:
    from capstone import *
    CAPSTONE_AVAILABLE = True
except Exception as e:
    CAPSTONE_AVAILABLE = False
    capstone_import_error = str(e)

# Full SHA-256 K constants (64 words) as 32-bit unsigned integers (hex)
K_hex = [
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

def words_to_bytes(words, endian='big'):
    """Pack list of 32-bit words into bytes with specified endianness."""
    b = bytearray()
    for w in words:
        if endian == 'big':
            b.extend(struct.pack('>I', w))
        else:
            b.extend(struct.pack('<I', w))
    return bytes(b)

def hexdump(data, width=16, max_bytes=None):
    """Return a formatted hexdump string (like hexdump -C)."""
    if max_bytes is None:
        max_bytes = len(data)
    out_lines = []
    for i in range(0, min(len(data), max_bytes), width):
        chunk = data[i:i+width]
        hex_bytes = ' '.join(f'{c:02x}' for c in chunk)
        ascii_repr = ''.join((chr(c) if 32 <= c < 127 else '.') for c in chunk)
        out_lines.append(f'{i:04x}  {hex_bytes:<{width*3}}  {ascii_repr}')
    return '\n'.join(out_lines)

def try_disasm(data, arch_name, base_addr=0x1000):
    """Attempt disassembly with capstone for a given arch_name string."""
    if not CAPSTONE_AVAILABLE:
        return f'Capstone not available: {capstone_import_error}'
    try:
        if arch_name == 'x86_64':
            md = Cs(CS_ARCH_X86, CS_MODE_64)
        elif arch_name == 'x86_32':
            md = Cs(CS_ARCH_X86, CS_MODE_32)
        elif arch_name == 'arm':
            md = Cs(CS_ARCH_ARM, CS_MODE_ARM)
        elif arch_name == 'arm_thumb':
            md = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
        elif arch_name == 'arm64':
            md = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
        elif arch_name == 'mips':
            md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_BIG_ENDIAN)
        elif arch_name == 'mips_le':
            md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
        elif arch_name == 'riscv':
            # Capstone may not support riscv in some builds; handle gracefully
            md = Cs(CS_ARCH_RISCV, CS_MODE_RISCV32)
        else:
            return f'Unsupported arch_name: {arch_name}'
    except Exception as e:
        return f'Failed to create disassembler for {arch_name}: {e}'

    md.detail = False
    out = []
    try:
        for insn in md.disasm(data, base_addr):
            out.append(f'0x{insn.address:x}:\t{insn.mnemonic}\t{insn.op_str}')
        if not out:
            return f'No instructions decoded for {arch_name} (data may not align to valid instructions).'
        return '\n'.join(out)
    except Exception as e:
        return f'Disassembly error for {arch_name}: {e}'

def main():
    print('SHA-256 K constants probe\n')
    print('Total constants:', len(K_hex))
    print('\nK constants (hex):')
    for i, w in enumerate(K_hex):
        print(f'K[{i:02d}] = 0x{w:08x}')
    print('\n--- Convert to bytes (big-endian) ---')
    be = words_to_bytes(K_hex, endian='big')
    print('Length (bytes):', len(be))
    print('\nHexdump (first 128 bytes, big-endian):')
    print(hexdump(be, max_bytes=128))
    print('\nFull hexdump (big-endian):')
    print(hexdump(be))

    print('\n--- Convert to bytes (little-endian) ---')
    le = words_to_bytes(K_hex, endian='little')
    print('Length (bytes):', len(le))
    print('\nHexdump (first 128 bytes, little-endian):')
    print(hexdump(le, max_bytes=128))
    print('\nFull hexdump (little-endian):')
    print(hexdump(le))

    # Attempt disassembly across ISAs for both endians
    archs_to_try = [
        ('x86_64', be),
        ('x86_64', le),
        ('x86_32', be),
        ('arm', be),
        ('arm_thumb', be),
        ('arm64', be),
        ('mips', be),
        ('mips_le', le),
        ('riscv', be),
    ]

    print('\n--- Disassembly attempts (requires capstone) ---')
    if not CAPSTONE_AVAILABLE:
        print('Capstone library not available. Install with: pip install capstone')
        print('Proceeding without disassembly.')
    for arch_name, data in archs_to_try:
        print('\n' + '='*60)
        print(f'Arch: {arch_name} | Endian used: {"big" if data is be else "little"} | bytes: {len(data)}')
        print('-'*60)
        result = try_disasm(data, arch_name)
        # Limit output length for readability
        if isinstance(result, str):
            # If long, show first 2000 chars
            if len(result) > 2000:
                print(result[:2000] + '\n... (truncated) ...')
            else:
                print(result)
        else:
            print(result)

    # Save raw bytes to files for offline analysis if desired
    try:
        with open('sha256_K_be.bin', 'wb') as f:
            f.write(be)
        with open('sha256_K_le.bin', 'wb') as f:
            f.write(le)
        print('\nRaw byte files written: sha256_K_be.bin, sha256_K_le.bin')
    except Exception as e:
        print('\nCould not write binary files:', e)

    print('\nNotes and suggestions:')
    print(textwrap.fill(
        "1) These constants are arbitrary 32-bit words; interpreting them as machine code will often produce "
        "nonsense or invalid instructions. Disassemblers will decode sequences where bit patterns align with "
        "valid opcodes, but that does not imply meaningful code. 2) Try sliding windows (offsets) and different "
        "base addresses; many ISAs require alignment. 3) For deeper analysis, try concatenating the constants with "
        "padding or repeating patterns, or embedding them into a crafted section of a minimal ELF/PE/Mach-O "
        "container so disassemblers treat them as code sections. 4) If you want, I can run this script here and "
        "return the raw disassembly outputs captured from this environment.",
        width=80
    ))

if __name__ == '__main__':
    main()

```

    SHA-256 K constants probe
    
    Total constants: 64
    
    K constants (hex):
    K[00] = 0x428a2f98
    K[01] = 0x71374491
    K[02] = 0xb5c0fbcf
    K[03] = 0xe9b5dba5
    K[04] = 0x3956c25b
    K[05] = 0x59f111f1
    K[06] = 0x923f82a4
    K[07] = 0xab1c5ed5
    K[08] = 0xd807aa98
    K[09] = 0x12835b01
    K[10] = 0x243185be
    K[11] = 0x550c7dc3
    K[12] = 0x72be5d74
    K[13] = 0x80deb1fe
    K[14] = 0x9bdc06a7
    K[15] = 0xc19bf174
    K[16] = 0xe49b69c1
    K[17] = 0xefbe4786
    K[18] = 0x0fc19dc6
    K[19] = 0x240ca1cc
    K[20] = 0x2de92c6f
    K[21] = 0x4a7484aa
    K[22] = 0x5cb0a9dc
    K[23] = 0x76f988da
    K[24] = 0x983e5152
    K[25] = 0xa831c66d
    K[26] = 0xb00327c8
    K[27] = 0xbf597fc7
    K[28] = 0xc6e00bf3
    K[29] = 0xd5a79147
    K[30] = 0x06ca6351
    K[31] = 0x14292967
    K[32] = 0x27b70a85
    K[33] = 0x2e1b2138
    K[34] = 0x4d2c6dfc
    K[35] = 0x53380d13
    K[36] = 0x650a7354
    K[37] = 0x766a0abb
    K[38] = 0x81c2c92e
    K[39] = 0x92722c85
    K[40] = 0xa2bfe8a1
    K[41] = 0xa81a664b
    K[42] = 0xc24b8b70
    K[43] = 0xc76c51a3
    K[44] = 0xd192e819
    K[45] = 0xd6990624
    K[46] = 0xf40e3585
    K[47] = 0x106aa070
    K[48] = 0x19a4c116
    K[49] = 0x1e376c08
    K[50] = 0x2748774c
    K[51] = 0x34b0bcb5
    K[52] = 0x391c0cb3
    K[53] = 0x4ed8aa4a
    K[54] = 0x5b9cca4f
    K[55] = 0x682e6ff3
    K[56] = 0x748f82ee
    K[57] = 0x78a5636f
    K[58] = 0x84c87814
    K[59] = 0x8cc70208
    K[60] = 0x90befffa
    K[61] = 0xa4506ceb
    K[62] = 0xbef9a3f7
    K[63] = 0xc67178f2
    
    --- Convert to bytes (big-endian) ---
    Length (bytes): 256
    
    Hexdump (first 128 bytes, big-endian):
    0000  42 8a 2f 98 71 37 44 91 b5 c0 fb cf e9 b5 db a5   B./.q7D.........
    0010  39 56 c2 5b 59 f1 11 f1 92 3f 82 a4 ab 1c 5e d5   9V.[Y....?....^.
    0020  d8 07 aa 98 12 83 5b 01 24 31 85 be 55 0c 7d c3   ......[.$1..U.}.
    0030  72 be 5d 74 80 de b1 fe 9b dc 06 a7 c1 9b f1 74   r.]t...........t
    0040  e4 9b 69 c1 ef be 47 86 0f c1 9d c6 24 0c a1 cc   ..i...G.....$...
    0050  2d e9 2c 6f 4a 74 84 aa 5c b0 a9 dc 76 f9 88 da   -.,oJt..\...v...
    0060  98 3e 51 52 a8 31 c6 6d b0 03 27 c8 bf 59 7f c7   .>QR.1.m..'..Y..
    0070  c6 e0 0b f3 d5 a7 91 47 06 ca 63 51 14 29 29 67   .......G..cQ.))g
    
    Full hexdump (big-endian):
    0000  42 8a 2f 98 71 37 44 91 b5 c0 fb cf e9 b5 db a5   B./.q7D.........
    0010  39 56 c2 5b 59 f1 11 f1 92 3f 82 a4 ab 1c 5e d5   9V.[Y....?....^.
    0020  d8 07 aa 98 12 83 5b 01 24 31 85 be 55 0c 7d c3   ......[.$1..U.}.
    0030  72 be 5d 74 80 de b1 fe 9b dc 06 a7 c1 9b f1 74   r.]t...........t
    0040  e4 9b 69 c1 ef be 47 86 0f c1 9d c6 24 0c a1 cc   ..i...G.....$...
    0050  2d e9 2c 6f 4a 74 84 aa 5c b0 a9 dc 76 f9 88 da   -.,oJt..\...v...
    0060  98 3e 51 52 a8 31 c6 6d b0 03 27 c8 bf 59 7f c7   .>QR.1.m..'..Y..
    0070  c6 e0 0b f3 d5 a7 91 47 06 ca 63 51 14 29 29 67   .......G..cQ.))g
    0080  27 b7 0a 85 2e 1b 21 38 4d 2c 6d fc 53 38 0d 13   '.....!8M,m.S8..
    0090  65 0a 73 54 76 6a 0a bb 81 c2 c9 2e 92 72 2c 85   e.sTvj.......r,.
    00a0  a2 bf e8 a1 a8 1a 66 4b c2 4b 8b 70 c7 6c 51 a3   ......fK.K.p.lQ.
    00b0  d1 92 e8 19 d6 99 06 24 f4 0e 35 85 10 6a a0 70   .......$..5..j.p
    00c0  19 a4 c1 16 1e 37 6c 08 27 48 77 4c 34 b0 bc b5   .....7l.'HwL4...
    00d0  39 1c 0c b3 4e d8 aa 4a 5b 9c ca 4f 68 2e 6f f3   9...N..J[..Oh.o.
    00e0  74 8f 82 ee 78 a5 63 6f 84 c8 78 14 8c c7 02 08   t...x.co..x.....
    00f0  90 be ff fa a4 50 6c eb be f9 a3 f7 c6 71 78 f2   .....Pl......qx.
    
    --- Convert to bytes (little-endian) ---
    Length (bytes): 256
    
    Hexdump (first 128 bytes, little-endian):
    0000  98 2f 8a 42 91 44 37 71 cf fb c0 b5 a5 db b5 e9   ./.B.D7q........
    0010  5b c2 56 39 f1 11 f1 59 a4 82 3f 92 d5 5e 1c ab   [.V9...Y..?..^..
    0020  98 aa 07 d8 01 5b 83 12 be 85 31 24 c3 7d 0c 55   .....[....1$.}.U
    0030  74 5d be 72 fe b1 de 80 a7 06 dc 9b 74 f1 9b c1   t].r........t...
    0040  c1 69 9b e4 86 47 be ef c6 9d c1 0f cc a1 0c 24   .i...G.........$
    0050  6f 2c e9 2d aa 84 74 4a dc a9 b0 5c da 88 f9 76   o,.-..tJ...\...v
    0060  52 51 3e 98 6d c6 31 a8 c8 27 03 b0 c7 7f 59 bf   RQ>.m.1..'....Y.
    0070  f3 0b e0 c6 47 91 a7 d5 51 63 ca 06 67 29 29 14   ....G...Qc..g)).
    
    Full hexdump (little-endian):
    0000  98 2f 8a 42 91 44 37 71 cf fb c0 b5 a5 db b5 e9   ./.B.D7q........
    0010  5b c2 56 39 f1 11 f1 59 a4 82 3f 92 d5 5e 1c ab   [.V9...Y..?..^..
    0020  98 aa 07 d8 01 5b 83 12 be 85 31 24 c3 7d 0c 55   .....[....1$.}.U
    0030  74 5d be 72 fe b1 de 80 a7 06 dc 9b 74 f1 9b c1   t].r........t...
    0040  c1 69 9b e4 86 47 be ef c6 9d c1 0f cc a1 0c 24   .i...G.........$
    0050  6f 2c e9 2d aa 84 74 4a dc a9 b0 5c da 88 f9 76   o,.-..tJ...\...v
    0060  52 51 3e 98 6d c6 31 a8 c8 27 03 b0 c7 7f 59 bf   RQ>.m.1..'....Y.
    0070  f3 0b e0 c6 47 91 a7 d5 51 63 ca 06 67 29 29 14   ....G...Qc..g)).
    0080  85 0a b7 27 38 21 1b 2e fc 6d 2c 4d 13 0d 38 53   ...'8!...m,M..8S
    0090  54 73 0a 65 bb 0a 6a 76 2e c9 c2 81 85 2c 72 92   Ts.e..jv.....,r.
    00a0  a1 e8 bf a2 4b 66 1a a8 70 8b 4b c2 a3 51 6c c7   ....Kf..p.K..Ql.
    00b0  19 e8 92 d1 24 06 99 d6 85 35 0e f4 70 a0 6a 10   ....$....5..p.j.
    00c0  16 c1 a4 19 08 6c 37 1e 4c 77 48 27 b5 bc b0 34   .....l7.LwH'...4
    00d0  b3 0c 1c 39 4a aa d8 4e 4f ca 9c 5b f3 6f 2e 68   ...9J..NO..[.o.h
    00e0  ee 82 8f 74 6f 63 a5 78 14 78 c8 84 08 02 c7 8c   ...toc.x.x......
    00f0  fa ff be 90 eb 6c 50 a4 f7 a3 f9 be f2 78 71 c6   .....lP......xq.
    
    --- Disassembly attempts (requires capstone) ---
    
    ============================================================
    Arch: x86_64 | Endian used: big | bytes: 256
    ------------------------------------------------------------
    0x1000:	mov	bpl, byte ptr [rdi]
    0x1003:	cwde	
    0x1004:	jno	0x103d
    0x1006:	xchg	ecx, eax
    0x1008:	mov	ch, 0xc0
    0x100a:	sti	
    0x100b:	iretd	
    0x100c:	jmp	0x39a5ebc6
    0x1011:	push	rsi
    0x1012:	ret	0x595b
    0x1015:	int1	
    0x1016:	adc	ecx, esi
    0x1018:	xchg	edx, eax
    
    ============================================================
    Arch: x86_64 | Endian used: little | bytes: 256
    ------------------------------------------------------------
    0x1000:	cwde	
    
    ============================================================
    Arch: x86_32 | Endian used: big | bytes: 256
    ------------------------------------------------------------
    0x1000:	inc	edx
    0x1001:	mov	ch, byte ptr [edi]
    0x1003:	cwde	
    0x1004:	jno	0x103d
    0x1006:	inc	esp
    0x1007:	xchg	ecx, eax
    0x1008:	mov	ch, 0xc0
    0x100a:	sti	
    0x100b:	iretd	
    0x100c:	jmp	0x39a5ebc6
    0x1011:	push	esi
    0x1012:	ret	0x595b
    0x1015:	int1	
    0x1016:	adc	ecx, esi
    0x1018:	xchg	edx, eax
    0x1019:	aas	
    0x101a:	and	byte ptr [ebx + ebp*4 - 0x272aa1e4], 7
    0x1022:	stosb	byte ptr es:[edi], al
    0x1023:	cwde	
    0x1024:	adc	al, byte ptr [ebx + 0x3124015b]
    0x102a:	test	dword ptr [esi - 0x3c82f3ab], edi
    0x1030:	jb	0xff0
    0x1032:	pop	ebp
    0x1033:	je	0xfb5
    0x1035:	fidiv	word ptr [ecx + 0x6dc9bfe]
    0x103b:	cmpsd	dword ptr [esi], dword ptr es:[edi]
    0x103c:	rcr	dword ptr [ebx - 0x641b8b0f], 0x69
    0x1043:	shr	edi, 0xbe
    0x1046:	inc	edi
    0x1047:	xchg	byte ptr [edi], cl
    0x1049:	rcr	dword ptr [ebp - 0x5ef3db3a], 0xcc
    0x1050:	sub	eax, 0x4a6f2ce9
    0x1055:	je	0xfdb
    0x1057:	stosb	byte ptr es:[edi], al
    0x1058:	pop	esp
    0x1059:	mov	al, 0xa9
    0x105b:	fdiv	qword ptr [esi - 7]
    0x105e:	mov	dl, bl
    0x1060:	cwde	
    0x1061:	push	ecx
    0x1063:	push	edx
    0x1064:	test	al, 0x31
    
    ============================================================
    Arch: arm | Endian used: big | bytes: 256
    ------------------------------------------------------------
    0x1000:	stmdals	pc!, {r1, r6, sb, fp, pc}
    0x1004:	hvc	#0x4371
    0x1008:	svcgt	#0xfbc0b5
    0x100c:	ldrbge	fp, [fp, #0x5e9]
    0x1010:	blpl	#0xff0968fc
    
    ============================================================
    Arch: arm_thumb | Endian used: big | bytes: 256
    ------------------------------------------------------------
    0x1000:	ldrh	r2, [r0, #0x12]
    0x1002:	ldr	r0, [sp, #0xbc]
    0x1004:	adds	r7, #0x71
    0x1006:	str	r1, [sp, #0x110]
    0x1008:	stm	r0!, {r0, r2, r4, r5, r7}
    0x100a:	ldm	r7, {r0, r1, r3, r4, r5, r6, r7}
    0x100c:	push	{r0, r3, r5, r6, r7, lr}
    0x100e:	adr	r5, #0x36c
    0x1010:	ldrsb	r1, [r7, r0]
    0x1012:	ldrh	r2, [r0, r7]
    0x1014:	bl	#0x55a23a
    0x1018:	subs	r7, #0x92
    0x101a:	adr	r4, #0x208
    0x101c:	adds	r3, r5, #2
    0x101e:	bpl	#0x10de
    0x1020:	lsls	r0, r3, #0x1f
    0x1022:	ldr	r0, [sp, #0x2a8]
    0x1024:	strh	r2, [r2, #0x18]
    0x1026:	lsls	r3, r3, #5
    0x1028:	adds	r1, #0x24
    0x102a:	bkpt	#0x85
    0x102c:	lsrs	r5, r2, #0x11
    0x102e:	stm	r3!, {r0, r2, r3, r4, r5, r6}
    0x1030:	bkpt	#0x72
    0x1032:	strb	r5, [r3, #0x11]
    0x1034:	udf	#0x80
    0x1036:	mrc2	p12, #5, sp, c1, c11, #4
    0x103a:	adr	r7, #0x18
    0x103c:	ldr	r3, [sp, #0x304]
    0x103e:	strb	r1, [r6, #0x13]
    0x1040:	ldr	r3, [sp, #0x390]
    0x1042:	stm	r1!, {r0, r3, r5, r6}
    0x1044:	bkpt	#0xef
    0x1046:	strh	r7, [r0, #0x32]
    0x1048:	stm	r1!, {r0, r1, r2, r3}
    0x104a:	stm	r6!, {r0, r2, r3, r4, r7}
    0x104c:	lsrs	r4, r4, #0x10
    0x104e:	ldm	r4!, {r0, r5, r7}
    
    ============================================================
    Arch: arm64 | Endian used: big | bytes: 256
    ------------------------------------------------------------
    0x1000:	ldrsw	x2, #0x60148
    0x1004:	add	x17, x27, #0x10d, lsl #12
    
    ============================================================
    Arch: mips | Endian used: big | bytes: 256
    ------------------------------------------------------------
    No instructions decoded for mips (data may not align to valid instructions).
    
    ============================================================
    Arch: mips_le | Endian used: little | bytes: 256
    ------------------------------------------------------------
    No instructions decoded for mips_le (data may not align to valid instructions).
    
    ============================================================
    Arch: riscv | Endian used: big | bytes: 256
    ------------------------------------------------------------
    No instructions decoded for riscv (data may not align to valid instructions).
    
    Raw byte files written: sha256_K_be.bin, sha256_K_le.bin
    
    Notes and suggestions:
    1) These constants are arbitrary 32-bit words; interpreting them as machine code
    will often produce nonsense or invalid instructions. Disassemblers will decode
    sequences where bit patterns align with valid opcodes, but that does not imply
    meaningful code. 2) Try sliding windows (offsets) and different base addresses;
    many ISAs require alignment. 3) For deeper analysis, try concatenating the
    constants with padding or repeating patterns, or embedding them into a crafted
    section of a minimal ELF/PE/Mach-O container so disassemblers treat them as code
    sections. 4) If you want, I can run this script here and return the raw
    disassembly outputs captured from this environment.
    


```python
# sha256_k_decompile_probe.py
# Run: python sha256_k_decompile_probe.py
import os
from pathlib import Path
from textwrap import dedent

# --- Constants (full list provided by user) ---
K_hex = [
"0x428a2f98","0x71374491","0xb5c0fbcf","0xe9b5dba5","0x3956c25b","0x59f111f1","0x923f82a4","0xab1c5ed5",
"0xd807aa98","0x12835b01","0x243185be","0x550c7dc3","0x72be5d74","0x80deb1fe","0x9bdc06a7","0xc19bf174",
"0xe49b69c1","0xefbe4786","0x0fc19dc6","0x240ca1cc","0x2de92c6f","0x4a7484aa","0x5cb0a9dc","0x76f988da",
"0x983e5152","0xa831c66d","0xb00327c8","0xbf597fc7","0xc6e00bf3","0xd5a79147","0x06ca6351","0x14292967",
"0x27b70a85","0x2e1b2138","0x4d2c6dfc","0x53380d13","0x650a7354","0x766a0abb","0x81c2c92e","0x92722c85",
"0xa2bfe8a1","0xa81a664b","0xc24b8b70","0xc76c51a3","0xd192e819","0xd6990624","0xf40e3585","0x106aa070",
"0x19a4c116","0x1e376c08","0x2748774c","0x34b0bcb5","0x391c0cb3","0x4ed8aa4a","0x5b9cca4f","0x682e6ff3",
"0x748f82ee","0x78a5636f","0x84c87814","0x8cc70208","0x90befffa","0xa4506ceb","0xbef9a3f7","0xc67178f2"
]

# --- Utilities ---
def hex_list_to_bytes(hex_list, endian='big'):
    b = bytearray()
    for h in hex_list:
        v = int(h, 16)
        if endian == 'big':
            b.extend(v.to_bytes(4, 'big'))
        else:
            b.extend(v.to_bytes(4, 'little'))
    return bytes(b)

OUT = Path("disasm")
OUT.mkdir(exist_ok=True)

# write raw binaries
be_bytes = hex_list_to_bytes(K_hex, 'big')
le_bytes = hex_list_to_bytes(K_hex, 'little')
Path("sha256_K_be.bin").write_bytes(be_bytes)
Path("sha256_K_le.bin").write_bytes(le_bytes)

print("Wrote sha256_K_be.bin and sha256_K_le.bin (256 bytes each).")

# --- Capstone disassembly harness ---
try:
    from capstone import *
except Exception as e:
    print("Capstone not installed. Install with: pip install capstone")
    raise

# architectures to try (capstone constants)
ARCHS = [
    ('x86_64', CS_ARCH_X86, CS_MODE_64),
    ('x86_32', CS_ARCH_X86, CS_MODE_32),
    ('arm', CS_ARCH_ARM, CS_MODE_ARM),
    ('arm_thumb', CS_ARCH_ARM, CS_MODE_THUMB),
    ('arm64', CS_ARCH_ARM64, CS_MODE_ARM),
    ('mips32', CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_BIG_ENDIAN),
    ('mips32_le', CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN),
    # riscv support depends on capstone build; include if available
]

# helper to attempt riscv if present
try:
    from capstone import CS_ARCH_RISCV, CS_MODE_RISCV32
    ARCHS.append(('riscv32', CS_ARCH_RISCV, CS_MODE_RISCV32))
except Exception:
    pass

# sliding offsets and alignments
OFFSETS = list(range(0, 16))  # try offsets 0..15
WINDOW_SIZES = [32, 64, 128, 256]  # window sizes to disassemble

def disasm_bytes(arch_name, arch, mode, data, base_addr=0x1000, max_insns=200):
    md = Cs(arch, mode)
    md.detail = False
    out_lines = []
    for i in range(0, len(data)):
        try:
            for insn in md.disasm(data[i:], base_addr + i):
                out_lines.append("0x{:x}:\t{}\t{}".format(insn.address, insn.mnemonic, insn.op_str))
                if len(out_lines) > max_insns:
                    break
            break
        except Exception:
            # decoding failed at this offset; continue
            break
    return out_lines

# main loop: for each endian, arch, offset, window
for endian_label, data in [('be', be_bytes), ('le', le_bytes)]:
    for arch_name, arch, mode in ARCHS:
        arch_dir = OUT / f"{arch_name}_{endian_label}"
        arch_dir.mkdir(parents=True, exist_ok=True)
        for off in OFFSETS:
            for w in WINDOW_SIZES:
                if off >= len(data):
                    continue
                chunk = data[off:off+w]
                try:
                    md = Cs(arch, mode)
                    md.detail = False
                    # attempt disassembly; capture first N instructions
                    lines = []
                    for insn in md.disasm(chunk, 0x1000 + off):
                        lines.append("0x{:x}:\t{}\t{}".format(insn.address, insn.mnemonic, insn.op_str))
                        if len(lines) >= 200:
                            break
                    fname = arch_dir / f"offset{off:02d}_win{w}.txt"
                    with open(fname, "w") as f:
                        f.write(f"# arch={arch_name} endian={endian_label} offset={off} window={w}\n")
                        if lines:
                            f.write("\n".join(lines))
                        else:
                            f.write("# no valid instructions decoded (or decoding produced no output)\n")
                except Exception as e:
                    # write error file
                    fname = arch_dir / f"offset{off:02d}_win{w}_error.txt"
                    with open(fname, "w") as f:
                        f.write(str(e))

print("Disassembly attempts complete. Check the 'disasm' directory for outputs.")

# --- Optional: embed into minimal ELF code section (requires lief) ---
try:
    import lief
    def make_minimal_elf_code_section(bytes_blob, out_path="sha256_k_code.elf", arch=lief.ELF.ARCH.x86_64):
        binary = lief.ELF.Binary("sha256_k_probe", lief.ELF.ELF_CLASS.CLASS64)
        binary.header.identity_os_abi = lief.ELF.OS_ABI.SYSTEMV
        # create a .text section with the bytes
        sec = lief.ELF.Section(".text")
        sec.content = list(bytes_blob)
        sec.type = lief.ELF.SECTION_TYPES.PROGBITS
        sec.flags = lief.ELF.SECTION_FLAGS.EXECINSTR | lief.ELF.SECTION_FLAGS.ALLOC
        binary.add(sec, loaded=True)
        binary.write(out_path)
        print(f"Wrote minimal ELF: {out_path}")
    # create both BE and LE ELF files (note: endianness in ELF is separate; we embed raw bytes)
    make_minimal_elf_code_section(be_bytes, out_path="sha256_K_be.elf")
    make_minimal_elf_code_section(le_bytes, out_path="sha256_K_le.elf")
    print("If you open these ELF files with objdump/IDA/Ghidra, treat the .text as code and try different ISAs.")
except Exception as e:
    print("lief not available or ELF creation failed; skip ELF embedding. Install lief to enable this step.")

# --- Summary file with metadata and hexdumps ---
summary = OUT / "summary.txt"
with open(summary, "w") as f:
    f.write("SHA-256 K constants probe\n\n")
    f.write("Total constants: 64\n\n")
    f.write("K constants (hex):\n")
    for i,h in enumerate(K_hex):
        f.write(f"K[{i:02d}] = {h}\n")
    f.write("\nWrote raw binaries: sha256_K_be.bin, sha256_K_le.bin\n")
    f.write("Disassembly outputs: disasm/<arch>_<endian>/offsetXX_winYY.txt\n")
print("Summary written to disasm/summary.txt")

```

    Wrote sha256_K_be.bin and sha256_K_le.bin (256 bytes each).
    Disassembly attempts complete. Check the 'disasm' directory for outputs.
    lief not available or ELF creation failed; skip ELF embedding. Install lief to enable this step.
    Summary written to disasm/summary.txt
    


```python
# sha_parity_probe.py
import hashlib
import numpy as np
from scipy.fft import fft

def sha256_bytes(msg: bytes):
    return hashlib.sha256(msg).digest()

def extract_padding_bits(msg: bytes):
    # For a simple probe, hash many related messages and examine specific 32-bit words
    h = sha256_bytes(msg)
    # return list of 32-bit words as ints
    return [int.from_bytes(h[i:i+4], 'big') for i in range(0, 32, 4)]

def spectral_test_on_word_deltas(msgs):
    # msgs: list of byte strings (e.g., mirrored pairs)
    deltas = []
    for a,b in msgs:
        wa = extract_padding_bits(a)
        wb = extract_padding_bits(b)
        # compute signed deltas for each 4-byte word
        deltas.append([ (x - y) for x,y in zip(wa, wb) ])
    arr = np.array(deltas).T  # shape (words, samples)
    for i,row in enumerate(arr):
        spec = np.abs(fft(row))
        print(f"word {i} peak:", spec.max())

if __name__ == "__main__":
    # example mirrored pairs
    pairs = [(b"ABC", b"CBA"), (b"Hello", b"olleH")]
    spectral_test_on_word_deltas(pairs)

```

    word 0 peak: 5165462911.0
    word 1 peak: 1366769115.0
    word 2 peak: 4534750278.0
    word 3 peak: 1693920329.0
    word 4 peak: 664890819.0
    word 5 peak: 1775812731.0
    word 6 peak: 1661431138.0
    word 7 peak: 672585357.0
    


```python
# compute normalized PSD and SNR for each word
from scipy.signal import welch
import numpy as np

def word_psd_snr(word_series, fs=1.0, nperseg=None):
    f, Pxx = welch(word_series, fs=fs, nperseg=nperseg, window='hann', scaling='density')
    peak_idx = np.argmax(Pxx)
    peak_power = Pxx[peak_idx]
    noise_power = np.median(np.delete(Pxx, peak_idx))
    snr = peak_power / (noise_power + 1e-12)
    return f, Pxx, peak_idx, peak_power, snr

```


```python
# permutation test: shuffle sample order many times and recompute peak power
def permutation_pvalue(word_series, n_iter=2000):
    _, Pxx_obs, peak_idx, peak_power_obs, _ = word_psd_snr(word_series)
    count = 0
    for _ in range(n_iter):
        shuffled = np.random.permutation(word_series)
        _, Pxx_sh, _, peak_power_sh, _ = word_psd_snr(shuffled)
        if peak_power_sh >= peak_power_obs:
            count += 1
    pval = (count + 1) / (n_iter + 1)
    return peak_power_obs, pval

```


```python
from scipy.signal import coherence, csd

def word_coherence_phase(x, y, fs=1.0, nperseg=None):
    f, Cxy = coherence(x, y, fs=fs, nperseg=nperseg)
    f, Pxy = csd(x, y, fs=fs, nperseg=nperseg)
    phase = np.angle(Pxy)
    return f, Cxy, phase

```


```python
# Save as nexus_parity_probe_analysis.py and run: python nexus_parity_probe_analysis.py
import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import trange
import os

# ---------------------------
# CONFIG
# ---------------------------
OUTDIR = "nexus_output"
os.makedirs(OUTDIR, exist_ok=True)
FS = 1.0            # sample rate (cycles per sample); adjust if you have real sampling rate
NPERSEG = 256       # PSD segment length (tune to your series length)
N_PERM = 2000       # permutation iterations for p-value
SNR_THRESHOLD = 5.0 # heuristic threshold
PVAL_THRESHOLD = 0.01

# ---------------------------
# USER DATA: replace these with your real time series arrays
# If you only have the 8 peak magnitudes, the script will synthesize example series.
# Replace `word_series_list` with your real arrays shaped (n_samples,) for each word.
# ---------------------------
# Provided peaks (used to seed synthetic example)
peaks = [5165462911.0,1366769115.0,4534750278.0,1693920329.0,
         664890819.0,1775812731.0,1661431138.0,672585357.0]

def synthesize_from_peaks(peaks, n_samples=4096, fs=FS):
    rng = np.random.default_rng(42)
    t = np.arange(n_samples) / fs
    words = []
    for i, pk in enumerate(peaks):
        # choose a frequency proportional to index to avoid collisions
        freq = 0.005*(i+1)  # cycles per sample (very low freq for demonstration)
        # amplitude scaled to peak value (but keep numeric stability)
        amp = pk / (1e9) * 1.0
        signal = amp * np.sin(2*np.pi*freq*t + rng.uniform(0,2*np.pi))
        # add broadband noise
        noise = rng.normal(scale=amp*0.2, size=n_samples)
        words.append(signal + noise)
    return words

# If you have real data, set `use_synth=False` and replace `word_series_list` with your arrays.
use_synth = True
if use_synth:
    word_series_list = synthesize_from_peaks(peaks, n_samples=4096)
else:
    # Example placeholder: replace with real arrays
    word_series_list = [np.loadtxt(f"word{i}.csv") for i in range(8)]

# ---------------------------
# FUNCTIONS
# ---------------------------
def compute_psd(word_series, fs=FS, nperseg=NPERSEG):
    f, Pxx = ss.welch(word_series, fs=fs, nperseg=nperseg, window='hann', scaling='density')
    peak_idx = np.argmax(Pxx)
    peak_power = Pxx[peak_idx]
    # robust background estimate: median excluding ±2 bins around peak
    exclude = np.arange(max(0, peak_idx-2), min(len(Pxx), peak_idx+3))
    bg = np.median(np.delete(Pxx, exclude))
    snr = peak_power / (bg + 1e-30)
    return f, Pxx, peak_idx, peak_power, bg, snr

def permutation_pvalue(word_series, n_iter=N_PERM):
    f, Pxx, peak_idx, peak_power_obs, bg, snr = compute_psd(word_series)
    count = 0
    rng = np.random.default_rng(123)
    for _ in range(n_iter):
        shuffled = rng.permutation(word_series)
        _, Pxx_sh, _, peak_power_sh, _, _ = compute_psd(shuffled)
        if peak_power_sh >= peak_power_obs:
            count += 1
    pval = (count + 1) / (n_iter + 1)
    return peak_power_obs, pval, f[peak_idx]

def compute_coherence_phase(x, y, fs=FS, nperseg=NPERSEG):
    f, Cxy = ss.coherence(x, y, fs=fs, nperseg=nperseg)
    f, Pxy = ss.csd(x, y, fs=fs, nperseg=nperseg)
    phase = np.angle(Pxy)
    return f, Cxy, phase

# ---------------------------
# ANALYSIS
# ---------------------------
results = []
psd_fig, axs = plt.subplots(4,2, figsize=(14,12))
axs = axs.flatten()
for i, series in enumerate(word_series_list):
    f, Pxx, peak_idx, peak_power, bg, snr = compute_psd(series)
    peak_power_obs, pval, peak_freq = permutation_pvalue(series)
    results.append({
        "word": i,
        "peak_power": float(peak_power_obs),
        "bg_median": float(bg),
        "snr": float(snr),
        "peak_freq": float(peak_freq),
        "perm_pval": float(pval)
    })
    ax = axs[i]
    ax.semilogy(f, Pxx, label=f"word {i}")
    ax.axvline(peak_freq, color='r', linestyle='--', label=f"peak {peak_freq:.5f}")
    ax.set_xlabel("Freq (cycles/sample)")
    ax.set_ylabel("PSD")
    ax.legend()
psd_fig.tight_layout()
psd_fig.savefig(os.path.join(OUTDIR, "psd_per_word.png"), dpi=150)

# Save numeric summary
df = pd.DataFrame(results)
df.to_csv(os.path.join(OUTDIR, "summary.csv"), index=False)

# ---------------------------
# COHERENCE & PHASE HEATMAPS
# ---------------------------
n = len(word_series_list)
# compute coherence matrix at each word's peak frequency (closest bin)
coh_matrix = np.zeros((n,n))
phase_matrix = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        f, Cxy, phase = compute_coherence_phase(word_series_list[i], word_series_list[j])
        # pick coherence at the peak frequency of word i
        target_freq = df.loc[df.word==i, "peak_freq"].values[0]
        idx = np.argmin(np.abs(f - target_freq))
        coh_matrix[i,j] = Cxy[idx]
        phase_matrix[i,j] = phase[idx]

plt.figure(figsize=(8,6))
plt.imshow(coh_matrix, vmin=0, vmax=1, cmap='viridis')
plt.colorbar(label='Coherence')
plt.title("Coherence matrix (at each word's peak freq)")
plt.xlabel("word j")
plt.ylabel("word i")
plt.savefig(os.path.join(OUTDIR, "coherence_matrix.png"), dpi=150)

plt.figure(figsize=(8,6))
plt.imshow(np.angle(np.exp(1j*phase_matrix)), cmap='twilight', vmin=-np.pi, vmax=np.pi)
plt.colorbar(label='Phase (radians)')
plt.title("Phase matrix (radians) at each word's peak freq")
plt.xlabel("word j")
plt.ylabel("word i")
plt.savefig(os.path.join(OUTDIR, "phase_matrix.png"), dpi=150)

# ---------------------------
# REPORT / INTERPRETATION HINTS
# ---------------------------
# Add interpretation heuristics to CSV
df['snr_flag'] = df['snr'] > SNR_THRESHOLD
df['pval_flag'] = df['perm_pval'] < PVAL_THRESHOLD
df.to_csv(os.path.join(OUTDIR, "summary_with_flags.csv"), index=False)

print("Analysis complete.")
print("Outputs written to folder:", OUTDIR)
print("Key files: psd_per_word.png, coherence_matrix.png, phase_matrix.png, summary_with_flags.csv")

```

    Analysis complete.
    Outputs written to folder: nexus_output
    Key files: psd_per_word.png, coherence_matrix.png, phase_matrix.png, summary_with_flags.csv
    


    
![png](output_10_1.png)
    



    
![png](output_10_2.png)
    



    
![png](output_10_3.png)
    



```python
#!/usr/bin/env python3
"""
Reproduce spectral/parity probe on SHA256 K constants and diagnostics
Single-file notebook-style script.

Author: Generated for user
Seed: 20260111

Notes:
- Safety: This script performs only spectral/diagnostic analysis on a 256-byte block.
- It does NOT attempt to invert SHA-256 or perform preimage attacks.
- Uses numpy, scipy, matplotlib, pandas, seaborn, statsmodels (for FDR).
"""

import os
import logging
from typing import Tuple, Dict, List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from numpy.fft import fft
from statsmodels.stats.multitest import fdrcorrection

# ---------------------------
# Configuration / Constants
# ---------------------------
OUT_DIR = "."
SEED = 20260111
RNG = np.random.default_rng(SEED)

NFFT = 256
FS = 1.0  # cycles per sample; frequency bins will be bin/NFFT
WINDOW = signal.windows.hann(NFFT, sym=False)
NO_OVERLAP = 0
PERMUTATIONS = 10000  # permutation count for p-values
SURROGATES = 1000     # surrogate global shuffles
SURROGATE_SEED = 20260111

# Filenames to be produced
SUMMARY_CSV = os.path.join(OUT_DIR, "summary.csv")
SUMMARY_FLAGS_CSV = os.path.join(OUT_DIR, "summary_with_flags.csv")
COHERENCE_CSV = os.path.join(OUT_DIR, "coherence.csv")
PHASE_CSV = os.path.join(OUT_DIR, "phase.csv")
SURROGATE_NPZ = os.path.join(OUT_DIR, "surrogate_stats.npz")

# PNG outputs
PSD_PNG = os.path.join(OUT_DIR, "psd_grid.png")
COHERENCE_PNG = os.path.join(OUT_DIR, "coherence_heatmap.png")
PHASE_PNG = os.path.join(OUT_DIR, "phase_heatmap.png")
SURROGATE_PNG = os.path.join(OUT_DIR, "surrogate_pvals_heatmap.png")
ENDIAN_PNG = os.path.join(OUT_DIR, "endian_comparison.png")
CHUNK_SENS_PNG = os.path.join(OUT_DIR, "chunking_sensitivity.png")
BISPEC_PNG = os.path.join(OUT_DIR, "bispectrum_example.png")
PARITY_PNG = os.path.join(OUT_DIR, "parity_autocorr.png")

# ---------------------------
# Input bytes (big-endian canonical)
# ---------------------------
HEX_BYTES_BE = (
    "428a2f9871374491b5c0fbcfe9b5dba53956c25b59f111f1923f82a4ab1c5ed5"
    "d807aa9812835b01243185be550c7dc372be5d7480deb1fe9bdc06a7c19bf174"
    "e49b69c1efbe47860fc19dc6240ca1cc2de92c6f4a7484aa5cb0a9dc76f988da"
    "983e5152a831c66db00327c8bf597fc7c6e00bf3d5a7914706ca635114292967"
    "27b70a852e1b21384d2c6dfc53380d13650a7354766a0abb81c2c92e92722c85"
    "a2bfe8a1a81a664bc24b8b70c76c51a3d192e819d6990624f40e3585106aa070"
    "19a4c1161e376c082748774c34b0bcb5391c0cb34ed8aa4a5b9cca4f682e6ff3"
    "748f82ee78a5636f84c878148cc7020890befffaa4506cebbef9a3f7c67178f2"
)
BYTES_BE = bytes.fromhex(HEX_BYTES_BE)
assert len(BYTES_BE) == 256, "Input must be 256 bytes"

# ---------------------------
# Utilities
# ---------------------------
def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)

def save_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    logging.info(f"Saved CSV: {path}")

def save_npz(path: str, **kwargs):
    np.savez_compressed(path, **kwargs)
    logging.info(f"Saved NPZ: {path}")

# ---------------------------
# Chunking and endian helpers
# ---------------------------
def chunk_bytes(data: bytes, n_chunks: int) -> List[bytes]:
    """Split bytes into n_chunks equal pieces."""
    L = len(data)
    assert L % n_chunks == 0
    chunk_len = L // n_chunks
    return [data[i*chunk_len:(i+1)*chunk_len] for i in range(n_chunks)]

def bytes_to_uint_sequence(block: bytes, target_len: int = 256) -> np.ndarray:
    """Return float sequence 0..255, zero-padded/truncated to target_len."""
    arr = np.frombuffer(block, dtype=np.uint8).astype(float)
    if len(arr) < target_len:
        out = np.zeros(target_len, dtype=float)
        out[:len(arr)] = arr
        return out
    else:
        return arr[:target_len]

def little_endian_variants(data: bytes) -> Dict[str, bytes]:
    """Return two little-endian reinterpretations:
       - reverse each 4-byte word
       - reverse entire byte array
    """
    # reverse each 4-byte word
    words4 = [data[i:i+4] for i in range(0, len(data), 4)]
    rev_words4 = b"".join(w[::-1] for w in words4)
    # reverse entire array
    rev_all = data[::-1]
    return {"rev_each_4": rev_words4, "rev_all": rev_all}

# ---------------------------
# Spectral helpers
# ---------------------------
def compute_welch_psd(x: np.ndarray, nfft: int = NFFT, fs: float = FS, window=WINDOW, noverlap: int = NO_OVERLAP):
    """Return freqs (bins) and PSD (power) using Welch with specified NFFT and Hann window."""
    freqs, Pxx = signal.welch(x, fs=fs, window=window, nperseg=nfft, noverlap=noverlap, nfft=nfft, return_onesided=True, scaling='density')
    # Pxx length will be nfft/2+1; we will use bins 0..127 (exclude Nyquist if needed)
    return freqs, Pxx

def detect_top_peak(Pxx: np.ndarray, exclude_bins: List[int] = None, top_n: int = 1) -> Tuple[int, float]:
    """Detect top peak bin index (0..len(Pxx)-1) and power. Optionally exclude bins."""
    if exclude_bins is None:
        exclude_bins = []
    mask = np.ones_like(Pxx, dtype=bool)
    mask[exclude_bins] = False
    # find argmax on masked array
    masked = np.where(mask, Pxx, -np.inf)
    idx = int(np.argmax(masked))
    return idx, float(Pxx[idx])

# ---------------------------
# Coherence and phase helpers
# ---------------------------
def compute_pair_coherence_phase(x: np.ndarray, y: np.ndarray, nfft: int = NFFT, fs: float = FS, window=WINDOW, noverlap: int = NO_OVERLAP):
    """Compute magnitude-squared coherence and cross-spectral density (for phase)."""
    f, Cxy = signal.coherence(x, y, fs=fs, window=window, nperseg=nfft, noverlap=noverlap, nfft=nfft)
    f2, Pxy = signal.csd(x, y, fs=fs, window=window, nperseg=nfft, noverlap=noverlap, nfft=nfft)
    # phase = angle of Pxy
    phase = np.angle(Pxy)
    return f, Cxy, phase

# ---------------------------
# Bispectrum / bicoherence (simple estimator)
# ---------------------------
def compute_bicoherence(x: np.ndarray, nfft: int = 128, seg_len: int = 128) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute a simple bicoherence estimate on signal x.
    Returns (f1, f2, bicoherence_matrix) where f1,f2 are frequency bins (0..nfft/2).
    Implementation: segment x into non-overlapping segments, compute FFT per segment,
    then compute normalized bispectrum estimate.
    """
    # downsample/truncate to multiple of seg_len
    L = len(x)
    n_segs = L // seg_len
    if n_segs < 2:
        seg_len = L
        n_segs = 1
    x = x[:n_segs * seg_len]
    segments = x.reshape(n_segs, seg_len)
    # compute FFT per segment
    fft_segs = np.fft.fft(segments, n=nfft, axis=1)[:, :nfft//2+1]  # shape (n_segs, n_bins)
    n_bins = fft_segs.shape[1]
    B = np.zeros((n_bins, n_bins), dtype=complex)
    denom = np.zeros((n_bins, n_bins), dtype=float)
    for s in range(n_segs):
        F = fft_segs[s]
        for i in range(n_bins):
            for j in range(n_bins):
                k = (i + j) % n_bins
                B[i, j] += F[i] * F[j] * np.conj(F[k])
                denom[i, j] += np.abs(F[i] * F[j])**2
    # normalized bicoherence
    with np.errstate(divide='ignore', invalid='ignore'):
        bico = np.abs(B)**2 / denom
        bico[np.isnan(bico)] = 0.0
    freqs = np.arange(n_bins) / nfft
    return freqs, freqs, bico

# ---------------------------
# Main pipeline functions
# ---------------------------
def analyze_chunking(data_bytes: bytes, n_chunks: int, label_prefix: str = "word") -> Tuple[pd.DataFrame, np.ndarray, np.ndarray, Dict]:
    """
    Run steps 2-5 for a given chunking (n_chunks).
    Returns summary_df, coherence_matrix, phase_matrix, and a dict of per-word PSDs and peaks.
    """
    logging.info(f"Analyzing chunking: {n_chunks} chunks")
    chunks = chunk_bytes(data_bytes, n_chunks)
    words = [f"{label_prefix}{i}" for i in range(n_chunks)]
    # Prepare storage
    psd_store = {}
    peaks = {}
    summary_rows = []
    # Preprocess and PSD
    for i, block in enumerate(chunks):
        seq = bytes_to_uint_sequence(block, target_len=NFFT)  # length 256
        freqs, Pxx = compute_welch_psd(seq, nfft=NFFT)
        # restrict to bins 0..127 (one-sided returned includes Nyquist at index 128)
        # We'll use indices 0..127 inclusive (len=128)
        Pxx_use = Pxx[:NFFT//2]
        freqs_use = freqs[:NFFT//2]
        # detect top peak (exclude DC? keep DC allowed)
        peak_bin, peak_power = detect_top_peak(Pxx_use)
        # compute background median excluding ±1 bin around peak
        exclude = [b for b in range(max(0, peak_bin-1), min(len(Pxx_use), peak_bin+2))]
        bg_mask = np.ones_like(Pxx_use, dtype=bool)
        bg_mask[exclude] = False
        bg_median = float(np.median(Pxx_use[bg_mask]))
        snr = float(peak_power / (bg_median + 1e-30))
        peak_freq = float(peak_bin / NFFT)
        psd_store[i] = {"freqs": freqs_use, "Pxx": Pxx_use}
        peaks[i] = {"peak_bin": peak_bin, "peak_power": peak_power, "peak_freq": peak_freq, "bg_median": bg_median, "snr": snr}
        summary_rows.append({
            "word": i,
            "peak_power": peak_power,
            "bg_median": bg_median,
            "snr": snr,
            "peak_bin": peak_bin,
            "peak_freq": peak_freq
        })
    summary_df = pd.DataFrame(summary_rows)
    # Permutation p-values (shuffle bytes within each block)
    perm_pvals = []
    logging.info("Starting within-block permutations for p-values (this may take time)...")
    for i, block in enumerate(chunks):
        seq_orig = bytes_to_uint_sequence(block, target_len=NFFT)
        observed_peak = peaks[i]["peak_power"]
        # permutation distribution
        rng = np.random.default_rng(SEED + i)  # deterministic per-block
        perm_max = np.zeros(PERMUTATIONS, dtype=float)
        for p in range(PERMUTATIONS):
            perm_block = rng.permutation(np.frombuffer(block, dtype=np.uint8))
            seq_perm = np.zeros(NFFT, dtype=float)
            seq_perm[:len(perm_block)] = perm_block
            _, Pxx_perm = compute_welch_psd(seq_perm, nfft=NFFT)
            perm_max[p] = np.max(Pxx_perm[:NFFT//2])
        # empirical p-value (one-sided)
        pval = float((np.sum(perm_max >= observed_peak) + 1) / (PERMUTATIONS + 1))
        perm_pvals.append(pval)
    summary_df["perm_pval"] = perm_pvals
    summary_df["snr_flag"] = summary_df["snr"] > 1.0  # trivial threshold (kept for compatibility)
    summary_df["pval_flag"] = summary_df["perm_pval"] < 0.001
    # Coherence and phase matrices (use each word's own peak bin for pairwise value)
    n = n_chunks
    coherence_mat = np.zeros((n, n), dtype=float)
    phase_mat = np.zeros((n, n), dtype=float)
    logging.info("Computing pairwise coherence and phase matrices...")
    for i in range(n):
        seq_i = bytes_to_uint_sequence(chunks[i], target_len=NFFT)
        for j in range(n):
            seq_j = bytes_to_uint_sequence(chunks[j], target_len=NFFT)
            f, Cxy, phase = compute_pair_coherence_phase(seq_i, seq_j, nfft=NFFT)
            # use peak bin of i (peak_bin is index into Pxx_use which is 0..127)
            peak_bin = peaks[i]["peak_bin"]
            # ensure index in range
            if peak_bin >= len(Cxy):
                val_coh = float(Cxy[-1])
                val_phase = float(phase[-1])
            else:
                val_coh = float(Cxy[peak_bin])
                val_phase = float(phase[peak_bin])
            coherence_mat[i, j] = val_coh
            phase_mat[i, j] = val_phase
    # Save coherence and phase CSVs for this chunking (if n==8, write canonical names)
    if n == 8:
        pd.DataFrame(coherence_mat).to_csv(COHERENCE_CSV, index=False, header=False)
        pd.DataFrame(phase_mat).to_csv(PHASE_CSV, index=False, header=False)
    # Return
    meta = {"psd_store": psd_store, "peaks": peaks, "chunks": chunks}
    return summary_df, coherence_mat, phase_mat, meta

# ---------------------------
# Surrogate baseline
# ---------------------------
def surrogate_baseline(data_bytes: bytes, n_chunks: int = 8, n_surrogates: int = SURROGATES, seed: int = SURROGATE_SEED):
    """Generate surrogate distributions by global shuffling and re-chunking."""
    rng = np.random.default_rng(seed)
    n = n_chunks
    # storage
    surrogate_peak_bins = np.zeros((n_surrogates, n), dtype=int)
    surrogate_peak_powers = np.zeros((n_surrogates, n), dtype=float)
    surrogate_coherences = np.zeros((n_surrogates, n, n), dtype=float)
    for s in range(n_surrogates):
        perm = rng.permutation(np.frombuffer(data_bytes, dtype=np.uint8))
        perm_bytes = bytes(perm.tolist())
        summary_s, coh_s, phase_s, meta_s = analyze_chunking(perm_bytes, n_chunks=n)
        surrogate_peak_bins[s, :] = summary_s["peak_bin"].values
        surrogate_peak_powers[s, :] = summary_s["peak_power"].values
        surrogate_coherences[s, :, :] = coh_s
        if (s+1) % 100 == 0:
            logging.info(f"Surrogate {s+1}/{n_surrogates} done")
    return surrogate_peak_bins, surrogate_peak_powers, surrogate_coherences

# ---------------------------
# Chunking sensitivity wrapper
# ---------------------------
def run_all_chunkings(data_bytes: bytes, chunk_sizes: List[int] = [4, 8, 16]):
    results = {}
    for n in chunk_sizes:
        summary_df, coh, phase, meta = analyze_chunking(data_bytes, n_chunks=n)
        results[n] = {"summary": summary_df, "coherence": coh, "phase": phase, "meta": meta}
    return results

# ---------------------------
# Parity and autocorrelation probes
# ---------------------------
def parity_and_autocorr(chunks: List[bytes]):
    """Compute byte-position parity autocorrelation across words and cross-correlation of LSB positions."""
    n = len(chunks)
    # treat each word as 32-byte vector (if chunk length differs, pad/truncate)
    word_len = len(chunks[0])
    arr = np.zeros((n, word_len), dtype=int)
    for i, b in enumerate(chunks):
        arr[i, :len(b)] = np.frombuffer(b, dtype=np.uint8)
    # parity per byte position (LSB parity)
    lsb = arr & 1  # shape (n, word_len)
    # autocorrelation across positions for each word (sum over words)
    # compute parity autocorrelation averaged across words
    maxlag = word_len - 1
    autocorr = np.zeros((n, 2*maxlag+1), dtype=float)
    for i in range(n):
        seq = lsb[i].astype(float) - np.mean(lsb[i])
        corr = signal.correlate(seq, seq, mode='full')
        autocorr[i] = corr / (np.max(np.abs(corr)) + 1e-30)
    # cross-correlation between LSB positions across words (position-wise correlation)
    crosscorr = np.corrcoef(lsb)  # n x n matrix
    return {"lsb": lsb, "autocorr": autocorr, "crosscorr": crosscorr}

# ---------------------------
# Endian comparison
# ---------------------------
def endian_comparison(data_bytes: bytes):
    variants = little_endian_variants(data_bytes)
    results = {}
    for name, variant in variants.items():
        res = run_all_chunkings(variant, chunk_sizes=[8])  # canonical 8-chunk analysis
        results[name] = res
    # Also include original big-endian
    results["big_endian"] = run_all_chunkings(data_bytes, chunk_sizes=[8])
    # Compare peak bins and coherence matrices
    compare_report = {}
    base_summary = results["big_endian"][8]["summary"]
    base_coh = results["big_endian"][8]["coherence"]
    for k, v in results.items():
        if k == "big_endian":
            continue
        summ = v[8]["summary"]
        coh = v[8]["coherence"]
        # which bins change?
        bin_changes = [(i, int(base_summary.loc[i, "peak_bin"]), int(summ.loc[i, "peak_bin"])) for i in range(8)]
        # which couplings persist? compare top off-diagonal coherence pairs
        # compute difference matrix
        coh_diff = np.abs(base_coh - coh)
        compare_report[k] = {"bin_changes": bin_changes, "coh_diff": coh_diff}
    return results, compare_report

# ---------------------------
# Main
# ---------------------------
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ensure_out_dir()
    logging.info("Starting SHA256 K constants spectral/parity probe pipeline")
    # 1) Input: big-endian bytes already loaded
    data_be = BYTES_BE
    # create little-endian variants
    le_variants = little_endian_variants(data_be)
    # 2-5) canonical 8-block analysis
    summary_df, coherence_mat, phase_mat, meta = analyze_chunking(data_be, n_chunks=8)
    save_csv(summary_df, SUMMARY_CSV)
    save_csv(summary_df.assign(snr_flag=summary_df["snr"]>1.0, pval_flag=summary_df["perm_pval"]<0.001), SUMMARY_FLAGS_CSV)
    pd.DataFrame(coherence_mat).to_csv(COHERENCE_CSV, index=False, header=False)
    pd.DataFrame(phase_mat).to_csv(PHASE_CSV, index=False, header=False)
    # 6) Endian test
    endian_results, endian_report = endian_comparison(data_be)
    # 7) Surrogate baseline (this is the heaviest step)
    logging.info("Starting surrogate baseline generation (this may take a while)...")
    s_peak_bins, s_peak_powers, s_coherences = surrogate_baseline(data_be, n_chunks=8, n_surrogates=SURROGATES, seed=SURROGATE_SEED)
    save_npz(SURROGATE_NPZ, peak_bins=s_peak_bins, peak_powers=s_peak_powers, coherences=s_coherences)
    # compute empirical z-scores for observed SNR and coherence
    # SNR observed:
    obs_snr = summary_df["snr"].values
    # surrogate SNRs: compute from surrogate_peak_powers and surrogate background medians approximated by median of surrogate Pxx excluding peak
    # For simplicity, compute surrogate SNR as surrogate_peak_powers / median of surrogate_peak_powers across surrogates for each word
    surrogate_snr = s_peak_powers / (np.median(s_peak_powers, axis=0)[None, :] + 1e-30)
    snr_z = (obs_snr - np.mean(surrogate_snr, axis=0)) / (np.std(surrogate_snr, axis=0) + 1e-30)
    # coherence z-scores for off-diagonals
    obs_coh = coherence_mat
    coh_mean = np.mean(s_coherences, axis=0)
    coh_std = np.std(s_coherences, axis=0) + 1e-30
    coh_z = (obs_coh - coh_mean) / coh_std
    # FDR-corrected p-values for off-diagonal coherence entries
    # compute empirical p-values from surrogate distribution
    pvals_coh = np.ones_like(obs_coh)
    for i in range(8):
        for j in range(8):
            null_dist = s_coherences[:, i, j]
            p_emp = (np.sum(null_dist >= obs_coh[i, j]) + 1) / (len(null_dist) + 1)
            pvals_coh[i, j] = p_emp
    # FDR correction on off-diagonals flattened
    offdiag_idx = [(i, j) for i in range(8) for j in range(8) if i != j]
    p_off = np.array([pvals_coh[i, j] for (i, j) in offdiag_idx])
    reject, pvals_fdr = fdrcorrection(p_off, alpha=0.05, method='indep')
    # reconstruct FDR matrix
    pvals_fdr_mat = np.ones_like(obs_coh)
    k = 0
    for (i, j) in offdiag_idx:
        pvals_fdr_mat[i, j] = pvals_fdr[k]
        k += 1
    # 8) Chunking sensitivity
    chunk_results = run_all_chunkings(data_be, chunk_sizes=[4, 8, 16])
    # build small table showing which peak bins persist across chunkings
    persist_table = []
    for n, res in chunk_results.items():
        summ = res["summary"]
        persist_table.append({"chunks": n, "peak_bins": list(summ["peak_bin"].astype(int).values)})
    persist_df = pd.DataFrame(persist_table)
    persist_csv = os.path.join(OUT_DIR, "chunking_peak_bins.csv")
    persist_df.to_csv(persist_csv, index=False)
    # 9) Higher-order coupling: compute bicoherence for top 3 blocks by SNR
    top3_idx = list(np.argsort(-summary_df["snr"].values)[:3])
    bispec_results = {}
    for idx in top3_idx:
        seq = bytes_to_uint_sequence(meta["chunks"][idx], target_len=NFFT)
        f1, f2, bico = compute_bicoherence(seq, nfft=128, seg_len=64)
        bispec_results[idx] = {"f1": f1, "f2": f2, "bico": bico}
    # 10) Parity and autocorrelation probes
    parity_res = parity_and_autocorr(meta["chunks"])
    # ---------------------------
    # Visualizations
    # ---------------------------
    sns.set(style="whitegrid")
    # PSD grid
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()
    for i in range(8):
        freqs = meta["psd_store"][i]["freqs"]
        Pxx = meta["psd_store"][i]["Pxx"]
        axes[i].plot(freqs, Pxx, color='C0')
        pb = int(summary_df.loc[i, "peak_bin"])
        axes[i].axvline(pb / NFFT, color='r', linestyle='--')
        axes[i].set_title(f"word {i}\npeak {pb}/{NFFT} ({pb/NFFT:.5f})")
        axes[i].set_xlabel("Freq (cycles/sample)")
        axes[i].set_ylabel("PSD")
    plt.tight_layout()
    plt.savefig(PSD_PNG, dpi=200)
    plt.close(fig)
    # Coherence heatmap
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(coherence_mat, annot=False, cmap="viridis", vmin=0, vmax=1, ax=ax)
    ax.set_title("Coherence matrix (at each word's peak freq)")
    ax.set_xlabel("word j")
    ax.set_ylabel("word i")
    plt.savefig(COHERENCE_PNG, dpi=200)
    plt.close(fig)
    # Phase heatmap (centered)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(phase_mat, annot=False, cmap="twilight", center=0, ax=ax)
    ax.set_title("Phase matrix (radians) at each word's peak freq")
    ax.set_xlabel("word j")
    ax.set_ylabel("word i")
    plt.savefig(PHASE_PNG, dpi=200)
    plt.close(fig)
    # Surrogate p-value heatmap (FDR-corrected)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(pvals_fdr_mat, annot=False, cmap="magma_r", vmin=0, vmax=0.05, ax=ax)
    ax.set_title("FDR-corrected p-values for coherence (off-diagonals)")
    plt.savefig(SURROGATE_PNG, dpi=200)
    plt.close(fig)
    # Endian comparison figure: show base coherence and variant diffs
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.heatmap(coherence_mat, ax=axes[0], cmap="viridis", vmin=0, vmax=1)
    axes[0].set_title("Big-endian coherence")
    # pick one variant (rev_each_4) for display
    rev_coh = endian_results["rev_each_4"][8]["coherence"]
    sns.heatmap(np.abs(coherence_mat - rev_coh), ax=axes[1], cmap="inferno")
    axes[1].set_title("Absolute difference (big - rev_each_4)")
    plt.savefig(ENDIAN_PNG, dpi=200)
    plt.close(fig)
    # Chunking sensitivity figure: show peak bins across chunkings
    fig, ax = plt.subplots(figsize=(8, 3))
    for idx, row in persist_df.iterrows():
        ax.plot(range(len(row["peak_bins"])), row["peak_bins"], marker='o', label=f"{row['chunks']} chunks")
    ax.set_xlabel("word index (within chunking)")
    ax.set_ylabel("peak_bin")
    ax.set_title("Chunking sensitivity: peak bins across chunkings")
    plt.legend()
    plt.savefig(CHUNK_SENS_PNG, dpi=200)
    plt.close(fig)
    # Bispectrum example plot for first top block
    bidx = top3_idx[0]
    bres = bispec_results[bidx]
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(bres["bico"], origin='lower', cmap='plasma', extent=(0, 0.5, 0, 0.5))
    ax.set_title(f"Bispectrum magnitude (word {bidx})")
    ax.set_xlabel("f2")
    ax.set_ylabel("f1")
    fig.colorbar(im, ax=ax)
    plt.savefig(BISPEC_PNG, dpi=200)
    plt.close(fig)
    # Parity autocorrelation plot
    fig, axes = plt.subplots(2, 1, figsize=(8, 6))
    # average autocorr across words
    avg_autocorr = np.mean(parity_res["autocorr"], axis=0)
    lags = np.arange(-avg_autocorr.size//2 + 1, avg_autocorr.size//2 + 1)
    axes[0].plot(lags, avg_autocorr)
    axes[0].set_title("Average parity autocorrelation across words (LSB)")
    # crosscorr heatmap
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    sns.heatmap(parity_res["crosscorr"], annot=True, cmap="coolwarm", center=0, ax=ax2)
    ax2.set_title("Cross-correlation between LSB positions across words")
    plt.savefig(PARITY_PNG, dpi=200)
    plt.close(fig)
    plt.close(fig2)
    # ---------------------------
    # Save summary outputs
    # ---------------------------
    save_csv(summary_df, SUMMARY_CSV)
    save_csv(summary_df.assign(snr_flag=summary_df["snr"]>1.0, pval_flag=summary_df["perm_pval"]<0.001), SUMMARY_FLAGS_CSV)
    pd.DataFrame(coherence_mat).to_csv(COHERENCE_CSV, index=False, header=False)
    pd.DataFrame(phase_mat).to_csv(PHASE_CSV, index=False, header=False)
    save_npz(SURROGATE_NPZ, peak_bins=s_peak_bins, peak_powers=s_peak_powers, coherences=s_coherences,
             snr_z=snr_z, coh_z=coh_z, pvals_coh=pvals_coh, pvals_fdr=pvals_fdr_mat)
    # textual summary
    strongest_pairs = []
    # find top off-diagonal coherence pairs
    coh_copy = coherence_mat.copy()
    np.fill_diagonal(coh_copy, -np.inf)
    flat_idx = np.argsort(coh_copy.flatten())[::-1]
    for k in range(6):
        idx = flat_idx[k]
        i = idx // coherence_mat.shape[1]
        j = idx % coherence_mat.shape[1]
        strongest_pairs.append((i, j, coherence_mat[i, j], pvals_fdr_mat[i, j]))
    # Print results
    print("\n--- Generated files ---")
    files = [SUMMARY_CSV, SUMMARY_FLAGS_CSV, COHERENCE_CSV, PHASE_CSV, SURROGATE_NPZ,
             PSD_PNG, COHERENCE_PNG, PHASE_PNG, SURROGATE_PNG, ENDIAN_PNG, CHUNK_SENS_PNG, BISPEC_PNG, PARITY_PNG, persist_csv]
    for f in files:
        print(f"- {f}")
    print("\n--- Short textual summary ---")
    print(f"Peak bins (word 0..7): {list(summary_df['peak_bin'].astype(int).values)}")
    print(f"Peak freqs (bin/NFFT): {list(summary_df['peak_freq'].values)}")
    print("Missing bins (if any) are visible in the peak bins list above.")
    print("Strongest coherence off-diagonal pairs (i, j, coherence, FDR-p):")
    for (i, j, val, p) in strongest_pairs:
        print(f"  ({i}, {j}) -> coh={val:.3f}, FDR-p={p:.4g}")
    print("\nPermutation p-values per word (perm_pval) saved in summary_with_flags.csv.")
    print("Surrogate distributions saved in:", SURROGATE_NPZ)
    logging.info("Pipeline complete.")

if __name__ == "__main__":
    main()

```

    2026-01-11 14:30:58,011 INFO Starting SHA256 K constants spectral/parity probe pipeline
    2026-01-11 14:30:58,011 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:30:58,014 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:02,046 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:02,064 INFO Saved CSV: .\summary.csv
    2026-01-11 14:31:02,066 INFO Saved CSV: .\summary_with_flags.csv
    2026-01-11 14:31:02,067 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:02,068 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:05,987 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:06,005 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:06,007 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:10,029 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:10,046 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:10,048 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:14,200 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:14,217 INFO Starting surrogate baseline generation (this may take a while)...
    2026-01-11 14:31:14,217 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:14,219 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:18,150 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:18,168 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:18,170 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:22,159 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:22,177 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:22,178 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:26,090 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:26,107 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:26,109 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:30,092 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:30,109 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:30,110 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:34,003 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:34,020 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:34,022 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:37,987 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:38,003 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:38,005 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:41,930 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:41,948 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:41,950 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:46,038 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:46,054 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:46,056 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:50,066 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:50,084 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:50,086 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:54,117 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:54,134 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:54,136 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:31:58,114 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:31:58,131 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:31:58,133 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:02,433 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:02,450 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:02,452 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:06,623 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:06,642 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:06,643 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:11,000 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:11,020 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:11,021 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:20,714 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:20,754 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:20,757 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:30,959 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:30,999 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:31,002 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:41,285 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:41,324 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:41,327 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:51,263 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:51,302 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:51,305 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:32:58,207 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:32:58,224 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:32:58,225 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:02,006 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:02,023 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:02,024 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:05,865 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:05,884 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:05,885 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:10,013 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:10,031 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:10,032 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:13,978 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:13,995 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:13,997 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:17,882 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:17,900 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:17,902 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:21,918 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:21,937 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:21,939 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:25,861 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:25,877 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:25,879 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:34,592 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:34,630 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:34,633 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:44,498 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:44,539 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:44,542 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:33:54,628 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:33:54,668 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:33:54,671 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:05,028 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:05,067 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:05,070 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:11,381 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:11,400 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:11,402 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:16,271 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:16,291 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:16,293 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:20,990 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:21,009 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:21,011 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:25,199 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:25,217 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:25,219 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:29,258 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:29,275 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:29,277 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:33,454 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:33,472 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:33,473 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:37,445 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:37,463 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:37,466 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:43,579 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:43,618 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:43,621 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:34:53,497 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:34:53,538 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:34:53,541 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:03,413 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:03,454 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:03,457 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:13,320 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:13,359 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:13,362 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:17,777 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:17,795 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:17,797 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:21,617 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:21,634 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:21,635 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:25,504 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:25,521 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:25,523 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:29,331 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:29,348 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:29,350 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:33,160 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:33,177 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:33,178 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:36,995 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:37,012 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:37,013 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:40,895 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:40,914 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:40,916 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:44,883 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:44,909 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:44,911 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:48,901 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:48,918 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:48,920 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:52,764 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:52,782 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:52,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:35:56,630 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:35:56,647 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:35:56,648 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:00,604 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:00,623 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:00,624 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:04,479 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:04,496 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:04,498 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:08,320 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:08,338 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:08,340 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:12,166 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:12,183 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:12,184 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:16,066 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:16,085 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:16,087 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:19,958 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:19,974 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:19,976 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:23,984 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:24,004 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:24,006 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:30,151 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:30,190 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:30,193 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:40,082 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:40,123 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:40,126 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:50,016 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:50,056 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:50,059 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:36:59,903 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:36:59,943 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:36:59,945 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:09,749 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:09,788 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:09,791 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:19,701 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:19,739 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:19,742 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:29,569 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:29,608 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:29,611 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:39,463 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:39,501 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:39,504 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:49,348 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:49,386 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:49,389 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:37:59,242 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:37:59,282 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:37:59,285 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:09,157 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:09,196 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:09,199 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:16,914 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:16,930 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:16,931 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:20,775 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:20,792 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:20,794 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:24,643 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:24,659 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:24,661 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:28,507 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:28,524 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:28,525 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:32,349 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:32,366 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:32,368 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:36,203 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:36,219 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:36,221 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:40,288 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:40,308 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:40,310 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:46,911 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:46,949 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:46,952 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:38:57,138 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:38:57,178 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:38:57,181 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:07,013 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:07,053 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:07,056 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:16,955 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:16,994 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:16,997 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:26,857 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:26,896 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:26,899 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:34,358 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:34,375 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:34,376 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:38,245 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:38,262 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:38,264 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:42,114 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:42,131 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:42,133 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:46,060 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:46,079 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:46,081 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:50,204 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:50,223 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:50,226 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:54,236 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:54,255 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:54,256 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:39:58,156 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:39:58,171 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:39:58,173 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:02,300 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:02,318 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:02,319 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:06,421 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:06,438 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:06,439 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:10,995 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:11,035 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:11,037 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:20,948 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:20,987 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:20,990 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:30,927 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:30,966 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:30,969 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:40,983 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:41,029 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:41,032 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:40:51,426 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:40:51,471 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:40:51,475 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:02,109 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:02,149 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:02,152 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:08,836 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:08,854 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:08,856 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:12,870 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:12,888 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:12,890 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:17,273 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:17,291 INFO Surrogate 100/1000 done
    2026-01-11 14:41:17,292 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:17,294 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:21,790 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:21,808 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:21,810 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:29,108 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:29,146 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:29,149 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:39,301 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:39,341 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:39,344 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:49,503 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:49,544 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:49,547 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:41:56,448 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:41:56,469 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:41:56,472 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:01,033 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:01,051 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:01,053 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:05,504 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:05,523 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:05,525 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:11,666 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:11,708 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:11,711 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:21,939 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:21,980 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:21,983 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:32,148 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:32,186 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:32,189 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:42,073 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:42,113 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:42,116 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:42:52,252 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:42:52,292 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:42:52,295 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:02,569 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:02,612 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:02,616 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:12,866 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:12,907 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:12,911 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:22,931 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:22,969 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:22,972 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:32,959 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:32,999 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:33,002 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:42,990 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:43,029 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:43,032 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:43:53,321 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:43:53,359 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:43:53,362 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:03,755 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:03,795 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:03,799 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:14,359 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:14,399 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:14,402 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:24,878 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:24,920 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:24,923 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:35,233 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:35,274 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:35,278 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:45,638 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:45,679 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:45,683 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:44:55,953 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:44:55,992 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:44:55,995 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:06,354 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:06,395 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:06,399 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:16,703 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:16,746 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:16,749 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:27,279 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:27,319 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:27,322 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:37,679 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:37,718 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:37,721 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:46,315 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:46,336 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:46,338 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:50,927 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:50,946 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:50,948 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:45:55,598 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:45:55,616 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:45:55,618 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:03,952 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:03,991 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:03,994 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:14,520 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:14,542 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:14,544 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:18,754 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:18,772 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:18,774 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:23,358 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:23,398 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:23,402 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:28,048 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:28,066 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:28,067 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:34,849 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:34,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:34,893 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:45,202 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:45,243 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:45,246 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:46:55,222 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:46:55,261 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:46:55,264 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:05,591 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:05,632 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:05,635 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:15,770 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:15,809 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:15,812 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:25,815 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:25,854 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:25,858 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:36,475 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:36,515 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:36,518 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:46,789 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:46,829 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:46,832 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:47:57,116 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:47:57,158 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:47:57,161 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:07,407 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:07,447 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:07,450 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:17,740 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:17,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:17,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:28,052 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:28,091 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:28,094 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:38,807 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:38,848 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:38,852 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:49,015 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:49,055 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:49,059 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:48:59,033 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:48:59,073 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:48:59,076 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:49:09,134 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:49:09,173 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:49:09,177 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:49:19,125 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:49:19,167 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:49:19,170 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:49:29,574 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:49:29,612 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:49:29,615 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:49:39,733 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:49:39,771 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:49:39,774 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:49:50,006 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:49:50,044 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:49:50,047 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:00,081 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:00,118 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:00,121 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:10,314 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:10,354 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:10,357 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:20,739 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:20,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:20,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:31,143 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:31,187 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:31,190 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:41,599 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:41,639 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:41,643 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:50:52,169 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:50:52,208 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:50:52,211 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:02,516 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:02,555 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:02,558 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:12,493 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:12,535 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:12,538 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:22,845 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:22,884 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:22,887 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:33,186 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:33,225 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:33,228 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:43,626 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:43,668 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:43,671 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:51:54,046 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:51:54,092 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:51:54,096 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:04,879 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:04,919 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:04,923 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:14,857 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:14,897 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:14,900 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:24,914 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:24,953 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:24,956 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:35,056 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:35,096 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:35,098 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:45,346 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:45,383 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:45,386 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:52:55,334 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:52:55,373 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:52:55,376 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:05,659 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:05,697 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:05,699 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:15,495 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:15,533 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:15,537 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:25,401 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:25,443 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:25,446 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:35,452 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:35,496 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:35,499 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:45,463 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:45,499 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:45,502 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:53:55,229 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:53:55,269 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:53:55,272 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:05,007 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:05,044 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:05,047 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:14,885 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:14,924 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:14,926 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:24,624 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:24,663 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:24,665 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:34,370 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:34,407 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:34,410 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:44,131 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:44,169 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:44,172 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:54:53,921 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:54:53,958 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:54:53,962 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:03,914 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:03,952 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:03,955 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:13,937 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:13,979 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:13,982 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:23,975 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:24,015 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:24,018 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:34,122 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:34,161 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:34,163 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:45,025 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:45,071 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:45,074 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:55:55,501 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:55:55,539 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:55:55,542 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:05,469 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:05,509 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:05,512 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:15,401 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:15,439 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:15,442 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:25,725 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:25,763 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:25,766 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:35,655 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:35,694 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:35,697 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:45,626 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:45,664 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:45,667 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:56:55,521 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:56:55,558 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:56:55,561 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:05,357 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:05,397 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:05,400 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:15,227 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:15,266 INFO Surrogate 200/1000 done
    2026-01-11 14:57:15,267 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:15,270 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:25,130 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:25,169 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:25,172 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:35,339 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:35,380 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:35,383 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:41,316 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:41,336 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:41,338 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:45,574 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:45,591 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:45,592 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:49,637 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:49,653 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:49,655 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:53,888 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:53,906 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:53,908 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:57:58,045 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:57:58,065 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:57:58,067 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:02,277 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:02,294 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:02,295 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:06,971 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:06,989 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:06,991 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:11,349 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:11,373 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:11,376 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:15,745 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:15,763 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:15,765 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:20,162 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:20,181 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:20,182 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:24,629 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:24,648 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:24,650 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:29,223 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:29,244 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:29,246 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:33,712 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:33,731 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:33,732 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:38,113 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:38,132 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:38,134 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:42,589 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:42,608 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:42,609 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:47,123 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:47,142 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:47,144 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:58:53,739 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:58:53,779 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:58:53,782 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:03,896 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:03,934 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:03,937 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:13,768 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:13,809 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:13,812 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:23,731 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:23,774 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:23,778 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:34,311 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:34,352 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:34,355 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:45,647 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:45,690 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:45,693 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 14:59:56,617 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 14:59:56,658 INFO Analyzing chunking: 8 chunks
    2026-01-11 14:59:56,660 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:06,635 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:06,675 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:06,678 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:16,770 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:16,809 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:16,812 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:26,596 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:26,635 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:26,638 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:36,114 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:36,132 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:36,134 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:40,409 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:40,429 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:40,431 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:44,758 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:44,776 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:44,778 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:48,964 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:48,982 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:48,983 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:53,027 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:53,046 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:53,048 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:00:56,977 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:00:56,993 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:00:56,995 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:01,014 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:01,031 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:01,032 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:05,179 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:05,197 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:05,199 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:09,203 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:09,220 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:09,221 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:13,058 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:13,073 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:13,075 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:17,123 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:17,145 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:17,147 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:21,453 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:21,470 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:21,471 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:28,313 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:28,351 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:28,354 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:38,215 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:38,253 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:38,256 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:48,314 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:48,361 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:48,365 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:01:58,288 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:01:58,327 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:01:58,329 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:02:08,193 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:02:08,232 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:02:08,235 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:02:18,332 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:02:18,380 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:02:18,385 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:02:29,012 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:02:29,055 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:02:29,058 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:02:39,960 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:02:40,003 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:02:40,006 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:02:50,046 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:02:50,086 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:02:50,089 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:00,546 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:00,586 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:00,588 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:09,337 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:09,360 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:09,362 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:14,131 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:14,149 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:14,150 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:18,162 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:18,181 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:18,183 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:22,254 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:22,271 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:22,272 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:26,305 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:26,323 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:26,325 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:30,499 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:30,517 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:30,519 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:34,568 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:34,583 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:34,585 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:38,579 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:38,597 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:38,598 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:42,576 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:42,594 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:42,595 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:47,173 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:47,192 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:47,194 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:03:55,389 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:03:55,433 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:03:55,436 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:06,724 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:06,778 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:06,782 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:17,406 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:17,448 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:17,452 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:27,671 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:27,710 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:27,713 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:37,522 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:37,560 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:37,563 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:47,417 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:47,460 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:47,463 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:04:57,437 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:04:57,475 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:04:57,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:07,412 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:07,450 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:07,453 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:17,460 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:17,498 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:17,501 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:27,779 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:27,818 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:27,821 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:33,332 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:33,349 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:33,351 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:37,694 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:37,711 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:37,713 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:41,981 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:41,998 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:42,000 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:46,263 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:46,281 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:46,283 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:50,528 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:50,547 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:50,548 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:54,891 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:54,910 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:54,912 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:05:59,329 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:05:59,348 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:05:59,350 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:06,685 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:06,723 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:06,726 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:17,070 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:17,108 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:17,111 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:25,454 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:25,473 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:25,475 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:29,858 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:29,875 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:29,877 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:34,206 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:34,224 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:34,226 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:38,984 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:39,006 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:39,008 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:43,687 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:43,705 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:43,707 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:47,982 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:47,998 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:48,000 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:52,285 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:52,305 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:52,306 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:06:56,686 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:06:56,727 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:06:56,730 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:03,313 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:03,331 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:03,333 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:07,673 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:07,690 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:07,692 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:12,072 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:12,093 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:12,095 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:16,499 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:16,520 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:16,522 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:21,774 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:21,793 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:21,795 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:26,253 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:26,273 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:26,275 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:30,737 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:30,756 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:30,757 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:35,129 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:35,148 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:35,150 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:39,293 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:39,310 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:39,311 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:43,419 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:43,436 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:43,438 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:07:52,245 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:07:52,283 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:07:52,286 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:02,180 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:02,218 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:02,220 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:12,029 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:12,067 INFO Surrogate 300/1000 done
    2026-01-11 15:08:12,067 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:12,070 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:20,415 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:20,433 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:20,434 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:25,015 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:25,035 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:25,037 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:30,634 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:30,652 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:30,653 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:35,038 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:35,057 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:35,058 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:39,245 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:39,263 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:39,265 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:43,485 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:43,504 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:43,506 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:47,741 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:47,759 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:47,761 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:52,210 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:52,236 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:52,239 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:08:56,403 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:08:56,421 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:08:56,423 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:00,345 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:00,362 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:00,363 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:04,399 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:04,418 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:04,420 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:08,430 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:08,448 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:08,449 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:12,464 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:12,481 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:12,483 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:16,693 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:16,710 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:16,712 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:22,609 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:22,648 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:22,651 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:31,232 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:31,251 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:31,253 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:35,507 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:35,527 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:35,528 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:39,893 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:39,911 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:39,913 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:44,072 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:44,089 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:44,091 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:48,079 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:48,097 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:48,098 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:52,303 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:52,323 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:52,324 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:09:56,449 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:09:56,467 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:09:56,469 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:01,874 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:01,916 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:01,919 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:12,438 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:12,478 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:12,481 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:22,514 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:22,553 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:22,556 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:32,525 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:32,565 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:32,568 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:42,788 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:42,828 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:42,831 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:50,252 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:50,268 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:50,270 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:54,566 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:54,583 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:54,585 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:10:58,796 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:10:58,813 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:10:58,814 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:02,777 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:02,793 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:02,794 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:06,722 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:06,742 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:06,744 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:10,806 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:10,823 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:10,824 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:14,967 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:14,984 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:14,985 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:18,964 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:18,980 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:18,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:22,962 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:22,979 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:22,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:26,989 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:27,007 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:27,009 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:33,119 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:33,159 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:33,162 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:43,026 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:43,064 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:43,066 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:11:53,020 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:11:53,059 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:11:53,062 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:02,922 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:02,960 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:02,963 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:12,841 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:12,879 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:12,882 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:22,769 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:22,788 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:22,789 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:26,624 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:26,641 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:26,643 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:30,753 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:30,771 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:30,773 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:35,114 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:35,132 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:35,134 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:39,362 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:39,382 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:39,384 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:43,615 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:43,633 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:43,635 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:48,053 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:48,074 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:48,076 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:52,604 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:52,622 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:52,624 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:12:57,041 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:12:57,060 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:12:57,061 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:01,442 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:01,461 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:01,463 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:11,260 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:11,298 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:11,301 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:21,236 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:21,274 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:21,277 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:25,530 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:25,549 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:25,550 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:29,875 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:29,893 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:29,894 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:38,564 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:38,603 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:38,605 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:48,755 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:48,794 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:48,797 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:13:59,264 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:13:59,303 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:13:59,306 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:09,421 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:09,442 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:09,445 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:14,018 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:14,041 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:14,043 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:18,664 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:18,684 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:18,686 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:23,368 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:23,387 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:23,389 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:28,956 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:28,974 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:28,976 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:33,552 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:33,573 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:33,575 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:38,014 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:38,033 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:38,034 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:46,452 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:46,471 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:46,473 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:50,801 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:50,818 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:50,820 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:55,004 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:55,023 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:55,024 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:14:59,484 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:14:59,505 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:14:59,508 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:04,113 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:04,131 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:04,133 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:08,314 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:08,331 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:08,333 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:12,866 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:12,884 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:12,887 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:17,355 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:17,376 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:17,378 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:21,982 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:22,004 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:22,005 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:26,532 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:26,550 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:26,552 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:34,584 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:34,625 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:34,628 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:44,780 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:44,820 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:44,823 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:15:54,986 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:15:55,026 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:15:55,029 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:05,419 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:05,461 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:05,465 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:15,930 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:15,973 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:15,977 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:26,411 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:26,451 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:26,455 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:37,034 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:37,075 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:37,078 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:47,675 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:47,722 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:47,726 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:16:58,264 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:16:58,303 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:16:58,306 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:03,907 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:03,928 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:03,930 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:08,384 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:08,403 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:08,404 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:12,965 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:12,983 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:12,984 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:17,410 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:17,428 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:17,430 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:21,856 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:21,875 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:21,877 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:26,257 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:26,275 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:26,276 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:30,624 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:30,643 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:30,644 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:34,961 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:34,980 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:34,982 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:41,582 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:41,622 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:41,625 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:17:51,515 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:17:51,553 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:17:51,556 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:01,472 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:01,512 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:01,515 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:11,436 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:11,474 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:11,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:21,972 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:22,012 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:22,016 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:32,160 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:32,199 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:32,203 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:40,525 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:40,545 INFO Surrogate 400/1000 done
    2026-01-11 15:18:40,545 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:40,547 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:45,126 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:45,146 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:45,148 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:49,587 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:49,604 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:49,606 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:53,873 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:53,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:53,892 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:18:58,309 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:18:58,328 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:18:58,330 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:02,760 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:02,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:02,782 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:07,397 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:07,417 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:07,419 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:17,487 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:17,525 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:17,528 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:27,963 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:28,003 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:28,006 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:37,832 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:37,870 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:37,873 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:47,700 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:47,738 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:47,741 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:19:57,773 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:19:57,811 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:19:57,814 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:07,812 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:07,852 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:07,855 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:18,595 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:18,637 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:18,640 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:28,764 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:28,806 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:28,809 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:39,123 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:39,161 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:39,164 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:49,345 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:49,385 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:49,388 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:20:59,589 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:20:59,631 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:20:59,634 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:10,281 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:10,321 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:10,325 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:21,309 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:21,358 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:21,361 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:32,859 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:32,905 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:32,908 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:44,509 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:44,551 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:44,555 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:51,761 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:51,778 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:51,779 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:55,739 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:55,756 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:55,758 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:21:59,975 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:21:59,992 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:21:59,994 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:04,457 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:04,476 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:04,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:08,893 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:08,912 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:08,914 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:13,260 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:13,278 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:13,280 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:17,522 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:17,541 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:17,543 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:22,082 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:22,100 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:22,102 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:26,931 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:26,950 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:26,952 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:36,939 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:36,978 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:36,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:45,235 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:45,253 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:45,254 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:49,742 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:49,761 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:49,763 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:54,208 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:54,227 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:54,228 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:22:58,711 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:22:58,730 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:22:58,731 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:03,053 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:03,073 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:03,075 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:07,456 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:07,476 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:07,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:11,872 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:11,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:11,892 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:16,394 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:16,412 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:16,415 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:20,613 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:20,633 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:20,635 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:24,930 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:24,948 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:24,949 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:29,341 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:29,358 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:29,360 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:33,667 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:33,685 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:33,687 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:37,992 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:38,011 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:38,013 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:42,595 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:42,615 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:42,618 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:23:51,147 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:23:51,186 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:23:51,190 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:01,524 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:01,564 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:01,567 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:11,841 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:11,891 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:11,894 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:23,021 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:23,072 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:23,075 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:33,912 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:33,952 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:33,955 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:45,077 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:45,118 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:45,121 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:24:55,525 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:24:55,568 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:24:55,570 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:05,393 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:05,416 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:05,417 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:09,376 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:09,393 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:09,395 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:13,491 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:13,508 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:13,509 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:17,447 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:17,464 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:17,466 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:21,595 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:21,611 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:21,613 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:25,641 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:25,658 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:25,660 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:30,492 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:30,531 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:30,534 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:38,060 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:38,077 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:38,079 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:42,032 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:42,051 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:42,053 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:46,014 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:46,030 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:46,031 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:49,997 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:50,016 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:50,017 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:25:54,064 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:25:54,079 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:25:54,081 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:02,566 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:02,604 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:02,607 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:12,464 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:12,502 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:12,505 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:22,400 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:22,439 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:22,442 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:32,464 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:32,503 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:32,506 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:38,960 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:38,978 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:38,979 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:43,012 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:43,028 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:43,030 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:47,044 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:47,061 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:47,062 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:51,014 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:51,030 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:51,031 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:54,924 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:54,941 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:54,942 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:26:58,956 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:26:58,974 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:26:58,976 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:03,099 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:03,118 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:03,120 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:09,206 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:09,254 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:09,257 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:18,219 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:18,235 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:18,237 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:22,112 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:22,129 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:22,132 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:26,181 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:26,197 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:26,199 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:30,155 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:30,172 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:30,174 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:34,056 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:34,073 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:34,075 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:38,086 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:38,104 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:38,105 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:42,029 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:42,046 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:42,047 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:46,102 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:46,118 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:46,120 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:50,102 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:50,123 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:50,125 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:27:54,542 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:27:54,561 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:27:54,563 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:02,072 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:02,110 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:02,113 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:12,073 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:12,124 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:12,129 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:22,602 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:22,641 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:22,644 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:32,560 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:32,600 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:32,603 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:42,489 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:42,527 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:42,530 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:28:52,511 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:28:52,549 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:28:52,552 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:02,454 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:02,494 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:02,497 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:12,414 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:12,453 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:12,456 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:22,574 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:22,616 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:22,619 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:32,787 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:32,826 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:32,829 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:42,899 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:42,939 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:42,942 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:29:53,280 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:29:53,319 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:29:53,322 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:03,463 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:03,504 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:03,508 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:13,845 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:13,886 INFO Surrogate 500/1000 done
    2026-01-11 15:30:13,887 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:13,890 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:24,596 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:24,645 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:24,648 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:35,895 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:35,947 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:35,951 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:46,674 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:46,714 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:46,717 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:30:57,121 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:30:57,163 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:30:57,165 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:07,408 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:07,448 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:07,451 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:17,690 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:17,730 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:17,733 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:29,037 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:29,078 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:29,081 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:38,229 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:38,247 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:38,249 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:42,371 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:42,390 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:42,392 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:46,823 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:46,842 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:46,843 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:51,233 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:51,251 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:51,253 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:31:58,183 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:31:58,223 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:31:58,226 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:05,488 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:05,506 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:05,508 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:09,962 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:09,979 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:09,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:14,441 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:14,463 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:14,465 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:18,920 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:18,937 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:18,939 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:23,304 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:23,323 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:23,325 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:27,759 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:27,777 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:27,779 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:32,142 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:32,161 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:32,163 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:36,606 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:36,623 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:36,625 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:41,099 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:41,119 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:41,121 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:45,664 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:45,682 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:45,684 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:50,184 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:50,202 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:50,203 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:54,554 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:54,572 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:54,573 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:32:58,880 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:32:58,898 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:32:58,900 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:07,592 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:07,632 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:07,635 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:17,515 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:17,553 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:17,557 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:27,412 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:27,450 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:27,454 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:37,345 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:37,384 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:37,387 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:47,294 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:47,334 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:47,337 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:33:57,272 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:33:57,311 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:33:57,314 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:07,158 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:07,198 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:07,201 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:17,120 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:17,160 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:17,163 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:27,338 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:27,377 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:27,380 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:35,447 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:35,465 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:35,466 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:39,373 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:39,390 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:39,392 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:43,405 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:43,423 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:43,424 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:47,495 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:47,512 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:47,514 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:51,609 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:51,624 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:51,626 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:55,771 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:55,790 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:55,792 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:34:59,912 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:34:59,929 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:34:59,930 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:03,863 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:03,881 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:03,882 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:07,897 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:07,916 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:07,918 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:12,501 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:12,543 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:12,547 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:22,464 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:22,503 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:22,506 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:32,364 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:32,402 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:32,405 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:42,208 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:42,246 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:42,250 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:35:52,160 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:35:52,200 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:35:52,202 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:03,173 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:03,220 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:03,224 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:13,606 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:13,646 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:13,649 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:18,760 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:18,778 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:18,779 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:23,111 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:23,130 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:23,132 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:30,482 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:30,523 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:30,526 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:41,506 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:41,547 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:41,550 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:36:52,541 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:36:52,584 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:36:52,588 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:03,556 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:03,603 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:03,606 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:14,433 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:14,470 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:14,473 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:25,298 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:25,338 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:25,341 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:35,734 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:35,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:35,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:46,589 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:46,630 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:46,633 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:37:57,768 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:37:57,809 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:37:57,813 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:08,034 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:38:08,081 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:38:08,085 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:18,404 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:38:18,442 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:38:18,446 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:28,823 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:38:28,865 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:38:28,869 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:39,050 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:38:39,093 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:38:39,097 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:49,420 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:38:49,459 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:38:49,462 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:38:59,959 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:00,000 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:00,003 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:10,094 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:10,133 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:10,136 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:20,270 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:20,309 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:20,312 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:30,017 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:30,055 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:30,058 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:39,859 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:39,898 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:39,901 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:49,646 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:49,685 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:49,688 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:39:59,492 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:39:59,532 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:39:59,535 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:09,345 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:09,385 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:09,388 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:19,255 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:19,292 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:19,295 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:29,178 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:29,217 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:29,220 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:39,010 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:39,050 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:39,053 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:48,933 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:48,973 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:48,975 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:40:58,706 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:40:58,745 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:40:58,749 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:08,585 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:08,625 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:08,629 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:18,441 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:18,481 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:18,484 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:28,323 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:28,363 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:28,366 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:38,253 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:38,290 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:38,293 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:48,190 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:48,227 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:48,231 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:41:58,085 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:41:58,125 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:41:58,128 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:08,029 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:08,068 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:08,071 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:17,936 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:17,975 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:17,978 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:27,923 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:27,963 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:27,966 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:37,832 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:37,871 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:37,874 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:47,763 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:47,802 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:47,805 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:42:57,618 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:42:57,658 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:42:57,661 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:07,541 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:07,580 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:07,582 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:14,362 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:14,378 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:14,380 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:18,155 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:18,172 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:18,173 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:22,044 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:22,061 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:22,063 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:25,874 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:25,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:25,891 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:29,736 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:29,753 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:29,755 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:33,504 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:33,521 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:33,522 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:38,675 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:38,713 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:38,716 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:48,648 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:48,686 INFO Surrogate 600/1000 done
    2026-01-11 15:43:48,687 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:48,690 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:43:58,681 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:43:58,723 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:43:58,726 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:09,075 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:09,115 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:09,118 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:14,973 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:14,990 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:14,991 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:19,466 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:19,484 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:19,486 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:23,955 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:23,972 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:23,974 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:28,331 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:28,350 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:28,352 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:32,865 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:32,884 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:32,886 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:36,993 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:37,014 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:37,017 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:41,051 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:41,068 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:41,069 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:45,162 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:45,179 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:45,181 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:49,590 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:49,606 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:49,608 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:53,829 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:53,845 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:53,847 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:44:59,779 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:44:59,818 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:44:59,821 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:45:09,760 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:45:09,798 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:45:09,801 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:45:19,779 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:45:19,818 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:45:19,821 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:45:29,934 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:45:29,977 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:45:29,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:45:40,308 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:45:40,348 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:45:40,350 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:45:50,307 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:45:50,345 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:45:50,348 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:00,576 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:00,616 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:00,619 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:10,532 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:10,570 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:10,573 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:20,435 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:20,474 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:20,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:31,061 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:31,099 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:31,102 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:40,979 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:41,017 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:41,020 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:46:50,764 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:46:50,802 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:46:50,805 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:00,642 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:00,681 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:00,684 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:10,530 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:10,569 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:10,573 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:20,434 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:20,476 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:20,479 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:30,571 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:30,611 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:30,614 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:40,524 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:40,565 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:40,568 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:47:50,546 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:47:50,590 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:47:50,593 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:00,977 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:01,017 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:01,020 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:11,607 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:11,647 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:11,651 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:21,906 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:21,948 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:21,952 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:32,135 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:32,177 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:32,180 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:42,090 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:42,129 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:42,132 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:48:51,877 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:48:51,915 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:48:51,918 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:01,804 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:01,842 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:01,845 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:11,957 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:12,003 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:12,006 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:22,279 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:22,318 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:22,322 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:32,546 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:32,585 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:32,588 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:42,719 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:42,758 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:42,762 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:49:53,900 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:49:53,940 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:49:53,943 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:04,285 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:04,323 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:04,326 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:14,149 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:14,187 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:14,190 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:24,029 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:24,069 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:24,072 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:34,303 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:34,346 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:34,350 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:45,149 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:45,194 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:45,197 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:50:55,675 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:50:55,717 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:50:55,720 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:05,742 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:05,782 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:05,785 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:15,989 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:16,028 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:16,031 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:26,190 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:26,233 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:26,237 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:36,281 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:36,319 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:36,322 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:46,094 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:46,131 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:46,134 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:51:55,920 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:51:55,959 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:51:55,962 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:05,127 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:05,144 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:05,147 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:08,980 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:08,995 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:08,997 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:12,763 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:12,781 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:12,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:16,637 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:16,654 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:16,655 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:25,630 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:25,669 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:25,672 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:35,667 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:35,706 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:35,709 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:45,587 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:45,626 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:45,629 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:52:55,495 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:52:55,535 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:52:55,538 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:05,395 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:05,435 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:05,438 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:15,315 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:15,353 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:15,356 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:25,929 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:25,976 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:25,980 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:34,974 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:34,993 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:34,995 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:39,656 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:39,678 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:39,680 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:43,834 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:43,851 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:43,853 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:48,241 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:48,259 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:48,261 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:53:58,152 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:53:58,190 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:53:58,193 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:54:08,375 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:54:08,421 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:54:08,424 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:54:19,125 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:54:19,168 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:54:19,171 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:54:29,761 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:54:29,802 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:54:29,805 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:54:40,419 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:54:40,473 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:54:40,478 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:54:51,097 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:54:51,139 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:54:51,143 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:01,518 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:01,558 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:01,562 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:11,627 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:11,670 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:11,673 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:21,934 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:21,975 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:21,978 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:32,566 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:32,606 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:32,610 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:43,358 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:43,410 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:43,414 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:55:54,322 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:55:54,360 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:55:54,363 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:04,249 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:04,288 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:04,291 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:14,326 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:14,367 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:14,370 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:24,820 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:24,862 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:24,866 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:35,159 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:35,200 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:35,203 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:45,228 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:45,267 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:45,270 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:56:55,639 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:56:55,678 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:56:55,681 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:05,802 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:05,841 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:05,844 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:16,256 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:16,295 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:16,298 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:26,486 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:26,525 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:26,527 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:36,507 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:36,548 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:36,551 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:46,402 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:46,442 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:46,444 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:57:56,488 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:57:56,526 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:57:56,529 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:06,637 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:06,675 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:06,678 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:16,712 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:16,751 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:16,754 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:26,693 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:26,734 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:26,738 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:36,690 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:36,728 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:36,731 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:46,699 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:46,736 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:46,739 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:58:56,763 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:58:56,802 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:58:56,805 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:07,032 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:07,075 INFO Surrogate 700/1000 done
    2026-01-11 15:59:07,076 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:07,079 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:17,371 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:17,407 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:17,410 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:27,230 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:27,269 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:27,272 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:37,204 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:37,242 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:37,244 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:47,166 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:47,205 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:47,208 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 15:59:57,054 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 15:59:57,093 INFO Analyzing chunking: 8 chunks
    2026-01-11 15:59:57,096 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:06,863 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:06,902 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:06,904 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:16,685 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:16,724 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:16,727 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:26,459 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:26,497 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:26,500 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:36,226 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:36,266 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:36,269 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:45,993 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:46,031 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:46,035 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:00:55,762 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:00:55,800 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:00:55,803 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:05,568 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:05,605 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:05,608 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:15,368 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:15,407 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:15,410 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:25,179 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:25,218 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:25,220 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:34,935 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:34,973 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:34,976 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:44,751 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:44,789 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:44,791 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:01:54,552 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:01:54,591 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:01:54,595 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:04,334 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:04,372 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:04,375 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:14,103 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:14,141 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:14,144 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:23,890 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:23,929 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:23,932 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:33,697 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:33,736 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:33,739 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:43,485 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:43,524 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:43,527 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:02:53,253 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:02:53,291 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:02:53,294 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:03,042 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:03,080 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:03,083 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:12,841 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:12,878 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:12,881 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:22,640 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:22,679 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:22,682 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:32,489 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:32,528 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:32,531 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:42,287 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:42,326 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:42,328 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:03:52,069 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:03:52,108 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:03:52,111 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:01,891 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:01,928 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:01,931 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:11,662 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:11,701 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:11,704 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:21,485 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:21,525 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:21,528 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:31,257 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:31,295 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:31,298 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:41,011 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:41,052 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:41,055 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:04:50,787 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:04:50,825 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:04:50,829 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:00,561 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:00,600 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:00,603 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:10,302 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:10,341 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:10,343 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:20,148 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:20,186 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:20,189 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:29,931 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:29,969 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:29,972 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:39,739 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:39,777 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:39,780 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:49,531 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:49,570 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:49,572 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:05:59,341 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:05:59,380 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:05:59,383 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:09,097 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:09,135 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:09,137 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:18,892 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:18,930 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:18,933 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:28,640 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:28,678 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:28,681 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:38,412 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:38,450 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:38,452 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:48,164 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:48,203 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:48,206 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:06:57,948 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:06:57,986 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:06:57,989 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:07,716 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:07,755 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:07,758 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:17,542 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:17,581 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:17,584 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:27,320 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:27,359 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:27,362 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:37,100 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:37,139 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:37,142 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:46,898 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:46,936 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:46,938 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:07:56,723 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:07:56,761 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:07:56,764 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:06,520 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:06,557 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:06,560 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:16,316 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:16,356 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:16,359 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:26,106 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:26,147 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:26,150 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:35,922 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:35,959 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:35,962 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:45,679 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:45,716 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:45,719 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:08:55,540 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:08:55,580 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:08:55,583 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:05,315 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:05,355 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:05,359 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:15,120 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:15,158 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:15,162 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:24,992 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:25,032 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:25,035 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:35,060 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:35,101 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:35,104 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:45,005 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:45,044 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:45,047 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:09:54,987 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:09:55,026 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:09:55,029 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:04,804 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:04,842 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:04,845 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:14,633 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:14,671 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:14,674 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:24,407 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:24,446 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:24,448 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:34,178 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:34,217 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:34,220 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:43,964 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:44,002 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:44,005 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:10:53,823 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:10:53,862 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:10:53,864 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:03,732 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:03,772 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:03,775 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:13,689 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:13,728 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:13,731 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:23,640 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:23,678 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:23,682 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:33,557 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:33,597 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:33,600 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:43,461 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:43,500 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:43,503 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:11:53,364 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:11:53,403 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:11:53,406 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:03,225 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:03,265 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:03,268 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:13,110 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:13,148 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:13,151 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:23,018 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:23,059 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:23,062 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:32,936 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:32,975 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:32,978 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:42,842 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:42,880 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:42,883 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:12:52,795 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:12:52,834 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:12:52,837 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:02,707 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:02,745 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:02,748 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:12,550 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:12,588 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:12,591 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:22,508 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:22,547 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:22,550 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:32,377 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:32,418 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:32,420 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:42,248 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:42,285 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:42,288 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:13:52,107 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:13:52,147 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:13:52,150 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:02,035 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:02,074 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:02,077 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:11,986 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:12,023 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:12,026 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:21,846 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:21,884 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:21,886 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:31,751 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:31,790 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:31,793 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:41,692 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:41,731 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:41,735 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:14:51,702 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:14:51,739 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:14:51,743 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:01,579 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:01,617 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:01,620 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:11,470 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:11,510 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:11,513 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:21,447 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:21,486 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:21,489 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:31,425 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:31,463 INFO Surrogate 800/1000 done
    2026-01-11 16:15:31,464 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:31,468 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:41,358 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:41,397 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:41,400 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:15:51,304 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:15:51,342 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:15:51,345 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:01,215 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:01,255 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:01,258 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:11,136 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:11,175 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:11,178 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:21,045 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:21,084 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:21,088 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:30,962 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:30,999 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:31,002 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:40,875 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:40,914 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:40,916 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:16:50,737 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:16:50,774 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:16:50,777 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:00,641 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:00,680 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:00,683 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:10,465 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:10,503 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:10,506 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:20,374 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:20,413 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:20,416 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:30,179 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:30,217 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:30,220 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:40,039 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:40,078 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:40,080 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:49,911 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:49,949 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:49,952 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:17:59,796 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:17:59,835 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:17:59,838 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:09,790 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:09,828 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:09,831 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:19,722 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:19,761 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:19,764 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:29,672 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:29,710 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:29,713 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:39,638 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:39,676 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:39,679 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:47,420 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:47,435 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:47,437 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:51,689 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:51,707 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:51,709 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:18:55,697 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:18:55,717 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:18:55,718 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:00,148 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:00,165 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:00,166 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:04,332 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:04,349 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:04,351 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:08,446 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:08,468 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:08,470 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:12,572 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:12,592 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:12,593 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:16,753 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:16,771 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:16,773 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:20,766 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:20,783 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:20,785 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:24,872 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:24,891 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:24,893 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:31,921 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:31,959 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:31,962 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:41,915 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:41,955 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:41,958 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:19:51,857 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:19:51,897 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:19:51,900 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:01,687 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:01,724 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:01,727 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:11,560 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:11,599 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:11,602 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:21,418 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:21,456 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:21,459 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:31,263 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:31,302 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:31,305 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:41,175 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:41,213 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:41,216 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:20:51,099 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:20:51,139 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:20:51,142 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:00,916 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:00,955 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:00,958 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:10,748 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:10,786 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:10,789 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:20,637 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:20,676 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:20,679 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:30,511 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:30,550 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:30,553 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:40,403 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:40,441 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:40,444 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:21:50,263 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:21:50,306 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:21:50,309 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:00,069 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:00,109 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:00,112 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:09,889 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:09,928 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:09,930 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:19,779 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:19,817 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:19,820 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:29,616 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:29,655 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:29,658 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:39,550 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:39,588 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:39,590 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:49,653 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:49,693 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:49,697 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:22:59,648 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:22:59,687 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:22:59,690 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:09,562 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:09,602 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:09,605 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:19,530 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:19,570 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:19,574 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:29,450 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:29,488 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:29,491 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:39,427 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:39,466 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:39,469 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:49,391 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:49,431 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:49,434 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:23:59,393 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:23:59,432 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:23:59,435 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:09,292 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:09,331 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:09,334 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:19,237 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:19,276 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:19,279 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:29,172 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:29,213 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:29,216 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:39,107 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:39,146 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:39,149 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:48,994 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:49,032 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:49,035 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:24:58,984 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:24:59,024 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:24:59,027 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:08,901 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:08,939 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:08,943 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:18,823 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:18,862 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:18,865 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:28,852 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:28,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:28,893 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:38,825 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:38,864 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:38,867 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:48,726 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:48,765 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:48,768 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:25:58,652 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:25:58,691 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:25:58,694 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:08,613 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:08,652 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:08,656 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:18,542 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:18,582 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:18,585 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:28,618 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:28,657 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:28,659 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:38,590 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:38,630 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:38,633 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:48,554 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:48,594 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:48,597 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:26:58,520 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:26:58,558 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:26:58,561 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:08,461 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:08,500 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:08,502 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:18,432 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:18,470 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:18,472 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:28,330 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:28,369 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:28,372 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:38,285 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:38,322 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:38,325 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:48,217 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:48,256 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:48,259 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:27:58,156 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:27:58,194 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:27:58,197 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:08,078 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:08,117 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:08,120 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:17,997 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:18,035 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:18,038 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:27,924 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:27,961 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:27,964 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:37,822 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:37,860 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:37,863 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:47,704 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:47,743 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:47,746 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:28:57,698 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:28:57,735 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:28:57,738 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:07,635 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:07,675 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:07,677 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:17,584 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:17,623 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:17,626 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:27,475 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:27,513 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:27,516 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:37,429 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:37,468 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:37,472 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:47,375 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:47,414 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:47,417 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:29:57,313 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:29:57,352 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:29:57,356 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:07,265 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:07,305 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:07,308 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:17,192 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:17,232 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:17,235 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:27,082 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:27,122 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:27,124 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:36,955 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:36,995 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:36,998 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:46,788 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:46,827 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:46,830 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:30:56,693 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:30:56,730 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:30:56,733 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:06,564 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:06,602 INFO Surrogate 900/1000 done
    2026-01-11 16:31:06,603 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:06,606 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:16,448 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:16,486 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:16,489 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:26,401 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:26,439 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:26,442 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:36,314 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:36,352 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:36,355 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:46,197 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:46,235 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:46,238 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:31:56,071 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:31:56,109 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:31:56,112 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:05,979 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:06,018 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:06,021 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:15,851 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:15,891 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:15,894 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:25,742 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:25,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:25,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:35,630 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:35,669 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:35,672 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:45,613 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:45,656 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:45,659 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:32:55,605 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:32:55,644 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:32:55,647 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:05,550 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:05,589 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:05,592 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:15,439 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:15,477 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:15,479 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:25,334 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:25,374 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:25,376 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:35,316 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:35,354 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:35,357 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:45,287 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:45,326 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:45,329 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:33:55,222 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:33:55,262 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:33:55,265 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:05,128 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:05,166 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:05,169 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:14,953 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:14,992 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:14,994 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:24,837 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:24,876 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:24,879 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:34,795 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:34,833 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:34,837 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:44,739 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:44,780 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:44,783 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:34:54,647 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:34:54,686 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:34:54,689 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:04,616 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:04,656 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:04,659 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:14,608 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:14,648 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:14,651 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:24,512 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:24,550 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:24,553 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:34,417 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:34,456 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:34,459 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:44,343 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:44,382 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:44,385 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:35:54,230 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:35:54,268 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:35:54,271 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:04,180 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:04,219 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:04,222 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:14,073 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:14,113 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:14,116 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:23,944 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:23,983 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:23,986 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:33,806 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:33,845 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:33,848 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:43,725 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:43,763 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:43,765 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:36:53,630 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:36:53,671 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:36:53,674 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:03,536 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:03,575 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:03,579 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:13,411 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:13,449 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:13,452 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:23,351 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:23,389 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:23,392 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:33,213 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:33,251 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:33,254 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:43,092 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:43,132 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:43,134 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:37:53,028 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:37:53,067 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:37:53,070 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:02,939 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:02,978 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:02,981 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:12,813 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:12,851 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:12,854 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:22,706 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:22,745 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:22,748 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:32,635 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:32,672 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:32,675 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:42,570 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:42,609 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:42,612 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:38:52,421 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:38:52,461 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:38:52,464 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:02,388 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:02,427 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:02,431 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:12,281 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:12,319 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:12,322 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:22,215 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:22,255 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:22,258 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:32,051 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:32,090 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:32,093 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:41,945 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:41,984 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:41,987 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:39:51,820 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:39:51,860 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:39:51,863 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:01,712 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:01,751 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:01,753 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:11,628 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:11,668 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:11,671 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:21,497 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:21,539 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:21,542 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:31,459 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:31,498 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:31,501 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:41,358 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:41,396 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:41,399 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:40:51,242 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:40:51,281 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:40:51,284 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:01,126 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:01,166 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:01,169 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:11,002 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:11,041 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:11,044 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:20,936 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:20,975 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:20,978 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:30,857 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:30,897 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:30,900 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:40,808 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:40,846 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:40,850 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:41:50,677 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:41:50,717 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:41:50,719 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:00,624 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:00,663 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:00,666 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:10,550 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:10,588 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:10,591 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:20,441 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:20,481 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:20,485 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:30,346 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:30,386 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:30,388 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:40,243 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:40,281 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:40,284 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:42:50,124 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:42:50,163 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:42:50,166 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:00,036 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:00,075 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:00,078 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:09,914 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:09,953 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:09,956 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:19,797 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:19,834 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:19,837 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:29,698 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:29,735 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:29,739 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:39,617 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:39,657 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:39,660 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:49,552 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:49,592 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:49,595 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:43:59,443 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:43:59,481 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:43:59,483 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:09,393 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:09,431 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:09,434 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:19,343 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:19,382 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:19,384 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:29,253 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:29,290 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:29,293 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:39,193 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:39,231 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:39,234 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:49,098 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:49,136 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:49,139 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:44:59,023 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:44:59,063 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:44:59,066 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:08,980 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:09,019 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:09,022 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:18,850 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:18,890 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:18,893 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:28,797 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:28,835 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:28,837 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:38,708 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:38,748 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:38,751 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:48,608 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:48,647 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:48,650 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:45:58,505 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:45:58,543 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:45:58,545 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:08,446 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:08,484 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:08,487 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:18,326 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:18,365 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:18,367 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:28,223 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:28,262 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:28,266 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:38,115 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:38,154 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:38,157 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:48,032 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:48,071 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:48,075 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:46:57,988 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:46:58,027 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:46:58,030 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:07,886 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:07,925 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:47:07,928 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:17,765 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:17,803 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:47:17,806 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:27,708 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:27,747 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:47:27,750 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:37,649 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:37,685 INFO Surrogate 1000/1000 done
    2026-01-11 16:47:37,701 INFO Saved NPZ: .\surrogate_stats.npz
    2026-01-11 16:47:37,704 INFO Analyzing chunking: 4 chunks
    2026-01-11 16:47:37,707 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:42,640 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:42,650 INFO Analyzing chunking: 8 chunks
    2026-01-11 16:47:42,653 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:47:52,483 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:47:52,522 INFO Analyzing chunking: 16 chunks
    2026-01-11 16:47:52,526 INFO Starting within-block permutations for p-values (this may take time)...
    2026-01-11 16:48:12,055 INFO Computing pairwise coherence and phase matrices...
    2026-01-11 16:48:14,991 INFO Saved CSV: .\summary.csv
    2026-01-11 16:48:14,993 INFO Saved CSV: .\summary_with_flags.csv
    2026-01-11 16:48:15,009 INFO Saved NPZ: .\surrogate_stats.npz
    2026-01-11 16:48:15,011 INFO Pipeline complete.
    

    
    --- Generated files ---
    - .\summary.csv
    - .\summary_with_flags.csv
    - .\coherence.csv
    - .\phase.csv
    - .\surrogate_stats.npz
    - .\psd_grid.png
    - .\coherence_heatmap.png
    - .\phase_heatmap.png
    - .\surrogate_pvals_heatmap.png
    - .\endian_comparison.png
    - .\chunking_sensitivity.png
    - .\bispectrum_example.png
    - .\parity_autocorr.png
    - .\chunking_peak_bins.csv
    
    --- Short textual summary ---
    Peak bins (word 0..7): [np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(0)]
    Peak freqs (bin/NFFT): [np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0)]
    Missing bins (if any) are visible in the peak bins list above.
    Strongest coherence off-diagonal pairs (i, j, coherence, FDR-p):
      (7, 6) -> coh=1.000, FDR-p=0.9564
      (7, 4) -> coh=1.000, FDR-p=0.9564
      (7, 1) -> coh=1.000, FDR-p=0.9564
      (6, 7) -> coh=1.000, FDR-p=0.9564
      (6, 3) -> coh=1.000, FDR-p=0.9564
      (4, 6) -> coh=1.000, FDR-p=0.9564
    
    Permutation p-values per word (perm_pval) saved in summary_with_flags.csv.
    Surrogate distributions saved in: .\surrogate_stats.npz
    


```python
# sha_feature_integration.py
import numpy as np

# ---------- helpers ----------
def popcount32(x):
    return bin(int(x) & 0xFFFFFFFF).count("1")

def residues_and_phases(arr, m):
    arr = np.asarray(arr, dtype=int)
    r = np.mod(arr, m)
    theta = 2.0 * np.pi * r.astype(float) / float(m)
    return r, theta

# ---------- SHA round feature extractor ----------
def extract_sha_round_features(states, xor_acc, K_constants, H0_constants=None, m=64):
    """
    states: np.ndarray shape (64,8) dtype=uint32 (per-round a..h)
    xor_acc: np.ndarray shape (64,) dtype=uint32 (per-round XOR accumulator or other scalar)
    K_constants: sequence length 64 of uint32 (your modified or standard K)
    H0_constants: optional sequence length 8 of uint32 (not required for these features)
    m: modulus for residues (default 64)
    Returns: dict of feature arrays (length 64)
    """
    rounds = int(states.shape[0])
    features = {}

    # 1) xor bitcount (compact scalar)
    features['xor_bitcount'] = np.array([popcount32(int(x)) for x in xor_acc], dtype=int)

    # 2) mix residue and mix popcount: (a_t XOR K_t)
    mix_residues = np.zeros(rounds, dtype=int)
    mix_popcounts = np.zeros(rounds, dtype=int)
    for t in range(rounds):
        a = int(states[t, 0])  # 'a' register
        Kt = int(K_constants[t]) & 0xFFFFFFFF
        mix = (a ^ Kt) & 0xFFFFFFFF
        mix_residues[t] = int(mix % m)
        mix_popcounts[t] = popcount32(mix)
    features['mix_residue'] = mix_residues
    features['mix_popcount'] = mix_popcounts

    # 3) per-round Hamming distance on 'a' (diffusion)
    a_hamming = np.zeros(rounds, dtype=int)
    prev = int(states[0, 0])
    a_hamming[0] = 0
    for t in range(1, rounds):
        cur = int(states[t, 0])
        a_hamming[t] = popcount32(cur ^ prev)
        prev = cur
    features['a_hamming'] = a_hamming

    # 4) ch and maj popcounts (nonlinear probes)
    ch_counts = np.zeros(rounds, dtype=int)
    maj_counts = np.zeros(rounds, dtype=int)
    for t in range(rounds):
        a = int(states[t, 0]); b = int(states[t, 1]); c = int(states[t, 2])
        ch = (a & b) ^ ((~a) & c)
        maj = (a & b) ^ (a & c) ^ (b & c)
        ch_counts[t] = popcount32(ch)
        maj_counts[t] = popcount32(maj)
    features['ch_popcount'] = ch_counts
    features['maj_popcount'] = maj_counts

    return features

# ---------- Integrate into Universal Verb Detector ----------
def sha_features_to_verb_coords(features, modulus=6, window_sizes=(8,16,32)):
    """
    Convert selected SHA-derived feature arrays into verb coordinates (R, E, SILR, closure).
    - features: dict returned by extract_sha_round_features
    - modulus: m for residues (e.g., 6 or 64)
    - window_sizes: list of window sizes for SILR
    Returns: dict with R, E, SILR, closure_rate and raw residues
    """
    # choose streams to test: mix_residue and xor_bitcount are good candidates
    mix_res = features['mix_residue']  # residues already mod m if extractor used m
    xor_bits = features['xor_bitcount']

    # If mix_res not in desired modulus, re-mod it:
    mix_res_mod = np.mod(mix_res, modulus)

    # R and E on mix_res_mod
    r, theta = residues_and_phases(mix_res_mod, modulus)
    R = float(np.abs(np.mean(np.exp(1j * theta))))
    counts = np.bincount(r.astype(int), minlength=modulus).astype(float)
    p = counts / counts.sum()
    mask = p > 0
    E = float(-np.sum(p[mask] * np.log(p[mask])) / np.log(modulus))

    # SILR on xor_bits (scale invariance across windows)
    x = xor_bits.astype(float)
    S = silr_scale_invariance(x, window_sizes)

    # closure-rate on deltas of mix_res_mod
    deltas = np.diff(mix_res_mod, prepend=mix_res_mod[0])
    closure = closure_rate_from_deltas(deltas, M=modulus)

    return {"R": R, "E": E, "SILR": S, "closure": closure, "residues": mix_res_mod}

# ---------- small helpers (reuse from your pipeline) ----------
def silr_scale_invariance(x: np.ndarray, window_sizes: Sequence[int], eps: float = 1e-12) -> float:
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return 0.0
    S_vals = []
    N = x.size
    for w in window_sizes:
        if w < 4 or w > N:
            continue
        n_windows = max(1, N // w)
        s_list = []
        for i in range(n_windows):
            seg = x[i*w:(i+1)*w]
            if seg.size < 2:
                continue
            mu = seg.mean()
            sigma = seg.std(ddof=0)
            z = (seg - mu) / (sigma + eps)
            S = z.std(ddof=0) / (abs(z.mean()) + eps)
            s_list.append(S)
        if s_list:
            S_vals.append(np.mean(s_list))
    if not S_vals:
        return 0.0
    S_vals = np.array(S_vals)
    mu = S_vals.mean()
    sigma = S_vals.std(ddof=0)
    cv = sigma / (abs(mu) + eps)
    return float(max(0.0, 1.0 - cv))

def closure_rate_from_deltas(deltas: Sequence[int], M: int) -> float:
    if len(deltas) == 0:
        return 0.0
    cum = 0
    hits = 0
    for d in deltas:
        cum = (cum + int(d)) % M
        if cum == 0:
            hits += 1
    return float(hits / len(deltas))

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[10], line 101
         98     return {"R": R, "E": E, "SILR": S, "closure": closure, "residues": mix_res_mod}
        100 # ---------- small helpers (reuse from your pipeline) ----------
    --> 101 def silr_scale_invariance(x: np.ndarray, window_sizes: Sequence[int], eps: float = 1e-12) -> float:
        102     x = np.asarray(x, dtype=float)
        103     if x.size == 0:
    

    NameError: name 'Sequence' is not defined



```python
#!/usr/bin/env python3
"""
Patched Universal Verb Detector + SHA extractor
Fix: define detrend_and_center before it's used to avoid NameError.
Single-file pipeline that:
 - detrends/centers signals
 - safely indexes PSD/CSD outputs
 - extracts SHA round features (mix_residue, xor_bitcount, a_hamming, ch/maj)
 - computes verb coordinates (R, E, SILR, closure)
 - optional excitation (xor_steer by default)
Outputs: NPZ, CSV, combined PNG in ./uvd_sha_output
"""
from __future__ import annotations
import os, logging
from typing import List, Sequence, Tuple, Dict, Any, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from numpy.fft import fft

# -----------------------
# CONFIG
# -----------------------
OUT_DIR = "uvd_sha_output"
os.makedirs(OUT_DIR, exist_ok=True)
SEED = 20260111
RNG = np.random.default_rng(SEED)
NFFT = 256
FS = 1.0
WINDOW = "hann"
NOVERLAP = 128
PERM_WITHIN = 2000
SURROGATES = 500
BICO_N = 128
ENABLE_EXCITATION = True

HEX_BYTES_BE = (
    "428a2f9871374491b5c0fbcfe9b5dba53956c25b59f111f1923f82a4ab1c5ed5"
    "d807aa9812835b01243185be550c7dc372be5d7480deb1fe9bdc06a7c19bf174"
    "e49b69c1efbe47860fc19dc6240ca1cc2de92c6f4a7484aa5cb0a9dc76f988da"
    "983e5152a831c66db00327c8bf597fc7c6e00bf3d5a7914706ca6351142929672"
    "7b70a852e1b21384d2c6dfc53380d13650a7354766a0abb81c2c92e92722c85a2"
    "bfe8a1a81a664bc24b8b70c76c51a3d192e819d6990624f40e3585106aa07019a"
    "4c1161e376c082748774c34b0bcb5391c0cb34ed8aa4a5b9cca4f682e6ff3748f"
    "82ee78a5636f84c878148cc7020890befffaa4506cebbef9a3f7c67178f2"
)
BYTES_BE = bytes.fromhex(HEX_BYTES_BE)

STANDARD_K = np.array([
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
], dtype=np.uint32)

STANDARD_H0 = np.array([
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
], dtype=np.uint32)

CUSTOM_K: Optional[np.ndarray] = None
CUSTOM_H0: Optional[np.ndarray] = None

# -----------------------
# Logging
# -----------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("uvd_sha")

# -----------------------
# Helper functions (including detrend_and_center)
# -----------------------
def rev4_bytes(b: bytes) -> bytes:
    out = bytearray()
    for i in range(0, len(b), 4):
        out.extend(b[i:i+4][::-1])
    return bytes(out)

def revall_bytes(b: bytes) -> bytes:
    return b[::-1]

def chunk_bytes(b: bytes, nblocks: int) -> List[bytes]:
    L = len(b)
    block_len = L // nblocks
    return [b[i*block_len:(i+1)*block_len] for i in range(nblocks)]

def bytes_to_signal(block: bytes, target_len: int = 256) -> np.ndarray:
    arr = np.frombuffer(block, dtype=np.uint8).astype(float)
    if arr.size < target_len:
        arr = np.pad(arr, (0, target_len - arr.size), mode="constant")
    else:
        arr = arr[:target_len]
    return arr

def detrend_and_center(sig: np.ndarray) -> np.ndarray:
    """Remove mean and linear trend, return float array."""
    sig = sig - np.mean(sig)
    return signal.detrend(sig, type="linear")

def popcount32(x: int) -> int:
    return bin(int(x) & 0xFFFFFFFF).count("1")

# -----------------------
# SHA compression rounds
# -----------------------
def rotr(x: int, n: int) -> int:
    return ((x >> n) | ((x << (32 - n)) & 0xFFFFFFFF)) & 0xFFFFFFFF

def sha256_compress_rounds(block_512: bytes, H_init: Optional[np.ndarray] = None, K_constants: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    assert len(block_512) == 64
    K = K_constants if K_constants is not None else STANDARD_K
    H0 = H_init if H_init is not None else STANDARD_H0
    w = np.zeros(64, dtype=np.uint32)
    for t in range(16):
        w[t] = int.from_bytes(block_512[t*4:(t+1)*4], "big")
    for t in range(16, 64):
        s0 = (rotr(w[t-15], 7) ^ rotr(w[t-15], 18) ^ (w[t-15] >> 3)) & 0xFFFFFFFF
        s1 = (rotr(w[t-2], 17) ^ rotr(w[t-2], 19) ^ (w[t-2] >> 10)) & 0xFFFFFFFF
        w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
    a,b,c,d,e,f,g,h = [int(x) for x in H0]
    states = np.zeros((64, 8), dtype=np.uint32)
    xor_acc = np.zeros(64, dtype=np.uint32)
    for t in range(64):
        S1 = (rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)) & 0xFFFFFFFF
        ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFF
        temp1 = (h + S1 + ch + int(K[t]) + int(w[t])) & 0xFFFFFFFF
        S0 = (rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)) & 0xFFFFFFFF
        maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFF
        temp2 = (S0 + maj) & 0xFFFFFFFF
        h = g; g = f; f = e; e = (d + temp1) & 0xFFFFFFFF
        d = c; c = b; b = a; a = (temp1 + temp2) & 0xFFFFFFFF
        states[t] = np.array([a,b,c,d,e,f,g,h], dtype=np.uint32)
        xor_acc[t] = a ^ b ^ c ^ d ^ e ^ f ^ g ^ h
    return states, xor_acc

# -----------------------
# SHA feature extractor
# -----------------------
def extract_sha_round_features(states: np.ndarray, xor_acc: np.ndarray, K_constants: np.ndarray, m: int = 64) -> Dict[str, np.ndarray]:
    rounds = int(states.shape[0])
    xor_bitcount = np.array([popcount32(int(x)) for x in xor_acc], dtype=int)
    mix_residue = np.zeros(rounds, dtype=int)
    mix_popcount = np.zeros(rounds, dtype=int)
    a_hamming = np.zeros(rounds, dtype=int)
    ch_popcount = np.zeros(rounds, dtype=int)
    maj_popcount = np.zeros(rounds, dtype=int)
    prev_a = int(states[0,0])
    for t in range(rounds):
        a = int(states[t,0]); b = int(states[t,1]); c = int(states[t,2])
        Kt = int(K_constants[t]) & 0xFFFFFFFF
        mix = (a ^ Kt) & 0xFFFFFFFF
        mix_residue[t] = int(mix % m)
        mix_popcount[t] = popcount32(mix)
        if t > 0:
            a_hamming[t] = popcount32(a ^ prev_a)
        prev_a = a
        ch = (a & b) ^ ((~a) & c)
        maj = (a & b) ^ (a & c) ^ (b & c)
        ch_popcount[t] = popcount32(ch)
        maj_popcount[t] = popcount32(maj)
    return {
        "xor_bitcount": xor_bitcount,
        "mix_residue": mix_residue,
        "mix_popcount": mix_popcount,
        "a_hamming": a_hamming,
        "ch_popcount": ch_popcount,
        "maj_popcount": maj_popcount
    }

# -----------------------
# Verb coordinates & spectral helpers
# -----------------------
def residues_and_phases(arr: Sequence[int], m: int) -> Tuple[np.ndarray, np.ndarray]:
    arr = np.asarray(arr, dtype=int)
    r = np.mod(arr, m)
    theta = 2.0 * np.pi * r.astype(float) / float(m)
    return r, theta

def sync_index_R(theta: np.ndarray) -> float:
    if theta.size == 0: return 0.0
    vec = np.exp(1j * theta); return float(np.abs(np.mean(vec)))

def mix_index_E(residues: np.ndarray, m: int) -> float:
    if residues.size == 0: return 0.0
    counts = np.bincount(residues.astype(int), minlength=m).astype(float)
    p = counts / counts.sum(); mask = p > 0
    ent = -np.sum(p[mask] * np.log(p[mask])); norm = np.log(m) if m>1 else 1.0
    return float(ent / norm)

def silr_scale_invariance(x: np.ndarray, window_sizes: Sequence[int], eps: float = 1e-12) -> float:
    x = np.asarray(x, dtype=float)
    if x.size == 0: return 0.0
    S_vals = []; N = x.size
    for w in window_sizes:
        if w < 4 or w > N: continue
        n_windows = max(1, N // w); s_list = []
        for i in range(n_windows):
            seg = x[i*w:(i+1)*w]; 
            if seg.size < 2: continue
            mu = seg.mean(); sigma = seg.std(ddof=0)
            z = (seg - mu) / (sigma + eps)
            S = z.std(ddof=0) / (abs(z.mean()) + eps); s_list.append(S)
        if s_list: S_vals.append(np.mean(s_list))
    if not S_vals: return 0.0
    S_vals = np.array(S_vals); mu = S_vals.mean(); sigma = S_vals.std(ddof=0)
    cv = sigma / (abs(mu) + eps); return float(max(0.0, 1.0 - cv))

def closure_rate_from_deltas(deltas: Sequence[int], M: int) -> float:
    if len(deltas) == 0: return 0.0
    cum = 0; hits = 0
    for d in deltas:
        cum = (cum + int(d)) % M
        if cum == 0: hits += 1
    return float(hits / len(deltas))

def compute_welch(sig: np.ndarray, nfft: int = NFFT, fs: float = FS, noverlap: int = NOVERLAP):
    f, Pxx = signal.welch(sig, fs=fs, window='hann', nperseg=nfft, noverlap=noverlap, nfft=nfft, return_onesided=True, scaling='density')
    return f, Pxx

def compute_psd_peak(sig: np.ndarray, nfft: int = NFFT, fs: float = FS, noverlap: int = NOVERLAP) -> Dict[str, Any]:
    f, Pxx = compute_welch(sig, nfft=nfft, fs=fs, noverlap=noverlap)
    nyq_bin = len(Pxx) - 1
    peak_idx = int(np.argmax(Pxx[:nyq_bin+1])); peak_power = float(Pxx[peak_idx])
    lo = max(0, peak_idx - 1); hi = min(nyq_bin, peak_idx + 1)
    mask = np.ones(nyq_bin + 1, dtype=bool); mask[lo:hi+1] = False
    bg = np.delete(Pxx[:nyq_bin+1], np.nonzero(~mask)[0])
    bg_median = float(np.median(bg)) if bg.size else float(np.median(Pxx))
    snr = float(peak_power / (bg_median + 1e-12))
    return {"f": f, "Pxx": Pxx, "peak_idx": peak_idx, "peak_power": peak_power, "bg_median": bg_median, "snr": snr, "peak_freq": float(f[peak_idx])}

def compute_csd_and_psd(x: np.ndarray, y: np.ndarray, nfft: int = NFFT, fs: float = FS):
    f_csd, Pxy = signal.csd(x, y, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    f_x, Pxx = signal.welch(x, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    f_y, Pyy = signal.welch(y, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    return f_csd, Pxy, Pxx, Pyy

def pairwise_coherence_phase(seqs: List[np.ndarray], peak_bins: List[int], nfft: int = NFFT, fs: float = FS):
    n = len(seqs); coh = np.zeros((n,n), dtype=float); phase = np.zeros((n,n), dtype=float)
    for i in range(n):
        for j in range(n):
            f, Pxy, Pxx_i, Pyy_j = compute_csd_and_psd(seqs[i], seqs[j], nfft=nfft, fs=fs)
            nyq = len(Pxy) - 1
            bin_idx = int(peak_bins[i]); bin_idx = max(0, min(bin_idx, nyq))
            num = np.abs(Pxy[bin_idx])**2; den = (Pxx_i[bin_idx] * Pyy_j[bin_idx]) + 1e-20
            coh[i,j] = float(np.clip(num / den, 0.0, 1.0)); phase[i,j] = float(np.angle(Pxy[bin_idx]))
    return coh, phase

def compute_bicoherence(x: np.ndarray, nfft: int = BICO_N) -> np.ndarray:
    if x.size >= nfft: x2 = x[:nfft]
    else: x2 = np.pad(x, (0, nfft - x.size), 'constant')
    X = fft(x2); half = nfft // 2; B = np.zeros((half, half), dtype=float)
    for f1 in range(half):
        for f2 in range(half):
            f3 = (f1 + f2) % nfft
            num = np.abs(X[f1] * X[f2] * np.conj(X[f3])); den = np.sqrt((np.abs(X[f1] * X[f2])**2) * (np.abs(X[f3])**2) + 1e-20)
            B[f1,f2] = float(num / (den + 1e-20))
    return B

def parity_and_autocorr(blocks: List[bytes]):
    n = len(blocks); blen = max(len(b) for b in blocks); parity = np.zeros((n, blen), dtype=int)
    for i,b in enumerate(blocks):
        arr = np.frombuffer(b, dtype=np.uint8); parity[i, :arr.size] = arr & 1
    lags = 31; autocorrs = np.zeros((n, 2*lags+1), dtype=float)
    for i in range(n):
        seq = parity[i].astype(float); ac_full = np.correlate(seq - seq.mean(), seq - seq.mean(), mode='full')
        denom = (np.var(seq) * seq.size + 1e-20); ac_norm = ac_full / denom
        center = len(ac_norm)//2; start = max(0, center - lags); end = start + 2*lags + 1
        if end <= len(ac_norm): autocorrs[i,:] = ac_norm[start:end]
        else:
            slice_vals = ac_norm[start:len(ac_norm)]; pad = 2*lags+1 - slice_vals.size
            autocorrs[i, :slice_vals.size] = slice_vals
            if pad > 0: autocorrs[i, slice_vals.size:] = 0.0
    crosscorr = np.corrcoef(parity.astype(float)); return parity, autocorrs, crosscorr

# -----------------------
# Main pipeline
# -----------------------
def run_pipeline():
    logger.info("Starting pipeline (detrend function present)")
    K_constants = CUSTOM_K if CUSTOM_K is not None else STANDARD_K
    H0_constants = CUSTOM_H0 if CUSTOM_H0 is not None else STANDARD_H0
    endian_variants = {"big": BYTES_BE, "rev4": rev4_bytes(BYTES_BE), "revall": revall_bytes(BYTES_BE)}
    chunkings = [4, 8, 16]
    results = {}

    def maybe_excite(base_bytes: bytes):
        if not ENABLE_EXCITATION: return base_bytes
        nb = bytearray(base_bytes)
        return bytes(excite_xor_steer(nb, key=0xA5, repeat=4))

    for name, base in endian_variants.items():
        excited = maybe_excite(base)
        for nblocks in chunkings:
            key = f"{name}_{nblocks}"
            logger.info("Analyze %s %d-blocks", name, nblocks)
            blocks = chunk_bytes(excited, nblocks)
            sigs = [detrend_and_center(bytes_to_signal(b, 256)) for b in blocks]
            psd_results = [compute_psd_peak(s, nfft=NFFT, fs=FS, noverlap=NOVERLAP) for s in sigs]
            peak_bins = [int(r["peak_idx"]) for r in psd_results]
            perm_pvals = [permutation_pvalue_peak(s, r["peak_power"], nperm=PERM_WITHIN, rng=RNG) for s, r in zip(sigs, psd_results)]
            coh_mat, phase_mat = pairwise_coherence_phase(sigs, peak_bins, nfft=NFFT, fs=FS)
            parity_mat, autocorrs, crosscorr = parity_and_autocorr(blocks)
            snrs = np.array([r["snr"] for r in psd_results]); top3 = np.argsort(-snrs)[:3]
            bico = {int(t): compute_bicoherence(sigs[t], nfft=BICO_N) for t in top3}
            block_512 = excited[:64] if len(excited) >= 64 else excited + bytes(64 - len(excited))
            states, xor_acc = sha256_compress_rounds(block_512, H_init=H0_constants, K_constants=K_constants)
            sha_features = extract_sha_round_features(states, xor_acc, K_constants, m=64)
            residues = sha_features["mix_residue"] % 6
            _, theta = residues_and_phases(residues, 6)
            R_full = sync_index_R(theta); E_full = mix_index_E(residues, 6)
            silr_global = silr_scale_invariance(sha_features["xor_bitcount"].astype(float), window_sizes=[8,16,32])
            deltas = np.diff(residues, prepend=residues[0]); closure = closure_rate_from_deltas(deltas, M=6)
            L = R_full * (1 - E_full) * silr_global; M_score = (1 - R_full) * E_full * silr_global
            T = np.sqrt(R_full * E_full); H = 0.35; B = 1 - abs(T - H) / max(H, 1 - H)
            df = pd.DataFrame([{
                "word": i,
                "peak_power": float(psd_results[i]["peak_power"]),
                "bg_median": float(psd_results[i]["bg_median"]),
                "snr": float(psd_results[i]["snr"]),
                "peak_bin": int(psd_results[i]["peak_idx"]),
                "peak_freq": float(psd_results[i]["peak_freq"]),
                "perm_pval": float(perm_pvals[i]),
                "snr_flag": float(psd_results[i]["snr"]) > 5,
                "pval_flag": float(perm_pvals[i]) < 0.001
            } for i in range(nblocks)])
            results[key] = {
                "df": df, "psd_results": psd_results, "sigs": sigs, "peak_bins": peak_bins,
                "perm_pvals": perm_pvals, "coherence": coh_mat, "phase": phase_mat,
                "parity": parity_mat, "autocorrs": autocorrs, "crosscorr": crosscorr,
                "bico": bico, "sha_features": sha_features, "R_full": R_full, "E_full": E_full,
                "silr_global": silr_global, "closure_rate": closure, "L": L, "M": M_score, "B": B
            }
            csv_path = os.path.join(OUT_DIR, f"summary_{key}.csv"); df.to_csv(csv_path, index=False); logger.info("Wrote %s", csv_path)

    # Surrogates (global shuffle)
    logger.info("Running surrogate baseline")
    surrogate_snr = np.zeros((SURROGATES, 8)); surrogate_coh = np.zeros((SURROGATES, 8, 8))
    for s in range(SURROGATES):
        perm_all = RNG.permutation(BYTES_BE); blocks = chunk_bytes(bytes(perm_all), 8)
        sigs = [detrend_and_center(bytes_to_signal(b, 256)) for b in blocks]
        for i, sig in enumerate(sigs):
            res = compute_psd_peak(sig, nfft=NFFT, fs=FS, noverlap=NOVERLAP)
            peak = res["peak_power"]; bg_med = float(np.median(res["Pxx"][:len(res["Pxx"])]))
            surrogate_snr[s, i] = peak / (bg_med + 1e-12)
        for i in range(8):
            for j in range(8):
                f, Pxy, Pxx_i, Pyy_j = compute_csd_and_psd(sigs[i], sigs[j], nfft=NFFT, fs=FS)
                bin_idx = 0 if len(Pxy) > 0 else 0
                surrogate_coh[s, i, j] = float(np.abs(Pxy[bin_idx])**2 / ((Pxx_i[bin_idx] * Pyy_j[bin_idx]) + 1e-20))
    logger.info("Surrogates done")

    # Save NPZ and combined figure (big_8 focus)
    npz_path = os.path.join(OUT_DIR, "uvd_sha_output.npz")
    npz_dict = {"surrogate_snr": surrogate_snr, "surrogate_coh_mean": surrogate_coh.mean(axis=0)}
    for k, v in results.items():
        npz_dict[f"{k}_csv"] = np.frombuffer(v["df"].to_csv(index=False).encode("utf-8"), dtype=np.uint8)
        npz_dict[f"{k}_coherence"] = v["coherence"]; npz_dict[f"{k}_phase"] = v["phase"]
    np.savez_compressed(npz_path, **npz_dict); logger.info("Wrote %s", npz_path)

    obs = results["big_8"]
    fig = plt.figure(figsize=(18,12)); gs = fig.add_gridspec(3,4,wspace=0.4,hspace=0.6)
    for i in range(8):
        ax = fig.add_subplot(gs[i//4, i%4]); r = obs["psd_results"][i]; ax.plot(r["f"], r["Pxx"], color="C0")
        peak_freq = r["f"][r["peak_idx"]]; ax.axvline(peak_freq, color="r", linestyle="--"); ax.set_xlim(0,0.5)
        ax.set_title(f"word {i} peak {peak_freq:.5f}")
    ax_coh = fig.add_subplot(gs[2,0]); sns.heatmap(obs["coherence"], vmin=0, vmax=1, cmap="viridis", ax=ax_coh); ax_coh.set_title("Coherence")
    ax_phase = fig.add_subplot(gs[2,1]); sns.heatmap(obs["phase"], center=0, cmap="RdBu_r", ax=ax_phase); ax_phase.set_title("Phase")
    ax_coords = fig.add_subplot(gs[2,2]); sha_feats = obs["sha_features"]; mix_res = sha_feats["mix_residue"] % 6
    centers = np.arange(len(mix_res))
    R_vals = [sync_index_R(np.exp(1j * 2*np.pi * mix_res[max(0,i-7):i+1] / 6)) for i in range(len(mix_res))]
    E_vals = [mix_index_E(mix_res[max(0,i-7):i+1], 6) for i in range(len(mix_res))]
    S_vals = [silr_scale_invariance(sha_feats["xor_bitcount"][max(0,i-15):i+1].astype(float), window_sizes=[4,8]) for i in range(len(mix_res))]
    ax_coords.plot(centers, R_vals, label="R"); ax_coords.plot(centers, E_vals, label="E"); ax_coords.plot(centers, S_vals, label="SILR")
    ax_coords.set_ylim(0,1.05); ax_coords.legend(); ax_coords.set_title("SHA-derived verb coords (rolling)")
    ax_par = fig.add_subplot(gs[2,3]); sns.heatmap(obs["autocorrs"], cmap="coolwarm", center=0, ax=ax_par); ax_par.set_title("Parity autocorr")
    plt.suptitle("UVD + SHA Integrated Summary (big_8)"); plt.tight_layout(rect=[0,0.03,1,0.95])
    figfile = os.path.join(OUT_DIR, "uvd_sha_summary.png"); fig.savefig(figfile, dpi=200); logger.info("Saved %s", figfile)

    # CSV summary
    rows = []
    for label in ["big","rev4","revall"]:
        key = f"{label}_8"; r = results[key]
        rows.append({"endian": label, "R_full": r["R_full"], "E_full": r["E_full"], "silr_global": r["silr_global"],
                     "closure_rate": r["closure_rate"], "L": r["L"], "M": r["M"], "B": r["B"], "peak_bins": ",".join(map(str, r["peak_bins"]))})
    summary_df = pd.DataFrame(rows); summary_csv = os.path.join(OUT_DIR, "uvd_sha_summary.csv"); summary_df.to_csv(summary_csv, index=False); logger.info("Wrote %s", summary_csv)

    logger.info("Pipeline complete"); return {"npz": npz_path, "png": figfile, "csv": summary_csv}

# -----------------------
# Entrypoint
# -----------------------
if __name__ == "__main__":
    out = run_pipeline()
    print("Generated files:")
    for v in out.values():
        print(" -", v)

```

    2026-01-11 18:20:35,188 INFO Starting pipeline (detrend function present)
    2026-01-11 18:20:35,189 INFO Analyze big 4-blocks
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[13], line 399
        395 # -----------------------
        396 # Entrypoint
        397 # -----------------------
        398 if __name__ == "__main__":
    --> 399     out = run_pipeline()
        400     print("Generated files:")
        401     for v in out.values():
    

    Cell In[13], line 306, in run_pipeline()
        304 psd_results = [compute_psd_peak(s, nfft=NFFT, fs=FS, noverlap=NOVERLAP) for s in sigs]
        305 peak_bins = [int(r["peak_idx"]) for r in psd_results]
    --> 306 perm_pvals = [permutation_pvalue_peak(s, r["peak_power"], nperm=PERM_WITHIN, rng=RNG) for s, r in zip(sigs, psd_results)]
        307 coh_mat, phase_mat = pairwise_coherence_phase(sigs, peak_bins, nfft=NFFT, fs=FS)
        308 parity_mat, autocorrs, crosscorr = parity_and_autocorr(blocks)
    

    NameError: name 'permutation_pvalue_peak' is not defined



```python
#!/usr/bin/env python3
"""
Universal Verb Detector - Integrated Pipeline with SHA Round Feature Extraction
Patched: includes permutation_pvalue_peak to avoid NameError.
Outputs: NPZ, CSV, combined PNG in ./uvd_sha_output
"""
from __future__ import annotations
import os, logging
from typing import List, Sequence, Tuple, Dict, Any, Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import signal
from numpy.fft import fft
import sys, traceback

def debug_shapes(name, *arrays):
    info = []
    for a in arrays:
        try:
            info.append(f"{getattr(a,'shape',None)}")
        except Exception as e:
            info.append(f"ERR:{e}")
    logger.info("DEBUG SHAPES %s: %s", name, ", ".join(info))

# Example usage before risky ops:
# debug_shapes("psd_results[0]", r["Pxx"])
# debug_shapes("Pxy", Pxy)
# debug_shapes("surrogate_coh", surrogate_coh)

# -----------------------
# CONFIG
# -----------------------
OUT_DIR = "uvd_sha_output"
os.makedirs(OUT_DIR, exist_ok=True)
SEED = 20260111
RNG = np.random.default_rng(SEED)
NFFT = 256
FS = 1.0
WINDOW = "hann"
NOVERLAP = 128
PERM_WITHIN = 2000
SURROGATES = 500
BICO_N = 128
ENABLE_EXCITATION = True

HEX_BYTES_BE = (
    "428a2f9871374491b5c0fbcfe9b5dba53956c25b59f111f1923f82a4ab1c5ed5"
    "d807aa9812835b01243185be550c7dc372be5d7480deb1fe9bdc06a7c19bf174"
    "e49b69c1efbe47860fc19dc6240ca1cc2de92c6f4a7484aa5cb0a9dc76f988da"
    "983e5152a831c66db00327c8bf597fc7c6e00bf3d5a7914706ca6351142929672"
    "7b70a852e1b21384d2c6dfc53380d13650a7354766a0abb81c2c92e92722c85a2"
    "bfe8a1a81a664bc24b8b70c76c51a3d192e819d6990624f40e3585106aa07019a"
    "4c1161e376c082748774c34b0bcb5391c0cb34ed8aa4a5b9cca4f682e6ff3748f"
    "82ee78a5636f84c878148cc7020890befffaa4506cebbef9a3f7c67178f2"
)
BYTES_BE = bytes.fromhex(HEX_BYTES_BE)

STANDARD_K = np.array([
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
], dtype=np.uint32)

STANDARD_H0 = np.array([
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
], dtype=np.uint32)

CUSTOM_K: Optional[np.ndarray] = None
CUSTOM_H0: Optional[np.ndarray] = None

# -----------------------
# Logging
# -----------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("uvd_sha")

# -----------------------
# Helpers (including permutation p-value)
# -----------------------
def rev4_bytes(b: bytes) -> bytes:
    out = bytearray()
    for i in range(0, len(b), 4):
        out.extend(b[i:i+4][::-1])
    return bytes(out)

def revall_bytes(b: bytes) -> bytes:
    return b[::-1]

def chunk_bytes(b: bytes, nblocks: int) -> List[bytes]:
    L = len(b)
    block_len = L // nblocks
    return [b[i*block_len:(i+1)*block_len] for i in range(nblocks)]

def bytes_to_signal(block: bytes, target_len: int = 256) -> np.ndarray:
    arr = np.frombuffer(block, dtype=np.uint8).astype(float)
    if arr.size < target_len:
        arr = np.pad(arr, (0, target_len - arr.size), mode="constant")
    else:
        arr = arr[:target_len]
    return arr

def detrend_and_center(sig: np.ndarray) -> np.ndarray:
    sig = sig - np.mean(sig)
    return signal.detrend(sig, type="linear")

def popcount32(x: int) -> int:
    return bin(int(x) & 0xFFFFFFFF).count("1")

def permutation_pvalue_peak(block_sig: np.ndarray, observed_peak: float, nperm: int = PERM_WITHIN, rng: np.random.Generator = RNG) -> float:
    """Empirical p-value by shuffling within-block (permutation test)."""
    count = 0
    arr = block_sig.copy()
    for _ in range(nperm):
        perm = rng.permutation(arr)
        f, Pxx = signal.welch(perm, fs=FS, window='hann', nperseg=NFFT, noverlap=0, nfft=NFFT, return_onesided=True)
        # safe nyquist
        nyq = len(Pxx) - 1
        peak = float(np.max(Pxx[:nyq+1]))
        if peak >= observed_peak:
            count += 1
    return (count + 1) / (nperm + 1)

# -----------------------
# SHA compression rounds
# -----------------------
def rotr(x: int, n: int) -> int:
    return ((x >> n) | ((x << (32 - n)) & 0xFFFFFFFF)) & 0xFFFFFFFF

def sha256_compress_rounds(block_512: bytes, H_init: Optional[np.ndarray] = None, K_constants: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
    assert len(block_512) == 64
    K = K_constants if K_constants is not None else STANDARD_K
    H0 = H_init if H_init is not None else STANDARD_H0
    w = np.zeros(64, dtype=np.uint32)
    for t in range(16):
        w[t] = int.from_bytes(block_512[t*4:(t+1)*4], "big")
    for t in range(16, 64):
        s0 = (rotr(w[t-15], 7) ^ rotr(w[t-15], 18) ^ (w[t-15] >> 3)) & 0xFFFFFFFF
        s1 = (rotr(w[t-2], 17) ^ rotr(w[t-2], 19) ^ (w[t-2] >> 10)) & 0xFFFFFFFF
        w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
    a,b,c,d,e,f,g,h = [int(x) for x in H0]
    states = np.zeros((64, 8), dtype=np.uint32)
    xor_acc = np.zeros(64, dtype=np.uint32)
    for t in range(64):
        S1 = (rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)) & 0xFFFFFFFF
        ch = ((e & f) ^ ((~e) & g)) & 0xFFFFFFFF
        temp1 = (h + S1 + ch + int(K[t]) + int(w[t])) & 0xFFFFFFFF
        S0 = (rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)) & 0xFFFFFFFF
        maj = ((a & b) ^ (a & c) ^ (b & c)) & 0xFFFFFFFF
        temp2 = (S0 + maj) & 0xFFFFFFFF
        h = g; g = f; f = e; e = (d + temp1) & 0xFFFFFFFF
        d = c; c = b; b = a; a = (temp1 + temp2) & 0xFFFFFFFF
        states[t] = np.array([a,b,c,d,e,f,g,h], dtype=np.uint32)
        xor_acc[t] = a ^ b ^ c ^ d ^ e ^ f ^ g ^ h
    return states, xor_acc

# -----------------------
# SHA feature extractor
# -----------------------
def extract_sha_round_features(states: np.ndarray, xor_acc: np.ndarray, K_constants: np.ndarray, m: int = 64) -> Dict[str, np.ndarray]:
    rounds = int(states.shape[0])
    xor_bitcount = np.array([popcount32(int(x)) for x in xor_acc], dtype=int)
    mix_residue = np.zeros(rounds, dtype=int)
    mix_popcount = np.zeros(rounds, dtype=int)
    a_hamming = np.zeros(rounds, dtype=int)
    ch_popcount = np.zeros(rounds, dtype=int)
    maj_popcount = np.zeros(rounds, dtype=int)
    prev_a = int(states[0,0])
    for t in range(rounds):
        a = int(states[t,0]); b = int(states[t,1]); c = int(states[t,2])
        Kt = int(K_constants[t]) & 0xFFFFFFFF
        mix = (a ^ Kt) & 0xFFFFFFFF
        mix_residue[t] = int(mix % m)
        mix_popcount[t] = popcount32(mix)
        if t > 0:
            a_hamming[t] = popcount32(a ^ prev_a)
        prev_a = a
        ch = (a & b) ^ ((~a) & c)
        maj = (a & b) ^ (a & c) ^ (b & c)
        ch_popcount[t] = popcount32(ch)
        maj_popcount[t] = popcount32(maj)
    return {
        "xor_bitcount": xor_bitcount,
        "mix_residue": mix_residue,
        "mix_popcount": mix_popcount,
        "a_hamming": a_hamming,
        "ch_popcount": ch_popcount,
        "maj_popcount": maj_popcount
    }

# -----------------------
# Verb coords & spectral helpers
# -----------------------
def residues_and_phases(arr: Sequence[int], m: int) -> Tuple[np.ndarray, np.ndarray]:
    arr = np.asarray(arr, dtype=int)
    r = np.mod(arr, m)
    theta = 2.0 * np.pi * r.astype(float) / float(m)
    return r, theta

def sync_index_R(theta: np.ndarray) -> float:
    if theta.size == 0: return 0.0
    vec = np.exp(1j * theta); return float(np.abs(np.mean(vec)))

def mix_index_E(residues: np.ndarray, m: int) -> float:
    if residues.size == 0: return 0.0
    counts = np.bincount(residues.astype(int), minlength=m).astype(float)
    p = counts / counts.sum(); mask = p > 0
    ent = -np.sum(p[mask] * np.log(p[mask])); norm = np.log(m) if m>1 else 1.0
    return float(ent / norm)

def silr_scale_invariance(x: np.ndarray, window_sizes: Sequence[int], eps: float = 1e-12) -> float:
    x = np.asarray(x, dtype=float)
    if x.size == 0: return 0.0
    S_vals = []; N = x.size
    for w in window_sizes:
        if w < 4 or w > N: continue
        n_windows = max(1, N // w); s_list = []
        for i in range(n_windows):
            seg = x[i*w:(i+1)*w]; 
            if seg.size < 2: continue
            mu = seg.mean(); sigma = seg.std(ddof=0)
            z = (seg - mu) / (sigma + eps)
            S = z.std(ddof=0) / (abs(z.mean()) + eps); s_list.append(S)
        if s_list: S_vals.append(np.mean(s_list))
    if not S_vals: return 0.0
    S_vals = np.array(S_vals); mu = S_vals.mean(); sigma = S_vals.std(ddof=0)
    cv = sigma / (abs(mu) + eps); return float(max(0.0, 1.0 - cv))

def closure_rate_from_deltas(deltas: Sequence[int], M: int) -> float:
    if len(deltas) == 0: return 0.0
    cum = 0; hits = 0
    for d in deltas:
        cum = (cum + int(d)) % M
        if cum == 0: hits += 1
    return float(hits / len(deltas))

def compute_welch(sig: np.ndarray, nfft: int = NFFT, fs: float = FS, noverlap: int = NOVERLAP):
    f, Pxx = signal.welch(sig, fs=fs, window='hann', nperseg=nfft, noverlap=noverlap, nfft=nfft, return_onesided=True, scaling='density')
    return f, Pxx

def compute_psd_peak(sig: np.ndarray, nfft: int = NFFT, fs: float = FS, noverlap: int = NOVERLAP) -> Dict[str, Any]:
    f, Pxx = compute_welch(sig, nfft=nfft, fs=fs, noverlap=noverlap)
    nyq_bin = len(Pxx) - 1
    peak_idx = int(np.argmax(Pxx[:nyq_bin+1])); peak_power = float(Pxx[peak_idx])
    lo = max(0, peak_idx - 1); hi = min(nyq_bin, peak_idx + 1)
    mask = np.ones(nyq_bin + 1, dtype=bool); mask[lo:hi+1] = False
    bg = np.delete(Pxx[:nyq_bin+1], np.nonzero(~mask)[0])
    bg_median = float(np.median(bg)) if bg.size else float(np.median(Pxx))
    snr = float(peak_power / (bg_median + 1e-12))
    return {"f": f, "Pxx": Pxx, "peak_idx": peak_idx, "peak_power": peak_power, "bg_median": bg_median, "snr": snr, "peak_freq": float(f[peak_idx])}

def compute_csd_and_psd(x: np.ndarray, y: np.ndarray, nfft: int = NFFT, fs: float = FS):
    f_csd, Pxy = signal.csd(x, y, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    f_x, Pxx = signal.welch(x, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    f_y, Pyy = signal.welch(y, fs=fs, window='hann', nperseg=nfft, noverlap=0, nfft=nfft)
    return f_csd, Pxy, Pxx, Pyy

def pairwise_coherence_phase(seqs: List[np.ndarray], peak_bins: List[int], nfft: int = NFFT, fs: float = FS):
    n = len(seqs); coh = np.zeros((n,n), dtype=float); phase = np.zeros((n,n), dtype=float)
    for i in range(n):
        for j in range(n):
            f, Pxy, Pxx_i, Pyy_j = compute_csd_and_psd(seqs[i], seqs[j], nfft=nfft, fs=fs)
            nyq = len(Pxy) - 1
            bin_idx = int(peak_bins[i]); bin_idx = max(0, min(bin_idx, nyq))
            num = np.abs(Pxy[bin_idx])**2; den = (Pxx_i[bin_idx] * Pyy_j[bin_idx]) + 1e-20
            coh[i,j] = float(np.clip(num / den, 0.0, 1.0)); phase[i,j] = float(np.angle(Pxy[bin_idx]))
    return coh, phase

def compute_bicoherence(x: np.ndarray, nfft: int = BICO_N) -> np.ndarray:
    if x.size >= nfft: x2 = x[:nfft]
    else: x2 = np.pad(x, (0, nfft - x.size), 'constant')
    X = fft(x2); half = nfft // 2; B = np.zeros((half, half), dtype=float)
    for f1 in range(half):
        for f2 in range(half):
            f3 = (f1 + f2) % nfft
            num = np.abs(X[f1] * X[f2] * np.conj(X[f3])); den = np.sqrt((np.abs(X[f1] * X[f2])**2) * (np.abs(X[f3])**2) + 1e-20)
            B[f1,f2] = float(num / (den + 1e-20))
    return B

def parity_and_autocorr(blocks: List[bytes]):
    n = len(blocks); blen = max(len(b) for b in blocks); parity = np.zeros((n, blen), dtype=int)
    for i,b in enumerate(blocks):
        arr = np.frombuffer(b, dtype=np.uint8); parity[i, :arr.size] = arr & 1
    lags = 31; autocorrs = np.zeros((n, 2*lags+1), dtype=float)
    for i in range(n):
        seq = parity[i].astype(float); ac_full = np.correlate(seq - seq.mean(), seq - seq.mean(), mode='full')
        denom = (np.var(seq) * seq.size + 1e-20); ac_norm = ac_full / denom
        center = len(ac_norm)//2; start = max(0, center - lags); end = start + 2*lags + 1
        if end <= len(ac_norm): autocorrs[i,:] = ac_norm[start:end]
        else:
            slice_vals = ac_norm[start:len(ac_norm)]; pad = 2*lags+1 - slice_vals.size
            autocorrs[i, :slice_vals.size] = slice_vals
            if pad > 0: autocorrs[i, slice_vals.size:] = 0.0
    crosscorr = np.corrcoef(parity.astype(float)); return parity, autocorrs, crosscorr

# -----------------------
# Main pipeline
# -----------------------
def run_pipeline():
    logger.info("Starting pipeline (permutation_pvalue_peak present)")
    K_constants = CUSTOM_K if CUSTOM_K is not None else STANDARD_K
    H0_constants = CUSTOM_H0 if CUSTOM_H0 is not None else STANDARD_H0
    endian_variants = {"big": BYTES_BE, "rev4": rev4_bytes(BYTES_BE), "revall": revall_bytes(BYTES_BE)}
    chunkings = [4, 8, 16]
    results = {}

    def maybe_excite(base_bytes: bytes):
        if not ENABLE_EXCITATION: return base_bytes
        nb = bytearray(base_bytes)
        return bytes(excite_xor_steer(nb, key=0xA5, repeat=4))

    for name, base in endian_variants.items():
        excited = maybe_excite(base)
        for nblocks in chunkings:
            key = f"{name}_{nblocks}"
            logger.info("Analyze %s %d-blocks", name, nblocks)
            blocks = chunk_bytes(excited, nblocks)
            sigs = [detrend_and_center(bytes_to_signal(b, 256)) for b in blocks]
            psd_results = [compute_psd_peak(s, nfft=NFFT, fs=FS, noverlap=NOVERLAP) for s in sigs]
            peak_bins = [int(r["peak_idx"]) for r in psd_results]
            perm_pvals = [permutation_pvalue_peak(s, r["peak_power"], nperm=PERM_WITHIN, rng=RNG) for s, r in zip(sigs, psd_results)]
            coh_mat, phase_mat = pairwise_coherence_phase(sigs, peak_bins, nfft=NFFT, fs=FS)
            parity_mat, autocorrs, crosscorr = parity_and_autocorr(blocks)
            snrs = np.array([r["snr"] for r in psd_results]); top3 = np.argsort(-snrs)[:3]
            bico = {int(t): compute_bicoherence(sigs[t], nfft=BICO_N) for t in top3}
            block_512 = excited[:64] if len(excited) >= 64 else excited + bytes(64 - len(excited))
            states, xor_acc = sha256_compress_rounds(block_512, H_init=H0_constants, K_constants=K_constants)
            sha_features = extract_sha_round_features(states, xor_acc, K_constants, m=64)
            residues = sha_features["mix_residue"] % 6
            _, theta = residues_and_phases(residues, 6)
            R_full = sync_index_R(theta); E_full = mix_index_E(residues, 6)
            silr_global = silr_scale_invariance(sha_features["xor_bitcount"].astype(float), window_sizes=[8,16,32])
            deltas = np.diff(residues, prepend=residues[0]); closure = closure_rate_from_deltas(deltas, M=6)
            L = R_full * (1 - E_full) * silr_global; M_score = (1 - R_full) * E_full * silr_global
            T = np.sqrt(R_full * E_full); H = 0.35; B = 1 - abs(T - H) / max(H, 1 - H)
            df = pd.DataFrame([{
                "word": i,
                "peak_power": float(psd_results[i]["peak_power"]),
                "bg_median": float(psd_results[i]["bg_median"]),
                "snr": float(psd_results[i]["snr"]),
                "peak_bin": int(psd_results[i]["peak_idx"]),
                "peak_freq": float(psd_results[i]["peak_freq"]),
                "perm_pval": float(perm_pvals[i]),
                "snr_flag": float(psd_results[i]["snr"]) > 5,
                "pval_flag": float(perm_pvals[i]) < 0.001
            } for i in range(nblocks)])
            results[key] = {
                "df": df, "psd_results": psd_results, "sigs": sigs, "peak_bins": peak_bins,
                "perm_pvals": perm_pvals, "coherence": coh_mat, "phase": phase_mat,
                "parity": parity_mat, "autocorrs": autocorrs, "crosscorr": crosscorr,
                "bico": bico, "sha_features": sha_features, "R_full": R_full, "E_full": E_full,
                "silr_global": silr_global, "closure_rate": closure, "L": L, "M": M_score, "B": B
            }
            csv_path = os.path.join(OUT_DIR, f"summary_{key}.csv"); df.to_csv(csv_path, index=False); logger.info("Wrote %s", csv_path)

    # Surrogates (global shuffle)
    logger.info("Running surrogate baseline")
    surrogate_snr = np.zeros((SURROGATES, 8)); surrogate_coh = np.zeros((SURROGATES, 8, 8))
    for s in range(SURROGATES):
        perm_all = RNG.permutation(BYTES_BE); blocks = chunk_bytes(bytes(perm_all), 8)
        sigs = [detrend_and_center(bytes_to_signal(b, 256)) for b in blocks]
        for i, sig in enumerate(sigs):
            res = compute_psd_peak(sig, nfft=NFFT, fs=FS, noverlap=NOVERLAP)
            peak = res["peak_power"]; bg_med = float(np.median(res["Pxx"][:len(res["Pxx"])]))
            surrogate_snr[s, i] = peak / (bg_med + 1e-12)
        for i in range(8):
            for j in range(8):
                f, Pxy, Pxx_i, Pyy_j = compute_csd_and_psd(sigs[i], sigs[j], nfft=NFFT, fs=FS)
                bin_idx = 0 if len(Pxy) > 0 else 0
                surrogate_coh[s, i, j] = float(np.abs(Pxy[bin_idx])**2 / ((Pxx_i[bin_idx] * Pyy_j[bin_idx]) + 1e-20))
    logger.info("Surrogates done")

    # Save NPZ and combined figure (big_8 focus)
    npz_path = os.path.join(OUT_DIR, "uvd_sha_output.npz")
    npz_dict = {"surrogate_snr": surrogate_snr, "surrogate_coh_mean": surrogate_coh.mean(axis=0)}
    for k, v in results.items():
        npz_dict[f"{k}_csv"] = np.frombuffer(v["df"].to_csv(index=False).encode("utf-8"), dtype=np.uint8)
        npz_dict[f"{k}_coherence"] = v["coherence"]; npz_dict[f"{k}_phase"] = v["phase"]
    np.savez_compressed(npz_path, **npz_dict); logger.info("Wrote %s", npz_path)

    obs = results["big_8"]
    fig = plt.figure(figsize=(18,12)); gs = fig.add_gridspec(3,4,wspace=0.4,hspace=0.6)
    for i in range(8):
        ax = fig.add_subplot(gs[i//4, i%4]); r = obs["psd_results"][i]; ax.plot(r["f"], r["Pxx"], color="C0")
        peak_freq = r["f"][r["peak_idx"]]; ax.axvline(peak_freq, color="r", linestyle="--"); ax.set_xlim(0,0.5)
        ax.set_title(f"word {i} peak {peak_freq:.5f}")
    ax_coh = fig.add_subplot(gs[2,0]); sns.heatmap(obs["coherence"], vmin=0, vmax=1, cmap="viridis", ax=ax_coh); ax_coh.set_title("Coherence")
    ax_phase = fig.add_subplot(gs[2,1]); sns.heatmap(obs["phase"], center=0, cmap="RdBu_r", ax=ax_phase); ax_phase.set_title("Phase")
    ax_coords = fig.add_subplot(gs[2,2]); sha_feats = obs["sha_features"]; mix_res = sha_feats["mix_residue"] % 6
    centers = np.arange(len(mix_res))
    R_vals = [sync_index_R(np.exp(1j * 2*np.pi * mix_res[max(0,i-7):i+1] / 6)) for i in range(len(mix_res))]
    E_vals = [mix_index_E(mix_res[max(0,i-7):i+1], 6) for i in range(len(mix_res))]
    S_vals = [silr_scale_invariance(sha_feats["xor_bitcount"][max(0,i-15):i+1].astype(float), window_sizes=[4,8]) for i in range(len(mix_res))]
    ax_coords.plot(centers, R_vals, label="R"); ax_coords.plot(centers, E_vals, label="E"); ax_coords.plot(centers, S_vals, label="SILR")
    ax_coords.set_ylim(0,1.05); ax_coords.legend(); ax_coords.set_title("SHA-derived verb coords (rolling)")
    ax_par = fig.add_subplot(gs[2,3]); sns.heatmap(obs["autocorrs"], cmap="coolwarm", center=0, ax=ax_par); ax_par.set_title("Parity autocorr")
    plt.suptitle("UVD + SHA Integrated Summary (big_8)"); plt.tight_layout(rect=[0,0.03,1,0.95])
    figfile = os.path.join(OUT_DIR, "uvd_sha_summary.png"); fig.savefig(figfile, dpi=200); logger.info("Saved %s", figfile)

    rows = []
    for label in ["big","rev4","revall"]:
        key = f"{label}_8"; r = results[key]
        rows.append({"endian": label, "R_full": r["R_full"], "E_full": r["E_full"], "silr_global": r["silr_global"],
                     "closure_rate": r["closure_rate"], "L": r["L"], "M": r["M"], "B": r["B"], "peak_bins": ",".join(map(str, r["peak_bins"]))})
    summary_df = pd.DataFrame(rows); summary_csv = os.path.join(OUT_DIR, "uvd_sha_summary.csv"); summary_df.to_csv(summary_csv, index=False); logger.info("Wrote %s", summary_csv)

    logger.info("Pipeline complete"); return {"npz": npz_path, "png": figfile, "csv": summary_csv}

if __name__ == "__main__":
    out = run_pipeline()
    print("Generated files:")
    for v in out.values():
        print(" -", v)

```

    2026-01-11 18:25:27,770 INFO Starting pipeline (permutation_pvalue_peak present)
    2026-01-11 18:25:27,770 INFO Analyze big 4-blocks
    C:\Users\Developer\AppData\Local\Temp\ipykernel_33544\3091619937.py:147: RuntimeWarning: overflow encountered in scalar add
      w[t] = (w[t-16] + s0 + w[t-7] + s1) & 0xFFFFFFFF
    2026-01-11 18:25:28,320 INFO Wrote uvd_sha_output\summary_big_4.csv
    2026-01-11 18:25:28,320 INFO Analyze big 8-blocks
    2026-01-11 18:25:29,389 INFO Wrote uvd_sha_output\summary_big_8.csv
    2026-01-11 18:25:29,390 INFO Analyze big 16-blocks
    2026-01-11 18:25:31,515 INFO Wrote uvd_sha_output\summary_big_16.csv
    2026-01-11 18:25:31,516 INFO Analyze rev4 4-blocks
    2026-01-11 18:25:32,067 INFO Wrote uvd_sha_output\summary_rev4_4.csv
    2026-01-11 18:25:32,068 INFO Analyze rev4 8-blocks
    2026-01-11 18:25:33,205 INFO Wrote uvd_sha_output\summary_rev4_8.csv
    2026-01-11 18:25:33,205 INFO Analyze rev4 16-blocks
    2026-01-11 18:25:35,629 INFO Wrote uvd_sha_output\summary_rev4_16.csv
    2026-01-11 18:25:35,630 INFO Analyze revall 4-blocks
    2026-01-11 18:25:36,283 INFO Wrote uvd_sha_output\summary_revall_4.csv
    2026-01-11 18:25:36,284 INFO Analyze revall 8-blocks
    2026-01-11 18:25:37,541 INFO Wrote uvd_sha_output\summary_revall_8.csv
    2026-01-11 18:25:37,541 INFO Analyze revall 16-blocks
    2026-01-11 18:25:39,981 INFO Wrote uvd_sha_output\summary_revall_16.csv
    2026-01-11 18:25:39,982 INFO Running surrogate baseline
    


    ---------------------------------------------------------------------------

    AxisError                                 Traceback (most recent call last)

    Cell In[15], line 417
        414     logger.info("Pipeline complete"); return {"npz": npz_path, "png": figfile, "csv": summary_csv}
        416 if __name__ == "__main__":
    --> 417     out = run_pipeline()
        418     print("Generated files:")
        419     for v in out.values():
    

    Cell In[15], line 367, in run_pipeline()
        365 surrogate_snr = np.zeros((SURROGATES, 8)); surrogate_coh = np.zeros((SURROGATES, 8, 8))
        366 for s in range(SURROGATES):
    --> 367     perm_all = RNG.permutation(BYTES_BE); blocks = chunk_bytes(bytes(perm_all), 8)
        368     sigs = [detrend_and_center(bytes_to_signal(b, 256)) for b in blocks]
        369     for i, sig in enumerate(sigs):
    

    File numpy/random/_generator.pyx:4971, in numpy.random._generator.Generator.permutation()
    

    AxisError: axis 0 is out of bounds for array of dimension 0



```python
# Nexus 10-Op ISA trace + GENLOCK baseline (single-cell, self-contained)
# - Calibrates mu/sigma from N_CAL single-block random messages (n = N_CAL*64 rounds)
# - Runs trace demos on BYTES / HEX / DNA payloads
# - Emits: ops, SILR z-score, p-gate, labels (COLD/EDDY/HOT), similarity, and VERIFY vs hashlib

import os, struct, hashlib, math, random
from collections import Counter

# ----------------------------
# Helpers
# ----------------------------
MASK32 = 0xFFFFFFFF

def rotr(x, n): return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32
def shr(x, n): return (x >> n) & MASK32

def popcount32(x): return int(x & MASK32).bit_count()
def popcount_bytes(b): return sum(byte.bit_count() for byte in b)

def hamming_words(words_a, words_b):
    # words are list/tuple of 32-bit ints
    return sum(popcount32(a ^ b) for a, b in zip(words_a, words_b))

def words_to_bytes(words):
    return b"".join(struct.pack(">I", w & MASK32) for w in words)

def sigmoid(x):
    # stable sigmoid
    if x >= 0:
        e = math.exp(-x)
        return 1.0 / (1.0 + e)
    else:
        e = math.exp(x)
        return e / (1.0 + e)

def dna_to_bytes(dna: str):
    # Pack 4 bases per byte, 2 bits each: A=0,C=1,G=2,T=3
    lut = {'A':0, 'C':1, 'G':2, 'T':3}
    dna = dna.strip().upper()
    if len(dna) % 4 != 0:
        raise ValueError("DNA length must be a multiple of 4 for 2-bit packing (e.g., 'ACGT' * k).")
    out = bytearray()
    for i in range(0, len(dna), 4):
        v = 0
        for j in range(4):
            v = (v << 2) | lut[dna[i+j]]
        out.append(v)
    return bytes(out)

# ----------------------------
# SHA-256 constants
# ----------------------------
K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

H0 = [
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]

def pad_sha256(msg: bytes):
    # Standard SHA-256 padding
    ml = len(msg) * 8
    out = bytearray(msg)
    out.append(0x80)
    while (len(out) % 64) != 56:
        out.append(0x00)
    out.extend(struct.pack(">Q", ml))
    return bytes(out)

def schedule_W(block64: bytes):
    W = list(struct.unpack(">16I", block64))
    for t in range(16, 64):
        s0 = rotr(W[t-15], 7) ^ rotr(W[t-15], 18) ^ shr(W[t-15], 3)
        s1 = rotr(W[t-2], 17) ^ rotr(W[t-2], 19) ^ shr(W[t-2], 10)
        W.append((W[t-16] + s0 + W[t-7] + s1) & MASK32)
    return W

# ----------------------------
# SILR / GENLOCK gate + labeling
# ----------------------------
# These values match your observed behavior closely:
# z0=1.0 and beta≈2.2 gives:
#   z=1.24 -> p≈0.63 (EDDY)
#   z=1.87 -> p≈0.87 (HOT)
#   z=0.15 -> p≈0.13 (COLD)
BETA = 2.2
Z0   = 1.0
P_COLD = 0.20
P_HOT  = 0.80

def label_from_p(p):
    if p >= P_HOT:
        return "HOT"
    if p < P_COLD:
        return "COLD"
    return "EDDY"

# ----------------------------
# Core compression with instrumentation
# ----------------------------
def sha256_trace_singleblock(msg: bytes, mu: float, sigma: float, do_verify=True):
    ops = []
    op_counts = Counter()
    per_round = []  # list of dicts: i, flips, z, p, sim, label

    # PROJECT: pad+frame
    op_counts["PROJECT"] += 1
    ops.append(("PROJECT", "pad+frame"))
    padded = pad_sha256(msg)

    # We only support single-block for this trace cell (fast + matches your baseline approach).
    if len(padded) != 64:
        raise ValueError(f"Trace cell expects single-block messages (<=55 bytes). Got padded length {len(padded)} bytes.")

    block = padded

    # PIN: init H0..H7
    op_counts["PIN"] += 1
    ops.append(("PIN", "init H0..H7"))
    H = H0[:]  # working chaining state

    # SYNC: block tick
    op_counts["SYNC"] += 1
    ops.append(("SYNC", "block tick"))

    # REFLECT: block density (measurable)
    density = popcount_bytes(block) / 512.0
    op_counts["REFLECT"] += 1
    ops.append(("REFLECT", f"block density={density:.4f}"))

    # FOLD: message schedule
    W = schedule_W(block)
    op_counts["FOLD"] += 1
    ops.append(("FOLD", "schedule W0..W63"))

    # PIN: load work regs
    op_counts["PIN"] += 1
    ops.append(("PIN", "load work regs"))
    a,b,c,d,e,f,g,h = H

    prev_after = None  # for similarity between successive after-states

    # 64 rounds
    for i in range(64):
        # GATE: round gates
        op_counts["GATE"] += 1
        ops.append(("GATE", f"round gates i={i:02d}"))

        # Save pre-state snapshot for flips (256 bits across 8 regs)
        pre = (a,b,c,d,e,f,g,h)

        S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (h + S1 + ch + K[i] + W[i]) & MASK32
        S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & MASK32

        # BRANCH: round update
        op_counts["BRANCH"] += 1
        h = g
        g = f
        f = e
        e = (d + temp1) & MASK32
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & MASK32

        post = (a,b,c,d,e,f,g,h)

        flips = hamming_words(pre, post)  # 0..256
        # GENLOCK z-score
        z = abs(flips - mu) / (sigma if sigma > 1e-9 else 1.0)
        p = sigmoid(BETA * (z - Z0))
        lab = label_from_p(p)

        # Similarity: 1 - normalized hamming to previous round's post-state
        if prev_after is None:
            sim = 0.0
        else:
            sim = 1.0 - (hamming_words(prev_after, post) / 256.0)
        prev_after = post

        per_round.append(dict(i=i, flips=flips, z=z, p=p, sim=sim, label=lab))
        ops.append(("BRANCH", f"round update | i={i:02d} {lab:<4} p={p:.2f} z={z:.2f} flips={flips:3d} sim={sim:.2f}"))

    # LEAK: chaining add
    op_counts["LEAK"] += 1
    ops.append(("LEAK", "chaining add (state carry)"))
    H = [
        (H[0] + a) & MASK32,
        (H[1] + b) & MASK32,
        (H[2] + c) & MASK32,
        (H[3] + d) & MASK32,
        (H[4] + e) & MASK32,
        (H[5] + f) & MASK32,
        (H[6] + g) & MASK32,
        (H[7] + h) & MASK32,
    ]

    # COLLAPSE: final digest
    op_counts["COLLAPSE"] += 1
    ops.append(("COLLAPSE", "final digest bytes"))
    digest = words_to_bytes(H).hex()

    # VERIFY
    ok = True
    if do_verify:
        ref = hashlib.sha256(msg).hexdigest()
        ok = (digest == ref)
        op_counts["VERIFY"] += 1
        ops.append(("VERIFY", "hashlib compare"))
    else:
        ref = None

    return {
        "ok": ok,
        "digest": digest,
        "ref": ref,
        "op_counts": dict(op_counts),
        "ops": ops,
        "per_round": per_round,
        "density": density
    }

# ----------------------------
# Baseline calibration (GENLOCK)
# ----------------------------
def calibrate_genlock(N_CAL=600, seed=0xC0FFEE):
    rng = random.Random(seed)
    flips_all = []
    # make single-block messages: length 0..55
    for _ in range(N_CAL):
        L = rng.randint(0, 55)
        msg = bytes(rng.getrandbits(8) for _ in range(L))
        # Run compression but only collect flips, without needing mu/sigma yet (use placeholders)
        # We'll compute flips directly by running the round loop here for speed/cleanliness.
        padded = pad_sha256(msg)
        block = padded  # single block by construction
        W = schedule_W(block)
        a,b,c,d,e,f,g,h = H0

        for i in range(64):
            pre = (a,b,c,d,e,f,g,h)
            S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[i] + W[i]) & MASK32
            S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & MASK32

            h = g
            g = f
            f = e
            e = (d + temp1) & MASK32
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & MASK32

            post = (a,b,c,d,e,f,g,h)
            flips_all.append(hamming_words(pre, post))

    n = len(flips_all)
    mu = sum(flips_all) / n
    var = sum((x - mu)**2 for x in flips_all) / (n - 1 if n > 1 else 1)
    sigma = math.sqrt(var)
    return n, mu, sigma

# ----------------------------
# Pretty reporting
# ----------------------------
def print_demo(title, msg_bytes, mu, sigma, show_asm_lines=16):
    print(f"\n=== {title} ===\n")
    res = sha256_trace_singleblock(msg_bytes, mu, sigma, do_verify=True)
    print(f"ok? {res['ok']}")
    print(f"digest: {res['digest']}\n")
    print(f"op counts: {res['op_counts']}\n")

    labels = Counter(r["label"] for r in res["per_round"])
    print(f"label counts (over 64 rounds): {dict(labels)}")

    for idx in [0, 1, 2, 3, 15, 31, 63]:
        r = res["per_round"][idx]
        print(f"  round {r['i']:02d}: flips={r['flips']:3d}  z={r['z']:.2f}  p={r['p']:.2f}  sim={r['sim']:.2f}  {r['label']}")

    print("\nassembly (truncated):\n")
    # print first few ops + then ellipsis
    asm_lines = []
    for op, desc in res["ops"]:
        if op == "BRANCH" or op == "GATE":
            asm_lines.append(f"{op:<9} {desc}")
        else:
            asm_lines.append(f"{op:<9} {desc}")
        if len(asm_lines) >= show_asm_lines:
            break
    print("\n".join(asm_lines))
    print("\n...\n")

    print("last 8 ops:", res["ops"][-8:])

# ----------------------------
# RUN
# ----------------------------
N_CAL = 600  # => n = 600*64 = 38400 rounds (matches your printout)
n, mu, sigma = calibrate_genlock(N_CAL=N_CAL, seed=0xC0FFEE)
print(f"GENLOCK baseline: n={n}  mu={mu:.3f}  sigma={sigma:.3f}")

# Demo 1: BYTES b'abc'
print_demo("BYTES: b'abc'", b"abc", mu, sigma)

# Demo 2: HEX '616263'
hex_payload = bytes.fromhex("616263")
print_demo("HEX: '616263'", hex_payload, mu, sigma)

# Demo 3: DNA 'ACGTACGTACGT' => 0x1b1b1b
dna = "ACGTACGTACGT"
dna_bytes = dna_to_bytes(dna)
print_demo(f"DNA: '{dna}'  (dna bytes: {dna_bytes.hex()})", dna_bytes, mu, sigma)

```

    GENLOCK baseline: n=38400  mu=127.894  sigma=8.039
    
    === BYTES: b'abc' ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    
    op counts: {'PROJECT': 1, 'PIN': 2, 'SYNC': 1, 'REFLECT': 1, 'FOLD': 1, 'GATE': 64, 'BRANCH': 64, 'LEAK': 1, 'COLLAPSE': 1, 'VERIFY': 1}
    
    label counts (over 64 rounds): {'EDDY': 44, 'HOT': 4, 'COLD': 16}
      round 00: flips=115  z=1.60  p=0.79  sim=0.00  EDDY
      round 01: flips=118  z=1.23  p=0.62  sim=0.54  EDDY
      round 02: flips=113  z=1.85  p=0.87  sim=0.56  HOT
      round 03: flips=115  z=1.60  p=0.79  sim=0.55  EDDY
      round 15: flips=129  z=0.14  p=0.13  sim=0.50  COLD
      round 31: flips=130  z=0.26  p=0.16  sim=0.49  COLD
      round 63: flips=118  z=1.23  p=0.62  sim=0.54  EDDY
    
    assembly (truncated):
    
    PROJECT   pad+frame
    PIN       init H0..H7
    SYNC      block tick
    REFLECT   block density=0.0254
    FOLD      schedule W0..W63
    PIN       load work regs
    GATE      round gates i=00
    BRANCH    round update | i=00 EDDY p=0.79 z=1.60 flips=115 sim=0.00
    GATE      round gates i=01
    BRANCH    round update | i=01 EDDY p=0.62 z=1.23 flips=118 sim=0.54
    GATE      round gates i=02
    BRANCH    round update | i=02 HOT  p=0.87 z=1.85 flips=113 sim=0.56
    GATE      round gates i=03
    BRANCH    round update | i=03 EDDY p=0.79 z=1.60 flips=115 sim=0.55
    GATE      round gates i=04
    BRANCH    round update | i=04 HOT  p=0.90 z=1.98 flips=112 sim=0.56
    
    ...
    
    last 8 ops: [('BRANCH', 'round update | i=61 EDDY p=0.56 z=1.11 flips=119 sim=0.54'), ('GATE', 'round gates i=62'), ('BRANCH', 'round update | i=62 EDDY p=0.56 z=1.11 flips=119 sim=0.54'), ('GATE', 'round gates i=63'), ('BRANCH', 'round update | i=63 EDDY p=0.62 z=1.23 flips=118 sim=0.54'), ('LEAK', 'chaining add (state carry)'), ('COLLAPSE', 'final digest bytes'), ('VERIFY', 'hashlib compare')]
    
    === HEX: '616263' ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    
    op counts: {'PROJECT': 1, 'PIN': 2, 'SYNC': 1, 'REFLECT': 1, 'FOLD': 1, 'GATE': 64, 'BRANCH': 64, 'LEAK': 1, 'COLLAPSE': 1, 'VERIFY': 1}
    
    label counts (over 64 rounds): {'EDDY': 44, 'HOT': 4, 'COLD': 16}
      round 00: flips=115  z=1.60  p=0.79  sim=0.00  EDDY
      round 01: flips=118  z=1.23  p=0.62  sim=0.54  EDDY
      round 02: flips=113  z=1.85  p=0.87  sim=0.56  HOT
      round 03: flips=115  z=1.60  p=0.79  sim=0.55  EDDY
      round 15: flips=129  z=0.14  p=0.13  sim=0.50  COLD
      round 31: flips=130  z=0.26  p=0.16  sim=0.49  COLD
      round 63: flips=118  z=1.23  p=0.62  sim=0.54  EDDY
    
    assembly (truncated):
    
    PROJECT   pad+frame
    PIN       init H0..H7
    SYNC      block tick
    REFLECT   block density=0.0254
    FOLD      schedule W0..W63
    PIN       load work regs
    GATE      round gates i=00
    BRANCH    round update | i=00 EDDY p=0.79 z=1.60 flips=115 sim=0.00
    GATE      round gates i=01
    BRANCH    round update | i=01 EDDY p=0.62 z=1.23 flips=118 sim=0.54
    GATE      round gates i=02
    BRANCH    round update | i=02 HOT  p=0.87 z=1.85 flips=113 sim=0.56
    GATE      round gates i=03
    BRANCH    round update | i=03 EDDY p=0.79 z=1.60 flips=115 sim=0.55
    GATE      round gates i=04
    BRANCH    round update | i=04 HOT  p=0.90 z=1.98 flips=112 sim=0.56
    
    ...
    
    last 8 ops: [('BRANCH', 'round update | i=61 EDDY p=0.56 z=1.11 flips=119 sim=0.54'), ('GATE', 'round gates i=62'), ('BRANCH', 'round update | i=62 EDDY p=0.56 z=1.11 flips=119 sim=0.54'), ('GATE', 'round gates i=63'), ('BRANCH', 'round update | i=63 EDDY p=0.62 z=1.23 flips=118 sim=0.54'), ('LEAK', 'chaining add (state carry)'), ('COLLAPSE', 'final digest bytes'), ('VERIFY', 'hashlib compare')]
    
    === DNA: 'ACGTACGTACGT'  (dna bytes: 1b1b1b) ===
    
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    
    op counts: {'PROJECT': 1, 'PIN': 2, 'SYNC': 1, 'REFLECT': 1, 'FOLD': 1, 'GATE': 64, 'BRANCH': 64, 'LEAK': 1, 'COLLAPSE': 1, 'VERIFY': 1}
    
    label counts (over 64 rounds): {'EDDY': 42, 'COLD': 19, 'HOT': 3}
      round 00: flips=119  z=1.11  p=0.56  sim=0.00  EDDY
      round 01: flips=135  z=0.88  p=0.44  sim=0.47  EDDY
      round 02: flips=128  z=0.01  p=0.10  sim=0.50  COLD
      round 03: flips=124  z=0.48  p=0.24  sim=0.52  EDDY
      round 15: flips=129  z=0.14  p=0.13  sim=0.50  COLD
      round 31: flips=130  z=0.26  p=0.16  sim=0.49  COLD
      round 63: flips=141  z=1.63  p=0.80  sim=0.45  HOT
    
    assembly (truncated):
    
    PROJECT   pad+frame
    PIN       init H0..H7
    SYNC      block tick
    REFLECT   block density=0.0293
    FOLD      schedule W0..W63
    PIN       load work regs
    GATE      round gates i=00
    BRANCH    round update | i=00 EDDY p=0.56 z=1.11 flips=119 sim=0.00
    GATE      round gates i=01
    BRANCH    round update | i=01 EDDY p=0.44 z=0.88 flips=135 sim=0.47
    GATE      round gates i=02
    BRANCH    round update | i=02 COLD p=0.10 z=0.01 flips=128 sim=0.50
    GATE      round gates i=03
    BRANCH    round update | i=03 EDDY p=0.24 z=0.48 flips=124 sim=0.52
    GATE      round gates i=04
    BRANCH    round update | i=04 EDDY p=0.30 z=0.61 flips=123 sim=0.52
    
    ...
    
    last 8 ops: [('BRANCH', 'round update | i=61 EDDY p=0.70 z=1.38 flips=139 sim=0.46'), ('GATE', 'round gates i=62'), ('BRANCH', 'round update | i=62 EDDY p=0.50 z=1.01 flips=136 sim=0.47'), ('GATE', 'round gates i=63'), ('BRANCH', 'round update | i=63 HOT  p=0.80 z=1.63 flips=141 sim=0.45'), ('LEAK', 'chaining add (state carry)'), ('COLLAPSE', 'final digest bytes'), ('VERIFY', 'hashlib compare')]
    


```python
# --- DROP-IN UPGRADE: multi-block + richer signatures (works with the previous cell's helpers/constants) ---

def sha256_trace(msg: bytes, mu: float, sigma: float, do_verify=True):
    ops_all = []
    op_counts = Counter()
    per_block = []
    padded = pad_sha256(msg)

    # init chaining
    H = H0[:]
    op_counts["PROJECT"] += 1
    ops_all.append(("PROJECT", "pad+frame (full message)"))

    # process blocks
    for bidx in range(0, len(padded), 64):
        block = padded[bidx:bidx+64]

        # PIN init/load
        op_counts["PIN"] += 1
        ops_all.append(("PIN", f"block {bidx//64}: load chaining H"))

        # SYNC
        op_counts["SYNC"] += 1
        ops_all.append(("SYNC", f"block {bidx//64}: block tick"))

        # REFLECT
        density = popcount_bytes(block) / 512.0
        op_counts["REFLECT"] += 1
        ops_all.append(("REFLECT", f"block {bidx//64}: density={density:.4f}"))

        # FOLD
        W = schedule_W(block)
        op_counts["FOLD"] += 1
        ops_all.append(("FOLD", f"block {bidx//64}: schedule W0..W63"))

        # working regs
        a,b,c,d,e,f,g,h = H
        init_regs = (a,b,c,d,e,f,g,h)

        prev_after = None
        prev_pre = None
        rounds = []

        for i in range(64):
            op_counts["GATE"] += 1
            ops_all.append(("GATE", f"block {bidx//64} round gates i={i:02d}"))

            pre = (a,b,c,d,e,f,g,h)

            S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[i] + W[i]) & MASK32
            S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & MASK32

            op_counts["BRANCH"] += 1
            h = g; g = f; f = e
            e = (d + temp1) & MASK32
            d = c; c = b; b = a
            a = (temp1 + temp2) & MASK32

            post = (a,b,c,d,e,f,g,h)

            flips = hamming_words(pre, post)
            z = abs(flips - mu) / (sigma if sigma > 1e-9 else 1.0)
            p = sigmoid(BETA * (z - Z0))
            lab = label_from_p(p)

            # similarity probes
            sim_prev_after = 0.0 if prev_after is None else 1.0 - (hamming_words(prev_after, post) / 256.0)
            sim_to_init    = 1.0 - (hamming_words(init_regs, post) / 256.0)
            sim_pre_flow   = 0.0 if prev_pre is None else 1.0 - (hamming_words(prev_pre, pre) / 256.0)

            prev_after = post
            prev_pre = pre

            rounds.append(dict(
                block=bidx//64, i=i, flips=flips, z=z, p=p, label=lab,
                sim=sim_prev_after, sim_init=sim_to_init, sim_pre=sim_pre_flow
            ))
            ops_all.append(("BRANCH", f"block {bidx//64} update | i={i:02d} {lab:<4} p={p:.2f} z={z:.2f} flips={flips:3d} sim={sim_prev_after:.2f} sim0={sim_to_init:.2f} pre={sim_pre_flow:.2f}"))

        # LEAK: chaining add
        op_counts["LEAK"] += 1
        ops_all.append(("LEAK", f"block {bidx//64}: chaining add"))
        H = [
            (H[0] + a) & MASK32,
            (H[1] + b) & MASK32,
            (H[2] + c) & MASK32,
            (H[3] + d) & MASK32,
            (H[4] + e) & MASK32,
            (H[5] + f) & MASK32,
            (H[6] + g) & MASK32,
            (H[7] + h) & MASK32,
        ]

        per_block.append(dict(block=bidx//64, density=density, rounds=rounds))

    # COLLAPSE
    op_counts["COLLAPSE"] += 1
    ops_all.append(("COLLAPSE", "final digest bytes"))
    digest = words_to_bytes(H).hex()

    # VERIFY
    ok = True
    ref = None
    if do_verify:
        ref = hashlib.sha256(msg).hexdigest()
        ok = (digest == ref)
        op_counts["VERIFY"] += 1
        ops_all.append(("VERIFY", "hashlib compare"))

    return {
        "ok": ok, "digest": digest, "ref": ref,
        "op_counts": dict(op_counts),
        "ops": ops_all,
        "per_block": per_block
    }

def summarize_trace(res):
    # flatten rounds
    rounds = [r for blk in res["per_block"] for r in blk["rounds"]]
    labels = Counter(r["label"] for r in rounds)
    n = len(rounds) if rounds else 1
    zs = sorted(r["z"] for r in rounds) if rounds else [0.0]
    sims = [r["sim"] for r in rounds] if rounds else [0.0]
    return {
        "blocks": len(res["per_block"]),
        "label_pct": {k: v/n for k,v in labels.items()},
        "z_mean": sum(zs)/len(zs),
        "z_95": zs[int(0.95*(len(zs)-1))],
        "sim_mean": sum(sims)/len(sims)
    }

def run_payload(name, msg_bytes, mu, sigma):
    print(f"\n=== {name} ===\n")
    res = sha256_trace(msg_bytes, mu, sigma, do_verify=True)
    summ = summarize_trace(res)
    print("ok?", res["ok"])
    print("digest:", res["digest"])
    print("blocks:", summ["blocks"])
    print("label%:", {k: round(v,3) for k,v in summ["label_pct"].items()})
    print("z_mean:", round(summ["z_mean"], 3), " z_95:", round(summ["z_95"], 3), " sim_mean:", round(summ["sim_mean"], 3))
    # last few ops
    print("\nlast 10 ops:")
    for op in res["ops"][-10:]:
        print(" ", op)
    return res, summ

# quick sanity demo
res_bytes, summ_bytes = run_payload("BYTES: b'abc'", b"abc", mu, sigma)
res_hex, summ_hex     = run_payload("HEX: 616263", bytes.fromhex("616263"), mu, sigma)
dna = "ACGTACGTACGT"
res_dna, summ_dna     = run_payload(f"DNA: {dna}", dna_to_bytes(dna), mu, sigma)

```

    
    === BYTES: b'abc' ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.688, 'HOT': 0.062, 'COLD': 0.25}
    z_mean: 0.785  z_95: 1.604  sim_mean: 0.498
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.30 z=0.61 flips=123 sim=0.52 sim0=0.53 pre=0.50')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.56 z=1.11 flips=119 sim=0.54 sim0=0.52 pre=0.52')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.56 z=1.11 flips=119 sim=0.54 sim0=0.50 pre=0.54')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.62 z=1.23 flips=118 sim=0.54 sim0=0.43 pre=0.54')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === HEX: 616263 ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.688, 'HOT': 0.062, 'COLD': 0.25}
    z_mean: 0.785  z_95: 1.604  sim_mean: 0.498
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.30 z=0.61 flips=123 sim=0.52 sim0=0.53 pre=0.50')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.56 z=1.11 flips=119 sim=0.54 sim0=0.52 pre=0.52')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.56 z=1.11 flips=119 sim=0.54 sim0=0.50 pre=0.54')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.62 z=1.23 flips=118 sim=0.54 sim0=0.43 pre=0.54')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === DNA: ACGTACGTACGT ===
    
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.656, 'COLD': 0.297, 'HOT': 0.047}
    z_mean: 0.723  z_95: 1.382  sim_mean: 0.488
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.70 z=1.38 flips=139 sim=0.46 sim0=0.52 pre=0.46')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.70 z=1.38 flips=139 sim=0.46 sim0=0.47 pre=0.46')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.50 z=1.01 flips=136 sim=0.47 sim0=0.49 pre=0.46')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 HOT  p=0.80 z=1.63 flips=141 sim=0.45 sim0=0.47 pre=0.47')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def compute_potential_on_circle(rho, L):
    """
    Solve ∇²Φ = ρ on a circle of length L with periodic BC.
    Using Fourier method: in k-space, Φ_k = -ρ_k / k² for k ≠ 0.
    For k=0, set Φ_0 = 0 (zero mean potential).
    """
    N = len(rho)
    dx = L / N
    x = np.linspace(0, L, N, endpoint=False)
    
    # Fourier transform
    rho_k = fft(rho)
    k = 2 * np.pi * np.fft.fftfreq(N, dx)
    
    # Avoid division by zero at k=0
    with np.errstate(divide='ignore', invalid='ignore'):
        Phi_k = -rho_k / (k**2)
        Phi_k[0] = 0  # Set zero mean
    
    # Inverse transform
    Phi = np.real(ifft(Phi_k))
    
    # Compute force field (negative gradient of Phi)
    F = -np.gradient(Phi, dx)
    
    return x, Phi, F

def test_particle_accelerations(x, F, kappa_iota_ratios):
    """
    Compute accelerations for test particles with different κ/ι ratios.
    """
    results = {}
    for ratio in kappa_iota_ratios:
        a = -ratio * F  # a = -(κ/ι) * ∇Φ
        results[ratio] = a
    return results

# Parameters
L = 2 * np.pi  # Circumference = 2π
N = 256
x = np.linspace(0, L, N, endpoint=False)

# Create a non-uniform deviation from SILR (simplest case: sinusoidal)
delta_theta = 0.5 * np.sin(2 * np.pi * x / L) + 0.2 * np.sin(4 * np.pi * x / L) + 0.1

# Mismatch charge density (always positive)
rho = delta_theta**2

# Solve for potential and force
x, Phi, F = compute_potential_on_circle(rho, L)

# Test particles with different κ/ι ratios
kappa_iota_ratios = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0]
accelerations = test_particle_accelerations(x, F, kappa_iota_ratios)

# Plot
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
axes = axes.flatten()

# Plot 1: Deviation from SILR
ax = axes[0]
ax.plot(x, delta_theta, 'b-', linewidth=2)
ax.set_xlabel('Position s')
ax.set_ylabel('δθ(s)')
ax.set_title('Deviation from SILR Baseline')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linestyle=':', alpha=0.5)

# Plot 2: Mismatch charge density
ax = axes[1]
ax.plot(x, rho, 'r-', linewidth=2)
ax.set_xlabel('Position s')
ax.set_ylabel('ρ(s)')
ax.set_title('Mismatch Charge Density')
ax.grid(True, alpha=0.3)

# Plot 3: Mismatch potential Φ
ax = axes[2]
ax.plot(x, Phi, 'g-', linewidth=2)
ax.set_xlabel('Position s')
ax.set_ylabel('Φ(s)')
ax.set_title('Mismatch Potential (Solution of ∇²Φ = ρ)')
ax.grid(True, alpha=0.3)

# Plot 4: Force field (-∇Φ)
ax = axes[3]
ax.plot(x, F, 'm-', linewidth=2)
ax.set_xlabel('Position s')
ax.set_ylabel('-∇Φ(s)')
ax.set_title('Force Field (Negative Gradient of Φ)')
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='k', linestyle=':', alpha=0.5)

# Plot 5: Accelerations for different κ/ι ratios
ax = axes[4]
for ratio, a in accelerations.items():
    ax.plot(x, a, label=f'κ/ι = {ratio}', alpha=0.7)
ax.set_xlabel('Position s')
ax.set_ylabel('a(s)')
ax.set_title('Acceleration for Different Test Particles')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8)
ax.axhline(y=0, color='k', linestyle=':', alpha=0.5)

# Plot 6: Equivalence principle check
ax = axes[5]
# Compute reference acceleration for κ/ι = 1
a_ref = accelerations[1.0]
for ratio, a in accelerations.items():
    if ratio != 1.0:
        relative_diff = np.abs(a - a_ref) / np.max(np.abs(a_ref))
        ax.plot(x, relative_diff, label=f'κ/ι = {ratio}', alpha=0.7)
ax.set_xlabel('Position s')
ax.set_ylabel('|a - a_ref|/|a_ref|')
ax.set_title('Violation of Equivalence Principle')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=8)
ax.set_yscale('log')

plt.suptitle('Static Mismatch Potential & Test Particle Accelerations on SILR-Pinned Ring', fontsize=14)
plt.tight_layout()
plt.show()

# Print key metrics
print("EQUIVALENCE PRINCIPLE TEST:")
print("=" * 50)
print("When κ/ι = 1.0, acceleration is independent of object properties.")
print("\nRoot-mean-square accelerations:")
for ratio, a in accelerations.items():
    rms_a = np.sqrt(np.mean(a**2))
    print(f"  κ/ι = {ratio:4.1f}: RMS acceleration = {rms_a:.6f}")

print("\nMaximum violation (relative to κ/ι=1.0):")
for ratio, a in accelerations.items():
    if ratio != 1.0:
        relative_diff = np.max(np.abs(a - accelerations[1.0])) / np.max(np.abs(accelerations[1.0]))
        print(f"  κ/ι = {ratio:4.1f}: max relative difference = {relative_diff:.6f}")

print("\n" + "=" * 50)
print("Key insight: When κ/ι ≠ 1, equivalence principle is violated.")
print("For SILR-stable structures, κ/ι ≈ 1 naturally.")
```

    C:\Users\Developer\AppData\Local\Temp\ipykernel_33544\3175618719.py:125: UserWarning: Glyph 8711 (\N{NABLA}) missing from font(s) Arial.
      plt.tight_layout()
    C:\Users\Developer\anaconda3\Lib\site-packages\IPython\core\pylabtools.py:170: UserWarning: Glyph 8711 (\N{NABLA}) missing from font(s) Arial.
      fig.canvas.print_figure(bytes_io, **kw)
    


    
![png](output_17_1.png)
    


    EQUIVALENCE PRINCIPLE TEST:
    ==================================================
    When κ/ι = 1.0, acceleration is independent of object properties.
    
    Root-mean-square accelerations:
      κ/ι =  0.5: RMS acceleration = 0.056384
      κ/ι =  0.8: RMS acceleration = 0.090214
      κ/ι =  1.0: RMS acceleration = 0.112767
      κ/ι =  1.2: RMS acceleration = 0.135321
      κ/ι =  1.5: RMS acceleration = 0.169151
      κ/ι =  2.0: RMS acceleration = 0.225534
    
    Maximum violation (relative to κ/ι=1.0):
      κ/ι =  0.5: max relative difference = 0.500000
      κ/ι =  0.8: max relative difference = 0.200000
      κ/ι =  1.2: max relative difference = 0.200000
      κ/ι =  1.5: max relative difference = 0.500000
      κ/ι =  2.0: max relative difference = 1.000000
    
    ==================================================
    Key insight: When κ/ι ≠ 1, equivalence principle is violated.
    For SILR-stable structures, κ/ι ≈ 1 naturally.
    


```python
# =========================
# NEXUS GENLOCK: "FIND IT EVERYWHERE" batch + signatures + similarity + plots
# =========================
import os, math, csv, random, hashlib
from collections import Counter, defaultdict

import numpy as np
import matplotlib.pyplot as plt

# ---- DNA encoders (keep your existing dna_to_bytes; add another option) ----
DNA_MAP_2BIT = {'A':0, 'C':1, 'G':2, 'T':3, 'a':0, 'c':1, 'g':2, 't':3}

def dna_to_bytes_2bit(seq: str) -> bytes:
    """Pack A/C/G/T into 2-bit symbols, 4 bases per byte. Drops non-ACGT."""
    bits = []
    for ch in seq:
        if ch in DNA_MAP_2BIT:
            bits.append(DNA_MAP_2BIT[ch])
    out = bytearray()
    acc = 0
    n = 0
    for v in bits:
        acc = (acc << 2) | v
        n += 1
        if n == 4:
            out.append(acc & 0xFF)
            acc = 0
            n = 0
    if n != 0:
        acc <<= (2 * (4 - n))
        out.append(acc & 0xFF)
    return bytes(out)

# ---- Universal payload builders ----
def as_bytes(payload, kind: str):
    kind = kind.lower()
    if kind == "bytes":
        if isinstance(payload, (bytes, bytearray)): return bytes(payload)
        if isinstance(payload, str): return payload.encode("utf-8")
        raise TypeError("bytes kind expects bytes/bytearray or str")
    if kind == "utf8":
        return str(payload).encode("utf-8")
    if kind == "hex":
        s = payload.strip().lower()
        if s.startswith("0x"): s = s[2:]
        return bytes.fromhex(s)
    if kind == "dna":
        # uses your existing dna_to_bytes (the 0x1b mapping)
        return dna_to_bytes(str(payload))
    if kind == "dna2bit":
        return dna_to_bytes_2bit(str(payload))
    raise ValueError(f"unknown kind: {kind}")

# ---- Flatten rounds for richer signatures ----
def flatten_rounds(res):
    return [r for blk in res["per_block"] for r in blk["rounds"]]

def signature_from_trace(res, summ, *, name=None, kind=None):
    rounds = flatten_rounds(res)
    n = len(rounds) if rounds else 1

    # label proportions
    lp = {k: 0.0 for k in ["EDDY","HOT","COLD"]}
    for k,v in summ["label_pct"].items():
        lp[k] = float(v)

    zs = np.array([r["z"] for r in rounds], dtype=float) if rounds else np.array([0.0])
    ps = np.array([r["p"] for r in rounds], dtype=float) if rounds else np.array([0.0])
    sim = np.array([r["sim"] for r in rounds], dtype=float) if rounds else np.array([0.0])
    sim0 = np.array([r.get("sim_init", 0.0) for r in rounds], dtype=float) if rounds else np.array([0.0])
    pre = np.array([r.get("sim_pre", 0.0) for r in rounds], dtype=float) if rounds else np.array([0.0])

    # “shape vector” — tweak freely, but keep it stable across domains
    vec = np.array([
        lp["EDDY"], lp["HOT"], lp["COLD"],
        float(zs.mean()), float(np.quantile(zs, 0.95)),
        float(ps.mean()), float(np.quantile(ps, 0.95)),
        float(sim.mean()), float(sim0.mean()), float(pre.mean()),
    ], dtype=float)

    # normalized vector for cosine similarity
    norm = float(np.linalg.norm(vec)) or 1.0
    vhat = vec / norm

    return {
        "name": name or "",
        "kind": kind or "",
        "blocks": summ.get("blocks", None),
        "digest": res.get("digest", ""),
        "ok": bool(res.get("ok", False)),
        "label_EDDY": lp["EDDY"],
        "label_HOT":  lp["HOT"],
        "label_COLD": lp["COLD"],
        "z_mean": float(zs.mean()),
        "z_95": float(np.quantile(zs, 0.95)),
        "p_mean": float(ps.mean()),
        "p_95": float(np.quantile(ps, 0.95)),
        "sim_mean": float(sim.mean()),
        "sim0_mean": float(sim0.mean()),
        "pre_mean": float(pre.mean()),
        "vec": vec,
        "vhat": vhat,
    }

def cosine(a, b):
    return float(np.dot(a, b))

# ---- Optional: calibrate mu/sigma for GENLOCK from random messages ----
def calibrate_genlock(n=38400, msg_len=64, seed=1):
    rng = random.Random(seed)
    flips = []
    # We only need flips distribution for one-round “state delta” proxy;
    # easiest: reuse sha256_trace but that’s heavier.
    # Instead: sample SHA-256 compression internal deltas if you already have a helper.
    #
    # If you don't, we'll do a cheap proxy: compare hash(state) across random blocks
    # (works surprisingly well as a baseline). You can replace this later with true internal flips.
    for _ in range(n):
        msg = bytes(rng.getrandbits(8) for _ in range(msg_len))
        h = hashlib.sha256(msg).digest()
        # flips vs a fixed reference digest (0s) -> popcount
        flips.append(int.from_bytes(h, "big").bit_count())
    mu = float(np.mean(flips))
    sigma = float(np.std(flips, ddof=0))
    return mu, sigma, n

# ---- Batch runner ----
def run_batch(items, mu, sigma, *, do_plots=True, save_csv_path=None, topk=12):
    """
    items: list of dicts like:
      {"name": "...", "kind": "bytes|hex|dna|dna2bit|utf8", "payload": ...}
    """
    results = []
    for it in items:
        msg = as_bytes(it["payload"], it["kind"])
        res = sha256_trace(msg, mu, sigma, do_verify=True)
        summ = summarize_trace(res)
        sig = signature_from_trace(res, summ, name=it["name"], kind=it["kind"])
        results.append((it, msg, res, summ, sig))

        print(f"\n=== {it['name']} ({it['kind']}) ===")
        print("ok?", res["ok"])
        print("digest:", res["digest"])
        print("blocks:", sig["blocks"])
        print("label%:", {"EDDY": round(sig["label_EDDY"],3), "HOT": round(sig["label_HOT"],3), "COLD": round(sig["label_COLD"],3)})
        print("z_mean:", round(sig["z_mean"],3), " z_95:", round(sig["z_95"],3),
              " sim_mean:", round(sig["sim_mean"],3), " sim0:", round(sig["sim0_mean"],3), " pre:", round(sig["pre_mean"],3))

    # similarity matrix on vhat
    names = [r[4]["name"] for r in results]
    V = np.stack([r[4]["vhat"] for r in results], axis=0)
    S = V @ V.T

    print("\n====================")
    print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
    print("====================")
    for i, name in enumerate(names):
        sims = [(names[j], float(S[i,j])) for j in range(len(names)) if j != i]
        sims.sort(key=lambda x: x[1], reverse=True)
        print(f"\n{name}:")
        for (n2, s) in sims[:min(topk, len(sims))]:
            print(f"  {n2:30s}  {s:.4f}")

    # optional CSV save (one row per payload)
    if save_csv_path:
        fieldnames = [k for k in results[0][4].keys() if k not in ("vec","vhat")]
        with open(save_csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            for (_,_,_,_,sig) in results:
                row = {k: sig[k] for k in fieldnames}
                w.writerow(row)
        print(f"\nSaved CSV: {save_csv_path}")

    # optional plots
    if do_plots:
        # bar plot of label proportions
        x = np.arange(len(names))
        ed = np.array([r[4]["label_EDDY"] for r in results])
        ho = np.array([r[4]["label_HOT"]  for r in results])
        co = np.array([r[4]["label_COLD"] for r in results])

        plt.figure()
        plt.bar(x - 0.25, ed, width=0.25, label="EDDY")
        plt.bar(x,         ho, width=0.25, label="HOT")
        plt.bar(x + 0.25,  co, width=0.25, label="COLD")
        plt.xticks(x, names, rotation=45, ha="right")
        plt.ylim(0, 1)
        plt.title("Label proportions (EDDY/HOT/COLD)")
        plt.legend()
        plt.tight_layout()
        plt.show()

        # z_mean plot
        plt.figure()
        plt.plot(x, np.array([r[4]["z_mean"] for r in results]), marker="o")
        plt.xticks(x, names, rotation=45, ha="right")
        plt.title("z_mean per payload")
        plt.tight_layout()
        plt.show()

        # z_95 plot
        plt.figure()
        plt.plot(x, np.array([r[4]["z_95"] for r in results]), marker="o")
        plt.xticks(x, names, rotation=45, ha="right")
        plt.title("z_95 per payload")
        plt.tight_layout()
        plt.show()

    return results, S, names

# =========================
# DEFAULT RUN (matches what you already tested)
# =========================

# If you already have mu/sigma in your notebook, keep them.
# Otherwise uncomment this:
# mu, sigma, _ = calibrate_genlock(n=38400, msg_len=64, seed=1)
print(f"GENLOCK baseline in-use: mu={mu:.3f} sigma={sigma:.3f}")

items = [
    {"name":"abc_bytes", "kind":"bytes", "payload": b"abc"},
    {"name":"abc_hex",   "kind":"hex",   "payload": "616263"},
    {"name":"dna_ascii_map", "kind":"dna", "payload": "ACGTACGTACGT"},
    {"name":"dna_2bit_packed", "kind":"dna2bit", "payload": "ACGTACGTACGT"},
    {"name":"utf8_sentence", "kind":"utf8", "payload": "the wall moves up to us"},
]

results, S, names = run_batch(items, mu, sigma, do_plots=True, save_csv_path=None, topk=10)

```

    GENLOCK baseline in-use: mu=127.894 sigma=8.039
    
    === abc_bytes (bytes) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.688, 'HOT': 0.062, 'COLD': 0.25}
    z_mean: 0.785  z_95: 1.815  sim_mean: 0.498  sim0: 0.494  pre: 0.498
    
    === abc_hex (hex) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.688, 'HOT': 0.062, 'COLD': 0.25}
    z_mean: 0.785  z_95: 1.815  sim_mean: 0.498  sim0: 0.494  pre: 0.498
    
    === dna_ascii_map (dna) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.656, 'HOT': 0.047, 'COLD': 0.297}
    z_mean: 0.723  z_95: 1.465  sim_mean: 0.488  sim0: 0.501  pre: 0.489
    
    === dna_2bit_packed (dna2bit) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.656, 'HOT': 0.047, 'COLD': 0.297}
    z_mean: 0.723  z_95: 1.465  sim_mean: 0.488  sim0: 0.501  pre: 0.489
    
    === utf8_sentence (utf8) ===
    ok? True
    digest: ea1b7f1ba0ee4b330ad4716aa87805368b37abb2b1974ed5cd0be755c99ea117
    blocks: 1
    label%: {'EDDY': 0.609, 'HOT': 0.172, 'COLD': 0.219}
    z_mean: 0.956  z_95: 2.248  sim_mean: 0.493  sim0: 0.498  pre: 0.494
    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex                         1.0000
      dna_ascii_map                   0.9960
      dna_2bit_packed                 0.9960
      utf8_sentence                   0.9942
    
    abc_hex:
      abc_bytes                       1.0000
      dna_ascii_map                   0.9960
      dna_2bit_packed                 0.9960
      utf8_sentence                   0.9942
    
    dna_ascii_map:
      dna_2bit_packed                 1.0000
      abc_bytes                       0.9960
      abc_hex                         0.9960
      utf8_sentence                   0.9827
    
    dna_2bit_packed:
      dna_ascii_map                   1.0000
      abc_bytes                       0.9960
      abc_hex                         0.9960
      utf8_sentence                   0.9827
    
    utf8_sentence:
      abc_bytes                       0.9942
      abc_hex                         0.9942
      dna_ascii_map                   0.9827
      dna_2bit_packed                 0.9827
    


    
![png](output_18_1.png)
    



    
![png](output_18_2.png)
    



    
![png](output_18_3.png)
    



```python
# Nexus SHA-256 Trace + GENLOCK + EDDY/HOT/COLD (single-cell)
import hashlib, math, random, statistics
from dataclasses import dataclass
from typing import List, Dict, Tuple, Any
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Bit utilities (32-bit)
# -----------------------------
MASK32 = 0xFFFFFFFF

def rotr(x, n): return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32
def shr(x, n): return (x >> n) & MASK32
def ch(x, y, z): return (x & y) ^ (~x & z)
def maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def bsig0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def bsig1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def ssig0(x): return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
def ssig1(x): return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def popcount32(x: int) -> int:
    return int(x & MASK32).bit_count()

def popcount256(words8: List[int]) -> int:
    # expects 8x32-bit words
    return sum(popcount32(w) for w in words8)

def hamming_words8(a8: List[int], b8: List[int]) -> int:
    return sum(popcount32((a8[i] ^ b8[i]) & MASK32) for i in range(8))

def sigmoid(x: float) -> float:
    # numerically safe
    if x >= 60: return 1.0
    if x <= -60: return 0.0
    return 1.0 / (1.0 + math.exp(-x))

def cosine_sim(v1: np.ndarray, v2: np.ndarray) -> float:
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    if n1 == 0 or n2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (n1 * n2))

# -----------------------------
# SHA-256 constants
# -----------------------------
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

H0_INIT = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

def sha256_pad(msg: bytes) -> bytes:
    ml = len(msg) * 8
    out = msg + b'\x80'
    while (len(out) % 64) != 56:
        out += b'\x00'
    out += ml.to_bytes(8, 'big')
    return out

def parse_block(block64: bytes) -> List[int]:
    return [int.from_bytes(block64[i:i+4], 'big') for i in range(0, 64, 4)]

# -----------------------------
# Trace structures
# -----------------------------
@dataclass
class RoundTrace:
    i: int
    flips: int
    z: float
    p: float
    label: str
    sim: float
    sim0: float
    pre: float

# -----------------------------
# GENLOCK + labeling
# -----------------------------
@dataclass
class GateParams:
    beta: float = 2.20
    z0: float = 0.80
    p_cold: float = 0.15
    p_hot: float = 0.85

def label_from_p(p: float, p_cold: float, p_hot: float) -> str:
    if p <= p_cold:
        return "COLD"
    if p >= p_hot:
        return "HOT"
    return "EDDY"

# -----------------------------
# SHA-256 with round trace
# flips = Hamming distance between (a..h) before and after each round (256-bit)
# sim  = cosine similarity of [p,z,flips_norm] vs previous round feature
# sim0 = cosine similarity vs round0 feature
# pre  = cosine similarity vs [0.5, 0.5, 0.5] anchor (your "pre" vibe)
# -----------------------------
def sha256_trace(msg: bytes, mu: float, sigma: float, gate: GateParams) -> Dict[str, Any]:
    padded = sha256_pad(msg)
    blocks = [padded[i:i+64] for i in range(0, len(padded), 64)]

    H = H0_INIT.copy()
    ops = []
    ops.append(("PROJECT", "pad+frame"))
    ops.append(("PIN", "init H0..H7"))
    ops.append(("SYNC", "block tick"))

    all_rounds: List[RoundTrace] = []
    labels_count = {"EDDY": 0, "HOT": 0, "COLD": 0}

    for bidx, blk in enumerate(blocks):
        W = [0]*64
        M = parse_block(blk)

        # quick "density" (byte-level) just for REFLECT logging
        density = sum(bin(x).count("1") for x in blk) / (len(blk)*8)
        ops.append(("REFLECT", f"block density={density:.4f}"))

        for t in range(16):
            W[t] = M[t]
        for t in range(16, 64):
            W[t] = (ssig1(W[t-2]) + W[t-7] + ssig0(W[t-15]) + W[t-16]) & MASK32

        ops.append(("FOLD", "schedule W0..W63"))
        ops.append(("PIN", "load work regs"))

        a,b,c,d,e,f,g,h = H

        # feature anchors
        round0_feat = None
        prev_feat = None
        anchor = np.array([0.5, 0.5, 0.5], dtype=float)

        for i in range(64):
            ops.append(("GATE", f"block {bidx} round gates i={i:02d}"))

            pre_state = [a,b,c,d,e,f,g,h]

            t1 = (h + bsig1(e) + ch(e,f,g) + K[i] + W[i]) & MASK32
            t2 = (bsig0(a) + maj(a,b,c)) & MASK32

            h = g
            g = f
            f = e
            e = (d + t1) & MASK32
            d = c
            c = b
            b = a
            a = (t1 + t2) & MASK32

            post_state = [a,b,c,d,e,f,g,h]

            flips = hamming_words8(pre_state, post_state)
            z = abs(flips - mu) / (sigma if sigma > 1e-9 else 1.0)
            p = sigmoid(gate.beta * (z - gate.z0))
            label = label_from_p(p, gate.p_cold, gate.p_hot)
            labels_count[label] += 1

            # feature vector for similarity
            flips_norm = 1.0 / (1.0 + math.exp(-(flips - mu) / (sigma if sigma > 1e-9 else 1.0)))
            feat = np.array([p, z / 3.0, flips_norm], dtype=float)  # keep ranges tame

            if round0_feat is None:
                round0_feat = feat.copy()
                sim = 0.0
                sim0 = 0.0
            else:
                sim = cosine_sim(feat, prev_feat) if prev_feat is not None else 0.0
                sim0 = cosine_sim(feat, round0_feat)

            pre = cosine_sim(feat, anchor)
            prev_feat = feat

            all_rounds.append(RoundTrace(i=i, flips=flips, z=z, p=p, label=label, sim=sim, sim0=sim0, pre=pre))
            ops.append(("BRANCH", f"block {bidx} update | i={i:02d} {label} p={p:.2f} z={z:.2f} flips={flips} sim={sim:.2f} sim0={sim0:.2f} pre={pre:.2f}"))

        # chaining add
        H = [(H[j] + v) & MASK32 for j,v in enumerate([a,b,c,d,e,f,g,h])]
        ops.append(("LEAK", f"block {bidx}: chaining add"))

    digest_bytes = b"".join(x.to_bytes(4, "big") for x in H)
    digest_hex = digest_bytes.hex()
    ops.append(("COLLAPSE", "final digest bytes"))

    # verify
    ref = hashlib.sha256(msg).hexdigest()
    ok = (ref == digest_hex)
    if ok:
        ops.append(("VERIFY", "hashlib compare"))

    # summary stats
    z_vals = [rt.z for rt in all_rounds]
    sim_vals = [rt.sim for rt in all_rounds]
    label_pct = {k: labels_count[k] / (len(all_rounds) if all_rounds else 1) for k in labels_count}
    z_mean = float(np.mean(z_vals)) if z_vals else 0.0
    z_95 = float(np.quantile(z_vals, 0.95)) if z_vals else 0.0
    sim_mean = float(np.mean(sim_vals)) if sim_vals else 0.0
    sim0_mean = float(np.mean([rt.sim0 for rt in all_rounds])) if all_rounds else 0.0
    pre_mean = float(np.mean([rt.pre for rt in all_rounds])) if all_rounds else 0.0

    return {
        "ok": ok,
        "digest": digest_hex,
        "blocks": len(blocks),
        "ops": ops,
        "rounds": all_rounds,
        "label_pct": label_pct,
        "z_mean": z_mean,
        "z_95": z_95,
        "sim_mean": sim_mean,
        "sim0": sim0_mean,
        "pre": pre_mean,
    }

# -----------------------------
# GENLOCK calibration:
# compute mu/sigma of flips across random messages and all 64 rounds
# -----------------------------
def calibrate_genlock(n_samples: int = 600, min_len: int = 1, max_len: int = 128, seed: int = 0) -> Tuple[float, float, int]:
    rng = random.Random(seed)
    flips_all = []

    # We need flips without using mu/sigma; do a "raw" run with dummy mu/sigma
    gate = GateParams()
    dummy_mu, dummy_sigma = 0.0, 1.0

    for _ in range(n_samples):
        L = rng.randint(min_len, max_len)
        msg = bytes(rng.getrandbits(8) for _ in range(L))
        t = sha256_trace(msg, dummy_mu, dummy_sigma, gate)  # flips are independent of mu/sigma
        flips_all.extend([rt.flips for rt in t["rounds"]])

    mu = float(np.mean(flips_all))
    sigma = float(np.std(flips_all, ddof=0))
    return mu, sigma, len(flips_all)

# -----------------------------
# Payload encoders
# -----------------------------
def bytes_payload(b: bytes) -> bytes:
    return b

def hex_payload(hx: str) -> bytes:
    hx = hx.strip().lower()
    if hx.startswith("0x"): hx = hx[2:]
    return bytes.fromhex(hx)

def dna_2bit_pack(dna: str) -> bytes:
    # A=00, C=01, G=10, T=11; pack 4 bases per byte
    m = {'A':0,'C':1,'G':2,'T':3,'a':0,'c':1,'g':2,'t':3}
    vals = [m[ch] for ch in dna if ch in m]
    out = bytearray()
    for i in range(0, len(vals), 4):
        chunk = vals[i:i+4]
        while len(chunk) < 4:
            chunk.append(0)
        b = (chunk[0]<<6) | (chunk[1]<<4) | (chunk[2]<<2) | (chunk[3])
        out.append(b & 0xFF)
    return bytes(out)

def utf8_payload(s: str) -> bytes:
    return s.encode("utf-8")

# -----------------------------
# Run suite + charts + similarity
# -----------------------------
gate = GateParams(beta=2.20, z0=0.80, p_cold=0.15, p_hot=0.85)

mu, sigma, n = calibrate_genlock(n_samples=600, min_len=1, max_len=128, seed=0)
print(f"GENLOCK baseline in-use: mu={mu:.3f} sigma={sigma:.3f}  (n={n})\n")

suite = [
    ("abc_bytes", "bytes", bytes_payload(b"abc")),
    ("abc_hex", "hex", hex_payload("616263")),
    ("dna_ascii_map", "dna", dna_2bit_pack("ACGTACGTACGT")),   # keep same packed bytes
    ("dna_2bit_packed", "dna2bit", dna_2bit_pack("ACGTACGTACGT")),
    ("utf8_sentence", "utf8", utf8_payload("Dean's Nexus: eddies fold the stream into trust.")),
]

results = {}
sig_vectors = {}

for name, kind, payload in suite:
    t = sha256_trace(payload, mu, sigma, gate)
    results[name] = t

    print(f"=== {name} ({kind}) ===\n")
    print(f"ok? {t['ok']}")
    print(f"digest: {t['digest']}")
    print(f"blocks: {t['blocks']}")
    lp = {k: round(v, 3) for k,v in t["label_pct"].items()}
    print(f"label%: {lp}")
    print(f"z_mean: {t['z_mean']:.3f}  z_95: {t['z_95']:.3f}  sim_mean: {t['sim_mean']:.3f}  sim0: {t['sim0']:.3f}  pre: {t['pre']:.3f}\n")

    # show last 10 ops
    print("last 10 ops:\n")
    for op in t["ops"][-10:]:
        print(f"  {op}")
    print("\n")

    # signature vector for cross-domain similarity
    v = np.array([
        t["label_pct"]["EDDY"],
        t["label_pct"]["HOT"],
        t["label_pct"]["COLD"],
        t["z_mean"],
        t["z_95"],
        t["sim_mean"],
    ], dtype=float)
    sig_vectors[name] = v

# -----------------------------
# Charts
# -----------------------------
names = [x[0] for x in suite]
eddy = [results[n]["label_pct"]["EDDY"] for n in names]
hot  = [results[n]["label_pct"]["HOT"]  for n in names]
cold = [results[n]["label_pct"]["COLD"] for n in names]
zmean = [results[n]["z_mean"] for n in names]
z95   = [results[n]["z_95"] for n in names]

x = np.arange(len(names))
w = 0.25

plt.figure(figsize=(10,4))
plt.title("Label proportions (EDDY/HOT/COLD)")
plt.bar(x - w, eddy, width=w, label="EDDY")
plt.bar(x,     hot,  width=w, label="HOT")
plt.bar(x + w, cold, width=w, label="COLD")
plt.xticks(x, names, rotation=35, ha="right")
plt.ylim(0, 1.0)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.title("z_mean per payload")
plt.plot(names, zmean, marker="o")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,4))
plt.title("z_95 per payload")
plt.plot(names, z95, marker="o")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()

# -----------------------------
# Cross-domain similarity
# -----------------------------
print("\n====================")
print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
print("====================\n")

for a in names:
    sims = []
    for b in names:
        if a == b: 
            continue
        sims.append((b, cosine_sim(sig_vectors[a], sig_vectors[b])))
    sims.sort(key=lambda x: x[1], reverse=True)
    print(f"{a}:")
    for b, s in sims:
        print(f"  {b:<30} {s:.4f}")
    print()

```

    GENLOCK baseline in-use: mu=127.942 sigma=8.024  (n=64256)
    
    === abc_bytes (bytes) ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.875, 'HOT': 0.094, 'COLD': 0.031}
    z_mean: 0.787  z_95: 1.825  sim_mean: 0.917  sim0: 0.769  pre: 0.905
    
    last 10 ops:
    
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.40 z=0.62 flips=123 sim=0.85 sim0=0.87 pre=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.67 z=1.11 flips=119 sim=0.94 sim0=0.99 pre=0.93')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.67 z=1.11 flips=119 sim=1.00 sim0=0.99 pre=0.93')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.72 z=1.24 flips=118 sim=1.00 sim0=0.99 pre=0.91')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === abc_hex (hex) ===
    
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.875, 'HOT': 0.094, 'COLD': 0.031}
    z_mean: 0.787  z_95: 1.825  sim_mean: 0.917  sim0: 0.769  pre: 0.905
    
    last 10 ops:
    
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.40 z=0.62 flips=123 sim=0.85 sim0=0.87 pre=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.67 z=1.11 flips=119 sim=0.94 sim0=0.99 pre=0.93')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.67 z=1.11 flips=119 sim=1.00 sim0=0.99 pre=0.93')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.72 z=1.24 flips=118 sim=1.00 sim0=0.99 pre=0.91')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === dna_ascii_map (dna) ===
    
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.859, 'HOT': 0.047, 'COLD': 0.094}
    z_mean: 0.724  z_95: 1.472  sim_mean: 0.929  sim0: 0.804  pre: 0.899
    
    last 10 ops:
    
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.78 z=1.38 flips=139 sim=1.00 sim0=0.92 pre=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.78 z=1.38 flips=139 sim=1.00 sim0=0.92 pre=0.97')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.61 z=1.00 flips=136 sim=1.00 sim0=0.88 pre=0.96')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 HOT p=0.86 z=1.63 flips=141 sim=0.99 sim0=0.93 pre=0.98')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === dna_2bit_packed (dna2bit) ===
    
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.859, 'HOT': 0.047, 'COLD': 0.094}
    z_mean: 0.724  z_95: 1.472  sim_mean: 0.929  sim0: 0.804  pre: 0.899
    
    last 10 ops:
    
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.78 z=1.38 flips=139 sim=1.00 sim0=0.92 pre=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.78 z=1.38 flips=139 sim=1.00 sim0=0.92 pre=0.97')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.61 z=1.00 flips=136 sim=1.00 sim0=0.88 pre=0.96')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 HOT p=0.86 z=1.63 flips=141 sim=0.99 sim0=0.93 pre=0.98')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === utf8_sentence (utf8) ===
    
    ok? True
    digest: 2210c0a0a7d09400c359b5eb77eb975fba7eacc73f79650f4134c22c1947bb08
    blocks: 1
    label%: {'EDDY': 0.828, 'HOT': 0.109, 'COLD': 0.062}
    z_mean: 0.879  z_95: 1.931  sim_mean: 0.897  sim0: 0.804  pre: 0.892
    
    last 10 ops:
    
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.40 z=0.62 flips=123 sim=0.98 sim0=0.87 pre=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.78 z=1.36 flips=117 sim=0.90 sim0=1.00 pre=0.90')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 HOT p=0.96 z=2.24 flips=110 sim=0.98 sim0=0.99 pre=0.85')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 HOT p=0.93 z=1.99 flips=112 sim=1.00 sim0=1.00 pre=0.86')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    


    
![png](output_19_1.png)
    



    
![png](output_19_2.png)
    



    
![png](output_19_3.png)
    


    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex                        1.0000
      utf8_sentence                  0.9987
      dna_ascii_map                  0.9945
      dna_2bit_packed                0.9945
    
    abc_hex:
      abc_bytes                      1.0000
      utf8_sentence                  0.9987
      dna_ascii_map                  0.9945
      dna_2bit_packed                0.9945
    
    dna_ascii_map:
      dna_2bit_packed                1.0000
      abc_bytes                      0.9945
      abc_hex                        0.9945
      utf8_sentence                  0.9902
    
    dna_2bit_packed:
      dna_ascii_map                  1.0000
      abc_bytes                      0.9945
      abc_hex                        0.9945
      utf8_sentence                  0.9902
    
    utf8_sentence:
      abc_bytes                      0.9987
      abc_hex                        0.9987
      dna_ascii_map                  0.9902
      dna_2bit_packed                0.9902
    
    


```python
# --- Nexus 10-op SHA256 tracer (single-cell) ---
import hashlib, math, random, struct, statistics
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# GENLOCK baseline (flip count)
# -------------------------------
def genlock_baseline(n: int = 64256, bits: int = 256, seed: int = 1234):
    rng = random.Random(seed)
    flips = []
    for _ in range(n):
        a = rng.getrandbits(bits)
        b = rng.getrandbits(bits)
        flips.append((a ^ b).bit_count())
    mu = float(statistics.fmean(flips))
    sigma = float(statistics.pstdev(flips))  # population sigma
    return {"n": n, "mu": mu, "sigma": sigma}

BASE = genlock_baseline(n=64256, bits=256, seed=1234)
MU, SIG = BASE["mu"], BASE["sigma"]
print(f"GENLOCK baseline in-use: mu={MU:.3f} sigma={SIG:.3f} (n={BASE['n']})")

# -------------------------------
# Helpers
# -------------------------------
def rotr(x, n): return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF
def shr(x, n): return (x >> n) & 0xFFFFFFFF

def Ch(x, y, z): return (x & y) ^ (~x & z)
def Maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)

def Sig0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sig1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sig0(x): return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
def sig1(x): return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

K = [
  0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
  0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
  0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
  0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
  0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
  0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
  0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
  0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

H0 = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

def pad_sha256(msg: bytes) -> bytes:
    ml = len(msg) * 8
    out = msg + b"\x80"
    while (len(out) % 64) != 56:
        out += b"\x00"
    out += struct.pack(">Q", ml)
    return out

def block_density(block64: bytes) -> float:
    # fraction of 1-bits in a 512-bit block
    ones = sum(b.bit_count() for b in block64)
    return ones / 512.0

def state_pack_256(a,b,c,d,e,f,g,h) -> int:
    # pack 8x32 into one 256-bit int
    return ((a<<224)|(b<<192)|(c<<160)|(d<<128)|(e<<96)|(f<<64)|(g<<32)|h) & ((1<<256)-1)

def cosine(u, v) -> float:
    u = np.asarray(u, dtype=float); v = np.asarray(v, dtype=float)
    du = float(np.dot(u,u)); dv = float(np.dot(v,v))
    if du == 0.0 or dv == 0.0: return 0.0
    return float(np.dot(u,v) / math.sqrt(du*dv))

# -------------------------------
# EDDY/HOT/COLD labeling
# -------------------------------
def zscore(flips: int, mu: float, sigma: float) -> float:
    if sigma <= 1e-12: return 0.0
    return abs(flips - mu) / sigma

def prob_from_z(z: float) -> float:
    # simple monotone "engagement" proxy (0..1)
    return 1.0 - math.exp(-z)

def label_from_z(z: float) -> str:
    # tune these two thresholds however you want:
    # - COLD = near-baseline (low deviation)
    # - HOT  = strong deviation (rare/high-z)
    if z < 0.35:
        return "COLD"
    if z >= 1.75:
        return "HOT"
    return "EDDY"

# -------------------------------
# Trace dataclasses
# -------------------------------
@dataclass
class RoundEvent:
    i: int
    flips: int
    z: float
    p: float
    label: str
    sim: float = 0.0
    sim0: float = 0.0
    pre: float = 0.0

@dataclass
class RunResult:
    ok: bool
    digest: str
    blocks: int
    label_pct: Dict[str, float]
    z_mean: float
    z_95: float
    sim_mean: float
    sim0: float
    pre: float
    op_counts: Dict[str, int]
    last_ops: List[Tuple[str,str]]
    assembly: List[str]

# -------------------------------
# Core SHA-256 with Nexus ops trace
# -------------------------------
def sha256_trace(msg: bytes, mu=MU, sigma=SIG, verify=True) -> RunResult:
    ops = []
    assembly = []
    op_counts = {k:0 for k in ["PROJECT","REFLECT","FOLD","LEAK","GATE","BRANCH","PIN","SYNC","VERIFY","COLLAPSE"]}

    def op(name, detail):
        ops.append((name, detail))
        op_counts[name] += 1

    # PROJECT
    op("PROJECT", "pad+frame")
    assembly.append("PROJECT   pad+frame")
    data = pad_sha256(msg)
    blocks = len(data)//64

    # PIN (init state)
    op("PIN", "init H0..H7")
    assembly.append("PIN       init H0..H7")
    H = H0.copy()

    all_round_events: List[RoundEvent] = []
    # process blocks
    for bidx in range(blocks):
        op("SYNC", f"block tick {bidx}")
        if bidx == 0:
            assembly.append("SYNC      block tick")
        block = data[bidx*64:(bidx+1)*64]

        # REFLECT
        dens = block_density(block)
        op("REFLECT", f"block density={dens:.4f}")
        if bidx == 0:
            assembly.append(f"REFLECT   block density={dens:.4f}")

        # FOLD (message schedule)
        W = list(struct.unpack(">16I", block))
        for i in range(16, 64):
            W.append((sig1(W[i-2]) + W[i-7] + sig0(W[i-15]) + W[i-16]) & 0xFFFFFFFF)
        op("FOLD", "schedule W0..W63")
        if bidx == 0:
            assembly.append("FOLD      schedule W0..W63")

        # PIN load work regs
        a,b,c,d,e,f,g,h = H
        op("PIN", "load work regs")
        if bidx == 0:
            assembly.append("PIN       load work regs")

        # round-by-round
        # We'll also build a per-round "partial signature" to compute sim vs final later.
        partial_counts = {"EDDY":0,"HOT":0,"COLD":0}
        partial_z = []
        # reference vectors for sim0 / pre
        ref0 = np.array([1,0,0, 0.0,0.0,0.0], dtype=float)  # "all-EDDY" anchor in signature space

        for i in range(64):
            op("GATE", f"block {bidx} round gates i={i}")
            if bidx == 0 and i < 5:
                assembly.append(f"GATE      round gates i={i:02d}")

            pre_state = state_pack_256(a,b,c,d,e,f,g,h)

            t1 = (h + Sig1(e) + Ch(e,f,g) + K[i] + W[i]) & 0xFFFFFFFF
            t2 = (Sig0(a) + Maj(a,b,c)) & 0xFFFFFFFF
            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF

            post_state = state_pack_256(a,b,c,d,e,f,g,h)
            flips = (pre_state ^ post_state).bit_count()
            z = zscore(flips, mu, sigma)
            p = prob_from_z(z)
            lab = label_from_z(z)

            partial_counts[lab] += 1
            partial_z.append(z)

            # sim is defined *after* we know the final signature; temporarily store 0s
            ev = RoundEvent(i=i, flips=flips, z=z, p=p, label=lab, sim=0.0, sim0=0.0, pre=0.0)
            all_round_events.append(ev)

            op("BRANCH", f"block {bidx} update | i={i:02d} {lab} p={p:.2f} z={z:.2f} flips={flips}")
            if bidx == 0 and i < 4:
                assembly.append(f"BRANCH    round update | i={i:02d} {lab:<4} p={p:.2f} z={z:.2f} flips={flips} sim=0.00")

        # LEAK (chaining add)
        H = [(H[j] + v) & 0xFFFFFFFF for j,v in enumerate([a,b,c,d,e,f,g,h])]
        op("LEAK", f"block {bidx}: chaining add")
        if bidx == 0:
            assembly.append("LEAK      chaining add")

    # COLLAPSE
    digest_bytes = b"".join(struct.pack(">I", x) for x in H)
    digest_hex = digest_bytes.hex()
    op("COLLAPSE", "final digest bytes")
    assembly.append("COLLAPSE  final digest bytes")

    ok = True
    if verify:
        ref = hashlib.sha256(msg).hexdigest()
        ok = (ref == digest_hex)
        op("VERIFY", "hashlib compare")
        assembly.append("VERIFY    hashlib compare")
    else:
        ref = None

    # Build stats over all rounds (across blocks)
    labels = [ev.label for ev in all_round_events]
    zvals = np.array([ev.z for ev in all_round_events], dtype=float)
    z_mean = float(zvals.mean()) if len(zvals) else 0.0
    z_95 = float(np.quantile(zvals, 0.95)) if len(zvals) else 0.0

    # label proportions
    uniq = sorted(set(labels))
    cnt = {k: labels.count(k) for k in uniq}
    total = len(labels) if labels else 1
    label_pct = {k: round(cnt[k]/total, 3) for k in cnt}

    # Signature vector for cross-domain similarity
    # [EDDY%, HOT%, COLD%, z_mean, z_95, blocks]
    sig = np.array([
        label_pct.get("EDDY",0.0),
        label_pct.get("HOT",0.0),
        label_pct.get("COLD",0.0),
        z_mean,
        z_95,
        float(blocks)
    ], dtype=float)

    # Now compute per-round sim as cosine(partial_signature, final_signature)
    final_sig = sig.copy()
    ref0 = np.array([1,0,0, 0.0,0.0,0.0], dtype=float)

    # Re-walk events grouped by blocks to compute running partial signature
    running = np.zeros_like(final_sig)
    running_counts = {"EDDY":0,"HOT":0,"COLD":0}
    running_z = []
    prev_sim = 0.0
    for ev in all_round_events:
        running_counts[ev.label] += 1
        running_z.append(ev.z)
        t = len(running_z)
        running[0] = running_counts["EDDY"]/t
        running[1] = running_counts["HOT"]/t
        running[2] = running_counts["COLD"]/t
        running[3] = float(np.mean(running_z))
        running[4] = float(np.quantile(running_z, 0.95))
        running[5] = float(blocks)

        ev.sim = cosine(running, final_sig)
        ev.sim0 = cosine(running, ref0)
        ev.pre = prev_sim
        prev_sim = ev.sim

    sim_mean = float(np.mean([ev.sim for ev in all_round_events])) if all_round_events else 0.0
    sim0_mean = float(np.mean([ev.sim0 for ev in all_round_events])) if all_round_events else 0.0
    pre_last = float(all_round_events[-1].pre) if all_round_events else 0.0

    # Patch a few assembly lines with sim for the first handful (optional)
    # (keeps it readable, doesn't spam)
    patched = []
    idx_round = 0
    for line in assembly:
        if line.startswith("BRANCH") and idx_round < len(all_round_events):
            ev = all_round_events[idx_round]
            if "sim=" in line:
                # already placeholder
                line = line.rsplit("sim=",1)[0] + f"sim={ev.sim:.2f}"
            else:
                line += f" sim={ev.sim:.2f}"
            idx_round += 1
        patched.append(line)
    assembly = patched

    return RunResult(
        ok=ok,
        digest=digest_hex,
        blocks=blocks,
        label_pct=label_pct,
        z_mean=z_mean,
        z_95=z_95,
        sim_mean=sim_mean,
        sim0=sim0_mean,
        pre=pre_last,
        op_counts=op_counts,
        last_ops=ops[-10:],
        assembly=assembly
    )

# -------------------------------
# Payload adapters
# -------------------------------
def bytes_payload(b: bytes) -> bytes:
    return b

def hex_payload(hx: str) -> bytes:
    hx = hx.strip().lower()
    if hx.startswith("0x"): hx = hx[2:]
    return bytes.fromhex(hx)

DNA_MAP_2BIT = {"A":0b00,"C":0b01,"G":0b10,"T":0b11}
def dna_2bit_packed(dna: str) -> bytes:
    dna = "".join([c for c in dna.upper() if c in "ACGT"])
    bits = 0
    out = bytearray()
    n = 0
    for c in dna:
        bits = (bits << 2) | DNA_MAP_2BIT[c]
        n += 1
        if n % 4 == 0:
            out.append(bits & 0xFF)
            bits = 0
    # pad remaining (if not multiple of 4 bases)
    rem = n % 4
    if rem:
        bits <<= (2*(4-rem))
        out.append(bits & 0xFF)
    return bytes(out)

def dna_ascii_map(dna: str) -> bytes:
    # "ascii map" version that still preserves the same 2-bit packing behavior
    # (so ACGTACGTACGT -> 1b1b1b)
    return dna_2bit_packed(dna)

def utf8_payload(s: str) -> bytes:
    return s.encode("utf-8")

# -------------------------------
# Run suite + plots + similarity
# -------------------------------
suite = [
    ("abc_bytes",       "bytes",  bytes_payload(b"abc")),
    ("abc_hex",         "hex",    hex_payload("616263")),
    ("dna_ascii_map",   "dna",    dna_ascii_map("ACGTACGTACGT")),
    ("dna_2bit_packed", "dna2bit",dna_2bit_packed("ACGTACGTACGT")),
    ("utf8_sentence",   "utf8",   utf8_payload("Dean’s Nexus trace: π/e/φ — hello world.")),
]

results: Dict[str, RunResult] = {}
signatures: Dict[str, np.ndarray] = {}

for name, kind, payload in suite:
    rr = sha256_trace(payload, mu=MU, sigma=SIG, verify=True)
    results[name] = rr
    sig = np.array([rr.label_pct.get("EDDY",0), rr.label_pct.get("HOT",0), rr.label_pct.get("COLD",0),
                    rr.z_mean, rr.z_95, float(rr.blocks)], dtype=float)
    signatures[name] = sig

    print(f"\n=== {name} ({kind}) ===")
    print(f"ok? {rr.ok}")
    print(f"digest: {rr.digest}")
    print(f"blocks: {rr.blocks}")
    print(f"label%: {rr.label_pct}")
    print(f"z_mean: {rr.z_mean:.3f}  z_95: {rr.z_95:.3f}  sim_mean: {rr.sim_mean:.3f}  sim0: {rr.sim0:.3f}  pre: {rr.pre:.3f}")
    print("\nlast 10 ops:")
    for opn, det in rr.last_ops:
        print(f"  {opn!r}, {det!r}")

# plots
names = [x[0] for x in suite]
eddy = [results[n].label_pct.get("EDDY",0) for n in names]
hot  = [results[n].label_pct.get("HOT",0) for n in names]
cold = [results[n].label_pct.get("COLD",0) for n in names]
zmean = [results[n].z_mean for n in names]

x = np.arange(len(names))
w = 0.25

plt.figure(figsize=(10,3))
plt.title("Label proportions (EDDY/HOT/COLD)")
plt.bar(x-w, eddy, width=w, label="EDDY")
plt.bar(x,   hot,  width=w, label="HOT")
plt.bar(x+w, cold, width=w, label="COLD")
plt.xticks(x, names, rotation=35, ha="right")
plt.ylim(0,1)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,3))
plt.title("z_mean per payload")
plt.plot(x, zmean, marker="o")
plt.xticks(x, names, rotation=35, ha="right")
plt.tight_layout()
plt.show()

# cosine similarity matrix
print("\n====================")
print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
print("====================\n")
for a in names:
    sims = []
    for b in names:
        if a == b: 
            continue
        sims.append((b, cosine(signatures[a], signatures[b])))
    sims.sort(key=lambda t: t[1], reverse=True)
    print(f"{a}:")
    for b, s in sims:
        print(f"  {b:<24} {s:.4f}")

# show assembly head for one payload (keeps output sane)
sample = results["abc_bytes"]
print("\n\nassembly (head):\n")
for line in sample.assembly[:18]:
    print(line)
print("\n...\n")

```

    GENLOCK baseline in-use: mu=128.034 sigma=7.984 (n=64256)
    
    === abc_bytes (bytes) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'COLD': 0.172, 'EDDY': 0.766, 'HOT': 0.062}
    z_mean: 0.794  z_95: 1.838  sim_mean: 0.993  sim0: 0.326  pre: 1.000
    
    last 10 ops:
      'BRANCH', 'block 0 update | i=60 EDDY p=0.47 z=0.63 flips=123'
      'GATE', 'block 0 round gates i=61'
      'BRANCH', 'block 0 update | i=61 EDDY p=0.68 z=1.13 flips=119'
      'GATE', 'block 0 round gates i=62'
      'BRANCH', 'block 0 update | i=62 EDDY p=0.68 z=1.13 flips=119'
      'GATE', 'block 0 round gates i=63'
      'BRANCH', 'block 0 update | i=63 EDDY p=0.72 z=1.26 flips=118'
      'LEAK', 'block 0: chaining add'
      'COLLAPSE', 'final digest bytes'
      'VERIFY', 'hashlib compare'
    
    === abc_hex (hex) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'COLD': 0.172, 'EDDY': 0.766, 'HOT': 0.062}
    z_mean: 0.794  z_95: 1.838  sim_mean: 0.993  sim0: 0.326  pre: 1.000
    
    last 10 ops:
      'BRANCH', 'block 0 update | i=60 EDDY p=0.47 z=0.63 flips=123'
      'GATE', 'block 0 round gates i=61'
      'BRANCH', 'block 0 update | i=61 EDDY p=0.68 z=1.13 flips=119'
      'GATE', 'block 0 round gates i=62'
      'BRANCH', 'block 0 update | i=62 EDDY p=0.68 z=1.13 flips=119'
      'GATE', 'block 0 round gates i=63'
      'BRANCH', 'block 0 update | i=63 EDDY p=0.72 z=1.26 flips=118'
      'LEAK', 'block 0: chaining add'
      'COLLAPSE', 'final digest bytes'
      'VERIFY', 'hashlib compare'
    
    === dna_ascii_map (dna) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'COLD': 0.25, 'EDDY': 0.719, 'HOT': 0.031}
    z_mean: 0.726  z_95: 1.487  sim_mean: 0.994  sim0: 0.384  pre: 0.999
    
    last 10 ops:
      'BRANCH', 'block 0 update | i=60 EDDY p=0.75 z=1.37 flips=139'
      'GATE', 'block 0 round gates i=61'
      'BRANCH', 'block 0 update | i=61 EDDY p=0.75 z=1.37 flips=139'
      'GATE', 'block 0 round gates i=62'
      'BRANCH', 'block 0 update | i=62 EDDY p=0.63 z=1.00 flips=136'
      'GATE', 'block 0 round gates i=63'
      'BRANCH', 'block 0 update | i=63 EDDY p=0.80 z=1.62 flips=141'
      'LEAK', 'block 0: chaining add'
      'COLLAPSE', 'final digest bytes'
      'VERIFY', 'hashlib compare'
    
    === dna_2bit_packed (dna2bit) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'COLD': 0.25, 'EDDY': 0.719, 'HOT': 0.031}
    z_mean: 0.726  z_95: 1.487  sim_mean: 0.994  sim0: 0.384  pre: 0.999
    
    last 10 ops:
      'BRANCH', 'block 0 update | i=60 EDDY p=0.75 z=1.37 flips=139'
      'GATE', 'block 0 round gates i=61'
      'BRANCH', 'block 0 update | i=61 EDDY p=0.75 z=1.37 flips=139'
      'GATE', 'block 0 round gates i=62'
      'BRANCH', 'block 0 update | i=62 EDDY p=0.63 z=1.00 flips=136'
      'GATE', 'block 0 round gates i=63'
      'BRANCH', 'block 0 update | i=63 EDDY p=0.80 z=1.62 flips=141'
      'LEAK', 'block 0: chaining add'
      'COLLAPSE', 'final digest bytes'
      'VERIFY', 'hashlib compare'
    
    === utf8_sentence (utf8) ===
    ok? True
    digest: 5119785df60ffdf865b95b7466481335d29c2d9068c8b9b83ecbda04dad95142
    blocks: 1
    label%: {'COLD': 0.172, 'EDDY': 0.766, 'HOT': 0.062}
    z_mean: 0.783  z_95: 1.838  sim_mean: 0.995  sim0: 0.366  pre: 1.000
    
    last 10 ops:
      'BRANCH', 'block 0 update | i=60 HOT p=0.85 z=1.87 flips=143'
      'GATE', 'block 0 round gates i=61'
      'BRANCH', 'block 0 update | i=61 HOT p=0.86 z=2.00 flips=144'
      'GATE', 'block 0 round gates i=62'
      'BRANCH', 'block 0 update | i=62 EDDY p=0.63 z=1.00 flips=136'
      'GATE', 'block 0 round gates i=63'
      'BRANCH', 'block 0 update | i=63 EDDY p=0.46 z=0.62 flips=133'
      'LEAK', 'block 0: chaining add'
      'COLLAPSE', 'final digest bytes'
      'VERIFY', 'hashlib compare'
    


    
![png](output_20_1.png)
    



    
![png](output_20_2.png)
    


    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex                  1.0000
      utf8_sentence            1.0000
      dna_ascii_map            0.9949
      dna_2bit_packed          0.9949
    abc_hex:
      abc_bytes                1.0000
      utf8_sentence            1.0000
      dna_ascii_map            0.9949
      dna_2bit_packed          0.9949
    dna_ascii_map:
      dna_2bit_packed          1.0000
      abc_bytes                0.9949
      abc_hex                  0.9949
      utf8_sentence            0.9948
    dna_2bit_packed:
      dna_ascii_map            1.0000
      abc_bytes                0.9949
      abc_hex                  0.9949
      utf8_sentence            0.9948
    utf8_sentence:
      abc_bytes                1.0000
      abc_hex                  1.0000
      dna_ascii_map            0.9948
      dna_2bit_packed          0.9948
    
    
    assembly (head):
    
    PROJECT   pad+frame
    PIN       init H0..H7
    SYNC      block tick
    REFLECT   block density=0.0254
    FOLD      schedule W0..W63
    PIN       load work regs
    GATE      round gates i=00
    BRANCH    round update | i=00 EDDY p=0.80 z=1.63 flips=115 sim=0.94
    GATE      round gates i=01
    BRANCH    round update | i=01 EDDY p=0.72 z=1.26 flips=118 sim=0.96
    GATE      round gates i=02
    BRANCH    round update | i=02 HOT  p=0.85 z=1.88 flips=113 sim=0.95
    GATE      round gates i=03
    BRANCH    round update | i=03 EDDY p=0.80 z=1.63 flips=115 sim=0.96
    GATE      round gates i=04
    LEAK      chaining add
    COLLAPSE  final digest bytes
    VERIFY    hashlib compare
    
    ...
    
    


```python
# Nexus ISA tracer for SHA-256 (single-cell, self-contained)
import os, math, hashlib, random
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Helpers
# -----------------------------
def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def shr(x, n):
    return (x >> n) & 0xFFFFFFFF

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def big_sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def big_sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def small_sigma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def small_sigma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def u32(x):
    return x & 0xFFFFFFFF

def popcount32(x: int) -> int:
    return int(x & 0xFFFFFFFF).bit_count()

def state_to_bits(state8: List[int]) -> int:
    # pack 8x32 into one 256-bit int for fast hamming
    out = 0
    for w in state8:
        out = (out << 32) | (w & 0xFFFFFFFF)
    return out

def hamming256(a: int, b: int) -> int:
    return (a ^ b).bit_count()

def normal_sf(z: float) -> float:
    # survival function for standard normal (two-sided-ish for magnitude)
    # p = P(|Z| >= z) = 2 * (1 - Phi(z)) = erfc(z/sqrt(2))
    return math.erfc(z / math.sqrt(2))

def percentile(xs: List[float], q: float) -> float:
    if not xs:
        return float("nan")
    return float(np.quantile(np.array(xs), q))

# -----------------------------
# SHA-256 constants
# -----------------------------
K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

IV = [
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]

# -----------------------------
# Payload adapters
# -----------------------------
DNA_MAP = {"A":0b00, "C":0b01, "G":0b10, "T":0b11}

def payload_bytes(kind: str, payload: Any) -> bytes:
    if kind == "bytes":
        if isinstance(payload, (bytes, bytearray)):
            return bytes(payload)
        raise TypeError("bytes payload must be bytes-like")
    if kind == "hex":
        if isinstance(payload, str):
            s = payload.strip().lower().replace("0x","")
            if len(s) % 2: s = "0" + s
            return bytes.fromhex(s)
        raise TypeError("hex payload must be str")
    if kind == "utf8":
        if isinstance(payload, str):
            return payload.encode("utf-8")
        raise TypeError("utf8 payload must be str")
    if kind == "dna":
        # ASCII map (each base -> 2 bits, but stored as bytes by packing 4 bases per byte)
        # We'll support two submodes via tuple: ("ascii"|"2bit", dna_string)
        if isinstance(payload, tuple) and len(payload) == 2:
            mode, dna = payload
        else:
            mode, dna = "ascii", payload
        dna = str(dna).strip().upper()
        if mode == "ascii":
            # simple byte map: A,C,G,T -> 0,1,2,3 then packed as bytes
            b = bytes([DNA_MAP[c] for c in dna])
            return b
        if mode == "2bit":
            bits = 0
            n = 0
            out = bytearray()
            for c in dna:
                bits = (bits << 2) | DNA_MAP[c]
                n += 1
                if n == 4:
                    out.append(bits & 0xFF)
                    bits = 0
                    n = 0
            if n:
                # pad remaining bases with zeros
                bits = bits << (2*(4-n))
                out.append(bits & 0xFF)
            return bytes(out)
        raise ValueError("dna mode must be 'ascii' or '2bit'")
    raise ValueError(f"Unknown kind: {kind}")

# -----------------------------
# ISA + tracing
# -----------------------------
@dataclass
class RoundStat:
    block: int
    i: int
    flips: int
    z: float
    p: float
    sim: float
    label: str

@dataclass
class TraceResult:
    ok: bool
    digest: str
    blocks: int
    op_counts: Dict[str,int]
    round_stats: List[RoundStat]
    ops_tail: List[Tuple[str,str]]
    sigvec: np.ndarray

def sha256_trace(message: bytes,
                 mu: float,
                 sigma: float,
                 z_cold: float = 0.25,
                 z_hot: float = 1.85,
                 sim_hot_max: float = 0.40,
                 keep_tail: int = 12) -> TraceResult:
    ops = []
    op_counts = {k:0 for k in ["PROJECT","PIN","SYNC","REFLECT","FOLD","GATE","BRANCH","LEAK","COLLAPSE","VERIFY"]}

    def emit(op, note):
        ops.append((op, note))
        op_counts[op] = op_counts.get(op, 0) + 1

    # PROJECT: pad+frame
    emit("PROJECT", "pad+frame")
    ml = len(message) * 8
    m = bytearray(message)
    m.append(0x80)
    while (len(m) * 8) % 512 != 448:
        m.append(0)
    m += ml.to_bytes(8, "big")

    # PIN: init H0..H7
    emit("PIN", "init H0..H7")
    h = IV.copy()

    blocks = len(m) // 64
    round_stats: List[RoundStat] = []

    # helper for similarity: cosine to "baseline flip vector" (all mu)
    # We'll compute sim as (1 - normalized |flips-mu|) squashed; simple and stable.
    # This is just a knob; you can swap for a real cosine on a longer signature later.
    def sim_from_flips(flips):
        # map deviation -> [0,1], where 1 means close to baseline
        dev = abs(flips - mu) / (sigma + 1e-9)
        return float(max(0.0, 1.0 - dev/4.0))

    for b in range(blocks):
        emit("SYNC", f"block {b} tick")
        chunk = m[b*64:(b+1)*64]
        emit("REFLECT", f"block density={sum(chunk)/(64*255):.4f}")

        # FOLD: schedule
        emit("FOLD", "schedule W0..W63")
        W = [int.from_bytes(chunk[i*4:(i+1)*4], "big") for i in range(16)]
        for i in range(16, 64):
            W.append(u32(small_sigma1(W[i-2]) + W[i-7] + small_sigma0(W[i-15]) + W[i-16]))

        # PIN: load work regs
        emit("PIN", "load work regs")
        a,b2,c,d,e,f,g,hh = h

        for i in range(64):
            emit("GATE", f"block {b} round gates i={i:02d}")

            pre_state = state_to_bits([a,b2,c,d,e,f,g,hh])

            t1 = u32(hh + big_sigma1(e) + ch(e,f,g) + K[i] + W[i])
            t2 = u32(big_sigma0(a) + maj(a,b2,c))

            hh = g
            g = f
            f = e
            e = u32(d + t1)
            d = c
            c = b2
            b2 = a
            a = u32(t1 + t2)

            post_state = state_to_bits([a,b2,c,d,e,f,g,hh])
            flips = hamming256(pre_state, post_state)

            z = abs(flips - mu) / (sigma + 1e-9)
            p = normal_sf(z)  # two-sided tail-ish
            sim = sim_from_flips(flips)

            # Labels are optional; verbs matter. Still useful for quick categorization.
            if z <= z_cold:
                label = "COLD"
            elif z >= z_hot and sim <= sim_hot_max:
                label = "HOT"
            else:
                label = "EDDY"

            emit("BRANCH", f"block {b} update | i={i:02d} {label} p={p:.2f} z={z:.2f} flips={flips} sim={sim:.2f}")

            round_stats.append(RoundStat(block=b, i=i, flips=flips, z=float(z), p=float(p), sim=float(sim), label=label))

        emit("LEAK", f"block {b}: chaining add")
        h = [u32(h[j] + x) for j,x in enumerate([a,b2,c,d,e,f,g,hh])]

    emit("COLLAPSE", "final digest bytes")
    digest = b"".join(x.to_bytes(4,"big") for x in h).hex()

    # VERIFY
    ref = hashlib.sha256(bytes(message)).hexdigest()
    ok = (digest == ref)
    emit("VERIFY", "hashlib compare")

    # signature vector for cross-domain cosine:
    # [EDDY%, HOT%, COLD%, z_mean, z_95, sim_mean]
    labels = [rs.label for rs in round_stats]
    n = len(labels) if labels else 1
    ed = labels.count("EDDY")/n
    ho = labels.count("HOT")/n
    co = labels.count("COLD")/n
    zs = [rs.z for rs in round_stats]
    sims = [rs.sim for rs in round_stats]
    sig = np.array([ed, ho, co,
                    float(np.mean(zs)) if zs else 0.0,
                    percentile(zs, 0.95) if zs else 0.0,
                    float(np.mean(sims)) if sims else 0.0], dtype=float)

    return TraceResult(
        ok=ok,
        digest=digest,
        blocks=blocks,
        op_counts=op_counts,
        round_stats=round_stats,
        ops_tail=ops[-keep_tail:],
        sigvec=sig
    )

# -----------------------------
# GENLOCK baseline builder
# -----------------------------
def build_genlock_baseline(n_samples: int = 2000,
                           msg_min: int = 0,
                           msg_max: int = 96,
                           seed: int = 1337) -> Tuple[float,float,int]:
    rnd = random.Random(seed)
    flips_all = []
    # build baseline on single-block traces (truncate/pad randomness via message length range)
    # We compute flips from SHA round-to-round state transitions, so we need the trace mechanics.
    # We'll do a lightweight compute: reuse sha256_trace but with temporary mu/sigma guesses,
    # then recompute flips distribution from the round_stats.
    tmp_mu, tmp_sigma = 128.0, 8.0
    for _ in range(n_samples):
        L = rnd.randint(msg_min, msg_max)
        msg = bytes(rnd.getrandbits(8) for _ in range(L))
        tr = sha256_trace(msg, mu=tmp_mu, sigma=tmp_sigma)
        for rs in tr.round_stats:
            flips_all.append(rs.flips)
    mu = float(np.mean(flips_all))
    sigma = float(np.std(flips_all, ddof=0))
    return mu, sigma, len(flips_all)

# -----------------------------
# Run suite
# -----------------------------
mu, sigma, n = build_genlock_baseline(n_samples=1000, msg_min=0, msg_max=96, seed=2026)
print(f"GENLOCK baseline in-use: mu={mu:.3f} sigma={sigma:.3f} (n={n})\n")

payloads = [
    ("abc_bytes", "bytes", b"abc"),
    ("abc_hex", "hex", "616263"),
    ("dna_ascii_map", "dna", ("ascii", "ACGTACGTACGT")),
    ("dna_2bit_packed", "dna", ("2bit", "ACGTACGTACGT")),
    ("utf8_sentence", "utf8", "whack-a-mole popped into my head")
]

results = {}
for name, kind, payload in payloads:
    msg = payload_bytes(kind, payload)
    tr = sha256_trace(msg, mu=mu, sigma=sigma)
    results[name] = (kind, payload, tr)

# -----------------------------
# Summaries
# -----------------------------
def label_props(stats: List[RoundStat]) -> Dict[str,float]:
    if not stats:
        return {}
    n = len(stats)
    out = {}
    for k in ["EDDY","HOT","COLD"]:
        out[k] = sum(1 for s in stats if s.label==k) / n
    return out

for name,(kind,payload,tr) in results.items():
    props = label_props(tr.round_stats)
    zs = [s.z for s in tr.round_stats]
    sims = [s.sim for s in tr.round_stats]
    print(f"=== {name} ({kind}) ===")
    print(f"ok? {tr.ok}")
    print(f"digest: {tr.digest}")
    print(f"blocks: {tr.blocks}")
    print(f"label%: { {k: round(v,3) for k,v in props.items()} }")
    print(f"z_mean: {np.mean(zs):.3f}  z_95: {np.quantile(zs,0.95):.3f}  sim_mean: {np.mean(sims):.3f}")
    print("last 10 ops:")
    for op in tr.ops_tail[-10:]:
        print(" ", op)
    print()

# -----------------------------
# Cross-domain similarity (cosine on signature vector)
# -----------------------------
def cosine(a: np.ndarray, b: np.ndarray) -> float:
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    if na == 0 or nb == 0:
        return 0.0
    return float(np.dot(a,b) / (na*nb))

names = list(results.keys())
sig = {name: results[name][2].sigvec for name in names}

print("\n====================")
print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
print("====================\n")
for a in names:
    sims = []
    for b in names:
        if a == b: continue
        sims.append((b, cosine(sig[a], sig[b])))
    sims.sort(key=lambda x: x[1], reverse=True)
    print(f"{a}:")
    for b,val in sims:
        print(f"  {b:28s} {val:.4f}")
    print()

# -----------------------------
# Whack-a-mole view: top rounds by z (per payload)
# -----------------------------
TOPK = 6
print("\n====================")
print("WHACK-A-MOLE (top z rounds per payload)")
print("====================\n")
for name,(kind,payload,tr) in results.items():
    rs = tr.round_stats
    rs_sorted = sorted(rs, key=lambda r: r.z, reverse=True)[:TOPK]
    print(f"{name}:")
    for r in rs_sorted:
        print(f"  block={r.block} i={r.i:02d} z={r.z:.2f} flips={r.flips} label={r.label}  (K={K[r.i]:08x})")
    print()

# -----------------------------
# Plots (label proportions + z_mean)
# -----------------------------
labels = ["EDDY","HOT","COLD"]
x = np.arange(len(names))
width = 0.25

prop_mat = np.zeros((len(labels), len(names)))
z_mean = np.zeros(len(names))

for j,name in enumerate(names):
    tr = results[name][2]
    props = label_props(tr.round_stats)
    for i,lbl in enumerate(labels):
        prop_mat[i,j] = props.get(lbl, 0.0)
    z_mean[j] = float(np.mean([s.z for s in tr.round_stats]))

plt.figure()
for i,lbl in enumerate(labels):
    plt.bar(x + (i-1)*width, prop_mat[i], width, label=lbl)
plt.xticks(x, names, rotation=35, ha="right")
plt.ylim(0, 1.0)
plt.title("Label proportions (EDDY/HOT/COLD)")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(names, z_mean, marker="o")
plt.xticks(rotation=35, ha="right")
plt.title("z_mean per payload")
plt.tight_layout()
plt.show()

```

    GENLOCK baseline in-use: mu=127.927 sigma=7.973 (n=92160)
    
    === abc_bytes (bytes) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.875, 'HOT': 0.0, 'COLD': 0.125}
    z_mean: 0.792  z_95: 1.835  sim_mean: 0.802
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.54 z=0.62 flips=123 sim=0.85')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.26 z=1.12 flips=119 sim=0.72')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.26 z=1.12 flips=119 sim=0.72')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.21 z=1.25 flips=118 sim=0.69')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === abc_hex (hex) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.875, 'HOT': 0.0, 'COLD': 0.125}
    z_mean: 0.792  z_95: 1.835  sim_mean: 0.802
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.54 z=0.62 flips=123 sim=0.85')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.26 z=1.12 flips=119 sim=0.72')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.26 z=1.12 flips=119 sim=0.72')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.21 z=1.25 flips=118 sim=0.69')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === dna_ascii_map (dna) ===
    ok? True
    digest: 5252677269f32b37e5c98cc77adbb102f5155aac869f0c0d6a5ff4600626fa17
    blocks: 1
    label%: {'EDDY': 0.703, 'HOT': 0.0, 'COLD': 0.297}
    z_mean: 0.515  z_95: 1.370  sim_mean: 0.871
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 COLD p=0.89 z=0.13 flips=129 sim=0.97')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.54 z=0.62 flips=123 sim=0.85')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 COLD p=0.99 z=0.01 flips=128 sim=1.00')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.79 z=0.26 flips=130 sim=0.94')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === dna_2bit_packed (dna) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.766, 'HOT': 0.0, 'COLD': 0.234}
    z_mean: 0.729  z_95: 1.480  sim_mean: 0.818
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.16 z=1.39 flips=139 sim=0.65')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.16 z=1.39 flips=139 sim=0.65')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.31 z=1.01 flips=136 sim=0.75')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.10 z=1.64 flips=141 sim=0.59')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    === utf8_sentence (utf8) ===
    ok? True
    digest: 2834e0187c99eedc7670e8c8957870a406967834922cfbf5778abae993dd8635
    blocks: 1
    label%: {'EDDY': 0.812, 'HOT': 0.0, 'COLD': 0.188}
    z_mean: 0.824  z_95: 1.979  sim_mean: 0.794
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.52 z=0.64 flips=133 sim=0.84')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.52 z=0.64 flips=133 sim=0.84')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.21 z=1.26 flips=138 sim=0.68')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.21 z=1.26 flips=138 sim=0.68')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex                      1.0000
      utf8_sentence                0.9984
      dna_2bit_packed              0.9945
      dna_ascii_map                0.9834
    
    abc_hex:
      abc_bytes                    1.0000
      utf8_sentence                0.9984
      dna_2bit_packed              0.9945
      dna_ascii_map                0.9834
    
    dna_ascii_map:
      dna_2bit_packed              0.9935
      abc_bytes                    0.9834
      abc_hex                      0.9834
      utf8_sentence                0.9807
    
    dna_2bit_packed:
      abc_bytes                    0.9945
      abc_hex                      0.9945
      dna_ascii_map                0.9935
      utf8_sentence                0.9916
    
    utf8_sentence:
      abc_bytes                    0.9984
      abc_hex                      0.9984
      dna_2bit_packed              0.9916
      dna_ascii_map                0.9807
    
    
    ====================
    WHACK-A-MOLE (top z rounds per payload)
    ====================
    
    abc_bytes:
      block=0 i=04 z=2.00 flips=112 label=EDDY  (K=3956c25b)
      block=0 i=53 z=1.89 flips=143 label=EDDY  (K=4ed8aa4a)
      block=0 i=02 z=1.87 flips=113 label=EDDY  (K=b5c0fbcf)
      block=0 i=57 z=1.87 flips=113 label=EDDY  (K=78a5636f)
      block=0 i=00 z=1.62 flips=115 label=EDDY  (K=428a2f98)
      block=0 i=03 z=1.62 flips=115 label=EDDY  (K=e9b5dba5)
    
    abc_hex:
      block=0 i=04 z=2.00 flips=112 label=EDDY  (K=3956c25b)
      block=0 i=53 z=1.89 flips=143 label=EDDY  (K=4ed8aa4a)
      block=0 i=02 z=1.87 flips=113 label=EDDY  (K=b5c0fbcf)
      block=0 i=57 z=1.87 flips=113 label=EDDY  (K=78a5636f)
      block=0 i=00 z=1.62 flips=115 label=EDDY  (K=428a2f98)
      block=0 i=03 z=1.62 flips=115 label=EDDY  (K=e9b5dba5)
    
    dna_ascii_map:
      block=0 i=50 z=1.77 flips=142 label=EDDY  (K=2748774c)
      block=0 i=52 z=1.51 flips=140 label=EDDY  (K=391c0cb3)
      block=0 i=00 z=1.50 flips=116 label=EDDY  (K=428a2f98)
      block=0 i=53 z=1.39 flips=139 label=EDDY  (K=4ed8aa4a)
      block=0 i=51 z=1.26 flips=138 label=EDDY  (K=34b0bcb5)
      block=0 i=08 z=1.14 flips=137 label=EDDY  (K=d807aa98)
    
    dna_2bit_packed:
      block=0 i=43 z=2.25 flips=110 label=EDDY  (K=c76c51a3)
      block=0 i=58 z=1.89 flips=143 label=EDDY  (K=84c87814)
      block=0 i=63 z=1.64 flips=141 label=EDDY  (K=c67178f2)
      block=0 i=44 z=1.50 flips=116 label=EDDY  (K=d192e819)
      block=0 i=48 z=1.39 flips=139 label=EDDY  (K=19a4c116)
      block=0 i=50 z=1.39 flips=139 label=EDDY  (K=2748774c)
    
    utf8_sentence:
      block=0 i=12 z=2.12 flips=111 label=EDDY  (K=72be5d74)
      block=0 i=56 z=2.12 flips=111 label=EDDY  (K=748f82ee)
      block=0 i=11 z=2.00 flips=112 label=EDDY  (K=550c7dc3)
      block=0 i=55 z=2.00 flips=112 label=EDDY  (K=682e6ff3)
      block=0 i=51 z=1.87 flips=113 label=EDDY  (K=34b0bcb5)
      block=0 i=57 z=1.75 flips=114 label=EDDY  (K=78a5636f)
    
    


    
![png](output_21_1.png)
    



    
![png](output_21_2.png)
    



```python
# Single-cell: SHA-256 + Nexus 10-verb trace + GENLOCK baseline + whack-a-mole

import os, math, hashlib, random
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Helpers
# ----------------------------
MASK32 = 0xFFFFFFFF

def rotr(x, n): return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32
def shr(x, n):  return (x >> n) & MASK32
def ch(x, y, z):  return (x & y) ^ (~x & z)
def maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def big_sigma0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def big_sigma1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def small_sigma0(x): return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
def small_sigma1(x): return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def pack_state(a,b,c,d,e,f,g,h) -> int:
    # pack 8x32 into 256-bit int (big-endian word order)
    return ((a<<224)|(b<<192)|(c<<160)|(d<<128)|(e<<96)|(f<<64)|(g<<32)|h)

def hamming256(x: int) -> int:
    return x.bit_count()

def cosine(u, v):
    u = np.array(u, dtype=float); v = np.array(v, dtype=float)
    nu = np.linalg.norm(u); nv = np.linalg.norm(v)
    return float(u.dot(v) / (nu*nv + 1e-12))

# SHA-256 constants
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

def pad_sha256(msg: bytes) -> bytes:
    ml = len(msg) * 8
    out = msg + b"\x80"
    while (len(out) % 64) != 56:
        out += b"\x00"
    out += ml.to_bytes(8, "big")
    return out

@dataclass
class RoundTrace:
    block: int
    i: int
    flips: int
    z: float
    k: int
    # verb tags are present conceptually; we keep them implicit in printing

@dataclass
class RunResult:
    name: str
    kind: str
    ok: bool
    digest: str
    blocks: int
    z_mean: float
    z_95: float
    flips_mean: float
    traces: List[RoundTrace]
    ops_tail: List[Tuple[str,str]]

def sha256_trace(msg: bytes, mu: float, sigma: float, keep_top=6) -> RunResult:
    padded = pad_sha256(msg)
    blocks = len(padded) // 64

    h = H0[:]
    traces: List[RoundTrace] = []
    flips_all: List[int] = []

    # Verb stream (high level)
    ops_tail: List[Tuple[str,str]] = []
    def op(tag, detail):
        ops_tail.append((tag, detail))
        if len(ops_tail) > 10:
            ops_tail.pop(0)

    op("PROJECT", "pad+frame")
    op("PIN", "init H0..H7")

    for b in range(blocks):
        op("SYNC", f"block tick b={b}")

        chunk = padded[b*64:(b+1)*64]
        # Message schedule
        W = [int.from_bytes(chunk[i*4:(i+1)*4], "big") for i in range(16)]
        for i in range(16, 64):
            W.append((small_sigma1(W[i-2]) + W[i-7] + small_sigma0(W[i-15]) + W[i-16]) & MASK32)

        # "REFLECT" as a simple block density proxy
        block_ones = sum(int.from_bytes(chunk[i:i+4], "big").bit_count() for i in range(0, 64, 4))
        block_density = block_ones / (64*8)
        op("REFLECT", f"block density={block_density:.4f}")
        op("FOLD", "schedule W0..W63")
        op("PIN", "load work regs")

        a,b2,c,d,e,f,g,hh = h
        prev_state = pack_state(a,b2,c,d,e,f,g,hh)

        for i in range(64):
            op("GATE", f"round gates i={i:02d}")
            T1 = (hh + big_sigma1(e) + ch(e,f,g) + K[i] + W[i]) & MASK32
            T2 = (big_sigma0(a) + maj(a,b2,c)) & MASK32
            hh = g
            g  = f
            f  = e
            e  = (d + T1) & MASK32
            d  = c
            c  = b2
            b2 = a
            a  = (T1 + T2) & MASK32

            cur_state = pack_state(a,b2,c,d,e,f,g,hh)
            flips = hamming256(prev_state ^ cur_state)
            flips_all.append(flips)

            z = abs(flips - mu) / (sigma + 1e-12)
            traces.append(RoundTrace(block=b, i=i, flips=flips, z=z, k=K[i]))

            prev_state = cur_state
            op("BRANCH", f"block {b} update | i={i:02d} z={z:.2f} flips={flips}")

        # chaining add
        op("LEAK", f"block {b}: chaining add")
        h = [
            (h[0] + a) & MASK32,
            (h[1] + b2) & MASK32,
            (h[2] + c) & MASK32,
            (h[3] + d) & MASK32,
            (h[4] + e) & MASK32,
            (h[5] + f) & MASK32,
            (h[6] + g) & MASK32,
            (h[7] + hh) & MASK32,
        ]

    op("COLLAPSE", "final digest bytes")
    digest = b"".join(x.to_bytes(4, "big") for x in h).hex()
    ref = hashlib.sha256(msg).hexdigest()
    op("VERIFY", "hashlib compare")
    ok = (digest == ref)

    z_vals = [t.z for t in traces]
    flips_vals = [t.flips for t in traces]
    z_mean = float(np.mean(z_vals)) if z_vals else 0.0
    z_95   = float(np.quantile(z_vals, 0.95)) if z_vals else 0.0
    flips_mean = float(np.mean(flips_vals)) if flips_vals else 0.0

    return ok, digest, blocks, z_mean, z_95, flips_mean, traces, ops_tail

# ----------------------------
# GENLOCK baseline builder (mu/sigma of flips)
# ----------------------------
def genlock_baseline(n_blocks=1024, seed=1234):
    rng = random.Random(seed)
    flips = []
    # sample random 64-byte blocks as independent inputs
    for _ in range(n_blocks):
        msg = bytes(rng.getrandbits(8) for _ in range(64))
        padded = pad_sha256(msg)
        chunk = padded[:64]  # exactly one block after padding for 64B? Actually 64B msg pads to 128B.
        # To keep baseline consistent, use a single *block* worth of bytes directly (not full message padding).
        chunk = msg  # treat as one block
        W = [int.from_bytes(chunk[i*4:(i+1)*4], "big") for i in range(16)]
        for i in range(16, 64):
            W.append((small_sigma1(W[i-2]) + W[i-7] + small_sigma0(W[i-15]) + W[i-16]) & MASK32)

        a,b2,c,d,e,f,g,hh = H0
        prev = pack_state(a,b2,c,d,e,f,g,hh)
        for i in range(64):
            T1 = (hh + big_sigma1(e) + ch(e,f,g) + K[i] + W[i]) & MASK32
            T2 = (big_sigma0(a) + maj(a,b2,c)) & MASK32
            hh = g; g=f; f=e; e=(d+T1)&MASK32; d=c; c=b2; b2=a; a=(T1+T2)&MASK32
            cur = pack_state(a,b2,c,d,e,f,g,hh)
            flips.append(hamming256(prev ^ cur))
            prev = cur
    mu = float(np.mean(flips))
    sigma = float(np.std(flips, ddof=0))
    n = len(flips)
    return n, mu, sigma

# ----------------------------
# Payload encoders
# ----------------------------
def from_hex(s: str) -> bytes:
    s = s.strip().lower()
    return bytes.fromhex(s)

def dna_2bit_pack(seq: str) -> bytes:
    # A=00 C=01 G=10 T=11 packed 4 bases per byte
    m = {'A':0,'C':1,'G':2,'T':3}
    seq = seq.strip().upper()
    out = bytearray()
    cur = 0
    bits = 0
    for ch_ in seq:
        if ch_ not in m: 
            continue
        cur = (cur << 2) | m[ch_]
        bits += 2
        if bits == 8:
            out.append(cur & 0xFF)
            cur = 0
            bits = 0
    if bits:
        cur = cur << (8 - bits)
        out.append(cur & 0xFF)
    return bytes(out)

def dna_ascii_map(seq: str) -> bytes:
    # lightweight mapping to bytes (not packed): A,C,G,T -> 0,1,2,3 repeated
    m = {'A':0,'C':1,'G':2,'T':3}
    seq = seq.strip().upper()
    return bytes(m.get(ch_, 0) for ch_ in seq)

# ----------------------------
# Run suite
# ----------------------------
n, mu, sigma = genlock_baseline(n_blocks=1440, seed=2026)  # ~92160 round-samples
print(f"GENLOCK baseline in-use: mu={mu:.3f} sigma={sigma:.3f} (n={n})\n")

payloads = [
    ("abc_bytes", "bytes", b"abc"),
    ("abc_hex", "hex", from_hex("616263")),
    ("dna_ascii_map", "dna", dna_ascii_map("ACGTACGTACGT")),
    ("dna_2bit_packed", "dna2bit", dna_2bit_pack("ACGTACGTACGT")),
    ("utf8_sentence", "utf8", "whack-a-mole is a simple peg and gear system.".encode("utf-8")),
]

results = []
for name, kind, msg in payloads:
    ok, digest, blocks, z_mean, z_95, flips_mean, traces, ops_tail = sha256_trace(msg, mu, sigma)
    results.append({
        "name": name, "kind": kind, "ok": ok, "digest": digest, "blocks": blocks,
        "z_mean": z_mean, "z_95": z_95, "flips_mean": flips_mean,
        "traces": traces, "ops_tail": ops_tail,
    })
    print(f"=== {name} ({kind}) ===")
    print(f"ok? {ok}")
    print(f"digest: {digest}")
    print(f"blocks: {blocks}")
    print(f"z_mean: {z_mean:.3f}  z_95: {z_95:.3f}  flips_mean: {flips_mean:.2f}\n")

# ----------------------------
# Cross-domain similarity (signature vectors)
# ----------------------------
# VERB-FOCUSED signature: [z_mean, z_95, flips_mean]
sig = {r["name"]: [r["z_mean"], r["z_95"], r["flips_mean"]] for r in results}

print("====================")
print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
print("====================\n")
for a in sig:
    sims = sorted(((b, cosine(sig[a], sig[b])) for b in sig if b != a), key=lambda x: -x[1])
    print(f"{a}:")
    for b, s in sims:
        print(f"  {b:25s} {s:.4f}")
    print()

# ----------------------------
# Whack-a-mole: top z rounds
# ----------------------------
print("====================")
print("WHACK-A-MOLE (top z rounds per payload)")
print("====================\n")
TOP = 6
for r in results:
    traces = sorted(r["traces"], key=lambda t: -t.z)[:TOP]
    print(f"{r['name']}:")
    for t in traces:
        print(f"  block={t.block} i={t.i:02d} z={t.z:.2f} flips={t.flips:3d}  (K={t.k:08x})")
    print()

# ----------------------------
# Plot: z_mean and z_95 per payload (no label obsession—these are dynamics summaries)
# ----------------------------
names = [r["name"] for r in results]
z_mean_vals = [r["z_mean"] for r in results]
z95_vals = [r["z_95"] for r in results]

plt.figure()
plt.plot(names, z_mean_vals, marker="o")
plt.title("z_mean per payload")
plt.xticks(rotation=30, ha="right")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(names, z95_vals, marker="o")
plt.title("z_95 per payload")
plt.xticks(rotation=30, ha="right")
plt.grid(True)
plt.show()

# ----------------------------
# Print the verb assembly head (the "ISA" view)
# ----------------------------
print("\nassembly (head-ish):\n")
print("PROJECT   pad+frame")
print("PIN       init H0..H7")
print("SYNC      block tick")
print("REFLECT   block density")
print("FOLD      schedule W0..W63")
print("PIN       load work regs")
print("GATE      round gates (x64)")
print("BRANCH    round update (x64)")
print("LEAK      chaining add")
print("COLLAPSE  final digest bytes")
print("VERIFY    hashlib compare")

```

    GENLOCK baseline in-use: mu=127.855 sigma=8.052 (n=92160)
    
    === abc_bytes (bytes) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    z_mean: 0.783  z_95: 1.808  flips_mean: 126.27
    
    === abc_hex (hex) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    z_mean: 0.783  z_95: 1.808  flips_mean: 126.27
    
    === dna_ascii_map (dna) ===
    ok? True
    digest: 5252677269f32b37e5c98cc77adbb102f5155aac869f0c0d6a5ff4600626fa17
    blocks: 1
    z_mean: 0.513  z_95: 1.365  flips_mean: 129.55
    
    === dna_2bit_packed (dna2bit) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    z_mean: 0.723  z_95: 1.459  flips_mean: 128.98
    
    === utf8_sentence (utf8) ===
    ok? True
    digest: bf587e37f6a5e7400fb8d1e5ca4cfec863fa23386cc56e7c932fcff6dc47375c
    blocks: 1
    z_mean: 0.851  z_95: 1.875  flips_mean: 127.23
    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex                   1.0000
      utf8_sentence             1.0000
      dna_2bit_packed           1.0000
      dna_ascii_map             1.0000
    
    abc_hex:
      abc_bytes                 1.0000
      utf8_sentence             1.0000
      dna_2bit_packed           1.0000
      dna_ascii_map             1.0000
    
    dna_ascii_map:
      dna_2bit_packed           1.0000
      abc_bytes                 1.0000
      abc_hex                   1.0000
      utf8_sentence             1.0000
    
    dna_2bit_packed:
      dna_ascii_map             1.0000
      abc_bytes                 1.0000
      abc_hex                   1.0000
      utf8_sentence             1.0000
    
    utf8_sentence:
      abc_bytes                 1.0000
      abc_hex                   1.0000
      dna_2bit_packed           1.0000
      dna_ascii_map             1.0000
    
    ====================
    WHACK-A-MOLE (top z rounds per payload)
    ====================
    
    abc_bytes:
      block=0 i=04 z=1.97 flips=112  (K=3956c25b)
      block=0 i=53 z=1.88 flips=143  (K=4ed8aa4a)
      block=0 i=02 z=1.84 flips=113  (K=b5c0fbcf)
      block=0 i=57 z=1.84 flips=113  (K=78a5636f)
      block=0 i=00 z=1.60 flips=115  (K=428a2f98)
      block=0 i=03 z=1.60 flips=115  (K=e9b5dba5)
    
    abc_hex:
      block=0 i=04 z=1.97 flips=112  (K=3956c25b)
      block=0 i=53 z=1.88 flips=143  (K=4ed8aa4a)
      block=0 i=02 z=1.84 flips=113  (K=b5c0fbcf)
      block=0 i=57 z=1.84 flips=113  (K=78a5636f)
      block=0 i=00 z=1.60 flips=115  (K=428a2f98)
      block=0 i=03 z=1.60 flips=115  (K=e9b5dba5)
    
    dna_ascii_map:
      block=0 i=50 z=1.76 flips=142  (K=2748774c)
      block=0 i=52 z=1.51 flips=140  (K=391c0cb3)
      block=0 i=00 z=1.47 flips=116  (K=428a2f98)
      block=0 i=53 z=1.38 flips=139  (K=4ed8aa4a)
      block=0 i=51 z=1.26 flips=138  (K=34b0bcb5)
      block=0 i=08 z=1.14 flips=137  (K=d807aa98)
    
    dna_2bit_packed:
      block=0 i=43 z=2.22 flips=110  (K=c76c51a3)
      block=0 i=58 z=1.88 flips=143  (K=84c87814)
      block=0 i=63 z=1.63 flips=141  (K=c67178f2)
      block=0 i=44 z=1.47 flips=116  (K=d192e819)
      block=0 i=48 z=1.38 flips=139  (K=19a4c116)
      block=0 i=50 z=1.38 flips=139  (K=2748774c)
    
    utf8_sentence:
      block=0 i=23 z=2.47 flips=108  (K=76f988da)
      block=0 i=22 z=2.34 flips=109  (K=5cb0a9dc)
      block=0 i=53 z=1.88 flips=143  (K=4ed8aa4a)
      block=0 i=56 z=1.88 flips=143  (K=748f82ee)
      block=0 i=24 z=1.84 flips=113  (K=983e5152)
      block=0 i=25 z=1.84 flips=113  (K=a831c66d)
    
    


    
![png](output_22_1.png)
    



    
![png](output_22_2.png)
    


    
    assembly (head-ish):
    
    PROJECT   pad+frame
    PIN       init H0..H7
    SYNC      block tick
    REFLECT   block density
    FOLD      schedule W0..W63
    PIN       load work regs
    GATE      round gates (x64)
    BRANCH    round update (x64)
    LEAK      chaining add
    COLLAPSE  final digest bytes
    VERIFY    hashlib compare
    


```python
# Nexus ISA SHA-256 tracer (single-cell, drop-in)
import hashlib, math, random, statistics
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any

# ----------------------------
# SHA-256 constants
# ----------------------------
K = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]
H0 = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]

MASK32 = 0xFFFFFFFF

def rotr(x, n): return ((x >> n) | ((x << (32-n)) & MASK32)) & MASK32
def shr(x, n): return (x >> n) & MASK32

def ch(x,y,z): return (x & y) ^ ((~x) & z)
def maj(x,y,z): return (x & y) ^ (x & z) ^ (y & z)

def big_sigma0(x): return rotr(x,2) ^ rotr(x,13) ^ rotr(x,22)
def big_sigma1(x): return rotr(x,6) ^ rotr(x,11) ^ rotr(x,25)
def small_sigma0(x): return rotr(x,7) ^ rotr(x,18) ^ shr(x,3)
def small_sigma1(x): return rotr(x,17) ^ rotr(x,19) ^ shr(x,10)

def u32(x): return x & MASK32

def hamming32(a, b):
    return (a ^ b).bit_count()

def hamming256(state_a, state_b):
    # state: 8x32-bit
    return sum(hamming32(state_a[i], state_b[i]) for i in range(8))

def pad_sha256(msg: bytes) -> bytes:
    ml = len(msg) * 8
    out = msg + b'\x80'
    while (len(out) % 64) != 56:
        out += b'\x00'
    out += ml.to_bytes(8, 'big')
    return out

def words_from_block(block64: bytes) -> List[int]:
    return [int.from_bytes(block64[i:i+4], 'big') for i in range(0,64,4)]

# ----------------------------
# Nexus-ish labeling (EDDY/HOT/COLD) — configurable thresholds
# ----------------------------
@dataclass
class GateConfig:
    z_cold: float = 0.30
    z_hot: float  = 1.60
    # sim is 1 - flips/256 (so ~0.5 random, higher = "less change")
    sim_hot_max: float = 0.55     # HOT = big shock, not a gentle drift
    sim_cold_min: float = 0.48    # COLD = low z and not too chaotic
    use_p: bool = True

def p_from_z(z: float) -> float:
    # smooth monotone map 0..1
    return 1.0 - math.exp(-max(0.0, z))

def label_round(z: float, sim: float, cfg: GateConfig) -> str:
    if z <= cfg.z_cold and sim >= cfg.sim_cold_min:
        return "COLD"
    if z >= cfg.z_hot and sim <= cfg.sim_hot_max:
        return "HOT"
    return "EDDY"

# ----------------------------
# Trace + compression
# ----------------------------
@dataclass
class RoundObs:
    block: int
    i: int
    flips: int
    z: float
    p: float
    sim: float
    k: int

@dataclass
class TraceResult:
    ok: bool
    digest: str
    blocks: int
    z_mean: float
    z_95: float
    flips_mean: float
    label_pct: Dict[str,float]
    rounds: List[RoundObs]
    ops: List[Tuple[str,str]]

def sha256_trace(payload: bytes, mu: float, sigma: float, cfg: GateConfig) -> TraceResult:
    ops: List[Tuple[str,str]] = []
    ops.append(("PROJECT","pad+frame"))

    msg = pad_sha256(payload)
    blocks = len(msg)//64

    H = H0.copy()
    ops.append(("PIN","init H0..H7"))

    all_rounds: List[RoundObs] = []
    label_counts = {"EDDY":0,"HOT":0,"COLD":0}

    for b in range(blocks):
        ops.append(("SYNC",f"block tick b={b}"))
        block = msg[b*64:(b+1)*64]
        W = words_from_block(block)
        # REFLECT: simple density proxy (popcount / bits)
        density = sum(w.bit_count() for w in W) / (16*32)
        ops.append(("REFLECT",f"block density={density:.4f}"))

        # FOLD: expand schedule
        for i in range(16,64):
            W.append(u32(small_sigma1(W[i-2]) + W[i-7] + small_sigma0(W[i-15]) + W[i-16]))
        ops.append(("FOLD","schedule W0..W63"))

        a,b_,c,d,e,f,g,h = H
        ops.append(("PIN","load work regs"))

        prev_state = [a,b_,c,d,e,f,g,h]
        init_state = prev_state[:]  # for sim0 if you ever want it

        for i in range(64):
            ops.append(("GATE",f"block {b} round gates i={i:02d}"))

            t1 = u32(h + big_sigma1(e) + ch(e,f,g) + K[i] + W[i])
            t2 = u32(big_sigma0(a) + maj(a,b_,c))
            h = g
            g = f
            f = e
            e = u32(d + t1)
            d = c
            c = b_
            b_ = a
            a = u32(t1 + t2)

            cur_state = [a,b_,c,d,e,f,g,h]
            flips = hamming256(prev_state, cur_state)
            z = abs(flips - mu) / (sigma if sigma > 1e-9 else 1.0)
            sim = 1.0 - (flips / 256.0)
            p = p_from_z(z) if cfg.use_p else float("nan")
            lab = label_round(z, sim, cfg)
            label_counts[lab] += 1

            all_rounds.append(RoundObs(block=b, i=i, flips=flips, z=z, p=p, sim=sim, k=K[i]))

            ops.append(("BRANCH",f"block {b} update | i={i:02d} {lab} p={p:.2f} z={z:.2f} flips={flips} sim={sim:.2f} (K={K[i]:08x})"))
            prev_state = cur_state

        # LEAK: chaining add
        H = [u32(H[j] + cur_state[j]) for j in range(8)]
        ops.append(("LEAK",f"block {b}: chaining add"))

    # COLLAPSE: final digest
    digest_bytes = b"".join(hh.to_bytes(4,'big') for hh in H)
    digest_hex = digest_bytes.hex()
    ops.append(("COLLAPSE","final digest bytes"))

    ref = hashlib.sha256(payload).hexdigest()
    ok = (ref == digest_hex)
    ops.append(("VERIFY","hashlib compare" if ok else "hashlib MISMATCH"))

    zs = [r.z for r in all_rounds]
    flips_list = [r.flips for r in all_rounds]
    z_mean = sum(zs)/len(zs) if zs else 0.0
    z_95 = sorted(zs)[int(0.95*(len(zs)-1))] if zs else 0.0
    flips_mean = sum(flips_list)/len(flips_list) if flips_list else 0.0

    total = sum(label_counts.values()) or 1
    label_pct = {k: v/total for k,v in label_counts.items()}

    return TraceResult(
        ok=ok, digest=digest_hex, blocks=blocks,
        z_mean=z_mean, z_95=z_95, flips_mean=flips_mean,
        label_pct=label_pct, rounds=all_rounds, ops=ops
    )

# ----------------------------
# GENLOCK calibration (μ, σ over flips distribution)
# ----------------------------
def genlock_calibrate(n_samples: int = 1500, seed: int = 12345, cfg: GateConfig = GateConfig()) -> Tuple[float,float,int]:
    rnd = random.Random(seed)
    flips_all = []
    # Use random 64-byte messages; each produces 64 rounds worth of flip observations
    for _ in range(n_samples):
        msg = bytes(rnd.getrandbits(8) for _ in range(64))
        # quick-run trace but only collect flips; skip storing ops for speed
        padded = pad_sha256(msg)
        H = H0.copy()
        block = padded[:64]
        W = words_from_block(block)
        for i in range(16,64):
            W.append(u32(small_sigma1(W[i-2]) + W[i-7] + small_sigma0(W[i-15]) + W[i-16]))
        a,b_,c,d,e,f,g,h = H
        prev_state = [a,b_,c,d,e,f,g,h]
        for i in range(64):
            t1 = u32(h + big_sigma1(e) + ch(e,f,g) + K[i] + W[i])
            t2 = u32(big_sigma0(a) + maj(a,b_,c))
            h,g,f,e,d,c,b_,a = g,f,e,u32(d + t1),c,b_,a,u32(t1 + t2)
            cur_state = [a,b_,c,d,e,f,g,h]
            flips_all.append(hamming256(prev_state, cur_state))
            prev_state = cur_state
    mu = statistics.mean(flips_all)
    sigma = statistics.pstdev(flips_all) if len(flips_all) > 1 else 1.0
    return mu, sigma, len(flips_all)

# ----------------------------
# Payload encoders
# ----------------------------
DNA_MAP = {'A':0,'C':1,'G':2,'T':3,'a':0,'c':1,'g':2,'t':3}

def hex_to_bytes(hexstr: str) -> bytes:
    hs = hexstr.strip().lower()
    if hs.startswith("0x"): hs = hs[2:]
    return bytes.fromhex(hs)

def dna_to_2bit_packed(seq: str) -> bytes:
    vals = [DNA_MAP[ch] for ch in seq if ch in DNA_MAP]
    out = bytearray()
    acc = 0
    bits = 0
    for v in vals:
        acc = (acc << 2) | (v & 0b11)
        bits += 2
        if bits == 8:
            out.append(acc & 0xFF)
            acc = 0
            bits = 0
    if bits:
        acc = acc << (8 - bits)
        out.append(acc & 0xFF)
    return bytes(out)

def dna_ascii_map(seq: str) -> bytes:
    # "ASCII map" version: keep 2-bit symbols, but store each as a nibble (0..3) in a byte stream
    # (different "surface", similar "verbs")
    vals = [DNA_MAP[ch] for ch in seq if ch in DNA_MAP]
    return bytes(vals)

# ----------------------------
# Similarity on signature vector
# ----------------------------
def cosine(a: List[float], b: List[float]) -> float:
    dot = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    if na == 0 or nb == 0: return 0.0
    return dot/(na*nb)

def signature(tr: TraceResult) -> List[float]:
    # minimal cross-domain signature: label proportions + z stats + flips_mean
    return [
        tr.label_pct.get("EDDY",0.0),
        tr.label_pct.get("HOT",0.0),
        tr.label_pct.get("COLD",0.0),
        tr.z_mean, tr.z_95, tr.flips_mean
    ]

def whack_a_mole(tr: TraceResult, topk: int = 6) -> List[RoundObs]:
    return sorted(tr.rounds, key=lambda r: r.z, reverse=True)[:topk]

# ----------------------------
# RUN DEMO
# ----------------------------
cfg = GateConfig(
    z_cold=0.30,
    z_hot=1.60,
    sim_hot_max=0.55,
    sim_cold_min=0.48,
)

# Calibrate GENLOCK (raise n_samples if you want tighter μ,σ)
mu, sigma, n = genlock_calibrate(n_samples=1200, seed=7, cfg=cfg)
print(f"GENLOCK baseline in-use: mu={mu:.3f} sigma={sigma:.3f} (n={n})\n")

payloads: Dict[str, Tuple[str, bytes]] = {}
payloads["abc_bytes"]      = ("bytes", b"abc")
payloads["abc_hex"]        = ("hex", hex_to_bytes("616263"))
payloads["dna_ascii_map"]  = ("dna", dna_ascii_map("ACGTACGTACGT"))
payloads["dna_2bit_packed"]= ("dna2bit", dna_to_2bit_packed("ACGTACGTACGT"))
payloads["utf8_sentence"]  = ("utf8", "whack-a-mole just popped into my head.".encode("utf-8"))

results: Dict[str, TraceResult] = {}
for name,(kind,payload) in payloads.items():
    tr = sha256_trace(payload, mu=mu, sigma=sigma, cfg=cfg)
    results[name] = tr

    print(f"=== {name} ({kind}) ===")
    print(f"ok? {tr.ok}")
    print(f"digest: {tr.digest}")
    print(f"blocks: {tr.blocks}")
    print(f"label%: { {k: round(v,3) for k,v in tr.label_pct.items()} }")
    print(f"z_mean: {tr.z_mean:.3f}  z_95: {tr.z_95:.3f}  flips_mean: {tr.flips_mean:.2f}")
    print("\nWHACK-A-MOLE (top z rounds):")
    for r in whack_a_mole(tr, topk=6):
        print(f"  block={r.block} i={r.i:02d} z={r.z:.2f} flips={r.flips:3d} sim={r.sim:.2f} (K={r.k:08x})")
    print("\nassembly (head-ish):")
    # show the first few ISA ops
    for op, desc in tr.ops[:12]:
        print(f"  {op:<8} {desc}")
    print("\nlast 10 ops:")
    for x in tr.ops[-10:]:
        print(f"  {x}")
    print("\n")

print("====================")
print("CROSS-DOMAIN SIMILARITY (cosine on signature vector)")
print("====================\n")

names = list(results.keys())
sigs = {k: signature(v) for k,v in results.items()}
for a in names:
    sims = []
    for b in names:
        if a == b: 
            continue
        sims.append((b, cosine(sigs[a], sigs[b])))
    sims.sort(key=lambda x: x[1], reverse=True)
    print(f"{a}:")
    for b, sc in sims:
        print(f"  {b:<18} {sc:.4f}")
    print()

```

    GENLOCK baseline in-use: mu=127.831 sigma=8.004 (n=76800)
    
    === abc_bytes (bytes) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.812, 'HOT': 0.016, 'COLD': 0.172}
    z_mean: 0.787  z_95: 1.603  flips_mean: 126.27
    
    WHACK-A-MOLE (top z rounds):
      block=0 i=04 z=1.98 flips=112 sim=0.56 (K=3956c25b)
      block=0 i=53 z=1.90 flips=143 sim=0.44 (K=4ed8aa4a)
      block=0 i=02 z=1.85 flips=113 sim=0.56 (K=b5c0fbcf)
      block=0 i=57 z=1.85 flips=113 sim=0.56 (K=78a5636f)
      block=0 i=00 z=1.60 flips=115 sim=0.55 (K=428a2f98)
      block=0 i=03 z=1.60 flips=115 sim=0.55 (K=e9b5dba5)
    
    assembly (head-ish):
      PROJECT  pad+frame
      PIN      init H0..H7
      SYNC     block tick b=0
      REFLECT  block density=0.0254
      FOLD     schedule W0..W63
      PIN      load work regs
      GATE     block 0 round gates i=00
      BRANCH   block 0 update | i=00 EDDY p=0.80 z=1.60 flips=115 sim=0.55 (K=428a2f98)
      GATE     block 0 round gates i=01
      BRANCH   block 0 update | i=01 EDDY p=0.71 z=1.23 flips=118 sim=0.54 (K=71374491)
      GATE     block 0 round gates i=02
      BRANCH   block 0 update | i=02 EDDY p=0.84 z=1.85 flips=113 sim=0.56 (K=b5c0fbcf)
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.45 z=0.60 flips=123 sim=0.52 (K=90befffa)')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=a4506ceb)')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=bef9a3f7)')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.71 z=1.23 flips=118 sim=0.54 (K=c67178f2)')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === abc_hex (hex) ===
    ok? True
    digest: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    blocks: 1
    label%: {'EDDY': 0.812, 'HOT': 0.016, 'COLD': 0.172}
    z_mean: 0.787  z_95: 1.603  flips_mean: 126.27
    
    WHACK-A-MOLE (top z rounds):
      block=0 i=04 z=1.98 flips=112 sim=0.56 (K=3956c25b)
      block=0 i=53 z=1.90 flips=143 sim=0.44 (K=4ed8aa4a)
      block=0 i=02 z=1.85 flips=113 sim=0.56 (K=b5c0fbcf)
      block=0 i=57 z=1.85 flips=113 sim=0.56 (K=78a5636f)
      block=0 i=00 z=1.60 flips=115 sim=0.55 (K=428a2f98)
      block=0 i=03 z=1.60 flips=115 sim=0.55 (K=e9b5dba5)
    
    assembly (head-ish):
      PROJECT  pad+frame
      PIN      init H0..H7
      SYNC     block tick b=0
      REFLECT  block density=0.0254
      FOLD     schedule W0..W63
      PIN      load work regs
      GATE     block 0 round gates i=00
      BRANCH   block 0 update | i=00 EDDY p=0.80 z=1.60 flips=115 sim=0.55 (K=428a2f98)
      GATE     block 0 round gates i=01
      BRANCH   block 0 update | i=01 EDDY p=0.71 z=1.23 flips=118 sim=0.54 (K=71374491)
      GATE     block 0 round gates i=02
      BRANCH   block 0 update | i=02 EDDY p=0.84 z=1.85 flips=113 sim=0.56 (K=b5c0fbcf)
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.45 z=0.60 flips=123 sim=0.52 (K=90befffa)')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=a4506ceb)')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=bef9a3f7)')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.71 z=1.23 flips=118 sim=0.54 (K=c67178f2)')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === dna_ascii_map (dna) ===
    ok? True
    digest: 5252677269f32b37e5c98cc77adbb102f5155aac869f0c0d6a5ff4600626fa17
    blocks: 1
    label%: {'EDDY': 0.578, 'HOT': 0.016, 'COLD': 0.406}
    z_mean: 0.517  z_95: 1.270  flips_mean: 129.55
    
    WHACK-A-MOLE (top z rounds):
      block=0 i=50 z=1.77 flips=142 sim=0.45 (K=2748774c)
      block=0 i=52 z=1.52 flips=140 sim=0.45 (K=391c0cb3)
      block=0 i=00 z=1.48 flips=116 sim=0.55 (K=428a2f98)
      block=0 i=53 z=1.40 flips=139 sim=0.46 (K=4ed8aa4a)
      block=0 i=51 z=1.27 flips=138 sim=0.46 (K=34b0bcb5)
      block=0 i=08 z=1.15 flips=137 sim=0.46 (K=d807aa98)
    
    assembly (head-ish):
      PROJECT  pad+frame
      PIN      init H0..H7
      SYNC     block tick b=0
      REFLECT  block density=0.0293
      FOLD     schedule W0..W63
      PIN      load work regs
      GATE     block 0 round gates i=00
      BRANCH   block 0 update | i=00 EDDY p=0.77 z=1.48 flips=116 sim=0.55 (K=428a2f98)
      GATE     block 0 round gates i=01
      BRANCH   block 0 update | i=01 EDDY p=0.52 z=0.73 flips=122 sim=0.52 (K=71374491)
      GATE     block 0 round gates i=02
      BRANCH   block 0 update | i=02 COLD p=0.20 z=0.23 flips=126 sim=0.51 (K=b5c0fbcf)
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 COLD p=0.14 z=0.15 flips=129 sim=0.50 (K=90befffa)')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.45 z=0.60 flips=123 sim=0.52 (K=a4506ceb)')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 COLD p=0.02 z=0.02 flips=128 sim=0.50 (K=bef9a3f7)')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 COLD p=0.24 z=0.27 flips=130 sim=0.49 (K=c67178f2)')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === dna_2bit_packed (dna2bit) ===
    ok? True
    digest: 8411e4357064fb6fbd9e41a70c1318cc8fe0ce87bcb25ef0d737a4ebf5f40128
    blocks: 1
    label%: {'EDDY': 0.719, 'HOT': 0.031, 'COLD': 0.25}
    z_mean: 0.728  z_95: 1.395  flips_mean: 128.98
    
    WHACK-A-MOLE (top z rounds):
      block=0 i=43 z=2.23 flips=110 sim=0.57 (K=c76c51a3)
      block=0 i=58 z=1.90 flips=143 sim=0.44 (K=84c87814)
      block=0 i=63 z=1.65 flips=141 sim=0.45 (K=c67178f2)
      block=0 i=44 z=1.48 flips=116 sim=0.55 (K=d192e819)
      block=0 i=48 z=1.40 flips=139 sim=0.46 (K=19a4c116)
      block=0 i=50 z=1.40 flips=139 sim=0.46 (K=2748774c)
    
    assembly (head-ish):
      PROJECT  pad+frame
      PIN      init H0..H7
      SYNC     block tick b=0
      REFLECT  block density=0.0293
      FOLD     schedule W0..W63
      PIN      load work regs
      GATE     block 0 round gates i=00
      BRANCH   block 0 update | i=00 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=428a2f98)
      GATE     block 0 round gates i=01
      BRANCH   block 0 update | i=01 EDDY p=0.59 z=0.90 flips=135 sim=0.47 (K=71374491)
      GATE     block 0 round gates i=02
      BRANCH   block 0 update | i=02 COLD p=0.02 z=0.02 flips=128 sim=0.50 (K=b5c0fbcf)
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.75 z=1.40 flips=139 sim=0.46 (K=90befffa)')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.75 z=1.40 flips=139 sim=0.46 (K=a4506ceb)')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.64 z=1.02 flips=136 sim=0.47 (K=bef9a3f7)')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 HOT p=0.81 z=1.65 flips=141 sim=0.45 (K=c67178f2)')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    === utf8_sentence (utf8) ===
    ok? True
    digest: 441f54e54521e885af7d1ef2617e132b078f7c3fb2d2bbacbd1d5d39bd6d5f67
    blocks: 1
    label%: {'EDDY': 0.625, 'HOT': 0.109, 'COLD': 0.266}
    z_mean: 0.815  z_95: 1.978  flips_mean: 129.30
    
    WHACK-A-MOLE (top z rounds):
      block=0 i=07 z=2.27 flips=146 sim=0.43 (K=ab1c5ed5)
      block=0 i=42 z=2.27 flips=146 sim=0.43 (K=c24b8b70)
      block=0 i=62 z=2.10 flips=111 sim=0.57 (K=bef9a3f7)
      block=0 i=30 z=1.98 flips=112 sim=0.56 (K=06ca6351)
      block=0 i=61 z=1.98 flips=112 sim=0.56 (K=a4506ceb)
      block=0 i=06 z=1.90 flips=143 sim=0.44 (K=923f82a4)
    
    assembly (head-ish):
      PROJECT  pad+frame
      PIN      init H0..H7
      SYNC     block tick b=0
      REFLECT  block density=0.2852
      FOLD     schedule W0..W63
      PIN      load work regs
      GATE     block 0 round gates i=00
      BRANCH   block 0 update | i=00 EDDY p=0.71 z=1.23 flips=118 sim=0.54 (K=428a2f98)
      GATE     block 0 round gates i=01
      BRANCH   block 0 update | i=01 COLD p=0.02 z=0.02 flips=128 sim=0.50 (K=71374491)
      GATE     block 0 round gates i=02
      BRANCH   block 0 update | i=02 COLD p=0.14 z=0.15 flips=129 sim=0.50 (K=b5c0fbcf)
    
    last 10 ops:
      ('BRANCH', 'block 0 update | i=60 EDDY p=0.67 z=1.10 flips=119 sim=0.54 (K=90befffa)')
      ('GATE', 'block 0 round gates i=61')
      ('BRANCH', 'block 0 update | i=61 EDDY p=0.86 z=1.98 flips=112 sim=0.56 (K=a4506ceb)')
      ('GATE', 'block 0 round gates i=62')
      ('BRANCH', 'block 0 update | i=62 EDDY p=0.88 z=2.10 flips=111 sim=0.57 (K=bef9a3f7)')
      ('GATE', 'block 0 round gates i=63')
      ('BRANCH', 'block 0 update | i=63 EDDY p=0.74 z=1.35 flips=117 sim=0.54 (K=c67178f2)')
      ('LEAK', 'block 0: chaining add')
      ('COLLAPSE', 'final digest bytes')
      ('VERIFY', 'hashlib compare')
    
    
    ====================
    CROSS-DOMAIN SIMILARITY (cosine on signature vector)
    ====================
    
    abc_bytes:
      abc_hex            1.0000
      dna_2bit_packed    1.0000
      utf8_sentence      1.0000
      dna_ascii_map      1.0000
    
    abc_hex:
      abc_bytes          1.0000
      dna_2bit_packed    1.0000
      utf8_sentence      1.0000
      dna_ascii_map      1.0000
    
    dna_ascii_map:
      dna_2bit_packed    1.0000
      abc_bytes          1.0000
      abc_hex            1.0000
      utf8_sentence      1.0000
    
    dna_2bit_packed:
      abc_bytes          1.0000
      abc_hex            1.0000
      dna_ascii_map      1.0000
      utf8_sentence      1.0000
    
    utf8_sentence:
      abc_bytes          1.0000
      abc_hex            1.0000
      dna_2bit_packed    1.0000
      dna_ascii_map      1.0000
    
    


```python
import numpy as np
import matplotlib.pyplot as plt

# Define the ring model for gravity emergence
L = 2 * np.pi  # Circumference of the ring
N = 256  # Number of points
x = np.linspace(0, L, N, endpoint=False)  # Position along the ring

# Mismatch field (deviation from SILR)
mismatch_field = 0.1 * np.sin(2 * np.pi * x / L)  # Simple sinusoidal mismatch

# Compute the mismatch charge density
rho = mismatch_field**2  # Square of the mismatch

# Solve Poisson's equation for potential using Fourier transform
rho_k = np.fft.fft(rho)
k = 2 * np.pi * np.fft.fftfreq(N, L/N)
phi_k = -rho_k / (k**2)
phi_k[0] = 0  # Set zero mean potential (no constant mismatch)
phi = np.fft.ifft(phi_k)  # Inverse Fourier to get the potential

# Compute the force field (negative gradient of potential)
force_field = -np.gradient(phi, L/N)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot the mismatch field
plt.subplot(3, 1, 1)
plt.plot(x, mismatch_field, label="Mismatch Field")
plt.title("Mismatch Field (Deviations from SILR)")
plt.xlabel("Position")
plt.ylabel("Mismatch")

# Plot the potential (phi)
plt.subplot(3, 1, 2)
plt.plot(x, phi, label="Potential (Φ)")
plt.title("Mismatch Potential (Solution of Poisson's Equation)")
plt.xlabel("Position")
plt.ylabel("Potential (Φ)")

# Plot the force field (gravity)
plt.subplot(3, 1, 3)
plt.plot(x, force_field, label="Force Field (F = -∇Φ)")
plt.title("Force Field (Gravitational Effects)")
plt.xlabel("Position")
plt.ylabel("Force (F)")

plt.tight_layout()
plt.show()

```

    C:\Users\Developer\AppData\Local\Temp\ipykernel_33544\2333101244.py:18: RuntimeWarning: divide by zero encountered in divide
      phi_k = -rho_k / (k**2)
    C:\Users\Developer\AppData\Local\Temp\ipykernel_33544\2333101244.py:18: RuntimeWarning: invalid value encountered in divide
      phi_k = -rho_k / (k**2)
    C:\Users\Developer\anaconda3\Lib\site-packages\matplotlib\cbook.py:1709: ComplexWarning: Casting complex values to real discards the imaginary part
      return math.isfinite(val)
    C:\Users\Developer\anaconda3\Lib\site-packages\matplotlib\cbook.py:1345: ComplexWarning: Casting complex values to real discards the imaginary part
      return np.asarray(x, float)
    


    
![png](output_24_1.png)
    



```python

```
