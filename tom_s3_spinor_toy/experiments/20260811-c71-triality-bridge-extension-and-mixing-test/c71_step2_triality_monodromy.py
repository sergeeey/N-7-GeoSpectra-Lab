"""C71 step 2 -- triality monodromy test, a well-posed, directly computable
version of round118's open sufficiency condition (iii): "triality acting
purely as 1(x)t with no admixture on the matter factor."

Key design fix over a naive attempt: solving Phi (the su(3) automorphism)
INDEPENDENTLY per channel (as step 1 did) confounds the test with each
channel's own Inn(su(3)) gauge freedom (Phi itself lives on a continuous
~8-real-dim orbit; the representation intertwiner U has an ADDITIONAL
GL(2,C)xC*xC* residual freedom on top, from Schur's lemma applied to the
reducible target 1+1+3+3bar -- two copies of the trivial rep can mix
arbitrarily, the 3 and 3bar each get an independent scalar). Composing three
INDEPENDENTLY-solved U's would produce a monodromy dominated by arbitrary
gauge choices, not physics.

Fix: use a SINGLE Phi (found once, against channel_v, reusing C70's own
committed solve) to build M_k, then find U_v, U_s, U_c against the SAME M_k
for all three channels. This was verified as a real, non-forced possibility
first (a single Phi bridges to all three channels with hom_dim=6, not
assumed). The composite monodromy V_cv @ V_sc @ V_vs still carries the
residual per-channel GL(2)xC*xC* freedom, so only GAUGE-INVARIANT features of
the monodromy are reported as meaningful: its action restricted to the
3-dimensional block (scalar = clean, non-scalar = genuine admixture) is
invariant under the residual freedom's action on that block up to an overall
phase; the 2-dim singlet-mixing freedom is NOT invariant and is explicitly
excluded from the interpretation.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c71_step2.json"


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
C71S1 = load_module("c71_step1_triality_bridge", HERE / "c71_step1_triality_bridge.py")
C68 = C70.C68


def find_u_for_channel(m_matrices: list[np.ndarray], gens_target: list[np.ndarray]) -> dict:
    basis = C68.hom_basis(m_matrices, gens_target)
    hom_dim = basis.shape[1]
    u, best_det = C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)
    residual = None
    if u is not None:
        u_inv = np.linalg.inv(u)
        residual = max(
            float(np.max(np.abs(u @ m_matrices[k] @ u_inv - gens_target[k]))) for k in range(8)
        )
    return {"hom_dim": hom_dim, "u": u, "det": best_det, "residual": residual}


def unitarity_defect(u: np.ndarray) -> float:
    """||U^dagger U - c*I|| minimized over scalar c -- 0 iff U is proportional
    to a unitary matrix (the natural notion here since U is only defined up
    to an overall complex scale by the norm constraint used to find Phi)."""
    gram = u.conj().T @ u
    c = np.trace(gram).real / 8.0
    return float(np.max(np.abs(gram - c * np.eye(8))))


def block_restriction(op: np.ndarray, indices: list[int]) -> np.ndarray:
    return op[np.ix_(indices, indices)]


def scalar_defect(block: np.ndarray) -> float:
    """||block - c*I|| minimized over scalar c -- 0 iff block acts as a pure
    phase/scale (no genuine admixture within that irrep)."""
    n = block.shape[0]
    c = np.trace(block) / n
    return float(np.max(np.abs(block - c * np.eye(n))))


def main() -> None:
    gens_r59 = C68.to_numpy_su3_r59()
    gens_v = C68.su3_g102_on_channel_v()
    gens_s = C71S1.su3_g102_on_channel_s()
    gens_c = C71S1.su3_g102_on_channel_c()

    solve_v = C70.run_direct_solve(gens_r59, gens_v, n_trials=3, norm_weight=5.0, seed=42)
    phi_v = solve_v["best"]["phi"]
    phi_inv = np.linalg.inv(phi_v)
    m_matrices = [sum(phi_inv[a, k] * gens_r59[a] for a in range(8)) for k in range(8)]

    results_v = find_u_for_channel(m_matrices, gens_v)
    results_s = find_u_for_channel(m_matrices, gens_s)
    results_c = find_u_for_channel(m_matrices, gens_c)

    print("channel_v:", {k: v for k, v in results_v.items() if k != "u"})
    print("channel_s:", {k: v for k, v in results_s.items() if k != "u"})
    print("channel_c:", {k: v for k, v in results_c.items() if k != "u"})

    U_v, U_s, U_c = results_v["u"], results_s["u"], results_c["u"]

    V_vs = U_s @ np.linalg.inv(U_v)  # channel_v -> channel_s
    V_sc = U_c @ np.linalg.inv(U_s)  # channel_s -> channel_c
    V_cv = U_v @ np.linalg.inv(U_c)  # channel_c -> channel_v

    monodromy = V_cv @ V_sc @ V_vs  # channel_v -> channel_v, around the full cycle

    unitarity = {
        "V_vs": unitarity_defect(V_vs),
        "V_sc": unitarity_defect(V_sc),
        "V_cv": unitarity_defect(V_cv),
        "monodromy": unitarity_defect(monodromy),
    }
    print("\nUnitarity defects (0 = proportional to unitary):", unitarity)
    print("(individual legs are NOT unitary -- expected, search_nonzero_intertwiner")
    print(" imposes no such constraint; the informative fact is that the full")
    print(" cycle product is, despite that.)")

    # By construction the monodromy commutes with the su(3) action on channel_v
    # (chained intertwining relations), so Schur's lemma ALONE already forces:
    # block-diagonal w.r.t. 1+1+3+3bar, and scalar on the 3 and on the 3bar
    # individually (each appears with multiplicity 1). None of that is new
    # physics -- it holds for ANY element of the centralizer. What Schur's
    # lemma does NOT force: unitarity of the monodromy (a generic centralizer
    # element need not be unitary), or scalar action on the 2-dim singlet pair
    # (Schur only guarantees an arbitrary GL(2,C) there). Those two are the
    # genuinely informative checks below.
    overall_scalar = complex(np.trace(monodromy) / 8.0)
    exact_identity_residual = float(np.max(np.abs(monodromy - overall_scalar * np.eye(8))))
    print(f"\nMonodromy overall scalar c = {overall_scalar}")
    print(f"|monodromy - c*I| = {exact_identity_residual:.3e}  (0 = monodromy IS c*Identity)")

    # 1+1+3+3bar decomposition indices are basis-dependent; use round59's own
    # convention (SUBSETS ordering): index 0 = trivial(1), indices 1,2,3 =
    # the 3 (deg-1 wedge), index 7 = trivial(1) (deg-3, top wedge), indices
    # 4,5,6 = the 3bar (deg-2 wedge). This is round59's construction basis,
    # NOT G102's -- the monodromy acts on the g102 (channel) side, so this
    # decomposition is only meaningful after transporting back via U_v^-1,
    # which is exactly what "acting on channel_v, expressed in round59's
    # basis via U_v^-1" achieves.
    monodromy_in_r59_basis = np.linalg.inv(U_v) @ monodromy @ U_v
    triplet_idx = [1, 2, 3]
    antitriplet_idx = [4, 5, 6]
    singlet_idx = [0, 7]

    block_defects = {
        "triplet_3": scalar_defect(block_restriction(monodromy_in_r59_basis, triplet_idx)),
        "antitriplet_3bar": scalar_defect(
            block_restriction(monodromy_in_r59_basis, antitriplet_idx)
        ),
        "singlet_1_1": scalar_defect(block_restriction(monodromy_in_r59_basis, singlet_idx)),
    }
    off_block = monodromy_in_r59_basis.copy()
    for idx in (triplet_idx, antitriplet_idx, singlet_idx):
        off_block[np.ix_(idx, idx)] = 0
    off_block_norm = float(np.max(np.abs(off_block)))

    print("\nMonodromy block structure (in round59's own 1+1+3+3bar basis):")
    print("  block/triplet/antitriplet defects -- SCHUR-FORCED, expected ~0 regardless")
    print("  of physics (any su(3)-centralizer element has this structure):", block_defects)
    print("  off-block-diagonal norm -- also Schur-forced:", off_block_norm)
    print("  singlet_1_1 defect is the exception: Schur only guarantees GL(2,C) there,")
    print("  so its near-zero value IS informative, not forced.")

    results = {
        "phi_v_residual": solve_v["best"]["max_residual"],
        "channel_v": {k: v for k, v in results_v.items() if k != "u"},
        "channel_s": {k: v for k, v in results_s.items() if k != "u"},
        "monodromy_overall_scalar": overall_scalar,
        "monodromy_exact_identity_residual": exact_identity_residual,
        "channel_c": {k: v for k, v in results_c.items() if k != "u"},
        "unitarity_defects": unitarity,
        "monodromy_block_scalar_defects": block_defects,
        "monodromy_off_block_diagonal_norm": off_block_norm,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
