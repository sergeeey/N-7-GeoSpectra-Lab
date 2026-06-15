"""Regression gate: S6-HARM-G1 — S⁶ coordinates and Cartan phase structure.

Pins:
- Nested sphere parameterization of S⁶ ⊂ ℝ⁷ satisfies Σ(xⁱ)² = ρ²
- Induced metric is diagonal with correct entries
- Volume = 16π³/15 × ρ⁶ (matches Vol(S⁶)) with β₃∈[0,π] range
- Cartan phase eigenvalue: −i∂_{φ_k} e^{im_kφ_k} = m_k
- All 8 SO(6) spinor Cartan weight vectors are half-integers with correct parity
"""

import sympy as sp
from sympy import I, pi, cos, sin, Rational, symbols, simplify, trigsimp, integrate

# ── Symbols ──────────────────────────────────────────────────────────────────
rho, b1, b2, b3, p1, p2, p3 = symbols(
    r"\rho \beta_1 \beta_2 \beta_3 \phi_1 \phi_2 \phi_3", real=True, positive=True
)

coords = [
    rho * sin(b1) * cos(p1),
    rho * sin(b1) * sin(p1),
    rho * cos(b1) * sin(b2) * cos(p2),
    rho * cos(b1) * sin(b2) * sin(p2),
    rho * cos(b1) * cos(b2) * sin(b3) * cos(p3),
    rho * cos(b1) * cos(b2) * sin(b3) * sin(p3),
    rho * cos(b1) * cos(b2) * cos(b3),
]

params = [b1, p1, b2, p2, b3, p3]

J_mat = sp.Matrix([[sp.diff(x, q) for q in params] for x in coords])
g = trigsimp(J_mat.T * J_mat)

half = Rational(1, 2)

weights_4 = [
    (+half, +half, +half),
    (+half, -half, -half),
    (-half, +half, -half),
    (-half, -half, +half),
]
weights_4bar = [
    (-half, -half, -half),
    (-half, +half, +half),
    (+half, -half, +half),
    (+half, +half, -half),
]


def test_s6_coordinate_constraint():
    """T1: Σᵢ(xⁱ)² = ρ² for all 7 embedding coordinates."""
    norm_sq = trigsimp(sum(x**2 for x in coords))
    assert simplify(norm_sq - rho**2) == 0, f"Constraint violated: {norm_sq}"


def test_s6_metric_diagonal():
    """T2a: Induced metric on S⁶ is diagonal."""
    for i in range(6):
        for j in range(i + 1, 6):
            assert trigsimp(g[i, j]) == 0, f"Off-diagonal g[{i},{j}] = {trigsimp(g[i, j])}"


def test_s6_metric_diagonal_entries():
    """T2b: Diagonal metric entries match nested sphere formula."""
    expected = [
        rho**2,
        rho**2 * sin(b1) ** 2,
        rho**2 * cos(b1) ** 2,
        rho**2 * cos(b1) ** 2 * sin(b2) ** 2,
        rho**2 * cos(b1) ** 2 * cos(b2) ** 2,
        rho**2 * cos(b1) ** 2 * cos(b2) ** 2 * sin(b3) ** 2,
    ]
    for k, (g_kk, exp) in enumerate(zip(g.diagonal(), expected)):
        assert trigsimp(g_kk - exp) == 0, f"g[{k},{k}] wrong: got {g_kk}, expected {exp}"


def test_s6_volume_element():
    """T2c: det(g) = ρ¹² sin²β₁ cos⁸β₁ sin²β₂ cos⁴β₂ sin²β₃."""
    det_expected = (
        rho**12 * sin(b1) ** 2 * cos(b1) ** 8 * sin(b2) ** 2 * cos(b2) ** 4 * sin(b3) ** 2
    )
    det_actual = sp.Mul(*g.diagonal())
    assert trigsimp(det_actual - det_expected) == 0


def test_s6_volume_16pi3_over_15():
    """T3: ∫ √det(g) dβ₁dφ₁dβ₂dφ₂dβ₃dφ₃ = 16π³/15 × ρ⁶.

    β₁,β₂ ∈ [0,π/2], β₃ ∈ [0,π], φ_k ∈ [0,2π].
    I₁=1/5, I₂=1/3, I₃=2 → 8π³/15 × (2ρ)⁶/... → 16π³/15 × ρ⁶.
    """
    I1 = integrate(sin(b1) * cos(b1) ** 4, (b1, 0, pi / 2))
    I2 = integrate(sin(b2) * cos(b2) ** 2, (b2, 0, pi / 2))
    I3 = integrate(sin(b3), (b3, 0, pi))

    assert I1 == Rational(1, 5), f"I₁ = {I1}"
    assert I2 == Rational(1, 3), f"I₂ = {I2}"
    assert I3 == 2, f"I₃ = {I3}"

    vol = rho**6 * I1 * (2 * pi) * I2 * (2 * pi) * I3 * (2 * pi)
    vol_expected = Rational(16, 15) * pi**3 * rho**6
    assert simplify(vol - vol_expected) == 0, f"Vol = {simplify(vol)}"


def test_cartan_phase_eigenvalue():
    """T4: −i∂_{φ} e^{imφ} = m × e^{imφ} for symbolic m."""
    m = sp.Symbol("m", rational=True)
    phi = sp.Symbol(r"\phi", real=True)
    phase = sp.exp(I * m * phi)
    ev = simplify(-I * sp.diff(phase, phi) / phase)
    assert ev == m, f"Eigenvalue is {ev}, expected m"


def test_cartan_eigenvalue_half_integers():
    """T4b: eigenvalue m_k ∈ {±½} for the fundamental spinor representation."""
    phi = sp.Symbol(r"\phi", real=True)
    for m_val in [Rational(1, 2), Rational(-1, 2)]:
        phase = sp.exp(I * m_val * phi)
        ev = simplify(-I * sp.diff(phase, phi) / phase)
        assert ev == m_val, f"For m={m_val}: got {ev}"


def test_spinor_weights_are_half_integers():
    """T5a: All 8 Cartan weight vectors have entries ∈ {±½}."""
    for w in weights_4 + weights_4bar:
        for mk in w:
            assert abs(mk) == half, f"Weight {mk} in {w} is not ±½"


def test_spinor_weights_chiral_parity():
    """T5b: 4-rep has even minus-count, 4̄-rep has odd minus-count."""
    for w in weights_4:
        n_minus = sum(1 for mk in w if mk < 0)
        assert n_minus % 2 == 0, f"4-rep weight {w} has odd parity"
    for w in weights_4bar:
        n_minus = sum(1 for mk in w if mk < 0)
        assert n_minus % 2 == 1, f"4̄-rep weight {w} has even parity"


def test_weight_vectors_unique():
    """T5c: All 8 weight vectors are distinct (no duplicates)."""
    all_weights = weights_4 + weights_4bar
    assert len(set(all_weights)) == 8, f"Duplicates found: {all_weights}"
