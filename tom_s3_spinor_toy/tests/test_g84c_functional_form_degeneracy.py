from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260622-g84c-functional-form-degeneracy"
    / "g84c_functional_form_degeneracy.py"
)
SPEC = importlib.util.spec_from_file_location(
    "g84c_functional_form_degeneracy", SCRIPT
)
assert SPEC and SPEC.loader
G84C = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G84C
SPEC.loader.exec_module(G84C)


def test_schema_and_allowed_verdict():
    result = G84C.run()
    required = {
        "verdict",
        "rho0",
        "intervals",
        "forms_compared",
        "analytic_value_slope_match_possible",
        "analytic_relations",
        "fit_results",
        "max_relative_errors",
        "rms_relative_errors",
        "slope_errors",
        "curvature_errors",
        "potential_minimum_comparison",
        "mass_proxy_comparison",
        "distinguishable_under_threshold",
        "threshold_used",
        "missing_tolerance_inputs",
        "next_required_gate",
    }
    assert required <= set(result)
    assert result["verdict"] in G84C.ALLOWED_VERDICTS


def test_value_and_slope_match_is_impossible_for_positive_coefficients():
    result = G84C.run()
    assert result["analytic_value_slope_match_possible"] is False
    assert "value_match_relation" in result["analytic_relations"]
    assert "slope_match_relation" in result["analytic_relations"]


def test_project_relevant_fit_distinguishes_forms():
    result = G84C.run()
    if result["verdict"] == "LOCAL_DEGENERACY_FOUND":
        assert (
            result["rms_relative_errors"]["f_6"]["project_relevant"]
            <= result["threshold_used"]["rms_relative_max"]
        )
        assert (
            result["max_relative_errors"]["f_6"]["project_relevant"]
            <= result["threshold_used"]["max_relative_max"]
        )
    else:
        assert result["verdict"] == "FUNCTIONAL_FORM_DISTINGUISHABLE"
        assert result["distinguishable_under_threshold"] is True


def test_threshold_is_explicitly_audit_defined():
    result = G84C.run()
    assert result["missing_tolerance_inputs"]
    assert result["threshold_used"]["rms_relative_max"] > 0
    assert result["threshold_used"]["max_relative_max"] > 0


def test_negative_control_is_not_called_physical_derivation():
    result = G84C.run()
    assert result["potential_minimum_comparison"]["evaluated"] is True
    assert "surrogate" in result["potential_minimum_comparison"]
    assert "physical derivation" not in result["potential_minimum_comparison"]["interpretation"].lower()


def test_all_gates_pass():
    assert all(G84C.run()["gates"].values())
