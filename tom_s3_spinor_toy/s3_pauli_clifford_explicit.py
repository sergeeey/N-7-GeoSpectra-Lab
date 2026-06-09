"""Explicit Pauli / Clifford scaffold for the Lawrence S3 chart.

This module is intentionally narrow. It only fixes the coordinate embedding,
Pauli map convention, Euclidean Clifford matrices, and metadata needed for
smoke-level verification.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi
from typing import Final

import numpy as np


PAULI_CLIFFORD_STATUS: Final[str] = "started"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class PauliCliffordMetadata:
    """Metadata for the explicit S3 Pauli/Clifford scaffold."""

    signature: str
    dimension: int
    factor_order: str
    pauli_map_convention: str
    safe_for_runtime: bool


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the standard Pauli matrices."""

    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma1, sigma2, sigma3


def lawrence_coordinates(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return the Lawrence embedding coordinates on round S^3."""

    alpha = np.asarray(alpha, dtype=float)
    theta = np.asarray(theta, dtype=float)
    theta_tilde = np.asarray(theta_tilde, dtype=float)
    rho = float(rho)

    x1 = rho * np.sin(alpha) * np.cos(theta)
    x2 = rho * np.sin(alpha) * np.sin(theta)
    x3 = rho * np.cos(alpha) * np.sin(theta_tilde)
    x4 = rho * np.cos(alpha) * np.cos(theta_tilde)
    return x1, x2, x3, x4


def lawrence_radius_squared(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> np.ndarray:
    """Return x1^2 + x2^2 + x3^2 + x4^2 for the Lawrence embedding."""

    x1, x2, x3, x4 = lawrence_coordinates(alpha, theta, theta_tilde, rho=rho)
    return x1**2 + x2**2 + x3**2 + x4**2


def pauli_map(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> np.ndarray:
    """Return U = x4 I + i(x1 sigma1 + x2 sigma2 + x3 sigma3).

    This is the explicit SU(2)-style map selected for this gate. It is pointwise
    norm-preserving in the sense U^\dagger U = rho^2 I_2.
    """

    x1, x2, x3, x4 = lawrence_coordinates(alpha, theta, theta_tilde, rho=rho)
    sigma1, sigma2, sigma3 = pauli_matrices()
    eye = np.eye(2, dtype=complex)

    return (
        np.asarray(x4)[..., None, None] * eye
        + 1.0j * np.asarray(x1)[..., None, None] * sigma1
        + 1.0j * np.asarray(x2)[..., None, None] * sigma2
        + 1.0j * np.asarray(x3)[..., None, None] * sigma3
    )


def clifford_3d_euclidean() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the 3D Euclidean Clifford scaffold, identified with the Pauli basis."""

    return pauli_matrices()


def clifford_4d_euclidean() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return a standard 4D Euclidean Clifford scaffold using Kronecker products."""

    sigma1, sigma2, sigma3 = pauli_matrices()
    eye2 = np.eye(2, dtype=complex)
    return (
        np.kron(sigma1, sigma1),
        np.kron(sigma2, sigma1),
        np.kron(sigma3, sigma1),
        np.kron(eye2, sigma2),
    )


def clifford_anticommutator_residuals(gammas: tuple[np.ndarray, ...]) -> dict[tuple[int, int], np.ndarray]:
    """Return the anticommutator residuals {gamma_a, gamma_b} - 2 delta_ab I."""

    dim = gammas[0].shape[0]
    eye = np.eye(dim, dtype=complex)
    residuals: dict[tuple[int, int], np.ndarray] = {}
    for a, gamma_a in enumerate(gammas):
        for b, gamma_b in enumerate(gammas):
            delta = 1.0 if a == b else 0.0
            residuals[(a, b)] = gamma_a @ gamma_b + gamma_b @ gamma_a - 2.0 * delta * eye
    return residuals


def validate_clifford(
    gammas: tuple[np.ndarray, ...],
    signature: str = "euclidean",
    atol: float = 1e-12,
) -> bool:
    """Validate the Clifford anticommutation relations for a fixed signature."""

    if signature != "euclidean":
        raise ValueError(f"Unsupported signature convention: {signature!r}")
    residuals = clifford_anticommutator_residuals(gammas)
    return bool(all(np.max(np.abs(residual)) <= atol for residual in residuals.values()))


def clifford_basis_ordering_metadata() -> dict[str, object]:
    """Return the metadata required by the gate."""

    return {
        "signature": "euclidean",
        "dimension": 4,
        "factor_order": "spinor / chirality / internal / placeholder",
        "pauli_map_convention": "U = x4 I + i(x1 sigma1 + x2 sigma2 + x3 sigma3)",
        "safe_for_runtime": SAFE_FOR_RUNTIME,
        "status": PAULI_CLIFFORD_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
    }


def pauli_map_unitarity_residual(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> np.ndarray:
    """Return U^\dagger U - rho^2 I for the selected Pauli map."""

    U = pauli_map(alpha, theta, theta_tilde, rho=rho)
    eye = np.eye(2, dtype=complex)
    target = (float(rho) ** 2) * eye
    return np.matmul(np.conjugate(np.swapaxes(U, -1, -2)), U) - target


def parity_candidate_p1(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Embedded inversion-like candidate: flip x1, x2, x3 and keep x4 fixed."""

    return alpha, np.asarray(theta, dtype=float) + pi, np.asarray(theta_tilde, dtype=float) + pi, float(rho)


def parity_candidate_p2(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    rho: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Coordinate-swap smoke candidate: alpha -> pi/2 - alpha."""

    return (pi / 2.0) - np.asarray(alpha, dtype=float), np.asarray(theta, dtype=float) + pi, np.asarray(theta_tilde, dtype=float) + pi, float(rho)

