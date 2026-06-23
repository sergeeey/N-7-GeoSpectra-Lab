from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g89b-b-minus-l-breaking-operator-audit"
    / "g89b_b_minus_l_breaking_operator_audit.py"
)
SPEC = importlib.util.spec_from_file_location("g89b_b_minus_l_breaking_operator_audit", SCRIPT)
assert SPEC and SPEC.loader
G89B = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G89B
SPEC.loader.exec_module(G89B)


def test_schema_and_allowed_verdict():
    result = G89B.run()
    required = {
        "gate",
        "verdict",
        "candidates_examined",
        "b_minus_l_exact",
        "nu_r_b_minus_l",
        "majorana_bilinear_b_minus_l",
        "b_minus_l_plus_two_candidate_found",
        "candidate_sources",
        "candidate_quantum_numbers",
        "coupling_to_nu_r_nu_r_allowed",
        "candidate_derived_from_geometry",
        "candidate_vev_available",
        "seesaw_supported",
        "dirac_only_supported",
        "missing_inputs",
        "next_required_gate",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {
        "B_MINUS_L_BREAKING_OPERATOR_FOUND",
        "MAJORANA_REQUIRES_NEW_B_MINUS_L_FIELD",
        "DIRAC_ONLY_CONFIRMED",
        "OPEN_MISSING_QUANTUM_NUMBERS",
        "OPEN_MISSING_SCALAR_SECTOR",
        "MIXED",
    }


def test_dirac_only_conclusion_and_no_plus_two_candidate():
    result = G89B.run()
    assert result["verdict"] == "DIRAC_ONLY_CONFIRMED"
    assert result["b_minus_l_exact"] is True
    assert result["nu_r_b_minus_l"] == -1
    assert result["majorana_bilinear_b_minus_l"] == -2
    assert result["b_minus_l_plus_two_candidate_found"] is False
    assert result["coupling_to_nu_r_nu_r_allowed"] is False
    assert result["seesaw_supported"] is False


def test_all_gates_pass():
    assert all(G89B.run()["gates"].values())

