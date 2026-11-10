# NEXUS dual-layer stack and route-reader test

**Status: RUNS.**

## Stack descent
Built the dyadic stack `64 → 32 → 16 → 8 → 4 → 2 → 1`. All 64 leaf addresses round-trip through six branch decisions. At every level, every parent interval is the ordered fusion of two equal-size children; after fusion, the parent occupies the next, larger LEN layer.

## Reader widths
| Reader width | Transfers to receive all 64 payload bits | Decisions to select a chunk | Decisions inside selected chunk to identify one bit | Total address decisions |
|---:|---:|---:|---:|---:|
| 1 | 64 | 6 | 0 | 6 |
| 2 | 32 | 5 | 1 | 6 |
| 4 | 16 | 4 | 2 | 6 |
| 8 | 8 | 3 | 3 | 6 |
| 16 | 4 | 2 | 4 | 6 |
| 32 | 2 | 1 | 5 | 6 |
| 64 | 1 | 0 | 6 | 6 |

The same six address bits can be read as six successive yes/no branch choices. The complete 64-bit payload still requires 64 one-bit transfers on a 1-bit reader; the stack organizes the address/route and payload transfer rather than reducing the payload length.

## Enigma route
`ATTACKATDAWN` → `OFZDNOMXLTCH` → `ATTACKATDAWN` with the same initial settings. Each position supplies a state-conditioned permutation; the route is the succession of rotor states and their transformations.

## SHA-256 transformations stacked by edge
Inserted all 64 SHA rounds in order as size-1 transformation nodes. Equal adjacent top blocks fused online; all intermediate stacks had strictly decreasing LEN from bottom to top and preserved the sum of lengths. At arrival 11 the active stack is `[8, 2, 1]`; at arrival 64 it is `[64]`. There are exactly 63 fusions. Each parent is the ordered composition of its equal-sized children.
Every composite node was checked forward against the corresponding round-trace segment and reversed back to its segment start. The 64-round root matches the forward SHA trace and reverses exactly when the schedule and constants are retained.

## SHA-256 route-back
One-block SHA-256 for `A` produced `559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd` and matched the standard implementation. After removing feed-forward using the known initial chaining value, the nested 64-round composite reversed exactly to the initial chaining value; every `W_t` was recovered from adjacent trace states.

## Structural reading
- **Route:** the six branch bits specify a leaf within the dyadic 64-block.
- **Payload:** the 64 data bits are transmitted at the reader’s width; no address tree compresses that information away.
- **Hold / fusion:** equal-size child blocks meet at a fusion boundary and become one larger-LEN parent. Along one vertical descent, LEN strictly decreases.
- **Enigma → SHA:** transfer state-conditioned transformations and route-back constraints, not Enigma’s exact no-self-letter invariant. SHA rounds are reversible with their drivers retained; the digest alone does not reveal the entire driver route.

## Exact scope
The dyadic address, binary-carry stack invariants, and reader-width checks are exhaustive for a 64-item stack. The SHA nested composite is checked over all 64 actual round nodes for the one-byte message A, with each node compared against its exact trace endpoints. Enigma is tested on one example. These checks do not demonstrate a general SHA preimage attack.
