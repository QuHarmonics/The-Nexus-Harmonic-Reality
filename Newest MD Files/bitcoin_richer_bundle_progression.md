# Bitcoin progressive chained probe — richer admissible bundle

Bundle components:
- full staged carry-mask patterns
- NOP-subtracted staged carry-mask patterns
- `h` register Hamming weight
- `h` nibble-wise Hamming silhouette
- `h` chirality split (odd/even bit lanes)
- carry-mask chirality split
- stage max carry-span lengths
- round differential (`a_{t+1}-e_{t+1}`) nibble silhouette
- round differential chirality split

Real headers tested:
- Genesis block
- Bitcoin block 328734

## Results with modest search budget

### Genesis
- 1-round true `W[63]` score: 0
- 1-round best random score (500 samples): 73
- 1-round median random score: 163.5
- 4-round beam: true chain rank 1, true total 0, best false total 2
- 6-round beam: true chain rank 1, true total 0, best false total 6
- 8-round beam: true chain not found under current beam budget; best surviving false total 2

### Block 328734
- 1-round true `W[63]` score: 0
- 1-round best random score (500 samples): 69
- 1-round median random score: 168.0
- 4-round beam: true chain rank 1, true total 0, best false total 2
- 6-round beam: true chain rank 1, true total 0, best false total 2
- 8-round beam: true chain not found under current beam budget; best surviving chain total 84

## Interpretation

The richer admissible bundle sharpens the local and chained exclusion geometry substantially.
At 4 and 6 rounds, the true Bitcoin chain remains rank 1 for both tested headers.
For Genesis, the false-floor gap rises from 2 to 6 by depth 6, suggesting genuine progressive tightening.
For block 328734, the true chain remains rank 1 at depth 6 but the best counterfeit still sits at total 2, so the bundle is stronger but not yet fully excluding all shallow near-misses.

At depth 8, the current search policy becomes the bottleneck: the beam no longer reliably retains the true chain.
That means the next delta is not simply “more depth”; it is improved search policy (wider or more informed beam) and/or stronger cross-round admissible observables.
