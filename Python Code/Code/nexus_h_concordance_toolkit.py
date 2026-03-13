#!/usr/bin/env python3
"""
Nexus H Concordance Toolkit (stream ↔ frame)

Goal:
  Estimate H from:
    (1) STREAM: time-series alignment score S_stream(H)
    (2) FRAME : geometric/ray-trace focusing score S_frame(H)
  Then test concordance: H_stream ≈ H_frame with bootstrap CIs and null controls.

This is analysis-only code for simulations / toy models. It does NOT provide
instructions for physical experiments.

USAGE EXAMPLES
  # Stream-only (CSV with columns: E_mech,E_em)
  python nexus_h_concordance_toolkit.py --stream_csv stream.csv --mode stream

  # Frame-only (provide an import path and function)
  python nexus_h_concordance_toolkit.py --frame_func "my_sim:run_rays" --mode frame

  # Both + concordance report
  python nexus_h_concordance_toolkit.py --stream_csv stream.csv --frame_func "my_sim:run_rays" --mode both

FRAME FUNCTION CONTRACT
  The function you pass via --frame_func MUST have signature:

    finals = run_rays(n_rays: int, H: float, seed: int) -> array-like shape (n_rays,2)

  It should return ONLY the final positions (float32/float64). Any additional diagnostics
  should be handled inside your sim and written elsewhere.
"""
from __future__ import annotations

import argparse
import importlib
import math
import os
from dataclasses import dataclass
from typing import Callable, Optional, Tuple, List

import numpy as np

# Optional SciPy; fall back gracefully if unavailable
try:
    from scipy.signal import hilbert
except Exception:
    hilbert = None


# ----------------------------
# Utilities
# ----------------------------

def parse_func(spec: str) -> Callable:
    """
    spec format: "module.submodule:function_name"
    """
    if ":" not in spec:
        raise ValueError(f'--frame_func must be "module:function". Got: {spec!r}')
    mod_name, fn_name = spec.split(":", 1)
    mod = importlib.import_module(mod_name)
    fn = getattr(mod, fn_name, None)
    if fn is None or not callable(fn):
        raise ValueError(f"Function {fn_name!r} not found/callable in module {mod_name!r}")
    return fn


def zscore(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    s = x.std(ddof=0)
    if s == 0:
        return np.zeros_like(x)
    return (x - x.mean()) / s


# ----------------------------
# STREAM estimator
# ----------------------------

def compute_cross(E_mech: np.ndarray, E_em: np.ndarray, phi: float) -> np.ndarray:
    """
    Cross-product proxy: E_mech * phase_shift(E_em)
    Uses analytic signal if SciPy is available; otherwise uses a pure rotation-less product.
    """
    E_mech = np.asarray(E_mech, dtype=float)
    E_em = np.asarray(E_em, dtype=float)
    if hilbert is None:
        # Degraded mode; still returns a deterministic score, but less phase-sensitive
        return E_mech * E_em

    analytic = hilbert(E_em)
    shifted = np.real(np.exp(1j * phi) * analytic)
    return E_mech * shifted


def autocorr(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    ac = np.correlate(x, x, mode="full")[len(x)-1:]
    denom = np.max(np.abs(ac)) + 1e-18
    return ac / denom


def stream_score(cross: np.ndarray,
                 sha_lags: np.ndarray,
                 lag_tol: int = 2,
                 peak_height: float = 0.05) -> float:
    """
    Score = (fraction of target lags matched by autocorr peaks) * (mean peak height).
    This is a simple, explainable proxy. Replace with your preferred stream metric.
    """
    ac = autocorr(cross)
    peaks = np.where(ac > peak_height)[0]
    if len(peaks) == 0:
        return 0.0
    matches = 0
    for lag in sha_lags:
        if np.any(np.abs(peaks - lag) <= lag_tol):
            matches += 1
    mean_peak = float(np.mean(ac[peaks]))
    return (matches / max(1, len(sha_lags))) * (mean_peak + 1e-9)


def estimate_H_stream(E_mech: np.ndarray,
                      E_em: np.ndarray,
                      H_grid: np.ndarray,
                      sha_lags: np.ndarray,
                      phase_map: Callable[[float], float]) -> Tuple[float, np.ndarray]:
    scores = np.empty(len(H_grid), dtype=float)
    for i, H in enumerate(H_grid):
        phi = float(phase_map(H))
        cross = compute_cross(E_mech, E_em, phi)
        scores[i] = stream_score(cross, sha_lags)
    best = float(H_grid[int(np.argmax(scores))])
    return best, scores


def bootstrap_H_stream(E_mech: np.ndarray,
                       E_em: np.ndarray,
                       H_grid: np.ndarray,
                       sha_lags: np.ndarray,
                       phase_map: Callable[[float], float],
                       n_boot: int = 200,
                       window_frac: float = 0.25,
                       rng: Optional[np.random.Generator] = None) -> np.ndarray:
    if rng is None:
        rng = np.random.default_rng()
    N = len(E_mech)
    w = max(32, int(N * window_frac))
    if w >= N:
        w = max(32, N // 2)
    Hs = []
    for _ in range(n_boot):
        start = int(rng.integers(0, max(1, N - w)))
        Hb, _ = estimate_H_stream(E_mech[start:start+w], E_em[start:start+w], H_grid, sha_lags, phase_map)
        Hs.append(Hb)
    return np.asarray(Hs, dtype=float)


# ----------------------------
# FRAME estimator
# ----------------------------

def frame_score(finals: np.ndarray, radius: float = 0.02) -> float:
    """
    Focusing score: max fraction inside a small ball of radius r.
    Fast implementation uses brute distance; for n_rays up to ~2e4 it's fine.
    """
    X = np.asarray(finals, dtype=float)
    n = X.shape[0]
    if n == 0:
        return 0.0
    # Choose candidate centers as a subsample to avoid O(n^2) at high n
    rng = np.random.default_rng(0)
    idx = rng.choice(n, size=min(n, 256), replace=False)
    centers = X[idx]
    best = 0
    for c in centers:
        d2 = np.sum((X - c)**2, axis=1)
        cnt = int(np.sum(d2 <= radius*radius))
        if cnt > best:
            best = cnt
    return best / n


def estimate_H_frame(run_rays: Callable[[int, float, int], np.ndarray],
                     H_grid: np.ndarray,
                     n_rays: int,
                     seed: int,
                     radius: float) -> Tuple[float, np.ndarray]:
    scores = np.empty(len(H_grid), dtype=float)
    for i, H in enumerate(H_grid):
        finals = run_rays(n_rays, float(H), int(seed + i))
        scores[i] = frame_score(finals, radius=radius)
    best = float(H_grid[int(np.argmax(scores))])
    return best, scores


def bootstrap_H_frame(run_rays: Callable[[int, float, int], np.ndarray],
                      H_grid: np.ndarray,
                      n_rays: int,
                      radius: float,
                      n_boot: int = 200,
                      seed: int = 123,
                      rng: Optional[np.random.Generator] = None) -> np.ndarray:
    if rng is None:
        rng = np.random.default_rng()
    Hs = []
    for b in range(n_boot):
        # For each bootstrap, re-run the sweep with a different seed and pick best H.
        Hb, _ = estimate_H_frame(run_rays, H_grid, n_rays=n_rays, seed=int(seed + 1000*b), radius=radius)
        Hs.append(Hb)
    return np.asarray(Hs, dtype=float)


# ----------------------------
# Main
# ----------------------------

@dataclass
class CI:
    lo: float
    hi: float

def ci95(samples: np.ndarray) -> CI:
    q = np.quantile(samples, [0.025, 0.975])
    return CI(float(q[0]), float(q[1]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["stream", "frame", "both"], default="both")
    ap.add_argument("--out_csv", default="h_sweep_results.csv")

    # H grid controls
    ap.add_argument("--H0", type=float, default=math.pi/9)
    ap.add_argument("--span_pct", type=float, default=2.0, help="±percent sweep around H0")
    ap.add_argument("--steps", type=int, default=81, help="number of grid points across span")

    # Stream inputs
    ap.add_argument("--stream_csv", type=str, default=None, help="CSV with columns E_mech,E_em")
    ap.add_argument("--sha_lags", type=str, default=None,
                    help="Comma-separated integer lags, e.g. '16,32,48,64'. If omitted, uses 16 multiples up to 256.")
    ap.add_argument("--phi_mode", choices=["pi_over_2", "pi_times_H", "const"], default="pi_over_2",
                    help="How to map H -> phase phi for stream alignment.")
    ap.add_argument("--phi_const", type=float, default=math.pi/2)

    # Frame inputs
    ap.add_argument("--frame_func", type=str, default=None, help='Import spec "module:function"')
    ap.add_argument("--n_rays", type=int, default=2000)
    ap.add_argument("--radius", type=float, default=0.02)
    ap.add_argument("--seed", type=int, default=123)

    # Bootstrap
    ap.add_argument("--n_boot", type=int, default=200)

    args = ap.parse_args()

    H0 = float(args.H0)
    span = float(args.span_pct) / 100.0
    H_grid = np.linspace(H0*(1-span), H0*(1+span), int(args.steps), dtype=float)

    # sha lags
    if args.sha_lags:
        sha_lags = np.asarray([int(x.strip()) for x in args.sha_lags.split(",") if x.strip()], dtype=int)
    else:
        sha_lags = np.asarray([16*k for k in range(1, 17)], dtype=int)

    # phase map
    if args.phi_mode == "pi_over_2":
        phase_map = lambda H: math.pi/2
    elif args.phi_mode == "pi_times_H":
        phase_map = lambda H: math.pi * float(H)
    else:
        phase_map = lambda H: float(args.phi_const)

    # results table
    rows = []

    # STREAM
    if args.mode in ("stream", "both"):
        if not args.stream_csv:
            raise SystemExit("--stream_csv required for mode stream/both")
        import pandas as pd
        df = pd.read_csv(args.stream_csv)
        if "E_mech" not in df.columns or "E_em" not in df.columns:
            raise SystemExit("stream_csv must have columns: E_mech,E_em")
        E_mech = df["E_mech"].to_numpy(dtype=float)
        E_em = df["E_em"].to_numpy(dtype=float)

        H_stream, S_stream = estimate_H_stream(E_mech, E_em, H_grid, sha_lags, phase_map)
        boot_stream = bootstrap_H_stream(E_mech, E_em, H_grid, sha_lags, phase_map, n_boot=int(args.n_boot))
        ci_stream = ci95(boot_stream)

        print(f"[STREAM] H* = {H_stream:.9f}   CI95=[{ci_stream.lo:.9f}, {ci_stream.hi:.9f}]   (n_boot={len(boot_stream)})")

    # FRAME
    if args.mode in ("frame", "both"):
        if not args.frame_func:
            raise SystemExit("--frame_func required for mode frame/both")
        run_rays = parse_func(args.frame_func)

        H_frame, S_frame = estimate_H_frame(run_rays, H_grid, n_rays=int(args.n_rays), seed=int(args.seed), radius=float(args.radius))
        boot_frame = bootstrap_H_frame(run_rays, H_grid, n_rays=int(args.n_rays), radius=float(args.radius), n_boot=int(args.n_boot), seed=int(args.seed))
        ci_frame = ci95(boot_frame)

        print(f"[FRAME ] H* = {H_frame:.9f}   CI95=[{ci_frame.lo:.9f}, {ci_frame.hi:.9f}]   (n_boot={len(boot_frame)})")

    # Concordance
    if args.mode == "both":
        diff = H_stream - H_frame
        overlap = not (ci_stream.hi < ci_frame.lo or ci_frame.hi < ci_stream.lo)
        print(f"[ΔH   ] H_stream - H_frame = {diff:+.9f}   CI overlap: {overlap}")

    # Write CSV of sweeps if available
    # We store whichever sweeps were computed.
    # Note: When both are run, H_grid is shared and both S are available.
    out_cols = {"H": H_grid}
    if args.mode in ("stream", "both"):
        out_cols["S_stream"] = S_stream
    if args.mode in ("frame", "both"):
        out_cols["S_frame"] = S_frame

    try:
        import pandas as pd
        pd.DataFrame(out_cols).to_csv(args.out_csv, index=False)
        print(f"Wrote sweep table: {args.out_csv}")
    except Exception as e:
        print(f"(CSV write skipped) {e}")

if __name__ == "__main__":
    main()
