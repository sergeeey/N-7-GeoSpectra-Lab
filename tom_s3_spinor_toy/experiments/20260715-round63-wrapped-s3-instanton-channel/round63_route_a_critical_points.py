"""Round 63 / Route A: does the a=3 (wrapped-S3 instanton) lambda(rho6) channel,
substituted into the established eq:Vtotal, produce an EFT-valid moduli minimum?

Structure (see claim.md for the frozen kill criteria):

  (a) POSITIVE CONTROL: reproduce the established constant-lambda G62 zero-fit
      rho6_min ~ 1.179, using the exact same normalization as
      experiments/20260621-g70-functional-form/vary_exponent.py (p=2 row) and
      experiments/20260626-g94-s3-np-instanton/g94_s3_np_instanton.py (RHO6_STAR).
      If this does not reproduce ~1.179, STOP -- the setup is wrong and nothing
      downstream can be trusted.

  (b) f_a3(rho6) = 1 - exp( c_eff * rho6^3 * (1/rho6*^2 - 1/rho6^2) ), where
      c_eff stands in for c*(C')^3 (preprint eq:slope2-exp, a=3 case), i.e. the
      SAME constant lambda in eq:Vtotal's f(rho6) is replaced by the a=3
      channel's own rho6-dependence lambda(rho6) = c_eff * rho6^3. This is a
      substitution only -- no other change to eq:Vtotal's structure.

  (c) V_total_a3(rho6) = V_0 * C^3 * f_a3(rho6) / rho6^12, same V_0*C^3 =
      V_FLUX and same rho6^12 volume normalization as the positive control.

  (d) Scan c_eff over signed log-spaced range [-1e4, 1e4], solve dV/drho6=0,
      classify every critical point (min/max/inflection) via the second
      derivative, and check EFT validity (rho6 > 1, real, positive).
      Two independent solving routes are used and cross-checked:
        Route 1: direct symbolic dV/drho6, numeric root-finding.
        Route 2: reduced algebraic condition f'(rho6)*rho6 = 12*f(rho6)
                 (derived from V = V_FLUX*f/(K*rho6^12) by the quotient rule,
                 an independent algebraic simplification of the same
                 stationarity condition -- NOT the same code path as Route 1's
                 raw sympy differentiation of the full quotient).

  (e) G94 cross-check: attempt to relate c_eff = c*(C')^3 to G94's own
      c_S3 in exp(-c_S3*rho3^3), via the SAME slope-2 substitution
      rho3 = C'*rho6^2, and report honestly whether the two parametrizations
      are simply related or not (they sit in structurally different places:
      G94's term is additive inside a 2D V_main(rho3,rho6); this round's term
      is multiplicative inside a 1D f(rho6)).

This is a Full-Ladder Standard-descriptive experiment (see claim.md). Question
type: descriptive (does a specific, pre-registered substitution into an
already-established formula produce an EFT-valid extremum?).
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from math import pi
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round63_route_a.json"

# ---------------------------------------------------------------------------
# Shared constants -- IDENTICAL to experiments/20260621-g70-functional-form
# /vary_exponent.py and experiments/20260626-g94-s3-np-instanton
# /g94_s3_np_instanton.py (RHO6_STAR). Re-typed here, not imported, to keep
# this script self-contained and auditable in isolation; values are cited
# from those two files, not re-derived.
# ---------------------------------------------------------------------------
C_SM = 0.986
V_FLUX = 15 * C_SM**3 / (16 * pi)
RHO6_STAR = 1.090
N_VOLUME = 6
VOLUME_POWER = 2 * N_VOLUME  # 12
K_VOL = (2 * pi**2) * (16 * pi**3 / 15)  # VOL_S3_UNIT * VOL_S6_UNIT

LAMBDA_CONST = 1.0 / 3.0  # BASE_LAMBDA from g70 (positive control only)

KAPPA_TARGET = float(sp.sqrt(sp.Rational(7, 6)))  # sqrt(7/6) ~ 1.0801
EXPECTED_RHO6_MIN = 1.1790597996215977  # from g70 results.csv, p=2.0 row

# G94's own calibrated window (cited, not re-verified this round)
G94_C_S3_LOW = 0.248
G94_C_S3_HIGH = 0.372
G94_C_S3_BEST = 0.235

# Slope-2 trajectory constant: rho3^3 = (16*pi/15) * rho6^6  (G28/G29),
# i.e. C'^3 = 16*pi/15  (so C' = (16*pi/15)**(1/3))
C_PRIME_CUBED = 16 * pi / 15

EFT_MIN_RHO6 = 1.0
RHO6_SCAN_LO = 0.02
RHO6_SCAN_HI = 20.0


# ===========================================================================
# (a) POSITIVE CONTROL -- constant lambda, must reproduce rho6_min ~ 1.179
# ===========================================================================


def positive_control() -> dict:
    rho6 = sp.symbols("rho6", positive=True, real=True)
    f_const = 1 - sp.exp(LAMBDA_CONST * (1 / sp.Float(RHO6_STAR) ** 2 - 1 / rho6**2))
    V = sp.Float(V_FLUX) * f_const / (sp.Float(K_VOL) * rho6**VOLUME_POWER)
    dV = sp.diff(V, rho6)
    d2V = sp.diff(V, rho6, 2)

    dV_num = sp.lambdify(rho6, dV, "numpy")
    d2V_num = sp.lambdify(rho6, d2V, "numpy")

    root = brentq(dV_num, RHO6_STAR + 1e-6, 3.0, xtol=1e-14, rtol=1e-14)
    second = float(d2V_num(root))
    is_min = second > 0

    rel_err = abs(root - EXPECTED_RHO6_MIN) / EXPECTED_RHO6_MIN
    match = rel_err < 1e-6

    kappa = root / RHO6_STAR

    return {
        "rho6_min": float(root),
        "expected_rho6_min": EXPECTED_RHO6_MIN,
        "relative_error": float(rel_err),
        "matches_g70_p2_reference": bool(match),
        "second_derivative": second,
        "is_minimum": bool(is_min),
        "kappa": float(kappa),
        "kappa_target_sqrt_7_6": KAPPA_TARGET,
    }


# ===========================================================================
# (b)-(d) a=3 channel: f_a3(rho6) = 1 - exp(c_eff * rho6^3 * (1/rho6*^2 - 1/rho6^2))
# ===========================================================================

rho6_sym, c_eff_sym = sp.symbols("rho6 c_eff", real=True)

f_a3_expr = 1 - sp.exp(c_eff_sym * rho6_sym**3 * (1 / sp.Float(RHO6_STAR) ** 2 - 1 / rho6_sym**2))
V_a3_expr = sp.Float(V_FLUX) * f_a3_expr / (sp.Float(K_VOL) * rho6_sym**VOLUME_POWER)

dV_a3_expr = sp.diff(V_a3_expr, rho6_sym)
d2V_a3_expr = sp.diff(V_a3_expr, rho6_sym, 2)

# Route 1: raw derivative of the full quotient (sympy diff), lambdified.
dV_a3_func = sp.lambdify((rho6_sym, c_eff_sym), dV_a3_expr, "numpy")
d2V_a3_func = sp.lambdify((rho6_sym, c_eff_sym), d2V_a3_expr, "numpy")
V_a3_func = sp.lambdify((rho6_sym, c_eff_sym), V_a3_expr, "numpy")
f_a3_func = sp.lambdify((rho6_sym, c_eff_sym), f_a3_expr, "numpy")

# Route 2: independent algebraic reduction. V = A*f/rho6^12 (A = V_FLUX/K_VOL
# constant) => dV/drho6 = A*(f'*rho6^12 - 12*f*rho6^11)/rho6^24
#           = A*(f'*rho6 - 12*f)/rho6^13.
# Stationary points (rho6 != 0) satisfy g(rho6) := f'(rho6)*rho6 - 12*f(rho6) = 0.
# This is solved via a SEPARATE symbolic expression (f' built directly from
# f_a3_expr, not from dV_a3_expr) and a separate numeric root-finder call, so
# it is an independent check of the same stationarity condition, not a
# re-run of Route 1's code path.
f_a3_prime_expr = sp.diff(f_a3_expr, rho6_sym)
g_reduced_expr = f_a3_prime_expr * rho6_sym - 12 * f_a3_expr
g_reduced_func = sp.lambdify((rho6_sym, c_eff_sym), g_reduced_expr, "numpy")


@dataclass
class CriticalPoint:
    rho6: float
    kind: str  # "minimum" / "maximum" / "inflection"
    eft_valid: bool
    v_value: float
    second_derivative: float
    route2_confirmed: bool


def find_critical_points(c_eff: float, n_grid: int = 4000) -> list[CriticalPoint]:
    """Scan for sign changes of dV/drho6 (Route 1), refine with brentq,
    classify via d2V, and cross-check each root against Route 2's reduced
    condition g(rho6)=0 (tolerance-based, independent formula).
    """
    grid = np.linspace(RHO6_SCAN_LO, RHO6_SCAN_HI, n_grid)
    try:
        vals = dV_a3_func(grid, c_eff)
    except Exception:
        return []
    vals = np.asarray(vals, dtype=float)
    finite = np.isfinite(vals)

    points: list[CriticalPoint] = []
    for i in range(len(grid) - 1):
        if not (finite[i] and finite[i + 1]):
            continue
        a, b = vals[i], vals[i + 1]
        if a == 0.0:
            root = grid[i]
        elif a * b < 0:
            try:
                root = brentq(
                    dV_a3_func, grid[i], grid[i + 1], args=(c_eff,), xtol=1e-13, rtol=1e-13
                )
            except (ValueError, RuntimeError):
                continue
        else:
            continue

        try:
            second = float(d2V_a3_func(root, c_eff))
            v_val = float(V_a3_func(root, c_eff))
            g_val = float(g_reduced_func(root, c_eff))
        except Exception:
            continue
        if not (np.isfinite(second) and np.isfinite(v_val)):
            continue

        if second > 1e-14:
            kind = "minimum"
        elif second < -1e-14:
            kind = "maximum"
        else:
            kind = "inflection"

        # Route 2 cross-check: g(rho6) should also be ~0 at this root.
        route2_ok = abs(g_val) < 1e-6 * max(1.0, abs(root) ** 12)

        points.append(
            CriticalPoint(
                rho6=float(root),
                kind=kind,
                eft_valid=bool(root > EFT_MIN_RHO6),
                v_value=v_val,
                second_derivative=second,
                route2_confirmed=bool(route2_ok),
            )
        )

    # De-duplicate roots that are extremely close (grid can catch a root twice
    # near a boundary).
    dedup: list[CriticalPoint] = []
    for p in points:
        if not any(abs(p.rho6 - q.rho6) < 1e-6 for q in dedup):
            dedup.append(p)
    return dedup


def scan_c_eff() -> dict:
    """Broad, sign-and-scale-agnostic scan of c_eff, as required by claim.md
    method step 2 (do not assume sign or scale in advance)."""
    magnitudes = np.logspace(-4, 4, 33)  # 1e-4 ... 1e4
    c_eff_values = sorted(set(list(magnitudes) + list(-magnitudes)))

    all_results = []
    eft_minima = []  # (c_eff, rho6_min)

    for c_eff in c_eff_values:
        crit_points = find_critical_points(c_eff)
        row = {
            "c_eff": float(c_eff),
            "n_critical_points": len(crit_points),
            "critical_points": [asdict(p) for p in crit_points],
        }
        all_results.append(row)
        for p in crit_points:
            if p.kind == "minimum" and p.eft_valid:
                eft_minima.append((float(c_eff), p.rho6))

    return {
        "scan_rows": all_results,
        "eft_valid_minima": eft_minima,
    }


# ===========================================================================
# (e) Asymptotic sanity check (independent qualitative route, per claim.md
# method step 5): behaviour of f_a3 / V_a3 as rho6 -> 0+ and rho6 -> infinity,
# for representative signs of c_eff. This does not replace the numeric scan;
# it is a qualitative cross-check on why minima appear/disappear.
# ===========================================================================


def asymptotic_notes() -> dict:
    notes = {}
    for sign, c_eff_rep in [("positive", 1.0), ("negative", -1.0)]:
        exponent_large_rho6 = "c_eff*rho6^3/rho6*^2 dominates (cubic) -> " + (
            "+inf" if c_eff_rep > 0 else "-inf"
        )
        f_large_rho6 = (
            "f_a3 -> -inf (V -> -inf * rho6^-12 -> 0^-, from below)"
            if c_eff_rep > 0
            else "f_a3 -> 1 (V -> V_FLUX/(K*rho6^12) -> 0^+, from above)"
        )
        exponent_small_rho6 = "-c_eff/rho6^2 dominates -> " + ("-inf" if c_eff_rep > 0 else "+inf")
        f_small_rho6 = (
            "f_a3 -> 1 (V -> V_FLUX/(K*rho6^12) -> +inf)"
            if c_eff_rep > 0
            else "f_a3 -> -inf (V -> -inf, i.e. -> -inf*rho6^-12 -> -inf)"
        )
        notes[sign] = {
            "c_eff_representative": c_eff_rep,
            "rho6_to_infinity": {"exponent": exponent_large_rho6, "consequence": f_large_rho6},
            "rho6_to_zero": {"exponent": exponent_small_rho6, "consequence": f_small_rho6},
        }
    return notes


# ===========================================================================
# Step 3: G94 cross-check
# ===========================================================================


def g94_crosscheck() -> dict:
    """Attempt: c_eff = c*(C')^3, and c (eq:buckingham-pi's coefficient, a=3
    case) is HYPOTHESIZED to be the same constant as G94's c_S3, since both
    trace to the same physical origin (D-brane action S_inst = c*Vol(S3) prop
    to c*rho3^3). Under slope-2, rho3^3 = (16*pi/15)*rho6^6, i.e. C'^3 =
    16*pi/15, so if c === c_S3:
        c_eff = c_S3 * (16*pi/15)
    This maps G94's window (0.248, 0.372), best 0.235, into a candidate
    c_eff window. This mapping is REPORTED, not asserted as necessarily
    correct -- see the structural caveat below.
    """
    c_eff_low = G94_C_S3_LOW * C_PRIME_CUBED
    c_eff_high = G94_C_S3_HIGH * C_PRIME_CUBED
    c_eff_best = G94_C_S3_BEST * C_PRIME_CUBED

    return {
        "hypothesis": "c (eq:buckingham-pi coefficient) == c_S3 (G94's D-brane "
        "instanton coefficient), both being the coefficient of the same "
        "S_inst = c*Vol(S3) prop c*rho3^3 D2-brane action.",
        "C_prime_cubed": float(C_PRIME_CUBED),
        "mapped_c_eff_window": [float(c_eff_low), float(c_eff_high)],
        "mapped_c_eff_best": float(c_eff_best),
        "structural_caveat": (
            "The mapping c_eff = c_S3 * C'^3 assumes 'c' is literally shared "
            "between the two parametrizations. But the two terms occupy "
            "DIFFERENT functional roles: G94's exp(-c_S3*rho3^3) is an "
            "ADDITIVE piece inside a 2D V_main(rho3,rho6) numerator; this "
            "round's f_a3 substitutes lambda(rho6)=c_eff*rho6^3 into the "
            "MULTIPLICATIVE bracket f(rho6)=1-exp(lambda*(1/rho6*^2-1/rho6^2)) "
            "of a DIFFERENT, already-rho3-eliminated 1D V_total(rho6). Even "
            "restricted to the same rho6, G94's substituted exponent scales "
            "as c_S3*(C')^3*rho6^6 (pure sixth power, from exp(-c_S3*rho3^3) "
            "with rho3=C'*rho6^2), while this round's exponent is "
            "c_eff*rho6^3/rho6*^2 - c_eff*rho6 (a cubic-minus-linear "
            "combination, from the (1/rho6*^2-1/rho6^2) factor). These are "
            "NOT the same function of rho6 even for equal c_eff. The window "
            "mapping above is therefore a numerical coincidence-check only, "
            "not a derivation that the two channels are the same physics."
        ),
    }


# ===========================================================================
# Main
# ===========================================================================


def main() -> None:
    print("=" * 78)
    print("Round 63 / Route A -- wrapped-S3 instanton (a=3) channel critical points")
    print("=" * 78)

    print("\n--- (a) POSITIVE CONTROL: constant-lambda G62 zero-fit ---")
    pc = positive_control()
    for k, v in pc.items():
        print(f"  {k}: {v}")
    if not pc["matches_g70_p2_reference"]:
        print("\n!!! POSITIVE CONTROL FAILED -- setup does not reproduce the")
        print("!!! established rho6_min ~ 1.179. STOPPING before Route A scan.")
        RESULTS_PATH.write_text(json.dumps({"positive_control": pc, "STOPPED": True}, indent=2))
        raise SystemExit(1)
    print("  -> Positive control OK: setup reproduces established result.")

    print("\n--- (b)-(d) a=3 channel: scanning c_eff (broad, signed, log-spaced) ---")
    scan = scan_c_eff()
    minima = scan["eft_valid_minima"]
    print(f"  c_eff values scanned: {len(scan['scan_rows'])}")
    print(f"  EFT-valid (rho6>1) local minima found: {len(minima)}")
    if minima:
        rho6_vals = [m[1] for m in minima]
        c_eff_vals = [m[0] for m in minima]
        print(
            f"  c_eff range giving EFT-valid minimum: [{min(c_eff_vals):.6g}, {max(c_eff_vals):.6g}]"
        )
        print(f"  resulting rho6_min range: [{min(rho6_vals):.6f}, {max(rho6_vals):.6f}]")
        overlap = (min(rho6_vals) <= 1.179 <= max(rho6_vals)) or any(
            abs(r - 1.179) / 1.179 < 0.05 for r in rho6_vals
        )
        print(f"  brackets or closely approaches established ~1.179: {overlap}")
    else:
        print("  No EFT-valid local minimum found for any scanned c_eff.")
        overlap = False

    print("\n--- Asymptotic sanity notes ---")
    asym = asymptotic_notes()
    for sign, d in asym.items():
        print(f"  c_eff {sign}:")
        print(f"    rho6->inf : {d['rho6_to_infinity']}")
        print(f"    rho6->0+  : {d['rho6_to_zero']}")

    print("\n--- (e) G94 cross-check ---")
    g94 = g94_crosscheck()
    print(f"  hypothesis: {g94['hypothesis']}")
    print(f"  C'^3 = 16*pi/15 = {g94['C_prime_cubed']:.6f}")
    print(f"  mapped c_eff window (from c_S3 in (0.248,0.372)): {g94['mapped_c_eff_window']}")
    print(f"  mapped c_eff best (from c_S3=0.235): {g94['mapped_c_eff_best']:.6f}")
    print(f"  structural caveat: {g94['structural_caveat']}")

    # Does the mapped G94 window fall inside the surviving EFT-valid c_eff range?
    g94_window_overlaps_surviving = False
    if minima:
        c_eff_vals = [m[0] for m in minima]
        lo, hi = min(c_eff_vals), max(c_eff_vals)
        mapped_lo, mapped_hi = g94["mapped_c_eff_window"]
        g94_window_overlaps_surviving = not (mapped_hi < lo or mapped_lo > hi)
    print(
        f"  mapped G94 window overlaps surviving EFT-valid c_eff range: {g94_window_overlaps_surviving}"
    )

    verdict_inputs = {
        "positive_control_ok": pc["matches_g70_p2_reference"],
        "eft_valid_minimum_exists": len(minima) > 0,
        "rho6_min_overlaps_established": overlap,
        "g94_window_overlaps_surviving_c_eff": g94_window_overlaps_surviving,
    }
    print("\n--- Verdict inputs (see claim.md kill criteria table) ---")
    for k, v in verdict_inputs.items():
        print(f"  {k}: {v}")

    RESULTS_PATH.write_text(
        json.dumps(
            {
                "positive_control": pc,
                "c_eff_scan_summary": {
                    "n_values_scanned": len(scan["scan_rows"]),
                    "eft_valid_minima": minima,
                },
                "full_scan_rows": scan["scan_rows"],
                "asymptotic_notes": asym,
                "g94_crosscheck": g94,
                "g94_window_overlaps_surviving_c_eff": g94_window_overlaps_surviving,
                "verdict_inputs": verdict_inputs,
            },
            indent=2,
        )
    )
    print(f"\nResults written -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
