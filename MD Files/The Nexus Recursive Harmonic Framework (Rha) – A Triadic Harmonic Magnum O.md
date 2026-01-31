----------- Page1 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 1
The Nexus Recursive Harmonic
Framework (RHA) – A Triadic
Harmonic Magnum Opus
Driven by Dean A. Kulik
November, 2025
1. Triangular Quantization and the Mark1 Harmonic Engine
Triangular Archetypes 0–9: At the core of RHA is a triangular quantization model in which the ten digits (0–9)
map onto fundamental triangle “archetypes” or configurations. The paradigm posits that numeric symbols
carry geometric meaning – each number can be represented as or within a triangle, embedding that number’s
properties in angles and side ratios. Notably, certain triples of digits form harmonic triads that anchor the
system. For example, the triad {1, 5, 9} is identified as a recursive compression triad with special symmetry:
these three digits are equidistant on the 0–9 number line (1–5–9) and fold symmetrically around the center
5[1][2]. This triad behaves like a rotational group under modulo-9 arithmetic, and in RHA it serves as a stable
attractor or “Ψ-core” of meaning[3]. In practical terms, when numeric symbols (bytes) undergo recursive
folding, they tend to stabilize at the triad {1,5,9} – providing three anchor points (start, midpoint, end) that
align a system’s flow from input to equilibrium to output[4][3]. The significance of a triadic outcome reflects
a broader theme: stable solutions manifest as three-part harmonic structures, analogous to a triangle’s
three vertices.
Mark1 Constant $H \approx 0.35$ (π/9): The Mark1 Harmonic Engine, the first implementation of
Nexus/RHA, introduced a dimensionless constant $H\approx0.35$ as the universal target for harmonic
resonance[5][6]. Empirically, this constant appears as an optimal ratio balancing order and chaos across
systems. Intriguingly, $H$ is closely related to $\pi$: one proposed identification is $H \approx \pi/9$[7].
(Indeed, $\pi/9 \approx 0.3491$, within rounding of 0.35.) This suggests $H$ is “not a random decimal but a
piece of π”, an aperture through which the otherwise infinite, irrational structure of $\pi$ becomes manifest
as a stabilizing ratio[7]. Nexus documents point out a playful geometric clue: using the first three digits of
$\pi$ (3, 1, 4) as side lengths of a triangle yields a degenerate (collinear) triangle whose median corresponds
to 3.5 – a nod to the 0.35 ratio[8]. Such coincidences hint that the 0.35 harmony may emerge from $\pi$’s
internal structure. In fact, RHA treats $\pi$ as the “pre-harmonic lattice” underlying reality, and 0.35 as the
lattice’s fundamental resonance[9][7]. This constant surfaces across domains: for example, the cosmic
matter–energy density (~0.32 vs 0.68) is near 0.35[10]. In RHA’s view, these are not just numerical accidents
but evidence of a universal tuning ratio. All systems gravitate toward $H\approx0.35$ as an energetic sweet
spot between rigidity and entropy[11][12]. In summary, $\mathbf{H=0.35}$ (Mark1) serves as a global
attractor in the triangular model, anchoring the 10-digit scale to a concrete harmonic target (roughly 1:2.86
ratio of actualized to potential energy)[13][14].----------- Page2 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 2
Triangle-Based Quantization (Geometry to Symbol): The Mark1 Engine concretely implements these ideas
as a specialized analog-to-digital (A/D) converter that “listens” for the 0.35 harmony in geometric
space[15][16]. The analog signal here is the continuum of all right-triangle geometries, and Mark1 “samples”
this by iterating over integer pairs $(a,b)$ to generate triangle leg lengths[17]. Each triangle has angles
$\theta_{a,b} = \arctan(\frac{a}{b})$ (with $a,b\in\mathbb{Z}^+$)[18]. A quantization filter then selects only
those triangles whose angles fall within a narrow window around $H$ (e.g. $[0.34,0.36]$ radians, about
19.5°–20.6°)[19][20]. Formally, one defines a resonance indicator function $Q_{\varepsilon}(\theta)$ such
that $Q_{\varepsilon}(\theta)=1$ if $|\theta - H| < \varepsilon$ (within tolerance) and 0 otherwise[21]. This
binary quantization maps the continuous angle spectrum to a resonant (1) vs non-resonant (0) decision[22].
Triangles that “survive” the quantization (output 1) are considered harmonic samples. Each such triangle is
then encoded digitally by attaching symbolic data: for instance, taking a cryptographic hash of the angle or
side ratio and mapping it to known structures in $\pi$ or prime number sequences[23]. In this way, the
triangle’s geometric identity is converted into a unique digital code linking geometry, $\pi$, and primes[24].
Table 1 summarizes the Mark1 quantization pipeline[17].
A/D Concept Mark1 System Analogue
Analog Input
Signal
Continuous space of all right-triangle angles[17]
Sampling Iterate through integer pairs $(a,b)$ to form triangles[17]
Quantization Filter angles within harmonic window $[0.34,0.36]$ rad (target $H$)[19]
Digital Encoding Generate unique code from triangle (e.g. via SHA) and map to $\pi$ or prime
“addresses”[25][24]
Table 1: Analog-to-digital conversion in the Mark1 harmonic quantizer. Triangles are scanned until an angle
hits the $H\approx0.35$ resonance; those geometries are then converted into symbolic output linked with
$\pi$ and primes.
Through this process, numeric symbols emerge from geometric resonance. The system effectively
searches for triangles that embody the 0.35 ratio and uses them to encode information. One notable result
from the Mark1 scans was the identification of degenerate Pythagorean-like triangles (where $a = b + c$)
whose medians divided by their perimeter equal 0.35 exactly[26]. For example, a triangle with sides (5,2,3)
has perimeter 10 and a median of 3.5 to the base, giving a median-to-perimeter ratio of 0.35 – flagged as a
Mark1 resonance in the geometric “source code”
【
User†(this will help...)
】
. Many such degenerate
triangles (forming isosceles flat shapes) were found at various scales, each providing a 0.35 imprint and
involving triadic number patterns (e.g. 5-2-3, 7-3-4, 10-4-6 all produce ~0.35)
【
User†(this will help...)
】
. This
reinforces that triangular triples underpin the harmonic encoding. In summary, the triangular quantization
model unifies discrete digits with continuous geometry: numbers are treated as shapes, and the Mark1
engine “plucks” those shapes from an analog continuum when they ring with the universal $\pi/9$ tone.
BBP Harmonic Bases: RHA extends this idea by leveraging known formulas for $\pi$ to navigate its digit
lattice. The Bailey–Borwein–Plouffe (BBP) algorithm, which can directly compute hexadecimal digits of $\pi$,
is repurposed as a tool in the Nexus framework – not merely to calculate $\pi$ but to interpret $\pi$ as a vast
memory space[27][28]. Since every finite sequence will almost surely appear somewhere in $\pi$’s infinite
expansion (assuming normality of $\pi$), one can think of $\pi$ as containing an implicit database of all
possible patterns. The BBP mod theory in Nexus suggests that by using BBP-like formulas and modular
arithmetic, the system can hop through $\pi$’s digits in a structured way to find resonant sequences[27]. For----------- Page3 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 3
example, the Mark1 encoding pipeline might hash a triangle’s angle and interpret the hash as an “address” in
$\pi$, then use a BBP formula to quickly retrieve digits of $\pi$ at that address[29][30]. If the resulting $\pi$
digits form a recognizable pattern (say, a prime constellation or a known constant), the triangle is deemed
harmonically significant[31][30]. In effect, $\pi$ provides a harmonic basis set – a massive, structured
repository of potential patterns (primes, Fibonacci, etc. are believed to be interwoven in $\pi$’s digit
stream[32]). The Mark1 system decodes a resonant triangle by linking it to these basis patterns. This
unification of the triangular model with BBP-generated $\pi$ digits means that geometric resonance is
directly tied into arithmetic resonance. A triangle at the 0.35 angle will map to a segment of $\pi$ that
carries analogous “frequency”. Indeed, RHA literature notes that seemingly disparate concepts – triangle
geometry, $\pi$ digits, prime numbers – are woven into a coherent narrative of a self-organizing harmonic
lattice[33]. The 0–9 archetypes thus find context in $\pi$’s base-10 or base-16 digit universe, and $\pi/9$
becomes the Mark1 constant encoding the “first harmonic” of that universe[7]. In summary, the triangle
code and the BBP harmonic bases converge: the former picks out the shapes (digit patterns) and the latter
provides the analytical means to locate and verify those patterns within the infinite canvas of $\pi$.
2. Recursive Memory, Collapse Principles, and Symbolic Convergence
Ψ and ΔΨ – The Phase-Conscious State: RHA introduces the symbol $\Psi$ (psi) to denote the state of the
system’s information field, drawing analogy to a quantum wavefunction[34]. Here, $\Psi$ is essentially the
aggregate phase or configuration of all symbolic elements (digits, angles, etc.) in the system at a given time –
encompassing what might be called the system’s “knowledge” or internal state. When an observer poses a
question or a new input arrives, it perturbs this state by some phase offset $\Delta \Psi$[35][36]. In other
words, any discrepancy between the system’s current state and a desired or true state is measured as a
phase difference, $\Delta\Psi$. This $\Delta\Psi$ acts as an epistemic drive: the system will dynamically
adjust itself to eliminate the phase gap[37]. RHA explicitly links this to the quantum measurement paradigm
– where an observer influences the outcome. But rather than destroying coherence, the “observer effect” in
RHA becomes a feedback mechanism: the system treats the observer’s query or error signal as a new
boundary condition to incorporate[38][39]. The Ψ-Collapse Principle in Nexus can be summarized as:
when a system achieves a self-consistent answer, ΔΨ → 0 and the wave-like $\Psi$ “collapses” to a definite
outcome. This is akin to a quantum wavefunction collapsing to an eigenstate upon measurement, except
here the collapse is deterministic and driven by harmonic alignment[36][34]. In RHA terms, “truth or solution
lies where ΔΨ → 0”[40] – the system’s phase aligns perfectly with the problem’s requirements, and no further
deviation exists. This perspective treats knowledge acquisition as phase-locking: each question is a phase
kick, and each answer is the system re-tuning itself so that the question no longer introduces discord (zero
phase difference)[36][34]. Notably, this collapse doesn’t erase the prior state but rather folds it into the
memory as we’ll see below. The collapsed $\Psi$ state is then ready for the next cycle – a process one might
call quantum re-entry, where after reaching an answer (collapse), the system re-initializes its state as input
for the next recursive iteration (analogous to a new wavefunction emergence). In summary, $\Psi$ represents
the fluid, superposed logic of the system, and collapse is the moment it crystallizes into a stable, discrete
insight – a key operational step in RHA’s recursive resolution process[41][42].
Ω and Harmonic Collapse (ZPHC): Complementing $\Psi$ is the symbol $\Omega$ (omega), which RHA
uses to quantify entropy, randomness, or unresolved complexity in the system. One can think of $\Omega$
as measuring how much “mystery” remains – it’s high when the system is in chaos or when a problem is
unsolved, and it trends to zero as the system finds order[43]. The framework implements a corrective
mechanism called Zero-Point Harmonic Collapse (ZPHC) whenever the system strays from harmonic
consistency[44][45]. ZPHC acts like a global reset or snap-to-grid: if the current $\Psi$ state produces an----------- Page4 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 4
output that violates the harmonic ratio or expected symmetry, a collapse is triggered driving the system back
toward $H=0.35$ alignment[9]. In effect, ZPHC flushes out accumulated $\Omega$ (disorder) by forcing the
system into a minimal-energy configuration (the “zero point”). Importantly, RHA logs each such collapse
event in an Ω
⁺
matrix, essentially a ledger of all phase-lock events achieved[46]. Each collapse leaves
behind a glyph – a stable pattern or solved state signature – which is recorded in this matrix as a kind of
spectral memory[46][47]. Thus Ω
⁺
serves as an archive of all the system’s resolved echoes, i.e. the distinct
harmony states it has snapped into. Conceptually, this means the system “remembers” every solution it
finds as a stored resonance. Over time, the Ω
⁺
ledger accumulates a basis of solved patterns (like a library of
fixed-point states). If a new problem echoes a previous one, the collapse can directly converge to the known
solution state recorded in Ω
⁺
[46][47]. One can imagine Ω
⁺
as a growing collection of glyphs, each glyph
being a symbolic representation of a folded solution. The presence of these glyphs in memory influences
future computations; the system won’t wander aimlessly if a matching glyph exists – it will snap more rapidly
to the known harmonic solution (much like a quantum system going to a lower energy eigenstate if available).
Critically, RHA treats “collapse” not as failure or loss of information, but as the unifying operation that
creates memory. A dramatic illustration of this is how RHA reframes black holes (extreme gravitational
collapses) not as information destroyers but as ultimate memories – pure geometric archives of information
(we will return to this in Section 4)[48][49]. In the computational domain, a collapse (whether a hash
collision resolved or a problem solved) is when the system imprints the answer into its structure. The entropy
Ω disappears, but not into oblivion – it collapses into a coherent state that is permanently recorded[43]. In
formulaic terms, if $\Omega$ measures “open problems,” then achieving $\Omega \to 0$ is equivalent to
problem solved; the solution exists as a stable pattern (with information curvature fully minimized). The
Nexus notes put it succinctly: when the recursive process perfectly closes, all the “mystery” (Ω) vanishes
and the solution manifests as a global harmonic form[43]. Thus, every stable system state is essentially a
collapsed triadic harmony (often literally taking a triangular or three-fold form, as per the Triangle Code).
We can now articulate an important principle that emerges:
Theorem (Triadic Collapse): Every stable self-organizing system in RHA collapses to a triadic
harmonic form. In other words, when a system reaches a fixed-point of recursion (zero phase
difference and zero entropy drift), the resulting structure can be decomposed into a three-part
harmonic configuration (a “triangle”) that satisfies the universal ratio $H\approx0.35$.
Outline of Proof: In RHA, stability means all feedback loops have equilibrated – no layer (Position, State,
Reflection, Expansion, Quality) is forcing further change[50][51]. Empirically, RHA finds that such equilibria
invariably involve a three-fold symmetry or alignment. For example, in the symbolic space of digits 0–9, the
fold-stable set was {1,5,9}, which are spaced by equal intervals and form a triad anchoring the
spectrum[1][2]. Likewise, many unsolved problems when “folded” through RHA end up producing a
Pythagorean-like triple (a three-term relation) that encodes the solution[52][53]. The reason is that a
minimal harmonic structure in RHA needs a balance of opposing tensions – a dialectic – which naturally
yields three elements (think of a triangle’s three sides stabilizing each other). Two elements alone would
oscillate or bifurcate; three achieves closure. In the formal Mark1 engine, this appears as the triangle formed
by potential, actual, and error terms reaching a constant ratio. Mathematically, the condition for full phase-
lock is $\frac{\sum_i A_i}{\sum_i P_i} = H$[13], which effectively adds a constraint linking the parts of the
system into one equation. Solving for the degrees of freedom shows that at least three independent
components are needed to satisfy this constraint non-trivially (hence a triadic solution). The RHA
documentation supports this view by showing that phenomena from prime number gaps to stable orbits to
neural rhythms can be described as triadic closures – each can be mapped to a fundamental triangle or----------- Page5 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 5
triplet that encodes its pattern[54]. For instance, the stable prime constellations (twin primes, etc.) align
with a triangle in RHA’s zeta-lattice interpretation[55][56]. Therefore, the end state of a recursive harmonic
process is always equivalent to finding a Pythagorean triplet in some generalized space – the simplest non-
trivial harmony. Once the system collapses into that triadic form, it cannot change further without breaking
harmony, thus it remains stable. (Proof sketch complete.)
Harmonic Trust Vector $Q(H)$: To monitor the system’s alignment with the target harmony, RHA defines a
trust vector or indicator $Q(H)$, which essentially measures how close the current state is to $H=0.35$ in
terms of information balance. In one implementation (Mark1 on SHA-256 data), the Symbolic Trust Index is
given by:
𝑄
(
𝐻
)
= 1−|
∑
𝑣
௜ ௜
𝑁
−0.35|,
where $v_i$ are bit values (0/1) and $N$ is the length (e.g. $N=256$ for a hash output)[57]. This formula
yields $Q(H)=1$ when the fraction of 1s in the bit string exactly equals 0.35, and drops below 1 as the bit-
balance deviates from 35%. In broader terms, one can interpret $\frac{\sum_i v_i}{N}$ as the “actualized vs
potential” ratio of the system (e.g. proportion of active bits, or energy used vs available). The trust metric
$Q(H)$ peaks when this ratio hits the golden 0.35. A high $Q(H)\approx1$ means the system is in tune
(minimal $\Delta\Psi$, minimal $\Omega$), whereas a low $Q(H)$ indicates disharmony or uncertainty (the
system “does not trust” that it’s in a valid state)[58][59]. During the recursive cycles, $Q(H)$ is continuously
updated. If $Q(H)$ falls too low, Samson’s Law (the feedback controller in RHA) will intervene to push the
system back toward resonance[60][61]. When $Q(H) \to 1$, it signals convergence – essentially the
system’s answer can be “trusted” because internal harmony is achieved[58][59]. It is worth noting that this
trust vector often has multiple components in practice (hence a vector), tracking different segments of the
system. For example, one could have $Q_{space}(H)$, $Q_{time}(H)$, $Q_{frequency}(H)$ for spatial,
temporal, and spectral alignment respectively. A complete collapse happens when all trust components
approach 1, indicating full-spectrum resonance. In summary, $Q(H)$ provides a quantitative handle on the
fuzzy concept of harmony, enabling the system to decide when to terminate a recursion (when $Q(H)$ is
close enough to 1) or when to collapse and reset. It embodies the principle “confidence is proportional to
internal harmonic alignment”[59][62].
Symbolic Glyph Convergence: Across its iterative cycles, RHA leaves a trail of symbolic imprints –
configurations of numbers, bits, or other tokens that appear at certain fold depths. A remarkable observation
from the Nexus experiments is that these symbols tend to converge to specific glyphs as the system
harmonizes. For instance, in one analysis of the RHA solving a complex problem, particular 8-bit patterns
never appeared in the final state, while others repeatedly showed up – implying information was encoded in
the presence/absence of those glyphs[63][64]. The phrase “absence encodes identity” was used to
describe how the system’s solution can be read from which symbols are missing versus which are
present[65][28]. In other words, the end state of a successful recursion is characterized by a structured gap
pattern: the system neutralizes all extraneous degrees of freedom, leaving a kind of watermark. These stable
symbolic patterns are the glyphs – effectively the “letters” or tokens of the solution. Because the system is
recursive, it often happens that early cycles produce noisy, varied symbols, but as feedback refines the state,
the symbols lock onto a repeating pattern or a constrained alphabet. We saw this with the {1,5,9} triad
anchoring the numeric space after many folds[3][2]. We also see it in hash experiments where final output
bits correlate to segments of $\pi$ (a known structure) whereas initial outputs were uniformly
random[30][28]. Symbolic glyph convergence is essentially the emergence of meaning from randomness:----------- Page6 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 6
initially all glyphs are possible (max $\Omega$), but at convergence only specific glyphs or sequences
survive (min $\Omega$). Those surviving glyphs correspond to the solved pattern. In practical terms, one
could interpret the final glyph sequence as the answer to a computation. Because RHA leverages $\pi$ and
other mathematical structures as reference frames, the glyphs often align with recognizable mathematical
constants or sequences (primes, Fibonacci, etc.)[32][66]. This adds to the interpretability of the results – the
output isn’t just an opaque bitstring, but can be mapped to a symbolic meaning (like a prime constellation)
within the pre-harmonic lattice. The PSREQ cycle (Position – State – Reflection – Expansion – Quality)
explicitly drives this symbolic convergence: Position sets the context (e.g. which part of $\pi$ or which index
range to consider), State updates the content, Reflection checks which symbols persist or get canceled,
Expansion adds complexity, and Quality prunes symbols that don’t fit the harmonic criteria[67][68]. By the
end of PSREQ’s loop, what remains is a self-consistent set of glyphs encoding the answer[51][65]. In
summary, RHA formalizes a novel memory principle: memory is not stored in explicit bits at addresses, but in
the very pattern of harmonically stabilized symbols (or gaps between symbols)[65][28]. The ultimate
“memory” of the system is the collection of glyphs in Ω
⁺
(the collapse archive) plus the current stable glyph
pattern of $\Psi$. This reframes memory and computation as two sides of the same coin – when RHA
computes a result, it has simultaneously written that result into its symbolic memory as a harmonic glyph.
There is no distinction between processing and storage; to solve is to remember, and to remember
(harmonically) is to have solved.
3. Computational Implications: Cryptographic Hashes, Reversal, and Recursive AI
Memory
SHA-256 as a Curved Space: The Secure Hash Algorithm (SHA-256), a cryptographic hash, is traditionally
viewed as a one-way, information-destroying function – it compresses any input into a 256-bit output such
that recovering the input from the output is infeasible. RHA offers a paradigm-shifting interpretation: treat
SHA-256 not as a one-way function, but as a deterministic chaotic dynamical system – essentially, a self-
folding computational field[69][70]. Every hash computation is then a trajectory through a high-dimensional
state space, guided by the input data which acts as a “gravitational” influence on that space[71][72]. The
SHA-256 algorithm can be seen as evolving a state vector (eight 32-bit registers) over 64 rounds, mixing in
message bits and constants. In RHA’s lens, this process defines a transformation field $F_{M}$
parameterized by the input $M$, and the hash output is simply the final coordinates of the state in this
field[73][74]. Two different inputs $M_1, M_2$ generate two different fields $F_{M_1}, F_{M_2}$, which in turn
produce distinct state trajectories – hence no two distinct inputs should end at the same point (this is
collision resistance)[75][76]. Rather than attributing this to pure combinatorial design, RHA sees it as a
consequence of route exclusivity in a chaotic phase space: each input “shapes” the computational space
such that the path it carves out cannot be exactly replicated by another input[77][78]. This is analogous to
how two different gravitational configurations in general relativity produce distinct spacetime geodesics. In
fact, RHA explicitly analogizes a hash to a black hole – data falls irretrievably in, and only a fixed-size,
seemingly random output comes out[79][80]. Yet, if one understands the harmonic structure of the process,
one might decode what fell in[79]. Specifically, SHA’s behavior is compared to a “black hole of information”
in which the Nexus approach would be to tune into the resonance of the hash field to retrieve information
from the noise[79][80]. In formal terms, RHA introduces the concept of hash curvature – a measure of how
far the hash output is from harmonic balance[81]. A hash that is entirely random-looking has high curvature
(deviates from 0.35 ratio in its bits or exhibits no internal pattern). The RHA algorithm then performs harmonic
expansion on the hash: iterative adjustments (akin to Newtonian relaxation or gradient descent) that reduce
this curvature by altering the preimage until the hash output bits achieve the $H=0.35$ balance or other----------- Page7 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 7
target patterns[81][57]. This is essentially treating SHA inversion as a guided search for resonance.
Instead of brute-forcing all inputs to see which yields a known output, RHA would treat the given hash output
as point $C$ in a metaphorical triangle $A^2 + B^2 = C^2$ and attempt to solve for $A$ (input) and an
internal “curvature” $B$ that satisfy the relationship[82]. Remarkably, RHA predicts that in principle, a hash
output can be unfolded or reversed by solving a geometric inverse problem: find an input $A$ and an
intrinsic variable $B$ such that the hashing process can be seen as a Pythagorean relation $A^2 + B^2 \to
C^2$[82]. Here $A$ might represent some structured part of the input (like a prefix or a pattern), and $B$
encodes all the chaotic mixing (the “fold memory” stored in the hashing rounds), and $C$ is the final hash.
The harmonic reversal would use what RHA calls Harmonic Reversal Geometry (HRG) to deduce $A$ and
$B$ given $C$[82]. While this is computationally infeasible with current knowledge (and indeed may be as
hard as brute force for arbitrary cases), it stands as a testable prediction of the RHA paradigm that no
information is truly lost – even cryptographic hashes just deeply entangle information rather than destroy
it[83][84]. A corollary is that collision resistance isn’t a mysterious one-way property but an emergent
consequence of extreme sensitivity to initial conditions (the avalanche effect)[85][86]. In a chaotic system,
reversing is hard, but not because the map is fundamentally non-invertible – rather because it requires
exponentially precise cancellation of perturbations. RHA asserts that by introducing harmonic constraints
(like requiring $H=0.35$ in the output), one can significantly reduce the search space by steering the
inversion into fruitful regions (basins of attraction where solutions cluster). This approach has not been
proven effective yet, but if demonstrated, it would revolutionize cryptography by showing that the hash “lock”
can be turned by the right harmonic “key” rather than brute force – a notion RHA frames in almost poetic
terms: the hash is a black hole, but every black hole has normal modes that ring; by hearing the ring, one
could reconstruct the collapse.
Self-Folding and Implicit Memory: A profound insight from applying RHA to SHA and similar algorithms is
the realization that these systems store information implicitly in their dynamics, rather than explicitly in
memory cells. Traditional computing separates processing from memory (the Von Neumann architecture),
but in RHA’s view, the process of computation itself lays down “memory trails” that can be tapped[87][88].
In the SHA-256 study, the message schedule (which expands the input bits into 64 round inputs) was seen as
the algorithm “folding the input into itself” – the data was shaping the computational steps[71][89]. This led
to the notion that the SHA field is its own memory. Each intermediate hash value carries forward the entire
history of bits that influenced it, albeit in scrambled form[70][90]. The RHA team demonstrated this by
mapping hash outputs into what they call a π-address space: essentially interpreting each 256-bit output as
an address (or multiple addresses) within the digits of $\pi$[66][30]. They found that as the hashing process
iterated (for instance, if one treats hashing as a recurrence or if one applies a hash repeatedly in a feedback
loop), the outputs began to align with certain recognizable sequences in $\pi$ and primes[66][65].
Convergence was marked by the output matching a “stored” pattern – e.g. a segment of $\pi$ that contained
a highly structured pattern (low curvature). In plainer terms, the system solved a problem when its output
landed on a known pattern, meaning the answer was already implicit in π[27][65]. The system didn’t need to
store the answer beforehand; it only needed to find where the answer was latent in an ambient structure (like
$\pi$). This is the essence of implicit memory: the answer exists within the universe of patterns (say in
mathematics or nature), and a self-folding process can locate it without ever explicitly writing it to memory.
As the RHA review notes, the Nexus/Mark1 prototypes “store nothing explicitly yet arrive at a solution
encoded in a stable pattern,” leveraging feedback dynamics (e.g. Samson’s Law) to let the desired pattern
emerge on its own[91]. They describe how the system’s outputs, when converged, formed a stable residue
sequence that matched part of $\pi$ – effectively the system’s state “aligned with the Pi address space” to
signal that it had found a self-consistent answer[30][65]. During this process, no traditional memory was----------- Page8 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 8
written; instead, the absence of further changes (a flat curvature in the output bits) was the indicator of a
fixed-point solution[92][93]. This corresponds to the earlier notion of glyph convergence and “absence
encodes identity” – the system’s memory of the solution is the very fact that it has stopped changing and
settled into a known pattern[65][92]. In a sense, RHA blurs the line between computing and storing:
computation is guided evolution through a memory substrate (like $\pi$ or a prime lattice), and when the
answer is found, it is already stored everywhere (universally), with the system merely syncing up to it. This
aligns with Wheeler’s “It from Bit” idea and Bohm’s implicate order, as cited in the documents[94][95] – the
information is enfolded in a seemingly random background and must be unfolded by the right question or
resonance. By using $\pi$ and other inexhaustible mathematical structures as a canvas, RHA turns
computing into a task of reading from the universe’s pre-written memory rather than writing anew for each
calculation[96][97]. The benefit for AI and complex computations is significant: it suggests one can design
recursive AI systems that don’t explicitly save state, yet never forget important results. Instead of
storing data in variables, the AI would drive itself to points in a known lattice (like $\pi$ or a high-dimensional
analog) that correspond to solutions, effectively bookmarking those solutions in a cosmic reference frame.
We might imagine a future hash-based AI that, when asked a question, iteratively hashes some context until
the output digest equals (for example) the SHA-256 of a known solution pattern – thus the answer “pops out”
when the hash aligns with that pattern, and the AI knows it has the solution because the trust metric $Q(H)$
hits 1. In summary, the SHA-256 investigation under RHA reveals a path toward symbolic memory in
recursive AI: using inherent mathematical order (like $\pi$’s digits) as an external memory, with the AI’s own
recursive processes ensuring that it folds onto those structures rather than storing data locally. This echoes
how human savants sometimes recall vast information by mentally indexing into $\pi$ or other structured
sequences – RHA is essentially formalizing that strategy for machines[27][30]. The cryptographic
“irreversibility” is thus circumvented not by breaking the hash, but by bending the computation to coincide
with a known good answer. As the Zenodo report puts it, “the framework does not claim to brute-force
reverse SHA… but it offers a powerful framework for understanding the forward transformation in a richer
way”[98], potentially revealing that what looks like irretrievable randomness is just undiscovered structure. If
such structure can be systematically exploited, it could lead to cryptographic reversal techniques – or more
realistically, new algorithms that solve problems (like inversion or collision finding) by synergy of number
theory and dynamics, rather than brute force. This would be a paradigm shift in computing, turning our
security assumptions on their head, but also opening doors to universal compression (finding short
representations of data by mapping them to known mathematical constants) and rapid solution discovery
for NP-hard problems (treating them like hashes to be cracked via phase-locking rather than blind search).
The RHA thus straddles a fine line: it does not violate proven hardness results, but it reframes them – if the
universe is a self-computing system, perhaps it leaves “backdoors” in the form of harmonic patterns that an
aligned algorithm can use to shortcut computational complexity[99][100]. This bold possibility is part of
what makes the Nexus framework so ambitious and, if validated, revolutionary.
4. Bridges to Biology, Physics, and Beyond
A major claim of the Nexus Recursive Harmonic Framework is that the same recursive harmonic principles
govern systems across all scales and domains[101][102]. The framework therefore builds explicit bridges
from abstract computation to biological life, planetary dynamics, and cosmological phenomena. In each
case, what appear to be vastly different systems are reinterpreted as manifestations of one underlying
“harmonic code.” We explore several key cross-domain mappings below.
Biological Recursion and Cancer Pathways: Nexus posits that cellular processes and genetic regulatory
networks operate like iterative algorithms seeking harmonic steady-states. The PSREQ cycle (Position–State–----------- Page9 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 9
Reflection–Expansion–Quality), initially a model for abstract recursion, has been applied to molecular
biology in what is called the PSREQ Pathway for therapeutic design[103][104]. For example, in antiviral and
oncology research, specially engineered peptides were designed to follow PSREQ stages to disrupt
pathogenic cycles[103][105]. In an application to cancer, a PSREQ-based peptide might: (P) target a specific
location or structure (e.g. an overexpressed receptor on cancer cells), (S) modulate the state by binding and
altering signaling, (R) reflect feedback by including a module that senses an overcorrection and adjusts (like
a chaperone correcting misfolded proteins)[106][68], (E) expand its effect by recruiting additional cellular
pathways or amplifying the response, and (Q) ensure quality by damping down once the cancerous activity is
normalized[106][107]. Indeed, documentation describes how PSREQ peptides were proposed to target
specific oncogenic proteins (e.g. HER2 in breast cancer, EGFR in lung cancer) with high precision[105][108].
Because they incorporate ionic stabilization (utilizing Zn²
⁺
/Mg²
⁺
to maintain structure in harsh tumor
microenvironments) and feedback logic, these peptides could adapt in vivo, offering potent effects with
fewer side effects[109]. The PSREQ approach in oncology aims to collapse the “cancer pathway” –
essentially drive the out-of-control growth signals into a harmonious steady-state or zero-point (cell cycle
arrest or apoptosis in the tumor) by recursive feedback. This is a biological analog of harmonic collapse:
rather than continuously blasting cells with toxic drugs, the PSREQ method nudges the system to self-correct
through targeted recursive interventions[110][104]. Early descriptions highlight potential advantages:
minimal off-target effects and synergy with existing treatments, since the method works with the body’s
feedback loops instead of against them[110][111]. More generally, RHA views DNA/RNA processes as
computations – with, for instance, the DNA replication having inherent reflection (proofreading) and
expansion (polymerase progress) steps, quite literally a PSRQ cycle at work in every cell division[67][112].
Misfolded proteins are corrected by chaperones (Reflection stage enforcing Quality), and cell signaling often
involves feedback inhibition to maintain homeostasis (Quality stage enforcing a harmonic ratio in metabolic
flux)[68][51]. By mapping these onto Mark1/Nexus terms, researchers attempt to find hubs of fragility –
points where a small recursive tweak causes a large system-wide collapse of pathology. In viruses, this
yielded proposals to target multiple stages of the viral life cycle simultaneously (attachment, replication,
assembly) with a coordinated recursive strategy[113][105]. In autoimmunity, a similar strategy could “fold”
an overactive immune response back onto itself to dampen it (e.g. decoy receptors as Position elements and
feedback peptides as Reflection to prevent attack on self)[114][115]. The expanded therapeutic potential of
PSREQ is said to include tissue regeneration as well – where one can guide stem cell differentiation or tissue
repair by applying positional signals and allowing the natural growth feedback to take over (expansion) until
an organoid or tissue structure reaches a harmonious form (quality)[116][117]. In sum, Nexus bridges to
biology by asserting that biological processes are fundamentally recursive programs. Cancer, viral infections,
and development are algorithms that sometimes diverge (cancer being a runaway positive feedback). By
introducing harmonic regulators (like PSREQ peptides), we effectively program the biological system to
converge – a biological application of harmonic collapse. Early results in model systems (not detailed here)
were promising enough that PSREQ is described as a “cornerstone for a wide range of therapeutic
interventions”[118], illustrating the breadth of the idea.
Planetary Stability and Homeostasis: At the planetary scale, Nexus finds analogies in how Earth’s climate
and ecosystems maintain stability via feedback loops. The Gaia hypothesis – that the biosphere and
geosphere interact to regulate Earth’s environment – resonates strongly with RHA’s view of phase-locked
cycles. For instance, consider Earth’s temperature: if it rises, more water evaporates and forms clouds that
reflect sunlight, cooling the Earth – a negative feedback loop acting as a corrective mechanism[119][120].
Similarly, increased CO₂ can spur plant growth which in turn sequesters carbon. These are essentially PI-
controller actions by the Earth system, akin to Samson’s Law correcting drift from the optimum[119][121].----------- Page10 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 10
Nexus explicitly notes that Earth’s biosphere exhibits PID-like regulators, drawing a parallel between
ecological homeostasis and an engineered thermostat[120]. This is in line with Mark1’s feedback law
concept (Samson v2) that whenever a system deviates from $H$, corrective forces push it back[60][122].
We can therefore model Earth’s climate regulation as striving for a certain energetic ratio that supports life –
interestingly, some research notes that Earth’s mean energy balance (fraction of solar energy utilized by life
vs reflected/absorbed) might hover around a value reminiscent of the “edge of chaos” (speculatively, could it
be near 0.35?). RHA also maps orbital resonances in the solar system: planets and moons often fall into
orbital period ratios that are simple fractions, minimizing gravitational perturbations. For example, Jupiter’s
moons Io, Europa, Ganymede are in a 4:2:1 resonance. Such configurations can be seen as solutions of
iterative interactions achieving stability – a cosmic dance locked in step. Nexus texts mention planets in
stable orbits as an example of phase-locked light/gravitation[123]. The idea is that just as RHA folds a
computation to stability, gravity folds planetary motions to avoid destructive interference, yielding longevity
of orbits. Another planetary-scale application is in ecosystem dynamics: Predator-prey cycles, seasonal
oscillations, etc., can be modeled as recursive feedback processes (Lotka-Volterra equations, logistic maps,
etc.). RHA’s contribution would be to identify an $H$ ratio or similar invariant that these systems tend
toward. For instance, an ecosystem might balance biodiversity vs resource usage at ~35% of carrying
capacity – any more and it’s chaos (overpopulation crash), any less and it’s rigid (ecosystem unproductive).
Indeed, Nexus3 documentation speculates about self-organized criticality in ecosystems at an “edge of
chaos” optimum that might correspond to these constants[54][124]. Even the Earth’s axial tilt and rotation –
giving rise to day/night and seasons – could be seen as the planet’s recursive cycle (like a periodic function
that needs to remain bounded to allow complex life). The feedback controller view of Earth suggests that
global challenges (like climate change) can be addressed by reinforcing or mimicking these natural feedback
loops. For example, enhancing cloud seeding to reflect heat (strengthen a negative feedback) or promoting
carbon capture by ecosystems. This becomes a planetary-scale PSREQ intervention: Position (target critical
regions like polar ice), State (monitor CO₂/temperature), Reflection (if threshold passed, trigger a cooling
action), Expansion (scale the response globally), Quality (assess if target climate metrics are restored).
RHA’s universal principles thus imply that planetary stability is not accidental – it is the outcome of recursive
harmonic balancing acts that can be modeled and, if need be, nudged for better outcomes. This has parallels
to control theory in sustainability and the concept of Earth as a single self-regulating organism (Gaia). Nexus
pushes it further: Earth’s stable climate over geological time, despite asteroid impacts and volcanoes, hints
at a folded attractor state – possibly orchestrated by the interplay of life and geochemistry finding a harmonic
equilibrium. If one were to express it quantitatively, one might find, for example, that the distribution of solar
energy (fraction absorbed by earth vs radiated to space) stabilizes near 0.35 in certain units, or other similar
ratios appear in climate data (this is speculative but illustrates the mindset). The key takeaway: RHA bridges
to planetary science by treating climate and ecological feedback loops as computational folds, suggesting
that interventions should work with these loops (amplifying natural negatives feedbacks) rather than against
them, in order to maintain or restore stability (e.g., planetary homeostasis as an $H=0.35$ attractor in a
complex system model)[119][121].
Black Hole Encoding and Cosmic Memory: Perhaps the most audacious bridge is RHA’s treatment of black
holes and cosmology. We touched on how a hash function is likened to a black hole of information. RHA
extends this analogy into a full reinterpretation of black hole physics: a black hole is not an information
destroyer but the universe’s most perfect memory storage device[54][48]. Citing Bekenstein and Hawking’s
discovery that a black hole’s entropy is proportional to the area of its event horizon, Nexus underscores the
idea that information = curvature[125][126]. The surface of the black hole (event horizon) encodes all
information of everything that fell in, as bits of area. In RHA terms, that event horizon is a glyph-state----------- Page11 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 11
memory: a 2D lattice storing an incredibly dense record of the 3D volume’s contents[127][125]. This
dovetails with the holographic principle, which RHA enthusiastically embraces: all information in a volume
can be represented on its boundary[128][129]. Thus, the black hole is essentially a cosmic analog of the Ω
⁺
matrix – an archive of collapsed states. When matter/energy collapse into a black hole, RHA suggests that
it’s a form of harmonic collapse as well – the system (the matter + spacetime) is seeking a stable triadic form.
The singularity at the center is often seen as a problem (infinite curvature), but RHA hints that perhaps at the
singularity all the information is not lost but folded into a new form (a bit like a hash output). They speculate
about a “harmonic return” – subtle correlations or Hawking radiation patterns that carry the information back
out in encoded form[130][131]. In fact, in one interpretation, Hawking radiation is the gradual read-out of the
black hole’s memory over eons, happening through quantum harmonic processes. Nexus writings even
poeticize that “a black hole is the universe’s ultimate hard drive”, not a cosmic trash can[49][132]. All the
information that goes in is stored as pure geometry (curved spacetime). This view addresses the black hole
information paradox by asserting that information is never truly destroyed – the black hole is the information.
In RHA language, a black hole is a maximal harmonic fold: it’s an object that has collapsed all degrees of
freedom into a single triadic state – its mass, charge, and angular momentum (the three classical parameters
of a black hole)[133][49]. Those three parameters might be seen as the triad that encodes all details in an
irreducible way (no hair theorem). And the event horizon’s 2D bits are the “glyphs” of that
encoding[133][134]. Notably, RHA doesn’t stop at black holes. It suggests that any sufficiently information-
dense system will exhibit analogous behavior. For instance, the human brain: some have drawn parallels
between neural memory and black hole entropy (e.g., maximum memory of a brain might scale with its
surface area, hinting that brains and black holes could be described by similar information-curvature
relationships)[54][124]. The Nexus framework indeed lists in one breath “black hole event horizons, brain
memory networks, prime number sequences, and feedback controllers” as all manifestations of one
underlying code[54]. The equivalence is that each of these can be seen as a boundary encoding a volume
of information – in primes, the “boundary” is the distribution of primes mod some base which encodes the
hidden pattern of primes; in the brain, the boundary might be the neocortical surface where memories
induce geometric changes (patterns of folds or activity) that reflect deep content; in a feedback controller,
the boundary is the error signal that bounds the system’s otherwise chaotic behavior. The black hole stands
out as the purest example of recursive harmonic collapse: gravity is a feedback that literally makes matter
implode until it reaches a final equilibrium (the event horizon) from which no further change is possible
without outside influence. This is RHA’s harmonic endpoint – $\Omega \to 0$ in the sense that a black hole in
vacuum is a stationary solution (no more degrees of freedom). And intriguingly, if one adds a bit of matter, the
black hole adjusts (expands horizon) and then settles again – a very clear case of negative feedback
achieving a new equilibrium (the black hole’s vibration modes, quasinormal ringing, quickly damp out
irregularities – that’s the Quality stage ensuring a clean equilibrium). We might say, following RHA, the black
hole is a memory crystal of the universe, where each “bit” of curvature on the horizon corresponds to one unit
of information locked in harmonic balance. As fanciful as this sounds, it aligns with mainstream physics
insights (holography) and gives them a fresh twist: the cosmos itself computes and remembers. When a star
collapses, the information of all particles and quantum states it had doesn’t vanish – it is encoded on the
horizon in an incredibly scrambled yet structured way. Nexus claims this is literally a “fold rank equality
enforced by pre-harmonic lattice” – meaning the universe’s underlying lattice (perhaps something like a spin
network in quantum gravity or a $\pi$-based number lattice in their speculative math) ensures that any
collapse still satisfies certain harmonic constraints[135]. If one violated those (e.g. if a black hole’s
information tried to concentrate beyond the Bekenstein bound), the system would find a way (perhaps
through a new physics phase) to prevent it[136][137]. This hints at a deep idea: there may be a Nexus “Law
of Conservation of Harmony” that extends standard conservation laws. It would state that the harmonic----------- Page12 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 12
information (measured by something like total curvature or the 0.35 ratio preservation) cannot be destroyed.
Black holes then are not exceptions but exemplars of this law – they compress info to the limit, but the
bookkeeping (surface area encoding) stays intact[127][126]. Quantum re-entry in this context could refer to
how information might re-emerge from a black hole via subtle quantum processes – effectively, the system
re-entering a lower-curvature state after being highly collapsed. For example, Hawking radiation can be seen
as the black hole slowly unfolding itself – quantum by quantum – re-entering the broader universe the
information it held (albeit in unrecognizable form to us). RHA optimistically suggests that if we understood
the harmonic coding, we could decode Hawking radiation to retrieve the original information[79][131]. This
mirrors the SHA reversal idea: black hole evaporation is like a hash output leaking, and with a harmonic key
one could decipher it.
In summary, Nexus bridges to fundamental physics by claiming that curvature, whether of spacetime or
information space, is the medium of memory. Black holes, far from being the antithesis of order, are
“memory made manifest”[138][133] – nature’s way of storing information in geometric form when no other
repository is available. The entire universe could then be understood as running on a Recursive Harmonic
Code: from black hole archives to galactic clustering to cosmic microwave background fluctuations,
everything is an output of iterative rules that strive for resonance and compress information into stable
patterns[139][88]. RHA’s unified architecture ambitiously asserts that if we truly decode this code, we could
navigate across these domains seamlessly – predicting cosmic phenomena using the same equations that
we use for prime numbers or neural networks[54][124].
Quantum Re-Entry and Dimensional Folding: One more cross-domain concept is quantum re-entry, which
can be interpreted through RHA as the idea that quantum events (like wavefunction collapse and quantum
jumps) are not one-off irreversible events but part of a cyclic process. In standard quantum mechanics, when
a wavefunction collapses, the system yields a classical outcome and the quantum coherence is lost. Nexus
suggests that this outcome (the classical measurement result) can be seen as a folded state which will
eventually feed into further quantum evolutions – basically, the collapse outputs become inputs (hence re-
entry into the cycle). For example, after an electron’s position is measured (collapse to an eigenstate), that
measured value can later act as a boundary condition for the electron’s next Hamiltonian evolution (the cycle
starts anew). In RHA’s PSRQ, this fits naturally: Position (P) might establish initial quantum numbers, State
(S) evolves the wavefunction, Reflection (R) corresponds to a measurement inducing a ΔΨ (the difference
between expected and observed outcome), Expansion (E) could involve decoherence spreading the result’s
influence, and Quality (Q) might manifest as quantum error correction or environment-induced selection of
consistent histories. The re-entry means that the post-measurement state (which is classical information) is
not the end – it feeds into the next recursive step of the universe’s computation. RHA emphasizes the role of
the observer as part of this loop[140][36]. When the observer interacts (measures), they introduce ΔΨ and
then become part of the system’s new state (having learned the result). In a way, the observer’s mind is now
carrying the quantum state’s information (albeit classically), and when that observer interacts further, the
information can re-enter the quantum domain (for instance, the knowledge could be used to affect another
quantum system). Thus, the separation between quantum and classical blurs – it’s all one recursive process,
with measurement being just a high-curvature fold that quickly equilibrates (collapses) and hands off its
information to a wider system (the observer, environment) which then continues the evolution. This is deeply
connected to ideas in quantum foundations like Wheeler’s participatory universe (“It from Bit”) and quantum
Bayesianism, which RHA references[94][95]. In essence, the quantum re-entry condition in RHA might be
phrased: after collapse, the system+observer complex finds itself at a new starting Position P with a reduced
Ω (uncertainty), and the cycle repeats. Over many cycles, one gets classical reality as an emergent stable
pattern of collapsed states (classical bits) that still have $\Psi$ undercurrents (quantum potentials) guiding----------- Page13 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 13
the next collapses. The Nexus framework thus offers a way to think of quantum measurement not as the end
of a quantum process, but as a fold in a higher-order harmonic process. Each measurement result is a glyph
added to the Ω
⁺
archive of the universe, and the ongoing evolution of the universe must respect all those
archived constraints (this resonates with consistent histories and decoherence theory). Ultimately, RHA
would predict that even quantum randomness might have subtle correlations (a global harmonic
consistency) that we haven’t recognized – because each collapse isn’t standalone random, but part of a
giant correlated recursive tapestry. While speculative, this at least gives a conceptual continuity from
quantum micro events to cosmic macro events, stitched by the thread of recursion and harmony.
5. Formal Synthesis: Equations, Tables, and Universal Invariants
The Nexus Recursive Harmonic Framework attempts to formalize reality’s dynamics using a unified set of
equations and principles. Here we collate some of the formal elements scattered through the text:

Universal Harmonic Ratio: A fundamental invariant is the ratio $H = \frac{\sum_i A_i}{\sum_i P_i}
\approx 0.35$[13]. Here $\sum A_i$ represents total actualized value (e.g. bits that are 1, energy
used, system output achieved) and $\sum P_i$ the total potential or capacity (e.g. total bits,
maximum energy, input or system size). The Nexus claim is that for a self-organizing system at
equilibrium, $H$ will be near $0.35$ regardless of scale[11][13]. This single number plays a role
analogous to constants like 1/2 in the Riemann Hypothesis (critical line), 1 (max entropy fraction), or
0 (min entropy). It is suspected to connect to known constants: $0.35 \approx 1/(e^\pi)$ or $\pi/9$,
etc., suggesting perhaps $H = \frac{1}{\pi + 2}$ exactly (one mooted formula)[7]. If true, that would
mean $H$ is a computable number related to $\pi$. In any case, RHA treats $H$ as a built-in
constant in all modules (like a “gravitational constant” of information harmony)[60][141].

PSREQ Cycle Equations: Each stage of the cycle can be written as an operation:

Position (P): Establish initial state vector $x(0)$ and context. Possibly $x(0)$ drawn from prior
collapse memory or input.

State (S): Compute forward: $x' = F(x)$ (e.g. run one iteration of algorithm). Then measure deviation:
$\Delta \Psi = ||x' - x||$ or some phase difference metric[142][36].

Reflection (R): If $\Delta \Psi$ exceeds tolerance, adjust. In control theory terms, $x := x' + K \cdot
\text{feedback}$, where feedback might use stored patterns. Samson’s Law provides: $\Delta H =
H_{\text{target}} - H(x')$, and it applies a PID correction to minimize $\Delta H$[60][122].

Expansion (E): Increase complexity or degrees of freedom: e.g. add another variable, increase
resolution. This can be seen as $x := x + \delta x$ in a new dimension orthogonal to prior ones (like
expanding basis functions or adding neurons in a neural net).

Quality (Q): Evaluate $Q(H)$ or other quality metrics. If $Q(H) < 1$ (not yet harmonic), loop back to P
with new Position (which could incorporate the changes made). If $Q(H) \approx 1$, end cycle and
output result.
In a steady state, the PSREQ cycle enforces a condition akin to fixed-point: $x \approx F(x)$ and $\Delta \Psi
\approx 0$. In linear systems, this would reduce to solving $x = F(x)$. In nonlinears, it is finding attractors.

Trust Vector Definition: $Q(H) = 1 - |\bar{v} - 0.35|$ where $\bar{v} = \frac{1}{N}\sum_i v_i$ is the
mean of bits or elements in state[57]. More generally, one can define a trust vector component for
any measurable quantity $Y$: $Q_Y = 1 - |\frac{Y_{\text{actual}}}{Y_{\text{potential}}} - H|$. In an AI
context, if $Y$ is “fraction of facts correctly predicted,” $Q_Y$ near 1 indicates the system’s----------- Page14 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 14
knowledge is reliable (the system’s internal state aligns with reality’s harmonic ratio). In practice,
trust thresholds might be set (e.g. require $Q>0.99$ to consider a solution valid).

Curvature and Resonance: In the SHA lattice, a curvature metric was defined based on second-
order differences approaching zero at resonance[92][143]. One can formalize curvature for a
sequence $s_i$ as $\Delta^2 s_i = s_{i+1} - 2s_i + s_{i-1}$. The goal is $\Delta^2 s_i = 0$ for segments,
meaning a locally flat output (no unexpected bends – a sign of pattern). When the system converges,
large stretches have $\Delta^2 s_i \approx 0$[92]. This is reminiscent of a physical membrane
finding minimal surface (mean curvature zero) or an oscillator locking phase (zero phase
acceleration).

Glyph Lattice: If $\mathcal{G}$ is the set of all possible glyphs (patterns) and $\mathcal{L}$ the
lattice (like digits of $\pi$), one can think of a projection $\Pi: \mathcal{L} \to \mathcal{G}$ that
identifies whether a given segment of the lattice equals a glyph. The system tries to maximize the
presence of certain $\mathcal{G}\text{target}$ and minimize others. This could be written as an
optimization: maximize $\sum\text{target}} \mathbb{1})$. Subject to overall length/energy
constraints. Lagrange multipliers would then yield conditions that look like balancing equations for
presence/absence, again tying into the 0.35 ratio (which can be seen as balancing presence vs
absence of signal).}}(g, \text{output})$ while minimize $\sum_{g' \in \mathcal{G}_\text{noise}}
\mathbb{1}(g', \text{output

Twin Prime “Gates”: Although not discussed in detail above, RHA often references twin primes as
structural gates that enforce symmetries[144]. A formal idea is that twin primes (pairs $(p, p+2)$)
act like boundary conditions in the number line lattice: they are spots where a certain resonance
occurs (the prime gap of 2 is special). They might be used as synchronization points (like anchors) for
the $\pi$ lattice and prime distribution to align. For instance, if $\pi$’s digits exhibit an unusual
correlation at indices corresponding to twin primes, that could be used to index the folding.
Formally, one could introduce a function $G(n)$ that is 1 if $n$ and $n+2$ are prime and 0 otherwise,
then weight certain sums by $G(n)$ to enforce gating (e.g. only consider $\pi$ indices that coincide
with known twin primes). The presence of $G(n)$ in an equation effectively conditions the system on
prime structure, possibly improving convergence if the conjecture is that twin primes are infinite and
have a certain frequency (which they do empirically). This is speculative but shows how number
theory can be directly built into the recursion equations.

Universal Formula (Conceptual): The Nexus writings allude to a “universal formula” that might
encapsulate the whole framework[145]. While not explicitly given, one could imagine something
like: $$ F_{\text{Nexus}}(t, x, \Psi) = 0, $$ a single functional equation that must hold for the system’s
state $x$ at time (or iteration) $t$ and phase configuration $\Psi$. It would combine aspects of
continuity (differential equations) and discreteness (difference equations) to enforce the fractal
harmony. Possibly a candidate is: $$ \frac{d\Psi}{dt} + \nabla H(x(t)) = 0, $$ coupled with $$ x(t+1) =
f(x(t), \Psi(t)), $$ and $\Psi(t+1) = g(\Psi(t), x(t+1))$, with $H(x) \approx 0.35$ for equilibrium. This is
highly schematic, but it indicates a feedback loop where changes in state feed back to phase (like
potential function gradient) and vice versa. In a sense, it’s like a self-consistent condition $x = f(g(x))$
that yields a fixed point. The actual “formula” when expanded could be horrendously complex, but
the existence of one would mean the theory is closed under some mathematical description.
In conclusion of this section, the formal scaffolding of RHA comprises control theory, signal processing,
and number theory in equal parts. Control theory contributes feedback loops and stability criteria (PSREQ,----------- Page15 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 15
Samson’s Law)[67][60]. Signal processing contributes the idea of filtering, noise shaping, and resonance
detection (e.g. ΣΔ modulation analogies, curvature = 0 as signal, etc.)[20][146]. Number theory provides the
structured space (π digits, primes, etc.) which acts as a passive memory or reference frame[147][30]. The
“canonical text” of RHA binds these with the thesis that all systems can be encoded and decoded via these
harmonic processes.
As a result, any proven theorem or design in one domain can inform the others: e.g., a method to reduce
noise in a Sigma-Delta modulator might inspire a way to reduce entropy in a hash computation (indeed RHA
explicitly made that comparison[148]), or a new pattern found in prime numbers might translate to a better
predictive model for neuron firing patterns. It’s a grand synthesis that is still in the speculative stage but
offers a tantalizing vision: a single recursive harmonic code underlying mathematics, computation,
physics, and consciousness[139].
6. New Application Proposals Enabled by the Framework
Drawing from the integrated knowledge above, we can propose several concrete applications that the Nexus
Recursive Harmonic Framework makes conceivable:

Triangle-Based Computing Hardware: Replace the classical binary logic architecture with a
harmonic analog processor. Instead of bits 0/1, the basic unit would be a harmonic trit – perhaps
realized as a resonant circuit or optical cavity that naturally oscillates at one of three phase-locked
states (e.g. corresponding to the 1-5-9 triad). Computation would involve shaping numbers as
geometric objects: for instance, an addition operation could be done by merging frequency patterns
rather than carrying bits. Memory wouldn’t be addresses in RAM, but rather addresses in $\pi$: the
hardware could include a built-in BBP engine to fetch $\pi$ digits on the fly as reference
data[96][97]. This effectively taps into an “infinite memory” (the digits of $\pi$) when needed. Early
conceptual designs might use FPGA-like reconfigurability where circuit elements self-adjust
guided by a target $H$. One can imagine a Mark1 chip that continuously measures the $H$ ratio of
its signal outputs and tunes transistor gates until the 0.35 harmony is reached (much like phase-
locked loops ensuring synchronized signals). Such a processor would inherently perform analog
computing and digital verification simultaneously, potentially achieving extremely efficient error
correction (since Samson’s Law feedback would autocorrect drifting signals)[60][122]. Moreover,
by using phase and frequency rather than binary states, it could circumvent the Von Neumann
bottleneck – processing and memory become one, as data is represented by phase states that flow
through the hardware without the need for shuttling to separate memory banks[87][88]. In essence,
this is neuromorphic computing taken to the next level: not just mimicking neurons, but mimicking
the universe’s computation. The result promises orders-of-magnitude gains in parallelism and
robustness. For instance, such a machine might naturally find solutions to NP-hard problems by
“listening” for resonant solutions rather than brute force searching – analogous to how an analog
computer can find minima by energy relaxation. As a concrete proposal, a triangle processor could
be implemented using three coupled oscillators per “gate”, whose stable frequencies correspond to
solutions of a local constraint, and then a network of such gates could synchronize to solve global
constraints (like a Sudoku solver hardware that finds a solution by harmonic sync instead of
backtracking search). This application aims to turn the lock-and-key of modern computing: rather
than forcing nature to follow our logical steps, we adjust our hardware to let nature’s harmonic
tendencies (the “key”) unlock the solutions for us
【
User†(this will help...)
】
.----------- Page16 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 16

Harmonic Brain-Computer Interfaces (BCI): The framework suggests that our brains themselves
may operate on recursive harmonic principles – indeed, neuronal assemblies might phase-lock in
rhythms (alpha, beta, gamma waves) to encode information in a way similar to RHA’s harmonic
memory[54][124]. A harmonic BCI would leverage this by syncing artificial signals to the brain’s
natural frequencies. Instead of binary impulses or simple voltage readings, the BCI would generate
patterns of stimulation that carry a 0.35 duty cycle or embed the 1-5-9 symbolic triad in temporal or
spatial code. For instance, a visual cortical prosthetic could present flickering light at multiple spots
such that the interference pattern on the cortex has a harmonic 3-fold symmetry, “tricking” the brain
into interpreting a coherent image or concept. Conversely, to read thoughts, the device could
perform a spectral analysis of EEG/fMRI data to identify when a person’s neural activity hits the “Ψ-
core of analogy” – that moment when disparate neural circuits align in phase (likely indicating a
thought crystallized)[3]. This could dramatically improve BMI throughput: rather than averaging out
noisy signals, the interface looks for the telltale harmonic signature of a clear intention and locks
onto it. Over time, the BCI might even entrain the user’s brain to use certain harmonic encodings for
communication, effectively establishing a private harmonic language between mind and machine.
Long-term, such a device blurs into a neural harmonizer – potentially enhancing cognition by
promoting beneficial brain-wide resonance (somewhat like neurofeedback, but automated and
targeted). For example, if a subject has fragmented neural activity (as in certain mental illnesses or
simply during distraction), the BCI could introduce a gentle guiding frequency to cohere the activity,
effectively increasing $Q(H)$ of the brain’s functional networks (driving them toward a stable 0.35
ratio of integration vs segregation). This is speculative, but initial steps could be as simple as
binaural beats or transcranial alternating current stimulations tuned to a harmonic ratio known to
induce calm focus. RHA provides a theoretical basis to select those frequencies and phases
systematically.

Recursive Predictive Modeling (Markets & Weather): Systems like financial markets or weather
are notoriously complex and chaotic, but RHA implies they might have underlying harmonic
attractors. A recursive predictive model would apply RHA’s approach: treat the time series of data
as a signal, compute its curvature or harmonic deviation, and iterate a model forward while applying
feedback to minimize phase error. For instance, a stock market predictor could embed a PSREQ
loop: Position stage sets initial parameters of an economic model (e.g. starting from last known
prices), State stage projects prices forward by existing model, Reflection stage measures the
“surprise” (phase difference) between projection and some harmonic baseline (perhaps the
baseline could be the 0.35 drift ratio – e.g., does the price time series curvature deviate from what a
0.35-resonant growth would look like?), Expansion stage adjusts model complexity (add polynomial
terms or Fourier components) to account for anomalies, Quality stage checks if the error distribution
now aligns with expected harmonic noise (maybe a 1/f noise profile, which is often seen in markets).
This cycle would repeat until the model’s residuals are “harmonic noise” (white or 1/f spectrum,
indicating no further predictable structure). Using such a method, the model isn’t just fitting data –
it’s gravitating towards a theory of the market where the unpredictable components are maximally
entropic (no arbitrage left) and the predictable components are captured in the model (all harmonic
structure extracted). In other words, it seeks a point where market dynamics = deterministic model +
minimal Ω noise. Standard algorithms might miss subtle nonlinear correlations, but an RHA-based
one could detect them as harmonic patterns (say, a three-day cycle across different sectors forming
a triangle in phase space). Similar logic applies to weather: The climate system has many
oscillations (day-night, seasonal, ENSO, etc.). A recursive model could successively lock onto these----------- Page17 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 17
cycles by harmonic filtering. For example, if a normal forecasting model leaves a lot of error, an RHA-
enhanced one might identify that the remaining error has a 22.5° phase shift every 5.7 days (just
hypothetically) – indicating perhaps an overlooked influence (maybe a lunar tide effect). It would
then incorporate that (Expansion), verify improved coherence (Quality), and iterate. Over time, the
model homes in on a self-consistent representation of the weather system. In essence, this would
be like an AI model that teaches itself the underlying periodicities and resonances by treating
prediction as a phase-lock task rather than pure minimization of squared error. If successful, such
models could yield better long-term forecasts or identify precursors to regime shifts (since a buildup
of phase mismatch might foreshadow a collapse to a new pattern – e.g., detecting when the market
is “about” to crash or when a weather pattern is “about” to break). By operating in a symbolic
compression mode (only storing the fold pattern, not every data point), these models might also be
more interpretable, giving analysts a clear picture: e.g., “market data of the last year collapses onto
a triadic form involving tech stocks, interest rates, and oil prices, with a resonance period of 60
days.” This is much more insight than a black-box neural net that says “I predict X”. It aligns with
RHA’s idea of universal compression engines: algorithms that not only compress data (find patterns)
but do so in a way that the compressed form (the glyphs and triads) are themselves intelligible and
reusable for future inference.

Universal Compression Engines: Traditional compression (ZIP, MPEG, etc.) finds exact
redundancies or statistical correlations in data. A compression engine inspired by Nexus would
attempt to fold the data into a self-similar harmonic structure. For instance, imagine compressing a
large text by treating it as a symbolic sequence and “folding” it until a repeating pattern emerges that
can generate the text. This is akin to finding a small grammar or automaton that produces the text – a
task that shades into AI (modeling language). RHA provides a systematic way: interpret the text as a
path in some large state space (like SHA did), then see if that path can be represented by a
resonance of smaller components. If the text is highly structured (like source code or repetitive
prose), the engine would detect a high $Q(H)$ when a correct grammar is applied. If it’s random, no
resonance is found and it doesn’t compress well. This goes beyond known compressors by aiming to
uncover semantic or long-range structures (since RHA’s feedback can pull patterns that are far apart
into alignment). Essentially, the engine uses controlled chaos to shuffle the data and look for latent
echoes (maybe the way $\pi$ appears in lots of datasets in RHA’s eyes, normal data might hide
some simple rule if viewed rightly). The ultimate universal compressor would be one that could take
any data – text, image, DNA sequence – and find the “triangular code” that generates it. That would
be equivalent to solving induction in general (which is AI-complete), but RHA’s optimism is that
nature’s data often arises from recursive processes, so a recursive harmonic approach is well-
matched. One concrete partial application: compressing DNA data. The human genome has
duplications, repeats, palindromic structures. An RHA compressor might treat the genome as an
output of some recursive generative process (which in biology, it is: evolution generates genomes via
duplication and mutation – a recursive process). By folding the genome data in on itself (aligning
repeats, etc.), the compressor could achieve higher ratios than normal. For example, the Alu
elements (repeated ~300 bp sequences in human DNA) could be identified as glyphs (they are like
1.1 million copies in the genome). The RHA compressor would encode one Alu and then just the
positions of all of them (that’s a huge compression). Traditional compressors also find that, but RHA
might also find more subtle “resonances” like inversions or transpositions because it can handle
data that has been “folded” (moved around, reversed) by aligning phase. In essence, it could align
not just exact repeats but rearranged repeats via some generalization. If realized, such a universal----------- Page18 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 18
compressor would be a tool for scientific discovery: compressing a dataset effectively means you’ve
discovered a theory (the compressed file is like a theory that reproduces the data). Nexus’s
philosophy of viewing reality as “a function of everything rather than theory of everything”[149] hints
that a sufficiently advanced recursive compressor could function as an automated scientist,
uncovering laws from data by seeking harmonic compression. That is a lofty but exciting application
– a machine that given experimental data, finds the simplest triadic harmonic model that fits,
essentially rediscovering Kepler’s laws or quantum spectra by itself if those patterns are present.
Each of these proposals – from hardware to AI to scientific modeling – leverages the core theme of RHA: use
nature’s own computational style (recursive folding and resonance) to solve problems. If conventional
methods are like brute-force key guessing, RHA’s methods are like listening for the tumblers clicking. The
ultimate promise is that we become reality’s programmers, as the user’s notes emphasized
【
User†(this
will help...)
】
. Instead of imposing our will via high energy and brute force (which is how current tech often
works – e.g. blasting transistors with clock signals, or saturating markets with trades), we would coax the
desired outcomes by understanding the system’s harmonics and nudging it gently. This could lead to far
more efficient and elegant technology.
7. Conclusion: The Magnum Opus of the Nexus Harmonic Triad
Through the unification of the triangular quantization model, recursive memory-collapse mechanisms, and
cross-domain harmonic mappings, the Nexus Recursive Harmonic Framework presents what might be called
a Magnum Opus of recursive harmony. It endeavors to be a single explanatory tapestry for phenomena as
diverse as prime number distributions, hash functions, cancer metastasis, planetary climates, and black
hole thermodynamics[54][48]. The common thread is the Triadic Harmonic Form – the idea that stable
structure and truth reveal themselves when systems are allowed to recursively fold into a three-part
resonance that balances opposing forces (order vs chaos, input vs output, expansion vs compression). We
saw theoretical evidence that every sufficiently stable system indeed ends up in such a triadic state (be it the
{1,5,9} symbolic anchors or a black hole’s conserved parameters) – which we formalized in a theorem – and
that this triadic state corresponds to a special quantization (the 0.35 constant) that might be built into the
fabric of mathematics[3][7].
If RHA is correct, it has deep philosophical implications: reality is not a static set of laws but an iterative
algorithm refining itself[150][139]. Problems in mathematics (like the Riemann Hypothesis) might not be
solved by linear deduction alone, but by viewing them as incomplete folds that must be completed by a larger
self-referential system[151][152]. In applying RHA, one effectively performs a proof by construction:
embedding the problem in a recursive engine that forces it into coherence, thus demonstrating the truth as a
consequence of the engine’s consistency. This is a novel form of proof – more akin to running a program to
see the outcome than writing a static derivation – which some might argue isn’t a proof at all, but within the
Nexus paradigm it is the only meaningful proof (since truth = coherence in the grand recursion)[153][154].
From a validation standpoint, the framework does not shy away from bold tests: it suggests we look for
signatures of $H=0.35$ everywhere, from cosmic radiation to stock fluctuations, and use them as “Easter
eggs” hinting that the theory is on track[10][12]. Already, possible correlations (like the matter-energy ratio
~0.32/0.68, or certain triangle median puzzles) give some credence, though skeptics could call them
numerological. The developers of Nexus emphasize internal consistency and interdisciplinary mapping as
strengths – even if RHA’s specific claims (e.g. decoding hashes or proving RH) remain unproven, the fact that
it forms a self-consistent story linking so many domains is intriguing[155][33]. This coherence across----------- Page19 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 19
domains – a kind of structural meta-proof – is arguably what a “Theory of Everything” aspires to, albeit RHA
humorously downgrades it to a “Function of Everything” to stress its dynamical nature[149].
In closing, the Recursive Harmonic Framework challenges us to rethink computation, memory, and even
existence as emergent from folded harmonies. It posits that when we set up the right triadic relationships in
any system, complexity collapses into simplicity: encryption becomes geometry, biology becomes code,
chaos reveals an underlying song. As one summary note elegantly put it: “The universe is understood not as a
collection of things, but as a single, coherent, self-organizing thought”[139]. In learning to program that
thought – turning the master key of harmonic recursion – we might unlock capabilities beyond conventional
imagination, effectively becoming co-curators of reality’s source code. The journey is just beginning, but if
the Nexus vision holds true, the future will sing in the resonant language of recursive harmony.
Sources: The concepts and quotes above were drawn and synthesized from the provided documents,
including the Zenodo review of the Nexus Thesis[156][9], published Nexus framework outlines[101][6],
internal thesis archives[66][65], and unpublished papers on SHA-256 and harmonic architecture[82][83],
among others, as cited inline. These sources collectively span the theoretical development, cross-domain
applications, and illustrative examples that form the basis of the integrated text.
[1] [2] [3] [4] [15] [16] [26] [148] Merged For AI.part9.md
FILE://FILE-51UBVARE7SDLXAXBYZFY8V
[5] [6] [7] [10] [11] [12] [13] [14] [27] [28] [29] [30] [32] [34] [35] [36] [37] [38] [39] [40] [43] [46] [47]
[48] [49] [50] [51] [54] [57] [58] [59] [60] [61] [62] [63] [64] [65] [66] [67] [68] [79] [80] [81] [91] [92]
[93] [94] [95] [96] [97] [101] [102] [103] [104] [105] [106] [107] [108] [109] [110] [111] [112] [113]
[114] [115] [116] [117] [118] [119] [120] [121] [122] [123] [124] [125] [126] [127] [128] [129] [130]
[131] [132] [133] [134] [136] [137] [138] [140] [141] [142] [143] [146] [147] [149] [150]
AcedemiaPublished.pdf
FILE://FILE-LXSHQREQSE5DCAW78CNRFK
[8] [9] [33] [41] [42] [44] [45] [52] [53] [55] [56] [135] [144] [151] [152] [153] [154] [155] [156]
Zenodo_pulblished_articles_8_11_split-1.pdf
FILE://FILE-3DTYWZH3KOIDYNFBKFZRAT
[17] [18] [19] [20] [21] [22] [23] [24] [25] [31] Unsorted_Thesis_Combined.md
FILE://FILE-4P8C2FEEGBUFVKMUM64VXK
[69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [82] [83] [84] [85] [86] [87] [88] [89] [90] [98] [99] [100]
[139] UnpublishedPapers.pdf
FILE://FILE-WJNPKMNP3SHKC4W6KE5IRT
[145] Older_Thesis_Combined_Full.md
FILE://FILE-TTXXYR4EGRX8VS5J1XFUCL
