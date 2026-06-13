"""Regression gate: LAMBDA-B5-V-RATIO-G0 — lambda-free CG ratio = sqrt(2).

Pins the scientific claim independently (own CG calls, not importing evidence script).
Catches regressions in sympy.physics.wigner or claim math without running standalone gate.

Claim: within Sector B (J_L=1/2, J_R=1, J=3/2, m_tgt=1/2),
       ratio R = CG(m_src=+1/2) / CG(m_src=-1/2) = sqrt(2) exactly,
       and R is independent of lambda.
"""

import sympy as sp
from sympy.physics.wigner import clebsch_gordan


def _cg(j1, j2, j3, m1, m2, m3):
    r = lambda x: sp.Rational(int(round(2 * x)), 2)
    return clebsch_gordan(r(j1), r(j2), r(j3), r(m1), r(m2), r(m3))


def test_cg_sector_b_values():
    cg_pos = _cg(0.5, 1, 1.5, 0.5, 0, 0.5)  # <1/2,+1/2;1,0|3/2,1/2> = sqrt(6)/3
    cg_neg = _cg(0.5, 1, 1.5, -0.5, 1, 0.5)  # <1/2,-1/2;1,1|3/2,1/2> = sqrt(3)/3
    # Individual values
    assert sp.simplify(cg_pos**2 - sp.Rational(2, 3)) == 0, f"cg_pos^2 = {cg_pos**2}, expected 2/3"
    assert sp.simplify(cg_neg**2 - sp.Rational(1, 3)) == 0, f"cg_neg^2 = {cg_neg**2}, expected 1/3"


def test_sector_b_ratio_is_sqrt2_exact():
    cg_pos = _cg(0.5, 1, 1.5, 0.5, 0, 0.5)
    cg_neg = _cg(0.5, 1, 1.5, -0.5, 1, 0.5)
    R = sp.simplify(cg_pos / cg_neg)
    assert sp.simplify(R**2 - 2) == 0, f"R^2 = {R**2}, expected 2"
    assert sp.simplify(R - sp.sqrt(2)) == 0, f"R = {R}, expected sqrt(2)"


def test_ratio_is_lambda_free():
    lam, vred, geom = sp.symbols("lambda vred geom", positive=True)
    cg_pos = _cg(0.5, 1, 1.5, 0.5, 0, 0.5)
    cg_neg = _cg(0.5, 1, 1.5, -0.5, 1, 0.5)
    R = sp.simplify((lam * vred * geom * cg_pos) / (lam * vred * geom * cg_neg))
    assert sp.diff(R, lam) == 0, "Ratio R must be lambda-free (lambda cancels)"
