"""Exact non-Cartan S3 generators in the Lawrence/Hopf chart.

This module records the standard raw SU(2)_L x SU(2)_R Killing fields in the
Euler-angle chart that underlies the repository's Wigner-D oracle:

    a = -theta
    b = 2 * alpha
    c = -theta_tilde

The implementation is intentionally lightweight. It does not touch S6 / SU4,
instanton / index / chirality claims, or any heavy spectral computation.

Convention:
    We expose the Hermitian left/right generators as I_{aL} and I_{aR} with
    a = 1, 2, 3, using the standard physics convention

        I = -i X

    for the underlying real Killing vector field X.  This is the exact
    coordinate-space layer needed for the standard S3 spinor-harmonic audit.
    The earlier Lawrence Cartan half-sum / half-difference bookkeeping remains
    a separate convention layer.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ScalarDerivatives:
    """First derivatives of a scalar function in (alpha, theta, theta_tilde)."""

    value: complex
    d_alpha: complex
    d_theta: complex
    d_theta_tilde: complex


def _prepare_trig(alpha: float | np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    alpha_arr = np.asarray(alpha, dtype=float)
    sin_2a = np.sin(2.0 * alpha_arr)
    cos_2a = np.cos(2.0 * alpha_arr)
    return sin_2a, cos_2a


def _lplus_coefficients(
    alpha: float | np.ndarray, theta: float | np.ndarray, theta_tilde: float | np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sin_2a, cos_2a = _prepare_trig(alpha)
    exp_m_theta = np.exp(-1.0j * np.asarray(theta, dtype=float))
    coeff_alpha = 0.5 * exp_m_theta
    coeff_theta = -1.0j * exp_m_theta * (cos_2a / sin_2a)
    coeff_theta_tilde = 1.0j * exp_m_theta / sin_2a
    return coeff_alpha, coeff_theta, coeff_theta_tilde


def _lminus_coefficients(
    alpha: float | np.ndarray, theta: float | np.ndarray, theta_tilde: float | np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sin_2a, cos_2a = _prepare_trig(alpha)
    exp_p_theta = np.exp(1.0j * np.asarray(theta, dtype=float))
    coeff_alpha = -0.5 * exp_p_theta
    coeff_theta = -1.0j * exp_p_theta * (cos_2a / sin_2a)
    coeff_theta_tilde = 1.0j * exp_p_theta / sin_2a
    return coeff_alpha, coeff_theta, coeff_theta_tilde


def _rplus_coefficients(
    alpha: float | np.ndarray, theta: float | np.ndarray, theta_tilde: float | np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sin_2a, cos_2a = _prepare_trig(alpha)
    exp_m_t = np.exp(-1.0j * np.asarray(theta_tilde, dtype=float))
    coeff_alpha = -0.5 * exp_m_t
    coeff_theta = -1.0j * exp_m_t / sin_2a
    coeff_theta_tilde = 1.0j * exp_m_t * (cos_2a / sin_2a)
    return coeff_alpha, coeff_theta, coeff_theta_tilde


def _rminus_coefficients(
    alpha: float | np.ndarray, theta: float | np.ndarray, theta_tilde: float | np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    sin_2a, cos_2a = _prepare_trig(alpha)
    exp_p_t = np.exp(1.0j * np.asarray(theta_tilde, dtype=float))
    coeff_alpha = 0.5 * exp_p_t
    coeff_theta = -1.0j * exp_p_t / sin_2a
    coeff_theta_tilde = 1.0j * exp_p_t * (cos_2a / sin_2a)
    return coeff_alpha, coeff_theta, coeff_theta_tilde


def raw_left_right_generator_coefficients(
    kind: str,
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return coefficients for the raw Euler-angle Killing fields.

    The operator acts on a scalar f(alpha, theta, theta_tilde) as

        coeff_alpha * partial_alpha f
        + coeff_theta * partial_theta f
        + coeff_theta_tilde * partial_theta_tilde f

    Supported kinds:
        L1, L2, L3, R1, R2, R3

    The underlying ladder operators are the standard SU(2) Euler-angle
    fields in the chart:

        a = -theta
        b = 2 alpha
        c = -theta_tilde

    and then converted back to (alpha, theta, theta_tilde).
    """

    if kind == "L1":
        lplus = _lplus_coefficients(alpha, theta, theta_tilde)
        lminus = _lminus_coefficients(alpha, theta, theta_tilde)
        return tuple(0.5 * (lp + lm) for lp, lm in zip(lplus, lminus))

    if kind == "L2":
        lplus = _lplus_coefficients(alpha, theta, theta_tilde)
        lminus = _lminus_coefficients(alpha, theta, theta_tilde)
        return tuple((lp - lm) / (2.0j) for lp, lm in zip(lplus, lminus))

    if kind == "L3":
        alpha_arr = np.asarray(alpha, dtype=float)
        zeros = np.zeros_like(alpha_arr)
        ones = np.ones_like(alpha_arr)
        return zeros, -1.0j * ones, zeros

    if kind == "R1":
        rplus = _rplus_coefficients(alpha, theta, theta_tilde)
        rminus = _rminus_coefficients(alpha, theta, theta_tilde)
        return tuple(0.5 * (rp + rm) for rp, rm in zip(rplus, rminus))

    if kind == "R2":
        rplus = _rplus_coefficients(alpha, theta, theta_tilde)
        rminus = _rminus_coefficients(alpha, theta, theta_tilde)
        return tuple((rp - rm) / (2.0j) for rp, rm in zip(rplus, rminus))

    if kind == "R3":
        alpha_arr = np.asarray(alpha, dtype=float)
        zeros = np.zeros_like(alpha_arr)
        ones = np.ones_like(alpha_arr)
        return zeros, zeros, -1.0j * ones

    raise KeyError(kind)


def apply_generator(
    kind: str,
    derivatives: ScalarDerivatives,
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> np.ndarray:
    """Apply one raw generator to a scalar with precomputed derivatives."""

    coeff_alpha, coeff_theta, coeff_theta_tilde = raw_left_right_generator_coefficients(
        kind, alpha, theta, theta_tilde
    )
    return (
        coeff_alpha * derivatives.d_alpha
        + coeff_theta * derivatives.d_theta
        + coeff_theta_tilde * derivatives.d_theta_tilde
    )


def lawrence_generator_aliases() -> dict[str, str]:
    """Map the project's I-labels to the raw SU(2) generator names used here."""

    return {
        "I1L": "L1",
        "I2L": "L2",
        "I3L": "L3",
        "I1R": "R1",
        "I2R": "R2",
        "I3R": "R3",
    }
