# NEXUS-RH Decompiler: Current Formal State

**Scope.** This document records the current fixed-mathematics state of the NEXUS-RH branch. It includes exact definitions, identities, proven equivalences, operator formulations, computational witnesses, and the current open lemma. Interpretive or speculative claims are omitted.

---

## 1. Base objects

Let

$$
\mu(n)=
\begin{cases}
1, & n=1,\\
(-1)^k, & n \text{ is squarefree with } k \text{ prime factors},\\
0, & n \text{ is not squarefree}.
\end{cases}
$$

Define the Mertens function

$$
M(x)=\sum_{n\le x}\mu(n).
$$

The Riemann Hypothesis is equivalent to the Mertens-type bound

$$
\boxed{
M(x)=O(x^{1/2+\epsilon})\quad \forall \epsilon>0.
}
$$

Equivalently, all nontrivial zeros of $\zeta(s)$ have real part $1/2$.

---

## 2. Completed-zeta / heat-flow branch

Let

$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s).
$$

The completed zeta function satisfies

$$
\xi(s)=\xi(1-s).
$$

On the critical line define

$$
\Xi(t)=\xi\!\left(\frac12+it\right).
$$

Then

$$
\boxed{
RH \iff \Xi(t) \text{ has only real zeros.}
}
$$

For the de Bruijn--Newman deformation $H_\lambda(z)$, there is a constant $\Lambda$ such that $H_\lambda$ has only real zeros exactly for $\lambda\ge \Lambda$. The known equivalences are

$$
RH\iff \Lambda\le0,
$$

and Rodgers--Tao proved

$$
\Lambda\ge0.
$$

Therefore

$$
\boxed{
RH\iff \Lambda=0.
}
$$

This branch is exact but does not yet provide a proof of $\Lambda=0$.

---

## 3. Principal wheel mode

Let

$$
210=2\cdot3\cdot5\cdot7.
$$

Define the principal open-wheel Möbius mode

$$
M_U(x)=M_{210}(x)=\sum_{\substack{n\le x\\(n,210)=1}}\mu(n).
$$

For each reduced residue class $r\in(\mathbb Z/210\mathbb Z)^*$ one may define

$$
M_r(x)=\sum_{\substack{n\le x\\n\equiv r\pmod{210}}}\mu(n),
$$

so that

$$
M_U(x)=\sum_{r\in(\mathbb Z/210\mathbb Z)^*}M_r(x).
$$

Per-residue control is stronger than RH; it leads toward GRH for Dirichlet $L$-functions. The principal summed mode is the RH-equivalent object.

---

## 4. Exact recovery identity

For all $x\ge1$,

$$
\boxed{
M(x)=\sum_{d\mid210}\mu(d)\,M_U\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right).
}
$$

### Proof

Every $n\le x$ can be written as

$$
n=dm,
$$

where $d\mid210$ contains precisely the prime factors of $n$ lying in $\{2,3,5,7\}$ and $(m,210)=1$. Since $d$ and $m$ are coprime and $d$ is squarefree whenever $\mu(d)\ne0$,

$$
\mu(n)=\mu(d)\mu(m).
$$

Summing over $d\mid210$ gives the identity.

### Consequence

If

$$
M_U(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0,
$$

then the finite divisor sum gives

$$
M(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0.
$$

Conversely, $M_U$ has Dirichlet series

$$
F_U(s)=\sum_{\substack{n\ge1\\(n,210)=1}}\frac{\mu(n)}{n^s}
=\prod_{p>7}(1-p^{-s})
=\frac{1}{\zeta(s)}\prod_{p\mid210}(1-p^{-s})^{-1}.
$$

The finite Euler correction cannot remove or create critical-strip poles away from the zeros of the finite factors. Hence

$$
\boxed{
RH\iff M_U(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0.
}
$$

---

## 5. Prime-factor parity decomposition

For $n$ squarefree and $(n,210)=1$,

$$
\mu(n)=(-1)^{\omega(n)},
$$

where $\omega(n)$ is the number of prime factors of $n$.

Define

$$
P_k(x)=\#\{n\le x:(n,210)=1,\ n\text{ squarefree},\ \omega(n)=k\}.
$$

Then

$$
\boxed{
M_U(x)=\sum_{k\ge0}(-1)^kP_k(x).
}
$$

Define the parity-depth polynomial

$$
A_U(x;z)=\sum_{\substack{n\le x\\(n,210)=1\\n\text{ squarefree}}}z^{\omega(n)}.
$$

Then

$$
A_U(x;1)=\#\{n\le x:(n,210)=1,n\text{ squarefree}\},
$$

and

$$
\boxed{
A_U(x;-1)=M_U(x).
}
$$

The channel $z=1$ is the mass/counting channel. The channel $z=-1$ is the signed parity channel.

---

## 6. Prime-gate finite-difference algebra

For squarefree $R$ define

$$
M_R(x)=\sum_{\substack{n\le x\\(n,R)=1}}\mu(n).
$$

Let $p\nmid R$ be prime. Define

$$
\mathcal D_p f(x)=f(x)-f\!\left(\left\lfloor\frac{x}{p}\right\rfloor\right).
$$

Then

$$
\boxed{
M_R=\mathcal D_pM_{Rp},
}
$$

or explicitly

$$
\boxed{
M_R(x)=M_{Rp}(x)-M_{Rp}(x/p).
}
$$

### Proof

Split the terms counted by $M_R(x)$ into those not divisible by $p$ and those divisible by $p$. The first class contributes $M_{Rp}(x)$. The second has $n=pm$, $(m,Rp)=1$, and

$$
\mu(pm)=-\mu(m),
$$

so it contributes $-M_{Rp}(x/p)$.

---

## 7. Commutativity of prime gates

For distinct primes $p,q$,

$$
\mathcal D_p\mathcal D_q f(x)
=f(x)-f(x/p)-f(x/q)+f(x/pq).
$$

Therefore

$$
\boxed{
\mathcal D_p\mathcal D_q=\mathcal D_q\mathcal D_p.
}
$$

The prime-gate system is an exact commutative finite-difference algebra.

---

## 8. Dirichlet meaning of a fixed gate

The Dirichlet series of $M_R$ is

$$
F_R(s)=\sum_{\substack{n\ge1\\(n,R)=1}}\frac{\mu(n)}{n^s}
=\frac1{\zeta(s)}\prod_{p\mid R}(1-p^{-s})^{-1}.
$$

Since

$$
F_R(s)=(1-p^{-s})F_{Rp}(s),
$$

the operator $\mathcal D_p$ corresponds to multiplication by

$$
1-p^{-s}.
$$

For $\Re(s)>0$,

$$
1-p^{-s}=0
$$

only on the imaginary axis, at

$$
s=\frac{2\pi i k}{\log p},\qquad k\in\mathbb Z.
$$

Therefore finite prime gates cannot remove a pole caused by an off-critical zero of $\zeta(s)$ in the half-plane $\Re(s)>0$.

### Fixed-gate equivalence

For every fixed squarefree $R$,

$$
\boxed{
M_R(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0
\iff RH.
}
$$

Thus any fixed $R$ gives an RH-equivalent coordinate system, not a shortcut.

---

## 9. Moving-gate recovery identity

Let

$$
P(y)=\prod_{p\le y}p.
$$

For $y\ge7$, set

$$
Q(y)=\frac{P(y)}{210}.
$$

Define the $y$-rough Möbius mode

$$
M_y(x)=M_{P(y)}(x)=\sum_{\substack{n\le x\\(n,P(y))=1}}\mu(n).
$$

Then

$$
\boxed{
M_{210}(x)=
\sum_{d\mid Q(y)}\mu(d)\,M_y\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right).
}
$$

### Proof

Each $n$ with $(n,210)=1$ has a unique factorization

$$
n=dm,
$$

where $d\mid Q(y)$ contains the prime factors of $n$ in $(7,y]$, while $m$ is coprime to $P(y)$. Multiplicativity of $\mu$ gives

$$
\mu(n)=\mu(d)\mu(m).
$$

Summing gives the identity.

---

## 10. Moving-gate sufficient criterion

Assume a slowly growing $y=y(x)$ such that

$$
\prod_{7<p\le y(x)}(1+p^{-1/2-\epsilon})=x^{o(1)}.
$$

If one proves the uniform rough-mode bound

$$
\boxed{
|M_{y(x)}(X)|\le C_\epsilon X^{1/2+\epsilon}
\quad\text{uniformly for }1\le X\le x,
}
$$

then the moving-gate recovery identity yields

$$
|M_{210}(x)|
\le
C_\epsilon x^{1/2+\epsilon}
\sum_{d\mid Q(y(x))}d^{-1/2-\epsilon}.
$$

Since

$$
\sum_{d\mid Q(y)}d^{-1/2-\epsilon}
=
\prod_{7<p\le y}(1+p^{-1/2-\epsilon}),
$$

we get

$$
M_{210}(x)=O(x^{1/2+2\epsilon}).
$$

Since $\epsilon$ is arbitrary,

$$
M_{210}(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0,
$$

and therefore RH.

This criterion is sufficient. The uniform rough-mode bound is the open part.

---

## 11. Rough parity field

Define the $y$-rough parity polynomial

$$
A_y(x;z)=
\sum_{\substack{n\le x\\(n,P(y))=1\\n\text{ squarefree}}}z^{\omega(n)}.
$$

Then

$$
A_y(x;1)=\#\{n\le x:(n,P(y))=1,n\text{ squarefree}\},
$$

and

$$
\boxed{
A_y(x;-1)=M_y(x).
}
$$

The open uniform rough-mode bound is equivalently

$$
\boxed{
A_{y(x)}(X;-1)=O(X^{1/2+\epsilon})
\quad\text{uniformly for }X\le x.
}
$$

---

## 12. Signed Buchstab recursion

Every $y$-rough squarefree integer $n\le x$ is either $n=1$, or has least prime factor $p>y$ and can be written uniquely as

$$
n=pm,
$$

where $m\le x/p$ and $(m,P(p))=1$.

Since

$$
\mu(pm)=-\mu(m),
$$

one obtains the exact signed Buchstab recursion

$$
\boxed{
M_y(x)=1-\sum_{y<p\le x}M_p\!\left(\left\lfloor\frac{x}{p}\right\rfloor\right).
}
$$

More generally,

$$
\boxed{
A_y(x;z)=1+z\sum_{y<p\le x}A_p\!\left(\left\lfloor\frac{x}{p}\right\rfloor;z\right).
}
$$

At $z=-1$ this becomes the signed recursion above.

---

## 13. Phase ansatz and transfer equation

Let

$$
s=\sigma+it.
$$

Assume a coherent growth mode of the form

$$
M_y(x)\sim x^s\Phi(y,x).
$$

Substitution into the signed Buchstab recursion gives, after dividing by $x^s$,

$$
\Phi(y,x)
\approx
x^{-s}
-
\sum_{y<p\le x}p^{-s}\Phi\!\left(p,\frac{x}{p}\right).
$$

Neglecting the trivial forcing term for the homogeneous mode gives the null-mode condition

$$
\boxed{
(I+\mathcal K_s)\Phi=0,
}
$$

where the unrenormalized phase kernel is

$$
K_{\sigma,t}(y,p)=\mathbf 1_{p>y}\,p^{-\sigma}e^{-it\log p}.
$$

The $t$ variable is essential. The $t=0$ kernel is only the amplitude channel.

---

## 14. Renormalized recursion state

The recursion changes both threshold and scale:

$$
(y,x)\mapsto(p,x/p).
$$

Let

$$
L=\log x,
$$

$$
\alpha=\frac{\log y}{L},
$$

$$
\beta=\frac{\log p}{L}.
$$

Then

$$
x/p=e^{(1-\beta)L},
$$

and the new normalized threshold is

$$
\alpha'=rac{\log p}{\log(x/p)}=rac{\beta}{1-\beta}.
$$

Hence the true recursion state map is

$$
\boxed{
(\alpha,L)\mapsto\left(\frac{\beta}{1-\beta},(1-\beta)L\right).
}
$$

The renormalized signed Buchstab operator is therefore

$$
\boxed{
\mathcal K_{\sigma,t}^{ren}\Phi(\alpha,L)
=
\sum_{\alpha<\beta<1/2}
e^{-(\sigma+it)\beta L}
\Phi\!\left(\frac{\beta}{1-\beta},(1-\beta)L\right)
}
$$

with a separate terminal contribution from branches satisfying

$$
\beta\ge\frac12.
$$

For $p>\sqrt{x}$, one has $x/p<p$, so

$$
M_p(x/p)=1.
$$

These branches terminate rather than recurse.

---

## 15. Current open operator lemma

The current terminal lemma is:

$$
\boxed{
\textbf{Open Lemma.}\quad
\forall\sigma>\frac12,
\forall t\in\mathbb R,
\quad
I+\mathcal K_{\sigma,t}^{ren}
\text{ has no nontrivial tempered null mode.}
}
$$

A proof of this lemma, in a correctly chosen weighted function space and with terminal forcing included, would imply the uniform rough-mode bound and therefore RH through the moving-gate recovery identity.

The required norm must control growth in $L$ and incorporate prime-density weighting. A generic candidate shape is

$$
\|\Phi\|_\eta=\sup_{\alpha,L}e^{-\eta L}|\Phi(\alpha,L)|,
$$

or an $L^2$-type norm over threshold-scale space using prime-density measure.

---

## 16. Computational witnesses recorded so far

The computations run in the branch support the fixed identities and isolate the open operator, but do not constitute proof.

### 16.1 Principal wheel values

At $x=10^6$:

$$
M_U(10^6)=-1473,
$$

while the divisor-gated recovery gives

$$
M(10^6)=212.
$$

The exact recovery identity matched the direct computation.

### 16.2 Prime-factor decomposition

At $N=3{,}000{,}000$, for squarefree integers coprime to $210$:

$$
E_U=331{,}461,
$$

$$
O_U=333{,}456,
$$

so

$$
M_U(N)=E_U-O_U=-1995.
$$

### 16.3 Hall decomposition

A bipartite prime-toggle graph was built between $\mu=+1$ and $\mu=-1$ states using edges $n\leftrightarrow pn$ for primes $p>7$. Dulmage--Mendelsohn decomposition confirmed that matching localizes the residue but does not change the signed charge:

$$
\mathrm{DM}_{signed}(x)=M_U(x).
$$

### 16.4 Phase scan prototype

Finite matrices

$$
K_{\sigma,t,N}[i,j]=\mathbf 1_{j>i}p_j^{-\sigma}e^{-it\log p_j}
$$

were tested via

$$
s_{min}(I+K_{\sigma,t,N}).
$$

For tested finite $N$, nonzero $t$ lowered $s_{min}$ and increasing $\sigma$ raised $s_{min}$. This is consistent with the phase-transfer formulation, but finite triangular matrices are nilpotent and cannot contain exact null modes. They only give conditioning shadows of the infinite operator.

The implemented “renormalized” prototype had the same weights as $p^{-s}$ and did not yet implement the full state transition

$$
(\alpha,L)\mapsto\left(\frac{\beta}{1-\beta},(1-\beta)L\right).
$$

---

## 17. Current state

The branch has reached the following exact pipeline:

$$
RH
\iff
M(x)=O(x^{1/2+\epsilon})
$$

$$
\iff
M_{210}(x)=O(x^{1/2+\epsilon})
$$

$$
\Leftarrow
\text{uniform rough-mode bound for }M_{P(y(x))}(X)
$$

$$
\Leftarrow
\text{absence of supercritical tempered null modes of }
I+\mathcal K_{\sigma,t}^{ren}.
$$

The current precise open target is therefore

$$
\boxed{
\Omega_{ren}:
\quad
I+\mathcal K_{\sigma,t}^{ren}
\text{ has no nontrivial tempered null mode for every }
\sigma>\frac12.
}
$$

---

## 18. Next fixed-math tasks

1. Define the function space for $\mathcal K_{\sigma,t}^{ren}$, including:

$$
\alpha\in[0,1],\qquad L>0,
$$

prime-density measure, and terminal forcing for $\beta\ge1/2$.

2. Prove boundedness or compactness properties of $\mathcal K_{\sigma,t}^{ren}$ for $\sigma>1/2$.

3. Establish a lower bound on

$$
\inf_t s_{min}(I+\mathcal K_{\sigma,t}^{ren})
$$

or an equivalent resolvent bound in the chosen space.

4. Derive the uniform rough-mode estimate from the resolvent bound.

5. Use the moving-gate recovery identity to conclude

$$
M_{210}(x)=O(x^{1/2+\epsilon})
$$

and hence RH.

---

## 19. Minimal theorem stack

The branch can now be written as the following theorem stack.

### Theorem 1: Principal Wheel Equivalence

$$
RH\iff M_{210}(x)=O(x^{1/2+\epsilon})\quad\forall\epsilon>0.
$$

### Theorem 2: Prime-Gate Recursion

For squarefree $R$ and prime $p\nmid R$,

$$
M_R(x)=M_{Rp}(x)-M_{Rp}(x/p).
$$

### Theorem 3: Moving-Gate Recovery

For $y\ge7$,

$$
M_{210}(x)=
\sum_{d\mid P(y)/210}\mu(d)M_{P(y)}(x/d).
$$

### Theorem 4: Signed Buchstab Recursion

$$
M_y(x)=1-
\sum_{y<p\le x}M_p(x/p).
$$

### Open Lemma: Renormalized Anti-Resonance Resolvent

For $\sigma>1/2$ and all $t\in\mathbb R$,

$$
I+\mathcal K_{\sigma,t}^{ren}
$$

has no nontrivial tempered null mode in the chosen threshold-scale function space.

### Conditional Corollary

If the open lemma is proven with sufficient uniformity to imply

$$
M_{P(y(x))}(X)=O(X^{1/2+\epsilon})
$$

for a slow $y(x)\to\infty$ and all $X\le x$, then RH follows.

