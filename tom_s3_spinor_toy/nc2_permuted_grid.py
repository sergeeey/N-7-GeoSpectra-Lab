"""NC2_PERMUTED_GRID_NEGATIVE_CONTROL — v0.2.0 spinor-geometry pivot, Tier-3.

Verifies that the Dirac spectral fingerprint |λ_min| = d/2 is a GENUINE
geometric discriminant, not a matrix artifact of the tridiagonal structure.

Test: randomly permute the potential V(α_i) while keeping the kinetic
(off-diagonal) structure intact.  The SUSY quantum-well structure of the
Dirac² operator requires the smooth ordering of V — permutation destroys it.

Expected: |λ_min|_perm >> d/2  (fingerprint is NOT preserved).
NC-2 passes (valid negative control) iff all seeds show large deviation.

Physical interpretation of the result:
  The Dirac² potential V(α) = κ(κ + χ·cos 2α)/sin² 2α is tuned to produce
  the SUSY partner ladder λ_n = n + d/2 through the smooth Jacobi polynomial
  structure.  Random permutation of V completely breaks this, and |λ_min|
  shoots up by hundreds of percent — confirming the fingerprint is a
  TOPOLOGICAL / GEOMETRIC property of the smooth Hopf coordinate system,
  not an artifact of the tridiagonal matrix topology alone.

Hard constraints (identical to E0/KT-3):
  - IPR not used as endpoint.
  - No claim about S³×S¹ (HA-4 OPEN).
  - No physical promotion.
"""

from __future__ import annotations

import json

import numpy as np
from scipy.linalg import eigh_tridiagonal

from tom_s3_spinor_toy.discrete_radial_dirac_proxy import dirac_sq_alpha_tridiag

NC2_MIN_DEVIATION: float = 0.50   # fingerprint must deviate >50%; actual ~300%
N_SEEDS: int = 5


def permuted_grid_lambda_min(
    d: int,
    l_sector: int = 0,
    n_grid: int = 2000,
    seed: int = 0,
    chirality: int = -1,
) -> float:
    """Lowest |λ| for H_χ with potential values V(α_i) randomly permuted.

    Kinetic structure (off-diagonal = -1/(4h²)) is preserved; only the
    potential array is permuted.  This destroys the SUSY quantum-well
    without changing the tridiagonal graph topology.
    """
    diag, off, _alpha = dirac_sq_alpha_tridiag(d, l_sector, n_grid, chirality)
    h = (np.pi / 2.0) / n_grid
    kinetic = 2.0 / (4.0 * h**2)
    potential = diag - kinetic
    rng = np.random.default_rng(seed)
    diag_perm = kinetic + rng.permutation(potential)
    val = eigh_tridiagonal(
        diag_perm, off, select="i", select_range=(0, 0), eigvals_only=True
    )
    return float(np.sqrt(abs(val[0])))


def run_nc2(
    d: int = 3,
    l_sector: int = 0,
    n_grid: int = 2000,
    n_seeds: int = N_SEEDS,
) -> dict:
    """Run NC-2 for one sphere dimension over n_seeds permutations."""
    from tom_s3_spinor_toy.disorder_survival_proxy import baseline_lambda_min

    analytic = float(d) / 2.0
    baseline = baseline_lambda_min(d, l_sector, n_grid)

    seed_results: list[dict] = []
    for seed in range(n_seeds):
        lm = permuted_grid_lambda_min(d, l_sector, n_grid, seed)
        dev = abs(lm - analytic) / analytic
        seed_results.append({
            "seed": seed,
            "lambda_min_permuted": lm,
            "deviation_fraction": dev,
            "fingerprint_destroyed": bool(dev > NC2_MIN_DEVIATION),
        })

    n_destroyed = sum(1 for r in seed_results if r["fingerprint_destroyed"])
    all_destroyed = n_destroyed == n_seeds

    return {
        "experiment": "NC2_PERMUTED_GRID_NEGATIVE_CONTROL",
        "version": "v0.2.0",
        "d": d,
        "n_grid": n_grid,
        "n_seeds": n_seeds,
        "analytic_target": analytic,
        "clean_baseline": baseline,
        "seed_results": seed_results,
        "n_seeds_fingerprint_destroyed": n_destroyed,
        "min_deviation_fraction": float(min(r["deviation_fraction"] for r in seed_results)),
        "max_deviation_fraction": float(max(r["deviation_fraction"] for r in seed_results)),
        "verdict": "NC2_PASS" if all_destroyed else "NC2_FAIL",
        "verdict_note": (
            "fingerprint destroyed in ALL seeds — harness is GEOMETRY-SENSITIVE"
            if all_destroyed else
            "fingerprint survived ≥1 permutation — FINGERPRINT MAY BE MATRIX ARTIFACT"
        ),
        "scope": {
            "HA-4": "OPEN — NC-2 is a Tier-3 control for S^d only",
            "promotion": "NONE — research_only",
            "ipr": "NOT USED as endpoint",
        },
    }


def run_nc2_full(n_grid: int = 2000) -> dict:
    """Run NC-2 for S³ (primary) and S⁶ (secondary); combine result."""
    s3 = run_nc2(d=3, n_grid=n_grid)
    s6 = run_nc2(d=6, n_grid=n_grid)
    overall = "NC2_PASS" if (s3["verdict"] == "NC2_PASS" and s6["verdict"] == "NC2_PASS") else "NC2_FAIL"
    return {
        "experiment": "NC2_PERMUTED_GRID_NEGATIVE_CONTROL_FULL",
        "overall_verdict": overall,
        "s3": s3,
        "s6": s6,
    }


def main() -> None:
    result = run_nc2_full()
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/"
        "nc2_permuted_grid_results.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    print(json.dumps(result, indent=2, default=str))
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
