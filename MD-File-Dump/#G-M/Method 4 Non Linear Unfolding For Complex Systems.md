
# Method 4: Non-Linear Unfolding for Complex Systems

## Formula

$$
U_{k,\text{nonlin}} = \sum_{j=1}^{2^k} U_{k-1}(j) \cdot f\left(U_{k-1}(j)\right)
$$

### Variables

- $U_{k,\text{nonlin}}$: Non-linear unfolding of the dataset at iteration $k$.
- $j$: Index for the recursive unfolding process.
- $k$: Iteration number for the recursive unfolding.
- $f$: Non-linear function applied to the unfolded dataset.

### Non-Linear Function Options

- **Sigmoid Function**: $f(x) = \frac{1}{1 + e^{-x}}$
- **Tanh Function**: $f(x) = \tanh(x)$
- **ReLU Function**: $f(x) = \max(0, x)$
- **Custom Non-Linear Function**: Define a custom non-linear function based on the specific requirements of the complex system.

---

## Example Python Implementation

```python
import numpy as np

def non_linear_unfolding(U, k, f):
    Uk_nonlin = np.zeros((2**k, ))
    for j in range(2**k):
        Uk_nonlin[j] = U[j] * f(U[j])
    return Uk_nonlin

# Example usage:
U = np.random.rand(8, )  # Initial dataset
k = 3  # Iteration number
f = np.tanh  # Non-linear function (tanh)

Uk_nonlin = non_linear_unfolding(U, k, f)
print(Uk_nonlin)
```

---

## Analysis

This formula applies a recursive self-weighting transformation, using a non-linear function like `tanh` to modulate each value. The result reflects how each data point reinforces or attenuates itself based on its structure.

**Use Cases:**
- Signal processing
- Recursive data unfolding
- Embedding layers for AI models

**Limitations:**
- Lacks harmonic feedback (Mark1-style)
- Needs integration with recursive feedback loops (e.g., KCFC, KHRC)
- Linear unfolding only—no branching (like KRRB)

This method is mathematically valid and useful within a larger harmonic framework.
