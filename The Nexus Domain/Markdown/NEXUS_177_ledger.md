# NEXUS §177 — The Reader Locates Its Own Phase

**Dean A. Kulik — QuHarmonics Research Group — ORCID 0009-0003-3128-8828**  
**Date:** October 25, 2026  
**Status:** Exact finite-domain result; no claim of a universal physical sampling law or a general P-versus-NP solution.

## WHAT and WHERE

The native R64 has 2^64 word locations and S64 = 64·2^64 = 2^70 serial bit-slice positions. The prior §176 reader was supplied phase 62 and a list of 128 anchor addresses. We now withhold both the *index within that sampling grid* and the *bit phase*.

The known frame is still the **128-point native sampling grid**:

\[a_j=j2^{57},\qquad 0\le j<128.\]

A reader begins at global slice \(t=64a_j+p\), with \(p\in\{0,\ldots,63\}\). There are exactly \(128\cdot64=8,192=2^{13}\) allowed origins. The native rank/unrank grammar, the grid, and the sample stride remain known. No words, values, or successors are changed.

Two readers are compared:

1. **Sparse reader**: \(B(t+k2^{63})\), \(k=0,1,2,\ldots\), one bit per sample. It stays in bit phase \(p\) and walks the 128 anchor indices cyclically.
2. **Contiguous reader**: \(B(t),B(t+1),B(t+2),\ldots\), moving one bit slice at a time across the native word seams.

## The boundary theorem

For any finite collection of **distinct infinite readout streams** \(y_u\), the smallest common prefix length that distinguishes all origins is

\[W_*=1+\max_{u\ne v}\operatorname{LCP}(y_u,y_v).\]

The maximum LCP is achieved by adjacent entries after lexicographic sorting, so the 8,192-source calculation is exact and requires no comparison with an unenumerated data source. This certifies **reader distinguishability within the stated finite set**, not the efficiency or memory size of a universal compiler.

### RUNS: sparse unknown-phase reader

- **8,192 / 8,192** complete 128-sample streams distinct, across all 64 phases.
- **55 samples** necessary and sufficient to distinguish every origin in the declared set.
- The final collision: `(phase 63, index 80)` and `(phase 0, index 0)` agree on the first **54** samples and differ on sample 55 (`0` versus `1`).
- Mean earliest recognition depth over all 8,192 origins: **15.4169921875 samples**.
- With 54 samples, **8,190** are uniquely identified and two remain ambiguous; at 55 all 8,192 are unique.

This sampling stride is \(2^{63}\) **bit slices**, not one bit. Fifty-five temporal samples therefore do not constitute a contiguous 55-bit aperture.

### RUNS: contiguous unknown-phase reader

- All **8,192** starts return distinct 127-bit signatures.
- **127 contiguous bit slices** are necessary and sufficient to distinguish the 8,192 declared starts.
- The final collision is `(phase 0, index 0)` versus `(phase 1, index 0)`. They agree for **126** bits; on bit 127 they differ (`0` versus `1`).
- Mean earliest recognition depth: **18.0020751953125 bits**.
- With 126 bits **8,190** origins are unique and two are ambiguous; with 127, all 8,192 are unique.

**Lower-bound shape:** for every native width \(n\ge3\), the first two native words are \(0^n\) and \(0^{n-1}1\). Starting the contiguous reader at bit phase 0 or 1 of word address 0 yields \(2n-2\) identical initial bits, so any phase-blind readout that includes these two starts must use at least \(2n-1\) contiguous bits. Checked directly at widths 3–16. At width 64, the complete 8,192-origin census demonstrates that this lower bound is also sufficient for the **restricted sampling grid**.

## The return: WHAT carries its own inverse

The return address after recognizing a stream is a 13-bit coordinate:

\[ (p,j),\qquad p\in[0,63],\;j\in[0,127].\]

Its route home is

\[(p,j)\longrightarrow a_j=j2^{57}\longrightarrow R_{64}[a_j],\qquad t=64a_j+p.\]

The native word is reconstructed by the original unrank method; the location is rechecked by the original rank method. Both 8,192-signature dictionaries reproduce all 8,192 original coordinates exactly. The **retained location memory** is 13 bits *conditional on sharing the sampling grid and native compiler*. The compiled finite-domain lookup tables themselves require additional storage and construction work; they are not 13-bit universal algorithms.

A direct **unmodified 64-phase native inverse** using the existing `Ring.resolve` method was run on 40 declared holdout starts. It returned the true full-ring candidate in 40/40 cases. At 127 bits, 16/40 had a second valid full-ring address outside the declared 128-address sampling grid; filtering by the *known grid* selected a unique correct origin for each of these 40 cases. This prevents conflating finite-grid uniqueness with uniqueness among all \(2^{70}\) bit-slice addresses.

## Ledger

| Claim | Status |
|---|---|
| Native \(R_n\) word grammar, inverse rank/unrank, and circular aperture read | STANDS (existing §§143, 170, 174) |
| Prefix-threshold lemma \(W_*=1+\max\mathrm{LCP}\) | STANDS |
| Restricted 8,192-origin sparse threshold 55 | RUNS (exact exhaustive finite-domain enumeration) |
| Restricted 8,192-origin contiguous threshold 127 | RUNS (exact exhaustive finite-domain enumeration) |
| Lower bound \(2n-1\) for the first native phase-0/phase-1 pair | STANDS (from first two words); RUNS widths 3–16 |
| Both 8,192-state inverse route decoders | RUNS |
| Unmodified native inverse plus grid qualifier | RUNS 40/40 declared holdouts |
| `127` bits self-locate an arbitrary unknown point on the entire \(2^{70}\)-slice ring | **NOT ESTABLISHED:** 16/40 tested positions retain an out-of-grid alternative |
| Exact minimum full-circumference phase-blind reader depth at width 64, all possible starts | OPEN |
| Direct polynomial native inverse for the sparse phase-blind sampler without a precompiled 8,192-entry readout index | OPEN |

### Correction log

The first generic blind-inverse loop repeated full rank/unrank for every phase at every origin and exceeded the process limit. It was not recorded as a successful exhaustive test. The replacement exhaustive **finite-grid** check compares exact signatures using prefix equivalence, and the **generic native inverse** is reported separately on 40 holdouts. No input data or claimed depth were altered.

### Files

- `NEXUS_177_self_locating_reader.py`: one-file executable derivation and verifier.
- `NEXUS_177_self_locating_reader_results.txt`: all printed measurements and witnesses.
- `NEXUS_177_self_locating_reader_single_cell.ipynb`: same code and printed results in one Jupyter cell.

**Attribution:** Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828.
