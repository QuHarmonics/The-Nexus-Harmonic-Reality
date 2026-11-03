# NEXUS §124 — BBP lanes and SHA-256 round in difference coordinates

Pre-run prediction SHA-256: `6f79721b0f6477069092816766f9832cbeae06d5a835bcc9b8e2a4e924a85332`

## Compiler instantiated

The difference table is built by the actual first-run equal-LEN stack with mixer fuse `(A,B) -> (A, A XOR B)`. Its output coefficients are evaluated as an ANF program; the table is not used only as a measurement.

## BBP lane fold

Compiled operator: `(q1,q4,q5,q6) -> 4*q1 - 2*q4 - q5 - q6, signed 7-bit output`.
All 65,536 four-nibble inputs were covered by the difference-table involution. The coefficient program was then executed on 2,926 rational-ring layer/column contributions (2,271 distinct input tuples).
The compiled columns, folded right-to-left through carry, yield `3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89`. Independent Machin route: `3.243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89`. The first 64 fractional hex digits agree.
Global column-normalization carry range over the finite N=64, G=12 stack: [-23, 37].
Different object: layer-local J carry has range [-4, 3]; exact identity H=w+16J-Jnext checks 2850/2850 with J in [-4,3].
ANF active monomials by degree: `{'0': 0, '1': 16, '2': 109, '3': 480, '4': 1306, '5': 2471, '6': 3577, '7': 4127, '8': 3609, '9': 2260, '10': 1019, '11': 336, '12': 74, '13': 8, '14': 0, '15': 0, '16': 0}`.

## SHA local gate compilation

Ch, Maj, full-adder and full-subtractor are each compiled from their complete 3-input truth table. The recovered ANF programs drive every bit of the 32-bit SHA additions, subtractions, Ch and Maj operations. Rotations and XORs remain their exact linear wiring operations.
Compiled SHA round vs reference: 1000/1000 randomized state/W/K cases matched and inverted.
Single-block message `NEXUS difference engine`: compiled digest `74f4227aab1097a2f87a499bc55e21cdb8ff2400908ee29f5b1e10e6136405df`; hashlib `74f4227aab1097a2f87a499bc55e21cdb8ff2400908ee29f5b1e10e6136405df`.
The compiled inverse returned all 256 eight-direction reader states through the 64-round path, using known W[t]/K[t]; feed-forward was reversed with incoming H retained.

## Difference tables of the composed SHA state map

The tables below are not a full enumeration of the 256-bit input domain. Each is the exact restriction of the actual 32-bit-word round/compression map to an LEN=8 affine reader slice, with one independent low-bit perturbation in each state word. The global SHA transformation itself is executed through the compiled bit-level operators above.

| Round | Max ANF degree | Active monomials (all degrees) | Mean H(DₐF) bits | Unique derivative vectors per direction | Affine on slice? |
|---:|---:|---:|---:|---:|---|
| 0 | 1 | 9/256 | 0.000000 | 1–1 | True |
| 1 | 4 | 48/256 | 2.886275 | 1–12 | False |
| 2 | 8 | 235/256 | 6.591220 | 34–128 | False |
| 3 | 8 | 256/256 | 6.964200 | 99–128 | False |
| 4 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 5 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 6 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 7 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 8 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 9 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 10 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 11 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 12 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 13 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 14 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 15 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 16 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 17 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 18 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 19 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 20 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 21 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 22 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 23 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 24 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 25 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 26 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 27 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 28 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 29 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 30 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 31 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 32 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 33 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 34 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 35 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 36 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 37 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 38 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 39 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 40 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 41 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 42 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 43 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 44 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 45 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 46 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 47 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 48 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 49 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 50 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 51 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 52 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 53 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 54 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 55 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 56 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 57 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 58 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 59 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 60 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 61 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 62 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 63 | 8 | 256/256 | 7.000000 | 128–128 | False |
| 64 | 8 | 256/256 | 7.000000 | 128–128 | False |
| feedforward | 8 | 256/256 | 7.000000 | 128–128 | False |

First round at which all 256 LEN=8 monomial addresses are active and every nonzero direction has 128 distinct derivative outputs (each occurring twice): 4.


The derivative-entropy column is the programme's `mean_a H(D_a F)` statistic on this declared 8-bit reader domain. It measures variation in derivative outputs for this restriction; it is not a physical energy measurement and not a claim that the full digest is invertible.

## Compile ledger

- BBP rational-ring lane contribution -> executed difference-program coefficients -> column carry -> π digits: **RUNS**.
- SHA Ch/Maj/full-adder/full-subtractor compiled locally from difference tables: **RUNS**.
- Full SHA-256 round arithmetic executed using reconstructed gate operators and compared to the reference: **RUNS**.
- 64-round route-back when W[t], K[t] and the endpoint state are available: **RUNS**.
- Digest-only inverse and minimal root observer: **OPEN**.

## Reproducibility

Run: `python nexus_bbp_sha_difference_engine.py` (standard library only; expects `sha256_bidirectional_audit.py` beside it). The JSON file stores the complete coefficient-support and per-depth results. The pre-run prediction seal is included beside these files.
