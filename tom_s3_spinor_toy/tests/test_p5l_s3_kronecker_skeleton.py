"""Tests for the explicit 32D Kronecker skeleton."""

from __future__ import annotations

import numpy as np

from s3_kronecker_skeleton import (
    kronecker_32d_basis_labels,
    kronecker_32d_basis_matrix,
    kronecker_32d_clifford_generators,
    kronecker_skeleton_metadata,
    validate_kronecker_clifford,
)


def test_kronecker_32d_basis_and_metadata() -> None:
    """The skeleton should expose a 32D binary basis and the required metadata."""

    labels = kronecker_32d_basis_labels()
    basis = kronecker_32d_basis_matrix()
    metadata = kronecker_skeleton_metadata()

    assert len(labels) == 32
    assert len(set(labels)) == 32
    assert basis.shape == (32, 32)
    assert metadata["signature"] == "euclidean"
    assert metadata["dimension"] == 32
    assert metadata["factor_order"] == "spinor / chirality / internal / flavor / placeholder"
    assert metadata["basis_order"] == "lexicographic binary order on five tensor factors"
    assert metadata["safe_for_runtime"] is False


def test_kronecker_32d_clifford_anticommutators() -> None:
    """The Kronecker scaffold should satisfy the Euclidean Clifford relations."""

    gammas = kronecker_32d_clifford_generators()
    assert validate_kronecker_clifford(gammas, signature="euclidean")

    residuals = {
        key: np.max(np.abs(value))
        for key, value in __import__("s3_kronecker_skeleton").kronecker_anticommutator_residuals(gammas).items()
    }
    assert max(residuals.values()) == 0.0

