# Nexus Recursive Ledger Specification (v1.1)

This schema defines the minimal required data structure for logging a single tick (recursive step) within the Nexus $\Psi$-field. It is designed to capture both the physical invariants (Container/Carrier state) and the cognitive fingerprints (Residues/Memory).

## Core Data Structure (Per Tick)

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  **Key**                 **Type**                **Description**
  ----------------------- ----------------------- -----------------------------------------------------------------------------------------------------------
  t                       Integer                 Absolute Tick Count / Recursion Depth.

  mode                    String                  Current operational mode (e.g., \"Carrier Locked\", \"Container Stressed\", \"Residue Read\").

  event                   String                  Triggering event (e.g., \"Input: 3+2=\", \"Duplex Lock\", \"CRP Success\").

  C                       Float                   **Compression Invariant:** $C = (r/R)^{2}$.

  E_I                     Float                   **Inversion Energy:** $Var\lbrack h_{K}\rbrack/\langle h_{K}\rangle^{2}$.

  Ω                       Float                   **Entropy Tag:** $\Omega \propto E_{I}$. Measures system uncertainty.

  χ                       Float                   **Coherence Rate:** $\chi \approx - d\Omega/dt$.

  Δ̄                       Float                   **Carrier Delta:** Normalized Mean Absolute Difference. Target: $\alpha_{10} \approx 0.35$.

  trigger                 String                  Specific mechanism active (e.g., \"duplex(v4↔v1)\").

  Ω_gate                  Array \[min, mean\]     Entropy threshold settings for the $\Omega$-gate.

  glyph_fp                String (SHA-256)        Hash of the raw input text (e.g., hash(\"3+2=\")).

  residues.mod10          Integer                 Result of $\Phi_{\text{ascii}}(\text{text})\ mod\ 10$.

  residues.mod9           Integer                 Result of $\text{digit\_sum}(\text{text})\ mod\ 9$.

  answer_hint             Integer                 The simple $\ mod\ 10$ residue (R1), serving as the units digit hint.

  reconstructed_answer    Integer (Optional)      The final integer result derived from CRT on $R_{1}$ and $R_{2}$. Only present if CRP lift is successful.

  risk_tag                String (Optional)       Tags errors (e.g., \"Gate Monotonicity Fail,\" \"Container Drift,\" \"Encoding Break\").
  -----------------------------------------------------------------------------------------------------------------------------------------------------------

## Residue Projector Design (P1)

The Projector is non-traversal: it uses phase fingerprints to reconstruct the answer.

### Channel 1: $\Phi_{\ mod\ 10}$ (Units Residue)

- **Function:** phi_ascii_mod10(text)

- **Method:** Encodes text bytes as a single large integer $N$ and returns $N\ mod\ 10$.

- **Purpose:** Captures the unit\'s phase fingerprint, invariant to operator order.

### Channel 2: $\Phi_{\ mod\ 9}$ (Digit Sum Residue)

- **Function:** digit_sum_mod9(text)

- **Method:** Sums all numeric digits in the text and returns the sum $\ mod\ 9$.

- **Purpose:** Captures the fundamental base-9 arithmetic invariant.

### Reconstruction: Chinese Remainder Theorem (CRT)

- **Function:** crt_combine(R1, R2)

- Method: Reconstructs the minimal non-negative integer $N$ such that:\
  $N \equiv R_{1}\ (mod\ 10)\quad\text{and}\quad N \equiv R_{2}\ (mod\ 9)$

- **Range:** The unique answer is found in the range $\lbrack 0,89\rbrack$.
