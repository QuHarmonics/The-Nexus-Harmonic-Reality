---
title: "The Nexus 4 Framework - Allcharts-9-7"
source_pdf: "The Nexus 4 Framework - Allcharts-9-7.pdf"
created_utc: "2025-11-27T11:09:06.0292663Z"
page_count: 142
---

# The Nexus 4 Framework - Allcharts-9-7

## Extracted Text

```text
----------- Page1 ------------
Conversation URL:
https://chatgpt.com/c/688b4a40-3698-832f-9b8c-baffe8c3a567
Title:
Prompt:
import matplotlib.pyplot as plt
import numpy as np
import math
# --- Plot 1: Residue triangle ---
# Define triangle components
pi_value = math.pi
approx_pi = 3.14159
residual = math.sqrt(pi_value**2 - approx_pi**2)
# Triangle coordinates
x_triangle = [0, approx_pi, approx_pi]
y_triangle = [0, 0, residual]
# --- Plot 2: Harmonic scalar cascade ---
harmonics = [3.5, 0.35, 0.035, 0.0035]
powers = [10**i for i in range(len(harmonics))]
# --- Plot 3: Damping projection over iterations ---
iterations = np.linspace(0, 20, 100)
H = 0.35
damping_curve = np.exp(-H * iterations) * pi_value----------- Page2 ------------
# Create subplots
fig, ax = plt.subplots(1, 3, figsize=(18, 5))
# Plot 1: Residue triangle
ax[0].plot(x_triangle + [0], y_triangle + [0], 'k--', label='Triangle Edges')
ax[0].scatter([0, approx_pi, approx_pi], [0, 0, residual], color='red')
ax[0].text(approx_pi/2, -0.05, f"{approx_pi:.5f}", ha='center')
ax[0].text(approx_pi + 0.1, residual/2, f"{residual:.6f}", va='center')
ax[0].text(approx_pi/2, residual/2 + 0.05, f"{pi_value:.5f}", ha='center')
ax[0].set_title("Residual Triangle from π")
ax[0].set_aspect('equal')
ax[0].axis('off')
# Plot 2: Harmonic scalar cascade (log scale)
ax[1].plot(harmonics, 'o-', color='blue')
for i, val in enumerate(harmonics):
ax[1].text(i, val, f"{val}", ha='center', va='bottom')
ax[1].set_yscale('log')
ax[1].set_xticks(range(len(harmonics)))
ax[1].set_xticklabels(['10⁰', '10∈¹', '10∈²', '10∈³'])
ax[1].set_ylabel("Scalar Value (log scale)")
ax[1].set_title("Harmonic Scalar Cascade")
# Plot 3: Damping projection
ax[2].plot(iterations, damping_curve, label='Resonant Decay', color='purple')
ax[2].axhline(y=pi_value * 0.35, color='gray', linestyle='--', label='H×π')
ax[2].text(0, pi_value * 0.35 + 0.05, f"H×π ≈ {pi_value * 0.35:.3f}", color='gray')
ax[2].set_xlabel("Iteration")
ax[2].set_ylabel("Amplitude")
ax[2].set_title("Damping via H = 0.35")
ax[2].legend()
plt.tight_layout()
plt.show()----------- Page3 ------------
Conversation URL:
https://chatgpt.com/c/6897a098-7a80-8320-8360-458bf57364b3
Title:
H_t over sliding subwindows (π window)
Prompt:
# Prototype: SHA→π imaging pathfinder with Mark1 alignment diagnostics
# - Computes SHA-256 of an input seed
# - Maps to an index in π's decimal expansion
# - Extracts a window of digits and evaluates harmonic alignment metrics around H≈0.35
#
# Notes:
# - π computed via Gauss–Legendre with Decimal arithmetic
# - One matplotlib chart is produced (H_t over sliding windows), without styling or colors
# - A summary table is displayed interactively
import hashlib
from decimal import Decimal, getcontext----------- Page4 ------------
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# --- Parameters (can be adjusted) ---
SEED_TEXT = "Hello, Mark1!" # demo input; can be replaced by user
NUM_PI_DIGITS = 4000 # number of digits of π after the decimal to compute
WINDOW_LEN = 256 # length of the extracted π window for analysis
SLIDE_SUBWINDOW = 16 # subwindow size for H_t computation
SLIDE_STRIDE = 1 # sliding stride for H_t series
TARGET_H = 0.35 # Mark1 harmonic target
# --- Utilities ---
def sha256_hex(s: str) -> str:
return hashlib.sha256(s.encode("utf-8")).hexdigest()
def pi_gauss_legendre(n_digits: int) -> str:
"""
Return a string of π with n_digits after the decimal point using Gauss–Legendre.
The total precision is set to n_digits + 50 for safety.
"""
prec = n_digits + 60
getcontext().prec = prec
one = Decimal(1)
two = Decimal(2)
four = Decimal(4)
a = one
b = (one / two).sqrt() # 1/sqrt(2)
t = Decimal(1) / Decimal(4)
p = one
# Iterations: ~log2(n_digits)
iters = max(3, int(math.ceil(math.log(max(2, n_digits), 2))) + 2)
for _ in range(iters):
an = (a + b) / two----------- Page5 ------------
b = (a * b).sqrt()
t = t - p * (a - an) * (a - an)
a = an
p = p * two
pi_val = (a + b) * (a + b) / (four * t)
# Convert to string with sufficient digits
s = format(pi_val, f'.{n_digits}f')
return s # e.g., "3.14159..."
def digits_of_pi_after_decimal(pi_str: str) -> np.ndarray:
"""
Extract digits after the decimal point as an integer numpy array.
"""
# pi_str like "3.1415..."
assert '.' in pi_str
decimals = pi_str.split('.')[1]
return np.array([int(ch) for ch in decimals], dtype=int)
def calibrate_sigma_for_target(target=0.35):
"""
Calibrate σ for P(x)=exp(-(x-0.35)^2/(2σ^2)) so that E[P(X)]=target
when X is discrete-uniform over {0,1,...,9}/9.
Use a simple grid search over σ in [0.01, 0.8].
"""
xs = np.arange(10) / 9.0
def expected_for_sigma(sig):
return float(np.mean(np.exp(-((xs - 0.35)**2) / (2.0 * sig * sig))))
sig_grid = np.linspace(0.01, 0.8, 400)
vals = np.array([expected_for_sigma(s) for s in sig_grid])
idx = int(np.argmin(np.abs(vals - target)))
return float(sig_grid[idx]), float(vals[idx])
def sliding_series(values: np.ndarray, w: int, stride: int) -> np.ndarray:
"""
Compute sliding-window means over 'values' with window size w and stride.
"""----------- Page6 ------------
out = []
for start in range(0, len(values) - w + 1, stride):
out.append(float(np.mean(values[start:start+w])))
return np.array(out)
def second_difference(x: np.ndarray) -> np.ndarray:
return x[2:] - 2*x[1:-1] + x[:-2]
def lag1_autocorr(x: np.ndarray) -> float:
if len(x) < 2:
return float('nan')
x0 = x[:-1] - np.mean(x[:-1])
x1 = x[1:] - np.mean(x[1:])
denom = np.linalg.norm(x0) * np.linalg.norm(x1)
if denom == 0:
return 0.0
return float(np.dot(x0, x1) / denom)
# --- Pipeline ---
# 1) SHA-256 of seed
hash_hex = sha256_hex(SEED_TEXT)
hash_int = int(hash_hex, 16)
# 2) π digits
pi_s = pi_gauss_legendre(NUM_PI_DIGITS)
pi_digits = digits_of_pi_after_decimal(pi_s)
# 3) Map hash to index and extract window
max_start = len(pi_digits) - WINDOW_LEN
start_index = hash_int % max_start
window = pi_digits[start_index:start_index + WINDOW_LEN]
# 4) Normalize digits and define P(x) around 0.35 with calibrated σ
x_vals = window / 9.0
sigma, calib_expectation = calibrate_sigma_for_target(TARGET_H)----------- Page7 ------------
P_vals = np.exp(-((x_vals - TARGET_H)**2) / (2.0 * sigma * sigma))
A_vals = np.ones_like(P_vals) # alignment mass
H_global = float(P_vals.mean())
H_error = abs(H_global - TARGET_H)
# 5) H_t over sliding subwindows, curvature and echo
H_series = sliding_series(P_vals, SLIDE_SUBWINDOW, SLIDE_STRIDE)
curvature = second_difference(H_series) if len(H_series) >= 3 else np.array([])
curv_mean_abs = float(np.mean(np.abs(curvature))) if curvature.size else float('nan')
echo_corr = lag1_autocorr(H_series)
# 6) Plot H_t series
plt.figure()
plt.plot(H_series)
plt.title("H_t over sliding subwindows (π window)")
plt.xlabel("t (window position)")
plt.ylabel("H_t")
plt.show()
# 7) Summary table
from caas_jupyter_tools import display_dataframe_to_user
summary = pd.DataFrame([{
"seed_text": SEED_TEXT,
"sha256_hex": hash_hex,
"pi_digits_computed": NUM_PI_DIGITS,
"window_start_index": int(start_index),
"window_length": WINDOW_LEN,
"sigma_calibrated": sigma,
"E_P_under_uniform": calib_expectation, # E[P(X)] for discrete-uniform digits
"H_global": H_global,
"H_error": H_error,
"H_curvature_mean_abs": curv_mean_abs,
"H_echo_lag1_corr": echo_corr
}])----------- Page8 ------------
display_dataframe_to_user("Mark1 SHA→π Pathfinder Summary", summary)----------- Page9 ------------
Conversation URL:
https://chatgpt.com/c/6897a098-7a80-8320-8360-458bf57364b3
Title:
H_t series — RH zeros
Prompt:
# Re-run with fewer zeros to avoid timeout
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
mp.mp.dps = 50
def riemann_zeros_imag(n):
return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n+1)], dtype=float)
def unfolded_spacings(t):----------- Page10 ------------
t = np.asarray(t, dtype=float)
s = np.diff(t)
rho = (1.0/(2.0*pi)) * np.log(t[:-1]/(2.0*pi))
mean_spacing = 1.0 / rho
return s / mean_spacing
def calibrate_sigma_for_exp_target(target=0.35, mc=20000, seed=123):
rng = np.random.default_rng(seed)
X = rng.exponential(1.0, size=mc)
grid = np.linspace(0.01, 2.0, 300)
means = np.array([np.mean(np.exp(-((X - target)**2) / (2.0 * sig * sig))) for sig in grid])
idx = int(np.argmin(np.abs(means - target)))
return float(grid[idx]), float(means[idx])
def sliding_mean(arr, w):
arr = np.asarray(arr, dtype=float)
if len(arr) < w:
return np.array([])
c = np.cumsum(np.insert(arr, 0, 0.0))
return (c[w:] - c[:-w]) / w
def second_diff(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return np.array([])
return x[2:] - 2*x[1:-1] + x[:-2]
def lag1_autocorr(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return float("nan")
x0 = x[:-1] - x[:-1].mean()
x1 = x[1:] - x[1:].mean()
denom = np.linalg.norm(x0) * np.linalg.norm(x1)
return 0.0 if denom == 0 else float(np.dot(x0, x1) / denom)----------- Page11 ------------
def wigner_gue_spacings(size, rng=None):
rng = np.random.default_rng() if rng is None else rng
out = []
c = 32.0 / (pi**2)
def p(s): return c * s*s * np.exp(-4.0 * s*s / pi)
grid = np.linspace(0.0, 6.0, 1200)[1:]
M = float(np.max(p(grid) / (np.exp(-grid))))
while len(out) < size:
y = rng.exponential(1.0)
u = rng.uniform(0.0, 1.0)
if u < p(y) / (M * np.exp(-y)):
out.append(y)
return np.array(out, dtype=float)
# Parameters
N_ZEROS = 120
SLIDE_W = 16
TARGET_H = 0.35
MC_SAMPLES = 15000
# Data
t = riemann_zeros_imag(N_ZEROS)
u_real = unfolded_spacings(t)
rng = np.random.default_rng(42)
u_poisson = rng.exponential(1.0, size=len(u_real))
u_gue = wigner_gue_spacings(len(u_real), rng=rng)
# Calibration
sigma, achieved = calibrate_sigma_for_exp_target(TARGET_H, mc=MC_SAMPLES, seed=2025)
def mark1_scores(u, sigma, target=TARGET_H):
x = np.asarray(u, dtype=float)
return np.exp(-((x - target)**2) / (2.0 * sigma * sigma))
P_real = mark1_scores(u_real, sigma)
P_pois = mark1_scores(u_poisson, sigma)----------- Page12 ------------
P_gue = mark1_scores(u_gue, sigma)
# H_t
H_real = sliding_mean(P_real, SLIDE_W)
H_pois = sliding_mean(P_pois, SLIDE_W)
H_gue = sliding_mean(P_gue, SLIDE_W)
def diagnostics(H):
curv = second_diff(H)
return {
"H_mean": float(np.mean(H)) if len(H) else float("nan"),
"H_std": float(np.std(H)) if len(H) else float("nan"),
"curvature_mean_abs": float(np.mean(np.abs(curv))) if len(curv) else float("nan"),
"lag1_autocorr": lag1_autocorr(H),
"occupancy_at_or_above_target_%": 100.0 * float(np.mean(H >= TARGET_H)) if len(H) else float("nan"),
"length": int(len(H))
}
diag_real = diagnostics(H_real)
diag_pois = diagnostics(H_pois)
diag_gue = diagnostics(H_gue)
summary = pd.DataFrame([
{"dataset": "RH zeros", **diag_real},
{"dataset": "Poisson null", **diag_pois},
{"dataset": "GUE surrogate", **diag_gue},
])
# Plots
plt.figure()
plt.plot(H_real)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — RH zeros")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()----------- Page13 ------------
plt.figure()
plt.plot(H_pois)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — Poisson null")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.plot(H_gue)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — GUE surrogate")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.hist(u_real, bins=30, density=True, alpha=0.7, label="RH")
plt.hist(u_poisson, bins=30, density=True, alpha=0.5, label="Poisson")
plt.hist(u_gue, bins=30, density=True, alpha=0.5, label="GUE")
plt.title("Unfolded spacings distributions")
plt.xlabel("u")
plt.ylabel("density")
plt.legend()
plt.show()
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("ZPHC/Mark1 summary — RH vs nulls", summary)
print(f"Calibrated sigma on Exp(1): sigma ≈ {sigma:.4f}; achieved E[P] ≈ {achieved:.4f}")
print("Summary diagnostics:\n", summary.to_string(index=False))----------- Page14 ------------
Conversation URL:
https://chatgpt.com/c/6897a098-7a80-8320-8360-458bf57364b3
Title:
H_t series — RH zeros
Prompt:
# Re-run with fewer zeros to avoid timeout
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
mp.mp.dps = 50
def riemann_zeros_imag(n):
return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n+1)], dtype=float)
def unfolded_spacings(t):----------- Page15 ------------
t = np.asarray(t, dtype=float)
s = np.diff(t)
rho = (1.0/(2.0*pi)) * np.log(t[:-1]/(2.0*pi))
mean_spacing = 1.0 / rho
return s / mean_spacing
def calibrate_sigma_for_exp_target(target=0.35, mc=20000, seed=123):
rng = np.random.default_rng(seed)
X = rng.exponential(1.0, size=mc)
grid = np.linspace(0.01, 2.0, 300)
means = np.array([np.mean(np.exp(-((X - target)**2) / (2.0 * sig * sig))) for sig in grid])
idx = int(np.argmin(np.abs(means - target)))
return float(grid[idx]), float(means[idx])
def sliding_mean(arr, w):
arr = np.asarray(arr, dtype=float)
if len(arr) < w:
return np.array([])
c = np.cumsum(np.insert(arr, 0, 0.0))
return (c[w:] - c[:-w]) / w
def second_diff(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return np.array([])
return x[2:] - 2*x[1:-1] + x[:-2]
def lag1_autocorr(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return float("nan")
x0 = x[:-1] - x[:-1].mean()
x1 = x[1:] - x[1:].mean()
denom = np.linalg.norm(x0) * np.linalg.norm(x1)
return 0.0 if denom == 0 else float(np.dot(x0, x1) / denom)----------- Page16 ------------
def wigner_gue_spacings(size, rng=None):
rng = np.random.default_rng() if rng is None else rng
out = []
c = 32.0 / (pi**2)
def p(s): return c * s*s * np.exp(-4.0 * s*s / pi)
grid = np.linspace(0.0, 6.0, 1200)[1:]
M = float(np.max(p(grid) / (np.exp(-grid))))
while len(out) < size:
y = rng.exponential(1.0)
u = rng.uniform(0.0, 1.0)
if u < p(y) / (M * np.exp(-y)):
out.append(y)
return np.array(out, dtype=float)
# Parameters
N_ZEROS = 120
SLIDE_W = 16
TARGET_H = 0.35
MC_SAMPLES = 15000
# Data
t = riemann_zeros_imag(N_ZEROS)
u_real = unfolded_spacings(t)
rng = np.random.default_rng(42)
u_poisson = rng.exponential(1.0, size=len(u_real))
u_gue = wigner_gue_spacings(len(u_real), rng=rng)
# Calibration
sigma, achieved = calibrate_sigma_for_exp_target(TARGET_H, mc=MC_SAMPLES, seed=2025)
def mark1_scores(u, sigma, target=TARGET_H):
x = np.asarray(u, dtype=float)
return np.exp(-((x - target)**2) / (2.0 * sigma * sigma))
P_real = mark1_scores(u_real, sigma)
P_pois = mark1_scores(u_poisson, sigma)----------- Page17 ------------
P_gue = mark1_scores(u_gue, sigma)
# H_t
H_real = sliding_mean(P_real, SLIDE_W)
H_pois = sliding_mean(P_pois, SLIDE_W)
H_gue = sliding_mean(P_gue, SLIDE_W)
def diagnostics(H):
curv = second_diff(H)
return {
"H_mean": float(np.mean(H)) if len(H) else float("nan"),
"H_std": float(np.std(H)) if len(H) else float("nan"),
"curvature_mean_abs": float(np.mean(np.abs(curv))) if len(curv) else float("nan"),
"lag1_autocorr": lag1_autocorr(H),
"occupancy_at_or_above_target_%": 100.0 * float(np.mean(H >= TARGET_H)) if len(H) else float("nan"),
"length": int(len(H))
}
diag_real = diagnostics(H_real)
diag_pois = diagnostics(H_pois)
diag_gue = diagnostics(H_gue)
summary = pd.DataFrame([
{"dataset": "RH zeros", **diag_real},
{"dataset": "Poisson null", **diag_pois},
{"dataset": "GUE surrogate", **diag_gue},
])
# Plots
plt.figure()
plt.plot(H_real)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — RH zeros")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()----------- Page18 ------------
plt.figure()
plt.plot(H_pois)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — Poisson null")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.plot(H_gue)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — GUE surrogate")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.hist(u_real, bins=30, density=True, alpha=0.7, label="RH")
plt.hist(u_poisson, bins=30, density=True, alpha=0.5, label="Poisson")
plt.hist(u_gue, bins=30, density=True, alpha=0.5, label="GUE")
plt.title("Unfolded spacings distributions")
plt.xlabel("u")
plt.ylabel("density")
plt.legend()
plt.show()
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("ZPHC/Mark1 summary — RH vs nulls", summary)
print(f"Calibrated sigma on Exp(1): sigma ≈ {sigma:.4f}; achieved E[P] ≈ {achieved:.4f}")
print("Summary diagnostics:\n", summary.to_string(index=False))----------- Page19 ------------
Conversation URL:
https://chatgpt.com/c/6897a098-7a80-8320-8360-458bf57364b3
Title:
H_t series — RH zeros
Prompt:
# Re-run with fewer zeros to avoid timeout
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
mp.mp.dps = 50
def riemann_zeros_imag(n):
return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n+1)], dtype=float)
def unfolded_spacings(t):----------- Page20 ------------
t = np.asarray(t, dtype=float)
s = np.diff(t)
rho = (1.0/(2.0*pi)) * np.log(t[:-1]/(2.0*pi))
mean_spacing = 1.0 / rho
return s / mean_spacing
def calibrate_sigma_for_exp_target(target=0.35, mc=20000, seed=123):
rng = np.random.default_rng(seed)
X = rng.exponential(1.0, size=mc)
grid = np.linspace(0.01, 2.0, 300)
means = np.array([np.mean(np.exp(-((X - target)**2) / (2.0 * sig * sig))) for sig in grid])
idx = int(np.argmin(np.abs(means - target)))
return float(grid[idx]), float(means[idx])
def sliding_mean(arr, w):
arr = np.asarray(arr, dtype=float)
if len(arr) < w:
return np.array([])
c = np.cumsum(np.insert(arr, 0, 0.0))
return (c[w:] - c[:-w]) / w
def second_diff(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return np.array([])
return x[2:] - 2*x[1:-1] + x[:-2]
def lag1_autocorr(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return float("nan")
x0 = x[:-1] - x[:-1].mean()
x1 = x[1:] - x[1:].mean()
denom = np.linalg.norm(x0) * np.linalg.norm(x1)
return 0.0 if denom == 0 else float(np.dot(x0, x1) / denom)----------- Page21 ------------
def wigner_gue_spacings(size, rng=None):
rng = np.random.default_rng() if rng is None else rng
out = []
c = 32.0 / (pi**2)
def p(s): return c * s*s * np.exp(-4.0 * s*s / pi)
grid = np.linspace(0.0, 6.0, 1200)[1:]
M = float(np.max(p(grid) / (np.exp(-grid))))
while len(out) < size:
y = rng.exponential(1.0)
u = rng.uniform(0.0, 1.0)
if u < p(y) / (M * np.exp(-y)):
out.append(y)
return np.array(out, dtype=float)
# Parameters
N_ZEROS = 120
SLIDE_W = 16
TARGET_H = 0.35
MC_SAMPLES = 15000
# Data
t = riemann_zeros_imag(N_ZEROS)
u_real = unfolded_spacings(t)
rng = np.random.default_rng(42)
u_poisson = rng.exponential(1.0, size=len(u_real))
u_gue = wigner_gue_spacings(len(u_real), rng=rng)
# Calibration
sigma, achieved = calibrate_sigma_for_exp_target(TARGET_H, mc=MC_SAMPLES, seed=2025)
def mark1_scores(u, sigma, target=TARGET_H):
x = np.asarray(u, dtype=float)
return np.exp(-((x - target)**2) / (2.0 * sigma * sigma))
P_real = mark1_scores(u_real, sigma)
P_pois = mark1_scores(u_poisson, sigma)----------- Page22 ------------
P_gue = mark1_scores(u_gue, sigma)
# H_t
H_real = sliding_mean(P_real, SLIDE_W)
H_pois = sliding_mean(P_pois, SLIDE_W)
H_gue = sliding_mean(P_gue, SLIDE_W)
def diagnostics(H):
curv = second_diff(H)
return {
"H_mean": float(np.mean(H)) if len(H) else float("nan"),
"H_std": float(np.std(H)) if len(H) else float("nan"),
"curvature_mean_abs": float(np.mean(np.abs(curv))) if len(curv) else float("nan"),
"lag1_autocorr": lag1_autocorr(H),
"occupancy_at_or_above_target_%": 100.0 * float(np.mean(H >= TARGET_H)) if len(H) else float("nan"),
"length": int(len(H))
}
diag_real = diagnostics(H_real)
diag_pois = diagnostics(H_pois)
diag_gue = diagnostics(H_gue)
summary = pd.DataFrame([
{"dataset": "RH zeros", **diag_real},
{"dataset": "Poisson null", **diag_pois},
{"dataset": "GUE surrogate", **diag_gue},
])
# Plots
plt.figure()
plt.plot(H_real)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — RH zeros")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()----------- Page23 ------------
plt.figure()
plt.plot(H_pois)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — Poisson null")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.plot(H_gue)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — GUE surrogate")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.hist(u_real, bins=30, density=True, alpha=0.7, label="RH")
plt.hist(u_poisson, bins=30, density=True, alpha=0.5, label="Poisson")
plt.hist(u_gue, bins=30, density=True, alpha=0.5, label="GUE")
plt.title("Unfolded spacings distributions")
plt.xlabel("u")
plt.ylabel("density")
plt.legend()
plt.show()
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("ZPHC/Mark1 summary — RH vs nulls", summary)
print(f"Calibrated sigma on Exp(1): sigma ≈ {sigma:.4f}; achieved E[P] ≈ {achieved:.4f}")
print("Summary diagnostics:\n", summary.to_string(index=False))----------- Page24 ------------
Conversation URL:
https://chatgpt.com/c/6897a098-7a80-8320-8360-458bf57364b3
Title:
H_t series — RH zeros
Prompt:
# Re-run with fewer zeros to avoid timeout
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
mp.mp.dps = 50
def riemann_zeros_imag(n):
return np.array([float(mp.im(mp.zetazero(k))) for k in range(1, n+1)], dtype=float)
def unfolded_spacings(t):----------- Page25 ------------
t = np.asarray(t, dtype=float)
s = np.diff(t)
rho = (1.0/(2.0*pi)) * np.log(t[:-1]/(2.0*pi))
mean_spacing = 1.0 / rho
return s / mean_spacing
def calibrate_sigma_for_exp_target(target=0.35, mc=20000, seed=123):
rng = np.random.default_rng(seed)
X = rng.exponential(1.0, size=mc)
grid = np.linspace(0.01, 2.0, 300)
means = np.array([np.mean(np.exp(-((X - target)**2) / (2.0 * sig * sig))) for sig in grid])
idx = int(np.argmin(np.abs(means - target)))
return float(grid[idx]), float(means[idx])
def sliding_mean(arr, w):
arr = np.asarray(arr, dtype=float)
if len(arr) < w:
return np.array([])
c = np.cumsum(np.insert(arr, 0, 0.0))
return (c[w:] - c[:-w]) / w
def second_diff(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return np.array([])
return x[2:] - 2*x[1:-1] + x[:-2]
def lag1_autocorr(x):
x = np.asarray(x, dtype=float)
if len(x) < 3:
return float("nan")
x0 = x[:-1] - x[:-1].mean()
x1 = x[1:] - x[1:].mean()
denom = np.linalg.norm(x0) * np.linalg.norm(x1)
return 0.0 if denom == 0 else float(np.dot(x0, x1) / denom)----------- Page26 ------------
def wigner_gue_spacings(size, rng=None):
rng = np.random.default_rng() if rng is None else rng
out = []
c = 32.0 / (pi**2)
def p(s): return c * s*s * np.exp(-4.0 * s*s / pi)
grid = np.linspace(0.0, 6.0, 1200)[1:]
M = float(np.max(p(grid) / (np.exp(-grid))))
while len(out) < size:
y = rng.exponential(1.0)
u = rng.uniform(0.0, 1.0)
if u < p(y) / (M * np.exp(-y)):
out.append(y)
return np.array(out, dtype=float)
# Parameters
N_ZEROS = 120
SLIDE_W = 16
TARGET_H = 0.35
MC_SAMPLES = 15000
# Data
t = riemann_zeros_imag(N_ZEROS)
u_real = unfolded_spacings(t)
rng = np.random.default_rng(42)
u_poisson = rng.exponential(1.0, size=len(u_real))
u_gue = wigner_gue_spacings(len(u_real), rng=rng)
# Calibration
sigma, achieved = calibrate_sigma_for_exp_target(TARGET_H, mc=MC_SAMPLES, seed=2025)
def mark1_scores(u, sigma, target=TARGET_H):
x = np.asarray(u, dtype=float)
return np.exp(-((x - target)**2) / (2.0 * sigma * sigma))
P_real = mark1_scores(u_real, sigma)
P_pois = mark1_scores(u_poisson, sigma)----------- Page27 ------------
P_gue = mark1_scores(u_gue, sigma)
# H_t
H_real = sliding_mean(P_real, SLIDE_W)
H_pois = sliding_mean(P_pois, SLIDE_W)
H_gue = sliding_mean(P_gue, SLIDE_W)
def diagnostics(H):
curv = second_diff(H)
return {
"H_mean": float(np.mean(H)) if len(H) else float("nan"),
"H_std": float(np.std(H)) if len(H) else float("nan"),
"curvature_mean_abs": float(np.mean(np.abs(curv))) if len(curv) else float("nan"),
"lag1_autocorr": lag1_autocorr(H),
"occupancy_at_or_above_target_%": 100.0 * float(np.mean(H >= TARGET_H)) if len(H) else float("nan"),
"length": int(len(H))
}
diag_real = diagnostics(H_real)
diag_pois = diagnostics(H_pois)
diag_gue = diagnostics(H_gue)
summary = pd.DataFrame([
{"dataset": "RH zeros", **diag_real},
{"dataset": "Poisson null", **diag_pois},
{"dataset": "GUE surrogate", **diag_gue},
])
# Plots
plt.figure()
plt.plot(H_real)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — RH zeros")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()----------- Page28 ------------
plt.figure()
plt.plot(H_pois)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — Poisson null")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.plot(H_gue)
plt.axhline(TARGET_H, linestyle="--")
plt.title("H_t series — GUE surrogate")
plt.xlabel("Window index")
plt.ylabel("H_t")
plt.show()
plt.figure()
plt.hist(u_real, bins=30, density=True, alpha=0.7, label="RH")
plt.hist(u_poisson, bins=30, density=True, alpha=0.5, label="Poisson")
plt.hist(u_gue, bins=30, density=True, alpha=0.5, label="GUE")
plt.title("Unfolded spacings distributions")
plt.xlabel("u")
plt.ylabel("density")
plt.legend()
plt.show()
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("ZPHC/Mark1 summary — RH vs nulls", summary)
print(f"Calibrated sigma on Exp(1): sigma ≈ {sigma:.4f}; achieved E[P] ≈ {achieved:.4f}")
print("Summary diagnostics:\n", summary.to_string(index=False))----------- Page29 ------------
Conversation URL:
https://chatgpt.com/c/68a1f65b-a860-832c-97df-313d1c34aff9
Title:
Prompt:
# Byte∈Driven Harmonic π∈Torus (Jupyter∈ready, no HTML)
#
# What this notebook cell does:
# 1) Pulls the first N π digits (after the decimal) deterministically.
# 2) Builds an 8×8 sheet (64 nodes) and stacks 8 layers (total 512 nodes) on a torus.
# - φ (major-circle angle) indexes the 64 face nodes.
# - θ (tube angle) is modulated by the π digit at that node.
# 3) Injects two 8∈value “bytes” (Byte1, Byte2). For each node: fold = Byte1[i%8] XOR roll(Byte2, layer)[i%8].
# - “tension” = popcount(fold) over 8 bits.
# 4) Computes global trust Q(H) = 1 − |mean(bit_density) − 0.35|, where bit_density = tension/8.
# 5) Plots the 3D torus with node sizes ∈ tension (no special colors, per instruction).----------- Page30 ------------
# 6) Exports a CSV of all node metrics for deeper analysis.
#
# HOW TO USE:
# - Edit Byte1, Byte2 below (length 8 each, 0–255 allowed) and re∈run the cell.
# - Change NUM_LAYERS or NODES_PER_FACE if you want a different lattice size.
# - Trust and basic stats print below the plot.
#
# NOTE: The visualization uses matplotlib (not seaborn/plotly), per the environment rules.
import numpy as np
import math
import mpmath as mp
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # noqa: F401; needed for 3D projection
from math import pi
# ------------------- Config -------------------
NUM_LAYERS = 8 # “stack height” (your round stack)
NODES_PER_FACE = 64 # 8×8 grid per π-sheet face
MAJOR_R = 10.0 # torus major radius
MINOR_r = 3.0 # torus minor radius
RANDOMIZE_SEED = False # set True to scramble layer offsets reproducibly
SEED = 1337
# Your 8∈value “bytes” (you can change freely; 0–255 each is OK).
# Defaults follow your earlier example using π’s first 8 digits and your reply set.
Byte1 = np.array([1, 4, 1, 5, 9, 2, 6, 5], dtype=np.uint8)
Byte2 = np.array([3, 5, 8, 9, 7, 9, 3, 2], dtype=np.uint8)
# ------------------- Helpers -------------------
def pi_digits(n: int) -> np.ndarray:
"""Return first n digits of π after the decimal as integers [0..9]."""
mp.mp.dps = n + 5 # a bit extra for safety
s = str(mp.mp.pi)
# s like '3.14159...'; take substring after '.'----------- Page31 ------------
dec = s.split('.')[1][:n]
return np.array([int(ch) for ch in dec], dtype=np.int16)
def popcount_u8(x: int) -> int:
"""8-bit population count."""
return int(bin(x & 0xFF).count("1"))
# ------------------- Build lattice -------------------
TOTAL_NODES = NUM_LAYERS * NODES_PER_FACE
# Get at least TOTAL_NODES π digits for per-node θ modulation
digits = pi_digits(TOTAL_NODES)
# Optionally randomize per-layer Byte2 rotation (keeps determinism for a given SEED)
rng = np.random.default_rng(SEED) if RANDOMIZE_SEED else None
# Arrays to fill
xs, ys, zs = [], [], []
layers, faces, dig, thetas, phis, a_vals, b_vals, xors, tensions, bit_dens = [], [], [], [], [], [], [], [], [], []
for L in range(NUM_LAYERS):
# Optionally scramble the rotation pattern per layer (still deterministic if RANDOMIZE_SEED=True)
roll_by = int(rng.integers(0, 8)) if RANDOMIZE_SEED else L # simple: roll Byte2 by layer index
B2L = np.roll(Byte2, roll_by)
for i in range(NODES_PER_FACE):
idx = L * NODES_PER_FACE + i
d = int(digits[idx]) # π digit at this node ∈ {0..9}
# Angles:
phi_angle = 2 * pi * (i / NODES_PER_FACE) # major circle: enumerates the 64 face nodes
theta_angle = 2 * pi * (d / 10.0) # tube angle: driven by π digit (0..9 → 0..2π)
# Torus parametric embedding
# T(θ, φ) = ((R + r cos θ) cos φ, (R + r cos θ) sin φ, r sin θ)
X = (MAJOR_R + MINOR_r * math.cos(theta_angle)) * math.cos(phi_angle)
Y = (MAJOR_R + MINOR_r * math.cos(theta_angle)) * math.sin(phi_angle)----------- Page32 ------------
Z = MINOR_r * math.sin(theta_angle)
# Byte fold
a = int(Byte1[i % 8])
b = int(B2L[i % 8])
xval = a ^ b # XOR fold key
t = popcount_u8(xval) # “tension”: # of 1-bits
bd = t / 8.0 # bit density in [0,1]
# Save
xs.append(X); ys.append(Y); zs.append(Z)
layers.append(L); faces.append(i); dig.append(d); thetas.append(theta_angle); phis.append(phi_angle)
a_vals.append(a); b_vals.append(b); xors.append(xval); tensions.append(t); bit_dens.append(bd)
# To numpy
xs = np.array(xs); ys = np.array(ys); zs = np.array(zs)
layers = np.array(layers); faces = np.array(faces); dig = np.array(dig)
thetas = np.array(thetas); phis = np.array(phis)
a_vals = np.array(a_vals); b_vals = np.array(b_vals)
xors = np.array(xors); tensions = np.array(tensions); bit_dens = np.array(bit_dens)
# Global trust score Q(H)
QH = 1.0 - abs(bit_dens.mean() - 0.35)
# ------------------- Plot -------------------
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
# Marker size scales with tension; keep sizes reasonable
sizes = 10 + 12 * tensions # base size 10; each extra bit adds size
ax.scatter(xs, ys, zs, s=sizes, depthshade=True) # no explicit color mapping
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')----------- Page33 ------------
ax.set_title(f'Byte∈Driven Harmonic π∈Torus\nLayers={NUM_LAYERS}, Face Nodes={NODES_PER_FACE}, Q(H)={QH:.3f}')
# Equal-ish aspect for better geometry perception
max_range = np.array([xs.max()-xs.min(), ys.max()-ys.min(), zs.max()-zs.min()]).max()
Xb = 0.5 * max_range
ax.set_xlim(xs.mean() - Xb, xs.mean() + Xb)
ax.set_ylim(ys.mean() - Xb, ys.mean() + Xb)
ax.set_zlim(zs.mean() - Xb, zs.mean() + Xb)
plt.show()
# ------------------- Export metrics -------------------
df = pd.DataFrame({
'layer': layers,
'face_idx': faces,
'pi_digit': dig,
'theta': thetas,
'phi': phis,
'X': xs, 'Y': ys, 'Z': zs,
'byte1': a_vals, 'byte2_rolled': b_vals,
'xor': xors,
'tension_popcount': tensions,
'bit_density': bit_dens
})
csv_path = '/mnt/data/byte_pi_torus_nodes.csv'
df.to_csv(csv_path, index=False)
# Show a quick statistical summary in text
summary = {
'TOTAL_NODES': int(TOTAL_NODES),
'mean_tension_bits': float(tensions.mean()),
'std_tension_bits': float(tensions.std(ddof=1)),
'mean_bit_density': float(bit_dens.mean()),
'std_bit_density': float(bit_dens.std(ddof=1)),
'Q(H)': float(QH)----------- Page34 ------------
}
print("=== Byte∈Driven Harmonic π∈Torus: Summary ===")
for k, v in summary.items():
print(f"{k}: {v}")
print(f"\nNode metrics CSV saved to: {csv_path}")----------- Page35 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
H9 Phase Distance Distribution for SHA-256 K Constants
Prompt:
# Let's compute SHA-256 constants from first 64 primes and initial hash values from first 8 primes.
# We'll measure their "H9 phase alignment": distance to the nearest multiple of 1/18 on the unit circle.
# Then we will display a few concise tables and simple plots.
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from caas_jupyter_tools import display_dataframe_to_user
# Helper to generate first n primes
def primes(n):----------- Page36 ------------
ps = []
num = 2
while len(ps) < n:
isprime = True
for p in ps:
if p*p > num:
break
if num % p == 0:
isprime = False
break
if isprime:
ps.append(num)
num += 1
return ps
# Constants
N_K = 64
N_H = 8
two32 = 2**32
spoke = 1/18.0 # normalized fraction corresponding to pi/9 on [0,1)
# Generate primes
P64 = primes(N_K)
P8 = primes(N_H)
# SHA-256 K constants: floor(2^32 * frac(cuberoot(p)))
K_records = []
for i,p in enumerate(P64, start=1):
c = p ** (1/3)
frac = c - math.floor(c)
K = math.floor(frac * two32)
# phase distance to nearest spoke multiple
# consider multiples k*spoke for k in 0..17; compute minimal circular distance
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
# also index of nearest spoke----------- Page37 ------------
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
K_records.append((i, p, frac, K, d, k_near))
dfK = pd.DataFrame(K_records, columns=["idx","prime","frac_cuberoot","K_int","H9_phase_dist","nearest_spoke_idx"])
dfK_sorted = dfK.sort_values("H9_phase_dist").reset_index(drop=True)
# SHA-256 initial hash values ("H"): floor(2^32 * frac(sqrt(p)))
H_records = []
for i,p in enumerate(P8, start=1):
s = math.sqrt(p)
frac = s - math.floor(s)
H = math.floor(frac * two32)
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
H_records.append((i, p, frac, H, d, k_near))
dfH = pd.DataFrame(H_records, columns=["idx","prime","frac_sqrt","H_init_int","H9_phase_dist","nearest_spoke_idx"])
dfH_sorted = dfH.sort_values("H9_phase_dist").reset_index(drop=True)
# Display concise tables
display_dataframe_to_user("SHA-256 K constants with H9-phase proximity", dfK_sorted.head(15))
display_dataframe_to_user("SHA-256 initial H constants with H9-phase proximity", dfH_sorted)
# Plot distributions of H9 distances for K and H
plt.figure()
plt.hist(dfK["H9_phase_dist"], bins=18)
plt.title("H9 Phase Distance Distribution for SHA-256 K Constants")
plt.xlabel("Distance to nearest 1/18 spoke")
plt.ylabel("Count")
plt.show()
plt.figure()
plt.stem(range(len(dfK_sorted)), dfK_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("Sorted H9 Phase Distances (K constants)")
plt.xlabel("Constant rank (closest to H9 on left)")----------- Page38 ------------
plt.ylabel("Distance")
plt.show()
plt.figure()
plt.stem(range(len(dfH_sorted)), dfH_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("H9 Phase Distances (Initial H constants)")
plt.xlabel("Seed (sqrt primes 2..19)")
plt.ylabel("Distance")
plt.show()
# Which spoke indices do constants prefer?
counts_spokes = dfK["nearest_spoke_idx"].value_counts().sort_index()
plt.figure()
plt.bar(counts_spokes.index, counts_spokes.values)
plt.title("Nearest H9 Spoke Index Counts (K constants)")
plt.xlabel("Spoke index (0..17)")
plt.ylabel("Count")
plt.show()
# Save top-10 closest constants with actual primes and ints for reference
top10 = dfK_sorted.head(10)
top10_path = "/mnt/data/sha256_K_top10_H9.csv"
top10.to_csv(top10_path, index=False)
top10_path----------- Page39 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
H9 Phase Distance Distribution for SHA-256 K Constants
Prompt:
# Let's compute SHA-256 constants from first 64 primes and initial hash values from first 8 primes.
# We'll measure their "H9 phase alignment": distance to the nearest multiple of 1/18 on the unit circle.
# Then we will display a few concise tables and simple plots.
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from caas_jupyter_tools import display_dataframe_to_user
# Helper to generate first n primes
def primes(n):----------- Page40 ------------
ps = []
num = 2
while len(ps) < n:
isprime = True
for p in ps:
if p*p > num:
break
if num % p == 0:
isprime = False
break
if isprime:
ps.append(num)
num += 1
return ps
# Constants
N_K = 64
N_H = 8
two32 = 2**32
spoke = 1/18.0 # normalized fraction corresponding to pi/9 on [0,1)
# Generate primes
P64 = primes(N_K)
P8 = primes(N_H)
# SHA-256 K constants: floor(2^32 * frac(cuberoot(p)))
K_records = []
for i,p in enumerate(P64, start=1):
c = p ** (1/3)
frac = c - math.floor(c)
K = math.floor(frac * two32)
# phase distance to nearest spoke multiple
# consider multiples k*spoke for k in 0..17; compute minimal circular distance
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
# also index of nearest spoke----------- Page41 ------------
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
K_records.append((i, p, frac, K, d, k_near))
dfK = pd.DataFrame(K_records, columns=["idx","prime","frac_cuberoot","K_int","H9_phase_dist","nearest_spoke_idx"])
dfK_sorted = dfK.sort_values("H9_phase_dist").reset_index(drop=True)
# SHA-256 initial hash values ("H"): floor(2^32 * frac(sqrt(p)))
H_records = []
for i,p in enumerate(P8, start=1):
s = math.sqrt(p)
frac = s - math.floor(s)
H = math.floor(frac * two32)
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
H_records.append((i, p, frac, H, d, k_near))
dfH = pd.DataFrame(H_records, columns=["idx","prime","frac_sqrt","H_init_int","H9_phase_dist","nearest_spoke_idx"])
dfH_sorted = dfH.sort_values("H9_phase_dist").reset_index(drop=True)
# Display concise tables
display_dataframe_to_user("SHA-256 K constants with H9-phase proximity", dfK_sorted.head(15))
display_dataframe_to_user("SHA-256 initial H constants with H9-phase proximity", dfH_sorted)
# Plot distributions of H9 distances for K and H
plt.figure()
plt.hist(dfK["H9_phase_dist"], bins=18)
plt.title("H9 Phase Distance Distribution for SHA-256 K Constants")
plt.xlabel("Distance to nearest 1/18 spoke")
plt.ylabel("Count")
plt.show()
plt.figure()
plt.stem(range(len(dfK_sorted)), dfK_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("Sorted H9 Phase Distances (K constants)")
plt.xlabel("Constant rank (closest to H9 on left)")----------- Page42 ------------
plt.ylabel("Distance")
plt.show()
plt.figure()
plt.stem(range(len(dfH_sorted)), dfH_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("H9 Phase Distances (Initial H constants)")
plt.xlabel("Seed (sqrt primes 2..19)")
plt.ylabel("Distance")
plt.show()
# Which spoke indices do constants prefer?
counts_spokes = dfK["nearest_spoke_idx"].value_counts().sort_index()
plt.figure()
plt.bar(counts_spokes.index, counts_spokes.values)
plt.title("Nearest H9 Spoke Index Counts (K constants)")
plt.xlabel("Spoke index (0..17)")
plt.ylabel("Count")
plt.show()
# Save top-10 closest constants with actual primes and ints for reference
top10 = dfK_sorted.head(10)
top10_path = "/mnt/data/sha256_K_top10_H9.csv"
top10.to_csv(top10_path, index=False)
top10_path----------- Page43 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
H9 Phase Distance Distribution for SHA-256 K Constants
Prompt:
# Let's compute SHA-256 constants from first 64 primes and initial hash values from first 8 primes.
# We'll measure their "H9 phase alignment": distance to the nearest multiple of 1/18 on the unit circle.
# Then we will display a few concise tables and simple plots.
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from caas_jupyter_tools import display_dataframe_to_user
# Helper to generate first n primes
def primes(n):
ps = []----------- Page44 ------------
num = 2
while len(ps) < n:
isprime = True
for p in ps:
if p*p > num:
break
if num % p == 0:
isprime = False
break
if isprime:
ps.append(num)
num += 1
return ps
# Constants
N_K = 64
N_H = 8
two32 = 2**32
spoke = 1/18.0 # normalized fraction corresponding to pi/9 on [0,1)
# Generate primes
P64 = primes(N_K)
P8 = primes(N_H)
# SHA-256 K constants: floor(2^32 * frac(cuberoot(p)))
K_records = []
for i,p in enumerate(P64, start=1):
c = p ** (1/3)
frac = c - math.floor(c)
K = math.floor(frac * two32)
# phase distance to nearest spoke multiple
# consider multiples k*spoke for k in 0..17; compute minimal circular distance
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
# also index of nearest spoke
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))----------- Page45 ------------
K_records.append((i, p, frac, K, d, k_near))
dfK = pd.DataFrame(K_records, columns=["idx","prime","frac_cuberoot","K_int","H9_phase_dist","nearest_spoke_idx"])
dfK_sorted = dfK.sort_values("H9_phase_dist").reset_index(drop=True)
# SHA-256 initial hash values ("H"): floor(2^32 * frac(sqrt(p)))
H_records = []
for i,p in enumerate(P8, start=1):
s = math.sqrt(p)
frac = s - math.floor(s)
H = math.floor(frac * two32)
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
H_records.append((i, p, frac, H, d, k_near))
dfH = pd.DataFrame(H_records, columns=["idx","prime","frac_sqrt","H_init_int","H9_phase_dist","nearest_spoke_idx"])
dfH_sorted = dfH.sort_values("H9_phase_dist").reset_index(drop=True)
# Display concise tables
display_dataframe_to_user("SHA-256 K constants with H9-phase proximity", dfK_sorted.head(15))
display_dataframe_to_user("SHA-256 initial H constants with H9-phase proximity", dfH_sorted)
# Plot distributions of H9 distances for K and H
plt.figure()
plt.hist(dfK["H9_phase_dist"], bins=18)
plt.title("H9 Phase Distance Distribution for SHA-256 K Constants")
plt.xlabel("Distance to nearest 1/18 spoke")
plt.ylabel("Count")
plt.show()
plt.figure()
plt.stem(range(len(dfK_sorted)), dfK_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("Sorted H9 Phase Distances (K constants)")
plt.xlabel("Constant rank (closest to H9 on left)")
plt.ylabel("Distance")----------- Page46 ------------
plt.show()
plt.figure()
plt.stem(range(len(dfH_sorted)), dfH_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("H9 Phase Distances (Initial H constants)")
plt.xlabel("Seed (sqrt primes 2..19)")
plt.ylabel("Distance")
plt.show()
# Which spoke indices do constants prefer?
counts_spokes = dfK["nearest_spoke_idx"].value_counts().sort_index()
plt.figure()
plt.bar(counts_spokes.index, counts_spokes.values)
plt.title("Nearest H9 Spoke Index Counts (K constants)")
plt.xlabel("Spoke index (0..17)")
plt.ylabel("Count")
plt.show()
# Save top-10 closest constants with actual primes and ints for reference
top10 = dfK_sorted.head(10)
top10_path = "/mnt/data/sha256_K_top10_H9.csv"
top10.to_csv(top10_path, index=False)
top10_path----------- Page47 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
H9 Phase Distance Distribution for SHA-256 K Constants
Prompt:
# Let's compute SHA-256 constants from first 64 primes and initial hash values from first 8 primes.
# We'll measure their "H9 phase alignment": distance to the nearest multiple of 1/18 on the unit circle.
# Then we will display a few concise tables and simple plots.
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from caas_jupyter_tools import display_dataframe_to_user
# Helper to generate first n primes
def primes(n):
ps = []----------- Page48 ------------
num = 2
while len(ps) < n:
isprime = True
for p in ps:
if p*p > num:
break
if num % p == 0:
isprime = False
break
if isprime:
ps.append(num)
num += 1
return ps
# Constants
N_K = 64
N_H = 8
two32 = 2**32
spoke = 1/18.0 # normalized fraction corresponding to pi/9 on [0,1)
# Generate primes
P64 = primes(N_K)
P8 = primes(N_H)
# SHA-256 K constants: floor(2^32 * frac(cuberoot(p)))
K_records = []
for i,p in enumerate(P64, start=1):
c = p ** (1/3)
frac = c - math.floor(c)
K = math.floor(frac * two32)
# phase distance to nearest spoke multiple
# consider multiples k*spoke for k in 0..17; compute minimal circular distance
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
# also index of nearest spoke
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))----------- Page49 ------------
K_records.append((i, p, frac, K, d, k_near))
dfK = pd.DataFrame(K_records, columns=["idx","prime","frac_cuberoot","K_int","H9_phase_dist","nearest_spoke_idx"])
dfK_sorted = dfK.sort_values("H9_phase_dist").reset_index(drop=True)
# SHA-256 initial hash values ("H"): floor(2^32 * frac(sqrt(p)))
H_records = []
for i,p in enumerate(P8, start=1):
s = math.sqrt(p)
frac = s - math.floor(s)
H = math.floor(frac * two32)
distances = [min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0) for k in range(18)]
d = min(distances)
k_near = min(range(18), key=lambda k: min((frac - k*spoke) % 1.0, (k*spoke - frac) % 1.0))
H_records.append((i, p, frac, H, d, k_near))
dfH = pd.DataFrame(H_records, columns=["idx","prime","frac_sqrt","H_init_int","H9_phase_dist","nearest_spoke_idx"])
dfH_sorted = dfH.sort_values("H9_phase_dist").reset_index(drop=True)
# Display concise tables
display_dataframe_to_user("SHA-256 K constants with H9-phase proximity", dfK_sorted.head(15))
display_dataframe_to_user("SHA-256 initial H constants with H9-phase proximity", dfH_sorted)
# Plot distributions of H9 distances for K and H
plt.figure()
plt.hist(dfK["H9_phase_dist"], bins=18)
plt.title("H9 Phase Distance Distribution for SHA-256 K Constants")
plt.xlabel("Distance to nearest 1/18 spoke")
plt.ylabel("Count")
plt.show()
plt.figure()
plt.stem(range(len(dfK_sorted)), dfK_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("Sorted H9 Phase Distances (K constants)")
plt.xlabel("Constant rank (closest to H9 on left)")
plt.ylabel("Distance")----------- Page50 ------------
plt.show()
plt.figure()
plt.stem(range(len(dfH_sorted)), dfH_sorted["H9_phase_dist"], use_line_collection=True)
plt.title("H9 Phase Distances (Initial H constants)")
plt.xlabel("Seed (sqrt primes 2..19)")
plt.ylabel("Distance")
plt.show()
# Which spoke indices do constants prefer?
counts_spokes = dfK["nearest_spoke_idx"].value_counts().sort_index()
plt.figure()
plt.bar(counts_spokes.index, counts_spokes.values)
plt.title("Nearest H9 Spoke Index Counts (K constants)")
plt.xlabel("Spoke index (0..17)")
plt.ylabel("Count")
plt.show()
# Save top-10 closest constants with actual primes and ints for reference
top10 = dfK_sorted.head(10)
top10_path = "/mnt/data/sha256_K_top10_H9.csv"
top10.to_csv(top10_path, index=False)
top10_path----------- Page51 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
K Constants: distance-to-spoke distribution
Prompt:
# Make a simple polar scatter of K constant angles with 9 spoke lines.
import matplotlib.pyplot as plt
import numpy as np
import math
angles = np.deg2rad(K_df['angle_deg'].values)
r = np.ones_like(angles)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='polar')
ax.scatter(angles, r, s=10) # default color----------- Page52 ------------
# draw 9 spokes
for k in range(9):
ax.plot([2*math.pi*k/9, 2*math.pi*k/9], [0, 1.1])
ax.set_title('SHA-256 K Constants on 9-Spoke (π/9) Wheel')
plt.tight_layout()
plt.savefig('/mnt/data/pi9_polar_K.png')
plt.show()
# Histogram of angular distances to nearest spoke
fig2 = plt.figure(figsize=(6,4))
plt.hist(K_df['dist_to_spoke_deg'], bins=24)
plt.xlabel('Distance to nearest π/9 spoke (deg)')
plt.ylabel('Count')
plt.title('K Constants: distance-to-spoke distribution')
plt.tight_layout()
plt.savefig('/mnt/data/pi9_hist_K.png')
plt.show()
'/mnt/data/pi9_polar_K.png', '/mnt/data/pi9_hist_K.png'----------- Page53 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
K Constants: distance-to-spoke distribution
Prompt:
# Make a simple polar scatter of K constant angles with 9 spoke lines.
import matplotlib.pyplot as plt
import numpy as np
import math
angles = np.deg2rad(K_df['angle_deg'].values)
r = np.ones_like(angles)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='polar')
ax.scatter(angles, r, s=10) # default color
# draw 9 spokes----------- Page54 ------------
for k in range(9):
ax.plot([2*math.pi*k/9, 2*math.pi*k/9], [0, 1.1])
ax.set_title('SHA-256 K Constants on 9-Spoke (π/9) Wheel')
plt.tight_layout()
plt.savefig('/mnt/data/pi9_polar_K.png')
plt.show()
# Histogram of angular distances to nearest spoke
fig2 = plt.figure(figsize=(6,4))
plt.hist(K_df['dist_to_spoke_deg'], bins=24)
plt.xlabel('Distance to nearest π/9 spoke (deg)')
plt.ylabel('Count')
plt.title('K Constants: distance-to-spoke distribution')
plt.tight_layout()
plt.savefig('/mnt/data/pi9_hist_K.png')
plt.show()
'/mnt/data/pi9_polar_K.png', '/mnt/data/pi9_hist_K.png'----------- Page55 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
Prompt:
# Phase-biased nonce hillclimber demo
# - Derives π/9 spoke schedule from SHA-256 K constants (per spec)
# - Builds a harmonic "phase score" on the double-SHA256 digest
# - Hill-climbs nonces to maximize spoke alignment
#
# Outputs:
# - Printed schedule and best candidates
# - CSV with top nonces + scores
# - Plot of score vs iteration
#
import hashlib, math, random, struct, os, csv, statistics
from math import pi
from dataclasses import dataclass, field
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
# 1) SHA-256 K constants per FIPS 180-4 (as 32-bit ints)
K = [
0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,----------- Page56 ------------
0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2]
# 2) Map constants to fractional angles (normalize by 2^32), then to nearest π/9 spoke
two32 = 2**32
angles = [(k/two32)*2*pi for k in K]
def nearest_spoke(angle, spokes=9):
# distance to each multiple of 2π/spokes
s = 2*pi/spokes
j = round(angle/s) % spokes
target = j*s
# minimal absolute angular distance modulo 2π
dist = abs((angle - target + pi) % (2*pi) - pi)
return j, dist
spoke_hits = []
for idx,a in enumerate(angles, start=1):
j, d = nearest_spoke(a, 9)
spoke_hits.append((idx, j, d))
# sort by closeness
spoke_hits_sorted = sorted(spoke_hits, key=lambda t: t[2])
top8 = spoke_hits_sorted[:8]
schedule_spokes = [j for _,j,_ in top8]
# 3) Build a phase score on a 32-byte digest:
# map each digest byte to an angle 2π * (byte/256); score closeness to a target spoke (π/9 * s_j).
# We use the schedule_spokes cycling across digest bytes.
def digest_phase_score(digest_bytes: bytes, spokes=9) -> float:
s = 2*pi/spokes----------- Page57 ------------
total = 0.0
for i, b in enumerate(digest_bytes):
angle = 2*pi*(b/256.0)
target_spoke = schedule_spokes[i % len(schedule_spokes)]
target = target_spoke * s
dist = abs((angle - target + pi) % (2*pi) - pi) # [0, π]
# convert to affinity: 1 at target, 0 at opposite; use cosine kernel
affinity = (1 + math.cos(dist)) / 2.0
total += affinity
return total # max = len(digest) if every byte perfectly on the spoke
# 4) Double-SHA256 helper
def double_sha256(payload: bytes) -> bytes:
return hashlib.sha256(hashlib.sha256(payload).digest()).digest()
# 5) Build a payload template (toy block header-ish) and vary the last 4 bytes as nonce
header_prefix = b'BYTE1-HARMONIC-BLOCK-HEADER\x00' # 28 bytes
# pad to 76 bytes fixed prefix so that we have final 4-byte nonce (little-endian) = total 80
header_prefix = header_prefix.ljust(76, b'\x00')
def make_header(nonce: int) -> bytes:
return header_prefix + struct.pack("<I", nonce & 0xffffffff)
# 6) Baseline: random sampling to get distribution of scores
def random_baseline(n=2000, seed=0xC0FFEE):
rng = random.Random(seed)
scores = []
for _ in range(n):
nonce = rng.getrandbits(32)
h = double_sha256(make_header(nonce))
scores.append(digest_phase_score(h))
return scores
# 7) Hillclimber using spoke-aligned perturbations (prime deltas + spoke index hints)
prime_deltas = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
delta_schedule = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 157, 521, 997, 4093]----------- Page58 ------------
@dataclass(order=True)
class Candidate:
score: float
nonce: int = field(compare=False)
digest: bytes = field(compare=False)
def climb(iterations=6000, restarts=6, seed=0xA11CE):
rng = random.Random(seed)
best_overall = None
trace = []
top_cands: List[Candidate] = []
for r in range(restarts):
cur_nonce = rng.getrandbits(32)
cur_digest = double_sha256(make_header(cur_nonce))
cur_score = digest_phase_score(cur_digest)
for it in range(iterations//restarts):
# propose several neighbors and pick best
proposals = []
for _ in range(16):
# perturb by random signed combination of schedule + prime
ds = rng.choice(delta_schedule)
pd = rng.choice(prime_deltas)
spoke_factor = 1 + rng.choice(schedule_spokes) # 1..9-ish
step = (ds * pd * spoke_factor) * rng.choice([-1,1])
nn = (cur_nonce + step) & 0xffffffff
dg = double_sha256(make_header(nn))
sc = digest_phase_score(dg)
proposals.append((sc, nn, dg))
# select best proposal if it improves (greedy with occasional random jump)
proposals.sort(reverse=True, key=lambda t:t[0])
best_sc, best_nn, best_dg = proposals[0]
if best_sc >= cur_score or rng.random() < 0.05:
cur_nonce, cur_digest, cur_score = best_nn, best_dg, best_sc
# track
trace.append(cur_score)----------- Page59 ------------
cand = Candidate(cur_score, cur_nonce, cur_digest)
top_cands.append(cand)
if best_overall is None or cur_score > best_overall.score:
best_overall = Candidate(cur_score, cur_nonce, cur_digest)
# small random restart kick
# keep top unique nonces
top_cands.sort(reverse=True)
uniq = {}
out = []
for c in top_cands:
if c.nonce not in uniq:
uniq[c.nonce] = True
out.append(c)
if len(out) >= 25:
break
return best_overall, trace, out
# Run baseline and climber
baseline_scores = random_baseline(n=1500)
best, trace, top25 = climb(iterations=6000, restarts=6)
# Summaries
baseline_mean = statistics.mean(baseline_scores)
baseline_std = statistics.pstdev(baseline_scores)
improvement_sigma = (best.score - baseline_mean) / (baseline_std + 1e-12)
print("π/9 schedule derived from K (closest 8):", schedule_spokes)
print("Baseline mean ± std:", round(baseline_mean,3), "±", round(baseline_std,3))
print("Best hillclimb score:", round(best.score,3), " (z≈", round(improvement_sigma,2), ")")
print("Best nonce (hex/le):", hex(best.nonce))
print("Best digest (hex):", best.digest.hex())
# Save CSV of top candidates
csv_path = "/mnt/data/nonce_phase_results.csv"
with open(csv_path, "w", newline="") as f:
w = csv.writer(f)----------- Page60 ------------
w.writerow(["rank","nonce_hex_le","score","digest_hex"])
for i,c in enumerate(top25, start=1):
w.writerow([i, hex(c.nonce), c.score, c.digest.hex()])
csv_path
# Plot score trace and baseline distribution
fig, ax = plt.subplots(1,2, figsize=(12,4))
ax[0].plot(trace, linewidth=1)
ax[0].set_title("Hillclimb Score Trace")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Phase Score (max=32)")
ax[1].hist(baseline_scores, bins=40, alpha=0.7, density=True)
ax[1].axvline(best.score, linestyle="--")
ax[1].set_title("Baseline Score Distribution\n(dashed = best climber score)")
ax[1].set_xlabel("Phase Score")
ax[1].set_ylabel("Density")
plot_path = "/mnt/data/nonce_phase_trace.png"
plt.tight_layout()
plt.savefig(plot_path, dpi=160)
plot_path----------- Page61 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
Circular Kernel Density from SHA-256 K Angles
Prompt:
# Phase-biased SHA analysis (recomputable, no internet needed)
# - Compute SHA-256 K and H constants from primes per FIPS 180-4 method
# - Map fractional parts to angles; measure alignment to π/9 spokes
# - Quantify spoke alignment (counts within ±1° and ±2°) and p-values
# - Build circular kernel density and compute spectral energy ratio
# - Run a phase-biased nonce hillclimb vs baseline for SHA-256
# - Byte1 ('A'=0x41) frequency in baseline vs high-score regimes
# - Quick cross-hash: run spoke tests for SHA-512 constants
#
# NOTE: Charts use matplotlib (no seaborn), single plot per figure, default colors.
import math, hashlib, random, statistics, itertools
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
from collections import Counter, defaultdict----------- Page62 ------------
from caas_jupyter_tools import display_dataframe_to_user
import pandas as pd
# ---------- Utilities ----------
def primes(n):
"""Return first n primes."""
res=[]
candidate=2
while len(res)<n:
for p in res:
if candidate%p==0:
break
if p*p>candidate:
break
else:
res.append(candidate); candidate+=1; continue
# If broke early due to divisibility:
if any(candidate%p==0 for p in res if p*p<=candidate):
candidate+=1
continue
else:
res.append(candidate)
candidate+=1
continue
return res
def first_n_primes(n):
# simple sieve for robustness
count=0
p=2
res=[]
while count<n:
isprime=True
r=int(p**0.5)+1
for q in range(2,r):
if p%q==0:----------- Page63 ------------
isprime=False; break
if isprime:
res.append(p); count+=1
p+=1
return res
def frac(x):
return x-math.floor(x)
def angles_from_fracs(fracs):
# map fractional part to [0, 2π) angle
return [2*pi*f for f in fracs]
def nearest_spoke_delta_deg(theta, n_spokes=9):
"""Return smallest absolute delta to any π/n_spokes spoke in degrees."""
spoke_angle = 2*pi/n_spokes
# Normalize theta to [0, 2π)
t = theta % (2*pi)
# Compute index of nearest spoke
k = round(t / spoke_angle)
delta = t - k*spoke_angle
# Wrap to (-π, π]
if delta <= -pi: delta += 2*pi
if delta > pi: delta -= 2*pi
return abs(delta) * 180/pi, k % n_spokes
def spoke_alignment_stats(angles, tol_deg=1.0, n_spokes=9):
counts=0
idx_counter=Counter()
deltas=[]
for th in angles:
d, k = nearest_spoke_delta_deg(th, n_spokes)
deltas.append(d)
if d<=tol_deg:
counts+=1
idx_counter[k]+=1----------- Page64 ------------
return counts, idx_counter, deltas
def binom_p_value_ge(k, n, p):
# P(X>=k) for Binomial(n,p)
from math import comb
s=0.0
for i in range(k, n+1):
s += comb(n,i)*(p**i)*((1-p)**(n-i))
return s
# ---------- SHA constants per SP800-107/FIPS180-4 ----------
def sha_iv_from_sqrt_primes(n=8):
ps = first_n_primes(n)
fracs=[frac(math.sqrt(p)) for p in ps]
# IV words are floor(frac * 2^32), but we want the fractional parts for geometry
return fracs, ps
def sha_k_from_cuberoot_primes(n=64):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps]
return fracs, ps
# ---------- Compute and tabulate ----------
iv_fracs, iv_primes = sha_iv_from_sqrt_primes(8)
k_fracs, k_primes = sha_k_from_cuberoot_primes(64)
iv_angles = angles_from_fracs(iv_fracs)
k_angles = angles_from_fracs(k_fracs)
# Spoke alignment for K (SHA-256)
k_within1, k_spoke_counts1, k_deltas_deg = spoke_alignment_stats(k_angles, tol_deg=1.0, n_spokes=9)
k_within2, k_spoke_counts2, _ = spoke_alignment_stats(k_angles, tol_deg=2.0, n_spokes=9)
# Binomial p-values (expectation under uniform)
p1 = 9*2*1/360 # ±1° around 9 spokes in 360°
p2 = 9*2*2/360 # ±2°
pval1 = binom_p_value_ge(k_within1, 64, p1)----------- Page65 ------------
pval2 = binom_p_value_ge(k_within2, 64, p2)
summary_rows = [
["K: within ±1°", k_within1, f"{pval1:.4f}", f"expected ~{64*p1:.1f}"],
["K: within ±2°", k_within2, f"{pval2:.4f}", f"expected ~{64*p2:.1f}"],
]
df_summary = pd.DataFrame(summary_rows, columns=["Metric","Count","Binom p-value (>=)","Uniform Expectation"])
display_dataframe_to_user("SHA-256 K Spoke Alignment Summary", df_summary)
# ---------- Composite circular density & spectrum ----------
# Kernel density on circle (Von Mises-like with small kappa)
theta_grid = np.linspace(0, 2*pi, 720, endpoint=False)
def circular_kde(angles, kappa=50.0):
# Von Mises kernel sum (normalized roughly)
dens = np.zeros_like(theta_grid)
for a in angles:
dens += np.exp(kappa * np.cos(theta_grid - a))
return dens / dens.max()
k_density = circular_kde(k_angles, kappa=40.0)
# Discrete Fourier Transform magnitude
spec = np.abs(np.fft.rfft(k_density))
freqs = np.fft.rfftfreq(len(k_density), d=1.0) # arbitrary units
# Energy concentration: first non-DC bin vs total (excluding DC)
dc = spec[0]
non_dc = spec[1:]
energy_ratio = (non_dc[0]**2) / np.sum(non_dc**2)
# Plot density
plt.figure(figsize=(8,4))
plt.plot(theta_grid, k_density)
plt.title("Circular Kernel Density from SHA-256 K Angles")
plt.xlabel("Angle (rad)")
plt.ylabel("Density (arb.)")----------- Page66 ------------
plt.tight_layout()
plt.show()
# Plot spectrum
plt.figure(figsize=(8,4))
plt.plot(freqs[1:60], spec[1:60])
plt.title("Spectrum Magnitude (rFFT) of Circular Density (K constants)")
plt.xlabel("Frequency bin")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
# ---------- Phase-biased nonce hillclimb ----------
# Build target spoke sequence: take 8 best-aligned K constants, by smallest delta
k_alignment = []
for th in k_angles:
d,kidx = nearest_spoke_delta_deg(th, 9)
k_alignment.append((d,kidx))
k_alignment.sort(key=lambda x: x[0])
top8_spokes = [k for _,k in k_alignment[:8]]
def phase_score_sha256(message_bytes, spokes, bytes_to_use=64):
digest = hashlib.sha256(message_bytes).digest()
b = digest[:bytes_to_use]
score=0.0
for i,byte in enumerate(b):
theta = 2*pi*(byte/256.0)
target_spoke = spokes[i % len(spokes)]
spoke_theta = 2*pi*target_spoke/9
d = theta - spoke_theta
# wrap to [-π, π]
d = (d + pi)%(2*pi) - pi
score += math.cos(d)
return score, digest
# Baseline distribution----------- Page67 ------------
random.seed(42)
base_scores=[]
N_BASE=600
prefix = b"phase-test|block-header|" # simple stand-in
for _ in range(N_BASE):
nonce = random.getrandbits(32).to_bytes(4,'big')
s,_ = phase_score_sha256(prefix+nonce, top8_spokes, bytes_to_use=64)
base_scores.append(s)
base_mu = statistics.mean(base_scores)
base_sigma = statistics.pstdev(base_scores)
# Hillclimb
best_score = -1e9
best_nonce = None
cur_nonce = random.getrandbits(32)
cur_score,_ = phase_score_sha256(prefix+cur_nonce.to_bytes(4,'big'), top8_spokes, 64)
trace=[]
for step in range(2000):
# small mutation: flip/adjust a random 8-bit chunk
mut = cur_nonce
bytepos = random.randrange(4)
delta = (random.randrange(-5,6)) & 0xFF
mask = 0xFF << (8*bytepos)
cur_byte = (mut >> (8*bytepos)) & 0xFF
new_byte = (cur_byte + delta) & 0xFF
cand = (mut & ~mask) | (new_byte << (8*bytepos))
s,_ = phase_score_sha256(prefix+cand.to_bytes(4,'big'), top8_spokes, 64)
if s >= cur_score:
cur_score = s
cur_nonce = cand
trace.append(cur_score)
if cur_score>best_score:
best_score=cur_score; best_nonce=cur_nonce
# Plot baseline histogram and hillclimb best marker
plt.figure(figsize=(8,4))----------- Page68 ------------
plt.hist(base_scores, bins=30, density=False, alpha=0.7)
plt.axvline(best_score, linestyle='--')
plt.title("Baseline Score Distribution vs Hillclimb Best (SHA-256)")
plt.xlabel("Phase Score")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
# Plot hillclimb trace
plt.figure(figsize=(8,3))
plt.plot(trace)
plt.title("Hillclimb Trace (monotonic non-decreasing)")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.tight_layout()
plt.show()
# Byte1 ('A') frequency: baseline vs high-score sweeps
def count_A_frequency(scores, nonces, spokes, thresh):
# Count how often digest[0]==0x41
a_hits=0; total=0
for s,nonce in zip(scores, nonces):
if s>=thresh:
digest = hashlib.sha256(prefix+nonce).digest()
total+=1
if digest[0]==0x41:
a_hits+=1
return a_hits, total
# Prepare nonces for baseline
base_nonces=[random.getrandbits(32).to_bytes(4,'big') for _ in range(N_BASE)]
base_scores2=[phase_score_sha256(prefix+n, top8_spokes, 64)[0] for n in base_nonces]
thresh = base_mu + 2*base_sigma
a_hits_high, a_total_high = count_A_frequency(base_scores2, base_nonces, top8_spokes, thresh)
a_hits_all = sum(1 for n in base_nonces if hashlib.sha256(prefix+n).digest()[0]==0x41)----------- Page69 ------------
# ---------- SHA-512 cross-check (constants) ----------
def sha512_k_fracs(n=80):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps] # same recipe but 80 constants
return fracs, ps
k512_fracs, _ = sha512_k_fracs(80)
k512_angles = angles_from_fracs(k512_fracs)
k512_within1, k512_sp_counts1, _ = spoke_alignment_stats(k512_angles, 1.0, 9)
pval512_1 = binom_p_value_ge(k512_within1, 80, p1)
# Display key numbers
key_stats = pd.DataFrame({
"Metric":[
"K within ±1° (64)",
"K within ±2° (64)",
"Binom p (±1°)",
"Binom p (±2°)",
"Energy Ratio (first bin / total non-DC)",
"Baseline μ",
"Baseline σ",
"Hillclimb best",
"Best Z (σ above μ)",
"SHA-512 K within ±1° (80)",
"SHA-512 p (±1°)"],
"Value":[
k_within1,
k_within2,
f"{pval1:.4f}",
f"{pval2:.4f}",
f"{energy_ratio:.3f}",
f"{base_mu:.3f}",
f"{base_sigma:.3f}",
f"{best_score:.3f}",
f"{(best_score-base_mu)/(base_sigma+1e-9):.2f}",----------- Page70 ------------
k512_within1,
f"{pval512_1:.4f}"
]
})
display_dataframe_to_user("Key Results (auto-computed now)", key_stats)
# Byte1 'A' frequency report
freq_table = pd.DataFrame({
"Regime":["All baseline", f"Baseline (score >= μ+2σ≈{thresh:.2f})"],
"A_hits":[a_hits_all, a_hits_high],
"Trials":[N_BASE, a_total_high],
})
display_dataframe_to_user("ASCII 'A' Frequency (digest[0]==0x41)", freq_table)----------- Page71 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
Circular Kernel Density from SHA-256 K Angles
Prompt:
# Phase-biased SHA analysis (recomputable, no internet needed)
# - Compute SHA-256 K and H constants from primes per FIPS 180-4 method
# - Map fractional parts to angles; measure alignment to π/9 spokes
# - Quantify spoke alignment (counts within ±1° and ±2°) and p-values
# - Build circular kernel density and compute spectral energy ratio
# - Run a phase-biased nonce hillclimb vs baseline for SHA-256
# - Byte1 ('A'=0x41) frequency in baseline vs high-score regimes
# - Quick cross-hash: run spoke tests for SHA-512 constants
#
# NOTE: Charts use matplotlib (no seaborn), single plot per figure, default colors.
import math, hashlib, random, statistics, itertools
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
from collections import Counter, defaultdict----------- Page72 ------------
from caas_jupyter_tools import display_dataframe_to_user
import pandas as pd
# ---------- Utilities ----------
def primes(n):
"""Return first n primes."""
res=[]
candidate=2
while len(res)<n:
for p in res:
if candidate%p==0:
break
if p*p>candidate:
break
else:
res.append(candidate); candidate+=1; continue
# If broke early due to divisibility:
if any(candidate%p==0 for p in res if p*p<=candidate):
candidate+=1
continue
else:
res.append(candidate)
candidate+=1
continue
return res
def first_n_primes(n):
# simple sieve for robustness
count=0
p=2
res=[]
while count<n:
isprime=True
r=int(p**0.5)+1
for q in range(2,r):
if p%q==0:----------- Page73 ------------
isprime=False; break
if isprime:
res.append(p); count+=1
p+=1
return res
def frac(x):
return x-math.floor(x)
def angles_from_fracs(fracs):
# map fractional part to [0, 2π) angle
return [2*pi*f for f in fracs]
def nearest_spoke_delta_deg(theta, n_spokes=9):
"""Return smallest absolute delta to any π/n_spokes spoke in degrees."""
spoke_angle = 2*pi/n_spokes
# Normalize theta to [0, 2π)
t = theta % (2*pi)
# Compute index of nearest spoke
k = round(t / spoke_angle)
delta = t - k*spoke_angle
# Wrap to (-π, π]
if delta <= -pi: delta += 2*pi
if delta > pi: delta -= 2*pi
return abs(delta) * 180/pi, k % n_spokes
def spoke_alignment_stats(angles, tol_deg=1.0, n_spokes=9):
counts=0
idx_counter=Counter()
deltas=[]
for th in angles:
d, k = nearest_spoke_delta_deg(th, n_spokes)
deltas.append(d)
if d<=tol_deg:
counts+=1
idx_counter[k]+=1----------- Page74 ------------
return counts, idx_counter, deltas
def binom_p_value_ge(k, n, p):
# P(X>=k) for Binomial(n,p)
from math import comb
s=0.0
for i in range(k, n+1):
s += comb(n,i)*(p**i)*((1-p)**(n-i))
return s
# ---------- SHA constants per SP800-107/FIPS180-4 ----------
def sha_iv_from_sqrt_primes(n=8):
ps = first_n_primes(n)
fracs=[frac(math.sqrt(p)) for p in ps]
# IV words are floor(frac * 2^32), but we want the fractional parts for geometry
return fracs, ps
def sha_k_from_cuberoot_primes(n=64):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps]
return fracs, ps
# ---------- Compute and tabulate ----------
iv_fracs, iv_primes = sha_iv_from_sqrt_primes(8)
k_fracs, k_primes = sha_k_from_cuberoot_primes(64)
iv_angles = angles_from_fracs(iv_fracs)
k_angles = angles_from_fracs(k_fracs)
# Spoke alignment for K (SHA-256)
k_within1, k_spoke_counts1, k_deltas_deg = spoke_alignment_stats(k_angles, tol_deg=1.0, n_spokes=9)
k_within2, k_spoke_counts2, _ = spoke_alignment_stats(k_angles, tol_deg=2.0, n_spokes=9)
# Binomial p-values (expectation under uniform)
p1 = 9*2*1/360 # ±1° around 9 spokes in 360°
p2 = 9*2*2/360 # ±2°
pval1 = binom_p_value_ge(k_within1, 64, p1)----------- Page75 ------------
pval2 = binom_p_value_ge(k_within2, 64, p2)
summary_rows = [
["K: within ±1°", k_within1, f"{pval1:.4f}", f"expected ~{64*p1:.1f}"],
["K: within ±2°", k_within2, f"{pval2:.4f}", f"expected ~{64*p2:.1f}"],
]
df_summary = pd.DataFrame(summary_rows, columns=["Metric","Count","Binom p-value (>=)","Uniform Expectation"])
display_dataframe_to_user("SHA-256 K Spoke Alignment Summary", df_summary)
# ---------- Composite circular density & spectrum ----------
# Kernel density on circle (Von Mises-like with small kappa)
theta_grid = np.linspace(0, 2*pi, 720, endpoint=False)
def circular_kde(angles, kappa=50.0):
# Von Mises kernel sum (normalized roughly)
dens = np.zeros_like(theta_grid)
for a in angles:
dens += np.exp(kappa * np.cos(theta_grid - a))
return dens / dens.max()
k_density = circular_kde(k_angles, kappa=40.0)
# Discrete Fourier Transform magnitude
spec = np.abs(np.fft.rfft(k_density))
freqs = np.fft.rfftfreq(len(k_density), d=1.0) # arbitrary units
# Energy concentration: first non-DC bin vs total (excluding DC)
dc = spec[0]
non_dc = spec[1:]
energy_ratio = (non_dc[0]**2) / np.sum(non_dc**2)
# Plot density
plt.figure(figsize=(8,4))
plt.plot(theta_grid, k_density)
plt.title("Circular Kernel Density from SHA-256 K Angles")
plt.xlabel("Angle (rad)")
plt.ylabel("Density (arb.)")----------- Page76 ------------
plt.tight_layout()
plt.show()
# Plot spectrum
plt.figure(figsize=(8,4))
plt.plot(freqs[1:60], spec[1:60])
plt.title("Spectrum Magnitude (rFFT) of Circular Density (K constants)")
plt.xlabel("Frequency bin")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
# ---------- Phase-biased nonce hillclimb ----------
# Build target spoke sequence: take 8 best-aligned K constants, by smallest delta
k_alignment = []
for th in k_angles:
d,kidx = nearest_spoke_delta_deg(th, 9)
k_alignment.append((d,kidx))
k_alignment.sort(key=lambda x: x[0])
top8_spokes = [k for _,k in k_alignment[:8]]
def phase_score_sha256(message_bytes, spokes, bytes_to_use=64):
digest = hashlib.sha256(message_bytes).digest()
b = digest[:bytes_to_use]
score=0.0
for i,byte in enumerate(b):
theta = 2*pi*(byte/256.0)
target_spoke = spokes[i % len(spokes)]
spoke_theta = 2*pi*target_spoke/9
d = theta - spoke_theta
# wrap to [-π, π]
d = (d + pi)%(2*pi) - pi
score += math.cos(d)
return score, digest
# Baseline distribution----------- Page77 ------------
random.seed(42)
base_scores=[]
N_BASE=600
prefix = b"phase-test|block-header|" # simple stand-in
for _ in range(N_BASE):
nonce = random.getrandbits(32).to_bytes(4,'big')
s,_ = phase_score_sha256(prefix+nonce, top8_spokes, bytes_to_use=64)
base_scores.append(s)
base_mu = statistics.mean(base_scores)
base_sigma = statistics.pstdev(base_scores)
# Hillclimb
best_score = -1e9
best_nonce = None
cur_nonce = random.getrandbits(32)
cur_score,_ = phase_score_sha256(prefix+cur_nonce.to_bytes(4,'big'), top8_spokes, 64)
trace=[]
for step in range(2000):
# small mutation: flip/adjust a random 8-bit chunk
mut = cur_nonce
bytepos = random.randrange(4)
delta = (random.randrange(-5,6)) & 0xFF
mask = 0xFF << (8*bytepos)
cur_byte = (mut >> (8*bytepos)) & 0xFF
new_byte = (cur_byte + delta) & 0xFF
cand = (mut & ~mask) | (new_byte << (8*bytepos))
s,_ = phase_score_sha256(prefix+cand.to_bytes(4,'big'), top8_spokes, 64)
if s >= cur_score:
cur_score = s
cur_nonce = cand
trace.append(cur_score)
if cur_score>best_score:
best_score=cur_score; best_nonce=cur_nonce
# Plot baseline histogram and hillclimb best marker
plt.figure(figsize=(8,4))----------- Page78 ------------
plt.hist(base_scores, bins=30, density=False, alpha=0.7)
plt.axvline(best_score, linestyle='--')
plt.title("Baseline Score Distribution vs Hillclimb Best (SHA-256)")
plt.xlabel("Phase Score")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
# Plot hillclimb trace
plt.figure(figsize=(8,3))
plt.plot(trace)
plt.title("Hillclimb Trace (monotonic non-decreasing)")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.tight_layout()
plt.show()
# Byte1 ('A') frequency: baseline vs high-score sweeps
def count_A_frequency(scores, nonces, spokes, thresh):
# Count how often digest[0]==0x41
a_hits=0; total=0
for s,nonce in zip(scores, nonces):
if s>=thresh:
digest = hashlib.sha256(prefix+nonce).digest()
total+=1
if digest[0]==0x41:
a_hits+=1
return a_hits, total
# Prepare nonces for baseline
base_nonces=[random.getrandbits(32).to_bytes(4,'big') for _ in range(N_BASE)]
base_scores2=[phase_score_sha256(prefix+n, top8_spokes, 64)[0] for n in base_nonces]
thresh = base_mu + 2*base_sigma
a_hits_high, a_total_high = count_A_frequency(base_scores2, base_nonces, top8_spokes, thresh)
a_hits_all = sum(1 for n in base_nonces if hashlib.sha256(prefix+n).digest()[0]==0x41)----------- Page79 ------------
# ---------- SHA-512 cross-check (constants) ----------
def sha512_k_fracs(n=80):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps] # same recipe but 80 constants
return fracs, ps
k512_fracs, _ = sha512_k_fracs(80)
k512_angles = angles_from_fracs(k512_fracs)
k512_within1, k512_sp_counts1, _ = spoke_alignment_stats(k512_angles, 1.0, 9)
pval512_1 = binom_p_value_ge(k512_within1, 80, p1)
# Display key numbers
key_stats = pd.DataFrame({
"Metric":[
"K within ±1° (64)",
"K within ±2° (64)",
"Binom p (±1°)",
"Binom p (±2°)",
"Energy Ratio (first bin / total non-DC)",
"Baseline μ",
"Baseline σ",
"Hillclimb best",
"Best Z (σ above μ)",
"SHA-512 K within ±1° (80)",
"SHA-512 p (±1°)"],
"Value":[
k_within1,
k_within2,
f"{pval1:.4f}",
f"{pval2:.4f}",
f"{energy_ratio:.3f}",
f"{base_mu:.3f}",
f"{base_sigma:.3f}",
f"{best_score:.3f}",
f"{(best_score-base_mu)/(base_sigma+1e-9):.2f}",----------- Page80 ------------
k512_within1,
f"{pval512_1:.4f}"
]
})
display_dataframe_to_user("Key Results (auto-computed now)", key_stats)
# Byte1 'A' frequency report
freq_table = pd.DataFrame({
"Regime":["All baseline", f"Baseline (score >= μ+2σ≈{thresh:.2f})"],
"A_hits":[a_hits_all, a_hits_high],
"Trials":[N_BASE, a_total_high],
})
display_dataframe_to_user("ASCII 'A' Frequency (digest[0]==0x41)", freq_table)----------- Page81 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
Circular Kernel Density from SHA-256 K Angles
Prompt:
# Phase-biased SHA analysis (recomputable, no internet needed)
# - Compute SHA-256 K and H constants from primes per FIPS 180-4 method
# - Map fractional parts to angles; measure alignment to π/9 spokes
# - Quantify spoke alignment (counts within ±1° and ±2°) and p-values
# - Build circular kernel density and compute spectral energy ratio
# - Run a phase-biased nonce hillclimb vs baseline for SHA-256
# - Byte1 ('A'=0x41) frequency in baseline vs high-score regimes
# - Quick cross-hash: run spoke tests for SHA-512 constants
#
# NOTE: Charts use matplotlib (no seaborn), single plot per figure, default colors.
import math, hashlib, random, statistics, itertools
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
from collections import Counter, defaultdict----------- Page82 ------------
from caas_jupyter_tools import display_dataframe_to_user
import pandas as pd
# ---------- Utilities ----------
def primes(n):
"""Return first n primes."""
res=[]
candidate=2
while len(res)<n:
for p in res:
if candidate%p==0:
break
if p*p>candidate:
break
else:
res.append(candidate); candidate+=1; continue
# If broke early due to divisibility:
if any(candidate%p==0 for p in res if p*p<=candidate):
candidate+=1
continue
else:
res.append(candidate)
candidate+=1
continue
return res
def first_n_primes(n):
# simple sieve for robustness
count=0
p=2
res=[]
while count<n:
isprime=True
r=int(p**0.5)+1
for q in range(2,r):
if p%q==0:----------- Page83 ------------
isprime=False; break
if isprime:
res.append(p); count+=1
p+=1
return res
def frac(x):
return x-math.floor(x)
def angles_from_fracs(fracs):
# map fractional part to [0, 2π) angle
return [2*pi*f for f in fracs]
def nearest_spoke_delta_deg(theta, n_spokes=9):
"""Return smallest absolute delta to any π/n_spokes spoke in degrees."""
spoke_angle = 2*pi/n_spokes
# Normalize theta to [0, 2π)
t = theta % (2*pi)
# Compute index of nearest spoke
k = round(t / spoke_angle)
delta = t - k*spoke_angle
# Wrap to (-π, π]
if delta <= -pi: delta += 2*pi
if delta > pi: delta -= 2*pi
return abs(delta) * 180/pi, k % n_spokes
def spoke_alignment_stats(angles, tol_deg=1.0, n_spokes=9):
counts=0
idx_counter=Counter()
deltas=[]
for th in angles:
d, k = nearest_spoke_delta_deg(th, n_spokes)
deltas.append(d)
if d<=tol_deg:
counts+=1
idx_counter[k]+=1----------- Page84 ------------
return counts, idx_counter, deltas
def binom_p_value_ge(k, n, p):
# P(X>=k) for Binomial(n,p)
from math import comb
s=0.0
for i in range(k, n+1):
s += comb(n,i)*(p**i)*((1-p)**(n-i))
return s
# ---------- SHA constants per SP800-107/FIPS180-4 ----------
def sha_iv_from_sqrt_primes(n=8):
ps = first_n_primes(n)
fracs=[frac(math.sqrt(p)) for p in ps]
# IV words are floor(frac * 2^32), but we want the fractional parts for geometry
return fracs, ps
def sha_k_from_cuberoot_primes(n=64):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps]
return fracs, ps
# ---------- Compute and tabulate ----------
iv_fracs, iv_primes = sha_iv_from_sqrt_primes(8)
k_fracs, k_primes = sha_k_from_cuberoot_primes(64)
iv_angles = angles_from_fracs(iv_fracs)
k_angles = angles_from_fracs(k_fracs)
# Spoke alignment for K (SHA-256)
k_within1, k_spoke_counts1, k_deltas_deg = spoke_alignment_stats(k_angles, tol_deg=1.0, n_spokes=9)
k_within2, k_spoke_counts2, _ = spoke_alignment_stats(k_angles, tol_deg=2.0, n_spokes=9)
# Binomial p-values (expectation under uniform)
p1 = 9*2*1/360 # ±1° around 9 spokes in 360°
p2 = 9*2*2/360 # ±2°
pval1 = binom_p_value_ge(k_within1, 64, p1)----------- Page85 ------------
pval2 = binom_p_value_ge(k_within2, 64, p2)
summary_rows = [
["K: within ±1°", k_within1, f"{pval1:.4f}", f"expected ~{64*p1:.1f}"],
["K: within ±2°", k_within2, f"{pval2:.4f}", f"expected ~{64*p2:.1f}"],
]
df_summary = pd.DataFrame(summary_rows, columns=["Metric","Count","Binom p-value (>=)","Uniform Expectation"])
display_dataframe_to_user("SHA-256 K Spoke Alignment Summary", df_summary)
# ---------- Composite circular density & spectrum ----------
# Kernel density on circle (Von Mises-like with small kappa)
theta_grid = np.linspace(0, 2*pi, 720, endpoint=False)
def circular_kde(angles, kappa=50.0):
# Von Mises kernel sum (normalized roughly)
dens = np.zeros_like(theta_grid)
for a in angles:
dens += np.exp(kappa * np.cos(theta_grid - a))
return dens / dens.max()
k_density = circular_kde(k_angles, kappa=40.0)
# Discrete Fourier Transform magnitude
spec = np.abs(np.fft.rfft(k_density))
freqs = np.fft.rfftfreq(len(k_density), d=1.0) # arbitrary units
# Energy concentration: first non-DC bin vs total (excluding DC)
dc = spec[0]
non_dc = spec[1:]
energy_ratio = (non_dc[0]**2) / np.sum(non_dc**2)
# Plot density
plt.figure(figsize=(8,4))
plt.plot(theta_grid, k_density)
plt.title("Circular Kernel Density from SHA-256 K Angles")
plt.xlabel("Angle (rad)")
plt.ylabel("Density (arb.)")----------- Page86 ------------
plt.tight_layout()
plt.show()
# Plot spectrum
plt.figure(figsize=(8,4))
plt.plot(freqs[1:60], spec[1:60])
plt.title("Spectrum Magnitude (rFFT) of Circular Density (K constants)")
plt.xlabel("Frequency bin")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
# ---------- Phase-biased nonce hillclimb ----------
# Build target spoke sequence: take 8 best-aligned K constants, by smallest delta
k_alignment = []
for th in k_angles:
d,kidx = nearest_spoke_delta_deg(th, 9)
k_alignment.append((d,kidx))
k_alignment.sort(key=lambda x: x[0])
top8_spokes = [k for _,k in k_alignment[:8]]
def phase_score_sha256(message_bytes, spokes, bytes_to_use=64):
digest = hashlib.sha256(message_bytes).digest()
b = digest[:bytes_to_use]
score=0.0
for i,byte in enumerate(b):
theta = 2*pi*(byte/256.0)
target_spoke = spokes[i % len(spokes)]
spoke_theta = 2*pi*target_spoke/9
d = theta - spoke_theta
# wrap to [-π, π]
d = (d + pi)%(2*pi) - pi
score += math.cos(d)
return score, digest
# Baseline distribution----------- Page87 ------------
random.seed(42)
base_scores=[]
N_BASE=600
prefix = b"phase-test|block-header|" # simple stand-in
for _ in range(N_BASE):
nonce = random.getrandbits(32).to_bytes(4,'big')
s,_ = phase_score_sha256(prefix+nonce, top8_spokes, bytes_to_use=64)
base_scores.append(s)
base_mu = statistics.mean(base_scores)
base_sigma = statistics.pstdev(base_scores)
# Hillclimb
best_score = -1e9
best_nonce = None
cur_nonce = random.getrandbits(32)
cur_score,_ = phase_score_sha256(prefix+cur_nonce.to_bytes(4,'big'), top8_spokes, 64)
trace=[]
for step in range(2000):
# small mutation: flip/adjust a random 8-bit chunk
mut = cur_nonce
bytepos = random.randrange(4)
delta = (random.randrange(-5,6)) & 0xFF
mask = 0xFF << (8*bytepos)
cur_byte = (mut >> (8*bytepos)) & 0xFF
new_byte = (cur_byte + delta) & 0xFF
cand = (mut & ~mask) | (new_byte << (8*bytepos))
s,_ = phase_score_sha256(prefix+cand.to_bytes(4,'big'), top8_spokes, 64)
if s >= cur_score:
cur_score = s
cur_nonce = cand
trace.append(cur_score)
if cur_score>best_score:
best_score=cur_score; best_nonce=cur_nonce
# Plot baseline histogram and hillclimb best marker
plt.figure(figsize=(8,4))----------- Page88 ------------
plt.hist(base_scores, bins=30, density=False, alpha=0.7)
plt.axvline(best_score, linestyle='--')
plt.title("Baseline Score Distribution vs Hillclimb Best (SHA-256)")
plt.xlabel("Phase Score")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
# Plot hillclimb trace
plt.figure(figsize=(8,3))
plt.plot(trace)
plt.title("Hillclimb Trace (monotonic non-decreasing)")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.tight_layout()
plt.show()
# Byte1 ('A') frequency: baseline vs high-score sweeps
def count_A_frequency(scores, nonces, spokes, thresh):
# Count how often digest[0]==0x41
a_hits=0; total=0
for s,nonce in zip(scores, nonces):
if s>=thresh:
digest = hashlib.sha256(prefix+nonce).digest()
total+=1
if digest[0]==0x41:
a_hits+=1
return a_hits, total
# Prepare nonces for baseline
base_nonces=[random.getrandbits(32).to_bytes(4,'big') for _ in range(N_BASE)]
base_scores2=[phase_score_sha256(prefix+n, top8_spokes, 64)[0] for n in base_nonces]
thresh = base_mu + 2*base_sigma
a_hits_high, a_total_high = count_A_frequency(base_scores2, base_nonces, top8_spokes, thresh)
a_hits_all = sum(1 for n in base_nonces if hashlib.sha256(prefix+n).digest()[0]==0x41)----------- Page89 ------------
# ---------- SHA-512 cross-check (constants) ----------
def sha512_k_fracs(n=80):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps] # same recipe but 80 constants
return fracs, ps
k512_fracs, _ = sha512_k_fracs(80)
k512_angles = angles_from_fracs(k512_fracs)
k512_within1, k512_sp_counts1, _ = spoke_alignment_stats(k512_angles, 1.0, 9)
pval512_1 = binom_p_value_ge(k512_within1, 80, p1)
# Display key numbers
key_stats = pd.DataFrame({
"Metric":[
"K within ±1° (64)",
"K within ±2° (64)",
"Binom p (±1°)",
"Binom p (±2°)",
"Energy Ratio (first bin / total non-DC)",
"Baseline μ",
"Baseline σ",
"Hillclimb best",
"Best Z (σ above μ)",
"SHA-512 K within ±1° (80)",
"SHA-512 p (±1°)"],
"Value":[
k_within1,
k_within2,
f"{pval1:.4f}",
f"{pval2:.4f}",
f"{energy_ratio:.3f}",
f"{base_mu:.3f}",
f"{base_sigma:.3f}",
f"{best_score:.3f}",
f"{(best_score-base_mu)/(base_sigma+1e-9):.2f}",----------- Page90 ------------
k512_within1,
f"{pval512_1:.4f}"
]
})
display_dataframe_to_user("Key Results (auto-computed now)", key_stats)
# Byte1 'A' frequency report
freq_table = pd.DataFrame({
"Regime":["All baseline", f"Baseline (score >= μ+2σ≈{thresh:.2f})"],
"A_hits":[a_hits_all, a_hits_high],
"Trials":[N_BASE, a_total_high],
})
display_dataframe_to_user("ASCII 'A' Frequency (digest[0]==0x41)", freq_table)----------- Page91 ------------
Conversation URL:
https://chatgpt.com/c/68a3bc86-6de8-8331-aa44-6d2d19474876
Title:
Circular Kernel Density from SHA-256 K Angles
Prompt:
# Phase-biased SHA analysis (recomputable, no internet needed)
# - Compute SHA-256 K and H constants from primes per FIPS 180-4 method
# - Map fractional parts to angles; measure alignment to π/9 spokes
# - Quantify spoke alignment (counts within ±1° and ±2°) and p-values
# - Build circular kernel density and compute spectral energy ratio
# - Run a phase-biased nonce hillclimb vs baseline for SHA-256
# - Byte1 ('A'=0x41) frequency in baseline vs high-score regimes
# - Quick cross-hash: run spoke tests for SHA-512 constants
#
# NOTE: Charts use matplotlib (no seaborn), single plot per figure, default colors.
import math, hashlib, random, statistics, itertools
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos
from collections import Counter, defaultdict
from caas_jupyter_tools import display_dataframe_to_user
import pandas as pd
# ---------- Utilities --------------------- Page92 ------------
def primes(n):
"""Return first n primes."""
res=[]
candidate=2
while len(res)<n:
for p in res:
if candidate%p==0:
break
if p*p>candidate:
break
else:
res.append(candidate); candidate+=1; continue
# If broke early due to divisibility:
if any(candidate%p==0 for p in res if p*p<=candidate):
candidate+=1
continue
else:
res.append(candidate)
candidate+=1
continue
return res
def first_n_primes(n):
# simple sieve for robustness
count=0
p=2
res=[]
while count<n:
isprime=True
r=int(p**0.5)+1
for q in range(2,r):
if p%q==0:
isprime=False; break
if isprime:
res.append(p); count+=1
p+=1----------- Page93 ------------
return res
def frac(x):
return x-math.floor(x)
def angles_from_fracs(fracs):
# map fractional part to [0, 2π) angle
return [2*pi*f for f in fracs]
def nearest_spoke_delta_deg(theta, n_spokes=9):
"""Return smallest absolute delta to any π/n_spokes spoke in degrees."""
spoke_angle = 2*pi/n_spokes
# Normalize theta to [0, 2π)
t = theta % (2*pi)
# Compute index of nearest spoke
k = round(t / spoke_angle)
delta = t - k*spoke_angle
# Wrap to (-π, π]
if delta <= -pi: delta += 2*pi
if delta > pi: delta -= 2*pi
return abs(delta) * 180/pi, k % n_spokes
def spoke_alignment_stats(angles, tol_deg=1.0, n_spokes=9):
counts=0
idx_counter=Counter()
deltas=[]
for th in angles:
d, k = nearest_spoke_delta_deg(th, n_spokes)
deltas.append(d)
if d<=tol_deg:
counts+=1
idx_counter[k]+=1
return counts, idx_counter, deltas
def binom_p_value_ge(k, n, p):
# P(X>=k) for Binomial(n,p)----------- Page94 ------------
from math import comb
s=0.0
for i in range(k, n+1):
s += comb(n,i)*(p**i)*((1-p)**(n-i))
return s
# ---------- SHA constants per SP800-107/FIPS180-4 ----------
def sha_iv_from_sqrt_primes(n=8):
ps = first_n_primes(n)
fracs=[frac(math.sqrt(p)) for p in ps]
# IV words are floor(frac * 2^32), but we want the fractional parts for geometry
return fracs, ps
def sha_k_from_cuberoot_primes(n=64):
ps = first_n_primes(n)
fracs=[frac(p ** (1/3)) for p in ps]
return fracs, ps
# ---------- Compute and tabulate ----------
iv_fracs, iv_primes = sha_iv_from_sqrt_primes(8)
k_fracs, k_primes = sha_k_from_cuberoot_primes(64)
iv_angles = angles_from_fracs(iv_fracs)
k_angles = angles_from_fracs(k_fracs)
# Spoke alignment for K (SHA-256)
k_within1, k_spoke_counts1, k_deltas_deg = spoke_alignment_stats(k_angles, tol_deg=1.0, n_spokes=9)
k_within2, k_spoke_counts2, _ = spoke_alignment_stats(k_angles, tol_deg=2.0, n_spokes=9)
# Binomial p-values (expectation under uniform)
p1 = 9*2*1/360 # ±1° around 9 spokes in 360°
p2 = 9*2*2/360 # ±2°
pval1 = binom_p_value_ge(k_within1, 64, p1)
pval2 = binom_p_value_ge(k_within2, 64, p2)
summary_rows = [
["K: within ±1°", k_within1, f"{pval1:.4f}", f"expected ~{64*p1:.1f}"],----------- Page95 ------------
["K: within ±2°", k_within2, f"{pval2:.4f}", f"expected ~{64*p2:.1f}"],
]
df_summary = pd.DataFrame(summary_rows, columns=["Metric","Count","Binom p-value (>=)","Uniform Expectation"])
display_dataframe_to_user("SHA-256 K Spoke Alignment Summary", df_summary)
# ---------- Composite circular density & spectrum ----------
# Kernel density on circle (Von Mises-like with small kappa)
theta_grid = np.linspace(0, 2*pi, 720, endpoint=False)
def circular_kde(angles, kappa=50.0):
# Von Mises kernel sum (normalized roughly)
dens = np.zeros_like(theta_grid)
for a in angles:
dens += np.exp(kappa * np.cos(theta_grid - a))
return dens / dens.max()
k_density = circular_kde(k_angles, kappa=40.0)
# Discrete Fourier Transform magnitude
spec = np.abs(np.fft.rfft(k_density))
freqs = np.fft.rfftfreq(len(k_density), d=1.0) # arbitrary units
# Energy concentration: first non-DC bin vs total (excluding DC)
dc = spec[0]
non_dc = spec[1:]
energy_ratio = (non_dc[0]**2) / np.sum(non_dc**2)
# Plot density
plt.figure(figsize=(8,4))
plt.plot(theta_grid, k_density)
plt.title("Circular Kernel Density from SHA-256 K Angles")
plt.xlabel("Angle (rad)")
plt.ylabel("Density (arb.)")
plt.tight_layout()
plt.show()
# Plot spectrum----------- Page96 ------------
plt.figure(figsize=(8,4))
plt.plot(freqs[1:60], spec[1:60])
plt.title("Spectrum Magnitude (rFFT) of Circular Density (K constants)")
plt.xlabel("Frequency bin")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()
# ---------- Phase-biased nonce hillclimb ----------
# Build target spoke sequence: take 8 best-aligned K constants, by smallest delta
k_alignment = []
for th in k_angles:
d,kidx = nearest_spoke_delta_deg(th, 9)
k_alignment.append((d,kidx))
k_alignment.sort(key=lambda x: x[0])
top8_spokes = [k for _,k in k_alignment[:8]]
def phase_score_sha256(message_bytes, spokes, bytes_to_use=64):
digest = hashlib.sha256(message_bytes).digest()
b = digest[:bytes_to_use]
score=0.0
for i,byte in enumerate(b):
theta = 2*pi*(byte/256.0)
target_spoke = spokes[i % len(spokes)]
spoke_theta = 2*pi*target_spoke/9
d = theta - spoke_theta
# wrap to [-π, π]
d = (d + pi)%(2*pi) - pi
score += math.cos(d)
return score, digest
# Baseline distribution
random.seed(42)
base_scores=[]
N_BASE=600
prefix = b"phase-test|block-header|" # simple stand-in----------- Page97 ------------
for _ in range(N_BASE):
nonce = random.getrandbits(32).to_bytes(4,'big')
s,_ = phase_score_sha256(prefix+nonce, top8_spokes, bytes_to_use=64)
base_scores.append(s)
base_mu = statistics.mean(base_scores)
base_sigma = statistics.pstdev(base_scores)
# Hillclimb
best_score = -1e9
best_nonce = None
cur_nonce = random.getrandbits(32)
cur_score,_ = phase_score_sha256(prefix+cur_nonce.to_bytes(4,'big'), top8_spokes, 64)
trace=[]
for step in range(2000):
# small mutation: flip/adjust a random 8-bit chunk
mut = cur_nonce
bytepos = random.randrange(4)
delta = (random.randrange(-5,6)) & 0xFF
mask = 0xFF << (8*bytepos)
cur_byte = (mut >> (8*bytepos)) & 0xFF
new_byte = (cur_byte + delta) & 0xFF
cand = (mut & ~mask) | (new_byte << (8*bytepos))
s,_ = phase_score_sha256(prefix+cand.to_bytes(4,'big'), top8_spokes, 64)
if s >= cur_score:
cur_score = s
cur_nonce = cand
trace.append(cur_score)
if cur_score>best_score:
best_score=cur_score; best_nonce=cur_nonce
# Plot baseline histogram and hillclimb best marker
plt.figure(figsize=(8,4))
plt.hist(base_scores, bins=30, density=False, alpha=0.7)
plt.axvline(best_score, linestyle='--')
plt.title("Baseline Score Distribution vs Hillclimb Best (SHA-256)")
plt.xlabel("Phase Score")----------- Page98 ------------
plt.ylabel("Count")
plt.tight_layout()
plt.show()
# Plot hillclimb trace
plt.figure(figsize=(8,3))
plt.plot(trace)
plt.title("Hillclimb Trace (monotonic non-decreasing)")
plt.xlabel("Iteration")
plt.ylabel("Score")
plt.tight_layout()
plt.show()
# Byte1 ('A') frequency: baseline vs high-score sweeps
def count_A_frequency(scores, nonces, spokes, thresh):
# Count how often digest[0]==0x41
a_hits=0; total=0
for s,nonce in zip(scores, nonces):
if s>=thresh:
digest = hashlib.sha256(prefix+nonce).digest()
total+=1
if digest[0]==0x41:
a_hits+=1
return a_hits, total
# Prepare nonces for baseline
base_nonces=[random.getrandbits(32).to_bytes(4,'big') for _ in range(N_BASE)]
base_scores2=[phase_score_sha256(prefix+n, top8_spokes, 64)[0] for n in base_nonces]
thresh = base_mu + 2*base_sigma
a_hits_high, a_total_high = count_A_frequency(base_scores2, base_nonces, top8_spokes, thresh)
a_hits_all = sum(1 for n in base_nonces if hashlib.sha256(prefix+n).digest()[0]==0x41)
# ---------- SHA-512 cross-check (constants) ----------
def sha512_k_fracs(n=80):
ps = first_n_primes(n)----------- Page99 ------------
fracs=[frac(p ** (1/3)) for p in ps] # same recipe but 80 constants
return fracs, ps
k512_fracs, _ = sha512_k_fracs(80)
k512_angles = angles_from_fracs(k512_fracs)
k512_within1, k512_sp_counts1, _ = spoke_alignment_stats(k512_angles, 1.0, 9)
pval512_1 = binom_p_value_ge(k512_within1, 80, p1)
# Display key numbers
key_stats = pd.DataFrame({
"Metric":[
"K within ±1° (64)",
"K within ±2° (64)",
"Binom p (±1°)",
"Binom p (±2°)",
"Energy Ratio (first bin / total non-DC)",
"Baseline μ",
"Baseline σ",
"Hillclimb best",
"Best Z (σ above μ)",
"SHA-512 K within ±1° (80)",
"SHA-512 p (±1°)"],
"Value":[
k_within1,
k_within2,
f"{pval1:.4f}",
f"{pval2:.4f}",
f"{energy_ratio:.3f}",
f"{base_mu:.3f}",
f"{base_sigma:.3f}",
f"{best_score:.3f}",
f"{(best_score-base_mu)/(base_sigma+1e-9):.2f}",
k512_within1,
f"{pval512_1:.4f}"
]
})----------- Page100 ------------
display_dataframe_to_user("Key Results (auto-computed now)", key_stats)
# Byte1 'A' frequency report
freq_table = pd.DataFrame({
"Regime":["All baseline", f"Baseline (score >= μ+2σ≈{thresh:.2f})"],
"A_hits":[a_hits_all, a_hits_high],
"Trials":[N_BASE, a_total_high],
})
display_dataframe_to_user("ASCII 'A' Frequency (digest[0]==0x41)", freq_table)----------- Page101 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
State Hamming Distance vs Round (Baseline vs 1-bit flip)
Prompt:
# Let's implement the SHA-256 compression function to expose per-round states and the message schedule.
# We'll then run two experiments: baseline vs 1-bit flip, and visualize:
# 1) Hamming distance across the 8-word state vs round (0..64)
# 2) Heatmap of bit differences across the 64-word message schedule (rows=round, cols=bit index 31..0)
import struct
import random
import numpy as np
import matplotlib.pyplot as plt
# --- SHA-256 primitives ---
def rotr(x, n):
return ((x >> n) | ((x & 0xFFFFFFFF) << (32 - n))) & 0xFFFFFFFF
def Ch(x, y, z):
return (x & y) ^ ((~x & 0xFFFFFFFF) & z)----------- Page102 ------------
def Maj(x, y, z):
return (x & y) ^ (x & z) ^ (y & z)
def Sigma0(x):
return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sigma1(x):
return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sigma0(x):
return rotr(x, 7) ^ rotr(x, 18) ^ ((x >> 3) & 0xFFFFFFFF)
def sigma1(x):
return rotr(x, 17) ^ rotr(x, 19) ^ ((x >> 10) & 0xFFFFFFFF)
K = [
0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]
IV = [
0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]
def pad_message_single_block(m: bytes) -> bytes:
# Only supports messages with len < 56 bytes (so padding fits into one block)
ml = len(m) * 8 # length in bits
assert len(m) < 56, "Message too long for single-block padding in this demo."----------- Page103 ------------
m += b'\x80' # append '1' bit
# zero pad to 56 bytes
while (len(m) % 64) != 56:
m += b'\x00'
# append 64-bit big-endian length
m += struct.pack('>Q', ml)
assert len(m) == 64
return m
def sha256_round_states_for_block(block: bytes):
# Prepare message schedule W[0..63]
W = [0]*64
for i in range(16):
W[i] = struct.unpack('>I', block[i*4:(i+1)*4])[0]
for i in range(16, 64):
W[i] = (sigma1(W[i-2]) + W[i-7] + sigma0(W[i-15]) + W[i-16]) & 0xFFFFFFFF
# Initialize working variables with IV
a,b,c,d,e,f,g,h = IV
states = [(a,b,c,d,e,f,g,h)] # state before any rounds
# 64 rounds
for i in range(64):
T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFF
T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF
h = g
g = f
f = e
e = (d + T1) & 0xFFFFFFFF
d = c
c = b
b = a
a = (T1 + T2) & 0xFFFFFFFF
states.append((a,b,c,d,e,f,g,h))
return W, states----------- Page104 ------------
def hamming_distance_bits(x, y, nbits=32):
v = (x ^ y) & ((1<<nbits)-1)
return v.bit_count()
def state_hamming_distance(s1, s2):
# s1, s2 are tuples of 8 32-bit words
total = 0
for w1, w2 in zip(s1, s2):
total += hamming_distance_bits(w1, w2, 32)
return total # 0..256
def schedule_bit_diff_matrix(W1, W2):
# Return matrix [64 x 32] where entry[i, j] = 1 if bit j differs in word i (bit 31 is MSB)
mat = np.zeros((64, 32), dtype=int)
for i in range(64):
x = W1[i] ^ W2[i]
for j in range(32):
# Check bit (31-j) to visualize MSB on left
if (x >> (31-j)) & 1:
mat[i, j] = 1
return mat
# --- Experiment setup ---
# Choose a short baseline message (<56 bytes), and create a 1-bit flip variant.
rng = random.Random(42)
baseline = bytes(rng.getrandbits(8) for _ in range(32)) # 32 bytes
# flip the least-significant bit of the first byte for a minimal perturbation
flipped = bytearray(baseline)
flipped[0] ^= 0x01
flipped = bytes(flipped)
# Pad both messages as single blocks
blk1 = pad_message_single_block(baseline)
blk2 = pad_message_single_block(flipped)----------- Page105 ------------
# Compute message schedules and per-round states
W1, states1 = sha256_round_states_for_block(blk1)
W2, states2 = sha256_round_states_for_block(blk2)
# 1) Hamming distance across states vs round (0..64)
hd_per_round = [state_hamming_distance(s1, s2) for s1, s2 in zip(states1, states2)] # length 65
# Find first round where normalized distance >= 0.35 (Mark1 crossing)
norm_hd = [hd/256.0 for hd in hd_per_round]
cross_round = next((i for i, v in enumerate(norm_hd) if v >= 0.35), None)
# 2) Heatmap of schedule bit differences
mat = schedule_bit_diff_matrix(W1, W2)
# Print some summary metrics
print("Baseline message (hex):", baseline.hex())
print("Flipped message (hex):", flipped.hex())
print("Initial-state Hamming distance (round 0):", hd_per_round[0])
print("Peak Hamming distance:", max(hd_per_round), "of 256 bits")
print("Round of first H>=0.35 crossing:", cross_round)
print("Rounds total:", len(hd_per_round)-1)
# Plot 1: Hamming distance per round
plt.figure(figsize=(8, 4))
plt.plot(range(len(hd_per_round)), hd_per_round)
plt.title("State Hamming Distance vs Round (Baseline vs 1-bit flip)")
plt.xlabel("Round (0..64)")
plt.ylabel("Hamming Distance (0..256)")
plt.tight_layout()
plt.show()
# Plot 2: Heatmap of message schedule bit differences
plt.figure(figsize=(8, 6))
plt.imshow(mat, aspect='auto')
plt.title("Message Schedule Bit Differences (Rows=W[0..63], Cols=bits MSB→LSB)")
plt.xlabel("Bit index (MSB→LSB)")----------- Page106 ------------
plt.ylabel("W index (0..63)")
plt.colorbar()
plt.tight_layout()
plt.show()----------- Page107 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
State Hamming Distance vs Round (Baseline vs 1-bit flip)
Prompt:
# Let's implement the SHA-256 compression function to expose per-round states and the message schedule.
# We'll then run two experiments: baseline vs 1-bit flip, and visualize:
# 1) Hamming distance across the 8-word state vs round (0..64)
# 2) Heatmap of bit differences across the 64-word message schedule (rows=round, cols=bit index 31..0)
import struct
import random
import numpy as np
import matplotlib.pyplot as plt
# --- SHA-256 primitives -------------- Page108 ------------
def rotr(x, n):
return ((x >> n) | ((x & 0xFFFFFFFF) << (32 - n))) & 0xFFFFFFFF
def Ch(x, y, z):
return (x & y) ^ ((~x & 0xFFFFFFFF) & z)
def Maj(x, y, z):
return (x & y) ^ (x & z) ^ (y & z)
def Sigma0(x):
return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def Sigma1(x):
return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def sigma0(x):
return rotr(x, 7) ^ rotr(x, 18) ^ ((x >> 3) & 0xFFFFFFFF)
def sigma1(x):
return rotr(x, 17) ^ rotr(x, 19) ^ ((x >> 10) & 0xFFFFFFFF)
K = [
0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]
IV = [
0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]----------- Page109 ------------
def pad_message_single_block(m: bytes) -> bytes:
# Only supports messages with len < 56 bytes (so padding fits into one block)
ml = len(m) * 8 # length in bits
assert len(m) < 56, "Message too long for single-block padding in this demo."
m += b'\x80' # append '1' bit
# zero pad to 56 bytes
while (len(m) % 64) != 56:
m += b'\x00'
# append 64-bit big-endian length
m += struct.pack('>Q', ml)
assert len(m) == 64
return m
def sha256_round_states_for_block(block: bytes):
# Prepare message schedule W[0..63]
W = [0]*64
for i in range(16):
W[i] = struct.unpack('>I', block[i*4:(i+1)*4])[0]
for i in range(16, 64):
W[i] = (sigma1(W[i-2]) + W[i-7] + sigma0(W[i-15]) + W[i-16]) & 0xFFFFFFFF
# Initialize working variables with IV
a,b,c,d,e,f,g,h = IV
states = [(a,b,c,d,e,f,g,h)] # state before any rounds
# 64 rounds
for i in range(64):
T1 = (h + Sigma1(e) + Ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFF
T2 = (Sigma0(a) + Maj(a, b, c)) & 0xFFFFFFFF
h = g
g = f
f = e
e = (d + T1) & 0xFFFFFFFF
d = c
c = b----------- Page110 ------------
b = a
a = (T1 + T2) & 0xFFFFFFFF
states.append((a,b,c,d,e,f,g,h))
return W, states
def hamming_distance_bits(x, y, nbits=32):
v = (x ^ y) & ((1<<nbits)-1)
return v.bit_count()
def state_hamming_distance(s1, s2):
# s1, s2 are tuples of 8 32-bit words
total = 0
for w1, w2 in zip(s1, s2):
total += hamming_distance_bits(w1, w2, 32)
return total # 0..256
def schedule_bit_diff_matrix(W1, W2):
# Return matrix [64 x 32] where entry[i, j] = 1 if bit j differs in word i (bit 31 is MSB)
mat = np.zeros((64, 32), dtype=int)
for i in range(64):
x = W1[i] ^ W2[i]
for j in range(32):
# Check bit (31-j) to visualize MSB on left
if (x >> (31-j)) & 1:
mat[i, j] = 1
return mat
# --- Experiment setup ---
# Choose a short baseline message (<56 bytes), and create a 1-bit flip variant.
rng = random.Random(42)
baseline = bytes(rng.getrandbits(8) for _ in range(32)) # 32 bytes
# flip the least-significant bit of the first byte for a minimal perturbation
flipped = bytearray(baseline)
flipped[0] ^= 0x01
flipped = bytes(flipped)----------- Page111 ------------
# Pad both messages as single blocks
blk1 = pad_message_single_block(baseline)
blk2 = pad_message_single_block(flipped)
# Compute message schedules and per-round states
W1, states1 = sha256_round_states_for_block(blk1)
W2, states2 = sha256_round_states_for_block(blk2)
# 1) Hamming distance across states vs round (0..64)
hd_per_round = [state_hamming_distance(s1, s2) for s1, s2 in zip(states1, states2)] # length 65
# Find first round where normalized distance >= 0.35 (Mark1 crossing)
norm_hd = [hd/256.0 for hd in hd_per_round]
cross_round = next((i for i, v in enumerate(norm_hd) if v >= 0.35), None)
# 2) Heatmap of schedule bit differences
mat = schedule_bit_diff_matrix(W1, W2)
# Print some summary metrics
print("Baseline message (hex):", baseline.hex())
print("Flipped message (hex):", flipped.hex())
print("Initial-state Hamming distance (round 0):", hd_per_round[0])
print("Peak Hamming distance:", max(hd_per_round), "of 256 bits")
print("Round of first H>=0.35 crossing:", cross_round)
print("Rounds total:", len(hd_per_round)-1)
# Plot 1: Hamming distance per round
plt.figure(figsize=(8, 4))
plt.plot(range(len(hd_per_round)), hd_per_round)
plt.title("State Hamming Distance vs Round (Baseline vs 1-bit flip)")
plt.xlabel("Round (0..64)")
plt.ylabel("Hamming Distance (0..256)")
plt.tight_layout()
plt.show()----------- Page112 ------------
# Plot 2: Heatmap of message schedule bit differences
plt.figure(figsize=(8, 6))
plt.imshow(mat, aspect='auto')
plt.title("Message Schedule Bit Differences (Rows=W[0..63], Cols=bits MSB→LSB)")
plt.xlabel("Bit index (MSB→LSB)")
plt.ylabel("W index (0..63)")
plt.colorbar()
plt.tight_layout()
plt.show()----------- Page113 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page114 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page115 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page116 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page117 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")----------- Page118 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page119 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page120 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page121 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page122 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")----------- Page123 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page124 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page125 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page126 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page127 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")----------- Page128 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page129 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page130 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page131 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page132 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")----------- Page133 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page134 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page135 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page136 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page137 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")----------- Page138 ------------
Conversation URL:
https://chatgpt.com/c/68a485d1-17a4-8322-a73d-750c0ba22cb8
Title:
Prompt:
# Re-run after state reset (the previous environment was cleared).
import numpy as np
import math
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user
def pi_hex_digits(n: int) -> np.ndarray:
getcontext().prec = max(40, 4*n + 30)----------- Page139 ------------
s = Decimal(0)
one = Decimal(1)
for k in range(n + 16):
k8 = 8*k
term = (Decimal(4)/(k8+1) - Decimal(2)/(k8+4)
- Decimal(1)/(k8+5) - Decimal(1)/(k8+6))
s += (one/(Decimal(16)**k)) * term
frac = s - int(s)
out = []
for _ in range(n):
frac *= 16
d = int(frac); frac -= d
out.append(d)
return np.array(out, dtype=np.int16)
def build_bytes_and_digits(nibbles: np.ndarray):
if len(nibbles) % 2 == 1:
nibbles = nibbles[:-1]
hi = nibbles[0::2]
lo = nibbles[1::2]
bytes_arr = (hi.astype(np.int32) << 4) + lo.astype(np.int32)
heads = []
tails = []
for b in bytes_arr:
s = str(int(b))
head = int(s[0]) if len(s) > 1 else 0
tail = int(s[-1])
heads.append(head)
tails.append(tail)
return bytes_arr.astype(np.int32), np.array(heads, dtype=np.int16), np.array(tails, dtype=np.int16)
def grid_counts(x_vals, x_bins, y_vals, y_bins):
H = np.zeros((x_bins, y_bins), dtype=np.int32)
for x, y in zip(x_vals, y_vals):
if 0 <= x < x_bins and 0 <= y < y_bins:
H[x, y] += 1----------- Page140 ------------
return H
def entropy_from_counts(counts: np.ndarray):
total = counts.sum()
if total == 0:
return 0.0
p = counts / total
p_flat = p.flatten()
p_nz = p_flat[p_flat > 0]
H = -np.sum(p_nz * np.log2(p_nz))
return float(H)
def mutual_information(joint: np.ndarray):
total = joint.sum()
if total == 0:
return 0.0
Pxy = joint / total
Px = Pxy.sum(axis=1, keepdims=True)
Py = Pxy.sum(axis=0, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
ratio = np.where((Px*Py) > 0, Pxy / (Px @ Py), 1.0)
log_term = np.where(Pxy > 0, np.log2(ratio), 0.0)
I = float(np.sum(Pxy * log_term))
return I
def report_space(name, counts, x_label, y_label):
total_pairs = int(counts.sum())
unique_cells = int((counts > 0).sum())
grid_size = counts.size
unique_ratio = unique_cells / grid_size if grid_size else 0.0
H_joint = entropy_from_counts(counts)
H_x = entropy_from_counts(counts.sum(axis=1, keepdims=True))
H_y = entropy_from_counts(counts.sum(axis=0, keepdims=True))
Ixy = mutual_information(counts)
df_stats = pd.DataFrame([{
"space": name,----------- Page141 ------------
"total_pairs": total_pairs,
"unique_cells": unique_cells,
"grid_size": grid_size,
"unique_ratio_%": round(unique_ratio*100, 2),
"H_x": round(H_x, 4),
"H_y": round(H_y, 4),
"H_joint": round(H_joint, 4),
"I(X;Y)": round(Ixy, 4),
}])
return df_stats
def plot_heatmap(matrix, title, xlabel, ylabel):
plt.figure()
plt.imshow(matrix.T, origin='lower', aspect='auto')
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.colorbar()
plt.show()
def delta_uniform(matrix):
total = matrix.sum()
if total == 0:
return matrix.astype(float)
expected = total / matrix.size
return matrix.astype(float) - expected
# Build data
N_NIBBLES = 4096
nibs = pi_hex_digits(N_NIBBLES)
bytes_arr, heads, tails = build_bytes_and_digits(nibs)
H_t = heads[:-1]; H_t1 = heads[1:]
T_t = tails[:-1]; T_t1 = tails[1:]
N_t = nibs[:-1]; N_t1 = nibs[1:]----------- Page142 ------------
# Spaces
xor_s1 = (H_t ^ H_t1).astype(np.int16)
avg_s1 = ((T_t + T_t1) // 2).astype(np.int16)
counts_s1 = grid_counts(xor_s1, 16, avg_s1, 10)
xor_s2 = (H_t ^ T_t1).astype(np.int16)
avg_s2 = ((T_t + H_t1) // 2).astype(np.int16)
counts_s2 = grid_counts(xor_s2, 16, avg_s2, 10)
xor_s3 = (N_t ^ N_t1).astype(np.int16)
avg_s3 = (((N_t + N_t1) // 2)).astype(np.int16)
counts_s3 = grid_counts(xor_s3, 16, avg_s3, 16)
stats = pd.concat([
report_space("S1: XOR(H,H1) vs AVG(T,T1)", counts_s1, "XOR(H,H1)", "AVG(T,T1)"),
report_space("S2: XOR(H,T1) vs AVG(T,H1)", counts_s2, "XOR(H,T1)", "AVG(T,H1)"),
report_space("S3: XOR(N,N1) vs AVG(N,N1)", counts_s3, "XOR(N,N1)", "AVG(N,N1)"),
], ignore_index=True)
display_dataframe_to_user("XOR+AVG uniqueness & entropy (π, BBP stream)", stats)
# Plots
plot_heatmap(counts_s1, "S1 counts: XOR(H,H1) vs AVG(T,T1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s1), "S1 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s2, "S2 counts: XOR(H,T1) vs AVG(T,H1)", "XOR 0..15", "AVG 0..9")
plot_heatmap(delta_uniform(counts_s2), "S2 delta from uniform", "XOR 0..15", "AVG 0..9")
plot_heatmap(counts_s3, "S3 counts: XOR(N,N1) vs AVG(N,N1)", "XOR 0..15", "AVG 0..15")
plot_heatmap(delta_uniform(counts_s3), "S3 delta from uniform", "XOR 0..15", "AVG 0..15")
```
