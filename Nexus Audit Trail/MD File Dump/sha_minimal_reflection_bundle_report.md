# Minimal Reflection Bundle Continuation

## Core result

The next code pass found the smallest currently known bundle that closes the tested 8-round tail:

$$
B_t^\star
=
\big(
\text{mask nibble silhouette},
\ \text{h nibble silhouette},
\ \text{h chirality}
\big)
$$

For the two real Bitcoin headers tested, this bundle gives:

- **genesis**: exactly **1** surviving chain across rounds $56..63$
- **block 328734**: exactly **1** surviving chain across rounds $56..63$

## Intermediate result

Using only

$$
\big(
\text{mask nibble silhouette},
\ \text{h nibble silhouette}
\big)
$$

we get:

- **block 328734**: already collapses to **1**
- **genesis**: collapses to **2**

So the remaining ambiguity in the hardest tested case is not mass and not nibble shape.

It is **phase-handedness**.

## Genesis residual twin

For genesis at depth 8, the two surviving chains under

$$
\big(
\text{mask nibble silhouette},
\ \text{h nibble silhouette}
\big)
$$

differ only at round $56$:

$$
W_{56}^{(0)} = \texttt{0x6ec7e42f}
$$

$$
W_{56}^{(1)} = \texttt{0x6ecee42f}
$$

with

$$
W_{56}^{(0)} \oplus W_{56}^{(1)} = \texttt{0x00090000}.
$$

The two survivors have:

- the **same** $h$-Hamming weight,
- the **same** $h$-nibble silhouette,
- but **different** $h$-chirality.

True path:
$$
h\text{-chirality} = (9,9)
$$

False twin:
$$
h\text{-chirality} = (10,8)
$$

So the final tie-breaker is **chirality**.

## Interpretation

This materially sharpens the trajectory.

The active local crystal now appears to be readable in a weaker basis than exact staged masks. The best current candidate is:

$$
\boxed{
\text{mask nibble silhouette} + \text{h nibble silhouette} + \text{h chirality}
}
$$

This suggests the local lock is not fundamentally a full-bit mask object. It is closer to a **nibble reflection + phase-handedness object**.

## Updated trajectory

The program now appears to move like:

$$
\text{exact local reflection}
\;\to\;
\text{nibble-preserving proxy reflection}
\;\to\;
\text{phase-handedness tie-break}
$$

That means the remaining hard problem is no longer local uniqueness itself.

The remaining hard problem is:

$$
\boxed{
\text{how to derive this minimal reflection bundle from admissible side geometry alone}
}
$$

## Next target

The next clean formal object is:

$$
\Sigma_{t,j} = (c_{t,j}, q_{t,j}, s_t, m_t)
$$

but with the local bundle $q_{t,j}$ now biased toward:

1. mask nibble silhouette,
2. $h$ nibble silhouette,
3. $h$ chirality.

This is the strongest current candidate for the **native reflection basis** of the local lock.
