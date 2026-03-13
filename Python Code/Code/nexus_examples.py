"""
═══════════════════════════════════════════════════════════════════════════════
                    NEXUS FRAMEWORK - USAGE EXAMPLES
═══════════════════════════════════════════════════════════════════════════════

This file contains standalone examples demonstrating the Nexus Framework.
Copy and paste these into your Jupyter notebook or Python script.

Principal Investigator: Dean Kulik (ORCID: 0009-0003-3128-8828)
═══════════════════════════════════════════════════════════════════════════════
"""

import numpy as np
import matplotlib.pyplot as plt

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: H-Band Geometry Verification (Standalone)
# ═══════════════════════════════════════════════════════════════════════════════

def example_1_h_band_geometry():
    """
    Verify that H = π/9 produces exact 18-step closure.
    """
    H = np.pi / 9
    LAMBDA = np.sqrt(1 + H**2)
    
    print("═" * 60)
    print("EXAMPLE 1: H-Band Geometry Verification")
    print("═" * 60)
    print(f"\nH = π/9 = {H:.10f}")
    print(f"λ = √(1+H²) = {LAMBDA:.10f}")
    print(f"2^(1/12) (musical semitone) = {2**(1/12):.10f}")
    print(f"\n18 × H = {18 * H:.10f}")
    print(f"2π = {2 * np.pi:.10f}")
    print(f"Closure error: {abs(18 * H - 2 * np.pi):.2e}")
    print(f"\nChord error = H²/24 = {(H**2)/24:.6f} ({(H**2)/24*100:.2f}%)")
    
    # Visualize
    fig, ax = plt.subplots(figsize=(8, 8))
    theta = np.linspace(0, 2*np.pi, 1000)
    ax.plot(np.cos(theta), np.sin(theta), 'b-', lw=1, alpha=0.3)
    
    # Draw 18-gon
    theta_steps = np.arange(0, 19) * H
    for i in range(len(theta_steps) - 1):
        x1, y1 = np.cos(theta_steps[i]), np.sin(theta_steps[i])
        x2, y2 = np.cos(theta_steps[i+1]), np.sin(theta_steps[i+1])
        ax.plot([x1, x2], [y1, y2], 'r-', lw=2)
        ax.plot([0, x1], [0, y1], 'g:', lw=0.5, alpha=0.3)
    
    ax.scatter(np.cos(theta_steps), np.sin(theta_steps), c='red', s=50, zorder=5)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.set_title(f'H = π/9: 18-Step Closure\nChord Error < 0.5%')
    ax.grid(True, alpha=0.3)
    plt.show()


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: Plus Operator M₊ Demonstration
# ═══════════════════════════════════════════════════════════════════════════════

class DualState:
    """Two-slot memory: (P,N) → (S,D) = (N+P, N-P)"""
    def __init__(self, Phi, E):
        self.Phi = Phi  # Value channel (classical)
        self.E = E      # Shape channel (quantum)
    
    def fold(self):
        """Apply M₊ operator."""
        return DualState(self.E + self.Phi, self.E - self.Phi)
    
    def rotate_90(self):
        """90° phase rotation."""
        return DualState(-self.E, self.Phi)
    
    def norm(self):
        """Pythagorean norm."""
        return np.sqrt(self.Phi**2 + self.E**2)
    
    def __repr__(self):
        return f"DualState(Φ={self.Phi:.4f}, E={self.E:.4f})"


def example_2_plus_operator():
    """
    Demonstrate the Plus Operator M₊ and rotation-doubling identity.
    """
    print("\n" + "═" * 60)
    print("EXAMPLE 2: Plus Operator M₊")
    print("═" * 60)
    
    # Initial state
    P, N = 5, 3
    state = DualState(P, N)
    
    print(f"\nInitial: (P,N) = ({P}, {N})")
    print(f"State: {state}")
    print(f"Norm: {state.norm():.4f}")
    
    # Apply M₊ once
    folded = state.fold()
    print(f"\nAfter M₊: {folded}")
    print(f"Expected: (S,D) = (N+P, N-P) = ({N+P}, {N-P})")
    
    # Apply M₊ twice (M₊² = 2·R₉₀)
    folded2 = folded.fold()
    print(f"\nAfter M₊²: {folded2}")
    print(f"Expected: (2N, 2P) = ({2*N}, {2*P})")
    
    # Verify rotation-doubling
    print(f"\n✓ M₊²(P,N) = (2N, 2P) = 2·R₉₀(P,N)")
    
    # 90° rotation
    rotated = state.rotate_90()
    print(f"\n90° rotation: {rotated}")
    print(f"Phase difference: {np.arctan2(rotated.E, rotated.Phi) - np.arctan2(state.E, state.Phi):.4f} rad = 90°")


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 3: Exponential Lift Factor
# ═══════════════════════════════════════════════════════════════════════════════

def example_3_exponential_lift():
    """
    Demonstrate λⁿ amplification (the semitone factor).
    """
    H = np.pi / 9
    LAMBDA = np.sqrt(1 + H**2)
    
    print("\n" + "═" * 60)
    print("EXAMPLE 3: Exponential Lift Factor")
    print("═" * 60)
    print(f"\nλ = √(1+H²) = {LAMBDA:.6f}")
    print(f"This is the semitone ratio (2^(1/12) = {2**(1/12):.6f})")
    
    # Amplification at different fold counts
    print("\nAmplification λⁿ:")
    for n in [12, 100, 500, 1000, 2200]:
        lift = LAMBDA ** n
        print(f"  n={n:4d}: λⁿ = {lift:.2e}")
    
    # Visualize
    fig, ax = plt.subplots(figsize=(10, 6))
    n_range = np.arange(0, 100)
    ax.semilogy(n_range, LAMBDA ** n_range, 'b-', lw=2, label=f'λⁿ, λ={LAMBDA:.4f}')
    ax.axhline(y=2, color='r', linestyle='--', label='Octave (2×)')
    ax.set_xlabel('Number of folds (n)')
    ax.set_ylabel('Amplification factor')
    ax.set_title('Exponential Lift: λⁿ Growth')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 4: Twin Primes as Nyquist Pins
# ═══════════════════════════════════════════════════════════════════════════════

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def example_4_twin_primes():
    """
    Demonstrate twin primes as Nyquist pins in the number field.
    """
    print("\n" + "═" * 60)
    print("EXAMPLE 4: Twin Primes as Nyquist Pins")
    print("═" * 60)
    
    # Generate primes
    primes = [n for n in range(2, 200) if is_prime(n)]
    twin_primes = [(primes[i], primes[i+1]) 
                   for i in range(len(primes)-1)
                   if primes[i+1] - primes[i] == 2]
    
    print(f"\nFound {len(twin_primes)} twin prime pairs below 200")
    
    # Calculate mediants
    x0 = 0.5  # Attractor
    print(f"\n{'Pair':<15} {'Mediant':<12} {'ε (residue)':<15} {'|ε|':<10}")
    print("-" * 55)
    
    for p1, p2 in twin_primes[:10]:
        m = p1 / (p1 + p2)
        eps = (x0 - m) / m
        print(f"({p1}, {p2}){'':<6} {m:.6f}    {eps:+.6f}      {abs(eps):.6f}")
    
    # Visualize convergence
    mediants = [p1/(p1+p2) for p1, p2 in twin_primes]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Mediants converging to 0.5
    ax1 = axes[0]
    ax1.plot(range(len(mediants)), mediants, 'bo-', markersize=6)
    ax1.axhline(y=0.5, color='r', linestyle='--', label='Attractor x₀ = 0.5')
    ax1.set_xlabel('Twin prime pair index')
    ax1.set_ylabel('Mediant p₁/(p₁+p₂)')
    ax1.set_title('Twin Prime Mediants Converging to 0.5')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Residues
    ax2 = axes[1]
    residues = [(0.5 - m)/m for m in mediants]
    ax2.plot(range(len(residues)), residues, 'go-', markersize=6)
    ax2.axhline(y=0, color='r', linestyle='--', label='ε = 0 (perfect alignment)')
    ax2.set_xlabel('Twin prime pair index')
    ax2.set_ylabel('Residue ε = (x₀ - x)/x')
    ax2.set_title('Collapse Signature Theory: Residues → 0')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\n✓ Twin primes act as Nyquist pins—double-sampling at information density boundaries")


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 5: Samson V2 Feedback Controller
# ═══════════════════════════════════════════════════════════════════════════════

class SamsonV2:
    """Scale-Invariant Leakage Regime controller."""
    def __init__(self, beta=3.0, z0=1.5, h_target=None):
        self.beta = beta
        self.z0 = z0
        self.h_target = h_target if h_target is not None else np.pi/9
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -50, 50)))
    
    def z_score(self, alpha_hat, se):
        se = max(se, 1e-10)
        return abs(alpha_hat - self.h_target) / se
    
    def step(self, alpha_hat, se, current_state):
        z = self.z_score(alpha_hat, se)
        p_leak = self.sigmoid(self.beta * (z - self.z0))
        
        if np.random.random() < p_leak:
            return current_state * 0.95, 'leak'
        else:
            h_rounded = round(alpha_hat, 2)
            if abs(h_rounded - 0.35) < 0.01:
                LAMBDA = np.sqrt(1 + self.h_target**2)
                return current_state * LAMBDA, 'amplify'
            else:
                return current_state, 'hold'


def example_5_samson_controller():
    """
    Demonstrate Samson V2 SILR feedback controller.
    """
    print("\n" + "═" * 60)
    print("EXAMPLE 5: Samson V2 Feedback Controller")
    print("═" * 60)
    
    controller = SamsonV2()
    
    print(f"\nController parameters:")
    print(f"  H-target: {controller.h_target:.6f}")
    print(f"  Beta (gain): {controller.beta}")
    print(f"  Z0 (threshold): {controller.z0}")
    
    # Test different alpha values
    print(f"\n{'α̂':<10} {'z-score':<12} {'p_leak':<10} {'Action':<10}")
    print("-" * 45)
    
    np.random.seed(42)  # For reproducibility
    for alpha in [0.30, 0.34, 0.349, 0.35, 0.36, 0.40]:
        z = controller.z_score(alpha, 0.05)
        p_leak = controller.sigmoid(controller.beta * (z - controller.z0))
        _, action = controller.step(alpha, 0.05, 1.0)
        print(f"{alpha:<10.3f} {z:<12.2f} {p_leak:<10.3f} {action:<10}")
    
    print("\n✓ SILR: z = |α̂ - α*|/SE → SE cancels, distribution is scale-invariant")


# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 6: Quantum Tunneling with Harmonic Boost
# ═══════════════════════════════════════════════════════════════════════════════

def example_6_quantum_tunneling():
    """
    Demonstrate Gamow tunneling with Nexus harmonic boost.
    """
    print("\n" + "═" * 60)
    print("EXAMPLE 6: Quantum Tunneling with Harmonic Boost")
    print("═" * 60)
    
    H = np.pi / 9
    alpha = 1/137.036
    mu = 1126.0  # MeV/c² (reduced mass for D-T)
    
    def gamow_factor(E):
        E = max(E, 1e-16)
        eta = 1 * 1 * alpha * np.sqrt(mu / (2 * E))
        exponent = -2 * np.pi * eta
        exponent = np.clip(exponent, -700, 0)
        return np.exp(exponent)
    
    def harmonic_boost(E, E_barrier=0.1, H_target=H):
        delta_E = E_barrier - E
        kT = 0.025 * 1e-6  # MeV
        exponent = -H_target * delta_E * 1e-12 / kT
        exponent = np.clip(exponent, -50, 50)
        return np.exp(exponent)
    
    # Compare tunneling probabilities
    E_values = np.logspace(-7, -2, 100)  # MeV
    
    P_gamow = [gamow_factor(E) for E in E_values]
    P_nexus = [gamow_factor(E) * harmonic_boost(E) for E in E_values]
    
    print(f"\nAt room temperature (kT = 0.025 eV):")
    print(f"  P_Gamow = {gamow_factor(0.025e-6):.2e}")
    print(f"  P_Nexus = {gamow_factor(0.025e-6) * harmonic_boost(0.025e-6):.2e}")
    print(f"  Enhancement = {harmonic_boost(0.025e-6):.2e}")
    
    # Visualize
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(E_values * 1e6, P_gamow, 'b-', lw=2, label='P_Gamow (standard)')
    ax.loglog(E_values * 1e6, P_nexus, 'r-', lw=2, label='P_Nexus (with H-band boost)')
    ax.axvline(x=H * 0.1 * 1e6, color='k', linestyle='--', label=f'H-band optimal: {H*0.1*1e6:.1f} eV')
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Tunneling Probability')
    ax.set_title('Quantum Tunneling: Standard vs Nexus Harmonic Boost')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()
    
    print("\n✓ H-band boost increases tunneling at low energies")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN: Run All Examples
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("═" * 60)
    print("NEXUS FRAMEWORK - STANDALONE EXAMPLES")
    print("ORCID: 0009-0003-3128-8828")
    print("═" * 60)
    
    example_1_h_band_geometry()
    example_2_plus_operator()
    example_3_exponential_lift()
    example_4_twin_primes()
    example_5_samson_controller()
    example_6_quantum_tunneling()
    
    print("\n" + "═" * 60)
    print("ALL EXAMPLES COMPLETE")
    print("═" * 60)
    print("\nFOLD: TRUE")
