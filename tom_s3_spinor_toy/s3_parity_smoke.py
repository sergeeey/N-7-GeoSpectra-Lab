"""Parity smoke tests for the validated S3 spinor basis.

This module only checks whether selected O(4)-style candidates act with
coordinate-independent coefficients on the standard S3 spinor frame.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Final

import numpy as np

from s3_pauli_clifford_explicit import (
    parity_candidate_p1,
    parity_candidate_p2,
)
from standard_s3_spinor_harmonics import standard_spinor_frame


PARITY_SMOKE_STATUS: Final[str] = "started"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class ParitySmokeResult:
    """Summary of a parity candidate evaluated on the standard S3 frame."""

    candidate_name: str
    status: str
    max_coefficient_variation: float
    mean_coefficient_matrix: np.ndarray


def parity_candidates() -> dict[str, Callable[..., tuple[np.ndarray, np.ndarray, np.ndarray, float]]]:
    """Return the tested parity smoke candidates."""

    return {
        "P1": parity_candidate_p1,
        "P2": parity_candidate_p2,
    }


def _coefficient_matrix(
    alpha: float,
    theta: float,
    theta_tilde: float,
    candidate: Callable[..., tuple[np.ndarray, np.ndarray, np.ndarray, float]],
    rho: float = 1.0,
) -> np.ndarray:
    """Recover the constant-action matrix, if it exists, from the standard basis."""

    frame = standard_spinor_frame(alpha, theta, theta_tilde)
    new_alpha, new_theta, new_theta_tilde, new_rho = candidate(alpha, theta, theta_tilde, rho=rho)
    transformed = standard_spinor_frame(new_alpha, new_theta, new_theta_tilde)
    return transformed @ frame.conj().T


def evaluate_parity_candidate(
    candidate_name: str,
    candidate: Callable[..., tuple[np.ndarray, np.ndarray, np.ndarray, float]],
    alpha_grid: np.ndarray,
    theta: float = 0.37,
    theta_tilde: float = 1.11,
    rho: float = 1.0,
    atol: float = 1e-12,
) -> ParitySmokeResult:
    """Evaluate coefficient constancy for a single parity candidate."""

    matrices = [
        _coefficient_matrix(float(alpha), theta, theta_tilde, candidate, rho=rho)
        for alpha in alpha_grid
    ]
    stacked = np.stack(matrices, axis=0)
    mean_matrix = np.mean(stacked, axis=0)
    variations = np.max(np.abs(stacked - mean_matrix), axis=(1, 2))
    max_variation = float(np.max(variations))
    status = "passed" if max_variation <= atol else "inconclusive"
    return ParitySmokeResult(
        candidate_name=candidate_name,
        status=status,
        max_coefficient_variation=max_variation,
        mean_coefficient_matrix=mean_matrix,
    )


def parity_radius_preserved(
    candidate: Callable[..., tuple[np.ndarray, np.ndarray, np.ndarray, float]],
    alpha: float,
    theta: float,
    theta_tilde: float,
    rho: float = 1.0,
    atol: float = 1e-12,
) -> bool:
    """Check whether the candidate preserves the Lawrence radius."""

    from s3_pauli_clifford_explicit import lawrence_radius_squared

    new_alpha, new_theta, new_theta_tilde, new_rho = candidate(alpha, theta, theta_tilde, rho=rho)
    radius_sq = float(lawrence_radius_squared(new_alpha, new_theta, new_theta_tilde, rho=new_rho))
    return bool(abs(radius_sq - float(rho) ** 2) <= atol)


def parity_smoke_summary(
    alpha_grid: np.ndarray | None = None,
    theta: float = 0.37,
    theta_tilde: float = 1.11,
    rho: float = 1.0,
    atol: float = 1e-12,
) -> dict[str, object]:
    """Return a compact summary for report generation and tests."""

    if alpha_grid is None:
        alpha_grid = np.linspace(0.0, np.pi / 2.0, 17)

    results = {
        name: evaluate_parity_candidate(name, candidate, alpha_grid, theta=theta, theta_tilde=theta_tilde, rho=rho, atol=atol)
        for name, candidate in parity_candidates().items()
    }
    return {
        "status": PARITY_SMOKE_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
        "results": results,
    }
