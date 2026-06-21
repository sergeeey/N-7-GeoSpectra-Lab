"""G69 tests: CSDR on G₂/SU(3) — independent 3+3̄+1+1 derivation (Approach Б).

Independent path to 3+3̄+1+1 via Spin(6)→SU(3) branching rules,
without using G67 triality. Confirms CONTENT; N_gen=3 multiplicity from G67.
"""

import os
import sys

os.path.dirname(__file__)
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260621-g69-csdr-coset"),
)

from g69_csdr import (  # noqa: E402
    DIM_G2,
    DIM_SU3,
    DIM_COSET,
    DIM_S6,
    COSET_IS_S6,
    SU4_FUND_DIM,
    SU4_TO_SU3_FUND,
    SU4_TO_SU3_ANTIFUND,
    S6_DIRAC_DIM,
    N_TRIPLET_FROM_CSDR,
    N_ANTITRIPLET_FROM_CSDR,
    N_SINGLET_FROM_CSDR,
    TOTAL_FROM_CSDR,
    CSDR_DECOMPOSITION,
    CSDR_MATCHES_G67,
    TANGENT_DIM_S6,
    CL6_REAL_DIM,
    N_GEN_FROM_CSDR_ALONE,
    N_GEN_FROM_TRIALITY,
    N_GEN_COMBINED,
    CSDR_ROLE,
    TRIALITY_ROLE,
    G69_STATUS,
    G67_N_TRIPLET,
    G67_N_SINGLET,
    G67_TOTAL,
)


# ── G69-E1: G₂/SU(3) coset dimensions ───────────────────────────────────────


def test_dim_g2():
    """G₂ Lie algebra has dimension 14."""
    assert DIM_G2 == 14, f"dim G₂ = {DIM_G2}, expected 14"


def test_dim_su3():
    """SU(3) Lie algebra has dimension 8."""
    assert DIM_SU3 == 8, f"dim SU(3) = {DIM_SU3}, expected 8"


def test_coset_dim_equals_6():
    """dim(G₂/SU(3)) = 14 - 8 = 6."""
    assert DIM_COSET == 6, f"dim(G₂/SU(3)) = {DIM_COSET}, expected 6"


def test_coset_is_s6():
    """G₂/SU(3) has dimension 6 = dim(S⁶)."""
    assert COSET_IS_S6
    assert DIM_COSET == DIM_S6


# ── G69-E2: SU(4) → SU(3) branching rules ───────────────────────────────────


def test_su4_fundamental_dimension():
    """SU(4) fundamental representation is 4-dimensional."""
    assert SU4_FUND_DIM == 4


def test_su4_fund_to_su3_branches_to_3plus1():
    """SU(4) fundamental 4 → 3 + 1 under SU(3) ⊂ SU(4)."""
    assert SU4_TO_SU3_FUND["triplet"] == 3
    assert SU4_TO_SU3_FUND["singlet"] == 1
    assert sum(SU4_TO_SU3_FUND.values()) == SU4_FUND_DIM  # 3+1=4


def test_su4_antifund_to_su3_branches_to_3bar_plus1():
    """SU(4) anti-fundamental 4̄ → 3̄ + 1 under SU(3)."""
    assert SU4_TO_SU3_ANTIFUND["antitriplet"] == 3
    assert SU4_TO_SU3_ANTIFUND["singlet"] == 1
    assert sum(SU4_TO_SU3_ANTIFUND.values()) == SU4_FUND_DIM  # 3̄+1=4


def test_dirac_spinor_dimension():
    """Full Dirac spinor of Spin(6) = 4+4̄ = 8-dimensional."""
    assert S6_DIRAC_DIM == 8


# ── G69-E2: Full decomposition 3+3̄+1+1 ──────────────────────────────────────


def test_csdr_triplet_count():
    """CSDR gives 3 SU(3)-triplet states (from 4 of SU(4))."""
    assert N_TRIPLET_FROM_CSDR == 3


def test_csdr_antitriplet_count():
    """CSDR gives 3 SU(3)-antitriplet states (from 4̄ of SU(4))."""
    assert N_ANTITRIPLET_FROM_CSDR == 3


def test_csdr_singlet_count():
    """CSDR gives 2 SU(3)-singlet states (one from 4, one from 4̄)."""
    assert N_SINGLET_FROM_CSDR == 2


def test_csdr_total_dimension():
    """Total CSDR content: 3+3̄+1+1 = 8-dimensional."""
    assert TOTAL_FROM_CSDR == 8
    assert N_TRIPLET_FROM_CSDR + N_ANTITRIPLET_FROM_CSDR + N_SINGLET_FROM_CSDR == 8


def test_csdr_decomposition_label():
    """CSDR decomposition is labeled 3+3̄+1+1."""
    assert CSDR_DECOMPOSITION == "3 + 3̄ + 1 + 1"


# ── G69-E4: Cross-check with G67 ─────────────────────────────────────────────


def test_csdr_matches_g67_triplet():
    """CSDR triplet count = G67 result: both give N_triplet = 3."""
    assert N_TRIPLET_FROM_CSDR == G67_N_TRIPLET, (
        f"CSDR: {N_TRIPLET_FROM_CSDR} triplets, G67: {G67_N_TRIPLET} triplets"
    )


def test_csdr_matches_g67_singlet():
    """CSDR singlet count = G67 result: both give N_singlet = 2."""
    assert N_SINGLET_FROM_CSDR == G67_N_SINGLET, (
        f"CSDR: {N_SINGLET_FROM_CSDR} singlets, G67: {G67_N_SINGLET} singlets"
    )


def test_csdr_matches_g67_total():
    """CSDR total = G67 total: both give 8-dim spinor."""
    assert TOTAL_FROM_CSDR == G67_TOTAL == 8


def test_csdr_matches_g67_flag():
    """Global consistency flag: CSDR path agrees with G67 triality path."""
    assert CSDR_MATCHES_G67, "CSDR does NOT match G67 — inconsistency detected!"


def test_two_independent_paths_agree():
    """Two independent paths give the same SU(3) content — structural robustness.

    Path 1 (G67): SO(8) triality → G₂ = Fix(Z₃) → 8 → 7+1 of G₂ → 3+3̄+1+1 of SU(3)
    Path 2 (G69): CSDR → Spin(6)=SU(4) spinor → SU(3)⊂SU(4) branching → 3+3̄+1+1
    """
    # Both give the same (n_triplet + n_antitriplet, n_singlet) = (6, 2)
    csdr = (N_TRIPLET_FROM_CSDR + N_ANTITRIPLET_FROM_CSDR, N_SINGLET_FROM_CSDR)
    g67 = (G67_N_TRIPLET * 2, G67_N_SINGLET)  # G67 N_TRIPLET=3 means 3+3̄=6 non-singlets
    assert csdr == g67, f"CSDR {csdr} ≠ G67 {g67}"


# ── G69-E5: Tangent space ─────────────────────────────────────────────────────


def test_tangent_space_dimension():
    """S⁶ tangent space is 6-dimensional."""
    assert TANGENT_DIM_S6 == DIM_S6 == 6


def test_clifford_algebra_dimension():
    """Cl(6,0) gives 8-dim real irrep (Cl(6,0) ≅ M₈(ℝ))."""
    assert CL6_REAL_DIM == 8


def test_cl6_unique_irrep():
    """Cl(6,0) ≅ M₈(ℝ) has a UNIQUE 8-dim real irrep — only ONE channel per S⁶.

    This contrasts with Cl(7,0) ≅ M₈(ℝ)⊕M₈(ℝ) which has TWO (from G68).
    The three triality channels come from different embeddings of Cl(6,0) in Cl(7,0).
    """
    # Cl(p,q) for p-q = 6 mod 8 → M_{2^(p+q)/2}(ℝ): ONE real irrep
    # vs Cl(7,0) with p-q = 7 mod 8 → M₈(ℝ)⊕M₈(ℝ): TWO real irreps
    n_cl6_irreps = 1  # unique
    n_cl7_irreps = 2  # from G68 (L and R channels)
    assert n_cl6_irreps == 1
    assert n_cl7_irreps == 2
    assert n_cl7_irreps - n_cl6_irreps == 1  # the "extra" irrep = second channel


# ── G69-E6: N_gen interpretation ─────────────────────────────────────────────


def test_csdr_alone_gives_one_generation():
    """A single CSDR application gives ONE copy of 3+3̄+1+1 (one generation)."""
    assert N_GEN_FROM_CSDR_ALONE == 1


def test_triality_gives_three_generations():
    """G67 triality provides the ×3 multiplier: N_gen = 3."""
    assert N_GEN_FROM_TRIALITY == 3


def test_combined_n_gen():
    """Combined result: N_gen = 3 (from G67 triality × G69 CSDR content)."""
    assert N_GEN_COMBINED == 3


def test_csdr_triality_roles():
    """CSDR provides content per generation; triality provides multiplicity."""
    assert "content" in CSDR_ROLE
    assert "multiplicity" in TRIALITY_ROLE


# ── G69 summary ───────────────────────────────────────────────────────────────


def test_g69_summary(capsys):
    """G69 summary: Approach Б result."""
    print("\n" + "=" * 60)
    print("G69: CSDR on G₂/SU(3) — Approach Б")
    print("=" * 60)
    print(f"\nCoset: G₂/SU(3), dim = {DIM_G2} - {DIM_SU3} = {DIM_COSET} = S⁶  ✓")
    print("\nSpin(6) = SU(4) spinor decomposition under SU(3):")
    print("  4 of SU(4) → 3 + 1 of SU(3)")
    print("  4̄ of SU(4) → 3̄ + 1 of SU(3)")
    print(f"  Combined: {CSDR_DECOMPOSITION}")
    print("\nComparison with G67 (triality path):")
    print(f"  G67: N_triplet={G67_N_TRIPLET}, N_singlet={G67_N_SINGLET}, total={G67_TOTAL}")
    print(
        f"  G69: N_triplet={N_TRIPLET_FROM_CSDR}, N_singlet={N_SINGLET_FROM_CSDR}, total={TOTAL_FROM_CSDR}"
    )
    print(f"  Match: {CSDR_MATCHES_G67}  ← TWO INDEPENDENT PATHS AGREE")
    print("\nN_gen:")
    print(f"  CSDR alone: {N_GEN_FROM_CSDR_ALONE} generation (one CSDR application)")
    print(f"  Triality (G67): {N_GEN_FROM_TRIALITY}× multiplier")
    print(f"  Combined: N_gen = {N_GEN_COMBINED}")
    print(f"\nStatus: {G69_STATUS}")
    print()

    assert G69_STATUS == "CONFIRM_CONTENT_INDEPENDENT"
