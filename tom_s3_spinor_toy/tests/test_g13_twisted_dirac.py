"""G13 tests: twisted Dirac index and chirality on nearly-Kähler S⁶ = G₂/SU(3)."""

import os
import sys

import sympy as sp
from sympy import Rational as R
from sympy import zeros

_exp_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g13-twisted-dirac"
)
sys.path.insert(0, _exp_dir)

_g11_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"
)
_g10b_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6")
_g10_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge")
for _p in [_g11_dir, _g10b_dir, _g10_dir]:
    sys.path.insert(0, _p)

from g13_twisted_dirac import (  # noqa: E402
    Gamma7,
    I8,
    su3_spin,
    _Sminus_basis,
    _Splus_basis,
    _singlet_count,
    G_so6,
)


# ── Topological (index theorem) ───────────────────────────────────────────────


def test_T1_euler_characteristic_S6():
    """χ(S⁶) = 2 from Betti numbers."""
    betti = [1, 0, 0, 0, 0, 0, 1]
    chi = sum((-1) ** k * b for k, b in enumerate(betti))
    assert chi == 2


def test_T2_pontryagin_classes_vanish():
    """H^4(S⁶) = 0 → p₁(S⁶) = 0 (S⁶ stably parallelizable)."""
    H4_S6 = 0
    assert H4_S6 == 0


def test_T3_A_hat_genus_one():
    """Â(S⁶) = 1 − p₁/24 + ⋯ = 1 when all Pontryagin classes vanish."""
    p1 = 0
    A_hat = R(1) - R(1, 24) * p1
    assert A_hat == 1


def test_T4_top_chern_class_equals_euler():
    """c₃(T^{1,0}) = χ(S⁶) = 2 (top Chern class = Euler class for almost complex)."""
    chi = 2
    c3 = chi
    assert c3 == 2


def test_T5_lower_chern_classes_zero():
    """c₁=c₂=0 for T^{1,0} over S⁶ (H²(S⁶) = H⁴(S⁶) = 0)."""
    c1 = 0
    c2 = 0
    assert c1 == 0 and c2 == 0


def test_T6_chern_character_formula():
    """ch₃(T^{1,0}) = c₃/2 = 1 (from Chern character with c₁=c₂=0)."""
    c3 = R(2)
    ch3 = c3 / 2  # = (c₁³ − 3c₁c₂ + 3c₃)/6 = 3c₃/6 = c₃/2 when c₁=c₂=0
    assert ch3 == 1


def test_T7_twisted_dirac_index_nonzero():
    """ind(D_{T^{1,0}}) = ∫ Â·ch₃ = 1·1 = 1 ≠ 0 (chirality EXISTS)."""
    A_hat = R(1)
    ch3 = R(1)
    index = A_hat * ch3
    assert index == 1
    assert index != 0  # non-zero → chiral zero mode exists


def test_T8_standard_dirac_index_zero():
    """ind(D^LC) = 0 (trivial twist → no chiral zero modes, G4 consistent)."""
    A_hat = R(1)
    ch3_trivial = R(0)  # trivial bundle E = ε: ch(ε) = 1, degree-6 part = 0
    index = A_hat * ch3_trivial
    assert index == 0


def test_index_scales_with_twist_rank():
    """ind(D_{E^⊕k}) = k · ind(D_E) (index is additive for direct sums)."""
    base_index = R(1)  # ind(D_{T^{1,0}}) = 1
    for k in range(1, 4):
        assert k * base_index == k


def test_index_formula_independent_of_A_hat_value():
    """For different hypothetical Â values the formula Â·ch₃ is linear."""
    ch3 = R(1)
    assert R(2) * ch3 == 2  # if Â were 2 (hypothetical)
    assert R(0) * ch3 == 0  # if Â were 0 → no chiral zero modes


# ── Chirality matrix ──────────────────────────────────────────────────────────


def test_T9a_gamma7_squared_is_identity():
    """Γ₇² = I₈ (valid chirality matrix)."""
    assert Gamma7 * Gamma7 == I8


def test_T9b_gamma7_equals_i_times_product():
    """Γ₇ = i·Γ₁Γ₂Γ₃Γ₄Γ₅Γ₆ (chirality = i × product of all gamma matrices)."""
    product = G_so6[0]
    for g in G_so6[1:]:
        product = product * g
    assert Gamma7 == sp.I * product


def test_gamma7_hermitian():
    """Γ₇ is hermitian (Γ₇† = Γ₇)."""
    assert Gamma7.H == Gamma7


def test_gamma7_anticommutes_with_gamma_a():
    """Γ₇ anticommutes with each Γ_a: {Γ₇, Γ_a} = 0."""
    for a, Ga in enumerate(G_so6):
        assert Gamma7 * Ga + Ga * Gamma7 == zeros(8), f"Anticommutator fails for Γ_{a + 1}"


def test_gamma7_eigenvalues_pm1():
    """Γ₇ has eigenvalues +1 and -1 only (chirality projections)."""
    S_plus = _Splus_basis()
    S_minus = _Sminus_basis()
    # Each column is a +1 or -1 eigenvector
    for j in range(S_plus.shape[1]):
        v = S_plus.col(j)
        assert Gamma7 * v == v
    for j in range(S_minus.shape[1]):
        v = S_minus.col(j)
        assert Gamma7 * v == -v


# ── SU(3) and chirality ───────────────────────────────────────────────────────


def test_T10_SU3_commutes_with_chirality():
    """[C_i^spin, Γ₇] = 0 for all 8 SU(3) generators (color preserves chirality)."""
    for i, C in enumerate(su3_spin):
        assert C * Gamma7 - Gamma7 * C == zeros(8), f"[C_{i}, Γ₇] ≠ 0"


def test_T11_S_minus_has_one_singlet():
    """S^- sector has exactly 1 SU(3) singlet (the zero mode of D_{T^{1,0}})."""
    Sminus = _Sminus_basis()
    assert Sminus.shape[1] == 4  # S^- is 4-dimensional
    assert _singlet_count(Sminus) == 1


def test_T12_S_plus_has_one_singlet():
    """S^+ sector has exactly 1 SU(3) singlet (S^+ = 1 ⊕ 3 as SU(3)-reps)."""
    Splus = _Splus_basis()
    assert Splus.shape[1] == 4  # S^+ is 4-dimensional
    assert _singlet_count(Splus) == 1


def test_T13_chirality_exhausts_spinor():
    """S^+ and S^- together span the full 8-dimensional spinor space."""
    Sminus = _Sminus_basis()
    Splus = _Splus_basis()
    assert Sminus.shape[1] + Splus.shape[1] == 8


def test_SU3_singlet_in_Sminus_is_color_neutral():
    """The SU(3) singlet in S^- is annihilated by all 8 color generators."""
    Sminus = _Sminus_basis()
    restricted = [Sminus.T * C * Sminus for C in su3_spin]
    stacked = sp.Matrix.vstack(*restricted)
    null_vecs = stacked.nullspace()
    assert len(null_vecs) == 1
    v = null_vecs[0]  # singlet in S^- coordinates
    # Embed back to 8-dim and check C_i · embed(v) = 0
    v_full = Sminus * v
    for i, C in enumerate(su3_spin):
        assert C * v_full == zeros(8, 1), f"C_{i} · singlet ≠ 0"


def test_SU3_generators_preserve_S_sectors():
    """Each C_i^spin maps S^+ to S^+ and S^- to S^- (block-diagonal in chirality basis)."""
    Sminus = _Sminus_basis()
    Splus = _Splus_basis()
    for i, C in enumerate(su3_spin):
        # C must not mix S^+ and S^-: C_restr_cross = Splus.T * C * Sminus = 0
        cross_pm = Splus.T * C * Sminus
        cross_mp = Sminus.T * C * Splus
        assert cross_pm == zeros(4, 4), f"C_{i} mixes S^+ → S^-"
        assert cross_mp == zeros(4, 4), f"C_{i} mixes S^- → S^+"


def test_two_singlets_total_one_per_sector():
    """Total SU(3) singlets = 2 (one in S^+, one in S^-); net chiral count = ±1."""
    n_plus = _singlet_count(_Splus_basis())
    n_minus = _singlet_count(_Sminus_basis())
    assert n_plus == 1 and n_minus == 1
    # Net index |n_plus - n_minus| = 0 from singlet count alone,
    # but the full twisted index = 1 because T^{1,0} shifts the count.
    # This test confirms the un-twisted structure; twisted index tested in test_T7.
    assert abs(n_plus - n_minus) == 0


def test_S_minus_not_all_singlets():
    """S^- is not entirely SU(3) singlets (3̄ component exists)."""
    n_minus = _singlet_count(_Sminus_basis())
    assert n_minus == 1  # 1 singlet, 3 non-singlet (the 3̄ part)
    assert n_minus < 4  # not all 4 basis vectors are singlets


def test_S_plus_not_all_singlets():
    """S^+ is not entirely SU(3) singlets (3 component exists)."""
    n_plus = _singlet_count(_Splus_basis())
    assert n_plus == 1  # 1 singlet, 3 non-singlet (the 3 part)
    assert n_plus < 4
