from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g84b-spectral-origin-inverse-square"
    / "g84b_spectral_origin_inverse_square.py"
)
SPEC = importlib.util.spec_from_file_location(
    "g84b_spectral_origin_inverse_square", SCRIPT
)
assert SPEC and SPEC.loader
G84B = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G84B
SPEC.loader.exec_module(G84B)


def test_schema_and_allowed_verdict():
    result = G84B.audit()
    required = {
        "verdict",
        "searched_terms",
        "files_examined_count",
        "operators_examined",
        "candidate_operator_count",
        "eigenvalue_scalings",
        "inverse_square_scaling_found",
        "proper_time_exponent_found",
        "proper_time_t_status",
        "final_effective_exponential_found",
        "determinant_or_zeta_prime_checked",
        "finite_part_behavior",
        "lambda_candidates_from_spectrum",
        "matches_one_third",
        "matches_pi_over_9",
        "lambda_np_fixed",
        "lambda_v_connection_found",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
    }
    assert required <= set(result)
    assert result["verdict"] in G84B.ALLOWED_VERDICTS


def test_inverse_square_exists_but_final_bridge_is_absent():
    result = G84B.audit()
    assert result["inverse_square_scaling_found"] is True
    assert result["proper_time_exponent_found"] is True
    assert result["final_effective_exponential_found"] is False
    assert result["verdict"] == "PROPER_TIME_FORM_ONLY"


def test_proper_time_t_is_integrated_not_fixed():
    result = G84B.audit()
    assert result["proper_time_t_status"] == "integrated_over"
    assert result["lambda_np_fixed"] is False


def test_no_lambda_v_bridge():
    result = G84B.audit()
    assert result["lambda_v_connection_found"] is False
    assert result["gates"]["G84B-7_lambda_v_remains_separate"]


def test_bridge_requires_more_than_integrand_level_form():
    result = G84B.audit()
    assert result["verdict"] != "SPECTRAL_BRIDGE_DERIVED"
    assert any("integrand" in item["reason"] or "integral" in item["reason"] for item in result["falsified_routes"])


def test_pi_over_nine_not_claimed_as_spectral_result():
    result = G84B.audit()
    assert result["matches_pi_over_9"] is False
    assert result["matches_one_third"] is False
