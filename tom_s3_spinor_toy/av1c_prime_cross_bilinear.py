"""AV1C_PRIME_CROSS_BILINEAR_DICTIONARY — v0.2.0, follow-up to AV-1c FAIL.

Pre-registered: experiments/.../claim_av1c_prime.md (written BEFORE this ran).

AV-1c failed (12.38% > 10%) with diagonal bilinears only.  This experiment
tests cross-bilinears phi_nl * phi_n'l' and — faithful to Tom's eq. (49) —
the constant f^(phi) term:

    sqrt(||g||) = f^(phi) + sum f^(psi) psi psi + ...

Analytic prior (pre-registered): every bilinear vanishes >= cos^2 at
alpha -> pi/2 while the target sin(2a) vanishes as cos^1; only the constant
term can compensate that boundary layer.  D1 (pure bilinears) vs D2
(bilinears + constant) is therefore a direct test of whether f^(phi) is
load-bearing in the radial layer of eq. 49.

Hard constraints:
  - No full spinor identification claim; angular (AV-2) pending.
  - No physical promotion; lambda = FREE_COUPLING_PARAMETER.
"""

from __future__ import annotations

import json
from itertools import combinations_with_replacement

import numpy as np

from tom_s3_spinor_toy.av1_angular_dictionary import (
    alpha_grid,
    gram_least_squares,
    inner_w,
    normalize,
)
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf

N_GRID: int = 4000
BOUNDARY_FAMILY: list[tuple[int, int]] = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
EXTENDED_FAMILY: list[tuple[int, int]] = [
    (n, l) for l in range(5) for n in range(l, l + 3)
]
PROMOTE_RESIDUAL: float = 0.05
KILL_RESIDUAL: float = 0.10
K_TERMS: int = 5


def build_bilinear_dictionary(
    modes: list[tuple[int, int]],
    alpha: np.ndarray,
    include_constant: bool,
    weighted: bool = True,
) -> tuple[list[str], np.ndarray]:
    """All unordered cross-bilinears phi_a*phi_b (+ optional constant), normalized."""
    labels: list[str] = []
    rows: list[np.ndarray] = []
    if include_constant:
        labels.append("const")
        rows.append(normalize(np.ones_like(alpha), alpha, weighted))
    for (n1, l1), (n2, l2) in combinations_with_replacement(modes, 2):
        prod = phi_nl_hopf(n1, l1, alpha) * phi_nl_hopf(n2, l2, alpha)
        labels.append(f"({n1},{l1})x({n2},{l2})")
        rows.append(normalize(prod, alpha, weighted))
    return labels, np.array(rows)


def greedy_k_term_labeled(
    target: np.ndarray,
    labels: list[str],
    dictionary: np.ndarray,
    alpha: np.ndarray,
    k: int = K_TERMS,
    weighted: bool = True,
) -> tuple[list[str], float, np.ndarray]:
    """OMP-style greedy; returns (chosen labels, residual fraction, residual array)."""
    chosen: list[int] = []
    residual = target.copy()
    for _ in range(k):
        projs = [abs(inner_w(residual, mode, alpha, weighted)) for mode in dictionary]
        for idx in chosen:
            projs[idx] = -1.0
        best = int(np.argmax(projs))
        chosen.append(best)
        sub = dictionary[chosen]
        coeffs, _ = gram_least_squares(target, sub, alpha, weighted)
        residual = target - coeffs @ sub
    res_frac = np.sqrt(
        inner_w(residual, residual, alpha, weighted)
        / inner_w(target, target, alpha, weighted)
    )
    return [labels[i] for i in chosen], float(res_frac), residual


def run_dictionary(
    name: str,
    modes: list[tuple[int, int]],
    include_constant: bool,
    n_grid: int = N_GRID,
    weighted: bool = True,
) -> dict:
    alpha = alpha_grid(n_grid)
    target = normalize(np.sin(2.0 * alpha), alpha, weighted)
    labels, dictionary = build_bilinear_dictionary(modes, alpha, include_constant, weighted)
    chosen, res_frac, residual = greedy_k_term_labeled(
        target, labels, dictionary, alpha, weighted=weighted
    )
    _, res_full = gram_least_squares(target, dictionary, alpha, weighted)
    peak_idx = int(np.argmax(np.abs(residual)))
    return {
        "dictionary": name,
        "n_elements": len(labels),
        "include_constant": include_constant,
        "greedy_5term_labels": chosen,
        "residual_5term": res_frac,
        "residual_full_ls": res_full,
        "residual_peak_alpha_over_pi": float(alpha[peak_idx] / np.pi),
        "constant_in_top5": "const" in chosen,
    }


def verdict_from_residual(residual: float) -> str:
    if residual < PROMOTE_RESIDUAL:
        return "PROMOTE_HT1_RADIAL_BILINEAR_STRUCTURE_SUPPORTED"
    if residual <= KILL_RESIDUAL:
        return "IMPROVED_BUT_INSUFFICIENT_HT1_STAYS_EXPLORATORY"
    return "KILL_HT1_STAYS_NOT_PROMOTED"


def run_av1c_prime(n_grid: int = N_GRID) -> dict:
    """Primary (D2, weighted) + mechanism checks (D1, D3) + sensitivity."""
    d1 = run_dictionary("D1_pure_bilinears", BOUNDARY_FAMILY, False, n_grid)
    d2 = run_dictionary("D2_bilinears_plus_const", BOUNDARY_FAMILY, True, n_grid)
    d3 = run_dictionary("D3_extended_plus_const", EXTENDED_FAMILY, True, n_grid)

    sens_unweighted = run_dictionary(
        "D2_unweighted", BOUNDARY_FAMILY, True, n_grid, weighted=False
    )
    sens_fine = run_dictionary("D2_fine_grid", BOUNDARY_FAMILY, True, 2 * n_grid)

    primary_residual = d2["residual_5term"]
    verdict = verdict_from_residual(primary_residual)

    p2_supported = d2["residual_5term"] < 0.5 * d1["residual_5term"]

    return {
        "experiment": "AV1C_PRIME_CROSS_BILINEAR_DICTIONARY",
        "version": "v0.2.0",
        "n_grid": n_grid,
        "primary_endpoint": "D2 greedy 5-term residual, weighted L2",
        "d1_pure_bilinears": d1,
        "d2_primary": d2,
        "d3_extended": d3,
        "sensitivity_unweighted": sens_unweighted,
        "sensitivity_fine_grid": sens_fine,
        "verdict": verdict,
        "mechanism": {
            "P2_constant_term_load_bearing": p2_supported,
            "d1_vs_d2_residual": [d1["residual_5term"], d2["residual_5term"]],
            "P1_residual_peak_alpha_over_pi_D1": d1["residual_peak_alpha_over_pi"],
        },
        "scope": {
            "angular": "NOT VERIFIED — radial layer only; AV-2 pending",
            "promotion_ceiling": "RADIAL_BILINEAR_STRUCTURE_SUPPORTED at most — "
            "NOT full spinor identification, NOT physical promotion",
            "lambda": "FREE_COUPLING_PARAMETER",
        },
    }


def main() -> None:
    result = run_av1c_prime()
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/"
        "av1c_prime_cross_bilinear_results.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    for key in ("d1_pure_bilinears", "d2_primary", "d3_extended"):
        d = result[key]
        print(
            f"{d['dictionary']:<28} 5-term={d['residual_5term']:.4f} "
            f"full-LS={d['residual_full_ls']:.4f} const_in_top5={d['constant_in_top5']} "
            f"peak_alpha/pi={d['residual_peak_alpha_over_pi']:.3f}"
        )
    print(f"\nVERDICT: {result['verdict']}")
    print(f"P2 (constant load-bearing): {result['mechanism']['P2_constant_term_load_bearing']}")
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
