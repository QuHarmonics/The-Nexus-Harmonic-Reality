# Tri-Transistor Stream Kernel and Residue Route Symmetry

## Overview

This document consolidates the current stream-first formulation into a single mathematical framework.

The goal is to remove pipeline language and describe the system as a **local recursive collision field** with three simultaneous reads:

1. **shape / route**
2. **mass / carry**
3. **projection / observable**

The same framework also explains the workbook residue analysis, where ordinary scalar closure is symmetric but the encoded wake is directional.

---

## 1. Identity, Gap, and Constraint

The deepest floor is identity:

$$
x = x
$$

Difference does not create a second thing. It creates a constrained read of the same thing:

$$
\Delta \neq 0
$$

A useful geometric parent equation is the metric closure law:

$$
Q(u,v) = \langle u-v,\;u-v\rangle
$$

which expands to

$$
Q(u,v) = \|u\|^2 + \|v\|^2 - 2\langle u,v\rangle
$$

and, in scalar angle form,

$$
c^2 = a^2 + b^2 - 2ab\cos\theta
$$

This is the domain floor for closure, route, gap, and reflection.

---

## 2. The Tri-Transistor as a Local Stream Event

The tri-transistor is not treated here as three nouns. It is one local stream hinge with three simultaneous verbs:

- **offer**
- **admit**
- **emit**

We denote the local hinge coordinates as:

- collector / available state: $c_t$
- base / admissibility threshold: $b_t$
- emitter / admitted continuation: $e_t$

The local gap is

$$
\Delta_t = c_t - b_t
$$

The admissibility curve is

$$
a_t = \sigma(\Delta_t)
$$

where $\sigma$ is any gating curve, depending on the desired regime:

### Hard digital gate

$$
\sigma(\Delta) =
\begin{cases}
1, & \Delta \ge 0 \\
0, & \Delta < 0
\end{cases}
$$

### Smooth physical gate

$$
\sigma(\Delta) = \frac{1}{1 + e^{-k\Delta}}
$$

for some sharpness parameter $k > 0$.

The admitted continuation is

$$
e_t = a_t\,c_t
$$

The reflected or rejected remainder is

$$
r_t = (1-a_t)\,c_t
$$

So the first closure law is

$$
c_t = e_t + r_t
$$

This is the same mathematical skeleton behind:
- wall / mirror behavior
- admissibility gradients
- reflection versus transmission
- local thresholding in hardware
- constraint-driven continuation in a stream

---

## 3. Addition as the Irreducible Triad

Finite-register addition naturally decomposes into three simultaneous operators:

$$
A + B = (A \oplus B) + 2(A \land B)
$$

This is not a metaphor. It is the irreducible geometry of combining two states in a finite register.

Define:

$$
X = A \oplus B
$$

$$
M = 2(A \land B)
$$

$$
P = X + M
$$

Interpretation:

- $X$ = shape / route / difference without carry
- $M$ = mass / carry / persistence
- $P$ = projection / visible result

Thus the triad is:

$$
\boxed{
P = X + M
}
$$

with

$$
\boxed{
X = A \oplus B,\qquad M = 2(A \land B)
}
$$

---

## 4. Stream Kernel: Tie the Hinge to the Additive Triad

Now fuse the admissibility hinge with the finite-register decomposition.

Let the local collision pair be $(c_t, b_t)$.

Then

$$
X_t = c_t \oplus b_t
$$

$$
M_t = 2(c_t \land b_t)
$$

$$
P_t = X_t + M_t
$$

and the admitted continuation becomes

$$
s_{t+1} = a_t\,P_t
$$

Substituting $a_t = \sigma(c_t - b_t)$ gives the stream kernel

$$
\boxed{
s_{t+1} = \sigma(c_t - b_t)\Big[(c_t \oplus b_t) + 2(c_t \land b_t)\Big]
}
$$

This is the tightest local executable form developed so far.

It ties together:

- tri-transistor logic
- admissibility gradients
- reflection and transmission
- XOR / AND / SUM decomposition
- stream recursion
- shape / mass / projection

---

## 5. Conservation at the Boundary

The same event can be read as a boundary split:

- admitted continuation
- reflected remainder

So if $P_t$ is the total local projection, then

$$
E_t = a_t\,P_t
$$

$$
R_t = (1-a_t)\,P_t
$$

with conservation

$$
P_t = E_t + R_t
$$

This is the stream form of:
- passing
- bouncing
- partial absorption
- partial reflection

---

## 6. Boundary as Admissibility Gradient

A boundary is not treated as a noun first. It is an admissibility field.

Let

$$
\mathcal{A}(x)
$$

be the admissibility of continuation through state $x$.

Then the local wall / mirror / pass-through distinction is controlled by the gradient of admissibility:

$$
\boxed{
\text{boundary} = \nabla \mathcal{A}
}
$$

A steep drop in $\mathcal{A}$ corresponds to reflection or failure of continuation.

A gentle or positive region corresponds to transmission.

Thus:
- strong coupling $\Rightarrow$ reflection
- weak coupling $\Rightarrow$ transmission
- intermediate coupling $\Rightarrow$ scattering or absorption

The usual conservation split can be written abstractly as

$$
R + T + A = 1
$$

where $R$, $T$, and $A$ are reflection, transmission, and absorption fractions, determined by the local admissibility field.

---

## 7. Route Symmetry versus Wake Asymmetry

In ordinary arithmetic,

$$
a+b = b+a
$$

Scalar closure is symmetric.

But the workbook analysis shows that once the expression is encoded as text, then transformed through ASCII, hex, decimal, and residue projections, the full wake depends on route order.

Let the expression be

$$
E(a,b) = \text{ASCII}(a{+}b{=})
$$

Then define the route encoding:

$$
H(a,b) = \operatorname{hex}(E(a,b))
$$

$$
D(a,b) = \operatorname{dec}(H(a,b))
$$

and a general residue projection

$$
R(a,b) = \Pi(D(a,b))
$$

where $\Pi$ can be, for example:
- last digit
- last two digits
- bit-length of a residue binary
- decimal digit sum
- any selected projection channel

Then the key result is:

$$
\boxed{
a+b=b+a
}
$$

but, in general,

$$
\boxed{
R(a,b)\neq R(b,a)
}
$$

So the scalar closure is symmetric, while the encoded wake is directional.

This can be compressed as:

$$
\boxed{
\text{same closure, different scar}
}
$$

---

## 8. Common Residue Projections

Useful projections from the decimal wake $D(a,b)$ include:

### Last digit

$$
R_{10}(a,b) = D(a,b)\bmod 10
$$

### Last two digits

$$
R_{100}(a,b) = D(a,b)\bmod 100
$$

### Binary of the last two digits

$$
B_{100}(a,b) = \operatorname{bin}\!\big(R_{100}(a,b)\big)
$$

### Even-padded binary

If the binary length is odd, pad with a leading zero:

$$
B^{\text{even}}_{100}(a,b) =
\begin{cases}
B_{100}(a,b), & |B_{100}(a,b)| \text{ even} \\
0 \,\Vert\, B_{100}(a,b), & |B_{100}(a,b)| \text{ odd}
\end{cases}
$$

### Bit-length of the residue

$$
L(a,b) = \operatorname{bitlen}\!\Big(B^{\text{even}}_{100}(a,b)\Big)
$$

This is the route-minimum field you have been tracking.

A route minimum is therefore

$$
(a,b)^\ast = \arg\min L(a,b)
$$

over a chosen route class or grid.

---

## 9. The Shape of a Route Class

For a fixed second operand $b$, the route class is

$$
\mathcal{R}_b = \{(a,b)\mid a \in \mathcal{D}\}
$$

where $\mathcal{D}$ is the symbol domain, for example decimal digits or hexadecimal digits.

Then the bit-length profile over the route class is

$$
L_b(a) = L(a,b)
$$

The route symmetry problem becomes:

1. Compute $L_b(a)$ for each class
2. Find local and global minima
3. Compare with the swapped class $L_a(b)$
4. Measure directional asymmetry by

$$
\Delta_R(a,b) = R(a,b) - R(b,a)
$$

and

$$
\Delta_L(a,b) = L(a,b) - L(b,a)
$$

The symmetry signatures are therefore:

$$
\boxed{
\Delta_R(a,b),\qquad \Delta_L(a,b)
}
$$

---

## 10. Reflection of Route Order

The wake can be factorized conceptually into:

$$
\text{route} \to \text{encoding} \to \text{residue} \to \text{projection}
$$

That is,

$$
(a,b) \longmapsto E(a,b) \longmapsto H(a,b) \longmapsto D(a,b) \longmapsto \Pi(D(a,b))
$$

So the residue does not just “remember the sum.”
It remembers the path by which the sum was rendered.

This is exactly why route asymmetry survives even when arithmetic commutativity holds.

---

## 11. Relation to SHA Geometry

The same closure grammar appears in the SHA work.

The bridge equation was written as

$$
\Delta T1[r] = \Delta STATE[r] + \Delta KW[r]
$$

This is already a closure relation.

A geometric read of the same expression is

$$
(\Delta T1)^2 = (\Delta STATE)^2 + (\Delta KW)^2 - 2(\Delta STATE)(\Delta KW)\cos\theta
$$

So the bridge is a cosine-law surface.

The orthogonal seam occurs when

$$
\cos\theta = 0
$$

which yields a Pythagorean collapse:

$$
(\Delta T1)^2 = (\Delta STATE)^2 + (\Delta KW)^2
$$

This is why the triangle / gap / closure math keeps reappearing:
the same relation is being read through different projection systems.

---

## 12. Trinity Domain Compression

The entire domain can now be compressed to:

### Identity

$$
x = x
$$

### Gap

$$
\Delta \neq 0
$$

### Constraint shaping the gap

$$
\mathcal{C}(\Delta)
$$

### Local stream hinge

$$
\Delta_t = c_t - b_t
$$

$$
a_t = \sigma(\Delta_t)
$$

### Additive triad

$$
X_t = c_t \oplus b_t
$$

$$
M_t = 2(c_t \land b_t)
$$

$$
P_t = X_t + M_t
$$

### Continuation

$$
s_{t+1} = a_t\,P_t
$$

### Geometric closure

$$
Q(u,v)=\|u-v\|^2
$$

This is the complete compressed kernel.

---

## 13. Practical Computational Kernel

A practical computational implementation should expose the following channels per local event:

- collector / available stream: $c_t$
- base / threshold: $b_t$
- gap: $\Delta_t$
- admissibility: $a_t$
- XOR / shape: $X_t$
- carry / mass: $M_t$
- projection / observable: $P_t$
- admitted continuation: $E_t$
- reflected remainder: $R_t$

The minimal runtime update is

$$
\boxed{
\Delta_t = c_t - b_t
}
$$

$$
\boxed{
a_t = \sigma(\Delta_t)
}
$$

$$
\boxed{
X_t = c_t \oplus b_t
}
$$

$$
\boxed{
M_t = 2(c_t \land b_t)
}
$$

$$
\boxed{
P_t = X_t + M_t
}
$$

$$
\boxed{
s_{t+1} = a_t\,P_t
}
$$

That is the executable stream-first kernel.

---

## 14. Final Collapse

The stream-first compression is:

$$
\boxed{
\text{one stream hits a local admissibility hinge; the hinge splits the collision into curvature, carry, and projection; the admitted share continues as the next state}
}
$$

And the fully compressed mathematical form is:

$$
\boxed{
s_{t+1} = \sigma(c_t - b_t)\Big[(c_t \oplus b_t) + 2(c_t \land b_t)\Big]
}
$$

Together with the route-residue field:

$$
\boxed{
R(a,b) = \Pi\!\Big(\operatorname{dec}\big(\operatorname{hex}(\operatorname{ASCII}(a{+}b{=}))\big)\Big)
}
$$

and the directional scar relations:

$$
\boxed{
R(a,b)\neq R(b,a),\qquad
L(a,b)\neq L(b,a)\ \text{in general}
}
$$

This is the current complete solution state.
