# Sparse Basin Proxy Report

## Scope

This is a **code-based proxy test** on the saved SHA/Bitcoin trace files already present in the working directory.

It does **not** prove a universal theorem of nature.
It does test the concrete claim that the current SHA/Bitcoin reverse traces already exhibit a **truth-retaining sparse survivor basin**.

## Main results

### 1. Truth retention

Across all `sha_lock_depth_counts.csv` rows, the truth path is retained in every recorded basin trace:

- Truth-retention rate: **1.000**
- Truth path exactly one in every row: **True**

### 2. Survivor collapse by richer bundle geometry

Mean survivor counts by bundle:

- `masks`: **48.625**
- `masks+nibbles`: **1.062**
- `masks+chirality`: **1.938**
- `masks+nibbles+chirality`: **1.000**

Reduction factor from masks-only to masks+nibbles+chirality:

$$
\frac{48.625}{1.000}
=
48.625
$$

So the richest bundle collapses the average survivor count by a factor of about **48.6x**
while retaining the truth path in every row.

### 3. True-rank stability under deeper push

From `sha_schedule_guided_deeper_push.json`:

- rows analyzed: **48**
- maximum depth reached: **16**
- true rank always 1: **True**
- true always in top 1: **True**
- maximum candidate count observed: **2**

### 4. Twin extinction

From `sha_broader_bitcoin_header_sweep.json`:

- nonunique cases: **11**
- next-depth collapse-to-1 cases: **6**
- next-depth collapse rate: **0.545**

From `sha_extinction_law_sweep.json`:

- two-survivor cases: **12**
- chirality-only kill cases: **9**
- chirality kill rate: **0.750**
- deeper kill cases: **7**
- deeper kill rate: **0.583**

## Interpretation

The saved real traces support the following proxy statement:

$$
\text{truth retained} = 1
$$

while

$$
\text{survivor count}
\downarrow
\text{sharply as bundle geometry gets richer.}
$$

That is exactly what a sparse survivor basin should look like:

1. the lawful lineage stays inside the basin,
2. the basin stays small relative to the coarse candidate space,
3. many local twins collapse under added geometry,
4. truth remains rank-1 deeper than a flat-search story would predict.

## Honest boundary

This report does **not** prove:

- general SHA-256 inversion,
- arbitrary Bitcoin header recovery,
- or a universal theorem about all folding systems.

It **does** show that the current saved Bitcoin/SHA traces already behave like a
**truth-retaining sparse basin proxy** rather than a flat blind search.
