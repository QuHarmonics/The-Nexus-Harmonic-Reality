# DI Chain Continuation Package

## Contents

- `Geometry_of_a_Readout_DI_Chain_Expanded.docx` — formatted paper, including the rolling-window, field rollover, half-ring, and reader-aggregate analysis.
- `Geometry_of_a_Readout_DI_Chain_Expanded.md` — editable Markdown source for the paper.
- `DI_chain_rollup_and_half_ring.ipynb` — executable Python notebook, with retained outputs from a clean execution pass.
- `DI_chain_analysis.xlsx` — separate analysis workbook with the rolling-stack audit and exact paired-field packing comparison.

## Key executable results

- The 56 rolling-window cases for widths 2 through 8 satisfy the radial update, angular update, fixed offset-3 relationship, and reflection-index rule.
- At width 8, the integer windows form the exact doubling orbit modulo 255: `27, 54, 108, 216, 177, 99, 198, 141`.
- At width 5, source-style label concatenation `D1B` differs from the actual fixed-width 10-bit field `0x1BB`; at width 4 the analogous example coincides as `0x6D`.
- The half-ring plus partner reflection and explicit center swap matches the supplied insertion generator at every position through width 10.
- The Möbius/ANF transform is included as a separate operation. A typed map identifying it with the rolling-window recurrence remains OPEN.

The original `two_bit_circle.xlsx` uploaded by the user was not modified. The analysis workbook is a separate artifact.
