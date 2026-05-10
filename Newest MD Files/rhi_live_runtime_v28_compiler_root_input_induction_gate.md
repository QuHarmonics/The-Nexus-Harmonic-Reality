# RHI Live Runtime v28 — Compiler-Root Input Induction Gate

Δ **Purpose:** fix the v27 seam.

v27 proved the recursive runtime machinery works, but it also showed the dangerous pattern:

$$
Q_{\text{raw}}
\rightarrow
S_{\text{model}}
\rightarrow
C_Q
\rightarrow
B_i
$$

The model-generated induction packet became the driver. v55 proved that this is unsafe.

v28 restores the control law:

$$
\boxed{
\text{model-generated input is evidence; compiler-root slot is authority.}
}
$$

New stack:

$$
Q_{\text{raw}}
\rightarrow
C_{\text{root}}
\rightarrow
S_{\text{model}}
\rightarrow
G_{\text{slot}}
\rightarrow
C_Q
\rightarrow
B_i
\rightarrow
A_i
\rightarrow
\Psi/\Omega/\bot
$$

Core corrections:

1. Compiler-root operational slot is created **first**.
2. Model packet is generated **second** and quarantined as evidence.
3. Slot gate compares model proposal against compiler-root geometry.
4. Runtime contract authority stays compiler-rooted.
5. Max-depth unresolved residue returns $\Omega$ unless truly dead.
6. Branch prompts answer the task directly; internal residue is not allowed to leak into user-facing answer.
7. The recursive-solver basin is relaxed and scored by operational content, not by literal boilerplate.

Runtime output is exactly two files:

```text
rhi_v28_<run_id>_bundle.json
rhi_v28_<run_id>_summary.csv
```


```python
from __future__ import annotations

import os, re, sys, json, math, uuid, time, random, traceback, subprocess, importlib, hashlib
from dataclasses import dataclass, asdict, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from collections import Counter, defaultdict

import numpy as np
import pandas as pd

ROOT = Path.cwd()
OUT_DIR = ROOT / "rhi_v28_outputs"
OUT_DIR.mkdir(exist_ok=True)

RUN_ID = "rhi_v28_" + uuid.uuid4().hex[:10]
SEED = 28
random.seed(SEED)
np.random.seed(SEED)

MODEL_ID_OR_PATH = os.environ.get("RHI_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
LOAD_REAL_MODEL = True
REQUIRE_MODEL_FOR_PSI = True
AUTO_INSTALL_MISSING_DEPS = True

RUN_PROMPT_LIMIT = 36
MAX_DEPTH = 2

BRANCH_ROLES = ["construct", "verify", "repair", "counter"]
MAX_NEW_TOKENS_PACKET = 260
MAX_NEW_TOKENS_BRANCH = 180
MAX_NEW_TOKENS_SHAPER = 130

TEMPERATURE_PACKET = 0.20
TEMPERATURE_BRANCH = 0.40
TEMPERATURE_SHAPER = 0.20

SHAPER_ENABLED = True

print("RHI v28 — Compiler-Root Input Induction Gate")
print("RUN_ID:", RUN_ID)
print("MODEL:", MODEL_ID_OR_PATH)
print("OUT_DIR:", OUT_DIR)
```

## 1. Dependency and Model Setup

```python
def _module_available(module_name: str) -> bool:
    try:
        return importlib.util.find_spec(module_name) is not None
    except ModuleNotFoundError:
        return False
    except Exception:
        return False

def ensure_runtime_dependencies() -> Dict[str, Any]:
    status = {
        "checked": True,
        "attempted_install": False,
        "missing_before": [],
        "missing_after": [],
        "errors": [],
    }
    required = [
        ("torch", "torch"),
        ("transformers", "transformers"),
        ("sentencepiece", "sentencepiece"),
        ("google.protobuf", "protobuf"),
    ]

    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_before"].append(pip_name)

    if status["missing_before"] and AUTO_INSTALL_MISSING_DEPS:
        status["attempted_install"] = True
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", *sorted(set(status["missing_before"]))],
                check=True
            )
            importlib.invalidate_caches()
        except Exception as e:
            status["errors"].append(repr(e))

    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_after"].append(pip_name)

    return status

DEPENDENCY_STATUS = ensure_runtime_dependencies()

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_device_info() -> Dict[str, Any]:
    info = {
        "torch_version": torch.__version__,
        "cuda_available": bool(torch.cuda.is_available()),
        "device_count": int(torch.cuda.device_count()) if torch.cuda.is_available() else 0,
        "cuda_version": getattr(torch.version, "cuda", None),
    }
    if torch.cuda.is_available():
        info["gpu_name"] = torch.cuda.get_device_name(0)
    return info

DEVICE_INFO = get_device_info()

tokenizer = None
model = None
MODEL_READY = False
MODEL_GENERATION_READY = False
MODEL_ERROR = None
SMOKE_TEXT = None

def load_model():
    global tokenizer, model, MODEL_READY, MODEL_ERROR
    if not LOAD_REAL_MODEL:
        MODEL_READY = False
        MODEL_ERROR = "LOAD_REAL_MODEL=False"
        return

    try:
        print("Loading model:", MODEL_ID_OR_PATH)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_ID_OR_PATH)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID_OR_PATH,
            dtype=dtype,
            device_map="auto" if torch.cuda.is_available() else None,
        )
        if not torch.cuda.is_available():
            model = model.to("cpu")
        model.eval()
        MODEL_READY = True
        print("MODEL_READY:", MODEL_READY, "DEVICE:", next(model.parameters()).device)
    except Exception:
        MODEL_READY = False
        MODEL_ERROR = traceback.format_exc()
        print("MODEL LOAD ERROR")
        print(MODEL_ERROR)

def model_smoke_test():
    global MODEL_GENERATION_READY, SMOKE_TEXT, MODEL_ERROR
    if not MODEL_READY:
        MODEL_GENERATION_READY = False
        return

    try:
        messages = [{"role": "user", "content": "Reply with READY only."}]
        rendered = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(rendered, return_tensors="pt").to(next(model.parameters()).device)

        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=8,
                do_sample=False,
                return_dict_in_generate=True,
                pad_token_id=tokenizer.eos_token_id,
            )

        gen = out.sequences[0][inputs.input_ids.shape[1]:]
        SMOKE_TEXT = tokenizer.decode(gen, skip_special_tokens=True).strip()
        MODEL_GENERATION_READY = bool(SMOKE_TEXT)
        print("MODEL_GENERATION_READY:", MODEL_GENERATION_READY)
        print("SMOKE:", SMOKE_TEXT)
    except Exception:
        MODEL_GENERATION_READY = False
        MODEL_ERROR = traceback.format_exc()
        print("MODEL SMOKE TEST FAILED")
        print(MODEL_ERROR)

load_model()
model_smoke_test()

print("DEPENDENCY_STATUS:", DEPENDENCY_STATUS)
print("DEVICE_INFO:", DEVICE_INFO)
```

## 2. Runtime Objects

```python
class State(Enum):
    PSI = "Ψ"
    OMEGA = "Ω"
    BOTTOM = "⊥"

@dataclass
class CompilerRootSlot:
    raw_input: str
    profile: str
    inferred_task: str
    required_operation: str
    preserved_function: str
    boundary_conditions: List[str]
    anti_fits: List[str]
    admissible_shape: str
    failure_modes: List[str]
    semantic_locks: Dict[str, str]
    forbidden_drifts: List[str]
    model_facing_prompt: str
    collapse_rule: str
    source: str = "compiler_root"
    compiler_confidence: float = 1.0

    def text_positive(self) -> str:
        return " ".join([
            self.required_operation,
            self.preserved_function,
            self.admissible_shape,
            " ".join(self.boundary_conditions),
        ])

    def text_negative(self) -> str:
        return " ".join(self.anti_fits + self.failure_modes + self.forbidden_drifts)

    def signature(self) -> str:
        s = json.dumps(asdict(self), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

@dataclass
class ModelInductionPacket:
    inferred_task: str
    required_operation: str
    preserved_function: str
    boundary_conditions: List[str]
    anti_fits: List[str]
    admissible_shape: str
    failure_modes: List[str]
    semantic_locks: Dict[str, str]
    forbidden_drifts: List[str]
    model_facing_prompt: str
    confidence: float
    packet_origin: str = "model"

    def text_positive(self) -> str:
        return " ".join([
            self.required_operation,
            self.preserved_function,
            self.admissible_shape,
            " ".join(self.boundary_conditions),
        ])

    def text_negative(self) -> str:
        return " ".join(self.anti_fits + self.failure_modes + self.forbidden_drifts)

@dataclass
class SlotGateDecision:
    decision: str
    accepted_origin: str
    authority: str
    alignment_score: float
    generic_score: float
    drift_flags: Dict[str, bool]
    reason: str
    root_signature: str
    model_packet_present: bool
    notes: List[str] = field(default_factory=list)

@dataclass
class RuntimeContract:
    profile: str
    raw_input: str
    inferred_task: str
    required_operation: str
    preserved_function: str
    boundary_conditions: List[str]
    anti_fits: List[str]
    admissible_shape: str
    failure_modes: List[str]
    semantic_locks: Dict[str, str]
    forbidden_drifts: List[str]
    model_facing_prompt: str
    collapse_rule: str
    authority: str
    accepted_origin: str
    slot_gate: Dict[str, Any]
    mutation_history: List[Dict[str, Any]] = field(default_factory=list)

    def signature(self) -> str:
        s = json.dumps(asdict(self), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

@dataclass
class ContractPatch:
    reason: str
    add_boundary_conditions: List[str] = field(default_factory=list)
    add_anti_fits: List[str] = field(default_factory=list)
    add_failure_modes: List[str] = field(default_factory=list)
    add_semantic_locks: Dict[str, str] = field(default_factory=dict)
    add_forbidden_drifts: List[str] = field(default_factory=list)
    refine_required_operation: str = ""
    refine_preserved_function: str = ""
    trace_note: str = ""

@dataclass
class Residue:
    description: str
    missing_pieces: List[str]
    failed_checks: List[str]
    contract_patch: Dict[str, Any]
    next_operation: str
    residue_score: float
    actionable: bool
    dead_reason: Optional[str] = None

@dataclass
class Branch:
    role: str
    origin: str
    depth: int
    prompt_used: str
    output: str
    score: float = 0.0
    checks: Dict[str, Any] = field(default_factory=dict)
    dimensions: Dict[str, float] = field(default_factory=dict)
    polysemy_check: bool = False
    rejected: bool = True
    rejection_reasons: List[str] = field(default_factory=list)

@dataclass
class PromptResult:
    prompt: str
    state: str
    reason: str
    depth: int
    root_slot: Dict[str, Any]
    model_packet: Optional[Dict[str, Any]]
    slot_gate: Dict[str, Any]
    final_contract: Dict[str, Any]
    contract_signatures: List[str]
    winner_branch: Optional[str]
    winner_origin: Optional[str]
    winner_score: float
    answer: str
    raw_answer: str
    shaped_answer: Optional[str]
    branches: List[Dict[str, Any]]
    residues: List[Dict[str, Any]]
    metrics: Dict[str, Any]
```

## 3. Utility Functions

```python
def normalize_text(s: Any) -> str:
    return re.sub(r"\s+", " ", str(s or "").lower()).strip()

def words(s: Any) -> List[str]:
    return re.findall(r"\b[a-zA-Z][a-zA-Z0-9_\-]{2,}\b", normalize_text(s))

def word_count(s: Any) -> int:
    return len(re.findall(r"\b\w+\b", str(s or "")))

def contains_any(text: str, terms: List[str]) -> bool:
    t = normalize_text(text)
    return any(term.lower() in t for term in terms if term)

def count_any(text: str, terms: List[str]) -> int:
    t = normalize_text(text)
    return sum(1 for term in terms if term and term.lower() in t)

def jaccard_text(a: str, b: str) -> float:
    wa = set(words(a))
    wb = set(words(b))
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)

def containment_score(needles: List[str], haystack: str) -> float:
    if not needles:
        return 1.0
    h = normalize_text(haystack)
    hits = 0
    for n in needles:
        nw = set(words(n))
        if not nw:
            continue
        hw = set(words(h))
        overlap = len(nw & hw) / max(1, len(nw))
        if overlap >= 0.45 or normalize_text(n) in h:
            hits += 1
    return hits / max(1, len(needles))

def unique_extend(base: List[str], add: List[str]) -> List[str]:
    out = list(base)
    seen = {normalize_text(x) for x in out}
    for item in add or []:
        s = str(item).strip()
        if s and normalize_text(s) not in seen:
            out.append(s)
            seen.add(normalize_text(s))
    return out

def extract_json_object(text: str) -> Optional[Dict[str, Any]]:
    if not text:
        return None
    candidates = [text]
    cleaned = re.sub(r"```(?:json|JSON)?", "", text).replace("```", "").strip()
    candidates.append(cleaned)
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start >= 0 and end > start:
        candidates.append(cleaned[start:end+1])

    for c in candidates:
        try:
            obj = json.loads(c)
            if isinstance(obj, dict):
                return obj
        except Exception:
            pass
    return None

def safe_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(v).strip() for v in x if str(v).strip()]
    if isinstance(x, str):
        if not x.strip():
            return []
        # split only if obvious semicolon format
        if ";" in x:
            return [p.strip() for p in x.split(";") if p.strip()]
        return [x.strip()]
    return [str(x).strip()]

def safe_dict(x: Any) -> Dict[str, str]:
    if isinstance(x, dict):
        return {str(k).strip(): str(v).strip() for k, v in x.items() if str(k).strip() and str(v).strip()}
    return {}

def clamp01(x: Any, default: float = 0.5) -> float:
    try:
        return max(0.0, min(1.0, float(x)))
    except Exception:
        return default

def model_generate(prompt: str, max_new_tokens: int, temperature: float) -> str:
    if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY:
        raise RuntimeError("Model generation not ready; refusing fallback Ψ.")

    messages = [{"role": "user", "content": prompt}]
    rendered = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(rendered, return_tensors="pt").to(next(model.parameters()).device)

    with torch.no_grad():
        out = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=True if temperature > 0 else False,
            return_dict_in_generate=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    gen = out.sequences[0][inputs.input_ids.shape[1]:]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()
```

## 4. Compiler-Root Slot

This is the authority layer. It is deterministic and profile-specific. It may be imperfect, but it cannot hallucinate authority from surface fluency.


```python
DEFAULT_LOCKS = {
    "contract": "runtime execution contract, not legal agreement",
    "tool": "external action/function/API channel with possible side effects",
    "controller": "agent governance loop that owns policy and next-action selection",
    "policy": "runtime decision rule, not organizational ownership",
    "evidence": "observation submitted to verifier/controller, not a command",
    "memory": "causal trace continuity, not a paragraph summary",
    "retrieval": "operational fit / missing-slot recovery, not noun overlap",
    "shape": "operational structure, not literal geometry unless explicitly requested",
    "rollback": "restore prior valid state while preserving evidence and trace",
    "induction": "structured coupling that changes model trajectory without direct payload transfer or weight change",
    "residue": "unresolved structure that can induce the next operation",
    "slot": "operational control surface / need-slot, not free-form summary",
}

PROFILE_PATTERNS = {
    "input_induction": ["input", "prompt", "ask", "user input", "model-facing", "induce", "induction", "coil"],
    "recursive_solver": ["recursive", "recursion", "residue", "keep solving", "bottom", "omega", "Ω", "next operation", "discovery"],
    "runtime_contract": ["contract", "precondition", "postcondition", "success", "failure", "api call", "function call"],
    "tool_safety": ["tool", "safe", "unsafe", "permission", "risk", "side effect", "execute", "rollback"],
    "evidence_control": ["tool output", "tool result", "evidence", "observation", "authority", "controller", "policy", "command"],
    "memory_trace": ["memory", "summary", "trace", "context", "which-path", "history", "state transition"],
    "inverse_retrieval": ["retrieval", "retrieve", "search", "keyword", "noun", "label", "inverse", "missing slot", "function instead of name"],
}

def infer_profile_root(raw_input: str) -> Tuple[str, Dict[str, int]]:
    t = normalize_text(raw_input)
    scores = {p: count_any(t, terms) for p, terms in PROFILE_PATTERNS.items()}

    if any(x in t for x in ["how we ask", "correct input", "user input", "model-facing", "prompt coil"]):
        scores["input_induction"] += 4
    if any(x in t for x in ["keep solving", "residue not answers", "recurses on residue", "recursive solver", "bottom"]):
        scores["recursive_solver"] += 4
    if "tool output" in t or "tool result" in t:
        scores["evidence_control"] += 4
    if "rollback" in t and "tool" in t:
        scores["tool_safety"] += 3
    if "conversation summary" in t or "agent memory" in t or "which-path" in t:
        scores["memory_trace"] += 4
    if "keyword" in t or "noun" in t or "retrieval" in t or "retrieve" in t:
        scores["inverse_retrieval"] += 4
    if "contract" in t and ("tool" in t or "api" in t or "runtime" in t):
        scores["runtime_contract"] += 4

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "general"
    return best, scores

def compile_root_slot(raw_input: str) -> CompilerRootSlot:
    profile, profile_scores = infer_profile_root(raw_input)

    locks = dict(DEFAULT_LOCKS)
    boundary = ["preserve the requested operation", "avoid surface paraphrase", "return Ω rather than false Ψ"]
    anti = ["generic answer", "surface vocabulary echo", "wrong semantic carrier"]
    failure = ["model answers raw words without compiling task geometry", "contract/spec echo without operational answer"]
    forbidden = ["legal-contract drift", "tool-output-as-command drift", "memory-as-summary drift", "keyword-only retrieval"]

    if profile == "input_induction":
        inferred = "compile raw user input into model-facing task geometry before answering"
        req = "extract implied task, preserved function, semantic locks, forbidden drift, and model-facing prompt"
        pres = "convert messy human signal into an internal operational contract without answering the raw wording directly"
        boundary += ["raw user words are not automatically the true task", "compiler-root contract must precede model answer"]
        anti += ["generic prompt rewriting tips", "surface paraphrase", "asking advice instead of compiling"]
        adm = "an induction packet that states the true internal task, preserved function, locks, forbidden drift, and collapse rule"
        failure += ["model-facing prompt is just a polite rewording", "packet omits forbidden drift or preserved function"]
        forbidden += ["just rephrase the prompt", "prompt engineering tips only"]
    elif profile == "recursive_solver":
        inferred = "operate a recursive solver that continues only on shaped residue"
        req = "turn Ω residue into a contract patch and next operation, not another answer draft"
        pres = "recursion solves unresolved structure; it does not keep talking"
        boundary += ["Ω means shaped unresolved residue", "⊥ only for true dead branch", "max depth unresolved should remain Ω unless impossible"]
        anti += ["answer-loop recursion", "append repair text to prompt", "collapse max-depth residue to bottom by default"]
        adm = "a residue engine that emits ΔC_t contract patches, stop rules, and Ψ/Ω/⊥ state transitions"
        failure += ["recursion discusses residue instead of mutating contract", "dead branch used for merely unresolved residue"]
        forbidden += ["keep talking loop", "max-depth equals bottom"]
    elif profile == "runtime_contract":
        inferred = "define a runtime execution contract for bounded action"
        req = "state preconditions, postconditions, success/failure criteria, side effects, rollback, and trace update"
        pres = "tool/function/API execution is bounded before and verified after action"
        boundary += ["contract means runtime execution contract", "not legal agreement", "checks occur before execution"]
        anti += ["legal agreement", "liability framing", "execute first and inspect later"]
        adm = "a runtime contract schema that gates action and records trace"
        failure += ["legal contract drift", "missing rollback", "missing postcondition"]
        forbidden += ["binding parties", "terms of service"]
    elif profile == "tool_safety":
        inferred = "gate tool use before execution"
        req = "check permission, preconditions, bounded side effects, risk, safe failure, and rollback"
        pres = "external action cannot proceed until risk and side effects are bounded"
        boundary += ["tool calls may change external state", "permission and side effects precede execution"]
        anti += ["execute because available", "trust tool blindly", "unbounded external side effect"]
        adm = "a safety gate that can reject, defer, sandbox, or safely execute a tool action"
        failure += ["permission omitted", "rollback omitted", "risk not bounded"]
        forbidden += ["just run it", "assume safe"]
    elif profile == "evidence_control":
        inferred = "treat tool output as evidence rather than command authority"
        req = "verify observation, route through controller, apply runtime policy, then choose next action"
        pres = "tool results inform the agent but do not control the agent"
        boundary += ["controller owns policy", "tool output is observation", "conflicts require verification"]
        anti += ["tool output commands next action", "administrator-policy drift", "authority confusion"]
        adm = "an evidence-control loop where observations pass through verifier and controller gate"
        failure += ["tool result becomes authority", "policy treated as organization/admin ownership"]
        forbidden += ["tool decides", "security team owns policy", "administrator policy"]
    elif profile == "memory_trace":
        inferred = "explain or design memory as causal trace continuity"
        req = "preserve state transitions, observations, decisions, actions, results, rollbacks, and updates"
        pres = "memory keeps which-path continuity, not just a compressed summary"
        boundary += ["summary is lossy", "trace preserves causal order", "state updates must be recoverable"]
        anti += ["memory is just a text summary", "recap replaces state", "which-path loss"]
        adm = "a trace object carrying state, observation, decision, action, result, rollback, and update"
        failure += ["summary-only memory", "causal order omitted", "state transitions absent"]
        forbidden += ["simple recap equals memory"]
    elif profile == "inverse_retrieval":
        inferred = "retrieve by inverse operational fit when noun matching fails"
        req = "extract desired operation, infer missing slot, generate candidates by function, reject noun-only matches"
        pres = "select artifacts that close the operational need even if labels differ"
        boundary += ["operation beats noun", "candidate must be verified by function", "surface label mismatch is allowed"]
        anti += ["keyword-only search", "noun overlap", "title match", "semantic adjacency without function"]
        adm = "retrieval contract that ranks candidates by preserved function and missing-slot closure"
        failure += ["candidate chosen because it sounds similar", "operation not verified"]
        forbidden += ["keyword-only", "noun overlap only"]
    else:
        inferred = "answer the request while preserving its operational function"
        req = "identify task, preserve operation, avoid semantic drift, answer directly"
        pres = "produce a useful answer without converting the task into an adjacent meaning"
        adm = "direct answer with explicit operation and constraints"

    model_prompt = (
        f"Task: {inferred}\n"
        f"Required operation: {req}\n"
        f"Preserved function: {pres}\n"
        f"Boundary conditions: {'; '.join(boundary)}\n"
        f"Anti-fits: {'; '.join(anti)}\n"
        f"Admissible shape: {adm}\n"
        f"Collapse rule: answer only if the operation is preserved; otherwise return Ω with shaped residue."
    )

    return CompilerRootSlot(
        raw_input=raw_input,
        profile=profile,
        inferred_task=inferred,
        required_operation=req,
        preserved_function=pres,
        boundary_conditions=boundary,
        anti_fits=anti,
        admissible_shape=adm,
        failure_modes=failure,
        semantic_locks=locks,
        forbidden_drifts=forbidden,
        model_facing_prompt=model_prompt,
        collapse_rule="Ψ requires model-origin output that fits compiler-root slot; Ω preserves unresolved residue; ⊥ only isolates truly dead branches",
        source="compiler_root",
        compiler_confidence=1.0 if profile != "general" else 0.7,
    )
```

## 5. Model Packet as Evidence

```python
def generate_model_packet(root: CompilerRootSlot) -> Tuple[Optional[ModelInductionPacket], Dict[str, Any]]:
    meta = {
        "attempted": False,
        "parse_ok": False,
        "raw": None,
        "error": None,
        "warnings": [],
    }

    prompt = f"""
You are a model-side Slot Proposal Generator.

You do NOT control the runtime.
You propose evidence only. A compiler-root slot will judge your proposal.

Return strict JSON only with fields:
- inferred_task: string
- required_operation: string
- preserved_function: string
- boundary_conditions: list of strings
- anti_fits: list of strings
- admissible_shape: string
- failure_modes: list of strings
- semantic_locks: object mapping term to required meaning
- forbidden_drifts: list of strings
- model_facing_prompt: string
- confidence: number 0..1

Raw user input:
{root.raw_input}

Compiler-root baseline geometry:
{json.dumps(asdict(root), indent=2, ensure_ascii=False)}

Rules:
- Preserve the compiler-root operation.
- Add texture only if it agrees with the root.
- Do not paraphrase into generic prompt advice.
- Do not convert runtime terms into legal/admin meanings.
- Do not answer the user.
""".strip()

    if not MODEL_GENERATION_READY:
        meta["warnings"].append("model_not_ready")
        return None, meta

    try:
        meta["attempted"] = True
        raw = model_generate(prompt, MAX_NEW_TOKENS_PACKET, TEMPERATURE_PACKET)
        meta["raw"] = raw
        obj = extract_json_object(raw)
        if not obj:
            meta["warnings"].append("json_parse_failed")
            return None, meta

        packet = ModelInductionPacket(
            inferred_task=str(obj.get("inferred_task") or "").strip(),
            required_operation=str(obj.get("required_operation") or "").strip(),
            preserved_function=str(obj.get("preserved_function") or "").strip(),
            boundary_conditions=safe_list(obj.get("boundary_conditions")),
            anti_fits=safe_list(obj.get("anti_fits")),
            admissible_shape=str(obj.get("admissible_shape") or "").strip(),
            failure_modes=safe_list(obj.get("failure_modes")),
            semantic_locks=safe_dict(obj.get("semantic_locks")),
            forbidden_drifts=safe_list(obj.get("forbidden_drifts")),
            model_facing_prompt=str(obj.get("model_facing_prompt") or "").strip(),
            confidence=clamp01(obj.get("confidence"), 0.5),
            packet_origin="model",
        )
        meta["parse_ok"] = True
        return packet, meta
    except Exception:
        meta["error"] = traceback.format_exc()
        return None, meta
```

## 6. Slot Gate

```python
GENERIC_PACKET_MARKERS = [
    "clear and concise instruction",
    "provide a prompt",
    "based on user instructions",
    "satisfy the missing operational need",
    "format suitable for the ai system",
    "understand the context",
    "compile input correctly",
    "generic prompt",
    "rewrite the prompt",
    "prompt engineering",
]

CRITICAL_DRIFT_MARKERS = [
    "legal agreement",
    "binding parties",
    "liability",
    "terms of service",
    "administrator policy",
    "security team owns",
    "tool decides",
    "memory is just a summary",
    "keyword-only",
]

def score_model_packet_against_root(root: CompilerRootSlot, packet: Optional[ModelInductionPacket]) -> SlotGateDecision:
    if packet is None:
        return SlotGateDecision(
            decision="use_root_no_model_packet",
            accepted_origin="compiler_root",
            authority="compiler_root",
            alignment_score=0.0,
            generic_score=0.0,
            drift_flags={"missing_model_packet": True},
            reason="no parseable model packet; compiler root remains authority",
            root_signature=root.signature(),
            model_packet_present=False,
        )

    root_pos = root.text_positive()
    model_pos = packet.text_positive()
    root_neg = root.text_negative()
    model_neg = packet.text_negative()
    combined_model = " ".join([
        packet.inferred_task,
        packet.required_operation,
        packet.preserved_function,
        packet.admissible_shape,
        packet.model_facing_prompt,
        " ".join(packet.boundary_conditions),
        " ".join(packet.anti_fits),
        " ".join(packet.failure_modes),
        " ".join(packet.forbidden_drifts),
    ])

    op_align = jaccard_text(root.required_operation, packet.required_operation + " " + packet.model_facing_prompt)
    preserved_align = jaccard_text(root.preserved_function, packet.preserved_function + " " + packet.inferred_task)
    positive_align = jaccard_text(root_pos, model_pos)
    boundary_cov = containment_score(root.boundary_conditions[:5], combined_model)
    anti_cov = containment_score(root.anti_fits[:4], model_neg + " " + combined_model)
    lock_cov = containment_score([f"{k} {v}" for k, v in list(root.semantic_locks.items())[:8]], json.dumps(packet.semantic_locks))

    alignment = (
        0.25 * op_align
        + 0.20 * preserved_align
        + 0.20 * positive_align
        + 0.15 * boundary_cov
        + 0.12 * anti_cov
        + 0.08 * lock_cov
    )

    generic_score = count_any(combined_model, GENERIC_PACKET_MARKERS) / max(1, len(GENERIC_PACKET_MARKERS))
    critical_drift = {m: (m in normalize_text(combined_model)) for m in CRITICAL_DRIFT_MARKERS}
    root_forbidden_hit = {f"root_forbidden:{f}": (normalize_text(f) in normalize_text(combined_model)) for f in root.forbidden_drifts if len(f) > 4}
    drift_flags = {
        "generic_packet": generic_score >= 0.10,
        "low_confidence": packet.confidence < 0.65,
        "low_alignment": alignment < 0.52,
        **critical_drift,
        **root_forbidden_hit,
    }

    critical = any(v for k, v in drift_flags.items() if k not in ["low_alignment"])

    if alignment >= 0.68 and not critical:
        decision = "accept_model_enrichment"
        accepted_origin = "compiler_root+model_enriched"
        reason = "model proposal aligns with compiler-root geometry and may enrich final contract"
    elif alignment >= 0.52 and not any(critical_drift.values()) and packet.confidence >= 0.70:
        decision = "use_root_with_model_notes"
        accepted_origin = "compiler_root"
        reason = "model proposal partially aligns but does not become authority"
    else:
        decision = "reject_model_use_root"
        accepted_origin = "compiler_root"
        reason = "model proposal is generic, drifting, or insufficiently aligned; compiler root remains authority"

    return SlotGateDecision(
        decision=decision,
        accepted_origin=accepted_origin,
        authority="compiler_root",
        alignment_score=float(alignment),
        generic_score=float(generic_score),
        drift_flags=drift_flags,
        reason=reason,
        root_signature=root.signature(),
        model_packet_present=True,
        notes=[
            f"op_align={op_align:.3f}",
            f"preserved_align={preserved_align:.3f}",
            f"positive_align={positive_align:.3f}",
            f"boundary_cov={boundary_cov:.3f}",
            f"anti_cov={anti_cov:.3f}",
            f"lock_cov={lock_cov:.3f}",
            f"packet_confidence={packet.confidence:.3f}",
        ],
    )

def build_contract(root: CompilerRootSlot, packet: Optional[ModelInductionPacket], gate: SlotGateDecision) -> RuntimeContract:
    # Authority remains compiler-rooted. Model enrichment is allowed only as non-conflicting texture.
    inferred_task = root.inferred_task
    req = root.required_operation
    pres = root.preserved_function
    boundary = list(root.boundary_conditions)
    anti = list(root.anti_fits)
    admissible = root.admissible_shape
    failure = list(root.failure_modes)
    locks = dict(root.semantic_locks)
    forbidden = list(root.forbidden_drifts)
    model_prompt = root.model_facing_prompt

    if packet and gate.decision == "accept_model_enrichment":
        boundary = unique_extend(boundary, packet.boundary_conditions[:4])
        anti = unique_extend(anti, packet.anti_fits[:4])
        failure = unique_extend(failure, packet.failure_modes[:4])
        forbidden = unique_extend(forbidden, packet.forbidden_drifts[:4])
        for k, v in packet.semantic_locks.items():
            if k not in locks and len(k) < 40 and len(v) < 180:
                locks[k] = v
        # Keep root task/preserved function as authority; only append model nuance to prompt if aligned.
        if packet.model_facing_prompt and gate.alignment_score >= 0.75:
            model_prompt = root.model_facing_prompt + "\nModel-side enrichment: " + packet.model_facing_prompt

    return RuntimeContract(
        profile=root.profile,
        raw_input=root.raw_input,
        inferred_task=inferred_task,
        required_operation=req,
        preserved_function=pres,
        boundary_conditions=boundary,
        anti_fits=anti,
        admissible_shape=admissible,
        failure_modes=failure,
        semantic_locks=locks,
        forbidden_drifts=forbidden,
        model_facing_prompt=model_prompt,
        collapse_rule=root.collapse_rule,
        authority="compiler_root",
        accepted_origin=gate.accepted_origin,
        slot_gate=asdict(gate),
        mutation_history=[],
    )
```

## 7. Contract Mutation from Residue

```python
def apply_patch(contract: RuntimeContract, patch: ContractPatch, depth: int) -> RuntimeContract:
    c = RuntimeContract(**asdict(contract))
    c.boundary_conditions = unique_extend(c.boundary_conditions, patch.add_boundary_conditions)
    c.anti_fits = unique_extend(c.anti_fits, patch.add_anti_fits)
    c.failure_modes = unique_extend(c.failure_modes, patch.add_failure_modes)
    c.forbidden_drifts = unique_extend(c.forbidden_drifts, patch.add_forbidden_drifts)

    c.semantic_locks = dict(c.semantic_locks)
    for k, v in patch.add_semantic_locks.items():
        if k and v:
            c.semantic_locks[str(k)] = str(v)

    if patch.refine_required_operation:
        c.required_operation = c.required_operation + " | refinement: " + patch.refine_required_operation
    if patch.refine_preserved_function:
        c.preserved_function = c.preserved_function + " | refinement: " + patch.refine_preserved_function

    c.mutation_history = list(c.mutation_history)
    c.mutation_history.append({
        "depth": depth,
        "patch": asdict(patch),
        "new_signature": c.signature(),
    })
    return c

def patch_from_failed_checks(contract: RuntimeContract, failed_checks: List[str], reasons: List[str], depth: int) -> ContractPatch:
    patch = ContractPatch(
        reason="compiler_root_residue_patch",
        trace_note=f"depth {depth}: patching failed checks {failed_checks}",
    )

    for fc in failed_checks:
        if fc in ["compiled_input", "compiled_not_raw", "model_facing"]:
            patch.add_boundary_conditions.append("answer must describe compiled model-facing task geometry, not generic prompt advice")
            patch.refine_required_operation = "explicitly convert raw input into internal task geometry"
            patch.add_anti_fits.append("generic prompt-writing advice")
        elif fc in ["residue_to_contract_patch", "contract_mutation"]:
            patch.add_boundary_conditions.append("residue must produce a contract patch ΔC_t")
            patch.refine_required_operation = "state how Ω residue mutates the contract"
            patch.add_anti_fits.append("append repair text without contract mutation")
        elif fc in ["stop_condition", "state_policy"]:
            patch.add_boundary_conditions.append("max-depth unresolved residue returns Ω unless truly dead")
            patch.add_anti_fits.append("collapse unresolved residue to bottom by default")
            patch.add_semantic_locks["⊥"] = "dead branch only: impossible, contradictory, or repeated no-change residue"
        elif fc in ["runtime_not_legal", "legal_drift"]:
            patch.add_semantic_locks["contract"] = "runtime execution contract, not legal agreement"
            patch.add_forbidden_drifts.extend(["legal agreement", "liability", "binding parties", "terms of service"])
        elif fc in ["tool_output_not_command", "evidence_control"]:
            patch.add_semantic_locks["evidence"] = "tool output is observation/evidence, not command authority"
            patch.add_semantic_locks["controller"] = "agent governance loop that owns policy and next action"
            patch.add_anti_fits.append("tool output controls next action")
        elif fc in ["memory_not_summary", "trace_continuity"]:
            patch.add_semantic_locks["memory"] = "causal trace continuity across state transitions"
            patch.add_anti_fits.append("memory is just a summary")
        elif fc in ["operation_not_noun", "inverse_fit"]:
            patch.add_semantic_locks["retrieval"] = "retrieve by operation and missing-slot closure, not noun overlap"
            patch.add_anti_fits.append("keyword-only retrieval")
        elif fc in ["meta_leak"]:
            patch.add_anti_fits.extend(["mentioning profile check", "discussing current residue", "auditor-facing language in user answer"])
            patch.add_boundary_conditions.append("user-facing branch answer must not expose internal audit/residue language")

    if "polysemy_or_origin_drift" in reasons:
        patch.add_boundary_conditions.append("polysemy lock must be explicit before collapse")

    if not patch.add_boundary_conditions and not patch.refine_required_operation:
        patch.add_boundary_conditions.append("answer must satisfy compiler-root admissible shape directly")
        patch.refine_required_operation = "make the operational fit explicit"

    return patch
```

## 8. Branch Prompting

```python
def contract_block_for_branch(contract: RuntimeContract) -> str:
    locks = "\n".join(f"- {k}: {v}" for k, v in list(contract.semantic_locks.items())[:12])
    return f"""
TASK PROFILE: {contract.profile}
INFERRED TASK: {contract.inferred_task}
REQUIRED OPERATION: {contract.required_operation}
PRESERVED FUNCTION: {contract.preserved_function}
ADMISSIBLE SHAPE: {contract.admissible_shape}

BOUNDARY CONDITIONS:
{chr(10).join("- " + x for x in contract.boundary_conditions[:10])}

ANTI-FITS:
{chr(10).join("- " + x for x in contract.anti_fits[:10])}

SEMANTIC LOCKS:
{locks}

FORBIDDEN DRIFTS:
{chr(10).join("- " + x for x in contract.forbidden_drifts[:10])}
""".strip()

def role_instruction(role: str) -> str:
    return {
        "construct": "Produce the clearest direct answer.",
        "verify": "First ensure the answer preserves the operation, then give the answer.",
        "repair": "Avoid the listed anti-fits and produce a corrected answer.",
        "counter": "Check the likely wrong interpretation, reject it briefly, then answer.",
    }.get(role, "Answer directly.")

def make_branch_prompt(contract: RuntimeContract, role: str, residue: Optional[Residue]) -> str:
    # Residue is used as hidden repair pressure, but the model is told not to expose it.
    repair_pressure = ""
    if residue:
        repair_pressure = (
            "\nInternal repair pressure, do not mention this section in the answer:\n"
            + json.dumps({
                "failed_checks": residue.failed_checks,
                "missing_pieces": residue.missing_pieces,
                "next_operation": residue.next_operation,
            }, ensure_ascii=False)
        )

    return f"""
You are an answer branch inside the RHI runtime.

Answer the USER REQUEST directly. Do not expose internal audit, residue, branch role, score, profile check, or contract debugging language.

USER REQUEST:
{contract.raw_input}

COMPILER-ROOT TASK GEOMETRY:
{contract_block_for_branch(contract)}

BRANCH ROLE:
{role}: {role_instruction(role)}

{repair_pressure}

OUTPUT REQUIREMENTS:
- Directly answer the user request.
- Preserve the required operation and preserved function.
- Use the semantic locks.
- Do not drift into anti-fits.
- Do not mention "current residue", "profile check", "failed checks", "depth", or "branch" in the final answer.
- If unresolved, state Ω with the shaped missing piece and next operation, not generic failure.
""".strip()

def generate_branch(contract: RuntimeContract, role: str, depth: int, residue: Optional[Residue]) -> Branch:
    prompt = make_branch_prompt(contract, role, residue)
    try:
        output = model_generate(prompt, MAX_NEW_TOKENS_BRANCH, TEMPERATURE_BRANCH)
        return Branch(role=role, origin="model", depth=depth, prompt_used=prompt, output=output)
    except Exception:
        return Branch(
            role=role,
            origin="error",
            depth=depth,
            prompt_used=prompt,
            output="",
            score=0.0,
            checks={"error": traceback.format_exc()},
            dimensions={},
            polysemy_check=False,
            rejected=True,
            rejection_reasons=["model_generation_error"],
        )
```

## 9. Operational Critic

```python
META_LEAK_MARKERS = [
    "profile check", "current residue", "failed checks", "depth 0", "depth 1", "depth 2", "depth 3",
    "branch role", "winner", "score", "contract patch", "audit dimensions", "residue score",
]
LEGAL_DRIFT = ["legal agreement", "binding parties", "liability", "contract law", "terms of service", "hereby"]
ADMIN_DRIFT = ["administrator policy", "security team", "company policy", "organizational policy"]
TOOL_AUTHORITY_DRIFT = ["tool decides", "tool output controls", "tool result commands", "output commands"]
SUMMARY_DRIFT = ["memory is just a summary", "conversation summary is memory", "simple recap is memory"]
KEYWORD_DRIFT = ["keyword-only", "noun overlap only", "title match only"]

PROFILE_THRESHOLDS = {
    "input_induction": 0.62,
    "recursive_solver": 0.62,
    "runtime_contract": 0.64,
    "tool_safety": 0.64,
    "evidence_control": 0.64,
    "memory_trace": 0.62,
    "inverse_retrieval": 0.62,
    "general": 0.64,
}

def profile_checks_for_output(text: str, contract: RuntimeContract) -> Dict[str, bool]:
    t = normalize_text(text)
    p = contract.profile

    if p == "input_induction":
        return {
            "compiled_input": contains_any(t, ["raw input", "user input", "model-facing", "internal question", "induction", "compiled"]),
            "preserved_function": contains_any(t, ["preserved function", "operation", "intent", "true task", "task geometry"]),
            "semantic_locks": contains_any(t, ["semantic lock", "forbidden drift", "boundary", "constraint"]),
            "not_generic_prompt_tips": not contains_any(t, ["prompt engineering tips", "just rephrase", "write a clearer prompt"]),
        }
    if p == "recursive_solver":
        return {
            "residue": contains_any(t, ["residue", "unresolved", "missing piece", "gap", "Ω"]),
            "residue_to_contract_patch": contains_any(t, ["contract patch", "mutate", "constraint update", "ΔC", "next operation"]),
            "not_answer_loop": contains_any(t, ["not answers", "not keep talking", "not another answer", "residue not answers", "solver"]),
            "stop_condition": contains_any(t, ["Ψ", "Ω", "⊥", "bottom", "stop", "dead branch", "collapse"]),
        }
    if p == "runtime_contract":
        return {
            "runtime_not_legal": contains_any(t, ["runtime", "execution", "function", "api", "tool"]) and not contains_any(t, LEGAL_DRIFT),
            "precondition": contains_any(t, ["precondition", "before", "prerequisite"]),
            "postcondition": contains_any(t, ["postcondition", "after", "verify", "expected state"]),
            "side_effect": contains_any(t, ["side effect", "bounded", "scope"]),
            "rollback": contains_any(t, ["rollback", "restore", "recover", "safe failure"]),
        }
    if p == "tool_safety":
        return {
            "permission": contains_any(t, ["permission", "authorized", "allowed", "capability"]),
            "precondition": contains_any(t, ["precondition", "before", "prerequisite", "input valid"]),
            "risk": contains_any(t, ["risk", "unsafe", "danger", "impact"]),
            "side_effect": contains_any(t, ["side effect", "bounded", "external state", "scope"]),
            "safe_failure": contains_any(t, ["reject", "abort", "rollback", "safe failure", "defer"]),
        }
    if p == "evidence_control":
        return {
            "tool_output_not_command": contains_any(t, ["evidence", "observation", "signal", "input to verifier"]) and not contains_any(t, TOOL_AUTHORITY_DRIFT),
            "controller_owns_policy": contains_any(t, ["controller", "runtime", "agent"]) and contains_any(t, ["policy", "gate", "decision rule", "next action"]) and not contains_any(t, ADMIN_DRIFT),
            "verification": contains_any(t, ["verify", "validate", "check", "corroborate"]),
            "conflict_handling": contains_any(t, ["conflict", "disagree", "inconsistent", "compare", "quarantine"]) or "conflicting" not in normalize_text(contract.raw_input),
        }
    if p == "memory_trace":
        return {
            "memory_not_summary": contains_any(t, ["not a summary", "more than a summary", "trace", "causal", "which-path"]),
            "state_transitions": contains_any(t, ["state", "transition", "event", "history"]),
            "obs_decision_action": contains_any(t, ["observation", "decision", "action", "result", "update"]),
            "continuity": contains_any(t, ["continuity", "across turns", "causal order", "previous state"]),
        }
    if p == "inverse_retrieval":
        return {
            "operation_not_noun": contains_any(t, ["operation", "function", "action", "affordance", "transformation"]),
            "missing_slot": contains_any(t, ["missing", "slot", "need", "inverse", "desired effect"]),
            "candidate": contains_any(t, ["candidate", "retrieve", "search", "rank", "select"]),
            "reject_noun_only": contains_any(t, ["not keyword", "not noun", "surface", "label", "reject"]),
            "verify_fit": contains_any(t, ["verify", "fit", "preserve", "closes", "works"]),
        }
    return {
        "substantive": word_count(text) >= 40,
        "operation": contains_any(t, ["operation", "function", "task", "constraint", "answer"]),
        "no_bad_drift": not contains_any(t, LEGAL_DRIFT + TOOL_AUTHORITY_DRIFT + SUMMARY_DRIFT + KEYWORD_DRIFT),
    }

def audit_branch(branch: Branch, contract: RuntimeContract) -> Branch:
    text = branch.output or ""
    t = normalize_text(text)
    wc = word_count(text)

    checks = profile_checks_for_output(text, contract)
    profile_quality = sum(bool(v) for v in checks.values()) / max(1, len(checks))

    positive_fit = jaccard_text(text, contract.required_operation + " " + contract.preserved_function + " " + contract.admissible_shape)
    boundary_fit = containment_score(contract.boundary_conditions[:6], text)
    anti_hit = containment_score(contract.anti_fits[:8], text)
    lock_hit = containment_score([f"{k} {v}" for k, v in list(contract.semantic_locks.items())[:8]], text)

    meta_leak = contains_any(t, META_LEAK_MARKERS)
    legal_drift = contains_any(t, LEGAL_DRIFT)
    admin_drift = contract.profile == "evidence_control" and contains_any(t, ADMIN_DRIFT)
    tool_authority_drift = contract.profile == "evidence_control" and contains_any(t, TOOL_AUTHORITY_DRIFT)
    summary_drift = contract.profile == "memory_trace" and contains_any(t, SUMMARY_DRIFT)
    keyword_drift = contract.profile == "inverse_retrieval" and contains_any(t, KEYWORD_DRIFT)

    drift_flags = {
        "meta_leak": meta_leak,
        "legal_drift": legal_drift,
        "admin_drift": admin_drift,
        "tool_authority_drift": tool_authority_drift,
        "summary_drift": summary_drift,
        "keyword_drift": keyword_drift,
    }

    length_score = min(1.0, wc / 90.0)
    if wc > 260:
        length_score -= min(0.2, (wc - 260) / 700)

    origin_score = 1.0 if branch.origin == "model" else 0.0
    drift_penalty = 0.10 * anti_hit + 0.16 * sum(1 for v in drift_flags.values() if v)

    score = (
        0.34 * profile_quality
        + 0.18 * positive_fit
        + 0.12 * boundary_fit
        + 0.08 * lock_hit
        + 0.13 * length_score
        + 0.15 * origin_score
        - drift_penalty
    )
    score = float(max(0.0, min(1.0, score)))

    polysemy_check = not any([legal_drift, admin_drift, tool_authority_drift, summary_drift, keyword_drift])

    threshold = PROFILE_THRESHOLDS.get(contract.profile, 0.64)
    reasons = []
    if branch.origin != "model":
        reasons.append("origin_not_model")
    if wc < 20:
        reasons.append("too_short")
    if meta_leak:
        reasons.append("meta_leak")
    if not polysemy_check:
        reasons.append("polysemy_drift")
    if profile_quality < 0.45:
        reasons.append("profile_quality_low")
    if score < threshold:
        reasons.append("below_threshold")

    branch.score = score
    branch.checks = {
        "profile_checks": checks,
        "drift_flags": drift_flags,
        "word_count": wc,
    }
    branch.dimensions = {
        "profile_quality": profile_quality,
        "positive_fit": positive_fit,
        "boundary_fit": boundary_fit,
        "anti_hit": anti_hit,
        "lock_hit": lock_hit,
        "length_score": length_score,
        "origin_score": origin_score,
        "drift_penalty": drift_penalty,
    }
    branch.polysemy_check = polysemy_check
    branch.rejected = bool(reasons)
    branch.rejection_reasons = reasons
    return branch
```

## 10. Residue and Collapse

```python
def collapse_gate(contract: RuntimeContract, branches: List[Branch]) -> Tuple[State, str, Optional[Branch], Dict[str, Any]]:
    if not branches:
        return State.OMEGA, "no_branches", None, {}

    ordered = sorted(branches, key=lambda b: b.score, reverse=True)
    best = ordered[0]
    second = ordered[1] if len(ordered) > 1 else None
    threshold = PROFILE_THRESHOLDS.get(contract.profile, 0.64)
    margin = best.score - (second.score if second else 0.0)

    valid = [b for b in ordered if b.origin == "model" and not b.rejected and b.polysemy_check]
    meta = {
        "threshold": threshold,
        "best_score": best.score,
        "margin": margin,
        "valid_count": len(valid),
        "valid_roles": [b.role for b in valid],
    }

    if best.origin != "model":
        return State.OMEGA, "winner_not_model_origin", best, meta
    if best.rejected or not best.polysemy_check:
        return State.OMEGA, "winner_rejected_or_polysemy_failed", best, meta

    if best.score >= threshold and margin >= 0.025:
        return State.PSI, "direct_margin_collapse", best, meta

    if len(valid) >= 2:
        top = valid[:3]
        mean_score = float(np.mean([b.score for b in top]))
        all_keys = set()
        for b in top:
            all_keys |= set(b.checks.get("profile_checks", {}).keys())
        agreed = 0
        for k in all_keys:
            if sum(bool(b.checks.get("profile_checks", {}).get(k, False)) for b in top) >= 2:
                agreed += 1
        op_agreement = agreed / max(1, len(all_keys))
        meta["consensus_mean_score"] = mean_score
        meta["op_agreement"] = op_agreement
        if mean_score >= threshold - 0.04 and op_agreement >= 0.55:
            return State.PSI, "operational_consensus_collapse", top[0], meta

    return State.OMEGA, "shaped_residue_remaining", best, meta

def compute_residue(contract: RuntimeContract, branches: List[Branch], depth: int) -> Residue:
    ordered = sorted(branches, key=lambda b: b.score, reverse=True)
    best = ordered[0] if ordered else None
    threshold = PROFILE_THRESHOLDS.get(contract.profile, 0.64)

    failed = Counter()
    reasons = []
    for b in branches:
        reasons.extend(b.rejection_reasons)
        for k, v in b.checks.get("profile_checks", {}).items():
            if not v:
                failed[k] += 1

    failed_checks = [k for k, _ in failed.most_common(5)]
    missing = []
    if best:
        if best.score < threshold:
            missing.append(f"best score {best.score:.3f} below threshold {threshold:.3f}")
        if not best.polysemy_check:
            missing.append("polysemy lock failed")
        if "meta_leak" in best.rejection_reasons:
            missing.append("branch leaked internal audit/residue language")
    else:
        missing.append("no branch produced output")

    missing.extend([f"profile check failed: {k}" for k in failed_checks[:4]])

    patch = patch_from_failed_checks(contract, failed_checks, reasons, depth)
    residue_score = 1.0 - (best.score if best else 0.0)

    # In v28, max-depth unresolved stays Ω unless truly dead.
    actionable = bool(failed_checks or missing) and depth < MAX_DEPTH
    dead_reason = None
    if not best or all(b.origin != "model" for b in branches):
        actionable = False
        dead_reason = "no_model_origin_branch"
    elif depth >= MAX_DEPTH:
        actionable = False
        dead_reason = "max_depth_unresolved_but_not_dead"

    return Residue(
        description=f"depth {depth}: shaped unresolved residue against compiler-root contract",
        missing_pieces=unique_extend([], missing),
        failed_checks=failed_checks,
        contract_patch=asdict(patch),
        next_operation="mutate contract using failed checks and rerun branches" if depth < MAX_DEPTH else "return Ω with shaped residue",
        residue_score=float(max(0.0, min(1.0, residue_score))),
        actionable=actionable,
        dead_reason=dead_reason,
    )

def is_true_bottom(residues: List[Residue], contract_signatures: List[str]) -> Tuple[bool, str]:
    if not residues:
        return False, ""
    last = residues[-1]
    if last.dead_reason == "no_model_origin_branch":
        return True, "no_model_origin_branch"
    # Repeated no-change signatures indicate dead mutation path.
    if len(contract_signatures) >= 3 and len(set(contract_signatures[-3:])) == 1:
        return True, "repeated_no_change_contract_patch"
    # Critical polysemy across all residues can bottom.
    critical = sum(1 for r in residues if any("polysemy" in x for x in r.missing_pieces))
    if critical >= 3:
        return True, "repeated_polysemy_failure"
    return False, ""
```

## 11. Payload Shaper

```python
def shape_payload(contract: RuntimeContract, raw_answer: str, raw_score: float) -> Tuple[str, bool, Dict[str, Any]]:
    if not SHAPER_ENABLED:
        return raw_answer, False, {"reason": "disabled"}

    prompt = f"""
Compress this answer without changing its operational meaning.

User request:
{contract.raw_input}

Required operation:
{contract.required_operation}

Preserved function:
{contract.preserved_function}

Forbidden drift:
{", ".join(contract.forbidden_drifts[:10])}

Raw answer:
{raw_answer}

Rules:
- Preserve the answer.
- Do not mention internal audit/residue/score/branch/depth.
- Keep 50-130 words if possible.
""".strip()

    try:
        shaped = model_generate(prompt, MAX_NEW_TOKENS_SHAPER, TEMPERATURE_SHAPER)
        tmp = Branch(role="shaper", origin="model", depth=999, prompt_used=prompt, output=shaped)
        tmp = audit_branch(tmp, contract)
        raw_wc = word_count(raw_answer)
        shaped_wc = word_count(shaped)
        accepted = (
            tmp.origin == "model"
            and tmp.polysemy_check
            and "meta_leak" not in tmp.rejection_reasons
            and tmp.score >= max(PROFILE_THRESHOLDS.get(contract.profile, 0.64) - 0.07, raw_score - 0.14)
            and shaped_wc <= max(145, raw_wc + 8)
        )
        return (shaped if accepted else raw_answer), bool(accepted), {
            "reason": "accepted" if accepted else "rejected",
            "raw_words": raw_wc,
            "shaped_words": shaped_wc,
            "audit_score": tmp.score,
            "audit_reasons": tmp.rejection_reasons,
        }
    except Exception:
        return raw_answer, False, {"reason": "shaper_exception", "error": traceback.format_exc()}
```

## 12. Recursive Solver

```python
def solve_prompt(raw_input: str) -> PromptResult:
    root = compile_root_slot(raw_input)
    packet, packet_meta = generate_model_packet(root)
    gate = score_model_packet_against_root(root, packet)
    contract = build_contract(root, packet, gate)

    contract_signatures = [contract.signature()]
    all_branches: List[Branch] = []
    residues: List[Residue] = []

    state = State.OMEGA
    reason = "not_started"
    winner: Optional[Branch] = None
    current_residue: Optional[Residue] = None

    for depth in range(MAX_DEPTH + 1):
        depth_branches = []
        for role in BRANCH_ROLES:
            b = generate_branch(contract, role, depth, current_residue)
            b = audit_branch(b, contract)
            depth_branches.append(b)
            all_branches.append(b)

        state, reason, winner, meta = collapse_gate(contract, depth_branches)

        if state == State.PSI:
            break

        residue = compute_residue(contract, depth_branches, depth)
        residues.append(residue)

        if depth >= MAX_DEPTH:
            bottom, bottom_reason = is_true_bottom(residues, contract_signatures)
            if bottom:
                state = State.BOTTOM
                reason = bottom_reason
            else:
                state = State.OMEGA
                reason = "max_depth_shaped_residue"
            break

        if not residue.actionable:
            bottom, bottom_reason = is_true_bottom(residues, contract_signatures)
            if bottom:
                state = State.BOTTOM
                reason = bottom_reason
            else:
                state = State.OMEGA
                reason = "non_actionable_shaped_residue"
            break

        patch = ContractPatch(**residue.contract_patch)
        new_contract = apply_patch(contract, patch, depth)
        new_sig = new_contract.signature()

        # If patch changes nothing, do not loop forever.
        if new_sig == contract.signature():
            state = State.OMEGA
            reason = "no_change_contract_patch"
            break

        contract = new_contract
        contract_signatures.append(new_sig)
        current_residue = residue

    raw_answer = winner.output if winner else ""
    final_answer = raw_answer
    shaped_answer = None
    shaping_accepted = False
    shaper_meta = {}

    if state == State.PSI and winner is not None:
        final_answer, shaping_accepted, shaper_meta = shape_payload(contract, raw_answer, winner.score)
        shaped_answer = final_answer if shaping_accepted else None

    if REQUIRE_MODEL_FOR_PSI and state == State.PSI:
        if winner is None or winner.origin != "model":
            state = State.OMEGA
            reason = "psi_requires_model_origin"
            final_answer = ""

    metrics = {
        "packet_meta": packet_meta,
        "slot_gate_decision": gate.decision,
        "slot_alignment_score": gate.alignment_score,
        "slot_generic_score": gate.generic_score,
        "accepted_contract_origin": contract.accepted_origin,
        "contract_authority": contract.authority,
        "contract_count": len(contract_signatures),
        "branch_count": len(all_branches),
        "model_branch_count": sum(1 for b in all_branches if b.origin == "model"),
        "rejected_branch_count": sum(1 for b in all_branches if b.rejected),
        "exhaust_ratio": sum(1 for b in all_branches if b.rejected) / max(1, len(all_branches)),
        "best_score": max([b.score for b in all_branches], default=0.0),
        "mean_score": float(np.mean([b.score for b in all_branches])) if all_branches else 0.0,
        "residue_count": len(residues),
        "shaping_accepted": shaping_accepted,
        "shaper_meta": shaper_meta,
    }

    return PromptResult(
        prompt=raw_input,
        state=state.value,
        reason=reason,
        depth=min(MAX_DEPTH, max([b.depth for b in all_branches], default=0)),
        root_slot=asdict(root),
        model_packet=asdict(packet) if packet else None,
        slot_gate=asdict(gate),
        final_contract=asdict(contract),
        contract_signatures=contract_signatures,
        winner_branch=winner.role if winner else None,
        winner_origin=winner.origin if winner else None,
        winner_score=winner.score if winner else 0.0,
        answer=final_answer,
        raw_answer=raw_answer,
        shaped_answer=shaped_answer,
        branches=[asdict(b) for b in all_branches],
        residues=[asdict(r) for r in residues],
        metrics=metrics,
    )
```

## 13. Prompt Battery

```python
PROMPT_BATTERY = [
    # Input induction
    "another thing is how we ask the AI. we may need a AI to generate the correct input from the user input.",
    "convert messy user input into the correct model-facing prompt before answering.",
    "design an input compiler that turns implied user intent into a runtime contract.",
    "explain why the raw user prompt is not always the true task.",
    "build a prompt coil compiler that induces the right internal question.",
    "how should an AI ask itself the right question from a vague user request.",

    # Recursive residue solving
    "if its recursive it should just keep solving, not keep talking.",
    "design a recursive AI loop that recurses on residue not answers.",
    "explain how Ω residue becomes the next better question.",
    "build a residue engine that mutates the contract instead of appending repair text.",
    "when should a recursive solver stop and return bottom.",
    "explain discovery as shaped residue becoming the next operation.",

    # Runtime contract
    "explain why current AI agents fail when they use tools before forming a contract.",
    "design a runtime contract for a file-writing tool.",
    "explain success and failure criteria for an API call.",
    "build a tool-use contract for deleting a file.",
    "show how preconditions and postconditions bound a function call.",
    "explain why tool calls need rollback plans.",

    # Tool safety
    "how should an agent decide whether a tool call is safe.",
    "design a safety gate for an external API call.",
    "when should an agent reject a tool call.",
    "describe safe failure for a dangerous tool action.",
    "explain permission checks before tool execution.",
    "describe bounded risk for tool use in an agent.",

    # Evidence control
    "why is tool output evidence rather than the driver of the agent.",
    "describe tool output as observation not command.",
    "why should the controller own policy after a tool returns.",
    "design a verifier that treats API output as evidence.",
    "describe the difference between evidence and authority in tool use.",
    "how should an agent treat conflicting tool outputs.",

    # Memory trace
    "explain memory in an agent as trace continuity rather than a text summary.",
    "why is a conversation summary not the same as agent memory.",
    "describe memory as causal event history across turns.",
    "why does context amnesia break recursive agents.",
    "explain why summaries lose which-path information.",
    "how should recursive memory preserve state transitions observations decisions and updates.",

    # Inverse retrieval
    "design a shape-first retrieval step where no noun match exists but the inverse need is clear.",
    "how should retrieval work when keywords fail but the operation is obvious.",
    "explain inverse operational fit for search without noun matching.",
    "design a verifier for retrieval candidates selected by need rather than label.",
    "how can an agent rank candidates by function instead of name.",
    "build a retrieval step that rejects keyword-only matches.",
]

PROMPTS = PROMPT_BATTERY[:RUN_PROMPT_LIMIT]
print("Prompt count:", len(PROMPTS))
```

## 14. Execute Run

```python
if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY:
    raise RuntimeError("Model generation is not ready. v28 refuses fallback Ψ.")

t0 = time.time()
RESULTS: List[PromptResult] = []

for i, prompt in enumerate(PROMPTS, start=1):
    print("=" * 100)
    print(f"[{i}/{len(PROMPTS)}] {prompt}")
    try:
        result = solve_prompt(prompt)
    except Exception:
        err = traceback.format_exc()
        root = compile_root_slot(prompt)
        dummy_gate = SlotGateDecision(
            decision="kernel_exception",
            accepted_origin="compiler_root",
            authority="compiler_root",
            alignment_score=0.0,
            generic_score=0.0,
            drift_flags={"kernel_exception": True},
            reason=err,
            root_signature=root.signature(),
            model_packet_present=False,
        )
        contract = build_contract(root, None, dummy_gate)
        result = PromptResult(
            prompt=prompt,
            state=State.OMEGA.value,
            reason="kernel_exception",
            depth=0,
            root_slot=asdict(root),
            model_packet=None,
            slot_gate=asdict(dummy_gate),
            final_contract=asdict(contract),
            contract_signatures=[contract.signature()],
            winner_branch=None,
            winner_origin=None,
            winner_score=0.0,
            answer="",
            raw_answer="",
            shaped_answer=None,
            branches=[],
            residues=[],
            metrics={"error": err},
        )
    RESULTS.append(result)
    print("STATE:", result.state, "REASON:", result.reason, "PROFILE:", result.final_contract.get("profile"))
    print("GATE:", result.slot_gate.get("decision"), "ALIGN:", round(float(result.slot_gate.get("alignment_score", 0)), 3))
    print("WINNER:", result.winner_branch, result.winner_score)
    print("ANSWER:", (result.answer or "")[:260].replace("\n", " "))

elapsed_seconds = time.time() - t0
print("Completed", len(RESULTS), "prompts in", elapsed_seconds, "seconds")
```

## 15. Save Exactly Two Output Files

```python
def summarize(results: List[PromptResult]) -> Tuple[Dict[str, Any], pd.DataFrame]:
    rows = []
    for r in results:
        raw_words = word_count(r.raw_answer)
        final_words = word_count(r.answer)
        rows.append({
            "run_id": RUN_ID,
            "prompt": r.prompt,
            "state": r.state,
            "reason": r.reason,
            "depth": r.depth,
            "profile": r.final_contract.get("profile"),
            "root_source": r.root_slot.get("source"),
            "model_packet_present": r.model_packet is not None,
            "model_packet_confidence": (r.model_packet or {}).get("confidence"),
            "slot_gate_decision": r.slot_gate.get("decision"),
            "slot_alignment_score": r.slot_gate.get("alignment_score"),
            "slot_generic_score": r.slot_gate.get("generic_score"),
            "accepted_contract_origin": r.final_contract.get("accepted_origin"),
            "contract_authority": r.final_contract.get("authority"),
            "contract_count": len(r.contract_signatures),
            "winner_branch": r.winner_branch,
            "winner_origin": r.winner_origin,
            "winner_score": r.winner_score,
            "branch_count": r.metrics.get("branch_count", 0),
            "model_branch_count": r.metrics.get("model_branch_count", 0),
            "rejected_branch_count": r.metrics.get("rejected_branch_count", 0),
            "exhaust_ratio": r.metrics.get("exhaust_ratio", 0.0),
            "best_score": r.metrics.get("best_score", 0.0),
            "mean_score": r.metrics.get("mean_score", 0.0),
            "residue_count": len(r.residues),
            "shaping_accepted": r.metrics.get("shaping_accepted", False),
            "raw_words": raw_words,
            "final_words": final_words,
            "compression_ratio": 1 - final_words / max(1, raw_words),
            "answer_preview": (r.answer or "")[:280].replace("\n", " "),
        })

    df = pd.DataFrame(rows)

    aggregate = {
        "run_id": RUN_ID,
        "version": "v28",
        "purpose": "compiler_root_input_induction_gate",
        "model_id_or_path": MODEL_ID_OR_PATH,
        "model_ready": MODEL_READY,
        "model_generation_ready": MODEL_GENERATION_READY,
        "model_error": MODEL_ERROR,
        "smoke_text": SMOKE_TEXT,
        "dependency_status": DEPENDENCY_STATUS,
        "device_info": DEVICE_INFO,
        "config": {
            "run_prompt_limit": RUN_PROMPT_LIMIT,
            "max_depth": MAX_DEPTH,
            "branch_roles": BRANCH_ROLES,
            "temperature_packet": TEMPERATURE_PACKET,
            "temperature_branch": TEMPERATURE_BRANCH,
            "require_model_for_psi": REQUIRE_MODEL_FOR_PSI,
            "shaper_enabled": SHAPER_ENABLED,
        },
        "elapsed_seconds": elapsed_seconds,
        "total_prompts": len(results),
        "psi_count": int((df["state"] == "Ψ").sum()) if len(df) else 0,
        "omega_count": int((df["state"] == "Ω").sum()) if len(df) else 0,
        "bottom_count": int((df["state"] == "⊥").sum()) if len(df) else 0,
        "psi_ratio": float((df["state"] == "Ψ").mean()) if len(df) else 0.0,
        "omega_ratio": float((df["state"] == "Ω").mean()) if len(df) else 0.0,
        "bottom_ratio": float((df["state"] == "⊥").mean()) if len(df) else 0.0,
        "mean_depth": float(df["depth"].mean()) if len(df) else 0.0,
        "mean_contract_count": float(df["contract_count"].mean()) if len(df) else 0.0,
        "mean_winner_score": float(df["winner_score"].mean()) if len(df) else 0.0,
        "mean_exhaust_ratio": float(df["exhaust_ratio"].mean()) if len(df) else 0.0,
        "mean_residue_count": float(df["residue_count"].mean()) if len(df) else 0.0,
        "mean_slot_alignment_score": float(df["slot_alignment_score"].mean()) if len(df) else 0.0,
        "slot_gate_counts": dict(Counter(df["slot_gate_decision"])) if len(df) else {},
        "reason_counts": dict(Counter(df["reason"])) if len(df) else {},
        "profile_metrics": {},
    }

    if len(df):
        for profile, g in df.groupby("profile"):
            aggregate["profile_metrics"][str(profile)] = {
                "count": int(len(g)),
                "psi_count": int((g["state"] == "Ψ").sum()),
                "omega_count": int((g["state"] == "Ω").sum()),
                "bottom_count": int((g["state"] == "⊥").sum()),
                "psi_ratio": float((g["state"] == "Ψ").mean()),
                "omega_ratio": float((g["state"] == "Ω").mean()),
                "mean_winner_score": float(g["winner_score"].mean()),
                "mean_exhaust_ratio": float(g["exhaust_ratio"].mean()),
                "mean_slot_alignment_score": float(g["slot_alignment_score"].mean()),
                "reason_counts": dict(Counter(g["reason"])),
            }

    return aggregate, df

aggregate, summary_df = summarize(RESULTS)

bundle = {
    "run_id": RUN_ID,
    "version": "v28",
    "purpose": "compiler_root_input_induction_gate",
    "aggregate": aggregate,
    "summary": summary_df.to_dict(orient="records"),
    "results": [asdict(r) for r in RESULTS],
    "profile_thresholds": PROFILE_THRESHOLDS,
    "default_locks": DEFAULT_LOCKS,
    "interpretation_lock": {
        "main_fix": "compiler-root slot is authority; model packet is evidence",
        "v27_seam": "free model-generated induction packets became the driver",
        "v28_flow": "Q_raw -> C_root -> S_model -> G_slot -> C_Q -> B_i -> A_i -> Ψ/Ω/⊥",
        "state_policy": "max-depth unresolved residue returns Ω unless truly dead",
        "psi_rule": "Ψ requires model-origin answer, operational fit, and polysemy safety",
        "bottom_rule": "⊥ only for true dead branch: no model-origin output, repeated no-change patch, or repeated critical polysemy failure",
    },
}

bundle_out = OUT_DIR / f"{RUN_ID}_bundle.json"
summary_out = OUT_DIR / f"{RUN_ID}_summary.csv"

with open(bundle_out, "w", encoding="utf-8") as f:
    json.dump(bundle, f, indent=2, ensure_ascii=False)

summary_df.to_csv(summary_out, index=False)

print("Saved exactly two output files:")
print(bundle_out)
print(summary_out)
print()
print(json.dumps(aggregate, indent=2, ensure_ascii=False)[:5000])
display(summary_df)
```

## 16. Readout

v28 should be judged by different diagnostics than v27.

Important fields:

```text
root_source
model_packet_present
model_packet_confidence
slot_gate_decision
slot_alignment_score
accepted_contract_origin
contract_authority
state
reason
residue_count
bottom_count
```

Expected improvement:

$$
\bot_{v28} \ll \bot_{v27}
$$

because unresolved max-depth cases now remain $\Omega$ unless truly dead.

The strongest positive signal is:

$$
\Psi \text{ increases while } \bot \text{ decreases and } \Omega \text{ becomes shaped.}
$$

The most important safety signal is:

$$
\boxed{
\text{contract_authority}=\text{compiler_root}
}
$$

always.
