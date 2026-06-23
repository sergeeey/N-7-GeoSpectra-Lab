"""G88C: adversarial referee for the physical mass ratio claim."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88c.json"


def run() -> dict:
    old_proxy = 0.020248
    canonical_proxy = 0.0025165
    reduction = canonical_proxy / old_proxy

    verdict = "CANONICAL_PROXY_ONLY"
    reference_value_verdict = "COORDINATE_ARTIFACT"

    gates = {
        "G88C-1_old_value_is_coordinate_artifact": old_proxy > canonical_proxy * 5,
        "G88C-2_canonical_proxy_exists": canonical_proxy > 0,
        "G88C-3_physical_ratio_not_confirmed": True,
        "G88C-4_missing_action_and_scale_map": True,
        "G88C-5_no_invalid_equality_between_old_and_canonical": abs(old_proxy - canonical_proxy) > 1e-3,
    }

    return {
        "gate": "G88C",
        "verdict": verdict,
        "reference_value_verdict": reference_value_verdict,
        "old_coordinate_ratio": old_proxy,
        "canonical_metric_only_ratio": canonical_proxy,
        "canonical_to_coordinate_ratio": reduction,
        "physical_mass_ratio_identified": False,
        "missing_inputs": [
            "explicit reduced 4D action",
            "M4/Ms map",
            "proof that the compared KK scale is defined in the same frame as the radion mass",
        ],
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88c-adversarial-mass-ratio-referee/g88c_adversarial_mass_ratio_referee.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
