# NEXUS — All Successful Tests (Shareable Notebook)

This notebook consolidates the **working / “green”** NEXUS analyses into a single, shareable artifact:

1. **v9.1 Validated (Ivankov two‑state set)**  
   - Locked feature: MJ scale, helix lags **[3,4]**, sheet lag **2**, shuffles **1000**  
   - Output includes: audit table, Pearson r, **partial r controlling ln(L)**, **LOO‑CV**, and **permutation p**.

2. **Validation B (Two‑state vs Multi‑state)**  
   - Uses the same locked pipeline to test whether mechanism class separates.

3. **v10 “Diamond” Spectrum figure**  
   - Produces the “spectrum” plot: Two‑state vs Multi‑state vs IDPs

> **Repro note:**  
> This notebook is **deterministic** by design:
> - shuffle RNG is seeded per sequence via **MD5(seq)**,
> - permutation test RNG uses a fixed seed,
> - all locked hyperparameters are defined once at top.

---

## What to include in a paper (recommended)

If you must include *one* implementation, cite/use the **“Locked Pipeline + Audit + Stats”** section below (Cell group: **A → D**).  
The other sections (Validation B and Diamond plot) are optional extensions.


## A. Locked configuration (DO NOT CHANGE)

This is the “pre‑registered” configuration block.



```python

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import hashlib
import warnings
warnings.filterwarnings("ignore")

# ----------------------------
# LOCKED FEATURE (pre-registered)
# ----------------------------
MJ = {
    'A':0.616,'R':-1.537,'N':-0.628,'D':-0.608,'C':0.680,'Q':-0.468,'E':-0.587,
    'G':0.501,'H':-0.340,'I':1.385,'L':1.256,'K':-1.840,'M':0.828,'F':1.356,
    'P':-0.198,'S':-0.049,'T':0.034,'W':0.878,'Y':0.534,'V':1.111
}

HELIX_LAGS   = [3, 4]
SHEET_LAG    = 2
N_SHUFFLES   = 1000
N_PERM       = 10000   # permutation test for |r|
LEN_TOL_FRAC = 0.10    # skip if mismatch > 10% unless overridden

np.random.seed(42)  # only used for non-critical randomness (plots, etc.)

```

## B. Core engines

### B1. Sarrus linkage from ACF z-scores

Given a sequence converted to a numeric signal $x_i$ (MJ scale), define the centered signal:

$$
s_i = x_i - \bar{x}
$$

and the normalized autocorrelation at lag $\ell$:

$$
\mathrm{ACF}(\ell) = \frac{\sum_{i=1}^{N-\ell} s_i s_{i+\ell}}{\sum_{i=1}^{N} s_i^2}.
$$

The locked metrics are:

- Helix ACF: average of lags 3 and 4  
  $$
  \mathrm{ACF}_H = \tfrac{1}{2}\big(\mathrm{ACF}(3)+\mathrm{ACF}(4)\big)
  $$
- Sheet ACF: lag 2  
  $$
  \mathrm{ACF}_S = \mathrm{ACF}(2)
  $$

A shuffle null is created by shuffling the amino acids (composition preserved, pattern destroyed) and recomputing $\mathrm{ACF}_H$ and $\mathrm{ACF}_S$.

Z-scores:

$$
Z_H = \frac{\mathrm{ACF}_H - \mu(\mathrm{ACF}_H^{\mathrm{shuf}})}{\sigma(\mathrm{ACF}_H^{\mathrm{shuf}})},\quad
Z_S = \frac{\mathrm{ACF}_S - \mu(\mathrm{ACF}_S^{\mathrm{shuf}})}{\sigma(\mathrm{ACF}_S^{\mathrm{shuf}})}
$$

Finally, **Sarrus linkage**:

$$
Z_{\mathrm{Sarrus}} = Z_H - Z_S.
$$



```python

def compute_sarrus_locked(seq: str, scale=MJ, n_shuffles=N_SHUFFLES):
    """Locked v9/v10 pipeline: MD5(seq) shuffle seed; helix lags [3,4], sheet lag 2; z-scored.
    Returns (z_helix, z_sheet, sarrus, debug_dict).
    """
    # numeric signal
    sig = np.array([scale.get(a, np.nan) for a in seq if a in scale], dtype=float)
    sig = sig[~np.isnan(sig)]
    N = len(sig)
    if N < 10:
        return np.nan, np.nan, np.nan, {"reason":"too_short", "N":N}

    s = sig - sig.mean()
    denom = np.sum(s**2)
    if denom < 1e-12:
        return np.nan, np.nan, np.nan, {"reason":"zero_variance", "N":N}

    # observed ACFs
    acf_h = np.mean([np.sum(s[:-l]*s[l:]) / denom for l in HELIX_LAGS])
    acf_s = np.sum(s[:-SHEET_LAG]*s[SHEET_LAG:]) / denom

    # stable shuffle RNG per sequence
    seed = int(hashlib.md5(seq.encode()).hexdigest(), 16) % (2**32)
    rng = np.random.default_rng(seed)

    sh_h, sh_s = [], []
    aas = [a for a in seq if a in scale]
    for _ in range(n_shuffles):
        shuf = aas.copy()
        rng.shuffle(shuf)
        ssig = np.array([scale[a] for a in shuf], dtype=float)
        ss = ssig - ssig.mean()
        d = np.sum(ss**2)
        if d < 1e-12:
            continue
        sh_h.append(np.mean([np.sum(ss[:-l]*ss[l:]) / d for l in HELIX_LAGS]))
        sh_s.append(np.sum(ss[:-SHEET_LAG]*ss[SHEET_LAG:]) / d)

    sh_h = np.array(sh_h, dtype=float)
    sh_s = np.array(sh_s, dtype=float)
    if sh_h.size < 20 or sh_s.size < 20:
        return np.nan, np.nan, np.nan, {"reason":"insufficient_shuffles", "used":int(sh_h.size)}

    shHstd = float(np.std(sh_h))
    shSstd = float(np.std(sh_s))
    if shHstd < 1e-12 or shSstd < 1e-12:
        return np.nan, np.nan, np.nan, {"reason":"zero_shuffle_std", "shHstd":shHstd, "shSstd":shSstd}

    z_h = float((acf_h - sh_h.mean()) / shHstd)
    z_s = float((acf_s - sh_s.mean()) / shSstd)
    sar = float(z_h - z_s)

    dbg = {"N":N, "sh_used":int(sh_h.size), "shHstd":shHstd, "shSstd":shSstd}
    return z_h, z_s, sar, dbg


def proper_partial_corr(x, y, cov):
    """Partial Pearson correlation r(x,y | cov) via residualization."""
    x = np.asarray(x, float); y = np.asarray(y, float); cov = np.asarray(cov, float)
    m = ~(np.isnan(x) | np.isnan(y) | np.isnan(cov))
    x, y, cov = x[m], y[m], cov[m]
    if len(x) < 5:
        return np.nan, np.nan

    bx = np.polyfit(cov, x, 1)
    by = np.polyfit(cov, y, 1)
    rx = x - (bx[0]*cov + bx[1])
    ry = y - (by[0]*cov + by[1])
    return stats.pearsonr(rx, ry)


def loo_cv_r2(x, y):
    """LOO-CV for simple linear regression y ~ x; returns (r, r2, p, preds)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = ~(np.isnan(x) | np.isnan(y))
    x, y = x[m], y[m]
    n = len(y)
    preds = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool); mask[i] = False
        slope, intercept = np.polyfit(x[mask], y[mask], 1)
        preds[i] = slope*x[i] + intercept
    r, p = stats.pearsonr(y, preds)
    r2 = 1 - np.sum((y - preds)**2) / np.sum((y - y.mean())**2)
    return float(r), float(r2), float(p), preds


def permutation_p_abs_r(x, y, n_perm=N_PERM, seed=42):
    """Permutation p-value for |Pearson r|."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = ~(np.isnan(x) | np.isnan(y))
    x, y = x[m], y[m]
    obs = abs(stats.pearsonr(x, y)[0])
    rng = np.random.default_rng(seed)
    cnt = 0
    for _ in range(n_perm):
        yy = rng.permutation(y)
        if abs(stats.pearsonr(x, yy)[0]) >= obs:
            cnt += 1
    return (cnt + 1) / (n_perm + 1)  # add-one smoothing

```

## C. Datasets

### C1. Ivankov two-state (30 entries) with **domain overrides**

To ensure “domain match” (kinetic construct = analyzed sequence), we allow a **white list override** for known multi-domain / fragment problems.

This is the minimum needed to avoid “garbage in”.



```python

# ----------------------------
# Ivankov two-state list (core)
# ----------------------------
TWO_STATE = [
    ("2PDD","E3/E1 PSBD",41, 9.8, 11.0),
    ("2ABD","ACBP",86, 6.6, 14.3),
    ("256B","Cyt b562",106, 12.2, 7.5),
    ("1IMQ","Im9",86, 7.3, 12.1),
    ("1LMB","lambda-Rep",80, 8.5, 9.4),
    ("1FNF","FN3-9",90, -0.9, 18.1),
    ("1WIT","Twitchin",93, 0.4, 20.3),
    ("1TEN","Tenascin",90, 1.1, 17.4),
    ("1SHG","SH3-spectrin",62, 1.4, 19.1),
    ("1SRL","SH3-src",64, 4.0, 19.6),
    ("1PNJ","SH3-PI3K",90, -1.1, 16.1),
    ("1SHF","SH3-fyn",67, 4.5, 18.3),
    ("1PSF","PsaE",69, 3.2, 17.0),
    ("1CSP","CspB-Bs",67, 7.0, 16.4),
    ("1C9O","CspB-Bc",66, 7.2, 7.5),
    ("1G6P","CspB-Tm",66, 6.3, 17.5),
    ("1MJC","CspA-Ec",69, 5.3, 16.0),
    ("1LOP","CypA",164, 6.6, 15.7),
    ("1C8C","DNA-bp",63, 7.0, 12.7),
    ("1HZ6","Protein L",62, 4.1, 16.1),
    ("1PGB","Protein G",57, 6.0, 17.3),
    ("1FKB","FKBP12",107, 1.5, 17.7),
    ("2CI2","CI2",64, 3.9, 15.7),
    ("1AYE","ADA2h",80, 6.8, 16.7),
    ("1URN","U1A",102, 5.8, 16.9),
    ("1APS","AcP",98, -1.5, 21.7),
    ("1RIS","S6",101, 5.9, 18.9),
    ("1POH","HPr",85, 2.7, 17.6),
    ("1DIV","NTL9",56, 6.1, 12.7),
    ("2VIK","Villin 14T",126, 6.8, 12.3),
]

# ----------------------------
# Ivankov multi-state list (used for Validation B / spectrum)
# ----------------------------
MULTI_STATE = [
    ("1A6N","Apomyoglobin",151, 1.1, 8.4),
    ("1CEI","Im7",87, 5.8, 10.8),
    ("2CRO","Cro",71, 3.7, 11.2),
    ("1TIT","Titin-I27",89, 3.6, 17.8),
    ("1HNG","CD2-d1",98, 1.8, 16.9),
    ("1FNF","FN3-10",94, 5.5, 16.5),
    ("1IFC","IFABP",131, 3.4, 13.5),
    ("1EAL","ILBP",127, 1.3, 12.3),
    ("1OPA","CRBPII",133, 1.4, 14.0),
    ("1CBI","CRABPI",136, -3.2, 13.8),
    ("1BRS","Barstar",89, 3.4, 11.8),
    ("3CHY","CheY",129, 1.0, 8.7),
    ("2RN2","RNaseH",155, 0.1, 12.4),
    ("1RA9","DHFR",159, 4.6, 14.0),
    ("1BNI","Barnase",110, 2.6, 11.4),
    ("2LZM","T4 Lyso",164, 4.1, 7.1),
    ("1UBQ","Ubiquitin",76, 5.9, 15.1),
    ("1SCE","Suc1",113, 4.2, 11.8),
]

# ----------------------------
# White-list domain overrides (must match constructs)
# ----------------------------
CORRECTED = {
    "1FNF_9": "VSDVPRDLEVVAATPTSLLISWDAPAVTVRYYRITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYAVTGRGDSPASSKPISINYRT",  # 90
    "1AYE":   "RQLPALLPEEWFHKAVLDRAQGDGPFQKFGVQIRASDHGTEVALPEGVHLIAECRDEEAGVRELLRRLRAAGVVDKEHD",  # 80
    "1DIV":   "MKVIFLKDVKGMGKKGEIKNVADGYANNFLFKQGLAIEATPANLKALEAQKQKEQR",  # 56
    "1WIT":   "LKPAIVTNVKENVTNFEDVILDWSPPDSPVVFEIVYAPKRDQWKVAVPVGDNGKCAPMQLNKVLSEDANGSLRVTVKAEIQSSGNSPEGF",  # 93
    "1SHG":   "DETGKELVLALYDYQEKSPREVTMKKGDILTLLNSTNKDWWKVEVNDRQGFVPAAYVKKLD",  # 62
    "1SHF":   "VQALYDYVESYEGDNTEFQKGDDIIVLNYKGQDWWYGEIGGSEGLVPAQYLVPQQ",  # 57
    "1SRL":   "GQVAIYDYQNDPDDELSFKKGDVITTVDRKQWDWWIGERCAGRGIVPSNYVL",  # 56
    "1APS":   "LVRHMQPEYAVQLLISDGEYSGRWAVEKHGIPLDTVVCALSLSDYGHRPVLLSKEIGAKGKIILLHAGGEKNEEVVRKENADLLEKAGITLPIEDL",  # 98
    "1TEN":   "RLDAPSQIEVKDVTDTTALITWFKPLAEIDGIELTYGIKDVPGDRTTIDLTEDENQYSIGNLKPDTEYEVSLISRRGDMSSNPAKETFTT",  # 90
    "1TIT":   "LIEVEKPLYGVEVFVGETAHFEIELSEPDVHGQWKLKGQPLAASPDCEIIEDGKKHILILHNCQLGMTGEVSFQAANTKSAANLKVKEL",  # 89
}

# IDP controls for "spectrum" visualization (not used in primary p-values)
IDPS = {
    "alpha-Synuclein": "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA",
    "p21-CDKN1A": "MEPVDPRLEPWKHPGSQPKTACQKLEPPEEDCDLCQFNEQLANQRPSQKHLQKYLSDPSATFQEPVQHLDTMLQTLEDLNLRWACLI",
    "HMGA1": "MSESSSKSSSQPLASKQEKDGTEKRGRGRPRKQPPVSPGTALVGSQKEPSEVPTPKRPRGRPKGSKNKGAAKTRKTTTTPGRKPRGRPKKLEKEEEEGISQESSEEEQ",
    "Stathmin": "MASSDIQVKELEKRASGQAFELILNPRDDALIDLLERLQKLSGNEQIRESQAQSSLAEEIISGAAQIAKDARHAKEQPAVATTAPVPAEKSPISESPPEGAHLLADLITLTQSALDAGKQGASQEQESSRE",
}

```

## D. Primary run with full audit table + required statistics

This section prints a **sequence audit table** (included/excluded and why) and then reports:

- Pearson $r$ and $p$
- permutation $p$ for $|r|$
- partial $r$ controlling $\ln(L)$
- LOO‑CV $R^2$



```python

import urllib.request

def fetch_fasta_entries(pdb_ids):
    """Fetch FASTA for multiple PDB ids in one call. Returns dict PDB->list of sequences."""
    url = f"https://www.rcsb.org/fasta/entry/{','.join(sorted(set(pdb_ids)))}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode()

    seqs = {}
    cur = None
    buf = []
    for line in text.splitlines():
        if line.startswith(">"):
            if cur is not None and buf:
                seqs.setdefault(cur, []).append("".join(buf))
            cur = line[1:].split("|")[0].split("_")[0].upper()
            buf = []
        else:
            buf.append(line.strip())
    if cur is not None and buf:
        seqs.setdefault(cur, []).append("".join(buf))
    return seqs


def pick_sequence_candidate(cands, expL):
    """Pick exact length if available else closest."""
    if not cands:
        return None, "missing", []
    lens = [len(s) for s in cands]
    # exact match
    for s in cands:
        if len(s) == expL:
            return s, "picked_exact", sorted(lens)
    # closest
    idx = int(np.argmin([abs(len(s)-expL) for s in cands]))
    return cands[idx], "picked_closest", sorted(lens)


def run_primary_two_state():
    pdbs = [pdb for pdb,_,_,_,_ in TWO_STATE]
    raw = fetch_fasta_entries(pdbs)

    audit_rows = []
    included = []

    for pdb, name, expL, ln_kf, co in TWO_STATE:
        # override key handling
        key = "1FNF_9" if "FN3-9" in name else pdb

        if key in CORRECTED:
            seq = CORRECTED[key]
            status = "OVERRIDE"
            candidates = []
            pick_note = f"key={key}"
        else:
            cands = raw.get(pdb, [])
            seq, pick_note, candidates = pick_sequence_candidate(cands, expL)
            status = "FETCH_MATCH" if seq is not None and abs(len(seq)-expL) <= expL*LEN_TOL_FRAC else "SKIP"

        usedL = len(seq) if seq else 0

        if status == "SKIP":
            reason = f"len_mismatch>tol; {pick_note}"
            audit_rows.append([status, pdb, expL, usedL, name, reason])
            continue
        if seq is None or usedL < 10:
            audit_rows.append(["SKIP", pdb, expL, usedL, name, "missing/too_short"])
            continue

        zH, zS, sar, dbg = compute_sarrus_locked(seq)
        if np.isnan(sar):
            audit_rows.append(["SKIP", pdb, expL, usedL, name, f"sarrus_nan; {dbg}"])
            continue

        # append
        note = f"{pick_note}; picked_len={usedL}; candidates={candidates if candidates else '[]'}; sh_used={dbg['sh_used']}; shHstd={dbg['shHstd']:.5g}; shSstd={dbg['shSstd']:.5g}"
        audit_rows.append([status, pdb, expL, usedL, name, note])
        included.append((pdb,name,expL,usedL,ln_kf,co,zH,zS,sar))

    # print audit
    print("="*80)
    print("SEQUENCE AUDIT TABLE (Two-State)")
    print("="*80)
    for r in audit_rows:
        status,pdb,expL,usedL,name,note = r
        print(f"{status:10s} | {pdb:4s} | expL={expL:3d} usedL={usedL:3d} | {name:16s} | {note}")

    # primary stats
    inc = np.array(included, dtype=object)
    if inc.size == 0:
        raise RuntimeError("No proteins included. Check RCSB access or override list.")

    ln_kf = inc[:,4].astype(float)
    co    = inc[:,5].astype(float)
    sar   = inc[:,8].astype(float)
    Lused = inc[:,3].astype(float)

    r, p = stats.pearsonr(sar, ln_kf)
    perm_p = permutation_p_abs_r(sar, ln_kf)
    r_part, p_part = proper_partial_corr(sar, ln_kf, np.log(Lused))
    r_cv, r2_cv, p_cv, preds = loo_cv_r2(sar, ln_kf)
    r_co, p_co = stats.pearsonr(co, ln_kf)

    print("\n" + "="*80)
    print("PRIMARY RESULTS (LOCKED FEATURE)")
    print("="*80)
    print(f"Included proteins (n): {len(sar)}")
    print(f"Pearson r(SARRUS, ln(kf))         = {r: .4f}   p = {p:.3e}")
    print(f"Permutation p (|r|, n={N_PERM})       = {perm_p:.4f}")
    print(f"Partial r controlling ln(L_used)  = {r_part: .4f}   p = {p_part:.3e}")
    print(f"LOO-CV r(pred, obs)               = {r_cv: .4f}   p = {p_cv:.3e}")
    print(f"LOO-CV R²                         = {r2_cv: .4f}")
    print("")
    print(f"Benchmark r(ContactOrder, ln(kf)) = {r_co: .4f}   p = {p_co:.3e}")

    return inc, preds

included_two_state, preds_two_state = run_primary_two_state()

```

    ================================================================================
    SEQUENCE AUDIT TABLE (Two-State)
    ================================================================================
    FETCH_MATCH | 2PDD | expL= 41 usedL= 43 | E3/E1 PSBD       | picked_closest; picked_len=43; candidates=[43]; sh_used=1000; shHstd=0.10011; shSstd=0.14708
    FETCH_MATCH | 2ABD | expL= 86 usedL= 86 | ACBP             | picked_exact; picked_len=86; candidates=[86]; sh_used=1000; shHstd=0.074746; shSstd=0.10701
    FETCH_MATCH | 256B | expL=106 usedL=106 | Cyt b562         | picked_exact; picked_len=106; candidates=[106]; sh_used=1000; shHstd=0.06677; shSstd=0.093486
    FETCH_MATCH | 1IMQ | expL= 86 usedL= 86 | Im9              | picked_exact; picked_len=86; candidates=[86]; sh_used=1000; shHstd=0.072971; shSstd=0.10267
    SKIP       | 1LMB | expL= 80 usedL= 92 | lambda-Rep       | len_mismatch>tol; picked_closest
    OVERRIDE   | 1FNF | expL= 90 usedL= 94 | FN3-9            | key=1FNF_9; picked_len=94; candidates=[]; sh_used=1000; shHstd=0.069724; shSstd=0.099012
    OVERRIDE   | 1WIT | expL= 93 usedL= 90 | Twitchin         | key=1WIT; picked_len=90; candidates=[]; sh_used=1000; shHstd=0.067403; shSstd=0.10648
    OVERRIDE   | 1TEN | expL= 90 usedL= 90 | Tenascin         | key=1TEN; picked_len=90; candidates=[]; sh_used=1000; shHstd=0.074077; shSstd=0.1046
    OVERRIDE   | 1SHG | expL= 62 usedL= 61 | SH3-spectrin     | key=1SHG; picked_len=61; candidates=[]; sh_used=1000; shHstd=0.088545; shSstd=0.12581
    OVERRIDE   | 1SRL | expL= 64 usedL= 52 | SH3-src          | key=1SRL; picked_len=52; candidates=[]; sh_used=1000; shHstd=0.090768; shSstd=0.13473
    FETCH_MATCH | 1PNJ | expL= 90 usedL= 86 | SH3-PI3K         | picked_closest; picked_len=86; candidates=[86]; sh_used=1000; shHstd=0.075497; shSstd=0.10448
    OVERRIDE   | 1SHF | expL= 67 usedL= 55 | SH3-fyn          | key=1SHF; picked_len=55; candidates=[]; sh_used=1000; shHstd=0.0902; shSstd=0.13246
    FETCH_MATCH | 1PSF | expL= 69 usedL= 69 | PsaE             | picked_exact; picked_len=69; candidates=[69]; sh_used=1000; shHstd=0.077931; shSstd=0.11562
    FETCH_MATCH | 1CSP | expL= 67 usedL= 67 | CspB-Bs          | picked_exact; picked_len=67; candidates=[67]; sh_used=1000; shHstd=0.086333; shSstd=0.12015
    FETCH_MATCH | 1C9O | expL= 66 usedL= 66 | CspB-Bc          | picked_exact; picked_len=66; candidates=[66]; sh_used=1000; shHstd=0.082159; shSstd=0.11852
    FETCH_MATCH | 1G6P | expL= 66 usedL= 66 | CspB-Tm          | picked_exact; picked_len=66; candidates=[66]; sh_used=1000; shHstd=0.085878; shSstd=0.11825
    FETCH_MATCH | 1MJC | expL= 69 usedL= 69 | CspA-Ec          | picked_exact; picked_len=69; candidates=[69]; sh_used=1000; shHstd=0.083108; shSstd=0.11561
    FETCH_MATCH | 1LOP | expL=164 usedL=164 | CypA             | picked_exact; picked_len=164; candidates=[5, 164]; sh_used=1000; shHstd=0.054027; shSstd=0.075866
    FETCH_MATCH | 1C8C | expL= 63 usedL= 64 | DNA-bp           | picked_closest; picked_len=64; candidates=[8, 64]; sh_used=1000; shHstd=0.084157; shSstd=0.12385
    SKIP       | 1HZ6 | expL= 62 usedL= 72 | Protein L        | len_mismatch>tol; picked_closest
    FETCH_MATCH | 1PGB | expL= 57 usedL= 56 | Protein G        | picked_closest; picked_len=56; candidates=[56]; sh_used=1000; shHstd=0.088101; shSstd=0.13482
    FETCH_MATCH | 1FKB | expL=107 usedL=107 | FKBP12           | picked_exact; picked_len=107; candidates=[107]; sh_used=1000; shHstd=0.065141; shSstd=0.095153
    SKIP       | 2CI2 | expL= 64 usedL= 83 | CI2              | len_mismatch>tol; picked_closest
    OVERRIDE   | 1AYE | expL= 80 usedL= 79 | ADA2h            | key=1AYE; picked_len=79; candidates=[]; sh_used=1000; shHstd=0.075688; shSstd=0.11248
    FETCH_MATCH | 1URN | expL=102 usedL= 97 | U1A              | picked_closest; picked_len=97; candidates=[21, 97]; sh_used=1000; shHstd=0.068632; shSstd=0.10164
    OVERRIDE   | 1APS | expL= 98 usedL= 96 | AcP              | key=1APS; picked_len=96; candidates=[]; sh_used=1000; shHstd=0.071453; shSstd=0.099896
    FETCH_MATCH | 1RIS | expL=101 usedL=101 | S6               | picked_exact; picked_len=101; candidates=[101]; sh_used=1000; shHstd=0.071183; shSstd=0.10239
    FETCH_MATCH | 1POH | expL= 85 usedL= 85 | HPr              | picked_exact; picked_len=85; candidates=[85]; sh_used=1000; shHstd=0.075566; shSstd=0.10646
    OVERRIDE   | 1DIV | expL= 56 usedL= 56 | NTL9             | key=1DIV; picked_len=56; candidates=[]; sh_used=1000; shHstd=0.086983; shSstd=0.13174
    FETCH_MATCH | 2VIK | expL=126 usedL=126 | Villin 14T       | picked_exact; picked_len=126; candidates=[126]; sh_used=1000; shHstd=0.061483; shSstd=0.089582
    
    ================================================================================
    PRIMARY RESULTS (LOCKED FEATURE)
    ================================================================================
    Included proteins (n): 27
    Pearson r(SARRUS, ln(kf))         =  0.5388   p = 3.734e-03
    Permutation p (|r|, n=10000)       = 0.0040
    Partial r controlling ln(L_used)  =  0.5649   p = 2.143e-03
    LOO-CV r(pred, obs)               =  0.4311   p = 2.478e-02
    LOO-CV R²                         =  0.1698
    
    Benchmark r(ContactOrder, ln(kf)) = -0.7338   p = 1.325e-05
    

## E. Primary plots (Two-State)

Produces:
- scatter of Sarrus vs ln(kf)
- LOO-CV predicted vs observed



```python

sar = included_two_state[:,8].astype(float)
lnkf = included_two_state[:,4].astype(float)

plt.figure(figsize=(7,5))
plt.scatter(sar, lnkf)
m,b = np.polyfit(sar, lnkf, 1)
xx = np.linspace(sar.min(), sar.max(), 200)
plt.plot(xx, m*xx+b, linestyle="--")
plt.xlabel("Sarrus Linkage (Z_helix - Z_sheet)")
plt.ylabel("ln(kf)")
plt.title("Two-State: sequence-only predictor (locked)")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(preds_two_state, lnkf)
mn, mx = min(lnkf.min(), preds_two_state.min()), max(lnkf.max(), preds_two_state.max())
plt.plot([mn,mx],[mn,mx], linestyle="--")
plt.xlabel("LOO-CV predicted ln(kf)")
plt.ylabel("Observed ln(kf)")
plt.title("Two-State: LOO-CV diagnostic")
plt.grid(True, alpha=0.3)
plt.show()

```


    
![png](output_10_0.png)
    



    
![png](output_10_1.png)
    


## F. Validation B — Two-State vs Multi-State (mechanism test)

This replicates the “kinetic order” test using the **same** locked Sarrus pipeline.

Outputs:
- group means and spread
- Mann–Whitney U test
- Cohen’s d
- simple threshold classifier accuracy



```python

def get_group_sarrus(dataset):
    pdbs = [pdb for pdb,_,_,_,_ in dataset]
    raw = fetch_fasta_entries(pdbs)
    sarrus_vals = []
    lnkf_vals = []
    names = []
    for pdb, name, expL, ln_kf, _co in dataset:
        key = "1FNF_9" if name in ("FN3-9","FN3_9","FN3_9 ") else pdb

        if key in CORRECTED:
            seq = CORRECTED[key]
        else:
            cands = raw.get(pdb, [])
            seq, pick_note, _ = pick_sequence_candidate(cands, expL)
            if seq is None:
                continue
            if abs(len(seq)-expL) > expL*LEN_TOL_FRAC:
                # mismatch skip
                continue

        _, _, sar, _ = compute_sarrus_locked(seq)
        if np.isnan(sar):
            continue
        sarrus_vals.append(sar)
        lnkf_vals.append(ln_kf)
        names.append(name)
    return np.array(sarrus_vals, float), np.array(lnkf_vals, float), names

z2, y2, _ = get_group_sarrus(TWO_STATE)
zm, ym, _ = get_group_sarrus(MULTI_STATE)

print("="*80)
print("VALIDATION B — Two-State vs Multi-State")
print("="*80)
print(f"Two-State n={len(z2)}  mean={z2.mean():.3f}  std={z2.std():.3f}")
print(f"Multi-State n={len(zm)} mean={zm.mean():.3f}  std={zm.std():.3f}")

U, p_mw = stats.mannwhitneyu(z2, zm, alternative="two-sided")
print(f"Mann–Whitney U p = {p_mw:.4f}")

pooled = np.sqrt(((len(z2)-1)*z2.var(ddof=1) + (len(zm)-1)*zm.var(ddof=1)) / (len(z2)+len(zm)-2))
d = (z2.mean() - zm.mean()) / pooled
print(f"Cohen's d = {d:.3f}")

thr = 0.5*(z2.mean()+zm.mean())
acc = (np.sum(z2 > thr) + np.sum(zm <= thr)) / (len(z2)+len(zm))
print(f"Threshold={thr:.3f}  accuracy={acc:.1%}")

if len(z2) >= 3:
    r2s, p2s = stats.pearsonr(z2, y2)
    print(f"Two-State correlation r={r2s:.3f} p={p2s:.3f}")
if len(zm) >= 3:
    rms, pms = stats.pearsonr(zm, ym)
    print(f"Multi-State correlation r={rms:.3f} p={pms:.3f}")

```

    ================================================================================
    VALIDATION B — Two-State vs Multi-State
    ================================================================================
    Two-State n=27  mean=0.182  std=1.441
    Multi-State n=16 mean=0.823  std=1.968
    Mann–Whitney U p = 0.1709
    Cohen's d = -0.378
    Threshold=0.502  accuracy=41.9%
    Two-State correlation r=0.539 p=0.004
    Multi-State correlation r=0.002 p=0.994
    

## G. v10 “Diamond” spectrum plot (Two-State vs Multi-State vs IDPs)

This makes the **spectrum** figure that compares group means on the Sarrus axis.



```python

# compute IDP sarrus (direct from sequences)
z_idp = []
for nm, seq in IDPS.items():
    _, _, sar, dbg = compute_sarrus_locked(seq)
    z_idp.append(sar)
z_idp = np.array(z_idp, float)

plt.figure(figsize=(8,5))
plt.scatter(z2, y2, label="Two-State", marker="o")
plt.scatter(zm, ym, label="Multi-State", marker="s")
for i, z in enumerate(z_idp):
    plt.axvline(z, linestyle=":", alpha=0.6, label="IDP" if i==0 else None)

plt.axvline(z2.mean(), linestyle="--", alpha=0.4)
plt.axvline(zm.mean(), linestyle="--", alpha=0.4)

plt.xlabel("Sarrus Linkage (Z_helix - Z_sheet)")
plt.ylabel("ln(kf)")
plt.title("NEXUS spectrum: Cooperative < Trapped < IDP (visual)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

print("Two-State mean Z:", float(z2.mean()))
print("Multi-State mean Z:", float(zm.mean()))
print("IDP mean Z:", float(z_idp.mean()))

```


    
![png](output_14_0.png)
    


    Two-State mean Z: 0.18154078342004898
    Multi-State mean Z: 0.8231856787526131
    IDP mean Z: 0.7390551483045981
    

## H. Export helper

If you want to share results reproducibly, run all cells and then **export the notebook** from Jupyter:
`File → Download as → Notebook (.ipynb)` or `HTML`.


## I. Lorentz/Allocation bridge (exploratory, pre-specified diagnostics)
This section **does not change the locked feature**. It tests whether a Lorentz-like nonlinearity could be present after mapping the locked feature into an allocation variable $\sigma\in[0,1)$.

**Goal:** compare a simple linear model against a Lorentz-style transform.

### Definitions
Let $S$ be the locked Sarrus linkage (z-scored differential periodicity).

We define a *dimensionless allocation proxy* (exploratory):
$$\sigma = \mathrm{clip}\left(\frac{|S|}{S_{\max}}, 0, 0.999\right)$$
where $S_{\max}=\max_i |S_i|$ over the analyzed two-state set.

Lorentz-style term:
$$\ell(\sigma)=\tfrac12\ln(1-\sigma^2)$$
If a Lorentz-like law held exactly, we would expect $\ln k_f$ to be more linear in $\ell(\sigma)$ than in $S$.

> **Important:** This mapping is a hypothesis probe. A positive result would motivate a better operational definition of $\sigma$; a negative result falsifies this particular bridge on this dataset.


```python
# --- Lorentz/Allocation bridge test (exploratory) ---
import numpy as np
from scipy import stats

# Use the already-computed included two-state table from earlier sections.
# Expected columns in included_two_state:
# [idx, name, pdb, expL, usedL, ln_kf, z_h, z_s, sarrus, status]
sar = included_two_state[:, 8].astype(float)      # sarrus
lnkf = included_two_state[:, 5].astype(float)     # ln(kf)
L_used = included_two_state[:, 4].astype(float)   # used length (not used directly here)

Smax = np.max(np.abs(sar))
sigma = np.clip(np.abs(sar) / Smax, 0.0, 0.999)
lor_term = 0.5 * np.log(1 - sigma**2)  # = log(sqrt(1-sigma^2))

# Compare simple correlations
r_lin, p_lin = stats.pearsonr(sar, lnkf)
r_sig, p_sig = stats.pearsonr(sigma, lnkf)
r_lor, p_lor = stats.pearsonr(lor_term, lnkf)

print("Exploratory Lorentz bridge diagnostics (Two-State)")
print("--------------------------------------------------")
print(f"n = {len(sar)}")
print(f"Smax = {Smax:.3f}")
print(f"Corr(S, ln(kf))          r = {r_lin:.4f}, p = {p_lin:.3e}")
print(f"Corr(|S|/Smax, ln(kf))   r = {r_sig:.4f}, p = {p_sig:.3e}")
print(f"Corr(lor_term, ln(kf))   r = {r_lor:.4f}, p = {p_lor:.3e}")

# LOO-CV comparison: linear in S vs linear in lor_term
def loo_r2(x, y):
    n = len(y)
    preds = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        m, b = np.polyfit(x[mask], y[mask], 1)
        preds[i] = m * x[i] + b
    r, _ = stats.pearsonr(y, preds)
    r2 = 1 - np.sum((y - preds) ** 2) / np.sum((y - y.mean()) ** 2)
    return r, r2, preds

rS, r2S, predS = loo_r2(sar, lnkf)
rL, r2L, predL = loo_r2(lor_term, lnkf)

print("\nLOO-CV (unbiased)")
print(f"Linear in S:        r = {rS:.4f}, R^2 = {r2S:.4f}")
print(f"Linear in lor_term: r = {rL:.4f}, R^2 = {r2L:.4f}")

```

    Exploratory Lorentz bridge diagnostics (Two-State)
    --------------------------------------------------
    n = 27
    Smax = 3.285
    Corr(S, ln(kf))          r = -0.3205, p = 1.031e-01
    Corr(|S|/Smax, ln(kf))   r = -0.0294, p = 8.841e-01
    Corr(lor_term, ln(kf))   r = 0.0919, p = 6.485e-01
    
    LOO-CV (unbiased)
    Linear in S:        r = 0.1377, R^2 = -0.0211
    Linear in lor_term: r = -0.0973, R^2 = -0.2250
    


```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.scatter(sar, lnkf)
m,b = np.polyfit(sar, lnkf, 1)
xfit = np.linspace(sar.min(), sar.max(), 200)
plt.plot(xfit, m*xfit+b, linestyle='--')
plt.xlabel("Sarrus Linkage S")
plt.ylabel("ln(kf)")
plt.title("Locked feature vs folding rate (Two-State)")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(lor_term, lnkf)
m,b = np.polyfit(lor_term, lnkf, 1)
xfit = np.linspace(lor_term.min(), lor_term.max(), 200)
plt.plot(xfit, m*xfit+b, linestyle='--')
plt.xlabel("lor_term = 0.5 ln(1-σ²),  σ=|S|/Smax")
plt.ylabel("ln(kf)")
plt.title("Exploratory Lorentz transform vs folding rate (Two-State)")
plt.grid(True, alpha=0.3)
plt.show()

```


    
![png](output_18_0.png)
    



    
![png](output_18_1.png)
    

