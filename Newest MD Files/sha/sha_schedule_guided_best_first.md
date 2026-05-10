# SHA / Bitcoin Schedule-Guided Best-First Search

## Goal

Turn the schedule law into an actual ranking engine and test whether it keeps the true chain alive with small beam widths.

Candidates are ranked by:

$$
Q(C) = \big(\text{schedule residual abs-sum},\ \text{schedule residual Hamming cost},\ \text{support depth}\big)
$$

with lower values preferred.

The bundle still enforces local admissibility, but the schedule law is now the main global ranking signal.

## Per-header results

### genesis (height 0)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 1 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 1 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 2 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 1 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_57043 (height 57043)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 1 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 3 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 3 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 1 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 1 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_100000 (height 100000)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 2 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 2 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 2 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 1 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 1 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 1 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_154595 (height 154595)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 2 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 1 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 1 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 2 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_277316 (height 277316)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 1 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 1 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 2 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 2 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 1 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_328734 (height 328734)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 1 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 1 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 1 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 2 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 1 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 1 | 1 | True | True | True | True | True | True | True |

### block_894470 (height 894470)

| Depth | Active round | Total candidates | True rank | k=1 | k=2 | k=4 | k=8 | k=16 | k=32 | k=64 |
|---:|---:|---:|---:|---|---|---|---|---|---|---|
| 1 | 63 | 1 | 1 | True | True | True | True | True | True | True |
| 2 | 62 | 1 | 1 | True | True | True | True | True | True | True |
| 3 | 61 | 1 | 1 | True | True | True | True | True | True | True |
| 4 | 60 | 1 | 1 | True | True | True | True | True | True | True |
| 5 | 59 | 2 | 1 | True | True | True | True | True | True | True |
| 6 | 58 | 1 | 1 | True | True | True | True | True | True | True |
| 7 | 57 | 1 | 1 | True | True | True | True | True | True | True |
| 8 | 56 | 1 | 1 | True | True | True | True | True | True | True |
| 9 | 55 | 1 | 1 | True | True | True | True | True | True | True |
| 10 | 54 | 1 | 1 | True | True | True | True | True | True | True |
| 11 | 53 | 2 | 1 | True | True | True | True | True | True | True |
| 12 | 52 | 2 | 1 | True | True | True | True | True | True | True |

## Beam-width survival summary

| Beam width | Depth | True-chain survival count | Total headers tested at depth |
|---:|---:|---:|---:|
| 1 | 1 | 7 | 7 |
| 1 | 2 | 7 | 7 |
| 1 | 3 | 7 | 7 |
| 1 | 4 | 7 | 7 |
| 1 | 5 | 7 | 7 |
| 1 | 6 | 7 | 7 |
| 1 | 7 | 7 | 7 |
| 1 | 8 | 7 | 7 |
| 1 | 9 | 7 | 7 |
| 1 | 10 | 7 | 7 |
| 1 | 11 | 7 | 7 |
| 1 | 12 | 7 | 7 |
| 2 | 1 | 7 | 7 |
| 2 | 2 | 7 | 7 |
| 2 | 3 | 7 | 7 |
| 2 | 4 | 7 | 7 |
| 2 | 5 | 7 | 7 |
| 2 | 6 | 7 | 7 |
| 2 | 7 | 7 | 7 |
| 2 | 8 | 7 | 7 |
| 2 | 9 | 7 | 7 |
| 2 | 10 | 7 | 7 |
| 2 | 11 | 7 | 7 |
| 2 | 12 | 7 | 7 |
| 4 | 1 | 7 | 7 |
| 4 | 2 | 7 | 7 |
| 4 | 3 | 7 | 7 |
| 4 | 4 | 7 | 7 |
| 4 | 5 | 7 | 7 |
| 4 | 6 | 7 | 7 |
| 4 | 7 | 7 | 7 |
| 4 | 8 | 7 | 7 |
| 4 | 9 | 7 | 7 |
| 4 | 10 | 7 | 7 |
| 4 | 11 | 7 | 7 |
| 4 | 12 | 7 | 7 |
| 8 | 1 | 7 | 7 |
| 8 | 2 | 7 | 7 |
| 8 | 3 | 7 | 7 |
| 8 | 4 | 7 | 7 |
| 8 | 5 | 7 | 7 |
| 8 | 6 | 7 | 7 |
| 8 | 7 | 7 | 7 |
| 8 | 8 | 7 | 7 |
| 8 | 9 | 7 | 7 |
| 8 | 10 | 7 | 7 |
| 8 | 11 | 7 | 7 |
| 8 | 12 | 7 | 7 |
| 16 | 1 | 7 | 7 |
| 16 | 2 | 7 | 7 |
| 16 | 3 | 7 | 7 |
| 16 | 4 | 7 | 7 |
| 16 | 5 | 7 | 7 |
| 16 | 6 | 7 | 7 |
| 16 | 7 | 7 | 7 |
| 16 | 8 | 7 | 7 |
| 16 | 9 | 7 | 7 |
| 16 | 10 | 7 | 7 |
| 16 | 11 | 7 | 7 |
| 16 | 12 | 7 | 7 |
| 32 | 1 | 7 | 7 |
| 32 | 2 | 7 | 7 |
| 32 | 3 | 7 | 7 |
| 32 | 4 | 7 | 7 |
| 32 | 5 | 7 | 7 |
| 32 | 6 | 7 | 7 |
| 32 | 7 | 7 | 7 |
| 32 | 8 | 7 | 7 |
| 32 | 9 | 7 | 7 |
| 32 | 10 | 7 | 7 |
| 32 | 11 | 7 | 7 |
| 32 | 12 | 7 | 7 |
| 64 | 1 | 7 | 7 |
| 64 | 2 | 7 | 7 |
| 64 | 3 | 7 | 7 |
| 64 | 4 | 7 | 7 |
| 64 | 5 | 7 | 7 |
| 64 | 6 | 7 | 7 |
| 64 | 7 | 7 | 7 |
| 64 | 8 | 7 | 7 |
| 64 | 9 | 7 | 7 |
| 64 | 10 | 7 | 7 |
| 64 | 11 | 7 | 7 |
| 64 | 12 | 7 | 7 |

## Strongest read

If the true chain survives at small beam widths under schedule-dominant ranking, then the path has moved beyond brute-force framing in a practical sense, not just a descriptive one.

This would mean:

$$
\text{bundle admissibility} + \text{schedule recurrence ranking}
\;\Rightarrow\;
\text{true chain preserved under narrow search}
$$

## Conclusion

This report does not yet claim full inversion. It tests whether the message schedule is strong enough to function as the first real search engine for the tail corridor.
