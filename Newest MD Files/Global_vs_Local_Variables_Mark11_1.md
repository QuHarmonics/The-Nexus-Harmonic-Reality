# Global vs Local Variables on Hidden Rails
## Mark 11.1 — Rail Geometry, Carrier Persistence, and the Washout / Survivor Split

**Dean A. Kulik**  
**QuHarmonics Research Group**  
**ORCID: 0009-0003-3128-8828**  
**NEXUS Phase 1289+ / Mark11 Continuation**

---

## Abstract

This document clarifies the distinction between **global** and **local** variables in the shape-channel program and uses the targeted persistence diagnostic to show why the two must be separated.

The central point is simple:

$$
\boxed{
\text{global washout does not erase local carrier structure}
}
$$

and

$$
\boxed{
\text{a dramatic local crossing does not imply a global phase change.}
}
$$

The rail geometry remains the hard floor:

$$
H \equiv r + \frac{k}{2} \pmod W,
\qquad
\Delta H \equiv 0 \pmod W.
$$

But once the rail floor is fixed, the observable bias must be decomposed into two scales:

1. **Global variables**, which summarize the entire field or the whole collection of \(k\)-families.
2. **Local variables**, which belong to one specific rail, subtype family, or neighboring rail packet.

This distinction becomes decisive at higher sieve depth. Through \(10^8\), the global mean bias remains positive but decays, suggesting aggregate washout. Yet the targeted persistence diagnostic shows that the family \(k=24\) carries a real long-lived asymmetry and crosses zero only near

$$
X_{\text{cross}} \approx 1.987\times 10^8.
$$

This is not an inconsistency. It is the expected behavior of a field whose aggregate is washing out while specific carriers remain dynamically real.

The purpose of this document is to formalize that distinction, provide the formulas, and summarize the current solve-state cleanly.

---

## 1. Why This Distinction Matters

Much of the confusion in the shape-channel program came from mixing quantities that describe the **whole field** with quantities that describe a **single carrier**.

When these are confused, two true statements look contradictory:

- the field appears to be washing out,
- a particular \(k\)-family appears to remain strongly structured.

The correct resolution is that these are statements about **different variables**.

A global average may decay while a local channel remains persistent.

Likewise, a local rail may cross sign dramatically while the global mean stays positive.

So the first necessary formal separation is:

$$
\boxed{
\text{global variable} = \text{field-level summary}
}
$$

$$
\boxed{
\text{local variable} = \text{rail- or family-level state}
}
$$

---

## 2. The Closed Rail Floor

The rail geometry remains the strongest closed part of the program.

For a prime pair \((p,p+k)\) at wheel depth \(W\), with subtype residue \(r\in S_W(k)\), define the midpoint

$$
H = p + \frac{k}{2}.
$$

Then the shape channel of the subtype is

$$
\boxed{
H \equiv r + \frac{k}{2} \pmod W.
}
$$

If \(H_j\) and \(H_{j+1}\) are consecutive midpoint centers in the same subtype, then

$$
\Delta H = H_{j+1}-H_j \equiv 0 \pmod W.
$$

This follows immediately because

$$
\Delta H
=
\left(p_{j+1}+\frac{k}{2}\right)
-
\left(p_j+\frac{k}{2}\right)
=
p_{j+1}-p_j,
$$

and within a fixed subtype

$$
p_{j+1}\equiv p_j\equiv r\pmod W.
$$

So

$$
\boxed{
\Delta H \equiv 0 \pmod W.
}
$$

These equations define the **local rail**. They do not, by themselves, determine the observed wobble or bias amplitude. They define the exact geometry on which the wobble rides.

---

## 3. Global Variables

Global variables summarize the behavior of the entire set of tested gap families.

### 3.1 Global mean bias

If \(z_X(k)\) is the standardized bias for gap family \(k\) at sieve depth \(X\), then the global mean is

$$
\boxed{
\bar z(X)=\frac{1}{N_k}\sum_k z_X(k),
}
$$

where the sum runs over the tested even gaps.

This quantity tells us how the whole field leans on average.

It does **not** tell us whether any individual \(k\)-family is special.

### 3.2 Global sign counts

Define

$$
N_+(X)=\#\{k:z_X(k)>0\},
\qquad
N_-(X)=\#\{k:z_X(k)<0\}.
$$

These describe the global sign balance of the tested families.

### 3.3 Global pair count

Let

$$
N_{\mathrm{pairs}}(X)=\sum_k \bigl(n_A(X;k)+n_B(X;k)\bigr).
$$

This is the total count of observed prime-pair events across the tested range.

### 3.4 Example trajectory

The aggregate trajectory measured so far is

$$
\bar z(3\times 10^6)\approx 0.237,
$$

$$
\bar z(10^7)\approx 0.301,
$$

$$
\bar z(3\times 10^7)\approx 0.282,
$$

$$
\bar z(10^8)\approx 0.163.
$$

This says the **global** field remains positive but is decaying.

That is a global statement only.

---

## 4. Local Variables

Local variables belong to a specific rail, family, subtype packet, or neighboring cluster.

### 4.1 Per-gap standardized bias

For a fixed gap \(k\), define

$$
\boxed{
z_X(k)=\frac{n_A(X;k)-n_B(X;k)}{\sqrt{n_A(X;k)+n_B(X;k)}}.
}
$$

This is the main local observable.

It tells us how one specific family leans at sieve depth \(X\).

### 4.2 Support pressure

For each gap family \(k\), define the odd-prime support pressure

$$
\boxed{
\Lambda(k)=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right).
}
$$

This is local in \(k\)-space.

It measures the support-dependent Hardy–Littlewood kick for that specific gap family.

Define the support-change detector

$$
\boxed{
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
}
$$

This tells us whether that local family sits on a cold rail or a hot hinge in the support channel.

### 4.3 Frame-local coordinate

For subtype frame \(F_\tau\),

$$
\boxed{
H_\tau(p)=\left(p+\frac{k}{2}\right)\bmod W.
}
$$

This is local to the chosen frame and carrier.

### 4.4 Neighbor curvature

For a fixed horizon \(t\), the local curvature across neighboring gap families is

$$
\boxed{
\Delta_k z_t = z_t(k+6)-2z_t(k)+z_t(k-6).
}
$$

This is a local neighborhood variable in \(k\)-space.

It measures how bent the nearby carrier packet is.

---

## 5. Why Global and Local Can Disagree

This is the core conceptual point.

A global field can wash out while a local family remains strong.

Likewise, a local family can cross zero while the global mean remains positive.

These are not contradictions because they belong to different levels.

The correct statements are:

$$
\boxed{
\text{global washout does not erase local carrier structure}
}
$$

and

$$
\boxed{
\text{a local crossing does not force a global inversion.}
}
$$

This is exactly what the targeted persistence diagnostic shows.

---

## 6. The Targeted Persistence Diagnostic

To separate genuine survivors from the aggregate washout, three local carriers were chosen:

- \(k=24\): strongest sustained positive signal,
- \(k=66\): negative comparator,
- \(k=84\): sign-crossing wobble control.

The decision rule was:

- if \(k=24\) remains large and separated while the controls decay, then \(k=24\) is a real carrier;
- if all three collapse uniformly toward zero, then the whole field is washing out without local survivors.

### 6.1 Persistence table

The measured \(z(k)\) values are:

| \(X\) | \(z(24)\) | \(z(66)\) | \(z(84)\) |
|---|---:|---:|---:|
| \(3\times 10^6\) | \(+0.9736\) | \(-0.9051\) | \(+0.1700\) |
| \(10^7\) | \(+1.4304\) | \(-0.7615\) | \(+0.4051\) |
| \(3\times 10^7\) | \(+1.8041\) | \(-0.4859\) | \(+0.0975\) |
| \(10^8\) | \(+1.0473\) | \(-0.6178\) | \(-0.4136\) |
| \(3\times 10^8\) | \(-0.5353\) | \(-0.5110\) | \(+0.4722\) |
| \(10^9\) | \(-0.8818\) | \(-0.1051\) | \(+0.5850\) |

### 6.2 Fine scan for \(k=24\)

A fine scan located the zero crossing of \(k=24\) near

$$
X_{\text{cross}}\approx 1.987\times 10^8.
$$

More precisely, the last positive values occur before roughly \(1.988\times 10^8\), and the sign is negative immediately after.

---

## 7. Interpretation of the Diagnostic

### 7.1 \(k=24\) is a real local carrier

The family \(k=24\) remains positive for multiple checkpoints over two decades of sieve depth, peaks near \(z\approx 1.80\), and only later crosses negative.

That is too coherent to dismiss as random residue.

So:

$$
\boxed{
k=24 \text{ is a real long-lived local carrier.}
}
$$

### 7.2 \(k=66\) is a stable negative control

The family \(k=66\) remains negative throughout while its magnitude slowly shrinks.

This is consistent with a decaying negative channel.

### 7.3 \(k=84\) is a wobble control

The family \(k=84\) flips sign and continues oscillating. It does not show the same persistent carrier structure as \(k=24\).

### 7.4 Global washout still holds

Even though \(k=24\) is real locally, the aggregate mean still decays. So the field-level story remains washout, but the local carrier story remains persistence plus later inversion.

That is the main point of the distinction.

---

## 8. Global vs Local Formulas

The clean split can be written as follows.

### 8.1 Global level

Global observables:

$$
\bar z(X)=\frac{1}{N_k}\sum_k z_X(k),
$$

$$
N_+(X)=\#\{k:z_X(k)>0\},
\qquad
N_-(X)=\#\{k:z_X(k)<0\},
$$

$$
N_{\mathrm{pairs}}(X)=\sum_k \bigl(n_A(X;k)+n_B(X;k)\bigr).
$$

These describe the whole field.

### 8.2 Local level

Local observables:

$$
z_X(k)=\frac{n_A(X;k)-n_B(X;k)}{\sqrt{n_A(X;k)+n_B(X;k)}},
$$

$$
\Lambda(k)=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right),
$$

$$
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6),
$$

$$
H_\tau(p)=\left(p+\frac{k}{2}\right)\bmod W,
$$

$$
\Delta_k z_t=z_t(k+6)-2z_t(k)+z_t(k-6).
$$

These describe one rail, one family, or one local neighborhood.

---

## 9. Relation to the Mark-0 Wobble Operator

The global/local split also clarifies the Mark-0 update operator.

For each local carrier \(k\), define the state

$$
S_t(k)=\bigl(z_t(k),v_t(k)\bigr),
$$

where \(z_t(k)\) is local lean and \(v_t(k)\) is local sway velocity.

Then the local update is

$$
v_{t+1}(k)
=
\rho\,v_t(k)
+
\beta\,\Delta\Lambda(k)\,G\!\bigl(z_t(k)\bigr)
+
\gamma\,\bigl[z_t(k+6)-2z_t(k)+z_t(k-6)\bigr]
+
C_t(k),
$$

$$
z_{t+1}(k)=z_t(k)+v_{t+1}(k).
$$

Here:

- \(\rho\) = memory / inertia,
- \(\beta\Delta\Lambda(k)\) = local support kick,
- \(\gamma\Delta_k z_t\) = local curvature,
- \(C_t(k)\) = unresolved local cross-talk.

This is a **local** rule. It predicts the movie on one rail family or one neighborhood.

The global quantities such as \(\bar z(X)\) are summaries **after** many local channels are aggregated.

---

## 10. What Is Solved and What Is Still Open

### Solved enough to trust

The rail floor is still the hardest result:

$$
H \equiv r+\frac{k}{2}\pmod W,
\qquad
\Delta H \equiv 0\pmod W.
$$

The global/local distinction is also now clear:

$$
\boxed{
\text{global washout and local persistence can coexist.}
}
$$

The \(k=24\) targeted diagnostic is the first confirmed example of a long-lived local carrier with a late real inversion.

### Still open

The following remain open:

1. whether \(k=24\) is unique or one of several late carriers,
2. whether the post-crossing negative phase of \(k=24\) damps, grows, or oscillates,
3. the exact analytic growth law for the GPM shape parameter,
4. the final higher-depth asymptotic form of the flip / wobble law.

---

## 11. The Next Useful Runs

The next runs that matter most are:

### 11.1 Extend the targeted diagnostic
Track

$$
k=24,\quad k=66,\quad k=84
$$

at

$$
3\times 10^9,\quad 10^{10}.
$$

This will tell us whether the \(k=24\) post-crossing negative phase is stable, oscillatory, or decaying.

### 11.2 Full sweep at \(10^9\)
Run

$$
k=6,12,\dots,126
$$

at \(10^9\) to determine whether \(k=24\) remains unique or whether other families exhibit similarly late carrier structure.

These are the next real local boundaries.

---

## 12. Conclusion

The project now has a clean two-scale reading.

At the **global** level, the field is washing out:

$$
\bar z(X)\downarrow \text{ toward }0.
$$

At the **local** level, at least one carrier remains dynamically real:

$$
k=24
$$

persisted strongly positive for a long interval and crossed only near

$$
X_{\text{cross}}\approx 1.987\times 10^8.
$$

So the correct final statement is:

$$
\boxed{
\text{the field washes out globally while specific rails remain alive locally.}
}
$$

That is the complete resolution of the global-versus-local confusion.

---

## Appendix A. Core Equations

### A.1 Midpoint rail
$$
H \equiv r+\frac{k}{2}\pmod W.
$$

### A.2 Step Theorem
$$
\Delta H \equiv 0 \pmod W.
$$

### A.3 Global mean bias
$$
\bar z(X)=\frac{1}{N_k}\sum_k z_X(k).
$$

### A.4 Per-gap standardized bias
$$
z_X(k)=\frac{n_A(X;k)-n_B(X;k)}{\sqrt{n_A(X;k)+n_B(X;k)}}.
$$

### A.5 Support pressure
$$
\Lambda(k)=
\sum_{\substack{q\mid k\\ q>3}}
\log\!\left(\frac{q-1}{q-2}\right).
$$

### A.6 Support-change detector
$$
\Delta\Lambda(k)=\Lambda(k)-\Lambda(k-6).
$$

### A.7 Local curvature in \(k\)-space
$$
\Delta_k z_t=z_t(k+6)-2z_t(k)+z_t(k-6).
$$

### A.8 Local state vector
$$
S_t(k)=\bigl(z_t(k),v_t(k)\bigr).
$$

### A.9 Mark-0 local update
$$
v_{t+1}(k)
=
\rho\,v_t(k)
+
\beta\,\Delta\Lambda(k)\,G\!\bigl(z_t(k)\bigr)
+
\gamma\,\bigl[z_t(k+6)-2z_t(k)+z_t(k-6)\bigr]
+
C_t(k),
$$

$$
z_{t+1}(k)=z_t(k)+v_{t+1}(k).
$$

### A.10 Crossing location for \(k=24\)
$$
X_{\text{cross}}\approx 1.987\times 10^8.
$$
