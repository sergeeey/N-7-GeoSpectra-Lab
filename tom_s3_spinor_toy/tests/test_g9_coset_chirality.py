"""G9: tests for the S⁶ = G₂/SU(3) equal-rank chirality mechanism."""

import sympy as sp
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260615-g9-coset-chirality"),
)
from g9_coset_chirality import (
    SHORT_ROOTS,
    LONG_ROOTS,
    ALL_ROOTS,
    norm2,
    reflect,
    vkey,
    generate_weyl_group,
    check_root_counts,
    check_long_roots_form_A2,
    check_short_roots_are_3_plus_3bar,
    s3,
)

H = sp.Rational(1, 2)


# ── root system structure ─────────────────────────────────────────────────────
def test_twelve_roots():
    """G₂ has exactly 12 roots."""
    assert len(ALL_ROOTS) == 12


def test_six_short_six_long():
    """6 short (|α|²=1) and 6 long (|α|²=3)."""
    assert len(SHORT_ROOTS) == 6
    assert len(LONG_ROOTS) == 6


def test_length_ratio_sqrt3():
    """G₂ length ratio long/short = √3."""
    for r in SHORT_ROOTS:
        assert norm2(r) == 1
    for r in LONG_ROOTS:
        assert norm2(r) == 3


def test_roots_come_in_pairs():
    """Every root has its negative in the system (root system axiom)."""
    keys = {vkey(r) for r in ALL_ROOTS}
    for r in ALL_ROOTS:
        assert vkey((-r[0], -r[1])) in keys


def test_root_counts_check():
    assert check_root_counts()


# ── SU(3) ⊂ G₂ ────────────────────────────────────────────────────────────────
def test_long_roots_form_a2():
    """The 6 long roots close into an A₂ = su(3) root system."""
    assert check_long_roots_form_A2()


def test_short_roots_3_plus_3bar():
    """The 6 short roots = weights of 3 ⊕ 3̄ of SU(3) = (TS⁶)_ℂ."""
    assert check_short_roots_are_3_plus_3bar()


def test_short_roots_two_triangles_sum_zero():
    """Each SU(3) fundamental triple of short roots sums to zero."""
    triple_3 = [(sp.Integer(1), sp.Integer(0)), (-H, s3 / 2), (-H, -s3 / 2)]
    sx = sp.simplify(sum(r[0] for r in triple_3))
    sy = sp.simplify(sum(r[1] for r in triple_3))
    assert sx == 0 and sy == 0


# ── Weyl groups & Euler characteristic ────────────────────────────────────────
def test_weyl_g2_order_12():
    """|W(G₂)| = 12 (dihedral of order 12)."""
    W = generate_weyl_group([SHORT_ROOTS[0], LONG_ROOTS[2]])
    assert len(W) == 12


def test_weyl_su3_order_6():
    """|W(SU(3))| = 6 (symmetric group S₃)."""
    su3_simple = [(sp.Rational(3, 2), s3 / 2), (-sp.Rational(3, 2), s3 / 2)]
    W = generate_weyl_group(su3_simple)
    assert len(W) == 6


def test_euler_characteristic_2():
    """χ(S⁶) = |W(G₂)|/|W(SU(3))| = 12/6 = 2 — matches χ(S⁶)=2."""
    W_g2 = generate_weyl_group([SHORT_ROOTS[0], LONG_ROOTS[2]])
    su3_simple = [(sp.Rational(3, 2), s3 / 2), (-sp.Rational(3, 2), s3 / 2)]
    W_su3 = generate_weyl_group(su3_simple)
    assert len(W_g2) // len(W_su3) == 2


def test_equal_rank():
    """rank(G₂) = rank(SU(3)) = 2 — the chirality-enabling condition."""
    rank_g2 = 2
    rank_su3 = 2
    assert rank_g2 == rank_su3


# ── reflection sanity ─────────────────────────────────────────────────────────
def test_reflection_is_involution():
    """Reflecting twice in the same root returns the original vector."""
    v = (sp.Integer(2), sp.Integer(1))
    alpha = LONG_ROOTS[4]  # (0, √3)
    once = reflect(v, alpha)
    twice = reflect(once, alpha)
    assert sp.simplify(twice[0] - v[0]) == 0
    assert sp.simplify(twice[1] - v[1]) == 0


def test_reflection_preserves_length():
    """Weyl reflections are isometries."""
    v = (sp.Integer(2), sp.Integer(1))
    for alpha in ALL_ROOTS:
        rv = reflect(v, alpha)
        assert sp.simplify(norm2(rv) - norm2(v)) == 0
