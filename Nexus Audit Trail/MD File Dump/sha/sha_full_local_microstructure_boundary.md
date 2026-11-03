# SHA / Bitcoin Full Local Microstructure Boundary

## Goal

Test the strongest remaining **local** carry-geometry candidate before moving to nonlocal schedule constraints:

1. exact $T1$ staged carry-mask microstructure
2. exact $T1 + T2$ local carry microstructure

The coarse bundle already enforces:

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

This probe asks whether upgrading from coarse local geometry to **exact local carry microstructure** is enough to collapse the remaining 2-survivor events.

## Readout

- total 2-survivor events tested: **12**
- local-twin events: **11**
- history-alias events: **1**

### Exact $T1$ staged carry microstructure

- total collapses: **4**
- local-twin collapses: **3**
- history-alias collapses: **1**

### Exact $T1 + T2$ local carry microstructure

- total collapses: **4**
- local-twin collapses: **3**
- history-alias collapses: **1**

## Case table

| Header | Depth | Active round | Support depth | Reflection branch | Exact $T1$ collapse? | Exact local collapse? |
|---|---:|---:|---:|---|---|---|
| genesis | 8 | 56 | 1 | True | False | False |
| block_100000 | 2 | 62 | 1 | False | True | True |
| block_100000 | 3 | 61 | 1 | True | False | False |
| block_100000 | 4 | 60 | 1 | False | False | False |
| block_154595 | 4 | 60 | 1 | True | False | False |
| block_154595 | 11 | 53 | 1 | True | False | False |
| block_277316 | 7 | 57 | 1 | False | True | True |
| block_277316 | 8 | 56 | 2 | False | True | True |
| block_328734 | 9 | 55 | 1 | True | False | False |
| block_894470 | 5 | 59 | 1 | True | False | False |
| block_894470 | 11 | 53 | 1 | True | True | True |
| block_894470 | 12 | 52 | 1 | True | False | False |

## Strongest result

Even **exact local carry microstructure** does not collapse most surviving pairs.

So the remaining wall is no longer plausibly described as a missing local observable.

The path now points to a nonlocal separator:

$$
\boxed{\text{schedule compatibility / cross-round recurrence}}
$$

rather than

$$
\boxed{\text{one more local carry-side trick}}
$$

## Conclusion

The current SHA / Bitcoin path has exhausted the most natural local bundle upgrades:

$$
\text{coarse local geometry} \;\to\; \text{exact local microstructure}
$$

and several false branches still survive.

That means the next milestone should be built around:

1. schedule-law compatibility,
2. cross-round best-first search,
3. control-law steering (KRRB / PSREQ / QRHS style) for branch pressure.
