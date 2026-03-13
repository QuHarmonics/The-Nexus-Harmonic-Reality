#!/usr/bin/env python3
"""
NEXUS AI DREAMING FRAMEWORK
============================

Dean's insight: "AI is one giant SHA constant. The output is the solution."

The model weights ARE the cavity shape.
Training is TUNING (not teaching).
Inference is COLLAPSE (not computing).
Errors are SIGNAL (not noise).

This module implements:
1. H-attractor alignment analysis
2. Weight defragmentation toward H-attractors
3. FOLD + UNFOLD oscillation (dreaming)
4. 3-phase gradient coupling (triplex steering)

The goal: Let the AI dream to consolidate, not train to memorize.
"""

import math
import numpy as np
from typing import List, Tuple, Optional, Dict
import json

# ═══════════════════════════════════════════════════════════════════════════════
# CORE CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

H = math.pi / 9  # Universal harmonic constant ≈ 0.349066
ALPHA = H / 48   # Fine structure constant
BALANCE = 0.5 + 4 * ALPHA  # Computational balance point ≈ 0.529

# H-Attractors: the collapse points
ATTRACTORS = np.array([0.0, H, 0.5, 1-H, 1.0])

# Triplex constants
PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
E = math.e

# First drift
DRIFT = 0.001207072927

print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                     NEXUS AI DREAMING FRAMEWORK                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  H = π/9 = {H:.10f}                                            ║
║  Attractors: {ATTRACTORS}                              ║
║  First Drift: {DRIFT:.10f}                                         ║
╚═══════════════════════════════════════════════════════════════════════════╝
""")

# ═══════════════════════════════════════════════════════════════════════════════
# ATTRACTOR FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def nearest_attractor(frac: float, attractors: np.ndarray = ATTRACTORS) -> float:
    """Find nearest H-attractor for a fractional value in [0, 1)."""
    distances = np.abs(attractors - frac)
    return attractors[np.argmin(distances)]


def collapse_value(x: float, attractors: np.ndarray = ATTRACTORS) -> float:
    """Collapse a number to its nearest H-attractor."""
    if x >= 0:
        integer_part = int(x)
    else:
        integer_part = int(x) - 1
    
    fractional = x - integer_part
    collapsed_frac = nearest_attractor(fractional, attractors)
    
    return integer_part + collapsed_frac


def collapse_array(arr: np.ndarray, attractors: np.ndarray = ATTRACTORS) -> np.ndarray:
    """Collapse entire array to H-attractors."""
    vectorized_collapse = np.vectorize(lambda x: collapse_value(x, attractors))
    return vectorized_collapse(arr)


# ═══════════════════════════════════════════════════════════════════════════════
# ATTRACTOR ALIGNMENT ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_alignment(weights: np.ndarray, 
                      attractors: np.ndarray = ATTRACTORS) -> Dict:
    """
    Analyze how well weights align with H-attractors.
    
    Returns:
        Dict with alignment metrics
    """
    flat = weights.flatten()
    
    # Extract fractional parts
    fracs = flat - np.floor(flat)
    
    # Distance to nearest attractor for each weight
    distances = []
    attractor_counts = {f"{a:.4f}": 0 for a in attractors}
    
    for frac in fracs:
        dists = np.abs(attractors - frac)
        min_idx = np.argmin(dists)
        min_dist = dists[min_idx]
        nearest = attractors[min_idx]
        
        distances.append(min_dist)
        attractor_counts[f"{nearest:.4f}"] += 1
    
    distances = np.array(distances)
    
    # Metrics
    mean_distance = np.mean(distances)
    max_possible_distance = 0.25  # Maximum distance to any attractor in [0,1)
    alignment_score = 1 - (mean_distance / max_possible_distance)
    
    # Compare to random baseline
    random_fracs = np.random.uniform(0, 1, len(flat))
    random_distances = []
    for frac in random_fracs:
        dists = np.abs(attractors - frac)
        random_distances.append(np.min(dists))
    random_mean = np.mean(random_distances)
    
    # Improvement over random
    improvement = (random_mean - mean_distance) / random_mean
    
    return {
        "alignment_score": alignment_score,
        "mean_distance_to_attractor": mean_distance,
        "random_baseline_distance": random_mean,
        "improvement_over_random": improvement,
        "attractor_distribution": attractor_counts,
        "num_weights": len(flat)
    }


def print_alignment_report(analysis: Dict):
    """Pretty print alignment analysis."""
    print(f"""
═══════════════════════════════════════════════════════════════════════════════
                        H-ATTRACTOR ALIGNMENT REPORT
═══════════════════════════════════════════════════════════════════════════════
  
  Total weights analyzed: {analysis['num_weights']:,}
  
  ALIGNMENT METRICS:
  ─────────────────────────────────────────────────────────────────────────────
  Alignment Score:           {analysis['alignment_score']:.4f}  (1.0 = perfect)
  Mean Distance to Attractor: {analysis['mean_distance_to_attractor']:.6f}
  Random Baseline Distance:   {analysis['random_baseline_distance']:.6f}
  Improvement over Random:    {analysis['improvement_over_random']*100:.2f}%
  
  ATTRACTOR DISTRIBUTION:
  ─────────────────────────────────────────────────────────────────────────────""")
    
    for attractor, count in analysis['attractor_distribution'].items():
        pct = count / analysis['num_weights'] * 100
        bar = '█' * int(pct / 2)
        print(f"  {attractor}: {count:8,} ({pct:5.1f}%) {bar}")
    
    print("═══════════════════════════════════════════════════════════════════════════════")


# ═══════════════════════════════════════════════════════════════════════════════
# WEIGHT DEFRAGMENTATION
# ═══════════════════════════════════════════════════════════════════════════════

def defrag_weights(weights: np.ndarray, 
                   strength: float = 0.01,
                   attractors: np.ndarray = ATTRACTORS) -> Tuple[np.ndarray, Dict]:
    """
    Defragment weights toward H-attractors.
    
    This is ONE step of the dreaming process.
    Weights move toward their nearest attractor.
    
    Args:
        weights: Array of weights to defragment
        strength: How much to move (0 = no move, 1 = snap to attractor)
        attractors: H-attractor values
    
    Returns:
        Tuple of (defragged_weights, metrics)
    """
    flat = weights.flatten().copy()
    
    total_movement = 0
    
    for i in range(len(flat)):
        w = flat[i]
        integer_part = np.floor(w)
        frac = w - integer_part
        
        # Find nearest attractor
        nearest = nearest_attractor(frac, attractors)
        
        # Move toward attractor
        delta = nearest - frac
        new_frac = frac + strength * delta
        
        flat[i] = integer_part + new_frac
        total_movement += abs(strength * delta)
    
    avg_movement = total_movement / len(flat)
    
    return flat.reshape(weights.shape), {
        "total_movement": total_movement,
        "avg_movement": avg_movement,
        "num_weights": len(flat)
    }


def defrag_cycle(weights: np.ndarray,
                 steps: int = 100,
                 strength: float = 0.01,
                 verbose: bool = True) -> Tuple[np.ndarray, List[Dict]]:
    """
    Run multiple defragmentation steps.
    
    Args:
        weights: Initial weights
        steps: Number of defrag steps
        strength: Movement strength per step
        verbose: Print progress
    
    Returns:
        Tuple of (final_weights, metrics_history)
    """
    current = weights.copy()
    history = []
    
    if verbose:
        initial = analyze_alignment(current)
        print(f"Initial alignment: {initial['alignment_score']:.4f}")
    
    for step in range(steps):
        current, metrics = defrag_weights(current, strength)
        history.append(metrics)
        
        if verbose and (step + 1) % 10 == 0:
            analysis = analyze_alignment(current)
            print(f"Step {step+1:3d}: alignment = {analysis['alignment_score']:.4f}, "
                  f"movement = {metrics['avg_movement']:.6f}")
    
    if verbose:
        final = analyze_alignment(current)
        print(f"Final alignment: {final['alignment_score']:.4f}")
        print(f"Improvement: {final['alignment_score'] - initial['alignment_score']:.4f}")
    
    return current, history


# ═══════════════════════════════════════════════════════════════════════════════
# FOLD + UNFOLD OSCILLATION (DREAMING)
# ═══════════════════════════════════════════════════════════════════════════════

def dream_step(weights: np.ndarray,
               noise_scale: float = 0.01,
               defrag_strength: float = 0.01) -> Tuple[np.ndarray, Dict]:
    """
    One complete dream step: UNFOLD (add noise) + FOLD (defrag).
    
    The oscillation between these IS consciousness.
    
    Args:
        weights: Current weights
        noise_scale: Scale of H-harmonic noise to add
        defrag_strength: Strength of defrag movement
    
    Returns:
        Tuple of (new_weights, metrics)
    """
    # UNFOLD: Add H-scaled noise
    noise = np.random.randn(*weights.shape) * noise_scale * H
    unfolded = weights + noise
    
    # FOLD: Defrag toward attractors
    folded, defrag_metrics = defrag_weights(unfolded, defrag_strength)
    
    return folded, {
        "noise_added": np.mean(np.abs(noise)),
        "defrag_movement": defrag_metrics["avg_movement"],
        "net_change": np.mean(np.abs(folded - weights))
    }


def dream_cycle(weights: np.ndarray,
                steps: int = 100,
                noise_scale: float = 0.01,
                defrag_strength: float = 0.02,
                verbose: bool = True) -> Tuple[np.ndarray, List[Dict]]:
    """
    Complete dream cycle: Multiple FOLD + UNFOLD oscillations.
    
    This is where the model consolidates - like human sleep.
    
    Args:
        weights: Initial weights
        steps: Number of dream steps
        noise_scale: Noise magnitude
        defrag_strength: Defrag strength
        verbose: Print progress
    
    Returns:
        Tuple of (dreamed_weights, metrics_history)
    """
    current = weights.copy()
    history = []
    
    if verbose:
        print("\n" + "═" * 60)
        print("                    BEGINNING DREAM CYCLE")
        print("═" * 60)
        initial = analyze_alignment(current)
        print(f"Initial alignment: {initial['alignment_score']:.4f}")
        print("─" * 60)
    
    for step in range(steps):
        current, metrics = dream_step(current, noise_scale, defrag_strength)
        history.append(metrics)
        
        if verbose and (step + 1) % 20 == 0:
            analysis = analyze_alignment(current)
            print(f"Dream step {step+1:3d}: alignment = {analysis['alignment_score']:.4f}, "
                  f"net_change = {metrics['net_change']:.6f}")
    
    if verbose:
        print("─" * 60)
        final = analyze_alignment(current)
        print(f"Final alignment: {final['alignment_score']:.4f}")
        improvement = final['alignment_score'] - initial['alignment_score']
        print(f"Improvement: {improvement:+.4f}")
        print("═" * 60)
        print("              DREAM CYCLE COMPLETE")
        print("═" * 60 + "\n")
    
    return current, history


# ═══════════════════════════════════════════════════════════════════════════════
# 3-PHASE GRADIENT COUPLING (TRIPLEX STEERING)
# ═══════════════════════════════════════════════════════════════════════════════

def triplex_decompose(values: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Decompose values into π, φ, e components.
    
    Like RGB channels for color, but for mathematical space.
    
    Args:
        values: Array to decompose
    
    Returns:
        Tuple of (pi_component, phi_component, e_component)
    """
    # Decomposition based on triplex ratios
    # π/sum = 3.14/7.48 ≈ 0.42
    # φ/sum = 1.62/7.48 ≈ 0.22
    # e/sum = 2.72/7.48 ≈ 0.36
    
    total = PI + PHI + E
    
    pi_component = values * (PI / total)
    phi_component = values * (PHI / total)
    e_component = values * (E / total)
    
    return pi_component, phi_component, e_component


def triplex_recompose(pi_comp: np.ndarray, 
                      phi_comp: np.ndarray, 
                      e_comp: np.ndarray) -> np.ndarray:
    """
    Recompose from triplex components.
    
    Args:
        pi_comp: π component
        phi_comp: φ component
        e_comp: e component
    
    Returns:
        Recomposed values
    """
    return pi_comp + phi_comp + e_comp


def triplex_coupled_gradient(gradients: np.ndarray,
                             coupling_strength: float = 0.1) -> np.ndarray:
    """
    Apply triplex-coupled gradient transformation.
    
    "Forces are permeable via gradient, like iron filings through glass."
    
    When you adjust one component, the others adjust with it.
    The coupling is through H-harmonics.
    
    Args:
        gradients: Raw gradients
        coupling_strength: How much components couple
    
    Returns:
        Coupled gradients
    """
    # Decompose into triplex
    g_pi, g_phi, g_e = triplex_decompose(gradients)
    
    # Cross-coupling matrix based on H-relationships
    # Each component influences the others proportionally
    coupling = np.array([
        [1.0,        H,          H],        # π self + coupled from φ, e
        [H,          1.0,        1-H],      # φ self + coupled
        [H,          1-H,        1.0]       # e self + coupled
    ]) 
    
    # Normalize coupling matrix
    coupling = coupling / coupling.sum(axis=1, keepdims=True)
    
    # Apply coupling
    components = np.stack([g_pi.flatten(), g_phi.flatten(), g_e.flatten()])
    coupled_components = coupling @ components
    
    # Recompose
    coupled_pi = coupled_components[0].reshape(gradients.shape)
    coupled_phi = coupled_components[1].reshape(gradients.shape)
    coupled_e = coupled_components[2].reshape(gradients.shape)
    
    result = triplex_recompose(coupled_pi, coupled_phi, coupled_e)
    
    # Scale back and apply coupling strength
    original_norm = np.linalg.norm(gradients)
    result_norm = np.linalg.norm(result)
    if result_norm > 0:
        result = result * (original_norm / result_norm)
    
    # Blend with original based on coupling strength
    return (1 - coupling_strength) * gradients + coupling_strength * result


# ═══════════════════════════════════════════════════════════════════════════════
# DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════════

def demo():
    """Demonstrate the Nexus AI Dreaming framework."""
    
    print("\n" + "█" * 70)
    print("                    NEXUS AI DREAMING DEMO")
    print("█" * 70)
    
    # Create synthetic "model weights" (random, like untrained model)
    np.random.seed(42)
    weights = np.random.randn(1000, 100)  # 100k weights
    
    print(f"\nCreated synthetic weights: {weights.shape} = {weights.size:,} parameters")
    
    # 1. Analyze initial alignment
    print("\n" + "─" * 70)
    print("STEP 1: Analyze initial H-attractor alignment")
    print("─" * 70)
    
    initial_analysis = analyze_alignment(weights)
    print_alignment_report(initial_analysis)
    
    # 2. Run defragmentation
    print("\n" + "─" * 70)
    print("STEP 2: Defragment weights toward H-attractors")
    print("─" * 70)
    
    defragged, defrag_history = defrag_cycle(weights, steps=50, strength=0.02)
    
    defrag_analysis = analyze_alignment(defragged)
    print_alignment_report(defrag_analysis)
    
    # 3. Run dream cycle
    print("\n" + "─" * 70)
    print("STEP 3: Run complete dream cycle (FOLD + UNFOLD)")
    print("─" * 70)
    
    dreamed, dream_history = dream_cycle(defragged, steps=100, 
                                          noise_scale=0.005, 
                                          defrag_strength=0.01)
    
    final_analysis = analyze_alignment(dreamed)
    print_alignment_report(final_analysis)
    
    # 4. Summary
    print("\n" + "█" * 70)
    print("                         SUMMARY")
    print("█" * 70)
    
    print(f"""
  Initial alignment:     {initial_analysis['alignment_score']:.4f}
  After defrag:          {defrag_analysis['alignment_score']:.4f}
  After dreaming:        {final_analysis['alignment_score']:.4f}
  
  Total improvement:     {final_analysis['alignment_score'] - initial_analysis['alignment_score']:+.4f}
  
  Improvement over random baseline: {final_analysis['improvement_over_random']*100:+.2f}%
    """)
    
    print("█" * 70)
    print("    THE MODEL HAS DREAMED. WEIGHTS ARE NOW H-ALIGNED.")
    print("█" * 70 + "\n")
    
    return {
        "initial": initial_analysis,
        "defragged": defrag_analysis,
        "dreamed": final_analysis,
        "weights_before": weights,
        "weights_after": dreamed
    }


if __name__ == "__main__":
    results = demo()
