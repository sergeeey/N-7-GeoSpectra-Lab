"""S6-HARM-G2: pytest pins for cotβ_k structure in SO(6) root generators.

Tom S³ analog:
  Row 13: ∂_θ + ∂_θ̃ = Î_{3L}  (Cartan = pure azimuthal)
  Row 15: cot(2α) = Hopf-frame artifact

S⁶ result:
  Cartan L₁₂ = ∂_{φ₁}   [pure azimuthal, no cotangent]
  Root   L₁₃: c_{φ₁} = cotβ₁ sinβ₂ cosφ₂ sinφ₁  [frame artifact]
  Root   L₃₅: c_{φ₂} = cotβ₂ sinβ₃ cosφ₃ sinφ₂  [frame artifact]
  Root   L₁₅: c_{φ₁} = cotβ₁ cosβ₂ sinβ₃ cosφ₃ sinφ₁
"""

import pytest
import sympy as sp
from sympy import cos, sin, cot, tan, symbols, simplify, trigsimp


# ── Shared setup ──────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def s6_setup():
    rho, b1, b2, b3, p1, p2, p3 = symbols(
        r"\rho \beta_1 \beta_2 \beta_3 \phi_1 \phi_2 \phi_3", real=True, positive=True
    )

    x = [
        rho * sin(b1) * cos(p1),
        rho * sin(b1) * sin(p1),
        rho * cos(b1) * sin(b2) * cos(p2),
        rho * cos(b1) * sin(b2) * sin(p2),
        rho * cos(b1) * cos(b2) * sin(b3) * cos(p3),
        rho * cos(b1) * cos(b2) * sin(b3) * sin(p3),
        rho * cos(b1) * cos(b2) * cos(b3),
    ]

    params = [b1, p1, b2, p2, b3, p3]

    g_inv = [
        1 / rho**2,
        1 / (rho**2 * sin(b1) ** 2),
        1 / (rho**2 * cos(b1) ** 2),
        1 / (rho**2 * cos(b1) ** 2 * sin(b2) ** 2),
        1 / (rho**2 * cos(b1) ** 2 * cos(b2) ** 2),
        1 / (rho**2 * cos(b1) ** 2 * cos(b2) ** 2 * sin(b3) ** 2),
    ]

    J = sp.Matrix([[sp.diff(xi, q) for q in params] for xi in x])

    def L_coeff(i: int, j: int) -> list:
        return [trigsimp(g_inv[k] * (x[i] * J[j, k] - x[j] * J[i, k])) for k in range(6)]

    return {
        "rho": rho,
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "L_coeff": L_coeff,
    }


# ── T1: L₁₂ = ∂_{φ₁} (Cartan, pure azimuthal) ──────────────────────────────
def test_s6_cartan_L12_is_d_phi1(s6_setup):
    """L₁₂ = ∂_{φ₁}: φ₁-coefficient = 1."""
    c = s6_setup["L_coeff"](0, 1)
    assert simplify(c[1] - 1) == 0, f"φ₁ coefficient = {c[1]}, expected 1"


def test_s6_cartan_L12_only_phi1(s6_setup):
    """L₁₂ has no β₁, β₂, φ₂, β₃, φ₃ components (pure azimuthal)."""
    c = s6_setup["L_coeff"](0, 1)
    for k in [0, 2, 3, 4, 5]:
        assert simplify(c[k]) == 0, f"coefficient {k} = {c[k]}, expected 0"


def test_s6_cartan_L34_is_d_phi2(s6_setup):
    """L₃₄ = ∂_{φ₂}: φ₂-coefficient = 1."""
    c = s6_setup["L_coeff"](2, 3)
    assert simplify(c[3] - 1) == 0, f"φ₂ coefficient = {c[3]}, expected 1"


def test_s6_cartan_L56_is_d_phi3(s6_setup):
    """L₅₆ = ∂_{φ₃}: φ₃-coefficient = 1."""
    c = s6_setup["L_coeff"](4, 5)
    assert simplify(c[5] - 1) == 0, f"φ₃ coefficient = {c[5]}, expected 1"


# ── T4: L₁₃ — cotβ₁ structure ───────────────────────────────────────────────
def test_s6_root_L13_phi1_has_cotb1(s6_setup):
    """L₁₃ φ₁-coefficient = cotβ₁ sinβ₂ cosφ₂ sinφ₁."""
    b1, b2, p2, p1 = s6_setup["b1"], s6_setup["b2"], s6_setup["p2"], s6_setup["p1"]
    c = s6_setup["L_coeff"](0, 2)
    expected = cot(b1) * sin(b2) * cos(p2) * sin(p1)
    assert trigsimp(c[1] - expected) == 0, f"φ₁ coeff = {c[1]}"


def test_s6_root_L13_no_long_range(s6_setup):
    """L₁₃ has no β₃ or φ₃ components (no long-range coupling)."""
    c = s6_setup["L_coeff"](0, 2)
    assert simplify(c[4]) == 0, f"β₃ coeff = {c[4]}, expected 0"
    assert simplify(c[5]) == 0, f"φ₃ coeff = {c[5]}, expected 0"


def test_s6_root_L13_full_structure(s6_setup):
    """L₁₃: all 6 coefficients match analytical expectation."""
    b1, b2, _b3, p1, p2, _p3 = (
        s6_setup["b1"],
        s6_setup["b2"],
        s6_setup["b3"],
        s6_setup["p1"],
        s6_setup["p2"],
        s6_setup["p3"],
    )
    c = s6_setup["L_coeff"](0, 2)
    expected = [
        -sin(b2) * cos(p1) * cos(p2),
        cot(b1) * sin(b2) * cos(p2) * sin(p1),
        tan(b1) * cos(p1) * cos(b2) * cos(p2),
        -tan(b1) * cos(p1) * sin(p2) / sin(b2),
        sp.Integer(0),
        sp.Integer(0),
    ]
    for k, (actual, exp) in enumerate(zip(c, expected)):
        assert trigsimp(actual - exp) == 0, f"coeff[{k}] residual = {trigsimp(actual - exp)}"


# ── T5: L₃₅ — cotβ₂ structure ───────────────────────────────────────────────
def test_s6_root_L35_phi2_has_cotb2(s6_setup):
    """L₃₅ φ₂-coefficient = cotβ₂ sinβ₃ cosφ₃ sinφ₂."""
    b2, b3, p3, p2 = s6_setup["b2"], s6_setup["b3"], s6_setup["p3"], s6_setup["p2"]
    c = s6_setup["L_coeff"](2, 4)
    expected = cot(b2) * sin(b3) * cos(p3) * sin(p2)
    assert trigsimp(c[3] - expected) == 0, f"φ₂ coeff = {c[3]}"


def test_s6_root_L35_no_phi1_coupling(s6_setup):
    """L₃₅ has no φ₁ or β₁ coupling (x³,x⁵ don't depend on φ₁)."""
    c = s6_setup["L_coeff"](2, 4)
    assert simplify(c[0]) == 0, f"β₁ coeff = {c[0]}"
    assert simplify(c[1]) == 0, f"φ₁ coeff = {c[1]}"


# ── T6: L₁₅ — cotβ₁ through β₂ level ────────────────────────────────────────
def test_s6_root_L15_phi1_has_cotb1(s6_setup):
    """L₁₅ φ₁-coefficient = cotβ₁ cosβ₂ sinβ₃ cosφ₃ sinφ₁."""
    b1, b2, b3, p3, p1 = (
        s6_setup["b1"],
        s6_setup["b2"],
        s6_setup["b3"],
        s6_setup["p3"],
        s6_setup["p1"],
    )
    c = s6_setup["L_coeff"](0, 4)
    expected = cot(b1) * cos(b2) * sin(b3) * cos(p3) * sin(p1)
    assert trigsimp(c[1] - expected) == 0, f"φ₁ coeff = {c[1]}"


# ── T7: Hierarchy — L₂₃ also has cotβ₁ ─────────────────────────────────────
def test_s6_root_L23_phi1_has_cotb1(s6_setup):
    """L₂₃ φ₁-coefficient = −cotβ₁ sinβ₂ cosφ₂ cosφ₁ (pattern confirmed)."""
    b1, b2, p1, p2 = s6_setup["b1"], s6_setup["b2"], s6_setup["p1"], s6_setup["p2"]
    c = s6_setup["L_coeff"](1, 2)
    expected = -cot(b1) * sin(b2) * cos(p2) * cos(p1)
    assert trigsimp(c[1] - expected) == 0, f"φ₁ coeff = {c[1]}"
