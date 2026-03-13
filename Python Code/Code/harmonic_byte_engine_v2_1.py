# harmonic_byte_engine_v2_1.py
# Complete, runnable program with correct Ψ, Ω resolution-at-cap, and lawful entropy term.
import math, numpy as np
from dataclasses import dataclass
from typing import List, Tuple

# === Nexus constants ===
H_MARK1     = math.pi / 9
PHI_RESIDUE = (math.sqrt(5) - 1) / 2
EPS         = 1e-12
TAU         = 1e-6      # Ω tolerance for RCQ harmonic mean target

# === Fixed bytes (π decimals, 8×8) ===
B1=[1,4,1,5,9,2,6,5]; B2=[3,5,8,9,7,9,3,2]
B3=[3,8,4,6,2,6,4,3]; B4=[3,8,3,2,7,9,5,0]
B5=[2,8,8,4,1,9,7,1]; B6=[6,9,3,9,9,3,7,5]
B7=[1,0,5,8,2,0,9,7]; B8=[4,5,9,2,3,0,7,8]
ALL=[B1,B2,B3,B4,B5,B6,B7,B8]

# === Waves ===
def psi(n:int, t:np.ndarray)->np.ndarray:
    return np.sin(2*math.pi*n*t) if n>0 else np.zeros_like(t)

def sfg_plus(acc:np.ndarray, nxt:np.ndarray)->np.ndarray:
    prod = acc*nxt
    m = np.max(np.abs(prod))
    return prod/m if m>EPS else acc  # keep acc if degenerate

def byte_emission_sum(byte:List[int], T:int=4096)->Tuple[np.ndarray,np.ndarray]:
    t = np.linspace(0,1,T,endpoint=False)
    w = np.zeros(T)
    for d in byte:
        w += psi(d, t)
    m = np.max(np.abs(w))
    return t, (w/m if m>EPS else w)

def byte_emission_oplus(byte:List[int], T:int=4096)->np.ndarray:
    t = np.linspace(0,1,T,endpoint=False)
    digits = [d for d in byte]
    nonzero = [d for d in digits if d!=0]
    if not nonzero:
        return np.zeros(T)
    acc = psi(nonzero[0], t)
    for d in digits[1:]:
        if d==0:
            continue
        acc = sfg_plus(acc, psi(d,t))
    m = np.max(np.abs(acc))
    return acc/m if m>EPS else acc

def fft_peaks(x:np.ndarray, k:int=8)->List[Tuple[int,float]]:
    spec = np.fft.rfft(x)
    mag  = np.abs(spec)
    if len(mag) > 0:
        mag[0] = 0.0  # de-emphasize DC in peak list
    idx  = np.argsort(mag)[::-1][:k]
    return [(int(i), float(mag[i])) for i in idx]

# === AHRC bins ===
@dataclass
class BinInfo:
    idx:int
    vals:List[float]

def hrc(values:List[float], N:int)->Tuple[List[BinInfo], float, float]:
    vmin, vmax = min(values), max(values)
    gip_range  = max(vmax - vmin, EPS)
    bins = [BinInfo(i, []) for i in range(N)]
    for v in values:
        fa = min(N-1, max(0, int(((v - vmin)/gip_range)*N - EPS)))
        bins[fa].vals.append(v)
    return bins, vmin, gip_range

def rcq(bininfo:BinInfo, w:float)->float:
    if not bininfo.vals:
        return None
    spread = (max(bininfo.vals) - min(bininfo.vals)) if len(bininfo.vals)>1 else 0.0
    return (len(bininfo.vals)) / (1.0 + (spread / max(w, EPS)))

def psi_score(bins:List[BinInfo], w:float)->float:
    rcqs = [rcq(b,w) for b in bins if b.vals]
    if not rcqs:
        return 1.0
    inv = [1.0/max(r,EPS) for r in rcqs]
    hm  = len(inv)/sum(inv)         # harmonic mean of RCQ
    return 1.0 / hm                 # coherence: 1 only when all RCQ==1

def _resolve_stalled_collisions(values:List[float], N:int)->List[float]:
    """Deterministic local curvature reallocation:
       moves colliders to nearest empty FA bins by setting values to bin centers.
       Minimal, local, and order-stable.
    """
    if N <= 1:
        return values[:]
    vmin, vmax = min(values), max(values)
    gip_range  = max(vmax - vmin, EPS)
    def fa(v):
        return min(N-1, max(0, int(((v - vmin)/gip_range)*N - EPS)))
    # occupancy
    occupants = {}
    for idx, v in enumerate(values):
        b = fa(v)
        occupants.setdefault(b, []).append((idx, v))
    counts = {b: len(lst) for b,lst in occupants.items()}
    empty = {b for b in range(N) if counts.get(b, 0)==0}
    # Build new value map (index -> new value)
    new_vals = {i: values[i] for i in range(len(values))}
    # For each colliding bin, keep one at center, relocate the rest to nearest empty bins
    for b, lst in occupants.items():
        if len(lst) <= 1:
            continue
        # First one: set to center of original bin
        center_b = b + 0.5
        keep_idx, _ = lst[0]
        new_vals[keep_idx] = vmin + (center_b / N) * gip_range
        # Others: assign to nearest empty bins
        for (idx, _v) in lst[1:]:
            # find nearest empty
            if not empty:
                # nothing empty: slight phi stride within bin ladder
                stride = (PHI_RESIDUE * 0.5) / N
                new_vals[idx] = vmin + (center_b / N) * gip_range + stride * gip_range
                continue
            # search outward
            best = None
            best_dist = None
            for e in list(empty):
                dist = abs(e - b)
                if best is None or dist < best_dist or (dist == best_dist and e < best):
                    best, best_dist = e, dist
            # assign
            center_e = best + 0.5
            new_vals[idx] = vmin + (center_e / N) * gip_range
            empty.remove(best)
    # Return in original order
    return [new_vals[i] for i in range(len(values))]

def rrt(values:List[float], N0:int=8, Ncap:int=2048)->Tuple[int, List[BinInfo], float]:
    N = N0
    while True:
        bins, vmin, gip_range = hrc(values, N)
        w = gip_range / N
        rcqs = [rcq(b,w) for b in bins if b.vals]
        rmax = max(rcqs) if rcqs else 1.0
        if rmax <= 1.0 + TAU:
            return N, bins, w
        if N >= Ncap:
            # Ω persists at cap → apply deterministic curvature reallocation once
            values = _resolve_stalled_collisions(values, N)
            bins, vmin, gip_range = hrc(values, N)
            w = gip_range / N
            return N, bins, w
        N <<= 1

def run(T:int=4096, N0:int=8, Ncap:int=2048):
    for i,byte in enumerate(ALL, start=1):
        # Emissions
        t, wsum = byte_emission_sum(byte, T=T)
        wop     = byte_emission_oplus(byte, T=T)

        peaks_sum = fft_peaks(wsum, k=8)
        peaks_op  = fft_peaks(wop,  k=8)

        # Lawful GIP carrier: ID ⊕ minimal deterministic entropy (φ-residue)
        gips = [((d * H_MARK1) + (idx * PHI_RESIDUE) * 1e-6) % 1.0 for idx, d in enumerate(byte)]

        N, bins, w = rrt(gips, N0=N0, Ncap=Ncap)
        rcqs = [rcq(b,w) for b in bins if b.vals]
        psi  = psi_score(bins, w)
        omega = sum(1 for r in rcqs if r and r>1.0+TAU)
        rmax  = max(rcqs) if rcqs else 1.0

        print(f"Byte{i}: N={N}, Ψ={psi:.6f}, Ω_bins={omega}, RCQ_max={rmax:.3f}")
        print(f"  Peaks(sum): {peaks_sum}")
        print(f"  Peaks(⊕):   {peaks_op}")

if __name__ == "__main__":
    run()
