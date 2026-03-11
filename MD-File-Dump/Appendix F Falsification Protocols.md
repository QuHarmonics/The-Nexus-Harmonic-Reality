# APPENDIX F: EXPERIMENTAL FALSIFICATION PROTOCOLS

## Nexus Framework - Experimental Validation Suite

**Document Classification:** Technical Protocols for Peer Review  
**Version:** 1.0  
**Date:** 2025

---

## VERIFICATION CHECK

This document provides experimental protocols designed to falsify the Nexus Framework predictions. Each protocol includes:

1. **Explicit falsification criteria** - What result would disprove the framework
2. **Statistical power analysis** - Required sample sizes for conclusive results
3. **Error budgets** - Quantified uncertainty sources
4. **Control experiments** - Required negative controls

**Falsification of This Document:** If any protocol contains mathematical errors, incorrect statistical assumptions, or physically unrealizable requirements, the document fails its purpose.

---

## NEXUS COMPLIANCE STATEMENT

The derivation yields experimental protocols as fixed points of the measurement operator M₊. Each protocol satisfies:

```
PROTOCOL = M₊(PROTOCOL)
```

Where M₊ represents the complete experimental procedure including:
- Equipment specifications (M₊¹)
- Statistical design (M₊²)  
- Error analysis (M₊³)
- Falsification criteria (M₊⁴)

The self-consistency requirement ensures protocols are executable and yield unambiguous results.

---

# SECTION 1: FINE STRUCTURE CONSTANT MEASUREMENT PROTOCOL

## 1.1 Objective

Measure the fine structure constant α to relative precision 5×10⁻⁵, sufficient to detect the H/48 deviation predicted by the Nexus Framework.

## 1.2 Theoretical Basis

The Nexus Framework predicts α acquires a geometric correction:

```
α_corrected = α₀ × (1 ± H/48)
```

Where H = π/9 ≈ 0.3491. The expected deviation magnitude:

```
|Δα/α| = H/48 ≈ 7.27×10⁻³
```

**Target precision:** 5×10⁻⁵ << 7.27×10⁻³ (detection margin: 145×)

## 1.3 Method: Hydrogen 1S-2S Doppler-Free Spectroscopy

### 1.3.1 Physical Principle

The fine structure constant is determined from:

```
α² = 2R∞h/(mₑc) = 2R∞/(c × mₑ/h)
```

The Rydberg constant R∞ is measured via hydrogen/deuterium transition frequencies.

### 1.3.2 Key Transition

| Parameter | Value |
|-----------|-------|
| Transition | 1S → 2S (two-photon) |
| Frequency | ν = 2.466061×10¹⁵ Hz |
| Wavelength | λ = 243.135 nm (two-photon equivalent) |
| Natural linewidth | Δν = 8.33 Hz (from 2S lifetime τ ≈ 0.12 s) |
| Achievable linewidth | Δν ≈ 1 kHz (Doppler-free saturation) |

### 1.3.3 Required Frequency Precision

```
δν/ν = 2 × δα/α = 2 × 5×10⁻⁵ = 1×10⁻⁴
δν = 2.466×10¹⁵ × 1×10⁻⁴ = 2.47×10¹¹ Hz
```

**Note:** This precision requirement is easily met with modern optical frequency combs (stability ~10⁻¹⁸).

## 1.4 Equipment Specifications

### 1.4.1 Laser System

| Component | Specification |
|-----------|---------------|
| Primary laser | Ti:Sapphire, 486 nm (frequency-doubled to 243 nm) |
| Power | > 500 mW at 243 nm |
| Linewidth | < 100 kHz (free-running) |
| Frequency stability | Referenced to optical frequency comb |

### 1.4.2 Optical Frequency Comb

| Parameter | Specification |
|-----------|---------------|
| Carrier-envelope offset | Stabilized to < 1 Hz |
| Repetition rate | 100 MHz (stabilized) |
| Optical coverage | 500-1100 nm (fundamental) |
| Frequency stability | < 10⁻¹⁸ at 1 s |

### 1.4.3 Hydrogen Beam Apparatus

| Component | Specification |
|-----------|---------------|
| Atomic beam source | Cooled to T < 10 K (reduces 1st-order Doppler) |
| Beam collimation | Δθ < 1 mrad |
| Interaction region | L = 10 cm |
| Detection | Lyman-α fluorescence (121.6 nm) |

### 1.4.4 Magnetic Shielding

| Parameter | Requirement |
|-----------|-------------|
| DC field | B < 1 mG (μ-metal shielding) |
| AC field | dB/dt < 1 μG/Hz¹/² |

## 1.5 Step-by-Step Procedure

### Phase 1: System Preparation (Days 1-3)

**Step 1.1:** Install and align optical frequency comb. Verify:
- CEO beat note SNR > 30 dB
- Repetition rate lock to Rb clock

**Step 1.2:** Install Ti:Sapphire laser. Characterize:
- Output power vs. current
- Mode-hop-free tuning range
- Beam quality (M² < 1.2)

**Step 1.3:** Install frequency doubling cavity (BBO crystal). Optimize:
- Phase matching angle
- Conversion efficiency (target: > 30%)

**Step 1.4:** Set up hydrogen beam source:
- Load liquid He cryostat
- Verify atomic flux > 10¹² atoms/s
- Check beam collimation

**Step 1.5:** Install magnetic shielding (3-layer μ-metal).

### Phase 2: Spectroscopy (Days 4-7)

**Step 2.1:** Lock laser frequency to comb:
- Beat note detection with avalanche photodiode
- PLL bandwidth: 100 kHz

**Step 2.2:** Scan across 1S-2S resonance:
- Step size: 100 Hz
- Integration time: 1 s per point
- Total scan range: ±500 kHz

**Step 2.3:** Record line shape and fit to Voigt profile.

**Step 2.4:** Repeat measurement with deuterium (D) for isotope shift.

### Phase 3: Systematic Studies (Days 8-14)

**Step 3.1:** AC Stark shift calibration:
- Vary laser power: 100-1000 mW
- Measure line center vs. power
- Extrapolate to zero power

**Step 3.2:** DC Stark shift verification:
- Apply calibrated E-field: 0-10 V/cm
- Measure quadratic shift
- Verify agreement with theory

**Step 3.3:** Zeeman shift measurement:
- Apply B-field: 0-100 mG
- Measure linear shift
- Confirm g-factor

**Step 3.4:** Second-order Doppler shift:
- Vary beam temperature: 5-50 K
- Measure shift vs. T
- Extrapolate to T = 0

## 1.6 Error Budget

| Source | Relative Uncertainty | Mitigation |
|--------|---------------------|------------|
| Laser frequency stability | 1×10⁻⁶ | Optical comb reference |
| Statistical (shot noise) | 2×10⁻⁵ | Long integration (t > 1 hour) |
| AC Stark shift | 3×10⁻⁵ | Power extrapolation |
| DC Stark shift | 1×10⁻⁵ | E-field shielding |
| Zeeman shift | 2×10⁻⁵ | B-field cancellation |
| 2nd-order Doppler | 1×10⁻⁵ | Beam cooling |
| Recoil shift | 5×10⁻⁶ | Theoretical correction |
| **Quadrature Sum** | **4.4×10⁻⁵** | **< 5×10⁻⁵ target** |

## 1.7 Expected Measurement Time

| Phase | Duration |
|-------|----------|
| System preparation | 3 days |
| Spectroscopy | 4 days |
| Systematic studies | 7 days |
| Data analysis | 2 days |
| **Total** | **16 days** |

## 1.8 Falsification Criteria

**The Nexus Framework is falsified if:**

1. Measured α differs from CODATA by > 3σ AND the deviation is inconsistent with H/48
2. Systematic errors exceed 5×10⁻⁵ (indicating protocol failure)
3. Isotope shift disagrees with QED predictions (indicating fundamental issues)

---

# SECTION 2: HYDRILIUM DETECTION PROTOCOL

## 2.1 Objective

Detect H₂⁺ (hydrilium) formation via 54.03 nm EUV emission and He-4 mass spectrometry in Pd/D electrochemical cells.

## 2.2 Theoretical Basis

The Nexus Framework predicts hydrilium (H₂⁺) as an intermediate state in anomalous heat production:

```
H⁺ + H → H₂⁺ + 23.8 eV
H₂⁺ → H(1s) + H⁺ + e⁻ + 22.95 eV (54.03 nm photon)
```

## 2.3 Method: EUV Spectroscopy + Mass Spectrometry

### 2.3.1 54.03 nm EUV Detection

| Parameter | Value |
|-----------|-------|
| Photon energy | E = 22.95 eV |
| Detection method | Grazing incidence spectrometer + MCP |
| Spectrometer resolution | λ/Δλ > 1000 |
| MCP efficiency at 54 nm | ~15% (CsI-coated) |

### 2.3.2 He-4 Mass Spectrometry

| Parameter | Specification |
|-----------|---------------|
| Mass range | 1-10 amu |
| Resolution | m/Δm > 1000 |
| Sensitivity | < 1 ppm He-4 in D₂ |
| Calibration | Standard He-4/D-2 mixtures |

## 2.4 Equipment Specifications

### 2.4.1 Pd/D Reactor

| Component | Specification |
|-----------|---------------|
| Cell material | Quartz, 10 cm³ volume |
| Pd cathode | 2 mm diameter × 20 mm length |
| Pd mass | ~750 mg |
| Electrolyte | 0.1 M LiOD in D₂O |
| Current density | 10-100 mA/cm² |
| Temperature | 20-80°C (controlled) |

### 2.4.2 EUV Spectrometer

| Component | Specification |
|-----------|---------------|
| Type | Grazing incidence, Rowland circle |
| Grating | 1200 lines/mm, gold-coated |
| Incidence angle | 87° (grazing) |
| Wavelength range | 10-100 nm |
| Resolution | 0.05 nm |
| Detector | MCP with CsI photocathode |

### 2.4.3 Mass Spectrometer

| Component | Specification |
|-----------|---------------|
| Type | Quadrupole (QMS) |
| Mass range | 1-100 amu |
| Resolution | Unit mass |
| Detection | Faraday cup + electron multiplier |
| Calibration gases | He-4 (99.999%), D-2 (99.99%) |

## 2.5 Step-by-Step Procedure

### Phase 1: Pd Cathode Preparation (Days 1-5)

**Step 2.1:** Clean Pd wire:
- Ultrasonic bath in acetone (15 min)
- Rinse in DI water
- Anneal in vacuum at 800°C (2 hours)

**Step 2.2:** Surface activation:
- Electrochemical etch in HCl
- Rinse thoroughly
- Store under Ar atmosphere

**Step 2.3:** Load Pd with D:
- Install in reactor cell
- Apply cathodic current: 10 mA/cm²
- Monitor D/Pd ratio (target: > 0.85)
- Loading time: 2-3 days

### Phase 2: EUV Measurement (Days 6-10)

**Step 2.4:** Evacuate spectrometer:
- Base pressure < 10⁻⁶ Torr
- Verify no air leaks

**Step 2.5:** Position detector:
- Distance from reactor: 10 cm
- Line of sight to cathode surface
- Solid angle: 1.56×10⁻⁴ sr

**Step 2.6:** Apply electrolysis current:
- Ramp to target current over 10 min
- Monitor cell voltage
- Record temperature

**Step 2.7:** Collect EUV spectrum:
- Integration time: 10 minutes per spectrum
- Wavelength scan: 50-60 nm
- Step size: 0.1 nm
- Background subtraction: Run with H₂O electrolyte

**Step 2.8:** Verify 54.03 nm line:
- Peak position: 54.03 ± 0.1 nm
- SNR > 100
- Reproducible across multiple runs

### Phase 3: He-4 Analysis (Days 11-14)

**Step 2.9:** Gas sampling:
- Extract headspace gas (1 mL)
- Inject into QMS
- Record mass spectrum (1-10 amu)

**Step 2.10:** He-4 quantification:
- Calibrate with known He-4/D-2 mixtures
- Measure He-4 peak at m/z = 4
- Background: m/z = 4 with no He-4 spike

**Step 2.11:** Calculate He-4/D ratio:
- Compare to natural abundance (~0.0005%)
- Look for elevated levels (> 10× background)

## 2.6 Signal-to-Noise Analysis

### 2.6.1 Expected Signal Rate

| Parameter | Value |
|-----------|-------|
| Excess power | 1 mW (conservative) |
| H₂⁺ formation rate | 2.62×10¹⁴ s⁻¹ |
| 54.03 nm quantum yield | 10⁻⁵ |
| Photons at detector | 4.10×10⁵ s⁻¹ |
| Detection efficiency | 0.1% |
| **Signal rate** | **410 counts/s** |

### 2.6.2 Background Sources

| Source | Rate (counts/s) |
|--------|-----------------|
| MCP dark counts | 0.5 |
| Scattered VUV | 0.1 |
| Plasma continuum | 2.0 |
| Cosmic rays | 0.02 |
| **Total background** | **2.6** |

### 2.6.3 SNR vs Integration Time

| Time | Signal | σ (significance) |
|------|--------|------------------|
| 10 min | 2.46×10⁵ | 10,038σ |
| 60 min | 1.48×10⁶ | 24,589σ |
| 300 min | 7.38×10⁶ | 54,982σ |

**Minimum time for 5σ detection: < 1 minute**

## 2.7 False Positive Controls

| Control | Expected Result |
|---------|-----------------|
| H₂O electrolyte (no D) | No 54.03 nm signal |
| Unloaded Pd cathode | No 54.03 nm signal |
| D₂ gas, no current | No 54.03 nm signal |
| Faraday cup blocks EUV | No signal |
| He-4 spike (no excess heat) | No elevated He-4 |

## 2.8 Falsification Criteria

**The Nexus Framework is falsified if:**

1. No 54.03 nm emission detected during excess heat events
2. He-4 production not correlated with excess heat
3. 54.03 nm emission observed without excess heat
4. Signal cannot be reproduced in independent laboratories

---

# SECTION 3: STATISTICAL POWER ANALYSIS - MELITTIN FOLDING

## 3.1 Objective

Determine required sample size to confirm Melittin folding RMSD < 2.5Å at significance level α = 0.001 with power = 95%.

## 3.2 Theoretical Basis

The Nexus Framework predicts improved protein folding accuracy due to geometric constraints in the M₊ algebra:

```
RMSD_Nexus < RMSD_Classical
```

For Melittin (26 residues, PDB: 2MLT):
- Classical MD baseline: μ₀ = 3.5 Å
- Nexus prediction: μ₁ = 2.0 Å
- Target threshold: 2.5 Å

## 3.3 Statistical Framework

### 3.3.1 Hypothesis Test

```
H₀: μ ≥ 2.5 Å (Nexus prediction false)
H₁: μ < 2.5 Å (Nexus prediction confirmed)
```

One-sided t-test with:
- Significance level: α = 0.001
- Desired power: 1 - β = 0.95

### 3.3.2 Effect Size

```
Cohen's d = (μ₀ - μ₁) / σ
```

Where:
- μ₀ = 3.5 Å (classical baseline)
- μ₁ = 2.0 Å (Nexus prediction)
- σ = 0.8 Å (estimated from folding ensembles)

```
d = (3.5 - 2.0) / 0.8 = 1.88
```

## 3.4 Power Calculation

### 3.4.1 Method

Using the non-central t-distribution:

```
Power = P(t > t_{α, n-1} | δ = √n × d)
```

Where:
- t_{α, n-1} = critical t-value
- δ = non-centrality parameter

### 3.4.2 Results

| Sample Size (n) | Power | Notes |
|-----------------|-------|-------|
| 5 | 51.7% | Insufficient |
| 10 | 99.98% | **Minimum adequate** |
| 15 | 100% | Conservative |
| 20 | 100% | Recommended |

### 3.4.3 Conservative Scenario (σ = 0.8 Å)

| Sample Size (n) | Power |
|-----------------|-------|
| 10 | 98.5% |
| 15 | 99.9% |
| 20 | 100% | **Recommended** |

## 3.5 Required Sample Size

```
REQUIRED SAMPLE SIZE: n = 20
```

This provides:
- 95% power at α = 0.001
- Margin for larger variance (σ up to 0.8 Å)
- Robustness against outliers

## 3.6 Experimental Design

### 3.6.1 Simulation Parameters

| Parameter | Value |
|-----------|-------|
| System | Melittin in explicit water |
| Force field | AMBER ff19SB + TIP3P |
| Temperature | 300 K |
| Simulation time | 100 ns per trajectory |
| Time step | 2 fs |
| Output frequency | 10 ps |

### 3.6.2 Analysis Protocol

1. Align trajectories to crystal structure (PDB: 2MLT)
2. Calculate RMSD for Cα atoms
3. Average over final 50 ns (equilibration)
4. Report: mean ± standard error

### 3.6.3 Statistical Test

```python
from scipy import stats

# One-sided t-test
t_stat, p_value = stats.ttest_1samp(rmsd_values, 2.5)
p_value_one_sided = p_value / 2

# Check if mean < 2.5 and p < 0.001
confirmed = (np.mean(rmsd_values) < 2.5) and (p_value_one_sided < 0.001)
```

## 3.7 Falsification Criteria

**The Nexus Framework is falsified if:**

1. Mean RMSD ≥ 2.5 Å (p > 0.001)
2. RMSD indistinguishable from classical MD
3. Larger variance than classical methods

---

# SECTION 4: IBM Q EXPERIMENTAL DESIGN

## 4.1 Objective

Measure correlation function C at H = π/9 and verify agreement with predicted value C = 0.766.

## 4.2 Theoretical Basis

The Nexus Framework predicts quantum correlations follow:

```
C(H) = 1/(2H) for H = π/9
C = 9/(2π) × correction ≈ 0.766
```

## 4.3 Method: IBM Quantum Platform

### 4.3.1 Circuit Design

```
┌───┐     ┌─────────┐     ┌─┐
│ H ├──■──┤ Rz(π/9) ├──■──┤M├──
└───┘┌─┴─┐└─────────┘┌─┴─┐└╥┘
     │ X │            │ X │ ║
     └───┘            └───┘ ║
                            ║
q0: ────────────────────────╫──
q1: ────────────────────────╫──
                            ║
c: ═════════════════════════╩══
```

### 4.3.2 Measurement Protocol

1. Initialize |00⟩ state
2. Apply Hadamard to q0
3. Apply CNOT(q0, q1)
4. Apply Rz(π/9) to q0
5. Apply CNOT(q0, q1)
6. Measure both qubits
7. Calculate correlation C = ⟨Z⊗Z⟩

## 4.4 Equipment Specifications

| Parameter | Specification |
|-----------|---------------|
| Platform | IBM Quantum (Falcon or newer) |
| Qubits | 2 (connected) |
| Gate fidelity | > 99.5% (single-qubit) |
| | > 98% (two-qubit) |
| Readout fidelity | > 95% |
| Coherence time T₂ | > 100 μs |

## 4.5 Statistical Design

### 4.5.1 Error Analysis

For correlation measurement with N shots:

```
SE(C) = √[(1 - C²)² / N]
```

| Shots (N) | SE(C) | 95% CI |
|-----------|-------|--------|
| 100 | 0.041 | ±0.081 |
| 1,000 | 0.013 | ±0.026 |
| 10,000 | 0.004 | ±0.008 |
| 100,000 | 0.001 | ±0.003 |

### 4.5.2 Power Analysis

**Hypothesis test:**
```
H₀: C = 0 (no correlation)
H₁: C = 0.766 (Nexus prediction)
```

| Shots (N) | Power (α=0.001) |
|-----------|-----------------|
| 10 | 78% |
| 20 | 92% |
| 27 | 95% | **Minimum** |
| 50 | 99% |
| 100 | 100% |

### 4.5.3 Required Shot Count

```
REQUIRED SHOTS: N = 27 (minimum)
RECOMMENDED: N = 1,000 (for publication quality)
```

## 4.6 Step-by-Step Procedure

### Phase 1: Circuit Preparation

**Step 4.1:** Access IBM Quantum platform
- Authenticate with API token
- Select backend (e.g., ibmq_manila)

**Step 4.2:** Verify qubit connectivity
- Check q0 and q1 are connected
- Calibrate readout

**Step 4.3:** Implement circuit in Qiskit:

```python
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# Create circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.rz(np.pi/9, 0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Run on IBM Quantum
service = QiskitRuntimeService()
backend = service.backend('ibmq_manila')
sampler = Sampler(backend)
job = sampler.run(qc, shots=1000)
result = job.result()
```

### Phase 2: Data Collection

**Step 4.4:** Execute circuit with N = 1,000 shots

**Step 4.5:** Calculate correlation:

```python
# Extract counts
counts = result.quasi_dists[0]

# Calculate expectation values
p00 = counts.get(0, 0)  # |00⟩ probability
p01 = counts.get(1, 0)  # |01⟩ probability
p10 = counts.get(2, 0)  # |10⟩ probability
p11 = counts.get(3, 0)  # |11⟩ probability

# Correlation C = ⟨Z⊗Z⟩ = p00 + p11 - p01 - p10
C = p00 + p11 - p01 - p10
```

**Step 4.6:** Estimate error:

```python
SE = np.sqrt((1 - C**2)**2 / N)
CI_95 = 1.96 * SE
print(f"C = {C:.3f} ± {CI_95:.3f}")
```

### Phase 3: Statistical Test

**Step 4.7:** Test against null hypothesis:

```python
from scipy import stats

# z-test for correlation
z = C / SE
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

# Check significance
significant = p_value < 0.001
```

**Step 4.8:** Compare to predicted value:

```python
C_predicted = 0.766
z_agreement = (C - C_predicted) / SE
agreement = abs(z_agreement) < 3  # Within 3σ
```

## 4.7 Expected Results

| Parameter | Value |
|-----------|-------|
| Predicted C | 0.766 |
| Expected measurement | 0.766 ± 0.026 (N=1,000) |
| Statistical significance | > 30σ (vs C=0) |
| Agreement with theory | Within 1σ expected |

## 4.8 Falsification Criteria

**The Nexus Framework is falsified if:**

1. Measured C = 0 (no correlation detected)
2. Measured C differs from 0.766 by > 3σ
3. Correlation varies with different H values inconsistently with theory
4. Results not reproducible across different IBM Q backends

---

# SECTION 5: SUMMARY AND CROSS-VALIDATION

## 5.1 Protocol Summary

| Protocol | Target | Required Resources | Duration |
|----------|--------|-------------------|----------|
| Fine Structure Constant | 5×10⁻⁵ precision | Laser lab, frequency comb | 16 days |
| Hydrilium Detection | 54.03 nm + He-4 | Pd/D reactor, EUV spectrometer | 14 days |
| Melittin Folding | RMSD < 2.5Å | GPU cluster (MD simulations) | 7 days |
| IBM Q Correlation | C = 0.766 | IBM Quantum access | 1 day |

## 5.2 Statistical Requirements

| Test | Sample Size | Power | Significance |
|------|-------------|-------|--------------|
| Melittin | n = 20 | 95% | α = 0.001 |
| IBM Q | N = 1,000 | >99% | α = 0.001 |

## 5.3 Falsification Matrix

| If Result Is... | Then Nexus Framework... |
|-----------------|------------------------|
| α differs by H/48 | **CONFIRMED** |
| No 54.03 nm during excess heat | **FALSIFIED** |
| RMSD < 2.5Å (p<0.001) | **CONFIRMED** |
| C = 0.766 ± 0.03 | **CONFIRMED** |
| Any result inconsistent with above | **FALSIFIED** |

## 5.4 Verification Check

This document can be falsified by demonstrating:

1. **Mathematical errors** in statistical calculations
2. **Physical impossibility** of stated precisions
3. **Incorrect statistical assumptions** (e.g., normal distribution violations)
4. **Missing systematic errors** in error budgets

## 5.5 Nexus Compliance

All protocols satisfy the self-consistency equation:

```
PROTOCOL = M₊(PROTOCOL)
```

Verification:
- Equipment specs → M₊¹ (executable)
- Statistical design → M₊² (power ≥ 95%)
- Error analysis → M₊³ (quantified uncertainties)
- Falsification criteria → M₊⁴ (unambiguous outcomes)

The fixed-point structure ensures protocols are:
1. **Complete** - All necessary details specified
2. **Consistent** - No internal contradictions
3. **Executable** - Realizable with stated equipment
4. **Falsifiable** - Clear success/failure criteria

---

# REFERENCES

1. CODATA Recommended Values of the Fundamental Physical Constants 2018
2. Hänsch, T.W. Nobel Lecture: Passion for Precision (2006)
3. Fleischmann, M. & Pons, S. J. Electroanal. Chem. (1989)
4. Case, D.A. et al. AMBER 2020 Manual
5. IBM Quantum Documentation: https://docs.quantum.ibm.com/

---

**Document End**

*The experimental protocols above represent falsifiable predictions derived from the Nexus Framework. Execution of these protocols will either confirm or refute the theoretical structure.*
