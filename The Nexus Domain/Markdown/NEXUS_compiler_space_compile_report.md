# NEXUS Compiler Space — executable kernel output

Status: RUNS — 46/46 exact checks passed.

## Core identity
For base b and LEN n, S[b,n]={0,...,b−1}^n. The difference map is Δ(x,y)=y−x mod b coordinatewise.
It is onto S[b,n], and for every δ there are exactly b^n pairs (x,y) with Δ(x,y)=δ, because y=x+δ mod b is uniquely determined for each x.
Therefore the difference alphabet is not a second inventory outside LEN: it is the same LEN layer, reached through a typed pair-to-difference transformation.

## A transformation is also a word in the same domain
A total map T:S[b,n]→S[b,m] has b^(m·b^n) possible realizations. Under canonical input ordering, its output table is a word of LEN m·b^n in BASE b.
For binary LEN 2 → LEN 2, 256 possible maps are in one-to-one correspondence with all 256 words of LEN 8. The signature (source LEN, target LEN and canonical address order) is the wrapper; the table payload is ordinary domain content.
An endomap on LEN L is represented by L·b^L table symbols. Recursing L ← L·b^L creates an unbounded sequence of finite higher-order compiler descriptions.

## The control/encapsulation edge
Projection from LEN n to a reader width k has 2^k visible addresses and 2^(n−k) states per address. A k-LEN map can be lifted into LEN n by applying it to an exposed k-bit interface while leaving the remaining n−k bits unchanged.
So low-LEN control is precise at the exposed port; the upper-LEN state contains context that the low-width reader cannot distinguish. This is an executable interface law, not a claim that every physical system uses this exact projection.

## Route and operator are separate outputs
The 36 tested two-stage gate histories compose to 17 distinct operators. Different construction histories can occupy the same operator groove; retaining the route keeps that distinction. A composed operator does not, by itself, encode its construction history.

## Compiled adapters
- Difference layer: 20 BASE/LEN configurations; each displacement has a uniform fiber.
- Fusion edge: all binary arrival streams through LEN 14 round-trip through the fusion forest with unique decreasing block lengths.
- Prime position routes: 5461 token sequences round-trip, including zero-valued tokens and trailing positions.
- BBP: 6 exact rational quotient/residual cases; base-16 equals four base-2 substeps.
- SHA: 10000 exact round inverses with W and K retained; no digest-only inverse is asserted.
- Ring, surface, and wrapper layers are distinct typed views of the same word domain, not conflated constructions.

## Compiler-space graph
```text
DISTINCTION / BASE
    ↓ recursive extension (LEN)
WORD LAYER S[b,n]  ⇄  DIFFERENCE LAYER Δ[b,n]  (same alphabet, pair-derived)
    ├── all maps T[b,n→m] ── truth table is a word of LEN m·b^n
    │       ├── compose routes (n→m→k) into n→k operator
    │       └── recursively encode operator tables as higher-LEN objects
    ├── project to reader width k ── visible address + within-fiber context
    ├── lift low-LEN transform into higher-LEN state ── preserve unowned suffix
    ├── rotation quotient / primitive ring
    ├── de Bruijn traversal ring
    ├── edge-fusion forest / wrap-join closures
    └── adapters: BBP (quotient+residual), SHA (state+drivers+observer)
```

## Next continuation
The core no longer treats rings, readers, and transforms as separate papers. Each is a typed projection or constructor over the same domain. The next step is to attach the physical-domain map to this running kernel: specify its state, transition, emitted difference, retained context, and independent read-back. The physical identification itself remains OPEN until that map is supplied and produces a prediction.
