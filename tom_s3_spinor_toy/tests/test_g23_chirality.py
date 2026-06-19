"""G23 tests: Chiral decomposition of H_F — SM chirality from γ_F."""

import os
import sys

import numpy as np

_g23_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g23-chirality")
sys.path.insert(0, _g23_dir)

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

from g23_chirality import (  # noqa: E402
    gamma_F,
    J_F,
    D_F,
    L_STATES,
    R_STATES,
    DIM_L,
    DIM_R,
    WITTEN_INDEX,
    GENS_PATI_SALAM,
    verify_gates,
    N,
    _anticomm_max,
    _comm_max,
)


# ── C1: γ_F² = I ──────────────────────────────────────────────────────────────


def test_gamma_squared_is_identity():
    """C1: γ_F is a Z₂ grading (γ_F² = I)."""
    assert np.allclose(gamma_F @ gamma_F, np.eye(N), atol=1e-12)


def test_gamma_is_diagonal():
    """γ_F is diagonal in the basis {S³ component × S⁶ mode}."""
    off_diag = gamma_F - np.diag(np.diag(gamma_F))
    assert np.allclose(off_diag, 0, atol=1e-12)


def test_gamma_eigenvalues_are_pm1():
    """γ_F has eigenvalues ±1 only (consistent with Z₂ grading)."""
    evals = np.diag(gamma_F).real
    assert np.all(np.abs(np.abs(evals) - 1) < 1e-12)


# ── C2: {D_F, γ_F} = 0 ────────────────────────────────────────────────────────


def test_df_anticommutes_with_gamma():
    """C2: {D_F, γ_F} = 0 — Yukawa flips chirality."""
    assert _anticomm_max(D_F, gamma_F) < 1e-10


def test_df_is_off_diagonal_in_chirality():
    """D_F maps exclusively L↔R: no diagonal blocks D[L,L] or D[R,R]."""
    assert np.allclose(D_F[np.ix_(L_STATES, L_STATES)], 0, atol=1e-10)
    assert np.allclose(D_F[np.ix_(R_STATES, R_STATES)], 0, atol=1e-10)


def test_df_off_diagonal_blocks_nonzero():
    """D_F connects L and R sectors (Yukawa coupling is non-trivial)."""
    assert np.max(np.abs(D_F[np.ix_(L_STATES, R_STATES)])) > 0.1
    assert np.max(np.abs(D_F[np.ix_(R_STATES, L_STATES)])) > 0.1


# ── C3: {J_F, γ_F} = 0 ────────────────────────────────────────────────────────


def test_jf_anticommutes_with_gamma():
    """C3: {J_F, γ_F} = 0 — KO-dimension 6 axiom (CPT flips chirality)."""
    assert _anticomm_max(J_F, gamma_F) < 1e-12


def test_jf_maps_between_chirality_sectors():
    """J_F maps H_F^+ ↔ H_F^- (confirmed by anticommuting with γ_F)."""
    # If J_F sends state k in L to J_F(k) in R, then J_F γ_F ψ = J_F(−ψ) = −J_F ψ
    # But γ_F J_F ψ = +J_F ψ → anticommutator = 0.
    assert np.allclose(J_F @ gamma_F + gamma_F @ J_F, 0, atol=1e-12)


# ── C4: [γ_F, G] = 0 ─────────────────────────────────────────────────────────


def test_gamma_commutes_with_all_gauge_generators():
    """C4: γ_F commutes with all 15 Pati-Salam generators."""
    for G in GENS_PATI_SALAM:
        assert _comm_max(gamma_F, G) < 1e-10


def test_gamma_commutes_with_su3():
    """SU(3) generators commute with γ_F (color doesn't break chirality)."""
    from g21_extended_schur import SU3_32

    for C in SU3_32:
        assert np.allclose(gamma_F @ C - C @ gamma_F, 0, atol=1e-10)


def test_gamma_commutes_with_bl():
    """U(1)_{B-L} commutes with γ_F (B-L is chirality-independent)."""
    from g21_extended_schur import BL_32

    assert np.allclose(gamma_F @ BL_32 - BL_32 @ gamma_F, 0, atol=1e-10)


# ── C5: Witten index = 0 ─────────────────────────────────────────────────────


def test_witten_index_zero():
    """C5: Witten index = dim(H_F^+) − dim(H_F^-) = 0."""
    assert WITTEN_INDEX == 0


def test_chiral_sectors_balanced():
    """Both chiral sectors have dimension 16 (half of H_F = ℂ^{32})."""
    assert DIM_L == 16
    assert DIM_R == 16


def test_chiral_sectors_partition_hf():
    """L_STATES ∪ R_STATES = {0, ..., 31} (complete partition)."""
    all_states = sorted(list(L_STATES) + list(R_STATES))
    assert all_states == list(range(N))


def test_l_sector_is_first_half():
    """L-chirality (γ_F=−1) = states 0-15 (S³ components 0,1 × S⁶ modes)."""
    assert list(L_STATES) == list(range(16))


def test_r_sector_is_second_half():
    """R-chirality (γ_F=+1) = states 16-31 (S³ components 2,3 × S⁶ modes)."""
    assert list(R_STATES) == list(range(16, 32))


# ── C6: SU(2)_L acts within H_F^- only ─────────────────────────────────────


def test_su2l_acts_only_on_left_sector():
    """C6: SU(2)_L generators act exclusively on H_F^- (left-chiral sector)."""
    from g21_extended_schur import J_32

    for k, J in enumerate(J_32):
        assert np.max(np.abs(J[np.ix_(R_STATES, R_STATES)])) < 1e-10, f"J_{k + 1} acts on R-sector"
        assert np.max(np.abs(J[np.ix_(R_STATES, L_STATES)])) < 1e-10, f"J_{k + 1} crosses sectors"
        assert np.max(np.abs(J[np.ix_(L_STATES, R_STATES)])) < 1e-10, f"J_{k + 1} crosses sectors"


def test_su2l_nontrivial_on_left_sector():
    """SU(2)_L has non-trivial action on H_F^- (actual doublet structure)."""
    from g21_extended_schur import J_32

    for J in J_32:
        J_LL = J[np.ix_(L_STATES, L_STATES)]
        assert np.max(np.abs(J_LL)) > 1e-6, "SU(2)_L acts trivially on L-sector"


# ── C7: SU(2)_R acts within H_F^+ only ─────────────────────────────────────


def test_su2r_acts_only_on_right_sector():
    """C7: SU(2)_R generators act exclusively on H_F^+ (right-chiral sector)."""
    from g21_extended_schur import K_32

    for k, K in enumerate(K_32):
        assert np.max(np.abs(K[np.ix_(L_STATES, L_STATES)])) < 1e-10, f"K_{k + 1} acts on L-sector"
        assert np.max(np.abs(K[np.ix_(L_STATES, R_STATES)])) < 1e-10, f"K_{k + 1} crosses sectors"
        assert np.max(np.abs(K[np.ix_(R_STATES, L_STATES)])) < 1e-10, f"K_{k + 1} crosses sectors"


def test_su2r_nontrivial_on_right_sector():
    """SU(2)_R has non-trivial action on H_F^+ (actual doublet structure)."""
    from g21_extended_schur import K_32

    for K in K_32:
        K_RR = K[np.ix_(R_STATES, R_STATES)]
        assert np.max(np.abs(K_RR)) > 1e-6, "SU(2)_R acts trivially on R-sector"


# ── Chirality mechanism: gauge quantum numbers, not spinor count ──────────────


def test_su2l_su2r_in_distinct_chiral_sectors():
    """SU(2)_L and SU(2)_R act in DIFFERENT chirality sectors (chiral SM structure)."""
    from g21_extended_schur import J_32, K_32

    J1_LL = J_32[0][np.ix_(L_STATES, L_STATES)]
    J1_RR = J_32[0][np.ix_(R_STATES, R_STATES)]
    K1_LL = K_32[0][np.ix_(L_STATES, L_STATES)]
    K1_RR = K_32[0][np.ix_(R_STATES, R_STATES)]
    # J_32 acts on L-sector but not R-sector
    assert np.max(np.abs(J1_LL)) > 1e-6
    assert np.max(np.abs(J1_RR)) < 1e-10
    # K_32 acts on R-sector but not L-sector
    assert np.max(np.abs(K1_RR)) > 1e-6
    assert np.max(np.abs(K1_LL)) < 1e-10


# ── Gate function ─────────────────────────────────────────────────────────────


def test_gate_function_passes():
    """verify_gates() returns PASS_G23_CHIRALITY (7/7)."""
    result = verify_gates()
    assert result == "PASS_G23_CHIRALITY (7/7)"
