# Addressability cost — verified result

Companion to `addressability_cost.ipynb` (executed, zero errors). Written 2026-10-03.

## The structure

Reading local cell `n` of an infinite whole `X` in base `b` is three operations:

- **Fold** — each shifted term reduces to `a_k·b^n mod q_k`; unbounded accumulation becomes finite residue state.
- **Address** — `X → b^n·X` brings depth `n` to the phase boundary.
- **Boundary** — `dist(frac(b^n X), d/b)` decides whether the phase sits inside one cell.

## Verified

- **Direct addressing does not require base alignment.** Tested on `e = Σ1/k!`, which has no radix
  scale anywhere. Hex digits extract correctly to n=2000, fold = `16^n mod k!`.
- **Mismatched radix costs, it does not block.** Decimal digits of π extract directly from the
  *base-16* BBP series, verified at six addresses to n=1000. No prefix materialized.
- **Cost is modulus growth alone.** Measured doubling ratios n=500 → n=1000:
  - π BBP base 16, moduli `8k+j`, log-sized → 2.18 (≈ n log n), 47,958 bits at n=1000
  - e factorial, moduli `k!` → 3.61 (≈ n²), 952,035 bits
  - π under base 10, moduli carry `16^k` → 3.95 (≈ n²), 5,583,670 bits — 116× the aligned case
- **The boundary is not a bottleneck.** Guard digits needed follow `P(run ≥ r) = 2·16^-r`, matched
  over four orders of magnitude; mean 0.136 digits, worst case `O(log_b n)` over n addresses.

## Criterion that survived

Direct local readout exists when each term's contribution under the address shift reduces to a
residue whose modulus grows slowly enough to compute, and the tail contracts. **Alignment buys
exactly one thing: it removes the scale factor from the modulus** (exponential in k → logarithmic
in k). It does not make addressing possible; it makes it cheap.

Separation that matters: *representation-direct* (prefix never built — all three cases) vs
*resource-direct* (cost grows slowly in the address — aligned π only).

## Claims killed during this work

- "Representation action = address action inverse" is the mechanism — **refuted by e**, which has
  no such relation and works anyway. That was the π-specific instance.
- "Mismatched radix collapses direct addressing" — **refuted** by the base-10 π extraction.
- A false MISMATCH at every decimal address traced to off-by-one reference indexing
  (`frac(10^n π)` indexes `d[n]`, not `d[n-1]`), not to the method.

## Not established

- Normality of π. The leakage column is consistent with zero at N=20,000; nothing stronger.
- Whether `O(n log n)` is optimal, or which constants admit log-modulus folds.
- Any claim that this structure governs physical systems. Measured for three number
  representations and nothing else.

## Related

Leakage measurement (kept because it rules out a tempting wrong conclusion): π's hex stream and
the sum-bit stream of a balanced binary adder both leak nothing above the iid floor, while a
period-7 control leaks maximally **and** is trivially addressable. So leakage is not the axis.
