"""L3b: does SO(4)xSO(4) subset SO(8) distinguish 8_v, 8_s, 8_c?

Builds an explicit Cl(8) representation (8 anticommuting 16x16 matrices),
splits the 16-dim Dirac spinor into 8_s/8_c via the full chirality operator,
and checks how the "block chirality" operators of two orthogonal SO(4)
subgroups (indices 1-4 and 5-8) act on each chiral sector.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5, "Attempted 2026-07-15, continued
further". Every subgroup of SO(7) (G2, SO(6)=Stab_SO(7)(point),
Stab_G2(quaternion subalgebra)) was already shown unable to distinguish
8_s from 8_c, because Spin(7) has a unique 8-dim spinor rep (E-L3B). This
module checks a subgroup that is NOT inside SO(7): SO(4)xSO(4) has rank 4 =
rank(SO(8)), so it cannot embed in SO(7) (rank 3) at all.
"""

import numpy as np

_I2 = np.eye(2)
_SX = np.array([[0, 1], [1, 0]], dtype=complex)
_SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
_SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def _kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def build_cl8_gammas():
    """Return dict {1..8: 16x16 matrix} realizing Cl(8): {Gamma_i,Gamma_j}=2 delta_ij."""
    return {
        1: _kron(_SX, _I2, _I2, _I2),
        2: _kron(_SY, _I2, _I2, _I2),
        3: _kron(_SZ, _SX, _I2, _I2),
        4: _kron(_SZ, _SY, _I2, _I2),
        5: _kron(_SZ, _SZ, _SX, _I2),
        6: _kron(_SZ, _SZ, _SY, _I2),
        7: _kron(_SZ, _SZ, _SZ, _SX),
        8: _kron(_SZ, _SZ, _SZ, _SY),
    }


GAMMA = build_cl8_gammas()

GAMMA_A = GAMMA[1] @ GAMMA[2] @ GAMMA[3] @ GAMMA[4]  # first SO(4) block chirality (e0..e3)
GAMMA_B = GAMMA[5] @ GAMMA[6] @ GAMMA[7] @ GAMMA[8]  # second SO(4) block chirality (e4..e7)
GAMMA_9 = GAMMA_A @ GAMMA_B  # full Spin(8) chirality operator


def clifford_relation_holds():
    """{Gamma_i, Gamma_j} = 2 delta_ij * I for all i,j in 1..8."""
    for i in range(1, 9):
        for j in range(1, 9):
            anticomm = GAMMA[i] @ GAMMA[j] + GAMMA[j] @ GAMMA[i]
            expected = 2 * np.eye(16) if i == j else np.zeros((16, 16))
            if not np.allclose(anticomm, expected, atol=1e-8):
                return False
    return True


def _proj(op, sign):
    return 0.5 * (np.eye(16) + sign * op)


def sector_dim(sign_a, sign_b):
    """Dimension of the joint (Gamma_A=sign_a, Gamma_B=sign_b) eigenspace."""
    proj = _proj(GAMMA_A, sign_a) @ _proj(GAMMA_B, sign_b)
    return round(np.trace(proj).real)


# 8_v under SO(4)xSO(4): trivially (4,1) + (1,4) -- vector splits along the two blocks.
DIM_8V_BLOCK1 = 4
DIM_8V_BLOCK2 = 4

# 8_s = same-block-chirality sectors (Gamma_A = Gamma_B); 8_c = opposite (Gamma_A = -Gamma_B).
DIM_8S_SAME_PLUS = sector_dim(+1, +1)
DIM_8S_SAME_MINUS = sector_dim(-1, -1)
DIM_8C_CROSS_PLUS_MINUS = sector_dim(+1, -1)
DIM_8C_CROSS_MINUS_PLUS = sector_dim(-1, +1)

RANK_SO4_X_SO4 = 4  # rank(SO(4)) + rank(SO(4)) = 2 + 2
RANK_SO7 = 3

if __name__ == "__main__":
    print("Cl(8) Clifford algebra verified:", clifford_relation_holds())
    print("Gamma_A^2=I:", np.allclose(GAMMA_A @ GAMMA_A, np.eye(16), atol=1e-8))
    print("Gamma_B^2=I:", np.allclose(GAMMA_B @ GAMMA_B, np.eye(16), atol=1e-8))
    print("[Gamma_A,Gamma_B]=0:", np.allclose(GAMMA_A @ GAMMA_B - GAMMA_B @ GAMMA_A, 0, atol=1e-8))
    print()
    print("8_s (same block-chirality) sectors:", DIM_8S_SAME_PLUS, "+", DIM_8S_SAME_MINUS)
    print(
        "8_c (opposite block-chirality) sectors:",
        DIM_8C_CROSS_PLUS_MINUS,
        "+",
        DIM_8C_CROSS_MINUS_PLUS,
    )
    print()
    print(
        f"rank(SO(4)xSO(4))={RANK_SO4_X_SO4} > rank(SO(7))={RANK_SO7}",
        "-- cannot embed in SO(7), escapes the unique-Spin(7)-spinor trap.",
    )
