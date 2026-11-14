"""C174: does C79's non-product S3-S6 coupling distinguish triality channels?

C79 built T = sum_i Z_i (x) Leibniz(U_v^-1 so4_1_selfdual_i U_v) -- an S3-Clifford
index paired with an so(4)_1 generator transported to Sigma via channel v's own
bridge U_v -- and swept eps over the RAW 128-dim space, finding one crossing later
explained as a 36-dim raw-kernel artifact (see C79 decision.md). This round asks
the question C79 itself flagged as untried: restricted to the physically relevant
vector (round59's own certified kernel vector, not the raw kernel), does building
the SAME coupling with channel s's or channel c's bridge (U_s, U_c) give the SAME
numbers as channel v -- or different ones?

If IDENTICAL: extends today's C173 (G44/G102: channels are IDENTICAL su(3)-modules,
not just isomorphic) to cover non-invariant-generator constructions too, not just
su(3)-invariant ones -- closing OB11's remaining door structurally, the same way
C173 closed item 3.

Method: compress D_joint(eps) onto the 2-dim physically-relevant subspace
span(e1(x)v_round59, e2(x)v_round59) (S3's own n=0 2-dim spinor factor, tensor
round59's own certified kernel vector) and diagonalize the resulting EXACT 2x2
Hermitian matrix -- artifact-free by construction, since the 36-dim raw kernel
never enters this compressed subspace except through its own overlap with
v_round59 (which IS the physically relevant vector by definition).

Reuses C79's Z_i/so(4)_1/D_S6 construction, C71's channel-s/c generators, C70's
bridge machinery, and C172's own round59-kernel-vector extraction, all via
importlib, unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c174.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C79 = load_module(
    "c79_nonproduct_coupling",
    HERE.parent / "20260811-c79-nonproduct-s3s6-coupling-attempt" / "c79_nonproduct_coupling.py",
)
C71 = load_module(
    "c71_step1_triality_bridge",
    HERE.parent
    / "20260811-c71-triality-bridge-extension-and-mixing-test"
    / "c71_step1_triality_bridge.py",
)
C172 = load_module(
    "c172_real_twisted_ds6_cl9",
    HERE.parent
    / "20260906-c172-p4-escalation-item2-real-twisted-ds6-cl9"
    / "c172_real_twisted_ds6_cl9.py",
)
C70 = C79.C70
C68 = C70.C68
R59 = C79.R59

CHANNEL_GENERATORS = {
    "v": C68.su3_g102_on_channel_v,
    "s": C71.su3_g102_on_channel_s,
    "c": C71.su3_g102_on_channel_c,
}


def get_bridge_for_channel(channel: str, seed: int) -> tuple[np.ndarray, dict]:
    """Same pipeline as C79's get_bridge_to_sigma, generalized to any channel."""
    gens_channel = CHANNEL_GENERATORS[channel]()
    gens_r59 = C68.to_numpy_su3_r59()
    solve = C70.run_direct_solve(gens_r59, gens_channel, n_trials=3, norm_weight=5.0, seed=seed)
    phi = solve["best"]["phi"]
    phi_inv = np.linalg.inv(phi)
    m_matrices = [sum(phi_inv[a, k] * gens_r59[a] for a in range(8)) for k in range(8)]
    basis = C68.hom_basis(m_matrices, gens_channel)
    u, best_det = C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)
    u_inv = np.linalg.inv(u)
    residual = max(
        float(np.max(np.abs(u @ m_matrices[k] @ u_inv - gens_channel[k]))) for k in range(8)
    )
    return u, {"channel": channel, "u_det": best_det, "intertwining_residual": residual}


def get_round59_kernel_vector() -> np.ndarray:
    """Reuse C172's own reconciliation function to get round59's certified,
    physically-relevant kernel vector, embedded in the 64-dim Sigma(x)Sigma space."""
    mod = C172.load_round59_module()
    E = mod.build_clifford(conj=False)
    D = mod.build_dirac(E, mod.NOMIZU)
    recon, v_round59 = C172.reconcile_round59_vector_against_full_kernel(mod, D)
    assert recon["applicable"] and recon["round59_own_vector_is_in_full_unrestricted_ker_D"]
    v_np = np.array(v_round59.evalf(), dtype=complex).reshape(-1)
    v_np = v_np / np.linalg.norm(v_np)
    return v_np, D


def build_t_and_base(channel: str, seed: int) -> dict:
    z_gens = [np.array(z.tolist(), dtype=complex) for z in C79.ROUND67.clifford_generators()]
    h_h = C79.ROUND67.calibrate_h_H()
    d_s3_scalar = float(sp.Rational(1, 2) * h_h)

    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, _anti = C79.self_dual_anti_self_dual_triples(so4_1)

    u_channel, bridge_sanity = get_bridge_for_channel(channel, seed=seed)
    u_inv = np.linalg.inv(u_channel)
    su2_on_sigma = [u_inv @ g.astype(complex) @ u_channel for g in self_dual]
    leibniz_su2 = [C79.leibniz_matrix(g) for g in su2_on_sigma]

    E = R59.build_clifford(conj=False)
    d_s6 = C79.C73.build_numeric_dirac(E, R59.NOMIZU)
    I2 = np.eye(2, dtype=complex)
    I64 = np.eye(64, dtype=complex)
    d_joint_base = d_s3_scalar * np.kron(I2, I64) + np.kron(I2, d_s6)

    z_kron = [np.kron(z, I64) for z in z_gens]
    leib_kron = [np.kron(I2, leib) for leib in leibniz_su2]
    t_raw = sum(z_kron[i] @ leib_kron[i] for i in range(3))
    t_generator = (t_raw + t_raw.conj().T) / 2

    return {
        "d_joint_base": d_joint_base,
        "t_generator": t_generator,
        "bridge_sanity": bridge_sanity,
        "d_s3_scalar": d_s3_scalar,
    }


def compress_to_physical_subspace(matrix: np.ndarray, v_round59: np.ndarray) -> np.ndarray:
    """Project matrix onto span(e1(x)v_round59, e2(x)v_round59), return exact 2x2.
    DIAGNOSTIC ONLY -- see honesty note in full_diagonalize_track_overlap below;
    this compression alone MISSES any component of T's action that leaks OUT of
    the 2-dim subspace, which is exactly what a coupling term is supposed to do.
    """
    e1 = np.array([1.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 1.0], dtype=complex)
    basis = [np.kron(e1, v_round59), np.kron(e2, v_round59)]
    basis = np.array(basis).T  # 128x2, already orthonormal (e1,e2 orthonormal, v_round59 unit)
    return basis.conj().T @ matrix @ basis


def full_diagonalize_track_overlap(
    d_joint_base: np.ndarray, t_generator: np.ndarray, v_round59: np.ndarray, eps_values: np.ndarray
) -> list[dict]:
    """HONESTY FIX (self-caught before trusting the first draft's result): the
    2x2 diagonal-block compression above showed IDENTICALLY eigvals=[1.5,1.5]
    for every channel and every eps -- which turned out to mean T's compressed
    action on this subspace is ~0, NOT that the three channels agree on a
    genuine, non-trivial answer. That is exactly the "vacuous test" failure
    mode this project's own discipline exists to catch (same class of error as
    C172's first-draft overclaim). Diagonalizing only a 2-dim projection misses
    any part of T that couples this subspace OUT to the rest of the 128-dim
    space -- which is precisely what an entangling coupling term is supposed to
    do. Fixed here: diagonalize the FULL 128x128 D_joint(eps) at each eps, and
    track the eigenvalue(s) whose eigenvector has the largest overlap with
    span(e1(x)v_round59, e2(x)v_round59) -- reports the tracked eigenvalue AND
    the overlap itself, so a reader can tell whether the tracking stays
    meaningful (overlap near 1) or the physical vector mixes strongly into the
    rest of the spectrum (overlap drops) as eps grows.
    """
    e1 = np.array([1.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 1.0], dtype=complex)
    basis = np.array([np.kron(e1, v_round59), np.kron(e2, v_round59)]).T  # 128x2

    traces = []
    for eps in eps_values:
        d_joint = d_joint_base + eps * t_generator
        herm_residual = float(np.max(np.abs(d_joint - d_joint.conj().T)))
        d_joint_herm = (d_joint + d_joint.conj().T) / 2
        evals, evecs = np.linalg.eigh(d_joint_herm)
        overlaps = np.sum(np.abs(basis.conj().T @ evecs) ** 2, axis=0)  # per eigenvector
        top2_idx = np.argsort(overlaps)[-2:]
        top2_idx = top2_idx[np.argsort(evals[top2_idx])]
        traces.append(
            {
                "eps": float(eps),
                "tracked_eigvals": [float(evals[i]) for i in top2_idx],
                "tracked_overlaps": [float(overlaps[i]) for i in top2_idx],
                "total_overlap_top2": float(sum(overlaps[i] for i in top2_idx)),
                "herm_residual": herm_residual,
            }
        )
    return traces


def main() -> dict:
    result: dict = {}

    v_round59, _D = get_round59_kernel_vector()
    result["v_round59_norm_check"] = float(np.linalg.norm(v_round59))

    eps_values = np.linspace(-2.0, 2.0, 41)
    per_channel = {}
    per_channel_compressed_diagnostic = {}
    for channel in ("v", "s", "c"):
        built = build_t_and_base(channel, seed=42)
        result[f"bridge_sanity_{channel}"] = built["bridge_sanity"]

        compressed_t = compress_to_physical_subspace(built["t_generator"], v_round59)
        result[f"compressed_t_max_abs_entry_{channel}"] = float(np.max(np.abs(compressed_t)))
        per_channel_compressed_diagnostic[channel] = compressed_t.tolist()

        per_channel[channel] = full_diagonalize_track_overlap(
            built["d_joint_base"], built["t_generator"], v_round59, eps_values
        )

    result["eps_sweep"] = eps_values.tolist()
    result["per_channel_eigval_traces"] = per_channel
    result["diagnostic_note"] = (
        "compressed_t_max_abs_entry_* near 0 confirms the FIRST-DRAFT 2x2-"
        "compression check was vacuous (T barely acts within the 2-dim "
        "subspace alone) -- the full-diagonalization + overlap-tracking "
        "check above is the one actually used for the verdict."
    )

    # ---- cross-channel comparison (tracked eigvals, not the vacuous compression) ----
    max_diff_v_s = 0.0
    max_diff_v_c = 0.0
    max_diff_s_c = 0.0
    min_overlap_seen = 1.0
    for i in range(len(eps_values)):
        ev_v = np.array(per_channel["v"][i]["tracked_eigvals"])
        ev_s = np.array(per_channel["s"][i]["tracked_eigvals"])
        ev_c = np.array(per_channel["c"][i]["tracked_eigvals"])
        max_diff_v_s = max(max_diff_v_s, float(np.max(np.abs(ev_v - ev_s))))
        max_diff_v_c = max(max_diff_v_c, float(np.max(np.abs(ev_v - ev_c))))
        max_diff_s_c = max(max_diff_s_c, float(np.max(np.abs(ev_s - ev_c))))
        for ch in ("v", "s", "c"):
            min_overlap_seen = min(min_overlap_seen, per_channel[ch][i]["total_overlap_top2"])

    result["max_diff_v_vs_s"] = max_diff_v_s
    result["max_diff_v_vs_c"] = max_diff_v_c
    result["max_diff_s_vs_c"] = max_diff_s_c
    result["min_overlap_seen_across_sweep"] = min_overlap_seen

    tol = 1e-6
    channel_independent = max_diff_v_s < tol and max_diff_v_c < tol and max_diff_s_c < tol
    tracking_meaningful = min_overlap_seen > 0.5

    bridges_ok = all(
        result[f"bridge_sanity_{ch}"]["intertwining_residual"] < 1e-6 for ch in ("v", "s", "c")
    )

    if not bridges_ok:
        verdict = "BLOCKED-BRIDGE-CONSTRUCTION-FAILS"
    elif not tracking_meaningful:
        verdict = "ARTIFACT-STILL-PRESENT"
    elif channel_independent:
        verdict = "CHANNEL-INDEPENDENT-CONFIRMED-EXTENDS-G44-NOGO"
    else:
        verdict = "CHANNEL-DEPENDENT-GENUINE-DISCOVERY"

    result["verdict"] = {
        "bridges_ok": bridges_ok,
        "tracking_meaningful_min_overlap_gt_0.5": tracking_meaningful,
        "channel_independent": channel_independent,
        "max_diff_across_all_channel_pairs": max(max_diff_v_s, max_diff_v_c, max_diff_s_c),
        "label": verdict,
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out, indent=2, default=str))
    with open(RESULTS_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {RESULTS_PATH}")
