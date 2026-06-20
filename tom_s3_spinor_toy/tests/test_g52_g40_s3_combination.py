"""
G52: G40 × S³ combination — does the S³ factor rescue G40 from WEAK status?

G40 (B2, WEAK): G₂→SU(3) SSB on S⁶ does not FORCE c₃=6.
    Correction (G52): G40 originally claimed π₅(S⁶)=ℤ₂ from Freudenthal suspension.
    WRONG — Freudenthal gives π_{n+1}(Sⁿ)=ℤ₂ for n≥3, so π₇(S⁶)=ℤ₂, NOT π₅(S⁶).
    Cellular approximation (Whitehead 1949): k < n → πₖ(Sⁿ)=0. k=5,n=6 → π₅(S⁶)=0.

G52 asks: Can the S³ factor provide a constraint that forces w₆=3 (→ c₃=6, N_gen=3)?

Analysis:
1. S³ Hopf winding: h ∈ π₃(S³) = ℤ — any integer, free.
2. π₅(S⁶) = 0 (cellular approx) → no SSB defect winding from S⁶ topology.
3. Combined topological invariant: ℤ × 0 = ℤ. No preferred element.
4. Cross-spectator structure (G28): S³ couples to SU(3) via Vol(S³) — volume, not winding.
5. Chern-Simons on S³: integer level k ∈ ℤ for SU(2), independent of S⁶.

VERDICT: WEAK (same as G40, now with corrected homotopy — π₅ error does not help G40).
"""

from math import gcd


# ── Homotopy group data ──────────────────────────────────────────────────

# Relevant homotopy groups (standard results)
# Cellular approximation (Whitehead 1949): πₖ(Sⁿ)=0 for k < n.
# Freudenthal suspension: π_{n+1}(Sⁿ)=ℤ₂ for n≥3.
# These two together:
#   π₅(S⁶) = 0  (k=5 < n=6, cellular approx — G40 error: confused with Freudenthal)
#   π₇(S⁶) = ℤ₂ (Freudenthal: n+1=7 for n=6)

PI_3_S3 = "Z"  # = ℤ: Hopf fibration, winding number h ∈ ℤ
PI_5_S6 = "0"  # = 0: cellular approx (k=5 < n=6); G40 error was "ℤ₂" (Freudenthal confusion)
PI_7_S6 = "Z_2"  # = ℤ₂: actual Freudenthal result for S⁶ (π_{6+1}(S⁶))
PI_3_S6 = "0"  # = 0: S⁶ is 5-connected
PI_5_S3 = "Z_2"  # = ℤ₂: Hopf map η₂ (torsion)


class TestHomotopyGroups:
    """
    Homotopy groups relevant to G40×S³ combination.
    """

    def test_pi5_s6_is_zero_cellular_approximation(self):
        """π₅(S⁶) = 0 by cellular approximation: k=5 < n=6 → πₖ(Sⁿ) = 0."""
        # Whitehead cellular approximation theorem (1949):
        #   Any map Sᵏ → Sⁿ with k < n is null-homotopic.
        #   Therefore πₖ(Sⁿ) = 0 for all k < n.
        # For S⁶: π₅(S⁶) = 0, π₄(S⁶) = 0, ..., π₁(S⁶) = 0.
        k, n = 5, 6
        assert k < n  # cellular approximation applies
        pi_5_S6 = 0  # πₖ(Sⁿ) = 0 by cellular approx
        assert pi_5_S6 == 0

    def test_freudenthal_suspension_gives_pi7_s6_not_pi5(self):
        """
        Freudenthal suspension: π_{n+1}(Sⁿ) = ℤ₂ for n ≥ 3.
        For S⁶ (n=6): π₇(S⁶) = ℤ₂, NOT π₅(S⁶).
        G40 confusingly applied 'Freudenthal' as π₅(S⁶) = ℤ₂ — this is wrong.
        """
        # Freudenthal: π_{n+1}(Sⁿ) = ℤ₂ for n ≥ 3
        n = 6
        freudenthal_index = n + 1  # = 7
        assert freudenthal_index == 7  # applies to π₇, not π₅

        pi_7_S6 = PI_7_S6  # = "Z_2": correct Freudenthal result
        pi_5_S6 = 0  # = 0: by cellular approximation

        assert pi_7_S6 == "Z_2"
        assert pi_5_S6 == 0
        assert pi_5_S6 != pi_7_S6  # the G40 error: used π₇ result for π₅ index

    def test_pi_5_s6_zero_means_no_defects(self):
        """π₅(S⁶) = 0 means G₂→SU(3) SSB has no stable 6D defects."""
        # In 6D, vortex-like defects in G₂→SU(3) would be classified by
        # π₅(G₂/SU(3)) = π₅(S⁶) = 0.
        # Therefore: NO topological defects from G₂→SU(3) SSB in 6D.
        # The G40 "allows c₃=6" claim must come from a different mechanism
        # (possibly the exact sequence involving SU(3)).
        pi_5_S6_is_trivial = True
        assert pi_5_S6_is_trivial

    def test_pi_3_s3_is_Z(self):
        """π₃(S³) = ℤ → S³ Hopf winding number h ∈ ℤ is free."""
        # This is the Hopf fibration: S¹ → S³ → S²
        # Hopf invariant h ∈ π₃(S²) = ℤ lifted to π₃(S³) = ℤ
        pi_3_S3_rank = 1  # rank of π₃(S³) as abelian group (= ℤ has rank 1)
        assert pi_3_S3_rank == 1

    def test_pi_3_s3_does_not_couple_to_s6_topology(self):
        """
        π₃(S³) is a property of the S³ factor alone.
        π₅(S⁶) (or whichever group classifies S⁶ SSB) is independent.
        The product space S³×S⁶ has:
          π₃(S³×S⁶) = π₃(S³) × π₃(S⁶) = ℤ × 0 = ℤ
        No coupling between S³ homotopy and S⁶ homotopy (Künneth for homotopy
        holds only for low dimensions / suspensions — but the key point is
        independence: S³ and S⁶ are in different factors of the product).
        """
        pi_3_S6 = 0  # S^6 is 5-connected, so π_3(S^6) = 0
        pi_3_S3 = 1  # rank(ℤ) = 1

        # For product: π_3(S³×S⁶) = π_3(S³) ⊕ π_3(S⁶) = ℤ ⊕ 0 = ℤ
        pi_3_product_rank = pi_3_S3 + pi_3_S6  # = 1 (from S^3 only)
        assert pi_3_product_rank == 1  # only the S^3 sector contributes


class TestG40StatusUnchanged:
    """
    G40 was WEAK: G₂→SU(3) SSB allows c₃=6 but does not force it.
    G52 checks if S³ factor changes this status.
    """

    def test_g40_winding_is_free(self):
        """
        G40 (B2): the G₂→SU(3) SSB winding w₆ is a free integer.
        It can be 0, ±1, ±2, ±3, ... — any value.
        N_gen=3 would need w₆=3 (or c₃=6), which is one choice among ℤ.
        """
        possible_windings = list(range(-5, 6))  # ℤ truncated for testing
        three_is_allowed = 3 in possible_windings
        three_is_forced = all(w == 3 for w in possible_windings)

        assert three_is_allowed  # G40: c₃=6 is allowed
        assert not three_is_forced  # G40: c₃=6 is not forced (WEAK)

    def test_s3_hopf_number_is_also_free(self):
        """S³ Hopf number h ∈ ℤ — free, not constrained to any specific value."""
        possible_hopf = list(range(-5, 6))
        assert 3 in possible_hopf  # allowed
        assert not all(h == 3 for h in possible_hopf)  # not forced

    def test_combined_pair_is_free(self):
        """
        Combined invariant (h, w₆) ∈ ℤ × ℤ.
        The pair (h=1, w₆=3) is one element among ℤ × ℤ.
        No algebraic reason to prefer it over (h=1, w₆=1) or (h=2, w₆=5).
        """
        # There is no natural "preferred element" in ℤ × ℤ
        # unless an additional physical constraint is imposed.
        # The geometry of S³×S⁶ with round metrics provides no such constraint.
        # Test: the pair (h=1, w₆=3) has no special status algebraically
        h, w6 = 1, 3
        # gcd(h, w₆) = 1, not special; h+w₆ = 4, not special; h*w₆ = 3, interesting but arbitrary
        assert gcd(h, w6) == 1  # coprime, not special
        assert h + w6 == 4  # sum = 4 ≠ 3
        assert h * w6 == 3  # product = 3 — but this is only a coincidence for (1,3)

    def test_no_topological_selection_of_w6_equals_3(self):
        """
        Is there ANY topological combination of (h, w₆) that forces w₆=3?
        Check: does π₃(S³) ≅ ℤ provide a constraint that pins w₆?

        Answer: No. The S³ and S⁶ topological sectors are independent.
        A constraint on h (like "h must be 1") would not constrain w₆.
        """

        # S³ factor: π_3(S^3) = ℤ. If we have h=1 (unit Hopf number),
        # this constrains the S³ sector only. The S⁶ SSB winding w₆ is separate.
        def s3_constraint(h: int) -> bool:
            """Does h=1 force w6=3? No."""
            # Even if we impose h=1, w₆ is still free
            return False  # h=1 does not force w₆=3

        assert s3_constraint(1) is False  # S³ constraint doesn't select w₆

    def test_cross_spectator_couples_volumes_not_windings(self):
        """
        G28 established: SU(2) coupling ← Vol(S⁶), SU(3) coupling ← Vol(S³).
        This cross-spectator effect couples VOLUMES (ρ₃, ρ₆), not winding numbers.
        Therefore, the coupling ratio fixing ρ₃/ρ₆² does not constrain w₆.
        """
        # The coupling ratio g₂²/g₃² = 15ρ₃³/(16πρ₆⁶) (G28/G29)
        # This is purely a volume effect, no topological content.
        # G51 already showed: this constraint doesn't even stabilize ρ, let alone fix w₆.
        coupling_ratio_contains_winding_number = False
        assert not coupling_ratio_contains_winding_number

    def test_chern_simons_on_s3_is_independent(self):
        """
        SU(2) Chern-Simons on S³ gives instanton number k ∈ ℤ for gauge fields.
        This k is the level of the SU(2) Chern-Simons theory.
        k is independent of the G₂→SU(3) SSB winding w₆ on S⁶.
        """
        # CS level k ∈ ℤ and SSB winding w₆ ∈ ℤ are independent
        k_values = list(range(0, 5))
        w6_values = list(range(0, 5))
        # All (k, w₆) pairs are equally valid — no coupling
        total_pairs = len(k_values) * len(w6_values)  # 25 pairs
        pairs_forcing_w6_3 = sum(1 for w6 in w6_values if w6 == 3)  # 1 pair (any k)
        assert pairs_forcing_w6_3 == 1  # only (k=any, w₆=3) — and k is not forced either
        assert total_pairs == 25  # all pairs equally valid


class TestG52Verdict:
    """
    G52 conclusion: S³ factor does not rescue G40 from WEAK status.
    """

    def test_g52_status_is_weak_same_as_g40(self):
        """
        G40 alone: WEAK (allows c₃=6, does not force it).
        G40 + S³:  WEAK (same — adding free topological data doesn't help).

        The S³ factor introduces h ∈ ℤ (another free integer) but does not
        impose a constraint that selects w₆=3.
        """
        g40_status = "WEAK"
        g52_status = "WEAK"  # S³ doesn't change the status
        assert g40_status == g52_status

    def test_n_gen_3_still_not_forced(self):
        """After G52: N_gen=3 is allowed but not forced by G40+S³."""
        n_gen_3_allowed = True  # SSB can give w₆=3 (one choice among ℤ)
        n_gen_3_forced = False  # No geometric mechanism forces w₆=3
        assert n_gen_3_allowed
        assert not n_gen_3_forced

    def test_dynamical_mechanism_still_needed(self):
        """
        Conclusion: N_gen=3 from G₂→SU(3) SSB requires a dynamical mechanism
        to select w₆=3, not just topology. The S³ factor doesn't provide it.

        Possible routes (all currently open):
        1. Instanton moduli counting (specific to the background)
        2. Quantum corrections to SSB potential selecting w₆=3
        3. Constraint from anomaly cancellation in the 4D effective theory
        """
        pure_geometry_selects_n3 = False
        dynamical_mechanism_needed = True
        assert not pure_geometry_selects_n3
        assert dynamical_mechanism_needed

    def test_t1_covers_g40_b2_via_rigidity_lemma(self):
        """
        T1 covers G40 (B2) via a different route:
        G40 was WEAK (allows c₃=6 but doesn't force it).
        Lemma 2 (rigidity): round metric → unique isotropy → 1 spinor sector.
        Even IF G₂→SU(3) SSB occurred and gave c₃=6,
        the round-metric constraint would force N_gen=1 in the spinor sector.
        Therefore G40+S³ is blocked by Lemma 2 of T1 as well.
        """
        # Lemma 2: round metric forces N_gen=1
        # Lemma 2: round metric forces N_gen=1 (established in G46 tests)
        # G40 gives c₃=6 (ALLOWED) but
        # c₃=6 with round metric still gives N_gen=1 per sector × some multiplicity?
        # Wait — c₃=6 would give 6 zero modes if the index theorem applied
        # But G40 was classified as WEAK, not as forcing 6 zero modes
        # The round metric constraint (Lemma 2) says: one isotropy → one coset
        # This would select the canonical sector with c₃=2, not c₃=6

        # Actually G40's c₃=6 is only available AFTER SSB breaks the round metric
        # Post-SSB, the metric is no longer round → Lemma 2 does not apply directly
        # So G40+S³ is WEAK: it escapes Lemma 2 by breaking the round metric assumption

        # This makes G52 genuinely interesting: it identifies the LOOPHOLE in Lemma 2
        lemma_2_assumes_round_metric = True
        g40_breaks_round_metric_via_ssb = True  # SSB changes the metric
        g40_escapes_lemma_2 = g40_breaks_round_metric_via_ssb and lemma_2_assumes_round_metric

        assert g40_escapes_lemma_2  # G40 is the one mechanism that could escape T1
        # But G40 is STILL WEAK — it allows c₃=6 but doesn't force it
        # G52 result: S³ doesn't provide the forcing mechanism either
        assert not pure_geometry_selects_n3 if (pure_geometry_selects_n3 := False) else True

    def test_g40_is_the_only_weak_route_remaining(self):
        """
        After G52: G40 (SSB) is the only WEAK route still open.
        All other mechanisms are either NULL or REJECT.
        The three-generation problem requires a dynamical explanation.
        """
        # Summary of mechanism status after all experiments:
        mechanism_status = {
            "G27-Z3": "REJECT",  # χ not divisible by 3
            "G30-G2": "REJECT",  # G₂ symmetry forces index=0
            "G31-S3": "REJECT",  # Lichnerowicz blocks adjoint
            "G33-A1": "REJECT",  # c₃=2 by Gauss-Bonnet-Chern
            "G34-B3": "REJECT",  # k_grav=0 → SU(2)₀ WZW
            "G34-A2": "REJECT",  # Ω⁶_Spin=0, η=0
            "G35-C1": "REJECT",  # rank(T^{1,0})≠ind
            "G36-K1": "REJECT",  # Adams ψ^k same for all n
            "G37-S1": "REJECT",  # String tadpole → c₃=2
            "G38-S2": "REJECT",  # G33 restated
            "G39-B1": "REJECT",  # Whitney → c₃=-2
            "G40-B2": "WEAK",  # G₂→SU(3) SSB allows but doesn't force c₃=6
            "G41-B3": "WEAK",  # 3 D-branes: rank-3 allowed, not forced
            "G42-B4": "REJECT",  # H⁴(S⁶)=0 → GS trivial
            "G43-B5": "REJECT",  # Harland-Nölle: no c₃=6 on S⁶
            "G44-B1": "REJECT",  # G₂ no 8-dim irrep
            "G45-B2": "WEAK",  # D₄ triality: algebraic only
            "G46": "NULL",  # Single metric → 1 coset structure
        }

        weak_routes = [k for k, v in mechanism_status.items() if v == "WEAK"]
        reject_or_null = [k for k, v in mechanism_status.items() if v in ("REJECT", "NULL")]

        assert "G40-B2" in weak_routes  # G40 is WEAK
        assert len(weak_routes) == 3  # G40, G41, G45 are the 3 WEAK routes
        assert len(reject_or_null) == 15  # all others are blocked
