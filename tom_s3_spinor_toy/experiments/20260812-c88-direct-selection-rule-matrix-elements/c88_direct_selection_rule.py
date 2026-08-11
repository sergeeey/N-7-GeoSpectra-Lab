"""C88 -- corrects and supersedes C87's eps-sweep methodology with a
direct, robust selection-rule matrix-element computation.

WHY THIS ROUND EXISTS (an integrity correction, not smoothed over):
while scoping the next round after C87, a direct check found
`d_joint_base` (the operator C86/C87 fed to `np.linalg.eigvalsh`) had
Hermiticity residual 0.0 at k=1 (C86, valid) but 2.0 at k=2 (C87,
INVALID) -- `eigvalsh` silently assumes Hermitian input and only reads
the Hermitian part, so C87's own "clean NULL" conclusion, while possibly
still correct, was reached via a computation that could have produced
ARBITRARY wrong eigenvalues, not merely imprecise ones. Root cause:
Meier's own `|p>` basis (symmetrized tensor products) is not orthonormal
-- individually, `l_{e3}` (repaired) is anti-Hermitian at k=1 (where it
coincides with `l_{e3}` literal) but genuinely NOT anti-Hermitian at
k=2, a real, structural feature of the construction, not a bug in the
repair. D-bar's own eigenvalues remain guaranteed real regardless (via
the algebraic quadratic identity certified in C85, independent of any
Hermiticity property) -- but `eigvalsh`-based DOWNSTREAM computations
(the joint eps-sweep) are not trustworthy wherever Hermiticity fails.

This round replaces the indirect eps-sweep crossing test with the
DIRECT thing the external reviewer's own C84B framing asked for:
compute the actual matrix elements <n',m'|T|n,m> connecting D-bar's own
eigenspaces. This needs no Hermiticity assumption at all -- D-bar is
guaranteed DIAGONALIZABLE (not merely real-eigenvalued) by its own
minimal polynomial (D-bar+k)(D-bar-(k+2))=0, which has distinct roots,
so a general (non-Hermitian) eigendecomposition gives a valid, complete
eigenbasis, and transforming any operator into that eigenbasis via
similarity (S^-1 X S, not the unitary S^dagger X S that would only be
valid for a normal matrix) correctly reads off inter-eigenspace matrix
elements regardless of whether S is unitary.

This is a genuinely cleaner test of the selection rule than the eps-
sweep ever was: the S3-side question ("does Z_i connect these two
eigenspaces") does not even require building the S6 factor at all.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c88.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C85 = load_module(
    "c85_certification",
    HERE.parent / "20260812-c85-peter-weyl-representation-certification" / "c85_certification.py",
)
C86 = load_module(
    "c86_full_k1_coupling",
    HERE.parent / "20260812-c86-full-k1-level-coupling-test" / "c86_full_k1_coupling.py",
)
ROUND67 = C86.ROUND67


def build_dbar_pr_numeric(k: int) -> np.ndarray:
    right_mult = [
        C85.right_mult_matrix_on_ab(u) for u in [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    ]
    l1, l2, l3 = C85.build_l_matrices(k, "repaired")
    dbar_pr = C85.build_dbar([l1, l2, l3], right_mult)
    return np.array(dbar_pr.evalf().tolist(), dtype=complex)


def direct_selection_rule_test(k: int) -> dict:
    """[VERIFIED-numpy] Diagonalize D-bar_pr via a GENERAL (non-Hermitian)
    eigendecomposition -- valid because D-bar is guaranteed diagonalizable
    by its own quadratic minimal polynomial, certified in C85 -- then
    transform Z_i into D-bar's own eigenbasis via similarity (S^-1 Z_i S)
    and read off the block connecting the "-k" eigenspace (physical n=k,
    sigma=-1) to the "+k+2" eigenspace (physical n=k-1, sigma=+1)."""
    dbar_pr = build_dbar_pr_numeric(k)
    dim_pr = dbar_pr.shape[0]

    eigvals, eigvecs = np.linalg.eig(dbar_pr)
    max_imag_part = float(np.max(np.abs(eigvals.imag)))
    eigvals_real = eigvals.real

    minus_k_mask = np.abs(eigvals_real - (-k)) < 1e-6
    plus_k2_mask = np.abs(eigvals_real - (k + 2)) < 1e-6
    minus_dim = int(np.sum(minus_k_mask))
    plus_dim = int(np.sum(plus_k2_mask))

    # sanity: eigenvector matrix S must be invertible (guaranteed by
    # diagonalizability) -- verify the reconstruction S @ diag(eigvals) @
    # S^-1 actually reproduces dbar_pr, catching any numerical failure.
    s_inv = np.linalg.inv(eigvecs)
    reconstruction_residual = float(np.max(np.abs(eigvecs @ np.diag(eigvals) @ s_inv - dbar_pr)))

    z_gens = [np.array(z.tolist(), dtype=complex) for z in ROUND67.clifford_generators()]
    dim_p = dim_pr // 2
    I_p = np.eye(dim_p, dtype=complex)

    off_diag_norms = []
    for i, z in enumerate(z_gens):
        z_pr = np.kron(I_p, z)  # matches D-bar's own (p,r) Kronecker convention
        z_eigbasis = s_inv @ z_pr @ eigvecs
        block = z_eigbasis[np.ix_(plus_k2_mask, minus_k_mask)]  # <+k+2 | Z_i | -k>
        off_diag_norms.append(
            {
                "generator": f"Z_{i + 1}",
                "block_shape": list(block.shape),
                "frobenius_norm": float(np.linalg.norm(block)),
                "max_abs_entry": float(np.max(np.abs(block))) if block.size else 0.0,
            }
        )

    return {
        "k": k,
        "dim_pr": dim_pr,
        "max_imaginary_part_of_eigenvalues": max_imag_part,
        "reconstruction_residual": reconstruction_residual,
        "minus_k_eigenspace_dim": minus_dim,
        "plus_k2_eigenspace_dim": plus_dim,
        "target_minus_dim": k + 2,
        "target_plus_dim": k,
        "dims_match_target": (minus_dim == k + 2) and (plus_dim == k if k > 0 else True),
        "off_diagonal_blocks": off_diag_norms,
        "all_generators_block_is_zero": all(b["frobenius_norm"] < 1e-8 for b in off_diag_norms),
    }


def main() -> None:
    print("=== Direct selection-rule test: does Z_i connect D-bar's own eigenspaces? ===")
    print("(No S6, no eps-sweep, no Hermiticity assumption -- pure S3-side algebra)\n")

    results = {}
    for k in (1, 2, 3, 4):
        r = direct_selection_rule_test(k)
        results[str(k)] = r
        print(f"k={k}:")
        print(
            f"  eigenvalues real (max |Im|={r['max_imaginary_part_of_eigenvalues']:.2e}), "
            f"reconstruction residual={r['reconstruction_residual']:.2e}"
        )
        print(
            f"  eigenspace dims: -k={r['minus_k_eigenspace_dim']} (target {r['target_minus_dim']}), "
            f"+k+2={r['plus_k2_eigenspace_dim']} (target {r['target_plus_dim']}), "
            f"match={r['dims_match_target']}"
        )
        for b in r["off_diagonal_blocks"]:
            print(f"  {b['generator']}: ||<+k+2|Z|-k>||_F = {b['frobenius_norm']:.6e}")
        print(f"  all_generators_block_is_zero: {r['all_generators_block_is_zero']}\n")

    all_dims_match = all(r["dims_match_target"] for r in results.values())
    all_zero = all(r["all_generators_block_is_zero"] for r in results.values())

    print("=== Summary ===")
    print(f"all eigenspace dimensions match round67's own target (k=1..4): {all_dims_match}")
    print(
        f"Z_i's own matrix elements between adjacent-n eigenspaces are ALL zero (k=1..4): {all_zero}"
    )

    out = {
        "results": results,
        "all_dims_match": all_dims_match,
        "z_i_connects_adjacent_n_eigenspaces": not all_zero,
        "verdict": (
            "Z_I_ITSELF_NEVER_CONNECTS_ADJACENT_N_EIGENSPACES__T_S_S3_SIDE_IS_STRUCTURALLY_BLOCK_DIAGONAL"
            if all_zero
            else "Z_I_HAS_NONZERO_MATRIX_ELEMENTS_BETWEEN_ADJACENT_N_EIGENSPACES__REQUIRES_FURTHER_CHECK"
        ),
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")
    print(f"\nVERDICT: {out['verdict']}")


if __name__ == "__main__":
    main()
