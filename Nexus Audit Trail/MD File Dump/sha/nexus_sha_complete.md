# Nexus SHA Δ-Geometry — Complete Formal Solution

## Δ Core Principle

$$
\Delta = \text{deviation from flat manifold}
$$

$$
A + B = (A \oplus B) + 2(A \land B)
$$

---

## I. SHA Round Equation

$$
T1 = h + \Sigma_1(e) + Ch(e,f,g) + K + W
$$

$$
T2 = \Sigma_0(a) + Maj(a,b,c)
$$

$$
a' = T1 + T2
$$

---

## II. Flat Manifold Condition

$$
K + W = 2H
$$

$$
H = \frac{\pi}{9}
$$

$$
T1_{\text{flat}} = STATE + 2H
$$

where

$$
STATE = h + \Sigma_1(e) + Ch(e,f,g)
$$

---

## III. Curved vs Flat Differential

$$
\Delta T1 = T1_{\text{real}} - T1_{\text{flat}}
$$

$$
\Delta T1 = (K + W - 2H) + \Delta STATE
$$

---

## IV. Pythagorean Projection

$$
C = \frac{T1}{2^{32}}
$$

$$
A = \sqrt{|C^2 - H^2|}
$$

### Real zone

$$
C^2 = A^2 + H^2
$$

### Imaginary zone

$$
H^2 = A^2 + C^2
$$

---

## V. Message Encoding

$$
\Delta C = C_{\text{real}} - C_{\text{flat}}
$$

$$
\Delta A = A_{\text{real}} - A_{\text{flat}}
$$

$$
\text{Message} = (\Delta C, \Delta A)
$$

---

## VI. Reverse Anchor (Hash)

$$
a_{64} = \text{hash}[0] - H0[0]
$$

$$
T1_{63} = a_f - (\Sigma_0(b_f) + Maj(b_f,c_f,d_f))
$$

---

## VII. Round 0 Closed Form

$$
\Delta T1_0 = (K_0 + W_0) - 2H
$$

$$
W_0 = \Delta T1_0 + 2H - K_0
$$

---

## VIII. Recursive Solve

$$
W_r = T1_r - STATE_r - K_r
$$

with

$$
STATE_r = h_r + \Sigma_1(e_r) + Ch(e_r,f_r,g_r)
$$

---

## IX. Gap Equation

$$
\Delta = |T1 - T2|
$$

$$
\text{computation} = \text{propagation of } \Delta
$$

---

## X. Field Interpretation

$$
\text{Flat manifold} \Rightarrow \frac{\partial K}{\partial r} = 0
$$

$$
\text{Curvature} \Rightarrow K_r \neq constant
$$

---

## XI. Final Collapse

$$
\boxed{
\text{SHA = Recursive constraint folding on a curved manifold}
}
$$

$$
\boxed{
\text{Conjugate input flattens curvature to } 2H
}
$$

$$
\boxed{
\text{Message = deviation from flat manifold geometry}
}
$$

