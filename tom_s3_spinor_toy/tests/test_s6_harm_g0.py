"""Regression gate: S6-HARM-G0 — SO(6) Clifford algebra foundation for S⁶.

Pins the algebraic foundation for S⁶ harmonic analysis parallel to Tom's S³ construction.
Claim: 6D hermitian gamma matrices Γ₁..Γ₆ (8×8, tensor products of Pauli matrices)
give a correct SO(6) Clifford algebra with 4⊕4̄ Weyl spinor splitting.
"""

import sympy as sp
from sympy import I, eye, zeros, Matrix, kronecker_product as kron, simplify

# ── Pauli matrices ──────────────────────────────────────────────────────────
s0 = eye(2)
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])

G = [
    kron(s1, s0, s0),
    kron(s2, s0, s0),
    kron(s3, s1, s0),
    kron(s3, s2, s0),
    kron(s3, s3, s1),
    kron(s3, s3, s2),
]
I8 = eye(8)
G7 = kron(s3, s3, s3)


def J(a: int, b: int) -> Matrix:
    return (G[a - 1] * G[b - 1] - G[b - 1] * G[a - 1]) / 4


def test_clifford_anticommutation():
    """T1: {Γ_a, Γ_b} = 2δ_{ab}I₈ for all 21 pairs."""
    for a in range(6):
        for b in range(a, 6):
            anti = G[a] * G[b] + G[b] * G[a]
            expected = 2 * I8 if a == b else zeros(8)
            assert simplify(anti - expected) == zeros(8), (
                f"Clifford relation failed for a={a + 1}, b={b + 1}"
            )


def test_so6_lie_algebra():
    """T2: so(6) algebra [J_{ab},J_{cd}]=δ_{ad}J_{bc}-δ_{ac}J_{bd}+δ_{bc}J_{ad}-δ_{bd}J_{ac}."""
    # [J₁₂, J₂₃] = J₁₃
    assert simplify(J(1, 2) * J(2, 3) - J(2, 3) * J(1, 2) - J(1, 3)) == zeros(8)
    # [J₁₂, J₃₄] = 0  (commuting generators)
    assert simplify(J(1, 2) * J(3, 4) - J(3, 4) * J(1, 2)) == zeros(8)
    # [J₁₃, J₃₅] = J₁₅
    assert simplify(J(1, 3) * J(3, 5) - J(3, 5) * J(1, 3) - J(1, 5)) == zeros(8)


def test_cartan_generators_commute():
    """T3: H₁=J₁₂, H₂=J₃₄, H₃=J₅₆ mutually commute (rank-3 Cartan subalgebra)."""
    H1, H2, H3 = J(1, 2), J(3, 4), J(5, 6)
    assert simplify(H1 * H2 - H2 * H1) == zeros(8)
    assert simplify(H1 * H3 - H3 * H1) == zeros(8)
    assert simplify(H2 * H3 - H3 * H2) == zeros(8)


def test_cartan_explicit_form():
    """T4: H_i = (i/2)(σ₃ in i-th tensor factor)."""
    assert simplify(J(1, 2) - (I / 2) * kron(s3, s0, s0)) == zeros(8)
    assert simplify(J(3, 4) - (I / 2) * kron(s0, s3, s0)) == zeros(8)
    assert simplify(J(5, 6) - (I / 2) * kron(s0, s0, s3)) == zeros(8)


def test_chirality_operator():
    """T5: Γ₇=σ₃⊗σ₃⊗σ₃ squares to I₈ and has eigenvalues ±1 with multiplicity 4 each."""
    assert simplify(G7 * G7 - I8) == zeros(8)
    eigs = {simplify(e): m for e, m in G7.eigenvals().items()}
    assert eigs.get(1) == 4, f"Γ₇ eigenvalue +1 should have multiplicity 4, got {eigs}"
    assert eigs.get(-1) == 4, f"Γ₇ eigenvalue -1 should have multiplicity 4, got {eigs}"


def test_chiral_split_4_4bar():
    """T6: Γ₇ splits 8-component spinor into 4⊕4̄ with correct SO(6) weights."""
    basis = [Matrix([0] * 8) for _ in range(8)]
    for k in range(8):
        basis[k][k] = 1

    chiral_plus = [k for k, v in enumerate(basis) if (G7 * v)[k] == 1]
    chiral_minus = [k for k, v in enumerate(basis) if (G7 * v)[k] == -1]

    assert len(chiral_plus) == 4
    assert len(chiral_minus) == 4

    # 4 representation: even number of −1/2 weights
    for k in chiral_plus:
        bits = [(k >> (2 - i)) & 1 for i in range(3)]
        n_minus = sum(bits)  # bits=1 → σ₃ eigenvalue −1 → weight −1/2
        assert n_minus % 2 == 0, f"State {k} in 4-rep has odd minus-weights: bits={bits}"

    # 4̄ representation: odd number of −1/2 weights
    for k in chiral_minus:
        bits = [(k >> (2 - i)) & 1 for i in range(3)]
        n_minus = sum(bits)
        assert n_minus % 2 == 1, f"State {k} in 4̄-rep has even minus-weights: bits={bits}"


def test_generators_preserve_chirality():
    """T7: All 15 SO(6) generators J_{ab} commute with Γ₇."""
    for a in range(1, 7):
        for b in range(a + 1, 7):
            comm = J(a, b) * G7 - G7 * J(a, b)
            assert simplify(comm) == zeros(8), f"J_{a}{b} does not commute with Γ₇"
