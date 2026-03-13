# nexus_sha_live_fft.py
# Live FFT / spectrogram diagnostics for "K[i] excitation" as SHA-256 blocks stream through.
# Measures carry/borrow/toggle proxies of K-constants' interaction with the state, then FFTs across blocks.
#
# Usage (example):
#   python nexus_sha_live_fft.py --N 4096 --cycles 17 --mode carry
#
# Notes:
# - K[i] is constant; what changes with data is carry propagation and bit toggling when +K[i] is applied.
# - Your current "H injection" (phi += pi/9) is a global gauge rotation in epicycles. Here, we measure *interaction*.
#
import argparse, struct
import numpy as np
import matplotlib.pyplot as plt
from math import pi

MASK32 = 0xFFFFFFFF
def rotr(x, n): return ((x >> n) | ((x << (32 - n)) & MASK32)) & MASK32
def shr(x, n): return (x >> n) & MASK32
def Ch(x, y, z): return (x & y) ^ (~x & z)
def Maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def Sigma0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sigma1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sigma0(x): return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)
def sigma1(x): return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

K = [1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298]
IV = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225]

def msg_schedule(block64: bytes):
    w = list(struct.unpack(">16I", block64))
    for i in range(16, 64):
        w.append((sigma1(w[i-2]) + w[i-7] + sigma0(w[i-15]) + w[i-16]) & MASK32)
    return w

def carry_count_add32(x, y):
    carry = 0
    carries = 0
    for b in range(32):
        xb = (x >> b) & 1
        yb = (y >> b) & 1
        new_carry = (xb & yb) | (carry & (xb ^ yb))
        if new_carry:
            carries += 1
        carry = 1 if new_carry else 0
    return carries

def borrow_count_sub32(x, y):
    borrow = 0
    borrows = 0
    for b in range(32):
        xb = (x >> b) & 1
        yb = (y >> b) & 1
        need = (xb - borrow) < yb
        if need:
            borrows += 1
        borrow = 1 if need else 0
    return borrows

def popcount32(x): return int(x & MASK32).bit_count()

def sha256_excitation(block64: bytes):
    W = msg_schedule(block64)
    a,b,c,d,e,f,g,h = IV
    carryK = np.zeros(64, dtype=np.float64)
    borrowK = np.zeros(64, dtype=np.float64)
    toggleT1 = np.zeros(64, dtype=np.float64)
    for i in range(64):
        preK = (h + Sigma1(e) + Ch(e,f,g) + W[i]) & MASK32
        T1 = (preK + K[i]) & MASK32
        T2 = (Sigma0(a) + Maj(a,b,c)) & MASK32
        carryK[i] = carry_count_add32(preK, K[i])
        borrowK[i] = borrow_count_sub32(T1, K[i])
        toggleT1[i] = popcount32(T1 ^ preK)
        h,g,f,e,d,c,b,a = g,f,e,(d + T1) & MASK32,c,b,a,(T1 + T2) & MASK32
    return carryK, borrowK, toggleT1

def make_blocks(N, cycles, amp=0.95):
    blocks = []
    input_series = np.zeros(N, dtype=np.float64)
    for j in range(N):
        phase = 2*pi*cycles*j/N
        val = int(((np.sin(phase)*amp + 1.0)/2.0) * (2**32 - 1)) & MASK32
        input_series[j] = val / (2**32 - 1)
        blocks.append(struct.pack(">I", val) + b"\x00"*(64-4))
    return blocks, input_series

def rfft_mag(x):
    X = np.fft.rfft(x - np.mean(x))
    return np.abs(X)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=2048)
    ap.add_argument("--cycles", type=int, default=11)
    ap.add_argument("--mode", choices=["carry","borrow","toggle"], default="carry")
    args = ap.parse_args()

    blocks, input_series = make_blocks(args.N, args.cycles)

    exc = np.zeros((64, args.N), dtype=np.float64)
    for j, blk in enumerate(blocks):
        carryK, borrowK, toggleT1 = sha256_excitation(blk)
        if args.mode == "carry":   exc[:, j] = carryK
        if args.mode == "borrow":  exc[:, j] = borrowK
        if args.mode == "toggle":  exc[:, j] = toggleT1

    freq_bins = np.fft.rfftfreq(args.N, d=1.0)
    input_spec = rfft_mag(input_series)
    dom_bin = 1 + int(np.argmax(input_spec[1:]))
    dom_freq = freq_bins[dom_bin]

    spec = np.zeros((64, len(freq_bins)))
    for i in range(64):
        spec[i,:] = rfft_mag(exc[i,:])

    # Input spectrum
    plt.figure(figsize=(10,4))
    plt.plot(freq_bins[1:], input_spec[1:])
    plt.axvline(dom_freq, linestyle="--")
    plt.title("Input stream FFT magnitude")
    plt.xlabel("Frequency (cycles per block index)")
    plt.ylabel("Magnitude")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Excitation heatmap
    plt.figure(figsize=(10,5))
    img = np.log1p(spec[:,1:])
    plt.imshow(img, aspect="auto", origin="lower",
               extent=[freq_bins[1], freq_bins[-1], 0, 63])
    plt.title(f"Per-round excitation FFT (mode={args.mode})")
    plt.xlabel("Frequency (cycles per block index)")
    plt.ylabel("Round index i")
    plt.colorbar(label="log(1 + |FFT|)")
    plt.tight_layout()
    plt.show()

    # Response at dominant input frequency
    resp = spec[:, dom_bin]
    plt.figure(figsize=(10,4))
    plt.plot(resp)
    plt.title(f"Round-wise response at dominant input frequency (f ≈ {dom_freq:.4f})")
    plt.xlabel("Round index i")
    plt.ylabel("Magnitude at dom bin")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
