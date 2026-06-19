"""G8: tests for the chirality obstruction on S³×S⁶."""

import sympy as sp
import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__), "..", "experiments", "20260615-g8-chirality-obstruction"
    ),
)
from g8_chirality_obstruction import (
    poincare_sphere,
    poincare_product,
    betti_numbers,
    dirac_eigenvalues_s6,
    dirac_eigenvalues_s3,
    chirality_index,
    t,
)


# ── A. Cohomology ─────────────────────────────────────────────────────────────
def test_poincare_sphere():
    """Poincaré polynomial of Sⁿ = 1 + tⁿ."""
    assert poincare_sphere(3) == 1 + t**3
    assert poincare_sphere(6) == 1 + t**6


def test_poincare_product_s3xs6():
    """P(S³×S⁶) = (1+t³)(1+t⁶) = 1 + t³ + t⁶ + t⁹."""
    P = poincare_product(3, 6)
    assert sp.expand(P - (1 + t**3 + t**6 + t**9)) == 0


def test_betti_numbers_s3xs6():
    """Betti numbers: b₀=b₃=b₆=b₉=1, all others 0."""
    b = betti_numbers(poincare_product(3, 6))
    assert b[0] == 1
    assert b[3] == 1
    assert b[6] == 1
    assert b[9] == 1
    for k in (1, 2, 4, 5, 7, 8):
        assert b[k] == 0, f"b{k} should be 0, got {b[k]}"


def test_no_wilson_lines():
    """b₁ = 0 → no Wilson lines (Hosotani impossible on S³×S⁶)."""
    b = betti_numbers(poincare_product(3, 6))
    assert b[1] == 0


def test_no_abelian_flux():
    """b₂ = 0 → no abelian magnetic flux on S³×S⁶."""
    b = betti_numbers(poincare_product(3, 6))
    assert b[2] == 0


def test_s3xs1_has_wilson_line():
    """Contrast: S³×S¹ HAS b₁=1 → Wilson line possible (BG-H1 / Hosotani)."""
    b = betti_numbers(poincare_product(3, 1))
    assert b[1] == 1, "S³×S¹ must admit a Wilson line"


# ── B. Spectrum symmetry → index ──────────────────────────────────────────────
def test_s6_spectrum_symmetric():
    """S⁶ Dirac spectrum is ±-symmetric → index = 0, no zero modes."""
    idx, zero = chirality_index(dirac_eigenvalues_s6(n_max=5))
    assert idx == 0
    assert zero == 0


def test_s3_spectrum_symmetric():
    """S³ Dirac spectrum is ±-symmetric → index = 0, no zero modes."""
    idx, zero = chirality_index(dirac_eigenvalues_s3(m_max=5))
    assert idx == 0
    assert zero == 0


def test_s6_eigenvalues_paired():
    """Every positive S⁶ eigenvalue has a negative partner of equal magnitude."""
    vals = dirac_eigenvalues_s6(n_max=4)
    pos = sorted(v for v in vals if v > 0)
    neg = sorted((-v for v in vals if v < 0))
    assert pos == neg


def test_s6_lowest_eigenvalue_is_3():
    """Lowest |S⁶ eigenvalue| = 3 (n=0): ±3/ρ. Confirms no zero mode."""
    vals = [abs(v) for v in dirac_eigenvalues_s6(n_max=0)]
    assert min(vals) == 3


# ── G₂/SU(3) coset dimension (escape route sanity) ───────────────────────────
def test_g2_su3_coset_dimension():
    """dim(G₂/SU(3)) = 14 - 8 = 6 = dim S⁶ — coset structure is dimensionally consistent."""
    dim_g2 = 14
    dim_su3 = 8
    assert dim_g2 - dim_su3 == 6


def test_coset_su3_matches_color_dimension():
    """The coset SU(3) and SM SU(3)_color have the same dimension (8 generators)."""
    dim_su3_coset = 8
    dim_su3_color = 3**2 - 1
    assert dim_su3_coset == dim_su3_color
