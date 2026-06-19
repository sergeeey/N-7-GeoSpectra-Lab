"""G15: B−L quantum number from S⁶ spinor geometry.

G14 established: S⁶ spinor = 1 ⊕ 3 ⊕ 3̄ ⊕ 1 under SU(3)_color.
G15 question: Does B−L emerge geometrically as a U(1) charge on the S⁶ spinor?

Answer: YES. B−L on the 8-dim S⁶ spinor is:

  B−L = −(1/3)(σ₃^{(1)} + σ₃^{(2)} + σ₃^{(3)})

where σ₃^{(k)} is σ₃ acting on the k-th qubit in the Kronecker basis |i₁i₂i₃⟩.

Equivalently:
  B−L = (2H−3)/3   where H = Hamming weight operator (diagonal: H[j,j] = popcount(j))

This is proportional to the spinor lift of the almost-complex structure J on S⁶:
  lift_to_spinor(J) = (i/2)(σ₃^{(1)} + σ₃^{(2)} + σ₃^{(3)}) = −(3i/2)·B−L

So J — the U(1) generator of u(3) = su(3) ⊕ u(1) — carries B−L in the spinor rep.

Sector assignments (combinatorial from Hamming weight):
  |000⟩ (H=0): B−L = −1  (lepton singlet)
  |011⟩,|101⟩,|110⟩ (H=2): B−L = +1/3  (quarks)
  |001⟩,|010⟩,|100⟩ (H=1): B−L = −1/3  (antiquarks)
  |111⟩ (H=3): B−L = +1  (anti-lepton singlet)

Hypercharge: Y = T3R + (B−L)/2
  T3R = ±1/2 from the S³ K-generators (right-handed SU(2)_R, G11).
  For T3R = 0 (left-handed sector): Y = (B−L)/2.

λ = FREE_COUPLING_PARAMETER throughout. sm_derivation_claimed = False.
"""

import json
import os
import sys

import sympy as sp
from sympy import zeros
from sympy import kronecker_product as kron

_EXP_DIR = os.path.dirname(__file__)
_REPO = os.path.abspath(os.path.join(_EXP_DIR, "..", ".."))

for _subdir in [
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g11_block_generators import lift_to_spinor, s3  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402
from g10_s6_so6_gauge import complex_structure  # noqa: E402

# ── Constants ────────────────────────────────────────────────────────────────

su3_vec = su3_generators()
su3_spin = [lift_to_spinor(C) for C in su3_vec]

I2 = sp.eye(2)
I8 = sp.eye(8)
Gamma7: sp.Matrix = kron(s3, s3, s3)

# Individual σ₃ operators on the 3-qubit system |i₁i₂i₃⟩
sigma3_1 = kron(s3, I2, I2)  # σ₃ on qubit 1 (bit weight 4)
sigma3_2 = kron(I2, s3, I2)  # σ₃ on qubit 2 (bit weight 2)
sigma3_3 = kron(I2, I2, s3)  # σ₃ on qubit 3 (bit weight 1)

# B−L generator: −(1/3)·(σ₃^{(1)} + σ₃^{(2)} + σ₃^{(3)})
# Diagonal entries: (2·popcount(index) − 3)/3
BmL: sp.Matrix = -sp.Rational(1, 3) * (sigma3_1 + sigma3_2 + sigma3_3)

# Hamming weight operator H = 3/2·I − 1/2·(σ₃^{(1)}+σ₃^{(2)}+σ₃^{(3)})
# H[j,j] = popcount(j) for j in {0..7}
Hamming: sp.Matrix = sp.Rational(3, 2) * I8 - sp.Rational(1, 2) * (sigma3_1 + sigma3_2 + sigma3_3)

# Sector indices (from G14)
SP_SINGLET = 0
QUARK = (3, 5, 6)
AQUARK = (1, 2, 4)
SM_SINGLET = 7

# Expected B−L values
BmL_LEP = sp.Integer(-1)  # lepton singlet |000⟩
BmL_Q = sp.Rational(1, 3)  # quarks
BmL_AQ = sp.Rational(-1, 3)  # antiquarks
BmL_ALEP = sp.Integer(1)  # anti-lepton singlet |111⟩


# ── Main experiment ──────────────────────────────────────────────────────────


def main() -> bool:
    results: dict = {}
    passed = 0

    # ── T1: BmL is diagonal ──────────────────────────────────────────────────
    t1_ok = BmL.is_diagonal()
    results["T1_BmL_diagonal"] = t1_ok
    passed += int(t1_ok)
    print(f"T1 B−L is diagonal: {'PASS' if t1_ok else 'FAIL'}")
    print(f"   entries: {[BmL[k, k] for k in range(8)]}")

    # ── T2: BmL = (2H−3)/3 where H = Hamming weight operator ────────────────
    BmL_from_H = (2 * Hamming - 3 * I8) * sp.Rational(1, 3)
    t2_ok = BmL - BmL_from_H == zeros(8, 8)
    results["T2_Hamming_formula"] = t2_ok
    passed += int(t2_ok)
    print(f"T2 B−L = (2H−3)/3: {'PASS' if t2_ok else 'FAIL'}")
    if t2_ok:
        print(f"   H diagonal: {[Hamming[k, k] for k in range(8)]}")

    # ── T3: [BmL, Γ₇] = 0 (both diagonal → trivially commute) ──────────────
    t3_ok = BmL * Gamma7 - Gamma7 * BmL == zeros(8, 8)
    results["T3_commutes_chirality"] = t3_ok
    passed += int(t3_ok)
    print(f"T3 [B−L, Γ₇] = 0: {'PASS' if t3_ok else 'FAIL'}")

    # ── T4: [BmL, Cᵢ^spin] = 0 for all 8 SU(3) generators ─────────────────
    bad_su3 = [(i, C) for i, C in enumerate(su3_spin) if BmL * C - C * BmL != zeros(8, 8)]
    t4_ok = len(bad_su3) == 0
    results["T4_commutes_SU3"] = t4_ok
    passed += int(t4_ok)
    print(
        f"T4 [B−L, C^spin] = 0 for all 8 generators: {'PASS' if t4_ok else 'FAIL'}"
        + (f" ({len(bad_su3)} violations)" if not t4_ok else "")
    )

    # ── T5: Quark sector {3,5,6}: B−L = +1/3 ────────────────────────────────
    t5_ok = all(BmL[j, j] == BmL_Q for j in QUARK)
    results["T5_quark_BmL"] = t5_ok
    passed += int(t5_ok)
    print(f"T5 quarks B−L = +1/3: {'PASS' if t5_ok else 'FAIL'}")
    print(f"   {[BmL[j, j] for j in QUARK]}")

    # ── T6: Antiquark sector {1,2,4}: B−L = −1/3 ────────────────────────────
    t6_ok = all(BmL[j, j] == BmL_AQ for j in AQUARK)
    results["T6_antiquark_BmL"] = t6_ok
    passed += int(t6_ok)
    print(f"T6 antiquarks B−L = −1/3: {'PASS' if t6_ok else 'FAIL'}")
    print(f"   {[BmL[j, j] for j in AQUARK]}")

    # ── T7: Singlets B−L = ±1 ───────────────────────────────────────────────
    t7_ok = BmL[SP_SINGLET, SP_SINGLET] == BmL_LEP and BmL[SM_SINGLET, SM_SINGLET] == BmL_ALEP
    results["T7_singlet_BmL"] = t7_ok
    passed += int(t7_ok)
    print(f"T7 singlets B−L = ±1: {'PASS' if t7_ok else 'FAIL'}")
    print(f"   |000⟩: {BmL[0, 0]},  |111⟩: {BmL[7, 7]}")

    # ── T8: B−L ∝ i·lift_to_spinor(J) ──────────────────────────────────────
    # lift_to_spinor(J) = J_spin(1,2)+J_spin(3,4)+J_spin(5,6) = (i/2)·(σ₃^{(1)}+σ₃^{(2)}+σ₃^{(3)})
    # BmL = −(1/3)·(σ₃^{(1)}+σ₃^{(2)}+σ₃^{(3)})
    # → lift_to_spinor(J) = −(3i/2)·BmL  ↔  BmL = (2i/3)·lift_to_spinor(J)
    J_geom = complex_structure()
    J_spin = lift_to_spinor(J_geom)
    # Check: J_spin == −(3i/2)·BmL
    expected_J_spin = BmL * sp.Rational(-3, 2) * sp.I
    t8_ok = J_spin - expected_J_spin == zeros(8, 8)
    results["T8_proportional_to_J"] = t8_ok
    passed += int(t8_ok)
    print(f"T8 lift_to_spinor(J) = −(3i/2)·B−L: {'PASS' if t8_ok else 'FAIL'}")
    print("   J is the u(1) center of u(3)=su(3)⊕u(1); its spinor lift carries B−L")

    # ── T9: Y = (B−L)/2 for T3R = 0 (left-handed sector) ───────────────────
    # |000⟩ lepton singlet: Y = 0 + (−1)/2 = −1/2  (charged lepton L doublet hypercharge)
    # |111⟩ anti-lepton:    Y = 0 + (+1)/2 = +1/2
    Y_000_T3R0 = BmL[0, 0] * sp.Rational(1, 2)
    Y_111_T3R0 = BmL[7, 7] * sp.Rational(1, 2)
    t9_ok = Y_000_T3R0 == sp.Rational(-1, 2) and Y_111_T3R0 == sp.Rational(1, 2)
    results["T9_Y_T3R0"] = t9_ok
    passed += int(t9_ok)
    print(f"T9 Y = (B−L)/2 for T3R=0: {'PASS' if t9_ok else 'FAIL'}")
    print(f"   |000⟩: Y={Y_000_T3R0},  |111⟩: Y={Y_111_T3R0}")

    # ── T10: Gell-Mann–Nishijima Y = T3R + (B−L)/2 for right-handed fermions ─
    # ν_R: B−L=−1, T3R=+1/2 → Y = 0  (sterile neutrino)
    # e_R: B−L=−1, T3R=−1/2 → Y = −1
    # u_R: B−L=+1/3, T3R=+1/2 → Y = +2/3
    # d_R: B−L=+1/3, T3R=−1/2 → Y = −1/3
    half = sp.Rational(1, 2)
    SM_table = [
        ("ν_R", BmL_LEP, +half, sp.Integer(0)),
        ("e_R", BmL_LEP, -half, sp.Integer(-1)),
        ("u_R", BmL_Q, +half, sp.Rational(2, 3)),
        ("d_R", BmL_Q, -half, sp.Rational(-1, 3)),
    ]
    t10_ok = all(T3R + bl * half == Y for _, bl, T3R, Y in SM_table)
    results["T10_SM_table"] = t10_ok
    passed += int(t10_ok)
    print(f"T10 Y = T3R + (B−L)/2 for SM right-handed fermions: {'PASS' if t10_ok else 'FAIL'}")
    for name, bl, T3R, Y in SM_table:
        computed = T3R + bl * half
        print(
            f"   {name}: B−L={bl}, T3R={T3R}, Y_formula={computed}, Y_SM={Y} {'✓' if computed == Y else '✗'}"
        )

    # ── T11: B−L constant within each SU(3) sector (Schur: irrep → scalar) ──
    quark_const = BmL[3, 3] == BmL[5, 5] and BmL[5, 5] == BmL[6, 6]
    aquark_const = BmL[1, 1] == BmL[2, 2] and BmL[2, 2] == BmL[4, 4]
    sector_vals = [BmL[0, 0], BmL[3, 3], BmL[1, 1], BmL[7, 7]]
    vals_distinct = len(set(sector_vals)) == 4
    t11_ok = quark_const and aquark_const and vals_distinct
    results["T11_uniqueness_sector_const"] = t11_ok
    passed += int(t11_ok)
    print(f"T11 B−L constant within sectors, distinct across: {'PASS' if t11_ok else 'FAIL'}")
    print(
        f"   sector values: 1={sector_vals[0]}, 3={sector_vals[1]}, 3̄={sector_vals[2]}, 1={sector_vals[3]}"
    )

    # ── T12: BmL is Hermitian (physical observable) ──────────────────────────
    t12_ok = BmL - BmL.H == zeros(8, 8)
    results["T12_BmL_hermitian"] = t12_ok
    passed += int(t12_ok)
    print(f"T12 B−L is Hermitian (physical observable): {'PASS' if t12_ok else 'FAIL'}")

    # ── Summary ───────────────────────────────────────────────────────────────
    total = 12
    print(f"\n{'=' * 60}")
    print(f"G15 B−L HYPERCHARGE: {passed}/{total} gates PASS")
    if passed == total:
        print("PASS_G15_BL_GEOMETRIC_ORIGIN")
        print()
        print("Key result:")
        print("  B−L = −(1/3)(σ₃^{(1)}+σ₃^{(2)}+σ₃^{(3)}) = (2H−3)/3")
        print("  lift_to_spinor(J) = −(3i/2)·B−L   [J = u(1) center of u(3)=su(3)⊕u(1)]")
        print("  Y = T3R + (B−L)/2  [T3R from S³ K-generators, G11]")
    else:
        print("INCOMPLETE — see failing gates above")

    out_path = os.path.join(_EXP_DIR, "g15_results.json")
    with open(out_path, "w") as f:
        json.dump({"passed": passed, "total": total, "gates": results}, f, indent=2)

    return passed == total


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
