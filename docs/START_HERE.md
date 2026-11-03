# Start here: a reading path through NEXUS

The NEXUS archive is not ordered by difficulty or publication date. These entry points help readers follow the *dependency chain* instead of searching through the entire historical corpus.

> C1: **All things must change.** The research asks which operations and return structures are forced when continuation and reversibility are kept in view.

## Route A — Understand the mathematical core

1. **The ring / fixed mold.** Begin with the partner relation between bit reversal and complement; understand why every word has a partner and an address. Search the [published papers](../Published%20Papers%20PDF) for *Against Its Own Reverse*, *Mapping the Nested Partner Ring*, and *Where Yes and No Become Maybe*.
2. **The clock.** *One Inverter* develops the fixed-point-free one-bit loop, its parity and the distinction between running clocks and locks.
3. **The retained step.** *Retained Continuation* introduces a reader at a position, a carry, and a writable field that preserves the history of the route.
4. **The exact inverse.** *Exact Algebra of Retained Continuation* formalizes single- and multi-reader reversal, return symmetries, and collision invariants.
5. **The unified domain.** *The Retained Continuation Domain* collects the ring, clock, step, closures, collisions, ports and read models with explicit status labels.

Not all of these newer titles have been copied to the current repository. When missing, consult the [public Drive archive](https://drive.google.com/drive/folders/1MQePNhpBUV-9UVLTq1CIOixxYLg3RgLq?usp=sharing), [Academia profile](https://independent.academia.edu/ClaudReins), or the published DOI record.

## Route B — Run the machine

- Explore the [Python programs](../Python%20Code) and [newer notebooks](../Jupyter-Notebooks-Newest).
- Look for self-contained verification scripts, stated seeds, expected periods and assertion counts.
- Read the execution trace *and* the correction log. A code run establishes its observed scope, not every interpretation later attached to it.
- The NEXUS AI notebooks use a local language model as a client of a deterministic reversible kernel. The model is not itself the proof provider.

## Route C — Browse applications

- **SHA-256:** forward schedules, inversion structure, trace constraints, candidate-vs-route distinction.
- **AI / compiler:** reversible state, BIND, provider ownership, switch-tape reconstruction.
- **Numbers / spectral work:** BBP, primes, Riemann-related operator experiments.
- **Matter / physical readings:** atomic shells, geometry, retained-field analogies and comparator models.

Applications should retain the same core status grading: **STANDS**, **RUNS**, **OPEN**, **DEAD END**, **PULL**.

## How to cite a result

Prefer the DOI of the precise published paper and version. For a code-derived claim, include the repository path, commit, exact command, input seed and readout. Do not substitute a generic NEXUS citation for a specific computation.

The [repository map](REPOSITORY_MAP.md) explains how the existing archive will be cataloged without erasing earlier iterations.