# SHA Trajectory Continuation — Depth-9 Collapse

## New result

I pushed the chain one round deeper.

For the previously hardest case (**genesis**) under the bundle

$$
B_t = \big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big),
$$

the survivor counts are:

- depth $8$ (rounds $56..63$): **2**
- depth $9$ (rounds $55..63$): **1**
- depth $10$ (rounds $54..63$): **1**
- depth $11$ (rounds $53..63$): **1**
- depth $12$ (rounds $52..63$): **1**

## Interpretation

This means the last apparent ambiguity at depth 8 was **not** a fundamental local wall.

It was a **combination-lock residual**.

In other words:

- at depth 8, the bundle
  $$
  \big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
  $$
  leaves two lawful-looking local continuations for genesis,
- but one more round of recursive coupling collapses the false twin.

So the local phase-handedness tie is real, but it is not globally stable.

## Stronger conclusion

We now have two different routes to uniqueness:

### Route A — local tie-break
Use

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette},\ \text{h chirality}\big)
$$

and the 8-round tail collapses to one immediately.

### Route B — deeper combination lock
Use only

$$
\big(\text{mask nibble silhouette},\ \text{h nibble silhouette}\big)
$$

and let the chain extend one more round:

$$
55..63
$$

Then the false twin dies.

## Updated trajectory

The active picture is now:

$$
\text{mask nibble reflection}
\;\to\;
\text{h nibble reflection}
\;\to\;
\text{either phase-handedness or one more round of combination locking}
$$

That is much stronger than the earlier read.

The remaining wall is therefore even narrower than before.

It is no longer:

$$
\text{find an exact-mask equivalent}
$$

It is closer to:

$$
\text{find the weakest admissible reflection basis that remains stable under one more round of recursive coupling}
$$

## Current best read

The local crystal identity appears to live at the **nibble reflection level**.

The remaining ambiguity at the tail edge is not broad-value ambiguity. It is a **shallow phase residual** that is unstable under deeper lawful chaining.

That means the trajectory is still tightening.
