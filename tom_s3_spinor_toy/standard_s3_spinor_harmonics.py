"""Standard lowest spinor harmonics on S^3 in Hopf/Lawrence coordinates.

This module provides a minimal standard spinor-harmonic frame for the round
three-sphere. It is intentionally small:

- no kNN;
- no S6 / SU4;
- no instantons / index / chirality;
- no heavy spectral computation.

The construction is the lowest Killing-spinor / spin-frame layer written in the
Hopf-like coordinates used in the Lawrence recovery:

    x1 = rho sin(alpha) cos(theta)
    x2 = rho sin(alpha) sin(theta)
    x3 = rho cos(alpha) sin(theta_tilde)
    x4 = rho cos(alpha) cos(theta_tilde)

The returned 2x2 matrix is unitary pointwise and its entries carry the expected
Cartan phases for the lowest S3 spinor harmonics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import numpy as np


SQRT2_INV: Final[float] = 1.0 / np.sqrt(2.0)


@dataclass(frozen=True)
class CartanWeight:
    """Weight pair for (I_{3L}, I_{3R}) in the local convention."""

    i_l: float
    i_r: float


def _phase(theta: float | np.ndarray, theta_tilde: float | np.ndarray, sign: int) -> np.ndarray:
    """Convenience phase helper.

    sign = +1 gives exp(i(theta ± theta_tilde)/2); sign = -1 gives the
    conjugate phase.
    """

    return np.exp(0.5j * sign * (theta + theta_tilde))


def standard_spinor_frame(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> np.ndarray:
    """Return the lowest standard S3 spinor frame as a 2x2 unitary matrix.

    The columns form the two lowest Killing-spinor basis states in the local
    Hopf/Lawrence chart:

        U = [[ cos(a) e^{+i(θ+θ~)/2},  sin(a) e^{+i(θ-θ~)/2}],
             [-sin(a) e^{-i(θ-θ~)/2},  cos(a) e^{-i(θ+θ~)/2}]]

    This is the standard SU(2) spin-frame matrix. Its columns are orthonormal
    pointwise and regular at alpha = 0 and alpha = pi/2.
    """

    c = np.cos(alpha)
    s = np.sin(alpha)
    a_plus = 0.5 * (theta + theta_tilde)
    a_minus = 0.5 * (theta - theta_tilde)

    return np.array(
        [
            [c * np.exp(1.0j * a_plus), s * np.exp(1.0j * a_minus)],
            [-s * np.exp(-1.0j * a_minus), c * np.exp(-1.0j * a_plus)],
        ],
        dtype=complex,
    )


def standard_spinor_entries(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
) -> dict[str, np.ndarray]:
    """Return the four scalar entries with explicit Cartan labels."""

    frame = standard_spinor_frame(alpha, theta, theta_tilde)
    return {
        "plus_plus": frame[0, 0],
        "plus_minus": frame[0, 1],
        "minus_plus": frame[1, 0],
        "minus_minus": frame[1, 1],
    }


def standard_spinor_cartan_weights() -> dict[str, CartanWeight]:
    """Cartan weights for the four matrix entries.

    Local convention:
        i I_{3L} = 1/2 (partial_theta + partial_theta_tilde)
        i I_{3R} = 1/2 (partial_theta - partial_theta_tilde)
    """

    return {
        "plus_plus": CartanWeight(+0.5, 0.0),
        "plus_minus": CartanWeight(0.0, +0.5),
        "minus_plus": CartanWeight(0.0, -0.5),
        "minus_minus": CartanWeight(-0.5, 0.0),
    }


def su2_fundamental_generators() -> dict[str, np.ndarray]:
    """Fundamental su(2) generators J_i = sigma_i / 2."""

    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    return {
        "J1": 0.5 * sigma1,
        "J2": 0.5 * sigma2,
        "J3": 0.5 * sigma3,
    }


def lifted_su2_generators() -> dict[str, dict[str, np.ndarray]]:
    """Left and right su(2) actions on the 2x2 spin frame.

    The frame entries can be viewed as the tensor-product basis
    |m_L> \otimes |m_R> with left action on rows and right action on columns.
    """

    j = su2_fundamental_generators()
    eye = np.eye(2, dtype=complex)
    return {
        "left": {name: np.kron(gen, eye) for name, gen in j.items()},
        "right": {name: np.kron(eye, gen) for name, gen in j.items()},
    }


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Matrix commutator [a, b]."""

    return a @ b - b @ a


def frame_is_unitary(
    alpha: float | np.ndarray,
    theta: float | np.ndarray,
    theta_tilde: float | np.ndarray,
    atol: float = 1e-12,
) -> bool:
    """Pointwise unitarity check for the spin frame."""

    frame = standard_spinor_frame(alpha, theta, theta_tilde)
    eye = np.eye(2, dtype=complex)
    return bool(np.allclose(frame.conj().T @ frame, eye, atol=atol))

