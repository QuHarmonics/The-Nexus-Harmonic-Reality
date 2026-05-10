# Nexus Boundary Validation Test Run

Generated: 2026-04-27 19:16:41

## Scope

This is a runnable validation pass for the addendum's minimum test stack:
primitive-domain logic, residence, weak-field gravity, sparsity harness, and SHA route/carry geometry.

This is not the full 10,000-ratio OBMT Sparsity Test because the canonical OBMT address map and curated dimensionless-ratio dataset were not available in machine-readable form.

## Summary

| test                             | pass   | detail                                                       |
|:---------------------------------|:-------|:-------------------------------------------------------------|
| Mark1 coupling identity          | True   | alpha diff=0.000e+00                                         |
| Residence separation             | True   | null commit=0.050, signal commit=1.000, effect ratio=8.8     |
| Boundary Gauss law               | True   | max rel err=2.375e-16                                        |
| Cut-density modifies outer field | True   | outer extra accel mean=0.094                                 |
| Sparsity harness executable      | True   | candidate expressions=17400, 6pi^5 ppm=-18.825, hits@20ppm=7 |
| SHA Sziklai identity             | True   | violations=0/32000                                           |
| SHA T2[0] anchor                 | True   | T2[0]=0x8909ae5                                              |
| SHA carry avalanche              | True   | HD mean=31.18, std=3.86                                      |

## Test 1 — Mark 1 Coupling Identity

$$
H = \frac{\pi}{9} = 0.349065850399
$$

$$
\alpha_\Gamma = \frac{H^2}{24} = \frac{\pi^2}{1944} = 0.005076956996
$$

Absolute identity error: `0.000e+00`.

## Test 2 — Residence Functional

Synthetic domain: annular boundary $\Gamma$ on a `64 x 64` lattice.

Weighted residence:

$$
\mathcal{S}_\Gamma[x] = \int_0^T w_\Gamma(x(t))\,dt
$$

with:

$$
w_\Gamma(x)=L_\Gamma(x)A_\Gamma(x)R_\Gamma(x)K_\Gamma(x).
$$

Threshold was derived from the null noise floor:

$$
\Theta_\Gamma = Q_{0.95}(\mathcal{S}_\Gamma^{null}) = 68.575474.
$$

Null mean residence: `19.127403`  
Boundary-signal mean residence: `168.802640`  
Null commit rate: `0.050`  
Boundary-signal commit rate: `1.000`  
Effect ratio: `8.83`

## Test 3 — Weak-Field Gravity and Boundary Gauss Law

Model:

$$
\rho_{eff}(r)=\rho_m(r)+\rho_*\frac{\pi^2}{1944}\chi_\Gamma^2(r).
$$

Boundary Gauss check:

$$
4\pi r^2 g(r) = 4\pi G M(<r).
$$

Max relative error: `2.375e-16`.

Matter-only outer velocity coefficient of variation: `0.1802`  
With cut-density outer velocity coefficient of variation: `0.1693`  
Mean outer extra acceleration fraction: `0.0941`

## Test 4 — Sparsity Harness

Target:

$$
\mu = \frac{m_p}{m_e} = 1836.152673426000.
$$

Candidate resonance:

$$
6\pi^5 = 1836.118108711688.
$$

Relative error:

$$
\frac{6\pi^5-\mu}{\mu} = -1.882453175707e-05
$$

PPM error: `-18.825`.

Expression-family candidates tested: `17400`.

Hit counts by log tolerance:

|   epsilon |   hits |
|----------:|-------:|
|    1e-06  |      0 |
|    5e-06  |      0 |
|    1e-05  |      0 |
|    2e-05  |      7 |
|    5e-05  |      8 |
|    0.0001 |      8 |

Top hits at 20 ppm saved in `sparsity_proton_electron_hits_20ppm.csv`.

## Test 5 — SHA-256 Route/Carry Geometry

Rounds checked:

$$
500\times64 = 32000.
$$

Sziklai identity:

$$
a_{i+1} - e_{i+1} \equiv T2_i - d_i \pmod{2^{32}}.
$$

Violations: `0`.

Universal first-round anchor:

$$
T2_0 = 0x8909ae5.
$$

NOP T2 carry signature: `0xde1a54568d60f7b6`  
NOP carry weight: `34/64`  
Random Hamming distance from NOP carry signature: mean `31.182`, std `3.861`.

## Files

- `results.json`
- `test_summary.csv`
- `residence_scores.csv`
- `closure_trace_density.npy`
- `gravity_spherical_profile.csv`
- `sparsity_proton_electron_hits_20ppm.csv`
- `sha_t2_carry_hd.csv`
