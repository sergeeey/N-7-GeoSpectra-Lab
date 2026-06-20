"""G33 tests: Chern-Gauss-Bonnet on S⁶ — A1 hypothesis verification.

Verifies:
  - χ(S⁶) = 2 (Betti numbers of S⁶)
  - c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (Chern-Gauss-Bonnet)
  - ind(D_{T^{1,0}S⁶}) = 1 (ONE generation from canonical bundle)
  - Frobenius consistency with G30: su3_index('3') = 1 ✓
  - All G₂-equivariant rank-3 bundles: c₃ ∈ {-2, 0, 2}
  - No G₂-equivariant rank-3 bundle has c₃=6
  - A1 hypothesis is NULL (circular — assumes N_gen as input)
  - G32 catalogue correction: fund. 3-rep has c₃=2, not 0
"""

import pytest
from fractions import Fraction

import sys
import pathlib

sys.path.insert(
    0,
    str(pathlib.Path(__file__).parent.parent / "experiments" / "20260620-g33-a1-euler-class"),
)

from g33_a1_euler_class import (
    chi_sphere,
    CHI_S6,
    c_top_t10_sphere,
    C3_T10_S6,
    index_from_c3,
    INDEX_T10_S6,
    frobenius_index,
    FROBENIUS_FUND,
    FROBENIUS_ANTIFUND,
    FROBENIUS_TRIVIAL,
    SU3_RANK3_REPS,
    MAX_C3_EQUIVARIANT_RANK3,
    a1_analysis,
    A1_THREE_GENERATIONS,
    G32_CATALOGUE_ERROR,
    GENERATION_ROUTES,
)


# ---------------------------------------------------------------------------
# Euler characteristic of spheres
# ---------------------------------------------------------------------------


class TestEulerCharacteristic:
    def test_chi_s6_is_2(self):
        """χ(S⁶) = 1 + (-1)⁶ = 2."""
        assert chi_sphere(6) == 2

    def test_chi_s3_is_0(self):
        """χ(S³) = 1 + (-1)³ = 0 (odd sphere)."""
        assert chi_sphere(3) == 0

    def test_chi_s2_is_2(self):
        """χ(S²) = 2 (S² = ℂP¹)."""
        assert chi_sphere(2) == 2

    def test_chi_s4_is_2(self):
        """χ(S⁴) = 2 (even sphere)."""
        assert chi_sphere(4) == 2

    def test_chi_s1_is_0(self):
        """χ(S¹) = 0."""
        assert chi_sphere(1) == 0

    def test_chi_s0_is_2(self):
        """χ(S⁰) = 2 (two points)."""
        assert chi_sphere(0) == 2

    def test_chi_s5_is_0(self):
        """χ(S⁵) = 0 (odd sphere)."""
        assert chi_sphere(5) == 0

    def test_chi_negative_n_raises(self):
        """Sphere undefined for n < 0."""
        with pytest.raises(ValueError, match="undefined"):
            chi_sphere(-1)

    def test_CHI_S6_constant(self):
        """Module constant CHI_S6 = 2."""
        assert CHI_S6 == 2

    def test_chi_formula(self):
        """χ(Sⁿ) = 1 + (-1)ⁿ for all n ≥ 0."""
        for n in range(10):
            assert chi_sphere(n) == 1 + (-1) ** n


# ---------------------------------------------------------------------------
# Chern-Gauss-Bonnet: c₃(T^{1,0}S⁶) = χ(S⁶) = 2
# ---------------------------------------------------------------------------


class TestChernGaussBonnet:
    def test_c3_t10_s6_is_2(self):
        """c₃(T^{1,0}S⁶) = χ(S⁶) = 2."""
        assert c_top_t10_sphere(6) == 2

    def test_c1_t10_s2_is_2(self):
        """c₁(T^{1,0}S²) = χ(S²) = 2 (S² = ℂP¹)."""
        assert c_top_t10_sphere(2) == 2

    def test_odd_sphere_raises(self):
        """No almost complex structure on S³, S⁵, ... → raises ValueError."""
        with pytest.raises(ValueError, match="almost complex"):
            c_top_t10_sphere(3)
        with pytest.raises(ValueError, match="almost complex"):
            c_top_t10_sphere(5)

    def test_c3_equals_chi_s6(self):
        """c₃(T^{1,0}S⁶) = χ(S⁶) — Chern-Gauss-Bonnet theorem."""
        assert C3_T10_S6 == CHI_S6

    def test_C3_T10_S6_constant(self):
        """Module constant C3_T10_S6 = 2."""
        assert C3_T10_S6 == 2

    def test_c_top_equals_chi_for_even_spheres(self):
        """c_n(T^{1,0}S^{2n}) = χ(S^{2n}) for all even spheres."""
        for n in [0, 2, 4, 6, 8]:
            assert c_top_t10_sphere(n) == chi_sphere(n)

    def test_c3_is_even(self):
        """c₃ must be even (ind = c₃/2 ∈ ℤ)."""
        assert C3_T10_S6 % 2 == 0


# ---------------------------------------------------------------------------
# Index of canonical bundle: ind(D_{T^{1,0}S⁶}) = 1
# ---------------------------------------------------------------------------


class TestIndexCanonicalBundle:
    def test_index_t10_s6_is_one(self):
        """ind(D_{T^{1,0}S⁶}) = c₃/2 = 2/2 = 1."""
        assert INDEX_T10_S6 == Fraction(1)

    def test_index_from_c3_basic(self):
        """index_from_c3(2) = 1."""
        assert index_from_c3(2) == Fraction(1)

    def test_index_from_c3_zero(self):
        """index_from_c3(0) = 0."""
        assert index_from_c3(0) == Fraction(0)

    def test_index_from_c3_six(self):
        """index_from_c3(6) = 3 (G32 escape cross-check)."""
        assert index_from_c3(6) == Fraction(3)

    def test_index_from_c3_negative(self):
        """index_from_c3(-2) = -1 (antifundamental 3̄)."""
        assert index_from_c3(-2) == Fraction(-1)

    def test_index_from_c3_odd_raises(self):
        """Odd c₃ raises ValueError (ind ∉ ℤ)."""
        with pytest.raises(ValueError, match="odd"):
            index_from_c3(1)
        with pytest.raises(ValueError, match="odd"):
            index_from_c3(3)

    def test_index_canonical_from_c3_constant(self):
        """INDEX_T10_S6 = index_from_c3(C3_T10_S6)."""
        assert INDEX_T10_S6 == index_from_c3(C3_T10_S6)

    def test_one_generation_from_canonical_bundle(self):
        """T^{1,0}S⁶ gives ONE generation (ind=1), not three."""
        assert int(INDEX_T10_S6) == 1
        assert int(INDEX_T10_S6) != 3


# ---------------------------------------------------------------------------
# Frobenius consistency with G30
# ---------------------------------------------------------------------------


class TestFrobeniusConsistency:
    def test_frobenius_fundamental_is_one(self):
        """su3_index('3') = mult(3 in S⁺) - mult(3 in S⁻) = 1 - 0 = 1."""
        assert FROBENIUS_FUND == 1

    def test_frobenius_antifundamental_is_minus_one(self):
        """su3_index('3bar') = 0 - 1 = -1."""
        assert FROBENIUS_ANTIFUND == -1

    def test_frobenius_trivial_is_zero(self):
        """su3_index('1') = 1 - 1 = 0 (trivial appears in both S⁺ and S⁻)."""
        assert FROBENIUS_TRIVIAL == 0

    def test_frobenius_consistent_with_chern_gauss_bonnet(self):
        """su3_index('3') = 1 = ind(D_{T^{1,0}S⁶}) = c₃/2 = 1 (consistent)."""
        assert FROBENIUS_FUND == int(INDEX_T10_S6)

    def test_fundamental_antifundamental_opposite(self):
        """3 and 3̄ give opposite indices (CPT conjugates)."""
        assert FROBENIUS_FUND + FROBENIUS_ANTIFUND == 0

    def test_frobenius_index_8_is_zero(self):
        """su3_index('8') = 0 (adjoint 8-dim doesn't appear in 4-dim spinors)."""
        assert frobenius_index("8") == 0

    def test_frobenius_index_6_is_zero(self):
        """su3_index('6') = 0 (sym² fundamental, too large for spinors)."""
        assert frobenius_index("6") == 0


# ---------------------------------------------------------------------------
# G₂-equivariant rank-3 bundles: c₃ ∈ {-2, 0, 2}
# ---------------------------------------------------------------------------


class TestG2EquivariantRank3:
    def test_exactly_three_rank3_su3_reps(self):
        """Exactly 3 SU(3)-reps of dim=3: {3, 3̄, 1⊕1⊕1}."""
        assert len(SU3_RANK3_REPS) == 3

    def test_all_reps_are_rank3(self):
        """All entries have dim=3."""
        assert all(r["dim"] == 3 for r in SU3_RANK3_REPS)

    def test_all_reps_are_g2_equivariant(self):
        """All SU(3)-isotropy-rep bundles are G₂-equivariant."""
        assert all(r["g2_equivariant"] for r in SU3_RANK3_REPS)

    def test_c3_values_are_subset_of_allowed(self):
        """c₃ ∈ {-2, 0, 2} for all G₂-equivariant rank-3 bundles."""
        allowed = {-2, 0, 2}
        for r in SU3_RANK3_REPS:
            assert r["c3"] in allowed, f"{r['name']} has c₃={r['c3']} ∉ {allowed}"

    def test_fundamental_has_c3_2(self):
        """Fundamental 3-rep: c₃=2 (Chern-Gauss-Bonnet + Frobenius)."""
        fund = next(r for r in SU3_RANK3_REPS if "fundamental 3" == r["name"])
        assert fund["c3"] == 2

    def test_antifundamental_has_c3_minus2(self):
        """Antifundamental 3̄-rep: c₃=-2 (conjugate of fundamental)."""
        antifund = next(r for r in SU3_RANK3_REPS if "antifundamental" in r["name"])
        assert antifund["c3"] == -2

    def test_trivial_has_c3_zero(self):
        """Trivial 1⊕1⊕1: c₃=0."""
        trivial = next(r for r in SU3_RANK3_REPS if "trivial" in r["name"])
        assert trivial["c3"] == 0

    def test_no_equivariant_rank3_bundle_with_c3_6(self):
        """No G₂-equivariant rank-3 bundle has c₃=6 → c₃=6 is non-equivariant."""
        assert all(r["c3"] != 6 for r in SU3_RANK3_REPS)

    def test_max_c3_equivariant_rank3_is_2(self):
        """Maximum c₃ for G₂-equivariant rank-3 bundles is 2 (one generation unit)."""
        assert MAX_C3_EQUIVARIANT_RANK3 == 2

    def test_max_c3_less_than_6(self):
        """max c₃ = 2 < 6: equivariant rank-3 bundles cannot reach ind=3."""
        assert MAX_C3_EQUIVARIANT_RANK3 < 6


# ---------------------------------------------------------------------------
# A1 hypothesis analysis
# ---------------------------------------------------------------------------


class TestA1Analysis:
    def test_a1_c3_canonical_unit_is_2(self):
        """A1 analysis: the canonical unit is c₃(T^{1,0}S⁶) = 2."""
        d = A1_THREE_GENERATIONS
        assert d["c3_canonical_unit"] == 2

    def test_a1_c3_needed_for_3gen_is_6(self):
        """A1 analysis: c₃=6 is needed for N_gen=3."""
        d = A1_THREE_GENERATIONS
        assert d["c3_needed"] == 6

    def test_a1_ratio_equals_n_gen(self):
        """The ratio c₃_needed / c₃_unit always equals N_gen (circular)."""
        for n_gen in [1, 2, 3, 4]:
            d = a1_analysis(n_gen)
            assert d["ratio_to_unit"] == n_gen

    def test_a1_is_circular(self):
        """A1 is circular: the ratio always equals N_gen (not derived)."""
        d = A1_THREE_GENERATIONS
        assert d["is_circular"] is True

    def test_a1_does_not_derive_n_gen(self):
        """A1 does not derive N_gen=3 from geometry."""
        d = A1_THREE_GENERATIONS
        assert d["derives_n_gen_geometrically"] is False

    def test_a1_verdict_is_null(self):
        """A1 verdict: NULL (c₃(T^{1,0}S⁶)=2, not 6)."""
        d = A1_THREE_GENERATIONS
        assert d["verdict"] == "NULL"

    def test_a1_not_confirmed(self):
        """A1 is not confirmed: c₃(T^{1,0}S⁶)=2≠6."""
        d = A1_THREE_GENERATIONS
        assert d["a1_confirmed"] is False

    def test_a1_gives_correct_c3_for_1gen(self):
        """A1 analysis for N_gen=1: c₃=2 (consistent with T^{1,0}S⁶)."""
        d = a1_analysis(1)
        assert d["c3_needed"] == 2

    def test_a1_gives_correct_c3_for_2gen(self):
        """A1 analysis for N_gen=2: c₃=4."""
        d = a1_analysis(2)
        assert d["c3_needed"] == 4


# ---------------------------------------------------------------------------
# G32 catalogue correction
# ---------------------------------------------------------------------------


class TestG32CatalogueCorrection:
    def test_g32_had_wrong_c3_for_fundamental(self):
        """G32 erroneously assigned c₃=0 to fundamental 3-rep."""
        assert G32_CATALOGUE_ERROR["c3_in_g32"] == 0

    def test_correct_c3_for_fundamental_is_2(self):
        """Correct value: c₃(fundamental 3-rep) = 2."""
        assert G32_CATALOGUE_ERROR["c3_correct"] == 2

    def test_g30_does_not_kill_fundamental_3_rep(self):
        """G30 kills G₂-IRREP bundles (7,14,27,...), NOT SU(3)-isotropy reps."""
        assert G32_CATALOGUE_ERROR["g30_kills_this"] is False

    def test_g32_main_conclusion_preserved(self):
        """G32's main conclusion (c₃=6 is non-equivariant) is preserved."""
        assert G32_CATALOGUE_ERROR["g32_main_conclusion_preserved"] is True

    def test_fundamental_ind_is_one(self):
        """Corrected: fundamental 3-rep gives ind=1 (one generation)."""
        assert G32_CATALOGUE_ERROR["ind_correct"] == 1


# ---------------------------------------------------------------------------
# Complete generation route map
# ---------------------------------------------------------------------------


class TestGenerationRoutes:
    def test_three_routes_defined(self):
        """Three generation routes: N_gen = 0, 1, 3."""
        n_gens = [r["n_gen"] for r in GENERATION_ROUTES]
        assert 0 in n_gens
        assert 1 in n_gens
        assert 3 in n_gens

    def test_zero_gen_is_null(self):
        """G₂-IRREP bundles give 0 generations (G30 killed)."""
        zero = next(r for r in GENERATION_ROUTES if r["n_gen"] == 0)
        assert "NULL" in zero["status"]

    def test_one_gen_route_is_equivariant(self):
        """T^{1,0}S⁶ route (N_gen=1) is G₂-equivariant."""
        one = next(r for r in GENERATION_ROUTES if r["n_gen"] == 1)
        assert one["equivariant"] is True
        assert one["c3"] == 2

    def test_three_gen_route_is_non_equivariant(self):
        """G32 escape (N_gen=3) is non-equivariant."""
        three = next(r for r in GENERATION_ROUTES if r["n_gen"] == 3)
        assert three["equivariant"] is False
        assert three["c3"] == 6

    def test_c3_equals_2_times_n_gen(self):
        """For all routes: c₃ = 2 × N_gen."""
        for r in GENERATION_ROUTES:
            assert r["c3"] == 2 * r["n_gen"]
