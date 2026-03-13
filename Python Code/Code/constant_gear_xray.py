#!/usr/bin/env python3
"""
CONSTANT GEAR XRAY (waveform pipeline sandbox)
=============================================

This is NOT a preimage solver and not a cryptographic attack tool.
It's an instrument: take a byte-stream, run it through an 8-register, 64-step pipeline,
and XRAY the internal motion as bit-planes + Hamming-weight "waveforms".

Key idea:
- The "constants" act like a microcode schedule.
- A 64-hex "residue" (or any bytes) can be used as a *gear key* that permutes the schedule.
- Optionally, the schedule can "float": each step makes a tiny swap based on current state,
  like a phase-locked controller—without touching the global clock.

Outputs:
- trace CSV (a..h per step)
- hamming waveform PNG (8 curves)
- bitplane GIF (8x32 bits per step, blown up)

Usage:
  python constant_gear_xray.py --msg "NEXUS" --key-hex 52b7...ca03
  python constant_gear_xray.py --msg-hex 000102 --key "any string"
  python constant_gear_xray.py --pi-seed --key-hex <64 hex> --float
"""

from __future__ import annotations
import argparse, struct, hashlib, csv
from pathlib import Path
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# --- Base schedule (SHA-256 K) as a convenient, well-studied "ROM" ---
K_BASE = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
]

H_INIT = [
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
]

MASK32 = 0xFFFFFFFF

def rotr(x: int, n: int) -> int:
    return ((x >> n) | (x << (32 - n))) & MASK32

def shr(x: int, n: int) -> int:
    return (x >> n) & MASK32

def Sigma0(x: int) -> int: return rotr(x,2) ^ rotr(x,13) ^ rotr(x,22)
def Sigma1(x: int) -> int: return rotr(x,6) ^ rotr(x,11) ^ rotr(x,25)
def sigma0(x: int) -> int: return rotr(x,7) ^ rotr(x,18) ^ shr(x,3)
def sigma1(x: int) -> int: return rotr(x,17) ^ rotr(x,19) ^ shr(x,10)

def Ch(x: int, y: int, z: int) -> int:
    return (x & y) ^ (~x & z)

def Maj(x: int, y: int, z: int) -> int:
    return (x & y) ^ (x & z) ^ (y & z)

def pad_one_block(msg: bytes) -> bytes:
    """Pad to one 64-byte block.

    For XRAY purposes we allow any length:
    - if msg <= 55 bytes: standard one-block padding
    - if msg > 55 bytes: fold down to 55 bytes by XOR-wrapping (a controlled "cut"),
      then apply standard padding. This keeps the demo single-block and fully deterministic.
    """
    if len(msg) > 55:
        buf = bytearray(55)
        for i, b in enumerate(msg):
            buf[i % 55] ^= b
        msg = bytes(buf)

    ml = len(msg) * 8
    out = msg + b"\x80"
    out += b"\x00" * (56 - len(out))
    out += struct.pack(">Q", ml)
    assert len(out) == 64
    return out

def xorshift32(seed: int) -> int:
    x = seed & MASK32
    x ^= (x << 13) & MASK32
    x ^= (x >> 17) & MASK32
    x ^= (x << 5) & MASK32
    return x & MASK32

def seed_from_bytes(b: bytes) -> int:
    h = hashlib.sha256(b).digest()
    return int.from_bytes(h[:4], "big")

def permute_schedule(key: bytes) -> list[int]:
    sched = K_BASE.copy()
    s = seed_from_bytes(key)
    for i in range(len(sched)-1, 0, -1):
        s = xorshift32(s)
        j = s % (i+1)
        sched[i], sched[j] = sched[j], sched[i]
    return sched

def message_schedule(block: bytes) -> list[int]:
    w = list(struct.unpack(">16I", block)) + [0]*48
    for i in range(16, 64):
        w[i] = (w[i-16] + sigma0(w[i-15]) + w[i-7] + sigma1(w[i-2])) & MASK32
    return w

def step_round(state: tuple[int,int,int,int,int,int,int,int], k: int, w: int) -> tuple[int,int,int,int,int,int,int,int]:
    a,b,c,d,e,f,g,h = state
    t1 = (h + Sigma1(e) + Ch(e,f,g) + k + w) & MASK32
    t2 = (Sigma0(a) + Maj(a,b,c)) & MASK32
    a2 = (t1 + t2) & MASK32
    e2 = (d + t1) & MASK32
    return (a2, a, b, c, e2, e, f, g)

def run_pipeline(msg: bytes, key: bytes, floating: bool=False) -> tuple[list[tuple[int,...]], bytes]:
    block = pad_one_block(msg)
    w = message_schedule(block)

    sched = permute_schedule(key)
    a,b,c,d,e,f,g,h = H_INIT
    trace = [(a,b,c,d,e,f,g,h)]

    s = seed_from_bytes(key)

    for i in range(64):
        k = sched[i]
        if floating:
            meas = (a ^ e ^ ((i+1) * 0x9e3779b9)) & MASK32
            s = xorshift32(s ^ meas)
            j = s % 64
            sched[i], sched[j] = sched[j], sched[i]
            k = sched[i]

        a,b,c,d,e,f,g,h = step_round((a,b,c,d,e,f,g,h), k, w[i])
        trace.append((a,b,c,d,e,f,g,h))

    residue = b"".join(struct.pack(">I", x) for x in trace[-1])
    return trace, residue

def hamming32(x: int) -> int:
    return int(x).bit_count()

def render_hamming(trace: list[tuple[int,...]], out_png: Path) -> None:
    rounds = list(range(len(trace)))
    series = list(zip(*trace))
    plt.figure(figsize=(10,4))
    for reg in series:
        plt.plot(rounds, [hamming32(x) for x in reg])
    plt.xlabel("step")
    plt.ylabel("popcount (bits set)")
    plt.title("Register Hamming-weight waveforms (8 registers)")
    plt.tight_layout()
    plt.savefig(out_png, dpi=200)
    plt.close()

def render_bitplane_gif(trace: list[tuple[int,...]], out_gif: Path, scale: int=4, pad: int=2) -> None:
    frames = []
    for st in trace:
        img = Image.new("L", ((32*scale)+(2*pad), (8*scale)+(2*pad)), 255)
        dr = ImageDraw.Draw(img)
        for r, val in enumerate(st):
            for c in range(32):
                bit = (val >> (31-c)) & 1
                x0 = pad + c*scale
                y0 = pad + r*scale
                if bit:
                    dr.rectangle([x0, y0, x0+scale-1, y0+scale-1], fill=0)
        frames.append(img.convert("P"))
    frames[0].save(out_gif, save_all=True, append_images=frames[1:], duration=60, loop=0)

def write_csv(trace: list[tuple[int,...]], out_csv: Path) -> None:
    with out_csv.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["step","a","b","c","d","e","f","g","h"])
        for i, st in enumerate(trace):
            w.writerow([i, *[f"0x{x:08x}" for x in st]])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--msg", type=str, default="", help="message as text")
    ap.add_argument("--msg-hex", type=str, default=None, help="message as hex bytes")
    ap.add_argument("--key", type=str, default=None, help="gear key as text")
    ap.add_argument("--key-hex", type=str, default=None, help="gear key as hex bytes")
    ap.add_argument("--float", action="store_true", help="enable floating microcode")
    ap.add_argument("--pi-seed", action="store_true", help="use the 64-digit pi seed as msg")
    ap.add_argument("--out", type=str, default="gear_xray", help="output prefix")
    args = ap.parse_args()

    if args.pi_seed:
        msg = b"1415926525897922846264882795028841971699975105820974944592078164"
    elif args.msg_hex:
        msg = bytes.fromhex(args.msg_hex)
    else:
        msg = args.msg.encode("utf-8")

    if args.key_hex:
        key = bytes.fromhex(args.key_hex)
    elif args.key is not None:
        key = args.key.encode("utf-8")
    else:
        key = hashlib.sha256(msg).digest()

    trace, residue = run_pipeline(msg, key, floating=args.float)

    prefix = Path(args.out)
    out_csv = prefix.with_suffix(".csv")
    out_png = prefix.with_suffix(".png")
    out_gif = prefix.with_suffix(".gif")

    write_csv(trace, out_csv)
    render_hamming(trace, out_png)
    render_bitplane_gif(trace, out_gif)

    print("wrote:", out_csv)
    print("wrote:", out_png)
    print("wrote:", out_gif)
    print("residue32 (hex):", residue[:32].hex())

if __name__ == "__main__":
    main()
