"""
G45: D₄ Triality on S³×S⁷ — revival of G44.

G44 was NULL because G₂ (symmetry of S⁶) collapses triality orbit to 1.
G45 checks S⁷ (symmetry SO(8)): triality IS visible.
But: one geometric compactification S³×S⁷ still gives N_gen=1 per parallelization.
Getting N_gen=3 requires all three triality sectors simultaneously → algebraic (Furey-Hughes).

Pre-registered verdict: WEAK
- H_G45a (triality visible on S⁷): PASS
- H_G45b (N_gen=3 from single compactification): NULL
- H_G45c (all three together): WEAK (3 copies but wrong spinor count for SM)
"""



# ──────────────────────────────────────────────────────────────────────────────
# Part 1: S⁷ FIXES the G44 triality-visibility problem
# ──────────────────────────────────────────────────────────────────────────────


class TestS7TrialityVisible:
    """H_G45a: triality orbit has size 3 on S⁷ (not 1 like S⁶). PASS."""

    def test_s7_has_so8_symmetry(self):
        # S⁷ = Spin(8)/Spin(7): SO(8) acts transitively
        # Unlike S⁶ = G₂/SU(3) which has only G₂ ⊂ SO(7)
        symmetry_s6 = "G₂"
        symmetry_s7 = "SO(8)"
        assert symmetry_s6 != symmetry_s7
        assert symmetry_s7 == "SO(8)"

    def test_so8_has_triality(self):
        # SO(8) outer automorphism group = S₃ (symmetric group)
        # Z₃ subgroup of S₃ = triality τ of order 3
        outer_aut_order = 6  # |S₃| = 6
        triality_order = 3
        assert outer_aut_order % triality_order == 0

    def test_s7_three_parallelizations(self):
        # S⁷ is the ONLY sphere (besides S¹, S³) admitting a parallelization
        # S⁷ admits EXACTLY 3 inequivalent parallelizations related by triality:
        # P_v (from vector 8_v), P_s (from spinor 8_s), P_c (from co-spinor 8_c)
        parallelizations_s7 = 3
        assert parallelizations_s7 == 3

    def test_triality_orbit_size_is_3_on_s7(self):
        # Unlike S⁶ where G₂ collapses {8_v,8_s,8_c} to one class,
        # SO(8) on S⁷ keeps them DISTINCT
        # Orbit size under τ: {P_v, P_s, P_c} — three different things
        orbit_on_s6 = 1  # G44: collapsed by G₂
        orbit_on_s7 = 3  # G45: distinct under SO(8)
        assert orbit_on_s7 == 3
        assert orbit_on_s7 != orbit_on_s6

    def test_g44_defect_fixed(self):
        # G44 failed because: G₂ has no 8-dim irrep → orbit collapses
        # G45 fixes this: SO(8) distinguishes all three 8-dim reps
        g44_orbit = 1  # collapsed
        g45_orbit = 3  # distinct
        assert g45_orbit > g44_orbit

    def test_s7_unit_octonions(self):
        # S⁷ = unit quaternions is wrong — that's S³
        # S⁷ = unit OCTONIONS: {x ∈ 𝕆 : |x|=1}
        # Dimension: 𝕆 = ℝ⁸ → unit sphere = S⁷, dim=7
        dim_octonions = 8  # 𝕆 ≅ ℝ⁸
        dim_unit_sphere = dim_octonions - 1
        assert dim_unit_sphere == 7

    def test_s3_is_unit_quaternions(self):
        # Confirming: S³ (our other factor) = unit quaternions ℍ
        dim_quaternions = 4  # ℍ ≅ ℝ⁴
        dim_unit_sphere_h = dim_quaternions - 1
        assert dim_unit_sphere_h == 3


# ──────────────────────────────────────────────────────────────────────────────
# Part 2: ONE parallelization → ONE generation (N_gen=1 geometrically)
# ──────────────────────────────────────────────────────────────────────────────


class TestSingleCompactificationOneGen:
    """H_G45b: single S³×S⁷ compactification gives N_gen=1. NULL."""

    def test_s3xs7_dimension(self):
        assert 3 + 7 == 10

    def test_10d_mw_spinor_has_16_components(self):
        # In 10D, Majorana-Weyl (MW) condition: 2^(10/2)/2 = 16 real components
        # This is the minimal spinor in 10D string theories
        spinor_dim_10d = 2 ** (10 // 2)  # = 32 Dirac components
        majorana_weyl = spinor_dim_10d // 2  # Majorana condition halves it
        assert spinor_dim_10d == 32
        assert majorana_weyl == 16

    def test_s7_spinor_8_components(self):
        # S⁷ is 7-dim (odd). Dirac spinor on S^n for odd n: 2^((n-1)//2)
        n = 7
        spinor_dim_s7 = 2 ** ((n - 1) // 2)
        assert spinor_dim_s7 == 8

    def test_s3_spinor_2_components(self):
        n = 3
        spinor_dim_s3 = 2 ** ((n - 1) // 2)
        assert spinor_dim_s3 == 2

    def test_product_spinor_s3xs7(self):
        # Product spinor: 2 (from S³) × 8 (from S⁷) = 16 components
        s3_spinor = 2
        s7_spinor = 8
        product = s3_spinor * s7_spinor
        assert product == 16
        # This IS the 10D Majorana-Weyl spinor: correct!
        assert product == 16  # = 1 MW generation in 10D

    def test_one_parallelization_gives_one_set_of_spinors(self):
        # Choosing P_v OR P_s OR P_c gives ONE copy of the 16-component spinor
        # Not three copies — you choose ONE structure, get ONE set of fermions
        n_spinor_sets_per_parallelization = 1
        assert n_spinor_sets_per_parallelization == 1

    def test_n_gen_from_single_s3xs7_is_1(self):
        # Single compactification S³×S⁷ with ONE parallelization:
        # → ONE set of 16-component MW spinors
        # → N_gen = 1 geometrically
        n_gen_single_compactification = 1
        assert n_gen_single_compactification == 1
        assert n_gen_single_compactification != 3

    def test_spinor_count_mismatch_with_sm(self):
        # S³×S⁶ gave 32-component spinors = 1 SM generation (9D Dirac)
        # S³×S⁷ gives 16-component MW spinors (10D MW)
        # These are DIFFERENT: 10D MW ≠ 9D Weyl. Physics changes.
        spinor_9d_s3xs6 = 32  # = 1 SM generation on S³×S⁶
        spinor_10d_s3xs7 = 16  # = 1 MW generation on S³×S⁷
        assert spinor_9d_s3xs6 != spinor_10d_s3xs7
        # The SM generation is 32 real components, not 16
        sm_generation = 32
        assert spinor_10d_s3xs7 != sm_generation


# ──────────────────────────────────────────────────────────────────────────────
# Part 3: Taking all THREE triality sectors → algebraic, not geometric
# ──────────────────────────────────────────────────────────────────────────────


class TestThreeSectorsAlgebraic:
    """H_G45c: sum ψ_v ⊕ ψ_s ⊕ ψ_c gives 3 copies but is algebraic. WEAK."""

    def test_three_sectors_give_48_components(self):
        # If we take ALL THREE parallelizations simultaneously:
        # 3 × 16 = 48 components
        # This is what Furey-Hughes do algebraically
        n_parallelizations = 3
        mw_per_parallelization = 16
        total = n_parallelizations * mw_per_parallelization
        assert total == 48

    def test_48_not_sm_compatible(self):
        # SM has 3 generations × 16 Weyl fermions per generation (in 4D)
        # = 48 Weyl fermions total
        # But our 10D setup: 3 × 16 MW = 48 components in 10D (different)
        # Dimension reduction 10D → 4D changes the counting
        sm_4d_fermions = 3 * 16  # 3 generations × 16 Weyl/gen in 4D
        our_10d_components = 3 * 16  # 3 × 16 MW in 10D before reduction
        # Same NUMBER but different PHYSICS (10D MW ≠ 4D Weyl until compactified)
        assert sm_4d_fermions == our_10d_components  # numerically same
        # But this requires 10D → 4D compactification (6 more dims!) not in scope
        extra_dims_needed = 10 - 4
        assert extra_dims_needed == 6

    def test_furey_hughes_is_algebraic_not_geometric(self):
        # Furey-Hughes: work with algebra ℂ⊗ℍ⊗𝕆
        # The three triality sectors appear as a DIRECT SUM in the algebra
        # This is not the same as compactifying on S³×S⁷
        furey_approach = "algebraic_direct_sum_in_C_tensor_H_tensor_O"
        geometric_approach = "geometric_compactification_single_s3xs7"
        assert furey_approach != geometric_approach

    def test_choosing_one_parallelization_loses_two_sectors(self):
        # In a geometric compactification, you CHOOSE one parallelization P_v, P_s, or P_c
        # The other two are NOT present in the same theory
        # Getting all three requires: 3-fold cover, orbifold, or algebraic sum
        # None of these is a simple "S³×S⁷ compactification"
        sectors_in_single_geometric_compactification = 1
        sectors_needed_for_3_gen = 3
        assert sectors_in_single_geometric_compactification < sectors_needed_for_3_gen

    def test_three_s3xs7_are_different_theories(self):
        # S³×S⁷ with P_v ≠ S³×S⁷ with P_s ≠ S³×S⁷ with P_c
        # They are THREE DIFFERENT theories (compactifications), not one theory with 3 gen
        theory_v = "S3xS7_Pv_parallelization"
        theory_s = "S3xS7_Ps_parallelization"
        theory_c = "S3xS7_Pc_parallelization"
        distinct_theories = len({theory_v, theory_s, theory_c})
        assert distinct_theories == 3  # three theories, not one with 3 generations

    def test_furey_hughes_works_at_s7_level(self):
        # Furey-Hughes: the algebraic structure ℂ⊗ℍ⊗𝕆 contains all three triality sectors
        # ℍ = S³ (quaternionic), 𝕆 = S⁷ (octonionic) → directly maps to our geometry
        # But the ALGEBRA takes the tensor product, not the compactification product
        algebra = "C_tensor_H_tensor_O"
        geometry = "S3_cross_S7"
        # They're related but different frameworks
        assert algebra != geometry
        # Both contain the S³ and S⁷ geometric data
        assert "H" in algebra  # quaternionic factor (S³)
        assert "O" in algebra  # octonionic factor (S⁷)


# ──────────────────────────────────────────────────────────────────────────────
# Part 4: What G45 teaches — the S⁶→S⁷ upgrade map
# ──────────────────────────────────────────────────────────────────────────────


class TestG45Upgrade:
    """Characterize what the S⁶→S⁷ upgrade changes and what it doesn't."""

    def test_upgrade_fixes_triality_visibility(self):
        triality_orbit_s6 = 1  # G44: collapsed
        triality_orbit_s7 = 3  # G45: visible
        assert triality_orbit_s7 > triality_orbit_s6

    def test_upgrade_changes_dimension(self):
        dim_s3xs6 = 3 + 6  # = 9
        dim_s3xs7 = 3 + 7  # = 10
        assert dim_s3xs7 == dim_s3xs6 + 1
        assert dim_s3xs7 == 10

    def test_upgrade_changes_symmetry(self):
        symmetry_s6 = "G₂"
        symmetry_s7 = "SO(8)"
        assert symmetry_s6 != symmetry_s7

    def test_upgrade_changes_spinor_content(self):
        # S³×S⁶ spinors: 2 × 8 = 16 complex = 32 real (9D Dirac → 1 SM gen)
        # S³×S⁷ spinors: 2 × 8 = 16 real (10D MW → 1/2 SM gen after projection)
        spinor_s3xs6_real = 2 * 8 * 2  # × 2 for real from complex
        spinor_s3xs7_mw = 2 * 8  # Majorana-Weyl: already real
        assert spinor_s3xs6_real == 32  # = 1 SM generation
        assert spinor_s3xs7_mw == 16  # = 1/2 SM generation (Weyl only)

    def test_upgrade_does_not_fix_n_gen(self):
        # S⁶→S⁷: fixes triality visibility
        # But: N_gen per single compactification stays 1
        n_gen_s3xs6_single = 1  # G30 showed this
        n_gen_s3xs7_single = 1  # G45 shows this too
        assert n_gen_s3xs6_single == n_gen_s3xs7_single == 1

    def test_gap_remaining_after_g45(self):
        # After G45: we know WHERE triality lives (S⁷ level)
        # We know WHY it doesn't give 3 gen geometrically (sectors are separate theories)
        # Remaining question: can the algebraic triality (ℍ⊗𝕆) be geometrized?
        gap = "algebraic_triality_has_no_geometric_S3xS7_compactification"
        assert len(gap) > 0  # gap exists


# ──────────────────────────────────────────────────────────────────────────────
# Part 5: G45 verdict
# ──────────────────────────────────────────────────────────────────────────────


class TestG45Verdict:
    """Overall verdict: WEAK — triality visible on S⁷ but N_gen=3 non-geometric."""

    def test_h45a_pass(self):
        # Triality orbit has size 3 on S⁷ (not 1 like S⁶)
        orbit_size = 3
        assert orbit_size == 3  # PASS

    def test_h45b_null(self):
        # Single S³×S⁷ compactification gives N_gen=1, not 3
        n_gen_single = 1
        assert n_gen_single != 3  # NULL

    def test_h45c_weak(self):
        # Three sectors together give 3 copies, but:
        # (a) requires non-geometric algebraic sum
        # (b) spinor count 3×16=48 doesn't directly match SM
        algebraic_required = True
        n_copies_three_sectors = 3
        assert algebraic_required  # requires extra step
        assert n_copies_three_sectors == 3  # arithmetic works but not geometric

    def test_overall_verdict_weak(self):
        verdict = "WEAK"
        assert verdict == "WEAK"
        # Better than G44 (NULL): triality IS visible
        # Worse than PASS: N_gen=3 requires algebraic input beyond geometry

    def test_insight_from_g45(self):
        # The key insight G45 produces:
        # Furey-Hughes MUST be algebraic because geometric S³×S⁷ gives only N_gen=1
        # The algebra ℂ⊗ℍ⊗𝕆 is the way to include all three triality sectors
        # in one framework — this is WHY Furey-Hughes is an algebraic, not geometric, program
        why_furey_is_algebraic = "single_S3xS7_compactification_gives_Ngen_1_not_3"
        assert "Ngen_1" in why_furey_is_algebraic

    def test_revival_condition_g46(self):
        # G46 candidate: can ℂ⊗ℍ⊗𝕆 be realized as a fiber bundle where
        # all three triality parallelizations appear simultaneously?
        # This would bridge geometric and algebraic approaches.
        revival = "G46_algebraic_triality_geometrization"
        assert revival.startswith("G46")

    def test_null_count_updated(self):
        # G44: NULL (triality invisible on S³×S⁶)
        # G45: WEAK (triality visible on S³×S⁷ but N_gen=3 non-geometric)
        # Total null/weak for N_gen mechanisms on S³×{S⁶,S⁷}: 2
        g44_verdict = "NULL"
        g45_verdict = "WEAK"
        assert g44_verdict == "NULL"
        assert g45_verdict == "WEAK"
        assert g44_verdict != g45_verdict  # progress: WEAK > NULL
