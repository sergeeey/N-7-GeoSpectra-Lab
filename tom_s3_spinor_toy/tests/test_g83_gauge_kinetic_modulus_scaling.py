from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g83-gauge-kinetic-modulus-scaling"
    / "g83_gauge_kinetic_modulus_scaling.py"
)
SPEC = importlib.util.spec_from_file_location(
    "g83_gauge_kinetic_modulus_scaling", SCRIPT
)
assert SPEC and SPEC.loader
G83 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G83)


def test_required_json_schema_and_allowed_verdict():
    result = G83.audit()
    required = {
        "verdict",
        "searched_terms",
        "files_examined",
        "modulus_definitions_found",
        "frame_definitions_found",
        "gauge_kinetic_candidates",
        "derived_alpha",
        "derived_C",
        "is_alpha_minus_two_derived",
        "is_k_fixed",
        "supports_lambda_np_pi_over_9",
        "supports_lambda_v_identity",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
    }
    assert required <= set(result)
    assert result["verdict"] in G83.ALLOWED_VERDICTS


def test_positive_power_candidates_are_recomputed_but_not_overstated():
    result = G83.audit()
    assert result["power_bookkeeping"] == {
        "rho3_power_on_constraint": 2,
        "vol_s3_power_on_constraint": 6,
        "vol_s6_power": 6,
        "internal_volume_power": 12,
    }
    assert result["candidate_positive_alpha"] == 6
    assert result["derived_alpha"] is None


def test_inverse_square_verdict_requires_strong_evidence():
    result = G83.audit()
    if result["verdict"] == "DERIVED_INVERSE_SQUARE":
        assert result["derived_alpha"] == -2
        assert result["is_alpha_minus_two_derived"] is True
        assert result["is_k_fixed"] is True
    else:
        assert result["is_alpha_minus_two_derived"] is False


def test_missing_action_forbids_inverse_square_promotion():
    result = G83.audit()
    assert result["missing_inputs"]
    assert result["verdict"] == "OPEN_MISSING_ACTION"
    assert result["verdict"] != "DERIVED_INVERSE_SQUARE"
    assert result["supports_lambda_np_pi_over_9"] is False


def test_lambda_v_identity_remains_unclaimed():
    result = G83.audit()
    assert result["supports_lambda_v_identity"] is False
    assert result["gates"]["G83-5_lambda_v_separate"]


def test_all_audit_gates_pass():
    result = G83.audit()
    assert all(result["gates"].values())
