NEXUS §126 — ASK THE RINGS: WP5 lockstep joint-orbit reconstruction

This is the corrected continuation from WP5 §121 -> §123 -> §124. The previous §125 SHA/de Bruijn XOR-edge query is kept as a separate exploratory projection and is not treated as the unresolved WP5 link.

Run:
  python nexus_ask_the_rings_lockstep.py

Dependencies: Python 3 standard library only.

Main files:
- nexus_ask_the_rings_lockstep.py: exact CRT joint-orbit reconstruction.
- NEXUS_ASK_THE_RINGS_lockstep_results.json: detailed result, including all nine complete joint orbits.
- NEXUS_ASK_THE_RINGS_lockstep_run.md: human-readable run report.
- NEXUS_running_audit_addendum_126.md: §126 addendum.
- running-audit (11).md: audit continued from §125 to §126.
- NEXUS_ASK_THE_RINGS_lockstep_prediction_2026-10-17.txt/.sha256: pre-run prediction and seal.

Result: 804 eligible lanes reconciled exactly; 692 coprime-period lanes; 112 lockstep lanes; 9 balanced lockstep lanes. All nine paired joint orbits have exact lean zero. Replacing the joint phase route by the full Cartesian product changes the lean in 5/9 of these cases. The general density-of-balance problem remains OPEN.
