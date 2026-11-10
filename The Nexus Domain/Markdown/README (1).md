# NEXUS palindrome half-width / Walsh review

## Result

**Discrete checks: PASS in the stated domains.** The half-word carrier is simple in its natural coordinates, while its placement in the full ring creates the higher-degree Walsh spectrum. The literal smaller-ring order does not survive extraction; the exact waveform survives only after the stated re-addressing.

## Independently reproduced checks

1. **Palindrome extraction/order:** At each width `n=2,...,20`, extracting palindromes from the original ring order and reading their first `ceil(n/2)` bits gives ascending binary order `0,...,2^m-1`. It equals the smaller ring order only at `n=2`.
2. **Re-addressing / scalar placement:** The post-run scalar address function `palindrome_halfword_address.py` was compared against every palindrome position in a materialized ring for widths 2–20: **4,090/4,090 passed**. A separate rank/location DP was also used for **122** spot checks across widths 2–20 and **40** prefix/seam checks at widths 63, 64, 127, 128, 255, 256, 511, 512, 1023, and 1024.
3. **Re-addressed latitude waveform:** The even/odd identities in the submitted proof passed at every width 2–20. In the ordinary latitude convention, `z_(2m)(B(R_m(j))) = 2 z_m(j)` and `z_(2m-1)(B(R_m(j))) = 2 z_m(j) + 1/2 - lastbit(R_m(j))`.
4. **Walsh parity split:** For every width 2–20, the even component has only even Walsh degrees and the palindrome-supported odd component has only odd Walsh degrees. The exact odd-energy fractions match the submitted formulas:
   - even `n`: `2^(1 - n/2)`;
   - odd `n=2h+1`: `(4h+1)/((2h+1) * 2^h)`.
5. **Compressed carrier:** In natural half-word coordinates the palindrome carrier has Walsh degree one only. In full ring-address coordinates it develops higher odd degrees; the degree sets are included in `results/main_audit_rerun_results.json`.
6. **Operator distinction:** For half-widths at least three, complementing a palindrome's half-word under the re-addressed coordinates is not the same permutation as applying the smaller ring's native partner map. The waveform identity therefore does not, by itself, imply unchanged Walsh-spectrum nesting.

## Provenance and scope limits

- The uploaded audit script's SHA-256 matches its `audit_source_sha256_before_run` seal: `1db03220e29a019e666b0a7d644e540a72c3a72acbdd48e3b487d9a23adbb3f5`.
- The uploaded ZIP omits `pairs_forced.py`, which the main audit script imports dynamically, and also omits the pre-run prediction file referenced by the stored prediction digest. The rerun therefore used the included `pairs_forced.py` compatibility adapter in this review bundle. That adapter reconstructs the described partner/canonical-face ordering and is explicitly **not** claimed to be the missing upstream source. The main audit's own in-array ring construction was also compared against this adapter through widths 1–10.
- The supplied scalar-placement code was derived after the main sealed run, according to the submitted proof. Its checks are reported separately from the main source seal.
- `OPEN 2`'s cusp/smoothness claim was not tested. No physical-spin or physical-sphere dynamics claim is established by these combinatorial tests.

## Reproduction

Use Python with NumPy installed. From this directory, run:

```bash
python palindrome_half_width_audit.py
python independent_placement_crosscheck.py
```

The first uses the included compatibility adapter; the second independently compares scalar placement against a constructed ring and a separate rank/location DP source in `sources/`.
