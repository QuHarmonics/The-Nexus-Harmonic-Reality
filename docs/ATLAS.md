# The NEXUS Ring Atlas

Dean A. Kulik · QuHarmonics Research Group · ORCID 0009-0003-3128-8828

[Original notebook](https://github.com/QuHarmonics/The-Nexus-Harmonic-Reality/blob/979ee0ee2fc971d622848aba7fc2fbd2fcedb2b5/The%20Nexus%20Domain/Code/NEXUS_Ring_Atlas.ipynb) · [Public portal](https://quharmonics.github.io/The-Nexus-Harmonic-Reality/) · [Native domain](../The%20Nexus%20Domain/) · [Research-first licensing](../LICENSE.md)

The Atlas is the executable observatory, comprising fifteen chapters from genesis, partner and ring addressing through readers, the one-inverter clock, reader–field closure, collision, read models and the proof laboratory. Four embedded engines provide mathematical operations, proof checks, figures and interactive explorers.

## Two routes

- Original: run in local Jupyter; the source notebook and its recorded outputs remain unchanged.
- Browser edition: generated at Pages build time by [the adapter](../tools/prepare_browser_lab.py), without a second committed copy of the Atlas. It clears saved outputs, installs packages through Pyodide and selects the compatible Plotly renderer. Run setup, then engine and chapter cells in order. Long closure checks are explicitly skipped by default; enable them with RUN_LONG=True. Browser execution of all cells remains to be checked after deployment.

## Correction ledger — exact seam

The initial lightweight portal and Python reference constructed ascending partner representatives followed by reversed partners, without exchanging the central seam pair. The facing involution held for both permutations, so its first tests did not distinguish the two orders. Atlas chapter 3 and the ring/address/word_at implementations specify the seam exchange for every width n >= 2. R2 is 00, 10, 01, 11, not 00, 01, 10, 11.

Correction: apply the central transposition after building the partner order. The updated Python and JavaScript references implement that rule. The original Atlas engine was independently loaded and its complete order, address and inverse were compared with the corrected construction at widths 1–9 (1,022 words). This is a source-equivalence check, not a new discovery or independently sealed prediction. The original paper and Atlas are not rewritten. Partner and reader–field transition laws are unaffected.

The browser edition is a generated presentation and execution adapter, not a new mathematical engine.
