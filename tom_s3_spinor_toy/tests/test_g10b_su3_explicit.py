"""G10-B: tests for explicit SU(3) ↪ SO(6) embedding."""

import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
)
from g10b_su3_explicit import frob, su3_generators  # noqa: E402
from g10_s6_so6_gauge import complex_structure, so6_generators  # noqa: E402

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
)


def test_exactly_8_generators():
    """su(3) has exactly 8 generators."""
    assert len(su3_generators()) == 8


def test_algebra_closes():
    """All [Tₐ,Tᵦ] remain in su(3): commute with J and are J-traceless."""
    su3 = su3_generators()
    J = complex_structure()
    for Ta in su3:
        for Tb in su3:
            comm = Ta * Tb - Tb * Ta
            assert sp.simplify(comm * J - J * comm) == sp.zeros(6, 6)
            assert sp.simplify(frob(comm, J)) == 0


def test_u1_independent_of_su3():
    """J ∉ span(su3): u(1) and su(3) are linearly independent."""
    su3 = su3_generators()
    J = complex_structure()
    J_proj = sum((frob(J, T) / frob(T, T) * T for T in su3), start=sp.zeros(6, 6))
    assert sp.simplify(J - J_proj) != sp.zeros(6, 6)


def test_gram_matrix_negative_definite():
    """Gram matrix Tr(TₐTᵦ) is negative definite → compact Lie algebra."""
    su3 = su3_generators()
    G = np.array(
        [[float(sp.trace(su3[a] * su3[b])) for b in range(8)] for a in range(8)],
        dtype=float,
    )
    eigs = np.linalg.eigvalsh(G)
    assert np.all(eigs < 0), f"Non-negative eigenvalue found: {eigs.max():.6f}"


def test_rank_2_cartan():
    """Centralizer of a generic Cartan element has dim 2 = rank su(3)."""
    su3 = su3_generators()
    mats = [M for _, M in so6_generators()]
    M_01, M_23, M_45 = mats[0], mats[9], mats[14]
    H_gen = 3 * M_01 - M_23 - 2 * M_45  # generic: a+b+c=0, all different
    cs = sp.symbols("x0:8")
    X_gen = sum((c * T for c, T in zip(cs, su3)), start=sp.zeros(6, 6))
    comm = H_gen * X_gen - X_gen * H_gen
    B = sp.Matrix([[sp.diff(comm[i, j], c) for c in cs] for i in range(6) for j in range(6)])
    assert 8 - B.rank() == 2


def test_su3_in_so6():
    """All su(3) generators are antisymmetric (in so(6)) and J-preserving."""
    su3 = su3_generators()
    J = complex_structure()
    for T in su3:
        assert T.T == -T
        assert sp.simplify(T * J - J * T) == sp.zeros(6, 6)
