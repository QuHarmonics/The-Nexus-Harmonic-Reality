"""
BOUNDARY ZOOM — Fine sweep around the death wall
"""
import numpy as np
from collections import deque

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

H = np.pi / 9

traj = generate_lorenz(3000)
mn, mx = traj.min(0), traj.max(0)
tn = 2*(traj - mn)/(mx - mn + 1e-8) - 1
W = 5
X = np.array([tn[i:i+W].flatten() for i in range(len(tn)-W-1)])
Y = tn[W+1:, 0:1]
n_tr = 1500
Xtr, Ytr = X[:n_tr], Y[:n_tr]
Xte, Yte = X[n_tr:n_tr+500], Y[n_tr:n_tr+500]
in_dim, hid, bs, epochs = W*3, 32, 64, 500

# Fine sweep: 0.30 to 0.40 in steps of 0.002
lrs = np.arange(0.300, 0.405, 0.002)

print("=" * 60)
print(f"BOUNDARY ZOOM: lr 0.300-0.400 (step 0.002)")
print(f"H = π/9 = {H:.6f}")
print("=" * 60)

# Run 5 seeds per lr for statistical robustness
print(f"\n{'LR':>6} | {'Alive/5':>7} | {'Mean Test':>10} | {'Note'}")
print("-" * 50)

for lr in lrs:
    alive_count = 0
    test_losses = []

    for seed in range(5):
        np.random.seed(42 + seed)
        W1 = np.random.randn(hid, in_dim) * np.sqrt(2.0/in_dim)
        b1 = np.zeros(hid)
        W2 = np.random.randn(1, hid) * np.sqrt(2.0/hid)
        b2 = np.zeros(1)
        alive = True

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
                alive = False
                break

            d2 = 2*(pred-yb)/bs
            dW2 = d2.T @ a1
            d1 = (d2 @ W2)*(1-a1**2)
            dW1 = d1.T @ xb

            W1 -= lr * dW1
            b1 -= lr * d1.sum(0)
            W2 -= lr * dW2
            b2 -= lr * d2.sum(0)

        if alive:
            alive_count += 1
            z1t = Xte @ W1.T + b1
            a1t = np.tanh(z1t)
            tl = float(np.mean((a1t @ W2.T + b2 - Yte)**2))
            test_losses.append(tl)

    mean_test = np.mean(test_losses) if test_losses else float('inf')
    note = ""
    if abs(lr - H) < 0.002:
        note = "← H = π/9"
    elif alive_count == 0:
        note = "DEAD"
    elif alive_count < 3:
        note = "FRAGILE"

    test_str = f"{mean_test:.6f}" if mean_test < 10 else "---"
    print(f"{lr:>6.3f} | {alive_count:>5}/5 | {test_str:>10} | {note}")

print(f"\nH = π/9 = {H:.6f}")
print(f"The death boundary should be visible as alive→dead transition")

# Also test a few architectures to check if boundary is stable
print("\n" + "=" * 60)
print("ARCHITECTURE ROBUSTNESS: Does the boundary hold?")
print("=" * 60)

configs = [
    (16, "16 hidden"),
    (32, "32 hidden"),
    (64, "64 hidden"),
    (128, "128 hidden"),
]

test_lrs = [0.30, 0.32, 0.34, 0.35, 0.36, 0.38, 0.40]

print(f"\n{'Config':>12} | " + " | ".join(f"lr={lr:.2f}" for lr in test_lrs))
print("-" * (15 + len(test_lrs) * 9))

for hidden, label in configs:
    row = f"{label:>12} | "
    for lr in test_lrs:
        alive_count = 0
        for seed in range(3):
            np.random.seed(42 + seed)
            W1 = np.random.randn(hidden, in_dim) * np.sqrt(2.0/in_dim)
            b1 = np.zeros(hidden)
            W2 = np.random.randn(1, hidden) * np.sqrt(2.0/hidden)
            b2 = np.zeros(1)
            alive = True

            for ep in range(500):
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
                    alive = False
                    break

                d2 = 2*(pred-yb)/bs
                dW2 = d2.T @ a1
                d1 = (d2 @ W2)*(1-a1**2)
                dW1 = d1.T @ xb
                W1 -= lr * dW1
                b1 -= lr * d1.sum(0)
                W2 -= lr * dW2
                b2 -= lr * d2.sum(0)

            if alive:
                alive_count += 1

        status = f"{'✓' * alive_count}{'✗' * (3-alive_count)}"
        row += f" {status:>6} |"
    print(row)

print(f"\nH = π/9 = {H:.6f}")
print("If boundary is real, the ✓→✗ transition should cluster near 0.35 across architectures")
