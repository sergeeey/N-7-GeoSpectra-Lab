"""OB11(ii), S6-restricted necessary condition: does a first-order (Dirac-operator-
shaped) channel-mixing term between distinct triality channels have any algebraic
room to exist, at the level of pointwise SU(3)-representation theory?

Reuses G102's already-verified octonion/g2/su3 machinery and restrict_to_subalgebra/
hom_dim tools by direct import, unmodified -- matching this project's established
reuse discipline (G102 itself reused G68 the same way; round124 reused G102 the
same way again).

Method (per claim.md, predictions recorded before running):
  P0: extract m = g2/su3 (6-dim complement of su3 within g2, via Frobenius-inner-
      product QR/SVD projection -- the isotropy/tangent representation).
  Control: verify [su3, m] subset m (reductive decomposition), not just assumed.
  P1: quadratic Casimir spectrum of m under su3 (sanity check it looks like the
      6-dim tangent rep, reusing C29's own Casimir technique).
  P2: dim Hom_su3(m tensor channel_i, channel_i) (diagonal) is nonzero -- harness
      sanity control. round59's own already-built single-channel Dirac operator
      IS a nonzero element of exactly this Hom-space (Clifford multiplication
      contracts a tangent index with a spinor index); if this returns 0 the
      harness is broken, not the physics.
  P3: dim Hom_su3(m tensor channel_i, channel_j) for all six off-diagonal pairs
      i != j in {v,s,c} -- the actual question.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ob11ii.json"

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

TOL = 1e-8


def flatten(mats: list[np.ndarray]) -> np.ndarray:
    """Stack matrices as columns of a (64, len) array (Frobenius/Euclidean space)."""
    return np.array([m.flatten() for m in mats]).T


def extract_m_basis(der: list[np.ndarray], su3: list[np.ndarray]) -> list[np.ndarray]:
    """Orthonormal basis of m = g2/su3, the Frobenius-orthogonal complement of
    su3's span within der's span (both already subspaces of so(8), 8x8 matrices).
    """
    Smat = flatten(su3)  # 64 x 8
    Dmat = flatten(der)  # 64 x 14
    Qs, _ = np.linalg.qr(Smat)  # 64 x 8 orthonormal basis of su3's span
    Dmat_perp = Dmat - Qs @ (Qs.T @ Dmat)  # remove su3-component from each der generator
    U, s, _ = np.linalg.svd(Dmat_perp, full_matrices=False)
    rank = int(np.sum(s > 1e-8 * s[0]))
    m_flat = U[:, :rank]
    return [m_flat[:, k].reshape(8, 8) for k in range(rank)]


def su3_action_on_m(
    su3: list[np.ndarray], m_basis: list[np.ndarray]
) -> tuple[list[np.ndarray], float]:
    """rho_m(X_a), 6x6 (or rank x rank) matrices, via ad(X_a) projected onto m's
    own orthonormal basis. Also returns the max residual of the su3-component of
    [X_a, m_k] (should be ~0 -- reductivity control, verified not assumed)."""
    dim_m = len(m_basis)
    m_flat = np.array([m.flatten() for m in m_basis]).T  # 64 x dim_m, orthonormal cols
    su3_flat = flatten(su3)
    Qsu3, _ = np.linalg.qr(su3_flat)

    rho_m = []
    max_su3_leak = 0.0
    for Xa in su3:
        rho_a = np.zeros((dim_m, dim_m))
        for k, mk in enumerate(m_basis):
            comm = Xa @ mk - mk @ Xa
            comm_flat = comm.flatten()
            su3_leak = float(np.max(np.abs(Qsu3.T @ comm_flat)))
            max_su3_leak = max(max_su3_leak, su3_leak)
            coeffs = m_flat.T @ comm_flat  # projection onto orthonormal m-basis
            rho_a[:, k] = coeffs
        rho_m.append(rho_a)
    return rho_m, max_su3_leak


def kron_sum(rho_x: np.ndarray, rho_y: np.ndarray) -> np.ndarray:
    """Leibniz-rule action of a Lie algebra generator on a tensor product rep:
    X |-> rho_x(X) kron I + I kron rho_y(X)."""
    nx, ny = rho_x.shape[0], rho_y.shape[0]
    return np.kron(rho_x, np.eye(ny)) + np.kron(np.eye(nx), rho_y)


def main() -> None:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    n_su3 = len(su3)

    # --- P0: extract m ---
    m_basis = extract_m_basis(der, su3)
    dim_m = len(m_basis)

    # --- reductivity control: [su3, m] subset m ---
    rho_m, max_su3_leak = su3_action_on_m(su3, m_basis)

    # --- P1: Casimir spectrum of m under su3 ---
    C2_m = sum(rho_m[a] @ rho_m[a] for a in range(n_su3))
    C2_m_eigs = np.sort(np.linalg.eigvalsh((C2_m + C2_m.T) / 2))

    # --- channels restricted to su3 (reused, unmodified) ---
    reps_su3 = G102.restrict_to_subalgebra(su3)  # (v_out, s_out, c_out), each 8 gens x 8x8
    labels = ("v", "s", "c")
    channel = dict(zip(labels, reps_su3))

    # --- build tensor reps m (x) channel_i for each channel ---
    tensor_reps = {}
    for lab in labels:
        rho_i = channel[lab]
        tensor_reps[lab] = [kron_sum(rho_m[a], rho_i[a]) for a in range(n_su3)]

    # --- P2 (diagonal, harness control) + P3 (off-diagonal, the actual question) ---
    hom_dims = {}
    for i_lab in labels:
        for j_lab in labels:
            hom_dims[f"{i_lab}-{j_lab}"] = G102.hom_dim(tensor_reps[i_lab], channel[j_lab])

    diag_keys = [f"{lab}-{lab}" for lab in labels]
    offdiag_keys = [f"{a}-{b}" for a in labels for b in labels if a != b]

    diag_vals = [hom_dims[k] for k in diag_keys]
    offdiag_vals = [hom_dims[k] for k in offdiag_keys]

    p0_pass = dim_m == 6
    reductivity_ok = max_su3_leak < TOL
    p2_pass = all(v > 0 for v in diag_vals)
    p3_all_zero = all(v == 0 for v in offdiag_vals)

    if not (p0_pass and reductivity_ok and p2_pass):
        verdict = "HARNESS_CONTROL_FAILED"
    elif p3_all_zero:
        verdict = "X_IJ_ZERO_NECESSARY_CONDITION_PROVEN"
    else:
        verdict = "MIXING_NOT_EXCLUDED_BY_NECESSARY_CONDITION"

    results = {
        "experiment": "ob11ii_channel_mixing_necessary_condition",
        "n_su3_generators": n_su3,
        "dim_m": dim_m,
        "p0_dim_m_is_6": p0_pass,
        "reductivity_max_su3_leak": max_su3_leak,
        "reductivity_ok": reductivity_ok,
        "C2_m_eigenvalues_sorted": C2_m_eigs.tolist(),
        "hom_dims": hom_dims,
        "diag_keys": diag_keys,
        "diag_vals": diag_vals,
        "offdiag_keys": offdiag_keys,
        "offdiag_vals": offdiag_vals,
        "p2_diagonal_all_nonzero": p2_pass,
        "p3_all_offdiag_zero": p3_all_zero,
        "verdict": verdict,
    }

    print("=" * 92)
    print("OB11(ii) S6-restricted necessary condition: channel-mixing Hom-space")
    print("=" * 92)
    print(f"n_su3_generators = {n_su3} (predict 8)")
    print(f"dim(m) = {dim_m} (predict 6)")
    print(f"reductivity check: max su3-leakage in [su3,m] = {max_su3_leak:.2e} (expect ~0)")
    print(f"C2(m) eigenvalues (sorted): {np.round(C2_m_eigs, 6)}")
    print()
    print(f"Hom_su3(m(x)channel_i, channel_j), all 9 pairs: {hom_dims}")
    print(f"  diagonal (P2, harness control): {dict(zip(diag_keys, diag_vals))}")
    print(f"  off-diagonal (P3, the question): {dict(zip(offdiag_keys, offdiag_vals))}")
    print()
    print(f"P2 diagonal all nonzero (harness sound)?  {p2_pass}")
    print(f"P3 all off-diagonal zero (X_ij forced 0)? {p3_all_zero}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
