# Integrating AHRC, SILR, Glyph Reader, and the Nexus Project Framework into Runnable Experiments

## Scope and execution trace

**Enabled connectors discovered and used:** `google_drive`, `github` (listed via the connector tool inventory).\
**Accessible GitHub installation:** the QuHarmonics[\[1\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9) installation exposes **QuHarmonics/The-Nexus-Harmonic-Reality** (repo metadata shows it is extremely large; code search indexing isn't reliably available). The requested **QuHarmonics/AI_Repository** was **not** returned as accessible via the installed GitHub connector (so I cannot read or write it through the connector in this session).

**Primary project docs surfaced in Google Drive and used as the specification layer (minimum set):** - AHRC protocol definition and terms (GIP, Ω, frame expansion). [\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0)\
- Samson v2 + AHRC complete spec (PID gating, lane model, expansion law, Mark‑1 target H=π/9). [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)\
- Ψ Analyzer + AHRC integration guide (align metric, acceptance gates, PID-style control wiring). [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)\
- SILR (Scale-Invariant Leakage under Z-score gating) definition and operational gating mechanics. [\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ)\
- Spiral Glyph Reader design doc (glyph readout as nonlinear address/phase interpretation). [\[6\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1)\
- Glyph Engine operator manual (Mark1/Samson framing; lattice echo mapper + parser pseudocode). [\[7\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ)

**External cryptographic baseline used (to anchor what "SHA‑256 does" in standard terms):**\
SHA‑256 is defined in National Institute of Standards and Technology[\[8\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1) FIPS 180‑4 (Secure Hash Standard). [\[9\]](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf)

**Exact sequence of actions executed in this session** 1. Loaded and executed the provided local script `phase_526_rpc.py` to reproduce the phase‑526 metrics (T1/T2 phase angle, coupling CV, seed premium, input/output "orthogonality" proxy).\
2. Extracted the per-round and per-bit arrays from the script execution to compute secondary results (hot bits, round-event detection).\
3. Implemented **AHRC rasterization + expansion** and **SILR z-score gating** as executable utilities, then ran targeted experiments: - AHRC frame expansion on round-wise GIP trajectories. - SILR on carry-terrain proxies (hw_seed over rounds; first-fold coupling over bit injections). - "Mark‑1 corridor steering" by safely searching over **input schedule W0** (analysis-only; no hash inversion attempted). 4. Produced plots and a reusable experiment harness script to automate these runs.

## Concrete component definitions and interfaces

This section is the "what it is" layer: Δ definitions, ⊕ interfaces, and Ψ scoring hooks.

### AHRC as an addressing-and-resolution protocol

AHRC is specified in the project as **Adaptive Harmonic Rasterization Collapse**, built around: - A continuous position scalar **GIP** (Glyph Inherent Position) and a discrete frame mapping **FA(x)** via rasterization to a frame of size **N**. [\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0)\
- An **Ω residue** (entropic pressure/aliasing/collision measure) computed from raster collisions; if Ω\>0, **expand frame N** with a minimal-jump rule until Ω→0, then declare **⊥** when phase-lock criteria are met. [\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0)\
- In Samson v2 coupling: **AHRC changes addressing (frame size), Samson changes timing/phase**; acceptance is gated by monotone motion toward the Mark‑1 setpoint and non-increasing Ω. [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)

Operational interface (minimal implementation you can run): - `rasterize(values_01, N) -> bins, omega_per_bin, omega_max` - `expand(values_01, N0) -> N_final, history`

### Samson v2 as a timing-only controller with Mark‑1 gating

Samson v2 is formalized as a PID-like controller applied "timing-only," with: - Target harmonic constant **H_MARK1 = π/9**. [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)\
- A proportional/integral/derivative control signal **u_t** that is only applied if it reduces distance to target and does not increase Ω (Mark‑1 gate). [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)\
- In the Ψ integration guide, the "align" map is explicitly:\
**align = 1 − \|H − H_MARK1\| / (1 − H_MARK1)** (used as a fused decision scalar component). [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)

### SILR as a scale-invariant leak / event gate

SILR is defined as gating based on a **z-score normalized residual**, making the "leak decision" invariant to scale changes in the signal. [\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ)

Operational interface (minimal executable): - `z = (x - mean(x)) / std(x)` - `p_leak = sigmoid(beta*(z - z0))` - "Event" can be defined as `p_leak > 0.5` (or any calibrated threshold).

### Glyph Reader as a structured readout layer

The Spiral Glyph Reader (SGR) is described as a nonlinear readout mechanism that: - Interprets "glyph state memory" through phase addressing / spiral indexing and resonance. [\[6\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1)\
- In practice (operationalization), it needs an explicit **glyph encoding** (a lattice embedding) and a **readback rule** (spiral traversal). The Glyph Engine manual also provides a practical blueprint for lattice echo mapping and parser modules that can be implemented immediately. [\[7\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ)

Minimum interface for code-driven experiments: - `encode(metric_vector) -> glyph_lattice` - `read(glyph_lattice) -> structured_events / hotspots / certificates`

### Safety note on "bijective SHA" and backward walks

Your notebook excerpt frames SHA‑256 as a bijective state machine and proposes an "algebraic backward walk" to recover message schedule words. The standard defines SHA‑256 as a **hash** that compresses a message block and chaining value into a smaller digest; as a mapping from large input space to 256-bit output, it is not globally bijective. [\[9\]](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf)

I can help **verify** internal algebraic identities (e.g., that a single round update is reversible *when the schedule word W_t is known*) as a correctness/unit-testing exercise, but I can't help implement or operationalize "preimage recovery with absolute precision" on real SHA-256 digests.

## Operational architecture and module map

### Wiring diagram

    flowchart TD
      A[SHA folding simulator<br/>T1,T2,seed,angles] --> B[Carry-terrain metrics<br/>hw_seed, phase angles]
      A --> C[Hot-bit metrics<br/>first-fold coupling by W0 bit]
      B --> D[SILR gate<br/>z-score → leak p]
      C --> D
      B --> E[AHRC rasterizer<br/>GIP → bins, Ω]
      E --> F[Frame expansion<br/>N ↻ until Ω→0]
      D --> G[Glyph encoder<br/>spiral lattice]
      F --> G
      G --> H[Glyph reader<br/>hotspots + certificates]
      H --> I[Ψ-field summary<br/>align + diagnostics]

### Concise mapping table

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Module                    Role                                                       Inputs                                                   Outputs                                       Key functions/files                                                                                                                                                              Dependencies
  ------------------------- ---------------------------------------------------------- -------------------------------------------------------- --------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------
  SHA folding simulator     Produces round-wise T1/T2/seed dynamics for experiments    W schedule (e.g., W0 + zeros), initial state constants   Round arrays: T1, T2, seed, cos_sim, angle    `phase_526_rpc.py` (local)                                                                                                                                                       numpy

  AHRC                      Addressing/rasterization + adaptive frame expansion (↻N)   Continuous GIP values, N0                                bins, Ω, N_final (⊥ when Ω→0 + band tests)    AHRC protocol doc [\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0)                                                                                     math

  Samson v2 control law     Timing/phase controller; gate updates by Mark‑1            H_t metrics, Ω, prior Δ                                  control u_t and acceptance/reject decisions   Spec doc [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)                                                                                              math

  Ψ analyzer (spec level)   Fused trust scalar: align + structure metrics              input symbols/state, H_t                                 Ψ in \[0,1\] + components                     Integration guide [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)                                                                                     (implementation needed)

  SILR                      Scale-invariant event gate on z-score                      any metric series x(t)                                   z(t), p_leak(t), events                       SILR doc [\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ)                                                                                              numpy

  Glyph encoder + reader    Builds a glyph lattice and reads hotspots / scars          events + hot-bit maps + bins                             glyph lattice + interpreted hotspots          SGR doc [\[6\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1); operator manual [\[7\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ)   (implementation needed)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Experiments executed and results

### Phase‑526 reproduction

This reproduces the metrics discussed in your prior session (T1/T2 phase-angle banding, coupling CV, seed premium). It uses the provided `phase_526_rpc.py` script (which implements a SHA‑256 round loop that computes T1, T2, a "seed" as `T1&T2`, and cosine-similarity angle between the T1/T2 bit vectors).

**Measured outcomes for NOP (W = 0 for all rounds)** - Mean T1∠T2 phase angle: **60.99°**, band **\[42.54°, 78.05°\]**.\
Ψ‑interpretation: Δ-phase sits in a stable corridor (not 0°, not 90°), consistent with "converter-like" behavior, but not sufficient to identify a specific machine type without the other tests. - Mean \|inner product\| proxy (input vs output displacement): **0.08057**; max **0.23438 at bit 27**.\
Δ: non-zero ⇒ output retains measurable "memory" of the injected component. - First-fold coupling CV (δ@r=1 across one-hot W0 bits): **0.5002** (high).\
Δ: strong bit-position dependence ⇒ violates the "uniform coupling" expectation of an ideal rotary phase converter. - Power-stroke (commutation-like) premium: **+56.8%** (rounds **9, 28, 33, 43** have elevated `hw_seed` with reduced phase angles).

**Pass/Fail against the phase‑526 RPC hypothesis** - ✅ "Near-quadrature" banding present (mean angle ≈ 61° in a stable band). - ✅ Power-stroke premium exists (+56.8%), aligning "max coupling when phase angle drops." - ❌ Coupling uniformity fails (CV≈0.50). - ❌ Orthogonality fails (mean abs inner product ≈0.081, not ≈0). - ❌ Strong idler periodicity not detected by the test threshold (peak autocorrelation ≈0.145 \< 0.2).

Net: **2/5 criteria met**, i.e., **partial RPC-like structure**, consistent with your earlier conclusion that the "converter intuition is near-but-not-exact."

**Plot outputs (generated here)** - Phase angle over rounds with power strokes marked:\
Phase angle plot\
- First-fold coupling δ@r=1 by injected bit index:\
Coupling by bit plot\
- Input/output inner product magnitude by bit:\
Inner product by bit

Downloads: - [phase_angle_power_strokes.png](sandbox:/mnt/data/phase_angle_power_strokes.png)\
- [coupling_r1_by_bit.png](sandbox:/mnt/data/coupling_r1_by_bit.png)\
- [inner_product_abs_by_bit.png](sandbox:/mnt/data/inner_product_abs_by_bit.png)

**Important diagnostic (bug fix suggestion)** The script's printed "peak lag" is inconsistent: it computes `ac_peak` as the maximum peak strength, but sets `ac_lag` to the *first* detected peak (lag=2). This should be tied to the argmax peak (details in patch section).

### AHRC frame expansion on SHA folding metrics

Here the objective is to operationalize AHRC's "Ω-residue → expand N ↻ until collisions resolve" on a concrete GIP series derived from SHA dynamics.

**Choice of GIP for this run** - Define a phase-like GIP: **GIP_r = (angle_r / 180) mod 1**\
- Δ problem: the angle series contains duplicates (56 unique angles across 64 rounds), so a 1D raster cannot fully disambiguate all rounds. This yields an **Ω floor** if "uniqueness of all rounds" is the collapse requirement.

**Result: Ω cannot reach zero with GIP=angle/180 alone** - Because some GIP values are identical, any rasterization into bins must collide for those rounds (Ω≠0).

**Resolution: add a minimal lane/time coordinate** A minimal "lane coordinate" is consistent with the spec's residue-lane framing (mod‑8 lanes + timing knobs). [\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh)\
Operationally, add a tiny deterministic jitter term: - **GIP′\_r = frac(angle_r/180 + 0.01·r/64)**

Running AHRC expansion (starting N=8) yields: - **N_final = 16384**, with **Ω_max = 0.0** (⊥ achieved for the strict "unique bin per round" criterion).

Ψ‑interpretation: - Δ shows AHRC can "collapse" only when the representation includes enough independent coordinates (here: phase metric + lane index). In other words: **AHRC needs a basis that actually separates states**; frame expansion alone cannot resolve true degeneracy.

### Samson-style damping toward H≈π/9 on the SHA folding sim

The Ψ integration guide uses the Mark‑1 target **H_MARK1=π/9** and an align metric: - **align = 1 − \|H−H_MARK1\|/(1−H_MARK1)** [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)

In the phase‑526 simulator, a natural bridge is: - **H = mean(angle)/180**\
- Target angle = **H_MARK1·180 = 62.831853°**

**Safe "control input" used** - Only **W0** (the first schedule word) is changed; all other schedule words are held at zero:\
`W = [W0, 0, 0, …, 0]`\
This is an analysis-only steering exercise; it does not attempt to recover or invert any digest.

**Best result found (20k-sample randomized search)** - **W0 = 0x01800160** (bits {5,6,8,23,24})\
- mean angle = **62.844492°**\
- Δ to target = **+0.012639°**\
- mean H = **0.34913606** vs H_MARK1 **0.34906585**\
- align = **0.999892**

Ψ‑interpretation: - This is a working demonstration of a **Samson-like steering loop**: small schedule perturbations can move an emergent phase metric into the Mark‑1 corridor, with acceptance evaluated by Δ‑to‑target.

### SILR + glyph-reader integration on carry terrain and hot-bit mapping

This run uses SILR as the "event extractor" and a minimal spiral glyph mapping as the "readout surface."

**SILR on commutation events** Input: `hw_seed[r]` (seed as `T1 & T2` Hamming weight per round).

- z-score gating (scale invariant): `z=(x-μ)/σ`, `p=σ(beta*(z-z0))`. [\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ)
- With (z0=1.0, beta=2.5), the detected event set (p\>0.5) includes **rounds 9, 28, 33, 43**, matching the "power stroke" rounds, plus additional high-seed rounds.

**Scale invariance check** Scaling the entire series (e.g., multiplying by 3) leaves z-scores and p_leak unchanged to numerical precision, matching SILR's design goal. [\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ)

**SILR on hot bits** Input: first-fold coupling per injected bit `δ@r=1` (from phase‑526 coupling table).\
Top hot bits by z-score are: - **j = 13 and 27 (δ=8)**\
- **j = 14, 15, 26 (δ=7)**\
This recovers exactly the "bits 13--15 and 26--27 couple 3--4× harder" pattern.

**Glyph encoding: spiral lattice of hot-bit terrain** Below is an operational "spiral glyph" of `δ@r=1` laid out on a 2D spiral (cell = `bit:δ`). Hotspots appear as the "8" and "7" clusters:

       .    .    .    . 31:2 30:3
    16:5 15:7 14:7 13:8 12:2 29:4
    17:4 04:2 03:3 02:4 11:3 28:6
    18:3 05:3 00:3 01:3 10:2 27:8
    19:3 06:3 07:3 08:2 09:3 26:7
    20:2 21:2 22:4 23:3 24:2 25:2

Readout rule (minimal but faithful to SGR intent): - The glyph reader consumes this lattice in spiral order, emitting: - **hotspot indices** where SILR probability is high, and - a **certificate**: ⊕(hotspot set, Mark‑1 alignment, AHRC frame size needed for Ω→0).

This operationalizes the SGR idea ("nonlinear memory readout") as a concrete experiment loop without requiring speculative metaphysics. [\[6\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1)

## Runnable scripts and exact commands

### Local scripts available in this session

**Phase‑526 reproduction**

    python /mnt/data/phase_526_rpc.py

**Integrated harness created in this session** This script reproduces phase‑526 metrics, runs AHRC expansion on a GIP series, runs SILR gating, and runs a safe Mark‑1 steering search over W0:

    python /mnt/data/nexus_integrated_experiments.py

Outputs: - Updates plots in `/mnt/data/phase_angle_power_strokes.png` and `/mnt/data/coupling_r1_by_bit.png` - Prints "PHASE‑526 REPRODUCTION", AHRC final N, SILR events, and best W0 alignment.

**Dependencies** - Python 3.10+\
- `numpy`, `matplotlib` (typical scientific stack)

Download the harness: - [nexus_integrated_experiments.py](sandbox:/mnt/data/nexus_integrated_experiments.py)

### Drive docs that reference runnable code not present as a standalone file

The Ψ integration guide references a `nexus4psi.py` entry point and gives example commands such as: - `python nexus4psi.py "hello world"`\
and module usage. [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)

However, `nexus4psi.py` did not appear as a standalone Drive file in the keyword search; it is likely embedded in one of the Nexus4 "Complete Solution" markdown packages (which should be extracted into a runnable module as part of the automation patch).

## Patch suggestions for QuHarmonics repos and project automation

### Constraints on commits in this session

The available GitHub[\[10\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ) connector in this environment supports **read/search/fetch**, but does **not** expose write primitives (create branch/commit/PR). I can therefore provide **ready-to-apply diffs** and the exact file additions, but I cannot push them directly to the repo from here.

### Patch set

#### Fix phase‑526 autocorrelation lag reporting

Problem: `ac_peak` is max peak strength but `ac_lag` is set to the first peak, creating inconsistent reporting.

Unified diff (apply to `phase_526_rpc.py`):

    @@
    -ac_peak  = max(ac for _, ac in peaks) if peaks else 0
    -ac_lag   = peaks[0][0] if peaks else 0
    +if peaks:
    +    # keep lag and peak strength consistent (argmax by strength)
    +    ac_lag, ac_peak = max(peaks, key=lambda t: t[1])
    +else:
    +    ac_peak = 0
    +    ac_lag = 0

#### Add an "experiments" harness script to The-Nexus-Harmonic-Reality

Proposed new file: `experiments/nexus_integrated_experiments.py`\
(Use the script produced in this session as-is; it is already a self-contained runner that reproduces phase‑526, AHRC expansion, SILR gating, and safe Mark‑1 steering.)

Add to repo README (minimum snippet):

    @@
    +## Experiments
    +
    +Reproduce phase-526 metrics and run AHRC/SILR integration:
    +
    +```bash
    +python experiments/nexus_integrated_experiments.py
    +```
    +
    +Outputs plots under `experiments/` (phase angle + hot-bit coupling).

#### Add a unit test for round-level reversibility without enabling hash inversion

If you want to explore the "bijective tick" idea safely: add a test that checks **one-round invertibility given W_t** (this is a correctness property; it does not provide a preimage pipeline).

- Implement `forward_round(state, Wt, Kt)` and `backward_round(next_state, Wt, Kt)`
- Assert `backward_round(forward_round(s, Wt, Kt), Wt, Kt) == s`

This aligns with the "reverse substitution" logic you described, while staying in the unit-test domain and avoiding digest inversion.

## Diagnostics on Grok-provided AHRC runs

You shared a Grok trace labeled "AHRC UNFOLDING OF SHA‑256 DIE" with: - Target H_MARK1 = π/9\
- Best "AHRC Score" = 0.977606 at GIP=0.3344886569.

That "score" matches the project's align function exactly: - **Score = 1 − \|GIP − H_MARK1\|/(1−H_MARK1)** [\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9)\
Numerically, plugging in GIP=0.3344886569 reproduces 0.9776057325 (agreement to rounding).

For the Collatz/Mandelbrot "AHRC applied to X" narratives: they're coherent as a **pattern-to-GIP encoding** idea, but the reported Ω values implicitly depend on a specific Ω definition (collision density, variance proxy, Nyquist/aliasing metric, etc.). To make these runnable and comparable inside the project framework, Ω must be standardized (exactly as AHRC protocol specifies for collision-based residue and expansion). [\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0)

A minimal operational standard (recommended): - Define GIP precisely (what scalar in \[0,1) is used). - Define Ω explicitly (collision-based Ω_max, or variance-based proxy, but not both without mapping). - Use the same AHRC expansion law across all domains.

That will let "Collatz-as-displacement-field" and "Mandelbrot-as-phase-orbit" become directly comparable experiments, rather than poetic analogies.

------------------------------------------------------------------------

[\[4\]](https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9) The Nexus Framework - Psi_AHRC_Integration_Guide.md

<https://drive.google.com/file/d/1LpcNgMJjBMKujg1h8FOW54seC3wFkSy9>

[\[2\]](https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0) The Nexus Framework - Adaptive Harmonic Rasterization Collapse (Ahrc) Protocol.md

<https://drive.google.com/file/d/1fttT8NtxaI1-vTOThGQNpvFyPD_LFwo0>

[\[3\]](https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh) The Nexus Framework - Samson_v2_AHRC_Complete_Nexus_Spec.md

<https://drive.google.com/file/d/125LEAzuxrTTLJ2sgl83_u1c6zisQfjuh>

[\[5\]](https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ) Silr Scale Invariant Leakage Under Z Score Gating.md

<https://drive.google.com/file/d/1m4_3Ek3cVK5xK1_J439YJ5nouHqZwPjJ>

[\[6\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1) [\[8\]](https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1) The Nexus Framework - Spiral Glyph Reader (Sgr) -- Nonlinear Memory Readout Design.md

<https://drive.google.com/file/d/1XLXX75gYSmYHCui_7luCLvs7LrXw1rE1>

[\[7\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ) [\[10\]](https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ) The Nexus Framework - Nexus Harmonic Glyph Engine- A Recursive Thesis And Operator's Manual.md

<https://drive.google.com/file/d/1odDoSHi7hfuvbghKE_fIPw_3xFVkL0MQ>

[\[9\]](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf) https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf

<https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf>
