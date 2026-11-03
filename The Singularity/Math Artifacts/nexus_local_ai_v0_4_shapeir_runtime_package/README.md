# Nexus Local AI v0.4 — ShapeIR Runtime

This package builds the next runtime mold:

raw prompt -> VNA -> ShapeIR -> retrieval-root NeedSlot -> model packet evidence -> AHRC/SILR/Glyph certificate -> Ψ/Ω/Σ/⊥/ρ.

Files:
- nexus_local_ai_v0_4_shapeir_runtime_notebook.ipynb: Jupyter notebook.
- nexus_shapeir_runtime_v04.py: importable runtime module.
- nexus_shapeir_seed_bank_v04.jsonl: default compiler seed bank.

Run:
1. Put your corpus files beside the notebook, or edit CORPUS_PATHS.
2. Open the notebook.
3. Set LOAD_MODEL=True for Qwen generation, False for compiler smoke test.
4. Run top to bottom.
5. Inspect nexus_shapeir_runs/*.json.

Core law:
C_root = authority.
Model/T2 output = evidence.
Answer = residue/stub.
Ω mutates the mold.
