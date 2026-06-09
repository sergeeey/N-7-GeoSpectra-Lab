"""Pre-registered smoke test for the temporary D = D0 + alpha V operator.

This is an engineering-only test. It does not claim a physical gauge-field
result, an instanton, an index, chirality, spectral flow, eta invariants, or
zero modes.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_with_temp_coupling import build_temp_coupled_dirac
from s3_dirac_exact_baseline import total_number_of_modes


def test_d_is_hermitian() -> None:
    """D must remain Hermitian for the engineering smoke test."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0)
    d_matrix = result["D"]

    assert np.linalg.norm(d_matrix - d_matrix.conjugate().T) < 1e-10


def test_d_is_not_equal_to_d0() -> None:
    """The coupling must produce a nonzero off-diagonal contribution."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0)
    v_matrix = result["V"]

    assert np.count_nonzero(v_matrix - np.diag(np.diag(v_matrix))) > 0
    assert not np.array_equal(result["D"], result["D0"])


def test_alpha_zero_returns_d0() -> None:
    """The zero-coupling limit returns the clean diagonal operator."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0, alpha=0.0)

    assert np.array_equal(result["D"], result["D0"])
    assert np.count_nonzero(result["V"]) == 0


def test_spectrum_has_no_forbidden_zone_gap_violations() -> None:
    """The temporary smoke spectrum should stay outside |lambda| < 1."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0)
    eigenvalues = np.linalg.eigvalsh(result["D"])

    assert np.min(np.abs(eigenvalues)) >= 1.0


def test_spectrum_is_symmetric_about_zero() -> None:
    """Eigenvalues should be symmetric under lambda -> -lambda."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0)
    eigenvalues = np.linalg.eigvalsh(result["D"])

    assert np.max(np.abs(eigenvalues + eigenvalues[::-1])) < 1e-10


def test_metadata_marks_engineering_alpha() -> None:
    """Metadata must expose the temporary alpha and warning flag."""
    result = build_temp_coupled_dirac(k_max=3, lambda_val=1.0, radius=1.0)
    metadata = result["metadata"]

    assert result["D"].shape == (total_number_of_modes(3), total_number_of_modes(3))
    assert metadata["ENGINEERING_ALPHA"] == 1.0
    assert metadata["warning"] == "direct Haar/unit-coframe normalization; final Ben_Achour basis mapping unresolved"
    assert metadata["normalization_status"] == "ANALYTIC_DIRECT_HAAR_CONVENTION"
