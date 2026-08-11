"""C78 -- exhaustive so(8) commutant of round59's physical D.

Genuinely new construction (not another candidate test): instead of
proposing a specific subalgebra of so(8) (round124's su(3)+u(1)+u(1) in
C75, round119's SO(4)+SO(4) in C77) and checking whether it commutes with
D, this round computes the FULL commutant of D within so(8) directly --
transport G102's complete 28-generator so8_basis() to Sigma via C70's
verified U_v, then solve for the linear subspace of so(8) coefficients
whose transported generator commutes with D via a single SVD null-space
computation.

If dim(commutant) = 8 (= su(3) exactly), this is an EXHAUSTIVE statement:
no subalgebra of so(8), of any dimension or structure, commutes with the
physical D except su(3) itself -- closing L3B_SPIN8_INTERFACE_SPEC.md
section 1.5's own "Dynamics" open item completely, not just for the two
candidates C75/C77 happened to test.

Reuses G102's so8_basis/derivation_basis/stabilizer_basis, C70's
run_direct_solve/hom_basis/search_nonzero_intertwiner, round59's
build_clifford/leibniz/NOMIZU, and C73's build_numeric_dirac, all
unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c78.json"
TOL = 1e-8


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C70 = load_module(
    "c70_bridge_diagnostics",
    HERE.parent
    / "20260811-c70-independent-bridge-fingerprint-and-direct-solve"
    / "c70_bridge_diagnostics.py",
)
C73 = load_module(
    "c73_dirac_battery",
    HERE.parent / "20260811-c73-round59-real-twisted-dirac-battery" / "c73_dirac_battery.py",
)
R59 = C70.C68.R59
G102 = C70.C68.G102


def get_bridge_to_sigma() -> tuple[np.ndarray, list[np.ndarray], dict]:
    """C70's own bridge Phi_v -> M_matrices -> U_v, reused unmodified."""
    gens_v = C70.C68.su3_g102_on_channel_v()
    gens_r59 = C70.C68.to_numpy_su3_r59()
    solve_v = C70.run_direct_solve(gens_r59, gens_v, n_trials=3, norm_weight=5.0, seed=42)
    phi_v = solve_v["best"]["phi"]
    phi_inv = np.linalg.inv(phi_v)
    m_matrices = [sum(phi_inv[a, k] * gens_r59[a] for a in range(8)) for k in range(8)]
    basis = C70.C68.hom_basis(m_matrices, gens_v)
    u_v, best_det = C70.C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)
    u_v_inv = np.linalg.inv(u_v)
    residual = max(
        float(np.max(np.abs(u_v @ m_matrices[k] @ u_v_inv - gens_v[k]))) for k in range(8)
    )
    return u_v, m_matrices, {"u_v_det": best_det, "intertwining_residual": residual}


def su3_in_span_of_so8(m_matrices: list[np.ndarray], so8: list[np.ndarray]) -> float:
    """Sanity check for P1: known su(3) generators (on channel_v, via su(3)_g102)
    must lie exactly in span(so8_basis()). Uses the su(3) generators on
    channel_v directly (not the Sigma-side M_matrices) since so8_basis() is
    itself expressed on channel_v."""
    gens_v = C70.C68.su3_g102_on_channel_v()
    so8_flat = np.array([g.reshape(-1) for g in so8])  # (28, 64)
    max_resid = 0.0
    for g in gens_v:
        coeffs, _, _, _ = np.linalg.lstsq(so8_flat.T, g.reshape(-1), rcond=None)
        recon = so8_flat.T @ coeffs
        max_resid = max(max_resid, float(np.max(np.abs(recon - g.reshape(-1)))))
    return max_resid


def leibniz_matrix(gen_on_sigma: np.ndarray) -> np.ndarray:
    return np.array(R59.leibniz(sp.Matrix(gen_on_sigma)).evalf(), dtype=complex)


def main() -> None:
    print("=== Step 1: so(8) basis sanity (28 generators, su(3) inside span) ===")
    so8 = G102.so8_basis()
    print(f"len(so8_basis()) = {len(so8)} (expect 28)")
    su3_residual = su3_in_span_of_so8(None, so8)
    print(f"max residual, su(3) generators reconstructed from so(8) span: {su3_residual:.3e}")

    print("\n=== Step 2: C70's bridge to Sigma ===")
    u_v, m_matrices, bridge_sanity = get_bridge_to_sigma()
    print(bridge_sanity)
    u_v_inv = np.linalg.inv(u_v)

    print("\n=== Step 3: build D, positive control (su(3) already known to commute) ===")
    E = R59.build_clifford(conj=False)
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)
    su3_leibniz = [leibniz_matrix(m) for m in m_matrices]
    max_su3_comm = max(float(np.max(np.abs(d_mat @ leib - leib @ d_mat))) for leib in su3_leibniz)
    print(f"max |[D, Leibniz(su3_gen)]| (expect ~0): {max_su3_comm:.3e}")

    print("\n=== Step 4: transport all 28 so(8) generators, build commutator map ===")
    d_norm = float(np.linalg.norm(d_mat))
    comm_vectors = []
    for i, g in enumerate(so8):
        g_sigma = u_v_inv @ g.astype(complex) @ u_v
        leib = leibniz_matrix(g_sigma)
        comm = d_mat @ leib - leib @ d_mat
        comm_vectors.append(comm.reshape(-1))
        if (i + 1) % 7 == 0:
            print(f"  ...processed {i + 1}/28 generators")
    comm_matrix = np.array(comm_vectors).T  # (4096, 28): columns = commutator of each generator

    print("\n=== Step 5: null space of the commutator map (the exhaustive commutant) ===")
    _u_svd, s_svd, vh_svd = np.linalg.svd(comm_matrix)
    rel_tol = TOL * max(1.0, s_svd[0])
    rank = int(np.sum(s_svd > rel_tol))
    commutant_dim = 28 - rank
    print(f"singular values: {np.round(s_svd, 6)}")
    print(f"rank(comm_matrix) = {rank}, commutant_dim = 28 - rank = {commutant_dim}")

    commutant_coeffs = vh_svd[rank:].conj()  # rows: coefficients over the 28 so(8) generators
    print(f"\ncommutant_dim = {commutant_dim} (predicted 8, = su(3))")

    print("\n=== Step 6: is su(3) exactly recovered as the commutant (or a subspace of it)? ===")
    gens_v = C70.C68.su3_g102_on_channel_v()
    so8_flat = np.array([g.reshape(-1) for g in so8])
    su3_coeffs = []
    for g in gens_v:
        coeffs, _, _, _ = np.linalg.lstsq(so8_flat.T, g.reshape(-1), rcond=None)
        su3_coeffs.append(coeffs)
    su3_coeffs = np.array(su3_coeffs)  # (8, 28)

    if commutant_dim > 0:
        proj_resid = []
        for row in su3_coeffs:
            coeffs_in_commutant, _, _, _ = np.linalg.lstsq(
                commutant_coeffs.T.real, row.real, rcond=None
            )
            recon = commutant_coeffs.T.real @ coeffs_in_commutant
            proj_resid.append(float(np.max(np.abs(recon - row.real))))
        su3_in_commutant_residual = max(proj_resid)
    else:
        su3_in_commutant_residual = float("nan")
    print(
        f"max residual, su(3) coeffs reconstructed from commutant span: "
        f"{su3_in_commutant_residual:.3e} (expect ~0 if su(3) subset commutant)"
    )

    results = {
        "so8_basis_len": len(so8),
        "su3_in_so8_span_residual": su3_residual,
        "bridge_sanity": bridge_sanity,
        "positive_control_su3_commutator": max_su3_comm,
        "D_frobenius_norm": d_norm,
        "singular_values": s_svd.tolist(),
        "rank_comm_matrix": rank,
        "commutant_dim": commutant_dim,
        "su3_in_commutant_span_residual": su3_in_commutant_residual,
        "conclusion": (
            f"Exhaustive so(8) commutant of the physical D has dimension "
            f"{commutant_dim} (predicted 8 = su(3) exactly). "
            + (
                "MATCHES prediction: no subalgebra of so(8) beyond su(3) "
                "commutes with D -- closes L3B_SPIN8_INTERFACE_SPEC.md "
                "section 1.5's own Dynamics open item exhaustively."
                if commutant_dim == 8
                else "DIFFERS FROM PREDICTION -- requires immediate, careful "
                "follow-up per this round's own kill_criterion, not to be "
                "explained away."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
