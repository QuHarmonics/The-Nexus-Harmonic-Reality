#!/usr/bin/env python3
# ============================================================
# NEXUS_PFDB_Preregistered_TestRunner_v2.py  (FULL RUN)
# ============================================================
# Verbs-only pipeline:
#   LOAD -> DETECT -> EXTRACT -> NULL -> VALIDATE -> WRITE
#
# v2 FIX: Works in Jupyter/IPython without requiring CLI args.
# - --data is OPTIONAL in v2.
# - If not provided:
#     1) use NEXUS_DATA environment variable if set
#     2) auto-search current dir and /mnt/data for a single plausible dataset
#     3) otherwise print clear instructions and exit (no stacktrace)
# ============================================================

import argparse
import os
import sys
import json
import re
import hashlib
from datetime import datetime

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ----------------------------
# Locked parameters (logged)
# ----------------------------
LOCK = {
    "scale": "KD",
    "helix_lags": [3, 4],
    "sheet_lag": 2,
    "shuffle_seed": "md5(sequence)",
    "n_shuffles_default": 5000,
    "capacity": 4.0,
    "pi_over_9": float(np.pi / 9.0),
}

KD = {
    "A": 1.8,  "C": 2.5,  "D": -3.5, "E": -3.5, "F": 2.8,
    "G": -0.4, "H": -3.2, "I": 4.5,  "K": -3.9, "L": 3.8,
    "M": 1.9,  "N": -3.5, "P": -1.6, "Q": -3.5, "R": -4.5,
    "S": -0.8, "T": -0.7, "V": 4.2,  "W": -0.9, "Y": -1.3,
}

# ----------------------------
# Utility: hashing
# ----------------------------
def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def md5_seed(text: str) -> int:
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)

def to_kd(seq: str) -> np.ndarray:
    return np.array([KD.get(aa, 0.0) for aa in seq], dtype=float)

# ----------------------------
# Core extractor (locked)
# ----------------------------
def autocorr_lag(arr: np.ndarray, lag: int) -> float:
    if lag <= 0 or lag >= len(arr):
        return np.nan
    a = arr[:-lag]
    b = arr[lag:]
    sa = a.std()
    sb = b.std()
    if sa == 0 or sb == 0:
        return 0.0
    return float(np.corrcoef(a, b)[0, 1])

def sarrus_linkage_raw(seq: str) -> float:
    x = to_kd(seq)
    if len(x) < 10:
        return np.nan
    z_h = np.nanmean([autocorr_lag(x, k) for k in LOCK["helix_lags"]])
    z_s = autocorr_lag(x, LOCK["sheet_lag"])
    return float(z_h - z_s)

def shuffle_seq(seq: str, rng: np.random.Generator) -> str:
    a = np.array(list(seq))
    rng.shuffle(a)
    return "".join(a.tolist())

def sarrus_zscore(seq: str, n_shuffles: int) -> tuple[float, float, float, float]:
    """Return (S_raw, S_z, null_mean, null_std)."""
    raw = sarrus_linkage_raw(seq)
    seed = md5_seed(seq)
    rng = np.random.default_rng(seed)
    nulls = np.empty(n_shuffles, dtype=float)
    for i in range(n_shuffles):
        s2 = shuffle_seq(seq, rng)
        nulls[i] = sarrus_linkage_raw(s2)
    mu = float(np.nanmean(nulls))
    sd = float(np.nanstd(nulls, ddof=1))
    z = (raw - mu) / sd if sd > 0 else 0.0
    return float(raw), float(z), mu, sd

# ----------------------------
# Column detection
# ----------------------------
SEQ_CANDIDATES = ["sequence","seq","aa_sequence","aa_seq","protein_sequence","fasta","Sequence","SEQ"]
LN_KF_CANDIDATES = ["ln_kf","ln(kf)","log_kf","log(kf)","lnkf","ln_k","ln_rate","ln_kfolding"]
KF_CANDIDATES = ["kf","k_f","kfold","k_folding","folding_rate","rate"]
PHI_CANDIDATES = ["phi","phi_width","phi_breadth","phi_sd","phi_std","phi_spread"]
CHEVRON_CANDIDATES = ["chevron_asym","chevron_asymmetry","chevron_curvature","chevron_beta"]

def detect_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    cols = list(df.columns)
    lower_map = {c.lower(): c for c in cols}
    for cand in candidates:
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    for c in cols:
        cl = c.lower()
        for cand in candidates:
            if cand.lower() in cl:
                return c
    return None

def coerce_sequence(s) -> str | None:
    if not isinstance(s, str):
        return None
    s = s.strip().upper()
    s = re.sub(r"[^ACDEFGHIKLMNPQRSTVWY]", "", s)
    return s if len(s) >= 10 else None

# ----------------------------
# Optional constructs: ambiguity A and sigma
# ----------------------------
def ambiguity_A_from_shuffles(null_std: float) -> float:
    return float(null_std)

def sigma_from_sarrus(raw: float, capacity: float) -> float:
    if capacity <= 0:
        return np.nan
    return float(np.clip(abs(raw) / capacity, 0.0, 0.999))

# ----------------------------
# Tests
# ----------------------------
def test1_primary(df: pd.DataFrame):
    x = df["S_z"].values
    y = df["ln_kf"].values
    r, p = stats.pearsonr(x, y)
    return {"r": float(r), "p": float(p), "pass": bool(abs(r) > 0.4 and p < 0.01)}

def test2_composition_null(df: pd.DataFrame):
    x_raw = df["S_raw"].values
    x_z = df["S_z"].values
    y = df["ln_kf"].values
    r_raw, p_raw = stats.pearsonr(x_raw, y)
    r_z, p_z = stats.pearsonr(x_z, y)
    ok = (abs(r_raw) < 0.2) and (abs(r_z) > 0.4)
    return {"r_raw": float(r_raw), "p_raw": float(p_raw), "r_z": float(r_z), "p_z": float(p_z), "pass": bool(ok)}

def test3_mechanism_proxy(df: pd.DataFrame):
    proxy = None
    if "phi_proxy" in df.columns and df["phi_proxy"].notna().sum() >= 8:
        proxy = "phi_proxy"
    elif "chevron_proxy" in df.columns and df["chevron_proxy"].notna().sum() >= 8:
        proxy = "chevron_proxy"
    if proxy is None:
        return {"pass": False, "not_testable": True, "detail": "No ruggedness proxy column found (phi/chevron)."}
    x = np.abs(df["S_z"].values)
    y = df[proxy].values
    m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 8:
        return {"pass": False, "not_testable": True, "detail": f"Insufficient rows for proxy={proxy}."}
    r, p = stats.pearsonr(x[m], y[m])
    return {"proxy": proxy, "r": float(r), "p": float(p), "pass": bool(abs(r) > 0.3 and p < 0.05)}

def test4_attractor(df: pd.DataFrame):
    out = {"pi_over_9": LOCK["pi_over_9"], "pass": False, "not_testable": False}
    if df["sigma"].notna().sum() < 10 or df["A"].notna().sum() < 10:
        out["not_testable"] = True
        out["detail"] = "sigma or A missing/insufficient"
        return out

    y = df["ln_kf"].values.astype(float)

    def u_shape_check(d, y):
        m = np.isfinite(d) & np.isfinite(y)
        if m.sum() < 10:
            return None
        dd = d[m].astype(float)
        yy = y[m].astype(float)
        c2, c1, c0 = np.polyfit(dd, yy, 2)
        if c2 == 0:
            return {"c2": float(c2), "vertex": np.nan, "ok": False}
        vertex = -c1 / (2*c2)
        scale = float(np.quantile(dd, 0.75))
        ok = (c2 > 0) and (abs(vertex) <= scale)
        return {"c2": float(c2), "c1": float(c1), "c0": float(c0), "vertex": float(vertex), "scale_q75": scale, "ok": bool(ok)}

    d_sigma = np.abs(df["sigma"].values - LOCK["pi_over_9"])
    d_A = np.abs(df["A"].values - LOCK["pi_over_9"])

    res_sigma = u_shape_check(d_sigma, y)
    res_A = u_shape_check(d_A, y)

    out["sigma_fit"] = res_sigma
    out["A_fit"] = res_A
    out["pass"] = bool((res_sigma and res_sigma["ok"]) and (res_A and res_A["ok"]))
    return out

def test5_basin_policy(df: pd.DataFrame):
    if df["sigma"].notna().sum() < 10:
        return {"pass": False, "not_testable": True, "detail": "sigma missing/insufficient to classify basins."}
    sigma = df["sigma"].values.astype(float)
    basin = np.full(len(sigma), "E", dtype=object)
    basin[(sigma >= 0.4) & (sigma < 0.8)] = "TRANSIENT"
    basin[sigma >= 0.8] = "PHI"
    counts = {k: int(np.sum(basin == k)) for k in ["E","TRANSIENT","PHI"]}
    return {"pass": True, "counts": counts, "note": "Basin logged as saturation class only (not speed)."}

# ----------------------------
# Load table
# ----------------------------
def load_table(path: str, sep: str | None):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".parquet":
        return pd.read_parquet(path)
    if ext == ".tsv":
        return pd.read_csv(path, sep="\t")
    if ext == ".csv":
        return pd.read_csv(path, sep="," if sep is None else sep)
    return pd.read_csv(path, sep=sep if sep is not None else None, engine="python")

def find_candidate_data() -> str | None:
    env = os.environ.get("NEXUS_DATA")
    if env and os.path.exists(env):
        return env
    roots = [os.getcwd(), "/mnt/data"]
    pat = re.compile(r"(pfdb|fold|kf|protein|dataset|rates).*\.(csv|tsv|parquet)$", re.I)
    hits = []
    for root in roots:
        try:
            for fn in os.listdir(root):
                if pat.match(fn):
                    hits.append(os.path.join(root, fn))
        except Exception:
            pass
    return hits[0] if len(hits) == 1 else None

# ----------------------------
# Report
# ----------------------------
def write_pdf_report(outpath: str, meta: dict, results: dict, fig_paths: list[str]):
    c = canvas.Canvas(outpath, pagesize=letter)
    width, height = letter
    y = height - 50

    def line(txt, dy=14, bold=False):
        nonlocal y
        c.setFont("Helvetica-Bold" if bold else "Helvetica", 10 if not bold else 11)
        c.drawString(40, y, txt[:110])
        y -= dy

    line("NEXUS Preregistered Test Runner Report (v2)", dy=20, bold=True)
    line(f"Generated (UTC): {meta['generated_utc']}")
    line(f"Data: {meta['data_path']}")
    line(f"SHA256: {meta['data_sha256']}")
    line(f"Rows loaded: {meta['n_loaded']}   Rows used: {meta['n_used']}")
    line("")
    line("LOCKED PARAMETERS", bold=True)
    for k, v in meta["locked_params"].items():
        line(f"- {k}: {v}")
    line("")
    line("COLUMN MAP", bold=True)
    for k, v in meta["column_map"].items():
        line(f"- {k}: {v}")
    line("")
    line("PREREG TESTS", bold=True)
    for k, v in results.items():
        line(f"{k}: {json.dumps(v)[:95]}")
    c.showPage()

    from reportlab.lib.utils import ImageReader
    for fp in fig_paths:
        c.setFont("Helvetica-Bold", 12)
        c.drawString(40, height - 40, os.path.basename(fp))
        img = ImageReader(fp)
        c.drawImage(img, 40, 120, width=520, height=520, preserveAspectRatio=True, anchor='c')
        c.showPage()

    c.save()

# ----------------------------
# Main
# ----------------------------
def main():
    ap = argparse.ArgumentParser(description="NEXUS preregistered PFDB runner (v2).")
    ap.add_argument("--data", required=False, help="Path to PFDB-like dataset (csv/tsv/parquet).")
    ap.add_argument("--outdir", default="nexus_out", help="Output directory.")
    ap.add_argument("--sep", default=None, help="Separator override for CSV.")
    ap.add_argument("--limit", type=int, default=None, help="Optional row limit for quick tests.")
    ap.add_argument("--n_shuffles", type=int, default=LOCK["n_shuffles_default"], help="Number of shuffles for null.")
    args, _ = ap.parse_known_args()

    data_path = args.data or find_candidate_data()
    if not data_path:
        print(
            "No dataset provided.\n\n"
            "Run:\n"
            "  python NEXUS_PFDB_Preregistered_TestRunner_v2.py --data /path/to/pfdb.csv\n\n"
            "In Jupyter:\n"
            "  %run NEXUS_PFDB_Preregistered_TestRunner_v2.py --data /path/to/pfdb.csv\n\n"
            "Or set:\n"
            "  os.environ['NEXUS_DATA']='/path/to/pfdb.csv'\n"
        )
        return 0

    os.makedirs(args.outdir, exist_ok=True)

    df = load_table(data_path, args.sep)
    n_loaded = len(df)
    if args.limit:
        df = df.head(args.limit).copy()

    seq_col = detect_column(df, SEQ_CANDIDATES)
    ln_kf_col = detect_column(df, LN_KF_CANDIDATES)
    kf_col = detect_column(df, KF_CANDIDATES) if ln_kf_col is None else None

    if seq_col is None:
        print("Could not detect sequence column. Candidates:", SEQ_CANDIDATES)
        return 0
    if ln_kf_col is None and kf_col is None:
        print("Could not detect ln(kf) or kf column.")
        print("ln(kf) candidates:", LN_KF_CANDIDATES)
        print("kf candidates:", KF_CANDIDATES)
        return 0

    phi_col = detect_column(df, PHI_CANDIDATES)
    chevron_col = detect_column(df, CHEVRON_CANDIDATES)

    work = pd.DataFrame()
    work["sequence"] = df[seq_col].apply(coerce_sequence)
    work = work.dropna(subset=["sequence"]).copy()
    work["L"] = work["sequence"].str.len()

    if ln_kf_col is not None:
        work["ln_kf"] = pd.to_numeric(df.loc[work.index, ln_kf_col], errors="coerce")
        ln_kf_name = ln_kf_col
    else:
        kf = pd.to_numeric(df.loc[work.index, kf_col], errors="coerce").replace(0, np.nan)
        work["ln_kf"] = np.log(kf)
        ln_kf_name = f"ln({kf_col})"

    if phi_col is not None:
        work["phi_proxy"] = pd.to_numeric(df.loc[work.index, phi_col], errors="coerce")
    if chevron_col is not None:
        work["chevron_proxy"] = pd.to_numeric(df.loc[work.index, chevron_col], errors="coerce")

    work = work.dropna(subset=["ln_kf"]).copy()

    # EXTRACT
    S_raw, S_z, mu, sd, A, sigma = [], [], [], [], [], []
    for seq in work["sequence"].tolist():
        raw, z, nmu, nsd = sarrus_zscore(seq, n_shuffles=args.n_shuffles)
        S_raw.append(raw); S_z.append(z); mu.append(nmu); sd.append(nsd)
        A.append(ambiguity_A_from_shuffles(nsd))
        sigma.append(sigma_from_sarrus(raw, LOCK["capacity"]))

    work["S_raw"] = S_raw
    work["S_z"] = S_z
    work["null_mean"] = mu
    work["null_std"] = sd
    work["A"] = A
    work["sigma"] = sigma

    work = work[np.isfinite(work["S_z"]) & np.isfinite(work["ln_kf"])].copy()
    n_used = len(work)

    results = {
        "TEST1_primary": test1_primary(work) if n_used >= 3 else {"pass": False, "detail": "insufficient rows"},
        "TEST2_composition_null": test2_composition_null(work) if n_used >= 3 else {"pass": False, "detail": "insufficient rows"},
        "TEST3_mechanism_proxy": test3_mechanism_proxy(work),
        "TEST4_attractor": test4_attractor(work),
        "TEST5_basin_policy": test5_basin_policy(work),
    }

    # FIGS
    fig_paths = []

    fig1 = os.path.join(args.outdir, "fig1_sarrusZ_vs_lnkf.png")
    plt.figure(figsize=(7,5))
    plt.scatter(work["S_z"], work["ln_kf"])
    if n_used >= 3:
        m, b = np.polyfit(work["S_z"], work["ln_kf"], 1)
        xx = np.linspace(work["S_z"].min(), work["S_z"].max(), 200)
        plt.plot(xx, m*xx+b, linestyle="--")
        r, p = stats.pearsonr(work["S_z"], work["ln_kf"])
    else:
        r, p = np.nan, np.nan
    plt.title(f"Sarrus Z vs ln(kf): r={r:.3f}, p={p:.2e}")
    plt.xlabel("S_z"); plt.ylabel("ln(kf)")
    plt.tight_layout(); plt.savefig(fig1, dpi=160); plt.close()
    fig_paths.append(fig1)

    fig2 = os.path.join(args.outdir, "fig2_sarrusRaw_vs_lnkf.png")
    plt.figure(figsize=(7,5))
    plt.scatter(work["S_raw"], work["ln_kf"])
    if n_used >= 3:
        m, b = np.polyfit(work["S_raw"], work["ln_kf"], 1)
        xx = np.linspace(work["S_raw"].min(), work["S_raw"].max(), 200)
        plt.plot(xx, m*xx+b, linestyle="--")
        r2, p2 = stats.pearsonr(work["S_raw"], work["ln_kf"])
    else:
        r2, p2 = np.nan, np.nan
    plt.title(f"Sarrus RAW vs ln(kf): r={r2:.3f}, p={p2:.2e}")
    plt.xlabel("S_raw"); plt.ylabel("ln(kf)")
    plt.tight_layout(); plt.savefig(fig2, dpi=160); plt.close()
    fig_paths.append(fig2)

    fig3 = os.path.join(args.outdir, "fig3_attractor_sigma.png")
    plt.figure(figsize=(7,5))
    d = np.abs(work["sigma"] - LOCK["pi_over_9"])
    plt.scatter(d, work["ln_kf"])
    plt.xlabel("|sigma - pi/9|"); plt.ylabel("ln(kf)")
    plt.title("Attractor test (sigma distance)")
    plt.tight_layout(); plt.savefig(fig3, dpi=160); plt.close()
    fig_paths.append(fig3)

    # WRITE
    out_csv = os.path.join(args.outdir, "NEXUS_Preregistered_Results_v1.csv")
    work.to_csv(out_csv, index=False)

    audit = {
        "generated_utc": datetime.utcnow().isoformat() + "Z",
        "data_path": data_path,
        "data_sha256": sha256_file(data_path),
        "n_loaded": int(n_loaded),
        "n_used": int(n_used),
        "column_map": {
            "sequence": seq_col,
            "ln_kf": ln_kf_name,
            "phi_proxy": phi_col,
            "chevron_proxy": chevron_col,
        },
        "locked_params": LOCK,
        "tests": results,
    }
    out_audit = os.path.join(args.outdir, "NEXUS_Preregistered_Audit_v1.json")
    with open(out_audit, "w", encoding="utf-8") as f:
        json.dump(audit, f, indent=2)

    out_pdf = os.path.join(args.outdir, "NEXUS_Preregistered_Report_v1.pdf")
    write_pdf_report(out_pdf, audit, results, fig_paths)

    print("DONE")
    print("Outputs:")
    print(" -", out_pdf)
    print(" -", out_audit)
    print(" -", out_csv)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
