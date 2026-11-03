# ============================================================
# DUAL-WAVE MÖBIUS TRANSFORMATION ALGEBRA
# Testing J² = I and JTJ = T⁻¹ on SHA-256 Schedule Growth
# ============================================================

import numpy as np
from collections import defaultdict
import hashlib
import struct
import itertools

# ------------------------------------------------------------
# 1. Define the SHA-256 schedule transformation T
# ------------------------------------------------------------

def sha256_message_schedule(seed_words):
    """
    Given 16 32-bit words (the seed), return the full 64-word schedule.
    This is the forward transformation T: seed → schedule.
    """
    if len(seed_words) != 16:
        raise ValueError("Need exactly 16 32-bit words")
    W = list(seed_words) + [0]*48
    for t in range(16, 64):
        s0 = (rotr(W[t-15], 7) ^ rotr(W[t-15], 18) ^ (W[t-15] >> 3)) & 0xFFFFFFFF
        s1 = (rotr(W[t-2], 17) ^ rotr(W[t-2], 19) ^ (W[t-2] >> 10)) & 0xFFFFFFFF
        W[t] = (W[t-16] + s0 + W[t-7] + s1) & 0xFFFFFFFF
    return W

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

# ------------------------------------------------------------
# 2. Define candidate involutions J
# ------------------------------------------------------------

def reverse_seed(seed):
    """Reverse the 16-word array."""
    return list(reversed(seed))

def complement_seed(seed):
    """Bitwise complement of each word."""
    return [(~w) & 0xFFFFFFFF for w in seed]

def reverse_and_complement(seed):
    """Reverse and complement."""
    return complement_seed(reverse_seed(seed))

def identity_j(seed):
    """Identity involution (trivial)."""
    return seed[:]

# List of involutions to test
involutions = {
    "reverse": reverse_seed,
    "complement": complement_seed,
    "reverse+complement": reverse_and_complement,
    "identity": identity_j,
}

# ------------------------------------------------------------
# 3. Test the Möbius conditions
# ------------------------------------------------------------

def test_mobius(J, T, state):
    """
    Test J² = I and JTJ = T⁻¹ on a given state.
    Returns True if both hold for that state.
    """
    # J² = I
    J2 = J(J(state))
    if tuple(J2) != tuple(state):
        return False, "J² ≠ I"

    # JTJ = T⁻¹
    # Compute T(state) = forward schedule
    T_state = T(state)
    # Apply J: J(T(state))
    JTJ_state = J(T_state)
    # Apply J to the original state first: J(state)
    J_state = J(state)
    # Then T⁻¹ is not directly available; but we can test by checking
    # T(JTJ_state) == state  (since JTJ = T⁻¹)
    # Actually condition is: T(JTJ_state) == state
    # That is: T(J(T(state))) == state
    # We need to verify T(J(T(state))) == state
    forward_of_dual = T(JTJ_state)  # This should be the original state
    if tuple(forward_of_dual) != tuple(state):
        return False, "T(JTJ) ≠ state (JTJ ≠ T⁻¹)"

    return True, "OK"

# ------------------------------------------------------------
# 4. Generate a set of random seed states for testing
# ------------------------------------------------------------

# Use a fixed seed for reproducibility
np.random.seed(42)

def random_seed():
    """Generate 16 random 32-bit words."""
    return [np.random.randint(0, 0xFFFFFFFF) for _ in range(16)]

# ------------------------------------------------------------
# 5. Run the tests
# ------------------------------------------------------------

print("=== DUAL-WAVE MÖBIUS TEST ON SHA-256 SCHEDULE ===\n")

# For each involution, test on 100 random seeds
n_tests = 100
results = {}

for name, J in involutions.items():
    print(f"Testing involution: {name}")
    passed = 0
    failed = 0
    for i in range(n_tests):
        state = random_seed()
        ok, msg = test_mobius(J, sha256_message_schedule, state)
        if ok:
            passed += 1
        else:
            failed += 1
            if i < 5:  # Show first few failures
                print(f"  Fail: {msg}")
    results[name] = (passed, failed)
    print(f"  Passed: {passed}/{n_tests}, Failed: {failed}/{n_tests}\n")

# ------------------------------------------------------------
# 6. If any involution passed, analyze its fixed points
# ------------------------------------------------------------

# We'll check for the reverse involution, as it's most likely
if results.get("reverse", (0, n_tests))[0] > 0:
    print("=== Analyzing fixed points of reverse involution ===\n")
    # Generate random seeds, find those that are fixed under reverse (palindrome seeds)
    fixed_seeds = []
    for _ in range(1000):
        seed = random_seed()
        if reverse_seed(seed) == seed:  # palindrome
            fixed_seeds.append(seed)

    print(f"Found {len(fixed_seeds)} palindrome seeds out of 1000")
    if fixed_seeds:
        # Test T on fixed seeds: does T(fixed) remain fixed?
        still_fixed = 0
        for seed in fixed_seeds[:20]:  # Test first 20
            sched = sha256_message_schedule(seed)
            # For a fixed point to be invariant under T, we need T(seed) = seed (but schedule is 64 words, so not same dimension)
            # Actually the transformation T maps 16 words to 64 words. For a fixed point, we need T(seed) = seed (impossible due to length change).
            # Instead, we can check if the output schedule is palindrome under some extension.
            # For now, we'll just note the existence.

        print("Fixed points exist under reverse, but T changes length, so T(fixed) is not directly fixed in the same space.")
        print("However, the reverse involution on the 16-word seed does show J² = I.")
        print("The condition JTJ = T⁻¹ may hold in a higher-dimensional space if T is extended appropriately.")
    else:
        print("No palindrome seeds found in the random sample.")
else:
    print("No involution passed the Möbius test.")

# ------------------------------------------------------------
# 7. Additional analysis: the reverse involution on the full schedule
# ------------------------------------------------------------

# We can also test J on the full 64-word schedule, by reversing the 64-word array.
def reverse_schedule(sched):
    return list(reversed(sched))

# Test on a random seed, generate schedule, then test reverse on schedule
print("\n=== Testing reverse on the full 64-word schedule ===\n")
seed = random_seed()
sched = sha256_message_schedule(seed)
rev_sched = reverse_schedule(sched)

# Check if J² = I on schedule
J2_sched = reverse_schedule(rev_sched)
print(f"J² = I on schedule: {J2_sched == sched}")

# JTJ = T⁻¹ on schedule: need to define T on schedules? Not straightforward.
# But we can test if rev_schedule is consistent with inverse mapping.
# Since T is not invertible on schedules (64 words from 16), we can't directly test T⁻¹.

print("\nDone.")