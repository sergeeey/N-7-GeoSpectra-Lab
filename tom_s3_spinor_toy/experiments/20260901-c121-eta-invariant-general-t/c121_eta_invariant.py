"""C121 -- eta(D^t) at general t, the candidate C120's own skeptic
pass surfaced. Computes the zeta-regularized eta invariant of the
torsion-deformed S^3 Dirac operator as a closed-form polynomial on the
base interval t in (0,1), via Hurwitz zeta / Bernoulli polynomials.

A first attempt at an independent numerical cross-check (naive
heat-kernel-style regularization, eps->0 extrapolation) was built,
run, found to diverge wildly against the closed form, and diagnosed:
the underlying sum is only zeta-regularized-convergent, not naive-
cutoff-convergent, so eps-extrapolation without pole subtraction is
mathematically invalid here -- removed from this script (see
decision.md for the full account, not silently dropped). Replaced
with a narrower but valid sanity check: the hand-coded Bernoulli-
polynomial arithmetic against sympy's own direct zeta() evaluation,
which catches implementation bugs (not a test of the analytic-
continuation theorem itself, a standard result).

This round does NOT extend the closed form to a neighboring interval
(crossing a spectral sign-flip requires spectral-flow-aware machinery
this round does not build, matching round116's own honest declination
to compute a formal spectral-flow integer) -- see claim.md's own
pre-registered risk section and decision.md for the honest scope.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy import Rational, Symbol, bernoulli, expand

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c121.json"

a = Symbol("a", real=True)


def zeta_H_neg_int(n_val: int, q):
    """zeta_H(-n, q) = -bernoulli(n+1, q) / (n+1), n a nonnegative int."""
    return -bernoulli(n_val + 1, q) / (n_val + 1)


def f_closed_form(a_expr):
    """f(0, a) = sum_n (m^2-1/4)*(m+a)^{-s} at s=0, m=n+3/2, via
    Hurwitz zeta at s=-2,-1,0 (the s-2,s-1,s decomposition)."""
    q = Rational(3, 2) + a_expr
    z0 = zeta_H_neg_int(0, q)  # zeta_H(0,q)
    z1 = zeta_H_neg_int(1, q)  # zeta_H(-1,q)
    z2 = zeta_H_neg_int(2, q)  # zeta_H(-2,q)
    return z2 - 2 * a_expr * z1 + (a_expr**2 - Rational(1, 4)) * z0


def eta_closed_form():
    return expand(f_closed_form(a) - f_closed_form(-a))


def zeta_H_direct(s_val, q):
    """sympy's own direct Hurwitz-zeta evaluation, independent of the
    hand-coded Bernoulli-polynomial arithmetic in zeta_H_neg_int --
    catches implementation bugs in that function specifically (not a
    test of the analytic-continuation theorem itself, which is a
    standard result, not this round's own claim)."""
    return sp.zeta(s_val, q)


def main() -> None:
    print("=== Closed-form eta(a) on base interval (via Bernoulli polynomials) ===")
    eta_cf = eta_closed_form()
    eta_cf_simplified = sp.simplify(eta_cf)
    print(f"eta(a) = {eta_cf_simplified}")

    poly = sp.Poly(eta_cf_simplified, a)
    degree = poly.degree()
    coeffs = poly.all_coeffs()  # highest degree first
    print(f"degree = {degree}, coeffs (high->low) = {coeffs}")

    even_degree_coeffs_zero = all(
        coeffs[len(coeffs) - 1 - d] == 0 for d in range(degree + 1) if d % 2 == 0
    )
    print(f"all even-degree coefficients zero (odd polynomial check): {even_degree_coeffs_zero}")

    eta_at_0 = eta_cf_simplified.subs(a, 0)
    print(f"eta(a=0) [t=1/2, should be 0, literature fact not independent check] = {eta_at_0}")

    print("\n=== Sanity check: hand-coded Bernoulli formula vs sympy's own zeta() ===")
    q_test = Rational(3, 2) + Rational(1, 2)  # a=1/2
    hand_z0 = zeta_H_neg_int(0, q_test)
    hand_z1 = zeta_H_neg_int(1, q_test)
    hand_z2 = zeta_H_neg_int(2, q_test)
    direct_z0 = sp.simplify(zeta_H_direct(0, q_test))
    direct_z1 = sp.simplify(zeta_H_direct(-1, q_test))
    direct_z2 = sp.simplify(zeta_H_direct(-2, q_test))
    sanity_matches = [hand_z0 == direct_z0, hand_z1 == direct_z1, hand_z2 == direct_z2]
    print(f"  zeta_H(0,q):  hand={hand_z0}  sympy.zeta={direct_z0}  match={sanity_matches[0]}")
    print(f"  zeta_H(-1,q): hand={hand_z1}  sympy.zeta={direct_z1}  match={sanity_matches[1]}")
    print(f"  zeta_H(-2,q): hand={hand_z2}  sympy.zeta={direct_z2}  match={sanity_matches[2]}")

    print(
        "\n=== NOTE: naive heat-kernel numerical cross-check attempted and ABANDONED as invalid ==="
    )
    print(
        "  A first attempt approximated eta(a) via sum_n mu(n)*sign(lambda)*"
        "exp(-eps*|lambda|),\n"
        "  extrapolated eps->0. This DIVERGED (differences of 5600-16800 against "
        "the closed form)\n"
        "  because mu(n)~n^2 makes the s=0 sum only conditionally/regularized-"
        "convergent -- naive\n"
        "  eps-extrapolation does not subtract the correct pole structure. This is "
        "informative, not\n"
        "  a coding bug: it is exactly why zeta-function regularization (not naive "
        "cutoff regularization)\n"
        "  is the mathematically required tool here. Removed from this script; "
        "see decision.md."
    )

    # Base-interval boundary limits (a -> 3/2^-) via closed form
    limit_base_upper = float(eta_cf_simplified.subs(a, Rational(3, 2)))
    print(f"\nBase interval closed-form value AT a=3/2 (t=1 boundary): {limit_base_upper}")

    out = {
        "eta_closed_form_expr": str(eta_cf_simplified),
        "degree": degree,
        "odd_polynomial_confirmed": bool(even_degree_coeffs_zero),
        "eta_at_a0_literature_fact": str(eta_at_0),
        "bernoulli_vs_sympy_zeta_sanity_check": {
            "zeta_H_0": {
                "hand": str(hand_z0),
                "sympy": str(direct_z0),
                "match": bool(sanity_matches[0]),
            },
            "zeta_H_neg1": {
                "hand": str(hand_z1),
                "sympy": str(direct_z1),
                "match": bool(sanity_matches[1]),
            },
            "zeta_H_neg2": {
                "hand": str(hand_z2),
                "sympy": str(direct_z2),
                "match": bool(sanity_matches[2]),
            },
        },
        "naive_heat_kernel_numerical_check": "ATTEMPTED_AND_ABANDONED_AS_INVALID -- see decision.md",
        "base_interval_closed_form_at_a_3over2_boundary": limit_base_upper,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
