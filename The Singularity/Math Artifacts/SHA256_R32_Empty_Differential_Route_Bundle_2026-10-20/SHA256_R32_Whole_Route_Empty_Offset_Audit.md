# Whole-route SHA-256 ring offset audit

## Ring execution and the folded medallion

Each source case is compared to the empty-message SHA-256 route at matching typed coordinates: schedule index, round index/register, boolean operation/input, arithmetic operation/operand/result/carry mask, and feed-forward word. The baseline is not merely the final empty digest; the same-route empty execution is the other side of the medallion across the entire route.

For each pair `(v,e)`, the run keeps both `delta=(v-e) mod 2^32` and `xor=v XOR e`. Each is immediately re-addressed in R32. For its point and each offset, the file records half-ring address, side bit, reflected partner address, residual, root, continuation depth, and outer-to-inner frame/provider chain. The round and operation labels are never dropped.

## Result

- Offset rows: 25240.
- Counts by typed view: `{'schedule': 320, 'round': 8000, 'addition': 12000, 'boolean': 4800, 'feedforward': 120}`.
- Counts by source case: `{'Q': 5048, 'GO': 5048, 'OK': 5048, 'CAT': 5048, 'NEXUS': 5048}`.
- Route keys that failed to align with empty baseline: 0.
- Every offset’s reflected partner law passes: True.
- Combined radial-reader records for K/H0 and digest/offset words: 6912.

## Reading the result

The two half-rings are represented by the fold coordinate plus side; the partner relation reconstructs the opposite side. Outer-frame ancestry records the route inward. This implements the paper’s fold-first address discipline without materializing R32. The empty hash is used as a route baseline at every corresponding stage, making the difference path explicit instead of looking only at final digest values.

This is an exact coordinate transformation and matched-route audit, not yet a proof that digest offsets determine an unknown source. Any such selector must preserve round-indexed K_t, W_t, carry/borrow fields, and source-fiber location.

## Files

- `SHA256_R32_Whole_Route_Empty_Offsets.csv` — every matched target-vs-empty value and both offsets, with folded-ring and ancestry coordinates.
- `SHA256_R32_All_Radial_Ring_Reads.csv` — constant, IV, digest, empty-digest, and offset readouts across ring scales.
- `SHA256_R32_Whole_Route_Empty_Offset_Summary.json` — checks and hashes.
- `SHA256_R32_Empty_Medallion_Audit.md` — empty hash, digest medallion offset, and all empty-message route files.


## Fold reconstruction check

- Checked `100,960` half-ring-plus-side reconstructions across observed values, empty-route baseline values, modular offsets, and XOR offsets; failures: `0`.
- Outer-frame/provider ancestry is retained for each difference value. A `00` or `11` frame continues inward; `01`/`10` decide the provider immediately. This makes the two-end rule recursive: the ends of each layer route to the next layer or the root.
- SHA constants remain in round order `K_0`…`K_63`. The half-ring fold gives the other side of each constant, but the two endpoint constants alone are not asserted to generate the intervening K values.
- `SHA256_R32_Empty_Digest_Offset_Overview.csv` condenses each test digest against the empty digest into concatenated big-endian words, preserving wordwise modular offsets and wordwise XOR offsets separately.
