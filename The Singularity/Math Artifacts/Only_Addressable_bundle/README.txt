Only Addressable (Kulik 2026) - scripts, certificates and outputs.
All scripts are plain Python 3 (numpy for across_language.py and parent_runs.py; matplotlib for figures.py).
Put every file in one folder and run from it. Some scripts also add /home/claude/space/rings to sys.path; that is harmless here.
Reader: witness_Kd.py (exact O(L) word_at / reader, location sets).  Ring builder: ringlib.py (closed form).
Run order and what each checks:
  top_block_law.py        Lemma A (exhaustive L=3..20) and the block law (top quarter, L=4..18)
  theorem_C_D.py          Theorem C first run (shows the s=0 edge case) and Theorem D, the pad law
  recheck_C_and_512.py    Theorem C with hypothesis s>=2 (1579/1579); pi-64 and 512-bit round trips
  obstruction_check.py    near-seam closed forms, excluded zone D=8..22
  across_language.py      R_d, E_d, minimal DFA sizes, depth-11 classes through depth 16 (exact atoms)
  parent_runs.py          runs met by parents of unreadable extensions through depth 12 (76/19/6)
  residue2_run.py         verifies the SHA-256 seal, runs the sealed residue-2 law + control, and Theorem E for D=13..119
  Kd_certificate.py       explicit witnesses D=8..40 (needs Kd_law.py)
  section_check.py        the tilted-section reader example
  figures.py, build_paper3.js   figures and the .docx (paths inside are absolute; edit to your folder)
Seal of the residue-2 prediction: see residue2_prediction.sha256 (60a2aad0...12fd65fd).
