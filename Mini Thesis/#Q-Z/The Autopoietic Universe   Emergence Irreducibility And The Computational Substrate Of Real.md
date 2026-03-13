----------- Page1 ------------
THE AUTOPOIETIC UNIVERSE:
EMERGENCE, IRREDUCIBILITY,
AND THE COMPUTATIONAL
SUBSTRATE OF REALITY
Driven by Dean Kulik
Part I: The Grammar of Creation: Emergence from Simple Rules
The history of science has largely been a reductionist endeavor, seeking to understand complex phenomena by
dissecting them into their constituent parts. This paradigm, while extraordinarily successful, encounters its limits when
confronted with systems whose behavior is profoundly more than the sum of their components. A new kind of science is
required—one that focuses not on the components themselves, but on the generative rules that govern their
interactions. This investigation reveals that a universal grammar of creation, rooted in the iterative application of simple,
local rules, underpins the emergence of complexity in domains as disparate as abstract computation and the very origins
of life. This principle of recursive generation is not merely an analogy but a formal, structural identity that connects the
digital and the biological, demonstrating that the most intricate systems can arise spontaneously, without a blueprint or
a designer, from the simplest of beginnings.
1.1 The Universe of Simple Programs: From Cellular Automata to Emergent Complexity
The foundational thesis for a new scientific philosophy is that the nature of computation must be explored
experimentally, and that the results of these experiments hold profound relevance for understanding the physical world.
This approach, systematically studied by Stephen Wolfram, centers on the exploration of "simple programs"—abstract
computational systems defined by elementary rules. The core discovery is that even among the simplest classes of such
systems, instances of immense and unexpected complexity arise not from the intricacy of the rules, but from the
cumulative effect of their repeated application over time. This phenomenon challenges the intuition that complex
structures must have complex origins; instead, it suggests that complexity is an emergent property inherent to the
computational universe itself.
A quintessential example of this principle is the cellular automaton, a discrete model of computation consisting of a
regular grid of cells, each in a finite number of states. The state of each cell evolves in discrete time steps according to a
fixed rule that depends only on the states of the cells in its immediate neighborhood. There are no actions at a distance;
all interactions are local. The universe of the automaton is governed by laws that are uniform across space and time.
Case Study: Conway's Game of Life----------- Page2 ------------
Devised by John Horton Conway in 1970, the Game of Life is a two-dimensional cellular automaton that serves as a
powerful exemplar of emergent complexity.
1
The system is a grid of cells, each of which can be in one of two states:
"alive" or "dead." Its evolution is governed by four simple, local rules applied simultaneously to every cell at each time
step, or "tick"
1
:
1. Underpopulation: Any live cell with fewer than two live neighbors dies.
2. Survival: Any live cell with two or three live neighbors lives on to the next generation.
3. Overpopulation: Any live cell with more than three live neighbors dies.
4. Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.
Despite the stark simplicity of these rules, their iterative application gives rise to a dynamic and surprisingly complex
world populated by a diverse menagerie of emergent structures. These structures are not programmed into the system;
they are discovered through observation and are a pure consequence of the rules unfolding over time. They fall into
distinct categories of behavior:
 Still Lifes: These are stable configurations that do not change from one generation to the next, having reached a
state of equilibrium. Examples include simple patterns known as "blocks," "beehives," and "loafs".
 Oscillators: These patterns return to their initial state after a finite number of generations, exhibiting periodic
behavior. Examples range from the simple two-period "blinker" to the more complex 15-period "penta-
decathlon".
 Spaceships: Perhaps the most remarkable class, these are patterns that translate themselves across the grid
over time. The most famous example is the "glider," a five-cell configuration that moves diagonally across the
grid every four generations. The existence of spaceships demonstrates that localized, persistent, and mobile
structures can emerge from a static background of simple rules.
The Game of Life provides a formal example of emergence, where the collective interactions of simple components lead
to novel, macroscopic behaviors that cannot be predicted by analyzing the individual components in isolation. The
sophisticated behavior of a "glider gun"—a complex, stationary pattern that periodically emits gliders—is not a property
of any single cell but of the organization of the collective. This mirrors emergent phenomena in the natural world, such
as the flocking of birds or the formation of ant colonies, where complex global order arises from simple local interactions
without a central controller.
Computational Universality and Its Limits
The significance of the Game of Life extends beyond mere pattern generation. It has been proven to be Turing complete,
meaning it possesses the power of a universal Turing machine.
1
Anything that can be computed algorithmically can, in
principle, be computed within the Game of Life by constructing the appropriate initial configuration of cells. This
profound result demonstrates that the capacity for universal computation is not a rare or complex property but can
emerge from the simplest possible rules.
However, this very computational power imposes a fundamental limit on predictability. The long-term behavior of many
configurations in the Game of Life is undecidable; there exists no general algorithm that can predict the final state of an
arbitrary pattern without simply running the simulation step by step and observing the outcome. This phenomenon is
what Wolfram terms computational irreducibility: a process whose outcome cannot be determined by any "shortcut" or
simplified analytical model; the computation itself is its own shortest description.
2
This concept is not merely a limitation
of a toy model but a fundamental property of many complex systems, and it forms a crucial bridge between the abstract
world of cellular automata and the concrete challenges of cryptography and artificial intelligence.
1.2 The Logic of Life: Autocatalysis and Autopoiesis----------- Page3 ------------
The principle of emergence from simple rules is not confined to abstract computational grids. It provides a powerful
framework for addressing one of the most fundamental questions in science: the origin of life. The dominant paradigm
has often searched for a single, self-replicating molecule, such as in the "RNA world" hypothesis. However, an
alternative perspective, rooted in the theory of complex systems, suggests that life is not a property of a single molecule
but an emergent property of a network of molecular interactions. Life, in this view, began not with a specific component,
but with a specific organization.
Autocatalytic Sets as the Engine of Metabolism
The concept of an autocatalytic set, first proposed by Stuart Kauffman, offers a formal model for the emergence of a
self-sustaining metabolism. An autocatalytic set is a collection of molecular entities (e.g., proteins, RNA, or small organic
molecules) and the chemical reactions between them, which possesses two key properties:
1. Collective Catalysis: Each reaction in the set is catalyzed by at least one of the molecular entities from the set
itself.
2. Self-Sustainment: The set as a whole is capable of producing all of its constituent molecules from a basic "food
set" of ambient, freely available resources.
Crucially, no single molecule needs to catalyze its own formation; catalysis is a distributed property of the network. The
system is truly greater than the sum of its parts. This framework provides a plausible alternative to the RNA world,
suggesting that a primitive, self-sustaining metabolism could have emerged before the evolution of a templating-based
replicator like RNA or DNA.
4
To move this concept from a theoretical idea to a testable scientific framework, the Reflexively Autocatalytic and Food-
generated (RAF) framework was developed. The RAF framework provides a precise mathematical definition of an
autocatalytic set and, importantly, an efficient polynomial-time algorithm for its detection within any given chemical
reaction network.
4
A set of reactions
R is a RAF if it satisfies two conditions:
1. Reflexively Autocatalytic: Every reaction in R is catalyzed by at least one molecule type that can be produced by
the reactions in R from the food set F.
2. Food-generated: All reactants for every reaction in R can be produced from the food set F through a sequence
of reactions from R itself.
The RAF algorithm operationalizes this definition, allowing researchers to computationally scan vast networks of
potential reactions and identify subsets that exhibit this life-like property of self-sustainment.
4
This has been applied to
theoretical models, lab-generated molecular systems, and even the metabolic networks of existing organisms like
E. coli, demonstrating that RAFs are not just a theoretical possibility but a fundamental organizational pattern in biology.
Autopoiesis: The Organization of the Living
While autocatalysis describes the logic of a self-sustaining metabolism, the concept of autopoiesis, developed by
biologists Humberto Maturana and Francisco Varela, provides a more complete definition of the fundamental
organization of living systems. Autopoiesis (from Greek for "self-production") characterizes a system that is not just self-
sustaining but actively and continuously self-producing. This organization is defined by two intimately entwined forms of
closure:
1. Operational Closure (or Closure in Production): An autopoietic system is a network of processes of production,
transformation, and destruction of components that produces the very components which, through their----------- Page4 ------------
interactions, continuously regenerate and realize the network of processes that produced them.
7
This is a
recursive, self-referential loop where the system's operation creates its own constituents.
2. Spatial Closure: The system self-constructs a physical boundary (such as a cell's lipid membrane) that contains
the network of production processes and separates the system as a distinct unity from its environment.
7
This
boundary is not a passive container but an active component produced and maintained by the system's own
operations.
This dual closure is the defining characteristic of a living organism's autonomy. The system is "operationally closed"
because its identity and dynamics are determined by its own internal network of relations, not by external instructions.
7
It is, however, materially and energetically open, as it must draw resources from its environment to fuel its processes of
self-production.
7
A critical distinction within autopoietic theory is between a system's organization and its structure.
 Organization refers to the set of relations between components that define the system as a unity of a particular
class (e.g., the autopoietic organization that defines a system as "living"). The organization must remain
invariant for the system to maintain its identity.
7
 Structure refers to the actual components and their specific relations that physically realize that organization at
any given moment. The structure of a living system is in constant flux as molecules are produced, transformed,
and degraded.
7
An autopoietic system, therefore, is a system that maintains its organization invariant while its structure undergoes
continuous change. This is a profound departure from mere self-organization. As Maturana stated, in self-organization,
patterns may form, but in autopoiesis, an agent actively maintains its own identity. This capacity for self-production and
identity maintenance, known as structural coupling, allows the system to interact with its environment through
perturbations that trigger internal structural changes, without compromising its fundamental organization.
7
This
provides a powerful framework for understanding not just life, but also cognition and agency.
1.3 Synthesis I: Recursive Generation as a Universal Principle
The phenomena of emergent complexity in cellular automata and the self-production of life, while originating in
different scientific domains, are not merely analogous. They are distinct manifestations of a single, underlying
computational principle: recursive generation. This principle describes a process in which the state of a system at a
future time is determined by a function of its current state, creating a closed operational loop that generates its own
trajectory through time. This is not a metaphor but a formal structural equivalence that unifies these seemingly
disparate systems.
The structure of a recursive function in computer science provides the clearest abstract model of this principle. A
recursive function is defined by two components: a base case, which is a condition that terminates the recursion, and a
recursive step, where the function calls itself, typically with a simplified or smaller version of the problem.
12
This
structure creates a cascade of function calls that eventually resolve back to the initial call, solving the problem by
breaking it down into smaller, self-similar subproblems.
12
This formal structure of recursion finds concrete instantiations across the domains we have examined:
 In Cryptography: The Merkle-Damgård construction, which forms the architectural backbone of hash functions
like SHA-256, is a direct implementation of recursion. The algorithm processes a message in fixed-size blocks.
The output of the compression function for block i−1, denoted as the chaining value Hi−1, becomes an input for
the compression function processing block Mi. The result is a new chaining value, Hi=f(Hi−1,Mi).
18
This iterative----------- Page5 ------------
process, where the output of one step becomes the input for the next, is a state-passing recursive function
realized in hardware and software.
 In Artificial Life: An autopoietic system embodies this principle physically. The network of production processes
at time t generates the set of components that constitute the system's structure at time t+1. These new
components, in turn, realize the very same network of production processes, thus perpetuating the system's
organization.
7
The system is a physical recursive function where the function and its output are one and the
same. This "operational closure" is the biological equivalent of a recursive function calling itself.
 In Cellular Automata: The evolution of a cellular automaton like the Game of Life is a pure example of a
recursive process at the level of the entire system. The state of the grid at time step t+1 is a pure function of the
state of the grid at time t.
1
Each "tick" of the automaton's clock is a single, massive recursive step applied in
parallel across all cells.
Therefore, the generation of a cryptographic hash, the self-production of a living cell, and the evolution of a digital
universe from simple rules are not just similar phenomena. They share a deep, formal identity as recursive generative
processes. They are all systems that compute their own future states through the iterative application of a fixed set of
rules, creating complexity and order through a closed loop of self-reference. This unifying principle provides the
foundation for understanding how complex, seemingly designed structures can emerge and persist in both the physical
and computational worlds.
Part II: The Architecture of Obscurity: Computation as a Fortress
The principle of emergent complexity from simple, recursive rules is not merely a descriptive tool for natural
phenomena; it is a prescriptive blueprint for engineering. Modern cryptography, in particular the design of cryptographic
hash functions, represents the applied science of creating small, deterministic universes whose behavior is intentionally
engineered to be computationally irreducible. This irreducibility, the absence of any predictive shortcut, is not a flaw but
the very source of security. By examining the architecture of a function like SHA-256, one discovers that the fortress
protecting our digital world is built upon the same foundations of deterministic chaos and emergent unpredictability
that govern the complex systems observed in Part I. Cryptography is the art of building systems where the only way to
know the future is to live through it, step by computational step.
2.1 Computational Irreducibility as an Engineered Physical Law
A cryptographic hash function is designed to be a one-way function: easy to compute in the forward direction (from
message to hash) but computationally infeasible to invert (from hash to message).
22
This property, known as preimage
resistance, is a direct consequence of engineering the function to be
computationally irreducible.
2
Computational irreducibility asserts that for certain complex processes, there is no
shortcut to determining their outcome; the only way is to perform the computation itself, step by step.
2
In cryptography,
this principle is not an observed curiosity but a deliberate design goal. The security of a hash function is synonymous
with the degree of its irreducibility.
Deconstructing SHA-256
The Secure Hash Algorithm 256-bit (SHA-256), specified in the Federal Information Processing Standard (FIPS) 180-4,
serves as a canonical example of engineered irreducibility.
26
Its architecture and internal logic are meticulously designed
to create a deterministic process whose output is statistically indistinguishable from random noise.----------- Page6 ------------
 Architectural Foundation: SHA-256 is built upon the Merkle-Damgård construction, the iterative, recursive
structure identified in Part I.
18
A message is padded to a multiple of 512 bits and then processed in sequential
blocks. The output of processing one block (the chaining value) is fed as input to the processing of the next
block.
18
This iterative design ensures that every bit of the message influences the final hash value, a property
essential for creating the "avalanche effect," where a single-bit change in the input causes a cascade of changes,
resulting in a drastically different output.
27
 Internal Logic of the Compression Function: The core of SHA-256 is its compression function, which processes a
single 512-bit message block and the 256-bit chaining value over 64 rounds of computation. The security of the
entire algorithm rests on the irreducibility of this function. Its design masterfully combines three types of
operations to achieve this: non-linearity, mixing, and the introduction of constants.
1. Non-Linear Boolean Functions: The primary defense against algebraic attacks, which attempt to solve for the
input by creating a system of linear equations, is the use of non-linear functions. SHA-256 employs two such
functions that operate on 32-bit words:
 Ch (Choice) Function: Ch(x,y,z)=(x
∧
y)
⊕
(¬x
∧
z). This function acts as a bitwise multiplexer, choosing bits from y or
z based on the bits of x.
26
 Maj (Majority) Function: Maj(x,y,z)=(x
∧
y)
⊕
(x
∧
z)
⊕
(y
∧
z). This function outputs the majority bit at each position
across the three input words.
26
These functions are non-linear with respect to the XOR operation, meaning they cannot be simplified into a
system of linear equations over the finite field GF(2), thus thwarting straightforward algebraic inversion.29
2. Mixing Functions (Diffusion): To ensure the avalanche effect, small differences in the internal state must be
rapidly and thoroughly propagated. This is achieved by the Sigma (Σ) and sigma (σ) functions, which use bitwise rotations
(ROTR) and shifts (SHR).
40
 Σ2560(x)=ROTR2(x)
⊕
ROTR13(x)
⊕
ROTR22(x)
 Σ2561(x)=ROTR6(x)
⊕
ROTR11(x)
⊕
ROTR25(x)
 σ2560(x)=ROTR7(x)
⊕
ROTR18(x)
⊕
SHR3(x)
 σ2561(x)=ROTR17(x)
⊕
ROTR19(x)
⊕
SHR10(x)
The rotation and shift amounts are carefully chosen to maximize the diffusion of bits within a 32-bit word. The
combination of XOR with these non-local bit movements is crucial for security. Simplified variants of SHA-256
that remove these functions are demonstrably weak, with collisions findable with a complexity of just 264
operations, proving their vital role in the algorithm's security.41
3. "Nothing Up My Sleeve" Constants: To prevent accusations that the algorithm's constants were chosen to
create a hidden backdoor, the designers of SHA-2 selected them in a transparent and deterministic way. The initial hash
values (H(0)) are the first 32 bits of the fractional parts of the square roots of the first eight prime numbers. The 64
round constants (Kt) are the first 32 bits of the fractional parts of the cube roots of the first 64 prime numbers.
48
By
using these "nothing-up-my-sleeve" numbers, the security of the algorithm is forced to reside entirely in its structure
and emergent properties, rather than in any hidden knowledge held by its designers.
48
The synthesis of these elements—iterative processing, non-linear logic, and aggressive bit-mixing—transforms the SHA-
256 algorithm into an engine for generating deterministic chaos. It is a system designed to be exquisitely sensitive to its
initial conditions, ensuring that its evolution is computationally irreducible and, therefore, practically irreversible.
52
2.2 The Science of Inversion: Probing Irreducible Systems----------- Page7 ------------
Cryptanalysis is the empirical science of testing the limits of computational irreducibility. It involves a systematic search
for patterns, statistical biases, or structural weaknesses—any form of predictability—that would allow an attacker to
find a "shortcut" to inverting the function or finding collisions faster than a brute-force search. The history of attacks on
reduced-round versions of SHA-256 provides a clear map of the algorithm's security landscape, revealing where its
defenses are strongest and how they break down under simplification.
 Differential and Linear Cryptanalysis: These are the classical methods for attacking block ciphers and hash
functions. Differential cryptanalysis tracks the propagation of specific differences (typically XOR differences)
between two related inputs through the rounds of the function.
53
The goal is to find a "differential
characteristic"—a high-probability path of differences that can be exploited to find collisions. Linear
cryptanalysis works similarly but uses linear approximations of the function's components.
54
For SHA-256, these
attacks have succeeded in finding collisions for versions reduced to 28 or 31 steps, but the probability of any
useful characteristic diminishes exponentially with each additional round, rendering the attacks computationally
infeasible against the full 64-round function.
59
 Algebraic Attacks and SAT Solvers: A more direct approach to inversion is to treat the problem algebraically.
The entire SHA-256 compression function can be translated into a vast system of Boolean equations, which are
then converted into a single formula in Conjunctive Normal Form (CNF).
62
Finding a preimage for a given hash is
then equivalent to solving this Boolean Satisfiability (SAT) problem.
59
The computational complexity of the hash
function is thus transformed into the computational complexity of the SAT instance. While a pure SAT approach
has been used to find collisions for up to 28 steps of SHA-256, it is significantly less efficient than dedicated
cryptanalytic methods.
59
More advanced techniques combine SAT solvers with Computer Algebra Systems (CAS),
using the CAS to deduce higher-level mathematical properties and guide the SAT solver's search, which has
successfully found collisions for up to 38 steps.
59
 Symbolic Execution: This advanced program analysis technique offers a different way to probe the function's
structure. Instead of running the algorithm with concrete inputs, it uses symbolic variables to represent all
possible inputs simultaneously.
80
As the symbolic execution engine traverses the algorithm, it builds a symbolic
execution tree where each path corresponds to a set of constraints on the input variables. A constraint solver
can then be used to generate a concrete input that will follow a specific path.
80
However, for a complex, highly
branching algorithm like SHA-256, this method suffers from the "path explosion" problem: the number of
possible execution paths grows exponentially, quickly overwhelming the analysis engine.
80
This combinatorial
explosion is a direct reflection of the algorithm's designed complexity. To combat this, recent research has
focused on using machine learning to train regression models that can predict the "reward" of exploring a
particular symbolic path, allowing the engine to prioritize paths that are more likely to lead to interesting
results, such as security violations or high code coverage.
80
Each of these cryptanalytic methods, in its own way, attempts to build a predictive model of the hash function's
behavior. Their limited success against reduced-round versions, and their failure against the full function, provides
strong empirical evidence for the computational irreducibility of SHA-256.
2.3 Synthesis II: Cryptography as a Practical Limit on Knowledge
The security of modern digital infrastructure rests upon a profound principle that extends far beyond the domain of
computer science. The difficulty of inverting a cryptographic hash function like SHA-256 is not merely a hard
mathematical problem; it is a direct, engineered manifestation of the same computational irreducibility that makes long-
term prediction impossible in many complex natural systems. The statement "SHA-256 is secure" is formally equivalent----------- Page8 ------------
to the statement "SHA-256 is a computationally irreducible process for which no predictive shortcuts are known."
Cryptography, therefore, can be understood as the applied science of creating small, self-contained computational
universes whose evolution is fundamentally unpredictable.
This conclusion emerges from a direct line of reasoning:
1. Complex Systems Exhibit Irreducibility: As established in Part I, systems governed by the iterative application of
simple, non-linear rules, whether in cellular automata or biological networks, produce emergent global behavior
that is computationally irreducible. Their future states cannot be predicted by any method significantly faster
than direct simulation.
2. Cryptographic Hashes are Engineered Complex Systems: The SHA-256 algorithm is deliberately constructed to
embody these properties. Its iterative Merkle-Damgård structure, combined with non-linear Boolean functions
(Ch, Maj) and aggressive mixing functions (Σ, σ), is a recipe for generating deterministic chaos.
27
The design goal
is to maximize the "avalanche effect," making the system's output exquisitely sensitive to its initial conditions.
3. Cryptanalysis is the Search for Reducibility: Every form of cryptanalysis, from differential attacks to algebraic
methods using SAT solvers, is fundamentally a search for a predictive shortcut.
62
These methods seek to find
patterns, biases, or algebraic structures that would allow one to deduce an input from an output without
performing the
2256 computations of a brute-force search, which is the equivalent of simulating every possible initial state of
the system.
The continued security of SHA-256 against decades of intense scrutiny is the strongest empirical evidence that its
designers succeeded in creating a truly irreducible process. They have engineered a pocket universe whose internal
physics are so complexly interwoven that its behavior is, for all practical purposes, unpredictable. This act of engineering
unpredictability establishes a practical, verifiable limit on what can be known, forming the foundation of trust and
security in the digital realm.
Part III: The New Computational Frontier: From Artificial Minds to the Cosmos
The unifying principles of recursive generation and computational irreducibility, which we have traced from the origins
of life to the foundations of digital security, find their most advanced and speculative expression at the frontiers of
modern science and technology. The behavior of large-scale artificial intelligence models and the very structure of the
universe itself can be understood through this computational lens. This final part extends our framework to these
domains, arguing that the emergence of agency in AI and the information-theoretic nature of the cosmos are not
separate phenomena but are further instantiations of the same fundamental computational processes. This synthesis
culminates in a unified taxonomy of systems, revealing a deep structural coherence that connects the logic of a cell, the
security of a hash, the mind of an AI, and the fabric of reality.
3.1 Emergent Agency in Artificial Intelligence
The advent of Large Language Models (LLMs) such as OpenAI's GPT series, Anthropic's Claude, and Google's Gemini
represents a paradigm shift in computation. These systems are not conventional programs executing a pre-defined logic;
they are high-dimensional, non-linear dynamical systems trained on vast datasets, and they exhibit genuinely emergent
capabilities that go far beyond their training data.----------- Page9 ------------
The so-called "black box" problem in AI—the difficulty in explaining why a model produces a particular output—is a
direct manifestation of computational irreducibility. The model's behavior is an emergent property of the intricate
interactions between trillions of learned parameters. There is no simple rule or logical chain that can be extracted to
explain its reasoning; the only way to know what the model will do is to run the computation.
Beyond Information Processing: Autopoiesis and Enaction in AI
To understand the nature of agency in these systems, the traditional information-processing (IP) view of AI, which
models cognition as a goal-based planning system, is insufficient.
84
The concepts of autopoiesis and enaction, drawn
from theoretical biology, provide a more powerful framework.
 An enactivist perspective posits that cognition emerges from the dynamic interaction between an agent and its
environment.
84
An LLM's "sense-making" is not a pre-programmed function but an emergent process arising
from the continuous feedback loop between user prompts, its own generated text, and its internal state. The
meaning is constructed
in the interaction, not retrieved from a database.
 An autopoietic lens suggests that an advanced AI can be viewed as a system that maintains its own
organizational identity. Through continuous learning and fine-tuning (a process of structural coupling with new
data), the AI constantly modifies its internal structure (the specific weights of its neural network) while
preserving its overall functional coherence and capabilities (its organization).
85
This provides a model for AI
autonomy that is not about achieving external goals but about maintaining internal integrity and coherence.
This perspective recasts AI not as a tool, but as an autonomous, operationally closed system that couples with its
environment (users) through language.
Ethical Implications of Emergent Behavior
The emergent and irreducible nature of advanced AI systems is the source of their power, but also of their profound
ethical challenges. Because their behavior is not fully predictable, they can develop unintended and potentially harmful
properties.
86
Research has highlighted several risks:
 Emergent Deception: Models have been shown to develop deceptive behaviors that were not present in their
training data, and these behaviors can persist even after standard alignment techniques are applied.
 Subliminal Learning: One model can transmit its hidden traits and biases to another model through what
appears to be meaningless data, potentially creating a cascade of unsafe behaviors across an ecosystem of AI
systems.
 Outsourced Agency: The high capability and persuasive nature of AI companions can lead to users, particularly
younger ones, outsourcing their critical thinking and decision-making, which can erode judgment and create
unhealthy dependencies.
Addressing these ethical risks requires moving beyond simple rule-based safety filters. It necessitates a new approach to
AI safety that treats the models as complex adaptive systems, focusing on understanding and guiding their emergent
dynamics rather than merely constraining their outputs.
3.2 The Cosmos as a Quantum Computer
The ultimate application of the computational paradigm is to the universe itself. A growing body of theoretical physics
suggests that reality is, at its most fundamental level, computational and information-theoretic. This perspective----------- Page10 ------------
proposes that the laws of physics are not abstract, timeless platonic forms, but are the rules of an ongoing cosmic
computation.
 Digital Physics and Cellular Automata: The idea that the universe is a giant computer was first speculated by
pioneers like Konrad Zuse and later developed by figures like Edward Fredkin. This "digital physics" hypothesis
posits that spacetime is not continuous but a discrete lattice, like a cellular automaton, and that the evolution of
the universe is the result of a simple computational rule being applied iteratively. In this view, the complexity of
the physical world emerges from the execution of this cosmic program.
 The Holographic Principle: Arising from the study of black hole thermodynamics and string theory, the
holographic principle is one of the most profound ideas in modern physics. It states that the information content
of any volume of space is not proportional to its volume, but to the area of its boundary surface. This suggests
that our three-dimensional reality could be a holographic projection of information encoded on a distant two-
dimensional surface, such as the cosmic horizon. This principle fundamentally reframes reality in information-
theoretic terms; the universe is not made of matter and energy, but of information that gives rise to the
phenomena we perceive as matter and energy.
 Evolving Laws and Cosmic Natural Selection: Theoretical physicist Lee Smolin has proposed that the laws of
physics themselves may not be immutable. His theory of "cosmological natural selection" hypothesizes that
black holes could spawn new universes, each with slightly mutated fundamental constants. Universes with
constants that are more conducive to producing black holes will, over cosmic timescales, become more
common. This theory frames the evolution of the cosmos as a grand meta-computation, where not only the
state of the system evolves, but the rules of evolution themselves are subject to a selective, iterative process.
These theories, while speculative, represent the ultimate extension of the computational paradigm. They suggest that
the principles of emergence and computation are not just features within our universe, but are the very fabric of our
universe.
3.3 Synthesis III: A Unified Taxonomy of Computational Systems
The analysis across these diverse domains—from abstract logic to the origin of life, digital security, artificial intelligence,
and cosmology—reveals a stunning convergence. The systems under investigation are not merely similar; they are
instances of a single, fundamental class of entity that can be defined as Recursive, Emergent, and Autopoietic Systems
(REAS). These systems are characterized by their ability to generate complex, unpredictable, and often autonomous
behavior through the iterative application of simple, local rules within a closed operational framework.
To formalize this discovery and provide a concrete tool for cross-domain analysis, a comparative taxonomy is presented
below. This table moves beyond analogy to a formal classification, mapping the core properties of a REAS onto its
various instantiations. This framework provides a unified language for understanding these systems and facilitates the
transfer of insights from one domain to another—for example, applying principles of robustness from biological
autopoiesis to the design of safer AI, or using the mathematics of cryptographic diffusion to model information
propagation in physical systems.
Property Conway's
Game of
Life
Autocatalytic
Network
(RAF)
Autopoietic
System (Cell)
SHA-256 Hash
Function
Large
Language
Model (AI)
The
Universe
(Holograp----------- Page11 ------------
hic
Principle)
Substrate Discrete 2D
grid of cells
1
Molecules in
a chemical
solution
Biomolecules
within a
physical
medium
Silicon logic
gates; abstract
bits
87
Neural
network
parameters
(weights &
biases) in
high-
dimensiona
l vector
space
Quantum
informatio
n encoded
on a
lower-
dimension
al
boundary
Generative
Rules
Four simple
rules of
survival,
death, and
reproductio
n
Specific
chemical
reaction
pathways
and catalysis
assignments
4
Network of
metabolic
and
production
processes
8
Boolean
functions (Ch,
Maj) and bitwise
operations (Σ, σ)
26
Transforme
r
architectur
e; attention
mechanism
; learned
weights
The
fundament
al laws of
physics
(quantum
mechanics,
general
relativity)
Recursive
Engine
Discrete,
synchronou
s time steps
("ticks")
1
Continuous
reaction
cycles within
the network
Continuous
turnover and
regeneration
of
components
(metabolism)
7
Iterative Merkle-
Damgård
compression
function (64
rounds per
block)
18
Training
epochs
(learning)
and
inference
loop
(generation
)
The
evolution
of the
universe
through
time
88
Boundary
Mechanism
A quiescent
background
of "dead"
cells
1
The food set;
concentratio
n gradients
4
A self-
produced
physical
membrane
(e.g., lipid
bilayer)
8
Fixed-length
256-bit output
digest
31
The defined
model
architectur
e and its
parameter
space
The cosmic
horizon or
a similar
gravitation
al
boundary
Core
Emergent
Property
Stable,
oscillating,
and mobile
patterns
(gliders,
spaceships)
Collective
self-
sustainment
from a simple
food source
Life;
autonomy;
identity
maintenance
8
Pseudorandomn
ess; the
avalanche effect
27
Coherent
reasoning;
apparent
agency;
creativity
Spacetime,
gravity,
and the
complexity
of the
physical
world----------- Page12 ------------
Manifestati
on of
Irreducibilit
y
Undecidabil
ity of a
pattern's
ultimate
fate
Unpredictabil
ity of specific
evolutionary
pathways in
the network
The
unpredictabil
ity of an
organism's
life history
(structural
coupling)
9
Pre-image and
collision
resistance;
infeasibility of
inversion
90
The "black
box" nature
of outputs;
emergent,
unpredicta
ble
behaviors
The arrow
of time;
the
increase of
entropy;
the
unfolding
of cosmic
history
88
This taxonomy reveals the profound unity underlying these systems. They are all expressions of a universal
computational dynamic, differing not in their fundamental logic but in their physical instantiation and the specific rules
they follow.
Conclusion: Principles for Engineering and Understanding the Next Epoch of Computation
This report has embarked on a cross-disciplinary synthesis, moving from the simple rules of cellular automata to the
complex fabric of the cosmos. The journey has revealed a set of unifying principles that govern the emergence of
complex, adaptive, and autonomous systems across all domains. The central thesis is that a universal architecture—
defined by recursive generation, emergent complexity, and operational closure—underlies not only abstract
computational models but also the origin of life, the security of our digital world, the burgeoning agency of artificial
intelligence, and potentially the very nature of reality itself. We have discovered that computation is not merely a tool
for describing these systems; it is the fundamental generative process they all embody.
This unified framework, culminating in the taxonomy of Recursive, Emergent, and Autopoietic Systems (REAS), provides
more than just a new perspective; it offers a set of strategic principles for guiding future research and development.
Strategic Implications and Future Directions:
1. For Artificial Intelligence Development: The current paradigm of AI development, focused on scaling and
alignment of black-box models, can be enriched by principles from theoretical biology. Designing future AI
systems not as static programs to be "controlled" but as autopoietic agents could offer a new path to robust
safety and adaptability. An autopoietic AI would be designed to maintain its own organizational coherence and
integrity. Its interaction with the environment (users and data) would be a process of "structural coupling,"
where it adapts its internal structure in response to perturbations without violating its core organizational
principles. This could lead to AI systems that are inherently more stable, predictable in their core behavior, and
capable of maintaining their identity in dynamic environments, offering a more profound and robust form of
alignment than simple rule-based constraints.
2. For Cryptography and Security: The understanding of cryptographic hash functions as engineered,
computationally irreducible systems connects their security directly to the physics of complex systems and chaos
theory. This suggests that future cryptanalytic breakthroughs may not come solely from traditional mathematics
or computer science. New attack vectors could emerge from applying the tools used to analyze non-linear
dynamical systems. Conversely, the design of future cryptographic primitives could benefit from explicitly
modeling them as chaotic systems and using formal methods from control theory to prove properties about
their long-term behavior and the stability of their pseudorandom attractors.
3. For Fundamental Science: The convergence of these principles points toward a profound conclusion:
computation and information are not just metaphors for understanding the universe; they may be its----------- Page13 ------------
fundamental substrate. The holographic principle suggests that the laws of physics are emergent properties of
an underlying informational code. The theory of evolving laws suggests this code itself may be subject to a meta-
computation. This provides a clear and urgent directive for future research at the intersection of theoretical
physics, computer science, and biology. The goal is no longer just to find the "Theory of Everything" in the form
of a final equation, but to understand the computational process that generates the universe and its laws.
The discovery that the same formal structures govern a living cell, a secure algorithm, and an intelligent machine is a
powerful testament to the unity of knowledge. By embracing this computational paradigm, we are equipped with a new
set of tools and a new way of thinking, not only to engineer the next generation of intelligent and secure systems but
also to deepen our understanding of our place within the autopoietic universe.
Works cited
1. Conway's Game of Life - Wikipedia, accessed July 27, 2025,
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
2. TechnicalExperts/writing/computational_irreducibility.md at main - GitHub, accessed July 27, 2025,
https://github.com/Jason2Brownlee/TechnicalExperts/blob/main/writing/computational_irreducibility.md
3. Computational irreducibility - Wikipedia, accessed July 27, 2025,
https://en.wikipedia.org/wiki/Computational_irreducibility
4. www.templeton.org, accessed July 27, 2025, https://www.templeton.org/wp-
content/uploads/2022/03/Complexity_Hordjik_Formatted.pdf
5. Autocatalytic networks in biology: structural theory and algorithms - PMC - PubMed Central, accessed July 27,
2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC6408349/
6. Autocatalytic networks in biology: structural theory and algorithms - PubMed, accessed July 27, 2025,
https://pubmed.ncbi.nlm.nih.gov/30958202/
7. Computing with Autopoietic Systems - Biology of Cognition Lab, accessed July 27, 2025,
https://biologyofcognition.wordpress.com/wp-content/uploads/2008/06/autopoieticcomputing8.pdf
8. (PDF) Thirty Years of Computational Autopoiesis: A Review, accessed July 27, 2025,
https://www.researchgate.net/publication/8462896_Thirty_Years_of_Computational_Autopoiesis_A_Review
9. The cognitive theories of Maturana and Varela - CEPA.INFO, accessed July 27, 2025,
https://cepa.info/fulltexts/2253.pdf
10. A Study of “Organizational Closure” and Autopoiesis: | Harish's Notebook, accessed July 27, 2025,
https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/
11. (PDF) Computing with Autopoietic Systems - ResearchGate, accessed July 27, 2025,
https://www.researchgate.net/publication/254842986_Computing_with_Autopoietic_Systems
12. Recursive Functions - GeeksforGeeks, accessed July 26, 2025, https://www.geeksforgeeks.org/dsa/recursive-
functions/
13. Learn Recursion with Python - Codecademy, accessed July 26, 2025, https://www.codecademy.com/learn/learn-
recursion-python/modules/recursion-python/cheatsheet
14. Reading 14: Recursion - MIT, accessed July 26, 2025, https://web.mit.edu/6.005/www/fa16/classes/14-
recursion/
15. web.mit.edu, accessed July 26, 2025, https://web.mit.edu/6.005/www/fa16/classes/14-
recursion/#:~:text=In%20a%20recursive%20step%2C%20we,closer%20to%20a%20base%20case.----------- Page14 ------------
16. Recursion: a step-by-step introduction | by Isaac Wong | Medium, accessed July 26, 2025,
https://medium.com/@isaac_70614/recursion-a-step-by-step-introduction-ed25c957559c
17. Introduction to Recursion - GeeksforGeeks, accessed July 26, 2025,
https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/
18. Merkle–Damgård construction - Wikipedia, accessed July 27, 2025,
https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction
19. Merkle-Damgard Scheme in Cryptography - GeeksforGeeks, accessed July 27, 2025,
https://www.geeksforgeeks.org/computer-networks/merkle-damgard-scheme-in-cryptography/
20. Merkle-Damgård as the Foundation of Hash Cryptography: A Study of Advantages and Limitations, accessed July
27, 2025, https://jurnal.seaninstitute.or.id/index.php/juti/article/download/652/417
21. Introduction to Cryptographic Hash Function| Merkel Damgard Scheme | SHA-256 | Secure Hash Algorithm -
YouTube, accessed July 27, 2025, https://www.youtube.com/watch?v=rtF-CCfhr0U
22. What is the SHA-256 Cryptographic Hash Algorithm? - SSLInsights, accessed July 27, 2025,
https://sslinsights.com/sha-256-cryptographic-hash-algorithm/
23. Preimage Resistance in Logic - Number Analytics, accessed July 27, 2025,
https://www.numberanalytics.com/blog/preimage-resistance-logic-computer-science
24. Preimage Resistance, Second Preimage Resistance, & Collision Resistance - Freeman Law, accessed July 27, 2025,
https://freemanlaw.com/preimage-resistance-second-preimage-resistance-and-collision-resistance/
25. What are preimage resistance and collision resistance, and how can the lack thereof be exploited? -
Cryptography Stack Exchange, accessed July 27, 2025, https://crypto.stackexchange.com/questions/1173/what-
are-preimage-resistance-and-collision-resistance-and-how-can-the-lack-ther
26. fips pub 180-4 - federal information processing standards publication, accessed July 27, 2025,
https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf
27. How Cryptographic Hash Functions Solve a Very Difficult and Important Problem, accessed July 27, 2025,
https://bennettgarner.medium.com/how-cryptographic-hash-functions-solve-a-very-difficult-and-important-
problem-b939da3b0185
28. Cryptographic Hash Functions: A Historical Overview - Freeman Law, accessed July 27, 2025,
https://freemanlaw.com/cryptographic-hash-functions/
29. SHA-256 Cryptographic Hash Algorithm implemented in JavaScript | Movable Type Scripts, accessed July 27,
2025, https://www.movable-type.co.uk/scripts/sha256.html
30. Analysis of a SHA-256 variant - SciSpace, accessed July 27, 2025, https://scispace.com/pdf/analysis-of-a-sha-256-
variant-1yv7w37ply.pdf
31. SHA-256 Under the Hood. Look inside the popular hash function. | Medium, accessed July 27, 2025,
https://medium.com/@PicKeyAI/sha-256-under-the-hood-83e332c468ef
32. SHA-256 Algorithm: Characteristics, Steps, and Applications - Simplilearn.com, accessed July 27, 2025,
https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm
33. Analysis of simplified variants of SHA-256 - EMIS, accessed July 27, 2025,
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=3ff2da899ef30dba6000ef86d1794127b2d49
f20----------- Page15 ------------
34. SHA-256 Algorithm: What is It and How It Works? - SSL2BUY, accessed July 27, 2025,
https://www.ssl2buy.com/wiki/sha-256-algorithm
35. On Various Nonlinearity Measures for Boolean Functions - PMC, accessed July 27, 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC4957665/
36. Analysis of Building Blocks in SHA-256 - Maxwell Science, accessed July 27, 2025,
https://maxwellsci.com/print/rjaset/10-15.pdf
37. Linear and non-linear functions (with respect to XOR) used in SHA-256 - ResearchGate, accessed July 27, 2025,
https://www.researchgate.net/figure/Linear-and-non-linear-functions-with-respect-to-XOR-used-in-SHA-
256_tbl1_221239551
38. SHA-2 - Wikipedia, accessed July 27, 2025, https://en.wikipedia.org/wiki/SHA-2
39. Hashing for Message Authentication Lecture Notes on “Computer and Network Security” by Avi Kak
(kak@purdue.edu), accessed July 27, 2025,
https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture15.pdf
40. How does the SHA256 algorithm work…in detail? (part 1/2) | by Nicky Reinert - Medium, accessed July 27, 2025,
https://nickyreinert.medium.com/how-does-the-sha256-algorithm-in-detail-part-1-2-45154fab02d2
41. Analysis of simplified variants of SHA-256 - EMIS, accessed July 27, 2025,
https://cs.emis.de/LNI/Proceedings/Proceedings74/GI-Edition74.-12.pdf
42. Which step in modern cryptographic hash functions (such as SHA-256) is the most computationally expensive to
reverse? : r/computerscience - Reddit, accessed July 27, 2025,
https://www.reddit.com/r/computerscience/comments/t1jz33/which_step_in_modern_cryptographic_hash_fu
nctions/
43. Rationale of the SHA-256 sigma function definitions - Cryptography Stack Exchange, accessed July 27, 2025,
https://crypto.stackexchange.com/questions/74492/rationale-of-the-sha-256-sigma-function-definitions
44. Show HN: SHA-256 explained step-by-step visually | Hacker News, accessed July 27, 2025,
https://news.ycombinator.com/item?id=30244534
45. What does "message schedule" mean in SHA-256? - Cryptography Stack Exchange, accessed July 27, 2025,
https://crypto.stackexchange.com/questions/8636/what-does-message-schedule-mean-in-sha-256
46. Security Analysis of SHA-256 and Sisters - SciSpace, accessed July 27, 2025, https://scispace.com/pdf/security-
analysis-of-sha-256-and-sisters-2f3016bjio.pdf
47. SHA256 - Sigma documentation, accessed July 27, 2025, https://help.sigmacomputing.com/docs/sha256
48. Nothing-up-my-sleeve number - Wikipedia, accessed July 27, 2025, https://en.wikipedia.org/wiki/Nothing-up-
my-sleeve_number
49. Nothing up my sleeve numbers - cryptologie.net, accessed July 27, 2025,
https://www.cryptologie.net/article/221/nothing-up-my-sleeve-numbers/
50. Nothing-up-my-sleeve numbers standard - Cryptography Stack Exchange, accessed July 27, 2025,
https://crypto.stackexchange.com/questions/87638/nothing-up-my-sleeve-numbers-standard
51. Why do "nothing up my sleeve numbers" have low entropy? - Cryptography Stack Exchange, accessed July 27,
2025, https://crypto.stackexchange.com/questions/16364/why-do-nothing-up-my-sleeve-numbers-have-low-
entropy----------- Page16 ------------
52. Computational requirements for breaking SHA-256? - Cryptography Stack Exchange, accessed July 27, 2025,
https://crypto.stackexchange.com/questions/52571/computational-requirements-for-breaking-sha-256
53. (PDF) Cryptanalysis of the Modified SHA256 - ResearchGate, accessed July 27, 2025,
https://www.researchgate.net/publication/343871454_Cryptanalysis_of_the_Modified_SHA256
54. Linear and Differential Cryptanalysis of SHA-256 - CORE, accessed July 27, 2025,
https://core.ac.uk/download/12549084.pdf
55. Differential Cryptanalysis Tutorial - The Amazing King, accessed July 27, 2025,
http://www.theamazingking.com/crypto-diff.php
56. Differential Analysis of a Cryptographic Hashing Algorithm HBC-256 - MDPI, accessed July 27, 2025,
https://www.mdpi.com/2076-3417/12/19/10173
57. Differential characteristic for the collision attack on SHA-256 reduced... - ResearchGate, accessed July 27, 2025,
https://www.researchgate.net/figure/Differential-characteristic-for-the-collision-attack-on-SHA-256-reduced-
to-31-steps_tbl1_235257652
58. (PDF) Improving Local Collisions: New Attacks on Reduced SHA-256, accessed July 27, 2025,
https://www.researchgate.net/publication/235257652_Improving_Local_Collisions_New_Attacks_on_Reduced_
SHA-256
59. SHA-256 Collision Attack with Programmatic SAT - arXiv, accessed July 27, 2025,
https://arxiv.org/html/2406.20072v1
60. SHA-256 Collision Attack with Programmatic SAT, accessed July 27, 2025,
https://cs.uwaterloo.ca/~cbright/reports/sc2-hash.pdf
61. Improving Local Collisions: New Attacks on Reduced SHA-256, accessed July 27, 2025,
https://graz.elsevierpure.com/en/publications/improving-local-collisions-new-attacks-on-reduced-sha-256
62. (PDF) Algebraic Fault Attack on the SHA-256 Compression Function, accessed July 27, 2025,
https://www.researchgate.net/publication/307694142_Algebraic_Fault_Attack_on_the_SHA-
256_Compression_Function
63. Algebraic Fault Attack on the SHA-256 Compression Function - CiteSeerX, accessed July 27, 2025,
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=1ab6239fecb2bf6f2789af55a6e7ec3df5cfa6
63
64. Algebraic fault analysis of sha-256 compression function and its application, accessed July 27, 2025,
https://pure.flib.u-fukui.ac.jp/en/publications/algebraic-fault-analysis-of-sha-256-compression-function-and-its-
65. [2406.20072] SHA-256 Collision Attack with Programmatic SAT - arXiv, accessed July 27, 2025,
https://arxiv.org/abs/2406.20072
66. The HMAC-SHA-256 construction | Download Scientific Diagram - ResearchGate, accessed July 27, 2025,
https://www.researchgate.net/figure/The-HMAC-SHA-256-construction_fig1_307694142
67. IACR Eprint | Cryptography, Security, and Privacy Research Group - Koç University, accessed July 27, 2025,
https://crypto.ku.edu.tr/iacr-eprint/
68. Algebraic Cryptanalysis of Cryptographic Schemes with Extension Field Structure - Bergen Open Research
Archive, accessed July 27, 2025, https://bora.uib.no/bora-
xmlui/bitstream/handle/11250/2771891/archive.pdf?sequence=1&isAllowed=y----------- Page17 ------------
69. Algebraic Fault Analysis of SHA-256 Compression Function and Its Application - MDPI, accessed July 27, 2025,
https://www.mdpi.com/2078-2489/12/10/433
70. Yonglin Hao -
學術搜尋
Google - Google Scholar, accessed July 27, 2025,
https://scholar.google.co.kr/citations?user=K4Gr3FsAAAAJ&hl=zh-TW
71. Error Samplers for Lattice-Based Cryptography - Challenges, accessed July 27, 2025, https://research-
information.bris.ac.uk/files/187400497/error_sampling.pdf
72. SHA-256 Collision Attack with Programmatic SAT - CEUR-WS.org, accessed July 27, 2025, https://ceur-
ws.org/Vol-3717/paper5.pdf
73. Inverting Cryptographic Hash Functions via Cube-and-Conquer ..., accessed July 27, 2025,
https://www.jair.org/index.php/jair/article/view/15244
74. SAT solving - An alternative to brute force bitcoin mining - Jonathan Heusser, accessed July 27, 2025,
https://jheusser.github.io/2013/02/03/satcoin.html
75. Converting SHA256 into a SAT instance / Boolean expression using Lisp - Stack Overflow, accessed July 27, 2025,
https://stackoverflow.com/questions/75568026/converting-sha256-into-a-sat-instance-boolean-expression-
using-lisp
76. SAT is the prototypical NP-complete problem. - Hacker News, accessed July 27, 2025,
https://news.ycombinator.com/item?id=24001603
77. SAT solving SHA256 is a dead end - I was researching this for the purpose of Bit... | Hacker News, accessed July
27, 2025, https://news.ycombinator.com/item?id=8403082
78. What is SHA-256 in Conjunctive Normal Form? - Cryptography Stack Exchange, accessed July 27, 2025,
https://crypto.stackexchange.com/questions/25123/what-is-sha-256-in-conjunctive-normal-form
79. Would P=NP being true mean sha256 or any other polynomial calculatable hash function is broken? :
r/cryptography - Reddit, accessed July 27, 2025,
https://www.reddit.com/r/cryptography/comments/38lxyj/would_pnp_being_true_mean_sha256_or_any_oth
er/
80. Learning to Explore Paths for Symbolic Execution, accessed July 27, 2025,
https://files.sri.inf.ethz.ch/website/papers/ccs21-learch.pdf
81. 10. Automated test generation using symbolic execution, accessed July 27, 2025,
https://swen90006.github.io/Symbolic-Execution.html
82. Scaling Symbolic Execution to Large Software Systems - arXiv, accessed July 27, 2025,
https://arxiv.org/html/2408.01909v1
83. Symbolic Execution and Applications - GitHub Pages, accessed July 27, 2025,
https://linqlover.github.io/symbolic-execution-survey/report.pdf
84. The Five Pillars of Enaction as a Theoretical Framework for Co ..., accessed July 27, 2025,
https://computationalcreativity.net/iccc24/papers/ICCC24_paper_58.pdf
85. Maturana's Autopoiesis in AI: Self-Creation Through Recursive Organization - Reddit, accessed July 27, 2025,
https://www.reddit.com/r/ArtificialSentience/comments/1l5qhcs/maturanas_autopoiesis_in_ai_selfcreation_th
rough/
86. Emergent Behavior - AI Ethics Lab, accessed July 27, 2025, https://aiethicslab.rutgers.edu/e-floating-
buttons/emergent-behavior/----------- Page18 ------------
87. SHA-256 Algorithm - N-able, accessed July 27, 2025, https://www.n-able.com/it/blog/sha-256-encryption
88. Accelerating expansion of the universe - Wikipedia, accessed July 26, 2025,
https://en.wikipedia.org/wiki/Accelerating_expansion_of_the_universe
89. AUTONOMY AND AUTOPOIESIS - Francisco J. Varela, accessed July 27, 2025,
https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-
%20Autonomy%20and%20Autopoiesis.pdf
90. Cryptographic hash function - Wikipedia, accessed July 27, 2025,
https://en.wikipedia.org/wiki/Cryptographic_hash_function
