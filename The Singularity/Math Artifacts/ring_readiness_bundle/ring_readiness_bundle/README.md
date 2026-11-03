# Ring readiness and fold replication — §20 and §21 of the Compiler Rings log

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828 · 2026-10-20

Run from this folder: `python3 -I fold_replicate.py` (U1–U5, seal `seal_folds.txt`) and `python3 -I readiness_ring.py` (RD1–RD3, seal `seal_readiness.txt`). Each script prints the seal hash it reads; the hash is unchanged after the run. Both rely on `wheels.py` beside them.

The two scripts are the run copies with one change: the import path points at this folder instead of `../wheels`.

The printed ledger shows `U2: False` and `U5: False`. Both are explained in §20 of `compiler_rings_log.md`:
- **U2** is notation. The seal wrote the R3 terminal residual as the bits `000`; the script compares it with the hex print `0`. The chain values are identical.
- **U5** is a DEAD END on the extrapolated clause "every frame from 2 up is incomplete". Frame 2 is complete for every L = 6–16; frames 0 and 1 and the frame-1 owner all ran as sealed.
