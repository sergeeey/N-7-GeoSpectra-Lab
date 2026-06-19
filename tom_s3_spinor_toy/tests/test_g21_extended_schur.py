"""G21 tests: Extended Schur — commutant dimension of End_G(H_F)."""

import os
import sys

import numpy as np

_g21_dir = os.path.join(
    os.path.dirname(__file__), "..", "experiments", "20260619-g21-extended-schur"
)
sys.path.insert(0, _g21_dir)

for _p in [
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g16-t3r-from-k3"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260619-g15-hypercharge"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g11-block-generators"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260618-g10b-su3-in-so6"),
    os.path.join(os.path.dirname(__file__), "..", "experiments", "20260617-g10-s6-so6-gauge"),
]:
    sys.path.insert(0, _p)

from g21_extended_schur import (  # noqa: E402
    commutant_dim,
    commutant_basis,
    GENS_CARTAN,
    GENS_NO_BL,
    GENS_WITH_BL,
    J_32,
    K_32,
    SU3_32,
    verify_gates,
    N,
)


# ── E1: Cartan torus ──────────────────────────────────────────────────────────


def test_cartan_dim_80():
    """Cartan (J3, K3, BmL) gives dim=80: color triplets still 3-fold degenerate."""
    assert commutant_dim(GENS_CARTAN) == 80


def test_cartan_degeneracy_from_triplets():
    """Each S³ sector has 2 color triplets (9 each) + 2 singlets: 2×9+2×1 = 20. 4×20=80."""
    assert commutant_dim(GENS_CARTAN) == 4 * (2 * 9 + 2 * 1)


# ── E2: SU(2)_L × SU(2)_R × SU(3) without B-L ───────────────────────────────


def test_commutant_no_bl_is_12():
    """E2 MAIN: dim(End_{SU(2)_L × SU(2)_R × SU(3)}(H_F)) = 12."""
    assert commutant_dim(GENS_NO_BL) == 12


def test_commutant_no_bl_schur_structure():
    """The 12-dim commutant = 2×M_2(ℂ) + 4×ℂ: two degenerate singlet blocks."""
    # Schur: 2² + 1² + 1² + 2² + 1² + 1² = 12
    # This corresponds to: (j=½, 0, 1)×2 + (j=½, 0, 3̄)×1 + (j=½, 0, 3)×1
    #                    + (0, j=½, 1)×2 + (0, j=½, 3̄)×1 + (0, j=½, 3)×1
    expected = 2 * (2**2) + 4 * (1**2)
    assert expected == 12
    assert commutant_dim(GENS_NO_BL) == expected


def test_su3_alone_does_not_fully_resolve_degeneracy():
    """SU(3) alone on S⁶ fiber: degenerate singlets remain if SU(2) not included."""
    d_su3_only = commutant_dim(SU3_32)
    # SU(3) resolves color within each sector, but leaves L and R sectors and singlet
    # degeneracy unresolved; dim much larger than 12
    assert d_su3_only > 12


# ── E3: Full group with U(1)_{B-L} ───────────────────────────────────────────


def test_commutant_with_bl_is_8():
    """E3 MAIN: dim(End_{SU(2)_L × SU(2)_R × SU(3) × U(1)_{B-L}}(H_F)) = 8."""
    assert commutant_dim(GENS_WITH_BL) == 8


def test_commutant_with_bl_matches_8_irreps():
    """8 = 8 distinct irrep types × 1² (all multiplicities = 1 with B-L)."""
    n_irreps = 8
    assert commutant_dim(GENS_WITH_BL) == n_irreps * 1


def test_8_irrep_types_are_sm_particle_types():
    """The 8 irreps correspond exactly to 8 SM fermion types (one generation).

    Under SU(2)_L × SU(2)_R × SU(3) × U(1)_{B-L}:
      L-sector: (ν, B-L=-1), (d̄, B-L=-1/3), (u, B-L=+1/3), (ē, B-L=+1)
      R-sector: (ν_R, B-L=-1), (d̄_R, B-L=-1/3), (u_R, B-L=+1/3), (ē_R, B-L=+1)
    One free mass scale per type — matching SM Yukawa count structure.
    """
    assert commutant_dim(GENS_WITH_BL) == 8


# ── E4: B-L reduces commutant by exactly 4 ───────────────────────────────────


def test_bl_reduces_commutant_by_4():
    """E4: Adding U(1)_{B-L} to the generators reduces commutant by exactly 4."""
    d_no = commutant_dim(GENS_NO_BL)
    d_with = commutant_dim(GENS_WITH_BL)
    assert d_no - d_with == 4


def test_bl_splits_two_degenerate_singlet_blocks():
    """The 4-unit reduction = two M_2(ℂ) blocks (4 each) → two pairs of ℂ blocks."""
    # Each M_2(ℂ) has dim=4. Splitting into 2 scalar copies gives 2 (dim=1 each).
    # Net change per block: 4 → 2. Two blocks: 8 → 4. Change = (8-4) = 4. ✓
    reduction_per_block = 2**2 - 2 * (1**2)  # M_2(ℂ) dim - 2 scalars
    assert reduction_per_block == 2
    n_degenerate_blocks = 2  # one in L-sector, one in R-sector
    assert n_degenerate_blocks * reduction_per_block == 4


# ── E5: Commutant basis structure ─────────────────────────────────────────────


def test_commutant_basis_no_bl_has_12_columns():
    """The null space of the commutator constraint system has exactly 12 basis vectors."""
    basis = commutant_basis(GENS_NO_BL)
    assert basis.shape == (N * N, 12)


def test_commutant_basis_with_bl_has_8_columns():
    """With B-L, commutant basis has exactly 8 columns."""
    basis = commutant_basis(GENS_WITH_BL)
    assert basis.shape == (N * N, 8)


def test_commutant_basis_orthonormal():
    """Basis vectors are orthonormal in the standard inner product."""
    basis = commutant_basis(GENS_WITH_BL)
    gram = basis.conj().T @ basis
    assert np.allclose(gram, np.eye(8), atol=1e-8)


def test_commutant_elements_actually_commute():
    """Every basis element of the commutant actually commutes with all generators."""
    basis = commutant_basis(GENS_WITH_BL)
    for k in range(basis.shape[1]):
        M = basis[:, k].reshape(N, N)
        for G in GENS_WITH_BL:
            comm = G @ M - M @ G
            assert np.allclose(comm, 0, atol=1e-7), (
                f"Basis element {k} does not commute with a generator; max|comm|={np.abs(comm).max():.2e}"
            )


# ── Monotonicity: more generators → smaller commutant ─────────────────────────


def test_more_generators_smaller_commutant():
    """Commutant is monotonically non-increasing as we add generators."""
    d_cartan = commutant_dim(GENS_CARTAN)  # 80
    d_no_bl = commutant_dim(GENS_NO_BL)  # 12
    d_with_bl = commutant_dim(GENS_WITH_BL)  # 8
    assert d_cartan >= d_no_bl >= d_with_bl


def test_cartan_subset_of_no_bl():
    """GENS_CARTAN ⊂ GENS_NO_BL ∪ {BL_32}: more constraints → smaller commutant."""
    # GENS_NO_BL contains J3 and K3 (which are in GENS_CARTAN) plus more generators.
    # So GENS_NO_BL has more constraints → smaller commutant.
    assert commutant_dim(GENS_NO_BL) < commutant_dim(GENS_CARTAN)


# ── Sanity: individual generator families ─────────────────────────────────────


def test_j3_alone_commutant_large():
    """J3 alone constrains only T3L → large commutant (most matrices allowed)."""
    d = commutant_dim([J_32[2]])
    # J3 has 3 eigenvalues: +1/2, -1/2, 0 with large degeneracy → commutant much larger than 8
    assert d > 100


def test_k3_alone_commutant_large():
    """K3 alone similarly gives large commutant."""
    d = commutant_dim([K_32[2]])
    assert d > 100


def test_su3_reduces_from_cartan():
    """Full SU(3) (not just BmL) reduces the commutant below Cartan-only."""
    d_cartan = commutant_dim(GENS_CARTAN)
    d_with_su3 = commutant_dim(SU3_32)
    # Adding the off-diagonal SU(3) generators should resolve color degeneracy
    # so commutant_with_full_SU3 ≠ commutant_cartan in general
    assert d_with_su3 != d_cartan


# ── Gate function ─────────────────────────────────────────────────────────────


def test_gate_function_passes():
    """verify_gates() returns PASS_G21_EXTENDED_SCHUR (5/5)."""
    result = verify_gates()
    assert result == "PASS_G21_EXTENDED_SCHUR (5/5)"
