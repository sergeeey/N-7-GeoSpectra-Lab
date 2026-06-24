"""G83: deterministic audit of the gauge-kinetic modulus scaling."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g83.json"

ALLOWED_VERDICTS = {
    "DERIVED_INVERSE_SQUARE",
    "DERIVED_POSITIVE_POWER",
    "NO_GAUGE_MODULUS_FOUND",
    "OPEN_MISSING_ACTION",
    "MIXED",
}

SEARCHED_TERMS = [
    "gauge kinetic",
    "gauge kinetic function",
    "KГ¤hler",
    "Kahler",
    "modulus",
    "T(rho",
    "rho6",
    "Einstein frame",
    "string frame",
    "Weyl",
    "dimensional reduction",
    "brane",
    "cycle",
    "volume",
    "flux",
    "gaugino",
    "non-perturbative",
    "lambda_np",
    "V_FLUX",
]

EVIDENCE = {
    "g28_decision": (
        "tom_s3_spinor_toy/experiments/"
        "20260619-g28-spectral-action/decision.md"
    ),
    "g28_implementation": (
        "tom_s3_spinor_toy/experiments/"
        "20260619-g28-spectral-action/g28_inner_fluctuation.py"
    ),
    "g54f_claim": (
        "tom_s3_spinor_toy/experiments/"
        "20260621-g54f-4d-eh-frame/claim.md"
    ),
    "g56_claim": (
        "tom_s3_spinor_toy/experiments/"
        "20260621-g56-kklt-like-np/claim.md"
    ),
    "g61_decision": (
        "tom_s3_spinor_toy/experiments/"
        "20260621-g61-lambda-origin/decision.md"
    ),
    "g79a_result": (
        "tom_s3_spinor_toy/experiments/"
        "20260622-g79a-lambda-identity-audit/results_g79a.json"
    ),
    "g79b_result": (
        "tom_s3_spinor_toy/experiments/"
        "20260622-g79b-lambda-bridge-feasibility/results_g79b.json"
    ),
    "g82_decision": (
        "tom_s3_spinor_toy/experiments/"
        "20260622-g82-canonical-mass/decision.md"
    ),
}

TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".txt"}


def _read(root: Path, key: str) -> str:
    return (root / EVIDENCE[key]).read_text(encoding="utf-8", errors="replace")


def _matching_files(root: Path) -> list[str]:
    """Return deterministic local files containing at least one search term."""
    matches: list[str] = []
    needles = [term.casefold() for term in SEARCHED_TERMS]
    for base in (root / "tom_s3_spinor_toy", root / "docs"):
        if not base.is_dir():
            continue
        for path in sorted(p for p in base.rglob("*") if p.suffix.lower() in TEXT_SUFFIXES):
            if HERE in path.parents:
                continue
            text = path.read_text(encoding="utf-8", errors="replace").casefold()
            if any(term in text for term in needles):
                matches.append(path.relative_to(root).as_posix())
    return matches


def _has_all(text: str, patterns: list[str]) -> bool:
    return all(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def audit(root: Path = ROOT) -> dict:
    missing_evidence = sorted(
        key for key, relative in EVIDENCE.items() if not (root / relative).is_file()
    )
    if missing_evidence:
        raise FileNotFoundError(f"Missing G83 evidence: {missing_evidence}")

    g28 = _read(root, "g28_implementation")
    g28_decision = _read(root, "g28_decision")
    g54f = _read(root, "g54f_claim")
    g56 = _read(root, "g56_claim")
    g61 = _read(root, "g61_decision")
    g79a = json.loads(_read(root, "g79a_result"))
    g79b = json.loads(_read(root, "g79b_result"))
    g82 = _read(root, "g82_decision")

    # Independent power bookkeeping from implemented project relations:
    # rho3 = C*rho6^2, Vol(S3) ~ rho3^3, Vol(S6) ~ rho6^6.
    rho3_power_on_constraint = 2
    vol_s3_power_on_constraint = 3 * rho3_power_on_constraint
    vol_s6_power = 6
    internal_volume_power = vol_s3_power_on_constraint + vol_s6_power

    g28_has_su2_candidate = _has_all(
        g28, [r"C_SU2", r"Vol\(S6\)", r"rho6\*\*6"]
    )
    g28_has_su3_candidate = _has_all(
        g28, [r"C_SU3", r"Vol\(S3\)", r"rho3\*\*3"]
    )
    g28_admits_not_4d = "Not 4D" in g28_decision
    g54_has_potential_frame_only = (
        "V^EH_Cas" in g54f and "V_int" in g54f and "gauge kinetic" not in g54f.casefold()
    )
    inverse_square_is_ansatz = (
        "only an ansatz" in g56
        and ("exp(−" in g56 or "exp(-" in g56)
        and ("ρ₆²" in g56 or "rho6**2" in g56)
    )
    g61_assumes_inverse_square = (
        "1/ρ₆²" in g61
        and "Status: WEAK" in g61
    )
    reduction_route = next(
        route
        for route in g79b["routes"]
        if route["id"] == "DIMENSIONAL_REDUCTION_GAUGE_KINETIC"
    )
    full_action_missing = (
        g28_admits_not_4d
        and g79b["verdict"] == "OPEN_MISSING_DERIVATION"
        and "higher-dimensional action" in reduction_route["missing_inputs"]
        and "exact T(rho6) relation" in reduction_route["missing_inputs"]
        and "M4/Ms" in g82
    )

    gauge_kinetic_candidates = [
        {
            "id": "G28_SU2_SPECTATOR_VOLUME",
            "expression": "1/g_SU2^2 proportional to Vol(S6)",
            "rho6_alpha_on_project_constraint": vol_s6_power,
            "frame": "internal spectral-action calculation; full 4D reduction absent",
            "status": "POSITIVE_POWER_CANDIDATE_NOT_4D_MODULUS",
        },
        {
            "id": "G28_SU3_SPECTATOR_VOLUME",
            "expression": "1/g_SU3^2 proportional to Vol(S3)",
            "rho6_alpha_on_project_constraint": vol_s3_power_on_constraint,
            "frame": "internal spectral-action calculation; full 4D reduction absent",
            "status": "POSITIVE_POWER_CANDIDATE_NOT_4D_MODULUS",
        },
        {
            "id": "G61_E7_TAU",
            "expression": "tau = 1/rho6^2",
            "rho6_alpha_on_project_constraint": -2,
            "frame": "not defined",
            "status": "ASSUMED_WEAK_CANDIDATE",
        },
    ]

    modulus_definitions = [
        {
            "source": EVIDENCE["g28_implementation"],
            "definition": "inverse gauge couplings from spectator volumes",
            "derived": True,
            "is_full_4d_gauge_modulus": False,
        },
        {
            "source": EVIDENCE["g61_decision"],
            "definition": "tau = 1/rho6^2",
            "derived": False,
            "is_full_4d_gauge_modulus": False,
        },
    ]
    frame_definitions = [
        {
            "source": EVIDENCE["g54f_claim"],
            "definition": "4D Einstein-frame rescaling for potential energy",
            "covers_gauge_kinetic_term": False,
        },
        {
            "source": EVIDENCE["g82_decision"],
            "definition": "conditional Einstein-frame radion kinetic metric",
            "covers_gauge_kinetic_term": False,
        },
    ]

    is_alpha_minus_two_derived = False
    is_k_fixed = False
    derived_alpha = None
    derived_C = None

    if is_alpha_minus_two_derived and is_k_fixed:
        verdict = "DERIVED_INVERSE_SQUARE"
    elif not modulus_definitions:
        verdict = "NO_GAUGE_MODULUS_FOUND"
    elif full_action_missing:
        verdict = "OPEN_MISSING_ACTION"
    else:
        verdict = "MIXED"

    supports_pi_over_9 = (
        is_alpha_minus_two_derived and is_k_fixed and derived_C == 1
    )
    supports_lambda_v_identity = (
        g79a["verdict"] == "PASS_SAME_LAMBDA"
        and g79b["verdict"] == "BRIDGE_DERIVED"
    )

    missing_inputs = [
        "higher-dimensional action containing the hidden gauge sector",
        "4D reduced and normalized gauge kinetic function f(T)",
        "explicit string-frame to 4D Einstein-frame treatment of gauge terms",
        "definition and normalization of T in terms of rho6",
        "hidden-sector embedding and wrapped cycle",
        "fixed coefficient k in T(rho6)",
    ]
    falsified_routes = [
        {
            "route": "G61_PI_OVER_9_AS_CURRENT_DERIVATION",
            "reason": "tau=1/rho6^2 is assumed rather than derived",
        },
        {
            "route": "G28_AS_COMPLETE_4D_GAUGE_MODULUS",
            "reason": "G28 explicitly states that the full 4D reduction is absent",
        },
    ]

    files_examined = _matching_files(root)
    gates = {
        "G83-1_evidence_present": not missing_evidence,
        "G83-2_positive_power_candidates_recomputed": (
            g28_has_su2_candidate
            and g28_has_su3_candidate
            and vol_s3_power_on_constraint == 6
            and vol_s6_power == 6
            and internal_volume_power == 12
        ),
        "G83-3_inverse_square_not_promoted": (
            inverse_square_is_ansatz
            and g61_assumes_inverse_square
            and not is_alpha_minus_two_derived
        ),
        "G83-4_missing_4d_action_detected": (
            g28_admits_not_4d and g54_has_potential_frame_only and full_action_missing
        ),
        "G83-5_lambda_v_separate": not supports_lambda_v_identity,
        "G83-6_verdict_allowed": verdict in ALLOWED_VERDICTS,
    }

    return {
        "gate": "G83",
        "verdict": verdict,
        "searched_terms": SEARCHED_TERMS,
        "files_examined": files_examined,
        "files_examined_count": len(files_examined),
        "modulus_definitions_found": modulus_definitions,
        "frame_definitions_found": frame_definitions,
        "gauge_kinetic_candidates": gauge_kinetic_candidates,
        "derived_alpha": derived_alpha,
        "derived_C": derived_C,
        "candidate_positive_alpha": 6,
        "is_alpha_minus_two_derived": is_alpha_minus_two_derived,
        "is_k_fixed": is_k_fixed,
        "supports_lambda_np_pi_over_9": supports_pi_over_9,
        "supports_lambda_v_identity": supports_lambda_v_identity,
        "missing_inputs": missing_inputs,
        "falsified_routes": falsified_routes,
        "next_required_gate": (
            "G84_EXPLICIT_REDUCED_GAUGE_ACTION_AND_FRAME_NORMALIZATION"
        ),
        "power_bookkeeping": {
            "rho3_power_on_constraint": rho3_power_on_constraint,
            "vol_s3_power_on_constraint": vol_s3_power_on_constraint,
            "vol_s6_power": vol_s6_power,
            "internal_volume_power": internal_volume_power,
        },
        "conclusion": (
            "The repository derives positive rho6^6 spectator-volume dependence "
            "for internal gauge kinetic coefficients, but does not derive a "
            "normalized 4D gauge modulus T(rho6). The inverse-square relation is "
            "an explicit weak assumption, so pi/9 is not presently supported."
        ),
        "gates": gates,
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g83-gauge-kinetic-modulus-scaling/g83_gauge_kinetic_modulus_scaling.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g83_gauge_kinetic_modulus_scaling.py -q",
            "python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py tom_s3_spinor_toy/tests/test_g79b_lambda_bridge_feasibility.py tom_s3_spinor_toy/tests/test_g82_canonical_mass.py -q",
        ],
    }


def main() -> int:
    result = audit()
    RESULTS_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "derived_alpha": result["derived_alpha"],
                "candidate_positive_alpha": result["candidate_positive_alpha"],
                "files_examined_count": result["files_examined_count"],
                "gates": result["gates"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if all(result["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
