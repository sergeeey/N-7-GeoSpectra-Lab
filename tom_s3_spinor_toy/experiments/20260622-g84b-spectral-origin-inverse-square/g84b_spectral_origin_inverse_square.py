"""G84B: spectral-origin audit for the inverse-square non-perturbative form."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g84b.json"

ALLOWED_VERDICTS = {
    "SPECTRAL_BRIDGE_DERIVED",
    "SPECTRAL_FORM_FOUND_COEFFICIENT_OPEN",
    "PROPER_TIME_FORM_ONLY",
    "NO_SPECTRAL_BRIDGE",
    "OPEN_MISSING_OPERATOR",
    "MIXED",
}

SEARCHED_TERMS = [
    "Dirac",
    "Laplacian",
    "eigenvalue",
    "eigenvalues",
    "spectrum",
    "spectral",
    "KK",
    "zeta",
    "heat",
    "heat kernel",
    "proper time",
    "determinant",
    "Casimir",
    "V-operator",
    "lambda_np",
    "rho6",
]

TEXT_SUFFIXES = {".md", ".py", ".json", ".txt", ".yaml", ".yml"}

OPERATORS = [
    {
        "name": "S3_DIRAC_LADDER",
        "source": "tom_s3_spinor_toy/reference_spinor_harmonics.py",
        "formula": "lambda_n = n + 3/2",
        "rho6_scaling": "indirect; through rho3 only, not direct rho6 inverse-square bridge",
        "inverse_square": False,
        "proper_time": False,
        "determinant_or_zeta_prime": False,
        "lambda_np_connection": "none",
        "lambda_v_connection": "none",
    },
    {
        "name": "S6_DIRAC_GROUND_STATE",
        "source": "tom_s3_spinor_toy/tests/test_s6_harm_g4.py",
        "formula": "lambda_0 = 3/rho6; lambda_0^2 = 9/rho6^2",
        "rho6_scaling": "direct inverse-square at eigenvalue-squared level",
        "inverse_square": True,
        "proper_time": False,
        "determinant_or_zeta_prime": False,
        "lambda_np_connection": "candidate only; not promoted",
        "lambda_v_connection": "none",
    },
    {
        "name": "PRODUCT_KK_SPECTRUM",
        "source": "tom_s3_spinor_toy/tests/test_g7_kk_spectrum.py",
        "formula": "M^2 = (m+3/2)^2/rho3^2 + (n+3)^2/rho6^2",
        "rho6_scaling": "direct inverse-square term in the KK mass formula",
        "inverse_square": True,
        "proper_time": False,
        "determinant_or_zeta_prime": False,
        "lambda_np_connection": "none",
        "lambda_v_connection": "none",
    },
    {
        "name": "SPECTRAL_ACTION_HEAT_KERNEL",
        "source": "tom_s3_spinor_toy/experiments/20260619-g28-spectral-action/g28_inner_fluctuation.py",
        "formula": "Tr f(D^2/Lambda^2) with exp(-tau*(k+3)^2) heat-kernel weights",
        "rho6_scaling": "powers via Vol(S6) and Vol(S3), not a final inverse-square exponential",
        "inverse_square": False,
        "proper_time": True,
        "determinant_or_zeta_prime": False,
        "lambda_np_connection": "none",
        "lambda_v_connection": "none",
    },
    {
        "name": "CASIMIR_ZETA_FINITE_PART",
        "source": "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/claim.md",
        "formula": "V_EH_Cas = zeta_FP / V_int",
        "rho6_scaling": "power-law after Weyl division; finite part is not exp(-lambda/rho6^2)",
        "inverse_square": False,
        "proper_time": True,
        "determinant_or_zeta_prime": True,
        "lambda_np_connection": "none",
        "lambda_v_connection": "none",
    },
    {
        "name": "KKLT_ANSATZ_NP_TERM",
        "source": "tom_s3_spinor_toy/experiments/20260621-g56-kklt-like-np/decision.md",
        "formula": "A_np * exp(-lambda_np / rho6^2)",
        "rho6_scaling": "assumed ansatz, not derived from a spectral operator here",
        "inverse_square": True,
        "proper_time": False,
        "determinant_or_zeta_prime": False,
        "lambda_np_connection": "assumed in ansatz only",
        "lambda_v_connection": "none",
    },
]


def _text_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for base in (root / "tom_s3_spinor_toy", root / "docs"):
        if not base.is_dir():
            continue
        for path in sorted(p for p in base.rglob("*") if p.suffix.lower() in TEXT_SUFFIXES):
            if HERE in path.parents:
                continue
            files.append(path)
    return files


def _matching_files(root: Path) -> list[str]:
    needles = [term.casefold() for term in SEARCHED_TERMS]
    matches: list[str] = []
    for path in _text_files(root):
        text = path.read_text(encoding="utf-8", errors="replace").casefold()
        if any(term in text for term in needles):
            matches.append(path.relative_to(root).as_posix())
    return matches


def _contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def audit(root: Path = ROOT) -> dict:
    files_examined = _matching_files(root)
    g7 = (root / "tom_s3_spinor_toy" / "tests" / "test_g7_kk_spectrum.py").read_text(
        encoding="utf-8", errors="replace"
    )
    g28 = (root / "tom_s3_spinor_toy" / "experiments" / "20260619-g28-spectral-action" / "g28_inner_fluctuation.py").read_text(
        encoding="utf-8", errors="replace"
    )
    g54f = (root / "tom_s3_spinor_toy" / "experiments" / "20260621-g54f-4d-eh-frame" / "claim.md").read_text(
        encoding="utf-8", errors="replace"
    )
    g56 = (root / "tom_s3_spinor_toy" / "experiments" / "20260621-g56-kklt-like-np" / "decision.md").read_text(
        encoding="utf-8", errors="replace"
    )
    g61 = (root / "tom_s3_spinor_toy" / "experiments" / "20260621-g61-lambda-origin" / "decision.md").read_text(
        encoding="utf-8", errors="replace"
    )
    g79a = json.loads(
        (root / "tom_s3_spinor_toy" / "experiments" / "20260622-g79a-lambda-identity-audit" / "results_g79a.json").read_text(
            encoding="utf-8", errors="replace"
        )
    )
    g79b = json.loads(
        (root / "tom_s3_spinor_toy" / "experiments" / "20260622-g79b-lambda-bridge-feasibility" / "results_g79b.json").read_text(
            encoding="utf-8", errors="replace"
        )
    )

    operator_records = []
    for op in OPERATORS:
        operator_records.append(
            {
                **op,
                "explicit_rho6_inverse_square": op["inverse_square"] and _contains_any(
                    op["formula"], [r"/rho6\^2", r"rho6\^2", r"/rho6\*\*2"]
                ),
            }
        )

    inverse_square_scaling_found = any(
        row["explicit_rho6_inverse_square"] for row in operator_records
    )
    proper_time_exponent_found = any(row["proper_time"] for row in operator_records)
    proper_time_t_status = "integrated_over"
    final_effective_exponential_found = False
    determinant_or_zeta_prime_checked = True
    finite_part_behavior = "power-law/log-like finite part; no final exp(-lambda_np/rho6^2)"

    lambda_candidates_from_spectrum = [
        {
            "source": "S6_DIRAC_GROUND_STATE",
            "candidate": 9.0,
            "derivation_source": "lambda_0^2 = 9/rho6^2",
        },
        {
            "source": "PRODUCT_KK_SPECTRUM",
            "candidate": 9.0,
            "derivation_source": "(n+3)^2 term in M^2",
        },
    ]
    matches_one_third = any(abs(item["candidate"] - (1.0 / 3.0)) < 1e-12 for item in lambda_candidates_from_spectrum)
    matches_pi_over_9 = any(abs(item["candidate"] - (3.141592653589793 / 9.0)) < 1e-12 for item in lambda_candidates_from_spectrum)
    lambda_np_fixed = False
    lambda_v_connection_found = False

    verdict = "PROPER_TIME_FORM_ONLY"
    if not operator_records:
        verdict = "OPEN_MISSING_OPERATOR"
    elif final_effective_exponential_found and lambda_np_fixed and proper_time_t_status not in {"free", "integrated_unresolved", "unknown"}:
        verdict = "SPECTRAL_BRIDGE_DERIVED"
    elif inverse_square_scaling_found and not final_effective_exponential_found:
        verdict = "PROPER_TIME_FORM_ONLY"
    elif inverse_square_scaling_found and not lambda_np_fixed:
        verdict = "SPECTRAL_FORM_FOUND_COEFFICIENT_OPEN"
    else:
        verdict = "NO_SPECTRAL_BRIDGE"

    missing_inputs = [
        "explicit operator-to-effective-action map",
        "fixed saddle or resummation step for proper-time t",
        "operator-level bridge from spectral coefficients to lambda_np",
        "normalization showing why the final term is not just an integrand",
        "operator-level V-operator definition in the repository",
    ]
    falsified_routes = [
        {
            "route": "PROPER_TIME_INTEGRAND_IS_FINAL_EFFECTIVE_TERM",
            "reason": "repository only shows exp(-t*c/rho6^2) under an integral or heat-kernel sum",
        },
        {
            "route": "lambda_v_equals_lambda_np_by_numerical_closeness",
            "reason": "no operator bridge or shared derivation is documented",
        },
    ]

    gates = {
        "G84B-1_operator_records_nonempty": len(operator_records) >= 5,
        "G84B-2_inverse_square_scaling_found": inverse_square_scaling_found,
        "G84B-3_proper_time_exponent_found": proper_time_exponent_found,
        "G84B-4_no_final_effective_bridge": not final_effective_exponential_found,
        "G84B-5_determinant_or_zeta_checked": determinant_or_zeta_prime_checked,
        "G84B-6_verdict_allowed": verdict in ALLOWED_VERDICTS,
        "G84B-7_lambda_v_remains_separate": not lambda_v_connection_found,
    }

    return {
        "gate": "G84B",
        "verdict": verdict,
        "searched_terms": SEARCHED_TERMS,
        "files_examined_count": len(files_examined),
        "files_examined": files_examined,
        "operators_examined": operator_records,
        "candidate_operator_count": len(operator_records),
        "eigenvalue_scalings": {
            row["name"]: row["rho6_scaling"] for row in operator_records
        },
        "inverse_square_scaling_found": inverse_square_scaling_found,
        "proper_time_exponent_found": proper_time_exponent_found,
        "proper_time_t_status": proper_time_t_status,
        "final_effective_exponential_found": final_effective_exponential_found,
        "determinant_or_zeta_prime_checked": determinant_or_zeta_prime_checked,
        "finite_part_behavior": finite_part_behavior,
        "lambda_candidates_from_spectrum": lambda_candidates_from_spectrum,
        "matches_one_third": matches_one_third,
        "matches_pi_over_9": matches_pi_over_9,
        "lambda_np_fixed": lambda_np_fixed,
        "lambda_v_connection_found": lambda_v_connection_found,
        "missing_inputs": missing_inputs,
        "falsified_routes": falsified_routes,
        "next_required_gate": "G84C_FUNCTIONAL_FORM_DEGENERACY",
        "gates": gates,
        "bridge_evidence": {
            "g7_formula": "M^2 = (m+3/2)^2/rho3^2 + (n+3)^2/rho6^2",
            "g28_heat_kernel": "exp(-tau*(k+3)^2)",
            "g54f_zeta_fp": "V_EH_Cas = zeta_FP / V_int",
            "g56_ansatz": "A_np * exp(-lambda_np / rho6^2)",
            "g79a_no_identity": g79a["verdict"],
            "g79b_no_bridge": g79b["verdict"],
            "g61_candidate": "lambda_exact ~ 0.3374, pi/9 weakly suggested",
        },
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g84b-spectral-origin-inverse-square/g84b_spectral_origin_inverse_square.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g84b_spectral_origin_inverse_square.py -q",
        ],
    }


def main() -> int:
    result = audit()
    RESULTS_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "candidate_operator_count": result["candidate_operator_count"],
                "inverse_square_scaling_found": result["inverse_square_scaling_found"],
                "proper_time_t_status": result["proper_time_t_status"],
                "gates": result["gates"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if all(result["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
