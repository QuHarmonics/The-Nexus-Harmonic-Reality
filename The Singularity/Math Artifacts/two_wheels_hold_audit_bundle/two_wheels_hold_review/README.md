# Two-wheels hold audit — delivery bundle

This bundle continues §17 of the supplied compiler-rings log with §18: the hold is treated as one partner-pair cut statistic evaluated in different reading orders and in the ring-width tower.

## Main results

- Five orders exhaustively checked for widths 2–12 at all 40,995 prefixes.
- Address, sheet, and leading-side-bit E/G route-code orders have identical full profile `H(t)=min(t,2^n-t)` on the tested widths.
- Value/counter order matches the existing `Delta + palindrome tent` formula and W3 seam maximum at every prefix.
- The declared half-table pair-adjacent lift has `H(t)=t mod 2`, so no more than one pair is held open.
- Tower mirror: full profile `H_(L+k)(t)=t-2 C_(L-k)(ceil(t/2^k))` with C counting non-palindromic partner-side words below the cut. Exhaustive over L=2..16, k=1..L and every t=0..2^L: 1,966,215 rows, zero mismatches. 130,111 points had an additional independent direct counter-order comparison.

## Reproduce

Run from this folder:

```bash
python hold_order_audit.py
python export_tower_profile.py
```

The first script writes compact order summaries and the full 40,995-row order CSV, and checks all tower points. The second materializes every tower profile point into a compressed CSV. The script sources and prediction statement have pre-run SHA-256 seals in the bundle. `SHA256SUMS.txt` inventories all final artifacts.

## Operational definitions and caveats

`hold_three_locations.md` gives the proof sketches and exact order constructions. The “half-table index” by itself names a pair, so the word-level profile uses the explicit lift “representative, then partner.” The route code is sorted by its leading side bit followed by the canonical E/G route code. The sheet stream follows the exact W6 transformation in the supplied runner (reverse the complete bit tape, complement, then re-chunk into words).

The uploaded `two_wheels_bundle.zip` did not contain the Excel workbook file. Therefore this run replayed the sheet order from the supplied W6 source code but did not independently reopen the workbook or recheck its cached cells. The hold identities remain finite combinatorial results, not a claim about physical time; that interpretation remains PULL.

An exploratory probe was used to resolve the phrase “non-palindromic partners below the ceiling” into the explicit partner-side count C. The official prediction was then hashed before the final audit. During profile materialization, a first attempt exposed an indexing issue at the width-zero tower base; the base was corrected and the exporter resealed before the successful zero-mismatch run. These details are recorded in `execution_provenance.json`.
