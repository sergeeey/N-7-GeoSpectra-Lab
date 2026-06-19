"""S6-HARM-G3: pytest pins for separation of variables on S⁶.

Key results:
  Δ = L₁ + (1/cos²β₁)[L₂ + (1/cos²β₂)L₃]
  L₃ = S² Laplacian: eigenvalues −l(l+1) on Legendre polynomials
  Separation is exact (diagonal metric → no cross β terms)
  Nested ODEs: l₃ → l₂ → λ (cotβ_k artifacts from G2 enter as centrifugal terms)
"""

import pytest
import sympy as sp
from sympy import cos, sin, symbols, simplify, trigsimp


@pytest.fixture(scope="module")
def s6_ops():
    b1, b2, b3 = symbols(r"\beta_1 \beta_2 \beta_3", real=True, positive=True)
    p1, p2, p3 = symbols(r"\phi_1 \phi_2 \phi_3", real=True, positive=True)

    sqrt_g = sin(b1) * cos(b1) ** 4 * sin(b2) * cos(b2) ** 2 * sin(b3)
    params = [b1, p1, b2, p2, b3, p3]
    g_inv = [
        sp.Integer(1),
        1 / sin(b1) ** 2,
        1 / cos(b1) ** 2,
        1 / (cos(b1) ** 2 * sin(b2) ** 2),
        1 / (cos(b1) ** 2 * cos(b2) ** 2),
        1 / (cos(b1) ** 2 * cos(b2) ** 2 * sin(b3) ** 2),
    ]

    def laplacian(f):
        result = sp.Integer(0)
        for k, q in enumerate(params):
            flux = sqrt_g * g_inv[k] * sp.diff(f, q)
            result += sp.diff(flux, q)
        return trigsimp(result / sqrt_g)

    def L3(f):
        return trigsimp(sp.diff(sin(b3) * sp.diff(f, b3), b3) / sin(b3))

    def L2(f):
        return trigsimp(
            sp.diff(sin(b2) * cos(b2) ** 2 * sp.diff(f, b2), b2) / (sin(b2) * cos(b2) ** 2)
        )

    def L1(f):
        return trigsimp(
            sp.diff(sin(b1) * cos(b1) ** 4 * sp.diff(f, b1), b1) / (sin(b1) * cos(b1) ** 4)
        )

    return {
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "laplacian": laplacian,
        "L1": L1,
        "L2": L2,
        "L3": L3,
    }


# ── T1: Nested Laplacian structure ───────────────────────────────────────────
def test_s6_laplacian_cosb3_is_L3_over_cos2(s6_ops):
    """Δ(cosβ₃) = L₃(cosβ₃)/(cos²β₁ cos²β₂): nested form for β₃-only function."""
    b1, b2, b3 = s6_ops["b1"], s6_ops["b2"], s6_ops["b3"]
    delta = s6_ops["laplacian"](cos(b3))
    expected = s6_ops["L3"](cos(b3)) / (cos(b1) ** 2 * cos(b2) ** 2)
    assert trigsimp(delta - expected) == 0


def test_s6_laplacian_sinb1sq_is_L1(s6_ops):
    """Δ(sin²β₁) = L₁(sin²β₁): nested form for β₁-only function."""
    b1 = s6_ops["b1"]
    delta = s6_ops["laplacian"](sin(b1) ** 2)
    L1_val = s6_ops["L1"](sin(b1) ** 2)
    assert trigsimp(delta - L1_val) == 0


def test_s6_laplacian_sinb2sq_is_L2_over_cos2(s6_ops):
    """Δ(sin²β₂) = L₂(sin²β₂)/cos²β₁: nested form for β₂-only function."""
    b1, b2 = s6_ops["b1"], s6_ops["b2"]
    delta = s6_ops["laplacian"](sin(b2) ** 2)
    L2_val = s6_ops["L2"](sin(b2) ** 2)
    assert trigsimp(delta - L2_val / cos(b1) ** 2) == 0


# ── T2: L₃ = S² Laplacian eigenvalues ───────────────────────────────────────
def test_s6_L3_P0_eigenvalue_zero(s6_ops):
    """L₃(1) = 0: l₃=0 eigenvalue."""
    assert simplify(s6_ops["L3"](sp.Integer(1))) == 0


def test_s6_L3_P1_eigenvalue_minus2(s6_ops):
    """L₃(cosβ₃) = −2cosβ₃: l₃=1, eigenvalue −l(l+1)=−2."""
    b3 = s6_ops["b3"]
    assert trigsimp(s6_ops["L3"](cos(b3)) + 2 * cos(b3)) == 0


def test_s6_L3_P2_eigenvalue_minus6(s6_ops):
    """L₃(P₂(cosβ₃)) = −6P₂: l₃=2, eigenvalue −6."""
    b3 = s6_ops["b3"]
    P2 = (3 * cos(b3) ** 2 - 1) / 2
    assert trigsimp(s6_ops["L3"](P2) + 6 * P2) == 0


# ── T3: Exact separation (no cross β terms) ──────────────────────────────────
def test_s6_separation_b1b2_product(s6_ops):
    """Δ(sin²β₁·sin²β₂) = L₁(sin²β₁)·sin²β₂ + sin²β₁·L₂(sin²β₂)/cos²β₁."""
    b1, b2 = s6_ops["b1"], s6_ops["b2"]
    f = sin(b1) ** 2 * sin(b2) ** 2
    delta = s6_ops["laplacian"](f)
    expected = (
        sin(b2) ** 2 * s6_ops["L1"](sin(b1) ** 2)
        + sin(b1) ** 2 * s6_ops["L2"](sin(b2) ** 2) / cos(b1) ** 2
    )
    assert trigsimp(delta - expected) == 0


def test_s6_separation_b1b3_product(s6_ops):
    """Δ(sin²β₁·cosβ₃) separates into L₁ and L₃ terms with no cross contribution."""
    b1, b2, b3 = s6_ops["b1"], s6_ops["b2"], s6_ops["b3"]
    f = sin(b1) ** 2 * cos(b3)
    delta = s6_ops["laplacian"](f)
    expected = cos(b3) * s6_ops["L1"](sin(b1) ** 2) + sin(b1) ** 2 * s6_ops["L3"](cos(b3)) / (
        cos(b1) ** 2 * cos(b2) ** 2
    )
    assert trigsimp(delta - expected) == 0


def test_s6_separation_three_way_product(s6_ops):
    """Δ(sin²β₁·sin²β₂·cosβ₃) = sum of L₁, L₂, L₃ terms — exact separation."""
    b1, b2, b3 = s6_ops["b1"], s6_ops["b2"], s6_ops["b3"]
    A1, A2, A3 = sin(b1) ** 2, sin(b2) ** 2, cos(b3)
    delta = s6_ops["laplacian"](A1 * A2 * A3)
    expected = trigsimp(
        A2 * A3 * s6_ops["L1"](A1)
        + A1 * A3 * s6_ops["L2"](A2) / cos(b1) ** 2
        + A1 * A2 * s6_ops["L3"](A3) / (cos(b1) ** 2 * cos(b2) ** 2)
    )
    assert trigsimp(delta - expected) == 0


# ── T4: Nesting — l₃ eigenvalue feeds into L₂ ODE ──────────────────────────
def test_s6_nesting_l3_feeds_into_l2(s6_ops):
    """Δ(sin²β₁·sinβ₂·cosβ₃) matches ODE decomposition with L₃(cosβ₃)=−2cosβ₃."""
    b1, b2, b3 = s6_ops["b1"], s6_ops["b2"], s6_ops["b3"]
    A1, A2, A3 = sin(b1) ** 2, sin(b2), cos(b3)
    delta = s6_ops["laplacian"](A1 * A2 * A3)
    expected = trigsimp(
        s6_ops["L1"](A1) * A2 * A3
        + A1 * s6_ops["L2"](A2) * A3 / cos(b1) ** 2
        + A1 * A2 * s6_ops["L3"](A3) / (cos(b1) ** 2 * cos(b2) ** 2)
    )
    assert trigsimp(delta - expected) == 0


# ── T5: L₁ structural formula ────────────────────────────────────────────────
def test_s6_L1_on_sin2b1(s6_ops):
    """L₁(sin²β₁) = 14cos²β₁ − 10: structural formula check."""
    b1 = s6_ops["b1"]
    result = s6_ops["L1"](sin(b1) ** 2)
    expected = 14 * cos(b1) ** 2 - 10
    assert trigsimp(result - expected) == 0, f"got {trigsimp(result)}"


def test_s6_L1_constant_kernel(s6_ops):
    """L₁(1) = 0: constants are in the kernel of L₁."""
    assert simplify(s6_ops["L1"](sp.Integer(1))) == 0


def test_s6_L1_L1sin2_plus_L1cos2_zero(s6_ops):
    """L₁(sin²β₁) + L₁(cos²β₁) = L₁(1) = 0: linearity check."""
    b1 = s6_ops["b1"]
    total = trigsimp(s6_ops["L1"](sin(b1) ** 2) + s6_ops["L1"](cos(b1) ** 2))
    assert simplify(total) == 0
