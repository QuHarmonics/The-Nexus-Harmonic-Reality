# NEXUS reverse-the-gap execution — 2026-10-16

Seal SHA-256: `f7e479f4e8a76d4e50d5817caed4398b933c05f3b72598ed074a6ca7fb913eb4`
Scope: algebraic/representation checks only; no candidate scans and no new datasets. Known orbital ordering is route-back data, not a blind landing.

## Gap 1 — orientation reader

**RUNS** for the angular-momentum representation. Generated ℓ=0…12 by terminating only when the lowering coefficient is zero; 156 directed ladder edges; every return check passed. Generated `2ℓ+1` offsets for every case and verified capacities `2n²` for n=1…20 after applying the physical spin doublet.

The angular ladder owns `2ℓ+1`; physical spin-½ supplies a separate two-state factor. Identifying those two physical spin states with NEXUS “two readings” remains a mapping, not a consequence of the count.

## Gap 2 — channel magnitude

**OPEN**, now typed. The map `(S,V) -> Σ=S+V` has rank 1 for two unknown channel fields and null direction `(1,-1)`. Adding `Δ=V-S` gives an invertible map with `S=(Σ-Δ)/2`, `V=(Σ+Δ)/2`. For `Σ=-55 MeV`, these equations give an entire symbolic family indexed by `Δ`, not one scale.

The wrapper that can own the scale is the scalar/vector field model: couplings, scalar/vector source densities, field equations (including nonlinear terms if present), finite-nucleus profiles, boundary conditions, and calibration. The linear uniform-matter form was written symbolically; no arbitrary parameters or candidate Δ values were scanned. The exact finite-nucleus profile used for the target `Σ(r)` remains unbound without that model specification.

## Gap 3 — order inside the copy above 82

**DEAD END** for “`1h9/2` is the next top-j gate.” Type check: `1h9/2` has `j=ℓ−1/2`; the h top-j orbital is `1h11/2`. The pair map gives `2f7/2` (`n_r=1, ℓ=3`) ↔ `1h9/2` (`n_r=0, ℓ=5`). Both have pseudo-ℓ 4; `2f7/2` is pseudo-anti-aligned and `1h9/2` pseudo-aligned. Therefore anti-aligned-first predicts `2f7/2` then `1h9/2`, whereas the already-recorded order is the reverse. This is a pair-splitting/order gap, not an h top-j count gap.

The correct owning link is the radial pseudospin-splitting term associated with the gradient of `Σ(r)=V(r)+S(r)`, evaluated for both states in one fully specified nuclear wrapper. The current material does not provide a runnable complete potential profile for that signed pair-energy calculation, so the order stays **OPEN**; the observed order is not counted as a prediction.

## Composite ledger

- Orientation fibre `2ℓ+1`: **RUNS**; spin-readings identification remains a mapping.
- Magnitude of `Δ`: **OPEN**; owner named as interaction wrapper, not a scalar value search.
- Copy order above 82: **OPEN**; owner named as nuclear pseudospin-splitting/level-energy route. The h-top-j ownership is a **DEAD END**.
