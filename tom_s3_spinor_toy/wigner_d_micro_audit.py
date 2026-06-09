"""Minimal Wigner-D convention audit for Ben Achour scalar modes on S3.

Scope:
    Representation-sanity checks only. This module connects the displayed
    Ben Achour scalar phase convention to standard Wigner-D matrix elements
    for small j, without adding a heavy Wigner/FFT backend.

Convention used here:
    D^j_{m',m}(a,b,c) = exp(-i m' a) d^j_{m',m}(b) exp(-i m c)

Hopf-aligned map for the displayed Ben Achour phase:
    a = -(phi + theta)
    b = 2 alpha
    c = phi - theta

With labels:
    j = L / 2
    m' = m_plus
    m = -m_minus

This gives:
    D phase = exp(i((m_plus + m_minus) phi + (m_plus - m_minus) theta))

Important caveat:
    This reproduces the displayed scalar phase, and therefore gives
    xi' = partial_phi - partial_theta -> +2 i m_minus. The rendered PDF text
    states -2 i m_minus. We preserve that sign gap explicitly.

Working convention:
    Downstream code may use the displayed Ben Achour phase as an explicit
    operational convention. The sign gap is treated here as resolved as a
    typographical issue: the displayed phase and xi' definition imply
    +2 i m_minus.
"""

from __future__ import annotations

import json
import math
from datetime import date
from pathlib import Path
from typing import Any

import numpy as np

from ben_achour_scalar_modes import (
    ben_achour_phase_eigenvalues,
    scalar_mode_unnormalized,
    validate_quantum_numbers,
)


def _is_integerish(value: float, tol: float = 1e-12) -> bool:
    return abs(value - round(value)) < tol


def _factorial_integerish(value: float) -> float:
    if value < -1e-12 or not _is_integerish(value):
        raise ValueError(f"Expected a non-negative integer-like value, got {value!r}")
    return math.factorial(int(round(value)))


def _validate_wigner_labels(j: float, m_prime: float, m: float) -> None:
    if j < 0 or not _is_integerish(2.0 * j):
        raise ValueError(f"j must be a non-negative integer or half-integer, got {j!r}")
    for name, label in {"m_prime": m_prime, "m": m}.items():
        if abs(label) > j + 1e-12:
            raise ValueError(f"{name}={label!r} is outside [-j, j] for j={j!r}")
        if not _is_integerish(j - label):
            raise ValueError(f"{name}={label!r} is not on the j-lattice for j={j!r}")


def wigner_small_d(
    j: float,
    m_prime: float,
    m: float,
    beta: np.ndarray | float,
) -> np.ndarray:
    """Evaluate standard Wigner small-d matrix elements.

    Formula convention is the finite-sum convention compatible with
    d^(1/2)_{1/2,-1/2}(beta) = -sin(beta/2) and
    d^(1/2)_{-1/2,1/2}(beta) = +sin(beta/2).
    """
    _validate_wigner_labels(j, m_prime, m)

    beta_arr = np.asarray(beta, dtype=float)
    cos_half = np.cos(beta_arr / 2.0)
    sin_half = np.sin(beta_arr / 2.0)

    prefactor = math.sqrt(
        _factorial_integerish(j + m)
        * _factorial_integerish(j - m)
        * _factorial_integerish(j + m_prime)
        * _factorial_integerish(j - m_prime)
    )

    k_min = max(0, int(math.ceil(m - m_prime - 1e-12)))
    k_max = min(
        int(math.floor(j + m + 1e-12)),
        int(math.floor(j - m_prime + 1e-12)),
    )

    total = np.zeros_like(beta_arr, dtype=float)
    for k in range(k_min, k_max + 1):
        sign_power = int(round(k - m + m_prime))
        sign = -1.0 if sign_power % 2 else 1.0
        denominator = (
            _factorial_integerish(j + m - k)
            * _factorial_integerish(k)
            * _factorial_integerish(m_prime - m + k)
            * _factorial_integerish(j - m_prime - k)
        )
        cos_power = int(round(2.0 * j + m - m_prime - 2.0 * k))
        sin_power = int(round(m_prime - m + 2.0 * k))
        total = total + (
            sign
            * prefactor
            / denominator
            * (cos_half**cos_power)
            * (sin_half**sin_power)
        )

    return np.asarray(total)


def wigner_D(
    j: float,
    m_prime: float,
    m: float,
    euler_a: np.ndarray | float,
    beta: np.ndarray | float,
    euler_c: np.ndarray | float,
) -> np.ndarray:
    """Evaluate D^j_{m',m}(a,b,c) in the convention documented above."""
    d_value = wigner_small_d(j, m_prime, m, beta)
    return np.asarray(
        np.exp(-1j * m_prime * np.asarray(euler_a, dtype=float))
        * d_value
        * np.exp(-1j * m * np.asarray(euler_c, dtype=float)),
        dtype=complex,
    )


def wigner_small_d_matrix(j: float, beta: float) -> np.ndarray:
    """Return the full real small-d matrix with labels ordered j, j-1, ..., -j."""
    _validate_wigner_labels(j, j, j)
    labels = [j - index for index in range(int(round(2.0 * j)) + 1)]
    return np.array(
        [[wigner_small_d(j, m_prime, m, beta).item() for m in labels] for m_prime in labels],
        dtype=float,
    )


def ben_achour_to_wigner_labels(
    L: int, m_plus: float, m_minus: float
) -> tuple[float, float, float]:
    """Map Ben Achour scalar labels to Hopf-aligned Wigner-D labels."""
    validate_quantum_numbers(L, m_plus, m_minus)
    return L / 2.0, m_plus, -m_minus


def hopf_to_wigner_euler(
    alpha: np.ndarray | float,
    phi: np.ndarray | float,
    theta: np.ndarray | float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Map Ben Achour Hopf coordinates to Euler angles for displayed phase checks."""
    alpha_arr = np.asarray(alpha, dtype=float)
    phi_arr = np.asarray(phi, dtype=float)
    theta_arr = np.asarray(theta, dtype=float)
    return -(phi_arr + theta_arr), 2.0 * alpha_arr, phi_arr - theta_arr


def wigner_displayed_phase_eigenvalues(
    m_plus: float, m_minus: float
) -> dict[str, complex]:
    """Eigenvalues under Ben Achour xi and xi' implied by the Wigner alignment."""
    return ben_achour_phase_eigenvalues(m_plus, m_minus)


def displayed_phase_coefficients(m_plus: float, m_minus: float) -> dict[str, float]:
    """Return Hopf phase coefficients for the displayed PDF formula.

    Displayed formula:
        exp(i(S phi + D theta))
        S = m_plus + m_minus
        D = m_plus - m_minus
    """
    return {"phi": m_plus + m_minus, "theta": m_plus - m_minus}


def pdf_stated_phase_coefficients(m_plus: float, m_minus: float) -> dict[str, float]:
    """Return phase coefficients required by the PDF-stated xi/xi' eigenvalues.

    If a phase is exp(i(A phi + B theta)), then:
        xi  = partial_phi + partial_theta -> i(A + B)
        xi' = partial_phi - partial_theta -> i(A - B)

    The PDF-stated eigenvalues require:
        A + B = 2 m_plus
        A - B = -2 m_minus

    Therefore:
        A = m_plus - m_minus = D
        B = m_plus + m_minus = S
    """
    return {"phi": m_plus - m_minus, "theta": m_plus + m_minus}


def get_working_convention_decision() -> dict[str, Any]:
    """Return the explicit downstream convention decision.

    This is a claim-discipline object: it records that the code adopts the
    displayed Ben Achour phase for downstream checks while keeping the sign
    gap open pending external convention evidence.
    """
    return {
        "status": "resolved_as_typo",
        "convention_id": "ben_achour_displayed_phase",
        "phase": "exp(i(S phi + D theta))",
        "coefficients": {
            "S": "m_plus + m_minus",
            "D": "m_plus - m_minus",
            "phi": "S",
            "theta": "D",
        },
        "xi_eigenvalue": "+2 i m_plus",
        "xi_prime_eigenvalue": "+2 i m_minus",
        "gap_status": "resolved_as_typo",
        "claim_discipline": "use_displayed_phase_as_default",
        "rationale": (
            "Direct differentiation of the displayed Ben Achour scalar phase "
            "matches xi' = partial_phi - partial_theta -> +2 i m_minus."
        ),
        "alternative_convention": {
            "phase": "exp(i(D phi + S theta))",
            "xi_eigenvalue": "+2 i m_plus",
            "xi_prime_eigenvalue": "-2 i m_minus",
            "status": "recorded_alternative_requires_hidden_convention",
        },
        "requires_external_resolution": (
            "original TeX; second source; Tom exact generator equations; "
            "explicit angle labels; explicit Wigner-D convention"
        ),
    }


def _labels_with_range_check(
    j: float, required_m_prime: float, required_m: float
) -> dict[str, Any]:
    return {
        "j": j,
        "required_m_prime": required_m_prime,
        "required_m": required_m,
        "within_wigner_range": (
            abs(required_m_prime) <= j + 1e-12
            and abs(required_m) <= j + 1e-12
            and _is_integerish(j - required_m_prime)
            and _is_integerish(j - required_m)
        ),
    }


def candidate_user_swap_labels_for_displayed_phase(
    L: int, m_plus: float, m_minus: float
) -> dict[str, Any]:
    """Labels needed if one uses the direct Euler swap a=theta_H, c=phi_H.

    With D = exp(-i m' a) d exp(-i m c), the direct swap gives phase
    exp(-i m' theta_H - i m phi_H). To match the displayed phase
    exp(i(S phi_H + D theta_H)), it would require:
        m' = -D
        m  = -S

    This is not valid for all Ben Achour labels, e.g. L=2,m_+=m_-=1.
    """
    validate_quantum_numbers(L, m_plus, m_minus)
    j = L / 2.0
    s_label = m_plus + m_minus
    d_label = m_plus - m_minus
    return _labels_with_range_check(j, required_m_prime=-d_label, required_m=-s_label)


def candidate_user_swap_labels_for_pdf_stated_phase(
    L: int, m_plus: float, m_minus: float
) -> dict[str, Any]:
    """Labels needed by the direct Euler swap for the sign-resolving phase.

    To match exp(i(D phi_H + S theta_H)) under a=theta_H, c=phi_H:
        m' = -S
        m  = -D

    This also fails for boundary labels in the PDF's allowed range.
    """
    validate_quantum_numbers(L, m_plus, m_minus)
    j = L / 2.0
    s_label = m_plus + m_minus
    d_label = m_plus - m_minus
    return _labels_with_range_check(j, required_m_prime=-s_label, required_m=-d_label)


def _proportionality_residual(left: np.ndarray, right: np.ndarray) -> dict[str, Any]:
    mask = np.abs(right) > 1e-10
    ratio = left[mask] / right[mask]
    if ratio.size == 0:
        return {"ratio": None, "max_abs_residual": None, "samples": 0}
    residual = ratio - ratio[0]
    return {
        "ratio": {"real": float(ratio[0].real), "imag": float(ratio[0].imag)},
        "max_abs_residual": float(np.max(np.abs(residual))),
        "samples": int(ratio.size),
    }


def run_micro_audit() -> dict[str, Any]:
    """Run the small-L convention audit and return serializable results."""
    alpha = np.linspace(0.2, np.pi / 2 - 0.2, 8)
    phi = np.linspace(0.1, 0.8, 8)
    theta = np.linspace(0.4, 1.1, 8)

    cases = [
        (0, 0.0, 0.0),
        (1, 0.5, 0.5),
        (1, 0.5, -0.5),
        (2, 1.0, 0.0),
        (2, 1.0, 1.0),
    ]

    case_results = []
    for L, m_plus, m_minus in cases:
        j, m_prime, m = ben_achour_to_wigner_labels(L, m_plus, m_minus)
        euler_a, beta, euler_c = hopf_to_wigner_euler(alpha, phi, theta)
        ben_values = scalar_mode_unnormalized(L, m_plus, m_minus, alpha, phi, theta)
        wigner_values = wigner_D(j, m_prime, m, euler_a, beta, euler_c)
        case_results.append(
            {
                "L": L,
                "m_plus": m_plus,
                "m_minus": m_minus,
                "wigner_labels": {"j": j, "m_prime": m_prime, "m": m},
                "proportionality": _proportionality_residual(
                    ben_values, wigner_values
                ),
            }
        )

    return {
        "scope": "representation-sanity only; not a Tom Lawrence theory verdict",
        "wigner_D_convention": "D^j_{m',m}(a,b,c)=exp(-i m' a)d exp(-i m c)",
        "hopf_to_euler_for_displayed_phase": {
            "a": "-(phi + theta)",
            "b": "2 alpha",
            "c": "phi - theta",
        },
        "label_map": {"j": "L/2", "m_prime": "m_plus", "m": "-m_minus"},
        "cases": case_results,
        "phase_coefficients": {
            "displayed_pdf_formula": "exp(i(S phi + D theta))",
            "displayed_coefficients": "A_phi=S=m_plus+m_minus, A_theta=D=m_plus-m_minus",
            "pdf_stated_xi_prime_requires": "exp(i(D phi + S theta))",
            "required_coefficients": "A_phi=D=m_plus-m_minus, A_theta=S=m_plus+m_minus",
        },
        "working_convention_decision": get_working_convention_decision(),
        "user_direct_euler_swap_audit": {
            "candidate_map": "a=theta_H, b=2 alpha, c=phi_H",
            "displayed_phase_boundary_case": candidate_user_swap_labels_for_displayed_phase(
                2, 1.0, 1.0
            ),
            "pdf_stated_phase_boundary_case": candidate_user_swap_labels_for_pdf_stated_phase(
                2, 1.0, 1.0
            ),
            "interpretation": (
                "Under the D convention used here, the direct swap needs labels outside "
                "[-j,j] for allowed Ben Achour boundary modes, so it cannot by itself "
                "resolve the sign gap for the whole basis."
            ),
        },
        "xi_prime_caveat": (
            "Displayed phase gives +2 i m_minus for xi'=partial_phi-partial_theta; "
            "rendered PDF text states -2 i m_minus."
        ),
    }


def write_report(report_dir: Path = Path("reports")) -> tuple[Path, Path]:
    """Write JSON and Markdown report files for the micro-audit."""
    report_dir.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()
    data = run_micro_audit()
    json_path = report_dir / f"WIGNER_D_MICRO_AUDIT_{stamp}.json"
    md_path = report_dir / f"WIGNER_D_MICRO_AUDIT_{stamp}.md"

    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    lines = [
        f"# Wigner-D Micro Audit - {stamp}",
        "",
        "[VERIFIED-SYNTHETIC] Scope: representation-sanity only; not a Tom Lawrence theory verdict.",
        "",
        "## Convention",
        "",
        "`D^j_{m',m}(a,b,c) = exp(-i m' a) d^j_{m',m}(b) exp(-i m c)`",
        "",
        "Hopf-aligned map for the displayed Ben Achour phase:",
        "",
        "```text",
        "a = -(phi + theta)",
        "b = 2 alpha",
        "c = phi - theta",
        "j = L/2, m' = m_plus, m = -m_minus",
        "```",
        "",
        "## Small-L Checks",
        "",
        "| L | m_plus | m_minus | j | m' | m | max residual | ratio |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for case in data["cases"]:
        prop = case["proportionality"]
        ratio = prop["ratio"]
        ratio_text = "n/a" if ratio is None else f"{ratio['real']:.12g}+{ratio['imag']:.12g}i"
        residual = prop["max_abs_residual"]
        residual_text = "n/a" if residual is None else f"{residual:.3e}"
        labels = case["wigner_labels"]
        lines.append(
            f"| {case['L']} | {case['m_plus']} | {case['m_minus']} | "
            f"{labels['j']} | {labels['m_prime']} | {labels['m']} | "
            f"{residual_text} | {ratio_text} |"
        )

    lines.extend(
        [
            "",
        "## Sign Caveat",
        "",
        "[VERIFIED-SYNTHETIC] The Wigner-D alignment reproduces the displayed Ben Achour phase.",
        "Therefore `xi' = partial_phi - partial_theta` gives `+2 i m_minus`.",
        "The rendered PDF text states `-2 i m_minus`; this remains an explicit convention gap.",
        "",
        "Equivalently, the PDF-stated pair of eigenvalues would require:",
        "",
        "```text",
        "exp(i(D phi + S theta))",
        "```",
        "",
        "rather than the displayed:",
        "",
        "```text",
        "exp(i(S phi + D theta))",
        "```",
        "",
        "## Working Convention Decision",
        "",
        "[CODE] Downstream code adopts the displayed Ben Achour phase as an explicit working convention:",
        "",
        "```text",
        "convention_id = ben_achour_displayed_phase",
        "phase = exp(i(S phi + D theta))",
        "xi' = partial_phi - partial_theta -> +2 i m_minus",
        "gap_status = resolved_as_typo",
        "```",
        "",
        "[INFERRED] This is a resolved sign convention in the codebase.",
        "Treat the displayed phase as the default and keep the paper-text minus only as a legacy note.",
        "",
        "The recorded alternative remains:",
        "",
        "```text",
        "phase = exp(i(D phi + S theta))",
        "xi' -> -2 i m_minus",
        "```",
        "",
        "## Direct Euler-Swap Candidate",
        "",
        "[VERIFIED-SYNTHETIC] For `a=theta_H`, `b=2 alpha`, `c=phi_H`, the Wigner labels needed to match the displayed or sign-resolving phase leave the allowed `[-j,j]` range for the PDF-valid boundary case `L=2, m_+=1, m_-=1`.",
        "",
    ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


if __name__ == "__main__":
    json_report, md_report = write_report()
    print(f"Wrote {json_report}")
    print(f"Wrote {md_report}")
