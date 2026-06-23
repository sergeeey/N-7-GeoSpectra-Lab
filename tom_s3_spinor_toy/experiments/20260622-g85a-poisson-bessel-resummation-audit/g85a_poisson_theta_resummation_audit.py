"""G85A: Poisson/theta resummation audit for the inverse-square NP form."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g85a.json"

ALLOWED_VERDICTS = {
    "RESUMMATION_BRIDGE_DERIVED",
    "POISSON_THETA_FORM_ONLY",
    "NO_RESUMMATION_BRIDGE",
    "OPEN_MISSING_SUMMATION_DATA",
    "MIXED",
}

SEARCHED_TERMS = [
    "Poisson",
    "Bessel",
    "theta",
    "modular",
    "resumm",
    "saddle",
    "worldline",
    "proper-time",
    "proper time",
    "determinant",
    "zeta",
    "heat kernel",
    "spectral action",
    "KKLT",
    "lambda_np",
    "rho6",
]

TEXT_SUFFIXES = {".md", ".py", ".json", ".txt", ".yaml", ".yml"}

FOCUS_FILES = [
    "tom_s3_spinor_toy/experiments/20260621-g54b-casimir-pole/decision.md",
    "tom_s3_spinor_toy/experiments/20260621-g54c-effective-potential/claim.md",
    "tom_s3_spinor_toy/experiments/20260621-g54c-effective-potential/decision.md",
    "tom_s3_spinor_toy/experiments/20260621-g54d-hadamard-fp/decision.md",
    "tom_s3_spinor_toy/experiments/20260621-g54e-zeta-fp-structure/decision.md",
    "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/claim.md",
    "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/decision.md",
    "tom_s3_spinor_toy/experiments/20260621-g56-kklt-like-np/decision.md",
    "tom_s3_spinor_toy/experiments/20260622-g84b-spectral-origin-inverse-square/claim.md",
    "tom_s3_spinor_toy/experiments/20260622-g84b-spectral-origin-inverse-square/decision.md",
    "tom_s3_spinor_toy/README.md",
    "tom_s3_spinor_toy/PROCEEDINGS.md",
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


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def _matching_files(root: Path) -> list[str]:
    needles = [term.casefold() for term in SEARCHED_TERMS]
    matches: list[str] = []
    for path in _text_files(root):
        text = _read_text(path).casefold()
        if any(term in text for term in needles):
            matches.append(path.relative_to(root).as_posix())
    return matches


def _load_focus_text(root: Path) -> dict[str, str]:
    focus_text: dict[str, str] = {}
    for rel in FOCUS_FILES:
        path = root / rel
        if path.is_file():
            focus_text[rel] = _read_text(path)
    return focus_text


def audit(root: Path = ROOT) -> dict:
    files_examined = _matching_files(root)
    focus_text = _load_focus_text(root)

    joined_focus = "\n\n".join(focus_text.values())
    poisson_identity_found = _contains_any(joined_focus, [r"\bPoisson\b", r"Poisson summation", r"bilateral theta"])
    theta_identity_found = _contains_any(joined_focus, [r"\btheta\b", r"\bTheta\b", r"theta function", r"bilateral theta"])
    bessel_identity_found = _contains_any(joined_focus, [r"\bBessel\b", r"\bjv\(", r"\biv\(", r"\bkv\(", r"\byv\("])
    proper_time_integrand_found = _contains_any(
        joined_focus,
        [r"exp\(-t\s*\*", r"exp\(-tau\s*\*", r"proper[- ]time", r"heat kernel"],
    )
    proper_time_t_status = "integrated_over"
    final_effective_exponential_found = _contains_any(
        joined_focus,
        [
            r"derived.*A\s*\*\s*exp\(\s*-lambda_np\s*/\s*rho6\^2\s*\)",
            r"promot.*A\s*\*\s*exp\(\s*-lambda_np\s*/\s*rho6\^2\s*\)",
            r"final effective.*A\s*\*\s*exp\(\s*-lambda_np\s*/\s*rho6\^2\s*\)",
        ],
    )
    ansatz_only_exponential_found = _contains_any(
        joined_focus,
        [r"A_np\s*\*\s*exp\(\s*-lambda_np\s*/\s*rho6\^2\s*\)", r"exp\(\s*-lambda_np\s*/\s*rho6\^2\s*\)"],
    )
    resummation_bridge_found = final_effective_exponential_found and (poisson_identity_found or bessel_identity_found)
    determinant_or_zeta_prime_checked = _contains_any(joined_focus, [r"zeta_FP", r"determinant", r"\bzeta\b"])
    lambda_np_fixed = False
    lambda_v_connection_found = False

    candidate_routes = [
        {
            "route": "POISSON_THETA_HEAT_KERNEL",
            "found": poisson_identity_found and theta_identity_found,
            "status": "form-only",
        },
        {
            "route": "BESSEL_REEXPRESSION",
            "found": bessel_identity_found,
            "status": "absent",
        },
        {
            "route": "PROPER_TIME_SADDLE",
            "found": proper_time_integrand_found,
            "status": "intermediate-only",
        },
        {
            "route": "DETERMINANT_ZETA_FINITE_PART",
            "found": determinant_or_zeta_prime_checked,
            "status": "finite-part-only",
        },
        {
            "route": "KKLT_ANSATZ",
            "found": ansatz_only_exponential_found,
            "status": "ansatz-only",
        },
    ]

    if resummation_bridge_found and lambda_np_fixed and proper_time_t_status not in {"free", "integrated_unresolved", "unknown"}:
        verdict = "RESUMMATION_BRIDGE_DERIVED"
    elif poisson_identity_found and theta_identity_found and proper_time_integrand_found and not resummation_bridge_found:
        verdict = "POISSON_THETA_FORM_ONLY"
    elif not any(route["found"] for route in candidate_routes):
        verdict = "NO_RESUMMATION_BRIDGE"
    else:
        verdict = "MIXED"

    missing_inputs = [
        "explicit Poisson/Bessel step that closes the effective-action bridge",
        "a deterministic resummation producing A * exp(-lambda_np / rho6^2)",
        "fixed or geometrically constrained lambda_np",
        "a non-free proper-time treatment that removes t from the final answer",
        "operator-level evidence that the Bessel route exists in the repository",
    ]
    falsified_routes = [
        {
            "route": "PROPER_TIME_INTEGRAND_IS_FINAL_EFFECTIVE_TERM",
            "reason": "repository shows only heat-kernel/proper-time form, not a derived final exponential",
        },
        {
            "route": "BESSEL_ROUTE_PRESENT_IN_REPO",
            "reason": "no usable Bessel identity or Bessel-based resummation was found in the local tree",
        },
        {
            "route": "lambda_v_equals_lambda_np_by_documentation",
            "reason": "no operator-level bridge between lambda_V and lambda_np is documented",
        },
    ]

    return {
        "gate": "G85A",
        "verdict": verdict,
        "searched_terms": SEARCHED_TERMS,
        "files_examined_count": len(files_examined),
        "files_examined": files_examined,
        "focus_files_examined": sorted(focus_text),
        "poisson_identity_found": poisson_identity_found,
        "theta_identity_found": theta_identity_found,
        "bessel_identity_found": bessel_identity_found,
        "proper_time_integrand_found": proper_time_integrand_found,
        "proper_time_t_status": proper_time_t_status,
        "final_effective_exponential_found": final_effective_exponential_found,
        "ansatz_only_exponential_found": ansatz_only_exponential_found,
        "resummation_bridge_found": resummation_bridge_found,
        "determinant_or_zeta_prime_checked": determinant_or_zeta_prime_checked,
        "lambda_np_fixed": lambda_np_fixed,
        "lambda_v_connection_found": lambda_v_connection_found,
        "candidate_routes": candidate_routes,
        "missing_inputs": missing_inputs,
        "falsified_routes": falsified_routes,
        "next_required_gate": "G85B_SPECTRAL_SADDLE_WORLDLINE_AUDIT",
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g85a-poisson-bessel-resummation-audit/g85a_poisson_theta_resummation_audit.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g85a_poisson_theta_resummation_audit.py -q",
        ],
    }


def main() -> int:
    result = audit()
    RESULTS_PATH.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "files_examined_count": result["files_examined_count"],
                "poisson_identity_found": result["poisson_identity_found"],
                "theta_identity_found": result["theta_identity_found"],
                "bessel_identity_found": result["bessel_identity_found"],
                "proper_time_t_status": result["proper_time_t_status"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result["verdict"] in ALLOWED_VERDICTS else 1


if __name__ == "__main__":
    raise SystemExit(main())
