"""G22: NCG first-order condition — maximal subalgebra compatible with D_F.

First-order condition (Connes real spectral triple axiom):
  [[D_F, a], J_F b* J_F⁻¹] = 0   for all a, b ∈ A

QUESTION: For which subalgebra of the Pati-Salam gauge algebra
  G_PS = SU(2)_L × SU(2)_R × SU(3) × U(1)_{B-L}
does the SM Yukawa D_F satisfy the NCG first-order condition?

ANALYTIC PREDICTION:
  [D_F, C_k] = 0 for all SU(3) generators (D_F connects same S⁶ index → color singlet)
  [D_F, B_L] = 0 for U(1)_{B-L} (same reason — D_F is B-L preserving)
  → [[D_F, C_k], anything] = 0 trivially, so SU(3) PASSES trivially.
  → [[D_F, BL], anything] = 0 trivially, so U(1)_{B-L} PASSES trivially.

  [D_F, J_k] ≠ 0 for SU(2)_L: D_F maps ν_L→ν_R and e_L→e_R separately,
    so J_k (which mixes ν_L↔e_L) doesn't commute with D_F.
  → [[D_F, J_k], J_F J_k J_F] = −0.25 (non-zero), so SU(2)_L FAILS.

  [D_F, K_k] ≠ 0 for SU(2)_R: analogous reasoning for R-sector.
  → SU(2)_R FAILS with the same violation magnitude.

CONCLUSION:
  The NCG first-order condition holds for the COLOR-B-L subalgebra
    SU(3) × U(1)_{B-L}
  and FAILS for the ELECTROWEAK algebra
    SU(2)_L × SU(2)_R.

PHYSICAL MEANING:
  D_F (SM Yukawa) is compatible with the NCG first-order axiom only
  for the UNBROKEN symmetry of the SM vacuum (color × B-L).
  The violation by SU(2)_L and SU(2)_R is EXPECTED: the Yukawa coupling
  IS the electroweak symmetry-breaking term.

  This reproduces the CCM result from the opposite direction:
  CCM takes A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ) (SM NCG algebra, a smaller algebra
  that includes only the scalar part of SU(2) acting on right-handed fields)
  and SHOWS the first-order condition holds.  We start from Pati-Salam
  (larger algebra) and find it FAILS, pointing to the SM subalgebra as
  the maximal compatible algebra.

  The violation magnitude 0.25 = (1/2)² × 1.0 matches
    |[D,J1]_{0,24}| × |[J_F J1 J_F]_{24,16}| = (1/2) × (1/2) = 0.25
  — a geometric factor of (1/2) from each SU(2) Lie algebra generator.

GATES:
  F1: |[[D_F, SU(3)], R]| < 1e-8  (SU(3) PASSES: D_F is color singlet)
  F2: |[[D_F, BL], R]|    < 1e-8  (U(1)_{B-L} PASSES: D_F preserves B-L)
  F3: |[[D_F, SU(2)_L], R]| > 0.1 (SU(2)_L FAILS: electroweak broken by D_F)
  F4: |[[D_F, SU(2)_R], R]| > 0.1 (SU(2)_R FAILS: same structure)
  F5: J_F² = I (confirming right-action formula R_k = J_F G_k J_F)

sm_derivation_claimed = False.
λ = FREE_COUPLING_PARAMETER.
"""

import os
import sys

import numpy as np

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g21-extended-schur"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g18_ncg import J_F as J_F_sym, YUKAWA_PAIRS, Y_nu, Y_e, Y_u, Y_d  # noqa: E402
from g21_extended_schur import J_32, K_32, SU3_32, BL_32, _to_np  # noqa: E402

N = 32  # dim(H_F)


# ── Build D_F numerically ─────────────────────────────────────────────────────


def _build_D(subs: dict) -> np.ndarray:
    D = np.zeros((N, N), dtype=complex)
    for i, j, coup in YUKAWA_PAIRS:
        c = complex(coup.subs(subs))
        D[i, j] = c
        D[j, i] = c
    return D


_unit = {Y_nu: 1, Y_e: 1, Y_u: 1, Y_d: 1}
D_F: np.ndarray = _build_D(_unit)

# ── J_F: real permutation matrix, J_F² = I ───────────────────────────────────

J_F: np.ndarray = _to_np(J_F_sym)

# ── Generator sets ────────────────────────────────────────────────────────────

GENS_SU3: list[np.ndarray] = SU3_32  # 8 generators of SU(3)
GENS_BL: list[np.ndarray] = [BL_32]  # 1 generator of U(1)_{B-L}
GENS_SU2L: list[np.ndarray] = J_32  # 3 generators of SU(2)_L
GENS_SU2R: list[np.ndarray] = K_32  # 3 generators of SU(2)_R

# All 15 Pati-Salam generators (full gauge group from S³×S⁶)
GENS_PATI_SALAM: list[np.ndarray] = J_32 + K_32 + SU3_32 + [BL_32]


# ── Right action: R_k = J_F G_k J_F  (J_F real, self-inverse) ───────────────


def right_action(gens: list[np.ndarray]) -> list[np.ndarray]:
    """Compute right-action generators R_k = J_F G_k J_F for each G_k."""
    return [J_F @ G @ J_F for G in gens]


# ── Core: nested commutator ───────────────────────────────────────────────────


def comm(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def max_fo_violation(
    D: np.ndarray,
    left_gens: list[np.ndarray],
    right_gens: list[np.ndarray],
) -> float:
    """Max |[[D, L_a], R_b]| over all left × right generator pairs."""
    worst = 0.0
    for La in left_gens:
        c1 = comm(D, La)
        for Rb in right_gens:
            c2 = comm(c1, Rb)
            worst = max(worst, float(np.max(np.abs(c2))))
    return worst


# ── Pre-computed violations per subalgebra ────────────────────────────────────

# Right-action partners for each subalgebra
_R_su3 = right_action(GENS_SU3)
_R_bl = right_action(GENS_BL)
_R_su2l = right_action(GENS_SU2L)
_R_su2r = right_action(GENS_SU2R)
_R_ps = right_action(GENS_PATI_SALAM)

viol_su3: float = max_fo_violation(D_F, GENS_SU3, _R_su3)
viol_bl: float = max_fo_violation(D_F, GENS_BL, _R_bl)
viol_su2l: float = max_fo_violation(D_F, GENS_SU2L, _R_su2l)
viol_su2r: float = max_fo_violation(D_F, GENS_SU2R, _R_su2r)
viol_full: float = max_fo_violation(D_F, GENS_PATI_SALAM, _R_ps)

# Predicted magnitude: (1/2) × (1/2) = 0.25  (each SU(2) generator has norm 1/2)
EXPECTED_SU2_VIOLATION: float = 0.25


# ── Gate verification ─────────────────────────────────────────────────────────


def verify_gates() -> str:
    gates_pass = 0

    # F1: SU(3) passes (trivially: [D_F, C_k] = 0 since D_F is color singlet)
    assert viol_su3 < 1e-8, f"F1 FAIL: SU(3) FO violation = {viol_su3:.3e} (expected 0)"
    gates_pass += 1

    # F2: U(1)_{B-L} passes (trivially: [D_F, BL] = 0 since D_F preserves B-L)
    assert viol_bl < 1e-8, f"F2 FAIL: U(1)_{{B-L}} FO violation = {viol_bl:.3e} (expected 0)"
    gates_pass += 1

    # F3: SU(2)_L fails — electroweak symmetry broken by D_F
    assert viol_su2l > 0.1, f"F3 FAIL: SU(2)_L FO violation = {viol_su2l:.3e} (expected > 0.1)"
    # Check predicted magnitude: (1/2)² = 0.25
    assert abs(viol_su2l - EXPECTED_SU2_VIOLATION) < 1e-8, (
        f"F3 FAIL: SU(2)_L violation = {viol_su2l:.6f} ≠ {EXPECTED_SU2_VIOLATION} (geometric prediction)"
    )
    gates_pass += 1

    # F4: SU(2)_R fails — same structure as SU(2)_L
    assert viol_su2r > 0.1, f"F4 FAIL: SU(2)_R FO violation = {viol_su2r:.3e} (expected > 0.1)"
    assert abs(viol_su2r - EXPECTED_SU2_VIOLATION) < 1e-8, (
        f"F4 FAIL: SU(2)_R violation = {viol_su2r:.6f} ≠ {EXPECTED_SU2_VIOLATION}"
    )
    gates_pass += 1

    # F5: J_F² = I (confirms right-action formula R_k = J_F G_k J_F)
    jf2_err = float(np.max(np.abs(J_F @ J_F - np.eye(N))))
    assert jf2_err < 1e-12, f"F5 FAIL: J_F² ≠ I (error = {jf2_err:.2e})"
    gates_pass += 1

    return f"PASS_G22_FIRST_ORDER ({gates_pass}/5)"


# ── Main ──────────────────────────────────────────────────────────────────────


if __name__ == "__main__":
    print("G22: NCG First-Order Condition — Subalgebra Analysis")
    print("=" * 55)
    print(f"N = {N},  D_F = SM Yukawa (all Y = 1)")
    print()
    print("First-order condition: [[D_F, L_a], J_F G_b J_F] = 0 ?")
    print()
    print(f"  SU(3)      (8 gens): max violation = {viol_su3:.3e}   PASS (D_F is color singlet)")
    print(f"  U(1)_{{B-L}} (1 gen):  max violation = {viol_bl:.3e}   PASS (D_F preserves B-L)")
    print(
        f"  SU(2)_L    (3 gens): max violation = {viol_su2l:.3e}   FAIL (electroweak broken by D_F)"
    )
    print(f"  SU(2)_R    (3 gens): max violation = {viol_su2r:.3e}   FAIL (same)")
    print(f"  Full PS    (15 gens): max violation = {viol_full:.3e}  FAIL (from SU(2) sectors)")
    print()
    print("Predicted SU(2) violation: |[D,J1]_{{0,24}}| × |R_{{24,16}}| = (1/2)(1/2) = 0.25")
    print(f"  Measured: {viol_su2l:.6f} (exact match)")
    print()
    print("CONCLUSION:")
    print(
        "  D_F is a NCG first-order operator w.r.t. SU(3) × U(1)_{{B-L}}  (unbroken vacuum symmetry)"
    )
    print(
        "  D_F is NOT a first-order operator w.r.t. SU(2)_L × SU(2)_R    (broken by Yukawa / Higgs)"
    )
    print("  Maximal compatible subalgebra = color × B-L  ↔  SM vacuum after electroweak SSB")
    print()
    print(verify_gates())
