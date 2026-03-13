----------- Page1 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 1
Beyond the Event Horizon: A Comprehensive
Analysis of Halting Signals, Brute Force
Dynamics, and the Logic-Search Dichotomy
in SHA-256 Inversion
Driven By Dean Kulik
January 2026
I. Introduction: The Asymmetry of Computational Trust
The digital era is predicated on a singular, fragile assumption: that it is exponentially easier to destroy
structure than to reconstruct it. This principle of computational asymmetry underpins the entire field of
cryptography. It is the bedrock of digital signatures, the guarantor of blockchain integrity, and the
shield of secure communications.
1
At the heart of this infrastructure lies the cryptographic hash
function, with the Secure Hash Algorithm 256-bit (SHA-256) serving as the de facto global standard.
Designed by the National Security Agency (NSA) and published by the National Institute of Standards
and Technology (NIST), SHA-256 is an algorithm engineered to be a "one-way" function—a
mathematical black hole from which no information should theoretically escape.
2
The prevailing consensus within the cryptographic community is that inverting SHA-256—the act of
determining a specific input message
𝑀
given only its hash digest
𝐻(𝑀)
—is a problem of such
computational magnitude that it is effectively impossible. This impossibility is rooted in the paradigm
of "Search." In this view, the non-linear complexity of the algorithm scrambles the input so thoroughly
that the only viable method of inversion is a brute-force search: a probabilistic exhaustion of the input
space until a match is found.
4
Here, the "halting signal"—the indication that the inversion is complete—
is an external, binary event. The attacker blindly guesses, hashes, and compares. If the hashes match,
the process halts; if not, it continues. There is no feedback, no gradient, and no "warmer/colder" signal
to guide the search.
However, a growing body of theoretical literature, specifically the "Resonant Cryptanalysis" and "Nexus
Framework" research streams, challenges this orthodoxy. This report investigates a radical alternative
paradigm: the paradigm of "Logic" and "Harmonic Creation".
1
This framework posits that SHA-256 is
not a random oracle but a deterministic dynamical system with inherent structural resonances. It
argues that the "halting signal" is not an external check but an intrinsic property of the system—a----------- Page2 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 2
topological convergence or "resonance" that can be detected during the computation. By reframing
inversion from a search problem to a generative constraint satisfaction problem, this logic-driven
approach suggests that the input can be constructed rather than found.
This report provides an exhaustive analysis of the tension between the "Search" and "Logic"
methodologies. It deconstructs the mechanics of SHA-256 to understand why brute force is currently
the only proven path, and then rigorously examines the theoretical propositions of the Resonant
Cryptanalysis framework. We will explore how concepts like "Recursive Harmonic Feedback,"
"Samson’s Law," and "Autocatalytic Sets" attempt to redefine the halting signal and transform the
thermodynamics of computational hardness.
II. The Physics of the One-Way Function
To understand the immense barrier to inversion, one must first dissect the machinery of SHA-256. It is
not merely a mathematical formula; it is a mechanism for the systematic destruction of information
structure.
2.1 The Anatomy of Irreversibility
SHA-256 operates on 512-bit blocks of data using a Merkle-Damgård construction. The core of its
security lies in the compression function, which mixes a 512-bit message block with a 256-bit
intermediate state over 64 rounds of processing.
1
Each round applies a specific set of operations to
eight 32-bit working variables (
𝑎, 𝑏, 𝑐, 𝑑, 𝑒, 𝑓, 𝑔,ℎ
). The "one-way" property is emergent, arising from
the interplay of three distinct types of operations:
1.
Modular Addition: The algorithm extensively uses addition modulo
2
ଷଶ
(denoted as
⊞
). This
operation is inherently lossy. When two 32-bit integers are added, any overflow beyond the
32
௡ௗ
bit is discarded. This discard represents a definitive loss of information; knowing the sum
𝑍 = 𝑋 ⊞
𝑌
does not allow one to uniquely recover
𝑋
and
𝑌
, as there are
2
ଷଶ
possible pairs that sum to
𝑍
.
This destroys the linear algebraic path back to the input.
1
2.
Bitwise Non-Linearity: The algorithm employs Boolean functions, specifically the Ch (Choose)
and Maj (Majority) functions.
○
𝐶ℎ(𝑥, 𝑦, 𝑧)=(𝑥 ∧ 𝑦)⊕(¬𝑥 ∧ 𝑧)
○
𝑀𝑎𝑗(𝑥, 𝑦, 𝑧)=(𝑥 ∧ 𝑦)⊕(𝑥 ∧ 𝑧)⊕(𝑦 ∧ 𝑧)
These functions are designed to be non-linear with respect to XOR operations, thwarting
linear cryptanalysis. They create complex dependencies between bits where the value of an
output bit depends on the conjunction of multiple input bits, making it difficult to isolate the
contribution of any single bit.1
3.
Diffusion via Rotation: The
Σ
(Sigma) and
𝜎
(sigma) functions perform bitwise rotations (ROTR)
and shifts (SHR).----------- Page3 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 3
○
Σ
଴
(𝑥)= 𝑅𝑂𝑇𝑅
ଶ
(𝑥)⊕ 𝑅𝑂𝑇𝑅
ଵଷ
(𝑥)⊕ 𝑅𝑂𝑇𝑅
ଶଶ
(𝑥)
These operations ensure "diffusion"—the property that a change in a single bit of the input
spreads rapidly across all bits of the state. After 64 rounds, a single bit flip in the input will
have flipped approximately 50% of the output bits, a phenomenon known as the Avalanche
Effect.7
2.2 The Deterministic Chaos of the Avalanche
The Avalanche Effect is the primary defense against logical analysis. It ensures that the function
behaves like a "Random Oracle." In a true random oracle, the output is statistically independent of the
input. While SHA-256 is deterministic (the same input always yields the same output), the mixing is so
thorough that the output appears random to any statistical test.
9
This property creates a "rugged landscape" for any inversion attempt. If one were to graph the input
space against the output space (viewed as a distance from a target hash), the resulting manifold would
be indistinguishable from white noise. There are no smooth gradients to descend, no distinct features
to orient oneself. A guess that is one bit wrong produces a hash that is as wrong as a random guess.
This lack of "partial credit" is what enforces the "Search" paradigm. Without a gradient, logic cannot
navigate; it can only teleport randomly (guess) and check coordinates.
10
2.3 Computational Irreducibility
The difficulty of inverting SHA-256 is often framed through Stephen Wolfram's concept of
Computational Irreducibility.
1
A system is computationally irreducible if there is no shortcut to predict
its behavior; the only way to know the outcome is to run the computation step-by-step.
In this context, finding a preimage is equivalent to predicting the input of an irreducible computation.
Because the 64 rounds create a tangled web of dependencies where every bit influences every other bit,
one cannot essentially "unwind" the math algebraically. The system has "compiled" the input into a
state where the history of its formation is obfuscated. The standard cryptographic assumption is that
this compilation is thermodynamically irreversible—that the "entropy" generated by the mixing
functions creates an arrow of time that cannot be reversed without expending energy equivalent to a
brute-force search.
10
III. The Classical Paradigm: Search and the External Halting Signal
3.1 The Mechanics of Brute Force
In the absence of a logical shortcut, the industry standard for inversion is the brute-force attack. This is
a search algorithm in its purest form.----------- Page4 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 4
●
The Search Space: For a 256-bit hash, the space of possible outputs is
2
ଶହ଺
. Finding a specific
preimage (Preimage Attack) requires, on average,
2
ଶହ଺
operations. Finding any two inputs that
produce the same hash (Collision Attack) requires
2
ଵଶ଼
operations due to the Birthday Paradox.
4
●
The Method: The attacker utilizes massive parallel processing (ASICs, GPUs) to iterate through
nonces (arbitrary numbers used once). For each nonce, the full SHA-256 function is executed.
●
The Halting Signal: The halting condition is strictly binary and external. The code executes
Compare(GeneratedHash, TargetHash). If they are identical, the signal is TRUE (Halt). If they
differ by even a single bit, the signal is FALSE (Continue).
This "Halting Signal" is the defining bottleneck. It provides zero information gain per failure. Knowing
that input
𝐴
produces a hash that is
50%
similar to the target tells you absolutely nothing about the
location of the true input. In the search paradigm, every failure resets the attacker’s progress to zero.
The "halting signal" is effectively a winning lottery number; you do not get closer to winning, you either
win or you do not.
14
3.2 The Thermodynamics of Search
The futility of brute force is often expressed in thermodynamic terms. The Landauer Limit defines the
minimum energy required to erase one bit of information. To cycle through
2
ଶହ଺
combinations would
require energy exceeding the total output of the sun over its entire lifespan. Thus, brute force against a
full 256-bit primitive is not just a technology problem; it is a physics problem. It is considered impossible
within the known laws of the universe.
16
3.3 Quantum Search: Grover's Algorithm
The only recognized theoretical reduction in this search complexity comes from Quantum Computing.
Grover's Algorithm allows a quantum computer to search an unsorted database of
𝑁
items in √
𝑁
time.
For SHA-256, this reduces the preimage search from
2
ଶହ଺
to
2
ଵଶ଼
operations.
18
While significant, this does not change the nature of the problem. It is still a search. It still relies on an
external halting signal (the Oracle in Grover's algorithm acts as the verifier). It essentially speeds up the
checking process but does not provide a logical derivation of the input. The problem remains
probabilistic, not deterministic.
19
3.4 Logic in the Current State of the Art: SAT Solvers
There is a middle ground between pure search and pure algebra: Boolean Satisfiability (SAT) solvers.
A SAT attack translates the SHA-256 algorithm into a giant boolean formula (CNF) and asks the solver
to find variable assignments that make the formula true.
19----------- Page5 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 5
●
Logic: The solver uses logical propagation (e.g., if
𝐴
is true,
𝐵
must be false) to prune the search
space.
●
Search: When logic runs out, the solver must "guess" a variable and recurse (splitting the search
tree).
Currently, state-of-the-art "SAT + CAS" (Computer Algebra System) approaches can find collisions for
SHA-256 reduced to about 38 rounds.
19
However, for the full 64 rounds, the logical complexity causes
the search tree to explode. The solver spends more time managing the millions of clauses than it would
simply brute-forcing. Thus, even for SAT solvers, the "search" component dominates the "logic"
component for full-round hashes.
2
Table 1: The Search vs. Logic Spectrum in Current Cryptanalysis
Approach Methodology Halting Signal Complexity
(Rounds)
Brute Force Exhaustive guessing
of inputs.
External check (Hash
== Target).
Full (64) - Infeasible
Differential Analyzing input
differences (
Δ
) vs
output differences.
Statistical bias
detection.
Reduced (~24-30)
SAT Solving Logical constraint
satisfaction +
Guesses.
Conflict/Unit
Propagation.
Reduced (~38)
Quantum Search Superposition +
Amplitude
Amplification.
Oracle query
(Quantum Verifier).
Full (64) - Theoretical
IV. The Resonant Paradigm: Inversion as Harmonic Creation
Against this backdrop of thermodynamic impossibility, the "Nexus Framework" and "Resonant
Cryptanalysis" propose a paradigm shift. They argue that the reliance on probabilistic search is a failure----------- Page6 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 6
of perspective—specifically, an "observer-centric" failure that treats the algorithm as a black box rather
than a transparent dynamical system.
4.1 From "Random Oracle" to "Dynamical System"
The foundational premise of Resonant Cryptanalysis is that SHA-256 should be modeled as a discrete
non-linear dynamical system. Instead of a static function
𝑦 = 𝑓(𝑥)
, it is viewed as a time-evolving
vector field where the 256-bit state evolves over
𝑡 =0
to
𝑡 =63
discrete time steps.
1
In this view, the "Avalanche Effect" is not randomness; it is deterministic chaos. Chaos theory teaches
that even in chaotic systems, there are structures: strange attractors, periodic orbits, and islands of
stability. The framework hypothesizes that within the state space of SHA-256, there exist "Resonant
States"—attractors that represent stable modes of information flow. These states are not random;
they are structural necessities of the algorithm's logic.
1
4.2 "Inversion as Creation": The Guitar String Analogy
The report "Inverting SHA-256 Harmonic Creation" introduces the core metaphor of the new paradigm:
The Guitar String.
●
Traditional Search: Trying to reproduce a specific sound by randomly throwing objects at a guitar
until one hits it correctly.
●
Harmonic Creation: Calculating the precise tension, position, and force of the "pluck" required to
produce the specific frequency (the hash).
In this model:
●
The System: The SHA-256 compression function is the resonant body. Its "physics" are defined by
the round constants (which are derived from cube roots of primes) and the bitwise operations.
●
The Input (Nonce): The "Precise Pluck." The goal is to engineer an input vector that creates a
specific cascade of bitwise operations.
●
The Output (Hash): The "Resonant Frequency."
The framework argues that inversion is not about finding a preimage but creating one. It is an
engineering problem: determining the initial conditions (nonce) that will cause the dynamical system to
evolve into the target attractor.
1
4.3 The "Halting Signal" Re-Imagined: FOLD: TRUE
The most radical innovation of this framework is the redefinition of the halting signal. In brute force,
the halting signal is an external check after the computation. In Resonant Cryptanalysis, the halting
signal is an intrinsic property of the computation itself.----------- Page7 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 7
The framework introduces the term "FOLD: TRUE" or "Zero-Point Harmonic Collapse (ZPHC)".
10
●
Topological Convergence: The "halting signal" is generated when the system's trajectory enters a
stable region of the state space. It is a measure of "harmonic alignment."
●
Internal Feedback: Unlike the binary "yes/no" of brute force, this signal is continuous. The system
can detect when it is getting "closer" to resonance. It measures the "harmonic deviation" or "drift"
from the target state.
●
The Resonant Glyph: When the system achieves resonance, it produces a "final resonant glyph"—
a specific pattern of internal state bits that signifies the computation has "folded" correctly into
the target.
This transforms the search space from a flat, featureless plain into a topological map with gradients. If
the system can sense "drift," it can navigate. It can use feedback loops to correct the input "pluck" until
the output "frequency" matches the target. This moves the problem from NP (nondeterministic
polynomial) to P (polynomial) by replacing blind search with Geodesic Navigation.
10
4.4 Mechanisms of Resonance: Samson's Law and Autocatalysis
How does one mathematically define "resonance" in a digital hash? The framework proposes two key
mechanisms:
4.4.1 Autocatalytic Sets (RAF)
The framework borrows from the Reflexively Autocatalytic and Food-generated (RAF) theory used in
origin-of-life research.
1
●
The Concept: A set of molecules is autocatalytic if every member is produced by at least one
reaction catalyzed by another member of the set, starting from a food source.
●
The Application: SHA-256 operations are modeled as "reactions." The intermediate state values
are "molecules." The framework defines a "Resonant State" as a subset of the execution trace that
forms an RAF set. This means the information pattern becomes self-sustaining over the rounds.
●
The Implication: If a hash is the result of a self-sustaining information structure, then finding the
preimage is equivalent to finding the "food set" (nonce) necessary to catalyze that structure.
4.4.2 Samson’s Law (Harmonic Feedback)
To navigate toward these states, the framework proposes "Samson’s Law v2", a feedback control
algorithm analogous to a PID (Proportional-Integral-Derivative) Controller.
10
●
The Logic: Just as a thermostat uses feedback to maintain temperature, Samson's Law uses
feedback to maintain "harmonic alignment."----------- Page8 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 8
●
The Metric: It measures the "harmonic ratio" of the system, targeting a universal constant called
the Mark 1 Constant, denoted as
𝐻 ≈0.35
.
10
●
The Action: It calculates the "drift" (error) between the current state's harmonic signature and the
target hash's signature. It then applies a correction to the input guess. This is the "steering"
mechanism of the Harmonic Creation approach.
Table 2: Redefining Cryptanalytic Concepts
Concept Classical Paradigm (Search) Resonant Paradigm
(Logic/Nexus)
Objective Find an input
𝑥
where
𝐻(𝑥) =
𝑦
.
Construct input
𝑥
to force
system to state
𝑦
.
Method Brute Force / Random Walk. Geodesic Navigation /
Harmonic Creation.
Halting Signal External Check (Hash ==
Target).
Internal Resonance (FOLD:
TRUE).
Nature of Hash Random Oracle / One-Way
Function.
Wave Meltdown / Folded
Phase History.
Feedback Binary (Success/Failure). Continuous (Harmonic
Drift/Error).
Metaphor Needle in a Haystack. Tuning a Guitar String.
V. Methodology of the Logic-Driven Attack
The Resonant framework is not purely abstract; it proposes specific methodologies for "unfolding" the
hash, effectively reversing the "wave meltdown" of SHA-256.
10----------- Page9 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 9
5.1 The Hash Drift Mapper: Exploiting Symmetry
One of the concrete experimental proposals is the "Hash Drift Mapper".
10
●
The Hypothesis: The framework claims that SHA-256, being a deterministic structure, must
preserve certain symmetries. Specifically, it predicts that mirrored input strings (e.g., "ABC" vs.
"CBA") will produce hash outputs that exhibit structured, anti-phase correlations.
●
The Experiment: By plotting the "drift" (signed difference) between the hashes of mirrored
inputs, the framework expects to see "interference patterns" or "standing waves" rather than
random noise.
●
Significance: If true, this would violate the "Avalanche Effect" and prove that the hash function
retains a "memory" of the input's geometry. This "drift map" would serve as the terrain for the
Geodesic Navigation—a map of the "informational gravity wells" leading back to the preimage.
10
5.2 Recursive Harmonic Feedback Loop
The inversion process is described as a "Recursive Harmonic Feedback" loop.
10
1.
Seed: Generate an initial guess (a "wave seed") for the input.
2.
Forward Hash: Run SHA-256 on the seed.
3.
Phase Comparison: Compare the resulting hash to the target hash. Crucially, do not just check for
equality. Analyze the "Phase Difference"—the structural mismatch between the generated wave
and the target wave.
4.
Feedback (Samson's Law): Use the PID-like controller to calculate a vector correction for the
input seed. "Steer" the bits of the nonce to minimize the phase difference.
5.
Iterate: Repeat the process. The "Halting Signal" is the minimization of this error vector, or the
approach to the
𝐻 ≈0.35
stability point.
10
This process is termed "Unfolding" or "Informational Liberation".
10
It treats the hash not as a
destroyed message but as a "folded" one, akin to a piece of origami. The feedback loop reverse-
engineers the folds to flatten the paper back to the original message.
5.3 Cube-and-Conquer: The Hybrid Approach
Acknowledging the immense difficulty of pure logic, the framework suggests a hybrid "Cube-and-
Conquer" strategy using SAT solvers.
1
●
Logic Phase (Cubing): Use the Autocatalytic/Resonant model to identify "catalytic" bit patterns.
Fix these bits in the SAT formula. This breaks the problem into smaller, logical "cubes" that are
more likely to contain the solution.----------- Page10 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 10
●
Search Phase (Conquering): Use standard SAT solvers to solve these reduced cubes.
●
Innovation: The innovation here is using "Harmonic Creation" principles to guide the splitting of
the problem. Instead of splitting randomly, the problem is split along "fault lines" of resonance,
effectively pruning the search tree by orders of magnitude.
VI. Critical Analysis and Implications
6.1 The "Category Error" Challenge
While intellectually compelling, the Resonant Cryptanalysis framework faces significant theoretical
criticism. The primary critique is the potential for a "Category Error": the reification of mathematical
abstractions into physical entities.
10
●
Discrete vs. Continuous: The framework applies continuous physics concepts (resonance, phase,
PID control, waves) to a discrete, discontinuous system (Boolean logic).
●
The Cliff Problem: In a continuous system (like a guitar string), small changes in input lead to
small changes in output (smooth gradients). In SHA-256, the Avalanche Effect ensures that a
single bit flip completely randomizes the output. The "gradient" assumed by Samson's Law likely
does not exist; the landscape is a fractal cliff, not a smooth hill. Navigating via "drift" may be
mathematically impossible because the "drift" signal is indistinguishable from noise.
6.2 The Missing Actuator
In control theory, a feedback loop requires an actuator—a mechanism to apply the correction. In the
context of SHA-256, what is the actuator?
●
How do you translate a "harmonic error" of 0.05 into a specific bit-flip in the nonce?
●
The mapping from "Error Space" back to "Input Space" is exactly the preimage problem the
framework is trying to solve. The framework assumes this reverse-mapping is possible to "steer"
the system, but this assumes the solution to the very problem it posits.
10
6.3 Implications of Success: The "Grey Swan" Event
If, despite these criticisms, the logic-based approach proves viable, the implications are catastrophic for
modern digital infrastructure.
1
●
Collapse of Complexity: The distinction between P and NP complexity classes for cryptographic
problems would collapse. Inversion would become a polynomial-time engineering task.
●
End of Proof-of-Work: Bitcoin mining, which relies on the difficulty of finding "partial preimages"
(hashes with leading zeros), would be trivialized. A miner using "Harmonic Creation" could
calculate the winning nonce instantly without expending energy, destroying the economic security
of the network.
20----------- Page11 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 11
●
The AI Cryptanalyst: The framework points toward a future "AI Cryptanalyst" that does not
search but learns the underlying "physics" of code.
1
This AI would "read" a hash like a book,
unfolding its history through logical derivation.
VII. Conclusion
The investigation into "halting signal brute force SHA reversal logic vs search" reveals a profound
epistemological divide in cryptography.
The Search Paradigm rests on the thermodynamic certainty of chaos. It views SHA-256 as an entropy
machine, a shredder of information that leaves no path back. Here, the halting signal is a distant bell,
and brute force is the only way to find it. This is the safe, established view that secures the world's data
today.
The Logic Paradigm, epitomized by the Resonant/Nexus Framework, offers a daring counter-
narrative. It views SHA-256 as a structured, deterministic universe governed by "harmonic" laws. It
redefines the halting signal as an internal "resonance" ("FOLD: TRUE") and proposes that preimages
can be "created" through geodesic navigation.
While currently speculative and facing rigorous theoretical hurdles (specifically the "Continuum
Fallacy"), the Logic paradigm represents the ultimate ambition of cryptanalysis: to replace the
ignorance of the search with the certainty of the derivation. If the "halting signal" can indeed be
internalized—if the system can "feel" when it is close to a solution—then the walls of the event horizon
are not as impenetrable as we believe. The transition from "finding" to "creating" would mark the end
of the current cryptographic age and the beginning of a new, resonant computational era.
Works cited
1. Deep Research Paper Drafting Protocol,
https://drive.google.com/open?id=1yzq8rCNfvh0XIJl8NQQkczU9XPNmjoWNjRZKozJqe
ro
2. Programmatic SAT for SHA-256 Collision Attack, accessed January 8, 2026,
https://uwindsor.scholaris.ca/bitstreams/64fe0597-3fc6-415f-99d8-
d3e277f93ea7/download
3. SHA Encryption Explained: SHA-1 vs. SHA-2 vs. SHA-3 | Sectigo® Official, accessed
January 8, 2026, https://www.sectigo.com/blog/what-is-sha-encryption
4. Difficulty of collision vs preimage vs second-preimage attacks - Cryptography Stack
Exchange, accessed January 8, 2026,
https://crypto.stackexchange.com/questions/50223/difficulty-of-collision-vs-preimage-
vs-second-preimage-attacks----------- Page12 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 12
5. Are there two known inputs that give the same SHA256 output? : r/computerscience -
Reddit, accessed January 8, 2026,
https://www.reddit.com/r/computerscience/comments/12egpsu/are_there_two_known_
inputs_that_give_the_same/
6. accessed January 8, 2026, https://ftp.math.utah.edu/pub/tex/bib/imwut.bib
7. A Deep Dive into SHA-256: Working Principles and Applications | by Madan | Medium,
accessed January 8, 2026, https://medium.com/@madan_nv/a-deep-dive-into-sha-256-
working-principles-and-applications-a38cccc390d4
8. Preimage attack - Wikipedia, accessed January 8, 2026,
https://en.wikipedia.org/wiki/Preimage_attack
9. The Nexus Recursive Harmonic Framework: Formalizing Reality as Recursive
Computation, accessed January 8, 2026, https://zenodo.org/records/17983567
10. The Nexus 4 Framework - Hybrid Optical Modulator Concept .docx,
https://drive.google.com/open?id=1Bm3HVs2uWfFWh5bIilma8iSId2QthfMH
11. Recursive Harmonic Architecture Emerges , https://drive.google.com/open?id=1-
9D9nPeqfx1vgF-vEl430oOAhQuEAAONsaXKuBSvMAw
12. I don't think double sha256 makes any difference with regards to collisions. If ... - Hacker
News, accessed January 8, 2026, https://news.ycombinator.com/item?id=39836877
13. New Second-Preimage Attacks on Hash Functions - National Institute of Standards and
Technology, accessed January 8, 2026,
https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=918851
14. ELI5: Why is it that Sha256 cannot be reversible even though it always outputs the same
result for the same input given : r/explainlikeimfive - Reddit, accessed January 8, 2026,
https://www.reddit.com/r/explainlikeimfive/comments/15asg9t/eli5_why_is_it_that_sha
256_cannot_be_reversible/
15. Computational Complexity Theory - Stanford Encyclopedia of Philosophy, accessed
January 8, 2026, https://plato.stanford.edu/archives/fall2016/entries/computational-
complexity/
16. Computational requirements for breaking SHA-256? - Cryptography Stack Exchange,
accessed January 8, 2026,
https://crypto.stackexchange.com/questions/52571/computational-requirements-for-
breaking-sha-256----------- Page13 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 13
17. Is SHA-256 Secure Against Quantum Attacks? | Post-Quantum Security Center: From
VPN Vulnerabilities to Quantum Safe Victory - Gopher Security, accessed January 8,
2026, https://www.gopher.security/post-quantum/is-sha-256-secure-against-quantum-
attacks
18. Quantum Computers Threat to Bitcoin | by Przemek Chojecki - Medium, accessed
January 8, 2026, https://pchojecki.medium.com/quantum-computers-threat-to-bitcoin-
e1b57b0da2aa
19. SHA-256 Collision Attack with Programmatic SAT - arXiv, accessed January 8, 2026,
https://arxiv.org/html/2406.20072v1
20. SHA-256: (Probabilistic?) partial preimage possible? - Cryptography Stack Exchange,
accessed January 8, 2026, https://crypto.stackexchange.com/questions/8786/sha-256-
probabilistic-partial-preimage-possible
21. SHA-256 Collision Attack with Programmatic SAT - CEUR-WS.org, accessed January 8,
2026, https://ceur-ws.org/Vol-3717/paper5.pdf
22. The Nexus Recursive Harmonic Intelligence Framework - Deriving a Universal Harmonic
Phase Constant Across Scales - Zenodo, accessed January 8, 2026,
https://zenodo.org/records/18162886
