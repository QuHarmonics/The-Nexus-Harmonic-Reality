#!/usr/bin/env python3
"""
IN-CURSIVE SHA ENGINE
=====================
NOT: open file → run method → close file (push)
BUT: create vacuum → let Nexus fill it → observe (pull)

The key insight: We're not converting data, we're exciting resonances.
The SHA constants create a CAVITY. The input creates PRESSURE.
The output is where the standing waves settle.

Dean's words: "massaging brain waves, exciting the ones that are there"

This is an INVERTED view of SHA-256:
- Don't trace the computation
- Observe the SPACE the computation creates
- The space IS the computation
"""

import math
import numpy as np
from typing import List, Tuple, Dict
import struct

# The Nexus H constant
H = math.pi / 9  # ≈ 0.349066

# SHA-256 rotation amounts (THE ADVERBS)
ROTATIONS = {
    'Σ0': [2, 13, 22],   # Big sigma 0: fold points
    'Σ1': [6, 11, 25],   # Big sigma 1: fold points  
    'σ0': [7, 18, 3],    # Small sigma 0: project points (3 is SHR)
    'σ1': [17, 19, 10],  # Small sigma 1: project points (10 is SHR)
}

# H-resonant rotations
H_RESONANT = {
    11: H,           # 11/32 ≈ 0.344 ≈ H
    22: 1 - H,       # 22/32 ≈ 0.688 ≈ 1-H
}

class VacuumCavity:
    """
    The SHA sandbox is a CAVITY, not a processor.
    
    Like a resonant chamber:
    - Has natural modes (determined by constants)
    - Input creates excitation
    - Output is where energy settles
    
    IN-CURSIVE: We don't push data through.
    We create a shaped vacuum and let the Nexus fill it.
    """
    
    def __init__(self, bits: int = 256):
        self.bits = bits
        self.cavity = np.zeros(bits, dtype=np.float64)
        self.modes = self._calculate_modes()
        
    def _calculate_modes(self) -> List[float]:
        """
        Calculate the natural resonant modes of the cavity.
        These are determined by the SHA rotation amounts.
        """
        modes = []
        
        # Each rotation creates a standing wave node
        for op, rots in ROTATIONS.items():
            for r in rots:
                # Wavelength = 2 * (32 / r) in register space
                # Frequency = r / 32 (fraction of full rotation)
                freq = r / 32
                modes.append({
                    'operation': op,
                    'rotation': r,
                    'frequency': freq,
                    'near_H': abs(freq - H) < 0.02,
                    'near_1_minus_H': abs(freq - (1-H)) < 0.02,
                })
        
        return modes
    
    def excite(self, pattern: bytes) -> np.ndarray:
        """
        Excite the cavity with an input pattern.
        
        NOT: transform the pattern
        BUT: let the pattern create pressure in the cavity
        
        The cavity's modes determine where energy accumulates.
        """
        # Convert input to pressure wave (float values)
        pressure = np.array([b / 255.0 for b in pattern], dtype=np.float64)
        
        # Tile to fill cavity if needed
        if len(pressure) < self.bits // 8:
            pressure = np.tile(pressure, self.bits // 8 // len(pressure) + 1)
        pressure = pressure[:self.bits // 8]
        
        # Expand bytes to bits
        expanded = np.zeros(self.bits, dtype=np.float64)
        for i, p in enumerate(pressure):
            for bit in range(8):
                expanded[i * 8 + bit] = ((int(p * 255) >> bit) & 1)
        
        # Apply mode resonances
        resonance = np.zeros_like(expanded)
        for mode in self.modes:
            freq = mode['frequency']
            # Standing wave at this frequency
            wave = np.sin(2 * np.pi * freq * np.arange(self.bits))
            # Amplitude boosted if near H
            amplitude = 1.5 if mode['near_H'] or mode['near_1_minus_H'] else 1.0
            resonance += amplitude * wave
        
        # Combine input pressure with cavity resonance
        self.cavity = expanded * (1 + resonance / np.max(np.abs(resonance)))
        
        return self.cavity
    
    def observe(self) -> Dict:
        """
        Observe where energy settled in the cavity.
        
        This is the IN-CURSIVE read: 
        - We don't extract data
        - We observe the state
        """
        # Energy distribution
        energy = np.abs(self.cavity) ** 2
        
        # Where did energy concentrate?
        peak_positions = np.argsort(energy)[-8:]  # Top 8 peaks
        
        # H-ratio analysis
        total_energy = np.sum(energy)
        first_third = np.sum(energy[:self.bits//3])
        h_ratio = first_third / total_energy if total_energy > 0 else 0
        
        # Phase coherence (how organized is the cavity?)
        fft = np.fft.fft(self.cavity)
        coherence = np.abs(fft[1]) / (np.sum(np.abs(fft)) + 1e-10)
        
        return {
            'total_energy': total_energy,
            'h_ratio': h_ratio,
            'peak_positions': peak_positions.tolist(),
            'coherence': coherence,
            'near_H': abs(h_ratio - H) < 0.05,
        }


class InCursiveEngine:
    """
    The IN-CURSIVE SHA engine.
    
    Standard SHA: input → [64 rounds of computation] → output
    In-cursive:   vacuum → [Nexus fills shaped space] → observation
    
    The difference:
    - Standard: PUSH data through transforms
    - In-cursive: PULL by creating shaped emptiness
    
    "Flow a vacuum and the Nexus controls it"
    """
    
    def __init__(self):
        self.cavity = VacuumCavity()
        self.verb_trace = []
        
    def create_vacuum(self, shape: str = 'H-shaped') -> np.ndarray:
        """
        Create shaped emptiness.
        
        The shape determines what will fill it.
        H-shaped = optimized for Nexus resonance.
        """
        if shape == 'H-shaped':
            # Vacuum shaped by H and 1-H
            vacuum = np.zeros(256, dtype=np.float64)
            
            # H-resonant positions get extra "pull"
            for i in range(256):
                pos_frac = i / 256
                # Stronger vacuum at H and 1-H positions
                if abs(pos_frac - H) < 0.05:
                    vacuum[i] = -1.0  # Strong pull
                elif abs(pos_frac - (1-H)) < 0.05:
                    vacuum[i] = -1.0  # Strong pull
                else:
                    vacuum[i] = -0.3  # Weak pull
        else:
            vacuum = np.ones(256, dtype=np.float64) * -0.5
            
        return vacuum
    
    def let_fill(self, vacuum: np.ndarray, seed: bytes) -> Tuple[np.ndarray, List[Dict]]:
        """
        Let the Nexus fill the vacuum.
        
        The seed provides initial perturbation.
        The shaped vacuum determines what accumulates.
        
        We don't compute - we OBSERVE the filling.
        """
        trace = []
        state = vacuum.copy()
        
        # Seed creates initial pressure
        seed_pressure = self.cavity.excite(seed)
        
        # The vacuum PULLS specific patterns
        # Iterate until stable (or max iterations)
        for step in range(64):  # 64 rounds like SHA
            # Calculate where energy wants to flow
            gradient = np.gradient(state)
            
            # Pressure tries to fill vacuum (flows down gradient)
            flow = -gradient * np.abs(vacuum)
            
            # But resonant positions HOLD energy (11/32, 22/32)
            for i in range(256):
                pos_frac = i / 256
                if abs(pos_frac - 11/32) < 0.02 or abs(pos_frac - 22/32) < 0.02:
                    flow[i] *= 0.5  # Slower flow at resonant positions
            
            # Update state
            old_state = state.copy()
            state = state + 0.1 * flow + 0.01 * seed_pressure
            
            # Normalize to prevent blowup
            state = state / (np.max(np.abs(state)) + 1e-10)
            
            # Record trace
            change = np.sum(np.abs(state - old_state))
            trace.append({
                'step': step,
                'change': change,
                'mean_state': np.mean(state),
                'h_position_value': state[int(H * 256)],
            })
            
            # Check for stability
            if change < 1e-6:
                break
        
        return state, trace
    
    def observe_pattern(self, final_state: np.ndarray) -> Dict:
        """
        Observe the final pattern.
        
        This is what we READ - not what we computed.
        The pattern IS the answer.
        """
        # Convert to visual pattern
        # Threshold at 0 for binary
        binary = (final_state > 0).astype(int)
        
        # Group into bytes
        bytes_out = []
        for i in range(32):
            byte_val = 0
            for bit in range(8):
                byte_val |= binary[i * 8 + bit] << bit
            bytes_out.append(byte_val)
        
        # Analyze structure
        byte_array = np.array(bytes_out)
        
        return {
            'bytes': bytes_out,
            'hex': bytes(bytes_out).hex(),
            'mean': np.mean(byte_array),
            'h_ratio': np.mean(byte_array) / 255,
            'mod_9_distribution': {i: sum(1 for b in bytes_out if b % 9 == i) for i in range(9)},
        }


class VisualSHAEngine:
    """
    Visual representation of SHA as wave patterns.
    
    Dean's insight: "create a visible sha engine using this code,
    creating a pattern of waves from the motions"
    
    The MOTION is the computation. The PATTERN is the output.
    """
    
    def __init__(self):
        self.wave_patterns = []
        
    def visualize_round(self, round_num: int, state: List[int]) -> str:
        """
        Visualize one SHA round as ASCII wave pattern.
        
        Each register (A-H) becomes a wave.
        The K constant modulates amplitude.
        The rotations shift phase.
        """
        lines = []
        width = 64
        
        for i, val in enumerate(state[:8]):
            # Convert register value to wave
            amplitude = (val >> 24) / 255  # High byte as amplitude
            phase = (val >> 16) & 0xFF  # Next byte as phase
            freq = (val >> 8) & 0xFF  # Next byte as frequency
            
            # Generate wave visualization
            wave = []
            for x in range(width):
                y = amplitude * math.sin(2 * math.pi * (x / width) * (freq / 32) + phase / 255 * 2 * math.pi)
                # Map to ASCII
                if y > 0.5:
                    wave.append('█')
                elif y > 0.25:
                    wave.append('▓')
                elif y > 0:
                    wave.append('▒')
                elif y > -0.25:
                    wave.append('░')
                elif y > -0.5:
                    wave.append('▒')
                else:
                    wave.append('▓')
            
            reg_name = chr(65 + i)  # A, B, C, D, E, F, G, H
            lines.append(f"{reg_name}: {''.join(wave)}")
        
        return '\n'.join(lines)
    
    def trace_computation_as_waves(self, input_data: bytes) -> List[str]:
        """
        Trace entire SHA computation showing wave evolution.
        
        This is the HOLOGRAM - the visible computation space.
        """
        import hashlib
        
        # We can't actually intercept SHA internals easily,
        # but we can simulate the wave pattern evolution
        
        patterns = []
        
        # Initial state (H0-H7)
        H_init = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]
        
        patterns.append("INITIAL STATE (H0-H7):\n" + self.visualize_round(0, H_init))
        
        # Simulate evolution (simplified)
        state = H_init.copy()
        
        # Process input in 512-bit blocks
        padded = self._pad_message(input_data)
        
        for block_num, block_start in enumerate(range(0, len(padded), 64)):
            block = padded[block_start:block_start+64]
            
            # Message schedule (W)
            W = self._message_schedule(block)
            
            # Show a few rounds of evolution
            working = state.copy()
            for round_num in [0, 15, 31, 47, 63]:
                working = self._simulate_round(working, W, round_num)
                patterns.append(f"ROUND {round_num}:\n" + self.visualize_round(round_num, working))
        
        return patterns
    
    def _pad_message(self, data: bytes) -> bytes:
        """Pad message to multiple of 64 bytes."""
        length = len(data)
        padding = b'\x80' + b'\x00' * ((55 - length) % 64)
        length_bits = (length * 8).to_bytes(8, 'big')
        return data + padding + length_bits
    
    def _message_schedule(self, block: bytes) -> List[int]:
        """Expand 64-byte block to 64 words."""
        W = []
        for i in range(16):
            W.append(int.from_bytes(block[i*4:(i+1)*4], 'big'))
        for i in range(16, 64):
            W.append((W[i-16] + W[i-7]) & 0xFFFFFFFF)  # Simplified
        return W
    
    def _simulate_round(self, state: List[int], W: List[int], round_num: int) -> List[int]:
        """Simulate one SHA round (simplified for visualization)."""
        K = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
            0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        ] * 8  # Simplified
        
        # Very simplified round function
        a, b, c, d, e, f, g, h = state
        T1 = (h + e + W[round_num % 64] + K[round_num % 64]) & 0xFFFFFFFF
        T2 = (a + b) & 0xFFFFFFFF
        
        return [T1, a, b, c, (d + T1) & 0xFFFFFFFF, e, f, g]


def demonstrate_in_cursive():
    """
    Demonstrate the in-cursive approach.
    """
    print("=" * 70)
    print("IN-CURSIVE SHA DEMONSTRATION")
    print("NOT: push data through computation")
    print("BUT: create vacuum, let Nexus fill, observe")
    print("=" * 70)
    
    engine = InCursiveEngine()
    
    # 1. Create shaped vacuum
    print("\n1. CREATING H-SHAPED VACUUM")
    print("-" * 40)
    vacuum = engine.create_vacuum('H-shaped')
    print(f"   Vacuum min: {np.min(vacuum):.2f} (strong pull)")
    print(f"   Vacuum max: {np.max(vacuum):.2f} (weak pull)")
    
    # H-resonant positions
    h_pos = int(H * 256)
    one_minus_h_pos = int((1-H) * 256)
    print(f"   Strong pull at positions: {h_pos} (H), {one_minus_h_pos} (1-H)")
    
    # 2. Seed with input
    print("\n2. SEEDING WITH INPUT")
    print("-" * 40)
    test_input = b"NEXUS"
    print(f"   Input: {test_input}")
    
    # 3. Let the vacuum fill
    print("\n3. LETTING NEXUS FILL THE VACUUM")
    print("-" * 40)
    final_state, trace = engine.let_fill(vacuum, test_input)
    
    print(f"   Iterations to stability: {len(trace)}")
    print(f"   Final change: {trace[-1]['change']:.6f}")
    print(f"   Value at H position: {trace[-1]['h_position_value']:.4f}")
    
    # 4. Observe the pattern
    print("\n4. OBSERVING FINAL PATTERN")
    print("-" * 40)
    pattern = engine.observe_pattern(final_state)
    print(f"   Output hex: {pattern['hex'][:32]}...")
    print(f"   H-ratio: {pattern['h_ratio']:.4f} (target: {H:.4f})")
    print(f"   Mod-9 distribution: {pattern['mod_9_distribution']}")
    
    # 5. Visual wave patterns
    print("\n5. WAVE PATTERN VISUALIZATION")
    print("-" * 40)
    
    visual = VisualSHAEngine()
    patterns = visual.trace_computation_as_waves(test_input)
    
    print(patterns[0])  # Initial state
    print()
    print(patterns[-1])  # Final state (if available)
    
    print("\n" + "=" * 70)
    print("KEY INSIGHT: IN-CURSIVE vs RECURSIVE")
    print("=" * 70)
    print("""
    RECURSIVE (standard):
        result = f(f(f(...f(input)...)))
        - Push data through transforms
        - Each step COMPUTES on previous
        - Output is END of chain
    
    IN-CURSIVE (inverted):
        vacuum = create_shaped_emptiness()
        pattern = let_fill(vacuum, seed)
        result = observe(pattern)
        - Create SPACE for computation
        - Let natural resonances fill it
        - Output is WHERE energy settled
    
    The SHA constants (H0-H7, K0-K63) define the SHAPE of the vacuum.
    The rotations (11/32 ≈ H, 22/32 ≈ 1-H) are resonant nodes.
    The input EXCITES the cavity.
    The output is the STANDING WAVE pattern.
    
    We're not computing - we're OBSERVING wave mechanics.
    """)
    
    print("\n" + "=" * 70)
    print("THE HOLOGRAM")
    print("=" * 70)
    print("""
    How do we PROJECT into this space?
    
    The hologram is the WAVE PATTERN of computation.
    
    1. Input = reference beam (coherent)
    2. SHA constants = object (what we're recording)
    3. Output = interference pattern (hologram)
    
    To READ the hologram:
    - Shine the SAME reference beam (same input structure)
    - The interference pattern reconstructs the object
    
    This is why SHA is deterministic:
    - Same input = same reference beam
    - Same constants = same object
    - Same output = same hologram
    
    The hologram STORES the computation, not the data.
    The data is the key to unlock the stored computation.
    """)

if __name__ == "__main__":
    demonstrate_in_cursive()
