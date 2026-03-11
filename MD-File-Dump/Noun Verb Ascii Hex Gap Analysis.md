# Noun/Verb Wave Gap Analysis (ASCII / Binary / Hex)

_Generated: 2026-01-11_

## What this is

You asked for a **non-token-fetish** way to look at language: treat text as a **continuous signal** (bytes → bits → phase), and then ask whether **nouning** and **verbing** leave different *gap signatures* in ASCII/binary/hex — but only when measured over **complete sets** (whole corpora), not single artifacts.

This report does exactly that on the Nexus documents currently loaded in this session.

## Data used (complete-set constraint)

The analysis pools *all* the following sources into a single stream (so we’re not overfitting one page):

- `nexus_complete_solution.md`
- `nexus_sha_harmonic_leak_addendum.md`
- `NexusSILR_Complete_Training (2).ipynb`
- `rotating_3_plate_smoothing.md`
- `The Nexus Framework - Sha Solved-Title Mathematical Waveforms As Multi-Dimensional .md`
- `The Nexus Framework - Title Mathematical Waveforms As Multi-Dimensional Representations Of Reality (2).md`
- `The Nexus Framework - Title The Waveform Nature Of Mathematical Operations In Asm (2).md`
- `The Nexus Framework - Title The Waveform Nature Of Mathematical Operations In Asm.md`
- `Title_Mathematical_Waveforms_as_Multi-Dimensional_Representations_of_Reality.md`
- `Title_The_Waveform_Nature_of_Mathematical_Operations_in_ASM.md`

## Definitions

### 1) From bytes to phase

Given an ASCII byte $b\in\{0,\dots,255\}$, define:

$$n(b)=b\bmod 16\qquad\text{(low hex nibble)}$$

$$\theta(b)=2\pi\,\frac{n(b)}{16}\qquad\text{(phase on a 16-spoke wheel)}$$

For language, we apply this either to **first-letter bytes** (word-onset phase) or **all bytes** (in-word carrier phase).

### 2) Noun-ish vs Verb-ish events

To avoid “tokenization worship” but still get a *category signal*, I used a **minimal heuristic POS classifier**:

- **Verb-ish (V):** auxiliaries/modals; words after `to`; common verb suffixes `-ing`, `-ed`, `-ize`, …

- **Noun-ish (N):** capitalization/terms; noun suffixes `-tion`, `-ment`, `-ness`, …; determiners → noun bias.

Everything else stays **U** (unknown) and is not forced.


This is intentionally crude; the point is **aggregate invariants**, not perfect tagging.

### 3) Gap signal

Let $p_1<p_2<\dots<p_k$ be the **character offsets** where a class event begins (noun word-starts or verb word-starts). Define gaps:

$$g_i = p_{i+1}-p_i$$

We summarize with mean/median/standard deviation and coefficient of variation:

$$\text{CV} = \frac{\sigma_g}{\mu_g}$$

## Results

### A) Gap structure (character-domain)

| Class        |   Token count |   Mean gap (chars) |   Median gap (chars) |   Std gap |      CV |
|:-------------|--------------:|-------------------:|---------------------:|----------:|--------:|
| Noun-ish (N) |          3656 |            39.3729 |                 24   |   49.3844 | 1.25427 |
| Verb-ish (V) |          1793 |            80.2087 |                 44.5 |  119.966  | 1.49567 |

Interpretation (strictly about the corpus you loaded):

- Verb-ish events are **more sparse** (larger mean gap) and **more bursty** (higher CV).

- Noun-ish events are **denser** and slightly **less bursty**.

### B) Binary signature (why nouns/verbs ‘feel’ different)

For first letters, ASCII has a known structural bit: bit 5 (0x20) separates **uppercase** from **lowercase** for alphabetic characters.

Measured over this full corpus:

- Noun-ish first-letter bit5 mean: $0.248$

- Verb-ish first-letter bit5 mean: $0.834$

So verb-ish word onsets are overwhelmingly lowercase, while noun-ish onsets are much more title/term-cased. That is a **binary-level category watermark** in English.

### C) Hex-phase bias (low nibble of first letters)

Low-nibble distributions for first letters differ strongly between noun-ish and verb-ish pools.

- Chi-square (2×16) on low-nibble counts: $\chi^2=285.16$ with $df=15$, $p\approx 0.00e+00$

- Total variation distance: $\mathrm{TVD}\approx 0.199$


Top nibble deltas (percentage-point differences):

| Nibble   |   Noun-ish % |   Verb-ish % |   Δ (V-N) pp |
|:---------|-------------:|-------------:|-------------:|
| 0x8      |     11.488   |      3.29057 |     -8.19739 |
| 0x7      |      4.51313 |      9.25823 |      4.7451  |
| 0x9      |      5.03282 |      9.42554 |      4.39272 |
| 0x3      |     15.6182  |     19.9665  |      4.34837 |
| 0x4      |     18.2166  |     14.8355  |     -3.38116 |
| 0x5      |      3.52845 |      6.4696  |      2.94116 |

This is the **hex-level** version of the binary fact above: different letter-onset populations → different nibble-phase occupation.

### D) Vowel density (carrier-wave differences)

- Noun-ish mean vowel ratio: $0.327\pm0.197$ over $3656$ words

- Verb-ish mean vowel ratio: $0.396\pm0.115$ over $1793$ words

Verbing carries **more vowel energy** (higher average vowel ratio) and is **less variable** across instances in this corpus.

### E) Weak 9/18 periodicity in the noun/verb sequence

Define a token-sequence signal $s_t\in\{-1,0,+1\}$ where noun-ish $=-1$, verb-ish $=+1$, unknown $=0$. On a 32,768-token window, the FFT shows several peaks with periods near ~9–10 and ~16–18 tokens.

This is **not proof** by itself (language has many built-in cadences), but it’s exactly the kind of “sideways” structure you were pointing at.


Top spectral components (token-domain):

|   freq (cycles/token) |   period (tokens) |   power |
|----------------------:|------------------:|--------:|
|           0.103949    |           9.62011 | 75289.8 |
|           0.00191638  |         521.818   | 71203.1 |
|           0.000116144 |        8610       | 70505.2 |
|           0.0573751   |          17.4291  | 63124.6 |
|           0.00214866  |         465.405   | 61464.2 |
|           0.00197445  |         506.471   | 53890.8 |
|           0.101742    |           9.82877 | 48578.2 |
|           0.00174216  |         574       | 46136.2 |

## A concrete “Universal Verb Detector” (sync vs avoid)

You described two SILR modes:

- **Sync-seeking:** phase bins clump (low entropy), autocorrelation positive

- **Sync-avoiding:** phase bins flatten *but* correlations show structured avoidance (negative or alternating autocorrelation)


Here’s a minimal detector that works on *any* byte stream, not just language:

1) Choose an event stream (e.g., word starts, opcode boundaries, or rising edges).

2) Map each event to a phase wheel (hex is 16-spoke; you can also use 9-spoke with $\pi/9$ framing).

3) Compute phase histogram $P$ and normalized Shannon entropy:

$$H(P)=-\sum_{i=0}^{m-1} P_i\log P_i\,,\quad H_{\max}=\log m\,,\quad S=1-\frac{H(P)}{H_{\max}}$$

$S\to 1$ means **clumping** (sync-seeking). $S\to 0$ means **flat occupancy**.

4) Compute a lag-1 autocorrelation of the phase sequence $(\theta_k)$:

$$\rho_1=\mathrm{corr}(\theta_k,\theta_{k+1})$$

$\rho_1>0$ tends to sync-seeking; $\rho_1<0$ tends to alternating/avoidance.

5) Add SILR scale-invariance by repeating steps 3–4 across window sizes and measuring stability:

$$\mathrm{SILR\_stab}(w)=\frac{\sigma_{z(w)}}{|\mu_{z(w)}|+\epsilon}$$

Then classify mode by $(S,\rho_1,\mathrm{SILR\_stab})$ jointly — never by one number.

## What I’d do next (if you want the ‘speech hides computation’ proof stronger)

- **Control corpora:** run the same pipeline on unrelated English text and on shuffled versions of your corpus.

- **Invariants across domains:** apply the exact same detector to (a) your SHA constant stream, (b) prime-gap streams, (c) assembly opcode streams.

- **Look for the same attractor band:** if your $H\approx \pi/9$ story is real as an invariant, you should see *the same* $(S,\rho_1)$ behavior recur at the same projection scales.

## Notes and limits

- This is **aggregate** evidence only; single spectacular alignments are treated as *anecdotes*.

- The noun/verb tagger here is intentionally light. If you want, we can swap it for a full POS tagger — but only if it *improves invariants* rather than creating a new fragile dependency.
