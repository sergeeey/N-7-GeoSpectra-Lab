"""Tests for the explicit S3 Pauli/Clifford scaffold."""

from __future__ import annotations

import numpy as np

from s3_pauli_clifford_explicit import (
    clifford_4d_euclidean,
    clifford_anticommutator_residuals,
    clifford_basis_ordering_metadata,
    lawrence_radius_squared,
    pauli_map_unitarity_residual,
)


def test_lawrence_s3_coordinates_preserve_radius() -> None:
    """The Lawrence embedding should lie on the radius-rho 3-sphere."""

    rho = 1.7
    alpha_grid = np.linspace(0.0, np.pi / 2.0, 9)
    theta_grid = np.linspace(0.0, 2.0 * np.pi, 7)
    theta_tilde_grid = np.linspace(0.0, 2.0 * np.pi, 5)

    for alpha in alpha_grid:
        for theta in theta_grid:
            for theta_tilde in theta_tilde_grid:
                radius_sq = float(lawrence_radius_squared(alpha, theta, theta_tilde, rho=rho))
                assert abs(radius_sq - rho**2) < 1e-12


def test_pauli_map_unitarity_on_grid() -> None:
    """The explicit Pauli map should satisfy U^\dagger U = rho^2 I on a grid."""

    rho = 1.3
    alpha_grid = np.linspace(0.0, np.pi / 2.0, 11)
    theta_grid = np.linspace(0.0, 2.0 * np.pi, 9)
    theta_tilde_grid = np.linspace(0.0, 2.0 * np.pi, 7)

    max_error = 0.0
    for alpha in alpha_grid:
        for theta in theta_grid:
            for theta_tilde in theta_tilde_grid:
                residual = pauli_map_unitarity_residual(alpha, theta, theta_tilde, rho=rho)
                max_error = max(max_error, float(np.max(np.abs(residual))))

    assert max_error < 1e-10


def test_clifford_4d_euclidean_anticommutators() -> None:
    """The 4D Euclidean Clifford scaffold should satisfy the anticommutators."""

    gammas = clifford_4d_euclidean()
    residuals = clifford_anticommutator_residuals(gammas)
    max_residual = max(float(np.max(np.abs(residual))) for residual in residuals.values())

    assert max_residual == 0.0


def test_clifford_basis_ordering_metadata_present() -> None:
    """The module must expose the required ordering and safety metadata."""

    metadata = clifford_basis_ordering_metadata()

    assert metadata["signature"] == "euclidean"
    assert metadata["dimension"] == 4
    assert metadata["factor_order"] == "spinor / chirality / internal / placeholder"
    assert metadata["pauli_map_convention"] == "U = x4 I + i(x1 sigma1 + x2 sigma2 + x3 sigma3)"
    assert metadata["safe_for_runtime"] is False

