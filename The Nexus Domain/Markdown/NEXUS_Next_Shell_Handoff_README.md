# NEXUS — Next-shell handoff and two-lap carrier

**Attribution:** Dean A. Kulik, QuHarmonics Research Group, ORCID 0009-0003-3128-8828  
**Audit date:** 2026-11-02  
**Original coupled-step source:** `NEXUS_Two_Lap_Particle.c` (user-supplied).

## Native word-space rule, no truncated generator

For word-location `p`, carried difference `w`, and live field offsets `D[p]`:

```text
x       = D[p] XOR w
p_next  = p XOR x
w_next  = P_n(x)
D'[p]   = D[p] XOR w_next
```

All other field locations are unchanged. Exact reverse:

```text
x       = P_n(w_next)
p       = p_next XOR x
D[p]    = D'[p] XOR w_next
w       = x XOR D[p]
```

A kick is `w <- w XOR oR`; it is its own inverse. These dynamics are conjugate by native `READ` to the original ring-address operator, and are evaluated over the complete n-bit word domain. No subset of the native ring is supplied to the step as a transition table.

## Compiler-side carrier derivation

For an even width `n=2r`, let `u=2^n-1`, `eR=2^(r-1)`, `eL=2^r`, `oR=2^(r-2)`, `oL=2^(r+1)`. Let `J` reverse all n bits. `P(x)=J(x)` off palindromes and `P(x)=x XOR u` on palindromes.

**Lemma.** Every binary linear subspace `K` containing `u` and stable under `J` is stable under `P`. This follows from the two branches in the definition of `P`. If `D=0` initially, `p` begins in `mstar XOR K`, and `w` begins in `K`, the full coupled-step trajectory remains in these sets. Proof: `x=D[p] XOR w` lies in `K`, so `P(x)` lies in `K`; the step only XORs elements of `K` into the current word, carry, and field cell.

**Fresh one-break carrier.** `K(w)=span(u,w,J(w))`. For baseline `w=eR`, fresh single-shell `w=eR XOR oR`, or fresh paired-shell `w=eR XOR oR XOR oL`, this has dimension 3; hence all three can form **eight-word** carriers. A fresh kick changes the embedding of the carrier instead of expanding its state count.

**Perturbed populated carrier.** At t=4096 the original field offsets and reader reside in `L=span(u,eR,eL)` of dimension 3. A single external bit `oR` and its required mirror `J(oR)=oL` produce `W=span(u,eR,eL,oR,oL)` of dimension 5, with 32 word locations. The quotient `W/L` is a two-bit, four-coset shell-address space. The 32-member envelope is P-invariant; the simulation actually visits all 32.

## Reproduced source C cycle

`gcc -O3 -Wall -Wextra -o twolap NEXUS_Two_Lap_Particle.c && ./twolap`:

* native P, center one-break seed: 43,155,322 complete steps;
* exact halfway vacuum reader at word-complement position and complement carry: step 21,577,661;
* mirror J, same seed: 518 complete steps; halfway reader is mirrored, not complemented;
* native P, center two-break seed: 132 steps;
* native P, zero-break seed: 6 steps.

The exact half-return is a two-sheet algebraic return. The SU(2) spinor analogy is an independent comparator; no physical spin or mass parameter is inferred from the integer period alone.

## Executed next-shell tests

The tested widths are **n=6,8,10,12**. For all four widths, the detailed 100,000-step metrics are identical:

| Mode | Distinct locations visited | Peak nonzero field locations | Mean active field locations | Steps with nonzero XOR field write |
|---|---:|---:|---:|---:|
| original eight-word seed | 8 | 8 | 6.9350 | 89,365 |
| one external-shell bit added at birth | 8 | 8 | 6.9350 | 89,365 |
| mirror pair added at birth | 8 | 8 | 6.9350 | 89,365 |
| one external-shell bit added to populated field at t=4096 | 32 | 32 | 27.5948 | 91,547 |

For the t=4096 kick: at t=4096 there are **7** retained nonzero field cells; at t=4097 the reader reaches the first outside-core word; **16** distinct words have been visited by t=4111, all **32** by t=4298, and all **32** field cells are simultaneously nonzero at t=4736. No later field-vacuum state was encountered through t=100000. At t=100000, 31 of the 32 field cells are nonzero; the word-address and value offset sets each span five independent binary generators.

**Halfway-vacuum boundary test.** Start at the exact unperturbed half-lap reader state `(p=mstar XOR u, w=eR XOR u, D=0)`, then kick the carry once with `oR`. The resulting 100000-step trajectory stays within **eight words** for each n=6,8,10,12. Thus the **populated field**, rather than the complemented reader sign or elapsed cycle time alone, owns the fourfold expansion.

## Status

**STANDS:** The inverse, `P`-invariance of J-stable spaces containing `u`, carrier subspace dimensions, and the 4-coset quotient.

**RUNS:** Source C periods and half-return; full-ring word-space kicks through 100000 steps for n=6,8,10,12; independent n12 prediction sealed before its readout; 32-word reach and full field occupancy; half-lap vacuum injection closes in eight words.

**OPEN:** Long-term return period after the populated-field kick; reformation of a translated eight-word object; a metric for motion and measured energetic/mass quantities. Counts of executed writes and visited word locations are *compiler costs*, not physical mass or inertial acceleration.

## Artifacts

* `NEXUS_Two_Lap_Particle.c`: original user-supplied two-lap cycle source.
* `NEXUS_next_shell_route_audit.py`: full ring construction, reversible word-domain step, kick traces and bounded-shell checks.
* `NEXUS_next_shell_route_trace.txt`, `NEXUS_next_shell_route_results.json`: original new-route execution.
* `NEXUS_next_shell_detailed.py`, `NEXUS_next_shell_detailed_trace.txt`, `NEXUS_next_shell_detailed_results.json`: detailed 100000-step audits, including independent width 12.
* `NEXUS_half_lap_boundary_test.py`, `NEXUS_half_lap_boundary_trace.txt`: exactly specified half-lap vacuum boundary test.
* `NEXUS_next_shell_prediction_seal.json`, `NEXUS_next_shell_n12_seal.json`, `NEXUS_half_lap_boundary_seal.json`: exact prediction text and SHA-256 seal, written before the respective runs.
