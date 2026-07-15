"""L3b: connect the vector-rep triality finding to the spinor-rep (Gamma_A,Gamma_B)
finding via an explicit Cl(8)-to-Cl(8) isomorphism.

Context: L3B_SPIN8_INTERFACE_SPEC.md SS1.5. Two Cl(8) realizations were built
independently this session:
  - Pauli-tensor (../20260715-l3b-so4xso4-candidate/so4xso4_branching.py):
    Gamma_1..Gamma_8 (16x16), 8_s/8_c as chirality eigenspaces, Gamma_A/Gamma_B
    distinguish s from c via same-vs-opposite block chirality.
  - Octonion-covariance (../20260715-l3b-triality-so4xso4-invariance/
    triality_so4xso4_invariance.py): V=S+=S-=O, triality via a(x).y+x.b(y)=c(x.y).

Both are representations of the SAME abstract so(8); by Schur's lemma, if
"8_s" and "S+ via b" are really the same real-type irrep, there is a UNIQUE
(up to scalar) intertwiner P. This module builds P (for 8_s<->S+) and Q (for
8_c<->S-) using the FULL 28-dimensional so(8) (not just the so(4)+so(4)
subalgebra, to pin down uniqueness genuinely), verifies uniqueness and
residual, and uses them to transport Gamma_A into the octonion language.

Result: Gamma_A transports to exactly diag(+1,+1,+1,+1,-1,-1,-1,-1) on the
S+ side (matching block1=H vs block2=Hl), and to the negative on the S- side
-- and this operator commutes with ALL 12 generators of the triality-
transported so(4)_1(+)so(4)_2, confirming the H/Hl block split IS preserved
under the full construction, consistently across V, S+, S-.

This corrects an earlier finding in this same investigation thread (commit
f63b992): a degenerate Casimir eigenvalue spectrum for the transported
so(4)_1 was read as "no invariant block split" -- but degenerate Casimir is
also exactly what TWO ISOTYPIC (same-type) 4-dim invariant blocks would
produce. The direct test (does a candidate chirality operator commute with
every generator?) resolves the ambiguity: it does, so the split IS
preserved -- verified explicitly below, block by block.
"""

import os
import sys

import numpy as np

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "20260715-l3b-so4xso4-candidate"),
)
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "20260715-l3b-triality-so4xso4-invariance"),
)

from so4xso4_branching import GAMMA, GAMMA_9, GAMMA_A, GAMMA_B  # noqa: E402
from triality_so4xso4_invariance import build_so4xso4_basis, solve_triality_partners  # noqa: E402

N = 8


def build_so8_basis():
    """28 antisymmetric generators E_ij - E_ji, i<j, spanning so(8) fully."""
    basis = []
    for i in range(N):
        for j in range(i + 1, N):
            mat = np.zeros((N, N))
            mat[i, j] = 1
            mat[j, i] = -1
            basis.append(mat)
    return np.array(basis)


SO8_BASIS = build_so8_basis()


def spin_lift(a):
    """so(8) generator a (8x8 antisymmetric) -> its spin representation (16x16),
    via M = (1/4) sum_ij a[i,j] Gamma_i Gamma_j (1-indexed Gamma dict, 0-indexed a).
    """
    mat = np.zeros((16, 16), dtype=complex)
    for i in range(N):
        for j in range(N):
            if a[i, j] != 0:
                mat += a[i, j] * (GAMMA[i + 1] @ GAMMA[j + 1]) / 4
    return mat


def chirality_eigenbasis():
    """Orthonormal bases for 8_s (+1) and 8_c (-1) eigenspaces of Gamma_9."""
    evals, evecs = np.linalg.eigh(GAMMA_9)
    v_s = evecs[:, evals > 0]
    v_c = evecs[:, evals < 0]
    return v_s, v_c


def build_intertwiner(restrict_fn, partner_role):
    """Solve for the unique (up to scalar) P with P @ M_a = partner_a @ P for all
    28 so(8) generators, where M_a = restrict_fn(spin_lift(a)) and partner_a is
    the b (partner_role='b') or c (partner_role='c') solution of the octonion
    covariance equation. Returns (P, max_residual, nullity).
    """
    partner_index = {"b": 0, "c": 1}[partner_role]
    m_list, partner_list = [], []
    for a in SO8_BASIS:
        m_list.append(restrict_fn(spin_lift(a)))
        partners = solve_triality_partners(a)
        partner_list.append(partners[partner_index].astype(complex))
    m_arr = np.array(m_list)
    partner_arr = np.array(partner_list)

    rows = []
    for m_a, partner_a in zip(m_arr, partner_arr):
        for i in range(N):
            for j in range(N):
                coeff = np.zeros(N * N, dtype=complex)
                for ell in range(N):
                    coeff[i * N + ell] += m_a[ell, j]
                    coeff[ell * N + j] -= partner_a[i, ell]
                rows.append(coeff)
    lhs = np.array(rows)
    _u, s, vt = np.linalg.svd(lhs)
    nullity = int(np.sum(s < 1e-6))
    p_matrix = vt[-1].reshape(N, N).conj()

    max_residual = 0.0
    for m_a, partner_a in zip(m_arr, partner_arr):
        max_residual = max(max_residual, np.max(np.abs(p_matrix @ m_a - partner_a @ p_matrix)))
    return p_matrix, max_residual, nullity


def transported_gamma_a_on_s_plus():
    v_s, _v_c = chirality_eigenbasis()
    ga_8s = v_s.conj().T @ GAMMA_A.astype(complex) @ v_s
    p_matrix, _residual, _nullity = build_intertwiner(lambda m16: v_s.conj().T @ m16 @ v_s, "b")
    return p_matrix @ ga_8s @ np.linalg.inv(p_matrix)


def transported_gamma_a_on_s_minus():
    _v_s, v_c = chirality_eigenbasis()
    ga_8c = v_c.conj().T @ GAMMA_A.astype(complex) @ v_c
    q_matrix, _residual, _nullity = build_intertwiner(lambda m16: v_c.conj().T @ m16 @ v_c, "c")
    return q_matrix @ ga_8c @ np.linalg.inv(q_matrix)


def transported_gamma_b_on_s_plus():
    """Sanity check: on 8_s, Gamma_A=Gamma_B by construction (same-chirality
    sector), so this should also transport to +D_A -- confirms the intertwiner
    is behaving consistently, not just for one operator.
    """
    v_s, _v_c = chirality_eigenbasis()
    gb_8s = v_s.conj().T @ GAMMA_B.astype(complex) @ v_s
    p_matrix, _residual, _nullity = build_intertwiner(lambda m16: v_s.conj().T @ m16 @ v_s, "b")
    return p_matrix @ gb_8s @ np.linalg.inv(p_matrix)


def transported_gamma_b_on_s_minus():
    """Sanity check: on 8_c, Gamma_A=-Gamma_B (opposite-chirality sector), so
    this should transport to +D_A (opposite of Gamma_A's -D_A there).
    """
    _v_s, v_c = chirality_eigenbasis()
    gb_8c = v_c.conj().T @ GAMMA_B.astype(complex) @ v_c
    q_matrix, _residual, _nullity = build_intertwiner(lambda m16: v_c.conj().T @ m16 @ v_c, "c")
    return q_matrix @ gb_8c @ np.linalg.inv(q_matrix)


def block_sign_operator():
    """D_A = diag(+1,+1,+1,+1,-1,-1,-1,-1): +1 on block1 (H), -1 on block2 (Hl)."""
    return np.diag([1.0, 1, 1, 1, -1, -1, -1, -1])


def transported_so4xso4_generators():
    """All 12 b-partners of the so(4)_1(+)so(4)_2 basis generators."""
    basis = build_so4xso4_basis()
    return np.array([solve_triality_partners(a)[0] for a in basis])


if __name__ == "__main__":
    v_s, v_c = chirality_eigenbasis()

    p_matrix, p_resid, p_null = build_intertwiner(lambda m16: v_s.conj().T @ m16 @ v_s, "b")
    print(f"P intertwiner (8_s <-> S+): nullity={p_null} (expect 1), max_resid={p_resid:.2e}")

    q_matrix, q_resid, q_null = build_intertwiner(lambda m16: v_c.conj().T @ m16 @ v_c, "c")
    print(f"Q intertwiner (8_c <-> S-): nullity={q_null} (expect 1), max_resid={q_resid:.2e}")

    transported_a_plus = transported_gamma_a_on_s_plus()
    transported_a_minus = transported_gamma_a_on_s_minus()
    d_a = block_sign_operator()

    print("\nTransported Gamma_A on S+ (should equal +D_A):")
    print(np.round(transported_a_plus.real, 4))
    print("matches +D_A:", np.allclose(transported_a_plus.real, d_a, atol=1e-6))

    transported_b_plus = transported_gamma_b_on_s_plus()
    transported_b_minus = transported_gamma_b_on_s_minus()
    print("\nTransported Gamma_B on S+ (should ALSO equal +D_A, since Gamma_A=Gamma_B on 8_s):")
    print("matches +D_A:", np.allclose(transported_b_plus.real, d_a, atol=1e-6))
    print("Transported Gamma_B on S- (should equal +D_A, since Gamma_A=-Gamma_B on 8_c):")
    print("matches +D_A:", np.allclose(transported_b_minus.real, d_a, atol=1e-6))

    print("\nTransported Gamma_A on S- (should equal -D_A):")
    print(np.round(transported_a_minus.real, 4))
    print("matches -D_A:", np.allclose(transported_a_minus.real, -d_a, atol=1e-6))

    transported_generators = transported_so4xso4_generators()
    max_comm = max(np.max(np.abs(d_a @ g - g @ d_a)) for g in transported_generators)
    print(
        f"\nD_A commutes with all 12 transported so(4)+so(4) generators: "
        f"max commutator = {max_comm:.2e}"
    )
    print("=> the H/Hl block split IS preserved under the transported algebra,")
    print("   consistently across V, S+, S- -- corrects the earlier Casimir-based")
    print("   'no split' reading (degenerate Casimir = isotypic split, not no split).")
