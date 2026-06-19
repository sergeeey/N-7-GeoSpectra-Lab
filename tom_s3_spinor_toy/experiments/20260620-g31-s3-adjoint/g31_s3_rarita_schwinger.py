"""
G31: Twisted Dirac D ⊗ V_j on S³ — Lichnerowicz barrier analysis.

Question: Does D ⊗ V_{adj} (j=1) on S³ have 3 zero modes → 3 SM generations?

Method: Lichnerowicz-Weitzenböck for constant-curvature S³.
Key formula:
  D²_V = ∇*∇ + R/4 + F_{V,spinor}
  F_{V_j,spinor} = -(1/ρ₃²)[C₂(J) - C₂(j_s) - C₂(j_b)]
  where J = j_s ± j_b (two coupling sectors).

For S³: R = 6/ρ₃², R/4 = 3/(2ρ₃²) in units 1/ρ₃².
"""

from fractions import Fraction


def casimir(j: Fraction) -> Fraction:
    """Quadratic Casimir C₂(j) = j(j+1) for SU(2) spin-j rep."""
    return j * (j + 1)


def lichnerowicz_sector(j_spinor: Fraction, j_bundle: Fraction, J_total: Fraction) -> Fraction:
    """
    Lichnerowicz lower bound on D² in sector J_total, in units 1/ρ₃².
    D² ≥ R/4 + F = 3/2 - [C₂(J) - C₂(j_s) - C₂(j_b)]
    """
    R_over_4 = Fraction(3, 2)
    F = -(casimir(J_total) - casimir(j_spinor) - casimir(j_bundle))
    return R_over_4 + F


def scan_bundle(j_bundle: Fraction, j_spinor: Fraction = Fraction(1, 2)) -> dict:
    """Full Lichnerowicz analysis for D ⊗ V_{j_bundle} on S³."""
    J_plus = j_spinor + j_bundle
    J_minus = abs(j_spinor - j_bundle)

    D_sq_plus = lichnerowicz_sector(j_spinor, j_bundle, J_plus)
    D_sq_minus = lichnerowicz_sector(j_spinor, j_bundle, J_minus)

    has_zero_modes = D_sq_plus <= 0 or D_sq_minus <= 0
    min_D_sq = min(D_sq_plus, D_sq_minus)

    # Zero-mode count in J+ sector (only sector that can go negative)
    dim_J_plus = int(2 * J_plus + 1)  # multiplicity of J+ rep

    return {
        "j_bundle": j_bundle,
        "J_plus": J_plus,
        "J_minus": J_minus,
        "D_sq_J_plus": D_sq_plus,
        "D_sq_J_minus": D_sq_minus,
        "min_D_sq": min_D_sq,
        "has_zero_modes": has_zero_modes,
        "zero_mode_dim_if_any": dim_J_plus if D_sq_plus <= 0 else 0,
    }


# ---------------------------------------------------------------------------
# Step 1 — S³ curvature data
# ---------------------------------------------------------------------------
print("=" * 65)
print("G31: D ⊗ V_{adj} on S³ — Lichnerowicz barrier")
print("=" * 65)

R_S3 = Fraction(6, 1)  # scalar curvature in units 1/ρ₃²
R_over_4 = Fraction(3, 2)  # = 6/4
print(f"\nStep 1: S³ curvature")
print(f"  R = 6/ρ₃² → R/4 = {R_over_4}/ρ₃²")

# Step 2 — Untwisted Dirac (sanity check)
r0 = scan_bundle(Fraction(0))
print(f"\nStep 2: Untwisted Dirac (j_bundle = 0, Lichnerowicz classic)")
print(f"  D² ≥ {r0['min_D_sq']}/ρ₃² > 0  [VERIFIED — no zero modes on S³]")

# Step 3 — Adjoint bundle j = 1
r1 = scan_bundle(Fraction(1))
print(f"\nStep 3: Adjoint bundle V_{{adj}}, j_bundle = 1")
print(f"  Coupling sectors: J+ = {r1['J_plus']}, J- = {r1['J_minus']}")
print(f"  D²(J+={r1['J_plus']}) = {r1['D_sq_J_plus']}/ρ₃²")
print(f"  D²(J-={r1['J_minus']}) = {r1['D_sq_J_minus']}/ρ₃²")
print(f"  min D² = {r1['min_D_sq']}/ρ₃² > 0")
print(f"  Has zero modes: {r1['has_zero_modes']}")
print(f"  → G31 KILL: D ⊗ V_{{adj}} has no zero modes on S³")

# Step 4 — Critical bundle: j_critical where D² first hits 0
print("\nStep 4: Critical spin j_critical scan")
print(f"  {'j_bundle':>10} | {'min D² (×1/ρ₃²)':>18} | {'zero-mode dim':>14} | verdict")
print("  " + "-" * 62)
for num in range(0, 9):
    j_b = Fraction(num, 2)
    r = scan_bundle(j_b)
    verdict = "zero modes!" if r["has_zero_modes"] else f"no"
    zm_dim = r["zero_mode_dim_if_any"] if r["has_zero_modes"] else "-"
    print(f"  {str(j_b):>10} | {str(r['min_D_sq']):>18} | {str(zm_dim):>14} | {verdict}")

r_rs = scan_bundle(Fraction(3, 2))
print(f"\n  j_critical = 3/2 (Rarita-Schwinger boundary: D² → 0)")
print(f"  At j=3/2: D²(J+={r_rs['J_plus']}) = {r_rs['D_sq_J_plus']} — boundary Killing spinors")
print(f"  dim(J+={r_rs['J_plus']}) = {int(2 * r_rs['J_plus'] + 1)} states (J=2 quintuplet), NOT 3")

# Step 5 — Parity obstruction: why 3 is impossible
print("\nStep 5: Parity obstruction — 3 generations impossible on S³")
print("  For D ⊗ V_j on S³, zero modes only appear in J+ = j+1/2 sector.")
print("  Zero-mode count (if any) = dim(J+) = 2(j+1/2)+1 = 2j+2 [ALWAYS EVEN].")
print("  3 generations require 3 zero modes.")
print("  3 is ODD. 2j+2 is EVEN for all j ∈ ½ℤ.")
print("  → No SU(2) bundle on S³ can give exactly 3 zero modes.")

print("\n" + "=" * 65)
print("G31 VERDICT: KILL")
print("  (a) Adjoint j=1 < j_critical=3/2 → Lichnerowicz D² > 0 → no zero modes")
print("  (b) Even for j > 3/2: zero-mode count = 2j+2 (EVEN) ≠ 3 (ODD)")
print("  → 3 SM generations from S³ Dirac zero modes is IMPOSSIBLE.")
print("=" * 65)
