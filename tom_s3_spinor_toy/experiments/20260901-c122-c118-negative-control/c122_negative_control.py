"""C122 v3 -- random-matrix negative control for C118's density
hypothesis. v1 was a category error (complex perturbation on a real
operator). v2 fixed that but FL Step 8a skeptic found the comparison
itself was broken: the real family's own `s*` came from C118's coarse
search (step 0.05), while v2's random family used a much finer
log-spaced search -- the two arms were never sampled in the same
region, so "no overlap" compared apples to an interval the real family
was never measured in. v2's headline "30-300x" was also arithmetically
wrong (per-dimension ratios are 15-195x), and v2's own pre-registered
kill criterion (matching s*~1/dim power-law exponents) was actually
SATISFIED by the random family and not reported.

v3 fixes all three: reuses C118's own `build_cell` UNMODIFIED to
rebuild the REAL D_PW_full/Delta_H matrices, runs the SAME fine
log-spaced search on BOTH families (symmetric instrument), and
computes kappa(V) (eigenvector condition number) for the REAL family
directly -- previously unmeasured, the single most informative gap
C118's own decision.md named and no round had closed.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
from sympy import S

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c122.json"
SEED = 20260901
THRESHOLD = 1e-9
DIMS = [68, 130, 212, 314, 436]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def random_real_spectrum_matrix(dim: int, rng: np.random.Generator) -> tuple[np.ndarray, float]:
    """Non-Hermitian matrix with a guaranteed real spectrum (similarity
    transform of a random real-symmetric matrix). Returns (matrix,
    kappa(S)) -- kappa(V)=kappa(S) exactly for this construction (V=S@O,
    O orthogonal from H0's own eigendecomposition, right-multiplication
    by an orthogonal matrix preserves singular values)."""
    h0 = rng.standard_normal((dim, dim))
    h0 = (h0 + h0.T) / 2
    s_mat = rng.standard_normal((dim, dim))
    kappa_s = float(np.linalg.cond(s_mat))
    s_inv = np.linalg.inv(s_mat)
    return s_mat @ h0 @ s_inv, kappa_s


def random_symmetric_unit_norm(dim: int, rng: np.random.Generator) -> np.ndarray:
    m = rng.standard_normal((dim, dim))
    m = (m + m.T) / 2
    op_norm = np.linalg.norm(m, ord=2)
    return m / op_norm


def max_im_at(d_full: np.ndarray, delta: np.ndarray, s: float) -> float:
    eigs = np.linalg.eigvals(d_full - s * delta)
    return float(np.max(np.abs(np.imag(eigs))))


def kappa_v(d_full: np.ndarray) -> float:
    """Eigenvector condition number: kappa(V) where D = V diag(lambda) V^-1."""
    _eigvals, eigvecs = np.linalg.eig(d_full)
    return float(np.linalg.cond(eigvecs))


def find_critical_s_fine(d_full: np.ndarray, delta: np.ndarray) -> tuple[float | None, list[dict]]:
    """Log-spaced scan (1e-8 to 1, 40 points) then bisection to
    relative tolerance 1e-4 -- the SAME search used for both the real
    and random families in this round (fixes v2's asymmetric-
    instrument bug)."""
    coarse = []
    s_grid = np.concatenate([[0.0], np.logspace(-8, 0, 40)])
    for s in s_grid:
        mi = max_im_at(d_full, delta, float(s))
        coarse.append({"s": float(s), "max_im": mi})

    if coarse[0]["max_im"] >= THRESHOLD:
        return None, coarse
    if coarse[-1]["max_im"] < THRESHOLD:
        return None, coarse

    lo, hi = 0.0, 1.0
    for row in coarse:
        if row["max_im"] < THRESHOLD:
            lo = max(lo, row["s"])
        else:
            hi = min(hi, row["s"])
            break

    for _ in range(60):
        mid = hi / 2 if lo == 0 else (lo + hi) / 2
        mi = max_im_at(d_full, delta, mid)
        if mi < THRESHOLD:
            lo = mid
        else:
            hi = mid
        if lo > 0 and (hi - lo) / hi < 1e-4:
            break
        if lo == 0 and hi < 1e-15:
            break

    return hi, coarse


def count_islands(coarse: list[dict]) -> int:
    """Counts real-restoration islands: sub-threshold stretches that
    reappear after an earlier supra-threshold crossing."""
    seen_supra = False
    islands = 0
    prev_supra = False
    for row in coarse:
        supra = row["max_im"] >= THRESHOLD
        if seen_supra and prev_supra and not supra:
            islands += 1
        if supra:
            seen_supra = True
        prev_supra = supra
    return islands


REAL_CELLS = [
    ("1", 2, S(1)),
    ("3/2", 3, S(3) / 2),
    ("2", 4, S(2)),
    ("5/2", 5, S(5) / 2),
    ("3", 6, S(3)),
]


def main() -> None:
    c85 = load_module(
        "c85_certification",
        HERE.parent
        / "20260812-c85-peter-weyl-representation-certification"
        / "c85_certification.py",
    )
    c114 = load_module(
        "c114_subset_analysis",
        HERE.parent
        / "20260830-c114-subset-analysis-matched-diagonal-cells"
        / "c114_subset_analysis.py",
    )
    c118 = load_module(
        "c118_eigengap_check",
        HERE.parent / "20260831-c118-eigengap-density-check" / "c118_eigengap_check.py",
    )

    print("=== REAL family: rebuild via C118's own build_cell, fine search, kappa(V) ===")
    real_rows = []
    for label, k_source, j2 in REAL_CELLS:
        print(f"\n--- real j2={label} ---")
        d_full, delta, dim = c118.build_cell(c85, c114, k_source, j2)
        kv = kappa_v(d_full)
        s_star, coarse = find_critical_s_fine(d_full, delta)
        islands = count_islands(coarse)
        row = {
            "j2": label,
            "dim": dim,
            "kappa_V": kv,
            "islands_in_fine_scan": islands,
        }
        if s_star is not None:
            row["s_star_fine"] = s_star
            row["s_star_fine_times_dim"] = s_star * dim
            print(f"  dim={dim}, kappa(V)={kv:.4g}, s*_fine={s_star:.6e}, islands={islands}")
        else:
            row["skipped"] = True
            print(
                f"  dim={dim}, kappa(V)={kv:.4g}, SKIPPED (s0/s1 guard failed), islands={islands}"
            )
        real_rows.append(row)

    print("\n=== RANDOM family: same fine search, same seed as v2 ===")
    rng = np.random.default_rng(SEED)
    random_rows = []
    for dim in DIMS:
        print(f"\n--- random dim={dim} ---")
        d_full, kappa_s = random_real_spectrum_matrix(dim, rng)
        d_full = d_full.astype(complex)
        delta = random_symmetric_unit_norm(dim, rng).astype(complex)
        s_star, coarse = find_critical_s_fine(d_full, delta)
        islands = count_islands(coarse)
        row = {"dim": dim, "kappa_S": kappa_s, "islands_in_fine_scan": islands}
        if s_star is not None:
            row["s_star_fine"] = s_star
            row["s_star_fine_times_dim"] = s_star * dim
            print(f"  dim={dim}, kappa(S)={kappa_s:.4g}, s*_fine={s_star:.6e}, islands={islands}")
        else:
            row["skipped"] = True
        random_rows.append(row)

    real_valid = [r for r in real_rows if not r.get("skipped")]
    random_valid = [r for r in random_rows if not r.get("skipped")]
    real_s_dim = [r["s_star_fine_times_dim"] for r in real_valid]
    random_s_dim = [r["s_star_fine_times_dim"] for r in random_valid]
    real_kappa = [r["kappa_V"] for r in real_valid]
    random_kappa = [r["kappa_S"] for r in random_valid]

    print("\n--- Summary (SAME fine instrument for both families) ---")
    print(f"Real   s*.dim: {real_s_dim}")
    print(f"Random s*.dim: {random_s_dim}")
    print(f"Real   kappa(V): {real_kappa}")
    print(f"Random kappa(V)=kappa(S): {random_kappa}")

    # Power-law fit ln(s*) vs ln(dim), both families
    def power_law_exponent(dims, s_vals):
        if len(dims) < 2:
            return None
        x = np.log(dims)
        y = np.log(s_vals)
        slope, _intercept = np.polyfit(x, y, 1)
        return float(slope)

    real_exponent = power_law_exponent(
        [r["dim"] for r in real_valid], [r["s_star_fine"] for r in real_valid]
    )
    random_exponent = power_law_exponent(
        [r["dim"] for r in random_valid], [r["s_star_fine"] for r in random_valid]
    )
    print(f"\nPower-law exponent (s* ~ dim^p): real p={real_exponent}, random p={random_exponent}")

    real_islands_total = sum(r["islands_in_fine_scan"] for r in real_rows)
    random_islands_total = sum(r["islands_in_fine_scan"] for r in random_rows)
    print(f"Total islands: real={real_islands_total}, random={random_islands_total}")

    overlap = None
    if real_s_dim and random_s_dim:
        real_range = (min(real_s_dim), max(real_s_dim))
        random_range = (min(random_s_dim), max(random_s_dim))
        overlap = not (random_range[1] < real_range[0] or random_range[0] > real_range[1])
    print(f"\nRanges overlap under SAME fine instrument: {overlap}")

    out = {
        "seed": SEED,
        "real_rows": real_rows,
        "random_rows": random_rows,
        "real_s_star_fine_times_dim": real_s_dim,
        "random_s_star_fine_times_dim": random_s_dim,
        "real_kappa_V": real_kappa,
        "random_kappa_V": random_kappa,
        "real_power_law_exponent": real_exponent,
        "random_power_law_exponent": random_exponent,
        "real_islands_total": real_islands_total,
        "random_islands_total": random_islands_total,
        "ranges_overlap_same_instrument": overlap,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
