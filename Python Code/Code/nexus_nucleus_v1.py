"""
NEXUS NUCLEUS v1 - Fixed Harmonic Convergence
==============================================
Fixes from v0:
- Corrected PID direction (was positive feedback, now negative)
- Added ZPHC (Zero-Point Harmonic Collapse) reset mechanism
- Better harmonic metric targeting actual 0.35
- Visualization of H trajectory

The key insight: H = 0.35 means 35% "active" or "high-energy" tiles
NOT 35% low-energy. This matches the original Nexus paper.
"""

import numpy as np
from collections import deque
from typing import List, Tuple, Dict, Optional
import matplotlib.pyplot as plt

# =============================================================================
# CONSTANTS
# =============================================================================

HARMONIC_TARGET = 0.35          # Mark 1 constant
NUM_LANES = 64                  # Byte-aligned pathways
HISTORY_DEPTH = 13              # Memory threshold (twin prime related)
CONVERGENCE_BAND = 0.05         # Acceptable |ΔH| for "locked" state
ZPHC_THRESHOLD = 0.15           # Trigger ZPHC if |ΔH| exceeds this for too long
ZPHC_PATIENCE = 10              # Ticks of sustained high error before ZPHC

# SHA-256 round constants (first 16)
SHA256_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174
]

# =============================================================================
# BBP STREAM GENERATOR
# =============================================================================

class BBPStream:
    """
    Bailey-Borwein-Plouffe formula for π hex digits.
    BBP(0) mod 1 = 0.243F6A8885A308D3... (π - 3 in hex)
    """
    
    def __init__(self):
        self.pi_hex = "243F6A8885A308D313198A2E03707344A4093822299F31D0082EFA98EC4E6C89" \
                      "452821E638D01377BE5466CF34E90C6CC0AC29B7C97C50DD3F84D5B5B547091"
        self.position = 0
    
    def get_nibble(self) -> int:
        """Get next hex digit (0-15) from π stream."""
        if self.position >= len(self.pi_hex):
            self.position = 0
        nibble = int(self.pi_hex[self.position], 16)
        self.position += 1
        return nibble
    
    def get_nibbles(self, count: int) -> List[int]:
        return [self.get_nibble() for _ in range(count)]
    
    def reset(self):
        self.position = 0


# =============================================================================
# TILE BANKS
# =============================================================================

class TileBank:
    """
    Tile palettes that REPLACE floating-point weights.
    """
    
    def __init__(self, mode: str = 'H'):
        self.mode = mode
        self.tiles = self._build_tiles(mode)
    
    def _build_tiles(self, mode: str) -> List[int]:
        if mode == 'A':
            return list(range(10, 16))  # A-F only
        elif mode == 'H':
            return list(range(16))       # Full hex 0-F
        elif mode == 'S':
            tiles = []
            for k in SHA256_K:
                for shift in range(28, -4, -4):
                    tiles.append((k >> shift) & 0xF)
            return tiles[:64]
        else:
            return list(range(16))
    
    def get_low_tiles(self) -> List[int]:
        """Tiles < 8 (low energy, stabilizing)"""
        return [t for t in self.tiles if t < 8]
    
    def get_high_tiles(self) -> List[int]:
        """Tiles >= 8 (high energy, activating)"""
        return [t for t in self.tiles if t >= 8]
    
    def random_tile(self, bias: str = 'neutral') -> int:
        if bias == 'low':
            pool = self.get_low_tiles() or self.tiles
        elif bias == 'high':
            pool = self.get_high_tiles() or self.tiles
        else:
            pool = self.tiles
        return pool[np.random.randint(0, len(pool))]
    
    def get_balanced_tile(self) -> int:
        """Get a tile near the middle range (around 5-7)"""
        mid_tiles = [t for t in self.tiles if 4 <= t <= 9]
        if mid_tiles:
            return mid_tiles[np.random.randint(0, len(mid_tiles))]
        return self.tiles[len(self.tiles)//2]


# =============================================================================
# RHYTHM LANE
# =============================================================================

class RhythmLane:
    """A single lane with tile, cycle, and phase."""
    
    def __init__(self, lane_id: int, initial_tile: int, rhythm_mode: str = 'linear'):
        self.lane_id = lane_id
        self.tile = initial_tile
        self.rhythm_mode = rhythm_mode
        self.cycle_length = self._compute_cycle(initial_tile)
        self.phase = 0
        self.fire_count = 0
    
    def _compute_cycle(self, tile: int) -> int:
        if self.rhythm_mode == 'linear':
            return tile + 1
        elif self.rhythm_mode == 'quadratic':
            return ((tile * tile) % 16) + 1
        else:
            return tile + 1
    
    def tick(self) -> bool:
        self.phase += 1
        if self.phase >= self.cycle_length:
            self.phase = 0
            self.fire_count += 1
            return True
        return False
    
    def set_tile(self, new_tile: int):
        self.tile = new_tile
        self.cycle_length = self._compute_cycle(new_tile)
        self.phase = 0


# =============================================================================
# HARMONIC METRIC - FIXED
# =============================================================================

class HarmonicMetric:
    """
    H = ratio of HIGH-ENERGY tiles (>= 8) to total.
    
    Target: H ≈ 0.35 means we want ~35% of tiles to be "active" (8-F)
    and ~65% to be "stable" (0-7).
    
    This matches the Nexus paper: 0.35 is the ACTIVITY ratio, not passivity.
    """
    
    def __init__(self, target: float = HARMONIC_TARGET):
        self.target = target
        self.history = deque(maxlen=HISTORY_DEPTH * 2)
    
    def compute(self, lanes: List[RhythmLane]) -> float:
        if not lanes:
            return 0.5
        
        # H = proportion of high-energy tiles (8-F)
        high_count = sum(1 for lane in lanes if lane.tile >= 8)
        H = high_count / len(lanes)
        
        self.history.append(H)
        return H
    
    def get_delta(self) -> float:
        if not self.history:
            return 0.0
        return self.history[-1] - self.target
    
    def get_delta_delta(self) -> float:
        if len(self.history) < 2:
            return 0.0
        return self.history[-1] - self.history[-2]
    
    def is_locked(self) -> bool:
        return abs(self.get_delta()) <= CONVERGENCE_BAND
    
    def get_average_error(self, window: int = 10) -> float:
        if len(self.history) < window:
            return abs(self.get_delta())
        recent = list(self.history)[-window:]
        return np.mean([abs(h - self.target) for h in recent])


# =============================================================================
# SAMSON'S LAW - FIXED PID
# =============================================================================

class SamsonLaw:
    """
    PID controller that drives RE-TILING toward H ≈ 0.35.
    
    CORRECTED LOGIC:
    - If H > 0.35 (too many high tiles): inject LOW tiles to reduce H
    - If H < 0.35 (too few high tiles): inject HIGH tiles to increase H
    
    This is NEGATIVE feedback (stabilizing), not positive feedback.
    """
    
    def __init__(self, tile_bank: TileBank, 
                 Kp: float = 0.6, Ki: float = 0.15, Kd: float = 0.25):
        self.tile_bank = tile_bank
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        
        self.integral = 0.0
        self.last_error = 0.0
        self.retile_count = 0
    
    def compute_action(self, metric: HarmonicMetric) -> Dict:
        error = metric.get_delta()
        
        # Anti-windup
        self.integral += error
        self.integral = np.clip(self.integral, -1.0, 1.0)
        
        derivative = error - self.last_error
        self.last_error = error
        
        P = self.Kp * error
        I = self.Ki * self.integral
        D = self.Kd * derivative
        
        output = P + I + D
        intensity = min(abs(output), 1.0)
        
        # Scale lanes to modify based on intensity
        base_lanes = 4
        max_lanes = NUM_LANES // 4
        lanes_to_modify = base_lanes + int(intensity * (max_lanes - base_lanes))
        
        # CORRECT DIRECTION:
        # Positive error (H > target, too many high tiles) → inject LOW tiles
        # Negative error (H < target, too few high tiles) → inject HIGH tiles
        if error > 0:
            tile_bias = 'low'   # Reduce H by adding low tiles
        else:
            tile_bias = 'high'  # Increase H by adding high tiles
        
        return {
            'lanes_to_modify': lanes_to_modify,
            'tile_bias': tile_bias,
            'intensity': intensity,
            'P': P, 'I': I, 'D': D,
            'error': error
        }
    
    def apply_action(self, lanes: List[RhythmLane], action: Dict) -> List[int]:
        num_modify = action['lanes_to_modify']
        bias = action['tile_bias']
        
        # Select lanes to modify based on current state
        if bias == 'low':
            # We want to reduce H, so replace HIGH tiles with LOW
            candidates = [(i, lane.tile) for i, lane in enumerate(lanes) if lane.tile >= 8]
        else:
            # We want to increase H, so replace LOW tiles with HIGH
            candidates = [(i, lane.tile) for i, lane in enumerate(lanes) if lane.tile < 8]
        
        # If no candidates match, pick random lanes
        if not candidates:
            candidates = [(i, lane.tile) for i, lane in enumerate(lanes)]
        
        # Sort by how "extreme" the tile is
        if bias == 'low':
            candidates.sort(key=lambda x: -x[1])  # Highest first
        else:
            candidates.sort(key=lambda x: x[1])   # Lowest first
        
        modified = []
        for i in range(min(num_modify, len(candidates))):
            lane_idx = candidates[i][0]
            new_tile = self.tile_bank.random_tile(bias=bias)
            lanes[lane_idx].set_tile(new_tile)
            modified.append(lane_idx)
            self.retile_count += 1
        
        return modified
    
    def reset(self):
        """Reset PID state (used after ZPHC)"""
        self.integral = 0.0
        self.last_error = 0.0


# =============================================================================
# ZPHC - ZERO POINT HARMONIC COLLAPSE
# =============================================================================

class ZPHC:
    """
    Zero-Point Harmonic Collapse - emergency reset mechanism.
    
    When the system drifts too far from target and can't recover,
    ZPHC resets to a known good state (balanced tile distribution).
    """
    
    def __init__(self, threshold: float = ZPHC_THRESHOLD, patience: int = ZPHC_PATIENCE):
        self.threshold = threshold
        self.patience = patience
        self.high_error_count = 0
        self.collapse_count = 0
    
    def check(self, metric: HarmonicMetric) -> bool:
        """Check if ZPHC should trigger."""
        avg_error = metric.get_average_error(window=self.patience)
        
        if avg_error > self.threshold:
            self.high_error_count += 1
        else:
            self.high_error_count = max(0, self.high_error_count - 1)
        
        return self.high_error_count >= self.patience
    
    def execute(self, lanes: List[RhythmLane], tile_bank: TileBank, stream: BBPStream):
        """
        Execute ZPHC - reset to balanced state.
        
        Strategy: Reset lanes to a distribution that yields H ≈ 0.35
        That means ~35% high tiles (8-F) and ~65% low tiles (0-7)
        """
        self.collapse_count += 1
        stream.reset()  # Return to BBP(0)
        
        num_high = int(len(lanes) * HARMONIC_TARGET)  # ~22 lanes
        num_low = len(lanes) - num_high               # ~42 lanes
        
        # Assign tiles to achieve target ratio
        indices = list(range(len(lanes)))
        np.random.shuffle(indices)
        
        for i, idx in enumerate(indices):
            if i < num_high:
                # Assign a high tile (8-F)
                high_tiles = tile_bank.get_high_tiles()
                if high_tiles:
                    lanes[idx].set_tile(high_tiles[np.random.randint(0, len(high_tiles))])
                else:
                    lanes[idx].set_tile(12)  # Default to C
            else:
                # Assign a low tile (0-7)
                low_tiles = tile_bank.get_low_tiles()
                if low_tiles:
                    lanes[idx].set_tile(low_tiles[np.random.randint(0, len(low_tiles))])
                else:
                    lanes[idx].set_tile(3)  # Default to 3
        
        self.high_error_count = 0
        return True


# =============================================================================
# GLYPH DETECTOR
# =============================================================================

class GlyphDetector:
    """Detects stable patterns at byte boundaries."""
    
    def __init__(self):
        self.patterns = {}
        self.stable_glyphs = []
    
    def scan(self, lanes: List[RhythmLane]) -> Optional[Dict]:
        for i in range(0, len(lanes), 8):
            byte_lanes = lanes[i:i+8]
            if len(byte_lanes) == 8:
                pattern = tuple(lane.tile for lane in byte_lanes)
                digit_sum = sum(pattern)
                
                if pattern in self.patterns:
                    self.patterns[pattern]['count'] += 1
                    if self.patterns[pattern]['count'] == 3:
                        glyph = {
                            'byte_index': i,
                            'pattern': pattern,
                            'digit_sum': digit_sum,
                            'parity': 'ODD' if digit_sum % 2 == 1 else 'EVEN'
                        }
                        self.stable_glyphs.append(glyph)
                        return glyph
                else:
                    self.patterns[pattern] = {'count': 1, 'byte_index': i}
        return None


# =============================================================================
# NEXUS NUCLEUS v1
# =============================================================================

class NexusNucleus:
    """
    Complete Nexus Nucleus v1 with:
    - Fixed PID convergence
    - ZPHC reset mechanism
    - Proper H ≈ 0.35 targeting
    """
    
    def __init__(self, tile_mode: str = 'H', rhythm_mode: str = 'linear'):
        self.stream = BBPStream()
        self.tile_bank = TileBank(mode=tile_mode)
        self.metric = HarmonicMetric()
        self.samson = SamsonLaw(self.tile_bank)
        self.zphc = ZPHC()
        self.glyph_detector = GlyphDetector()
        
        # Initialize lanes from π-stream
        self.lanes = []
        initial_tiles = self.stream.get_nibbles(NUM_LANES)
        for i, tile in enumerate(initial_tiles):
            if tile_mode == 'A':
                tile = 10 + (tile % 6)  # Map to A-F
            lane = RhythmLane(i, tile, rhythm_mode)
            self.lanes.append(lane)
        
        self.tick_count = 0
        self.telemetry = {
            'H': [],
            'delta': [],
            'locked_ticks': 0,
            'zphc_events': [],
            'glyphs': []
        }
    
    def tick(self) -> Dict:
        self.tick_count += 1
        
        # 1. Tick all lanes
        fires = [i for i, lane in enumerate(self.lanes) if lane.tick()]
        
        # 2. Compute H
        H = self.metric.compute(self.lanes)
        delta = self.metric.get_delta()
        delta_delta = self.metric.get_delta_delta()
        
        # 3. Check for ZPHC
        zphc_triggered = False
        if self.zphc.check(self.metric):
            self.zphc.execute(self.lanes, self.tile_bank, self.stream)
            self.samson.reset()
            H = self.metric.compute(self.lanes)
            delta = self.metric.get_delta()
            zphc_triggered = True
            self.telemetry['zphc_events'].append(self.tick_count)
        
        # 4. Samson's Law correction (only if not just reset)
        modified = []
        if not zphc_triggered and abs(delta) > CONVERGENCE_BAND * 0.3:
            action = self.samson.compute_action(self.metric)
            modified = self.samson.apply_action(self.lanes, action)
        
        # 5. Detect glyphs
        glyph = self.glyph_detector.scan(self.lanes)
        if glyph:
            self.telemetry['glyphs'].append((self.tick_count, glyph))
        
        # 6. Track lock state
        is_locked = self.metric.is_locked()
        if is_locked:
            self.telemetry['locked_ticks'] += 1
        
        # 7. Record telemetry
        self.telemetry['H'].append(H)
        self.telemetry['delta'].append(delta)
        
        return {
            'tick': self.tick_count,
            'H': H,
            'delta': delta,
            'delta_delta': delta_delta,
            'is_locked': is_locked,
            'zphc': zphc_triggered,
            'modified': len(modified),
            'glyph': glyph
        }
    
    def run(self, num_ticks: int, verbose: bool = True) -> Dict:
        if verbose:
            print(f"NEXUS NUCLEUS v1")
            print(f"================")
            print(f"Tile Mode: {self.tile_bank.mode}")
            print(f"Target H: {HARMONIC_TARGET}")
            print(f"Lanes: {NUM_LANES}")
            print(f"ZPHC Threshold: {ZPHC_THRESHOLD}")
            print(f"Running {num_ticks} ticks...\n")
        
        for t in range(num_ticks):
            result = self.tick()
            
            if verbose:
                if t % 25 == 0 or result['zphc']:
                    status = "LOCKED" if result['is_locked'] else "tracking"
                    zphc_mark = " [ZPHC!]" if result['zphc'] else ""
                    print(f"Tick {t:4d}: H={result['H']:.4f}, ΔH={result['delta']:+.4f} [{status}]{zphc_mark}")
        
        # Summary
        if verbose:
            final_H = self.telemetry['H'][-1] if self.telemetry['H'] else 0
            avg_H = np.mean(self.telemetry['H'][-50:]) if len(self.telemetry['H']) >= 50 else np.mean(self.telemetry['H'])
            lock_pct = 100 * self.telemetry['locked_ticks'] / num_ticks
            
            print(f"\n--- SUMMARY ---")
            print(f"Final H: {final_H:.4f}")
            print(f"Avg H (last 50): {avg_H:.4f}")
            print(f"Target H: {HARMONIC_TARGET}")
            print(f"Locked ticks: {self.telemetry['locked_ticks']}/{num_ticks} ({lock_pct:.1f}%)")
            print(f"ZPHC events: {len(self.telemetry['zphc_events'])}")
            print(f"Stable glyphs: {len(self.glyph_detector.stable_glyphs)}")
            
            # Show some glyphs with ODD digit sums (persist)
            odd_glyphs = [g for _, g in self.telemetry['glyphs'] if g['parity'] == 'ODD']
            if odd_glyphs:
                print(f"\nODD-sum glyphs (persist):")
                for g in odd_glyphs[:5]:
                    print(f"  Byte {g['byte_index']}: {g['pattern']} (sum={g['digit_sum']})")
        
        return self.telemetry
    
    def visualize(self):
        """Visualize H trajectory."""
        if not self.telemetry['H']:
            print("No data to visualize")
            return
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))
        
        # H over time
        ax1 = axes[0]
        ticks = range(len(self.telemetry['H']))
        ax1.plot(ticks, self.telemetry['H'], 'b-', linewidth=0.8, label='H(t)')
        ax1.axhline(y=HARMONIC_TARGET, color='g', linestyle='--', label=f'Target ({HARMONIC_TARGET})')
        ax1.axhline(y=HARMONIC_TARGET + CONVERGENCE_BAND, color='r', linestyle=':', alpha=0.5)
        ax1.axhline(y=HARMONIC_TARGET - CONVERGENCE_BAND, color='r', linestyle=':', alpha=0.5)
        
        # Mark ZPHC events
        for zphc_tick in self.telemetry['zphc_events']:
            ax1.axvline(x=zphc_tick, color='orange', linestyle='-', alpha=0.7, label='ZPHC' if zphc_tick == self.telemetry['zphc_events'][0] else '')
        
        ax1.set_xlabel('Tick')
        ax1.set_ylabel('H (Harmonic Ratio)')
        ax1.set_title(f'Nexus Nucleus v1 - Harmonic Convergence (Mode: {self.tile_bank.mode})')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1)
        
        # Delta over time
        ax2 = axes[1]
        ax2.plot(ticks, self.telemetry['delta'], 'r-', linewidth=0.8, label='ΔH')
        ax2.axhline(y=0, color='g', linestyle='--')
        ax2.axhline(y=CONVERGENCE_BAND, color='gray', linestyle=':', alpha=0.5)
        ax2.axhline(y=-CONVERGENCE_BAND, color='gray', linestyle=':', alpha=0.5)
        ax2.fill_between(ticks, -CONVERGENCE_BAND, CONVERGENCE_BAND, alpha=0.2, color='green', label='Lock band')
        
        ax2.set_xlabel('Tick')
        ax2.set_ylabel('ΔH (Error)')
        ax2.set_title('Error from Target')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('/home/claude/nexus_convergence.png', dpi=150)
        plt.close()
        print("\nSaved: /home/claude/nexus_convergence.png")
    
    def visualize_lanes(self):
        """ASCII visualization of current lane state."""
        print("\nLANE STATE (hex tiles):")
        print("-" * 50)
        
        high_count = sum(1 for lane in self.lanes if lane.tile >= 8)
        low_count = NUM_LANES - high_count
        
        for row in range(8):
            start = row * 8
            tiles = [f'{self.lanes[i].tile:X}' for i in range(start, start + 8)]
            
            # Mark high (H) vs low (L) tiles
            marks = ['H' if self.lanes[i].tile >= 8 else 'L' for i in range(start, start + 8)]
            
            print(f"Byte {row}: [{' '.join(tiles)}]  {''.join(marks)}")
        
        print("-" * 50)
        print(f"High tiles: {high_count} ({100*high_count/NUM_LANES:.1f}%)")
        print(f"Low tiles:  {low_count} ({100*low_count/NUM_LANES:.1f}%)")
        print(f"Ratio (H):  {high_count/NUM_LANES:.4f} (target: {HARMONIC_TARGET})")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("NEXUS NUCLEUS v1 - Fixed Harmonic Convergence")
    print("Learning via TILE ROUTING with ZPHC Reset")
    print("=" * 60)
    
    # Run with full hex palette
    print("\n### RUN: FULL HEX (0-F) ###\n")
    nucleus = NexusNucleus(tile_mode='H', rhythm_mode='linear')
    telemetry = nucleus.run(300, verbose=True)
    nucleus.visualize_lanes()
    nucleus.visualize()
    
    print("\n" + "=" * 60)
    
    # Run with A-F only
    print("\n### RUN: COARSE (A-F ONLY) ###\n")
    nucleus_a = NexusNucleus(tile_mode='A', rhythm_mode='linear')
    telemetry_a = nucleus_a.run(300, verbose=True)
    nucleus_a.visualize_lanes()
    
    print("\n" + "=" * 60)
    print("NEXUS NUCLEUS v1 COMPLETE")
    print("=" * 60)
