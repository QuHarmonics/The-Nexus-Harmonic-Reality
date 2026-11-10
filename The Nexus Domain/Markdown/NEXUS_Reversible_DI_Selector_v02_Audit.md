# NEXUS — Reversible DI Selector v02: upstream execution audit

**Date:** 2026-10-29 / 2026-10-30 execution session  
**Input:** Original `NEXUS_Fold_Compiler_Notebook (2).zip`; SHA256 prefix `8a8f6eef4de7ab09`.  
**Status conventions:** STANDS / RUNS / OPEN / DEAD END; no CONFIRMED.  
**Files:** `NEXUS_Reversible_DI_Selector_v02.py`, `NEXUS_Reversible_DI_Selector_v02_Single_Cell.ipynb`, `NEXUS_Reversible_DI_Selector_v02_results.txt`.

## Question and contract

The earlier one-pass sequence-only forward selector produced 11 geometric nearest-backbone N–O addresses and matched **0/719** native addresses across the fixed set of 12 chains; a fixed-alpha generator matched **322/719**. The earlier selector could not revisit torsions after a delayed contact became possible. Can reversible geometry improve native-address recovery **without importing target coordinates, torsions, contact maps, or secondary-structure annotations into the emitter**?

The test is independent of read-back identities from the native rings, which are address/decompilation operations, not physical energy functions. The latest NEXUS audit's held-vs-running complementarity is respected; no new held/run input bit is invented.

## Implementation

A chain is initialized with fixed **ideal peptide bond lengths, bond angles, trans omega**, and all-alpha torsions. This deliberately strong baseline is entirely sequence-independent in its starting conformation. At each appending step the active prefix (only atoms at or before the current residue) is scored. A short reversible backward sweep attempts ±30-degree changes around earlier phi/psi bonds. The entire downstream rigid subtree is rotated, maintaining ideal covalent geometry. **Future atom coordinates are cached for computational convenience but never enter the prefix score or selection decision before emission.** No native structure is accessed by the selector; reference coordinates are used only for the final metrics.

Torsion acceptance is a strict decrease in a **chosen, uncalibrated proxy objective**: coarse C-alpha and virtual-C-beta repulsion; soft Gaussian N–O separation; an approximate orientation factor using a virtual donor direction and carbonyl orientation; pairwise virtual-sidechain packing; and a weak alpha torsion prior. The coefficients are chosen before inspecting the v02 benchmark scores: `ca_clash=3.0, cb_clash=1.0, hb=2.8, hp=0.32, backbone_local=0.07`. They do **not** represent a validated molecular-mechanics potential, solvent free energy, or real peptide conformational kinetics.

Primary controls (all 12 chains): zero-width fixed-alpha, reversible 4-residue window, reversible 8-residue window; no-H-bond, no-H-bond-directionality, no-steric eight-residue ablations; shuffled amino-acid order; post-chain backward sweep. The same four held-out PDBs and eight predetermined *E. coli* chains are scored, with no parameter fitting to any of them.

### Pooled native-address results

The reported native target is the same retrospective 3.5 Å nearest-backbone acceptor criterion as v01 (proline excluded as N–H donor, sequence separation > 2). This is not a chemical hydrogen-bond energy criterion. F1 pools exact `(donor_index,acceptor_index)` matches; comparing only a count of contacts would be misleading.

| Executor / control | Native | Emitted | Exact matches | Recall | Pooled F1 | Mean CA RMSD (Å) | Accepted revisions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Frozen fixed alpha | 719 | 1,157 | **322** | **0.4478** | **0.3433** | 41.70 | 0 |
| Reversible window 4 | 719 | 1,131 | 238 | 0.3310 | 0.2573 | 37.74 | 1,755 |
| Reversible window 8 | 719 | 1,133 | 237 | 0.3296 | 0.2559 | 37.56 | 1,851 |
| Window 8, omit HB proximity | 719 | 934 | 214 | 0.2976 | 0.2589 | 20.13 | 1,639 |
| Window 8, omit HB directional factor | 719 | 1,135 | 263 | 0.3658 | 0.2837 | 34.84 | 1,858 |
| Window 8, omit steric repulsion | 719 | 1,158 | 133 | 0.1850 | 0.1417 | 21.77 | 2,528 |
| Window 8, shuffle amino acids | 719 | 1,117 | 250 | 0.3477 | 0.2723 | 40.47 | 1,616 |
| Window 8 plus one full-chain sweep | 719 | 1,139 | 240 | 0.3338 | 0.2583 | 37.43 | 1,970 |

Note: the shuffled control changes the sequence driving geometry, then compares contacts by **original residue index** to the target; proline donor masking remains based on the original target sequence in the evaluation. Interpret it as a position-indexed sequence perturbation, not an actual homologous sequence.

The earlier v01 greedy selector matched **0/719** and was computationally distinct from the fixed-alpha seed. It is not equivalent to a v02 zero-width run: the latter is specifically the same fixed-alpha starting conformation used by every reversible version.

### Execution and geometry checks

- Ideal N–CA, CA–C and C–N bond lengths, peptide omega ≈ 180 degrees, and consistency between stored and geometrically measured phi/psi hold to the asserted numeric tolerances (bond deviation < 1e-8 Å; omega and torsion error < 1e-7 degrees). These are properties of exact rigid rotations, not an empirical native geometry reconstruction.
- The rolling window 8 accepted **1,851** earlier-torsion changes over **37,505** candidate rotations across 12 proteins. Reversible execution is real within this algorithm.
- Adding one final full-chain sweep lowers the **model's own objective** on chains where changes are accepted. Yet only **240/719** native contacts match after that sweep, versus **237/719** before it. Lowering the toy energy is not correlated reliably with recovering native contact addresses.
- Average CA RMSD can improve while exact contact recovery worsens. Both are reported: an aligned global position metric is not interchangeable with a closure-address metric.
- The no-direction and shuffled controls perform **better** than the eight-residue full model. This actively falsifies any claim that the current approximate directional term or current amino-acid-specific packing representation captures the needed predictive constraint.
- In chain `1CMB`, fixed alpha matches 33; reversible window 8 matches 12; removal of the approximate directional term restores 33. This does not mean physical hydrogen bonds lack directionality; it means this term is a poor model of it.
- All numbers are from one completed Python execution of the standalone script; the one-cell notebook contains identical code and saved stdout from that script, **not a second independent notebook execution**. Wall time ~350 seconds on the available CPU. NumPy required; no external network used.

## Most important upstream dependency

**The reversible update mechanism is no longer the blocker. The selector's physical criterion is.** The program changes a backbone torsion when an approximate score decreases; a protein changes conformation through a many-body energy landscape, solvent-mediated interactions, steric and electronic structure, competing side-chain rotamers, temperature and kinetic accessibility. The present score uses none of these comprehensively. A mathematically correct rigid rotation can be physically incorrectly selected.

An appropriate next-level relationship is

\[
\tau_i = -\frac{\partial F(\boldsymbol\theta,\mathrm{environment})}{\partial \theta_i},
\qquad
\mathrm{rate\ of\ change}\ \theta_i\ \mathrm{depends\ on}\ \tau_i,\ \mathrm{friction,\ and\ thermal\ fluctuations}.
\]

Here \(F\) must be an independently specified free-energy model; it cannot be supplied by the finished native fold. In particular, the native ring's identity of a “held” versus “running” address does not supply a torque or transition probability. The next productive test must implement and validate an interaction model **before** attempting native fold recovery, with explicit tests of two-body angular hydrogen-bond geometry, steric exclusions, rotamer alternatives, and small known interactions. No unjustified native-fold conclusions from this v02 run.

## Ledger

- **STANDS:** Rigid rotation of downstream atoms around a backbone torsion preserves ideal covalent geometry; NeRF placement follows from specified internal geometry; native ring pairing identities are independent of energy selection.
- **RUNS:** A sequence-only current-prefix reversible executor; 4/8-residue windows and post-chain full sweep; fixed-alpha, interaction ablations, and position-indexed shuffle control; same 12 chain-held-out structures; exact-address metrics and C-alpha RMSD.
- **DEAD END:** This v02 score as a forward native fold/closure selector. Window-8 recovery is 237/719 versus 322/719 for frozen alpha, and sequence shuffle outperforms the full score (250/719). No validated link from local node ends to these revision decisions.
- **OPEN:** Physical interaction free energy, solvent and full sidechain representation, kinetic accessibility/thermal rates, nonlocal REACH, correct per-residue torsion-selection law, forward protein node emission from sequence, and structural memory across environmental transitions.

## Next prompt

> Continue NEXUS one DI provider upstream from the v02 reversible torsion reader. A sequence-only rolling-window executor accepted 1,851 backward revisions but recovered only 237/719 exact native N–O closure addresses at window 8, worse than frozen fixed-alpha 322/719. Omitting its approximate hydrogen-bond directional term improved recovery to 263/719, and a shuffled sequence reached 250/719. The problem is the criterion authorizing changes, not the ability to change them. Build and test an **independently justified local torque/energy kernel**, starting with explicit N–H donor and C=O acceptor geometry, excluded-volume and real side-chain placement, then solvent competition. First validate angular preferences, two-body contact geometry, torque signs, and invariances on small synthetic cases without any native protein coordinates. Then integrate only tested terms into the reversible executor, retain a no-target-data leakage boundary, and rerun the fixed 12-chain benchmark with frozen-alpha, shuffled, no-H-bond and no-steric controls. Include window 0/4/8, an optional post-chain pass, per-chain and pooled exact-address recovery, RMSD, and all failures; do not tune on held-out folds. Keep STANDS/RUNS/OPEN/DEAD END honest. Produce a complete single-cell Jupyter notebook, execution log, audit, and next exact prompt.
