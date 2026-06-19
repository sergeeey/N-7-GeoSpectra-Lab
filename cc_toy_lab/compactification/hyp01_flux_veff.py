"""HYP_01 — minimal flux / moduli V_eff toy model for lambda fixation."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

import numpy as np
from scipy.optimize import minimize

HypothesisStatus = Literal[
    "hypothesis_supported",
    "hypothesis_killed",
    "inconclusive",
]


@dataclass(frozen=True)
class FluxParams:
    """Toy coefficients — not a physical compactification Lagrangian."""

    a: float = 1.0
    b: float = 0.5
    kappa: float = 0.35


@dataclass(frozen=True)
class CriticalPoint:
    lam: float
    radius: float
    squash: float
    value: float
    hessian_min_eig: float


@dataclass(frozen=True)
class Hyp01Report:
    hypothesis_id: str
    coupled: bool
    flux_integers: tuple[int, int]
    status: HypothesisStatus
    falsifier_triggered: bool
    critical_points: tuple[CriticalPoint, ...]
    message: str


def v_eff(
    lam: float,
    radius: float,
    n1: int,
    n2: int,
    params: FluxParams,
    *,
    coupled: bool,
) -> float:
    """Minimal 2D toy V_eff(lambda, R; N1, N2).

    Radion + flux energy + optional lambda–flux mixing kappa * lambda * N1 * N2 / R.
    Decoupled branch omits all lambda dependence (falsifier).
    """
    r = max(float(radius), 1e-6)
    radion = params.a / r**4 + params.b * r**4
    flux = float(n1**2) / r**2 + float(n2**2)
    if not coupled:
        return radion + flux
    mix = params.kappa * lam * float(n1 * n2) / r
    return radion + flux + mix + lam**2


def partial_lam(
    lam: float,
    radius: float,
    n1: int,
    n2: int,
    params: FluxParams,
    *,
    coupled: bool,
) -> float:
    if not coupled:
        return 0.0
    r = max(float(radius), 1e-6)
    return params.kappa * float(n1 * n2) / r + 2.0 * lam


def grad_veff(
    x: np.ndarray,
    n1: int,
    n2: int,
    params: FluxParams,
    *,
    coupled: bool,
) -> np.ndarray:
    lam, radius = map(float, x)
    r = max(radius, 1e-6)
    if coupled:
        dl = params.kappa * float(n1 * n2) / r + 2.0 * lam
        dr = (
            -4.0 * params.a / r**5
            + 4.0 * params.b * r**3
            - 2.0 * float(n1**2) / r**3
            - params.kappa * lam * float(n1 * n2) / r**2
        )
    else:
        dl = 0.0
        dr = -4.0 * params.a / r**5 + 4.0 * params.b * r**3 - 2.0 * float(n1**2) / r**3
    return np.array([dl, dr], dtype=float)


def _hessian_min_eig_2d(
    x: np.ndarray,
    n1: int,
    n2: int,
    params: FluxParams,
    *,
    coupled: bool,
) -> float:
    step = 1e-4
    h = np.zeros((2, 2))

    def f(vec: np.ndarray) -> float:
        return v_eff(vec[0], vec[1], n1, n2, params, coupled=coupled)

    for i in range(2):
        for j in range(2):
            ei = np.zeros(2)
            ej = np.zeros(2)
            ei[i] = step
            ej[j] = step
            h[i, j] = (
                f(x + ei + ej) - f(x + ei - ej) - f(x - ei + ej) + f(x - ei - ej)
            ) / (4.0 * step**2)
    return float(np.min(np.linalg.eigvalsh(h)))


def find_critical_points(
    n1: int,
    n2: int,
    params: FluxParams = FluxParams(),
    *,
    coupled: bool,
    seeds: tuple[tuple[float, float], ...] = (
        (-0.2, 1.0),
        (-0.4, 1.1),
        (-0.1, 0.9),
    ),
) -> list[CriticalPoint]:
    found: list[CriticalPoint] = []
    for lam0, r0 in seeds:
        if coupled:
            def objective(r_only: np.ndarray) -> float:
                r = float(r_only[0])
                lam = -params.kappa * float(n1 * n2) / (2.0 * r)
                return v_eff(lam, r, n1, n2, params, coupled=True)

            result = minimize(
                objective,
                x0=np.array([r0], dtype=float),
                method="L-BFGS-B",
                bounds=[(0.4, 3.0)],
            )
            r = float(result.x[0])
            lam = -params.kappa * float(n1 * n2) / (2.0 * r)
        else:
            result = minimize(
                lambda x: v_eff(x[0], x[1], n1, n2, params, coupled=False),
                x0=np.array([lam0, r0], dtype=float),
                method="L-BFGS-B",
                bounds=[(-2.0, 2.0), (0.4, 3.0)],
            )
            lam, r = map(float, result.x)
        x = np.array([lam, r])
        grad = grad_veff(x, n1, n2, params, coupled=coupled)
        if np.linalg.norm(grad) > 1e-5:
            continue
        hess_min = _hessian_min_eig_2d(x, n1, n2, params, coupled=coupled)
        found.append(
            CriticalPoint(
                lam=lam,
                radius=r,
                squash=1.0,
                value=float(v_eff(lam, r, n1, n2, params, coupled=coupled)),
                hessian_min_eig=hess_min,
            )
        )
    unique: list[CriticalPoint] = []
    seen: set[tuple[int, int]] = set()
    for cp in found:
        key = (round(cp.lam, 5), round(cp.radius, 5))
        if key in seen:
            continue
        seen.add(key)
        unique.append(cp)
    return unique


def run_hyp01_experiment(
    n1: int = 1,
    n2: int = 2,
    params: FluxParams = FluxParams(),
) -> tuple[Hyp01Report, Hyp01Report]:
    """Run coupled + decoupled branches; return (coupled_report, falsifier_report)."""
    coupled_cps = find_critical_points(n1, n2, params, coupled=True)
    decoupled_cps = find_critical_points(n1, n2, params, coupled=False)

    lam_grid = np.linspace(-1.0, 1.0, 11)
    decoupled_flat = all(
        abs(partial_lam(l, 1.0, n1, n2, params, coupled=False)) < 1e-12 for l in lam_grid
    )

    if len(coupled_cps) >= 1:
        coupled_status: HypothesisStatus = "hypothesis_supported"
        lam_star = coupled_cps[0].lam
        coupled_msg = (
            f"Coupled flux sector yields {len(coupled_cps)} critical point(s); "
            f"lambda_*={lam_star:.6f} at N1={n1}, N2={n2}."
        )
    else:
        coupled_status = "inconclusive"
        coupled_msg = "No stable coupled critical point found in toy search window."

    coupled_report = Hyp01Report(
        hypothesis_id="HYP_01_FLUX_STABILIZATION",
        coupled=True,
        flux_integers=(n1, n2),
        status=coupled_status,
        falsifier_triggered=False,
        critical_points=tuple(coupled_cps),
        message=coupled_msg,
    )

    falsifier_report = Hyp01Report(
        hypothesis_id="HYP_01_FLUX_STABILIZATION",
        coupled=False,
        flux_integers=(n1, n2),
        status="hypothesis_killed" if decoupled_flat else "inconclusive",
        falsifier_triggered=decoupled_flat,
        critical_points=tuple(decoupled_cps),
        message=(
            "Falsifier: d V_eff / d lambda == 0 identically when flux-lambda coupling removed."
            if decoupled_flat
            else "Decoupled branch did not exhibit flat lambda direction as expected."
        ),
    )
    return coupled_report, falsifier_report


def report_to_dict(report: Hyp01Report) -> dict:
    d = asdict(report)
    d["critical_points"] = [asdict(cp) for cp in report.critical_points]
    return d
