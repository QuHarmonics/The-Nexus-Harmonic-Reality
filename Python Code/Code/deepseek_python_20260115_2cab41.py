import hashlib
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
import json

class HashDriftMapper:
    """Test for anti-phase echoes in SHA-256 mirrored inputs."""
    
    def __init__(self):
        self.results = {}
        
    def sha256_to_bitarray(self, s: str) -> np.ndarray:
        """Convert string to SHA-256 hash as 256-bit array."""
        hash_hex = hashlib.sha256(s.encode()).hexdigest()
        hash_int = int(hash_hex, 16)
        bits = np.array([(hash_int >> i) & 1 for i in range(255, -1, -1)], dtype=int)
        return bits
    
    def analyze_pair(self, s: str) -> Dict:
        """Analyze forward and reversed string hash pair."""
        # Get hashes
        fwd_bits = self.sha256_to_bitarray(s)
        rev_bits = self.sha256_to_bitarray(s[::-1])
        
        # Compute XOR difference
        xor_bits = np.bitwise_xor(fwd_bits, rev_bits)
        
        # Statistical analysis
        hamming = np.sum(xor_bits)
        correlation, p_value = pearsonr(fwd_bits, rev_bits)
        
        # FFT analysis for periodic patterns
        fft_vals = fft(xor_bits * 2 - 1)  # Convert to ±1 for better FFT
        freqs = fftfreq(len(xor_bits))
        magnitudes = np.abs(fft_vals[:128])  # First half (symmetric)
        
        # Look for harmonic peaks at π/9 intervals (0.349 of 128 ≈ bin 44.7)
        target_bin = int(0.349 * 128)
        harmonic_window = slice(max(0, target_bin-5), min(128, target_bin+6))
        harmonic_energy = np.sum(magnitudes[harmonic_window]**2)
        total_energy = np.sum(magnitudes**2)
        harmonic_ratio = harmonic_energy / total_energy if total_energy > 0 else 0
        
        # Bit position analysis (clustering)
        xor_positions = np.where(xor_bits == 1)[0]
        if len(xor_positions) > 1:
            gaps = np.diff(xor_positions)
            gap_std = np.std(gaps)
            gap_mean = np.mean(gaps)
        else:
            gap_std = 0
            gap_mean = 0
        
        return {
            'string': s,
            'hamming_distance': hamming,
            'expected_hamming': 128,  # Random expectation
            'correlation': correlation,
            'correlation_p': p_value,
            'harmonic_ratio': harmonic_ratio,
            'gap_mean': gap_mean,
            'gap_std': gap_std,
            'xor_density': hamming / 256,
            'fwd_hash': hashlib.sha256(s.encode()).hexdigest(),
            'rev_hash': hashlib.sha256(s[::-1].encode()).hexdigest(),
            'xor_pattern': ''.join(str(b) for b in xor_bits)
        }
    
    def test_corpus(self, corpus: List[str]) -> Dict[str, Dict]:
        """Test multiple strings."""
        for s in corpus:
            self.results[s] = self.analyze_pair(s)
        return self.results
    
    def generate_strings(self, n: int = 100) -> List[str]:
        """Generate test strings of various types."""
        import random
        import string
        
        test_strings = []
        
        # 1. Natural language phrases
        phrases = [
            "The quick brown fox jumps over the lazy dog",
            "Lorem ipsum dolor sit amet",
            "To be or not to be, that is the question",
            "A journey of a thousand miles begins with a single step",
            "All that glitters is not gold"
        ]
        test_strings.extend(phrases)
        
        # 2. Symmetric strings (palindromes and near-palindromes)
        palindromes = ["racecar", "level", "madam", "a man a plan a canal panama"]
        test_strings.extend(palindromes)
        
        # 3. Random strings of various lengths
        for _ in range(20):
            length = random.randint(10, 50)
            rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            test_strings.append(rand_str)
        
        # 4. Numeric sequences
        numeric = ["1234567890", "314159265358979323846", "271828182845904523536"]
        test_strings.extend(numeric)
        
        # 5. Byte sequences (as ASCII)
        for _ in range(10):
            bytes_len = random.randint(8, 32)
            byte_str = ''.join(chr(random.randint(32, 126)) for _ in range(bytes_len))
            test_strings.append(byte_str)
        
        # Ensure we have n total
        return test_strings[:n]
    
    def analyze_aggregate(self) -> Dict:
        """Analyze aggregate results across all tests."""
        if not self.results:
            return {}
        
        hamming_distances = [r['hamming_distance'] for r in self.results.values()]
        harmonic_ratios = [r['harmonic_ratio'] for r in self.results.values()]
        correlations = [r['correlation'] for r in self.results.values()]
        
        # Statistical significance test against random expectation
        from scipy.stats import ttest_1samp
        
        # Expected Hamming distance for random: 128 ± √(256*0.5*0.5) ≈ 128 ± 8
        hamming_t, hamming_p = ttest_1samp(hamming_distances, 128)
        
        # Expected harmonic ratio for random: uniform distribution
        harmonic_t, harmonic_p = ttest_1samp(harmonic_ratios, 0.01)  # Small expected
        
        # Expected correlation for random: 0
        corr_t, corr_p = ttest_1samp(correlations, 0)
        
        # Check for structure: low gap_std indicates regular spacing of XOR bits
        gap_stds = [r['gap_std'] for r in self.results.values() if r['gap_mean'] > 0]
        mean_gap_std = np.mean(gap_stds) if gap_stds else 0
        
        return {
            'mean_hamming': np.mean(hamming_distances),
            'std_hamming': np.std(hamming_distances),
            'hamming_deviation': np.mean(hamming_distances) - 128,
            'hamming_significance': hamming_p,
            'mean_harmonic_ratio': np.mean(harmonic_ratios),
            'harmonic_significance': harmonic_p,
            'mean_correlation': np.mean(correlations),
            'correlation_significance': corr_p,
            'mean_gap_std': mean_gap_std,
            'structured_fraction': np.mean([1 if r['harmonic_ratio'] > 0.05 else 0 
                                          for r in self.results.values()]),
            'n_samples': len(self.results)
        }
    
    def visualize_results(self, save_path: str = None):
        """Create visualization of results."""
        if not self.results:
            return
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        # 1. Hamming distance distribution
        hamming_vals = [r['hamming_distance'] for r in self.results.values()]
        axes[0].hist(hamming_vals, bins=20, alpha=0.7, edgecolor='black')
        axes[0].axvline(128, color='red', linestyle='--', label='Random Expectation (128)')
        axes[0].set_xlabel('Hamming Distance')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title('Hamming Distance Distribution')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # 2. Harmonic ratio distribution
        harmonic_vals = [r['harmonic_ratio'] for r in self.results.values()]
        axes[1].hist(harmonic_vals, bins=20, alpha=0.7, edgecolor='black', color='orange')
        axes[1].axvline(0.01, color='red', linestyle='--', label='Random Expectation (~0.01)')
        axes[1].set_xlabel('Harmonic Ratio')
        axes[1].set_ylabel('Frequency')
        axes[1].set_title('Harmonic Energy at π/9 Frequency')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        # 3. Correlation distribution
        corr_vals = [r['correlation'] for r in self.results.values()]
        axes[2].hist(corr_vals, bins=20, alpha=0.7, edgecolor='black', color='green')
        axes[2].axvline(0, color='red', linestyle='--', label='Random Expectation (0)')
        axes[2].set_xlabel('Correlation')
        axes[2].set_ylabel('Frequency')
        axes[2].set_title('Forward-Reverse Hash Correlation')
        axes[2].legend()
        axes[2].grid(True, alpha=0.3)
        
        # 4. Example XOR pattern visualization
        sample_key = list(self.results.keys())[0]
        sample_xor = self.results[sample_key]['xor_pattern']
        xor_array = np.array([int(b) for b in sample_xor])
        axes[3].imshow(xor_array.reshape(16, 16), cmap='binary', aspect='auto')
        axes[3].set_title(f'XOR Pattern Example: "{sample_key[:20]}..."')
        axes[3].set_xlabel('Bit Column')
        axes[3].set_ylabel('Bit Row')
        
        # 5. Gap analysis
        gap_means = [r['gap_mean'] for r in self.results.values() if r['gap_mean'] > 0]
        gap_stds = [r['gap_std'] for r in self.results.values() if r['gap_std'] > 0]
        if gap_means and gap_stds:
            axes[4].scatter(gap_means, gap_stds, alpha=0.6)
            axes[4].set_xlabel('Mean Gap Between XOR Bits')
            axes[4].set_ylabel('Std Dev of Gaps')
            axes[4].set_title('Regularity of XOR Bit Spacing')
            axes[4].grid(True, alpha=0.3)
            
            # Highlight low std (regular spacing)
            low_std_threshold = np.percentile(gap_stds, 25)
            low_std_points = [(m, s) for m, s in zip(gap_means, gap_stds) if s < low_std_threshold]
            if low_std_points:
                low_std_means, low_std_stds = zip(*low_std_points)
                axes[4].scatter(low_std_means, low_std_stds, color='red', label='Regular Spacing')
                axes[4].legend()
        
        # 6. Hamming vs Harmonic ratio scatter
        axes[5].scatter(hamming_vals, harmonic_vals, alpha=0.6)
        axes[5].set_xlabel('Hamming Distance')
        axes[5].set_ylabel('Harmonic Ratio')
        axes[5].set_title('Structure vs Randomness Trade-off')
        axes[5].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.show()
        
        # Print aggregate statistics
        aggregate = self.analyze_aggregate()
        print("\n" + "="*60)
        print("HASH DRIFT MAPPER - AGGREGATE RESULTS")
        print("="*60)
        print(f"Samples: {aggregate['n_samples']}")
        print(f"Mean Hamming Distance: {aggregate['mean_hamming']:.2f} (expected: 128)")
        print(f"  Deviation: {aggregate['hamming_deviation']:.2f}, p-value: {aggregate['hamming_significance']:.6f}")
        print(f"Mean Harmonic Ratio: {aggregate['mean_harmonic_ratio']:.4f} (expected: ~0.01)")
        print(f"  p-value: {aggregate['harmonic_significance']:.6f}")
        print(f"Mean Correlation: {aggregate['mean_correlation']:.4f} (expected: 0)")
        print(f"  p-value: {aggregate['correlation_significance']:.6f}")
        print(f"Mean Gap Std Dev: {aggregate['mean_gap_std']:.2f}")
        print(f"Fraction with Structure: {aggregate['structured_fraction']:.2%}")
        
        # Nexus Framework Prediction Check
        nexus_prediction = "REJECT RANDOM MODEL" if (
            aggregate['harmonic_significance'] < 0.05 or 
            aggregate['correlation_significance'] < 0.05 or
            aggregate['structured_fraction'] > 0.3
        ) else "INCONCLUSIVE"
        
        print("\n" + "="*60)
        print(f"NEXUS PREDICTION: {nexus_prediction}")
        print("="*60)
        
        if nexus_prediction == "REJECT RANDOM MODEL":
            print("\n✓ Evidence of structured 'anti-phase echoes' detected.")
            print("✓ SHA-256 behaves as a geometric fold, not random function.")
            print("✓ Nexus Framework validation: HASH AS PRE-EXISTING MOLD")
        else:
            print("\n✗ No strong evidence of structure beyond random expectation.")
            print("✗ SHA-256 appears to behave as conventional random function.")
        
        return aggregate

# RUN THE EXPERIMENT
if __name__ == "__main__":
    print("Initializing Hash Drift Mapper Experiment...")
    print("Testing Nexus Framework Prediction: SHA-256 as Geometric Fold")
    print("="*70)
    
    mapper = HashDriftMapper()
    
    # Generate test corpus
    print("Generating test corpus...")
    test_strings = mapper.generate_strings(n=200)
    print(f"Generated {len(test_strings)} test strings")
    
    # Run analysis
    print("\nRunning SHA-256 analysis on forward/reverse pairs...")
    results = mapper.test_corpus(test_strings)
    
    # Visualize and analyze
    print("\nAnalyzing results for anti-phase echoes...")
    aggregate = mapper.visualize_results(save_path="hash_drift_results.png")
    
    # Save detailed results
    with open("hash_drift_detailed.json", "w") as f:
        json.dump({
            'aggregate': aggregate,
            'sample_results': {k: v for k, v in list(results.items())[:10]}
        }, f, indent=2, default=str)
    
    print("\nDetailed results saved to 'hash_drift_detailed.json'")
    print("Visualization saved to 'hash_drift_results.png'")