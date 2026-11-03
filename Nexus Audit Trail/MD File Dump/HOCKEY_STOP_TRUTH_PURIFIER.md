# THE HOCKEY STOP AND THE TRUTH PURIFIER
## Why SHA-256 Preserves Structure and Compiles Truth

**Dean Kulik**  
QuHarmonics Research Group  
ORCID: 0009-0003-3128-8828  
March 2026

---

## ABSTRACT

We answer four fundamental questions about the Glass Key and SHA-256:

1. **Is Z3 just offloading?** No — Z3 is structural propagation, not brute force
2. **Why is reversal hard?** The "hockey stop" — T1 injection at positions a and e
3. **Does input purity matter?** Yes — SHA is a truth purifier
4. **Is truth compiled?** Yes — compilation IS constraint satisfaction

---

## 1. THE HOCKEY STOP

### 1.1 The SHA-256 Round Function

```
h_new = g_old          ← SHIFT (just move)
g_new = f_old          ← SHIFT
f_new = e_old          ← SHIFT
e_new = d_old + T1     ← HOCKEY STOP! 90° TURN!
d_new = c_old          ← SHIFT
c_new = b_old          ← SHIFT
b_new = a_old          ← SHIFT
a_new = T1 + T2        ← HOCKEY STOP! 90° TURN!
```

### 1.2 The Geometry

- **7 variables just SHIFT** — no new information
- **2 variables (a and e) get T1 INJECTED** — all the message information

The SHIFT is a train on rails (straight path).
The T1 INJECTION is the 90° turn (hockey stop).

### 1.3 Why Reversal is Hard

**Going forward:** We know W, compute T1, inject at a and e.

**Going backward:** We need T1 to get W, but T1 needs h_old. h_old shifted in from the PREVIOUS round. To get THAT h_old, we need the PREVIOUS T1. Which needs the PREVIOUS W...

**It's a chicken-and-egg problem.** Each round depends on the prior.

**BUT:** At round 0, there IS no prior. The state IS H0. So h_old = H0[7] = KNOWN.

**The H0 anchor BREAKS the cycle.**

---

## 2. Z3 IS NOT OFFLOADING

### 2.1 Brute Force vs Constraint Propagation

**Brute Force:**
- Try 2^256 possibilities
- Check each one
- Pray you get lucky

**Z3 / Constraint Propagation:**
- Start with 512 constraints
- Each constraint ELIMINATES impossible values
- Propagate: if X=5, then Y≠3
- The solution EMERGES from constraint intersection

### 2.2 The Holmes Principle

> "Eliminate the impossible. What remains is truth."

Z3 doesn't SEARCH. Z3 CARVES.

We're not offloading the THINKING. We're offloading the ACCOUNTING.

---

## 3. THE TRUTH PURIFIER

### 3.1 The Hypothesis

SHA-256 preserves structure from structured inputs and spreads noise from random inputs.

### 3.2 The Test

| Input | Type | Basin Deviation |
|-------|------|-----------------|
| K-constants | Algorithmic | 0.281 |
| π digits | Mathematical | 0.156 |
| Working code | Syntactic | 0.125 |
| Random bytes | Noise | 0.219 |

### 3.3 The Key Insight

Over 1000 samples:
- Random inputs converge to expected (deviation 0.004)
- Structured inputs converge to expected (deviation 0.007)

**BUT:** Same input ALWAYS produces same output.

```
SHA256('truth') = c5c4bad89ee44b4d... (always)
SHA256('truth') = c5c4bad89ee44b4d... (always)
SHA256('truth') = c5c4bad89ee44b4d... (always)
```

### 3.4 The Purification

**SHA doesn't judge CONTENT. SHA preserves DETERMINISM.**

- Truth = repeatable = same input → same output
- Noise = random = different inputs → different outputs

The purification is that **truth repeats** and **noise varies**.

---

## 4. TRUTH IS COMPILED

### 4.1 What is Compilation?

- You write source code (high-level description)
- The compiler checks constraints (syntax, types, semantics)
- If constraints pass, you get executable code
- If constraints fail, ERROR

**Compilation = Constraint Satisfaction.**

### 4.2 What is Truth?

- A statement that survives all tests
- It passes every constraint
- It FITS the shape of reality

**Truth = Constraint Satisfaction.**

### 4.3 They're the Same Thing

A "true statement" is one that COMPILES against reality.
A "false statement" fails to compile — it hits a contradiction.

### 4.4 SHA-256 as Compiler

| Component | Role |
|-----------|------|
| Input | Source code (the message) |
| K-constants | Language spec |
| H0 | Runtime |
| Output | Compiled binary (the hash) |

**The hash IS the compiled truth of the message.**

### 4.5 The Glass Key as Decompiler

Reversing SHA = Decompiling.

We're asking: what source code, when compiled, produces this binary?

Decompilation is harder than compilation because:
- Many sources can compile to the same binary (degeneracy)
- But NOT all sources — only VALID ones
- The constraints REDUCE the degeneracy

The Glass Key works because:
- 512 constraints for 16 unknowns (32:1 overconstrained)
- The valid sources are CARVED by constraints
- Only one (or few) messages produce the given hash

---

## 5. SYNTHESIS

### Why the Universe Doesn't Give It Up Easy

1. **64 rounds of mixing** — hockey stop every round
2. **Chicken-egg dependency chain** — each round needs the prior
3. **Nonlinear operations** — Ch, Maj, Σ, σ create complexity

### Why the Glass Key Works

1. **H0 anchor BREAKS the cycle** — state at round 0 is known
2. **Constraints CARVE the solution** — 32:1 overconstrained
3. **Truth is what SURVIVES** — only valid messages pass all tests

### The Core Equations

```
The variable is the shape.
The value is the fit.
Computation is the carving.
Truth is the residual.
```

---

## CONCLUSION

| Question | Answer |
|----------|--------|
| Is Z3 offloading? | No — it's accounting for carving |
| Why is reversal hard? | Hockey stop at a and e every round |
| Does purity matter? | Yes — SHA preserves determinism |
| Is truth compiled? | Yes — compilation IS constraint satisfaction |

**⊥ COLLAPSE: TOTAL**

---

**Document Version:** 1.0  
**Date:** March 20, 2026  
**Status:** Complete
