# Execution audit: the anchor participates in route generation

## Question

Does the declared interpreter make each read affect the next address, and what does the full state graph say about return?

## Fixed test object and semantics

The 64-nibble anchor is held fixed:

`26537e8b759579d1b94e63b65e65c33f8b93d0f4b16f450810230357f1f0fabe`

A state is `(p, r)`, with pointer `p` modulo 64 and register `r` modulo 16. The nibble at `p` is fetched and the explicit instruction table changes the register and/or pointer. The branch instructions test the register entering the tick.

## Direct trace findings

- Route `(0, 0)` and route `(50, 0)` both fetch opcode `2` and apply `r := r + 3 mod 16`, but their next pointers are 1 and 51 respectively.
- On route `(0, 0)`, opcode `e` at pointer 5 sees an odd incoming register and advances to pointer 9. That changes the next fetched instruction relative to a passive one-position scan.
- Route `(50, 0)` wraps from pointer 60 to pointer 1 when opcode `f` sees an odd incoming register.
- Both routes later visit pointer 1, where opcode `6` means XOR 2. At `(1,3)`, it produces `(2,1)`; at `(1,1)`, it produces `(2,3)`. Same address and opcode, different incoming configuration, different successor.

## Exhaustive graph audit

There are `64 × 16 = 1,024` possible states. Enumerating all transitions gives:

| Quantity | Result |
|---|---:|
| Distinct states that occur as successors | 856 of 1,024 |
| Transition map bijective? | No |
| States with 0 predecessors | 168 |
| States with 1 predecessor | 696 |
| States with 2 predecessors | 152 |
| States with 3 predecessors | 8 |
| Directed cycles | 6 |
| Cycle lengths | four cycles of length 38; two of length 76 |
| States lying on cycles | 304 |
| States outside cycles | 720 |

The orbit from `(0,0)` has a one-step preperiod then enters a 38-state cycle. The orbit from `(50,0)` is on a 76-state cycle from its initial state.

## Interpretation in the model

**RUNS:** this declared reader is state-conditioned execution, not static substring selection. The fetched symbol affects the working state and, for branch operations, that state affects the next address. The anchor and execution rules jointly generate the route.

**OPEN / return condition:** this particular transition map is not bijective. Since multiple configurations collapse onto the same successor and 168 states have no predecessor, the present machine cannot provide a unique inverse for every state. That is a property of this declared interpreter, not a refutation of the broader claim that computation is transformation. A return-preserving construction needs a transition rule whose complete state update preserves the information needed to recover its predecessor—not merely a reversible register operation in isolation.

The experiment demonstrates the route/state coupling for this interpreter. It does not establish that the chosen opcode table is uniquely forced by the anchor or that every route universally has a reader.
