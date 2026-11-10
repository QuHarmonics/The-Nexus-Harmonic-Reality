# NEXUS two-operand helix-end control — independent execution

Date: 2026-10-29. Source: `NEXUS_Fold_Compiler_Notebook (2).zip`, `data/ecoli_chains.json` and `data/ecoli_water.json`. Script: `NEXUS_Two_Operand_End_Control_v01.py`. Dataset: 155 chains, 16,877 residues, 666 merged T3/T4 helix runs. This is **retrospective**, using already-solved coordinate models and a 3.5-Å N-to-O proximity rule.

## Reproduction of pasted calculation

The pasted `99` free-donor endpoints and `73` satisfying at least one of four flags reproduce when side-chain N/O atoms are ignored for a structure with no ordered crystal waters. This condition occurs in the supplied expression `if we['waters'] else np.zeros((0,3))` even for `sidechain_NO`. After retaining side-chain atoms independently of water availability, the count is 98 endpoints, 72 flagged. The changed case is `4MTD`, accession `P0AC51`, at a putative continuation from donor 16 to 17 (zero-based segment indices).

Of the corrected 98 free-donor endpoints, 39 have glycine within the nominated window, 33 have an ordered water within 3.5 Å of the projected carbonyl oxygen, 12 have a side-chain nitrogen near that carbonyl, 21 have the next subsequent residue occupied or proline. These overlap; the union is 72/98 (73.5%). Without the `next step` marker, the union is 65/98 (66.3%).

## Continuation controls

To avoid interpreting marks as causes merely because they occur at endpoints, the same flags were evaluated at 3,747 observed helix steps where the next donor **does** close onto the carbonyl indicated by the same T3/T4 register (immediate adjacent step, unchanged k). Rates:

| Marker | Corrected free-donor endpoints (n=98) | Observed continuing closures (n=3,747) |
|---|---:|---:|
| Gly in a four-residue C-cap-like window | 39/98 (39.8%) | 554/3,747 (14.8%) |
| Water within 3.5 Å of projected carbonyl O | 33/98 (33.7%) | 784/3,747 (20.9%) |
| Side-chain N within 3.5 Å of projected carbonyl O | 12/98 (12.2%) | 173/3,747 (4.6%) |
| Subsequent position (+2) already closes or proline | 21/98 (21.4%) | 3,523/3,747 (94.0%) |
| Any of all four | 72/98 (73.5%) | 3,653/3,747 (97.5%) |
| Any of first three | 65/98 (66.3%) | 1,356/3,747 (36.2%) |

There is an association for some flags, notably local glycine and carbonyl surroundings, **but there is no deterministic stop rule**. The +2 condition is more prevalent while nodes continue; combining it into a four-way stop flag makes the classification especially misleading.

For all 98 corrected free-donor ends, the N atom of the projected next donor is **more than 3.5 Å from the register-predicted carbonyl O** in the already solved coordinates (median 5.837 Å); as a contrasting read-back, all 3,747 observed same-register continuing contacts satisfy the distance cutoff (median 2.966 Å). This geometrical distinction is conditioned on the observed closure definition and cannot predict the fold in advance. Water contact does not exclude a backbone N–H closure: 784 continuing contacts coexist with water within 3.5 Å of the target O.

## Accounting issue

The pasted claim combines `1,192/1,289` previously assigned endings with `73/99` from a new selection to state `1,265/1,289` (~98%). These have **not** been shown to be a disjoint partition of the same 1,289 endpoints. The earlier remaining count is 97; the new sample contains 99 (98 after correcting the side-chain check). Therefore simply adding 73 cannot establish 1,265 distinct explained endpoints. Also, at most a geometric co-occurrence is assigned, not a cause of ending.

## Verdict

- **RUNS:** both-operand inspection, 73/99 original result, corrected 72/98 result, and control rates.
- **STANDS:** the pair word has two operands; register-predicted contacts can be checked directly on structural coordinates.
- **OPEN:** whether water, side-chain contacts, glycine, or their time-dependent competition actually *causes* a new helix to terminate; which upstream transformations determine the ensuing geometry.
- **DEAD END:** promoting the four-way union into a deterministic physical stop rule, and deriving 98% causally explained node ends from nonmatched populations.

This control should be recorded as a qualified, retrospective association, not as a new resolution of the forward emitter. A future thermophile/mesophile homolog comparison would also require explicit residue alignment and independent separation of sequence effects from temperature and other crystallographic differences.
