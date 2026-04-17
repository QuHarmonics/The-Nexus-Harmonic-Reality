# SHA Minimal Closure Law — Continuation Note

## Main result

The current trajectory can now be stated more sharply.

For the tested real Bitcoin headers, the bundle

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

is already strong enough to force a **unique lawful chain by shallow depth**.

## Minimal collapse depths

| Header | Bundle | First depth with exactly 1 true survivor | Depth trace |
|---|---|---:|---|
| block_328734 | mask_nib | None | 8:8, 9:128, 10:64, 11:64, 12:16 |
| block_328734 | mask_nib+h_nib | 8 | 8:1, 9:2, 10:1, 11:1, 12:1 |
| block_328734 | mask_nib+h_nib+h_chir | 8 | 8:1, 9:1, 10:1, 11:1, 12:1 |
| genesis | mask_nib | None | 8:32, 9:8, 10:8, 11:32, 12:128 |
| genesis | mask_nib+h_nib | 9 | 8:2, 9:1, 10:1, 11:1, 12:1 |
| genesis | mask_nib+h_nib+h_chir | 8 | 8:1, 9:1, 10:1, 11:1, 12:1 |

The key row is:

- **genesis / mask_nib+h_nib**: depth trace `8:2, 9:1, 10:1, 11:1, 12:1`

So the only residual ambiguity in the hardest tested case disappears after **one more round of lawful recursive coupling**.

## Genesis residual twin structure

At depth $8$, the two remaining genesis survivors under

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

differ only at round $56$:

- $W_{56}^{(0)} = \texttt{0x6ec7e42f}$
- $W_{56}^{(1)} = \texttt{0x6ecee42f}$

and their paired $h_{56}$ values are:

- $h_{56}^{(0)} = \texttt{0x4d8edce6}$
- $h_{56}^{(1)} = \texttt{0x4d87dce6}$

The residual twin has a striking symmetry:

$$
W_{56}^{(0)} \oplus W_{56}^{(1)} = \texttt{0x00090000}
$$

$$
h_{56}^{(0)} \oplus h_{56}^{(1)} = \texttt{0x00090000}
$$

and the fused-wall sum is preserved exactly:

$$
(W_{56}^{(0)} + h_{56}^{(0)}) \bmod 2^{32} = (W_{56}^{(1)} + h_{56}^{(1)}) \bmod 2^{32}
$$

In the actual data, this equality is `True`.

So the false twin is not a random near miss. It is a **balanced residual split** of the same fused wall.

## Why the false twin dies

When the chain is extended one more round, the two depth-8 survivors behave differently:

| Residual path | $W_{56}$ | lawful round-55 extensions | sample $W_{55}$ |
|---:|---|---:|---|
| 0 | `0x6ec7e42f` | 1 | `0x847d44e1` |
| 1 | `0x6ecee42f` | 0 | — |

So one path remains extendable and the other becomes **non-extendable** under the same proxy basis.

## Strongest current reading

The local crystal identity now appears to live at the level of:

$$
\boxed{\text{mask nibble silhouette} + \text{h nibble silhouette}}
$$

with the final tie-break supplied by either:

$$
\text{h chirality}
$$

or

$$
\text{one more round of recursive coupling}
$$

## Working theorem target

A clean next theorem target is:

$$
\text{For the tested real headers, }
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
\text{ collapses to a unique lawful chain by depth }9.
$$

This is stronger than a ranking claim. It is a **constructive shallow-depth closure claim**.