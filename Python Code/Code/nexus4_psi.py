# Nexus 4 Companion — Ψ Analyzer (Median-Z, RCQ, Align, D-Lattice)
# Usage (as a module): import nexus4_psi as n4; n4.analyze_hex(hex_digest)
# Or run as script: python nexus4_psi.py "abc" (interpreted as ascii; will hash with SHA-256)

import math, hashlib, statistics
from typing import List, Dict, Tuple

H_MARK1 = math.pi / 9.0  # ~0.34906585

# -----------------------------
# Helpers
# -----------------------------

def sha256_hex_from_ascii(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def hex_to_nibbles(hexstr: str) -> List[int]:
    hexstr = ''.join(ch for ch in hexstr.lower() if ch in "0123456789abcdef")
    nibbles = []
    for ch in hexstr:
        if '0' <= ch <= '9':
            nibbles.append(ord(ch) - ord('0'))
        else:
            nibbles.append(10 + (ord(ch) - ord('a')))
    return nibbles

def nibbles_to_angles(nibbles: List[int]) -> List[float]:
    # map each 0..15 to angle on unit circle
    return [(2.0*math.pi/16.0)*v for v in nibbles]

def circular_mean_magnitude(angles: List[float]) -> float:
    if not angles:
        return 0.0
    C = sum(math.cos(t) for t in angles) / len(angles)
    S = sum(math.sin(t) for t in angles) / len(angles)
    return math.hypot(C, S)  # A in [0,1]

def align_from_H(H_value: float, H_target: float = H_MARK1) -> float:
    if H_value >= 0 and H_value <= 1:
        denom = max(1e-12, 1.0 - H_target)
        return max(0.0, 1.0 - abs(H_value - H_target)/denom)
    return 0.0

def bits_from_hex(hexstr: str) -> List[int]:
    # returns MSB-first bit list from hex string
    b = bytes.fromhex(hexstr)
    out = []
    for byte in b:
        for k in range(7, -1, -1):
            out.append((byte >> k) & 1)
    return out

def run_lengths(bits: List[int]) -> List[int]:
    if not bits:
        return []
    lens = []
    cur = bits[0]
    count = 1
    for bit in bits[1:]:
        if bit == cur:
            count += 1
        else:
            lens.append(count)
            cur = bit
            count = 1
    lens.append(count)
    return lens

def js_divergence(p: Dict[int, float], u: Dict[int, float]) -> float:
    # Jensen-Shannon divergence using natural logs
    keys = set(p.keys()) | set(u.keys())
    def safe(v): return max(v, 1e-18)
    M = {k: 0.5*(p.get(k,0.0) + u.get(k,0.0)) for k in keys}
    js = 0.0
    for k in keys:
        pk, uk, mk = safe(p.get(k,0.0)), safe(u.get(k,0.0)), safe(M[k])
        js += 0.5*pk*math.log(pk/mk) + 0.5*uk*math.log(uk/mk)
    return js

def pmf_from_lengths(lens: List[int]) -> Dict[int, float]:
    if not lens:
        return {}
    total = len(lens)
    pmf = {}
    for L in lens:
        pmf[L] = pmf.get(L, 0) + 1
    for k in list(pmf.keys()):
        pmf[k] /= total
    return pmf

def geometric_reference(lens: List[int]) -> Dict[int, float]:
    # set geometric parameter p so that E[L] = avg_len -> p = 1/avg_len
    if not lens:
        return {}
    avg = statistics.mean(lens)
    p = max(1e-6, min(1.0, 1.0/max(avg, 1e-6)))
    # truncate at max observed L and renormalize
    Lmax = max(lens)
    probs = {}
    Z = 0.0
    for L in range(1, Lmax+1):
        val = (1-p)**(L-1) * p
        probs[L] = val
        Z += val
    for L in probs:
        probs[L] /= Z if Z > 0 else 1.0
    return probs

def rcq_from_bits(bits: List[int]) -> float:
    lens = run_lengths(bits)
    if not lens:
        return 0.0
    p = pmf_from_lengths(lens)
    u = geometric_reference(lens)
    js = js_divergence(p, u)
    # map via 1/(1+js) to [0,1]
    rcq = 1.0/(1.0 + js)
    return max(0.0, min(1.0, rcq))

# -----------------------------
# Digit-Triangle lattice features
# -----------------------------

def classify_triad(a: int, b: int, c: int):
    # assume a >= b >= c >= 0
    if a == 0:
        return ("invalid", 0.0)
    eps = (b + c - a) / a
    if eps > 0:
        return ("constructive", eps)
    elif abs(eps) < 1e-12:
        return ("ray", 0.0)
    else:
        return ("invalid", eps)  # negative

def medians_ray(a: float, b: float, c: float):
    # a=b+c
    mb = 0.5*(b + 2*c)
    mc = 0.5*(2*b + c)
    return mb, mc

def triad_features_from_values(vals):
    if len(vals) < 3:
        return dict(avg_abs_eps=0.0, avg_ZH=0.0, avg_Zsym=0.0, avg_Knorm=0.0, frac_constructive=0.0, frac_ray=0.0)
    import statistics, math
    Eps, ZH, Zsym, Knorm = [], [], [], []
    n_constructive = 0
    n_ray = 0
    n_total = 0

    for i in range(len(vals)-2):
        tri = sorted((vals[i], vals[i+1], vals[i+2]), reverse=True)
        a, b, c = tri[0], tri[1], tri[2]
        typ, eps = classify_triad(a, b, c)
        if a <= 0:
            continue
        n_total += 1
        s = b / a
        ZH.append(min(abs(s - H_MARK1), abs(s - (1.0 - H_MARK1)), abs(s - 0.5)))
        Zsym.append(abs(0.5 - s))

        if typ == "constructive":
            n_constructive += 1
            Eps.append(eps)
            # Heron's area (Kn)
            per = a + b + c
            K = 0.25*math.sqrt(max(0.0, per*( -a + b + c)*( a - b + c)*( a + b - c)))
            Knorm.append((K / (a*a)) if a>0 else 0.0)
        elif typ == "ray":
            n_ray += 1
            Eps.append(0.0)
            mb, mc = medians_ray(a,b,c)
            Knorm.append(0.0)  # area zero
        else:  # invalid
            Eps.append(abs(eps))  # penalize gap
            Knorm.append(0.0)

    if n_total == 0:
        n_total = 1
    out = {
        "avg_abs_eps": float(statistics.mean(abs(x) for x in Eps)) if Eps else 0.0,
        "avg_ZH": float(statistics.mean(ZH)) if ZH else 0.0,
        "avg_Zsym": float(statistics.mean(Zsym)) if Zsym else 0.0,
        "avg_Knorm": float(statistics.mean(Knorm)) if Knorm else 0.0,
        "frac_constructive": n_constructive / n_total,
        "frac_ray": n_ray / n_total,
    }
    return out

# -----------------------------
# Ψ-score
# -----------------------------

def psi_score(features, weights=None) -> float:
    if weights is None:
        weights = [0.30, 0.20, 0.10, 0.20, 0.10, 0.10]
    w1, w2, w3, w4, w5, w6 = weights
    align = features.get("align", 0.0)
    rcq = features.get("rcq", 0.0)
    avg_abs_eps = min(1.0, abs(features.get("avg_abs_eps", 0.0)))
    avg_ZH = min(1.0, abs(features.get("avg_ZH", 0.0)))
    avg_Zsym = min(1.0, abs(features.get("avg_Zsym", 0.0)))
    avg_Knorm = max(0.0, min(1.0, features.get("avg_Knorm", 0.0)))

    Psi = (
        w1*align
        + w2*rcq
        + w3*(1.0 - avg_abs_eps)
        + w4*(1.0 - avg_ZH)
        + w5*(1.0 - avg_Zsym)
        + w6*avg_Knorm
    )
    return max(0.0, min(1.0, Psi))

# -----------------------------
# Top-level
# -----------------------------

def analyze_hex(hex_digest: str, weights=None):
    nibbles = hex_to_nibbles(hex_digest)
    angles = nibbles_to_angles(nibbles)
    H = circular_mean_magnitude(angles)
    align = align_from_H(H)

    bits = bits_from_hex(hex_digest)
    rcq = rcq_from_bits(bits)

    tri = triad_features_from_values(nibbles)

    feats = {
        "H": H,
        "align": align,
        "rcq": rcq,
        **tri
    }
    feats["Psi"] = psi_score(feats, weights=weights)
    return feats

def analyze_ascii(s: str, weights=None):
    hex_digest = sha256_hex_from_ascii(s)
    out = analyze_hex(hex_digest, weights=weights)
    out["hex"] = hex_digest
    return out

if __name__ == "__main__":
    import sys, json
    if len(sys.argv) >= 2:
        text = sys.argv[1]
        res = analyze_ascii(text)
        print(json.dumps(res, indent=2))
    else:
        print("Usage: python nexus4_psi.py \"your text\"")
