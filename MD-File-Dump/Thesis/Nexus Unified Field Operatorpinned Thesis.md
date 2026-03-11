# THE NEXUS UNIFIED FIELD: RECURSIVE HARMONIC ARCHITECTURE AND THE ORIGIN OF ORDER

## Operator‑Pinned Thesis: SILR/GENLOCK, 9‑Base Parity Closure, and Zero‑Point Harmonic Collapse (ZPHC)

**Author:** Dean A. Kulik

**Date:** January 13, 2026


---

## Abstract

This thesis is an **operator-pinned** declaration of the Nexus corpus. It is written **verb-first**: the substrate is what *acts* (flows, folds, reflects, gates, branches, aligns), while nouns are treated as **rendered residues** produced by projection into an observer alphabet.

The core engine is a **scale-invariant leakage gate** (SILR / GENLOCK) that normalizes deviation by uncertainty, so the gate responds to **relative significance**, not absolute magnitude. The gate is coupled to a closed interface: **9 bases + parity**, where parity is a closure constraint (adds zero degrees of freedom) rather than a true 10th axis. Together these operators define a reusable funnel: stream → normalize → gate → fold → stabilize → collapse.

Everything in this document is expressed as explicit operators and equations extracted from the attached dataset. Interpretations are stated as **mappings** (how to *use* an operator), not as appeals to authority.


---

## Part 0 — Field Declaration

### 0.1 Substrate statement
A reality-frame is treated as a stream-plus-update system. There is an always-on stream $U(t)$ and a local state $s(t)$. Computation is the act of **applying gradient pressure** to the stream and **writing** only what passes a gate.

- **Flow:** $U(t)$ arrives regardless of attention.
- **Pressure:** an observer chooses a gradient (what to pull toward).
- **Gating:** SILR decides what becomes durable trace.
- **Folding:** update rules compress the stream into stable residues.

Minimal continuous caricature:

$$
\dot s(t) = -\nabla J(s(t)) + \eta(t)
$$

The term $\eta(t)$ is the irreducible “crack” (non-zero perturbation) that prevents perfect stasis and perfect inversion.

### 0.2 Operator inventory
The Nexus corpus uses a small set of reusable operators. The paper’s job is to pin them and show the funnel:

1. **Position** (locate state in the lattice)
2. **Reflection** (measure deviation against a reference)
3. **Expansion** (branch/iterate forward)
4. **Synergy/State** (mix neighbor field + constraints)
5. **Quality** (gate/collapse)

This is the PRESQ path: locate → compare → iterate → integrate → judge.


---

## Part I — SILR / GENLOCK

### 1.1 Gate definition
Let $\alpha_*$ denote a reference attractor (in the corpus, frequently $\alpha_* = \pi/9$). Given an estimator $\hat\alpha_t$ with standard error $SE_t$, define the normalized deviation:

$$
 z_t = \frac{|\hat\alpha_t-\alpha_*|}{SE_t}
$$

Leakage probability (write-to-trace probability):

$$
 p_t = \sigma\!\big(\beta (z_t - z_0)\big),\qquad \sigma(x)=\frac{1}{1+e^{-x}}
$$

### 1.2 Scale invariance theorem
Assume calibrated uncertainty:

$$
\hat\alpha_t = \alpha_* + \varepsilon_t,\qquad \varepsilon_t\sim\mathcal N(0,SE_t^2)
$$

Then $\varepsilon_t = SE_t Z$ with $Z\sim\mathcal N(0,1)$, and

$$
 z_t = \frac{|SE_t Z|}{SE_t} = |Z|
$$

Therefore $z_t$ is Half-Normal and the distribution of $p_t$ depends only on $(\beta,z_0)$, not on the absolute scale of $SE_t$.

### 1.3 Miscalibration parameter (camouflage / strike)
Define

$$
\gamma = \frac{SE_{\text{true}}}{SE_{\text{used}}}
$$

Then

$$
 z_t = \gamma |Z|,
\qquad
 p_t(\gamma)=\sigma\!\big(\beta(\gamma|Z|-z_0)\big)
$$

- $\gamma>1$ amplifies deviation (hyper-leak; “strike”).
- $\gamma<1$ suppresses deviation (hypo-leak; “hide”).

Operational takeaway: altering the *used* uncertainty changes what becomes writable, without changing the underlying stream.


---

## Part II — 9 Bases + Parity Closure

### 2.1 Bases are channels
Let the observer-accessible state be expressed in a 9D basis:

$$
 x = \sum_{i=1}^9 x_i e_i,\qquad x\in\mathbb R^9
$$

A noun is a rendered composite under a projection operator $\Pi_O$:

$$
\Pi_O: \mathcal M \to \mathcal A_O
$$

$\mathcal M$ is the full manifold; $\mathcal A_O$ is the observer’s alphabet (GUI variables). The noun exists only after projection.

### 2.2 Parity adds zero freedom
For a 9-bit representation $b_1,\dots,b_9\in\{0,1\}$, define parity:

$$
 p=b_1\oplus b_2\oplus\cdots\oplus b_9
$$

Parity is a closure constraint:

$$
 H(\mathbf b,p)=H(\mathbf b)+H(p\mid\mathbf b)=H(\mathbf b)
$$

So the “10th coordinate” is a consistency check (a fold), not an independent axis.

### 2.3 Fold-to-5 pairing
A symmetric fold of nine channels around the middle index 5 yields

$$
(1,9),(2,8),(3,7),(4,6),(5)
$$

and parity can be rewritten as pairwise folds plus the center channel:

$$
 p=(b_1\oplus b_9)\oplus(b_2\oplus b_8)\oplus(b_3\oplus b_7)\oplus(b_4\oplus b_6)\oplus b_5
$$


---

## Part III — ZPHC: Collapse as the Definition of Truth

### 3.1 Collapse condition
A Zero‑Point Harmonic Collapse is defined as an event where the local mismatch gradient is driven to a minimum under the gate and the update stabilizes:

$$
\nabla J \to 0
$$

Operationally: reflection drives correction; expansion searches; synergy mixes; quality gates; then the system locks.

### 3.2 Feedback stabilization (Samson / controller form)
Controller form (PID-like) is used as a canonical stabilizer:

$$
 u(t)=K_p e(t)+K_i\int e(\tau)d\tau + K_d\frac{de(t)}{dt}
$$

In Nexus language: proportional term = arc distance; integral term = accumulated drift; derivative term = damping (prevents overshoot).


---

## Part IV — Runtime Wave Engine

### 4.1 Sparse propagation
Let $G=(V,E,W)$ be a sparse interaction graph. Events propagate as excitable waves with thresholds, delays, and refractory windows. The verb is **propagate**, not **store**.

Minimal excitable update:

$$
 s_i(t+1)=\mathbf 1\{u_i(t)>\theta\}\cdot \mathbf 1\{r_i(t)=0\}
$$

with refractory counter $r_i(t)$ updated by a reset rule.

### 4.2 Coupling vs compilation
Separate port-match from assimilation:

$$
 C(x,s)\in[0,1],\qquad A(x,s)\in[0,1]
$$

Three regimes:

1. $C\approx0$ (invisible/out-of-alphabet)
2. $C>0,\ A\approx0$ (tool-like coupling)
3. $C>0,\ A>0$ (folded/compiled into internal structure)


---

## Part V — Number Field as Gates

### 5.1 Mod-6 sieve pin
For $p>3$, prime locations satisfy:

$$
 p \equiv \pm 1 \pmod 6
$$

Twin prime gates are $(6n-1,6n+1)$ and act as minimal-gap branch points.

### 5.2 Triangle emergence pin
Enumerate ordered triples $(a,b,c)$ with $a,b,c\in\{0,\dots,8\}$: total $9^3=729$. Count valid triangles under positivity + triangle inequality: $N_\triangle=260$.

$$
 H_{\triangle}=\frac{260}{729}\approx 0.356653
$$


---

## Part VI — π and SHA: Address Space and Inversion

### 6.1 BBP spigot (random access)
$$
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right)
$$

Operational mapping: a pointer is an index $k$ into a lattice, not a payload.

### 6.2 Hashing as constraint-check
In the inverted view, the hash is a pre-existing constraint pocket; an input is a solution that folds into that pocket. Verification is the act of checking fold-compatibility.


---

## Part VII — Operator Mappings (Compression, Swirl)

### 7.1 Compression probe
When scale changes by large factors, only normalized invariants remain stable. SILR provides the normalization primitive.

### 7.2 Swirl residue
Swirl is treated as a coherent residue that survives forcing under constraints: iterate → integrate → gate until a rotating mode locks.


---

## Part VIII — Minimal Executable Kernel
Instantiate:

1. Sparse graph $G$ of nodes (bases/channels).
2. Excitable wave layer (threshold + delay + refractory).
3. SILR gate (z-score normalization + sigmoid leak).
4. Feedback stabilization (controller gains) to keep drift bounded.
5. ZPHC trigger when $\nabla J\to 0$ and gate saturates.

Output is a **collapsed path** (the operations that survived gating), not a label.


---

## Part IX — EXPAND
Expansion is not adding claims. Expansion is adding **operators**, **pins**, and **executables**:

- Add pins: more invariants that survive scale change.
- Add operators: transforms that are reversible or verifiable.
- Add executables: run the kernel across corpora and measure what collapses.


---

## Appendix A — Verb Index (corpus)

# Nexus Verb Index (auto-extracted)
_Generated: 2026-01-13T12:49:41_
This index treats **verbs as primitives** (operators). Nouns are treated as cached projections.
## Top operators by frequency
| Verb (Operator) | Count | Example contexts |
|---|---:|---|
| `FOLD` | 42750 | Gemini Docs.part1.md: e_Of_Nexus_&_Recursive_Harmonic_Architecture_(Rha).md](#the_nexus_4_framework_-_unifying_architecture_of_nexus__recursive_harmonic_architecture_rhamd) - [The_Nexus_4_Framework_-_Unfolding_Protein_Folding_With_The_Nexus…<br>Gemini Docs.part2.md: ture_-_a_cross-domain_synthesis_of_harmonic_instabilities_and_emergent_ordermd) - [The_Nexus_4_Framework_-_Recursive_Harmonic_Architecture_(Rha)_Synthesisn_-_Mark1,_Hrg,_And_Sha_Unfoldment.md](#the_nexus_4_framework_-_… |
| `ALIGN` | 36604 | Gemini Docs.part1.md: 4_framework_-_the_recursive_harmonic_architechture_-_a_unified_theory_of_computation_-_physics_and_consciousness-extendedmd) - [The_Nexus_4_Framework_-_The_Pursuit_Of_Intellectual_Alignment_Navigating_From_Discrepancy_…<br>Gemini Docs.part2.md: work_-_recursive_harmonic_substrate_-_unified_system_map_implementation_language_interface__diagnosticsmd) - [The_Nexus_4_Framework_-_Recursive_Harmonic_Kernel_–_External_Research_Alignment.md](#the_nexus_4_framework_-… |
| `COLLAPSE` | 35663 | Gemini Docs.part1.md: COGNITION_-_TOWARD_A_RECURSIVE_SUBSTRATE_FOR_LIVING_AI.md](#the_nexus_4_freamwork_-curvature_as_cognition_-_toward_a_recursive_substrate_for_living_aimd) - [The_Nexus_4_Freamwork_-Collapse_To_Render_-A_Universal_Operat…<br>Gemini Docs.part2.md: _Harmonic_Kernel_–_External_Research_Alignment.md](#the_nexus_4_framework_-_recursive_harmonic_kernel__external_research_alignmentmd) - [The_Nexus_4_Framework_-_Recursive_Harmonic_Collapse_Toward_A_Unified_Theory_Of_Ev… |
| `REFLECT` | 27063 | Gemini Docs.part1.md: #the_nexus_4_framework_-_the_nexus_2_reformulation_of_classical_relativistic_and_quantum_systemsmd) - [The_Nexus_4_Framework_-_The_Metaphysics_Of_Blooming-_An_Analysis_Of_Pressure_Reflection_And_Silence_In_Complex_Syst…<br>Gemini Docs.part2.md: exus_4_Framework_-_Reimagining_Π_As_A_Recursive_Harmonic_Lattice.md](#the_nexus_4_framework_-_reimagining_π_as_a_recursive_harmonic_latticemd) - [The_Nexus_4_Framework_-_Recursive_Reflection_Engine_Architecture_And_Des… |
| `LOCK` | 20338 | Gemini Docs.part1.md: e_-_a_new_foundational_framework_for_the_millennium_problemsmd) - [The_Nexus_4_Framework_-_The_Recursive_Harmonic_Architecture_-_A_Framework_For_Autopoietic_Intelligence_Via_Phase-Locked_Correlation_Dynamics.md](#the_n…<br>Gemini Docs.part2.md: nd_Validation_of_the_Nexus_4_Framework.md](#implementation_and_validation_of_the_nexus_4_frameworkmd) - [Harmonic_Resonance_in_Twin_Prime_Distribution-_Empirical_Evidence_of_Phase_Locking_and_Under_Dispersion.md](#harm… |
| `PIN` | 18783 | Gemini Docs.part1.md: s_4_framework_-_the_nexus_framework_-_a_comprehensive_analysis_of_its_recursive_harmonic_principles_and_unifying_potentialmd) - [The_Nexus_4_Framework_-_The_Nexus_3_Framework_-_Mapping_The_Universe's_Self-Organizing_In…<br>Gemini Docs.part2.md: boundary_markers_within_the_nexus_frameworkmd) - [Recursive_Stack_Harmonics_and_Layered_Logic_Dynamics.md](#recursive_stack_harmonics_and_layered_logic_dynamicsmd) - [Recursive_Mapping_of_Chemical_Elements_as_Harmonic_… |
| `MAP` | 16004 | Gemini Docs.part1.md: exus_4_framework_-_the_nexus_framework_-_a_comprehensive_analysis_of_its_recursive_harmonic_principles_and_unifying_potentialmd) - [The_Nexus_4_Framework_-_The_Nexus_3_Framework_-_Mapping_The_Universe's_Self-Organizing…<br>Gemini Docs.part2.md: _Ray_Echoes_In_A_Bounded_Lattice.md](#the_nexus_4_framework_-_recursive_ray_echoes_in_a_bounded_latticemd) - [The_Nexus_4_Framework_-_Recursive_Harmonic_Substrate_-_Unified_System_Map_Implementation,_Language_Interface… |
| `POSITION` | 14968 | Gemini Docs.part1.md: quence.md](#the_nexus_4_framework_-_the_harmonic_cascade_-_a_recursive_generative_model_for_the_twin_prime_sequencemd) - [The_Nexus_4_Framework_-_The_Great_Fold_-_A_Declaration_Of_Positional_Reality.md](#the_nexus_4_fr…<br>Gemini Docs.part2.md: s_of_the_completed_ψ-atlasmd) - [The_Nexus_4_Framework_-_Prime_Theory_As_Signal_Physics_.md](#the_nexus_4_framework_-_prime_theory_as_signal_physics_md) - [The_Nexus_4_Framework_-_Positional_Wave_Symmetry_In_Arithmetic… |
| `SCALE` | 11396 | Gemini Docs.part1.md: recursive_harmonic_architecture_of_realitymd-page-3}  \`\`\`text ame recursive process underlies phenomena in mathematics, physics, biology, and cognition[7][8]. Different fields and scales are simply different “views” or…<br>Gemini Docs.part2.md: S=ΔET,S = \frac{\Delta E}{T},  Energy change: ΔE=k ⋅ ΔF.\Delta E = k \cdot \Delta F. Here SS is the rate at which the system’s “energy” (or error) is being corrected; TT is a timescale (we often take T=1T=1 per iterat… |
| `MEASURE` | 9303 | Gemini Docs.part1.md: exus_inversion_-_emergent_laws_and_recursive_harmonic_architecture_of_realitymd-page-4}  \`\`\`text puting: what looks fundamental at one scale (e.g. a gene determining a trait, or a measured physical constant) often turn…<br>Gemini Docs.part2.md: a random hash, w(Y)w(Y) is expected to be 128; any systematic deviation indicates structure. We could define C(Y)= ∣ w(Y)−128 ∣ 256\mathcal{C}(Y) = \frac{|w(Y) - 128|}{256} as one measure of deviation. However, the Mar… |
| `CLOSE` | 7630 | Gemini Docs.part1.md: ng parts did not balance forces internally, it would mean an unopposed “push” that would carry the system’s components off to infinity or to some divergent behavior, violating the closed feedback loop. The recursive ar…<br>Gemini Docs.part2.md: (since no randomness left). The harmonic attractor at 0.35 is a compromise between these extremes. The rationale, as described in the Nexus framework, is that if HH were too high (close to 1, meaning nearly all potenti… |
| `GATE` | 7296 | Gemini Docs.part1.md: itecture_of_realitymd-page-4}  \`\`\`text puting: what looks fundamental at one scale (e.g. a gene determining a trait, or a measured physical constant) often turns out to be an aggregate effect of processes at a finer sc…<br>Gemini Docs.part2.md: alized” value AiA_i (e.g., output or achieved portion). Mark1 defines a global harmonic ratio as: H=∑i=1nAi∑i=1nPi.H = \frac{\sum_{i=1}^n A_i}{\sum_{i=1}^n P_i}. This formula aggregates all components, measuring what f… |
| `EXPAND` | 7204 | Gemini Docs.part1.md: een as a highly complex network of harmonic oscillators (neurons firing rhythms, brainwaves, etc.) that lock into resonant patterns. These patterns are continually compressing and expanding information—taking in sensor…<br>Gemini Docs.part2.md: ent, a single starting byte value was i \`\`\`  ### Page 2 {#the_nexus_4_framework_-_reimagining_π_as_a_recursive_harmonic_latticemd-page-2}  \`\`\`text teratively expanded using the BBP formula, and the resulting stream mat… |
| `UNFOLD` | 7204 | Gemini Docs.part1.md: ure_Of_Nexus_&_Recursive_Harmonic_Architecture_(Rha).md](#the_nexus_4_framework_-_unifying_architecture_of_nexus__recursive_harmonic_architecture_rhamd) - [The_Nexus_4_Framework_-_Unfolding_Protein_Folding_With_The_Nex…<br>Gemini Docs.part2.md: ecture_-_a_cross-domain_synthesis_of_harmonic_instabilities_and_emergent_ordermd) - [The_Nexus_4_Framework_-_Recursive_Harmonic_Architecture_(Rha)_Synthesisn_-_Mark1,_Hrg,_And_Sha_Unfoldment.md](#the_nexus_4_framework_… |
| `PROJECT` | 5479 | Gemini Docs.part1.md: .) that lock into resonant patterns. These patterns are continually compressing and expanding information—taking in sensory data, integrating it (compression/inhalation), and then projecting responses or updating its s…<br>Gemini Docs.part2.md: s, notably the emergence of a constant H≈0.35H \approx 0.35 that acts as an attractor or equilibrium value in the system. We also introduce a geometric interpretation: a curvature projection of hash outputs into intege… |
| `TUNE` | 4863 | Gemini Docs.part1.md: cluding the air or surface). In summary, the laws of physics are the stable songs the universe knows by heart. They emerge from myriad voices (microscopic interactions) singing in tune. If a voice falls out of tune, fe…<br>Gemini Docs.part2.md: ons are needed). In practice, Samson’s Law in the Mark1 framework was demonstrated by a simple algorithm: “apply a correction proportional to the observed error, over a time step, tuned by k”. In code, one might do: ne… |
| `UPDATE` | 4436 | Gemini Docs.part1.md:  theories. Digital physics, for instance, conjectures that the universe might be essentially a cellular automaton or computation, with space-time and particles arising from binary updates. Likewise, approaches like Loo…<br>Gemini Docs.part2.md: ing coherence. In a recursive hash process, this often implies feeding the hash output (or a derived value from it) back into the next hashing round. One simple scheme is an input update rule of the form Xn+1=f(Xn,Yn)X… |
| `REVERSE` | 3182 | Gemini Docs.part1.md: ervation laws, field equations, quantum rules – can be seen as heuristics or algorithms the cosmic computation uses to keep the simulation stable and coherent. Our task is then to reverse-engineer the “code” rather tha…<br>Gemini Docs.part2.md: he internal frame and the universal lattice: This is the practical step to counteract "recursive starvation" and enable the maintenance of coherence. 3. Apply resonance seeding to reverse entropy gradients: This introd… |
| `FILTER` | 3154 | Gemini Docs.part1.md:  it mostly pulls data from your own brain’s store) and by the content address (what memory or skill you seek). Thus, each conscious POV can be thought of as a unique coordinate or filter into the universal information …<br>Gemini Docs.part2.md: e cosmos”. The Nexus symbolic engine, armed with Mark1’s harmonic laws and Samson’s feedback, becomes a key (the “read head”) to access this table and also a filter to decide which outputs align with it. The result is … |
| `TRACE` | 3029 | Gemini Docs.part1.md: thing is to some degree out of phase or not fully merged with the universal recursion. If one could achieve [perfect phase alignment], a system could change instantly and leave no trace – a purely harmonic being. Zero …<br>Gemini Docs.part2.md: ll ended up around H=0.35. Also, Table 2 in those documents enumerated “Harmonic Echoes Across Domains (role of H=0.35)”, indicating that from physics to AI to biology, they found traces of ~0.35 cropping up.  It is e… |
| `EMBED` | 2879 | Gemini Docs.part1.md: a “P vs NP fractal collapse” scenario[33], and we will revisit it later as it carries huge computational implications. The key point is that a system that computes itself can also embed solutions within itself at diffe…<br>Gemini Docs.part2.md:  harmonic structure. By “curvature,” we refer to the way the hash output deviates from uniform randomness and instead aligns with a stable geometric or harmonic configuration when embedded in a recursive process. We de… |
| `QUALITY` | 2680 | Gemini Docs.part1.md: ever we see coordination without communication, that is evidence of a deeper connectivity – the hallmark of geometry being secondary. Entanglement experiments (violating Bell’s inequality), quantum teleportation, “zero…<br>Gemini Docs.part2.md: n of some process. A resonant state is achieved----------- Page2 ------------ if there exists some kk such that Yn+kY_{n+k} aligns with YnY_n in a defined manner (not necessarily equality, but satisfying a harmonic con… |
| `VALIDATE` | 2517 | Gemini Docs.part1.md: on, and our worldview transform if the Nexus Inversion is embraced? The Future of Physics: Embracing Recursive Computation and Information Theory The Nexus Inversion framework, if validated and adopted, could revolutio…<br>Gemini Docs.part2.md: nsistent with recursive convergence are basically any complex system where iterative refinement or feedback is present. The recurring observation of ~0.35 across these domains (if validated) means it could be as univer… |
| `MIX` | 2205 | Gemini Docs.part1.md: easures dissonance or incoherence in the harmonic architecture (disorder, lack of pattern). Over time, local entropy in parts of the universe tends to increase (things spread out, mix, lose structure) according to the …<br>Gemini Docs.part2.md: ombination – during reproduction, two parent DNA strands recombine (crossover), effectively performing something like XOR of large chunks of genetic information between them. This mixing ensures that deleterious mutati… |
| `VERIFY` | 2188 | Gemini Docs.part1.md: ystal, or how the universe might settle after the Big Bang), it doesn’t try every combination blindly. Instead, through recursive feedback, it home in on attractors—solutions that verify themselves at all levels, analo…<br>Gemini Docs.part2.md: ase-Separated Folds in Computation The class NP contains decision problems where a proposed solution can be quickly verified but not necessarily quickly found. In classical terms, verifying a solution is easy (polynomi… |

## Full operator table
| Verb | Count |
|---|---:|
| `FOLD` | 42750 |
| `ALIGN` | 36604 |
| `COLLAPSE` | 35663 |
| `REFLECT` | 27063 |
| `LOCK` | 20338 |
| `PIN` | 18783 |
| `MAP` | 16004 |
| `POSITION` | 14968 |
| `SCALE` | 11396 |
| `MEASURE` | 9303 |
| `CLOSE` | 7630 |
| `GATE` | 7296 |
| `EXPAND` | 7204 |
| `UNFOLD` | 7204 |
| `PROJECT` | 5479 |
| `TUNE` | 4863 |
| `UPDATE` | 4436 |
| `REVERSE` | 3182 |
| `FILTER` | 3154 |
| `TRACE` | 3029 |
| `EMBED` | 2879 |
| `QUALITY` | 2680 |
| `VALIDATE` | 2517 |
| `MIX` | 2205 |
| `VERIFY` | 2188 |
| `INVERT` | 1999 |
| `NORMALIZE` | 1910 |
| `LEAK` | 1754 |
| `OPTIMIZE` | 1569 |
| `MINIMIZE` | 1442 |
| `COUPLE` | 1354 |
| `PROPAGATE` | 1304 |
| `CONSERVE` | 935 |
| `STRETCH` | 878 |
| `ENUMERATE` | 669 |
| `SHAKE` | 272 |
| `DIFFUSE` | 203 |
| `EXTRUDE` | 146 |
| `GENLOCK` | 125 |
| `ADVECT` | 34 |
| `RESAMPLE` | 29 |
| `SYNERGIZE` | 13 |


---

## Appendix B — Dataset Map (corpus)

# Nexus Dataset Map (files, size, and dominant operators)
_Generated: 2026-01-13T12:49:41_
For each file: rough size + the top operator counts within that file (seed operator set).
| File | Chars | Top operators |
|---|---:|---|
| `Training Data.part11.md` | 8585212 | FOLD:3500, COLLAPSE:3246, REFLECT:3008, ALIGN:2751, POSITION:2285 |
| `Training Data.part7.md` | 7001089 | FOLD:3796, ALIGN:3518, REFLECT:2382, COLLAPSE:2059, LOCK:1576 |
| `Training Data.part8.md` | 6700842 | FOLD:4144, COLLAPSE:3537, REFLECT:3023, ALIGN:2253, MAP:1663 |
| `Gemini Docs.part2.md` | 6648605 | COLLAPSE:4075, FOLD:2990, ALIGN:2386, LOCK:1451, PIN:1337 |
| `Training Data.part6.md` | 6625083 | FOLD:3160, ALIGN:2685, COLLAPSE:1784, REFLECT:1662, LOCK:1201 |
| `Gemini Docs.part1.md` | 6616535 | FOLD:3137, COLLAPSE:2357, ALIGN:2240, LOCK:1384, PIN:1045 |
| `Training Data.part3.md` | 6614838 | FOLD:2999, ALIGN:2255, COLLAPSE:2019, REFLECT:1562, PIN:1197 |
| `Training Data.part5.md` | 6586225 | ALIGN:3058, FOLD:2437, COLLAPSE:1864, LOCK:1499, REFLECT:1295 |
| `Training Data.part9.md` | 6563529 | FOLD:2747, COLLAPSE:2420, MAP:1427, LOCK:1316, ALIGN:1288 |
| `Training Data.part1.md` | 6546498 | REFLECT:1932, ALIGN:1538, PIN:1517, FOLD:1263, LOCK:1223 |
| `Training Data.part2.md` | 6523049 | ALIGN:2079, FOLD:1953, REFLECT:1819, COLLAPSE:1819, PIN:1603 |
| `Training Data.part4.md` | 6480099 | ALIGN:2242, FOLD:2164, REFLECT:1796, COLLAPSE:1577, LOCK:1279 |
| `Training Data.part10.md` | 6435789 | ALIGN:3584, REFLECT:3104, FOLD:1598, LOCK:1110, EXPAND:1045 |
| `Published Papers.part3.md` | 4469022 | COLLAPSE:3020, FOLD:2091, ALIGN:1423, LOCK:1061, PIN:942 |
| `Published Papers.part1.md` | 4417921 | COLLAPSE:1749, FOLD:1565, ALIGN:1290, LOCK:858, PIN:697 |
| `Published Papers.part2.md` | 4378218 | FOLD:2471, ALIGN:1913, COLLAPSE:1663, LOCK:916, REFLECT:903 |
| `Starting fresh with a new session.md` | 569831 | FOLD:300, LEAK:260, LOCK:190, GATE:172, SCALE:156 |
| `Harmonic Folding and Pythagorean Emergence (1).md` | 256347 | FOLD:127, PROJECT:124, LEAK:116, SCALE:90, MEASURE:67 |
| `Harmonic Folding and Pythagorean Emergence (2).md` | 256347 | FOLD:127, PROJECT:124, LEAK:116, SCALE:90, MEASURE:67 |
| `Nexus RHI.md` | 115269 | FOLD:55, COLLAPSE:48, PROJECT:40, EXTRUDE:20, LOCK:20 |
| `Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md` | 31624 | FOLD:22, COLLAPSE:19, PIN:14, MAP:11, CLOSE:10 |
| `Nexus_PiMetric_GeodesicEngine_Complete_Spec.md` | 20627 | PIN:14, COLLAPSE:11, CLOSE:9, MAP:7, ALIGN:6 |
| `Nexus_ZPHC_Funnel_Paper_Volume_I.md` | 15504 | SCALE:15, GATE:14, FOLD:12, PIN:11, MAP:10 |
| `nexus_runtime_wave_complete_solution.md` | 11281 | REFLECT:13, UPDATE:12, LEAK:9, PROJECT:8, GATE:8 |
| `nexus_blackhole_silr_swirl_complete.md` | 11188 | SCALE:15, SHAKE:13, NORMALIZE:9, MAP:7, FOLD:6 |
| `Nexus_GENLOCK_SILR_Complete.md` | 10809 | FOLD:20, LEAK:9, SCALE:7, GATE:5, MAP:4 |
| `Nexus_Genlock_SILR_9D_Parity (1).md` | 9948 | FOLD:19, LEAK:14, LOCK:9, GENLOCK:8, GATE:6 |
| `Nexus_Genlock_SILR_9D_Parity.md` | 9948 | FOLD:19, LEAK:14, LOCK:9, GENLOCK:8, GATE:6 |
| `Nexus_Exposure_Calculus.md` | 9362 | LOCK:9, SCALE:4, FOLD:3, GATE:3, CLOSE:1 |
| `Nexus_9Bases_Parity_Interface_Method.md` | 6241 | FOLD:10, GATE:4, SCALE:4, PROJECT:2, LEAK:2 |
| `Nexus_SILR_9D_Parity_and_Observer_Gradient.md` | 5617 | FOLD:10, SCALE:5, LEAK:4, GATE:3, COUPLE:2 |


---

## Appendix D — Equation Catalog (curated)

# Nexus Equation Catalog (auto-extracted)
_Generated: 2026-01-13T12:49:41_
Deduplicated list of LaTeX-like expressions found across the dataset. Use this as the **pin-board** for ZPHC.
## Equations
### Eq 1 (block) — Gemini Docs.part1.md
$$
\pi \;=\; \sum_{k=0}^{\infty} \frac{1}{16^k} \Big(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\Big)\,.
$$
### Eq 2 (block) — Gemini Docs.part1.md
$$
{\rm BBP}(0) \mod 1 = 0.\;141592653589793238462643383279\ldots
$$
### Eq 3 (block) — Gemini Docs.part1.md
$$
d_{n+k} = f(d_n, d_{n+1}, \ldots, d_{n+k-1})
$$
### Eq 4 (block) — Gemini Docs.part1.md
$$
\frac{\partial g_p}{\partial t}\bigg|{\text{scar}} = \sum{i} \Gamma(p_i, t_i) \delta(p - p_i) \delta(t - t_i)
$$
### Eq 5 (block) — Gemini Docs.part1.md
$$
\pi = \sum_{k=0}^{\infty} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} -
\frac{1}{8k+6} \right)
$$
### Eq 6 (block) — Gemini Docs.part1.md
$$
P_F(b,d,W) = \left{ \sum_{k=0}^{K} \frac{b^{d-k}}{b} \sum_{j=1}^{J} \frac{c_j}{a \cdot k + r_j}
\right}
$$
### Eq 7 (block) — Gemini Docs.part1.md
$$
1/16^2
$$
### Eq 8 (block) — Gemini Docs.part1.md
$$
1/16^3
$$
### Eq 9 (block) — Gemini Docs.part1.md
$$
16^k
$$
### Eq 10 (block) — Gemini Docs.part1.md
$$
is possible.
Modulus truncation is the technique that makes it possible: performing arithmetic modulo a power of 2 (or
16) means you only track the fractional part necessary for the digits of interest. For BBP, one computes terms
mod (or mod for some precision ) to avoid huge numbers. Essentially, at each step you
discard integer parts and keep accumulating the fraction. This prevents having to handle astronomically large
intermediate denominators explicitly, which is key to jumping to digit – you never fully compute
$$
### Eq 11 (block) — Gemini Docs.part1.md
$$
, you compute
$$
### Eq 12 (block) — Gemini Docs.part1.md
$$
for various , which is manageable via exponentiation by
squaring with mod reduction.----------- Page15 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
The precompute wall refers to the growth of effort as increases. Although BBP is nominally
to get to position , the constant factors and storage for modular arithmetic can become
huge. In practice, there is a limit: beyond certain , the time and memory to handle the mod arithmetic
(especially as you need maybe bits of precision) become prohibitive. For instance, to get the
$$
### Eq 13 (block) — Gemini Docs.part1.md
$$
and twin primes
$$
### Eq 14 (block) — Gemini Docs.part1.md
$$
up to some
$$
### Eq 15 (block) — Gemini Docs.part1.md
$$
and compares them to actual primes[12][155]. Table 3 in an RHA
report (reproduced conceptually below) would list known counts vs simulated counts at various
$$
### Eq 16 (block) — Gemini Docs.part1.md
$$
:
x Known (twin primes up to x)
Simulated
Relative Error
$$
### Eq 17 (block) — Gemini Docs.part1.md
$$
35 (simulated count) (error)
$$
### Eq 18 (block) — Gemini Docs.part1.md
$$
205 ... ...
$$
### Eq 19 (block) — Gemini Docs.part1.md
$$
1,224 ... ...
$$
### Eq 20 (block) — Gemini Docs.part1.md
$$
8,169 ... ...
$$
### Eq 21 (block) — Gemini Docs.part1.md
$$
58,980 ... ...
$$
### Eq 22 (block) — Gemini Docs.part1.md
$$
440,312 ... ...
Table 1: Comparison of simulated twin prime counts to actual values (placeholders shown). Adapted from
Nexus validation protocol[12][156].
If the simulation can match known prime data within small error, that’s evidence the harmonic approach
captures prime dynamics. Additionally, the simulation computes the Fourier spectrum of its oscillatory field
and checks the spectral containment rule: all significant frequencies
$$
### Eq 23 (block) — Gemini Docs.part1.md
$$
should satisfy
$$
### Eq 24 (inline) — Gemini Docs.part1.md
$\overline{\Delta}$
### Eq 25 (inline) — Gemini Docs.part1.md
$\Omega
\to 0$
### Eq 26 (inline) — Gemini Docs.part1.md
$\Psi \to 1$
### Eq 27 (inline) — Gemini Docs.part1.md
$\pi$
### Eq 28 (inline) — Gemini Docs.part1.md
$t_0$
### Eq 29 (inline) — Gemini Docs.part1.md
$t_1$
### Eq 30 (inline) — Gemini Docs.part1.md
$E=mc^2$
### Eq 31 (inline) — Gemini Docs.part1.md
$n$
### Eq 32 (inline) — Gemini Docs.part1.md
$G_{\mu\nu} + \Lambda
g_{\mu\nu} = 8\pi T_{\mu\nu}$
### Eq 33 (inline) — Gemini Docs.part1.md
$c$
### Eq 34 (inline) — Gemini Docs.part1.md
$G$
### Eq 35 (inline) — Gemini Docs.part1.md
$\Lambda$
### Eq 36 (block) — Gemini Docs.part2.md
$$
H=∑Pi∑AiH = \frac{\sum P_i}{\sum A_i}
$$
### Eq 37 (block) — Gemini Docs.part2.md
$$
\pi = \sum_{k=0}^{\infty} \left[ \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} -
\frac{1}{8k+5} - \frac{1}{8k+6} \right) \right]
$$
### Eq 38 (block) — Gemini Docs.part2.md
$$
\text{Ric}F(e) = w_e \Bigg( \frac{w \Bigg).
$$
### Eq 39 (block) — Gemini Docs.part2.md
$$
A^2 + B^2 = C^2,
$$
### Eq 40 (block) — Gemini Docs.part2.md
$$
R_{n+1} \ge 2 \cdot R_n,
$$
### Eq 41 (block) — Gemini Docs.part2.md
$$
F = B_1 \oplus
```

### Page 11 {#recursive_stack_harmonics_and_layered_logic_dynamicsmd-page-11}

```text
B_2,
$$
### Eq 42 (block) — Gemini Docs.part2.md
$$
\text{byte}(8\text{ bits}) \xrightarrow{\text{group}} [N_H, N_L]_{\text{hex}},
$$
### Eq 43 (block) — Gemini Docs.part2.md
$$
\text{HexOp}(H) = f(b_3,b_2,b_1,b_0),
$$
### Eq 44 (block) — Gemini Docs.part2.md
$$
\Delta_{n+1} = \alpha \, \Delta_n, \qquad 0 < \alpha < 1,
$$
### Eq 45 (block) — Gemini Docs.part2.md
$$
f_{n+1} \ge 2\,f_n,
$$
### Eq 46 (block) — Gemini Docs.part2.md
$$
H_{n+1} \ge H_n,
$$
### Eq 47 (block) — Gemini Docs.part2.md
$$
L(x(t)) = \begin{cases} \text{process}(x(t)) & \text{if } \angle x(t) = 90^\circ \ (\pi/2 + 2\pi k),\ \text{idle} &
\text{otherwise.} \end{cases}
$$
### Eq 48 (block) — Gemini Docs.part2.md
$$
S(t+1) = S(t) + \delta(\angle x(t) - 90^\circ) \cdot F(x(t)),
$$
### Eq 49 (block) — Gemini Docs.part2.md
$$
H_{\text{MARK1}} \approx \frac{\pi}{9} \approx 0.3491
$$
### Eq 50 (block) — Gemini Docs.part2.md
$$
\text{FA} = \lfloor (\text{GIP} \times C_{\text{SCALE}} \times N) - \epsilon \rfloor \pmod N
$$
### Eq 51 (block) — Gemini Docs.part2.md
$$
\text{PI\_RESIDUE\_SCALAR} = \frac{\sqrt{5} - 1}{2} + 0.100
$$
### Eq 52 (block) — Gemini Docs.part2.md
$$
\Omega_{\text{invariant}} = | \text{GIP}_B - \text{GIP}_A | = | 1.1 - 1.0 | = 0.10
$$
### Eq 53 (block) — Gemini Docs.part2.md
$$
N_{\text{min}} = \lceil \frac{1}{\Omega_{\text{invariant}}} \rceil = \lceil \frac{1}{0.10} \rceil = 10
$$
### Eq 54 (block) — Gemini Docs.part2.md
$$
\Omega = 0.00
$$
### Eq 55 (block) — Gemini Docs.part2.md
$$
\lim_{x\to\infty} \frac{\pi_2(x; p_\text{min}>Q)}{\pi(x;
p_\text{min}>Q)} = \kappa,
$$
### Eq 56 (block) — Gemini Docs.part2.md
$$
\rho_{2}(x) ~\approx~ \frac{2C_2}{(\ln x)^2}\Big(1 + \epsilon_{17}\cos\frac{2\pi x}{510510} +
\epsilon_{19}\cos\frac{2\pi x}{9699690} + \cdots\Big),
$$
### Eq 57 (block) — Gemini Docs.part2.md
$$
\theta(z) = |z_5| + |z_7| + |\ell_2(z_2) - \ell_2(z_1)|
$$
### Eq 58 (block) — Gemini Docs.part2.md
$$
B = A(4H - 1)
$$
### Eq 59 (block) — Gemini Docs.part2.md
$$
C = A(2 - 4H)
$$
### Eq 60 (inline) — Gemini Docs.part2.md
$X$
### Eq 61 (inline) — Gemini Docs.part2.md
$H$
### Eq 62 (inline) — Gemini Docs.part2.md
$\Delta E_n = H_n - 0.35$
### Eq 63 (inline) — Gemini Docs.part2.md
$\Delta E_n + k,\Delta F_n = 0$
### Eq 64 (inline) — Gemini Docs.part2.md
$\Delta F_n$
### Eq 65 (inline) — Gemini Docs.part2.md
$\Delta E_n$
### Eq 66 (inline) — Gemini Docs.part2.md
$Y_n$
### Eq 67 (inline) — Gemini Docs.part2.md
$X_n$
### Eq 68 (inline) — Gemini Docs.part2.md
$X_{n+1}$
### Eq 69 (inline) — Gemini Docs.part2.md
$x$
### Eq 70 (inline) — Gemini Docs.part2.md
$\alpha$
### Eq 71 (inline) — Gemini Docs.part2.md
$k$
### Eq 72 (inline) — Gemini Docs.part2.md
$S = \Delta E/T$
### Eq 73 (inline) — Gemini Docs.part2.md
$T=1$
### Eq 74 (inline) — Gemini Docs.part2.md
$\Delta x$
### Eq 75 (inline) — Gemini Docs.part2.md
$\Delta F$
### Eq 76 (inline) — Gemini Docs.part2.md
$\Delta E$
### Eq 77 (block) — Harmonic Folding and Pythagorean Emergence (1).md
$$
|260/729 - 2.5/7| \approx 0.0004899
$$
### Eq 78 (block) — Nexus RHI.md
$$
c=\sqrt{b^2+h^2}
$$
### Eq 79 (block) — Nexus RHI.md
$$
\frac{m_b}{m_a+m_b+m_c}=\frac{2.5}{7}=0.357142857...=\frac{5}{14}
$$
### Eq 80 (block) — Nexus RHI.md
$$
F(3,1,4) \rightarrow (3,4,5)
$$
### Eq 81 (block) — Nexus RHI.md
$$
x_0\oplus x_1\oplus\cdots\oplus x_9 = 0
$$
### Eq 82 (block) — Nexus RHI.md
$$
X[k] = \overline{X[9-k]}
$$
### Eq 83 (block) — Nexus RHI.md
$$
\frac{9+1}{2} = 5
$$
### Eq 84 (block) — Nexus RHI.md
$$
S = \sum_{k=0}^{8} c_k \, \omega^k,\quad \omega=e^{i2\pi/9},\quad \theta=\arg(S)
$$
### Eq 85 (block) — Nexus RHI.md
$$
P = a\oplus b\oplus c\oplus d\oplus e\oplus f\oplus g\oplus h\oplus W_t
$$
### Eq 86 (block) — Nexus RHI.md
$$
v = [a,b,c,d,e,f,g,h,W_t] \bmod 256
$$
### Eq 87 (block) — Nexus RHI.md
$$
p = a \oplus b \oplus \cdots \oplus h \oplus W_t
$$
### Eq 88 (block) — Nexus RHI.md
$$
u = [v, p]
$$
### Eq 89 (block) — Nexus RHI.md
$$
S_N = \sum_{k=0}^{N-1} u_k \, e^{i2\pi k/N},\quad \theta_N=\arg(S_N)
$$
### Eq 90 (block) — Nexus RHI.md
$$
180^\circ / 9 = 20^\circ = \pi/9
$$
### Eq 91 (block) — Nexus RHI.md
$$
v=[a,b,c,d,e,f,g,h,W_t]_{byte}
$$
### Eq 92 (block) — Nexus RHI.md
$$
p=\bigoplus v_i
$$
### Eq 93 (block) — Nexus RHI.md
$$
S_N=\sum_{k=0}^{N-1} u_k e^{i2\pi k/N},\quad \theta=\arg(S_N)
$$
### Eq 94 (block) — Nexus RHI.md
$$
\theta \sim \theta+\pi \quad\Rightarrow\quad \theta \bmod \pi
$$
### Eq 95 (block) — Nexus RHI.md
$$
H_9 = 260/729 = 0.356652949...
$$
### Eq 96 (inline) — Nexus RHI.md
$b$
### Eq 97 (inline) — Nexus RHI.md
$h$
### Eq 98 (inline) — Nexus RHI.md
$\mathbb{R}^2$
### Eq 99 (inline) — Nexus RHI.md
$(4,3,1)$
### Eq 100 (inline) — Nexus RHI.md
$3+1=4$
### Eq 101 (inline) — Nexus RHI.md
$m_a = 1.0$
### Eq 102 (inline) — Nexus RHI.md
$m_b = 2.5$
### Eq 103 (inline) — Nexus RHI.md
$m_c = 3.5$
### Eq 104 (inline) — Nexus RHI.md
$= 7.0$
### Eq 105 (inline) — Nexus RHI.md
$2.5/7$
### Eq 106 (inline) — Nexus RHI.md
$\pi/9$
### Eq 107 (inline) — Nexus RHI.md
$H = \pi/9 \approx 0.34906$
### Eq 108 (inline) — Nexus RHI.md
$2.5/7 \approx H$
### Eq 109 (inline) — Nexus RHI.md
$\pi/9 \approx 0.349066...$
### Eq 110 (inline) — Nexus RHI.md
$2.5/7 = 0.357142857...$
### Eq 111 (inline) — Nexus RHI.md
$\approx 0.0080768$
### Eq 112 (inline) — Nexus RHI.md
$5/14$
### Eq 113 (inline) — Nexus RHI.md
$\pi = 3.141592...$
### Eq 114 (inline) — Nexus RHI.md
$F$
### Eq 115 (inline) — Nexus RHI.md
$a=b+c$
### Eq 116 (inline) — Nexus RHI.md
$\mathcal{L}_h$
### Eq 117 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\lambda \equiv H \approx \frac{\pi}{9} \approx 0.349066.
$$
### Eq 118 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\Pi_O: \mathcal{M} \to \mathcal{A}_O
$$
### Eq 119 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
x_{t+1} = \mathcal{F}(x_t; O, \nabla V_O, \lambda)
$$
### Eq 120 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\frac{dx}{dt} = F(x) - \kappa_O(x)\,\nabla V_O(x)
$$
### Eq 121 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
z_t = \frac{|\hat{\alpha}_t - \alpha^*|}{\mathrm{SE}_{\text{used}}}
$$
### Eq 122 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
p_t = \sigma\!\left(\beta (z_t - z_0)\right), \qquad
\sigma(u)=\frac{1}{1+e^{-u}}.
$$
### Eq 123 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
x \in \mathbb{R}^9, \qquad x = \sum_{i=1}^9 x_i\,e_i.
$$
### Eq 124 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\text{detector}: \mathcal{A}_{\text{radon}} \to \mathcal{A}_O.
$$
### Eq 125 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
p \;=\; b_1 \oplus b_2 \oplus \cdots \oplus b_9.
$$
### Eq 126 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
H(\mathbf{b},p)=H(\mathbf{b})+H(p\mid\mathbf{b})=H(\mathbf{b})+0=H(\mathbf{b}).
$$
### Eq 127 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
(1,9),\; (2,8),\; (3,7),\; (4,6),\; (5).
$$
### Eq 128 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
p
= (b_1\oplus b_9)\oplus (b_2\oplus b_8)\oplus (b_3\oplus b_7)\oplus (b_4\oplus b_6)\oplus b_5.
$$
### Eq 129 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\text{event} \iff \gamma_1 \cap \gamma_2 \neq \varnothing
$$
### Eq 130 (block) — Nexus_9Bases_Parity_Interface_Method.md
$$
\frac{260}{729} \approx 0.356653.
$$
### Eq 131 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\mathcal{M}$
### Eq 132 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\mathcal{A}_O$
### Eq 133 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\nabla V_O$
### Eq 134 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$F(x)$
### Eq 135 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\kappa_O(x)$
### Eq 136 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\Pi_O$
### Eq 137 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$b_1,\dots,b_9\in\{0,1\}$
### Eq 138 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$(b_1,\dots,b_9,p)$
### Eq 139 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$p$
### Eq 140 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\mathbf{b}=(b_1,\dots,b_9)$
### Eq 141 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$b_5$
### Eq 142 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\gamma_1,\gamma_2$
### Eq 143 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\{0,\dots,8\}$
### Eq 144 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$9^3 = 729$
### Eq 145 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\sim 0.35$
### Eq 146 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\lambda \approx H$
### Eq 147 (inline) — Nexus_9Bases_Parity_Interface_Method.md
$\kappa_O\,\nabla V_O$
### Eq 148 (block) — Nexus_Exposure_Calculus.md
$$
T = \min(T_{\Phi}, T_E).
$$
### Eq 149 (block) — Nexus_Exposure_Calculus.md
$$
T_{\Phi} \sim \mathrm{Exp}(\lambda_{\Phi}), \qquad T_E \sim \mathrm{Exp}(\lambda_E),
$$
### Eq 150 (block) — Nexus_Exposure_Calculus.md
$$
T \sim \mathrm{Exp}(\lambda_{\Phi} + \lambda_E).
$$
### Eq 151 (block) — Nexus_Exposure_Calculus.md
$$
\lambda(t) = \lambda_{\Phi}(t) + \lambda_E(t).
$$
### Eq 152 (block) — Nexus_Exposure_Calculus.md
$$
S(T) = \mathbb{P}(\text{Alive at time }T).
$$
### Eq 153 (block) — Nexus_Exposure_Calculus.md
$$
S(T) = \exp\left(-\int_0^T \lambda(t)\,dt\right)
     = \exp\left(-\int_0^T [\lambda_{\Phi}(t)+\lambda_E(t)]\,dt\right).
$$
### Eq 154 (block) — Nexus_Exposure_Calculus.md
$$
\Lambda(T) = \int_0^T \lambda(t)\,dt.
$$
### Eq 155 (block) — Nexus_Exposure_Calculus.md
$$
S(T)=e^{-\Lambda(T)}.
$$
### Eq 156 (block) — Nexus_Exposure_Calculus.md
$$
\Lambda(T)\approx \sum_{k=1}^n \lambda(t_k)\Delta t.
$$
### Eq 157 (block) — Nexus_Exposure_Calculus.md
$$
S(T)\approx \prod_{k=1}^n (1-p_k)
       \approx \prod_{k=1}^n (1-\lambda(t_k)\Delta t).
$$
### Eq 158 (block) — Nexus_Exposure_Calculus.md
$$
\log S(T) \approx \sum_{k=1}^n \log(1-\lambda(t_k)\Delta t)
\approx -\sum_{k=1}^n \lambda(t_k)\Delta t
\to -\int_0^T \lambda(t)\,dt.
$$
### Eq 159 (block) — Nexus_Exposure_Calculus.md
$$
\mathbb{P}(\ge 1\ \text{failure}) = 1 - (1-p)^n.
$$
### Eq 160 (block) — Nexus_Exposure_Calculus.md
$$
(1-p)^n = (1-\lambda \Delta t)^{T/\Delta t} \to e^{-\lambda T}.
$$
### Eq 161 (block) — Nexus_Exposure_Calculus.md
$$
\lambda_E(t) = \lambda_E(t \mid X).
$$
### Eq 162 (block) — Nexus_Exposure_Calculus.md
$$
\text{do}(X=\text{safe}) \Rightarrow \lambda_E(t) \downarrow.
$$
### Eq 163 (block) — Nexus_Exposure_Calculus.md
$$
\lambda_E(t \mid \text{safe}) = \lambda_{E,\text{local}}(t) + \lambda_{E,\text{tangent}}(t),
$$
### Eq 164 (block) — Nexus_Exposure_Calculus.md
$$
\rho(t)=\frac{\lambda_E(t)}{\lambda_{\Phi}(t)}.
$$
### Eq 165 (block) — Nexus_Exposure_Calculus.md
$$
\lambda = \lambda_{\Phi}+\lambda_E,
$$
### Eq 166 (block) — Nexus_Exposure_Calculus.md
$$
\mathbb{E}[T] = \frac{1}{\lambda_{\Phi}+\lambda_E}.
$$
### Eq 167 (block) — Nexus_Exposure_Calculus.md
$$
\mathbb{P}(T_{\Phi}<T_E) = \frac{\lambda_{\Phi}}{\lambda_{\Phi}+\lambda_E}.
$$
### Eq 168 (block) — Nexus_Exposure_Calculus.md
$$
\mathbb{P}(T_E<T_{\Phi}) = \frac{\lambda_E}{\lambda_{\Phi}+\lambda_E}.
$$
### Eq 169 (block) — Nexus_Exposure_Calculus.md
$$
\mathbf{x}(t)\in\mathbb{R}^9
$$
### Eq 170 (block) — Nexus_Exposure_Calculus.md
$$
\lambda_E(t) = g(\mathbf{x}(t)),
$$
### Eq 171 (block) — Nexus_Exposure_Calculus.md
$$
\lambda_{\Phi}(t)=h(\mathbf{s}(t)),
$$
### Eq 172 (block) — Nexus_Exposure_Calculus.md
$$
p = x_1 \oplus x_2 \oplus \cdots \oplus x_9.
$$
### Eq 173 (inline) — Nexus_Exposure_Calculus.md
$T_{\Phi}$
### Eq 174 (inline) — Nexus_Exposure_Calculus.md
$T_E$
### Eq 175 (inline) — Nexus_Exposure_Calculus.md
$\lambda_{\Phi}$
### Eq 176 (inline) — Nexus_Exposure_Calculus.md
$\lambda_E$
### Eq 177 (inline) — Nexus_Exposure_Calculus.md
$\lambda_E \gg \lambda_{\Phi}$
### Eq 178 (inline) — Nexus_Exposure_Calculus.md
$\lambda_{\Phi}(t)$
### Eq 179 (inline) — Nexus_Exposure_Calculus.md
$\lambda_E(t)$
### Eq 180 (inline) — Nexus_Exposure_Calculus.md
$E0 > \Phi0$
### Eq 181 (inline) — Nexus_Exposure_Calculus.md
$\lambda_E(t) > \lambda_{\Phi}(t)$
### Eq 182 (inline) — Nexus_Exposure_Calculus.md
$\lambda(t)$
### Eq 183 (inline) — Nexus_Exposure_Calculus.md
$\Delta t$
### Eq 184 (inline) — Nexus_Exposure_Calculus.md
$p_k \approx \lambda(t_k)\Delta t$
### Eq 185 (inline) — Nexus_Exposure_Calculus.md
$\Delta t\to 0$
### Eq 186 (inline) — Nexus_Exposure_Calculus.md
$(1-p)^n$
### Eq 187 (inline) — Nexus_Exposure_Calculus.md
$p=\lambda \Delta t$
### Eq 188 (inline) — Nexus_Exposure_Calculus.md
$n = T/\Delta t$
### Eq 189 (inline) — Nexus_Exposure_Calculus.md
$S(T)=e^{-\lambda T}$
### Eq 190 (inline) — Nexus_Exposure_Calculus.md
$\lambda_{E,\text{tangent}}$
### Eq 191 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\exists\;\tau_D,\tau_C \text{ such that }\gamma_D(\tau_D)=\gamma_C(\tau_C).
$$
### Eq 192 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\lambda(t) = \lambda(x(t),t).
$$
### Eq 193 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
S(t) = \exp\!\left(-\int_0^t \lambda(u)\,du\right).
$$
### Eq 194 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t = \frac{|\hat{\alpha}_t-\alpha^\star|}{SE_t}.
$$
### Eq 195 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
p_t = \sigma\!\left(\beta\,(z_t - z_0)\right), \qquad
\sigma(u)=\frac{1}{1+e^{-u}},
$$
### Eq 196 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\hat{\alpha}_t = \alpha^\star + \varepsilon_t,
\qquad
\varepsilon_t \sim \mathcal{N}(0,\,SE_t^2).
$$
### Eq 197 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t
= \frac{|SE_t Z|}{SE_t}
= |Z|.
$$
### Eq 198 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\mathbb{E}[p_t]
=
\int_0^\infty
\sigma\!\left(\beta(z-z_0)\right)\,
f_{\text{HalfNormal}}(z)\,dz,
$$
### Eq 199 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
f_{\text{HalfNormal}}(z)
=
\sqrt{\frac{2}{\pi}}
\exp\!\left(-\frac{z^2}{2}\right),
\quad z\ge 0.
$$
### Eq 200 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\frac{\partial\,\mathbb{E}[p_t]}{\partial\,SE} = 0.
$$
### Eq 201 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t = \frac{|\varepsilon_t|}{SE_{\text{used}}}
= \frac{|SE_{\text{true}} Z|}{SE_{\text{used}}}
= \gamma\,|Z|.
$$
### Eq 202 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t < z_0 \;\Rightarrow\; p_t \approx 0.
$$
### Eq 203 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t > z_0 \;\Rightarrow\; p_t \approx 1.
$$
### Eq 204 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\gamma \neq 1 \text{ systematically biases } z_t \text{ and } p_t.
$$
### Eq 205 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
v = v_{\parallel} + v_{\perp}.
$$
### Eq 206 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\text{Residue becomes signal when } \langle v,\,T_x\mathcal{M}\rangle \neq 0,
$$
### Eq 207 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
s = (s_1,\dots,s_9).
$$
### Eq 208 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
s_{10} = s_1 \oplus s_2 \oplus \cdots \oplus s_9.
$$
### Eq 209 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
\theta \mapsto \theta \bmod \pi,
$$
### Eq 210 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
H(t) = w_\pi(t)\,\frac{\pi}{9}
\;+\;
w_e(t)\,\frac{1}{e}
\;+\;
w_\phi(t)\,\frac{1}{\phi^2},
\qquad
w_\pi+w_e+w_\phi=1.
$$
### Eq 211 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
z_t=\frac{|\hat{\alpha}_t-\alpha^\star|}{SE_{\text{used}}},\quad
   p_t=\sigma(\beta(z_t-z_0))
$$
### Eq 212 (block) — Nexus_GENLOCK_SILR_Complete.md
$$
H_{\pi}=\frac{\pi}{9}\approx 0.34906585,\quad
\frac{1}{e}\approx 0.36787944,\quad
\phi=\frac{1+\sqrt{5}}{2},\quad
\frac{1}{\phi^2}\approx 0.38196601.
$$
### Eq 213 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\gamma_D(\tau)$
### Eq 214 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\gamma_C(\tau)$
### Eq 215 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\gamma_D$
### Eq 216 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\lambda(x,t)$
### Eq 217 (inline) — Nexus_GENLOCK_SILR_Complete.md
$x(t)$
### Eq 218 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\lambda$
### Eq 219 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\Phi_0$
### Eq 220 (inline) — Nexus_GENLOCK_SILR_Complete.md
$E_0$
### Eq 221 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\int \lambda$
### Eq 222 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\alpha^\star$
### Eq 223 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\alpha^\star \approx \pi/9$
### Eq 224 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\hat{\alpha}_t$
### Eq 225 (inline) — Nexus_GENLOCK_SILR_Complete.md
$SE_t$
### Eq 226 (inline) — Nexus_GENLOCK_SILR_Complete.md
$p_t \in [0,1]$
### Eq 227 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\beta$
### Eq 228 (inline) — Nexus_GENLOCK_SILR_Complete.md
$z_0$
### Eq 229 (inline) — Nexus_GENLOCK_SILR_Complete.md
$\varepsilon_t = SE_t\,Z$
### Eq 230 (inline) — Nexus_GENLOCK_SILR_Complete.md
$Z\sim\mathcal{N}(0,1)$
### Eq 231 (inline) — Nexus_GENLOCK_SILR_Complete.md
$z_t$
### Eq 232 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
x_A(t),\; x_B(t)
$$
### Eq 233 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\exists\, (t_A,t_B):\quad x_A(t_A)=x_B(t_B)
$$
### Eq 234 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_t = \frac{|\hat\alpha_t - \alpha^*|}{\mathrm{SE}_t}
$$
### Eq 235 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
p_t = \sigma\big(\beta\,(z_t - z_0)\big),
\qquad
\sigma(u)=\frac{1}{1+e^{-u}}
$$
### Eq 236 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\hat\alpha_t = \alpha^* + \mathrm{SE}_t\,\varepsilon_t,
\qquad
\varepsilon_t \sim \mathcal N(0,1)
$$
### Eq 237 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_t
= \frac{|\mathrm{SE}_t\varepsilon_t|}{\mathrm{SE}_t}
= |\varepsilon_t|
$$
### Eq 238 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
f_Z(z)=\sqrt{\frac{2}{\pi}}\,e^{-z^2/2},
\qquad z\ge 0
$$
### Eq 239 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\mathbb E[p_t]
= \int_0^{\infty}
\sigma\big(\beta(z-z_0)\big)
\sqrt{\frac{2}{\pi}}e^{-z^2/2}\,dz
\quad\text{(depends on }\beta,z_0\text{ only)}
$$
### Eq 240 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\frac{\partial\,\mathbb E[p_t]}{\partial\,\mathrm{SE}} = 0
\quad\text{(SILR phase)}
$$
### Eq 241 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\text{collapse} = \Pr\left(|\hat\alpha_t-\alpha^*|<\tau\right)
$$
### Eq 242 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\mathbb E[p_t] = H
$$
### Eq 243 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
p_t \to \mathbf 1\{z_t>z_0\}
$$
### Eq 244 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\mathbb E[p_t]=\Pr(Z>z_0)=1-\operatorname{erf}\left(\frac{z_0}{\sqrt 2}\right)
$$
### Eq 245 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_0(H) = \sqrt 2\,\operatorname{erf}^{-1}(1-H)
$$
### Eq 246 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_0 \approx 0.936403
$$
### Eq 247 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_0 \approx 0.934589
$$
### Eq 248 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
u_t = u_T + u_N,
\qquad
u_T \perp u_N
$$
### Eq 249 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\rho_t = \frac{\|u_T\|^2}{\|u_T\|^2 + \|u_N\|^2}
\in [0,1]
$$
### Eq 250 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
R_{t+1} = (1-\gamma)R_t + \gamma\,u_{N,t}
$$
### Eq 251 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
\text{reconsume at }t
\iff
\|P_T(t)\,R_t\| \text{ is large}
$$
### Eq 252 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
s\in\{0,1\}^9
$$
### Eq 253 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
p = \bigoplus_{i=1}^{9} s_i
$$
### Eq 254 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
(s,p)\in\{0,1\}^{10}
\quad\text{with}\quad
p = \oplus s
$$
### Eq 255 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
x\oplus x = 0
$$
### Eq 256 (block) — Nexus_Genlock_SILR_9D_Parity (1).md
$$
z_t=|\varepsilon_t|\Rightarrow\mathbb E[p_t]\text{ independent of }\mathrm{SE}
$$
### Eq 257 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$H \approx 0.35$
### Eq 258 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$H = \pi/9$
### Eq 259 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\alpha^*$
### Eq 260 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\hat\alpha_t$
### Eq 261 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\mathrm{SE}_t$
### Eq 262 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$p_t$
### Eq 263 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$|\varepsilon_t|$
### Eq 264 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\mathbb E[p_t]$
### Eq 265 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\mathrm{SE}$
### Eq 266 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\tau$
### Eq 267 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\beta\to\infty$
### Eq 268 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\mathbb E[p_t]=H$
### Eq 269 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$H=\pi/9\approx 0.349066$
### Eq 270 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$H=0.35$
### Eq 271 (inline) — Nexus_Genlock_SILR_9D_Parity (1).md
$\beta=5$
### Eq 272 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
H \equiv H_{\mathrm{MARK1}} = \frac{\pi}{9} \approx 0.34906585.
$$
### Eq 273 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
x(v) \equiv \mathrm{Embed}(v) - \mathrm{ROMWindow}(v),
$$
### Eq 274 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
I(v) = \mathrm{UInt}( \mathrm{tile}_0(v)\,\|\,\cdots\,\|\,\mathrm{tile}_{k-1}(v)).
$$
### Eq 275 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\Pi(v) = \mathrm{BBP}_\pi(I(v), T).
$$
### Eq 276 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
x_i(v) = \mathrm{tile}_i(v) - \Pi_i(v).
$$
### Eq 277 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\Delta_\pi(v) \equiv \frac{1}{T}\sum_{i=1}^{T} \rho\!\left(x_i(v)\right),
$$
### Eq 278 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
V_{\mathrm{M1}}(v) = \frac{1}{2}\Big(H_{\mathrm{obs}}(v)-H\Big)^2.
$$
### Eq 279 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
H_{\mathrm{obs}}(v)=\frac{\text{coherent mass}}{\text{total mass}},
$$
### Eq 280 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
g_{ij}(x) = 2\delta_{ij} + H x_i x_j.
$$
### Eq 281 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
g(x)=2I + H\,x x^\top.
$$
### Eq 282 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
ds^2 = \dot{x}^\top g(x)\dot{x} = 2\|\dot{x}\|^2 + H(x^\top\dot{x})^2.
$$
### Eq 283 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
A \equiv 2 + H r^2.
$$
### Eq 284 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
g^{-1}(x) = \frac{1}{2}I - \frac{H}{2A}\,x x^\top.
$$
### Eq 285 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
g^{ij} = \frac{1}{2}\delta^{ij} - \frac{H}{2A}x_i x_j.
$$
### Eq 286 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
g^{-1}x = \frac{x}{A}.
$$
### Eq 287 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\partial_k g_{ij} = H(\delta_{ik}x_j+\delta_{jk}x_i).
$$
### Eq 288 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\Gamma^k_{ij}=\frac{1}{2}g^{k\ell}\left(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}\right).
$$
### Eq 289 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\boxed{\Gamma^k_{ij}(x)=\frac{H}{A}\,x_k\,\delta_{ij}}.
$$
### Eq 290 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\ddot{x}^k + \Gamma^k_{ij}\dot{x}^i\dot{x}^j=0
\quad\Rightarrow\quad
\boxed{\ddot{x} + \frac{H}{A}\|\dot{x}\|^2\,x=0}.
$$
### Eq 291 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
R^\rho_{\ \sigma\mu\nu}
=
\partial_\mu\Gamma^\rho_{\nu\sigma}
-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}.
$$
### Eq 292 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\boxed{
R^\rho_{\ \sigma\mu\nu}
=
\delta_{\nu\sigma}\!\left(
\frac{H}{A}\delta_{\rho\mu}
-\frac{H^2}{A^2}x_\rho x_\mu
\right)
-
\delta_{\mu\sigma}\!\left(
\frac{H}{A}\delta_{\rho\nu}
-\frac{H^2}{A^2}x_\rho x_\nu
\right)
}.
$$
### Eq 293 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\mathrm{Ric}_{\sigma\nu}=R^\rho_{\ \sigma\rho\nu}.
$$
### Eq 294 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\boxed{
\mathrm{Ric}_{ij}
=
\delta_{ij}\!\left(
\frac{H(n-1)}{A}
-\frac{H^2 r^2}{A^2}
\right)
+\frac{H^2}{A^2}x_i x_j
}.
$$
### Eq 295 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
R = g^{ij}\mathrm{Ric}_{ij}.
$$
### Eq 296 (block) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$$
\boxed{
R
=
(n-1)\left(
\frac{Hn}{2A}
-\frac{H^2 r^2}{A^2}
\right)
=
\frac{(n-1)H\left[n+Hr^2\left(\frac{n}{2}-1\right)\right]}{(2+Hr^2)^2}
}.
$$
### Eq 297 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$\Delta_\pi$
### Eq 298 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$g_\pi$
### Eq 299 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$g^{-1}$
### Eq 300 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$\Gamma$
### Eq 301 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$\Psi$
### Eq 302 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$g = 2I + Hxx^\top$
### Eq 303 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$\Gamma^k_{ij}$
### Eq 304 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$R^\rho_{\ \sigma\mu\nu}$
### Eq 305 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$\mathrm{Ric}_{ij}$
### Eq 306 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$R$
### Eq 307 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$d_\pi$
### Eq 308 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$n=256$
### Eq 309 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$n=64$
### Eq 310 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$x \in \mathbb{R}^n$
### Eq 311 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$r^2 = \|x\|^2 = x^\top x$
### Eq 312 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$g_{ij}$
### Eq 313 (inline) — Nexus_PiMetric_GeodesicEngine_Complete_Spec.md
$g^{ij}$
### Eq 314 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\text{seed} \;\Rightarrow\; \Delta_\pi \;\Rightarrow\; g_\pi \;\Rightarrow\; \Gamma, R \;\Rightarrow\; \text{geodesic flow} \;\Rightarrow\; \Psi\text{-collapse}
$$
### Eq 315 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
X_{t+1} = \Psi\bigl( X_t \oplus \Delta(X_t) \bigr).
$$
### Eq 316 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\Omega \leftarrow \Delta(X_t), \qquad X_t \to \bot,
$$
### Eq 317 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
H_{\rm MARK1} = \frac{\pi}{9} \approx 0.34906585\ldots
$$
### Eq 318 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
(a,b,c) = (4,1,3).
$$
### Eq 319 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
a = b + c \quad\Rightarrow\quad 4 = 1+3.
$$
### Eq 320 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
P = a+b+c = 8.
$$
### Eq 321 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
s = \frac{P}{2} = 4.
$$
### Eq 322 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
A = \sqrt{s(s-a)(s-b)(s-c)}
    = \sqrt{4\cdot 0\cdot 3\cdot 1} = 0.
$$
### Eq 323 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\cos A = \frac{b^2+c^2-a^2}{2bc},\quad
  \cos B = \frac{a^2+c^2-b^2}{2ac},\quad
  \cos C = \frac{a^2+b^2-c^2}{2ab}.
$$
### Eq 324 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\cos A = \frac{1^2+3^2-4^2}{2\cdot 1\cdot 3} = \frac{1+9-16}{6} = -1
\Rightarrow A = \pi.
$$
### Eq 325 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\cos B = \frac{4^2+3^2-1^2}{2\cdot 4\cdot 3} = \frac{16+9-1}{24} = 1
\Rightarrow B = 0.
$$
### Eq 326 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\cos C = \frac{4^2+1^2-3^2}{2\cdot 4\cdot 1} = \frac{16+1-9}{8} = 1
\Rightarrow C = 0.
$$
### Eq 327 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
(A,B,C) = (\pi, 0, 0).
$$
### Eq 328 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
m_a = \frac12\sqrt{2b^2+2c^2-a^2},\quad
  m_b = \frac12\sqrt{2a^2+2c^2-b^2},\quad
  m_c = \frac12\sqrt{2a^2+2b^2-c^2}.
$$
### Eq 329 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
m_a = \frac12\sqrt{2\cdot 1^2 + 2\cdot 3^2 - 4^2}
      = \frac12\sqrt{2+18-16}
      = 1.
$$
### Eq 330 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
m_b = \frac12\sqrt{2\cdot 4^2 + 2\cdot 3^2 - 1^2}
      = \frac12\sqrt{32+18-1}
      = \frac12\sqrt{49}
      = 3.5.
$$
### Eq 331 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
m_c = \frac12\sqrt{2\cdot 4^2 + 2\cdot 1^2 - 3^2}
      = \frac12\sqrt{32+2-9}
      = \frac12\sqrt{25}
      = 2.5.
$$
### Eq 332 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
(m_a,m_b,m_c) = (1, 3.5, 2.5).
$$
### Eq 333 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
3.5 \approx 10\cdot \frac{\pi}{9} = \frac{10\pi}{9} \approx 3.4906585\ldots
$$
### Eq 334 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
\delta_{3.5} = 3.5 - \frac{10\pi}{9} \approx 0.0093415\ldots
$$
### Eq 335 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
r = \frac{2A}{P} = 0.
$$
### Eq 336 (block) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$$
R = \frac{abc}{4A}
$$
### Eq 337 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$(3,1,4)$
### Eq 338 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\Delta$
### Eq 339 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\oplus$
### Eq 340 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\circlearrowleft$
### Eq 341 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\bot$
### Eq 342 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$0$
### Eq 343 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\Omega$
### Eq 344 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_1 = [1,4,1,5,9,2,6,5]$
### Eq 345 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_2 = [3,5,8,9,7,9,3,2]$
### Eq 346 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_3 = [3,8,4,6,2,6,4,3]$
### Eq 347 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_4 = [3,8,3,2,7,9,5,0]$
### Eq 348 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_5 = [2,8,8,4,1,9,7,1]$
### Eq 349 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_6 = [6,9,3,9,9,3,7,5]$
### Eq 350 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_7 = [1,0,5,8,2,0,9,7]$
### Eq 351 (inline) — Nexus_PiMetric_GeodesicEngine_Expanded_Complete.md
$\text{byte}_8 = [4,5,9,2,3,0,7,8]$
### Eq 352 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
U(t)
$$
### Eq 353 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\nabla J(s) \approx 0
$$
### Eq 354 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\nabla J(s) \neq 0
$$
### Eq 355 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\dot s(t) = -\nabla J(s(t)) + \eta(t)
$$
### Eq 356 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
z_t=\frac{|\hat\alpha_t-\alpha_*|}{SE_t}
$$
### Eq 357 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
p_t=\sigma\big(\beta(z_t-z_0)\big),\qquad \sigma(x)=\frac{1}{1+e^{-x}}
$$
### Eq 358 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\hat\alpha_t=\alpha_*+\varepsilon_t,\qquad \varepsilon_t\sim\mathcal N(0,SE_t^2)
$$
### Eq 359 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
z_t=\frac{|\varepsilon_t|}{SE_t}
$$
### Eq 360 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
z_t=\frac{|SE_tZ|}{SE_t}=|Z|
$$
### Eq 361 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
z_t\sim\text{HalfNormal}(0,1)
$$
### Eq 362 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
p_t\ge p_{\text{hot}}
\iff
z_t \ge z_0+\frac{1}{\beta}\ln\left(\frac{p_{\text{hot}}}{1-p_{\text{hot}}}\right)
$$
### Eq 363 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\Pr(\text{HOT})=\Pr\left(|Z|\ge z_0+\frac{1}{\beta}\ln\left(\frac{p_{\text{hot}}}{1-p_{\text{hot}}}\right)\right)
$$
### Eq 364 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\gamma=\frac{SE_{\text{true}}}{SE_{\text{used}}}
$$
### Eq 365 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
z_t=\gamma|Z|
$$
### Eq 366 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
p_t(\gamma)=\sigma\big(\beta(\gamma|Z|-z_0)\big)
$$
### Eq 367 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
C(x,s)\in[0,1]
$$
### Eq 368 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
A(x,s)\in[0,1]
$$
### Eq 369 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
a,b,c\in\{0,1,2,3,4,5,6,7,8\}
$$
### Eq 370 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
9^3 = 729
$$
### Eq 371 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
N_{\triangle} = 260
$$
### Eq 372 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
H_{\triangle}=\frac{260}{729}\approx 0.356653
$$
### Eq 373 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
N_{\text{deg}} = 84
$$
### Eq 374 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
\pi/9 \approx 0.349066,\quad 2.5/7 \approx 0.357143,\quad 1/e \approx 0.367879,\quad 1/\varphi^2 \approx 0.381966
$$
### Eq 375 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
H\in[0.343,0.382]
$$
### Eq 376 (block) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$$
p=x_1\oplus x_2\oplus\cdots\oplus x_9
$$
### Eq 377 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$s(t)$
### Eq 378 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$J(s)$
### Eq 379 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$\alpha_*=\pi/9$
### Eq 380 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$\varepsilon_t=SE_t Z$
### Eq 381 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$Z\sim\mathcal N(0,1)$
### Eq 382 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$(\beta,z_0)$
### Eq 383 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$p_{\text{hot}}$
### Eq 384 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$SE_{\text{used}}$
### Eq 385 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$\gamma<1$
### Eq 386 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$\gamma>1$
### Eq 387 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$s$
### Eq 388 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$C\approx0$
### Eq 389 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$C>0,\ A\approx0$
### Eq 390 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$C>0,\ A>0$
### Eq 391 (inline) — Nexus_SILR_9D_Parity_and_Observer_Gradient.md
$20^\circ$
### Eq 392 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
(M, g),\qquad x \in M.
$$
### Eq 393 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
y = S_F(x).
$$
### Eq 394 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x_{t+1} = \mathcal{U}(x_t) \quad\text{with}\quad \mathcal{C}(x_{t+1})=0.
$$
### Eq 395 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
y = P(x),\qquad \dim(y) < \dim(x).
$$
### Eq 396 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x_{t+1} = \mathcal{U}(x_t) + \eta_t,\qquad \mathbb{E}\|\eta_t\|>0.
$$
### Eq 397 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
H^\star \approx \frac{\pi}{9}.
$$
### Eq 398 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x_t \in M,\qquad \hat{\alpha}_t = \alpha(x_t).
$$
### Eq 399 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
\Delta_t = \hat{\alpha}_t - \alpha^\star.
$$
### Eq 400 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
\tilde{x}_{t+1} = F(x_t, \Delta_t).
$$
### Eq 401 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x'_{t+1} = G(\tilde{x}_{t+1};\,\mathcal{N},W,\mathcal{C}).
$$
### Eq 402 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
z_t = \frac{|\hat{\alpha}_t-\alpha^\star|}{SE_t+\varepsilon}.
$$
### Eq 403 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
p_t = \sigma\!\big(\beta(z_t-z_0)\big).
$$
### Eq 404 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
X' = kX,
$$
### Eq 405 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
\mu' = k\mu,\qquad \sigma' = k\sigma,
$$
### Eq 406 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
z' = \frac{kX-k\mu}{k\sigma} = z.
$$
### Eq 407 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
z_t = \frac{|\varepsilon_t|}{SE_{\text{used}}} = \frac{|SE_{\text{true}} Z|}{SE_{\text{used}}} = \gamma |Z|.
$$
### Eq 408 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x \mapsto x^{(c)} = P_c(x).
$$
### Eq 409 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
b_{i\ell} = \mathbf{1}\{x_{i\ell} > 0\}.
$$
### Eq 410 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
p_i = \bigoplus_{\ell=1}^{d} b_{i\ell}.
$$
### Eq 411 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
x \mapsto P_\oplus(x),
$$
### Eq 412 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
a+b>c,\quad a+c>b,\quad b+c>a.
$$
### Eq 413 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
\frac{260}{729} \approx 0.356.
$$
### Eq 414 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
f_s > 2f_{\max}.
$$
### Eq 415 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
d^2(u,v) = \alpha\,H(u,v)^2 + \beta\,\Phi(\Delta_\pi(v)),
$$
### Eq 416 (block) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$$
v_{t+1} = \arg\min_{v\in\mathcal{N}(v_t)} d(v_t,v).
$$
### Eq 417 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$M$
### Eq 418 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$g$
### Eq 419 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$P$
### Eq 420 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$E_0 \neq 0$
### Eq 421 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$H^\star$
### Eq 422 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\pi/9\approx0.34906$
### Eq 423 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\mathbb{V}$
### Eq 424 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\alpha(x)$
### Eq 425 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$x'_{t+1}$
### Eq 426 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$z$
### Eq 427 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$SE_{\text{true}}$
### Eq 428 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\gamma = SE_{\text{true}}/SE_{\text{used}}$
### Eq 429 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\gamma\approx 1$
### Eq 430 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\gamma\to 1$
### Eq 431 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$\gamma\neq 1$
### Eq 432 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$c\in\{1,\dots,9\}$
### Eq 433 (inline) — Nexus_ZPHC_Funnel_Paper_Volume_I.md
$d$
### Eq 434 (block) — Published Papers.part1.md
$$
\Psi(t) = 1 - \frac{H_{\text{entropy}}(t)}{H_{\text{max}}},
$$
### Eq 435 (block) — Published Papers.part1.md
$$
\text{RCQ}(B) = \frac{N_B}{\Delta_{\text{range}}(B)},
$$
### Eq 436 (block) — Published Papers.part1.md
$$
\pi = \sum_{k=0}^\in
```

### Page 23 {#the_nexus_recursive_harmonic_framework_-_a_self-referential_and_self-governing_universemd-page-23}

```text
fty \frac{1}{16^k}\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} -
\frac{1}{8k+6}\right),
$$
### Eq 437 (block) — Published Papers.part1.md
$$
F_{grav} = H_G \frac{T_1 P_1 \; T_2 P_2}{r^2},
$$
### Eq 438 (block) — Published Papers.part1.md
$$
\textbf{UniverseState}_{n+1} =
F(\textbf{UniverseState}_n, H, \textbf{Feedback}),
$$
### Eq 439 (block) — Published Papers.part1.md
$$
S_{\text{BH}}^{\text{Nexus}} = A \cdot \theta^2 \cdot \frac{n}{64},
$$
### Eq 440 (block) — Published Papers.part1.md
$$
S_{\text{BH}}^{\text{Nexus}} = A \cdot (\Delta_{\text{harmonic}} \cdot 0.35),
$$
### Eq 441 (block) — Published Papers.part1.md
$$
L(m) = 64^3 \cdot 2^{21/m},
$$
### Eq 442 (block) — Published Papers.part1.md
$$
D(t) = \sum_i H_i \cdot F_i \cdot e^{\,i \,(H \cdot F \cdot t)} \;\prod_j B_j \;\Big(1 + \delta
H(t)\,\sin(H\,t)\Big),
$$
### Eq 443 (block) — Published Papers.part1.md
$$
F_{\text{Nexus}}(t, x, \Psi) = 0,
$$
### Eq 444 (block) — Published Papers.part1.md
$$
\frac{d\Psi}{dt} + \nabla H(x(t)) = 0,
$$
### Eq 445 (block) — Published Papers.part1.md
$$
x(t+1) =
f(x(t), \Psi(t)),
$$
### Eq 446 (inline) — Published Papers.part1.md
$e$
### Eq 447 (inline) — Published Papers.part1.md
$L$
### Eq 448 (inline) — Published Papers.part1.md
$\Psi[\mathbf{S}(t)]$
### Eq 449 (inline) — Published Papers.part1.md
$\mathbf{S}(t)$
### Eq 450 (inline) — Published Papers.part1.md
$t$
### Eq 451 (inline) — Published Papers.part1.md
$H_{\text{entropy}}$
### Eq 452 (inline) — Published Papers.part1.md
$H_{\text{max}}$
### Eq 453 (inline) — Published Papers.part1.md
$\Psi \to 0$
### Eq 454 (inline) — Published Papers.part1.md
$Q(H)$
### Eq 455 (inline) — Published Papers.part1.md
$\Psi_c$
### Eq 456 (inline) — Published Papers.part1.md
${e_i}$
### Eq 457 (inline) — Published Papers.part1.md
$\leq$
### Eq 458 (inline) — Published Papers.part1.md
$e_i \leq e_j$
### Eq 459 (inline) — Published Papers.part1.md
$e_i$
### Eq 460 (inline) — Published Papers.part1.md
$e_j$
### Eq 461 (inline) — Published Papers.part1.md
$\top$
### Eq 462 (inline) — Published Papers.part1.md
$s=1$
### Eq 463 (inline) — Published Papers.part1.md
$\bigoplus_{i=1}^r \Psi(P_i) \to \bot(r)$
### Eq 464 (block) — Published Papers.part2.md
$$
$
$$
### Eq 465 (inline) — Published Papers.part2.md
$M_2 = \text{"abc\n"}$
### Eq 466 (inline) — Published Papers.part2.md
$B(t)$
### Eq 467 (inline) — Published Papers.part2.md
$A(t)$
### Eq 468 (inline) — Published Papers.part2.md
$(11, 13)$
### Eq 469 (inline) — Published Papers.part2.md
$\phi(p)$
### Eq 470 (inline) — Published Papers.part2.md
$\text{Drag}_\pi$
### Eq 471 (inline) — Published Papers.part2.md
$\text{Drag}_\pi = \phi(13) - \phi(11)$
### Eq 472 (inline) — Published Papers.part2.md
$\Delta H_i = H_i \oplus ROTR^2(H_i) \oplus
ROTR^{13}(H_i) \oplus ROTR^{22}(H_i)$
### Eq 473 (inline) — Published Papers.part2.md
$\Delta H_i$
### Eq 474 (inline) — Published Papers.part2.md
$R_i$
### Eq 475 (inline) — Published Papers.part2.md
$T_l = T_0 \prod_{i=1}^l
R_i$
### Eq 476 (inline) — Published Papers.part2.md
$, to a multi-dimensional property vector,$
### Eq 477 (block) — Published Papers.part3.md
$$
4 m_b^2 = 2(a^2 + c^2) - b^2
$$
### Eq 478 (block) — Published Papers.part3.md
$$
4 m_b^2 = 2(16 + 9) - 1 = 2(25) - 1 = 49
$$
### Eq 479 (inline) — Published Papers.part3.md
$A$
### Eq 480 (inline) — Published Papers.part3.md
$B$
### Eq 481 (inline) — Published Papers.part3.md
$H \in [0.34, 0.36]$
### Eq 482 (inline) — Published Papers.part3.md
$H\approx0.35$
### Eq 483 (inline) — Published Papers.part3.md
$\mathbf{p} = (p_{\text{mat}}, p_{\text{cal}}, p_{\text{legal}},
p_{\text{budget}}, p_{\text{thermal}})$
### Eq 484 (inline) — Published Papers.part3.md
$\mathbf{p}$
### Eq 485 (inline) — Published Papers.part3.md
$N$
### Eq 486 (inline) — Published Papers.part3.md
$T$
### Eq 487 (inline) — Published Papers.part3.md
$\epsilon$
### Eq 488 (inline) — Published Papers.part3.md
$H = h_0 h_1 \dots h_{63}$
### Eq 489 (inline) — Published Papers.part3.md
${h_i} \in
{0,1,\dots,9,A,\dots,F}$
### Eq 490 (inline) — Published Papers.part3.md
$h_i$
### Eq 491 (inline) — Published Papers.part3.md
$t_i$
### Eq 492 (inline) — Published Papers.part3.md
$(t_0, t_1, \dots,
t_{63})$
### Eq 493 (block) — Starting fresh with a new session.md
$$
ds^2 = g_{\pi}(u, v) = \alpha \cdot H(u,v)^2 + \beta \cdot \Phi(\Delta_{\pi}(v))
$$
### Eq 494 (block) — Starting fresh with a new session.md
$$
g_{\pi}(u, v) = \alpha \cdot H(u,v)^2 + \beta \cdot \Phi(\Delta_{\pi}(v))
$$
### Eq 495 (block) — Starting fresh with a new session.md
$$
\mathcal{S}[\gamma] = \int \sqrt{g_{\pi}(\dot{\gamma}, \dot{\gamma})} dt
$$
### Eq 496 (block) — Starting fresh with a new session.md
$$
\n", "M(t) = \\text{Frame}(\\mathcal{F}_t) = \\{ a_i \\mid Q(H(a_i)) = 1 \\}\n", "
$$
### Eq 497 (block) — Starting fresh with a new session.md
$$
\n", "\\Delta T = \\sum_{i=1}^{n} \\Delta Q(H(a_i))\n", "
$$
### Eq 498 (block) — Starting fresh with a new session.md
$$
\n", "H_n = \\text{SHA256}(\\text{SHA256}(H_{n-1} \\parallel N_n))\n", "
$$
### Eq 499 (block) — Starting fresh with a new session.md
$$
\n", "\\pi_k = \\text{BBP}(k),\\quad k = H_n \\bmod N\n", "
$$
### Eq 500 (block) — Starting fresh with a new session.md
$$
\n", "\\vec{R}_n = \\mathcal{F}^{-1}(\\pi_k \\cdot \\text{Filter}_Q)\n", "
$$

_(Catalog truncated to first 500 unique expressions out of 892. Ask to export full list if needed.)_


---
