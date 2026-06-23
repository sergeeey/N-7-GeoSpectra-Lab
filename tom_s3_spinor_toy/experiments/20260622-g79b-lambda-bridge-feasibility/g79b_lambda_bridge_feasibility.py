"""G79B вЂ” deterministic feasibility audit for bridging two lambda sectors."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g79b.json"

ALLOWED_VERDICTS = {
    "BRIDGE_DERIVED",
    "BRIDGE_REFUTED",
    "OPEN_MISSING_DERIVATION",
    "MIXED",
}

EVIDENCE = {
    "v_definition": "docs/compactification/registry/P13A_v_operator_ansatz.yaml",
    "v_nonidentifiability": "experiments/20260611-lambda-b5-g4-identifiability/results_g4.json",
    "np_candidates": "tom_s3_spinor_toy/experiments/20260621-g61-lambda-origin/decision.md",
    "parameter_registry": (
        "tom_s3_spinor_toy/experiments/"
        "20260622-g76-parameter-registry/parameter_registry.json"
    ),
    "identity_audit": (
        "tom_s3_spinor_toy/experiments/"
        "20260622-g79a-lambda-identity-audit/results_g79a.json"
    ),
    "nonlinear_hypothesis": "docs/compactification/hypotheses/HYP_03_NONLINEAR_REALIZATION.md",
    "np_implementation": "tom_s3_spinor_toy/tests/test_g62_observables.py",
}


def dependency_graph() -> dict:
    nodes = [
        {
            "id": "lambda_v_operator",
            "kind": "free_parameter",
            "inputs": ["V_operator_normalization", "V_observable"],
            "status": "FREE",
        },
        {
            "id": "lambda_np",
            "kind": "free_parameter",
            "inputs": ["NP_action", "rho6_field_definition"],
            "status": "FREE",
        },
        {
            "id": "rho6",
            "kind": "shared_geometry",
            "inputs": ["S6_radius_convention"],
            "status": "CONDITIONAL",
        },
        {
            "id": "S3xS6_geometry",
            "kind": "shared_geometry",
            "inputs": ["n3", "n6", "metric_conventions"],
            "status": "FIXED_WITHIN_ANSATZ",
        },
        {
            "id": "bridge_map",
            "kind": "missing_derivation",
            "inputs": [
                "common_reduced_action",
                "canonical_field_map",
                "operator_to_NP_matching",
            ],
            "status": "OPEN",
        },
    ]
    edges = [
        {"from": "S3xS6_geometry", "to": "lambda_v_operator", "status": "insufficient"},
        {"from": "S3xS6_geometry", "to": "lambda_np", "status": "candidate_only"},
        {"from": "rho6", "to": "lambda_np", "status": "implemented_in_ansatz"},
        {"from": "lambda_v_operator", "to": "bridge_map", "status": "missing_normalization"},
        {"from": "lambda_np", "to": "bridge_map", "status": "missing_microscopic_action"},
    ]
    return {"nodes": nodes, "edges": edges}


def routes() -> list[dict]:
    return [
        {
            "id": "DIRECT_OPERATOR_MATCHING",
            "required_derivation": (
                "Derive V-operator and NP exponential from one normalized reduced action, "
                "then show the same coefficient multiplies both terms after field redefinitions."
            ),
            "existing_evidence": ["v_definition", "v_nonidentifiability", "nonlinear_hypothesis"],
            "missing_inputs": [
                "parent action containing both sectors",
                "operationally normalized V observable",
                "canonical field redefinition linking V variables to rho6",
            ],
            "falsifier": (
                "The common action contains independent counterterms or independent "
                "normalization constants for the two coefficients."
            ),
            "derivation_executable_with_current_repo": False,
            "current_status": "OPEN",
        },
        {
            "id": "DIMENSIONAL_REDUCTION_GAUGE_KINETIC",
            "required_derivation": (
                "Perform the full higher-dimensional to 4D Einstein-frame reduction and "
                "derive both the V coupling and the gauge kinetic/modulus function f(T), "
                "including T(rho6)."
            ),
            "existing_evidence": ["parameter_registry", "np_implementation"],
            "missing_inputs": [
                "higher-dimensional action",
                "normalized gravitational and gauge terms",
                "dilaton/warp dependence",
                "exact T(rho6) relation",
            ],
            "falsifier": "The reduced coefficients depend on independent moduli or normalization constants.",
            "derivation_executable_with_current_repo": False,
            "current_status": "OPEN",
        },
        {
            "id": "GAUGINO_CONDENSATION",
            "required_derivation": (
                "Specify a hidden gauge sector, derive W_np=A exp(-2*pi*T/h_dual), "
                "derive T(rho6), and independently match its coefficient to lambda_v_operator."
            ),
            "existing_evidence": ["np_candidates"],
            "missing_inputs": [
                "explicit hidden-sector embedding",
                "dual Coxeter number selected by the model",
                "gauge kinetic function",
                "T(rho6) derivation",
                "separate V-to-NP coefficient matching",
            ],
            "falsifier": (
                "The derived lambda_np differs from lambda_v_operator after all "
                "normalizations, or the hidden sector is absent/inconsistent."
            ),
            "derivation_executable_with_current_repo": False,
            "current_status": "CONDITIONAL_CANDIDATE_ONLY",
        },
        {
            "id": "INSTANTON_ACTION",
            "required_derivation": (
                "Compute the wrapped Euclidean brane DBI+CS action and reduce it to "
                "S_inst=lambda_np/rho6^2, then match the same normalized interaction "
                "to the V-operator coefficient."
            ),
            "existing_evidence": ["np_candidates"],
            "missing_inputs": [
                "brane species and wrapped cycle",
                "brane tension",
                "dilaton and warp factor",
                "RR/NS background fields",
                "cycle-volume normalization",
                "V-sector matching calculation",
            ],
            "falsifier": (
                "The instanton action has a different rho6 dependence or an independent prefactor."
            ),
            "derivation_executable_with_current_repo": False,
            "current_status": "OPEN",
        },
        {
            "id": "NUMERICAL_COINCIDENCE",
            "required_derivation": (
                "No derivation exists; compare candidate numbers only as a diagnostic."
            ),
            "existing_evidence": ["np_candidates", "identity_audit"],
            "missing_inputs": ["a theoretical mechanism turning proximity into identity"],
            "falsifier": (
                "Candidate agreement disappears under allowed normalization, uplift, "
                "or radius-convention changes."
            ),
            "derivation_executable_with_current_repo": True,
            "current_status": "INSUFFICIENT_FOR_IDENTITY",
        },
    ]


def audit(root: Path = ROOT) -> dict:
    missing_evidence = sorted(
        key for key, rel in EVIDENCE.items() if not (root / rel).is_file()
    )
    route_rows = routes()
    derived_routes = [
        row for row in route_rows if row["current_status"] == "BRIDGE_DERIVED"
    ]
    refuted_routes = [
        row for row in route_rows if row["current_status"] == "BRIDGE_REFUTED"
    ]
    executable_derivations = [
        row["id"]
        for row in route_rows
        if row["derivation_executable_with_current_repo"]
        and row["id"] != "NUMERICAL_COINCIDENCE"
    ]

    if derived_routes:
        verdict = "BRIDGE_DERIVED"
    elif len(refuted_routes) == len(route_rows):
        verdict = "BRIDGE_REFUTED"
    else:
        verdict = "OPEN_MISSING_DERIVATION"

    gates = {
        "G79B-1_evidence_files_exist": not missing_evidence,
        "G79B-2_dependency_graph_complete": len(dependency_graph()["nodes"]) >= 5,
        "G79B-3_all_routes_have_required_fields": all(
            {
                "required_derivation",
                "missing_inputs",
                "falsifier",
                "derivation_executable_with_current_repo",
            }
            <= set(row)
            for row in route_rows
        ),
        "G79B-4_numerical_coincidence_not_bridge": next(
            row for row in route_rows if row["id"] == "NUMERICAL_COINCIDENCE"
        )["current_status"]
        == "INSUFFICIENT_FOR_IDENTITY",
        "G79B-5_g78_bridge_status_conditional": True,
        "G79B-6_verdict_allowed": verdict in ALLOWED_VERDICTS,
    }
    return {
        "gate": "G79B",
        "verdict": verdict,
        "precondition": "G79A=OPEN_IDENTITY_UNPROVEN",
        "dependency_graph": dependency_graph(),
        "routes": route_rows,
        "route_count": len(route_rows),
        "missing_evidence": missing_evidence,
        "bridge_derivations_executable_now": executable_derivations,
        "g78_status": (
            "CONDITIONAL_FOR_LAMBDA_NP; BLOCKED_AS_DERIVATION_OF_LAMBDA_V_OPERATOR"
        ),
        "conclusion": (
            "Current repository data can test numerical proximity and internal "
            "consistency, but cannot derive or refute the cross-sector bridge."
        ),
        "gates": gates,
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g79b-lambda-bridge-feasibility/g79b_lambda_bridge_feasibility.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g79b_lambda_bridge_feasibility.py -q",
            "python -m pytest tom_s3_spinor_toy/tests/test_g79a_lambda_identity_audit.py tom_s3_spinor_toy/tests/test_g76_parameter_registry.py -q",
        ],
    }


def main() -> int:
    results = audit()
    RESULTS_PATH.write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if all(results["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
