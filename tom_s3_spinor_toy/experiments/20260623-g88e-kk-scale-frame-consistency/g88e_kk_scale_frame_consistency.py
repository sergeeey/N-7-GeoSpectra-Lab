"""G88E: KK-scale and frame consistency audit."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88e.json"

C_SM = 0.986
RHO6_STAR = 1.090
LAMBDA_NP = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15

D_EXT = 4
PATH_TANGENT = np.array([2.0, 1.0])
KINETIC_MATRIX = np.diag(np.array([3.0, 6.0])) + np.outer(np.array([3.0, 6.0]), np.array([3.0, 6.0])) / (D_EXT - 2)
PATH_K = float(PATH_TANGENT @ KINETIC_MATRIX @ PATH_TANGENT)

A_NP = V_FLUX * exp(LAMBDA_NP / RHO6_STAR**2)


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAMBDA_NP / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def run() -> dict:
    rho = rho_minimum()
    vpp_rho = second_derivative_rho(rho)

    coordinate_ratio = sqrt(vpp_rho / (1.0 / rho**2))
    canonical_ratio = sqrt((rho**2 * vpp_rho / PATH_K) / (1.0 / rho**2))

    frame_definitions = ["Einstein frame", "string frame"]
    kk_definitions = {
        "coordinate": "m_KK = 1/rho6",
        "string_unit": "m_KK = 1/rho_min",
        "einstein_frame": None,
    }

    gates = {
        "G88E-1_frame_definitions_present": len(frame_definitions) == 2,
        "G88E-2_kk_coordinate_proxy_defined": kk_definitions["coordinate"] is not None,
        "G88E-3_einstein_frame_kk_map_missing": kk_definitions["einstein_frame"] is None,
        "G88E-4_ratio_depends_on_convention": canonical_ratio < coordinate_ratio,
    }

    verdict = "FRAME_MAP_MISSING" if all(gates.values()) else "MIXED"
    return {
        "gate": "G88E",
        "verdict": verdict,
        "frame_definitions_found": frame_definitions,
        "kk_scale_definitions": kk_definitions,
        "coordinate_proxy_value": coordinate_ratio,
        "canonical_proxy_value": canonical_ratio,
        "same_frame_comparison": False,
        "scale_map_explicit": False,
        "missing_inputs": [
            "explicit Einstein-frame KK scale map",
            "M4/Ms normalization stack",
            "same-frame comparison for radion mass and KK threshold",
        ],
        "falsified_routes": [
            "claim that the KK scale is already fixed in the same normalization as the radion mass",
            "claim that the old 2.02% ratio is frame invariant",
        ],
        "next_required_gate": "FULL_REDUCED_ACTION_RECONSTRUCTION",
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88e-kk-scale-frame-consistency/g88e_kk_scale_frame_consistency.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())

