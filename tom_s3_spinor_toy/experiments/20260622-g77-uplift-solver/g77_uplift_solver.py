"""G77 вЂ” reproducible algebraic uplift solver for the G62 toy potential."""

from __future__ import annotations

import json
from math import exp, pi
from pathlib import Path

from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g77.json"

C_SM = 0.986
F_FLUX = 15 * C_SM**3 / (16 * pi)
LAMBDA_NP = 1.0 / 3.0
RHO_TARGET = 1.090
A_FIXED = 0.3787
K_VOL = 2 * pi**2 * 16 * pi**3 / 15
POWERS = (2, 4, 6, 8)


def potential(rho: float, *, amplitude: float, uplift_d: float, power: int, k: float) -> float:
    return (F_FLUX - amplitude * exp(-LAMBDA_NP / rho**2)) / (k * rho**12) + uplift_d / rho**power


def potential_derivative(
    rho: float, *, amplitude: float, uplift_d: float, power: int, k: float
) -> float:
    b = amplitude * exp(-LAMBDA_NP / rho**2)
    numerator_derivative = -(2 * LAMBDA_NP / rho**3) * b
    base = numerator_derivative / (k * rho**12) - 12 * (F_FLUX - b) / (k * rho**13)
    uplift = -power * uplift_d / rho ** (power + 1)
    return base + uplift


def derivatives(
    rho: float, *, amplitude: float, uplift_d: float, power: int, k: float, step: float = 1e-5
) -> tuple[float, float]:
    vm = potential(rho - step, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k)
    v0 = potential(rho, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k)
    vp = potential(rho + step, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k)
    first = potential_derivative(
        rho, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k
    )
    return first, (vp - 2 * v0 + vm) / step**2


def solve_at_target(power: int, k: float) -> dict:
    rho = RHO_TARGET
    denom = (12 - power) - 2 * LAMBDA_NP / rho**2
    if abs(denom) < 1e-12:
        raise ValueError("singular target-radius uplift system")
    b = (12 - power) * F_FLUX / denom
    amplitude = b * exp(LAMBDA_NP / rho**2)
    uplift_d = (b - F_FLUX) * rho ** (power - 12) / k
    value = potential(rho, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k)
    first, second = derivatives(
        rho, amplitude=amplitude, uplift_d=uplift_d, power=power, k=k
    )
    return {
        "power": power,
        "rho0": rho,
        "B": b,
        "A_np": amplitude,
        "A_shift_vs_0p3787_percent": 100 * (amplitude / A_FIXED - 1),
        "D": uplift_d,
        "K": k,
        "V_residual": value,
        "dV_residual": first,
        "curvature": second,
        "local_minimum": second > 0,
    }


def fixed_a_equation(rho: float, power: int) -> float:
    b = A_FIXED * exp(-LAMBDA_NP / rho**2)
    return -2 * LAMBDA_NP * b + (power - 12) * (F_FLUX - b) * rho**2


def solve_with_fixed_a(power: int, k: float) -> dict:
    grid = [0.7 + 0.002 * i for i in range(701)]
    roots: list[float] = []
    left = grid[0]
    f_left = fixed_a_equation(left, power)
    for right in grid[1:]:
        f_right = fixed_a_equation(right, power)
        if f_left * f_right < 0:
            roots.append(brentq(lambda r: fixed_a_equation(r, power), left, right))
        left, f_left = right, f_right
    if len(roots) != 1:
        raise RuntimeError(f"expected one root for p={power}, found {roots}")
    rho = roots[0]
    b = A_FIXED * exp(-LAMBDA_NP / rho**2)
    uplift_d = (b - F_FLUX) * rho ** (power - 12) / k
    value = potential(rho, amplitude=A_FIXED, uplift_d=uplift_d, power=power, k=k)
    first, second = derivatives(
        rho, amplitude=A_FIXED, uplift_d=uplift_d, power=power, k=k
    )
    return {
        "power": power,
        "rho0": rho,
        "rho_shift_vs_uv_percent": 100 * (rho / RHO_TARGET - 1),
        "A_np": A_FIXED,
        "D": uplift_d,
        "K": k,
        "V_residual": value,
        "dV_residual": first,
        "curvature": second,
        "local_minimum": second > 0,
    }


def run() -> dict:
    target_k1 = [solve_at_target(p, 1.0) for p in POWERS]
    target_repo = [solve_at_target(p, K_VOL) for p in POWERS]
    fixed_k1 = [solve_with_fixed_a(p, 1.0) for p in POWERS]
    fixed_repo = [solve_with_fixed_a(p, K_VOL) for p in POWERS]

    sample = target_k1[0]
    wrong_convention_residual = potential(
        RHO_TARGET,
        amplitude=sample["A_np"],
        uplift_d=sample["D"],
        power=sample["power"],
        k=K_VOL,
    )
    rows = target_k1 + target_repo + fixed_k1 + fixed_repo
    residual_ok = all(abs(row["V_residual"]) < 1e-14 and abs(row["dV_residual"]) < 1e-10 for row in rows)
    gates = {
        "G77-1_equations_satisfied": residual_ok,
        "G77-2_reference_tables_reproduced": (
            abs(target_k1[0]["A_np"] - 0.4012) < 5e-4
            and abs(fixed_k1[0]["rho0"] - 1.1964) < 5e-4
        ),
        "G77-3_positive_stable_uplifts": all(row["D"] > 0 and row["local_minimum"] for row in rows),
        "G77-4_both_normalizations_recorded": (
            abs(target_k1[0]["D"] / target_repo[0]["D"] - K_VOL) < 1e-8
        ),
        "G77-5_wrong_normalization_control_fails": abs(wrong_convention_residual) > 1e-6,
        "G77-6_power_not_derived": True,
    }
    verdict = "PASS_ALGEBRAIC_TOY" if all(gates.values()) else "FAIL"
    return {
        "gate": "G77",
        "verdict": verdict,
        "inputs": {
            "C_SM": C_SM,
            "F_flux": F_FLUX,
            "lambda_np": LAMBDA_NP,
            "rho_target": RHO_TARGET,
            "A_fixed": A_FIXED,
            "powers": list(POWERS),
            "K_vol": K_VOL,
        },
        "target_radius": {"K_1": target_k1, "K_repo": target_repo},
        "fixed_amplitude": {"K_1": fixed_k1, "K_repo": fixed_repo},
        "negative_control_wrong_K_residual": wrong_convention_residual,
        "gates": gates,
        "microscopic_uplift_derived": False,
        "reproduction_command": (
            "python tom_s3_spinor_toy/experiments/"
            "20260622-g77-uplift-solver/g77_uplift_solver.py"
        ),
    }


def main() -> int:
    results = run()
    RESULTS_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if results["verdict"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
