"""
NEXUS UNIFIED CONSTRAINT SYSTEM — v1.0
=======================================
Architecture: GPT's ConstraintSystem ABC (the shell)
Kernel: Claude's locked Sarrus pipeline (the verb)
Physics: Corrected NexusMatter (no double-normalization)
Crypto: Real SHA-256 T1 trace extraction

Author: Dean Kulik (ORCID 0009-0003-3128-8828)
Compiled: 2026-02-15
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal, Tuple, List, Optional
import numpy as np
import hashlib
import struct

# ==============================================================================
# CONSTANTS
# ==============================================================================
H_ATTRACTOR = np.pi / 9        # ≈ 0.3491 — Universal stability point
E_BOUNDARY = 0.4               # Coherent threshold
PHI_BOUNDARY = 0.8             # Dissipative threshold
ZERO_DAMPING = 0.9999          # Singularity guard

# ==============================================================================
# STATE
# ==============================================================================
@dataclass
class ConstraintState:
    sigma: float
    basin: Literal['E', 'PHI', 'TRANSIENT']
    sarrus: float
    gamma: float  # Lorentz factor = 1/sqrt(1-sigma^2)

# ==============================================================================
# THE ANCESTOR VERB: ALLOCATE
# ==============================================================================
class ConstraintSystem(ABC):
    """
    Any finite system that must split budget between exploration and collapse.
    measure_geometry() returns RAW constraint differential.
    update_state() normalizes by capacity → sigma → gamma.
    """

    def __init__(self, raw_stream, capacity: float = 1.0):
        self.stream = raw_stream
        self.capacity = capacity
        self.sigma = 0.0
        self.basin = 'E'
        self._sarrus = 0.0

    @abstractmethod
    def measure_geometry(self) -> float:
        """Return RAW differential constraint (before normalization)."""
        pass

    def resolve_latency(self) -> float:
        safe = min(abs(self.sigma), ZERO_DAMPING)
        return 1.0 / np.sqrt(1.0 - safe ** 2)

    def update_state(self) -> ConstraintState:
        self._sarrus = self.measure_geometry()
        self.sigma = np.clip(abs(self._sarrus) / self.capacity, 0.0, 1.0)
        if self.sigma < E_BOUNDARY:
            self.basin = 'E'
        elif self.sigma > PHI_BOUNDARY:
            self.basin = 'PHI'
        else:
            self.basin = 'TRANSIENT'
        return ConstraintState(
            sigma=self.sigma, basin=self.basin,
            sarrus=self._sarrus, gamma=self.resolve_latency()
        )


# ==============================================================================
# DOMAIN 1: BIOLOGY — LOCKED SARRUS PIPELINE
# ==============================================================================

# Miyazawa-Jernigan burial energy (the CORRECT scale)
MJ_SCALE = {
    'A': 0.616, 'R':-1.537, 'N':-0.628, 'D':-0.608, 'C': 0.680,
    'Q':-0.468, 'E':-0.587, 'G': 0.501, 'H':-0.340, 'I': 1.385,
    'L': 1.256, 'K':-1.840, 'M': 0.828, 'F': 1.356, 'P':-0.198,
    'S':-0.049, 'T': 0.034, 'W': 0.878, 'Y': 0.534, 'V': 1.111
}
HELIX_LAGS = [3, 4]
SHEET_LAG = 2
N_SHUFFLES = 1000


class NexusBio(ConstraintSystem):
    """
    Protein folding constraint extraction.
    THE LOCKED PIPELINE — not an approximation of it.
    """

    def __init__(self, sequence: str, capacity: float = 4.0):
        super().__init__(sequence, capacity)
        self.sequence = sequence
        self._z_helix = 0.0
        self._z_sheet = 0.0
        self._diagnostics = {}

    def measure_geometry(self) -> float:
        seq = self.sequence
        sig = np.array([MJ_SCALE.get(a, np.nan) for a in seq if a in MJ_SCALE], dtype=float)
        sig = sig[~np.isnan(sig)]
        N = len(sig)
        if N < 10:
            return 0.0

        s = sig - sig.mean()
        denom = np.sum(s ** 2)
        if denom < 1e-12:
            return 0.0

        # ACF at locked lags (total-energy normalization, NOT windowed Pearson)
        def acf(lag):
            return np.sum(s[:-lag] * s[lag:]) / denom

        acf_h = np.mean([acf(l) for l in HELIX_LAGS])
        acf_s = acf(SHEET_LAG)

        # Deterministic seed: MD5 of sequence STRING (not signal bytes)
        seed = int(hashlib.md5(seq.encode()).hexdigest(), 16) % (2 ** 32)
        rng = np.random.default_rng(seed)

        aas = [a for a in seq if a in MJ_SCALE]
        sh_h, sh_s = [], []
        for _ in range(N_SHUFFLES):
            shuf = aas.copy()
            rng.shuffle(shuf)
            ssig = np.array([MJ_SCALE[a] for a in shuf], dtype=float)
            ss = ssig - ssig.mean()
            d = np.sum(ss ** 2)
            if d < 1e-12:
                continue
            sh_h.append(np.mean([np.sum(ss[:-l] * ss[l:]) / d for l in HELIX_LAGS]))
            sh_s.append(np.sum(ss[:-SHEET_LAG] * ss[SHEET_LAG:]) / d)

        sh_h, sh_s = np.array(sh_h), np.array(sh_s)
        if sh_h.size < 20:
            return 0.0
        std_h, std_s = np.std(sh_h), np.std(sh_s)
        if std_h < 1e-12 or std_s < 1e-12:
            return 0.0

        self._z_helix = (acf_h - sh_h.mean()) / std_h
        self._z_sheet = (acf_s - sh_s.mean()) / std_s
        self._diagnostics = {
            'acf_h': acf_h, 'acf_s': acf_s,
            'null_mean_h': sh_h.mean(), 'null_std_h': std_h,
            'null_mean_s': sh_s.mean(), 'null_std_s': std_s,
            'n_valid_shuffles': len(sh_h), 'seq_len': N,
        }

        return self._z_helix - self._z_sheet  # The Sarrus Linkage


# ==============================================================================
# DOMAIN 2: CRYPTOGRAPHY — SHA-256 T1 TRACE
# ==============================================================================

SHA256_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b,
    0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
    0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,
    0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152,
    0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
    0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819,
    0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
    0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
    0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]
SHA256_H0 = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

def _ror32(v, n):
    return ((v >> n) | (v << (32 - n))) & 0xFFFFFFFF

def sha256_trace(data: bytes) -> Tuple[List[int], str]:
    """Full SHA-256 with T1 round trace extraction."""
    bit_len = len(data) * 8
    padded = data + b'\x80'
    while (len(padded) % 64) != 56:
        padded += b'\x00'
    padded += struct.pack('>Q', bit_len)

    w = [0] * 64
    for i in range(16):
        w[i] = struct.unpack('>I', padded[i*4:(i+1)*4])[0]
    for i in range(16, 64):
        s0 = _ror32(w[i-15], 7) ^ _ror32(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = _ror32(w[i-2], 17) ^ _ror32(w[i-2], 19) ^ (w[i-2] >> 10)
        w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

    a, b, c, d, e, f, g, h = list(SHA256_H0)
    T1_trace = []

    for i in range(64):
        S1 = _ror32(e, 6) ^ _ror32(e, 11) ^ _ror32(e, 25)
        ch = (e & f) ^ (~e & g) & 0xFFFFFFFF
        t1 = (h + S1 + ch + SHA256_K[i] + w[i]) & 0xFFFFFFFF
        T1_trace.append(t1)
        S0 = _ror32(a, 2) ^ _ror32(a, 13) ^ _ror32(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        t2 = (S0 + maj) & 0xFFFFFFFF
        h, g, f, e, d, c, b, a = g, f, e, (d+t1)&0xFFFFFFFF, c, b, a, (t1+t2)&0xFFFFFFFF

    final = [(SHA256_H0[i] + [a,b,c,d,e,f,g,h][i]) & 0xFFFFFFFF for i in range(8)]
    return T1_trace, ''.join(f'{x:08x}' for x in final)


class NexusCrypto(ConstraintSystem):
    """SHA-256 constraint geometry via T1 parity differential."""

    def __init__(self, preimage: bytes, capacity: float = 1.0):
        super().__init__(preimage, capacity)
        self.trace = []
        self.digest = None

    def measure_geometry(self) -> float:
        self.trace, self.digest = sha256_trace(self.stream)
        odd = sum(1 for t in self.trace if bin(t).count('1') % 2 == 1)
        return (2 * odd - 64) / 64  # Signed parity differential


# ==============================================================================
# DOMAIN 3: PHYSICS — SPECIAL RELATIVITY
# ==============================================================================

class NexusMatter(ConstraintSystem):
    """Physical constraint: velocity as budget allocation against c."""

    def __init__(self, velocity: float, c: float = 299792458.0):
        super().__init__(velocity, capacity=c)  # capacity = c
        self.v = float(velocity)
        self.c = float(c)

    def measure_geometry(self) -> float:
        return self.v  # RAW velocity; update_state divides by capacity=c → beta


# ==============================================================================
# IVANKOV DATASET — TWO-STATE BENCHMARK
# ==============================================================================

IVANKOV_TWO_STATE = [
    ("2PDD", "PSBD",           41,  9.8, "LKKLTLKNLISKLGLKPAKRKSQG" + "KLPSGIKKLANSL"),
    ("2ABD", "ACBP",           86,  6.6, None),
    ("256B", "Cyt_b562",      106, 12.2, None),
    ("1IMQ", "Im9",            86,  7.3, None),
    ("1LMB", "lambda-Rep",     80,  8.5, None),
    ("1FNF", "FN3-9",          90, -0.9,
     "VSDVPRDLEVVAATPTSLLISWDAPAVTVRYYRITYGETGGNSPVQEFTVPGSKSTATISGLKPGVDYTITVYAVTGRGDSPASSKPISINYRT"),
    ("1WIT", "Twitchin",       93,  0.4,
     "LKPAIVTNVKENVTNFEDVILDWSPPDSPVVFEIVYAPKRDQWKVAVPVGDNGKCAPMQLNKVLSEDANGSLRVTVKAEIQSSGNSPEGFK"),
    ("1TEN", "Tenascin",       90,  1.1,
     "RLDAPSQIEVKDVTDTTALITWFKPLAEIDGIELTYGIKDVPGDRTTIDLTEDENQYSIGNLKPDTEYEVSLISRRGDMSSNPAKETFTT"),
    ("1SHG", "SH3-spectrin",   62,  1.4,
     "DETGKELVLALYDYQEKSPREVTMKKGDILTLLNSTNKDWWKVEVNDRQGFVPAAYVKKLD"),
    ("1SRL", "SH3-src",        64,  4.0,
     "GQVAIYDYQNDPDDELSFKKGDVITTVDRKQWDWWIGERCAGRGIVPSNYVL"),
    ("1PNJ", "SH3-PI3K",       90, -1.1, None),
    ("1SHF", "SH3-fyn",        67,  4.5,
     "VQALYDYVESYEGDNTEFQKGDDIIVLNYKGQDWWYGEIGGSEGLVPAQYLVPQQ"),
    ("1PSF", "PsaE",           69,  3.2, None),
    ("1CSP", "CspB-Bs",        67,  7.0, None),
    ("1C9O", "CspB-Bc",        66,  7.2, None),
    ("1G6P", "CspB-Tm",        66,  6.3, None),
    ("1MJC", "CspA-Ec",        69,  5.3, None),
    ("1LOP", "CypA",          164,  6.6, None),
    ("1C8C", "DNA-bp",         63,  7.0, None),
    ("1HZ6", "Protein_L",      62,  4.1, None),
    ("1PGB", "Protein_G",      57,  6.0, None),
    ("1FKB", "FKBP12",        107,  1.5, None),
    ("2CI2", "CI2",            64,  3.9, None),
    ("1AYE", "ADA2h",          80,  6.8,
     "RQLPALLPEEWFHKAVLDRAQGDGPFQKFGVQIRASDHGTEVALPEGVHLIAECRDEEAGVRELLRRLRAAGVVDKEHD"),
    ("1URN", "U1A",           102,  5.8, None),
    ("1APS", "AcP",            98, -1.5,
     "LVRHMQPEYAVQLLISDGEYSGRWAVEKHGIPLDTVVCALSLSDYGHRPVLLSKEIGAKGKIILLHAGGEKNEEVVRKENADLLEKAGITL"),
    ("1RIS", "S6",            101,  5.9, None),
    ("1POH", "HPr",            85,  2.7, None),
    ("1DIV", "NTL9",           56,  6.1,
     "MKVIFLKDVKGMGKKGEIKNVADGYANNFLFKQGLAIEATPANLKALEAQKQKEQR"),
    ("2VIK", "Villin_14T",    126,  6.8, None),
]

IDP_CONTROLS = [
    ("P37840", "a-Synuclein",  "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEA"),
    ("P10636", "Tau_K18",      "VQIINKKLDLSNVQSKCGSKDNIKHVPGGGSVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL"),
    ("Q15648", "FUS_LCD",      "MASNDYTQQATQSYGAYPTQPGQGYSQQSSQPYGQQSYSGYSQSTDTSGYGQSSYSSYGQSQNTGYGTQSTPQGYGSTGGYGSSQSSQSSYGQQSSYPGYGQQPAPSSTSGSYGSSSQSSSYGQPQSGSYSQQPSYGGQQQSYGQQQSYNPPQGYGQQNQYNS"),
    ("P15532", "NDP_kinase",   "MANLERTFIAIKPDGVQRGLVGEIIKRFEQKGFRLVGLKFMQASEDLLKEHYVDLKDRP"),
]


# ==============================================================================
# EXECUTION
# ==============================================================================

def run_cross_domain_proof():
    """
    The proof: three substrates, one verb, same geometry.
    """
    import urllib.request
    from scipy import stats

    print("=" * 80)
    print("  NEXUS UNIFIED CONSTRAINT SYSTEM — CROSS-DOMAIN PROOF")
    print("  Architecture: ConstraintSystem ABC")
    print("  Kernel: Locked Sarrus pipeline (MJ, lags [3,4]/2, 1000 shuffles, MD5 seed)")
    print("=" * 80)

    # ──────────────────────────────────────────────────────────────
    # DOMAIN 1: PHYSICS (instant — no network, no shuffles)
    # ──────────────────────────────────────────────────────────────
    print("\n┌─ DOMAIN 1: PHYSICS ─────────────────────────────────────────────┐")
    physics_tests = [
        ("Rest",    0.0),
        ("0.1c",    29979245.8),
        ("0.5c",    149896229.0),
        ("0.9c",    269813212.2),
        ("0.99c",   296794173.42),
        ("0.999c",  299492665.542),
    ]
    print(f"  {'NAME':<10} {'β':>6} {'σ':>8} {'γ':>10} {'BASIN':<12}")
    print("  " + "─" * 50)
    for name, v in physics_tests:
        p = NexusMatter(v)
        st = p.update_state()
        print(f"  {name:<10} {v/p.c:>6.3f} {st.sigma:>8.4f} {st.gamma:>10.4f} {st.basin:<12}")
    print("└────────────────────────────────────────────────────────────────┘")

    # ──────────────────────────────────────────────────────────────
    # DOMAIN 2: CRYPTOGRAPHY
    # ──────────────────────────────────────────────────────────────
    print("\n┌─ DOMAIN 2: CRYPTOGRAPHY ────────────────────────────────────────┐")
    crypto_tests = [b"", b"hello", b"NEXUS", b"The quick brown fox",
                    b"\x00" * 64, b"\xff" * 64]
    print(f"  {'INPUT':<22} {'ODD/64':>6} {'σ':>8} {'γ':>8} {'BASIN':<10} {'HASH[:16]'}")
    print("  " + "─" * 75)
    for msg in crypto_tests:
        cr = NexusCrypto(msg)
        st = cr.update_state()
        label = repr(msg)[:20]
        odd = sum(1 for t in cr.trace if bin(t).count('1') % 2 == 1)
        print(f"  {label:<22} {odd:>3}/64 {st.sigma:>8.4f} {st.gamma:>8.4f} "
              f"{st.basin:<10} {cr.digest[:16]}")
    print("└────────────────────────────────────────────────────────────────┘")

    # ──────────────────────────────────────────────────────────────
    # DOMAIN 3: BIOLOGY — FULL IVANKOV BENCHMARK
    # ──────────────────────────────────────────────────────────────
    print("\n┌─ DOMAIN 3: BIOLOGY — IVANKOV TWO-STATE BENCHMARK ───────────────┐")
    print("  Fetching sequences from RCSB...")

    # Fetch all PDB FASTAs
    pdbs = list(set(row[0] for row in IVANKOV_TWO_STATE))
    url = f"https://www.rcsb.org/fasta/entry/{','.join(sorted(pdbs))}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            fasta_text = resp.read().decode()
    except Exception as e:
        print(f"  FETCH FAILED: {e}")
        print(f"  Running with override sequences only...")
        fasta_text = ""

    # Parse FASTA
    fasta_db = {}
    cur, buf = None, []
    for line in fasta_text.splitlines():
        if line.startswith(">"):
            if cur and buf:
                fasta_db.setdefault(cur, []).append("".join(buf))
            cur = line[1:].split("|")[0].split("_")[0].upper()
            buf = []
        else:
            buf.append(line.strip())
    if cur and buf:
        fasta_db.setdefault(cur, []).append("".join(buf))

    # Run locked pipeline
    results = []  # (name, sarrus, ln_kf, seq_len)
    skipped = []

    print(f"\n  {'PDB':<6} {'NAME':<14} {'LEN':>4} {'Z_H':>7} {'Z_S':>7} "
          f"{'SARRUS':>8} {'ln(kf)':>7} {'σ':>6} {'BASIN':<10} {'STATUS'}")
    print("  " + "─" * 95)

    for pdb, name, expL, ln_kf, override in IVANKOV_TWO_STATE:
        # Sequence selection
        if override:
            seq = override
            status = "OVERRIDE"
        else:
            cands = fasta_db.get(pdb, [])
            if not cands:
                skipped.append((pdb, name, "NO_FASTA"))
                continue
            # Pick closest length chain
            seq = min(cands, key=lambda s: abs(len(s) - expL))
            if abs(len(seq) - expL) > expL * 0.10:
                skipped.append((pdb, name, f"LEN_MISMATCH({len(seq)}vs{expL})"))
                continue
            status = "FETCH"

        bio = NexusBio(seq)
        st = bio.update_state()

        if abs(st.sarrus) < 1e-12 and bio._z_helix == 0 and bio._z_sheet == 0:
            skipped.append((pdb, name, "ZERO_VARIANCE"))
            continue

        results.append((name, st.sarrus, ln_kf, len(seq)))
        print(f"  {pdb:<6} {name:<14} {len(seq):>4} {bio._z_helix:>7.3f} "
              f"{bio._z_sheet:>7.3f} {st.sarrus:>8.3f} {ln_kf:>7.1f} "
              f"{st.sigma:>6.3f} {st.basin:<10} {status}")

    # IDP controls
    print(f"\n  {'ID':<6} {'NAME':<14} {'LEN':>4} {'Z_H':>7} {'Z_S':>7} "
          f"{'SARRUS':>8} {'ln(kf)':>7} {'σ':>6} {'BASIN':<10}")
    print("  " + "─" * 80)
    idp_sarrus = []
    for uid, name, seq in IDP_CONTROLS:
        bio = NexusBio(seq)
        st = bio.update_state()
        idp_sarrus.append(st.sarrus)
        print(f"  {uid:<6} {name:<14} {len(seq):>4} {bio._z_helix:>7.3f} "
              f"{bio._z_sheet:>7.3f} {st.sarrus:>8.3f} {'N/A':>7} "
              f"{st.sigma:>6.3f} {st.basin:<10}")

    if len(results) < 10:
        print(f"\n  Only {len(results)} proteins — insufficient for statistics.")
        print("└────────────────────────────────────────────────────────────────┘")
        return

    # ──────────────────────────────────────────────────────────────
    # STATISTICS — THE LOCKED TESTS
    # ──────────────────────────────────────────────────────────────
    names = [r[0] for r in results]
    S = np.array([r[1] for r in results])
    Y = np.array([r[2] for r in results])
    L = np.array([np.log(r[3]) for r in results])
    n = len(S)

    # Pearson
    r_pear, p_pear = stats.pearsonr(S, Y)

    # Permutation test
    n_perm = 10000
    rng_p = np.random.default_rng(42)
    r_obs = abs(r_pear)
    count = 1
    for _ in range(n_perm):
        Y_shuf = rng_p.permutation(Y)
        if abs(np.corrcoef(S, Y_shuf)[0, 1]) >= r_obs:
            count += 1
    p_perm = count / (n_perm + 1)

    # Partial correlation controlling ln(L)
    def residuals(x, c):
        sl, il = np.polyfit(c, x, 1)
        return x - (sl * c + il)
    r_partial, p_partial = stats.pearsonr(residuals(S, L), residuals(Y, L))

    # LOO-CV
    preds = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        sl, il = np.polyfit(S[mask], Y[mask], 1)
        preds[i] = sl * S[i] + il
    r_loo, _ = stats.pearsonr(Y, preds)
    r2_loo = 1 - np.sum((Y - preds) ** 2) / np.sum((Y - Y.mean()) ** 2)

    # ──────────────────────────────────────────────────────────────
    # LORENTZ BRIDGE — CORRECTED
    # ──────────────────────────────────────────────────────────────
    sigma_rank = 1 - stats.rankdata(S) / (n + 1)
    sigma_rank = np.clip(sigma_rank, 0.01, 0.99)
    lor_term = 0.5 * np.log(1 - sigma_rank ** 2)

    r_lor, p_lor = stats.pearsonr(lor_term, Y)

    # LOO for Lorentz
    preds_lor = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        sl, il = np.polyfit(lor_term[mask], Y[mask], 1)
        preds_lor[i] = sl * lor_term[i] + il
    r_loo_lor, _ = stats.pearsonr(Y, preds_lor)
    r2_loo_lor = 1 - np.sum((Y - preds_lor) ** 2) / np.sum((Y - Y.mean()) ** 2)

    # AIC
    rss_lin = np.sum((Y - np.polyval(np.polyfit(S, Y, 1), S)) ** 2)
    rss_lor = np.sum((Y - np.polyval(np.polyfit(lor_term, Y, 1), lor_term)) ** 2)
    aic_lin = n * np.log(rss_lin / n) + 4
    aic_lor = n * np.log(rss_lor / n) + 4

    print(f"""
  ┌─ STATISTICS ──────────────────────────────────────────────────┐
  │  n = {n} two-state folders                                    │
  │                                                                │
  │  PRIMARY (Sarrus → ln_kf):                                    │
  │    Pearson r       = {r_pear:>8.4f}   p = {p_pear:.2e}              │
  │    Permutation p   = {p_perm:.4f}    (10000 perms)                │
  │    Partial r (|L)  = {r_partial:>8.4f}   p = {p_partial:.2e}              │
  │    LOO-CV r        = {r_loo:>8.4f}   R² = {r2_loo:.4f}               │
  │                                                                │
  │  LORENTZ BRIDGE (corrected):                                   │
  │    Lorentz r       = {r_lor:>8.4f}   p = {p_lor:.2e}              │
  │    LOO-CV r        = {r_loo_lor:>8.4f}   R² = {r2_loo_lor:.4f}               │
  │    AIC linear      = {aic_lin:>8.2f}                               │
  │    AIC Lorentz     = {aic_lor:>8.2f}  {'← WINS' if aic_lor < aic_lin else ''}                          │
  │                                                                │
  │  IDP CONTROLS:                                                 │
  │    Folder mean S   = {np.mean(S):>8.3f}                            │
  │    IDP mean S      = {np.mean(idp_sarrus):>8.3f}                            │
  └────────────────────────────────────────────────────────────────┘""")

    if skipped:
        print(f"\n  Skipped ({len(skipped)}):")
        for pdb, name, reason in skipped:
            print(f"    {pdb} {name}: {reason}")

    # ──────────────────────────────────────────────────────────────
    # PLOTS
    # ──────────────────────────────────────────────────────────────
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # 1: Sarrus vs ln(kf)
    ax = axes[0, 0]
    ax.scatter(S, Y, c='steelblue', s=70, alpha=0.8, edgecolors='white', linewidth=0.5, zorder=3)
    sl, il = np.polyfit(S, Y, 1)
    xf = np.linspace(S.min() - 0.3, S.max() + 0.3, 100)
    ax.plot(xf, sl * xf + il, 'k--', alpha=0.5)
    ax.set_xlabel('Sarrus Linkage S')
    ax.set_ylabel('ln(kf)')
    ax.set_title(f'Primary: r={r_pear:.3f}, perm p={p_perm:.4f}')
    ax.grid(True, alpha=0.3)

    # 2: Lorentz bridge
    ax = axes[0, 1]
    ax.scatter(sigma_rank, Y, c='steelblue', s=70, alpha=0.8, edgecolors='white', linewidth=0.5, zorder=3)
    sig_c = np.linspace(0.01, 0.95, 200)
    sl_l, il_l = np.polyfit(lor_term, Y, 1)
    ax.plot(sig_c, sl_l * 0.5 * np.log(1 - sig_c ** 2) + il_l, 'r-', linewidth=2.5, label='Lorentz', alpha=0.8)
    sl_s, il_s = np.polyfit(sigma_rank, Y, 1)
    ax.plot(sig_c, sl_s * sig_c + il_s, 'b--', linewidth=1.5, label='Linear', alpha=0.7)
    ax.set_xlabel('σ (rank-based entropy load)')
    ax.set_ylabel('ln(kf)')
    ax.set_title(f'Lorentz r={r_lor:.3f} vs Linear')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 3: LOO-CV
    ax = axes[1, 0]
    ax.scatter(preds, Y, c='steelblue', s=70, alpha=0.7, label=f'Linear (R²={r2_loo:.3f})', zorder=3)
    ax.scatter(preds_lor, Y, c='red', s=70, alpha=0.7, marker='s', label=f'Lorentz (R²={r2_loo_lor:.3f})', zorder=3)
    mn = min(Y.min(), preds.min(), preds_lor.min()) - 1
    mx = max(Y.max(), preds.max(), preds_lor.max()) + 1
    ax.plot([mn, mx], [mn, mx], 'k--', alpha=0.5)
    ax.set_xlabel('LOO Predicted ln(kf)')
    ax.set_ylabel('Observed ln(kf)')
    ax.set_title('LOO-CV: Linear vs Lorentz')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 4: Cross-domain gamma comparison
    ax = axes[1, 1]
    # Physics curve
    beta_range = np.linspace(0, 0.999, 500)
    gamma_sr = 1 / np.sqrt(1 - beta_range ** 2)
    ax.plot(beta_range, gamma_sr, 'k-', linewidth=3, alpha=0.6, label='γ = 1/√(1−σ²)')

    # Bio data points
    kf = np.exp(Y)
    R0 = np.max(kf) * 1.1
    gamma_bio = R0 / kf
    ax.scatter(sigma_rank, gamma_bio, c='steelblue', s=80, alpha=0.8, zorder=3,
               edgecolors='white', linewidth=0.5, label='Two-state folders')

    ax.set_xlabel('σ (constraint saturation)')
    ax.set_ylabel('γ (time dilation / latency)')
    ax.set_title('Cross-Domain: One Geometry, Three Substrates')
    ax.set_yscale('log')
    ax.set_ylim(0.5, 500)
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.suptitle('NEXUS UNIFIED SYSTEM — CROSS-DOMAIN CONSTRAINT PROOF\n'
                 'Architecture: ConstraintSystem ABC | Kernel: Locked Sarrus Pipeline',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/nexus_unified_proof.png', dpi=150, bbox_inches='tight')
    print("\n  Saved: nexus_unified_proof.png")
    print("└────────────────────────────────────────────────────────────────┘")


if __name__ == "__main__":
    run_cross_domain_proof()
