# SHA + Bitcoin Harmonic Round Analysis

## Scope

This run treats the **real recorded SHA/Bitcoin event rounds** as a discrete 64-step signal on the SHA die.

The event set is the union of:
- exact schedule-boundary events,
- broader-sweep nonunique cases,
- broader-sweep counterexample cases.

The question here is not whether SHA is literally music.
It is whether the event frontier behaves like a **concentrated harmonic band** rather than a flat random occupancy.

## Main results

### 1. Late-band concentration

Using the empirical late-wave band **53 through 62**:

- total recorded events: **25**
- late-band events: **24**
- late-band occupancy rate:
$$
0.960
$$

### 2. Round centroid

Weighted by event count, the frontier is centered at:

$$
r_{\text{mean}} = 57.800
$$

with weighted spread:

$$
\sigma_r = 2.926
$$

### 3. Peak rounds

Top occupied rounds:
|   round |   count |
|--------:|--------:|
|      56 |       5 |
|      60 |       5 |
|      57 |       3 |
|      62 |       3 |
|      53 |       2 |
|      55 |       2 |
|      59 |       2 |
|      61 |       2 |

### 4. Dominant spectral bins

Top non-DC round-spectrum components:
|   bin |   frequency |   period_rounds |   magnitude |
|------:|------------:|----------------:|------------:|
|     1 |    0.015625 |        64       |    23.9827  |
|     2 |    0.03125  |        32       |    21.0941  |
|     3 |    0.046875 |        21.3333  |    16.7931  |
|     4 |    0.0625   |        16       |    11.7489  |
|    15 |    0.234375 |         4.26667 |     8.80986 |
|    14 |    0.21875  |         4.57143 |     8.75065 |
|    16 |    0.25     |         4       |     8.544   |
|    13 |    0.203125 |         4.92308 |     8.24083 |

### 5. Dominant autocorrelation lags

Top autocorrelation lags:
|   lag |   autocorrelation |
|------:|------------------:|
|     1 |         0.572634  |
|     4 |         0.525428  |
|     3 |         0.461621  |
|     5 |         0.347699  |
|     2 |         0.34693   |
|     6 |         0.226045  |
|     7 |         0.173134  |
|     8 |         0.0774403 |

### 6. Cadence spacing between occupied rounds

Spacing counts between occupied rounds:
|   spacing |   count |
|----------:|--------:|
|         1 |       6 |
|         2 |       2 |

## Interpretation

This is not a proof of a literal acoustic model.

It **does** show that the real SHA/Bitcoin inversion frontier is not flat.
It behaves like a **late concentrated cadence band** with:

- strong confinement near rounds **56-60**,
- very high late-band energy concentration,
- recurring local spacing structure,
- and a nontrivial round-spectrum.

So the useful working statement is:

$$
\text{the frontier behaves more like a late harmonic body than a uniform search surface}
$$

That is consistent with the earlier schedule-capacity picture:
the attack happens earlier, but the usable discriminative body survives late.
