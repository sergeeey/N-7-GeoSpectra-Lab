"""S6-HARM-G4: pytest pins for Dirac spectrum on S⁶.

Key results:
  Christoffel Γ^{φ₁}_{φ₁β₁} = cot(β₁)  [G1 metric, ρ-independent]
  Riemann R^{φ₁}_{β₁φ₁β₁} = 1           [mixed component, ρ-independent]
  Sectional curvature K(β₁,φ₁) = 1/ρ²   [round sphere confirmation]
  Scalar curvature R = 30/ρ²              [n(n-1)/ρ² = 6·5/ρ²]
  Lichnerowicz: |λ₀|² = 9/ρ² > R/4 = 15/(2ρ²) ✓
  Killing spinors: 8 = 2^3 = G0 weight count ✓
  Spectrum: ±(l+3)/ρ for l = 0, 1, 2, ...
  Tom S³ analog: min eigenvalue ratio S⁶/S³ = 2 = n(S⁶)/n(S³)
"""

import pytest
from sympy import cos, sin, cot, symbols, simplify, trigsimp, diff, Rational, Integer


@pytest.fixture(scope="module")
def s6_dirac():
    b1, rho = symbols(r"\beta_1 \rho", real=True, positive=True)
    n = 6

    g_b1 = rho**2
    g_p1 = rho**2 * sin(b1) ** 2

    Chr_p1_p1b1 = trigsimp(Rational(1, 2) / g_p1 * diff(g_p1, b1))
    Chr_b1_p1p1 = trigsimp(-Rational(1, 2) / g_b1 * diff(g_p1, b1))

    term2 = trigsimp(-diff(Chr_p1_p1b1, b1))
    term4 = trigsimp(-Chr_p1_p1b1 * Chr_p1_p1b1)
    Riemann_mixed = trigsimp(term2 + term4)

    Riemann_covariant = g_p1 * Riemann_mixed
    K = trigsimp(Riemann_covariant / (g_b1 * g_p1))

    R_scalar = n * (n - 1) / rho**2
    Lich_bound = R_scalar / 4
    lambda0_sq = Rational(n * n, 4) / rho**2
    excess = simplify(lambda0_sq - Lich_bound)

    killing_count = 2 ** (n // 2)
    g0_weights = [(s1, s2, s3) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]

    spectrum_pos = [Rational(lv + n // 2, 1) / rho for lv in range(4)]

    n_s3 = 3
    lambda0_s3 = Rational(n_s3, 2) / rho
    lambda0_s6 = Rational(n, 2) / rho
    ratio = simplify(lambda0_s6 / lambda0_s3)

    return {
        "b1": b1,
        "rho": rho,
        "n": n,
        "g_b1": g_b1,
        "g_p1": g_p1,
        "Chr_p1_p1b1": Chr_p1_p1b1,
        "Chr_b1_p1p1": Chr_b1_p1p1,
        "Riemann_mixed": Riemann_mixed,
        "K": K,
        "R_scalar": R_scalar,
        "Lich_bound": Lich_bound,
        "lambda0_sq": lambda0_sq,
        "excess": excess,
        "killing_count": killing_count,
        "g0_weights": g0_weights,
        "spectrum_pos": spectrum_pos,
        "lambda0_s3": lambda0_s3,
        "lambda0_s6": lambda0_s6,
        "ratio": ratio,
    }


# ── T1: Christoffel symbols ───────────────────────────────────────────────────
def test_s6_chr_phi1_phi1_beta1_is_cotbeta1(s6_dirac):
    """Γ^{φ₁}_{φ₁β₁} = cot(β₁): log-derivative of g_{φ₁φ₁} wrt β₁."""
    b1 = s6_dirac["b1"]
    assert trigsimp(s6_dirac["Chr_p1_p1b1"] - cot(b1)) == Integer(0)


def test_s6_chr_beta1_phi1phi1_formula(s6_dirac):
    """Γ^{β₁}_{φ₁φ₁} = −sin(β₁)cos(β₁): centripetal Christoffel."""
    b1 = s6_dirac["b1"]
    assert trigsimp(s6_dirac["Chr_b1_p1p1"] + sin(b1) * cos(b1)) == Integer(0)


# ── T2: Riemann tensor ────────────────────────────────────────────────────────
def test_s6_riemann_mixed_equals_1(s6_dirac):
    """R^{φ₁}_{β₁φ₁β₁} = 1: unit mixed Riemann component (ρ-independent)."""
    assert s6_dirac["Riemann_mixed"] == Integer(1)


# ── T3: Sectional curvature ───────────────────────────────────────────────────
def test_s6_sectional_curvature_is_1_over_rho2(s6_dirac):
    """K(β₁,φ₁) = 1/ρ²: S⁶ with radius ρ has constant sectional curvature."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["K"] - 1 / rho**2) == Integer(0)


# ── T4: Scalar curvature ──────────────────────────────────────────────────────
def test_s6_scalar_curvature_30_over_rho2(s6_dirac):
    """R = 30/ρ²: scalar curvature n(n-1)/ρ² with n=6."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["R_scalar"] - 30 / rho**2) == Integer(0)


# ── T5: Lichnerowicz ──────────────────────────────────────────────────────────
def test_s6_lichnerowicz_bound_is_15_over_2rho2(s6_dirac):
    """Lichnerowicz bound R/4 = 15/(2ρ²)."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["Lich_bound"] - Rational(15, 2) / rho**2) == Integer(0)


def test_s6_ground_state_satisfies_lichnerowicz(s6_dirac):
    """Ground state |λ₀|² = 9/ρ² > 15/(2ρ²): excess = 3/(2ρ²) > 0."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["excess"] - Rational(3, 2) / rho**2) == Integer(0)


def test_s6_ground_state_lambda0_sq(s6_dirac):
    """Ground state |λ₀|² = (n/2)²/ρ² = 9/ρ²."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["lambda0_sq"] - 9 / rho**2) == Integer(0)


# ── T6: Killing spinors ───────────────────────────────────────────────────────
def test_s6_killing_spinor_count_is_8(s6_dirac):
    """Killing spinor count = 2^{n/2} = 2³ = 8 for S⁶."""
    assert s6_dirac["killing_count"] == 8


def test_s6_killing_count_matches_g0_weights(s6_dirac):
    """8 Killing spinors = 8 G0 weight vectors (±½,±½,±½) of SO(6) spinor rep."""
    assert s6_dirac["killing_count"] == len(s6_dirac["g0_weights"])


def test_s6_g0_weight_vectors_are_8(s6_dirac):
    """G0 weight vectors (±½,±½,±½): enumerate all 2³=8 sign combinations."""
    weights = s6_dirac["g0_weights"]
    assert len(weights) == 8
    # Each weight has 3 components, each ±1 (stored as ±1 for convenience)
    assert all(len(w) == 3 for w in weights)
    assert all(abs(c) == 1 for w in weights for c in w)


# ── T7: Spectrum ──────────────────────────────────────────────────────────────
def test_s6_spectrum_l0_is_3_over_rho(s6_dirac):
    """Dirac spectrum l=0: λ = ±3/ρ (Killing spinors)."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["spectrum_pos"][0] - 3 / rho) == Integer(0)


def test_s6_spectrum_l1_is_4_over_rho(s6_dirac):
    """Dirac spectrum l=1: λ = ±4/ρ."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["spectrum_pos"][1] - 4 / rho) == Integer(0)


def test_s6_spectrum_l2_is_5_over_rho(s6_dirac):
    """Dirac spectrum l=2: λ = ±5/ρ."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["spectrum_pos"][2] - 5 / rho) == Integer(0)


# ── T8: Tom Lawrence S³ analog ────────────────────────────────────────────────
def test_s6_tom_s3_lambda0_is_3_over_2rho(s6_dirac):
    """S³ Dirac minimum eigenvalue = 3/(2ρ): Tom Lawrence analog."""
    rho = s6_dirac["rho"]
    assert simplify(s6_dirac["lambda0_s3"] - Rational(3, 2) / rho) == Integer(0)


def test_s6_over_s3_eigenvalue_ratio_is_2(s6_dirac):
    """Minimum eigenvalue ratio S⁶/S³ = 2 = n(S⁶)/n(S³) = 6/3."""
    assert s6_dirac["ratio"] == Integer(2)
