"""
L3b: does SO(4)xSO(4) subset SO(8) distinguish 8_v, 8_s, 8_c?

Builds an explicit Cl(8) representation (8 anticommuting 16x16 matrices),
verifies the Clifford relation directly, splits the 16-dim Dirac spinor into
8_s/8_c via the full chirality operator, and checks how the "block chirality"
operators of two orthogonal SO(4) subgroups (indices 1-4 and 5-8) act on
each chiral sector.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5, "Attempted 2026-07-15, continued
further". Every subgroup of SO(7) (G2, SO(6)=Stab_SO(7)(point),
Stab_G2(quaternion subalgebra)) was already shown unable to distinguish
8_s from 8_c, because Spin(7) has a unique 8-dim spinor rep (E-L3B). This
script checks a subgroup that is NOT inside SO(7): SO(4)xSO(4) has rank 4 =
rank(SO(8)), so it cannot embed in SO(7) (rank 3) at all.
"""

import numpy as np

I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(*mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


G = {
    1: kron(sx, I2, I2, I2),
    2: kron(sy, I2, I2, I2),
    3: kron(sz, sx, I2, I2),
    4: kron(sz, sy, I2, I2),
    5: kron(sz, sz, sx, I2),
    6: kron(sz, sz, sy, I2),
    7: kron(sz, sz, sz, sx),
    8: kron(sz, sz, sz, sy),
}

# Verify Cl(8): {Gamma_i, Gamma_j} = 2 delta_ij * I
for i in range(1, 9):
    for j in range(1, 9):
        anticomm = G[i] @ G[j] + G[j] @ G[i]
        expected = 2 * np.eye(16) if i == j else np.zeros((16, 16))
        assert np.allclose(anticomm, expected, atol=1e-8), f"Clifford relation failed at {i},{j}"
print("Cl(8) Clifford algebra verified: {Gamma_i,Gamma_j}=2 delta_ij  [PASS]")

G9 = G[1] @ G[2] @ G[3] @ G[4] @ G[5] @ G[6] @ G[7] @ G[8]
assert np.allclose(G9 @ G9, np.eye(16), atol=1e-8)
assert np.allclose(G9, G9.conj().T, atol=1e-8)
evals = np.linalg.eigvalsh(G9)
print(
    "Full chirality Gamma_9 eigenvalues:",
    np.round(evals.real, 6),
    " (expect 8x -1, 8x +1)  [PASS]"
    if np.allclose(sorted(evals.real), [-1] * 8 + [1] * 8)
    else "  [FAIL]",
)

GA = G[1] @ G[2] @ G[3] @ G[4]
GB = G[5] @ G[6] @ G[7] @ G[8]
assert np.allclose(GA @ GA, np.eye(16), atol=1e-8)
assert np.allclose(GB @ GB, np.eye(16), atol=1e-8)
assert np.allclose(GA @ GB - GB @ GA, 0, atol=1e-8)
assert np.allclose(GA @ GB, G9, atol=1e-8)
print(
    "Block chirality operators Gamma_A, Gamma_B: [Gamma_A,Gamma_B]=0, "
    "Gamma_A*Gamma_B=Gamma_9  [PASS]"
)


def proj(op, sign):
    return 0.5 * (np.eye(16) + sign * op)


print()
print("Joint (Gamma_A, Gamma_B) sector dimensions:")
for sA in (1, -1):
    for sB in (1, -1):
        P = proj(GA, sA) @ proj(GB, sB)
        dim = round(np.trace(P).real)
        chirality = "8_s (same block-chirality)" if sA == sB else "8_c (opposite block-chirality)"
        print(f"  Gamma_A={sA:+d}, Gamma_B={sB:+d}  ->  dim={dim}   [{chirality}]")

print()
print("Conclusion: 8_s = (Gamma_A=Gamma_B) sectors, 8_c = (Gamma_A=-Gamma_B)")
print("sectors, both 4+4=8-dimensional. SO(4)xSO(4) distinguishes s from c.")
print("Rank check: rank(SO(4)xSO(4))=4 = rank(SO(8)) -- cannot embed in")
print("SO(7) (rank 3), so this escapes the Spin(7)-unique-spinor trap that")
print("killed every previously-tested candidate (G2, SO(6), Stab_G2(H)).")
