# NEXUS v03 — Local interaction torque and reversible backbone execution

**Execution ledger · 2026-10-29 / 30 · STANDS / RUNS / OPEN / DEAD END**  
**Reference input:** supplied `NEXUS_Fold_Compiler_Notebook (2).zip`, SHA256 prefix `8a8f6eef4de7ab09`.  
**Programs:** `NEXUS_Explicit_Torque_DI_v03.py` and the identical-source **single-cell** `.ipynb`.  
**Results:** 96 chain × model records, `NEXUS_Explicit_Torque_DI_v03_benchmark.json`; complete readable log with 96 records.

## Scope and no-leakage contract

The new interface is `current prefix geometry → hypothetical local interaction energy → finite torsional update → changed geometry`. Both the sequence and native structural coordinates are read from the original bundle. **Only amino-acid letters** enter the forward executor; native N/CA/C/O positions are used only by `metrics_v03` *after* each emitted candidate is complete. No target contacts, target torsions, PDB secondary-structure states, codons, field-optimized native fold, or future-residue coordinates enter prefix selection. The full chain is cached in all-α form to make rotations efficient, but its future atoms are not used by `model_energy(p,n)` before the current prefix reaches them.

The rings' partner/facing identities are mathematically separate from the free-energy model and do not select physical torsions. This protects the native ring's verified address identities against a failed physical assignment.

## Explicitly executed operations

1. **Place** ideal backbone N–CA–C and carbonyl oxygen with fixed bond lengths and angles; the initial all-α torsions are a strong fixed baseline. Place a virtual L-Cβ in the standard handedness, except glycine. The actual full side chain is *not* constructed.
2. **Orient** an explicit approximate amide hydrogen H at 1.01 Å from N using the normalized negative bisector of N→previous-C and N→CA, excluding proline. Compute direction-sensitive N–H···O=C interactions with N···O preferred 2.95 Å, donor alignment near linear and C–O···H near 120°. The smooth Gaussian parameters are hypotheses, not ab initio chemistry.
3. **Exclude** CA/CB/NO pair overlaps using positive short-range quadratic penalties with sequence-neighbor exclusions. No full AMBER/CHARMM electrostatics, all-atom van der Waals or bonded angle energy is included.
4. **Compete with water** using an **implicit** term that stabilizes exposed unsatisfied polar positions and diminishes as intramolecular hydrogen-bond satisfaction rises. This is not actual solvent molecules, chemical potential, explicit hydration-shell geometry or a calibrated solvation free energy.
5. **Transfer/rotate** the downstream subtree rigidly around phi or psi and accept only energy-reducing 30-degree candidates evaluated with the existing prefix. A deterministic scheduler examines one old hinge per **two** incoming residues, alternates phi/psi, and restricts eligibility to a four- or eight-residue lookback. A post-chain sweep additionally considers each hinge once. It is a deliberately fixed execution *budget*, not a molecular time step or validated kinetics.

The illustrative weights were fixed before benchmarking: `{'steric_ca': 2.6, 'steric_cb': 1.2, 'steric_polar': 0.9, 'hb': 2.4, 'hydrophobe': 0.17, 'water': 0.65, 'torsion': 0.045}`. Energy outputs are in arbitrary **toy units**, not kcal/mol, and should not be interpreted as physical conformational free energy. 

## Small-system validation **before** use on protein structures

| Test | Observed result | Status |
|---|---|---|
| Four-atom N–H···O=C pair optimum | -2.400000 toy-energy units; off-angle placement less favorable | RUNS |
| Global translation and rotation of pair | Energy invariant to 1e-10 | STANDS for constructed kernel |
| Independent Cartesian finite-difference forces | Net-force norm 4.44e-11; net-torque norm 1.37e-10 | RUNS |
| Angular torque sign | 0.126656 toy-energy/radian; small step along it lowers energy | RUNS |
| Backbone psi torque sign | -0.041351 toy-energy/radian, finite difference | RUNS |
| Repulsion and solvent trend | Overlap penalty rises as separation decreases; exposed unsatisfied groups get more hydration reward | RUNS (formula sanity) |
| Stereo/rotamers | L-Cβ determinant 2.504142; three distinct χ1 pseudo-Cγ placements with fixed CB–CG bond | RUNS as *geometry only* |
| Covalent invariants | All modeled peptide N–CA, CA–C, C–N distances and trans-ω remain within asserted numerical tolerance through rigid downstream updates | STANDS for rigid transform |

**Important limitation:** This kernel does **not** execute full side-chain χ1/χ2 rotamer optimization, stereospecific atomic hydrogen placement from quantum calculations, explicit waters, solvent ions or thermal dynamics. The three χ1 geometries are separate tests only.

## Identical fixed 12-chain benchmark

Four previous held-out structures (`1BTA`, `1PGA`, `2PTL`, `2TRX`) plus eight predetermined *E. coli* entries from the **same v02 `read_truth()` function**. Total native nearest-backbone-acceptor contacts = **719**, defined by the prior 3.5 Å N–O cutoff, |i−j| > 2, and no backbone NH donor at proline. This is a geometric proxy, not a hydrogen-bond energy ground truth.

| Forward model | Exact matches / 719 | Emitted contacts | Precision | Recall | F1 | Mean Cα RMSD (Å) | Revisions |
|---|---:|---:|---:|---:|---:|---:|---:|
| `alpha` | 322/719 | 1157 | 0.2783 | 0.4478 | 0.3433 | 41.70 | 0 |
| `roll4` | 325/719 | 1157 | 0.2809 | 0.4520 | 0.3465 | 41.43 | 11 |
| `roll8` | 319/719 | 1157 | 0.2757 | 0.4437 | 0.3401 | 41.52 | 31 |
| `roll8_no_hbond` | 236/719 | 1043 | 0.2263 | 0.3282 | 0.2679 | 39.66 | 452 |
| `roll8_no_steric` | 319/719 | 1157 | 0.2757 | 0.4437 | 0.3401 | 41.52 | 31 |
| `roll8_no_solvent` | 321/719 | 1157 | 0.2774 | 0.4465 | 0.3422 | 41.70 | 12 |
| `roll8_shuffle` | 303/719 | 1161 | 0.2610 | 0.4214 | 0.3223 | 41.48 | 25 |
| `roll8_post` | 307/719 | 1157 | 0.2653 | 0.4270 | 0.3273 | 41.58 | 90 |

**Specific tests and failures:**

- Window 4 improves the all-α contact count by just **3/719** (325 vs 322). Only two of twelve chains improve (1B93 +2 and 1CMB +1); the rest are unchanged. It is not evidence of native-fold selection.
- Window 8 worsens it by **3/719** (319 vs 322). In one comparison, 1AG9 and 1BL0 each lose one, 1CMB loses one, the others tie.
- Removing hydrogen-bond attraction causes **236/719**, i.e. far fewer correct contacts than the full 8-window model, but doesn't validate the attraction model against experiment.
- Removing sterics gives the same **319/719** as window 8. This ablation has no identifiable contact-level effect in the restricted sampled path — **failure to demonstrate meaningful discrimination by steric energy in this protocol**.
- Removing solvent gives **321/719**, almost the baseline. Our implicit solvent is not a credible substitute for explicit hydration/ionic strength.
- Shuffling the amino acid order gives **303/719**, lower than 319/719. The small sequence-specific benefit depends on this weak baseline and does not show that the model recovers long-range folding.
- One full-chain relaxation pass after window-8 produces **307/719**, losing twelve matches while improving its own toy energy. This is a decisive negative control on the objective.
- Absolute mean aligned Cα RMSD remains ~40 Å for these ~50–175-residue chains: poor global structural reconstruction even where the contact count looks respectable.

## Provenance and reproducibility

The runtime's full sequence was split into two **foreground** batches (first seven chains, then resume remaining five) to avoid the execution environment's command timeout. `NEXUS_V03_LIMIT=7` limits the first stage; `NEXUS_V03_RESUME=1` reads its atomic per-chain checkpoint and computes missing chains. No data or parameters changed between batches. The merged JSON contains 96 individual records and the readable log contains every chain and ablation. The one-cell notebook embeds the same complete Python source and the saved output of this **staged standalone** execution; it has **not** been independently rerun by a second Jupyter kernel. On a local environment, leave both flags unset to run all 12 without resumption. For numerical-library stability, set `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and `MKL_NUM_THREADS=1` before starting Python/Jupyter.

The code includes the baseline v02 geometry/readback routines and a *new* v03 kernel. This makes v03 source longer but executable from one cell using only NumPy and the source ZIP. The checkpoint is an execution convenience, not a training set.

## Ledger

**STANDS** — Rigid rotations preserve covalent geometry; interaction energy is invariant under global rigid-body transforms; its differential gives zero net force/torque under such transforms. These are exact mechanical constraints or properties of the chosen mathematical potential.

**RUNS** — Explicit approximate NH/CO orientations; qualitative short-range and angle tests; virtual L-Cβ and three χ1 alternatives (geometry only); toy implicit hydration competition; finite-difference torsional torque; rolling 4/8 windows; one later-revision-pass; 12-chain exact-contact, RMSD and CPU controls; matched 719 reference addresses and 96 experiment records.

**DEAD END** — This uncalibrated v03 objective as a valid sequence-to-native-fold selector. A +3/719 improvement at window 4 is too small and inconsistent; the window 8 and post-chain run degrade exact matching. Even the fixed-alpha baseline is structurally inaccurate (mean RMSD ~41.7 Å).

**OPEN** — Detailed conformational free-energy landscape and solvation chemical potential; rotamer/side-chain and backbone coupled relaxation; specific water and ionic effects; correct dynamics and detailed balance; nonlocal REACH/partner assignment; a sequence-derived forward fold; native ring operators as *causal* physics rather than address encodings.

## Upstream provider isolated

This run establishes that **a geometrically correct torque calculation is not equivalent to knowing the physically valid free energy that generates it**. The next provider is the energy/solvation *state* on which the torque depends: complete competing partners, alternative side-chain rotamers, solvent and thermal sampling. A scalar minimized in a small rolling window can reinforce the all-α starting basin without exploring the nonlocal beta-sheet basins, regardless of whether its directional HB term passes a small synthetic unit test.

## Prompt for the next round

> Continue NEXUS from v03. The explicit NH···O=C torque kernel passes synthetic invariance, force/torque-sum, chirality, rotamer-geometry and hydration-competition sanity checks. But the 12-chain contact benchmark still recovers only 325/719 (window 4), 319/719 (window 8) versus 322/719 for fixed α. No-HB drops to 236/719; no steric is unchanged; post-chain relaxation drops to 307/719. Mean Cα RMSD remains about 40 Å. **Do not tune a heuristic energy on these held-out structures or call a verified torque model a validated force field.** Go one provider upstream: build a small physically grounded *free-energy comparison* for an explicitly hydrated, side-chain rotamer-coupled peptide with known bonded terms, electrostatics, excluded volume and explicit testable hydration competition. Derive gradient and rate/detailed-balance tests, first on small molecules and independent references. Then test whether multiple conformational starting states and stochastic reversible dynamics, rather than all-α initialization, escape the prior basin. Keep the 12-chain holdout only as a final external test and report every control. Deliver one complete runnable single-cell notebook, full execution trace, STANDS/RUNS/OPEN/DEAD END audit, and the next exact prompt.
