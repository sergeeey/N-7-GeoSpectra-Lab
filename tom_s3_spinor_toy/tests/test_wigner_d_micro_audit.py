"""Micro-audit tests for Wigner-D conventions against Ben Achour scalar modes.

These tests are a representation-sanity layer only. They do not claim anything
about Tom Lawrence's full spinor construction.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from ben_achour_scalar_modes import (
    pdf_stated_killing_eigenvalues,
    scalar_mode_unnormalized,
)
from wigner_d_micro_audit import (
    ben_achour_to_wigner_labels,
    candidate_user_swap_labels_for_displayed_phase,
    candidate_user_swap_labels_for_pdf_stated_phase,
    displayed_phase_coefficients,
    get_working_convention_decision,
    hopf_to_wigner_euler,
    pdf_stated_phase_coefficients,
    wigner_D,
    wigner_displayed_phase_eigenvalues,
    wigner_small_d_matrix,
)


def _assert_proportional(left: np.ndarray, right: np.ndarray) -> None:
    mask = np.abs(right) > 1e-10
    ratio = left[mask] / right[mask]
    assert ratio.size > 0
    assert np.all(np.isfinite(ratio))
    assert np.max(np.abs(ratio - ratio[0])) < 1e-10


@pytest.mark.parametrize(
    ("L", "m_plus", "m_minus"),
    [
        (0, 0.0, 0.0),
        (1, 0.5, 0.5),
        (1, 0.5, -0.5),
        (2, 1.0, 0.0),
        (2, 1.0, 1.0),
    ],
)
def test_ben_achour_modes_are_proportional_to_hopf_mapped_wigner_D(
    L: int, m_plus: float, m_minus: float
) -> None:
    """Small-L scalar modes match Wigner-D up to normalization/sign.

    The comparison uses the displayed Ben Achour phase
    exp(i(S phi + D theta)) and the Hopf-aligned Euler map.
    """
    alpha = np.linspace(0.2, np.pi / 2 - 0.2, 8)
    phi = np.linspace(0.1, 0.8, 8)
    theta = np.linspace(0.4, 1.1, 8)

    j, m_prime, m = ben_achour_to_wigner_labels(L, m_plus, m_minus)
    euler_a, beta, euler_c = hopf_to_wigner_euler(alpha, phi, theta)

    ben_values = scalar_mode_unnormalized(L, m_plus, m_minus, alpha, phi, theta)
    wigner_values = wigner_D(j, m_prime, m, euler_a, beta, euler_c)

    _assert_proportional(ben_values, wigner_values)


@pytest.mark.parametrize("j", [0.5, 1.0])
def test_wigner_small_d_is_unitary_for_small_j(j: float) -> None:
    """Explicit small-d matrices should be orthogonal for real beta."""
    beta = 0.73
    matrix = wigner_small_d_matrix(j, beta)

    assert matrix @ matrix.T == pytest.approx(np.eye(matrix.shape[0]))


def test_wigner_mapping_reproduces_displayed_xi_eigenvalues() -> None:
    """The Hopf-aligned Wigner phase gives the same xi values as the displayed PDF."""
    eig = wigner_displayed_phase_eigenvalues(m_plus=1.0, m_minus=0.5)

    assert eig["xi"] == pytest.approx(2j)
    assert eig["xi_prime_from_displayed_phase"] == pytest.approx(1j)


def test_xi_prime_sign_is_resolved_as_typo_after_wigner_mapping() -> None:
    """Wigner-D alignment confirms the displayed-phase xi' sign convention."""
    displayed = wigner_displayed_phase_eigenvalues(m_plus=0.0, m_minus=1.0)
    stated = pdf_stated_killing_eigenvalues(m_plus=0.0, m_minus=1.0)

    assert displayed["xi_prime_from_displayed_phase"] == pytest.approx(2j)
    assert stated["xi_prime_pdf_stated"] == pytest.approx(-2j)


def test_pdf_stated_xi_prime_requires_swapping_displayed_phase_coefficients() -> None:
    """The stated xi' sign is equivalent to exp(i(D phi + S theta))."""
    displayed = displayed_phase_coefficients(m_plus=1.0, m_minus=0.5)
    stated = pdf_stated_phase_coefficients(m_plus=1.0, m_minus=0.5)

    assert displayed == {"phi": 1.5, "theta": 0.5}
    assert stated == {"phi": 0.5, "theta": 1.5}
    assert displayed != stated


def test_user_direct_euler_swap_cannot_match_displayed_phase_for_all_pdf_labels() -> None:
    """The direct Euler swap needs Wigner labels outside [-j,j] for boundary modes."""
    labels = candidate_user_swap_labels_for_displayed_phase(
        L=2, m_plus=1.0, m_minus=1.0
    )

    assert labels["j"] == 1.0
    assert labels["required_m"] == -2.0
    assert labels["within_wigner_range"] is False


def test_user_direct_euler_swap_cannot_match_pdf_stated_phase_for_all_pdf_labels() -> None:
    """Even the sign-resolving phase is not generally compatible with direct swap labels."""
    labels = candidate_user_swap_labels_for_pdf_stated_phase(
        L=2, m_plus=1.0, m_minus=1.0
    )

    assert labels["j"] == 1.0
    assert labels["required_m_prime"] == -2.0
    assert labels["within_wigner_range"] is False


def test_working_convention_is_resolved_as_typo() -> None:
    """Downstream code uses the displayed Ben Achour phase by default."""
    decision = get_working_convention_decision()

    assert decision["status"] == "resolved_as_typo"
    assert decision["convention_id"] == "ben_achour_displayed_phase"
    assert decision["phase"] == "exp(i(S phi + D theta))"
    assert decision["xi_prime_eigenvalue"] == "+2 i m_minus"
    assert decision["gap_status"] == "resolved_as_typo"
    assert decision["claim_discipline"] == "use_displayed_phase_as_default"
    assert decision["alternative_convention"]["phase"] == "exp(i(D phi + S theta))"
    assert decision["alternative_convention"]["xi_prime_eigenvalue"] == "-2 i m_minus"
    assert "original TeX" in decision["requires_external_resolution"]
    assert "Tom exact generator equations" in decision["requires_external_resolution"]


def test_ladder_consistency_uses_negative_m_minus_in_wigner_label_map() -> None:
    """The displayed phase maps to Wigner labels with m = -m_minus."""
    j, m_prime, m = ben_achour_to_wigner_labels(L=1, m_plus=0.5, m_minus=0.5)

    assert j == pytest.approx(0.5)
    assert m_prime == pytest.approx(0.5)
    assert m == pytest.approx(-0.5)
