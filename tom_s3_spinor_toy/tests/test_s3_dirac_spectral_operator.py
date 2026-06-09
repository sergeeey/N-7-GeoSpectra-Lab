"""Tests for the P1b diagonal spectral Dirac operator prototype on S3.

The operator is diagonal in the exact spectral branch basis. It is not a graph
operator, not a finite-difference operator, and not a gauge-field calculation.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_exact_baseline import analytic_dirac_spectrum_s3, total_number_of_modes
from s3_dirac_spectral_operator import build_dirac_matrix
from s3_spinor_spectral_labels import generate_spectral_spinor_records


def _expanded_baseline_eigenvalues(k_max: int, radius: float = 1.0) -> np.ndarray:
    values: list[float] = []
    for entry in analytic_dirac_spectrum_s3(k_max=k_max, radius=radius):
        values.extend([entry["eigenvalue"]] * entry["degeneracy"])
    return np.array(sorted(values), dtype=float)


def test_matrix_shape_matches_total_modes() -> None:
    """Matrix dimension equals the summed branch degeneracy through k_max."""
    matrix = build_dirac_matrix(k_max=3, radius=1.0)

    assert matrix.shape == (total_number_of_modes(3), total_number_of_modes(3))


def test_spectrum_matches_p0_exact_baseline() -> None:
    """Dense eigvalsh of the small diagonal prototype matches the exact spectrum."""
    matrix = build_dirac_matrix(k_max=3, radius=1.0)
    eigenvalues = np.linalg.eigvalsh(matrix.toarray())
    expected = _expanded_baseline_eigenvalues(k_max=3, radius=1.0)

    assert eigenvalues == pytest_approx_array(expected)


def test_operator_is_hermitian() -> None:
    """The diagonal spectral prototype is Hermitian by construction."""
    matrix = build_dirac_matrix(k_max=4, radius=1.0)
    residual = matrix - matrix.getH()

    assert residual.nnz == 0


def test_no_zero_modes_clean_round_s3() -> None:
    """The clean round S3 diagonal prototype has no zero eigenvalues."""
    matrix = build_dirac_matrix(k_max=4, radius=1.0)
    diagonal = matrix.diagonal()

    assert np.min(np.abs(diagonal)) > 1e-12


def test_diagonal_entries_follow_p1a_records() -> None:
    """Each P1a branch eigenvalue is repeated by its branch degeneracy."""
    matrix = build_dirac_matrix(k_max=2, radius=2.0)
    diagonal = matrix.diagonal()
    expected: list[float] = []
    for record in generate_spectral_spinor_records(k_max=2, radius=2.0):
        expected.extend([record["eigenvalue"]] * record["degeneracy_per_branch"])

    assert np.array_equal(diagonal, np.array(expected, dtype=float))


def pytest_approx_array(expected: np.ndarray) -> object:
    """Local helper to keep pytest out of type check paths until assertion time."""
    import pytest

    return pytest.approx(expected)
