# The Nexus Recursive Harmonic Framework (RHA) — A Triadic Harmonic Magnum Opus
**Driven by:** Dean A. Kulik  
**Date:** November 2025

---

## 0. Notation, Grammar, and Invariants (Ψ-lock)

### 0.1 Nexus symbols and fold-logic
- Phase/control symbols: \( \Delta \) (phase perturbation), \( \oplus \) (phase-join), \( \↻ \) (feedback loop), \( \bot \) (reject / inconsistency), \( \Psi \) (active field state), \( \Omega \) (unresolved entropy), \( \Omega^+ \) (collapsed entry / spectral memory).
- Trust tokens: \( Q \) (trust), \( \kappa \) (curvature), \( H \) (harmonic target), \( \eta \) (tolerance).

### 0.2 Allowed moves (kernel-safe primitives)
1. **Absolute difference:** \( \mathrm{ad}(x,y)=|x-y| \).
2. **Simple sum:** \( \mathrm{ss}(x,y)=x+y \).
3. **Binary bit-length:** 
   $$
   \ell_2(n)=
   \begin{cases}
   \lfloor \log_2 n \rfloor + 1, & n\ge 1\\
   0, & n=0~.
   \end{cases}
   $$
4. **Decimal digit-sum:** \( s_{10}(n)=\sum \text{(base-10 digits of }n\text{)} \).

These four moves plus equality/concatenation are the only permitted symbolic transforms when claiming formal invariants.

### 0.3 Header fold (primary fold operator)
For ordered pair \( (a,b)\in\mathbb{N}^2 \):
$$
\Phi(a,b)=\big(a',b'\big)=\big(|b-a|,\;a+b\big).
$$

**Basic consequences (for \(a,b\ge 0\)):**
- Monotone sum: \( s_{t+1} = a' + b' = |b-a| + a+b \ge a+b = s_t \).
- Parity of \( a+b \) is preserved mod \( 2 \).
- If \( a=b \Rightarrow \Phi(a,b)=(0,2a) \) (absorbing difference).
- **gcd invariance:** \( \gcd(a,b) = \gcd(|b-a|,a+b) \). Thus if \( \gcd(a,b)=1 \) then all iterates remain coprime.

We call the forward orbit \( \{(a_t,b_t)\}_{t\ge 0} \) a **header-fold orbit**.

### 0.4 Eight-beat Nexus kernel (trace vector)
Let \( x=a+b \), and let \( \vec{d}(x) \) be the base-10 digits of \( x \). For a digit sequence \( \vec{d}=(d_1,\dots,d_L) \), define the absolute discrete difference
$$
(\Delta \vec{d})_i = |d_{i+1}-d_i|,\quad \mathrm{len}(\Delta\vec{d})=\max(L-1,0),\quad \Delta^k=\underbrace{\Delta(\Delta(\cdots\Delta}_{k\text{ times}}\vec{d}))~.
$$

The **Eight-beat** record at a fold is:
1. Past: \( (a,b) \)  
2. Now: \( (a',b')=\Phi(a,b) \)  
3. \( L_0=\mathrm{len}\big(\vec{d}(a+b)\big) \)  
4. \( L_1=\mathrm{len}\big(\Delta \vec{d}(a+b)\big) \)  
5. \( |L_1-L_0| \)  
6. \( L_4=\mathrm{len}\big(\Delta^4 \vec{d}(a+b)\big) \)  
7. \( |L_4 - |L_1-L_0|| \)  
8. \( L_\Delta=L_1 \).

Set \( \mathrm{len}(\emptyset)=0 \) by convention.

---

## 1. Triangular Quantization and the Mark1 Harmonic Engine

### 1.1 Mark1 harmonic constant \( H_{\text{MARK1}} \)
We adopt the exact form
$$
H_{\text{MARK1}}=\frac{\pi}{9}\approx 0.3490658503988659.
$$
Prose shorthand “0.35” is allowed; all calculations use \( \pi/9 \) (radians).

**Associated slope (target ratio):**
$$
r^\star=\tan\!\left(\frac{\pi}{9}\right)\approx 0.36397023426620234~.
$$

### 1.2 Triadic archetype and the \(\{1,5,9\}\) anchor
On the digit ring \( \mathbb{Z}_{10} \), the positions \( \{1,5,9\} \) are equally separated by 4. This triad functions as a **Ψ-core** (compression triplet) after folding; no group property is asserted beyond equidistance and symmetry anchoring.

Define the triadic projection \( \pi_{\triangle}:\{0,\dots,9\}\to \Delta^2 \) (barycentric simplex) by
$$
w_c(d)=\exp\!\left(-\frac{\min_{c\in\{1,5,9\}} |d-c|^2}{2\sigma^2}\right),\qquad
\mathbf{b}(d)=\frac{\big(w_1(d),w_5(d),w_9(d)\big)}{\sum_{c\in\{1,5,9\}}w_c(d)},
$$
with scale \( \sigma>0 \). The point \( \mathbf{b}(d) \) provides the triangle “archetype” embedding of digit \( d \).

### 1.3 Angle quantizer (right-triangle scan)
Enumerate coprime integer legs \( (a,b)\in\mathbb{Z}_{>0}^2 \) and angle
$$
\theta(a,b)=\arctan\!\left(\frac{a}{b}\right)\in(0,\tfrac{\pi}{2}).
$$
Fix angular tolerance (default)
$$
\varepsilon_\theta=10^{-3}\ \text{rad}\ (\approx 0.0573^\circ).
$$
The **resonance indicator** is
$$
Q_{\varepsilon_\theta}(\theta)=\mathbb{1}\big(|\theta-H_{\text{MARK1}}|<\varepsilon_\theta\big).
$$

**Slope tolerance (derived):** Since \( \frac{d}{dx}\arctan x = \frac{1}{1+x^2} \),
$$
|\theta-\theta^\star|<\varepsilon_\theta\quad\Longrightarrow\quad
\left|\frac{a}{b}-r^\star\right| < \varepsilon_r,\quad
\varepsilon_r=\varepsilon_\theta\cdot \big(1+(r^\star)^2\big).
$$
Numerically,
$$
\varepsilon_r\approx 10^{-3}\cdot\big(1+0.3639702^2\big)\approx 1.132\times 10^{-3}.
$$

### 1.4 Farey–mediant pursuit (dense hits guarantee)
Let \( \frac{p_0}{q_0}<r^\star<\frac{p_1}{q_1} \) be initial rationals. Iteratively form mediant 
$$
\frac{p}{q}=\frac{p_0+p_1}{q_0+q_1}
$$
and replace the bracket that still contains \( r^\star \). This realizes the continued-fraction convergents of \( r^\star \). Since rationals are dense, there exist infinitely many coprime \( (a,b)=(p,q) \) obeying \( \left|\frac{a}{b}-r^\star\right|<\varepsilon_r \Rightarrow Q_{\varepsilon_\theta}(\theta)=1 \).

### 1.5 Glyph encoding for triangle hits (allowed-move only)
For a hit \( (a,b) \), define the **glyph**
$$
g(a,b)=\Big(\underbrace{|b-a|}_{\mathrm{ad}},\ \underbrace{a+b}_{\mathrm{ss}},\ \underbrace{\ell_2(a+b)}_{\text{bit\_len}},\ \underbrace{s_{10}(a)+s_{10}(b)}_{\text{digit\_sum}}\Big).
$$
**Equivalence:** \( (a,b)\sim(c,d) \iff g(a,b)=g(c,d) \).

### 1.6 Quantizer acceptance window in degrees
For reporting,
$$
\varepsilon_\theta^{\circ}=\varepsilon_\theta\cdot \frac{180}{\pi}\approx 0.0573^\circ,\qquad
\theta^\star=\frac{180}{9}=20^\circ.
$$

### 1.7 Degenerate “median/perimeter” claim (Ω quarantine)
For flat triples \( (x,y,z) \) with \( x=y+z \), median to base \( m=\tfrac{x}{2} \) and perimeter \( P=2x \) gives \( \rho=\tfrac{m}{P}=\tfrac{1}{4} \). Hence any “exact \( 0.35 \)” from this construction is **tagged \( \Omega \)** unless exhibited with a reproducible counter-definition that fits allowed moves.

### 1.8 Asymptotic hit density (Diophantine estimate)
Let \( B\ge 1 \) and count
$$
N(B)=\#\Big\{(a,b)\in\mathbb{Z}_{>0}^2:\ \gcd(a,b)=1,\ b\le B,\ \left|\frac{a}{b}-r^\star\right|<\varepsilon_r\Big\}.
$$
Using coprime pair density \( \frac{6}{\pi^2} \) and interval width \( 2\varepsilon_r \), the asymptotic
$$
N(B)\ \sim\ \frac{12}{\pi^2}\,\varepsilon_r\,B^2\qquad (B\to\infty)
$$
estimates expected resonance hits up to slope denominator \( B \).

---

## 2. Recursive Memory, Collapse, and Symbolic Convergence

### 2.1 Ψ-state, Δ-kick, and collapse metric
Let \( \Psi_t \) be the system’s active field; a query/input injects \( \Delta\Psi_t \). Choose a task-appropriate norm \( \|\cdot\| \) and define
$$
\varepsilon_\Psi(t)=\|\Delta\Psi_t\|,\qquad
\text{Collapse when } \lim_{t\to\infty}\varepsilon_\Psi(t)=0.
$$

### 2.2 Ω-ledger (spectral memory)
Each collapse produces a stable glyph and trace. Record entries as
$$
\Omega^+ = \big\{ (g,\ \mathrm{addr}_B,\ B,\ L,\ Q,\ \kappa,\ \mathrm{EightBeat},\ \text{timestamp}) \big\}.
$$

### 2.3 Triadic Collapse Theorem (header-fold form)
**Theorem.** Any header-fold orbit that admits an infinite subsequence of Mark1 hits (accepted angles) collapses symbolically to three generator classes whose invariant ratio converges to \( H_{\text{MARK1}}=\pi/9 \).

**Sketch (allowed-move calculus):**
1. Non-decreasing sums \( s_t \) and bounded differences \( d_t=|b_t-a_t| \) control growth.
2. Farey pursuit guarantees infinite rational hits near \( r^\star \).
3. Acceptance prunes symbol space to three equivalence classes under \( g \), forming a triad; the observed ratio stabilizes at \( H_{\text{MARK1}} \).

---

## 3. Trust, Curvature, and Termination

### 3.1 Scalar trust for bitfields
For a bitstring \( \mathbf{v}\in\{0,1\}^N \) with mean \( \bar v=\frac{1}{N}\sum_i v_i \),
$$
Q_{\text{space}}=1-\left|\bar v - H_{\text{MARK1}}\right|.
$$

### 3.2 General trust components (actual/potential normalization)
Let observable \( Y\in[0, Y_{\max}] \), with normalized \( \widetilde{Y}=Y/Y_{\max}\in[0,1] \). Define
$$
Q_Y=1-\big|\widetilde{Y}-H_{\text{MARK1}}\big|.
$$
Typical components: \( Q_{\text{space}}, Q_{\text{time}}, Q_{\text{freq}} \).

**Aggregated confidence (geometric mean with weights \( w_j>0, \sum w_j=1 \)):**
$$
\overline{Q}=\prod_{j} Q_j^{\,w_j}.
$$

### 3.3 Curvature metric (second difference, robust)
For a real sequence \( s_1,\dots,s_M \) (from allowed transforms),
$$
\Delta^2 s_i = s_{i+1}-2s_i+s_{i-1},\qquad
\kappa = \mathrm{median}_i\big(|\Delta^2 s_i|\big).
$$
**Normalized curvature (for scale \( S>0 \)):**
$$
\kappa_{\text{norm}}=\frac{\kappa}{S}.
$$

### 3.4 Termination (Ψ-lock) and hysteresis
Let \( \eta=10^{-3} \). Terminate when
$$
Q_j \ge 1-\eta\ \ \forall j,\qquad \kappa \le 10^{-3}.
$$
To avoid false locks, require **hysteresis**: conditions must hold for \( T_{\text{hold}} \) consecutive iterations (e.g., \( T_{\text{hold}}=5 \)).

### 3.5 Lyapunov-like merit function (for PSREQ control)
Define
$$
V_t = \big(1-\overline{Q}_t\big) + \lambda\, \kappa_t,\qquad \lambda>0,
$$
and enforce \( V_{t+1}\le V_t \) via controller design.

### 3.6 Spectral trust and entropy
Given a power spectrum \( \{P_k\}_{k=1}^K \) of a sequence, define spectral flatness
$$
\mathrm{SFM}=\frac{\exp\!\left(\frac{1}{K}\sum_{k=1}^{K}\ln P_k\right)}{\frac{1}{K}\sum_{k=1}^{K}P_k}\in[0,1].
$$
Set a target \( \mathrm{SFM}^\star \) (e.g., near 0 for harmonic content) and define
$$
Q_{\text{freq}}=1-\left|\mathrm{SFM}-\mathrm{SFM}^\star\right|.
$$

### 3.7 Contraction model and convergence rate
If the closed-loop map \( F_c \) is a contraction on a complete metric space with constant \( L<1 \):
$$
\|F_c(x)-F_c(y)\|\le L\|x-y\|,
$$
then the unique fixed point \( x^\star \) is reached with rate
$$
\|x_t-x^\star\|\le L^t\|x_0-x^\star\|.
$$

### 3.8 First-order trust dynamics
For a measured ratio \( \rho(t) \in [0,1] \) driven toward \( H \), model
$$
\frac{d\rho}{dt}=-k\big(\rho-H\big)\quad\Rightarrow\quad \rho(t)=H+(\rho_0-H)e^{-kt}.
$$

---

## 4. SHA-256 as Structured Compression Field (SCF) and HRG Steering

### 4.1 SCF observable construction (allowed-move sequences)
From internal round words \( W_i \) (conceptual), derive sequences
$$
s^{(\mathrm{hw})}_i=\frac{\text{HammingWeight}(W_i)}{\text{bitlen}(W_i)},\quad
s^{(\ell_2)}_i=\ell_2\!\big(|W_i|\big),\quad
s^{(d)}_i=s_{10}\!\big(|W_i|\big),
$$
and compute \( Q \) on the digest and \( \kappa \) on \( s^{(\cdot)} \).

### 4.2 Harmonic Reversal Geometry (HRG): steering, not inversion
Let \( M \) be a preimage parameterized by an admissible palette \( \mathcal{P} \) (e.g., constrained suffix). HRG searches
$$
M^\star=\arg\min_{M\in\mathcal{P}}\ \Big[\ \alpha\,(1-\overline{Q}(M))+\beta\,\kappa(M)\ \Big],\quad \alpha,\beta>0,
$$
subject to allowed-move perturbations on \( \mathcal{P} \). This **reduces \( \Omega \)** in curated families but does **not** assert generic inversion of SHA-256.

### 4.3 Pythagorean surrogate (interpretive guide)
Use a surrogate consistency relation
$$
A^2+B^2 \to C^2,
$$
where \( C \) encodes digest observables, \( A \) structured preimage features, \( B \) curvature/entropy residue. HRG attempts to co-tune \( (A,B) \) so \( \overline{Q}\uparrow \), \( \kappa\downarrow \) under palette constraints.

---

## 5. \(\pi\)/BBP Addressability and the Ω\(^+\) Ledger

### 5.1 BBP (base-16) for positional access
$$
\pi=\sum_{k=0}^{\infty}\frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right).
$$

### 5.2 Glyph → address contract (allowed-move only)
For \( g=(g_1,g_2,g_3,g_4) \),
$$
h(g)=s_{10}(g_1)+s_{10}(g_2)+s_{10}(g_3)+s_{10}(g_4),\qquad
\mathrm{addr}_B(g)=\big(\ell_2(g_2)\cdot h(g)\big)\bmod M_B,
$$
with base \( B\in\{10,16\} \) and stride modulus \( M_B \) declared in advance. Extract window
$$
\Pi^{(B)}\big[\mathrm{addr}_B(g):\mathrm{addr}_B(g)+L\big)
$$
for fixed \( L \).

### 5.3 Anchor detection (statistical Ω-promotion test)
Let \( \mathcal{A} \) be a pre-declared set of anchors (e.g., patterns, primes, motifs). Define indicator
$$
X=\mathbb{1}\Big(\Pi^{(B)}[\cdot]\ \text{contains an anchor from }\mathcal{A}\Big).
$$
Under null i.i.d. digits (base \( B \)), the probability that a specific length-\( m \) pattern appears in any of \( W \) non-overlapping windows is
$$
p_0 \le 1-(1-B^{-m})^{W}\ \approx\ W\,B^{-m}\quad (\text{Bonferroni}).
$$
Promote to \( \Omega^+ \) only if
$$
X=1,\quad p_0\le \alpha\quad (\text{e.g., } \alpha=10^{-3}),\quad \overline{Q}\ge 1-\eta,\quad \kappa\le 10^{-3}.
$$

### 5.4 Twin-prime gating (controlled Ω)
Define \( G(n)=\mathbb{1}(\text{$n$ and $n+2$ prime}) \). A window is **gated** if its index obeys \( G(\mathrm{addr}_B(g))=1 \) or aligns to a twin-prime schedule. Treat any enrichment claims as \( \Omega \) until significance passes the anchor test.

**Density heuristic (Ω-tagged):** Under the Hardy–Littlewood heuristic, the expected count up to \( x \) is \( \sim 2C_2\frac{x}{(\log x)^2} \) with twin-prime constant \( C_2\approx 0.66016 \). Use only as guidance; do not promote without tests above.

### 5.5 Minimal Ω\(^+\) ledger schema
Each row:
$$
(g,\ \mathrm{addr}_B,\ B,\ L,\ \overline{Q},\ \kappa,\ \text{EightBeat},\ \text{status}\in\{\Omega,\Omega^+\},\ \text{note})
$$

---

## 6. PSREQ Cycle and Samson’s Law (feedback control)

### 6.1 PSREQ operators (discrete time)
Let state \( x_t \), controller input \( u_t \), forward map \( x' = F(x_t) \), error metric \( \Delta\Psi_t \). The stages:
- **Position (P):** initialize \( x_0 \) (input or prior \( \Omega^+ \)).
- **State (S):** \( x'_t = F(x_t) \), compute \( \Delta\Psi_t \).
- **Reflection (R):** if \( \|\Delta\Psi_t\|>\tau \), set \( x_t \gets x'_t + u_t \).
- **Expansion (E):** enrich DOF: \( x_t \gets x_t \oplus \delta x_t \).
- **Quality (Q):** evaluate \( \overline{Q}_t, \kappa_t \); terminate if Ψ-lock, else \( t\leftarrow t+1 \).

### 6.2 Samson’s Law v2 — PID steering to \( H_{\text{MARK1}} \)
Let measured ratio \( \widehat{H}(x_t)\in[0,1] \), error \( e_t = H_{\text{MARK1}} - \widehat{H}(x_t) \). Controller:
$$
u_t = K_P e_t + K_I \sum_{k=0}^{t} e_k + K_D (e_t - e_{t-1}),
$$
$$
x_{t+1} = F(x_t) + u_t.
$$

**LTI surrogate stability:** If locally \( x_{t+1}\approx a x_t + b u_t \) with \( |a|<1 \), standard discrete PID tuning yields closed-loop pole \( z \) inside the unit circle. A conservative region:
$$
0<K_P<\frac{1-a}{b},\quad 0<K_I<\frac{(1-a)^2}{2b},\quad 0\le K_D\le \frac{1-a}{2b}.
$$

### 6.3 Phase-join rule (⊕) and reject (⊥)
- **⊕ join:** merge two partial states \( x,y \) iff \( Q(x\oplus y)\ge \min(Q(x),Q(y)) \) and \( \kappa(x\oplus y)\le \max(\kappa(x),\kappa(y)) \).
- **⊥ reject:** if any invariant under allowed moves is violated (e.g., declared tolerance exceeded), tag \( \bot \) and revert to last Ψ-lock.

---

## 7. Cross-Domain Bridges (falsifiable signatures)

### 7.1 Biology / PSREQ therapeutics
Duty-cycle stabilization near \( H \):
$$
\mathrm{DC}=\frac{T_{\text{on}}}{T_{\text{on}}+T_{\text{off}}}\ \to\ H_{\text{MARK1}},\quad
Q_{\mathrm{DC}}=1-\left|\mathrm{DC}-H_{\text{MARK1}}\right|.
$$
Therapy stops when \( Q_{\mathrm{DC}}\ge 1-\eta \) over \( T_{\text{hold}} \).

### 7.2 Planetary homeostasis
**Energy-balance model:**
$$
(1-\alpha)\frac{S_0}{4}=\sigma T^4,
$$
with albedo \( \alpha \), solar constant \( S_0 \), Stefan–Boltzmann \( \sigma \), temperature \( T \). Define usable-energy fraction \( \rho=\frac{E_{\text{used}}}{E_{\text{available}}} \) and monitor
$$
Q_{\text{planet}}=1-\big|\rho - H_{\text{MARK1}}\big|.
$$

### 7.3 Black-hole phenomenology (Ω-conjecture)
Bekenstein–Hawking entropy
$$
S=\frac{k_B c^3}{4G\hbar}\,A=\frac{k_B A}{4 \ell_P^2},
$$
with area \( A \) and Planck length \( \ell_P \). Conjectural clustering of quasinormal-mode ratios (Ω-tagged):
$$
\frac{\gamma}{\omega}\ \approx\ f\!\big(\tan(\tfrac{\pi}{9})\big)\quad\text{for rational \( f \)}.
$$

### 7.4 Markets & weather — assimilation form
Let a baseline predictor give \( x'_t \); assimilate observation \( y_t \) with gain \( K_t \):
$$
x_{t+1}=x'_t + K_t\,(y_t - x'_t),\qquad
K_t = \arg\min_{K}\ \Big( (1-\overline{Q}_{t+1}) + \lambda \kappa_{t+1}\Big).
$$

---

## 8. Structured Examples (specifications)

### 8.1 Triangle-ledger pipeline (T-Ledger)
For each \( (a,b) \) with \( \gcd(a,b)=1 \):
1. \( \theta=\arctan(a/b) \), accept if \( |\theta-\pi/9|<\varepsilon_\theta \).
2. Record glyph \( g(a,b) \).
3. Record Eight-beat.
4. Compute \( \mathrm{addr}_B(g) \) and window \( \Pi^{(B)}[\cdot] \).
5. Evaluate \( \overline{Q}, \kappa \); run anchor test; set \( \Omega \) or \( \Omega^+ \).

**Stop:** first triple of \( \Omega^+ \) rows satisfying Ψ-lock \( (\overline{Q}\ge 1-\eta,\ \kappa\le 10^{-3}) \).

### 8.2 SCF/HRG palette (S-Ledger)
Choose a curated preimage family \( \mathcal{P} \) (e.g., fixed prefix, variable numeric nonce restricted by allowed moves). For each \( M\in\mathcal{P} \):
- Compute digest observables; build \( s^{(\cdot)} \).
- Evaluate \( \overline{Q}, \kappa \).
- HRG guidance: accept perturbations that strictly reduce \( V_t \).
- Record ledger; apply \( \Omega^+ \) test.

### 8.3 \(\pi\)-ledger (π-Ledger)
Map glyphs to \( \mathrm{addr}_B \), scan fixed window \( L \), run anchor test, then Eight-beat + trust/curvature checks for promotion.

---

## 9. Editorial Guardrails (numerology hygiene)

- Compute with \( \pi/9 \); display “0.35” for readability only.
- Cosmology/coincidence claims remain \( \Omega \) unless they pass **both** trust/curvature thresholds and the statistical anchor test.
- All theorem-level statements derive solely from allowed moves.

---

## 10. Synthesis (Ψ-state, Ω-residue, ↻-plan)

- **Ψ-state (collapsed):**  
  \( H_{\text{MARK1}}=\pi/9 \) defined; angle/slope tolerances explicit; glyph equivalence explicit; \( \overline{Q} \), \( \kappa \), hysteresis, Lyapunov \( V_t \) provided; SCF/HRG posed as constrained optimization; BBP addressing and statistical promotion rule given; PSREQ/PID stabilization region supplied; asymptotic hit density supplied; spectral trust supplied.

- **Ω-residue (isolated):**  
  Black-hole QNM ratio conjecture; any degenerate-triangle median/perimeter “0.35” claim without Eight-beat + stats; un-gated twin-prime enrichments without correction; any triad “group” assertion beyond equidistance.

- **↻-plan:**  
  Populate T- / S- / π-Ledgers to 3 \( \Omega^+ \) entries each with Ψ-lock; then instantiate domain pilots (hardware resonance gate, BCI duty-cycle entrainment).

---

## Appendix A — Operators and Identities

### A.1 Length and digit operators
For \( n\in\mathbb{N} \), \( \vec{d}(n) \) are base-10 digits:
$$
\mathrm{len}(\vec{d}(n))=
\begin{cases}
1, & n=0\\
\lfloor \log_{10} n \rfloor +1, & n\ge 1
\end{cases},\qquad
s_{10}(n)=\sum \vec{d}(n).
$$

### A.2 Δ on digit sequences
$$
(\Delta \vec{d})_i=|d_{i+1}-d_i|,\quad \mathrm{len}(\Delta \vec{d})=\max(\mathrm{len}(\vec{d})-1,0).
$$

### A.3 Acceptance defaults
$$
\varepsilon_\theta=10^{-3}\ \text{rad},\quad
\varepsilon_r=\varepsilon_\theta\cdot\big(1+(r^\star)^2\big),\quad
\eta=10^{-3},\quad
T_{\text{hold}}=5.
$$

---

## Appendix B — Boxed Formulas (ready-to-cite)

### B.1 Mark1 resonance test
$$
\boxed{~Q_{\varepsilon_\theta}(\theta)=\mathbb{1}\big(|\theta-\pi/9|<\varepsilon_\theta\big)~,}
$$
$$
\boxed{~\left|\frac{a}{b}-\tan(\pi/9)\right|<\varepsilon_\theta\big(1+\tan^2(\pi/9)\big)~.}
$$

### B.2 Glyph map
$$
\boxed{~g(a,b)=\big(|b-a|,\ a+b,\ \ell_2(a+b),\ s_{10}(a)+s_{10}(b)\big)~.}
$$

### B.3 Trust, curvature, aggregation
$$
\boxed{~Q_Y=1-\big|\tfrac{Y}{Y_{\max}}-H_{\text{MARK1}}\big|,\quad \overline{Q}=\prod_j Q_j^{\,w_j}~,}
$$
$$
\boxed{~\kappa=\mathrm{median}\big(|\Delta^2 s_i|\big)~.}
$$

### B.4 Termination (Ψ-lock with hysteresis)
$$
\boxed{~Q_j\ge 1-\eta\ \forall j,\quad \kappa\le 10^{-3}\ \text{for } T_{\text{hold}}\ \text{consecutive steps}~.}
$$

### B.5 BBP (positional \( \pi \), base-16)
$$
\boxed{~\pi=\sum_{k=0}^{\infty}\frac{1}{16^k}\left(\frac{4}{8k+1}-\frac{2}{8k+4}-\frac{1}{8k+5}-\frac{1}{8k+6}\right)~.}
$$

### B.6 Glyph → address
$$
\boxed{~\mathrm{addr}_B(g)=\big(\ell_2(g_2)\cdot \sum_{i=1}^4 s_{10}(g_i)\big)\bmod M_B~.}
$$

### B.7 Samson’s Law (PID)
$$
\boxed{~u_t = K_P e_t + K_I \sum_{k=0}^{t} e_k + K_D (e_t - e_{t-1}),\quad e_t=H_{\text{MARK1}}-\widehat{H}(x_t)~.}
$$

### B.8 Lyapunov merit
$$
\boxed{~V_t = \big(1-\overline{Q}_t\big) + \lambda\,\kappa_t,\ \ \lambda>0,\ \text{ enforce } V_{t+1}\le V_t~.}
$$

### B.9 Asymptotic resonance-hit count
$$
\boxed{~N(B)\ \sim\ \frac{12}{\pi^2}\,\varepsilon_r\,B^2\quad (B\to\infty)~.}
$$

---

## Appendix C — Micro-Ledger Templates

### C.1 Triangle-Ledger (T-Ledger)

| Hit | \( (a,b) \) | \( \theta \) (rad) | \( Q_{\varepsilon_\theta} \) | Glyph \( g \) | Eight-beat | \( \mathrm{addr}_B \) | \( \overline{Q} \) | \( \kappa \) | Status |
|---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---|
| 1 |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |  |

**Stop rule:** first \( \ge 3 \) entries with \( \Omega^+ \) and Ψ-lock.

### C.2 SCF-Ledger (S-Ledger)

| Case | Palette \( \mathcal{P} \) | Preimage \( M \) | Digest Obs. | Round trace \( s \) | \( \overline{Q} \) | \( \kappa \) | \( \mathrm{addr}_B \) | Eight-beat | Status |
|---:|:---|:---|:---|:---|:---:|:---:|:---:|:---|:---|
| 1 |  |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |  |

### C.3 \(\pi\)-Ledger (π-Ledger)

| Row | Glyph \( g \) | \( \mathrm{addr}_B \) | Base \( B \) | Window \( L \) | Anchor? | \( \overline{Q} \) | \( \kappa \) | Status |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 |  |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |

---

## Appendix D — Fixed-Byte Seeding (spec)

**Seed rule (declare locally):** From each 8-digit byte \([d_1,\dots,d_8]\), form ordered pairs by concatenation
$$
(a,b)=(10\,d_1+d_2,\ 10\,d_3+d_4),\quad (a',b')=(10\,d_5+d_6,\ 10\,d_7+d_8),
$$
gcd-reduce to coprime pairs, then feed each pair into §1.3–§1.5 and log via Appendix C. (This rule uses only concatenation, digit-sum, gcd; all are compatible with allowed-move discipline for invariants.)

---

## Appendix E — Glossary

- **Glyph:** Allowed-move feature tuple attached to an accepted geometry or symbol; forms addressing keys.  
- **Ω/Ω\(^+\):** Unresolved / collapsed entries; \( \Omega^+ \) acts as spectral memory.  
- **Ψ-lock:** Termination event with \( Q \) near 1 and curvature flatness (\( \kappa \) small) held across hysteresis.
