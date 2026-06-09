"""P5E smoke tests for explicit non-Cartan S3 coordinate generators.

These checks are local representation-sanity tests only. They verify that the
coordinate-space raw SU(2)_L x SU(2)_R generators act consistently on the
validated lowest standard S3 spinor frame.
"""

from __future__ import annotations

import numpy as np

from s3_lawrence_noncartan_generators import (
    ScalarDerivatives,
    apply_generator,
    lawrence_generator_aliases,
)
from standard_s3_spinor_harmonics import lifted_su2_generators


def _entry_bundle(alpha: float, theta: float, theta_tilde: float) -> dict[str, ScalarDerivatives]:
    """Return values and derivatives for the four standard basis entries."""

    c = np.cos(alpha)
    s = np.sin(alpha)
    ap = 0.5 * (theta + theta_tilde)
    am = 0.5 * (theta - theta_tilde)

    plus_plus = c * np.exp(1.0j * ap)
    plus_minus = s * np.exp(1.0j * am)
    minus_plus = -s * np.exp(-1.0j * am)
    minus_minus = c * np.exp(-1.0j * ap)

    return {
        "plus_plus": ScalarDerivatives(
            value=plus_plus,
            d_alpha=-s * np.exp(1.0j * ap),
            d_theta=0.5j * plus_plus,
            d_theta_tilde=0.5j * plus_plus,
        ),
        "plus_minus": ScalarDerivatives(
            value=plus_minus,
            d_alpha=c * np.exp(1.0j * am),
            d_theta=0.5j * plus_minus,
            d_theta_tilde=-0.5j * plus_minus,
        ),
        "minus_plus": ScalarDerivatives(
            value=minus_plus,
            d_alpha=-c * np.exp(-1.0j * am),
            d_theta=-0.5j * minus_plus,
            d_theta_tilde=0.5j * minus_plus,
        ),
        "minus_minus": ScalarDerivatives(
            value=minus_minus,
            d_alpha=-s * np.exp(-1.0j * ap),
            d_theta=-0.5j * minus_minus,
            d_theta_tilde=-0.5j * minus_minus,
        ),
    }


def _basis_action_matrix(kind: str, alpha: float, theta: float, theta_tilde: float) -> tuple[np.ndarray, np.ndarray]:
    """Return the basis vector and its generator action at one point."""

    bundle = _entry_bundle(alpha, theta, theta_tilde)
    basis = np.array([bundle[name].value for name in ("plus_plus", "plus_minus", "minus_plus", "minus_minus")], dtype=complex)
    action = np.array(
        [
            apply_generator(kind, bundle[name], alpha=alpha, theta=theta, theta_tilde=theta_tilde)
            for name in ("plus_plus", "plus_minus", "minus_plus", "minus_minus")
        ],
        dtype=complex,
    )
    return basis, action


def test_raw_generator_aliases_are_registered() -> None:
    """The raw Euler-generator names are the documented I-label aliases."""

    aliases = lawrence_generator_aliases()
    assert aliases == {
        "I1L": "L1",
        "I2L": "L2",
        "I3L": "L3",
        "I1R": "R1",
        "I2R": "R2",
        "I3R": "R3",
    }


def test_noncartan_generators_act_consistently_on_standard_spinor_frame() -> None:
    """The non-Cartan generators preserve the validated standard basis span."""

    points_a = [
        (0.41, 0.73, 1.29),
        (0.53, 0.91, 0.17),
        (0.22, 1.20, 0.80),
        (0.61, 0.20, 1.00),
    ]
    points_b = [
        (0.37, 0.11, 0.61),
        (0.45, 1.01, 0.31),
        (0.28, 0.90, 1.40),
        (0.56, 0.50, 0.20),
    ]
    kinds = ["L1", "L2", "L3", "R1", "R2", "R3"]

    def fit_matrix(points: list[tuple[float, float, float]], kind: str) -> np.ndarray:
        system = []
        rhs = []
        for alpha, theta, theta_tilde in points:
            basis, action = _basis_action_matrix(kind, alpha, theta, theta_tilde)
            for row in range(4):
                mat_row = np.zeros((4, 4), dtype=complex)
                mat_row[row, :] = basis
                system.append(mat_row.reshape(-1))
                rhs.append(action[row])
        system_arr = np.vstack(system)
        rhs_arr = np.asarray(rhs, dtype=complex)
        sol, *_ = np.linalg.lstsq(system_arr, rhs_arr, rcond=None)
        return sol.reshape(4, 4)

    for kind in kinds:
        matrix_a = fit_matrix(points_a, kind)
        matrix_b = fit_matrix(points_b, kind)
        np.testing.assert_allclose(matrix_a, matrix_b, atol=1e-10)


def test_noncartan_generators_match_lifted_standard_oracle() -> None:
    """The fitted coordinate generators agree with the lifted su(2) oracle."""

    oracle = lifted_su2_generators()
    points = [
        (0.41, 0.73, 1.29),
        (0.53, 0.91, 0.17),
        (0.22, 1.20, 0.80),
        (0.61, 0.20, 1.00),
    ]

    def fit_matrix(kind: str) -> np.ndarray:
        system = []
        rhs = []
        for alpha, theta, theta_tilde in points:
            bundle = _entry_bundle(alpha, theta, theta_tilde)
            basis = np.array(
                [bundle[name].value for name in ("plus_plus", "plus_minus", "minus_plus", "minus_minus")],
                dtype=complex,
            )
            action = np.array(
                [
                    apply_generator(kind, bundle[name], alpha=alpha, theta=theta, theta_tilde=theta_tilde)
                    for name in ("plus_plus", "plus_minus", "minus_plus", "minus_minus")
                ],
                dtype=complex,
            )
            for row in range(4):
                mat_row = np.zeros((4, 4), dtype=complex)
                mat_row[row, :] = basis
                system.append(mat_row.reshape(-1))
                rhs.append(action[row])
        system_arr = np.vstack(system)
        rhs_arr = np.asarray(rhs, dtype=complex)
        sol, *_ = np.linalg.lstsq(system_arr, rhs_arr, rcond=None)
        return sol.reshape(4, 4)

    expectations = {
        "L1": oracle["left"]["J1"],
        "L2": oracle["left"]["J2"],
        "L3": oracle["left"]["J3"],
        "R1": oracle["right"]["J1"],
        "R2": oracle["right"]["J2"],
        "R3": oracle["right"]["J3"],
    }

    for kind, target in expectations.items():
        fitted = fit_matrix(kind)
        np.testing.assert_allclose(fitted, target, atol=1e-10)


def test_noncartan_commutators_close_with_standard_convention() -> None:
    """The fitted generators satisfy the standard Hermitian su(2) convention."""

    oracle = lifted_su2_generators()
    left = oracle["left"]
    right = oracle["right"]

    np.testing.assert_allclose(
        left["J1"] @ left["J2"] - left["J2"] @ left["J1"],
        1.0j * left["J3"],
        atol=1e-12,
    )
    np.testing.assert_allclose(
        left["J2"] @ left["J3"] - left["J3"] @ left["J2"],
        1.0j * left["J1"],
        atol=1e-12,
    )
    np.testing.assert_allclose(
        left["J3"] @ left["J1"] - left["J1"] @ left["J3"],
        1.0j * left["J2"],
        atol=1e-12,
    )

    np.testing.assert_allclose(
        right["J1"] @ right["J2"] - right["J2"] @ right["J1"],
        1.0j * right["J3"],
        atol=1e-12,
    )
    np.testing.assert_allclose(
        right["J2"] @ right["J3"] - right["J3"] @ right["J2"],
        1.0j * right["J1"],
        atol=1e-12,
    )
    np.testing.assert_allclose(
        right["J3"] @ right["J1"] - right["J1"] @ right["J3"],
        1.0j * right["J2"],
        atol=1e-12,
    )

    for lname, lmat in left.items():
        for rname, rmat in right.items():
            np.testing.assert_allclose(lmat @ rmat - rmat @ lmat, np.zeros((4, 4), dtype=complex), atol=1e-12)
