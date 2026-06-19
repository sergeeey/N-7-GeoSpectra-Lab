"""G24 tests: Blind spectrum — SO(4)×G₂ rep theory predicts SM fermion content."""

import os
import sys

import numpy as np

_g24_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g24-blind-spectrum"
)
sys.path.insert(0, _g24_dir)

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

from g24_blind_spectrum import (  # noqa: E402
    C2_SU3,
    C2_J,
    C2_K,
    evals_su3,
    evals_J,
    evals_K,
    evals_JK,
    SU3_N_SINGLET,
    SU3_N_TRIPLET,
    SU3_CASIMIR_F,
    SU2J_N_SINGLET,
    SU2J_N_DOUBLET,
    SU2J_CASIMIR,
    SU2K_N_SINGLET,
    SU2K_N_DOUBLET,
    _casimir_spread,
    verify_gates,
    N,
)


# ── B1: SU(3) Casimir on 8-dim S⁶ ────────────────────────────────────────


def test_su3_casimir_has_two_singlets():
    """Spin(7)→G₂→SU(3) branching: 2 SU(3) singlet modes (1+1) in S⁶ spinor."""
    assert SU3_N_SINGLET == 2


def test_su3_casimir_has_six_non_singlets():
    """Spin(7)→G₂→SU(3) branching: 6 triplet/antitriplet modes (3+3̄) in S⁶ spinor."""
    assert SU3_N_TRIPLET == 6


def test_su3_casimir_non_singlets_uniform():
    """3 and 3̄ have the same Casimir — same non-abelian Casimir eigenvalue."""
    assert _casimir_spread(evals_su3) < 1e-8


def test_su3_casimir_nonzero_for_triplets():
    """SU(3) Casimir > 0 for color-charged modes (non-singlets are non-trivial)."""
    assert SU3_CASIMIR_F > 1e-8


def test_su3_casimir_dimension_check():
    """8-dim S⁶ spinor: 2 singlets + 6 non-singlets = 8."""
    assert SU3_N_SINGLET + SU3_N_TRIPLET == 8


def test_su3_casimir_is_positive_semidefinite():
    """C₂_SU3 (with sign convention for antihermitian generators) is positive semidefinite."""
    assert np.all(evals_su3 > -1e-10)


# ── B2: SU(2)_L Casimir on 4-dim S³ ─────────────────────────────────────


def test_su2l_casimir_two_singlets():
    """(2,1)+(1,2) decomposition: 2 SU(2)_L singlet states (the (1,2) sector)."""
    assert SU2J_N_SINGLET == 2


def test_su2l_casimir_one_doublet():
    """(2,1)+(1,2) decomposition: 2 SU(2)_L doublet states (the (2,1) sector)."""
    assert SU2J_N_DOUBLET == 2


def test_su2l_casimir_doublet_value():
    """C₂(j=1/2) = 3/4 — standard SU(2) spin-1/2 Casimir in physics normalization."""
    assert abs(SU2J_CASIMIR - 0.75) < 1e-8


def test_su2l_casimir_is_positive_semidefinite():
    """C₂_J ≥ 0: SU(2)_L generators are hermitian."""
    assert np.all(evals_J > -1e-10)


# ── B3: SU(2)_R Casimir on 4-dim S³ ─────────────────────────────────────


def test_su2r_casimir_two_singlets():
    """(2,1)+(1,2) decomposition: 2 SU(2)_R singlet states (the (2,1) sector)."""
    assert SU2K_N_SINGLET == 2


def test_su2r_casimir_one_doublet():
    """(2,1)+(1,2) decomposition: 2 SU(2)_R doublet states (the (1,2) sector)."""
    assert SU2K_N_DOUBLET == 2


def test_su2r_casimir_doublet_value():
    """C₂_R(j=1/2) = 3/4 — same as SU(2)_L by symmetry."""
    nonzero = evals_K[evals_K > 1e-8]
    assert len(nonzero) == 2
    assert abs(nonzero[0] - 0.75) < 1e-8


# ── B4: Complementarity C₂(J) + C₂(K) = 3/4 × I₄ ───────────────────────


def test_jk_casimir_uniform():
    """C₂(J)+C₂(K) = (3/4)I₄: every S³ state is in (2,1) or (1,2), never both."""
    spread = float(np.max(evals_JK) - np.min(evals_JK))
    assert spread < 1e-8


def test_jk_casimir_value():
    """C₂(J)+C₂(K) = 3/4 on all S³ states (sum of complementary doublet Casimirs)."""
    assert abs(evals_JK[0] - 0.75) < 1e-8


def test_jk_casimir_not_zero():
    """Doublet structure exists: total Casimir is nonzero."""
    assert evals_JK[0] > 1e-8


def test_l_and_r_doublet_sectors_are_complementary():
    """States with C₂(J) = 3/4 have C₂(K) = 0, and vice versa."""
    d_J = np.linalg.eigh(C2_J)
    vecs_J = d_J[1]  # columns = eigenvectors
    # For each J eigenvector: J-doublet (eigenvalue 3/4) → K-singlet (eigenvalue 0)
    for i in range(4):
        ev_J = float(d_J[0][i])
        vec = vecs_J[:, i]
        ev_K = float(np.real(vec @ C2_K @ vec))
        assert abs(ev_J + ev_K - 0.75) < 1e-8, (
            f"State {i}: C₂(J)={ev_J:.4f} + C₂(K)={ev_K:.4f} = {ev_J + ev_K:.4f} ≠ 0.75"
        )


# ── B5: Dimension count ────────────────────────────────────────────────────


def test_hf_dimension_from_blind_prediction():
    """4 S³ components × 8 S⁶ modes = 32 = dim(H_F) — pure group theory prediction."""
    n_s3 = SU2J_N_SINGLET + SU2J_N_DOUBLET
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET
    assert n_s3 * n_s6 == N


def test_s3_spinor_dimension():
    """Spin(4) spinor = 4-dimensional (matches dim of S³ component index)."""
    assert SU2J_N_SINGLET + SU2J_N_DOUBLET == 4


def test_s6_spinor_dimension():
    """Spin(7) spinor = 8-dimensional (matches number of S⁶ modes)."""
    assert SU3_N_SINGLET + SU3_N_TRIPLET == 8


# ── B6: Fermion sector sizes ───────────────────────────────────────────────


def test_left_sector_size():
    """L-chiral sector: SU(2)_L doublet (2) × S⁶ modes (8) = 16 states."""
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET
    assert SU2J_N_DOUBLET * n_s6 == 16


def test_right_sector_size():
    """R-chiral sector: SU(2)_R doublet (2) × S⁶ modes (8) = 16 states."""
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET
    assert SU2K_N_DOUBLET * n_s6 == 16


def test_total_sector_balance():
    """L + R = 32 (equal chirality sectors — consistent with Witten index = 0)."""
    n_s6 = SU3_N_SINGLET + SU3_N_TRIPLET
    assert SU2J_N_DOUBLET * n_s6 + SU2K_N_DOUBLET * n_s6 == N


# ── Casimir matrices (structural checks) ─────────────────────────────────


def test_su3_casimir_is_diagonal_in_color_blocks():
    """SU(3) Casimir commutes with all SU(3) generators (is in the center)."""
    from g21_extended_schur import SU3_32

    su3_8 = [G[np.ix_(list(range(8)), list(range(8)))].real for G in SU3_32]
    for G in su3_8:
        assert np.allclose(C2_SU3 @ G - G @ C2_SU3, 0, atol=1e-10)


def test_j_casimir_commutes_with_su2l():
    """C₂(J) is in the center of SU(2)_L — commutes with all J generators."""
    from g21_extended_schur import J_32

    S3 = [0, 8, 16, 24]
    for J in J_32:
        J4 = J[np.ix_(S3, S3)]
        assert np.allclose(C2_J @ J4 - J4 @ C2_J, 0, atol=1e-10)


# ── Gate function ─────────────────────────────────────────────────────────


def test_gate_function_passes():
    """verify_gates() returns PASS_G24_BLIND_SPECTRUM (6/6)."""
    assert verify_gates() == "PASS_G24_BLIND_SPECTRUM (6/6)"
