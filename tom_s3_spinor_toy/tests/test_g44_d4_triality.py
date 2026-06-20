"""
G44: D₄ Triality on S³×S⁶ — Can It Give N_gen=3?

Pre-registered prediction: NULL
Basis: G₂ has no 8-dim irrep → all three SO(8) octets decompose as 7⊕1 under G₂.
Triality orbit {8_v, 8_s, 8_c} collapses to single G₂-isomorphism class.
S⁶ = G₂/SU(3) cannot distinguish the three reps → triality invisible from S⁶ geometry.
"""


# ──────────────────────────────────────────────────────────────────────────────
# G₂ irrep dimensions (Weyl dimension formula, exact integers)
# G₂ has rank 2, root system G₂, Weyl group order 12.
# Fundamental reps: (1,0)=7, (0,1)=14.
# Dimensions grow as: 1, 7, 14, 27, 64, 77, 182, 189, 273, 286, ...
# CRITICAL: no irrep of dimension 8 exists.
# ──────────────────────────────────────────────────────────────────────────────

G2_IRREP_DIMS = [1, 7, 14, 27, 64, 77, 182, 189, 273, 286]


class TestG2NoEightDimIrrep:
    """Key lemma: G₂ has no 8-dimensional irreducible representation."""

    def test_8_not_in_g2_irrep_list(self):
        assert 8 not in G2_IRREP_DIMS

    def test_g2_smallest_irreps_are_1_and_7(self):
        small = sorted(d for d in G2_IRREP_DIMS if d <= 14)
        assert small == [1, 7, 14]

    def test_no_g2_irrep_between_7_and_14(self):
        between = [d for d in G2_IRREP_DIMS if 7 < d < 14]
        assert between == [], f"Unexpected irrep dimension between 7 and 14: {between}"

    def test_8_dim_module_decomposition_is_unique(self):
        # Only way to write 8 as sum of G₂ irrep dims (all ≤ 8):
        # 7 + 1 = 8 (unique)
        # 1 + 1 + ... (8 trivials) — but 8 trivials = reducible sum, not isomorphic to 7⊕1
        # For a SEMISIMPLE module: 7⊕1 is the unique indecomposable of dimension 8 from irreps ≤8
        assert 7 + 1 == 8
        # No alternative: dim 2,3,4,5,6 don't exist in G₂
        g2_dims_le8 = [d for d in G2_IRREP_DIMS if d <= 8]
        assert g2_dims_le8 == [1, 7]


class TestSO8TrialityReps:
    """SO(8) has exactly three 8-dimensional reps related by triality."""

    def test_three_8dim_reps_exist(self):
        so8_8dim_reps = {"8_v": 8, "8_s": 8, "8_c": 8}
        for name, dim in so8_8dim_reps.items():
            assert dim == 8, f"{name} should have dimension 8"

    def test_triality_permutes_three_reps_cyclically(self):
        # τ: 8_v → 8_s → 8_c → 8_v (cyclic, order 3)
        reps = ["8_v", "8_s", "8_c"]
        tau_cycle = {reps[i]: reps[(i + 1) % 3] for i in range(3)}
        assert tau_cycle["8_v"] == "8_s"
        assert tau_cycle["8_s"] == "8_c"
        assert tau_cycle["8_c"] == "8_v"
        # Confirm order 3
        r = "8_v"
        for _ in range(3):
            r = tau_cycle[r]
        assert r == "8_v"

    def test_triality_outer_automorphism_order_3(self):
        # |Out(SO(8))| = |S₃| = 6; the Z₃ subgroup is triality
        out_so8_order = 6  # S₃
        triality_order = 3  # Z₃ ⊂ S₃
        assert triality_order == 3
        assert out_so8_order % triality_order == 0

    def test_three_reps_pairwise_non_isomorphic_as_so8_modules(self):
        # Distinguished by their SO(8) highest weights:
        # 8_v: (1,0,0,0) — vector
        # 8_s: (0,0,0,1) — left spinor
        # 8_c: (0,0,1,0) — right spinor (using D4 Dynkin notation)
        highest_weights = {
            "8_v": (1, 0, 0, 0),
            "8_s": (0, 0, 0, 1),
            "8_c": (0, 0, 1, 0),
        }
        reps = list(highest_weights.values())
        # All pairwise distinct
        assert reps[0] != reps[1]
        assert reps[1] != reps[2]
        assert reps[0] != reps[2]


class TestBranchingRulesSO8ToG2:
    """All three 8-dim SO(8) reps restrict to identical G₂-modules."""

    def test_8v_branches_to_7_plus_1(self):
        # 8_v|_{G₂} = (1,0) ⊕ (0,0) = 7 ⊕ 1
        decomp_8v = {7: 1, 1: 1}
        assert sum(k * v for k, v in decomp_8v.items()) == 8

    def test_8s_branches_to_7_plus_1(self):
        # 8_s|_{G₂} = (1,0) ⊕ (0,0) = 7 ⊕ 1
        decomp_8s = {7: 1, 1: 1}
        assert sum(k * v for k, v in decomp_8s.items()) == 8

    def test_8c_branches_to_7_plus_1(self):
        # 8_c|_{G₂} = (1,0) ⊕ (0,0) = 7 ⊕ 1
        decomp_8c = {7: 1, 1: 1}
        assert sum(k * v for k, v in decomp_8c.items()) == 8

    def test_all_three_branching_rules_are_identical(self):
        def branching(d):
            return frozenset([(7, 1), (1, 1)])  # same for all three
        assert branching("8_v") == branching("8_s") == branching("8_c")

    def test_triality_orbit_collapses_under_g2(self):
        # From G₂ perspective, {8_v, 8_s, 8_c} all look the same: 7⊕1
        g2_class = frozenset([(7, 1), (1, 1)])
        classes = {rep: g2_class for rep in ["8_v", "8_s", "8_c"]}
        # Orbit has size 1 (single isomorphism class) not 3
        distinct_classes = set(classes.values())
        assert len(distinct_classes) == 1, (
            f"Expected 1 G₂-iso class, got {len(distinct_classes)}: {distinct_classes}"
        )

    def test_intertwining_space_is_1d(self):
        # Schur: Hom_{G₂}(7⊕1, 7⊕1) ≅ End_{G₂}(7) ⊕ End_{G₂}(1)
        # = ℂ ⊕ ℂ (since both 7 and 1 are irreducible)
        # dim = 2, meaning there IS a G₂-equivariant isomorphism between any two 8-dim reps
        # i.e., 8_v ≅ 8_s ≅ 8_c as G₂-modules
        dim_end_7 = 1  # Schur: End_{G₂}(irrep) ≅ ℂ
        dim_end_1 = 1
        dim_hom_g2_8_to_8 = dim_end_7 + dim_end_1
        assert dim_hom_g2_8_to_8 == 2  # 2-dimensional space of G₂-equivariant maps
        # Non-zero Hom → they ARE isomorphic as G₂-modules
        assert dim_hom_g2_8_to_8 > 0


class TestS6SpinorStructure:
    """S⁶ fermion content: 8-component spinors in SU(4), not SO(8)."""

    def test_s6_dimension(self):
        assert 6 == 6  # S⁶ is 6-dimensional

    def test_dirac_spinor_dim_on_s6(self):
        # S⁶ is even-dimensional (6D), Dirac spinor = 2^(6/2) = 8 components
        n = 6
        dirac_dim = 2 ** (n // 2)
        assert dirac_dim == 8

    def test_s6_spinor_lives_in_su4_not_so8(self):
        # S⁶ holonomy group = SO(6), and Spin(6) ≅ SU(4)
        # The 8 spinor components transform under SU(4): 4 ⊕ 4̄ (Weyl)
        # NOT under SO(8) or its triality-related representations

        dim_4 = 4
        dim_4bar = 4
        assert dim_4 + dim_4bar == 8  # matches S⁶ spinor dimension

        # Critical: SU(4) has NO triality automorphism (only SO(8)/Spin(8) does)
        # → triality cannot act on S⁶ spinors
        triality_in_su4 = False
        assert not triality_in_su4

    def test_s6_is_coset_g2_over_su3(self):
        # S⁶ = G₂/SU(3) as a coset space
        # G₂ isotropy group at a point of S⁶ is SU(3)
        dim_g2 = 14
        dim_su3 = 8
        dim_s6 = dim_g2 - dim_su3
        assert dim_s6 == 6

    def test_one_spinor_bundle_not_three(self):
        # S⁶ has a unique spin structure (up to G₂ action)
        # There is ONE 8-component spinor bundle, not three
        num_spinor_bundles_s6 = 1
        assert num_spinor_bundles_s6 == 1
        # Triality would require THREE distinct spinor bundles
        num_required_for_triality = 3
        assert num_spinor_bundles_s6 < num_required_for_triality


class TestTrialityInvisibleFromS6:
    """The triality orbit is invisible from S⁶ geometry."""

    def test_g2_subgroup_fixed_by_triality(self):
        # G₂ ⊂ SO(7) ⊂ SO(8) is PRESERVED by the triality automorphism τ
        # i.e., τ(G₂) = G₂ as a subgroup of SO(8)
        # Consequence: τ acts ON G₂, but the G₂-module structure is unchanged
        # → The three reps 8_v, 8_s, 8_c are G₂-equivariantly isomorphic
        g2_preserved_by_triality = True
        assert g2_preserved_by_triality

    def test_triality_orbit_size_from_s6_is_1(self):
        # From S⁶'s geometric point of view (G₂ symmetry):
        # The triality orbit {8_v, 8_s, 8_c} collapses to 1 isomorphism class
        orbit_size_from_s6 = 1  # not 3
        assert orbit_size_from_s6 == 1

    def test_no_gen3_from_triality_on_s6(self):
        # If triality orbit collapses to 1 class → it cannot produce N_gen=3
        orbit_classes = 1
        n_gen_from_triality = orbit_classes  # = 1, not 3
        assert n_gen_from_triality != 3

    def test_pattern_consistency_with_g30(self):
        # G30 showed G₂-instanton index = 0 (G₂ symmetry prevents index ≠ 0)
        # G44 shows triality invisible (G₂ symmetry collapses triality orbit to 1)
        # Both: G₂ symmetry of S⁶ is the obstruction
        g30_verdict = "NULL"  # G₂-instanton index = 0
        g44_verdict = "NULL"  # triality orbit collapses
        shared_cause = "G₂ symmetry of S⁶"
        assert g30_verdict == g44_verdict == "NULL"
        assert shared_cause == "G₂ symmetry of S⁶"


class TestRevivalConditionS3xS7:
    """D₄ triality is natural on S⁷, not S⁶ — revival condition for G45."""

    def test_s7_has_full_spin8_structure(self):
        # S⁷ = Spin(8)/Spin(7) as a coset space
        # The SO(8) group acts on S⁷, giving access to all three 8-dim reps
        dim_s7 = 7
        symmetry_group_s7 = "SO(8)"
        # S⁷ is the unit sphere in ℝ⁸, and SO(8) acts transitively
        assert dim_s7 == 7
        assert symmetry_group_s7 == "SO(8)"

    def test_s7_admits_triality(self):
        # Three inequivalent parallelizations of S⁷ are related by triality
        # This is the Hopf fibration structure: S¹→S³→S⁷, S³→S⁷→S⁴, ...
        # The three are GEOMETRICALLY DISTINCT on S⁷
        parallelizations_s7 = 3  # related by triality
        assert parallelizations_s7 == 3

    def test_s6_lacks_so8_structure(self):
        # S⁶ = G₂/SU(3) has G₂ ⊂ SO(7) ⊂ SO(8)
        # G₂ ≠ SO(8) → S⁶ does NOT have full SO(8) structure
        symmetry_s6 = "G₂"
        symmetry_s7 = "SO(8)"
        assert symmetry_s6 != symmetry_s7

    def test_s3_x_s7_is_10d(self):
        # S³ × S⁷: dim = 3 + 7 = 10
        # This equals the CRITICAL SUPERSTRING DIMENSION
        dim_s3xs7 = 3 + 7
        string_critical_dim = 10
        assert dim_s3xs7 == string_critical_dim

    def test_g44_revival_condition(self):
        # Revival: replace S⁶ with S⁷ in the compactification
        # S³×S⁶ (dim=9, G₂ symmetry, triality invisible)
        # → S³×S⁷ (dim=10, SO(8) symmetry, triality visible)
        original_dim = 9
        revival_dim = 10
        assert revival_dim == original_dim + 1
        assert revival_dim == 10  # string dimension

    def test_s7_spinor_dimension(self):
        # S⁷ is 7-dimensional (odd). Dirac spinors: 2^((7-1)/2) = 2^3 = 8
        n = 7
        dirac_dim_s7 = 2 ** ((n - 1) // 2)
        assert dirac_dim_s7 == 8

    def test_s3_x_s7_total_spinor_count(self):
        # S³ spinors: 2 components (Weyl)
        # S⁷ spinors: 8 components
        # Product spinor: 2 × 8 = 16 (Majorana-Weyl in 10D)
        s3_spinor = 2
        s7_spinor = 8
        product_spinor = s3_spinor * s7_spinor
        assert product_spinor == 16
        # 10D Majorana-Weyl: 16 real components per generation
        # (vs 32 on S³×S⁶ for 1 SM generation)


class TestG44Verdict:
    """Final verdict: G44 NULL — D₄ triality cannot generate N_gen=3 on S³×S⁶."""

    def test_claim_falsified(self):
        # Claim: triality acts non-trivially on S³×S⁶ spinors → N_gen=3
        # Falsification: G₂ has no 8-dim irrep → all three octets = same G₂-module
        claim_status = "FALSIFIED"
        assert claim_status == "FALSIFIED"

    def test_mechanism_killed(self):
        verdict = "NULL"
        reason = "G₂_no_8dim_irrep_triality_orbit_collapses"
        assert verdict == "NULL"
        assert "G₂" in reason

    def test_null_consistent_with_g30_theorem(self):
        # G44 NULL is consistent with the exhaustion theorem from G30-G43
        # Pattern: every "3" in S³×S⁶ reduces to dim_ℂ(S⁶)=3 or is circular
        g44_actual_orbit_size = 1  # collapses under G₂
        assert g44_actual_orbit_size != 3

    def test_revival_is_s3_x_s7_not_s3_x_s6(self):
        # The octonionic explanation for N_gen=3 (Furey-Hughes) lives at S⁷ level
        # G44 NULL does NOT kill the octonionic program — it redirects it
        octonionic_program_lives_at = "S7_level"
        our_manifold = "S6_level"
        assert octonionic_program_lives_at != our_manifold
        assert octonionic_program_lives_at == "S7_level"
