# SHA / Bitcoin Branch Split Note

## What widened testing changed

The broader sweep shows that `two survivors` is **not** a single phenomenon.

There are at least **two different branch species** under the coarse bundle

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big).
$$

## Branch A — runtime reflection twins

These are the pairs that satisfy:

$$
\Delta W_t = \Delta h_t
$$

with

$$
\text{single-nibble} + \text{weight-2} + \text{mixed-parity}
$$

and they differ in chirality.

These are genuine coarse-fiber reflections: the coarse bundle identifies the pair, but chirality separates it.

| Header | Depth | Round | Delta | Chirality-added survivors | One-round-deeper survivors |
|---|---:|---:|---|---:|---:|
| genesis | 8 | 56 | `0x00090000` | 1 | 1 |
| block_100000 | 3 | 61 | `0x000c0000` | 1 | 2 |
| block_154595 | 4 | 60 | `0x00006000` | 1 | 1 |
| block_154595 | 11 | 53 | `0x00030000` | 1 | 1 |
| block_328734 | 9 | 55 | `0x06000000` | 1 | 1 |
| block_894470 | 5 | 59 | `0x00000006` | 1 | 1 |
| block_894470 | 11 | 53 | `0x90000000` | 1 | 2 |
| block_894470 | 12 | 52 | `0x0000c000` | 1 | None |

Immediate read:

- total reflection-twin cases: **8**
- all are killed by adding chirality: **True**
- killed one round deeper in all observed cases: **False**

That last line is **false**: some reflection twins survive one round deeper. So chirality is the cleaner splitter than depth.

## Branch B — coarse alias pairs

These are the pairs that do **not** match the reflection species.

Typical properties:

- $\Delta W_t \neq \Delta h_t$, or
- not single-nibble, or
- not weight-2, or
- chirality does **not** distinguish them.

These are not simple runtime reflections. They are a different alias mechanism.

| Header | Depth | Round | DeltaW | DeltaH | Chirality-added survivors | One-round-deeper survivors |
|---|---:|---:|---|---|---:|---:|
| block_100000 | 2 | 62 | `0x000001e0` | `0x000000a0` | 2 | 2 |
| block_100000 | 4 | 60 | `0x00000000` | `0x00000000` | 1 | 1 |
| block_277316 | 7 | 57 | `0xf0000000` | `0x50000000` | 2 | 2 |
| block_277316 | 8 | 56 | `0x40000000` | `0x00000000` | 2 | 1 |

Immediate read:

- total coarse-alias cases: **4**
- killed by chirality in all cases: **False**
- killed one round deeper in all cases: **False**

Both of those lines are **false**. These aliases require a different refinement law.

## Strongest current correction

The earlier path was too compressed. The correct branch picture is now:

$$
\text{coarse 2-survivor event}
\;\to\;
\begin{cases}
\text{runtime reflection twin} & \text{(chirality splits)}\\
\text{coarse alias pair} & \text{(chirality may fail)}
\end{cases}
$$

So the tested law is no longer

$$
\text{all twins die by chirality or one more round}
$$

but rather

$$
\text{all observed reflection twins die by chirality, while other coarse aliases still exist}
$$

## What this means for the path

This is still progress.

It means the live object is not a single residual species, but a **branching residual taxonomy**.

The next proof target becomes:

1. characterize Branch A cleanly as runtime reflection,
2. characterize Branch B as a different coarse alias class,
3. find the next invariant that kills Branch B.
