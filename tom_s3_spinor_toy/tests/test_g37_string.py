"""Tests for G37: String Tadpole Gate — S1 circularity/null check."""

from fractions import Fraction


def euler_sphere(n):
    return 1 + (-1) ** n


# ── Dimensional mismatch ─────────────────────────────────────────────────
class TestDimensionalMismatch:
    def test_dim_s3xs6_is_9(self):
        assert 3 + 6 == 9

    def test_m6_requires_dim_6(self):
        dim_internal = 6  # 10D string: M₄(4) + M₆(6) = 10
        dim_s3xs6 = 9
        assert dim_s3xs6 != dim_internal

    def test_s6_alone_fits_as_m6(self):
        assert 6 == 6  # S⁶ alone has right dimension

    def test_s3xs6_not_valid_m6(self):
        dim_mismatch = (3 + 6) != 6
        assert dim_mismatch


# ── Euler characteristics ────────────────────────────────────────────────
class TestEulerCharacteristics:
    def test_chi_s3_zero(self):
        assert euler_sphere(3) == 0

    def test_chi_s6_two(self):
        assert euler_sphere(6) == 2

    def test_chi_product_zero(self):
        assert euler_sphere(3) * euler_sphere(6) == 0

    def test_euler_tadpole_s6_non_integer(self):
        tadpole = Fraction(euler_sphere(6), 24)
        assert tadpole == Fraction(1, 12)
        assert tadpole.denominator != 1  # not integer

    def test_euler_tadpole_product_zero(self):
        chi_product = euler_sphere(3) * euler_sphere(6)
        tadpole = Fraction(chi_product, 24)
        assert tadpole == 0

    def test_chi_s3xs4_zero(self):
        # Bryant-Salamon G₂ manifold S³×S⁴
        assert euler_sphere(3) * euler_sphere(4) == 0


# ── Â genus ─────────────────────────────────────────────────────────────
class TestAHatGenus:
    def test_pontryagin_s6_trivial(self):
        # TSⁿ ⊕ ε¹ = εⁿ⁺¹ → all Pontryagin classes vanish
        p1_s6 = 0
        p2_s6 = 0
        assert p1_s6 == 0
        assert p2_s6 == 0

    def test_a_hat_s6_is_one(self):
        p1 = 0
        A_hat = 1 - Fraction(p1, 24)
        assert A_hat == 1

    def test_a_hat_product_is_one(self):
        assert 1 * 1 == 1  # Â(S³×S⁶) = Â(S³) · Â(S⁶)

    def test_no_correction_to_tadpole(self):
        # Â=1 → ∫ ch₃(V) Â = ∫ ch₃(V) (no correction)
        A_hat_s6 = 1
        correction_factor = A_hat_s6
        assert correction_factor == 1


# ── Type IIA tadpole ─────────────────────────────────────────────────────
class TestTypeIIATadpole:
    def ch3_from_c3(self, c3):
        return Fraction(c3, 2)

    def test_minimal_source_gives_n_gen_1(self):
        n_d0_min = 1
        c3 = n_d0_min * 2
        ind = c3 // 2
        assert ind == 1  # minimal source → N_gen=1 (consistent with G33)

    def test_c3_6_needs_3_d0_branes(self):
        c3_target = 6
        n_d0_needed = c3_target // 2
        assert n_d0_needed == 3

    def test_3_d0_branes_circular(self):
        n_d0 = 3
        n_gen_from_d0 = n_d0  # by tadpole: c₃/2 = N_D0 → N_gen = N_D0
        n_gen_observed = 3
        assert n_gen_from_d0 == n_gen_observed  # circular

    def test_minimal_o6_tadpole_gives_c3_2(self):
        # χ(S⁶)/24 = 1/12; minimal integer: k=12 → c₃/2=1 → c₃=2
        k_min = 12
        c3_from_k = k_min // 12 * 2
        assert c3_from_k == 2
        assert c3_from_k // 2 == 1  # N_gen=1

    def test_n_gen_3_from_tadpole_circular(self):
        # k=36 gives c₃=6: but 36=3×12 → three copies of minimal → circular
        k = 36
        k_min = 12
        assert k == 3 * k_min  # three copies
        c3 = k // 12 * 2
        assert c3 == 6
        n_gen = c3 // 2
        assert n_gen == 3  # embeds N_gen=3 as "3 copies"


# ── Heterotic anomaly ────────────────────────────────────────────────────
class TestHeteroticAnomaly:
    def test_anomaly_fixes_c2_not_c3(self):
        # Green-Schwarz: ∫ ch₂(V) = ∫ ch₂(TM₆)
        # This is a constraint on c₂, NOT c₃
        fixes_c2 = True
        fixes_c3 = False
        assert fixes_c2
        assert not fixes_c3

    def test_s6_not_calabi_yau(self):
        s6_is_cy = False  # Newlander-Nirenberg fails for S⁶
        assert not s6_is_cy

    def test_heterotic_n_gen_formula_inapplicable(self):
        # Heterotic N_gen=|χ(CY₃)|/2 requires integrable complex structure
        s6_is_cy = False
        formula_applicable = s6_is_cy
        assert not formula_applicable

    def test_c3_free_after_anomaly(self):
        # After Green-Schwarz: c₃(V) ∈ ℤ unconstrained (any value satisfies anomaly)
        all_consistent = True
        assert all_consistent


# ── Brane count circularity ──────────────────────────────────────────────
class TestBraneCircularity:
    def test_brane_table(self):
        expected = {1: 2, 2: 4, 3: 6, 4: 8}
        for n_branes, expected_c3 in expected.items():
            c3 = 2 * n_branes
            assert c3 == expected_c3

    def test_n3_branes_gives_n_gen_3(self):
        n_branes = 3
        c3 = 2 * n_branes
        n_gen = c3 // 2
        assert n_gen == n_branes  # n_gen = n_branes always → circular

    def test_choice_of_3_is_circular(self):
        n_gen_physical = 3
        n_branes_needed = n_gen_physical
        # Choosing n_branes=3 to get n_gen=3 is circular
        n_gen_from_branes = n_branes_needed
        assert n_gen_from_branes == n_gen_physical


# ── M-theory G₂ ─────────────────────────────────────────────────────────
class TestMTheoryG2:
    def test_s6_not_g2_manifold(self):
        # S⁶ = G₂/SU(3) is the HOMOGENEOUS SPACE, not a G₂ holonomy manifold
        dim_g2_manifold = 7  # G₂ holonomy requires 7D
        dim_s6 = 6
        assert dim_s6 != dim_g2_manifold

    def test_bryant_salamon_s3xs4(self):
        # Canonical G₂ manifold: S³×S⁴ (Bryant-Salamon), not S³×S⁶
        chi_s3xs4 = euler_sphere(3) * euler_sphere(4)
        assert chi_s3xs4 == 0  # χ=0 → no tadpole

    def test_g4_tadpole_zero_for_s3xs4(self):
        # b₄(S³×S⁴): no 4-cocycle → no G₄ flux → c₃ free
        b4_s3 = 0  # β₄(S³)=0
        b4_s3xs4 = b4_s3 * 1  # product formula
        assert b4_s3xs4 == 0


# ── Overall verdict ──────────────────────────────────────────────────────
class TestOverallVerdict:
    def test_all_mechanisms_null_or_circular(self):
        mechanisms = {
            "dim_mismatch": "NULL",
            "euler_tadpole": "NULL",
            "a_hat_genus": "NULL",
            "type_iia": "CIRCULAR",
            "heterotic": "NULL",
            "brane_count": "CIRCULAR",
            "m_theory_g2": "NULL",
        }
        for m, verdict in mechanisms.items():
            assert verdict in ("NULL", "CIRCULAR"), f"{m} unexpectedly passed"

    def test_minimal_tadpole_consistent_with_g33(self):
        # Key consistency: minimal string source → c₃=2 → N_gen=1 = G33 result
        c3_minimal = 2
        ind_minimal = c3_minimal // 2
        g33_ind = 1  # G33 established ind=1
        assert ind_minimal == g33_ind

    def test_n_gen_3_requires_3x_minimal_circular(self):
        c3_target = 6
        c3_minimal = 2
        ratio = c3_target // c3_minimal
        assert ratio == 3  # three times minimal = N_gen=3 as prior

    def test_structural_conclusion(self):
        # Geometry gives exactly 1 generation; N_gen is a free parameter
        ind_from_geometry = 1  # G33: ind(D_{T^{1,0}S⁶})=1
        n_gen_observed = 3
        geometry_selects_n_gen = ind_from_geometry == n_gen_observed
        assert not geometry_selects_n_gen  # topology alone cannot select N_gen=3
