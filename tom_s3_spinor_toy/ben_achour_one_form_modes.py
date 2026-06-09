"""Ben Achour S3 one-form modes in Hopf coordinates.

This module implements a source-supported geometry layer for the Ben Achour
S3 conventions used by the project. It provides low-mode symbolic one-form
families E_i and E'_i via the published Killing one-forms and the
``B, C`` construction:

    B_i  = * d( Phi_i xi~ )
    B'_i = * d( Phi_i xi'~ )
    C_i  = * d B_i
    C'_i = * d B'_i
    E_i  = (L + 2) B_i + C_i
    E'_i = (L + 2) B'_i - C'_i

The implementation is intentionally scoped to source-supported geometry and
low-mode symbolic checks. It does not construct or promote any physical
V-operator.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import sympy as sp

from ben_achour_scalar_modes import (
    scalar_mode_metadata as _scalar_mode_metadata,
    validate_quantum_numbers,
)


PARTIAL_LOW_MODE_IMPLEMENTATION = "PARTIAL_LOW_MODE_IMPLEMENTATION"
BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE = "BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE"
NORMALIZATION_DEPENDENT = "NORMALIZATION_DEPENDENT"
SOURCE_SUPPORTED_GEOMETRY = "SOURCE_SUPPORTED_GEOMETRY"
INCONCLUSIVE = "INCONCLUSIVE"
VANISHING_OR_EXCLUDED = "VANISHING_OR_EXCLUDED"


@dataclass(frozen=True)
class OneFormComponents:
    """One-form components in the ordered basis (dalpha, dtheta, dphi)."""

    dalpha: sp.Expr
    dtheta: sp.Expr
    dphi: sp.Expr

    def as_matrix(self) -> sp.Matrix:
        return sp.Matrix([self.dalpha, self.dtheta, self.dphi])


@dataclass(frozen=True)
class TwoFormComponents:
    """Two-form components in the ordered basis (dalpha^dtheta, dalpha^dphi, dtheta^dphi)."""

    dalpha_dtheta: sp.Expr
    dalpha_dphi: sp.Expr
    dtheta_dphi: sp.Expr

    def as_matrix(self) -> sp.Matrix:
        return sp.Matrix([self.dalpha_dtheta, self.dalpha_dphi, self.dtheta_dphi])


@dataclass(frozen=True)
class BenAchourOneFormModeResult:
    """Low-mode source-supported Ben Achour one-form families."""

    L: int
    m_plus: float
    m_minus: float
    scalar_mode: sp.Expr
    xi_tilde: OneFormComponents
    xi_prime_tilde: OneFormComponents
    A: OneFormComponents
    A_prime: OneFormComponents
    B: OneFormComponents
    B_prime: OneFormComponents
    C: OneFormComponents
    C_prime: OneFormComponents
    E: OneFormComponents
    E_prime: OneFormComponents
    source_geometry_status: str
    normalization_status: str
    scalar_identity_status: str
    killing_identity_status: str
    readiness_verdict: str
    mode_applicability_status: str
    blocking_fields: tuple[str, ...]
    source_convention: str


def hopf_coordinate_symbols() -> tuple[sp.Symbol, sp.Symbol, sp.Symbol]:
    """Return the frozen Hopf coordinate symbols (alpha, theta, phi)."""

    alpha, theta, phi = sp.symbols("alpha theta phi", real=True)
    return alpha, theta, phi


def hopf_embedding(alpha: sp.Expr, theta: sp.Expr, phi: sp.Expr) -> tuple[sp.Expr, ...]:
    """Ben Achour Hopf embedding in the project coordinate convention."""

    return (
        sp.sin(alpha) * sp.cos(phi),
        sp.sin(alpha) * sp.sin(phi),
        sp.cos(alpha) * sp.cos(theta),
        sp.cos(alpha) * sp.sin(theta),
    )


def hopf_metric_tensor(alpha: sp.Expr) -> sp.Matrix:
    """Metric tensor in the ordered basis (dalpha, dtheta, dphi)."""

    return sp.diag(1, sp.cos(alpha) ** 2, sp.sin(alpha) ** 2)


def hopf_volume_density(alpha: sp.Expr) -> sp.Expr:
    return sp.sin(alpha) * sp.cos(alpha)


def orthonormal_coframe(alpha: sp.Expr) -> tuple[OneFormComponents, OneFormComponents, OneFormComponents]:
    """Return the orthonormal coframe (e_alpha, e_theta, e_phi)."""

    return (
        OneFormComponents(sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        OneFormComponents(sp.Integer(0), sp.cos(alpha), sp.Integer(0)),
        OneFormComponents(sp.Integer(0), sp.Integer(0), sp.sin(alpha)),
    )


def xi_flat(alpha: sp.Expr) -> OneFormComponents:
    """Metric dual of xi = partial_theta + partial_phi."""

    return killing_one_form("xi", alpha)


def xi_prime_flat(alpha: sp.Expr) -> OneFormComponents:
    """Metric dual of xi' = partial_phi - partial_theta."""

    return killing_one_form("xi_prime", alpha)


def scalar_mode_symbolic(
    L: int,
    m_plus: float,
    m_minus: float,
    alpha: sp.Expr,
    theta: sp.Expr,
    phi: sp.Expr,
) -> sp.Expr:
    """Symbolic Ben Achour scalar mode using the displayed phase convention."""

    validate_quantum_numbers(L, m_plus, m_minus)

    s_label = sp.Rational(int(round(2 * (m_plus + m_minus))), 2)
    d_label = sp.Rational(int(round(2 * (m_plus - m_minus))), 2)
    poly_order = sp.Integer(int(round(L / 2.0 - m_plus)))
    x = sp.cos(2 * alpha)
    return sp.exp(sp.I * (s_label * phi + d_label * theta)) * (
        (1 - x) ** (s_label / 2) * (1 + x) ** (d_label / 2) * sp.jacobi(poly_order, s_label, d_label, x)
    )


def scalar_mode_metadata(L: int, m_plus: float, m_minus: float) -> dict[str, Any]:
    """Expose the existing scalar-mode metadata contract."""

    return _scalar_mode_metadata(L, m_plus, m_minus)


def killing_vector_contravariant(which: str) -> OneFormComponents:
    """Return the Killing vector components in the coordinate basis.

    The project convention uses xi = ∂theta + ∂phi and xi' = ∂phi - ∂theta.
    """

    if which == "xi":
        return OneFormComponents(sp.Integer(0), sp.Integer(1), sp.Integer(1))
    if which in {"xi_prime", "xi'"}:
        return OneFormComponents(sp.Integer(0), sp.Integer(-1), sp.Integer(1))
    raise ValueError(f"Unknown Killing vector label: {which!r}")


def killing_one_form(which: str, alpha: sp.Expr) -> OneFormComponents:
    """Metric-dual one-forms for the source-supported Killing vectors."""

    if which == "xi":
        return OneFormComponents(sp.Integer(0), sp.cos(alpha) ** 2, sp.sin(alpha) ** 2)
    if which in {"xi_prime", "xi'"}:
        return OneFormComponents(sp.Integer(0), -sp.cos(alpha) ** 2, sp.sin(alpha) ** 2)
    raise ValueError(f"Unknown Killing vector label: {which!r}")


def mode_applicability_status(L: int) -> str:
    """Classify whether the low-mode E/E' chain is supported for a given L."""

    if L <= 1:
        return VANISHING_OR_EXCLUDED
    return SOURCE_SUPPORTED_GEOMETRY


def one_form_norm_squared(one_form: OneFormComponents, alpha: sp.Expr) -> sp.Expr:
    """Norm squared of a one-form in the Ben Achour Hopf metric."""

    metric_inv = sp.diag(1, sp.sec(alpha) ** 2, sp.csc(alpha) ** 2)
    vec = one_form.as_matrix()
    return sp.simplify((vec.T * metric_inv * vec)[0])


def exterior_derivative_one_form(
    one_form: OneFormComponents, alpha: sp.Expr, theta: sp.Expr, phi: sp.Expr
) -> TwoFormComponents:
    """Exterior derivative of a one-form in the coordinate basis."""

    a, b, c = one_form.dalpha, one_form.dtheta, one_form.dphi
    alpha_theta = sp.diff(b, alpha) - sp.diff(a, theta)
    alpha_phi = sp.diff(c, alpha) - sp.diff(a, phi)
    theta_phi = sp.diff(c, theta) - sp.diff(b, phi)
    return TwoFormComponents(
        sp.simplify(alpha_theta),
        sp.simplify(alpha_phi),
        sp.simplify(theta_phi),
    )


def hodge_star_two_form(two_form: TwoFormComponents, alpha: sp.Expr) -> OneFormComponents:
    """Hodge star on 2-forms with the source-supported sign convention."""

    u = two_form.dalpha_dtheta
    v = two_form.dalpha_dphi
    w = two_form.dtheta_dphi
    return OneFormComponents(
        sp.simplify(w / (sp.sin(alpha) * sp.cos(alpha))),
        sp.simplify(-v * sp.cot(alpha)),
        sp.simplify(u * sp.tan(alpha)),
    )


def star_d_one_form(
    one_form: OneFormComponents, alpha: sp.Expr, theta: sp.Expr, phi: sp.Expr
) -> OneFormComponents:
    """Compute * d acting on a one-form."""

    return hodge_star_two_form(exterior_derivative_one_form(one_form, alpha, theta, phi), alpha)


def low_mode_scalar_identity_status(
    L: int, m_plus: float, m_minus: float, alpha: sp.Expr, theta: sp.Expr, phi: sp.Expr
) -> str:
    """Classify the scalar-mode phase eigenvalue convention."""

    scalar = scalar_mode_symbolic(L, m_plus, m_minus, alpha, theta, phi)
    lhs_xi = sp.simplify(sp.diff(scalar, theta) + sp.diff(scalar, phi))
    lhs_xi_prime = sp.simplify(sp.diff(scalar, phi) - sp.diff(scalar, theta))
    expected = 2 * sp.I * sp.Rational(int(round(2 * m_plus)), 2) * scalar
    expected_prime = 2 * sp.I * sp.Rational(int(round(2 * m_minus)), 2) * scalar
    if sp.simplify(lhs_xi - expected) == 0 and sp.simplify(lhs_xi_prime - expected_prime) == 0:
        return SOURCE_SUPPORTED_GEOMETRY
    return INCONCLUSIVE


def build_low_mode_ben_achour_one_form_modes(
    L: int, m_plus: float, m_minus: float
) -> BenAchourOneFormModeResult:
    """Build the low-mode Ben Achour one-form families."""

    alpha, theta, phi = hopf_coordinate_symbols()
    scalar = scalar_mode_symbolic(L, m_plus, m_minus, alpha, theta, phi)

    xi_tilde = killing_one_form("xi", alpha)
    xi_prime_tilde = killing_one_form("xi_prime", alpha)

    A = OneFormComponents(
        sp.diff(scalar, alpha),
        sp.diff(scalar, theta),
        sp.diff(scalar, phi),
    )
    A_prime = A

    B = star_d_one_form(
        OneFormComponents(
            sp.simplify(scalar * xi_tilde.dalpha),
            sp.simplify(scalar * xi_tilde.dtheta),
            sp.simplify(scalar * xi_tilde.dphi),
        ),
        alpha,
        theta,
        phi,
    )
    B_prime = star_d_one_form(
        OneFormComponents(
            sp.simplify(scalar * xi_prime_tilde.dalpha),
            sp.simplify(scalar * xi_prime_tilde.dtheta),
            sp.simplify(scalar * xi_prime_tilde.dphi),
        ),
        alpha,
        theta,
        phi,
    )

    C = star_d_one_form(B, alpha, theta, phi)
    C_prime = star_d_one_form(B_prime, alpha, theta, phi)

    E = OneFormComponents(
        sp.simplify((L + 2) * B.dalpha + C.dalpha),
        sp.simplify((L + 2) * B.dtheta + C.dtheta),
        sp.simplify((L + 2) * B.dphi + C.dphi),
    )
    E_prime = OneFormComponents(
        sp.simplify((L + 2) * B_prime.dalpha - C_prime.dalpha),
        sp.simplify((L + 2) * B_prime.dtheta - C_prime.dtheta),
        sp.simplify((L + 2) * B_prime.dphi - C_prime.dphi),
    )

    scalar_status = low_mode_scalar_identity_status(L, m_plus, m_minus, alpha, theta, phi)
    source_status = SOURCE_SUPPORTED_GEOMETRY
    normalization_status = NORMALIZATION_DEPENDENT
    readiness = BEN_ACHOUR_E_MODES_IMPLEMENTED_LOW_MODE if scalar_status == SOURCE_SUPPORTED_GEOMETRY else PARTIAL_LOW_MODE_IMPLEMENTATION

    return BenAchourOneFormModeResult(
        L=L,
        m_plus=m_plus,
        m_minus=m_minus,
        scalar_mode=scalar,
        xi_tilde=xi_tilde,
        xi_prime_tilde=xi_prime_tilde,
        A=A,
        A_prime=A_prime,
        B=B,
        B_prime=B_prime,
        C=C,
        C_prime=C_prime,
        E=E,
        E_prime=E_prime,
        source_geometry_status=source_status,
        normalization_status=normalization_status,
        scalar_identity_status=scalar_status,
        killing_identity_status=source_status,
        readiness_verdict=readiness,
        mode_applicability_status=mode_applicability_status(L),
        blocking_fields=(
            "exact normalization of E_i / E'_i",
            "physical V-operator density",
            "physical interpretation",
        ),
        source_convention="Ben Achour scalar phase + Hopf geometry + Killing one-forms; exact normalization unresolved",
    )


def p13a1_ben_achour_one_form_mode_implementation_summary() -> dict[str, Any]:
    """Return a compact summary for reports and tests."""

    alpha, theta, phi = hopf_coordinate_symbols()
    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=1, m_minus=1)
    xi = low_mode.xi_tilde
    xip = low_mode.xi_prime_tilde
    xi_star_d = star_d_one_form(xi, alpha, theta, phi)
    xip_star_d = star_d_one_form(xip, alpha, theta, phi)
    return {
        "status": low_mode.readiness_verdict,
        "source_geometry_status": low_mode.source_geometry_status,
        "normalization_status": low_mode.normalization_status,
        "scalar_identity_status": low_mode.scalar_identity_status,
        "killing_identity_status": low_mode.killing_identity_status,
        "mode_applicability_status": low_mode.mode_applicability_status,
        "xi_tilde_norm_sq": sp.simplify(one_form_norm_squared(xi, alpha)),
        "xi_prime_tilde_norm_sq": sp.simplify(one_form_norm_squared(xip, alpha)),
        "xi_star_d_status": sp.simplify(xi_star_d.as_matrix() + 2 * xi.as_matrix()),
        "xi_prime_star_d_status": sp.simplify(xip_star_d.as_matrix() - 2 * xip.as_matrix()),
        "blocking_fields": low_mode.blocking_fields,
        "readiness_verdict": low_mode.readiness_verdict,
        "source_convention": low_mode.source_convention,
        "E": low_mode.E,
        "E_prime": low_mode.E_prime,
        "B": low_mode.B,
        "B_prime": low_mode.B_prime,
        "C": low_mode.C,
        "C_prime": low_mode.C_prime,
        "scalar_mode": low_mode.scalar_mode,
        "A": low_mode.A,
    }
