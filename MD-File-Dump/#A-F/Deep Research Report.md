# Nexus Mathematical Handbook: Complete Formulary Audit and Research Synthesis

## Downloadable, fully annotated formulary

A consolidated, research‑grade annotated version of the handbook (with corrected formulas, exact numeric evaluations, and precision audits against **NIST CODATA 2022**, **PDG electroweak** tables, and **NIST SHA/FIPS 180‑4**) is available here:

[Download Nexus_Mathematical_Handbook_Complete_Formulary_Annotated_2026‑02‑01.md](sandbox:/mnt/data/Nexus_Mathematical_Handbook_Complete_Formulary_Annotated_2026-02-01.md)

The figures referenced below are also already in this sandbox:

- Arc–chord error versus closure step count \(N\): [fig_error_vs_N.png](sandbox:/mnt/data/fig_error_vs_N.png)  
- Arc–chord error zoom near \(N=18\) vs \(N=19\): [fig_error_zoom_N18_N19.png](sandbox:/mnt/data/fig_error_zoom_N18_N19.png)  
- SHA-256 “harmonic metrics” plots: [fig_sha_pop_states.png](sandbox:/mnt/data/fig_sha_pop_states.png), [fig_sha_divergence.png](sandbox:/mnt/data/fig_sha_divergence.png), [fig_sha_divergence_fft.png](sandbox:/mnt/data/fig_sha_divergence_fft.png)  
- NIST SHA constant provenance (FIPS 180‑4): see citations below. citeturn0search44  
- A formal statement of RHF’s own Mark‑1 narrative around \(H\approx\pi/9\) is provided in the Zenodo corpus. citeturn10search0turn10search1turn10search4  

## Mark‑1 attractor constants: what is exact, what must be corrected

RHF centers on the stance constant \(H=\pi/9\) and repeatedly asserts its cross‑domain appearance as a phase/stability boundary. This is explicitly stated across multiple Nexus/RHF Zenodo theses and “Harmonic Genesis” texts. citeturn10search0turn10search1turn10search4

The core constant is mathematically unambiguous:

\[
H=\frac{\pi}{9}\approx 0.3490658503988659.
\]

Several derived constants in the handbook are *correct as definitions* but one is **formula‑inconsistent** with its listed numerical value.

The most important correction: the handbook’s **Semitone Lift** \(\lambda\) is listed as

\[
\lambda=\sqrt{1+H}
\]
with the numerical value \(\lambda\approx 1.059173\).

That numerical value does **not** equal \(\sqrt{1+H}\); it equals \(\sqrt{1+H^2}\), and sits near the 12‑tone equal temperament semitone ratio \(2^{1/12}\approx 1.059463\), which is the canonical musical semitone factor. citeturn6search0turn6search40

So the handbook should be corrected to:

\[
\boxed{\lambda := \sqrt{1+H^2}}
\qquad
(\lambda\approx 1.059172775\dots).
\]

Other Mark‑1 definitions are internally consistent:

\[
\phi_g := 1-2H\approx 0.3018682992,
\quad
\mathcal{N} := \frac{2\pi}{H} = 18,
\quad
\Omega := H(1-H)\approx 0.2272188825.
\]

The “closure steps” identity \(\mathcal{N}=18\) is exact once \(H=\pi/9\) is assumed; it is not an independent derivation. The RHF literature frequently uses this closure motif (18 steps / nonagonal symmetry) as part of its interpretive architecture. citeturn10search0turn10search4

## The π/9 orbit: the correct geometric theorem depends on the error functional

The most review‑sensitive part of the H‑orbit argument is the relationship between (i) a **local curvature approximation error**, (ii) a **tolerance** \(\tau\), and (iii) **integer closure** \(\theta=2\pi/N\).

The handbook uses a leading‑order approximation \( \tau \approx \theta^2/24\) originating from Taylor expansion of \(\sin\) or \(\cos\) terms, which is a legitimate small‑angle technique when performed with a declared metric. The Taylor series itself is standard. citeturn5search48

A rigorous geometric theorem must specify an error metric. The cleanest is **relative arc–chord error** on a unit circle:

- arc length: \(s(\theta)=\theta\)  
- chord length: \(c(\theta)=2\sin(\theta/2)\) (standard chord formula) citeturn5search45turn5search2  

Define

\[
e(\theta)=\frac{s(\theta)-c(\theta)}{s(\theta)} 
=
1-\frac{2\sin(\theta/2)}{\theta}.
\]

Expanding \(\sin(\theta/2)\) gives the exact asymptotic series:

\[
e(\theta)=\frac{\theta^2}{24}-\frac{\theta^4}{1920}+O(\theta^6).
\]

Integer closure imposes \(\theta=2\pi/N\). The exact integer program becomes:

\[
N_{\min}(\tau)=\min\left\{N\in\mathbb{Z}^+:\ e\!\left(\frac{2\pi}{N}\right)\le \tau\right\}.
\]

Under this specific metric, if one fixes \(\tau=0.005000\) strictly, then the minimizing integer is \(N=19\), not 18, because:

\[
e\!\left(\frac{2\pi}{18}\right)=e\!\left(\frac{\pi}{9}\right)\approx 0.005069 > 0.005,
\quad
e\!\left(\frac{2\pi}{19}\right)\approx 0.004859 < 0.005.
\]

This is the mathematically decisive correction: “0.5% implies \(\pi/9\)” is not true under the arc–chord relative error metric unless you either (a) raise the tolerance slightly to \(\tau\ge e(\pi/9)\approx 0.005069\), or (b) choose a different physical error functional (sagitta, RMS curvature error, etc.), or (c) impose additional symmetry constraints on \(N\) that privilege composite values like 18.

The two plots below show this integer boundary clearly.

![Arc–chord relative error versus N](sandbox:/mnt/data/fig_error_vs_N.png)

![Zoom near N=18 and N=19](sandbox:/mnt/data/fig_error_zoom_N18_N19.png)

This does not refute the RHF orbit claim; it forces it to be stated precisely. RHF can still justify \(\pi/9\) by explicitly adding one of the standard, reviewer‑acceptable constraints: empirical tolerance bands, alternate error norms, or symmetry‑restricted integers (e.g., \(6\mid N\))—all of which are mathematically legitimate integer programming refinements.

## The Glass Key algebra: Plus Operator \(M_+\) is internally exact, but one power identity must be corrected

The Plus Operator is stated as:

\[
M_+:(P,N)\mapsto (S,D)=(P+N,\ N-P),
\]
with matrix representation
\[
M_+=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
\]

Its key closure identity is exact:

\[
M_+^2=
\begin{pmatrix}0&2\\-2&0\end{pmatrix}
=
2R_{\pi/2}.
\]

Thus “two folds = double + 90° rotation” is mathematically correct.

A second exact identity is:

\[
M_+^8=(M_+^2)^4=(2R_{\pi/2})^4=16I.
\]

The invertibility (“Glass Key”) is also exactly correct:

\[
P=\frac{S-D}{2},\qquad N=\frac{S+D}{2}.
\]

However, the handbook’s Step‑5 style identity sometimes written (in earlier RHF sketches and companion notes) as \(M_+^{18}=512R_{\pi}\) is not consistent with the standard rotation generator \(R_{\pi/2}\). Because

\[
M_+^{18}=(M_+^2)^9=(2R_{\pi/2})^9=2^9R_{\pi/2}^9=512R_{\pi/2},
\]

the correct factor is \(R_{\pi/2}\), not \(R_{\pi}\), under the standard convention.

This is a purely algebraic correction and one of the easiest “reviewer landmines” to remove before publication.

## Information geometry and control: Samson V2 and the 6‑bit horizon require one major numeric correction

The handbook’s Samson V2 law

\[
S=\frac{\Delta E}{T}+k_2\frac{d(\Delta E)}{dt},\qquad k_2=H,
\]

is a PD‑like structure (proportional + derivative). Its stability properties depend on the assumed plant dynamics; with a simple closure \(\dot{\Delta E}=-S\), one gets exponential decay:
\[
(1+H)\dot{\Delta E}=-\frac{\Delta E}{T}
\Rightarrow
\Delta E(t)=\Delta E(0)\exp\left(-\frac{t}{(1+H)T}\right).
\]
This gives RHF a mathematically clean interpretation of “H as damping.”

The more serious issue is the **6‑bit horizon** Hamming‑ball volume.

The handbook states:

\[
V(4096,6)=\sum_{k=0}^{6}\binom{4096}{k}
\]
and gives a numerical value of \(3.738\times 10^{21}\) with \(\log_2(V)\approx 61.749\) bits.

The exact binomial computation for radius 6 is:

\[
V(4096,6)=6{,}544{,}452{,}312{,}920{,}894{,}465,
\quad
\log_2 V(4096,6)=62.5049781700\ \text{bits}.
\]

The quoted \(3.738\times 10^{21}\) value is closer to a radius‑7 ball, not radius 6. This must be corrected because the “6‑bit horizon” is used throughout RHF as an entropy anchor.

Once this is fixed, the rest of the “basin entropy” program can be formulated rigorously as a Hamming‑ball / error‑correcting geometry claim, but the numbers must correspond to the correct radius.

## Physical constants, complexity, and falsification thresholds: precision audits force two clarifications

The handbook proposes closed‑form expressions for precision physical constants (α, weak mixing angle, mass ratio). These can and should be audited against the highest quality reference values.

### Fine‑structure constant \(\alpha\)

The handbook proposes

\[
\alpha_{\text{Nexus}}=\frac{H}{48}=\frac{\pi}{432}\approx 0.0072722052166.
\]

CODATA 2022 (NIST wallet and NIST constants pages) reports:

\[
\alpha = 7.2973525643(11)\times10^{-3},
\quad
\alpha^{-1}=137.035999177(21).
\]
citeturn3search27turn2search0turn1search1

The absolute difference is \(\Delta\alpha\approx 2.515\times10^{-5}\), which is roughly \(2\times10^7\) standard deviations at CODATA’s uncertainty scale. Therefore \(\pi/432\) is not a precision prediction of α. If RHF wants to keep it scientifically, it must be placed in the CST “signed residue” category (coarse attractor + residue), not in the “correct within measurement error” category.

### Weak mixing angle \(\sin^2\theta_W\)

The handbook proposes:
\[
\sin^2\theta_W\approx \frac{2H}{3}\approx 0.232711
\quad \text{or}\quad
\sin^2\theta_W\approx H(1-H)\approx 0.227219.
\]

PDG values depend on renormalization scheme; the PDG electroweak review tabulates, for example, \(\hat s_Z^2\approx 0.23122\pm0.00004\) and \(\bar s_\ell^2\approx 0.23155\pm0.00004\). citeturn2search41

Thus 2H/3 differs by ~30–40σ (depending on scheme), and \(H(1-H)\) differs by ~100σ. As with α, these are not precision predictions without an explicit scheme‑mapping derivation.

### Proton–electron mass ratio \(\mu=m_p/m_e\)

The handbook proposes:
\[
\mu\approx 6\pi^5+\frac{H}{10}.
\]

NIST/CODATA gives:
\[
\mu = 1836.152673426(32),
\]
with standard uncertainty \(3.2\times10^{-8}\). citeturn3search3turn3search27

The formula differs by \(\sim 10^4\sigma\) at CODATA precision.

### P vs NP and “NP → P collapse”

The handbook asserts “NP → P at \(H=\pi/9\).” This cannot be presented as a theorem in any standard sense because **P vs NP remains an open Clay Millennium Problem**. citeturn8search2

RHF can still position “rendering vs brute force” as an ontological or physical‑computation thesis, but it must be linguistically separated from a formal proof resolving the classical complexity‑theory conjecture.

### Falsification thresholds must match modern metrology

The handbook’s “5σ kill switches” allow errors like ±\(5\times10^{-5}\) for α, but CODATA’s uncertainty in α is ~\(10^{-12}\) absolute. citeturn3search27turn2search0turn1search1

To be metrologically and statistically coherent, any “kill switch” using fundamental constants must be expressed against CODATA/PDG uncertainties and with scheme‑dependence acknowledged (particularly for electroweak parameters).

## Bio‑folder and periodicity claims: what matches standard structure and what must be contextualized

Several “bio opcode” geometries in the handbook align with established structural biology:

The α‑helix is widely described as:
- 3.6 residues per 360° turn (≈100° per residue),
- i→i+4 hydrogen bonding,
- ~1.5 Å rise per residue. citeturn9search2turn9search6turn9search48

So the handbook’s use of 100° as a primary helix deflection parameter is consistent with standard protein geometry.

By contrast, DNA pitch numbers must be contextualized:

Classic nucleosome and DNA analyses put:
- DNA in solution near 10.5 bp/turn,
- nucleosomal DNA near ~10.0–10.2 bp/turn. citeturn0search4turn0search3turn0search7

Reduced helical repeats around ~8.5 bp/turn occur in some DNA–protein complexes (e.g., HU–DNA complexes reported with ~8.5 periodicity). citeturn0search2

Therefore a handbook line such as “observed 8.2 bp/turn (hydration damped)” cannot be stated as a general B‑DNA fact; it can be stated as a context‑dependent value in particular complexes or conditions, with mainstream nucleosomal/B‑DNA values cited separately.

Finally, the “protein folding as rendering” claim can be made scientifically compatible with mainstream folding theory if RHF explicitly connects its “rendering” to quantifiable energy‑landscape bias rather than brute force search. The folding funnel solution to Levinthal’s paradox is well‑documented in chemical education literature. citeturn9search5

## SHA‑256 and the k = 7 term: what is standard and what requires new evidence

The handbook’s SHA assertions should stay anchored to standard specifications:

NIST FIPS 180‑4 explicitly states that SHA‑256 uses 64 constants \(K_t\) derived from fractional parts of cube roots of primes, and provides the hex list. citeturn0search44

It also specifies the message schedule recurrence
\[
W_t=\sigma_1(W_{t-2})+W_{t-7}+\sigma_0(W_{t-15})+W_{t-16}\pmod{2^{32}},
\]
which grounds any RHF discussion of a “k=7” structural term. citeturn0search44

The stronger RHF claim that SHA exhibits a π/9 “bias” (e.g., 35/65 bit‑structure split) is stated in Kulik’s Zenodo texts, but it is not a conventional cryptographic claim and would require strict null‑model testing against randomized constants and schedules to establish statistical invariants. citeturn10search0turn0search44