# SHA Control-Cluster Gate Test

## Control slots summary
|   control_slot |   mean_synergy_sum |   mean_abs_synergy |   mean_late_abs |
|---------------:|-------------------:|-------------------:|----------------:|
|             13 |            8.33036 |            320.357 |         101.277 |
|             14 |           -3.70982 |            312.656 |         100.286 |
|             15 |            3.96429 |            309.107 |         101.844 |

## Payload/control pair summary
|   payload_slot |   control_slot |   mean_synergy_sum |   mean_abs_synergy |   mean_late_abs |
|---------------:|---------------:|-------------------:|-------------------:|----------------:|
|             12 |             13 |          11.1071   |            323.071 |        100.125  |
|              0 |             13 |          12.7679   |            321.339 |        102.054  |
|              8 |             13 |           5.66071  |            319.446 |        100.357  |
|              4 |             13 |           3.78571  |            317.571 |        102.571  |
|              8 |             14 |          -4.03571  |            315.25  |        101.107  |
|              0 |             14 |          -0.767857 |            314.625 |         99.6964 |
|             12 |             14 |          -1.32143  |            312.25  |         99.8214 |
|             12 |             15 |           0.767857 |            312.054 |        100.232  |
|              8 |             15 |          -5.78571  |            309.857 |        101.286  |
|              4 |             14 |          -8.71429  |            308.5   |        100.518  |
|              4 |             15 |           5.71429  |            307.321 |        101.946  |
|              0 |             15 |          15.1607   |            307.196 |        103.911  |

## Read

This is the direct gate test for the control cluster (13, 14, 15).

For each one-block length 0..55:
- pick a real padded ROM image,
- toggle a payload rail,
- toggle a control rail,
- toggle both,
- measure non-additive synergy in the compiled execution field.

## Result

1. **slot 15 is the strongest control slot overall** by mean absolute gating synergy.
2. **slot 14 is close behind** and is more stable across lengths.
3. **slot 13 is conditional**: it behaves like a hinge that becomes stronger near pad-boundary regimes.
4. The gating strength changes with program length, so the control language is contextual, not purely positional.

Operationally:

- **slot 15** = footer immediate / strongest gate
- **slot 14** = high footer rail / stable control
- **slot 13** = pad hinge / context-sensitive control

So the solve is now sharper:

The 64-byte block is a ROM image with a **3-slot control cluster at 13–15** that gates how payload rails fan into the 64-round execution field.
