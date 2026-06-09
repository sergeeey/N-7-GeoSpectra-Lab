"""Explicit 32D Kronecker skeleton for the validated S3 scaffold.

This module is deliberately narrow: it only fixes a 32-dimensional tensor-product
skeleton, a small Euclidean Clifford scaffold, and a parity-formalization
summary tied to the already validated S3 basis.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Final

import numpy as np

from s3_parity_smoke import parity_smoke_summary


KRONECKER_SKELETON_STATUS: Final[str] = "started"
RUNTIME_STATUS: Final[str] = "research_only"
V_SELECTION_STATUS: Final[str] = "smoke_only"
SAFE_FOR_RUNTIME: Final[bool] = False


@dataclass(frozen=True)
class KroneckerSkeletonMetadata:
    """Metadata for the explicit 32D Kronecker skeleton."""

    signature: str
    dimension: int
    factor_order: str
    basis_order: str
    safe_for_runtime: bool


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the standard Pauli matrices."""

    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return sigma1, sigma2, sigma3


def kronecker_32d_basis_labels() -> list[tuple[int, int, int, int, int]]:
    """Return lexicographic binary labels for the 32 tensor-product basis states."""

    return list(product((0, 1), repeat=5))


def kronecker_32d_basis_matrix() -> np.ndarray:
    """Return the 32x32 identity used as the skeleton basis matrix."""

    return np.eye(32, dtype=complex)


def kronecker_32d_clifford_generators() -> tuple[np.ndarray, ...]:
    """Return a 5-generator Euclidean Clifford scaffold on the 32D tensor product."""

    sigma1, sigma2, sigma3 = pauli_matrices()
    eye2 = np.eye(2, dtype=complex)

    gamma1 = np.kron(np.kron(np.kron(np.kron(sigma1, eye2), eye2), eye2), eye2)
    gamma2 = np.kron(np.kron(np.kron(np.kron(sigma2, eye2), eye2), eye2), eye2)
    gamma3 = np.kron(np.kron(np.kron(np.kron(sigma3, sigma1), eye2), eye2), eye2)
    gamma4 = np.kron(np.kron(np.kron(np.kron(sigma3, sigma2), eye2), eye2), eye2)
    gamma5 = np.kron(np.kron(np.kron(np.kron(sigma3, sigma3), sigma1), eye2), eye2)
    return gamma1, gamma2, gamma3, gamma4, gamma5


def kronecker_anticommutator_residuals(
    gammas: tuple[np.ndarray, ...]
) -> dict[tuple[int, int], np.ndarray]:
    """Return the anticommutator residuals {gamma_a, gamma_b} - 2 delta_ab I."""

    dim = gammas[0].shape[0]
    eye = np.eye(dim, dtype=complex)
    residuals: dict[tuple[int, int], np.ndarray] = {}
    for a, gamma_a in enumerate(gammas):
        for b, gamma_b in enumerate(gammas):
            delta = 1.0 if a == b else 0.0
            residuals[(a, b)] = gamma_a @ gamma_b + gamma_b @ gamma_a - 2.0 * delta * eye
    return residuals


def validate_kronecker_clifford(
    gammas: tuple[np.ndarray, ...],
    signature: str = "euclidean",
    atol: float = 1e-12,
) -> bool:
    """Validate the Clifford anticommutation relations for the Kronecker scaffold."""

    if signature != "euclidean":
        raise ValueError(f"Unsupported signature convention: {signature!r}")
    residuals = kronecker_anticommutator_residuals(gammas)
    return bool(all(np.max(np.abs(residual)) <= atol for residual in residuals.values()))


def kronecker_skeleton_metadata() -> dict[str, object]:
    """Return the metadata required by the gate."""

    return {
        "signature": "euclidean",
        "dimension": 32,
        "factor_order": "spinor / chirality / internal / flavor / placeholder",
        "basis_order": "lexicographic binary order on five tensor factors",
        "safe_for_runtime": SAFE_FOR_RUNTIME,
        "status": KRONECKER_SKELETON_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
    }


def s3_parity_formalization_summary() -> dict[str, object]:
    """Return the already smoke-validated parity status in formalized form."""

    summary = parity_smoke_summary()
    return {
        "status": KRONECKER_SKELETON_STATUS,
        "runtime_status": RUNTIME_STATUS,
        "v_selection_status": V_SELECTION_STATUS,
        "safe_for_runtime": SAFE_FOR_RUNTIME,
        "parity_summary": summary,
        "formalized_candidate": "P2 coordinate-swap smoke candidate",
        "formalized_verdict": "passed",
    }

