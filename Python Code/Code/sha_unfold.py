#!/usr/bin/env python3
"""
THE UNFOLD: SHA CONSTANTS AS GENERATIVE ENGINE

The same constants that CREATE the vacuum can UNDO it.
- FOLD (SHA): Collapse TO constant-defined attractors
- UNFOLD (Dream): Expand FROM constant-defined attractors

The constants are bidirectional. They define the landscape.
Same mold, different direction.

Dean Kulik | January 2026
"""

import math
import numpy as np
from typing import List, Tuple

# =============================================================================
# THE SHA CONSTANTS - THESE ARE THE KEYS
# =============================================================================

# Initial hash values: fractional parts of √(first 8 primes)
# These define the STRUCTURE of the vacuum
H_INIT = [
    0x6a09e667,  # √2
    0xbb67ae85,  # √3
    0x3c6ef372,  # √5
    0xa54ff53a,  # √7
    0x510e527f,  # √11
    0x9b05688c,  # √13
    0x1f83d9ab,  # √17
    0x5be0cd19,  # √19
]

# Round constants: fractional parts of ∛(first 64 primes)
# These define the DYNAMICS of the vacuum
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Universal harmonic constant
H = math.pi / 9  # ≈ 0.349066

print("=" * 70)
print("THE UNFOLD: SHA CONSTANTS AS GENERATIVE ENGINE")
print("=" * 70)

# =============================================================================
# EXTRACT H-STRUCTURE FROM CONSTANTS
# =============================================================================

def normalize_constant(c: int) -> float:
    """Normalize 32-bit constant to [0, 1]"""
    return c / 0xFFFFFFFF

def extract_h_signature(constants: List[int]) -> dict:
    """
    Extract the H-signature from SHA constants.
    These define the attractor landscape.
    """
    normalized = [normalize_constant(c) for c in constants]
    
    # Find how many are near H-attractors
    attractors = [0, H, 0.5, 1-H, 1.0]
    
    near_H = sum(1 for n in normalized if abs(n - H) < 0.05)
    near_half = sum(1 for n in normalized if abs(n - 0.5) < 0.05)
    near_1mH = sum(1 for n in normalized if abs(n - (1-H)) < 0.05)
    
    mean = np.mean(normalized)
    
    return {
        'normalized': normalized,
        'mean': mean,
        'near_H': near_H,
        'near_0.5': near_half,
        'near_1-H': near_1mH,
        'distance_from_H': abs(mean - H),
        'distance_from_0.5': abs(mean - 0.5),
    }

print("\n1. H-SIGNATURE IN SHA CONSTANTS")
print("-" * 40)

h_sig = extract_h_signature(H_INIT)
print(f"\nInitial Hash Values (H_INIT):")
print(f"  Mean: {h_sig['mean']:.6f}")
print(f"  Distance from H (0.349): {h_sig['distance_from_H']:.6f}")
print(f"  Distance from 0.5: {h_sig['distance_from_0.5']:.6f}")

k_sig = extract_h_signature(K)
print(f"\nRound Constants (K):")
print(f"  Mean: {k_sig['mean']:.6f}")
print(f"  Distance from H: {k_sig['distance_from_H']:.6f}")
print(f"  Distance from 0.5: {k_sig['distance_from_0.5']:.6f}")

# =============================================================================
# THE UNFOLD FUNCTION
# =============================================================================

print("\n" + "=" * 70)
print("2. THE UNFOLD FUNCTION")
print("=" * 70)

class SHAUnfold:
    """
    Use SHA constants to GENERATE instead of HASH.
    
    The constants created the fold.
    The constants can undo it.
    
    FOLD:   Input → compress through constants → Hash
    UNFOLD: Seed  → expand through constants  → Output
    """
    
    def __init__(self):
        self.H = H
        self.h_init = [normalize_constant(h) for h in H_INIT]
        self.k = [normalize_constant(k) for k in K]
        
    def constant_resonance(self, value: float, round_num: int) -> float:
        """
        Resonate a value with the round constant.
        This is the REVERSE of what SHA does.
        
        SHA: compresses toward constant
        UNFOLD: expands from constant
        """
        k_val = self.k[round_num % 64]
        
        # Instead of mixing DOWN, we mix UP
        # The constant SEEDS the expansion
        expanded = value + k_val * self.H
        
        # Keep in bounds but preserve structure
        return expanded % 1.0
    
    def h_init_seed(self, index: int) -> float:
        """Get initial seed from H_INIT constants"""
        return self.h_init[index % 8]
    
    def unfold_round(self, state: List[float], round_num: int) -> List[float]:
        """
        One round of UNFOLD.
        
        SHA round: state → compress → new_state (smaller info)
        UNFOLD round: state → expand → new_state (richer info)
        """
        new_state = []
        
        for i, val in enumerate(state):
            # Get corresponding constant
            k_val = self.k[(round_num * 8 + i) % 64]
            h_val = self.h_init[i % 8]
            
            # EXPAND instead of COMPRESS
            # SHA: val = (val + k) mod 2^32  (loses info)
            # UNFOLD: val = val * h + k * H  (adds structure)
            
            expanded = val * h_val + k_val * self.H
            
            # Normalize to attractor basin
            normalized = expanded % 1.0
            
            # Slight drift toward H-attractors (the "dream" part)
            attractors = [0, self.H, 0.5, 1-self.H, 1.0]
            nearest = min(attractors, key=lambda a: abs(normalized - a))
            
            # Partial collapse (dreamlike, not hard)
            dream_strength = 0.1
            dreamed = normalized + dream_strength * (nearest - normalized)
            
            new_state.append(dreamed)
        
        return new_state
    
    def unfold(self, seed: bytes, rounds: int = 64) -> np.ndarray:
        """
        Full UNFOLD: seed → expanded output
        
        Uses the same number of rounds as SHA (64)
        but runs expansion instead of compression.
        """
        # Initialize state from seed + H_INIT
        state = []
        for i in range(8):
            if i < len(seed):
                seed_val = seed[i] / 255
            else:
                seed_val = 0.5
            
            # Combine seed with H_INIT constant
            combined = (seed_val + self.h_init[i]) / 2
            state.append(combined)
        
        # Run unfold rounds
        for r in range(rounds):
            state = self.unfold_round(state, r)
        
        return np.array(state)
    
    def dream_generate(self, seed: bytes, length: int = 64) -> np.ndarray:
        """
        Generate a sequence by chained unfolding.
        Like dreaming - each output seeds the next.
        """
        output = []
        current_seed = seed
        
        for i in range(length // 8):
            # Unfold current seed
            unfolded = self.unfold(current_seed, rounds=16)
            output.extend(unfolded)
            
            # Use output as next seed (the dream chain)
            current_seed = bytes([int(v * 255) % 256 for v in unfolded])
        
        return np.array(output[:length])

# Demo
print("\nUnfold Demo:")
unfolder = SHAUnfold()

# Test seed
seed = b"NEXUS"
print(f"\nSeed: '{seed.decode()}'")

# Single unfold
unfolded = unfolder.unfold(seed, rounds=64)
print(f"\nUnfolded (8 values):")
print(f"  {[f'{v:.4f}' for v in unfolded]}")

# Check H-alignment
attractors = [0, H, 0.5, 1-H, 1.0]
near_attractor = sum(
    1 for v in unfolded 
    if any(abs(v - a) < 0.1 for a in attractors)
)
print(f"\n  Values near H-attractors: {near_attractor}/8")

# Dream generation
print(f"\nDream Generation (64 values):")
dreamed = unfolder.dream_generate(seed, length=64)

print(f"  First 8: {[f'{v:.3f}' for v in dreamed[:8]]}")
print(f"  Mean: {np.mean(dreamed):.4f}")
print(f"  Std: {np.std(dreamed):.4f}")

# Distribution analysis
hist, bins = np.histogram(dreamed, bins=10, range=(0, 1))
print(f"\n  Distribution across [0,1]:")
for i in range(10):
    bar = '█' * hist[i]
    print(f"    {bins[i]:.1f}-{bins[i+1]:.1f}: {bar}")

# =============================================================================
# THE FULL CIRCLE
# =============================================================================

print("\n" + "=" * 70)
print("3. THE FULL CIRCLE: FOLD ↔ UNFOLD")
print("=" * 70)

import hashlib

def full_circle_demo(message: str):
    """
    Demonstrate the full circle:
    INPUT → FOLD (SHA) → HASH → UNFOLD → OUTPUT
    
    The OUTPUT resonates with INPUT through the constants.
    """
    print(f"\nMessage: '{message}'")
    
    # FOLD (SHA-256)
    hash_bytes = hashlib.sha256(message.encode()).digest()
    hash_hex = hash_bytes.hex()
    print(f"  FOLD → {hash_hex[:32]}...")
    
    # UNFOLD (using hash as seed)
    unfolder = SHAUnfold()
    unfolded = unfolder.unfold(hash_bytes[:8], rounds=64)
    
    print(f"  UNFOLD → {[f'{v:.3f}' for v in unfolded]}")
    
    # Measure resonance
    # Original message as numbers
    original_vals = [ord(c) / 255 for c in message[:8]]
    while len(original_vals) < 8:
        original_vals.append(0.5)
    
    # Correlation
    corr = np.corrcoef(original_vals, unfolded)[0, 1]
    print(f"  Resonance (correlation): {corr:.4f}")
    
    # H-signature match
    orig_near_H = sum(1 for v in original_vals if abs(v - H) < 0.15 or abs(v - (1-H)) < 0.15)
    unfold_near_H = sum(1 for v in unfolded if abs(v - H) < 0.15 or abs(v - (1-H)) < 0.15)
    print(f"  H-signature: original={orig_near_H}, unfolded={unfold_near_H}")
    
    return hash_hex, unfolded

# Test messages
print("\nFull Circle Tests:")
full_circle_demo("NEXUS")
full_circle_demo("H = pi/9")
full_circle_demo("Dean")

# =============================================================================
# THE INSIGHT
# =============================================================================

print("\n" + "=" * 70)
print("THE INSIGHT")
print("=" * 70)

print("""
THE CONSTANTS ARE BIDIRECTIONAL
───────────────────────────────

SHA uses constants to COMPRESS:
  √2, √3, √5, √7, √11, √13, √17, √19  (H_INIT)
  ∛(primes 1-64)                       (K)
  
These constants DEFINE the vacuum chamber.
They CREATE the attractor landscape.

FOLD:   Input collapses TO constant-defined attractors
UNFOLD: Seed expands FROM constant-defined attractors

SAME CONSTANTS. DIFFERENT DIRECTION.

        ┌─────────────────────────────┐
        │     SHA CONSTANTS           │
        │  (the vacuum definition)    │
        └─────────────┬───────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
    ┌─────────┐             ┌─────────┐
    │  FOLD   │             │ UNFOLD  │
    │  (SHA)  │             │ (Dream) │
    │         │             │         │
    │ compress│             │ expand  │
    │ toward  │             │ from    │
    │constants│             │constants│
    └─────────┘             └─────────┘
          │                       │
          ▼                       ▼
       HASH                   OUTPUT
    (pure state)          (generated)


The unfold IS the training.
The constants ARE the pre-trained weights.
SHA already did the work.
We just run it backwards.


IMPLICATIONS FOR AI:
───────────────────
1. Don't train from scratch
2. Use SHA constants as initialization
3. They already encode H ≈ 0.35
4. They already define the vacuum
5. Generation = unfolding the hash

The model weights should BE the SHA constants.
Training should BE alignment to those constants.
Generation should BE unfolding through them.
""")

# =============================================================================
# PRACTICAL APPLICATION
# =============================================================================

print("\n" + "=" * 70)
print("PRACTICAL: SHA CONSTANTS AS NEURAL NETWORK INIT")
print("=" * 70)

class SHAInitializedLayer:
    """
    Neural network layer initialized with SHA constants.
    The constants already encode H-structure.
    """
    
    def __init__(self, input_dim: int, output_dim: int):
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        # Initialize weights FROM SHA constants
        self.weights = self._sha_init(input_dim, output_dim)
        self.bias = np.array([normalize_constant(k) for k in K[:output_dim]])
        
    def _sha_init(self, m: int, n: int) -> np.ndarray:
        """Initialize weights using SHA constants"""
        weights = np.zeros((m, n))
        
        for i in range(m):
            for j in range(n):
                # Use combination of H_INIT and K
                h_idx = (i + j) % 8
                k_idx = (i * n + j) % 64
                
                h_val = normalize_constant(H_INIT[h_idx])
                k_val = normalize_constant(K[k_idx])
                
                # Combine with H-weighting
                weights[i, j] = h_val * H + k_val * (1 - H)
        
        return weights
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        return np.tanh(x @ self.weights + self.bias)
    
    def measure_h_alignment(self) -> float:
        """How aligned are weights to H-attractors?"""
        flat = self.weights.flatten()
        attractors = [0, H, 0.5, 1-H, 1.0]
        
        aligned = sum(
            1 for w in flat 
            if any(abs(w - a) < 0.05 for a in attractors)
        )
        
        return aligned / len(flat)

# Demo
print("\nSHA-Initialized Layer:")
layer = SHAInitializedLayer(8, 8)

print(f"  Weight shape: {layer.weights.shape}")
print(f"  Weight mean: {np.mean(layer.weights):.4f}")
print(f"  Weight std: {np.std(layer.weights):.4f}")
print(f"  H-alignment: {layer.measure_h_alignment()*100:.1f}%")

# Compare to random init
random_weights = np.random.randn(8, 8) * 0.1
random_aligned = sum(
    1 for w in random_weights.flatten() 
    if any(abs(w - a) < 0.05 for a in [0, H, 0.5, 1-H, 1.0])
)
print(f"\n  Random init H-alignment: {random_aligned/64*100:.1f}%")
print(f"  SHA init is {layer.measure_h_alignment()/(random_aligned/64+0.01):.1f}x more aligned")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
The solution was in the constants all along.

SHA constants = the vacuum definition = the attractor landscape

FOLD uses them to compress.
UNFOLD uses them to expand.
TRAINING uses them as initialization.
GENERATION uses them as the dream engine.

The constants are the universal library.
They already encode H ≈ 0.35.
They already solved the problem.

We just needed to run them the other way.
""")

print("=" * 70)
print("Dean Kulik | January 2026 | ORCID: 0009-0003-3128-8828")
print("=" * 70)
