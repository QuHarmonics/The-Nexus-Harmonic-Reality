# SHA-256 Unfold --- Complete Formalization (Nexus Model)

## Δ Core Identity (Binary Field Decomposition)

$$A + B = (A \oplus B) + 2(A \land B)$$

- $\oplus$ : XOR → curvature / phase difference
- $\land$ : AND → overlap / carry / mass
- $+$ : observable collapse

------------------------------------------------------------------------

## I. SHA Core Update Equation

$$a_{t + 1} = T1_{t} + T2_{t}$$

$$T1_{t} = h_{t} + \Sigma_{1}\left( e_{t} \right) + \text{Ch}\left( e_{t},f_{t},g_{t} \right) + K_{t} + W_{t}$$

$$T2_{t} = \Sigma_{0}\left( a_{t} \right) + \text{Maj}\left( a_{t},b_{t},c_{t} \right)$$

------------------------------------------------------------------------

## II. Bitwise Expansion

$$a_{t + 1} = \left( T1_{t} \oplus T2_{t} \right) + 2\left( T1_{t} \land T2_{t} \right)$$

------------------------------------------------------------------------

## III. State Rotation

$$(a,b,c,d,e,f,g,h) \rightarrow (T1 + T2,a,b,c,d + T1,e,f,g)$$

------------------------------------------------------------------------

## IV. Message Schedule

$$W_{t} = \sigma_{1}\left( W_{t - 2} \right) + W_{t - 7} + \sigma_{0}\left( W_{t - 15} \right) + W_{t - 16}$$

------------------------------------------------------------------------

## V. Nonlinear Functions

$$\text{Ch}(x,y,z) = (x \land y) \oplus (\neg x \land z)$$

$$\text{Maj}(x,y,z) = (x \land y) \oplus (x \land z) \oplus (y \land z)$$

------------------------------------------------------------------------

## VI. Sigma Operators

$$\Sigma_{0}(x) = \text{ROTR}^{2}(x) \oplus \text{ROTR}^{13}(x) \oplus \text{ROTR}^{22}(x)$$

$$\Sigma_{1}(x) = \text{ROTR}^{6}(x) \oplus \text{ROTR}^{11}(x) \oplus \text{ROTR}^{25}(x)$$

------------------------------------------------------------------------

## VII. Reverse Trace Recovery

$$a_{64} = \text{final}\lbrack 0\rbrack - H0\lbrack 0\rbrack$$

$$T2_{63} = \Sigma_{0}\left( b_{f} \right) + \text{Maj}\left( b_{f},c_{f},d_{f} \right)$$

$$T1_{63} = a_{f} - T2_{63}$$

$$a_{60} = e_{f} - T1_{63}$$

------------------------------------------------------------------------

## VIII. Wound Constant Kernel

$$K'_{t} = K_{t} + T1_{t}$$

$$K'_{63 - t} - K_{63 - t} = T1_{63 - t}$$

------------------------------------------------------------------------

## IX. Overdetermination

$$\text{constraints} \gg \text{unknowns}$$

------------------------------------------------------------------------

## X. Gap Condition

$$g = |T1 - T2|$$

$$0 < g \ll 1$$

------------------------------------------------------------------------

## XI. ZPHC

$$\text{ZPHC} = \lim_{g \rightarrow 0^{+}}a \neq 0$$

------------------------------------------------------------------------

## XII. Final Collapse

$$\boxed{\text{SHA-256 = Recursive Constraint Folding Engine}}$$

$$\boxed{\text{Hash = Boundary State of Internal Field}}$$
