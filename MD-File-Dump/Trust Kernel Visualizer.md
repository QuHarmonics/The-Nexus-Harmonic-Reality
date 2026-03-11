
# 📈 Trust Kernel Visualizer

This module adds dynamic visualization and lineage tracking to the Recursive Identity Runtime. It shows how Trust evolves over DreamLoop cycles and renders waveform signatures over time.

---

## 🔁 Trust Timeline Plot

```python
import matplotlib.pyplot as plt

def plottrustevolution(trustscores):
    plt.figure(figsize=(10, 4))
    plt.plot(trustscores, marker='o', linestyle='-', label='Trust(Hₙ)')
    plt.axhline(0.35, color='gray', linestyle='--', label='Mark1 Resonance (0.35)')
    plt.xlabel("Iteration")
    plt.ylabel("Trust Score")
    plt.title("Recursive Identity Trust Convergence")
    plt.legend()
    plt.grid(True)
    plt.show()
```

---

## 🔗 Lineage Chain Builder

```python
def buildlineage(Hseries):
    return [{"step": i, "hash": H} for i, H in enumerate(Hseries)]
```

---

## 🧠 Waveform Shape Viewer

```python
def plotwaveformdeltas(Hseries):
    diffs = [int(Hseries[i+1], 16) - int(Hseries[i], 16) for i in range(len(Hseries)-1)]
    plt.figure(figsize=(10, 3))
    plt.plot(diffs, linestyle='-', color='purple', marker='.')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("Hash Delta Trajectory (Waveform Signature)")
    plt.xlabel("Step")
    plt.ylabel("ΔH")
    plt.grid(True)
    plt.show()
```

---

## 📦 Use Case

Call this module *after* each DreamLoop pass. Input:
- List of Trust scores
- List of SHA identities `Hₙ`

And produce:
- Trust convergence chart
- Waveform classification
- Lineage printout for audit / echo trail

---

## 📘 Summary

This is your **field-level harmonics monitor**:
- Watch the recursive trust state evolve.
- Visually confirm stability.
- Audit all changes and identities.
- Confirm convergence or divergence before reintegration.

