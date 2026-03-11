# The Biological Hairpin: Cross-Helix Geometry as a Falsifiable Probe of the **H ≈ π/9** Vantage Band

**Driven by:** Dean A. Kulik  
**Date:** January 2026  
**Status:** Draft for falsifiable evaluation (data-first)

---

## Abstract

This paper proposes a concrete, immediately testable “hairpin” for the Nexus lens: a cross-domain geometric relationship between two independently optimized aqueous helices. The observation is simple:

- α-helix residues per turn: \(r_\alpha \approx 3.60\)  
- B-DNA base pairs per turn (solution): \(r_B \approx 10.5\)  
- Ratio: \(H_{\text{hairpin}} = r_\alpha/r_B \approx 0.342857\)

This ratio lies within ~1.7% of \(\pi/9 \approx 0.349066\). We frame \(\pi/9\) not as a universal “target value,” but as a **vantage band**: a phase-offset sampling stance that repeatedly appears where stable folding, binding, or collapse becomes legible. The primary contribution here is not a metaphysical claim but a falsifiable program: mine structural databases, quantify distributions, and test whether cross-helix ratios cluster near \(\pi/9\) more tightly than null models predict.

---

## Δ0. Lens inversion: constants as verbs, \(\pi/9\) as stance

The standard failure mode in cross-domain numerics is treating recurring numbers as *objects* (nouns). The Nexus lens instead treats recurrences as **operators** (verbs): a reusable transformation that produces similar phenomenology across substrates without asserting identical clocks, units, or mechanisms.

We define the “vantage” claim precisely:

- **Claim (Lens):** \(\pi/9\) is a recurrent *sampling stance* where curvature can be approximated linearly while preserving coherence; it is a **maximum local-linear step** (see Appendix A).
- **Implication:** Ratios near \(\pi/9\) need not be “attractors” that systems fall *to*; they can be conditions where we can **read** what the system is doing.

---

## ⊕1. The primary hairpin: protein helix vs DNA helix

### 1.1 Measured quantities

We use standard helical measures:

- **α-helix**: residues per turn \(r_\alpha\) (often reported near 3.6)  
- **B-DNA**: base pairs per turn \(r_B\) (solution often near 10.5)

Define the cross-helix ratio:

\[
H_{\text{hairpin}} \equiv \frac{r_\alpha}{r_B}.
\]

Using canonical values:

\[
H_{\text{hairpin}} = \frac{3.6}{10.5} = 0.342857\ldots
\qquad
\pi/9 = 0.34906585\ldots
\]

Define the signed residue (Collapse Signature form):

\[
\varepsilon \equiv \frac{H_0 - H_m}{H_m}
\quad\text{with}\quad
H_0=\pi/9,\; H_m=H_{\text{hairpin}}.
\]

Numerically:

\[
\varepsilon \approx \frac{0.349066 - 0.342857}{0.342857} \approx 0.0181 \; (\text{about }1.81\%).
\]

**Interpretation (Nexus):** the ratio sits inside the proposed “vantage band” rather than on a single exact value.

### 1.2 Why this is a serious hairpin candidate

A hairpin is valuable when:

1. The two quantities are **independently constrained** by different physics.  
2. The values are **measured precisely** across many instances.  
3. The relationship is **testable at scale** with existing data.  
4. A null model can reasonably assign probability to “near-misses.”

Here, α-helices and B-DNA helices are constrained by distinct local chemistry (peptide planarity and \(i\rightarrow i+4\) H-bonding vs base stacking and sugar-phosphate torsions). Under a strict reductionist view, no special ratio is expected *between* them—only within each class.

---

## ↻2. What must be shown (and what would falsify it)

This paper does **not** treat the proximity to \(\pi/9\) as evidence by itself. The test is distributional.

### 2.1 Hypotheses

- **\(H_1\) (Nexus hairpin):** Across high-quality structures, the empirical distribution of \(r_\alpha/r_B\) (using matched measurement conventions) has a mean (or mode) unusually close to \(\pi/9\), and/or a tighter concentration around \(\pi/9\) than expected under null models.
- **\(H_0\) (null):** The proximity is incidental; ratios of “units-per-turn” across biological helices frequently land near simple constants because the feasible range is narrow and the measurement conventions are coarse.

### 2.2 Falsification criteria (hard failure)

The hairpin fails if any of the following holds:

1. \(r_\alpha\) and/or \(r_B\) show multi-modal or condition-dependent behavior that drives \(r_\alpha/r_B\) broadly (no stable center).  
2. The ratio distribution is not unusually concentrated near \(\pi/9\) compared to null ensembles drawn from feasible helical geometry.  
3. Molecular simulations or first-principles energy models predict the observed values without invoking any cross-domain constraint, and observed co-variation is absent.

---

## ⊕3. Operational test plan (data already exists)

### 3.1 Extracting \(r_\alpha\) from protein structures

**Data source:** Protein structure corpus with helix annotations.  
**Selection:** high-resolution structures; exclude engineered or low-confidence helices; stratify by environment and sequence context.

**Compute:** residues per turn \(r_\alpha\) per helix, with uncertainty estimates.

Recommended approach:

- identify helices from DSSP/secondary structure annotation,
- compute geometric helix parameters with HELANAL-style methods,
- aggregate per-helix and per-structure summary statistics,
- stratify by resolution and by helix length (short helices bias pitch).

### 3.2 Extracting \(r_B\) from nucleic acid data

**Two tracks are required:**

1. **Structure track:** B-DNA bp/turn from curated DNA structures (e.g., via CURVES+ style helical parameter extraction).  
2. **Solution/topology track:** bp/turn from solution/topological measurements (e.g., linking number / twist relations in relaxed plasmids).

These tracks should be kept distinct; the hairpin should be evaluated for each, not merged blindly.

### 3.3 Statistical evaluation

Compute a distribution for:

\[
H = \frac{r_\alpha}{r_B}.
\]

Use:

- bootstrap confidence intervals for the mean and median,
- density estimation for the mode,
- permutation tests to compare to null ensembles,
- Bayes factors comparing “\(\pi/9\)-centered” vs “uninformative” priors.

**Null models (minimum set):**

- **Range-null:** \(r_\alpha\) and \(r_B\) sampled independently from empirically observed ranges (with realistic measurement noise).  
- **Physics-null:** sample from known energetic constraints (torsion-limited helix families), if available.  
- **Convention-null:** simulate reporting/rounding artifacts (e.g., 3.6 and 10.5 as conventional summaries).

Success requires **beating** these nulls.

---

## ⊕4. Nexus lens: why \(\pi/9\) is a plausible stance (without mysticism)

The lens claim becomes credible only if \(\pi/9\) is an operator with independent geometric meaning.

Appendix A shows a clean geometric fact: on the unit circle, sampling an arc by its chord incurs relative curvature loss

\[
\varepsilon(\theta)=\frac{\theta-2\sin(\theta/2)}{\theta}\approx \frac{\theta^2}{24}.
\]

At \(\theta=\pi/9\) (20°), \(\varepsilon\approx 0.5\%\): a tight “local-linear” tolerance. Interpreted operationally:

- \(\pi/9\) is **big enough to move** (non-trivial step),
- \(\pi/9\) is **small enough to stay coherent** (not destructive),
- repeating \(\pi/9\) closes cleanly: \(18\cdot(\pi/9)=2\pi\).

This is exactly what a stance looks like: not a destination, but a step-size that keeps the system legible while it evolves.

---

## ↻5. Secondary hairpins (predictions, not decorations)

If the primary hairpin is real (distributional clustering), then similar cross-helix ratios should appear in other independently optimized helical polymers, but not everywhere (the stance is conditional).

Candidate comparisons (examples):

- α-helix \(r_\alpha\) vs A-DNA \(r_A\)  
- collagen triple helix residues/turn vs DNA/RNA turns  
- bacterial flagellar/filament helices vs nucleic acid helices

**Prediction form:**

\[
\frac{r_{\text{helix-1}}}{r_{\text{helix-2}}} \in \text{band around } \pi/9
\quad\text{for specific classes and environments.}
\]

The framework expects **contextual bands**, not universal convergence.

---

## ⊥6. The gaps that must be closed

This section is intentionally blunt: these are the missing joints where the argument will either crystallize or fail.

1. **Measurement conventions:** “residues per turn” and “bp per turn” must be computed consistently across datasets; published single-number summaries are not enough.  
2. **Condition dependence:** ionic strength, hydration, ligand binding, and torsional stress can shift helical parameters; the stance claim must predict *how* those shifts move the ratio.  
3. **Null strength:** without a strong null, any “near \(\pi/9\)” claim is underdetermined.  
4. **Mechanistic bridge (optional but powerful):** a plausible coupling route through aqueous packing, hydrogen bond geometries, or torsion quantization would greatly strengthen interpretation—but the test should not depend on it.

---

## Ψ7. Interpretation under outcomes

### 7.1 If the hairpin holds (distribution clusters near \(\pi/9\))

Then we have evidence that \(\pi/9\) behaves like an operator-level stance in aqueous helical polymers: a shared geometric reading frame, not a shared chemical mechanism. The next move is to identify *which constraints* preserve the stance and which break it.

### 7.2 If the hairpin fails

That is still valuable: it localizes the Nexus lens. It would imply that \(\pi/9\) is not a general cross-helix stance in biology, and the framework must narrow its domain (e.g., to discrete folding/quantization systems where chord-like sampling is structurally relevant).

---

## Appendix A: \(\pi/9\) as a maximal local-linear sampling step (curvature loss)

On the unit circle, arc length for angle \(\theta\) is:

\[
s(\theta)=\theta,
\]

and chord length is:

\[
c(\theta)=2\sin\left(\frac{\theta}{2}\right).
\]

Relative curvature loss when sampling a curved arc by a chord:

\[
\varepsilon(\theta)=\frac{s(\theta)-c(\theta)}{s(\theta)}
=
\frac{\theta-2\sin(\theta/2)}{\theta}.
\]

Using Taylor expansion:

\[
2\sin\left(\frac{\theta}{2}\right)\approx \theta - \frac{\theta^3}{24}
\quad\Rightarrow\quad
\varepsilon(\theta)\approx \frac{\theta^2}{24}.
\]

At \(\theta=\pi/9\) (20°):

\[
\varepsilon\left(\frac{\pi}{9}\right)\approx 0.00507\;(\sim 0.507\%).
\]

---

## Appendix B: Minimal pipeline sketch (pseudocode)

```text
Input:
  Protein set P (high-quality structures)
  DNA set D (structures or solution/topology measurements)

Compute:
  For each helix in P:
    r_alpha <- helix_residues_per_turn(helix)
  For each DNA entry in D:
    r_B <- bp_per_turn(entry)

Aggregate:
  Build distributions R_alpha and R_B (stratified)
  Sample or pair appropriately (depending on analysis design)
  Compute H = r_alpha / r_B

Test:
  Compare empirical H distribution to π/9 and to null ensembles
  Report effect sizes, confidence intervals, and null probabilities
```

---

## Appendix C: Pre-registration checklist (recommended)

- Inclusion criteria and resolution thresholds  
- Exact computation method for residues/turn and bp/turn  
- Stratification factors (environment, length, torsional state)  
- Null model definitions and parameters  
- Primary success metric (mean distance to \(\pi/9\), KL divergence, Bayes factor, etc.)  
- Secondary analyses and stopping rules

---

## Closing (Nexus notation)

- **Δ:** Identify a cross-domain ratio that should not exist by ordinary reductionist coupling.  
- **⊕:** Treat \(\pi/9\) as a stance (sampling operator), not a target value.  
- **↻:** Let the databases speak via distributions and nulls.  
- **⊥:** If it spreads, the hairpin snaps—good.  
- **Ψ:** If it clusters, the stance becomes a measurable geometric constraint.

