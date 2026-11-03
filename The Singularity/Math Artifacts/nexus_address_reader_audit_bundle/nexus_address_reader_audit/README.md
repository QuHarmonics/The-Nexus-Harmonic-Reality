# NEXUS Address-Reader Widths 13–16

This is the reproducible follow-up to §22/§23, adding §24 to the compiler log. It tests arrival order only; the ring, partner rule, center swap and physical address are unchanged.

## Start here

1. Read `audit_report.md` for the method, exact scores and scope boundaries.
2. Read `compiler_rings_log.md` §24 for the merged ledger entry.
3. Run `python scripts/address_reader_width13_16.py` to reconstruct the ring, cross-check it against `sources/wheels.py`, and rerun the complete structured-family audit.

## What was checked

Widths 13–16 were tested exhaustively over every input word (8,192; 16,384; 32,768; and 65,536 words). At each width, every member of a predefined reader family was scored. The family reads outer bit-pairs in order from the ends inward, allows either arrival order inside each pair, then enumerates every ordering of a 3-bit center core for odd widths or a 4-bit core for even widths. Family sizes were 192, 768, 384 and 1,536 input-bit schedules. The readiness score is an exact integer event sum turned into an exact rational mean.

The structured-family minimum beats the full outside-in schedule and MSB-first at all four widths. Plain-value core order is family-optimal at widths 14–16. At width 13, the optimal 3-bit core instead reads the middle bit first, then the high-significance bit, then the low-significance bit; plain value is 484 event-sum units worse.

This is **not** an exhaustive search over all `n!` schedules at widths 13–16. Global optimality remains OPEN. The prediction protocol is recorded before execution and its hash remained unchanged.

## Files

- `prediction_seal.txt`, `prediction_seal.sha256`: pre-run protocol and seal.
- `sources/wheels.py`: byte-for-byte copy of the existing ring source; SHA-256 is recorded in the results and provenance.
- `scripts/address_reader_width13_16.py`: direct ring reconstruction, source cross-check, semantic readiness scorer and structured-family enumerator.
- `outputs/address_reader_width13_16_results.json`: exact results, means, min counts, source checks, and seal checks.
- `outputs/address_reader_summary.csv`: comparator-reader summary and exact means.
- `outputs/address_reader_per_output_bit.csv`: mean readiness event for each address output bit under each named reader.
- `outputs/address_reader_structured_family.csv`: all 2,880 structured-family schedules with exact score and whether each attains the minimum.
- `audit_report.md`: method and results.
- `compiler_rings_log.md`: previous merged log through §23 plus new §24.
- `execution_provenance.json`, `SHA256SUMS.txt`: provenance and file checksums.

The script requires Python 3 and NumPy.
