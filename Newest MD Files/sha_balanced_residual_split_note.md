# SHA Balanced Residual Split Note

## Core observation

The remaining depth-8 genesis twin is not a random false path.  
It is a **balanced residual split** of the same fused wall.

Let the two surviving round-56 pairs be

$$
(W_{56}^{(0)}, h_{56}^{(0)})
=
(\texttt{0x6ec7e42f},\ \texttt{0x4d8edce6})
$$

and

$$
(W_{56}^{(1)}, h_{56}^{(1)})
=
(\texttt{0x6ecee42f},\ \texttt{0x4d87dce6})
$$

Then:

$$
W_{56}^{(0)} \oplus W_{56}^{(1)} = \texttt{0x00090000}
$$

$$
h_{56}^{(0)} \oplus h_{56}^{(1)} = \texttt{0x00090000}
$$

but also

$$
W_{56}^{(1)} - W_{56}^{(0)} = \texttt{0x00070000}
\pmod{2^{32}}
$$

$$
h_{56}^{(1)} - h_{56}^{(0)} = \texttt{0xfff90000}
\pmod{2^{32}}
$$

and the fused-wall sum is preserved exactly:

$$
(W_{56}^{(0)} + h_{56}^{(0)}) \bmod 2^{32}
=
(W_{56}^{(1)} + h_{56}^{(1)}) \bmod 2^{32}
=
\texttt{0xbc56c115}
$$

## Interpretation

This means the false twin survives because it performs an **equal-and-opposite transfer inside the same local reflection class**.

The transfer preserves:

- the fused-wall sum,
- the $h$ Hamming weight,
- the $h$ nibble silhouette.

But it does **not** preserve chirality.

True path:
$$
h\text{-chirality} = (9, 9)
$$

False twin:
$$
h\text{-chirality} = (10, 8)
$$

So the twin is invisible to a bundle that only sees

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

but becomes visible once either

$$
\text{h chirality}
$$

is added, or the chain is extended one more round.

## Why nibble reflection allows the twin

The residual perturbation is concentrated in a single nibble-weight class.

The XOR pattern

$$
\texttt{0x00090000}
$$

has Hamming weight $2$ inside the affected nibble band. That means the local nibble population can remain unchanged even while phase-handedness shifts.

So the twin is best understood as

$$
\text{same local mass}
\;+\;
\text{same local nibble shape}
\;+\;
\text{different phase-handedness}
$$

This is exactly the kind of residual ambiguity that a **combination lock** can temporarily tolerate but a deeper chain kills.

## Working lemma candidate

A plausible next lemma is:

> If two local splits of the same fused wall preserve nibble reflection and Hamming mass but differ by a balanced phase-handed transfer, then they may survive shallow local matching but cannot both remain extendable under deeper lawful recursive coupling.

This is not yet a general theorem, but it is the exact pattern observed in the current hardest tested case.

## Updated practical consequence

The current best minimal local bundle remains

$$
\boxed{\text{mask nibble silhouette} + \text{h nibble silhouette}}
$$

with the final residual tie-break supplied by either

$$
\text{h chirality}
$$

or

$$
\text{one more round of lawful recursive coupling}
$$
