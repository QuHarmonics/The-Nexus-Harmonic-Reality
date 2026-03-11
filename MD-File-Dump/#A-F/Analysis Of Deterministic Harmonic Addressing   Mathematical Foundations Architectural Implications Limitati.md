----------- Page1 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 1
A Comprehensive Analysis
of Deterministic Harmonic
Addressing: Mathematical
Foundations, Architectural
Implications, and Practical
Limitations
Driven by Dean Kulik
January 2026
Executive Summary
This report provides a comprehensive technical analysis of Deterministic Harmonic Addressing
(DHA), a novel computational paradigm for direct, searchless information retrieval from the digit
expansions of specific mathematical constants. The core mechanism of DHA is a two-stage
process. The first stage involves a deterministic mapping from an input seed, denoted as
𝑆
, to a
specific digit position or address,
𝑑
. This mapping is governed by modular arithmetic over a large,
pre-computed modulus,
𝑀(𝐾)
, which is derived from the Least Common Multiple (LCM) of
denominators found in the underlying mathematical formula. The mathematical integrity of this
addressing scheme is underpinned by the principles of the Chinese Remainder Theorem (CRT).
The second stage employs a "locked projector" function,
𝑃
ி
, which leverages the well-established
properties of Bailey-Borwein-Plouffe (BBP) type formulas to extract the digit or a window of digits
at the computed address
𝑑
without calculating any preceding digits.
The central findings of this analysis validate the mathematical plausibility and internal consistency
of the DHA mechanism. Its architecture elegantly builds upon the foundational work of BBP-type
digit extraction, introducing a novel and deterministic method for selecting the target digit
position. This approach eliminates any form of search, iteration, or optimization (argmin) during----------- Page2 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 2
the lookup phase, offering a "zero traversal" guarantee. However, the report identifies a critical
and significant scalability bottleneck associated with the pre-computation and magnitude of the
addressing modulus,
𝑀(𝐾)
. This modulus, essential for the system's cyclic properties, grows at a
super-exponential rate with the desired precision of the output, representing a formidable one-
time setup cost.
Potential applications for DHA are identified in domains requiring verifiable, deterministic, and
computationally reproducible data generation. These include cryptographic systems (for key and
nonce generation), high-fidelity scientific simulations (as a source for quasi-Monte Carlo
methods), and auditable data storage and retrieval systems. The primary limitations of the DHA
framework are threefold: the "field criterion," which restricts its application to the esoteric class
of constants admitting BBP-type formulas; the base-dependency of the BBP digit extraction,
which constrains the output format (e.g., to hexadecimal for
𝜋
); and the aforementioned
computational burden of the
𝑀(𝐾)
modulus.
In conclusion, Deterministic Harmonic Addressing represents a theoretically sound and
architecturally elegant framework that bridges deterministic input with the pseudo-random
structure of transcendental numbers. Its practical viability is, however, highly constrained by its
substantial pre-computation requirements. The system is best characterized as a "bake-once,
read-many" architecture, optimally suited for specialized applications where the underlying
mathematical "field" is fixed and the high cost of initialization can be amortized over a vast
number of subsequent, rapid lookups.
1.0 Deconstruction of the Deterministic Harmonic Addressing Paradigm
1.1 The Central Thesis: Input as Operator
The conceptual foundation of Deterministic Harmonic Addressing (DHA) is articulated in its
central thesis: "the input is the operator." This statement signifies a fundamental departure from
conventional computational models that treat an input as a query to be processed through
search, optimization, or iterative refinement. In a typical search algorithm, the input defines a
target, and the system executes a series of steps—often involving loops over a variable x or an
argmin function—to locate data that matches the target. In contrast, the DHA framework
redefines the input seed,
𝑆
, as a direct parameter to a deterministic mathematical function. This
function does not search for an answer; it computes one directly. The seed does not ask a
question; it commands an operation.
This operational paradigm is predicated on the existence of a highly structured, infinite
information field—a specific mathematical constant—from which data (digits) can be extracted.
The role of the input seed is to act as a precise navigational instruction, directing the
computational machinery to a unique location within this field and extracting the information----------- Page3 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 3
resident at that location. The process is entirely deterministic, meaning a given seed
𝑆
will always
produce the exact same output. It is also "truthful" in the sense that the output is a verifiable
property of the underlying mathematical constant, not an approximation derived from a heuristic
process. This philosophy of direct computation over traversal or search is the defining
characteristic of the DHA architecture.
1.2 The Two-Stage Architecture
The DHA mechanism is implemented as a distinct two-stage process, separating the problem of
locating information from the problem of extracting it.
Stage 1: Addressing (Seed
→
Address)
In this initial stage, an input seed
𝑆
is transformed into a numerical address
𝑑
. This address
corresponds to a specific digit position within the base-
𝑏
expansion of the chosen constant,
𝐹
.
The mapping is a direct, deterministic function, primarily involving modular arithmetic. The seed is
reduced modulo a very large, carefully constructed integer,
𝑀(𝐾)
, which defines the cyclic nature
of the address space. The result of this operation is the address
𝑑
. This stage is notable for its
complete absence of search loops or iterative approximation. The address is not found; it is
calculated in a single, direct step.
Stage 2: Projection (Address
→
Digit(s))
Once the address
𝑑
is determined, it is passed to the second stage, termed the "locked
projector." This component is a specialized computational engine designed to extract the digit (or
a small window of
𝑊
digits) starting at position
𝑑
of the constant
𝐹
. This is achieved using a digit-
extraction algorithm of the Bailey-Borwein-Plouffe (BBP) type. The projector function,
𝑃
ி
(𝑏, 𝑑, 𝑊)
,
leverages modular arithmetic to perform this extraction efficiently, without needing to compute
the
𝑑 −1
digits that precede it. The term "locked" signifies that the projector is a fixed
mathematical function defined by the chosen constant, base, and BBP formula; it is an immutable
part of the system's configuration.
This two-stage design creates a clear separation of concerns. The addressing mechanism is a
novel contribution that imposes a deterministic structure on the selection of digit positions. The
projection mechanism leverages a known, powerful technique for efficient information retrieval
from that selected position.
1.3 Contrasting DHA with Existing Methodologies
To fully appreciate the architectural novelty of DHA, it is essential to contrast it with existing
methodologies for computing the digits of mathematical constants.
Versus Full Computation: The most straightforward method for finding the
𝑑
-th digit of a
constant is to compute its value from the beginning using a suitable series or algorithm, storing all
intermediate digits until the desired position is reached. For large values of
𝑑
, this approach is----------- Page4 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 4
computationally infeasible due to its immense memory requirements (proportional to
𝑑
) and
processing time. DHA's primary advantage is its ability to bypass this requirement entirely.
Versus Spigot Algorithms: Spigot algorithms represent a significant improvement by generating
digits sequentially, one at a time, without needing to store all previous digits.
1
The name evokes
the image of a tap (a spigot) releasing digits in a controlled, sequential flow.
1
While they are
memory-efficient, they are fundamentally serial. To get to the
𝑑
-th digit, one must still effectively
traverse the computation for the preceding digits. The DHA paradigm of "Zero traversal" is a
direct counterpoint to this sequential generation model.
Versus Digit-Extraction Algorithms (BBP): The discovery of the Bailey-Borwein-Plouffe (BBP)
formula in 1995 was a landmark achievement, introducing the concept of a true digit-extraction
algorithm.
4
The BBP formula and its variants allow for the computation of the
𝑑
-th digit of certain
constants (like
𝜋
in base 16) in isolation, without computing the digits from 1 to
𝑑 −1
.
4
This is
precisely the mechanism used in DHA's projection stage. However, the BBP algorithm itself
provides no guidance on how to choose the digit position
𝑑
. The selection of
𝑑
is external to the
algorithm; it is an arbitrary input provided by the user. DHA's innovation is not in the extraction
itself, but in providing a formal, deterministic mechanism for mapping an input seed
𝑆
to the
address
𝑑
. It builds an architectural framework around the BBP engine, transforming it from a tool
for arbitrary lookups into a component of a deterministic input-output system.
The following table provides a structured comparison of these methodologies, highlighting the
unique position of DHA.
Table 1: Comparison of Digit Computation Methodologies
Metric Full
Computation
Spigot
Algorithm
BBP Digit
Extraction
Deterministic
Harmonic
Addressing
(DHA)
Random
Access
Capability
No No Yes Yes (via
deterministic
mapping)----------- Page5 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 5
State
Dependency
Requires all
𝑑 −
1
previous
digits
Requires state
from previous
digit
Stateless (per-
digit
computation)
Stateless (per-
lookup
computation)
Memory
Complexity
𝑂(𝑑)
𝑂(log𝑑)
or
𝑂(1)
𝑂(log𝑑)
𝑂(log𝑑)
for
lookup; high for
pre-
computation
Time
Complexity
for
𝑑
-th digit
𝑂(𝑑
ଶ
)
or higher
𝑂(𝑑
ଶ
)
or higher
𝑂(𝑑log𝑑)
6
𝑂(𝐾log𝑑)
for
lookup; high for
pre-
computation
Pre-
computation
Cost
Low Low Low Very High
(Computation
of
𝑀(𝐾)
)
Key
Mathematical
Principle
Series
Summation
Mixed-Radix
Representation
3
Modular
Exponentiation
5
BBP + Chinese
Remainder
Theorem
This comparison clarifies that DHA's value proposition is not in improving the speed of a single
digit extraction over BBP, but in creating a new capability: the deterministic, verifiable, and
searchless mapping from a compact input seed to a specific, extractable piece of information
within a vast mathematical constant. It trades a significant one-time pre-computation cost for the
ability to perform these mappings directly and efficiently.
2.0 The Field Criterion: BBP-Type Constants as Information Substrates
2.1 The Bailey-Borwein-Plouffe (BBP) Formula as a Gateway
The operational domain of the DHA mechanism is not arbitrary; it is strictly defined by what is
termed the "Field criterion." A constant
𝐹
qualifies as a valid information field for DHA if and only if
it admits a series representation of a specific form, known as a BBP-type formula.
5
The general
form of such a formula is:----------- Page6 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 6
𝛼 = ෍
𝑝(𝑘)
𝑏
௞
𝑞(𝑘)
ஶ
௞ୀ଴
where
𝑝(𝑘)
and
𝑞(𝑘)
are polynomials with integer coefficients,
deg
(𝑝)<
deg
(𝑞)
, and
𝑏 ≥2
is an
integer base.
8
The thesis provides a more specific, yet common, instance of this structure:
𝐹 = ෍
1
𝑏
௞
ஶ
௞ୀ଴
෍
𝑐
௝
𝑎 ⋅ 𝑘 + 𝑟
௝
௃
௝ୀଵ
In this formulation, the polynomial ratio
𝑝(𝑘)/𝑞(𝑘)
is expressed as a sum of partial fractions where
the denominator
𝑞(𝑘)
is a product of linear factors. This structure is the fundamental enabler for
digit extraction. The term
1/𝑏
௞
acts as a base-
𝑏
positional operator; each term in the outer sum
contributes to the digits of
𝐹
at positions increasingly shifted to the right. This allows for the
mathematical isolation of digits at a specific position
𝑑
by multiplying the entire series by
𝑏
ௗ
,
which effectively shifts the
𝑑
-th digit to the left of the radix point, allowing its value to be
determined by examining the fractional part of the resulting sum.
5
Without a constant's
adherence to this BBP-form, the "locked projector" of DHA would have no mathematical
foundation upon which to operate.
The discovery of such formulas is not systematic. It is often the result of experimental
mathematics, employing integer relation-finding algorithms like PSLQ (Partial Sum of Squares -
Lower Quadrature) to search for linear combinations of related series that sum to a known
constant.
5
This means the set of known DHA-compatible fields is a product of discovery rather
than a systematically derivable class of numbers.
2.2 Analysis of Qualifying Constants
The class of constants for which BBP-type formulas are known, while esoteric, is surprisingly rich
and includes many fundamental mathematical entities. The canonical example, and the one that
sparked the field, is the formula for
𝜋
in base 16, discovered by Simon Plouffe in 1995
5
:
𝜋 = ෍
1
16
௞
ஶ
௞ୀ଴
൬
4
8𝑘 +1
−
2
8𝑘 +4
−
1
8𝑘 +5
−
1
8𝑘 +6
൰
This formula perfectly matches the DHA field criterion with
𝑏 =16
,
𝑎 =8
, coefficients
𝑐 =
{4,−2,−1,−1}
, and offsets
𝑟
௝
∈{1,4,5,6}
. Since its discovery, extensive research has produced a
large compendium of similar formulas for other constants.
8
Examples of qualifying constants
include:----------- Page7 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 7
●
Powers of Pi: Formulas exist for
𝜋
ଶ
,
𝜋
ଷ
, and
𝜋
ସ
.
10
●
Logarithms: Numerous logarithms have BBP-type representations, most famously
ln(2)
in
base 2, but also for many other primes and rational arguments such as
ln(3)
,
ln(5)
, and
ln(9/10)
.
8
●
Zeta Function Values: BBP-type formulas have been found for Apéry's constant
𝜁(3)
and
𝜁(5)
.
9
●
Other Special Constants: The set also includes Catalan's constant (
𝐺
), Clausen's integral
values, and various combinations of these constants, such as
𝜋ln(2)
.
9
This body of work defines the universe of potential information substrates for DHA. Each
constant, paired with its specific BBP formula and base, constitutes a unique "field" from which
DHA can deterministically address and project digits. The "field" is therefore not merely the
constant itself, but the triplet
(𝐹, 𝑏,
formula
)
. A single constant like
𝜋
might be part of multiple fields
if it has different BBP-type formulas in different bases, though such instances are rare.
2.3 The Role of Base b and its Implications
A critical and unavoidable constraint of the DHA field criterion is the base-dependency of the BBP
formula. The digit-extraction property is intrinsically tied to the base
𝑏
that appears in the
1/𝑏
௞
term of the series. The famous BBP formula for
𝜋
, for example, is a base-16 formula.
Consequently, it can be used to extract hexadecimal (base-16) digits, and by simple conversion,
binary (base-2) digits. It cannot, however, be used to directly compute decimal (base-10) digits of
𝜋
.
4
This limitation has profound implications for the practical application of a DHA system. If an
application requires output in a specific base (e.g., decimal for financial calculations), a DHA field
can only be used if a BBP-type formula for the underlying constant exists in that specific base.
Research has shown that such formulas are not universally available. For instance, a 2004 paper
by Borwein, Galway, and Borwein demonstrated that no degree-1 BBP-type formula for
𝜋
exists
for any base that is not a power of two.
16
This result strongly suggests that a DHA system built
upon the standard
𝜋
formula is fundamentally incapable of producing decimal digits directly.
Furthermore, the connection between BBP-type constants and the statistical properties of their
digit expansions is an area of active research. It is conjectured that any irrational number with a
BBP-type formula in base
𝑏
is normal to base
𝑏
.
8
Normality implies that any finite sequence of
digits of a given length appears with the expected frequency. If this conjecture holds, it means
that the information substrate being accessed by DHA is, for all statistical purposes, a sequence
of random digits. The DHA mechanism, therefore, provides a deterministic and verifiable method
for accessing a specific segment of a sequence that is computationally indistinguishable from
random noise. This synthesis of determinism and high-quality pseudorandomness is one of the----------- Page8 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 8
most powerful implications of the DHA architecture, particularly for applications in cryptography
and stochastic modeling. It offers a source of what could be termed "verifiable randomness"—a
pseudorandom sequence where the value at any given position can be independently calculated
and verified without reference to the rest of the sequence.
3.0 The Core Computational Engine: The Locked Projector
3.1 The Projector Function
𝑃
ி
(𝑏, 𝑑, 𝑊)
The computational heart of the DHA system is the "locked projector," a function denoted as
𝑃
ி
(𝑏, 𝑑, 𝑊)
. Its purpose is to calculate a window of
𝑊
digits of the constant
𝐹
in base
𝑏
, starting at
the
𝑑
-th position after the radix point. The mathematical basis for this operation is the
manipulation of the BBP series to isolate the desired digits.
The fundamental principle of digit extraction is to shift the target digit into a position where it can
be easily isolated. This is achieved by computing the fractional part of
𝑏
ௗ
𝐹
. Multiplying the
constant
𝐹
by
𝑏
ௗ
shifts the entire digit sequence
𝑑
places to the left, moving the
𝑑
-th fractional
digit into the units place of the integer part. All subsequent digits form the new fractional part.
Therefore, the sequence of digits starting at position
𝑑 +1
is given by
{𝑏
ௗ
𝐹}
, where
{⋅}
denotes
the fractional part.
5
To get the single digit at position
𝑑 +1
, one would compute
⌊𝑏{𝑏
ௗ
𝐹}⌋
.
The DHA projector function is defined using the BBP series for
𝐹
:
$$ P_F(b,d,W) = \left{ \sum_{k=0}^{K} \frac{b^{d-k}}{b} \sum_{j=1}^{J} \frac{c_j}{a \cdot k + r_j}
\right} $$
This formulation is equivalent to computing
{𝑏
ௗିଵ
𝐹}
. The term
𝑏
ௗି௞
effectively scales each
component of the sum, achieving the necessary digit shift. The summation is split into two
conceptual parts: a "head" from
𝑘 =0
to
𝑑
, and a "tail" from
𝑘 = 𝑑 +1
onwards. The integer part
of the shifted value, which must be discarded, arises exclusively from terms in the head of the
sum, as for
𝑘 > 𝑑
, the exponent
𝑑 − 𝑘
is negative, ensuring those terms remain fractional.5
3.2 Truncation and the Tail Bound Unit
Since the BBP series is infinite, a practical computation requires it to be truncated at some finite
number of terms,
𝐾
. The choice of
𝐾
is critical for the accuracy of the result. The thesis specifies
that
𝐾
must be chosen such that the contribution of the residual tail of the series (from
𝑘 = 𝐾 +1
to infinity) is less than
𝑏
ିௐ
, where
𝑊
is the desired window size or precision. This ensures that the
error introduced by truncation is too small to affect the digits being computed. The "Tail bound
unit" mentioned in the hardware sketch is the logical component responsible for this analysis and
the determination of an adequate
𝐾
.----------- Page9 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 9
However, this truncation introduces a subtle but significant potential for error. The calculation
yields the fractional part of the sum with high precision. If this fractional part is extremely close to
1.0 (e.g.,
0.99999999...
), a minuscule error from the truncated tail, when added, could cause a
carry-over that flips the most significant digits (e.g., from a sequence of
𝐹
's in hexadecimal to a
sequence of
0
's).
5
This is analogous to adding 1 to 999 and having the carry propagate through all
digits. While unlikely for a random digit sequence, it is a possibility that must be handled by
choosing a sufficiently large
𝐾
and using adequate computational precision, making the error
analysis performed by the Tail bound unit a non-trivial aspect of a robust implementation.
3.3 The Mechanics of Modular Arithmetic
The true computational elegance of the BBP algorithm, and thus the DHA projector, lies in its use
of modular arithmetic to manage the size of intermediate calculations. A naive evaluation of the
projector sum would involve multi-precision arithmetic, as the numerators
𝑏
ௗି௞
would become
enormous for large
𝑑
. This would defeat the purpose of a memory-efficient algorithm.
5
The key insight is that since we are only interested in the fractional part of the sum, we can
perform all calculations modulo 1. For each term in the sum, of the form
𝑏
ௗି௞
/𝑚
௞,௝
(where
𝑚
௞,௝
=
𝑎 ⋅ 𝑘 + 𝑟
௝
), we only need its fractional part. The fractional part of a rational number
𝑁/𝑀
can be
found by computing
(𝑁 (mod 𝑀))/𝑀
. Applying this, the term becomes:
ቊ
𝑏
ௗି௞
𝑚
௞,௝
ቋ =
𝑏
ௗି௞
(mod 𝑚
௞,௝
)
𝑚
௞,௝
This transformation is profound. The computationally intensive part is now the modular
exponentiation
𝑏
ௗି௞
(mod 𝑚
௞,௝
)
. This can be calculated very efficiently using algorithms like the
binary method (square-and-multiply) or, as specified in the DHA thesis, the Montgomery Ladder.
Crucially, this entire operation can be performed using standard fixed-precision integer arithmetic
(e.g., 64-bit integers), as long as the intermediate products in the modular exponentiation do not
exceed the register size. This avoids the need for specialized BigNum libraries and is the reason
BBP-type algorithms are so efficient in terms of memory.1 The "Residue engine" is the hardware
or software module that implements this modular exponentiation.
The claim in the thesis of "no loops over x" is a nuanced one. It is true that there is no search loop
to find a value. However, the projector function itself contains a computational loop that iterates
from
𝑘 =0
to the truncation limit
𝐾
. The complexity of this loop is not dependent on the value of
the digits, but it is dependent on the address
𝑑
. The dominant operation inside the loop is the
modular exponentiation, which has a time complexity of
𝑂(log(𝑑 − 𝑘))
for an exponent of size
𝑑 −
𝑘
. Summing over the
𝐾 +1
terms, the total time complexity for a single projection is approximately----------- Page10 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 10
𝑂(𝐾 ⋅log𝑑)
. Since
𝐾
is determined by the required precision
𝑊
and is typically small relative to
𝑑
,
this complexity is very favorable compared to the
𝑂(𝑑
ଶ
)
or worse complexity of traversal-based
algorithms. The term "locked" in "locked projector" can be interpreted as signifying the fixed,
immutable nature of this computational process once the field parameters
(𝐹, 𝑏, 𝑊)
are defined. It
behaves like a mathematical constant function, mapping any valid address
𝑑
to a unique digit
sequence.
4.0 The Addressing Mechanism: From Seed to Deterministic Address
4.1 The Modulus
𝑀(𝐾)
: The Role of the Least Common Multiple (LCM)
The most significant architectural innovation presented in the DHA framework is its deterministic
addressing mechanism. This mechanism provides a direct, mathematical mapping from an
arbitrary input seed
𝑆
to a digit address
𝑑
. The centerpiece of this mapping is a large, composite
modulus,
𝑀(𝐾)
, defined as the Least Common Multiple (LCM) of all the linear denominators,
𝑚
௞,௝
= 𝑎 ⋅ 𝑘 + 𝑟
௝
, that appear in the truncated BBP sum for
𝑘
ranging from
0
to
𝐾
.
𝑀(𝐾)=
lcm
{𝑎 ⋅ 𝑘 + 𝑟
௝
∣0≤ 𝑘 ≤ 𝐾,1≤ 𝑗 ≤ 𝐽}
The choice of the LCM is not arbitrary; it is the mathematical linchpin that ensures the cyclic
behavior of the address space. The computation of the LCM for a sequence of integers is a non-
trivial task. It can be performed iteratively by applying the identity
lcm
(𝑥, 𝑦)=(|𝑥 ⋅ 𝑦|)/
gcd
(𝑥, 𝑦)
repeatedly for all numbers in the set.
19
The complexity of finding the GCD of two numbers
𝑎
and
𝑏
using the Euclidean algorithm is
𝑂(log(min(𝑎, 𝑏)))
.
20
Since the numbers in the set for
𝑀(𝐾)
go up
to approximately
𝑎 ⋅ 𝐾
, and the intermediate LCM value grows extremely rapidly, the overall
complexity of computing
𝑀(𝐾)
is significant.
20
More importantly, the magnitude of
𝑀(𝐾)
grows at a super-exponential rate with
𝐾
. The Prime
Number Theorem implies that the LCM of integers up to
𝑛
, denoted
𝜓(𝑛)
, is asymptotically equal
to
𝑒
௡
. Since the set of denominators includes numbers up to roughly
𝑎 ⋅ 𝐾
, the size of
𝑀(𝐾)
is on
the order of
𝑒
௔⋅௄
. This means that even for modest values of
𝐾
(e.g.,
𝐾 =100
),
𝑀(𝐾)
will be an
astronomically large number, far exceeding the capacity of standard 64-bit or 128-bit integer
types and necessitating the use of arbitrary-precision arithmetic (BigNum) libraries for its storage
and for any calculations involving it.
4.2 The Chinese Remainder Theorem (CRT) as the Unifying Principle
The thesis explicitly invokes the Chinese Remainder Theorem (CRT) as the justification for using
𝑀(𝐾)
as the modulus. The statement "Reducing
𝑑
modulo
𝑀(𝐾)
preserves all residues
simultaneously (CRT)" is the key to understanding the mechanism's correctness.----------- Page11 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 11
The CRT, in its classical form, states that a system of simultaneous congruences has a unique
solution modulo the product of the moduli, provided the moduli are pairwise coprime.
21
For
example, knowing
𝑥 (mod 3)
,
𝑥 (mod 5)
, and
𝑥 (mod 7)
allows one to uniquely determine
𝑥 (mod 105)
. The CRT is widely used in computer science to break down computations with large
numbers into parallel computations with smaller numbers.
21
DHA employs the underlying principle of the CRT in a slightly different, yet powerful, way. It relies
on a fundamental property of the Least Common Multiple. If an integer
𝑑
ᇱ
is congruent to
𝑑
modulo
𝑀(𝐾)
, i.e.,
𝑑
ᇱ
≡ 𝑑 (mod 𝑀(𝐾))
, it implies that
𝑑
ᇱ
− 𝑑
is a multiple of
𝑀(𝐾)
. Since
𝑀(𝐾)
is the
LCM of all the denominators
𝑚
௞,௝
, it means that
𝑀(𝐾)
is itself a multiple of every individual
𝑚
௞,௝
.
Therefore,
𝑑
ᇱ
− 𝑑
must also be a multiple of every
𝑚
௞,௝
, which in turn means that
𝑑
ᇱ
≡ 𝑑 (mod 𝑚
௞,௝
)
for all
𝑘, 𝑗
in the defining set.
This property is the guarantee of "CRT-safe addressing." The projector function computes terms
involving modular exponentiation, such as
𝑏
ௗି௞
(mod 𝑚
௞,௝
)
. The result of this exponentiation
depends on the exponent,
𝑑 − 𝑘
, modulo the order of the multiplicative group of integers modulo
𝑚
௞,௝
. By ensuring that any two addresses
𝑑
and
𝑑
ᇱ
that are congruent modulo
𝑀(𝐾)
are also
congruent modulo every individual denominator
𝑚
௞,௝
, the DHA framework guarantees that the
projector function will yield the exact same output for both
𝑑
and
𝑑
ᇱ
. This establishes that the
entire sequence of digits generated by the projector is periodic, with a period that divides
𝑀(𝐾)
.
The address space can be "folded" upon itself without affecting the output of the projector,
creating a finite, cyclic space of unique digit windows.
4.3 The Address Map:
𝑑 =(
REDUCE
(𝑆)) (mod 𝜆 ⋅ 𝑀(𝐾))
With the modulus
𝑀(𝐾)
established, the address map itself is remarkably simple. An input seed
𝑆
is first processed by an unspecified REDUCE function. This is likely a preliminary step to map an
arbitrary input (which could be a string or a very large number) into a standard integer format
suitable for modular arithmetic. A cryptographic hash function is a prime candidate for this role.
The core of the mapping is a single modular reduction: the reduced seed is taken modulo
𝜆 ⋅ 𝑀(𝐾)
to produce the final address
𝑑
. This operation is computationally trivial once the modulus is
known. It is a direct, non-iterative calculation that perfectly aligns with the thesis claim of "no
search, no curvature gating." The complexity lies not in the mapping operation itself, but in the
prior, one-time computation of the modulus.
4.4 The Role of the Coprime Stride
𝜆
The parameter
𝜆
is described as a "small coprime stride." It is an integer that shares no factors
with
𝑀(𝐾)
. Multiplying the core modulus
𝑀(𝐾)
by
𝜆
serves to expand the total address space. The
primary purpose of this stride is likely to improve the statistical properties of the mapping from
seeds to addresses. If seeds are sequential (e.g.,
𝑆, 𝑆 +1, 𝑆 +2,...
), reducing them modulo
𝑀(𝐾)----------- Page12 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 12
would result in sequential addresses. By using a larger modulus
𝜆 ⋅ 𝑀(𝐾)
and potentially
incorporating
𝜆
into the reduction function, the mapping can disperse sequential inputs more
effectively across the address space, preventing clustering and enhancing the pseudorandom
appearance of the addressed digit sequences.
To provide a clear reference for the system's components, the following table summarizes the key
parameters and their roles within the DHA architecture.
Table 2: Key Parameters of the DHA System
Parameter Description Role How
Determined
Dependency
𝐹
A mathematical
constant (e.g.,
𝜋
)
Information
Substrate
Chosen from
BBP
Compendium
8
-
𝑏
An integer
number base
(e.g., 16)
Number Base
for Digit
Extraction
Defined by the
BBP formula for
𝐹
5
𝐹
𝑊
Integer window
size
Precision of the
output
User-defined
parameter
-
𝐾
Truncation limit
for the BBP
series
Accuracy
Control
Derived from
𝑊
to bound tail
error
𝑊, 𝑏
𝑆
Input seed User Input /
Operator
Provided by the
user or a
process
------------ Page13 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 13
𝑚
௞,௝
Denominators
in the BBP sum
(e.g.,
8𝑘 + 1
)
Modular bases
for residue
calculation
Defined by the
BBP formula
𝐹
𝑀(𝐾)
LCM of all
𝑚
௞,௝
for
0 ≤ 𝑘 ≤ 𝐾
Primary
modulus for
address space
Derived from
the set of all
𝑚
௞,௝
𝐾, 𝐹
𝜆
Small integer
coprime to
𝑀(𝐾)
Stride for
address space
expansion
Chosen system
parameter
𝑀(𝐾)
𝑑
The final digit
address
Input to the
Projector
Function
Calculated:
REDUCE
(𝑆) (mod 𝜆
𝑀(𝐾))
𝑆, 𝜆, 𝑀(𝐾)
This table illustrates the chain of dependencies that flows from the user's choice of precision (
𝑊
)
through the truncation limit (
𝐾
) to the computationally demanding modulus
𝑀(𝐾)
, which in turn
defines the address space for the mapping from the seed
𝑆
to the final address
𝑑
.
5.0 Architectural and Implementation Framework
5.1 The Residue Engine: Montgomery Ladder
The thesis specifies a "Residue engine (Montgomery ladder)" as a core component of its
proposed hardware implementation. This choice is highly significant and points toward
applications where security and resistance to physical attacks are paramount. The "Residue
engine" is responsible for the most computationally intensive part of the projector function: the
modular exponentiation
𝑏
ௗି௞
(mod 𝑚
௞,௝
)
.
The Montgomery Ladder is an algorithm for computing modular exponentiation,
𝑔
௞
(mod 𝑁)
.
24
It
processes the bits of the exponent
𝑘
from left to right. Unlike the standard square-and-multiply
algorithm, which performs a different sequence of operations depending on whether the current
bit is a 0 or a 1, the Montgomery Ladder performs a fixed sequence of a multiplication and a
squaring in every single iteration, regardless of the exponent bit's value.
24
This operational regularity is its key advantage. Attacks on cryptographic hardware often rely on
measuring subtle variations in power consumption or timing to deduce the secret key being----------- Page14 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 14
processed. These are known as side-channel attacks (e.g., Simple Power Analysis or SPA).
Because the Montgomery Ladder's operational flow is independent of the secret data (the bits of
the exponent), it does not leak information through these side channels, making it inherently
resistant to SPA.
24
Furthermore, the Montgomery Ladder is well-suited for hardware implementation. The two
arithmetic operations within each loop iteration are independent and can be parallelized, which
can nearly double the performance on a device with two processing units.
24
This aligns perfectly
with the hardware sketch's mention of parallel modules. The choice of the Montgomery Ladder is
therefore not merely an implementation detail for efficiency; it is a deliberate architectural
decision that endows the DHA system with properties essential for high-assurance and
cryptographic applications.
5.2 CRT-Safe Addressing and the Comb Adder
The hardware sketch also specifies "CRT-safe addressing" and a "Comb adder."
CRT-Safe Addressing: This term refers to the hardware implementation of the address mapping
function,
𝑑 =
REDUCE
(𝑆) (mod 𝜆 ⋅ 𝑀(𝐾))
. As established, the modulus
𝑀(𝐾)
can be an extremely
large number. "CRT-safe addressing" therefore implies the existence of a dedicated arithmetic
logic unit (ALU) capable of performing modular arithmetic with this large, pre-computed modulus.
The "safety" comes from the guarantee provided by the Chinese Remainder Theorem that this
modular reduction correctly preserves the residues needed by the projector, thus ensuring the
cyclicity of the address space.
Comb Adder: The term "Comb adder" is likely a metaphorical reference to the final summation
step within the projector function. The BBP formula for a constant
𝐹
is a sum of
𝐽
rational terms.
The projector computes the contribution of each of these
𝐽
terms in parallel and then sums the
results. In digital signal processing, a comb filter adds a signal to delayed versions of itself. Here,
the "Comb adder" is the hardware block that takes the outputs from the
𝐽
parallel residue
calculation paths and combines them to produce the final fractional value from which the digits
are extracted.
5.3 Optional Seed Dispersion via Cryptographic Hashing
The thesis notes that the role of a Secure Hash Algorithm (SHA) is "optional, never necessary."
This component would act as the REDUCE function on the input seed
𝑆
before the final modular
mapping.
The purpose of applying a cryptographic hash function like SHA-256 is to improve the statistical
properties of the seed distribution.
27
If the input seeds
𝑆
are non-uniform—for example, if they are
sequential integers like 1, 2, 3,...—the resulting addresses
𝑑
might also exhibit undesirable patterns----------- Page15 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 15
or clustering within the address space. A cryptographic hash function acts as a strong pseudo-
random permutation. It takes an input and produces a fixed-size output that is computationally
indistinguishable from random noise. Hashing the seed,
𝐻(𝑆)
, before the modular reduction
effectively decorrelates the input sequence, ensuring that the resulting addresses are uniformly
distributed throughout the range
[0, 𝜆 ⋅ 𝑀(𝐾)−1]
.
29
This optionality creates two distinct operational modes for a DHA system.
1.
Transparent Mode (No Hash): The mapping from seed
𝑆
to address
𝑑
is a simple modular
reduction. This relationship is mathematically transparent and easily auditable. An observer
can reason algebraically about the relationship between inputs and outputs.
2.
Secure Mode (With Hash): The mapping from
𝑆
to
𝑑
is mediated by a one-way function.
The relationship is now computationally opaque; it is infeasible to predict the address for a
given seed without computing the hash, and impossible to reverse the process. This mode
provides superior statistical distribution at the cost of algebraic transparency.
The choice between these modes would depend on the specific application's requirements,
balancing the need for auditability against the need for unpredictability.
The following table maps the abstract components from the DHA thesis to their concrete
implementations and functions.
Table 3: Summary of Architectural Components and Functions
DHA Component Corresponding
Algorithm/Structur
e
Function in DHA Key Advantage
Residue Engine
Montgomery Ladder
Algorithm
24
Performs the
modular
exponentiation
𝑏
ௗି௞
(mod 𝑚
௞,௝
)
required by the
projector.
High efficiency in
hardware; inherent
resistance to simple
side-channel
attacks.
26----------- Page16 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 16
CRT-Safe
Addressing
Large-Modulus
Arithmetic Logic
Unit (ALU)
Implements the
address map
𝑑 =
REDUCE
(𝑆) (mod 𝜆 ⋅
𝑀(𝐾))
.
Guarantees the
cyclic property of
the address space,
as justified by the
CRT.
21
Seed Dispersion
Cryptographic Hash
Function (e.g., SHA-
256)
27
Pre-processes the
input seed
𝑆
to
ensure uniform
address distribution.
Decorrelates input
seeds, preventing
clustering and
improving statistical
randomness.
29
Tail Bound Unit Numerical Error
Bound Analysis
Determines the
series truncation
limit
𝐾
based on the
desired precision
𝑊
.
Ensures the
accuracy of the
extracted digits by
bounding the
truncation error.
5
Comb Adder Parallel Summation
Circuit
Sums the outputs of
the parallel BBP
term computations
to get the final
result.
Enables parallel
computation of the
BBP series
components for
improved
performance.
This architectural blueprint reveals a system designed for high performance and security,
grounding the abstract claims of the thesis in well-established principles of cryptographic
hardware design and computational number theory.
6.0 System Dynamics and Scheduling
6.1 The Golden Angle (
𝜙
) as a Low-Discrepancy Address Scheduling Law
The thesis introduces the golden ratio,
𝜙 =(1+
√
5)/2
, as a "spacing law for scheduling
addresses." This indicates that the DHA system is conceptualized not merely for single, isolated
lookups but as an engine for generating sequences of addresses and their corresponding digits.
The reference to
𝜙
points directly to the field of quasi-random sequences, also known as low-
discrepancy sequences.
31----------- Page17 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 17
Unlike pseudo-random numbers, which aim to mimic the statistical properties of true randomness,
quasi-random sequences are designed to fill a space as evenly and uniformly as possible.32 They
are deterministic and, by avoiding clustering and gaps, often lead to faster convergence in
numerical methods like quasi-Monte Carlo integration.31 The canonical one-dimensional low-
discrepancy sequence is the van der Corput sequence, and a closely related and simpler-to-
generate sequence is based on the golden ratio:
𝑥
௡
={𝑛 ⋅ 𝜙}
where
𝑛 =1,2,3,...
and
{⋅}
denotes the fractional part. This sequence populates the interval
[0,1)
in
a maximally uniform way; each new point is placed in the largest existing gap.32
Within the DHA framework, this principle can be used to generate a sequence of input seeds, for
example, by setting
𝑆
௡
=⌊𝑛 ⋅ 𝜙 ⋅ 𝐶⌋
for some scaling constant
𝐶
. The resulting sequence of
addresses,
𝑑
௡
, would then be well-distributed throughout the entire address space defined by
𝑀(𝐾)
. This provides a deterministic and structured method for "sampling" the digits of the
underlying constant
𝐹
, ensuring comprehensive coverage rather than random, clustered probing.
This is particularly valuable for applications in simulation or data analysis where uniform sampling
of the information field is desired.
6.2 The Constant e as a Continuous Growth Gauge
The thesis describes the mathematical constant
𝑒 ≈2.71828
as a "continuous growth gauge for
resource pacing." This connects the DHA system to the mathematics of exponential growth and
continuous processes. The constant
𝑒
is the base of the natural logarithm and arises
fundamentally from any situation involving continuous compounding or growth, where the rate of
change of a quantity is proportional to the quantity itself.
35
In a computational or resource management context, this suggests a model for controlling the
rate of operations over time. For example, the rate at which a DHA system generates new
addresses or the computational budget allocated to it could be modeled by an exponential
function,
𝑅(𝑡)= 𝑅
଴
𝑒
௞௧
. This allows for:
●
Resource Pacing: A system could be designed to start slowly and exponentially increase its
rate of data generation, or conversely, to decay its activity over time. This is critical for
systems that need to adapt to changing loads, manage power consumption, or pace their
output to match the capacity of a downstream consumer.
37
●
Optimal Planning: The constant
𝑒
also appears in optimal planning problems. A classic
example is the "secretary problem" or problems of optimal stopping. The presence of
𝑒
in the----------- Page18 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 18
DHA stack suggests its use in strategies for deciding when to perform a lookup, perhaps to
maximize the probability of finding a sequence with certain properties within a given time
budget.
The inclusion of both
𝜙
and
𝑒
in the conceptual stack implies a sophisticated vision for DHA as a
dynamic system. It is not just a static lookup table. Instead, it is a generative framework where
𝜙
governs the spatial distribution of queries (which addresses to sample), and
𝑒
governs the
temporal distribution of those queries (when to perform the sampling). This allows the system to
be controlled with a high degree of mathematical precision, producing outputs that are structured
in both space (the address domain) and time.
This dual-control mechanism offers a powerful tuning capability. An application could use a
𝜙
-
based seed schedule to generate a sequence of digits that are uniformly sampled from the
constant
𝐹
. Alternatively, it could use a cryptographically secure pseudo-random number
generator (CSPRNG) to generate seeds, resulting in a sequence of digits that are pseudo-
randomly sampled. The former provides structured, even coverage, while the latter provides
statistical randomness in the sampling pattern itself, layered on top of the statistical randomness
of the BBP digits. DHA thus becomes a versatile engine capable of generating deterministic,
verifiable data streams with finely-tuned statistical properties tailored to the needs of the
application.
7.0 Critical Analysis: Stated Benefits and Inherent Limitations
7.1 Evaluating "Truthfulness" and "Zero Traversal"
The DHA framework claims several key benefits, most notably "Truthfulness" and "Zero traversal."
A critical examination reveals these claims to be largely valid, but with important caveats.
Truthfulness: This concept appears to refer to the deterministic and mathematically rigorous
nature of the DHA process. For a given set of public parameters (the constant
𝐹
, base
𝑏
, and the
BBP formula), the mapping from an input seed
𝑆
to an output digit sequence is unalterable and
verifiable. The output is a "true" property of the underlying constant, not an artifact of a
stochastic or heuristic process. This property is powerful for applications requiring auditability
and non-repudiation. For instance, in a system based on DHA, one can provide a seed
𝑆
and a
digit sequence and allow any third party to independently verify that the sequence is the correct
output for that seed. This is a form of computational integrity that is difficult to achieve with
conventional pseudo-random generators.
Zero Traversal: This claim is central to the efficiency of DHA. It is true that, during the lookup
phase, the system does not need to compute or iterate through the digits from 1 to
𝑑 −1
to
access the digit at position
𝑑
.
16
This is a direct inheritance from the properties of BBP-type----------- Page19 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 19
algorithms. However, this claim must be qualified. It completely elides the significant, one-time
pre-computation cost required to establish the system, specifically the calculation of the modulus
𝑀(𝐾)
. Furthermore, while there is no traversal loop over the digits, the projector function itself
contains a computational loop that runs from
𝑘 =0
to
𝐾
, and the complexity of each iteration
within that loop is logarithmically dependent on the address
𝑑
. Therefore, "Zero traversal" applies
accurately to the digit space but can obscure the computational reality of both the setup and the
lookup procedures.
7.2 Constraint Analysis: The Universe of BBP-Type Constants
A fundamental and severe limitation of the DHA architecture is its reliance on the existence of a
BBP-type formula for its information field. The mechanism is intrinsically tied to this specific
mathematical structure. This has two major consequences:
1.
Limited Applicability: The set of constants for which BBP-type formulas are known is a
small, esoteric subset of all mathematical constants.
5
Many important constants, such as
Euler's constant
𝛾
or constants for which no such formula has been discovered, cannot be
used as a DHA field.
2.
Non-Systematic Discovery: There is no known systematic algorithm for finding a BBP-type
formula for an arbitrary constant
𝛼
in a given base
𝑏
.
6
The known formulas have been
discovered through a combination of brilliant insight and extensive computational searches
using integer relation algorithms.
40
This means that the set of available DHA fields cannot be
expanded on demand. An organization cannot simply decide to build a DHA system based on
their constant of choice; they are restricted to the existing, known compendium.
7.3 Computational Complexity: The
𝑀(𝐾)
Bottleneck
The single greatest practical impediment to the widespread implementation of DHA is the
computational complexity and sheer magnitude of the addressing modulus,
𝑀(𝐾)
. This parameter
is the Achilles' heel of the entire architecture.
As previously discussed,
𝑀(𝐾)
is the LCM of all denominators in the BBP sum up to a truncation
limit
𝐾
. The value of
𝐾
is determined by the desired output precision
𝑊
. The size of
𝑀(𝐾)
grows
super-exponentially with
𝐾
. To illustrate, consider the BBP formula for
𝜋
. The denominators are of
the form
8𝑘 + 𝑟
. If a modest precision requires, say,
𝐾 =1000
, the largest denominator would be
around 8000. The LCM of all integers up to
𝑛
is approximately
𝑒
௡
. Therefore,
𝑀(1000)
would be a
number with thousands of decimal digits.
This has two devastating practical effects:
1.
Pre-computation Cost: The one-time cost of calculating this enormous number is
formidable. It would require significant computational resources and specialized arbitrary-
precision arithmetic software.----------- Page20 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 20
2.
Operational Cost: The address mapping,
𝑑 =
REDUCE
(𝑆) (mod 𝜆 ⋅ 𝑀(𝐾))
, requires
performing modular arithmetic with this massive number. While the BBP projector cleverly
avoids multi-precision arithmetic, the DHA addressing stage re-introduces it at the front end.
This undermines one of the key practical advantages of the BBP algorithm.
The economics of a DHA system are therefore dominated by this trade-off. The extremely high,
fixed setup cost of computing and storing
𝑀(𝐾)
must be amortized over a very large number of
lookups. This makes DHA unsuitable for general-purpose computation or applications with
changing parameters. It is only economically viable in highly specialized scenarios, such as a
hardware-implemented system (akin to a ROM) where the field is fixed for the lifetime of the
device and the number of expected lookups is astronomical.
7.4 Base Dependency and Numerical Precision
Finally, two further limitations inherited from the BBP foundation deserve mention.
Base Dependency: As analyzed in Section 2.3, the output of the DHA projector is locked to the
base
𝑏
of the underlying BBP formula.
5
For the most famous constant,
𝜋
, this means the output is
in hexadecimal, not decimal. This restricts the direct applicability of the system for many common
use cases.
Numerical Precision: While the use of modular arithmetic is elegant, the system is not immune to
numerical precision issues. The reliance on fixed-precision (e.g., 64-bit) integer arithmetic means
there is a limit to the size of the denominators
𝑚
௞,௝
that can be handled. More importantly, the risk
of a carry-propagation error due to the truncation of the infinite series remains a concern that
requires careful error analysis and potentially higher-precision intermediate calculations to
mitigate, especially when a very high-fidelity output is required.
5
8.0 The 'Nexus' Conceptual Model
8.1 Interpreting "Operator, Weave, Echo, Glyph"
The thesis concludes by aligning the DHA framework with a conceptual model called 'Nexus',
described through a set of four metaphorical terms: "Operator, Weave, Echo, Glyph." This
terminology appears to be an abstract, qualitative layer designed to capture the system's
information-theoretic essence.
●
Operator: This clearly refers to the input seed,
𝑆
. As established in the core thesis, the input
is not a passive query but an active operator that acts upon the system to produce a result. It
is the prime mover in the DHA process.----------- Page21 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 21
●
Weave: This metaphor aptly describes the underlying BBP-type constant,
𝐹
. The sequence
of its digits is an infinitely intricate, complex pattern. While conjectured to be statistically
random (normal), it is also perfectly deterministic and interwoven with deep mathematical
structure. "Weave" captures this dual nature of complexity and order.
●
Echo: This term represents the action of the locked projector,
𝑃
ி
. The projector can be seen
as "pinging" the weave at a specific address
𝑑
. The result—the sequence of digits at that
location—is the "echo" that returns. It is a reflection of the weave's local structure at the
point specified by the operator.
●
Glyph: This refers to the final output: the small, finite window of digits extracted by the
projector. A glyph is a symbolic figure or character. The output digits are a compact,
symbolic representation—a meaningful piece of information—extracted from the seemingly
endless and chaotic weave of the constant.
8.2 Synthesizing a Coherent Model
The term "Nexus" itself provides a powerful organizing concept for the entire architecture. In
modern computer science and software engineering, a Nexus is often a framework or platform
designed to connect and manage the interactions between multiple, disparate components or
teams, especially in the context of scaling complex systems.
42
The Nexus framework for Scrum,
for example, helps coordinate multiple development teams working on a single product by
managing their dependencies and integration points.
42
In the context of DHA, "Nexus" can be understood as the overarching framework that integrates
the distinct mathematical and computational components into a cohesive whole. It is the
architectural nexus that connects:
●
The input space of seeds (
𝑆
).
●
The addressing logic (modular reduction, CRT, LCM).
●
The information substrate (the BBP constant, the "weave").
●
The projection engine (the locked projector, the "echo").
●
The output space of digits (the "glyphs").
The DHA Nexus acts as a bridge between the realms of deterministic, discrete user input and the
complex, pseudo-random, continuous nature of a transcendental number. It provides the
managed interface and the mathematical guarantees that allow these two disparate worlds to
interact in a predictable and verifiable way. The conceptual model of Operator
→
Weave
→
Echo
→
Glyph describes the flow of information through this nexus, from a simple input command to
the extraction of a profound and symbolic piece of mathematical truth. This abstract layer, while
not technical, provides a valuable and insightful way to reason about the system's purpose and
function as a whole.----------- Page22 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 22
9.0 Conclusion and Potential Research Avenues
9.1 Summary of Findings
Deterministic Harmonic Addressing (DHA) presents a novel and mathematically coherent
architecture for direct, non-iterative access to the digit expansions of a specific class of
mathematical constants. The analysis confirms that its two-stage design—a deterministic
addressing mechanism followed by a BBP-type projection—is theoretically sound. The core
innovation lies in the addressing scheme, which uses the Least Common Multiple of the BBP
denominators to define a cyclic address space, with the Chinese Remainder Theorem providing
the mathematical guarantee for its correctness. This enables a verifiable, one-to-one mapping
from an input seed to an output digit sequence, achieving the stated goals of "truthfulness" and
"zero traversal" during the lookup phase.
However, the practical implementation of DHA faces a formidable obstacle in the pre-
computation and operational use of the addressing modulus,
𝑀(𝐾)
. This value's super-
exponential growth with required precision represents a significant setup cost, confining the
system's viability to "bake-once, read-many" scenarios. Further limitations are inherited from its
BBP foundation, namely the restriction to a small class of constants and the base-dependency of
the output. The proposed hardware architecture, particularly the specification of a Montgomery
Ladder, strongly suggests an intended application in security-sensitive domains where side-
channel resistance is a primary concern.
9.2 Viable Applications
Despite its limitations, the unique properties of the DHA framework make it a compelling
candidate for several specialized applications:
●
Cryptography: DHA could serve as a highly structured Deterministic Random Bit Generator
(DRBG). It could be used to generate keys, nonces, or initialization vectors from a master
seed in a manner that is both computationally reproducible and verifiable by third parties. Its
side-channel resistant design makes it suitable for implementation in secure hardware like
smart cards or hardware security modules (HSMs).
●
Scientific Simulation: In fields that rely on quasi-Monte Carlo methods, DHA could provide a
deterministic and highly uniform source of sampling points. By using a
𝜙
-based seed
scheduling law, it can generate well-distributed, low-discrepancy sequences that are
perfectly reproducible across different machines and simulation runs, eliminating a key
source of variance in stochastic modeling.
●
Verifiable Data Generation and "Stateless" Storage: DHA offers a method for generating
vast, complex datasets from a small set of initial parameters. Any portion of the dataset can
be regenerated on-demand from a seed without storing the entire dataset. This is useful for----------- Page23 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 23
benchmarking, testing, or even as a form of "proof-of-work" in decentralized systems, where
participants must prove they have access to specific data that can be verified efficiently.
9.3 Future Research Avenues
The analysis of the DHA framework points to several promising avenues for future research that
could address its primary limitations and expand its potential.
●
The
𝑀(𝐾)
Problem: The most critical area for research is mitigating the bottleneck
associated with the modulus
𝑀(𝐾)
. This could involve:
○
Developing highly optimized algorithms specifically for computing the LCM of the
arithmetic progressions found in BBP denominators.
○
Investigating alternative addressing schemes that might achieve cyclicity without relying
on a single, monolithic modulus. This could perhaps involve hierarchical or multi-stage
modular mappings.
●
Expanding the Field: The utility of DHA is directly proportional to the number of known BBP-
type constants. Continued experimental searches with integer relation algorithms like PSLQ
for new formulas could uncover representations for other important constants or for existing
constants in more useful bases (especially base 10).
●
Formal Security Analysis: A rigorous cryptographic analysis of the digit sequences
produced by DHA is needed. While the underlying constants are conjectured to be normal, a
formal proof of the statistical properties of sequences sampled via different seed scheduling
schemes (e.g., linear congruential,
𝜙
-based, or hash-based) would be necessary to certify
DHA for use in high-security cryptographic applications.
●
Exploring Alternative Projectors: The DHA addressing concept—mapping a seed to an
address within a sequence—is powerful. Research could explore whether this deterministic
addressing front-end could be coupled with other types of digit-extraction algorithms that
are not strictly of the BBP type, potentially broadening the class of constants that could be
incorporated into such a framework.
Works cited
1.
Spigot algorithm - Wikipedia, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Spigot_algorithm
2.
Spigot Algorithm -- from Wolfram MathWorld, accessed August 17, 2025,
https://mathworld.wolfram.com/SpigotAlgorithm.html
3.
A Spigot Algorithm for the Digits of Pi, accessed August 17, 2025,
https://www.cs.williams.edu/~heeringa/classes/cs135/s15/readings/spigot.pdf
4.
en.wikipedia.org, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_for----------- Page24 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 24
mula#:~:text=The%20BBP%20formula%20gives%20rise,i.e.%2C%20in%20base%
2010).
5.
Bailey–Borwein–Plouffe formula - Wikipedia, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_for
mula
6.
Direct Dial to
𝜋
: The Formula That Changed Our Approach to Calculating Pi's
Elusive Digits | by Sam Vaseghi | Intuition | Medium, accessed August 17, 2025,
https://medium.com/intuition/direct-dial-to-the-formula-that-changed-our-
approach-to-calculating-pis-elusive-digits-003447a5becc
7.
algorithms - Intuitive explanation of Bailey-Borwein-Plouffe $\pi ..., accessed
August 17, 2025, https://math.stackexchange.com/questions/317124/intuitive-
explanation-of-bailey-borwein-plouffe-pi-extraction-formula
8.
A Compendium of BBP-Type Formulas for Mathematical Constants -
ResearchGate, accessed August 17, 2025,
https://www.researchgate.net/publication/2316901_A_Compendium_of_BBP-
Type_Formulas_for_Mathematical_Constants
9.
A Compendium of BBP-Type Formulas for Mathematical ... - CiteSeerX, accessed
August 17, 2025,
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=69a047cc1dd
f1631f0f65a936d04cfe2765904c2
10.
BBP-Type Formula -- from Wolfram MathWorld, accessed August 17, 2025,
https://mathworld.wolfram.com/BBP-TypeFormula.html
11.
How the heck does the Bailey-Borwein-Plouffe formula compute the nth digit of
pi? Is there a relatively concise explanation anywhere? : r/math - Reddit, accessed
August 17, 2025,
https://www.reddit.com/r/math/comments/3kbuyg/how_the_heck_does_the_bail
eyborweinplouffe/
12.
BBP Formula -- from Wolfram MathWorld, accessed August 17, 2025,
https://mathworld.wolfram.com/BBPFormula.html
13.
A Compendium of BBP-Type Formulas For Mathematical Constants | PDF -
Scribd, accessed August 17, 2025,
https://www.scribd.com/document/462960684/bbp-formulas
14.
3.5 Unpacking the BBP Formula for Pi - CARMA, accessed August 17, 2025,
https://carmamaths.org/jon/Preprints/Books/Other/bbp.pdf----------- Page25 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 25
15.
Computing the nth digit of π directly - Applied Mathematics Consulting,
accessed August 17, 2025, https://www.johndcook.com/blog/2025/03/14/bbp/
16.
A Compendium of BBP-Type Formulas for Mathematical Constants - David H
Bailey, accessed August 17, 2025,
https://www.davidhbailey.com/dhbpapers/bbp-formulas.pdf
17.
A class of digit extraction BBP-type formulas in general binary bases 1
Introduction, accessed August 17, 2025, https://nntdm.net/papers/nntdm-
17/NNTDM-17-4-18-32.pdf
18.
Can some one explain the BBP formula or spigot digit extraction like I'm 5? What
about like I'm a 29 year old with a decent understanding of math? - Reddit,
accessed August 17, 2025,
https://www.reddit.com/r/math/comments/14azhv/can_some_one_explain_the_b
bp_formula_or_spigot/
19.
Is there a simple way to determine least common multiple of an arbitrary number
of integers?, accessed August 17, 2025,
https://www.reddit.com/r/learnprogramming/comments/sw0ngy/is_there_a_sim
ple_way_to_determine_least_common/
20.
algorithms - Least common multiple of a list of numbers - Computer ..., accessed
August 17, 2025, https://cs.stackexchange.com/questions/107254/least-
common-multiple-of-a-list-of-numbers
21.
Chinese remainder theorem - Wikipedia, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Chinese_remainder_theorem
22.
en.wikipedia.org, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Chinese_remainder_theorem#:~:text=The%20Chine
se%20remainder%20theorem%20is,similar%20computations%20on%20small%2
0integers.
23.
The Chinese Remainder Theorem - Governors State University, accessed August
17, 2025,
https://opus.govst.edu/cgi/viewcontent.cgi?article=1000&context=capstones_m
ath
24.
The Montgomery Powering Ladder, accessed August 17, 2025,
https://cr.yp.to/bib/2003/joye-ladder.pdf
25.
Simple explanation of Montgomery ladder : r/crypto - Reddit, accessed August
17, 2025,----------- Page26 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 26
https://www.reddit.com/r/crypto/comments/fmbfd9/simple_explanation_of_mon
tgomery_ladder/
26.
(PDF) An efficient implementation of Montgomery Powering Ladder ..., accessed
August 17, 2025,
https://www.researchgate.net/publication/220850945_An_efficient_implementat
ion_of_Montgomery_Powering_Ladder_in_reconfigurable_hardware
27.
cryptographic hashing algorithm: Topics by Science.gov, accessed August 17,
2025,
https://www.science.gov/topicpages/c/cryptographic+hashing+algorithm.html
28.
Balancing security and efficiency in deterministic random bit generators for post-
quantum cryptography - CEUR-WS.org, accessed August 17, 2025, https://ceur-
ws.org/Vol-3925/short01.pdf
29.
Can we use a Cryptographic hash function to generate infinite random
numbers?, accessed August 17, 2025,
https://crypto.stackexchange.com/questions/76382/can-we-use-a-
cryptographic-hash-function-to-generate-infinite-random-numbers
30.
Hashing, Randomness and Dictionaries - CiteSeerX, accessed August 17, 2025,
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=ab38f38378a7
29940ffb87ba3b7d11209d76d096
31.
Golden Ratio Sequences for Low-Discrepancy Sampling - Computer Graphics
and Multimedia - RWTH Aachen, accessed August 17, 2025,
https://www.graphics.rwth-aachen.de/publication/032/
32.
Low-discrepancy sequence - Wikipedia, accessed August 17, 2025,
https://en.wikipedia.org/wiki/Low-discrepancy_sequence
33.
Quasi-random initial population for genetic algorithms | Request PDF -
ResearchGate, accessed August 17, 2025,
https://www.researchgate.net/publication/250728841_Quasi-
random_initial_population_for_genetic_algorithms
34.
Quasirandom sequences - Grant Slatton, accessed August 17, 2025,
https://grantslatton.com/quasirandom
35.
e (mathematical constant) - Wikipedia, accessed August 17, 2025,
https://en.wikipedia.org/wiki/E_(mathematical_constant)----------- Page27 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Page | 27
36.
Mathematical Peace: Exploring the Role of Euler's Number in Global Strategy and
Cooperation - Science Publishing Group, accessed August 17, 2025,
https://www.sciencepublishinggroup.com/article/10.11648/j.ajam.20251301.17
37.
US5982771A - Controlling bandwidth allocation using a pace counter - Google
Patents, accessed August 17, 2025,
https://patents.google.com/patent/US5982771A/en
38.
Robust Budget Pacing with a Single Sample - arXiv, accessed August 17, 2025,
https://arxiv.org/pdf/2302.02006
39.
Euler Found the First Binary Digit Extraction Formula for π in 1779 - Scholarly
Commons, accessed August 17, 2025,
https://scholarlycommons.pacific.edu/cgi/viewcontent.cgi?article=1049&context
=euleriana
40.
A class of digit extraction BBP-type formulas in general binary bases -
ResearchGate, accessed August 17, 2025,
https://www.researchgate.net/publication/266354182_A_class_of_digit_extractio
n_BBP-type_formulas_in_general_binary_bases
41.
Bailey–Borwein–Plouffe formula implementation in C++? - Stack Overflow,
accessed August 17, 2025, https://stackoverflow.com/questions/7265697/bailey-
borwein-plouffe-formula-implementation-in-c
42.
The Nexus Framework For Scaling Scrum In Software Development - DevCom,
accessed August 17, 2025, https://devcom.com/blog/nexus-framework-for-
scaling-scrum/
43.
The Nexus™ Guide - Scrum.org, accessed August 17, 2025,
https://www.scrum.org/resources/nexus-guide
44.
Nexus: A Lightweight and Scalable Multi-Agent Framework for Complex Tasks
Automation, accessed August 17, 2025,
https://www.researchgate.net/publication/389391888_Nexus_A_Lightweight_and
_Scalable_Multi-Agent_Framework_for_Complex_Tasks_Automation
45.
The Nexus Approach to Integrating Multithreading and Communication -
CiteSeerX, accessed August 17, 2025,
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=21683362bbc
ac9620bc5238ee42378f4022db9ac
46.
Nexus: Roles, team structure and events - FutureLearn, accessed August 17,
2025, https://www.futurelearn.com/info/courses/scaling-agile/0/steps/332265
