"""Load frozen P11–P13G YAML registries (canonical source on disk)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

REGISTRY_DIR = Path(__file__).resolve().parents[2] / "docs" / "compactification" / "registry"

FROZEN_GATE_FILES = (
    "P11_robust_wigner_cg_pattern.yaml",
    "P12_matrix_element_pattern.yaml",
    "P13A_v_operator_ansatz.yaml",
    "P13B1_spinor_basis.yaml",
    "P13C_ben_achour_sources.yaml",
    "P13D_convention_stack.yaml",
    "P13E_no_go.yaml",
    "P13F_no_go.yaml",
    "P13G_handoff.yaml",
)


def load_registry(name: str) -> dict[str, Any]:
    path = REGISTRY_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Frozen registry missing: {path}")
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"Registry {name} must be a mapping")
    return data


def assert_frozen_registry_present() -> list[str]:
    missing = [f for f in FROZEN_GATE_FILES if not (REGISTRY_DIR / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing frozen registry files: {missing}")
    return list(FROZEN_GATE_FILES)


def registry_snapshot_json() -> str:
    payload = {f: load_registry(f) for f in FROZEN_GATE_FILES}
    return json.dumps(payload, indent=2, sort_keys=True)
