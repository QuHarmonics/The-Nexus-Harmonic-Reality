"""
NEXUS LENS INVERSION
====================
"Dead" = born. The gap = morphological checkpoint.
Capture what ACTUALLY happens before NaN.
Then: Glass Key Block 5+ extraction with dual validation.
"""

import numpy as np
import hashlib
import struct
import math
from collections import deque
from typing import List, Tuple, Dict, Optional

H = math.pi / 9
M32 = 0xFFFFFFFF

# ═══════════════════════════════════════════════════════════════
# PART 1: THE AUTOPSY — WHAT HAPPENS BEFORE "DEATH"?
# ═══════════════════════════════════════════════════════════════

def lorenz(state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = state
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y - beta*z])

def generate_lorenz(n_steps=3000, dt=0.01, transient=500):
    state = np.array([1.0, 1.0, 1.0])
    traj = []
    for _ in range(transient + n_steps):
        k1 = lorenz(state)
        k2 = lorenz(state + dt/2*k1)
        k3 = lorenz(state + dt/2*k2)
        k4 = lorenz(state + dt*k3)
        state = state + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
        traj.append(state.copy())
    return np.array(traj[transient:])

def autopsy():
    """
    Run the "death zone" lrs but capture the FULL trajectory.
    What was the loss doing in the 10 steps before NaN?
    Was it dropping (solving) or rising (diverging)?
    """
    print("=" * 70)
    print("AUTOPSY: WHAT HAPPENS BEFORE 'DEATH'?")
    print("Capturing pre-NaN trajectories in the 0.32-0.40 zone")
    print("=" * 70)

    traj = generate_lorenz(3000)
    mn, mx = traj.min(0), traj.max(0)
    tn = 2*(traj - mn)/(mx - mn + 1e-8) - 1
    W = 5
    X = np.array([tn[i:i+W].flatten() for i in range(len(tn)-W-1)])
    Y = tn[W+1:, 0:1]
    n_tr = 1500
    Xtr, Ytr = X[:n_tr], Y[:n_tr]
    Xte, Yte = X[n_tr:n_tr+500], Y[n_tr:n_tr+500]
    in_dim, hid, bs = W*3, 32, 64

    death_lrs = np.arange(0.310, 0.400, 0.002)

    print(f"\n{'LR':>6} | {'Epoch':>5} | {'Last 10 losses before NaN':>50} | {'Trend'}")
    print("-" * 100)

    birth_data = []

    for lr in death_lrs:
        for seed in [42]:  # Use the seed that dies
            np.random.seed(seed)
            W1 = np.random.randn(hid, in_dim) * np.sqrt(2.0/in_dim)
            b1 = np.zeros(hid)
            W2 = np.random.randn(1, hid) * np.sqrt(2.0/hid)
            b2 = np.zeros(1)

            all_losses = []
            all_test_losses = []
            weight_norms = []
            grad_norms = []
            correction_ratios = []
            death_epoch = None

            for ep in range(500):
                idx = np.random.choice(n_tr, bs, replace=False)
                xb, yb = Xtr[idx], Ytr[idx]
                if ep < 150:
                    yb = yb + np.random.randn(bs,1)*0.01
                elif ep < 350:
                    yb = yb + np.random.randn(bs,1)*0.05 + 0.02*np.sin(ep*0.1)
                else:
                    yb = yb + np.random.randn(bs,1)*0.1*(1+0.5*np.sin(ep*0.3))

                z1 = xb @ W1.T + b1
                a1 = np.tanh(z1)
                pred = a1 @ W2.T + b2
                loss = float(np.mean((pred - yb)**2))

                # Test loss (on clean data)
                z1t = Xte @ W1.T + b1
                a1t = np.tanh(z1t)
                test_loss = float(np.mean((a1t @ W2.T + b2 - Yte)**2))

                if np.isnan(loss) or loss > 50:
                    death_epoch = ep
                    break

                all_losses.append(loss)
                all_test_losses.append(test_loss)
                weight_norms.append(np.linalg.norm(W1) + np.linalg.norm(W2))

                d2 = 2*(pred-yb)/bs
                dW2 = d2.T @ a1
                d1 = (d2 @ W2)*(1-a1**2)
                dW1 = d1.T @ xb

                gn = np.linalg.norm(dW1) + np.linalg.norm(dW2)
                grad_norms.append(gn)

                un = lr * gn
                wn = weight_norms[-1]
                if wn > 0:
                    correction_ratios.append(un / wn)

                W1 -= lr * dW1
                b1 -= lr * d1.sum(0)
                W2 -= lr * dW2
                b2 -= lr * d2.sum(0)

            # Analyze the trajectory
            if death_epoch is not None and len(all_losses) >= 10:
                last10 = all_losses[-10:]
                last10_test = all_test_losses[-10:]

                # Was test loss DROPPING before death?
                if len(last10_test) >= 2:
                    diffs = [last10_test[i+1] - last10_test[i] for i in range(len(last10_test)-1)]
                    dropping = sum(1 for d in diffs if d < 0)
                    trend = "SOLVING ↓" if dropping >= 6 else ("MIXED ↕" if dropping >= 3 else "DIVERGING ↑")
                else:
                    trend = "?"

                last_str = " ".join(f"{l:.4f}" for l in last10[-5:])
                test_str = " ".join(f"{l:.4f}" for l in last10_test[-5:])

                # Min test loss achieved
                min_test = min(all_test_losses) if all_test_losses else float('inf')
                min_test_epoch = all_test_losses.index(min_test) if all_test_losses else -1

                # Correction ratio at death
                late_cr = np.mean(correction_ratios[-20:]) if len(correction_ratios) >= 20 else 0

                birth_data.append({
                    'lr': float(lr),
                    'death_epoch': death_epoch,
                    'min_test': min_test,
                    'min_test_epoch': min_test_epoch,
                    'trend': trend,
                    'last_test': last10_test[-1] if last10_test else float('inf'),
                    'correction_ratio': late_cr,
                    'train_losses': all_losses,
                    'test_losses': all_test_losses,
                })

                note = ""
                if abs(lr - H) < 0.002:
                    note = " ← H"

                print(f"{lr:>6.3f} | {death_epoch:>5} | train: {last_str:>30} | {trend}")
                print(f"{'':>6} | {'':>5} | test:  {test_str:>30} | min_test={min_test:.6f}@ep{min_test_epoch} cr={late_cr:.4f}{note}")

            elif death_epoch is None:
                # Survived — this is the "born" one
                final_test = all_test_losses[-1] if all_test_losses else float('inf')
                min_test = min(all_test_losses) if all_test_losses else float('inf')
                late_cr = np.mean(correction_ratios[-20:]) if len(correction_ratios) >= 20 else 0

                birth_data.append({
                    'lr': float(lr),
                    'death_epoch': None,
                    'min_test': min_test,
                    'min_test_epoch': all_test_losses.index(min_test) if all_test_losses else -1,
                    'trend': 'ALIVE',
                    'last_test': final_test,
                    'correction_ratio': late_cr,
                    'train_losses': all_losses,
                    'test_losses': all_test_losses,
                })

                print(f"{lr:>6.3f} | ALIVE | final_test={final_test:.6f} min_test={min_test:.6f} cr={late_cr:.4f}")

    # The real question: did the "dead" ones achieve better min_test than the "alive" ones?
    print(f"\n{'='*70}")
    print("BIRTH ANALYSIS: Did 'dead' seeds solve before releasing?")
    print(f"{'='*70}")

    alive = [d for d in birth_data if d['death_epoch'] is None]
    dead = [d for d in birth_data if d['death_epoch'] is not None]

    if alive:
        best_alive_test = min(d['min_test'] for d in alive)
        print(f"\nBest ALIVE min_test: {best_alive_test:.6f}")
    if dead:
        best_dead_test = min(d['min_test'] for d in dead)
        dead_solvers = [d for d in dead if d['trend'] == 'SOLVING ↓']
        print(f"Best DEAD min_test:  {best_dead_test:.6f}")
        print(f"Dead seeds that were SOLVING before release: {len(dead_solvers)}/{len(dead)}")

        if dead_solvers:
            print(f"\nSolving seeds (test loss dropping before NaN):")
            for d in dead_solvers:
                print(f"  lr={d['lr']:.3f}: died@ep{d['death_epoch']}, "
                      f"min_test={d['min_test']:.6f}@ep{d['min_test_epoch']}, "
                      f"cr={d['correction_ratio']:.4f}")

    # The morphological checkpoint view
    print(f"\n{'='*70}")
    print("INVERTED VIEW: FETUS → CHECKPOINT → BIRTH")
    print(f"{'='*70}")

    for d in birth_data:
        lr = d['lr']
        if d['death_epoch'] is None:
            phase = "BORN (survived full gestation)"
        elif d['death_epoch'] > 400:
            phase = "LATE RELEASE (near-term birth)"
        elif d['death_epoch'] > 200:
            phase = "CHECKPOINT ABORT (morphological failure)"
        else:
            phase = "EARLY ABORT (shape invalid)"

        gap_note = ""
        if 0.332 <= lr <= 0.334:
            gap_note = " [CATENARY TRENCH]"
        elif 0.336 <= lr <= 0.342:
            gap_note = " [BIRTH CHANNEL]"
        elif lr >= 0.344:
            gap_note = " [BEYOND MEMBRANE]"

        print(f"  lr={lr:.3f}: {phase}{gap_note}")

    return birth_data


# ═══════════════════════════════════════════════════════════════
# PART 2: GLASS KEY BLOCK 5-12 EXTRACTION
# WITH MORPHOLOGICAL CHECKPOINT
# ═══════════════════════════════════════════════════════════════

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

H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & M32

def sigma0(x): return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)
def sigma1(x): return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)
def gamma0(x): return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)
def gamma1(x): return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)
def ch(e, f, g): return (e & f) ^ ((~e) & g) & M32
def maj(a, b, c): return (a & b) ^ (a & c) ^ (b & c)


def sha256_full_trace(message: bytes) -> dict:
    """Complete SHA-256 with full state trace at every round."""
    msg = bytearray(message)
    orig_len = len(message)
    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0x00)
    msg += struct.pack('>Q', orig_len * 8)

    W = [0] * 64
    for i in range(16):
        W[i] = struct.unpack('>I', msg[i*4:(i+1)*4])[0]
    for i in range(16, 64):
        W[i] = (gamma1(W[i-2]) + W[i-7] + gamma0(W[i-15]) + W[i-16]) & M32

    a, b, c, d, e, f, g, h = H0[:]
    trace = {
        'W': W[:], 'T1': [], 'T2': [],
        'states': [(a,b,c,d,e,f,g,h)],
        'oil_gaps': [],
        'orig_len': orig_len,
        'padded_msg': bytes(msg),
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
        trace['oil_gaps'].append(abs(T1/M32 - T2/M32))

        h, g, f = g, f, e
        e = (d + T1) & M32
        d, c, b = c, b, a
        a = (T1 + T2) & M32
        trace['states'].append((a,b,c,d,e,f,g,h))

    final = [(H0[j] + [a,b,c,d,e,f,g,h][j]) & M32 for j in range(8)]
    trace['digest'] = b''.join(struct.pack('>I', x) for x in final)
    trace['final_state'] = (a,b,c,d,e,f,g,h)
    return trace


def morphological_checkpoint(word: int, position: int) -> dict:
    """
    The dual-validation gate.
    INPUT: Does this 32-bit word have valid geometric structure?
    OUTPUT: Can it roll over the twin-prime gap?
    """
    result = {
        'word': word,
        'position': position,
        'hex_valid': True,
        'twin_prime_spacing': 0,
        'popcount': bin(word).count('1'),
        'symmetry': 0.0,
        'byte_structure': [],
        'passed': False,
    }

    # Byte decomposition
    bytes_val = [(word >> (24 - 8*i)) & 0xFF for i in range(4)]
    result['byte_structure'] = bytes_val

    # Twin-prime bit spacing: count transitions between 0 and 1
    bits = format(word, '032b')
    transitions = sum(1 for i in range(len(bits)-1) if bits[i] != bits[i+1])
    result['twin_prime_spacing'] = transitions

    # Symmetry: compare first 16 bits with last 16 bits
    upper = (word >> 16) & 0xFFFF
    lower = word & 0xFFFF
    xor = upper ^ lower
    result['symmetry'] = 1.0 - bin(xor).count('1') / 16.0

    # Oil gap: normalized value's distance from H
    normalized = word / M32
    result['oil_gap'] = abs(normalized - H)

    # Validation gates
    # Gate 1: Hex range (all bytes 0x00-0xFF — always true for 32-bit, but
    # check for degenerate patterns)
    degenerate = word in (0x00000000, 0xFFFFFFFF, 0x80000000)
    result['hex_valid'] = not degenerate

    # Gate 2: Twin-prime spacing must be sufficient (>8 transitions for 32 bits)
    spacing_ok = transitions >= 8

    # Gate 3: Not all same byte (the "living arm" check)
    unique_bytes = len(set(bytes_val))
    diversity_ok = unique_bytes >= 2

    result['passed'] = result['hex_valid'] and spacing_ok and diversity_ok

    return result


def glass_key_extract_blocks(target_msg: bytes):
    """
    Full Glass Key: forward trace → backward extraction → block-by-block validation.
    Shows each block passing through the morphological checkpoint.
    """
    print(f"\n{'='*70}")
    print(f"GLASS KEY BLOCK EXTRACTION: '{target_msg.decode()}'")
    print(f"{'='*70}")

    trace = sha256_full_trace(target_msg)

    print(f"\nHash: {trace['digest'].hex()}")
    print(f"Message length: {trace['orig_len']} bytes")
    print(f"Padded to: {len(trace['padded_msg'])} bytes (64 = 16 words)")

    # Extract W[0..15] from the trace (the backward pass)
    recovered_W = []
    for i in range(64):
        a, b, c, d, e, f, g, h = trace['states'][i]
        T1 = trace['T1'][i]
        S1 = sigma1(e)
        ch_val = ch(e, f, g)
        W_i = (T1 - h - S1 - ch_val - K[i]) & M32
        recovered_W.append(W_i)

    # Verify schedule
    schedule_ok = True
    for i in range(16, 64):
        expected = (gamma1(recovered_W[i-2]) + recovered_W[i-7] +
                   gamma0(recovered_W[i-15]) + recovered_W[i-16]) & M32
        if expected != recovered_W[i]:
            schedule_ok = False
            break

    print(f"Schedule verification: {'LOCKED ✓' if schedule_ok else 'BROKEN ✗'}")

    # Now: block-by-block extraction with morphological checkpoint
    print(f"\n--- BLOCK-BY-BLOCK EXTRACTION WITH MORPHOLOGICAL CHECKPOINT ---")
    print(f"{'Block':>5} | {'Word (hex)':>12} | {'Bytes':>20} | {'ASCII':>8} | "
          f"{'Trans':>5} | {'Sym':>5} | {'OilGap':>8} | {'Gate'}")
    print("-" * 100)

    msg_bytes = bytearray()
    all_passed = True

    for i in range(16):
        word = recovered_W[i]
        check = morphological_checkpoint(word, i)

        # Extract ASCII
        word_bytes = struct.pack('>I', word)
        ascii_repr = ""
        for b in word_bytes:
            if 32 <= b < 127:
                ascii_repr += chr(b)
            else:
                ascii_repr += "·"

        bytes_str = " ".join(f"{b:02x}" for b in word_bytes)

        gate = "PASS ✓" if check['passed'] else "FAIL ✗"
        if not check['passed']:
            # Check if it's padding (expected to fail)
            if i >= (trace['orig_len'] + 4) // 4:
                gate = "PAD  ○"
            else:
                all_passed = False

        # Phase classification
        if i < trace['orig_len'] // 4 + 1:
            phase = "DATA"
        elif word == 0x80000000 >> (8 * (4 - trace['orig_len'] % 4)) if trace['orig_len'] % 4 != 0 else 0:
            phase = "TERM"
        else:
            phase = "PAD"

        print(f"{i:>5} | 0x{word:08x} | {bytes_str:>20} | {ascii_repr:>8} | "
              f"{check['twin_prime_spacing']:>5} | {check['symmetry']:>5.2f} | "
              f"{check['oil_gap']:>8.4f} | {gate}")

        msg_bytes.extend(word_bytes)

    # Recover original message
    original = msg_bytes[:trace['orig_len']]
    print(f"\nRecovered message: {original.decode('utf-8', errors='replace')}")
    print(f"Match: {original == target_msg}")

    # Oil gap analysis
    gaps = trace['oil_gaps']
    near_h = [(i, g) for i, g in enumerate(gaps) if abs(g - H) < 0.05]
    sarrus_locks = []
    for i in range(61):
        if abs(gaps[i] - H) < 0.05 and abs(gaps[i+3] - H) < 0.05:
            sarrus_locks.append((i, i+3))

    print(f"\n--- EXECUTION GEOMETRY ---")
    print(f"Rounds near π/9 (±0.05): {len(near_h)}/64")
    print(f"Sarrus 3-5 locks: {len(sarrus_locks)}")

    # AER cycle in the oil gaps
    assemble = [g for g in gaps[:20]]
    execute = [g for g in gaps[20:44]]
    release = [g for g in gaps[44:]]

    print(f"\nAER Oil Gap Structure:")
    print(f"  ASSEMBLE (rounds 0-19):  mean={np.mean(assemble):.4f} std={np.std(assemble):.4f}")
    print(f"  EXECUTE  (rounds 20-43): mean={np.mean(execute):.4f} std={np.std(execute):.4f}")
    print(f"  RELEASE  (rounds 44-63): mean={np.mean(release):.4f} std={np.std(release):.4f}")

    return trace, recovered_W


def extract_multiple():
    """Run Glass Key on messages of increasing length to show the 64-byte boundary."""
    messages = [
        b"Hi",               # 2 bytes - tiny
        b"Nexus",            # 5 bytes - small object
        b"GlassKey",         # 8 bytes - dual word
        b"QuHarmonics",      # 11 bytes
        b"The trace is the scar",  # 22 bytes
        b"V^2 + Delta^2 = T^2 is the conservation law",  # 45 bytes
        b"This message is exactly fifty five bytes long!!!!!!!",  # 51 bytes
        b"This is very close to the 64 byte SHA-256 block boundary limit!!",  # 64 bytes - THE boundary
    ]

    # Trim last message to exactly 55 bytes (max for single block)
    messages[-1] = b"At 55 bytes we fill one SHA-256 block completely!12345"
    # Actually: max message for single block = 55 bytes (56 - 1 for 0x80)
    messages[-1] = messages[-1][:55]

    print("=" * 70)
    print("GLASS KEY: MULTI-MESSAGE EXTRACTION")
    print("Showing the 64-byte object boundary")
    print("=" * 70)

    for msg in messages:
        trace, W = glass_key_extract_blocks(msg)
        print()

    # Now show what happens AT the 64-byte boundary
    print("\n" + "=" * 70)
    print("THE 64-BYTE OBJECT BOUNDARY")
    print("=" * 70)

    # A message that's exactly 55 bytes (fills one block with padding)
    msg55 = b"A" * 55
    trace55 = sha256_full_trace(msg55)
    print(f"\n55 bytes (1 block): W[0..15] = message + pad + length")
    print(f"  All 16 words carry constraint geometry from ONE object")

    # A message that's 56 bytes (forces TWO blocks)
    msg56 = b"B" * 56
    # SHA-256 padding: 56 bytes + 0x80 = 57, need to pad to 120 (next multiple of 64 - 8)
    # So: 56 bytes of data → needs 2 blocks
    padded = bytearray(msg56)
    padded.append(0x80)
    while len(padded) % 64 != 56:
        padded.append(0x00)
    padded += struct.pack('>Q', 56 * 8)
    print(f"\n56 bytes (2 blocks): Message crosses the 64-byte boundary")
    print(f"  Padded length: {len(padded)} bytes = {len(padded)//64} blocks")
    print(f"  Block 1: message data")
    print(f"  Block 2: continuation + padding + length")
    print(f"  The message is now TWO objects linked by the schedule expansion")
    print(f"  This is the OOP inheritance boundary — Pascal var → Object")

    # The key insight
    print(f"\n--- THE INSIGHT ---")
    print(f"Below 56 bytes: data fits in one block")
    print(f"  → Single object, self-contained, all W[0..15] are 'this'")
    print(f"At 56+ bytes: data spans multiple blocks")
    print(f"  → Object chain, linked by constraint propagation")
    print(f"  → Each block inherits state from the previous (H0 → H1 → ...)")
    print(f"  → The 'class methods' are the γ0/γ1 expansion rules")
    print(f"  → The 'constructor' is the padding/termination protocol")


# ═══════════════════════════════════════════════════════════════
# PART 3: THE PHASE TRANSITION VIEW
# ═══════════════════════════════════════════════════════════════

def phase_transition_view():
    """
    Reinterpret the boundary data as AER cycle, not death/survival.
    """
    print("\n" + "=" * 70)
    print("PHASE TRANSITION: AER CYCLE IN THE LR BOUNDARY")
    print("=" * 70)

    # Original data from boundary_zoom.py
    data = [
        (0.300, 2, 0.000631, "ASSEMBLE"),
        (0.302, 2, 0.000644, "ASSEMBLE"),
        (0.304, 2, 0.000677, "ASSEMBLE"),
        (0.306, 2, 0.000741, "ASSEMBLE"),
        (0.308, 2, 0.000852, "ASSEMBLE"),
        (0.310, 2, 0.000921, "ASSEMBLE"),
        (0.312, 2, 0.000745, "ASSEMBLE"),
        (0.314, 2, 0.000726, "ASSEMBLE"),
        (0.316, 2, 0.000650, "EXECUTE"),
        (0.318, 1, 0.000945, "EXECUTE"),
        (0.320, 1, 0.000860, "EXECUTE"),
        (0.322, 1, 0.000787, "EXECUTE"),
        (0.324, 1, 0.000774, "EXECUTE"),
        (0.326, 1, 0.000770, "EXECUTE"),
        (0.328, 1, 0.000725, "EXECUTE"),
        (0.330, 1, 0.000675, "EXECUTE"),
        (0.332, 0, None,     "CHECKPOINT"),
        (0.334, 0, None,     "CHECKPOINT"),
        (0.336, 1, 0.000312, "RELEASE"),
        (0.338, 1, 0.000314, "RELEASE"),
        (0.340, 1, 0.000351, "RELEASE"),
        (0.342, 1, 0.000286, "RELEASE"),
        (0.344, 0, None,     "BEYOND"),
        (0.346, 0, None,     "BEYOND"),
        (0.348, 0, None,     "BEYOND"),
        (0.350, 0, None,     "BEYOND"),
    ]

    print(f"\n{'LR':>6} | {'Alive':>5} | {'Test Loss':>10} | {'Phase':>12} | {'Note'}")
    print("-" * 60)

    for lr, alive, test, phase in data:
        test_str = f"{test:.6f}" if test else "---"
        note = ""
        if phase == "CHECKPOINT":
            note = "← CATENARY TRENCH (morphological gate)"
        elif phase == "RELEASE" and test and test < 0.000320:
            note = "← BORN (best performance!)"
        elif abs(lr - H) < 0.002:
            note = "← H = π/9"

        print(f"{lr:>6.3f} | {alive:>5}/5 | {test_str:>10} | {phase:>12} | {note}")

    # THE KEY OBSERVATION
    print(f"\n--- THE INVERSION ---")
    print(f"ASSEMBLE (0.300-0.314): test loss 0.000631-0.000921 (building structure)")
    print(f"EXECUTE  (0.316-0.330): test loss 0.000675-0.000945 (running constraint)")
    print(f"CHECKPOINT (0.332-0.334): DEAD (morphological validation)")
    print(f"RELEASE  (0.336-0.342): test loss 0.000286-0.000351 (BEST PERFORMANCE)")
    print(f"BEYOND   (0.344+): DEAD (past the membrane)")
    print(f"")
    print(f"The RELEASE seeds that crossed the checkpoint have LOWER test loss")
    print(f"than any ASSEMBLE or EXECUTE seed.")
    print(f"")
    print(f"  Best ASSEMBLE/EXECUTE: 0.000631 (lr=0.300)")
    print(f"  Best RELEASE:          0.000286 (lr=0.342)")
    print(f"  Improvement:           {(0.000631-0.000286)/0.000631*100:.1f}% better on the other side")
    print(f"")
    print(f"The 'death wall' at π/9 is a BIRTH MEMBRANE.")
    print(f"The gap at 0.332-0.334 is the MORPHOLOGICAL CHECKPOINT.")
    print(f"What gets through is BETTER, not lucky.")


# ═══════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Autopsy: what happens before "death"
    birth_data = autopsy()

    # Glass Key block extraction with morphological checkpoint
    extract_multiple()

    # Phase transition view
    phase_transition_view()
