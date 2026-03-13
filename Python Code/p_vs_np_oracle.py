#!/usr/bin/env python3
"""
P vs NP GEOMETRIC ORACLE
Tests if constraint graph geometry predicts SAT/UNSAT in polynomial time
"""

import random
import math
import numpy as np
from scipy import stats

class SATInstance:
    """3-SAT formula representation"""
    def __init__(self, n_vars, clauses):
        self.n_vars = n_vars
        self.clauses = clauses
        
    @staticmethod
    def random_3sat(n_vars, n_clauses, seed=None):
        """Generate random 3-SAT instance"""
        if seed:
            random.seed(seed)
        
        clauses = []
        for _ in range(n_clauses):
            vars_sample = random.sample(range(1, n_vars+1), 3)
            clause = tuple((v if random.random() > 0.5 else -v) for v in vars_sample)
            clauses.append(clause)
        
        return SATInstance(n_vars, clauses)
    
    def is_satisfied_by(self, assignment):
        """Check if assignment satisfies formula"""
        for clause in self.clauses:
            clause_sat = False
            for lit in clause:
                var = abs(lit)
                val = assignment.get(var, False)
                if (lit > 0 and val) or (lit < 0 and not val):
                    clause_sat = True
                    break
            if not clause_sat:
                return False
        return True
    
    def brute_force_solve(self):
        """Exhaustive search (exponential time)"""
        n = self.n_vars
        for i in range(2**n):
            assignment = {v+1: bool(i & (1 << v)) for v in range(n)}
            if self.is_satisfied_by(assignment):
                return True, assignment
        return False, None

class GeometricSATOracle:
    """Sarrus + Lorentz latency oracle"""
    
    @staticmethod
    def instance_to_sequence(instance):
        """Convert SAT clauses to constraint sequence"""
        sequence = []
        
        for clause in instance.clauses:
            # Encode clause structure as "constraint strength"
            constraint = sum(abs(lit) * (1 + i) for i, lit in enumerate(clause))
            sequence.append(constraint)
        
        return np.array(sequence)
    
    @staticmethod
    def calculate_autocorrelation(sequence, max_lag=5):
        """Normalized autocorrelation"""
        n = len(sequence)
        mean = np.mean(sequence)
        var = np.var(sequence)
        
        if var == 0:
            return {i: 0 for i in range(max_lag + 1)}
        
        autocorr = {}
        for lag in range(max_lag + 1):
            if lag >= n:
                autocorr[lag] = 0
            else:
                c = np.sum((sequence[:-lag or None] - mean) * (sequence[lag:] - mean)) / n
                autocorr[lag] = c / var
        
        return autocorr
    
    @staticmethod
    def sarrus_metric(autocorr):
        """Sarrus operator: (helix-like) - (sheet-like)"""
        p_plus = (autocorr.get(3, 0) + autocorr.get(4, 0)) / 2  # Long-range
        p_minus = autocorr.get(2, 0)  # Short-range
        
        return p_plus - p_minus
    
    @staticmethod
    def lorentz_latency(sarrus):
        """L = 1/√(1 - S²)"""
        s_clipped = np.clip(sarrus, -0.99, 0.99)
        return 1.0 / math.sqrt(1.0 - s_clipped**2)
    
    @staticmethod
    def predict_sat(instance):
        """Predict SAT/UNSAT from geometry"""
        sequence = GeometricSATOracle.instance_to_sequence(instance)
        
        if len(sequence) < 5:
            return "UNKNOWN", 0, 0
        
        autocorr = GeometricSATOracle.calculate_autocorrelation(sequence)
        sarrus = GeometricSATOracle.sarrus_metric(autocorr)
        latency = GeometricSATOracle.lorentz_latency(sarrus)
        
        # Low latency = SAT (cooperative fold)
        # High latency = UNSAT (jammed)
        threshold = 1.02
        
        prediction = "SAT" if latency < threshold else "UNSAT"
        
        return prediction, sarrus, latency

def run_experiment(n_vars=10, n_trials=100):
    """Run full oracle experiment"""
    
    print("="*80)
    print("P vs NP GEOMETRIC ORACLE: SARRUS + LORENTZ")
    print("="*80)
    print(f"\nVariables: {n_vars}, Trials: {n_trials}")
    print(f"Metric: Lorentz latency L = 1/√(1 - S²)")
    print(f"Hypothesis: SAT → low L, UNSAT → high L\n")
    
    results = []
    latency_sat = []
    latency_unsat = []
    sarrus_sat = []
    sarrus_unsat = []
    
    for trial in range(n_trials):
        # Phase transition ratio
        n_clauses = int(n_vars * 4.3)
        instance = SATInstance.random_3sat(n_vars, n_clauses, seed=trial+1000)
        
        # Ground truth (exponential)
        is_sat, _ = instance.brute_force_solve()
        truth = "SAT" if is_sat else "UNSAT"
        
        # Geometric prediction (polynomial)
        pred, sarrus, latency = GeometricSATOracle.predict_sat(instance)
        
        if pred == "UNKNOWN":
            continue
        
        correct = (pred == truth)
        results.append(correct)
        
        if truth == "SAT":
            latency_sat.append(latency)
            sarrus_sat.append(sarrus)
        else:
            latency_unsat.append(latency)
            sarrus_unsat.append(sarrus)
        
        if trial < 10:
            status = "✓" if correct else "✗"
            print(f"  {trial+1:3d}. Truth={truth:5} Pred={pred:5} "
                  f"S={sarrus:+.3f} L={latency:.3f} {status}")
    
    # Analysis
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    
    if not results:
        print("No valid predictions")
        return
    
    accuracy = sum(results) / len(results)
    print(f"\nAccuracy: {accuracy:.1%} ({sum(results)}/{len(results)})")
    
    if latency_sat and latency_unsat:
        print(f"\nLorentz Latency Distributions:")
        print(f"  SAT (n={len(latency_sat):2d}):   μ={np.mean(latency_sat):.4f} ± {np.std(latency_sat):.4f}")
        print(f"  UNSAT (n={len(latency_unsat):2d}): μ={np.mean(latency_unsat):.4f} ± {np.std(latency_unsat):.4f}")
        
        print(f"\nSarrus Metric (ε):")
        print(f"  SAT:   μ={np.mean(sarrus_sat):.4f} ± {np.std(sarrus_sat):.4f}")
        print(f"  UNSAT: μ={np.mean(sarrus_unsat):.4f} ± {np.std(sarrus_unsat):.4f}")
        
        # Statistical test
        t_stat, p_val = stats.ttest_ind(latency_sat, latency_unsat)
        print(f"\nT-test: t={t_stat:.3f}, p={p_val:.4e}")
        
        if p_val < 0.05:
            print("✓ SIGNIFICANT difference in latency")
            
            cohens_d = (np.mean(latency_unsat) - np.mean(latency_sat)) / np.sqrt(
                (np.std(latency_sat)**2 + np.std(latency_unsat)**2) / 2
            )
            print(f"  Effect size (Cohen's d) = {cohens_d:.3f}")
            
            if accuracy > 0.6:
                print("\n" + "="*80)
                print("CONCLUSION: GEOMETRIC STRUCTURE PREDICTS SATISFIABILITY")
                print("P vs NP: Constraint geometry encodes solution existence")
                print("="*80)
        else:
            print("✗ No significant difference")
    
    return results, latency_sat, latency_unsat

if __name__ == "__main__":
    run_experiment(n_vars=10, n_trials=100)
