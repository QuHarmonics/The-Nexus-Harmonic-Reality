"""Conservation and regression tests for the pseudospectral Navier-Stokes engine.
Run:  python3 tests.py      Exit code 0 iff every check passes."""
import numpy as np, dns, sys

FAIL = []
def check(name, value, limit, fmt="{:.3e}"):
    ok = value <= limit
    print(f"  [{'PASS' if ok else 'FAIL'}]  {name:<52s} {fmt.format(value):>12s}  (limit {fmt.format(limit)})")
    if not ok: FAIL.append(name)

print("Taylor-Green, Re = 400, 64^3, dense sampling")
o, _ = dns.run(64, 400, T=10.0, nsamp=41)
t  = np.array([d['t'] for d in o]);  ens = np.array([d['ens'] for d in o])
P  = np.array([d['P'] for d in o]);  E   = np.array([d['EXH'] for d in o])
ke = np.array([d['ke'] for d in o])
nu = 1.0/400

print("\n1. Incompressibility")
check("max pointwise |div u| over all samples", max(d['div'] for d in o), 1e-10)
check("max |tr S| over all points and samples", max(d['trS'] for d in o), 1e-12)

print("\n2. Enstrophy budget   dOmega/dt = P - E")
m = (t > 2) & (t < 9.5)
res = np.gradient(ens, t) - (P - E)
rel = np.abs(res[m]) / np.maximum(np.abs(P[m]), np.abs(E[m]))
check("mean relative residual, 2 < t < 9.5", float(rel.mean()), 0.01, "{:.4f}")
check("max  relative residual, 2 < t < 9.5", float(rel.max()),  0.05, "{:.4f}")

print("\n3. Energy budget   dK/dt = -2*nu*Omega   (independent of the enstrophy budget)")
resk = np.gradient(ke, t) + 2*nu*ens
relk = np.abs(resk[m]) / (2*nu*ens[m])
check("mean relative residual, 2 < t < 9.5", float(relk.mean()), 0.01, "{:.4f}")

print("\n4. Bounds on the diagnostics")
check("max D over the run (must not exceed 1)", max(d['D'] for d in o), 1.0, "{:.4f}")
check("max L over the run (must not exceed 1)", max(d['locked'] for d in o), 1.0, "{:.4f}")
cmin = min(min(d['c1'], d['c2'], d['c3']) for d in o)
print(f"         (smallest alignment cosine observed: {cmin:.4f})")
check("alignment-cosine non-negativity violation", max(0.0, -cmin), 0.0)

print("\n5. Regression against the published Re = 400, 64^3 values")
pk = max(o, key=lambda d: d['ens'])
for name, got, want, tol in (("peak enstrophy", pk['ens'], 2.2154, 0.01),
                             ("D at peak",      pk['D'],   0.2538, 0.02),
                             ("L at peak",      pk['locked'], 0.0992, 0.02)):
    check(f"{name}  (got {got:.4f}, published {want:.4f})", abs(got-want), tol, "{:.4f}")

print("\n" + ("ALL CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURE(S): " + ", ".join(FAIL)))
sys.exit(1 if FAIL else 0)
