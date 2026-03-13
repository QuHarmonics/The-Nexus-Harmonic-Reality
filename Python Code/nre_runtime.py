
from __future__ import annotations

"""
Nexus Runtime Environment (NRE) — Notebook-ready module + demos

Save to:
  D:\\nexus\\data\\nre_project\\nre_runtime.py

Run in Jupyter:
  %run D:\\nexus\\data\\nre_project\\nre_runtime.py

or import via importlib.
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple, List
import math
import numpy as np


# ============================================================
# Exceptions
# ============================================================

class BufferUnderrun(RuntimeError):
    """Raised when internal update budget cannot meet minimum (event-horizon / lag-out)."""
    pass


# ============================================================
# Core Kernel (Physics)
# ============================================================

class IBandwidthConstrained(ABC):
    @property
    @abstractmethod
    def N(self) -> int: ...

    @property
    @abstractmethod
    def beta(self) -> float: ...

    @abstractmethod
    def allocate_budgets(self) -> Tuple[int, int, float, float, float]: ...


@dataclass
class Universe:
    """Universe singleton with a simple gravity-like budget-tax field."""
    N_default: int = 1024
    gravity_sources: List["Mass"] = field(default_factory=list)

    def register_mass(self, m: "Mass") -> None:
        self.gravity_sources.append(m)

    def gravity_drag(self, position: float) -> int:
        """Integer tax on local budget from nearby masses: sum(ceil(strength/(d+eps)))."""
        eps = 1e-6
        tax = 0
        for src in self.gravity_sources:
            d = abs(position - src.position) + eps
            tax += int(math.ceil(src.strength / d))
        return tax


UNIVERSE = Universe()


@dataclass
class Observer(IBandwidthConstrained):
    """
    Bandwidth-constrained Observer.

    Integer scheduler:
        N_eff = N - gravity_tax
        Bm   = round(beta * N_eff)
        Bi   = floor(sqrt(N_eff^2 - Bm^2))
        dτ/dt = Bi / N_eff
        γ     = 1 / (dτ/dt)
    """
    name: str = "observer"
    position: float = 0.0
    _beta: float = 0.0
    N_override: Optional[int] = None

    proper_time: float = 0.0
    coord_time: float = 0.0
    last: Dict[str, float] = field(default_factory=dict)

    @property
    def N(self) -> int:
        return int(self.N_override if self.N_override is not None else UNIVERSE.N_default)

    @property
    def beta(self) -> float:
        return max(0.0, min(float(self._beta), 0.999999999))

    @beta.setter
    def beta(self, v: float) -> None:
        self._beta = float(v)

    def allocate_budgets(self) -> Tuple[int, int, float, float, float]:
        N = self.N
        tax = UNIVERSE.gravity_drag(self.position)
        N_eff = max(1, N - tax)

        Bm = int(round(self.beta * N_eff))
        Bm = max(0, min(Bm, N_eff))

        Bi = int(math.floor(math.sqrt(max(0, N_eff * N_eff - Bm * Bm))))

        beta_eff = (Bm / N_eff) if N_eff > 0 else 0.0
        dtaudt = (Bi / N_eff) if N_eff > 0 else 0.0
        gamma = float("inf") if dtaudt <= 0 else 1.0 / dtaudt

        self.last = dict(
            N=float(N),
            tax=float(tax),
            N_eff=float(N_eff),
            Bm=float(Bm),
            Bi=float(Bi),
            beta_req=float(self.beta),
            beta_eff=float(beta_eff),
            dtaudt=float(dtaudt),
            gamma=float(gamma),
        )
        return Bm, Bi, beta_eff, dtaudt, gamma

    def Tick(self, dt: float = 1.0, min_internal_bits: int = 1) -> Dict[str, float]:
        self.coord_time += dt
        self.allocate_budgets()

        if int(self.last["Bi"]) < int(min_internal_bits):
            raise BufferUnderrun(
                f"{self.name}: BufferUnderrun (Bi={int(self.last['Bi'])} < {min_internal_bits}). "
                f"Event horizon at beta_eff={self.last['beta_eff']:.6f} with N_eff={int(self.last['N_eff'])}."
            )

        self.proper_time += dt * float(self.last["dtaudt"])

        out = dict(self.last)
        out.update(coord_time=float(self.coord_time), proper_time=float(self.proper_time))
        return out


@dataclass
class Mass(Observer):
    """A mass both observes and creates a gravity-like budget tax for others."""
    strength: float = 128.0

    def __post_init__(self) -> None:
        UNIVERSE.register_mass(self)


# ============================================================
# Biological Runtime (Life)
# ============================================================

class ISpectral(ABC):
    @abstractmethod
    def GetSpectralEntropy(self) -> Tuple[float, float, float]: ...


@dataclass
class Geometry:
    kind: str = "Geometry"
    details: Dict[str, float] = field(default_factory=dict)


@dataclass
class Fluid:
    kind: str = "Fluid"
    details: Dict[str, float] = field(default_factory=dict)


KYTE_DOOLITTLE: Dict[str, float] = {
    "I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5,
    "M": 1.9, "A": 1.8, "G": -0.4, "T": -0.7, "S": -0.8,
    "W": -0.9, "Y": -1.3, "P": -1.6, "H": -3.2, "E": -3.5,
    "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5,
}


@dataclass
class Protein(ISpectral):
    name: str
    sequence: str
    sigma_crit: float = 0.88

    def _clean(self) -> Tuple[str, Dict[str, int]]:
        seq = (self.sequence or "").upper()
        dropped: Dict[str, int] = {}
        kept = []
        for ch in seq:
            if ch in KYTE_DOOLITTLE:
                kept.append(ch)
            elif ch.isalpha():
                dropped[ch] = dropped.get(ch, 0) + 1
        return "".join(kept), dropped

    def GetSpectralEntropy(self) -> Tuple[float, float, float]:
        cleaned, _ = self._clean()
        x = np.array([KYTE_DOOLITTLE[a] for a in cleaned], dtype=float)
        L = int(len(x))
        if L < 2:
            return 0.0, 0.0, 0.0

        X = np.fft.rfft(x)
        P = (np.abs(X) ** 2)
        total = float(P.sum())
        if total <= 0:
            return 0.0, 0.0, 0.0

        p = P / total
        mask = p > 0
        H = float(-(p[mask] * np.log2(p[mask])).sum())

        K = int(len(p))
        Hmax = float(math.log2(K)) if K > 1 else 0.0
        sigma = (H / Hmax) if Hmax > 0 else 0.0
        return H, Hmax, sigma

    def gamma_bio(self) -> float:
        _, _, sigma = self.GetSpectralEntropy()
        sigma = max(0.0, min(float(sigma), 0.999999999))
        return 1.0 / math.sqrt(1.0 - sigma * sigma)

    def Fold(self) -> object:
        H, Hmax, sigma = self.GetSpectralEntropy()
        g = float("inf") if sigma >= 1.0 else 1.0 / math.sqrt(max(1e-12, 1.0 - sigma * sigma))
        payload = {"H": float(H), "Hmax": float(Hmax), "sigma": float(sigma), "gamma_bio": float(g)}

        if sigma > self.sigma_crit:
            return Geometry(details=payload)
        return Fluid(details=payload)


# ============================================================
# Demos
# ============================================================

def demo_physics_integer_scheduler(
    betas=(0.0, 0.5, 0.8, 0.9, 0.99, 0.999),
    N: int = 1024,
    with_gravity: bool = True,
) -> List[Dict[str, float]]:
    UNIVERSE.N_default = int(N)
    UNIVERSE.gravity_sources = []

    if with_gravity:
        Mass(name="M0", position=0.0, _beta=0.0, strength=N * 0.10)

    o = Observer(name="O", position=1.0)
    rows: List[Dict[str, float]] = []
    for b in betas:
        o.beta = b
        try:
            rows.append(o.Tick())
        except BufferUnderrun as e:
            rows.append({**o.last, "coord_time": float(o.coord_time), "proper_time": float(o.proper_time), "error": str(e)})
    return rows


def demo_biology_sequences() -> List[Tuple[str, object, Dict[str, int]]]:
    ubiquitin = "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG"
    alpha_syn = "MDVFMKGLSKAKEGVVAAAEKTKQGVAEAAGKTKEGVLYVGSKTKEGVVHGVATVAEKTKEQVTNVGGAVVTGVTAVAQKTVEGAGSIAAATGFVKKDQLGKNEEGAPQEGILEDMPVDPDNEAYEMPSEEGYQDYEPEAGO"

    out = []
    for name, seq in [("Ubiquitin", ubiquitin), ("Alpha-synuclein", alpha_syn)]:
        p = Protein(name=name, sequence=seq, sigma_crit=0.88)
        cleaned, dropped = p._clean()
        out.append((name, p.Fold(), dropped))
    return out


def demo_all() -> None:
    print("=" * 72)
    print("NRE Demo: Integer Update Budget (Physics)")
    print("=" * 72)
    for r in demo_physics_integer_scheduler():
        if "error" in r:
            print(f"beta_req={r['beta_req']:.3f} beta_eff={r['beta_eff']:.6f} N_eff={int(r['N_eff'])} tax={int(r['tax'])} -> ERROR: {r['error']}")
        else:
            print(f"beta_req={r['beta_req']:.3f} beta_eff={r['beta_eff']:.6f} N_eff={int(r['N_eff'])} tax={int(r['tax'])}  dτ/dt={r['dtaudt']:.6f}  γ={r['gamma']:.6f}")

    print("\n" + "=" * 72)
    print("NRE Demo: Spectral Folding (Biology)")
    print("=" * 72)
    for name, res, dropped in demo_biology_sequences():
        kind = getattr(res, "kind", type(res).__name__)
        d = getattr(res, "details", {})
        print(f"{name}")
        print(f"  dropped_nonstandard: {dropped if dropped else '{}'}")
        print(f"  sigma:      {d.get('sigma'):.6f}")
        print(f"  gamma_bio:  {d.get('gamma_bio'):.6f}")
        print(f"  regime:     {kind}  (sigma_crit=0.88)")
        print("-" * 72)


if __name__ == "__main__":
    demo_all()
