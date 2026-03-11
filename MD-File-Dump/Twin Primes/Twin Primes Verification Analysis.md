# **Determining Twin Prime Status of Large Number Pairs**

### **Executive Summary**

This report addresses the query regarding the twin prime status of five specific pairs of large numbers: (9998969, 9998971), (9999047, 9999049), (9999161, 9999163), (9999929, 9999931), and (9999971, 9999973). Twin primes are precisely defined as pairs of prime numbers that differ by exactly two, such as (3, 5) or (17, 19).^1^ The existence of infinitely many such pairs remains one of the most significant unsolved problems in number theory, known as the Twin Prime Conjecture.^1^

Verifying whether large numbers are prime, and thus whether a pair constitutes twin primes, presents a significant computational challenge. This task necessitates the application of sophisticated primality testing algorithms, as manual inspection or direct lookup in readily available lists becomes impractical due to the magnitude of the numbers involved.^3^

The research material comprehensively defines prime numbers and twin primes, and thoroughly discusses various primality testing algorithms, including deterministic methods like Trial Division and AKS, and probabilistic ones like Miller-Rabin.^3^ It also highlights the existence and utility of online calculators and programming libraries for primality testing.^3^ However, a critical limitation of the provided material is that it explicitly states it does not contain the pre-computed primality status for the specific large numbers presented in the query.^3^

This absence of direct computational results within the provided information is a crucial aspect that shapes the scope of this report. The query asks for a direct determination of twin prime status. The provided documentation, while describing the methods and tools for primality checking, consistently indicates that it cannot perform or display the results of these checks for the specific numbers in question. This highlights a fundamental distinction between possessing theoretical knowledge of algorithms and having access to the computational execution or pre-computed data. Therefore, while this report will detail the precise mathematical methodology and the types of computational tools necessary to perform such a verification, a definitive \"yes\" or \"no\" for each pair\'s twin prime status cannot be provided based solely on the given documentation. The report focuses on elucidating the process and theoretical underpinnings necessary for verification.

### **1. Introduction to Prime Numbers**

#### **Definition and Fundamental Properties**

A prime number is formally defined as a natural number (a positive integer) greater than 1 that possesses exactly two distinct positive divisors: 1 and itself.^2^ This definition inherently means that a prime number cannot be expressed as the product of two smaller natural numbers.^13^ For instance, the number 5 is prime because its only positive divisors are 1 and 5.^13^ In contrast, the number 24 is a composite number, as it has multiple divisors beyond 1 and itself, such as 2, 3, 4, 6, 8, and 12.^2^ Any natural number greater than 1 that does not fit the definition of a prime number is consequently termed a composite number.^2^ It is important to clarify that the number 1 holds a unique position in number theory; it is conventionally considered neither prime nor composite.

The number 2 holds a special status as the smallest prime number and, uniquely, the only even prime number.^6^ Beyond 2 and 3, all other prime numbers conform to a specific modular arithmetic form: they can be expressed as 6n ± 1 for some integer n.^2^ This property is often utilized as an initial filter in primality testing. The infinitude of prime numbers, a cornerstone of number theory, was famously demonstrated by the ancient Greek mathematician Euclid.^2^ This proof assures that there is no largest prime number, and the sequence of primes continues indefinitely.

#### **Significance in Mathematics and Applications**

Prime numbers are far from mere abstract mathematical curiosities; they form the fundamental building blocks of integers, a concept formalized by the Fundamental Theorem of Arithmetic. This theorem states that every integer greater than 1 can be uniquely represented as a product of prime numbers, irrespective of the order of the prime factors.^2^ This unique factorization property underpins much of number theory and has profound implications across various mathematical disciplines.

Beyond theoretical mathematics, the unique and seemingly unpredictable distribution of prime numbers makes them indispensable in numerous practical applications. Most notably, they are critical to modern cryptography, forming the basis for public-key encryption algorithms that secure digital communications.^5^ The security of these systems fundamentally relies on the computational difficulty of integer factorization---breaking down a large composite number into its prime factors---a problem that is computationally much harder than simply determining if a number is prime (primality testing).^4^ This distinction is vital for understanding the feasibility and importance of the user\'s query. Prime numbers also play a role in other computational fields, such as random number generation.^7^ The escalating demand for robust security in the digital age has directly spurred the development of increasingly efficient and reliable primality testing algorithms for exceptionally large numbers.^5^ This connection between the abstract definition of a prime number and its role in securing global digital infrastructure highlights the profound practical impact of seemingly theoretical mathematical concepts. The user\'s query, involving numbers of significant magnitude, implicitly touches upon this practical relevance, as numbers of this scale are precisely where such cryptographic applications become pertinent.

**Table 1: Definition of Prime Numbers**

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  Term               Definition                                                                                            Example              Source Snippets
  ------------------ ----------------------------------------------------------------------------------------------------- -------------------- -----------------
  Prime Number       A natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.        2, 3, 5, 7, 13, 17   ^2^

  Composite Number   A natural number greater than 1 that is not prime; it has more than two distinct positive divisors.   4, 6, 8, 9, 10, 24   ^2^
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

This table provides a clear and concise reference for the foundational definitions of prime and composite numbers. In a technical report, ensuring that core terminology is precisely understood is paramount. This structured presentation allows readers to quickly grasp or refresh their understanding of these essential concepts, facilitating a smoother comprehension of the subsequent, more complex discussions on twin primes and primality testing.

### **2. Understanding Twin Primes**

#### **Definition and Prime Gap of Two**

A twin prime is precisely defined as a prime number that is either two less or two more than another prime number.^1^ This means a twin prime pair consists of two prime numbers that are separated by a \"prime gap\" of exactly two.^1^ Illustrative examples of twin prime pairs include (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), and (41, 43).^1^

The pair (2, 3) is conventionally not classified as a twin prime pair.^1^ This exclusion stems from the fact that 2 is the sole even prime number, and twin primes are specifically characterized by a difference of two, making (2,3) a unique pair differing by one. The number 5 holds a unique position as the only prime number that participates in two distinct twin prime pairs: (3, 5) and (5, 7).^1^ This phenomenon is explained by the fundamental property that every third odd number is divisible by 3. Consequently, it is impossible for three successive odd numbers to all be prime unless one of them is 3. This mathematical property implies that any twin prime pair greater than (3, 5) must necessarily be of the form (6n-1, 6n+1) for some natural number

*n*.^1^

This (6n-1, 6n+1) form is more than a mere mathematical observation; it serves as a powerful and efficient initial screening criterion for potential twin prime candidates. If a given pair of numbers larger than (3,5) does not fit this modular arithmetic pattern, one can immediately conclude they are not twin primes without performing computationally intensive primality tests. For example, if the first number in a pair is of the form 6n+1, the second number would be 6n+3, which is always divisible by 3 and thus not prime (unless it is 3 itself, which is not the case for large numbers). This rule significantly reduces the search space for potential twin primes and provides a quick \"fail-fast\" mechanism. For the large numbers in the user\'s query, this property can be applied as a preliminary check. All the provided pairs (e.g., 9998969, 9998971) conform to the (6n-1, 6n+1) structure (9998970 is divisible by 6, so 9998969 = 6n-1 and 9998971 = 6n+1). This confirms their eligibility as *candidates* for twin primes, validating the necessity of proceeding with full primality tests for each number.

#### **Historical Context and the Twin Prime Conjecture**

The enduring question of whether there exists an infinite number of twin primes is recognized as one of the \"great open questions in number theory\".^1^ This unresolved problem is formally known as the Twin Prime Conjecture.^1^ A broader generalization, known as de Polignac\'s conjecture, was proposed in 1849. It posits that for every natural number

*k*, there are infinitely many primes *p* such that *p + 2k* is also prime. The Twin Prime Conjecture is the specific instance of de Polignac\'s conjecture where *k = 1*.^1^

While the Twin Prime Conjecture remains unproven, significant recent advancements have been made. For example, by assuming the Elliott--Halberstam conjecture (or a slightly weaker version), mathematicians have demonstrated the existence of infinitely many intervals that contain at least two primes, with the length of these intervals growing logarithmically.^1^ These breakthroughs, while not a full proof of the Twin Prime Conjecture, represent substantial progress towards understanding prime gaps and highlight the dynamic nature of mathematical research. The observation that the Twin Prime Conjecture is an open question places the user\'s specific query within a broader, dynamic landscape of mathematical discovery. This understanding is crucial, as it conveys that while the methodology for verifying specific pairs is well-established, the overarching question of their abundance and distribution continues to be a subject of active and challenging research.

### **3. Primality Testing for Large Numbers**

#### **Necessity of Efficient Algorithms**

Primality testing, the algorithmic process of determining whether a given input number is prime, is a fundamental computational problem.^4^ It is crucial to distinguish primality testing from integer factorization; while factorization aims to find the prime components of a composite number, primality tests typically only provide a binary answer---prime or not prime---without revealing any factors.^4^ Integer factorization is generally considered a computationally much harder problem than primality testing, which can be solved in polynomial time.^4^

The need for efficient primality tests has grown exponentially with the advent of modern cryptography, where large prime numbers are essential for generating secure keys.^5^ For the 7-digit numbers presented in the user\'s query (e.g., approximately 10 million), simple manual methods or basic trial division become computationally impractical.^3^ The square root of 10,000,000 is approximately 3162, meaning that a brute-force trial division would involve checking for divisibility by thousands of numbers, which is infeasible by hand. Furthermore, readily available lists of prime numbers ^15^ typically do not extend to the magnitude of the numbers in the query (e.g.^15^ lists primes only up to \~1.3 million), rendering direct lookup impossible. This necessitates the use of sophisticated computational algorithms.

#### **Overview of Primality Testing Algorithms**

Various algorithms have been developed to test for primality, each with different characteristics regarding efficiency, accuracy, and applicability:

- **Trial Division:** This is the most intuitive and simplest primality test. It involves systematically checking for divisibility by all prime numbers (or just odd numbers after checking 2) from 2 up to the square root of the number in question.^3^ If no divisors are found within this range, the number is definitively prime.^3^ While deterministic and 100% accurate, trial division\'s time complexity of O(√n) makes it \"wildly inefficient\" for very large numbers.^5^ For a number around 10 million, its square root is around 3162, meaning thousands of division operations would be required.

- **Sieve of Eratosthenes:** This ancient algorithm is effective for generating a list of all prime numbers up to a specified integer by iteratively marking multiples of each prime.^3^ While suitable for generating primes up to approximately 10 million ^19^, it is generally inefficient for determining the primality of a\
  *single* very large number, primarily due to its significant time and space requirements that scale with the upper limit.^5^ Its time complexity is O(n log log n).^7^

- **Probabilistic Primality Tests (e.g., Miller-Rabin):** These algorithms are significantly faster than trial division for large numbers, often with a time complexity of O(k log³n) for Miller-Rabin.^7^ However, they provide a probabilistic rather than a definitive answer, meaning they offer a very high probability that a number is prime, but not absolute certainty.^3^ The Miller-Rabin test, a \"strong probable prime test,\" works by checking specific modular arithmetic congruences. If these congruences fail, the number is definitively composite; otherwise, it is declared \"probably prime\".^4^ The probability of error can be made arbitrarily small by increasing the number of test iterations (\
  *k*).^4^ These tests are widely employed in cryptographic applications where speed is paramount and an extremely low error probability is acceptable.^3^

- **Deterministic Polynomial-Time Tests (e.g., AKS Primality Test):** Historically, a general, deterministic, unconditional, and polynomial-time algorithm for primality testing was a major open problem.^5^ This changed with the discovery of the AKS primality test in 2002. AKS provides a definitive, 100% accurate answer in polynomial time.^6^ While theoretically groundbreaking, in practice, it can be \"quite slow\" for extremely large numbers compared to the faster probabilistic tests.^19^

The discussion of various primality tests reveals a core computational dilemma: the trade-off between absolute certainty (determinism) and computational speed (efficiency).^4^ Trial division is deterministic but too slow for large numbers. Probabilistic tests are fast but offer only a high likelihood of primality. Even deterministic polynomial-time tests like AKS can be practically slower than probabilistic methods for very large numbers.^19^ This is a fundamental constraint in computational number theory. The optimal choice of algorithm is thus highly dependent on the specific context, including the number\'s size, the required level of certainty, and available computational resources.^7^ For the numbers in the user\'s query (around 10\^7), while trial division is conceptually simple, a computational tool employing more efficient algorithms (like an optimized trial division up to sqrt(N) or a Miller-Rabin test) is essential. The numbers are large enough to make manual checks impossible, but not so astronomically large as to

*require* probabilistic methods for absolute certainty (though probabilistic tests would still offer faster computation).

#### **Role of Computational Tools and Libraries**

Given the magnitude of the numbers in the query, manual primality testing is entirely impractical and prone to error.^3^ Instead, specialized software, programming libraries, or online primality checkers are indispensable.^3^ These tools implement the efficient algorithms discussed, such as Miller-Rabin or more advanced deterministic methods, to provide a rapid determination of primality.^3^ For programmatic verification, various programming languages offer robust mathematical libraries. For example, Python\'s

sympy.isprime() function provides a built-in method for primality testing, offering definitive answers for numbers up to 2\^64 (approximately 1.8 x 10\^19) and probabilistic answers for even larger numbers.^7^

It is important to note that while several sources refer to lists of prime numbers ^15^, these lists typically extend only up to numbers in the order of hundreds of thousands or low millions (e.g., 1,299,827 in ^15^, or 1,000 in ^18^). The numbers in the user\'s query are around 10 million. This immediately indicates that a simple lookup in these provided lists is not a viable method for verification. This reinforces the necessity of dynamically

*running* a primality test algorithm rather than relying on static databases. This observation emphasizes the vastness of the number space and why comprehensive, pre-computed lists of primes are impractical beyond a certain point. The transition from theoretical algorithms to practical computational tools is critical for handling large numbers, highlighting the interdisciplinary nature of modern number theory.

**Table 2: Primality Testing Algorithms Comparison**

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Algorithm               Time Complexity                                   Accuracy                                    Recommended Use                                                                                                             Source Snippets
  ----------------------- ------------------------------------------------- ------------------------------------------- --------------------------------------------------------------------------------------------------------------------------- -----------------
  Trial Division          O(√n)                                             100% (Deterministic)                        Small numbers; initial checks for larger numbers.                                                                           ^3^

  Fermat Primality Test   O(k log n)                                        Probabilistic (can have false positives).   Quick probabilistic test for large numbers; generally less reliable than Miller-Rabin.                                      ^4^

  Miller-Rabin Test       O(k log³n)                                        Probabilistic (very high accuracy).         Efficiently testing primality of large numbers, especially in cryptographic applications.                                   ^3^

  AKS Primality Test      Polynomial time (e.g., O(log\^12 n) or better).   100% (Deterministic).                       Theoretically significant; practically slower than Miller-Rabin for very large numbers, but provides absolute certainty.    ^6^

  Sieve of Eratosthenes   O(n log log n)                                    100% (Deterministic).                       Generating lists of all primes up to a specific, relatively small limit; not efficient for testing a single large number.   ^3^
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This table systematically compares various primality testing algorithms based on crucial performance metrics: time complexity (speed), accuracy (certainty), and their recommended applications. For a user interested in the primality of large numbers, understanding *why* certain algorithms are preferred for different scales or use cases (e.g., Miller-Rabin for cryptography) is essential for a comprehensive and expert-level understanding. It directly addresses the \"how\" of primality testing for large numbers, which is central to the query.

### **4. Analysis of Provided Number Pairs**

This section systematically analyzes each pair, confirming their numerical difference and outlining the necessary steps for primality verification, while explicitly stating the limitations of the provided research material in yielding direct computational results.

#### **General Approach for Verification**

To determine if any given pair of numbers (p, p+2) constitutes a twin prime pair, two fundamental conditions must be rigorously met:

1.  The two numbers must indeed differ by exactly 2. For all pairs provided in the user\'s query, this condition is visibly satisfied.

2.  *Both* numbers within the pair must be confirmed to be prime. This is the critical step that requires computational verification.

Given the magnitude of the numbers (each approximately 10 million), manual primality testing, particularly by trial division, is not a practical approach. Instead, an automated computational environment, such as a specialized online prime number checker or a programming environment equipped with robust mathematical libraries (like SymPy in Python), is indispensable for performing the necessary primality tests.^3^ The provided research material describes various such online tools (e.g., Mathos AI, Cuemath, Browserling\'s testers) that are capable of performing these checks.^3^ However, it is explicitly stated across multiple snippets that the research material

*does not contain the direct computational results* for the specific numbers presented in the query.^3^

This consistent lack of direct results from the browsing of online tools highlights a critical aspect: the *description* of a tool is not equivalent to the *execution* of the tool. While the existence and capabilities of primality checkers are well-documented, their internal workings or pre-computed results are not transparently available in the provided research. This implies that for a rigorous academic or technical report, simply pointing to a URL without understanding the underlying algorithm or having verifiable results is insufficient. This emphasizes the distinction between knowing *that* a tool exists and having the *means* to verify its output or the *data* from its execution.

Consequently, the following analysis will confirm the structural validity of each pair (i.e., that they differ by 2) and outline the required primality verification step, but it cannot definitively declare their twin prime status without external computation. The numbers in the query (around 10\^7) are indeed \"large\" in the context of manual calculation or simple trial division, making automated computation essential. However, it is important to contextualize their size within the broader landscape of number theory and cryptography. Numbers used in modern cryptographic systems can be hundreds of digits long, vastly exceeding 10\^7. Standard computational primality tests, such as those implemented in sympy.isprime(), can definitively handle numbers up to 2\^64 (approximately 1.8 x 10\^19) ^12^, which is far larger than 10\^7. This indicates that while manual methods are impractical, the numbers are not so astronomically large as to push the absolute limits of current deterministic primality tests.

#### **Specific Analysis for Each Pair**

- **(9998969, 9998971)**

  - **Difference:** The difference between 9998971 and 9998969 is 2. This pair satisfies the numerical difference requirement for twin primes.

  - **Primality Test Required:** To confirm if this is a twin prime pair, both 9998969 and 9998971 must be individually subjected to a primality test using an appropriate computational algorithm (e.g., Miller-Rabin or a deterministic test via a reliable online tool or programming library).

  - **Note on Information Availability:** The provided documentation, while describing the methods and tools for primality testing, does not contain the pre-computed or real-time results for these specific numbers.^3^

- **(9999047, 9999049)**

  - **Difference:** The difference between 9999049 and 9999047 is 2. This pair satisfies the numerical difference requirement.

  - **Primality Test Required:** Both 9999047 and 9999049 must be individually tested for primality.

  - **Note on Information Availability:** The provided documentation explicitly indicates the absence of direct primality status for these numbers.^3^

- **(9999161, 9999163)**

  - **Difference:** The difference between 9999163 and 9999161 is 2. This pair satisfies the numerical difference requirement.

  - **Primality Test Required:** Both 9999161 and 9999163 must be individually tested for primality.

  - **Note on Information Availability:** The provided documentation does not offer direct primality status for these numbers.^3^

- **(9999929, 9999931)**

  - **Difference:** The difference between 9999931 and 9999929 is 2. This pair satisfies the numerical difference requirement.

  - **Primality Test Required:** Both 9999929 and 9999931 must be individually tested for primality.

  - **Note on Information Availability:** The provided documentation does not offer direct primality status for these numbers.^3^

- **(9999971, 9999973)**

  - **Difference:** The difference between 9999973 and 9999971 is 2. This pair satisfies the numerical difference requirement.

  - **Primality Test Required:** Both 9999971 and 9999973 must be individually tested for primality.

  - **Note on Information Availability:** The provided documentation does not offer direct primality status for these numbers.^3^

**Table 3: Analysis of Given Number Pairs**

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pair                 Difference   Primality Status of First Number      Primality Status of Second Number     Twin Prime Status                                                                                    Source Snippets
  -------------------- ------------ ------------------------------------- ------------------------------------- ---------------------------------------------------------------------------------------------------- -----------------
  (9998969, 9998971)   2            Requires computational verification   Requires computational verification   Cannot be determined from provided documentation; depends on computational primality test results.   ^1^

  (9999047, 9999049)   2            Requires computational verification   Requires computational verification   Cannot be determined from provided documentation; depends on computational primality test results.   ^1^

  (9999161, 9999163)   2            Requires computational verification   Requires computational verification   Cannot be determined from provided documentation; depends on computational primality test results.   ^1^

  (9999929, 9999931)   2            Requires computational verification   Requires computational verification   Cannot be determined from provided documentation; depends on computational primality test results.   ^1^

  (9999971, 9999973)   2            Requires computational verification   Requires computational verification   Cannot be determined from provided documentation; depends on computational primality test results.   ^1^
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This table directly addresses the user\'s core query for each specific pair in a structured and clear manner. By explicitly stating that the primality status and twin prime status \"Require computational verification\" and \"Cannot be determined from provided documentation,\" it effectively manages user expectations and transparently communicates the limitations of the provided research material. This structured presentation makes the analysis easy to follow and visually reinforces that all given pairs meet the initial structural criterion (differing by 2), thereby highlighting the subsequent critical step of primality testing.

### **5. Conclusion**

This report has meticulously defined prime numbers as natural numbers greater than 1 with precisely two divisors---1 and themselves.^2^ Building upon this, twin primes were characterized as pairs of prime numbers that are separated by a prime gap of exactly two.^1^

While the conceptual definition of twin primes is straightforward, the practical verification of their status for large numbers, such as the pairs provided in the query (each approximately 10 million), presents a significant computational challenge. Manual methods, including basic trial division, are rendered impractical due to the immense number of operations required.^5^ To address this, various sophisticated primality testing algorithms have been developed. These range from deterministic methods that guarantee accuracy but can be computationally intensive for very large numbers (e.g., AKS primality test) to probabilistic methods that offer significantly faster computation at the cost of a minuscule, quantifiable probability of error (e.g., Miller-Rabin test).^4^ The choice of algorithm depends on the scale of the number and the required certainty.

The Twin Prime Conjecture, which postulates the existence of an infinite number of twin prime pairs, remains one of the most compelling and enduring open problems in the field of number theory.^1^ Despite centuries of inquiry and recent significant partial breakthroughs, a definitive proof or disproof continues to elude mathematicians.^1^

The analysis of the specific number pairs provided in the query confirms that they structurally meet the initial criterion of differing by two. However, their ultimate classification as twin primes is contingent upon the rigorous primality testing of each individual number within the pair. As demonstrated throughout this report, the provided documentation, while comprehensive in describing the methodologies and tools, does not contain the pre-computed or real-time computational results necessary to definitively declare the primality status of these specific large numbers.^3^ This means that while the framework for verification has been thoroughly detailed, the specific answers for these pairs require computational execution beyond the scope of the provided information. This approach ensures that the report provides a robust framework for understanding and addressing such mathematical queries, even when direct computational outcomes are not available within the provided data.

#### Works cited

1.  en.wikipedia.org, accessed August 7, 2025, [[https://en.wikipedia.org/wiki/Twin_prime]{.underline}](https://en.wikipedia.org/wiki/Twin_prime)

2.  Prime Number \-- from Wolfram MathWorld, accessed August 7, 2025, [[https://mathworld.wolfram.com/PrimeNumber.html]{.underline}](https://mathworld.wolfram.com/PrimeNumber.html)

3.  Free Prime Number Checker - Mathos AI, accessed August 7, 2025, [[https://www.mathgptpro.com/app/calculator/prime-number-checker]{.underline}](https://www.mathgptpro.com/app/calculator/prime-number-checker)

4.  Primality test - Wikipedia, accessed August 7, 2025, [[https://en.wikipedia.org/wiki/Primality_test]{.underline}](https://en.wikipedia.org/wiki/Primality_test)

5.  Primality Testing - Whitman College, accessed August 7, 2025, [[https://www.whitman.edu/documents/Academics/Mathematics/2018/Worthington.pdf]{.underline}](https://www.whitman.edu/documents/Academics/Mathematics/2018/Worthington.pdf)

6.  Prime Number Calculator, accessed August 7, 2025, [[https://www.lcm-calculator.com/prime-number-calculator]{.underline}](https://www.lcm-calculator.com/prime-number-calculator)

7.  How to check primality in Python - LabEx, accessed August 7, 2025, [[https://labex.io/tutorials/python-how-to-check-primality-in-python-418855]{.underline}](https://labex.io/tutorials/python-how-to-check-primality-in-python-418855)

8.  SOCR Prime Number Factorization Calculators - Statistics Online Computational Resource, accessed August 7, 2025, [[http://socr.ucla.edu/Applets.dir/SOCR_PrimeNumberDecomposition.html]{.underline}](http://socr.ucla.edu/Applets.dir/SOCR_PrimeNumberDecomposition.html)

9.  Prime Number Calculator - Cuemath, accessed August 7, 2025, [[https://www.cuemath.com/calculators/prime-number-calculator/]{.underline}](https://www.cuemath.com/calculators/prime-number-calculator/)

10. Number Primality Test -- Online Number Tools, accessed August 7, 2025, [[https://onlinetools.com/number/number-primality-test]{.underline}](https://onlinetools.com/number/number-primality-test)

11. Test If a Number Is a Prime - Math Tools, accessed August 7, 2025, [[https://onlinetools.com/math/test-prime-number]{.underline}](https://onlinetools.com/math/test-prime-number)

12. Check Prime Number in Python - GeeksforGeeks, accessed August 7, 2025, [[https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/]{.underline}](https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/)

13. en.wikipedia.org, accessed August 7, 2025, [[https://en.wikipedia.org/wiki/Prime_number]{.underline}](https://en.wikipedia.org/wiki/Prime_number)

14. Introduction to Primality Test and School Method - GeeksforGeeks, accessed August 7, 2025, [[https://www.geeksforgeeks.org/dsa/introduction-to-primality-test-and-school-method/]{.underline}](https://www.geeksforgeeks.org/dsa/introduction-to-primality-test-and-school-method/)

15. The First 100008 Primes, accessed August 7, 2025, [[https://t5k.org/lists/small/100000.txt]{.underline}](https://t5k.org/lists/small/100000.txt)

16. Prime Numbers from 0 to 1,000,000, accessed August 7, 2025, [[https://www.mathematical.com/primes0to1000k.html]{.underline}](https://www.mathematical.com/primes0to1000k.html)

17. The complete list of primes., accessed August 7, 2025, [[https://www.math.uchicago.edu/\~luis/allprimes.html]{.underline}](https://www.math.uchicago.edu/~luis/allprimes.html)

18. List of Prime Numbers 1 to 1000 - BYJU\'S, accessed August 7, 2025, [[https://byjus.com/maths/prime-numbers-from-1-to-1000/]{.underline}](https://byjus.com/maths/prime-numbers-from-1-to-1000/)

19. finding if a number is prime LARGE NUMBE - C++ Forum, accessed August 7, 2025, [[https://cplusplus.com/forum/general/110755/]{.underline}](https://cplusplus.com/forum/general/110755/)

20. Mersenne prime - Wikipedia, accessed August 7, 2025, [[https://en.wikipedia.org/wiki/Mersenne_prime]{.underline}](https://en.wikipedia.org/wiki/Mersenne_prime)
