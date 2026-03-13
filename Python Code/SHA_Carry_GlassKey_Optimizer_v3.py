#!/usr/bin/env python3
# ============================================================
# SHA_Carry_GlassKey_Optimizer_v3.py  (FULL RUN, NOTEBOOK-SAFE)
# ============================================================
# Fixes:
#  1) No more SystemExit in Jupyter:
#     - If running under ipykernel/IPython, we DO NOT call sys.exit / raise SystemExit.
#     - main() returns normally.
#  2) Stats robustness:
#     - Welch t-test only if both groups have non-trivial variance.
#     - Always reports Mann–Whitney U (rank-based) as primary.
#     - Adds a permutation p-value for carry mean difference (default 5000 perms).
#
# Verbs:
#   GENERATE -> SCORE (carry events) -> MUTATE -> SELECT -> REPEAT
#   MEASURE -> PHASE-MAP -> TEST CONCENTRATION
#
# Outputs (outdir):
#   population_history.csv
#   winners.csv
#   history.png
#   carry_hist.png
#   phase_scatter.png
#   report.txt
# ============================================================

import argparse, os, math, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------------
# SHA-256 carry counter
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
    b = block.copy()
    for i in range(16):
        if rng.random() < p_word:
            w = int(b[i])
            for bit in range(32):
                if rng.random() < p_bit:
                    w ^= (1 << bit)
            if rng.random() < 0.05:
                w = int(rng.integers(0, 2**32))
            b[i] = np.uint32(w)
    return b

def run_search(n_gen=80, pop=256, elite=32, seed=7):
    rng = np.random.default_rng(seed)
    population = [random_block(rng) for _ in range(pop)]
    hist = []

    best_block = None
    best_score = None

    for g in range(n_gen):
        scores = np.array([sha256_compress_carry(b) for b in population], dtype=int)
        idx = np.argsort(scores)
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

        next_pop = elites.copy()
        while len(next_pop) < pop:
            parent = elites[int(rng.integers(0, elite))]
            child = mutate_block(rng, parent)
            next_pop.append(child)
        population = next_pop

    final_scores = np.array([sha256_compress_carry(b) for b in population], dtype=int)
    idx = np.argsort(final_scores)
    winners = [population[i] for i in idx[:elite]]
    if best_block is not None:
        winners.append(best_block)

    return pd.DataFrame(hist), winners

# -----------------------------
# Robust stats helpers
# -----------------------------
def permutation_pvalue_mean_diff(x, y, n_perm=5000, seed=123):
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    obs = float(np.mean(x) - np.mean(y))
    pooled = np.concatenate([x, y])
    n_x = len(x)
    count = 0
    for _ in range(n_perm):
        rng.shuffle(pooled)
        d = float(np.mean(pooled[:n_x]) - np.mean(pooled[n_x:]))
        if abs(d) >= abs(obs):
            count += 1
    return obs, (count + 1) / (n_perm + 1)

# -----------------------------
# Core run (notebook-safe)
# -----------------------------
def run(gens=80, pop=256, elite=32, seed=7, outdir="sha_glasskey_out", n_perm=5000):
    os.makedirs(outdir, exist_ok=True)

    hist_df, winners = run_search(n_gen=gens, pop=pop, elite=elite, seed=seed)
    hist_df.to_csv(os.path.join(outdir, "population_history.csv"), index=False)

    rng = np.random.default_rng(seed + 999)
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
    df.to_csv(os.path.join(outdir, "winners.csv"), index=False)

    w = df[df["label"]=="winner"].copy()
    r = df[df["label"]=="random"].copy()

    # Primary: Mann–Whitney (robust)
    mw_stat, mw_p = stats.mannwhitneyu(w["carry"], r["carry"], alternative="two-sided")

    # Welch t-test only if variance isn't ~0 (avoids catastrophic cancellation warning)
    t_p = None
    if w["carry"].std(ddof=1) > 1e-9 and r["carry"].std(ddof=1) > 1e-9:
        _, t_p = stats.ttest_ind(w["carry"], r["carry"], equal_var=False)

    # Permutation p-value on mean difference
    mean_diff, perm_p = permutation_pvalue_mean_diff(w["carry"], r["carry"], n_perm=n_perm, seed=seed+123)

    # π/9 (20°) concentration
    target = 20.0
    dist_w = np.abs(((w["theta_deg"] - target + 180) % 360) - 180)
    dist_r = np.abs(((r["theta_deg"] - target + 180) % 360) - 180)
    mw_d_stat, mw_d_p = stats.mannwhitneyu(dist_w, dist_r, alternative="two-sided")

    # Report
    with open(os.path.join(outdir, "report.txt"), "w", encoding="utf-8") as f:
        f.write("SHA Glass Key Optimizer v3 (notebook-safe, robust stats)\n")
        f.write(f"gens={gens}, pop={pop}, elite={elite}, seed={seed}, perms={n_perm}\n\n")
        f.write("Carry comparison (winners vs random baseline)\n")
        f.write(f"winner mean carry: {w['carry'].mean():.2f}\n")
        f.write(f"random mean carry: {r['carry'].mean():.2f}\n")
        f.write(f"MW p: {mw_p:.3e}\n")
        if t_p is not None:
            f.write(f"Welch t-test p: {t_p:.3e}\n")
        else:
            f.write("Welch t-test: skipped (near-zero variance detected)\n")
        f.write(f"mean diff (winner-random): {mean_diff:.2f}\n")
        f.write(f"permutation p(|diff|): {perm_p:.3e}\n\n")
        f.write("Phase concentration test (distance to 20 deg)\n")
        f.write(f"winner median dist: {np.median(dist_w):.2f} deg\n")
        f.write(f"random median dist: {np.median(dist_r):.2f} deg\n")
        f.write(f"MW p: {mw_d_p:.3e}\n")

    # Plots (no explicit colors)
    plt.figure(figsize=(8,5))
    plt.plot(hist_df["gen"], hist_df["best"], label="best")
    plt.plot(hist_df["gen"], hist_df["median"], label="median")
    plt.xlabel("generation")
    plt.ylabel("carry events")
    plt.title("Evolution history: carry minimization")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "history.png"), dpi=160)
    plt.close()

    plt.figure(figsize=(8,5))
    plt.hist(w["carry"], bins=25, alpha=0.6, label="winners")
    plt.hist(r["carry"], bins=25, alpha=0.6, label="random")
    plt.xlabel("carry events")
    plt.ylabel("count")
    plt.title("Carry distributions: winners vs random baseline")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "carry_hist.png"), dpi=160)
    plt.close()

    plt.figure(figsize=(8,5))
    plt.scatter(r["zh"], r["zs"], alpha=0.7, label="random")
    plt.scatter(w["zh"], w["zs"], alpha=0.7, label="winners")
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
    plt.savefig(os.path.join(outdir, "phase_scatter.png"), dpi=160)
    plt.close()

    print("DONE")
    print("Outputs in:", outdir)
    # Return paths for notebook use
    return {
        "outdir": outdir,
        "report": os.path.join(outdir, "report.txt"),
        "winners_csv": os.path.join(outdir, "winners.csv"),
        "history_csv": os.path.join(outdir, "population_history.csv")
    }

def run_in_notebook(gens=80, pop=256, elite=32, seed=7, outdir="sha_glasskey_out", n_perm=5000):
    return run(gens=gens, pop=pop, elite=elite, seed=seed, outdir=outdir, n_perm=n_perm)

# -----------------------------
# CLI entrypoint (Jupyter-safe)
# -----------------------------
def main():
    ap = argparse.ArgumentParser(description="SHA carry 'Glass Key' optimizer (v3).")
    ap.add_argument("--gens", type=int, default=80)
    ap.add_argument("--pop", type=int, default=256)
    ap.add_argument("--elite", type=int, default=32)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--outdir", default="sha_glasskey_out")
    ap.add_argument("--perms", type=int, default=5000)
    args, _ = ap.parse_known_args()
    run(gens=args.gens, pop=args.pop, elite=args.elite, seed=args.seed, outdir=args.outdir, n_perm=args.perms)
    return 0

if __name__ == "__main__":
    # If inside IPython/Jupyter, don't raise SystemExit (prevents the annoying SystemExit: 0)
    in_ipy = ("ipykernel" in sys.modules) or ("IPython" in sys.modules and hasattr(sys, "ps1"))
    if in_ipy:
        main()
    else:
        raise SystemExit(main())
