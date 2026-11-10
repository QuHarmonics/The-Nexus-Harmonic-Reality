# Exact transition path: cell state to Walsh sectors

**Date:** 2026-10-10  
**Scope:** the 3-bit cell transformation `F(a,b,c)=(b⊕1,c⊕1,a⊕1)` and its induced action on readers. This certifies the local coordinate change; it does not yet encode the full 32-position SHA execution graph.

## 1. Keep the arrows distinct

There are three different maps:

1. **Pointwise sign encoding:** `a ↦ A=(-1)^a`, `b ↦ B=(-1)^b`, `c ↦ C=(-1)^c`. This is bijective on each bit. On reader outputs, `s(0)=+1`, `s(1)=-1`, so `s(u⊕v)=s(u)s(v)`.
2. **Walsh coordinate transform:** a reader truth table `f∈R^8` is sent to its eight coefficients `f̂(S)=(1/8)Σ_x f(x)χ_S(x)`. Retaining all eight coefficients is an invertible coordinate change; its inverse is `f(x)=Σ_S f̂(S)χ_S(x)`.
3. **Sector projection:** selecting only a subset of coefficients is a separate map and can discard information. A projection to the `ABC` coordinate is not the Walsh transform itself.

A single cell state does not by itself become a Walsh-sector coordinate. Walsh coordinates describe the eight-entry function/readout over all cell states.

## 2. State transition and pullback

Order states as

`(000,001,010,011,100,101,110,111)`.

Let `P[y,x]=1` iff `F(x)=y`. Then the state permutation satisfies `P⁶=I`; `F³(x)=x⊕111` for all eight states. A reader vector is pulled back by `f_next=Pᵀf`, so `f_next(x)=f(F(x))`.

Use Walsh basis order `(1,A,B,C,AB,AC,BC,ABC)`, and let `W` be the matrix mapping truth-table values to Walsh coefficients. The transition in Walsh coordinates is

`M = W Pᵀ W⁻¹`.

For the chosen row/column ordering, exact integer arithmetic yields

```text
[ 1  0  0  0  0  0  0  0]
[ 0  0  0 -1  0  0  0  0]
[ 0 -1  0  0  0  0  0  0]
[ 0  0 -1  0  0  0  0  0]
[ 0  0  0  0  0  1  0  0]
[ 0  0  0  0  0  0  1  0]
[ 0  0  0  0  1  0  0  0]
[ 0  0  0  0  0  0  0 -1]
```

This gives the reader pullbacks directly:

- `1 → 1`
- `A → −B`, `B → −C`, `C → −A`
- `AB → BC`, `BC → AC`, `AC → AB`
- `ABC → −ABC`

Thus the transformation is block-diagonal across the constant, degree-one, degree-two, and degree-three Walsh subspaces. It is still an invertible transformation: `M⁶=I`. Its third power is

`diag(1,−1,−1,−1,+1,+1,+1,−1)`,

which is exactly the reader action induced by complementing all three input bits.

## 3. Exact regression results

`verify_walsh_transition_path.py` uses integer matrices and rational elimination only. It verifies:

- `P⁶=I`;
- `F³` complements all three bits on all eight states;
- `M=W Pᵀ W⁻¹` equals the displayed matrix;
- `M⁶=I` and the stated diagonal form of `M³`;
- the parity, majority, and choice reader orbits have sizes `2, 8, 24`;
- all their transformed signed reader rows span exactly the seven-dimensional nonconstant subspace;
- all 256 Boolean functions form 22 orbits under the 24 affine rotation/XOR-mask maps.

Captured output: `WALSH_TRANSITION_PATH_run.txt`.

## 4. What this settles—and does not

The local path `cell truth table → signed reader → full Walsh coefficient vector → reader pullback` is now an exact commuting coordinate description. The encoding and complete Walsh transform lose no information. Information loss occurs only when a sector or subset of coefficients is deliberately selected.

This does not, by itself, map a whole SHA state to the cell machine. That lift must preserve each cell invocation's ordered source wires, each output destination, and each typed edge: spatial offsets for `Σ₀/Σ₁`, temporal lags for `Maj/Ch`, and the `carry_i → carry_{i+1}` handoff. The next object is therefore a typed execution graph plus an encoding that intertwines every source transition with its target path—not another endpoint statistic.
