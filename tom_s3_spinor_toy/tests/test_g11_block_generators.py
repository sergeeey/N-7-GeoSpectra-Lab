"""G11 tests: 32×32 block generators J, K, C_i for Ψ = ψ_{S³}⊗ψ_{S⁶}."""

import os
import sys

import pytest
import sympy as sp
from sympy import I, zeros, kronecker_product as kron

# ── add experiment to path ──────────────────────────────────────────────────
_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"
)
_g10_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge")
_g10b_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6")
for _p in [_exp_dir, _g10_dir, _g10b_dir]:
    sys.path.insert(0, _p)

from g11_block_generators import (  # noqa: E402
    J_S3,
    K_S3,
    J_spinor,
    lift_to_spinor,
    su3_generators,
    I4,
    I8,
    half,
)

su3_vec = su3_generators()
su3_spin = [lift_to_spinor(C) for C in su3_vec]

R = sp.Rational


def _eps3(a, b, c):
    if (a, b, c) in {(0, 1, 2), (1, 2, 0), (2, 0, 1)}:
        return 1
    if (a, b, c) in {(0, 2, 1), (2, 1, 0), (1, 0, 2)}:
        return -1
    return 0


# ── S³ algebra tests ─────────────────────────────────────────────────────────


@pytest.mark.parametrize("a,b", [(a, b) for a in range(3) for b in range(3)])
def test_su2L_algebra(a, b):
    """[J_a,J_b] = iε_{abc}J_c for SU(2)_L."""
    comm = J_S3[a] * J_S3[b] - J_S3[b] * J_S3[a]
    expected = sum((I * _eps3(a, b, c) * J_S3[c] for c in range(3)), zeros(4))
    assert comm - expected == zeros(4)


@pytest.mark.parametrize("a,b", [(a, b) for a in range(3) for b in range(3)])
def test_su2R_algebra(a, b):
    """[K_a,K_b] = iε_{abc}K_c for SU(2)_R."""
    comm = K_S3[a] * K_S3[b] - K_S3[b] * K_S3[a]
    expected = sum((I * _eps3(a, b, c) * K_S3[c] for c in range(3)), zeros(4))
    assert comm - expected == zeros(4)


@pytest.mark.parametrize("a,b", [(a, b) for a in range(3) for b in range(3)])
def test_JL_KR_commute(a, b):
    """[J_L, K_R] = 0: L and R sectors decouple."""
    assert J_S3[a] * K_S3[b] - K_S3[b] * J_S3[a] == zeros(4)


def test_J3_eigenvalues():
    """J₃ = diag(½, -½, 0, 0) — weak isospin T3L."""
    assert J_S3[2] == sp.Matrix([[half, 0, 0, 0], [0, -half, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


def test_K3_eigenvalues():
    """K₃ = diag(0, 0, ½, -½) — right isospin T3R."""
    assert K_S3[2] == sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, half, 0], [0, 0, 0, -half]])


# ── Spinor lift tests ────────────────────────────────────────────────────────


def test_lift_gives_8x8():
    """Each lifted generator is 8×8."""
    for C in su3_spin:
        assert C.shape == (8, 8)


def test_lift_nonzero():
    """No generator lifts to the zero matrix."""
    for i, C in enumerate(su3_spin):
        assert C != zeros(8), f"C_{i + 1}^spin is zero"


@pytest.mark.parametrize("i,j", [(i, j) for i in range(8) for j in range(8)])
def test_spinor_lift_homomorphism(i, j):
    """φ([Cᵢ,Cⱼ]^vec) = [φ(Cᵢ),φ(Cⱼ)]^spin for all 64 pairs."""
    comm_vec = su3_vec[i] * su3_vec[j] - su3_vec[j] * su3_vec[i]
    lhs = lift_to_spinor(comm_vec)
    rhs = su3_spin[i] * su3_spin[j] - su3_spin[j] * su3_spin[i]
    assert lhs - rhs == zeros(8), f"hom. fails for (i={i},j={j})"


# ── 32×32 tensor product tests ───────────────────────────────────────────────


def test_J3_32_diagonal_structure():
    """J₃^{32} = kron(diag(½,-½,0,0), I₈): 8×(½) + 8×(-½) + 16×(0)."""
    J3_32 = kron(J_S3[2], I8)
    diag = [J3_32[i, i] for i in range(32)]
    assert sum(1 for v in diag if v == half) == 8
    assert sum(1 for v in diag if v == -half) == 8
    assert sum(1 for v in diag if v == 0) == 16


def test_K3_32_diagonal_structure():
    """K₃^{32} = kron(diag(0,0,½,-½), I₈): 16×(0) + 8×(½) + 8×(-½)."""
    K3_32 = kron(K_S3[2], I8)
    diag = [K3_32[i, i] for i in range(32)]
    assert sum(1 for v in diag if v == half) == 8
    assert sum(1 for v in diag if v == -half) == 8
    assert sum(1 for v in diag if v == 0) == 16


def test_J_C_commute_32x32():
    """[J₃^{32}, C₁^{32}] = 0: S³ and S⁶ sectors decouple."""
    J3_32 = kron(J_S3[2], I8)
    C1_32 = kron(I4, su3_spin[0])
    comm = J3_32 * C1_32 - C1_32 * J3_32
    assert comm == zeros(32)


def test_K_C_commute_32x32():
    """[K₃^{32}, C₁^{32}] = 0: SU(2)_R and SU(3) also decouple."""
    K3_32 = kron(K_S3[2], I8)
    C1_32 = kron(I4, su3_spin[0])
    comm = K3_32 * C1_32 - C1_32 * K3_32
    assert comm == zeros(32)


def test_J_K_commute_32x32():
    """[J₃^{32}, K₃^{32}] = 0 (both in S³ sector, different blocks)."""
    J3_32 = kron(J_S3[2], I8)
    K3_32 = kron(K_S3[2], I8)
    assert J3_32 * K3_32 - K3_32 * J3_32 == zeros(32)


# ── J_spinor Clifford sanity ─────────────────────────────────────────────────


def test_J_spinor_anti_hermitian():
    """J_{ab}^spin is anti-Hermitian: (J_{ab})† = -J_{ab}."""
    for a in range(1, 7):
        for b in range(a + 1, 7):
            Jab = J_spinor(a, b)
            assert Jab.H == -Jab, f"J_spinor({a},{b}) not anti-Hermitian"


def test_J_spinor_so6_algebra():
    """[J_{12}, J_{23}] = J_{13}: so(6) algebra spot check."""
    J12 = J_spinor(1, 2)
    J23 = J_spinor(2, 3)
    J13 = J_spinor(1, 3)
    assert J12 * J23 - J23 * J12 - J13 == zeros(8)
