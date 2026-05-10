# SHA/Bitcoin Inversion Frontier Audit

## Scope

This audit uses the **real saved trace files** already present in the working directory:

- `sha_lock_depth_counts.csv`
- `sha_schedule_guided_deeper_push.json`
- `sha_schedule_compatibility_boundary.json`
- `sha_broader_bitcoin_header_sweep.json`
- `sha_extinction_law_sweep.json`

It does **not** prove general SHA-256 inversion or a complete Bitcoin shortcut.
It measures how close the current trace stack is to a **truth-retaining sparse inversion basin**.

## Main findings

### 1. Rich bundle collapse while keeping truth alive

Mean survivors:
- masks: **48.625**
- masks+nibbles+chirality: **1.000**

Reduction factor:
$$
\frac{48.625}{1.000}
=
48.625
$$

Truth retention on the richest bundle:
$$
1.000
$$

### 2. True-rank persistence

Across deeper-push rows:
- max depth observed: **16**
- max candidate count observed: **2**
- true rank = 1 rate: **1.000**
- true in top 1 rate: **1.000**

### 3. Exact schedule boundary is the sharpest discriminator

Across two-survivor schedule-boundary events:
- schedule discrimination rate:
$$
1.000
$$

That means the true branch is exact under schedule compatibility while the false branch is not,
for **every recorded two-survivor event** in this dataset.

Mean false-branch schedule penalties:
- absolute residual sum: **1353837245.2**
- Hamming-weight residual sum: **21.8**

### 4. Twin extinction is real but not yet total

- nonunique broader-sweep cases: **11**
- next-depth collapse rate: **0.545**
- chirality kill rate: **0.750**
- deeper kill rate: **0.583**

### 5. Local twin law

Among nonunique cases, the fraction matching the strong local-twin signature
(delta-equal, single-nibble, weight-2, mixed-parity, fused-wall preservation) is:

$$
0.455
$$

### 6. Conservative heuristic inversion-readiness score

This is a plain average of five observed terms:
- truth retention,
- collapse strength,
- true-rank persistence,
- exact-schedule discrimination,
- mean twin-extinction rate.

Result:
$$
0.921
$$

This is **not** a theorem. It is a compact operational summary of the current frontier.

## Interpretation

The current saved traces support the following code-backed statement:

$$
\text{truth stays alive}
$$

while

$$
\text{candidate count collapses sharply under richer geometry}
$$

and

$$
\text{exact schedule compatibility cleanly separates true from false twins at the recorded frontier.}
$$

That is already much stronger than a flat blind-search story.

## Honest boundary

This still does **not** prove:
- arbitrary SHA-256 inversion,
- arbitrary Bitcoin header recovery,
- or complete replacement of mining by guided inversion.

What it **does** show is that the present trace stack is behaving like a
**structured inversion frontier** with a strong schedule-compatibility discriminator.
