#!/usr/bin/env python3
"""
SHA-256 XRAY TOOL (safe instrumentation)
- Exact integer SHA-256 (no float math)
- Records full internal register state for every round
- Produces:
  * CSV trace (registers per round)
  * PNG plot (Hamming-weight waveform over rounds)
  * GIF animation (8x32 register bit-plane per round)

Usage:
  python sha256_xray_tool.py "hello"
  python sha256_xray_tool.py --hex 0000000000
"""
from __future__ import annotations
import argparse, struct, hashlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

MASK32 = 0xFFFFFFFF

def rotr(x: int, n: int) -> int:
    return ((x >> n) | (x << (32 - n))) & MASK32

def shr(x: int, n: int) -> int:
    return (x >> n) & MASK32

K = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298]

H0 = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225]

def Sigma0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sigma1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sigma0(x): return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
def sigma1(x): return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def Ch(x, y, z):  return (x & y) ^ (~x & z)
def Maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)

def pad_message(msg: bytes) -> bytes:
    ml = len(msg) * 8
    msg += b'\x80'
    msg += b'\x00' * ((56 - (len(msg) % 64)) % 64)
    msg += struct.pack(">Q", ml)
    return msg

def sha256_trace(msg: bytes):
    padded = pad_message(msg)
    h = H0[:]
    traces = []
    for bidx in range(0, len(padded), 64):
        block = padded[bidx:bidx+64]
        w = list(struct.unpack(">16I", block))
        for i in range(16, 64):
            w.append((w[i-16] + sigma0(w[i-15]) + w[i-7] + sigma1(w[i-2])) & MASK32)
        w_arr = np.array(w, dtype=np.uint32)

        a,b,c,d,e,f,g,hh = h
        state = np.zeros((65, 8), dtype=np.uint32)
        state[0] = np.array([a,b,c,d,e,f,g,hh], dtype=np.uint32)

        for t in range(64):
            T1 = (hh + Sigma1(e) + Ch(e,f,g) + K[t] + int(w_arr[t])) & MASK32
            T2 = (Sigma0(a) + Maj(a,b,c)) & MASK32
            hh = g
            g = f
            f = e
            e = (d + T1) & MASK32
            d = c
            c = b
            b = a
            a = (T1 + T2) & MASK32
            state[t+1] = np.array([a,b,c,d,e,f,g,hh], dtype=np.uint32)

        h = [(x + int(y)) & MASK32 for x,y in zip(h, state[64])]
        ham = np.array([sum(int(v).bit_count() for v in row) for row in state], dtype=np.int32)

        traces.append({"W": w_arr, "state": state, "hamming": ham, "block_index": bidx//64, "block": block})

    digest_hex = "".join(f"{x:08x}" for x in h)
    return digest_hex, traces

def bit_matrix_8x32(state_row):
    m = np.zeros((8, 32), dtype=np.uint8)
    for r in range(8):
        v = int(state_row[r])
        for b in range(32):
            m[r, b] = (v >> (31 - b)) & 1
    return m

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("message", help="message as UTF-8 text unless --hex is set")
    ap.add_argument("--hex", action="store_true", help="interpret message as hex bytes (no 0x prefix)")
    ap.add_argument("--block", type=int, default=0, help="which padded 512-bit block to visualize")
    ap.add_argument("--out_prefix", default="sha256_xray", help="output file prefix")
    args = ap.parse_args()

    msg = bytes.fromhex(args.message) if args.hex else args.message.encode("utf-8")

    digest_hex, traces = sha256_trace(msg)
    print("sha256:", digest_hex)
    print("hashlib_check:", hashlib.sha256(msg).hexdigest())
    if digest_hex != hashlib.sha256(msg).hexdigest():
        raise SystemExit("Mismatch vs hashlib; something is wrong.")

    if args.block < 0 or args.block >= len(traces):
        raise SystemExit(f"block index out of range (0..{len(traces)-1})")

    tr = traces[args.block]
    state = tr["state"]
    ham = tr["hamming"]
    reg_names = ["a","b","c","d","e","f","g","h"]

    # CSV trace
    rows = []
    for r in range(65):
        rec = {"round": r, "hamming_bits_total": int(ham[r])}
        for i,nm in enumerate(reg_names):
            rec[nm] = int(state[r,i])
        rows.append(rec)
    df = pd.DataFrame(rows)
    csv_path = f"{args.out_prefix}_trace_block{args.block}.csv"
    df.to_csv(csv_path, index=False)
    print("wrote", csv_path)

    # PNG waveform: total hamming
    plt.figure()
    plt.plot(df["round"], df["hamming_bits_total"])
    plt.xlabel("Round")
    plt.ylabel("Total 1-bits across a..h (0..256)")
    plt.title("SHA-256 X-ray: Hamming-weight waveform (single block)")
    png_path = f"{args.out_prefix}_hamming_block{args.block}.png"
    plt.savefig(png_path, dpi=160, bbox_inches="tight")
    plt.close()
    print("wrote", png_path)

    # GIF: 8x32 bit-plane animation
    frames = 65
    bit_frames = np.stack([bit_matrix_8x32(state[r]) for r in range(frames)], axis=0)

    fig = plt.figure()
    ax = plt.gca()
    im = ax.imshow(bit_frames[0], aspect="auto", interpolation="nearest")
    ax.set_yticks(range(8))
    ax.set_yticklabels(reg_names)
    ax.set_xticks([0, 7, 15, 23, 31])
    ax.set_xticklabels(["31", "24", "16", "8", "0"])
    ax.set_xlabel("Bit position (MSB→LSB)")

    def update(frame):
        im.set_data(bit_frames[frame])
        ax.set_title(f"SHA-256 X-ray: register bit-plane (round {frame})")
        return (im,)

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=120, blit=True)
    gif_path = f"{args.out_prefix}_bits_block{args.block}.gif"
    ani.save(gif_path, writer="pillow", fps=8)
    plt.close(fig)
    print("wrote", gif_path)

if __name__ == "__main__":
    main()
