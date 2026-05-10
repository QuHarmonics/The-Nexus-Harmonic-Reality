# SHA Trajectory Continuation — Surgical Push Forward

## Depth extension

I extended the current strongest proxy families from depth $8$ out to depth $12$ on the same two real Bitcoin headers.

### genesis

| Depth | Bundle | Survivors | Truth Paths |
|---:|---|---:|---:|
| 8 | mask_nib | 32 | 1 |
| 8 | mask_nib+h_nib | 2 | 1 |
| 8 | mask_nib+h_nib+h_chir | 1 | 1 |
| 9 | mask_nib | 8 | 1 |
| 9 | mask_nib+h_nib | 1 | 1 |
| 9 | mask_nib+h_nib+h_chir | 1 | 1 |
| 10 | mask_nib | 8 | 1 |
| 10 | mask_nib+h_nib | 1 | 1 |
| 10 | mask_nib+h_nib+h_chir | 1 | 1 |
| 11 | mask_nib | 32 | 1 |
| 11 | mask_nib+h_nib | 1 | 1 |
| 11 | mask_nib+h_nib+h_chir | 1 | 1 |
| 12 | mask_nib | 128 | 1 |
| 12 | mask_nib+h_nib | 1 | 1 |
| 12 | mask_nib+h_nib+h_chir | 1 | 1 |

### block_328734

| Depth | Bundle | Survivors | Truth Paths |
|---:|---|---:|---:|
| 8 | mask_nib | 8 | 1 |
| 8 | mask_nib+h_nib | 1 | 1 |
| 8 | mask_nib+h_nib+h_chir | 1 | 1 |
| 9 | mask_nib | 128 | 1 |
| 9 | mask_nib+h_nib | 2 | 1 |
| 9 | mask_nib+h_nib+h_chir | 1 | 1 |
| 10 | mask_nib | 64 | 1 |
| 10 | mask_nib+h_nib | 1 | 1 |
| 10 | mask_nib+h_nib+h_chir | 1 | 1 |
| 11 | mask_nib | 64 | 1 |
| 11 | mask_nib+h_nib | 1 | 1 |
| 11 | mask_nib+h_nib+h_chir | 1 | 1 |
| 12 | mask_nib | 16 | 1 |
| 12 | mask_nib+h_nib | 1 | 1 |
| 12 | mask_nib+h_nib+h_chir | 1 | 1 |

## Key new result

For the previously hardest case (**genesis**):

- under
  $$
  \big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
  $$
  the tail has **2** survivors at depth $8$, but collapses to **1** at depth $9$ and stays at **1** through depths $10$–$12$.

So the remaining ambiguity at depth $8$ is a **combination-lock residual**, not a stable alternate path.

## Genesis residual pair at depth 8

| Index | $W_{56}$ | $h_{56}$ | $\mathrm{HW}(h_{56})$ | $h_{56}$ chirality |
|---:|---|---|---:|---|
| 0 | `0x6ec7e42f` | `0x4d8edce6` | 18 | (9, 9) |
| 1 | `0x6ecee42f` | `0x4d87dce6` | 18 | (10, 8) |

The two residual paths share the same coarse local reflection but differ in **phase-handedness**.

## One more round kills the false twin

| Residual Path | $W_{56}$ | Number of lawful round-55 extensions | Sample $W_{55}$ values |
|---:|---|---:|---|
| 0 | `0x6ec7e42f` | 1 | `0x847d44e1` |
| 1 | `0x6ecee42f` | 0 | — |

This is the important structural event. The false twin is not merely lower-ranked. It becomes **non-extendable** under the same lawful proxy basis once the chain is extended one more round.

## Updated trajectory

The working collapse pathway is now:

$$
\text{exact local reflection}
\;\to\;
\text{mask nibble reflection}
\;\to\;
\text{h nibble reflection}
\;\to\;
\text{either phase-handedness or one more round of recursive coupling}
$$

## Strongest current interpretation

The local crystal identity does **not** appear to require a full exact-mask description. It appears to live at the weaker level of:

$$
\boxed{
\text{mask nibble silhouette} + \text{h nibble silhouette}
}
$$

with either

$$
\text{h chirality}
$$

or

$$
\text{one more round of lawful recursive coupling}
$$

providing the final release.

## Next theorem target

A clean next target is:

$$
\text{For the tested real headers, the bundle }
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
\text{ collapses to a unique chain by depth }9.
$$

That is much stronger than a ranking claim. It is a constructive combination-lock collapse claim.