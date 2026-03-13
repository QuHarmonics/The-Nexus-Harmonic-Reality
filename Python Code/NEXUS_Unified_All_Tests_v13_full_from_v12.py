import numpy as np
import pandas as pd
import hashlib
import urllib.request
from scipy import stats
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

np.set_printoptions(suppress=True, precision=6)
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 50)


# =============================================================================
# LOCKED CONFIGURATION (DO NOT CHANGE AFTER RELEASE)
# =============================================================================

LOCK = {
    "SCALE": "MJ",
    "HELIX_LAGS": [3, 4],
    "SHEET_LAG": 2,
    "N_SHUFFLES": 1000,
    "N_PERM": 10000,
    "LEN_TOL_FRAC": 0.10,     # 10% mismatch -> skip unless overridden
}

# Miyazawa–Jernigan scale (locked values used throughout the project)
MJ_SCALE = {
    'C': 1.36, 'F': 1.27, 'I': 1.24, 'L': 1.21, 'V': 1.13,
    'W': 1.08, 'M': 0.99, 'A': 0.61, 'G': 0.01, 'P': -0.14,
    'Y': -0.23, 'T': -0.25, 'S': -0.38, 'H': -0.65, 'Q': -0.69,
    'N': -0.78, 'E': -0.91, 'K': -1.18, 'D': -1.23, 'R': -1.62
}


# -----------------------------------------------------------------------------
# Corrected / overridden constructs (explicit domain enforcement)
# -----------------------------------------------------------------------------
CORRECTED_CONSTRUCTS = {
    # Key naming for disambiguation where needed
    "1FNF_9":  "VSDVPRDLEVVAATPTSLLISWDAPAVTVRYYRITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYAVTGRGDSPASSKPISINYRT",
    "1AYE":    "RQLPALLPEEWFHKAVLDRAQGDGPFQKFGVQIRASDHGTEVALPEGVHLIAECRDEEAGVRELLRRLRAAGVVDKEHD",
    "1DIV":    "MKVIFLKDVKGMGKKGEIKNVADGYANNFLFKQGLAIEATPANLKALEAQKQKEQR",
    "1WIT":    "LKPAIVTNVKENVTNFEDVILDWSPPDSPVVFEIVYAPKRDQWKVAVPVGDNGKCAPMQLNKVLSEDANGSLRVTVKAEIQSSGNSPEGF",
    "1SHG":    "DETGKELVLALYDYQEKSPREVTMKKGDILTLLNSTNKDWWKVEVNDRQGFVPAAYVKKLD",
    "1SHF":    "VQALYDYVESYEGDNTEFQKGDDIIVLNYKGQDWWYGEIGGSEGLVPAQYLVPQQ",
    "1SRL":    "GQVAIYDYQNDPDDELSFKKGDVITTVDRKQWDWWIGERCAGRGIVPSNYVL",
    "1APS":    "LVRHMQPEYAVQLLISDGEYSGRWAVEKHGIPLDTVVCALSLSDYGHRPVLLSKEIGAKGKIILLHAGGEKNEEVVRKENADLLEKAGITLPIEDL",
    "1TEN":    "RLDAPSQIEVKDVTDTTALITWFKPLAEIDGIELTYGIKDVPGDRTTIDLTEDENQYSIGNLKPDTEYEVSLISRRGDMSSNPAKETFTT",
    "1TIT":    "LIEVEKPLYGVEVFVGETAHFEIELSEPDVHGQWKLKGQPLAASPDCEIIEDGKKHILILHNCQLGMTGEVSFQAANTKSAANLKVKEL",
}

# -----------------------------------------------------------------------------
# Two-state benchmark: (pdb_id, label, expected_length, ln(kf))
# -----------------------------------------------------------------------------
TWO_STATE = [
    ("2PDD", "PSBD", 41, 9.8),
    ("2ABD", "ACBP", 86, 6.6),
    ("256B", "Cyt_b562", 106, 12.2),
    ("1IMQ", "Im9", 86, 7.3),
    ("1LMB", "lambda_Rep", 80, 8.5),
    ("1FNF", "FN3_9", 90, -0.9),
    ("1WIT", "Twitchin", 93, 0.4),
    ("1TEN", "Tenascin", 90, 1.1),
    ("1SHG", "SH3_spectrin", 62, 1.4),
    ("1SRL", "SH3_src", 64, 4.0),
    ("1PNJ", "SH3_PI3K", 90, -1.1),
    ("1SHF", "SH3_fyn", 67, 4.5),
    ("1PSF", "PsaE", 69, 3.2),
    ("1CSP", "CspB_Bs", 67, 7.0),
    ("1C9O", "CspB_Bc", 66, 7.2),
    ("1G6P", "CspB_Tm", 66, 6.3),
    ("1MJC", "CspA_Ec", 69, 5.3),
    ("1LOP", "CypA", 164, 6.6),
    ("1C8C", "DNA_bp", 63, 7.0),
    ("1HZ6", "Protein_L", 62, 4.1),
    ("1PGB", "Protein_G", 57, 6.0),
    ("1FKB", "FKBP12", 107, 1.5),
    ("2CI2", "CI2", 64, 3.9),
    ("1AYE", "ADA2h", 80, 6.8),
    ("1URN", "U1A", 102, 5.8),
    ("1APS", "AcP", 98, -1.5),
    ("1RIS", "S6", 101, 5.9),
    ("1POH", "HPr", 85, 2.7),
    ("1DIV", "NTL9", 56, 6.1),
    ("2VIK", "Villin_14T", 126, 6.8),
]

# -----------------------------------------------------------------------------
# Multi-state set (for the "spectrum" plot; correlation is expected to be weak/flat)
# -----------------------------------------------------------------------------
MULTI_STATE = [
    ("1A6N", "Apomyoglobin", 151, 1.1),
    ("1CEI", "Im7", 87, 5.8),
    ("2CRO", "Cro", 71, 3.7),
    ("1TIT", "Titin_I27", 89, 3.6),
    ("1HNG", "CD2_d1", 98, 1.8),
    ("1FNF", "FN3_10", 94, 5.5),
    ("1IFC", "IFABP", 131, 3.4),
    ("1EAL", "ILBP", 127, 1.3),
    ("1OPA", "CRBPII", 133, 1.4),
    ("1CBI", "CRABPI", 136, -3.2),
    ("1BRS", "Barstar", 89, 3.4),
    ("3CHY", "CheY", 129, 1.0),
    ("2RN2", "RNaseH", 155, 0.1),
    ("1RA9", "DHFR", 159, 4.6),
    ("1BNI", "Barnase", 110, 2.6),
    ("2LZM", "T4_Lyso", 164, 4.1),
    ("1UBQ", "Ubiquitin", 76, 5.9),
    ("1SCE", "Suc1", 113, 4.2),
]

# -----------------------------------------------------------------------------
# IDP controls (sequence-only controls; ln(kf) not applicable)
# -----------------------------------------------------------------------------
IDP_SEQS = {
    "a-Synuclein": "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA",
    "Tau_K18":      "MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKESPLQTPTEDGSEEPGSETSDAKSTPTAEDVTAPLVDEGAPGQKGQAAAQPHTKG",
    "FUS_LCD":      "MSNQSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSYGQQSSSYGQQSSSYGQQSSSYGQQSSSYGQQSSSYGQQSSSYGQQSSSYGQQSSS",
    "NDP_kinase":   "MNKDRKYYLIVGDVGPEMGKGTQCEKLAEAGADVVVVDRSAGVEVTVEGEVVEKVLAGDTPEEIRHVFGKPVVAMVWEGLNVVKTGR",
}


def md5_seed(seq: str) -> int:
    return int(hashlib.md5(seq.encode("utf-8")).hexdigest(), 16) % (2**32)

def seq_to_signal(seq: str, scale=MJ_SCALE) -> np.ndarray:
    return np.array([scale.get(aa, 0.0) for aa in seq if aa in scale], dtype=float)

def acf_total_energy(signal: np.ndarray, lag: int) -> float:
    n = len(signal)
    if n <= lag or lag <= 0:
        return np.nan
    s = signal - signal.mean()
    denom = np.sum(s**2)
    if denom < 1e-12:
        return np.nan
    return float(np.sum(s[:-lag] * s[lag:]) / denom)

def sarrus_locked(seq: str, n_shuf: int = LOCK["N_SHUFFLES"]) -> dict:
    """Returns Z_H, Z_S, SARRUS and shuffle stds for audit."""
    sig = seq_to_signal(seq)
    if len(sig) < 10:
        return {"z_h": np.nan, "z_s": np.nan, "sarrus": np.nan, "sh_std_h": np.nan, "sh_std_s": np.nan}
    # observed
    H = np.nanmean([acf_total_energy(sig, l) for l in LOCK["HELIX_LAGS"]])
    S = acf_total_energy(sig, LOCK["SHEET_LAG"])
    # shuffles (deterministic per protein)
    seed = md5_seed(seq)
    rng = np.random.default_rng(seed)
    shH, shS = [], []
    for _ in range(n_shuf):
        shuf = sig.copy()
        rng.shuffle(shuf)
        h = np.nanmean([acf_total_energy(shuf, l) for l in LOCK["HELIX_LAGS"]])
        s = acf_total_energy(shuf, LOCK["SHEET_LAG"])
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


USE_RCSB = False  # set True in normal environments with internet

def fetch_rcsb_fasta(pdb_ids):
    url = "https://www.rcsb.org/fasta/entry/" + ",".join(sorted(set(pdb_ids)))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode("utf-8", errors="replace")
    seqs = {}
    cur = None
    buf = []
    for line in text.splitlines():
        if line.startswith(">"):
            if cur is not None:
                seqs[cur] = "".join(buf)
            # take first token, strip chain suffixes like _A
            cur = line[1:].split("|")[0].split("_")[0].upper()
            buf = []
        else:
            buf.append(line.strip())
    if cur is not None:
        seqs[cur] = "".join(buf)
    return seqs

all_pdbs = [p for p,_,_,_ in (TWO_STATE + MULTI_STATE)]
rcsb_seqs = {}
if USE_RCSB:
    try:
        print("Fetching FASTA from RCSB...")
        rcsb_seqs = fetch_rcsb_fasta(all_pdbs)
        print(f"Fetched {len(rcsb_seqs)} FASTA entries.")
    except Exception as e:
        print("RCSB fetch failed (running offline). Error:", e)
        rcsb_seqs = {}
else:
    print("RCSB fetch disabled (offline mode).")


def choose_sequence(pdb_id: str, name: str, exp_len: int, fetched: dict) -> dict:
    # FN3 special keying
    if pdb_id == "1FNF" and name == "FN3_9":
        key = "1FNF_9"
    else:
        key = pdb_id
    # override priority
    if key in CORRECTED_CONSTRUCTS:
        seq = CORRECTED_CONSTRUCTS[key]
        used_len = len(seq)
        return {"status":"OVERRIDE", "seq":seq, "used_len":used_len, "reason":f"key={key}"}
    # fetched
    if pdb_id in fetched:
        seq = fetched[pdb_id]
        used_len = len(seq)
        tol = max(1, int(np.ceil(exp_len * LOCK["LEN_TOL_FRAC"])))
        if abs(used_len - exp_len) <= tol:
            return {"status":"FETCH_MATCH", "seq":seq, "used_len":used_len, "reason":"len_within_tol"}
        else:
            return {"status":"SKIP", "seq":None, "used_len":used_len, "reason":f"len_mismatch>{LOCK['LEN_TOL_FRAC']:.0%} ({used_len} vs {exp_len})"}
    return {"status":"SKIP", "seq":None, "used_len":np.nan, "reason":"missing_fasta_and_no_override"}

def build_audit(dataset, fetched):
    rows = []
    for pdb, name, expL, ln_kf in dataset:
        pick = choose_sequence(pdb, name, expL, fetched)
        if pick["status"] == "SKIP":
            rows.append({
                "STATUS": "SKIP", "PDB": pdb, "NAME": name, "expL": expL, "usedL": pick["used_len"],
                "reason": pick["reason"], "zH": np.nan, "zS": np.nan, "SARRUS": np.nan,
                "shHstd": np.nan, "shSstd": np.nan, "ln_kf": ln_kf
            })
            continue
        metrics = sarrus_locked(pick["seq"], LOCK["N_SHUFFLES"])
        rows.append({
            "STATUS": pick["status"], "PDB": pdb, "NAME": name, "expL": expL, "usedL": pick["used_len"],
            "reason": pick["reason"], "zH": metrics["z_h"], "zS": metrics["z_s"], "SARRUS": metrics["sarrus"],
            "shHstd": metrics["sh_std_h"], "shSstd": metrics["sh_std_s"], "ln_kf": ln_kf
        })
    return pd.DataFrame(rows)

audit_two = build_audit(TWO_STATE, rcsb_seqs)
audit_multi = build_audit(MULTI_STATE, rcsb_seqs)

display(audit_two.head(10))


included_two = audit_two[(audit_two["STATUS"]!="SKIP") & np.isfinite(audit_two["SARRUS"])]
skipped_two = audit_two[audit_two["STATUS"]=="SKIP"]
print(f"Included (two-state): {len(included_two)}")
print(f"Skipped (two-state):  {len(skipped_two)}")
display(skipped_two[["PDB","NAME","expL","usedL","reason"]].head(20))


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
    # residualize
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
    return r, r2, p, preds

S = included_two["SARRUS"].to_numpy(float)
Y = included_two["ln_kf"].to_numpy(float)
L = np.log(included_two["usedL"].to_numpy(float))

r, p = stats.pearsonr(S, Y)
p_perm = permutation_p_abs_r(S, Y, n_perm=LOCK["N_PERM"])
r_part, p_part = partial_corr(S, Y, L)
r_loo, r2_loo, p_loo, preds = loo_linear(S, Y)

print("PRIMARY (locked feature)")
print(f"n = {len(S)}")
print(f"Pearson r(SARRUS, ln(kf)) = {r: .4f}   p = {p: .3e}")
print(f"Permutation p(|r|)        = {p_perm: .4f}   (n_perm={LOCK['N_PERM']})")
print(f"Partial r | ln(L_used)    = {r_part: .4f}   p = {p_part: .3e}")
print(f"LOO-CV r(pred, obs)       = {r_loo: .4f}   p = {p_loo: .3e}")
print(f"LOO-CV R^2                = {r2_loo: .4f}")


def fit_linear_aic(x, y):
    # y = a + b x
    b, a = np.polyfit(x, y, 1)
    resid = y - (a + b*x)
    n = len(y)
    rss = np.sum(resid**2)
    k = 2  # a,b
    # Gaussian AIC up to constant: n*ln(RSS/n) + 2k
    aic = n * np.log(rss / n) + 2*k
    return a, b, aic

def loo_model(x, y, mode="linear"):
    n = len(y)
    preds = np.zeros(n)
    for i in range(n):
        m = np.ones(n, dtype=bool); m[i] = False
        if mode == "linear":
            b, a = np.polyfit(x[m], y[m], 1)
            preds[i] = a + b*x[i]
        elif mode == "lorentz":
            # Stable mid-rank CDF encoder on the training fold (reduces rank-jump artifacts in small n)
            xm = np.asarray(x[m], dtype=float)
            ym = np.asarray(y[m], dtype=float)
            ntr = len(xm)

            # Training sigma: mid-rank CDF = (rank - 0.5)/n
            order = np.argsort(xm)
            ranks = np.empty(ntr, dtype=float)
            ranks[order] = np.arange(1, ntr+1, dtype=float)  # 1..n
            sigma = (ranks - 0.5) / ntr
            sigma = np.clip(sigma, 0.01, 0.99)

            lam = 0.5*np.log(1 - sigma**2)
            b, a = np.polyfit(lam, ym, 1)

            # Held-out sigma computed against the SAME training fold CDF definition:
            xi = float(x[i])
            less = np.sum(xm < xi)
            equal = np.sum(xm == xi)
            sigma_i = (less + 0.5*equal) / ntr
            sigma_i = np.clip(sigma_i, 0.01, 0.99)
            lam_i = 0.5*np.log(1 - sigma_i**2)
            preds[i] = a + b*lam_i
        else:
            raise ValueError("unknown mode")
    r = np.corrcoef(preds, y)[0,1]
    r2 = 1 - np.sum((y - preds)**2) / np.sum((y - y.mean())**2)
    return r, r2, preds

# Linear baseline
a_lin, b_lin, aic_lin = fit_linear_aic(S, Y)
r_loo_lin, r2_loo_lin, pred_lin = loo_model(S, Y, "linear")

# Lorentz (rank-based sigma)
r_loo_lor, r2_loo_lor, pred_lor = loo_model(S, Y, "lorentz")

# Correlation of Lorentz prediction with Y (for reporting symmetry)
# (This is NOT the same as corr(S, Y); it is corr(pred, obs) under LOO)
print("LORENTZ BRIDGE (corrected probe)")
print(f"AIC linear   = {aic_lin: .2f}")
# For Lorentz AIC, fit on full data using rank sigma
n_full = len(S)
order = np.argsort(S)
ranks = np.empty(n_full, dtype=float)
ranks[order] = np.arange(1, n_full+1, dtype=float)
sigma_full = (ranks - 0.5) / n_full
sigma_full = np.clip(sigma_full, 0.01, 0.99)
lam_full = 0.5*np.log(1 - sigma_full**2)
a_lor, b_lor, aic_lor = fit_linear_aic(lam_full, Y)
print(f"AIC lorentz  = {aic_lor: .2f}  {'<- wins' if aic_lor < aic_lin else ''}")
print(f"LOO r linear  = {r_loo_lin: .4f}   R^2 = {r2_loo_lin: .4f}")
print(f"LOO r lorentz = {r_loo_lor: .4f}   R^2 = {r2_loo_lor: .4f}")


# Primary scatter
fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(S, Y)
m, b = np.polyfit(S, Y, 1)
xx = np.linspace(S.min(), S.max(), 200)
ax.plot(xx, m*xx+b, linestyle="--")
ax.set_title(f"PRIMARY: r={float(r):.3f}, p={float(p):.2e}")
ax.set_xlabel("Sarrus Linkage (Z_H - Z_S)")
ax.set_ylabel("ln(kf)")
ax.grid(True, alpha=0.3)
plt.show()

# LOO prediction plot (linear vs lorentz)
fig, ax = plt.subplots(figsize=(8,5))
ax.scatter(Y, pred_lin, label="LOO linear")
ax.scatter(Y, pred_lor, label="LOO lorentz")
minv, maxv = float(min(Y.min(), pred_lin.min(), pred_lor.min())), float(max(Y.max(), pred_lin.max(), pred_lor.max()))
ax.plot([minv, maxv], [minv, maxv], linestyle="--")
ax.set_xlabel("Observed ln(kf)")
ax.set_ylabel("Predicted ln(kf)")
ax.set_title("LOO predictions")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()


def compute_S_for_dataset(dataset, fetched):
    vals = []
    for pdb, name, expL, ln_kf in dataset:
        pick = choose_sequence(pdb, name, expL, fetched)
        if pick["status"] == "SKIP":
            continue
        s = sarrus_locked(pick["seq"], LOCK["N_SHUFFLES"])["sarrus"]
        if np.isfinite(s):
            vals.append(s)
    return np.array(vals, float)

S_two = compute_S_for_dataset(TWO_STATE, rcsb_seqs)
S_multi = compute_S_for_dataset(MULTI_STATE, rcsb_seqs)
S_idp = []
for nm, seq in IDP_SEQS.items():
    d = sarrus_locked(seq, LOCK["N_SHUFFLES"])
    if np.isfinite(d["sarrus"]):
        S_idp.append(d["sarrus"])
S_idp = np.array(S_idp, float)

print(f"Two-state mean S:   {S_two.mean(): .3f}  (n={len(S_two)})")
print(f"Multi-state mean S: {S_multi.mean(): .3f}  (n={len(S_multi)})")
print(f"IDP mean S:         {S_idp.mean(): .3f}  (n={len(S_idp)})")

fig, ax = plt.subplots(figsize=(9,3))
ax.boxplot([S_two, S_multi, S_idp], labels=["Two-state","Multi-state","IDP"])
ax.set_ylabel("Sarrus Linkage")
ax.set_title("Spectrum (descriptive)")
ax.grid(True, axis="y", alpha=0.3)
plt.show()


from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Literal, Tuple
import struct

E_BOUNDARY = 0.4
PHI_BOUNDARY = 0.8

@dataclass
class ConstraintState:
    sigma: float
    basin: Literal["E","TRANSIENT","PHI"]
    gamma: float
    metric: float

class ConstraintSystem(ABC):
    def __init__(self, capacity: float = 1.0):
        self.capacity = float(capacity)

    @abstractmethod
    def metric_raw(self) -> float:
        ...

    def sigma(self) -> float:
        m = abs(self.metric_raw())
        return float(np.clip(m / self.capacity, 0.0, 1.0))

    def gamma(self) -> float:
        s = min(self.sigma(), 0.9999)
        return float(1.0 / np.sqrt(1.0 - s*s))

    def basin(self) -> str:
        s = self.sigma()
        if s < E_BOUNDARY: return "E"
        if s > PHI_BOUNDARY: return "PHI"
        return "TRANSIENT"

    def state(self) -> ConstraintState:
        return ConstraintState(self.sigma(), self.basin(), self.gamma(), self.metric_raw())

class PhysicsBeta(ConstraintSystem):
    def __init__(self, beta: float):
        super().__init__(capacity=1.0)
        self.beta = float(beta)
    def metric_raw(self) -> float:
        return self.beta

class CryptoOddParity(ConstraintSystem):
    def __init__(self, data: bytes):
        super().__init__(capacity=1.0)
        self.data = data
        self.trace = None
        self.digest = None

    @staticmethod
    def _sha256_T1_trace_oneblock(data: bytes):
        # Minimal SHA-256 single-block implementation for trace (not optimized).
        h0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
              0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
        K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
             0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
             0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
             0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
             0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
             0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
             0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
             0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
        # pad to one block
        bit_len = len(data) * 8
        padded = data + b'\x80'
        while (len(padded) % 64) != 56:
            padded += b'\x00'
        padded += struct.pack(">Q", bit_len)
        padded = padded[:64]  # one block only
        w = [0]*64
        for i in range(16):
            w[i] = struct.unpack(">I", padded[i*4:(i+1)*4])[0]
        for i in range(16,64):
            s0 = ((w[i-15] >> 7) | (w[i-15] << 25)) ^ ((w[i-15] >> 18) | (w[i-15] << 14)) ^ (w[i-15] >> 3)
            s1 = ((w[i-2] >> 17) | (w[i-2] << 15)) ^ ((w[i-2] >> 19) | (w[i-2] << 13)) ^ (w[i-2] >> 10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

        a,b,c,d,e,f,g,h = h0
        trace = []
        for i in range(64):
            S1 = ((e>>6)|(e<<26)) ^ ((e>>11)|(e<<21)) ^ ((e>>25)|(e<<7))
            ch = (e & f) ^ (~e & g)
            t1 = (h + S1 + ch + K[i] + w[i]) & 0xFFFFFFFF
            trace.append(t1)
            S0 = ((a>>2)|(a<<30)) ^ ((a>>13)|(a<<19)) ^ ((a>>22)|(a<<10))
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (S0 + maj) & 0xFFFFFFFF
            h,g,f,e,d,c,b,a = g,f,e,(d+t1)&0xFFFFFFFF,c,b,a,(t1+t2)&0xFFFFFFFF

        final = [(h0[i] + [a,b,c,d,e,f,g,h][i]) & 0xFFFFFFFF for i in range(8)]
        digest = "".join(f"{x:08x}" for x in final)
        return trace, digest

    def metric_raw(self) -> float:
        self.trace, self.digest = self._sha256_T1_trace_oneblock(self.data)
        odd = sum(1 for t in self.trace if (bin(int(t)).count("1") % 2) == 1)
        total = len(self.trace)
        # map to [-1,1]
        return float((2*odd - total)/total)

class BioSarrus(ConstraintSystem):
    def __init__(self, seq: str):
        super().__init__(capacity=4.0)  # empirical
        self.seq = seq
    def metric_raw(self) -> float:
        return float(sarrus_locked(self.seq, LOCK["N_SHUFFLES"])["sarrus"])


# Demo: Physics
print("PHYSICS")
for beta in [0.0, 0.1, 0.5, 0.9, 0.99, 0.999]:
    st = PhysicsBeta(beta).state()
    print(f"beta={beta:>6}  sigma={st.sigma:>6.3f}  gamma={st.gamma:>8.4f}  basin={st.basin}")

print("\nCRYPTO (toy)")
for msg in [b"", b"hello", b"NEXUS", b"The quick brown fox", b"\x00"*16, b"\xff"*16]:
    cs = CryptoOddParity(msg)
    st = cs.state()
    odd = sum(1 for t in cs.trace if (bin(int(t)).count('1') % 2) == 1)
    print(f"{msg[:18]!r:<22} odd={odd:>2}/64  metric={st.metric:>7.4f}  sigma={st.sigma:>6.3f}  gamma={st.gamma:>8.4f} basin={st.basin}  hash[:16]={cs.digest[:16]}")

print("\nBIO (single example: Ubiquitin override if present)")
ubq = "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG"
bs = BioSarrus(ubq).state()
print(f"Sarrus={bs.metric: .4f}  sigma={bs.sigma: .3f} gamma={bs.gamma: .4f} basin={bs.basin}")
