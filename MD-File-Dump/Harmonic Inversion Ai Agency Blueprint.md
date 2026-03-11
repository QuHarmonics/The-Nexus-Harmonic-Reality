# **The Autopoietic Nonce: A Generative Model for Cryptographic Search Based on Harmonic Resonance**

### **Abstract**

This report introduces the Generative Nonce Model (GNM), a novel framework for nonce determination in proof-of-work systems that challenges the prevailing assumption of computational irreducibility in cryptographic hash functions. By synthesizing principles from autopoietic systems theory and a harmonic model of computation, the GNM reframes the search for a valid nonce not as a brute-force traversal of a chaotic space, but as a guided, generative process. We model the SHA-256 compression function as an operationally closed, autocatalytic network. The GNM employs a recursive, generative algorithm, guided by heuristics derived from the \'Resonance Chord\' principle, to construct a valid computational trace that culminates in a nonce satisfying a given difficulty target. A valid nonce is thus not found, but *emerges* as the stable state of this self-organizing process. We propose a practical implementation pathway using a custom-heuristic Conflict-Driven Clause Learning (CDCL) SAT solver and outline an experimental protocol for validation on round-reduced SHA-256. The GNM represents a potential paradigm shift in cryptanalysis and offers a concrete application of artificial life principles to fundamental problems in computer science.

## **Introduction: Beyond Computational Irreducibility**

### **The Intractability of Nonce Determination**

The security of many decentralized systems, most notably the Bitcoin network, relies on a computational puzzle known as proof-of-work.^1^ Miners compete to find a \"nonce\" (number used once), a 32-bit value that, when combined with other data in a block header and hashed using the SHA-256 algorithm, produces a digest that is numerically smaller than a network-defined difficulty target.^1^ The fundamental security assumption underpinning this process is the pre-image resistance of the cryptographic hash function. This property ensures that it is computationally infeasible to find an input that produces a given output.^5^

This infeasibility is a direct consequence of the design philosophy of hash functions like SHA-256, which are constructed to exhibit an \"avalanche effect\": a minuscule change in the input results in a drastically different, unpredictable output.^8^ The iterative application of non-linear mixing functions over 64 rounds is intended to create a process that is, for all practical purposes, computationally irreversible.^10^ The effort required for a brute-force search is on the order of

2256 operations, a task far beyond the capacity of current and foreseeable classical computing technology.^13^

This practical intractability is an exemplar of a more profound concept articulated by Stephen Wolfram: **Computational Irreducibility**. This principle posits that for certain complex computational systems, no shortcut exists to determine their final state; the only way to know the outcome is to execute every step of the computation sequentially.^15^ The design of SHA-256, with its intricate cascade of bitwise operations, is a deliberate attempt to engineer such an irreducible process, thereby securing the proof-of-work mechanism against predictive attacks.^17^

### **The \'Resonance Chord\' Hypothesis**

This report challenges the absolute application of computational irreducibility to cryptographic hashing. We introduce the \'Resonance Chord\' hypothesis, which posits that while the output of SHA-256 may be statistically indistinguishable from random ^19^, the internal dynamics of the compression function are not devoid of structure. The hypothesis suggests that the high-dimensional state space of the algorithm contains preferential pathways or \"harmonics\"---trajectories that exhibit a form of structural coherence or algebraic simplicity relative to the vast majority of chaotic, unpredictable paths.

This perspective is inspired by field-theoretic models of computation, which treat computation not as a discrete manipulation of symbols but as the evolution of a continuous field. A particularly relevant framework is the \"Möbius Collapse Logic\" (MCL), which models computation as a \"living resonance field\" where solutions correspond to stable attractors or fixed points within the field\'s dynamics.^21^ The \'Resonance Chord\' hypothesis adapts this idea to the discrete domain of SHA-256, proposing that a valid hash is the endpoint of a trajectory that follows these underlying resonances.

### **An Autopoietic Approach to Cryptanalysis**

Building on this hypothesis, we propose a fundamentally new approach to the nonce determination problem: modeling the search as an **autopoietic**, or self-producing, process. This reframes the challenge from a search *for* a pre-existing solution in a vast space to the guided *generation* of a solution. The core idea is to treat the 64 rounds of the SHA-256 compression function as a dynamical system that can be guided to self-organize into a state satisfying the difficulty target. The valid nonce is not found but rather *emerges* as an integral component of this final, stable state.

This methodology draws heavily from the fields of **Artificial Life** and **autopoiesis**, which study how complex, stable organization can arise from the local interactions of simple components. The principles of autopoiesis, first articulated by Maturana and Varela to describe living cells, provide a formal language for systems that continuously produce and maintain their own organization.^22^

This report details the architecture of the **Generative Nonce Model (GNM)**, a predictive and generative framework designed to implement this autopoietic search. By treating the hash function\'s internal dynamics as an autonomous system, the GNM attempts to bypass computational irreducibility by operating on a higher level of abstraction---the level of the system\'s emergent organization, rather than the level of its individual bitwise operations. This represents a potential paradigm shift, moving cryptanalysis from a process of breaking a system\'s components to one of steering the system\'s behavior as a whole.

## **The Theoretical Framework: Computation as an Autopoietic Field**

### **Autopoiesis and Operational Closure in Computational Systems**

The theory of autopoiesis, developed by biologists Humberto Maturana and Francisco Varela, provides a formal characterization of living systems.^22^ An autopoietic system is defined as a network of processes of production that generates the very components that constitute the network, thereby realizing itself as a distinct, autonomous unity. This theory introduces several key distinctions critical for our model:

- **Organization vs. Structure:** Organization refers to the abstract configuration of relations between processes that defines a system\'s identity. Structure refers to the actual components and relations that physically realize that organization in a specific instance.^22^ An autopoietic system maintains its organization while its structure is in constant flux.

- **Operational Closure:** The network of processes is self-contained and recursive. The system\'s dynamics are determined by its own organization, not by external instruction. It does not have inputs or outputs in the traditional sense; rather, it has perturbations.

- **Structural Coupling:** An autopoietic system exists in an environment with which it interacts. Through a history of recurrent interactions, the system\'s structure changes in a way that is congruent with the environment, a process known as structural coupling. The environment triggers structural changes but does not specify or direct them.^26^

We can formally model the SHA-256 compression function as an operationally closed computational system. The security of the Merkle-Damgård construction, upon which SHA-256 is built, relies on this iterative, self-contained structure to ensure that the entire message history is thoroughly mixed into the final state, producing the avalanche effect.^30^ This design feature, intended for security, is formally analogous to the biological principle of operational closure. This analogy allows us to apply conceptual tools developed for self-producing systems to the domain of cryptanalysis.

In this model:

- **Components:** The 256-bit internal state, represented by the eight 32-bit working variables (a,b,c,d,e,f,g,h).

- **Processes:** The 64 rounds of computation, each defined by the functions Ch, Maj, Σ0​, Σ1​, and addition modulo 232.^32^

- **Organization:** The fixed algorithm of the 64-round state update transformation.

- **Structure:** The specific sequence of 256-bit state values for a given input message block.

- **Operational Closure:** The state at round t+1 is produced exclusively by the processes operating on the components (the state) at round t and a given message word Wt​. The network of processes (the 64 rounds) continuously regenerates the components (the state variables), thereby maintaining the system\'s organization throughout the computation.

### **Adapting the RAF Framework for Nonce Generation**

To formalize the concept of self-production within this computational system, we adapt the **Reflexively Autocatalytic and Food-generated (RAF) framework**.^34^ The RAF framework provides a precise mathematical definition for autocatalytic sets, which are networks of reactions that are collectively self-sustaining from a given set of initial resources, or a \"food set\". A set of reactions

R is a RAF if: 1) every reaction in R is catalyzed by at least one molecule produced by R, and 2) all reactants required by R can be produced from an initial food set F using only the reactions in R.

We map the nonce generation problem onto the RAF framework as follows:

- **Molecule Types (X):** The set of all possible 32-bit words that can exist as values for the internal state variables (a through h) and the message schedule words (Wt​).

- **Food Set (F):** The initial resources for the computation. This set includes the fixed Initial Value (IV) specified in the SHA-256 standard, the known parts of the block header (previous block hash, timestamp, etc.), and the difficulty target, which acts as a constraint on the final state of the system.^33^ The variable nonce is the part of the \"food\" we aim to generate.

- **Reactions (R):** The state update transformations for each of the 64 rounds. A \"reaction\" rt​ consumes the state at round t−1 and the message word Wt​ as reactants to produce the new state at round t.

- **Catalysis (C):** This is the central innovation of our model. Catalysis is not a static property of certain \"molecules\" but a dynamic, guiding influence. A state transition (a \"reaction\") is considered \"catalyzed\" if it aligns with the system\'s predicted resonant pathways. The predictive heuristic of the GNM, guided by the Harmonic Fitness Function, *is the catalytic process*. It selectively accelerates desirable reactions (pathways) that are more likely to lead to a self-sustaining and valid final state.

### **The Harmonic Framework: Resonance and Computational Geometry**

The \'Resonance Chord\' principle is formalized through a **Harmonic Fitness Function**, Φ(statet​,Wt​), which quantifies the \"resonance\" or structural stability of a potential state transition. This concept draws inspiration from frameworks like Möbius Collapse Logic (MCL), which describe computation as a dynamical process of collapse in a resonance field, where solutions are attractors.^21^ While SHA-256 is a discrete system, we hypothesize that its state space is not uniform but possesses a \"computational geometry\" with valleys and ridges, corresponding to more or less stable trajectories.

The fitness function Φ is derived from an analysis of the algebraic and differential properties of the SHA-256 round functions. For instance, the non-linear Boolean functions Ch and Maj have well-understood differential properties.^37^ The

Maj function, defined as Maj(x,y,z)=(x∧y)⊕(x∧z)⊕(y∧z), behaves linearly with respect to XOR differences when all input differences are equal (i.e., if Δx=Δy=Δz, then ΔMaj=Δx).^38^ Such linear propagation paths represent a form of structural stability---a \"harmonic\" or low-energy trajectory through the computational space. The function

Φ would assign a higher score to state transitions that exhibit such predictable, low-complexity behavior.

The goal of the GNM is to find a complete 64-round trajectory where each step is \"catalyzed\" by a high fitness score. This reframes cryptanalysis as a problem in control theory for complex systems. The GNM acts as a control algorithm, applying small, targeted \"perturbations\" (i.e., selecting specific values for unconstrained bits in the message schedule) at each step to steer the chaotic dynamics of the hash function along a desired, stable path---one that culminates in a valid hash. This approach is analogous to the Ott-Grebogi-Yorke (OGY) method for controlling chaos, which stabilizes unstable periodic orbits in a dynamical system through minimal interventions.^40^

## **The Generative Nonce Model (GNM): Architecture and Dynamics**

### **A Recursive Architecture for State Generation**

The GNM is architected as a recursive function, a structure that mirrors the self-referential nature of autopoietic systems. Instead of iteratively simulating the forward computation of the hash function, the GNM recursively *constructs* a valid computational trace from the final state backward, or from an initial state forward in a guided manner. The function, GenerateTrace(current_state, round_number), is defined by a base case and a recursive step, a common pattern for solving problems that can be decomposed into smaller, self-similar subproblems.^43^

- **Base Case:** The recursion terminates when round_number reaches its limit (e.g., 64 for a forward construction). At this point, the current_state is evaluated against the problem\'s terminal constraint---the network difficulty target. If the state satisfies the target, the function returns the successfully constructed trace, which contains the complete message schedule (W0​\...W63​) from which the nonce can be extracted. If the state does not satisfy the target, the function returns a failure signal, triggering backtracking in the call stack.^47^

- **Recursive Step:** For any round t \< 64, the function executes the core generative process. It utilizes the Harmonic Heuristic (detailed below) to generate a pruned set of candidate next states and their corresponding message schedule words, {(statet+1​,Wt​)}. For each promising candidate in this set, it makes a recursive call: GenerateTrace(state\_{t+1}, round_number + 1). This process is analogous to a depth-first search of a computation tree, but one that is aggressively pruned at each level to only explore harmonically resonant pathways.^50^ The recursive structure itself is a direct computational implementation of autopoietic self-production: each function call is an act of the system regenerating its own computational structure (the trace) one step further towards a complete and stable form.

### **The Harmonic Heuristic as a Path Selection Strategy**

The efficacy of the GNM hinges on its ability to navigate the astronomically large state space of SHA-256. A naive recursive search would be equivalent to a brute-force attack and suffer from the same exponential path explosion problem that plagues unguided symbolic execution of complex programs.^52^ The GNM\'s Harmonic Heuristic serves as a powerful path selection strategy to mitigate this explosion.

This approach is analogous to the use of learning-based and domain-specific heuristics in modern SAT solvers and symbolic execution engines.^52^ In these systems, rather than exploring paths or assigning variables randomly, a guiding function predicts which branches are most likely to lead to a solution or a contradiction, thereby pruning the search space.^58^

The Harmonic Fitness Function Φ, introduced in the previous section, acts as this guide. At each recursive step, potential next states are scored based on their adherence to principles of algebraic simplicity and predictable differential propagation. The GNM prioritizes the exploration of states with the highest fitness scores, effectively steering the generative process away from chaotic, \"dissonant\" regions of the state space and towards coherent, \"harmonic\" trajectories. This heuristic-guided generation transforms an intractable search problem into a manageable generative one.

### **Emergence of the Nonce as a Stable System State**

Within the GNM framework, a valid nonce is not the direct object of the search; rather, it is an emergent property of a successfully generated, self-consistent computational trace. This perspective aligns with theories of emergence in complex systems, where global order arises from local interactions without a central controller.

This process finds a powerful analogue in cellular automata like John Conway\'s Game of Life. In the Game of Life, complex, persistent structures such as \"still lifes,\" \"oscillators,\" and \"gliders\" emerge from a few simple, local rules applied in parallel across a grid. These emergent patterns can be seen as autopoietic entities that maintain their organization within their computational environment.^62^

Similarly, the GNM facilitates the emergence of a stable, globally consistent structure---a complete 64-round computational trace that satisfies all constraints from the initial IV to the final difficulty target. This complete trace is an \"autopoietic entity\" within the computational universe of SHA-256. The nonce is simply one of the components of this emergent structure, discovered not by exhaustive search but as a necessary element of the system\'s self-organized stability. This suggests a new class of generative algorithms modeled on developmental processes, which \"grow\" a solution according to intrinsic rules and environmental constraints, much like an organism\'s phenotype unfolds from its genotype according to the laws of physics and chemistry.^65^

## **Implementation and Validation Pathways**

### **A Hybrid SAT+CAS Strategy**

A practical implementation of the Generative Nonce Model can be achieved by framing the nonce-finding problem as a Boolean Satisfiability (SAT) problem.^66^ This involves translating the entire SHA-256 compression function for a given number of rounds into a single, large Conjunctive Normal Form (CNF) formula. Each bitwise operation (AND, XOR, NOT) and each bit of the modular additions is converted into a set of logical clauses that constrain the relationships between input, output, and intermediate variables.^71^

The core of the GNM---the Harmonic Heuristic---can be integrated directly into a modern Conflict-Driven Clause Learning (CDCL) SAT solver as a custom **branching heuristic**.^55^ Standard CDCL solvers employ heuristics like VSIDS (Variable State Independent Decaying Sum), which prioritize branching on variables that have recently been involved in conflicts.^56^ Our approach replaces this with a domain-specific heuristic. The solver would be programmed to prioritize assigning truth values to variables representing the internal state bits in a way that maximizes the Harmonic Fitness Function

Φ.

Calculating Φ may require reasoning about mathematical properties, such as modular arithmetic, that are cumbersome to express and solve at the purely Boolean level. To address this, we propose a hybrid **SAT+CAS** architecture. The SAT solver handles the primary search, while a Computer Algebra System (CAS) is called programmatically to analyze the current partial assignment and provide guidance. This hybrid approach has already proven successful in finding collisions in step-reduced SHA-256, significantly outperforming pure SAT-based methods by allowing the solver to leverage higher-level algebraic insights.^78^

### **Leveraging Massively Parallel Architectures**

The computational demands of solving a SAT instance representing even a moderately round-reduced SHA-256 are immense. The GNM\'s guided search, while more efficient than brute force, still requires vast computational resources. The proposed implementation is therefore targeted at high-performance computing (HPC) environments.

The recursive, tree-searching nature of the GNM is well-suited for massively parallel execution. Different branches of the search space can be explored concurrently on separate compute nodes, a classic application of distributed and parallel computing paradigms. An ideal platform for this research would be a system like the National Science Foundation\'s **Nexus supercomputer**, a \$20 million system at Georgia Tech designed specifically for large-scale, demanding AI research.^80^ Its architecture, combining high-performance computing with massive memory and storage, is tailored for tackling complex problems and giant datasets of the kind generated by our proposed SAT+CAS solver.^80^

### **Experimental Protocol and Validation Metrics**

To validate the GNM, a multi-stage experimental protocol is proposed:

1.  **Calibration on Reduced-Round SHA-256:** The initial experiments will target heavily reduced versions of the SHA-256 compression function (e.g., 16--24 rounds). Collisions and preimages for these versions have been found using existing techniques, providing a baseline for comparison.^78^ The primary goal in this phase is to calibrate the Harmonic Fitness Function\
    Φ and demonstrate a measurable performance improvement over standard CDCL solvers using generic heuristics like VSIDS.

2.  **Incremental Scaling and State-of-the-Art Comparison:** The number of rounds will be incrementally increased to 28, 31, and 38. The performance of the GNM-guided solver will be benchmarked against the best-known results in the literature, such as the differential cryptanalysis attacks pioneered by Mendel, Nad, and Schläffer, which represent the state of the art for these round counts.^79^

3.  **Validation Metrics:** The primary metric for success will be the time-to-solution or, more granularly, the number of decisions made by the SAT solver before finding a satisfying assignment. A successful outcome would be a performance improvement that scales super-linearly better than baseline solvers as the number of rounds increases. This would provide strong evidence that the harmonic heuristic is not merely making lucky guesses but is effectively pruning the exponential search space in a structurally informed way.

To clarify the novelty of the proposed approach, the following table compares it with existing nonce determination strategies.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Approach                                                                     Underlying Principle           Search Strategy                         Complexity Scaling (Hypothesized)   Key Challenge
  ---------------------------------------------------------------------------- ------------------------------ --------------------------------------- ----------------------------------- -----------------------------------------------------
  **Brute-Force Search**                                                       Exhaustive Search              Sequential or Random Guessing           O(2n)                               Immense search space

  **Standard SAT Attack**                                                      Constraint Propagation         Generic Heuristics (e.g., VSIDS/CDCL)   O(cn) for c\<2                      Path explosion, complex CNF encoding

  **GNM-Guided SAT Attack**                                                    Generative Self-Organization   Harmonic Branching Heuristic            Potentially Sub-exponential         Defining an effective Harmonic Fitness Function (Φ)

  **Table 4.1: A Comparative Framework for Nonce Determination Strategies.**                                                                                                              
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Conclusion: Implications for Cryptanalysis and Artificial Life**

### **A New Paradigm for Cryptanalysis?**

The Generative Nonce Model represents more than just a novel algorithm; it is a proof-of-concept for a new paradigm in cryptanalysis rooted in the principles of complex systems and artificial life. If validated, this approach would demonstrate that even computational systems meticulously designed to be chaotic and irreducible can harbor emergent organizational principles. These principles, operating at a higher level of abstraction than the underlying bitwise logic, can potentially be exploited to render the system\'s behavior predictable and controllable.

This has profound implications for the future of cryptography. The security of future cryptographic primitives may need to be evaluated not only for resistance to traditional differential, linear, and algebraic attacks but also for resilience against \"holistic\" attacks that target the system\'s emergent organizational dynamics. A successful GNM would initiate a co-evolutionary arms race: advances in AI for detecting emergent order would necessitate the design of cryptographic functions that are more robustly chaotic, which in turn would drive the development of more sophisticated AI-based cryptanalysis.

### **Computational Autopoiesis Beyond Biology**

The GNM serves as a concrete and non-trivial application of computational autopoiesis to a domain far removed from its biological origins.^24^ It demonstrates that core concepts such as operational closure, structural coupling, and self-production are not mere metaphors but can be formalized as powerful analytical and engineering tools for purely computational systems. This work aims to advance the theoretical foundations of Artificial Life by showing that its principles can be applied to solve fundamental problems in computer science, bridging the gap between the simulation of life and the engineering of intelligent systems.^88^

### **Future Directions and Open Questions**

This research opens several avenues for future inquiry. The Harmonic Heuristic, initially designed based on known cryptanalytic properties, could be evolved or learned. Machine learning techniques, such as reinforcement learning or graph neural networks, could be employed to automatically discover the \"resonant\" properties of a given hash function, creating an adaptive cryptanalytic tool that learns to steer the system without prior human knowledge of its specific vulnerabilities.^52^

Furthermore, the autopoietic generative model may be generalizable to other computationally hard constraint satisfaction problems (CSPs).^92^ Fields such as protein folding, logistics optimization, and circuit design are characterized by vast search spaces governed by complex local rules. A generative approach that \"grows\" a valid solution according to a guiding heuristic landscape could prove more efficient than traditional search-based methods.

Ultimately, this work touches upon a deep philosophical question regarding the nature of computation itself. Is it a purely syntactic, rule-following process, or does the \"computational universe\" possess an intrinsic geometry and dynamics, as suggested by physical and field-theoretic models?. The success of a model based on \"harmonic resonance\" would lend significant weight to the latter view. It would suggest that the universe of simple programs described by Wolfram is not just a static landscape of discrete rules but a dynamic field governed by its own physical-like laws---a world where chaos and order are not mutually exclusive but are two facets of a deeper, generative reality.

#### Works cited

1.  What Is a Bitcoin Nonce and How Does It Work - Lightspark, accessed July 27, 2025, [[https://www.lightspark.com/glossary/nonce]{.underline}](https://www.lightspark.com/glossary/nonce)

2.  Nonce: What It Means and How It\'s Used in Blockchain - Investopedia, accessed July 27, 2025, [[https://www.investopedia.com/terms/n/nonce.asp]{.underline}](https://www.investopedia.com/terms/n/nonce.asp)

3.  What Is a Nonce in Blockchain: Definition and Purpose - Tatum.io, accessed July 27, 2025, [[https://tatum.io/blog/what-is-a-nonce-in-blockchain]{.underline}](https://tatum.io/blog/what-is-a-nonce-in-blockchain)

4.  What Is a Nonce? A No-Nonsense Dive into Proof of Work - CoinCentral, accessed July 27, 2025, [[https://coincentral.com/what-is-a-nonce-proof-of-work/]{.underline}](https://coincentral.com/what-is-a-nonce-proof-of-work/)

5.  Cryptographic Hash Functions: A Historical Overview - Freeman Law, accessed July 27, 2025, [[https://freemanlaw.com/cryptographic-hash-functions/]{.underline}](https://freemanlaw.com/cryptographic-hash-functions/)

6.  Hash Function - Definitions, Example, How it Works - Corporate Finance Institute, accessed July 27, 2025, [[https://corporatefinanceinstitute.com/resources/cryptocurrency/hash-function/]{.underline}](https://corporatefinanceinstitute.com/resources/cryptocurrency/hash-function/)

7.  Cryptographic Hash Functions -- Networks at ITP, accessed July 27, 2025, [[https://itp.nyu.edu/networks/explanations/cryptographic-hash-functions/]{.underline}](https://itp.nyu.edu/networks/explanations/cryptographic-hash-functions/)

8.  How Cryptographic Hash Functions Solve a Very Difficult and Important Problem, accessed July 27, 2025, [[https://bennettgarner.medium.com/how-cryptographic-hash-functions-solve-a-very-difficult-and-important-problem-b939da3b0185]{.underline}](https://bennettgarner.medium.com/how-cryptographic-hash-functions-solve-a-very-difficult-and-important-problem-b939da3b0185)

9.  Is SHA-256 secure? Legal & Compliance Experts Say Yes---Here\'s Why - Blog, accessed July 27, 2025, [[https://blog.pagefreezer.com/sha-256-benefits-evidence-authentication]{.underline}](https://blog.pagefreezer.com/sha-256-benefits-evidence-authentication)

10. Are cryptographic hash functions fundamentally irreversible? : r/askscience - Reddit, accessed July 27, 2025, [[https://www.reddit.com/r/askscience/comments/1w1jms/are_cryptographic_hash_functions_fundamentally/]{.underline}](https://www.reddit.com/r/askscience/comments/1w1jms/are_cryptographic_hash_functions_fundamentally/)

11. Which step in modern cryptographic hash functions (such as SHA-256) is the most computationally expensive to reverse? : r/computerscience - Reddit, accessed July 27, 2025, [[https://www.reddit.com/r/computerscience/comments/t1jz33/which_step_in_modern_cryptographic_hash_functions/]{.underline}](https://www.reddit.com/r/computerscience/comments/t1jz33/which_step_in_modern_cryptographic_hash_functions/)

12. Is hashing really a irreversible process? - Stack Overflow, accessed July 27, 2025, [[https://stackoverflow.com/questions/47017606/is-hashing-really-a-irreversible-process]{.underline}](https://stackoverflow.com/questions/47017606/is-hashing-really-a-irreversible-process)

13. Computational requirements for breaking SHA-256? - Cryptography Stack Exchange, accessed July 27, 2025, [[https://crypto.stackexchange.com/questions/52571/computational-requirements-for-breaking-sha-256]{.underline}](https://crypto.stackexchange.com/questions/52571/computational-requirements-for-breaking-sha-256)

14. Mastering SHA-256: The Ultimate Guide - Number Analytics, accessed July 27, 2025, [[https://www.numberanalytics.com/blog/mastering-sha-256-ultimate-guide]{.underline}](https://www.numberanalytics.com/blog/mastering-sha-256-ultimate-guide)

15. TechnicalExperts/writing/computational_irreducibility.md at main - GitHub, accessed July 27, 2025, [[https://github.com/Jason2Brownlee/TechnicalExperts/blob/main/writing/computational_irreducibility.md]{.underline}](https://github.com/Jason2Brownlee/TechnicalExperts/blob/main/writing/computational_irreducibility.md)

16. Computational irreducibility - Wikipedia, accessed July 27, 2025, [[https://en.wikipedia.org/wiki/Computational_irreducibility]{.underline}](https://en.wikipedia.org/wiki/Computational_irreducibility)

17. SHA-256 Algorithm: Characteristics, Steps, and Applications - Simplilearn.com, accessed July 27, 2025, [[https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm]{.underline}](https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm)

18. Note (d) for Human Thinking: A New Kind of Science \| Online by Stephen Wolfram \[Page 1100\], accessed July 27, 2025, [[https://www.wolframscience.com/nks/notes-10-12\--hashing/]{.underline}](https://www.wolframscience.com/nks/notes-10-12--hashing/)

19. Are the SHA family hash outputs practically random? - Cryptography Stack Exchange, accessed July 27, 2025, [[https://crypto.stackexchange.com/questions/12822/are-the-sha-family-hash-outputs-practically-random]{.underline}](https://crypto.stackexchange.com/questions/12822/are-the-sha-family-hash-outputs-practically-random)

20. Is there any bias whatsoever in modern hash function outputs?, accessed July 27, 2025, [[https://crypto.stackexchange.com/questions/67385/is-there-any-bias-whatsoever-in-modern-hash-function-outputs]{.underline}](https://crypto.stackexchange.com/questions/67385/is-there-any-bias-whatsoever-in-modern-hash-function-outputs)

21. Everything, Everywhere, All at Once - The Fundamental Computational Structure of The Universe - Figshare, accessed July 27, 2025, [[https://figshare.com/articles/thesis/Everything_Everywhere_All_at_Once\_-\_The_Fundamental_Computational_Structure_of_The_Universe/28881194]{.underline}](https://figshare.com/articles/thesis/Everything_Everywhere_All_at_Once_-_The_Fundamental_Computational_Structure_of_The_Universe/28881194)

22. Computing with Autopoietic Systems - Biology of Cognition Lab, accessed July 27, 2025, [[https://biologyofcognition.wordpress.com/wp-content/uploads/2008/06/autopoieticcomputing8.pdf]{.underline}](https://biologyofcognition.wordpress.com/wp-content/uploads/2008/06/autopoieticcomputing8.pdf)

23. (PDF) Computing with Autopoietic Systems - ResearchGate, accessed July 27, 2025, [[https://www.researchgate.net/publication/254842986_Computing_with_Autopoietic_Systems]{.underline}](https://www.researchgate.net/publication/254842986_Computing_with_Autopoietic_Systems)

24. (PDF) Thirty Years of Computational Autopoiesis: A Review, accessed July 27, 2025, [[https://www.researchgate.net/publication/8462896_Thirty_Years_of_Computational_Autopoiesis_A_Review]{.underline}](https://www.researchgate.net/publication/8462896_Thirty_Years_of_Computational_Autopoiesis_A_Review)

25. Rediscovering Computational Autopoiesis \| Santa Fe Institute, accessed July 27, 2025, [[https://www.santafe.edu/research/results/working-papers/rediscovering-computational-autopoiesis]{.underline}](https://www.santafe.edu/research/results/working-papers/rediscovering-computational-autopoiesis)

26. The cognitive theories of Maturana and Varela - CEPA.INFO, accessed July 27, 2025, [[https://cepa.info/fulltexts/2253.pdf]{.underline}](https://cepa.info/fulltexts/2253.pdf)

27. A Study of "Organizational Closure" and Autopoiesis: \| Harish\'s Notebook, accessed July 27, 2025, [[https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/]{.underline}](https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/)

28. Maturana\'s Autopoiesis in AI: Self-Creation Through Recursive Organization - Reddit, accessed July 27, 2025, [[https://www.reddit.com/r/ArtificialSentience/comments/1l5qhcs/maturanas_autopoiesis_in_ai_selfcreation_through/]{.underline}](https://www.reddit.com/r/ArtificialSentience/comments/1l5qhcs/maturanas_autopoiesis_in_ai_selfcreation_through/)

29. AUTONOMY AND AUTOPOIESIS - Francisco J. Varela, accessed July 27, 2025, [[https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-%20Autonomy%20and%20Autopoiesis.pdf]{.underline}](https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-%20Autonomy%20and%20Autopoiesis.pdf)

30. Merkle--Damgård construction - Wikipedia, accessed July 27, 2025, [[https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction]{.underline}](https://en.wikipedia.org/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction)

31. Merkle-Damgard Scheme in Cryptography - GeeksforGeeks, accessed July 27, 2025, [[https://www.geeksforgeeks.org/computer-networks/merkle-damgard-scheme-in-cryptography/]{.underline}](https://www.geeksforgeeks.org/computer-networks/merkle-damgard-scheme-in-cryptography/)

32. The cryptographic hash function SHA-256, accessed July 27, 2025, [[https://helix.stormhub.org/papers/SHA-256.pdf]{.underline}](https://helix.stormhub.org/papers/SHA-256.pdf)

33. fips pub 180-4 - federal information processing standards publication, accessed July 27, 2025, [[https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf]{.underline}](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.180-4.pdf)

34. www.templeton.org, accessed July 27, 2025, [[https://www.templeton.org/wp-content/uploads/2022/03/Complexity_Hordjik_Formatted.pdf]{.underline}](https://www.templeton.org/wp-content/uploads/2022/03/Complexity_Hordjik_Formatted.pdf)

35. Autocatalytic networks in biology: structural theory and algorithms - PMC - PubMed Central, accessed July 27, 2025, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC6408349/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC6408349/)

36. Self-generating autocatalytic networks: structural results, algorithms, and their relevance to evolutionary processes - ResearchGate, accessed July 27, 2025, [[https://www.researchgate.net/publication/373680463_Self-generating_autocatalytic_networks_structural_results_algorithms_and_their_relevance_to_evolutionary_processes]{.underline}](https://www.researchgate.net/publication/373680463_Self-generating_autocatalytic_networks_structural_results_algorithms_and_their_relevance_to_evolutionary_processes)

37. Linear and Differential Cryptanalysis of SHA-256 - CORE, accessed July 27, 2025, [[https://core.ac.uk/download/12549084.pdf]{.underline}](https://core.ac.uk/download/12549084.pdf)

38. Analysis of a SHA-256 variant - SciSpace, accessed July 27, 2025, [[https://scispace.com/pdf/analysis-of-a-sha-256-variant-1yv7w37ply.pdf]{.underline}](https://scispace.com/pdf/analysis-of-a-sha-256-variant-1yv7w37ply.pdf)

39. Differential Analysis of a Cryptographic Hashing Algorithm HBC-256 - MDPI, accessed July 27, 2025, [[https://www.mdpi.com/2076-3417/12/19/10173]{.underline}](https://www.mdpi.com/2076-3417/12/19/10173)

40. Control of chaos - Wikipedia, accessed July 27, 2025, [[https://en.wikipedia.org/wiki/Control_of_chaos]{.underline}](https://en.wikipedia.org/wiki/Control_of_chaos)

41. Control of Chaotic Dynamical Systems using OGY - IS MUNI, accessed July 27, 2025, [[https://is.muni.cz/el/1431/jaro2016/M6201/um/OGY.pdf]{.underline}](https://is.muni.cz/el/1431/jaro2016/M6201/um/OGY.pdf)

42. Mastering Chaos Control in Dynamical Systems - Number Analytics, accessed July 27, 2025, [[https://www.numberanalytics.com/blog/chaos-control-dynamical-systems-ultimate-guide]{.underline}](https://www.numberanalytics.com/blog/chaos-control-dynamical-systems-ultimate-guide)

43. Recursive Functions - GeeksforGeeks, accessed July 26, 2025, [[https://www.geeksforgeeks.org/dsa/recursive-functions/]{.underline}](https://www.geeksforgeeks.org/dsa/recursive-functions/)

44. Recursion: a step-by-step introduction \| by Isaac Wong \| Medium, accessed July 26, 2025, [[https://medium.com/@isaac_70614/recursion-a-step-by-step-introduction-ed25c957559c]{.underline}](https://medium.com/@isaac_70614/recursion-a-step-by-step-introduction-ed25c957559c)

45. Difference Between Recursion and Iteration - Interview Kickstart, accessed July 26, 2025, [[https://interviewkickstart.com/blogs/learn/difference-between-recursion-and-iteration]{.underline}](https://interviewkickstart.com/blogs/learn/difference-between-recursion-and-iteration)

46. Introduction to Recursion - GeeksforGeeks, accessed July 26, 2025, [[https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/]{.underline}](https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/)

47. What is \'Base Case\' in Recursion? - GeeksforGeeks, accessed July 26, 2025, [[https://www.geeksforgeeks.org/dsa/what-is-base-case-in-recursion/]{.underline}](https://www.geeksforgeeks.org/dsa/what-is-base-case-in-recursion/)

48. Base Condition in Recursion - CodeChef, accessed July 26, 2025, [[https://www.codechef.com/learn/course/recursion/LRECUR01/problems/RECUR14]{.underline}](https://www.codechef.com/learn/course/recursion/LRECUR01/problems/RECUR14)

49. Reading 14: Recursion - MIT, accessed July 26, 2025, [[https://web.mit.edu/6.005/www/fa16/classes/14-recursion/]{.underline}](https://web.mit.edu/6.005/www/fa16/classes/14-recursion/)

50. Recursion in Python: Concepts, Examples, and Tips \| DataCamp, accessed July 26, 2025, [[https://www.datacamp.com/tutorial/recursion-in-python]{.underline}](https://www.datacamp.com/tutorial/recursion-in-python)

51. Recursion in Python: An Introduction, accessed July 26, 2025, [[https://realpython.com/python-recursion/]{.underline}](https://realpython.com/python-recursion/)

52. Learning to Explore Paths for Symbolic Execution, accessed July 27, 2025, [[https://files.sri.inf.ethz.ch/website/papers/ccs21-learch.pdf]{.underline}](https://files.sri.inf.ethz.ch/website/papers/ccs21-learch.pdf)

53. Scaling Symbolic Execution to Large Software Systems - arXiv, accessed July 27, 2025, [[https://arxiv.org/html/2408.01909v1]{.underline}](https://arxiv.org/html/2408.01909v1)

54. Symbolic Execution and Applications - GitHub Pages, accessed July 27, 2025, [[https://linqlover.github.io/symbolic-execution-survey/report.pdf]{.underline}](https://linqlover.github.io/symbolic-execution-survey/report.pdf)

55. Learning Rate Based Branching Heuristic for SAT Solvers \| Request PDF - ResearchGate, accessed July 27, 2025, [[https://www.researchgate.net/publication/303901008_Learning_Rate_Based_Branching_Heuristic_for_SAT_Solvers]{.underline}](https://www.researchgate.net/publication/303901008_Learning_Rate_Based_Branching_Heuristic_for_SAT_Solvers)

56. Boosting the Performance of CDCL-Based SAT Solvers by Exploiting Backbones and Backdoors - MDPI, accessed July 27, 2025, [[https://www.mdpi.com/1999-4893/15/9/302]{.underline}](https://www.mdpi.com/1999-4893/15/9/302)

57. NEURAL HEURISTICS FOR SAT SOLVING - Representation Learning on Graphs and Manifolds, accessed July 27, 2025, [[https://rlgm.github.io/papers/32.pdf]{.underline}](https://rlgm.github.io/papers/32.pdf)

58. CrystalBall: How to create your custom SAT solver, accessed July 27, 2025, [[http://www.cs.toronto.edu/\~arijit/crystalball_poster.pdf]{.underline}](http://www.cs.toronto.edu/~arijit/crystalball_poster.pdf)

59. arXiv:2402.10705v3 \[cs.AI\] 13 Nov 2024, accessed July 27, 2025, [[https://arxiv.org/pdf/2402.10705]{.underline}](https://arxiv.org/pdf/2402.10705)

60. SAT Solver - hliejun/projects, accessed July 27, 2025, [[https://hliejun.github.io/projects/satsolver/]{.underline}](https://hliejun.github.io/projects/satsolver/)

61. Theoretical explanations for practical success of SAT solvers?, accessed July 27, 2025, [[https://cstheory.stackexchange.com/questions/37886/theoretical-explanations-for-practical-success-of-sat-solvers]{.underline}](https://cstheory.stackexchange.com/questions/37886/theoretical-explanations-for-practical-success-of-sat-solvers)

62. Autopoiesis and cognition in the game of life - PubMed, accessed July 27, 2025, [[https://pubmed.ncbi.nlm.nih.gov/15245630/]{.underline}](https://pubmed.ncbi.nlm.nih.gov/15245630/)

63. \[2407.21086\] Non-Platonic Autopoiesis of a Cellular Automaton Glider in Asymptotic Lenia, accessed July 27, 2025, [[https://arxiv.org/abs/2407.21086]{.underline}](https://arxiv.org/abs/2407.21086)

64. Autopoiesis and Cognition in the Game of Life - CiteSeerX, accessed July 27, 2025, [[https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=b9a502e5b6de14087b7e9ba627f4ea6d4fc8ed2c]{.underline}](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=b9a502e5b6de14087b7e9ba627f4ea6d4fc8ed2c)

65. Bioattractors: dynamical systems theory and the evolution of regulatory processes - PMC, accessed July 27, 2025, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC4048087/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC4048087/)

66. SHA-256 Collision Attack with Programmatic SAT - CEUR-WS.org, accessed July 27, 2025, [[https://ceur-ws.org/Vol-3717/paper5.pdf]{.underline}](https://ceur-ws.org/Vol-3717/paper5.pdf)

67. \[2406.20072\] SHA-256 Collision Attack with Programmatic SAT - arXiv, accessed July 27, 2025, [[https://arxiv.org/abs/2406.20072]{.underline}](https://arxiv.org/abs/2406.20072)

68. Converting SHA256 into a SAT instance / Boolean expression using Lisp - Stack Overflow, accessed July 27, 2025, [[https://stackoverflow.com/questions/75568026/converting-sha256-into-a-sat-instance-boolean-expression-using-lisp]{.underline}](https://stackoverflow.com/questions/75568026/converting-sha256-into-a-sat-instance-boolean-expression-using-lisp)

69. SAT solving SHA256 is a dead end - I was researching this for the purpose of Bit\... \| Hacker News, accessed July 27, 2025, [[https://news.ycombinator.com/item?id=8403082]{.underline}](https://news.ycombinator.com/item?id=8403082)

70. Would P=NP being true mean sha256 or any other polynomial calculatable hash function is broken? : r/cryptography - Reddit, accessed July 27, 2025, [[https://www.reddit.com/r/cryptography/comments/38lxyj/would_pnp_being_true_mean_sha256_or_any_other/]{.underline}](https://www.reddit.com/r/cryptography/comments/38lxyj/would_pnp_being_true_mean_sha256_or_any_other/)

71. (PDF) Algebraic Fault Attack on the SHA-256 Compression Function, accessed July 27, 2025, [[https://www.researchgate.net/publication/307694142_Algebraic_Fault_Attack_on_the_SHA-256_Compression_Function]{.underline}](https://www.researchgate.net/publication/307694142_Algebraic_Fault_Attack_on_the_SHA-256_Compression_Function)

72. Extending SAT Solvers to Cryptographic Problems, accessed July 27, 2025, [[https://www.msoos.org/wordpress/wp-content/uploads/2011/03/Extending_SAT_2009.pdf]{.underline}](https://www.msoos.org/wordpress/wp-content/uploads/2011/03/Extending_SAT_2009.pdf)

73. Converting (math) problems to SAT instances - Computer Science Stack Exchange, accessed July 27, 2025, [[https://cs.stackexchange.com/questions/12087/converting-math-problems-to-sat-instances]{.underline}](https://cs.stackexchange.com/questions/12087/converting-math-problems-to-sat-instances)

74. G2SAT: Learning to Generate SAT Formulas - PMC - PubMed Central, accessed July 27, 2025, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC7138247/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC7138247/)

75. SAT Encoding: An Introduction - Venkatesh-Prasad Ranganath - Medium, accessed July 27, 2025, [[https://rvprasad.medium.com/sat-encoding-an-introduction-44d23049ab2a]{.underline}](https://rvprasad.medium.com/sat-encoding-an-introduction-44d23049ab2a)

76. SAT-based preimage attacks on SHA-1, accessed July 27, 2025, [[https://yurichev.com/mirrors/SAT_SMT_crypto/thesis-output.pdf]{.underline}](https://yurichev.com/mirrors/SAT_SMT_crypto/thesis-output.pdf)

77. Modern SAT solvers: fast, neat and underused (part 3 of N) - The Coding Nest, accessed July 27, 2025, [[https://codingnest.com/modern-sat-solvers-fast-neat-and-underused-part-3-of-n/]{.underline}](https://codingnest.com/modern-sat-solvers-fast-neat-and-underused-part-3-of-n/)

78. SHA-256 Collision Attack with Programmatic SAT - arXiv, accessed July 27, 2025, [[https://arxiv.org/html/2406.20072v1]{.underline}](https://arxiv.org/html/2406.20072v1)

79. SHA-256 Collision Attack with Programmatic SAT, accessed July 27, 2025, [[https://cs.uwaterloo.ca/\~cbright/reports/sc2-hash.pdf]{.underline}](https://cs.uwaterloo.ca/~cbright/reports/sc2-hash.pdf)

80. Georgia Tech to Build \$20M National AI Supercomputer \| News Center, accessed July 26, 2025, [[https://news.gatech.edu/news/2025/07/15/georgia-tech-build-20m-national-ai-supercomputer]{.underline}](https://news.gatech.edu/news/2025/07/15/georgia-tech-build-20m-national-ai-supercomputer)

81. Finding SHA-2 Characteristics: Searching Through a Minefield of Contradictions - COSIC, accessed July 27, 2025, [[https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/2104]{.underline}](https://cosicdatabase.esat.kuleuven.be/backend/publications/files/conferencepaper/2104)

82. Improving Local Collisions: New Attacks on Reduced SHA-256, accessed July 27, 2025, [[https://graz.elsevierpure.com/en/publications/improving-local-collisions-new-attacks-on-reduced-sha-256]{.underline}](https://graz.elsevierpure.com/en/publications/improving-local-collisions-new-attacks-on-reduced-sha-256)

83. (PDF) Improving Local Collisions: New Attacks on Reduced SHA-256, accessed July 27, 2025, [[https://www.researchgate.net/publication/235257652_Improving_Local_Collisions_New_Attacks_on_Reduced_SHA-256]{.underline}](https://www.researchgate.net/publication/235257652_Improving_Local_Collisions_New_Attacks_on_Reduced_SHA-256)

84. (PDF) Practical Collisions for SHAMATA-256 - ResearchGate, accessed July 27, 2025, [[https://www.researchgate.net/publication/221274585_Practical_Collisions_for_SHAMATA-256]{.underline}](https://www.researchgate.net/publication/221274585_Practical_Collisions_for_SHAMATA-256)

85. Rediscovering Computational Autopoiesis - CiteSeerX, accessed July 27, 2025, [[https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=02080ab1602242fc9e9bbf4560b65bb9192b29f7]{.underline}](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=02080ab1602242fc9e9bbf4560b65bb9192b29f7)

86. (PDF) Rediscovering Computational Autopoiesis - ResearchGate, accessed July 27, 2025, [[https://www.researchgate.net/publication/2831744_Rediscovering_Computational_Autopoiesis]{.underline}](https://www.researchgate.net/publication/2831744_Rediscovering_Computational_Autopoiesis)

87. Computational Autopoiesis: The Original Algorithm \| Santa Fe Institute, accessed July 27, 2025, [[https://www.santafe.edu/research/results/working-papers/computational-autopoiesis-the-original-algorithm]{.underline}](https://www.santafe.edu/research/results/working-papers/computational-autopoiesis-the-original-algorithm)

88. Artificial life - Wikipedia, accessed July 27, 2025, [[https://en.wikipedia.org/wiki/Artificial_life]{.underline}](https://en.wikipedia.org/wiki/Artificial_life)

89. Artificial Life as Theoretical Biology: How to do real science with computer simulation - Geoffrey Miller, accessed July 27, 2025, [[https://geoffrey-miller-y5jr.squarespace.com/s/1995-real-science-simulation.pdf]{.underline}](https://geoffrey-miller-y5jr.squarespace.com/s/1995-real-science-simulation.pdf)

90. Computing the Origin of Life \| News - NASA Astrobiology, accessed July 27, 2025, [[https://astrobiology.nasa.gov/news/computing-the-origin-of-life/]{.underline}](https://astrobiology.nasa.gov/news/computing-the-origin-of-life/)

91. AI: Artificial Life - Biology, accessed July 27, 2025, [[https://biology.kenyon.edu/slonc/bio3/AI/A_LIFE/a_life.html]{.underline}](https://biology.kenyon.edu/slonc/bio3/AI/A_LIFE/a_life.html)

92. Constraint satisfaction problem - Wikipedia, accessed July 27, 2025, [[https://en.wikipedia.org/wiki/Constraint_satisfaction_problem]{.underline}](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

93. 5 CONSTRAINT SATISFACTION PROBLEMS - Artificial Intelligence: A Modern Approach, accessed July 27, 2025, [[http://aima.cs.berkeley.edu/newchap05.pdf]{.underline}](http://aima.cs.berkeley.edu/newchap05.pdf)

94. Constraint satisfaction problems (csp) \| PPTX - SlideShare, accessed July 27, 2025, [[https://www.slideshare.net/slideshow/constraint-satisfaction-problems-csp/251030176]{.underline}](https://www.slideshare.net/slideshow/constraint-satisfaction-problems-csp/251030176)
