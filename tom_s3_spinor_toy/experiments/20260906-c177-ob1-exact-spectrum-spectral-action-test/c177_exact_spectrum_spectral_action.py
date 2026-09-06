"""C177: does the spectral action S_f(t,Lambda), computed from D^t's own
EXACT, already-established closed-form spectrum on S3 (no borrowed 4D
heat-kernel coefficients), have a genuine minimum at t=1/2, robustly
across a pre-registered family of cutoff functions f and cutoff scales
Lambda -- or does the verdict depend on which f/Lambda is chosen?

Spectrum (established in this project, NOT re-derived here):
  D^t(n, sigma) = sigma*(n + 3/2) + 3*(t - 1/2),   n = 0, 1, 2, ...
                                                     sigma = +1, -1
  multiplicity m(n) = (n+1)*(n+2)  (per sigma)
  -- round67/E2 decision.md lines 22-27 (additive shift, h_H=3);
     round67/E2 claim.md line 73 + G7's own g7_kk_spectrum.py (multiplicity).

Spectral action:
  S_f(t, Lambda) = Sum_{n, sigma} m(n) * f( D^t(n,sigma)^2 / Lambda^2 )

Analytic fact (derived here, not assumed): writing x = 3*(t-1/2), for
FIXED n the two sigma branches give lambda^2 = (a_n+x)^2 and (a_n-x)^2
with a_n=n+3/2, EQUAL multiplicity m(n) each -- so
  g_n(x) = f((a_n+x)^2/L^2) + f((a_n-x)^2/L^2)
is manifestly even in x for ANY f (swap sigma <-> -sigma is the same as
x -> -x). Hence S_f(x) = S_f(-x) for ANY f -- t=1/2 (x=0) is ALWAYS a
critical point. The decisive question is the SIGN of S_f''(0):
  d/dx[(a+x)f'(u)] with u=(a+x)^2/L^2 gives, after differentiating twice
  and setting x=0 (u_0 = a_n^2/L^2):
    S_f''(0) = Sum_n m(n) * [ (4/L^2) f'(u_0) + (8 a_n^2/L^4) f''(u_0) ]
  S_f''(0) > 0  => t=1/2 is a local MIN (Levi-Civita preferred)
  S_f''(0) < 0  => t=1/2 is a local MAX (t=0,1 preferred)
This closed form is cross-checked below against a fully independent,
mechanical sympy symbolic differentiation of a truncated sum (no shared
code path with the hand-derivation above).
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c177.json"

# ---------------------------------------------------------------------------
# Step 1: the established spectrum (reused, not re-derived)
# ---------------------------------------------------------------------------


def a_n(n: int) -> float:
    return n + 1.5


def mult_n(n: int) -> int:
    return (n + 1) * (n + 2)


def lambda_sq(n: int, sigma: int, t: float) -> float:
    x = 3.0 * (t - 0.5)
    return (sigma * a_n(n) + x) ** 2


# ---------------------------------------------------------------------------
# Step 2: three pre-registered cutoff functions, all applied to
# u = lambda^2/Lambda^2 (u >= 0 always)
# ---------------------------------------------------------------------------


def f1(u: float) -> float:
    """f(u) = exp(-u) -- standard heat-kernel-type cutoff."""
    return math.exp(-u)


def f1_prime(u: float) -> float:
    return -math.exp(-u)


def f1_double_prime(u: float) -> float:
    return math.exp(-u)


def f2(u: float) -> float:
    """f(u) = exp(-u^2) -- steeper, super-Gaussian-in-u cutoff."""
    return math.exp(-(u**2))


def f2_prime(u: float) -> float:
    return -2.0 * u * math.exp(-(u**2))


def f2_double_prime(u: float) -> float:
    return (-2.0 + 4.0 * u**2) * math.exp(-(u**2))


def _bump_h(s: float) -> float:
    return math.exp(-1.0 / s) if s > 0.0 else 0.0


def f3(u: float) -> float:
    """Smooth, COMPACTLY SUPPORTED cutoff: 1 for u<=0.25, 0 for u>=1,
    C-infinity transition in between (standard partition-of-unity bump).
    Qualitatively different regulator from f1/f2 (exactly zero beyond a
    finite mode number, not just decaying)."""
    if u <= 0.25:
        return 1.0
    if u >= 1.0:
        return 0.0
    s = (u - 0.25) / 0.75
    h_a, h_b = _bump_h(1.0 - s), _bump_h(s)
    return h_a / (h_a + h_b) if (h_a + h_b) > 0 else 0.0


CUTOFFS = {
    "f1_exp_minus_u": (f1, f1_prime, f1_double_prime),
    "f2_exp_minus_u_squared": (f2, f2_prime, f2_double_prime),
    "f3_smooth_compact": (f3, None, None),
}


# ---------------------------------------------------------------------------
# Step 3: exact (truncated, residual-checked) numeric spectral action
# ---------------------------------------------------------------------------


def spectral_action(f, t: float, lam: float, n_max: int) -> tuple[float, float]:
    """Returns (S_f(t,Lambda), truncation_residual_ratio)."""
    total = 0.0
    last_level_contribution = 0.0
    for n in range(n_max + 1):
        m = mult_n(n)
        level_total = 0.0
        for sigma in (1, -1):
            u = lambda_sq(n, sigma, t) / lam**2
            level_total += m * f(u)
        total += level_total
        last_level_contribution = level_total
    residual_ratio = abs(last_level_contribution) / abs(total) if total != 0 else 0.0
    return total, residual_ratio


def choose_n_max(lam: float) -> int:
    return max(200, math.ceil(8 * lam))


# ---------------------------------------------------------------------------
# Step 4: closed-form S_f''(0), from the hand-derivation in the module
# docstring
# ---------------------------------------------------------------------------


def s_f_double_prime_0(f_prime, f_double_prime, lam: float, n_max: int) -> float:
    total = 0.0
    for n in range(n_max + 1):
        m = mult_n(n)
        a = a_n(n)
        u0 = a**2 / lam**2
        term = (4.0 / lam**2) * f_prime(u0) + (8.0 * a**2 / lam**4) * f_double_prime(u0)
        total += m * term
    return total


def s_f_double_prime_0_finite_difference(f, lam: float, n_max: int, h: float = 1e-4) -> float:
    s_plus, _ = spectral_action(f, 0.5 + h, lam, n_max)
    s_mid, _ = spectral_action(f, 0.5, lam, n_max)
    s_minus, _ = spectral_action(f, 0.5 - h, lam, n_max)
    return (s_plus - 2.0 * s_mid + s_minus) / h**2


# ---------------------------------------------------------------------------
# Step 5: independent sympy cross-check of the hand-derived S_f''(0)
# formula (mechanical differentiation, no shared code with Step 4)
# ---------------------------------------------------------------------------


def sympy_cross_check_f1(lam_value: float, n_max_symbolic: int | None = None) -> dict:
    if n_max_symbolic is None:
        # must be large enough that exp(-a_n^2/Lambda^2) is negligible at
        # n=n_max_symbolic, else the truncated symbolic sum has NOT converged
        # and its second derivative is not comparable to the (converged)
        # numeric result -- this under-truncation was exactly the cause of
        # a spurious sign flip caught on this round's first run (see
        # decision.md).
        n_max_symbolic = min(60, math.ceil(6 * lam_value))
    t_sym, lam_sym = sp.symbols("t Lambda", positive=True, real=True)
    x_sym = 3 * (t_sym - sp.Rational(1, 2))
    total = sp.Integer(0)
    for n in range(n_max_symbolic + 1):
        a = n + sp.Rational(3, 2)
        m = (n + 1) * (n + 2)
        for sigma in (1, -1):
            u = (sigma * a + x_sym) ** 2 / lam_sym**2
            total += m * sp.exp(-u)
    second_derivative = sp.diff(total, t_sym, 2)
    # dt = (2/3) dx, so d^2/dt^2 = (dx/dt)^2 d^2/dx^2 = (1/9)... actually
    # x = 3(t-1/2) => dx/dt = 3, d^2/dx^2 = (1/9) d^2/dt^2. We want S_f''(0)
    # as defined in x (Step 4 above uses x-derivatives) -- convert:
    s_pp_in_x_from_sympy = second_derivative / 9
    value_at_half = s_pp_in_x_from_sympy.subs({t_sym: sp.Rational(1, 2), lam_sym: lam_value})
    return {
        "n_max_symbolic": n_max_symbolic,
        "sympy_S_f_pp_0_value": float(value_at_half),
    }


# ---------------------------------------------------------------------------
# Step 6: evenness check S_f(x) = S_f(-x), numeric spot-check
# ---------------------------------------------------------------------------


def evenness_spotcheck(f, lam: float, n_max: int, offsets=(0.05, 0.13, 0.37, 0.9)) -> dict:
    checks = []
    for d in offsets:
        s_plus, _ = spectral_action(f, 0.5 + d, lam, n_max)
        s_minus, _ = spectral_action(f, 0.5 - d, lam, n_max)
        rel_diff = abs(s_plus - s_minus) / max(abs(s_plus), abs(s_minus), 1e-300)
        checks.append({"t_offset": d, "S_plus": s_plus, "S_minus": s_minus, "rel_diff": rel_diff})
    return {"checks": checks, "all_even_to_1e-9": all(c["rel_diff"] < 1e-9 for c in checks)}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main() -> None:
    lambdas = [3.0, 5.0, 10.0, 20.0, 50.0]
    t_grid = [round(-1.0 + 0.0125 * k, 4) for k in range(241)]  # -1.0 .. 2.0

    results: dict = {"per_cutoff": {}}

    for cutoff_name, (f, fp, fpp) in CUTOFFS.items():
        per_lambda = {}
        for lam in lambdas:
            n_max = choose_n_max(lam)

            # (a) numeric sweep -> argmin
            values = [spectral_action(f, t, lam, n_max) for t in t_grid]
            s_values = [v[0] for v in values]
            residuals = [v[1] for v in values]
            min_idx = min(range(len(s_values)), key=lambda i: s_values[i])
            t_star = t_grid[min_idx]
            max_residual = max(residuals)

            # (b) S_f''(0): closed form (if smooth f) + finite-difference (always).
            # NOTE: s_f_double_prime_0() is derived/documented in x=3(t-1/2), while
            # the finite-difference version steps t directly -- since dx/dt=3
            # (constant), d^2/dt^2 = 9 * d^2/dx^2 (chain rule, no extra term since
            # x is affine in t). Multiply by 9 here so both are compared in the
            # SAME variable (t) -- this exact factor-of-9 mismatch was caught by
            # this round's own internal cross-check on the first run (see
            # decision.md Sec. on "genuine bug found via the round's own gate").
            fd_second_deriv = s_f_double_prime_0_finite_difference(f, lam, n_max)
            closed_form_second_deriv = (
                9.0 * s_f_double_prime_0(fp, fpp, lam, n_max) if fp is not None else None
            )

            # (c) evenness spot-check
            even_check = evenness_spotcheck(f, lam, n_max)

            entry = {
                "n_max_used": n_max,
                "max_truncation_residual_ratio": max_residual,
                "t_star_argmin": t_star,
                "S_at_t_star": s_values[min_idx],
                "S_f_double_prime_0_finite_difference": fd_second_deriv,
                "S_f_double_prime_0_closed_form": closed_form_second_deriv,
                "closed_form_vs_finite_difference_agree": (
                    abs(fd_second_deriv - closed_form_second_deriv)
                    / max(abs(fd_second_deriv), abs(closed_form_second_deriv), 1e-300)
                    < 1e-4
                    if closed_form_second_deriv is not None
                    else None
                ),
                "evenness_spotcheck": even_check,
                "t_half_is_argmin": t_star == 0.5,
                "t_zero_or_one_is_argmin": t_star in (0.0, 1.0),
            }
            per_lambda[f"Lambda_{lam}"] = entry
        results["per_cutoff"][cutoff_name] = per_lambda

    # independent sympy mechanical cross-check for f1, one Lambda value
    results["sympy_independent_cross_check_f1"] = {
        str(lam): sympy_cross_check_f1(lam) for lam in [5.0, 10.0]
    }

    # ------------------------------------------------------------------
    # aggregate verdict
    # ------------------------------------------------------------------
    all_argmins_at_half = all(
        entry["t_half_is_argmin"]
        for per_lambda in results["per_cutoff"].values()
        for entry in per_lambda.values()
    )
    all_argmins_at_zero_or_one = all(
        entry["t_zero_or_one_is_argmin"]
        for per_lambda in results["per_cutoff"].values()
        for entry in per_lambda.values()
    )
    any_internal_inconsistency = any(
        entry["closed_form_vs_finite_difference_agree"] is False
        for per_lambda in results["per_cutoff"].values()
        for entry in per_lambda.values()
    )
    # cross-check argmin vs S_f''(0) sign, per entry
    argmin_vs_sign_consistent = all(
        (entry["t_half_is_argmin"] and entry["S_f_double_prime_0_finite_difference"] > 0)
        or (entry["t_zero_or_one_is_argmin"] and entry["S_f_double_prime_0_finite_difference"] < 0)
        for per_lambda in results["per_cutoff"].values()
        for entry in per_lambda.values()
    )

    if any_internal_inconsistency or not argmin_vs_sign_consistent:
        label = "INTERNAL-INCONSISTENCY"
    elif all_argmins_at_half:
        label = "EXACT-SELECTOR-DIES-AT-HALF"
    elif all_argmins_at_zero_or_one:
        label = "EXACT-SELECTOR-CONFIRMED"
    else:
        label = "REGULATOR-DEPENDENT"

    results["verdict"] = {
        "label": label,
        "all_argmins_at_half": all_argmins_at_half,
        "all_argmins_at_zero_or_one": all_argmins_at_zero_or_one,
        "any_internal_inconsistency": any_internal_inconsistency,
        "argmin_vs_sign_consistent": argmin_vs_sign_consistent,
    }

    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(json.dumps(results["verdict"], indent=2))
    print(f"Saved: {RESULTS_PATH}")


if __name__ == "__main__":
    main()
