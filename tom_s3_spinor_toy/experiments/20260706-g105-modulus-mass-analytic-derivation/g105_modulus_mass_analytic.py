"""G105: analytic derivation of the modulus-mass power law found numerically in G103.

G103 fit m_mod ~ lambda^0.4928 by curve-fitting a numerical sweep (FITTED, not DERIVED).
This gate asks: does that exponent follow from the STRUCTURE of the potential itself,
via a small-lambda expansion -- not from any new physical input?

The potential (identical to G103/G104's run_for_lambda, just written dimensionlessly):
    V(rho) ~ [V_flux - A_np(lambda)*exp(-lambda/rho^2)] / (const * rho^n)
    A_np(lambda) = V_flux * exp(lambda/rho_star^2)   [G60's Minkowski-pearl construction]
    n = 2*N  (N = dim of the second sphere; N=6 for the S3xS6 case G103 tested)

Substituting x = rho/rho_star and mu = lambda/rho_star^2 collapses this to a
ONE-PARAMETER-FAMILY potential f(x,mu) = x^-n * [1 - exp(mu*(1 - x^-2))], independent
of V_flux/rho_star themselves (they only set the overall scale, not the shape).
NOTE: f(x,0)=0 identically for ALL x -- mu=0 is not itself a stationary point of a
well-defined minimum, it is the point where the WHOLE potential degenerates to zero
(the G60 Minkowski-uplift construction). "x0" below is lim_{mu->0} x_min(mu), obtained
from the O(mu) COEFFICIENT of f, not from f itself at mu=0 (skeptic review 2026-07-06,
FL Step 8a, caught this imprecision in the original wording -- see decision.md).

Two independent, pre-existing project results turn out to be the SAME small-mu
expansion of this ONE function:
  - G66 (2026-06-21, PROMOTE): kappa^2 = (N+1)/N -- this is x0^2 = lim_{mu->0} x_min(mu)^2,
    which is exactly mu-INDEPENDENT at leading order (ALGEBRAIC genericity: true for any n
    in this functional form -- see decision.md for the algebraic-vs-physical distinction;
    PHYSICAL genericity, i.e. that an actual S^a x S^N compactification reduces to exactly
    this potential shape for N outside the tested {6}, is NOT independently proven here --
    it is G104's own (a,N)-generalized construction, empirically checked at (a,N)=(2,6) and
    (3,6) only).
  - G103 (2026-07-05, PROMOTE): m_mod ~ lambda^0.4928 (fitted) -- this is f''(x_min(mu))
    at leading order in mu, which this gate shows is EXACTLY mu^1 (mass ~ sqrt(lambda)),
    with a computable O(mu^2) correction that accounts for the 0.4928 vs 0.500 gap.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp
from scipy.optimize import minimize_scalar

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_g105.json"
G103_RESULTS_PATH = HERE.parent / "20260705-g103-kk-lambda-blindness" / "results_g103.json"

RHO_STAR = 1.090  # same UV-selection scale as G57/G60/G103, unchanged


def leading_order_minimum(n: int) -> sp.Expr:
    """x0 = sqrt((n+2)/n) -- lim_{mu->0} x_min(mu), from the O(mu) coefficient of
    f(x,mu); f(x,0)=0 identically for all x, so this is NOT a stationary point of f
    at mu=0 itself (see module docstring)."""
    return sp.sqrt(sp.Rational(n + 2, n))


def exponent_coefficients(n: int) -> tuple[float, float]:
    """A, B such that f''(x_min(mu), mu) = A*mu + B*mu**2 + O(mu**3).

    Derived by expanding x_min(mu) = x0 + c1*mu (implicit function theorem on f_x=0),
    then substituting into f_xx and re-expanding in mu.
    """
    x, mu = sp.symbols("x mu", positive=True, real=True)
    f = x ** (-n) * (1 - sp.exp(mu * (1 - x**-2)))
    fx = sp.diff(f, x)
    fxx = sp.diff(f, x, 2)

    x0 = leading_order_minimum(n)
    c1 = sp.symbols("c1")
    xmin_ansatz = x0 + c1 * mu

    fx_series = sp.series(fx.subs(x, xmin_ansatz), mu, 0, 3).removeO()
    poly = sp.Poly(sp.expand(fx_series), mu)
    coeffs = poly.all_coeffs()[::-1]
    c1_eq = coeffs[2]  # O(mu^2) coefficient of f_x(x_min(mu)) must vanish
    c1_val = sp.solve(c1_eq, c1)[0]

    fxx_series = sp.series(fxx.subs(x, x0 + c1_val * mu), mu, 0, 3).removeO()
    fxx_poly = sp.Poly(sp.expand(fxx_series), mu)
    fxx_coeffs = fxx_poly.all_coeffs()[::-1]
    a_coeff = float(fxx_coeffs[1])
    b_coeff = float(fxx_coeffs[2]) if len(fxx_coeffs) > 2 else 0.0
    return a_coeff, b_coeff


def predicted_local_exponent(n: int, lam: float, rho_star: float = RHO_STAR) -> float:
    """d ln(m_mod) / d ln(lambda) at the given lambda, from the closed-form A,B fit."""
    a_coeff, b_coeff = exponent_coefficients(n)
    mu = lam / rho_star**2
    slope = (a_coeff + 2 * b_coeff * mu) / (a_coeff + b_coeff * mu)
    return slope / 2.0


def exact_numeric_check(n: int, lam: float, rho_star: float = RHO_STAR) -> dict:
    """Full (non-perturbative) numeric minimization, for cross-checking the expansion
    against the actual bounded optimizer G103/G104 use -- not just the series."""
    mu = lam / rho_star**2

    def f_of_x(xx: float) -> float:
        return xx ** (-n) * (1 - float(sp.exp(mu * (1 - xx**-2))))

    result = minimize_scalar(f_of_x, bounds=(0.5, 3.0), method="bounded", options={"xatol": 1e-14})
    x_min = result.x
    rho_min = x_min * rho_star
    return {"x_min": x_min, "rho_min": rho_min}


def exact_fxx_at_min(n: int, lam: float, rho_star: float = RHO_STAR) -> float:
    """f''(x_min, mu) via EXACT (non-perturbative) minimization + symbolic second
    derivative -- no series truncation anywhere. Used both for the global-fit
    cross-check (matching G103's own methodology) and for bounding the perturbative
    formula's error at the edge of G103's fit range."""
    x, mu_sym = sp.symbols("x mu", positive=True, real=True)
    f = x ** (-n) * (1 - sp.exp(mu_sym * (1 - x**-2)))
    fxx = sp.diff(f, x, 2)
    fxx_num = sp.lambdify((x, mu_sym), fxx, "numpy")

    exact = exact_numeric_check(n, lam, rho_star)
    mu = lam / rho_star**2
    return float(fxx_num(exact["x_min"], mu))


def global_fit_exponent(n: int, lam_values: list[float], rho_star: float = RHO_STAR) -> float:
    """Reproduces G103's OWN fitting methodology exactly: a log-log linear fit of
    |f''(x_min)| vs lambda over a set of sweep points, using the EXACT (non-perturbative)
    f'' at each point -- NOT the local closed-form (A,B) formula. This is the correct,
    apples-to-apples comparison to G103's 0.4928 (also a range-fit, not a local
    derivative) -- see decision.md, skeptic concern #2 (D2 methodology mismatch)."""
    logs_mu = [math.log(lam / rho_star**2) for lam in lam_values]
    logs_fpp = [math.log(abs(exact_fxx_at_min(n, lam, rho_star))) for lam in lam_values]
    npt = len(lam_values)
    mean_x = sum(logs_mu) / npt
    mean_y = sum(logs_fpp) / npt
    slope = sum((lx - mean_x) * (ly - mean_y) for lx, ly in zip(logs_mu, logs_fpp)) / sum(
        (lx - mean_x) ** 2 for lx in logs_mu
    )
    return slope / 2.0


def main() -> None:
    results: dict = {"gate": "G105", "n_tested": []}

    # --- D1: leading-order minimum reproduces G66's kappa^2=(N+1)/N for N=2..10 ---
    d1_rows = []
    for big_n in range(2, 11):
        n = 2 * big_n
        x0 = leading_order_minimum(n)
        kappa_sq_pred = float(x0**2)
        kappa_sq_target = (big_n + 1) / big_n
        d1_rows.append(
            {
                "N": big_n,
                "kappa_sq_leading_order": kappa_sq_pred,
                "kappa_sq_G66_target": kappa_sq_target,
                "match": abs(kappa_sq_pred - kappa_sq_target) < 1e-12,
            }
        )
    d1_pass = all(r["match"] for r in d1_rows)
    results["D1_leading_order_reproduces_G66"] = d1_rows
    results["D1_pass"] = d1_pass

    # --- D2: GLOBAL exact fit over G103's own sweep range, matching G103's methodology
    # exactly (log-log linear fit, same 9 lambda points) -- NOT the local closed-form
    # value at one point. Skeptic review 2026-07-06 (FL Step 8a) found the original D2
    # compared a local derivative (at lambda=1/3) to G103's range-averaged fit exponent
    # -- different observables that can agree or disagree independent of whether the
    # underlying claim is true. Fixed here to compare fit-to-fit, like-for-like.
    a_coeff, b_coeff = exponent_coefficients(12)
    results["D2_A_coefficient_N6"] = a_coeff
    results["D2_B_coefficient_N6"] = b_coeff

    g103 = json.loads(G103_RESULTS_PATH.read_text())
    g103_fit_exponent = g103["checks"]["M_modulus_exponent"]
    g103_lambda_values = [row["lambda_np"] for row in g103["sweep"]]
    this_gate_global_fit = global_fit_exponent(12, g103_lambda_values)
    d2_pass = abs(this_gate_global_fit - g103_fit_exponent) < 0.01
    results["D2_this_gate_global_fit_exponent"] = this_gate_global_fit
    results["D2_G103_fitted_exponent"] = g103_fit_exponent
    results["D2_pass"] = d2_pass

    # --- D5: perturbative (A,B closed-form) vs EXACT local exponent at the TOP of
    # G103's fit range (lambda=0.60, mu~0.505 -- NOT small) -- bounds the truncation
    # error of the O(mu^2) expansion directly, rather than only indirectly via D3's
    # rho_min check (skeptic review 2026-07-06, concern #4). ---
    lam_max = max(g103_lambda_values)
    perturbative_at_max = predicted_local_exponent(12, lam_max)
    step = 1e-4
    exact_fpp_lo = exact_fxx_at_min(12, lam_max * (1 - step))
    exact_fpp_hi = exact_fxx_at_min(12, lam_max * (1 + step))

    exact_local_slope = (math.log(abs(exact_fpp_hi)) - math.log(abs(exact_fpp_lo))) / (
        math.log(lam_max * (1 + step)) - math.log(lam_max * (1 - step))
    )
    exact_local_exponent_at_max = exact_local_slope / 2.0
    d5_pass = abs(perturbative_at_max - exact_local_exponent_at_max) < 0.02
    results["D5_perturbative_exponent_at_lambda_max"] = perturbative_at_max
    results["D5_exact_local_exponent_at_lambda_max"] = exact_local_exponent_at_max
    results["D5_pass"] = d5_pass

    # --- D3: cross-check rho_min against every point in G103's actual sweep ---
    d3_rows = []
    for row in g103["sweep"]:
        lam = row["lambda_np"]
        exact = exact_numeric_check(12, lam)
        d3_rows.append(
            {
                "lambda": lam,
                "rho_min_G103": row["rho6_min"],
                "rho_min_this_gate": exact["rho_min"],
                "diff": abs(exact["rho_min"] - row["rho6_min"]),
            }
        )
    d3_pass = all(r["diff"] < 1e-5 for r in d3_rows)
    results["D3_rho_min_cross_check"] = d3_rows
    results["D3_pass"] = d3_pass

    # --- D4: does the local exponent -> 0.5 as lambda -> 0? ---
    small_lam_exponents = [predicted_local_exponent(12, lam) for lam in [0.05, 0.02, 0.005]]
    d4_pass = (
        all(
            small_lam_exponents[i] < small_lam_exponents[i + 1]
            for i in range(len(small_lam_exponents) - 1)
        )
        and small_lam_exponents[-1] < 0.5
    )  # strictly monotonic increase toward, not past, 0.5
    results["D4_small_lambda_exponents"] = small_lam_exponents
    results["D4_pass"] = d4_pass

    verdict = "PROMOTE" if (d1_pass and d2_pass and d3_pass and d4_pass and d5_pass) else "FAIL"
    results["verdict"] = verdict

    print(f"D1 (kappa^2 leading-order = G66 for N=2..10): {d1_pass}")
    for r in d1_rows:
        print(
            f"   N={r['N']:2d}  predicted={r['kappa_sq_leading_order']:.6f}  target={r['kappa_sq_G66_target']:.6f}"
        )
    print(
        f"\nD2 (A={a_coeff:.4f}, B={b_coeff:.4f}) GLOBAL fit exponent (this gate, exact, "
        f"same 9 points as G103): {this_gate_global_fit:.4f}  vs G103's own fit: "
        f"{g103_fit_exponent:.4f}  -> {d2_pass}"
    )
    print(f"\nD3 (rho_min cross-check vs every G103 sweep point): {d3_pass}")
    for r in d3_rows:
        print(
            f"   lambda={r['lambda']:.4f}  G103={r['rho_min_G103']:.6f}  this_gate={r['rho_min_this_gate']:.6f}  diff={r['diff']:.2e}"
        )
    print(f"\nD4 (exponent -> 0.5 as lambda -> 0): {small_lam_exponents} -> {d4_pass}")
    print(
        f"\nD5 (perturbative vs exact local exponent at lambda_max={lam_max:.4f}, mu~0.5, "
        f"NOT small): perturbative={perturbative_at_max:.4f}  exact={exact_local_exponent_at_max:.4f}"
        f"  -> {d5_pass}"
    )
    print(f"\nVERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"Results -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
