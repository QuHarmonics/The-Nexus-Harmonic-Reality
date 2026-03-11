# ARX Horizon Combinatorics Audit (LAW_ARX_HORIZON_006)

**Timestamp (UTC):** 2026-01-28T23:14:40Z

This note verifies the exact Hamming-ball basin cardinality and entropy for a 4096-bit space at radius $r=6$.

## Definition

For dimension $N$ and Hamming radius $r$, the closed ball volume is

$$
V(N,r)=\sum_{k=0}^r \binom{N}{k}.
$$

Define basin entropy (bits):

$$
S(N,r)=\log_2 V(N,r).
$$

Fractional tolerance (dimensionless) is

$$
\varepsilon = \frac64096.
$$

## Exact result: $N=4096$, $r=6$

- Exact volume:

$$
V(4096,6) = 6544452312920894465
$$

- Exact entropy:

$$
S(4096,6) = \log_2 V(4096,6) \approx 62.504978170045\ \text{bits}.
$$

- Fractional tolerance:

$$
\varepsilon = \frac{6}{4096} \approx 0.001464843750 \approx 0.146484\%.
$$

## “Dimensional tax” against a 65.1-bit approximation

If a prior approximation gave $S_\text{approx}=65.1$ bits, the multiplicative overestimate factor is

$$
\text{shrink} = \frac{2^{S_\text{approx}}}{V(4096,6)} \approx 6.041982.
$$

So the *exact* basin is about **6.04× smaller** than the 65.1-bit approximation.

## Sweep table: $N\in\{2048,4096,8192\}$, $r\in\{4,5,6,7,8\}$

Columns: $N$, $r$, $100\cdot r/N$ (percent), $S(N,r)$ in bits, and exact integer $V(N,r)$.

|    N |   r |   r_over_N_pct |   S_bits |                           V |
|-----:|----:|---------------:|---------:|----------------------------:|
| 2048 |   4 |      0.195312  |  39.4136 |                732293847553 |
| 2048 |   5 |      0.244141  |  48.0896 |             299508757152257 |
| 2048 |   6 |      0.292969  |  56.5018 |          102032894512403969 |
| 2048 |   7 |      0.341797  |  64.6909 |        29779114853401546241 |
| 2048 |   8 |      0.390625  |  72.6867 |      7601144649614993968385 |
| 4096 |   4 |      0.0976562 |  43.4143 |              11722405098497 |
| 4096 |   5 |      0.12207   |  53.0913 |            9595965398287361 |
| 4096 |   6 |      0.146484  |  62.505  |         6544452312920894465 |
| 4096 |   7 |      0.170898  |  71.6959 |      3824767661079701330945 |
| 4096 |   8 |      0.195312  |  80.6937 |   1955414105242000351926785 |
| 8192 |   4 |      0.0488281 |  47.4147 |             187604202252289 |
| 8192 |   5 |      0.0610352 |  58.0922 |          307258199112615937 |
| 8192 |   6 |      0.0732422 |  68.5066 |       419305084954303813633 |
| 8192 |   7 |      0.0854492 |  78.6983 |    490407335058953610147841 |
| 8192 |   8 |      0.0976562 |  88.6973 | 501809410502206993903334401 |

## Reproducibility script (reference)

```python
import math

def verify_horizon(N=4096, r=6):
    volume = sum(math.comb(N, k) for k in range(r+1))
    entropy = math.log2(volume)
    return volume, entropy

if __name__ == "__main__":
    V, S = verify_horizon(4096, 6)
    print("V =", V)
    print("S =", S)
```

