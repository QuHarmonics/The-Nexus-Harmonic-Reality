# NEXUS §194 — Zipper value-channel / dry-face audit

**Date:** 2026-10-30  |  **Input:** `NEXUS_Fold_Compiler_Notebook (2).zip`  |  **Script:** one runnable Python cell  |  **Status:** conditional structural association, not forward folding prediction

## Scope and exact provenance

This follows the provided `running-audit-5.md` §192–193, in which the decompiled antiparallel ladder alternates bonded and idle rows and the **143 hairpin boundaries** were obtained from the finished coordinate data. The two-arm zipper is indexed as `(e−t, s+t)`, with `t=0` at the crease. Only the face score is computed from amino-acid identities, before reading the burial and ordered-water labels. This is a **conditional** test, since crease selection and arm length were supplied by the structure-based §193 detector. It cannot show sequence-only discovery of those crease locations.

The §5 source, *Reading Proteins Through the Rings*, specifies slot words `00` (unshared pair) and `11` (hydrogen on N/O), water `11 11 00 00`, and a qualitative slot-count/hydropathy relationship. It does **not** supply a fixed 20-residue water-slot table. The table below is an explicit coarse implementation added for this experiment, not a pre-existing derived identity: oxygen groups contribute approximate acceptor-pair slots, N/O hydrogens contribute donor slots; physiological protonation is approximated, sulfur excluded, and `H` histidine simplified. It is a **chemical model**, not a literal electron-state census or universal physical law.

The analysis is staged: (A) use undirected nearest-backbone contacts from the solved structures to identify `(e,s,k)` exactly as in §193; (B) read amino-acid identity only to predict a lower-slot dry parity and hash every prediction; (C) examine the completed coordinates and water file. We do not use the target Cβ, CA or waters to choose the prediction. Nevertheless, hairpin localization is label-derived, and the same known corpus has informed earlier design choices. The hash is a program-order seal, **not** a new independent held-out preregistration.

## One-base shape/value interface

At the residue-address level, each row swaps two cell addresses by the exact transposition of the native pair word: `P(W(i,j)) = W(j,i)` when `i != j`. Verified exhaustively for widths `m=2..7`. The shape channel is that pair relation and alternating row phase. The value channel records the N/O water-facing slot types offered by each side chain. The score is a projection **from the multiset of binary 2-bit slot symbols into an integer count**, not an assertion that chemistry is equivalent to binary addition.

The frozen primary vote was: count side-chain `11` plus `00` slots over all residues at even `t` and odd `t`. Fewer slots predicts the **dry** face; ties abstain. The flipped-parity null selects the other face. Compare that predicted face against average nonlocal Cα neighbor density within 8 Å around each side-chain Cβ (Gly and missing Cβ use Cα as an explicit proxy), excluding neighbors within 3 sequence positions. This is **burial proxy**, not true solvent-accessible surface area (SASA). As an independent read, count ordered crystallographic water oxygens within 4 Å of the same probe.

## Frozen rule and seal

- Primary rule SHA-256: `ef88d6309cd941aeae63eef4fc5a346c193b66cd9d3355c5d95c0b58256ffba4`
- Conditional per-hairpin prediction manifest SHA-256: `03b2aa98d86642b4155df76282fa87fde58d871d3a49e3eda162e8a7e521d279`
- Hairpins: **143**, primary abstentions 5, burial ties 2.

### Frozen side-chain slot assumptions

| Amino acid | H (`11`) | LP (`00`) | Total |
|---|---:|---:|---:|
| A | 0 | 0 | 0 |
| C | 0 | 0 | 0 |
| D | 0 | 4 | 4 |
| E | 0 | 4 | 4 |
| F | 0 | 0 | 0 |
| G | 0 | 0 | 0 |
| H | 1 | 1 | 2 |
| I | 0 | 0 | 0 |
| K | 3 | 0 | 3 |
| L | 0 | 0 | 0 |
| M | 0 | 0 | 0 |
| N | 2 | 2 | 4 |
| P | 0 | 0 | 0 |
| Q | 2 | 2 | 4 |
| R | 5 | 0 | 5 |
| S | 1 | 2 | 3 |
| T | 1 | 2 | 3 |
| V | 0 | 0 | 0 |
| W | 1 | 0 | 1 |
| Y | 1 | 2 | 3 |

## Primary outcomes

| Readout | Result | Interpretation |
|---|---:|---|
| Raw slot total | **105/136 (77.2%)** | Conditional match |
| Parity-flip null | **31/136 (22.8%)** | Complements the primary vote by design; not an independent random model |
| Always predict odd face | **92/136 (67.6%)** | Important class/face imbalance control |
| Per-residue slot density | **101/136 (74.3%)** | Corrects unequal even/odd face size |
| Exclude crease row; use density | **99/130 (76.2%)** | 11 score ties + 2 burial ties |
| Binary polar/nonpolar, per residue | **100/133 (75.2%)** | Coarsest count |
| Within-hairpin composition-preserving shuffle | **75.3 raw matches on average** | 3,000 shuffles, mean n=133.4, upper-tail p≈0.00033 (different tie count) |
| Raw-score gain over always-odd | **+13/136** | Paired exact McNemar p=0.0854; not decisive |
| Density-score gain over always-odd | **+11/136** | Paired exact McNemar p=0.2074; not decisive |
| Chain-block bootstrap | **77.2% [69.9%, 84.3%]** | 4,000 block resamples of 91 source chains |
| Bootstrap gain over always-odd | **[0.0%, 18.8%]** | 95% interval includes no gain |

The raw binomial comparison to 50% (`p=6.63e−11`) is **not the proper sole test** because the observed face labels are imbalanced, with 92 of the 136 scored structures classified as odd-dry. The more demanding always-odd paired comparison is not decisive. Randomly shuffling the slot scores within each hairpin gives a more favorable signal for sequence placement, but it does not remove the structural conditioning or prove a folding mechanism.

## Ordered-water read and structural face check

| Measure | Result |
|---|---:|
| Ordered water within 4 Å of predicted wet-face sidechain proxy | **360/940 = 38.3%** |
| Ordered water within 4 Å of predicted dry-face proxy | **202/860 = 23.5%** |
| Within-hairpin higher wet than dry water fraction | **89** |
| Within-hairpin lower wet than dry water fraction | **32** |
| Tied water fraction | **17** |
| Both arms have sidechain Cβ pointing to same structural plane-normal side on the same row | **509/772 = 65.9%** |

Water contacts are based on ordered crystal waters, not all solvent molecules, and are sensitive to the coordinate set. The 65.9% same-side rate is a limitation of the idealized assertion that every even-row side chain on both arms represents one common physical face; a real β-sheet twists, kinks, bulges, and connects other strands. The orientation is a **read-back** using the structural CA/CB coordinates, not a source of sequence predictions.

## Bimetal-offset check

For the subset with both specified staggered turn closures observed—`e.NH -> s.O` and `(s−1).NH -> e.O`—I constructed an **exploratory** oriented plane from the crease coordinates, assigned the predicted dry parity an actual Cβ side and compared it to the side on which CA(s−1) sits relative to the two-strand crease midpoint. This is a chosen geometric proxy for “offset side,” not a previously derived curling operator or a force/torque calculation.

Result: **27/46 same side, 19/46 opposite** (two-sided binomial p≈0.302). Neither the face direction nor the bend torque is uniquely determined by the directed slot transpositions. **The bimetal curl hypothesis remains OPEN.**

## What the compiler does and does not derive

- **STANDS (mathematics):** Native off-diagonal transposition of pair words; alternating rows can be written as permutation/identity steps; no single globally registered square is required.
- **RUNS (conditional association):** Slot-count parity correlates with burial and ordered-water incidence on the detected zipper arms; the results above include parity, size, composition and block-resampling controls.
- **OPEN (physics):** The 20-aa slot-count lookup is an approximate chemical interpretation, not an exact atom-derived count; β-face orientation is not determined everywhere by row parity; solvent access, side-chain rotamers and relative hairpin configuration are unresolved.
- **OPEN (forward DI):** The sequence alone still does not identify `(e,s,k)` or the distant strand. The crease offset alone does not determine the dry-face orientation or a signed curvature.
- **DEAD END (overclaim):** “77.2% proves the dry face is generated by the ring”, “all even residues on both arms point to one physical side”, and “the stagger forces the bimetal curl”. The data do not establish any of these.

## Complete per-hairpin readout

`dry`: 0=even-row face, 1=odd-row face, `—`=abstain. `observed`: face with greater nonlocal Cα neighbor density. `hit`: binary exact dry-side decision. Water counts are near-Cβ ordered waters.

| Hairpin (PDB/acc/e-s-k) | S | Even slots | Odd slots | Pred dry | Observed dry | Mean burial even | Mean burial odd | Waters even/odd | Hit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2F1F/P00894/36-41-6 | 77 | 21 | 3 | 1 | 0 | 7.12 | 6.83 | 6/2 | × |
| 5WQV/P07013/37-40-12 | 77 | 18 | 28 | 0 | 0 | 6.43 | 5.67 | 1/3 | ✓ |
| 5WQV/P07013/78-81-6 | 159 | 18 | 0 | 1 | 1 | 4.88 | 7.33 | 1/2 | ✓ |
| 5WQV/P07013/18-22-4 | 40 | 12 | 5 | 1 | 1 | 4.50 | 5.75 | 3/2 | ✓ |
| 7WW6/P08337/74-77-6 | 151 | 12 | 17 | 0 | 0 | 7.12 | 6.17 | 2/2 | ✓ |
| 1FS0/P0A6E6/53-57-6 | 110 | 9 | 12 | 0 | 0 | 6.00 | 5.17 | 2/2 | ✓ |
| 1FS0/P0A6E6/7-15-4 | 22 | 3 | 9 | 0 | 0 | 7.67 | 6.00 | 2/3 | ✓ |
| 1FS0/P0A6E6/71-74-6 | 145 | 19 | 0 | 1 | 1 | 6.50 | 9.00 | 5/1 | ✓ |
| 1FS0/P0A6E6/26-29-4 | 55 | 0 | 11 | 0 | 1 | 5.83 | 6.00 | 2/2 | × |
| 1XEO/P0A6K3/111-115-6 | 226 | 7 | 16 | 0 | 0 | 6.75 | 6.17 | 3/2 | ✓ |
| 1JKE/P0A6M4/12-20-11 | 32 | 8 | 16 | 0 | 0 | 9.67 | 8.75 | 3/6 | ✓ |
| 1JKE/P0A6M4/56-60-3 | 116 | 11 | 3 | 1 | 1 | 5.25 | 6.00 | 1/1 | ✓ |
| 4KEH/P0A6Q3/146-154-4 | 300 | 7 | 14 | 0 | 0 | 9.67 | 8.00 | 1/3 | ✓ |
| 1ETO/P0A6R3/6-11-4 | 17 | 9 | 10 | 0 | 0 | 4.17 | 4.00 | 0/2 | ✓ |
| 9H45/P0A6X3/40-46-4 | 86 | 7 | 3 | 1 | 0 | 6.50 | 5.00 | 3/0 | × |
| 1OWF/P0A6X7/62-67-4 | 129 | 13 | 9 | 1 | 1 | 3.83 | 4.25 | 1/0 | ✓ |
| 1OWF/P0A6Y1/61-66-4 | 127 | 13 | 15 | 0 | 1 | 3.67 | 3.75 | 1/1 | × |
| 2HZA/P0A6Z6/89-93-6 | 182 | 4 | 11 | 0 | 1 | 5.00 | 6.17 | 0/2 | × |
| 4PYA/P0A738/67-72-8 | 139 | 38 | 3 | 1 | 1 | 5.50 | 11.12 | 3/1 | ✓ |
| 6SYM/P0A746/124-129-4 | 253 | 8 | 16 | 0 | 0 | 6.83 | 6.75 | 1/3 | ✓ |
| 6SYM/P0A746/82-85-8 | 167 | 29 | 10 | 1 | 1 | 5.50 | 6.38 | 7/2 | ✓ |
| 5LS7/P0A790/22-27-6 | 49 | 14 | 16 | 0 | 0 | 6.75 | 5.83 | 1/3 | ✓ |
| 2AU7/P0A7A9/32-37-6 | 69 | 15 | 3 | 1 | 1 | 4.75 | 5.83 | 5/2 | ✓ |
| 2AU7/P0A7A9/94-97-6 | 191 | 11 | 10 | 1 | 0 | 9.38 | 9.00 | 1/4 | × |
| 2AU7/P0A7A9/9-12-3 | 21 | 8 | 10 | 0 | 1 | 5.75 | 7.25 | 3/4 | × |
| 1JL1/P0A7Y4/23-26-8 | 49 | 17 | 15 | 1 | 1 | 8.70 | 8.88 | 3/2 | ✓ |
| 1HJR/P0A814/8-11-8 | 19 | 8 | 11 | 0 | 1 | 8.80 | 10.88 | 1/0 | × |
| 1HJR/P0A814/20-23-4 | 43 | 12 | 7 | 1 | 1 | 5.67 | 8.00 | 0/0 | ✓ |
| 3HVV/P0A862/30-34-4 | 64 | 3 | 10 | 0 | 1 | 5.83 | 6.00 | 3/3 | × |
| 3HVV/P0A862/5-8-4 | 13 | 8 | 8 | — | 0 | 7.83 | 5.25 | 4/2 | — |
| 1NU0/P0A8I1/9-12-4 | 21 | 7 | 0 | 1 | — | 10.50 | 10.50 | 4/1 | — |
| 1NU0/P0A8I1/19-24-4 | 43 | 12 | 0 | 1 | 1 | 6.17 | 10.25 | 2/2 | ✓ |
| 1Q5X/P0A8R0/145-148-4 | 293 | 12 | 0 | 1 | 1 | 9.33 | 10.75 | 3/0 | ✓ |
| 4K4C/P0A8Y8/104-112-6 | 216 | 16 | 1 | 1 | 1 | 7.50 | 11.33 | 6/1 | ✓ |
| 1MJC/P0A9X9/56-59-4 | 115 | 7 | 3 | 1 | 1 | 5.33 | 7.25 | 2/1 | ✓ |
| 8XYF/P0A9Y6/54-57-4 | 111 | 8 | 4 | 1 | 1 | 4.67 | 7.25 | 5/1 | ✓ |
| 3CCD/P0AA04/34-37-4 | 71 | 6 | 12 | 0 | 0 | 9.00 | 6.00 | 2/4 | ✓ |
| 1R94/P0AAC8/32-36-8 | 68 | 17 | 6 | 1 | 1 | 5.50 | 5.88 | 3/0 | ✓ |
| 1R94/P0AAC8/81-84-6 | 165 | 22 | 7 | 1 | 1 | 4.00 | 6.50 | 2/1 | ✓ |
| 1R94/P0AAC8/56-59-6 | 115 | 8 | 15 | 0 | 0 | 6.38 | 5.83 | 0/2 | ✓ |
| 2DXA/P0AAR3/129-134-4 | 263 | 0 | 14 | 0 | 0 | 10.17 | 9.50 | 2/1 | ✓ |
| 2DXA/P0AAR3/51-57-8 | 108 | 8 | 6 | 1 | 1 | 9.40 | 9.88 | 4/5 | ✓ |
| 4HR7/P0ABD8/43-46-4 | 89 | 4 | 8 | 0 | 0 | 7.50 | 6.25 | 1/2 | ✓ |
| 1F9Z/P0AC81/114-118-6 | 232 | 11 | 11 | — | 0 | 9.50 | 7.50 | 2/3 | — |
| 1F9Z/P0AC81/33-38-4 | 71 | 15 | 10 | 1 | 1 | 5.33 | 7.25 | 0/0 | ✓ |
| 1MUL/P0ACF0/54-59-8 | 113 | 15 | 9 | 1 | 1 | 4.90 | 5.88 | 4/4 | ✓ |
| 1DM9/P0ACG8/54-57-6 | 111 | 13 | 18 | 0 | 1 | 6.25 | 7.00 | 1/3 | × |
| 1XS0/P0AD59/69-74-8 | 143 | 21 | 8 | 1 | 0 | 8.70 | 8.12 | 2/0 | × |
| 1XS0/P0AD59/43-46-4 | 89 | 11 | 13 | 0 | 0 | 7.83 | 5.75 | 3/2 | ✓ |
| 1XS0/P0AD59/55-62-6 | 117 | 12 | 8 | 1 | 1 | 9.25 | 11.50 | 2/3 | ✓ |
| 1XS0/P0AD59/83-88-6 | 171 | 17 | 8 | 1 | 1 | 5.75 | 6.67 | 2/1 | ✓ |
| 4P1M/P0ADS2/6-9-6 | 15 | 9 | 20 | 0 | 0 | 4.88 | 3.67 | 0/2 | ✓ |
| 9PME/P0AE70/53-60-4 | 113 | 0 | 4 | 0 | 0 | 8.67 | 7.25 | 2/2 | ✓ |
| 9PME/P0AE70/14-18-6 | 32 | 12 | 1 | 1 | 1 | 7.75 | 9.33 | 0/2 | ✓ |
| 1MVF/P0AE72/34-37-6 | 71 | 18 | 0 | 1 | 1 | 3.12 | 4.17 | 1/2 | ✓ |
| 1QU9/P0AF93/21-24-4 | 45 | 7 | 7 | — | 1 | 6.50 | 9.50 | 4/1 | — |
| 2OUG/P0AFW0/37-40-8 | 77 | 13 | 15 | 0 | 0 | 5.20 | 4.25 | 0/2 | ✓ |
| 1UMU/P0AG11/58-61-6 | 119 | 14 | 3 | 1 | 1 | 7.38 | 7.67 | 2/2 | ✓ |
| 1QYN/P0AG86/57-65-12 | 122 | 11 | 26 | 0 | 0 | 9.79 | 7.75 | 0/3 | ✓ |
| 1QYN/P0AG86/42-46-12 | 88 | 36 | 13 | 1 | 1 | 5.29 | 7.92 | 8/1 | ✓ |
| 1ESO/P0AGD1/13-16-8 | 29 | 26 | 4 | 1 | 1 | 3.30 | 3.75 | 4/1 | ✓ |
| 1QVC/P0AGE0/87-94-6 | 181 | 25 | 18 | 1 | 1 | 5.38 | 5.83 | 4/4 | ✓ |
| 4LW4/P0AGF2/69-73-8 | 142 | 22 | 6 | 1 | 1 | 6.80 | 9.12 | 4/0 | ✓ |
| 7EYJ/P0C037/18-22-8 | 40 | 9 | 14 | 0 | 1 | 6.00 | 6.88 | 4/4 | × |
| 7EYJ/P0C037/7-10-5 | 17 | 13 | 14 | 0 | 1 | 5.00 | 5.33 | 4/4 | × |
| 4FXI/P0C077/64-69-4 | 133 | 4 | 3 | 1 | 1 | 7.83 | 9.25 | 0/0 | ✓ |
| 1QWI/P0C0L2/86-89-4 | 175 | 10 | 3 | 1 | 1 | 3.50 | 4.75 | 5/0 | ✓ |
| 1QWI/P0C0L2/11-15-7 | 26 | 8 | 26 | 0 | 0 | 5.38 | 4.62 | 1/6 | ✓ |
| 1SLU/P23827/54-59-6 | 113 | 20 | 14 | 1 | 1 | 5.75 | 6.50 | 0/0 | ✓ |
| 5XU7/P24224/107-110-8 | 217 | 23 | 4 | 1 | 1 | 5.20 | 10.62 | 7/2 | ✓ |
| 5XU7/P24224/75-79-6 | 154 | 26 | 4 | 1 | 1 | 4.88 | 7.17 | 2/3 | ✓ |
| 1TT8/P26602/78-85-8 | 163 | 14 | 12 | 1 | 1 | 9.00 | 10.50 | 4/1 | ✓ |
| 1TT8/P26602/143-146-8 | 289 | 16 | 18 | 0 | 1 | 8.70 | 9.75 | 1/3 | × |
| 1TT8/P26602/131-134-6 | 265 | 18 | 14 | 1 | 1 | 7.00 | 7.67 | 3/3 | ✓ |
| 8IWI/P27838/63-66-4 | 129 | 6 | 3 | 1 | 0 | 7.83 | 6.25 | 2/4 | × |
| 8IWI/P27838/73-76-4 | 149 | 17 | 1 | 1 | 1 | 5.00 | 8.25 | 4/2 | ✓ |
| 8IWI/P27838/42-46-4 | 88 | 3 | 9 | 0 | 0 | 8.50 | 7.00 | 2/3 | ✓ |
| 8IWI/P27838/34-37-4 | 71 | 18 | 0 | 1 | 1 | 4.67 | 7.75 | 6/1 | ✓ |
| 8IWI/P27838/53-58-4 | 111 | 13 | 5 | 1 | 1 | 6.33 | 9.50 | 4/1 | ✓ |
| 1FM0/P30749/121-124-4 | 245 | 15 | 10 | 1 | 1 | 4.33 | 5.75 | 1/3 | ✓ |
| 1RYA/P32056/37-41-4 | 78 | 16 | 7 | 1 | 1 | 6.50 | 7.25 | 4/2 | ✓ |
| 1X8D/P32156/45-50-4 | 95 | 7 | 0 | 1 | 1 | 5.33 | 6.50 | 1/0 | ✓ |
| 4QAK/P37025/154-157-6 | 311 | 16 | 12 | 1 | 1 | 4.62 | 5.33 | 2/4 | ✓ |
| 4QAK/P37025/78-83-4 | 161 | 6 | 4 | 1 | 1 | 6.83 | 10.00 | 2/0 | ✓ |
| 5LS7/P37613/41-49-6 | 90 | 12 | 10 | 1 | 0 | 9.62 | 8.50 | 3/3 | × |
| 5LS7/P37613/56-59-4 | 115 | 19 | 0 | 1 | 1 | 5.83 | 9.25 | 6/2 | ✓ |
| 1U5W/P39411/79-82-8 | 161 | 17 | 6 | 1 | 0 | 10.00 | 9.88 | 2/2 | × |
| 1U5W/P39411/91-94-6 | 185 | 14 | 19 | 0 | 1 | 8.25 | 8.67 | 4/1 | × |
| 1OI4/P45470/43-48-4 | 91 | 3 | 12 | 0 | 0 | 7.83 | 4.75 | 2/2 | ✓ |
| 4MAK/P45956/60-65-6 | 125 | 12 | 3 | 1 | 0 | 6.12 | 5.33 | 4/2 | × |
| 3QMQ/P64461/42-48-6 | 90 | 24 | 8 | 1 | 1 | 6.12 | 8.17 | 0/2 | ✓ |
| 4NTK/P65870/108-112-4 | 220 | 7 | 3 | 1 | 0 | 7.67 | 6.50 | 1/1 | × |
| 2A6Q/P69346/30-34-4 | 64 | 9 | 3 | 1 | 1 | 5.67 | 6.00 | 1/0 | ✓ |
| 1F3Z/P69783/62-66-6 | 128 | 5 | 13 | 0 | 0 | 8.88 | 7.67 | 0/0 | ✓ |
| 5Z38/P69913/22-30-4 | 52 | 15 | 0 | 1 | 1 | 5.67 | 6.75 | 3/0 | ✓ |
| 5Z38/P69913/13-17-4 | 30 | 4 | 9 | 0 | 1 | 5.67 | 5.75 | 0/2 | × |
| 5E1L/P75862/127-135-4 | 262 | 4 | 0 | 1 | 0 | 10.50 | 9.75 | 1/0 | × |
| 5E1L/P75862/22-26-4 | 48 | 3 | 9 | 0 | 0 | 7.83 | 6.00 | 0/0 | ✓ |
| 5E1L/P75862/12-17-4 | 29 | 21 | 4 | 1 | 1 | 7.67 | 10.25 | 0/1 | ✓ |
| 5E1L/P75862/115-120-6 | 235 | 8 | 9 | 0 | 1 | 7.38 | 7.83 | 1/3 | × |
| 5E1L/P75862/145-148-4 | 293 | 5 | 4 | 1 | 0 | 4.67 | 4.00 | 3/1 | × |
| 2FS2/P76084/99-107-8 | 206 | 30 | 7 | 1 | 1 | 6.70 | 11.12 | 5/1 | ✓ |
| 1MZG/P76194/59-63-8 | 122 | 30 | 7 | 1 | 1 | 5.40 | 9.12 | 4/3 | ✓ |
| 2G2N/P76341/26-29-4 | 55 | 3 | 12 | 0 | 1 | 5.17 | 6.00 | 2/2 | × |
| 2VB2/P77214/62-65-4 | 127 | 12 | 7 | 1 | 1 | 6.00 | 8.50 | 1/2 | ✓ |
| 1NJK/P77712/76-84-8 | 160 | 24 | 7 | 1 | 1 | 7.00 | 10.00 | 7/1 | ✓ |
| 1VH5/P77781/103-111-6 | 214 | 16 | 1 | 1 | 1 | 7.25 | 11.17 | 5/1 | ✓ |
| 3O9X/Q46864/21-24-4 | 45 | 11 | 6 | 1 | 0 | 4.67 | 3.75 | 1/3 | × |
| 3HI2/Q46865/74-77-6 | 151 | 7 | 20 | 0 | 0 | 7.12 | 6.17 | 2/0 | ✓ |
| 3HI2/Q46865/86-89-6 | 175 | 15 | 0 | 1 | 1 | 5.75 | 9.00 | 3/1 | ✓ |
| 4Q2U/Q47149/61-65-6 | 126 | 9 | 12 | 0 | 1 | 7.62 | 8.83 | 3/1 | × |
| 4Q2U/Q47149/72-75-4 | 147 | 15 | 3 | 1 | 1 | 7.17 | 8.50 | 2/1 | ✓ |
| 8K6G/P00816/134-138-10 | 272 | 33 | 7 | 1 | 1 | 3.58 | 4.60 | 7/4 | ✓ |
| 1VSR/P09184/125-128-4 | 253 | 13 | 0 | 1 | 1 | 5.50 | 7.25 | 2/0 | ✓ |
| 1VSR/P09184/20-27-3 | 47 | 4 | 13 | 0 | — | 6.75 | 6.75 | 1/2 | — |
| 1VSR/P09184/32-35-3 | 67 | 9 | 0 | 1 | 1 | 6.75 | 8.75 | 2/0 | ✓ |
| 3A7L/P0A6T9/61-64-4 | 125 | 6 | 8 | 0 | 0 | 7.67 | 6.00 | 0/0 | ✓ |
| 3A7L/P0A6T9/18-22-6 | 40 | 21 | 10 | 1 | 1 | 6.75 | 8.67 | 3/1 | ✓ |
| 4FYY/P0A7F3/123-126-6 | 249 | 23 | 3 | 1 | 1 | 5.38 | 8.00 | 5/0 | ✓ |
| 4FYY/P0A7F3/131-136-4 | 267 | 5 | 10 | 0 | 0 | 7.17 | 6.25 | 1/2 | ✓ |
| 2H09/P0A9F1/63-67-4 | 130 | 7 | 0 | 1 | 1 | 5.50 | 8.75 | 2/1 | ✓ |
| 9SV1/P0AB65/37-41-6 | 78 | 16 | 4 | 1 | 1 | 7.00 | 10.00 | 4/2 | ✓ |
| 3MPY/P0ABF4/34-38-4 | 72 | 6 | 4 | 1 | 1 | 6.50 | 7.25 | 0/0 | ✓ |
| 4MTD/P0AC51/99-104-4 | 203 | 7 | 4 | 1 | 1 | 6.50 | 8.50 | 0/0 | ✓ |
| 4MTD/P0AC51/75-80-4 | 155 | 5 | 6 | 0 | 1 | 6.83 | 7.50 | 0/0 | × |
| 5YPP/P0ADF8/37-42-6 | 79 | 6 | 3 | 1 | 1 | 6.62 | 6.83 | 0/2 | ✓ |
| 4DT4/P0AEM0/102-106-6 | 208 | 3 | 7 | 0 | 0 | 5.25 | 4.83 | 5/5 | ✓ |
| 3BMB/P0AFW4/62-67-6 | 129 | 21 | 16 | 1 | 0 | 8.12 | 6.83 | 3/3 | × |
| 3BMB/P0AFW4/109-113-6 | 222 | 8 | 15 | 0 | 0 | 7.25 | 5.33 | 2/5 | ✓ |
| 4HF0/P0AGK8/57-63-4 | 120 | 3 | 6 | 0 | 1 | 6.83 | 7.50 | 1/2 | × |
| 2UYK/P0AGL2/21-24-4 | 45 | 7 | 7 | — | 1 | 6.50 | 9.50 | 3/1 | — |
| 4XB6/P16685/73-77-8 | 150 | 12 | 18 | 0 | 0 | 10.10 | 6.88 | 3/3 | ✓ |
| 4XB6/P16685/52-57-4 | 109 | 4 | 14 | 0 | 1 | 3.83 | 4.25 | 3/2 | × |
| 8VRG/P23869/5-8-4 | 13 | 3 | 9 | 0 | 0 | 7.33 | 7.25 | 1/2 | ✓ |
| 1NP6/P32125/54-57-6 | 111 | 15 | 8 | 1 | 1 | 3.12 | 3.67 | 5/1 | ✓ |
| 6OD1/P39375/98-101-4 | 199 | 13 | 5 | 1 | 1 | 5.00 | 7.50 | 0/0 | ✓ |
| 6OD1/P39375/69-77-6 | 146 | 18 | 0 | 1 | 1 | 6.12 | 8.33 | 1/0 | ✓ |
| 7N0J/P64506/28-32-4 | 60 | 11 | 0 | 1 | 1 | 8.33 | 11.25 | 0/0 | ✓ |
| 7N0J/P64506/37-42-4 | 79 | 7 | 7 | — | 1 | 8.50 | 9.50 | 0/1 | — |
| 6KML/P64578/73-78-4 | 151 | 11 | 0 | 1 | 1 | 6.17 | 9.50 | 1/1 | ✓ |
| 6KML/P64578/62-65-7 | 127 | 15 | 6 | 1 | 1 | 7.12 | 7.75 | 1/0 | ✓ |
| 6HPC/P67697/9-13-4 | 22 | 9 | 3 | 1 | 1 | 6.00 | 8.00 | 1/0 | ✓ |
| 1NAQ/P69488/45-48-6 | 93 | 22 | 13 | 1 | 1 | 4.00 | 4.17 | 3/3 | ✓ |

## Full console execution output

```text
RULE_SHA256 ef88d6309cd941aeae63eef4fc5a346c193b66cd9d3355c5d95c0b58256ffba4
SLOT_WORDS {"A": [0, 0], "C": [0, 0], "D": [0, 4], "E": [0, 4], "F": [0, 0], "G": [0, 0], "H": [1, 1], "I": [0, 0], "K": [3, 0], "L": [0, 0], "M": [0, 0], "N": [2, 2], "P": [0, 0], "Q": [2, 2], "R": [5, 0], "S": [1, 2], "T": [1, 2], "V": [0, 0], "W": [1, 0], "Y": [1, 2]}
PREDICTIONS_SEALED_HAIRPINS 143 SHA256 03b2aa98d86642b4155df76282fa87fde58d871d3a49e3eda162e8a7e521d279
ABSTENTIONS 5
BURIAL_NONLOCAL_CB_TO_CA_8A
TESTED 136 of 143 MATCH 105 FLIP_NULL 31 ALWAYS_EVEN 44 ALWAYS_ODD 92
MATCH_RATE 0.772059 FLIP_RATE 0.227941
BINOM_UPPER_0.5 6.63172e-11
WATER_ORDERED_CB_WITHIN_4A
WET_FACE_WATERS 360 940 0.383
DRY_FACE_WATERS 202 860 0.2349
SAME_SIDE_ARMS 509 / 772
FACE_SIGN_CONSISTENCY [('even', 0.765), ('odd', 0.754)]
MATCH_BY_K [(3, 2, 3), (4, 46, 60), (5, 0, 1), (6, 35, 45), (7, 2, 2), (8, 15, 20), (10, 1, 1), (11, 1, 1), (12, 3, 3)]
SLOT_MARGINS Counter({2: 13, 7: 12, 5: 12, 4: 12, 6: 10, 9: 10, 11: 9, 3: 7, 1: 7, 18: 6, 8: 6, 15: 6, 12: 5, 0: 5, 19: 4, 13: 3, 23: 3, 16: 3, 10: 2, 22: 2, 17: 2, 35: 1, 14: 1, 26: 1, 20: 1})
WATER_PER_HAIRPIN_WET_GT_DRY 89 32 17
OFFSET_DRY_SIDE_NOT_IDENTIFIABLE e.NH->s.O and (s-1).NH->e.O are directional bonds on a topology; no oriented surface normal follows from indices alone.
EXAMPLE 2F1F/P00894/36-41-6 slots 21 3 pred 1 burial 7.12 6.83 hit False
EXAMPLE 5WQV/P07013/37-40-12 slots 18 28 pred 0 burial 6.43 5.67 hit True
EXAMPLE 5WQV/P07013/78-81-6 slots 18 0 pred 1 burial 4.88 7.33 hit True
EXAMPLE 5WQV/P07013/18-22-4 slots 12 5 pred 1 burial 4.5 5.75 hit True
EXAMPLE 7WW6/P08337/74-77-6 slots 12 17 pred 0 burial 7.12 6.17 hit True
EXAMPLE 1FS0/P0A6E6/53-57-6 slots 9 12 pred 0 burial 6.0 5.17 hit True
EXAMPLE 1FS0/P0A6E6/7-15-4 slots 3 9 pred 0 burial 7.67 6.0 hit True
RESULTS_JSON /mnt/data/NEXUS_Face_Value_Channel_v03_results.json 97043
POSTHOC_DIAGNOSTICS_BEGIN
MODE raw tested 136 hit 105 accuracy 0.77206 predict_even/odd/tie 50 88 5 pair_counts {(1, 0): 13, (0, 0): 31, (1, 1): 74, (0, 1): 18}
MODE density tested 136 hit 101 accuracy 0.74265 predict_even/odd/tie 64 74 5 pair_counts {(1, 0): 9, (0, 0): 37, (1, 1): 64, (0, 1): 26}
MODE exclude_crease tested 130 hit 99 accuracy 0.76154 predict_even/odd/tie 62 70 11 pair_counts {(1, 0): 6, (0, 0): 36, (1, 1): 63, (0, 1): 25}
MODE binary tested 133 hit 100 accuracy 0.75188 predict_even/odd/tie 65 70 8 pair_counts {(1, 0): 7, (0, 0): 38, (1, 1): 62, (0, 1): 26}
SHUFFLE_RAW_CONDITIONAL observed_hit 105 observed_n 136 null_mean_hit 75.273 null_mean_N 133.365 upper_tail_hit 0.00033
PRIMARY_CORRECT_EVEN/ODD 31 74
POSTHOC_DIAGNOSTICS_END
STAGGER_OFFSET_EXPLORATORY {'eligible': 46, 'dry_same_side_as_offset': 27, 'dry_opposite_side_to_offset': 19} EXAMPLES [('5WQV/P07013/18-22-4', -0.62, -3.56, True), ('1FS0/P0A6E6/53-57-6', 0.13, -3.56, False), ('1FS0/P0A6E6/7-15-4', 0.97, -2.22, False), ('1XEO/P0A6K3/111-115-6', -0.46, -3.48, True), ('1JKE/P0A6M4/12-20-11', 0.7, -2.46, False)]
MCNEMAR_VS_ALWAYS_ODD raw improve 31 worsen 18 exact_p 0.085433
MCNEMAR_VS_ALWAYS_ODD density improve 37 worsen 26 exact_p 0.207368
MCNEMAR_VS_ALWAYS_ODD exclude_crease improve 36 worsen 25 exact_p 0.200031
MCNEMAR_VS_ALWAYS_ODD binary improve 38 worsen 26 exact_p 0.168643
BOOTSTRAP_BLOCKS 91 HIT_CI95 [0.6985294117647058, 0.8428571428571429] GAIN_VS_ALWAYS_ODD_CI95 [0.0, 0.1875117481203008]
RING_PAIR_TRANSPOSITION PASS widths m=2..7 off diagonal (native P sends W(i,j)->W(j,i))

```

## Complete single-cell runnable source

The code below is the script that produced this audit and trace. Run as one Jupyter cell, with NumPy installed and `NEXUS_Fold_Compiler_Notebook (2).zip` in `/mnt/data` or your working directory. It writes the full machine-readable per-hairpin table to `/mnt/data/NEXUS_Face_Value_Channel_v03_results.json`.

```python
"""NEXUS zipper face / water slot test. Requires numpy and original Notebook ZIP.
   Single file; paste entirety into one Jupyter cell to execute.
   Frozen predictions logged and SHA256'd before structural readout.
"""
import collections, hashlib, json, math, zipfile
from pathlib import Path
import numpy as np

ZIP = Path('/mnt/data/NEXUS_Fold_Compiler_Notebook (2).zip')
if not ZIP.exists(): ZIP=Path('NEXUS_Fold_Compiler_Notebook (2).zip')
with zipfile.ZipFile(ZIP) as z:
    RAW=json.loads(z.read('NEXUS_Fold_Compiler_Notebook/data/ecoli_chains.json'))
    WAT_LIST=json.loads(z.read('NEXUS_Fold_Compiler_Notebook/data/ecoli_water.json'))
WAT={(e['acc'],e['set']):e for e in WAT_LIST}

# Side-chain count of water-facing R2 slot types: H=11, acceptor LP=00.
# Coarse count: standard neutral/physiological microstate, sulfur excluded, simplified carboxyl delocalization.
# Pair order is (#hydrogen H slots, #unshared acceptor pair slots).
SLOTS={
 'A':(0,0),'C':(0,0),'D':(0,4),'E':(0,4),'F':(0,0),
 'G':(0,0),'H':(1,1),'I':(0,0),'K':(3,0),'L':(0,0),
 'M':(0,0),'N':(2,2),'P':(0,0),'Q':(2,2),'R':(5,0),
 'S':(1,2),'T':(1,2),'V':(0,0),'W':(1,0),'Y':(1,2)
}
assert len(SLOTS)==20
RULE='Face t parity. Each residue sidechain slots count H=11 and pair=00; sum per even and odd t across both rails (e-t,s+t). Lower count predicts dry. If equal, abstain. Flip null inverts selected parity. Burial read from nonlocal C-alpha density within 8A around sidechain C-beta; water read >=1 ordered O within 4A of C-beta. No fitted thresholds; conditional e,s,k from structure.'
print('RULE_SHA256',hashlib.sha256(RULE.encode()).hexdigest())
print('SLOT_WORDS',json.dumps(SLOTS,sort_keys=True))

# stage A: window detection recovers e,s,k from UNDIRECTED observed nearest backbone pairs;
# this is structural conditioning, NOT a sequence-only hairpin detector.
geo=[]; hp=[]
for ci,ent in enumerate(RAW):
    R=ent['residues']; L=len(R)
    if L<30: geo.append(None); continue
    seq=''.join(r[1] for r in R)
    N=np.asarray([r[2] for r in R],float)
    O=np.asarray([r[5] for r in R],float)
    dd=np.linalg.norm(N[:,None,:]-O[None,:,:],axis=2)
    idx=np.arange(L); dd[np.abs(idx[:,None]-idx[None,:])<=2]=np.inf
    directed=set()
    for i in range(1,L):
        if seq[i]=='P':continue
        j=int(dd[i].argmin())
        if dd[i,j]<=3.5: directed.add((i,j))
    geo.append((L,seq,directed))
    und={(min(i,j),max(i,j)) for i,j in directed}
    byS=collections.defaultdict(list)
    for a,b in und: byS[a+b].append((a,b))
    for S,pts in byS.items():
        pts=sorted(set(pts)); run=[pts[0]]
        for p in pts[1:]+[None]:
            if p is not None and p[0]-run[-1][0]<=2:
                run.append(p);continue
            if len(run)>=3 and run[-1][1]-run[-1][0]<=8:
                e,s=run[-1]; k=min(e-run[0][0],e,L-1-s)
                hp.append((ci,e,s,k,S))
            if p is not None: run=[p]
assert len(hp)==143, f'detector returned {len(hp)} not 143'

# stage B: pure sequence-side predictions sealed, before Cbeta, water or burial are read
PRED=[]
for ci,e,s,k,S in hp:
    seq=geo[ci][1]
    a=[0,0]; h=[0,0]; lp=[0,0]; letters=[[],[]]
    for t in range(k+1):
        for rid in (e-t,s+t):
            hh,pp=SLOTS[seq[rid]]
            h[t%2]+=hh; lp[t%2]+=pp; a[t%2]+=hh+pp
            letters[t%2].append((rid,seq[rid]))
    dry=0 if a[0]<a[1] else (1 if a[1]<a[0] else None)
    PRED.append({'id':f'{RAW[ci]["pdb"]}/{RAW[ci]["acc"]}/{e}-{s}-{k}',
                 'chain_index':ci,'e':e,'s':s,'k':k,'S':S,
                 'even_slots':a[0],'odd_slots':a[1],
                 'even_H':h[0],'odd_H':h[1],'even_LP':lp[0],'odd_LP':lp[1],
                 'dry_parity':dry,'residue_rows':letters})
blob=json.dumps(PRED,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
seal=hashlib.sha256(blob).hexdigest()
print('PREDICTIONS_SEALED_HAIRPINS',len(PRED),'SHA256',seal)
print('ABSTENTIONS',sum(p['dry_parity'] is None for p in PRED))

# Stage C: read structure and water after freezing predictions.
# Cbeta missing for Gly: use C-alpha as explicitly disclosed proxy; missing other Cbeta likewise.
# Burial count: sequence-nonlocal C-alpha contacts <8 A to each CB proxy, |i-j|>3.
# Water: any crystal O within 4 A CB proxy; does not imply true solvent accessibility.
REPORT=[]
all_par=collections.Counter(); water_assoc=[]; same_side=[]
for p in PRED:
    ci=p['chain_index'];ent=RAW[ci];R=ent['residues'];L=len(R)
    CA=np.asarray([r[3] for r in R],float)
    B=np.asarray([r[6] if len(r)>6 and isinstance(r[6],list) and len(r[6])==3 else r[3] for r in R],float)
    real_CB=np.asarray([len(r)>6 and isinstance(r[6],list) and len(r[6])==3 for r in R],bool)
    # check for protein residue cross interactions (all nonlocal CA)
    dist=np.linalg.norm(B[:,None,:]-CA[None,:,:],axis=2)
    idx=np.arange(L); dist[np.abs(idx[:,None]-idx[None,:])<=3]=np.inf
    neighbours=(dist<8).sum(axis=1)
    wat=WAT.get((ent['acc'],ent['set']),{'waters':[]})
    WX=np.asarray([w[:3] for w in wat['waters']],float).reshape(-1,3)
    if len(WX):
        dw=np.linalg.norm(B[:,None,:]-WX[None,:,:],axis=2)
        water=(dw<=4).any(axis=1)
        ndist=dw.min(axis=1)
    else:
        water=np.zeros(L,bool);ndist=np.full(L,float('inf'))
    e,s,k=p['e'],p['s'],p['k']
    face_idx=[[j for t in range(k+1) if t%2==q for j in (e-t,s+t)] for q in (0,1)]
    # mean raw burial density: no fitting
    burial=[float(np.mean(neighbours[x])) for x in face_idx]
    water_n=[int(water[x].sum()) for x in face_idx]
    water_denom=[len(x) for x in face_idx]
    # actual β side-chain sign consistency, using local normal only for the read-back.
    # n=cross(outgoing strand tangent, bridge vector), global orientation cancels in comparison
    normal=np.cross(CA[e-1]-CA[e],CA[s]-CA[e]) if e>=1 else np.zeros(3)
    norm=float(np.linalg.norm(normal)); flipcount=0;samecount=0;signs={0:[],1:[]}
    if norm>1e-8:
        normal/=norm
        for t in range(k+1):
            l,r=e-t,s+t
            if real_CB[l] and real_CB[r]:
                dl=float(np.dot(B[l]-CA[l],normal));dr=float(np.dot(B[r]-CA[r],normal))
                if abs(dl)>0.05 and abs(dr)>0.05:
                    samecount+=(dl*dr>0);flipcount+=1
            for j in (l,r):
                if real_CB[j]:
                    dp=float(np.dot(B[j]-CA[j],normal))
                    if abs(dp)>0.05:signs[t%2].append(1 if dp>0 else -1)
    frac_consistent={q:(max(signs[q].count(1),signs[q].count(-1))/len(signs[q]) if signs[q] else None) for q in (0,1)}
    pred=p['dry_parity']
    # truth: higher nonlocal density => more buried; ties in density are unscored
    actual=0 if burial[0]>burial[1] else (1 if burial[1]>burial[0] else None)
    match=(pred==actual) if pred is not None and actual is not None else None
    r={**{kk:vv for kk,vv in p.items() if kk!='residue_rows'},
       'nres_even':len(face_idx[0]),'nres_odd':len(face_idx[1]),'burial_even':burial[0], 'burial_odd':burial[1],
       'actual_dry':actual,'match':match,'water_even':water_n[0], 'water_odd':water_n[1],
       'water_den_even':water_denom[0], 'water_den_odd':water_denom[1],
       'both_arms_same_side':samecount,'both_arms_count':flipcount,
       'cb_sign_consistency_even':frac_consistent[0], 'cb_sign_consistency_odd':frac_consistent[1]}
    REPORT.append(r)

labelled=[r for r in REPORT if r['match'] is not None]
hits=sum(x['match'] for x in labelled)
flipped=len(labelled)-hits
base_even=sum(r['actual_dry']==0 for r in labelled)
base_odd=len(labelled)-base_even
print('BURIAL_NONLOCAL_CB_TO_CA_8A')
print('TESTED',len(labelled),'of',len(REPORT),'MATCH',hits,'FLIP_NULL',flipped,'ALWAYS_EVEN',base_even,'ALWAYS_ODD',base_odd)
print('MATCH_RATE',round(hits/max(1,len(labelled)),6),'FLIP_RATE',round(flipped/max(1,len(labelled)),6))
# exact binomial sign test to 0.5; cannot fit based on data
from math import comb
n=len(labelled); k=hits
p_upper=sum(comb(n,i) for i in range(k,n+1))/2**n if n else float('nan')
print('BINOM_UPPER_0.5',f'{p_upper:.6g}')
print('WATER_ORDERED_CB_WITHIN_4A')
wet=[r for r in REPORT if r['dry_parity'] is not None]
wet_on_pred=sum(r['water_odd' if r['dry_parity']==0 else 'water_even'] for r in wet)
wet_n_pred=sum(r['water_den_odd' if r['dry_parity']==0 else 'water_den_even'] for r in wet)
dry_on_pred=sum(r['water_even' if r['dry_parity']==0 else 'water_odd'] for r in wet)
dry_n_pred=sum(r['water_den_even' if r['dry_parity']==0 else 'water_den_odd'] for r in wet)
print('WET_FACE_WATERS',wet_on_pred,wet_n_pred,round(wet_on_pred/max(1,wet_n_pred),4))
print('DRY_FACE_WATERS',dry_on_pred,dry_n_pred,round(dry_on_pred/max(1,dry_n_pred),4))
print('SAME_SIDE_ARMS',sum(r['both_arms_same_side'] for r in REPORT),'/',sum(r['both_arms_count'] for r in REPORT))
print('FACE_SIGN_CONSISTENCY',[(q,round(float(np.mean([r['cb_sign_consistency_'+q] for r in REPORT if r['cb_sign_consistency_'+q] is not None])),3)) for q in ('even','odd')])
print('MATCH_BY_K',sorted([(kk, sum(r['match'] for r in labelled if r['k']==kk),sum(r['k']==kk for r in labelled)) for kk in sorted({r['k'] for r in REPORT})]))
print('SLOT_MARGINS',collections.Counter(abs(r['even_slots']-r['odd_slots']) for r in REPORT))
# score water presence per hairpin non-parametric paired sign, explicit
w_wins=w_losses=w_ties=0
for r in wet:
    wet_fraction=r['water_odd' if r['dry_parity']==0 else 'water_even']/max(1,r['water_den_odd' if r['dry_parity']==0 else 'water_den_even'])
    dry_fraction=r['water_even' if r['dry_parity']==0 else 'water_odd']/max(1,r['water_den_even' if r['dry_parity']==0 else 'water_den_odd'])
    if wet_fraction>dry_fraction:w_wins+=1
    elif wet_fraction<dry_fraction:w_losses+=1
    else:w_ties+=1
print('WATER_PER_HAIRPIN_WET_GT_DRY',w_wins,w_losses,w_ties)
# predeclared informational diagnostics: expected no specific curling sign w/o orientation mapping.
print('OFFSET_DRY_SIDE_NOT_IDENTIFIABLE', 'e.NH->s.O and (s-1).NH->e.O are directional bonds on a topology; no oriented surface normal follows from indices alone.')
for r in REPORT[:7]:
    print('EXAMPLE',r['id'],'slots',r['even_slots'],r['odd_slots'],'pred',r['dry_parity'],'burial',round(r['burial_even'],2),round(r['burial_odd'],2),'hit',r['match'])
OUT=Path('/mnt/data/NEXUS_Face_Value_Channel_v03_results.json')
OUT.write_text(json.dumps({'input_zip':ZIP.name,'rule_sha256':hashlib.sha256(RULE.encode()).hexdigest(),'prediction_sha256':seal,'slots':SLOTS,'reports':REPORT},indent=2,allow_nan=False))
print('RESULTS_JSON',str(OUT),OUT.stat().st_size)

# IMPORTANT POST-HOC DIAGNOSTICS, motivated by the unequal face sizes and class imbalance.
# Not part of the previously printed rule seal, labelled exploratory and not a new seal.
print('POSTHOC_DIAGNOSTICS_BEGIN')
from collections import Counter

def vote(a,b):return 0 if a<b else (1 if b<a else None)
def calc_mode(p,mode='density', seq_override=None):
    ci,e,s,k=p['chain_index'],p['e'],p['s'],p['k']
    seq=geo[ci][1] if seq_override is None else seq_override
    scores=[0,0]; sizes=[0,0]
    for t in range(0 if mode!='exclude_crease' else 1,k+1):
        for pos in (e-t,s+t):
            sizes[t%2]+=1
            hh,lp=SLOTS[seq[pos]]
            scores[t%2]+=(hh+lp if mode!='binary' else int(hh+lp>0))
    if mode in ('density','exclude_crease','binary'):
        scores=[x/max(1,z) for x,z in zip(scores,sizes)]
    return vote(*scores)

truth={r['id']:r['actual_dry'] for r in REPORT}
for mode in ('raw','density','exclude_crease','binary'):
    m=[]; pcounts=Counter(); pairs=Counter()
    for p in PRED:
        v=calc_mode(p,mode) if mode!='raw' else p['dry_parity']
        t=truth[p['id']]
        pcounts[v]+=1
        if v is not None and t is not None:
            m.append(int(v==t))
            pairs[(v,t)]+=1
    print('MODE',mode,'tested',len(m),'hit',sum(m),'accuracy',round(sum(m)/max(1,len(m)),5),'predict_even/odd/tie',pcounts[0],pcounts[1],pcounts[None],'pair_counts',dict(pairs))

# sequence shuffle within each detected hairpin: same residue multiset, same unequal parity sizes, no fitting
rng=np.random.default_rng(193)
shuffles=3000
baseline=[]
for z in range(shuffles):
    hit=n_scored=0
    for p in PRED:
        ci,e,s,k=p['chain_index'],p['e'],p['s'],p['k']
        rows=[q for t in range(k+1) for q in (e-t,s+t)]
        vals=[sum(SLOTS[geo[ci][1][r]]) for r in rows]
        v=np.asarray(vals,dtype=int)[rng.permutation(len(vals))]
        a=[int(v[np.arange(len(v))//2%2==j].sum()) for j in (0,1)]
        pred=vote(*a)
        t=truth[p['id']]
        if pred is not None and t is not None:
            n_scored+=1; hit+=pred==t
    baseline.append((hit,n_scored))
observed_primary=sum(r['match'] for r in REPORT if r['match'] is not None)
N_primary=len(labelled)
basehit=np.asarray([h for h,n in baseline]); basen=np.asarray([n for h,n in baseline]);
print('SHUFFLE_RAW_CONDITIONAL','observed_hit',observed_primary,'observed_n',N_primary,
      'null_mean_hit',round(float(basehit.mean()),3),'null_mean_N',round(float(basen.mean()),3),
      'upper_tail_hit',round(float((1+sum(basehit>=observed_primary))/(shuffles+1)),5))
# Paired dominance check vs majority parity under the SAME labelled denominator
raw_lab=[r for r in REPORT if r['match'] is not None]
a=sum(r['match'] and r['actual_dry']==0 for r in raw_lab)
b=sum(r['match'] and r['actual_dry']==1 for r in raw_lab)
print('PRIMARY_CORRECT_EVEN/ODD',a,b)
print('POSTHOC_DIAGNOSTICS_END')
# Exploratory bimetal read-back (NOT a sequence-derived crease/curl predictor).
# Only evaluate explicit staggered return bond (s-1).NH -> e.O with e.NH -> s.O,
# and a nondegenerate local plane. Native plane normal n = (CA[e-1]-CA[e]) x (CA[s]-CA[e]).
# Dry-face orientation is sign of median actual sidechain CB displacement w.r.t n.
# Offset side is sign of (CA[s-1]-sheet_edge_midpoint) dot n.
# This is a geometrical association, NOT proof of a causal torque or curvature.
bi=Counter(); examples=[]
for p in PRED:
    e,s,k=p['e'],p['s'],p['k'];ci=p['chain_index']
    if s-e<=3: continue
    dirset=geo[ci][2]
    if (e,s) not in dirset or (s-1,e) not in dirset: continue
    pred=p['dry_parity'];
    if pred is None:continue
    R=RAW[ci]['residues'];CA=np.asarray([r[3] for r in R],float)
    B=np.asarray([r[6] if len(r)>6 and isinstance(r[6],list) else r[3] for r in R],float)
    present=np.asarray([len(r)>6 and isinstance(r[6],list) for r in R])
    normal=np.cross(CA[e-1]-CA[e], CA[s]-CA[e]);mag=float(np.linalg.norm(normal))
    if mag<1e-8:continue
    normal/=mag
    scores=[]
    for t in range(k+1):
        if t%2==pred:
            for j in (e-t,s+t):
                if present[j]:scores.append(float(np.dot(B[j]-CA[j],normal)))
    if not scores:continue
    dry_side=float(np.median(scores))
    offset=float(np.dot(CA[s-1]-(CA[e]+CA[s])/2,normal))
    if abs(dry_side)<0.05 or abs(offset)<0.05:continue
    bi['eligible']+=1
    side_agrees=(dry_side*offset>0)
    bi['dry_same_side_as_offset']+=side_agrees
    bi['dry_opposite_side_to_offset']+=not side_agrees
    if len(examples)<5:examples.append((p['id'],round(dry_side,2),round(offset,2),bool(side_agrees)))
print('STAGGER_OFFSET_EXPLORATORY',dict(bi),'EXAMPLES',examples)
# Direct McNemar (raw/density vs always-odd) exact two-sided binomial discordances.
for mode in ('raw','density','exclude_crease','binary'):
    good=bad=0
    for p in PRED:
        v=calc_mode(p,mode) if mode!='raw' else p['dry_parity']
        t=truth[p['id']]
        if t is None or v is None:continue
        if v==0 and t==0:good+=1
        if v==0 and t==1:bad+=1
    n=good+bad
    pv=min(1.0,2*sum(comb(n,i) for i in range(0,min(good,bad)+1))/2**n) if n else float('nan')
    print('MCNEMAR_VS_ALWAYS_ODD',mode,'improve',good,'worsen',bad,'exact_p',round(pv,6))
# Chain-blocked bootstrap (exploratory), to avoid treating hairpins in one PDB as independent.
series=collections.defaultdict(list)
for p in PRED:
    r=next(rr for rr in REPORT if rr['id']==p['id'])
    if r['match'] is not None:
        series[p['chain_index']].append((int(r['match']), int(r['actual_dry']==1)))
chains=list(series)
rng2=np.random.default_rng(194)
diffs=[]; hits_boot=[]
for _ in range(4000):
    selected=rng2.choice(chains,len(chains),replace=True)
    vals=[v for ci in selected for v in series[int(ci)]]
    arr=np.asarray(vals)
    if len(arr):
        hits_boot.append(float(arr[:,0].mean()))
        diffs.append(float((arr[:,0]-arr[:,1]).mean()))
ci_hit=np.quantile(hits_boot,[0.025,0.975]);ci_diff=np.quantile(diffs,[0.025,0.975])
print('BOOTSTRAP_BLOCKS',len(chains),'HIT_CI95',ci_hit.tolist(),'GAIN_VS_ALWAYS_ODD_CI95',ci_diff.tolist())
# Independent exact ring arithmetic (no protein data): directed pair transposition.
def rev(x,n):return int(f'{x:0{n}b}'[::-1],2)
def comp(x,n):return x ^ ((1<<n)-1)
def native(x,n):
    j=rev(x,n)
    return comp(x,n) if j==x else j
for m in range(2,8):
    for i in range(1<<m):
        for j in range(1<<m):
            if i!=j:
                w=(i<<m)|rev(j,m)
                ww=(j<<m)|rev(i,m)
                assert native(w,2*m)==ww
print('RING_PAIR_TRANSPOSITION','PASS widths m=2..7 off diagonal (native P sends W(i,j)->W(j,i))')

```

## Precise next prompt

> Continue NEXUS §195 from the §194 zipper value-channel audit.
> 
> The conditional face reader tested 143 detected E. coli hairpins. The sequence-side side-chain R2 slot tally predicted the structurally more buried face in 105/136 scorable cases (77.2%); after normalizing by face size, 101/136 (74.3%). Ordered waters contacted 38.3% of residues on the predicted wet face and 23.5% on the predicted dry face. But always-odd already predicts 92/136, so the raw gain of 13 has paired p=0.085; an independent sequence placement shuffle is favorable (p≈0.00033). On an actual structural local normal, only 509/772 matched row pairs have side chains pointing to the same geometric side. The crease-offset proxy agrees with the dry side 27/46 (p≈0.30). This is conditional readback, because e,s,k are derived from solved structures; it is NOT a sequence-only fold prediction.
> 
> Go one transformation upstream without inventing a new binary cutoff. Examine the physical *interface that orients the two strand faces and selects a distant partner*: sequence-derived side-chain shape/rotamer and the surrounding competing solvent/other-strand surfaces. Separate the mathematical pair-ring transposition from the atomistic side-chain orientation, and resolve the false same-face assumption on actual antiparallel strands.
> 
> First specify an executable, orientation-invariant construction of strand-local face normals from covalent geometry, and derive when the two rail parities denote the same actual face (or the opposite). Check this on synthetic ideal antiparallel sheets, then on the 143 existing hairpins. Do not peek at burial/water to choose a phase. Recheck the slot→burial/water association on orientation-consistent subsets against a proper always-parity baseline, sequence shuffles and chain-block held-out splits.
> 
> Only if a sequence-only observable selects the orientation and strand partner should you seal a new forward prediction. Do not infer an independent crease address from these observed hairpins. Include full code in one runnable Jupyter cell, the entire execution log, 143-row trace, one downloadable Markdown artifact, and a STANDS/RUNS/OPEN/DEAD END ledger.
> 
> Finish with the next precise prompt for the following round.


---
**Audit generated from exact executed script and original mounted files.**
