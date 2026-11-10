# NEXUS §189 candidate — ring doubling-break crease prediction, sealed mapping and hairpin landing

**Run date:** 2026-10-29. **Source:** `running-audit-4.md` (§§187–188), *Reading Proteins Through the Rings* §10, `NEXUS_Fold_Compiler_Notebook (2).zip` containing `ecoli_chains.json`. No energy fitting and no water data used.

## 1. Precise claim and its missing interface

The workbook's exact full-width circular window update is

\[
  v_{t+1}=2v_t-(2^W-1)b_t,\qquad b_t\in\{0,1\},
\]

where \(b_t\) is the bit leaving the window. With the same bit arriving at the bottom, the operation is ordinary doubling exactly when \(b_t=0\), and end-around carry when \(b_t=1\). A **doubling-break event** is \((b_{t-1},b_t)=(0,1)\).

This is a statement *about a given serialized stream*. To turn it into residue-index predictions, the hypothesis additionally requires an observation map \(t(i)\), a phase \(\delta\), and (for a one-bit-per-residue clock) a sampling step. Nothing in the ring facing law alone fixes this map. Without it, an event cannot yield a unique residue pair \(e,s\), hence cannot yield \(S=e+s\).

The **strict ring-only crease prediction is thus underdetermined**. We nevertheless ran two fixed zero-phase hypotheses to test the simplest possible registration without fitting to target hairpins.

## 2. Predeclared, conditional residue-to-ring registration

For each of the 160 chain records, use its *resolved residue count* \(L\), set \(w=\max(2,\lceil\log_2 L\rceil)\), and construct the native \(R_w\), with representatives ascending, last-pair crease swap, and facing images in reverse order. Sample a single departing bit per residue, starting at phase zero.

- **Primary (actual sliding-stream interpretation):** concatenate the \(w\)-bit ring words, MSB first. Assign the first \(L\) serialized bits to residue positions \(0,\dots,L-1\). At each 0→1, i.e. positions \(i-1,i\), predict \(e=i-1\), \(s=i\), \(S=2i-1\).
- **Secondary (word-MSB diagnostic):** instead take the MSB of the native ring word at address \(i\); this is *not* a consecutive sliding-window bitstream and is displayed only to delimit the interpretation.

**Leakage constraint:** Code constructs and serializes the full SHA-256 prediction manifest from the chain identifiers and lengths *before* any structural coordinates are used to compute a hairpin. Targets are then independently extracted using the unchanged §188 geometry. This is a code-level freeze, **not a claim of previously unseen preregistration**: this conversation includes exploratory checks before packaging the final seal.

**Seal:** `9ecfcfdc31f333fcf432a9fd7a3a902693d4260303f64c573cd04d1bbddc7dac` (canonical sorted-key JSON of the protocol and 160 predictions). See `NEXUS_Ring_DoublingBreak_Predictions_v01_SEALED.json`.

**Important limitation:** using \(L\) from crystallographically resolved residues is a read-back coverage choice, not a protein-independent way to determine the forward clock. Using the original gene length would require an additional mapping around unresolved residues.

## 3. Structural landing, no fitted parameters

Target definition reproduced verbatim from the supplied §188 script: nearest N···O within 3.5 Å, exclude residue separation ≤2, proline donors omitted, facing runs on constant \(S=i+j\), ≥3 contacts, consecutive run increments ≤2, terminal arm gap ≤8, and chain length ≥30. Readback recovers **143 hairpins on 160 chains**, with **49 even-S and 94 odd-S**.

| Predeclared metric | Primary serialized stream | Secondary word-MSB diagnostic |
|---|---:|---:|
| Proposed 0→1 events | 3,366 | 513 |
| Exact S matches | 11 / 143 | 2 / 143 |
| Crease centre within one residue | 64 / 143 | 5 / 143 |
| Within two residues | 101 / 143 | 9 / 143 |
| Within five residues | 141 / 143 | 21 / 143 |
| Event-level exact precision | 11 / 3,366 = 0.33% | 2 / 513 = 0.39% |

The large broad-tolerance recall is not evidence of precise localization: the primary produces 3,366 events. Of the 11 exact primary hits, all are odd-S hairpins. A boundary between consecutive integer positions necessarily has \(S=(i-1)+i=2i-1\), hence **never predicts an even-S centre**. An additional operation would be needed for the 49 even-S pinches (single-cell centre) without fitting post-hoc.

## 4. Controls (3,000 Monte Carlo replicates each)

Two controls use the exact same event count or fixed ring pattern per chain; both retain each chain's true hairpins untouched.

| Metric | Observed | Equal-count random boundary: average (95% interval) | Circular phase-shift ring: average (95% interval) |
|---|---:|---|---|
| Exact S | 11 | 16.50 (10–24) | 16.48 (10–24) |
| Centre within 1 | 64 | 57.32 (46–69) | 63.68 (53–75) |
| Centre within 2 | 101 | 85.42 (74–96) | 100.22 (90–111) |
| Centre within 5 | 141 | 126.25 (119–133) | 135.26 (130–140) |

The within-two comparison exceeds *uniform random event sites* (empirical one-sided upper-tail \(p=0.0033\)) but **not the native pattern with a random unknown phase** (\(p=0.4775\)). The latter is the necessary control for claiming predictive power from the ring's particular bitstream. Within-one likewise fails against phase shift (\(p=0.5155\)). The within-five near-saturation effect (\(p=0.0147\) against shifts) is neither an exact crease prediction nor adjusted for multiple tolerances; it cannot close the open link.

Choosing a separate phase *after seeing each chain's hairpins* can achieve **91/143 exact**. That is an oracle leakage diagnostic, not a prediction. It demonstrates why observing agreement after centring the ring on a known crease proves nothing about placing the crease.

## 5. Mathematical inference

Given any 0→1 location \(t_0\) in the native ring serialization and any target boundary \(i\), define the unobserved registration \(t(i)=t_0+(i-i_0)\) mod stream length with phase chosen so the event occurs at \(i\). The full-width carry equation continues to hold identically. **Therefore the carry law plus ring cannot distinguish these physical placements**: the anchor and clock are missing providers. A chain cannot be treated as one universal square; each observed reflection may have a local \(S=e+s\), but \(S\) is a *consequence of known ends* unless a forward process places them.

## 6. Ledger

- **STANDS:** Native facing identity; full-width end-around update; 0→1 and 1→0 are paired around a closed binary stream; two adjacent indices have odd sum.
- **RUNS:** R2–R6 sliding carry identity checks, SHA-256 frozen prediction manifest, independent recreation of §188's 143 hairpins and parity split; primary/secondary landings and two null ensembles.
- **DEAD END:** Zero-phase ring sampling as a complete fold-crease predictor; interpreting a post-hoc phase as prediction; using near-saturation wide tolerance as a precise landing.
- **OPEN:** Derive a physically justified map between executed transitions and the chain's residue-by-residue clock/phase, including single-cell even-S crease placement; source of long-range strand partner REACH. No field or water claim follows from this test.

## 7. Reproduction artifacts

- `NEXUS_Ring_DoublingBreak_Hairpin_Seal_v01.py` — full reproducible single-cell-compatible source; prediction sealed before target derivation.
- `NEXUS_Ring_DoublingBreak_Hairpin_Seal_v01_Single_Cell.ipynb` — same code as one notebook cell, with the complete saved transcript.
- `NEXUS_Ring_DoublingBreak_Predictions_v01_SEALED.json` — SHA-256 and per-chain predictions.
- `NEXUS_Ring_DoublingBreak_Hairpin_v01_results.json` — target hairpins, per-chain candidate placements, null summaries and all counts.
- `NEXUS_Ring_DoublingBreak_Hairpin_v01_execution.txt` — complete stdout.

## 8. Exact next prompt

> Continue NEXUS §189 from the sealed doubling-break null test. R2–R6 end-around-carry identities hold, but zero-phase serialized ring breaks match only 11/143 hairpin sums exactly and 64/143 within one residue, indistinguishable from randomized native-ring phase (16.48 and 63.68 expected). A post-hoc phase can fit up to 91/143 per chain and is prohibited. Moreover, a boundary between consecutive residues predicts odd S only; 49/143 creases have even S.
>
> **Derive the missing reader registration rather than fitting more bit rules.** From the executed input available at translation time, specify precisely which physical event advances a ring reading, what fixes its phase, how a local forward run opens and closes a square, and how a centre may lie on a residue (even S) or between residues (odd S). Do not read target contacts, coordinates, crease centres or a posteriori partner indices to define the mapping. If no such derivation exists, prove the interface is underdetermined and report that as OPEN rather than inventing a selector. Freeze the mapping, run it against the same 143 hairpins with matched-count and random-phase controls, then address long-range partner REACH separately. Supply one runnable cell, full traces and STANDS/RUNS/OPEN/DEAD END, followed by the next prompt.
