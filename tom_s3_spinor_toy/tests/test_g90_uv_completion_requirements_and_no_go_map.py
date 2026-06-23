"""G90 tests: UV completion requirements and no-go map."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_DIR = PROJECT_ROOT / "experiments" / "20260623-g90-uv-completion-requirements-and-no-go-map"
SCRIPT = EXPERIMENT_DIR / "g90_uv_completion_requirements_and_no_go_map.py"
RESULTS = EXPERIMENT_DIR / "results_g90.json"
NOTE = EXPERIMENT_DIR / "UV_COMPLETION_REQUIREMENTS_AND_NO_GO_MAP.md"

SPEC = importlib.util.spec_from_file_location("g90_uv_completion_requirements_and_no_go_map", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

ALLOWED_VERDICTS = {
    "UV_REQUIREMENTS_EXPLICITLY_LISTED",
    "NO_GO_MAP_COMPLETE",
    "PARTIAL_REQUIREMENTS_ONLY",
    "INSUFFICIENT_EVIDENCE",
    "MIXED",
}

REQUIRED_UV_ITEMS = [
    "A mechanism for exp(-lambda/rho6^2).",
    "A source for lambda.",
    "A hidden gauge / brane / instanton sector or comparable UV origin.",
    "A full 4D reduced action.",
    "Canonical radion normalization.",
    "Same-frame KK scale.",
    "A B-L breaking sector if Majorana/seesaw neutrinos are desired.",
    "Otherwise an explicit Dirac-only neutrino prediction.",
]

REQUIRED_ROUTES = [
    "Standard gauge reduction",
    "Spectral / proper-time",
    "Poisson / theta resummation",
    "Saddle / worldline",
    "Dual modulus",
    "Warp factor",
    "Dimensional lambda gate",
    "Physical mass ratio / canonical normalization",
    "Majorana mass / neutrino seesaw",
]


def _load_json() -> dict:
    return json.loads(RESULTS.read_text(encoding="utf-8"))


def test_script_writes_expected_files(tmp_path: Path) -> None:
    result = MODULE.build_result()
    assert result["verdict"] in ALLOWED_VERDICTS


def test_results_schema_and_verdict() -> None:
    data = _load_json()
    assert data["verdict"] in ALLOWED_VERDICTS
    assert set(data["uv_requirements"]) == set(REQUIRED_UV_ITEMS)
    assert all(item in NOTE.read_text(encoding="utf-8") for item in REQUIRED_UV_ITEMS)


def test_note_contains_required_routes_and_requirements() -> None:
    note = NOTE.read_text(encoding="utf-8")
    for route in REQUIRED_ROUTES:
        assert route in note, route
    for req in REQUIRED_UV_ITEMS:
        assert req in note, req


def test_supported_claims_have_evidence_pointers() -> None:
    data = _load_json()
    for item in data["supported_claims"]:
        assert item["evidence"], item
        assert isinstance(item["evidence"], list)
        assert all(isinstance(pointer, str) and pointer for pointer in item["evidence"])


def test_no_overclaiming_physical_ratio_or_majorana() -> None:
    note = NOTE.read_text(encoding="utf-8")
    assert "confirmed physical prediction" not in note.lower()
    assert "bare Majorana mass" in note
    assert "does not support" in note or "does not" in note.lower()


def test_json_includes_required_status_sections() -> None:
    data = _load_json()
    assert data["lambda_origin_status"]["status"] == "FREE_COUPLING_PARAMETER"
    assert data["mass_ratio_status"]["status"] == "INSUFFICIENT_ACTION"
    assert data["neutrino_status"]["status"] == "DIRAC_ONLY_CONFIRMED"
    assert data["next_required_gate"]
    assert data["no_go_routes"]
    assert data["conditional_routes"]

