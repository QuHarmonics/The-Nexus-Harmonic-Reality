# NEXUS — Turning a transformation into unique data

**Question.** Can the route of a transformation be represented as unique, recoverable data without encoding only the final readout and without using a digest?

## Keep the layers separate

1. **Route:** the ordered transformations, their types, parameters, and return/inverse information.
2. **Composed map/readout:** what the route does when composed. Different routes may produce the same map.
3. **Wrapper/context:** the higher-level relation that places the route within a wider structure. It remains above the compiler-route layer rather than silently folded into it.

The representation should encode the route's structure, not a recorded trajectory of materialized state values.

## Reversible route code

For a declared finite primitive vocabulary, assign every primitive a distinct opcode. A route with `n` operations can be serialized as:

`ROUTE:v1:` + `1` repeated `n` times + `0` + the `n` opcode tokens in order.

The unary prefix carries the route length; after reading it, the decoder knows exactly how many fixed-width opcode tokens follow. The encoding can therefore be decoded without ambiguity. For parameterized operations, each token needs a type identifier and a self-delimiting canonical encoding for its parameters. The header must identify the opcode vocabulary/version and the route's input/output types.

This is injective by construction: distinct opcode sequences receive distinct encodings. It is reversible and variable-length; it is not a fixed-width fingerprint.

## Exact toy run

To honour the NEXUS way-home rule, the toy uses only reversible primitives on the state set `{0,1,2}`:

- `I`: identity
- `A`: swap 0 and 1
- `B`: swap 1 and 2

Each primitive is its own inverse. The inverse route is obtained by reversing the token order and replacing each token with its inverse. All routes of length 0 through 5 were enumerated; every code was unique, every code decoded to its original route, and every route followed by its inverse returned every state home.

| Exact check | Result |
|---|---:|
| Routes enumerated | 364 |
| Unique route encodings | 364 |
| Route decode round-trips | all pass |
| Route followed by inverse returns every state | all pass |
| Distinct composed maps | 6 |
| Route histories collapsed if only the composed map is kept | 358 |

Two witnesses:

- `I` and `A;A` both compose to the identity map, but their route codes differ.
- `A;B;A` and `B;A;B` both compose to the same swap, but their route codes differ.

The six possible resulting permutations are the six map-level fibers; within each fiber many distinct routes land on the same composed map. The route code preserves those histories rather than folding them together.

## What the test means

**RUNS:** the serializer is injective over the declared routes; decoding is exact; inverse routes restore every state.

**Structural landing:** unique route data must preserve the ordered transformation tokens (and their parameters/types/return information), not only the endpoint or composed map. In this toy, a map-only encoding collapses 358 route identities; a route encoding collapses none.

**OPEN — identity across representations:** uniqueness is always relative to a declared primitive vocabulary and route-identity rule. If two different descriptions should count as the same transformation, an explicit rewrite/equivalence system must say so. Until that is defined, merging distinct histories would silently destroy the very information the map is intended to preserve.

**OPEN — full NEXUS encoding:** the six proposed verbs MARK, COMPARE, CARRY, HOLD, ROUTE, CLOSE need formal opcode semantics, typed inputs/outputs, parameter grammar, and inverse/return encoding. The toy proves the serialization principle, not that the six-verb basis is complete or minimal.

**Boundary:** put the route and its typed interface on the compiler layer. Encode wrapper/context as a separate higher-layer relation referring to the route.

## Next derivation

Specify each NEXUS primitive as a typed reversible write; define how its inverse or way-home reference is represented; then define which rewrites preserve route identity and which preserve only composed-map identity. Only after that can the general NEXUS route be encoded in unique data without choosing arbitrary representatives.
