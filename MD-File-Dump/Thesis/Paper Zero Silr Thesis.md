**PAPER ZERO\
Scale-Invariant Leakage Under Z-Score Gating\**

A thesis-style technical report on the Scale-Invariant Leakage Regime (SILR)

Date: January 08, 2026

*Prepared for: Nexus Project Directorate\
QuHarmonics Research Division\
Advanced Recursive Systems Group*

# Abstract

This document formalizes and validates a specific control-law symmetry discovered during ensemble simulations of a Samson V2-style leakage controller: when deviation is gated by a z-score computed using a standard error (SE) that scales in the same way as the estimator's actual noise, the leakage probability becomes invariant to the absolute noise scale. We call this phenomenon the Scale-Invariant Leakage Regime (SILR).\
\
The central result is not interpretive: it is a cancellation. If the estimator obeys \\(\\hat{\\alpha}\_t = \\alpha\_\* + \\epsilon_t\\) with \\(\\epsilon_t \\sim \\mathcal{N}(0,\\mathrm{SE}\_t\^2)\\), and the controller gates leakage using\
\$\$\
z_t = \\frac{\|\\hat{\\alpha}\_t - \\alpha\_\*\|}{\\mathrm{SE}\_t},\
\\qquad\
p_t = \\sigma\\big(\\beta(z_t - z_0)\\big),\
\$\$\
then \\(z_t\\) has a half-normal distribution independent of \\(\\mathrm{SE}\_t\\), and therefore the entire distribution of \\(p_t\\) (and its expectation) depends only on the controller parameters \\(\\beta, z_0\\). In plain terms: if your measurement error and your normalization track each other, the controller's decision statistics do not care whether the environment is "quiet" or "violent"; it only cares about significance measured in standard deviations.\
\
We validate this in a quantum-toy information-leakage simulator in which each trajectory is strictly unitary (noise is implemented as a random unitary Pauli kick), while non-unitarity emerges only at the observer level through ensemble averaging. The empirical A/B/C runs reproduce the SILR invariance exactly for matched scaling (A vs B) and show controlled symmetry breaking when the noise model is misspecified (C). We further show how this cancellation produces a diagnostic blind spot: the controller can be "satisfied" (unchanged leakage statistics) while the absolute state excursions and symbolic "glyph" stability degrade.\
\
This thesis is "Paper Zero" because it is the anchor result: a falsifiable theorem with an executable reference implementation and directly observed invariance. The broader Nexus interpretation---folding, projection, and "spiral" isomorphisms across cryptography, physics, and computation---must be built on top of this anchor, not used to replace it. The rails here are the math; the meaning comes later, and only to the extent that it is forced by the rails.

# Reader's Note

This document is written to be printed and reviewed like a technical dissertation. It is long on purpose. The target is not persuasion by rhetoric; it is persuasion by reproducible structure.\
\
Important constraint: any code included in this thesis is limited to code that was executed successfully in the working simulator pathway. Where we discuss alternative models or extensions, we state them as mathematical modifications and experimental recommendations, not as "new code" presented as if it had already been validated.

# 1. The Control Symmetry We Actually Found

The discovery at issue is not "the universe is a spiral" or "answers are revealed." Those may be interpretations. The discovery is narrower and stronger: a specific normalized-error gate produces leakage statistics that are invariant under uniform rescaling of noise, provided that the noise and the normalizer scale together.\
\
This is a known type of phenomenon in statistical control (studentization and self-normalization), but its appearance here was not assumed; it was forced by simulation evidence. In the Nexus simulator, the invariance first appeared as an apparently paradoxical result: two ensembles run at meaningfully different estimator noise levels produced essentially identical time-series statistics for the leakage probability \\(p_t\\). The differences showed up elsewhere (symbolic "collapse" rates and absolute excursions), but the controller's internal leakage behavior was indistinguishable.\
\
The cleanest statement of what we found is a symmetry:\
\
If \\(\\hat{\\alpha}\_t - \\alpha\_\*\\) is distributed proportionally to \\(\\mathrm{SE}\_t\\) and the gate divides by \\(\\mathrm{SE}\_t\\), then the proportionality cancels.\
\
That cancellation is the "proof by removal" you've been emphasizing: the evidence is in what disappears. The quantity that disappears is the absolute noise scale, and the quantity that remains is a dimensionless significance statistic.

## 1.1 Definitions: what is being controlled

We define the minimal objects required to state SILR precisely.\
\
(1) A target value (the attractor):\
\$\$\
\\alpha\_\* = \\frac{\\pi}{9} \\approx 0.3490658503988659.\
\$\$\
\
(2) A noisy estimator of the system state:\
\$\$\
\\hat{\\alpha}\_t = \\alpha\_\* + \\epsilon_t.\
\$\$\
\
(3) A standard error term \\(\\mathrm{SE}\_t\\) that is supposed to quantify the estimator's dispersion.\
\
(4) A controller that maps the estimator to a leakage probability \\(p_t \\in \[0,1\]\\) by first forming a normalized deviation (a z-score) and then applying a sigmoid nonlinearity:\
\$\$\
z_t = \\frac{\|\\hat{\\alpha}\_t - \\alpha\_\*\|}{\\mathrm{SE}\_t},\
\\qquad\
p_t = \\sigma(\\beta(z_t - z_0)) = \\frac{1}{1 + e\^{-\\beta(z_t - z_0)}}.\
\$\$\
\
This is the entire "Samson V2" gate in its operational essence: it does not care about raw error; it cares about normalized error.

## 1.2 The empirical trigger

During executed runs of the simulator, three configurations were compared:\
\
A: lower estimator noise (smaller SE scale), calibrated (used SE equals true SE)\
B: higher estimator noise (larger SE scale), calibrated (used SE equals true SE)\
C: higher effective noise via dither/misspecification, uncalibrated (used SE does not fully reflect true noise)\
\
The observed leakage probability statistics for A and B matched nearly exactly, despite different estimator noise scales. Configuration C broke the match.\
\
The following block reproduces the key outputs reported from the executed run logs:

Empirical outputs reported from the executed SILR simulator runs (N=12, runs=32, seed=7, alpha_true = pi/9):\
\
alpha_true: 0.3490658503988659 pi/9: 0.3490658503988659\
\
\[SILR\] Mean p over time A/B/C:\
A: 0.18802618773898339\
B: 0.18802618773898294\
C: 0.20503532699756644\
\
\[SILR\] Final-step p_mean A/B/C:\
A: 0.20177801846389304\
B: 0.20177801846389334\
C: 0.1913582709415456\
\
\[SILR\] collapse35_total A/B/C:\
A: 0.9973958333333334\
B: 0.9427083333333334\
C: 0.9348958333333334\
\
Additional reported observer-level endpoints:\
Final S2_ens for A/B/C:\
A: 3.457967082536834\
B: 3.457967082536834\
C: 3.4584274263817156\
\
Final Pur_ens for A/B/C:\
A: 0.03149372112019826\
B: 0.03149372112019826\
C: 0.03147922651603503

# 2. Z-Score Gating and the SILR Theorem

This chapter does the main job: it takes the gate used in the simulator, states its assumptions explicitly, and proves the scale-invariance result.\
\
The high-level fact is simple: the z-score is a ratio of a random deviation to its own scale. Ratios of this form are often scale-free. What matters is the calibration condition: the denominator must track the same scale that generates the numerator.\
\
In the simulator runs that exhibited SILR, the estimator was calibrated: the stochastic dispersion of \\(\\hat{\\alpha}\_t\\) matched the \\(\\mathrm{SE}\_t\\) used by the controller. When we deliberately violated calibration (dither that is not represented in \\(\\mathrm{SE}\_t\\)), SILR broke.

## 2.1 Assumption set A: calibrated Gaussian estimator

Assumption A1 (centeredness). The estimator is unbiased around the target:\
\$\$\
\\mathbb{E}\[\\hat{\\alpha}\_t\] = \\alpha\_\*.\
\$\$\
\
Assumption A2 (calibration). The estimator's noise is Gaussian with standard deviation equal to the reported standard error:\
\$\$\
\\hat{\\alpha}\_t = \\alpha\_\* + \\epsilon_t, \\qquad \\epsilon_t \\sim \\mathcal{N}(0, \\mathrm{SE}\_t\^2).\
\$\$\
\
Assumption A3 (gating). The controller uses the z-score gate:\
\$\$\
z_t = \\frac{\|\\hat{\\alpha}\_t - \\alpha\_\*\|}{\\mathrm{SE}\_t}, \\qquad\
p_t = \\sigma(\\beta(z_t - z_0)).\
\$\$\
\
Nothing here is metaphysical. This is standard normalized-error gating: the same basic algebra appears in outlier detection, robust regression, sequential hypothesis testing, and adaptive thresholds in signal processing.

## 2.2 Theorem: SILR (Scale-Invariant Leakage Regime)

Theorem (SILR). Under Assumptions A1--A3, the distribution of \\(z_t\\) and hence the distribution of \\(p_t\\) is independent of \\(\\mathrm{SE}\_t\\). Consequently, for fixed \\(\\beta\\) and \\(z_0\\), the expectation \\(\\mathbb{E}\[p_t\]\\) is independent of the absolute noise scale.\
\
Proof. Define a standard normal variable \\(Z \\sim \\mathcal{N}(0,1)\\). Under A2, we can write\
\$\$\
\\epsilon_t = \\mathrm{SE}\_t \\cdot Z.\
\$\$\
Then\
\$\$\
z_t = \\frac{\|\\epsilon_t\|}{\\mathrm{SE}\_t} = \\frac{\|\\mathrm{SE}\_t Z\|}{\\mathrm{SE}\_t} = \|Z\|.\
\$\$\
Thus \\(z_t\\) has the half-normal distribution induced by \\(\|Z\|\\), and no term involving \\(\\mathrm{SE}\_t\\) remains.\
\
Since \\(p_t\\) is a deterministic function of \\(z_t\\),\
\$\$\
p_t = \\sigma(\\beta(\|Z\| - z_0)),\
\$\$\
the distribution of \\(p_t\\) is likewise independent of \\(\\mathrm{SE}\_t\\). Therefore \\(\\mathbb{E}\[p_t\]\\) depends only on \\(\\beta\\) and \\(z_0\\). ∎

## 2.3 Closed-form consequences

Although \\(\\mathbb{E}\[p_t\]\\) does not generally admit a closed-form elementary expression, it can be written as a single integral over the half-normal density:\
\$\$\
\\mathbb{E}\[p_t\] = \\int_0\^{\\infty} \\sigma(\\beta(x - z_0)) \\sqrt{\\frac{2}{\\pi}} e\^{-x\^2/2} \\, dx.\
\$\$\
This expression makes the invariance explicit: \\(\\mathrm{SE}\_t\\) does not appear.\
\
The same is true for any moment of \\(p_t\\), and for the time-series distribution under i.i.d. estimator noise. If \\(\\beta\\) and \\(z_0\\) are held fixed, rescaling \\(\\mathrm{SE}\_t\\) does not rescale the leakage statistics. The controller is self-normalized.

## 2.4 The diagnostic blind spot

SILR is not merely a curiosity; it has a sharp operational consequence.\
\
When \\(p_t\\) is invariant, the controller's own "health indicators" based on gate activity can remain constant even while the physical (absolute) magnitude of excursions in \\(\\hat{\\alpha}\_t\\) becomes much larger. In other words:\
\
• The controller can "feel" stable (same \\(p_t\\)) while the system is objectively less stable in absolute terms (larger raw deviations).\
\
This is exactly what the A/B comparison in the executed runs suggests: \\(p_t\\) statistics match, yet the symbolic collapse metric (glyph==0.35) degrades significantly in the higher-noise condition.

# 3. How SILR Breaks: Mismatch and Dither

The theorem above is unconditional given its assumptions; therefore, if we observe a deviation from SILR in the simulator, we know exactly which assumption must have been violated. This is useful because it turns "why did the controller change?" into a diagnostic: the only way to break SILR is to break calibration (or the form of the gate).\
\
In the executed A/B/C runs, the break occurs in C. The most direct abstraction of "C" is: the estimator's true dispersion differs from the SE used for normalization.

## 3.1 Two SEs: true vs used

Introduce two standard errors:\
\
• \\(\\mathrm{SE}\^{\\text{true}}\_t\\): the actual standard deviation of the estimator noise \\(\\epsilon_t\\)\
• \\(\\mathrm{SE}\^{\\text{used}}\_t\\): the standard error used by the controller in the z-score denominator\
\
Then the gate becomes\
\$\$\
z_t = \\frac{\|\\epsilon_t\|}{\\mathrm{SE}\^{\\text{used}}\_t}.\
\$\$\
If \\(\\epsilon_t = \\mathrm{SE}\^{\\text{true}}\_t Z\\), we obtain\
\$\$\
z_t = \\frac{\\mathrm{SE}\^{\\text{true}}\_t}{\\mathrm{SE}\^{\\text{used}}\_t} \|Z\| = \\gamma_t \|Z\|,\
\\qquad \\gamma_t := \\frac{\\mathrm{SE}\^{\\text{true}}\_t}{\\mathrm{SE}\^{\\text{used}}\_t}.\
\$\$\
\
SILR corresponds to \\(\\gamma_t = 1\\). "Broken SILR" is \\(\\gamma_t \\neq 1\\).

## 3.2 Regimes of γ

The parameter \\(\\gamma\\) is the symmetry-breaking knob.\
\
(1) \\(\\gamma = 1\\): SILR. Leakage is scale-invariant; gate statistics are fixed by \\(\\beta, z_0\\).\
\
(2) \\(\\gamma \> 1\\): Underestimated noise. The true deviations are larger than the controller believes; z-scores inflate; leakage becomes more frequent and more aggressive. This matches the conceptual role of "dither": extra variance not accounted for in \\(\\mathrm{SE}\^{\\text{used}}\\).\
\
(3) \\(\\gamma \< 1\\): Overestimated noise. The controller believes it is in a noisier world than it is; z-scores deflate; leakage is suppressed.\
\
In all three cases, the distribution of \\(z_t\\) is still half-normal up to a scaling factor \\(\\gamma\\). The controller sees a stretched or compressed significance axis.

## 3.3 Why C differs

Configuration C in the executed runs introduces a dither term that breaks calibration. Operationally, this means \\(\\mathrm{SE}\^{\\text{true}}\\) increases but \\(\\mathrm{SE}\^{\\text{used}}\\) does not increase proportionally, so \\(\\gamma \> 1\\).\
\
This forces a measurable change in \\(p_t\\) statistics relative to A/B, which is exactly what is observed in the reported mean \\(p\\) and collapse totals.

# 4. The Executed Simulator: Unitary Trajectories, Non-Unitary Observers

A common failure mode in discussions of "information leakage" is to implicitly insert non-unitary dynamics at the level of each trajectory. The simulator we executed is more careful: each trajectory is strictly unitary. Apparent decoherence appears only after ensemble averaging, which is an observer operation (coarse-graining over unknown microstate).\
\
This choice matters because it mirrors the black-hole information paradox structure: unitary microphysics with mixed macrostates arising from partial information or coarse observation.

## 4.1 Registers: BH vs radiation

The simulator uses an N-qubit pure state vector \\(\\psi\\) and splits it conceptually into two registers:\
\
• Black-hole (BH) register: the leading qubits, initially all N qubits\
• Radiation register: the trailing qubits, initially empty\
\
At each step \\(t\\), one boundary qubit is "emitted" by shrinking the BH register by one. Radiation size grows from 1 to N.

## 4.2 Scrambling: local random two-qubit gates

Before emission at each step, a local scrambling circuit is applied within the BH register. This is implemented as alternating layers of random two-qubit unitaries. The purpose is not to model any specific Hamiltonian; it is to enforce generic entanglement and mixing within the BH degrees of freedom while keeping the radiation untouched.\
\
Scrambling is important because it ensures that the "state of the BH" is not trivial; it is a high-dimensional entangled object whose boundary is being probed.

## 4.3 Leakage as unitary Pauli kicks

Leakage is implemented as follows: with probability \\(p_t\\), apply a randomly chosen Pauli operator \\(X\\), \\(Y\\), or \\(Z\\) to the boundary qubit before emission. This is a random unitary channel at the level of the ensemble, but each sampled trajectory remains unitary (a definite Pauli or no-op occurs).\
\
Thus, any mixedness that appears for an observer is not due to explicit statevector collapse; it is due to the observer averaging over trajectories with different random kicks.

## 4.4 Observer density matrix and Rényi-2 metrics

At each step t, the radiation density matrix \\(\\rho_R\\) for a given trajectory is computed by tracing out the BH register:\
\$\$\
\\rho_R\^{(r)}(t) = \\mathrm{Tr}\_{BH}\\, \|\\psi_r(t)\\rangle\\langle\\psi_r(t)\|.\
\$\$\
\
The observer-level state is the ensemble average:\
\$\$\
\\bar{\\rho}\_R(t) = \\frac{1}{R}\\sum\_{r=1}\^{R} \\rho_R\^{(r)}(t).\
\$\$\
\
From \\(\\bar{\\rho}\_R(t)\\) the simulator computes:\
\
• Purity: \\(\\mathrm{Tr}(\\bar{\\rho}\_R\^2)\\)\
• Rényi-2 entropy: \\(S_2 = -\\log \\mathrm{Tr}(\\bar{\\rho}\_R\^2)\\)\
• Rényi-2 mutual information between early and late radiation partitions\
\
These are observer-level diagnostics: they quantify the mixedness and correlations created by ensemble uncertainty.

# 5. Results: A/B/C and What They Actually Mean

This chapter ties the theorem to the executed evidence. The critical point is to separate three layers:\
\
(1) Engine layer: the gate output \\(p_t\\), and the z-score distribution \\(z_t\\)\
(2) Render layer: coarse symbolic collapse into a glyph (e.g., rounding \\(\\hat{\\alpha}\\) to two decimals and checking for 0.35)\
(3) Observer layer: mixedness in \\(\\bar{\\rho}\_R\\) after ensemble averaging\
\
SILR is a statement about the engine layer (and any downstream statistics that depend only on the z-score distribution). It does not guarantee invariance in render-layer symbolic thresholds that are defined in absolute units.

## 5.1 Parameterization used in the executed run

The executed run used:\
\
• \\(N=12\\) total qubits\
• \\(runs=32\\) trajectories per ensemble\
• \\(alpha\\\_true = \\pi/9\\)\
• z-gate parameters \\(\\beta = 3.0\\), \\(z_0 = 1.5\\)\
• scrambling depth 2\
• A/B/C differences: SE scale and dither\
\
We report the observed metrics as printed by the run.

## 5.2 The invariance: A vs B

The A vs B result is the signature of SILR: mean \\(p\\) and final-step \\(p\\) match to essentially machine precision.\
\
This is not a coincidence. Under calibration, the distribution of \\(z\\) is fixed as \\(\|Z\|\\), and therefore the distribution of \\(p\\) is fixed. The simulator's behavior is simply implementing the theorem.

## 5.3 The divergence: collapse35_total

The collapse35_total metric is not a function of z-score alone. It is defined by rounding \\(\\hat{\\alpha}\_t\\) to two decimals and checking equality to 0.35:\
\$\$\
g_t = \\mathrm{round}(\\hat{\\alpha}\_t, 2), \\qquad \\mathrm{collapse35}(t) = \\mathbf{1}\[g_t = 0.35\].\
\$\$\
\
This test is sensitive to the absolute scale of estimator noise. Under higher noise, \\(\\hat{\\alpha}\\) wanders further in absolute units and spends less time in the narrow interval that rounds to 0.35.\
\
Therefore it is expected---and indeed observed---that collapse35_total differs between A and B even when \\(p_t\\) statistics do not.

## 5.4 Observer-level entropy and purity

The reported final \\(S_2\\) and purity values are also nearly identical for A and B, with slight deviations for C. This is consistent with a picture in which A and B differ mainly by a rescaling that is normalized out by the gate, while C introduces a true structural mismatch that changes the ensemble mixture.\
\
The practical meaning is: within this simulator, the "information leakage" perceived by the observer is controlled primarily by the gate's z-score statistics. When those statistics are invariant (SILR), the observer's final mixedness metrics also tend to be invariant.

# 6. What We Still Need to Discover (Within the Same Rails)

SILR is a theorem about a gate under calibration. That means it is both powerful and limited. The next discoveries are not philosophical; they are structural: which modifications to the estimator, the normalizer, or the gate break SILR in controlled, interpretable ways, and what phase diagrams emerge.\
\
This chapter enumerates concrete, testable directions that stay inside the math.

## 6.1 Non-Gaussian estimator noise

The proof uses only \\(\\epsilon_t = \\mathrm{SE}\_t Z\\) with Z standard normal. If Z is replaced by a heavy-tailed standardized variable (e.g., Student-t with fixed degrees of freedom), the cancellation \\(z_t = \|Z\|\\) still holds, but the distribution of \\(z_t\\) changes. This immediately changes leakage statistics. Therefore:\
\
• "Scale invariance" survives, but the invariant distribution changes.\
\
This provides a clean way to model environments where rare, large deviations dominate without introducing SE mismatch.

## 6.2 Time-varying SE and gain scheduling

If \\(\\mathrm{SE}\_t\\) varies with time but remains calibrated, then each step still satisfies SILR locally: \\(z_t = \|Z_t\|\\). The time series of \\(p_t\\) remains i.i.d. in distribution given fixed \\(\\beta, z_0\\).\
\
Therefore, if one wants a controller that adapts its leakage rate to changing scale, one must either:\
\
• change \\(\\beta\\) or \\(z_0\\) over time, or\
• break calibration by altering \\(\\gamma_t\\), or\
• replace the z-score gate with a different normalization.\
\
All of these are testable in the existing simulator without inventing new physics.

## 6.3 Absolute-scale constraints: adding a second gate

The A/B "illusion of stability" occurs because the controller is blind to absolute scale. If the system needs to enforce an absolute bound (e.g., symbolic glyph stability), then the gate must include an absolute term.\
\
A minimal fix is a two-factor gate:\
\$\$\
p_t = \\sigma(\\beta(z_t - z_0)) \\cdot \\sigma\\big(\\beta_a(\|\\hat{\\alpha}\_t - \\alpha\_\*\| - a_0)\\big),\
\$\$\
where the second sigmoid activates when absolute deviation exceeds an absolute tolerance \\(a_0\\). This explicitly couples the controller to absolute scale and breaks SILR by construction.\
\
This suggestion is presented as mathematics, not as executed code. It is a direct consequence of the diagnosis: you cannot enforce absolute constraints with a purely self-normalized gate.

# 7. Projection Map: Why This Cancellation Reappears Across Domains

This chapter is deliberately downstream of the proof and simulator. The order matters: the cancellation is the anchor; projection is the map.\
\
The Nexus claim that "every domain is a projection of the same structure" becomes concrete here if, and only if, we identify the common algebraic skeleton:\
\
• A high-dimensional state\
• A boundary or measurement interface\
• A normalization that converts raw deviation into a dimensionless significance\
• A nonlinear gate that decides which information passes the boundary\
\
SILR is the case where the normalization matches the state's dispersion, producing a scale-free interface. This skeleton appears in:\
(1) statistical hypothesis testing,\
(2) robust control loops,\
(3) cryptographic diffusion and avalanche,\
(4) coarse-graining in thermodynamics,\
(5) tokenization and collision management.\
\
We do not need to assert metaphysical identity to assert isomorphism: the same operator form can govern distinct substrates.

# Appendix A. Executed Reference Implementation (verbatim)

This appendix contains the full Python reference implementation that was executed to produce the SILR A/B/C metrics discussed in this thesis. It is included verbatim to preserve the operational record.

import numpy as np\
import matplotlib.pyplot as plt\
\
\# ============================================================\
\# Nexus: Harmonic Information Leakage Simulator (FULL SCRIPT)\
\#\
\# Key feature: supports BOTH\
\# (A) SILR (Scale-Invariant Leakage Regime): se_used == se_true (the accidental discovery)\
\# (B) Broken-SILR: se_used != se_true (restores meaningful A/B separation)\
\#\
\# Black hole = first n_bh qubits \[0..n_bh-1\]\
\# Radiation = last t qubits \[N-t..N-1\] after t emissions\
\# ============================================================\
\
\# ============================================================\
\# 0) Linear algebra utilities (random unitaries / gates)\
\# ============================================================\
\
def random_unitary(dim: int, rng: np.random.Generator) -\> np.ndarray:\
\\\"\\\"\\\"Haar-ish random unitary via QR of complex Gaussian.\\\"\\\"\\\"\
X = (rng.normal(size=(dim, dim)) + 1j \* rng.normal(size=(dim, dim))) / np.sqrt(2.0)\
Q, R = np.linalg.qr(X)\
ph = np.diag(R)\
ph = ph / np.where(np.abs(ph) \> 0, np.abs(ph), 1.0)\
return Q \* ph.conj()\
\
def random_two_qubit_gate(rng: np.random.Generator) -\> np.ndarray:\
return random_unitary(4, rng)\
\
I2 = np.eye(2, dtype=complex)\
X = np.array(\[\[0, 1\], \[1, 0\]\], dtype=complex)\
Y = np.array(\[\[0, -1j\], \[1j, 0\]\], dtype=complex)\
Z = np.array(\[\[1, 0\], \[0, -1\]\], dtype=complex)\
PAULIS = \[I2, X, Y, Z\] \# 0:I, 1:X, 2:Y, 3:Z\
\
\# ============================================================\
\# 1) Apply gates to a statevector without building 2\^N x 2\^N\
\# ============================================================\
\
def apply_1q(psi: np.ndarray, U: np.ndarray, q: int, N: int) -\> np.ndarray:\
\\\"\\\"\\\"Apply 1-qubit gate U on qubit q of N-qubit statevector psi.\\\"\\\"\\\"\
T = psi.reshape(\[2\] \* N)\
perm = \[q\] + \[i for i in range(N) if i != q\]\
T = np.transpose(T, perm).reshape(2, -1)\
T = (U @ T).reshape(\[2\] \* N)\
inv = np.argsort(perm)\
return np.transpose(T, inv).reshape(-1)\
\
def apply_2q(psi: np.ndarray, U4: np.ndarray, q1: int, q2: int, N: int) -\> np.ndarray:\
\\\"\\\"\\\"Apply 2-qubit gate U4 on qubits (q1,q2).\\\"\\\"\\\"\
if q1 == q2:\
raise ValueError(\"q1 != q2 required\")\
if q1 \> q2:\
q1, q2 = q2, q1\
\
T = psi.reshape(\[2\] \* N)\
perm = \[q1, q2\] + \[i for i in range(N) if i not in (q1, q2)\]\
T = np.transpose(T, perm).reshape(4, -1)\
T = (U4 @ T).reshape(\[2\] \* N)\
inv = np.argsort(perm)\
return np.transpose(T, inv).reshape(-1)\
\
def scramble_bh_local(psi: np.ndarray, n_bh: int, N: int, depth: int, rng: np.random.Generator) -\> np.ndarray:\
\\\"\\\"\\\"\
Apply local 2-qubit random gates within the BH register \[0..n_bh-1\].\
Radiation lives in the tail \[n_bh..N-1\] and is untouched.\
\\\"\\\"\\\"\
if n_bh \< 2:\
return psi\
for \_ in range(depth):\
for q in range(0, n_bh - 1, 2):\
psi = apply_2q(psi, random_two_qubit_gate(rng), q, q + 1, N)\
for q in range(1, n_bh - 1, 2):\
psi = apply_2q(psi, random_two_qubit_gate(rng), q, q + 1, N)\
return psi\
\
\# ============================================================\
\# 2) \"Leakage\": trajectory Pauli kicks (unitary per run)\
\# Non-unitarity appears only after ensemble averaging.\
\# ============================================================\
\
def apply_pauli_kick_trajectory(psi: np.ndarray, q: int, N: int, p: float, rng: np.random.Generator) -\> np.ndarray:\
\\\"\\\"\\\"\
With probability p, apply random X/Y/Z to qubit q.\
Still unitary per trajectory.\
\\\"\\\"\\\"\
p = float(np.clip(p, 0.0, 1.0))\
if p \<= 0:\
return psi\
if rng.random() \< (1.0 - p):\
return psi\
choice = int(rng.integers(1, 4)) \# 1:X 2:Y 3:Z\
return apply_1q(psi, PAULIS\[choice\], q, N)\
\
\# ============================================================\
\# 3) Nexus control: alpha_hat -\> glyph -\> leakage probability\
\# ============================================================\
\
def sigmoid(x: float) -\> float:\
return float(1.0 / (1.0 + np.exp(-x)))\
\
def alpha_hat_step(alpha_true: float, se_true: float, rng: np.random.Generator, dither: float = 0.0) -\> float:\
\\\"\\\"\\\"Sample alpha_hat \~ N(alpha_true, se_true\^2), optional uniform dither.\\\"\\\"\\\"\
a = float(rng.normal(loc=alpha_true, scale=se_true))\
if dither \> 0:\
a += float(rng.uniform(-dither, dither))\
return a\
\
def leakage_from_alpha_z(alpha_hat: float, alpha_true: float, se_used: float, beta: float = 3.0, z0: float = 1.5) -\> float:\
\\\"\\\"\\\"\
Z-score gate:\
z = \|alpha_hat - alpha_true\| / se_used\
p = sigmoid(beta \* (z - z0))\
IMPORTANT:\
- If se_used == se_true used to generate alpha_hat, leakage becomes scale-invariant (SILR).\
- If se_used differs from se_true, the invariance breaks and A/B separate.\
\\\"\\\"\\\"\
se_used = max(float(se_used), 1e-12)\
z = abs(alpha_hat - alpha_true) / se_used\
return sigmoid(beta \* (z - z0))\
\
def glyph_router_multiplier(glyph: float, target: float = 0.35, mode: str = \"off\") -\> float:\
\\\"\\\"\\\"\
Optional: make glyph a router (render-layer controls engine-layer).\
\
mode:\
\"off\" -\> multiplier 1.0 (default)\
\"hard\" -\> 0.0 if glyph==target else 1.0 (strict valve)\
\"soft\" -\> gentle suppression near target\
\\\"\\\"\\\"\
if mode == \"off\":\
return 1.0\
if mode == \"hard\":\
return 0.0 if abs(glyph - target) \< 1e-12 else 1.0\
if mode == \"soft\":\
sigma = 0.003\
return float(1.0 - np.exp(-((glyph - target) \*\* 2) / (2 \* sigma \* sigma)))\
raise ValueError(\"mode must be one of: off, hard, soft\")\
\
\# ============================================================\
\# 4) Radiation density matrix from a statevector snapshot\
\# ============================================================\
\
def rho_radiation_from_state(psi: np.ndarray, N: int, t: int) -\> np.ndarray:\
\\\"\\\"\\\"\
At step t (1..N), radiation has t qubits in the tail.\
Convention: BH qubits are \[0..N-t-1\], radiation \[N-t..N-1\].\
\\\"\\\"\\\"\
dimR = 2 \*\* t\
dimB = 2 \*\* (N - t)\
M = psi.reshape(dimB, dimR) \# BH x R\
rhoR = M.conj().T @ M \# R x R\
return rhoR\
\
def renyi2_from_rho(rho: np.ndarray) -\> tuple\[float, float\]:\
\\\"\\\"\\\"Return (S2, purity) where S2 = -log Tr(rho\^2).\\\"\\\"\\\"\
pur = float(np.sum(np.abs(rho) \*\* 2).real) \# Frobenius\^2 for Hermitian\
pur = max(pur, 1e-15)\
return float(-np.log(pur)), float(pur)\
\
def partial_trace_radiation(rho: np.ndarray, keep: list\[int\], t: int) -\> np.ndarray:\
\\\"\\\"\\\"\
Partial trace on a density matrix rho of a t-qubit radiation register.\
keep = list of qubit indices to keep (within radiation: 0..t-1).\
\\\"\\\"\\\"\
keep = list(keep)\
trace = \[i for i in range(t) if i not in keep\]\
\
T = rho.reshape(\[2\] \* t + \[2\] \* t)\
perm = keep + trace + \[i + t for i in keep\] + \[i + t for i in trace\]\
T = np.transpose(T, perm)\
\
dk = 2 \*\* len(keep)\
dt = 2 \*\* len(trace)\
T = T.reshape(dk, dt, dk, dt)\
rho_keep = np.einsum(\"a b c b -\> a c\", T)\
return rho_keep\
\
\# ============================================================\
\# 5) One trajectory (unitary per run): store snapshots\
\# ============================================================\
\
def run_one_trajectory_store(\
N: int = 12,\
alpha_true: float = np.pi / 9,\
\# Measurement reality (generative noise)\
se0_true: float = 0.005,\
se_scale_with_bh_true: bool = True,\
\# Observer/controller belief (used in z-score gate)\
se0_used: float \| None = None, \# None -\> se_used = se_true (SILR)\
se_scale_with_bh_used: bool = False, \# if se0_used is not None, can optionally scale it with BH size\
dither: float = 0.0,\
depth: int = 2,\
beta_z: float = 3.0,\
z0: float = 1.5,\
glyph_route_mode: str = \"off\", \# off/hard/soft\
seed: int = 0\
):\
rng = np.random.default_rng(seed)\
dim = 2 \*\* N\
\
\# Random initial pure state\
psi = (rng.normal(size=dim) + 1j \* rng.normal(size=dim))\
psi /= np.linalg.norm(psi)\
\
n_bh = N\
snaps = np.zeros((N, dim), dtype=complex)\
p_hist = np.zeros(N, dtype=float)\
glyph_hist = np.zeros(N, dtype=float)\
collapse35 = np.zeros(N, dtype=float)\
\
for t in range(1, N + 1):\
\# Scramble BH\
psi = scramble_bh_local(psi, n_bh=n_bh, N=N, depth=depth, rng=rng)\
\
\# True SE (reality)\
se_true = (se0_true / np.sqrt(max(n_bh, 1))) if se_scale_with_bh_true else float(se0_true)\
\
\# Used SE (belief). If None -\> SILR regime (se_used == se_true).\
if se0_used is None:\
se_used = se_true\
else:\
se_used = (se0_used / np.sqrt(max(n_bh, 1))) if se_scale_with_bh_used else float(se0_used)\
\
\# alpha_hat and glyph\
a_hat = alpha_hat_step(alpha_true, se_true, rng, dither=dither)\
g = round(a_hat, 2)\
\
\# leakage from z-score using se_used\
p_t = leakage_from_alpha_z(a_hat, alpha_true, se_used, beta=beta_z, z0=z0)\
\
\# optional glyph routing\
p_t \*= glyph_router_multiplier(g, target=0.35, mode=glyph_route_mode)\
p_t = float(np.clip(p_t, 0.0, 1.0))\
\
p_hist\[t - 1\] = p_t\
glyph_hist\[t - 1\] = g\
collapse35\[t - 1\] = 1.0 if abs(g - 0.35) \< 1e-12 else 0.0\
\
\# Apply leakage on boundary qubit about to be emitted (last BH qubit)\
boundary = n_bh - 1\
psi = apply_pauli_kick_trajectory(psi, q=boundary, N=N, p=p_t, rng=rng)\
\
\# Emit boundary: BH shrinks by 1\
n_bh -= 1\
snaps\[t - 1\] = psi\
\
return snaps, p_hist, glyph_hist, collapse35\
\
\# ============================================================\
\# 6) Ensemble observer metrics: build rho_bar_R(t)\
\# ============================================================\
\
def ensemble_observer_metrics(\
N: int = 12,\
runs: int = 32,\
seed: int = 0,\
\*\*traj_kwargs\
):\
\# Prevent the classic \"multiple values for seed\" error:\
\# if caller mistakenly includes seed in traj_kwargs, we treat it as base_seed.\
base_seed = int(traj_kwargs.pop(\"seed\", seed))\
\
dim = 2 \*\* N\
all_snaps = np.zeros((runs, N, dim), dtype=complex)\
all_p = np.zeros((runs, N), dtype=float)\
all_c35 = np.zeros((runs, N), dtype=float)\
\
for r in range(runs):\
snaps, p_hist, glyph_hist, c35 = run_one_trajectory_store(\
N=N, seed=base_seed + r, \*\*traj_kwargs\
)\
all_snaps\[r\] = snaps\
all_p\[r\] = p_hist\
all_c35\[r\] = c35\
\
S2_ens = np.zeros(N, dtype=float)\
Pur_ens = np.zeros(N, dtype=float)\
MI2_ens = np.zeros(N, dtype=float)\
\
for t in range(1, N + 1):\
dimR = 2 \*\* t\
rho_sum = np.zeros((dimR, dimR), dtype=complex)\
\
for r in range(runs):\
psi = all_snaps\[r, t - 1\]\
rho_sum += rho_radiation_from_state(psi, N=N, t=t)\
\
rho_bar = rho_sum / runs\
\
s2, pur = renyi2_from_rho(rho_bar)\
S2_ens\[t - 1\] = s2\
Pur_ens\[t - 1\] = pur\
\
\# Rényi-2 MI between early and late parts of radiation (within rho_bar)\
if t \>= 2:\
split = t // 2\
early = list(range(0, split))\
late = list(range(split, t))\
\
rhoE = partial_trace_radiation(rho_bar, keep=early, t=t)\
rhoL = partial_trace_radiation(rho_bar, keep=late, t=t)\
\
s2E, \_ = renyi2_from_rho(rhoE)\
s2L, \_ = renyi2_from_rho(rhoL)\
MI2_ens\[t - 1\] = float(s2E + s2L - S2_ens\[t - 1\])\
else:\
MI2_ens\[t - 1\] = 0.0\
\
return {\
\"S2_ens\": S2_ens,\
\"Pur_ens\": Pur_ens,\
\"MI2_ens\": MI2_ens,\
\"p_mean\": all_p.mean(axis=0),\
\"p_std\": all_p.std(axis=0),\
\"collapse35_rate\": all_c35.mean(axis=0),\
\"collapse35_total\": float(all_c35.mean()),\
}\
\
\# ============================================================\
\# 7) Run examples + plot\
\# ============================================================\
\
def plot_abc(N: int, A: dict, B: dict, C: dict, title_prefix: str = \"\"):\
t = np.arange(1, N + 1)\
\
plt.figure()\
plt.plot(t, A\[\"S2_ens\"\], label=\"A\")\
plt.plot(t, B\[\"S2_ens\"\], label=\"B\")\
plt.plot(t, C\[\"S2_ens\"\], label=\"C\")\
plt.xlabel(\"Emitted qubits\")\
plt.ylabel(\"S2_ens(R) \[nats\]\")\
plt.title(f\"{title_prefix}Observer-level Rényi-2 entropy (ensemble mixedness)\")\
plt.legend()\
plt.show()\
\
plt.figure()\
plt.plot(t, A\[\"Pur_ens\"\], label=\"A\")\
plt.plot(t, B\[\"Pur_ens\"\], label=\"B\")\
plt.plot(t, C\[\"Pur_ens\"\], label=\"C\")\
plt.xlabel(\"Emitted qubits\")\
plt.ylabel(\"Pur_ens = Tr(rho_bar\^2)\")\
plt.title(f\"{title_prefix}Observer-level purity\")\
plt.legend()\
plt.show()\
\
plt.figure()\
plt.plot(t, A\[\"MI2_ens\"\], label=\"A\")\
plt.plot(t, B\[\"MI2_ens\"\], label=\"B\")\
plt.plot(t, C\[\"MI2_ens\"\], label=\"C\")\
plt.xlabel(\"Emitted qubits\")\
plt.ylabel(\"I2_ens(early:late) \[nats\]\")\
plt.title(f\"{title_prefix}Observer-level Rényi-2 mutual information\")\
plt.legend()\
plt.show()\
\
plt.figure()\
plt.plot(t, A\[\"collapse35_rate\"\], marker=\"o\", label=\"A\")\
plt.plot(t, B\[\"collapse35_rate\"\], marker=\"o\", label=\"B\")\
plt.plot(t, C\[\"collapse35_rate\"\], marker=\"o\", label=\"C\")\
plt.xlabel(\"Emitted qubits\")\
plt.ylabel(\"P(glyph = 0.35)\")\
plt.title(f\"{title_prefix}Glyph collapse rate (render layer)\")\
plt.legend()\
plt.show()\
\
def main():\
N = 12\
runs = 32\
seed = 7\
\
alpha_true = np.pi / 9 \# latent constant\
print(\"alpha_true:\", float(alpha_true), \" pi/9:\", float(np.pi/9))\
\
\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\
\# (I) SILR: se_used == se_true (reproduces the accidental invariance)\
\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\
silr_shared = dict(\
alpha_true=alpha_true,\
depth=2,\
beta_z=3.0,\
z0=1.5,\
glyph_route_mode=\"off\",\
\# se0_used=None =\> se_used == se_true\
se0_used=None,\
)\
\
A_silr = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0020, dither=0.0, \*\*silr_shared)\
B_silr = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0050, dither=0.0, \*\*silr_shared)\
C_silr = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0050, dither=0.0005, \*\*silr_shared)\
\
print(\"\\n\[SILR\] Mean p over time A/B/C:\",\
A_silr\[\"p_mean\"\].mean(), B_silr\[\"p_mean\"\].mean(), C_silr\[\"p_mean\"\].mean())\
print(\"\[SILR\] Final-step p_mean A/B/C:\",\
A_silr\[\"p_mean\"\]\[-1\], B_silr\[\"p_mean\"\]\[-1\], C_silr\[\"p_mean\"\]\[-1\])\
print(\"\[SILR\] collapse35_total A/B/C:\",\
A_silr\[\"collapse35_total\"\], B_silr\[\"collapse35_total\"\], C_silr\[\"collapse35_total\"\])\
\
plot_abc(N, A_silr, B_silr, C_silr, title_prefix=\"\[SILR\] \")\
\
\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\
\# (II) Broken-SILR: se_used is a fixed belief (restores A vs B separation)\
\# \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\
\# se0_used is the observer\'s belief about SE (constant or optionally BH-scaled).\
\# Use se_scale_with_bh_used=False for fixed denominator across time.\
broken_shared = dict(\
alpha_true=alpha_true,\
depth=2,\
beta_z=3.0,\
z0=1.5,\
glyph_route_mode=\"off\",\
se0_used=0.0035,\
se_scale_with_bh_used=False,\
)\
\
A = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0020, dither=0.0, \*\*broken_shared)\
B = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0050, dither=0.0, \*\*broken_shared)\
C = ensemble_observer_metrics(N=N, runs=runs, seed=seed, se0_true=0.0050, dither=0.0005, \*\*broken_shared)\
\
print(\"\\n\[Broken-SILR\] Mean p over time A/B/C:\",\
A\[\"p_mean\"\].mean(), B\[\"p_mean\"\].mean(), C\[\"p_mean\"\].mean())\
print(\"\[Broken-SILR\] Final-step p_mean A/B/C:\",\
A\[\"p_mean\"\]\[-1\], B\[\"p_mean\"\]\[-1\], C\[\"p_mean\"\]\[-1\])\
print(\"\[Broken-SILR\] collapse35_total A/B/C:\",\
A\[\"collapse35_total\"\], B\[\"collapse35_total\"\], C\[\"collapse35_total\"\])\
\
plot_abc(N, A, B, C, title_prefix=\"\[Broken-SILR\] \")\
\
if \_\_name\_\_ == \"\_\_main\_\_\":\
main()
