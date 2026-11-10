# Hole 3: schedule-tail ROBDD binding contract

## Typed object

Define `C(H) = TailRelation(H) AND PadValid(B) AND DigestClosure(H0, B)` with the following actual handles supplied by the caller:

- `manager`: the existing ROBDD manager / variable universe;
- `tail_relation`: Boolean BDD for the backward schedule relation and tail-to-512-bit-block/ring-coordinate bijection;
- `pad_valid`: BDD over exactly the block/message variables used by `tail_relation`;
- `digest_closure`: BDD for the target digest/compression closure equations using the same symbolic state variables or an explicit variable map;
- `region`: optional ring-address cofactor for the region being pruned.

Conceptual wiring (API-agnostic):

```python
C = manager.and_all(tail_relation, pad_valid, digest_closure)
C_region = manager.and_(C, region) if region is not None else C
```

This is only an interface contract, not runnable implementation; the actual ROBDD API and variable IDs were not supplied.

## Required checks before status can become RUNS

1. **Variable identity:** prove the schedule-tail variables map bijectively to the intended block/ring variables; do not silently create duplicate variables.
2. **Constraint equivalence:** prove `C` represents the same valid assignments as the original message, padding, schedule, and digest equations.
3. **No lost solutions:** every original satisfying assignment must extend to a satisfying assignment of `C`, and conversely after projection to message variables.
4. **Cofactor preservation:** each region split must satisfy `C == OR_regions cofactor(C, region)` for a disjoint exhaustive region partition.
5. **Effect measurement:** compare ROBDD node counts before and after the tail constraints under the same variable ordering, with the same preprocessing and memory/time accounting.

The provided bundle does not include `cofactor_inverse_bdd.py`, its API, the SHA schedule BDD, `PadValid`, or digest closure predicates. Therefore the named certificate is **BOUND**, while the implementation wiring is **OPEN**. No reduction claim is made.
