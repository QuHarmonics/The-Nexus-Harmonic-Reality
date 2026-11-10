# §107 candidate — The groove is the fiber of composition; unique operator data is a normal form

**Attribution:** Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828  
**Scope:** exact finite algebra, not a physical dataset. No hash was used for route or operator encoding.

## Hole

A route must drive a payload without being selected by that payload. It must also be possible to distinguish (a) route history, (b) the composed transformation, and (c) a readout/value produced after a lossy projection. The question is not “what value did we observe?” but “what transformation record uniquely names the action, and what route record preserves its factorization?”

## Typed model

Let the typed state space be \(X=(\mathbb Z/8\mathbb Z)^3\), with lanes \((a,b,c)\). Fix six reversible primitive transformations before supplying any state:

- `A+B`: \((a,b,c)\mapsto(a+b,b,c)\)
- `A-B`: \((a,b,c)\mapsto(a-b,b,c)\)
- `B+C`: \((a,b,c)\mapsto(a,b+c,c)\)
- `B-C`: \((a,b,c)\mapsto(a,b-c,c)\)
- `SWAP_AB`: \((a,b,c)\mapsto(b,a,c)\)
- `NEG_C`: \((a,b,c)\mapsto(a,b,-c)\)

All arithmetic is modulo 8. A route is an ordered word in these fixed tokens. The input never selects the route. The same word acts on every input state.

## The algebraic split

Let \(\Sigma^*\) be the set of all finite route words and let \(\pi(w)\) be the operator obtained by composing the route. Define

\[
w\sim v\quad\Longleftrightarrow\quad \pi(w)=\pi(v).
\]

This is the **groove relation**: two route histories occupy the same groove exactly when they induce the same transformation. It is a congruence: if \(w\sim v\), then \(u w z\sim u v z\) for any surrounding routes \(u,z\), since composing equal operators on either side preserves equality. The groove is the equivalence class (fiber) under \(\pi\), not a payload value.

The route code and operator code therefore have different jobs:

- **Route record (`NXRT` candidate):** typed primitive-vocabulary version plus the ordered token word. This retains factorization/history.
- **Operator record (`NXOP` candidate):** domain type plus a canonical normal form for the composed action. For this affine test, \(T(x)=Mx+c\) is encoded by the exact matrix \(M\) and offset \(c\) over \(\mathbb Z/8\mathbb Z\).

The affine record is unique in its declared coordinate system: \(c=T(0)\), and each column of \(M\) is \(T(e_i)-T(0)\) modulo 8. That construction specifies the transformation and does not depend on which payload later passes through it. Checking the operator against all states is validation of the representation, not the source from which the route was encoded.

Different route words can share one `NXOP` and still have distinct `NXRT` records. Conversely, two different outputs can occur under one fixed route; that does not make the route data-dependent.

## Run

Enumerated all words of lengths 0–4 over the six primitives. There are \(1+6+6^2+6^3+6^4=1555\) routes. All \(512\) states of \(X\) were used to verify the composed affine operator.

| Test | Result |
|---|---:|
| Ordered routes | 1,555 |
| Unique route words | 1,555 |
| Distinct canonical operator records | 446 |
| Distinct operators after extensional comparison on all 512 states | 446 |
| Operators failing bijectivity | 0 |
| Route/canonical-operator mismatches | 0 |
| Route-inverse failures | 0 |
| Primitive frame-rule failures | 0 |
| Groove classes with multiple route histories | 200 |
| Route histories beyond one representative per groove | 1,109 |
| Largest observed groove | 83 routes |

The count 1,109 is \(1555-446\): histories beyond one representative in each operator class. It is not a count of lost payload states. Those are different fibers and must not be conflated.

## Matter collision versus logic collision

**Matter/value collision:**

\[
(3,2,5)\xrightarrow{A+B}(5,2,5),\qquad
(4,1,5)\xrightarrow{A+B}(5,1,5).
\]

The projection that keeps only the first output reports 5 for both inputs. The full states are different, and `A+B` is bijective because the carried second lane restores the inverse \(a=s-b\). The collision was introduced by the projection, not by the route.

**Logic/groove collision:** the empty route and `A+B;A-B` have distinct route codes but compose to the identity operator. They are different factorizations in the same groove. The route record can retain the histories; the operator record intentionally identifies their shared action.

## “Whatever changes is what gets changed” — footprint law

For `A+B`, the read set is \(\{a,b\}\), the write footprint is \(\{a\}\), and lanes \(b,c\) are framed (unchanged). For `A+B;NEG_C`, the exact write footprint is \(\{a,c\}\); lane \(b\) remains unchanged. Its output dependencies are \(a'\leftarrow(a,b)\), \(b'\leftarrow b\), and \(c'\leftarrow c\). These declarations belong to the transformation definition; they are not inferred from a particular payload.

For an arbitrary reversible update of a target lane, a clean sufficient pattern is to retain every required control/carry lane and apply a bijection on the target conditional on the retained controls. A transformation that actually merges full states cannot be made reversible merely by naming its output differently; the missing distinguishing route/state must be preserved somewhere in the declared state/interface.

## Ledger landing

- Unique ordered route encoding relative to the declared token vocabulary: **RUNS**.
- Unique operator encoding as \((\text{typed domain},M,c)\) for this affine family: **RUNS**.
- Groove as the fiber of route composition: **RUNS** by construction and tested witnesses.
- Value-only collisions can occur after projection even when the full transformation is reversible: **RUNS**.
- Frame preservation for the six primitives and tested compositions: **RUNS**.
- Full NEXUS verbs `MARK`, `COMPARE`, `CARRY`, `HOLD`, `ROUTE`, `CLOSE`: **OPEN**. They still need typed interfaces, read/write footprints, inverse/way-home semantics, and explicit rewrite/equivalence rules. The six affine test operators are witnesses, not a substitute grammar.
- Context: remains a higher wrapper; it is not silently encoded into the compiler-layer route or operator.

## Reproducibility

Run `python nexus_groove_route_law.py`. Exact output is in `nexus_groove_route_law_results.json` and `nexus_groove_route_law_run.txt`. No SHA, hash, data-derived route selection, or external dataset is used.
