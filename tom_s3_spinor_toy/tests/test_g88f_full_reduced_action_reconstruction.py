from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260623-g88f-full-reduced-action-reconstruction"
    / "g88f_full_reduced_action_reconstruction.py"
)
SPEC = importlib.util.spec_from_file_location("g88f_full_reduced_action_reconstruction", SCRIPT)
assert SPEC and SPEC.loader
G88F = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = G88F
SPEC.loader.exec_module(G88F)


def test_schema_and_allowed_verdict():
    result = G88F.run()
    required = {
        "gate",
        "verdict",
        "searched_terms",
        "files_examined_count",
        "source_files",
        "evidence_levels",
        "full_reduced_action_reconstructed",
        "canonical_field_defined",
        "canonical_normalization_explicit",
        "coordinate_proxy_value",
        "canonical_proxy_value",
        "physical_ratio_value",
        "ratio_invariant_under_reparametrization",
        "same_frame_comparison",
        "missing_inputs",
        "falsified_routes",
        "next_required_gate",
        "gates",
        "reproduction_command",
    }
    assert required <= set(result)
    assert result["verdict"] in {
        "REDUCED_ACTION_RECONSTRUCTED",
        "INSUFFICIENT_ACTION",
        "CANONICAL_PROXY_ONLY",
        "COORDINATE_ARTIFACT",
        "INVALID_ACTION",
        "MIXED",
    }


def test_action_is_incomplete_and_not_physical():
    result = G88F.run()
    assert result["verdict"] == "INSUFFICIENT_ACTION"
    assert result["physical_ratio_value"] is None
    assert result["full_reduced_action_reconstructed"] is False
    assert result["same_frame_comparison"] is False


def test_gates_reflect_incomplete_chain():
    gates = G88F.run()["gates"]
    assert gates["G88F-1_sources_found"] is True
    # G88F-2 is True: partial chain elements (canonical_field, einstein_frame,
    # kk_scale, reduced_action) now exist in G82/G83/G85 — chain is partial but
    # full reconstruction (G88F-3) is still absent, verdict stays INSUFFICIENT_ACTION
    assert gates["G88F-2_partial_chain_present"] is True
    assert gates["G88F-3_full_reconstruction_found"] is False
    assert gates["G88F-4_physical_ratio_not_promoted"] is True
    assert gates["G88F-5_coordinate_proxy_remains_proxy"] is True
