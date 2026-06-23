from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g89a-majorana-gauge-invariance-selection-rules"
    / "g89a_majorana_gauge_invariance_selection_rules.py"
)
SPEC = importlib.util.spec_from_file_location("g89a_majorana_gauge_invariance_selection_rules", SCRIPT)
assert SPEC and SPEC.loader
G89A = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G89A
SPEC.loader.exec_module(G89A)


def test_schema_and_allowed_verdict():
    result = G89A.run()
    required = {
        "gate",
        "verdict",
        "searched_terms",
        "files_examined_count",
        "source_files",
        "nu_r_b_minus_l",
        "majorana_bilinear_b_minus_l",
        "exact_b_minus_l_preserved",
        "b_minus_l2_scalar_found",
        "dirac_neutrino_explicit",
        "majorana_missing_from_repo",
        "mass_term_status",
        "requires_b_minus_l_breaking",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {
        "MAJORANA_ALLOWED",
        "MAJORANA_FORBIDDEN_BY_B_MINUS_L",
        "MAJORANA_REQUIRES_B_MINUS_L_BREAKING",
        "DIRAC_ONLY_ALLOWED",
        "INSUFFICIENT_QUANTUM_NUMBERS",
        "MIXED",
    }


def test_dirac_only_conclusion_is_supported():
    result = G89A.run()
    assert result["verdict"] == "DIRAC_ONLY_ALLOWED"
    assert result["nu_r_b_minus_l"] == -1
    assert result["majorana_bilinear_b_minus_l"] == -2
    assert result["exact_b_minus_l_preserved"] is True
    assert result["b_minus_l2_scalar_found"] is False
    assert result["dirac_neutrino_explicit"] is True


def test_all_gates_pass():
    assert all(G89A.run()["gates"].values())

