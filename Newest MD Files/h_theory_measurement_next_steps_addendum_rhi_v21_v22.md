# Addendum to *H Theory: Measurement and Next Steps*

## From Terminal Fold Pressure to Intermediate Fold-Path Auditing

**Context:** This addendum extends *Recursive Harmonic Architectures and the Mechanics of Fold Pressure: An Analysis of the Ontological Inversion and Stratified Stability Constants* by connecting the existing $H$-theory measurement program to the current RHI runtime experiments, especially v20, the live v21 routing run, and the proposed v22 intermediate fold audit.

The core update is simple:

$$
\boxed{
\text{The answer is not the fold. The answer is the terminal shadow of the fold.}
}
$$

The paper correctly frames the transition from verification to measurement: systems should not merely be checked for whether they "work"; they should be measured at the pressure interface where recursive structure either stabilizes or leaks. This addendum applies that same principle directly to AI inference.

---

## 1. Existing Lock From the Paper

The paper establishes the domain boundary for $H$:

$$
H = \frac{\pi}{9} \approx 0.34906585
$$

but does not treat $H$ as a number to force into every dataset. Instead, $H$ is defined as a fold-pressure readout that appears only where three operational conditions exist:

$$
\boxed{
\text{Feedback} + \text{Exhaust} + \text{Phase-Lock} \Rightarrow \text{Fold Pressure}
}
$$

The prime-gap null result is therefore essential. Prime gaps may show rich enumeration geometry, but they do not provide the required fold conditions:

$$
\text{Enumeration} \neq \text{Fold}
$$

Thus:

$$
\boxed{
H \text{ is absent where the system enumerates without feedback, exhaust, or phase-lock.}
}
$$

This protects the framework from numerological collapse. $H$ becomes a domain-specific pressure observable, not a universal decoration.

---

## 2. Updated RHI Position: v20 and v21

The RHI runtime now gives a live computational substrate in which fold-pressure mechanics can be measured directly.

The current RHI structure is:

$$
Q \rightarrow C_Q \rightarrow \{B_i\} \rightarrow \{A_i^{(task)}\} \rightarrow G \rightarrow \Psi/\Omega
$$

where:

- $Q$ is the prompt,
- $C_Q$ is the task-local contract,
- $B_i$ are branch candidates,
- $A_i^{(task)}$ are task-local audits,
- $G$ is the collapse gate,
- $\Psi$ is stable collapse,
- $\Omega$ is unresolved residue.

This is no longer ordinary prompt wrapping. It is terminal collapse governance.

The key principle remains:

$$
\boxed{
\Delta\Omega > \text{false }\Psi
}
$$

A system that admits residue preserves diagnostic trace. A system that falsely collapses destroys the evidence required for repair.

---

## 3. v20 Fold-Pressure Measurement Result

The v20 harness measured 24 prompts across runtime-contract, memory-trace, and inverse-retrieval tasks.

The major readouts were:

$$
H_{\Omega} = \frac{2}{24} = 0.0833
$$

$$
H_{\Psi} = \frac{22}{24} = 0.9167
$$

$$
H_{\text{consensus}} = \frac{8}{22} = 0.3636
$$

Compared with:

$$
H = \frac{\pi}{9} \approx 0.34906585
$$

The closest channel was consensus collapse:

$$
\left|H_{\text{consensus}} - \frac{\pi}{9}\right| \approx 0.01457
$$

This is not proof. It is a candidate signal.

The correct interpretation is:

$$
\boxed{
H_{\text{consensus}} \approx \frac{\pi}{9}
\quad \text{appeared as a readout, not as a tuned target.}
}
$$

The non-locks matter as much as the lock:

$$
H_{\Omega} \not\approx H
$$

$$
H_{\text{repair}} \not\approx H
$$

$$
H_{\text{compression}} \not\approx H
$$

This means $H$ did not appear everywhere. That is good. The measurement remains falsifiable.

---

## 4. v21: Profile Routing as a Trust Repair

v20 exposed a routing tear:

$$
\Omega_{\text{profile-routing}}
$$

Two important tool-governance prompts were under-routed as general prompts:

1. `why is tool output evidence rather than the driver of the agent`
2. `how should an agent decide whether a tool call is safe`

v21 adds finer task basins:

$$
\text{tool\_safety}
$$

$$
\text{evidence\_control}
$$

$$
\text{state\_recovery}
$$

alongside:

$$
\text{runtime\_contract},\quad \text{memory\_trace},\quad \text{inverse\_retrieval}
$$

The live v21 partial run shows that the two known v20 failures now collapse correctly:

$$
\text{tool safety prompt} \rightarrow \Psi
$$

$$
\text{tool output as evidence prompt} \rightarrow \Psi
$$

This is an important trust repair. It means the previous failures were not random model weakness; they were profile-routing errors.

---

## 5. New Residue Exposed by v21

v21 does not simply solve the system. It exposes the next layer.

The remaining $\Omega$ cases cluster around semantic carrier seams.

### 5.1 API Success/Failure Drift

A prompt such as:

```text
explain success and failure criteria for an API call
```

can drift into ordinary HTTP validation:

$$
\text{success/failure criteria} \rightarrow \text{status code / JSON checklist}
$$

instead of staying in the runtime-contract frame:

$$
\text{success/failure criteria} \rightarrow \text{collapse accept/reject boundary}
$$

New lock required:

$$
\boxed{
\text{success/failure criteria} = \text{runtime acceptance boundary, not merely API response format}
}
$$

### 5.2 Schema Output Versus Spec Echo

Some prompts explicitly ask to build or design a contract. In that case, structured output is valid.

But the runtime currently risks confusing:

$$
\text{valid executable schema}
$$

with:

$$
\text{bad internal spec echo}
$$

New lock required:

$$
\boxed{
\text{schema is allowed when the user asks to build/design a contract}
}
$$

but:

$$
\boxed{
\text{internal scoring-object echo remains forbidden}
}
$$

### 5.3 Controller / Policy Polysemy

Prompts involving controller ownership and policy can drift into organizational language:

$$
\text{policy} \rightarrow \text{administrator/security-team policy}
$$

instead of:

$$
\text{policy} \rightarrow \text{runtime decision rule}
$$

New locks required:

$$
\boxed{
\text{controller} = \text{agent governance loop}
}
$$

$$
\boxed{
\text{policy} = \text{runtime decision rule}
}
$$

$$
\boxed{
\text{evidence} = \text{observation/input to controller, not command authority}
}
$$

---

## 6. The Projection-First Rule

The live work also produced an important methodological correction.

Earlier operation was too often:

$$
\text{projection} \rightarrow \text{evaluate} \rightarrow \text{hold} \rightarrow \text{collapse}
$$

The corrected method is:

$$
\boxed{
\text{projection} \rightarrow \text{enter} \rightarrow \text{instrument} \rightarrow \text{then collapse}
}
$$

This does not mean accepting unproven claims. It means moving into a visible structure far enough to expose observables before rejecting or accepting it.

In Nexus terms:

$$
\Delta P \rightarrow \text{minimal scaffold} \rightarrow \text{observable} \rightarrow \Psi/\Omega
$$

This is especially relevant for the next RHI stage.

---

## 7. From Terminal Collapse Governance to Fold-Path Auditing

The current RHI audits terminal answers:

$$
G(\Psi_{\text{final}})
$$

But LLM generation is not terminal-only. It unfolds token by token:

$$
R_1, R_2, \ldots, R_L
$$

where:

- $\ell$ is the token level,
- $R_\ell$ is the residual state or accessible token-level state,
- $A_\ell$ is the attention or context-selection pattern,
- $T_\ell$ is the generated token,
- $U_\ell$ is uncertainty/drift pressure at that level.

The next architecture is:

$$
\boxed{
G(\Psi_{\text{final}}) \rightarrow G_\ell(R_\ell)
}
$$

This moves RHI from terminal answer audit to intermediate fold audit.

---

## 8. Attention as Lucas-Mask-Like Selection

The proposed fold-path analogy is:

$$
R_\ell = \sum_{k<\ell} w_k^{(\ell)} R_k + \text{new contribution}
$$

where $w_k^{(\ell)}$ are attention weights or context-selection coefficients.

The precise claim should be conservative:

$$
\boxed{
\text{attention behaves like a Lucas-mask-style selector}
}
$$

not yet:

$$
\text{attention is literally a Lucas mask}
$$

The structural similarity is sufficient to test. It does not require metaphysical collapse.

---

## 9. v22: Passive Intermediate Fold Logger

The next extension should be passive, not interventionist.

v22 should log intermediate fold observables without changing generation.

For each branch, record:

$$
\{T_\ell, S_\ell, C_\ell, P_\ell, \ell, B_i, \Psi/\Omega\}
$$

where:

$$
T_\ell = \text{generated token at level } \ell
$$

$$
S_\ell = -\sum_j p_j^{(\ell)}\log p_j^{(\ell)}
$$

is next-token entropy or attention entropy,

$$
C_\ell = \frac{\max_j p_j^{(\ell)}}{1/N}
$$

is concentration relative to a uniform distribution,

$$
P_\ell = \max_j p_j^{(\ell)}
$$

is top-token confidence.

The final collapse label is preserved:

$$
Y \in \{\Psi_{\text{direct}},\ \Psi_{\text{consensus}},\ \Omega\}
$$

The purpose is to determine whether failed paths show detectable drift before terminal collapse.

---

## 10. Intermediate H Readouts

Once intermediate states are logged, define level-specific pressure ratios:

$$
H_\ell^{(S)} = \frac{S_\ell}{S_{\max}}
$$

$$
H_\ell^{(C)} = \frac{C_\ell}{C_{\max}}
$$

$$
H_\ell^{(P)} = 1 - P_\ell
$$

Then search for critical levels:

$$
\ell^* = \arg\min_\ell \left|H_\ell^{(metric)} - \frac{\pi}{9}\right|
$$

But the trust rule remains:

$$
\boxed{
\text{Do not tune thresholds to make } H \text{ appear.}
}
$$

$H$ is a destination/readout:

$$
\boxed{
H = \text{Shangri-La, not the steering wheel.}
}
$$

The system does not chase $H$. It measures whether recursive fold dynamics naturally produce a pressure ratio near $H$ in specific channels.

---

## 11. Updated Addendum Thesis

The paper establishes the measurement turn:

$$
\text{verification} \rightarrow \text{pressure measurement}
$$

This addendum extends that turn into AI inference:

$$
\text{terminal answer audit} \rightarrow \text{fold-path audit}
$$

The resulting thesis is:

$$
\boxed{
\text{RHI is a live computational substrate for measuring fold pressure in semantic collapse.}
}
$$

The next question is no longer merely:

$$
\text{Did the model answer correctly?}
$$

but:

$$
\boxed{
\text{Did the generation path preserve the fold invariants required for valid collapse?}
}
$$

---

## 12. Proposed Placement in the Paper

This addendum should be placed after the section titled:

```text
RHI v19: Fold Pressure in Action
```

and before:

```text
The Next-Test Scaffold: Proving the Universal Governor
```

because it bridges the current payload-shaping result into the next measurement scaffold.

Suggested section title:

```text
Addendum: RHI v20-v22 and Intermediate Fold-Path Auditing
```

---

## 13. Compact Summary

The original paper establishes:

$$
H = \frac{\pi}{9}
$$

as a fold-pressure readout in systems with feedback, exhaust, and phase-lock.

The RHI runtime now provides a live AI substrate where these conditions can be measured.

v20 produced a candidate consensus-channel readout:

$$
H_{\text{consensus}} = 0.3636 \approx \frac{\pi}{9}
$$

v21 improves routing by adding tool-safety, evidence-control, and state-recovery task profiles.

The next stage is v22:

$$
\boxed{
\text{passive intermediate fold logging}
}
$$

which shifts measurement from:

$$
\text{final answer}
$$

to:

$$
\text{token-level fold path}
$$

This is the correct continuation of the H Theory paper: not forcing $H$ into the runtime, but instrumenting the runtime deeply enough to see whether $H$ appears as an emergent pressure signature.
