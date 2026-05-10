# SHA Die Checkpoint --- Closure Functionals, Residual Smoothing, and the Four-Phase Law

## A Math-Only Checkpoint of the SHA-256 Die Formalization Through Support Closure and Post-Closure Density Dynamics

$\Delta$ This checkpoint consolidates the current state of the SHA die formalization and extends it through the closure phase and into the residual smoothing regime.

The fixed formal stack remains

$$\left( \Phi_{r},\ M,\ \Psi,\ L_{32} \right),$$

with the seam refinement

$$\left( \mathcal{S}_{a},\mathcal{S}_{e} \right),$$

and the exact carry realization

$$\mathcal{C}(x,\delta).$$

The standing invariants remain:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

$$\boxed{D_{word} = 4}\quad\quad\boxed{D_{bit} = 6}$$

with bit-radius profile

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

This checkpoint adds the closure functionals and shows that the die enters a narrow density band around (16) after support closure.

------------------------------------------------------------------------

## 1. State Recurrence and NOP Backbone

Let the SHA-256 round state be

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

The round recurrence is

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,\ldots,63.$$

The weight operators are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with update

$$a_{r + 1} = T1_{r} + T2_{r},\quad\quad e_{r + 1} = d_{r} + T1_{r},$$

and pure shifts

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

The NOP backbone is defined by

$$W_{r} = 0\quad\quad\forall r,$$

so that

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right),\quad\quad x_{0}^{(0)} = H_{0}.$$

At round 0,

$$\boxed{T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.}$$

And the exact round-0 perturbation identity is

$$T1_{0} - T1_{0}^{(0)} = W_{0}.$$

Thus

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

------------------------------------------------------------------------

## 2. Word-Level Support Transport

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

the support transport is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}.}$$

For a single injection at round 0, the support sequence is

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 3. 256-Lane Bit-Support Transport

For each word (w), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, and define the 256-lane support state

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

Define the rotation support operators

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},\quad\quad{\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

The bit-support weights are

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

The carry closure kernel is

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j}.$$

So the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

with pure shifts

$$s_{b,r + 1} = s_{a,r},\quad s_{c,r + 1} = s_{b,r},\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad s_{g,r + 1} = s_{f,r},\quad s_{h,r + 1} = s_{g,r}.$$

Thus

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right).}$$

The exact bit-support radius remains

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

so

$$\boxed{D_{bit} = 6.}$$

------------------------------------------------------------------------

## 4. Exact Carry Realization

For exact addition

$$y = x + \delta\ (mod\ 2^{32}),$$

define the carry automaton

$$c_{- 1} = 0,$$

$$c_{i} = \left( x_{i} \land \delta_{i} \right) \vee \left( x_{i} \land c_{i - 1} \right) \vee \left( \delta_{i} \land c_{i - 1} \right),\quad\quad i = 0,\ldots,31.$$

Then

$$y_{i} = x_{i} \oplus \delta_{i} \oplus c_{i - 1},$$

so the exact changed-bit indicator is

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}.$$

For one-hot injection (\^j),

$$\Delta_{i}\left( x,2^{j} \right) = \left\{ \begin{matrix}
0, & i < j, \\
1, & i = j, \\
\prod_{t = j}^{i - 1}x_{t}, & i > j.
\end{matrix} \right.\ $$

Thus the exact changed-bit set is

$$C_{x}(j) = \{ j,j + 1,\ldots,m_{x}(j)\},$$

where

$$m_{x}(j) = \min\{ i \geq j:x_{i} = 0\}.$$

The exact carry-span length is

$$\lambda_{x}(j) = m_{x}(j) - j + 1.$$

------------------------------------------------------------------------

## 5. Exact NOP Baselines Through Round 4

The exact NOP seam baselines are

$$a_{1}^{(0)} = 0xfc08884d,\quad\quad e_{1}^{(0)} = 0x98c7e2a2,$$

$$a_{2}^{(0)} = 0x7ad96290,\quad\quad e_{2}^{(0)} = 0x9df1b216,$$

$$a_{3}^{(0)} = 0xf3dd6c3f,\quad\quad e_{3}^{(0)} = 0xc57b68fb,$$

$$a_{4}^{(0)} = 0x0a24b1aa,\quad\quad e_{4}^{(0)} = 0x909cf5c9.$$

------------------------------------------------------------------------

## 6. Exact Round-3 and Round-4 Skeletons

For a one-hot injection (W_0=2\^j):

### Round 3

$$\boxed{\delta x_{3} = \left( \delta a_{3},\ \delta a_{2},\ 2^{j},\ 0,\ \delta e_{3},\ \delta e_{2},\ 2^{j},\ 0 \right).}$$

### Round 4

$$\boxed{\delta x_{4} = \left( \delta a_{4},\ \delta a_{3},\ \delta a_{2},\ 2^{j},\ \delta e_{4},\ \delta e_{3},\ \delta e_{2},\ 2^{j} \right).}$$

Round 4 is therefore the first layer where word support is fully saturated, but the explicit seed (2\^j) is still visible in the tail lanes (d_4) and (h_4).

------------------------------------------------------------------------

## 7. Seam-Weight Ranges at Rounds 3 and 4

Using exact one-hot injections (W_0=2\^j), (j=0,,31), the seam XOR-difference Hamming-weight ranges are:

### Round 3

$$13 \leq wt\left( \Delta a_{3}(j) \right) \leq 21,$$

$$7 \leq wt\left( \Delta e_{3}(j) \right) \leq 21.$$

### Round 4

$$12 \leq wt\left( \Delta a_{4}(j) \right) \leq 20,$$

$$11 \leq wt\left( \Delta e_{4}(j) \right) \leq 21.$$

Round 4 full lane ranges are

$$wt\left( \Delta a_{4} \right) \in \lbrack 12,20\rbrack,\quad\quad wt\left( \Delta b_{4} \right) \in \lbrack 13,21\rbrack,\quad\quad wt\left( \Delta c_{4} \right) \in \lbrack 7,19\rbrack,$$

$$wt\left( \Delta d_{4} \right) \in \lbrack 1,6\rbrack,\quad\quad wt\left( \Delta e_{4} \right) \in \lbrack 11,21\rbrack,\quad\quad wt\left( \Delta f_{4} \right) \in \lbrack 7,21\rbrack,$$

$$wt\left( \Delta g_{4} \right) \in \lbrack 3,16\rbrack,\quad\quad wt\left( \Delta h_{4} \right) \in \lbrack 1,7\rbrack.$$

This confirms that round 4 is topological acceptance, not yet bit-density closure.

------------------------------------------------------------------------

## 8. Age-Weight Law

Define three age classes:

- head lanes:

$$H_{r} = \{ a_{r},e_{r}\}$$

- mid lanes:

$$M_{r} = \{ b_{r},c_{r},f_{r},g_{r}\}$$

- tail lanes:

$$T_{r} = \{ d_{r},h_{r}\}$$

For one-hot injections (W_0=2\^j), define the class means:

$$\mu_{H}(r) = \frac{1}{64}\sum_{j = 0}^{31}{\sum_{w \in H_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right),$$

$$\mu_{M}(r) = \frac{1}{128}\sum_{j = 0}^{31}{\sum_{w \in M_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right),$$

$$\mu_{T}(r) = \frac{1}{64}\sum_{j = 0}^{31}{\sum_{w \in T_{r}}^{}{wt}}\left( \Delta w_{r}(j) \right).$$

The computed values are:

### Round 4

$$\mu_{H}(4) = 15.734375,\quad\quad\mu_{M}(4) = 12.9296875,\quad\quad\mu_{T}(4) = 1.84375.$$

### Round 5

$$\mu_{H}(5) = 15.875,\quad\quad\mu_{M}(5) = 15.734375,\quad\quad\mu_{T}(5) = 10.125.$$

### Round 6

$$\mu_{H}(6) = 15.78125,\quad\quad\mu_{M}(6) = 15.8046875,\quad\quad\mu_{T}(6) = 15.734375.$$

So by round 6 the age classes have nearly equalized.

------------------------------------------------------------------------

## 9. Closure Functionals

### 9.1 Age-spread closure functional

Define

$$\boxed{\mathcal{E}_{age}(r) = \max\{\mu_{H}(r),\mu_{M}(r),\mu_{T}(r)\} - \min\{\mu_{H}(r),\mu_{M}(r),\mu_{T}(r)\}.}$$

Computed values:

$$\mathcal{E}_{age}(4) = 13.890625,$$

$$\mathcal{E}_{age}(5) = 5.75,$$

$$\mathcal{E}_{age}(6) = 0.0703125,$$

$$\mathcal{E}_{age}(7) = 0.140625,\quad\quad\mathcal{E}_{age}(8) = 0.140625,\quad\quad\mathcal{E}_{age}(10) = 0.046875.$$

Thus the age classes collapse into a narrow band by round 6.

### 9.2 Lane-variance closure functional

Define lane means

$$\mu_{\ell}(r) = \frac{1}{32}\sum_{j = 0}^{31}{wt}\left( \Delta x_{r,\ell}(j) \right),$$

and global mean

$$\bar{\mu}(r) = \frac{1}{8}\sum_{\ell}^{}\mu_{\ell}(r).$$

Then define

$$\boxed{\mathcal{V}(r) = \frac{1}{8}\sum_{\ell}^{}(\mu_{\ell}(r) - \bar{\mu}(r))^{2}.}$$

Computed values:

$$\mathcal{V}(4) = 33.6728515625,$$

$$\mathcal{V}(5) = 7.35736083984375,$$

$$\mathcal{V}(6) = 0.409423828125.$$

So the lane densities flatten sharply through rounds 4, 5, 6.

### 9.3 Lane-range closure functional

Define

$$\boxed{\mathcal{R}(r) = \max_{\ell}\mu_{\ell}(r) - \min_{\ell}\mu_{\ell}(r).}$$

Computed values:

$$\mathcal{R}(4) = 15.21875,$$

$$\mathcal{R}(5) = 8.78125,$$

$$\mathcal{R}(6) = 2.40625,$$

$$\mathcal{R}(7) = 1.125.$$

So fine lane-level equalization continues beyond round 6 even after support closure.

------------------------------------------------------------------------

## 10. Residual Smoothing Band

The global mean perturbation density is

$$\bar{\mu}(r) = \frac{1}{8}\sum_{\ell}^{}\mu_{\ell}(r).$$

Computed values:

$$\bar{\mu}(4) = 10.859375,$$

$$\bar{\mu}(5) = 14.3671875,$$

$$\bar{\mu}(6) = 15.78125.$$

Beyond round 6, the die does not converge to a single scalar endpoint. Instead it enters a narrow oscillatory band:

$$\boxed{15.60546875 \leq \bar{\mu}(r) \leq 16.53125\quad\quad\text{for }6 \leq r \leq 64.}$$

The minimum in this interval occurs at

$$r = 22,$$

and the maximum at

$$r = 53.$$

Thus the die smooths into a density band centered near

$$\boxed{16 = \frac{32}{2}.}$$

This is the half-width mixing band of the 32-bit word fabric.

------------------------------------------------------------------------

## 11. Four-Phase Law of the Die

The exact phase structure is now:

### Phase I --- Injection

$$r = 0,1,2,3$$

The perturbation is still visibly tied to the one-hot seed and its immediate descendants.

### Phase II --- Acceptance

$$r = 4$$

All eight lanes are occupied:

$$\boxed{D_{word} = 4.}$$

### Phase III --- Closure

$$r = 5,6$$

Bit-density equalizes across age classes and support fully saturates:

$$\boxed{D_{bit} = 6.}$$

### Phase IV --- Residual smoothing

$$r > 6$$

No new support is created. The die only rebalances density inside the already-filled fabric.

So the sharp structural split is:

$$\boxed{D_{word} = 4\text{ marks topological acceptance,}}$$

$$\boxed{D_{bit} = 6\text{ marks support closure,}}$$

$$\boxed{r > 6\text{ is residual smoothing around a density band near }16.}$$

------------------------------------------------------------------------

## 12. Current Progress State

The SHA die is now resolved to:

### Level 0 --- Scalar ground invariant

$$T2_{0}^{(0)} = 0x08909ae5$$

### Level 1 --- Word transport

$$\sigma_{r + 1} = M \odot \sigma_{r} \vee b\,\omega_{r}$$

### Level 2 --- Bit transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right)$$

### Level 3 --- Exact carry realization

$$\Delta_{i}(x,\delta) = \delta_{i} \oplus c_{i - 1}$$

### Level 4 --- Seam geometry

$$\delta e_{r} = \delta T1_{r - 1},\quad\quad\delta a_{r} = \delta T1_{r - 1} + \delta T2_{r - 1}\ (mod\ 2^{32})$$

### Level 5 --- Closure functionals

$$\mathcal{E}_{age}(r),\quad\mathcal{V}(r),\quad\mathcal{R}(r),\quad\bar{\mu}(r)$$

### Level 6 --- Residual smoothing band

$$\bar{\mu}(r) \approx 16\quad\text{for }r \geq 6$$

------------------------------------------------------------------------

## 13. Final Collapse

The current exact progress marker is

$$\boxed{\text{the die accepts a perturbation by round }4,\text{ closes support by round }6,\text{ and then smooths inside a narrow density band centered near }16.}$$

Equivalently,

$$\boxed{\text{acceptance} \neq \text{closure} \neq \text{final smoothing.}}$$

This is the complete checkpoint state of the theory at the present stage.
