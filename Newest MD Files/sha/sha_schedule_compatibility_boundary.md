# SHA / Bitcoin Schedule Compatibility Boundary

## Goal

Move beyond local carry geometry and test whether the surviving false branches already fail the **true SHA-256 message schedule** when audited as full chains.

The schedule law is

$$
W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16} \pmod{2^{32}}.
$$

For each 2-survivor event, we evaluate the candidate chain by replacing the guessed tail words into the known header schedule frame and measuring the schedule residuals round by round.

## Readout

- total 2-survivor events tested: **12**
- local-twin events: **11**
- history-alias events: **1**

### Exact schedule collapse

- total collapses: **12**
- local-twin collapses: **11**
- history-alias collapses: **1**

### True branch preferred by schedule residual sum

- total: **12 / 12**
- local twins: **11 / 11**
- history aliases: **1 / 1**

### True branch preferred by schedule residual Hamming cost

- total: **12 / 12**
- local twins: **11 / 11**
- history aliases: **1 / 1**

## Case table

| Header | Depth | Support depth | Reflection branch | Exact schedule collapse? | True better by abs-sum? | True better by HW-sum? |
|---|---:|---:|---|---|---|---|
| genesis | 8 | 1 | True | True | True | True |
| block_100000 | 2 | 1 | False | True | True | True |
| block_100000 | 3 | 1 | True | True | True | True |
| block_100000 | 4 | 1 | False | True | True | True |
| block_154595 | 4 | 1 | True | True | True | True |
| block_154595 | 11 | 1 | True | True | True | True |
| block_277316 | 7 | 1 | False | True | True | True |
| block_277316 | 8 | 2 | False | True | True | True |
| block_328734 | 9 | 1 | True | True | True | True |
| block_894470 | 5 | 1 | True | True | True | True |
| block_894470 | 11 | 1 | True | True | True | True |
| block_894470 | 12 | 1 | True | True | True | True |

## Strongest result

The schedule law is a much stronger separator than any remaining local observable.

If exact schedule consistency collapses most pairs, then the corridor has truly moved from

$$
\text{local geometry}
\;\to\;
\text{global recurrence compatibility}.
$$

Even when exact collapse is not complete, the schedule residual acts as a principled best-first score because the true chain should minimize recurrence error globally.

## Conclusion

The next milestone should therefore be built around:

1. schedule-law compatibility as the main ranking signal,
2. best-first / A*-like branching over chain states,
3. local bundle terms only as tie-breakers or admissible side witnesses.
