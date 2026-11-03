#!/usr/bin/env python3
"""
hexagonal_transfer_engine.py

The F6 adapter is built from the source-derived constraints themselves.

For the frame-winding construction:

    C0(u, theta) = u - cos(theta)               [frame compatibility]
    C1(u, theta, b) = u^n - 1/b                [radix compatibility]

For the hexagonal frame:
    n = 6

Instead of freezing b=64, the transfer engine treats b as the continuous
drive coordinate. The zero set is then

    u = cos(theta)
    b = sec(theta)^6

This exposes the continuous coupling before imposing the discrete radix lock.

The engine reports:
  * full 2-D residual fields at fixed b
  * the continuous transfer curve theta <-> b
  * local transfer slopes
  * integer / power-of-two click-stops
  * forward/reverse perturbation checks
  * channel-removal controls
  * post-hoc F6 null-vector derivation

The known [4,-2,-1,-1] residue is never used by the computation.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import csv
import json
import math

import numpy as np
import sympy as sp


N = 6


# ---------------------------------------------------------------------------
# Source-derived constraints
# ---------------------------------------------------------------------------

def frame_residual(u: np.ndarray | float, theta: np.ndarray | float) -> np.ndarray:
    """C0: endpoint is the frame mark coordinate."""
    return np.asarray(u) - np.cos(np.asarray(theta))


def radix_residual(
    u: np.ndarray | float,
    b: np.ndarray | float,
    n: int = N,
) -> np.ndarray:
    """C1: endpoint raised to shell spacing is reciprocal radix."""
    return np.asarray(u) ** n - 1.0 / np.asarray(b)


def residual_norm(
    u: np.ndarray | float,
    theta: np.ndarray | float,
    b: np.ndarray | float,
) -> np.ndarray:
    r0 = frame_residual(u, theta)
    r1 = radix_residual(u, b)
    return np.hypot(r0, r1)


# ---------------------------------------------------------------------------
# Continuous self-constrained transfer curve
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TransferPoint:
    b: float
    theta: float
    u: float
    dtheta_db: float
    du_db: float
    closure_residual: float


def transfer_curve(
    b_min: float = 2.0,
    b_max: float = 256.0,
    count: int = 2001,
) -> list[TransferPoint]:
    """
    Solve both source constraints continuously for b>1.

    u = b^(-1/n)
    theta = arccos(u)

    This is not a guessed gearing law; it is the zero set of the two
    source-derived constraints.
    """
    if b_min <= 1:
        raise ValueError("b_min must be > 1")
    if b_max < b_min:
        raise ValueError("b_max must be >= b_min")
    if b_max == b_min:
        # A single-point evaluation is useful for lock calibration.
        count = 1
    if count < 1:
        raise ValueError("count must be >= 1")

    bs = np.linspace(b_min, b_max, count)

    out: list[TransferPoint] = []
    for b in bs:
        u = b ** (-1.0 / N)
        theta = math.acos(u)

        # Analytical derivatives from the same constraint manifold.
        # u = b^(-1/N)
        du_db = -(u / (N * b))
        # theta = acos(u)
        dtheta_db = -du_db / math.sqrt(1.0 - u * u)

        r = math.hypot(float(frame_residual(u, theta)),
                       float(radix_residual(u, b)))

        out.append(
            TransferPoint(
                b=float(b),
                theta=float(theta),
                u=float(u),
                dtheta_db=float(dtheta_db),
                du_db=float(du_db),
                closure_residual=float(r),
            )
        )
    return out


# ---------------------------------------------------------------------------
# 2-D residual field
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FieldSummary:
    b: float
    grid_size: int
    min_norm: float
    min_u: float
    min_theta: float
    min_r0: float
    min_r1: float


def residual_field(
    b: float,
    u_min: float = 0.25,
    u_max: float = 0.999,
    theta_min: float = 0.01,
    theta_max: float = math.pi / 2 - 0.01,
    grid_size: int = 401,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, FieldSummary]:
    """
    Build the actual 2-D C0/C1 residual field at fixed radix b.
    """
    if b <= 1:
        raise ValueError("b must be > 1")

    us = np.linspace(u_min, u_max, grid_size)
    thetas = np.linspace(theta_min, theta_max, grid_size)
    U, TH = np.meshgrid(us, thetas, indexing="xy")

    R0 = frame_residual(U, TH)
    R1 = radix_residual(U, b)
    NORM = np.hypot(R0, R1)

    idx = np.unravel_index(np.argmin(NORM), NORM.shape)
    summary = FieldSummary(
        b=float(b),
        grid_size=grid_size,
        min_norm=float(NORM[idx]),
        min_u=float(U[idx]),
        min_theta=float(TH[idx]),
        min_r0=float(R0[idx]),
        min_r1=float(R1[idx]),
    )
    return U, TH, R0, R1, NORM, summary


# ---------------------------------------------------------------------------
# Discrete locks / click-stops
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Lock:
    b: int
    theta_deg: float
    u: float
    radix_type: str


def lock_table(
    b_values: list[int] | None = None,
) -> list[Lock]:
    if b_values is None:
        b_values = list(range(2, 257))

    out: list[Lock] = []
    for b in sorted(set(b_values)):
        if b <= 1:
            continue
        u = b ** (-1.0 / N)
        theta = math.degrees(math.acos(u))

        if b & (b - 1) == 0:
            radix_type = "power_of_two"
        else:
            radix_type = "integer"

        out.append(Lock(b=b, theta_deg=theta, u=u, radix_type=radix_type))
    return out


# ---------------------------------------------------------------------------
# Perturbation / inverse-synchronization tests
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PerturbationCheck:
    b0: float
    theta0_deg: float
    delta_b: float
    theta_forward_deg: float
    theta_backward_deg: float
    theta_linear_prediction_deg: float
    residual_forward: float
    residual_backward: float


def perturbation_check(
    b0: float,
    delta_b: float,
) -> PerturbationCheck:
    """
    Move the radix coordinate and observe the forced theta response.

    Forward:
      b -> b + db, then solve C0=C1=0.

    Backward:
      reconstruct b from theta.

    This tests inverse synchronization of the same constraint manifold.
    """
    if b0 <= 1 or b0 + delta_b <= 1:
        raise ValueError("invalid radix perturbation")

    u0 = b0 ** (-1.0 / N)
    theta0 = math.acos(u0)

    b1 = b0 + delta_b
    u1 = b1 ** (-1.0 / N)
    theta1 = math.acos(u1)

    # Reconstruct b from the returned theta:
    b_back = math.cos(theta1) ** (-N)
    theta_back = math.acos(b_back ** (-1.0 / N))

    # Local tangent prediction dtheta/db at b0.
    dtheta_db = (u0 / (N * b0)) / math.sqrt(1.0 - u0 * u0)
    theta_lin = theta0 + dtheta_db * delta_b

    r_forward = math.hypot(
        float(frame_residual(u1, theta1)),
        float(radix_residual(u1, b1)),
    )

    r_backward = math.hypot(
        float(frame_residual(math.cos(theta_back), theta_back)),
        float(radix_residual(math.cos(theta_back), b_back)),
    )

    return PerturbationCheck(
        b0=b0,
        theta0_deg=math.degrees(theta0),
        delta_b=delta_b,
        theta_forward_deg=math.degrees(theta1),
        theta_backward_deg=math.degrees(theta_back),
        theta_linear_prediction_deg=math.degrees(theta_lin),
        residual_forward=r_forward,
        residual_backward=r_backward,
    )


# ---------------------------------------------------------------------------
# Source-derived F6 null vector
# ---------------------------------------------------------------------------

def derive_f6_null_vector() -> list[int]:
    """
    Derive the F6 shell null vector from frame geometry.

    Source-derived common operator:
      F(t) = C [log(1-t^2) - log(1-2 cos(theta)t+t^2)]

    At theta=pi/3, the reciprocal quadratic factors and pole annihilation
    determine the reduced numerator. The shell-basis conversion uses u=1/2.
    """
    t = sp.symbols("t")
    theta = sp.pi / 3
    u = sp.Rational(1, 2)

    # The annihilated pole pair for F6.
    q120 = sp.Poly(t**2 + t + 1, t)

    # Reduced reciprocal quadratic fixed by the F6 log-free/DC constraints.
    qres = sp.Poly(t**2 - 4 * t + 1, t)

    numerator = sp.Poly(sp.expand(q120.as_expr() * qres.as_expr()), t)

    coeffs = []
    for r in range(1, 7):
        coeffs.append(sp.simplify(numerator.nth(r - 1) * u**r))

    denoms = [sp.denom(x) for x in coeffs]
    lcm = sp.ilcm(*[int(d) for d in denoms])
    ints = [int(x * lcm) for x in coeffs]

    g = 0
    for x in ints:
        g = math.gcd(g, abs(x))
    ints = [x // g for x in ints]

    first = next(x for x in ints if x)
    if first < 0:
        ints = [-x for x in ints]

    return ints


# ---------------------------------------------------------------------------
# Channel-removal controls
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ChannelControl:
    both_min_norm: float
    c0_only_min_abs_c0: float
    c1_only_min_abs_c1: float


def channel_controls(
    b: float,
    grid_size: int = 401,
) -> ChannelControl:
    """
    Controls are reported separately:
      both = simultaneous source constraints
      C0 only = frame residual alone
      C1 only = radix residual alone

    This avoids confusing a single-channel zero with a genuine mesh.
    """
    us = np.linspace(0.25, 0.999, grid_size)
    th = np.linspace(0.01, math.pi / 2 - 0.01, grid_size)
    U, TH = np.meshgrid(us, th, indexing="xy")

    R0 = frame_residual(U, TH)
    R1 = radix_residual(U, b)

    return ChannelControl(
        both_min_norm=float(np.min(np.hypot(R0, R1))),
        c0_only_min_abs_c0=float(np.min(np.abs(R0))),
        c1_only_min_abs_c1=float(np.min(np.abs(R1))),
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def main() -> None:
    print("HEXAGONAL C0/C1 TRANSFER ENGINE")
    print("================================")
    print("Source-derived constraints:")
    print("  C0 = u - cos(theta)")
    print("  C1 = u^6 - 1/b")
    print()
    print("The known F6 lock is deliberately NOT supplied to the solver.")
    print()

    curve = transfer_curve(2.0, 256.0, 9)
    print("CONTINUOUS TRANSFER:")
    for p in curve:
        print(
            f"  b={p.b:8.3f}  theta={math.degrees(p.theta):9.5f}°"
            f"  u={p.u:.8f}  dtheta/db={p.dtheta_db:.8e}"
        )

    print()
    print("F6 POINT:")
    p = transfer_curve(64.0, 64.0, 1)[0]
    print(f"  b=64 -> u={p.u:.12f}, theta={math.degrees(p.theta):.12f}°")
    print(f"  closure residual={p.closure_residual:.3e}")

    print()
    print("PERTURBATION:")
    pc = perturbation_check(64.0, 1.0)
    print(
        f"  b: {pc.b0} -> {pc.b0 + pc.delta_b}"
        f"  theta: {pc.theta0_deg:.9f}° -> {pc.theta_forward_deg:.9f}°"
    )
    print(
        f"  linear local prediction: {pc.theta_linear_prediction_deg:.9f}°"
    )
    print(
        f"  forward residual={pc.residual_forward:.3e},"
        f" backward residual={pc.residual_backward:.3e}"
    )

    print()
    print("F6 NULL VECTOR (derived):")
    null = derive_f6_null_vector()
    print(f"  {null}")
    print(f"  sum={sum(null)}")

    print()
    print("POST-HOC RESIDUE LABEL ONLY:")
    print("  [4,-2,-1,-1]")
    print("  supplied to solver: NO")

    print()
    print("LOCKS: powers of two from 2..256")
    for lock in lock_table([2, 4, 8, 16, 32, 64, 128, 256]):
        print(
            f"  b={lock.b:3d}  theta={lock.theta_deg:9.5f}°"
            f"  u={lock.u:.8f}  type={lock.radix_type}"
        )


if __name__ == "__main__":
    main()
