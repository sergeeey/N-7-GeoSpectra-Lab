"""AV1_ANGULAR_DICTIONARY_ROBUSTNESS — v0.2.0, item-40 partial closure.

Pre-registered: experiments/20260610-spinor-geometry-pivot-v0.2.0/claim_av1_angular.md
(written BEFORE this module ran).

Three checks:
  AV-1a  global argmax of |<tom, phi_nl>| over 49-mode dictionary — must be (1,1)
  AV-1b  Gram least-squares decomposition (supportive, basis-dependent)
  AV-1c  bilinear probe: sin(2a) = tom_ansatz^2 vs span{phi_nl^2} — Tom's eq. 49
         radial layer

Connection to Tom's framework:
  tom_ansatz^2 = sin(2a) = 2*sqrt(det g) on S3 in Hopf coordinates, i.e. the
  LHS of Tom's eq. (49) up to a constant.  AV-1c asks whether the radial part
  of that expansion is efficiently captured by low-(n,l) Dirac bilinears.

Hard constraints (unchanged):
  - Full angular/spinor verification (half-integer Hopf weights, spin
    connection) is NOT performed here — that is AV-2.
  - No physical promotion; lambda = FREE_COUPLING_PARAMETER.
"""

from __future__ import annotations

import json

import numpy as np

from tom_s3_spinor_toy.geometry_s3_hopf import volume_measure
from tom_s3_spinor_toy.reference_spinor_harmonics import phi_nl_hopf, tom_ansatz

L_MAX: int = 6           # dictionary: 0 <= l <= L_MAX, l <= n <= l + N_EXTRA
N_EXTRA: int = 6
L_MAX_BILINEAR: int = 4
N_EXTRA_BILINEAR: int = 4
N_GRID: int = 4000

AV1A_EXPECTED_ARGMAX: tuple[int, int] = (1, 1)
AV1A_EXPECTED_VALUE: float = 0.9204
AV1B_RESIDUAL_MAX: float = 0.05    # 5-term approx, fraction of ||tom||
AV1C_RESIDUAL_MAX: float = 0.10    # 5-term bilinear approx
HT1_BOUNDARY_NORM_MIN: float = 0.80  # exploratory H-T1 promotion threshold


def alpha_grid(n_grid: int = N_GRID) -> np.ndarray:
    """Open grid on (0, pi/2) — endpoints excluded (modes vanish there)."""
    return np.linspace(0.0, np.pi / 2.0, n_grid + 2)[1:-1]


def inner_w(f: np.ndarray, g: np.ndarray, alpha: np.ndarray, weighted: bool = True) -> float:
    """<f, g> with weight sinα·cosα (weighted=True) or plain dα (False)."""
    w = volume_measure(alpha) if weighted else np.ones_like(alpha)
    return float(np.trapezoid(f * g * w, alpha))


def normalize(f: np.ndarray, alpha: np.ndarray, weighted: bool = True) -> np.ndarray:
    return f / np.sqrt(inner_w(f, f, alpha, weighted))


def build_dictionary(
    alpha: np.ndarray,
    l_max: int = L_MAX,
    n_extra: int = N_EXTRA,
    weighted: bool = True,
    squared: bool = False,
) -> tuple[list[tuple[int, int]], np.ndarray]:
    """Normalized dictionary {phi_nl} (or {phi_nl^2}) as rows of a matrix."""
    labels: list[tuple[int, int]] = []
    rows: list[np.ndarray] = []
    for l_val in range(l_max + 1):
        for n_val in range(l_val, l_val + n_extra + 1):
            mode = phi_nl_hopf(n_val, l_val, alpha)
            if squared:
                mode = mode * mode
            rows.append(normalize(mode, alpha, weighted))
            labels.append((n_val, l_val))
    return labels, np.array(rows)


def projection_table(
    target: np.ndarray,
    labels: list[tuple[int, int]],
    dictionary: np.ndarray,
    alpha: np.ndarray,
    weighted: bool = True,
) -> list[dict]:
    """|<target, mode>| for every dictionary mode, sorted descending."""
    table = []
    for (n_val, l_val), mode in zip(labels, dictionary):
        proj = inner_w(target, mode, alpha, weighted)
        table.append({"n": n_val, "l": l_val, "projection": proj, "abs_projection": abs(proj)})
    table.sort(key=lambda r: -r["abs_projection"])
    return table


def gram_least_squares(
    target: np.ndarray,
    dictionary: np.ndarray,
    alpha: np.ndarray,
    weighted: bool = True,
) -> tuple[np.ndarray, float]:
    """Solve min ||target - c·dict|| in the chosen L²; return (c, residual_fraction)."""
    w = volume_measure(alpha) if weighted else np.ones_like(alpha)
    # Gram matrix G_ij = <d_i, d_j>, rhs b_i = <d_i, target>
    weighted_dict = dictionary * w
    gram = weighted_dict @ dictionary.T * (alpha[1] - alpha[0])
    rhs = weighted_dict @ target * (alpha[1] - alpha[0])
    coeffs, *_ = np.linalg.lstsq(gram, rhs, rcond=1e-10)
    approx = coeffs @ dictionary
    res = target - approx
    residual_fraction = np.sqrt(inner_w(res, res, alpha, weighted) / inner_w(target, target, alpha, weighted))
    return coeffs, float(residual_fraction)


def greedy_k_term(
    target: np.ndarray,
    labels: list[tuple[int, int]],
    dictionary: np.ndarray,
    alpha: np.ndarray,
    k: int = 5,
    weighted: bool = True,
) -> tuple[list[tuple[int, int]], float]:
    """Greedy (OMP-style) k-term approximation; returns chosen labels + residual."""
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
    res_frac = np.sqrt(inner_w(residual, residual, alpha, weighted) / inner_w(target, target, alpha, weighted))
    return [labels[i] for i in chosen], float(res_frac)


def run_av1(n_grid: int = N_GRID, weighted: bool = True) -> dict:
    """Run AV-1a / AV-1b / AV-1c; return verdict dict."""
    alpha = alpha_grid(n_grid)
    tom = normalize(tom_ansatz(alpha), alpha, weighted)

    # --- AV-1a: global argmax over 49-mode dictionary -----------------------
    labels, dictionary = build_dictionary(alpha, weighted=weighted)
    table = projection_table(tom, labels, dictionary, alpha, weighted)
    top = table[0]
    argmax = (top["n"], top["l"])
    av1a_pass = argmax == AV1A_EXPECTED_ARGMAX

    # --- AV-1b: greedy 5-term least squares (supportive) --------------------
    chosen, residual_5term = greedy_k_term(tom, labels, dictionary, alpha, k=5, weighted=weighted)
    coeffs_full, _ = gram_least_squares(tom, dictionary, alpha, weighted)
    dominant_ls_idx = int(np.argmax(np.abs(coeffs_full)))
    av1b_pass = residual_5term < AV1B_RESIDUAL_MAX

    # --- AV-1c: bilinear probe of Tom's eq. 49 radial layer ------------------
    tom_sq = normalize(tom_ansatz(alpha) ** 2, alpha, weighted)
    labels_b, dict_b = build_dictionary(
        alpha, l_max=L_MAX_BILINEAR, n_extra=N_EXTRA_BILINEAR, weighted=weighted, squared=True
    )
    chosen_b, residual_b = greedy_k_term(tom_sq, labels_b, dict_b, alpha, k=5, weighted=weighted)
    phi11_sq_in_top5 = AV1A_EXPECTED_ARGMAX in chosen_b
    av1c_pass = residual_b < AV1C_RESIDUAL_MAX

    # --- H-T1 exploratory: n = l boundary family share -----------------------
    boundary_idx = [i for i, (n_val, l_val) in enumerate(labels) if n_val == l_val]
    sub = dictionary[boundary_idx]
    _, res_boundary = gram_least_squares(tom, sub, alpha, weighted)
    boundary_explained = 1.0 - res_boundary**2
    ht1_signal = boundary_explained > HT1_BOUNDARY_NORM_MIN

    return {
        "experiment": "AV1_ANGULAR_DICTIONARY_ROBUSTNESS",
        "version": "v0.2.0",
        "n_grid": n_grid,
        "weighted": weighted,
        "av1a": {
            "argmax": list(argmax),
            "argmax_value": top["abs_projection"],
            "expected": list(AV1A_EXPECTED_ARGMAX),
            "top10": table[:10],
            "verdict": "AV1A_PASS" if av1a_pass else "AV1A_FAIL_DICTIONARY_ARTIFACT",
        },
        "av1b": {
            "greedy_5term_modes": [list(c) for c in chosen],
            "residual_5term": residual_5term,
            "ls_dominant_mode": list(labels[dominant_ls_idx]),
            "verdict": "AV1B_PASS" if av1b_pass else "AV1B_FAIL",
            "caveat": "non-orthogonal dictionary — coefficients basis-dependent",
        },
        "av1c": {
            "greedy_5term_modes": [list(c) for c in chosen_b],
            "residual_5term": residual_b,
            "phi11_sq_in_top5": phi11_sq_in_top5,
            "verdict": "AV1C_PASS" if av1c_pass else "AV1C_FAIL",
        },
        "ht1_exploratory": {
            "boundary_family_explained_norm": boundary_explained,
            "threshold": HT1_BOUNDARY_NORM_MIN,
            "signal": ht1_signal,
            "status": "EXPLORATORY_ONLY — promotion rules in claim_av1_angular.md",
        },
        "scope": {
            "angular": "NOT VERIFIED — radial dictionary only; AV-2 (2D operator) required",
            "promotion": "NONE — research_only",
            "lambda": "FREE_COUPLING_PARAMETER",
        },
    }


def run_av1_with_sensitivity(n_grid: int = N_GRID) -> dict:
    """Primary run + 2 pre-registered sensitivity checks."""
    primary = run_av1(n_grid=n_grid, weighted=True)
    sens_unweighted = run_av1(n_grid=n_grid, weighted=False)
    sens_fine = run_av1(n_grid=2 * n_grid, weighted=True)
    return {
        "primary": primary,
        "sensitivity_unweighted": {
            "av1a_argmax": sens_unweighted["av1a"]["argmax"],
            "av1a_verdict": sens_unweighted["av1a"]["verdict"],
            "av1c_residual": sens_unweighted["av1c"]["residual_5term"],
        },
        "sensitivity_fine_grid": {
            "av1a_argmax": sens_fine["av1a"]["argmax"],
            "av1a_value": sens_fine["av1a"]["argmax_value"],
            "av1c_residual": sens_fine["av1c"]["residual_5term"],
        },
    }


def main() -> None:
    result = run_av1_with_sensitivity()
    out_path = (
        "experiments/20260610-spinor-geometry-pivot-v0.2.0/av1_angular_dictionary_results.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, default=str)
    p = result["primary"]
    print(f"AV-1a: argmax={p['av1a']['argmax']} value={p['av1a']['argmax_value']:.6f} "
          f"-> {p['av1a']['verdict']}")
    print(f"AV-1b: 5-term residual={p['av1b']['residual_5term']:.4f} -> {p['av1b']['verdict']}")
    print(f"AV-1c: 5-term residual={p['av1c']['residual_5term']:.4f} "
          f"phi11^2 in top5={p['av1c']['phi11_sq_in_top5']} -> {p['av1c']['verdict']}")
    print(f"H-T1:  boundary family explains {p['ht1_exploratory']['boundary_family_explained_norm']:.4f} "
          f"(signal={p['ht1_exploratory']['signal']})")
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
