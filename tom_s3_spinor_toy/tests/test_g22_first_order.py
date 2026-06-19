"""G22 tests: NCG first-order condition — subalgebra compatibility with D_F."""

import os
import sys

import numpy as np

_g22_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g22-first-order")
sys.path.insert(0, _g22_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g18-ncg-dirac-df"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g21-extended-schur"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g22_first_order import (  # noqa: E402
    D_F,
    J_F,
    GENS_SU3,
    GENS_BL,
    GENS_SU2L,
    GENS_SU2R,
    max_fo_violation,
    right_action,
    viol_su3,
    viol_bl,
    viol_su2l,
    viol_su2r,
    viol_full,
    EXPECTED_SU2_VIOLATION,
    verify_gates,
    N,
)


# ── F1: SU(3) — first-order condition holds trivially ────────────────────────


def test_su3_fo_passes():
    """F1 MAIN: SU(3) satisfies first-order condition (D_F is color singlet)."""
    assert viol_su3 < 1e-8


def test_su3_commutes_with_df():
    """[D_F, C_k] = 0 for all SU(3) generators — making first-order trivial."""
    from g22_first_order import comm

    for Ck in GENS_SU3:
        assert np.allclose(comm(D_F, Ck), 0, atol=1e-10)


def test_su3_fo_not_cheating():
    """First-order holds for SU(3) because [D, C_k] = 0, not because R_k = 0."""
    # Right-action SU(3) generators are non-zero
    R_su3 = right_action(GENS_SU3)
    for Rk in R_su3:
        assert np.max(np.abs(Rk)) > 1e-6, "Right-action SU(3) generator is zero"


# ── F2: U(1)_{B-L} — first-order condition holds trivially ──────────────────


def test_bl_fo_passes():
    """F2 MAIN: U(1)_{B-L} satisfies first-order condition (D_F preserves B-L)."""
    assert viol_bl < 1e-8


def test_bl_commutes_with_df():
    """[D_F, BL] = 0 — D_F is B-L neutral (each YUKAWA_PAIR has same B-L value)."""
    from g22_first_order import comm
    from g21_extended_schur import BL_32

    assert np.allclose(comm(D_F, BL_32), 0, atol=1e-10)


# ── F3: SU(2)_L — first-order condition FAILS ────────────────────────────────


def test_su2l_fo_fails():
    """F3 MAIN: SU(2)_L violates first-order condition (electroweak broken by D_F)."""
    assert viol_su2l > 0.1


def test_su2l_violation_exact_quarter():
    """F3: SU(2)_L violation = 0.25 exactly (geometric factor (1/2)(1/2))."""
    assert abs(viol_su2l - EXPECTED_SU2_VIOLATION) < 1e-8


def test_su2l_does_not_commute_with_df():
    """[D_F, J_k] ≠ 0 for SU(2)_L generators — the source of the first-order violation."""
    from g22_first_order import comm

    for Jk in GENS_SU2L:
        commutator_norm = np.max(np.abs(comm(D_F, Jk)))
        assert commutator_norm > 1e-6, f"[D_F, J_k] = 0 unexpectedly (max={commutator_norm:.2e})"


def test_su2l_violation_physical_chain():
    """The violation traces: ν_L → [D,J1] → e_R → R_J1 → ν_R, value = -0.25."""
    from g22_first_order import comm

    J1 = GENS_SU2L[0]
    R_J1 = right_action([J1])[0]
    nested = comm(comm(D_F, J1), R_J1)
    # Entry (0, 16): ν_L row, ν_R column
    assert abs(nested[0, 16] + 0.25) < 1e-8, (
        f"Violation at (ν_L, ν_R) = {nested[0, 16]} (expected -0.25)"
    )


# ── F4: SU(2)_R — first-order condition FAILS ────────────────────────────────


def test_su2r_fo_fails():
    """F4 MAIN: SU(2)_R violates first-order condition."""
    assert viol_su2r > 0.1


def test_su2r_violation_exact_quarter():
    """F4: SU(2)_R violation = 0.25 exactly (same geometric factor as SU(2)_L)."""
    assert abs(viol_su2r - EXPECTED_SU2_VIOLATION) < 1e-8


def test_su2l_su2r_violation_equal():
    """SU(2)_L and SU(2)_R violations are equal by symmetry of the construction."""
    assert abs(viol_su2l - viol_su2r) < 1e-8


# ── F5: J_F² = I ─────────────────────────────────────────────────────────────


def test_jf_squared_is_identity():
    """F5: J_F is its own inverse (J_F² = I), confirming right-action formula."""
    assert np.allclose(J_F @ J_F, np.eye(N), atol=1e-12)


def test_jf_is_real():
    """J_F has zero imaginary part — it is a real permutation matrix."""
    assert np.allclose(J_F.imag, 0, atol=1e-12)


# ── Full Pati-Salam inherits SU(2) failure ────────────────────────────────────


def test_full_pati_salam_fo_fails():
    """Full Pati-Salam violation = same 0.25 (SU(2) sectors dominate)."""
    assert viol_full > 0.1
    assert abs(viol_full - EXPECTED_SU2_VIOLATION) < 1e-8


def test_color_bl_subgroup_passes():
    """SU(3) × U(1)_{B-L} together: first-order condition holds."""
    color_bl_gens = GENS_SU3 + GENS_BL
    R_color_bl = right_action(color_bl_gens)
    viol = max_fo_violation(D_F, color_bl_gens, R_color_bl)
    assert viol < 1e-8


# ── Physical interpretation ───────────────────────────────────────────────────


def test_maximal_compatible_subalgebra_is_color_bl():
    """The maximal subalgebra with first-order condition = SU(3) × U(1)_{B-L}."""
    # SU(3) × U(1)_{B-L}: passes
    color_bl_gens = GENS_SU3 + GENS_BL
    R_cb = right_action(color_bl_gens)
    assert max_fo_violation(D_F, color_bl_gens, R_cb) < 1e-8
    # Adding any SU(2): fails
    assert (
        max_fo_violation(D_F, color_bl_gens + GENS_SU2L, right_action(color_bl_gens + GENS_SU2L))
        > 0.1
    )
    assert (
        max_fo_violation(D_F, color_bl_gens + GENS_SU2R, right_action(color_bl_gens + GENS_SU2R))
        > 0.1
    )


def test_violation_proportional_to_yukawa():
    """SU(2)_L violation scales linearly with Yukawa coupling value."""
    from g18_ncg import Y_nu, Y_e, Y_u, Y_d, YUKAWA_PAIRS

    def make_D(y):
        D = np.zeros((N, N), dtype=complex)
        for i, j, c in YUKAWA_PAIRS:
            v = float(c.subs({Y_nu: y, Y_e: y, Y_u: y, Y_d: y}))
            D[i, j] = D[j, i] = v
        return D

    R_su2l = right_action(GENS_SU2L)
    v1 = max_fo_violation(make_D(1.0), GENS_SU2L, R_su2l)
    v2 = max_fo_violation(make_D(2.0), GENS_SU2L, R_su2l)
    # Violation scales as Y² (bilinear in D_F)... actually linear in Y:
    # [[D, J], R_J] is linear in D, which is linear in Y
    assert abs(v2 / v1 - 2.0) < 1e-8, f"Expected 2× scaling, got {v2 / v1:.4f}"


# ── Gate function ─────────────────────────────────────────────────────────────


def test_gate_function_passes():
    """verify_gates() returns PASS_G22_FIRST_ORDER (5/5)."""
    result = verify_gates()
    assert result == "PASS_G22_FIRST_ORDER (5/5)"
