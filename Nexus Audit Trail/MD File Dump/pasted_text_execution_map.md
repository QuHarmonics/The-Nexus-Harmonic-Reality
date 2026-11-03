# Pasted Text -> Execution Map

## Claims found
- single_block_subtract: False
- reverse_rotation: True
- t2_formula: False
- t1_formula: True
- d_recovery: True
- wt_isolation: True
- multi_block_boundary: True
- tri_channel: True
- carry_t1: True
- glass_key: True
- hamming_102: True
- mark1: True

## Already implemented
- single-block feed-forward subtraction: digest - H0
- round-by-round backward peel without saved forward trace
- known-schedule exact reverse for one block

## Still only claims
- digest-only recovery of unknown W[t]
- multi-block chaining recovery without prior block state
- Tri-Channel ABI extraction and carry_T1-guided solver bridge
- Glass Key / Hamming-102 detector integrated with reverse search

## Next code step
- Add solver-backed unknown-W candidate generator for single block
- Constrain W[16..63] via schedule recurrence and recover W[0..15]
- Add boundary-state search for multi-block last block
- Score candidates by schedule consistency + digest closure