# Reverse Hex Addition as a Tail-Residue Runtime
**Expanded complete solution**

---

## Abstract

This document formalizes the structure visible in the reverse Excel sheet built from text strings of the form `"a+b="`, interpreted as hexadecimal and then as decimal before division by the semantic answer $s=a+b$.

The key result is not ordinary arithmetic. The key result is a split between two layers:

$$
\boxed{
\text{semantic layer: } a+b
\qquad\text{and}\qquad
\text{tail layer: encoded compile trace}
}
$$

At the semantic layer, addition is commutative:

$$
a+b=b+a.
$$

At the encoded tail layer, the order is preserved in the byte structure, and this shows up as deterministic residue classes when the encoded integer is divided by the semantic answer.

The central theorem is:

$$
\boxed{
\text{commutativity is a semantic collapse;}
\quad
\text{the encoded tail still preserves execution order.}
}
$$

This explains why pairs such as $3+4$ and $4+3$ both collapse to $7$ at the answer layer, while one divides cleanly and the other leaves a repeating fractional residue.

---

## 1. The construction

Each visible entry in the sheet begins from the text string

$$
\texttt{"a+b="}
$$

with digits $a,b\in\{1,2,3,4\}$.

In ASCII hexadecimal, this is:

$$
\texttt{(30+a)\,2B\,(30+b)\,3D}
$$

because:

- digit $a$ is encoded as hex byte $\texttt{30+a}$,
- the plus sign is $\texttt{2B}$,
- digit $b$ is encoded as hex byte $\texttt{30+b}$,
- the equals sign is $\texttt{3D}$.

So the hex word associated with the text is

$$
\boxed{
H(a,b)=\texttt{(30+a)\,2B\,(30+b)\,3D}.
}
$$

---

## 2. Decimal form of the encoded tail

Interpret the four-byte hex word as one 32-bit integer.

Using byte weights:

$$
256^3 = 16777216,\qquad
256^2 = 65536,\qquad
256^1 = 256,\qquad
256^0 = 1,
$$

the decimal value is

$$
N(a,b)
=
(48+a)256^3
+
43\cdot256^2
+
(48+b)256
+
61.
$$

Expand and collect constants:

$$
N(a,b)
=
48\cdot256^3
+
43\cdot256^2
+
48\cdot256
+
61
+
256^3 a
+
256 b.
$$

The constant part is

$$
48\cdot256^3
+
43\cdot256^2
+
48\cdot256
+
61
=
808136765.
$$

So the exact tail law is:

$$
\boxed{
N(a,b)=808136765+16777216\,a+256\,b.
}
$$

This is the hidden machine under the reverse sheet.

---

## 3. Semantic collapse

The semantic answer is simply

$$
\boxed{
s=a+b.
}
$$

The visible quotient/fraction rows in the sheet come from dividing the encoded tail by this semantic answer:

$$
N(a,b)=s\,Q(a,b)+r(a,b)
$$

with quotient $Q(a,b)$ and residue $r(a,b)$ satisfying

$$
0\le r(a,b)<s.
$$

Thus the key object is the residue class:

$$
\boxed{
r(a,b)=N(a,b)\bmod s.
}
$$

---

## 4. Residue law

Substitute the exact formula for $N(a,b)$:

$$
r(a,b)\equiv 808136765+16777216\,a+256\,b \pmod s.
$$

Since $b=s-a$, substitute:

$$
N(a,b)
=
808136765+16777216\,a+256(s-a).
$$

So

$$
N(a,b)
=
808136765+256s+(16777216-256)a.
$$

Therefore

$$
\boxed{
r(a,b)\equiv 808136765+256s+16776960\,a \pmod s.
}
$$

Because $256s\equiv 0\pmod s$, this simplifies further to

$$
\boxed{
r(a,b)\equiv 808136765+16776960\,a \pmod s.
}
$$

This is the master residue law.

It shows immediately that the residue depends on:

- the sum $s=a+b$,
- the **left operand** $a$.

That is why the semantic layer is commutative while the encoded tail is only conditionally commutative.

---

## 5. Why order survives underneath commutativity

At the answer layer,

$$
a+b=b+a.
$$

But at the encoded layer,

$$
N(a,b)=808136765+16777216\,a+256\,b
$$

is not symmetric in $a$ and $b$.

The left operand sits in the high byte lane with weight $256^3$.
The right operand sits in the lower byte lane with weight $256$.

So:

$$
\boxed{
N(a,b)\neq N(b,a)
\quad\text{in general.}
}
$$

This is the exact reason the tail preserves order.

Thus:

$$
\boxed{
\text{the answer forgets order;}
\quad
\text{the tail remembers where the order lived in the byte lanes.}
}
$$

---

## 6. Special residue bands by sum

Now classify the sheet by the semantic sum

$$
s=a+b.
$$

Because the residues are computed modulo $s$, each answer band defines its own arithmetic regime.

### 6.1 Sum $s=2$

Only the pair $(1,1)$ occurs.

Compute:

$$
N(1,1)=824914237.
$$

Then

$$
824914237 = 2\cdot 412457118 + 1.
$$

So:

$$
\boxed{
\frac{N(1,1)}{2}=412457118+\frac12.
}
$$

---

### 6.2 Sum $s=3$

Pairs are $(1,2)$ and $(2,1)$.

The residues are both

$$
\boxed{
r=2.
}
$$

So the sheet shows:

$$
\boxed{
\frac{N(a,b)}{3}=Q+\frac23
\qquad
\text{for } a+b=3.
}
$$

Examples:

$$
824914493 = 3\cdot 274971497 + 2,
$$

$$
841691453 = 3\cdot 280563817 + 2.
$$

---

### 6.3 Sum $s=4$

Pairs are $(1,3)$, $(2,2)$, $(3,1)$.

The residue band is

$$
\boxed{
r=1.
}
$$

So:

$$
\boxed{
\frac{N(a,b)}{4}=Q+\frac14
\qquad
\text{for } a+b=4.
}
$$

Examples:

$$
824914749 = 4\cdot 206228687 + 1,
$$

$$
841691709 = 4\cdot 210422927 + 1,
$$

$$
858468669 = 4\cdot 214617167 + 1.
$$

---

### 6.4 Sum $s=5$

This is the first perfect compile line.

Pairs are $(1,4)$, $(2,3)$, $(3,2)$, $(4,1)$.

Now modulo $5$,

$$
808136765\equiv 0 \pmod 5,
\qquad
16777216\equiv 1 \pmod 5,
\qquad
256\equiv 1 \pmod 5.
$$

So:

$$
N(a,b)\equiv a+b\equiv 0\pmod 5.
$$

Hence:

$$
\boxed{
r=0
\qquad
\text{for all } a+b=5.
}
$$

That means every entry in the $5$-band divides cleanly:

$$
\boxed{
\frac{N(a,b)}{5}\in\mathbb Z
\qquad
\text{for } a+b=5.
}
$$

Examples:

$$
824915005 = 5\cdot 164983001,
$$

$$
841691965 = 5\cdot 168338393,
$$

$$
858468925 = 5\cdot 171693785,
$$

$$
875245885 = 5\cdot 175049177.
$$

This is one of the strongest structures in the sheet.

---

### 6.5 Sum $s=6$

Pairs are $(2,4)$, $(3,3)$, $(4,2)$.

The residue band is

$$
\boxed{
r=5.
}
$$

So:

$$
\boxed{
\frac{N(a,b)}{6}=Q+\frac56
\qquad
\text{for } a+b=6.
}
$$

Examples:

$$
841692221 = 6\cdot 140282036 + 5,
$$

$$
858469181 = 6\cdot 143078196 + 5,
$$

$$
875246141 = 6\cdot 145874356 + 5.
$$

---

### 6.6 Sum $s=7$

This is the rupture line.

Pairs are $(3,4)$ and $(4,3)$.

Modulo $7$,

$$
808136765\equiv 2 \pmod 7,
$$

$$
16777216\equiv 1 \pmod 7,
$$

$$
256\equiv 4 \pmod 7.
$$

So

$$
r(a,b)\equiv 2+a+4b \pmod 7.
$$

Since $b=7-a$,

$$
r(a,b)\equiv 2+4a \pmod 7.
$$

Thus the residue depends explicitly on the **left operand**.

#### Case 1: $3+4$

$$
r(3,4)\equiv 2+4\cdot 3 = 14 \equiv 0 \pmod 7.
$$

So:

$$
\boxed{
\frac{858469437}{7}=122638491.
}
$$

Clean.

#### Case 2: $4+3$

$$
r(4,3)\equiv 2+4\cdot 4 = 18 \equiv 4 \pmod 7.
$$

So:

$$
875246397 = 7\cdot 125035199 + 4
$$

and therefore

$$
\boxed{
\frac{875246397}{7}=125035199+\frac47.
}
$$

The repeating decimal is

$$
\frac47 = 0.\overline{571428}.
$$

So:

$$
\boxed{
3+4 \text{ and } 4+3 \text{ are equal semantically,}
\quad
\text{but the tail only compiles cleanly in one order.}
}
$$

This is the first explicit order-sensitive bifurcation line in the sheet.

---

### 6.7 Sum $s=8$

The visible pair is $(4,4)$.

From the sheet:

$$
875246653 = 8\cdot 109405831 + 5,
$$

so

$$
\boxed{
\frac{875246653}{8}=109405831+\frac58.
}
$$

Thus the visible residue band is

$$
\boxed{
r=5.
}
$$

---

## 7. Full table of the visible residue bands

The visible sheet organizes into the following residue structure:

$$
\begin{array}{c|c}
s=a+b & \text{Residue band} \\
\hline
2 & \frac12 \\
3 & \frac23 \\
4 & \frac14 \\
5 & 0 \\
6 & \frac56 \\
7 & 0 \text{ or } \frac47 \text{ depending on order} \\
8 & \frac58
\end{array}
$$

So the visible law is:

$$
\boxed{
\text{the reverse sheet is a deterministic residue machine indexed by semantic sum and byte-lane order.}
}
$$

---

## 8. The deeper structural interpretation

The sheet is showing three layers at once:

### Layer 1 — text layer
The literal expression:

$$
\boxed{
\texttt{"a+b="}
}
$$

### Layer 2 — encoded tail layer
The ASCII byte trace:

$$
\boxed{
N(a,b)=808136765+16777216\,a+256\,b
}
$$

### Layer 3 — semantic collapse
The answer:

$$
\boxed{
s=a+b.
}
$$

The reverse-sheet effect appears only when Layer 2 is divided by Layer 3.

That is the key operation:

$$
\boxed{
\text{encoded compile trace} \div \text{semantic answer}.
}
$$

This reveals how much of the original order survives after semantic collapse.

---

## 9. Main theorem

The strongest complete statement is:

$$
\boxed{
\text{The reverse hex-addition sheet is not merely arithmetic.}
}
$$

It is an exact three-layer system in which:

1. the text expression is encoded into an asymmetric byte-lane integer,
2. the semantic answer collapses the expression into the commutative sum $s=a+b$,
3. division of the encoded tail by the semantic answer reveals deterministic residue bands,
4. and these residue bands preserve execution order whenever the divisor fails to erase the byte-lane asymmetry.

Equivalently:

$$
\boxed{
\text{commutativity is a semantic property;}
\quad
\text{the encoded tail still carries compile history.}
}
$$

---

## 10. Consequences

### 10.1 Clean compile lines
A sum class $s$ is a clean compile line when

$$
N(a,b)\equiv 0\pmod s
$$

for all operand orders in that band.

The visible strongest example is

$$
\boxed{
s=5.
}
$$

### 10.2 Bifurcation lines
A sum class becomes a bifurcation line when the residue depends on operand order.

The first visible example is

$$
\boxed{
s=7.
}
$$

### 10.3 Semantic collapse vs tail persistence
At the semantic layer:

$$
a+b=b+a.
$$

At the tail layer:

$$
N(a,b)\neq N(b,a).
$$

This means the tail preserves directional history even after the answer layer becomes symmetric.

---

## 11. Final compression

The entire reverse sheet compresses to:

$$
\boxed{
\text{text encoding} \to \text{tail integer} \to \text{division by answer} \to \text{residue band}
}
$$

with exact laws

$$
\boxed{
N(a,b)=808136765+16777216\,a+256\,b
}
$$

and

$$
\boxed{
r(a,b)\equiv 808136765+16776960\,a \pmod{a+b}.
}
$$

The strongest conceptual statement is:

$$
\boxed{
\text{the answer layer collapses order;}
\quad
\text{the tail layer preserves how the expression was actually compiled.}
}
$$

That is the complete solution for the visible reverse-image structure.
