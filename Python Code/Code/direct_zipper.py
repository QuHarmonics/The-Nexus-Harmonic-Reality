#!/usr/bin/env python3
"""
DIRECT ZIPPER
hash ⊕ constants = search_space

The hash IS half the zipper.
The constants ARE the other half.
XOR meshes them.
"""

import hashlib
import numpy as np
import math

H = math.pi / 9

# Constants as bytes
H_INIT_BYTES = bytes([
    0x6a, 0x09, 0xe6, 0x67, 0xbb, 0x67, 0xae, 0x85,
    0x3c, 0x6e, 0xf3, 0x72, 0xa5, 0x4f, 0xf5, 0x3a,
    0x51, 0x0e, 0x52, 0x7f, 0x9b, 0x05, 0x68, 0x8c,
    0x1f, 0x83, 0xd9, 0xab, 0x5b, 0xe0, 0xcd, 0x19
])

K_BYTES = bytes([
    0x42, 0x8a, 0x2f, 0x98, 0x71, 0x37, 0x44, 0x91,
    0xb5, 0xc0, 0xfb, 0xcf, 0xe9, 0xb5, 0xdb, 0xa5,
    0x39, 0x56, 0xc2, 0x5b, 0x59, 0xf1, 0x11, 0xf1,
    0x92, 0x3f, 0x82, 0xa4, 0xab, 0x1c, 0x5e, 0xd5
])

def direct_unfold(hash_bytes):
    """hash ⊕ H_INIT ⊕ K = unfolded"""
    out = bytearray(32)
    for i in range(32):
        out[i] = hash_bytes[i] ^ H_INIT_BYTES[i] ^ K_BYTES[i]
    return bytes(out)

def unfold(msg):
    h = hashlib.sha256(msg.encode()).digest()
    u = direct_unfold(h)
    return h, u

print("DIRECT ZIPPER: hash ⊕ constants")
print("=" * 50)

tests = ['NEXUS', 'H = pi/9', 'Dean', 'test', 'hello', 'a', 'b']

for msg in tests:
    h, u = unfold(msg)
    # Try to decode as ASCII
    printable = ''.join(chr(b) if 32 <= b < 127 else '.' for b in u)
    norm = [b/255 for b in u]
    print(f"\n'{msg}'")
    print(f"  hash:   {h.hex()[:16]}")
    print(f"  unfold: {u.hex()[:16]}")
    print(f"  ascii:  {printable[:16]}")
    print(f"  mean:   {np.mean(norm):.4f}")

# ============================================================
print("\n" + "=" * 50)
print("CAN WE RECOVER MESSAGE STRUCTURE?")

# XOR is reversible: if unfold = hash ⊕ const
# then hash = unfold ⊕ const
# and if we know the message pattern...

def fold_back(unfolded):
    """unfold ⊕ constants = hash"""
    out = bytearray(32)
    for i in range(32):
        out[i] = unfolded[i] ^ H_INIT_BYTES[i] ^ K_BYTES[i]
    return bytes(out)

# Test round trip
msg = "NEXUS"
h1, u1 = unfold(msg)
h2 = fold_back(u1)
print(f"\nRound trip test:")
print(f"  Original hash:  {h1.hex()[:32]}")
print(f"  Recovered hash: {h2.hex()[:32]}")
print(f"  Match: {h1 == h2}")

# ============================================================
print("\n" + "=" * 50)
print("H-SIGNATURE IN UNFOLDED SPACE")

attractors = [0, H, 0.5, 1-H, 1.0]
for msg in tests[:4]:
    _, u = unfold(msg)
    norm = [b/255 for b in u]
    near = sum(1 for v in norm if min(abs(v-a) for a in attractors) < 0.1)
    print(f"'{msg}': mean={np.mean(norm):.3f}, near_H={near}/32")

# ============================================================
print("\n" + "=" * 50)
print("THE INSIGHT")
print("""
hash ⊕ constants = search_space

Fold:   message → SHA → hash
Unfold: hash ⊕ constants = search_space

The search_space is where the message LIVES.
It's not the message. It's the SPACE containing it.

To find message: search within (hash ⊕ constants) space
The constants BOUND the search.
The hash LOCATES within those bounds.

P(2)NP: Two halves of same zipper.
""")
