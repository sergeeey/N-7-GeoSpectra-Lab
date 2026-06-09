"""Tests for Ben Achour et al. S3 scalar-mode conventions.

These tests intentionally cover only the PDF-verified scalar/Hopf layer.
They do not claim anything about Tom Lawrence's full spinor construction.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from ben_achour_scalar_modes import (
    ben_achour_phase_eigenvalues,
    pdf_stated_killing_eigenvalues,
    scalar_mode_unnormalized,
    validate_quantum_numbers,
)


def test_quantum_number_validation_accepts_pdf_allowed_values() -> None:
    """PDF constraints: |m_±| <= L/2 and L/2 - m_± in N."""
    validate_quantum_numbers(2, 1, 0)
    validate_quantum_numbers(3, 1.5, -0.5)


def test_quantum_number_validation_rejects_disallowed_values() -> None:
    """Out-of-range or non-lattice labels should fail before evaluation."""
    with pytest.raises(ValueError, match="abs"):
        validate_quantum_numbers(2, 2, 0)
    with pytest.raises(ValueError, match="integer lattice"):
        validate_quantum_numbers(2, 0.5, 0)


def test_scalar_mode_shape_and_complex_dtype() -> None:
    """The scalar mode evaluates on broadcastable alpha/phi/theta arrays."""
    alpha = np.linspace(0.1, np.pi / 2 - 0.1, 12)
    phi = np.linspace(0.2, 1.1, 12)
    theta = np.linspace(0.3, 1.2, 12)

    values = scalar_mode_unnormalized(2, 1, 0, alpha, phi, theta)

    assert values.shape == alpha.shape
    assert np.iscomplexobj(values)
    assert np.all(np.isfinite(values))


def test_pdf_phase_gives_xi_eigenvalue_plus_2_i_m_plus() -> None:
    """For exp(i(S phi + D theta)), (partial_phi + partial_theta) gives +2 i m_+."""
    eig = ben_achour_phase_eigenvalues(m_plus=1, m_minus=0)
    assert eig["xi"] == pytest.approx(2j)


def test_pdf_phase_xi_prime_sign_is_resolved_as_typo() -> None:
    """The displayed scalar phase fixes xi' = partial_phi - partial_theta."""
    phase = ben_achour_phase_eigenvalues(m_plus=0, m_minus=1)
    stated = pdf_stated_killing_eigenvalues(m_plus=0, m_minus=1)

    assert phase["xi_prime_from_displayed_phase"] == pytest.approx(2j)
    assert stated["xi_prime_pdf_stated"] == pytest.approx(-2j)
    assert phase["xi_prime_from_displayed_phase"] != pytest.approx(
        stated["xi_prime_pdf_stated"]
    )


def test_ladder_consistency_maps_m_minus_with_negative_wigner_weight() -> None:
    """The displayed phase convention maps m_minus to the negative Wigner weight."""
    from wigner_d_micro_audit import ben_achour_to_wigner_labels

    j, m_prime, m = ben_achour_to_wigner_labels(L=1, m_plus=0.5, m_minus=0.5)

    assert j == pytest.approx(0.5)
    assert m_prime == pytest.approx(0.5)
    assert m == pytest.approx(-0.5)
