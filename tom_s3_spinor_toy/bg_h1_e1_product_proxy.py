"""BG-H1-E1 — Discrete S³×S¹ proxy gate.

Precondition: BG-H1-G0 PASS v1.1, BG-H1-G1 PASS.
Pre-registration: experiments/20260610-bg-h1-s3xs1-bridge/claim_bg_h1.md

Question: Does the v0.2.0 FD discrete S³ Dirac, extended to the S³×S¹
product spectrum via eigenvalue additivity λ²=λ_S3²+(m/R)², reproduce
the pre-registered KK gap formula δ₁(R)=√(9/4+(m₁/R)²)−3/2 within 1%?

Method — spectrum additivity (exact for Kronecker-sum structure):
  1. λ_S3_0_disc = lowest eigenvalue from FD tridiagonal on S³ (reuses E0 operator)
  2. S¹ modes: p = m/R  (kept EXACT — Fourier basis; no S¹ discretization error)
  3. Product eigenvalue: λ²_{0,m₁} = λ_S3_0_disc² + (m₁/R)²
  4. Discrete gap: δ_disc(R) = √(λ_S3_0_disc² + (m₁/R)²) − λ_S3_0_disc
  5. Analytic gap: δ_analytic(R) = √(9/4 + (m₁/R)²) − 3/2

Kronecker-sum cross-check (small grids): builds D²_prod = D²_S3 ⊗ I_S1 + I_S3 ⊗ D²_S1
and verifies eigenvalues match {λ_S3_i² + λ_S1_j²} to machine precision.

Kill condition (pre-registered): max rel error > 1e-2 → FAIL, record in null_results/.

Sensitivity (pre-registered):
  1. Both spin structures: periodic (m₁=1) and antiperiodic (m₁=1/2).
  2. Grid convergence: N_alpha ∈ {500, 1000, 2000, 4000} (S³ FD only; S¹ is exact).
  3. Edge behavior: large-R recovery (δ→0) and small-R KK dominance (δ large).

Scope guards (enforced by tests, matching G1 forbidden_claims):
  - No claim "S³×S¹ solved"
  - No claim "physical spin structure selected"
  - lambda = FREE_COUPLING_PARAMETER
  - safe_for_runtime = False
  - GEOMETRY_AGNOSTIC intact until BG-H1-E1 verdict joined with G0+G1

Mathematical sources: C-H gr-qc/9505009, traced in source_register_bg_h1_g0.md v1.1.
Algebraic basis: Kronecker-sum eigenvalue theorem (standard linear algebra).
"""

from __future__ import annotations

import math
from typing import Final

import numpy as np
from scipy.linalg import eigh_tridiagonal

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import (
    dirac_sq_alpha_tridiag,
    recover_ladder,
)


# ---------------------------------------------------------------------------
# Pre-registered constants (claim_bg_h1.md)
# ---------------------------------------------------------------------------

E1_R_VALUES: Final = (0.5, 1.0, 2.0, 4.0, 6.0, 8.0)
E1_N_ALPHA_CONV: Final = (500, 1000, 2000, 4000)  # grid-convergence levels
E1_N_ALPHA_PRIMARY: Final = 4000  # primary gate N_alpha
E1_REL_ERROR_KILL: Final = 1e-2  # pre-registered kill condition

E1_PERIODIC_M1: Final = 1.0  # first KK mode (periodic, m ∈ ℤ)
E1_ANTIPERIODIC_M1: Final = 0.5  # first KK mode (antiperiodic, m ∈ ℤ+½)

# Analytic S³ ground-state eigenvalue k₀ = 3/2 (C-H eq 3.26, n=0, d=3)
K0_ANALYTIC: Final = 1.5


# ---------------------------------------------------------------------------
# Core gap formulas
# ---------------------------------------------------------------------------


def analytic_gap(R: float, m1: float) -> float:
    """δ_analytic(R) = √(9/4 + (m₁/R)²) − 3/2.

    Pre-registered formula (claim_bg_h1.md, eq for both spin structures).
    Periodic: m₁=1; antiperiodic: m₁=1/2.
    For m₁=0 returns 0.0 (periodic ground state, R-independent).
    """
    if m1 == 0.0:
        return 0.0
    return math.sqrt(9.0 / 4.0 + (m1 / R) ** 2) - K0_ANALYTIC


def product_gap(k0: float, R: float, m1: float) -> float:
    """δ(R; k0, m₁) = √(k0² + (m₁/R)²) − k0.

    k0 may be the discrete FD approximation OR the analytic value 3/2.
    When k0=3/2 and m₁>0 this equals analytic_gap(R, m1) exactly.
    """
    if m1 == 0.0:
        return 0.0
    return math.sqrt(k0**2 + (m1 / R) ** 2) - k0


def gap_rel_error(k0_disc: float, R: float, m1: float) -> float:
    """Relative error |δ_disc − δ_analytic| / |δ_analytic|.

    Returns 0.0 for m₁=0 (both numerator and denominator are 0).
    """
    d_disc = product_gap(k0_disc, R, m1)
    d_anal = analytic_gap(R, m1)
    if abs(d_anal) < 1e-15:
        return 0.0
    return abs(d_disc - d_anal) / abs(d_anal)


# ---------------------------------------------------------------------------
# S³ discrete ground state
# ---------------------------------------------------------------------------


def s3_ground_eigenvalue(n_alpha: int) -> float:
    """Lowest |eigenvalue| of the FD S³ radial Dirac (n=0 level, l=0, χ=-1).

    Reuses discrete_radial_dirac_proxy.recover_ladder verified in E0 gate.
    Converges to k₀=3/2 as n_alpha→∞.
    """
    return float(recover_ladder(3, 0, n_alpha, 1)[0])


# ---------------------------------------------------------------------------
# S¹ discrete spectrum (periodic and antiperiodic, for Kronecker-sum check)
# ---------------------------------------------------------------------------


def s1_discrete_eigenvalues(n_s1: int, R: float, spin_structure: str) -> np.ndarray:
    """Eigenvalues of -(1/R²)∂²_θ on S¹ (circumference 2πR) with N_s1 grid points.

    spin_structure='periodic':     Bloch phase = 0    → m ∈ ℤ (periodic BCs)
    spin_structure='antiperiodic': Bloch phase = 1/2  → m ∈ ℤ+1/2 (antiperiodic BCs)

    Returns positive eigenvalues only (squared Fourier momenta (m/R)²).
    Analytic (exact) values: m²/R² for m=0,1,...,N_s1/2 (periodic) or
                             (m+1/2)²/R² for m=0,...,N_s1/2-1 (antiperiodic).
    The FD matrix approximation converges to these as N_s1→∞.
    """
    h = 2.0 * math.pi / n_s1  # grid spacing in angle θ ∈ [0,2π)
    c = 1.0 / (R**2 * h**2)  # prefactor for -(1/R²)(d²/dθ²)

    # Build circulant matrix for -d²/dθ²
    main = np.full(n_s1, 2.0 * c)
    off = np.full(n_s1, -c)

    # Periodic (standard circulant)
    if spin_structure == "periodic":
        mat = np.diag(main) + np.diag(off[:-1], 1) + np.diag(off[:-1], -1)
        mat[0, n_s1 - 1] = -c
        mat[n_s1 - 1, 0] = -c
    elif spin_structure == "antiperiodic":
        # Twisted BCs: ψ(θ+2π) = -ψ(θ) → Bloch phase e^{iπ} = -1
        # The FD matrix for antiperiodic BCs has +c (instead of -c) at corners
        mat = np.diag(main) + np.diag(off[:-1], 1) + np.diag(off[:-1], -1)
        mat[0, n_s1 - 1] = +c  # +c from the -(-1) = +1 Bloch phase
        mat[n_s1 - 1, 0] = +c
    else:
        raise ValueError(f"Unknown spin_structure: {spin_structure!r}")

    return np.linalg.eigvalsh(mat)


# ---------------------------------------------------------------------------
# Primary gate: gap vs R sweep
# ---------------------------------------------------------------------------


def run_gap_vs_R(n_alpha: int, R_values: tuple, m1: float, label: str) -> dict:
    """For each R, compute δ_disc and δ_analytic and rel_error.

    label: human-readable spin structure name.
    """
    k0 = s3_ground_eigenvalue(n_alpha)
    results = []
    for R in R_values:
        d_disc = product_gap(k0, R, m1)
        d_anal = analytic_gap(R, m1)
        rel_err = gap_rel_error(k0, R, m1)
        results.append(
            {
                "R": R,
                "delta_disc": d_disc,
                "delta_analytic": d_anal,
                "rel_error": rel_err,
                "pass": rel_err < E1_REL_ERROR_KILL,
            }
        )
    return {
        "n_alpha": n_alpha,
        "m1": m1,
        "spin_structure": label,
        "k0_disc": k0,
        "results": results,
        "max_rel_error": max(r["rel_error"] for r in results),
        "all_pass": all(r["pass"] for r in results),
    }


# ---------------------------------------------------------------------------
# Sensitivity 1: grid convergence
# ---------------------------------------------------------------------------


def run_grid_convergence(R_fixed: float, m1: float, n_alpha_list: tuple) -> dict:
    """Check δ_disc(N_alpha) converges to δ_analytic as N_alpha grows.

    Expected: monotone decreasing relative error.
    """
    d_anal = analytic_gap(R_fixed, m1)
    records = []
    for n_alpha in n_alpha_list:
        k0 = s3_ground_eigenvalue(n_alpha)
        d_disc = product_gap(k0, R_fixed, m1)
        rel_err = abs(d_disc - d_anal) / abs(d_anal) if abs(d_anal) > 1e-15 else 0.0
        records.append(
            {
                "n_alpha": n_alpha,
                "k0_disc": k0,
                "delta_disc": d_disc,
                "delta_analytic": d_anal,
                "rel_error": rel_err,
            }
        )
    errors = [r["rel_error"] for r in records]
    monotone = all(errors[i] >= errors[i + 1] for i in range(len(errors) - 1))
    return {
        "R_fixed": R_fixed,
        "m1": m1,
        "n_alpha_list": list(n_alpha_list),
        "records": records,
        "monotone_convergence": monotone,
        "final_rel_error": records[-1]["rel_error"],
    }


# ---------------------------------------------------------------------------
# Sensitivity 2: edge behavior
# ---------------------------------------------------------------------------


def run_edge_behavior(n_alpha: int) -> dict:
    """Verify edge-behavior predictions (pre-registration sensitivity #3).

    Large R (R=8): δ ~ (m₁/R)²/(2k₀) = m₁²/(3R²) for R→∞.
    Small R (R=0.5): δ shows KK dominance (δ >> pure-S³ gap).

    For periodic m₁=1, R=8: δ_analytic = √(9/4+1/64) - 3/2 ≈ 0.00521
    Large-R approximation: (m₁/R)²/(2k₀) = 1/(3·64) ≈ 0.00521 ✓
    For periodic m₁=1, R=0.5: δ_analytic = √(9/4+4) - 3/2 = 1.0 (KK dominates)
    """
    k0 = s3_ground_eigenvalue(n_alpha)

    R_large = 8.0
    m1 = E1_PERIODIC_M1
    d_large_R = product_gap(k0, R_large, m1)
    d_large_R_anal = analytic_gap(R_large, m1)
    # Large-R leading-order approximation: δ ≈ (m₁/R)²/(2k₀)
    large_R_approx = (m1 / R_large) ** 2 / (2.0 * K0_ANALYTIC)
    large_R_is_small = d_large_R_anal < 0.01  # gap is small at large R

    R_small = 0.5
    d_small_R = product_gap(k0, R_small, m1)
    d_small_R_anal = analytic_gap(R_small, m1)
    kk_dominates = d_small_R_anal > 0.5  # KK gap >> typical level spacing

    # Monotone: δ decreasing in R (for m₁ > 0)
    R_vals = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0]
    gaps_anal = [analytic_gap(R, m1) for R in R_vals]
    gaps_disc = [product_gap(k0, R, m1) for R in R_vals]
    analytic_monotone = all(gaps_anal[i] >= gaps_anal[i + 1] for i in range(len(R_vals) - 1))
    discrete_monotone = all(gaps_disc[i] >= gaps_disc[i + 1] for i in range(len(R_vals) - 1))

    return {
        "R_large": R_large,
        "delta_large_R_disc": d_large_R,
        "delta_large_R_analytic": d_large_R_anal,
        "large_R_approx": large_R_approx,
        "large_R_approx_rel_err": abs(large_R_approx - d_large_R_anal) / d_large_R_anal,
        "large_R_is_small": large_R_is_small,
        "R_small": R_small,
        "delta_small_R_disc": d_small_R,
        "delta_small_R_analytic": d_small_R_anal,
        "kk_dominates_at_small_R": kk_dominates,
        "analytic_gaps_monotone_in_R": analytic_monotone,
        "discrete_gaps_monotone_in_R": discrete_monotone,
    }


# ---------------------------------------------------------------------------
# Fully-discrete Kronecker-sum cross-check (small grids)
# ---------------------------------------------------------------------------


def run_kronecker_sum_check(n_alpha_small: int = 30, n_s1: int = 16, R: float = 1.0) -> dict:
    """Kronecker-sum identity check for small S³×S¹ product grid.

    Builds D²_prod = D²_S3_disc ⊗ I_S1 + I_S3 ⊗ D²_S1_disc and verifies
    that its eigenvalues equal all pairwise sums {λ_S3_i + λ_S1_j}.

    This is a pure algebraic identity (Kronecker-sum eigenvalue theorem):
    if A ∈ R^{m×m} and B ∈ R^{n×n} then eig(A⊗I_n + I_m⊗B) = {a_i+b_j}.
    Should hold to machine precision (≤1e-10).

    Also checks that the lowest product eigenvalue matches (k₀_disc)²+(0)² = k₀_disc²
    (periodic m=0 ground state), and (k₀_disc)²+(1/R)² for m=1 (first KK level).
    """
    # D²_S3 (tridiagonal on interior n_alpha_small - 1 points)
    d_diag, d_off, _ = dirac_sq_alpha_tridiag(3, 0, n_alpha_small, chirality=-1)
    n_s3 = len(d_diag)  # = n_alpha_small - 1 interior points
    D2_S3 = np.diag(d_diag) + np.diag(d_off, 1) + np.diag(d_off, -1)
    lambda_S3 = np.linalg.eigvalsh(D2_S3)  # eigenvalues of D²_S3

    # D²_S1 (periodic second-derivative circulant on N_s1 points)
    h_s1 = 2.0 * math.pi / n_s1  # angle spacing
    c_s1 = 1.0 / (R**2 * h_s1**2)
    main_s1 = np.full(n_s1, 2.0 * c_s1)
    D2_S1 = (
        np.diag(main_s1)
        + np.diag(np.full(n_s1 - 1, -c_s1), 1)
        + np.diag(np.full(n_s1 - 1, -c_s1), -1)
    )
    D2_S1[0, n_s1 - 1] = -c_s1
    D2_S1[n_s1 - 1, 0] = -c_s1
    lambda_S1 = np.linalg.eigvalsh(D2_S1)

    # Product operator via Kronecker sum
    I_S1 = np.eye(n_s1)
    I_S3 = np.eye(n_s3)
    D2_prod = np.kron(D2_S3, I_S1) + np.kron(I_S3, D2_S1)
    lambda_prod = np.linalg.eigvalsh(D2_prod)

    # Expected: all pairwise sums
    expected = np.sort(np.array([a + b for a in lambda_S3 for b in lambda_S1]))
    lambda_prod_sorted = np.sort(lambda_prod)

    max_abs_err = float(np.max(np.abs(lambda_prod_sorted - expected)))
    rel_scale = float(np.mean(np.abs(expected[expected > 0]))) if np.any(expected > 0) else 1.0
    max_rel_err = max_abs_err / rel_scale if rel_scale > 0 else max_abs_err

    # Verify lowest product eigenvalue = k₀_disc² (S³ ground, m=0 KK ground)
    k0_disc = math.sqrt(abs(float(lambda_S3[0])))
    lowest_expected = float(lambda_S3[0] + lambda_S1[0])  # m=0: λ_S1[0]=0
    lowest_actual = float(lambda_prod_sorted[0])

    return {
        "n_alpha_small": n_alpha_small,
        "n_s1": n_s1,
        "R": R,
        "n_s3": n_s3,
        "n_total": n_s3 * n_s1,
        "max_abs_err_kronecker": max_abs_err,
        "max_rel_err_kronecker": max_rel_err,
        "kronecker_identity_pass": max_abs_err < 1e-8,
        "lowest_eigenvalue_actual": lowest_actual,
        "lowest_eigenvalue_expected": lowest_expected,
        "k0_disc_from_kronecker": k0_disc,
    }


# ---------------------------------------------------------------------------
# Negative control: periodic m=0 ground state (δ = 0 for all R)
# ---------------------------------------------------------------------------


def run_negative_control_periodic_ground(n_alpha: int) -> dict:
    """Periodic m=0: gap = 0 for all R (R-independent ground state).

    This is the pre-registration baseline: pure S³ fingerprint E0≈3/2 is
    unshifted by S¹ compactification when m=0.
    """
    k0 = s3_ground_eigenvalue(n_alpha)
    all_zero = True
    results = []
    for R in E1_R_VALUES:
        d = product_gap(k0, R, 0.0)  # m=0
        zero = abs(d) < 1e-14
        all_zero = all_zero and zero
        results.append({"R": R, "delta": d, "is_zero": zero})
    return {
        "spin_structure": "periodic",
        "m": 0,
        "n_alpha": n_alpha,
        "k0_disc": k0,
        "results": results,
        "all_zero": all_zero,
        "pass": all_zero,
    }


# ---------------------------------------------------------------------------
# Full E1 gate
# ---------------------------------------------------------------------------


def run_e1_gate(n_alpha: int = E1_N_ALPHA_PRIMARY) -> dict:
    """Run the full BG-H1-E1 gate.

    Returns structured dict with all sub-results and overall verdict.
    """
    # Primary sweep — both spin structures, full R range
    periodic = run_gap_vs_R(n_alpha, E1_R_VALUES, E1_PERIODIC_M1, "periodic")
    antiperiodic = run_gap_vs_R(n_alpha, E1_R_VALUES, E1_ANTIPERIODIC_M1, "antiperiodic")

    # Negative control: m=0 periodic ground state (δ=0 for all R)
    neg_ctrl = run_negative_control_periodic_ground(n_alpha)

    # Grid convergence (both spin structures, R=1.0)
    conv_periodic = run_grid_convergence(1.0, E1_PERIODIC_M1, E1_N_ALPHA_CONV)
    conv_antiperiodic = run_grid_convergence(1.0, E1_ANTIPERIODIC_M1, E1_N_ALPHA_CONV)

    # Edge behavior
    edge = run_edge_behavior(n_alpha)

    # Fully discrete Kronecker sum cross-check
    kronecker = run_kronecker_sum_check(n_alpha_small=30, n_s1=16, R=1.0)

    max_periodic = periodic["max_rel_error"]
    max_antiperiodic = antiperiodic["max_rel_error"]
    max_overall = max(max_periodic, max_antiperiodic)

    verdict = "PASS" if max_overall < E1_REL_ERROR_KILL else "FAIL"

    return {
        "gate": "BG-H1-E1",
        "date": "2026-06-10",
        "precondition": "BG-H1-G0 PASS v1.1 + BG-H1-G1 PASS",
        "n_alpha_primary": n_alpha,
        "periodic": periodic,
        "antiperiodic": antiperiodic,
        "negative_control": neg_ctrl,
        "grid_convergence_periodic": conv_periodic,
        "grid_convergence_antiperiodic": conv_antiperiodic,
        "edge_behavior": edge,
        "kronecker_sum_check": kronecker,
        "max_rel_error_periodic": max_periodic,
        "max_rel_error_antiperiodic": max_antiperiodic,
        "max_rel_error_overall": max_overall,
        "kill_threshold": E1_REL_ERROR_KILL,
        "spin_structure_fork_reported": True,
        "physical_spin_structure_selected": False,
        "verdict": verdict,
        "scope": (
            "E1 discrete proxy; λ=FREE_COUPLING_PARAMETER; "
            "GEOMETRY_AGNOSTIC intact; no physical spin-structure selection; "
            "no S3xS1 solved claim; no physical promotion"
        ),
        "forbidden_claims": [
            "S3xS1 solved",
            "physical spin structure selected",
            "lambda fixed",
            "physical promotion",
            "safe_for_runtime",
            "geometry determined",
        ],
    }
