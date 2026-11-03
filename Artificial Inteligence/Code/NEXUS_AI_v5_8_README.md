# NEXUS AI v5.8 — Immutable-Ring Stabilizer Quotient

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828

## Run

Open `NEXUS_AI_v5_8_Unified.ipynb` in Jupyter. Run the first code cell, then the read-only demonstration cell. The final Gemma cell is optional and only works if LM Studio serves a loaded model at localhost:1235. Standard-library Python 3.10+.

This notebook is complete: it contains the actual v5.7.1 engine and all prior layers, plus the v5.8 quotient. It does not require the older notebooks to be executed first. It preserves the established ledger replay. For a clean, isolated run, use a fresh directory; on your original machine, keep it alongside your existing ledgers if continuity is desired.

## Mathematical reduction

When a complete pair state is fixed by the exact reader-exchanging symmetry tau = H_h Phi_phi J_swap, reader B is determined by A:

pB = Phi_phi(pA) XOR h;  wB = phi(wA); D[Phi_phi(q) XOR h] = phi(D[q]).

The exact quotient stores (pA,wA) plus one field word per orbit of q -> Phi_phi(q) XOR h. It handles simultaneous reads and XOR writes, including coincident readers and fixed field cells. Every update has an exact inverse with no saved history.

Scope: two readers and their retained field in one eight-word K carrier coset, K-valued carries/field words, with the entire provided source satisfying tau. Invalid or missing stabilizers are UNLINKED/UNBOUND, never silently projected.

The ring itself is immutable. The quotient changes the representation used by its reader/field transition, not the ring or its partner law.

## Corrected state count

For the documented 806-tick seed at width 4, phi=A and h=u. There are four 2-cell field orbits, each with 3 independent K bits, plus 3 bits for pA and 3 for wA: 18 raw independent bits. The conserved charge fixes one parity in this stabilizer subspace, leaving 17 bits for this charge slice. Exhaustive counting yields 131,072 states on that fixed-charge slice. This corrects the earlier unsupported 15-bit count.

## Verification

88,620 deterministic checks across widths 4,6,8,10,12,14,16, covering all 20 stabilized canonical seeds at each width, populated symmetric fields, translations into another coset, native-equivalence, exact reversal, and the supplied 806-step witness. Initialization retains all earlier deterministic suites.

The existing two-argument LM Studio `nexus_pair_carrier_symmetry_goal` is enriched with `stabilizer_quotient`; it does not require any new arguments or change the live machine.

## Status

RUNS: exact stabilizer quotient, forward/inverse and comparison with full paired machine; known 806 witness lands in reduced engine.
STANDS: quotient algebra and conserved-charge parity relation.
OPEN: derive unknown vacuum-return depths from initial boundary, and cross-carrier release under a new port law. Neither is claimed solved.

Prediction SHA-256 (before the independent v5.8 native readout): `715e120ab4dcb09bea72be9ab6e448834ed5f1e13c598a6fd83d195d072778df`.
