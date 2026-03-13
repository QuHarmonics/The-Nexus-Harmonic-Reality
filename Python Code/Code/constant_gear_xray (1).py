#!/usr/bin/env python3
"""
CONSTANT-GEAR XRAY (safe instrumentation)
========================================
Not a solver. No preimage search. This is an "X-ray" view of a 64-step, 8-register pipeline.

It compares:
- fixed gear: standard SHA-256 K[0..63]
- floating gear: K permuted deterministically from a key (default: the input bytes)

Outputs (in the working directory):
  constant_gear_fixed_trace.csv
  constant_gear_float_trace.csv
  constant_gear_wave_compare.png
  constant_gear_fixed_bits.gif
  constant_gear_float_bits.gif

Usage:
  python constant_gear_xray.py "hello"
  python constant_gear_xray.py --hexbytes 00ff10
  python constant_gear_xray.py "msg" --keyhex <hex>
"""
from __future__ import annotations
import argparse, struct, hashlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

MASK32 = 0xFFFFFFFF

def rotr(x: int, n: int) -> int:
    return ((x >> n) | (x << (32 - n))) & MASK32

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

def pad_sha256(msg: bytes) -> bytes:
    ml = len(msg) * 8
    msg += b'\x80'
    while (len(msg) % 64) != 56:
        msg += b'\x00'
    msg += struct.pack('>Q', ml)
    return msg

def schedule(W16: list[int]) -> list[int]:
    W = W16[:]
    for i in range(16, 64):
        s0 = rotr(W[i-15], 7) ^ rotr(W[i-15], 18) ^ (W[i-15] >> 3)
        s1 = rotr(W[i-2], 17) ^ rotr(W[i-2], 19) ^ (W[i-2] >> 10)
        W.append((W[i-16] + s0 + W[i-7] + s1) & MASK32)
    return W

def words_from_block(block: bytes) -> list[int]:
    return list(struct.unpack('>16I', block))

def compress_trace_oneblock(msg: bytes, K_use: list[int]) -> tuple[pd.DataFrame, bytes]:
    msg_p = pad_sha256(msg)
    block = msg_p[:64]  # single-block focus
    W = schedule(words_from_block(block))
    a,b,c,d,e,f,g,hv = H0
    rows = []
    for i in range(64):
        S1 = rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = (hv + S1 + ch + K_use[i] + W[i]) & MASK32
        S0 = rotr(a,2) ^ rotr(a,13) ^ rotr(a,22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = (S0 + maj) & MASK32
        hv = g
        g = f
        f = e
        e = (d + temp1) & MASK32
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & MASK32
        rows.append({"round": i, "a": a,"b": b,"c": c,"d": d,"e": e,"f": f,"g": g,"h": hv})
    # feedforward (for completeness)
    h_final = [(x+y) & MASK32 for x,y in zip(H0, [a,b,c,d,e,f,g,hv])]
    digest = b"".join(struct.pack(">I", x) for x in h_final)
    return pd.DataFrame(rows), digest

def popcount32(x: int) -> int:
    return int(x).bit_count()

def total_hw(df: pd.DataFrame) -> list[int]:
    out = []
    for _, r in df.iterrows():
        out.append(sum(popcount32(int(r[k])) for k in "abcdefgh"))
    return out

def permute_K(key_bytes: bytes) -> list[int]:
    seed = int.from_bytes(hashlib.sha256(key_bytes).digest()[:8], "big", signed=False)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(64)
    return [K[i] for i in perm]

def bitplane_image(words: list[int], scale: int = 12, pad: int = 10) -> Image.Image:
    # 8x32 -> scaled grayscale image
    w, h = 32, 8
    img = Image.new("L", (w*scale + 2*pad, h*scale + 2*pad), 255)
    draw = ImageDraw.Draw(img)
    for r, word in enumerate(words):
        for b in range(32):
            bit = (word >> (31-b)) & 1
            if bit:
                x0 = pad + b*scale
                y0 = pad + r*scale
                draw.rectangle([x0, y0, x0+scale-1, y0+scale-1], fill=0)
    return img

def save_bitplane_gif(df: pd.DataFrame, out_gif: str, label: str):
    frames = []
    for _, r in df.iterrows():
        words = [int(r[k]) for k in "abcdefgh"]
        frames.append(bitplane_image(words))
    # set duration so it "reads" like a clock
    frames[0].save(out_gif, save_all=True, append_images=frames[1:], duration=120, loop=0)

def save_wave_compare(df0: pd.DataFrame, df1: pd.DataFrame, out_png: str):
    y0 = total_hw(df0)
    y1 = total_hw(df1)
    x = list(range(len(y0)))
    plt.figure(figsize=(10,4))
    plt.plot(x, y0, label="fixed gear")
    plt.plot(x, y1, label="floating gear")
    plt.xlabel("round")
    plt.ylabel("total 1-bits across a..h (0..256)")
    plt.title("Waveform compare: fixed vs floating constant schedule")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=160)
    plt.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("text", nargs="?", default="1415926525897922846264882795028841971699975105820974944592078164")
    ap.add_argument("--hexbytes", action="store_true", help="parse input as hex into raw bytes")
    ap.add_argument("--keyhex", default="", help="hex to derive floating schedule (default: input bytes)")
    ap.add_argument("--outprefix", default="constant_gear")
    args = ap.parse_args()

    if args.hexbytes:
        msg = bytes.fromhex(args.text)
    else:
        msg = args.text.encode("utf-8")

    key_bytes = bytes.fromhex(args.keyhex) if args.keyhex else msg

    df_fixed, dig_fixed = compress_trace_oneblock(msg, K)
    df_float, dig_float = compress_trace_oneblock(msg, permute_K(key_bytes))

    pref = args.outprefix
    df_fixed.to_csv(f"{pref}_fixed_trace.csv", index=False)
    df_float.to_csv(f"{pref}_float_trace.csv", index=False)
    save_wave_compare(df_fixed, df_float, f"{pref}_wave_compare.png")
    save_bitplane_gif(df_fixed, f"{pref}_fixed_bits.gif", "fixed")
    save_bitplane_gif(df_float, f"{pref}_float_bits.gif", "float")

    print("fixed digest:", dig_fixed.hex())
    print("float digest:", dig_float.hex())
    print("wrote outputs with prefix:", pref)

if __name__ == "__main__":
    main()
