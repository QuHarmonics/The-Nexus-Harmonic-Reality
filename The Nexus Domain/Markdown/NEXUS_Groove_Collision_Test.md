# NEXUS test — groove, collision, and route reversibility

## Question
Can logic-equivalence, payload collision, reversibility, and change-locality be separated without hashing or measuring a dataset?

## Exact witness

The value-only projection is `sum(a,b)=a+b`. Its inputs `(3,2)` and `(4,1)` both read as `5`. That is a collision in the value channel; it does not make the two input pairs equal.

Retain the carry lane and use the payload-independent reversible transformation

`ADD_HOLD(a,b) = (a+b,b)`.

Then `(3,2) -> (5,2)` and `(4,1) -> (5,1)`, and the inverse `(s,b) -> (s-b,b)` returns each original pair. The route definition is identical for both payloads. The logic stays in one groove while the matter differs.

## Logic collision

`I` and `SWAP;SWAP` are different route histories, but both compose to the identity operator. They occupy the same groove under operator equivalence. If history matters, the route channel keeps their factorisations distinct; the operator channel intentionally identifies them.

## Change locality

Extend the route to `ADD_HOLD(a,b,c) = (a+b,b,c)`. Across all 125 states in `{-2,-1,0,1,2}^3`, the unrelated `C` lane is unchanged. Exact perturbations give dependencies `A -> {A}`, `B -> {A,B}`, and `C -> {C}`. The transformation changes only outputs that its dependency/write rules assign; no unrelated lane is silently rewritten.

## Landing

- **RUNS:** value-only addition merges distinct payloads.
- **RUNS:** keeping the carry makes this transformation reversible and recovers the past input.
- **RUNS:** distinct route factorizations can belong to one operator-equivalence groove.
- **RUNS:** the frame condition holds for the declared unowned lane.
- **OPEN:** generalising this witness to NEXUS's six verbs requires their precise types, write sets, dependencies, composition, and inverse rules.

No cryptographic hash is used as route data or operator representation. This is a small exact witness, not yet the canonical NEXUS grammar.
