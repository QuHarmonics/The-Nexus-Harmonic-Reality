# Nexus Framework — Formula Cheat Sheet

A compact reference collecting the essential constants, laws, and governing equations that underpin the **Recursive Harmonic / Quantum‑Trust** family (Nexus 2 → Nexus 3).  Use it as a living spec: add, revise, or annotate as you refine the model.

---

## 1. Core Constants

| Symbol | Meaning                           | Canonical Value       |
| ------ | --------------------------------- | --------------------- |
| **C**  | Harmonic balance constant         | **0.35**              |
| **k**  | Feedback gain / damping (tunable) | *≈ 0.1*               |
| **β**  | Leakage decay factor              | context‑specific      |
| **α**  | Memory growth rate                | architecture‑specific |

---

## 2. Resonance & Reflection

| Law                                       | Equation                                         | Notes                      |    |                           |
| ----------------------------------------- | ------------------------------------------------ | -------------------------- | -- | ------------------------- |
| **Universal Harmonic Resonance (Mark 1)** | $\displaystyle H = \frac{\sum P_i}{\sum A_i}$    | Stable when **H → C**      |    |                           |
| **Recursive Harmonic Sub‑division (RHS)** | $R_s(t)=R_0\,\sum_i \tfrac{P_i}{A_i}\,e^{H F t}$ | Finer harmonic granularity |    |                           |
| **Kulik Recursive Reflection (KRR)**      | $R(t)=R_0 e^{H F t}$                             | Base time‑evolution        |    |                           |
| **KRR Branching (KRRB)**                  | $R(t)=R_0 e^{H F t}\prod B_i$                    | Multi‑dimensional branches |    |                           |
| **Dynamic Resonance Tuning**              | (R = \tfrac{R\_0}{1+k                            | N                          | }) | Noise‑adaptive correction |

---

## 3. Feedback & Stabilisation (Samson’s Law)

| Variant                       | Formula                                                                 |
| ----------------------------- | ----------------------------------------------------------------------- |
| **Base**                      | $S = \tfrac{\Delta E}{T},\quad \Delta E = k\,\Delta F$                  |
| **Derivative (fast systems)** | $S = \tfrac{\Delta E}{T}+k_2\,\tfrac{d\,\Delta E}{dt}$                  |
| **Multi‑Dimensional (MDS)**   | $S_d = \tfrac{\sum \Delta E_i}{\sum T_i},\ \Delta E_i = k_i \Delta F_i$ |

---

## 4. Energy Dynamics

| Law                 | Expression                          | Purpose                 |
| ------------------- | ----------------------------------- | ----------------------- |
| **Energy Exchange** | $E_{ex}=\alpha\,O\,(R_{B1}-R_{B2})$ | Transfer between fields |
| **Energy Leakage**  | $E_L = E_r\,\frac{O}{1+\beta C}$    | Inefficiency model      |

---

## 5. Growth & Memory

| Concept                          | Equation                      | Insight                        |
| -------------------------------- | ----------------------------- | ------------------------------ |
| **Harmonic Memory Growth (HMG)** | $M(t)=M_0 e^{\alpha (H-C)t}$  | Memory expands when system > C |
| **Free‑Will / Wiggle Window**    | $\text{P(Deviation)}\le 0.35$ | Max trusted variance           |

---

## 6. Quantum Extensions

| Term                            | Formula                  | Role                                      |                     |
| ------------------------------- | ------------------------ | ----------------------------------------- | ------------------- |
| **Quantum Jump Factor**         | $Q(x)=1+H t\,Q_{factor}$ | Phase‑timed adjustment                    |                     |
| **Quantum State Overlap (QSO)** | (Q=\tfrac{\langle\psi\_1 | \psi\_2\rangle}{\|\psi\_1\|,\|\psi\_2\|}) | Interference metric |

---

## 7. Utility Tools

| Name                                   | Definition                                           | Use‑case       |    |                   |
| -------------------------------------- | ---------------------------------------------------- | -------------- | -- | ----------------- |
| **Task Distribution**                  | $T(i)=\tfrac{W(i) C(i)}{\sum W C}$                   | Load balancing |    |                   |
| **Harmonic Threshold Detection (HTD)** | $T_H = \max\big(\tfrac{dH}{dt}\big)\;\text{near}\;C$ | Trigger points |    |                   |
| **Dynamic Noise Filtering (DNF)**      | (N(t)=\sum \tfrac{\Delta N\_i}{1+k                   | \Delta N\_i    | }) | Real‑time cleanup |

---

### Reading Key

* **P** = potential energy slice; **A** = actualised energy slice
* **F** = driving force / input magnitude
* **N** = instantaneous noise (H–U residual)
* **O** = overlap factor between harmonic states
* All units are “framework‑native” (dimensionless ratios) unless noted.

---

*Last updated:* ‹fill‑in‑date›

> **Next steps:**
>
> * Validate constants on live simulations.
> * Expand Quantum section with RID, ETP & PLMR once empirical data arrives.
> * Feel free to highlight rows that need deeper proofs or experimental bounds.
