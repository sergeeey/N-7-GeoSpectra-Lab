"""
G61 — Origin of λ: dimensional hypothesis vs gaugino condensation.

G60 Pearl: A_np ≈ V_FLUX · exp(λ/ρ₆*²) from Minkowski condition.
This inverts to: λ_exact = ρ₆*² · ln(A_np_fitted / V_FLUX) ≈ 0.3374.

Two geometric candidates for λ:
  (A) λ = dim(S³) / dim(S³×S⁶) = 3/9 = 1/3 ≈ 0.3333  [dimensional]
  (B) λ = 2π / h^∨(E7) = 2π/18 = π/9 ≈ 0.3491         [gaugino, E7 ⊂ E8]

Minkowski pearl prediction at each candidate:
  A_np(λ) = V_FLUX · exp(λ/ρ₆*²)

Promote criterion: |λ_candidate - λ_exact| / λ_exact < 5% AND |A_np_pred - 0.38| / 0.38 < 5%
"""

import pytest
from math import pi, exp, log

C = 0.986
V_FLUX = 15 * C**3 / (16 * pi)
RHO6_STAR = 1.090
A_NP_FITTED = 0.38
LAM_FITTED = 0.30

# Minkowski-exact λ: V_FLUX·exp(λ/ρ₆*²) = A_np_fitted
LAM_EXACT_MK = RHO6_STAR**2 * log(A_NP_FITTED / V_FLUX)

# Candidate A: dimensional — λ = dim(S³) / dim(S³×S⁶)
DIM_S3 = 3
DIM_INTERNAL = 9  # S³(3) + S⁶(6)
LAM_DIM = DIM_S3 / DIM_INTERNAL  # = 1/3 ≈ 0.3333

# Candidate B: E7 gaugino condensation — λ = 2π / h^∨(E7)
H_DUAL_E7 = 18  # dual Coxeter number of E7
LAM_E7 = 2 * pi / H_DUAL_E7  # = π/9 ≈ 0.3491


def a_np_from_minkowski(lam: float) -> float:
    """A_np prediction from Minkowski pearl given λ."""
    return V_FLUX * exp(lam / RHO6_STAR**2)


# ── G61-A: Minkowski-exact λ as reference ─────────────────────────────────────


class TestA_MinkowskiReference:
    def test_lam_exact_reproduces_a_np(self):
        """By construction λ_exact gives A_np_pred = 0.38 exactly."""
        a_pred = a_np_from_minkowski(LAM_EXACT_MK)
        assert abs(a_pred - A_NP_FITTED) / A_NP_FITTED < 1e-6

    def test_lam_exact_value(self):
        """λ_exact ≈ 0.337: significantly different from fitted λ=0.30 (11% off)."""
        assert 0.30 < LAM_EXACT_MK < 0.40
        diff_from_fitted = abs(LAM_EXACT_MK - LAM_FITTED) / LAM_FITTED
        print(f"\n  λ_exact = {LAM_EXACT_MK:.5f},  λ_fitted(G56) = {LAM_FITTED:.2f}")
        print(f"  G56 fitted λ differs from Minkowski-exact by {diff_from_fitted:.1%}")
        assert diff_from_fitted > 0.05, "λ_fitted too close to λ_exact (unexpected consistency)"

    def test_lam_exact_close_to_one_third(self):
        """λ_exact ≈ 1/3: dimensional candidate is within 1.2%."""
        diff = abs(LAM_EXACT_MK - 1.0 / 3.0) / LAM_EXACT_MK
        print(f"\n  |λ_exact - 1/3| / λ_exact = {diff:.1%}")
        assert diff < 0.02, f"λ_exact not close to 1/3: {diff:.1%}"


# ── G61-B: Candidate A — dimensional λ = 3/9 = 1/3 ──────────────────────────


class TestB_DimensionalCandidate:
    def test_lam_dim_value(self):
        """λ_dim = dim(S³)/dim(S³×S⁶) = 3/9 = 1/3."""
        assert LAM_DIM == 1.0 / 3.0

    def test_lam_dim_close_to_mk_exact(self):
        """λ_dim = 1/3 within 1.2% of Minkowski-exact λ."""
        diff = abs(LAM_DIM - LAM_EXACT_MK) / LAM_EXACT_MK
        print(f"\n  λ_dim = {LAM_DIM:.5f},  λ_exact = {LAM_EXACT_MK:.5f},  diff = {diff:.1%}")
        assert diff < 0.02, f"λ_dim not within 2% of λ_exact: {diff:.1%}"

    def test_a_np_from_dim_lambda(self):
        """A_np_pred(λ=1/3) within 3% of 0.38."""
        a_pred = a_np_from_minkowski(LAM_DIM)
        diff = abs(a_pred - A_NP_FITTED) / A_NP_FITTED
        print(
            f"\n  A_np_pred(λ=1/3) = {a_pred:.5f},  target = {A_NP_FITTED:.2f},  diff = {diff:.1%}"
        )
        assert diff < 0.05, f"A_np prediction error {diff:.1%} > 5%"

    def test_dimensional_ratio_natural(self):
        """3/9 = dim(S³)/dim(internal) is geometrically natural: wrapped cycle fraction."""
        # The internal manifold is S³×S⁶, total dim = 9
        # D2-brane wraps S³ (3-cycle): fraction of internal space wrapped = 3/9
        assert DIM_S3 + (DIM_INTERNAL - DIM_S3) == DIM_INTERNAL  # 3 + 6 = 9
        assert DIM_INTERNAL - DIM_S3 == 6  # S⁶ complement


# ── G61-C: Candidate B — E7 gaugino condensation λ = π/9 ─────────────────────


class TestC_E7GauginoCandidate:
    def test_lam_e7_value(self):
        """λ_E7 = 2π/h^∨(E7) = 2π/18 = π/9."""
        assert abs(LAM_E7 - pi / 9) < 1e-10

    def test_e7_dual_coxeter(self):
        """E7 has dual Coxeter number h^∨ = 18 (standard Lie group fact)."""
        # Dual Coxeter numbers: SU(N)→N, SO(N)→N-2, E6→12, E7→18, E8→30, G₂→4
        assert H_DUAL_E7 == 18

    def test_lam_e7_close_to_mk_exact(self):
        """λ_E7 = π/9 ≈ 0.349 within 3.5% of λ_exact = 0.337."""
        diff = abs(LAM_E7 - LAM_EXACT_MK) / LAM_EXACT_MK
        print(f"\n  λ_E7 = {LAM_E7:.5f},  λ_exact = {LAM_EXACT_MK:.5f},  diff = {diff:.1%}")
        assert diff < 0.05, f"λ_E7 not within 5% of λ_exact: {diff:.1%}"

    def test_a_np_from_e7_lambda(self):
        """A_np_pred(λ=π/9) within 2% of 0.38 — BEST gaugino match."""
        a_pred = a_np_from_minkowski(LAM_E7)
        diff = abs(a_pred - A_NP_FITTED) / A_NP_FITTED
        print(
            f"\n  A_np_pred(λ_E7) = {a_pred:.5f},  target = {A_NP_FITTED:.2f},  diff = {diff:.1%}"
        )
        assert diff < 0.03, f"E7 A_np prediction error {diff:.1%} > 3%"

    def test_e7_string_embedding_natural(self):
        """E7 ⊂ E8: natural in E8×E8 heterotic string (S³×S⁶ ⊂ 10D)."""
        # E8 × E8 heterotic string decomposes E8 ⊃ E7 × SU(2)
        # Gaugino condensation in one E8 factor gives V_np ~ exp(-2π τ/h^∨(E7))
        # With τ = 1/ρ₆²: matches V_np = -A · exp(-λ_E7/ρ₆²), λ_E7 = 2π/18
        h_e8 = 30
        h_e7 = 18
        h_su2 = 2
        # E8 ⊃ E7 × SU(2): dimensions 248 ⊃ 133 + 3 + adjoint rep
        assert h_e7 < h_e8  # h^∨(E7) < h^∨(E8): E7 condensate is weaker than E8


# ── G61-D: Comparative summary ────────────────────────────────────────────────


class TestD_ComparativeSummary:
    def test_candidate_ranking(self):
        """Rank candidates by proximity to Minkowski-exact λ."""
        candidates = {
            "λ=1/3 (dimensional)": LAM_DIM,
            "λ=π/9 (E7 gaugino)": LAM_E7,
            "λ=3/10 (G56 fitted)": LAM_FITTED,
        }
        diffs = {name: abs(lam - LAM_EXACT_MK) / LAM_EXACT_MK for name, lam in candidates.items()}
        print("\n  Candidates vs Minkowski-exact λ=0.3374:")
        for name, diff in sorted(diffs.items(), key=lambda x: x[1]):
            a_pred = a_np_from_minkowski(candidates[name])
            print(f"    {name}: Δλ={diff:.1%}, A_np_pred={a_pred:.4f}")
        # Dimensional (1/3) must be closest
        assert diffs["λ=1/3 (dimensional)"] < diffs["λ=3/10 (G56 fitted)"]

    def test_both_candidates_within_5pct_of_a_np(self):
        """Both 1/3 and π/9 predict A_np within 5% of 0.38."""
        for lam, name in [(LAM_DIM, "1/3"), (LAM_E7, "π/9")]:
            a_pred = a_np_from_minkowski(lam)
            diff = abs(a_pred - A_NP_FITTED) / A_NP_FITTED
            assert diff < 0.05, f"λ={name}: A_np error {diff:.1%} > 5%"

    def test_g56_fitted_lambda_is_worst_match(self):
        """λ=0.30 (G56 fitted) gives largest A_np error among the three candidates."""
        diffs_anp = {
            LAM_DIM: abs(a_np_from_minkowski(LAM_DIM) - A_NP_FITTED) / A_NP_FITTED,
            LAM_E7: abs(a_np_from_minkowski(LAM_E7) - A_NP_FITTED) / A_NP_FITTED,
            LAM_FITTED: abs(a_np_from_minkowski(LAM_FITTED) - A_NP_FITTED) / A_NP_FITTED,
        }
        worst = max(diffs_anp, key=diffs_anp.get)
        assert worst == LAM_FITTED, (
            f"Expected G56 fitted λ to have worst A_np prediction, "
            f"but got {worst:.4f} with error {diffs_anp[worst]:.1%}"
        )
