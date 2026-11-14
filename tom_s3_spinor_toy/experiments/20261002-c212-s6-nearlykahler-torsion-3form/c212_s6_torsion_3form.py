"""C212: explicit nearly-Kahler torsion 3-form on S6=G2/SU(3).

Source (full text fetched via mcp__arxiv__download_paper, verified against
the primary not abstract-only): Agricola, Borowka, Friedrich, "S6 and the
geometry of nearly Kahler 6-manifolds", arXiv:1707.08591, Proposition 4.2:

    T^c(X,Y,Z) = -<N,(X x Y) x Z>

where X,Y,Z are tangent vectors to S6 at the point N in R^7=Im(O), and
"x" is the octonion cross product A x B = (1/2)(AB - BA), restricted to
Im(O). This is the torsion 3-form of S6's characteristic (= canonical,
by Proposition 4.2) connection -- the SAME object this project's own
nearly-Kahler/characteristic-connection literature (Agricola 2002,
Agricola-Hofmann-Lawn 2003) already engages with for S3's analogous
structure, just never computed explicitly for the S6 factor.

Reuse discipline: build_phi() (the octonion Fano-plane structure tensor,
which IS the cross-product structure constant: e_i x e_j = phi_ijk e_k)
and the su(3)/complement generator split are imported from g96_g2_su3.py
via importlib (same pattern as C211) -- not rebuilt.

Tangent-space identification: at the base point N (G96's own "preferred
direction" e6, 0-indexed 7th basis vector), the tangent space T_N(S6) is
identified with g2's complement m via the orbit map K |-> K@N (standard
reductive-space construction) -- NOT an independent new construction,
the same complement G96 already certified as the SU(3) representation
3+3bar.

Positive control (MANDATORY before trusting any T_abc number, per this
project's own "instrument calibration before discovery" discipline,
C201): Gray's theorem (cited in the source paper, Theorem 2/G76) states
the torsion of a nearly-Kahler 6-manifold's characteristic connection is
TOTALLY ANTISYMMETRIC. T_abc is checked for total antisymmetry
numerically -- if that check fails, the formula/cross-product
implementation has a bug and the numeric magnitude must not be trusted.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c212.json"


def _load_g96():
    g96_path = HERE.parent / "20260626-g96-s6-g2-su3" / "g96_g2_su3.py"
    spec = importlib.util.spec_from_file_location("g96_g2_su3", g96_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_g96 = _load_g96()
build_phi = _g96.build_phi
find_g2_generators = _g96.find_g2_generators
commutator = _g96.commutator


def build_su3_and_complement(
    gens: list[np.ndarray],
) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Verbatim copy of G96's main() Steps 4/4b (same as C211's helper)."""
    e6 = np.zeros(7)
    e6[6] = 1.0

    A_stab = np.column_stack([G @ e6 for G in gens])
    _, sv_stab, Vt_stab = np.linalg.svd(A_stab, full_matrices=True)
    rank_stab = int(np.sum(sv_stab > 1e-10))
    null_coeffs = Vt_stab[rank_stab:]

    gen_matrix = np.array([G.flatten() for G in gens])
    su3_gens_flat = null_coeffs @ gen_matrix
    su3_gens = [row.reshape(7, 7) for row in su3_gens_flat]

    Q_su3, _ = np.linalg.qr(su3_gens_flat.T, mode="reduced")
    comp_vecs = []
    for G in gens:
        g_flat = G.flatten()
        proj = Q_su3 @ (Q_su3.T @ g_flat)
        residual = g_flat - proj
        if np.linalg.norm(residual) > 1e-10:
            comp_vecs.append(residual)
    C_mat = np.column_stack(comp_vecs)
    Q_c, R_c = np.linalg.qr(C_mat, mode="reduced")
    n_comp = int(np.sum(np.abs(np.diag(R_c)) > 1e-10))
    comp_gens = [Q_c[:, k].reshape(7, 7) for k in range(n_comp)]

    return su3_gens, comp_gens


def octonion_cross(phi: np.ndarray, A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """(A x B)_k = sum_ij phi[i,j,k] A_i B_j, from e_i x e_j = phi_ijk e_k."""
    return np.einsum("ijk,i,j->k", phi, A, B)


def main() -> None:
    print("\n=== C212: nearly-Kahler torsion 3-form on S6=G2/SU(3) ===\n")

    phi = build_phi()
    gens = find_g2_generators(phi)
    assert len(gens) == 14, f"Expected 14 G2 generators, got {len(gens)}"

    su3_gens, comp_gens = build_su3_and_complement(gens)
    assert len(su3_gens) == 8 and len(comp_gens) == 6, (
        "su3/complement dims off from G96"
    )
    print(f"Step 1: reused G96's complement basis, dim={len(comp_gens)} [OK]")

    N = np.zeros(7)
    N[6] = 1.0

    tangent = np.array([G @ N for G in comp_gens])
    rank_tangent = int(np.sum(np.linalg.svd(tangent, compute_uv=False) > 1e-10))
    print(
        f"Step 2: tangent vectors v_a = K_a @ N built, rank={rank_tangent} [expect 6]"
    )
    assert rank_tangent == 6, (
        "Tangent vectors degenerate -- complement does not act freely at N"
    )

    # Sanity: cross product is antisymmetric and orthogonal to both factors
    cross_antisym_err = 0.0
    cross_orth_err = 0.0
    for a in range(6):
        for b in range(6):
            cab = octonion_cross(phi, tangent[a], tangent[b])
            cba = octonion_cross(phi, tangent[b], tangent[a])
            cross_antisym_err = max(cross_antisym_err, float(np.max(np.abs(cab + cba))))
            cross_orth_err = max(
                cross_orth_err,
                abs(float(np.dot(cab, tangent[a]))),
                abs(float(np.dot(cab, tangent[b]))),
            )
    print(
        f"Step 3: cross product sanity -- antisymmetry err={cross_antisym_err:.2e}, "
        f"orthogonality err={cross_orth_err:.2e} [expect ~0 both]"
    )
    assert cross_antisym_err < 1e-10 and cross_orth_err < 1e-10, (
        "Cross product implementation bug"
    )

    # Torsion 3-form: T_abc = -<N, (v_a x v_b) x v_c>
    T = np.zeros((6, 6, 6))
    for a in range(6):
        for b in range(6):
            cross_ab = octonion_cross(phi, tangent[a], tangent[b])
            for c in range(6):
                T[a, b, c] = -float(
                    np.dot(N, octonion_cross(phi, cross_ab, tangent[c]))
                )

    # MANDATORY positive control: Gray's theorem says T is totally antisymmetric
    max_asym_err = 0.0
    for a in range(6):
        for b in range(6):
            for c in range(6):
                max_asym_err = max(max_asym_err, abs(T[a, b, c] + T[b, a, c]))
                max_asym_err = max(max_asym_err, abs(T[a, b, c] + T[a, c, b]))
    print(
        f"Step 4 [POSITIVE CONTROL]: total antisymmetry of T, max err={max_asym_err:.2e} "
        f"[Gray's theorem requires ~0 -- if this fails, DO NOT TRUST the magnitude below]"
    )

    norm_T_sq = float(np.sum(T**2))
    max_abs_T = float(np.max(np.abs(T)))

    verdict = "PASS_CALIBRATED" if max_asym_err < 1e-9 else "BLOCKED_CALIBRATION_FAILED"
    print(
        f"\nStep 5: |T|^2 = sum T_abc^2 = {norm_T_sq:.6f}, max|T_abc| = {max_abs_T:.6f}"
    )
    print(f"[{verdict}]")

    results = {
        "dim_complement": len(comp_gens),
        "tangent_rank": rank_tangent,
        "cross_antisym_err": cross_antisym_err,
        "cross_orth_err": cross_orth_err,
        "torsion_total_antisymmetry_err": max_asym_err,
        "norm_T_squared": norm_T_sq,
        "max_abs_T_component": max_abs_T,
        "source": (
            "Agricola-Borowka-Friedrich, arXiv:1707.08591, Prop 4.2, "
            "full text fetched via mcp__arxiv__download_paper"
        ),
        "status": verdict,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"-> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
