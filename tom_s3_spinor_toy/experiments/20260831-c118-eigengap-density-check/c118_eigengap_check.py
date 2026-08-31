"""C118 v2 -- eigenvalue-density alternative to the "asymmetric rule",
corrected redesign after v1's global-minimum-gap statistic turned out
to be dominated by an unrelated structural degeneracy (D1=D2=
kron(I_dim_q, dbar) has exact repeated eigenvalues by construction --
see claim.md's SUBSTRATE FAILURE section for the full diagnosis).

v2 sweeps a continuous removal fraction s in [0,1] for a fixed,
cell-independent component choice (the corner (j2,j2), confirmed to
break reality at every tested cell) and locates s* -- the critical
fraction at which max|Im| first exceeds the project's own 1e-9
threshold. Per claim.md's pre-registration: does s* trend downward as
cell dimension grows?

Duplicates dbar_full's few lines (a closure inside C114's run_cell,
not module-level) but otherwise reuses C114's own build_M_ab_general,
magnetic_range unchanged via direct import.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import S

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c118.json"
THRESHOLD = 1e-9


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build_cell(c85_mod, c114_mod, k_source: int, j2):
    """Returns (D_PW_full_np, Delta_H_np) for the (j2,j2) corner removal."""
    rmult = [c85_mod.right_mult_matrix_on_ab(u) for u in ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]

    def dbar_full(level: int) -> sp.Matrix:
        l1, l2, l3 = c85_mod.build_l_matrices(level, "repaired")
        dbar = c85_mod.build_dbar([l1, l2, l3], rmult)
        dim_q = level + 1
        return sp.Matrix(sp.kronecker_product(sp.eye(dim_q), dbar))

    j1 = S(k_source) / 2
    target_level = int(2 * (j1 + j2))
    D1 = dbar_full(k_source)
    D2 = dbar_full(target_level)
    D1_np = np.array(D1.evalf().tolist(), dtype=np.float64)
    D2_np = np.array(D2.evalf().tolist(), dtype=np.float64)

    a_vals = c114_mod.magnetic_range(j2)
    pairs = [(a, b) for a in a_vals for b in a_vals]
    M_sum_np = None
    M_corner_np = None
    for a, b in pairs:
        M = c114_mod.build_M_ab_general(c85_mod, k_source, j2, a, b)
        M_np = np.array(M.evalf().tolist(), dtype=np.float64)
        M_sum_np = M_np if M_sum_np is None else M_sum_np + M_np
        if a == j2 and b == j2:
            M_corner_np = M_np
    assert M_corner_np is not None, f"corner (j2,j2)=({j2},{j2}) not found in pairs"

    n1, n2 = D1_np.shape[0], D2_np.shape[0]
    nt = n1 + n2

    def assemble(M_np):
        B_np = np.kron(M_np, np.eye(2))
        DPW = np.zeros((nt, nt), dtype=complex)
        DPW[:n1, :n1] = D1_np
        DPW[n1:, n1:] = D2_np
        DPW[n1:, :n1] = B_np
        DPW[:n1, n1:] = B_np.conj().T
        return DPW

    D_PW_full = assemble(M_sum_np)
    D_PW_removed = assemble(M_sum_np - M_corner_np)
    # Delta_H such that D_PW(s) = D_PW_full - s * Delta_H matches
    # D_PW_full at s=0 and D_PW_removed at s=1.
    Delta_H = D_PW_full - D_PW_removed
    return D_PW_full, Delta_H, nt


def max_im_at(D_PW_full: np.ndarray, Delta_H: np.ndarray, s: float) -> float:
    eigs = np.linalg.eigvals(D_PW_full - s * Delta_H)
    return float(np.max(np.abs(np.imag(eigs))))


def find_critical_s(D_PW_full: np.ndarray, Delta_H: np.ndarray) -> tuple[float, list[dict]]:
    coarse = []
    s_grid = np.linspace(0.0, 1.0, 21)
    for s in s_grid:
        mi = max_im_at(D_PW_full, Delta_H, float(s))
        coarse.append({"s": float(s), "max_im": mi})

    assert coarse[0]["max_im"] < THRESHOLD, "s=0 should be real (full sum, P0 already confirmed)"
    assert coarse[-1]["max_im"] > THRESHOLD, "s=1 (full corner removal) should break reality"

    lo, hi = 0.0, 1.0
    for row in coarse:
        if row["max_im"] < THRESHOLD:
            lo = max(lo, row["s"])
        else:
            hi = min(hi, row["s"])
            break

    for _ in range(30):
        mid = (lo + hi) / 2
        mi = max_im_at(D_PW_full, Delta_H, mid)
        if mi < THRESHOLD:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-6:
            break

    return hi, coarse


CELLS = [
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

    rows = []
    for label, k_source, j2 in CELLS:
        print(f"\n=== j2={label} (k_source={k_source}) ===")
        D_PW_full, Delta_H, dim = build_cell(c85, c114, k_source, j2)
        s_star, coarse = find_critical_s(D_PW_full, Delta_H)
        row = {"j2": label, "dim": dim, "s_star": s_star, "coarse_scan": coarse}
        rows.append(row)
        print(f"  dim={dim}, s*={s_star:.6f}")

    dims = [r["dim"] for r in rows]
    s_stars = [r["s_star"] for r in rows]
    reversals = sum(1 for i in range(len(s_stars) - 1) if s_stars[i + 1] > s_stars[i])
    monotone_enough = reversals <= 1

    print("\n--- Summary (dim, s*) ---")
    for r in rows:
        print(f"  j2={r['j2']:>4}: dim={r['dim']:>4}  s*={r['s_star']:.6f}")
    print(f"\nReversals in s* as dim increases: {reversals}")
    print(f"Monotone enough (<=1 reversal, per pre-registration): {monotone_enough}")

    verdict = (
        "DENSITY_HYPOTHESIS_SUPPORTED_S_STAR_TRENDS_DOWN"
        if monotone_enough
        else "DENSITY_HYPOTHESIS_NOT_SUPPORTED_S_STAR_DOES_NOT_TREND_DOWN"
    )

    out = {
        "rows": rows,
        "dims": dims,
        "s_stars": s_stars,
        "reversals": reversals,
        "monotone_enough": monotone_enough,
        "verdict": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {verdict}")


if __name__ == "__main__":
    main()
