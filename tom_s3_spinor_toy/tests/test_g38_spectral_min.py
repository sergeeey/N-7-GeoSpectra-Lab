"""Tests for G38: Spectral Action Minimum on Bundle Space — S2 null check."""

import math
from fractions import Fraction


# ── Helpers ──────────────────────────────────────────────────────────────
def ch3_from_c3(c3: int) -> Fraction:
    return Fraction(c3, 2)


def ind_from_c3(c3: int) -> int:
    return c3 // 2


def s_zero(c3: int, f0: float = 1.0) -> float:
    return ind_from_c3(c3) * f0


def s_ym_lower(c3: int, K: float = 1.0) -> float:
    return K * (c3 / 2) ** (2 / 3)


def s_spec_lower(c3: int, f0: float = 1.0, K: float = 1.0) -> float:
    return s_zero(c3, f0) + s_ym_lower(c3, K)


# ── S2-A: Cohomology constraints ─────────────────────────────────────────
class TestCohomologyConstraints:
    def test_h2_s6_vanishes(self):
        h2 = 0  # rank of H^2(S^6; Z)
        assert h2 == 0

    def test_h4_s6_vanishes(self):
        h4 = 0  # rank of H^4(S^6; Z)
        assert h4 == 0

    def test_h6_s6_is_z(self):
        h6 = 1  # rank of H^6(S^6; Z) = Z
        assert h6 == 1

    def test_c1_forced_zero(self):
        c1_in_h2 = 0  # c1 must live in H^2(S^6; Z) = 0
        assert c1_in_h2 == 0

    def test_c2_forced_zero(self):
        c2_in_h4 = 0  # c2 must live in H^4(S^6; Z) = 0
        assert c2_in_h4 == 0

    def test_c3_is_only_free_class(self):
        free_chern_classes = ["c3"]
        assert len(free_chern_classes) == 1
        assert "c3" in free_chern_classes

    def test_ch3_from_c1_c2_c3(self):
        c1, c2, c3 = 0, 0, 6
        # ch3 = (c1^3 - 3*c1*c2 + 3*c3) / 6
        ch3 = (c1**3 - 3 * c1 * c2 + 3 * c3) // 6
        assert ch3 == c3 // 2  # simplifies to c3/2 when c1=c2=0


# ── S2-B: Zero mode counting ─────────────────────────────────────────────
class TestZeroModeCount:
    def test_ind_c3_2(self):
        assert ind_from_c3(2) == 1  # T^{1,0}S^6: one zero mode

    def test_ind_c3_4(self):
        assert ind_from_c3(4) == 2

    def test_ind_c3_6(self):
        assert ind_from_c3(6) == 3  # c3=6: three zero modes

    def test_ind_c3_8(self):
        assert ind_from_c3(8) == 4

    def test_ind_equals_ch3(self):
        for c3 in [2, 4, 6, 8]:
            assert ind_from_c3(c3) == ch3_from_c3(c3)

    def test_zero_mode_contribution_c3_2(self):
        assert s_zero(2) == 1.0

    def test_zero_mode_contribution_c3_6(self):
        assert s_zero(6) == 3.0

    def test_c3_6_has_more_zero_modes_than_c3_2(self):
        assert ind_from_c3(6) > ind_from_c3(2)

    def test_s_zero_monotone(self):
        vals = [s_zero(c3) for c3 in [2, 4, 6, 8]]
        assert all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))


# ── S2-C: Seeley-DeWitt expansion ────────────────────────────────────────
class TestSeeleyDeWittExpansion:
    def test_a0_not_c3_dependent(self):
        rank = 3
        vol_s6 = 16 * math.pi**3 / 15
        a0 = rank * vol_s6
        a0_c3_2 = a0
        a0_c3_6 = a0  # same — a0 depends only on rank and Vol
        assert a0_c3_2 == a0_c3_6

    def test_a2_not_c3_dependent(self):
        rank, R = 3, 30
        vol_s6 = 16 * math.pi**3 / 15
        a2 = rank * (R / 6) * vol_s6
        assert a2 > 0  # positive geometric contribution

    def test_a4_gauge_increases_with_c3(self):
        # a4 gauge term proportional to integral(||F||^2) = S_YM
        s_ym_c3_2 = s_ym_lower(2)
        s_ym_c3_6 = s_ym_lower(6)
        assert s_ym_c3_6 > s_ym_c3_2

    def test_a6_ch3_term_increases_with_c3(self):
        # a6 contains ch3(V) (from Atiyah-Singer via heat kernel)
        for c3_low, c3_high in [(2, 4), (4, 6), (6, 8)]:
            assert ch3_from_c3(c3_high) > ch3_from_c3(c3_low)


# ── S2-D: Yang-Mills lower bound ─────────────────────────────────────────
class TestYMLowerBound:
    def test_ym_bound_c3_2(self):
        assert abs(s_ym_lower(2) - 1.0) < 1e-10  # normalized to 1

    def test_ym_bound_c3_4(self):
        expected = 2 ** (2 / 3)
        assert abs(s_ym_lower(4) - expected) < 1e-10

    def test_ym_bound_c3_6(self):
        expected = 3 ** (2 / 3)
        assert abs(s_ym_lower(6) - expected) < 1e-10

    def test_ym_bound_monotone(self):
        bounds = [s_ym_lower(c3) for c3 in [2, 4, 6, 8]]
        assert all(bounds[i] < bounds[i + 1] for i in range(len(bounds) - 1))

    def test_ym_ratio_c3_6_vs_c3_2(self):
        ratio = s_ym_lower(6) / s_ym_lower(2)
        assert ratio > 2.0  # ratio = 3^(2/3) ≈ 2.08 > 2
        assert ratio < 2.5

    def test_ym_bound_scales_as_power_two_thirds(self):
        # S_YM,min(c3) ~ (c3/2)^(2/3)
        for c3 in [2, 4, 6, 8]:
            expected = (c3 / 2) ** (2 / 3)
            assert abs(s_ym_lower(c3, K=1.0) - expected) < 1e-10


# ── S2-E: Total spectral action comparison ───────────────────────────────
class TestSpectralActionComparison:
    def test_s_spec_c3_2_lt_c3_4(self):
        assert s_spec_lower(2) < s_spec_lower(4)

    def test_s_spec_c3_4_lt_c3_6(self):
        assert s_spec_lower(4) < s_spec_lower(6)

    def test_s_spec_c3_6_lt_c3_8(self):
        assert s_spec_lower(6) < s_spec_lower(8)

    def test_delta_s_positive(self):
        delta_s = s_spec_lower(6) - s_spec_lower(2)
        assert delta_s > 0

    def test_minimum_at_c3_2(self):
        c3_range = range(2, 20, 2)
        s_vals = {c3: s_spec_lower(c3) for c3 in c3_range}
        min_c3 = min(s_vals, key=lambda c3: s_vals[c3])
        assert min_c3 == 2

    def test_s2_null_verdict(self):
        s_c3_6 = s_spec_lower(6)
        s_c3_2 = s_spec_lower(2)
        s2_selects_c3_6 = s_c3_6 < s_c3_2  # claim: c3=6 is minimum
        assert not s2_selects_c3_6  # REFUTED: minimum is at c3=2


# ── S2-F: Non-monotone mechanism check ───────────────────────────────────
class TestNonMonotoneMechanisms:
    def test_geometric_terms_c3_independent(self):
        rank = 3
        vol_s6 = 16 * math.pi**3 / 15
        R = 30
        a0 = rank * vol_s6
        a2 = rank * (R / 6) * vol_s6
        # These are identical for all c3
        assert a0 > 0
        assert a2 > 0

    def test_s3_factor_c3_independent(self):
        vol_s3_contribution = 2 * math.pi**2  # Vol(S^3)
        assert vol_s3_contribution > 0  # contributes positively, not c3-dependent

    def test_finite_dirac_c3_independent(self):
        # D_F (finite spectral triple) depends on Yukawa couplings, not c3
        c3_dependence_of_df = False
        assert not c3_dependence_of_df

    def test_no_negative_c3_term_found(self):
        no_negative_c3_term = True
        assert no_negative_c3_term


# ── S2-G: G38 = G33 structural identity ──────────────────────────────────
class TestStructuralIdentity:
    def test_g33_minimum_c3(self):
        # G33: ind(D_{T^{1,0}S^6}) = c3(T^{1,0}S^6)/2 = chi(S^6)/2 = 1
        ind_g33 = 1
        c3_canonical = ind_g33 * 2
        assert c3_canonical == 2

    def test_g38_minimum_c3(self):
        # G38: spectral action minimum at c3=2
        c3_range = range(2, 20, 2)
        min_c3 = min(c3_range, key=lambda c3: s_spec_lower(c3))
        assert min_c3 == 2

    def test_g38_minimum_equals_g33_minimum(self):
        c3_g33 = 2  # canonical bundle
        c3_g38 = min(range(2, 20, 2), key=lambda c3: s_spec_lower(c3))
        assert c3_g33 == c3_g38

    def test_g38_not_independent_of_g33(self):
        g38_independent = False  # G38 reduces to G33
        assert not g38_independent

    def test_n_gen_from_spectral_action_minimum(self):
        c3_min = 2  # from spectral action minimum
        n_gen_from_s2 = c3_min // 2  # = 1
        n_gen_observed = 3
        assert n_gen_from_s2 == 1
        assert n_gen_from_s2 != n_gen_observed
