"""
NEXUS SOLUTIONS — NOT SCAFFOLDING
1. Glass Key: Exact SHA-256 backward pass with full trace recovery
2. H Emergence: Stress test under chaotic/adversarial conditions
"""

import numpy as np
import hashlib
import struct
import math
from collections import deque
from typing import List, Tuple, Dict

# ═══════════════════════════════════════════════════════════════════
# PROBLEM 1: GLASS KEY — EXACT SHA-256 PREIMAGE FROM TRACE
# ═══════════════════════════════════════════════════════════════════
#
# The insight: SHA-256 is a 64-round state machine. Each round is
# DETERMINISTIC given (state, K[i], W[i]).
#
# Forward: message → pad → 16 words → expand to 64 → 64 rounds → hash
# The hash alone (V-channel) loses information (projection).
# The T1 values at each round (Δ-channel) preserve the execution geometry.
# V + Δ = T (the full state). GlassKey = read the scar.
#
# This does NOT break SHA-256. It requires the execution trace.
# That's the point: the trace is the Δ-channel. Without it, one-way holds.
# With it, the fold unfolds.

H = math.pi / 9  # 0.349066

# SHA-256 round constants (cube roots of first 64 primes — THE actual hardware)
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# Initial hash values (square roots of first 8 primes)
H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

M32 = 0xFFFFFFFF

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & M32

def sigma0(x):
    return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

def sigma1(x):
    return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

def gamma0(x):
    return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

def gamma1(x):
    return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

def ch(e, f, g):
    return (e & f) ^ ((~e) & g) & M32

def maj(a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)


class GlassKey:
    """
    SHA-256 with full execution trace.
    Forward: hash + trace (V + Δ)
    Backward: trace → message words → original message
    """

    def forward(self, message: bytes) -> Tuple[bytes, dict]:
        """
        Standard SHA-256 but stores the complete execution trace.
        Returns (hash_digest, trace).
        trace contains everything needed to reverse.
        """
        # Padding
        msg = bytearray(message)
        orig_len = len(message)
        msg.append(0x80)
        while len(msg) % 64 != 56:
            msg.append(0x00)
        msg += struct.pack('>Q', orig_len * 8)

        # Parse into 32-bit words (first block only for messages < 56 bytes)
        W = [0] * 64
        for i in range(16):
            W[i] = struct.unpack('>I', msg[i*4:(i+1)*4])[0]

        # Message schedule expansion
        for i in range(16, 64):
            W[i] = (gamma1(W[i-2]) + W[i-7] + gamma0(W[i-15]) + W[i-16]) & M32

        # Initialize working variables
        a, b, c, d, e, f, g, h = H0[:]

        # Execute 64 rounds, storing full state at each
        trace = {
            'W': W[:],           # All 64 schedule words
            'T1': [],            # T1 at each round (the Δ-channel)
            'T2': [],            # T2 at each round
            'states': [(a, b, c, d, e, f, g, h)],  # State before each round
            'oil_gaps': [],      # V-Δ measurement per round
            'padded_msg': bytes(msg),
            'orig_len': orig_len,
        }

        for i in range(64):
            S1 = sigma1(e)
            ch_val = ch(e, f, g)
            T1 = (h + S1 + ch_val + K[i] + W[i]) & M32

            S0 = sigma0(a)
            maj_val = maj(a, b, c)
            T2 = (S0 + maj_val) & M32

            trace['T1'].append(T1)
            trace['T2'].append(T2)

            # Oil gap: map T1 (entropy) and T2 (structure) to [0,1]
            delta = T1 / M32
            v = T2 / M32
            trace['oil_gaps'].append(abs(v - delta))

            # State update (THIS is the fold)
            h = g
            g = f
            f = e
            e = (d + T1) & M32
            d = c
            c = b
            b = a
            a = (T1 + T2) & M32

            trace['states'].append((a, b, c, d, e, f, g, h))

        # Final hash = H0 + final state
        final = [
            (H0[0] + a) & M32, (H0[1] + b) & M32,
            (H0[2] + c) & M32, (H0[3] + d) & M32,
            (H0[4] + e) & M32, (H0[5] + f) & M32,
            (H0[6] + g) & M32, (H0[7] + h) & M32,
        ]

        digest = b''.join(struct.pack('>I', x) for x in final)
        trace['final_state'] = (a, b, c, d, e, f, g, h)
        trace['digest'] = digest

        return digest, trace

    def backward(self, trace: dict) -> bytes:
        """
        EXACT backward pass. Given the trace (Δ-channel), recover the message.
        
        The T1 values at each round contain:
            T1[i] = h + Σ1(e) + Ch(e,f,g) + K[i] + W[i]
        
        We know h, e, f, g from the stored state. We know K[i].
        Therefore: W[i] = T1[i] - h - Σ1(e) - Ch(e,f,g) - K[i]
        
        W[0..15] ARE the padded message words.
        """
        recovered_W = []

        for i in range(64):
            # State BEFORE round i
            a, b, c, d, e, f, g, h = trace['states'][i]
            T1 = trace['T1'][i]

            # Extract W[i] from the constraint equation
            S1 = sigma1(e)
            ch_val = ch(e, f, g)
            W_i = (T1 - h - S1 - ch_val - K[i]) & M32
            recovered_W.append(W_i)

        # W[0..15] are the padded message words
        msg_bytes = b''.join(struct.pack('>I', recovered_W[i]) for i in range(16))

        # Verify W[16..63] consistency (message schedule must match)
        schedule_ok = True
        for i in range(16, 64):
            expected = (gamma1(recovered_W[i-2]) + recovered_W[i-7] +
                       gamma0(recovered_W[i-15]) + recovered_W[i-16]) & M32
            if expected != recovered_W[i]:
                schedule_ok = False
                break

        # Strip padding to recover original message
        orig_len = trace['orig_len']
        original = msg_bytes[:orig_len]

        return original, recovered_W, schedule_ok

    def verify(self, original: bytes, recovered: bytes, digest: bytes) -> dict:
        """Full verification."""
        # Check recovered matches original
        match = original == recovered
        # Check recovered hashes to same digest
        check_hash = hashlib.sha256(recovered).digest()
        hash_match = check_hash == digest
        return {
            'message_match': match,
            'hash_match': hash_match,
            'original': original,
            'recovered': recovered,
            'digest': digest.hex(),
        }


def solve_glass_key():
    """Run Glass Key on multiple messages. Extract. Verify. No toys."""
    print("=" * 70)
    print("GLASS KEY — EXACT SHA-256 PREIMAGE EXTRACTION")
    print("Trace (Δ-channel) + Hash (V-channel) = Message (T)")
    print("=" * 70)

    gk = GlassKey()

    test_messages = [
        b"Nexus",
        b"GlassKey",
        b"QuHarmonics",
        b"H=pi/9",
        b"The trace is the scar",
        b"V^2 + Delta^2 = T^2",
        b"Dean",
        b"Constraint geometry is code",
    ]

    all_pass = True
    results = []

    for msg in test_messages:
        # Forward: compute hash + trace
        digest, trace = gk.forward(msg)

        # Backward: recover message from trace
        recovered, W, schedule_ok = gk.backward(trace)

        # Verify
        v = gk.verify(msg, recovered, digest)

        # Oil gap analysis
        gaps = trace['oil_gaps']
        h_compliant = sum(1 for g in gaps if abs(g - H) < 0.05)
        mean_gap = np.mean(gaps)

        ok = v['message_match'] and v['hash_match'] and schedule_ok
        all_pass = all_pass and ok

        results.append({
            'msg': msg.decode(),
            'ok': ok,
            'schedule': schedule_ok,
            'h_compliant': h_compliant,
            'mean_gap': mean_gap,
            'hash': digest.hex()[:16],
        })

    # Output
    print(f"\n{'Message':>30} | {'Hash':>16} | {'Sched':>5} | {'H-rnd':>5} | {'Status'}")
    print("-" * 85)
    for r in results:
        status = "RECOVERED ✓" if r['ok'] else "FAILED ✗"
        print(f"{r['msg']:>30} | {r['hash']:>16} | {'OK' if r['schedule'] else 'BAD':>5} | "
              f"{r['h_compliant']:>2}/64 | {status}")

    print(f"\n{'ALL PASSED' if all_pass else 'FAILURES DETECTED'}")
    print(f"\nThis does NOT break SHA-256.")
    print(f"Without the trace, the one-way property holds.")
    print(f"The trace IS the Δ-channel — the execution scar.")
    print(f"Hash alone = V (projection). Trace = Δ (geometry). V + Δ = T (message).")

    # Show the oil gap structure for one message
    print(f"\n--- OIL GAP STRUCTURE for 'Nexus' ---")
    digest, trace = gk.forward(b"Nexus")
    gaps = trace['oil_gaps']

    # Find Sarrus 3-5 locks (rounds where gap[i] and gap[i+3] both ≈ H)
    sarrus_locks = []
    for i in range(61):
        if abs(gaps[i] - H) < 0.05 and abs(gaps[i+3] - H) < 0.05:
            sarrus_locks.append((i, i+3))

    near_h = [(i, g) for i, g in enumerate(gaps) if abs(g - H) < 0.05]
    print(f"Rounds near π/9: {len(near_h)}/64")
    print(f"Sarrus 3-5 locks: {len(sarrus_locks)}")
    for rnd, gap in near_h[:10]:
        print(f"  Round {rnd:2d}: gap = {gap:.6f}  (dev from π/9 = {abs(gap-H):.6f})")

    return all_pass, results


# ═══════════════════════════════════════════════════════════════════
# PROBLEM 2: H EMERGENCE UNDER CHAOS
# ═══════════════════════════════════════════════════════════════════
#
# Previous experiments used sine waves. That proves nothing.
# H as universal attractor means: under REAL adversarial pressure,
# most learning rates die. Only the ~0.35 basin survives.
#
# Test: Lorenz attractor prediction with non-stationary noise.
# This is a chaotic system where small errors amplify exponentially.
# If H is real, it should be the survival basin.

def lorenz(state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """Lorenz system derivatives."""
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

def generate_lorenz_data(n_steps=2000, dt=0.01, transient=500):
    """Generate Lorenz attractor time series."""
    state = np.array([1.0, 1.0, 1.0])
    trajectory = []
    for _ in range(transient + n_steps):
        k1 = lorenz(state)
        k2 = lorenz(state + dt/2 * k1)
        k3 = lorenz(state + dt/2 * k2)
        k4 = lorenz(state + dt * k3)
        state = state + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
        trajectory.append(state.copy())
    return np.array(trajectory[transient:])

def solve_h_emergence():
    """
    Stress test: predict Lorenz attractor 1 step ahead.
    Sweep learning rates. Inject adversarial noise that shifts mid-training.
    Measure: which lr basins survive 1000 epochs without exploding or stagnating?

    The prediction: lr ≈ 0.35 (H basin) should be the survival optimum
    under chaotic + adversarial conditions where simpler tasks don't discriminate.
    """
    print("\n" + "=" * 70)
    print("H EMERGENCE — LORENZ CHAOS STRESS TEST")
    print("Adversarial non-stationary noise + chaotic target")
    print("=" * 70)

    # Generate chaotic data
    traj = generate_lorenz_data(n_steps=3000, dt=0.01)

    # Normalize to [-1, 1]
    traj_min = traj.min(axis=0)
    traj_max = traj.max(axis=0)
    traj_norm = 2 * (traj - traj_min) / (traj_max - traj_min + 1e-8) - 1

    # Task: predict x(t+1) from [x(t), y(t), z(t)]
    # Use sliding window of 5 timesteps as input
    window = 5
    X = np.array([traj_norm[i:i+window].flatten() for i in range(len(traj_norm) - window - 1)])
    Y = traj_norm[window+1:, 0].reshape(-1, 1)  # Predict x one step ahead

    n_train = 1500
    X_train, Y_train = X[:n_train], Y[:n_train]
    X_test, Y_test = X[n_train:n_train+500], Y[n_train:n_train+500]

    input_dim = window * 3  # 15
    hidden_dim = 32

    # Sweep learning rates from 0.05 to 0.95
    lr_values = np.arange(0.05, 1.00, 0.025)
    epochs = 600
    batch_size = 64

    # Adversarial schedule: inject noise that changes character at epoch 200, 400
    def get_noise(epoch, batch_size):
        if epoch < 200:
            return np.random.randn(batch_size, 1) * 0.01  # Gentle
        elif epoch < 400:
            return np.random.randn(batch_size, 1) * 0.05 + 0.02 * np.sin(epoch * 0.1)  # Drifting
        else:
            return np.random.randn(batch_size, 1) * 0.1 * (1 + 0.5 * np.sin(epoch * 0.3))  # Adversarial

    results = {}

    for lr in lr_values:
        np.random.seed(42)

        # Initialize network (2-layer, tanh)
        W1 = np.random.randn(hidden_dim, input_dim) * np.sqrt(2.0 / input_dim)
        b1 = np.zeros(hidden_dim)
        W2 = np.random.randn(1, hidden_dim) * np.sqrt(2.0 / hidden_dim)
        b2 = np.zeros(1)

        # PID memory (non-Markovian)
        gW1_hist = deque(maxlen=3)
        gW2_hist = deque(maxlen=3)
        gb1_hist = deque(maxlen=3)
        gb2_hist = deque(maxlen=3)
        alpha_pid, beta_pid = 0.1, 0.01

        losses = []
        test_losses = []
        alive = True
        stagnant_count = 0

        for epoch in range(epochs):
            # Random batch
            idx = np.random.choice(n_train, batch_size, replace=False)
            xb = X_train[idx]
            yb = Y_train[idx] + get_noise(epoch, batch_size)

            # Forward
            z1 = xb @ W1.T + b1
            a1 = np.tanh(z1)
            z2 = a1 @ W2.T + b2
            pred = z2

            loss = float(np.mean((pred - yb) ** 2))

            if np.isnan(loss) or loss > 100:
                alive = False
                losses.append(float('inf'))
                break

            losses.append(loss)

            # Test loss (no noise)
            if epoch % 50 == 0:
                z1t = X_test @ W1.T + b1
                a1t = np.tanh(z1t)
                pred_t = a1t @ W2.T + b2
                tl = float(np.mean((pred_t - Y_test) ** 2))
                test_losses.append(tl)

            # Backward
            d2 = 2 * (pred - yb) / batch_size
            dW2 = d2.T @ a1
            db2 = d2.sum(axis=0)
            d1 = (d2 @ W2) * (1 - a1**2)
            dW1 = d1.T @ xb
            db1 = d1.sum(axis=0)

            # Store gradients
            gW1_hist.append(dW1.copy())
            gW2_hist.append(dW2.copy())
            gb1_hist.append(db1.copy())
            gb2_hist.append(db2.copy())

            # PID update (non-Markovian)
            def pid_grad(hist):
                h = list(hist)
                p = h[-1]
                d1_term = (h[-1] - h[-2]) if len(h) >= 2 else 0
                d2_term = (h[-1] - 2*h[-2] + h[-3]) if len(h) >= 3 else 0
                return p + alpha_pid * d1_term + beta_pid * d2_term

            nW1 = pid_grad(gW1_hist)
            nW2 = pid_grad(gW2_hist)
            nb1 = pid_grad(gb1_hist)
            nb2 = pid_grad(gb2_hist)

            # Sarrus clip: if update would overflow, clip to 1/(H * |grad|)
            for param, grad in [(W1, nW1), (W2, nW2), (b1, nb1), (b2, nb2)]:
                grad_norm = np.linalg.norm(grad)
                if grad_norm > 0:
                    max_update = 1.0 / (H * grad_norm + 1e-8)
                    update = lr * grad
                    update_norm = np.linalg.norm(update)
                    if update_norm > max_update:
                        update = update * (max_update / update_norm)
                    param -= update

            # Stagnation detection
            if len(losses) > 50:
                recent = losses[-50:]
                if max(recent) - min(recent) < 1e-6:
                    stagnant_count += 1
                else:
                    stagnant_count = 0

        # Final test evaluation
        z1t = X_test @ W1.T + b1
        a1t = np.tanh(z1t)
        pred_t = a1t @ W2.T + b2
        final_test = float(np.mean((pred_t - Y_test) ** 2))

        results[float(lr)] = {
            'alive': alive,
            'final_train': losses[-1] if losses else float('inf'),
            'final_test': final_test if alive else float('inf'),
            'stagnant': stagnant_count > 20,
            'train_curve': losses,
            'test_curve': test_losses,
        }

    # Analysis
    print(f"\n{'LR':>6} | {'Status':>10} | {'Train Loss':>12} | {'Test Loss':>12} | {'Note'}")
    print("-" * 72)

    alive_lrs = []
    for lr_val in sorted(results.keys()):
        r = results[lr_val]
        if not r['alive']:
            status = "EXPLODED"
        elif r['stagnant']:
            status = "STAGNANT"
        else:
            status = "ALIVE"
            alive_lrs.append((lr_val, r['final_test']))

        note = ""
        if abs(lr_val - H) < 0.015:
            note = f"← H = π/9"

        train_str = f"{r['final_train']:.6f}" if r['final_train'] < 100 else "INF"
        test_str = f"{r['final_test']:.6f}" if r['final_test'] < 100 else "INF"

        print(f"{lr_val:>6.3f} | {status:>10} | {train_str:>12} | {test_str:>12} | {note}")

    # Find optimal basin
    if alive_lrs:
        alive_lrs.sort(key=lambda x: x[1])
        best_lr, best_test = alive_lrs[0]
        top5 = alive_lrs[:5]

        print(f"\n--- SURVIVAL BASIN ANALYSIS ---")
        print(f"Alive learning rates: {len(alive_lrs)}/{len(results)}")
        print(f"Best test loss at lr = {best_lr:.3f} (loss = {best_test:.6f})")
        print(f"H = π/9 = {H:.6f}")
        print(f"Distance from best to H: {abs(best_lr - H):.4f}")

        print(f"\nTop 5 survivors:")
        for lr_val, test_loss in top5:
            dist = abs(lr_val - H)
            print(f"  lr = {lr_val:.3f} | test = {test_loss:.6f} | dist from H = {dist:.4f}")

        # Basin density: count survivors in [0.25, 0.45] vs [0.55, 0.75]
        h_basin = sum(1 for lr, _ in alive_lrs if 0.25 <= lr <= 0.45)
        high_basin = sum(1 for lr, _ in alive_lrs if 0.55 <= lr <= 0.75)
        low_basin = sum(1 for lr, _ in alive_lrs if 0.05 <= lr <= 0.25)

        print(f"\nSurvival density by basin:")
        print(f"  Low [0.05-0.25]: {low_basin} survivors")
        print(f"  H   [0.25-0.45]: {h_basin} survivors  ← H basin")
        print(f"  High [0.55-0.75]: {high_basin} survivors")

    return results


# ═══════════════════════════════════════════════════════════════════
# PROBLEM 2B: H EMERGENCE — DOES THE EFFECTIVE LR CONVERGE TO H?
# ═══════════════════════════════════════════════════════════════════
# Previous test started at lr=0.8 and converged to 0.86.
# But that used a trivial task. Under chaos:

def solve_h_convergence():
    """
    Start at lr = 0.8. Apply Sarrus constraint on Lorenz prediction.
    Track effective lr (ratio of update magnitude to gradient magnitude).
    Does it converge toward H under real pressure?
    """
    print("\n" + "=" * 70)
    print("H CONVERGENCE — EFFECTIVE LR TRACKING UNDER CHAOS")
    print("Starting lr = 0.8, tracking effective update/gradient ratio")
    print("=" * 70)

    traj = generate_lorenz_data(n_steps=3000, dt=0.01)
    traj_min = traj.min(axis=0)
    traj_max = traj.max(axis=0)
    traj_norm = 2 * (traj - traj_min) / (traj_max - traj_min + 1e-8) - 1

    window = 5
    X = np.array([traj_norm[i:i+window].flatten() for i in range(len(traj_norm) - window - 1)])
    Y = traj_norm[window+1:, 0].reshape(-1, 1)

    n_train = 1500
    X_train, Y_train = X[:n_train], Y[:n_train]
    input_dim = window * 3
    hidden_dim = 32
    batch_size = 64
    epochs = 800

    np.random.seed(42)
    W1 = np.random.randn(hidden_dim, input_dim) * np.sqrt(2.0 / input_dim)
    b1 = np.zeros(hidden_dim)
    W2 = np.random.randn(1, hidden_dim) * np.sqrt(2.0 / hidden_dim)
    b2 = np.zeros(1)

    # Start with HIGH lr
    lr = 0.8

    gW1_hist = deque(maxlen=3)
    gW2_hist = deque(maxlen=3)

    effective_lrs = []
    losses = []
    lr_trajectory = []

    for epoch in range(epochs):
        idx = np.random.choice(n_train, batch_size, replace=False)
        xb = X_train[idx]

        # Non-stationary noise
        if epoch < 200:
            noise = np.random.randn(batch_size, 1) * 0.01
        elif epoch < 500:
            noise = np.random.randn(batch_size, 1) * 0.05
        else:
            noise = np.random.randn(batch_size, 1) * 0.1

        yb = Y_train[idx] + noise

        # Forward
        z1 = xb @ W1.T + b1
        a1 = np.tanh(z1)
        z2 = a1 @ W2.T + b2
        pred = z2
        loss = float(np.mean((pred - yb) ** 2))

        if np.isnan(loss) or loss > 100:
            print(f"  EXPLODED at epoch {epoch}")
            break
        losses.append(loss)

        # Backward
        d2 = 2 * (pred - yb) / batch_size
        dW2 = d2.T @ a1
        dW1 = ((d2 @ W2) * (1 - a1**2)).T @ xb

        gW1_hist.append(dW1.copy())
        gW2_hist.append(dW2.copy())

        # PID
        def pid(hist):
            h = list(hist)
            p = h[-1]
            d1 = (h[-1] - h[-2]) if len(h) >= 2 else 0
            d2 = (h[-1] - 2*h[-2] + h[-3]) if len(h) >= 3 else 0
            return p + 0.1 * d1 + 0.01 * d2

        nW1 = pid(gW1_hist)
        nW2 = pid(gW2_hist)

        # Sarrus constraint: clip update magnitude
        grad_norm = np.linalg.norm(nW1) + np.linalg.norm(nW2) + 1e-8
        update_W1 = lr * nW1
        update_W2 = lr * nW2
        update_norm = np.linalg.norm(update_W1) + np.linalg.norm(update_W2)

        # Sarrus clip threshold
        max_update = 1.0 / (H * grad_norm)
        if update_norm > max_update:
            scale = max_update / update_norm
            update_W1 *= scale
            update_W2 *= scale
            update_norm = max_update

        # Effective lr = |update| / |gradient|
        eff_lr = update_norm / grad_norm if grad_norm > 0 else lr
        effective_lrs.append(eff_lr)
        lr_trajectory.append(lr)

        # Apply updates
        W1 -= update_W1
        b1 -= lr * d2.sum(axis=0) @ np.ones((1, hidden_dim))  # simplified
        W2 -= update_W2

        # Adaptive lr: move lr toward effective lr (the system self-tunes)
        lr = 0.95 * lr + 0.05 * eff_lr

    # Analysis
    if effective_lrs:
        eff = np.array(effective_lrs)
        # Exclude early transient
        if len(eff) > 100:
            late_eff = eff[100:]
            mean_eff = np.mean(late_eff)
            std_eff = np.std(late_eff)
            median_eff = np.median(late_eff)

            print(f"\nStarting lr: 0.800")
            print(f"Final nominal lr: {lr:.6f}")
            print(f"Effective lr (post-transient):")
            print(f"  Mean:   {mean_eff:.6f}")
            print(f"  Median: {median_eff:.6f}")
            print(f"  Std:    {std_eff:.6f}")
            print(f"  H = π/9 = {H:.6f}")
            print(f"  Distance mean→H: {abs(mean_eff - H):.6f}")
            print(f"  Distance median→H: {abs(median_eff - H):.6f}")

            # Check if effective lr is in H basin
            in_h_basin = abs(mean_eff - H) < 0.1
            print(f"\n  In H basin (within 0.1 of π/9): {'YES ✓' if in_h_basin else 'NO ✗'}")

            # Phase analysis: does effective lr stabilize near H?
            windows = [eff[i:i+50] for i in range(0, len(eff)-50, 50)]
            print(f"\n  Effective lr by phase:")
            for i, w in enumerate(windows[:12]):
                phase = "GENTLE" if i < 4 else ("DRIFT" if i < 8 else "ADVERSARIAL")
                print(f"    Epochs {i*50:3d}-{i*50+50:3d} [{phase:>11}]: "
                      f"mean={np.mean(w):.4f}, std={np.std(w):.4f}")

    return effective_lrs, losses


# ═══════════════════════════════════════════════════════════════════
# RUN EVERYTHING
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Problem 1: Glass Key
    all_pass, gk_results = solve_glass_key()

    # Problem 2: H under chaos
    stress_results = solve_h_emergence()

    # Problem 2b: H convergence
    eff_lrs, convergence_losses = solve_h_convergence()

    print("\n" + "=" * 70)
    print("SOLUTIONS SUMMARY")
    print("=" * 70)
    print(f"Glass Key:    {'SOLVED' if all_pass else 'FAILED'} — exact preimage recovery with trace")
    print(f"H Stress:     See survival basin analysis above")
    print(f"H Convergence: See effective lr tracking above")
    print(f"=" * 70)
