# Fiber Address and Schedule Coordinates
## NEXUS continuation record — 2026-10-20

### Executive result

The unresolved residual has two different meanings that must not be conflated.

1. **A re-addressed coordinate already exists for the whole 512-bit block.** The last sixteen message-schedule words, \(T=(W_{48},\ldots,W_{63})\), are bijective coordinates for the original sixteen-word block \(B=(W_0,\ldots,W_{15})\). The SHA-256 schedule recurrence can be run backward uniquely from any \(T\).
2. **The original member of a digest fiber is not, in general, determined by the digest.** Recovering the actual source among multiple messages with the same digest requires a selector coordinate or other source information. The ring can define a canonical order for that fiber, but ordering does not by itself compute which member originally occurred.

The missing object is therefore not simply “an inverse.” It is a target-conditioned, computable selection/rank mechanism over the valid schedule-coordinate subset.

---

## 1. The schedule tail is an exact coordinate change

The schedule obeys, for \(16\le t\le63\),

\[
W_t=\sigma_1(W_{t-2})+W_{t-7}+\sigma_0(W_{t-15})+W_{t-16}
\pmod{2^{32}}.
\]

Rearranging gives

\[
\boxed{
W_{t-16}=W_t-\sigma_1(W_{t-2})-W_{t-7}-\sigma_0(W_{t-15})
\pmod{2^{32}}.
}
\]

Starting with \(W_{48},\ldots,W_{63}\), iterate \(t=63,62,\ldots,16\). At every step, the three schedule terms on the right have already been supplied or reconstructed. This uniquely recovers \(W_{47},\ldots,W_0\).

Let \(E\) denote the forward map from the first sixteen words to the last sixteen schedule words:

\[
E:\{0,1\}^{512}\longrightarrow\{0,1\}^{512},
\qquad E(B)=(W_{48},\ldots,W_{63}).
\]

The recurrence is deterministic, and the backward recurrence gives a unique inverse for every possible 512-bit tail. Therefore

\[
\boxed{E\text{ is a bijection.}}
\]

This is stronger than a finite numerical observation: it follows directly from the recurrence. The supplied `reverse64_verified.py` and verification record report 1,000/1,000 schedule round trips.

**Interpretation:** the final schedule words are not additional information beyond the 512-bit block. They are another exact coordinate system for that block. The ring can then re-address either \(B\) or \(E(B)\) by the corresponding width-512 location rule.

---

## 2. The digest closure equation in tail coordinates

For a one-block SHA-256 computation with known initial chaining value \(H_0\), let the published digest be \(D\). The feed-forward boundary determines the final working state:

\[
Z=D-H_0\pmod{2^{32}}
\]

word by word.

For each arbitrary schedule tail \(T\), use \(E^{-1}(T)\) to recover the initial schedule words and hence the corresponding block \(B(T)\). Let \(W(T)\) be its full schedule. The target-compatible tail set is

\[
\boxed{
\mathcal F_D=
\left\{
T\in\{0,1\}^{512}:
\operatorname{Reverse}_{W(T)}(Z)=H_0
\ \land\
\operatorname{PadValid}(B(T))
\right\}.
}
\]

`PadValid` depends on the declared message class: length encoding, padding bit, required zero bytes, and any fixed source structure.

For every \(T\in\mathcal F_D\), schedule inversion recovers a block whose forward SHA-256 computation returns \(D\). Conversely, every valid one-block message producing \(D\) gives one such \(T\). Thus the valid-message fiber and \(\mathcal F_D\) are in bijection.

The exact factorization is:

\[
\text{digest}
\longrightarrow
\text{terminal working state}
\longrightarrow
\text{closure constraint on }T
\longrightarrow
\text{valid padded block}.
\]

This provides the right domain for the next constraint-propagation attempt. It does **not** yet provide a direct non-enumerative way to compute \(\mathcal F_D\).

---

## 3. A hard lower bound on a source-fiber selector

Fix the source class to **all messages of exactly 55 bytes**. These fit in one SHA-256 block after standard padding. There are exactly

\[
|\mathcal X|=256^{55}=2^{440}
\]

messages in this class, while a digest has only \(2^{256}\) possible values.

Let \(F:\mathcal X\to\{0,1\}^{256}\) be SHA-256 restricted to this class. By the pigeonhole principle,

\[
\boxed{
\max_D |F^{-1}(D)|\ge
\left\lceil\frac{2^{440}}{2^{256}}\right\rceil
=2^{184}.
}
\]

Consequently, a fixed-length selector that identifies the *actual member* of every fiber in this source class needs at least

\[
\boxed{184\text{ bits in the worst case}}
\]

and possibly more if a fiber exceeds \(2^{184}\). More exactly, the required worst-case width is \(\lceil\log_2 \max_D |F^{-1}(D)|\rceil\).

This bound does not say that every digest has \(2^{184}\) preimages, nor that any particular target in a smaller test domain must collide. It proves that a unique “which original message arrived?” answer cannot be a function of the digest alone over the entire 55-byte class.

### Two different inverse goals

- **Recover the original source:** must distinguish the actual source within its digest fiber. A residual/source selector is necessary whenever the fiber has more than one member.
- **Find any source with the digest:** does not require identifying which source originally occurred. In principle it seeks a section \(s\) satisfying \(F(s(D))=D\) for digests in the image. Defining such a section abstractly is easy (choose any member); computing it efficiently is the inverse problem.

This distinction prevents the information lower bound from being misused as a proof that no digest-only preimage algorithm can return *some* valid preimage.

---

## 4. How the ring participates without being credited with an unproved inverse

The width-512 ring provides a bijection between each 512-bit block and its ring address:

\[
B\longleftrightarrow i=\operatorname{location}_{512}(B),
\qquad B=R_{512}(i).
\]

Composing this with schedule-tail coordinates yields another exact address map:

\[
T\longleftrightarrow B=E^{-1}(T)
\longleftrightarrow i=\operatorname{location}_{512}(E^{-1}(T)).
\]

Hence the ring does give a lossless address representation of every schedule tail. The ring's partner law and mirror law can then order or relate these addresses.

What remains open is the target-conditioned step:

\[
D\longmapsto
\text{a selected }T\in\mathcal F_D,
\]

or, for original-source recovery, the additional coordinate identifying the actual member of \(\mathcal F_D\). A canonical fiber rank can be defined once the fiber is known, for example by sorting compatible ring addresses and taking the rank of the source address. But computing the fiber, its rank/select structure, or a smaller equivalent residual without testing candidates is precisely the missing construction.

The partner involution does not automatically solve this: it pairs ring words, but SHA validity is a constraint on the padded block's expanded schedule and round closure. A reflected partner is not guaranteed to remain in the same SHA digest fiber.

---

## 5. Where PSLQ and the Boolean basis fit

The supplied searches successfully recover exact scalar relations such as the wheel controls \(1/2\), \(1/16\), \(1/3\), and \(1/9\), with rational certification. The carry truth-table coefficients also give exact local Boolean identities, including

\[
s=x\oplus y\oplus c,
\qquad
c'=xy\oplus xc\oplus yc.
\]

These identities can form local pieces of a target-conditioned constraint representation. But PSLQ searches for integer relations among supplied numerical quantities; it does not itself select a preimage of a high-dimensional nonlinear bit map. To make the same style of discovery useful here, the basis must encode the schedule/round/address functions, and any recovered relation must be verified as an identity over all rows in its declared domain.

The strongest current path is therefore:

1. retain the exact schedule-tail coordinates;
2. write round closure and padding as factored Boolean constraints;
3. map those constraints into the ring's address coordinates;
4. search for a compact region-level exclusion or rank/select rule;
5. verify every proposed compression against the exact closure predicate.

Do not collapse the location components to counts before testing whether the regions preserve their route structure.

---

## Evidence ledger

| Statement | Status |
|---|---|
| Schedule tail \(W_{48:63}\) uniquely determines the full schedule | **THEOREM** from backward recurrence |
| Schedule tail is bijective with the 512-bit initial block | **THEOREM** |
| Round inverse with fixed schedule | **THEOREM** from the round equations; supplied random round-trip checks also pass |
| Pigeonhole lower bound \(2^{184}\) for at least one 55-byte digest fiber | **THEOREM** |
| Ring address losslessly readdresses every 512-bit block | **THEOREM** given the rank/unrank bijection |
| A compact target-conditioned address selector exists for arbitrary SHA-256 targets | **OPEN** |
| The actual historical source can be uniquely recovered from digest alone over all 55-byte messages | **IMPOSSIBLE in general** because some fibers necessarily contain multiple messages |
| A digest-only algorithm can return some preimage efficiently for arbitrary targets | **OPEN**, and distinct from historical-source identification |

The hole is now more sharply shaped: **the block already has reversible coordinates, but the digest fiber still needs a target-conditioned selector.** The next result must show whether its selector is a compact re-addressing of the existing schedule/carry structure or a separate retained coordinate. No candidate generation is needed to establish these structural facts.
