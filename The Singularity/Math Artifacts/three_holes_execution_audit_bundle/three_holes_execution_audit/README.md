# Three-hole execution audit — 2026-10-20

## Executive outcome

- **Hole 1, ring-coordinate latitude spectrum:** the corrected block formula and palindrome-carrier formula reproduce every coefficient of direct unnormalized Walsh transforms for widths 2–12 (8,188 body coefficients and 8,188 carrier coefficients). Direct transform measurements through width 20 reproduce the stored energy shares and 1,036,432 active full-spectrum masks at n=20. The block-sum formula has been run as a finite evaluator; no optimized O(wt(K)) implementation of each reversal-ordered inner sum is claimed.
- **Hole 2C, radial certificate angle:** the offset arithmetic is exact and passed 1,554 checks for D=13..96. The single-angle profile claim does **not** hold for every D: all tested D congruent to 0 or 1 mod 3 passed, while only 6/28 tested D congruent to 2 mod 3 passed. The first failure is D=14, L=12, address 2052, slice 4, word `111101001111`: observed 0, expected 1. Thus this candidate angle is not a general certificate for the whole target family. This does not prove that no different certificate exists.
- **Hole 3, SHA schedule-tail pruning:** the certificate is formally specified as an intersection, but the supplied files do not contain `cofactor_inverse_bdd.py` or a runnable ROBDD API. No executable pruning, equivalence check, or node-count reduction was performed. Its implementation status remains OPEN.

## Hole 1 — formula and measurements

Let `E_n(i)=(z_n(i)+z_n(N-1-i))/2`. It is zero at palindrome sites and equals the latitude at nonpalindrome sites. The complete block reconstruction retains every local slot and uses `eta_K(i)=1[r_i<K]`, so a palindrome slot is kept in place but masked to zero.

For even n=2h, H=2^h, e_K=1[K>=H/2], S_K=K+e_K and D_K=K(K-1)/2+max(0,K-H/2). The within-block labels r_i are 0..S_K-1 in increasing h-bit-reversal order. For each K and local i, the twice-latitude contribution is `v2=2*(h-popcount(K)-popcount(r_i))` if r_i<K, else zero; for odd n=2h+1 it is `v2=2h-1+2*mu-2*popcount(K)-2*popcount(r_i)` for each `mu in (1,0)`, again masked by r_i<K. The corresponding q offsets are `D_K+i` for even width and `2D_K+(1-mu)S_K+i` for odd width. These are summed with the exact low-address Walsh character and the seam sign. The computed predictions matched the direct transform coefficient-by-coefficient at n=2..12.

| n | Degree-2 / full latitude energy | Degree-2 / body energy | Degree-1 / full energy | Active full modes |
|---:|---:|---:|---:|---:|
| 6 | 53.1250% | 70.8333% | 4.6875000% | 53 |
| 8 | 55.9937% | 63.9927% | 0.7812500% | 211 |
| 10 | 51.9287% | 55.3906% | 0.1635742% | 954 |
| 12 | 46.7403% | 48.2481% | 0.0361125% | 3,808 |
| 16 | 38.9498% | 39.2565% | 0.0016417% | 63,806 |
| 20 | 32.7503% | 32.8144% | 0.0000822% | 1,036,432 |

Additional exact outcomes: at n=12 the degree-one full-latitude share is 0.0361124674%; at n=20, 1,036,432 of 1,048,576 full-spectrum coefficients are nonzero. The degree-two/full-energy values round to the previously reported 53.1250%, 55.9937%, 51.9287%, 46.7403%, 38.9498%, and 32.7503% at widths 6, 8, 10, 12, 16, and 20, respectively.

The finite data support degree-two as the largest degree bin at the tested widths 4–20, but not as a majority of total energy at widths 12 and 20. The claim that a continuum quadratic phase causes the concentration remains an interpretation, not a consequence of these finite coefficient checks alone.

## Hole 2C — exact offset and actual target replay

For `p=floor(2D/3)+1` and `u_D=1/2 + 2^(-p) + (2/3)2^(-(D-1))`, the exact center-out offset for L>=p is

`q_L=floor(2^L(u_D-1/2)) = 2^(L-p) + floor((2/3)2^(L-D+1))`.

That arithmetic passed 1,554 exact Fraction checks. It is weaker than the target-language claim: a correct offset does not by itself imply that the selected ring-word bit equals the requested q_D bit.

| D mod 3 | D tested | Entire profiles matched | Slice comparisons / matches | First mismatch |
|---:|---:|---:|---:|---|
| 1 | 28 | 28/28 | 1,498/1,498 | none |
| 2 | 28 | 6/28 | 1,499/1,526 | D=14, L=12, addr=2052, bit 0 != 1 |
| 0 | 28 | 28/28 | 1,554/1,554 | none |

Across D=13..96, 84 profiles and 4,578 slices were tested. 27 slices mismatch, across 22 depths. The full failure rows are in `results/radial_profile_failures.csv`. The `A(q_D)` support-union idea can still be expressed as an intersection of slice preimages, but a closed certificate for all target depths has not been established by this candidate angle.

## Hole 3 — schedule-tail region binding contract

The only supported formal object in the supplied material is

`C(H) = {a in R_512 : TailValid(a) AND PadValid(a) AND DigestClosure(a)}`.

This gives a well-typed *specification* of the residual region, not an executed ROBDD prune. The expected wiring is to conjoin (1) the backward SHA schedule-tail relation / bijective tail constraints, (2) padding validity, and (3) the digest closure predicates in the same variable manager and ordering, then cofactor the conjunction by ring-address regions. To claim `RUNS`, the implementation must demonstrate equivalence to the original valid-message predicate, preserve every valid assignment, and report node counts under the same ordering before and after pruning.

The uploaded certificate archive contains matrix/certificate tables and a character lab, but no `cofactor_inverse_bdd.py`, ROBDD variable schema, SHA schedule constraint implementation, PadValid node, or digest-closure API. A recursive filename scan of the available ZIP archives, including nested ZIP entries, also found no matching runnable provider names; this is an availability check, not proof that a differently named implementation cannot exist. Therefore no code was invented to mimic those missing dependencies. The status remains **BOUND as a named set; wiring OPEN**.

## Provenance

Prediction SHA-256 (literal bytes): `e2f4b03aed0841db2a97e203cfdae7caa2980ebd2136368489af36546bd9ae03`.
Audit-source SHA-256 before and after: `ebe53dd8067611c171f9e6d8bfc2dcafbe56e475c1199cc06a2f435f648a9d65`.
The literal-byte source and prediction hashes matched after execution. The audit uses exact integer/rational arithmetic for formulas and radial offsets; direct Walsh transforms are unnormalized integer FWHTs. Hole 1 formula comparison was exhaustive for all coefficients at n=2..12; full-energy spectra were directly measured at all widths n=2..20.

## Ledger update

- Hole 1 corrected body and carrier block formulas: **SEALED, RUNS** for coefficients n=2..12; measured spectral energy through n=20. Optimized reversal-order-sum evaluator remains OPEN.
- Degree-two concentration: **RUNS as a finite measured statistic**; continuum/quantum explanation remains **PULL/OPEN**.
- Hole 2C offset equation: **SEALED, RUNS** over 1,554 exact checks. Target certificate angle: **DEAD END as a universal witness** for the stated q_D family; failures are explicit. General A(q_D) support reduction and non-regularity proof remain OPEN unless supplied independently.
- Hole 3 certificate: **BOUND as a formal intersection**; ROBDD wiring and pruning measurements **OPEN** because implementation providers are absent.
- Holes 4 and 5: unchanged OPEN/PULL.
