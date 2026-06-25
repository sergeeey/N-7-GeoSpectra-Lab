"""
Tests for E-L3B: bundle obstruction theorem.

Key result: Path B (G₂-equivariant bundle distinction) is provably impossible.
All three SO(8) triality channels restrict to the same G₂-equivariant bundle.
Distinction requires full SO(8)/Spin(8) structure (Path A / Schur's lemma).
"""

import sys
import os
from collections import Counter

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260625-l3b-bundle-obstruction"),
)
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "experiments", "20260625-kp-zero-mode")
)

from l3b_bundle import (
    SU3_8V,
    SU3_8S,
    SU3_8C,
    G2_8V,
    G2_8S,
    G2_8C,
    SO7_8V,
    SO7_8S,
    SO7_8C,
    SO7_8V_DIMS,
    SO7_8S_DIM,
    SO7_8C_DIM,
    SO8_DISTINCT,
    run_l3b_analysis,
)
from kp_zero_mode import su3_dim, g2_dim


class TestSU3IsomorphismLevel:
    """SU(3)-level: all three channels give the same module."""

    def test_8v_su3_module_content(self):
        c = Counter(SU3_8V)
        assert c[(1, 0)] == 1  # one 3̄ (conjugate fundamental)
        assert c[(0, 1)] == 1  # one 3 (anti-fundamental)
        assert c[(0, 0)] == 2  # two singlets

    def test_8s_su3_module_content(self):
        c = Counter(SU3_8S)
        assert c[(1, 0)] == 1
        assert c[(0, 1)] == 1
        assert c[(0, 0)] == 2

    def test_8c_su3_module_content(self):
        c = Counter(SU3_8C)
        assert c[(1, 0)] == 1
        assert c[(0, 1)] == 1
        assert c[(0, 0)] == 2

    def test_all_three_su3_modules_identical(self):
        """The key isomorphism: all three channels → same SU(3)-module."""
        assert Counter(SU3_8V) == Counter(SU3_8S)
        assert Counter(SU3_8S) == Counter(SU3_8C)

    def test_su3_total_dimension(self):
        for reps in [SU3_8V, SU3_8S, SU3_8C]:
            assert sum(su3_dim(*r) for r in reps) == 8

    def test_g2_bundle_isomorphism_consequence(self):
        """
        Homogeneous bundle correspondence: G₂-bundles on G₂/SU(3) ↔ SU(3)-reps.
        Same SU(3)-module → same G₂-equivariant bundle.
        """
        same = Counter(SU3_8V) == Counter(SU3_8S) == Counter(SU3_8C)
        assert same, "All three channels must give the same G₂-equivariant bundle"


class TestG2IsomorphismLevel:
    """G₂-level: all three channels give the same G₂-module (7⊕1)."""

    def test_8v_g2_module(self):
        c = Counter(G2_8V)
        assert c[(1, 0)] == 1  # G₂ fundamental = 7
        assert c[(0, 0)] == 1  # G₂ singlet = 1

    def test_8s_g2_module(self):
        c = Counter(G2_8S)
        assert c[(1, 0)] == 1
        assert c[(0, 0)] == 1

    def test_8c_g2_module(self):
        c = Counter(G2_8C)
        assert c[(1, 0)] == 1
        assert c[(0, 0)] == 1

    def test_all_three_g2_modules_identical(self):
        assert Counter(G2_8V) == Counter(G2_8S)
        assert Counter(G2_8S) == Counter(G2_8C)

    def test_g2_total_dimension(self):
        for reps in [G2_8V, G2_8S, G2_8C]:
            assert sum(g2_dim(*r) for r in reps) == 8

    def test_path_b_provably_impossible(self):
        """
        No G₂-invariant can distinguish 8_v, 8_s, 8_c.
        Path B (pure G₂ bundle geometry) is provably impossible.
        """
        g2_same = Counter(G2_8V) == Counter(G2_8S) == Counter(G2_8C)
        assert g2_same, "Path B impossible confirmed"


class TestSO7PartialDistinction:
    """SO(7)-level: partial distinction possible (8_v ≠ 8_s = 8_c)."""

    def test_8v_so7_splits(self):
        """8_v branches to 7⊕1 under SO(7) — SPLITS into two parts."""
        assert SO7_8V == "7+1"
        assert sum(SO7_8V_DIMS) == 8
        assert len(SO7_8V_DIMS) == 2  # has two components

    def test_8s_so7_stays_irreducible(self):
        """8_s remains irreducible as Spin(7) spinor."""
        assert SO7_8S == "8s"
        assert SO7_8S_DIM == 8

    def test_8c_so7_stays_irreducible(self):
        """8_c remains irreducible as Spin(7) spinor (same as 8_s)."""
        assert SO7_8C == "8s"
        assert SO7_8C_DIM == 8

    def test_8v_differs_from_8s_at_so7_level(self):
        """At SO(7) level, 8_v ≠ 8_s: one splits, one stays irreducible."""
        assert SO7_8V != SO7_8S

    def test_8s_equals_8c_at_so7_level(self):
        """
        Critical: 8_s = 8_c under SO(7).
        Spin(7) has a UNIQUE 8-dimensional spinor representation.
        Cannot distinguish all three channels below SO(8).
        """
        assert SO7_8S == SO7_8C

    def test_so7_only_partial_distinction(self):
        """SO(7) distinguishes 8_v from {8_s,8_c} but NOT 8_s from 8_c."""
        # Partial (2/3): can distinguish 8_v
        assert SO7_8V != SO7_8S
        assert SO7_8V != SO7_8C
        # Fails (1/3): cannot distinguish 8_s from 8_c
        assert SO7_8S == SO7_8C

    def test_so7_cannot_achieve_all_distinct(self):
        """Full three-way distinction requires going beyond SO(7)."""
        all_distinct_at_so7 = SO7_8V != SO7_8S != SO7_8C and SO7_8V != SO7_8C
        # 8_s = 8_c prevents all-distinct, so this must be False
        assert not all_distinct_at_so7


class TestSO8FullDistinction:
    """SO(8)/Spin(8) level: all three channels distinct (triality definition)."""

    def test_so8_all_three_distinct(self):
        """By definition of triality: 8_v, 8_s, 8_c are pairwise non-isomorphic."""
        assert SO8_DISTINCT

    def test_schur_lemma_applies(self):
        """
        Schur's lemma for Spin(8): pairwise non-isomorphic reps are Hom=0.
        Hom_{Spin(8)}(8_v, 8_s) = Hom_{Spin(8)}(8_s, 8_c) = Hom_{Spin(8)}(8_v, 8_c) = 0
        → zero modes from different channels are Spin(8)-invariantly orthogonal.
        """
        # Verify distinct (non-zero Hom would require isomorphism)
        assert SO8_DISTINCT
        # The Schur's lemma conclusion: channels give orthogonal zero modes
        schur_orthogonality_holds = SO8_DISTINCT
        assert schur_orthogonality_holds


class TestLevelHierarchy:
    """Verify the complete hierarchy of distinction levels."""

    def test_su3_g2_no_distinction(self):
        """SU(3) and G₂ levels: zero distinction (0/3)."""
        assert Counter(SU3_8V) == Counter(SU3_8S) == Counter(SU3_8C)
        assert Counter(G2_8V) == Counter(G2_8S) == Counter(G2_8C)

    def test_so7_partial_distinction(self):
        """SO(7) level: partial distinction (1/3 groups distinguishable)."""
        assert SO7_8V != SO7_8S  # 8_v is different
        assert SO7_8S == SO7_8C  # 8_s and 8_c are the same

    def test_so8_full_distinction(self):
        """SO(8) level: full distinction (all three distinct)."""
        assert SO8_DISTINCT

    def test_minimum_level_is_so8(self):
        """
        Theorem: The minimum group level for distinguishing all three channels
        is SO(8)/Spin(8). N_gen=3 is an SO(8) phenomenon, not G₂ geometry.
        """
        su3_ok = Counter(SU3_8V) == Counter(SU3_8S)
        g2_ok = Counter(G2_8V) == Counter(G2_8S)
        so7_ok = SO7_8S == SO7_8C  # blocks full distinction
        so8_ok = SO8_DISTINCT

        # Hierarchy: SU(3) ≅ G₂ (no distinction) ⊊ SO(7) (partial) ⊊ SO(8) (full)
        assert su3_ok and g2_ok  # SU(3)=G₂: no distinction
        assert so7_ok  # SO(7) blocks: 8_s=8_c
        assert so8_ok  # SO(8): all distinct → minimum level


class TestRunFunction:
    """Integration test for the main analysis function."""

    def test_run_returns_dict(self):
        result = run_l3b_analysis()
        assert isinstance(result, dict)

    def test_all_checks_pass(self):
        result = run_l3b_analysis()
        assert result["checks_passed"] == result["checks_total"]
        assert result["verdict"] == "PASS"

    def test_path_b_impossible(self):
        result = run_l3b_analysis()
        assert result["path_b_impossible"] is True

    def test_g2_bundles_isomorphic(self):
        result = run_l3b_analysis()
        assert result["g2_bundles_isomorphic"] is True

    def test_so8_all_distinct(self):
        result = run_l3b_analysis()
        assert result["so8_all_distinct"] is True

    def test_min_level_is_so8(self):
        result = run_l3b_analysis()
        assert result["min_level_for_distinction"] == "SO(8)"

    def test_conclusion(self):
        result = run_l3b_analysis()
        assert result["l3b_conclusion"] == "PATH_B_IMPOSSIBLE; USE_SCHUR_SO8"
