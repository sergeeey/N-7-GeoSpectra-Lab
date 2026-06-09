"""Ben Achour et al. scalar harmonics on S3 in Hopf coordinates.

Reference: arXiv:1505.03426v2, "Explicit vector spherical harmonics on
the 3-sphere", Sec. II, eqs. (1)-(5).

Scope:
    This module implements the scalar-mode convention needed for local
    sanity checks. It is not a Dirac spinor-harmonic implementation.

Important caveat:
    The rendered PDF displays the scalar phase as exp(i(S phi + D theta))
    with S=m_+ + m_- and D=m_+ - m_-, but later states
    xi'(Phi_i)=nu_i Phi_i with nu_i=-2 i m_- for xi'=partial_phi-partial_theta.
    The displayed phase gives +2 i m_- under that operator. The project
    treats the sign as resolved in favor of the displayed-phase convention and
    keeps the paper-text minus only as a legacy note.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from scipy.special import eval_jacobi


def _is_integer_lattice(value: float, tol: float = 1e-12) -> bool:
    return abs(value - round(value)) < tol


def validate_quantum_numbers(L: int, m_plus: float, m_minus: float) -> None:
    """Validate Ben Achour scalar-mode labels.

    PDF constraints:
        |m_±| <= L/2
        L/2 - m_± in N

    The labels may be integer or half-integer depending on L.
    """
    if not isinstance(L, int) or L < 0:
        raise ValueError(f"L must be a non-negative integer, got {L!r}")

    half_l = L / 2.0
    if abs(m_plus) > half_l or abs(m_minus) > half_l:
        raise ValueError(
            f"Require abs(m_±) <= L/2, got L={L}, m_plus={m_plus}, m_minus={m_minus}"
        )

    if not _is_integer_lattice(half_l - m_plus) or not _is_integer_lattice(
        half_l - m_minus
    ):
        raise ValueError(
            "Require L/2 - m_± on the integer lattice, "
            f"got L={L}, m_plus={m_plus}, m_minus={m_minus}"
        )


def scalar_mode_unnormalized(
    L: int,
    m_plus: float,
    m_minus: float,
    alpha: np.ndarray | float,
    phi: np.ndarray | float,
    theta: np.ndarray | float,
) -> np.ndarray:
    """Evaluate the displayed Ben Achour scalar mode without normalization.

    Displayed eq. (3):
        Phi = C exp(i(S phi + D theta))
              (1 - x)^(S/2) (1 + x)^(D/2)
              P_{L/2-m_+}^{(S,D)}(x)

    where:
        x = cos(2 alpha)
        S = m_+ + m_-
        D = m_+ - m_-

    This helper is intended for convention tests. Use non-negative S and D
    unless the full paper normalization/branch convention is being handled.
    """
    validate_quantum_numbers(L, m_plus, m_minus)

    s_label = m_plus + m_minus
    d_label = m_plus - m_minus
    poly_order_float = L / 2.0 - m_plus
    if not _is_integer_lattice(poly_order_float):
        raise ValueError(f"Jacobi order must be integer, got {poly_order_float}")
    poly_order = int(round(poly_order_float))

    alpha_arr = np.asarray(alpha, dtype=float)
    phi_arr = np.asarray(phi, dtype=float)
    theta_arr = np.asarray(theta, dtype=float)

    x = np.cos(2.0 * alpha_arr)
    phase = np.exp(1j * (s_label * phi_arr + d_label * theta_arr))
    radial = ((1.0 - x) ** (s_label / 2.0)) * ((1.0 + x) ** (d_label / 2.0))
    jacobi = eval_jacobi(poly_order, s_label, d_label, x)
    return np.asarray(phase * radial * jacobi, dtype=complex)


def ben_achour_phase_eigenvalues(m_plus: float, m_minus: float) -> dict[str, complex]:
    """Eigenvalues implied by the displayed scalar phase.

    For exp(i(S phi + D theta)):
        (partial_phi + partial_theta) -> i(S + D) = 2 i m_+
        (partial_phi - partial_theta) -> i(S - D) = 2 i m_-
    """
    s_label = m_plus + m_minus
    d_label = m_plus - m_minus
    return {
        "partial_phi": 1j * s_label,
        "partial_theta": 1j * d_label,
        "xi": 1j * (s_label + d_label),
        "xi_prime_from_displayed_phase": 1j * (s_label - d_label),
    }


def pdf_stated_killing_eigenvalues(m_plus: float, m_minus: float) -> dict[str, complex]:
    """Eigenvalues stated below eqs. (4)-(5) in the rendered PDF."""
    return {
        "xi_pdf_stated": 2j * m_plus,
        "xi_prime_pdf_stated": -2j * m_minus,
    }


def scalar_mode_metadata(L: int, m_plus: float, m_minus: float) -> dict[str, Any]:
    """Return scalar-mode labels for reports/debugging."""
    validate_quantum_numbers(L, m_plus, m_minus)
    return {
        "L": L,
        "m_plus": m_plus,
        "m_minus": m_minus,
        "S": m_plus + m_minus,
        "D": m_plus - m_minus,
        "jacobi_order": int(round(L / 2.0 - m_plus)),
        "normalization": "omitted; use rendered PDF/original TeX for C_{L,m+,m-}",
        "domain": "alpha in [0, pi/2], phi/theta in [0, 2pi)",
    }
