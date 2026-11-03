# SHA ROM Control-Rail Test

## Aggregate slot interaction strength
|   rom_word |   mean_abs_round_synergy |
|-----------:|-------------------------:|
|          1 |                  2088.73 |
|         10 |                  2081.53 |
|          3 |                  2080.87 |
|         11 |                  2076.07 |
|         13 |                  2074.33 |
|          4 |                  2073.6  |
|          2 |                  2072.33 |
|          9 |                  2069    |
|         14 |                  2065.07 |
|         15 |                  2062.87 |
|          8 |                  2058.33 |
|         12 |                  2058.2  |
|          7 |                  2053    |
|          5 |                  2052.67 |
|          6 |                  2028    |
|          0 |                  2021.53 |

## Strongest pairwise round synergies
|   slot_a |   slot_b |   round_synergy |   pair_late_ratio |
|---------:|---------:|----------------:|------------------:|
|       11 |       10 |           -2165 |          0.243365 |
|       10 |       11 |           -2165 |          0.243365 |
|        1 |       15 |           -2144 |          0.257272 |
|       15 |        1 |           -2144 |          0.257272 |
|        3 |        1 |           -2142 |          0.237905 |
|        1 |        3 |           -2142 |          0.237905 |
|       10 |        4 |           -2136 |          0.231537 |
|        4 |       10 |           -2136 |          0.231537 |
|        1 |       14 |           -2128 |          0.245171 |
|       14 |        1 |           -2128 |          0.245171 |
|        9 |        1 |           -2127 |          0.259167 |
|        1 |        9 |           -2127 |          0.259167 |
|       13 |        4 |           -2118 |          0.249876 |
|       11 |        2 |           -2118 |          0.241191 |
|        4 |       13 |           -2118 |          0.249876 |
|        2 |       11 |           -2118 |          0.241191 |
|        3 |       14 |           -2113 |          0.252812 |
|       14 |        3 |           -2113 |          0.252812 |
|       10 |        9 |           -2110 |          0.26002  |
|        9 |       10 |           -2110 |          0.26002  |

## Contextual slot perturbation
| program   |   slot | base_word_hex   |   delta_round_sum |   delta_early |   delta_mid |   delta_late |
|:----------|-------:|:----------------|------------------:|--------------:|------------:|-------------:|
| abc       |      0 | 0x61626380      |                38 |            38 |          -3 |            3 |
| abc       |      4 | 0x00000000      |                15 |            32 |         -10 |           -7 |
| abc       |      8 | 0x00000000      |                -3 |           -17 |          29 |          -15 |
| abc       |     13 | 0x00000000      |                17 |             4 |          17 |           -4 |
| abc       |     14 | 0x00000000      |                52 |             1 |          36 |           15 |
| abc       |     15 | 0x00000018      |                14 |             1 |          -7 |           20 |
| len55     |      0 | 0x42424242      |               -99 |           -21 |         -81 |            3 |
| len55     |      4 | 0x42424242      |               -99 |           -15 |         -72 |          -12 |
| len55     |      8 | 0x42424242      |              -112 |           -21 |         -82 |           -9 |
| len55     |     13 | 0x42424280      |                22 |            -1 |          -1 |           24 |
| len55     |     14 | 0x00000000      |               -46 |             0 |         -28 |          -18 |
| len55     |     15 | 0x000001b8      |               -42 |             0 |         -51 |            9 |

## Read

This pass is about nonlinearity in the compiled field.

If all ROM words were plain data cells, pairwise composition would look close to additive.

It does not.

The biggest interaction magnitudes concentrate around:
- early payload rails
- footer rails
- specific hinge pairings

And in real one-block programs, toggling slot 14 or 15 produces a different round-profile than toggling an ordinary payload rail.

Operational read:
- slot 15 behaves like a footer immediate
- slot 14 behaves like a high footer / control rail
- payload rails still drive most of the lexical pressure
- composition in the compiler/runtime is nonlinear, so the block behaves like microcode, not flat data
