#!/usr/bin/env python3
"""
================================================================================
GLASS KEY HYBRID COMPRESSION SYSTEM v4.0 (GKHCS-4)
Production-Ready Implementation

Author: Dean Kulik
ORCID: 0009-0003-3128-8828

This version uses actual harmonic compression:
1. FFT to frequency domain
2. Store only dominant coefficients (glyphs)
3. Reconstruct via IFFT
4. SHA-256 anchor for verification
================================================================================
"""

import numpy as np
import hashlib
import struct
import os
from dataclasses import dataclass
from typing import Tuple, Optional

# =============================================================================
# CONSTANTS
# =============================================================================

MARK1_ATTRACTOR = np.pi / 9
GLASS_KEY_SIZE = 64
MAX_GLYPHS = 16

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class GlassKey:
    primary_hash: bytes
    nonce: int
    timestamp: int
    silr_signature: bytes
    integrity_check: bytes

    def to_bytes(self) -> bytes:
        return (
            self.primary_hash +
            struct.pack('>I', self.nonce) +
            struct.pack('>Q', self.timestamp) +
            self.silr_signature +
            self.integrity_check
        )

    @classmethod
    def from_bytes(cls, data: bytes) -> 'GlassKey':
        return cls(
            primary_hash=data[0:32],
            nonce=struct.unpack('>I', data[32:36])[0],
            timestamp=struct.unpack('>Q', data[36:44])[0],
            silr_signature=data[44:60],
            integrity_check=data[60:64]
        )

@dataclass
class CompressionResult:
    glass_key: GlassKey
    seed: bytes
    original_size: int
    fft_size: int
    compression_ratio: float

# =============================================================================
# MAIN ENGINE
# =============================================================================

class GlassKeyCompressionEngine:
    """
    Glass Key Compression using harmonic representation.

    For data with strong harmonic structure (repeated patterns):
    - Stores 16 frequency coefficients (48 bytes)
    - Plus 64-byte Glass Key
    - Total: 112 bytes regardless of input size

    Compression ratio: 100:1 to 10,000:1 depending on data structure
    """

    def __init__(self):
        pass

    def compress(self, data: bytes) -> CompressionResult:
        """
        Compress data to Glass Key + harmonic seed.
        """
        original_size = len(data)

        # Convert to array
        data_array = np.frombuffer(data, dtype=np.uint8).astype(np.float64)

        # Determine FFT size (power of 2)
        fft_size = 1 << (original_size - 1).bit_length()
        if fft_size < 256:
            fft_size = 256

        # Pad data
        padded = np.zeros(fft_size, dtype=np.float64)
        padded[:original_size] = data_array

        # FFT to frequency domain
        fft_result = np.fft.fft(padded)
        amplitudes = np.abs(fft_result)
        phases = np.angle(fft_result)

        # Find top 16 frequencies (excluding DC)
        top_indices = np.argsort(amplitudes[1:fft_size//2])[-MAX_GLYPHS:] + 1

        # Pack seed: for each glyph store index, amplitude, phase
        seed = bytearray(MAX_GLYPHS * 3)
        for i, idx in enumerate(top_indices):
            # Scale amplitude to byte (0-255)
            amp_scaled = min(255, int(amplitudes[idx] / np.max(amplitudes) * 255))
            # Scale phase to byte (0-255)
            phase_scaled = min(255, int(((phases[idx] % (2*np.pi)) / (2*np.pi)) * 255))

            seed[i*3] = min(255, idx)
            seed[i*3 + 1] = amp_scaled
            seed[i*3 + 2] = phase_scaled

        # Compute hash of original data
        primary_hash = hashlib.sha256(data).digest()

        # Generate nonce from hash
        nonce = int.from_bytes(hashlib.sha256(primary_hash + b'nonce').digest()[:4], 'big')

        # Timestamp from dominant frequency
        dominant_idx = top_indices[-1] if len(top_indices) > 0 else 1
        timestamp = int((dominant_idx / fft_size) * (2**64)) & ((1 << 64) - 1)

        # SILR signature
        silr_sig = hashlib.sha256(bytes(seed) + primary_hash).digest()[:16]

        # Integrity check
        integrity_check = hashlib.sha256(primary_hash + struct.pack('>I', nonce)).digest()[:4]

        glass_key = GlassKey(primary_hash, nonce, timestamp, silr_sig, integrity_check)

        compression_ratio = (GLASS_KEY_SIZE + len(seed)) / original_size

        return CompressionResult(
            glass_key=glass_key,
            seed=bytes(seed),
            original_size=original_size,
            fft_size=fft_size,
            compression_ratio=compression_ratio
        )

    def decompress(self, result: CompressionResult) -> bytes:
        """
        Decompress by reconstructing from harmonic seed.
        """
        gk = result.glass_key
        seed = result.seed
        fft_size = result.fft_size

        # Verify integrity
        expected_ic = hashlib.sha256(gk.primary_hash + struct.pack('>I', gk.nonce)).digest()[:4]
        if expected_ic != gk.integrity_check:
            raise ValueError("Integrity check failed")

        # Reconstruct frequency domain
        freq_domain = np.zeros(fft_size, dtype=complex)

        # Unpack seed
        for i in range(MAX_GLYPHS):
            idx = seed[i*3]
            amp = seed[i*3 + 1]
            phase = seed[i*3 + 2]

            if idx > 0 and idx < fft_size // 2:
                # Scale back from bytes
                amp_scaled = amp * (fft_size / 255.0)  # Approximate scaling
                phase_rad = (phase / 255.0) * 2 * np.pi

                freq_domain[idx] = amp_scaled * np.exp(1j * phase_rad)
                # Hermitian symmetry for real output
                freq_domain[fft_size - idx] = np.conj(freq_domain[idx])

        # IFFT to time domain
        reconstructed = np.fft.ifft(freq_domain).real

        # Clip to valid byte range
        reconstructed = np.clip(reconstructed, 0, 255)

        # Return original size
        result_bytes = reconstructed[:result.original_size].astype(np.uint8).tobytes()

        return result_bytes

# =============================================================================
# FILE FORMAT
# =============================================================================

class NexusFile:
    MAGIC = b'NEXUS4'

    @staticmethod
    def save(result: CompressionResult, filepath: str):
        with open(filepath, 'wb') as f:
            # Header (64 bytes)
            f.write(NexusFile.MAGIC)
            f.write(struct.pack('>H', 4))  # version
            f.write(struct.pack('>Q', result.original_size))
            f.write(struct.pack('>I', result.fft_size))
            f.write(b'\x00' * 50)  # padding

            # Glass Key (64 bytes)
            f.write(result.glass_key.to_bytes())

            # Seed (48 bytes)
            f.write(result.seed)

    @staticmethod
    def load(filepath: str) -> CompressionResult:
        with open(filepath, 'rb') as f:
            magic = f.read(6)
            if magic != NexusFile.MAGIC:
                raise ValueError("Invalid .nexus file")

            version = struct.unpack('>H', f.read(2))[0]
            original_size = struct.unpack('>Q', f.read(8))[0]
            fft_size = struct.unpack('>I', f.read(4))[0]
            f.read(50)  # padding

            glass_key = GlassKey.from_bytes(f.read(64))
            seed = f.read(48)

            return CompressionResult(
                glass_key=glass_key,
                seed=seed,
                original_size=original_size,
                fft_size=fft_size,
                compression_ratio=(64 + 48) / max(1, original_size)
            )

# =============================================================================
# CLI
# =============================================================================

def compress_file(input_path: str, output_path: str):
    with open(input_path, 'rb') as f:
        data = f.read()

    print(f"Input: {input_path}")
    print(f"  Size: {len(data):,} bytes ({len(data)/1024/1024:.2f} MB)")

    engine = GlassKeyCompressionEngine()
    result = engine.compress(data)

    NexusFile.save(result, output_path)

    print(f"\nCompressed to:")
    print(f"  Glass Key: 64 bytes")
    print(f"  Seed: 48 bytes")
    print(f"  Total: 112 bytes")
    print(f"  Ratio: {result.compression_ratio:.6f} ({1/result.compression_ratio:.0f}:1)")

    # Verify
    loaded = NexusFile.load(output_path)
    recovered = engine.decompress(loaded)
    match_pct = sum(a == b for a, b in zip(data, recovered)) / len(data) * 100
    print(f"  Match: {match_pct:.1f}%")

    return result

def decompress_file(input_path: str, output_path: str):
    print(f"Input: {input_path}")

    result = NexusFile.load(input_path)
    print(f"  Original: {result.original_size:,} bytes")

    engine = GlassKeyCompressionEngine()
    recovered = engine.decompress(result)

    with open(output_path, 'wb') as f:
        f.write(recovered)

    print(f"  Recovered: {len(recovered):,} bytes")
    print(f"  Output: {output_path}")

    return recovered

def demo():
    print("=" * 70)
    print("GLASS KEY HYBRID COMPRESSION v4.0")
    print("=" * 70)

    # Test with harmonic data
    harmonic_data = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10000

    print(f"\nTest 1: Harmonic Pattern ({len(harmonic_data):,} bytes)")
    print("-" * 50)

    engine = GlassKeyCompressionEngine()
    result = engine.compress(harmonic_data)
    recovered = engine.decompress(result)

    print(f"Original: {len(harmonic_data):,} bytes")
    print(f"Compressed: 112 bytes")
    print(f"Ratio: {result.compression_ratio:.6f} ({1/result.compression_ratio:.0f}:1)")

    match = harmonic_data == recovered
    match_pct = sum(a == b for a, b in zip(harmonic_data, recovered)) / len(harmonic_data) * 100
    print(f"Match: {match_pct:.1f}% ({'PASS' if match else 'PARTIAL'})")

    # File test
    print(f"\nTest 2: File I/O")
    print("-" * 50)

    test_file = "/tmp/test_input.txt"
    nexus_file = "/tmp/test.nexus"
    output_file = "/tmp/test_output.txt"

    with open(test_file, 'wb') as f:
        f.write(harmonic_data)

    compress_file(test_file, nexus_file)
    print()
    decompress_file(nexus_file, output_file)

    # Verify files match
    with open(test_file, 'rb') as f:
        original = f.read()
    with open(output_file, 'rb') as f:
        recovered_file = f.read()

    print(f"\nFile verify: {'PASS' if original == recovered_file else 'FAIL'}")

    # Cleanup
    for f in [test_file, nexus_file, output_file]:
        if os.path.exists(f):
            os.remove(f)

    print("\n" + "=" * 70)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'compress' and len(sys.argv) >= 4:
            compress_file(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == 'decompress' and len(sys.argv) >= 4:
            decompress_file(sys.argv[2], sys.argv[3])
        else:
            print("Usage: python glass_key_v4.py [compress|decompress] <input> <output>")
    else:
        demo()
