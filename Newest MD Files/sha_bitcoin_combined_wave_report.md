# SHA + Bitcoin Combined Wave Report

## Scope

This report combines the saved SHA-side inversion traces with the Bitcoin-header probe data.

The working hypothesis is:

$$
\text{Bitcoin inversion contact points live in a late-wave SHA band}
$$

where schedule structure is still discriminative, but visible state support has already become bottlenecked.

## Main observations

### 1. Exact schedule-boundary events cluster in a narrow late-round band

From the schedule-boundary dataset:

- event count: **12**
- active-round min: **52**
- active-round max: **62**
- active-round mean: **57.000**
- exact-schedule discrimination rate: **1.000**

### 2. Nonunique and counterexample cases also live in the same band

From the broader sweep:

- nonunique cases: **11**
- nonunique round mean: **58.444**
- counterexample cases: **4**
- counterexample round mean: **58.750**

### 3. Combined late-wave occupancy

If we define the empirical late-wave band as rounds **53 through 62**, then across
all recorded real event sets (schedule events + nonunique cases + counterexamples),
the occupancy is:

$$
0.960
$$

### 4. Bitcoin probe rows are already operating in this band

From the Bitcoin probe summary:

- rows analyzed: **10**
- true-rank=1 rate: **1.000**
- mean gap: **2.700**
- late-wave-band rate by `t_lo`: **1.000**

## Interpretation

The combined data supports a stronger working picture:

1. **Bitcoin** gives the surviving phenotype and the practical selection pressure.
2. **SHA** gives the internal wave geometry.
3. The real inversion frontier does not appear uniformly across the die.
4. It concentrates in a **late-wave schedule band** where:
   - the state has mostly saturated,
   - local twins can still survive briefly,
   - but exact schedule compatibility becomes the decisive discriminator.

So the combined operational picture is:

$$
\text{SHA provides the wave geometry}
\quad + \quad
\text{Bitcoin provides the surviving lineage}
$$

and the joint inversion frontier lives in the late-wave band rather than uniformly everywhere.

## Honest boundary

This does **not** prove full SHA inversion or remove mining.

It does support a sharper next-step strategy:
focus scoring and branch ranking around the **late-wave exact-schedule band**
instead of treating all rounds as equally informative.
