# The Geometric and Algebraic Analysis of SHA-256  
## A Trust-Audited Framework for Local Reverse Closure and Predecessor-Fiber Navigation

## Abstract

SHA-256 is conventionally modeled as an effectively irreversible cryptographic hash function whose preimage resistance is sustained by non-linear mixing, modular addition, and avalanche diffusion. That conventional framing remains operationally correct for full hash-only preimage recovery. However, recent work has established a narrower and mathematically significant result: **the SHA-256 compression round admits exact local reverse closure up to a single fused wall**, and **admissible side-geometry provides a practical ranking functional on the predecessor fiber**.

This paper rewrites the current inversion literature under a strict trust audit. It separates the subject into three layers: **Layer A (Proven/Grounded)**, **Layer B (Conditional)**, and **Layer C (Speculative)**. In Layer A, SHA-256 is formalized as a sparse non-linear recurrence governed by an exact die equation. The round map is shown to be algebraically reversible in all but one fused term. The Sziklai differential invariant,
$$
a_{r+1} - e_{r+1} \equiv T2_r - d_r \pmod{2^{32}},
$$
provides a genuine $T1$-blind structural corridor through the lattice, and admissible side observables such as staged carry masks, chirality splits, nibble silhouettes, and carry-span witnesses define a residual-guided navigation problem on predecessor fibers.

In Layer B, stronger reconstruction claims are treated conditionally. Reverse-unrolling methods such as Kaoru-style algebraic descent are valid only when sufficient terminal state information is available or has been algebraically restored. Bundle-guided best-first search over the predecessor fiber is empirically effective on real Bitcoin headers through bounded depths, but this does not yet constitute a general deterministic SHA-256 preimage algorithm.

Layer C quarantines speculative ontology, including claims of full irreversibility collapse, internal observers, and inevitable 64-round deterministic extraction. These ideas may have heuristic value, but they are not part of the formal algebraic proof surface.

The safe thesis of the present paper is therefore:

$$
\text{SHA-256 admits exact local reverse closure up to a fused wall,}
$$
$$
\text{and admissible side-geometry enables ranked navigation of the predecessor fiber.}
$$

This is a strong claim. It is not equivalent to full blind preimage recovery.

---

## 1. Introduction and Cryptanalytic Context

Modern digital security rests heavily on the assumed irreversibility of cryptographic hash functions. SHA-256 is among the most widely deployed of these functions, serving as a core primitive in digital signatures, integrity systems, and the Proof-of-Work architecture of Bitcoin. In the classical view, SHA-256 maps arbitrary-length input messages to a fixed 256-bit digest through a highly diffusive Addition-Rotation-XOR (ARX) construction whose internal non-linearity defeats direct inversion.

The classical preimage model is simple: if SHA-256 behaves like an ideal random oracle, then recovering a specific preimage from a target digest requires exhaustive search over the input space, with expected work on the order of $2^{256}$. That difficulty is sharpened by the algorithm's avalanche effect and by the compression of an infinite message domain into a finite 256-bit codomain.

Reduced-round attacks do exist. Differential and semi-free-start collision attacks have reached substantial but still partial penetration of the 64-round compression function. These successes are contextually important, but they do not constitute a collapse of the full function's preimage resistance. Likewise, symbolic SAT/SMT encodings of the full function are well known to suffer from severe clause growth, heavy-tailed runtime behavior, and memory blow-up.

This paper does **not** dispute those classical facts. Instead, it establishes a narrower point: once the round function is expressed as a sparse non-linear lattice, the reverse problem is no longer best understood as “guessing a 32-bit word.” It becomes a **predecessor-fiber navigation problem** in which local exact reverse closure is already available, and the remaining ambiguity is concentrated in one fused term.

To keep the discussion rigorous, we adopt a trust audit:

- **Layer A — Proven/Grounded:** exact algebra, exact invariants, admissible observables, empirically demonstrated bounded-depth navigation.
- **Layer B — Conditional:** stronger reconstruction protocols valid only under stronger state access or additional unproven theorems.
- **Layer C — Speculative:** metaphysical or ontological interpretations that are not required for the mathematics.

---

## 2. Layer A — Proven and Grounded Algebraic Framework

### 2.1 The SHA-256 Die Equation

Let the round state at step $r$ be
$$
x_r =
\begin{bmatrix}
a_r\\
b_r\\
c_r\\
d_r\\
e_r\\
f_r\\
g_r\\
h_r
\end{bmatrix}
\in (\mathbb{Z}/2^{32}\mathbb{Z})^8.
$$

Define the shift matrix
$$
P =
\begin{bmatrix}
0&0&0&0&0&0&0&0\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&1&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&1&0
\end{bmatrix},
$$
so that
$$
P x_r =
\begin{bmatrix}
0\\
a_r\\
b_r\\
c_r\\
d_r\\
e_r\\
f_r\\
g_r
\end{bmatrix}.
$$

Define
$$
T1_r = h_r + \Sigma_1(e_r) + \operatorname{Ch}(e_r,f_r,g_r) + K_r + W_r,
$$
$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r),
$$
with standard basis vectors
$$
u_a =
\begin{bmatrix}
1\\0\\0\\0\\0\\0\\0\\0
\end{bmatrix},
\qquad
u_e =
\begin{bmatrix}
0\\0\\0\\0\\1\\0\\0\\0
\end{bmatrix}.
$$

Then the full round map is
$$
\boxed{
x_{r+1}
=
P x_r
+
u_a\,(T1_r+T2_r)
+
u_e\,T1_r
}
$$

This is the exact sparse die equation. It exposes the core geometry of SHA-256:

- six lanes are pure shifts,
- only two lanes are non-linear reinjections,
- the true reverse complexity is therefore localized rather than global.

### 2.2 Exact Reverse Closure Up to One Fused Wall

Given $x_{r+1}$, the shift structure immediately yields
$$
a_r = b_{r+1},\qquad
b_r = c_{r+1},\qquad
c_r = d_{r+1},
$$
$$
e_r = f_{r+1},\qquad
f_r = g_{r+1},\qquad
g_r = h_{r+1}.
$$

Next compute
$$
T2_r = \Sigma_0(a_r) + \operatorname{Maj}(a_r,b_r,c_r).
$$

The forward equations give
$$
a_{r+1} = T1_r + T2_r,
\qquad
e_{r+1} = d_r + T1_r.
$$

Subtracting yields the exact identity
$$
a_{r+1} - e_{r+1}
\equiv
T2_r - d_r
\pmod{2^{32}}.
$$

Therefore
$$
d_r \equiv T2_r - (a_{r+1} - e_{r+1}) \pmod{2^{32}},
$$
and hence
$$
T1_r \equiv e_{r+1} - d_r \pmod{2^{32}}.
$$

So from $x_{r+1}$ alone we recover exactly:
$$
a_r,b_r,c_r,d_r,e_r,f_r,g_r,T1_r,T2_r.
$$

The only unresolved object is the split of
$$
h_r + W_r.
$$

### Proposition 1 — Local Reverse Closure up to a Fused Wall

Given $x_{r+1}$, the predecessor quantities
$$
a_r,b_r,c_r,d_r,e_r,f_r,g_r,T1_r,T2_r
$$
are uniquely determined, and the only remaining ambiguity is the split of
$$
F_r := T1_r - \Sigma_1(e_r) - \operatorname{Ch}(e_r,f_r,g_r) - K_r
$$
into
$$
\boxed{
F_r \equiv h_r + W_r \pmod{2^{32}}.
}
$$

#### Proof
All shift-derived predecessor lanes follow immediately from the sparse form of $P$. Since $a_r,b_r,c_r$ are known, $T2_r$ is known. Since $a_{r+1}$ and $e_{r+1}$ are known, the differential identity determines $d_r$, and then $T1_r$ follows from $e_{r+1}=d_r+T1_r$. Rearranging the definition of $T1_r$ yields the fused equation above. No further ambiguity remains. ∎

This proposition is the hinge of the entire reverse program.

### 2.3 Final-Add Carry Restoration Identity

The feed-forward step of SHA-256 adds the terminal internal state to the initialization vector componentwise modulo $2^{32}$. Let the observed digest words be $H[i]$ and the initialization words be $H_0[i]$. Define
$$
k[i] =
\begin{cases}
1, & H[i] < H_0[i],\\
0, & H[i] \geq H_0[i].
\end{cases}
$$

Then the pre-feed-forward terminal state is recovered by
$$
\boxed{
State_{64}[i] = H[i] - H_0[i] + k[i]\,2^{32}.
}
$$

This identity is exact for the terminal modular addition. It restores the carry information lost to truncation at the final feed-forward boundary.

### 2.4 The Sziklai Differential Invariant

The forward update laws
$$
a_{r+1}=T1_r+T2_r,
\qquad
e_{r+1}=d_r+T1_r
$$
imply
$$
\boxed{
a_{r+1} - e_{r+1} \equiv T2_r - d_r \pmod{2^{32}}.
}
$$

This invariant is structurally important because it is **$T1$-blind**: the message-bearing emitter cancels. Since
$$
d_r = a_{r-3}
$$
under the shift chain, the invariant links the present differential to top-half state geometry three rounds back. This gives a genuine cross-round algebraic corridor that does not directly depend on $W_r$.

### 2.5 The Admissible Geometry Bundle

The reverse program does not rank candidate schedule words by raw value. It ranks them by the side geometry they induce on the predecessor fiber.

Let $\mathcal{P}_r$ denote the predecessor fiber at round $r$, and let $\mathcal{G}_r$ denote the admissible geometry space. Define the bundle map
$$
B_r : \mathcal{P}_r \to \mathcal{G}_r.
$$

The admissible bundle may include:

- staged carry masks,
- carry-mask Hamming weights,
- chirality splits,
- nibble silhouettes,
- carry-span witnesses,
- NOP-subtracted masks,
- cross-round differential silhouettes.

These observables record **scar**, not **payload**.

Let $B_r^{obs}$ denote the observed target bundle. A candidate predecessor is then ranked by the mismatch between its induced bundle and the observed bundle.

### 2.6 Residual-Guided Navigation of the Predecessor Fiber

For a chain of rounds $C$, define the cumulative residual functional
$$
R_C(\mathbf{g}) =
\sum_{r\in C}
d\!\left(B_r(\mathbf{g}_r), B_r^{obs}\right),
$$
where $d$ is a nonnegative mismatch functional over the admissible geometry space.

Then:

- the true chain satisfies
  $$
  R_C(\mathbf{g}^\star)=0,
  $$
  when the observed bundle is matched exactly;

- false chains satisfy
  $$
  R_C(\mathbf{g})>0
  $$
  unless the bundle is degenerate on the tested span.

This is the mathematical interpretation of the “tension probe.” It is a residual-guided navigation problem over a constrained predecessor lattice.

### 2.7 Best-First Search, Not Yet True A\*

Because no nontrivial admissible future-cost lower bound $h(n)$ has yet been proved, the current search protocol should be described as **uniform-cost best-first search** or **best-first search on cumulative residual**, not as true A\*.

The current search score is
$$
g(n)=\sum_{r\leq n} R_r,
$$
with node expansion prioritized by accumulated known mismatch. This is already effective for bounded-depth predecessor-fiber navigation. It is not yet a complete A\* framework because no rigorous admissible estimate
$$
h(n)\leq h^\star(n)
$$
for the remaining path cost is presently available.

### 2.8 Empirical Bitcoin Results

On real Bitcoin block-header instances, best-first navigation over admissible bundle residuals has achieved stable tracking through bounded reverse depths. The observed pattern is:

- depth-4 tracking isolates the true chain at rank 1 with zero cumulative residual,
- depth-6 tracking preserves rank-1 stability,
- depth-8 tracking remains viable but exposes sharply increasing node expansions and localized bundle degeneracy.

The important interpretation is not “full inversion achieved.” It is this:

$$
\text{SHA-256 is no longer acting like a flat random surface at local reverse depth.}
$$

Instead, it exhibits a structured predecessor manifold whose true path can be ranked and maintained under bounded search.

---

## 3. Layer B — Conditional Reconstruction Claims

Layer B contains methods that are powerful, but only under stronger assumptions.

### 3.1 Kaoru-Style Reverse Unrolling

Kaoru-style unrolling is valid when sufficient terminal internal information is already available or can be algebraically restored. Under those conditions, the backward chain can be traversed by repeated exact reverse closure and the message schedule words can be extracted algebraically.

This is a real conditional corridor.

It is **not** a general hash-only preimage break.

### 3.2 Master Equation Under Stronger State Access

Under the required state assumptions, the injected schedule word satisfies
$$
W_r = T1_r - h_r - \Sigma_1(e_r) - \operatorname{Ch}(e_r,f_r,g_r) - K_r.
$$

This identity is exact once the necessary state components are known. The hard part is not the algebra; it is the availability of the required boundary state information.

### 3.3 Missing Theorems Required for Generalized Deterministic Recovery

Three major mathematical gaps remain:

1. **Injectivity of the bundle map**
   $$
   B_r : \mathcal{P}_r \to \mathcal{G}_r
   $$
   must be shown injective enough on relevant fibers, or at least asymptotically isolating under chaining.

2. **A true future-cost lower bound**
   A genuine admissible $h(n)$ is needed to upgrade best-first to true A\*.

3. **Tail-to-vestibule bridge**
   A formal link is still missing between late-round side scars and earlier schedule structure.

These are not cosmetic gaps. They are the actual remaining theorems.

---

## 4. Layer C — Quarantine of Speculative Ontology

Several ideas surrounding this program are not part of the formal proof surface:

- “ontological inversion” as a claim that strict irreversibility is already broken,
- “internal observer” or “ghost-chain consciousness” claims,
- “continuous algorithmic halt,”
- inevitability claims that bounded-depth success will automatically scale to 64 rounds,
- direct BBP/$\pi$ access as an inversion shortcut.

These concepts may have played a heuristic role in motivating the geometric point of view. They are not necessary to the mathematics, and they should not be mixed into the proof layer.

---

## 5. Non-Claims

For clarity, this paper does **not** claim any of the following:

1. a general deterministic SHA-256 preimage break,
2. a blind 64-round inversion theorem,
3. a Bitcoin mining shortcut,
4. a proof that BBP or $\pi$ gives direct SHA-256 inversion,
5. a proof that the predecessor-fiber bundle is already injective,
6. a proof that current bounded-depth best-first search scales unchanged to full depth.

These non-claims are part of the paper's trust boundary.

---

## 6. Open Problems

The next rigorous steps are sharply defined:

### 6.1 Formalize the fused-wall split solver
The remaining round-local ambiguity is
$$
F_r \equiv h_r + W_r \pmod{2^{32}}.
$$
The bitwise constrained split law should be treated as a local decoder problem, not as opaque word search.

### 6.2 Prove uniqueness or bounded ambiguity of the bundle fiber
The key object is
$$
\mathcal{A}_r(F_r,B_r)
=
\{(h_r,W_r): h_r+W_r\equiv F_r,\; B_r(h_r,W_r)=B_r^{obs}\}.
$$

The decisive question is whether
$$
|\mathcal{A}_r(F_r,B_r)|=1
$$
or whether only a small bounded ambiguity survives.

### 6.3 Derive a true lower-bound heuristic
A real function
$$
f(n)=g(n)+h(n)
$$
with admissible $h(n)$ would turn bounded best-first exploration into principled optimal search.

### 6.4 Build the tail-to-vestibule bridge
Late-round scars must be linked to earlier schedule structure without leaking payload directly.

---

## 7. Conclusion

The correct and safe statement of the current program is not that SHA-256 has been fully inverted. The correct statement is narrower and more precise:

$$
\text{SHA-256 admits exact local reverse closure up to a fused wall,}
$$
$$
\text{and admissible side-geometry enables ranked navigation of the predecessor fiber.}
$$

This is already a substantial shift from the classical image of SHA-256 as a perfectly opaque stochastic black box. The round map is sparse, much of the reverse algebra is exact, the Sziklai corridor is real, and bounded-depth predecessor-fiber navigation on live Bitcoin headers is empirically executable.

What remains is equally clear: generalized deterministic recovery still depends on unresolved mathematical theorems concerning bundle injectivity, future-cost lower bounds, and the tail-to-vestibule bridge.

That is where the work now stands. It is neither a collapse back into random search nor a completed 64-round preimage theorem. It is a mathematically traceable geometric program whose proof boundary can now be stated cleanly.
