# Hold-by-order and tower-mirror prediction

## Operational definition
For width n, P_n(x) is the existing ring partner: bit reversal J_n(x) when J_n(x) != x, otherwise complement. For an ordered stream sigma of all 2^n words, define H_sigma(t) as the number of partner pairs with exactly one member among the first t stream words. This is an order-dependent prefix-cut statistic; no timing or physical interpretation is implied.

The five orders under test are fixed as follows:
1. **address**: R_n[0],...,R_n[2^n-1], the center-swapped ring from `wheels.ring_arrays`.
2. **value/counter**: 0,1,...,2^n-1.
3. **sheet**: make T by concatenating fixed-width binary R_n words in address order, reverse all bits of T, complement every bit, then chunk the resulting stream into n-bit words. This is the W6 sheet convention already implemented in `run_wheels.py`.
4. **route code**: sort all words by the fixed-width lexicographic/integer order of the corpus E/G route code (`side bit || canonical route code`) in `nexus_route_rank_sphere_audit.py`.
5. **half-table index lifted to words**: order canonical representatives by increasing `half_index`/representative rank, and emit each representative immediately followed by its partner. The half-table is pair-indexed; this lift makes the within-pair read order explicit.

All five orders must be permutations of the complete word set. H_sigma(t) must equal a direct seen/unseen partner-pair counter at every prefix. Predictions: address and route-code orders reach 2^(n-1) open pairs at their first-half seam; value order matches the already sealed native counter profile and has peak 2^(n-2)+2^floor((n+1)/2)-1; the adjacent-pair half-table lift has peak 1. No closed-form peak is prespecified for the sheet order.

## Tower-mirror prediction
For L >= 2, 1 <= k <= L, n=L+k, and every t in [0,2^L], define q=ceil(t/2^k). Let C_w(q) count low-width words x<q that are non-palindromic and on the partner side x>P_w(x), with C_0(q)=0. The predicted profile is

    H_{L+k}(t) = t - 2 C_{L-k}(ceil(t/2^k)).

The formalization distinguishes “non-palindromic partners below q” from all non-palindromic words: the count is explicitly partner-side words x>P_w(x). It agrees with the stated seam formula at t=2^L if the full profile holds.

## Scope and provenance
The source bundle itself does not include the Excel workbook. The sheet convention is reproduced from the W6 implementation in the supplied `run_wheels.py`; route code comes from the separately supplied corpus route audit. Some exploratory checks were used to make the ambiguous phrase “non-palindromic partners below q” executable. This document is the prediction for the formal audit run, not a claim that no exploratory calculation occurred before it was written.
