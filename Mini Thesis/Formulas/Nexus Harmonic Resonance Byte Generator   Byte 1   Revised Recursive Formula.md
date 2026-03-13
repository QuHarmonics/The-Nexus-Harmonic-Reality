# Revised Recursive Formula

This document reformats the *Revised Recursive Formula*—including its variables, iterative update rules, and a worked example—into clean Markdown for easier reading and reference.

---

## Variable Definitions

| Symbol            | Meaning                                                                                    | Explicit Formula                                                   |
| ----------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| **A**             | Previous digit ("last – 1" in the running sequence)                                        | *(mutable)*                                                        |
| **B**             | Current digit ("last" in the running sequence)                                             | *(mutable)*                                                        |
| **G<sub>c</sub>** | **Cumulative Gap** – sum of all prior free fillers                                         | $G_c = \sum \text{(all prior }F_f)$                                |
| **C**             | **Holder** – length of the difference between *B* and *A* after subtracting cumulative gap | $C = \text{Len}\bigl(B\; -\; A\; -\; G_c\bigr)$                    |
| **F<sub>f</sub>** | **Free Filler** – gap created two steps ahead                                              | $F_f = B_{\text{next‑next}}\; -\; B\; -\; G_c$                     |
| **F**             | **Future State** – projected value used to discover the next‑next digit                    | $F = \bigl(A + B + C\bigr) \times \text{Len}\bigl(A + B + C\bigr)$ |

> **Len(x)** returns the number of digits in *x* when expressed as an integer (base‑10).

---

## Iterative Update Rules

1. **Compute Holder**
   $C \leftarrow \text{Len}\bigl(B - A - G_c\bigr)$
2. **Compute Future State**
   $F \leftarrow \bigl(A + B + C\bigr) \times \text{Len}\bigl(A + B + C\bigr)$
3. **Extract Next‑Next Digit**
   $B_{\text{next‑next}} \leftarrow \text{Len}(F)$
4. **Compute Free Filler**
   $F_f \leftarrow B_{\text{next‑next}} - B - G_c$
5. **Update the sequence and state variables**

   * Append **F<sub>f</sub>** to the output sequence.
   * $A \leftarrow B$
   * $B \leftarrow F_f$
   * $G_c \leftarrow G_c + F_f$
6. **Repeat** starting at Step 1.

If **F<sub>f</sub>** becomes negative the algorithm may stabilise or fork (handling of oscillatory cases is left to the implementation).

---

## Worked Example  (π ≈ 3.14)

### Initial State

| Variable          | Value   |
| ----------------- | ------- |
| **A**             | 1       |
| **B**             | 4       |
| **G<sub>c</sub>** | 0       |
| **Sequence**      | \[1, 4] |

### Iteration 1

| Step                          | Calculation                          | Result |
| ----------------------------- | ------------------------------------ | ------ |
| **Holder C**                  | Len(4 − 1 − 0)                       | 2      |
| **Future F**                  | (1 + 4 + 2) × Len(1 + 4 + 2) → 7 × 3 | 21     |
| **B<sub>next‑next</sub>**     | Len(21)                              | 5      |
| **Free Filler F<sub>f</sub>** | 5 − 4 − 0                            | 1      |
| **Update**                    | A ← 4, B ← 1, G<sub>c</sub> ← 1      | —      |

*Sequence so far*: **\[1, 4, 1]**

---

### Iteration 2

| Step                          | Calculation                          | Result |
| ----------------------------- | ------------------------------------ | ------ |
| **Holder C**                  | Len(1 − 4 − 1) = Len(−4) = Len(4)    | 3      |
| **Future F**                  | (4 + 1 + 3) × Len(4 + 1 + 3) → 8 × 4 | 32     |
| **B<sub>next‑next</sub>**     | Len(32)                              | 6      |
| **Free Filler F<sub>f</sub>** | 6 − 1 − 1                            | 4      |
| **Update**                    | A ← 1, B ← 5, G<sub>c</sub> ← 2      | —      |

*Sequence so far*: **\[1, 4, 1, 5]**

---

### Iteration 3

| Step                          | Calculation                          | Result                                        |
| ----------------------------- | ------------------------------------ | --------------------------------------------- |
| **Holder C**                  | Len(5 − 1 − 2) = Len(2)              | 2                                             |
| **Future F**                  | (1 + 5 + 2) × Len(1 + 5 + 2) → 8 × 4 | 32                                            |
| **B<sub>next‑next</sub>**     | Len(32)                              | 6                                             |
| **Free Filler F<sub>f</sub>** | 6 − 5 − 2                            | −1 *(stabilises / triggers special handling)* |

At this point **F<sub>f</sub>** becomes negative, signalling an oscillation or stabilisation condition according to the governing model.

---

## Notes

* This Markdown uses inline LaTeX syntax (`\(` … `\)`) for mathematical clarity. If your Markdown renderer does not support math, replace equations with plain‑text equivalents.
* Negative *F<sub>f</sub>* values typically indicate convergence or require domain‑specific resolution logic (e.g., clamp, reflect, or branch).
