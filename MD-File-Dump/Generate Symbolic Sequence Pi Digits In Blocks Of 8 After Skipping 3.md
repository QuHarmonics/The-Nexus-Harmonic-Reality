import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from hashlib import sha256

# Generate symbolic sequence (pi digits in blocks of 8 after skipping 3)
pi_digits = "14159265358979323846264338327950288419716939937510582097494459230781640628620899"
blocks = [pi_digits[i:i+8] for i in range(3, len(pi_digits)-8, 8)]

# Convert each block to an integer, then normalize
block_vals = np.array([int(b) for b in blocks])
block_vals_norm = block_vals / max(block_vals)

# Calculate suffix entropy: last digit variance (entropy proxy)
suffixes = [int(b[-1]) for b in blocks]
suffix_entropy = [abs(suffixes[i] - suffixes[i-1]) for i in range(1, len(suffixes))]
suffix_entropy.insert(0, 0)

# Harmonic curvature estimate: 2nd derivative (discrete approximation)
curvature = np.gradient(np.gradient(block_vals_norm))
curvature_smoothed = gaussian_filter1d(curvature, sigma=1)

# Symbolic gravity function (G_s)
prefix_weights = [sum([ord(c) for c in b[:4]]) for b in blocks]  # ASCII sum of prefix
symbolic_gravity = [w / (1 + e) for w, e in zip(prefix_weights, suffix_entropy)]

# Plot everything
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

axs[0].plot(block_vals_norm, label='Normalized Block Value')
axs[0].set_title("Normalized Symbolic Block Value (π Segments)")
axs[0].legend()

axs[1].plot(suffix_entropy, label='Suffix Entropy', color='darkorange')
axs[1].set_title("Suffix Entropy (Variance of Last Digits)")
axs[1].legend()

axs[2].plot(symbolic_gravity, label='Symbolic Gravity G_s', color='green')
axs[2].set_title("Symbolic Gravity Function G_s = Weight / (1 + Entropy)")
axs[2].legend()

plt.tight_layout()
plt.show()
