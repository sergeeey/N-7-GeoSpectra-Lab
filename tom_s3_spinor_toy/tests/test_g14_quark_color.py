"""G14 tests: quark color triplet and SU(3) fundamental from S⁶ spinor geometry."""

import os
import sys

import sympy as sp
from sympy import zeros

_exp_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g14-quark-color")
sys.path.insert(0, _exp_dir)

_g11_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"
)
_g10b_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6")
_g10_dir = os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge")
for _p in [_g11_dir, _g10b_dir, _g10_dir]:
    sys.path.insert(0, _p)

from g14_quark_color import (  # noqa: E402
    AQUARK,
    QUARK,
    SM_SINGLET,
    SP_SINGLET,
    Gamma7,
    _cartan_weights,
    _commutant_dim,
    _sel,
    su3_spin,
)


# ── Sector structure ──────────────────────────────────────────────────────────


def test_SP_singlet_is_000():
    """Singlet in S^+ is |000⟩ = index 0 (all σ₃ eigenvalue +1)."""
    assert SP_SINGLET == 0
    assert bin(0).count("1") == 0


def test_SM_singlet_is_111():
    """Singlet in S^- is |111⟩ = index 7 (all σ₃ eigenvalue −1) = G13 zero mode."""
    assert SM_SINGLET == 7
    assert bin(7).count("1") == 3


def test_quark_indices_have_two_ones():
    """Quark states |011⟩,|101⟩,|110⟩ each have exactly two 1-bits (two ↓ spins)."""
    for j in QUARK:
        assert bin(j).count("1") == 2, f"index {j} has {bin(j).count('1')} ones, expected 2"


def test_antiquark_indices_have_one_one():
    """Antiquark states |001⟩,|010⟩,|100⟩ each have exactly one 1-bit (one ↓ spin)."""
    for j in AQUARK:
        assert bin(j).count("1") == 1, f"index {j} has {bin(j).count('1')} ones, expected 1"


def test_three_quark_colors():
    """Exactly 3 two-1-bit numbers in {0..7} = three quark color choices."""
    two_ones = [n for n in range(8) if bin(n).count("1") == 2]
    assert sorted(two_ones) == sorted(list(QUARK))


def test_three_antiquark_colors():
    """Exactly 3 one-1-bit numbers in {0..7} = three antiquark color choices."""
    one_ones = [n for n in range(8) if bin(n).count("1") == 1]
    assert sorted(one_ones) == sorted(list(AQUARK))


def test_full_decomposition_covers_all_8():
    """1 + 3 + 3 + 1 = 8 and all 8 spinor basis indices are covered."""
    all_idx = {SP_SINGLET} | set(QUARK) | set(AQUARK) | {SM_SINGLET}
    assert len(all_idx) == 8
    assert all_idx == set(range(8))


def test_combinatorial_quark_singlet_relation():
    """Quarks + singlets together form: {n : n even} = S^+ = {0,3,5,6}."""
    even_bits = [n for n in range(8) if bin(n).count("1") % 2 == 0]
    assert sorted(even_bits) == sorted([SP_SINGLET] + list(QUARK))


# ── Chirality checks ──────────────────────────────────────────────────────────


def test_quark_indices_in_Splus():
    """All quark basis vectors have Γ₇ eigenvalue +1 (in S^+ sector)."""
    for j in QUARK:
        e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
        assert Gamma7 * e_j == e_j, f"|{j}⟩ not in S^+ (Γ₇ eigenvalue ≠ +1)"


def test_antiquark_indices_in_Sminus():
    """All antiquark basis vectors have Γ₇ eigenvalue −1 (in S^- sector)."""
    for j in AQUARK:
        e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
        assert Gamma7 * e_j == -e_j, f"|{j}⟩ not in S^- (Γ₇ eigenvalue ≠ −1)"


def test_sm_singlet_in_Sminus():
    """G13 zero mode |111⟩ is in S^- (Γ₇ eigenvalue −1)."""
    e7 = sp.Matrix([1 if k == 7 else 0 for k in range(8)])
    assert Gamma7 * e7 == -e7


def test_sp_singlet_in_Splus():
    """|000⟩ is in S^+ (Γ₇ eigenvalue +1)."""
    e0 = sp.Matrix([1 if k == 0 else 0 for k in range(8)])
    assert Gamma7 * e0 == e0


# ── Invariance and irreducibility ─────────────────────────────────────────────


def test_quark_subspace_SU3_invariant():
    """C_i^spin maps each quark basis vector to S^+ (no leakage to S^-)."""
    SM_IDX = [1, 2, 4, 7]
    for C in su3_spin:
        for j in QUARK:
            e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
            Ce_j = C * e_j
            for k in SM_IDX:
                assert Ce_j[k] == 0, f"C * |{j}⟩ leaks to S^- index {k}"


def test_antiquark_subspace_SU3_invariant():
    """C_i^spin maps each antiquark basis vector to S^- (no leakage to S^+)."""
    SP_IDX = [0, 3, 5, 6]
    for C in su3_spin:
        for j in AQUARK:
            e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
            Ce_j = C * e_j
            for k in SP_IDX:
                assert Ce_j[k] == 0, f"C * |{j}⟩ leaks to S^+ index {k}"


def test_quark_subspace_irreducible_Schur():
    """Quark subspace is SU(3)-irreducible: commutant has dimension 1 (Schur's lemma)."""
    B_q = _sel(QUARK)
    C_q = [B_q.T * C * B_q for C in su3_spin]
    assert _commutant_dim(C_q) == 1


def test_antiquark_subspace_irreducible_Schur():
    """Antiquark subspace is SU(3)-irreducible: commutant has dimension 1."""
    B_a = _sel(AQUARK)
    C_a = [B_a.T * C * B_a for C in su3_spin]
    assert _commutant_dim(C_a) == 1


# ── Cartan weights and 3 vs 3̄ ─────────────────────────────────────────────────


def test_quark_has_three_distinct_weights():
    """Three quark color states have three distinct Cartan weight vectors."""
    B_q = _sel(QUARK)
    C_q = [B_q.T * C * B_q for C in su3_spin]
    w = _cartan_weights(C_q)
    assert len(set(w)) == 3


def test_antiquark_has_three_distinct_weights():
    """Three antiquark states have three distinct Cartan weight vectors."""
    B_a = _sel(AQUARK)
    C_a = [B_a.T * C * B_a for C in su3_spin]
    w = _cartan_weights(C_a)
    assert len(set(w)) == 3


def test_quark_cartan_weights_sum_zero():
    """Sum of quark Cartan weights = 0 (traceless generators of SU(3))."""
    B_q = _sel(QUARK)
    C_q = [B_q.T * C * B_q for C in su3_spin]
    w = _cartan_weights(C_q)
    assert sum(wi for wi, _ in w) == 0
    assert sum(wj for _, wj in w) == 0


def test_antiquark_cartan_weights_sum_zero():
    """Sum of antiquark Cartan weights = 0."""
    B_a = _sel(AQUARK)
    C_a = [B_a.T * C * B_a for C in su3_spin]
    w = _cartan_weights(C_a)
    assert sum(wi for wi, _ in w) == 0
    assert sum(wj for _, wj in w) == 0


def test_3_and_3bar_are_conjugate_representations():
    """Antiquark weights = negatives of quark weights: 3 and 3̄ are dual reps."""
    B_q = _sel(QUARK)
    B_a = _sel(AQUARK)
    C_q = [B_q.T * C * B_q for C in su3_spin]
    C_a = [B_a.T * C * B_a for C in su3_spin]
    q_w = set(_cartan_weights(C_q))
    a_w = set(_cartan_weights(C_a))
    a_neg = {(-w1, -w2) for w1, w2 in a_w}
    assert q_w == a_neg, f"3 and 3̄ weight mismatch: quark={q_w}, neg(antiquark)={a_neg}"


def test_quark_generators_anti_hermitian():
    """Quark generators are anti-Hermitian (C + C† = 0): unitary representation."""
    B_q = _sel(QUARK)
    for C in [B_q.T * gen * B_q for gen in su3_spin]:
        assert C + C.H == zeros(3, 3)


def test_antiquark_generators_anti_hermitian():
    """Antiquark generators are anti-Hermitian."""
    B_a = _sel(AQUARK)
    for C in [B_a.T * gen * B_a for gen in su3_spin]:
        assert C + C.H == zeros(3, 3)


# ── Integration: G14 connects to G13 ─────────────────────────────────────────


def test_G13_singlet_not_in_quark_subspace():
    """G13 zero mode |111⟩ is NOT in the quark subspace (different SU(3) charge)."""
    assert SM_SINGLET not in QUARK
    e7 = sp.Matrix([1 if k == 7 else 0 for k in range(8)])
    # e7 should NOT be in span of quark basis vectors {e3, e5, e6}
    B_q = _sel(QUARK)
    # Project e7 onto quark subspace
    proj = B_q * B_q.T * e7
    assert proj == sp.zeros(8, 1), "G13 singlet has nonzero projection onto quark subspace"


def test_quark_singlet_separates_from_lepton_singlet():
    """The two singlets (|000⟩ and |111⟩) are in OPPOSITE chirality sectors."""
    e0 = sp.Matrix([1 if k == 0 else 0 for k in range(8)])
    e7 = sp.Matrix([1 if k == 7 else 0 for k in range(8)])
    # |000⟩ in S^+, |111⟩ in S^-
    assert Gamma7 * e0 == e0
    assert Gamma7 * e7 == -e7


def test_SU3_color_charges_quark_vs_lepton():
    """Quarks carry nonzero color charge; the |000⟩ singlet does not."""
    e0 = sp.Matrix([1 if k == 0 else 0 for k in range(8)])
    for C in su3_spin:
        # e0 = S^+ singlet: all color generators annihilate it
        assert C * e0 == sp.zeros(8, 1), "|000⟩ should be color-neutral"
        # Quark states carry color (at least one C_i is nonzero on them)
    quark_charged = False
    for j in QUARK:
        e_j = sp.Matrix([1 if k == j else 0 for k in range(8)])
        for C in su3_spin:
            if C * e_j != sp.zeros(8, 1):
                quark_charged = True
                break
    assert quark_charged, "No quark state carries color charge"
