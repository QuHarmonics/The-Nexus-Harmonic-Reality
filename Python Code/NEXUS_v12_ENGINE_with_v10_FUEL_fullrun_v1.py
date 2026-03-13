#!/usr/bin/env python3
# =============================================================================
# NEXUS_v12_ENGINE_with_v10_FUEL_fullrun_v1.py   (FULL RUN, NOTEBOOK-SAFE)
# =============================================================================
# Goal (verbs, not nouns):
#   LOAD v10 Ivankov dataset (TWO_STATE=30 entries) + corrected constructs
#   ACQUIRE sequence (override > fetched FASTA > skip)
#   EXTRACT locked Sarrus (MJ scale; helix lags [3,4]; sheet lag 2; MD5-seeded shuffles)
#   ANALYZE (Pearson r, permutation p, partial corr controlling ln(L), LOO-CV)
#   TEST Lorentz probe (rank->sigma->Lambda) with stable CDF encoder
#   EXPORT audit + figures to outdir
#
# This merges:
#   - v12 "engine" (audit/enforcement + reporting structure)
#   - v10 "fuel" (Ivankov 27+ protein list + corrected constructs dictionary)
#
# NOTE:
#   - If you have internet, set USE_RCSB=True to fetch missing sequences.
#   - If offline, you'll get partial inclusion unless you paste additional overrides.
#
# Run in notebook:
#   %run NEXUS_v12_ENGINE_with_v10_FUEL_fullrun_v1.py --outdir nexus_v12xv10_out --use_rcsb 1
#
# Or import:
#   import importlib.util; ...; mod.run_in_notebook(...)
# =============================================================================

import argparse, os, math, hashlib, urllib.request, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# ----------------------------
# LOCKED CONFIG (v12)
# ----------------------------
LOCK = {
    "SCALE": "MJ",
    "HELIX_LAGS": [3, 4],
    "SHEET_LAG": 2,
    "N_SHUFFLES": 1000,
    "N_PERM": 10000,
    "LEN_TOL_FRAC": 0.10,  # 10% mismatch tolerance unless overridden
}

# MJ scale (v12 locked)
MJ_SCALE = {
    'C': 1.36, 'F': 1.27, 'I': 1.24, 'L': 1.21, 'V': 1.13,
    'W': 1.08, 'M': 0.99, 'A': 0.61, 'G': 0.01, 'P': -0.14,
    'Y': -0.23, 'T': -0.25, 'S': -0.38, 'H': -0.65, 'Q': -0.69,
    'N': -0.78, 'E': -0.91, 'K': -1.18, 'D': -1.23, 'R': -1.62
}

# ----------------------------
# v10 FUEL: Ivankov dataset + corrected constructs
# ----------------------------
# Format: (PDB, NAME, exp_length, ln_kf, ???)  -> we keep exp_length, ln_kf.
TWO_STATE = [
    ("2PDD","E3/E1 PSBD",41,9.8),
    ("2ABD","ACBP",86,6.6),
    ("256B","Cyt b562",106,12.2),
    ("1IMQ","Im9",86,7.3),
    ("1LMB","lambda-Rep",80,8.5),
    ("1FNF","FN3-9",90,-0.9),
    ("1WIT","Twitchin",93,0.4),
    ("1TEN","Tenascin",90,1.1),
    ("1SHG","SH3-spectrin",62,1.4),
    ("1SRL","SH3-src",64,4.0),
    ("1PNJ","SH3-PI3K",90,-1.1),
    ("1SHF","SH3-fyn",67,4.5),
    ("1PSF","PsaE",69,3.2),
    ("1CSP","CspB-Bs",67,7.0),
    ("1C9O","CspB-Bc",66,7.2),
    ("1G6P","CspB-Tm",66,6.3),
    ("1MJC","CspA-Ec",69,5.3),
    ("1LOP","CypA",164,6.6),
    ("1C8C","DNA-bp",63,7.0),
    ("1HZ6","Protein L",62,4.1),
    ("1PGB","Protein G",57,6.0),
    ("1FKB","FKBP12",107,1.5),
    ("2CI2","CI2",64,3.9),
    ("1AYE","ADA2h",80,6.8),
    ("1URN","U1A",102,5.8),
    ("1APS","AcP",98,-1.5),
    ("1RIS","S6",101,5.9),
    ("1POH","HPr",85,2.7),
    ("1DIV","NTL9",56,6.1),
    ("2VIK","Villin 14T",126,6.8),
]

MULTI_STATE = [
    ("1A6N","Apomyoglobin",151,1.1),
    ("1CEI","Im7",87,5.8),
    ("2CRO","Cro",71,3.7),
    ("1TIT","Titin-I27",89,3.6),
    ("1HNG","CD2-d1",98,1.8),
    ("1FNF","FN3-10",94,5.5),
    ("1IFC","IFABP",131,3.4),
    ("1EAL","ILBP",127,1.3),
    ("1OPA","CRBPII",133,1.4),
    ("1CBI","CRABPI",136,-3.2),
    ("1BRS","Barstar",89,3.4),
    ("3CHY","CheY",129,1.0),
    ("2RN2","RNaseH",155,0.1),
    ("1RA9","DHFR",159,4.6),
    ("1BNI","Barnase",110,2.6),
    ("2LZM","T4 Lyso",164,4.1),
    ("1UBQ","Ubiquitin",76,5.9),
    ("1SCE","Suc1",113,4.2),
]

# Corrected constructs (domain enforcement)
CORRECTED = {
    "1FNF_9": "VSDVPRDLEVVAATPTSLLISWDAPAVTVRYYRITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYAVTGRGDSPASSKPISINYRT",
    "1AYE": "RQLPALLPEEWFHKAVLDRAQGDGPFQKFGVQIRASDHGTEVALPEGVHLIAECRDEEAGVRELLRRLRAAGVVDKEHD",
    "1DIV": "MKVIFLKDVKGMGKKGEIKNVADGYANNFLFKQGLAIEATPANLKALEAQKQKEQR",
    "1WIT": "LKPAIVTNVKENVTNFEDVILDWSPPDSPVVFEIVYAPKRDQWKVAVPVGDNGKCAPMQLNKVLSEDANGSLRVTVKAEIQSSGNSPEGF",
    "1SHG": "DETGKELVLALYDYQEKSPREVTMKKGDILTLLNSTNKDWWKVEVNDRQGFVPAAYVKKLD",
    "1SHF": "VQALYDYVESYEGDNTEFQKGDDIIVLNYKGQDWWYGEIGGSEGLVPAQYLVPQQ",
    "1SRL": "GQVAIYDYQNDPDDELSFKKGDVITTVDRKQWDWWIGERCAGRGIVPSNYVL",
    "1APS": "LVRHMQPEYAVQLLISDGEYSGRWAVEKHGIPLDTVVCALSLSDYGHRPVLLSKEIGAKGKIILLHAGGEKNEEVVRKENADLLEKAGITLPIEDL",
    "1TEN": "RLDAPSQIEVKDVTDTTALITWFKPLAEIDGIELTYGIKDVPGDRTTIDLTEDENQYSIGNLKPDTEYEVSLISRRGDMSSNPAKETFTT",
    "1TIT": "LIEVEKPLYGVEVFVGETAHFEIELSEPDVHGQWKLKGQPLAASPDCEIIEDGKKHILILHNCQLGMTGEVSFQAANTKSAANLKVKEL",
}

# ----------------------------
# Core extraction (v12 locked)
# ----------------------------
def md5_seed(seq: str) -> int:
    return int(hashlib.md5(seq.encode("utf-8")).hexdigest(), 16) % (2**32)

def seq_to_signal(seq: str, scale=MJ_SCALE) -> np.ndarray:
    return np.array([scale.get(aa, 0.0) for aa in seq if aa in scale], dtype=float)

def acf_total_energy(signal: np.ndarray, lag: int) -> float:
    n = len(signal)
    if n <= lag or lag <= 0:
        return np.nan
    s = signal - signal.mean()
    denom = float(np.sum(s**2))
    if denom < 1e-12:
        return np.nan
    return float(np.sum(s[:-lag] * s[lag:]) / denom)

def sarrus_locked(seq: str, n_shuf: int = LOCK["N_SHUFFLES"]) -> dict:
    sig = seq_to_signal(seq)
    if len(sig) < 10:
        return {"z_h": np.nan, "z_s": np.nan, "sarrus": np.nan, "sh_std_h": np.nan, "sh_std_s": np.nan}

    H = float(np.nanmean([acf_total_energy(sig, l) for l in LOCK["HELIX_LAGS"]]))
    S = float(acf_total_energy(sig, LOCK["SHEET_LAG"]))

    seed = md5_seed(seq)
    rng = np.random.default_rng(seed)
    shH, shS = [], []
    for _ in range(n_shuf):
        shuf = sig.copy()
        rng.shuffle(shuf)
        h = float(np.nanmean([acf_total_energy(shuf, l) for l in LOCK["HELIX_LAGS"]]))
        s = float(acf_total_energy(shuf, LOCK["SHEET_LAG"]))
        if np.isfinite(h) and np.isfinite(s):
            shH.append(h); shS.append(s)

    shH = np.array(shH, float); shS = np.array(shS, float)
    if len(shH) < 20:
        return {"z_h": np.nan, "z_s": np.nan, "sarrus": np.nan, "sh_std_h": np.nan, "sh_std_s": np.nan}

    muH, sdH = float(shH.mean()), float(shH.std(ddof=1))
    muS, sdS = float(shS.mean()), float(shS.std(ddof=1))
    if sdH < 1e-12 or sdS < 1e-12:
        return {"z_h": np.nan, "z_s": np.nan, "sarrus": np.nan, "sh_std_h": sdH, "sh_std_s": sdS}

    z_h = (H - muH) / sdH
    z_s = (S - muS) / sdS
    return {"z_h": float(z_h), "z_s": float(z_s), "sarrus": float(z_h - z_s), "sh_std_h": sdH, "sh_std_s": sdS}

# ----------------------------
# FASTA fetch (RCSB)
# ----------------------------
def fetch_rcsb_fasta(pdb_ids):
    url = "https://www.rcsb.org/fasta/entry/" + ",".join(sorted(set(pdb_ids)))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    seqs = {}
    cur = None
    buf = []
    for line in text.splitlines():
        if line.startswith(">"):
            if cur is not None:
                seqs.setdefault(cur, []).append("".join(buf))
            cur = line[1:].split("|")[0].split("_")[0].upper()
            buf = []
        else:
            buf.append(line.strip())
    if cur is not None:
        seqs.setdefault(cur, []).append("".join(buf))
    return seqs

def pick_best_candidate(pdb: str, candidates, exp_len: int):
    if not candidates:
        return None, "no_candidates"
    # exact length first
    for s in candidates:
        if len(s) == exp_len:
            return s, "picked_exact"
    # else closest length
    idx = int(np.argmin([abs(len(s)-exp_len) for s in candidates]))
    return candidates[idx], "picked_closest"

def choose_sequence(pdb_id: str, name: str, exp_len: int, fetched: dict) -> dict:
    # special key
    key = "1FNF_9" if (pdb_id == "1FNF" and "FN3-9" in name) else pdb_id

    if key in CORRECTED:
        seq = CORRECTED[key]
        return {"status": "OVERRIDE", "seq": seq, "used_len": len(seq), "reason": f"key={key}"}

    # fetched candidates for pdb_id
    if pdb_id in fetched:
        cand = fetched[pdb_id]
        seq, why = pick_best_candidate(pdb_id, cand, exp_len)
        if seq is None:
            return {"status": "SKIP", "seq": None, "used_len": np.nan, "reason": "no_candidates"}
        used_len = len(seq)
        tol = max(1, int(np.ceil(exp_len * LOCK["LEN_TOL_FRAC"])))
        if abs(used_len - exp_len) <= tol:
            return {"status": "FETCH_MATCH", "seq": seq, "used_len": used_len, "reason": why}
        return {"status": "SKIP", "seq": None, "used_len": used_len, "reason": f"len_mismatch>{LOCK['LEN_TOL_FRAC']:.0%} ({used_len} vs {exp_len})"}

    return {"status": "SKIP", "seq": None, "used_len": np.nan, "reason": "missing_fasta_and_no_override"}

def build_audit(dataset, fetched):
    rows = []
    for pdb, name, expL, ln_kf in dataset:
        pick = choose_sequence(pdb, name, expL, fetched)
        if pick["status"] == "SKIP":
            rows.append({"STATUS":"SKIP","PDB":pdb,"NAME":name,"expL":expL,"usedL":pick["used_len"],
                         "reason":pick["reason"],"zH":np.nan,"zS":np.nan,"SARRUS":np.nan,
                         "shHstd":np.nan,"shSstd":np.nan,"ln_kf":ln_kf})
            continue
        metrics = sarrus_locked(pick["seq"], LOCK["N_SHUFFLES"])
        rows.append({"STATUS":pick["status"],"PDB":pdb,"NAME":name,"expL":expL,"usedL":pick["used_len"],
                     "reason":pick["reason"],"zH":metrics["z_h"],"zS":metrics["z_s"],"SARRUS":metrics["sarrus"],
                     "shHstd":metrics["sh_std_h"],"shSstd":metrics["sh_std_s"],"ln_kf":ln_kf})
    return pd.DataFrame(rows)

# ----------------------------
# Stats (v12)
# ----------------------------
def permutation_p_abs_r(x, y, n_perm=LOCK["N_PERM"], seed=42):
    rng = np.random.default_rng(seed)
    r_obs = abs(stats.pearsonr(x, y)[0])
    count = 0
    for _ in range(n_perm):
        y_sh = rng.permutation(y)
        r = abs(stats.pearsonr(x, y_sh)[0])
        if r >= r_obs:
            count += 1
    return (count + 1) / (n_perm + 1)

def partial_corr(x, y, cov):
    mask = np.isfinite(x) & np.isfinite(y) & np.isfinite(cov)
    x = x[mask]; y = y[mask]; cov = cov[mask]
    bx = np.polyfit(cov, x, 1); by = np.polyfit(cov, y, 1)
    rx = x - np.polyval(bx, cov)
    ry = y - np.polyval(by, cov)
    return stats.pearsonr(rx, ry)

def loo_linear(x, y):
    n = len(x)
    preds = np.zeros(n)
    for i in range(n):
        m = np.ones(n, dtype=bool); m[i] = False
        slope, intercept = np.polyfit(x[m], y[m], 1)
        preds[i] = slope * x[i] + intercept
    r, p = stats.pearsonr(preds, y)
    r2 = 1 - np.sum((y - preds)**2) / np.sum((y - y.mean())**2)
    return float(r), float(r2), float(p), preds

def stable_midrank_cdf(train_x, x0):
    # consistent CDF for held-out: midrank among train points + 0.5
    train_x = np.asarray(train_x, float)
    n = len(train_x)
    lt = np.sum(train_x < x0)
    eq = np.sum(train_x == x0)
    return float((lt + 0.5*eq + 0.5) / (n + 1.0))

def loo_lorentz(S, Y):
    n = len(S)
    preds = np.zeros(n)
    for i in range(n):
        m = np.ones(n, dtype=bool); m[i] = False
        S_tr = S[m]; Y_tr = Y[m]
        # sigma for training using rankdata -> (0,1)
        ranks = stats.rankdata(S_tr, method="average")
        sigma_tr = ranks / (len(ranks) + 1.0)
        sigma_tr = np.clip(sigma_tr, 0.01, 0.99)
        lam_tr = 0.5*np.log(1 - sigma_tr**2)
        b, a = np.polyfit(lam_tr, Y_tr, 1)
        # sigma for held-out using stable cdf encoder
        sigma_i = stable_midrank_cdf(S_tr, S[i])
        sigma_i = float(np.clip(sigma_i, 0.01, 0.99))
        lam_i = 0.5*np.log(1 - sigma_i**2)
        preds[i] = a + b*lam_i
    r = float(np.corrcoef(preds, Y)[0,1])
    r2 = float(1 - np.sum((Y - preds)**2) / np.sum((Y - Y.mean())**2))
    return r, r2, preds

def fit_linear_aic(x, y):
    b, a = np.polyfit(x, y, 1)
    resid = y - (a + b*x)
    n = len(y)
    rss = float(np.sum(resid**2))
    k = 2
    return float(a), float(b), float(n*np.log(rss/n) + 2*k)

# ----------------------------
# RUN
# ----------------------------
def run(outdir="nexus_v12xv10_out", use_rcsb=True):
    os.makedirs(outdir, exist_ok=True)

    all_pdbs = [p for p,_,_,_ in (TWO_STATE + MULTI_STATE)]
    fetched = {}
    if use_rcsb:
        try:
            print("Fetching FASTA from RCSB...")
            fetched = fetch_rcsb_fasta(all_pdbs)
            print(f"Fetched FASTA for {len(fetched)} PDB IDs.")
        except Exception as e:
            print("RCSB fetch failed; running offline. Error:", e)
            fetched = {}
    else:
        print("RCSB fetch disabled (offline mode).")

    audit_two = build_audit(TWO_STATE, fetched)
    audit_multi = build_audit(MULTI_STATE, fetched)

    audit_two.to_csv(os.path.join(outdir, "audit_two_state.csv"), index=False)
    audit_multi.to_csv(os.path.join(outdir, "audit_multi_state.csv"), index=False)

    included = audit_two[(audit_two["STATUS"]!="SKIP") & np.isfinite(audit_two["SARRUS"])].copy()
    print(f"Included (two-state): {len(included)} / {len(audit_two)}")
    print(f"Skipped (two-state):  {int((audit_two['STATUS']=='SKIP').sum())}")

    # Primary stats (two-state only)
    S = included["SARRUS"].to_numpy(float)
    Y = included["ln_kf"].to_numpy(float)
    L = np.log(included["usedL"].to_numpy(float))

    r, p = stats.pearsonr(S, Y)
    p_perm = permutation_p_abs_r(S, Y)
    r_part, p_part = partial_corr(S, Y, L)
    r_loo, r2_loo, p_loo, pred_lin = loo_linear(S, Y)

    # Lorentz probe
    # Full-fit AICs
    a_lin, b_lin, aic_lin = fit_linear_aic(S, Y)

    sigma_full = stats.rankdata(S, method="average") / (len(S)+1.0)
    sigma_full = np.clip(sigma_full, 0.01, 0.99)
    lam_full = 0.5*np.log(1 - sigma_full**2)
    a_lor, b_lor, aic_lor = fit_linear_aic(lam_full, Y)

    r_loo_lor, r2_loo_lor, pred_lor = loo_lorentz(S, Y)

    # Save report
    with open(os.path.join(outdir, "report.txt"), "w", encoding="utf-8") as f:
        f.write("NEXUS v12 engine + v10 fuel (full run)\n")
        f.write(f"use_rcsb={use_rcsb}\n")
        f.write(f"Included two-state n={len(S)}\n\n")
        f.write("PRIMARY\n")
        f.write(f"Pearson r(SARRUS, ln(kf)) = {r:.4f}  p = {p:.3e}\n")
        f.write(f"Permutation p(|r|) = {p_perm:.4f} (n_perm={LOCK['N_PERM']})\n")
        f.write(f"Partial r | ln(L_used) = {r_part:.4f}  p = {p_part:.3e}\n")
        f.write(f"LOO-CV r(pred, obs) = {r_loo:.4f}  p = {p_loo:.3e}\n")
        f.write(f"LOO-CV R^2 = {r2_loo:.4f}\n\n")
        f.write("LORENTZ PROBE\n")
        f.write(f"AIC linear  = {aic_lin:.2f}\n")
        f.write(f"AIC lorentz = {aic_lor:.2f} {'<- wins' if aic_lor < aic_lin else ''}\n")
        f.write(f"LOO r linear  = {np.corrcoef(pred_lin, Y)[0,1]:.4f}  R^2={r2_loo:.4f}\n")
        f.write(f"LOO r lorentz = {r_loo_lor:.4f}  R^2={r2_loo_lor:.4f}\n")

    # Plots
    # Primary scatter
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(S, Y)
    m, b = np.polyfit(S, Y, 1)
    xx = np.linspace(S.min(), S.max(), 200)
    ax.plot(xx, m*xx+b, linestyle="--")
    ax.set_title(f"PRIMARY: r={float(r):.3f}, p={float(p):.2e}, n={len(S)}")
    ax.set_xlabel("Sarrus Linkage (Z_H - Z_S)")
    ax.set_ylabel("ln(kf)")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "primary_scatter.png"), dpi=160)
    plt.close()

    # LOO predictions vs observed
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(Y, pred_lin, label="LOO linear")
    ax.scatter(Y, pred_lor, label="LOO lorentz")
    minv = float(min(Y.min(), pred_lin.min(), pred_lor.min()))
    maxv = float(max(Y.max(), pred_lin.max(), pred_lor.max()))
    ax.plot([minv, maxv], [minv, maxv], linestyle="--")
    ax.set_xlabel("Observed ln(kf)")
    ax.set_ylabel("Predicted ln(kf)")
    ax.set_title("LOO predictions")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "loo_predictions.png"), dpi=160)
    plt.close()

    print("DONE. Outputs in:", outdir)
    return outdir

def run_in_notebook(outdir="nexus_v12xv10_out", use_rcsb=True):
    return run(outdir=outdir, use_rcsb=use_rcsb)

def main():
    ap = argparse.ArgumentParser(description="NEXUS v12 engine + v10 fuel full run (notebook-safe).")
    ap.add_argument("--outdir", default="nexus_v12xv10_out")
    ap.add_argument("--use_rcsb", type=int, default=1, help="1=fetch RCSB FASTA, 0=offline")
    args, _ = ap.parse_known_args()
    run(outdir=args.outdir, use_rcsb=bool(args.use_rcsb))
    return 0

if __name__ == "__main__":
    in_ipy = ("ipykernel" in sys.modules) or ("IPython" in sys.modules and hasattr(sys, "ps1"))
    if in_ipy:
        main()
    else:
        raise SystemExit(main())
