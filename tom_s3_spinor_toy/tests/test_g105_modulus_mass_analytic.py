import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260706-g105-modulus-mass-analytic-derivation"
    / "g105_modulus_mass_analytic.py"
)
SPEC = importlib.util.spec_from_file_location("g105_modulus_mass_analytic", SCRIPT)
assert SPEC and SPEC.loader
G105 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(G105)

G103_RESULTS = (
    ROOT
    / "tom_s3_spinor_toy"
    / "experiments"
    / "20260705-g103-kk-lambda-blindness"
    / "results_g103.json"
)


def test_leading_order_minimum_matches_g66_for_n6():
    """D1 (N=6, the case G66/G103/G104 all use): x0^2 must equal exactly 7/6."""
    x0 = G105.leading_order_minimum(12)
    assert abs(float(x0**2) - 7.0 / 6.0) < 1e-12


def test_leading_order_minimum_matches_g66_for_all_n():
    """D1 (general): x0^2 = (N+1)/N for N=2..10 -- G66's formula is not special to N=6."""
    for big_n in range(2, 11):
        x0 = G105.leading_order_minimum(2 * big_n)
        target = (big_n + 1) / big_n
        assert abs(float(x0**2) - target) < 1e-12


def test_global_fit_exponent_matches_g103_fit():
    """D2 (fixed after skeptic review 2026-07-06): this gate's GLOBAL log-log fit,
    computed the SAME way G103 computed its own fit (range fit over the same 9 lambda
    points, exact non-perturbative f''), must land within 0.01 of G103's 0.4928.
    Comparing a local derivative to a range-fit (the original, flawed D2) is NOT done
    here -- that mismatch was the skeptic's strongest finding."""
    g103 = json.loads(G103_RESULTS.read_text())
    g103_fit = g103["checks"]["M_modulus_exponent"]
    lam_values = [row["lambda_np"] for row in g103["sweep"]]
    this_gate_fit = G105.global_fit_exponent(12, lam_values)
    assert abs(this_gate_fit - g103_fit) < 0.01


def test_perturbative_formula_accurate_at_top_of_fit_range():
    """D5: the closed-form (A,B) perturbative exponent must stay close to the EXACT
    local exponent even at the least-favorable point (lambda=0.60, mu~0.5 -- not a
    small parameter) -- otherwise the O(mu^2) truncation could not be trusted across
    G103's actual sweep range. Added after skeptic review 2026-07-06 (concern #4:
    convergence away from lambda->0 was previously checked only indirectly via D3)."""
    lam_max = 0.60
    perturbative = G105.predicted_local_exponent(12, lam_max)
    step = 1e-4
    fpp_lo = G105.exact_fxx_at_min(12, lam_max * (1 - step))
    fpp_hi = G105.exact_fxx_at_min(12, lam_max * (1 + step))
    import math

    exact_slope = (math.log(abs(fpp_hi)) - math.log(abs(fpp_lo))) / (
        math.log(lam_max * (1 + step)) - math.log(lam_max * (1 - step))
    )
    exact_exponent = exact_slope / 2.0
    assert abs(perturbative - exact_exponent) < 0.02


def test_rho_min_reproduces_every_g103_sweep_point():
    """D3: this gate's independent sympy+scipy reimplementation must reproduce EVERY
    point of G103's own 9-point sweep to within 1e-5 -- an independent cross-check,
    not a reuse of G103's own code."""
    g103 = json.loads(G103_RESULTS.read_text())
    for row in g103["sweep"]:
        exact = G105.exact_numeric_check(12, row["lambda_np"])
        assert abs(exact["rho_min"] - row["rho6_min"]) < 1e-5


def test_exponent_approaches_half_as_lambda_shrinks():
    """D4: the predicted local exponent must approach 0.5 monotonically as lambda
    shrinks -- the mark of a genuine asymptotic limit, not a fitting artifact."""
    exponents = [G105.predicted_local_exponent(12, lam) for lam in [0.10, 0.03, 0.005]]
    assert exponents[0] < exponents[1] < exponents[2] < 0.5
    assert exponents[-1] > 0.499


def test_exponent_coefficients_are_deterministic():
    """Regression pin: A and B for N=6 must be stable, non-zero, and of the sign that
    gives a POSITIVE mass^2 for positive lambda (A>0, since mass^2 ~ A*mu at leading
    order and mu=lambda/rho_star^2>0 for physical lambda)."""
    a_coeff, b_coeff = G105.exponent_coefficients(12)
    assert a_coeff > 0
    assert abs(a_coeff - 8.158) < 0.01
    assert b_coeff != 0
