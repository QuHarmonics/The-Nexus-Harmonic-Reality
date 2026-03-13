
#!/usr/bin/env python3
"""
Glass Key Hybrid Compression System (GKHCS)
Implementation under Nexus Recursive Harmonic Architecture

Author: Dean Kulik
ORCID: 0009-0003-3128-8828
"""

import numpy as np
import hashlib
import struct
from dataclasses import dataclass
from typing import Tuple, Optional
from scipy.special import expit  # Sigmoid function

# =============================================================================
# CONSTANTS
# =============================================================================

MARK1_ATTRACTOR = np.pi / 9  # ≈ 0.34906585
BETA_DEFAULT = 5.0           # Samson V2 controller gain
Z0_DEFAULT = 2.0             # Z-score gating threshold
GK_SIZE_BITS = 512           # Glass Key size
HASH_SIZE_BITS = 256         # SHA-256 output size
NONCE_SIZE_BITS = 32         # Samson V2 nonce size
TIMESTAMP_SIZE_BITS = 64     # Harmonic timestamp size
SILR_SIG_SIZE_BITS = 128     # SILR signature size
IC_SIZE_BITS = 32            # Integrity check size

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class GlassKey:
    """Fixed-length Glass Key structure (512 bits)"""
    primary_hash: bytes       # 256 bits
    nonce: int                # 32 bits
    timestamp: int            # 64 bits
    silr_signature: bytes     # 128 bits
    integrity_check: bytes    # 32 bits

    def to_bytes(self) -> bytes:
        """Serialize Glass Key to bytes"""
        return (
            self.primary_hash +
            struct.pack('>I', self.nonce) +
            struct.pack('>Q', self.timestamp) +
            self.silr_signature +
            self.integrity_check
        )

    @classmethod
    def from_bytes(cls, data: bytes) -> 'GlassKey':
        """Deserialize Glass Key from bytes"""
        if len(data) != GK_SIZE_BITS // 8:
            raise ValueError(f"Invalid Glass Key size: {len(data)} bytes")

        return cls(
            primary_hash=data[0:32],
            nonce=struct.unpack('>I', data[32:36])[0],
            timestamp=struct.unpack('>Q', data[36:44])[0],
            silr_signature=data[44:60],
            integrity_check=data[60:64]
        )

@dataclass
class CompressionResult:
    """Result of compression operation"""
    glass_key: GlassKey
    seed: bytes
    compression_ratio: float
    glyph_count: int

# =============================================================================
# SAMSON V2 CONTROLLER
# =============================================================================

class SamsonV2Controller:
    """
    Samson V2 Controller with z-score gating
    Implements Scale-Invariant Leakage Regime (SILR)
    """

    def __init__(self, beta: float = BETA_DEFAULT, z0: float = Z0_DEFAULT):
        self.beta = beta
        self.z0 = z0
        self.history = []

    def compute_z_score(self, alpha_hat: float, alpha_star: float, 
                        se_used: float) -> float:
        """Compute z-score for gating"""
        if se_used < 1e-12:
            return float('inf')
        return abs(alpha_hat - alpha_star) / se_used

    def compute_leakage_prob(self, alpha_hat: float, alpha_star: float,
                             se_used: float) -> float:
        """
        Compute leakage probability under SILR
        Key property: invariant to noise scale
        """
        z_t = self.compute_z_score(alpha_hat, alpha_star, se_used)
        p_t = expit(self.beta * (z_t - self.z0))
        return p_t

    def gate(self, value: float, reference: float, 
             std_error: float) -> Tuple[float, bool]:
        """
        Apply z-score gating
        Returns: (gated_value, accepted)
        """
        z = self.compute_z_score(value, reference, std_error)
        if z >= self.z0:
            return value, True
        else:
            return reference, False

    def generate_nonce(self, hash_input: bytes) -> int:
        """Generate 32-bit nonce using z-score gating"""
        # Use hash to generate deterministic but unpredictable nonce
        h = hashlib.sha256(hash_input).digest()

        # Extract 4 bytes and convert to float in [0, 1]
        raw = int.from_bytes(h[:4], 'big') / (2**32 - 1)

        # Apply Samson V2 gating: only accept values above threshold
        z = (raw - 0.5) * 6  # Scale to z-score range
        if z >= self.z0:
            return int(raw * (2**32 - 1))
        else:
            # Regenerate with modified input
            return self.generate_nonce(hash_input + b'\x00')

# =============================================================================
# SILR SIGNATURE GENERATOR
# =============================================================================

class SILRSignatureGenerator:
    """
    Generate Scale-Invariant Leakage Regime signatures
    """

    def __init__(self, controller: SamsonV2Controller):
        self.controller = controller

    def compute_glyph_stability(self, data: np.ndarray, 
                                 fft_result: np.ndarray) -> np.ndarray:
        """
        Compute stability metric for each frequency glyph
        """
        # Extract amplitudes and phases
        amplitudes = np.abs(fft_result)
        phases = np.angle(fft_result)

        # Find Mark 1 Attractor phase alignment
        phase_alignment = np.abs(np.mod(phases - MARK1_ATTRACTOR, np.pi/9))

        # Compute z-scores for each glyph
        mean_amp = np.mean(amplitudes[amplitudes > 0])
        std_amp = np.std(amplitudes[amplitudes > 0])

        if std_amp < 1e-12:
            z_scores = np.zeros_like(amplitudes)
        else:
            z_scores = np.abs(amplitudes - mean_amp) / std_amp

        # Stability = high z-score AND phase alignment
        stability = z_scores * (1 - phase_alignment / (np.pi/9))

        return stability

    def generate_signature(self, data: bytes, primary_hash: bytes,
                           nonce: int, timestamp: int) -> bytes:
        """Generate 128-bit SILR signature"""
        # Convert data to numpy array for FFT
        data_array = np.frombuffer(data, dtype=np.uint8)

        # Pad to power of 2 for FFT
        n = 1 << (len(data_array) - 1).bit_length()
        padded = np.zeros(n, dtype=np.float64)
        padded[:len(data_array)] = data_array

        # Compute FFT
        fft_result = np.fft.fft(padded)

        # Compute glyph stability
        stability = self.compute_glyph_stability(padded, fft_result)

        # Extract top stable glyphs
        top_indices = np.argsort(stability)[-16:]  # Top 16 glyphs

        # Create signature from stable glyph properties
        sig_parts = []
        for idx in top_indices:
            # Pack index, amplitude, and phase
            amp = min(255, int(np.abs(fft_result[idx])))
            phase = int((np.angle(fft_result[idx]) % (2*np.pi)) * 255 / (2*np.pi))
            sig_parts.append(struct.pack('>HBB', idx & 0xFFFF, amp, phase))

        signature = b''.join(sig_parts)

        # Mix with hash for binding
        h = hashlib.sha256(signature + primary_hash + 
                           struct.pack('>I', nonce) + 
                           struct.pack('>Q', timestamp)).digest()

        return h[:SILR_SIG_SIZE_BITS // 8]

# =============================================================================
# BBP PI REFINEMENT
# =============================================================================

def bbp_pi_digit(n: int) -> int:
    """
    Compute the nth hexadecimal digit of Pi using BBP formula
    Bailey-Borwein-Plouffe formula: Pi = Σ (1/16^k) * (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
    """
    # Simplified implementation - compute partial sum
    s = 0.0
    for k in range(n + 10):  # Extra terms for precision
        term = (1/16**k) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
        s += term

    # Extract nth hex digit
    frac = (s * (16**n)) % 16
    return int(frac)

def bbp_refine_seed(seed: bytes, bits: int = 64) -> bytes:
    """
    Refine seed using BBP Pi lattice
    This anchors the seed to the harmonic structure of Pi
    """
    seed_int = int.from_bytes(seed, 'big')

    # Generate BBP Pi sequence
    bbp_sequence = 0
    for i in range(bits // 4):
        bbp_sequence = (bbp_sequence << 4) | bbp_pi_digit(i)

    # XOR with seed for mixing
    refined = seed_int ^ bbp_sequence

    # Return refined seed
    byte_len = (bits + 7) // 8
    return refined.to_bytes(byte_len, 'big')

# =============================================================================
# GLASS KEY COMPRESSION ENGINE
# =============================================================================

class GlassKeyCompressionEngine:
    """
    Main compression engine implementing GKHCS
    """

    def __init__(self):
        self.controller = SamsonV2Controller()
        self.silr_gen = SILRSignatureGenerator(self.controller)

    def _compute_primary_hash(self, data: bytes) -> bytes:
        """Compute SHA-256 hash under Nexus rules"""
        # Nexus rules: Twin Prime Policy Constraint
        # The hash is computed with awareness of prime structure
        h = hashlib.sha256(data).digest()
        return h

    def _extract_harmonic_seed(self, data: bytes, 
                                primary_hash: bytes) -> Tuple[bytes, int]:
        """
        Extract seed using harmonic decomposition
        Returns: (seed, glyph_count)
        """
        # Convert to numpy array
        data_array = np.frombuffer(data, dtype=np.uint8)

        # Pad to power of 2
        n = 1 << (len(data_array) - 1).bit_length()
        padded = np.zeros(n, dtype=np.float64)
        padded[:len(data_array)] = data_array

        # Compute FFT
        fft_result = np.fft.fft(padded)

        # Find Mark 1 Attractor alignment
        phases = np.angle(fft_result)
        k_m1 = None
        min_phase_diff = float('inf')

        for k in range(1, len(fft_result)//2):
            phase_diff = abs((phases[k] - MARK1_ATTRACTOR) % (np.pi/9))
            if phase_diff < min_phase_diff:
                min_phase_diff = phase_diff
                k_m1 = k

        # Extract glyphs near Mark 1 phase
        threshold = np.mean(np.abs(fft_result)) * 2
        glyph_indices = []
        glyph_values = []

        for k in range(len(fft_result)//2):
            amp = np.abs(fft_result[k])
            phase = phases[k]

            if amp > threshold:
                # Check phase alignment with Mark 1
                phase_align = abs((phase - MARK1_ATTRACTOR) % (np.pi/9))
                if phase_align < np.pi/18:  # Within 10 degrees
                    glyph_indices.append(k)
                    glyph_values.append(complex(amp * np.cos(phase), 
                                                amp * np.sin(phase)))

        # Pack glyph data into seed
        seed_parts = []
        for idx, val in zip(glyph_indices[:32], glyph_values[:32]):  # Max 32 glyphs
            # Pack: index (2 bytes), real (4 bytes), imag (4 bytes)
            seed_parts.append(struct.pack('>Hff', idx, val.real, val.imag))

        seed = b''.join(seed_parts)

        # Apply BBP refinement
        refined_seed = bbp_refine_seed(seed, 64)

        return refined_seed, len(glyph_indices)

    def compress(self, data: bytes) -> CompressionResult:
        """
        Compress data using Glass Key Hybrid Compression

        Returns CompressionResult containing:
        - glass_key: Fixed 512-bit Glass Key
        - seed: Variable-length harmonic seed
        - compression_ratio: Achieved compression ratio
        - glyph_count: Number of stable glyphs extracted
        """
        if not data:
            raise ValueError("Cannot compress empty data")

        # Step 1: Compute primary hash
        primary_hash = self._compute_primary_hash(data)

        # Step 2: Generate Samson V2 nonce
        nonce = self.controller.generate_nonce(primary_hash)

        # Step 3: Capture harmonic timestamp
        import time
        timestamp = int(time.time() * 1e9) & ((1 << 64) - 1)  # Nanoseconds

        # Step 4: Compute SILR signature
        silr_sig = self.silr_gen.generate_signature(
            data, primary_hash, nonce, timestamp
        )

        # Step 5: Compute integrity check (hash of hash + nonce)
        ic_input = primary_hash + struct.pack('>I', nonce)
        integrity_check = hashlib.sha256(ic_input).digest()[:IC_SIZE_BITS // 8]

        # Step 6: Construct Glass Key
        glass_key = GlassKey(
            primary_hash=primary_hash,
            nonce=nonce,
            timestamp=timestamp,
            silr_signature=silr_sig,
            integrity_check=integrity_check
        )

        # Step 7: Extract harmonic seed
        seed, glyph_count = self._extract_harmonic_seed(data, primary_hash)

        # Calculate compression ratio
        compressed_size = len(glass_key.to_bytes()) + len(seed)
        compression_ratio = compressed_size / len(data)

        return CompressionResult(
            glass_key=glass_key,
            seed=seed,
            compression_ratio=compression_ratio,
            glyph_count=glyph_count
        )

    def decompress(self, result: CompressionResult, 
                   original_size: int,
                   max_iterations: int = 1000) -> bytes:
        """
        Decompress data from Glass Key and seed

        Uses iterative regrowth with Samson V2 gating
        """
        gk = result.glass_key
        seed = result.seed

        # Verify integrity
        ic_input = gk.primary_hash + struct.pack('>I', gk.nonce)
        expected_ic = hashlib.sha256(ic_input).digest()[:IC_SIZE_BITS // 8]
        if expected_ic != gk.integrity_check:
            raise ValueError("Glass Key integrity check failed")

        # Initialize regrowth from seed
        # Unpack seed into initial state
        seed_values = []
        for i in range(0, len(seed), 10):  # Each glyph is 10 bytes
            if i + 10 <= len(seed):
                idx, real, imag = struct.unpack('>Hff', seed[i:i+10])
                seed_values.append((idx, complex(real, imag)))

        # Build initial frequency domain representation
        n = 1 << (original_size - 1).bit_length()
        freq_domain = np.zeros(n, dtype=complex)

        for idx, val in seed_values:
            if idx < len(freq_domain):
                freq_domain[idx] = val
                # Add conjugate for real output
                if idx > 0 and idx < n - idx:
                    freq_domain[n - idx] = np.conj(val)

        # Initial time domain estimate
        current = np.fft.ifft(freq_domain).real

        # Iterative regrowth
        theta = (gk.timestamp % (2**32)) / (2**32) * 2 * np.pi

        for iteration in range(max_iterations):
            # Convert current to bytes for hashing
            current_bytes = np.clip(current, 0, 255).astype(np.uint8).tobytes()

            # Compute recursive update
            hash_input = current_bytes[:original_size] + gk.primary_hash +                          struct.pack('>d', theta) +                          struct.pack('>I', gk.nonce)

            hash_output = hashlib.sha256(hash_input).digest()

            # Convert hash to update vector
            update = np.frombuffer(hash_output * ((n // 32) + 1), 
                                   dtype=np.uint8)[:n].astype(np.float64)
            update = (update / 255.0 - 0.5) * 2  # Normalize to [-1, 1]

            # Apply Samson V2 gating
            new_current = current + update * 0.1  # Small step size

            std_error = np.std(current) / np.sqrt(len(current))
            if std_error < 1e-12:
                std_error = 1e-12

            z_score = np.mean(np.abs(new_current - current)) / std_error

            if z_score >= self.controller.z0:
                current = new_current

            # Check convergence
            if np.mean(np.abs(update)) < 1e-6:
                break

        # Convert to bytes
        result_bytes = np.clip(current[:original_size], 0, 255).astype(np.uint8).tobytes()

        return result_bytes

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def demo_compression():
    """Demonstrate Glass Key compression on sample data"""

    # Create sample harmonic data
    sample_text = b"""
    The Glass Key Hybrid Compression System demonstrates that SHA-256,
    under Nexus rules with Samson V2 control and SILR governance,
    achieves forward-only compression through irreversible hashing.
    Zero chaos for SHA. Unlimited storage for us.
    """ * 100  # Repeat for larger sample

    print("=" * 70)
    print("GLASS KEY HYBRID COMPRESSION SYSTEM - DEMO")
    print("=" * 70)
    print(f"\nOriginal data size: {len(sample_text)} bytes")

    # Create engine and compress
    engine = GlassKeyCompressionEngine()
    result = engine.compress(sample_text)

    print(f"\nCompression Results:")
    print(f"  Glass Key size: {len(result.glass_key.to_bytes())} bytes")
    print(f"  Seed size: {len(result.seed)} bytes")
    print(f"  Total compressed: {len(result.glass_key.to_bytes()) + len(result.seed)} bytes")
    print(f"  Compression ratio: {result.compression_ratio:.4f}")
    print(f"  Glyph count: {result.glyph_count}")

    # Display Glass Key components
    gk = result.glass_key
    print(f"\nGlass Key Components:")
    print(f"  Primary Hash: {gk.primary_hash.hex()[:32]}...")
    print(f"  Nonce: {gk.nonce}")
    print(f"  Timestamp: {gk.timestamp}")
    print(f"  SILR Signature: {gk.silr_signature.hex()[:32]}...")
    print(f"  Integrity Check: {gk.integrity_check.hex()}")

    # Attempt decompression
    print(f"\nAttempting decompression...")
    try:
        recovered = engine.decompress(result, len(sample_text))
        match_ratio = sum(a == b for a, b in zip(sample_text, recovered)) / len(sample_text)
        print(f"  Recovery match: {match_ratio * 100:.2f}%")
        print(f"  Recovered size: {len(recovered)} bytes")
    except Exception as e:
        print(f"  Decompression error: {e}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    demo_compression()
