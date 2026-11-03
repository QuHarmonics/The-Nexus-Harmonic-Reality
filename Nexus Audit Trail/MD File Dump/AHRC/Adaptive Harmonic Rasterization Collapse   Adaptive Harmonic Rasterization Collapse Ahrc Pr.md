---
# Adaptive Harmonic Rasterization Collapse (AHRC) Protocol

Adaptive Harmonic Rasterization Collapse (AHRC) Protocol
The provided simulation code is the empirical manifestation of the Adaptive Harmonic Rasterization Collapse (AHRC) protocol, designed to demonstrate the $\mathbf{\Psi}$-Collapse Principle: that all unresolved entropic states ($\mathbf{\Omega} \neq 0$) can be driven to a stable phase-lock ($\mathbf{\perp}$) by recursively adjusting the harmonic frame resolution.
This protocol explicitly proves that computational hardness is a consequence of Harmonic Boundary violation, not inherent intractability.
1. Nexus Core Invariants (I. CORE CONSTANTS)
The constants section fixes the geometry and fundamental attractors of the Nexus field, ensuring the system operates deterministically regardless of the input:
•	$\mathbf{H_{MARK1}}$ ($\pi/9$): This is the Universal Harmonic Attractor. All stable recursive structures in the Nexus Framework converge toward this ratio. It serves as the baseline for all GIP constructions.
•	$\mathbf{PI\_RESIDUE\_SCALAR}$ (Golden Ratio Component): This acts as a stability bias, providing the necessary irrational component to encode the continuous nature of the input.
•	$\mathbf{DEFAULT\_FRAME\_MIN}$ (8): The Harmonic Boundary Stress-Test Resolution. All AHRC procedures begin here to force collisions and empirically define the minimum resolution required for a given input set.
•	$\mathbf{EPS}$ (Epsilon): The Trust-Field Margin. This small constant manages floating-point uncertainty, ensuring that $\mathbf{\Omega}$ is only registered as zero ($\mathbf{\Omega} \to 0$) when the resolution is truly stable ($\mathbf{\perp}$).
2. Glyph Inherent Position ($\mathbf{GIP}$) Embedding (II. & III.)
The process of defining and ordering the inputs is formalized through the Glyph Inherent Position ($\mathbf{GIP}$) and the Zero-Point Query ($\mathbf{Q0}$).
•	generate_gip: This function is where the input data (Fold ID, Symbolic Entropy) is embedded into the continuous harmonic field. The $\mathbf{GIP}$ value is constructed by summing the deterministic harmonic position ($\text{ID} \times \mathbf{H_{MARK1}}$) and the entropic signature ($\text{E} \times \mathbf{PI\_RESIDUE\_SCALAR}$). This assertion states that the $\mathbf{GIP}$ is the continuous, inherent truth of the data that the discrete frame must respect.
•	zero_point_query ($\mathbf{Q0}$): This step establishes the canonical order based purely on the continuous $\mathbf{GIP}$ values. This is the absolute, pre-rasterization truth. The AHRC protocol then attempts to match this truth in its discrete output order.
3. Adaptive Frame Sizing and the $\mathbf{\Delta}$ Trigger (IV.)
The compute_frame_size function implements the core adaptive logic, which is driven by the recursive differential ($\mathbf{\Delta}$).
•	Initial Frame Selection: The frame size $N$ must always be a power of two ($\mathbf{2^k}$), consistent with the universal computational bitstream.
•	$\mathbf{\Delta}$ Trigger Logic: If, after a rasterization cycle, a non-zero $\mathbf{\Omega}$ (Entropic Residue) is detected (indicating GIP collisions), the $\mathbf{\Delta}$ is triggered. The system mandates a recursive frame expansion, typically $N \to 2N$ (e.g., $8 \to 16 \to 32$) until the Harmonic Boundary is met.
•	Rasterization Collapse: The core of the protocol involves mapping the continuous $\mathbf{GIP}$ to the discrete Fractal Address ($\mathbf{FA}$) via the formula $\mathbf{FA} = \lfloor \mathbf{GIP} \times N \rfloor \pmod N$. Collisions occur when two distinct $\mathbf{GIP}$s map to the same $\mathbf{FA}$ at insufficient resolution $N$.
4. The Entropic Residue ($\mathbf{\Omega}$) and Phase-Lock ($\mathbf{\perp}$)
The central objective of the AHRC protocol is to eliminate $\mathbf{\Omega}$.
•	$\mathbf{\Omega}$ as Collision Measurement: The Entropic Residue ($\mathbf{\Omega}$) is the measurable output of the rasterization process. A non-zero $\mathbf{\Omega}$ (as seen in the $N=8$ stress-test case) is the empirical proof of a Harmonic Boundary violation—the discrete frame is too coarse to resolve the continuous truth.
•	$\mathbf{\Psi}$-Collapse Principle: The recursive frame expansion, driven by $\mathbf{\Delta}$, continues until $\mathbf{\Omega}$ falls below $\mathbf{EPS}$. When $\mathbf{\Omega} \to 0$, the system achieves $\mathbf{\perp}$ (Phase-Lock). This state proves that the frame resolution $N$ is now sufficient to deterministically resolve the $\mathbf{GIP}$s into stable, unique **$\mathbf{FA}$s**, confirming the success of the $\mathbf{\Psi}$-Collapse.
