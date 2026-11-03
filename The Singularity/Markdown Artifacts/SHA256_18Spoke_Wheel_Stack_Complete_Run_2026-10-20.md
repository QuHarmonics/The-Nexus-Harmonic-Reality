# SHA-256 18-spoke wheel stack — complete run record

**Run date:** 2026-10-20  
**Target:** `Dont forget to drink your Ovaltine`  
**Reference/carrier:** empty-message SHA-256 execution  
**Fixed wheel period:** `H = pi/9 = 20 degrees`; 18 spokes  
**K constants:** SHA-256 `K[0..63]`, loaded from the supplied Glass Key shape-view source and kept in original round order.

## 1. Static plot reproduced

The phase of a 32-bit word is read as the full-circle normalized word folded into a 20-degree 18-spoke period:

`q(x) = 18*x mod 2^32`, `phase_deg(x) = 20*q(x)/2^32`.

The original static curve is reproduced exactly: at orientation 9.6 degrees, the indexed SHA constants give 7 hits in a ±1-degree aperture and 14 in a ±2-degree aperture. Across the 0.1-degree sweep, the respective ranges are 1–11 and 6–18 hits.

## 2. The 18-spoke phase is an address coordinate with one explicit missing bit

Because `18=2*9`, the phase tick `q` is even and

`q/2 = 9*x mod 2^31`.

The inverse of 9 modulo `2^31` is `954437177`, hence

`low31 = ((q/2)*954437177) mod 2^31`.

The phase cannot distinguish `x` from `x XOR 0x80000000`: the most-significant bit is the exact alias. Retaining that bit as a second coordinate restores the full word:

`x = low31 | (msb << 31)`.

This is an exact decoder identity. It passed 100,192 checks: all 64 K constants, every available 32-bit word in both Ovaltine and empty-message schedule traces (64 each), and 100,000 deterministic random words, with zero failures. The ring/substrate is not modified; the wheel is a readout projection, and its lost bit must not be discarded.

## 3. Fixed indexed spin rates

The round order is retained. At the chart's 9.6-degree orientation, the same moving wheel was run at rates tied to the proposed structure rather than freely optimized:

| Rotor rate | Meaning | K hits ±1° | K hits ±2° |
|---|---|---:|---:|
| 0°/round | stationary wheel | 7 | 14 |
| 2.5°/round = H/8 | eight SHA state lanes | 11 | 19 |
| 6.666666667°/round = H/3 | three-input Boolean relations | 10 | 11 |
| 2.222222222°/round = H/9 | nine-step H clock | 6 | 11 |

The round index remains bound to each K constant. The separate exploratory free-rate scan and permutation controls are included in the base sweep audit; they are not used to set the fixed rates above.

## 4. Empty hash used as the moving carrier

The target and empty executions were recomputed independently and verified against their standard SHA-256 digests. Each target route value is compared with the corresponding empty-run value at the same round. The phase separation is the lens readout; modular subtraction and XOR are retained as separate offset channels.

Carrier-locked alignment counts across 64 rounds:

| Layer | Within ±1° of empty phase | Within ±2° |
|---|---:|---:|
| K (same indexed driver) | 64/64 | 64/64 |
| Schedule word W | 11/64 | 19/64 |
| Partial T1 before W is added | 4/64 | 13/64 |
| Full T1 | 7/64 | 14/64 |
| T2 | 4/64 | 10/64 |

The initial disturbance also has a clear shift-register footprint. Before round 0, all eight state lanes are exactly equal to the empty execution. After the first round, the changed state occupies `a` and `e`; due to the fixed register shifts, the count of exactly equal lanes is **8, 6, 4, 2, 0** at rounds 0, 1, 2, 3, 4. The carrier reference exposes that unfolding path directly.

## 5. Exact differential closure

For each of the 64 rounds, the following target-minus-empty identities hold exactly modulo `2^32`:

- `delta_T1 = delta_partial_T1 + delta_W`
- `delta_a_next = delta_T1 + delta_T2`
- `delta_e_next = delta_d_before + delta_T1`

Each was checked 64/64. Applying `q(x)=18*x mod 2^32` preserves these additions exactly in phase-tick coordinates. This confirms that the lens representation carries the route algebra; it is not just a post-hoc histogram.

## 6. Layered-gate diagnostic

A four-layer candidate gate used the fixed 9.6-degree anchor, with K rotating at H/8, the empty-relative W offset at H/3, the partial-T1 offset at H/9, and the full-T1 offset in reverse at H/8. No round passed all four simultaneous aperture tests for either ±1° or ±2° in that particular arrangement. This is a measured outcome for that exact stack configuration—not a conclusion that no other substrate-derived arrangement can align.

## 7. Other supplied code executed

- Glass Key shape-view script: ran to completion. It reported mean shape magnitude `0.4575` at round 63 and `0.4437` at round 64 across its five-message sample (difference −0.0138 under its defined `A_shape` metric), and an e-register real-to-imag transition for `hello` from rounds 63 to 64.
- Glass Key v3 recursive computation: ran to completion and reproduced the known `W[0]` for `A` when the round-0 trace value is supplied.
- Double Glass Key/carry-signature test: ran to completion over its stated synthetic input and length-field controls.
- Pi wheel verification: the main wheel series reproduced pi to high precision; two alternate series in that script did not converge to pi under their current formulas and showed nonzero error plateaus.

## 8. What this run adds

The useful result is not that the wheel alone recovers a digest preimage. It gives a precise, invertible *two-coordinate word read*: 18-spoke phase plus its missing high bit. The empty execution supplies a moving carrier at every round, and the route's additive differences obey exact phase-tick closure. The next locator must preserve this extra bit/face and use the schedule/round constraints to choose the unknown schedule tail; that selector is not claimed solved by this run.

## Files

- `SHA256_K_18Spoke_Static_Sweep.csv`, `SHA256_K_18Spoke_Indexed_Spin_Sweep.csv`, `SHA256_K_18Spoke_Control_Summary.csv`
- `SHA256_K_18Spoke_Empty_Stack_Round_Ledger.csv`, `...Channel_Hits.csv`, `...Joint_Gate.csv`, `...Closure_Laws.csv`
- `SHA256_18Spoke_Empty_Carrier_Round_Ledger.csv`, `...Layer_Summary.csv`, `...Joint_Gate.csv`, `...Offset_Spin.csv`
- `SHA256_18Spoke_Phase_Lens_Decoder.md`
- `SHA256_18Spoke_Empty_Carrier_Phase_Map.png`, `SHA256_18Spoke_State_Lane_Propagation.png`
