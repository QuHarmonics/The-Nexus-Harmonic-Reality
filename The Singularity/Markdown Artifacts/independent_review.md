# Reverse-complement match coding: independent prototype review

## Scope and provenance

The first invocation of the original prototype failed before benchmarking because `ENC` applied `ord()` to integers produced by iterating over `bytes`. No dataset result was produced by that failed invocation. A corrected copy changed the map to `ENC = {c: i for i, c in enumerate(DNA)}`. The corrected coder, benchmark script, prediction, and local FASTA excerpt were hashed before execution; all hashes matched afterward (see `pre_run_seals.json` and `post_run_seals.json`).

This is an independent prototype, not a rerun of the separate `partner_coder_bundle.zip` described in the conversation: that bundle was not present in the runtime. The Arabidopsis full-genome values reported in the conversation therefore remain peer-reported here, not independently measured by this run.

## Results from the corrected prototype

The encoder uses 2-bit A/C/G/T literals, direct LZ matches, and optional reverse-complement match tokens; all custom stream sizes include its header and token overhead. Standard coders are tested on both ASCII sequence and the identical 2-bit-packed representation. Every tested stream decoded byte-for-byte to the input.

| Dataset | Bases | Direct-only bytes | Reverse-complement bytes | RC/direct-only | RC / best packed standard | RC / best ASCII standard | RC bases matched |
|---|---:|---:|---:|---:|---:|---:|---:|
| random_dna_52k | 52,224 | 13,068 | 13,071 | 1.000 | 1.000 | 0.910 | 15 |
| synthetic_inverted_repeats_exact_52k | 52,224 | 13,068 | 7,125 | 0.545 | 0.545 | 0.495 | 24,597 |
| synthetic_inverted_repeats_1pct_mutated_52k | 52,224 | 13,068 | 8,089 | 0.619 | 0.619 | 0.562 | 23,950 |
| SARS_CoV_2_reference_excerpt_4_4k | 4,408 | 1,113 | 1,113 | 1.000 | 1.000 | 0.878 | 0 |

The strongest result is on the constructed exact inverted-repeat fixture: 32 reverse-complement matches cover 24,597 bases, and the custom stream is 0.545× the best standard coder on the 2-bit-packed control. At 1% mutation, it is 0.619× the best packed standard coder. On seeded random DNA it is 1.0003× the best packed baseline (a 4-byte loss), consistent with no meaningful benefit from an absent repeat. The 4,408-base SARS-CoV-2 prefix is a short natural-data control with no reverse-complement matches found by these parser settings; it is not a whole-genome result.

Important scope limit: the local SARS sequence is a manually transcribed excerpt, not independently checksummed against the whole NCBI record. No result from this prototype supports the full-genome Arabidopsis byte counts reported separately.

## Interpretation

These measurements demonstrate the mechanics of a reverse-complement match token on controlled data containing such repeats. They do not establish a general compression advantage for arbitrary DNA. A fair benchmark should compare against standard compression both before and after the same 2-bit alphabet packing, report coder framing overhead, preserve a reverse-match-disabled control, and state the source sequence checksum.
