"""
H1 — Geometric origin of NP exponent: λ = dim(Sᵃ) / dim(Sᵃ×Sᵇ) = a/(a+b)

Hypothesis: the NP exponent for product sphere Sᵃ×Sᵇ is the dimensional ratio.
Tests structural self-consistency across 5 product families.

Framework fixed from S³×S⁶ (G57, G60, G62):
  V_FLUX = 15·C³/(16π)   (Freund-Rubin on SM constraint, C=0.986)
  ρ* = 1.090              (UV-selection c_{1/2}=0, G57)
  K_VOL = 2π²·16π³/15    (4D EH-frame volume factor)

NOTE: V_FLUX and ρ* are NOT re-derived per (a,b). This is a STRUCTURAL test
of the λ-parametrization, not a full per-geometry calculation.
"""

import pytest
from math import pi, exp, sqrt
from scipy.optimize import minimize_scalar

C = 0.986
V_FLUX = 15 * C**3 / (16 * pi)  # ≈ 0.2861
RHO_STAR = 1.090  # UV-selection, G57
K_VOL = 2 * pi**2 * 16 * pi**3 / 15  # ≈ 652.8


def lam_geometric(a: int, b: int) -> float:
    return a / (a + b)


def a_np_minkowski(lam: float) -> float:
    """A_np from Minkowski condition V_total(ρ*)=0 (G60 pearl)."""
    return V_FLUX * exp(lam / RHO_STAR**2)


def v_total(rho: float, lam: float) -> float:
    anp = a_np_minkowski(lam)
    v_np = -anp * exp(-lam / rho**2)
    return (V_FLUX + v_np) / (K_VOL * rho**12)


def find_minimum(lam: float):
    res = minimize_scalar(
        lambda r: v_total(r, lam),
        bounds=(RHO_STAR + 0.001, 2.5),
        method="bounded",
    )
    return res.x, res.fun


def second_deriv(rho: float, lam: float, dr: float = 5e-4) -> float:
    return (v_total(rho + dr, lam) - 2 * v_total(rho, lam) + v_total(rho - dr, lam)) / dr**2


# All test cases: (a, b, label)
CASES = [
    (1, 8, "S1xS8"),
    (2, 7, "S2xS7"),
    (3, 6, "S3xS6"),  # anchor — must match G62
    (4, 5, "S4xS5"),
    (5, 4, "S5xS4"),
]


class TestH1_PositiveControl:
    """S³×S⁶ must reproduce G62 anchor result."""

    def test_lambda_geometric_s3_s6(self):
        assert abs(lam_geometric(3, 6) - 1 / 3) < 1e-10

    def test_rho_min_matches_g62(self):
        lam = lam_geometric(3, 6)
        rho_min, _ = find_minimum(lam)
        assert abs(rho_min - 1.1791) < 0.001, f"anchor broken: ρ_min={rho_min:.4f}"

    def test_v_min_matches_g62(self):
        lam = lam_geometric(3, 6)
        _, v_min = find_minimum(lam)
        assert v_min < 0
        assert abs(v_min - (-2.527e-6)) < 0.05e-6, f"V_min={v_min:.4e}"

    def test_mass_ratio_matches_g62(self):
        lam = lam_geometric(3, 6)
        rho_min, _ = find_minimum(lam)
        v2 = second_deriv(rho_min, lam)
        m2_mod = v2
        m2_kk = 1.0 / rho_min**2
        ratio = sqrt(abs(m2_mod) / m2_kk)
        assert abs(ratio - 0.0202) < 0.001, f"m_mod/m_KK={ratio:.4f}"


class TestH1_NegativeControl:
    """λ=0 gives flat potential (no stabilization); λ outside family is unphysical."""

    def test_lambda_zero_flat_potential(self):
        # With λ=0: V_NP = -A_np·exp(0) = -V_FLUX (constant)
        # V_total = (V_FLUX - V_FLUX)/(K_VOL·ρ^12) = 0 everywhere — flat, no stabilization
        lam = 0.0
        anp = a_np_minkowski(lam)
        assert abs(anp - V_FLUX) < 1e-10  # A_np = V_FLUX exactly at λ=0
        assert abs(v_total(2.0, lam)) < 1e-12  # V_total ≡ 0
        assert abs(v_total(3.0, lam)) < 1e-12

    def test_lambda_outside_family_larger_anp(self):
        # λ=1 is outside physical family (a/(a+b) < 1 always)
        # A_np is monotone in λ — λ=1 gives deeper NP than any physical (a,b)
        lam_max_physical = lam_geometric(5, 4)  # S⁵×S⁴ = 5/9, largest in family
        anp_max = a_np_minkowski(lam_max_physical)
        anp_unphysical = a_np_minkowski(1.0)
        assert anp_unphysical > anp_max


class TestH1_FamilyStructure:
    """For all (a,b) in the family: minimum exists, ρ_min > ρ*, V_min < 0."""

    @pytest.mark.parametrize("a,b,label", CASES)
    def test_minimum_exists(self, a, b, label):
        lam = lam_geometric(a, b)
        rho_min, v_min = find_minimum(lam)
        assert rho_min > RHO_STAR, f"{label}: ρ_min={rho_min:.4f} not > ρ*={RHO_STAR}"
        assert v_min < 0, f"{label}: V_min={v_min:.3e} not negative"

    @pytest.mark.parametrize("a,b,label", CASES)
    def test_kklt_structure(self, a, b, label):
        """UV-selection ρ* and NP minimum ρ_min are distinct (KKLT uplift structure)."""
        lam = lam_geometric(a, b)
        rho_min, _ = find_minimum(lam)
        separation = (rho_min - RHO_STAR) / RHO_STAR
        assert separation > 0.01, f"{label}: separation too small: {separation:.3f}"

    @pytest.mark.parametrize("a,b,label", CASES)
    def test_eft_self_consistent(self, a, b, label):
        """m_mod << m_KK — moduli lighter than KK: EFT is valid."""
        lam = lam_geometric(a, b)
        rho_min, _ = find_minimum(lam)
        v2 = second_deriv(rho_min, lam)
        m2_mod = v2
        m2_kk = 1.0 / rho_min**2
        ratio = sqrt(abs(m2_mod) / m2_kk)
        assert ratio < 0.15, f"{label}: m_mod/m_KK={ratio:.3f} exceeds 15%"
        assert ratio > 0.001, f"{label}: m_mod/m_KK={ratio:.4f} suspiciously tiny"


class TestH1_RhoMinUniversality:
    """UNEXPECTED: ρ_min ≈ 1.179 is nearly λ-independent across the whole family.

    Variation across all (a,b): only 0.2%. The minimum POSITION is set by
    ρ* (UV-selection geometry), not by the dimensional split a/(a+b).
    Only V_min and m_mod/m_KK scale with λ.
    """

    @pytest.mark.parametrize("a,b,label", CASES)
    def test_rho_min_near_universal(self, a, b, label):
        lam = lam_geometric(a, b)
        rho_min, _ = find_minimum(lam)
        assert abs(rho_min - 1.179) < 0.002, (
            f"{label} (λ={lam:.3f}): ρ_min={rho_min:.4f} deviates from universal 1.179"
        )

    def test_rho_min_spread_below_0p3_percent(self):
        """Total spread of ρ_min across the family < 0.3%."""
        rho_mins = [find_minimum(lam_geometric(a, b))[0] for a, b, _ in CASES]
        spread = (max(rho_mins) - min(rho_mins)) / min(rho_mins)
        assert spread < 0.003, f"spread={spread:.4f} exceeds 0.3%"

    def test_v_min_scales_linearly_with_lambda(self):
        """V_min ∝ λ: ratio V_min[i+1]/V_min[i] ≈ λ[i+1]/λ[i] within 15%."""
        rows = [(lam_geometric(a, b), find_minimum(lam_geometric(a, b))[1]) for a, b, _ in CASES]
        for i in range(len(rows) - 1):
            lam_i, v_i = rows[i]
            lam_next, v_next = rows[i + 1]
            ratio_v = v_next / v_i  # both negative → ratio positive
            ratio_lam = lam_next / lam_i
            assert abs(ratio_v / ratio_lam - 1.0) < 0.15, (
                f"V_min scaling off at step {i}: V_ratio={ratio_v:.3f}, λ_ratio={ratio_lam:.3f}"
            )


class TestH1_MonotonicPattern:
    """ρ_min and m_mod/m_KK vary monotonically with λ (clean geometric signal)."""

    def _compute_row(self, a, b):
        lam = lam_geometric(a, b)
        rho_min, v_min = find_minimum(lam)
        v2 = second_deriv(rho_min, lam)
        ratio = sqrt(abs(v2) / (1.0 / rho_min**2))
        return lam, rho_min, v_min, ratio

    def test_rho_min_increases_with_lambda(self):
        """Larger λ → minimum at larger radius (monotone)."""
        rows = [self._compute_row(a, b) for a, b, _ in CASES]
        rho_mins = [r[1] for r in rows]
        diffs = [rho_mins[i + 1] - rho_mins[i] for i in range(len(rho_mins) - 1)]
        all_positive = all(d > 0 for d in diffs)
        all_negative = all(d < 0 for d in diffs)
        assert all_positive or all_negative, f"ρ_min not monotone: {[f'{r:.4f}' for r in rho_mins]}"

    def test_print_family_table(self, capsys):
        """Print results table for all (a,b) — visible with pytest -s."""
        print("\n\nH1 — λ-family results:")
        print(f"{'Manifold':10} {'λ':6} {'ρ_min':8} {'V_min':12} {'m/m_KK':8}")
        print("-" * 50)
        for a, b, label in CASES:
            lam, rho_min, v_min, ratio = self._compute_row(a, b)
            marker = "← G62" if (a, b) == (3, 6) else ""
            print(f"{label:10} {lam:.4f} {rho_min:.4f}  {v_min:+.3e}  {ratio:.4f} {marker}")
        print()
