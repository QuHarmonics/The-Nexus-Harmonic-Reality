<div align="center">

<sub>QUHARMONICS · CRYPTOGRAPHY</sub>

# Executable work

**SHA-256 reference traces, differential and carry analyzers, symbolic probes, Jacobian calculations, and runnable verification harnesses.**

[← Cryptography](../) · [NEXUS home](../../README.md) · [Papers](../Published%20Papers/) · [Code](../Code/) · [Markdown](../Markdown/) · [Transcripts](../Transcripts/)

</div>

---

> **Collection status:** This directory currently contains its navigation README but no deposited implementation files. The guidance below describes where new material belongs; it does not claim it is already here.

## Purpose

SHA-256 reference traces, differential and carry analyzers, symbolic probes, Jacobian calculations, and runnable verification harnesses. This collection belongs to the **Cryptography** research area and should remain identifiable as that area develops.

## Reproducibility contract

When implementations are added, each project should identify its inputs, environment and dependencies, a runnable entry point, an expected readout, and its scope of testing. A notebook cell output is evidence of the run recorded in that file, not automatically evidence that another machine reproduced it.

Suggested file companions: `README.md`, `requirements.txt` or environment details, tests, prediction seal, execution trace, and correction log. Never quietly repair a mismatch in the reported output. Source code and the published result must remain traceable to one another.

## Reading rule

**Run code before treating a trace as evidence.** A discovered internal symmetry or constraint is not, by itself, an efficient preimage attack, a security break, or a practical cryptanalytic result.

**Research ledger:** **STANDS** = proved identity or external theorem; **RUNS** = executed readout with stated scope; **OPEN** = missing derivation/link; **DEAD END** = observed landing owned elsewhere; **PULL** = external or physical interpretation. These words are not interchangeable.

## In this research area

- Keep the standard algorithm and test vectors explicit.
- Log the exact round, message schedule, and bit-width assumptions.
- Separate structural identities from any claimed practical inversion.
- Retain failed routes and correct the ownership of their readouts.

---

<sub>Research by **Dean A. Kulik** · QuHarmonics Research Group · [Website](https://quharmonics.com/) · [ORCID](https://orcid.org/0009-0003-3128-8828)</sub>
