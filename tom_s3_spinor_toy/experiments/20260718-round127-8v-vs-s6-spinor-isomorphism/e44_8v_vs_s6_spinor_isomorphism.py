"""Round127: is ℂ⊗8_v (complexified octonion vector rep, round124/G102),
restricted to su(3), isomorphic AS A COMPLEX su(3)-REPRESENTATION to Σ
(G14/G15's "S6 spinor", Λ•(ℂ3), built via Clifford-lifting su(3)'s action
on S6's 6-dim tangent space)? If an explicit isomorphism S exists,
transport round124's su(3)-centralizer generators through S into Σ's
basis and compare LITERALLY (not just by eigenvalue ratio, unlike the
flawed round126 approach) against G15's own established B-L matrix.

Reuses everything by direct import:
  - G102 (octonion table, su(3) on 8_v, centralizer)
  - G15's own module-level su3_spin (8 complex 8x8 matrices, su(3) on Σ)
    and BmL (G15's established B-L operator) -- g15_hypercharge.py itself
    imports g11_block_generators.lift_to_spinor and
    g10b_su3_explicit.su3_generators, so importing G15 pulls in the whole
    chain, nothing re-derived.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round127.json"
TOL = 1e-8

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec_g102 = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec_g102 and _spec_g102.loader
G102 = importlib.util.module_from_spec(_spec_g102)
_spec_g102.loader.exec_module(G102)

# g15_hypercharge.py inserts its own dependency paths via sys.path at import
# time (g11_block_generators, g10b_su3_explicit, g10_s6_so6_gauge) -- let it
# do that itself by importing it the same way it imports itself, rather
# than duplicating its own sys.path bookkeeping here.
G15_DIR = HERE.parent / "20260619-g15-hypercharge"
sys.path.insert(0, str(G15_DIR))
_spec_g15 = importlib.util.spec_from_file_location(
    "g15_hypercharge", G15_DIR / "g15_hypercharge.py"
)
assert _spec_g15 and _spec_g15.loader
G15 = importlib.util.module_from_spec(_spec_g15)
_spec_g15.loader.exec_module(G15)


def sympy_to_complex_np(mats: list[sp.Matrix]) -> list[np.ndarray]:
    return [np.array(M.evalf(), dtype=complex) for M in mats]


def hom_space_nullspace(reps_a: list[np.ndarray], reps_b: list[np.ndarray]) -> np.ndarray:
    """Complex nullspace of the stacked Sylvester system S@A_k = B_k@S for
    all k -- returns columns as an orthonormal basis of the Hom space
    (each column, reshaped, is one basis intertwiner)."""
    n_a = reps_a[0].shape[0]
    n_b = reps_b[0].shape[0]
    rows = []
    for a_k, b_k in zip(reps_a, reps_b):
        op = np.kron(a_k.T, np.eye(n_b)) - np.kron(np.eye(n_a), b_k)
        rows.append(op)
    mat = np.vstack(rows)
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > TOL * max(mat.shape) * (s[0] if len(s) else 1.0)))
    null = vt[rank:].conj().T  # columns = orthonormal basis (numpy svd gives Vt; V=Vt^H)
    return null


def main() -> None:
    # --- su(3) acting on 8_v (round124/G102), complexified ---
    der = G102.derivation_basis()
    su3_v_real = G102.stabilizer_basis(der)  # 8 real 8x8 antisymmetric matrices
    su3_v = [A.astype(complex) for A in su3_v_real]

    _cent_dim, cent_su3_real = G102.centralizer_dim(su3_v_real)
    cent_su3 = [C.astype(complex) for C in cent_su3_real]

    # --- su(3) acting on Sigma (G15's own su3_spin, complex 8x8) ---
    su3_sigma = sympy_to_complex_np(G15.su3_spin)
    BmL_sigma = np.array(G15.BmL.evalf(), dtype=complex)

    assert len(su3_v) == 8 and len(su3_sigma) == 8

    # --- Hom space: S such that S @ su3_v[i] = su3_sigma[i] @ S for all i ---
    hom_basis = hom_space_nullspace(su3_v, su3_sigma)
    hom_dim = hom_basis.shape[1]

    # --- search for an invertible element of the Hom space ---
    rng = np.random.default_rng(0)
    found_S = None
    best_det = 0.0
    n_trials = 200
    for _ in range(n_trials):
        coeffs = rng.normal(size=hom_dim) + 1j * rng.normal(size=hom_dim)
        S_flat = hom_basis @ coeffs
        S = S_flat.reshape(8, 8)
        det = abs(np.linalg.det(S))
        if det > best_det:
            best_det = det
        if det > 1e-3:
            found_S = S
            break

    # --- verify the isomorphism, if found ---
    iso_residual = None
    if found_S is not None:
        S = found_S
        Sinv = np.linalg.inv(S)
        residuals = [float(np.max(np.abs(S @ su3_v[i] @ Sinv - su3_sigma[i]))) for i in range(8)]
        iso_residual = max(residuals)

        # --- transport round124's centralizer generators through S ---
        cent_transported = [S @ C @ Sinv for C in cent_su3]

        # --- compare against BmL: is BmL in the span of {cent_transported} plus su3? ---
        # BmL commutes with all su3_sigma (G15's own T4), so if the isomorphism is
        # correct, cent_transported should also commute with su3_sigma -- check this
        # as an independent consistency test before comparing to BmL directly.
        commute_check = [
            float(np.max(np.abs(ct @ su3_sigma[i] - su3_sigma[i] @ ct)))
            for ct in cent_transported
            for i in range(8)
        ]
        max_commute_residual = max(commute_check)

        # Fit BmL as a linear combination of the (up to) 2 transported generators
        # via least squares: BmL ≈ a*cent_transported[0] + b*cent_transported[1]
        A_fit = np.stack([c.flatten() for c in cent_transported], axis=1)  # 64 x 2
        b_fit = BmL_sigma.flatten()
        coeffs_fit, residuals_fit, rank_fit, sv_fit = np.linalg.lstsq(A_fit, b_fit, rcond=None)
        reconstructed = A_fit @ coeffs_fit
        fit_residual = float(np.max(np.abs(reconstructed - b_fit)))
        fit_relative = fit_residual / float(np.max(np.abs(b_fit)))
    else:
        max_commute_residual = None
        coeffs_fit = None
        fit_residual = None
        fit_relative = None

    if hom_dim != 6:
        verdict = "STRUCTURE_MISMATCH"
    elif found_S is None:
        verdict = "NO_ISOMORPHISM_IN_HOM_SPACE"
    elif iso_residual is not None and iso_residual > 1e-6:
        verdict = "ISOMORPHISM_VERIFICATION_FAILED"
    elif fit_relative is not None and fit_relative < 1e-4:
        verdict = "LITERAL_MATCH_FOUND"
    else:
        verdict = "NO_LITERAL_MATCH"

    results = {
        "round": 127,
        "hom_dim": hom_dim,
        "best_det_found": best_det,
        "isomorphism_found": found_S is not None,
        "iso_residual": iso_residual,
        "max_commute_residual_of_transported_centralizer": max_commute_residual,
        "bml_fit_coeffs_real": [complex(c).real for c in coeffs_fit]
        if coeffs_fit is not None
        else None,
        "bml_fit_coeffs_imag": [complex(c).imag for c in coeffs_fit]
        if coeffs_fit is not None
        else None,
        "bml_fit_residual_relative": fit_relative,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Round127 -- is C x 8_v isomorphic to Sigma (S6 spinor) as a complex su(3)-module?")
    print("=" * 92)
    print(f"Hom_C(C x 8_v, Sigma) dimension = {hom_dim} (predict 6, matching G102's Hom_su3=6)")
    print(f"Best |det(S)| found over {n_trials} random trials in Hom space = {best_det:.6e}")
    print(f"Invertible isomorphism found: {found_S is not None}")
    if found_S is not None:
        print(f"Isomorphism residual (S @ A_i @ S^-1 - B_i, max over i): {iso_residual:.3e}")
        print(
            f"Transported centralizer commutes with su(3)_Sigma? residual = {max_commute_residual:.3e}"
        )
        print(f"Fit B-L as combo of transported centralizer: coeffs = {coeffs_fit}")
        print(f"Fit residual (relative to max|BmL|): {fit_relative:.6e}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
