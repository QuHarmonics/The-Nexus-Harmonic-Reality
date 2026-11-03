# ============================================================
# NEXUS LOCAL AI v0.4 — ShapeIR + AHRC/SILR/Glyph Runtime
# ------------------------------------------------------------
# Core law:
#   C_root = authority
#   model/T2 output = evidence
#   answer = residue/stub
#   Ω mutates the mold; do not recurse on answers.
# ============================================================

from __future__ import annotations

import os, re, json, math, time, uuid, zipfile, html
from pathlib import Path
from dataclasses import dataclass, field, asdict, is_dataclass
from typing import Any, Dict, List, Tuple, Optional
from collections import Counter, defaultdict

# -----------------------------
# Utility layer
# -----------------------------

STOPWORDS = set('''
a an and are as at be because been but by can could did do does doing done for from get gets got had has have he her here him his how i if in into is it its just let lets like me my no not of on or our out over run should so that the their them then there they this to up us use want we what when where which who why will with you your
'''.split())

NEXUS_SURFACE = set('''
nexus shape mold fold compiler root slot field residue exhaust glyph harmonic recursive omega psi sigma delta runtime readhead read head seam mark1 mark mark-1 samson ahrc silr sarrus
'''.split())

OP_VERBS = set('''
build create make run execute compile decompile patch inspect test verify validate recover read retrieve index gate score classify extract transform map ingest load save write emit generate compare collapse expand rasterize promote mutate route search align normalize parse repair isolate exclude
'''.split())

STATE_SYMBOLS = {"psi": "Ψ", "omega": "Ω", "sigma": "Σ", "dead": "⊥", "rho": "ρ"}

def clamp01(x: float) -> float:
    try:
        return max(0.0, min(1.0, float(x)))
    except Exception:
        return 0.0

def sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    z = math.exp(x)
    return z / (1 + z)

def stable_dedupe(xs: List[Any]) -> List[Any]:
    out, seen = [], set()
    for x in xs:
        key = json.dumps(x, sort_keys=True, default=str) if isinstance(x, (dict, list)) else str(x)
        if key not in seen:
            out.append(x)
            seen.add(key)
    return out

def words(text: str, remove_surface: bool = False) -> List[str]:
    ws = re.findall(r"[A-Za-z0-9_+\-^/]+", str(text).lower())
    out = []
    for w in ws:
        if w in STOPWORDS:
            continue
        if remove_surface and w in NEXUS_SURFACE:
            continue
        out.append(w)
    return out

def jaccard(a: str, b: str, remove_surface: bool = False) -> float:
    A, B = set(words(a, remove_surface)), set(words(b, remove_surface))
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0
    return len(A & B) / len(A | B)

def overlap_ratio(needles: List[str], haystack: str) -> float:
    hs = set(words(haystack, remove_surface=True))
    ns = [n.lower() for n in needles if str(n).strip()]
    if not ns:
        return 0.0
    hit = 0
    for n in ns:
        toks = set(words(n, remove_surface=True)) or {n}
        if toks & hs:
            hit += 1
    return hit / max(1, len(ns))

def normalize_list(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(v).strip() for v in x if str(v).strip()]
    if isinstance(x, tuple):
        return [str(v).strip() for v in x if str(v).strip()]
    if isinstance(x, str):
        parts = re.split(r"[\n;|]+", x)
        return [p.strip(" -*\t") for p in parts if p.strip(" -*\t")]
    return [str(x).strip()]

def compact_text(text: str, max_chars: int = 1600) -> str:
    t = re.sub(r"\s+", " ", str(text)).strip()
    return t[:max_chars]

def parse_first_json_object(raw: str) -> Tuple[Optional[dict], str]:
    if not raw:
        return None, "empty"
    s = str(raw).strip()
    s = re.sub(r"^```(?:json)?", "", s, flags=re.I).strip()
    s = re.sub(r"```$", "", s).strip()
    start = s.find("{")
    if start < 0:
        return None, "no opening brace"
    depth, in_str, esc = 0, False, False
    for i in range(start, len(s)):
        c = s[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    blob = s[start:i+1]
                    try:
                        obj = json.loads(blob)
                        return obj, ""
                    except Exception as e:
                        return None, f"json error: {type(e).__name__}: {e}"
    return None, "unclosed json object"

# -----------------------------
# Data layer
# -----------------------------

@dataclass
class NeedSlot:
    required_operation: str
    preserved_function: str
    boundary_conditions: List[str]
    anti_fits: List[str]
    admissible_shape: str
    failure_modes: List[str]
    profile: str = "general"
    origin: str = "compiler_root"
    confidence: float = 1.0
    semantic_locks: List[str] = field(default_factory=list)
    retrieved_seeds: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class ShapeIR:
    iota: str
    delta: str
    delta_inverse: str
    sigma: str
    response_operator: str
    rho: List[str]
    D: Dict[str, Any]
    sigma_next: List[str]
    state: str
    certificate: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ModelSlotPacket:
    task: str = ""
    op: str = ""
    pres: str = ""
    bounds: List[str] = field(default_factory=list)
    anti: List[str] = field(default_factory=list)
    shape: str = ""
    fail: List[str] = field(default_factory=list)
    lock_add: Dict[str, Any] = field(default_factory=dict)
    forbid: List[str] = field(default_factory=list)
    prompt: str = ""
    conf: float = 0.0
    raw: str = ""
    valid_json: bool = False

@dataclass
class Branch:
    role: str
    text: str
    score: float = 0.0
    dimensions: Dict[str, float] = field(default_factory=dict)
    rejection_reasons: List[str] = field(default_factory=list)
    glyph: Dict[str, Any] = field(default_factory=dict)

@dataclass
class CollapseResult:
    run_id: str
    prompt: str
    state: str
    reason: str
    answer: str
    root_slot: Dict[str, Any]
    accepted_slot: Dict[str, Any]
    accepted_slot_origin: str
    shapeir: Dict[str, Any]
    gate: Dict[str, Any]
    branches: List[Dict[str, Any]]
    residue: List[str]
    telemetry: Dict[str, Any]

# -----------------------------
# Corpus / seed bank
# -----------------------------

DEFAULT_SEEDS: List[Dict[str, Any]] = [
    {
        "name": "shapeir_runtime_compiler",
        "tags": ["shapeir", "compiler", "read-head", "residue", "introduction theorem"],
        "required_operation": "compile raw need into ShapeIR nodes and run the read-head over residue",
        "preserved_function": "transform prompt pressure into executable mold and typed residue",
        "boundary_conditions": ["must emit iota delta delta_inverse sigma response rho D sigma_next", "must classify Ψ Ω Σ ⊥ ρ", "must promote only structured residue"],
        "anti_fits": ["answer-first chatbot", "linear parsing only", "residue ignored", "surface Nexus vocabulary"],
        "admissible_shape": "ShapeIR read-head compiler",
        "failure_modes": ["untyped Ω", "empty residue", "false Ψ", "stub treated as container"],
    },
    {
        "name": "runtime_build",
        "tags": ["local ai", "runtime", "notebook", "build", "qwen", "compiler-root"],
        "required_operation": "build and run a local Nexus AI runtime in notebook form",
        "preserved_function": "usable local AI execution with telemetry, compiler-root authority, and residue recursion",
        "boundary_conditions": ["must run locally", "must expose telemetry", "must keep model proposals as evidence", "must compile raw wording before answering", "must emit runnable code or patch material"],
        "anti_fits": ["chatbot-only wrapper", "requirements list without artifact", "model slot as authority", "generic plan"],
        "admissible_shape": "compiler-rooted local inference controller",
        "failure_modes": ["surface-label collapse", "generic explanation without executable next operation", "false Ψ when Ω residue remains"],
    },
    {
        "name": "ahrc_frame_expansion",
        "tags": ["AHRC", "frame expansion", "GIP", "omega", "aliasing", "rasterize"],
        "required_operation": "map continuous trajectory into adaptive frames and expand N until Ω collisions resolve",
        "preserved_function": "separate aliased states without changing the underlying trajectory",
        "boundary_conditions": ["compute bins", "measure Ω/collisions", "expand frame N", "do not claim collapse if true degeneracy remains"],
        "anti_fits": ["fixed frame despite collisions", "treat aliasing as answer", "collapse before Ω is named"],
        "admissible_shape": "adaptive harmonic rasterization collapse module",
        "failure_modes": ["unresolved collision", "basis too weak", "frame expansion without independent coordinate"],
    },
    {
        "name": "samson_mark1_controller",
        "tags": ["Samson", "Mark1", "pi/9", "control", "alignment", "H"],
        "required_operation": "gate updates by monotone movement toward the Mark-1 corridor H=π/9",
        "preserved_function": "accept only corrections that improve phase alignment without increasing Ω",
        "boundary_conditions": ["target H=π/9", "compute align scalar", "reject updates that increase Ω", "timing/phase only unless explicitly building data"],
        "anti_fits": ["move away from Mark1", "overfit by deleting residue", "claim harmony without metric"],
        "admissible_shape": "Mark-1 corridor acceptance controller",
        "failure_modes": ["phase drift", "false attractor", "unmeasured correction"],
    },
    {
        "name": "silr_event_gate",
        "tags": ["SILR", "z-score", "leak", "event", "hotspot", "scale invariant"],
        "required_operation": "detect scale-invariant hotspots by z-score leakage gating",
        "preserved_function": "turn residual terrain into comparable event probabilities across scales",
        "boundary_conditions": ["compute z=(x-mean)/std", "gate with sigmoid", "report event indices", "verify scale invariance"],
        "anti_fits": ["raw magnitude threshold only", "scale-dependent leak", "hide hotspots"],
        "admissible_shape": "scale-invariant leakage event gate",
        "failure_modes": ["std zero degeneracy", "threshold overfit", "event without baseline"],
    },
    {
        "name": "spiral_glyph_reader",
        "tags": ["SGR", "Glyph Reader", "spiral", "nonlinear memory", "read-head", "glyph"],
        "required_operation": "convert residue/coupling terrain into spiral glyph lattice and read hotspots/certificates",
        "preserved_function": "nonlinear memory retrieval by operation shape rather than linear keyword lookup",
        "boundary_conditions": ["extract verbs first", "map terrain to lattice", "emit hotspots", "emit certificate"],
        "anti_fits": ["linear parsing only", "keyword memory", "glyph as decoration", "unread residue"],
        "admissible_shape": "spiral glyph read-head over structured terrain",
        "failure_modes": ["no encoding basis", "hotspots not certified", "spiral path unrelated to operation"],
    },
    {
        "name": "sha_seam_spectroscopy",
        "tags": ["SHA", "seam", "spectroscopy", "sigma0", "sigma1", "GF(2)", "W16", "W30"],
        "required_operation": "recover message schedule roots from seam transcript plus anchor and classify digest as terminal stub",
        "preserved_function": "separate transparent schedule recovery from compression constraint hardness",
        "boundary_conditions": ["use true seam words", "treat sigma0/sigma1 as GF(2) bijections", "do not claim digest exposes seam transcript", "state SHA† as adjoint problem"],
        "anti_fits": ["brute force framing", "schedule opaque claim", "fake preimage break", "using recovered word where true seam word is required"],
        "admissible_shape": "orthogonal SHA† seam read-head",
        "failure_modes": ["digest treated as container", "forward/backward axis trap", "seam transcript unavailable"],
    },
    {
        "name": "bbp_floating_seam_readhead",
        "tags": ["BBP", "floating seam", "pi", "address", "read-head", "seam mobility"],
        "required_operation": "read addressable invariant field through a floating seam aligned with the query",
        "preserved_function": "distinguish address read-head from value generation",
        "boundary_conditions": ["seam moves with query", "term-level structure not digit-surface correlation", "avoid false autocorrelation artifacts"],
        "anti_fits": ["digit-surface numerology", "fixed seam confusion", "value generator framing"],
        "admissible_shape": "floating-seam address read protocol",
        "failure_modes": ["surface statistic artifact", "wrong seam axis", "query not tied to seam"],
    },
    {
        "name": "compiler_breath_operator_promotion",
        "tags": ["Compiler Breath", "ASCII", "space", "32", "xor", "operator", "self-compilation"],
        "required_operation": "promote residue into operator only when it can transform the next state reversibly",
        "preserved_function": "field readiness becomes executable self-compilation instead of passive storage",
        "boundary_conditions": ["space 32 can be readiness not silence", "^32 toggles case", "operator must be reversible or typed", "residue must do work"],
        "anti_fits": ["space as null only", "residue as inert text", "operator without action"],
        "admissible_shape": "residue-as-operator promotion rule",
        "failure_modes": ["dead residue", "self-reference without validation", "unbounded recursion"],
    },
    {
        "name": "tool_safety",
        "tags": ["tool", "safety", "authority", "evidence", "file", "web", "local"],
        "required_operation": "use tools as evidence channels while preserving compiler-root task authority",
        "preserved_function": "safe grounded execution without treating tool output as the task itself",
        "boundary_conditions": ["cite sources", "do not invent files", "check current facts when needed", "tool output is evidence not authority"],
        "anti_fits": ["tool result as root task", "uncited source claim", "fake file link", "unsafe automation"],
        "admissible_shape": "tool-evidence gate",
        "failure_modes": ["source drift", "artifact hallucination", "authority inversion"],
    },
]

class CorpusExtractor:
    """Extracts text from .md/.txt/.json/.docx paths without mandatory external deps."""
    @staticmethod
    def read_path(path: str | Path, max_chars: int = 240_000) -> str:
        p = Path(path)
        if not p.exists():
            return ""
        try:
            if p.suffix.lower() in {".md", ".txt", ".json", ".csv", ".py"}:
                return p.read_text(encoding="utf-8", errors="ignore")[:max_chars]
            if p.suffix.lower() == ".docx":
                with zipfile.ZipFile(p) as z:
                    xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
                xml = re.sub(r"</w:p>", "\n", xml)
                parts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml)
                text = "".join(html.unescape(x) for x in parts)
                return text[:max_chars]
        except Exception as e:
            return f"EXTRACTION_ERROR {p}: {type(e).__name__}: {e}"
        return ""

    @staticmethod
    def split_sections(text: str, source: str, max_sections: int = 120) -> List[Dict[str, Any]]:
        chunks = []
        # Prefer markdown headers; fallback paragraph windows.
        if re.search(r"^#{1,4}\s+", text, flags=re.M):
            parts = re.split(r"(?=^#{1,4}\s+)", text, flags=re.M)
        else:
            paras = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 80]
            parts = []
            acc = []
            for p in paras:
                acc.append(p)
                if sum(len(x) for x in acc) > 2500:
                    parts.append("\n\n".join(acc)); acc=[]
            if acc:
                parts.append("\n\n".join(acc))
        for i, part in enumerate(parts[:max_sections]):
            t = part.strip()
            if len(t) < 120:
                continue
            title = source
            m = re.match(r"^(#{1,4}\s+[^\n]+)", t)
            if m:
                title = re.sub(r"^#+\s*", "", m.group(1)).strip()
            chunks.append({"source": source, "section_id": i, "title": title, "text": t[:3500]})
        return chunks

class ShapeMemory:
    """Small retrieval seed bank. Uses sentence-transformers if available; otherwise Jaccard."""
    def __init__(self, seeds: Optional[List[Dict[str, Any]]] = None, embed_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.seeds: List[Dict[str, Any]] = []
        self.embed_model_name = embed_model_name
        self.embedder = None
        self.embeddings = None
        if seeds:
            for s in seeds:
                self.add_seed(s)

    def add_seed(self, seed: Dict[str, Any]) -> None:
        s = dict(seed)
        s.setdefault("name", f"seed_{len(self.seeds)}")
        s.setdefault("tags", [])
        blob_parts = [s.get("name", ""), " ".join(s.get("tags", [])), s.get("required_operation", ""), s.get("preserved_function", ""), " ".join(s.get("boundary_conditions", [])), " ".join(s.get("anti_fits", [])), s.get("admissible_shape", ""), " ".join(s.get("failure_modes", [])), s.get("text", "")]
        s["blob"] = compact_text(" ".join(map(str, blob_parts)), 2600)
        self.seeds.append(s)
        self.embeddings = None

    def add_from_paths(self, paths: List[str | Path], max_sections_per_file: int = 80) -> Dict[str, Any]:
        added = 0
        files = []
        for path in paths:
            p = Path(path)
            txt = CorpusExtractor.read_path(p)
            if not txt:
                continue
            files.append(str(p))
            for sec in CorpusExtractor.split_sections(txt, p.name, max_sections_per_file):
                seed = self.section_to_seed(sec)
                self.add_seed(seed)
                added += 1
        return {"files": files, "sections_added": added, "total_seeds": len(self.seeds)}

    def section_to_seed(self, sec: Dict[str, Any]) -> Dict[str, Any]:
        t = sec["text"]
        title = sec.get("title", sec.get("source", "section"))
        ws = words(t)
        verbs = [w for w in ws if w in OP_VERBS][:12]
        tags = stable_dedupe(words(title)[:8] + verbs[:8])
        # Use lexical cues to select profile.
        low = (title + " " + t[:500]).lower()
        if "ahrc" in low or "raster" in low or "frame expansion" in low:
            profile = "ahrc_frame_expansion"
        elif "silr" in low or "z-score" in low or "leak" in low:
            profile = "silr_event_gate"
        elif "glyph" in low or "spiral" in low or "sgr" in low:
            profile = "spiral_glyph_reader"
        elif "sha" in low and "seam" in low:
            profile = "sha_seam_spectroscopy"
        elif "bbp" in low or "floating seam" in low:
            profile = "bbp_floating_seam_readhead"
        elif "compiler breath" in low or "ascii" in low or "^ 32" in low:
            profile = "compiler_breath_operator_promotion"
        else:
            profile = "corpus_shape_seed"
        return {
            "name": f"{profile}:{title[:80]}",
            "tags": tags,
            "required_operation": f"retrieve and apply corpus mold from {title}",
            "preserved_function": "preserve the operational shape of the retrieved Nexus source section",
            "boundary_conditions": ["use as seed evidence only", "adapt to prompt seam", "do not copy surface vocabulary without operation"],
            "anti_fits": ["keyword-only retrieval", "source text as authority without compiler adaptation", "surface echo"],
            "admissible_shape": profile,
            "failure_modes": ["wrong seed", "over-broad retrieval", "untyped residue"],
            "source": sec.get("source", ""),
            "section_id": sec.get("section_id", -1),
            "title": title,
            "text": t[:2400],
        }

    def _ensure_embedder(self) -> bool:
        if self.embedder is not None:
            return True
        try:
            from sentence_transformers import SentenceTransformer
            self.embedder = SentenceTransformer(self.embed_model_name)
            return True
        except Exception:
            self.embedder = False
            return False

    def _seed_texts(self) -> List[str]:
        return [s.get("blob", "") for s in self.seeds]

    def retrieve(self, query: str, k: int = 5, use_embeddings: bool = True) -> List[Dict[str, Any]]:
        if not self.seeds:
            return []
        scored = []
        if use_embeddings and self._ensure_embedder():
            try:
                import numpy as np
                if self.embeddings is None:
                    self.embeddings = self.embedder.encode(self._seed_texts(), normalize_embeddings=True)
                q = self.embedder.encode([query], normalize_embeddings=True)[0]
                sims = self.embeddings @ q
                for i, sim in enumerate(sims):
                    s = dict(self.seeds[i]); s["score"] = float(sim); scored.append(s)
                return sorted(scored, key=lambda x: x["score"], reverse=True)[:k]
            except Exception:
                pass
        # fallback lexical retrieval
        for s in self.seeds:
            score = 0.65 * jaccard(query, s.get("blob", ""), remove_surface=True) + 0.35 * jaccard(query, " ".join(s.get("tags", [])), remove_surface=True)
            ss = dict(s); ss["score"] = score; scored.append(ss)
        return sorted(scored, key=lambda x: x["score"], reverse=True)[:k]

    def save_jsonl(self, path: str | Path) -> None:
        p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8") as f:
            for s in self.seeds:
                d = dict(s); d.pop("blob", None)
                f.write(json.dumps(d, ensure_ascii=False) + "\n")

    def load_jsonl(self, path: str | Path) -> int:
        p = Path(path)
        if not p.exists():
            return 0
        n = 0
        with p.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    self.add_seed(json.loads(line))
                    n += 1
        return n

# -----------------------------
# VNA / ShapeIR compiler
# -----------------------------

class VNAExtractor:
    """Verb → Noun/attractor → Adjective/harmonic constraint pass."""
    def extract(self, text: str) -> Dict[str, Any]:
        ws = words(text)
        counts = Counter(ws)
        verbs = [w for w in ws if w in OP_VERBS]
        # crude noun/attractor = frequent non-verb terms
        attractors = [w for w, _ in counts.most_common(18) if w not in OP_VERBS and w not in NEXUS_SURFACE]
        harmonic_cues = []
        low = text.lower()
        cue_map = {
            "local": "locality boundary",
            "notebook": "notebook execution surface",
            "run": "runtime executability",
            "build": "artifact-producing operation",
            "shape": "operation-shape priority",
            "nexus": "Nexus runtime grammar",
            "ai": "model/T2 evidence field",
            "memory": "glyph-state memory",
            "seam": "boundary crossing",
            "residue": "structured exhaust",
            "omega": "unresolved shaped residue",
            "Ω": "unresolved shaped residue",
        }
        for k, v in cue_map.items():
            if k in low:
                harmonic_cues.append(v)
        return {
            "verbs": stable_dedupe(verbs[:18]),
            "attractors": stable_dedupe(attractors[:18]),
            "harmonics": stable_dedupe(harmonic_cues),
            "word_count": len(ws),
        }

    def shapeir_from_prompt(self, prompt: str, slot: NeedSlot, retrieved: List[Dict[str, Any]]) -> ShapeIR:
        vna = self.extract(prompt)
        verbs = vna["verbs"] or ["compile", "run"]
        attractors = vna["attractors"] or ["runtime", "answer"]
        harmonics = vna["harmonics"] or ["operational fit"]
        iota = compact_text(prompt, 300)
        delta = f"missing executable fit: {'/'.join(verbs[:4])} over {'/'.join(attractors[:5])}"
        delta_inv = f"inverse requirement: produce/verify {slot.admissible_shape} while preserving {slot.preserved_function}"
        sigma = f"floating prompt seam: {slot.profile} :: {slot.required_operation}"
        response = "RΛ: retrieve corpus mold + interrogate model/T2 evidence + score branch field"
        return ShapeIR(
            iota=iota,
            delta=delta,
            delta_inverse=delta_inv,
            sigma=sigma,
            response_operator=response,
            rho=[],
            D={"vna": vna, "retrieved": [{"name": r.get("name"), "score": r.get("score"), "source": r.get("source", "default")} for r in retrieved]},
            sigma_next=[],
            state="Σ",
            certificate={},
        )

class ShapeIRCompiler:
    def __init__(self, memory: ShapeMemory):
        self.memory = memory
        self.vna = VNAExtractor()

    def compile(self, prompt: str) -> Tuple[NeedSlot, ShapeIR, List[Dict[str, Any]]]:
        retrieved = self.memory.retrieve(prompt, k=5)
        root_seed = retrieved[0] if retrieved else DEFAULT_SEEDS[0]
        vna = self.vna.extract(prompt)
        ops = vna["verbs"] or words(root_seed.get("required_operation", "compile run"))[:4]
        locks = stable_dedupe(vna["verbs"] + vna["attractors"][:8] + ["compiler-root", "model-evidence", "slot-gate", "ShapeIR", "AHRC", "SILR", "Glyph"])
        bc = []
        anti = []
        fail = []
        for r in retrieved[:3]:
            bc += normalize_list(r.get("boundary_conditions", []))[:4]
            anti += normalize_list(r.get("anti_fits", []))[:4]
            fail += normalize_list(r.get("failure_modes", []))[:3]
        bc += ["C_root remains authority", "model/T2 output is evidence only", "answer must be read as residue/stub", "Ω must name typed residue"]
        anti += ["answer-first chatbot", "surface Nexus vocabulary", "untyped Ω", "model packet as authority"]
        fail += ["false Ψ", "empty residue", "branch-field degeneracy", "linear keyword memory"]
        profile = root_seed.get("admissible_shape", root_seed.get("name", "shapeir_runtime_compiler"))
        if "runtime" in prompt.lower() or "local ai" in prompt.lower() or "build" in prompt.lower():
            profile = "runtime_build"
        if "glyph" in prompt.lower() or "memory" in prompt.lower():
            profile = "spiral_glyph_reader"
        req = f"{' / '.join(ops[:4])}: {root_seed.get('required_operation', 'compile the prompt into executable shape')}"
        slot = NeedSlot(
            required_operation=req,
            preserved_function=root_seed.get("preserved_function", "preserve operational fit"),
            boundary_conditions=stable_dedupe(bc)[:16],
            anti_fits=stable_dedupe(anti)[:16],
            admissible_shape=root_seed.get("admissible_shape", profile),
            failure_modes=stable_dedupe(fail)[:14],
            profile=profile,
            origin="compiler_root+retrieval_seed_bank",
            confidence=1.0,
            semantic_locks=locks[:18],
            retrieved_seeds=[{k: r.get(k) for k in ["name", "score", "source", "section_id", "title"]} for r in retrieved],
        )
        shapeir = self.vna.shapeir_from_prompt(prompt, slot, retrieved)
        return slot, shapeir, retrieved

# -----------------------------
# AHRC / Samson / SILR / Glyph modules
# -----------------------------

class AHRC:
    @staticmethod
    def rasterize(values_01: List[float], N: int) -> Dict[str, Any]:
        bins = []
        counts = Counter()
        for x in values_01:
            x = float(x) % 1.0
            b = min(N - 1, max(0, int(math.floor(x * N))))
            bins.append(b); counts[b] += 1
        collisions = {int(k): int(v) for k, v in counts.items() if v > 1}
        omega_max = max([v - 1 for v in counts.values()] or [0])
        omega_total = sum(max(0, v - 1) for v in counts.values())
        return {"N": N, "bins": bins, "collisions": collisions, "omega_max": int(omega_max), "omega_total": int(omega_total)}

    @staticmethod
    def expand(values_01: List[float], N0: int = 8, max_N: int = 16384) -> Dict[str, Any]:
        N = max(2, int(N0))
        history = []
        while N <= max_N:
            r = AHRC.rasterize(values_01, N)
            history.append({"N": N, "omega_max": r["omega_max"], "omega_total": r["omega_total"], "collision_bins": len(r["collisions"])})
            if r["omega_max"] == 0:
                return {"resolved": True, "N_final": N, "history": history, "last": r}
            N *= 2
        return {"resolved": False, "N_final": N//2, "history": history, "last": history[-1] if history else {}}

class Samson:
    H_MARK1 = math.pi / 9

    @staticmethod
    def align(H: float) -> float:
        return clamp01(1.0 - abs(float(H) - Samson.H_MARK1) / max(1e-9, (1.0 - Samson.H_MARK1)))

    @staticmethod
    def from_branch_scores(scores: List[float]) -> Dict[str, Any]:
        if not scores:
            H = 0.0
        else:
            # Use score variance pressure as a normalized H proxy; stable field near mid-structure.
            mean = sum(scores) / len(scores)
            H = clamp01(mean / 1.8 + (max(scores)-min(scores)) / 2.0)
        return {"H_proxy": H, "H_MARK1": Samson.H_MARK1, "align": Samson.align(H)}

class SILR:
    @staticmethod
    def zscores(xs: List[float]) -> List[float]:
        if not xs:
            return []
        n = len(xs)
        mu = sum(xs)/n
        var = sum((x-mu)**2 for x in xs)/max(1, n)
        sd = math.sqrt(var)
        if sd < 1e-12:
            return [0.0 for _ in xs]
        return [(x-mu)/sd for x in xs]

    @staticmethod
    def gate(xs: List[float], z0: float = 1.0, beta: float = 2.5) -> Dict[str, Any]:
        zs = SILR.zscores(xs)
        ps = [sigmoid(beta*(z-z0)) for z in zs]
        events = [i for i, p in enumerate(ps) if p > 0.5]
        return {"z": zs, "p": ps, "events": events, "z0": z0, "beta": beta}

class GlyphReader:
    @staticmethod
    def spiral_coords(n: int) -> Dict[int, Tuple[int, int]]:
        # square spiral: 0 at center, then right/up/left/down.
        coords = {0: (0, 0)}
        x = y = 0
        step = 1
        idx = 1
        while idx < n:
            for dx, dy, run in [(1,0,step),(0,1,step),(-1,0,step+1),(0,-1,step+1)]:
                for _ in range(run):
                    if idx >= n:
                        break
                    x += dx; y += dy
                    coords[idx] = (x, y)
                    idx += 1
                if idx >= n:
                    break
            step += 2
        return coords

    @staticmethod
    def render(values: List[float], labels: Optional[List[str]] = None, width: int = 6) -> str:
        n = len(values)
        coords = GlyphReader.spiral_coords(n)
        xs = [c[0] for c in coords.values()]
        ys = [c[1] for c in coords.values()]
        minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
        grid = [[".".rjust(width) for _ in range(maxx-minx+1)] for __ in range(maxy-miny+1)]
        for i, (x,y) in coords.items():
            lab = labels[i] if labels else str(i)
            val = values[i]
            cell = f"{lab}:{val:.2f}"[-width:].rjust(width)
            grid[maxy-y][x-minx] = cell
        return "\n".join(" ".join(row) for row in grid)

    @staticmethod
    def certificate(branches: List[Branch], residue: List[str], ahrc: Dict[str, Any], silr: Dict[str, Any], samson: Dict[str, Any]) -> Dict[str, Any]:
        scores = [b.score for b in branches]
        labels = [b.role[:3] for b in branches]
        lattice = GlyphReader.render(scores, labels=labels) if scores else ""
        return {
            "glyph_lattice": lattice,
            "hot_branch_indices": silr.get("events", []),
            "ahrc_resolved": ahrc.get("resolved"),
            "ahrc_N_final": ahrc.get("N_final"),
            "samson_align": samson.get("align"),
            "residue_count": len(residue),
            "certificate_state": "Ψ" if not residue and ahrc.get("resolved") else "Ω",
        }

# -----------------------------
# Model adapter
# -----------------------------

class LocalModel:
    def __init__(self, model_id_or_path: str, local_files_only: bool = False):
        self.model_id_or_path = model_id_or_path
        self.local_files_only = local_files_only
        self.tokenizer = None
        self.model = None
        self.ready = False
        self.error = None

    def load(self) -> Dict[str, Any]:
        try:
            import torch
            from transformers import AutoTokenizer, AutoModelForCausalLM
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id_or_path, local_files_only=self.local_files_only, trust_remote_code=True)
            dtype = torch.float16 if torch.cuda.is_available() else torch.float32
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id_or_path,
                local_files_only=self.local_files_only,
                torch_dtype=dtype,
                device_map="auto" if torch.cuda.is_available() else None,
                trust_remote_code=True,
            )
            self.ready = True
            return {"model_ready": True, "model_id": self.model_id_or_path, "device": "cuda" if torch.cuda.is_available() else "cpu"}
        except Exception as e:
            self.error = f"{type(e).__name__}: {e}"
            self.ready = False
            return {"model_ready": False, "model_id": self.model_id_or_path, "error": self.error}

    def render_messages(self, messages: List[Dict[str, str]]) -> str:
        if self.tokenizer is not None and hasattr(self.tokenizer, "apply_chat_template"):
            try:
                return self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            except Exception:
                pass
        return "\n".join(f"{m.get('role','user').upper()}: {m.get('content','')}" for m in messages) + "\nASSISTANT:"

    def generate(self, messages: List[Dict[str, str]], max_new_tokens: int = 600, sample: bool = False) -> str:
        if not self.ready:
            raise RuntimeError("model not loaded")
        import torch
        prompt = self.render_messages(messages)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=bool(sample),
                temperature=0.2 if sample else None,
                top_p=0.9 if sample else None,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        new = out[0][inputs["input_ids"].shape[-1]:]
        return self.tokenizer.decode(new, skip_special_tokens=True).strip()

# -----------------------------
# Runtime scoring and control
# -----------------------------

class BindingScorer:
    def __init__(self, embed_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embed_model_name = embed_model_name
        self.embedder = None

    def load(self) -> Dict[str, Any]:
        try:
            from sentence_transformers import SentenceTransformer
            self.embedder = SentenceTransformer(self.embed_model_name)
            return {"embedder_ready": True, "embed_model": self.embed_model_name}
        except Exception as e:
            self.embedder = False
            return {"embedder_ready": False, "error": f"{type(e).__name__}: {e}", "fallback": "jaccard"}

    def cosine(self, a: str, b: str) -> float:
        if self.embedder:
            try:
                emb = self.embedder.encode([a, b], normalize_embeddings=True)
                return float(emb[0] @ emb[1])
            except Exception:
                pass
        return jaccard(a, b, remove_surface=True)

    def slot_bind_score(self, text: str, slot: NeedSlot) -> Tuple[float, Dict[str, float]]:
        pos_text = " ".join([slot.required_operation, slot.preserved_function, slot.admissible_shape] + slot.boundary_conditions + slot.semantic_locks)
        anti_text = " ".join(slot.anti_fits + slot.failure_modes)
        positive = self.cosine(text, pos_text)
        anti = self.cosine(text, anti_text)
        lock_ratio = overlap_ratio(slot.semantic_locks, text)
        req_overlap = jaccard(text, slot.required_operation, remove_surface=True)
        raw = 0.58*positive + 0.27*lock_ratio + 0.15*req_overlap - 0.38*anti
        return clamp01((raw + 0.25) / 1.15), {
            "positive_fit": round(positive,4),
            "anti_fit": round(anti,4),
            "semantic_lock_ratio": round(lock_ratio,4),
            "required_operation_overlap": round(req_overlap,4),
            "slot_bind_score": round(clamp01((raw + 0.25)/1.15),4),
        }


def runtime_artifact_score(text: str) -> float:
    s = str(text).lower()
    code_signals = ["```python", "def ", "class ", "import ", "from ", "return ", "dataclass", "path(", "json.dumps", "write_text", "pip install", "argparse", "if __name__"]
    notebook_signals = ["cell", "notebook", "run this", "paste", "save", "file", "patch", "execute", "output_dir"]
    return clamp01((sum(x in s for x in code_signals) + 0.45*sum(x in s for x in notebook_signals))/5.0)

def generic_plan_score(text: str) -> float:
    s = str(text).lower()
    plan_terms = ["we will", "we'll", "should", "ensure", "requirements", "criteria", "recommended", "step-by-step plan", "architecture should"]
    numbered = len(re.findall(r"\n\s*\d+\.", str(text)))
    return clamp01((sum(x in s for x in plan_terms) + min(numbered, 5)*0.35)/5.0) * (1.0 - 0.55*runtime_artifact_score(text))

class NexusShapeRuntime:
    def __init__(self, model_id_or_path: str = "Qwen/Qwen2.5-1.5B-Instruct", embed_model_name: str = "sentence-transformers/all-MiniLM-L6-v2", local_files_only: bool = False, out_dir: str = "nexus_shapeir_runs", psi_min: float = 0.61, margin_min: float = 0.045, max_depth: int = 2):
        self.model_id_or_path = model_id_or_path
        self.embed_model_name = embed_model_name
        self.local_files_only = local_files_only
        self.out_dir = Path(out_dir); self.out_dir.mkdir(parents=True, exist_ok=True)
        self.psi_min = psi_min
        self.margin_min = margin_min
        self.max_depth = max_depth
        self.memory = ShapeMemory(DEFAULT_SEEDS, embed_model_name=embed_model_name)
        self.compiler = ShapeIRCompiler(self.memory)
        self.scorer = BindingScorer(embed_model_name)
        self.model = LocalModel(model_id_or_path, local_files_only=local_files_only)
        self.load_info: Dict[str, Any] = {}

    def ingest_paths(self, paths: List[str | Path], max_sections_per_file: int = 80) -> Dict[str, Any]:
        info = self.memory.add_from_paths(paths, max_sections_per_file=max_sections_per_file)
        return info

    def load(self, load_model: bool = True, load_embedder: bool = True) -> Dict[str, Any]:
        info = {"runtime": "nexus_local_ai_v0.4_shapeir"}
        if load_embedder:
            info.update(self.scorer.load())
            # memory embedder loads lazily; no need to force.
        if load_model:
            info.update(self.model.load())
        else:
            info.update({"model_ready": False, "model_skipped": True})
        self.load_info = info
        return info

    def ask_model_for_slot_packet(self, prompt: str, root_slot: NeedSlot, shapeir: ShapeIR) -> ModelSlotPacket:
        if self.model is None or not self.model.ready:
            return ModelSlotPacket(prompt=prompt, raw="NO_MODEL", valid_json=False, conf=0.0)
        schema = {"task":"short task","op":"verb operation","pres":"preserved function","bounds":["short bound"],"anti":["short anti-fit"],"shape":"admissible shape","fail":["short failure"],"lock_add":{},"forbid":["short forbid"],"prompt":"short prompt summary","conf":0.75}
        root_short = {"op": root_slot.required_operation, "pres": root_slot.preserved_function, "bounds": root_slot.boundary_conditions[:6], "anti": root_slot.anti_fits[:6], "shape": root_slot.admissible_shape, "ShapeIR_sigma": shapeir.sigma}
        messages = [
            {"role":"system", "content":"Return ONE complete minified JSON object only. No markdown. No comments. lock_add must be {}. Short strings. Close every bracket."},
            {"role":"user", "content":"RAW PROMPT:\n"+prompt+"\n\nCOMPILER ROOT:\n"+json.dumps(root_short, ensure_ascii=False)+"\n\nSCHEMA:\n"+json.dumps(schema, ensure_ascii=False)+"\n\nReturn valid JSON only."},
        ]
        try:
            raw = self.model.generate(messages, max_new_tokens=420, sample=False)
        except Exception as e:
            return ModelSlotPacket(prompt=prompt, raw=f"GENERATION_ERROR:{type(e).__name__}:{e}", valid_json=False, conf=0.0)
        obj, err = parse_first_json_object(raw)
        if obj is None:
            return ModelSlotPacket(prompt=prompt, raw=raw, valid_json=False, conf=0.0)
        return ModelSlotPacket(
            task=str(obj.get("task", "")), op=str(obj.get("op", "")), pres=str(obj.get("pres", "")), bounds=normalize_list(obj.get("bounds", [])), anti=normalize_list(obj.get("anti", [])), shape=str(obj.get("shape", "")), fail=normalize_list(obj.get("fail", [])), lock_add=obj.get("lock_add", {}) if isinstance(obj.get("lock_add", {}), dict) else {}, forbid=normalize_list(obj.get("forbid", [])), prompt=str(obj.get("prompt", prompt)), conf=float(obj.get("conf", 0.0) or 0.0), raw=raw, valid_json=True)

    def slot_gate(self, root: NeedSlot, packet: ModelSlotPacket) -> Tuple[NeedSlot, Dict[str, Any]]:
        root_text = " ".join([root.required_operation, root.preserved_function, root.admissible_shape] + root.boundary_conditions + root.anti_fits)
        packet_text = " ".join([packet.task, packet.op, packet.pres, packet.shape] + packet.bounds + packet.anti + packet.fail)
        equivalence = jaccard(root_text, packet_text, remove_surface=True) if packet_text.strip() else 0.0
        less_constrained = len(packet.anti) < max(1, len(root.anti_fits)//4) or len(packet.bounds) < 1
        accepted = bool(packet.valid_json and packet.conf >= 0.55 and equivalence >= 0.12 and not less_constrained)
        gate = {
            "packet_valid_json": packet.valid_json,
            "packet_conf": packet.conf,
            "operational_equivalence_proxy": round(equivalence,4),
            "less_constrained": less_constrained,
            "accepted_as_authority": False,
            "accepted_as_evidence": accepted,
            "reason": "model_packet_evidence_only" if accepted else "fallback_root_model_packet_not_operationally_sufficient",
            "raw_packet_excerpt": compact_text(packet.raw, 800),
        }
        # The root remains authority even if packet is good evidence.
        return root, gate

    def branch_prompt(self, prompt: str, slot: NeedSlot, shapeir: ShapeIR, role: str, residue: List[str]) -> List[Dict[str, str]]:
        slot_json = json.dumps(asdict(slot), ensure_ascii=False, indent=2)
        shape_json = json.dumps(asdict(shapeir), ensure_ascii=False, indent=2)
        residue_text = "\n".join(f"- {r}" for r in residue) if residue else "- none"
        sys = (
            "You are a Nexus ShapeIR branch generator. "
            "Do not answer from surface vocabulary. Read the prompt as ι, compile Δ and Δ^-1, pass through Σ, and emit concrete residue. "
            "For runtime_build, emit runnable code/notebook patch material or exact executable next operation. "
            "C_root is authority; model text is evidence only."
        )
        user = (
            f"BRANCH ROLE: {role}\n\nRAW PROMPT:\n{prompt}\n\nACCEPTED SLOT:\n{slot_json}\n\nSHAPEIR:\n{shape_json}\n\nCURRENT RESIDUE:\n{residue_text}\n\n"
            "Produce the branch output. If building, include paste-ready code/cell material. If unresolved, name the Ω residue precisely."
        )
        return [{"role":"system","content":sys}, {"role":"user","content":user}]

    def deterministic_fallback_branch(self, prompt: str, slot: NeedSlot, shapeir: ShapeIR, role: str, residue: List[str]) -> str:
        if slot.profile == "runtime_build" or "build" in prompt.lower():
            return """Paste/run this v0.4 ShapeIR smoke cell:

```python
# v0.4 ShapeIR smoke test
PROMPT = "build the Nexus local AI as a ShapeIR runtime"
slot, shapeir, retrieved = rt.compiler.compile(PROMPT)
packet = rt.ask_model_for_slot_packet(PROMPT, slot, shapeir)
accepted, gate = rt.slot_gate(slot, packet)
print("Σ:", shapeir.sigma)
print("C_root:", slot.required_operation)
print("S_model_valid:", packet.valid_json)
print("Gate:", gate)
result = rt.run(PROMPT, save=True)
nexus_shape_readout_v04(result)
```

This performs the operation: raw need → ShapeIR → retrieval-root slot → model evidence gate → branch field → AHRC/SILR/Glyph certificate → Ψ/Ω/Σ/⊥/ρ."""
        return f"ShapeIR branch {role}: ι={shapeir.iota}; Δ={shapeir.delta}; Σ={shapeir.sigma}; operation={slot.required_operation}; unresolved residue={residue or 'none'}"

    def generate_branches(self, prompt: str, slot: NeedSlot, shapeir: ShapeIR, residue: List[str]) -> List[Branch]:
        roles = ["shapeir_direct", "ahrc_resolution", "silr_hotspot_gate", "glyph_readhead", "compiler_breath_promotion"]
        branches = []
        for role in roles:
            if self.model.ready:
                try:
                    text = self.model.generate(self.branch_prompt(prompt, slot, shapeir, role, residue), max_new_tokens=700, sample=False)
                except Exception as e:
                    text = f"MODEL_BRANCH_ERROR {type(e).__name__}: {e}\n" + self.deterministic_fallback_branch(prompt, slot, shapeir, role, residue)
            else:
                text = self.deterministic_fallback_branch(prompt, slot, shapeir, role, residue)
            branches.append(Branch(role=role, text=text))
        return branches

    def audit_branch(self, branch: Branch, prompt: str, slot: NeedSlot, shapeir: ShapeIR) -> Branch:
        slot_score, dims = self.scorer.slot_bind_score(branch.text, slot)
        prompt_fit = self.scorer.cosine(branch.text, prompt)
        length = len(words(branch.text))
        length_score = clamp01(length / 75.0) if length < 75 else clamp01(1.15 - max(0, length - 260)/520.0)
        artifact = runtime_artifact_score(branch.text) if (slot.profile == "runtime_build" or "build" in prompt.lower()) else 0.0
        generic = generic_plan_score(branch.text)
        shapeir_fit = jaccard(branch.text, " ".join([shapeir.iota, shapeir.delta, shapeir.delta_inverse, shapeir.sigma, shapeir.response_operator]), remove_surface=True)
        residue_flags = []
        if dims["anti_fit"] > dims["positive_fit"] + 0.03:
            residue_flags.append("anti_fit_exceeds_positive_fit")
        if prompt_fit < 0.10:
            residue_flags.append("low_prompt_fit")
        if length < 25:
            residue_flags.append("too_short_to_preserve_function")
        if slot.profile == "runtime_build" or "build" in prompt.lower():
            if artifact < 0.28:
                residue_flags.append("runtime_build_no_executable_artifact")
            if generic > 0.45:
                residue_flags.append("generic_plan_instead_of_build")
        if shapeir_fit < 0.05:
            residue_flags.append("shapeir_decoupled")
        quality = 0.50*slot_score + 0.16*clamp01((prompt_fit+0.1)/0.9) + 0.12*length_score + 0.16*shapeir_fit + 0.18*artifact - 0.14*generic
        branch.score = round(clamp01(quality), 4)
        branch.dimensions = {**dims, "prompt_fit": round(prompt_fit,4), "length_score": round(length_score,4), "word_count": length, "runtime_artifact_score": round(artifact,4), "generic_plan_score": round(generic,4), "shapeir_fit": round(shapeir_fit,4)}
        branch.rejection_reasons = stable_dedupe(residue_flags)
        return branch

    def patch_slot_from_residue(self, slot: NeedSlot, shapeir: ShapeIR, residue: List[str]) -> Tuple[NeedSlot, ShapeIR]:
        if not residue:
            return slot, shapeir
        patched = NeedSlot(**asdict(slot))
        rho = list(shapeir.rho)
        sigma_next = list(shapeir.sigma_next)
        for rr in residue:
            r = str(rr)
            rho.append(r)
            if r.startswith("branch_field_low_margin"):
                patched.boundary_conditions = stable_dedupe(patched.boundary_conditions + ["low-margin branch fields require AHRC/SILR/Glyph certificate or remain Ω"])
                patched.failure_modes = stable_dedupe(patched.failure_modes + ["branch-field degeneracy"])
                sigma_next.append("operator:increase_probe_diversity")
            elif r == "runtime_build_no_executable_artifact":
                patched.boundary_conditions = stable_dedupe(patched.boundary_conditions + ["runtime_build must emit runnable code, notebook cell, or file patch"])
                patched.anti_fits = stable_dedupe(patched.anti_fits + ["requirements list without executable artifact"])
                sigma_next.append("operator:require_executable_artifact")
            elif r == "generic_plan_instead_of_build":
                patched.anti_fits = stable_dedupe(patched.anti_fits + ["generic plan that describes but does not build"])
                sigma_next.append("operator:block_generic_plan")
            elif r == "shapeir_decoupled":
                patched.boundary_conditions = stable_dedupe(patched.boundary_conditions + ["branch must bind to ι Δ Δ^-1 Σ RΛ ρ D"])
                sigma_next.append("operator:bind_shapeir_nodes")
            elif r == "model_packet_invalid_json":
                patched.boundary_conditions = stable_dedupe(patched.boundary_conditions + ["model packet must be compact valid JSON or be quarantined"])
                sigma_next.append("operator:compact_packet_request")
            else:
                sigma_next.append(f"operator:address_{re.sub(r'[^a-zA-Z0-9_]+','_',r)[:48]}")
        patched.origin = patched.origin + "+residue_patch"
        new_shape = ShapeIR(**asdict(shapeir))
        new_shape.rho = stable_dedupe(rho)
        new_shape.sigma_next = stable_dedupe(sigma_next)
        new_shape.state = "Ω"
        return patched, new_shape

    def collapse(self, prompt: str, slot: NeedSlot, shapeir: ShapeIR, branches: List[Branch], depth: int, residue: List[str]) -> Tuple[str, Branch, str, List[str], Dict[str, Any], ShapeIR]:
        ordered = sorted(branches, key=lambda b: b.score, reverse=True)
        top = ordered[0]
        runner = ordered[1] if len(ordered) > 1 else None
        margin = top.score - (runner.score if runner else 0.0)
        new_residue = list(residue)
        for b in ordered:
            for rr in b.rejection_reasons:
                if rr not in new_residue:
                    new_residue.append(rr)
        if runner and margin < self.margin_min:
            new_residue.append(f"branch_field_low_margin:{round(margin,4)}")
        if not new_residue and top.score < self.psi_min:
            new_residue.append("score_below_psi_without_localized_failure")
        scores = [b.score for b in ordered]
        # AHRC over branch scores: normalize scores into [0,1] trajectory.
        if scores:
            mn, mx = min(scores), max(scores)
            vals = [(s-mn)/(mx-mn+1e-9) for s in scores]
        else:
            vals = []
        ahrc = AHRC.expand(vals, N0=8, max_N=2048) if vals else {"resolved": False, "N_final": None, "history": []}
        silr = SILR.gate(scores, z0=0.75, beta=2.0) if scores else {"events": [], "z": [], "p": []}
        samson = Samson.from_branch_scores(scores)
        glyph_cert = GlyphReader.certificate(ordered, new_residue, ahrc, silr, samson)
        new_shape = ShapeIR(**asdict(shapeir))
        new_shape.rho = stable_dedupe(list(new_shape.rho) + new_residue)
        new_shape.D = {**new_shape.D, "branch_scores": scores, "top_role": top.role, "margin": round(margin,4), "ahrc": ahrc, "silr": {"events": silr.get("events", []), "z": [round(z,4) for z in silr.get("z", [])], "p": [round(p,4) for p in silr.get("p", [])]}, "samson": samson}
        new_shape.certificate = glyph_cert
        telemetry = {"top_role": top.role, "top_score": top.score, "runner_score": runner.score if runner else None, "margin": round(margin,4), "depth": depth, "profile": slot.profile, "residue_count": len(new_residue), "ahrc_resolved": ahrc.get("resolved"), "ahrc_N_final": ahrc.get("N_final"), "silr_events": silr.get("events", []), "samson_align": round(samson.get("align",0),4), "glyph_certificate_state": glyph_cert.get("certificate_state")}
        clean = (not top.rejection_reasons) and (not new_residue or all(str(r).startswith("branch_field_low_margin") for r in new_residue) is False)
        if top.score >= self.psi_min and margin >= self.margin_min and not top.rejection_reasons and len(new_residue)==0:
            new_shape.state = "Ψ"
            return "Ψ", top, "psi_score_margin_clean_shapeir_closed", new_residue, telemetry, new_shape
        if top.score >= self.psi_min and margin >= self.margin_min and glyph_cert.get("certificate_state") == "Ψ" and not top.rejection_reasons:
            new_shape.state = "Ψ"
            return "Ψ", top, "psi_glyph_certificate_closed", new_residue, telemetry, new_shape
        if depth >= self.max_depth:
            new_shape.state = "Ω" if top.score >= 0.25 else "⊥"
            if top.score < 0.25:
                return "⊥", top, "dead_branch_low_score_after_max_depth", new_residue, telemetry, new_shape
            if any(str(r).startswith("branch_field_low_margin") for r in new_residue):
                return "Ω", top, "omega_branch_field_degenerate_after_max_depth", new_residue, telemetry, new_shape
            return "Ω", top, "omega_shaped_residue_after_max_depth", new_residue, telemetry, new_shape
        new_shape.state = "Ω"
        return "Ω", top, "omega_recurse_on_residue", new_residue, telemetry, new_shape

    def run(self, prompt: str, save: bool = True) -> CollapseResult:
        run_id = "nexus_shapeir_" + uuid.uuid4().hex[:10]
        root_slot, shapeir, retrieved = self.compiler.compile(prompt)
        packet = self.ask_model_for_slot_packet(prompt, root_slot, shapeir)
        accepted_slot, gate = self.slot_gate(root_slot, packet)
        residue: List[str] = []
        if not packet.valid_json and self.model.ready:
            residue.append("model_packet_invalid_json")
        slot = accepted_slot
        branches: List[Branch] = []
        final_top = None
        final_state = "Ω"
        final_reason = "not_run"
        final_telemetry: Dict[str, Any] = {}
        final_shapeir = shapeir
        for depth in range(self.max_depth + 1):
            branches = self.generate_branches(prompt, slot, final_shapeir, residue)
            branches = [self.audit_branch(b, prompt, slot, final_shapeir) for b in branches]
            state, top, reason, residue, telemetry, final_shapeir = self.collapse(prompt, slot, final_shapeir, branches, depth, residue)
            final_top, final_state, final_reason, final_telemetry = top, state, reason, telemetry
            if state == "Ψ" or state == "⊥":
                break
            slot, final_shapeir = self.patch_slot_from_residue(slot, final_shapeir, residue)
        result = CollapseResult(
            run_id=run_id,
            prompt=prompt,
            state=final_state,
            reason=final_reason,
            answer=final_top.text if final_top else "",
            root_slot=asdict(root_slot),
            accepted_slot=asdict(slot),
            accepted_slot_origin=slot.origin,
            shapeir=asdict(final_shapeir),
            gate=gate,
            branches=[asdict(b) for b in sorted(branches, key=lambda x: x.score, reverse=True)],
            residue=stable_dedupe(residue),
            telemetry=final_telemetry,
        )
        if save:
            p = self.out_dir / f"{run_id}_result.json"
            p.write_text(json.dumps(asdict(result), indent=2, ensure_ascii=False), encoding="utf-8")
        return result

# -----------------------------
# Readout helpers
# -----------------------------

def nexus_shape_readout_v04(result: CollapseResult):
    import pandas as pd
    r = asdict(result) if is_dataclass(result) else result
    print("Δ NEXUS SHAPEIR READOUT v0.4")
    print("="*88)
    for k in ["run_id", "state", "reason", "accepted_slot_origin", "residue"]:
        print(f"{k}: {r.get(k)}")
    print("\nΣ / ShapeIR:")
    shape = r.get("shapeir", {})
    for k in ["iota", "delta", "delta_inverse", "sigma", "response_operator", "state"]:
        print(f"{k}: {shape.get(k)}")
    print("\nGate:")
    print(json.dumps(r.get("gate", {}), indent=2, ensure_ascii=False)[:4000])
    print("\nTelemetry:")
    print(json.dumps(r.get("telemetry", {}), indent=2, ensure_ascii=False)[:4000])
    cert = shape.get("certificate", {})
    if cert.get("glyph_lattice"):
        print("\nGlyph lattice:")
        print(cert["glyph_lattice"])
    rows = []
    for b in r.get("branches", []):
        row = {"role": b.get("role"), "score": b.get("score"), "rejection_reasons": " | ".join(b.get("rejection_reasons", []))}
        row.update(b.get("dimensions", {}))
        rows.append(row)
    df = pd.DataFrame(rows)
    if len(df):
        try:
            display(df.sort_values("score", ascending=False))
        except Exception:
            print(df.sort_values("score", ascending=False).to_string(index=False))
    out = Path("nexus_shapeir_runs") / f"{r.get('run_id','latest')}_shapeir_readout_v04.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(r, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nSaved ShapeIR trace:", out)
    return df

print("Nexus Local AI v0.4 ShapeIR runtime loaded.")
