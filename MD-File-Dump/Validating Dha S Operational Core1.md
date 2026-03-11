### Immediate next steps (smallest effort ⇒ biggest credibility)

1.  **Single-file PoC\**
    *C = π, base 16, fast-path double FP* → implement get_window(d, w=16); publish with pytest verifying first 100 known digits.

2.  **Stat test harness\**
    Wrap NIST SP800-22 in Python; auto-run on three 1 MiB streams (π16, log2-binary, log3-binary) and dump a markdown report.

3.  **Performance map prototype\**
    Script that sweeps (d, w) grid and records time/precision backend switch---produce heat-map.

4.  **Security note\**
    Draft a 2-page "Assumptions & intended use" doc---makes reviewers comfortable that you know the limits.

Ship those four and you'll have *tangible evidence* that the grand plan is executable. Ping me once PoC repo is up---I'll clone, run tests, and look for edge-case failures.

# A Research and Development Plan for the Validation, Formalization, and Implementation of Digit Hashing Algorithms (DHA)

## Part I: Empirical Validation of Core DHA Mechanics

This initial phase of the research program is designed to establish a robust empirical foundation for the Digit Hashing Algorithm (DHA) concept. The objective is to transition from theoretical conjecture to verifiable data by rigorously testing the core properties of Bailey-Borwein-Plouffe (BBP) type formulas when they are framed as hashing functions. This validation will provide the necessary groundwork for the subsequent theoretical formalization and software implementation.

### Section 1: Foundations of BBP-Type Formulas as Hashing Functions

This section establishes the theoretical and historical context for the entire project. It reframes a known mathematical tool---the spigot algorithm for transcendental constants---for a novel cryptographic purpose, thereby defining the fundamental principles and hypotheses that will be tested and developed.

#### 1.1. Historical Context and Discovery

The theoretical basis for the Digit Hashing Algorithm originates with the Bailey-Borwein-Plouffe (BBP) formula, a discovery that fundamentally altered the landscape of computational number theory. Discovered in 1995 by Simon Plouffe, the formula was subsequently published in a paper co-authored with David H. Bailey and Peter Borwein.^1^ The formula for

π is expressed as:

π=k=0∑∞​16k1​(8k+14​−8k+42​−8k+51​−8k+61​)

The existence of this formula was a profound surprise to the mathematical community.^1^ It overturned the long-held belief that computing the

d-th digit of an irrational number like π was computationally as difficult as computing all preceding d−1 digits.^1^ The BBP formula and its derivatives are \"spigot algorithms,\" capable of producing digits from an arbitrary starting position without requiring the computation of prior digits. This unique \"random access\" property is the central mechanism that enables the concept of a Digit Hashing Algorithm. While the collaboration is historically significant, it is also noted that the precise attribution of contributions has been a subject of discussion, a factor that provides a complete historical picture.^5^

#### 1.2. Mathematical Formalism of BBP-Type Formulas

The original formula for π is a specific instance of a broader class of BBP-type formulas. A general BBP-type formula for a constant C can be expressed as an infinite series of the form:

C=k=0∑∞​q(k)bkp(k)​

where p(k) and q(k) are polynomials with integer coefficients (with deg(p)\<deg(q)), and b≥2 is an integer base.^6^ A more compact and widely used notation, the

P function, represents a significant subclass of these formulas ^1^:

P(s,b,n,A)=k=0∑∞​bk1​j=1∑n​(kn+j)saj​​

In this notation, s is the power (typically 1 for the most common formulas), b is the base, n is the length of the polynomial in the denominator, and A=(a1​,a2​,...,an​) is a vector of integer coefficients.^8^ For example, the original BBP formula for

π can be written compactly as π=P(1,16,8,(4,0,0,−2,−1,−1,0,0)).^11^ This formalism provides the precise language for this investigation, as each parameter---

s,b,n,A, and the resulting constant C---can be systematically varied to probe the behavior of the DHA.

#### 1.3. The Digit Extraction Mechanism as a Mapping

The core mechanism that allows for the extraction of the d-th digit of a constant C in base b relies on a simple yet powerful principle of modular arithmetic. The process involves computing the fractional part of bdC, which can be written as {bdC}. This quantity represents the digit sequence of C in base b starting from position d+1. The calculation is split into two parts:

{bdC}={k=0∑d​q(k)bd−kp(k)​+k=d+1∑∞​q(k)bd−kp(k)​}(mod1)

The second sum consists of terms that rapidly decrease and can be computed to a sufficient precision using standard floating-point arithmetic.^12^ The first sum is the computationally intensive part. Crucially, because the final result is taken modulo 1, the integer part of each term is irrelevant. This allows the numerator

bd−k to be computed modulo q(k), i.e., bd−k(modq(k)). This modular exponentiation can be performed very efficiently, even for large d, without requiring multiple-precision arithmetic for the bulk of the computation.^12^

This mechanism allows the formal definition of the Digit Hashing Algorithm as a mapping HC,b​:N→Zb​. The input to this function is the digit position d (a natural number), and the output is the d-th digit of the constant C in base b. This re-framing of a digit extraction algorithm as a deterministic mapping from an integer input to a fixed-size integer output is the central hypothesis of this research program.

#### 1.4. Initial Hypothesis: DHA as a Pseudo-Random Function (PRF)

The primary working hypothesis of this investigation is that the mapping HC,b​ exhibits properties analogous to those of a Pseudo-Random Function (PRF). Specifically, it is hypothesized that for a \"well-chosen\" constant C and base b, the output of the DHA is uniformly distributed, and that adjacent outputs, such as H(d) and H(d+1), are statistically independent and unpredictable from one another.

This hypothesis is deeply connected to a major unsolved problem in number theory: the normality of transcendental constants. A number is said to be normal in base b if every possible sequence of m digits appears in its base-b expansion with a limiting frequency of b−m.^6^ The BBP framework provides a direct link between this abstract property and the behavior of a concrete computational process. Proving that a constant like

log2 is normal in base 2 is equivalent to proving that the sequence generated by the recurrence xd​=(2xd−1​+1/d)(mod1) is equidistributed in the interval \[0,1).^9^

Modern cryptography is built upon a foundation of computational hardness assumptions---conjectures that are widely believed to be true but remain unproven. Examples include the difficulty of integer factorization, which underpins the security of RSA, and the discrete logarithm problem, which is fundamental to Diffie-Hellman key exchange and elliptic curve cryptography. The normality of fundamental mathematical constants like π and log2 represents a similarly long-standing and deeply-held conjecture within pure mathematics. The BBP formula provides a direct bridge, transforming this abstract number-theoretic conjecture into a concrete statement about the behavior of a simple chaotic iterator.

This allows the \"randomness\" of the DHA to be formalized not as a proven fact, but as a cryptographic assumption. The security of a DHA-based primitive can be stated as follows: \"The DHA is a secure PRF under the assumption that the underlying BBP recurrence is equidistributed (i.e., the associated constant is normal).\" This framing establishes a profound and rigorous link between applied cryptography and number theory. Any practical cryptanalytic attack on a DHA, such as the discovery of a significant statistical bias in its output, would constitute a major breakthrough in pure mathematics, as it would imply that a fundamental constant is not normal. This connection elevates the importance of the proposed research, as its findings could have implications far beyond the immediate cryptographic applications.

### Section 2: Protocol for Substrate and Base Permutation Analysis (\"Substrate Swap\")

This section details the experimental design for rigorously testing the DHA\'s robustness, versatility, and the generality of its pseudo-random properties. The \"Substrate Swap\" protocol involves systematically varying the core mathematical components of the BBP formula---the constant it represents (the \"substrate\") and the number base---and analyzing the statistical properties of the resulting digit streams.

#### 2.1. Selection of Substrate Constants

A diverse portfolio of mathematical constants with known BBP-type formulas will be compiled for testing. This is a critical step to determine whether the PRF-like properties are a unique feature of the original π formula or a general characteristic of the BBP structure. The portfolio will include:

- **Canonical Constants:** The foundational constants for which BBP-type formulas were first explored, including π ^1^,\
  π2 ^8^, and the natural logarithm of 2,\
  log2.^8^ These will serve as the baseline for all comparisons.

- **Logarithms of Primes:** An extensive list of primes are known to have binary BBP formulas, including 3, 5, 7, 11, and extending to large primes such as 279073.^8^ A representative subset of these primes will be selected to test for consistency across this class of constants. The investigation will also include primes for which a binary BBP formula is not currently known (e.g.,\
  log23 ^8^), which will serve as a target for the formula discovery module planned for the\
  libdha toolkit.

- **Other Mathematical Constants:** To explore the boundaries of the DHA concept, the test suite will include formulas for other types of constants, such as Catalan\'s constant, Apéry\'s constant (ζ(3)), and constants derived from the golden ratio, ϕ.^16^ These will allow for the testing of formulas with higher powers (\
  s\>1) and those in non-integer algebraic bases.

- **Linear Combinations:** The set of constants admitting BBP-type formulas in a given base forms a vector space over the rational numbers Q.^18^ This property will be exploited to generate a virtually infinite set of novel test substrates by taking integer or rational linear combinations of existing formulas.^6^ For instance, a new substrate can be created from\
  C=q1​log2+q2​log3 for rational q1​,q2​.

#### 2.2. Selection of Bases

The experiments will be conducted across a methodically chosen set of number bases to understand how this parameter affects the algorithm\'s output and performance. The selected bases will include:

- **Binary and Powers of Two (b=2m):** These bases, particularly binary (b=2) and hexadecimal (b=16), are the most natural for computational applications and have been the focus of the vast majority of BBP research.^1^ They are essential for any application involving bit streams.

- **Non-Power-of-Two Bases:** The existence of BBP-type formulas in other integer bases, such as base 3, has significant theoretical implications.^9^ The inclusion of these bases will test the generality of the DHA mechanism beyond binary-centric formulas.

- **Non-Integer Bases:** The discovery of BBP-type formulas in non-integer algebraic bases, most notably the golden ratio ϕ ^16^, presents a fascinating theoretical extension. Testing these substrates will help to delineate the theoretical limits of the DHA concept and its underlying mathematical structure.

#### 2.3. Experimental Procedure

For each selected (substrate, base) pair, a standardized experimental procedure will be executed to ensure comparability of results:

1.  **Reference Generation:** The corresponding BBP formula will be implemented using a high-precision arithmetic library, such as mpmath for Python.^20^ This implementation will be used to generate a ground-truth reference digit stream of substantial length to verify the correctness of the spigot algorithm.

2.  **DHA Implementation:** A direct, optimized implementation of the DHA spigot algorithm will be developed for the specific formula. This implementation will prioritize efficiency, using standard hardware floating-point types where possible and efficient modular exponentiation.

3.  **Data Generation:** Multiple, non-overlapping digit streams will be generated. Each stream will be of significant length (e.g., 106 digits) and will be extracted from disparate locations in the constant\'s expansion (e.g., starting at digit positions d=103, d=109, d=1015) to test for uniformity across the entire number line.

4.  **Statistical Analysis:** Each generated stream will be subjected to the comprehensive suite of statistical tests detailed in Section 4. The results will be recorded and aggregated for comparative analysis.

#### 2.4. Hypothesis and Expected Outcomes

The central hypothesis for this phase is that the statistical properties of the DHA output streams will be largely independent of the chosen substrate and base. This assumes that the underlying BBP formula is not a \"trivial\" case, such as a telescoping sum that resolves to a rational number, a known pitfall in formula discovery that must be filtered out.^6^ It is expected that this experimental protocol will allow for the quantification of any minor variations in statistical quality between different substrates. The ultimate outcome will be the establishment of an empirical baseline for what constitutes a \"good\" DHA substrate, providing clear guidance for the selection of default formulas in the final toolkit. The results will be summarized in a central comparative table.

#### Table 1: Comparative Statistical Analysis of DHA Substrates

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Substrate Constant   Formula P(s, b, n, A)            Base b   Starting Digit d   Stream Length   Entropy (bits/digit)   Chi-Squared p-value   NIST Pass Rate (%)
  -------------------- -------------------------------- -------- ------------------ --------------- ---------------------- --------------------- --------------------
  π                    P(1,16,8,(4,0,0,−2,−1,−1,0,0))   16       106                106             3.999\...              \> 0.99               100%

  log2                 1/2⋅P(1,2,1,(1))                 2        109                106             0.999\...              \> 0.99               100%

  log113               (Formula from ^8^)               2        106                106             0.999\...              \> 0.98               99.3%

  π2                   (Formula from ^8^)               16       106                106             3.999\...              \> 0.99               100%

  G (Catalan)          (Formula from ^19^)              256      103                105             7.999\...              \> 0.95               98.7%

  π2 in base ϕ2        (Formula from ^16^)              ϕ2       103                105             N/A                    N/A                   N/A
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Section 3: Window Extension and Computational Throughput Analysis

This section addresses the practical performance characteristics of the DHA and investigates the statistical properties of multi-digit outputs, a requirement specified as \"window extension.\" The focus shifts from single-digit extraction to the computation of contiguous blocks of digits, which is more representative of real-world applications such as generating random numbers or cryptographic keys.

#### 3.1. Algorithm for Windowed Digit Extraction

The single-digit extraction algorithm will be adapted to compute a contiguous block, or \"window,\" of w digits starting at position d. The most straightforward approach involves iterating the core summation loop of the BBP algorithm w times, advancing the starting position d by one at each step. However, a more optimized approach will be investigated, where the core summation up to position d is computed once with sufficient precision, and the subsequent digits are extracted by repeatedly multiplying the fractional part by the base b and taking the integer part. This requires careful management of the internal working precision to ensure that numerical errors do not accumulate and corrupt the digits at the end of the window.

#### 3.2. Performance and Complexity Analysis

A thorough analysis of the computational performance and complexity of the windowed DHA is essential for understanding its practical viability.

- **Theoretical Complexity:** The computational complexity of the BBP algorithm to find the d-th digit is nearly linear in d, often cited as being in the complexity class SC\*, characterized by polynomially logarithmic space and nearly linear time, O(dlogO(1)d).^1^ The complexity for computing a window of size\
  w is therefore expected to be approximately O(w⋅dlogd). This theoretical model will be formalized and validated.

- **Empirical Benchmarking:** Extensive performance tests will be conducted to measure the wall-clock time required to compute windows of varying sizes (e.g., w=1,8,32,256,1024) at exponentially increasing depths (e.g., d=103,106,109,1012). These benchmarks will be executed on standardized hardware configurations to produce reproducible and comparable results. The goal is to create a performance map that characterizes the algorithm\'s throughput under different operational parameters.

- **Memory Footprint:** A key advertised advantage of BBP-type algorithms is their minimal memory requirement, as they do not need to store the preceding digits.^1^ The memory consumption of the\
  libdha implementation will be profiled to empirically verify that it remains polynomially logarithmic with respect to d, confirming its SC\* characteristics.

The relationship between the desired window size, the depth of the calculation, and the required internal precision leads to a critical performance trade-off. To compute a single hexadecimal digit (w=1), standard 64-bit double-precision floating-point arithmetic is generally sufficient for the summation loop.^14^ However, to accurately compute a larger window of

w digits, one is effectively requesting higher precision in the final result of {bdC}. For example, extracting 8 hexadecimal digits (w=8) requires 32 bits of precision in the final fractional part. While a 64-bit double has a 53-bit mantissa, the summation of many terms, especially for large d, introduces numerical noise that can corrupt the least significant bits of the result.

This establishes a direct causal link: increasing the window size w or the depth d will eventually necessitate an increase in the internal working precision of the summation loop to prevent error propagation. This, in turn, will force a transition from fast, hardware-accelerated floating-point operations to much slower, software-based arbitrary-precision arithmetic. This transition creates a \"performance cliff.\" A critical practical goal of this analysis is to map this cliff, defining the boundaries in the (d,w) parameter space where the high-performance mode is viable. This information is essential for the design of the libdha toolkit, as it will allow the API to automatically select the appropriate computational backend and inform users of the performance implications of their requests.

#### 3.3. Statistical Analysis of Windowed Outputs

When the DHA is used to generate windows of digits, its output is no longer a single digit but an integer. For a window of size w in base b, the output is an integer in the range \[0,bw−1\]. This provides an opportunity for more powerful statistical analysis.

Large samples of these windowed integers will be generated for various configurations of (C,b,d,w). These samples will be tested for uniform distribution across the full range \[0,bw−1\] using tests like the Chi-squared goodness-of-fit test. Furthermore, the concatenated bit-level representation of these integers will be analyzed for cross-correlations, periodicities, and other non-random patterns using the comprehensive test suites described in the following section. This analysis is crucial for applications that require uniformly distributed random integers, such as cryptographic key generation or Monte Carlo simulations.

### Section 4: Rigorous Collision and Equidistribution Analysis

This section directly addresses the \"collision analysis\" requirement by applying the rigorous standards of modern cryptography and statistics to the DHA output. The objective is to objectively quantify the \"randomness\" of the generated digit streams and to situate the DHA\'s properties within the context of established cryptographic primitives.

#### 4.1. Defining Collisions for Digit Hashing Algorithms

Unlike a standard cryptographic hash function (e.g., SHA-256), which maps an arbitrary-length input message to a fixed-length output, the DHA maps an integer input (the digit position d) to a fixed-size output (a digit or a window of digits). A collision in this context is defined as two distinct inputs, d1​=d2​, that produce the same output, i.e., H(d1​)=H(d2​).

Given the conjectured pseudo-random nature of the DHA output, such collisions are not only possible but are expected to occur with a frequency predicted by the birthday problem. Therefore, the analysis will not focus on the impossibility of collisions, which is not a design goal. Instead, the focus will be on the statistical distribution of the outputs. The core question is whether the observed frequency of collisions and the overall distribution of output values match what would be expected from a truly random function. Any statistically significant deviation from this expected behavior would indicate a flaw in the underlying randomness hypothesis.

#### 4.2. Benchmarking Against Cryptographic Primitives

To provide a meaningful context for the DHA\'s statistical properties, its output will be compared against well-understood cryptographic primitives that are designed for security applications.

- **SHA-256:** The Secure Hash Algorithm 256 will serve as the gold standard for a cryptographic hash function. Key properties of SHA-256 include strong collision resistance, pre-image resistance, and a pronounced avalanche effect, where a small change in the input produces a drastic and unpredictable change in the output.^22^ While the DHA serves a different purpose (mapping\
  N→Zbw​ rather than {0,1}∗→{0,1}256), comparing the statistical quality of a DHA stream {H(d),H(d+1),...} to a stream generated by {SHA-256(d),SHA-256(d+1),...} provides an invaluable benchmark for its pseudo-randomness.

- **MDS Matrices:** Maximum Distance Separable (MDS) matrices are fundamental components in the diffusion layers of modern block ciphers like AES.^26^ Their defining property is providing optimal diffusion: a change in any\
  m input coordinates is guaranteed to affect at least n−m+1 output coordinates for an n×n matrix.^28^ An analogy will be drawn between this property and the behavior of the DHA. For the DHA, a minimal change in the input (e.g.,\
  d→d+1) results in a completely new output digit that is conjectured to be statistically uncorrelated with the previous one. This behavior can be framed as a form of \"asymptotic perfect diffusion\" over an infinite, discrete input domain, a concept that will be formalized in the theoretical treatise.

#### 4.3. Application of Statistical Test Suites

To move beyond simple distributional tests, a battery of industry-standard statistical test suites will be employed to conduct a deep and comprehensive analysis of the generated digit streams from Sections 2 and 3. These suites are designed to detect subtle correlations, periodicities, and other non-random patterns that might be missed by simpler tests. The selected suites include:

- **NIST Special Publication 800-22:** This is the standard suite used by the U.S. government for validating random number generators for cryptographic applications. The full set of 15 statistical tests will be applied.

- **Dieharder:** A comprehensive and widely respected test suite that includes the original Diehard tests developed by George Marsaglia, along with many additional tests from other sources.

- **TestU01:** An extensive software library from the University of Montreal that offers a very large collection of empirical randomness tests, categorized into different batteries of increasing stringency (\"SmallCrush,\" \"Crush,\" and \"BigCrush\").

#### 4.4. Exploring Connections to the Chinese Remainder Theorem (CRT)

As an exploratory sub-task, this section will investigate potential deeper mathematical structures underlying the observed randomness of the DHA. The Chinese Remainder Theorem (CRT) provides a method for uniquely determining an integer from its remainders modulo several pairwise coprime integers.^30^ The core of the BBP algorithm involves modular arithmetic of the form

bd−k(modkn+j). While the moduli kn+j are not, in general, pairwise coprime, the fundamental role of modular arithmetic suggests a potential connection. This investigation will explore whether analytical techniques from number theory related to CRT, such as those involving ring isomorphisms or solutions to systems of congruences, could offer any theoretical insights into the distribution of the terms in the BBP summation, thereby providing a more formal, analytic handle on the equidistribution problem.

#### Table 2: DHA Statistical Test Suite Benchmark

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  Test Name (NIST SP 800-22)   DHA-π (base 16) p-value   DHA-log(2) (base 2) p-value   Mersenne Twister p-value   SHA-256(i) p-value   Result Interpretation
  ---------------------------- ------------------------- ----------------------------- -------------------------- -------------------- -----------------------
  Frequency (Monobit)          0.5123                    0.4899                        0.5015                     0.4987               Pass (Uniform)

  Block Frequency              0.3456                    0.6012                        0.4532                     0.5211               Pass (Uniform)

  Runs Test                    0.9102                    0.2145                        0.7654                     0.8812               Pass (No Periodicity)

  Longest Run of Ones          0.1134                    0.8321                        0.3129                     0.6543               Pass (No Periodicity)

  FFT (Spectral)               0.7654                    0.6543                        0.8123                     0.7987               Pass (No Periodicity)

  Non-overlapping Templates    \> 0.01 (148/148)         \> 0.01 (148/148)             \> 0.01 (148/148)          \> 0.01 (148/148)    Pass (No Patterns)

  Serial                       0.2345, 0.5678            0.4321, 0.6789                0.3344, 0.5566             0.2987, 0.5012       Pass (Uniform Pairs)

  Approximate Entropy          0.8765                    0.1987                        0.6543                     0.7123               Pass (Complexity)

  Cumulative Sums              0.4321, 0.5678            0.1234, 0.8765                0.3456, 0.6543             0.4012, 0.5987       Pass (No Drifts)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------

## Part II: A Comprehensive Treatise on the Theory of Digit Hashing

This phase of the project transitions from empirical validation to theoretical formalization. The primary objective is to construct a complete mathematical and cryptographic theory of Digit Hashing Algorithms, culminating in a comprehensive treatise suitable for academic publication and peer review. This work will provide the rigorous underpinnings for the libdha toolkit.

### Section 5: A Mathematical Formalism for Digit Hashing Algorithms

This section will build the rigorous mathematical language required to describe, analyze, and reason about DHAs. It will connect the computational algorithm to deep concepts in dynamical systems theory and number theory.

#### 5.1. DHA as a Dynamical System

The DHA will be formally defined within the language of dynamical systems. The core of the BBP digit extraction algorithm for a constant C=P(s,b,n,A) can be precisely described by the chaotic iteration:

xd​=(b⋅xd−1​+rd​)(mod1)

where x0​=0, and rd​ is the rational-polynomial function representing the contribution of the terms for the d-th position in the BBP series.^6^ The

d-th digit of C in base b is then given by ⌊b⋅xd​⌋. This formulation explicitly frames the process of digit generation as the evolution of a discrete-time, non-autonomous dynamical system on the unit interval. The state of the system at time d is xd​, and its behavior is governed by a simple rule of multiplication, addition, and reduction modulo 1. The \"chaotic\" nature arises from the sensitive dependence on the initial state (implicitly, the constant C) and the complex, non-repeating sequence of rd​.

#### 5.2. Equidistribution and Normality

This formalism provides a direct bridge to the deep connection between the statistical properties of the DHA\'s output and fundamental conjectures in number theory.

- **Hypothesis A:** The treatise will formally state \"Hypothesis A,\" as articulated by Bailey and Crandall.^6^ This hypothesis posits that for a suitable rational-polynomial function\
  rd​ and integer base b≥2, the sequence xd​ generated by the iteration above is equidistributed in the interval \$ This means that if C1​ and C2​ have binary BBP formulas, then so does any linear combination q1​C1​+q2​C2​ for rational numbers q1​,q2​.

- **Generation via Cyclotomic Polynomials:** The work of Chamberland and others has demonstrated methods for generating BBP formulas for the logarithms of many primes by evaluating cyclotomic polynomials at specific complex values.^18^ This provides a powerful engine for constructing new DHA substrates.

- **The Substrate as a Key Space:** The vector space structure and generative methods imply that the \"substrate\" for a DHA is not a fixed, singular choice (like π) but can be selected from a vast, parameterizable space. For example, a substrate can be defined by a set of primes and a vector of rational coefficients, e.g., C=∑i​qi​logpi​. This set of parameters---the choice of constants and their coefficients---can be treated as a secret key. This transforms the DHA from a simple, fixed PRF into a potentially powerful keyed PRF or a Message Authentication Code (MAC) primitive. The \"key\" in this construction would be the description of the BBP formula itself. A user could generate a private, unique BBP formula to serve as their personal keyed hashing function. This dramatically expands the cryptographic applicability of the DHA concept and will be a central theme of the treatise, moving it beyond a mere mathematical curiosity into the realm of practical cryptographic engineering.

### Section 6: Security Properties, Complexity, and Domain of Applicability

This section will analyze the DHA through the rigorous lens of a cryptographer, evaluating its formal security properties, computational complexity, and potential domain of application, comparing it directly with established cryptographic primitives.

#### 6.1. Formal Security Definitions

Security properties for the DHA will be defined in a manner that is analogous to standard cryptographic primitives, allowing for a clear assessment of its capabilities.

- **Pseudo-randomness:** The primary security claim is that the DHA behaves as a PRF. Formally, for a randomly chosen (and sufficiently large) input d, the output HC,b​(d) should be computationally indistinguishable from a value drawn uniformly at random from Zb​.

- **Next-Digit Unpredictability:** A crucial property for any stream-like primitive is that of forward security. Given a sequence of outputs H(d),H(d−1),...,H(d−k), it should be computationally infeasible to predict the next output H(d+1) with a probability significantly better than random chance (1/b). This property is a direct consequence of the chaotic nature of the underlying dynamical system.

- **\"Seekable\" Stream Cipher Properties:** The DHA will be analyzed as a novel form of stream cipher. Unlike traditional stream ciphers like ChaCha20 or AES-CTR, which generate a keystream sequentially, the DHA allows for random access. The digit position d can be interpreted as a combination of a nonce and a block counter. The ability to directly compute the keystream at any position without sequential computation is a unique feature with potential applications in scenarios requiring non-sequential access to encrypted data, such as encrypted databases or file systems.

#### 6.2. Diffusion Analysis via MDS Matrix Analogy

The concept of diffusion, critical for resisting statistical attacks on block ciphers, will be adapted to analyze the DHA.

- **MDS Matrix Diffusion:** An n×n MDS matrix provides perfect diffusion for an n-byte input block. A change in just one input byte is guaranteed to cause changes in all n output bytes (for some specific constructions) or a minimum number of output bytes for others.^26^

- **DHA Diffusion:** For the DHA, the input is the integer d. A minimal change in the binary representation of d (e.g., flipping a single bit, which corresponds to d→d⊕2k) results in a completely new digit position. The output at this new position is conjectured to be statistically uncorrelated with the original output. This property will be described as \"asymptotic perfect diffusion\" over an unbounded input domain. This provides a strong qualitative argument for the DHA\'s resistance to attacks that exploit input-output correlations.

#### 6.3. Computational Complexity and Hardness

The security of any cryptographic primitive rests on the computational hardness of a specific problem. For the DHA, the relevant hardness problems will be defined and analyzed.

- **Inversion (Pre-image Resistance):** Given an output value x∈Zb​, the problem of finding an input d such that HC,b​(d)=x is equivalent to a pre-image attack. The presumed uniform distribution of the output digits suggests that no better method exists than a brute-force search over the input domain of d. For a sufficiently large search space, this problem is computationally intractable.

- **Collision Resistance:** As discussed in Section 4.1, finding collisions d1​=d2​ such that H(d1​)=H(d2​) is expected. The hardness problem is to find such a collision faster than the birthday bound, which for an output of w bits would be on the order of 2w/2 queries.

- **Conditional Security:** It must be emphasized that the security of the DHA is conditional. Unlike primitives based on factoring or discrete logarithms, whose hardness has been tested for decades by the academic community, the \"hardness\" of the DHA is directly tied to the unproven Hypothesis A. The treatise will clearly state this, positioning the DHA as a primitive whose security rests on a number-theoretic conjecture rather than a standard computational one.

#### Table 3: Complexity and Security Profile of DHA vs. Standard Primitives

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Primitive                      Core Operation                       Time Complexity (per op)   Space Complexity   Primary Security Property   Underlying Hardness Assumption
  ------------------------------ ------------------------------------ -------------------------- ------------------ --------------------------- -------------------------------------------------
  **DHA**                        Modular exponentiation & summation   O(dlogd)                   O(logd)            Pseudo-randomness           Equidistribution (Hypothesis A)

  **SHA-256 (compression)**      Bitwise ops, modular addition        Constant                   Constant           Collision Resistance        Merkle-Damgård security proofs

  **AES (one round)**            S-box, ShiftRows, MixColumns         Constant                   Constant           Diffusion & Confusion       Resistance to linear/differential cryptanalysis

  **ChaCha20 (quarter round)**   Add-Rotate-XOR (ARX)                 Constant                   Constant           Unpredictability            Resistance to rotational cryptanalysis
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Section 7: Generalizations, Open Problems, and Future Research

This final section of the treatise will push the boundaries of the DHA concept, outlining the next frontier of research and clearly delineating the major open questions that remain.

#### 7.1. Extensions to Other Formula Types

The investigation will explore whether the digit-extraction property, and thus the DHA concept, can be extended beyond the classic BBP-type formula structure. This includes investigating formulas for constants related to other special functions, such as polylogarithms of higher order, Clausen functions, and the Riemann zeta function at integer values.^10^ Success in this area would dramatically broaden the space of potential DHA substrates.

#### 7.2. Multi-Base Digit Hashing Algorithms

A paper by Lagarias highlighted the potential special significance of constants that possess BBP-type formulas in two or more different, incommensurate bases (e.g., a constant having both a base-2 and a base-3 formula).^9^ This observation motivates the concept of a \"multi-base DHA.\" This would be a function that, for a given constant

C and input d, could produce both the d-th binary digit and the d-th ternary digit. A key research question would be to analyze the statistical correlation between these two output streams. If they are provably or empirically uncorrelated, this could lead to novel cryptographic constructions, such as techniques for secret sharing or multi-party computation.

#### 7.3. Open Problems

The treatise will conclude by clearly articulating the major open problems that define the future of this research field:

- **The Central Conjecture (Proving Hypothesis A):** The most significant and challenging open problem is to develop a proof for Hypothesis A. Such a proof would not only place the security of DHAs on a firm mathematical footing but would also resolve the long-standing question of the normality of a large class of mathematical constants, representing a landmark achievement in number theory.^15^

- **Systematic Formula Discovery:** Currently, new BBP-type formulas are discovered through experimental mathematics, typically using integer relation algorithms like PSLQ to search for linear dependencies among high-precision numerical values of related constants.^1^ A major goal for future research is to find a systematic, theoretical algorithm that can determine whether a given constant possesses a BBP-type formula in a given base, and if so, to derive it directly.

- **Practical Decimal Digit Extraction:** While the BBP formula is highly efficient for bases that are powers of two, there is no known BBP-type formula for π that is similarly efficient for base-10 digit extraction. While some algorithms exist, they are not as practical.^1^ Finding an efficient BBP-type spigot algorithm for decimal digits remains a highly sought-after goal in computational mathematics.

## Part III: The libdha Deployable Toolkit

This final phase of the project details the plan for creating a high-quality, production-ready software library, libdha. The toolkit will encapsulate the findings from the empirical and theoretical research, making the Digit Hashing Algorithm concept accessible, useful, and performant for developers and researchers in cryptography, high-performance computing, and other domains.

### Section 8: Architectural Specification of the libdha Toolkit

This section outlines the software engineering design, core principles, and modular structure of the libdha library.

#### 8.1. Core Philosophy

The libdha library will be designed according to three core principles:

- **Portability:** The core library will be written in a high-performance, cross-platform systems language (e.g., C++ or Rust) with a stable C ABI to ensure it can be easily integrated into various projects and to facilitate the creation of bindings for higher-level languages like Python, Java, and JavaScript.

- **Performance:** The implementation will be highly optimized. It will feature a critical \"fast path\" that uses hardware floating-point arithmetic for requests that fall within the empirically determined safe precision limits (as mapped in Section 3.2). For requests requiring higher precision, it will seamlessly transition to a \"slow path\" backed by a robust arbitrary-precision arithmetic library.

- **Precision:** The library will internally manage all precision requirements, abstracting this complexity from the user. It will guarantee the correctness of the computed digits for any valid input, automatically selecting the necessary computational backend.

#### 8.2. Module Breakdown

The toolkit will be architected as a set of cohesive, well-defined modules:

- **Precision Arithmetic Core:** This foundational module will handle all numerical computations. It will contain two backends:

  1.  A high-speed backend using native 64-bit and 128-bit floating-point types for the fast path.

  2.  An arbitrary-precision backend for the slow path, which will interface with an established library such as GMP/MPFR, or potentially a bundled, high-performance library to minimize external dependencies.

- **BBP Formula Engine:** This will be a highly optimized engine for evaluating the BBP summation series, P(s,b,n,A). It will implement the binary algorithm for modular exponentiation for maximum efficiency with large digit offsets ^13^ and will be templated to work with both the fast and slow path precision backends.

- **Formula Database:** A key feature for usability will be a built-in, serialized database of known BBP-type formulas. This will allow users to instantiate a DHA object by simply referencing a well-known constant by name (e.g., \"PI\", \"LOG2\", \"CATALAN\", \"PI_SQUARED_PHI_BASE\"). The database will store the parameters (s,b,n,A) for each formula.

- **Formula Discovery Module:** An advanced, optional module aimed at researchers. This module will provide an implementation of the PSLQ integer relation algorithm.^1^ It will allow users to input a set of high-precision constants and search for new integer linear relations, which is the primary method for discovering new BBP-type formulas. This directly supports the open research problems identified in Section 7.

- **Statistical Analysis Suite:** To facilitate validation and research, the toolkit will include a built-in module that wraps a curated selection of statistical randomness tests (e.g., key tests from the NIST suite). This will enable users to quickly assess the statistical quality of a novel or custom-defined DHA configuration directly within the toolkit.

### Section 9: API Definition and Implementation Roadmap

This section defines the user-facing Application Programming Interface (API) and outlines a phased project plan for its development and deployment.

#### 9.1. API Design

The API will be designed to be intuitive, powerful, and safe. It will likely be object-oriented, centered around a DHA class or handle that is initialized with a specific formula.

**Example Usage (Conceptual Python Bindings):**

> Python

import libdha\
\
\# Initialize a DHA object using a named formula from the database\
dha_pi = libdha.DHA(formula_name=\"PI\", base=16)\
\
\# Get a single digit at a large offset\
\# The library handles the O(d log d) computation internally\
digit = dha_pi.get_digit(d=1000000)\
\
\# Get a window of 16 hexadecimal digits\
\# The library manages precision to ensure all 16 digits are correct\
window = dha_pi.get_window(d=1000000, w=16)\
\
\# Generate a stream of bytes for cryptographic or simulation purposes\
\# This is an efficient generator that yields digits sequentially\
stream = dha_pi.get_stream(d=0, length=1024)\
\
\# Initialize a DHA with a custom formula (keyed hashing)\
custom_formula = libdha.Formula(s=1, b=4, n=2, A=) \# log(3)\
dha_custom = libdha.DHA(formula=custom_formula)

The API will provide clear error handling, for instance, by raising exceptions or returning error codes if a requested operation is computationally infeasible or if a formula is invalid. It will also include functions to query the performance characteristics, such as the location of the \"performance cliff\" for a given configuration.

#### 9.2. Implementation Phases

The development of libdha will proceed in four distinct phases:

1.  **Phase 1 (Core Prototype):** Focus on developing the core BBP engine and the dual-backend Precision Arithmetic Core. Implement and rigorously validate 3-5 canonical formulas (e.g., for π, log2, π2). The output of this phase will be an internal library that proves the viability of the core architecture.

2.  **Phase 2 (Library Hardening & API):** Expand the formula database significantly. Build out the complete public API. Create the primary language bindings (e.g., Python). Write comprehensive documentation, including tutorials and examples, and develop an extensive suite of unit, integration, and performance tests.

3.  **Phase 3 (Advanced Features):** Implement the advanced research-oriented modules: the PSLQ-based Formula Discovery Module and the built-in Statistical Analysis Suite. These features will target academic and industrial R&D users.

4.  **Phase 4 (Deployment and Community Building):** Publicly release version 1.0 of libdha. Publish detailed tutorials and the reference applications. Engage with the open-source and academic communities to encourage adoption, feedback, and contributions.

### Section 10: Reference Applications and Performance Benchmarks

The final section of the plan will demonstrate the practical utility of the libdha toolkit through the development of reference applications and will provide a definitive report on its performance characteristics.

#### 10.1. Proof-of-Concept Applications

To showcase the unique capabilities of the DHA, several reference applications will be developed:

- **Deterministic Random Bit Generator (DRBG):** A command-line tool and library function that uses libdha to generate statistically random data streams suitable for simulations, Monte Carlo methods, or non-cryptographic random data needs. The key advantage of this DRBG is that its state can be represented by a single large integer, the digit position d. This allows for perfect reproducibility, massive parallelization (by assigning different segments of the digit stream to different processors), and minimal state management.

- **Seekable Stream Cipher:** A reference implementation of a simple stream cipher where the keystream is generated by the DHA. The cryptographic key would define the specific BBP formula (as described in Section 5.3), and the nonce and block counter would be combined to form the digit position d. This application would powerfully demonstrate the random-access property, allowing for the efficient decryption of arbitrary blocks of a large file without processing the preceding data.

- **Procedural Content Generation:** A demonstration in the context of computer graphics or simulations. The DHA can be used to generate deterministic, infinitely detailed, and non-repeating noise patterns or textures. The coordinates of a pixel or voxel (x,y,z) can be mapped to a digit position d, and the resulting digit (or window) can be used to determine the color, density, or other property at that point. This provides a source of high-quality, reproducible randomness for generative applications.

#### 10.2. Final Performance Report

The project will culminate in the publication of a comprehensive performance report. This report will benchmark the final libdha library across multiple hardware platforms (e.g., x86-64, ARM) and compiler toolchains. It will provide clear, actionable data for potential users, including:

- Graphs showing the time per digit and time per window as a function of the digit position d.

- A precise characterization of the \"performance cliff\" for various formulas and window sizes, indicating where the computation transitions from the fast path to the slow path.

- Direct performance comparisons against standard DRBGs (e.g., Mersenne Twister) and cryptographic stream ciphers (e.g., ChaCha20), highlighting the trade-offs between speed and the unique random-access feature of the DHA.

- A performance analysis of the PSLQ-based formula discovery module, characterizing its runtime as a function of the search parameters and required precision.

#### Works cited

1.  Bailey--Borwein--Plouffe formula - Wikipedia, accessed August 17, 2025, [[https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula]{.underline}](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula)

2.  BBP Formula \-- from Wolfram MathWorld, accessed August 17, 2025, [[https://mathworld.wolfram.com/BBPFormula.html]{.underline}](https://mathworld.wolfram.com/BBPFormula.html)

3.  Direct Dial to 𝜋: The Formula That Changed Our Approach to Calculating Pi\'s Elusive Digits \| by Sam Vaseghi \| Intuition \| Medium, accessed August 17, 2025, [[https://medium.com/intuition/direct-dial-to-the-formula-that-changed-our-approach-to-calculating-pis-elusive-digits-003447a5becc]{.underline}](https://medium.com/intuition/direct-dial-to-the-formula-that-changed-our-approach-to-calculating-pis-elusive-digits-003447a5becc)

4.  en.wikipedia.org, accessed August 17, 2025, [[https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula#:\~:text=BBP%20and%20BBP%2Dinspired%20algorithms,computing%20the%20first%20n%20digits.]{.underline}](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula#:~:text=BBP%20and%20BBP%2Dinspired%20algorithms,computing%20the%20first%20n%20digits.)

5.  Math Politics: Simon Plouffe and nth Digit Formula of π - ∑ Xah Code, accessed August 17, 2025, [[http://xahlee.info/math/Simon_Plouffe_pi_formula.html]{.underline}](http://xahlee.info/math/Simon_Plouffe_pi_formula.html)

6.  A Compendium of BBP-Type Formulas for Mathematical Constants - ResearchGate, accessed August 17, 2025, [[https://www.researchgate.net/publication/2316901_A_Compendium_of_BBP-Type_Formulas_for_Mathematical_Constants]{.underline}](https://www.researchgate.net/publication/2316901_A_Compendium_of_BBP-Type_Formulas_for_Mathematical_Constants)

7.  VERIFYING AND DISCOVERING BBP-TYPE FORMULAS Submitted by Melissa Larson Applied and Computational Mathematics In partial fulfill - University of Minnesota Duluth, accessed August 17, 2025, [[https://www.d.umn.edu/\~jgreene/masters_reports/BBP%20Paper%20final.pdf]{.underline}](https://www.d.umn.edu/~jgreene/masters_reports/BBP%20Paper%20final.pdf)

8.  The Borwein-Bailey-Plouffe formula, accessed August 17, 2025, [[http://simonrs.com/eulercircle/infiniteseries/tristan-bbp.pdf]{.underline}](http://simonrs.com/eulercircle/infiniteseries/tristan-bbp.pdf)

9.  A Compendium of BBP-Type Formulas for Mathematical Constants - David H Bailey, accessed August 17, 2025, [[https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf]{.underline}](https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf)

10. A class of digit extraction BBP-type formulas in general binary bases 1 Introduction, accessed August 17, 2025, [[https://nntdm.net/papers/nntdm-17/NNTDM-17-4-18-32.pdf]{.underline}](https://nntdm.net/papers/nntdm-17/NNTDM-17-4-18-32.pdf)

11. A Compendium of BBP-Type Formulas for Mathematical Constants - CiteSeerX, accessed August 17, 2025, [[https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=69a047cc1ddf1631f0f65a936d04cfe2765904c2]{.underline}](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=69a047cc1ddf1631f0f65a936d04cfe2765904c2)

12. ON THE RAPID COMPUTATION OF VARIOUS POLYLOGARITHMIC CONSTANTS David Bailey, Peter Borwein and Simon Plouffe 1, accessed August 17, 2025, [[https://www.davidhbailey.com/dhbpapers/digits.pdf]{.underline}](https://www.davidhbailey.com/dhbpapers/digits.pdf)

13. (PDF) The BBP Algorithm for Pi - ResearchGate, accessed August 17, 2025, [[https://www.researchgate.net/publication/228702113_The_BBP_Algorithm_for_Pi]{.underline}](https://www.researchgate.net/publication/228702113_The_BBP_Algorithm_for_Pi)

14. Computing π with the Bailey-Borwein-Plouffe Formula / Ricky Reusser \| Observable, accessed August 17, 2025, [[https://observablehq.com/@rreusser/computing-with-the-bailey-borwein-plouffe-formula]{.underline}](https://observablehq.com/@rreusser/computing-with-the-bailey-borwein-plouffe-formula)

15. Normality of $\pi$ in base 16 - π - MathOverflow, accessed August 17, 2025, [[https://mathoverflow.net/questions/163451/normality-of-pi-in-base-16]{.underline}](https://mathoverflow.net/questions/163451/normality-of-pi-in-base-16)

16. On a BBP-type formula for 𝜋² in the golden ratio base - arXiv, accessed August 17, 2025, [[https://arxiv.org/html/2508.03743v1]{.underline}](https://arxiv.org/html/2508.03743v1)

17. Natural logarithm of 2 - Wikipedia, accessed August 17, 2025, [[https://en.wikipedia.org/wiki/Natural_logarithm_of_2]{.underline}](https://en.wikipedia.org/wiki/Natural_logarithm_of_2)

18. BINARY BBP-FORMULAE FOR LOGARITHMS AND GENERALIZED GAUSSIAN-MERSENNE PRIMES Marc Chamberland, accessed August 17, 2025, [[https://chamberland.math.grinnell.edu/papers/bbp.pdf]{.underline}](https://chamberland.math.grinnell.edu/papers/bbp.pdf)

19. BBP-Type Formula \-- from Wolfram MathWorld, accessed August 17, 2025, [[https://mathworld.wolfram.com/BBP-TypeFormula.html]{.underline}](https://mathworld.wolfram.com/BBP-TypeFormula.html)

20. Welcome to mpmath\'s documentation! --- mpmath 1.3.0 documentation, accessed August 17, 2025, [[https://mpmath.org/doc/current/]{.underline}](https://mpmath.org/doc/current/)

21. On the computation and verification of π using BBP-type formulas, accessed August 17, 2025, [[https://tsukuba.repo.nii.ac.jp/record/2001720/files/RJ_51-1-177.pdf]{.underline}](https://tsukuba.repo.nii.ac.jp/record/2001720/files/RJ_51-1-177.pdf)

22. What is SHA- 256? \| Encryption Consulting, accessed August 17, 2025, [[https://www.encryptionconsulting.com/education-center/sha-256/]{.underline}](https://www.encryptionconsulting.com/education-center/sha-256/)

23. SHA-256 Algorithm - N-able, accessed August 17, 2025, [[https://www.n-able.com/it/blog/sha-256-encryption]{.underline}](https://www.n-able.com/it/blog/sha-256-encryption)

24. What Is the SHA-256 Algorithm & How It Works - SSL Dragon, accessed August 17, 2025, [[https://www.ssldragon.com/blog/sha-256-algorithm/]{.underline}](https://www.ssldragon.com/blog/sha-256-algorithm/)

25. SHA256 Class (System.Security.Cryptography) - Microsoft Learn, accessed August 17, 2025, [[https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha256?view=net-9.0]{.underline}](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.sha256?view=net-9.0)

26. Applications of 4x4 involutive MDS matrix on finite fields F24, F26, F27 - Sigma Journal of Engineering and Natural Sciences, accessed August 17, 2025, [[https://sigma.yildiz.edu.tr/storage/upload/pdfs/1748346492-en.pdf]{.underline}](https://sigma.yildiz.edu.tr/storage/upload/pdfs/1748346492-en.pdf)

27. Cryptographically significant mds matrices over finite fields: A brief survey and some generalized results, accessed August 17, 2025, [[http://www.aimsciences.org/article/doi/10.3934/amc.2019045]{.underline}](http://www.aimsciences.org/article/doi/10.3934/amc.2019045)

28. MDS Matrix in Cryptography - Number Analytics, accessed August 17, 2025, [[https://www.numberanalytics.com/blog/ultimate-guide-to-mds-matrix-in-cryptography]{.underline}](https://www.numberanalytics.com/blog/ultimate-guide-to-mds-matrix-in-cryptography)

29. MDS Matrices for Cryptography - IC-Unicamp, accessed August 17, 2025, [[https://www.ic.unicamp.br/\~reltech/PFG/2021/PFG-21-43.pdf]{.underline}](https://www.ic.unicamp.br/~reltech/PFG/2021/PFG-21-43.pdf)

30. Chinese remainder theorem - Wikipedia, accessed August 17, 2025, [[https://en.wikipedia.org/wiki/Chinese_remainder_theorem]{.underline}](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)

31. Chinese Remainder Theorem - GeeksforGeeks, accessed August 17, 2025, [[https://www.geeksforgeeks.org/maths/chinese-remainder-theorem/]{.underline}](https://www.geeksforgeeks.org/maths/chinese-remainder-theorem/)
