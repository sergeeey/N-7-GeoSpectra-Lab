"""C83 -- the genuinely untested remainder of C78's 20-dim so(8) complement.

Scoping finding (see claim.md): so(4)_1+so(4)_2 (round119's 12 generators,
tested in C77/C79-C82) has an exact 1-dim intersection with su(3) itself
-- a specific linear combination that commutes with D exactly, even
though C77 correctly found no individual basis generator does. This
means so(4)_1+so(4)_2's effective "shadow" within C78's 20-dim complement
has rank 11, not 12 -- leaving a genuinely untested 9-dimensional piece.

This round: (1) re-verifies the overlap finding and the 9-dim remaining
basis computation exactly as scoped, (2) tests it in three groups of 3
generators (SVD-ordered, reproducible) via C81's exact corrected
(raw-kernel-excluded) methodology, using round67's Z_i unmodified.

Reuses C81's run_for_triple, C79's get_bridge_to_sigma/leibniz_matrix,
C78's G102.so8_basis, C70's su3_g102_on_channel_v, round59's
build_clifford/NOMIZU, C73's build_numeric_dirac, all unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c83.json"
TOL = 1e-8


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C81 = load_module(
    "c81_raw_kernel_excluded_retest",
    HERE.parent / "20260811-c81-raw-kernel-excluded-retest" / "c81_raw_kernel_excluded_retest.py",
)
C79 = C81.C79


def find_su3_overlap_direction(so4_flat: np.ndarray, su3_flat: np.ndarray) -> dict:
    """P1: the specific linear combination of so4_all's 12 generators that
    lies exactly in su(3) (commutes with D), found via a joint SVD null-space."""
    M = np.hstack([so4_flat.T, -su3_flat.T])
    _u, s, vt = np.linalg.svd(M)
    null_idx = int(np.argmin(s))
    null_vec = vt[null_idx]
    c1 = null_vec[:12].real
    c2 = null_vec[12:].real
    overlap_dir = (so4_flat.T @ c1).reshape(8, 8)
    residual_check = float(np.max(np.abs((so4_flat.T @ c1) - (su3_flat.T @ c2))))
    return {
        "smallest_singular_value": float(s[null_idx]),
        "residual_check": residual_check,
        "c1_coeffs": c1.tolist(),
        "overlap_direction": overlap_dir,
    }


def build_remaining_complement_basis(
    so4_flat: np.ndarray, complement_basis: np.ndarray
) -> tuple[np.ndarray, dict]:
    """P2: rank-aware (SVD-based, not naive QR) extraction of the genuinely
    untested part of the complement, after removing so(4)_1+so(4)_2's own
    shadow within it."""
    Q_complement, _ = np.linalg.qr(complement_basis.T)  # (64, 20)
    shadow_coords = Q_complement.conj().T @ so4_flat.T  # (20, 12)
    u_s, s_s, _vt_s = np.linalg.svd(shadow_coords)
    rho = int(np.sum(s_s > 1e-8 * s_s[0]))
    new_onb = u_s[:, rho:]  # (20, 20-rho)
    new_generators_flat = new_onb.T @ Q_complement.T  # (20-rho, 64)
    overlap_check = float(np.max(np.abs(shadow_coords.conj().T @ new_onb)))
    gram = new_generators_flat.conj() @ new_generators_flat.T
    gram_identity_residual = float(np.max(np.abs(gram - np.eye(new_generators_flat.shape[0]))))
    return new_generators_flat, {
        "shadow_singular_values": s_s.tolist(),
        "rho": rho,
        "remaining_dim": int(new_generators_flat.shape[0]),
        "overlap_check": overlap_check,
        "gram_identity_residual": gram_identity_residual,
    }


def build_complement_basis(u_v_inv, u_v, d_mat) -> tuple[np.ndarray, int]:
    G102 = C79.C70.C68.G102
    so8 = G102.so8_basis()
    so8_flat = np.array([g.reshape(-1) for g in so8]).astype(complex)
    comm_vectors = []
    for g in so8:
        g_sigma = u_v_inv @ g.astype(complex) @ u_v
        leib = C79.leibniz_matrix(g_sigma)
        comm = d_mat @ leib - leib @ d_mat
        comm_vectors.append(comm.reshape(-1))
    comm_matrix = np.array(comm_vectors).T  # (4096, 28)
    _u_svd, s_svd, vh_svd = np.linalg.svd(comm_matrix)
    rank = int(np.sum(s_svd > TOL * max(1.0, s_svd[0])))
    complement_coeffs = vh_svd[:rank].conj()
    complement_basis = complement_coeffs @ so8_flat  # (20, 64)
    return complement_basis, rank


def main() -> None:
    C70 = C79.C70
    C73 = C79.C73
    R59 = C79.R59

    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_flat = np.array([g.reshape(-1) for g in so4_all]).astype(complex)
    gens_v = C70.C68.su3_g102_on_channel_v()
    su3_flat = np.array([g.reshape(-1) for g in gens_v]).astype(complex)

    print("=== P1: su(3) cap so(4)_1+so(4)_2 overlap direction ===")
    overlap = find_su3_overlap_direction(so4_flat, su3_flat)
    print(f"smallest singular value: {overlap['smallest_singular_value']:.3e}")
    print(f"residual check: {overlap['residual_check']:.3e}")

    u_v, bridge_sanity = C79.get_bridge_to_sigma()
    print("bridge_sanity:", bridge_sanity)
    u_v_inv = np.linalg.inv(u_v)
    E = R59.build_clifford(conj=False)
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)

    g_sigma_overlap = u_v_inv @ overlap["overlap_direction"].astype(complex) @ u_v
    leib_overlap = C79.leibniz_matrix(g_sigma_overlap)
    comm_overlap = d_mat @ leib_overlap - leib_overlap @ d_mat
    overlap_commutator = float(np.max(np.abs(comm_overlap)))
    print(f"||[D, Leibniz(overlap_dir)]|| = {overlap_commutator:.3e} (expect ~0)")

    print("\n=== P2: build the 20-dim complement, extract the 9-dim remainder ===")
    complement_basis, complement_rank = build_complement_basis(u_v_inv, u_v, d_mat)
    print(f"complement dim: {complement_rank} (expect 20)")
    remaining_generators, remaining_info = build_remaining_complement_basis(
        so4_flat, complement_basis
    )
    print(f"rho (so4 shadow rank): {remaining_info['rho']} (expect 11)")
    print(f"remaining dim: {remaining_info['remaining_dim']} (expect 9)")
    print(f"overlap check: {remaining_info['overlap_check']:.3e}")
    print(f"gram identity residual: {remaining_info['gram_identity_residual']:.3e}")

    d_s3_scalar = float(C79.sp.Rational(1, 2) * C79.ROUND67.calibrate_h_H())
    groups = {
        "group_0_1_2": remaining_generators[0:3].reshape(3, 8, 8),
        "group_3_4_5": remaining_generators[3:6].reshape(3, 8, 8),
        "group_6_7_8": remaining_generators[6:9].reshape(3, 8, 8),
    }

    group_results = {}
    for label, triple in groups.items():
        print(f"\n=== Testing {label} via C81's corrected methodology ===")
        result = C81.run_for_triple(triple, label, d_mat, d_s3_scalar)
        group_results[label] = result

    no_genuine_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in group_results.values()
    )

    results = {
        "overlap_finding": {
            "smallest_singular_value": overlap["smallest_singular_value"],
            "residual_check": overlap["residual_check"],
            "c1_coeffs": overlap["c1_coeffs"],
            "commutator_with_D": overlap_commutator,
        },
        "complement_dim": complement_rank,
        "remaining_complement_info": remaining_info,
        "group_results": group_results,
        "no_genuine_signal_found": bool(no_genuine_signal),
        "conclusion": (
            "so(4)_1+so(4)_2 has an exact 1-dim overlap with su(3) (found, "
            f"verified commutator {overlap_commutator:.3e}). Genuinely "
            f"untested complement: {remaining_info['remaining_dim']} dims. "
            + (
                "Tested in 3 groups of 3 via C81's corrected methodology: "
                "NO genuine crossing in any group. This completes the FULL "
                "20-dim so(8) complement's coverage for this specific "
                "Z_i-coupling construction on S3's n=0 sector -- every "
                "candidate tested, all clean nulls."
                if no_genuine_signal
                else "At least one group shows a crossing surviving raw-"
                "kernel exclusion -- the first candidate anywhere in this "
                "project's so(8) search to do so, requiring the same extra "
                "scrutiny as any unexpectedly positive result before being "
                "trusted."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
