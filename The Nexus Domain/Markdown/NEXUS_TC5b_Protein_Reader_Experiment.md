# NEXUS protein reader experiment: TC5b (1L2Y)

**Date:** 26 October 2026  
**Status:** RUNS (exact finite honeycomb enumeration and contact-data scoring), physical fold prediction not supported by this first test.  
**Pre-comparison seal (SHA-256 of canonical prediction JSON):** `56a60011b3d264a2eeb7e8667388a48d0239b0ad26ed4d92490d309208a8f9fc`

## Question

Can an actual protein primary sequence select a turn-word shape using the NEXUS honeycomb compiler (§§144–165), without measuring the destination structure first?

## Source and input

Trp-cage miniprotein TC5b, PDB **1L2Y**, is a chemically synthesized 20-residue peptide rather than a sequence with a unique, documented native gene. **The gene/codon-to-protein layer is therefore not asserted.** Its published amino-acid sequence is `NLYIQWLKDGGPSSGRPPPS` (BMRB 5292, RCSB 1L2Y).

A declared binary HP classification uses H letters `ACFGILMPVWY` (sorted letters in the executable manifest are authoritative), with all other amino acids P. The resulting word is `PHHHPHHPPHHHPPHPHHHP`. This is a coarse HP label assignment; in particular, treatment of glycine and proline as H is model-dependent, not a biochemical derivation.

## Predeclared method

- Fix the first bond of a 2D honeycomb path. Interpret each of 18 turns as ±60°; reject self-intersections.
- Confirm known counts for 2–10 turn words: 4, 8, 16, 30, 58, 112, 216, 406, 776 (record §§144–145).
- Score all valid paths by number of nonconsecutive nearest-neighbor H–H pairs, requiring residue-index separation ≥3. Maximize the score.
- Among minimum-energy (maximum-contact) paths, sort possible contacts by frequency (tie-break by ascending residue indices); nominate eight pairs. Freeze them in JSON and SHA-256 *before consulting PDB coordinates*.
- Held-out readout: count Cα–Cα distances ≤8.0 Å in all 38 NMR models; a consensus contact occurs in ≥19 models.
- Compare the eight selected pairs with all eligible H–H pairs and the exact uniform-set hypergeometric null. A random-set baseline is a reference distribution, not proof of physical prediction.

## Frozen lattice result

Of 262,144 possible 18-turn words, **125,168** yield self-avoiding honeycomb paths. The maximum contact score is **4**, attained by **4** paths. The lexicographically first turn word is `010100111101101010` (hex `14f6a`), whose exact native `R18` address is **71,885**.

The sealed eight predictions, in one-based residue coordinates:

`(2,7), (2,19), (4,17), (6,11), (6,15), (7,12), (10,19), (12,17)`.

Each predicted pair belongs to **2 of the 4** maximum-scoring paths: there is no single unique contact configuration.

## Experimental result

The 1L2Y NMR coordinate ensemble contains **38** models, all matching the published peptide sequence. The public copy was fetched via the GitHub repository `spiwokv/md4structbioinf`, file `1L2Y.pdb`, Git blob SHA1 `aa15c9c8999f6f38ddf1e14a543f23aa92c757ac`. The official structure metadata are at https://www.rcsb.org/structure/1L2Y.

| Sealed residue pair | Conformers supporting contact | Consensus? |
|---|---:|---|
| 2–7 | 0/38 | No |
| 2–19 | 38/38 | Yes |
| 4–17 | 0/38 | No |
| 6–11 | 38/38 | Yes |
| 6–15 | 0/38 | No |
| 7–12 | 1/38 | No |
| 10–19 | 0/38 | No |
| 12–17 | 38/38 | Yes |

Of **54 eligible** H–H pairs, **18** are consensus contacts in the 38-model NMR ensemble. The sealed predictions hit **3/8 = 37.5%**, versus uniform-pair-set expected **8×18/54 = 2.6667** hits. Exact hypergeometric `Pr(overlap≥3) = 0.540080260`. The first binary HP→honeycomb selector does **not** significantly enrich the actual experimental contacts.

## Post-seal structural finding: two competing shape classes

The four contact-maximizing paths form exactly **two complement mirror pairs**. Mirror paths have identical H–H contact sets, as the record's honeycomb symmetry implies:

- **Shape A**: `010100111101101010` and `101011000010010101`; native addresses **71885, 146106**. Contacts `(2,19),(4,17),(6,15),(7,12)`. Of four contacts, one appears in the NMR consensus.
- **Shape B**: `011110000101111010` and `100001111010000101`; native addresses **183123, 102213**. Contacts `(2,7),(6,11),(10,19),(12,17)`. Of four contacts, two appear in the NMR consensus.

**Crucial:** The eight sealed contacts were the **union** of the two distinct contact topologies. They do not constitute a single simultaneously achievable conformation on the lattice. Selecting a path requires an interface that breaks this degeneracy. The mirror bit is *not* that selector; within a mirror pair the same shape information is retained.

Shape A has two `1001/0110` hexagon-exchange windows, at one-based turn-window positions 4 and 11; shape B has none. These are candidate local rewrite windows, **not** the 26-turn locks of §155 and not independently verified physically possible molecular moves.

## Architectural conclusion

The first reader stack is operational:

`AA sequence → HP word → 18-bit legal turn words → H–H contact relation → native R18 addresses → experimentally testable contact query`.

The missing selector is now localized: **HP input and lattice legality alone permit two distinct maximal contact topologies**, each with a mirror image. A next prediction must add a *predeclared* physical constraint (e.g., backbone chirality, peptide torsion restrictions, proline restrictions, side-chain geometry, or a larger tetrahedral/diamond interface) and test it against **a second held-out protein**, not tune this target after seeing its fold. The NMR ensemble is not 38 statistically independent experiments.

A true 2-bit DNA→6-bit codon→AA test will require a verified coding sequence from a naturally encoded protein, because TC5b is a synthetic peptide with no unique native transcript. Reverse translation would create invented gene data and is deliberately not used.

## Reproduce

Source and original data:
- NEXUS reference record §§144–165, in the supplied `NEXUS_Reference_Record_1-181.docx`
- TC5b sequence: https://bmrb.protein.osaka-u.ac.jp/data_library/summary/index.php?bmrbId=5292
- PDB coordinates: https://www.rcsb.org/structure/1L2Y
- Public archived coordinate copy: https://github.com/spiwokv/md4structbioinf

Run `python NEXUS_TC5b_gene_to_turn_test.py seal` to check the frozen seal and enumerate the lattice. After downloading the original PDB coordinate file, run `python NEXUS_TC5b_gene_to_turn_test.py score 1L2Y.pdb` for the 38-model comparison. The independent `NEXUS_TC5b_score_frozen_observations.py` reproduces the contact scoring using the 54 measured H–H pair counts supplied with this experiment. `NEXUS_TC5b_postseal_orbit_diagnostic.py` reproduces the distinct mirror/shape orbits.
