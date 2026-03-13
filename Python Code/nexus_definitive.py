#!/usr/bin/env python3
"""
NEXUS DEFINITIVE PIPELINE — v10 CANONICAL
==========================================
This is the ONE implementation. Every other version is wrong.

Source of truth: v10 Diamond Build (produced r=0.5388 on n=27)
Changes from v10: +3 domain overrides (1LMB, 1HZ6, 2CI2) → n=30
                  + Corrected Lorentz bridge (column bug fixed)
                  + Cross-domain ABC integration
                  + Full diagnostic output

LOCKED (do not change):
  Scale:        Miyazawa-Jernigan inter-residue contact energy
  Helix lags:   [3, 4]
  Sheet lag:    2
  Shuffles:     1000
  Shuffle:      amino acid LIST, re-map to signal each iteration
  Std:          ddof=0 (population std)
  Seed:         MD5(sequence string) mod 2^32
  RNG:          numpy default_rng

Author: Dean Kulik (ORCID 0009-0003-3128-8828)
Compiled: 2026-02-16 by Claude (locked to v10 Diamond)
"""

import numpy as np
from scipy import stats
import hashlib
import urllib.request
import warnings
import sys
import json
from datetime import datetime

warnings.filterwarnings("ignore")

# ==============================================================================
# 1) LOCKED CONFIGURATION — IDENTICAL TO v10 DIAMOND BUILD
# ==============================================================================
MJ = {
    'A': 0.616, 'R':-1.537, 'N':-0.628, 'D':-0.608, 'C': 0.680,
    'Q':-0.468, 'E':-0.587, 'G': 0.501, 'H':-0.340, 'I': 1.385,
    'L': 1.256, 'K':-1.840, 'M': 0.828, 'F': 1.356, 'P':-0.198,
    'S':-0.049, 'T': 0.034, 'W': 0.878, 'Y': 0.534, 'V': 1.111
}
HELIX_LAGS = [3, 4]
SHEET_LAG = 2
N_SHUFFLES = 1000
N_PERM = 10000
LEN_TOL = 0.10

# ==============================================================================
# 2) DATASET — IVANKOV (2003) WITH ALL DOMAIN OVERRIDES
# ==============================================================================

# Domain overrides: kinetics construct sequences
# Original 10 from v10:
OVERRIDES = {
    "1FNF_9": "VSDVPRDLEVVAATPTSLLISWDAPAVTVRYYRITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYAVTGRGDSPASSKPISINYRT",
    "1AYE":   "RQLPALLPEEWFHKAVLDRAQGDGPFQKFGVQIRASDHGTEVALPEGVHLIAECRDEEAGVRELLRRLRAAGVVDKEHD",
    "1DIV":   "MKVIFLKDVKGMGKKGEIKNVADGYANNFLFKQGLAIEATPANLKALEAQKQKEQR",
    "1WIT":   "LKPAIVTNVKENVTNFEDVILDWSPPDSPVVFEIVYAPKRDQWKVAVPVGDNGKCAPMQLNKVLSEDANGSLRVTVKAEIQSSGNSPEGFK",
    "1SHG":   "DETGKELVLALYDYQEKSPREVTMKKGDILTLLNSTNKDWWKVEVNDRQGFVPAAYVKKLD",
    "1SHF":   "VQALYDYVESYEGDNTEFQKGDDIIVLNYKGQDWWYGEIGGSEGLVPAQYLVPQQ",
    "1SRL":   "GQVAIYDYQNDPDDELSFKKGDVITTVDRKQWDWWIGERCAGRGIVPSNYVL",
    "1APS":   "LVRHMQPEYAVQLLISDGEYSGRWAVEKHGIPLDTVVCALSLSDYGHRPVLLSKEIGAKGKIILLHAGGEKNEEVVRKENADLLEKAGITL",
    "1TEN":   "RLDAPSQIEVKDVTDTTALITWFKPLAEIDGIELTYGIKDVPGDRTTIDLTEDENQYSIGNLKPDTEYEVSLISRRGDMSSNPAKETFTT",
    "1TIT":   "LIEVEKPLYGVEVFVGETAHFEIELSEPDVHGQWKLKGQPLAASPDCEIIEDGKKHILILHNCQLGMTGEVSFQAANTKSAANLKVKEL",
    # NEW: Three previously missing overrides
    # 1LMB: Lambda repressor N-terminal domain, residues 7-86 of PDB chain
    # PDB FASTA = 92aa, kinetics construct = 80aa
    "1LMB":   "LTQEQLEDARRLKAIYEKKKNELGLSQESVADKMGMGQSGVGALFNGINALNAYNAALLAKILKVSVEEFSPSIAREIYE",
    # 1HZ6: Protein L B1 domain, His-tag removed + first 3 expression residues
    # PDB FASTA = 72aa (with His-tag), kinetics construct = 62aa
    "1HZ6":   "EVTIKANLIFANGSTQTAEFKGTFEKATSEAYAYADTLKKDNGEWTVDVADKGYTLNIKFAG",
    # 2CI2: CI2, residues 20-83 (standard Jackson/Fersht construct)
    # PDB FASTA = 83aa, kinetics construct = 64aa
    "2CI2":   "LKTEWPELVGKSVEEAKKVILQDKPEAQIIVLPVGTIVTMEYRIDRVRLFVDKLDNIAEVPRVG",
}

# Two-state benchmark: (pdb, name, expected_length, ln_kf, contact_order)
TWO_STATE = [
    ("2PDD", "PSBD",          41,  9.8, 11.0),
    ("2ABD", "ACBP",          86,  6.6, 14.3),
    ("256B", "Cyt_b562",     106, 12.2,  7.5),
    ("1IMQ", "Im9",           86,  7.3, 12.1),
    ("1LMB", "lambda-Rep",    80,  8.5,  9.4),
    ("1FNF", "FN3-9",         90, -0.9, 18.1),
    ("1WIT", "Twitchin",      93,  0.4, 20.3),
    ("1TEN", "Tenascin",      90,  1.1, 17.4),
    ("1SHG", "SH3-spectrin",  62,  1.4, 19.1),
    ("1SRL", "SH3-src",       64,  4.0, 19.6),
    ("1PNJ", "SH3-PI3K",      90, -1.1, 16.1),
    ("1SHF", "SH3-fyn",       67,  4.5, 18.3),
    ("1PSF", "PsaE",          69,  3.2, 17.0),
    ("1CSP", "CspB-Bs",       67,  7.0, 16.4),
    ("1C9O", "CspB-Bc",       66,  7.2,  7.5),
    ("1G6P", "CspB-Tm",       66,  6.3, 17.5),
    ("1MJC", "CspA-Ec",       69,  5.3, 16.0),
    ("1LOP", "CypA",         164,  6.6, 15.7),
    ("1C8C", "DNA-bp",        63,  7.0, 12.7),
    ("1HZ6", "Protein_L",     62,  4.1, 16.1),
    ("1PGB", "Protein_G",     57,  6.0, 17.3),
    ("1FKB", "FKBP12",       107,  1.5, 17.7),
    ("2CI2", "CI2",           64,  3.9, 15.7),
    ("1AYE", "ADA2h",         80,  6.8, 16.7),
    ("1URN", "U1A",          102,  5.8, 16.9),
    ("1APS", "AcP",           98, -1.5, 21.7),
    ("1RIS", "S6",           101,  5.9, 18.9),
    ("1POH", "HPr",           85,  2.7, 17.6),
    ("1DIV", "NTL9",          56,  6.1, 12.7),
    ("2VIK", "Villin_14T",   126,  6.8, 12.3),
]

MULTI_STATE = [
    ("1A6N", "Apomyoglobin", 151,  1.1,  8.4),
    ("1CEI", "Im7",           87,  5.8, 10.8),
    ("2CRO", "Cro",           71,  3.7, 11.2),
    ("1TIT", "Titin-I27",     89,  3.6, 17.8),
    ("1HNG", "CD2-d1",        98,  1.8, 16.9),
    ("1FNF", "FN3-10",        94,  5.5, 16.5),
    ("1IFC", "IFABP",        131,  3.4, 13.5),
    ("1EAL", "ILBP",         127,  1.3, 12.3),
    ("1OPA", "CRBPII",       133,  1.4, 14.0),
    ("1CBI", "CRABPI",       136, -3.2, 13.8),
    ("1BRS", "Barstar",       89,  3.4, 11.8),
    ("3CHY", "CheY",         129,  1.0,  8.7),
    ("2RN2", "RNaseH",       155,  0.1, 12.4),
    ("1RA9", "DHFR",         159,  4.6, 14.0),
    ("1BNI", "Barnase",      110,  2.6, 11.4),
    ("2LZM", "T4_Lyso",      164,  4.1,  7.1),
    ("1UBQ", "Ubiquitin",     76,  5.9, 15.1),
    ("1SCE", "Suc1",         113,  4.2, 11.8),
]

IDP_CONTROLS = {
    "alpha-Synuclein": "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA",
    "p21-CDKN1A":      "MEPVDPRLEPWKHPGSQPKTACQKLEPPEEDCDLCQFNEQLANQRPSQKHLQKYLSDPSATFQEPVQHLDTMLQTLEDLNLRWACLI",
}

# ==============================================================================
# 3) CORE: LOCKED SARRUS PIPELINE (EXACT v10 LOGIC)
# ==============================================================================

def compute_sarrus(seq, scale=MJ, helix_lags=HELIX_LAGS, sheet_lag=SHEET_LAG,
                   n_shuf=N_SHUFFLES):
    """
    Sarrus Linkage extraction — EXACT v10 Diamond logic.
    
    CRITICAL DETAILS (v10-locked):
    - Shuffles amino acid LIST, re-maps to signal each iteration
    - Uses np.std() with ddof=0 (population std)
    - Seeds with MD5 of sequence string
    - Uses numpy default_rng
    """
    sig = np.array([scale.get(aa, 0.0) for aa in seq if aa in scale], dtype=float)
    if len(sig) < 10:
        return dict(z_h=np.nan, z_s=np.nan, sarrus=np.nan, 
                    sh_std_h=np.nan, sh_std_s=np.nan, n_valid=0)
    
    s = sig - sig.mean()
    denom = np.sum(s * s)
    if denom < 1e-12:
        return dict(z_h=np.nan, z_s=np.nan, sarrus=np.nan,
                    sh_std_h=np.nan, sh_std_s=np.nan, n_valid=0)
    
    # Observed ACF at locked lags (total-energy normalization)
    acf_h = np.mean([np.sum(s[:-l] * s[l:]) / denom for l in helix_lags])
    acf_s = np.sum(s[:-sheet_lag] * s[sheet_lag:]) / denom
    
    # Shuffle null: shuffle amino acid LIST, re-map each time
    valid = [aa for aa in seq if aa in scale]
    seed = int(hashlib.md5(seq.encode()).hexdigest(), 16) % (2**32)
    rng = np.random.default_rng(seed)
    
    sh_h, sh_s = [], []
    for _ in range(n_shuf):
        sh = valid.copy()
        rng.shuffle(sh)
        ssig = np.array([scale[a] for a in sh], dtype=float)
        ss = ssig - ssig.mean()
        d = np.sum(ss * ss)
        if d < 1e-12:
            continue
        sh_h.append(np.mean([np.sum(ss[:-l] * ss[l:]) / d for l in helix_lags]))
        sh_s.append(np.sum(ss[:-sheet_lag] * ss[sheet_lag:]) / d)
    
    if len(sh_h) < 20:
        return dict(z_h=np.nan, z_s=np.nan, sarrus=np.nan,
                    sh_std_h=np.nan, sh_std_s=np.nan, n_valid=len(sh_h))
    
    sh_h = np.array(sh_h)
    sh_s = np.array(sh_s)
    
    # ddof=0 (population std) — THIS IS THE v10 CONVENTION
    std_h = float(np.std(sh_h))       # NOT ddof=1
    std_s = float(np.std(sh_s))       # NOT ddof=1
    
    if std_h < 1e-12 or std_s < 1e-12:
        return dict(z_h=np.nan, z_s=np.nan, sarrus=np.nan,
                    sh_std_h=std_h, sh_std_s=std_s, n_valid=len(sh_h))
    
    z_h = float((acf_h - sh_h.mean()) / std_h)
    z_s = float((acf_s - sh_s.mean()) / std_s)
    
    return dict(
        z_h=z_h, z_s=z_s, sarrus=z_h - z_s,
        sh_std_h=std_h, sh_std_s=std_s, n_valid=len(sh_h),
        acf_h=float(acf_h), acf_s=float(acf_s),
        null_mean_h=float(sh_h.mean()), null_mean_s=float(sh_s.mean()),
    )


# ==============================================================================
# 4) STATISTICS (EXACT v10 LOGIC)
# ==============================================================================

def partial_corr(x, y, cov):
    m = ~(np.isnan(x) | np.isnan(y) | np.isnan(cov))
    x, y, cov = x[m], y[m], cov[m]
    if len(x) < 5:
        return np.nan, np.nan
    rx = x - np.polyval(np.polyfit(cov, x, 1), cov)
    ry = y - np.polyval(np.polyfit(cov, y, 1), cov)
    return stats.pearsonr(rx, ry)


def loo_cv(x, y):
    n = len(y)
    preds = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool); mask[i] = False
        sl, il = np.polyfit(x[mask], y[mask], 1)
        preds[i] = sl * x[i] + il
    r, p = stats.pearsonr(preds, y)
    r2 = 1 - np.sum((y - preds)**2) / np.sum((y - y.mean())**2)
    return float(r), float(p), float(r2), preds


def perm_p(x, y, n_perm=N_PERM, seed=42):
    obs = abs(stats.pearsonr(x, y)[0])
    rng = np.random.default_rng(seed)
    cnt = 0
    for _ in range(n_perm):
        if abs(stats.pearsonr(x, rng.permutation(y))[0]) >= obs:
            cnt += 1
    return cnt / n_perm


# ==============================================================================
# 5) FASTA FETCH
# ==============================================================================

def fetch_fasta(pdb_ids):
    url = f"https://www.rcsb.org/fasta/entry/{','.join(sorted(set(pdb_ids)))}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    text = urllib.request.urlopen(req, timeout=60).read().decode()
    seqs = {}
    cur, buf = None, []
    for line in text.splitlines():
        if line.startswith(">"):
            if cur and buf:
                seqs.setdefault(cur, []).append("".join(buf))
            cur = line[1:].split("|")[0].split("_")[0].upper()
            buf = []
        else:
            buf.append(line.strip())
    if cur and buf:
        seqs.setdefault(cur, []).append("".join(buf))
    return seqs


# ==============================================================================
# 6) MAIN EXECUTION
# ==============================================================================

def run_pipeline():
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    
    print("=" * 90)
    print(f"  NEXUS DEFINITIVE PIPELINE — v10 CANONICAL")
    print(f"  Timestamp: {ts}")
    print(f"  Scale: MJ burial energy (v10) | Lags: H=[3,4] S=2 | Shuffles: 1000")
    print(f"  Shuffle: AA list | Std: ddof=0 | Seed: MD5(seq) | RNG: default_rng")
    print("=" * 90)
    
    # Verify overrides
    print(f"\n  Override sequences: {len(OVERRIDES)}")
    for key, seq in OVERRIDES.items():
        print(f"    {key:<8} len={len(seq):>3}")
    
    # Fetch FASTA
    all_pdbs = set(p for p,_,_,_,_ in TWO_STATE) | set(p for p,_,_,_,_ in MULTI_STATE)
    print(f"\n  Fetching FASTA from RCSB for {len(all_pdbs)} PDB entries...")
    try:
        raw = fetch_fasta(list(all_pdbs))
        print(f"  Fetched: {len(raw)} entries")
    except Exception as e:
        print(f"  FETCH FAILED: {e}")
        print(f"  Running with overrides only")
        raw = {}
    
    # ─── Process datasets ───
    def process(rows, label):
        results = []
        audit = []
        
        for pdb, name, expL, ln_kf, co in rows:
            # Resolve sequence
            okey = "1FNF_9" if (pdb == "1FNF" and "FN3-9" in name) else pdb
            
            if okey in OVERRIDES:
                seq = OVERRIDES[okey]
                status = "OVERRIDE"
            elif pdb in raw:
                candidates = raw[pdb]
                seq = min(candidates, key=lambda s: abs(len(s) - expL))
                if abs(len(seq) - expL) > expL * LEN_TOL:
                    audit.append(f"  SKIP {pdb:<6} {name:<16} len={len(seq)} vs {expL} (>{LEN_TOL*100:.0f}%)")
                    continue
                status = "FETCH"
            else:
                audit.append(f"  SKIP {pdb:<6} {name:<16} NO_FASTA")
                continue
            
            # Compute Sarrus
            res = compute_sarrus(seq)
            if np.isnan(res['sarrus']):
                audit.append(f"  SKIP {pdb:<6} {name:<16} NAN_SARRUS (std_h={res['sh_std_h']}, std_s={res['sh_std_s']})")
                continue
            
            results.append({
                'pdb': pdb, 'name': name, 'len': len(seq), 'expL': expL,
                'ln_kf': ln_kf, 'co': co, 'status': status, 'seq': seq,
                **res,
            })
        
        return results, audit
    
    print(f"\n  Processing two-state...")
    ts_results, ts_audit = process(TWO_STATE, "Two-State")
    print(f"  Processing multi-state...")
    ms_results, ms_audit = process(MULTI_STATE, "Multi-State")
    
    # ─── Audit table ───
    print(f"\n{'='*90}")
    print(f"  SEQUENCE AUDIT TABLE")
    print(f"{'='*90}")
    print(f"\n  [TWO-STATE: {len(ts_results)} included, {len(ts_audit)} skipped]")
    print(f"  {'PDB':<6} {'NAME':<16} {'STATUS':<10} {'LEN':>4} {'expL':>4} "
          f"{'Z_H':>7} {'Z_S':>7} {'SARRUS':>8} {'ln(kf)':>7}")
    print(f"  {'─'*85}")
    for r in ts_results:
        print(f"  {r['pdb']:<6} {r['name']:<16} {r['status']:<10} {r['len']:>4} {r['expL']:>4} "
              f"{r['z_h']:>7.3f} {r['z_s']:>7.3f} {r['sarrus']:>8.3f} {r['ln_kf']:>7.1f}")
    if ts_audit:
        print(f"\n  Skipped:")
        for a in ts_audit:
            print(a)
    
    print(f"\n  [MULTI-STATE: {len(ms_results)} included, {len(ms_audit)} skipped]")
    print(f"  {'PDB':<6} {'NAME':<16} {'STATUS':<10} {'LEN':>4} {'expL':>4} "
          f"{'Z_H':>7} {'Z_S':>7} {'SARRUS':>8} {'ln(kf)':>7}")
    print(f"  {'─'*85}")
    for r in ms_results:
        print(f"  {r['pdb']:<6} {r['name']:<16} {r['status']:<10} {r['len']:>4} {r['expL']:>4} "
              f"{r['z_h']:>7.3f} {r['z_s']:>7.3f} {r['sarrus']:>8.3f} {r['ln_kf']:>7.1f}")
    if ms_audit:
        print(f"\n  Skipped:")
        for a in ms_audit:
            print(a)
    
    # ─── IDP controls ───
    print(f"\n  [IDP CONTROLS]")
    idp_sarrus = []
    for name, seq in IDP_CONTROLS.items():
        res = compute_sarrus(seq)
        idp_sarrus.append(res['sarrus'])
        print(f"  {name:<20} len={len(seq):>3} Z_H={res['z_h']:>7.3f} Z_S={res['z_s']:>7.3f} "
              f"SARRUS={res['sarrus']:>8.3f}")
    
    if len(ts_results) < 10:
        print(f"\n  INSUFFICIENT DATA: only {len(ts_results)} two-state proteins")
        return
    
    # ─── Statistics ───
    n = len(ts_results)
    S = np.array([r['sarrus'] for r in ts_results])
    Y = np.array([r['ln_kf'] for r in ts_results])
    L = np.array([np.log(r['len']) for r in ts_results])
    CO = np.array([r['co'] for r in ts_results])
    
    r_pear, p_pear = stats.pearsonr(S, Y)
    pp = perm_p(S, Y)
    r_part, p_part = partial_corr(S, Y, L)
    r_loo, p_loo, r2_loo, preds_lin = loo_cv(S, Y)
    r_co, p_co = stats.pearsonr(CO, Y)
    
    # Multi-state correlation
    if len(ms_results) >= 5:
        Sm = np.array([r['sarrus'] for r in ms_results])
        Ym = np.array([r['ln_kf'] for r in ms_results])
        r_ms, p_ms = stats.pearsonr(Sm, Ym)
    else:
        r_ms, p_ms = np.nan, np.nan
    
    # ─── Lorentz bridge (corrected) ───
    # Rank-based σ mapping (monotone, assumption-free)
    sigma_rank = 1 - stats.rankdata(S) / (n + 1)
    sigma_rank = np.clip(sigma_rank, 0.01, 0.99)
    lor_term = 0.5 * np.log(1 - sigma_rank**2)
    
    r_lor, p_lor = stats.pearsonr(lor_term, Y)
    
    # LOO for Lorentz
    preds_lor = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool); mask[i] = False
        St = S[mask]; Yt = Y[mask]
        sig_t = 1 - stats.rankdata(St) / (len(St) + 1)
        sig_t = np.clip(sig_t, 0.01, 0.99)
        lt = 0.5 * np.log(1 - sig_t**2)
        sl, il = np.polyfit(lt, Yt, 1)
        sig_i = np.clip(stats.percentileofscore(St, S[i]) / 100.0, 0.01, 0.99)
        # Invert: higher S → lower sigma → faster
        sig_i = 1 - sig_i
        preds_lor[i] = sl * 0.5 * np.log(1 - sig_i**2) + il
    r_loo_lor, _ = stats.pearsonr(Y, preds_lor)
    r2_loo_lor = 1 - np.sum((Y - preds_lor)**2) / np.sum((Y - Y.mean())**2)
    
    # AIC
    rss_lin = np.sum((Y - np.polyval(np.polyfit(S, Y, 1), S))**2)
    rss_lor = np.sum((Y - np.polyval(np.polyfit(lor_term, Y, 1), lor_term))**2)
    aic_lin = n * np.log(rss_lin / n) + 4
    aic_lor = n * np.log(rss_lor / n) + 4
    
    print(f"""
{'='*90}
  PRIMARY RESULTS — TWO-STATE (n={n})
{'='*90}
  Pearson r(Sarrus, ln_kf)     = {r_pear:>8.4f}   p = {p_pear:.2e}
  Permutation p (|r|, {N_PERM})   = {pp:.4f}
  Partial r (controlling ln_L) = {r_part:>8.4f}   p = {p_part:.2e}
  LOO-CV r                     = {r_loo:>8.4f}   R² = {r2_loo:.4f}

  Benchmark: r(CO, ln_kf)      = {r_co:>8.4f}   p = {p_co:.2e}

{'='*90}
  CORRECTED LORENTZ BRIDGE
{'='*90}
  Lorentz r(½ln(1-σ²), ln_kf) = {r_lor:>8.4f}   p = {p_lor:.2e}
  LOO-CV r (Lorentz)           = {r_loo_lor:>8.4f}   R² = {r2_loo_lor:.4f}
  AIC linear                   = {aic_lin:>8.2f}
  AIC Lorentz                  = {aic_lor:>8.2f}  {'← WINS' if aic_lor < aic_lin else ''}

{'='*90}
  SPECTRUM
{'='*90}
  Two-state mean Sarrus   = {np.mean(S):>8.3f}  (n={n})
  Multi-state mean Sarrus = {np.mean([r['sarrus'] for r in ms_results]):>8.3f}  (n={len(ms_results)})
  Multi-state r(S, ln_kf) = {r_ms:>8.4f}  (p={p_ms:.2e})
  IDP mean Sarrus         = {np.mean(idp_sarrus):>8.3f}  (n={len(idp_sarrus)})
""")
    
    # ─── Plots ───
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1: Primary scatter (Sarrus vs ln_kf)
    ax = axes[0, 0]
    ax.scatter(S, Y, c='steelblue', s=70, alpha=0.8, edgecolors='white', linewidth=0.5, zorder=3)
    sl, il = np.polyfit(S, Y, 1)
    xf = np.linspace(S.min() - 0.5, S.max() + 0.5, 200)
    ax.plot(xf, sl * xf + il, 'k--', alpha=0.5)
    for r in ts_results:
        if r['status'] == 'OVERRIDE' and r['pdb'] in ('1LMB', '1HZ6', '2CI2'):
            ax.annotate(r['pdb'], (r['sarrus'], r['ln_kf']), fontsize=7,
                       color='red', alpha=0.8, xytext=(5, 5), textcoords='offset points')
    ax.set_xlabel('Sarrus Linkage S')
    ax.set_ylabel('ln(kf)')
    ax.set_title(f'Primary: n={n}, r={r_pear:.3f}, perm p={pp:.4f}')
    ax.grid(True, alpha=0.3)
    
    # 2: Lorentz bridge
    ax = axes[0, 1]
    ax.scatter(sigma_rank, Y, c='steelblue', s=70, alpha=0.8, edgecolors='white', linewidth=0.5, zorder=3)
    sig_c = np.linspace(0.01, 0.95, 200)
    sl_l, il_l = np.polyfit(lor_term, Y, 1)
    ax.plot(sig_c, sl_l * 0.5 * np.log(1 - sig_c**2) + il_l, 'r-', linewidth=2.5, 
            label=f'Lorentz (r={r_lor:.3f})', alpha=0.8)
    sl_s, il_s = np.polyfit(sigma_rank, Y, 1)
    ax.plot(sig_c, sl_s * sig_c + il_s, 'b--', linewidth=1.5, label='Linear', alpha=0.7)
    ax.set_xlabel('σ (rank-based)')
    ax.set_ylabel('ln(kf)')
    ax.set_title('Lorentz Bridge (Corrected)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 3: LOO-CV comparison
    ax = axes[0, 2]
    ax.scatter(preds_lin, Y, c='steelblue', s=60, alpha=0.7, label=f'Linear R²={r2_loo:.3f}', zorder=3)
    ax.scatter(preds_lor, Y, c='red', s=60, alpha=0.7, marker='s', label=f'Lorentz R²={r2_loo_lor:.3f}', zorder=3)
    mn, mx = min(Y.min(), preds_lin.min(), preds_lor.min()) - 1, max(Y.max(), preds_lin.max(), preds_lor.max()) + 1
    ax.plot([mn, mx], [mn, mx], 'k--', alpha=0.5)
    ax.set_xlabel('LOO Predicted ln(kf)')
    ax.set_ylabel('Observed ln(kf)')
    ax.set_title('LOO-CV: Linear vs Lorentz')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # 4: Spectrum (two-state vs multi-state vs IDP)
    ax = axes[1, 0]
    ax.scatter(S, Y, c='steelblue', s=60, alpha=0.8, label=f'Two-state (n={n})')
    if ms_results:
        Sm = np.array([r['sarrus'] for r in ms_results])
        Ym = np.array([r['ln_kf'] for r in ms_results])
        ax.scatter(Sm, Ym, c='orange', s=60, marker='s', alpha=0.8, label=f'Multi-state (n={len(ms_results)})')
    for i, (nm, sv) in enumerate(zip(IDP_CONTROLS.keys(), idp_sarrus)):
        ax.axvline(sv, linestyle=':', color='red', alpha=0.6, label='IDP' if i==0 else None)
    ax.set_xlabel('Sarrus Linkage S')
    ax.set_ylabel('ln(kf)')
    ax.set_title('The Folding Spectrum')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    
    # 5: Contact order comparison
    ax = axes[1, 1]
    ax.scatter(CO, Y, c='gray', s=60, alpha=0.7, label=f'CO (r={r_co:.3f})')
    sl_co, il_co = np.polyfit(CO, Y, 1)
    xco = np.linspace(CO.min() - 1, CO.max() + 1, 200)
    ax.plot(xco, sl_co * xco + il_co, 'k--', alpha=0.5)
    ax.set_xlabel('Relative Contact Order (%)')
    ax.set_ylabel('ln(kf)')
    ax.set_title(f'Benchmark: Contact Order r={r_co:.3f}')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # 6: Cross-domain gamma
    ax = axes[1, 2]
    beta_range = np.linspace(0, 0.999, 500)
    gamma_sr = 1 / np.sqrt(1 - beta_range**2)
    ax.plot(beta_range, gamma_sr, 'k-', linewidth=3, alpha=0.5, label='γ = 1/√(1−σ²)')
    kf = np.exp(Y)
    R0 = np.max(kf) * 1.1
    gamma_bio = R0 / kf
    ax.scatter(sigma_rank, gamma_bio, c='steelblue', s=80, alpha=0.8, zorder=3,
               edgecolors='white', linewidth=0.5, label='Two-state folders')
    ax.set_xlabel('σ (constraint saturation)')
    ax.set_ylabel('γ (latency factor)')
    ax.set_title('Cross-Domain: One Geometry')
    ax.set_yscale('log')
    ax.set_ylim(0.5, 1000)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.suptitle(f'NEXUS DEFINITIVE — v10 Canonical Pipeline | n={n} | '
                 f'r={r_pear:.3f} | Lorentz AIC={aic_lor:.1f}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    out_png = '/mnt/user-data/outputs/nexus_definitive.png'
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    print(f"  Saved: {out_png}")
    
    # Save JSON manifest
    manifest = {
        'timestamp': ts,
        'pipeline': 'v10_canonical',
        'n_two_state': n,
        'n_multi_state': len(ms_results),
        'n_idp': len(idp_sarrus),
        'pearson_r': round(r_pear, 4),
        'pearson_p': float(f'{p_pear:.2e}'),
        'permutation_p': pp,
        'partial_r': round(float(r_part), 4),
        'loo_r': round(r_loo, 4),
        'loo_r2': round(r2_loo, 4),
        'lorentz_r': round(r_lor, 4),
        'lorentz_loo_r2': round(r2_loo_lor, 4),
        'aic_linear': round(aic_lin, 2),
        'aic_lorentz': round(aic_lor, 2),
        'co_r': round(r_co, 4),
        'multi_state_r': round(float(r_ms), 4) if np.isfinite(r_ms) else None,
        'two_state_mean_sarrus': round(float(np.mean(S)), 3),
        'idp_mean_sarrus': round(float(np.mean(idp_sarrus)), 3),
        'scale': 'MJ_v10_burial_energy',
        'shuffle_method': 'aa_list_remap',
        'std_ddof': 0,
        'overrides': list(OVERRIDES.keys()),
        'proteins': [
            {'pdb': r['pdb'], 'name': r['name'], 'len': r['len'], 
             'sarrus': round(r['sarrus'], 4), 'ln_kf': r['ln_kf'], 
             'status': r['status']}
            for r in ts_results
        ],
    }
    
    json_path = '/mnt/user-data/outputs/nexus_definitive_manifest.json'
    with open(json_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"  Saved: {json_path}")
    
    return manifest


if __name__ == "__main__":
    manifest = run_pipeline()
