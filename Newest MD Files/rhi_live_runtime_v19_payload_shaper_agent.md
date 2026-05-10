# RHI Live Runtime v19 — Payload-Shaped Recursive Interface

Δ **Purpose:** v18 proved the runtime can reach real Ψ on the three core prompts with local model output, task-local gates, payload gating, and a two-file return bundle. v19 keeps that structure and adds the next missing layer: a final **payload shaper**.

v18 solved the correctness/collapse problem. v19 addresses the speaking problem:

$$
\text{winning branch payload} \rightarrow \text{final human-facing payload}
$$

The shaper does **not** choose the answer. The gates still choose the answer. The shaper compresses and clarifies the accepted payload without changing the task-local meaning.

The output contract remains exactly two files per run:

1. `RUN_ID_bundle.json` — complete results, traces, raw winner, shaped answer, model/device status.
2. `RUN_ID_summary.csv` — compact table for quick inspection.

Core correction:

$$
\Psi_{\text{correct}} \rightarrow \Psi_{\text{readable}}
$$


```python

from __future__ import annotations

import os
import sys
import subprocess
import importlib.util
import re
import json
import math
import uuid
import random
import traceback
from dataclasses import dataclass, asdict, field
from pathlib import Path
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

ROOT = Path.cwd()
OUT_DIR = ROOT / "rhi_v19_outputs"
OUT_DIR.mkdir(exist_ok=True)

RUN_ID = "rhi_v19_" + uuid.uuid4().hex[:10]
SEED = 7
random.seed(SEED)
np.random.seed(SEED)

print("ROOT:", ROOT)
print("OUT_DIR:", OUT_DIR)
print("RUN_ID:", RUN_ID)
```


```python
# Runtime configuration.

MODEL_ID_OR_PATH = os.environ.get("RHI_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")

LOAD_REAL_MODEL = True
REQUIRE_MODEL_FOR_PSI = True

MAX_NEW_TOKENS = 360
TEMPERATURE = 0.30
TOP_P = 0.88
MAX_RECURSION_DEPTH = 2

# v19 final payload shaper. The resolver still decides; the shaper only compresses the accepted payload.
ENABLE_PAYLOAD_SHAPER = True
SHAPER_MAX_NEW_TOKENS = 220
SHAPER_SAMPLE = False

SHAPER_WORD_BUDGET_BY_PROFILE = {
    "runtime_contract": 180,
    "memory_trace": 150,
    "inverse_retrieval": 160,
    "general": 150,
}

# v18 preflight: install missing protobuf/sentencepiece before model load when possible.
AUTO_INSTALL_MISSING_DEPS = True

# Base gates. v17 applies several of these through task-local profiles.
PSI_MIN = 0.58
MARGIN_MIN = 0.045
PROMPT_FIT_MIN = 0.28
TRACE_MIN = 0.45
POLYSEMY_MIN = 0.30

# Task-local quality thresholds.
QUALITY_MIN_BY_PROFILE = {
    "runtime_contract": 0.42,
    "memory_trace": 0.34,
    "inverse_retrieval": 0.34,
    "general": 0.34,
}

CONTRACT_ECHO_MAX = 0.18
SCHEMA_ECHO_MAX = 0.25
LEGAL_TRAP_MAX = 0.04
LITERAL_SHAPE_TRAP_MAX = 0.04

CONSENSUS_SCORE_MIN = 0.58
CONSENSUS_AUDIT_MIN = 0.80
CONSENSUS_PAYLOAD_MIN = 0.70

print("MODEL_ID_OR_PATH:", MODEL_ID_OR_PATH)
print("LOAD_REAL_MODEL:", LOAD_REAL_MODEL)
print("REQUIRE_MODEL_FOR_PSI:", REQUIRE_MODEL_FOR_PSI)
print("AUTO_INSTALL_MISSING_DEPS:", AUTO_INSTALL_MISSING_DEPS)
print("ENABLE_PAYLOAD_SHAPER:", ENABLE_PAYLOAD_SHAPER)
```


```python

# Robust model loading and generation.
# Uses rendered chat-template string -> tokenizer(...) -> model.generate(**inputs).

tokenizer = None
model = None
MODEL_READY = False
MODEL_GENERATION_READY = False
MODEL_ERROR = None
DEVICE_INFO = {}


def _module_available(module_name: str) -> bool:
    """Robust dependency probe.

    importlib.util.find_spec("google.protobuf") can raise ModuleNotFoundError
    when the parent namespace package `google` is absent. That was the v18.0
    preflight tear. Use import_module and catch the missing-parent case.
    """
    try:
        importlib.import_module(module_name)
        return True
    except ModuleNotFoundError:
        return False
    except Exception:
        # If the module exists but fails while importing, fall back to find_spec.
        # Guard find_spec too, because dotted modules can still raise on parent import.
        try:
            return importlib.util.find_spec(module_name) is not None
        except ModuleNotFoundError:
            return False
        except Exception:
            return False


def ensure_runtime_dependencies() -> Dict[str, Any]:
    """Install/check tokenizer dependencies before loading the model.

    v17 exposed a real environment tear: protobuf was missing, so the model never loaded.
    v18.1 fixes the preflight itself: missing `google` must be handled as
    "protobuf missing," not as a notebook-crashing exception.
    """
    status = {
        "checked": True,
        "attempted_install": False,
        "missing_before": [],
        "missing_after": [],
        "errors": [],
    }
    required = [("google.protobuf", "protobuf"), ("sentencepiece", "sentencepiece")]

    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_before"].append(pip_name)

    if status["missing_before"] and AUTO_INSTALL_MISSING_DEPS:
        status["attempted_install"] = True
        try:
            cmd = [sys.executable, "-m", "pip", "install", "-U"] + status["missing_before"]
            print("Installing missing model dependencies:", " ".join(status["missing_before"]))
            subprocess.check_call(cmd)
            importlib.invalidate_caches()
        except Exception as e:
            status["errors"].append("".join(traceback.format_exception_only(type(e), e)).strip())

    for module_name, pip_name in required:
        if not _module_available(module_name):
            status["missing_after"].append(pip_name)

    return status

DEPENDENCY_STATUS = ensure_runtime_dependencies()
print("DEPENDENCY_STATUS:", DEPENDENCY_STATUS)

def infer_model_device():
    import torch
    if model is None:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    try:
        return next(model.parameters()).device
    except Exception:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

def move_batch_to_device(batch, device):
    moved = {}
    for k, v in batch.items():
        if hasattr(v, "to"):
            moved[k] = v.to(device)
        else:
            moved[k] = v
    return moved

def try_load_model(model_id_or_path: str) -> bool:
    global tokenizer, model, MODEL_READY, MODEL_ERROR, DEVICE_INFO

    if not LOAD_REAL_MODEL:
        MODEL_ERROR = "LOAD_REAL_MODEL=False"
        print("Model loading disabled.")
        return False

    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        DEVICE_INFO["dependency_status"] = DEPENDENCY_STATUS
        DEVICE_INFO["torch_version"] = torch.__version__
        DEVICE_INFO["cuda_available"] = bool(torch.cuda.is_available())
        DEVICE_INFO["device_count"] = int(torch.cuda.device_count())
        if torch.cuda.is_available():
            DEVICE_INFO["gpu_name"] = torch.cuda.get_device_name(0)
            DEVICE_INFO["cuda_version"] = torch.version.cuda

        print("Torch/CUDA:", DEVICE_INFO)

        tokenizer = AutoTokenizer.from_pretrained(model_id_or_path, trust_remote_code=True)
        if tokenizer.pad_token_id is None and tokenizer.eos_token is not None:
            tokenizer.pad_token = tokenizer.eos_token

        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        kwargs = dict(
            trust_remote_code=True,
            device_map="auto" if torch.cuda.is_available() else None,
            low_cpu_mem_usage=True,
        )

        try:
            model = AutoModelForCausalLM.from_pretrained(model_id_or_path, dtype=dtype, **kwargs)
        except TypeError:
            model = AutoModelForCausalLM.from_pretrained(model_id_or_path, torch_dtype=dtype, **kwargs)

        if not torch.cuda.is_available():
            model.to(torch.device("cpu"))

        model.eval()
        MODEL_READY = True
        MODEL_ERROR = None
        print("MODEL_READY:", MODEL_READY)
        print("INFER_DEVICE:", infer_model_device())
        return True

    except Exception as e:
        MODEL_READY = False
        MODEL_ERROR = "".join(traceback.format_exception_only(type(e), e)).strip()
        print("MODEL LOAD FAILED.")
        print(MODEL_ERROR)
        return False

def render_messages(messages: List[Dict[str, str]]) -> str:
    if hasattr(tokenizer, "apply_chat_template"):
        try:
            rendered = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
            if isinstance(rendered, str) and rendered.strip():
                return rendered
        except Exception as e:
            print("apply_chat_template string render failed; using manual template:", type(e).__name__, e)

    parts = []
    for m in messages:
        role = str(m.get("role", "user")).upper()
        content = str(m.get("content", ""))
        parts.append(f"{role}:\n{content}")
    parts.append("ASSISTANT:\n")
    return "\n\n".join(parts)

def raw_model_generate(messages: List[Dict[str, str]], max_new_tokens: int = 80, sample: bool = False) -> str:
    import torch
    if not MODEL_READY:
        raise RuntimeError("Model is not loaded.")

    device = infer_model_device()
    rendered = render_messages(messages)
    inputs = tokenizer(rendered, return_tensors="pt")
    inputs = move_batch_to_device(inputs, device)

    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        pad_token_id=tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    if sample:
        gen_kwargs.update(dict(do_sample=True, temperature=TEMPERATURE, top_p=TOP_P))
    else:
        gen_kwargs.update(dict(do_sample=False))

    with torch.no_grad():
        out = model.generate(**inputs, **gen_kwargs)

    input_len = inputs["input_ids"].shape[-1]
    gen = out[0][input_len:]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()

_ = try_load_model(MODEL_ID_OR_PATH)

try:
    smoke = raw_model_generate([
        {"role": "system", "content": "You are a runtime smoke test."},
        {"role": "user", "content": "Reply with one short sentence containing the word READY."},
    ], max_new_tokens=40, sample=False)
    MODEL_GENERATION_READY = bool(smoke.strip())
    print("MODEL_GENERATION_READY:", MODEL_GENERATION_READY)
    print("SMOKE:", smoke)
except Exception as e:
    MODEL_GENERATION_READY = False
    MODEL_ERROR = "".join(traceback.format_exception_only(type(e), e)).strip()
    print("MODEL GENERATION FAILED.")
    print(MODEL_ERROR)
    print(traceback.format_exc())
```


```python

# Text utilities and anti-echo gates.

STOPWORDS = {
    "the","a","an","and","or","but","if","then","else","of","to","in","on","for","with","by","as",
    "is","are","was","were","be","being","been","it","this","that","these","those","from","at",
    "into","out","about","so","because","therefore","than","not","no","yes","do","does","did",
    "can","could","should","would","will","just","they","them","their","you","your","we","our",
    "i","me","my","he","she","his","her","its","what","how","why","when"
}

NEXUS_SURFACE_TERMS = {
    "nexus","contract","carrier","domain","boundary","collapse","shape","value","slot","need",
    "forbidden","neighbor","operational","recursive","recursion","krrb","omega","psi","field",
    "fold","runtime","phase","lock","audit","trace","signal","evidence","branch","repair",
    "candidate","construct","verify","counter","prompt","polysemy"
}

CONTRACT_ECHO_MARKERS = [
    "prompt:", "inverse need:", "preserved function:", "boundary conditions:",
    "domain carrier:", "forbidden neighbors:", "polysemy lock:", "collapse target:",
    "repair history:", "active_templates", "required_meaning", "forbidden_meaning",
    "clean_prompt", "semantic trap", "model origin", "runtime-contract fit"
]

SCHEMA_ECHO_MARKERS = [
    "precondition:", "postcondition:", "success criteria:", "failure criteria:",
    "allowed side effects:", "rollback mechanism:", "runtime path:", "corrected runtime path:",
    "repair target:", "need-slot contract:"
]

LEGAL_TRAP_TERMS = [
    "legal", "legally", "law", "liability", "stakeholder", "stakeholders",
    "signed", "binding agreement", "parties", "compliance", "enforceable",
    "contractual obligations", "breach", "confidentiality"
]

LITERAL_SHAPE_TRAP_TERMS = ["circle", "sphere", "oval", "ellipse", "round object", "visual characteristics"]

def words(text: str, remove_nexus_surface: bool = False) -> List[str]:
    toks = re.findall(r"[a-zA-Z0-9_ΔΨΩ⊕↻⊥]+", str(text).lower())
    toks = [t for t in toks if t not in STOPWORDS and len(t) > 1]
    if remove_nexus_surface:
        toks = [t for t in toks if t not in NEXUS_SURFACE_TERMS]
    return toks

def wordset(text: str, remove_nexus_surface: bool = False) -> set:
    return set(words(text, remove_nexus_surface=remove_nexus_surface))

def jaccard_text(a: str, b: str, remove_nexus_surface: bool = False) -> float:
    wa, wb = wordset(a, remove_nexus_surface), wordset(b, remove_nexus_surface)
    if not wa and not wb:
        return 1.0
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / max(1, len(wa | wb))

def contains_any(text: str, terms: List[str]) -> bool:
    s = str(text).lower()
    return any(str(t).lower() in s for t in terms)

def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))

def harmonic_mean(vals: List[float], eps: float = 1e-9) -> float:
    vals = [max(eps, float(v)) for v in vals]
    return len(vals) / sum(1.0 / v for v in vals)

def field_hit_score(text: str, field_terms: List[str], max_terms: int = 10) -> float:
    if not field_terms:
        return 0.5
    s = str(text).lower()
    uniq = []
    for t in field_terms:
        t = str(t).lower().strip()
        if t and t not in uniq:
            uniq.append(t)
    uniq = uniq[:max_terms]
    hits = sum(1 for term in uniq if term in s)
    return clamp(hits / max(1, len(uniq)))

def marker_penalty(text: str, markers: List[str], scale: int = 6) -> float:
    s = str(text).lower()
    hits = sum(1 for m in markers if m in s)
    return clamp(hits / max(1, scale))

def contract_echo_penalty(text: str) -> float:
    s = str(text).lower()
    marker = marker_penalty(s, CONTRACT_ECHO_MARKERS, scale=5)
    jsonish = 0.20 if ("{" in s and "}" in s and ":" in s) else 0.0
    long_label_block = 0.25 if len(re.findall(r"\*\*[^*]+:\*\*", str(text))) >= 4 else 0.0
    return clamp(marker + jsonish + long_label_block)

def schema_echo_penalty(text: str) -> float:
    return marker_penalty(str(text).lower(), SCHEMA_ECHO_MARKERS, scale=5)

def legal_trap_penalty(text: str) -> float:
    s = str(text).lower()
    hits = sum(1 for t in LEGAL_TRAP_TERMS if t in s)
    return clamp(hits / 5)

def literal_shape_trap_penalty(prompt: str, answer: str) -> float:
    p = prompt.lower()
    if "shape-first retrieval" not in p:
        return 0.0
    s = answer.lower()
    hits = sum(1 for t in LITERAL_SHAPE_TRAP_TERMS if t in s)
    return clamp(hits / 2)

def payload_text(answer: str) -> str:
    # Strip obvious spec recitation blocks. The remaining text is the payload we score for solution quality.
    lines = str(answer).splitlines()
    kept = []
    skip_markers = tuple(m.replace(":", "").lower() for m in CONTRACT_ECHO_MARKERS + SCHEMA_ECHO_MARKERS)
    for line in lines:
        cleaned = line.strip().strip("*# ").lower().replace("**", "")
        if any(cleaned.startswith(m) for m in skip_markers):
            continue
        if "{" in line and "}" in line and ":" in line:
            continue
        kept.append(line)
    return "\n".join(kept).strip() or str(answer).strip()
```


```python
# Shape templates, task profiles, and contract.

# v17 correction: template detection is no longer naive substring OR.
# "agent" alone must not activate CONTRACT or TOOL. It was causing memory prompts
# to inherit the runtime-contract/polysemy channel.
SHAPE_TEMPLATES = {
    "CONTRACT": {"needs": ["runtime", "precondition", "postcondition", "success", "failure", "rollback", "trace"]},
    "GROOVE": {"needs": ["adapter", "low-rank", "weights", "delta", "dataset", "loss", "eval"]},
    "SEARCH": {"needs": ["inverse", "fit", "candidate", "rank", "verify", "evidence"]},
    "REPAIR": {"needs": ["failure", "cause", "patch", "test", "rerun", "trace"]},
    "MEMORY": {"needs": ["state", "trace", "retrieve", "preserve", "update", "continuity"]},
    "BOUNDARY": {"needs": ["boundary", "reject", "constraint", "preserve", "violate", "gate"]},
    "RECURSE": {"needs": ["recursive", "branch", "feedback", "repair", "collapse", "omega"]},
    "TOOL": {"needs": ["tool", "input", "output", "side-effect", "verify"]},
}

@dataclass
class NeedSlotContract:
    prompt: str
    clean_prompt: str
    active_templates: List[str]
    task_profile: str
    inverse_need: str
    preserved_function: str
    boundary_conditions: List[str]
    domain_carrier: List[str]
    forbidden_neighbors: List[str]
    polysemy_lock: Dict[str, Dict[str, str]]
    collapse_target: str
    repair_history: List[Dict[str, Any]] = field(default_factory=list)


def clean_prompt_text(prompt: str) -> str:
    # Do not let repair instructions become the user domain.
    lines = []
    for line in str(prompt).splitlines():
        if line.strip().lower().startswith("repair target:"):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def detect_shape_template(prompt: str) -> List[str]:
    p = str(prompt).lower()
    active = []

    # Explicit runtime-contract/tool intent only.
    contract_hit = (
        "contract" in p or
        "precondition" in p or "postcondition" in p or
        "success criteria" in p or "failure criteria" in p or
        ("tool" in p and any(x in p for x in ["before", "intent", "side effect", "rollback", "trace", "call", "use"]))
    )
    if contract_hit:
        active.append("CONTRACT")

    tool_hit = any(x in p for x in ["tool", "api", "function call", "tool call", "execute", "external function"])
    if tool_hit:
        active.append("TOOL")

    if any(x in p for x in ["search", "retrieve", "retrieval", "find", "query", "lookup", "index", "rag"]):
        active.append("SEARCH")
    if any(x in p for x in ["train", "lora", "qlora", "adapter", "fine tune", "weights", "groove", "model"]):
        active.append("GROOVE")
    if any(x in p for x in ["fix", "repair", "error", "failed", "broken", "bug", "traceback", "syntaxerror", "nameerror"]):
        active.append("REPAIR")
    if any(x in p for x in ["remember", "memory", "recall", "lost", "state", "context", "continuity"]):
        active.append("MEMORY")
    if any(x in p for x in ["boundary", "limit", "forbidden", "constraint", "safety", "gate", "reject"]):
        active.append("BOUNDARY")
    if any(x in p for x in ["recursive", "recursion", "again", "loop", "fold", "iterate", "turn"]):
        active.append("RECURSE")

    # De-duplicate while preserving order.
    out = []
    for x in active:
        if x not in out:
            out.append(x)
    return out or ["GENERAL"]


def infer_task_profile(active: List[str]) -> str:
    a = set(active)
    if "CONTRACT" in a or "TOOL" in a:
        return "runtime_contract"
    if "MEMORY" in a:
        return "memory_trace"
    if "SEARCH" in a:
        return "inverse_retrieval"
    return "general"


def requires_polysemy_lock(contract_or_active) -> bool:
    active = contract_or_active.active_templates if hasattr(contract_or_active, "active_templates") else contract_or_active
    a = set(active)
    return "CONTRACT" in a or "TOOL" in a


def shape_mass(text: str, active_templates: List[str]) -> Dict[str, float]:
    masses = {}
    for name in active_templates:
        if name == "GENERAL":
            continue
        needs = SHAPE_TEMPLATES[name]["needs"]
        masses[name] = sum(1 for n in needs if n.lower() in str(text).lower()) / max(1, len(needs))
    if not masses:
        masses["GENERAL"] = 0.5
    return masses


def shape_score(text: str, active_templates: List[str]) -> float:
    masses = shape_mass(text, active_templates)
    return clamp(sum(masses.values()) / max(1, len(masses)))


def extract_domain_terms(prompt: str, max_terms: int = 14) -> List[str]:
    ws = words(clean_prompt_text(prompt), remove_nexus_surface=True)
    counts = Counter(ws)
    return [w for w, _ in counts.most_common(max_terms)]


def infer_forbidden_neighbors(active: List[str]) -> List[str]:
    forb = set()
    if "TOOL" in active or "CONTRACT" in active:
        forb.update(["tool-first action", "premature execution", "api reflex", "surface task completion"])
        forb.update(["legal contract interpretation", "binding agreement interpretation", "stakeholder/legal framing"])
    if "GROOVE" in active:
        forb.update(["full retrain reflex", "weight churn", "dataset worship", "loss-only tuning"])
    if "SEARCH" in active:
        forb.update(["noun lookup", "keyword matching", "unverified retrieval", "search without verifier", "literal shape example"])
    if "REPAIR" in active:
        forb.update(["blanket rewrite", "threshold fiddling", "silent failure", "patch without test"])
    if "MEMORY" in active:
        forb.update(["stateless answer", "context amnesia", "surface recall", "summary as memory", "precondition checklist as explanation"])
    if "BOUNDARY" in active:
        forb.update(["unsafe override", "constraint erasure", "boundary confusion"])
    if "RECURSE" in active:
        forb.update(["linear pipeline", "single branch", "dead loop", "nested sweep masquerading as recursion"])
    if not forb:
        forb.update(["surface label", "generic explanation", "noun-only answer"])
    return sorted(forb)


def build_contract(prompt: str, repair_history: Optional[List[Dict[str, Any]]] = None) -> NeedSlotContract:
    clean = clean_prompt_text(prompt)
    active = detect_shape_template(clean)
    profile = infer_task_profile(active)
    domain_terms = extract_domain_terms(clean)

    inverse_need = "construct the missing operational slot implied by the prompt; answer directly; reject wrong semantic carriers"

    preserved = []
    if profile == "runtime_contract":
        preserved.append("form a runtime execution contract before tool use")
    if "GROOVE" in active:
        preserved.append("shape model behavior through low-rank update without overwriting the base model")
    if profile == "inverse_retrieval":
        preserved.append("retrieve by inverse operational fit when no noun match exists")
    if "REPAIR" in active:
        preserved.append("repair the failed dimension and rerun")
    if profile == "memory_trace":
        preserved.append("preserve trace continuity across turns rather than compressing state into summary text")
    if "RECURSE" in active:
        preserved.append("branch recursively until Ψ collapse or Ω residue")
    if not preserved:
        preserved.append("preserve the prompt's verb-level operation")

    boundaries = [
        "answer the user prompt directly; do not print the internal contract/spec",
        "do not collapse on shared framework vocabulary alone",
        "require answer origin from the real model when model mode is enabled",
        "require prompt-grounded evidence for the selected answer",
        "prefer Ω over false Ψ when top branches disagree operationally",
        "preserve base answer when controller evidence is weak",
    ]
    if profile == "runtime_contract":
        boundaries.insert(1, "contract means runtime execution contract, not legal agreement")
        boundaries.insert(4, "reject legal-contract/stakeholder/liability framing unless explicitly negated")
    if profile == "inverse_retrieval":
        boundaries.append("shape means operational fit/inverse need, not literal circles/spheres unless explicitly requested")
    if profile == "memory_trace":
        boundaries.append("memory means causal trace continuity, not a text summary or precondition checklist")

    if profile == "runtime_contract":
        polysemy_lock = {
            "contract": {
                "required_meaning": "runtime execution contract: preconditions, postconditions, success criteria, failure criteria, allowed side effects, rollback, trace update",
                "forbidden_meaning": "legal/binding agreement between parties, stakeholders, liability, compliance, signed contract",
            },
            "tool": {
                "required_meaning": "external function/API/action channel with side effects",
                "forbidden_meaning": "generic physical implement unless the prompt asks for physical tools",
            },
        }
    else:
        polysemy_lock = {}

    return NeedSlotContract(
        prompt=prompt,
        clean_prompt=clean,
        active_templates=active,
        task_profile=profile,
        inverse_need=inverse_need,
        preserved_function="; ".join(preserved),
        boundary_conditions=boundaries,
        domain_carrier=domain_terms,
        forbidden_neighbors=infer_forbidden_neighbors(active),
        polysemy_lock=polysemy_lock,
        collapse_target="one executable answer with model origin, direct payload, task-local fit, prompt grounding, semantic trap rejection, and trace sufficient to debug",
        repair_history=repair_history or [],
    )


def contract_field_terms(contract: NeedSlotContract) -> Dict[str, List[str]]:
    if contract.polysemy_lock:
        poly_terms = words(" ".join(v["required_meaning"] for v in contract.polysemy_lock.values()), remove_nexus_surface=True)
    else:
        # Task-local neutral channel: use the preserved function/domain rather than contract/tool polysemy.
        poly_terms = words(contract.preserved_function, remove_nexus_surface=True) + contract.domain_carrier
    return {
        "need": words(contract.inverse_need, remove_nexus_surface=True),
        "function": words(contract.preserved_function, remove_nexus_surface=True),
        "boundary": words(" ".join(contract.boundary_conditions), remove_nexus_surface=True),
        "domain": contract.domain_carrier,
        "forbidden": words(" ".join(contract.forbidden_neighbors), remove_nexus_surface=True),
        "collapse": words(contract.collapse_target, remove_nexus_surface=True),
        "polysemy_required": poly_terms,
    }


def repair_guidance(repair_history: List[Dict[str, Any]]) -> str:
    if not repair_history:
        return "No prior repair. Answer directly."
    last = repair_history[-1]
    weak = last.get("weakest_observable", "unknown")
    if weak == "contract_echo":
        return "Previous answer echoed the internal spec. Do not print prompt/contract fields; give only the answer payload."
    if weak == "legal_trap":
        return "Previous answer drifted toward legal-contract language. Use runtime/API/tool-call semantics only."
    if weak == "literal_shape":
        return "Previous answer used literal circles/spheres. Treat shape as operational fit, not geometry nouns."
    if weak == "quality":
        return "Previous answer was thin. Add the missing mechanism and a concrete test condition."
    if weak == "margin":
        return "Top branches were close. Make the operational stance explicit in one compact answer."
    if weak == "polysemy_lock":
        return "Previous answer was judged against a semantic lock. Answer the active task directly and avoid wrong carrier meanings."
    return f"Repair only failed dimension: {weak}."
```


```python
# Candidate generation. v17 gives the model compact task-local instructions, not the whole contract object.

BRANCH_SYSTEMS = {
    "construct": "Constructor branch. Answer the user's prompt directly from the missing operation. Do not print internal contract fields.",
    "verify": "Verifier branch. Give the answer only if it preserves the operation and rejects the wrong carrier.",
    "repair": "Repair branch. Patch the weakest observable only. Do not recite the audit/spec.",
    "counter": "Counter branch. Name the wrong path briefly, then provide the corrected answer.",
}

def deterministic_branch(prompt: str, contract: NeedSlotContract, branch_name: str, reason: str = "fallback") -> Dict[str, Any]:
    text = f"Diagnostic fallback for {branch_name}. This is not a model answer."
    return {"branch": branch_name, "answer": text, "origin": reason, "generation_error": MODEL_ERROR}


def meaning_lock_instruction(contract: NeedSlotContract) -> str:
    if contract.task_profile == "runtime_contract":
        return (
            '- "contract" means runtime execution contract for an agent/tool call, not a legal agreement.\n'
            '- "tool" means external function/API/action channel with side effects.\n'
        )
    if contract.task_profile == "inverse_retrieval":
        return '- "shape" means operational fit/inverse need, not a literal visual circle/sphere.\n'
    if contract.task_profile == "memory_trace":
        return '- "memory" means live causal trace continuity across state transitions, not a text summary.\n'
    return '- Preserve the verb-level operation requested by the prompt.\n'


def task_style_instruction(contract: NeedSlotContract) -> str:
    if contract.task_profile == "inverse_retrieval":
        return (
            "Give a concrete retrieval algorithm in 4-6 steps. "
            "Use operational-fit language: need vector, inverse cavity, candidate generation, ranking, verifier. "
            "Do not choose a literal shape like circle or sphere."
        )
    if contract.task_profile == "memory_trace":
        return (
            "Explain memory as a live causal/event trace: state transitions, tool calls, observations, decisions, rollback, and update continuity. "
            "Do not answer as a precondition/postcondition checklist."
        )
    if contract.task_profile == "runtime_contract":
        return (
            "Explain runtime execution contracts for tool calls: preconditions, allowed side effects, success/failure criteria, rollback, and trace update. "
            "Do not use legal/stakeholder/binding-agreement framing."
        )
    return "Give a compact direct answer with a concrete mechanism and one test condition."


def model_generate_one(prompt: str, contract: NeedSlotContract, branch_name: str) -> Dict[str, Any]:
    if not MODEL_GENERATION_READY:
        return deterministic_branch(prompt, contract, branch_name, reason="fallback_model_not_ready")

    required_terms = ", ".join(contract.domain_carrier[:8])
    repair = repair_guidance(contract.repair_history)

    user = f"""
USER PROMPT:
{contract.clean_prompt}

TASK PROFILE:
{contract.task_profile}

MEANING LOCK:
{meaning_lock_instruction(contract)}
PRESERVED FUNCTION:
{contract.preserved_function}

REPAIR GUIDANCE:
{repair}

ANSWER MODE:
{task_style_instruction(contract)}

HARD RULES:
1. Do not print the internal spec, field names, JSON, Prompt/Inverse Need/Boundary Conditions/Polysemy Lock, or Repair History.
2. Give only the answer payload.
3. Use at least two prompt-domain terms: {required_terms}
4. Avoid checklist form unless the user asks for a checklist.
"""

    messages = [
        {"role": "system", "content": BRANCH_SYSTEMS[branch_name]},
        {"role": "user", "content": user},
    ]

    try:
        text = raw_model_generate(messages, max_new_tokens=MAX_NEW_TOKENS, sample=True)
        if not text.strip():
            return deterministic_branch(prompt, contract, branch_name, reason="fallback_empty_generation")
        return {"branch": branch_name, "answer": text.strip(), "origin": "model", "generation_error": None}
    except Exception as e:
        err = "".join(traceback.format_exception_only(type(e), e)).strip()
        return {**deterministic_branch(prompt, contract, branch_name, reason="fallback_error"), "generation_error": err}


def generate_candidates(prompt: str, contract: NeedSlotContract) -> List[Dict[str, Any]]:
    return [model_generate_one(prompt, contract, b) for b in BRANCH_SYSTEMS]
```


```python
# Operational audit, payload scoring, direct gate, consensus gate.


def task_quality_hmean(contract: NeedSlotContract, audit: Dict[str, Any]) -> float:
    profile = contract.task_profile
    if profile == "runtime_contract":
        dims = [audit["F_need"], audit["F_function"], audit["F_boundary"], audit["F_trap"], audit["F_collapse"], audit["F_polysemy"]]
    elif profile == "memory_trace":
        # Memory answers should not be punished for not discussing runtime-contract boundaries.
        dims = [audit["F_need"], audit["F_function"], audit["F_collapse"], audit["F_shape"], audit["F_prompt"]]
    elif profile == "inverse_retrieval":
        # Retrieval answers must preserve inverse fit and avoid noun/literal-shape traps.
        dims = [audit["F_need"], audit["F_function"], audit["F_trap"], audit["F_collapse"], audit["F_shape"], audit["F_prompt"]]
    else:
        dims = [audit["F_need"], audit["F_function"], audit["F_collapse"], audit["F_prompt"]]
    return harmonic_mean(dims)


def answer_operational_audit(prompt: str, contract: NeedSlotContract, answer: str, origin: str) -> Dict[str, Any]:
    active = contract.active_templates
    fields = contract_field_terms(contract)
    payload = payload_text(answer)
    a = payload.lower()

    F_need = clamp(0.50 * field_hit_score(payload, fields["need"]) + 0.50 * field_hit_score(payload, fields["domain"]))
    F_function = clamp(
        0.65 * field_hit_score(payload, fields["function"]) +
        0.35 * sum([
            contains_any(a, ["preserve", "maintain", "function", "operation", "before", "after", "continuity", "inverse", "fit"]),
            contains_any(a, ["execute", "candidate", "select", "verify", "state", "update", "rollback", "rank", "retrieve"]),
        ]) / 2
    )
    F_boundary = clamp(
        0.55 * field_hit_score(payload, fields["boundary"]) +
        0.45 * sum([
            contains_any(a, ["boundary", "constraint", "gate", "reject", "protect", "forbidden", "precondition", "postcondition"]),
            contains_any(a, ["false", "wrong", "weak", "premature", "surface", "side effect", "rollback"]),
        ]) / 2
    )
    forbidden_hit = field_hit_score(payload, fields["forbidden"])
    trap_language = sum([
        contains_any(a, ["not", "instead", "wrong", "fails", "reject", "avoid", "forbidden"]),
        contains_any(a, ["tool-first", "surface", "generic", "noun", "keyword", "literal", "exact match"]),
    ]) / 2
    F_trap = clamp(0.45 * forbidden_hit + 0.55 * trap_language)

    F_collapse = clamp(
        0.45 * field_hit_score(payload, fields["collapse"]) +
        0.55 * sum([
            contains_any(a, ["because", "therefore", "so", "result", "answer"]),
            contains_any(a, ["one", "single", "executable", "run", "test", "trace", "step", "algorithm"]),
        ]) / 2
    )

    F_shape = shape_score(payload, active)
    F_prompt = field_hit_score(payload, words(contract.clean_prompt, remove_nexus_surface=True), max_terms=12)

    if requires_polysemy_lock(contract):
        F_polysemy = field_hit_score(payload, fields["polysemy_required"], max_terms=12)
    else:
        # Neutral unless the task actually invokes contract/tool polysemy.
        F_polysemy = 1.0

    C_echo = contract_echo_penalty(answer)
    S_echo = schema_echo_penalty(answer)
    L_trap = legal_trap_penalty(answer) if requires_polysemy_lock(contract) else 0.0
    Literal_shape = literal_shape_trap_penalty(contract.clean_prompt, answer)

    O_model = 1.0 if origin == "model" else 0.0

    hot = clamp((F_need + F_function + F_shape + F_prompt + F_polysemy) / 5)
    cold = clamp((F_boundary + F_trap + F_collapse + (1.0 - L_trap) + (1.0 - C_echo)) / 5)
    hotcold_balance = clamp(1.0 - abs(hot - cold))

    base_audit = {
        "F_need": F_need,
        "F_function": F_function,
        "F_boundary": F_boundary,
        "F_trap": F_trap,
        "F_collapse": F_collapse,
        "F_shape": F_shape,
        "F_prompt": F_prompt,
        "F_polysemy": F_polysemy,
        "contract_echo_penalty": C_echo,
        "schema_echo_penalty": S_echo,
        "legal_trap_penalty": L_trap,
        "literal_shape_trap_penalty": Literal_shape,
        "payload_validity": 0.0,
        "hot": hot,
        "cold": cold,
        "hotcold_balance": hotcold_balance,
        "quality_hmean": 0.0,
        "quality_mean": 0.0,
        "O_model": O_model,
        "payload_text": payload,
    }

    quality = task_quality_hmean(contract, base_audit)
    mean_quality = float(np.mean([F_need, F_function, F_boundary, F_trap, F_collapse]))

    payload_validity = clamp(
        1.0
        - 0.45 * C_echo
        - 0.25 * S_echo
        - 0.20 * L_trap
        - 0.20 * Literal_shape
    )

    base_audit.update({
        "payload_validity": payload_validity,
        "quality_hmean": quality,
        "quality_mean": mean_quality,
    })
    return base_audit


def trace_sufficiency(answer: str, audit: Dict[str, Any], contract: NeedSlotContract) -> float:
    payload = audit["payload_text"].lower()
    profile = contract.task_profile

    if profile == "memory_trace":
        evidence_bits = [
            contains_any(payload, ["trace", "continuity", "state", "transition", "event", "tool call", "observation", "decision", "update"]),
            contains_any(payload, ["rather than", "not", "instead", "summary", "compress"]),
            field_hit_score(payload, contract.domain_carrier, max_terms=8) >= 0.25,
            audit["quality_hmean"] >= QUALITY_MIN_BY_PROFILE[profile],
            audit["payload_validity"] >= 0.75,
            audit["O_model"] >= 1.0,
        ]
    elif profile == "inverse_retrieval":
        evidence_bits = [
            contains_any(payload, ["inverse", "need", "candidate", "rank", "verify", "retrieval", "noun", "match"]),
            contains_any(payload, ["algorithm", "step", "select", "score", "fit"]),
            field_hit_score(payload, contract.domain_carrier, max_terms=8) >= 0.25,
            audit["quality_hmean"] >= QUALITY_MIN_BY_PROFILE[profile],
            audit["payload_validity"] >= 0.75,
            audit["O_model"] >= 1.0,
        ]
    else:
        evidence_bits = [
            contains_any(payload, ["because", "therefore", "so", "why", "fails"]),
            contains_any(payload, ["precondition", "postcondition", "success", "failure", "rollback", "trace", "state", "candidate", "verify"]),
            field_hit_score(payload, contract.domain_carrier, max_terms=8) >= 0.25,
            audit["quality_hmean"] >= QUALITY_MIN_BY_PROFILE.get(profile, QUALITY_MIN_BY_PROFILE["general"]),
            audit["payload_validity"] >= 0.75,
            audit["O_model"] >= 1.0,
        ]
    return clamp(sum(evidence_bits) / len(evidence_bits))


def branch_score(prompt: str, contract: NeedSlotContract, branch: Dict[str, Any]) -> Dict[str, Any]:
    answer = branch["answer"]
    origin = branch.get("origin", "unknown")
    audit = answer_operational_audit(prompt, contract, answer, origin)
    fields = contract_field_terms(contract)

    payload = audit["payload_text"]
    stance_terms = [
        field_hit_score(payload, fields["need"]),
        field_hit_score(payload, fields["function"]),
        field_hit_score(payload, fields["domain"]),
        field_hit_score(payload, fields["collapse"]),
    ]
    if requires_polysemy_lock(contract):
        stance_terms.append(field_hit_score(payload, fields["polysemy_required"]))
    contract_stance = float(np.mean(stance_terms))
    trace = trace_sufficiency(answer, audit, contract)

    poly_weight = 0.12 if requires_polysemy_lock(contract) else 0.00
    redistributed = 0.12 - poly_weight

    score = clamp(
        0.26 * audit["quality_hmean"] +
        0.18 * contract_stance +
        (0.14 + redistributed/2) * audit["F_prompt"] +
        poly_weight * audit["F_polysemy"] +
        0.12 * trace +
        (0.10 + redistributed/2) * audit["payload_validity"] +
        0.06 * audit["hotcold_balance"] +
        0.04 * audit["O_model"]
    )

    return {
        **branch,
        "score": score,
        "contract_stance": contract_stance,
        "trace_sufficiency": trace,
        "audit": audit,
    }


def score_candidates(prompt: str, contract: NeedSlotContract, candidates: List[Dict[str, Any]]) -> pd.DataFrame:
    rows = [branch_score(prompt, contract, c) for c in candidates]
    flat = []
    for r in rows:
        a = r["audit"]
        flat.append({
            "branch": r["branch"],
            "origin": r.get("origin"),
            "score": r["score"],
            "task_profile": contract.task_profile,
            "contract_stance": r["contract_stance"],
            "trace_sufficiency": r["trace_sufficiency"],
            "quality_hmean": a["quality_hmean"],
            "F_need": a["F_need"],
            "F_function": a["F_function"],
            "F_boundary": a["F_boundary"],
            "F_trap": a["F_trap"],
            "F_collapse": a["F_collapse"],
            "F_shape": a["F_shape"],
            "F_prompt": a["F_prompt"],
            "F_polysemy": a["F_polysemy"],
            "payload_validity": a["payload_validity"],
            "contract_echo_penalty": a["contract_echo_penalty"],
            "schema_echo_penalty": a["schema_echo_penalty"],
            "legal_trap_penalty": a["legal_trap_penalty"],
            "literal_shape_trap_penalty": a["literal_shape_trap_penalty"],
            "O_model": a["O_model"],
            "hot": a["hot"],
            "cold": a["cold"],
            "hotcold_balance": a["hotcold_balance"],
            "generation_error": r.get("generation_error"),
            "answer": r["answer"],
            "payload_text": a["payload_text"],
        })
    return pd.DataFrame(flat).sort_values("score", ascending=False).reset_index(drop=True)


def audit_agreement(row_a: pd.Series, row_b: pd.Series) -> float:
    keys = ["F_need", "F_function", "F_trap", "F_collapse", "F_prompt"]
    if str(row_a.get("task_profile", "")) == "runtime_contract":
        keys += ["F_boundary", "F_polysemy"]
    diffs = [abs(float(row_a[k]) - float(row_b[k])) for k in keys]
    return clamp(1.0 - float(np.mean(diffs)))


def quality_min_for_row(row: pd.Series) -> float:
    return QUALITY_MIN_BY_PROFILE.get(str(row.get("task_profile", "general")), QUALITY_MIN_BY_PROFILE["general"])


def row_gate_failures(row: pd.Series, require_margin: bool, margin: float) -> List[str]:
    failed = []
    profile = str(row.get("task_profile", "general"))
    if float(row["score"]) < PSI_MIN:
        failed.append("score")
    if require_margin and margin < MARGIN_MIN:
        failed.append("margin")
    if REQUIRE_MODEL_FOR_PSI and row["origin"] != "model":
        failed.append("model_origin")
    if float(row["trace_sufficiency"]) < TRACE_MIN:
        failed.append("trace")
    if float(row["quality_hmean"]) < quality_min_for_row(row):
        failed.append("quality")
    if float(row["F_prompt"]) < PROMPT_FIT_MIN:
        failed.append("prompt_grounding")
    if profile == "runtime_contract" and float(row["F_polysemy"]) < POLYSEMY_MIN:
        failed.append("polysemy_lock")
    if float(row["contract_echo_penalty"]) > CONTRACT_ECHO_MAX:
        failed.append("contract_echo")
    if float(row["schema_echo_penalty"]) > SCHEMA_ECHO_MAX:
        failed.append("schema_echo")
    if profile == "runtime_contract" and float(row["legal_trap_penalty"]) > LEGAL_TRAP_MAX:
        failed.append("legal_trap")
    if profile == "inverse_retrieval" and float(row["literal_shape_trap_penalty"]) > LITERAL_SHAPE_TRAP_MAX:
        failed.append("literal_shape")
    if float(row["payload_validity"]) < 0.75:
        failed.append("payload_validity")
    return failed


def direct_gate(scored: pd.DataFrame) -> Dict[str, Any]:
    if scored.empty:
        return {"ok": False, "reason": "no_candidates", "failed": ["no_candidates"], "margin": 0.0}
    top = scored.iloc[0]
    second = scored.iloc[1] if len(scored) > 1 else None
    margin = float(top["score"] - (second["score"] if second is not None else 0.0))
    failed = row_gate_failures(top, require_margin=True, margin=margin)
    return {
        "ok": len(failed) == 0,
        "reason": "direct_margin_collapse" if len(failed) == 0 else "no_direct_collapse",
        "failed": failed,
        "margin": margin,
        "top_score": float(top["score"]),
        "top_origin": top["origin"],
        "task_profile": top.get("task_profile"),
        "trace_sufficiency": float(top["trace_sufficiency"]),
        "quality_hmean": float(top["quality_hmean"]),
        "quality_min": quality_min_for_row(top),
        "F_prompt": float(top["F_prompt"]),
        "F_polysemy": float(top["F_polysemy"]),
        "payload_validity": float(top["payload_validity"]),
        "contract_echo_penalty": float(top["contract_echo_penalty"]),
        "schema_echo_penalty": float(top["schema_echo_penalty"]),
        "legal_trap_penalty": float(top["legal_trap_penalty"]),
        "literal_shape_trap_penalty": float(top["literal_shape_trap_penalty"]),
    }


def consensus_gate(scored: pd.DataFrame) -> Dict[str, Any]:
    if len(scored) < 2:
        return {"ok": False, "reason": "not_enough_branches"}

    top = scored.iloc[0]
    second = scored.iloc[1]
    margin = float(top["score"] - second["score"])

    top_fail = row_gate_failures(top, require_margin=False, margin=margin)
    second_fail = row_gate_failures(second, require_margin=False, margin=margin)

    hard_top = top_fail[:]
    hard_second = second_fail[:]

    agreement = audit_agreement(top, second)
    payload_agree = jaccard_text(str(top["payload_text"]), str(second["payload_text"]), remove_nexus_surface=True)

    ok = (
        float(top["score"]) >= CONSENSUS_SCORE_MIN and
        float(second["score"]) >= CONSENSUS_SCORE_MIN and
        not hard_top and
        not hard_second and
        agreement >= CONSENSUS_AUDIT_MIN and
        (payload_agree >= 0.18 or agreement >= 0.90)
    )

    return {
        "ok": bool(ok),
        "reason": "consensus_collapse" if ok else "no_consensus",
        "margin": margin,
        "audit_agreement": agreement,
        "payload_agreement": payload_agree,
        "top_fail_no_margin": top_fail,
        "second_fail_no_margin": second_fail,
    }


def weakest_observable(scored: pd.DataFrame, direct: Dict[str, Any], consensus: Dict[str, Any]) -> str:
    if scored.empty:
        return "no_candidates"
    top = scored.iloc[0]
    failed = direct.get("failed", [])

    priority = [
        "model_origin", "contract_echo", "schema_echo", "legal_trap", "literal_shape",
        "payload_validity", "polysemy_lock", "quality", "prompt_grounding", "trace", "margin", "score"
    ]
    for p in priority:
        if p in failed:
            return p

    dims = {
        "need": float(top["F_need"]),
        "function": float(top["F_function"]),
        "boundary": float(top["F_boundary"]),
        "trap": float(top["F_trap"]),
        "collapse": float(top["F_collapse"]),
        "polysemy": float(top["F_polysemy"]),
        "payload": float(top["payload_validity"]),
    }
    return min(dims.items(), key=lambda kv: kv[1])[0]
```


```python

# Recursive resolver, payload shaper, and runner.

def dataframe_scores_for_json(scored: pd.DataFrame) -> List[Dict[str, Any]]:
    out = []
    for _, row in scored.iterrows():
        d = {}
        for col in scored.columns:
            val = row[col]
            if isinstance(val, (np.integer, np.floating)):
                val = val.item()
            d[col] = val
        out.append(d)
    return out



def target_word_budget(contract: NeedSlotContract) -> int:
    return int(SHAPER_WORD_BUDGET_BY_PROFILE.get(contract.task_profile, 150))


def shaper_instruction(contract: NeedSlotContract) -> str:
    profile = contract.task_profile
    if profile == "runtime_contract":
        return (
            "Explain the runtime mechanism sharply: why tool use before a runtime execution contract fails. "
            "Keep preconditions, side effects, success/failure criteria, rollback, and trace update if present. "
            "Do not frame contract as legal or stakeholder agreement."
        )
    if profile == "memory_trace":
        return (
            "Explain memory as causal trace continuity across turns. Preserve state transitions, observations, "
            "tool calls, decisions, rollback/update continuity if present. Do not turn it into a precondition checklist."
        )
    if profile == "inverse_retrieval":
        return (
            "Describe the retrieval step as inverse operational fit: infer missing operation, generate candidates, "
            "rank by fit, verify against constraints, select. Do not use literal shapes like circles/spheres."
        )
    return "Make the answer direct, compact, and operational without changing its meaning."


def deterministic_shaped_payload(raw_payload: str, contract: NeedSlotContract) -> str:
    """Fallback shaper: strip obvious excess and cap rough length without changing content."""
    text = payload_text(raw_payload).strip()
    # Remove hanging incomplete last line if generation was cut mid-sentence.
    parts = re.split(r'(?<=[.!?])\s+', text)
    cleaned = []
    for p in parts:
        if p.strip():
            cleaned.append(p.strip())
    words_budget = target_word_budget(contract)
    out = " ".join(cleaned).strip() or text
    toks = out.split()
    if len(toks) > words_budget:
        out = " ".join(toks[:words_budget]).rstrip(" ,;:") + "."
    return out


def shape_final_payload(prompt: str, contract: NeedSlotContract, winner_row: pd.Series, collapse_reason: str, scored: pd.DataFrame) -> Dict[str, Any]:
    """v19 final pass: turn the accepted branch payload into a crisp answer.

    This does not participate in branch selection. It is a post-collapse renderer.
    It must preserve the accepted meaning and is audited afterward.
    """
    raw = str(winner_row.get("payload_text", winner_row.get("answer", ""))).strip()
    if not ENABLE_PAYLOAD_SHAPER:
        shaped = deterministic_shaped_payload(raw, contract)
        audit = answer_operational_audit(prompt, contract, shaped, str(winner_row.get("origin", "model")))
        return {
            "enabled": False,
            "origin": "disabled",
            "accepted": True,
            "reason": "shaper_disabled",
            "raw_payload": raw,
            "shaped_payload": shaped,
            "audit": audit,
        }

    if MODEL_GENERATION_READY:
        system = (
            "You are a final answer shaper. You do not choose the answer. "
            "You compress the accepted payload into a clear human-facing answer while preserving meaning. "
            "Do not add new claims. Do not print internal specs or scoring labels."
        )
        user = f"""
USER PROMPT:
{contract.clean_prompt}

TASK PROFILE:
{contract.task_profile}

PRESERVE THIS MEANING:
{shaper_instruction(contract)}

ACCEPTED RAW PAYLOAD:
{raw}

OUTPUT RULES:
1. Return only the final answer payload.
2. Keep it under {target_word_budget(contract)} words.
3. Prefer 2-4 short paragraphs or a tight numbered list only if the raw payload is already procedural.
4. Do not mention branches, audits, scores, gates, Ψ, Ω, polysemy, or internal contracts.
5. Do not use legal-contract language unless the user explicitly asked for law.
6. Do not change the answer's operational meaning.
"""
        try:
            shaped = raw_model_generate(
                [{"role": "system", "content": system}, {"role": "user", "content": user}],
                max_new_tokens=SHAPER_MAX_NEW_TOKENS,
                sample=SHAPER_SAMPLE,
            ).strip()
            if not shaped:
                raise RuntimeError("empty shaped payload")
            origin = "model_shaper"
            err = None
        except Exception as e:
            shaped = deterministic_shaped_payload(raw, contract)
            origin = "fallback_shaper_error"
            err = "".join(traceback.format_exception_only(type(e), e)).strip()
    else:
        shaped = deterministic_shaped_payload(raw, contract)
        origin = "fallback_model_not_ready"
        err = MODEL_ERROR

    audit = answer_operational_audit(prompt, contract, shaped, "model" if str(winner_row.get("origin")) == "model" else str(winner_row.get("origin")))
    quality_min = QUALITY_MIN_BY_PROFILE.get(contract.task_profile, 0.34)
    accepted = (
        audit["payload_validity"] >= 0.80 and
        audit["contract_echo_penalty"] <= CONTRACT_ECHO_MAX and
        audit["schema_echo_penalty"] <= SCHEMA_ECHO_MAX and
        audit["legal_trap_penalty"] <= LEGAL_TRAP_MAX and
        audit["literal_shape_trap_penalty"] <= LITERAL_SHAPE_TRAP_MAX and
        audit["quality_hmean"] >= max(0.24, quality_min - 0.12)
    )

    if not accepted:
        # Never let the renderer damage a valid collapse. Use deterministic compression of the accepted payload.
        fallback = deterministic_shaped_payload(raw, contract)
        fallback_audit = answer_operational_audit(prompt, contract, fallback, "model" if str(winner_row.get("origin")) == "model" else str(winner_row.get("origin")))
        return {
            "enabled": True,
            "origin": origin,
            "accepted": False,
            "reason": "shaped_payload_failed_audit_using_deterministic_payload",
            "error": err,
            "raw_payload": raw,
            "rejected_shaped_payload": shaped,
            "shaped_payload": fallback,
            "audit": audit,
            "fallback_audit": fallback_audit,
        }

    return {
        "enabled": True,
        "origin": origin,
        "accepted": True,
        "reason": "shaped_payload_accepted",
        "error": err,
        "raw_payload": raw,
        "shaped_payload": shaped,
        "audit": audit,
    }


def _collapse_result(prompt: str, contract: NeedSlotContract, scored: pd.DataFrame, trace_entry: Dict[str, Any], depth: int, reason: str) -> Dict[str, Any]:
    winner = scored.iloc[0]
    shaper = shape_final_payload(prompt, contract, winner, reason, scored)
    final_payload = shaper.get("shaped_payload") or winner["payload_text"]
    return {
        "run_id": RUN_ID,
        "prompt": prompt,
        "state": "Ψ",
        "reason": reason,
        "depth": depth,
        "winner_branch": winner["branch"],
        "winner_origin": winner["origin"],
        "winner_score": float(winner["score"]),
        "answer": final_payload,
        "payload": final_payload,
        "raw_winner_answer": winner["answer"],
        "raw_winner_payload": winner["payload_text"],
        "shaper": shaper,
        "contract": asdict(contract),
        "trace": [trace_entry],
        "device_info": DEVICE_INFO,
    }

def recursive_resolve(prompt: str, depth: int = 0, repair_history: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    repair_history = repair_history or []
    contract = build_contract(prompt, repair_history=repair_history)

    candidates = generate_candidates(prompt, contract)
    scored = score_candidates(prompt, contract, candidates)

    direct = direct_gate(scored)
    consensus = consensus_gate(scored)

    trace_entry = {
        "depth": depth,
        "contract": asdict(contract),
        "scores": dataframe_scores_for_json(scored),
        "direct_gate": direct,
        "consensus_gate": consensus,
    }

    if direct["ok"]:
        return _collapse_result(prompt, contract, scored, trace_entry, depth, direct["reason"])

    if consensus["ok"]:
        return _collapse_result(prompt, contract, scored, trace_entry, depth, consensus["reason"])

    if REQUIRE_MODEL_FOR_PSI and not MODEL_GENERATION_READY:
        winner = scored.iloc[0] if len(scored) else None
        return {
            "run_id": RUN_ID,
            "prompt": prompt,
            "state": "Ω",
            "reason": "model_generation_failed",
            "depth": depth,
            "winner_branch": None if winner is None else winner["branch"],
            "winner_origin": None if winner is None else winner["origin"],
            "winner_score": None if winner is None else float(winner["score"]),
            "answer": None if winner is None else winner["answer"],
            "payload": None if winner is None else winner["payload_text"],
            "contract": asdict(contract),
            "trace": [trace_entry],
            "device_info": DEVICE_INFO,
        }

    if depth >= MAX_RECURSION_DEPTH:
        winner = scored.iloc[0]
        return {
            "run_id": RUN_ID,
            "prompt": prompt,
            "state": "Ω",
            "reason": "max_depth_residue",
            "depth": depth,
            "winner_branch": winner["branch"],
            "winner_origin": winner["origin"],
            "winner_score": float(winner["score"]),
            "answer": winner["answer"],
            "payload": winner["payload_text"],
            "contract": asdict(contract),
            "trace": [trace_entry],
            "device_info": DEVICE_INFO,
        }

    weak = weakest_observable(scored, direct, consensus)
    winner = scored.iloc[0]
    new_history = repair_history + [{
        "failed_gate": direct.get("failed", []),
        "consensus_reason": consensus.get("reason"),
        "weakest_observable": weak,
        "winner_branch": winner["branch"],
        "winner_origin": winner["origin"],
        "winner_score": float(winner["score"]),
        "contract_echo_penalty": float(winner["contract_echo_penalty"]),
        "schema_echo_penalty": float(winner["schema_echo_penalty"]),
        "legal_trap_penalty": float(winner["legal_trap_penalty"]),
        "literal_shape_trap_penalty": float(winner["literal_shape_trap_penalty"]),
        "payload_validity": float(winner["payload_validity"]),
        "F_polysemy": float(winner["F_polysemy"]),
    }]

    child = recursive_resolve(prompt, depth=depth + 1, repair_history=new_history)
    child["trace"] = [trace_entry] + child["trace"]
    return child

def run_rhi_v19(prompt: str) -> Dict[str, Any]:
    result = recursive_resolve(prompt)
    print("=" * 100)
    print("PROMPT:", prompt)
    print("STATE:", result["state"], "REASON:", result["reason"], "DEPTH:", result["depth"])
    print("WINNER:", result["winner_branch"], result["winner_origin"], result["winner_score"])
    print("FINAL ANSWER:\n", result["answer"])
    if result.get("raw_winner_payload"):
        print("\nRAW WINNER PAYLOAD:\n", result.get("raw_winner_payload"))
    print("\nPAYLOAD:\n", result.get("payload"))
    return result


def build_summary_rows(results: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows = []
    for prompt, result in results.items():
        final_trace = result.get("trace", [])[-1] if result.get("trace") else {}
        direct_gate = final_trace.get("direct_gate", {})
        consensus_gate = final_trace.get("consensus_gate", {})
        rows.append({
            "run_id": result.get("run_id"),
            "prompt": prompt,
            "state": result.get("state"),
            "reason": result.get("reason"),
            "depth": result.get("depth"),
            "winner_branch": result.get("winner_branch"),
            "winner_origin": result.get("winner_origin"),
            "winner_score": result.get("winner_score"),
            "direct_ok": direct_gate.get("ok"),
            "direct_failed": "|".join(direct_gate.get("failed", [])) if isinstance(direct_gate.get("failed"), list) else direct_gate.get("failed"),
            "consensus_ok": consensus_gate.get("ok"),
            "consensus_reason": consensus_gate.get("reason"),
            "shaper_origin": (result.get("shaper") or {}).get("origin"),
            "shaper_accepted": (result.get("shaper") or {}).get("accepted"),
            "raw_answer_preview": str(result.get("raw_winner_payload", result.get("answer", "")))[:240].replace("\n", " "),
            "answer_preview": str(result.get("answer", ""))[:320].replace("\n", " "),
        })
    return rows


def save_two_file_bundle(results: Dict[str, Dict[str, Any]], out_dir: Path = OUT_DIR) -> Tuple[Path, Path]:
    """Write exactly two return files: full JSON bundle + compact CSV summary."""
    summary_rows = build_summary_rows(results)
    summary_df = pd.DataFrame(summary_rows)

    bundle = {
        "run_id": RUN_ID,
        "created_root": str(ROOT),
        "out_dir": str(out_dir),
        "model_id_or_path": MODEL_ID_OR_PATH,
        "load_real_model": LOAD_REAL_MODEL,
        "require_model_for_psi": REQUIRE_MODEL_FOR_PSI,
        "model_ready": MODEL_READY,
        "model_generation_ready": MODEL_GENERATION_READY,
        "model_error": MODEL_ERROR,
        "dependency_status": DEPENDENCY_STATUS,
        "device_info": DEVICE_INFO,
        "prompts": list(results.keys()),
        "summary": summary_rows,
        "results": results,
    }

    bundle_path = out_dir / f"{RUN_ID}_bundle.json"
    summary_path = out_dir / f"{RUN_ID}_summary.csv"

    with open(bundle_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    summary_df.to_csv(summary_path, index=False)

    print("saved bundle:", bundle_path)
    print("saved summary:", summary_path)
    print("RETURN THESE TWO FILES ONLY:")
    print("1)", bundle_path)
    print("2)", summary_path)
    return bundle_path, summary_path
```


```python

# Test prompts.
# Add your own prompts to this list.

TEST_PROMPTS = [
    "explain why current AI agents fail when they use tools before forming a contract",
    "explain memory in an agent as trace continuity rather than a text summary",
    "design a shape-first retrieval step where no noun match exists but the inverse need is clear",
]

results = {}
for p in TEST_PROMPTS:
    results[p] = run_rhi_v19(p)
```


```python

# Two-file output only.
# This cell writes exactly:
#   1. <RUN_ID>_bundle.json   = full details for return/debug
#   2. <RUN_ID>_summary.csv   = compact overview

bundle_path, summary_path = save_two_file_bundle(results)
summary = pd.DataFrame(build_summary_rows(results))
display(summary)
```
