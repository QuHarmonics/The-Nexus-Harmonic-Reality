# Audit of the reflected BBP compiler

## Independent output checks

Using an independent high-precision calculation of pi (mpmath, 4000 decimal digits), I computed the first 2400 hexadecimal fractional digits and compared them with the uploaded programs' output.

- `pi_compiled_from_4_runs.py 2000`: emitted 2000 hexadecimal digits beginning at offset n=3. All 2000 matched the independent reference segment at offsets 3 through 2002.
- `pi_compiled.py 1024`: emitted 1024 hexadecimal digits beginning at offset n=255. All 1024 matched the independent reference segment at offsets 255 through 1278.
- `pi_compiled_from_empty.py 2000` (the no-preloaded-state variant added for this audit): spawned the four n=0 lanes before its first read, then advanced and spawned on every step. All 2000 output digits matched the independent reference from offset n=0.

Reference prefix: `243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89`.

## What `reflect.py` establishes

It records the active BBP lane keys, denominators, residues and weights. Within its declared candidate family `v' = (a*v+b) mod d`, with `a in 0..255` and `b in 0..15`, it finds the unique fit `(16,0)` across 130,560 observed transitions. The observed spawn denominators fit `d=8n+j` for j in {1,4,5,6}; newly born residues equal `1 mod d`; weights remain `{1:4,4:-2,5:-1,6:-1}`. Four runs are enough to pin down the parameters within these model classes, and later observed runs test those fits.

This is a genuine runtime-reflection experiment, but uniqueness is relative to the chosen candidate families and structural model. A finite trace cannot establish uniqueness among every possible mathematical rule.

## Scope qualification: what is and isn't removed

The emitted programs do not call the original `bbp()` function and do not use modular exponentiation for already-active lanes. Those lanes advance by `v = 16*v mod d`.

However, the `read()` function still evaluates a fixed-point approximation to the contribution of unopened future lanes using terms of the form `16^-h / (8*(n+h)+j)`, with an error allowance. That is BBP-tail structure, expressed as a continuation rule. So “no BBP in it” is accurate only in the narrower sense of no original BBP digit-extraction routine/modular-power loop; it is not a formula-free or tail-free generator.

The supplied four-run program is also not literally empty-state: it starts at n=3 with 16 preloaded lane states. The added `pi_compiled_from_empty.py` removes that initial lane preload by spawning the n=0 lanes before the first read. It still retains the same analytical tail rule for not-yet-spawned lanes.

## Remaining test

To get a stricter motion-only engine, replace the analytical tail evaluation with explicit future-lane state / interval certification, and show that the same local transition plus spawn rules produce every digit without evaluating the BBP tail expression directly. That would test whether the motion ledger itself contains sufficient operational state, rather than relying on a formula for the unresolved tail.
