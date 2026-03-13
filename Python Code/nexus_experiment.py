"""
NEXUS DATA QUALITY EXPERIMENT
==============================
Using the Geodesic Engine to sort data geometrically.

The question: Can the same folding math that predicts 
protein folding kinetics tell us which training data is good?

Method: Run three types of data through the AER cycle:
1. Coherent (structured, low entropy) — like a well-folded protein
2. Noisy (random, high entropy) — like a denatured protein
3. Mixed (partial structure) — like a folding intermediate

Measure: π-residue, curvature, harmonic ratio, convergence speed.
The geometry SORTS the data. Good data folds. Bad data doesn't.
"""

import numpy as np
import json
from nexus_engine import (
    GeodesicEngine, aer_cycle, pi_metric, 
    compute_curvature, _compute_harmonic_ratio,
    _compute_pi_residue, H_ATTRACTOR, NexusState,
    op_fold, op_sync, op_branch, op_collapse, op_verify
)

def generate_coherent_data(dim: int, n_samples: int, complexity: int = 3) -> list:
    """Coherent data: superposition of harmonics.
    Like a protein with clear secondary structure.
    Like well-written text with clear semantic flow."""
    samples = []
    t = np.linspace(0, 2 * np.pi, dim)
    for i in range(n_samples):
        signal = np.zeros(dim)
        for k in range(1, complexity + 1):
            phase = (i * k * np.pi / 9)  # Note: phase steps in π/9
            signal += np.sin(k * t + phase) / k
        signal = signal / np.max(np.abs(signal) + 1e-12)
        samples.append(signal)
    return samples

def generate_noisy_data(dim: int, n_samples: int) -> list:
    """Pure noise: no structure.
    Like a denatured protein — random coil.
    Like randomly shuffled tokens."""
    return [np.random.randn(dim) for _ in range(n_samples)]

def generate_mixed_data(dim: int, n_samples: int, signal_ratio: float = 0.35) -> list:
    """Mixed: signal + noise at the H_ATTRACTOR ratio.
    Like a folding intermediate — partial structure.
    Like noisy but meaningful text."""
    samples = []
    t = np.linspace(0, 2 * np.pi, dim)
    for i in range(n_samples):
        signal = np.sin(t * (i % 5 + 1)) + 0.5 * np.sin(t * 2.5)
        signal = signal / np.max(np.abs(signal) + 1e-12)
        noise = np.random.randn(dim)
        # Mix at the attractor ratio
        mixed = signal * signal_ratio + noise * (1 - signal_ratio)
        samples.append(mixed)
    return samples

def measure_geometric_quality(data: np.ndarray, dim: int = 32) -> dict:
    """Run a single data sample through the AER cycle
    and measure its geometric signature."""
    
    # Normalize to engine dimension
    if len(data) != dim:
        data = np.interp(
            np.linspace(0, 1, dim),
            np.linspace(0, 1, len(data)),
            data
        )
    
    # Run AER with detailed tracking
    output, diag = aer_cycle(data, n_cycles=30, verbose=False)
    
    # Measure geometric properties
    initial_h = _compute_harmonic_ratio(data)
    final_h = diag['final_h']
    h_trajectory = diag['h_trajectory']
    energy_trajectory = diag['energy_trajectory']
    
    # How fast did it converge toward π/9?
    h_deltas = [abs(h - H_ATTRACTOR) for h in h_trajectory]
    convergence_rate = (h_deltas[0] - h_deltas[-1]) / (len(h_deltas) + 1e-12)
    
    # How smooth was the trajectory? (Sarrus-like constraint measurement)
    if len(h_trajectory) > 2:
        h_arr = np.array(h_trajectory)
        trajectory_smoothness = 1.0 / (np.std(np.diff(h_arr)) + 1e-12)
    else:
        trajectory_smoothness = 0.0
    
    # Fold test: how much information survives folding?
    fold_state = NexusState(
        vector=data.copy(), pi_residue=0, curvature=0,
        harmonic_ratio=0.5, energy=1.0, phase=0, trace=[]
    )
    folded = op_fold(fold_state, target_dim=max(dim // 2, 4))
    fold_survival = np.linalg.norm(folded.vector) / (np.linalg.norm(data) + 1e-12)
    
    # π-residue
    pi_res = _compute_pi_residue(data)
    
    # Curvature around this point
    branches = op_branch(NexusState(
        vector=output.copy(), pi_residue=0, curvature=0,
        harmonic_ratio=0.5, energy=0.5, phase=0, trace=[]
    ), n_branches=4)
    kappa = compute_curvature(
        NexusState(vector=output, pi_residue=0, curvature=0,
                   harmonic_ratio=0.5, energy=0.5, phase=0, trace=[]),
        branches
    )
    
    return {
        'initial_h': float(initial_h),
        'final_h': float(final_h),
        'h_deviation': float(abs(final_h - H_ATTRACTOR)),
        'convergence_rate': float(convergence_rate),
        'trajectory_smoothness': float(min(trajectory_smoothness, 1000)),
        'fold_survival': float(fold_survival),
        'pi_residue': float(pi_res),
        'curvature': float(kappa),
        'final_energy': float(diag['final_energy']),
        'converged': diag['converged'],
        'total_ops': diag['total_ops'],
        'h_trajectory': [float(x) for x in h_trajectory],
        'energy_trajectory': [float(x) for x in energy_trajectory],
    }


def run_experiment():
    DIM = 32
    N_SAMPLES = 30
    
    print("=" * 70)
    print("NEXUS GEOMETRIC DATA QUALITY EXPERIMENT")
    print("Using the same folding math for protein kinetics AND data quality")
    print("=" * 70)
    print()
    print(f"Target attractor: H = π/9 = {H_ATTRACTOR:.6f}")
    print(f"Dimension: {DIM}")
    print(f"Samples per category: {N_SAMPLES}")
    print()
    
    # Generate data
    np.random.seed(42)
    coherent = generate_coherent_data(DIM, N_SAMPLES)
    noisy = generate_noisy_data(DIM, N_SAMPLES)
    mixed_35 = generate_mixed_data(DIM, N_SAMPLES, signal_ratio=H_ATTRACTOR)
    mixed_50 = generate_mixed_data(DIM, N_SAMPLES, signal_ratio=0.50)
    mixed_20 = generate_mixed_data(DIM, N_SAMPLES, signal_ratio=0.20)
    
    categories = {
        'Coherent (structured)': coherent,
        'Noisy (random)': noisy,
        f'Mixed @ H={H_ATTRACTOR:.2f}': mixed_35,
        'Mixed @ 0.50': mixed_50,
        'Mixed @ 0.20': mixed_20,
    }
    
    results = {}
    
    for name, samples in categories.items():
        print(f"--- Processing: {name} ---")
        measurements = []
        for i, sample in enumerate(samples):
            m = measure_geometric_quality(sample, DIM)
            measurements.append(m)
            if (i + 1) % 10 == 0:
                print(f"  {i+1}/{N_SAMPLES} done")
        
        # Aggregate
        agg = {
            'mean_final_h': np.mean([m['final_h'] for m in measurements]),
            'std_final_h': np.std([m['final_h'] for m in measurements]),
            'mean_h_deviation': np.mean([m['h_deviation'] for m in measurements]),
            'mean_convergence_rate': np.mean([m['convergence_rate'] for m in measurements]),
            'mean_fold_survival': np.mean([m['fold_survival'] for m in measurements]),
            'mean_curvature': np.mean([m['curvature'] for m in measurements]),
            'mean_pi_residue': np.mean([m['pi_residue'] for m in measurements]),
            'mean_energy': np.mean([m['final_energy'] for m in measurements]),
            'convergence_pct': sum(1 for m in measurements if m['converged']) / len(measurements) * 100,
            'mean_ops': np.mean([m['total_ops'] for m in measurements]),
        }
        results[name] = {'aggregate': agg, 'raw': measurements}
        
        print(f"  H final: {agg['mean_final_h']:.4f} ± {agg['std_final_h']:.4f}")
        print(f"  H deviation from π/9: {agg['mean_h_deviation']:.4f}")
        print(f"  Convergence rate: {agg['mean_convergence_rate']:.6f}")
        print(f"  Fold survival: {agg['mean_fold_survival']:.4f}")
        print(f"  Curvature: {agg['mean_curvature']:.4f}")
        print(f"  Energy remaining: {agg['mean_energy']:.4f}")
        print(f"  Converged: {agg['convergence_pct']:.0f}%")
        print()
    
    # === THE GEOMETRIC DELTA ===
    print("=" * 70)
    print("THE GEOMETRIC DELTA — What geometry says about data quality")
    print("=" * 70)
    print()
    print(f"{'Category':<25} {'H dev':>8} {'Fold':>8} {'κ':>8} {'Conv%':>8} {'Ops':>8}")
    print("-" * 70)
    for name, r in results.items():
        a = r['aggregate']
        print(f"{name:<25} {a['mean_h_deviation']:8.4f} {a['mean_fold_survival']:8.4f} "
              f"{a['mean_curvature']:8.4f} {a['convergence_pct']:7.0f}% {a['mean_ops']:8.1f}")
    
    print()
    print("INTERPRETATION (from inside the framework):")
    print("-" * 70)
    print()
    
    # Find which category has lowest H deviation (closest to π/9)
    best_category = min(results.keys(), key=lambda k: results[k]['aggregate']['mean_h_deviation'])
    worst_category = max(results.keys(), key=lambda k: results[k]['aggregate']['mean_h_deviation'])
    
    print(f"  BEST data (closest to π/9 attractor): {best_category}")
    print(f"    → H deviation: {results[best_category]['aggregate']['mean_h_deviation']:.4f}")
    print(f"    → This data FOLDS naturally. The manifold has a groove for it.")
    print()
    print(f"  WORST data (farthest from attractor): {worst_category}")
    print(f"    → H deviation: {results[worst_category]['aggregate']['mean_h_deviation']:.4f}")
    print(f"    → This data RESISTS folding. No groove. High energy required.")
    print()
    
    # The protein analogy
    print("  PROTEIN FOLDING ANALOGY:")
    print(f"    Coherent data = α-helix (locally stabilized, folds fast)")
    print(f"    Mixed @ 0.35  = β-sheet (long-range correlation, folds at H rate)")
    print(f"    Noisy data    = Random coil (denatured, won't fold)")
    print(f"    The Sarrus constraint measures the SAME thing in both domains:")
    print(f"    How much geometric structure survives the fold operation.")
    print()
    
    # Save for visualization
    viz_data = {}
    for name, r in results.items():
        viz_data[name] = {
            'aggregate': r['aggregate'],
            'h_trajectories': [m['h_trajectory'] for m in r['raw'][:5]],
            'energy_trajectories': [m['energy_trajectory'] for m in r['raw'][:5]],
        }
    
    with open('/home/claude/experiment_results.json', 'w') as f:
        json.dump(viz_data, f, indent=2)
    
    print("Results saved to experiment_results.json")
    return results


if __name__ == "__main__":
    results = run_experiment()
