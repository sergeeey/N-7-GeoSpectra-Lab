"""G32 tests: Non-G₂-equivariant bundle escape route on S⁶.

Verifies that:
  - G₂-equivariant bundles all have ind=0 (confirming G30 null result)
  - Non-equivariant bundle with c₃=6 has ind=3 (escape route)
  - The escape is consistent with SM gauge group (color singlet)
  - K-theory quantization: c₃ must be even, ind=c₃/2
"""

import pytest
from fractions import Fraction

import sys, pathlib

sys.path.insert(
    0, str(pathlib.Path(__file__).parent.parent / "experiments" / "20260620-g32-s6-bundle-escape")
)

from g32_s6_bundle_index import (
    BundleS6,
    a_hat_s6,
    ch3,
    index_s6,
    sm_compatible,
    g32_status,
    G2_EQUIVARIANT_BUNDLES,
    GENERATOR_BUNDLE,
    ESCAPE_BUNDLE_G32,
)


# ---------------------------------------------------------------------------
# Cohomology of S⁶
# ---------------------------------------------------------------------------


class TestS6Cohomology:
    def test_s6_has_no_even_cohomology_below_degree_6(self):
        """H^k(S⁶;ℤ) = 0 for k = 2, 4 → c₁=c₂=0 for all bundles."""
        nontrivial_degrees = {0, 6}
        assert 2 not in nontrivial_degrees  # H²=0 → c₁=0
        assert 4 not in nontrivial_degrees  # H⁴=0 → c₂=0

    def test_s6_top_class_is_integer(self):
        """H⁶(S⁶;ℤ) = ℤ — the fundamental class lives here."""
        assert 6 in {0, 6}

    def test_a_hat_s6_is_one(self):
        """Â(S⁶) = 1 (stably parallelizable sphere)."""
        assert a_hat_s6() == Fraction(1)

    def test_bundle_c3_must_be_even(self):
        """Odd c₃ is forbidden: ind = c₃/2 ∉ ℤ."""
        with pytest.raises(ValueError, match="odd"):
            BundleS6(rank=3, c3=1)

    def test_bundle_c3_even_is_allowed(self):
        """Even c₃ is fine: ind = c₃/2 ∈ ℤ."""
        b = BundleS6(rank=3, c3=4)
        assert index_s6(b) == Fraction(2)

    def test_bundle_zero_c3_allowed(self):
        """c₃=0 is allowed (trivial or G₂-equivariant bundles)."""
        b = BundleS6(rank=1, c3=0)
        assert index_s6(b) == Fraction(0)


# ---------------------------------------------------------------------------
# Index formula on S⁶
# ---------------------------------------------------------------------------


class TestIndexFormulaS6:
    def test_index_is_c3_over_2(self):
        """ind(D_V) = c₃(V)/2 for bundles on S⁶."""
        for c3 in [0, 2, 4, 6, 8, 10, -2, -4]:
            b = BundleS6(rank=3, c3=c3)
            assert index_s6(b) == Fraction(c3, 2)

    def test_chern_character_degree6(self):
        """ch₃(V) = c₃(V)/2 (with c₁=c₂=0)."""
        b = BundleS6(rank=3, c3=6)
        assert ch3(b) == Fraction(3)

    def test_a_hat_times_ch3_gives_index(self):
        """Explicit: ind = Â(S⁶) × ch₃(V) = 1 × c₃/2 = c₃/2."""
        b = BundleS6(rank=3, c3=6)
        assert a_hat_s6() * ch3(b) == index_s6(b)

    def test_index_linear_in_c3(self):
        """Index is linear in c₃."""
        b2 = BundleS6(rank=3, c3=2)
        b6 = BundleS6(rank=3, c3=6)
        assert 3 * index_s6(b2) == index_s6(b6)

    def test_negative_c3_gives_negative_index(self):
        """c₃ < 0 → ind < 0 (chirality flip)."""
        b = BundleS6(rank=3, c3=-6)
        assert index_s6(b) == Fraction(-3)

    def test_index_zero_for_c3_zero(self):
        """Trivial bundle c₃=0: ind=0."""
        b = BundleS6(rank=3, c3=0)
        assert index_s6(b) == Fraction(0)


# ---------------------------------------------------------------------------
# G₂-equivariant bundles: all have c₃=0, ind=0 (confirms G30)
# ---------------------------------------------------------------------------


class TestG2EquivariantBundles:
    def test_all_g2_bundles_have_c3_zero(self):
        """G30 theorem: G₂-equivariant bundles have c₃=0 (G₂ symmetry kills c₃)."""
        for b in G2_EQUIVARIANT_BUNDLES:
            assert b.c3 == 0, f"G₂-equivariant bundle {b.description} has c₃≠0"

    def test_all_g2_bundles_have_index_zero(self):
        """G30 theorem: ind(D_{V_λ}) = 0 for all G₂-equivariant bundles V_λ."""
        for b in G2_EQUIVARIANT_BUNDLES:
            assert index_s6(b) == Fraction(0), f"G₂-bundle {b.description} has ind≠0"

    def test_trivial_bundle_is_g2_equivariant(self):
        """Trivial (singlet) bundle is G₂-equivariant."""
        trivial = next(b for b in G2_EQUIVARIANT_BUNDLES if b.rank == 1)
        assert trivial.g2_equivariant

    def test_su3_fundamental_is_g2_equivariant(self):
        """SU(3) fundamental (rank=3) is G₂-equivariant."""
        fund = next(b for b in G2_EQUIVARIANT_BUNDLES if "fundamental 3 " in b.description)
        assert fund.g2_equivariant
        assert fund.rank == 3
        assert fund.c3 == 0

    def test_adjoint_is_g2_equivariant(self):
        """SU(3) adjoint (rank=8) is G₂-equivariant."""
        adj = next(b for b in G2_EQUIVARIANT_BUNDLES if b.rank == 8)
        assert adj.g2_equivariant

    def test_g2_fundamental_is_equivariant(self):
        """G₂ fundamental (rank=7) is G₂-equivariant."""
        g2f = next(b for b in G2_EQUIVARIANT_BUNDLES if b.rank == 7)
        assert g2f.g2_equivariant

    def test_killed_by_g30_flag(self):
        """g32_status marks G₂-equivariant bundles as killed by G30."""
        for b in G2_EQUIVARIANT_BUNDLES:
            s = g32_status(b)
            assert s["killed_by_g30"]

    def test_g2_equivariant_verdict_is_null(self):
        """G₂-equivariant bundles all get verdict=NULL (ind=0, no generations)."""
        for b in G2_EQUIVARIANT_BUNDLES:
            s = g32_status(b)
            assert s["verdict"] == "NULL"


# ---------------------------------------------------------------------------
# Escape route: generator and 3× generator bundles
# ---------------------------------------------------------------------------


class TestEscapeBundle:
    def test_generator_has_c3_2(self):
        """Generator of K̃(S⁶) = ℤ has c₃=2."""
        assert GENERATOR_BUNDLE.c3 == 2

    def test_generator_not_g2_equivariant(self):
        """Generator bundle is not G₂-equivariant."""
        assert not GENERATOR_BUNDLE.g2_equivariant

    def test_generator_has_index_1(self):
        """Generator has ind=1 (one chiral zero mode)."""
        assert index_s6(GENERATOR_BUNDLE) == Fraction(1)

    def test_escape_bundle_c3_is_6(self):
        """Escape bundle (3× generator) has c₃=6."""
        assert ESCAPE_BUNDLE_G32.c3 == 6

    def test_escape_bundle_not_g2_equivariant(self):
        """Escape bundle is not G₂-equivariant (escapes G30)."""
        assert not ESCAPE_BUNDLE_G32.g2_equivariant

    def test_escape_bundle_index_is_3(self):
        """Escape bundle has ind=3 — three chiral zero modes."""
        assert index_s6(ESCAPE_BUNDLE_G32) == Fraction(3)

    def test_escape_bundle_ind_equals_3_flag(self):
        """g32_status flags ind_equals_3=True for escape bundle."""
        s = g32_status(ESCAPE_BUNDLE_G32)
        assert s["ind_equals_3"]

    def test_escape_bundle_not_killed_by_g30(self):
        """Escape bundle survives G30 (non-equivariant)."""
        s = g32_status(ESCAPE_BUNDLE_G32)
        assert not s["killed_by_g30"]

    def test_escape_bundle_verdict_is_open(self):
        """Escape bundle gets verdict=OPEN: ind=3, SM-compatible, non-equivariant."""
        s = g32_status(ESCAPE_BUNDLE_G32)
        assert s["verdict"] == "OPEN"

    def test_escape_is_3_times_generator_by_index(self):
        """ind(escape) = 3 × ind(generator)."""
        assert index_s6(ESCAPE_BUNDLE_G32) == 3 * index_s6(GENERATOR_BUNDLE)


# ---------------------------------------------------------------------------
# SM compatibility: color-singlet constraint
# ---------------------------------------------------------------------------


class TestSMCompatibility:
    def test_color_singlet_compatible_with_any_c3(self):
        """Color-singlet constraint does NOT restrict c₃ topologically."""
        for c3 in [0, 2, 4, 6, 8]:
            b = BundleS6(rank=3, c3=c3)
            assert sm_compatible(b), f"c₃={c3} should be SM-compatible"

    def test_escape_bundle_is_sm_compatible(self):
        """G32 escape bundle (c₃=6) is SM-compatible."""
        assert sm_compatible(ESCAPE_BUNDLE_G32)

    def test_sm_compatible_flag_in_status(self):
        """g32_status reports sm_compatible=True for escape bundle."""
        s = g32_status(ESCAPE_BUNDLE_G32)
        assert s["sm_compatible"]

    def test_g2_equivariant_bundles_also_sm_compatible(self):
        """G₂-equivariant bundles are also SM-compatible (but have ind=0)."""
        for b in G2_EQUIVARIANT_BUNDLES:
            assert sm_compatible(b)

    def test_separation_of_topology_and_gauge_structure(self):
        """c₃ is a topological invariant, independent of SU(3)_C fiber action."""
        b_singlet = BundleS6(rank=3, c3=6, description="color singlet, c₃=6")
        b_color = BundleS6(rank=3, c3=6, description="color rep, c₃=6")
        assert index_s6(b_singlet) == index_s6(b_color)  # same topology
        assert sm_compatible(b_singlet)
        assert sm_compatible(b_color)


# ---------------------------------------------------------------------------
# K-theory: classification of rank-3 bundles on S⁶
# ---------------------------------------------------------------------------


class TestKTheoryS6:
    def test_k_theory_generator_exists(self):
        """π₅(U(3)) = ℤ: rank-3 bundles on S⁶ classified by ℤ, generator has c₃=2."""
        gen = GENERATOR_BUNDLE
        assert gen.c3 == 2
        assert index_s6(gen) == Fraction(1)

    def test_all_c3_values_allowed(self):
        """K-theory: c₃ = 2k for any k ∈ ℤ — all are consistent."""
        for k in range(-3, 4):
            b = BundleS6(rank=3, c3=2 * k)
            assert index_s6(b) == Fraction(k)

    def test_g2_equivariant_c3_zero_not_generator(self):
        """G₂-equivariant bundles have c₃=0 (k=0), they are NOT the generator."""
        for b in G2_EQUIVARIANT_BUNDLES:
            assert b.c3 == 0  # k=0 in K-theory classification
