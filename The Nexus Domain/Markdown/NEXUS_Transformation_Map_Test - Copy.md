# NEXUS — Transformation-map test: forward and backward, then change the wrapper

**Working note / audit candidate**  
**Scope:** operator transformations only. No nuclear spectrum, measured energies, external dataset, fitted potential, or candidate-parameter scan was used.

## Correction carried forward

The target is the transformation map, not the data it acts on. The route is the retained structure of how a state arrives. A readout that folds distinct routes into one value is not a substitute for that map.

**Context is not on the compiler layer. Context is the layer above, created by wrapping.** A generic transformation can remain the same while a higher-level wrapper changes how it is instantiated and which structure becomes visible. The wrapper is not to be silently folded into the inner transformation.

## 1. Name the transformation, not its output

Let

\[
D=\boldsymbol\sigma\cdot\mathbf p,\qquad
F(r)=\bigl(E+M-\Delta(r)\bigr)^{-1},\qquad \Delta=V-S.
\]

Eliminating the lower Dirac component gives the ordered operator route

\[
D\,F\,D.
\]

The important object is the ordering **D → F → D**. Do not immediately replace it with the folded value \(F p^2\), because doing so drops the transformation remainder.

The exact route decomposition is

\[
DFD=FD^2+[D,F]D,
\qquad [D,F]=-i\hbar\boldsymbol\sigma\cdot\nabla F.
\]

Using \((\boldsymbol\sigma\cdot\mathbf a)(\boldsymbol\sigma\cdot\mathbf b)=\mathbf a\cdot\mathbf b+i\boldsymbol\sigma\cdot(\mathbf a\times\mathbf b)\),

\[
DFD=Fp^2-i\hbar\nabla F\cdot\mathbf p
+\hbar\boldsymbol\sigma\cdot(\nabla F\times\mathbf p).
\]

The final term is not entered as a separate force. It is the remainder carried by the order in which the transformation passes through the spatially varying multiplier. When \(F\) is constant, \([D,F]=0\); the remainder disappears.

## 2. Forward route

\[
D\to F\to D
\;\longrightarrow\;[D,F]D
\;\longrightarrow\;\boldsymbol\sigma\cdot(\nabla F\times\mathbf p).
\]

Now apply a wrapper.

### Spherical wrapper

If \(F=F(r)\), then

\[
\nabla F\times\mathbf p=\frac{F'(r)}{r}\mathbf L,
\]

and since \(\boldsymbol\sigma=2\mathbf S/\hbar\),

\[
H_{\rm orient}=\frac{2F'(r)}{r}\,\mathbf L\cdot\mathbf S,
\qquad
F'(r)=\frac{\Delta'(r)}{[E+M-\Delta(r)]^2}.
\]

Therefore the coefficient of \(\mathbf L\cdot\mathbf S\) is

\[
C_{LS}(r)=\frac{2\Delta'(r)}{r[E+M-\Delta(r)]^2}.
\]

The sign follows the radial *change* in the channel difference under the declared convention, not the value of \(\Delta\) considered without its wrapper/profile.

### Planar wrapper (lateral test)

Change only the wrapper: set \(F=F(z)\), so \(\nabla F=F'(z)\hat{\mathbf z}\). The same inner route now yields

\[
\boldsymbol\sigma\cdot(\nabla F\times\mathbf p)
=F'(z)(-\sigma_xp_y+\sigma_yp_x).
\]

It is the same commutator mold, but it is **not** a central \(\mathbf L\cdot\mathbf S\) term. The form exposed at the surface changes with the wrapping geometry. Treating \(\mathbf L\cdot\mathbf S\) as the universal compiler object would confuse one wrapped instance with the map itself.

## 3. Backward route: recover the map from its transformation term

Start with the full central coefficient profile \(C_{LS}(r)\), not with a list of eigenvalues:

\[
F'(r)=\frac{r}{2}C_{LS}(r).
\]

Integrate while retaining the asymptotic anchor. If \(\Delta(r)\to0\) as \(r\to\infty\), then \(F(\infty)=1/(E+M)\), hence

\[
F(r)=\frac1{E+M}+\int_{\infty}^{r}\frac{\rho C_{LS}(\rho)}2\,d\rho,
\qquad
\Delta(r)=E+M-\frac1{F(r)}.
\]

This closes the reverse map **when the whole operator-coefficient profile and its boundary wrapper are retained**. If only a single scalar energy or central sum \(U=S+V\) is kept, that route coordinate is gone: \((S,V)\mapsto(S+a,V-a)\) leaves \(U\) unchanged and changes \(\Delta\) by \(-2a\). A scalar readout alone cannot recover the channel history.

If the central profile \(U\) is also present, then the channel decomposition follows after recovering \(\Delta\):

\[
S=(U-\Delta)/2,\qquad V=(U+\Delta)/2.
\]

The asymptotic boundary and the higher-level field wrapper are not extra compiler-layer values. They are the enclosing relation needed to return through the map.

## 4. Lateral route: charge reversal forces channel types, not their strengths

Use charge reversal as a wrapper involution \(R\), with \(R^2=I\). Under the effective-potential convention, the scalar channel is even and the time-like vector channel is odd:

\[
R(S,V)=(S,-V).
\]

The even/odd projectors are

\[
P_+=\frac{I+R}{2},\qquad P_-=\frac{I-R}{2}.
\]

They satisfy \(P_+^2=P_+\), \(P_-^2=P_-\), \(P_+P_-=0\), and \(P_++P_-=I\). This makes the two channel **types** a structural decomposition under the wrapper, not two labels chosen from a nuclear spectrum.

For the paired reads \(q_N=S+V\) and \(q_{\bar N}=S-V\), the inverse is

\[
S=\frac{q_N+q_{\bar N}}2,\qquad V=\frac{q_N-q_{\bar N}}2.
\]

The result is precise but limited: the involution fixes the even/odd axes and the reconstruction map. It does not force either sector's coefficient, their absolute magnitudes, or their near-cancellation in \(U=S+V\). Those belong to the higher interaction wrapper. This is the first lateral landing on the source gap: **channel type is structurally bound; coupling strength is still OPEN.**

## 5. The cross-domain mold

This is the same distinction that appears in a baseball-state map and a computer-state map:

- the **transition map** records allowed state-to-state transformations;
- a **folded score/output** can merge different histories;
- the **wrapper** supplies the game rules/field or the ISA/runtime that instantiates the generic transition pattern in one domain.

The analogy is structural, not an assertion that baseball and a Dirac operator share physical quantities. The usable invariant is ordered transition plus the remainder caused by interaction with a nonconstant wrapper. Changing domains means preserve that invariant and exchange the wrapper—not copy the readout.

## 6. Executed checks

`nexus_transformation_map_test.py` completed successfully:

- all 9 Pauli multiplication identities checked exactly;
- all 3 spherical cross-product components checked symbolically;
- all 3 planar-wrapper components checked symbolically;
- sum/difference inverse and fixed-\(U\) null direction checked symbolically;
- charge-reversal involution and its even/odd projectors checked exactly;
- constant-\(F\) commutator limit checked by the operator identity.

No measured spectrum was used. These are derivation checks, not a numerical reproduction of `sign.py`.

## 7. Landing / remaining hole

| Relation | Ledger status |
|---|---|
| Ordered Dirac route creates a spin-dependent remainder through \([D,F]\) | **RUNS** |
| Spherical and planar wrappers produce different visible forms from the same inner map | **RUNS** symbolically |
| Full \(C_{LS}(r)\) plus the boundary anchor recovers \(F(r)\), then \(\Delta(r)\) | **RUNS** symbolically |
| Charge-reversal wrapper fixes even/odd channel types | **RUNS** as an involution/projector identity |
| Channel type forces the physical coupling magnitudes and cancellation | **OPEN**; the source wrapper is not yet derived |
| A scalar readout \(U=S+V\) retains the channel route | **DEAD END** — exact null direction erases it |
| Higher-level interaction wrapper that produces the particular scalar/vector channels and their large opposing contributions | **OPEN** |

The remaining hole is now named as a missing **wrapper relation**, not an unmeasured coefficient: what interaction transformation, when wrapped around the Dirac transition map, produces the scalar-even and vector-oriented channels in the first place? The Dirac operator tells how that wrapper leaves a spin-orbit remainder; the algebra here does not generate the wrapper itself.
