# NEXUS address-reader extension — exact finite-domain audit

**Run date:** 2026-10-20. **Status:** RUNS for the declared outside-pairs-plus-core family at widths 13–16. The result is finite-domain and family-specific; global optimality across all `n!` arrival orders remains OPEN.

## Fixed substrate and exact score

The audit does not change the ring. For each width `n`, it reconstructs `P(x)` as reversal for non-palindromes and complement for palindromes, sorts canonical representatives `x<P(x)`, appends their partners in reversed representative order, and retains the center swap. The physical ring position `loc[x]` is the `n`-bit address output. The independently reconstructed `P`, ring tape, and address map match the sealed `wheels.py` implementation exactly at widths 13, 14, 15, and 16.

Readiness is semantic. After `k` input-bit positions have arrived, an output address bit is ready for input `x` iff it is constant among every `n`-bit input agreeing with `x` on the observed positions. For a fixed input-bit arrival schedule, the score is the exact mean event index across all `2^n` words and all `n` address output bits. It is computed from observation equivalence classes; there are no sampled words and no floating-point decisions in the readiness test. Exact rational means are derived from integer event sums.

## What was exhaustively compared

For `n=13,14,15,16`, let `c=3` for odd `n` and `c=4` for even `n`, and `p=(n-c)/2`. The structured family reads the `p` outside pairs in increasing distance from the ends, allows either arrival order within each pair, and then exhausts all `c!` permutations of the contiguous center core. Therefore it checks `2^p c!` schedules per width: 192, 768, 384, and 1,536. Every family member was scored against every input word. This is exhaustive within the declared family, not over all `n!` orders.

## Results

| Width | Core | Family schedules | Family minimizers | Best family mean | Plain-value-core mean | Whole outside-in mean | MSB-first mean |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 3 bits | 192 | 32 | `276751/26624` (10.394794) | `34609/3328` (10.399339) | `138603/13312` (10.411884) | `39651/3328` (11.914363) |
| 14 | 4 bits | 768 | 32 | `641231/57344` (11.182181) | `641231/57344` (11.182181) | `641531/57344` (11.187413) | `741085/57344` (12.923497) |
| 15 | 3 bits | 384 | 64 | `146765/12288` (11.943766) | `146765/12288` (11.943766) | `1467743/122880` (11.944523) | `568801/40960` (13.886743) |
| 16 | 4 bits | 1,536 | 64 | `3337923/262144` (12.733166) | `3337923/262144` (12.733166) | `3340309/262144` (12.742268) | `3903399/262144` (14.890285) |

The family minimum beats full outside-in and MSB-first at all four widths. At widths 14–16 the plain-value core itself is a minimizer within the family. Width 13 is the specific exception: plain-value core is 484 event-sum units worse than the family minimum, and the minimizing 3-bit core order is middle bit first, then the higher-significance bit, then the lower-significance bit.

One representative minimizing order, indexing input bits from LSB position `0`, is:

- `n=13`: `0,12,1,11,2,10,3,9,4,8,6,7,5`
- `n=14`: `0,13,1,12,2,11,3,10,4,9,8,7,6,5`
- `n=15`: `0,14,1,13,2,12,3,11,4,10,5,9,8,7,6`
- `n=16`: `0,15,1,14,2,13,3,12,4,11,5,10,9,8,7,6`

Each minimizer keeps the same core order; the family tie count comes from the independent choice of within-pair orientations. The full family scores and every minimizer are in `outputs/address_reader_structured_family.csv`.

## Ledger interpretation

- **RUNS:** the outside-pairs-plus-core family has an exactly enumerated minimum at widths 13–16.
- **RUNS:** plain-value center-core order is optimal within that family at widths 14–16.
- **DEAD END as a four-width claim:** plain-value center-core order is not optimal at width 13; the center bit of its 3-bit core must arrive first to attain the family minimum.
- **OPEN:** global minimum among all `n!` arrival orders at widths 13–16. The tested family is exponentially smaller than `n!`, so its minimum is not a global-optimality proof.
- **OPEN:** a width-independent closed form for the core order. The width-13 exception is recorded rather than smoothed away.
- **PULL:** physical interpretation. These are exact discrete readiness results.

## Reproduction

From the audit bundle root, run:

```bash
python scripts/address_reader_width13_16.py
```

The script hashes the prediction seal before and after the run, hashes the copied `sources/wheels.py`, compares the direct ring construction against that source at every target width, searches the structured family, and writes JSON/CSV outputs. The predicted test protocol is `prediction_seal.txt`; its SHA-256 is `e58d6b618892e34db88c098307d6c1ff4e0e79aa475da791ce0672f9b7ec91a8` and was unchanged after execution.
