"""C77 -- Gate 2 test for round119's SO(4)xSO(4) candidate, plus a written
scoping of why the actual T-to-D bridge is NOT attempted here.

Direct extension of C75's methodology (round124's su(3)+u(1)+u(1) candidate)
to round119's SO(4)xSO(4) candidate (a genuinely different 12-dim subalgebra,
per round125: only a 3-dim abelian intersection with round124's 10-dim
candidate). Transport round119's 12 so(4)+so(4) generators (built on
channel_v=8_v via triality_so4xso4_invariance.py's own build_so4xso4_basis(),
unmodified) onto round59's Sigma via C70's verified U_v, then test whether
round59's REAL physical D commutes with them.

SCOPE LIMIT, stated in claim.md and restated here: this does NOT build the
actual "T-to-D bridge" (using round119's own triality-automorphism matrix T
to construct a genuine channel-permuting operator). That requires resolving
round119's own documented, still-open vector-vs-spinor-representation
consistency gap (triality_so4xso4_invariance.py's own end-of-file diagnostic)
and building an SO(4)xSO(4)-equivariant identification of Sigma with 8_s and
8_c specifically -- neither attempted here. See claim.md and decision.md for
the full reasoning.

Reuses G102's derivation_basis/stabilizer_basis (su(3), for the positive
control and the P1 sanity check), triality_so4xso4_invariance.py's own
build_so4xso4_basis unmodified, C70's run_direct_solve/hom_basis/
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
RESULTS_PATH = HERE / "results_c77.json"
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
SO4MOD = load_module(
    "triality_so4xso4_invariance",
    HERE.parent / "20260715-l3b-triality-so4xso4-invariance" / "triality_so4xso4_invariance.py",
)
R59 = C70.C68.R59
G102 = C70.C68.G102


def subspace_rank(mats: list[np.ndarray]) -> int:
    flat = np.array([m.reshape(-1) for m in mats])
    s = np.linalg.svd(flat, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0] if len(s) else 1.0)))


def check_basis_compatibility_p1() -> dict:
    """Reproduces round125's own published dim(A)=12, dim(A cap su3+cent)=3
    result, confirming this round combines the two source modules in the
    SAME convention round125 already verified -- not a new mismatch."""
    so4xso4 = SO4MOD.build_so4xso4_basis()
    so4xso4_list = [so4xso4[i] for i in range(so4xso4.shape[0])]
    dim_a = subspace_rank(so4xso4_list)

    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    _cent_dim, cent = G102.centralizer_dim(su3)
    combined_b = su3 + cent
    dim_b = subspace_rank(combined_b)

    union_list = so4xso4_list + combined_b
    dim_union = subspace_rank(union_list)
    dim_intersection = dim_a + dim_b - dim_union

    return {
        "dim_A_so4xso4": dim_a,
        "dim_B_su3_plus_centralizer": dim_b,
        "dim_A_union_B": dim_union,
        "dim_A_intersect_B": dim_intersection,
        "matches_round125": (dim_a, dim_b, dim_union, dim_intersection) == (12, 10, 19, 3),
    }


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


def commutator_with_physical_D(D: np.ndarray, gen_on_sigma: np.ndarray) -> dict:
    leib = np.array(R59.leibniz(sp.Matrix(gen_on_sigma)).evalf(), dtype=complex)
    comm = D @ leib - leib @ D
    return {
        "max_abs_entry": float(np.max(np.abs(comm))),
        "frobenius_norm": float(np.linalg.norm(comm)),
    }


def positive_control_su3_commutes(D: np.ndarray, m_matrices: list[np.ndarray]) -> float:
    max_comm = 0.0
    for m_k in m_matrices:
        leib_mk = np.array(R59.leibniz(sp.Matrix(m_k)).evalf(), dtype=complex)
        comm = D @ leib_mk - leib_mk @ D
        max_comm = max(max_comm, float(np.max(np.abs(comm))))
    return max_comm


def main() -> None:
    print("=== Step 1: basis-compatibility sanity (reproduce round125) ===")
    p1 = check_basis_compatibility_p1()
    print(p1)
    if not p1["matches_round125"]:
        print("!! MISMATCH with round125's published numbers -- STOPPING, see kill_criterion.")
        RESULTS_PATH.write_text(
            json.dumps({"p1_basis_compatibility": p1, "STOPPED": True}, indent=2)
        )
        return

    print("\n=== Step 2: C70's bridge to Sigma ===")
    u_v, m_matrices, bridge_sanity = get_bridge_to_sigma()
    print(bridge_sanity)
    u_v_inv = np.linalg.inv(u_v)

    print("\n=== Step 3: positive control -- D vs genuine su(3) generators ===")
    E = R59.build_clifford(conj=False)
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)
    positive_control = positive_control_su3_commutes(d_mat, m_matrices)
    print(f"max |[D, Leibniz(M_k)]| over all 8 su(3) gens (expect ~0): {positive_control:.3e}")

    print("\n=== Step 4: Gate 2 test -- transport SO(4)xSO(4)'s 12 generators, check vs D ===")
    so4xso4 = SO4MOD.build_so4xso4_basis()
    per_generator = []
    max_frob = 0.0
    for i in range(so4xso4.shape[0]):
        g_sigma = u_v_inv @ so4xso4[i].astype(complex) @ u_v
        result = commutator_with_physical_D(d_mat, g_sigma)
        per_generator.append(result)
        max_frob = max(max_frob, result["frobenius_norm"])
        print(
            f"  generator {i:2d}: max_abs_entry={result['max_abs_entry']:.4f}  "
            f"frobenius_norm={result['frobenius_norm']:.4f}"
        )

    d_norm = float(np.linalg.norm(d_mat))
    min_frob = min(r["frobenius_norm"] for r in per_generator)
    print(f"\n|D| (Frobenius, for scale): {d_norm:.4f}")
    print(
        f"min/max relative violation across 12 generators: "
        f"{min_frob / d_norm:.4f} / {max_frob / d_norm:.4f}"
    )

    results = {
        "p1_basis_compatibility": p1,
        "bridge_sanity": bridge_sanity,
        "positive_control_su3_commutator": positive_control,
        "so4xso4_per_generator_commutator_with_D": per_generator,
        "D_frobenius_norm": d_norm,
        "min_relative_violation": min_frob / d_norm,
        "max_relative_violation": max_frob / d_norm,
        "conclusion": (
            "Gate 2 tested for round119's SO(4)xSO(4) candidate for the "
            "first time. Does NOT constitute a T-to-D bridge -- see "
            "claim.md/decision.md for why that requires additional, "
            "not-yet-existing infrastructure (an SO(4)xSO(4)-equivariant "
            "identification of Sigma with 8_s and 8_c, and resolution of "
            "round119's own open vector-vs-spinor consistency gap)."
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
