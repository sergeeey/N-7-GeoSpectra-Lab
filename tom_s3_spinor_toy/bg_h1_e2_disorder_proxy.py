"""BG-H1-E2 — Disorder robustness gate for S³×S¹ product KK gap.

Tests whether δ₁(R) = √(k₀_disc² + (m₁/R)²) − k₀_disc survives diagonal
disorder W=0.5 on the S³ FD sector. S¹ modes are kept exact (not disordered).

Pre-registered kill condition (claim_bg_h1.md):
  Fingerprint on product MORE fragile than on pure S³ alone → FAIL.
  Operationalized as:
    (a) max_R fragility_ratio > E2_FRAGILITY_RATIO_KILL (product/S3 relative fragility)
    (b) mean_rel_error > E2_REL_MEAN_ERROR_KILL at any R vs analytic baseline
    (c) mean δ(R) not monotone decreasing in R

Disorder model (same as KT-3):
  diag_disordered = diag + W × ξ,  ξ ~ Uniform(−1, 1), independent per grid point.
  S¹ modes: EXACT (Fourier basis), no S¹ disorder.

Hard constraints (inherited from claim_bg_h1.md):
  - lambda = FREE_COUPLING_PARAMETER
  - safe_for_runtime = False
  - No physical spin structure selection
  - No S³×S¹ geometry claim (GEOMETRY_AGNOSTIC intact)
"""

from __future__ import annotations

import math
from typing import Final

import numpy as np
from scipy.linalg import eigh_tridiagonal

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import dirac_sq_alpha_tridiag

# ---------------------------------------------------------------------------
# Pre-registered constants (frozen — do not modify between pre-registration and run)
# ---------------------------------------------------------------------------

E2_W_DISORDER: Final = 0.5
E2_N_SEEDS: Final = 30
E2_N_ALPHA: Final = 1000
E2_R_VALUES: Final = (0.5, 1.0, 2.0, 4.0, 6.0, 8.0)
E2_REL_MEAN_ERROR_KILL: Final = 0.05  # 5% mean relative error vs analytic baseline
E2_FRAGILITY_RATIO_KILL: Final = 10.0  # product not >10× more fragile than S³ alone
E2_PERIODIC_M1: Final = 1.0
E2_ANTIPERIODIC_M1: Final = 0.5
K0_ANALYTIC: Final = 1.5  # exact S³ ground state


# ---------------------------------------------------------------------------
# Core formulas (identical to E1 — do not alter)
# ---------------------------------------------------------------------------


def analytic_gap(R: float, m1: float) -> float:
    """δ_analytic(R) = √(9/4 + (m₁/R)²) − 3/2."""
    if m1 == 0.0:
        return 0.0
    return math.sqrt(9.0 / 4.0 + (m1 / R) ** 2) - K0_ANALYTIC


def product_gap(k0: float, R: float, m1: float) -> float:
    """Product gap δ = √(k₀² + (m₁/R)²) − k₀ for given k₀."""
    if m1 == 0.0:
        return 0.0
    return math.sqrt(k0**2 + (m1 / R) ** 2) - k0


# ---------------------------------------------------------------------------
# S³ disorder model (replicates KT-3 exactly)
# ---------------------------------------------------------------------------


def s3_clean_ground(n_alpha: int) -> float:
    """S³ ground eigenvalue k₀ = |λ_min| without disorder (W=0 baseline)."""
    diag, off, _ = dirac_sq_alpha_tridiag(3, 0, n_alpha, chirality=-1)
    val = eigh_tridiagonal(diag, off, select="i", select_range=(0, 0), eigvals_only=True)
    return float(np.sqrt(abs(val[0])))


def s3_disordered_ground(n_alpha: int, W: float, seed: int) -> float:
    """Lowest |λ| of S³ FD operator with diagonal disorder W·ξ, ξ ~ Uniform(−1, 1)."""
    diag, off, _ = dirac_sq_alpha_tridiag(3, 0, n_alpha, chirality=-1)
    rng = np.random.default_rng(seed)
    xi = rng.uniform(-1.0, 1.0, size=len(diag))
    diag_d = diag + W * xi
    val = eigh_tridiagonal(diag_d, off, select="i", select_range=(0, 0), eigvals_only=True)
    return float(np.sqrt(abs(val[0])))


# ---------------------------------------------------------------------------
# Disorder sweep
# ---------------------------------------------------------------------------


def run_disorder_sweep(
    n_alpha: int = E2_N_ALPHA,
    W: float = E2_W_DISORDER,
    n_seeds: int = E2_N_SEEDS,
    R_values: tuple = E2_R_VALUES,
    m1_periodic: float = E2_PERIODIC_M1,
    m1_antiperiodic: float = E2_ANTIPERIODIC_M1,
) -> dict:
    """Run disorder sweep and collect per-seed k₀ and δ(R) statistics.

    Returns a dict containing:
      - k₀ baseline (clean, no disorder)
      - per-seed k₀ samples and their statistics
      - per-R δ(R) statistics for both spin structures
      - fragility ratios: product_fragility / s3_fragility
    """
    k0_base = s3_clean_ground(n_alpha)

    k0_samples: list[float] = []
    # delta[struct][seed][R_idx]
    delta_by_struct: dict[str, list[list[float]]] = {
        "periodic": [],
        "antiperiodic": [],
    }

    for seed in range(n_seeds):
        k0_s = s3_disordered_ground(n_alpha, W, seed)
        k0_samples.append(k0_s)
        delta_by_struct["periodic"].append([product_gap(k0_s, R, m1_periodic) for R in R_values])
        delta_by_struct["antiperiodic"].append(
            [product_gap(k0_s, R, m1_antiperiodic) for R in R_values]
        )

    k0_arr = np.array(k0_samples)
    k0_shifts = np.abs(k0_arr - k0_base)
    s3_mean_rel_frag = float(np.mean(k0_shifts) / k0_base)
    s3_max_rel_frag = float(np.max(k0_shifts) / k0_base)

    def _r_stats(struct: str, m1: float) -> list[dict]:
        arr = np.array(delta_by_struct[struct])  # (n_seeds, n_R)
        base_deltas = np.array([product_gap(k0_base, R, m1) for R in R_values])
        stats_list = []
        for ri, R in enumerate(R_values):
            d_samp = arr[:, ri]
            d_base = base_deltas[ri]
            d_anal = analytic_gap(R, m1)
            mean_d = float(np.mean(d_samp))
            std_d = float(np.std(d_samp))
            # mean relative error vs analytic (tests systematic shift)
            mean_rel_err_vs_analytic = float(abs(mean_d - d_anal) / max(abs(d_anal), 1e-15))
            # fragility: mean|Δδ|/δ_base, where Δδ = δ_disordered − δ_clean
            mean_abs_shift = float(np.mean(np.abs(d_samp - d_base)))
            product_mean_rel_frag = float(mean_abs_shift / max(abs(d_base), 1e-15))
            fragility_ratio = product_mean_rel_frag / max(s3_mean_rel_frag, 1e-15)
            stats_list.append(
                {
                    "R": R,
                    "d_analytic": d_anal,
                    "d_baseline_disc": float(d_base),
                    "mean": mean_d,
                    "std": std_d,
                    "mean_rel_error_vs_analytic": mean_rel_err_vs_analytic,
                    "product_mean_rel_fragility": product_mean_rel_frag,
                    "fragility_ratio": fragility_ratio,
                }
            )
        return stats_list

    periodic_stats = _r_stats("periodic", m1_periodic)
    antiperiodic_stats = _r_stats("antiperiodic", m1_antiperiodic)

    # Monotonicity: mean(δ(R)) must be decreasing in R
    def _monotone_decreasing(stats: list[dict]) -> bool:
        means = [s["mean"] for s in stats]
        return all(means[i] >= means[i + 1] for i in range(len(means) - 1))

    return {
        "W": W,
        "n_alpha": n_alpha,
        "n_seeds": n_seeds,
        "R_values": list(R_values),
        "k0_baseline": k0_base,
        "k0_mean": float(np.mean(k0_arr)),
        "k0_std": float(np.std(k0_arr)),
        "s3_mean_rel_fragility": s3_mean_rel_frag,
        "s3_max_rel_fragility": s3_max_rel_frag,
        "periodic": {
            "m1": m1_periodic,
            "r_stats": periodic_stats,
            "monotone_decreasing": _monotone_decreasing(periodic_stats),
        },
        "antiperiodic": {
            "m1": m1_antiperiodic,
            "r_stats": antiperiodic_stats,
            "monotone_decreasing": _monotone_decreasing(antiperiodic_stats),
        },
    }


# ---------------------------------------------------------------------------
# Gate verdict
# ---------------------------------------------------------------------------


def e2_verdict(sweep: dict) -> dict:
    """Apply pre-registered kill conditions and return verdict dict."""
    failures: list[str] = []

    # Kill (c): monotonicity
    if not sweep["periodic"]["monotone_decreasing"]:
        failures.append("periodic_mean_delta_not_monotone_decreasing")
    if not sweep["antiperiodic"]["monotone_decreasing"]:
        failures.append("antiperiodic_mean_delta_not_monotone_decreasing")

    # Kill (b): mean relative error vs analytic
    max_err_p = max(s["mean_rel_error_vs_analytic"] for s in sweep["periodic"]["r_stats"])
    max_err_a = max(s["mean_rel_error_vs_analytic"] for s in sweep["antiperiodic"]["r_stats"])
    if max_err_p > E2_REL_MEAN_ERROR_KILL:
        failures.append(
            f"periodic_max_mean_rel_error={max_err_p:.3e} > kill={E2_REL_MEAN_ERROR_KILL}"
        )
    if max_err_a > E2_REL_MEAN_ERROR_KILL:
        failures.append(
            f"antiperiodic_max_mean_rel_error={max_err_a:.3e} > kill={E2_REL_MEAN_ERROR_KILL}"
        )

    # Kill (a): fragility ratio — core differential kill
    max_frag_p = max(s["fragility_ratio"] for s in sweep["periodic"]["r_stats"])
    max_frag_a = max(s["fragility_ratio"] for s in sweep["antiperiodic"]["r_stats"])
    if max_frag_p > E2_FRAGILITY_RATIO_KILL:
        failures.append(
            f"periodic_fragility_ratio={max_frag_p:.2f} > kill={E2_FRAGILITY_RATIO_KILL}"
        )
    if max_frag_a > E2_FRAGILITY_RATIO_KILL:
        failures.append(
            f"antiperiodic_fragility_ratio={max_frag_a:.2f} > kill={E2_FRAGILITY_RATIO_KILL}"
        )

    return {
        "verdict": "FAIL" if failures else "PASS",
        "failures": failures,
        "max_periodic_mean_rel_error": max_err_p,
        "max_antiperiodic_mean_rel_error": max_err_a,
        "max_periodic_fragility_ratio": max_frag_p,
        "max_antiperiodic_fragility_ratio": max_frag_a,
        "kill_thresholds": {
            "monotone_decreasing": True,
            "mean_rel_error": E2_REL_MEAN_ERROR_KILL,
            "fragility_ratio": E2_FRAGILITY_RATIO_KILL,
        },
        "scope": {
            "lambda": "FREE_COUPLING_PARAMETER",
            "safe_for_runtime": False,
            "spin_structure_selected": False,
            "geometry_claim": "none — GEOMETRY_AGNOSTIC intact",
            "description": "descriptive robustness check only",
        },
    }


# ---------------------------------------------------------------------------
# Gate runner
# ---------------------------------------------------------------------------


def run_e2_gate(n_alpha: int = E2_N_ALPHA) -> dict:
    """Orchestrate BG-H1-E2: disorder robustness of product KK gap δ(R)."""
    sweep = run_disorder_sweep(n_alpha=n_alpha)
    verdict = e2_verdict(sweep)
    return {
        "gate": "BG-H1-E2",
        "description": "Disorder robustness of S³×S¹ product KK gap at W=0.5",
        "n_alpha": n_alpha,
        "sweep": sweep,
        "verdict": verdict,
    }
