"""Step 4 red-team: can the three triality channels reduce to one physical
degree of freedom via a change of basis?

Re-verifies G102's own S5 result (Hom_so8 off-diagonal = 0, i.e. the three
channels are inequivalent Spin(8) representations, Schur's lemma) directly,
then adds a concrete demonstration: build the "coincidental" su(3)-level
identification Phi between two channels (which exists, since they share
identical su(3) content), and show explicitly that Phi does NOT intertwine
a generic so(8) element -- only elements of g2/su(3) specifically.

Reuses G102's spin_rep_blocks, hom_dim, stabilizer_basis, restrict_to_subalgebra
unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_step4.json"

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

TOL = 1e-8


def hom_basis(rep_a: list[np.ndarray], rep_b: list[np.ndarray]) -> np.ndarray:
    """Same Sylvester-kernel construction as G102.hom_dim, but returns the
    actual nullspace basis (columns = vec(S) for each S with S A_k = B_k S),
    not just its dimension."""
    n_a = rep_a[0].shape[0]
    n_b = rep_b[0].shape[0]
    rows = []
    for a_k, b_k in zip(rep_a, rep_b):
        op = np.kron(a_k.T, np.eye(n_b)) - np.kron(np.eye(n_a), b_k)
        rows.append(op)
    mat = np.vstack(rows)
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(mat.shape) * (s[0] if len(s) else 1.0)))
    return vt[rank:].conj().T  # columns are nullspace basis vectors (n_a*n_b, dim)


def main() -> None:
    vec, sp, sm = G102.spin_rep_blocks()  # each: 28 so(8) generator images, 8x8

    # --- P1: re-verify G102's S5 (Hom_so8 off-diagonal = 0) directly ---
    hom_vec_sp = G102.hom_dim(vec, sp)
    hom_vec_sm = G102.hom_dim(vec, sm)
    hom_sp_sm = G102.hom_dim(sp, sm)
    p1_pass = hom_vec_sp == 0 and hom_vec_sm == 0 and hom_sp_sm == 0

    # positive control, reused from G102: diagonal Hom_so8 = 1 (Schur, self-map is scalar)
    hom_vec_vec = G102.hom_dim(vec, vec)

    # --- Build su(3) and its images in each channel (already-established identical content) ---
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    reps_su3 = G102.restrict_to_subalgebra(su3)  # (v_out, s_out, c_out), su3's 8 gens each
    v_su3, s_su3, _c_su3 = reps_su3

    # --- P2/P3: build the "coincidental" Phi: vec -> sp via su(3)-equivariance,
    # then test it against a GENERIC so(8) element (P2, should fail) and against
    # su(3) itself / g2 (P3, should hold -- load-bearing negative control on the harness) ---
    basis_su3 = hom_basis(v_su3, s_su3)  # nullspace w.r.t. su(3) only
    hom_dim_su3 = basis_su3.shape[1]

    rng = np.random.default_rng(0)
    coeffs = rng.normal(size=hom_dim_su3) + 1j * rng.normal(size=hom_dim_su3)
    phi_flat = basis_su3 @ coeffs
    Phi = phi_flat.reshape(8, 8, order="F")  # column-major, matches vec(AXB) convention
    Phi_norm = float(np.max(np.abs(Phi)))

    # P3 control: does Phi intertwine su(3) itself? (it MUST, by construction)
    su3_residual = max(float(np.max(np.abs(Phi @ a - b @ Phi))) for a, b in zip(v_su3, s_su3))
    p3_pass = su3_residual < TOL * max(1.0, Phi_norm)

    # P2: does Phi intertwine a GENERIC so(8) element (random combination of all 28
    # basis generators, same coefficients applied to vec's own image and sp's own image)?
    rng2 = np.random.default_rng(1)
    generic_coeffs = rng2.normal(size=28)
    X_vec = sum(c * g for c, g in zip(generic_coeffs, vec))
    X_sp = sum(c * g for c, g in zip(generic_coeffs, sp))
    generic_residual = float(np.max(np.abs(Phi @ X_vec - X_sp @ Phi)))
    generic_norm = float(np.max(np.abs(X_vec)))
    p2_pass = generic_residual > 1e-2 * max(1.0, generic_norm) * max(1.0, Phi_norm)

    if not p3_pass:
        verdict = "HARNESS_CONTROL_FAILED"
    elif not p1_pass:
        verdict = "SO8_HOM_NONZERO_REDUNDANCY_WORRY_LIVE"
    elif not p2_pass:
        verdict = "COINCIDENTAL_PHI_SURVIVES_GENERIC_ELEMENT_SURPRISE"
    else:
        verdict = "THREE_CHANNELS_PROVABLY_NOT_REDUNDANT"

    results = {
        "experiment": "step4_channel_redundancy_redteam",
        "hom_so8_vec_sp": hom_vec_sp,
        "hom_so8_vec_sm": hom_vec_sm,
        "hom_so8_sp_sm": hom_sp_sm,
        "hom_so8_vec_vec_positive_control": hom_vec_vec,
        "p1_all_offdiag_zero": p1_pass,
        "hom_dim_su3_vec_sp": hom_dim_su3,
        "phi_norm": Phi_norm,
        "su3_intertwine_residual": su3_residual,
        "p3_su3_control_pass": p3_pass,
        "generic_intertwine_residual": generic_residual,
        "generic_element_norm": generic_norm,
        "p2_generic_fails_as_predicted": p2_pass,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Step 4 red-team: can 3 triality channels reduce to 1 via change of basis?")
    print("=" * 92)
    print(
        f"P1: Hom_so8(vec,sp)={hom_vec_sp}, Hom_so8(vec,sm)={hom_vec_sm}, "
        f"Hom_so8(sp,sm)={hom_sp_sm} (predict 0,0,0)"
    )
    print(f"    positive control Hom_so8(vec,vec)={hom_vec_vec} (predict 1, Schur)")
    print(f"    P1 pass? {p1_pass}")
    print()
    print(f"Hom_su3(vec,sp) dimension = {hom_dim_su3} (room for the 'coincidental' Phi)")
    print(f"Constructed Phi, norm={Phi_norm:.3f}")
    print(f"  su(3)-intertwine residual (P3, must hold): {su3_residual:.2e}  pass={p3_pass}")
    print(
        f"  generic so(8)-intertwine residual (P2, must FAIL): {generic_residual:.4f} "
        f"(element norm {generic_norm:.3f})  pass(fails-as-predicted)={p2_pass}"
    )
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
