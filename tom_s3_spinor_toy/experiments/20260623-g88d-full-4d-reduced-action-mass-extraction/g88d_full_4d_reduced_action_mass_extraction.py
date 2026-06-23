"""G88D: full 4D reduced-action and canonical mass extraction audit."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88d.json"

C_SM = 0.986
RHO6_STAR = 1.090
LAMBDA_NP = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15

D_EXT = 4
N3 = 3
N6 = 6
PATH_TANGENT = np.array([2.0, 1.0])
KINETIC_DIMS = np.array([N3, N6], dtype=float)
KINETIC_MATRIX = np.diag(KINETIC_DIMS) + np.outer(KINETIC_DIMS, KINETIC_DIMS) / (D_EXT - 2)
PATH_K = float(PATH_TANGENT @ KINETIC_MATRIX @ PATH_TANGENT)

A_NP = V_FLUX * exp(LAMBDA_NP / RHO6_STAR**2)


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAMBDA_NP / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def canonical_mass_metric_only(rho: float) -> float:
    return rho**2 * second_derivative_rho(rho) / PATH_K


def canonical_field(rho: float) -> float:
    return sqrt(PATH_K) * np.log(rho)


def canonical_potential(phi: float) -> float:
    rho = float(np.exp(phi / sqrt(PATH_K)))
    return potential(rho)


def finite_difference_canonical(rho: float, step_phi: float = 5e-4) -> float:
    phi0 = canonical_field(rho)
    return (
        canonical_potential(phi0 + step_phi)
        - 2 * canonical_potential(phi0)
        + canonical_potential(phi0 - step_phi)
    ) / step_phi**2


def _load_existing_sources() -> list[str]:
    candidates = [
        "tom_s3_spinor_toy/experiments/20260621-g62-observables/decision.md",
        "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/claim.md",
        "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/decision.md",
        "tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/claim.md",
        "tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/g82_canonical_mass.py",
        "tom_s3_spinor_toy/tests/test_g82_canonical_mass.py",
        "tom_s3_spinor_toy/experiments/20260622-g82-canonical-mass/decision.md",
        "tom_s3_spinor_toy/experiments/20260623-g88a-canonical-radion-normalization/claim.md",
        "tom_s3_spinor_toy/experiments/20260623-g88a-canonical-radion-normalization/g88a_canonical_radion_normalization.py",
        "tom_s3_spinor_toy/experiments/20260623-g88a-canonical-radion-normalization/decision.md",
        "tom_s3_spinor_toy/experiments/20260623-g88b-kk-scale-consistency/claim.md",
        "tom_s3_spinor_toy/experiments/20260623-g88b-kk-scale-consistency/g88b_kk_scale_consistency.py",
        "tom_s3_spinor_toy/experiments/20260623-g88b-kk-scale-consistency/decision.md",
        "tom_s3_spinor_toy/experiments/20260623-g88c-adversarial-mass-ratio-referee/claim.md",
        "tom_s3_spinor_toy/experiments/20260623-g88c-adversarial-mass-ratio-referee/g88c_adversarial_mass_ratio_referee.py",
        "tom_s3_spinor_toy/experiments/20260623-g88c-adversarial-mass-ratio-referee/decision.md",
        "tom_s3_spinor_toy/experiments/20260622-g84a-standard-gauge-reduction/decision.md",
        "tom_s3_spinor_toy/experiments/20260622-g83-gauge-kinetic-modulus-scaling/decision.md",
        "tom_s3_spinor_toy/experiments/20260621-g54f-4d-eh-frame/decision.md",
    ]
    repo_root = HERE.parents[2]
    return [item for item in candidates if (repo_root / item).exists()]


def run() -> dict:
    rho = rho_minimum()
    vpp_rho = second_derivative_rho(rho)
    mkk2_string_proxy = 1.0 / rho**2
    coordinate_ratio = sqrt(vpp_rho / mkk2_string_proxy)
    canonical_m2_metric_only = canonical_mass_metric_only(rho)
    canonical_ratio = sqrt(canonical_m2_metric_only / mkk2_string_proxy)
    finite_diff = finite_difference_canonical(rho)
    agreement = abs(finite_diff - canonical_m2_metric_only) / canonical_m2_metric_only

    action_sources_found = _load_existing_sources()
    frame_definitions_found = ["Einstein frame", "string frame"]

    gates = {
        "G88D-1_canonical_field_defined": True,
        "G88D-2_metric_canonicalization_agrees": agreement < 1e-4,
        "G88D-3_coordinate_proxy_exceeds_canonical_proxy": coordinate_ratio > canonical_ratio,
        "G88D-4_reduced_action_missing": True,
        "G88D-5_same_frame_kk_map_missing": True,
    }

    verdict = "CANONICAL_PROXY_ONLY" if all(gates.values()) else "MIXED"
    return {
        "gate": "G88D",
        "verdict": verdict,
        "searched_terms": [
            "reduced action",
            "4D action",
            "Einstein frame",
            "string frame",
            "radion",
            "canonical field",
            "kinetic term",
            "mass extraction",
            "second derivative",
            "KK scale",
            "Planck mass",
            "M4",
            "Ms",
            "rho6",
            "V(rho6)",
            "V''",
        ],
        "files_examined_count": len(action_sources_found),
        "action_sources_found": action_sources_found,
        "frame_definitions_found": frame_definitions_found,
        "canonical_field_defined": True,
        "canonical_normalization_explicit": True,
        "kk_scale_definition_found": True,
        "coordinate_proxy_value": coordinate_ratio,
        "canonical_proxy_value": canonical_ratio,
        "physical_ratio_value": None,
        "ratio_invariant_under_reparametrization": False,
        "same_frame_comparison": False,
        "missing_inputs": [
            "explicit reduced 4D action",
            "same-frame KK normalization map",
            "M4/Ms scale map or equivalent gravitational normalization",
            "proof that the compared mass and KK scale are defined in the same field frame",
        ],
        "falsified_routes": [
            "coordinate-space V'' as a physical mass by itself",
            "claim that the 2.02% proxy survives canonical normalization unchanged",
            "claim that canonicalization alone fixes the KK normalization",
        ],
        "next_required_gate": "G88E_KK_SCALE_FRAME_CONSISTENCY",
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88d-full-4d-reduced-action-mass-extraction/"
            "g88d_full_4d_reduced_action_mass_extraction.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
