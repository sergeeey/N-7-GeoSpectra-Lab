"""G106: pre-registered third-point confirmation of G105's closed-form formulas at N=7.

G105 proved analytically (small-lambda expansion) that kappa^2=(N+1)/N and the modulus-mass
exponent's leading order + O(lambda) correction are ALGEBRAIC properties of the potential's
functional form, for any N. Skeptic review (FL Step 8a, G105 decision.md) flagged that this
had only been checked NUMERICALLY at N=6 (both (a,N)=(2,6) and (3,6) -- G104/G105's own two
tested points share the same N). PHYSICAL genericity -- that G104's (a,N)-generalized
construction actually reduces to the assumed potential shape at a genuinely different N --
was not independently confirmed.

This gate closes that gap with N=7 (a=2), lambda=1/3 (the project's canonical reference
value, used everywhere else): a point NEVER touched by any prior gate.

Protocol (pre-registration, AOG-1): the PREDICTED values below were computed and written
down BEFORE running G104's actual (2,7) numerical minimization -- see decision.md for the
literal transcript order. This script re-derives the same predictions from G105's own
functions and then runs G104's own machinery fresh, so the comparison is reproducible by
anyone re-running this file, not just a one-off transcript claim.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g106.json"

G105_SCRIPT = (
    HERE.parent / "20260706-g105-modulus-mass-analytic-derivation" / "g105_modulus_mass_analytic.py"
)
G104_SCRIPT = HERE.parent / "20260705-g104-h1-h2-s2xs6" / "g104_h1_h2_s2xs6.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


G105 = _load("g105_modulus_mass_analytic", G105_SCRIPT)
G104 = _load("g104_h1_h2_s2xs6", G104_SCRIPT)

BIG_N = 7
SMALL_N = 2 * BIG_N  # n=14, the "n" convention used throughout G105
LAM = 1.0 / 3.0  # canonical reference value (G62/G66/G103/G104's own positive controls)


def predicted() -> dict:
    """G105's closed-form predictions for (BIG_N, LAM) -- computed from G105's OWN
    functions only, no reference to G104's numeric machinery."""
    x0 = G105.leading_order_minimum(SMALL_N)
    kappa_sq = float(x0**2)
    mass_exponent = G105.predicted_local_exponent(SMALL_N, LAM)
    return {"kappa_sq": kappa_sq, "mass_exponent": mass_exponent}


def actual() -> dict:
    """G104's own (a,N)-generalized numerical machinery, run fresh at (a,N)=(2,7)."""
    result = G104.run_for_lambda(2, BIG_N, LAM)
    step = 1e-4
    lam_lo, lam_hi = LAM * (1 - step), LAM * (1 + step)
    r_lo = G104.run_for_lambda(2, BIG_N, lam_lo)
    r_hi = G104.run_for_lambda(2, BIG_N, lam_hi)
    local_exponent = (math.log(r_hi["m_mod"]) - math.log(r_lo["m_mod"])) / (
        math.log(lam_hi) - math.log(lam_lo)
    )
    return {
        "exists": result["exists"],
        "kappa_sq": result["kappa_sq"],
        "rho_min": result["rho_min"],
        "mass_exponent_local": local_exponent,
    }


def main() -> None:
    pred = predicted()
    act = actual()

    kappa_diff = abs(act["kappa_sq"] - pred["kappa_sq"])
    kappa_pass = kappa_diff < 1e-2  # same absolute bar G104 itself used for its own (a,N) tests

    exponent_diff = abs(act["mass_exponent_local"] - pred["mass_exponent"])
    exponent_pass = exponent_diff < 0.02  # same bar as G105's own D5 check

    verdict = "PROMOTE" if (act["exists"] and kappa_pass and exponent_pass) else "FAIL"

    results = {
        "gate": "G106",
        "point_tested": {"a": 2, "N": BIG_N, "lambda": LAM},
        "predicted": pred,
        "actual": act,
        "kappa_diff": kappa_diff,
        "kappa_pass": kappa_pass,
        "exponent_diff": exponent_diff,
        "exponent_pass": exponent_pass,
        "verdict": verdict,
    }

    print(f"Point tested: (a,N)=(2,{BIG_N}), lambda={LAM:.6f} -- never touched by any prior gate")
    print("\nPREDICTED (from G105's closed-form formulas, computed first):")
    print(f"  kappa^2 = {pred['kappa_sq']:.6f}")
    print(f"  mass exponent (local, at lambda=1/3) = {pred['mass_exponent']:.4f}")
    print("\nACTUAL (from G104's own numerical machinery, run after):")
    print(f"  kappa^2 = {act['kappa_sq']:.6f}   diff={kappa_diff:.6f}  -> {kappa_pass}")
    print(
        f"  mass exponent (local) = {act['mass_exponent_local']:.4f}   diff={exponent_diff:.4f}  -> {exponent_pass}"
    )
    print(f"\nVERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"Results -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
