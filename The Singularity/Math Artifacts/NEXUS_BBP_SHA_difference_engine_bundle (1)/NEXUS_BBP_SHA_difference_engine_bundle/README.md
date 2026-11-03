# NEXUS §124 — BBP lanes and SHA-256 in difference coordinates

This bundle reproduces the latest run, built on the `compiler_space.py` difference stack and mixer fuse `(A,B) -> (A,A XOR B)`.

## Run

Place these files in one directory and run:

```bash
python nexus_bbp_sha_difference_engine.py
```

Python standard library only. The included `sha256_bidirectional_audit.py` is used as the independent SHA-256 reference.

## What is built

- A complete 16-input-bit difference table for the BBP four-lane weighted fold.
- Direct evaluation of its difference coefficients at the rational-ring lane addresses, then the actual right-to-left BBP column fold and Machin comparison.
- A separate exact run of the layer-local BBP carry `J_k(m)` recurrence so its owner and bound are not confused with the global column-normalization carry.
- Difference compilation of `Ch`, `Maj`, full-adder and full-subtractor truth tables; the recovered local operators drive the 32-bit SHA word transformations.
- A compiled SHA-256 round and its inverse; one complete block; 256 return routes; and difference tables at every round depth on an explicit `LEN=8` affine slice of the 256-bit chaining state.

The digest-only inverse and a minimum root observer remain OPEN. The route-back test retains the actual message schedule `W[t]` and constants `K[t]`; it does not claim otherwise.

`NEXUS_running_audit_addendum_124.md` records the run, including the carry-owner correction.
