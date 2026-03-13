#!/usr/bin/env python3
"""
SHA_Carry_GlassKey_Optimizer_v1.py

Verbs:
  GENERATE -> SCORE (carry events) -> MUTATE -> SELECT -> REPEAT
  MEASURE -> PHASE-MAP -> TEST CONCENTRATION

What it does:
- Implements SHA-256 compression carry-count proxy (side-channel "stress")
- Runs an evolutionary search for 512-bit blocks with minimal carry events
- Computes a simple phase angle for each block using lag-2 vs lag-4 autocorrelation
  of bit-density across words (a "circular" proxy analogous to (Z_sheet, Z_helix))
- Tests whether low-carry winners concentrate near theta = pi/9 (20 degrees)

Important:
- This is NOT a cryptographic attack and does not claim weakness.
- It tests an *internal* side-channel proxy: carry activity differs by input structure.

Outputs (outdir):
- population_history.csv
- winners.csv
- phase_scatter.png
- carry_hist.png
- report.txt
"""

import argparse, os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------------
# SHA-256 carry counter (same as v1)
# -----------------------------
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

# -----------------------------
# Phase proxy for 16-word block
# -----------------------------
def bitcount32(x: np.uint32) -> int:
    return int(int(x).bit_count())

def acf_lag(series: np.ndarray, lag: int) -> float:
    if lag <= 0 or lag >= len(series):
        return np.nan
    a = series[:-lag]
    b = series[lag:]
    sa = a.std()
    sb = b.std()
    if sa == 0 or sb == 0:
        return 0.0
    return float(np.corrcoef(a, b)[0, 1])

def block_phase(block_words: np.ndarray):
    """
    Compute zh ~ mean ACF at lag 4 (period-4) and zs ~ ACF at lag 2 (period-2)
    using per-word bitcounts as the 16-length signal.
    Returns (theta in [0,2pi), radius, zh, zs)
    """
    s = np.array([bitcount32(w) for w in block_words], dtype=float)
    zh = acf_lag(s, 4)
    zs = acf_lag(s, 2)
    theta = math.atan2(zs, zh)
    if theta < 0:
        theta += 2*math.pi
    radius = float(math.sqrt(zh*zh + zs*zs))
    return float(theta), radius, float(zh), float(zs)

# -----------------------------
# Evolutionary search
# -----------------------------
def random_block(rng):
    return rng.integers(0, 2**32, size=16, dtype=np.uint32)

def mutate_block(rng, block, p_word=0.2, p_bit=0.02):
    """
    Mutate by:
      - with prob p_word per word: flip a few bits with prob p_bit per bit
      - occasionally replace an entire word
    """
    b = block.copy()
    for i in range(16):
        if rng.random() < p_word:
            w = int(b[i])
            # bit flips
            for bit in range(32):
                if rng.random() < p_bit:
                    w ^= (1 << bit)
            # rare word replace
            if rng.random() < 0.05:
                w = int(rng.integers(0, 2**32))
            b[i] = np.uint32(w)
    return b

def run_search(n_gen=80, pop=256, elite=32, offspring=224, seed=7):
    rng = np.random.default_rng(seed)
    population = [random_block(rng) for _ in range(pop)]
    hist = []

    best_block = None
    best_score = None

    for g in range(n_gen):
        scores = np.array([sha256_compress_carry(b) for b in population], dtype=int)
        idx = np.argsort(scores)  # lower carry = better
        elites = [population[i] for i in idx[:elite]]

        if best_score is None or scores[idx[0]] < best_score:
            best_score = int(scores[idx[0]])
            best_block = population[idx[0]].copy()

        hist.append({
            "gen": g,
            "best": int(scores[idx[0]]),
            "p10": int(np.percentile(scores, 10)),
            "median": int(np.median(scores)),
            "mean": float(np.mean(scores)),
            "worst": int(scores[idx[-1]])
        })

        # breed next generation
        next_pop = elites.copy()
        while len(next_pop) < pop:
            parent = elites[int(rng.integers(0, elite))]
            child = mutate_block(rng, parent)
            next_pop.append(child)
        population = next_pop

    # collect winners: top elite from final gen + best ever
    final_scores = np.array([sha256_compress_carry(b) for b in population], dtype=int)
    idx = np.argsort(final_scores)
    winners = [population[i] for i in idx[:elite]]
    if best_block is not None:
        winners.append(best_block)

    return hist, winners

# -----------------------------
# Main
# -----------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gens", type=int, default=80)
    ap.add_argument("--pop", type=int, default=256)
    ap.add_argument("--elite", type=int, default=32)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--outdir", default="sha_glasskey_out")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    hist, winners = run_search(n_gen=args.gens, pop=args.pop, elite=args.elite,
                               offspring=args.pop-args.elite, seed=args.seed)

    hist_df = pd.DataFrame(hist)
    hist_df.to_csv(os.path.join(args.outdir, "population_history.csv"), index=False)

    # Evaluate winners & a random baseline sample
    rng = np.random.default_rng(args.seed + 999)
    baseline = [random_block(rng) for _ in range(len(winners))]

    rows = []
    for label, blocks in [("winner", winners), ("random", baseline)]:
        for b in blocks:
            carry = sha256_compress_carry(b)
            theta, radius, zh, zs = block_phase(b)
            rows.append({
                "label": label,
                "carry": int(carry),
                "theta_deg": float(theta * 180.0 / math.pi),
                "radius": float(radius),
                "zh": float(zh),
                "zs": float(zs)
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(args.outdir, "winners.csv"), index=False)

    # Statistical tests
    w = df[df["label"]=="winner"]
    r = df[df["label"]=="random"]
    t_stat, t_p = stats.ttest_ind(w["carry"], r["carry"], equal_var=False)
    mw_stat, mw_p = stats.mannwhitneyu(w["carry"], r["carry"], alternative="two-sided")

    target = 20.0
    dist_w = np.abs(((w["theta_deg"] - target + 180) % 360) - 180)
    dist_r = np.abs(((r["theta_deg"] - target + 180) % 360) - 180)

    # concentration test: are winners closer to 20° than random?
    mw_d_stat, mw_d_p = stats.mannwhitneyu(dist_w, dist_r, alternative="two-sided")

    # save report
    with open(os.path.join(args.outdir, "report.txt"), "w", encoding="utf-8") as f:
        f.write("SHA Glass Key Optimizer v1\n")
        f.write(f"gens={args.gens}, pop={args.pop}, elite={args.elite}, seed={args.seed}\n\n")
        f.write("Carry comparison (winners vs random baseline of equal size)\n")
        f.write(f"winner mean carry: {w['carry'].mean():.2f}\n")
        f.write(f"random mean carry: {r['carry'].mean():.2f}\n")
        f.write(f"t-test p: {t_p:.3e}\n")
        f.write(f"MW p: {mw_p:.3e}\n\n")
        f.write("Phase concentration test (distance to 20 deg)\n")
        f.write(f"winner median dist: {np.median(dist_w):.2f} deg\n")
        f.write(f"random median dist: {np.median(dist_r):.2f} deg\n")
        f.write(f"MW p: {mw_d_p:.3e}\n")

    # Plots
    # 1) history
    plt.figure(figsize=(8,5))
    plt.plot(hist_df["gen"], hist_df["best"], label="best")
    plt.plot(hist_df["gen"], hist_df["median"], label="median")
    plt.xlabel("generation")
    plt.ylabel("carry events")
    plt.title("Evolution history: carry minimization")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "history.png"), dpi=160)
    plt.close()

    # 2) carry histogram
    plt.figure(figsize=(8,5))
    plt.hist(w["carry"], bins=25, alpha=0.6, label="winners")
    plt.hist(r["carry"], bins=25, alpha=0.6, label="random")
    plt.xlabel("carry events")
    plt.ylabel("count")
    plt.title("Carry distributions: winners vs random baseline")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "carry_hist.png"), dpi=160)
    plt.close()

    # 3) phase scatter
    plt.figure(figsize=(8,5))
    plt.scatter(r["zh"], r["zs"], alpha=0.7, label="random")
    plt.scatter(w["zh"], w["zs"], alpha=0.7, label="winners")
    # target ray at 20 deg: slope = tan(20deg)
    slope = math.tan(math.radians(20.0))
    x = np.linspace(min(df["zh"].min(), -1), max(df["zh"].max(), 1), 200)
    plt.plot(x, slope*x, linestyle="--", label="20° ray")
    plt.axhline(0, linewidth=0.5)
    plt.axvline(0, linewidth=0.5)
    plt.xlabel("zh (lag-4 ACF of bitcount)")
    plt.ylabel("zs (lag-2 ACF of bitcount)")
    plt.title("Phase space of blocks (winners vs random)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "phase_scatter.png"), dpi=160)
    plt.close()

    print("DONE")
    print(f"Outputs in: {args.outdir}")

if __name__ == "__main__":
    main()
