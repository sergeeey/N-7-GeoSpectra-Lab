"""G16: T3R from S³ K-generators — completing Y = T3R + (B−L)/2.

G11: K_i = SU(2)_R generators on S³, K₃ = block_diag(0₂, σ₃/2) in {L↑,L↓,R↑,R↓}.
G15: B−L on S⁶, lift_to_spinor(J) = −(3i/2)·B−L.

G16 question: Do K₃ eigenvalues give T3R = ±1/2 for right-handed SM fermions, completing
Y = T3R + (B−L)/2 as a purely geometric formula on the 32-dim S³×S⁶ spinor?

Answer: YES. The 32-component spinor in the kron(S³_4, S⁶_8) basis decomposes as:

  Rows 0–7:   |L,↑⟩⊗S⁶   T3R=0, T3L=+1/2
  Rows 8–15:  |L,↓⟩⊗S⁶   T3R=0, T3L=−1/2
  Rows 16–23: |R,↑⟩⊗S⁶   T3R=+1/2
  Rows 24–31: |R,↓⟩⊗S⁶   T3R=−1/2

Right-handed sector (rows 16–31), Y = K₃^{32} + (B−L)/2:

  SM right-handed fermions:
    ν_R  Y=0      row 16  = 16 + |000⟩  (T3R=+1/2, B−L=−1)
    u_R  Y=+2/3   rows 19,21,22          (T3R=+1/2, B−L=+1/3)
    e_R  Y=−1     row 24  = 24 + |000⟩  (T3R=−1/2, B−L=−1)
    d_R  Y=−1/3   rows 27,29,30          (T3R=−1/2, B−L=+1/3)

  CPT conjugates (antifermions):
    d̄_R Y=+1/3  rows 17,18,20           (T3R=+1/2, B−L=−1/3)
    ē_R  Y=+1    row 23  = 16 + |111⟩   (T3R=+1/2, B−L=+1)
    ū_R  Y=−2/3  rows 25,26,28          (T3R=−1/2, B−L=−1/3)
    ν̄_R Y=0     row 31  = 24 + |111⟩   (T3R=−1/2, B−L=+1)

Y = K₃^{32} + BmL_32/2 is fully derived from S³×S⁶ geometry:
  S³ sector (K₃):  right-handed SU(2)_R generator (G11)
  S⁶ sector (B−L): spinor lift of J's U(1) center (G15)
No additional assumptions needed beyond the product structure.

Left-handed sector bonus (T3R=0): Y = B−L/2 correctly gives
  lepton doublet Y = −1/2 and quark doublet Y = +1/6 (SM values).

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
    "experiments/20260619-g15-hypercharge",
    "experiments/20260618-g11-block-generators",
    "experiments/20260618-g10b-su3-in-so6",
    "experiments/20260617-g10-s6-so6-gauge",
]:
    sys.path.insert(0, os.path.join(_REPO, _subdir))

from g11_block_generators import K_S3, J_S3, lift_to_spinor, I4, I8  # noqa: E402
from g10b_su3_explicit import su3_generators  # noqa: E402
from g15_hypercharge import BmL, SP_SINGLET, SM_SINGLET, QUARK, AQUARK  # noqa: E402

# ── Constants ─────────────────────────────────────────────────────────────────

half = sp.Rational(1, 2)

su3_spin = [lift_to_spinor(C) for C in su3_generators()]

# T3R on 32-dim S³×S⁶ spinor (K₃ acts on S³, trivial on S⁶)
K3_32: sp.Matrix = kron(K_S3[2], I8)

# T3L on 32-dim (J₃ acts on S³, trivial on S⁶) — for independence check
J3_32: sp.Matrix = kron(J_S3[2], I8)

# SU(3)_color on 32-dim (C_i acts on S⁶, trivial on S³)
C32 = [kron(I4, C) for C in su3_spin]

# B−L on 32-dim (acts on S⁶, trivial on S³)
BmL_32: sp.Matrix = kron(I4, BmL)

# Hypercharge Y = T3R + (B−L)/2  (32×32 diagonal)
Y_32: sp.Matrix = K3_32 + BmL_32 * half

# Row ranges in kron(S³_4, S⁶_8) basis
L_UP = list(range(0, 8))  # |L,↑⟩⊗S⁶: T3L=+1/2, T3R=0
L_DN = list(range(8, 16))  # |L,↓⟩⊗S⁶: T3L=−1/2, T3R=0
R_UP = list(range(16, 24))  # |R,↑⟩⊗S⁶: T3R=+1/2
R_DN = list(range(24, 32))  # |R,↓⟩⊗S⁶: T3R=−1/2

# SM fermion row assignments: row = S³_sector_index × 8 + S⁶_index
SM_RH_FERMIONS = {
    "nu_R": (16 + SP_SINGLET, sp.Integer(0)),
    "e_R": (24 + SP_SINGLET, sp.Integer(-1)),
    "u_R_1": (16 + QUARK[0], sp.Rational(2, 3)),
    "u_R_2": (16 + QUARK[1], sp.Rational(2, 3)),
    "u_R_3": (16 + QUARK[2], sp.Rational(2, 3)),
    "d_R_1": (24 + QUARK[0], sp.Rational(-1, 3)),
    "d_R_2": (24 + QUARK[1], sp.Rational(-1, 3)),
    "d_R_3": (24 + QUARK[2], sp.Rational(-1, 3)),
}

SM_RH_ANTIFERMIONS = {
    "nu_Rbar": (24 + SM_SINGLET, sp.Integer(0)),
    "e_Rbar": (16 + SM_SINGLET, sp.Integer(1)),
    "u_Rbar_1": (24 + AQUARK[0], sp.Rational(-2, 3)),
    "u_Rbar_2": (24 + AQUARK[1], sp.Rational(-2, 3)),
    "u_Rbar_3": (24 + AQUARK[2], sp.Rational(-2, 3)),
    "d_Rbar_1": (16 + AQUARK[0], sp.Rational(1, 3)),
    "d_Rbar_2": (16 + AQUARK[1], sp.Rational(1, 3)),
    "d_Rbar_3": (16 + AQUARK[2], sp.Rational(1, 3)),
}


def main() -> bool:
    results: dict = {}
    passed = 0

    # ── T1: K₃^{32} is diagonal ──────────────────────────────────────────────
    t1_ok = K3_32.is_diagonal()
    results["T1_K3_diagonal"] = t1_ok
    passed += int(t1_ok)
    print(f"T1 K₃^{{32}} is diagonal: {'PASS' if t1_ok else 'FAIL'}")

    # ── T2: eigenvalue structure 16×0 + 8×(+1/2) + 8×(−1/2) ─────────────────
    diag_K3 = [K3_32[i, i] for i in range(32)]
    n0 = sum(1 for v in diag_K3 if v == 0)
    n_pos = sum(1 for v in diag_K3 if v == half)
    n_neg = sum(1 for v in diag_K3 if v == -half)
    t2_ok = n0 == 16 and n_pos == 8 and n_neg == 8
    results["T2_eigenvalue_structure"] = t2_ok
    passed += int(t2_ok)
    print(f"T2 K₃^{{32}} eigenvalues 16×0+8×(+½)+8×(−½): {'PASS' if t2_ok else 'FAIL'}")
    print(f"   16×0: {n0}  8×(+1/2): {n_pos}  8×(−1/2): {n_neg}")

    # ── T3: [K₃^{32}, J₃^{32}] = 0 — T3R and T3L are independent ────────────
    t3_ok = K3_32 * J3_32 - J3_32 * K3_32 == zeros(32, 32)
    results["T3_K3_J3_commute"] = t3_ok
    passed += int(t3_ok)
    print(f"T3 [K₃^{{32}}, J₃^{{32}}] = 0 (T3R ⊥ T3L): {'PASS' if t3_ok else 'FAIL'}")

    # ── T4: [K₃^{32}, C_i^{32}] = 0 for all 8 SU(3) generators ─────────────
    bad_c = [i for i, C in enumerate(C32) if K3_32 * C - C * K3_32 != zeros(32, 32)]
    t4_ok = len(bad_c) == 0
    results["T4_K3_commutes_SU3"] = t4_ok
    passed += int(t4_ok)
    print(
        f"T4 [K₃^{{32}}, C_i^{{32}}] = 0 for all 8 color gens: {'PASS' if t4_ok else 'FAIL'}"
        + (f" ({len(bad_c)} violations)" if not t4_ok else "")
    )

    # ── T5: Y_32 = K₃^{32} + BmL_32/2 is diagonal ───────────────────────────
    t5_ok = Y_32.is_diagonal()
    results["T5_Y_diagonal"] = t5_ok
    passed += int(t5_ok)
    print(f"T5 Y_32 = K₃^{{32}} + BmL_32/2 diagonal: {'PASS' if t5_ok else 'FAIL'}")
    if t5_ok:
        print(f"   Y values in R,↑ sector: {[Y_32[i, i] for i in R_UP]}")
        print(f"   Y values in R,↓ sector: {[Y_32[i, i] for i in R_DN]}")

    # ── T6: SM right-handed fermion Y values ──────────────────────────────────
    t6_fails = [(n, r, Y_32[r, r], y) for n, (r, y) in SM_RH_FERMIONS.items() if Y_32[r, r] != y]
    t6_ok = len(t6_fails) == 0
    results["T6_SM_fermion_Y"] = t6_ok
    passed += int(t6_ok)
    print(f"T6 SM right-handed fermion Y: {'PASS' if t6_ok else 'FAIL'}")
    for name, (row, Y_exp) in SM_RH_FERMIONS.items():
        ok = Y_32[row, row] == Y_exp
        print(f"   {name:<10}: row {row}, Y={Y_32[row, row]} (exp {Y_exp}) {'✓' if ok else '✗'}")

    # ── T7: SM right-handed antifermion Y values ──────────────────────────────
    t7_fails = [
        (n, r, Y_32[r, r], y) for n, (r, y) in SM_RH_ANTIFERMIONS.items() if Y_32[r, r] != y
    ]
    t7_ok = len(t7_fails) == 0
    results["T7_SM_antifermion_Y"] = t7_ok
    passed += int(t7_ok)
    print(f"T7 SM right-handed antifermion Y: {'PASS' if t7_ok else 'FAIL'}")
    for name, (row, Y_exp) in SM_RH_ANTIFERMIONS.items():
        ok = Y_32[row, row] == Y_exp
        print(f"   {name:<12}: row {row}, Y={Y_32[row, row]} (exp {Y_exp}) {'✓' if ok else '✗'}")

    # ── T8: Left-handed sector Y = B−L/2 (T3R=0) — SM doublet consistency ────
    # Lepton doublet: B−L=−1 → Y=−1/2  (SM Y_{L_lep}=−1/2 ✓)
    # Quark doublet:  B−L=+1/3 → Y=+1/6 (SM Y_{L_quark}=+1/6 ✓)
    Y_lep_L = Y_32[L_UP[SP_SINGLET], L_UP[SP_SINGLET]]
    Y_quark_L = Y_32[L_UP[QUARK[0]], L_UP[QUARK[0]]]
    t8_ok = Y_lep_L == sp.Rational(-1, 2) and Y_quark_L == sp.Rational(1, 6)
    results["T8_L_sector_doublet_Y"] = t8_ok
    passed += int(t8_ok)
    print(f"T8 Left sector doublet Y (SM consistency): {'PASS' if t8_ok else 'FAIL'}")
    print(
        f"   Lepton doublet Y = {Y_lep_L} (SM: −1/2 ✓)"
        if Y_lep_L == sp.Rational(-1, 2)
        else f"   FAIL: Y_lep_L={Y_lep_L}"
    )
    print(
        f"   Quark doublet Y  = {Y_quark_L} (SM: +1/6 ✓)"
        if Y_quark_L == sp.Rational(1, 6)
        else f"   FAIL: Y_quark_L={Y_quark_L}"
    )

    # ── T9: [Y_32, C_i^{32}] = 0 — hypercharge is color-neutral ─────────────
    bad_yc = [i for i, C in enumerate(C32) if Y_32 * C - C * Y_32 != zeros(32, 32)]
    t9_ok = len(bad_yc) == 0
    results["T9_Y_commutes_SU3"] = t9_ok
    passed += int(t9_ok)
    print(
        f"T9 [Y_32, C_i^{{32}}] = 0 (charge-color separation): {'PASS' if t9_ok else 'FAIL'}"
        + (f" ({len(bad_yc)} violations)" if not t9_ok else "")
    )

    # ── T10: Y_32 is Hermitian ────────────────────────────────────────────────
    t10_ok = Y_32 - Y_32.H == zeros(32, 32)
    results["T10_Y_hermitian"] = t10_ok
    passed += int(t10_ok)
    print(f"T10 Y_32 is Hermitian: {'PASS' if t10_ok else 'FAIL'}")

    # ── Summary ───────────────────────────────────────────────────────────────
    total = 10
    print(f"\n{'=' * 60}")
    print(f"G16 T3R FROM K₃: {passed}/{total} gates PASS")
    if passed == total:
        print("PASS_G16_T3R_GEOMETRIC_ORIGIN")
        print()
        print("Key result:")
        print("  T3R = K₃ eigenvalue on S³ right-handed block (±1/2, G11)")
        print("  B−L = spinor lift of J's U(1) center (G15)")
        print("  Y = K₃^{32} + BmL_32/2 — fully geometric (S³ × S⁶)")
        print("  Right-handed sector (16 states):")
        print("    ν_R(Y=0), u_R×3(Y=+2/3), e_R(Y=−1), d_R×3(Y=−1/3)")
        print("    ν̄_R(Y=0), ū_R×3(Y=−2/3), ē_R(Y=+1), d̄_R×3(Y=+1/3)")
        print("  Left-handed sector: Y=B−L/2 gives SM doublet hypercharges")
    else:
        print("INCOMPLETE — see failing gates above")

    out_path = os.path.join(_EXP_DIR, "g16_results.json")
    with open(out_path, "w") as f:
        json.dump({"passed": passed, "total": total, "gates": results}, f, indent=2)

    return passed == total


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
