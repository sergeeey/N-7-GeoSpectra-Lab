"""Tests for the direct Haar-unit coframe D0 + V smoke layer.

This layer uses the exact direct Haar/unit-coframe scale. It is not a final
Ben Achour basis-mapping result and must not be used for physical gauge-field
claims.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_exact_baseline import total_number_of_modes
from s3_dirac_spectral_operator import build_dirac_matrix
from s3_dirac_with_temp_coupling import build_temp_coupled_dirac
from s3_reduced_matrix_elements import reduced_element_metadata


def test_lambda_zero_returns_clean_d0() -> None:
    """The temporary coupled operator reduces to D0 when lambda=0."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=0.0)
    expected_d0 = build_dirac_matrix(k_max=1).toarray()

    assert np.array_equal(result["D"], expected_d0)
    assert np.count_nonzero(result["V"]) == 0


def test_temp_coupled_operator_is_hermitian() -> None:
    """D0 + V remains Hermitian in the direct Haar-unit coframe convention."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=1.0)

    assert np.allclose(result["D"], result["D"].conjugate().T)


def test_temp_v_is_nonzero_for_lambda_one() -> None:
    """The coupling V term is nonzero for lambda=1."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=1.0)

    assert np.count_nonzero(result["V"]) > 0


def test_temp_matrix_size_matches_clean_mode_count() -> None:
    """The smoke layer keeps the current clean spectral-basis dimension."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=1.0)
    expected_size = total_number_of_modes(1)

    assert result["D"].shape == (expected_size, expected_size)
    assert result["D0"].shape == (expected_size, expected_size)
    assert result["V"].shape == (expected_size, expected_size)


def test_metadata_marks_temporary_engineering_convention() -> None:
    """Metadata must prevent treating this as final Ben Achour basis mapping."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=1.0)
    metadata = result["metadata"]
    reduced_metadata = reduced_element_metadata()

    assert metadata["normalization_status"] == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert metadata["final_ben_achour_normalization"] == "unresolved"
    assert metadata["one_form_scale"] == 1.0
    assert reduced_metadata["normalization_status"] == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert reduced_metadata["final_ben_achour_normalization"] == "unresolved"


def test_temp_v_is_off_diagonal_and_nonzero() -> None:
    """The smoke-layer V is a nonzero branch-paired projection."""
    result = build_temp_coupled_dirac(k_max=1, lambda_val=0.25)
    v_matrix = result["V"]

    assert np.count_nonzero(v_matrix) > 0
    assert np.count_nonzero(np.diag(v_matrix)) == 0
