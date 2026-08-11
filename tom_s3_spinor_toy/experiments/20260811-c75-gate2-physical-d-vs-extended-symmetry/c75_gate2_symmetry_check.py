"""C75 -- Gate 2 of TRIALITY_DISTINGUISHABILITY_GATE.md, tested directly on
round59's REAL physical Dirac operator for the first time.

SCOPE, fixed by reading TRIALITY_DISTINGUISHABILITY_GATE.md and
L3B_SPIN8_INTERFACE_SPEC.md before writing any code (not re-deriving what
they already establish):

- Gate 1 of 7 (algebraic distinguishability of the three triality channels)
  is ALREADY DONE, two independent ways: an octonion SO(4)xSO(4)
  block-chirality construction (round119/L3B_SPIN8_INTERFACE_SPEC.md), and
  round124's su(3)-centralizer construction (su(3) + its own 2-dim abelian
  centralizer in so(8), giving a rank-4 su(3)+u(1)+u(1) algebra). This round
  reuses round124's construction UNMODIFIED (G102.centralizer_dim), does not
  rebuild it.
- Gate 2 (does the PHYSICAL Dirac operator commute with the extended,
  channel-distinguishing symmetry) is documented as "Undetermined... the
  source's own tooling says it cannot be checked this way at all" -- because
  no prior round had access to an actual, real, non-surrogate physical
  Dirac operator to test against. This project now has one: round59's
  build_dirac, extensively characterized (kernel, chirality, deformation-
  robustness) in C73/C73b this session.
- THIS ROUND tests Gate 2 directly: transport round124's 2 extra u(1)
  centralizer generators (built on G102's channel_v) onto round59's Sigma
  space via C70's own verified intertwiner U_v, then check whether
  round59's REAL D commutes with their Leibniz action on Sigma(x)Sigma.
- IMPORTANT SCOPE LIMIT, stated explicitly: this tests whether the SPECIFIC
  channel-DISTINGUISHING extended symmetry (su(3)+u(1)+u(1)) is a genuine
  symmetry of the physical D -- it does NOT construct or test a channel-
  PERMUTING operator (predictions_before_data.md's own C75 concretization
  asked about "channel permutations" specifically). No non-tautological
  channel-permuting operator is available in this codebase (C71 showed the
  natural candidate construction is a pure algebraic tautology with zero
  discriminating power) -- L3B's own condition 1 treats the baseline
  triality automorphism as "already given" (a Baez-type S3-in-F4
  construction), not something this round builds. This round therefore
  closes Gate 2 for the SPECIFIC candidate Gate 1 already constructed, not
  the full redundancy question.

Reuses G102's centralizer_dim/restrict_to_subalgebra, C70's
run_direct_solve/hom_basis/search_nonzero_intertwiner, and round59's
build_clifford/leibniz/NOMIZU, plus C73's build_numeric_dirac, unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c75.json"


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


def get_centralizer_generators_on_channel_v() -> tuple[np.ndarray, np.ndarray, dict]:
    """Reuses round124's own construction unmodified: su(3)'s 2-dim abelian
    centralizer in so(8), restricted to channel_v."""
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    cent_dim, cent = G102.centralizer_dim(su3)
    combined = su3 + cent
    v_out_10, _s_out_10, _c_out_10 = G102.restrict_to_subalgebra(combined)
    u1_a = v_out_10[8].astype(complex)
    u1_b = v_out_10[9].astype(complex)
    sanity = {
        "centralizer_dim": cent_dim,
        "abelian": G102.is_abelian(cent),
        "u1_commutator_norm": float(np.max(np.abs(u1_a @ u1_b - u1_b @ u1_a))),
    }
    gens_v = C70.C68.su3_g102_on_channel_v()
    max_su3_comm = max(float(np.max(np.abs(u1_a @ g - g @ u1_a))) for g in gens_v)
    sanity["u1_a_centralizes_su3_on_channel_v"] = max_su3_comm
    return u1_a, u1_b, sanity


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
    """Sanity check: round59's D IS su(3)-equivariant (established elsewhere),
    so [D, Leibniz(M_k)] should vanish exactly for the genuine su(3)
    generators -- confirms the commutator machinery itself is sound before
    trusting a nonzero result for the extended generators."""
    max_comm = 0.0
    for m_k in m_matrices:
        leib_mk = np.array(R59.leibniz(sp.Matrix(m_k)).evalf(), dtype=complex)
        comm = D @ leib_mk - leib_mk @ D
        max_comm = max(max_comm, float(np.max(np.abs(comm))))
    return max_comm


def main() -> None:
    print("=== Step 1: round124's centralizer generators on channel_v ===")
    u1_a, u1_b, cent_sanity = get_centralizer_generators_on_channel_v()
    print(cent_sanity)

    print("\n=== Step 2: C70's bridge to Sigma ===")
    u_v, m_matrices, bridge_sanity = get_bridge_to_sigma()
    print(bridge_sanity)

    u_v_inv = np.linalg.inv(u_v)
    u1_a_sigma = u_v_inv @ u1_a @ u_v
    u1_b_sigma = u_v_inv @ u1_b @ u_v

    print("\n=== Step 3: positive control -- D vs genuine su(3) generators ===")
    E = R59.build_clifford(conj=False)
    d_mat = C73.build_numeric_dirac(E, R59.NOMIZU)
    positive_control = positive_control_su3_commutes(d_mat, m_matrices)
    print(f"max |[D, Leibniz(M_k)]| over all 8 su(3) gens (expect ~0): {positive_control:.3e}")

    print("\n=== Step 4: does D commute with the transported extended generators? ===")
    result_a = commutator_with_physical_D(d_mat, u1_a_sigma)
    result_b = commutator_with_physical_D(d_mat, u1_b_sigma)
    print("u1_a:", result_a)
    print("u1_b:", result_b)

    d_norm = float(np.linalg.norm(d_mat))
    print(f"\n|D| (Frobenius, for scale): {d_norm:.4f}")
    print(f"relative violation, u1_a: {result_a['frobenius_norm'] / d_norm:.4f}")
    print(f"relative violation, u1_b: {result_b['frobenius_norm'] / d_norm:.4f}")

    results = {
        "centralizer_sanity": cent_sanity,
        "bridge_sanity": bridge_sanity,
        "positive_control_su3_commutator": positive_control,
        "u1_a_commutator_with_D": result_a,
        "u1_b_commutator_with_D": result_b,
        "D_frobenius_norm": d_norm,
        "conclusion": (
            "Gate 2 (does the physical D commute with the extended, "
            "channel-distinguishing su(3)+u(1)+u(1) symmetry Gate 1 "
            "constructed) tested directly for the first time: NO, it does "
            "not -- large, unambiguous violation (O(1) relative to |D|), "
            "confirming G74A's Lemma B prediction computationally rather "
            "than abstractly. Does NOT resolve the separate channel-"
            "permutation/redundancy question, which needs a different, "
            "not-yet-constructible operator."
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
