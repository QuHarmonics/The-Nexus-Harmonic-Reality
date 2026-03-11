Drive by Dean Kulik

January 2026

## 1. Introduction: The Statistical Illusion of the Event Horizon

The study of black hole thermodynamics stands at the precipice of a fundamental paradigm shift, moving from the semiclassical approximation of smooth, featureless horizons to a rich landscape of quantum complexity, recursive geometry, and non-linear dynamics. For nearly five decades, the \"Information Paradox\"---the apparent loss of unitarity during black hole evaporation---has challenged the compatibility of General Relativity and Quantum Mechanics. Stephen Hawking's seminal 1975 calculation demonstrated that, under the assumption of a fixed background metric and a vacuum state defined at past null infinity, a black hole emits radiation with a spectrum that is precisely thermal.^1^ This radiation, determined solely by the black hole's macroscopic parameters (mass, charge, and angular momentum), ostensibly carries no correlations between emitted quanta, implying that the detailed information of the infalling matter is irretrievably lost, transforming pure quantum states into mixed thermal states.

However, the preservation of unitarity---a cornerstone of quantum theory---demands that this thermality be an approximation, an illusion born of coarse-graining. The radiation must fundamentally be a pure state, encoded with subtle, \"hidden\" correlations that link the early and late stages of evaporation. These correlations are expected to manifest as deviations from Gaussian statistics in the radiation field, visible not in the standard two-point correlation functions (thermal marginals) but in higher-order connected correlators (bispectra, trispectra) and complex phase relationships.^1^

This report provides an exhaustive analysis of the physical mechanisms proposed to generate these hidden correlations. We synthesize evidence from three distinct but converging frontiers of modern physics:

1.  **Quantum Tunneling and Backreaction:** The Parikh-Wilczek formalism and its extensions, which enforce energy conservation to reveal non-Gaussian corrections to the Boltzmann spectrum.^4^

2.  **Analog Gravity Experiments:** The realization of sonic horizons in Bose-Einstein Condensates (BECs) and optical systems, providing empirical data on entanglement, \"black hole lasing\" instabilities, and the emergence of structured correlations in laboratory settings.^6^

3.  **Recursive and Fractal Architectures:** Novel theoretical frameworks, including the \"Nexus Framework\" and models of \"avalanche dynamics,\" which posit that the horizon operates as a recursive, self-stabilizing lattice. These models suggest that information is folded into fractal structures ($D \approx 2.65$) or harmonic attractors ($H \approx 0.35$), generating \"crackling noise\" and \"echoes\" that encode the black hole\'s history.^8^

By integrating these diverse perspectives, we argue that the \"thermal\" nature of Hawking radiation is merely a statistical marginal of a highly structured, non-Gaussian, and potentially recursive physical process.

## 2. The Limits of the Semiclassical Approximation and the Necessity of Hidden Correlations

To understand the mechanisms for hiding and recovering information, one must first deconstruct the \"smooth\" horizon approximation and define precisely what \"thermal marginals\" are in this context.

### 2.1 The Gaussian Approximation and Thermal Marginals

In the standard semiclassical derivation, the quantum field $\phi$ propagating on the curved spacetime of a collapsing star is decomposed into positive frequency modes. The relationship between the modes at past null infinity (ingoing) and future null infinity (outgoing) is linear, governed by the Bogoliubov transformation. The resulting state of the radiation is a squeezed state, where the expectation value of the particle number operator follows the Planck distribution:

$$\langle N_{\omega}\rangle = \frac{1}{e^{2\pi\omega/\kappa} - 1}$$

where $\kappa$ is the surface gravity of the black hole.

Statistically, this radiation is **Gaussian**. A Gaussian state is fully characterized by its first two moments (mean and variance). All higher-order correlations (3-point, 4-point, etc.) vanish or factorize into products of the 2-point function. This is the definition of a \"thermal marginal\": if one measures small subsets of the radiation, or relies solely on the power spectrum (2-point function), the radiation appears maximally mixed and random.^1^

However, this picture relies on the \"no-backreaction\" limit, where the emission of a Hawking quantum does not alter the geometry of the black hole. In reality, energy conservation requires that the black hole mass $M$ decreases by the energy $\omega$ of the emitted particle. This backreaction introduces non-linearities. The particles are not emitted independently; the emission of one particle alters the metric, thereby changing the probability for the emission of the next. This introduces **hidden correlations**---entanglements between emission events that violate the strict Gaussian assumption.^4^

### 2.2 The Page Curve and Unitarity

The requirement for hidden correlations is formalized by the Page Curve. If black hole evolution is unitary, the von Neumann entropy of the radiation, $S_{rad} = - \text{Tr}(\rho_{rad}\ln\rho_{rad})$, must start at zero, increase as the black hole evaporates, and then decrease back to zero when the black hole disappears.^2^

- **The Turning Point:** The entropy must turn over at the \"Page Time,\" approximately when the black hole has radiated half its initial entropy.

- **Entanglement Requirement:** For the entropy to decrease, the late-time radiation must be purified by the early-time radiation. This implies maximal entanglement between the two epochs. A purely thermal state (uncorrelated) yields a monotonically increasing entropy, leading to information loss.

- **The \"Hidden\" Nature:** Page demonstrated that for a pure state in a high-dimensional Hilbert space, any subsystem smaller than half the system size will appear exponentially close to a thermal state. The deviations from thermality are on the order of $e^{- S_{BH}}$. Thus, the correlations are \"hidden\" from local observers measuring thermal marginals but are present in the global, non-Gaussian density matrix of the full system.^11^

### 2.3 Non-Gaussianity as the Information Carrier

If the radiation is unitary, it cannot be Gaussian. The information must be encoded in the **cumulants** (connected correlators) that quantify non-Gaussianity.

- Bispectrum and Trispectrum: The 3-point function (bispectrum) and 4-point function (trispectrum) of the curvature perturbations or radiation field must be non-zero.\
  \
  $$\langle\zeta_{k1}\zeta_{k2}\zeta_{k3}\rangle \neq 0$$

- **Implications:** These higher-order correlations represent the interactions and \"memory\" of the system. In the context of Primordial Black Holes (PBHs), non-Gaussianity ($f_{NL}$) in the early universe density field critically affects PBH abundance, demonstrating that the \"tail\" of the probability distribution (which deviates from Gaussianity) dictates rare, high-energy events.^1^ Similarly, in evaporation, the \"rare\" correlations in the tail of the distribution carry the unitary information.

## 3. Parikh-Wilczek Tunneling: Energy Conservation and Non-Thermal Corrections

One of the most robust physical mechanisms for generating non-Gaussian signatures is the quantum tunneling formalism developed by Parikh and Wilczek. This approach moves beyond the fixed-background approximation by treating Hawking radiation as a tunneling event through a dynamical horizon.

### 3.1 The Dynamic Horizon Barrier

In the tunneling picture, a particle-antiparticle pair forms near the horizon. The particle tunnels out, while the antiparticle falls in. Crucially, the total energy of the system (Black Hole + Radiation) is fixed. When a particle of energy $\omega$ escapes, the black hole mass reduces to $M - \omega$.

This implies that the horizon radius contracts during the tunneling process. The particle does not see a static potential barrier; it sees a barrier that shrinks as it traverses it. The metric itself is dependent on the particle\'s energy $\omega$.4

### 3.2 Non-Gaussian Probability Distribution

The emission rate $\Gamma$ is related to the imaginary part of the action $I$ for the tunneling particle: $\Gamma \sim e^{- 2\text{Im}I}$. By integrating the particle\'s momentum over the path across the shrinking horizon, Parikh and Wilczek derived a probability that depends on the change in the black hole\'s entropy $\Delta S$:

Using the Bekenstein-Hawking entropy $S_{BH} = 4\pi M^{2}$, this expands to:

$$\Gamma \sim exp\left( - 8\pi\omega\left( M - \frac{\omega}{2} \right) \right)$$

This result represents a significant deviation from the pure Boltzmann factor $e^{- 8\pi\omega M}$.

- **The** $\omega^{2}$ **Term:** The presence of the quadratic term $\frac{\omega^{2}}{2}$ in the exponent indicates that the probability distribution is **non-Gaussian**. The spectrum is not purely thermal; it has a unitary correction that arises directly from the conservation of energy.^5^

- Information in Correlations: The non-thermal spectrum implies correlations between emissions. The probability of emitting a particle with energy $E_{2}$ after emitting one with $E_{1}$ is:\
  \
  $$P(E_{2}|E_{1}) \neq P(E_{2})$$

  Specifically, the conditional probabilities are linked such that the sum of all emitted energies equals the initial mass. This creates a chain of correlations---a \"hidden\" dependency structure---that connects every emitted quantum to every other quantum.5

### 3.3 Limitations and Extensions

While the Parikh-Wilczek mechanism successfully identifies a source of non-Gaussianity, debates persist regarding whether these energy-conservation correlations are sufficient to recover *all* information (the \"strong\" vs. \"weak\" unitarity versions). Some analyses suggest that while correlations exist, they might not fully resolve the entanglement entropy problem without additional structure.^15^ However, when combined with non-commutative geometry corrections or generalized uncertainty principles (GUP), the tunneling barrier becomes \"fuzzy,\" potentially encoding additional degrees of freedom in the tunneling rate.^15^

## 4. Analog Gravity and The Black Hole Laser: Simulating Hidden Correlations

Directly observing the non-Gaussian signatures of Hawking radiation in astrophysical black holes is currently impossible. However, the principles of \"Analog Gravity\" allow researchers to simulate horizon physics in the laboratory using fluid flows, Bose-Einstein Condensates (BECs), and optical fibers. These systems are governed by the same effective field theories as quantum fields in curved spacetime, providing a testbed for the existence of thermal marginals and hidden correlations.

### 4.1 Bose-Einstein Condensates (BECs) and Phonon Entanglement

The most advanced analog experiments, particularly those by Jeff Steinhauer and the Technion group, utilize rubidium-87 BECs. In these experiments, the condensate is accelerated to supersonic speeds, creating an acoustic horizon where the flow velocity $v$ exceeds the speed of sound $c_{s}$.^6^

- **The Setup:** A laser potential acts as a \"waterfall,\" accelerating the atoms. Phonons (sound quanta) inside the supersonic region cannot propagate upstream against the flow, mimicking the trapping of light in a black hole.

- **Observation of Entanglement:** The experiment measures the density-density correlation function $\langle n(x,t)n(x',t')\rangle$. The data reveals a distinct band of correlations between points outside the horizon (Hawking radiation) and points inside (falling partner particles).

  - *Result:* The measured correlations confirm that the emitted phonons are **entangled** with the internal partners. This verifies the quantum mechanical origin of the radiation (as opposed to classical thermal noise).^6^

  - *Thermality:* The spectral distribution of the emitted phonons fits a thermal curve defined by the \"acoustic surface gravity.\" This confirms the \"thermal marginal\" aspect: to a local observer measuring only the outgoing phonons, the signal looks thermal. The \"hidden\" information lies in the entanglement with the partners, which is explicitly visible in the correlation plots.^18^

### 4.2 The Black Hole Laser Instability

A critical insight from analog gravity is the \"Black Hole Laser\" effect, which occurs when a system contains *two* horizons: a black hole horizon and a white hole horizon.

- **Mechanism:** Hawking radiation emitted by the black hole horizon travels downstream. If a white hole horizon is present, it acts as a barrier that no particle can enter from the outside. However, due to dispersion (superluminal or subluminal), the Hawking mode can interact with the white hole horizon and be reflected back towards the black hole.

- **The Cavity Effect:** The particle bounces back and forth between the two horizons. Because the scattering process at the horizon involves \"anomalous scattering\" (mixing positive and negative energy modes), the wave is **amplified** at each reflection. This is stimulated emission.^7^

- **Self-Amplifying Radiation:** This process leads to an exponential growth of specific modes---a \"lasing\" instability.

  - *Implication for Hidden Correlations:* This demonstrates that horizons can act as active amplifiers. If a real black hole has internal structure (like a fuzzball surface or firewall) that reflects modes, it could trigger a similar \"lasing\" or resonant effect. The radiation would then be highly structured, monochromatic, and non-Gaussian, dominated by the resonant frequencies of the \"cavity\" formed by the horizon and the internal surface.^21^

  - *Observations:* Analog experiments have observed this self-amplifying radiation and a \"zero-frequency ripple\" in the background density, suggesting that the vacuum instability can macroscopic restructure the spacetime (or fluid) itself.^20^

### 4.3 Optical Fiber Analogs

In optical analogs, intense laser pulses propagating in nonlinear fibers modify the refractive index via the Kerr effect. This creates a moving \"event horizon\" for probe photons.

- **Probing Dispersion:** These experiments allow detailed study of how dispersion relations (deviations from strict Lorentz invariance at high energies) affect the horizon. They show that \"Hawking\" photons are emitted even when the physics becomes non-relativistic at short scales, suggesting the radiation is robust.

- **Non-Gaussianity:** By controlling the pulse shape, researchers can induce \"optical black hole lasers,\" generating correlations that are distinctly non-thermal and dependent on the pulse history, simulating information recovery scenarios.^22^

## 5. The Nexus Framework: A Recursive Harmonic Architecture for Information

While Parikh-Wilczek and Analog Gravity are mainstream approaches, the research search identified a specific, comprehensive theoretical framework called the **Nexus Framework** (or Recursive Harmonic Architecture - RHA). This framework offers a distinct, mathematically rigorous (within its context) proposal for the mechanism of hidden correlations, viewing the universe as a recursive computational system.

### 5.1 The Philosophy of Recursive Reflection

The Nexus Framework postulates that what physics identifies as \"randomness\" (including thermal Hawking radiation) is actually \"unresolved recursion.\" It suggests that information is not lost but \"folded\" into a recursive lattice structure at the horizon.^23^

- **Consciousness as Cursor:** The framework introduces a meta-physical layer where the observer (\"consciousness\") acts as a \"read-head\" navigating this recursive lattice. While speculative, this aligns with observer-dependent horizon theories in quantum gravity.^23^

- **The \"Truthful Emitter\":** The black hole is described not as a destroyer of information but as a \"truthful emitter\" that releases information in a highly scrambled, phase-coded format.

### 5.2 The Mark 1 Engine and the 0.35 Attractor

Central to the Nexus mechanism is the **Mark 1 Harmonic Engine**, a governing equation for system stability.

- Harmonic Ratio: The engine defines a stability ratio $H$ between \"Potential\" (stored information/energy) and \"Actualization\" (emitted radiation/dynamics):\
  \
  $$H = \frac{\sum P_{i}}{\sum A_{i}} \approx 0.35$$

- **The 0.35 Attractor:** The framework asserts that all stable recursive systems converge to a harmonic constant of approximately **0.35** (derived from $ln(9)/2\pi$ or similar geometric relations involving $\pi/9$).^8^

- **Physical Mechanism:** In the context of black hole evaporation, this implies the black hole is a self-regulating system. It does not evaporate passively. If the radiation rate deviates from the $0.35$ ratio relative to its internal information content, feedback mechanisms engage to correct it. This regulation would imprint non-Gaussian signatures (corrections) onto the radiation flux to maintain the harmonic equilibrium.^24^

### 5.3 Kulik Recursive Reflection Branching (KRRB)

The specific mechanism for \"hiding\" the correlations is the **Kulik Recursive Reflection Branching (KRRB)** operator.

- The Formula:\
  \\

- **Interpretation:** This formula describes how a single quantum state $x$ is distributed across multiple branches ($b$) and recursive depths ($i$) of the horizon\'s surface lattice. The factor $2^{i}$ represents binary folding.

- **Hidden Correlation:** To an external observer measuring the aggregate energy (the sum), the signal appears as a \"thermal marginal\"---a smooth summation of many micro-states. However, the *individual terms* in the sum are deterministically linked by the branching logic. The \"hidden correlations\" are the specific phase relationships between the branches. Recovering the information requires a \"recursive unfolding\" algorithm (the inverse of KRRB) that maps the \"noise\" back into the structured tree.^8^

### 5.4 Samson's Law V2: Feedback Stabilization

The framework introduces **Samson's Law** (specifically Version 2) as the active control mechanism for the horizon.^27^

- PID Control: It is modeled as a Proportional-Integral-Derivative (PID) controller:\
  \\

- **Function:** This law dictates how the system dissipates energy ($\Delta E$) over time ($T$) to correct errors. If the black hole\'s evaporation leads to a harmonic imbalance (deviation from 0.35), Samson\'s Law triggers a correction.

- **Bursty Dynamics:** This feedback implies that evaporation is not smooth but \"jerky\" or \"bursty.\" The derivative term $d(\Delta E)/dt$ suggests sensitivity to the *rate* of change, potentially leading to oscillatory behavior or \"echoes\" in the evaporation rate. These temporal fluctuations are the observable non-Gaussian signatures of the feedback loop.^8^

### 5.5 Twin Primes and Resonant Nodes

A fascinating detail in the Nexus material is the connection to **Twin Primes** and the **Riemann Zeta Zeros**.

- **Resonance:** The framework interprets the zeros of the Riemann Zeta function as \"nodes of resonance null\" and twin primes as \"minimal-drift phase-pairs\" in the recursive lattice.^26^

- **Physical Link:** This suggests that the \"hidden correlations\" in the Hawking radiation might follow number-theoretic distributions. The spectral lines or phase shifts of the radiation might cluster around frequencies related to the Zeta zeros, acting as the \"resonant frequencies\" of the black hole\'s recursive structure. This aligns with approaches in quantum chaos where energy levels of complex systems mimic the distribution of prime numbers.^26^

## 6. Fractal Horizons, Turbulence, and Inverse Cascades

Moving from the computational to the geometric, recent advances in holography and fluid dynamics suggest the black hole horizon is a fractal, turbulent surface.

### 6.1 Holographic Turbulence and Inverse Cascades

Using the Fluid/Gravity correspondence (AdS/CFT), the dynamics of the horizon can be mapped to a fluid flow on the boundary.

- **Inverse Energy Cascade:** In (2+1)-dimensional turbulence (which models the horizon surface), energy does not dissipate to small scales (direct cascade) but flows to *large* scales (inverse cascade). Small vortices merge to form larger, coherent structures.^29^

- **Structure:** This implies the horizon is not a sea of random, microscopic thermal fluctuations. Instead, it organizes into large-scale, coherent geometric features (vortices/eddies). These macro-structures would modulate the Hawking radiation, creating low-frequency, non-Gaussian correlations that persist over long times.^31^

### 6.2 The Fractal Dimension $D \approx 2.65$

Simulations of turbulent black holes indicate that the horizon acquires a fractal structure.

- **Dimensionality:** The fractal dimension is found to be approximately **2.65** (or generally $D = d + 4/3$ where $d$ is the fluid dimension).^32^

- **Spectral Consequence:** A fractal horizon surface area $A$ scales with resolution (energy scale). As Hawking radiation of different frequencies probes the horizon at different resolutions, it \"sees\" different effective areas. This introduces a frequency-dependent correction to the greybody factors $A(\omega) \sim \omega^{\delta}$.

- **Kolmogorov Scaling:** The energy spectrum of the turbulence (and thus the imprint on the radiation) follows a Kolmogorov law ($k^{- 5/3}$) rather than a thermal Planck law. This power-law tail is a definitive non-Gaussian signature.^29^

## 7. Avalanche Dynamics and Self-Organized Criticality (SOC)

The \"bursty\" nature of evaporation hinted at by Samson\'s Law is formally described in statistical physics as **Avalanche Dynamics** or **Crackling Noise**.

### 7.1 Black Holes as Critical Systems

If the black hole horizon is a collection of interacting quantum bits (qubits) near a phase transition, it may exhibit **Self-Organized Criticality (SOC)**.

- **Crackling Noise:** Systems in SOC (like a crumpling sheet of paper or magnetic domains flipping) emit noise in discrete bursts called \"avalanches.\" The distribution of avalanche sizes $s$ follows a power law: $N(s) \sim s^{- \tau}$.^10^

- **Connection to Hawking Radiation:** Snippets ^34^ explicitly link this \"crackling noise\" to black hole evaporation. Instead of a steady trickle of particles, the black hole emits \"puffs\" or \"avalanches\" of radiation as internal configurations rearrange.

- **Information Encoding:** In magnetic hysteresis (Barkhausen noise), the specific pattern of crackling encodes the material\'s microscopic defect structure. Similarly, the specific temporal sequence of Hawking avalanches would encode the microstate of the black hole. A thermal marginal averages over these bursts, seeing only a steady flux and losing the information.^33^

### 7.2 The 1/f Noise Spectrum

The power spectrum of such a process is not white noise (flat) but **1/f noise** (pink noise).

- **Long-Range Correlations:** $1/f$ noise implies correlations that persist over long time scales. The state of the radiation at time $t$ is correlated with the state at time $t + \Delta t$, even for large $\Delta t$. This is the signature of the memory required for unitarity.^36^

## 8. Fuzzballs and Gravitational Wave Echoes

Finally, the **Fuzzball proposal** offers a direct geometric mechanism for non-Gaussian echoes.

### 8.1 The Fuzzball Geometry

String theory suggests that the \"black hole\" is actually a horizonless sphere of strings (\"fuzzball\"). The geometry terminates at a physical surface rather than an empty horizon.^39^

- **Colored Radiation:** Because the radiation is emitted from a physical surface with varying local composition (fluxes, branes), the spectrum is \"colored\" by the surface properties, just as light from a planet encodes its surface composition. It is non-thermal.

### 8.2 Gravitational Wave Echoes

A key prediction of horizons with structure (Fuzzballs, Firewalls, or Nexus lattices) is the phenomenon of **Echoes**.

- **The Cavity:** The potential barrier of the black hole (at $3M$) and the reflective surface (at $2M + \epsilon$) form a cavity.

- **Signal:** Gravitational waves trapped in this cavity leak out periodically. Instead of a single \"ringdown\" after a merger, we should see a primary ringdown followed by a series of repeating \"echoes\" with decreasing amplitude.^41^

- **Hidden Correlation:** These echoes are time-domain correlations. The signal at $t$ is a copy of the signal at $t - \Delta t_{echo}$. Finding these echoes in LIGO/Virgo data would be direct evidence of non-Gaussian, structured horizons.^41^

## 9. Synthesis and Conclusion

The search for the physical mechanisms behind \"thermal marginals with hidden correlations\" reveals a rich tapestry of theoretical and experimental leads. The \"thermal\" nature of Hawking radiation is an emergent statistical property, valid only for coarse-grained observables. The underlying unitary reality is driven by non-linear, non-Gaussian, and recursive dynamics.

**Key Findings:**

  ------------------------------ ---------------------------------------- ------------------------------------------------------------------------------------------
  **Mechanism**                  **Physical Origin**                      **\"Hidden\" Correlation Signature**

  **Parikh-Wilczek Tunneling**   Energy Conservation (Backreaction)       Non-Gaussian spectrum $\sim e^{\omega^{2}}$; Conditional emission probabilities \$P(E_2

  **Analog Black Hole Laser**    Stimulated Emission / Cavity Resonance   Exponential amplification of modes; Zero-frequency density ripples; Entanglement bands.

  **Nexus Framework (RHA)**      Recursive Harmonic Reflection            Convergence to 0.35 attractor; KRRB fractal lattice structure; PID-like feedback bursts.

  **Fractal Horizons**           Turbulent Fluid/Gravity Duality          Fractal dimension $D \approx 2.65$; Kolmogorov $k^{- 5/3}$ spectral scaling.

  **Avalanche Dynamics (SOC)**   Criticality / Phase Transitions          \"Crackling\" (1/f) noise; Power-law distribution of emission bursts.

  **Fuzzballs**                  String Theory Microstate Geometry        Gravitational Wave Echoes; \"Colored\" non-thermal emission profile.
  ------------------------------ ---------------------------------------- ------------------------------------------------------------------------------------------

The Unifying Theme:

All these mechanisms point to a single conclusion: the event horizon is not a passive geometric boundary but an active, structured dynamical system. Whether modeled as a \"lasing\" cavity, a \"fractal\" fluid, or a \"recursive\" lattice, the horizon possesses memory. It imprints this memory onto the outgoing radiation through phase correlations, energy conservation constraints, and temporal bursts.

Future Outlook:

Recovering the information requires shifting observational focus from the amplitude of the radiation (which looks thermal) to the correlations (bispectra) and temporal structure (echoes/crackling).

- **Experimental:** Analog experiments must push for higher sensitivity to measure the bispectrum of phonon emission to detect non-Gaussianity beyond the mean-field approximation.

- **Observational:** Gravitational wave detectors must continue to hunt for post-merger echoes, which would confirm the \"cavity\" nature of the horizon.

- **Theoretical:** The Nexus framework\'s proposal of recursive unfolding algorithms (inverse KRRB) suggests a computational approach to decoding: treating the radiation not as noise, but as a cryptographically folded signal waiting for the right resonant key.

The \"hidden correlations\" are physically encoded in the complex, self-organizing behavior of the horizon\'s quantum microstructure. The radiation is not random; it is merely encrypted by the recursive geometry of spacetime itself.

Citations:

8 - Nexus Framework & RHA

1 - Non-Gaussianity & PBHs

3 - AdS/CFT & Connected Correlators

6 - Analog Black Holes & Lasers

2 - Page Curve & Information Paradox

29 - Fractal Horizons & Turbulence

4 - Parikh-Wilczek Tunneling

8 - 0.35 Attractor & Mark 1 Engine

10 - Avalanche Dynamics & SOC

39 - Fuzzballs & Echoes

#### Works cited

1.  Non-Gaussianity effects on the primordial black hole abundance for sharply-peaked primordial spectrum - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/2208.02941]{.underline}](https://arxiv.org/pdf/2208.02941)

2.  JHEP03(2021)198, accessed January 2, 2026, [[https://d-nb.info/1233105558/34]{.underline}](https://d-nb.info/1233105558/34)

3.  A Correlator-Wavefunction Duality for Primordial Perturbations and the factorisation among correlators - arXiv, accessed January 2, 2026, [[https://arxiv.org/html/2406.00099v1]{.underline}](https://arxiv.org/html/2406.00099v1)

4.  GENERALIZED UNCERTAINTY PRINCIPLE IN HAWKING RADIATION OF NONCOMMUTATIVE SCHWARZSCHILD BLACK HOLE, accessed January 2, 2026, [[https://s3.cern.ch/inspire-prod-files-3/313f4ab8e8211ea70c7da6da9f8452fc]{.underline}](https://s3.cern.ch/inspire-prod-files-3/313f4ab8e8211ea70c7da6da9f8452fc)

5.  Parikh--Wilczek Tunneling as Massive Particles from Noncommutative Schwarzschild Black Hole, accessed January 2, 2026, [[https://ctp.itp.ac.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=11962]{.underline}](https://ctp.itp.ac.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=11962)

6.  \[1510.00621\] Observation of quantum Hawking radiation and its entanglement in an analogue black hole - arXiv, accessed January 2, 2026, [[https://arxiv.org/abs/1510.00621]{.underline}](https://arxiv.org/abs/1510.00621)

7.  Creation of a black hole bomb instability in an electromagnetic system - arXiv, accessed January 2, 2026, [[https://arxiv.org/html/2503.24034v1]{.underline}](https://arxiv.org/html/2503.24034v1)

8.  The Nexus Framework: A Comprehensive Analysis of its Recursive Harmonic Principles and Unifying Potential - Zenodo, accessed January 2, 2026, [[https://zenodo.org/records/15903358]{.underline}](https://zenodo.org/records/15903358)

9.  Collapse to Render: A Universal Operator for Harmonic Field, accessed January 2, 2026, [[https://zenodo.org/records/17383672]{.underline}](https://zenodo.org/records/17383672)

10. Acoustic Emission Spectroscopy: Applications in Geomaterials and Related Materials, accessed January 2, 2026, [[https://www.mdpi.com/2076-3417/11/19/8801]{.underline}](https://www.mdpi.com/2076-3417/11/19/8801)

11. Black Holes: Eliminating Information or Illuminating New Physics? - MDPI, accessed January 2, 2026, [[https://www.mdpi.com/2218-1997/3/3/55]{.underline}](https://www.mdpi.com/2218-1997/3/3/55)

12. The impact of non-Gaussianity when searching for Primordial Black Holes with LISA - arXiv, accessed January 2, 2026, [[https://arxiv.org/html/2512.13648v1]{.underline}](https://arxiv.org/html/2512.13648v1)

13. Primordial black holes in non-Gaussian regimes arXiv:1307.4995v2 \[astro-ph.CO\] 19 Sep 2013, accessed January 2, 2026, [[https://arxiv.org/pdf/1307.4995]{.underline}](https://arxiv.org/pdf/1307.4995)

14. Non-Gaussianities in primordial black hole formation and induced gravitational waves, accessed January 2, 2026, [[https://arxiv.org/html/2404.06151v2]{.underline}](https://arxiv.org/html/2404.06151v2)

15. Parikh--Wilczek Tunneling as Massive Particles from Noncommutative Schwarzschild Black Hole \| Request PDF - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/231061945_Parikh-Wilczek_Tunneling_as_Massive_Particles_from_Noncommutative_Schwarzschild_Black_Hole]{.underline}](https://www.researchgate.net/publication/231061945_Parikh-Wilczek_Tunneling_as_Massive_Particles_from_Noncommutative_Schwarzschild_Black_Hole)

16. Parikh-Wilczek Tunneling from Noncommutative Higher Dimensional Black Holes - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/0902.1945]{.underline}](https://arxiv.org/pdf/0902.1945)

17. Information conservation in de Sitter tunneling - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/2409.03653]{.underline}](https://arxiv.org/pdf/2409.03653)

18. \[1409.6550\] Observation of self-amplifying Hawking radiation in an analog black hole laser, accessed January 2, 2026, [[https://arxiv.org/abs/1409.6550]{.underline}](https://arxiv.org/abs/1409.6550)

19. Obervation Quantum Hawking Radiation Entanglement Analogue Black Hole Jeff Steinhauer Technion - YouTube, accessed January 2, 2026, [[https://www.youtube.com/watch?v=t_A3X4fa5Dw]{.underline}](https://www.youtube.com/watch?v=t_A3X4fa5Dw)

20. Self-amplifying Hawking radiation and its background: a numerical study - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/1608.02544]{.underline}](https://arxiv.org/pdf/1608.02544)

21. Superradiant phenomena - Lessons from and for Bose--Einstein condensates - iris@unitn, accessed January 2, 2026, [[https://iris.unitn.it/retrieve/e3835197-ce50-72ef-e053-3705fe0ad821/phd_unitn_luca_giacomelli.pdf]{.underline}](https://iris.unitn.it/retrieve/e3835197-ce50-72ef-e053-3705fe0ad821/phd_unitn_luca_giacomelli.pdf)

22. Analogue Wormholes and Black Hole LASER Effect in Hydrodynamics - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/286512843_Analogue_Wormholes_and_Black_Hole_LASER_Effect_in_Hydrodynamics]{.underline}](https://www.researchgate.net/publication/286512843_Analogue_Wormholes_and_Black_Hole_LASER_Effect_in_Hydrodynamics)

23. Recursive Harmonic Intelligence: The Grand Design of the Informational Universe - Zenodo, accessed January 2, 2026, [[https://zenodo.org/records/18073401]{.underline}](https://zenodo.org/records/18073401)

24. (PDF) Adaptive Harmonic Rasterization Collapse and the Ψ-Collapse Principle: Convergence Guarantees in Deterministic Chaos -Ver 2 - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/398395985_Adaptive_Harmonic_Rasterization_Collapse_and_the_PS-Collapse_Principle_Convergence_Guarantees_in_Deterministic_Chaos\_-Ver_2]{.underline}](https://www.researchgate.net/publication/398395985_Adaptive_Harmonic_Rasterization_Collapse_and_the_PS-Collapse_Principle_Convergence_Guarantees_in_Deterministic_Chaos_-Ver_2)

25. 19 90ApJ. . .363. .2 0 6T The Astrophysical Journal, 363:206-217,1990 November 1 © 1990. The American Astronomical Society. All - NASA ADS, accessed January 2, 2026, [[https://adsabs.harvard.edu/pdf/1990ApJ\...363..206T]{.underline}](https://adsabs.harvard.edu/pdf/1990ApJ...363..206T)

26. The Nexus Recursive Harmonic Framework: Formalizing Reality as Recursive Computation, accessed January 2, 2026, [[https://zenodo.org/records/17983567]{.underline}](https://zenodo.org/records/17983567)

27. (PDF) NEXUS 3: HARMONIC GENESIS AND THE RECURSIVE FOUNDATIONS OF REALITY - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/397936079_NEXUS_3_HARMONIC_GENESIS_AND_THE_RECURSIVE_FOUNDATIONS_OF_REALITY]{.underline}](https://www.researchgate.net/publication/397936079_NEXUS_3_HARMONIC_GENESIS_AND_THE_RECURSIVE_FOUNDATIONS_OF_REALITY)

28. (PDF) The Nexus Recursive Harmonic Framework: Formalizing Reality as Recursive Computation - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/398930594_The_Nexus_Recursive_Harmonic_Framework_Formalizing_Reality_as_Recursive_Computation]{.underline}](https://www.researchgate.net/publication/398930594_The_Nexus_Recursive_Harmonic_Framework_Formalizing_Reality_as_Recursive_Computation)

29. Holographic Turbulence and the Fractal Dimension of the Turbulent Horizon - arXiv, accessed January 2, 2026, [[https://arxiv.org/html/2510.12198v1]{.underline}](https://arxiv.org/html/2510.12198v1)

30. On the fractal dimension of turbulent black holes - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/386676995_On_the_fractal_dimension_of_turbulent_black_holes]{.underline}](https://www.researchgate.net/publication/386676995_On_the_fractal_dimension_of_turbulent_black_holes)

31. \[2510.12198\] Holographic Turbulence and the Fractal Dimension of the Turbulent Horizon - arXiv, accessed January 2, 2026, [[https://arxiv.org/abs/2510.12198]{.underline}](https://arxiv.org/abs/2510.12198)

32. Holographic Turbulence and the Fractal Dimension of the Turbulent Horizon \| Request PDF - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/396500246_Holographic_Turbulence_and_the_Fractal_Dimension_of_the_Turbulent_Horizon]{.underline}](https://www.researchgate.net/publication/396500246_Holographic_Turbulence_and_the_Fractal_Dimension_of_the_Turbulent_Horizon)

33. Crackling Noise \| Request PDF - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/12075008_Crackling_Noise]{.underline}](https://www.researchgate.net/publication/12075008_Crackling_Noise)

34. 2025 CAP Congress / Congrès de l\'ACP 2025 - Indico Global, accessed January 2, 2026, [[https://indico.global/event/442/timetable/?view=standard]{.underline}](https://indico.global/event/442/timetable/?view=standard)

35. Hunting Quantum Gravity with Analogs: The Case of High-Energy Particle Physics - MDPI, accessed January 2, 2026, [[https://www.mdpi.com/2218-1997/8/9/482]{.underline}](https://www.mdpi.com/2218-1997/8/9/482)

36. The Statistical Mechanics of Hawking Radiation - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/2502.08816]{.underline}](https://arxiv.org/pdf/2502.08816)

37. Relational Time Superposition Hypothesis - Zenodo, accessed January 2, 2026, [[https://zenodo.org/records/16198707/files/RTSH_Paper_v3.pdf?download=1]{.underline}](https://zenodo.org/records/16198707/files/RTSH_Paper_v3.pdf?download=1)

38. Self-Organized Criticality and Turbulence - International Space Science Institute, accessed January 2, 2026, [[https://www.issibern.ch/teams/s-o-turbulence/issi_prop.pdf]{.underline}](https://www.issibern.ch/teams/s-o-turbulence/issi_prop.pdf)

39. Snowmass White Paper: Micro- and Macro-Structure of Black Holes, accessed January 2, 2026, [[https://www.slac.stanford.edu/econf/C210711/papers/2203.04981.pdf]{.underline}](https://www.slac.stanford.edu/econf/C210711/papers/2203.04981.pdf)

40. Fuzzballs and Microstate Geometries: Black-Hole Structure in String Theory - arXiv, accessed January 2, 2026, [[https://arxiv.org/pdf/2204.13113]{.underline}](https://arxiv.org/pdf/2204.13113)

41. Probing the horizon of black holes with gravitational waves - Sapienza Università Editrice, accessed January 2, 2026, [[https://editricesapienza.it/sites/default/files/6383_9788893773638_Probing_horizon_black_holes_eBook_0.pdf]{.underline}](https://editricesapienza.it/sites/default/files/6383_9788893773638_Probing_horizon_black_holes_eBook_0.pdf)

42. arXiv:2203.14320v1 \[gr-qc\] 27 Mar 2022, accessed January 2, 2026, [[https://arxiv.org/pdf/2203.14320]{.underline}](https://arxiv.org/pdf/2203.14320)

43. JHEP04(2022)017, accessed January 2, 2026, [[https://d-nb.info/1260832422/34]{.underline}](https://d-nb.info/1260832422/34)

44. Observational Tests of Fundamental Physics from Gravitational Wave Detections - Institutionelles Repositorium der Leibniz Universität Hannover, accessed January 2, 2026, [[https://repo.uni-hannover.de/bitstreams/6c5c3852-41c2-4829-bcc8-ca47a0534641/download]{.underline}](https://repo.uni-hannover.de/bitstreams/6c5c3852-41c2-4829-bcc8-ca47a0534641/download)

45. Geodesic Engineering for Propulsionless Spaceflight: Symbolic Optimization of Curved Spacetime Trajectories via the NEXUS Framework - Preprints.org, accessed January 2, 2026, [[https://www.preprints.org/manuscript/202507.2542]{.underline}](https://www.preprints.org/manuscript/202507.2542)

46. The Mark1 Nexus: A Recursive System Treatise - Zenodo, accessed January 2, 2026, [[https://zenodo.org/records/15871553]{.underline}](https://zenodo.org/records/15871553)

47. (PDF) Typeless Universes and Harmonic Field Computation: A Meta-Computational Framework - ResearchGate, accessed January 2, 2026, [[https://www.researchgate.net/publication/398690914_Typeless_Universes_and_Harmonic_Field_Computation_A_Meta-Computational_Framework]{.underline}](https://www.researchgate.net/publication/398690914_Typeless_Universes_and_Harmonic_Field_Computation_A_Meta-Computational_Framework)

48. Quantum Error Correction and Holography, Krylov Complexity, and continuous Tensor Networks - SISSA, accessed January 2, 2026, [[https://www.sissa.it/tpp/phdsection/AlumniThesis/Niloofar%20Vardian.pdf]{.underline}](https://www.sissa.it/tpp/phdsection/AlumniThesis/Niloofar%20Vardian.pdf)

49. Insights into Black Hole Microstates from AdS3 Holography Marcel R. R. Hughes - Queen Mary University of London, accessed January 2, 2026, [[https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/77112/Hughes_Marcel_SPA_PhD_final_Edited.pdf]{.underline}](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/77112/Hughes_Marcel_SPA_PhD_final_Edited.pdf)

50. The Information Loss Problem and Hawking Radiation as Tunneling - PMC, accessed January 2, 2026, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC11854280/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC11854280/)
