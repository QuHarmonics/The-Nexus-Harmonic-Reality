"""
NEXUS GEODESIC ENGINE v0.1
==========================
The 10-Operator ISA as Executable Geometric Training

This is not a simulation of the Nexus Framework.
This IS the framework running.

Operators are verbs. Constants are folded operations.
Training is navigation. The manifold is pre-computed.
We're building the reader, not the book.

Dean Kulik / QuHarmonics Research Group
ORCID: 0009-0003-3128-8828
CC BY-NC 4.0
"""

import numpy as np
import hashlib
import struct
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
import json

# ============================================================
# CONSTANTS — These are not parameters. They are operations
# folded into number form for transit.
# ============================================================

H_ATTRACTOR = np.pi / 9  # 0.349066... The stable release version
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio — the clock/pacer

# SHA-256 first 8 round constants (cube roots of first 8 primes)
# These are hardware configuration values, not "nothing-up-my-sleeve"
SHA_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
]

# ============================================================
# THE STATE VECTOR — Typeless. Identity emerges from interaction.
# ============================================================

@dataclass
class NexusState:
    """A point on the information manifold.
    
    Not a tensor. Not an embedding. A POSITION in pre-computed space.
    The state knows where it is relative to the lattice.
    """
    vector: np.ndarray          # The raw state (position on manifold)
    pi_residue: float = 0.0     # Distance from lattice alignment
    curvature: float = 0.0      # Local Ollivier-Ricci curvature
    harmonic_ratio: float = 0.5 # Current H — should converge to π/9
    energy: float = 1.0         # Tension remaining to resolve
    phase: int = 0              # Which AER phase we're in
    trace: List[float] = field(default_factory=list)  # Execution scar
    
    @property
    def is_collapsed(self) -> bool:
        """ZPHC threshold — has the state found its ground?"""
        return self.energy < 0.01 and abs(self.harmonic_ratio - H_ATTRACTOR) < 0.05
    
    @property
    def entropy(self) -> float:
        """Normalized Shannon entropy of the state vector."""
        v = np.abs(self.vector)
        v = v / (v.sum() + 1e-12)
        v = v[v > 0]
        return -np.sum(v * np.log2(v)) / np.log2(len(self.vector) + 1)


# ============================================================
# THE 10-OPERATOR ISA
# These are not functions that act ON data.
# They are what data DOES when it's in these configurations.
# ============================================================

class Op(Enum):
    """The Nexus Instruction Set Architecture.
    
    Every computation in the universe — SHA-256 rounds, protein folding,
    neural network forward passes, galaxy formation — uses only these.
    Human CS scoped them into specialized versions.
    These are the unscoped originals.
    """
    PIN       = "PIN"        # Lock constraint — freeze a degree of freedom
    REFLECT   = "REFLECT"    # Symmetry operation — ξ(s) = ξ(1-s)
    FOLD      = "FOLD"       # Compress/project — higher dim → lower dim
    GATE      = "GATE"       # Conditional passage — XOR/interference
    BRANCH    = "BRANCH"     # Path divergence — superposition of futures
    LEAK      = "LEAK"       # Constraint bleed — viscosity, diffusion
    COLLAPSE  = "COLLAPSE"   # State reduction — measurement, decision
    SYNC      = "SYNC"       # Resonance alignment — phase lock
    VERIFY    = "VERIFY"     # Consistency check — no ghost traces
    RELEASE   = "RELEASE"    # Output/propagation — the answer leaves


def op_pin(state: NexusState, axis: int = 0, value: float = None) -> NexusState:
    """PIN: Lock a constraint. Freeze a degree of freedom.
    
    In proteins: disulfide bond forms, locking two residues.
    In SHA-256: a round constant fixes the mixing angle.
    In training: a learned feature becomes permanent.
    """
    new_vec = state.vector.copy()
    if value is None:
        value = new_vec[axis % len(new_vec)]
    new_vec[axis % len(new_vec)] = value
    # Pinning reduces energy — one less thing to resolve
    new_energy = state.energy * (1 - H_ATTRACTOR / len(new_vec))
    state.trace.append(('PIN', axis, value))
    return NexusState(
        vector=new_vec,
        pi_residue=state.pi_residue,
        curvature=state.curvature,
        harmonic_ratio=state.harmonic_ratio,
        energy=new_energy,
        phase=state.phase,
        trace=state.trace
    )


def op_reflect(state: NexusState, axis: int = 0) -> NexusState:
    """REFLECT: Symmetry operation. The mirror.
    
    In Riemann: ξ(s) = ξ(1-s) — the functional equation.
    In proteins: mirror image chirality check.
    In training: self-attention IS reflection — the model sees itself.
    """
    new_vec = state.vector.copy()
    # Reflect around the mean of the specified axis neighborhood
    mid = len(new_vec) // 2
    new_vec = np.concatenate([new_vec[mid:], new_vec[:mid]])
    # Reflection preserves energy but changes phase
    state.trace.append(('REFLECT', axis))
    return NexusState(
        vector=new_vec,
        pi_residue=state.pi_residue,
        curvature=-state.curvature,  # Curvature flips under reflection
        harmonic_ratio=state.harmonic_ratio,
        energy=state.energy,
        phase=state.phase,
        trace=state.trace
    )


def op_fold(state: NexusState, target_dim: int = None) -> NexusState:
    """FOLD: Compress higher dimension into lower dimension.
    
    This IS hashing. This IS protein folding. This IS attention.
    Information preserved, projected into different basis.
    The playing card rotated edge-on looks like a line.
    
    NOT destruction. Redistribution.
    """
    vec = state.vector
    if target_dim is None:
        target_dim = max(len(vec) // 2, 4)
    
    # Fold by pairing and combining — like SHA-256 message schedule
    new_vec = np.zeros(target_dim)
    for i in range(len(vec)):
        # Each input element contributes to a folded position
        # using golden ratio stepping to avoid aliasing (Nyquist)
        target_idx = int(i * PHI) % target_dim
        # XOR-like combination: add with phase alternation
        if i % 2 == 0:
            new_vec[target_idx] += vec[i]
        else:
            new_vec[target_idx] -= vec[i]
    
    # Normalize to preserve total information magnitude
    norm = np.linalg.norm(new_vec)
    if norm > 0:
        new_vec = new_vec * (np.linalg.norm(vec) / norm)
    
    # Folding increases pi_residue (we moved away from original coords)
    # but decreases entropy (more compressed)
    new_residue = state.pi_residue + abs(len(vec) - target_dim) / len(vec)
    
    state.trace.append(('FOLD', len(vec), target_dim))
    return NexusState(
        vector=new_vec,
        pi_residue=new_residue,
        curvature=state.curvature,
        harmonic_ratio=state.harmonic_ratio,
        energy=state.energy * 0.9,  # Folding dissipates some energy
        phase=state.phase,
        trace=state.trace
    )


def op_gate(state: NexusState, condition: np.ndarray = None) -> NexusState:
    """GATE: Conditional passage. XOR interference.
    
    In SHA-256: the Ch and Maj functions.
    In proteins: allosteric gating.
    In training: ReLU, attention masking — what passes, what doesn't.
    
    The gate creates contrast. Boundaries. Structure from interference.
    """
    vec = state.vector.copy()
    if condition is None:
        # Self-gating: use the state's own structure as the condition
        # Split vector, XOR-combine the halves
        mid = len(vec) // 2
        condition = np.sign(vec[:mid]) if mid > 0 else np.ones_like(vec)
    
    # Apply gate: elements where condition is positive pass, others are damped
    for i in range(len(vec)):
        cond_val = condition[i % len(condition)]
        if cond_val <= 0:
            vec[i] *= H_ATTRACTOR  # Damped, not destroyed
    
    state.trace.append(('GATE', float(np.mean(condition > 0))))
    return NexusState(
        vector=vec,
        pi_residue=state.pi_residue,
        curvature=state.curvature,
        harmonic_ratio=state.harmonic_ratio,
        energy=state.energy * 0.95,
        phase=state.phase,
        trace=state.trace
    )


def op_branch(state: NexusState, n_branches: int = 2) -> List[NexusState]:
    """BRANCH: Path divergence. Superposition of futures.
    
    In quantum: superposition. All paths computed.
    In SHA-256: speculative execution of multiple rounds.
    In proteins: folding intermediates exploring conformations.
    In training: beam search, dropout, ensemble — all are BRANCH.
    
    Returns multiple states. The universe runs ALL of them.
    We pick one later (COLLAPSE). That's the cost.
    """
    branches = []
    for b in range(n_branches):
        new_vec = state.vector.copy()
        # Each branch gets a perturbation seeded by golden ratio
        # This ensures maximum coverage, minimum overlap (Nyquist)
        phase_shift = 2 * np.pi * b / (n_branches * PHI)
        perturbation = np.sin(
            np.arange(len(new_vec)) * phase_shift + b * np.pi / 9
        ) * state.energy * 0.1
        new_vec += perturbation
        
        new_state = NexusState(
            vector=new_vec,
            pi_residue=state.pi_residue,
            curvature=state.curvature,
            harmonic_ratio=state.harmonic_ratio,
            energy=state.energy,
            phase=state.phase,
            trace=state.trace.copy() + [('BRANCH', b, n_branches)]
        )
        branches.append(new_state)
    return branches


def op_leak(state: NexusState, rate: float = None) -> NexusState:
    """LEAK: Constraint bleed. Viscosity. Diffusion.
    
    In Navier-Stokes: viscosity dissipating momentum.
    In proteins: thermal fluctuations loosening constraints.
    In SHA-256: bit diffusion across words.
    In training: weight decay, regularization — controlled forgetting.
    
    Not a bug. The system needs controlled leakage to avoid
    rigidity. Too tight = brittle. Too loose = chaos.
    The rate should converge to H_ATTRACTOR.
    """
    if rate is None:
        rate = H_ATTRACTOR
    
    vec = state.vector.copy()
    # Leak: each element bleeds into neighbors (diffusion)
    leaked = np.zeros_like(vec)
    for i in range(len(vec)):
        leaked[i] = vec[i] * (1 - rate)
        # Bleed into neighbors
        leaked[(i + 1) % len(vec)] += vec[i] * rate * 0.5
        leaked[(i - 1) % len(vec)] += vec[i] * rate * 0.5
    
    state.trace.append(('LEAK', rate))
    return NexusState(
        vector=leaked,
        pi_residue=state.pi_residue * (1 + rate * 0.1),
        curvature=state.curvature * (1 - rate),  # Curvature smooths
        harmonic_ratio=state.harmonic_ratio,
        energy=state.energy * (1 - rate * 0.5),
        phase=state.phase,
        trace=state.trace
    )


def op_collapse(branches: List[NexusState]) -> NexusState:
    """COLLAPSE: State reduction. Measurement. Decision.
    
    This is the Ψ-Collapse Operator. This is measurement.
    This is what makes P ≠ NP from the scoped view:
    - VERIFY (read the answer) = P
    - TRAVERSE (find the answer) = NP  
    - COLLAPSE destroys the path information
    - The gap between generation and verification IS the collapse cost
    
    Selects the branch with lowest energy AND closest to H_ATTRACTOR.
    """
    if not branches:
        raise ValueError("Nothing to collapse")
    if len(branches) == 1:
        return branches[0]
    
    # Score each branch: minimize energy while staying near attractor
    scores = []
    for b in branches:
        h_deviation = abs(b.harmonic_ratio - H_ATTRACTOR)
        score = b.energy + h_deviation * 10  # H-alignment is 10x more important
        scores.append(score)
    
    best_idx = int(np.argmin(scores))
    winner = branches[best_idx]
    
    # Collapse destroys path information — this is irreversible
    # (Unless you kept the trace — that's the Glass Key)
    winner.trace.append(('COLLAPSE', best_idx, len(branches)))
    winner.energy *= 0.8  # Collapse releases energy
    return winner


def op_sync(state: NexusState, reference: np.ndarray = None) -> NexusState:
    """SYNC: Resonance alignment. Phase lock.
    
    In BSD conjecture: local-global lattice resonance.
    In proteins: cooperative folding (many residues snap at once).
    In SHA-256: the chaining variables synchronizing.
    In training: batch normalization, layer norm — SYNC operations.
    
    Aligns the state with a reference (the lattice).
    """
    vec = state.vector.copy()
    
    if reference is None:
        # Self-sync: align with the state's own harmonic structure
        # Use the DFT to find dominant frequencies, then reinforce
        fft = np.fft.rfft(vec)
        magnitudes = np.abs(fft)
        # Keep only components that are above the H_ATTRACTOR threshold
        threshold = np.max(magnitudes) * H_ATTRACTOR
        fft[magnitudes < threshold] *= H_ATTRACTOR  # Dampen, don't kill
        vec = np.fft.irfft(fft, n=len(vec))
    else:
        # Sync with external reference: blend toward it
        blend = H_ATTRACTOR  # Blend rate IS the attractor
        ref_scaled = reference[:len(vec)] if len(reference) >= len(vec) else \
                     np.pad(reference, (0, len(vec) - len(reference)))
        ref_norm = ref_scaled / (np.linalg.norm(ref_scaled) + 1e-12) * np.linalg.norm(vec)
        vec = vec * (1 - blend) + ref_norm * blend
    
    # Sync moves harmonic_ratio toward H_ATTRACTOR
    new_h = state.harmonic_ratio + (H_ATTRACTOR - state.harmonic_ratio) * 0.3
    
    state.trace.append(('SYNC', float(new_h)))
    return NexusState(
        vector=vec,
        pi_residue=state.pi_residue * 0.9,  # Better aligned
        curvature=state.curvature,
        harmonic_ratio=new_h,
        energy=state.energy * 0.95,
        phase=state.phase,
        trace=state.trace
    )


def op_verify(state: NexusState) -> Tuple[NexusState, bool]:
    """VERIFY: Consistency check. No ghost traces.
    
    In Hodge conjecture: every cohomology class has a geometric representative.
    In proteins: the structure passes the Ramachandran check.
    In SHA-256: the hash verifies the message.
    In training: validation loss — does the model generalize?
    
    Returns the state and whether it passed verification.
    """
    vec = state.vector
    
    # Check 1: Is the harmonic ratio near the attractor?
    h_ok = abs(state.harmonic_ratio - H_ATTRACTOR) < 0.1
    
    # Check 2: Is the entropy reasonable (not collapsed to nothing, not pure noise)?
    ent = state.entropy
    ent_ok = 0.1 < ent < 0.9
    
    # Check 3: Is the curvature positive (convergent, not divergent)?
    curv_ok = state.curvature >= 0
    
    # Check 4: Self-consistency — fold and unfold, measure residual
    folded = op_fold(NexusState(
        vector=vec.copy(), pi_residue=0, curvature=0,
        harmonic_ratio=0.5, energy=1.0, phase=0, trace=[]
    ), target_dim=max(len(vec) // 2, 2))
    
    # The fold residual tells us how much information survived
    fold_ok = np.linalg.norm(folded.vector) > 0.1 * np.linalg.norm(vec)
    
    passed = h_ok and ent_ok and fold_ok
    
    state.trace.append(('VERIFY', passed, {
        'h_ok': h_ok, 'ent_ok': ent_ok, 
        'curv_ok': curv_ok, 'fold_ok': fold_ok
    }))
    return state, passed


def op_release(state: NexusState) -> Tuple[np.ndarray, List]:
    """RELEASE: Output. Propagation. The answer leaves the system.
    
    In AER: the final phase. Constraint resolution emits output.
    In proteins: the folded structure is released from the ribosome.
    In SHA-256: the hash digest is emitted.
    In training: inference — the model produces an answer.
    
    Returns the output vector and the execution trace (the scar).
    """
    state.trace.append(('RELEASE', float(state.energy), float(state.harmonic_ratio)))
    return state.vector.copy(), state.trace


# ============================================================
# THE π-METRIC — Distance that knows about the lattice
# ============================================================

def pi_metric(u: np.ndarray, v: np.ndarray, alpha: float = 0.5, beta: float = 0.5) -> float:
    """The π-Metric: ds² = α·H(u,v)² + β·Φ(Δπ(v))
    
    Distance that favors harmonic alignment.
    Meaningful directions are SHORT. Meaningless directions are LONG.
    This is how geometry becomes training signal.
    """
    # Raw Hamming-like distance (how different are the states?)
    hamming = np.sum(np.abs(u - v)) / (len(u) + 1e-12)
    
    # π-Residue of target state: how well does v align with the lattice?
    # Compute by hashing v and checking alignment with π digits
    v_hash = _hash_to_float(v)
    pi_residue = abs(v_hash - H_ATTRACTOR)  # Distance from the attractor
    
    # The metric: raw distance + alignment penalty
    ds2 = alpha * hamming**2 + beta * pi_residue**2
    return float(ds2)


def compute_curvature(state: NexusState, neighbors: List[NexusState]) -> float:
    """Discrete Ollivier-Ricci curvature approximation.
    
    κ > 0: Paths converging → semantic gravity well → GOOD
    κ < 0: Paths diverging → chaos → BAD
    κ = 0: Flat → no signal
    
    This is how the engine "feels" where meaning is.
    """
    if not neighbors or len(neighbors) < 2:
        return 0.0
    
    # Compute pairwise distances from state to each neighbor
    d_to_neighbors = [
        pi_metric(state.vector, n.vector) 
        for n in neighbors
    ]
    
    # Compute pairwise distances between neighbors
    d_between = []
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            d_between.append(pi_metric(neighbors[i].vector, neighbors[j].vector))
    
    if not d_between:
        return 0.0
    
    # Curvature ≈ 1 - (mean neighbor-neighbor distance / mean state-neighbor distance)
    mean_to = np.mean(d_to_neighbors)
    mean_between = np.mean(d_between)
    
    if mean_to < 1e-12:
        return 1.0  # Perfect convergence
    
    kappa = 1 - mean_between / (mean_to + 1e-12)
    return float(np.clip(kappa, -1, 1))


# ============================================================
# THE AER CYCLE — The universal training loop
# ============================================================

def aer_cycle(
    data: np.ndarray,
    n_cycles: int = 10,
    verbose: bool = False
) -> Tuple[np.ndarray, Dict[str, Any]]:
    """ASSEMBLE → EXECUTE → RELEASE
    
    This IS the training loop. Not gradient descent.
    Not backprop. Geometric navigation.
    
    ASSEMBLE: Ingest data, map to manifold coordinates
    EXECUTE:  Navigate using operators (curvature-guided)
    RELEASE:  Emit output when ZPHC threshold reached
    
    The loop self-regulates toward H ≈ π/9.
    """
    diagnostics = {
        'cycles': [],
        'h_trajectory': [],
        'energy_trajectory': [],
        'curvature_trajectory': [],
        'operators_used': [],
    }
    
    # === ASSEMBLE PHASE ===
    # Map input data to initial state on the manifold
    state = NexusState(
        vector=data.astype(float).copy(),
        pi_residue=_compute_pi_residue(data),
        curvature=0.0,
        harmonic_ratio=_compute_harmonic_ratio(data),
        energy=1.0,
        phase=0,
        trace=[]
    )
    
    if verbose:
        print(f"[ASSEMBLE] dim={len(data)}, H={state.harmonic_ratio:.4f}, "
              f"π-res={state.pi_residue:.4f}, energy={state.energy:.4f}")
    
    for cycle in range(n_cycles):
        # === EXECUTE PHASE ===
        # Select operators based on current state geometry
        
        # 1. Measure local geometry
        branches = op_branch(state, n_branches=3)
        state.curvature = compute_curvature(state, branches)
        
        ops_this_cycle = []
        
        # 2. Decision tree based on state condition
        if state.harmonic_ratio > H_ATTRACTOR + 0.1:
            # Too chaotic → SYNC to pull toward attractor
            state = op_sync(state)
            ops_this_cycle.append('SYNC')
        elif state.harmonic_ratio < H_ATTRACTOR - 0.1:
            # Too rigid → LEAK to add controlled noise
            state = op_leak(state, rate=H_ATTRACTOR * 0.5)
            ops_this_cycle.append('LEAK')
        
        if state.curvature < 0:
            # Diverging → FOLD to compress and find structure
            state = op_fold(state)
            ops_this_cycle.append('FOLD')
            # After fold, re-expand with GATE to restore dimension
            if len(state.vector) < len(data):
                # Pad back up and gate
                expanded = np.zeros(len(data))
                expanded[:len(state.vector)] = state.vector
                state.vector = expanded
                state = op_gate(state)
                ops_this_cycle.append('GATE')
        elif state.curvature > 0.5:
            # Strong convergence → PIN the good parts
            # Find the most stable elements and pin them
            stability = np.abs(np.diff(state.vector, prepend=state.vector[0]))
            most_stable = int(np.argmin(stability))
            state = op_pin(state, axis=most_stable)
            ops_this_cycle.append('PIN')
        
        if state.energy > 0.5:
            # Still high tension → BRANCH and COLLAPSE to explore
            branches = op_branch(state, n_branches=4)
            # Score branches by curvature
            for b in branches:
                b.curvature = compute_curvature(b, 
                    [bb for bb in branches if bb is not b])
                b.harmonic_ratio = _compute_harmonic_ratio(b.vector)
            state = op_collapse(branches)
            ops_this_cycle.append('BRANCH→COLLAPSE')
        
        # 3. Always VERIFY at end of execute
        state, passed = op_verify(state)
        ops_this_cycle.append(f'VERIFY:{"✓" if passed else "✗"}')
        
        # 4. Update harmonic ratio from actual state
        state.harmonic_ratio = _compute_harmonic_ratio(state.vector)
        
        # Record diagnostics
        diagnostics['cycles'].append(cycle)
        diagnostics['h_trajectory'].append(state.harmonic_ratio)
        diagnostics['energy_trajectory'].append(state.energy)
        diagnostics['curvature_trajectory'].append(state.curvature)
        diagnostics['operators_used'].append(ops_this_cycle)
        
        if verbose:
            print(f"  [EXECUTE {cycle}] ops={ops_this_cycle}, "
                  f"H={state.harmonic_ratio:.4f}, κ={state.curvature:.4f}, "
                  f"E={state.energy:.4f}")
        
        # === CHECK FOR ZERO-POINT HARMONIC COLLAPSE ===
        if state.is_collapsed:
            if verbose:
                print(f"  [ZPHC] Collapsed at cycle {cycle}! "
                      f"H={state.harmonic_ratio:.4f}")
            break
    
    # === RELEASE PHASE ===
    output, trace = op_release(state)
    diagnostics['final_h'] = state.harmonic_ratio
    diagnostics['final_energy'] = state.energy
    diagnostics['converged'] = state.is_collapsed
    diagnostics['total_ops'] = sum(len(ops) for ops in diagnostics['operators_used'])
    
    if verbose:
        print(f"[RELEASE] H={state.harmonic_ratio:.4f}, E={state.energy:.4f}, "
              f"converged={state.is_collapsed}, total_ops={diagnostics['total_ops']}")
    
    return output, diagnostics


# ============================================================
# THE BRAGG RESONATOR — Navigation filter
# ============================================================

def bragg_filter(candidates: List[NexusState], lattice_freq: np.ndarray) -> List[NexusState]:
    """Bragg Resonator: Only transitions that constructively
    interfere with the lattice propagate.
    
    k' - k = G  (reciprocal lattice vector)
    
    This is the massive pruning. Most possible next states
    are destructive interference (hallucinations, non-sequiturs).
    Only resonant ones pass.
    """
    passed = []
    for c in candidates:
        # Compute the "momentum transfer" of this transition
        c_freq = np.fft.rfft(c.vector)
        delta_k = np.abs(c_freq[:len(lattice_freq)]) - np.abs(lattice_freq)
        
        # Check if delta_k aligns with a lattice harmonic
        # (is the momentum transfer a multiple of the fundamental?)
        fundamental = H_ATTRACTOR  # The fundamental frequency IS H
        alignment = np.mean(np.cos(2 * np.pi * np.abs(delta_k) / (fundamental + 1e-12)))
        
        if alignment > 0:  # Constructive interference
            passed.append(c)
    
    return passed if passed else candidates[:1]  # Always keep at least one


# ============================================================
# SAMSON'S LAW — Homeostatic feedback controller
# ============================================================

def samsons_law(state: NexusState, target_h: float = H_ATTRACTOR) -> float:
    """Samson's Law: S = ΔE/T + k·dΔE/dt
    
    PID-like controller that keeps the system at H ≈ π/9.
    Returns a correction factor to apply to the next operation.
    """
    delta_e = state.harmonic_ratio - target_h
    
    # Derivative estimate from trace
    if len(state.trace) >= 2:
        recent_h = [t[1] for t in state.trace[-5:] if t[0] == 'SYNC']
        if len(recent_h) >= 2:
            d_delta = recent_h[-1] - recent_h[-2]
        else:
            d_delta = 0
    else:
        d_delta = 0
    
    T = 1.0  # Relaxation time
    k = 0.5  # Derivative gain
    
    correction = delta_e / T + k * d_delta
    return float(np.clip(correction, -1, 1))


# ============================================================
# UTILITY FUNCTIONS — The plumbing
# ============================================================

def _hash_to_float(data: np.ndarray) -> float:
    """Hash a vector to a float in [0, 1) for lattice addressing."""
    raw_bytes = data.tobytes()
    h = hashlib.sha256(raw_bytes).digest()
    # Take first 8 bytes as uint64, normalize to [0, 1)
    val = struct.unpack('>Q', h[:8])[0]
    return val / (2**64)


def _compute_pi_residue(data: np.ndarray) -> float:
    """How far is this data from the lattice?
    Hash it, compare to H_ATTRACTOR."""
    h = _hash_to_float(data)
    return abs(h - H_ATTRACTOR)


def _compute_harmonic_ratio(data: np.ndarray) -> float:
    """Compute the harmonic ratio of a state vector.
    
    This is the fraction of spectral energy in the
    'structured' (low-frequency) components vs total.
    Should converge to H ≈ π/9 in well-trained states.
    """
    if len(data) < 4:
        return 0.5
    fft = np.fft.rfft(data)
    magnitudes = np.abs(fft)
    total = np.sum(magnitudes) + 1e-12
    
    # The "structured" portion: frequencies below the H_ATTRACTOR threshold
    cutoff = max(1, int(len(magnitudes) * H_ATTRACTOR))
    structured = np.sum(magnitudes[:cutoff])
    
    return float(structured / total)


# ============================================================
# THE GEODESIC ENGINE — Full pipeline
# ============================================================

class GeodesicEngine:
    """The operational heart of the Nexus AI system.
    
    Replaces: gradient descent, backpropagation, loss functions
    With: curvature sensing, resonance filtering, geometric navigation
    
    This engine doesn't learn by adjusting weights.
    It learns by moving through the manifold —
    discovering where the grooves are.
    """
    
    def __init__(self, dim: int = 64):
        self.dim = dim
        self.grooves: List[np.ndarray] = []  # Learned trajectories
        self.attractors: List[np.ndarray] = []  # Discovered gravity wells
        self.lattice_freq = np.zeros(dim // 2 + 1)  # Lattice structure
        self.total_cycles = 0
        self.h_history: List[float] = []
    
    def ingest(self, data: np.ndarray) -> Dict[str, Any]:
        """Feed data to the engine. This IS training.
        
        Each piece of data is a trajectory through the manifold.
        Repeated similar data strengthens the groove.
        Novel data creates new grooves or extends existing ones.
        """
        # Normalize to engine dimension
        if len(data) != self.dim:
            data = np.interp(
                np.linspace(0, 1, self.dim),
                np.linspace(0, 1, len(data)),
                data
            )
        
        # Run the AER cycle
        output, diagnostics = aer_cycle(data, n_cycles=20, verbose=False)
        
        # If converged, this trajectory is a groove
        if diagnostics['converged']:
            self.grooves.append(output)
            # Check if this is near an existing attractor
            is_new_attractor = True
            for att in self.attractors:
                if pi_metric(output, att) < 0.1:
                    is_new_attractor = False
                    break
            if is_new_attractor:
                self.attractors.append(output)
        
        # Update lattice structure
        fft = np.fft.rfft(output)
        self.lattice_freq = self.lattice_freq * 0.95 + np.abs(fft) * 0.05
        
        self.total_cycles += 1
        self.h_history.append(diagnostics['final_h'])
        
        return diagnostics
    
    def navigate(self, query: np.ndarray) -> Tuple[np.ndarray, Dict]:
        """Given a query (input), navigate to the answer.
        
        This IS inference. Not matrix multiplication through weights.
        Following the curvature of the manifold from query to response.
        """
        if len(query) != self.dim:
            query = np.interp(
                np.linspace(0, 1, self.dim),
                np.linspace(0, 1, len(query)),
                query
            )
        
        # Start at the query position
        state = NexusState(
            vector=query.astype(float),
            pi_residue=_compute_pi_residue(query),
            curvature=0.0,
            harmonic_ratio=_compute_harmonic_ratio(query),
            energy=1.0,
            phase=0,
            trace=[]
        )
        
        # Find nearest attractor(s) — these are the gravitational targets
        if self.attractors:
            distances = [pi_metric(query, att) for att in self.attractors]
            nearest_idx = int(np.argmin(distances))
            target = self.attractors[nearest_idx]
            
            # Navigate toward the attractor using SYNC
            state = op_sync(state, reference=target)
        
        # Run AER to refine
        output, diagnostics = aer_cycle(state.vector, n_cycles=15, verbose=False)
        
        # Bragg filter the output
        candidate = NexusState(
            vector=output, pi_residue=0, curvature=0,
            harmonic_ratio=0.5, energy=0.5, phase=0, trace=[]
        )
        filtered = bragg_filter([candidate], self.lattice_freq)
        
        return filtered[0].vector, diagnostics
    
    def status(self) -> Dict[str, Any]:
        """Engine telemetry."""
        return {
            'total_cycles': self.total_cycles,
            'grooves': len(self.grooves),
            'attractors': len(self.attractors),
            'mean_h': float(np.mean(self.h_history[-100:])) if self.h_history else 0,
            'h_deviation_from_pi9': float(abs(
                np.mean(self.h_history[-100:]) - H_ATTRACTOR
            )) if self.h_history else 1.0,
            'lattice_strength': float(np.mean(self.lattice_freq)),
        }


# ============================================================
# DEMO: Run the engine on actual data
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("NEXUS GEODESIC ENGINE v0.1")
    print("Geometry IS Code. Training IS Navigation.")
    print("=" * 60)
    print()
    
    # Create engine
    engine = GeodesicEngine(dim=32)
    
    # Generate some structured data (simulating chat data)
    # In production this would be real tokenized text
    np.random.seed(42)
    
    print("--- TRAINING PHASE (Ingestion as Geometric Folding) ---")
    print()
    
    # Ingest data with varying structure levels
    for i in range(50):
        # Mix of structured (sine waves) and noise
        t = np.linspace(0, 2 * np.pi, 32)
        structured = np.sin(t * (i % 5 + 1)) * 0.7
        noise = np.random.randn(32) * 0.3
        data = structured + noise
        
        diag = engine.ingest(data)
        
        if (i + 1) % 10 == 0:
            status = engine.status()
            print(f"  Ingested {i+1}/50 | Grooves: {status['grooves']} | "
                  f"Attractors: {status['attractors']} | "
                  f"Mean H: {status['mean_h']:.4f} | "
                  f"H dev from π/9: {status['h_deviation_from_pi9']:.4f}")
    
    print()
    print("--- INFERENCE PHASE (Navigation) ---")
    print()
    
    # Query the engine
    query = np.sin(np.linspace(0, 2 * np.pi, 32) * 3) * 0.5
    result, nav_diag = engine.navigate(query)
    
    print(f"  Query → Result")
    print(f"  Input  H: {_compute_harmonic_ratio(query):.4f}")
    print(f"  Output H: {_compute_harmonic_ratio(result):.4f}")
    print(f"  π-Metric distance: {pi_metric(query, result):.4f}")
    print(f"  Converged: {nav_diag['converged']}")
    print(f"  Final H: {nav_diag['final_h']:.4f}")
    print(f"  Target H (π/9): {H_ATTRACTOR:.4f}")
    
    print()
    status = engine.status()
    print("--- ENGINE STATUS ---")
    for k, v in status.items():
        print(f"  {k}: {v}")
    
    print()
    print("=" * 60)
    print("The manifold has grooves. The engine navigates.")
    print("Geometry was always code. We just stopped reading it.")
    print("=" * 60)
