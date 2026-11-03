#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Iterable, Protocol
import json


class DualRead(Protocol):
    def forward(self, state: Any) -> float: ...
    def reverse(self, state: Any) -> float: ...
    def parameter(self, state: Any) -> tuple[float, ...]: ...


@dataclass(frozen=True)
class Sample:
    state: Any
    forward: float
    reverse: float
    residual: float
    parameters: tuple[float, ...]


@dataclass(frozen=True)
class ZeroCrossing:
    parameter_index: int
    left_parameter: float
    right_parameter: float
    estimated_parameter: float
    residual_left: float
    residual_right: float


class DualReadResidualEngine:
    """
    Generic dual-read residual scanner.

    The engine knows nothing about pi, BBP, [4,-2,-1,-1], or the expected
    surviving frame. A domain adapter supplies the exact forward/reverse reads.
    """

    def __init__(self, reader: DualRead, tolerance: float = 1e-12):
        if tolerance <= 0:
            raise ValueError("tolerance must be > 0")
        self.reader = reader
        self.tolerance = tolerance

    def sample(self, states: Iterable[Any]) -> list[Sample]:
        out = []
        for state in states:
            f = float(self.reader.forward(state))
            r = float(self.reader.reverse(state))
            out.append(
                Sample(
                    state=state,
                    forward=f,
                    reverse=r,
                    residual=f - r,
                    parameters=tuple(self.reader.parameter(state)),
                )
            )
        return out

    def zeros_on_1d_grid(
        self, states: list[Any], parameter_index: int = 0
    ) -> list[ZeroCrossing]:
        if len(states) < 2:
            return []

        samples = sorted(
            self.sample(states),
            key=lambda s: s.parameters[parameter_index],
        )

        zeros = []
        for i, s in enumerate(samples):
            p = s.parameters[parameter_index]
            if abs(s.residual) <= self.tolerance:
                zeros.append(
                    ZeroCrossing(
                        parameter_index,
                        p, p, p, s.residual, s.residual
                    )
                )

            if i == 0:
                continue

            a = samples[i - 1]
            b = s
            ra, rb = a.residual, b.residual
            if abs(ra) <= self.tolerance or abs(rb) <= self.tolerance:
                continue

            if ra * rb < 0.0:
                pa = a.parameters[parameter_index]
                pb = b.parameters[parameter_index]
                alpha = -ra / (rb - ra)
                pz = pa + alpha * (pb - pa)
                zeros.append(
                    ZeroCrossing(
                        parameter_index,
                        pa, pb, pz, ra, rb
                    )
                )
        return zeros


def residual_statistics(samples: list[Sample]) -> dict[str, float]:
    if not samples:
        return {"count": 0.0}

    abs_r = [abs(s.residual) for s in samples]
    return {
        "count": float(len(samples)),
        "max_abs_residual": max(abs_r),
        "mean_abs_residual": sum(abs_r) / len(abs_r),
        "near_zero_count": float(sum(r <= 1e-12 for r in abs_r)),
    }


def export_json(
    samples: list[Sample],
    crossings: list[ZeroCrossing],
    path: str,
) -> None:
    payload = {
        "samples": [asdict(s) for s in samples],
        "crossings": [asdict(c) for c in crossings],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)


class HexagonalReadNotImplemented:
    """
    Deliberate safety boundary.

    The corpus supplies the common BBP operator and proposes a forward/reverse
    arm interpretation, but the exact two executable arm functions have not
    been supplied as code here. Refusing to invent them prevents artificial
    zero residuals.
    """

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(
            "Supply the exact hexagonal forward/reverse arm definitions "
            "before running discovery."
        )


if __name__ == "__main__":
    print("DUAL-READ RESIDUAL ENGINE")
    print("=========================")
    print("Generic engine: READY")
    print("Target constants/residues: NONE")
    print("Hexagonal adapter: awaiting exact forward/reverse arms")
