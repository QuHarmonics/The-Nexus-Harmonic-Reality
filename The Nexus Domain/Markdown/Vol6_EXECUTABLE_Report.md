# Vol6 Executable Pins Report

This pass enforces **executable-only pins**: cells must run in a clean environment with `RUN_DEMOS=False`.

## Key fixes applied
- `matplotlib` import patch: `import matplotlib.artist` must occur before `import matplotlib.pyplot as plt` in this environment.
- Heavy demo loops are wrapped behind `RUN_DEMOS=False`.
- Optional UI/CLI dependencies are quarantined (`dash`, `PyInquirer`).

## Notebook results

### Crypto
- Original: `Vol6_crypto_novel_pins.ipynb`
- Executable subset: `Vol6_crypto_EXECUTABLE.ipynb`
- Status: **16 code cells kept**, **8 quarantined**
- Quarantine reasons: NameError×7, FileNotFoundError×1

### Pi
- Original: `Vol6_pi_novel_pins.ipynb`
- Executable subset: `Vol6_pi_EXECUTABLE_v2.ipynb`
- Status: **1 code cells kept**, **1 quarantined**
- Quarantine reasons: ModuleNotFoundError×1

### System
- Original: `Vol6_system_novel_pins.ipynb`
- Executable subset: `Vol6_system_EXECUTABLE.ipynb`
- Status: **5 code cells kept**, **7 quarantined**
- Quarantine reasons: NameError×6, ModuleNotFoundError×1

### Cross
- Original: `Vol6_cross_novel_pins.ipynb`
- Executable subset: `Vol6_cross_EXECUTABLE_v2.ipynb`
- Status: **19 code cells kept**, **18 quarantined**
- Quarantine reasons: NameError×6, ModuleNotFoundError×2, LookupError×1, FileNotFoundError×1, TypeError×1, TIMEOUT×3, SyntaxError×3, IndexError×1

## Next rule (so we don’t repeat Vol6)
From here on, a cell is a **pin** only if it satisfies at least one:
1) Defines an operator (`def`/`class`) with no missing deps
2) Executes a bounded demo (fast, deterministic) behind `RUN_DEMOS`
3) Produces a verifiable artifact (hash check, reconstruction check, invariant check)

Everything else stays archived but not promoted.
