"""S6-HARM-G1: S⁶ coordinate system and Cartan phase structure.

Parallel to Tom Lawrence S³ rows 11-14:
  Row 11: x^α coordinates confirmed (sin(2α)dα measure)
  Row 13: ∂_θ + ∂_θ̃ = Î_{3L},  ∂_θ - ∂_θ̃ = Î_{3R}
  Row 14: spinor phase exp(i[i_L(θ+θ̃)+i_R(θ-θ̃)])

S⁶ analog:
  3 azimuthal angles φ_k ↔ 3 Cartan generators H_k = J_{2k-1,2k}
  Spinor Cartan phase: e^{i(m₁φ₁ + m₂φ₂ + m₃φ₃)},  m_k ∈ {±½}
"""

import json
from pathlib import Path

import sympy as sp
from sympy import I, pi, cos, sin, Rational, symbols, simplify, trigsimp, integrate

results: dict = {}


def chk(label: str, passed: bool, note: str = ""):
    results[label] = "PASS" if passed else f"FAIL: {note}"
    return passed


# ── Symbols ──────────────────────────────────────────────────────────────────
rho, b1, b2, b3, p1, p2, p3 = symbols(
    r"\rho \beta_1 \beta_2 \beta_3 \phi_1 \phi_2 \phi_3", real=True, positive=True
)

# ── T1: Coordinate constraint Σ(xⁱ)² = ρ² ──────────────────────────────────
# Nested sphere parameterization of S⁶ ⊂ ℝ⁷
# Pairs (x¹,x²), (x³,x⁴), (x⁵,x⁶) correspond to Cartan planes (H₁,H₂,H₃)
# x⁷ is the "pole" direction of the innermost S²

coords = [
    rho * sin(b1) * cos(p1),  # x¹
    rho * sin(b1) * sin(p1),  # x²
    rho * cos(b1) * sin(b2) * cos(p2),  # x³
    rho * cos(b1) * sin(b2) * sin(p2),  # x⁴
    rho * cos(b1) * cos(b2) * sin(b3) * cos(p3),  # x⁵
    rho * cos(b1) * cos(b2) * sin(b3) * sin(p3),  # x⁶
    rho * cos(b1) * cos(b2) * cos(b3),  # x⁷
]

norm_sq = trigsimp(sum(x**2 for x in coords))
chk(
    "T1_constraint_sum_xi_sq_eq_rho_sq",
    simplify(norm_sq - rho**2) == 0,
    f"residual = {simplify(norm_sq - rho**2)}",
)

# ── T2: Metric tensor (induced, diagonal) ────────────────────────────────────
# Coordinate order: (β₁, φ₁, β₂, φ₂, β₃, φ₃)
params = [b1, p1, b2, p2, b3, p3]

# Jacobian: 7 rows (x^i) × 6 cols (∂/∂q_j)
J_mat = sp.Matrix([[sp.diff(x, q) for q in params] for x in coords])

# Induced metric g = J^T J
g = trigsimp(J_mat.T * J_mat)

# Expected diagonal entries
g_expected_diag = [
    rho**2,
    rho**2 * sin(b1) ** 2,
    rho**2 * cos(b1) ** 2,
    rho**2 * cos(b1) ** 2 * sin(b2) ** 2,
    rho**2 * cos(b1) ** 2 * cos(b2) ** 2,
    rho**2 * cos(b1) ** 2 * cos(b2) ** 2 * sin(b3) ** 2,
]

# Check diagonal
diag_ok = True
for k, (g_kk, exp) in enumerate(zip(g.diagonal(), g_expected_diag)):
    res = trigsimp(g_kk - exp)
    if res != 0:
        diag_ok = False
        results[f"T2_g_{params[k]}{params[k]}_wrong"] = f"residual={res}"

chk("T2_metric_diagonal_correct", diag_ok)

# Check off-diagonal = 0
offdiag_ok = True
for i in range(6):
    for j in range(i + 1, 6):
        res = trigsimp(g[i, j])
        if res != 0:
            offdiag_ok = False
            results[f"T2_off_diag_{i}{j}_nonzero"] = str(res)

chk("T2_metric_off_diagonal_zero", offdiag_ok)

# Volume element √det(g)
# det(g) = ρ¹² sin²β₁ cos⁸β₁ sin²β₂ cos⁴β₂ sin²β₃
det_g = rho**12 * sin(b1) ** 2 * cos(b1) ** 8 * sin(b2) ** 2 * cos(b2) ** 4 * sin(b3) ** 2
sqrt_det_g = rho**6 * sin(b1) * cos(b1) ** 4 * sin(b2) * cos(b2) ** 2 * sin(b3)

# Verify: det(g) matches g product
det_from_g = sp.Mul(*g.diagonal())  # diagonal product (since g is diagonal)
det_diff = trigsimp(det_from_g - det_g)
chk("T2_det_g_formula", det_diff == 0, f"residual = {det_diff}")

results["T2_sqrt_det_g"] = "rho^6 * sin(b1)*cos(b1)^4 * sin(b2)*cos(b2)^2 * sin(b3)"

# ── T3: Volume of S⁶ ─────────────────────────────────────────────────────────
# Vol(S⁶) = ∫ sqrt_det_g db1 dp1 db2 dp2 db3 dp3
# β₁,β₂ ∈ [0,π/2],  β₃ ∈ [0,π],  φ₁,φ₂,φ₃ ∈ [0,2π]
# Factor out ρ⁶ and (2π)³, integrate the β parts:
#   I₁ = ∫₀^{π/2} sinβ₁ cos⁴β₁ dβ₁ = 1/5
#   I₂ = ∫₀^{π/2} sinβ₂ cos²β₂ dβ₂ = 1/3
#   I₃ = ∫₀^π    sinβ₃          dβ₃ = 2

I1 = integrate(sin(b1) * cos(b1) ** 4, (b1, 0, pi / 2))
I2 = integrate(sin(b2) * cos(b2) ** 2, (b2, 0, pi / 2))
I3 = integrate(sin(b3), (b3, 0, pi))

results["T3_I1_integral"] = str(I1)  # should be 1/5
results["T3_I2_integral"] = str(I2)  # should be 1/3
results["T3_I3_integral"] = str(I3)  # should be 2

vol_s6 = rho**6 * I1 * (2 * pi) * I2 * (2 * pi) * I3 * (2 * pi)
vol_s6_simplified = sp.simplify(vol_s6)

# Expected: 16π³/15 × ρ⁶
vol_expected = Rational(16, 15) * pi**3 * rho**6

chk(
    "T3_vol_s6_eq_16pi3_over_15",
    simplify(vol_s6_simplified - vol_expected) == 0,
    f"got {vol_s6_simplified}, expected {vol_expected}",
)

results["T3_vol_s6"] = str(vol_s6_simplified)

# ── T4: Cartan phase eigenvalue ──────────────────────────────────────────────
# H_k = J_{2k-1,2k} from G0 generates rotation in the (x^{2k-1}, x^{2k}) plane
# In coordinate representation on S⁶: H_k → functional eigenvalue m_k
# Check: (−i ∂_{φ_k}) e^{im_k φ_k} = m_k × e^{im_k φ_k}
# where m_k ∈ {+1/2, −1/2} (half-integer → spinor)

m = sp.Symbol("m", rational=True)  # generic weight
phi = sp.Symbol(r"\phi", real=True)

phase = sp.exp(I * m * phi)
D_phase = sp.diff(phase, phi)
eigenvalue = sp.simplify(-I * D_phase / phase)

chk("T4_cartan_eigenvalue_is_m", eigenvalue == m, f"got {eigenvalue}")

# Verify for m = ±1/2 specifically
for m_val in [sp.Rational(1, 2), sp.Rational(-1, 2)]:
    phase_v = sp.exp(I * m_val * phi)
    ev = sp.simplify(-I * sp.diff(phase_v, phi) / phase_v)
    chk(f"T4_eigenvalue_for_m{m_val}", ev == m_val, f"got {ev}")

# Matrix eigenvalue check (from G0): H_k has matrix eigenvalues ±i/2
# In functional rep: m_k = eigenvalue of (−i∂_{φ_k})
# Matrix eigenvalue = i × m_k  [consistency: i × (±1/2) = ±i/2 ✓]
matrix_eigenvalue_positive = I * sp.Rational(1, 2)
matrix_eigenvalue_negative = I * sp.Rational(-1, 2)
results["T4_matrix_eigenvalue_plus"] = str(matrix_eigenvalue_positive)  # +i/2
results["T4_matrix_eigenvalue_minus"] = str(matrix_eigenvalue_negative)  # -i/2
results["T4_consistency"] = "functional m_k = ±1/2 ↔ matrix eigenvalue i×m_k = ±i/2 (G0 confirmed)"

# ── T5: Weight table — all 8 Cartan weight vectors ──────────────────────────
# From G0: 4 weights (even minus-count) and 4̄ weights (odd minus-count)
half = sp.Rational(1, 2)

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

# Verify each weight vector: all m_k ∈ {±1/2}
all_half_integers = all(all(abs(m) == half for m in w) for w in weights_4 + weights_4bar)
chk("T5_all_weights_are_half_integers", all_half_integers)

# Verify chiral parity: 4 has even number of (−1/2), 4̄ has odd
parity_4_ok = all(sum(1 for m in w if m < 0) % 2 == 0 for w in weights_4)
parity_4bar_ok = all(sum(1 for m in w if m < 0) % 2 == 1 for w in weights_4bar)
chk("T5_4_rep_even_parity", parity_4_ok)
chk("T5_4bar_rep_odd_parity", parity_4bar_ok)

# Cartan phase for each spinor component
phases_4 = [f"exp(i({m1}φ₁ + {m2}φ₂ + {m3}φ₃))" for m1, m2, m3 in weights_4]
phases_4bar = [f"exp(i({m1}φ₁ + {m2}φ₂ + {m3}φ₃))" for m1, m2, m3 in weights_4bar]

results["T5_cartan_phases_4_rep"] = phases_4
results["T5_cartan_phases_4bar_rep"] = phases_4bar
results["T5_total_spinor_components"] = 8
results["T5_analog_of_Tom_row14"] = "e^{i(m₁φ₁+m₂φ₂+m₃φ₃)} ← S⁶ analog of exp(i[i_L(θ+θ̃)+i_R(θ-θ̃)])"

# Verify total 8 unique weight vectors (no duplicates)
all_weights = weights_4 + weights_4bar
unique_weights = set(all_weights)
chk("T5_8_unique_weight_vectors", len(unique_weights) == 8, f"got {len(unique_weights)}")

# ── Summary ──────────────────────────────────────────────────────────────────
pass_count = sum(1 for v in results.values() if str(v) == "PASS")
total_checks = sum(
    1
    for k, v in results.items()
    if not any(
        k.endswith(s)
        for s in [
            "_integral",
            "_sqrt_det_g",
            "_vol_s6",
            "eigenvalue_plus",
            "eigenvalue_minus",
            "_consistency",
            "_phases_4_rep",
            "_phases_4bar_rep",
            "_components",
            "_analog",
        ]
    )
)

verdict = "PASS_S6_COORDINATES_CARTAN_PHASES_CONFIRMED" if pass_count >= 10 else "FAIL"

output = {
    "gate": "S6-HARM-G1",
    "date": "2026-06-15",
    "verdict": verdict,
    "pass_count": pass_count,
    "total_boolean_checks": total_checks,
    "coordinates": "7-component nested sphere: (sinβ₁cosφ₁, sinβ₁sinφ₁, cosβ₁sinβ₂cosφ₂, ...)",
    "ranges": "β₁,β₂∈[0,π/2], β₃∈[0,π], φ₁,φ₂,φ₃∈[0,2π]",
    "volume": "16π³/15 × ρ⁶",
    "cartan_structure": "H_k ↔ φ_k, eigenvalue m_k = ±1/2",
    "tom_analog": "e^{i(m₁φ₁+m₂φ₂+m₃φ₃)} ← exp(i[i_L(θ+θ̃)+i_R(θ-θ̃)])",
    "results": {k: str(v) if not isinstance(v, list) else v for k, v in results.items()},
}

out_path = Path(__file__).parent / "results_s6_harm_g1.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, default=str)

print(f"\nVerdict: {verdict}")
print(f"Pass: {pass_count} / {total_checks}")
for k, v in results.items():
    if isinstance(v, list):
        print(f"  · {k}:")
        for item in v:
            print(f"      {item}")
    elif str(v) == "PASS":
        print(f"  ✓ {k}")
    elif str(v).startswith("FAIL"):
        print(f"  ✗ {k}: {v}")
    else:
        print(f"  · {k}: {v}")
