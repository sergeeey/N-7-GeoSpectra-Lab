"""G82 вЂ” canonical normalization audit for the G62 rho6 modulus."""

from __future__ import annotations

import json
from math import exp, pi, sqrt
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g82.json"

D_EXT = 4
N3 = 3
N6 = 6
PATH_TANGENT = np.array([2.0, 1.0])  # beta3 = const + 2 beta6
C_SM = 0.986
RHO_STAR = 1.090
LAMBDA_NP = 1.0 / 3.0
V_FLUX = 15 * C_SM**3 / (16 * pi)
K_VOL = 2 * pi**2 * 16 * pi**3 / 15
A_NP = V_FLUX * exp(LAMBDA_NP / RHO_STAR**2)


def kinetic_matrix() -> np.ndarray:
    dims = np.array([N3, N6], dtype=float)
    return np.diag(dims) + np.outer(dims, dims) / (D_EXT - 2)


def path_kinetic_coefficient() -> float:
    return float(PATH_TANGENT @ kinetic_matrix() @ PATH_TANGENT)


def potential(rho: float) -> float:
    return (V_FLUX - A_NP * exp(-LAMBDA_NP / rho**2)) / (K_VOL * rho**12)


def rho_minimum() -> float:
    return float(minimize_scalar(potential, bounds=(0.9, 1.5), method="bounded").x)


def second_derivative_rho(rho: float, step: float = 5e-4) -> float:
    return (potential(rho + step) - 2 * potential(rho) + potential(rho - step)) / step**2


def canonical_hessian_metric_only(rho: float) -> float:
    """dВІV/dphiВІ for phi=sqrt(G_path)*ln(rho), setting M4=1.

    At a stationary point the term proportional to dV/drho vanishes.
    """
    return rho**2 * second_derivative_rho(rho) / path_kinetic_coefficient()


def finite_difference_canonical(rho: float, step_phi: float = 5e-4) -> float:
    g = path_kinetic_coefficient()
    phi0 = sqrt(g) * np.log(rho)

    def v_phi(phi: float) -> float:
        return potential(float(np.exp(phi / sqrt(g))))

    return (v_phi(phi0 + step_phi) - 2 * v_phi(phi0) + v_phi(phi0 - step_phi)) / step_phi**2


def run() -> dict:
    rho = rho_minimum()
    vpp_rho = second_derivative_rho(rho)
    mkk2_string_proxy = 1.0 / rho**2
    old_ratio = sqrt(vpp_rho / mkk2_string_proxy)
    canonical_m2_metric_only = canonical_hessian_metric_only(rho)
    canonical_ratio_metric_only = sqrt(canonical_m2_metric_only / mkk2_string_proxy)
    finite_diff = finite_difference_canonical(rho)
    agreement = abs(finite_diff - canonical_m2_metric_only) / canonical_m2_metric_only

    gates = {
        "G82-1_path_metric_exact_90": abs(path_kinetic_coefficient() - 90.0) < 1e-12,
        "G82-2_hessian_transform_agrees": agreement < 1e-4,
        "G82-3_proxy_changes_materially": canonical_ratio_metric_only < old_ratio / 5,
        "G82-4_absolute_scale_not_identified": True,
        "G82-5_noncanonical_rescaling_changes_hessian": abs(vpp_rho - canonical_m2_metric_only) > 1e-6,
    }
    verdict = "CONDITIONAL" if all(gates.values()) else "FAIL"
    return {
        "gate": "G82",
        "verdict": verdict,
        "assumption": "4D Einstein-frame product-space kinetic metric; M4=Ms=1 only for metric-only proxy",
        "rho_min": rho,
        "path_kinetic_coefficient": path_kinetic_coefficient(),
        "coordinate_mass_ratio_proxy": old_ratio,
        "canonical_mass_ratio_metric_only": canonical_ratio_metric_only,
        "canonical_to_coordinate_ratio": canonical_ratio_metric_only / old_ratio,
        "canonical_hessian_metric_only": canonical_m2_metric_only,
        "finite_difference_canonical_hessian": finite_diff,
        "relative_agreement": agreement,
        "physical_mass_ratio_identified": False,
        "missing_inputs": [
            "explicitly normalized 4D reduced action",
            "M4/Ms scale map (or equivalent gravitational normalization)",
            "proof that the imposed rho3=C*rho6^2 path is the physical mass eigen-direction"
        ],
        "gates": gates,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260622-g82-canonical-mass/g82_canonical_mass.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
