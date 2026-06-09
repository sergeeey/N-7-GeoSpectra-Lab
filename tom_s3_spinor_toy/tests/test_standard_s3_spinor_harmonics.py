"""Tests for the standard lowest S3 spinor-harmonic frame.

This is a local representation-sanity layer only. It does not attempt to
validate Lawrence's original ansatz, S6/SU4, instantons, index theory, or any
heavy spectral computation.
"""

from __future__ import annotations

import numpy as np

from standard_s3_spinor_harmonics import (
    CartanWeight,
    commutator,
    frame_is_unitary,
    lifted_su2_generators,
    standard_spinor_cartan_weights,
    standard_spinor_entries,
    standard_spinor_frame,
)
from geometry_s3_hopf import volume_measure, s3_volume_analytical
from wigner_d_micro_audit import wigner_D


def _entry_derivatives(entry_name: str, value: complex) -> tuple[complex, complex]:
    """Analytic derivatives of each matrix entry with respect to (theta, theta_tilde)."""

    if entry_name == "plus_plus":
        return 0.5j * value, 0.5j * value
    if entry_name == "plus_minus":
        return 0.5j * value, -0.5j * value
    if entry_name == "minus_plus":
        return -0.5j * value, 0.5j * value
    if entry_name == "minus_minus":
        return -0.5j * value, -0.5j * value
    raise KeyError(entry_name)


def test_standard_spinor_frame_is_unitary_and_regular() -> None:
    """The lowest spin frame is pointwise unitary and finite at alpha endpoints."""

    theta = 0.37
    theta_tilde = 1.11
    for alpha in [0.0, 1e-8, 0.25, np.pi / 4, np.pi / 2 - 1e-8, np.pi / 2]:
        frame = standard_spinor_frame(alpha, theta, theta_tilde)
        assert np.isfinite(frame).all()
        assert frame_is_unitary(alpha, theta, theta_tilde)
        np.testing.assert_allclose(
            frame.conj().T @ frame,
            np.eye(2, dtype=complex),
            atol=1e-12,
        )
        det = np.linalg.det(frame)
        np.testing.assert_allclose(det, 1.0 + 0.0j, atol=1e-12)


def test_cartan_entry_phases_match_expected_weights() -> None:
    """Each matrix entry carries the expected local (I3L, I3R) phase weight."""

    alpha = 0.41
    theta = 0.73
    theta_tilde = 1.29
    entries = standard_spinor_entries(alpha, theta, theta_tilde)
    weights = standard_spinor_cartan_weights()

    for name, entry in entries.items():
        d_theta, d_theta_tilde = _entry_derivatives(name, entry)
        op_l = 0.5 * (d_theta + d_theta_tilde)
        op_r = 0.5 * (d_theta - d_theta_tilde)
        weight = weights[name]
        assert isinstance(weight, CartanWeight)
        np.testing.assert_allclose(op_l, 1j * weight.i_l * entry, atol=1e-12)
        np.testing.assert_allclose(op_r, 1j * weight.i_r * entry, atol=1e-12)


def test_lifted_su2_generators_close_and_commute_between_sides() -> None:
    """Left and right su(2) generators close with the standard commutators."""

    gens = lifted_su2_generators()
    left = gens["left"]
    right = gens["right"]

    eps = {
        ("J1", "J2"): "J3",
        ("J2", "J3"): "J1",
        ("J3", "J1"): "J2",
    }

    for (a, b), c in eps.items():
        np.testing.assert_allclose(commutator(left[a], left[b]), 1j * left[c], atol=1e-12)
        np.testing.assert_allclose(commutator(right[a], right[b]), 1j * right[c], atol=1e-12)
        np.testing.assert_allclose(commutator(left[a], right[b]), 0.0, atol=1e-12)


def test_standard_spinor_frame_columns_are_orthonormal() -> None:
    """The two basis spinors are orthonormal as the columns of an SU(2) matrix."""

    alpha = 0.53
    theta = 0.91
    theta_tilde = 0.17
    frame = standard_spinor_frame(alpha, theta, theta_tilde)

    col0 = frame[:, 0]
    col1 = frame[:, 1]
    np.testing.assert_allclose(np.vdot(col0, col0), 1.0 + 0.0j, atol=1e-12)
    np.testing.assert_allclose(np.vdot(col1, col1), 1.0 + 0.0j, atol=1e-12)
    np.testing.assert_allclose(np.vdot(col0, col1), 0.0 + 0.0j, atol=1e-12)


def test_standard_spinor_frame_matches_wigner_d_half_oracle() -> None:
    """The standard frame is the j=1/2 Wigner-D matrix up to a fixed sigma_3 gauge."""

    alpha = 0.41
    theta = 0.73
    theta_tilde = 1.29
    frame = standard_spinor_frame(alpha, theta, theta_tilde)

    euler_a = -theta
    euler_b = 2.0 * alpha
    euler_c = -theta_tilde
    wigner = np.array(
        [
            [
                wigner_D(0.5, 0.5, 0.5, euler_a, euler_b, euler_c),
                wigner_D(0.5, 0.5, -0.5, euler_a, euler_b, euler_c),
            ],
            [
                wigner_D(0.5, -0.5, 0.5, euler_a, euler_b, euler_c),
                wigner_D(0.5, -0.5, -0.5, euler_a, euler_b, euler_c),
            ],
        ],
        dtype=complex,
    )
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    oracle = sigma3 @ wigner @ sigma3

    np.testing.assert_allclose(frame, oracle, atol=1e-12)


def test_standard_spinor_frame_has_expected_haar_norms() -> None:
    """Each entry has the correct full-S3 Haar norm under the Lawrence measure."""

    alpha = np.linspace(0.0, np.pi / 2, 5001)
    frame = standard_spinor_frame(alpha, 0.23, 1.41)
    expected = np.pi**2

    for idx in np.ndindex(frame.shape[:2]):
        entry = frame[idx]
        norm_sq = float(
            np.trapezoid(np.abs(entry) ** 2 * volume_measure(alpha), alpha) * (2.0 * np.pi) ** 2
        )
        np.testing.assert_allclose(norm_sq, expected, rtol=1e-6, atol=1e-6)


def test_standard_spinor_frame_columns_normalize_to_s3_volume() -> None:
    """The column norms integrate to the S^3 volume, consistent with Haar normalization."""

    alpha = np.linspace(0.0, np.pi / 2, 5001)
    frame = standard_spinor_frame(alpha, 0.23, 1.41)
    vol = s3_volume_analytical()

    for col in range(2):
        norm_sq = 0.0
        for row in range(2):
            entry = frame[row, col]
            norm_sq += float(
                np.trapezoid(np.abs(entry) ** 2 * volume_measure(alpha), alpha) * (2.0 * np.pi) ** 2
            )
        np.testing.assert_allclose(norm_sq, vol, rtol=1e-6, atol=1e-6)
