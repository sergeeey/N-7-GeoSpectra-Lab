"""OB11(ii) hard half, first step: does round59's real Sigma (the curvature-
twisted Clifford module actually used to prove dim ker=1) carry the same
abstract su(3)-module type (1+1+3+3bar) as G102's triality channels?

Reuses round59's own Clifford/spin-lift/ADNU construction unmodified, by
direct import. Computes the quadratic Casimir spectrum of su(3) acting on
Sigma, using the exact same technique C29 already validated for G102's
channels (OB11 condition i).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ob11ii_bridge.json"

R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)
_spec = importlib.util.spec_from_file_location("round59_route_a_independent", R59_PATH)
assert _spec and _spec.loader
R59 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(R59)

TOL = 1e-8


def to_numpy(mat: sp.Matrix) -> np.ndarray:
    return np.array(mat.evalf(), dtype=complex)


def main() -> None:
    clifford = R59.build_clifford()  # e_1..e_6, 8x8 sympy matrices

    # --- build su(3) generators on Sigma via round59's own ADNU + spin_lift ---
    su3_sympy = [R59.spin_lift(R59.ADNU[i], clifford) for i in range(1, 9)]
    su3 = [to_numpy(m) for m in su3_sympy]
    n_su3 = len(su3)

    # --- P1: sanity -- su(3) closes under commutator (8-dim Lie algebra) ---
    su3_flat = np.array([m.flatten() for m in su3]).T  # 64 x 8
    Q, _ = np.linalg.qr(su3_flat)
    max_closure_residual = 0.0
    for a in range(n_su3):
        for b in range(a + 1, n_su3):
            comm = su3[a] @ su3[b] - su3[b] @ su3[a]
            comm_flat = comm.flatten()
            coeffs = Q.conj().T @ comm_flat
            recon = Q @ coeffs
            residual = float(np.max(np.abs(recon - comm_flat)))
            max_closure_residual = max(max_closure_residual, residual)
    p1_pass = max_closure_residual < 1e-6

    # --- P2: quadratic Casimir spectrum ---
    C2 = sum(su3[a] @ su3[a] for a in range(n_su3))
    C2_herm = (C2 + C2.conj().T) / 2
    eigs = np.sort(np.linalg.eigvalsh(C2_herm))

    n_zero = int(np.sum(np.abs(eigs) < 1e-6))
    nonzero_eigs = eigs[np.abs(eigs) >= 1e-6]
    nonzero_spread = (
        float(np.max(nonzero_eigs) - np.min(nonzero_eigs)) if len(nonzero_eigs) else 0.0
    )
    p2_pass = n_zero == 2 and len(nonzero_eigs) == 6 and nonzero_spread < 1e-6

    if not p1_pass:
        verdict = "HARNESS_CONTROL_FAILED_ADNU_NOT_CLOSED_SU3"
    elif p2_pass:
        verdict = "SAME_MODULE_TYPE_CONFIRMED_BRIDGE_VIABLE"
    else:
        verdict = "DIFFERENT_MODULE_TYPE_BRIDGE_DEAD"

    results = {
        "experiment": "ob11ii_round59_su3_bridge",
        "n_su3_generators": n_su3,
        "max_closure_residual": max_closure_residual,
        "p1_su3_closes": p1_pass,
        "C2_eigenvalues_sorted": eigs.tolist(),
        "n_zero_eigenvalues": n_zero,
        "n_nonzero_eigenvalues": len(nonzero_eigs),
        "nonzero_spread": nonzero_spread,
        "p2_matches_1_1_3_3bar_pattern": p2_pass,
        "verdict": verdict,
    }

    print("=" * 92)
    print("OB11(ii) hard half, step 1: round59 Sigma vs triality-channel su(3)-module type")
    print("=" * 92)
    print(f"n_su3_generators = {n_su3} (predict 8)")
    print(f"su(3) closure residual = {max_closure_residual:.2e} (expect ~0)")
    print(f"P1 (su(3) closes)?  {p1_pass}")
    print()
    print(f"C2 eigenvalues (sorted): {np.round(eigs, 6)}")
    print(f"n_zero={n_zero}, n_nonzero={len(nonzero_eigs)}, nonzero_spread={nonzero_spread:.2e}")
    print(f"P2 (matches 1+1+3+3bar pattern: 2 zero + 6 equal nonzero)?  {p2_pass}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
