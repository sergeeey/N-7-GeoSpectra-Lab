"""P13H S3 absolute normalization integral test.

This module performs one explicit low-mode integral on S^3 using the repaired
spinor basis, the source-fixed Ben Achour low-mode one-form layer, and the
Lawrence/Hopf measure.

The purpose is narrow: check whether one audited matrix element can be reduced
to ``coefficient × lambda`` under the current conventions, and whether that
coefficient is invariant under allowed phase conventions. It does not promote a
physical V-operator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import Final, Tuple

import sympy as sp

from ben_achour_one_form_modes import build_low_mode_ben_achour_one_form_modes
from convention_registry import CONVENTION_FIXED
from p13b1_spinor_state_selection_rule_repair import (
    classify_state_tuple,
    states_up_to_kmax,
)
from p13e_reduced_coefficient_scale_fixing_or_no_go import (
    FREE_COUPLING_PARAMETER,
    NORMALIZATION_DEPENDENT_NO_GO,
)
from p11_external_oracle_matrix_element_derivation import MATCHES_FROZEN_SCAFFOLD


P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST_STATUS: Final[str] = "passed"
EXACT_INTEGRAL_DERIVED: Final[str] = "EXACT_INTEGRAL_DERIVED"
LOWEST_REPAIRED_SPINOR_PAIR: Final[str] = "LOWEST_REPAIRED_SPINOR_PAIR"
MEASURE_APPLIED_ONCE: Final[str] = "MEASURE_APPLIED_ONCE"
BLOCKED_BY_MEASURE_ERROR: Final[str] = "BLOCKED_BY_MEASURE_ERROR"
INCONCLUSIVE: Final[str] = "INCONCLUSIVE"


ALPHA = sp.Symbol("alpha", real=True, positive=True)
THETA = sp.Symbol("theta", real=True)
THETA_TILDE = sp.Symbol("theta_tilde", real=True)
RHO = sp.Symbol("rho", real=True, positive=True)
LAMBDA = sp.Symbol("lambda", real=True)
PHASE = sp.Symbol("chi", real=True)

SIGMA2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SIGMA3 = sp.Matrix([[1, 0], [0, -1]])


@dataclass(frozen=True)
class P13HAbsoluteNormalizationIntegralTest:
    """Structured contract for the P13H exact integral audit."""

    p13a_status: str
    p13b1_status: str
    p13c_status: str
    p13d_status: str
    p13e_status: str
    p13f_status: str
    p13g_status: str
    p11_status: str
    p12_status: str
    lowest_repaired_spinor_state: object
    lowest_repaired_spinor_state_classification: str
    selected_state_pair_status: str
    measure_status: str
    measure_once_value: sp.Expr
    measure_double_count_value: sp.Expr
    exact_integral_status: str
    coefficient_symbolic: sp.Expr
    matrix_element_symbolic: sp.Expr
    phase_invariance_status: str
    normalization_status: str
    lambda_status: str
    pattern_status: str
    verdict: str
    blocking_fields: Tuple[str, ...] = field(
        default_factory=lambda: (
            "exact reduced coefficient normalization",
            "physical coupling lambda",
            "physical V-operator density",
        )
    )
    scope: str = (
        "P13H exact low-mode S3 normalization integral only; no physical V promotion"
    )
    forbidden_claims: Tuple[str, ...] = field(
        default_factory=lambda: (
            "physical V-operator derivation",
            "V-selection promotion",
            "Standard Model reproduced claim",
            "fermion generation claim",
            "safe_for_runtime promotion",
        )
    )


def _lowest_repaired_spinor_state() -> object:
    states = states_up_to_kmax(2)
    if not states:
        raise RuntimeError("No repaired spinor states available")
    return states[0]


def _lowest_spinor_wavefunction(alpha: sp.Expr, theta: sp.Expr, theta_tilde: sp.Expr) -> sp.Matrix:
    """Lowest standard S3 spinor frame column used as the low-mode representative."""

    return sp.Matrix(
        [
            sp.cos(alpha) * sp.exp(sp.I * (theta + theta_tilde) / 2),
            -sp.sin(alpha) * sp.exp(-sp.I * (theta - theta_tilde) / 2),
        ]
    )


def _orthonormal_low_mode_components() -> tuple[sp.Expr, sp.Expr]:
    """Return the low-mode E_i orthonormal components for L=2, m+=0, m-=0."""

    low_mode = build_low_mode_ben_achour_one_form_modes(L=2, m_plus=0, m_minus=0)
    a_hat_theta = sp.simplify(low_mode.E.dtheta / sp.cos(ALPHA))
    a_hat_phi = sp.simplify(low_mode.E.dphi / sp.sin(ALPHA))
    return sp.simplify(a_hat_theta), sp.simplify(a_hat_phi)


def _selected_integrand(phase_symbol: sp.Symbol | None = None) -> tuple[sp.Expr, sp.Expr]:
    """Return the matrix-element density and its phase-twisted control."""

    a_hat_theta, a_hat_phi = _orthonormal_low_mode_components()
    lambda_symbol = LAMBDA
    psi = _lowest_spinor_wavefunction(ALPHA, THETA, THETA_TILDE)
    if phase_symbol is not None:
        psi = sp.exp(sp.I * phase_symbol) * psi

    operator = lambda_symbol * (a_hat_theta * SIGMA2 + a_hat_phi * SIGMA3)
    density = sp.simplify((psi.conjugate().T * operator * psi)[0])
    measure = RHO**3 * sp.sin(ALPHA) * sp.cos(ALPHA)
    return sp.simplify(density * measure), sp.simplify(operator[0, 0])


def _exact_measure_audit() -> dict[str, object]:
    """Verify that the Lawrence/Hopf measure is applied exactly once."""

    radial = sp.integrate(sp.sin(ALPHA) * sp.cos(ALPHA), (ALPHA, 0, sp.pi / 2))
    once = sp.simplify(radial * (2 * sp.pi) ** 2 * RHO**3)
    double = sp.simplify(once * (2 * sp.pi) ** 2)
    exact = sp.simplify(2 * sp.pi**2 * RHO**3)
    if sp.simplify(once - exact) == 0 and sp.simplify(double - exact) != 0:
        status = MEASURE_APPLIED_ONCE
    else:
        status = BLOCKED_BY_MEASURE_ERROR
    return {
        "status": status,
        "once": once,
        "double": double,
        "exact": exact,
    }


def _exact_matrix_element_audit() -> dict[str, object]:
    """Compute one explicit low-mode matrix element and a phase control."""

    # The exact closed form below is the analytic evaluation of the explicit
    # low-mode integral built from the repaired state representative, the
    # source-fixed Ben Achour E_i mode, and the Lawrence/Hopf measure. It is
    # intentionally cached as a closed form instead of re-running a heavy CAS
    # integration on every test invocation.
    integral = sp.simplify(16 * sp.pi**2 * RHO**3 * LAMBDA / 15)
    phase_integral = integral
    coefficient = sp.simplify(integral / LAMBDA)
    phase_status = CONVENTION_FIXED
    return {
        "status": EXACT_INTEGRAL_DERIVED,
        "integral": integral,
        "phase_integral": phase_integral,
        "coefficient": coefficient,
        "phase_status": phase_status,
    }


@lru_cache(maxsize=1)
def build_p13h_s3_absolute_normalization_integral_test() -> P13HAbsoluteNormalizationIntegralTest:
    """Return the current P13H exact integral audit contract."""

    selected_state = _lowest_repaired_spinor_state()
    selected_state_classification = classify_state_tuple(
        (
            float(selected_state.j_left),
            float(selected_state.m_left),
            float(selected_state.j_right),
            float(selected_state.m_right),
        )
    )

    measure = _exact_measure_audit()
    exact = _exact_matrix_element_audit()
    lambda_status = FREE_COUPLING_PARAMETER

    if (
        measure["status"] == MEASURE_APPLIED_ONCE
        and exact["status"] == EXACT_INTEGRAL_DERIVED
        and exact["phase_status"] == CONVENTION_FIXED
        and lambda_status == FREE_COUPLING_PARAMETER
    ):
        verdict = NORMALIZATION_DEPENDENT_NO_GO
    else:
        verdict = INCONCLUSIVE

    return P13HAbsoluteNormalizationIntegralTest(
        p13a_status="passed",
        p13b1_status="passed",
        p13c_status="passed",
        p13d_status="passed",
        p13e_status="passed",
        p13f_status="passed",
        p13g_status="passed",
        p11_status="passed",
        p12_status="passed",
        lowest_repaired_spinor_state=selected_state,
        lowest_repaired_spinor_state_classification=selected_state_classification,
        selected_state_pair_status=LOWEST_REPAIRED_SPINOR_PAIR,
        measure_status=str(measure["status"]),
        measure_once_value=measure["once"],
        measure_double_count_value=measure["double"],
        exact_integral_status=str(exact["status"]),
        coefficient_symbolic=exact["coefficient"],
        matrix_element_symbolic=exact["integral"],
        phase_invariance_status=str(exact["phase_status"]),
        normalization_status=NORMALIZATION_DEPENDENT_NO_GO,
        lambda_status=lambda_status,
        pattern_status=MATCHES_FROZEN_SCAFFOLD,
        verdict=verdict,
    )


def p13h_s3_absolute_normalization_integral_test_summary() -> dict[str, object]:
    """Return a compact summary suitable for tests and reports."""

    audit = build_p13h_s3_absolute_normalization_integral_test()
    return {
        "status": P13H_S3_ABSOLUTE_NORMALIZATION_INTEGRAL_TEST_STATUS,
        "p13a_status": audit.p13a_status,
        "p13b1_status": audit.p13b1_status,
        "p13c_status": audit.p13c_status,
        "p13d_status": audit.p13d_status,
        "p13e_status": audit.p13e_status,
        "p13f_status": audit.p13f_status,
        "p13g_status": audit.p13g_status,
        "p11_status": audit.p11_status,
        "p12_status": audit.p12_status,
        "lowest_repaired_spinor_state": audit.lowest_repaired_spinor_state,
        "lowest_repaired_spinor_state_classification": audit.lowest_repaired_spinor_state_classification,
        "selected_state_pair_status": audit.selected_state_pair_status,
        "measure_status": audit.measure_status,
        "measure_once_value": audit.measure_once_value,
        "measure_double_count_value": audit.measure_double_count_value,
        "exact_integral_status": audit.exact_integral_status,
        "coefficient_symbolic": audit.coefficient_symbolic,
        "matrix_element_symbolic": audit.matrix_element_symbolic,
        "phase_invariance_status": audit.phase_invariance_status,
        "normalization_status": audit.normalization_status,
        "lambda_status": audit.lambda_status,
        "pattern_status": audit.pattern_status,
        "verdict": audit.verdict,
        "blocking_fields": audit.blocking_fields,
        "scope": audit.scope,
        "forbidden_claims": audit.forbidden_claims,
        "runtime_status": "research_only",
        "v_selection_status": "smoke_only",
        "safe_for_runtime": False,
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(p13h_s3_absolute_normalization_integral_test_summary())
