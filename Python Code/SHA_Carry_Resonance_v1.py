#!/usr/bin/env python3
"""
SHA_Carry_Resonance_v1.py

Protocol (verbs):
  GENERATE (random vs patterned blocks)
  COMPRESS (SHA-256, count carry events in modular adds)
  COMPARE (stats + effect sizes)
  OUTPUT (CSV + histogram)

Notes:
- This does NOT claim cryptographic weakness.
- It tests the SIDE-CHANNEL proxy: carry activity as a "stress/effort" trace.
"""

import argparse, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import hashlib

K = np.array([
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
], dtype=np.uint32)

H0 = np.array([
    0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
    0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19
], dtype=np.uint32)

MASK32 = np.uint32(0xFFFFFFFF)

def rotr(x, n):
    return np.uint32(((x >> n) | (x << np.uint32(32 - n))) & MASK32)

def shr(x, n):
    return np.uint32(x >> n)

def Sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def Sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def sigma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ shr(x, 3)

def sigma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ shr(x, 10)

def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def add32_carry(a, b):
    a = int(np.uint32(a)); b = int(np.uint32(b))
    carry = 0
    carry_events = 0
    s = 0
    for i in range(32):
        ai = (a >> i) & 1
        bi = (b >> i) & 1
        si = ai ^ bi ^ carry
        carry_out = (ai & bi) | (ai & carry) | (bi & carry)
        carry_events += carry_out
        carry = carry_out
        s |= (si << i)
    return np.uint32(s), int(carry_events)

def addN_carry(*args):
    total = np.uint32(0)
    ce = 0
    for x in args:
        total, c = add32_carry(total, np.uint32(x))
        ce += c
    return total, ce

def sha256_compress_carry(block_words):
    W = np.zeros(64, dtype=np.uint32)
    W[:16] = block_words.astype(np.uint32)
    carry_total = 0

    for t in range(16, 64):
        s1 = sigma1(W[t-2])
        s0 = sigma0(W[t-15])
        tmp, c1 = addN_carry(s1, W[t-7], s0, W[t-16])
        W[t] = tmp
        carry_total += c1

    a,b,c,d,e,f,g,h = H0.copy()

    for t in range(64):
        T1, cT1 = addN_carry(h, Sigma1(e), Ch(e,f,g), K[t], W[t])
        T2, cT2 = addN_carry(Sigma0(a), Maj(a,b,c))
        carry_total += (cT1 + cT2)

        h = g; g = f; f = e
        e, cE = add32_carry(d, T1); carry_total += cE
        d = c; c = b; b = a
        a, cA = add32_carry(T1, T2); carry_total += cA

    return int(carry_total)

# Generators
def gen_block_random(rng):
    return rng.integers(0, 2**32, size=16, dtype=np.uint32)

def gen_block_sparse(rng, bits_on=3):
    words = []
    for _ in range(16):
        pos = rng.choice(32, size=bits_on, replace=False)
        w = 0
        for p in pos: w |= (1 << int(p))
        words.append(np.uint32(w))
    return np.array(words, dtype=np.uint32)

def gen_block_no_adjacent(rng, density=0.22):
    words = []
    for _ in range(16):
        w = 0
        i = 0
        while i < 32:
            if rng.random() < density:
                w |= (1 << i)
                i += 2
            else:
                i += 1
        words.append(np.uint32(w))
    return np.array(words, dtype=np.uint32)

def gen_block_sector1_like(rng):
    words = []
    baseA = np.uint32(0x11111111)
    baseB = np.uint32(0x01010101)
    baseC = np.uint32(0x00010001)
    for i in range(16):
        if i % 4 in (0,1,2):
            w = baseA ^ (np.uint32(rng.integers(0, 2**8)) << np.uint32((i % 4) * 8))
        else:
            w = baseB ^ (np.uint32(rng.integers(0, 2**8)) << np.uint32((i % 4) * 8))
        if rng.random() < 0.2:
            w ^= baseC
        words.append(np.uint32(w))
    return np.array(words, dtype=np.uint32)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000, help="blocks per group")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--outdir", default="sha_carry_out")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    groups = {
        "random": [],
        "sparse3": [],
        "no_adj": [],
        "sector1_like": []
    }

    for _ in range(args.n):
        groups["random"].append(sha256_compress_carry(gen_block_random(rng)))
        groups["sparse3"].append(sha256_compress_carry(gen_block_sparse(rng, bits_on=3)))
        groups["no_adj"].append(sha256_compress_carry(gen_block_no_adjacent(rng, density=0.22)))
        groups["sector1_like"].append(sha256_compress_carry(gen_block_sector1_like(rng)))

    df = pd.DataFrame({k: pd.Series(v) for k,v in groups.items()})
    df.to_csv(os.path.join(args.outdir, "carry_counts.csv"), index=False)

    # summary stats vs random
    comps = []
    for name in ["sparse3","no_adj","sector1_like"]:
        t_stat, t_p = stats.ttest_ind(df[name], df["random"], equal_var=False)
        mw_stat, mw_p = stats.mannwhitneyu(df[name], df["random"], alternative="two-sided")
        delta = df[name].mean() - df["random"].mean()
        d = (df[name].mean() - df["random"].mean()) / np.sqrt(((df[name].std(ddof=1)**2 + df["random"].std(ddof=1)**2)/2))
        comps.append([name, float(df[name].mean()), float(df["random"].mean()), float(delta), float(d), float(t_p), float(mw_p)])

    comp_df = pd.DataFrame(comps, columns=["pattern","mean_carry","mean_random","delta","cohens_d","t_p","mw_p"])
    comp_df.to_csv(os.path.join(args.outdir, "summary_vs_random.csv"), index=False)

    # histogram
    plt.figure(figsize=(9,5))
    for col in df.columns:
        plt.hist(df[col], bins=40, alpha=0.5, label=col)
    plt.xlabel("Total carry events per compression (one block)")
    plt.ylabel("Count")
    plt.title("SHA-256 carry-event distributions: random vs patterned")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "carry_hist.png"), dpi=160)
    plt.close()

    print("DONE")
    print(comp_df)

if __name__ == "__main__":
    main()
