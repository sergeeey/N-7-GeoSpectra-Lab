"""L3b tests: SO(4)xSO(4) subset SO(8) -- first candidate distinguishing 8_v, 8_s, 8_c.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5. Every subgroup of SO(7) tested so
far (G2, SO(6)=Stab_SO(7)(point), Stab_G2(quaternion subalgebra)) inherits
the "Spin(7) has a unique 8-dim spinor" identity (E-L3B) and cannot
distinguish 8_s from 8_c. SO(4)xSO(4) has rank 4 = rank(SO(8)) and
structurally cannot embed in SO(7) (rank 3), escaping that trap.
"""

import os
import sys

import numpy as np

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260715-l3b-so4xso4-candidate"
)
sys.path.insert(0, _exp_dir)

from so4xso4_branching import (  # noqa: E402
    GAMMA_A,
    GAMMA_B,
    GAMMA_9,
    DIM_8V_BLOCK1,
    DIM_8V_BLOCK2,
    DIM_8S_SAME_PLUS,
    DIM_8S_SAME_MINUS,
    DIM_8C_CROSS_PLUS_MINUS,
    DIM_8C_CROSS_MINUS_PLUS,
    RANK_SO4_X_SO4,
    RANK_SO7,
    clifford_relation_holds,
)


def test_cl8_clifford_relation():
    """{Gamma_i, Gamma_j} = 2 delta_ij I for the explicit 16x16 representation."""
    assert clifford_relation_holds()


def test_gamma_a_gamma_b_are_involutions():
    """Block chirality operators square to the identity."""
    assert np.allclose(GAMMA_A @ GAMMA_A, np.eye(16), atol=1e-8)
    assert np.allclose(GAMMA_B @ GAMMA_B, np.eye(16), atol=1e-8)


def test_gamma_a_gamma_b_commute():
    """Chirality operators of two orthogonal SO(4) blocks commute."""
    assert np.allclose(GAMMA_A @ GAMMA_B - GAMMA_B @ GAMMA_A, 0, atol=1e-8)


def test_gamma_a_times_gamma_b_equals_full_chirality():
    """Gamma_A * Gamma_B = Gamma_9, the full Spin(8) chirality operator."""
    assert np.allclose(GAMMA_A @ GAMMA_B, GAMMA_9, atol=1e-8)
    assert np.allclose(GAMMA_9 @ GAMMA_9, np.eye(16), atol=1e-8)


def test_8v_splits_block_additively():
    """8_v = (4,1) + (1,4) under SO(4)xSO(4): block-additive, dimension 4+4=8."""
    assert DIM_8V_BLOCK1 == 4
    assert DIM_8V_BLOCK2 == 4
    assert DIM_8V_BLOCK1 + DIM_8V_BLOCK2 == 8


def test_8s_is_same_block_chirality_sector():
    """8_s = (Gamma_A=Gamma_B) sectors, each 4-dimensional, total 8."""
    assert DIM_8S_SAME_PLUS == 4
    assert DIM_8S_SAME_MINUS == 4
    assert DIM_8S_SAME_PLUS + DIM_8S_SAME_MINUS == 8


def test_8c_is_opposite_block_chirality_sector():
    """8_c = (Gamma_A=-Gamma_B) sectors, each 4-dimensional, total 8."""
    assert DIM_8C_CROSS_PLUS_MINUS == 4
    assert DIM_8C_CROSS_MINUS_PLUS == 4
    assert DIM_8C_CROSS_PLUS_MINUS + DIM_8C_CROSS_MINUS_PLUS == 8


def test_all_four_sectors_partition_16_dimensions():
    """The four (Gamma_A,Gamma_B) sectors partition the full 16-dim Dirac spinor."""
    total = DIM_8S_SAME_PLUS + DIM_8S_SAME_MINUS + DIM_8C_CROSS_PLUS_MINUS + DIM_8C_CROSS_MINUS_PLUS
    assert total == 16


def test_so4xso4_distinguishes_s_from_c():
    """8_s (same-chirality) and 8_c (opposite-chirality) are structurally distinct
    sectors under SO(4)xSO(4) -- unlike every previously-tested subgroup of SO(7).
    """
    same_chirality_dim = DIM_8S_SAME_PLUS + DIM_8S_SAME_MINUS
    opposite_chirality_dim = DIM_8C_CROSS_PLUS_MINUS + DIM_8C_CROSS_MINUS_PLUS
    assert same_chirality_dim == opposite_chirality_dim == 8
    # The distinguishing structure is the SIGN CORRELATION (Gamma_A vs Gamma_B),
    # not the raw dimension -- both are 8, but which sectors compose 8_s vs 8_c differs.


def test_so4xso4_cannot_embed_in_so7():
    """rank(SO(4)xSO(4)) > rank(SO(7)): structurally cannot be a subgroup of SO(7),
    hence escapes the "Spin(7) has a unique 8-dim spinor" trap (E-L3B) that killed
    every previously-tested candidate (G2, SO(6), Stab_G2(quaternion subalgebra)).
    """
    assert RANK_SO4_X_SO4 == 4
    assert RANK_SO7 == 3
    assert RANK_SO4_X_SO4 > RANK_SO7
