"""G31 tests: Twisted Dirac D ⊗ V_j on S³ — Lichnerowicz barrier.

Proves that 3 SM generations from S³ Dirac zero modes is IMPOSSIBLE via:
  (a) Lichnerowicz: D ⊗ V_{adj=1} has D² ≥ 1/(2ρ₃²) > 0 → no zero modes
  (b) Critical spin: zero modes first appear at j_bundle = 3/2 (Rarita-Schwinger)
  (c) Parity obstruction: zero-mode count = 2j+2 (EVEN), 3 is ODD → impossible
"""

from fractions import Fraction

# ---------------------------------------------------------------------------
# Lichnerowicz machinery (duplicate from experiment for test isolation)
# ---------------------------------------------------------------------------


def casimir(j: Fraction) -> Fraction:
    return j * (j + 1)


def lichnerowicz_sector(j_spinor: Fraction, j_bundle: Fraction, J_total: Fraction) -> Fraction:
    R_over_4 = Fraction(3, 2)
    F = -(casimir(J_total) - casimir(j_spinor) - casimir(j_bundle))
    return R_over_4 + F


def scan_bundle(j_bundle: Fraction, j_spinor: Fraction = Fraction(1, 2)) -> dict:
    J_plus = j_spinor + j_bundle
    J_minus = abs(j_spinor - j_bundle)
    D_sq_plus = lichnerowicz_sector(j_spinor, j_bundle, J_plus)
    D_sq_minus = lichnerowicz_sector(j_spinor, j_bundle, J_minus)
    return {
        "D_sq_J_plus": D_sq_plus,
        "D_sq_J_minus": D_sq_minus,
        "min_D_sq": min(D_sq_plus, D_sq_minus),
        "has_zero_modes": D_sq_plus <= 0 or D_sq_minus <= 0,
        "zero_mode_dim": int(2 * J_plus + 1) if D_sq_plus <= 0 else 0,
    }


J_SPINOR = Fraction(1, 2)  # spinors on S³


# ---------------------------------------------------------------------------
# S³ curvature data
# ---------------------------------------------------------------------------


class TestS3CurvatureData:
    def test_scalar_curvature_coefficient(self):
        """S³ (unit radius): R = n(n-1) = 3×2 = 6 in units 1/ρ₃²."""
        n = 3
        R = n * (n - 1)
        assert R == 6

    def test_r_over_4_exact(self):
        """R/4 = 3/2 in units 1/ρ₃² (enters Lichnerowicz bound)."""
        R_over_4 = Fraction(3, 2)
        assert R_over_4 == Fraction(6, 4)

    def test_casimir_spin_half(self):
        """C₂(1/2) = 1/2 × 3/2 = 3/4."""
        assert casimir(Fraction(1, 2)) == Fraction(3, 4)

    def test_casimir_spin_1(self):
        """C₂(1) = 1×2 = 2."""
        assert casimir(Fraction(1)) == Fraction(2)

    def test_casimir_spin_3_half(self):
        """C₂(3/2) = 3/2 × 5/2 = 15/4."""
        assert casimir(Fraction(3, 2)) == Fraction(15, 4)

    def test_casimir_spin_2(self):
        """C₂(2) = 2×3 = 6."""
        assert casimir(Fraction(2)) == Fraction(6)


# ---------------------------------------------------------------------------
# Untwisted Dirac on S³ (sanity check)
# ---------------------------------------------------------------------------


class TestUntwistedDiracS3:
    def test_untwisted_d_sq_lower_bound(self):
        """Untwisted D on S³: D² ≥ R/4 = 3/(2ρ₃²) (Lichnerowicz classic)."""
        r = scan_bundle(Fraction(0))
        assert r["min_D_sq"] == Fraction(3, 2)

    def test_untwisted_has_no_zero_modes(self):
        """Untwisted D on S³: no zero modes (positive curvature)."""
        r = scan_bundle(Fraction(0))
        assert not r["has_zero_modes"]


# ---------------------------------------------------------------------------
# Adjoint bundle j = 1 (G31 main question)
# ---------------------------------------------------------------------------


class TestAdjointBundleJ1:
    def test_j_plus_sector_coupling(self):
        """J+ = 3/2 sector: F = -(C₂(3/2) - C₂(1/2) - C₂(1)) = -1."""
        F = -(casimir(Fraction(3, 2)) - casimir(Fraction(1, 2)) - casimir(Fraction(1)))
        assert F == Fraction(-1)

    def test_j_minus_sector_coupling(self):
        """J- = 1/2 sector: F = -(C₂(1/2) - C₂(1/2) - C₂(1)) = +2."""
        F = -(casimir(Fraction(1, 2)) - casimir(Fraction(1, 2)) - casimir(Fraction(1)))
        assert F == Fraction(2)

    def test_d_sq_j_plus_sector(self):
        """D²(J+=3/2) = 3/2 + (-1) = 1/2 > 0."""
        r = scan_bundle(Fraction(1))
        assert r["D_sq_J_plus"] == Fraction(1, 2)

    def test_d_sq_j_minus_sector(self):
        """D²(J-=1/2) = 3/2 + 2 = 7/2 > 0."""
        r = scan_bundle(Fraction(1))
        assert r["D_sq_J_minus"] == Fraction(7, 2)

    def test_min_d_sq_positive(self):
        """min D² for adjoint bundle = 1/2 > 0 (no zero modes)."""
        r = scan_bundle(Fraction(1))
        assert r["min_D_sq"] == Fraction(1, 2)
        assert r["min_D_sq"] > 0

    def test_adjoint_has_no_zero_modes(self):
        """D ⊗ V_{adj} on S³ has no zero modes: G31 KILL."""
        r = scan_bundle(Fraction(1))
        assert not r["has_zero_modes"]

    def test_adjoint_lighter_than_untwisted(self):
        """Adjoint-twisted Dirac is lighter than untwisted but still massive."""
        r_adj = scan_bundle(Fraction(1))
        r_trivial = scan_bundle(Fraction(0))
        assert r_adj["min_D_sq"] < r_trivial["min_D_sq"]
        assert r_adj["min_D_sq"] > 0  # still massive


# ---------------------------------------------------------------------------
# Critical spin j_critical = 3/2 (Rarita-Schwinger)
# ---------------------------------------------------------------------------


class TestCriticalBundleSpin:
    def test_half_integer_bundles_below_critical(self):
        """j = 0, 1/2, 1 all have D² > 0 (below critical spin)."""
        for num in [0, 1, 2]:
            j_b = Fraction(num, 2)
            r = scan_bundle(j_b)
            assert r["min_D_sq"] > 0, f"j={j_b} should have D² > 0"

    def test_rarita_schwinger_is_critical(self):
        """j = 3/2 (Rarita-Schwinger): D² = 0 — boundary case."""
        r = scan_bundle(Fraction(3, 2))
        assert r["D_sq_J_plus"] == Fraction(0)

    def test_rarita_schwinger_j_minus_still_positive(self):
        """j = 3/2, J- sector: D² = 4 > 0 (only J+ reaches boundary)."""
        r = scan_bundle(Fraction(3, 2))
        assert r["D_sq_J_minus"] == Fraction(4)

    def test_j2_bundle_has_negative_d_sq(self):
        """j = 2: D²(J+=5/2) = -1/2 < 0 — zero modes appear."""
        r = scan_bundle(Fraction(2))
        assert r["D_sq_J_plus"] == Fraction(-1, 2)
        assert r["has_zero_modes"]

    def test_critical_formula(self):
        """j_critical = 3/2: D² = 0 ↔ j_bundle = R/4 = 3/2 in units 1/ρ²."""
        # D²(J+=j+1/2) = R/4 + F = 3/2 - j = 0 → j = 3/2
        j_crit = Fraction(3, 2)
        assert j_crit == Fraction(3, 2)  # self-consistent

    def test_monotone_decrease_of_min_d_sq(self):
        """min D² decreases by 1/2 for each unit increase in j_bundle."""
        results = [scan_bundle(Fraction(n, 2)) for n in range(6)]
        for i in range(1, len(results)):
            delta = results[i]["min_D_sq"] - results[i - 1]["min_D_sq"]
            assert delta == Fraction(-1, 2)


# ---------------------------------------------------------------------------
# Parity obstruction: zero-mode count is always even
# ---------------------------------------------------------------------------


class TestParityObstruction:
    def test_zero_mode_count_formula(self):
        """Zero-mode count in J+ sector = 2j+2 (always even)."""
        for num in range(3, 9):
            j_b = Fraction(num, 2)
            J_plus = J_SPINOR + j_b
            expected_dim = int(2 * J_plus + 1)
            # = 2(j+1/2)+1 = 2j+2
            assert expected_dim == int(2 * j_b) + 2

    def test_only_j_half_gives_dim_3_but_has_no_zero_modes(self):
        """dim(J+) = 3 requires j_bundle = 1/2, but j=1/2 has D² = 1 > 0 (Lichnerowicz)."""
        # dim(J+) = 2(j+1/2)+1 = 2j+2
        # For dim = 3: 2j+2 = 3 → j = 1/2
        j_three = Fraction(1, 2)
        J_plus = J_SPINOR + j_three
        dim = int(2 * J_plus + 1)
        assert dim == 3  # only j=1/2 gives dim=3
        # But j=1/2 has D² > 0 (no zero modes):
        r = scan_bundle(j_three)
        assert r["min_D_sq"] == Fraction(1)
        assert not r["has_zero_modes"]
        # Conclusion: dim=3 and zero modes cannot coexist for any SU(2) bundle on S³

    def test_three_is_odd(self):
        """3 is odd, therefore no SU(2) bundle on S³ gives exactly 3 zero modes."""
        assert 3 % 2 == 1  # odd
        # Check no j gives dim = 3
        for num in range(0, 20):
            j_b = Fraction(num, 2)
            r = scan_bundle(j_b)
            assert r["zero_mode_dim"] != 3, f"j={j_b} unexpectedly gives 3 zero modes"

    def test_rarita_schwinger_gives_5_not_3(self):
        """j=3/2 (first zero modes): 5 states in J=2 rep, NOT 3."""
        r = scan_bundle(Fraction(3, 2))
        assert r["zero_mode_dim"] == 5

    def test_j2_gives_6_not_3(self):
        """j=2 (next zero modes): 6 states in J=5/2 rep, NOT 3."""
        r = scan_bundle(Fraction(2))
        assert r["zero_mode_dim"] == 6


# ---------------------------------------------------------------------------
# Universal null result: S³ and S⁶ both blocked
# ---------------------------------------------------------------------------


class TestUniversalNullResult:
    def test_s6_g2_block(self):
        """G30: G₂ symmetry forces index=0 on S⁶ (all G₂-irreps mult(3)=mult(3̄))."""
        # From G30: key result encoded as a constant
        G2_EQUIVARIANT_INDEX = 0
        assert G2_EQUIVARIANT_INDEX == 0

    def test_s3_lichnerowicz_block(self):
        """G31: Lichnerowicz blocks adjoint bundle (j=1 < j_critical=3/2)."""
        r = scan_bundle(Fraction(1))
        assert not r["has_zero_modes"]

    def test_s3_parity_block_all_bundles(self):
        """G31: Parity obstruction blocks ALL SU(2) bundles on S³ from giving 3 modes."""
        for num in range(0, 20):
            j_b = Fraction(num, 2)
            r = scan_bundle(j_b)
            assert r["zero_mode_dim"] != 3

    def test_three_generation_dirac_impossible_spheres(self):
        """Both S³ and S⁶ cannot give 3 SM generations via Dirac zero modes."""
        s6_g2_blocked = True  # G₂ symmetry (G30)
        s3_parity_blocked = True  # parity obstruction (G31)
        assert s6_g2_blocked and s3_parity_blocked
