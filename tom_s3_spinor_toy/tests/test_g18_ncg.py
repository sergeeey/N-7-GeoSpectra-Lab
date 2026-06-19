"""G18 tests: NCG finite Dirac operator D_F on the 32-dim S³×S⁶ spinor."""

import os
import sys

import sympy as sp

_g18_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g18-ncg-dirac-df")
sys.path.insert(0, _g18_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g17-electric-charge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g18_ncg import (  # noqa: E402
    CPT_PAIRS,
    D_F,
    PAIR_MAP,
    YUKAWA_PAIRS,
    Y_d,
    Y_e,
    Y_nu,
    Y_u,
    gamma_F,
    J_F,
)
from g17_electric_charge import Q_32  # noqa: E402


# ── Chirality γ_F ──────────────────────────────────────────────────────────────


def test_gamma_F_diagonal():
    """γ_F is diagonal."""
    assert gamma_F.is_diagonal()


def test_gamma_F_squares_to_identity():
    """γ_F² = I₃₂."""
    assert gamma_F**2 == sp.eye(32)


def test_gamma_F_L_minus_R_plus():
    """γ_F = −1 on L-sector (rows 0–15), +1 on R-sector (16–31)."""
    for i in range(16):
        assert gamma_F[i, i] == -1, f"row {i}: expected γ_F = -1"
    for i in range(16, 32):
        assert gamma_F[i, i] == 1, f"row {i}: expected γ_F = +1"


# ── Charge conjugation J_F ─────────────────────────────────────────────────────


def test_J_F_squares_to_identity():
    """J_F² = I₃₂ (charge conjugation is involution)."""
    assert J_F**2 == sp.eye(32)


def test_J_F_symmetric():
    """J_F = J_F.T (symmetric permutation matrix)."""
    assert J_F == J_F.T


def test_J_F_all_pairs_cross_sectors():
    """Every CPT pair has one L-row (0–15) and one R-row (16–31)."""
    for i, j in CPT_PAIRS:
        in_L = i < 16
        in_R = j >= 16
        assert (in_L and in_R) or (not in_L and in_R is not False), (
            f"pair ({i},{j}) does not cross L↔R"
        )
        # Exactly one in L and one in R
        assert (i < 16) != (j < 16), f"pair ({i},{j}): both on same side"


def test_J_F_anticommutes_with_gamma_F():
    """{J_F, γ_F} = 0 — KO-dimension 6, ε' = −1."""
    for i, j in CPT_PAIRS:
        assert gamma_F[i, i] + gamma_F[j, j] == 0, (
            f"pair ({i},{j}): γ_F[i]+γ_F[j] = {gamma_F[i, i] + gamma_F[j, j]}"
        )


# ── Finite Dirac operator D_F ─────────────────────────────────────────────────


def test_D_F_hermitian():
    """D_F = D_F† (Hermitian — D_F is real symmetric)."""
    assert D_F == D_F.T


def test_D_F_zero_diagonal():
    """D_F has zero diagonal (no fermion mass without Higgs VEV)."""
    for i in range(32):
        assert D_F[i, i] == 0, f"row {i}: D_F[{i},{i}] = {D_F[i, i]} ≠ 0"


def test_D_F_zero_LL_block():
    """D_F is zero on L×L block (rows 0–15 × 0–15)."""
    for i in range(16):
        for j in range(16):
            assert D_F[i, j] == 0, f"D_F[{i},{j}] = {D_F[i, j]} ≠ 0 in L×L"


def test_D_F_zero_RR_block():
    """D_F is zero on R×R block (rows 16–31 × 16–31)."""
    for i in range(16, 32):
        for j in range(16, 32):
            assert D_F[i, j] == 0, f"D_F[{i},{j}] = {D_F[i, j]} ≠ 0 in R×R"


def test_D_F_anticommutes_with_gamma_F():
    """{D_F, γ_F} = 0 — D_F is chiral (connects L↔R)."""
    for i, j, _ in YUKAWA_PAIRS:
        assert gamma_F[i, i] + gamma_F[j, j] == 0, (
            f"Yukawa ({i},{j}): γ_F[i]+γ_F[j] = {gamma_F[i, i] + gamma_F[j, j]}"
        )


def test_D_F_commutes_with_charge():
    """[D_F, Q_32] = 0 — D_F connects states of equal electric charge."""
    for i, j, _ in YUKAWA_PAIRS:
        assert Q_32[i, i] == Q_32[j, j], f"Yukawa ({i},{j}): Q[i]={Q_32[i, i]} ≠ Q[j]={Q_32[j, j]}"


def test_D_F_commutes_with_J_F():
    """[D_F, J_F] = 0 — KO-dimension 6, ε'' = +1.

    [D_F, J_F][i,k] = D_F[i, pair(k)] − D_F[pair(i), k].
    Verified for all Yukawa pairs using PAIR_MAP closure.
    """
    yukawa_lookup: dict[tuple[int, int], sp.Expr] = {}
    for i, j, y in YUKAWA_PAIRS:
        yukawa_lookup[(i, j)] = y
        yukawa_lookup[(j, i)] = y

    for i, j, y in YUKAWA_PAIRS:
        pi, pj = PAIR_MAP[i], PAIR_MAP[j]
        lhs = yukawa_lookup.get((i, pj), sp.Integer(0))
        rhs = yukawa_lookup.get((pi, j), sp.Integer(0))
        assert sp.expand(lhs - rhs) == 0, f"[D_F,J_F]≠0 at Yukawa pair ({i},{j}): {lhs} ≠ {rhs}"


def test_D_F_exactly_four_yukawa_couplings():
    """D_F has exactly 4 free Yukawa couplings: Y_nu, Y_e, Y_u, Y_d."""
    distinct = {y for _, _, y in YUKAWA_PAIRS}
    assert distinct == {Y_nu, Y_e, Y_u, Y_d}


def test_D_F_yukawa_pair_count():
    """D_F has exactly 16 Yukawa matrix connections (8 particle + 8 CPT-partner)."""
    assert len(YUKAWA_PAIRS) == 16


def test_D_F_neutrino_coupling():
    """ν_L(0) ↔ ν_R(16) carries Y_nu; CPT partner ν̄_L(15) ↔ ν̄_R(31) also Y_nu."""
    assert D_F[0, 16] == Y_nu
    assert D_F[16, 0] == Y_nu
    assert D_F[15, 31] == Y_nu
    assert D_F[31, 15] == Y_nu


def test_D_F_electron_coupling():
    """e_L(8) ↔ e_R(24) carries Y_e; CPT partner ē_L(7) ↔ ē_R(23) also Y_e."""
    assert D_F[8, 24] == Y_e
    assert D_F[24, 8] == Y_e
    assert D_F[7, 23] == Y_e
    assert D_F[23, 7] == Y_e


def test_D_F_up_quark_triplet():
    """u_L(3,5,6) ↔ u_R(19,21,22) — 3 colors, each coupling Y_u."""
    for il, ir in [(3, 19), (5, 21), (6, 22)]:
        assert D_F[il, ir] == Y_u, f"u-quark pair ({il},{ir}): {D_F[il, ir]}"
        assert D_F[ir, il] == Y_u


def test_D_F_down_quark_triplet():
    """d_L(11,13,14) ↔ d_R(27,29,30) — 3 colors, each coupling Y_d."""
    for il, ir in [(11, 27), (13, 29), (14, 30)]:
        assert D_F[il, ir] == Y_d, f"d-quark pair ({il},{ir}): {D_F[il, ir]}"
        assert D_F[ir, il] == Y_d
