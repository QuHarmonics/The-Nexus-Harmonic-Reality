# NEXUS Interactive Observatory

[Live portal](https://quharmonics.github.io/The-Nexus-Harmonic-Reality/) · [Original Ring Atlas](https://github.com/QuHarmonics/The-Nexus-Harmonic-Reality/blob/979ee0ee2fc971d622848aba7fc2fbd2fcedb2b5/The%20Nexus%20Domain/Code/NEXUS_Ring_Atlas.ipynb) · [Atlas guide](../ATLAS.md) · [Research-first licensing](../../LICENSE.md)

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828.

This is a dependency-free JavaScript implementation of selected mathematical instruments, not a replacement of the fifteen-chapter original Atlas. Browser values are executed locally. The source notebook's original Git blob is a9154bbbe38a26fbb35905c2760ea7547f385301; SHA-256 e0884d0b912d25a627a06b462b627fee114629edde94006d8790869471bf7cc2.

| Instrument | Contract | Return / limitation |
| --- | --- | --- |
| Address codec | Atlas chapters 2–4, mirror-pair rank and seam | Exact BigInt address/word inverse through 64-bit UI; inverse is rank-directed bisection, not exhaustive enumeration. |
| Nested reader | Chapters 3, 8: radial angle, tape windows | Exact slot/slice at integer multiples of 1/4096 turn. Ring diagram is illustrative radial-band bit encoding. Tape loss is measured by distinct windows, not a new derivation of every formula. |
| Inverter clock | Chapter 10, left rotate XOR 1 | Exact inverse and orbit census; discrete spin projection, no physical frequency claim. |
| Retained field | Chapter 11, single reader and field | Inverse from complete state. Carrier dimension gives the class. The 43,155,322-tick return is a source-recorded result; not run by this UI. |
| Directed port | Chapter 12, joint old-field read then XOR writes | Derived third-reader initial state for target and fixed tick 3; forward landing may fail if the added reader changes the base trace. Full inverse is always checked. |
| Contract compiler | Arithmetic contract split and carry composition | Three monotone R2 carry words; balanced decomposition is an implementation choice. Not a general synthesis theorem. |
| Clause boundary | Local three-variable clauses, two-variable interfaces | Four exact persistent counts; generated deterministic examples, not the historical Entry 136 instance or a general SAT result. |

| Wrapping square | Circular tape `00011011`, exact window extension, nibble exchange and reversal | The tape is the observed concatenation `00|01|10|11`, not the Atlas's seam-exchanged R2 ordering. The four-word relation and transport/perturbation contrast are demonstrated on the specified source; arbitrary nonlinear computations do not follow from it. |

## Verification scope

Run `node tools/verify_observatory.mjs` in the repository. The audit checks the exact ring order digest from the original Atlas, every address and inverse at widths 1–9, selected 64-bit source vectors, the width-nine orbit census, the target-5 port witness and joint inverse/charge laws, complete small reader states, small carry composition trees and generated local clauses against exhaustive counts. These are source-equivalence and finite execution checks, not independently sealed new predictions.

The original Atlas is unmodified. The current compiler instruments are independent, scoped implementations of the mathematical interfaces discussed in current work; complete general method-to-ring synthesis and unrestricted SAT remain OPEN. No public claim about prior scientific priority is established by this observatory.
