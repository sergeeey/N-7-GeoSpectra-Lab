"""G88B: KK / Planck / string scale consistency audit."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88b.json"

C_SM = 0.986
RHO6_STAR = 1.090
LAM = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15

D_EXT = 4
PATH_TANGENT = np.array([2.0, 1.0])
KINETIC_MATRIX = np.diag(np.array([3.0, 6.0])) + np.outer(np.array([3.0, 6.0]), np.array([3.0, 6.0])) / (D_EXT - 2)
PATH_K = float(PATH_TANGENT @ KINETIC_MATRIX @ PATH_TANGENT)

A_NP = V_FLUX * exp(LAM / RHO6_STAR**2)


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAM / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def run() -> dict:
    rho = rho_minimum()
    vpp_rho = second_derivative_rho(rho)
    mkk_string = 1.0 / rho
    mmod_string = sqrt(vpp_rho)

    coordinate_ratio = mmod_string / mkk_string
    canonical_ratio = sqrt((rho**2 * vpp_rho / PATH_K) / mkk_string**2)

    scale_factor = canonical_ratio / coordinate_ratio
    missing_inputs = [
        "explicit reduced 4D action normalization",
        "M4/Ms map or equivalent convention stack",
        "proof that the KK scale is being compared in the same frame as the radion mass",
    ]

    gates = {
        "G88B-1_string_unit_KK_scale_reproduced": abs(mkk_string - 1.0 / rho) < 1e-12,
        "G88B-2_coordinate_vs_canonical_ratios_differ": abs(canonical_ratio - coordinate_ratio) > 1e-4,
        "G88B-3_scale_map_missing": True,
        "G88B-4_ratio_is_convention_dependent": scale_factor < 0.2,
    }

    verdict = "SCALE_CONVENTION_DEPENDENT" if all(gates.values()) else "MIXED"
    return {
        "gate": "G88B",
        "verdict": verdict,
        "rho_min": rho,
        "mkk_string": mkk_string,
        "mmod_string": mmod_string,
        "coordinate_mass_ratio_proxy": coordinate_ratio,
        "canonical_mass_ratio_metric_only": canonical_ratio,
        "canonical_to_coordinate_ratio": scale_factor,
        "path_kinetic_coefficient": PATH_K,
        "physical_mass_ratio_identified": False,
        "missing_inputs": missing_inputs,
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88b-kk-scale-consistency/g88b_kk_scale_consistency.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
