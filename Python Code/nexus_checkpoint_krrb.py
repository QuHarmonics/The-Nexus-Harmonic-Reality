# nexus_checkpoint_krrb.py
# Features -> routing state {BORN,GESTATE,REFLECT,DEFER,EOL}
# Δ-channel ladder and KRRB branching scaffold.

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Callable, Any
import math

H_DEFAULT = math.pi / 9.0

@dataclass
class CheckpointParams:
    H: float = H_DEFAULT
    tau_byte: float = 0.05      # byte pin threshold
    theta_scar: float = 0.50    # scar threshold on transitions
    p_min: int = 2              # minimal pins for object closure
    g_max: float = 0.22         # max mean gap for BORN
    s_max: int = 8              # max scars for BORN
    g_gestate: float = 0.30     # mean gap bound for gestation
    E_gestate: float = 6.0      # scar energy bound for gestation
    g_reflect: float = 0.30     # mean gap bound for reflection (still near H)
    E_reflect: float = 10.0     # scar energy threshold for reflection
    tau_word: float = 0.06      # optional word pin threshold
    eol_flag: bool = False      # explicit lifecycle (linear) EOL

@dataclass
class DigestFeatures:
    x: List[float]
    g: List[float]
    pins: List[int]
    pin_count: int
    g_mean: float
    transitions: List[float]
    scars: List[int]
    scar_count: int
    scar_energy: float
    y_words: Optional[List[float]] = None
    g_words: Optional[List[float]] = None
    word_pins: Optional[List[int]] = None

def bytes_to_words_be(digest_bytes: bytes) -> List[int]:
    if len(digest_bytes) != 32:
        raise ValueError("digest_bytes must be length 32")
    words = []
    for i in range(0, 32, 4):
        w = (digest_bytes[i] << 24) | (digest_bytes[i+1] << 16) | (digest_bytes[i+2] << 8) | digest_bytes[i+3]
        words.append(w)
    return words

def compute_features(digest_bytes: bytes, p: CheckpointParams) -> DigestFeatures:
    if len(digest_bytes) != 32:
        raise ValueError("digest_bytes must be 32 bytes")
    x = [b / 255.0 for b in digest_bytes]
    g = [abs(xi - p.H) for xi in x]
    pins = [i for i,gi in enumerate(g) if gi <= p.tau_byte]
    g_mean = sum(g) / 32.0

    transitions = [abs(x[i+1] - x[i]) for i in range(31)]
    scars = [i for i,ti in enumerate(transitions) if ti >= p.theta_scar]
    scar_energy = sum(transitions[i] for i in scars)

    words = bytes_to_words_be(digest_bytes)
    y = [w / (2**32 - 1) for w in words]
    Gw = [abs(yj - p.H) for yj in y]
    word_pins = [j for j,gj in enumerate(Gw) if gj <= p.tau_word]

    return DigestFeatures(
        x=x, g=g, pins=pins, pin_count=len(pins), g_mean=g_mean,
        transitions=transitions, scars=scars, scar_count=len(scars), scar_energy=scar_energy,
        y_words=y, g_words=Gw, word_pins=word_pins
    )

BORN = "BORN"
GESTATE = "GESTATE"
REFLECT = "REFLECT"
DEFER = "DEFER"
EOL = "EOL"

def classify(feat: DigestFeatures, p: CheckpointParams,
             resolvable: Optional[bool]=None, tension: Optional[float]=None) -> str:
    # Linear EOL (scope end)
    if p.eol_flag:
        return EOL

    # Optional higher-layer routing: DEFER if unresolved + high tension
    if resolvable is not None and tension is not None:
        if (not resolvable) and (tension > 0.5):
            return DEFER

    # Encapsulated object
    if (feat.pin_count >= p.p_min) and (feat.g_mean <= p.g_max) and (feat.scar_count <= p.s_max):
        return BORN

    # Fragile pre-object (fetus)
    if (feat.pin_count < p.p_min) and (feat.g_mean <= p.g_gestate) and (feat.scar_energy <= p.E_gestate):
        return GESTATE

    # Macro↔quantum bounce: near H but tearing too hard
    if (feat.g_mean <= p.g_reflect) and ((feat.scar_count > p.s_max) or (feat.scar_energy > p.E_reflect)):
        return REFLECT

    # Default safe routing: reflect (not “dead”)
    return REFLECT


# ---------------- Δ-channel ladder and KRRB scaffold ----------------

DeltaExtractor = Callable[[Any], Any]

def delta0_from_features(feat: DigestFeatures) -> Dict[str, Any]:
    return {"pins": feat.pins, "scars": feat.scars, "word_pins": feat.word_pins}

def delta1_carry_bits_from_trace(trace: Any) -> Any:
    # expects per-round raw sums (pre-mod) to extract carry bits
    raise NotImplementedError

def delta2_state_anchors(trace: Any, anchor_rounds: List[int]) -> Any:
    raise NotImplementedError

@dataclass
class Branch:
    name: str
    delta_extractor: DeltaExtractor
    score: float = 0.0

def krrb_search(branches: List[Branch],
                cases: List[Tuple[bytes, Dict[str, Any]]],
                params: CheckpointParams) -> List[Branch]:
    scored: List[Branch] = []
    for br in branches:
        total = 0.0
        for digest_bytes, meta in cases:
            feat = compute_features(digest_bytes, params)
            state = classify(feat, params,
                             resolvable=meta.get("resolvable"),
                             tension=meta.get("tension"))

            # match expected state if given
            exp = meta.get("expected_state")
            if exp is not None:
                total += 1.0 if state == exp else 0.0
            else:
                total += 1.0 if state in (BORN, GESTATE) else 0.2

            # ensure delta extractor is callable
            try:
                if br.name.startswith("delta0"):
                    _ = br.delta_extractor(feat)
                else:
                    _ = br.delta_extractor(meta.get("trace"))
                total += 0.1
            except NotImplementedError:
                total += 0.0

        br.score = total / max(1, len(cases))
        scored.append(br)

    scored.sort(key=lambda b: b.score, reverse=True)
    return scored
