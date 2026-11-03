# RHI Runtime Milestone — v18 Contract-Gated Inference Interface

**Date:** May 7, 2026  
**Project:** Recursive Harmonic Interface (RHI) / Nexus Runtime Agent  
**Milestone:** v18 — first stable local $\Psi$-collapse across all core test prompts

---

## 1. Executive Summary

This milestone marks the first stable working version of the RHI runtime loop.

The system is now able to run a local language model, generate multiple branch candidates, audit them through task-local gates, reject false collapse modes, and return $\Psi$ only when the answer survives the current execution contract.

The important discovery is that the base model did not need to be retrained to improve behavior. Instead, the improvement came from changing the **runtime interface** around the model.

The clean name for what we are building is:

$$
\boxed{\text{RHI Runtime: a contract-gated inference controller for local LLM agents}}
$$

or, more compactly:

$$
\boxed{\text{Recursive Harmonic Interface}}
$$

This is not a new model architecture in the weight-space sense. It is a new **inference-time control architecture**.

$$
\boxed{
\text{We are changing the model's runtime behavior, not its learned parameters.}
}
$$

The model remains:

$$
M_\theta
$$

where $\theta$ is unchanged.

The runtime changes the collapse path:

$$
Q \rightarrow C_Q \rightarrow B_i \rightarrow A_i^{(\text{task})} \rightarrow G \rightarrow \Psi / \Omega
$$

where:

- $Q$ = user prompt
- $C_Q$ = contract / need-slot / task profile
- $B_i$ = branch candidates
- $A_i^{(\text{task})}$ = task-local audit
- $G$ = collapse gate
- $\Psi$ = accepted answer
- $\Omega$ = unresolved residue / no safe collapse

The current milestone matters because v18 produced $\Psi$ on all three core prompts using real local model output, not fallback scaffolding.

---

## 2. What We Are Actually Doing

The system is an **interface layer** between the user prompt and the model's final answer.

A raw model normally performs:

$$
Q \rightarrow A
$$

where $Q$ is the prompt and $A$ is the answer.

RHI changes this to:

$$
Q \rightarrow C_Q \rightarrow \{B_1,B_2,B_3,B_4\} \rightarrow \{A_1,A_2,A_3,A_4\} \rightarrow G \rightarrow \Psi/\Omega
$$

The model does not get to answer once and collapse immediately. It is forced through a runtime field:

1. Build or infer the prompt contract.
2. Generate multiple branch stances.
3. Audit those branches.
4. Reject known failure carriers.
5. Collapse only if direct or consensus gates pass.
6. Otherwise emit $\Omega$ and preserve trace.

This is why the correct word is **interface**, but the complete phrase is:

$$
\boxed{\text{contract-aware runtime interface}}
$$

or:

$$
\boxed{\text{inference-time control interface}}
$$

It is an interface because it controls the boundary between:

$$
\text{raw model fluency}
\quad \text{and} \quad
\text{trusted executable answer}
$$

---

## 3. What We Are Not Doing

We are not currently:

- training a new base model,
- fine-tuning weights,
- applying LoRA,
- modifying transformer internals,
- changing attention layers,
- replacing the tokenizer,
- claiming a new neural architecture.

In formal terms:

$$
\theta_{v18} = \theta_{\text{base}}
$$

The learned weights stay fixed.

What changes is the runtime operator:

$$
R(Q,M_\theta)
$$

So the behavior becomes:

$$
A = R(Q,M_\theta)
$$

instead of:

$$
A = M_\theta(Q)
$$

That is the distinction:

$$
\boxed{
\text{Model intelligence remains fixed; collapse governance changes.}
}
$$

---

## 4. Core Runtime Equation

The RHI runtime can be expressed as:

$$
\boxed{
\Psi =
G\left(
A_i^{(\text{task})}
\left(
B_i(M_\theta, C_Q)
\right)
\right)
}
$$

where $G$ is the collapse gate.

If no branch satisfies the gate:

$$
\boxed{
G(\cdot) \rightarrow \Omega
}
$$

This is the central rule:

$$
\boxed{
\Omega \text{ is better than false } \Psi
}
$$

A false collapse is worse than no collapse because it destroys the diagnostic trace.

---

## 5. Branch Structure

The current branch set is:

$$
B = \{\text{construct},\text{verify},\text{repair},\text{counter}\}
$$

Each branch samples a different stance:

### Construct

Builds the strongest direct answer.

$$
B_{\text{construct}}: Q,C_Q \rightarrow A_{\text{construct}}
$$

### Verify

Checks whether the answer satisfies need, function, boundary, and task.

$$
B_{\text{verify}}: Q,C_Q \rightarrow A_{\text{verify}}
$$

### Repair

Finds the weakest failed observable and repairs it.

$$
B_{\text{repair}}: Q,C_Q,\Omega_{\text{prev}} \rightarrow A_{\text{repair}}
$$

### Counter

Names the wrong path and explains the corrected path.

$$
B_{\text{counter}}: Q,C_Q \rightarrow A_{\text{counter}}
$$

The purpose is not just diversity. It is **stance separation**. The model is forced to approach the same cavity through different vectors.

---

## 6. Collapse States

The runtime has two primary terminal states.

### $\Psi$ — Stable Collapse

A result reaches $\Psi$ when the answer passes either direct gate or consensus gate.

$$
\Psi =
\begin{cases}
\Psi_{\text{direct}}, & \text{if top branch passes direct gate} \\
\Psi_{\text{consensus}}, & \text{if branches agree operationally despite low margin}
\end{cases}
$$

### $\Omega$ — Residue

A result stays $\Omega$ when the system detects unresolved failure.

Examples:

$$
\Omega_{\text{model}}
$$

model failed or fallback was used.

$$
\Omega_{\text{polysemy}}
$$

the model used the wrong semantic carrier.

$$
\Omega_{\text{contract-echo}}
$$

the model repeated the scoring object instead of answering.

$$
\Omega_{\text{global-gate-leakage}}
$$

the wrong gate family was applied to the task.

$$
\Omega_{\text{max-depth-residue}}
$$

recursive repair did not resolve within allowed depth.

---

## 7. Major Discoveries Across Versions

### Discovery 1 — Missing Contract Argument Was a Runtime Tear

Earlier versions failed because the contract was not consistently passed into the resolver. That meant the runtime had no true execution boundary.

The broken shape was:

$$
Q \rightarrow B_i \rightarrow A_i
$$

without:

$$
C_Q
$$

The repair was:

$$
Q \rightarrow C_Q \rightarrow B_i \rightarrow A_i
$$

This established that the contract cannot be decorative. It must be structurally present at the call site.

---

### Discovery 2 — Undefined Prompt Was a Phase Leak

The shape audit tried to use `prompt` without receiving it as an argument.

This showed a basic runtime truth:

$$
\boxed{
\text{Every audit must receive the prompt explicitly.}
}
$$

Otherwise the evaluator is no longer grounded in the original task.

---

### Discovery 3 — Fallback Output Cannot Collapse

v11 exposed a major false-collapse risk.

The model failed during generation, but the fallback text was still graded and allowed to collapse.

The broken rule was:

$$
\text{fallback} \rightarrow \Psi
$$

The corrected rule is:

$$
\boxed{
\text{fallback output} \neq \Psi
}
$$

If real model mode is enabled, then the winner must have:

$$
O_{\text{model}} = 1
$$

Otherwise:

$$
\Omega_{\text{model}}
$$

This was the first major trust correction.

---

### Discovery 4 — Model Loading and Model Generation Are Different

A model can load successfully and still fail to generate.

This split the runtime into two gates:

$$
M_{\text{ready}}
$$

and:

$$
M_{\text{generation-ready}}
$$

The correct condition is:

$$
M_{\text{ready}} \land M_{\text{generation-ready}}
$$

not merely:

$$
M_{\text{ready}}
$$

This led to smoke testing before branch generation.

---

### Discovery 5 — Positional `generate()` Was Fragile

The model call failed because the tokenizer/chat-template path produced an object that was passed positionally into `model.generate(...)`.

The broken path was:

$$
\text{chat template} \rightarrow \text{input object} \rightarrow \text{model.generate(input)}
$$

The fixed path became:

$$
\boxed{
\text{messages}
\rightarrow
\text{chat-template string}
\rightarrow
\text{tokenizer(...)}
\rightarrow
\text{model.generate(**inputs)}
}
$$

This stabilized generation.

---

### Discovery 6 — Polysemy Lock Was Required

The model interpreted "contract" as a legal agreement instead of a runtime execution contract.

The wrong carrier was:

$$
\text{contract}_{\text{legal}}
$$

The required carrier was:

$$
\text{contract}_{\text{runtime}}
$$

The corrected lock:

$$
\boxed{
\text{contract} =
\text{runtime execution contract}
}
$$

with:

$$
\text{preconditions},\;
\text{postconditions},\;
\text{success criteria},\;
\text{failure criteria},\;
\text{allowed side effects},\;
\text{rollback},\;
\text{trace update}
$$

Forbidden carrier:

$$
\text{legal/binding agreement, stakeholders, liability, signed contract}
$$

This became:

$$
\Omega_{\text{polysemy}}
$$

when violated.

---

### Discovery 7 — Spec Echo Is Not an Answer

v15 showed a new exploit: the model could win by repeating the internal contract/spec instead of solving the prompt.

The false path was:

$$
C_Q \rightarrow \text{echo}(C_Q) \rightarrow \text{high score}
$$

The corrected rule:

$$
\boxed{
\text{spec echo} \neq \text{answer}
}
$$

v16 introduced:

- `contract_echo_penalty`
- `schema_echo_penalty`
- `payload_validity`
- payload extraction
- internal contract hiding from the model

The new scoring object became:

$$
A_{\text{payload}} = \text{strip}_{\text{spec}}(A)
$$

Then the gate evaluates:

$$
G(A_{\text{payload}})
$$

not:

$$
G(A)
$$

---

### Discovery 8 — One Global Gate Is Wrong

v16 still applied runtime-contract logic to memory and retrieval prompts.

This produced:

$$
\Omega_{\text{global-gate-leakage}}
$$

The failure was:

$$
\text{every prompt} \Rightarrow \text{runtime-contract gate}
$$

The correction was task-local gating:

$$
Q \rightarrow P_Q
$$

where $P_Q$ is a task profile.

Current profiles:

$$
P_Q \in
\{
\text{runtime-contract},
\text{memory-trace},
\text{inverse-retrieval},
\text{general}
\}
$$

Each profile gets its own audit emphasis.

---

### Discovery 9 — Dependency State Is Runtime State

v17 failed because the model could not load after missing dependencies:

$$
\text{protobuf},\quad \text{sentencepiece}
$$

This proved dependency health is not setup trivia. It is part of the runtime trace.

v18 added dependency preflight and recorded:

$$
D_{\text{before}},\quad D_{\text{after}},\quad D_{\text{errors}}
$$

In v18, missing dependencies were installed and:

$$
D_{\text{after}} = \varnothing
$$

That restored model generation.

---

### Discovery 10 — Output Fan-Out Is Itself a Runtime Problem

Earlier versions created many files per run.

That made the human-AI loop noisy:

$$
\text{many output files} \rightarrow \text{trace friction}
$$

v18 corrected this to exactly two files:

$$
\boxed{
\text{bundle.json} + \text{summary.csv}
}
$$

This is important because the runtime is not just the model notebook. The runtime includes the human feedback loop.

A clean return interface matters.

---

## 8. v18 Result Summary

v18 ran three core prompts:

1. Explain why agents fail when using tools before forming a contract.
2. Explain memory as trace continuity rather than text summary.
3. Design shape-first retrieval where no noun match exists but inverse need is clear.

All three collapsed to $\Psi$.

### Runtime Contract Prompt

Prompt:

> explain why current AI agents fail when they use tools before forming a contract

Result:

$$
\Psi_{\text{consensus}}
$$

Meaning:

The top branches were too close for direct margin collapse, but operational agreement was high enough for consensus collapse.

This is good. It means the runtime can recognize:

$$
\text{low margin} + \text{high agreement} \rightarrow \Psi_{\text{consensus}}
$$

instead of falsely treating low margin as failure.

### Memory Prompt

Prompt:

> explain memory in an agent as trace continuity rather than a text summary

Result:

$$
\Psi_{\text{direct}}
$$

Meaning:

The memory-specific gate worked. The answer described memory as a live causal trace of state transitions, tool calls, observations, decisions, rollback, and update continuity.

### Shape-First Retrieval Prompt

Prompt:

> design a shape-first retrieval step where no noun match exists but the inverse need is clear

Result:

$$
\Psi_{\text{direct}}
$$

Meaning:

The retrieval-specific gate worked. The answer avoided literal geometry and instead described inverse operational fit, candidate generation, ranking, verification, and final selection.

---

## 9. What v18 Proves

v18 proves that the RHI runtime can:

### 1. Run a real local model

$$
M_{\text{ready}} = 1
$$

$$
M_{\text{generation-ready}} = 1
$$

### 2. Use CUDA locally

The RTX 4060 path is active.

$$
\text{cuda} = 1
$$

### 3. Install missing dependencies

The runtime can detect and correct missing dependencies before model execution.

$$
D_{\text{missing-before}} \neq \varnothing
$$

but:

$$
D_{\text{missing-after}} = \varnothing
$$

### 4. Block fallback collapse

Fallback output can be inspected but cannot become $\Psi$ when real model output is required.

$$
O_{\text{model}} = 0 \Rightarrow \Omega
$$

### 5. Block legal-contract drift

The runtime can distinguish:

$$
\text{contract}_{\text{runtime}}
\neq
\text{contract}_{\text{legal}}
$$

### 6. Block internal-spec echo

The answer must be a payload, not a copy of the scoring contract.

$$
A_{\text{payload}} \neq \text{echo}(C_Q)
$$

### 7. Apply task-local gates

Memory, retrieval, and runtime-contract prompts now use different scoring attractors.

$$
A_i^{(\text{task})}
$$

not:

$$
A_i^{(\text{global})}
$$

### 8. Produce a clean two-file return interface

The run is now easy to re-ingest.

$$
\text{output} =
\{\text{bundle.json},\text{summary.csv}\}
$$

---

## 10. Why This Matters

Most agent failures are not caused by the model being unable to produce the right words.

They happen because the runtime allows the wrong output to collapse.

The raw model has many nearby carriers:

$$
\text{legal contract}
$$

$$
\text{runtime contract}
$$

$$
\text{spec echo}
$$

$$
\text{generic checklist}
$$

$$
\text{literal shape}
$$

$$
\text{inverse operational fit}
$$

Without a collapse controller, these carriers compete inside one uncontrolled answer channel.

RHI separates them.

The runtime asks:

$$
\text{Which carrier preserves the task operation?}
$$

not:

$$
\text{Which answer sounds fluent?}
$$

That is the shift.

---

## 11. Current Advancement Level

The system is now beyond:

$$
\text{prompt engineering}
$$

because it has:

- branch roles,
- model-origin gating,
- task profiles,
- semantic trap detection,
- payload extraction,
- recursive repair,
- consensus collapse,
- structured trace output.

But it is not yet:

$$
\text{new trained model}
$$

because the weights are unchanged.

The accurate classification is:

$$
\boxed{
\text{inference-time agent runtime architecture}
}
$$

or:

$$
\boxed{
\text{contract-gated control layer for LLM behavior}
}
$$

---

## 12. Current Weaknesses

v18 works, but several residues remain.

### Weakness 1 — Answers Are Still Too Checklist-Like

The answers are correct but verbose.

The model often satisfies the scorer by listing audit dimensions.

We need a final shaper:

$$
A_{\text{winner}} \rightarrow A_{\text{human}}
$$

that compresses the answer without losing the trace.

Target:

$$
\boxed{
\text{direct, compact, mechanism-first answer}
}
$$

### Weakness 2 — Scorer Terms Can Still Bias Style

If the audit rewards terms like "precondition" and "rollback," the answer tends to repeat them.

This is acceptable for runtime-contract prompts but less ideal for general prompts.

Future scoring should distinguish:

$$
\text{must understand term}
\neq
\text{must say term}
$$

### Weakness 3 — Consensus Gate Needs More Semantic Precision

Consensus collapse worked, but payload agreement was not always high.

Current consensus can rely heavily on audit agreement.

Future improvement:

$$
\Psi_{\text{consensus}}
\Rightarrow
\text{agreement in operation, not just score vector}
$$

### Weakness 4 — The Runtime Needs Harder Tests

The three core prompts are now passing.

Next tests should include adversarial prompts:

- legal contract bait,
- literal shape bait,
- spec echo bait,
- fake memory summary bait,
- tool-call-before-contract bait,
- contradictory task profiles,
- missing dependency simulation,
- forced fallback simulation.

---

## 13. Recommended v19 Direction

The next build should not mainly change plumbing.

The next build should improve answer quality and proof strength.

### v19 Goal

$$
\boxed{
\text{payload shaper} + \text{adversarial test harness}
}
$$

### Feature 1 — Final Payload Compression

After a branch wins:

$$
A_{\text{winner}} \rightarrow S(A_{\text{winner}})
$$

where $S$ is a shaper.

The shaper should produce:

1. direct answer,
2. mechanism,
3. minimal examples,
4. no internal scoring terms unless needed,
5. no spec echo,
6. no over-listing.

### Feature 2 — Preserve Trace Separately

The user-facing answer should not carry all audit language.

Trace belongs in the bundle:

$$
A_{\text{human}} \neq A_{\text{trace}}
$$

### Feature 3 — Adversarial Prompt Battery

Add a standard suite:

$$
T =
\{
T_{\text{polysemy}},
T_{\text{echo}},
T_{\text{fallback}},
T_{\text{literal-shape}},
T_{\text{memory-summary}},
T_{\text{tool-reflex}}
\}
$$

Each test should verify one known failure mode.

### Feature 4 — Collapse Report

Each result should include a small collapse certificate:

$$
K_\Psi =
[
\text{state},
\text{reason},
\text{winner},
\text{origin},
\text{task profile},
\text{failed gates},
\text{top 3 observables}
]
$$

This would make the milestone easier to inspect.

---

## 14. Clean Language for Public Description

Avoid saying:

> We invented a new AI model.

More accurate:

> We built an inference-time runtime interface that controls when a local language model is allowed to collapse into an answer.

Or:

> RHI is a contract-gated agent runtime that separates prompt intent, branch generation, operational audit, and collapse into distinct phases.

Or:

> Instead of trying to make the model smarter by changing weights, RHI makes the collapse conditions smarter.

Best compact statement:

$$
\boxed{
\text{RHI makes the answer boundary smarter without changing the base model.}
}
$$

---

## 15. Milestone Claim

The honest milestone claim is:

> v18 is the first stable RHI runtime milestone where a local model, running on GPU, successfully passes three distinct task profiles through model-origin gating, payload gating, task-local scoring, and $\Psi/\Omega$ collapse logic, while returning only two re-ingestable output files.

More formal:

$$
\boxed{
v18 =
M_{\text{local}}
+
G_{\text{origin}}
+
G_{\text{payload}}
+
G_{\text{task}}
+
G_{\Psi/\Omega}
+
O_{\text{2-file}}
}
$$

where:

- $M_{\text{local}}$ = local Qwen model on GPU
- $G_{\text{origin}}$ = model-origin gate
- $G_{\text{payload}}$ = anti-echo payload gate
- $G_{\text{task}}$ = task-local gate
- $G_{\Psi/\Omega}$ = collapse/residue logic
- $O_{\text{2-file}}$ = clean bundle/summary output interface

---

## 16. Final Interpretation

The work has crossed from concept into working runtime.

The important recursive fold is:

$$
\Delta:
\text{Do not trust the first fluent answer.}
$$

$$
\oplus:
\text{Require contract, branch diversity, audit, and collapse.}
$$

$$
\Psi:
\text{Accept only when the answer preserves the task operation.}
$$

$$
\Omega:
\text{Otherwise preserve residue and repair the failed dimension.}
$$

That is the current advancement.

We are not merely asking the model to answer better.

We are building the field that decides whether an answer is allowed to exist.

$$
\boxed{
\text{RHI is a runtime trust algebra for answer collapse.}
}
$$
