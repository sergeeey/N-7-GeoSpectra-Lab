from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g85a-poisson-bessel-resummation-audit"
    / "g85a_poisson_theta_resummation_audit.py"
)
SPEC = importlib.util.spec_from_file_location("g85a_poisson_theta_resummation_audit", SCRIPT)
assert SPEC and SPEC.loader
G85A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G85A
SPEC.loader.exec_module(G85A)


def test_schema_and_allowed_verdict():
    result = G85A.audit()
    required = {
        "gate",
        "verdict",
        "searched_terms",
        "files_examined_count",
        "files_examined",
        "focus_files_examined",
        "poisson_identity_found",
        "theta_identity_found",
        "bessel_identity_found",
        "proper_time_integrand_found",
        "proper_time_t_status",
        "final_effective_exponential_found",
        "resummation_bridge_found",
        "determinant_or_zeta_prime_checked",
        "lambda_np_fixed",
        "lambda_v_connection_found",
        "candidate_routes",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
        "reproduction_commands",
    }
    assert required <= set(result)
    assert result["verdict"] in G85A.ALLOWED_VERDICTS


def test_poisson_theta_form_is_present_but_not_closed():
    result = G85A.audit()
    assert result["poisson_identity_found"] is True
    assert result["theta_identity_found"] is True
    assert result["proper_time_integrand_found"] is True
    assert result["proper_time_t_status"] == "integrated_over"
    assert result["final_effective_exponential_found"] is False
    assert result["resummation_bridge_found"] is False
    assert result["verdict"] == "POISSON_THETA_FORM_ONLY"


def test_bessel_route_is_absent():
    result = G85A.audit()
    assert result["bessel_identity_found"] is False
    assert any("Bessel" in item["reason"] for item in result["falsified_routes"])


def test_lambda_np_and_lambda_v_remain_unfixed_and_separate():
    result = G85A.audit()
    assert result["lambda_np_fixed"] is False
    assert result["lambda_v_connection_found"] is False


def test_candidate_routes_make_the_gap_explicit():
    result = G85A.audit()
    routes = {item["route"]: item for item in result["candidate_routes"]}
    assert routes["POISSON_THETA_HEAT_KERNEL"]["found"] is True
    assert routes["BESSEL_REEXPRESSION"]["found"] is False
    assert routes["PROPER_TIME_SADDLE"]["found"] is True
    assert routes["DETERMINANT_ZETA_FINITE_PART"]["found"] is True
    assert routes["KKLT_ANSATZ"]["found"] is True


def test_no_claim_of_final_effective_exponential():
    result = G85A.audit()
    assert result["verdict"] != "RESUMMATION_BRIDGE_DERIVED"
    assert any("resummation" in item.lower() for item in result["missing_inputs"])
    assert result["final_effective_exponential_found"] is False
