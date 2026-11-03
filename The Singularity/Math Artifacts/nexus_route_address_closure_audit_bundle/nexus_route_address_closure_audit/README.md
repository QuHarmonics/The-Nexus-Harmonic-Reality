# NEXUS Route–Address Closure Cross-Bundle Audit

## Result

The bridge check passes. Two separately implemented route/address paths agree on every word at widths 2–12 (8,188 total). Physical positions form a permutation at every checked width, and partner addresses obey `pos(P(x)) = 2^n - 1 - pos(x)`. Every within-weight-band rank set is exactly `0..binom(n,w)-1` across all 2,046 words at widths 1–10, covering 65 weight bands.

The two included sealed scripts also match their recorded SHA-256 seals:

- Route/rank audit: `ee827844ba91d592c81cb1f6f22f42dc0a2ea97820a3d532e199d6e30803020b`
- Reflection/lift audit: `4277c3f1b18df45ab669f00f75e33596458216d31573983dcec1e2269e607d8f`

The reflection/lift audit was rerun successfully in the authoring session. Its reported checks cover 2,097,148 words across widths 2–20, 228 weight bands, 699,048 cases for each of the three covariance identities, 699,048 E/G outputs, pole queries through source width 4,096, and two 255-step digest routes. The route/rank audit also reran successfully in the authoring session.

## Reproduce the bridge check

Run from this directory:

```bash
python nexus_closure_cross_bundle_audit.py
```

The script verifies the two source seals, cross-compares the independent route and position implementations, checks partner reflection, and validates the exact within-band rank sets. Results are written to `nexus_closure_cross_bundle_audit_results.json`.

## Boundary of the result

This closes the tested discrete chain `route ↔ word ↔ canonical rank ↔ physical ring address`, including the separate partner-side bit and center swap. The sphere coordinates remain an exact embedding chosen for the combinatorial system; these checks do not independently establish physical spin-½ dynamics.

The `two_branch` proof and source are explicitly an unsealed independent audit. The two SHA-256 matches establish that the included files match the included seal values; they do not provide an external signature or prove who produced a file.
