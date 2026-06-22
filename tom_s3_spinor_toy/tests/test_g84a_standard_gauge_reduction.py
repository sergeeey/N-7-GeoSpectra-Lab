from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g84a-standard-gauge-reduction"
    / "g84a_standard_gauge_reduction.py"
)
SPEC = importlib.util.spec_from_file_location("g84a_standard_gauge_reduction", SCRIPT)
assert SPEC and SPEC.loader
G84A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G84A
SPEC.loader.exec_module(G84A)


def test_schema_and_verdict():
    result = G84A.run()
    required = {
        "verdict",
        "action_ansatz",
        "sector_results",
        "weyl_scaling",
        "derived_baseline_alphas",
        "inverse_square_derived",
        "required_compensators",
        "supports_lambda_np_pi_over_9",
        "supports_lambda_v_identity",
        "gates",
    }
    assert required <= set(result)
    assert result["verdict"] in G84A.ALLOWED_VERDICTS


def test_direct_and_logarithmic_power_derivations_agree():
    result = G84A.run()
    for row in result["sector_results"]:
        assert row["direct_volume_alpha"] == row["log_derivative_alpha"]


def test_standard_reduction_gives_positive_volume_powers():
    result = G84A.run()
    assert result["derived_baseline_alphas"] == {
        "BULK_S3XS6": 12,
        "LOCALIZED_S3": 6,
        "LOCALIZED_S6": 6,
    }
    assert result["verdict"] == "DERIVED_POSITIVE_POWER_STANDARD_ANSATZ"


def test_four_dimensional_yang_mills_is_weyl_invariant():
    result = G84A.run()
    assert G84A.weyl_power_in_omega(4, form_rank=2) == 0
    assert result["weyl_scaling"]["changes_rho6_power_in_4d"] is False


def test_weyl_detector_has_negative_control_power():
    assert G84A.weyl_power_in_omega(5, form_rank=2) == 1
    assert G84A.weyl_power_in_omega(3, form_rank=2) == -1


def test_inverse_square_requires_explicit_compensator():
    result = G84A.run()
    assert result["inverse_square_derived"] is False
    assert result["required_compensators"] == {
        "bulk_prefactor_alpha": -14,
        "s3_localized_prefactor_alpha": -8,
        "s6_localized_prefactor_alpha": -8,
    }


def test_no_lambda_identity_or_pi_over_9_claim():
    result = G84A.run()
    assert result["supports_lambda_np_pi_over_9"] is False
    assert result["supports_lambda_v_identity"] is False


def test_all_gates_pass():
    assert all(G84A.run()["gates"].values())
