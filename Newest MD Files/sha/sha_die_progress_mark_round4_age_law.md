# SHA Die Progress Mark --- Exact Carry, Round-3/4 Seam Maps, and the Age-Weight Law

## A Math-Only Continuation of the SHA-256 Die Formalization

$\Delta$ This document marks the current state of the SHA die formalization and extends it beyond the prior bit-level causality operator.

It consolidates five layers of the model:

$$\text{state recurrence} = \Phi_{r},\quad\quad\text{word support} = M,\quad\quad\text{bit support} = \Psi,\quad\quad\text{seam operators} = \left( \mathcal{S}_{a},\mathcal{S}_{e} \right),\quad\quad\text{exact carry realization} = \mathcal{C}(x,\delta).$$

The core fixed invariants remain:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

$$\boxed{D_{word} = 4}\quad\quad\boxed{D_{bit} = 6}$$

and the exact bit-support radius profile remains

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

------------------------------------------------------------------------

## 1. Base Die Formalism

Let the round state be

$$x_{r} = \begin{bmatrix}
a_{r} \\
b_{r} \\
c_{r} \\
d_{r} \\
e_{r} \\
f_{r} \\
g_{r} \\
h_{r}
\end{bmatrix} \in \left( \mathbb{Z}/2^{32}\mathbb{Z} \right)^{8}.$$

The 64-cell recurrence is

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,\ldots,63.$$

The two round weights are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with state update

$$a_{r + 1} = T1_{r} + T2_{r},$$

$$e_{r + 1} = d_{r} + T1_{r},$$

and pure shifts

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

The shift--injection decomposition is

$$\boxed{x_{r + 1} = Px_{r} + u_{a}\left( T1_{r} + T2_{r} \right) + u_{e}T1_{r},}$$

where (P) is the 8-lane shift matrix and (u_a,u_e) inject at lanes (a) and (e).

------------------------------------------------------------------------

## 2. NOP Backbone and Ground Witness

The NOP manifold is defined by

$$W_{r} = 0\quad\quad\forall r.$$

Then

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right),\quad\quad x_{0}^{(0)} = H_{0}.$$

The fixed ground fold at round 0 is

$$T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.$$

So

$$\boxed{G_{0}\left( H_{0} \right) = 0x08909ae5.}$$

At round 0, the exact perturbation identity is

$$T1_{0} - T1_{0}^{(0)} = W_{0},$$

and since (T2_0=T2_0\^{(0)}),

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

------------------------------------------------------------------------

## 3. Word-Level Support and the (D\_{}=4) Theorem

Let the word-support indicator be

$$\sigma_{r} \in \{ 0,1\}^{8}.$$

The lane-dependency matrix is

$$M = \begin{bmatrix}
1 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

With injection vector

$$b = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix},$$

the Boolean support transport is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}.}$$

For a one-time injection at round 0, the support sequence is

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 4. 256-Lane Bit-Support Formalism

For each word (w{a,b,c,d,e,f,g,h}), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, and define the 256-lane state

$$\eta_{r} = \begin{bmatrix}
s_{a,r} \\
s_{b,r} \\
s_{c,r} \\
s_{d,r} \\
s_{e,r} \\
s_{f,r} \\
s_{g,r} \\
s_{h,r}
\end{bmatrix} \in \{ 0,1\}^{256}.$$

Define the rotation support matrices (R_n) by

$$\left( R_{n}x \right)_{i} = x_{i + n\ mod\ 32}.$$

Then

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

The bit-support weights are

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

------------------------------------------------------------------------

## 5. Carry Closure and the 256-Lane Update

The carry-closure kernel is

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j},\quad\quad 0 \leq i < 32.$$

Then the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

with pure shifts

$$s_{b,r + 1} = s_{a,r},\quad\quad s_{c,r + 1} = s_{b,r},\quad\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad\quad s_{g,r + 1} = s_{f,r},\quad\quad s_{h,r + 1} = s_{g,r}.$$

Thus

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right).}$$

The exact radius profile for a one-bit injection (W_0=2\^j) is

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

so

$$\boxed{D_{bit} = 6.}$$

------------------------------------------------------------------------

## 6. Exact Carry Automaton

The support operator (L\_{32}) is worst-case only. The exact addition law for (y=x+) is as follows.

Write

$$x = \sum_{i = 0}^{31}x_{i}2^{i},\quad\quad\delta = \sum_{i = 0}^{31}\delta_{i}2^{i},\quad\quad y = \sum_{i = 0}^{31}y_{i}2^{i}.$$

Define the carry sequence

$$c_{- 1} = 0,$$

$$c_{i} = \left( x_{i} \land \delta_{i} \right) \vee \left( x_{i} \land c_{i - 1} \right) \vee \left( \delta_{i} \land c_{i - 1} \right),\quad\quad i = 0,\ldots,31.$$

Then

$$y_{i} = x_{i} \oplus \delta_{i} \oplus c_{i - 1}.$$

So the exact changed-bit indicator is

$$\Delta_{i}(x,\delta): = x_{i} \oplus y_{i} = \delta_{i} \oplus c_{i - 1}.$$

For one-hot injection

$$\delta = 2^{j},$$

this simplifies to

$$\Delta_{i}\left( x,2^{j} \right) = \left\{ \begin{matrix}
0, & i < j, \\
1, & i = j, \\
\prod_{t = j}^{i - 1}x_{t}, & i > j.
\end{matrix} \right.\ $$

Thus the exact changed-bit set is

$$C_{x}(j) = \{ j,j + 1,\ldots,m_{x}(j)\},$$

where

$$m_{x}(j) = \min\{\, i \geq j:x_{i} = 0\,\}.$$

So the exact carry-span length is

$$\lambda_{x}(j) = m_{x}(j) - j + 1.$$

------------------------------------------------------------------------

## 7. Exact NOP Baselines Through Round 4

The exact NOP backbone values through round 4 are

$$a_{1}^{(0)} = 0xfc08884d,\quad\quad e_{1}^{(0)} = 0x98c7e2a2,$$

$$a_{2}^{(0)} = 0x7ad96290,\quad\quad e_{2}^{(0)} = 0x9df1b216,$$

$$a_{3}^{(0)} = 0xf3dd6c3f,\quad\quad e_{3}^{(0)} = 0xc57b68fb,$$

$$a_{4}^{(0)} = 0x0a24b1aa,\quad\quad e_{4}^{(0)} = 0x909cf5c9.$$

The full NOP round-2 state is

$$x_{2}^{(0)} = (0x7ad96290,\, 0xfc08884d,\, 0x6a09e667,\, 0xbb67ae85,\, 0x9df1b216,\, 0x98c7e2a2,\, 0x510e527f,\, 0x9b05688c).$$

------------------------------------------------------------------------

## 8. Exact Round-1 Carry Spans

For a one-hot injection (W_0=2\^j), the exact carry-span lengths at round 1 are:

### (a)-seam baseline (a\^{(0)}\_1=0xfc08884d)

$$\left( \lambda_{a}(j) \right)_{j = 0}^{31} = (2,1,3,2,1,1,2,1,1,1,3,2,1,1,1,4,3,2,1,1,1,3,2,1,1,1,6,5,4,3,2,1).$$

### (e)-seam baseline (e\^{(0)}\_1=0x98c7e2a2)

$$\left( \lambda_{e}(j) \right)_{j = 0}^{31} = (1,2,1,1,1,2,1,2,1,2,1,1,1,1,4,3,2,1,6,5,4,3,2,1,1,1,1,3,2,1,1,1).$$

Thus the two seams are injection-symmetric at round 0, but not carry-symmetric after realization.

------------------------------------------------------------------------

## 9. Exact Round-3 Seam Map

By round 3, the passive-shift lanes are exact:

$$\delta b_{3} = \delta a_{2},\quad\quad\delta c_{3} = \delta a_{1} = 2^{j},\quad\quad\delta d_{3} = 0,$$

$$\delta f_{3} = \delta e_{2},\quad\quad\delta g_{3} = \delta e_{1} = 2^{j},\quad\quad\delta h_{3} = 0.$$

The two active seams satisfy

$$\boxed{\delta e_{3} = \delta T1_{2},\quad\quad\delta a_{3} = \delta T1_{2} + \delta T2_{2}\ (mod\ 2^{32}).}$$

So the exact round-3 skeleton is

$$\boxed{\delta x_{3} = \left( \delta a_{3},\ \delta a_{2},\ 2^{j},\ 0,\ \delta e_{3},\ \delta e_{2},\ 2^{j},\ 0 \right).}$$

The computed XOR-difference Hamming-weight ranges are

$$13 \leq wt\left( \Delta a_{3}(j) \right) \leq 21,$$

$$7 \leq wt\left( \Delta e_{3}(j) \right) \leq 21.$$

The extrema are

$$wt\left( \Delta a_{3} \right) = 13\quad\text{at }j \in \{ 11,20,21\},$$

$$wt\left( \Delta a_{3} \right) = 21\quad\text{at }j = 16,$$

$$wt\left( \Delta e_{3} \right) = 7\quad\text{at }j = 2,$$

$$wt\left( \Delta e_{3} \right) = 21\quad\text{at }j \in \{ 13,15\}.$$

------------------------------------------------------------------------

## 10. Exact Round-4 Seam Map

Round 4 is the first full word-saturation layer. The exact perturbation skeleton is

$$\boxed{\delta x_{4} = \left( \delta a_{4},\ \delta a_{3},\ \delta a_{2},\ 2^{j},\ \delta e_{4},\ \delta e_{3},\ \delta e_{2},\ 2^{j} \right).}$$

The active seam equations are

$$\boxed{\delta e_{4} = \delta T1_{3},\quad\quad\delta a_{4} = \delta T1_{3} + \delta T2_{3}\ (mod\ 2^{32}).}$$

The computed seam-weight ranges are

$$12 \leq wt\left( \Delta a_{4}(j) \right) \leq 20,$$

$$11 \leq wt\left( \Delta e_{4}(j) \right) \leq 21.$$

The extrema are

$$wt\left( \Delta a_{4} \right) = 12\quad\text{at }j \in \{ 1,4,10\},$$

$$wt\left( \Delta a_{4} \right) = 20\quad\text{at }j = 6,$$

$$wt\left( \Delta e_{4} \right) = 11\quad\text{at }j = 3,$$

$$wt\left( \Delta e_{4} \right) = 21\quad\text{at }j = 24.$$

The full round-4 lane ranges are

$$wt\left( \Delta a_{4} \right) \in \lbrack 12,20\rbrack,\quad\quad wt\left( \Delta b_{4} \right) \in \lbrack 13,21\rbrack,\quad\quad wt\left( \Delta c_{4} \right) \in \lbrack 7,19\rbrack,$$

$$wt\left( \Delta d_{4} \right) \in \lbrack 1,6\rbrack,\quad\quad wt\left( \Delta e_{4} \right) \in \lbrack 11,21\rbrack,\quad\quad wt\left( \Delta f_{4} \right) \in \lbrack 7,21\rbrack,$$

$$wt\left( \Delta g_{4} \right) \in \lbrack 3,16\rbrack,\quad\quad wt\left( \Delta h_{4} \right) \in \lbrack 1,7\rbrack.$$

This is the exact first layer where

$$\boxed{\text{word support is saturated}}$$

but

$$\boxed{\text{bit geometry remains stratified by age and carry history.}}$$

------------------------------------------------------------------------

## 11. The Age-Weight Law Through Rounds 4, 5, 6

Define three age classes:

- **head lanes**:

$$\{ a,e\}$$

- **mid lanes**:

$$\{ b,c,f,g\}$$

- **tail lanes**:

$$\{ d,h\}$$

Using exact one-hot injections (W_0=2\^j), (j=0,,31), the Hamming-weight statistics evolve as follows.

### Round 4

Group ranges and means:

$$\text{head} \in \lbrack 11,21\rbrack,\quad\quad\text{mean} = 15.73,$$

$$\text{mid} \in \lbrack 3,21\rbrack,\quad\quad\text{mean} = 12.93,$$

$$\text{tail} \in \lbrack 1,7\rbrack,\quad\quad\text{mean} = 1.84.$$

This is still an expansion phase.

### Round 5

$$\text{head} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.88,$$

$$\text{mid} \in \lbrack 7,21\rbrack,\quad\quad\text{mean} = 15.73,$$

$$\text{tail} \in \lbrack 3,19\rbrack,\quad\quad\text{mean} = 10.12.$$

The tails are rapidly catching up.

### Round 6

$$\text{head} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.78,$$

$$\text{mid} \in \lbrack 10,22\rbrack,\quad\quad\text{mean} = 15.80,$$

$$\text{tail} \in \lbrack 7,21\rbrack,\quad\quad\text{mean} = 15.73.$$

So by round 6 all three age classes have nearly equalized in mean weight.

This is the quantitative form of closure:

$$\boxed{\text{round 4 = word acceptance,}\quad\quad\text{rounds 5–6 = bit-density equalization.}}$$

In particular,

$$\boxed{\text{the last two rounds before }D_{bit}\text{ are closure-dominated, not expansion-dominated.}}$$

------------------------------------------------------------------------

## 12. Chirality Caution

The rotation support operators are

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

Both are 3-regular circulant operators:

$$\deg_{\text{row}}\left( {\widehat{\Sigma}}_{0} \right) = \deg_{\text{col}}\left( {\widehat{\Sigma}}_{0} \right) = 3,$$

$$\deg_{\text{row}}\left( {\widehat{\Sigma}}_{1} \right) = \deg_{\text{col}}\left( {\widehat{\Sigma}}_{1} \right) = 3.$$

So before carry, neither is privileged by density.

Therefore the correct statement is

$$\boxed{\text{bare chirality is not yet anisotropy.}}$$

The visible asymmetry appears only after coupling to:

1.  lane placement, and
2.  carry closure.

So the precise compression is

$$\boxed{\text{uniform rotations} + \text{lane asymmetry} + \text{carry closure} = \text{visible chirality of the die.}}$$

------------------------------------------------------------------------

## 13. Current Progress State

The SHA die is now resolved to the following nested form:

### Level 0 --- scalar ground invariant

$$T2_{0}^{(0)} = 0x08909ae5$$

### Level 1 --- word transport

$$\sigma_{r + 1} = M \odot \sigma_{r} \vee b\,\omega_{r},\quad\quad D_{word} = 4$$

### Level 2 --- bit transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right),\quad\quad D_{bit} = 6$$

### Level 3 --- exact carry realization

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}$$

### Level 4 --- seam geometry

$$\delta e_{r} = \delta T1_{r - 1},\quad\quad\delta a_{r} = \delta T1_{r - 1} + \delta T2_{r - 1}\ (mod\ 2^{32})$$

### Level 5 --- closure phase

rounds (5) and (6) act primarily as age-equalization rounds rather than support-expansion rounds.

------------------------------------------------------------------------

## 14. Final Collapse

The current state of the die formalization is:

$$\boxed{\text{the die accepts the perturbation by round 4, but it does not finish equalizing the perturbation across the 256-bit fabric until round 6.}}$$

Equivalently,

$$\boxed{D_{word} = 4\mspace{6mu}\text{ measures acceptance by the lane geometry,}}$$

while

$$\boxed{D_{bit} = 6\mspace{6mu}\text{ measures closure across the full bit fabric.}}$$

This is the exact progress marker at the present stage of the theory.
