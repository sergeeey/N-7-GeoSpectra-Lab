"""Tests for the Ben Achour one-form mode implementation gate."""

from __future__ import annotations

import sympy as sp

from ben_achour_one_form_modes import (
    BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE,
    NORMALIZATION_DEPENDENT,
    SOURCE_SUPPORTED_GEOMETRY,
    VANISHING_OR_EXCLUDED,
    build_low_mode_ben_achour_one_form_modes,
    hopf_coordinate_symbols,
    hopf_embedding,
    hopf_metric_tensor,
    mode_applicability_status,
    one_form_norm_squared,
    orthonormal_coframe,
    scalar_mode_symbolic,
    star_d_one_form,
    xi_flat,
    xi_prime_flat,
)


def test_coordinate_and_metric_conventions_match_ben_achour() -> None:
    alpha, theta, phi = hopf_coordinate_symbols()
    embedding = hopf_embedding(alpha, theta, phi)
    metric = hopf_metric_tensor(alpha)
    coframe = orthonormal_coframe(alpha)

    assert embedding[0] == sp.sin(alpha) * sp.cos(phi)
    assert embedding[1] == sp.sin(alpha) * sp.sin(phi)
    assert embedding[2] == sp.cos(alpha) * sp.cos(theta)
    assert embedding[3] == sp.cos(alpha) * sp.sin(theta)
    assert metric == sp.diag(1, sp.cos(alpha) ** 2, sp.sin(alpha) ** 2)
    assert coframe[0].as_matrix() == sp.Matrix([1, 0, 0])
    assert coframe[1].as_matrix() == sp.Matrix([0, sp.cos(alpha), 0])
    assert coframe[2].as_matrix() == sp.Matrix([0, 0, sp.sin(alpha)])


def test_killing_one_forms_are_metric_duals_and_star_d_smoke_checks() -> None:
    alpha, theta, phi = hopf_coordinate_symbols()
    xi = xi_flat(alpha)
    xip = xi_prime_flat(alpha)

    assert one_form_norm_squared(xi, alpha) == 1
    assert one_form_norm_squared(xip, alpha) == 1

    xi_star_d = star_d_one_form(xi, alpha, theta, phi).as_matrix()
    xip_star_d = star_d_one_form(xip, alpha, theta, phi).as_matrix()

    assert all(
        sp.simplify(sp.expand_trig(value)) == 0
        for value in (xi_star_d + 2 * xi.as_matrix())
    )
    assert all(
        sp.simplify(sp.expand_trig(value)) == 0
        for value in (xip_star_d - 2 * xip.as_matrix())
    )


def test_low_mode_e_modes_nonzero_for_l2_nonboundary_labels() -> None:
    result = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)

    assert result.source_geometry_status == SOURCE_SUPPORTED_GEOMETRY
    assert result.normalization_status == NORMALIZATION_DEPENDENT
    assert result.readiness_verdict == BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE
    assert result.mode_applicability_status == SOURCE_SUPPORTED_GEOMETRY
    assert result.E.as_matrix().shape == (3, 1)
    assert result.E_prime.as_matrix().shape == (3, 1)
    assert any(sp.simplify(component) != 0 for component in result.E.as_matrix())
    assert any(sp.simplify(component) != 0 for component in result.E_prime.as_matrix())


def test_l1_is_classified_as_excluded_not_success() -> None:
    assert mode_applicability_status(1) == VANISHING_OR_EXCLUDED
    assert mode_applicability_status(0) == VANISHING_OR_EXCLUDED


def test_scalar_mode_phase_eigenvalues_match_displayed_convention() -> None:
    alpha, theta, phi = hopf_coordinate_symbols()
    scalar = scalar_mode_symbolic(2, 1, 1, alpha, theta, phi)

    xi_action = sp.simplify(sp.diff(scalar, theta) + sp.diff(scalar, phi))
    xi_prime_action = sp.simplify(sp.diff(scalar, phi) - sp.diff(scalar, theta))

    assert sp.simplify(xi_action - 2 * sp.I * scalar) == 0
    assert sp.simplify(xi_prime_action - 2 * sp.I * scalar) == 0
