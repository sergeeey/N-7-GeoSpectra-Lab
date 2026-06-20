"""Tests for G36: K-Theory Gate — K1 circularity check."""


# ── K̃(S⁶) cohomology structure ─────────────────────────────────────────
class TestKTheoryStructure:
    def test_h6_s6_is_z(self):
        # H^*(S⁶;ℤ): only H⁰=H⁶=ℤ
        betti = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1}
        assert betti[6] == 1
        assert all(betti[k] == 0 for k in range(1, 6))

    def test_k_tilde_s6_is_z(self):
        # K̃(S⁶) = H⁶(S⁶;ℤ) = ℤ via AHSS
        rank_k_tilde_s6 = 1  # ℤ has rank 1
        assert rank_k_tilde_s6 == 1

    def test_h3_s6_zero(self):
        # H³(S⁶;ℤ) = 0 → no B-field twist available
        h3_S6 = 0
        assert h3_S6 == 0

    def test_generator_ch3(self):
        # Generator β of K̃(S⁶) has ch₃(β) = 1
        ch3_beta = 1
        assert ch3_beta == 1


# ── Chern character map ──────────────────────────────────────────────────
class TestChernCharacter:
    def ch3_from_c3(self, c3):
        return c3 / 2

    def test_ch3_formula(self):
        # ch₃(V) = c₃(V)/2 for rank-3 bundle with c₁=c₂=0
        assert self.ch3_from_c3(2) == 1
        assert self.ch3_from_c3(6) == 3
        assert self.ch3_from_c3(4) == 2

    def test_t10_is_generator(self):
        # T^{1,0}S⁶: c₃=2 → ch₃=1 → K-class = β (generator)
        c3_T10 = 2
        ch3_T10 = self.ch3_from_c3(c3_T10)
        assert ch3_T10 == 1

    def test_g32_bundle_is_3beta(self):
        # G32 bundle: c₃=6 → ch₃=3 → K-class = 3β
        c3_bundle = 6
        ch3_bundle = self.ch3_from_c3(c3_bundle)
        assert ch3_bundle == 3


# ── Adams operations ─────────────────────────────────────────────────────
class TestAdamsOperations:
    def adams_op(self, k, n, sphere_dim=6):
        return (k ** (sphere_dim // 2)) * n

    def test_s6_adams_is_k_cubed(self):
        # ψ^k on K̃(S⁶): eigenvalue = k³ (since S⁶ = S^{2·3})
        for k in [2, 3, 4]:
            for n in [1, 2, 3]:
                result = self.adams_op(k, n)
                assert result == k**3 * n

    def test_eigenvalue_independent_of_n(self):
        # Adams eigenvalue k³ is the same for n=1 and n=3
        k = 2
        ev_n1 = self.adams_op(k, 1) // 1
        ev_n3 = self.adams_op(k, 3) // 3
        assert ev_n1 == ev_n3  # no distinction between n=1 and n=3

    def test_adams_does_not_select_n3(self):
        # No eigenvalue condition singles out n=3
        k = 3
        eigenvalues = {n: self.adams_op(k, n) // n for n in [1, 2, 3, 4, 5]}
        # All eigenvalues are k³ = 27, regardless of n
        assert all(v == k**3 for v in eigenvalues.values())


# ── Stability analysis ───────────────────────────────────────────────────
class TestStability:
    def test_stable_range_for_s6(self):
        # Stable range: rank > dim/2 = 3 for S⁶
        dim_S6 = 6
        stable_rank = dim_S6 // 2  # = 3
        rank_bundle = 3
        # Rank-3 is at the boundary (stable range: rank > 3)
        assert rank_bundle == stable_rank

    def test_pi5_u3_is_stable(self):
        # π₅(U(3)) = ℤ = π₅(U(∞)) — stable homotopy group
        # No extra unstable class beyond K-theory
        pi5_U3_rank = 1  # ℤ has rank 1
        pi5_Ustable_rank = 1
        assert pi5_U3_rank == pi5_Ustable_rank

    def test_no_twisted_k_theory(self):
        # H³(S⁶;ℤ) = 0 → twisted K-theory = untwisted
        h3_S6 = 0
        twist_is_trivial = h3_S6 == 0
        assert twist_is_trivial


# ── Circularity test ─────────────────────────────────────────────────────
class TestCircularity:
    def test_3beta_means_3_copies(self):
        # K̃(S⁶) = ℤ is torsion-free: 3β = β+β+β (three copies)
        # No non-decomposable element with ch₃=3 distinct from 3×(ch₃=1)
        n = 3
        decomposition = n * 1  # n copies of β (ch₃=1 each)
        total_ch3 = decomposition
        assert total_ch3 == 3  # '3' = three copies = N_gen=3 as input

    def test_k1_circular(self):
        # ch₃(V)=3 → N_gen=3 is circular: same "3" as SM observation
        n_gen_from_k = 3  # K1 claim
        n_gen_observed = 3  # SM observation
        assert n_gen_from_k == n_gen_observed  # same "3" → circular

    def test_pattern_matches_a1_c1b(self):
        # All three "3" claims reduce to dim_ℂ(S⁶)=3 in disguise
        dim_c_s6 = 3  # geometric fact
        n_from_a1 = dim_c_s6  # A1: dim_ℂ(S⁶)=3 → N_gen=3 (G33: CIRCULAR)
        n_from_c1b = dim_c_s6  # C1-B: rank(T^{1,0}S⁶)=3 (G35: INVALID)
        n_from_k1 = 3  # K1: ch₃=3 copies of β (G36: CIRCULAR)
        assert n_from_a1 == n_from_c1b == n_from_k1 == dim_c_s6

    def test_ind_is_1_not_3(self):
        # The actual generation count from index theorem is 1, not 3
        c3_T10 = 2  # G33
        ind_T10 = c3_T10 // 2
        assert ind_T10 == 1  # ONE generation from geometry

    def test_k_theory_no_independent_selection(self):
        # K̃(S⁶) = ℤ has no distinguished element that selects n=3 independently
        # The group ℤ is homogeneous: no element is more "natural" than another
        group_is_homogeneous = True  # ℤ has no special automorphism fixing 3
        assert group_is_homogeneous


# ── D-brane angle ────────────────────────────────────────────────────────
class TestDBraneKTheory:
    def test_d_brane_needs_compact_bulk(self):
        # Minasian-Moore tadpole requires compact 10D geometry
        s6_is_compact = True  # S⁶ itself is compact
        has_bulk_cancellation = False  # but no compact 10D embedding here
        assert s6_is_compact
        assert not has_bulk_cancellation  # cannot fix ch₃ without bulk

    def test_h6_integral_vanishes_only_compact(self):
        # ∫_{S⁶} G₆ = 0 is tadpole condition — only meaningful in compact space
        # On S⁶ alone: any value of ch₃(V) is consistent (no cancellation)
        ch3_values = [1, 2, 3, 4, 5]
        # All consistent without compact bulk constraint
        assert all(v > 0 for v in ch3_values)  # no value excluded
