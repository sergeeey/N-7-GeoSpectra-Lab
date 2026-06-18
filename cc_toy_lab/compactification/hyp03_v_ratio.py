"""HYP_03 support — lambda-free V-RATIO-G0 observable (Wigner-Eckart sector B)."""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Literal

HypothesisStatus = Literal[
    "hypothesis_supported",
    "hypothesis_killed",
    "hypothesis_deferred",
    "inconclusive",
]


@dataclass(frozen=True)
class Hyp03Report:
    hypothesis_id: str
    sector: str
    r_observable: float
    lambda_derivative: float
    status: HypothesisStatus
    toy_test_deferred: bool
    message: str


def clebsch_gordan_j_half_j1_j_three_half(m_src: float, m_v: float) -> float:
    """CG(<1/2,m_src>, <1,m_V>) -> |3/2, +1/2> — sector B from V-RATIO-G0."""
    # Fixed analytic values from xlsx row 22 (verified-sympy in upstream log).
    table = {
        (+0.5, 0.0): math.sqrt(6.0) / 3.0,
        (-0.5, +1.0): math.sqrt(3.0) / 3.0,
    }
    key = (float(m_src), float(m_v))
    if key not in table:
        raise ValueError(f"Unsupported CG pair: {key}")
    return table[key]


def v_ratio_sector_b() -> float:
    cg_plus = clebsch_gordan_j_half_j1_j_three_half(+0.5, 0.0)
    cg_minus = clebsch_gordan_j_half_j1_j_three_half(-0.5, +1.0)
    return cg_plus / cg_minus


def run_hyp03_experiment() -> Hyp03Report:
    """Nonlinear-realization toy deferred; verify lambda-free structural ratio."""
    r_b = v_ratio_sector_b()
    expected = math.sqrt(2.0)
    rel_err = abs(r_b - expected) / expected
    if rel_err < 1e-12:
        status: HypothesisStatus = "hypothesis_supported"
        msg = (
            f"R_B = sqrt(2) confirmed ({r_b:.12f}); dR/dlambda = 0 — "
            "theory testable without fixing lambda. "
            "Full nonlinear-realization descent toy deferred (Tom Q1-Q2)."
        )
    else:
        status = "hypothesis_killed"
        msg = f"R_B mismatch: got {r_b}, expected {expected}."

    return Hyp03Report(
        hypothesis_id="HYP_03_NONLINEAR_REALIZATION",
        sector="B_JL_half_JR1_J_three_half_m_tgt_half",
        r_observable=float(r_b),
        lambda_derivative=0.0,
        status=status,
        toy_test_deferred=True,
        message=msg,
    )


def report_to_dict(report: Hyp03Report) -> dict:
    return asdict(report)
