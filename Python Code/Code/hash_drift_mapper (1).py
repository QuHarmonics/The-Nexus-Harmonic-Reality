"""
Hash Drift Mapper (SHA-256)
Mirror-Input Echo Test Utilities

Usage (demo):
    python hash_drift_mapper.py
"""

import hashlib
import numpy as np

def sha256_bits_utf8(s: str) -> np.ndarray:
    """SHA-256 of UTF-8 string -> 256 bits (0/1)."""
    h = hashlib.sha256(s.encode("utf-8")).digest()
    b = np.frombuffer(h, dtype=np.uint8)
    return np.unpackbits(b).astype(np.int8)

def delta_bits(a_bits: np.ndarray, b_bits: np.ndarray) -> np.ndarray:
    """XOR delta bits."""
    return (a_bits ^ b_bits).astype(np.int8)

def hamming(bits: np.ndarray) -> int:
    return int(bits.sum())

def corr_pm1(a_bits: np.ndarray, b_bits: np.ndarray) -> float:
    """Correlation using +/-1 encoding."""
    ap = (a_bits * 2 - 1).astype(np.int16)
    bp = (b_bits * 2 - 1).astype(np.int16)
    return float(ap.dot(bp) / 256.0)

def delta_spectrum(delta: np.ndarray, eps: float = 1e-12):
    """
    FFT magnitudes of mean-centered delta, plus two summary stats.
    Returns (magnitudes, peakiness, flatness).
    """
    d = (delta.astype(np.float32) - float(delta.mean()))
    fft = np.fft.rfft(d)
    mag = np.abs(fft)
    mag[0] = 0.0

    med = float(np.median(mag[1:]))
    peakiness = float(mag.max() / (med + eps))

    m = mag[1:] + eps
    geom = float(np.exp(np.mean(np.log(m))))
    arith = float(np.mean(m))
    flatness = float(geom / arith)
    return mag, peakiness, flatness

def hash_drift_mapper(s: str):
    """
    Compute SHA-256 forward vs reversed metrics.
    Returns a dict with Hamming, correlation, and spectrum stats.
    """
    a = sha256_bits_utf8(s)
    b = sha256_bits_utf8(s[::-1])
    d = delta_bits(a, b)
    mag, peak, flat = delta_spectrum(d)
    top_idx = mag.argsort()[-5:][::-1]
    top_peaks = [(int(i), float(mag[i])) for i in top_idx]
    return {
        "len": len(s),
        "hamming": hamming(d),
        "corr": corr_pm1(a, b),
        "peakiness": peak,
        "flatness": flat,
        "top_peaks": top_peaks,
    }

if __name__ == "__main__":
    tests = [
        "hello world",
        "0123456789"*8,
        "abc"*60 + "!",
        "DeanKulik_Nexus",
    ]
    for t in tests:
        print(t, "->", hash_drift_mapper(t))
