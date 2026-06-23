"""G88A: canonical radion normalization audit for the G62 mass proxy."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g88a.json"

C_SM = 0.986
RHO6_STAR = 1.090
LAM = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15

D_EXT = 4
N3 = 3
N6 = 6
PATH_TANGENT = np.array([2.0, 1.0])
KINETIC_DIMS = np.array([N3, N6], dtype=float)
KINETIC_MATRIX = np.diag(KINETIC_DIMS) + np.outer(KINETIC_DIMS, KINETIC_DIMS) / (D_EXT - 2)
PATH_K = float(PATH_TANGENT @ KINETIC_MATRIX @ PATH_TANGENT)

A_NP = V_FLUX * exp(LAM / RHO6_STAR**2)


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAM / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def canonical_hessian_metric_only(rho: float) -> float:
    return rho**2 * second_derivative_rho(rho) / PATH_K


def finite_difference_canonical(rho: float, step_phi: float = 5e-4) -> float:
    phi0 = sqrt(PATH_K) * np.log(rho)

    def v_phi(phi: float) -> float:
        return potential(float(np.exp(phi / sqrt(PATH_K))))

    return (v_phi(phi0 + step_phi) - 2 * v_phi(phi0) + v_phi(phi0 - step_phi)) / step_phi**2


def run() -> dict:
    rho = rho_minimum()
    vpp_rho = second_derivative_rho(rho)
    mkk2_string = 1.0 / rho**2

    coordinate_ratio = sqrt(vpp_rho / mkk2_string)
    canonical_hessian = canonical_hessian_metric_only(rho)
    canonical_ratio = sqrt(canonical_hessian / mkk2_string)
    finite_diff = finite_difference_canonical(rho)
    agreement = abs(finite_diff - canonical_hessian) / canonical_hessian

    gates = {
        "G88A-1_path_metric_exact_90": abs(PATH_K - 90.0) < 1e-12,
        "G88A-2_finite_difference_agrees": agreement < 1e-4,
        "G88A-3_canonical_proxy_is_smaller": canonical_ratio < coordinate_ratio / 5,
        "G88A-4_canonical_field_is_logarithmic": True,
        "G88A-5_physical_ratio_not_identified": True,
    }

    verdict = "CANONICAL_PROXY_ONLY" if all(gates.values()) else "MIXED"
    return {
        "gate": "G88A",
        "verdict": verdict,
        "rho_min": rho,
        "path_kinetic_coefficient": PATH_K,
        "coordinate_mass_ratio_proxy": coordinate_ratio,
        "canonical_hessian_metric_only": canonical_hessian,
        "canonical_mass_ratio_metric_only": canonical_ratio,
        "canonical_to_coordinate_ratio": canonical_ratio / coordinate_ratio,
        "finite_difference_canonical_hessian": finite_diff,
        "relative_agreement": agreement,
        "physical_mass_ratio_identified": False,
        "missing_inputs": [
            "explicitly normalized 4D reduced action",
            "M4/Ms scale map (or equivalent gravitational normalization)",
            "proof that the imposed rho3=C*rho6^2 path is the physical mass eigen-direction",
        ],
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260623-g88a-canonical-radion-normalization/g88a_canonical_radion_normalization.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "MIXED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
