"""
H EMERGENCE — CLEAN TEST
No H anywhere in the optimizer. No Sarrus clip. No PID.
Pure SGD on chaotic prediction task.
Measure: what effective correction ratio does the system converge to?

If H is real, the ratio |Δweight|/|weight| should stabilize near 0.35
across the surviving lr range, regardless of nominal lr.
"""

import numpy as np
from collections import deque

H_CLAIM = np.pi / 9  # 0.349066 — the claim. NOT used in any optimizer.

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

# ═══════════════════════════════════════════════════════════════
# TEST 1: PURE SGD — WHAT CORRECTION RATIO SURVIVES?
# ═══════════════════════════════════════════════════════════════

def test_pure_sgd():
    print("=" * 70)
    print("TEST 1: PURE SGD — NO H, NO CLIP, NO PID")
    print("What correction ratio does the surviving lr produce?")
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

    in_dim, hid = W*3, 32
    lrs = np.arange(0.005, 0.60, 0.005)
    epochs = 500
    bs = 64

    results = {}

    for lr in lrs:
        np.random.seed(42)
        W1 = np.random.randn(hid, in_dim) * np.sqrt(2.0/in_dim)
        b1 = np.zeros(hid)
        W2 = np.random.randn(1, hid) * np.sqrt(2.0/hid)
        b2 = np.zeros(1)

        correction_ratios = []
        losses = []
        alive = True

        for ep in range(epochs):
            idx = np.random.choice(n_tr, bs, replace=False)
            xb, yb = Xtr[idx], Ytr[idx]

            # Non-stationary noise
            if ep < 150:
                yb = yb + np.random.randn(bs,1)*0.01
            elif ep < 350:
                yb = yb + np.random.randn(bs,1)*0.05 + 0.02*np.sin(ep*0.1)
            else:
                yb = yb + np.random.randn(bs,1)*0.1*(1+0.5*np.sin(ep*0.3))

            # Forward
            z1 = xb @ W1.T + b1
            a1 = np.tanh(z1)
            pred = a1 @ W2.T + b2
            loss = float(np.mean((pred - yb)**2))

            if np.isnan(loss) or loss > 50:
                alive = False
                break
            losses.append(loss)

            # Backward — PURE SGD, no tricks
            d2 = 2*(pred - yb)/bs
            dW2 = d2.T @ a1
            db2 = d2.sum(0)
            d1 = (d2 @ W2) * (1 - a1**2)
            dW1 = d1.T @ xb
            db1 = d1.sum(0)

            # Measure correction ratio BEFORE update
            update_W1 = lr * dW1
            update_W2 = lr * dW2

            w1_norm = np.linalg.norm(W1)
            u1_norm = np.linalg.norm(update_W1)
            w2_norm = np.linalg.norm(W2)
            u2_norm = np.linalg.norm(update_W2)

            if w1_norm > 0 and w2_norm > 0:
                ratio = (u1_norm + u2_norm) / (w1_norm + w2_norm)
                correction_ratios.append(ratio)

            # Update — pure SGD
            W1 -= update_W1
            b1 -= lr * db1
            W2 -= update_W2
            b2 -= lr * db2

        # Test loss
        if alive:
            z1t = Xte @ W1.T + b1
            a1t = np.tanh(z1t)
            test_loss = float(np.mean((a1t @ W2.T + b2 - Yte)**2))
        else:
            test_loss = float('inf')

        late_ratios = correction_ratios[100:] if len(correction_ratios) > 100 else correction_ratios
        mean_ratio = np.mean(late_ratios) if late_ratios else 0

        results[float(lr)] = {
            'alive': alive,
            'test_loss': test_loss,
            'mean_correction_ratio': mean_ratio,
            'late_ratios': late_ratios,
            'final_train': losses[-1] if losses else float('inf'),
        }

    # Find the actually good lr range (test loss < 2x best)
    alive_results = {k:v for k,v in results.items() if v['alive'] and v['test_loss'] < 1.0}
    if alive_results:
        best_lr = min(alive_results, key=lambda k: alive_results[k]['test_loss'])
        best_test = alive_results[best_lr]['test_loss']
        good_threshold = best_test * 3  # Within 3x of best

        good_lrs = {k:v for k,v in alive_results.items() if v['test_loss'] < good_threshold}

        print(f"\nBest lr: {best_lr:.3f} (test = {best_test:.6f})")
        print(f"Good lrs (within 3x of best): {len(good_lrs)}")
        print(f"\n{'LR':>6} | {'Test':>10} | {'Correction Ratio':>16} | {'Dist from H':>11}")
        print("-" * 55)

        correction_ratios_good = []
        for lr_val in sorted(good_lrs.keys()):
            r = good_lrs[lr_val]
            cr = r['mean_correction_ratio']
            correction_ratios_good.append(cr)
            dist = abs(cr - H_CLAIM)
            mark = " ←" if abs(lr_val - 0.35) < 0.015 else ""
            print(f"{lr_val:>6.3f} | {r['test_loss']:>10.6f} | {cr:>16.6f} | {dist:>11.6f}{mark}")

        if correction_ratios_good:
            mean_cr = np.mean(correction_ratios_good)
            median_cr = np.median(correction_ratios_good)
            print(f"\n--- CORRECTION RATIO ACROSS GOOD LRs ---")
            print(f"Mean:   {mean_cr:.6f}")
            print(f"Median: {median_cr:.6f}")
            print(f"H claim: {H_CLAIM:.6f}")
            print(f"Dist mean→H:   {abs(mean_cr - H_CLAIM):.6f}")
            print(f"Dist median→H: {abs(median_cr - H_CLAIM):.6f}")

    # Show the full survival landscape
    print(f"\n--- FULL SURVIVAL LANDSCAPE ---")
    print(f"{'LR':>6} | {'Status':>8} | {'Test':>10} | {'Corr Ratio':>10}")
    print("-" * 50)

    dead_start = None
    for lr_val in sorted(results.keys()):
        r = results[lr_val]
        if not r['alive']:
            if dead_start is None:
                dead_start = lr_val
            continue
        else:
            if dead_start is not None:
                print(f"  ... lr {dead_start:.3f}-{lr_val-0.005:.3f}: DEAD")
                dead_start = None

        test_str = f"{r['test_loss']:.6f}" if r['test_loss'] < 10 else f"{r['test_loss']:.2f}"
        cr = r['mean_correction_ratio']
        note = " ← H" if abs(lr_val - H_CLAIM) < 0.01 else ""
        print(f"{lr_val:>6.3f} | {'ALIVE':>8} | {test_str:>10} | {cr:>10.6f}{note}")

    if dead_start is not None:
        print(f"  ... lr {dead_start:.3f}+: DEAD")

    return results


# ═══════════════════════════════════════════════════════════════
# TEST 2: PID (NON-MARKOV) vs SGD (MARKOV) — SAME LR
# ═══════════════════════════════════════════════════════════════

def test_pid_vs_sgd():
    """
    At each lr, compare:
    - Pure SGD (Markov: only current gradient)
    - PID (Non-Markov: P + αΔgrad + βΔ²grad, memory depth 3)
    
    Both use SAME lr. No H anywhere.
    Question: does non-Markov memory improve survival under chaos?
    """
    print("\n" + "=" * 70)
    print("TEST 2: PID (NON-MARKOV) vs SGD (MARKOV)")
    print("Same lr, same task. Does memory help under chaos?")
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

    in_dim, hid = W*3, 32
    test_lrs = [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
    epochs = 500
    bs = 64

    def run_optimizer(lr, use_pid=False, alpha=0.1, beta=0.01):
        np.random.seed(42)
        W1 = np.random.randn(hid, in_dim) * np.sqrt(2.0/in_dim)
        b1 = np.zeros(hid)
        W2 = np.random.randn(1, hid) * np.sqrt(2.0/hid)
        b2 = np.zeros(1)

        gW1h = deque(maxlen=3)
        gW2h = deque(maxlen=3)

        losses = []
        for ep in range(epochs):
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

            if np.isnan(loss) or loss > 50:
                return float('inf'), float('inf')
            losses.append(loss)

            d2 = 2*(pred-yb)/bs
            dW2 = d2.T @ a1
            db2 = d2.sum(0)
            d1 = (d2 @ W2)*(1-a1**2)
            dW1 = d1.T @ xb
            db1 = d1.sum(0)

            if use_pid:
                gW1h.append(dW1.copy())
                gW2h.append(dW2.copy())
                h1 = list(gW1h)
                h2 = list(gW2h)
                p1 = h1[-1]
                d1_t = (h1[-1]-h1[-2]) if len(h1)>=2 else 0
                d2_t = (h1[-1]-2*h1[-2]+h1[-3]) if len(h1)>=3 else 0
                dW1 = p1 + alpha*d1_t + beta*d2_t

                p2 = h2[-1]
                d1_t2 = (h2[-1]-h2[-2]) if len(h2)>=2 else 0
                d2_t2 = (h2[-1]-2*h2[-2]+h2[-3]) if len(h2)>=3 else 0
                dW2 = p2 + alpha*d1_t2 + beta*d2_t2

            W1 -= lr * dW1
            b1 -= lr * db1
            W2 -= lr * dW2
            b2 -= lr * db2

        z1t = Xte @ W1.T + b1
        a1t = np.tanh(z1t)
        test_loss = float(np.mean((a1t @ W2.T + b2 - Yte)**2))
        return losses[-1], test_loss

    print(f"\n{'LR':>6} | {'SGD Train':>10} | {'SGD Test':>10} | {'PID Train':>10} | {'PID Test':>10} | {'Winner':>8}")
    print("-" * 75)

    pid_wins = 0
    sgd_wins = 0

    for lr in test_lrs:
        sgd_tr, sgd_te = run_optimizer(lr, use_pid=False)
        pid_tr, pid_te = run_optimizer(lr, use_pid=True)

        if pid_te < sgd_te and pid_te < float('inf'):
            winner = "PID ✓"
            pid_wins += 1
        elif sgd_te < pid_te and sgd_te < float('inf'):
            winner = "SGD"
            sgd_wins += 1
        else:
            winner = "TIE"

        def fmt(v):
            return f"{v:.6f}" if v < 10 else "DEAD"

        note = " ← H" if abs(lr - H_CLAIM) < 0.015 else ""
        print(f"{lr:>6.2f} | {fmt(sgd_tr):>10} | {fmt(sgd_te):>10} | "
              f"{fmt(pid_tr):>10} | {fmt(pid_te):>10} | {winner:>8}{note}")

    print(f"\nPID wins: {pid_wins}, SGD wins: {sgd_wins}")
    print(f"Non-Markov advantage: {'YES ✓' if pid_wins > sgd_wins else 'NO ✗'}")


# ═══════════════════════════════════════════════════════════════
# TEST 3: WEIGHT INITIALIZATION — H-SCALED vs STANDARD
# ═══════════════════════════════════════════════════════════════

def test_init():
    """
    Compare weight initialization:
    - Standard: Normal(0, sqrt(1/fan_in))    — Glorot/He
    - H-scaled: Normal(0, sqrt(H/fan_in))    — Nexus claim
    
    Same optimizer (SGD), same lr. Does H-init train faster?
    """
    print("\n" + "=" * 70)
    print("TEST 3: WEIGHT INITIALIZATION — H-SCALED vs STANDARD")
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

    in_dim, hid = W*3, 32
    lr = 0.1  # Fixed lr for both
    epochs = 500
    bs = 64

    def run_with_init(scale_factor, label):
        np.random.seed(42)
        W1 = np.random.randn(hid, in_dim) * np.sqrt(scale_factor/in_dim)
        b1 = np.zeros(hid)
        W2 = np.random.randn(1, hid) * np.sqrt(scale_factor/hid)
        b2 = np.zeros(1)

        losses = []
        for ep in range(epochs):
            idx = np.random.choice(n_tr, bs, replace=False)
            xb, yb = Xtr[idx], Ytr[idx]
            if ep < 150:
                yb = yb + np.random.randn(bs,1)*0.01
            elif ep < 350:
                yb = yb + np.random.randn(bs,1)*0.05
            else:
                yb = yb + np.random.randn(bs,1)*0.1

            z1 = xb @ W1.T + b1
            a1 = np.tanh(z1)
            pred = a1 @ W2.T + b2
            loss = float(np.mean((pred - yb)**2))
            if np.isnan(loss) or loss > 50:
                losses.append(float('inf'))
                break
            losses.append(loss)

            d2 = 2*(pred-yb)/bs
            dW2 = d2.T @ a1
            d1 = (d2 @ W2)*(1-a1**2)
            dW1 = d1.T @ xb

            W1 -= lr * dW1
            b1 -= lr * d1.sum(0)
            W2 -= lr * dW2
            b2 -= lr * d2.sum(0)

        z1t = Xte @ W1.T + b1
        a1t = np.tanh(z1t)
        test_loss = float(np.mean((a1t @ W2.T + b2 - Yte)**2))
        return losses, test_loss

    # Test multiple init scales
    scales = [0.1, 0.2, H_CLAIM, 0.5, 1.0, 2.0, 3.0]
    labels = ["0.1", "0.2", f"H={H_CLAIM:.3f}", "0.5", "1.0 (Glorot)", "2.0 (He)", "3.0"]

    print(f"\n{'Init Scale':>15} | {'Loss@50':>10} | {'Loss@200':>10} | {'Test Loss':>10}")
    print("-" * 55)

    for scale, label in zip(scales, labels):
        losses, test = run_with_init(scale, label)
        l50 = losses[49] if len(losses) > 49 else float('inf')
        l200 = losses[199] if len(losses) > 199 else float('inf')

        def fmt(v):
            return f"{v:.6f}" if v < 10 else "DEAD"

        mark = " ←" if "H=" in label else ""
        print(f"{label:>15} | {fmt(l50):>10} | {fmt(l200):>10} | {fmt(test):>10}{mark}")


# ═══════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    results = test_pure_sgd()
    test_pid_vs_sgd()
    test_init()
