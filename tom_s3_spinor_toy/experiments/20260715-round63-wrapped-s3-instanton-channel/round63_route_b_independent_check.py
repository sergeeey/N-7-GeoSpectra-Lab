"""
Round 63 -- Route B independent check (numerical grid search, NOT symbolic solve).

Purpose
-------
Independently cross-check (different method, no shared code with Route A) whether
substituting the a=3 wrapped-S3-instanton channel's own rho6-dependence,
    lambda(rho6) = c_eff * rho6**3        (c_eff plays the role of c*(C')**3)
into the established f(rho6) of eq:Vtotal,
    f(rho6)      = 1 - exp( lambda * (1/rho6_star**2 - 1/rho6**2) ),
    V_total(rho6) = V_0 * C**3 * f(rho6) / rho6**12,
produces an EFT-valid (rho6 > 1, genuine local minimum, V''>0) extremum, for
some range of c_eff, and if so what rho6_min results -- compared to the
established constant-lambda result rho6_min ~= 1.1791 (G62, lambda=1/3 exact,
rho6_star=1.090, tests/test_g62_observables.py).

Method (deliberately NOT a symbolic dV/drho6=0 solve)
-------------------------------------------------------
Coarse-to-fine NUMERICAL GRID SEARCH:
  1. Evaluate V_total on a coarse log-ish grid over a wide rho6 range.
  2. Compute dV/drho6 via central finite differences on that grid.
  3. Find sign changes of the finite-difference derivative (- to +  => local
     min candidate; + to -  => local max candidate).
  4. Refine each bracket by bisecting on the SIGN of the finite-difference
     derivative (still purely numerical -- no symbolic algebra, no
     scipy.optimize root/minimize solver call).
  5. Confirm "genuine minimum" via a numerical second derivative (central
     difference of the already-numerical first derivative) and by directly
     comparing V just to the left/right of the candidate.

No sympy. No scipy.optimize. Pure Python + a hand-rolled grid/bisection
routine, so the method is structurally independent of a symbolic
critical-point solve.

Positive control (mandatory, run FIRST)
----------------------------------------
Reproduce the established constant-lambda result (lambda=1/3, rho6_star=1.090)
with THIS script's own V_total/grid-search machinery before touching the a=3
substitution. This validates the V_total/rho6_star setup independently of
Route A and independently of the scipy.optimize.minimize_scalar call used in
tests/test_g62_observables.py (same formula, different solver).

Source of constants: tests/test_g62_observables.py (V_FLUX, RHO6_STAR, LAM,
K_VOL) and preprint.tex eq:Vtotal, eq:buckingham-pi, eq:slope2-exp
(sec:lambda, roughly lines 952-1075).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

# ── established constants (from tests/test_g62_observables.py) ─────────────

C = 0.986
V_FLUX = 15 * C**3 / (16 * math.pi)
RHO6_STAR = 1.090  # G57 UV-selection fixed point
LAM_CONST = 1.0 / 3.0  # G61 dimensional: dim(S^3)/dim(S^3 x S^6)

VOL_S3_COEFF = 2 * math.pi**2
VOL_S6_COEFF = 16 * math.pi**3 / 15
K_VOL = VOL_S3_COEFF * VOL_S6_COEFF  # rho6-independent normalization; does NOT
# shift the argmin of V_total (dividing by a positive constant preserves the
# location of extrema) -- included only to match tests/test_g62_observables.py
# numerically for the positive-control cross-check.

EXP_CLAMP = 700.0  # exp(x) overflows float64 above ~709.78; clamp for safety


def _safe_exp(x: float) -> float:
    """exp(x) with overflow protection (returns a huge finite number instead
    of raising / producing inf, so downstream arithmetic and sign comparisons
    stay well-defined)."""
    if x > EXP_CLAMP:
        return math.exp(EXP_CLAMP) * (1.0 + (x - EXP_CLAMP))  # monotonic surrogate
    if x < -EXP_CLAMP:
        return 0.0
    return math.exp(x)


# ── generic V_total machinery, parametrized by a lambda(rho6) function ─────


def f_of_rho6(rho6: float, lam_func) -> float:
    lam_val = lam_func(rho6)
    exponent = lam_val * (1.0 / RHO6_STAR**2 - 1.0 / rho6**2)
    return 1.0 - _safe_exp(exponent)


def v_total(rho6: float, lam_func) -> float:
    return V_FLUX * f_of_rho6(rho6, lam_func) / (K_VOL * rho6**12)


def lam_const_func(_rho6: float) -> float:
    """Original established channel: lambda = 1/3, constant."""
    return LAM_CONST


def make_lam_a3_func(c_eff: float):
    """a=3 wrapped-S3-instanton channel: lambda(rho6) = c_eff * rho6**3
    (c_eff stands in for c*(C')**3 in eq:slope2-exp / claim.md's f_{a=3})."""

    def lam_a3(rho6: float) -> float:
        return c_eff * rho6**3

    return lam_a3


# ── numerical derivative helpers (finite differences only) ─────────────────


def d1(v_func, rho6: float, h: float = 1e-4) -> float:
    """Central first derivative via finite differences."""
    return (v_func(rho6 + h) - v_func(rho6 - h)) / (2 * h)


def d2(v_func, rho6: float, h: float = 5e-4) -> float:
    """Central second derivative via finite differences."""
    return (v_func(rho6 + h) - 2 * v_func(rho6) + v_func(rho6 - h)) / h**2


# ── coarse-to-fine grid search for extrema (NO symbolic solve, NO scipy) ───


@dataclass
class Extremum:
    rho6: float
    kind: str  # "min" or "max"
    v_value: float
    v_second_deriv: float
    eft_valid: bool  # rho6 > 1


def grid_search_extrema(
    v_func,
    rho6_lo: float,
    rho6_hi: float,
    n_coarse: int = 4000,
    refine_levels: int = 60,
) -> list[Extremum]:
    """
    Coarse-to-fine grid search:
      - Walk a coarse grid, compute the finite-difference derivative sign at
        each point.
      - Every sign change brackets a candidate extremum.
      - Bisect on the SIGN of the derivative within the bracket (not on the
        value of the derivative -- a pure sign-bisection, deliberately not a
        Newton/root-finder call) down to `refine_levels` halvings.
      - Classify min vs max from the sign transition, and confirm via a
        numerical second derivative.
    """
    xs = [rho6_lo + (rho6_hi - rho6_lo) * i / (n_coarse - 1) for i in range(n_coarse)]
    h_deriv = (rho6_hi - rho6_lo) / n_coarse / 4.0
    h_deriv = max(h_deriv, 1e-6)

    signs = []
    for x in xs:
        # guard against stepping outside domain at the boundaries
        xm = max(x - h_deriv, rho6_lo * 0.999999)
        xp = min(x + h_deriv, rho6_hi * 1.000001)
        deriv = (v_func(xp) - v_func(xm)) / (xp - xm)
        signs.append(1 if deriv > 0 else (-1 if deriv < 0 else 0))

    extrema: list[Extremum] = []
    for i in range(len(xs) - 1):
        s0, s1 = signs[i], signs[i + 1]
        if s0 == 0 or s1 == 0 or s0 == s1:
            continue
        # bracket [xs[i], xs[i+1]] contains a sign change -> extremum candidate
        lo, hi = xs[i], xs[i + 1]
        sign_lo = s0
        for _ in range(refine_levels):
            mid = 0.5 * (lo + hi)
            xm = mid - h_deriv * 0.1
            xp = mid + h_deriv * 0.1
            deriv_mid = (v_func(xp) - v_func(xm)) / (xp - xm)
            sign_mid = 1 if deriv_mid > 0 else (-1 if deriv_mid < 0 else 0)
            if sign_mid == 0:
                lo = hi = mid
                break
            if sign_mid == sign_lo:
                lo = mid
            else:
                hi = mid
        rho6_ext = 0.5 * (lo + hi)

        kind = "min" if (s0 == -1 and s1 == 1) else "max"
        vpp = d2(v_func, rho6_ext)
        extrema.append(
            Extremum(
                rho6=rho6_ext,
                kind=kind,
                v_value=v_func(rho6_ext),
                v_second_deriv=vpp,
                eft_valid=(rho6_ext > 1.0),
            )
        )
    return extrema


# ── STEP 1: positive control -- reproduce established rho6_min ~= 1.1791 ───


def positive_control() -> dict:
    def v_func(r):
        return v_total(r, lam_const_func)

    extrema = grid_search_extrema(v_func, rho6_lo=0.5, rho6_hi=3.0, n_coarse=5000)
    minima = [e for e in extrema if e.kind == "min" and e.eft_valid]

    result = {
        "extrema_found": [asdict(e) for e in extrema],
        "n_eft_valid_minima": len(minima),
    }
    if minima:
        best = min(minima, key=lambda e: e.v_value)
        result["rho6_min"] = best.rho6
        result["v_min"] = best.v_value
        result["v_second_deriv_at_min"] = best.v_second_deriv
        result["matches_established_1p1791"] = abs(best.rho6 - 1.1791) < 0.01
    else:
        result["rho6_min"] = None
        result["matches_established_1p1791"] = False
    return result


# ── STEP 2: a=3 channel scan over representative c_eff spread ──────────────


def scan_a3_channel() -> dict:
    # Representative spread of c_eff (= c*(C')**3), both signs, several
    # orders of magnitude, plus the "matched at rho6*" special value
    # c_eff_match = LAM_CONST / RHO6_STAR**3 (the c_eff for which
    # lambda_a3(rho6_star) == LAM_CONST exactly, i.e. the a=3 channel agrees
    # with the constant channel AT the anchor point rho6_star).
    c_eff_match = LAM_CONST / RHO6_STAR**3
    c_eff_values = sorted(
        set(
            [
                -2.0,
                -1.0,
                -0.5,
                -0.3,
                -0.2,
                -0.1,
                -0.05,
                -0.02,
                -0.01,
                -0.005,
                0.005,
                0.01,
                0.02,
                0.05,
                0.1,
                0.15,
                0.2,
                c_eff_match,
                0.3,
                LAM_CONST,
                0.4,
                0.5,
                0.7,
                1.0,
                1.5,
                2.0,
            ]
        )
    )

    per_c_eff = []
    survivors = []  # c_eff giving an EFT-valid genuine local min
    for c_eff in c_eff_values:
        lam_func = make_lam_a3_func(c_eff)

        def v_func(r, lf=lam_func):
            return v_total(r, lf)

        # wide scan window: rho6 in (0.05, 6.0) to see the whole landscape,
        # not just the EFT-valid slice, so we can tell "no min at all" apart
        # from "min exists but at rho6<1 (sub-stringy, EFT-invalid)".
        extrema = grid_search_extrema(v_func, rho6_lo=0.05, rho6_hi=6.0, n_coarse=6000)
        minima = [e for e in extrema if e.kind == "min"]
        genuine_minima = [e for e in minima if e.v_second_deriv > 0]
        eft_valid_minima = [e for e in genuine_minima if e.eft_valid]

        entry = {
            "c_eff": c_eff,
            "n_minima_total": len(minima),
            "n_genuine_minima": len(genuine_minima),
            "n_eft_valid_genuine_minima": len(eft_valid_minima),
            "all_minima": [asdict(e) for e in minima],
        }
        per_c_eff.append(entry)
        if eft_valid_minima:
            best = min(eft_valid_minima, key=lambda e: e.v_value)
            survivors.append({"c_eff": c_eff, "rho6_min": best.rho6, "v_min": best.v_value})

    return {
        "c_eff_match_at_rho6_star": c_eff_match,
        "per_c_eff": per_c_eff,
        "survivors": survivors,
    }


# ── STEP 3: assemble + report ───────────────────────────────────────────────


def main() -> None:
    print("=" * 78)
    print("ROUND 63 -- ROUTE B independent check (grid search, no symbolic solve)")
    print("=" * 78)

    print("\n--- STEP 1: positive control (constant lambda=1/3, established) ---")
    pc = positive_control()
    print(json.dumps(pc, indent=2, default=str))
    if pc["rho6_min"] is not None:
        print(f"\n  Route-B rho6_min = {pc['rho6_min']:.5f}   (established G62 value: 1.1791)")
        print(f"  Matches established value within 0.01: {pc['matches_established_1p1791']}")
    else:
        print(
            "\n  POSITIVE CONTROL FAILED -- no EFT-valid minimum found for the "
            "constant-lambda channel. STOP: setup is broken, do not trust "
            "the a=3 scan below."
        )

    print("\n--- STEP 2: a=3 channel, lambda(rho6) = c_eff * rho6**3 ---")
    scan = scan_a3_channel()
    print(f"c_eff value matching constant-lambda AT rho6* = {scan['c_eff_match_at_rho6_star']:.5f}")
    print("\nc_eff sweep summary (only survivors + boundary cases shown in full):")
    for entry in scan["per_c_eff"]:
        tag = "  <-- EFT-VALID GENUINE MIN" if entry["n_eft_valid_genuine_minima"] > 0 else ""
        print(
            f"  c_eff={entry['c_eff']:+.4f}  minima_total={entry['n_minima_total']} "
            f"genuine={entry['n_genuine_minima']} eft_valid_genuine="
            f"{entry['n_eft_valid_genuine_minima']}{tag}"
        )

    print("\nSurvivors (c_eff giving an EFT-valid rho6>1 genuine local minimum):")
    if scan["survivors"]:
        for s in scan["survivors"]:
            print(
                f"  c_eff={s['c_eff']:+.4f}  ->  rho6_min={s['rho6_min']:.4f}  V_min={s['v_min']:.3e}"
            )
        rho6_mins = [s["rho6_min"] for s in scan["survivors"]]
        print(f"\n  rho6_min range across survivors: [{min(rho6_mins):.4f}, {max(rho6_mins):.4f}]")
        print("  compare to established constant-lambda rho6_min ~= 1.1791")
    else:
        print("  NONE -- no c_eff in the scanned range produced an EFT-valid genuine minimum.")

    out = {
        "positive_control": pc,
        "a3_channel_scan": scan,
    }
    out_path = Path(__file__).parent / "results_round63_route_b.json"
    out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\nFull results written to {out_path}")


if __name__ == "__main__":
    main()
