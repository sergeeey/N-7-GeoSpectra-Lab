"""C79 -- a genuine non-product S3-S6 coupling term (exploratory, hypothesis-driven).

See claim.md for the full honesty ledger. In short: every prior round in
this arc (C70-C78) tested symmetries of round59's D_S6, an operator with
NO dependence on S3. This round builds an actual coupling term mixing an
S3 Clifford index (round67's Z_i, Cl(0,3)) with an S6/octonion generator
(round119's so(4)_1, split into a genuine su(2) triple via the standard
so(4)=su(2)+su(2) self-dual/anti-self-dual decomposition, transported to
Sigma via C70's verified U_v), restricted to S3's n=0, +-branch sector
(round67's own "constant spinor" level, where D_S3 acts as a known scalar).

WHICH piece of so(8)'s complement plays "S3's gauge index" is an explicit
POSTULATE, not a derivation -- stated plainly in claim.md, not smuggled in.

Reuses round67's clifford_generators/calibrate_h_H, triality_so4xso4_
invariance.py's build_so4xso4_basis, C70's run_direct_solve/hom_basis/
search_nonzero_intertwiner, round59's build_clifford/leibniz/NOMIZU, and
C73's build_numeric_dirac, all unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c79.json"


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
SO4MOD = load_module(
    "triality_so4xso4_invariance",
    HERE.parent / "20260715-l3b-triality-so4xso4-invariance" / "triality_so4xso4_invariance.py",
)
ROUND67 = load_module(
    "e2_s3_torsion_deformation",
    HERE.parent / "20260717-round67-e2-s3-torsion-deformation" / "e2_s3_torsion_deformation.py",
)
R59 = C70.C68.R59


def get_bridge_to_sigma() -> tuple[np.ndarray, dict]:
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
    return u_v, {"u_v_det": best_det, "intertwining_residual": residual}


def self_dual_anti_self_dual_triples(so4_1: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """so4_1 has 6 generators in the order (0,1),(0,2),(0,3),(1,2),(1,3),(2,3)
    (matching build_so4xso4_basis()'s nested-loop order). Standard so(4)=su(2)+su(2)
    self-dual / anti-self-dual split on Lambda^2(R^4): (e01+-e23, e02-+e13, e03+-e12)."""
    e01, e02, e03, e12, e13, e23 = so4_1
    self_dual = np.array([e01 + e23, e02 - e13, e03 + e12])
    anti_self_dual = np.array([e01 - e23, e02 + e13, e03 - e12])
    return self_dual, anti_self_dual


def check_su2_closure(triple: np.ndarray) -> dict:
    """Verify [g_i, g_j] = c * g_k (cyclic) for some nonzero constant c -- genuine
    su(2) closure, not assumed."""
    g1, g2, g3 = triple
    comms = {
        "[g1,g2]_vs_g3": (g1 @ g2 - g2 @ g1, g3),
        "[g2,g3]_vs_g1": (g2 @ g3 - g3 @ g2, g1),
        "[g3,g1]_vs_g2": (g3 @ g1 - g1 @ g3, g2),
    }
    report = {}
    for name, (comm, target) in comms.items():
        flat_comm = comm.reshape(-1)
        flat_target = target.reshape(-1)
        coeff = float(np.dot(flat_comm, flat_target) / np.dot(flat_target, flat_target))
        residual = float(np.max(np.abs(flat_comm - coeff * flat_target)))
        report[name] = {"coeff": coeff, "residual": residual}
    return report


def leibniz_matrix(gen_on_sigma: np.ndarray) -> np.ndarray:
    return np.array(R59.leibniz(sp.Matrix(gen_on_sigma)).evalf(), dtype=complex)


def main() -> None:
    print("=== Step 1: round67's Z_i (Cl(0,3)) and h_H calibration ===")
    z_gens = [np.array(z.tolist(), dtype=complex) for z in ROUND67.clifford_generators()]
    h_h = ROUND67.calibrate_h_H()
    d_s3_scalar = float(sp.Rational(1, 2) * h_h)  # D^{1/2}(constant spinor) = (1/2)*h_H
    print(f"h_H = {h_h}, D_S3 scalar at t=1/2 (n=0, + branch) = {d_s3_scalar}")

    print("\n=== Step 2: round119's so(4)_1, self-dual/anti-self-dual split ===")
    so4_all = SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, anti_self_dual = self_dual_anti_self_dual_triples(so4_1)
    sd_closure = check_su2_closure(self_dual)
    asd_closure = check_su2_closure(anti_self_dual)
    print("self-dual closure:", sd_closure)
    print("anti-self-dual closure:", asd_closure)
    # use self-dual triple (arbitrary but stated choice -- see claim.md postulate)
    su2_triple = self_dual

    print("\n=== Step 3: C70's bridge, transport su(2) triple to Sigma ===")
    u_v, bridge_sanity = get_bridge_to_sigma()
    print(bridge_sanity)
    u_v_unitarity_residual = float(np.max(np.abs(u_v.conj().T @ u_v - np.eye(8))))
    u_v_singular_values = np.linalg.svd(u_v, compute_uv=False).tolist()
    print(
        f"U_v unitarity residual ||U_v^dagger U_v - I||_max = {u_v_unitarity_residual:.4f} "
        "(NOT unitary -- see decision.md)"
    )
    print(f"U_v singular values: {np.round(u_v_singular_values, 4)}")
    u_v_inv = np.linalg.inv(u_v)
    su2_on_sigma = [u_v_inv @ g.astype(complex) @ u_v for g in su2_triple]
    leibniz_su2 = [leibniz_matrix(g) for g in su2_on_sigma]

    print("\n=== Step 4: build D_S6, restrict to n=0 +-branch sector (128-dim joint space) ===")
    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)
    I2 = np.eye(2, dtype=complex)
    I64 = np.eye(64, dtype=complex)
    d_joint_base = d_s3_scalar * np.kron(I2, I64) + np.kron(I2, d_s6)

    z_kron = [np.kron(z, I64) for z in z_gens]
    leib_kron = [np.kron(I2, leib) for leib in leibniz_su2]
    t_raw = sum(z_kron[i] @ leib_kron[i] for i in range(3))
    hermiticity_residual_T_raw = float(np.max(np.abs(t_raw - t_raw.conj().T)))
    print(f"||T_raw - T_raw^dagger||_max = {hermiticity_residual_T_raw:.3e}")

    # U_v (C70's intertwiner, reused unmodified throughout C75/C77/C78) is NOT
    # unitary -- verified directly this round (singular values 0.546-1.740, far
    # from 1; see decision.md). Those prior rounds never needed Leibniz(g_sigma)
    # to be individually anti-Hermitian -- they only tested [D, Leibniz(g_sigma)],
    # a similarity-invariant statement about intertwining, unaffected by U_v's
    # non-unitarity. THIS round needs T itself to be Hermitian to be a valid
    # addition to a physical Dirac-type operator, so T is explicitly Hermitized
    # here: T = (T_raw + T_raw^dagger)/2. Documented, not silently patched.
    t_generator = (t_raw + t_raw.conj().T) / 2
    hermiticity_residual_T = float(np.max(np.abs(t_generator - t_generator.conj().T)))
    hermiticity_residual_base = float(np.max(np.abs(d_joint_base - d_joint_base.conj().T)))
    print(f"||T (Hermitized) - T^dagger||_max = {hermiticity_residual_T:.3e}")
    print(f"||D_joint_base - D_joint_base^dagger||_max = {hermiticity_residual_base:.3e}")

    print("\n=== Step 5: eps=0 sanity -- is ker(D_joint) empty? ===")
    eigvals_base = np.linalg.eigvalsh(d_joint_base)
    min_abs_eigval_base = float(np.min(np.abs(eigvals_base)))
    print(f"min |eigenvalue| at eps=0: {min_abs_eigval_base:.6f} (expect nonzero)")

    print("\n=== Step 6: sweep eps, look for zero-crossings ===")
    eps_values = np.linspace(-2.0, 2.0, 81)
    min_abs_eigval_per_eps = []
    for eps in eps_values:
        d_joint = d_joint_base + eps * t_generator
        herm_check = float(np.max(np.abs(d_joint - d_joint.conj().T)))
        eigvals = np.linalg.eigvalsh(d_joint)
        min_abs_eigval_per_eps.append(float(np.min(np.abs(eigvals))))
        if herm_check > 1e-8:
            print(f"  !! eps={eps:.3f}: Hermiticity check FAILED, residual {herm_check:.3e}")

    min_abs_eigval_per_eps = np.array(min_abs_eigval_per_eps)
    crossing_tol = 1e-6
    crossing_indices = np.where(min_abs_eigval_per_eps < crossing_tol)[0]
    crossings = [
        {"eps": float(eps_values[i]), "min_abs_eigval": float(min_abs_eigval_per_eps[i])}
        for i in crossing_indices
    ]
    overall_min_idx = int(np.argmin(min_abs_eigval_per_eps))
    print(
        f"global min |eigenvalue| over sweep: {min_abs_eigval_per_eps[overall_min_idx]:.6f} "
        f"at eps={eps_values[overall_min_idx]:.3f}"
    )
    print(f"number of crossings (min|eigval| < {crossing_tol}): {len(crossings)}")
    for c in crossings:
        print(f"  crossing at eps={c['eps']:.3f}")

    results = {
        "d_s3_scalar_n0_plus_branch": d_s3_scalar,
        "self_dual_closure": sd_closure,
        "anti_self_dual_closure": asd_closure,
        "bridge_sanity": bridge_sanity,
        "u_v_unitarity_residual": u_v_unitarity_residual,
        "u_v_singular_values": u_v_singular_values,
        "hermiticity_residual_T_raw_before_hermitizing": hermiticity_residual_T_raw,
        "hermiticity_residual_T": hermiticity_residual_T,
        "hermiticity_residual_base": hermiticity_residual_base,
        "min_abs_eigval_eps0": min_abs_eigval_base,
        "eps_sweep": eps_values.tolist(),
        "min_abs_eigval_per_eps": min_abs_eigval_per_eps.tolist(),
        "global_min_abs_eigval": float(min_abs_eigval_per_eps[overall_min_idx]),
        "global_min_at_eps": float(eps_values[overall_min_idx]),
        "n_crossings": len(crossings),
        "crossings": crossings,
        "conclusion": (
            f"{len(crossings)} zero-crossing(s) found in eps in [-2,2] for this "
            "specific, explicitly-postulated non-product coupling term (S3's "
            "n=0 +-branch sector only). "
            + (
                "NO crossings found -- consistent with every prior route in "
                "this project closing; a genuine, informative negative result "
                "for this specific postulate, not a proof no coupling anywhere "
                "could work."
                if len(crossings) == 0
                else "CROSSING(S) FOUND -- per this round's own kill_criterion, "
                "this is an unexpectedly positive result after 8 rounds of "
                "consistent negatives and REQUIRES independent skeptical "
                "verification before being trusted, not immediate acceptance."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
