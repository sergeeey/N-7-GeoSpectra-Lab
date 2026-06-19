"""P13H — explicit low-mode S3 normalization integral test."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

import numpy as np

from cc_toy_lab.compactification.convention_registry import Classification
from cc_toy_lab.compactification.p11_p12_pattern import p12_scale_class, pattern_compatible
from cc_toy_lab.compactification.p13b1_basis import (
    ConventionId,
    load_modes,
    normalize_spinor,
    primary_pair_indices,
)
from cc_toy_lab.compactification.p13d_conventions import (
    assert_hermiticity_preservation,
    gamma_matrices,
    su4_generators_smoke,
)
from cc_toy_lab.compactification.p13_fixed_inputs import assert_p13_chain_fixed
from cc_toy_lab.compactification.registry_loader import assert_frozen_registry_present
from cc_toy_lab.compactification.s3_lawrence_hopf import (
    VOLUME_DOC,
    ben_achour_E_i,
    ben_achour_E_prime_i,
    volume_weight,
)

ConventionId = Literal["CONV_HAAR_UNIT", "CONV_HAAR_HARMONIC_SQRT2"]


@dataclass(frozen=True)
class IntegralResult:
    i: int
    j: int
    convention: ConventionId
    matrix_element: complex
    coefficient: complex
    lambda_factor: float


@dataclass(frozen=True)
class P13HReport:
    gate_id: str
    volume_element: str
    hermiticity_max_error: float
    primary_pair: tuple[int, int]
    primary_coefficient: complex
    primary_matrix_element: complex
    p11_pattern_compatible: bool
    coeff_11_unit: complex
    coeff_11_sqrt2: complex
    convention_invariant_for_diagonal_11: bool
    classification: Classification
    lambda_role: str
    p13e_status_preserved: bool
    runtime: str
    safe_for_runtime: bool
    selection_rules: str
    promotion: str
    details: dict


def _integration_grid(n: int = 12) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    alpha = np.linspace(1e-3, 0.5 * np.pi - 1e-3, n)
    theta = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    theta_tilde = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    return alpha, theta, theta_tilde


def _A_field(
    I: int,
    alpha: np.ndarray,
    theta: np.ndarray,
    theta_tilde: np.ndarray,
) -> np.ndarray:
    """P13C map: I=0 -> E_i, I=1 -> E'_i components contracted with gamma index."""
    if I == 0:
        emb = ben_achour_E_i(alpha, theta, theta_tilde)
    elif I == 1:
        emb = ben_achour_E_prime_i(alpha, theta, theta_tilde)
    else:
        raise ValueError(f"Smoke truncation supports I in {{0,1}}, got {I}")
    return emb  # shape (4, n) for gamma index a


def matrix_element(
    i: int,
    j: int,
    convention: ConventionId,
    *,
    grid_n: int = 12,
) -> IntegralResult:
    """Compute <psi_i| V_S3 |psi_j> = lambda * coefficient."""
    assert_p13_chain_fixed()
    assert_frozen_registry_present()
    modes = load_modes()
    mode_i = modes[i]
    mode_j = modes[j]
    alpha, theta, theta_tilde = _integration_grid(grid_n)

    aa, tt, ttt = np.meshgrid(alpha, theta, theta_tilde, indexing="ij")
    alpha_f = aa.ravel()
    theta_f = tt.ravel()
    theta_tilde_f = ttt.ravel()

    psi_i, _ = normalize_spinor(mode_i, alpha_f, theta_f, theta_tilde_f, convention)
    psi_j, _ = normalize_spinor(mode_j, alpha_f, theta_f, theta_tilde_f, convention)

    gammas = gamma_matrices()
    generators = su4_generators_smoke()

    w = volume_weight(alpha_f)
    dalpha = (0.5 * np.pi) / max(grid_n - 1, 1)
    dtheta = (2.0 * np.pi) / grid_n
    dtheta_tilde = (2.0 * np.pi) / grid_n
    weight = w * dalpha * dtheta * dtheta_tilde

    integral = 0.0 + 0.0j
    for a, gamma_a in enumerate(gammas):
        for I, T_I in enumerate(generators):
            A = _A_field(I, alpha_f, theta_f, theta_tilde_f)[a]
            for p in range(alpha_f.size):
                val = (
                    np.vdot(psi_i[:, p], gamma_a @ (T_I @ psi_j[:, p]))
                    * A[p]
                    * weight[p]
                )
                integral += val

    coeff = integral  # matrix_element = lambda * coeff
    return IntegralResult(
        i=i,
        j=j,
        convention=convention,
        matrix_element=integral,
        coefficient=coeff,
        lambda_factor=1.0,
    )


def hermiticity_check_primary_pair(
    convention: ConventionId = "CONV_HAAR_UNIT",
    *,
    grid_n: int = 12,
) -> float:
    """|M_ij - conj(M_ji)| for primary pair — should be ~0."""
    i, j = primary_pair_indices()
    m_ij = matrix_element(i, j, convention, grid_n=grid_n).matrix_element
    m_ji = matrix_element(j, i, convention, grid_n=grid_n).matrix_element
    return float(abs(m_ij - np.conj(m_ji)))


def run_p13h_integral_test(*, grid_n: int = 24) -> P13HReport:
    assert_p13_chain_fixed()
    assert_frozen_registry_present()
    herm_gamma = assert_hermiticity_preservation()
    i, j = primary_pair_indices()

    primary_unit = matrix_element(i, j, "CONV_HAAR_UNIT", grid_n=grid_n)
    primary_sqrt2 = matrix_element(i, j, "CONV_HAAR_HARMONIC_SQRT2", grid_n=grid_n)

    d11_unit = matrix_element(1, 1, "CONV_HAAR_UNIT", grid_n=grid_n).coefficient
    d11_sqrt2 = matrix_element(1, 1, "CONV_HAAR_HARMONIC_SQRT2", grid_n=grid_n).coefficient

    herm_pair = hermiticity_check_primary_pair("CONV_HAAR_UNIT", grid_n=grid_n)

    p11_ok = pattern_compatible(i, j, abs(primary_unit.coefficient))
    denom = max(abs(d11_unit), abs(d11_sqrt2), 1e-15)
    rel_diag = float(abs(d11_sqrt2 - d11_unit) / denom)
    conv_inv_diag = rel_diag < 0.05 and denom > 1e-9

    classification = _classify(
        p11_ok=p11_ok,
        primary_abs=abs(primary_unit.coefficient),
        conv_inv_diag=conv_inv_diag,
        rel_diag=rel_diag,
        herm_pair=herm_pair,
    )

    return P13HReport(
        gate_id="P13H",
        volume_element=VOLUME_DOC,
        hermiticity_max_error=max(herm_gamma, herm_pair),
        primary_pair=(i, j),
        primary_coefficient=primary_unit.coefficient,
        primary_matrix_element=primary_unit.matrix_element,
        p11_pattern_compatible=p11_ok,
        coeff_11_unit=d11_unit,
        coeff_11_sqrt2=d11_sqrt2,
        convention_invariant_for_diagonal_11=conv_inv_diag,
        classification=classification,
        lambda_role="FREE_COUPLING_PARAMETER",
        p13e_status_preserved=True,
        runtime="research_only",
        safe_for_runtime=False,
        selection_rules="smoke_only",
        promotion="forbidden_without_separate_gate",
        details={
            "primary_sqrt2_coeff": complex(primary_sqrt2.coefficient),
            "p12_scale_class_primary": p12_scale_class(i, j),
            "p12_scale_class_11": p12_scale_class(1, 1),
            "relative_diagonal_11_change": rel_diag,
            "grid_n": grid_n,
        },
    )


def _classify(
    *,
    p11_ok: bool,
    primary_abs: float,
    conv_inv_diag: bool,
    rel_diag: float,
    herm_pair: float,
) -> Classification:
    if herm_pair > 1e-6:
        return Classification.FAILED
    if not p11_ok:
        return Classification.INCONCLUSIVE
    # Diagonal (1,1) convention dependence → P13E NO_GO preserved
    if not conv_inv_diag and rel_diag > 0.05:
        return Classification.NORMALIZATION_DEPENDENT_NO_GO
    # Off-diagonal zero: lambda cannot be fixed from this element (P12 scale)
    if primary_abs < 1e-10:
        return Classification.FREE_COUPLING_PARAMETER_CONFIRMED
    return Classification.NORMALIZATION_DEPENDENT_NO_GO


def _json_complex(z: complex) -> dict[str, float]:
    return {"re": float(z.real), "im": float(z.imag)}


def report_to_dict(report: P13HReport) -> dict:
    d = asdict(report)
    d["classification"] = report.classification.value
    d["primary_coefficient"] = _json_complex(report.primary_coefficient)
    d["primary_matrix_element"] = _json_complex(report.primary_matrix_element)
    d["coeff_11_unit"] = _json_complex(report.coeff_11_unit)
    d["coeff_11_sqrt2"] = _json_complex(report.coeff_11_sqrt2)
    details = dict(d["details"])
    if "primary_sqrt2_coeff" in details:
        details["primary_sqrt2_coeff"] = _json_complex(complex(details["primary_sqrt2_coeff"]))
    details["relative_diagonal_11_change"] = float(details["relative_diagonal_11_change"])
    details["grid_n"] = int(details["grid_n"])
    d["details"] = details
    d["p13e_status_preserved"] = bool(d["p13e_status_preserved"])
    d["safe_for_runtime"] = bool(d["safe_for_runtime"])
    d["convention_invariant_for_diagonal_11"] = bool(d["convention_invariant_for_diagonal_11"])
    d["p11_pattern_compatible"] = bool(d["p11_pattern_compatible"])
    return d
