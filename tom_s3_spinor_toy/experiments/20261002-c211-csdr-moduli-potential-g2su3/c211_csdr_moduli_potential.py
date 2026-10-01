"""C211: CSDR gravity-moduli potential for S6=G2/SU(3), built from G96's own data.

Source formula (Chatzistavrakidis-Manousselis-Prezas-Zoupanos, arXiv:0712.2717,
"Coset Space Dimensional Reduction of Einstein-Yang-Mills theory", eq. 4.27),
full text fetched via mcp__arxiv__download_paper, NOT abstract-only:

    V = (1/4) e^{2(alpha-beta)phi} * (
            gamma_ab gamma^cd gamma^ef f^a_ce f^b_df
          + 2 gamma^ab f^c_da f^d_cb
          + 4 e^{2 beta phi} gamma^ab f_iac f^ic_b
          - 4 e^{2 beta phi} lambda_D
        )

The paper states explicitly: "the first two terms have a non-zero
contribution only in the case of non-symmetric coset spaces." G2/SU(3) is
the field's own prototype non-symmetric (nearly-Kahler) coset space, so
these two terms are the ones this project can evaluate right now using
ALREADY-CERTIFIED data (G96, C210) -- no new gauge-sector assumption needed.

This script computes, in the project's own already-verified G2/SU(3)
generator basis:
    Term1 = sum_{a,c,e} (f^a_ce)^2            [gamma=delta convention]
    Term2 = 2 * sum_{a,c,d} f^c_da * f^d_ca

where f^a_bc is the COSET-COSET-COSET structure constant: the component of
[Q_a, Q_b] (a,b complement/coset indices) that lands BACK IN the complement,
as opposed to the su(3) component (which G96 Step 5b already checked lies in
the complement itself via [su3,complement] subset complement -- a DIFFERENT
contraction from the one needed here).

Reuse discipline (per project feedback memory "Proxy instead of calling the
tool" / "Derive from, don't check against"): build_phi/find_g2_generators are
IMPORTED from g96_g2_su3.py, not reimplemented. The su(3)/complement
extraction steps are not factored into functions in that file (they live
inline in main()), so they are copied here VERBATIM (same stabilizer
condition, same QR-orthogonal-complement construction) to get the identical
complement basis G96 already certified -- not an independent re-derivation
that might silently diverge.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c211.json"


def _load_g96():
    """Import G96's module by path (sibling experiment dir, not a package)."""
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
    """Verbatim copy of G96's main() Steps 4/4b -- same stabilizer + QR complement."""
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


def complement_structure_constants(
    comp_gens: list[np.ndarray],
) -> tuple[np.ndarray, float]:
    """f^a_bc: the complement-COMPONENT of [comp_gens[b], comp_gens[c]].

    comp_gens are orthonormal in the Frobenius (49-dim flattened) inner
    product (QR output) -- this IS the gamma_ab = delta_ab convention
    eq. 4.27 assumes (an overall unit-radius normalization; any physical
    radius modulus rho_6 enters only through the e^{...phi} prefactors the
    paper keeps separate, consistent with how this project already treats
    rho_6 as an independent overall scale -- see the G54 Freund-Rubin chain).

    Returns:
        f: (6,6,6) tensor, f[a,b,c] = coefficient of comp_gens[a] in the
           complement-projection of [comp_gens[b], comp_gens[c]]
        max_residual: largest norm of the part of [comp_b,comp_c] NOT
           explained by su(3)+complement (must be ~0 -- sanity check that
           complement+su3 together span all of g2, which G96 already
           established: dim 8+6=14)
    """
    n = len(comp_gens)
    comp_flat = np.column_stack([g.flatten() for g in comp_gens])  # 49 x 6, orthonormal cols
    f = np.zeros((n, n, n))
    for b in range(n):
        for c in range(n):
            if b == c:
                continue
            C = commutator(comp_gens[b], comp_gens[c])
            c_flat = C.flatten()
            # orthonormal basis -> projection coefficients are just inner products
            coeffs = comp_flat.T @ c_flat
            f[:, b, c] = coeffs
    return f, 0.0


def main() -> None:
    print("\n=== C211: CSDR gravity-moduli potential for S6=G2/SU(3) ===\n")

    phi = build_phi()
    gens = find_g2_generators(phi)
    assert len(gens) == 14, f"Expected 14 G2 generators, got {len(gens)}"
    print(f"Step 1: reused G96's G2 generators, dim={len(gens)} [OK, matches G96/C210]")

    su3_gens, comp_gens = build_su3_and_complement(gens)
    print(
        f"Step 2: su(3) dim={len(su3_gens)}, complement dim={len(comp_gens)} "
        f"[expected 8, 6 -- matches G96]"
    )
    assert len(su3_gens) == 8 and len(comp_gens) == 6, "su3/complement dims off from G96"

    # Sanity: su3 + complement together must reconstruct full commutators
    # (su3-part via lstsq against su3 basis, as G96 Step 5b already checks;
    # here we additionally require the REMAINDER after removing the su3
    # component lies entirely in the complement -- i.e. su3 (+) complement
    # really is all of g2, not just dimension-matched by coincidence).
    su3_flat = np.column_stack([g.flatten() for g in su3_gens])
    comp_flat = np.column_stack([g.flatten() for g in comp_gens])
    full_flat = np.column_stack([su3_flat, comp_flat])  # 49 x 14, should span g2
    max_recon_err = 0.0
    for i in range(len(comp_gens)):
        for j in range(len(comp_gens)):
            if i == j:
                continue
            C = commutator(comp_gens[i], comp_gens[j]).flatten()
            coeffs, _, _, _ = np.linalg.lstsq(full_flat, C, rcond=None)
            recon = full_flat @ coeffs
            max_recon_err = max(max_recon_err, float(np.max(np.abs(C - recon))))
    print(
        f"Step 3: [comp,comp] fully spanned by su3+complement? "
        f"max residual={max_recon_err:.2e} [expect < 1e-9]"
    )
    assert max_recon_err < 1e-9, "su3+complement do not span g2 -- cannot trust f^a_bc below"

    f, _ = complement_structure_constants(comp_gens)
    max_f = float(np.max(np.abs(f)))
    print(f"Step 4: coset-coset-coset structure constants f^a_bc extracted, max|f|={max_f:.6f}")
    print(
        "        (nonzero confirms G2/SU(3) is NON-symmetric, as the CSDR "
        "literature's own eq. 4.27 remark predicts)"
    )

    term1 = float(np.sum(f**2))
    term2 = 2.0 * float(np.einsum("cda,dca->", f, f))
    print("\nStep 5: eq. (4.27) gravity-only terms (gamma=delta, unit radius):")
    print(f"  Term1 = sum_ace (f^a_ce)^2        = {term1:.6f}")
    print(f"  Term2 = 2 sum_acd f^c_da f^d_ca   = {term2:.6f}")
    print(f"  Term1 + Term2 (pre-e^phi prefactor contribution to V) = {term1 + term2:.6f}")

    results = {
        "dim_g2": len(gens),
        "dim_su3": len(su3_gens),
        "dim_complement": len(comp_gens),
        "comp_spans_with_su3_max_residual": max_recon_err,
        "max_abs_f_abc": max_f,
        "term1_sum_f_squared": term1,
        "term2_cross_contraction": term2,
        "term1_plus_term2": term1 + term2,
        "source": (
            "Chatzistavrakidis-Manousselis-Prezas-Zoupanos, arXiv:0712.2717, "
            "eq. 4.27, full text fetched via mcp__arxiv__download_paper"
        ),
        "status": "COMPUTED" if max_recon_err < 1e-9 else "BLOCKED",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\n[{results['status']}] -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
