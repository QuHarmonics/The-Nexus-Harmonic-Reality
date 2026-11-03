Mapping the Nested Partner Ring - run bundle
Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828. October 2026.

paper/      Mapping_the_Nested_Partner_Ring.docx (and PDF), build_map.js, figures.py, figs/
atlas/      seals (seal_*.txt, *.sha256), the scripts that verify them, outputs and JSON results
wheels/     wheels.py, the ring library (rank, unrank, ring_arrays) every script imports
compiler_rings_log.md   running log; sections 23-26 cover this bundle

Seals (SHA-256 of the seal file, hashed before each run; each runner rechecks it before and after):
  seal_frames.txt    deea12785b7254d12f0414692e6c76a887a6206b23f59f880e9abacd36459775  frame law, L = 17-22 fresh   RUNS
  seal_readers.txt   b41403660526c910f6e1b560a378d43446fac013b748c20f61794b4e50961623  reader atlas RA1-RA6       RA1-3, RA6 RUN; RA4, RA5 DEAD END
  seal_readers2.txt  acb799a49ce209b0b62b8534364795ff5c3faca34480d13c60b0e50b8a40d626  readers at n = 17-19      face, successor, partner RUN; k fit DEAD END
  seal_witness.txt   1d41cd5f68cd320b9e058d795931050624b7e3d12d6f75b064df2907636e6ede  one angle, D = 13-400     RUNS

Rerun (Python 3 with numpy; from inside atlas/):
  python3 frame_atlas.py          (about 6 s)
  python3 frame_owner_check.py    (about 1 min)
  NMAX=16 python3 reader_atlas.py (about 12 s)
  NS=17,18,19 python3 reader_extend.py (about 40 s)
  DMAX=400 python3 witness_run.py (a few seconds)
  DMAX=30 python3 preimage_map.py (about 20 s)
  python3 independent_check.py    (brute force cross-check, several minutes)
