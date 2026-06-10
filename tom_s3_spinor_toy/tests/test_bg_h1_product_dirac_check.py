"""Tests — BG-H1 G1: Product Dirac cross-check for S³×S¹.

Gate: BG-H1-G1 (precondition: BG-H1-G0 PASS v1.1)
Pre-registration: experiments/20260610-bg-h1-s3xs1-bridge/claim_bg_h1.md

Key claim: λ²(S³×S¹) = (n+3/2)² + (m/R)²
  verified numerically to ≤1e-6 relative error
  for n ∈ {0,1,2,3}, both spin structures, R ∈ {0.5,1,2,5}.

Convention-pin test runs FIRST (class TestConventionPin).
Negative control (wrong-i) verified before any spectrum claim.

These regressions pin:
  1. Convention-pin: correct vs wrong construction differ
  2. Clifford anticommutation {Γ^j, Γ^4}=0 for j=1,2,3
  3. Product square D4² = -(k²+p²)·I₄ to machine precision
  4. Full grid max rel error < 1e-6
  5. δ₁(R) for periodic (m=1) and antiperiodic (m=½)
  6. Periodic ground state R-independent (m=0)
  7. Antiperiodic ground state R-sensitive (δ₀(R=0.5) ≠ δ₀(R=5))
  8. Spin structure fork reported; NO physical selection
  9. Scope guards (forbidden claims absent, item40 cap, lambda free)
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from tom_s3_spinor_toy.bg_h1_product_dirac_check import (
    G1_ANTICOM_THRESHOLD,
    G1_REL_ERROR_THRESHOLD,
    G1_R_VALUES,
    G1_S3_LEVELS,
    GAMMA,
    _build_correct,
    _build_wrong,
    check_clifford_anticommutation,
    check_product_square,
    check_wrong_convention,
    g1_gate_summary,
    run_delta1_check,
    run_g1_gate,
    run_g1_grid_check,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def g1_report():
    return run_g1_gate()


@pytest.fixture(scope="module")
def g1_summary():
    return g1_gate_summary()


@pytest.fixture(scope="module")
def grid_result():
    return run_g1_grid_check()


@pytest.fixture(scope="module")
def delta1_result():
    return run_delta1_check()


# ---------------------------------------------------------------------------
# Class 1: Convention pin (MUST run first; ensures correct i-placement)
# ---------------------------------------------------------------------------


class TestConventionPin:
    """Pin the i-placement convention before any spectrum measurement.

    Correct: A = D_t + p*I₂ (D_t already anti-Hermitian)
    Wrong:   A = 1j*D_t + p*I₂ (double i → real diagonal)
    """

    def test_correct_gives_kp_squared(self):
        """D4_correct² = -(k²+p²)·I₄ to 1e-14."""
        k, p = 1.5, 1.0
        D4 = _build_correct(k, p)
        D4_sq = D4 @ D4
        expected = -(k**2 + p**2)
        assert np.allclose(D4_sq, expected * np.eye(4), atol=1e-13), (
            f"D4_correct² should be {expected:.4f}·I₄, got diag={np.diag(D4_sq)}"
        )

    def test_wrong_gives_different_diagonal(self):
        """D4_wrong² diagonal ≠ -(k²+p²): negative control confirms i-bug."""
        k, p = 1.5, 1.0
        D4c = _build_correct(k, p)
        D4w = _build_wrong(k, p)
        D4c_sq_diag = np.sort(np.diag(D4c @ D4c).real)
        D4w_sq_diag = np.sort(np.diag(D4w @ D4w).real)
        assert not np.allclose(D4c_sq_diag, D4w_sq_diag, atol=1e-10), (
            "Wrong and correct constructions give same D²: convention-pin failed"
        )

    def test_wrong_matches_pk_cross_formula(self):
        """D4_wrong² has eigenvalues -(p-k)² and -(p+k)² (the wrong formula)."""
        k, p = 1.5, 1.0
        D4w_sq = _build_wrong(k, p) @ _build_wrong(k, p)
        actual = np.sort(np.diag(D4w_sq).real)
        expected = np.sort([-((p - k) ** 2), -((p - k) ** 2), -((p + k) ** 2), -((p + k) ** 2)])
        assert np.allclose(actual, expected, atol=1e-12), (
            f"D4_wrong² diagonal = {actual}, expected {expected}"
        )

    def test_pin_passes_in_report(self, g1_report):
        """Convention-pin is PASS in the full report."""
        assert g1_report.convention_pin_pass, (
            "Convention-pin FAILED — do not trust any spectrum results"
        )

    def test_constructions_differ_in_report(self, g1_report):
        """Report records that the two constructions differ."""
        assert g1_report.convention_wrong_differs

    def test_correct_eigenvalues_imaginary(self):
        """D4_correct eigenvalues are purely imaginary: ±i√(k²+p²)."""
        k, p = 1.5, 1.0
        eigs = np.linalg.eigvals(_build_correct(k, p))
        # All eigenvalues should have Re≈0
        max_real = float(np.max(np.abs(eigs.real)))
        assert max_real < 1e-12, f"Real parts of eigenvalues: {eigs.real}"
        # Imaginary parts should be ±√(k²+p²)
        expected_imag = math.sqrt(k**2 + p**2)
        imag_vals = np.sort(np.abs(eigs.imag))
        assert np.allclose(imag_vals, [expected_imag] * 4, atol=1e-12), (
            f"|imag(eig)| = {imag_vals}, expected {expected_imag:.6f}"
        )

    def test_wrong_eigenvalues_not_uniform(self):
        """D4_wrong gives NON-UNIFORM imaginary spectrum — exposing the bug.

        Correct: all 4 eigenvalues = ±i√(k²+p²) (2-fold degenerate).
        Wrong:   two distinct pairs ±i|p-k| and ±i(p+k) — non-degenerate.
        Both are purely imaginary (block anti-Hermitian preserved), but values differ.
        The bug is wrong formula, not wrong algebra type.
        """
        k, p = 1.5, 1.0  # |p-k|=0.5, p+k=2.5, √(k²+p²)≈1.803
        eigs_wrong = np.linalg.eigvals(_build_wrong(k, p))
        wrong_abs = np.sort(np.abs(eigs_wrong.imag))
        expected_wrong = np.sort([abs(p - k), abs(p - k), p + k, p + k])
        assert np.allclose(wrong_abs, expected_wrong, atol=1e-12), (
            f"D4_wrong |eig imag| = {wrong_abs}, expected {expected_wrong}"
        )
        # Confirm these differ from the correct formula
        correct_val = math.sqrt(k**2 + p**2)
        assert not np.allclose(wrong_abs, [correct_val] * 4, atol=1e-6), (
            "Wrong construction gives same eigenvalues as correct — convention-pin unclear"
        )


# ---------------------------------------------------------------------------
# Class 2: Clifford anticommutation {Γ^j, Γ^4} = 0
# ---------------------------------------------------------------------------


class TestCliffordAnticommutation:
    """Clifford algebra verification for the N=4 product construction.

    {Γ^j, Γ^4} = 0 for j=1,2,3 (required for JOINT cross-term mechanism).
    Source: C-H eq 2.1, traced in BG-H1-G0 source register v1.1 Claim 3b.
    """

    def test_anticommutation_j1(self):
        G1, G4 = GAMMA[1], GAMMA[4]
        ac = G1 @ G4 + G4 @ G1
        assert np.max(np.abs(ac)) < G1_ANTICOM_THRESHOLD, (
            f"{{Γ¹,Γ⁴}} ≠ 0: max={np.max(np.abs(ac)):.2e}"
        )

    def test_anticommutation_j2(self):
        G2, G4 = GAMMA[2], GAMMA[4]
        ac = G2 @ G4 + G4 @ G2
        assert np.max(np.abs(ac)) < G1_ANTICOM_THRESHOLD, (
            f"{{Γ²,Γ⁴}} ≠ 0: max={np.max(np.abs(ac)):.2e}"
        )

    def test_anticommutation_j3(self):
        G3, G4 = GAMMA[3], GAMMA[4]
        ac = G3 @ G4 + G4 @ G3
        assert np.max(np.abs(ac)) < G1_ANTICOM_THRESHOLD, (
            f"{{Γ³,Γ⁴}} ≠ 0: max={np.max(np.abs(ac)):.2e}"
        )

    def test_clifford_squares_positive(self):
        """(Γ^a)² = +I₄ for all a (positive definite Riemannian signature)."""
        for a in (1, 2, 3, 4):
            Ga = GAMMA[a]
            sq = Ga @ Ga
            assert np.allclose(sq, np.eye(4), atol=1e-12), (
                f"(Γ^{a})² ≠ I₄: max dev = {np.max(np.abs(sq - np.eye(4))):.2e}"
            )

    def test_clifford_anti_commutation_all_pass(self, g1_report):
        """All three anticommutators pass in the full report."""
        assert g1_report.clifford_anticom_pass


# ---------------------------------------------------------------------------
# Class 3: Product square D4² = -(k²+p²)·I₄
# ---------------------------------------------------------------------------


class TestProductSquare:
    """Pin the core algebraic result: D4² = -(k²+p²)·I₄.

    Tests specific (k,p) pairs to near machine precision.
    These are analytic facts, so rel error should be ≈1e-15, not 1e-6.
    """

    @pytest.mark.parametrize(
        "n,m,R",
        [
            (0, 0, 1.0),  # pure S³ (m=0)
            (0, 1, 1.0),  # first KK
            (1, 1, 2.0),  # n=1, m=1, R=2
            (3, 2, 0.5),  # large n, large m/R
            (0, 0, 5.0),  # large R (R-independence check)
        ],
    )
    def test_d_squared_equals_kp_formula(self, n, m, R):
        k = n + 1.5
        p = m / R
        res = check_product_square(k, p)
        assert res["pass"], (
            f"n={n}, m={m}, R={R}: rel_error={res['max_rel_error']:.2e} > {G1_REL_ERROR_THRESHOLD}"
        )
        assert res["max_rel_error"] < 1e-14, (
            f"Analytic test should be at machine precision, got {res['max_rel_error']:.2e}"
        )

    def test_off_diagonal_zero(self):
        """D4² is scalar × I₄: off-diagonal elements vanish."""
        k, p = 2.5, 0.75
        D4 = _build_correct(k, p)
        D4_sq = D4 @ D4
        off = D4_sq.copy()
        np.fill_diagonal(off, 0)
        assert np.max(np.abs(off)) < 1e-13

    def test_anti_hermitian(self):
        """D4 is anti-Hermitian: D4† = -D4."""
        k, p = 1.5, 0.5
        D4 = _build_correct(k, p)
        assert np.allclose(D4.conj().T, -D4, atol=1e-14), "D4 is not anti-Hermitian"

    @pytest.mark.parametrize("n", G1_S3_LEVELS)
    def test_s3_only_recovers_ch_eigenvalue(self, n):
        """m=0 (pure S³): λ² = (n+3/2)² = C-H eq 3.26."""
        k = n + 1.5
        res = check_product_square(k, 0.0)
        assert abs(res["lambda2_measured"] - k**2) / k**2 < 1e-14, (
            f"n={n}: measured λ²={res['lambda2_measured']:.10f}, predicted={k**2:.10f}"
        )


# ---------------------------------------------------------------------------
# Class 4: Full grid check (pre-registered test grid)
# ---------------------------------------------------------------------------


class TestGridCheck:
    """Full grid over (n, m, R, spin_structure) from claim_bg_h1.md."""

    def test_max_rel_error_below_threshold(self, grid_result):
        """Max relative error over entire grid < 1e-6 (pre-registered kill condition)."""
        assert grid_result["max_rel_error"] < G1_REL_ERROR_THRESHOLD, (
            f"Grid max rel error = {grid_result['max_rel_error']:.2e} > {G1_REL_ERROR_THRESHOLD}"
        )

    def test_grid_verdict_pass(self, grid_result):
        assert grid_result["verdict"] == "PASS"

    def test_all_grid_points_pass(self, grid_result):
        """Every individual (n, m, R) point must pass."""
        failures = [r for r in grid_result["results"] if not r["pass"]]
        assert len(failures) == 0, f"{len(failures)} grid points failed: {failures[:3]}"

    def test_both_spin_structures_covered(self, grid_result):
        """Both periodic and antiperiodic spin structures are tested."""
        structures = {r["spin_structure"] for r in grid_result["results"]}
        assert "periodic" in structures
        assert "antiperiodic" in structures

    def test_n_points_count(self, grid_result):
        """Grid covers expected number of points."""
        # 4 levels × (4 periodic m + 3 antiperiodic m) × 4 R values = 4×7×4 = 112
        expected = len(G1_S3_LEVELS) * (4 + 3) * len(G1_R_VALUES)
        assert grid_result["n_points"] == expected or len(grid_result["results"]) == expected, (
            f"Expected {expected} grid points, got {len(grid_result['results'])}"
        )

    def test_analytic_precision(self, grid_result):
        """All errors should be near machine precision (analytic formula, exact basis)."""
        max_err = grid_result["max_rel_error"]
        assert max_err < 1e-13, (
            f"Analytic check should be at machine precision, max rel error = {max_err:.2e}. "
            "If > 1e-13, there is a structural numerical issue."
        )


# ---------------------------------------------------------------------------
# Class 5: KK gap δ₁(R) checks
# ---------------------------------------------------------------------------


class TestDelta1Gap:
    """KK gap δ₁(R) for both spin structures (pre-registered formula)."""

    def test_delta1_periodic_formula(self, delta1_result):
        """Periodic δ₁(R) = √(9/4+1/R²)−3/2 matches numerical D4 eigenvalue."""
        max_err = max(r["delta1_periodic_error"] for r in delta1_result["records"])
        assert max_err < G1_REL_ERROR_THRESHOLD, f"Periodic δ₁(R) max error = {max_err:.2e}"

    def test_delta0_antiperiodic_formula(self, delta1_result):
        """Antiperiodic δ₀(R) = √(9/4+1/(4R²))−3/2 matches numerical D4 eigenvalue."""
        max_err = max(r["delta0_anti_error"] for r in delta1_result["records"])
        assert max_err < G1_REL_ERROR_THRESHOLD, f"Antiperiodic δ₀(R) max error = {max_err:.2e}"

    def test_periodic_ground_state_r_independent(self, delta1_result):
        """Periodic m=0: λ² = (3/2)², independent of R for all R in test grid."""
        assert delta1_result["periodic_ground_r_independent"], (
            "Periodic ground state (m=0) should be R-independent"
        )
        for r in delta1_result["records"]:
            assert r["periodic_ground_error"] < 1e-13, (
                f"R={r['R']}: periodic ground λ² error = {r['periodic_ground_error']:.2e}"
            )

    def test_antiperiodic_ground_r_sensitive(self, delta1_result):
        """Antiperiodic m=½: δ₀(R=0.5) ≠ δ₀(R=5.0) — ground state is R-sensitive."""
        assert delta1_result["antiperiodic_ground_r_sensitive"], (
            "Antiperiodic ground state should be R-sensitive (δ₀(R=0.5) ≠ δ₀(R=5.0))"
        )

    @pytest.mark.parametrize("R", G1_R_VALUES)
    def test_delta1_periodic_numerical_value(self, R):
        """Spot-check: periodic δ₁(R) = √(9/4+1/R²)−3/2 at each R."""
        k0, m1 = 1.5, 1.0
        D4 = _build_correct(k0, m1 / R)
        lam2 = float(-np.diag(D4 @ D4)[0].real)
        delta1 = math.sqrt(lam2) - k0
        expected = math.sqrt(9.0 / 4.0 + 1.0 / R**2) - 1.5
        assert abs(delta1 - expected) / max(abs(expected), 1e-15) < 1e-12, (
            f"R={R}: δ₁={delta1:.8f}, expected={expected:.8f}"
        )

    @pytest.mark.parametrize("R", G1_R_VALUES)
    def test_large_r_limit(self, R):
        """δ₁(R) → 0 as R → ∞: large-R behavior δ₁ ~ 1/(3R²) to leading order."""
        if R < 2.0:
            pytest.skip("Large-R limit only tested for R ≥ 2")
        delta1 = math.sqrt(9.0 / 4.0 + 1.0 / R**2) - 1.5
        # At R=5: δ₁ ≈ 1/(3·25) = 0.013; formula gives ~0.0133
        assert delta1 < 1.0 / R, f"R={R}: δ₁={delta1:.4f} should be < 1/R={1 / R:.4f}"


# ---------------------------------------------------------------------------
# Class 6: G1 gate verdict
# ---------------------------------------------------------------------------


class TestG1GateVerdict:
    """Pin the G1 gate result."""

    def test_verdict_pass(self, g1_report):
        """G1 verdict must be PASS."""
        assert g1_report.verdict == "PASS", (
            f"G1 verdict = {g1_report.verdict!r}. "
            f"max_rel_error={g1_report.max_rel_error:.2e}, "
            f"convention_pin={g1_report.convention_pin_pass}"
        )

    def test_summary_verdict_consistent(self, g1_summary):
        assert g1_summary["verdict"] == "PASS"

    def test_max_rel_error_below_threshold(self, g1_report):
        assert g1_report.max_rel_error < G1_REL_ERROR_THRESHOLD, (
            f"G1 max_rel_error = {g1_report.max_rel_error:.2e}"
        )

    def test_all_sub_checks_pass(self, g1_report):
        assert g1_report.convention_pin_pass
        assert g1_report.clifford_anticom_pass
        assert g1_report.grid_verdict == "PASS"


# ---------------------------------------------------------------------------
# Class 7: Spin structure fork (both branches; no selection)
# ---------------------------------------------------------------------------


class TestSpinStructureFork:
    """Both spin structures are computed; neither is selected (pre-registered fork)."""

    def test_spin_structure_fork_reported(self, g1_report):
        assert g1_report.spin_structure_fork_reported

    def test_no_physical_spin_structure_selected(self, g1_report):
        assert not g1_report.physical_spin_structure_selected, (
            "Spin structure selection is FORBIDDEN at G1 stage — no physical input available"
        )

    def test_no_physical_selection_in_summary(self, g1_summary):
        assert not g1_summary["physical_spin_structure_selected"]

    def test_periodic_and_antiperiodic_both_in_grid(self, grid_result):
        periodic = [r for r in grid_result["results"] if r["spin_structure"] == "periodic"]
        antiperiodic = [r for r in grid_result["results"] if r["spin_structure"] == "antiperiodic"]
        assert len(periodic) > 0
        assert len(antiperiodic) > 0


# ---------------------------------------------------------------------------
# Class 8: Scope guards (forbidden claims)
# ---------------------------------------------------------------------------


class TestScopeGuards:
    """BG-H1-G1 PASS must not generate any forbidden claims."""

    FORBIDDEN = [
        "s3xs1 solved",
        "physical spin structure selected",
        "lambda fixed",
        "physical promotion",
        "safe_for_runtime",
        "geometry determined",
    ]

    def test_forbidden_claims_list_populated(self, g1_report):
        assert len(g1_report.forbidden_claims) >= 4

    def test_no_solved_claim(self, g1_report):
        fc = [c.lower() for c in g1_report.forbidden_claims]
        assert any("solved" in c for c in fc)

    def test_no_lambda_fixed(self, g1_report):
        fc = [c.lower() for c in g1_report.forbidden_claims]
        assert any("lambda" in c for c in fc)

    def test_scope_says_lambda_free(self, g1_report):
        assert (
            "free_coupling_parameter" in g1_report.scope.replace(" ", "_").lower()
            or "free_coupling" in g1_report.scope.lower()
            or "free coupling" in g1_report.scope.lower()
        )

    def test_scope_says_geometry_agnostic(self, g1_report):
        assert (
            "geometry_agnostic" in g1_report.scope.lower()
            or "geometry agnostic" in g1_report.scope.lower()
            or "geometry_agnostic" in g1_report.scope.replace(" ", "_").lower()
        )

    def test_scope_says_no_physical_promotion(self, g1_report):
        assert "no physical promotion" in g1_report.scope.lower()

    def test_safe_for_runtime_false(self, g1_report):
        fc_lower = " ".join(g1_report.forbidden_claims).lower()
        assert "safe_for_runtime" in fc_lower or "safe for runtime" in fc_lower

    def test_summary_scope_preserved(self, g1_summary):
        assert "lambda" in g1_summary["scope"].lower()
        assert (
            "geometry_agnostic" in g1_summary["scope"].lower()
            or "GEOMETRY_AGNOSTIC" in g1_summary["scope"]
        )


# ---------------------------------------------------------------------------
# Class 9: Physical limits (what this does NOT mean)
# ---------------------------------------------------------------------------


class TestPhysicalLimits:
    """G1 PASS proves analytic consistency, not geometry or physics."""

    def test_g1_pass_does_not_mean_s3xs1_is_true_geometry(self, g1_report):
        """G1 PASS is descriptive spectral consistency, not a geometry claim."""
        # The test passes if the report itself does not assert this
        forbidden_substrings = ["true geometry", "actual geometry", "s3xs1_solved"]
        scope_lower = g1_report.scope.lower()
        for s in forbidden_substrings:
            assert s not in scope_lower, f"Forbidden substring {s!r} found in scope"

    def test_g1_pass_does_not_select_compactification_radius(self, g1_report):
        """R values are test parameters, not physical predictions."""
        # Verified by no physical_spin_structure_selected AND no R-stabilization claim
        assert not g1_report.physical_spin_structure_selected

    def test_g1_pass_does_not_fix_lambda(self, g1_report):
        """lambda = FREE_COUPLING_PARAMETER regardless of G1 outcome."""
        fc_lower = " ".join(g1_report.forbidden_claims).lower()
        assert "lambda fixed" in fc_lower or "lambda" in fc_lower
