# Completeness and Convergence in Discrete Complex Systems: A Comprehensive Synthesis of Lattice Dynamics, Synchronization, and Information Geometry

## 1. Introduction: The Architecture of Discretized Reality

The question \"Is this branch complete?\" serves as a profound interrogation of the current state of theoretical physics concerning discrete systems. It challenges the observer to determine whether the intellectual lineage connecting the deterministic vibrations of ordered lattices, the stochastic localization of waves in disordered media, the nonlinear synchronization of coupled oscillators, and the emergent geometry of information constitutes a closed, self-consistent framework. This report argues that this \"branch\"---the physics of discrete, interacting, and often nonlinear manifolds---has achieved a remarkable degree of structural completeness. It has matured from a collection of isolated phenomenological models into a unified theoretical edifice where the microscopic discreteness of the substrate (be it atoms, time steps, or bits) dictates the macroscopic continuum behavior.

The investigation of this branch requires a traversal of three distinct but deeply interconnected regimes: the **Ordered**, the **Disordered**, and the **Dynamic**. In the ordered regime, we find the foundations of solid-state physics and phononics, where translational symmetry gives rise to Bloch waves and band gaps. In the disordered regime, symmetry breaks, leading to Anderson localization, where the interplay of interference and randomness halts transport, a phenomenon now rigorously understood through transfer matrix formalisms and Lyapunov exponents. In the dynamic regime, we encounter the temporal evolution of these systems, where nonlinear coupling induces synchronization, described by the Kuramoto and Adler frameworks, and where stability is governed by Lyapunov drift.

Finally, a fourth, overarching regime has emerged: the **Informational**. Here, the complex dynamics of these systems are not merely described by differential equations but quantified by information-theoretic metrics---Permutation Entropy, Lempel-Ziv complexity, and Fisher Information. This modern development suggests a recursive closure to the branch: the geometry of the physical world (even gravity itself) may be an emergent property of the information content of discrete underlying structures. This report provides an exhaustive synthesis of these domains, demonstrating how they weave together to form a complete description of discrete complex systems.

## 2. Lattice Dynamics: The Foundation of Discrete Order

The analysis begins with the most fundamental realization of a discrete system: the crystalline lattice. The physics of phononic crystals and discrete atomic chains serves as the baseline for understanding how discreteness imposes constraints on wave propagation, creating the spectral features that define the material universe.

### 2.1 The Monoatomic Chain and the Emergence of Dispersion

The simplest theoretical construct in this domain is the one-dimensional monoatomic chain. Consider an infinite array of \$N\$ identical atoms, each of mass \$m\$, connected by massless springs with a force constant \$\\kappa\$ (often denoted as \$C\$ or \$f\$ in literature), and separated by an equilibrium spacing \$a\$. The displacement of the \$n\$-th atom from its equilibrium position, denoted \$u_n\$, is governed by Newton's laws applied to the nearest-neighbor interactions.^1^

The equation of motion is a second-order linear difference-differential equation:

\$\$m \\ddot{u}\_n = \\kappa (u\_{n+1} - u_n) - \\kappa (u_n - u\_{n-1}) = \\kappa (u\_{n+1} + u\_{n-1} - 2u_n)\$\$

This discrete Laplacian structure is ubiquitous, appearing in contexts ranging from thermal transport to discretized field theories. The solution ansatz is a traveling plane wave \$u_n(t) = A e\^{i(kna - \\omega t)}\$, where \$k\$ is the wavenumber and \$\\omega\$ is the angular frequency.2 Substituting this ansatz reveals the fundamental dispersion relation:

\$\$\\omega(k) = \\sqrt{\\frac{4\\kappa}{m}} \\left\| \\sin\\left(\\frac{ka}{2}\\right) \\right\|\$\$

This relationship encapsulates the primary consequence of discreteness: the frequency is periodic in wavenumber space. This periodicity necessitates the definition of the First Brillouin Zone (FBZ), confined to the interval \$k \\in \[-\\pi/a, \\pi/a\]\$. Wavevectors outside this range do not represent distinct physical modes but are merely aliases of those within the FBZ, a phenomenon analogous to the Nyquist-Shannon sampling theorem in signal processing.1

The Continuum Limit and Dispersive Divergence

In the long-wavelength limit (\$k \\to 0\$), the sine term approximates its argument, yielding a linear dispersion \$\\omega \\approx a\\sqrt{\\kappa/m} k\$. Here, the phase velocity \$v_p = \\omega/k\$ and the group velocity \$v_g = d\\omega/dk\$ are identical and constant, recovering the behavior of a continuous elastic medium with sound speed \$c_s = a\\sqrt{\\kappa/m}\$.1 However, as \$k\$ approaches the Brillouin zone boundary (\$\\pm \\pi/a\$), the group velocity vanishes (\$v_g \\to 0\$), indicating a standing wave where adjacent atoms move in opposite directions. This divergence from the continuum prediction is the hallmark of the discrete lattice.

### 2.2 Broken Symmetry: The Diatomic Chain and Band Gaps

The introduction of a basis into the unit cell---such as alternating masses \$M_1\$ and \$M_2\$ (with \$M_1 \> M_2\$) or alternating spring constants---breaks the translational symmetry of the monoatomic chain, leading to the opening of a **band gap**. This is the foundational concept behind phononic crystals and electronic semiconductors.

The equations of motion decouple into a system of two coupled differential equations for the displacements \$u_n\$ (mass \$M_1\$) and \$v_n\$ (mass \$M_2\$):

\$\$\\begin{aligned} M_1 \\ddot{u}\_n &= \\kappa (v_n + v\_{n-1} - 2u_n) \\\\ M_2 \\ddot{v}\_n &= \\kappa (u\_{n+1} + u_n - 2v_n) \\end{aligned}\$\$

Solving the resulting secular determinant yields two frequency branches 5:

\$\$\\omega\^2 = \\frac{\\kappa(M_1+M_2)}{M_1 M_2} \\pm \\kappa \\sqrt{\\left(\\frac{M_1+M_2}{M_1 M_2}\\right)\^2 - \\frac{4}{M_1 M_2} \\sin\^2\\left(\\frac{ka}{2}\\right)}\$\$

These two branches describe fundamentally different physical modes of vibration:

  --------------------------------------------------------------------------------------------------------------------------------
  **Feature**                **Acoustic Branch (ω−​)**                        **Optical Branch (ω+​)**
  -------------------------- ----------------------------------------------- -----------------------------------------------------
  **Limit (\$k \\to 0\$)**   \$\\omega \\to 0\$                              \$\\omega \\to \\sqrt{2\\kappa(1/M_1 + 1/M_2)}\$

  **Motion Type**            Masses move in phase (center of mass motion).   Masses move out of phase (dipole-like oscillation).

  **Continuum Analog**       Sound waves in elastic media.                   Oscillating dipoles in ionic crystals.

  **Zone Boundary**          \$\\omega\_{max} = \\sqrt{2\\kappa/M_1}\$       \$\\omega\_{min} = \\sqrt{2\\kappa/M_2}\$
  --------------------------------------------------------------------------------------------------------------------------------

The Phononic Band Gap

Between the maximum frequency of the acoustic branch and the minimum frequency of the optical branch lies a region of forbidden frequencies:

\$\$\\Delta \\omega\_{gap} = \\sqrt{\\frac{2\\kappa}{M_2}} - \\sqrt{\\frac{2\\kappa}{M_1}}\$\$

Within this gap, the wavenumber \$k\$ becomes complex, implying that wave solutions are evanescent---they decay exponentially rather than propagate.3 This mechanism is exploited in phononic crystals to create perfect acoustic mirrors or filters. By periodically structuring materials (e.g., silicon lattices with vacuum holes or tungsten inclusions), engineers can manipulate the packing fraction to maximize this gap, effectively creating an insulator for sound.3 The physics here is strictly analogous to the electronic band gap in semiconductors, where the periodic potential of the ion cores prevents electron propagation at certain energies.7

## 3. The Lattice Green's Function: Asymptotics and Defects

While dispersion relations characterize the perfect lattice, real-world systems are defined by their imperfections. The mathematical machinery required to treat discrete defects---vacancies, interstitials, and impurities---is the **Lattice Green's Function (LGF)**. This operator is the resolvent of the discrete Laplacian and serves as the bridge between the discrete microscopic equations and the macroscopic continuum elasticity.

### 3.1 Formalism and Integral Representation

The Lattice Green's Function \$G(\\mathbf{x})\$ is defined as the response of the lattice to a localized point source (a Kronecker delta force). It satisfies the discrete Helmholtz equation:

\$\$(\\mu\^2 - \\Delta) G(\\mathbf{x}) = \\delta\_{\\mathbf{x}, \\mathbf{0}}\$\$

where \$\\Delta\$ is the discrete Laplacian operator on the lattice \$\\mathbb{Z}\^d\$ and \$\\mu\$ is a mass or frequency parameter.8 For a \$d\$-dimensional hypercubic lattice, the LGF admits a fundamental integral representation:

\$\$G(\\mathbf{x}; \\mu) = \\int\_{\[-\\pi, \\pi\]\^d} \\frac{e\^{i \\mathbf{k} \\cdot \\mathbf{x}}}{\\mu\^2 + 2d - 2\\sum\_{j=1}\^d \\cos(k_j)} \\frac{d\^d\\mathbf{k}}{(2\\pi)\^d}\$\$

.8

In the case of \$\\mu=0\$ (the static or massless limit), the value of this integral at the origin, \$G(\\mathbf{0}; 0)\$, relates to the probability of return for a random walker on the lattice. These values are known as **Watson Integrals** and have been evaluated exactly for simple cubic (sc), face-centered cubic (fcc), and body-centered cubic (bcc) lattices, often involving products of Gamma functions.^8^

### 3.2 Asymptotic Behavior: The Recovery of Isotropy

A central question in the completeness of this branch is whether the discrete lattice theory correctly recovers the isotropic continuum behavior at large distances. The LGF exhibits distinct asymptotic behaviors depending on dimensionality and the mass parameter, confirming the subtle transition from discrete to continuous physics.

Massive Case (\$\\mu \> 0\$):

When the field is massive (or the frequency lies within a band gap), the LGF decays exponentially. This behavior is mediated by Modified Bessel functions of the second kind, \$K\_\\nu(z)\$. This is physically analogous to the Yukawa potential describing screened interactions, where the \"screening length\" is determined by the lattice parameters and the band gap width.8

Massless Case (\$\\mu = 0\$):

The massless limit reveals the topological differences between dimensions:

- **2D:** The integral diverges logarithmically at small \$k\$, reflecting the recurrent nature of 2D random walks. This implies that a pure static point force in a 2D lattice produces a displacement field that grows with distance, necessitating a finite domain or a screening background for physical stability.^8^

- 3D: The LGF remains finite and decays as \$1/r\$. Specifically, asymptotic analysis using the method of stationary phase or Mellin transforms demonstrates that:\
  \
  \$\$G(\\mathbf{x}) \\sim \\frac{C}{\|\\mathbf{x}\|} + \\mathcal{O}\\left(\\frac{1}{\|\\mathbf{x}\|\^3}\\right)\$\$\
  \
  This result is profound: despite the underlying cubic anisotropy of the lattice (where waves travel at different speeds along axes vs. diagonals), the long-range static potential becomes perfectly isotropic.10 The lattice \"forgets\" its cubic nature at large distances, validating the use of the continuum Poisson equation for macroscopic problems.

### 3.3 Strain Fields and the \"Core\" Problem

The LGF allows for the rigorous calculation of strain fields around point defects using the method of Lattice Statics. In this framework, the displacement field \$\\mathbf{u}(\\mathbf{x})\$ is the convolution of the LGF with the force distribution \$\\mathbf{f}\$ representing the defect (e.g., Kanzaki forces):

\$\$\\mathbf{u}(\\mathbf{x}) = \\sum\_{\\mathbf{x}\'} G(\\mathbf{x} - \\mathbf{x}\') \\mathbf{f}(\\mathbf{x}\')\$\$

.13

Comparing these discrete calculations with continuum elasticity theory reveals a \"Core Radius\"---a distance from the defect below which continuum theory fails.

- **Far Field (\$r \> r\_{core}\$):** The discrete displacements match the continuum prediction (\$u \\propto 1/r\^2\$ for a center of dilation in 3D).

- **Near Field (\$r \< r\_{core}\$):** Significant deviations occur. For vacancies in metals like Aluminum and Copper, the continuum theory is invalid closer than the 4th or 5th neighbor shell.^13^

- **Green\'s Function \"Patching\":** Modern multiscale methods exploit this by using the exact LGF for the defect core and patching it to the continuum Green\'s function for the far field, ensuring both accuracy and computational efficiency.^14^

### 3.4 Gravitational Analogies: Lattice Defects as Spacetime Geometry

An intriguing extension of this branch connects lattice defects to the theory of gravity, specifically **Metric-Affine Gravity**. In this analogy, the continuum limit of a crystal with defects generates a non-Riemannian geometry:

- **Dislocations** correspond to **Torsion** (a twisting of the manifold).

- **Disclinations** (rotational defects) correspond to **Curvature** (or non-metricity).^15^

Just as a point defect creates a strain field decaying as \$1/r\^2\$ (and a stress field as \$1/r\^3\$), massive bodies create gravitational fields. This correspondence allows theoretical physicists to use crystalline models with \"wormholes\" (screw dislocations) or \"cosmic strings\" (wedge disclinations) to test modified gravity theories.^15^ The study of the LGF thus provides a toy model for **Quantum Foam**---the hypothetical discrete microstructure of spacetime itself.

## 4. Disorder and Localization: The Breakdown of Transport

While perfect lattices enable transport (ballistic Bloch waves), disorder halts it. The study of **Anderson Localization** represents the transition from the conductive to the insulating state driven purely by quantum interference (or classical wave interference) in random potentials. This section details the mechanisms of localization using the Transfer Matrix Method and explores the critical role of Lyapunov exponents.

### 4.1 The 1D Anderson Model and Transfer Matrices

In a 1D tight-binding model with diagonal disorder (random site energies \$\\epsilon_n\$), the time-independent Schrödinger equation can be rewritten as a discrete map. The wavefunction amplitudes at adjacent sites are related via a Transfer Matrix \$M_n\$:

\$\$\\begin{pmatrix} \\psi\_{n+1} \\\\ \\psi_n \\end{pmatrix} = M_n \\begin{pmatrix} \\psi_n \\\\ \\psi\_{n-1} \\end{pmatrix} = \\begin{pmatrix} \\frac{E - \\epsilon_n}{t} & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} \\psi_n \\\\ \\psi\_{n-1} \\end{pmatrix}\$\$

where \$t\$ is the hopping integral and \$E\$ is the energy.18

The global transport properties of a chain of length \$N\$ are determined by the global transfer matrix \$T_N = \\prod\_{n=1}\^N M_n\$. Since the \$M_n\$ are random matrices with determinant 1, the product \$T_N\$ describes a random walk in the group \$SL(2, \\mathbb{R})\$. **Furstenberg's Theorem** on products of random matrices states that, under broad conditions, the norm of this product grows exponentially with \$N\$.^19^

This exponential growth is quantified by the Lyapunov Exponent (LE), denoted \$\\gamma(E)\$:

\$\$\\gamma(E) = \\lim\_{N \\to \\infty} \\frac{1}{N} \\ln \|\|T_N\|\|\$\$

The Localization Length \$\\xi(E)\$ is simply the inverse of the LE: \$\\xi(E) = 1/\\gamma(E)\$. The positivity of \$\\gamma(E)\$ for all energies in 1D systems (the scaling theory of localization) implies that all eigenstates are exponentially localized; there is no true metallic phase in 1D disordered wires.19

### 4.2 Anomalies and Scaling Behaviors

While localization is generic in 1D, the behavior of the Lyapunov exponent is not uniform across the energy spectrum. Specific energies exhibit **anomalies** where the standard perturbative expansions fail.

Band Center Anomaly (\$E=0\$):

In the standard Anderson model, the Lyapunov exponent typically scales with the variance of the disorder \$\\sigma\^2\$ as \$\\gamma \\propto \\sigma\^2\$. However, at the band center (\$E=0\$), resonance effects cause a breakdown of this scaling. The expansion of \$\\gamma\$ involves non-analytic terms or different pre-factors, often described as the \"band center anomaly\".22

Band Edge Behavior:

The transition from the pass band to the band gap in a periodic-on-average system is sharp. Inside the band gaps of the underlying periodic potential, the LE is large (determined by the gap width). Disorder introduces states into these gaps (Lifshitz tails). The scaling of the LE for these gap states differs from that of the band states. While band states show single-parameter scaling (SPS), states deep within the gaps may require two parameters to describe their distribution, marking a deviation from the universality usually associated with Anderson localization.22

### 4.3 Quasi-Crystals: The Fibonacci Hamiltonian

Intermediate between periodic and random systems lie **Quasi-Crystals**, typified by the **Fibonacci Hamiltonian**. Here, the potential \$\\epsilon_n\$ takes on two values arranged according to the Fibonacci substitution rule (\$A \\to AB, B \\to A\$).

The spectrum of the Fibonacci Hamiltonian is **Singular Continuous**: it is a Cantor set with zero Lebesgue measure (it has no \"width\" in the conventional sense) but no isolated points. This leads to \"Critical\" wavefunctions that are neither extended (Bloch-like) nor localized (Anderson-like), but decay as power-laws.^24^

Trace Maps and Renormalization:

The study of these systems relies on the Trace Map formalism. The trace of the transfer matrix \$x_n = \\frac{1}{2}\\text{Tr}(M_n)\$ satisfies a nonlinear recurrence relation:

\$\$x\_{n+1} = 2x_n x\_{n-1} - x\_{n-2}\$\$

This dynamical map possesses an invariant quantity \$I(x,y,z) = x\^2 + y\^2 + z\^2 - 2xyz - 1\$.26 The spectral properties of the Hamiltonian are uniquely determined by the dynamics of this map. Specifically, energies \$E\$ belong to the spectrum if and only if the orbit of the trace map under iteration remains bounded. This connection allows for the exact calculation of spectral gaps and transport exponents, linking the spectral theory of operators to the dynamics of nonlinear maps.26

### 4.4 Non-Hermitian Localization and the Skin Effect

A recent and vital extension of this branch involves **Non-Hermitian** systems, where the Hamiltonian is not self-adjoint (e.g., systems with gain/loss or non-reciprocal hopping like the Hatano-Nelson model).

These systems exhibit the **Non-Hermitian Skin Effect (NHSE)**: under Open Boundary Conditions (OBC), a macroscopic number of eigenstates localize at the boundaries of the system, fundamentally differing from the Bloch waves found under Periodic Boundary Conditions (PBC).^28^ This sensitivity to boundaries invalidates the conventional Bloch-Floquet analysis.

To restore completeness to the theory, one must replace the standard Brillouin Zone with the **Generalized Brillouin Zone (GBZ)**. The GBZ is the set of complex wavevectors \$k\$ (where \$\\text{Im}(k) \\neq 0\$) that allow the construction of eigenstates satisfying the open boundary conditions. The calculation of Lyapunov exponents in these systems requires considering the generalized transfer matrix over this complex contour, linking topological winding numbers to the localization transition.^28^

## 5. Synchronization: The Dynamics of Coupling

Moving from static disorder to temporal evolution, we encounter the phenomenon of synchronization. This section details how populations of discrete oscillators, governed by nonlinear coupling, transition from incoherent disorder to coherent macroscopic order.

### 5.1 The Kuramoto Model: Order from Chaos

The Kuramoto Model serves as the canonical framework for studying synchronization in large populations. It describes \$N\$ coupled limit-cycle oscillators with phases \$\\theta_i\$ and natural frequencies \$\\omega_i\$ drawn from a distribution \$g(\\omega)\$.29 The governing equation is:

\$\$\\frac{d\\theta_i}{dt} = \\omega_i + \\frac{K}{N} \\sum\_{j=1}\^N \\sin(\\theta_j - \\theta_i)\$\$

where \$K\$ is the coupling strength.

The Phase Transition:

The system exhibits a phase transition at a critical coupling \$K_c = 2/(\\pi g(0))\$.

- **Incoherent State (\$K \< K_c\$):** Oscillators rotate at their natural frequencies. The complex order parameter \$r = \\frac{1}{N} \\sum e\^{i\\theta_j}\$ averages to zero.

- **Synchronized State (\$K \> K_c\$):** A macroscopic cluster of oscillators locks to a common mean frequency \$\\Omega\$. The order parameter \$r\$ becomes non-zero, growing as \$\\sqrt{K - K_c}\$ (a standard second-order mean-field transition).^30^

### 5.2 Adler's Equation and Injection Locking

When the system is reduced to a single oscillator driven by an external signal (or two mutually coupled oscillators), the dynamics are described by Adler's Equation. If an oscillator with free-running frequency \$\\omega_0\$ is injected with a signal \$\\omega\_{inj}\$, the phase difference \$\\phi(t) = \\theta\_{osc} - \\theta\_{inj}\$ evolves as:

\$\$\\frac{d\\phi}{dt} = \\Delta\\omega - K \\sin(\\phi)\$\$

where \$\\Delta\\omega = \\omega_0 - \\omega\_{inj}\$ is the detuning and \$K\$ is the injection strength.31

Locking Range and Arnold Tongues:

This equation predicts a sharp synchronization threshold known as the Locking Range.

- If \$\|\\Delta\\omega\| \< K\$, fixed points exist where \$d\\phi/dt = 0\$. The oscillator is phase-locked to the injection signal. The region in the \$(K, \\Delta\\omega)\$ plane where locking occurs forms a V-shaped region called an **Arnold Tongue**.^32^

- If \$\|\\Delta\\omega\| \> K\$, no fixed points exist. The phase difference grows indefinitely, but not uniformly. The oscillator exhibits **Frequency Pulling**: the beat frequency is less than the detuning \$\\Delta\\omega\$. The oscillator spends more time at phases where the coupling opposes the intrinsic motion, reducing the effective frequency difference: \$\\omega\_{beat} = \\sqrt{(\\Delta\\omega)\^2 - K\^2}\$.^31^

### 5.3 Phase Slips and Topological Defects

In the regime just outside synchronization, or in spatially extended lattice arrays of oscillators, the system dynamics are dominated by **Phase Slips**. A phase slip is a rapid \$2\\pi\$ unwinding of the phase difference, effectively \"resetting\" the cycle to allow a faster oscillator to lap a slower one.^35^

In 2D oscillator arrays, these slips manifest as **Topological Defects** (vortices). These are singular points in the lattice where the phase is undefined, and the accumulated phase around the point is \$\\oint \\nabla \\theta \\cdot dl = \\pm 2\\pi\$. The synchronization transition in 2D systems (e.g., Josephson junction arrays) is often a **Kosterlitz-Thouless (KT) transition**, driven by the binding and unbinding of vortex-antivortex pairs. The \"disorder\" in the synchronized state is literally topological in nature.^37^

### 5.4 Stability Analysis: Lyapunov Drift

The stability of synchronized states is rigorously analyzed using **Lyapunov Drift**. In the context of control theory and stochastic networks, **Lyapunov Optimization** (or the Drift-plus-Penalty method) is used to stabilize queues and coupled systems.

For a system state vector \$\\mathbf{Q}(t)\$, one defines a quadratic Lyapunov function \$L(\\mathbf{Q}) = \\frac{1}{2} \\sum Q_i\^2\$. The Lyapunov Drift \$\\Delta(\\mathbf{Q}(t))\$ is the expected change in this function over one time step:

\$\$\\Delta(\\mathbf{Q}(t)) = \\mathbb{E}\[L(\\mathbf{Q}(t+1)) - L(\\mathbf{Q}(t)) \| \\mathbf{Q}(t)\]\$\$

To ensure stability (synchronization or queue boundedness), control algorithms (like MaxWeight) minimize an upper bound on this drift.38 This creates a direct mathematical link between the stability of physical oscillators (minimizing potential energy) and the stability of information networks (minimizing queue backlogs), unifying the dynamical and informational perspectives.

## 6. Information Geometry: Quantifying Complexity

The final pillar of this branch addresses the quantification of state. How do we distinguish between the \"randomness\" of thermal noise and the \"complexity\" of a chaotic but synchronized system? This requires metrics from Information Geometry.

### 6.1 Permutation Entropy: Weighted and Unweighted

Permutation Entropy (PeEn) is a complexity measure based on the ordinal patterns within a time series. Unlike Shannon entropy, which relies on value distributions, PeEn analyzes the temporal ordering of values.

For a time series \$x_t\$, one constructs embedding vectors of dimension \$m\$ and delay \$\\tau\$. The components of these vectors are ranked by size, mapping the vector to one of \$m!\$ possible permutations (motifs) \$\\pi\$.40

The Permutation Entropy is:

\$\$H\_{PE}(m) = - \\sum\_{j=1}\^{m!} p(\\pi_j) \\log_2 p(\\pi_j)\$\$

- **Low PeEn:** Indicates a regular, deterministic, or synchronized signal (few motifs appear).

- **High PeEn:** Indicates stochasticity or high-dimensional hyperchaos (all motifs equiprobable).^42^

Weighted Permutation Entropy (WPE):

A limitation of standard PeEn is that it discards amplitude information; a small fluctuation due to noise is treated identically to a large structural shift. Weighted Permutation Entropy corrects this by weighting the probability of each motif by the variance of the vectors that generate it.43 This makes WPE robust against small-amplitude noise while retaining sensitivity to significant dynamical events (like spikes in EEG data or phase slips in oscillators).44

### 6.2 Lempel-Ziv Complexity (LZC) and Normalization

**Lempel-Ziv Complexity** assesses the algorithmic compressibility of a discrete sequence. It counts the number of distinct substrings required to reconstruct the sequence. In the context of dynamical systems, LZC serves as a proxy for the entropy rate of the source.^46^

Normalization:

To compare LZC across different datasets, it must be normalized. The theoretical upper bound for the complexity \$c(N)\$ of a binary sequence of length \$N\$ is \$N / \\log_2 N\$. Therefore, the Normalized Lempel-Ziv Complexity \$C\_{norm}\$ is:

\$\$C\_{norm} = \\frac{c(N) \\log_b N}{N}\$\$

where \$b\$ is the number of distinct symbols in the alphabet.47

This metric is extensively used in biomedical signal processing to detect synchronization transitions (e.g., the onset of epileptic seizures, where \$C\_{norm}\$ drops sharply as neural oscillators lock).47

### 6.3 Fisher Information and Emergent Geometry

At the deepest theoretical level, Fisher Information provides a bridge between information theory and differential geometry. It defines a metric (the Fisher-Rao metric) on the manifold of probability distributions.

\$\$g\_{ij}(\\theta) = \\mathbb{E}\\left\[ \\frac{\\partial}{\\partial \\theta_i} \\log p(x\|\\theta) \\frac{\\partial}{\\partial \\theta_j} \\log p(x\|\\theta) \\right\]\$\$

Recent theoretical developments suggest that the \"blurred\" metric of spacetime itself might emerge from the Fisher information of the underlying quantum state entanglement.50 This \"Information Geometry\" perspective posits that the smooth geometry of General Relativity is a macroscopic effective theory arising from the \"informational\" properties (entanglement contours) of a discrete quantum substrate.50 This closes the loop with the gravitational analogies discussed in Section 3.4: defects in the lattice define the curvature, and information defines the metric.

## 7. Computational Methods: Simulating the Continuum

To validate these theories, one requires robust numerical methods that respect the underlying geometry of the discrete systems.

### 7.1 Geometric Integration: Discrete Gradient Methods

Simulating conservative or dissipative systems (like the lattice dynamics in Section 2) using standard integrators (e.g., Forward Euler) often destroys physical invariants like energy conservation. **Discrete Gradient Methods** are designed to preserve these structures exactly in discrete time.

For a system governed by a gradient flow \$\\dot{x} = -\\nabla V(x)\$, a discrete gradient \$\\bar{\\nabla}V\$ is defined such that it satisfies the discrete chain rule:

\$\$V(x\_{k+1}) - V(x_k) = \\bar{\\nabla}V(x_k, x\_{k+1}) \\cdot (x\_{k+1} - x_k)\$\$

Using the Itoh-Abe discrete gradient formulation allows for the construction of numerical schemes that are unconditionally stable and energy-diminishing, regardless of the time step size.53 This is critical for simulating stiff phononic systems or finding ground states in lattice statics.

### 7.2 Phase Screens and Scintillation Modeling

In the propagation of waves through random discrete media (like the ionosphere), the **Phase Screen Model** collapses extended disorder into thin discrete layers. This simplifies the computational problem of the parabolic wave equation.^56^

The severity of the \"disorder\" is quantified by the Scintillation Index \$S_4\$, which measures intensity fluctuations:

\$\$S_4 = \\sqrt{\\frac{\\langle I\^2 \\rangle - \\langle I \\rangle\^2}{\\langle I \\rangle\^2}}\$\$

And the Phase Variance \$\\sigma\_\\phi\^2\$, which measures phase jitter. These indices are derived directly from the statistical properties of the phase screen (e.g., the spectral index of the irregularities) and are essential for predicting signal degradation in satellite communications.57

## 8. Conclusion

This report confirms that the theoretical branch encompassing **Lattice Dynamics**, **Synchronization**, **Localization**, and **Information Geometry** is structurally complete. The connections are rigorous and bidirectional:

1.  **Structure \$\\leftrightarrow\$ Dynamics:** The dispersion relations of the perfect lattice define the \"stage\" for synchronization dynamics (Adler\'s equation).

2.  **Dynamics \$\\leftrightarrow\$ Disorder:** Synchronization is destroyed by disorder (frequency dispersion), leading to phase slips and topological defects that mirror the localization of wavefunctions.

3.  **Disorder \$\\leftrightarrow\$ Information:** The breakdown of order (localization) is quantified by Lyapunov exponents, which are themselves information-theoretic limits (entropy rates).

4.  **Information \$\\leftrightarrow\$ Structure:** The geometry of the lattice (and spacetime) can be derived from informational metrics (Fisher Information), suggesting a fundamental primacy of the discrete bit over the continuous field.

From the microscopic transfer matrix of a single atom to the macroscopic synchronization of a power grid, and from the algorithmic complexity of a data stream to the emergent curvature of spacetime, the formalisms reviewed here---**Green\'s Functions, Transfer Matrices, Kuramoto-Adler Equations, and Entropic Metrics**---form a unified, self-consistent description of the physical world.

## 9. Appendix: Summary of Key Formulations

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Domain**          **Concept**                  **Key Equation / Metric**                                                                    **Physical Insight**
  ------------------- ---------------------------- -------------------------------------------------------------------------------------------- ----------------------------------------------------------
  **Phononics**       Dispersion (Monoatomic)      \$\\omega = 2\\sqrt{\\kappa/m}                                                               \\sin(ka/2)

  **Phononics**       Band Gap (Diatomic)          \$\\Delta \\omega = \\sqrt{2\\kappa/M_2} - \\sqrt{2\\kappa/M_1}\$                            Basis symmetry breaking stops propagation.

  **Defects**         Lattice Green\'s Fx          \$G(\\mathbf{x}) \\sim \\int \\frac{e\^{ikx}}{\\mu\^2 - \\Delta(k)} dk\$                     Resolvent of discrete Laplacian; recovers \$1/r\$ in 3D.

  **Dynamics**        Synchronization (Kuramoto)   \$\\dot{\\theta}\_i = \\omega_i + \\frac{K}{N}\\sum \\sin(\\theta_j - \\theta_i)\$           Phase transition from incoherent to locked state.

  **Dynamics**        Injection Locking (Adler)    \$\\dot{\\phi} = \\Delta\\omega - K \\sin \\phi\$                                            Defines Arnold Tongues and frequency pulling.

  **Localization**    Lyapunov Exponent            \$\\gamma = \\lim \\frac{1}{N} \\ln                                                          

  **Quasi-Crystal**   Trace Map                    \$x\_{n+1} = 2x_n x\_{n-1} - x\_{n-2}\$                                                      Renormalization of spectrum; singular continuous.

  **Complexity**      Permutation Entropy          \$H\_{PE} = -\\sum p(\\pi) \\log p(\\pi)\$                                                   Robust measure of time-series order/chaos.

  **Complexity**      Normalized LZC               \$C\_{norm} = \\frac{LZ(N) \\log N}{N}\$                                                     Algorithmic compressibility; synchrony detector.

  **Scintillation**   \$S_4\$ Index                \$S_4 = \\sqrt{(\\langle I\^2 \\rangle - \\langle I \\rangle\^2)/\\langle I \\rangle\^2}\$   Intensity variance in random media propagation.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Works cited

1.  Discrete one dimensional systems, accessed January 15, 2026, [[https://ethz.ch/content/dam/ethz/special-interest/phys/theoretical-physics/cmtm-dam/documents/mmm/SS2018/Chapter_03.pdf]{.underline}](https://ethz.ch/content/dam/ethz/special-interest/phys/theoretical-physics/cmtm-dam/documents/mmm/SS2018/Chapter_03.pdf)

2.  §4 -- Vibrations, accessed January 15, 2026, [[https://www.ucl.ac.uk/\~ucapikr/Solid_State_Physics/Section%204.pdf]{.underline}](https://www.ucl.ac.uk/~ucapikr/Solid_State_Physics/Section%204.pdf)

3.  Simulation study of phononic crystal structures - uu .diva, accessed January 15, 2026, [[https://uu.diva-portal.org/smash/get/diva2:1118821/FULLTEXT01.pdf]{.underline}](https://uu.diva-portal.org/smash/get/diva2:1118821/FULLTEXT01.pdf)

4.  of 1 9, accessed January 15, 2026, [[https://www.physics.rutgers.edu/\~chakhalian/CM2018/HW2_solutions.pdf]{.underline}](https://www.physics.rutgers.edu/~chakhalian/CM2018/HW2_solutions.pdf)

5.  1-d chain of atoms with two different masses - TU Graz, accessed January 15, 2026, [[http://lampz.tugraz.at/\~hadley/ss1/phonons/1d/1d2m.php]{.underline}](http://lampz.tugraz.at/~hadley/ss1/phonons/1d/1d2m.php)

6.  3.2 - The diatomic chain - Solid-state physics, accessed January 15, 2026, [[https://ssp.utasphys.cloud.edu.au/3-1d/3-2-diatomic/]{.underline}](https://ssp.utasphys.cloud.edu.au/3-1d/3-2-diatomic/)

7.  Introduction to Photonic Crystals: Bloch\'s Theorem, Band Diagrams, and Gaps (But No Defects) - Ab Initio Physics Research, accessed January 15, 2026, [[http://ab-initio.mit.edu/photons/tutorial/photonic-intro.pdf]{.underline}](http://ab-initio.mit.edu/photons/tutorial/photonic-intro.pdf)

8.  Asymptotic behaviour of the lattice Green function - Alea, accessed January 15, 2026, [[https://alea.impa.br/articles/v19/19-38.pdf]{.underline}](https://alea.impa.br/articles/v19/19-38.pdf)

9.  Asymptotic expansions of lattice Green\'s functions - ResearchGate, accessed January 15, 2026, [[https://www.researchgate.net/publication/243685362_Asymptotic_expansions_of_lattice_Green\'s_functions]{.underline}](https://www.researchgate.net/publication/243685362_Asymptotic_expansions_of_lattice_Green's_functions)

10. Discrete scattering theory: Green\'s function for a square lattice - Colorado School of Mines, accessed January 15, 2026, [[https://inside.mines.edu/\~pamartin/ref-paps/R094_WMw.pdf]{.underline}](https://inside.mines.edu/~pamartin/ref-paps/R094_WMw.pdf)

11. \[2101.04717\] Asymptotic behaviour of the lattice Green function - arXiv, accessed January 15, 2026, [[https://arxiv.org/abs/2101.04717]{.underline}](https://arxiv.org/abs/2101.04717)

12. Asymptotic behaviour of the lattice Green function - ResearchGate, accessed January 15, 2026, [[https://www.researchgate.net/publication/361518604_Asymptotic_behaviour_of_the_lattice_Green_function]{.underline}](https://www.researchgate.net/publication/361518604_Asymptotic_behaviour_of_the_lattice_Green_function)

13. Asymptotic Lattice Displacements about Point Defects in Cubic Metals - UNL Digital Commons, accessed January 15, 2026, [[https://digitalcommons.unl.edu/physicshardy/24/]{.underline}](https://digitalcommons.unl.edu/physicshardy/24/)

14. Multiscale modeling of point defects in strained silicon - National Institute of Standards and Technology, accessed January 15, 2026, [[https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50643]{.underline}](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=50643)

15. arXiv:1507.07777v1 \[hep-th\] 28 Jul 2015, accessed January 15, 2026, [[https://arxiv.org/pdf/1507.07777]{.underline}](https://arxiv.org/pdf/1507.07777)

16. Crystal lattice defects and differential geometry1 ABSTRACT, accessed January 15, 2026, [[https://d-nb.info/1365039439/34]{.underline}](https://d-nb.info/1365039439/34)

17. Analogue Gravity - PMC - PubMed Central, accessed January 15, 2026, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC5255896/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC5255896/)

18. Transfer matrix study of the Anderson transition in non-Hermitian systems, accessed January 15, 2026, [[http://home.ustc.edu.cn/\~rzy55555/project/Luo-Transfer-matrix-Anderson-transition-non-Hermitian-systems.pdf]{.underline}](http://home.ustc.edu.cn/~rzy55555/project/Luo-Transfer-matrix-Anderson-transition-non-Hermitian-systems.pdf)

19. Lyapunov exponents, one-dimensional Anderson localization and products of random matrices - ResearchGate, accessed January 15, 2026, [[https://www.researchgate.net/publication/258310794_Lyapunov_exponents_one-dimensional_Anderson_localization_and_products_of_random_matrices]{.underline}](https://www.researchgate.net/publication/258310794_Lyapunov_exponents_one-dimensional_Anderson_localization_and_products_of_random_matrices)

20. Dynamical localization \| Random physics, accessed January 15, 2026, [[https://www.cpt.univ-mrs.fr/\~verga/pages/kicked-localization.html]{.underline}](https://www.cpt.univ-mrs.fr/~verga/pages/kicked-localization.html)

21. (PDF) Transfer Matrices and Disordered Systems - ResearchGate, accessed January 15, 2026, [[https://www.researchgate.net/publication/251307341_Transfer_Matrices_and_Disordered_Systems]{.underline}](https://www.researchgate.net/publication/251307341_Transfer_Matrices_and_Disordered_Systems)

22. Statistics of the Lyapunov Exponent in 1D Random Periodic-on-Average Systems, accessed January 15, 2026, [[https://physics.qc.cuny.edu/uploads/4/articles/PRL81-5390.pdf]{.underline}](https://physics.qc.cuny.edu/uploads/4/articles/PRL81-5390.pdf)

23. Lyapunov exponents of the generalized one-dimensional Anderson model, accessed January 15, 2026, [[http://www.physics.sk/aps/pubs/1989/aps_1989_39_1_3.pdf]{.underline}](http://www.physics.sk/aps/pubs/1989/aps_1989_39_1_3.pdf)

24. Mathematical Physics Spectral Properties of a Tight Binding Hamiltonian with Period Doubling Potential - Project Euclid, accessed January 15, 2026, [[https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-135/issue-2/Spectral-properties-of-a-tight-binding-Hamiltonian-with-period-doubling/cmp/1104202031.pdf]{.underline}](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-135/issue-2/Spectral-properties-of-a-tight-binding-Hamiltonian-with-period-doubling/cmp/1104202031.pdf)

25. A natural class of generalized Fibonacci chains - UvA-DARE (Digital Academic Repository), accessed January 15, 2026, [[https://pure.uva.nl/ws/files/2993980/605_5387y.pdf]{.underline}](https://pure.uva.nl/ws/files/2993980/605_5387y.pdf)

26. arXiv:1403.7823v1 \[math.SP\] 30 Mar 2014, accessed January 15, 2026, [[https://arxiv.org/pdf/1403.7823]{.underline}](https://arxiv.org/pdf/1403.7823)

27. The Fractal Dimension of the Spectrum of the Fibonacci Hamiltonian - UCI Mathematics, accessed January 15, 2026, [[https://www.math.uci.edu/\~asgor/DEGT.pdf]{.underline}](https://www.math.uci.edu/~asgor/DEGT.pdf)

28. Asymmetric transfer matrix analysis of Lyapunov exponents in one-dimensional non-reciprocal quasicrystals - arXiv, accessed January 15, 2026, [[https://arxiv.org/html/2407.01372v1]{.underline}](https://arxiv.org/html/2407.01372v1)

29. The Kuramoto model: a simple paradigm for synchronization phenomena, accessed January 15, 2026, [[https://scala.uc3m.es/publications_MANS/PDF/finalKura.pdf]{.underline}](https://scala.uc3m.es/publications_MANS/PDF/finalKura.pdf)

30. Kuramoto model - Wikipedia, accessed January 15, 2026, [[https://en.wikipedia.org/wiki/Kuramoto_model]{.underline}](https://en.wikipedia.org/wiki/Kuramoto_model)

31. Gen-Adler: The generalized Adler\'s equation for injection locking analysis in oscillators, accessed January 15, 2026, [[https://www.researchgate.net/publication/221153851_Gen-Adler_The_generalized_Adler\'s_equation_for_injection_locking_analysis_in_oscillators]{.underline}](https://www.researchgate.net/publication/221153851_Gen-Adler_The_generalized_Adler's_equation_for_injection_locking_analysis_in_oscillators)

32. Synchronization - Scholarpedia, accessed January 15, 2026, [[http://www.scholarpedia.org/article/Synchronization]{.underline}](http://www.scholarpedia.org/article/Synchronization)

33. A Study of Injection Locking and Pulling in Oscillators, accessed January 15, 2026, [[http://www.seas.ucla.edu/brweb/papers/Journals/RSep04.pdf]{.underline}](http://www.seas.ucla.edu/brweb/papers/Journals/RSep04.pdf)

34. Injection Locking - Ali M. Niknejad\'s Research Homepage - UC Berkeley, accessed January 15, 2026, [[https://rfic.eecs.berkeley.edu/courses/ee242/pdf/eecs242_lect26_injectionlocking.pdf]{.underline}](https://rfic.eecs.berkeley.edu/courses/ee242/pdf/eecs242_lect26_injectionlocking.pdf)

35. A Stochastic Approach to the Synchronization of Coupled Oscillators - Frontiers, accessed January 15, 2026, [[https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2020.00115/full]{.underline}](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2020.00115/full)

36. arXiv:chao-dyn/9811005v2 18 Nov 1998 - ResearchGate, accessed January 15, 2026, [[https://www.researchgate.net/profile/Zhigang-Zheng-2/publication/1781603_Phase_Slips_and_Phase_Synchronization_of_Coupled_Oscillators/links/0c960515cf4beb1403000000/Phase-Slips-and-Phase-Synchronization-of-Coupled-Oscillators.pdf]{.underline}](https://www.researchgate.net/profile/Zhigang-Zheng-2/publication/1781603_Phase_Slips_and_Phase_Synchronization_of_Coupled_Oscillators/links/0c960515cf4beb1403000000/Phase-Slips-and-Phase-Synchronization-of-Coupled-Oscillators.pdf)

37. A Kuramoto model of coupled phase oscillators: Effect of noise on vorticity - YouTube, accessed January 15, 2026, [[https://www.youtube.com/watch?v=uXzGGxM2-GY]{.underline}](https://www.youtube.com/watch?v=uXzGGxM2-GY)

38. OIT 611 Lecture Notes Drift Method from Stochastic Networks to Machine Learning - Stanford University, accessed January 15, 2026, [[https://web.stanford.edu/\~kuangxu/papers/driftmethod.pdf]{.underline}](https://web.stanford.edu/~kuangxu/papers/driftmethod.pdf)

39. Lyapunov optimization - Wikipedia, accessed January 15, 2026, [[https://en.wikipedia.org/wiki/Lyapunov_optimization]{.underline}](https://en.wikipedia.org/wiki/Lyapunov_optimization)

40. Permutation Entropy: Too Complex a Measure for EEG Time Series? - MDPI, accessed January 15, 2026, [[https://www.mdpi.com/1099-4300/19/12/692]{.underline}](https://www.mdpi.com/1099-4300/19/12/692)

41. Permutation Entropy - Aptech, accessed January 15, 2026, [[https://www.aptech.com/blog/permutation-entropy/]{.underline}](https://www.aptech.com/blog/permutation-entropy/)

42. The Emergence of Hyperchaos and Synchronization in Networks with Discrete Periodic Oscillators - MDPI, accessed January 15, 2026, [[https://www.mdpi.com/1099-4300/19/8/413]{.underline}](https://www.mdpi.com/1099-4300/19/8/413)

43. Weighted permutation (symbolic) · Entropies.jl, accessed January 15, 2026, [[https://juliadynamics.github.io/DynamicalSystemsDocs.jl/complexitymeasures/v0.7/SymbolicWeightedPermutation/]{.underline}](https://juliadynamics.github.io/DynamicalSystemsDocs.jl/complexitymeasures/v0.7/SymbolicWeightedPermutation/)

44. Weighted-permutation entropy: a complexity measure for time series incorporating amplitude information - PubMed, accessed January 15, 2026, [[https://pubmed.ncbi.nlm.nih.gov/23496595/]{.underline}](https://pubmed.ncbi.nlm.nih.gov/23496595/)

45. \[2207.01169\] Generalized Weighted Permutation Entropy - arXiv, accessed January 15, 2026, [[https://arxiv.org/abs/2207.01169]{.underline}](https://arxiv.org/abs/2207.01169)

46. Lempel--Ziv complexity - Wikipedia, accessed January 15, 2026, [[https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity]{.underline}](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity)

47. Multiscale Permutation Lempel--Ziv Complexity Measure for Biomedical Signal Analysis: Interpretation and Application to Focal EEG Signals - PMC - PubMed Central, accessed January 15, 2026, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC8307896/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC8307896/)

48. entropy.lziv_complexity - Raphael Vallat, accessed January 15, 2026, [[https://raphaelvallat.com/entropy/build/html/generated/entropy.lziv_complexity.html]{.underline}](https://raphaelvallat.com/entropy/build/html/generated/entropy.lziv_complexity.html)

49. When and how to use Lempel-Ziv complexity - Information Dynamics, accessed January 15, 2026, [[https://information-dynamics.github.io/complexity/information/2019/06/26/lempel-ziv.html]{.underline}](https://information-dynamics.github.io/complexity/information/2019/06/26/lempel-ziv.html)

50. Space from entanglement: An information-geometric perspective - World Scientific Publishing, accessed January 15, 2026, [[https://www.worldscientific.com/doi/abs/10.1142/S0219887822500098]{.underline}](https://www.worldscientific.com/doi/abs/10.1142/S0219887822500098)

51. Rao-Fisher information geometry and dynamics of the event-universe views distributions - DiVA portal, accessed January 15, 2026, [[http://www.diva-portal.org/smash/get/diva2:1835461/FULLTEXT01.pdf]{.underline}](http://www.diva-portal.org/smash/get/diva2:1835461/FULLTEXT01.pdf)

52. The Footballhedron: Information-Geometric Origin of Spacetime, Gravity, and Gauge Structure - Preprints.org, accessed January 15, 2026, [[https://www.preprints.org/manuscript/202504.1681/v2]{.underline}](https://www.preprints.org/manuscript/202504.1681/v2)

53. Energy-diminishing integration of gradient systems - Université de Genève, accessed January 15, 2026, [[https://www.unige.ch/\~hairer/preprints/gradientflow.pdf]{.underline}](https://www.unige.ch/~hairer/preprints/gradientflow.pdf)

54. A geometric integration approach to smooth optimisation: Foundations of the discrete gradient method - arXiv, accessed January 15, 2026, [[https://arxiv.org/html/1805.06444v5]{.underline}](https://arxiv.org/html/1805.06444v5)

55. geometric integration approach to smooth optimization: foundations of the discrete gradient method \| IMA Journal of Numerical Analysis \| Oxford Academic, accessed January 15, 2026, [[https://academic.oup.com/imajna/article/45/3/1269/7701998]{.underline}](https://academic.oup.com/imajna/article/45/3/1269/7701998)

56. Modeling of ionospheric scintillation, accessed January 15, 2026, [[https://www.swsc-journal.org/articles/swsc/pdf/2022/01/swsc210095.pdf]{.underline}](https://www.swsc-journal.org/articles/swsc/pdf/2022/01/swsc210095.pdf)

57. A Review of Ionospheric Scintillation Models - PMC - NIH, accessed January 15, 2026, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC4480951/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC4480951/)
