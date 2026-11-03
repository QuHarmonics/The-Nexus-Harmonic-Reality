# SHA as a Die --- Bit-Level Causality Operator

## A Complete Math-Only Formalization of the 64-Cell SHA-256 Die, Word Support, and 256-Lane Intra-Word Causality

$\Delta$ This document formalizes the die interpretation of SHA-256 as a fixed 64-cell nonlinear recurrence over \[ (Z / 2^{32}Z)^8 \] with a message perturbation field written onto a pre-existing NOP backbone.

The focus is strictly mathematical:

- state recurrence,
- die decomposition,
- word-level support transport,
- bit-level support transport,
- carry-closure as the nonlocal intra-word kernel,
- exact support-radius results for a single perturbed bit of (W_0).

The two anchor facts are:

$$\boxed{T2_{0}^{(0)} = 0x08909ae5}$$

for the NOP backbone ground fold at round (0), and

$$\boxed{D_{bit} = 6}$$

for the worst-case 256-lane support diameter under the Boolean support model.

------------------------------------------------------------------------

## 1. State Space and Round Recurrence

Let the SHA-256 round state be the 8-word column vector

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

For one 512-bit block, the die executes a 64-step nonlinear recurrence

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right),\quad\quad r = 0,1,\ldots,63.$$

The round weights are

$$T1_{r} = h_{r} + \Sigma_{1}\left( e_{r} \right) + Ch\left( e_{r},f_{r},g_{r} \right) + K_{r} + W_{r},$$

$$T2_{r} = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with all arithmetic performed modulo (2\^{32}).

The state update is

$$a_{r + 1} = T1_{r} + T2_{r},$$

$$e_{r + 1} = d_{r} + T1_{r},$$

and the remaining registers shift:

$$b_{r + 1} = a_{r},\quad c_{r + 1} = b_{r},\quad d_{r + 1} = c_{r},$$

$$f_{r + 1} = e_{r},\quad g_{r + 1} = f_{r},\quad h_{r + 1} = g_{r}.$$

------------------------------------------------------------------------

## 2. The Sigma and Logic Operators

Define the right-rotation operator on 32-bit words:

$${ROTR}^{n}(x).$$

Then the SHA sigma operators are

$$\Sigma_{0}(x) = {ROTR}^{2}(x) \oplus {ROTR}^{13}(x) \oplus {ROTR}^{22}(x),$$

$$\Sigma_{1}(x) = {ROTR}^{6}(x) \oplus {ROTR}^{11}(x) \oplus {ROTR}^{25}(x).$$

The nonlinear Boolean gates are

$$Ch(e,f,g) = (e \land f) \oplus (\neg e \land g),$$

$$Maj(a,b,c) = (a \land b) \oplus (a \land c) \oplus (b \land c).$$

------------------------------------------------------------------------

## 3. Shift--Injection Decomposition of the Die

Define the (8) shift matrix

$$P = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}.$$

Let

$$u_{a} = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{bmatrix},\quad\quad u_{e} = \begin{bmatrix}
0 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}.$$

Then the full round map can be written as

$$\boxed{x_{r + 1} = Px_{r} + u_{a}\,\left( T1_{r} + T2_{r} \right) + u_{e}\, T1_{r}.}$$

This shows that each die cell is structurally sparse:

- six channels are pure register transport,
- only two channels ((a) and (e)) receive nonlinear reinjection.

------------------------------------------------------------------------

## 4. NOP Backbone and Ground Fold

Define the NOP manifold by setting the message field to zero:

$$W_{r} = 0\quad\quad\forall r.$$

Then the message-free backbone satisfies

$$x_{r + 1}^{(0)} = \Phi_{r}\left( x_{r}^{(0)},0 \right).$$

At round (0),

$$x_{0}^{(0)} = H_{0},$$

where (H_0) is the SHA-256 initialization vector.

The NOP ground fold is

$$T2_{0}^{(0)} = \Sigma_{0}\left( H_{0}\lbrack 0\rbrack \right) + Maj\left( H_{0}\lbrack 0\rbrack,H_{0}\lbrack 1\rbrack,H_{0}\lbrack 2\rbrack \right) = 0x08909ae5.$$

Thus the ground operator is

$$G_{r}\left( x_{r} \right) = \Sigma_{0}\left( a_{r} \right) + Maj\left( a_{r},b_{r},c_{r} \right),$$

with

$$\boxed{G_{0}\left( H_{0} \right) = 0x08909ae5.}$$

This is the fixed message-free floor of the first die cell.

------------------------------------------------------------------------

## 5. Round-0 Perturbation Identity

Let the real trajectory be

$$x_{r} = x_{r}^{(0)} + \delta x_{r}$$

in residue form modulo (2\^{32}).

At round (0), the perturbation obeys the exact identity

$$T1_{0} - T1_{0}^{(0)} = W_{0}.$$

Since

$$T2_{0} = T2_{0}^{(0)},$$

it follows immediately that

$$a_{1} - a_{1}^{(0)} = W_{0},$$

$$e_{1} - e_{1}^{(0)} = W_{0}.$$

Therefore the message enters only two words on the first step:

$$\boxed{\delta a_{1} = \delta e_{1} = W_{0}.}$$

At the word level, this gives the initial support vector

$$\Sigma_{1} = \{ a,e\}.$$

------------------------------------------------------------------------

## 6. Word-Level Support Dynamics

Let the word-support indicator be

$$\sigma_{r} \in \{ 0,1\}^{8},$$

where ((\_r)\_j=1) means word-lane (j) depends on the chosen perturbation.

The word-level dependency matrix is

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

The support update is

$$\boxed{\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}}$$

over the Boolean semiring, with injection vector

$$b = \begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}.$$

For a single perturbation injected only at round (0),

$$\omega_{0} = 1,\quad\quad\omega_{r} = 0\ \ (r > 0),$$

and

$$\sigma_{n} = M^{\lbrack n - 1\rbrack} \odot b.$$

The first four word-support layers are

$$\Sigma_{1} = \{ a,e\},$$

$$\Sigma_{2} = \{ a,b,e,f\},$$

$$\Sigma_{3} = \{ a,b,c,e,f,g\},$$

$$\Sigma_{4} = \{ a,b,c,d,e,f,g,h\}.$$

Hence the word support diameter is

$$\boxed{D_{word} = 4.}$$

------------------------------------------------------------------------

## 7. Explosion to 256 Lanes

Now refine from words to individual bits.

For each word (w{a,b,c,d,e,f,g,h}), let

$$s_{w,r} \in \{ 0,1\}^{32}$$

be its bit-support vector, with index (i=0) denoting the least significant bit.

Define the full 256-lane state

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

------------------------------------------------------------------------

## 8. Rotation Support Operators

Let (R_n) be the (32) rotation permutation matrix acting on bit-support vectors:

$$\left( R_{n}x \right)_{i} = x_{i + n\ mod\ 32}.$$

Then the Boolean support versions of the sigma operators are

$${\widehat{\Sigma}}_{0} = R_{2} \vee R_{13} \vee R_{22},$$

$${\widehat{\Sigma}}_{1} = R_{6} \vee R_{11} \vee R_{25}.$$

------------------------------------------------------------------------

## 9. Choice and Majority Support

Because () and () are same-bit Boolean operators, their support is simply the lane-wise union of their arguments:

$$supp\left( Ch(e,f,g) \right) = s_{e,r} \vee s_{f,r} \vee s_{g,r},$$

$$supp\left( Maj(a,b,c) \right) = s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

So the bit-support of the round weights is

$$\tau_{r}^{(1)} = s_{h,r} \vee {\widehat{\Sigma}}_{1}s_{e,r} \vee s_{e,r} \vee s_{f,r} \vee s_{g,r} \vee \omega_{r},$$

$$\tau_{r}^{(2)} = {\widehat{\Sigma}}_{0}s_{a,r} \vee s_{a,r} \vee s_{b,r} \vee s_{c,r}.$$

------------------------------------------------------------------------

## 10. Carry Closure as the Intra-Word Nonlocal Kernel

The only truly nonlocal intra-word mechanism is carry propagation.

Define the lower-triangular prefix operator

$$L_{32}(x)_{i} = \underset{j = 0}{\bigvee^{i}}x_{j},\quad\quad 0 \leq i < 32.$$

Equivalently, in matrix form,

$$L_{32} = \left( \ell_{ij} \right)_{0 \leq i,j < 32},\quad\quad\ell_{ij} = \left\{ \begin{matrix}
1, & j \leq i, \\
0, & j > i.
\end{matrix} \right.\ $$

This is the upward-carry support kernel: bit (i) of a sum can depend on any lower-or-equal bit because carry may ripple upward.

For support transport, use

$$supp(u + v) = L_{32}(u \vee v).$$

------------------------------------------------------------------------

## 11. The 256-Lane Intra-Word Causality Operator

With the support weights (\^{(1)}\_r,\^{(2)}*r) and the carry kernel (L*{32}), the 256-lane update is

$$s_{a,r + 1} = L_{32}\left( \tau_{r}^{(1)} \vee \tau_{r}^{(2)} \right),$$

$$s_{e,r + 1} = L_{32}\left( s_{d,r} \vee \tau_{r}^{(1)} \right),$$

and the six pure shifts are

$$s_{b,r + 1} = s_{a,r},\quad\quad s_{c,r + 1} = s_{b,r},\quad\quad s_{d,r + 1} = s_{c,r},$$

$$s_{f,r + 1} = s_{e,r},\quad\quad s_{g,r + 1} = s_{f,r},\quad\quad s_{h,r + 1} = s_{g,r}.$$

Thus the 256-lane die dynamics are

$$\boxed{\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right),}$$

where () is the piecewise Boolean-semiring map defined by the equations above.

------------------------------------------------------------------------

## 12. Single-Bit Injection Geometry

Let a single bit (j) of (W_0) be perturbed:

$$\omega_{0} = e_{j},\quad\quad\omega_{r} = 0\ \ (r > 0).$$

At round (1), because the perturbation enters only through (T1_0), we obtain

$$supp\left( a_{1} \right) = supp\left( e_{1} \right) = \{ j,j + 1,\ldots,31\}.$$

So a single bit at position (j) generates immediate first-step support of size

$$32 - j$$

in each of the two active words (a_1) and (e_1).

Thus low-order injected bits spread faster under the carry kernel than high-order injected bits.

------------------------------------------------------------------------

## 13. Bit-Support Radius

Define the bit-support radius for injected bit (j) as

$$\rho(j) = \min\left\{ r \geq 1:\text{all 256 state bits are in support by round }r \right\}.$$

Using the 256-lane Boolean support model above, the computed result is

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

So the three characteristic radii are

$$\boxed{\rho_{\min} = 4,\quad\quad\rho_{typ} = 5,\quad\quad\rho_{\max} = 6.}$$

This proves that a single perturbed bit of (W_0) reaches the full 256-lane state in at most six rounds under the support model.

------------------------------------------------------------------------

## 14. Support Diameters

At the word level, the perturbation reaches all eight words in four rounds:

$$\boxed{D_{word} = 4.}$$

At the bit level, the worst-case support diameter is larger because carry propagation is directional:

$$\boxed{D_{bit} = 6.}$$

The difference

$$D_{bit} - D_{word} = 2$$

is entirely due to intra-word carry geometry.

Word-lane reach saturates in four rounds, but high-order injected bits require two extra rounds before rotation plus carry closes the last untouched bit positions.

------------------------------------------------------------------------

## 15. Block-Operator View

Let the pure shift skeleton over 8 words be the (256) block matrix

$$\mathbb{P} = \begin{bmatrix}
0 & I & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & I & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & I & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & I & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & I & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & I & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix},$$

where each block is (32).

The (a)-injection block is

$$\mathbb{A} = \begin{bmatrix}
L_{32}\left( {\widehat{\Sigma}}_{0} \vee I \right) & L_{32}I & L_{32}I & 0 & L_{32}{\widehat{\Sigma}}_{1} & L_{32}I & L_{32}I & L_{32}I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix},$$

and the (e)-injection block is

$$\mathbb{E} = \begin{bmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & L_{32}I & L_{32}{\widehat{\Sigma}}_{1} & L_{32}I & L_{32}I & L_{32}I \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}.$$

If the message support vector is (\_r{0,1}\^{32}), then the message injection block is

$$\beta = \begin{bmatrix}
L_{32} \\
0 \\
0 \\
0 \\
L_{32} \\
0 \\
0 \\
0
\end{bmatrix}.$$

So the coarse block-support recurrence is

$$\boxed{\eta_{r + 1} = \left( \mathbb{P} \vee \mathbb{A} \vee \mathbb{E} \right) \odot \eta_{r}\mspace{6mu} \vee \mspace{6mu}\beta\,\omega_{r}.}$$

This is the 256-lane causality skeleton of the die.

------------------------------------------------------------------------

## 16. Three Nested Levels of the Die

The complete die now decomposes into three nested mathematical levels:

### 16.1 State recurrence

$$x_{r + 1} = \Phi_{r}\left( x_{r},W_{r} \right)$$

### 16.2 Word-support transport

$$\sigma_{r + 1} = M \odot \sigma_{r}\mspace{6mu} \vee \mspace{6mu} b\,\omega_{r}$$

### 16.3 Bit-support transport

$$\eta_{r + 1} = \Psi\left( \eta_{r},\omega_{r} \right)$$

with the carry kernel

$$L_{32}$$

as the nonlocal intra-word closure operator.

This can be summarized as

$$\boxed{\text{state dynamics} = \Phi_{r},\quad\quad\text{word support dynamics} = M,\quad\quad\text{bit support dynamics} = \Psi,\quad\quad\text{carry closure} = L_{32}.}$$

------------------------------------------------------------------------

## 17. Final Collapse

The SHA-256 die is a fixed 64-cell recursive lattice over ((Z/2^{32}Z)^8) with a message-free NOP ground and a variable displacement field.

Its first fixed ground witness is

$$\boxed{T2_{0}^{(0)} = 0x08909ae5.}$$

Its word-level support saturates in

$$\boxed{D_{word} = 4}$$

rounds.

Its bit-level support saturates in

$$\boxed{D_{bit} = 6}$$

rounds.

And for a single injected bit (j) of (W_0),

$$\boxed{\rho(j) = \left\{ \begin{matrix}
4, & j = 0, \\
5, & 1 \leq j \leq 25, \\
6, & 26 \leq j \leq 31.
\end{matrix} \right.\ }$$

The die therefore has a mathematically sharp causality structure:

- sparse at the state-update level,
- dense at the support level,
- and carry-limited at the bit-closure level.

This is the complete current solution state for the bit-level causality operator of the SHA die.
