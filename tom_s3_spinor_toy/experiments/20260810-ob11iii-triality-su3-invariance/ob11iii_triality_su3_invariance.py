"""OB11(iii), cross-construction check: is the su(3) matter action genuinely
triality-fixed, within Baez's octonion-trilinear-covariance realization of the
triality triple (V=S+=S-=O), independent of G102's Cl(0,8)-chirality-splitting
realization?

Reuses `experiments/20260715-l3b-triality-so4xso4-invariance/triality_so4xso4_invariance.py`
unmodified: its own from-scratch octonion table, g2 basis, and
`solve_triality_partners` (Baez, "The Octonions," Sec 2.4). Extracts su(3) from
THIS file's own g2 basis via the same stabilizer-of-a-point technique G102 uses,
staying entirely within one self-contained construction to avoid any cross-file
basis-alignment problem.

Method (per claim.md, predictions recorded before running):
  P1: dim(su3) = 8 (stabilizer of a point in this file's own g2).
  P2: for all 8 su3 generators a, solve_triality_partners(a) = (a, a) exactly.
  P3 (negative control): a generic non-g2 so(8) element does NOT satisfy this.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ob11iii.json"

L3B_PATH = (
    HERE.parent / "20260715-l3b-triality-so4xso4-invariance" / "triality_so4xso4_invariance.py"
)
_spec = importlib.util.spec_from_file_location("triality_so4xso4_invariance", L3B_PATH)
assert _spec and _spec.loader
L3B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L3B)

TOL = 1e-8


def nullspace(mat: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > tol * max(mat.shape) * (s[0] if len(s) else 1.0)))
    return vt[rank:]


def stabilizer_basis(g2_basis: np.ndarray, point_index: int = 1) -> list[np.ndarray]:
    """Elements of span(g2_basis) annihilating e_{point_index} -- same technique
    as G102.stabilizer_basis, applied to THIS file's own from-scratch g2.

    point_index MUST be an imaginary unit (>=1), matching G102's own default.
    Index 0 is the octonion real unit "1" -- every derivation kills it
    automatically (D(1)=D(1*1)=2D(1) => D(1)=0), so stabilizing e_0 does not
    cut g2 down to su(3) at all; caught by an initial run giving dim 7 instead
    of the expected 8, traced to this exact convention mismatch before
    accepting any result."""
    e_pt = np.zeros(8)
    e_pt[point_index] = 1.0
    cols = np.array([g @ e_pt for g in g2_basis]).T  # 8 x n_gens
    coeffs = nullspace(cols)
    return [sum(c * g2_basis[k] for k, c in enumerate(row)) for row in coeffs]


def main() -> None:
    g2 = L3B.G2_BASIS  # (14, 8, 8)
    su3 = stabilizer_basis(g2)
    n_su3 = len(su3)

    # --- P2: solve_triality_partners on every su3 generator ---
    su3_residuals = []
    for a in su3:
        b, c, lstsq_residual = L3B.solve_triality_partners(a)
        b_dev = float(np.max(np.abs(b - a)))
        c_dev = float(np.max(np.abs(c - a)))
        su3_residuals.append(
            {
                "b_deviation_from_a": b_dev,
                "c_deviation_from_a": c_dev,
                "lstsq_residual": float(lstsq_residual),
            }
        )

    max_b_dev = max(r["b_deviation_from_a"] for r in su3_residuals)
    max_c_dev = max(r["c_deviation_from_a"] for r in su3_residuals)
    p2_pass = max_b_dev < TOL and max_c_dev < TOL

    # --- P3: negative control, generic non-g2 so(8) element ---
    rng = np.random.default_rng(0)
    raw = rng.normal(size=(8, 8))
    generic = raw - raw.T  # generic antisymmetric so(8) element

    # project out any g2-component to guarantee it's not accidentally in g2
    g2_flat = np.array([m.flatten() for m in g2])  # 14 x 64
    Qg2, _ = np.linalg.qr(g2_flat.T)
    generic_flat = generic.flatten()
    generic_flat_perp = generic_flat - Qg2 @ (Qg2.T @ generic_flat)
    generic_perp = generic_flat_perp.reshape(8, 8)
    # NOTE: no re-antisymmetrization needed -- g2's span lies entirely within the
    # antisymmetric subspace of R^{8x8}, so projecting an already-antisymmetric
    # `generic` onto g2's Frobenius-orthogonal complement stays antisymmetric
    # automatically (verified below, not assumed).
    antisym_residual = float(np.max(np.abs(generic_perp + generic_perp.T)))
    generic_perp_norm = float(np.max(np.abs(generic_perp)))

    b_gen, c_gen, resid_gen = L3B.solve_triality_partners(generic_perp)
    b_gen_dev = float(np.max(np.abs(b_gen - generic_perp)))
    c_gen_dev = float(np.max(np.abs(c_gen - generic_perp)))
    p3_pass = b_gen_dev > 1e-3 or c_gen_dev > 1e-3

    p1_pass = n_su3 == 8

    if not p3_pass:
        verdict = "HARNESS_CONTROL_FAILED"
    elif p1_pass and p2_pass:
        verdict = "SU3_TRIALITY_FIXED_CONFIRMED_INDEPENDENT_CONSTRUCTION"
    else:
        verdict = "SU3_NOT_TRIALITY_FIXED_SURPRISE"

    results = {
        "experiment": "ob11iii_triality_su3_invariance",
        "n_su3_generators": n_su3,
        "p1_dim_su3_is_8": p1_pass,
        "su3_triality_residuals": su3_residuals,
        "max_b_deviation": max_b_dev,
        "max_c_deviation": max_c_dev,
        "p2_all_su3_triality_fixed": p2_pass,
        "generic_element_antisym_residual": antisym_residual,
        "generic_element_perp_norm": generic_perp_norm,
        "generic_b_deviation": b_gen_dev,
        "generic_c_deviation": c_gen_dev,
        "generic_lstsq_residual": float(resid_gen),
        "p3_negative_control_pass": p3_pass,
        "verdict": verdict,
    }

    print("=" * 92)
    print("OB11(iii) cross-construction check: su(3) triality-fixedness")
    print("=" * 92)
    print(f"n_su3_generators = {n_su3} (predict 8)")
    print(f"max |b-a| over su3 = {max_b_dev:.2e}, max |c-a| over su3 = {max_c_dev:.2e}")
    print(f"P2 (all su3 triality-fixed)?  {p2_pass}")
    print()
    print(f"Negative control: generic so(8) element (perp-to-g2 norm {generic_perp_norm:.3f})")
    print(f"  |b-a| = {b_gen_dev:.4f}, |c-a| = {c_gen_dev:.4f} (expect >> 0)")
    print(f"P3 (negative control passes)?  {p3_pass}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
