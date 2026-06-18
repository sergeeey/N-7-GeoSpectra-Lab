"""G10: tests for S⁶ → SO(6) gauge structure (Tom's mechanism, s₂=6)."""

import os
import sys

import sympy as sp

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
)
from g10_s6_so6_gauge import so6_generators, complex_structure  # noqa: E402


def test_15_antisymmetric_generators():
    """so(6) has 15 generators, all antisymmetric."""
    gens = so6_generators()
    assert len(gens) == 15
    assert all(M.T == -M for _, M in gens)


def test_algebra_closes():
    """Every commutator of so(6) generators stays antisymmetric (closes in so(6))."""
    mats = [M for _, M in so6_generators()]
    for A in mats:
        for B in mats:
            C = A * B - B * A
            assert C.T == -C


def test_dim_so6_equals_su4():
    """dim so(6) = 15 = dim su(4) (local isomorphism)."""
    assert len(so6_generators()) == 4**2 - 1


def test_complex_structure_squares_to_minus_identity():
    """J² = −I."""
    J = complex_structure()
    assert J * J == -sp.eye(6)


def test_J_is_sum_of_three_generators():
    """J = M01 + M23 + M45 (the U(1) generator inside so(6))."""
    idx = {ab: M for ab, M in so6_generators()}
    J = complex_structure()
    assert sp.simplify(J - (idx[(0, 1)] + idx[(2, 3)] + idx[(4, 5)])) == sp.zeros(6, 6)


def test_J_commutant_is_u3_dim9():
    """The commutant of J in so(6) is u(3), dimension 9 (so su(3)=8 + u(1)=1)."""
    mats = [M for _, M in so6_generators()]
    J = complex_structure()
    cs = sp.symbols("c0:15")
    X = sp.zeros(6, 6)
    for c, M in zip(cs, mats):
        X += c * M
    comm = X * J - J * X
    A = sp.Matrix([[sp.diff(comm[i, j], c) for c in cs] for i in range(6) for j in range(6)])
    assert 15 - A.rank() == 9


def test_vector6_splits_3_3bar():
    """J eigenvalues are ±i with multiplicity 3 each → 6 = 3 ⊕ 3̄."""
    J = complex_structure()
    ev = J.eigenvals()
    assert ev.get(sp.I, 0) == 3
    assert ev.get(-sp.I, 0) == 3
