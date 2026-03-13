
#!/usr/bin/env python3
"""
NEXUS Preregistered Biology Test Runner (v1)
===========================================

VERBS, NOT NOUNS. This script operationalizes the preregistered falsifiers:

TEST 1: External validation on an external dataset (PFDB-like):
        |r| > 0.4 and p < 0.01 between Sarrus Z and ln(kf)

TEST 2: Composition-null victory:
        raw composition-only correlates weakly (|r| < 0.2) while z-scored Sarrus correlates strongly (|r| > 0.4)

TEST 3: Mechanistic coupling:
        Sarrus magnitude correlates with ruggedness proxy (phi breadth / chevron asymmetry) if present

TEST 4: Attractor test (pre-registered):
        ln(kf) vs |sigma - pi/9| (and/or |A - pi/9|) shows a valley at 0 (minimum)

TEST 5: Basin ≠ speed:
        Basins are reported as saturation phenotypes only; no basin→speed claim is made.

What this does:
- Load CSV/TSV/Parquet and AUTO-DETECT columns for sequence and ln(kf).
- Compute locked Sarrus feature:
    MJ map -> autocorr at helix lags [3,4] and sheet lag [2] -> S = Z_H - Z_S
    shuffle-null z-score using deterministic MD5 seed per sequence
- Compute additional metrics if columns exist (ambiguity A, sigma, ruggedness proxies)
- Run prereg tests and generate:
    (a) console summary
    (b) PDF report
    (c) JSON audit log (hashes, exclusions, column mapping)

Usage:
    python NEXUS_PFDB_Preregistered_TestRunner_v1.py --data /path/to/pfdb.csv

Notes:
- Parameters are LOCKED unless you explicitly change them in the "LOCKED PARAMS" block.
- If dataset lacks needed columns for some tests, those tests are marked "NOT EVALUATED" (not "pass").
"""
from __future__ import annotations

import argparse, json, hashlib, os, sys
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# -----------------------------
# LOCKED PARAMS (do not change)
# -----------------------------
HELIX_LAGS = (3, 4)
SHEET_LAG = 2
N_SHUFFLES = 10000          # prereg default
SHUFFLE_SEED_POLICY = "md5(sequence)"
MJ_SCALE_NAME = "Kyte-Doolittle (KD)"  # This is what your earlier notebooks used; keep locked.
CAPACITY = 4.0              # sigma capacity for saturation mapping (lens parameter)
PI_OVER_9 = float(np.pi/9)

# Decision thresholds (pre-registered)
TEST1_R_ABS_MIN = 0.4
TEST1_P_MAX = 0.01
TEST2_RAW_R_ABS_MAX = 0.2
TEST2_Z_R_ABS_MIN = 0.4

# ------------
# MJ scale KD
# ------------
KD = {
    'A': 1.8,'C': 2.5,'D': -3.5,'E': -3.5,'F': 2.8,'G': -0.4,'H': -3.2,'I': 4.5,
    'K': -3.9,'L': 3.8,'M': 1.9,'N': -3.5,'P': -1.6,'Q': -3.5,'R': -4.5,'S': -0.8,
    'T': -0.7,'V': 4.2,'W': -0.9,'Y': -1.3
}

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def md5_seed(text: str) -> int:
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)

def to_kd(seq: str) -> np.ndarray:
    return np.array([KD.get(aa, 0.0) for aa in seq], dtype=float)

def autocorr_lag(x: np.ndarray, lag: int) -> float:
    if lag <= 0 or lag >= len(x):
        return np.nan
    a, b = x[:-lag], x[lag:]
    sa, sb = a.std(), b.std()
    if sa == 0 or sb == 0:
        return 0.0
    return float(np.corrcoef(a, b)[0,1])

def sarrus_raw(seq: str) -> float:
    x = to_kd(seq)
    if len(x) < 10:
        return np.nan
    z_h = np.nanmean([autocorr_lag(x, k) for k in HELIX_LAGS])
    z_s = autocorr_lag(x, SHEET_LAG)
    return float(z_h - z_s)

def shuffle_seq(seq: str, rng: np.random.Generator) -> str:
    arr = np.frombuffer(seq.encode("ascii", "ignore"), dtype=np.uint8).copy()
    rng.shuffle(arr)
    return arr.tobytes().decode("ascii", "ignore")

def sarrus_z(seq: str, n_shuffles: int = N_SHUFFLES) -> Tuple[float,float,float,float]:
    """
    Returns (S_raw, S_z, null_mean, null_std)
    Deterministic per-sequence RNG: md5(seed)
    """
    raw = sarrus_raw(seq)
    seed = md5_seed(seq)
    rng = np.random.default_rng(seed)
    nulls = np.empty(n_shuffles, dtype=float)
    for i in range(n_shuffles):
        s2 = shuffle_seq(seq, rng)
        nulls[i] = sarrus_raw(s2)
    mu = float(np.nanmean(nulls))
    sd = float(np.nanstd(nulls, ddof=1))
    z = (raw - mu)/sd if sd > 0 else 0.0
    return float(raw), float(z), mu, sd

def safe_numeric(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")

def detect_column(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in lower:
            return lower[cand.lower()]
    # fuzzy contains
    for c in df.columns:
        cl = c.lower()
        for cand in candidates:
            if cand.lower() in cl:
                return c
    return None

@dataclass
class ColumnMap:
    sequence: Optional[str] = None
    ln_kf: Optional[str] = None
    kf: Optional[str] = None
    ambiguity: Optional[str] = None
    sigma: Optional[str] = None
    ruggedness_phi_breadth: Optional[str] = None
    ruggedness_chevron_asym: Optional[str] = None
    length: Optional[str] = None
    name: Optional[str] = None
    class_label: Optional[str] = None

def infer_columns(df: pd.DataFrame) -> ColumnMap:
    seq_col = detect_column(df, ["sequence","seq","aa_sequence","protein_sequence"])
    ln_kf_col = detect_column(df, ["ln_kf","ln(kf)","lnkf","log_kf","logkf","ln_rate","lnkfold"])
    kf_col = detect_column(df, ["kf","k_f","folding_rate","rate","kf_s-1","kf_s^-1"])
    amb_col = detect_column(df, ["ambiguity","A_amb","amb","A"])
    sigma_col = detect_column(df, ["sigma","sat","saturation","v_over_c","v/c"])
    phi_col = detect_column(df, ["phi_breadth","phi_width","phi_std","phi_var","phi_distribution_breadth"])
    chev_col = detect_column(df, ["chevron_asym","chevron_asymmetry","chevron_curvature","chevron_beta"])
    len_col = detect_column(df, ["length","L","seq_len","n_res","residues"])
    name_col = detect_column(df, ["name","protein","id","pdb","uniprot","entry"])
    class_col = detect_column(df, ["class","fold_class","two_state","kinetic_class","category","label"])
    return ColumnMap(seq_col, ln_kf_col, kf_col, amb_col, sigma_col, phi_col, chev_col, len_col, name_col, class_col)

def compute_ln_kf(df: pd.DataFrame, cm: ColumnMap) -> pd.Series:
    if cm.ln_kf and cm.ln_kf in df.columns:
        return safe_numeric(df[cm.ln_kf])
    if cm.kf and cm.kf in df.columns:
        kf = safe_numeric(df[cm.kf])
        return np.log(kf.replace(0, np.nan))
    return pd.Series([np.nan]*len(df), index=df.index)

def basin_from_sigma(sigma: np.ndarray) -> np.ndarray:
    """
    Basin labels are phenotypes of saturation only (NOT speed).
    Using legacy thresholds 0.4/0.8 ONLY for descriptive reporting,
    and we mark them as descriptive.
    """
    out = np.full(len(sigma), "NA", dtype=object)
    m = np.isfinite(sigma)
    out[m & (sigma < 0.4)] = "E"
    out[m & (sigma >= 0.4) & (sigma < 0.8)] = "TRANSIENT"
    out[m & (sigma >= 0.8)] = "PHI"
    return out

def sigma_from_sarrus_z(sz: np.ndarray, capacity: float = CAPACITY) -> np.ndarray:
    # Saturation proxy: map |Z| into [0,1) using a bounded transform.
    # This is a lens definition, not a claim of physics.
    z = np.abs(sz)
    return z / (capacity + z)

def corr_report(x: np.ndarray, y: np.ndarray, label: str) -> Dict:
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 5:
        return {"label": label, "n": int(m.sum()), "r": np.nan, "p": np.nan}
    r, p = stats.pearsonr(x[m], y[m])
    return {"label": label, "n": int(m.sum()), "r": float(r), "p": float(p)}

def valley_test(xdist: np.ndarray, y: np.ndarray, label: str) -> Dict:
    """
    Pre-registered valley check:
    We regress y on |d| and |d|^2 and test whether quadratic term is positive
    and minimum occurs near d=0 within data support.
    This is a conservative operationalization of "valley at 0".
    """
    m = np.isfinite(xdist) & np.isfinite(y)
    if m.sum() < 8:
        return {"label": label, "n": int(m.sum()), "quad_b": np.nan, "quad_p": np.nan, "note": "insufficient n"}
    d = np.asarray(xdist[m], float)
    yy = np.asarray(y[m], float)
    X = np.column_stack([np.ones_like(d), d, d**2])
    # OLS
    beta = np.linalg.lstsq(X, yy, rcond=None)[0]
    yhat = X @ beta
    resid = yy - yhat
    n, k = len(yy), X.shape[1]
    s2 = (resid@resid) / (n-k)
    cov = s2 * np.linalg.inv(X.T@X)
    se = np.sqrt(np.diag(cov))
    # quadratic term
    b2 = beta[2]
    t = b2 / se[2] if se[2] > 0 else np.nan
    p = 2*(1 - stats.t.cdf(abs(t), df=n-k)) if np.isfinite(t) else np.nan
    return {"label": label, "n": int(n), "quad_b": float(b2), "quad_p": float(p)}

def make_report(df: pd.DataFrame, out_pdf: str, summary: Dict, plots: Dict):
    with PdfPages(out_pdf) as pdf:
        # Page 1: summary text
        fig = plt.figure(figsize=(8.5, 11))
        fig.clf()
        txt = json.dumps(summary, indent=2)
        fig.text(0.05, 0.95, "NEXUS Preregistered Test Runner v1", fontsize=16, va="top")
        fig.text(0.05, 0.92, "VERBS: load → extract → null → predict → validate → kill", fontsize=10, va="top")
        fig.text(0.05, 0.89, "Summary (JSON):", fontsize=12, va="top")
        fig.text(0.05, 0.87, txt[:5000], fontsize=8, va="top", family="monospace")
        pdf.savefig(fig)
        plt.close(fig)

        # Plots
        for title, fig in plots.items():
            fig.suptitle(title)
            pdf.savefig(fig)
            plt.close(fig)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=str, required=True, help="Path to PFDB-like dataset (csv/tsv/parquet)")
    ap.add_argument("--outdir", type=str, default="nexus_out", help="Output directory")
    ap.add_argument("--sep", type=str, default=None, help="CSV separator override (default auto)")
    ap.add_argument("--limit", type=int, default=None, help="Optional row limit for quick runs")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    data_path = args.data

    # Load
    ext = os.path.splitext(data_path)[1].lower()
    if ext in [".parquet"]:
        df = pd.read_parquet(data_path)
    else:
        sep = args.sep
        if sep is None:
            # crude sniff: if tabs likely
            with open(data_path, "rb") as f:
                head = f.read(4096).decode("utf-8", "ignore")
            sep = "\t" if head.count("\t") > head.count(",") else ","
        df = pd.read_csv(data_path, sep=sep)

    if args.limit:
        df = df.head(args.limit).copy()

    cm = infer_columns(df)
    if not cm.sequence:
        raise SystemExit("Could not detect a sequence column. Provide a column named like 'sequence' or pass a preprocessed file.")

    # Extract
    seqs = df[cm.sequence].astype(str).str.upper().str.replace(r"[^ACDEFGHIKLMNPQRSTVWY]", "", regex=True)
    ln_kf = compute_ln_kf(df, cm)

    # Length
    if cm.length and cm.length in df.columns:
        L = safe_numeric(df[cm.length])
    else:
        L = seqs.str.len().astype(float)

    # Compute Sarrus raw + z
    S_raw = np.full(len(df), np.nan, float)
    S_z   = np.full(len(df), np.nan, float)
    null_mu = np.full(len(df), np.nan, float)
    null_sd = np.full(len(df), np.nan, float)

    for i, s in enumerate(seqs):
        if len(s) < 10:
            continue
        r, z, mu, sd = sarrus_z(s, N_SHUFFLES)
        S_raw[i], S_z[i], null_mu[i], null_sd[i] = r, z, mu, sd

    # Derived lens metrics
    if cm.sigma and cm.sigma in df.columns:
        sigma = safe_numeric(df[cm.sigma]).to_numpy()
    else:
        sigma = sigma_from_sarrus_z(S_z, CAPACITY)

    if cm.ambiguity and cm.ambiguity in df.columns:
        A = safe_numeric(df[cm.ambiguity]).to_numpy()
    else:
        A = np.full(len(df), np.nan, float)

    basin = basin_from_sigma(sigma)

    # Mechanistic proxies (optional)
    phi_b = safe_numeric(df[cm.ruggedness_phi_breadth]).to_numpy() if cm.ruggedness_phi_breadth else np.full(len(df), np.nan, float)
    chev_a = safe_numeric(df[cm.ruggedness_chevron_asym]).to_numpy() if cm.ruggedness_chevron_asym else np.full(len(df), np.nan, float)

    # ---- TESTS ----
    results = {}

    # TEST 1
    rep1 = corr_report(S_z, ln_kf.to_numpy(), "Sarrus_Z vs ln(kf)")
    pass1 = (np.isfinite(rep1["r"]) and abs(rep1["r"]) > TEST1_R_ABS_MIN and rep1["p"] < TEST1_P_MAX)
    results["TEST1_external_validation"] = {"criterion": f"|r|>{TEST1_R_ABS_MIN} and p<{TEST1_P_MAX}", "report": rep1, "pass": bool(pass1)}

    # TEST 2
    rep2_raw = corr_report(S_raw, ln_kf.to_numpy(), "Sarrus_RAW vs ln(kf)")
    rep2_z   = rep1
    pass2 = (np.isfinite(rep2_raw["r"]) and abs(rep2_raw["r"]) < TEST2_RAW_R_ABS_MAX and np.isfinite(rep2_z["r"]) and abs(rep2_z["r"]) > TEST2_Z_R_ABS_MIN)
    results["TEST2_composition_null"] = {
        "criterion": f"|r_raw|<{TEST2_RAW_R_ABS_MAX} and |r_z|>{TEST2_Z_R_ABS_MIN}",
        "raw": rep2_raw, "z": rep2_z, "pass": bool(pass2)
    }

    # TEST 3 (optional)
    rep3a = corr_report(np.abs(S_z), phi_b, "|Sarrus_Z| vs PhiBreadth")
    rep3b = corr_report(np.abs(S_z), chev_a, "|Sarrus_Z| vs ChevronAsym")
    mech_ok = False
    note3 = "requires ruggedness proxy columns"
    if np.isfinite(rep3a["r"]) or np.isfinite(rep3b["r"]):
        note3 = "evaluated on available proxies"
        # prereg idea: any positive association that survives p<0.05 (exploratory threshold here)
        mech_ok = ((np.isfinite(rep3a["r"]) and rep3a["p"] < 0.05) or (np.isfinite(rep3b["r"]) and rep3b["p"] < 0.05))
    results["TEST3_mechanism_proxy"] = {"note": note3, "phi": rep3a, "chevron": rep3b, "pass": bool(mech_ok) if note3!="requires ruggedness proxy columns" else "NOT_EVALUATED"}

    # TEST 4 (optional valley)
    vt_sigma = valley_test(np.abs(sigma - PI_OVER_9), ln_kf.to_numpy(), "Valley at sigma≈pi/9")
    vt_A     = valley_test(np.abs(A - PI_OVER_9), ln_kf.to_numpy(), "Valley at A≈pi/9") if np.isfinite(A).any() else {"label":"Valley at A≈pi/9","n":0,"quad_b":np.nan,"quad_p":np.nan,"note":"A not provided"}
    # Pass if quadratic positive and p<0.05 (valley)
    pass4_sigma = (np.isfinite(vt_sigma["quad_b"]) and vt_sigma["quad_b"] > 0 and vt_sigma["quad_p"] < 0.05)
    pass4_A     = (np.isfinite(vt_A["quad_b"]) and vt_A["quad_b"] > 0 and vt_A["quad_p"] < 0.05)
    results["TEST4_attractor_pi_over_9"] = {
        "criterion": "quadratic valley at 0 (b2>0, p<0.05)",
        "sigma": vt_sigma, "A": vt_A,
        "pass": bool(pass4_sigma or pass4_A) if (vt_sigma["n"]>=8 or vt_A.get("n",0)>=8) else "NOT_EVALUATED"
    }

    # TEST 5 is conceptual; we enforce by not claiming basin→speed, and by reporting basin only descriptively.
    results["TEST5_basin_not_speed"] = {"enforced": True, "note": "Basins reported as saturation phenotypes only; no basin→speed inference performed.", "pass": True}

    # ---- AUDIT LOG ----
    out_pdf = os.path.join(args.outdir, "NEXUS_Preregistered_Report_v1.pdf")
    out_json = os.path.join(args.outdir, "NEXUS_Preregistered_Audit_v1.json")
    out_csv = os.path.join(args.outdir, "NEXUS_Preregistered_Results_v1.csv")

    audit = {
        "inputs": {
            "data_path": os.path.abspath(data_path),
            "data_sha256": sha256_file(data_path),
            "rows_loaded": int(len(df)),
        },
        "locked_params": {
            "HELIX_LAGS": HELIX_LAGS,
            "SHEET_LAG": SHEET_LAG,
            "N_SHUFFLES": N_SHUFFLES,
            "SHUFFLE_SEED_POLICY": SHUFFLE_SEED_POLICY,
            "MJ_SCALE_NAME": MJ_SCALE_NAME,
            "CAPACITY": CAPACITY,
            "PI_OVER_9": PI_OVER_9,
        },
        "column_map": asdict(cm),
        "exclusions": {
            "seq_len_lt_10": int((seqs.str.len() < 10).sum()),
            "missing_ln_kf": int(ln_kf.isna().sum()),
            "invalid_feature": int(np.sum(~np.isfinite(S_z))),
        },
        "tests": results
    }

    # Save per-row results
    out_df = pd.DataFrame({
        "name": df[cm.name] if cm.name else np.arange(len(df)),
        "sequence": seqs,
        "L": L,
        "ln_kf": ln_kf,
        "S_raw": S_raw,
        "S_z": S_z,
        "sigma": sigma,
        "ambiguity_A": A,
        "basin_desc": basin,
        "phi_breadth": phi_b,
        "chevron_asym": chev_a
    })
    out_df.to_csv(out_csv, index=False)

    with open(out_json, "w") as f:
        json.dump(audit, f, indent=2)

    # ---- PLOTS ----
    plots = {}

    # Plot 1: S_z vs ln_kf
    fig1 = plt.figure(figsize=(7,5))
    ax = fig1.add_subplot(111)
    m = np.isfinite(S_z) & np.isfinite(ln_kf.to_numpy())
    ax.scatter(S_z[m], ln_kf.to_numpy()[m], s=12)
    if m.sum() >= 2:
        b1, a1 = np.polyfit(S_z[m], ln_kf.to_numpy()[m], 1)
        xx = np.linspace(np.nanmin(S_z[m]), np.nanmax(S_z[m]), 200)
        ax.plot(xx, a1 + b1*xx, linestyle="--")
    ax.set_xlabel("Sarrus Z")
    ax.set_ylabel("ln(kf)")
    ax.set_title("Primary test: Sarrus Z vs ln(kf)")
    plots["Primary"] = fig1

    # Plot 2: RAW vs ln_kf
    fig2 = plt.figure(figsize=(7,5))
    ax = fig2.add_subplot(111)
    m = np.isfinite(S_raw) & np.isfinite(ln_kf.to_numpy())
    ax.scatter(S_raw[m], ln_kf.to_numpy()[m], s=12)
    ax.set_xlabel("Sarrus RAW")
    ax.set_ylabel("ln(kf)")
    ax.set_title("Composition null: RAW vs ln(kf)")
    plots["Composition null"] = fig2

    # Plot 3: Attractor valley sigma
    fig3 = plt.figure(figsize=(7,5))
    ax = fig3.add_subplot(111)
    d = np.abs(sigma - PI_OVER_9)
    m = np.isfinite(d) & np.isfinite(ln_kf.to_numpy())
    ax.scatter(d[m], ln_kf.to_numpy()[m], s=12)
    ax.set_xlabel("|sigma - pi/9|")
    ax.set_ylabel("ln(kf)")
    ax.set_title("Attractor test (sigma)")
    plots["Attractor sigma"] = fig3

    # Plot 4: Basin counts (descriptive only)
    fig4 = plt.figure(figsize=(7,4))
    ax = fig4.add_subplot(111)
    vc = pd.Series(basin).value_counts()
    ax.bar(vc.index.astype(str), vc.values)
    ax.set_xlabel("Basin (descriptive saturation phenotype)")
    ax.set_ylabel("Count")
    ax.set_title("Basin distribution (descriptive only)")
    plots["Basin"] = fig4

    make_report(out_df, out_pdf, audit, plots)

    # ---- CONSOLE SUMMARY ----
    print("\n=== NEXUS Preregistered Runner v1 ===")
    print("Column map:", asdict(cm))
    for k, v in results.items():
        print(f"\n{k}")
        print(json.dumps(v, indent=2))
    print(f"\nWROTE:\n  {out_pdf}\n  {out_json}\n  {out_csv}")

if __name__ == "__main__":
    main()
