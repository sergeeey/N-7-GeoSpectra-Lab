"""KT3_DISORDER_SURVIVAL_TEST — v0.2.0 spinor-geometry pivot.

Tests whether the Dirac spectral fingerprint (|λ_min| = d/2) survives
diagonal disorder W·diag(ξ_i), ξ_i ~ Uniform[-1, 1], on the Hopf α-grid.

Pre-registered kill-test (from decision_record_v0.2.0.md):
  At W = 0.1, if max-over-seeds shift of |λ_min| exceeds
  KT3_THRESHOLD = 0.25  (= half the S²↔S³ spectral distance |1.0 − 1.5| / 2)
  → verdict KT3_FAIL_OR_SCOPE_W0_ONLY.

  Physical meaning: if |λ_min| shifts by > 0.25, S³ fingerprint enters S²
  territory and geometry discrimination breaks.  KT3_PASS means the fingerprint
  is robust to this disorder level.

Operator: H_χ u = -(1/4) u'' + κ(κ + χ·cos 2α)/sin² 2α · u + W · ξ_i · u
  (E0 baseline + diagonal disorder; κ = l + (d-1)/2, χ = -1 fixed).

Hard constraints honored (identical to E0, enforced by tests):
  - IPR not used as primary endpoint anywhere.
  - No claim this resolves S³×S¹ GEOMETRY_AGNOSTIC (HA-4 OPEN).
  - No physical promotion (research_only).
  - tom_ansatz → phi_11 remains RADIAL_PROJECTION_FINDING_ONLY (unchanged).
"""

from __future__ import annotations

import json

import numpy as np
from scipy.linalg import eigh_tridiagonal

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import dirac_sq_alpha_tridiag

# ---------------------------------------------------------------------------
# Constants — pre-registered in decision_record_v0.2.0.md
# ---------------------------------------------------------------------------

W_VALUES: list[float] = [0.01, 0.05, 0.1, 0.25, 0.5]
N_SEEDS: int = 10
KT3_THRESHOLD: float = 0.25   # gap/2 = |λ_min(S²) − λ_min(S³)| / 2
W_KILL: float = 0.1            # the pre-registered disorder level for the verdict


# ---------------------------------------------------------------------------
# Core disorder computation
# ---------------------------------------------------------------------------

def baseline_lambda_min(
    d: int,
    l_sector: int = 0,
    n_grid: int = 2000,
    chirality: int = -1,
) -> float:
    """Clean (W=0) lowest |λ| from the E0 operator, matches recover_ladder[0]."""
    diag, off, _alpha = dirac_sq_alpha_tridiag(d, l_sector, n_grid, chirality)
    val = eigh_tridiagonal(
        diag, off, select="i", select_range=(0, 0), eigvals_only=True
    )
    return float(np.sqrt(abs(val[0])))


def disordered_lambda_min(
    d: int,
    l_sector: int,
    n_grid: int,
    W: float,
    seed: int,
    chirality: int = -1,
) -> float:
    """Lowest |λ| of H_χ + W·diag(ξ_i) for one disorder realisation."""
    diag, off, _alpha = dirac_sq_alpha_tridiag(d, l_sector, n_grid, chirality)
    rng = np.random.default_rng(seed)
    xi = rng.uniform(-1.0, 1.0, size=len(diag))
    diag_disordered = diag + W * xi
    val = eigh_tridiagonal(
        diag_disordered, off, select="i", select_range=(0, 0), eigvals_only=True
    )
    return float(np.sqrt(abs(val[0])))


# ---------------------------------------------------------------------------
# Sweep
# ---------------------------------------------------------------------------

def disorder_survival_sweep(
    d: int = 3,
    l_sector: int = 0,
    n_grid: int = 2000,
    w_values: list[float] | None = None,
    n_seeds: int = N_SEEDS,
) -> list[dict]:
    """Sweep W × seeds; record |λ_min| shifts from the W=0 baseline.

    Returns a list of per-W dicts (JSON-serialisable).
    """
    if w_values is None:
        w_values = W_VALUES

    baseline = baseline_lambda_min(d, l_sector, n_grid)
    results: list[dict] = []

    for W in w_values:
        lambdas: list[float] = []
        shifts: list[float] = []
        for seed in range(n_seeds):
            lm = disordered_lambda_min(d, l_sector, n_grid, W, seed)
            lambdas.append(lm)
            shifts.append(abs(lm - baseline))

        results.append({
            "W": float(W),
            "baseline_lambda_min": float(baseline),
            "lambda_min_samples": lambdas,
            "shifts": shifts,
            "mean_shift": float(np.mean(shifts)),
            "median_shift": float(np.median(shifts)),
            "max_shift": float(np.max(shifts)),
            "std_shift": float(np.std(shifts)),
        })

    return results


# ---------------------------------------------------------------------------
# Kill-test verdict
# ---------------------------------------------------------------------------

def kt3_verdict(
    sweep_results: list[dict],
    W_kill: float = W_KILL,
    threshold: float = KT3_THRESHOLD,
) -> dict:
    """Pre-registered verdict on the KT-3 kill condition.

    Fails if max_shift OR median_shift at W_kill exceeds threshold.
    Also reports W* (largest W in sweep where max_shift < threshold).
    """
    entry = next(
        (r for r in sweep_results if abs(r["W"] - W_kill) < 1e-9), None
    )
    if entry is None:
        return {"verdict": "W_KILL_NOT_IN_SWEEP", "W_kill": W_kill}

    max_shift = entry["max_shift"]
    median_shift = entry["median_shift"]
    fails = (max_shift > threshold) or (median_shift > threshold)

    verdict = "KT3_FAIL_OR_SCOPE_W0_ONLY" if fails else "KT3_PASS"
    margin = threshold - max_shift  # positive = safe margin

    # W* = largest W in sweep where max_shift < threshold
    w_star: float | None = None
    for r in sorted(sweep_results, key=lambda x: x["W"]):
        if r["max_shift"] < threshold:
            w_star = r["W"]
        else:
            break

    return {
        "verdict": verdict,
        "W_kill": W_kill,
        "max_shift_at_W_kill": max_shift,
        "median_shift_at_W_kill": median_shift,
        "threshold": threshold,
        "safety_margin": float(margin),
        "w_star": w_star,
        "w_star_note": (
            f"fingerprint robust for W ≤ {w_star}" if w_star is not None
            else "not determined (all W values pass or none)"
        ),
    }


# ---------------------------------------------------------------------------
# Full KT-3 run
# ---------------------------------------------------------------------------

def run_kt3(n_grid: int = 2000) -> dict:
    """Orchestrate KT-3: S³ primary, S⁶ secondary; record hard constraints."""
    s3_sweep = disorder_survival_sweep(d=3, l_sector=0, n_grid=n_grid)
    s3_verd = kt3_verdict(s3_sweep)

    s6_sweep = disorder_survival_sweep(d=6, l_sector=0, n_grid=n_grid)
    s6_verd = kt3_verdict(s6_sweep)

    # Cross-sphere separation check at W_kill = 0.1
    s3_entry = next(r for r in s3_sweep if abs(r["W"] - W_KILL) < 1e-9)
    s6_entry = next(r for r in s6_sweep if abs(r["W"] - W_KILL) < 1e-9)
    s3_lm_samples = s3_entry["lambda_min_samples"]
    s6_lm_samples = s6_entry["lambda_min_samples"]
    # S³ ≈ 1.5, S⁶ ≈ 3.0 — gap = 1.5 >> threshold 0.25; check worst-case overlap
    s3_max_lm = float(max(s3_lm_samples))
    s6_min_lm = float(min(s6_lm_samples))
    separation_ok = s6_min_lm - s3_max_lm > 0.5  # conservative: gap still > 0.5

    return {
        "experiment": "KT3_DISORDER_SURVIVAL_TEST",
        "version": "v0.2.0",
        "primary_endpoint": (
            "shift of |lambda_min| under diagonal disorder W·diag(xi); "
            "IPR not used"
        ),
        "kill_condition": (
            f"max-over-seeds shift at W={W_KILL} > threshold={KT3_THRESHOLD} → "
            "KT3_FAIL_OR_SCOPE_W0_ONLY"
        ),
        "n_grid": n_grid,
        "n_seeds": N_SEEDS,
        "w_values": W_VALUES,
        "s3": {
            "sweep": s3_sweep,
            "verdict": s3_verd,
        },
        "s6": {
            "sweep": s6_sweep,
            "verdict": s6_verd,
        },
        "cross_sphere_separation_at_W01": {
            "s3_max_lambda_min": s3_max_lm,
            "s6_min_lambda_min": s6_min_lm,
            "gap": float(s6_min_lm - s3_max_lm),
            "separation_ok": bool(separation_ok),
        },
        "scope": {
            "HA-4": (
                "OPEN — disorder survival on pure S^d does not address the "
                "original S3xS1 GEOMETRY_AGNOSTIC verdict"
            ),
            "promotion": "NONE — research_only",
            "tom_ansatz": "RADIAL_PROJECTION_FINDING_ONLY — unchanged from E0",
            "ipr": "NOT USED as primary endpoint",
        },
    }


def main() -> None:
    result = run_kt3(n_grid=2000)
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/"
        "kt3_disorder_survival_results.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    print(json.dumps(result, indent=2, default=str))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
