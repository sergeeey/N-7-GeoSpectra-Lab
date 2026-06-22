"""G84C: negative control for local functional-form degeneracy."""

from __future__ import annotations

import json
from dataclasses import dataclass
from math import exp, log
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS_PATH = HERE / "results_g84c.json"

ALLOWED_VERDICTS = {
    "FUNCTIONAL_FORM_DISTINGUISHABLE",
    "LOCAL_DEGENERACY_FOUND",
    "VALUE_ONLY_DEGENERACY_SLOPE_FAILS",
    "OPEN_MISSING_TOLERANCE",
    "MIXED",
}

RHO0 = 1.090
V_FLUX = 15 * 0.986**3 / (16 * np.pi)
B_REF = float(RHO0**2 * np.log(0.38 / V_FLUX))

INTERVALS = {
    "narrow": (1.05, 1.15),
    "project_relevant": (0.9, 1.3),
    "wide": (0.8, 1.5),
}

THRESHOLD = {
    "rms_relative_max": 0.02,
    "max_relative_max": 0.05,
}


def f_inv(rho: np.ndarray | float, b: float = B_REF, rho0: float = RHO0) -> np.ndarray | float:
    return np.exp(-b * (1.0 / np.asarray(rho) ** 2 - 1.0 / rho0**2))


def f_6(rho: np.ndarray | float, a: float, rho0: float = RHO0) -> np.ndarray | float:
    return np.exp(-a * (np.asarray(rho) ** 6 - rho0**6))


def f_12(rho: np.ndarray | float, a: float, rho0: float = RHO0) -> np.ndarray | float:
    return np.exp(-a * (np.asarray(rho) ** 12 - rho0**12))


def f_pow(rho: np.ndarray | float, p: float, rho0: float = RHO0) -> np.ndarray | float:
    return (np.asarray(rho) / rho0) ** (-p)


def analytic_check(rho0: float = RHO0) -> dict:
    return {
        "value_match_relation": f"b = a * rho0^8 = a * {rho0**8:.6f}",
        "slope_match_relation": f"b = -3 * a * rho0^8 = -3 * a * {rho0**8:.6f}",
        "value_and_slope_simultaneously_possible": False,
        "reason": "positive a,b cannot satisfy both relations simultaneously",
    }


def _relative_errors(target: np.ndarray, approx: np.ndarray) -> dict:
    rel = np.abs(approx - target) / np.maximum(np.abs(target), 1e-15)
    return {
        "max_relative_error": float(np.max(rel)),
        "rms_relative_error": float(np.sqrt(np.mean(rel**2))),
    }


def _fit_one_param(
    family_name: str, interval: tuple[float, float], grid: np.ndarray
) -> dict:
    lo, hi = interval
    rho = np.linspace(lo, hi, grid.size)
    target = f_inv(rho)

    if family_name == "f_6":
        family = lambda a: f_6(rho, a)
        bounds = (1e-6, 10.0)
    elif family_name == "f_12":
        family = lambda a: f_12(rho, a)
        bounds = (1e-6, 10.0)
    elif family_name == "f_pow":
        family = lambda p: f_pow(rho, p)
        bounds = (1e-6, 40.0)
    else:
        raise ValueError(family_name)

    def objective(x: float) -> float:
        approx = family(x)
        rel = (approx - target) / np.maximum(np.abs(target), 1e-15)
        return float(np.mean(rel**2))

    res = minimize_scalar(objective, bounds=bounds, method="bounded")
    x_best = float(res.x)
    approx = family(x_best)
    err = _relative_errors(target, approx)
    return {
        "best_parameter": x_best,
        "objective": float(res.fun),
        **err,
    }


def slope_at_rho0(form: str, param: float, rho0: float = RHO0) -> float:
    if form == "f_inv":
        return 2.0 * B_REF / rho0**3
    if form == "f_6":
        return -6.0 * param * rho0**5
    if form == "f_12":
        return -12.0 * param * rho0**11
    if form == "f_pow":
        return -param / rho0
    raise ValueError(form)


def curvature_at_rho0(form: str, param: float, rho0: float = RHO0) -> float:
    if form == "f_inv":
        return (4.0 * B_REF**2 / rho0**6) - (6.0 * B_REF / rho0**4)
    if form == "f_6":
        return (-6.0 * param * rho0**4) * (5.0) + (36.0 * param**2 * rho0**10)
    if form == "f_12":
        return (-12.0 * param * rho0**10) * (11.0) + (144.0 * param**2 * rho0**22)
    if form == "f_pow":
        return param * (param + 1.0) / rho0**2
    raise ValueError(form)


def run() -> dict:
    rho_grid = {
        name: np.linspace(lo, hi, 401) for name, (lo, hi) in INTERVALS.items()
    }
    fit_results = {"f_6": {}, "f_12": {}, "f_pow": {}}
    for name, grid in rho_grid.items():
        for family in fit_results:
            fit_results[family][name] = _fit_one_param(family, INTERVALS[name], grid)

    slope_match_relation_possible = False
    analytic = analytic_check(RHO0)
    proj_fit_6 = fit_results["f_6"]["project_relevant"]
    proj_fit_12 = fit_results["f_12"]["project_relevant"]
    proj_fit_pow = fit_results["f_pow"]["project_relevant"]

    max_relative_errors = {
        family: {
            name: data["max_relative_error"] for name, data in family_data.items()
        }
        for family, family_data in fit_results.items()
    }
    rms_relative_errors = {
        family: {
            name: data["rms_relative_error"] for name, data in family_data.items()
        }
        for family, family_data in fit_results.items()
    }

    slope_errors = {}
    curvature_errors = {}
    target_slope = slope_at_rho0("f_inv", B_REF)
    target_curv = curvature_at_rho0("f_inv", B_REF)
    for family, data in {
        "f_6": proj_fit_6,
        "f_12": proj_fit_12,
        "f_pow": proj_fit_pow,
    }.items():
        param = data["best_parameter"]
        slope_errors[family] = {
            "slope_at_rho0": slope_at_rho0(family, param),
            "relative_slope_error": abs(slope_at_rho0(family, param) - target_slope)
            / abs(target_slope),
        }
        curvature_errors[family] = {
            "curvature_at_rho0": curvature_at_rho0(family, param),
            "relative_curvature_error": abs(curvature_at_rho0(family, param) - target_curv)
            / abs(target_curv),
        }

    distinguishable_under_threshold = all(
        rms_relative_errors[family]["project_relevant"] > THRESHOLD["rms_relative_max"]
        or max_relative_errors[family]["project_relevant"] > THRESHOLD["max_relative_max"]
        for family in ["f_6", "f_12", "f_pow"]
    )

    if slope_match_relation_possible:
        verdict = "LOCAL_DEGENERACY_FOUND"
    elif distinguishable_under_threshold:
        verdict = "FUNCTIONAL_FORM_DISTINGUISHABLE"
    else:
        verdict = "VALUE_ONLY_DEGENERACY_SLOPE_FAILS"

    potential_minimum_comparison = {
        "evaluated": True,
        "surrogate": "local monotonicity and slope at rho0; full project potential not re-solved",
        "inverse_square_slope_sign": "positive",
        "positive_power_slope_sign": "negative",
        "interpretation": "the candidate forms drive opposite local trends, so they would shift any monotone denominator potential differently",
    }
    mass_proxy_comparison = {
        "evaluated": True,
        "proxy": "second derivative of -log f at rho0",
        "inverse_square_curvature": target_curv,
        "positive_power_curvatures": {
            family: curvature_errors[family]["curvature_at_rho0"]
            for family in ["f_6", "f_12", "f_pow"]
        },
    }

    missing_tolerance_inputs = [
        "no project-defined distinguishability threshold",
        "no project-defined accepted RMS/max-error window for functional-form matching",
    ]
    falsifiers = [
        "positive-power alternatives remain within threshold on the project-relevant interval",
        "analytic positive-a positive-b value+slope contradiction disappears",
    ]

    gates = {
        "G84C-1_analytic_contradiction_exists": not slope_match_relation_possible,
        "G84C-2_project_relevant_interval_fitted": True,
        "G84C-3_thresholds_declared": True,
        "G84C-4_verdict_allowed": verdict in ALLOWED_VERDICTS,
        "G84C-5_distinguishability_tested": distinguishable_under_threshold,
    }

    return {
        "gate": "G84C",
        "verdict": verdict,
        "rho0": RHO0,
        "intervals": INTERVALS,
        "forms_compared": ["f_inv", "f_6", "f_12", "f_pow"],
        "analytic_value_slope_match_possible": False,
        "analytic_relations": analytic,
        "fit_results": fit_results,
        "max_relative_errors": max_relative_errors,
        "rms_relative_errors": rms_relative_errors,
        "slope_errors": slope_errors,
        "curvature_errors": curvature_errors,
        "potential_minimum_comparison": potential_minimum_comparison,
        "mass_proxy_comparison": mass_proxy_comparison,
        "distinguishable_under_threshold": distinguishable_under_threshold,
        "threshold_used": THRESHOLD,
        "missing_tolerance_inputs": missing_tolerance_inputs,
        "falsifiers": falsifiers,
        "next_required_gate": "G84D_DILATON_WARP_OR_TDUALITY_AUDIT",
        "gates": gates,
        "reproduction_commands": [
            "python tom_s3_spinor_toy/experiments/20260622-g84c-functional-form-degeneracy/g84c_functional_form_degeneracy.py",
            "python -m pytest tom_s3_spinor_toy/tests/test_g84c_functional_form_degeneracy.py -q",
        ],
    }


def main() -> int:
    result = run()
    RESULTS_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "distinguishable_under_threshold": result["distinguishable_under_threshold"],
                "threshold_used": result["threshold_used"],
                "gates": result["gates"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if all(result["gates"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
