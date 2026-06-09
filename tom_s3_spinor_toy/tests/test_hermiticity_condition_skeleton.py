"""Hermiticity tests for the minimal Option B coupling scaffold V.

The current V is a k_max=1 symbolic coefficient scaffold. It is not the full
physical homogeneous SU(2) matrix element for arbitrary k.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from s3_dirac_exact_baseline import total_number_of_modes
from s3_coupling_v_option_b import build_v_symbolic, expand_spectral_basis_states
from s3_reduced_matrix_elements import (
    reduced_element_metadata,
    reduced_elements_for_kmax1,
)


def generate_hermitian_test_matrix(k_max: int) -> np.ndarray:
    """Return the minimal symbolic V scaffold with the clean S3 mode dimension."""
    return build_v_symbolic(k_max=k_max)


def test_hermiticity_stub() -> None:
    """The symbolic k_max=1 scaffold is Hermitian."""
    matrix = generate_hermitian_test_matrix(k_max=1)

    assert np.array_equal(matrix, matrix.conjugate().T)


def test_nonzero_structure_requires_real_v() -> None:
    """The symbolic scaffold is no longer the old zero placeholder."""
    matrix = generate_hermitian_test_matrix(k_max=1)

    assert np.count_nonzero(matrix) > 0, "Stub matrix is zero: implement real V"


def test_v_is_hermitian() -> None:
    """Hermiticity check using numerical tolerance for symbolic coefficients."""
    matrix = generate_hermitian_test_matrix(k_max=1)

    assert np.allclose(matrix, matrix.conjugate().T)


def test_v_shape_matches_clean_mode_count() -> None:
    """The current scaffold does not expand the internal gauge-doublet index."""
    matrix = generate_hermitian_test_matrix(k_max=1)
    expected_size = total_number_of_modes(1)

    assert matrix.shape == (expected_size, expected_size)


def test_left_invariant_selection_rules_are_satisfied() -> None:
    """Nonzero entries obey the working (J_L,J_R)=(1,0) selection rules."""
    matrix = generate_hermitian_test_matrix(k_max=1)
    states = expand_spectral_basis_states(k_max=1)

    for target_index, source_index in zip(*np.nonzero(matrix)):
        source = states[source_index]
        target = states[target_index]
        q_left = target.m_left - source.m_left

        assert target.j_right == source.j_right
        assert target.m_right == source.m_right
        assert abs(target.j_left - source.j_left) <= 1.0
        assert q_left in {-1.0, 0.0, 1.0}
        assert not (source.j_left == 0.0 and target.j_left == 0.0)


def test_reduced_elements_are_real() -> None:
    """Working k_max=1 reduced elements are real analytic coefficients."""
    elements = reduced_elements_for_kmax1()

    assert elements
    assert all(isinstance(value, float) for value in elements.values())
    assert all(np.isfinite(value) for value in elements.values())


def test_reduced_element_metadata_marks_unresolved_normalization() -> None:
    """Do not over-claim the current coefficients as final Ben Achour normalization."""
    metadata = reduced_element_metadata()

    assert metadata["J_L"] == 1.0
    assert metadata["J_R"] == 0.0
    assert metadata["normalization_status"] == "ANALYTIC_DIRECT_HAAR_CONVENTION"
    assert metadata["final_ben_achour_normalization"] == "unresolved"
    assert metadata["claim_scope"] == "engineering smoke tests only; no quantitative physics claims"
