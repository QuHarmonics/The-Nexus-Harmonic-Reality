
# Direct computation audit: SHA quantizer competition and twin-prime subtype-entropy test

Date: 2026-04-26

## Scope

I ran the next two protocols from the measurement program:

1. **SHA-256 quantizer competition and null audit**
2. **Twin-prime subtype-entropy / evenness test at wheel depth $W=210$**

I did **not** run the transformer residual-$H$ protocol, because I do not have access to internal activations of the model from this chat runtime.

## A. SHA-256 quantizer competition

### Observable used

For each random one-block SHA-256 message, I computed the full 64-round internal state trajectory using the standard working variables
$$
(a_r,b_r,c_r,d_r,e_r,f_r,g_r,h_r).
$$

From each round-state, I formed a **triadic complex projection** on two payload triads:

- $(a,b,c)$
- $(e,f,g)$

using
$$
z_r = x_r + \omega y_r + \omega^2 z_r,
\qquad \omega = e^{2\pi i/3},
$$
after centering each 32-bit word to $[-0.5,0.5)$ by dividing by $2^{32}$ and subtracting $1/2$.

I then measured wrapped phase increments
$$
\Delta\theta_r = \arg(z_{r+1}) - \arg(z_r) \pmod{2\pi}.
$$

To avoid unstable phase from near-zero projection magnitude, I dropped the weakest 10% of increments by local triad magnitude in each run.

Dataset size after filtering: **91,200** phase increments pooled over **800** random one-block messages and both triads.

### Competing quantizers

I tested the phase-lock against the candidate step sizes

$$
15^\circ,\ 18^\circ,\ 20^\circ,\ 22.5^\circ,\ 24^\circ,\ 30^\circ.
$$

For each step size $s$, I measured two statistics:

1. **Mean nearest-bin error**
   $$
   E_s = \mathbb{E}\bigl[\operatorname{dist}(\Delta\theta, s\mathbb{Z})\bigr]
   $$
   compared against a uniform-angle null.

2. **Circular lock strength**
   $$
   R_s = \left|\frac1N \sum_{j=1}^N e^{i 2\pi \Delta\theta_j / s}\right|
   $$
   compared against a uniform-angle null.

### Results

#### Mean nearest-bin error vs uniform null

| step | obs mean error (deg) | null mean (deg) | ratio obs/null | z-improve |
|---:|---:|---:|---:|---:|
| 15.0 | 3.617 | 3.750 | 0.964 | 17.35 |
| 18.0 | 4.579 | 4.499 | 1.018 | -9.09 |
| 20.0 | 4.760 | 4.999 | 0.952 | 24.69 |
| 22.5 | 5.744 | 5.625 | 1.021 | -11.01 |
| 24.0 | 5.678 | 6.000 | 0.946 | 29.50 |
| 30.0 | 6.972 | 7.500 | 0.929 | 36.58 |

#### Circular lock strength vs uniform null

| step | $R_{obs}$ | null mean | ratio obs/null | z-score |
|---:|---:|---:|---:|---:|
| 30.0 | 0.0823 | 0.0030 | 27.67 | 51.31 |
| 24.0 | 0.0629 | 0.0029 | 21.98 | 39.16 |
| 22.5 | 0.0605 | 0.0030 | 20.13 | 36.58 |
| 20.0 | 0.0560 | 0.0030 | 18.96 | 34.61 |
| 18.0 | 0.0497 | 0.0030 | 16.68 | 29.65 |
| 15.0 | 0.0409 | 0.0030 | 13.79 | 24.10 |

### Interpretation

**There is a strong non-random phase-lock signal in the chosen SHA observable.**

However, **$H=\pi/9=20^\circ$ is not uniquely selected by this first competition**. On this observable:

- $20^\circ$ is strongly non-random
- but $24^\circ$ and especially $30^\circ$ score even better

So the current status is:

$$
\boxed{\text{SHA has a real phase-lock structure, but this observable does not single out } H=\pi/9 \text{ uniquely.}}
$$

This is still useful. It means the signal is real enough to survive nulls, but the **coordinate choice** is not yet canonically aligned to the claimed $H$-axis.

### Round localization

I also localized lock strength by round for the 20° and 30° quantizers.

- For **20°**, strongest rounds were: 38, 15, 50, 24, 60
- For **30°**, strongest rounds were: 60, 44, 43, 15, 10

Segment aggregation:

| segment | 20° z-score | 30° z-score |
|---|---:|---:|
| early (0–15) | 14.51 | 21.68 |
| mid (16–47) | 25.38 | 37.60 |
| late (48–63) | 15.41 | 24.63 |

So this chosen observable is **not** an early-only waist effect. It is distributed, with strongest concentration in the mid rounds.

## B. Twin-prime subtype-entropy / evenness test

### Setup

I generated primes up to
$$
N = 2,000,000
$$
and extracted twin-prime starts $p$ such that $(p,p+2)$ is a twin pair.

I used wheel depth
$$
W = 210
$$
with the exact admissible twin residues
$$
S_{210}(2) = \{11,17,29,41,59,71,101,107,137,149,167,179,191,197,209\},
$$
which are the standard 15 twin subtypes mod 210.

For windows of width
$$
210,\ 420,\ 630
$$
stepped by 210, I computed:

- twin density = twin count / admissible candidate count
- subtype entropy
- subtype **evenness**
  $$
  J = \frac{H}{\log k_{occ}}
  $$
  where $k_{occ}$ is the number of occupied subtype bins in that window

This was to remove the trivial effect that more twins automatically raise raw entropy.

### Results

| width | windows | corr(evenness, density) | low-Q density | high-Q density | ratio |
|---:|---:|---:|---:|---:|---:|
| 210 | 7757 | 0.777 | 0.0667 | 0.1584 | 2.38 |
| 420 | 9213 | 0.542 | 0.0805 | 0.1069 | 1.33 |
| 630 | 9453 | 0.328 | 0.1009 | 0.0873 | 0.86 |

### Interpretation

The raw subtype-entropy observable is **too confounded by count** to trust directly. Even after switching to evenness:

- the correlation is positive at widths 210 and 420
- but it weakens substantially by width 630
- and by 630 the top-quartile evenness windows are actually *less* dense than the bottom quartile

So the honest status is:

$$
\boxed{\text{the first aligned twin-prime test is suggestive at small windows, but not yet stable enough to count as a confirmed signal.}}
$$

That is still an improvement over the earlier generic-compression proxy, because this test is now actually aligned to the wheel/subtype structure. But it is **not** a locked result yet.

## Bottom line

### Closed from this run

1. The SHA phase observable shows a **real, strong non-random quantization structure** under null comparison.
2. The twin-prime aligned wheel test gives a **nontrivial but unstable** signal.

### Not yet closed

1. $H=\pi/9$ is **not uniquely selected** by the present SHA observable.
2. The twin-prime information-density claim is **not yet stable** across window scales.
3. The transformer residual-$H$ protocol remains unrun because there are no internal activations available in this runtime.

## Files

- `sha_quantizer_competition.csv`
- `sha_lock_strength.csv`
- `sha_round_lock_20deg.csv`
- `sha_round_lock_30deg.csv`
- `twin_prime_evenness_summary.csv`
- `sha_quantizer_competition.png`
- `sha_round_localization.png`
- `twin_prime_evenness_density.png`
