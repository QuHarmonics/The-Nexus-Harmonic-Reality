# SHA / Bitcoin Residual Taxonomy Refinement

## Question

When a coarse two-survivor event appears, is it always a local twin at the active round?

## Answer

No.

The observed 2-survivor events split into two structural types:

1. **local twins** — the two chains differ at exactly one round in the current tail window
2. **history aliases** — the two chains differ at multiple rounds and only collapse to the same coarse survivor count at the current depth

## Full list

| Header | Depth | Active round | Differing rounds | # differing rounds | Current $W_t$ same? | Current $h_t$ same? | Reflection branch? |
|---|---:|---:|---|---:|---|---|---|
| genesis | 8 | 56 | [56] | 1 | False | False | True |
| block_100000 | 2 | 62 | [62] | 1 | False | False | False |
| block_100000 | 3 | 61 | [61] | 1 | False | False | True |
| block_100000 | 4 | 60 | [61] | 1 | True | True | False |
| block_154595 | 4 | 60 | [60] | 1 | False | False | True |
| block_154595 | 11 | 53 | [53] | 1 | False | False | True |
| block_277316 | 7 | 57 | [57] | 1 | False | False | False |
| block_277316 | 8 | 56 | [56, 57] | 2 | False | True | False |
| block_328734 | 9 | 55 | [55] | 1 | False | False | True |
| block_894470 | 5 | 59 | [59] | 1 | False | False | True |
| block_894470 | 11 | 53 | [53] | 1 | False | False | True |
| block_894470 | 12 | 52 | [52] | 1 | False | False | True |

## Type A — local twins

Total local twins: **11**

These are the cases where the entire ambiguity is concentrated at a single active round.
These are the cleanest candidates for the runtime-reflection law.

| Header | Depth | Active round | Current $\Delta W_t$ | Current $\Delta h_t$ | Reflection branch? |
|---|---:|---:|---|---|---|
| genesis | 8 | 56 | `0x00090000` | `0x00090000` | True |
| block_100000 | 2 | 62 | `0x000001e0` | `0x000000a0` | False |
| block_100000 | 3 | 61 | `0x000c0000` | `0x000c0000` | True |
| block_100000 | 4 | 60 | `0x00000000` | `0x00000000` | False |
| block_154595 | 4 | 60 | `0x00006000` | `0x00006000` | True |
| block_154595 | 11 | 53 | `0x00030000` | `0x00030000` | True |
| block_277316 | 7 | 57 | `0xf0000000` | `0x50000000` | False |
| block_328734 | 9 | 55 | `0x06000000` | `0x06000000` | True |
| block_894470 | 5 | 59 | `0x00000006` | `0x00000006` | True |
| block_894470 | 11 | 53 | `0x90000000` | `0x90000000` | True |
| block_894470 | 12 | 52 | `0x0000c000` | `0x0000c000` | True |

## Type B — history aliases

Total history aliases: **1**

These are not purely local twins. The ambiguity is distributed across multiple rounds of the tail chain.
So they require a different explanation than the simple runtime-reflection involution.

| Header | Depth | Active round | Differing rounds | Current $\Delta W_t$ | Current $\Delta h_t$ |
|---|---:|---:|---|---|---|
| block_277316 | 8 | 56 | [56, 57] | `0x40000000` | `0x00000000` |

## Strongest correction

The residual taxonomy is now sharper than the earlier branch split.

The right picture is:

$$
\text{coarse 2-survivor event}
\;\to\;
\begin{cases}
\text{local twin} & \text{(single-round ambiguity)}\\
\text{history alias} & \text{(multi-round ambiguity)}
\end{cases}
$$

and only some local twins belong to the clean runtime-reflection branch.

## Conclusion

The path is now better resolved:

- not all 2-survivor events are the same,
- not all of them are local,
- and the true runtime-reflection law should be stated only for the **local twin** branch.
