"""G76 вЂ” validate the stabilization parameter registry."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY_PATH = HERE / "parameter_registry.json"
RESULTS_PATH = HERE / "results_g76.json"
REQUIRED_FIELDS = {"symbol", "class", "provenance", "dependencies", "scope"}
ALLOWED_CLASSES = {"fixed", "conditional", "free"}


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def audit_registry(registry: dict) -> dict:
    entries = registry["parameters"]
    symbols = [entry["symbol"] for entry in entries]
    symbol_set = set(symbols)

    complete = all(REQUIRED_FIELDS <= set(entry) for entry in entries)
    unique = len(symbols) == len(symbol_set)
    classes_valid = all(entry["class"] in ALLOWED_CLASSES for entry in entries)
    dangling = sorted(
        {
            dep
            for entry in entries
            for dep in entry["dependencies"]
            if dep not in symbol_set
        }
    )
    by_symbol = {entry["symbol"]: entry for entry in entries}

    gates = {
        "G76-1_schema_complete": complete and unique and classes_valid,
        "G76-2_no_dangling_dependencies": not dangling,
        "G76-3_external_inputs_explicit": (
            by_symbol["C_SM"]["class"] == "conditional"
            and by_symbol["C_SM"]["provenance"] == "external"
        ),
        "G76-4_lambda_symbols_separate": (
            "lambda_np" in symbol_set
            and "lambda_v_operator" in symbol_set
            and by_symbol["lambda_np"] is not by_symbol["lambda_v_operator"]
        ),
        "G76-5_amplitudes_conditional": (
            by_symbol["A_np"]["class"] == "conditional"
            and by_symbol["uplift_D"]["class"] == "conditional"
        ),
        "G76-6_mass_scale_not_claimed_fixed": by_symbol["M4_over_Ms"]["class"] == "free",
    }
    counts = {
        category: sum(entry["class"] == category for entry in entries)
        for category in sorted(ALLOWED_CLASSES)
    }
    verdict = "PASS" if all(gates.values()) else "FAIL"
    return {
        "gate": "G76",
        "verdict": verdict,
        "parameter_count": len(entries),
        "class_counts": counts,
        "gates": gates,
        "dangling_dependencies": dangling,
        "lambda_identity_assumed": False,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260622-g76-parameter-registry/g76_parameter_registry.py"
        ),
    }


def main() -> int:
    results = audit_registry(load_registry())
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
