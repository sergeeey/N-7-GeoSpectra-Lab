"""C178: proper degenerate perturbation theory on the FULL 36-dim raw
kernel of round59's D (x2 for the S3 factor = 72-dim degenerate subspace),
answering the question C174's own Relaxation Map named and did not
attempt: does the projected zeroth-order Hamiltonian T_0 = P^dagger T P
(the standard degenerate-PT object, whose eigenvalues ARE the first-order
energy corrections) have a channel-independent eigenvalue spectrum across
v/s/c, unlike C174's own two artifact-dominated single-vector attempts?

Reuses C174's own build_t_and_base() (unmodified, via importlib) for
d_joint_base/t_generator per channel, and C174's get_round59_kernel_vector()
for v_round59 -- no reconstruction of round59's D or the channel bridges,
only the NEW degenerate-PT machinery on top.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c178.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C174 = load_module(
    "c174_channel_independence_check",
    HERE.parent
    / "20260906-c174-ob11-nonproduct-d-channel-independence"
    / "c174_channel_independence_check.py",
)

TOL_KERNEL = 1e-8
TOL_CHANNEL_MATCH = 1e-6


def extract_d_s6(d_joint_base: np.ndarray, d_s3_scalar: float) -> np.ndarray:
    """d_joint_base = d_s3_scalar*kron(I2,I64) + kron(I2,d_s6) -- extract
    d_s6 from either diagonal 64x64 block (both blocks are identical by
    construction; this is checked, not assumed, in main())."""
    return d_joint_base[0:64, 0:64] - d_s3_scalar * np.eye(64, dtype=complex)


def compute_kernel_basis(d_s6: np.ndarray, tol: float = TOL_KERNEL) -> dict:
    _u, s, vh = np.linalg.svd(d_s6)
    null_mask = s < tol
    # svd of a square matrix returns 64 singular values; null vectors are
    # the corresponding rows of vh (since d_s6 @ v = 0 for v with sv~0)
    kernel_basis = vh.conj().T[:, null_mask]  # 64 x dim(ker)
    return {
        "dim_kernel": int(kernel_basis.shape[1]),
        "smallest_nonzero_singular_value": float(np.sort(s)[np.sum(null_mask)])
        if np.sum(null_mask) < 64
        else None,
        "largest_null_singular_value": float(np.max(s[null_mask])) if np.any(null_mask) else 0.0,
        "kernel_basis": kernel_basis,
    }


def build_degenerate_subspace_basis(kernel_basis: np.ndarray) -> np.ndarray:
    """P: 128 x (2*dim_ker), columns = kron(e1,k_j) then kron(e2,k_j) for
    each kernel basis vector k_j. Orthonormal by construction (e1,e2 and
    kernel_basis columns are each orthonormal)."""
    e1 = np.array([1.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 1.0], dtype=complex)
    dim_ker = kernel_basis.shape[1]
    cols = []
    for j in range(dim_ker):
        cols.append(np.kron(e1, kernel_basis[:, j]))
    for j in range(dim_ker):
        cols.append(np.kron(e2, kernel_basis[:, j]))
    return np.array(cols).T  # 128 x 2*dim_ker


def project_operator(op: np.ndarray, p: np.ndarray) -> np.ndarray:
    return p.conj().T @ op @ p


def pt_validity_check(
    d_joint_base: np.ndarray,
    t_generator: np.ndarray,
    p: np.ndarray,
    t0_eigvals: np.ndarray,
    d_s3_scalar: float,
    eps: float,
) -> dict:
    """Direct numerical cross-check: at small eps, do the FULL operator's
    eigenvalues near d_s3_scalar shift by ~eps*(T_0 eigenvalue)? Uses the
    eigenvectors with the largest overlap with span(columns of P) to
    identify the 'same' states, per standard degenerate PT bookkeeping."""
    dim_deg = p.shape[1]
    d_full = d_joint_base + eps * t_generator
    d_full_herm = (d_full + d_full.conj().T) / 2
    evals, evecs = np.linalg.eigh(d_full_herm)
    overlaps = np.sum(np.abs(p.conj().T @ evecs) ** 2, axis=0)
    top_idx = np.argsort(overlaps)[-dim_deg:]
    tracked_evals = np.sort(evals[top_idx])
    predicted = d_s3_scalar + eps * np.sort(t0_eigvals)
    max_abs_diff = float(np.max(np.abs(tracked_evals - predicted)))
    min_overlap_in_tracked = float(np.min(overlaps[top_idx]))
    return {
        "eps": eps,
        "max_abs_diff_actual_vs_predicted": max_abs_diff,
        "min_overlap_in_tracked_set": min_overlap_in_tracked,
        "relative_to_eps_squared": max_abs_diff / eps**2 if eps != 0 else None,
    }


def gauge_noise_vs_channel_signal(seeds: list[int]) -> dict:
    """CRITICAL self-check, added after the first run's own
    CHANNEL-DEPENDENT result: C142/OB4's own established finding is that
    C70/C71's U_v/U_s/U_c bridges are Inn(su(3))-orbit gauge freedom, NOT
    unique -- run_direct_solve's optimizer can land on any gauge-equivalent
    representative. Before trusting a "channels differ" verdict, check
    whether the SAME channel, re-bridged with a DIFFERENT seed, shows a
    similar-sized shift (gauge noise) -- if between-channel differences do
    not exceed within-channel (same-channel, different-seed) noise, the
    "channel-dependence" is a gauge artifact, not a physical finding."""
    per_channel_spectra = {"v": [], "s": [], "c": []}
    for channel in ("v", "s", "c"):
        for seed in seeds:
            built = C174.build_t_and_base(channel, seed=seed)
            d_s6 = extract_d_s6(built["d_joint_base"], built["d_s3_scalar"])
            ker = compute_kernel_basis(d_s6)
            p = build_degenerate_subspace_basis(ker["kernel_basis"])
            t0 = project_operator(built["t_generator"], p)
            evals = np.sort(np.linalg.eigvalsh((t0 + t0.conj().T) / 2))
            per_channel_spectra[channel].append(evals)

    within_channel_pairwise_max = {}
    for channel in ("v", "s", "c"):
        arr = np.array(per_channel_spectra[channel])
        pmax = 0.0
        for i in range(len(seeds)):
            for j in range(i + 1, len(seeds)):
                pmax = max(pmax, float(np.max(np.abs(arr[i] - arr[j]))))
        within_channel_pairwise_max[channel] = pmax

    means = {ch: np.array(per_channel_spectra[ch]).mean(axis=0) for ch in ("v", "s", "c")}
    between_mean_diff = {
        "v_vs_s": float(np.max(np.abs(means["v"] - means["s"]))),
        "v_vs_c": float(np.max(np.abs(means["v"] - means["c"]))),
        "s_vs_c": float(np.max(np.abs(means["s"] - means["c"]))),
    }
    max_within_noise = max(within_channel_pairwise_max.values())
    signal_to_noise = {k: v / max_within_noise for k, v in between_mean_diff.items()}

    return {
        "seeds_used": seeds,
        "within_channel_pairwise_max_diff": within_channel_pairwise_max,
        "max_within_channel_noise": max_within_noise,
        "between_channel_mean_spectrum_diff": between_mean_diff,
        "signal_to_noise_ratio": signal_to_noise,
        "v_distinguishable_from_s_and_c": (
            signal_to_noise["v_vs_s"] > 2.0 and signal_to_noise["v_vs_c"] > 2.0
        ),
        "s_and_c_distinguishable_from_each_other": signal_to_noise["s_vs_c"] > 2.0,
    }


def main() -> dict:
    result: dict = {}

    v_round59, _D_sympy = C174.get_round59_kernel_vector()

    per_channel_built = {}
    for channel in ("v", "s", "c"):
        per_channel_built[channel] = C174.build_t_and_base(channel, seed=42)

    # --- honesty check 1: d_joint_base (hence d_s6) is channel-independent,
    # verified not assumed ---
    base_v = per_channel_built["v"]["d_joint_base"]
    d_joint_base_channel_independent = all(
        float(np.max(np.abs(per_channel_built[ch]["d_joint_base"] - base_v))) < 1e-12
        for ch in ("s", "c")
    )
    result["d_joint_base_identical_across_channels"] = d_joint_base_channel_independent

    d_s3_scalar = per_channel_built["v"]["d_s3_scalar"]
    d_s6 = extract_d_s6(base_v, d_s3_scalar)
    result["d_s6_is_hermitian_residual"] = float(np.max(np.abs(d_s6 - d_s6.conj().T)))

    # --- honesty check 2: block [64:128,64:128] gives the SAME d_s6 (kron(I2,d_s6)
    # structure actually holds, not assumed) ---
    d_s6_other_block = base_v[64:128, 64:128] - d_s3_scalar * np.eye(64, dtype=complex)
    result["d_s6_both_blocks_agree_residual"] = float(np.max(np.abs(d_s6 - d_s6_other_block)))

    # --- kernel of D ---
    kernel_info = compute_kernel_basis(d_s6)
    result["dim_kernel_D"] = kernel_info["dim_kernel"]
    result["largest_null_singular_value"] = kernel_info["largest_null_singular_value"]
    result["smallest_nonzero_singular_value"] = kernel_info["smallest_nonzero_singular_value"]
    result["dim_kernel_matches_established_36"] = kernel_info["dim_kernel"] == 36

    kernel_basis = kernel_info["kernel_basis"]

    # --- honesty check 3: v_round59 lies within this SVD-computed kernel ---
    coeffs = kernel_basis.conj().T @ v_round59
    reconstructed = kernel_basis @ coeffs
    residual_v_round59_in_kernel = float(np.max(np.abs(reconstructed - v_round59)))
    result["v_round59_in_svd_kernel_residual"] = residual_v_round59_in_kernel

    # --- build 72-dim (2*dim_ker) degenerate subspace ---
    p = build_degenerate_subspace_basis(kernel_basis)
    result["degenerate_subspace_dim"] = p.shape[1]

    # --- project T for each channel, diagonalize ---
    per_channel_t0_eigvals = {}
    for channel in ("v", "s", "c"):
        t_gen = per_channel_built[channel]["t_generator"]
        t0 = project_operator(t_gen, p)
        t0_herm_residual = float(np.max(np.abs(t0 - t0.conj().T)))
        evals = np.linalg.eigvalsh((t0 + t0.conj().T) / 2)
        per_channel_t0_eigvals[channel] = {
            "eigvals_sorted": evals.tolist(),
            "t0_herm_residual": t0_herm_residual,
        }
    result["per_channel_t0"] = per_channel_t0_eigvals

    # --- pairwise channel comparison ---
    ev_v = np.array(per_channel_t0_eigvals["v"]["eigvals_sorted"])
    ev_s = np.array(per_channel_t0_eigvals["s"]["eigvals_sorted"])
    ev_c = np.array(per_channel_t0_eigvals["c"]["eigvals_sorted"])
    max_diff_v_s = float(np.max(np.abs(ev_v - ev_s)))
    max_diff_v_c = float(np.max(np.abs(ev_v - ev_c)))
    max_diff_s_c = float(np.max(np.abs(ev_s - ev_c)))
    result["max_diff_v_vs_s"] = max_diff_v_s
    result["max_diff_v_vs_c"] = max_diff_v_c
    result["max_diff_s_vs_c"] = max_diff_s_c

    # --- degenerate-PT validity cross-check (channel v, two small eps) ---
    pt_checks = []
    for eps in (1e-3, 1e-4):
        pt_checks.append(
            pt_validity_check(
                per_channel_built["v"]["d_joint_base"],
                per_channel_built["v"]["t_generator"],
                p,
                ev_v,
                d_s3_scalar,
                eps,
            )
        )
    result["pt_validity_checks_channel_v"] = pt_checks

    # --- physical-vector overlap: which corrected eigenvector is closest
    # to round59's own specific direction? (informational, per Step -5g) ---
    e1 = np.array([1.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 1.0], dtype=complex)
    physical_vecs = np.array([np.kron(e1, v_round59), np.kron(e2, v_round59)]).T  # 128x2
    physical_in_p_coords = p.conj().T @ physical_vecs  # 72x2, coords in the P basis

    per_channel_overlap_report = {}
    for channel in ("v", "s", "c"):
        t_gen = per_channel_built[channel]["t_generator"]
        t0 = project_operator(t_gen, p)
        t0 = (t0 + t0.conj().T) / 2
        evals, evecs = np.linalg.eigh(t0)
        overlaps = np.sum(np.abs(evecs.conj().T @ physical_in_p_coords) ** 2, axis=1)
        top_idx = int(np.argmax(overlaps))
        per_channel_overlap_report[channel] = {
            "best_eigval": float(evals[top_idx]),
            "best_overlap_with_physical_subspace": float(overlaps[top_idx]),
        }
    result["physical_direction_overlap_per_channel"] = per_channel_overlap_report

    # --- gauge-noise-vs-channel-signal check (added after first run's own
    # CHANNEL-DEPENDENT result, before trusting it -- see function docstring) ---
    gauge_check = gauge_noise_vs_channel_signal(seeds=[42, 1, 7, 99, 123, 7000, 55, 314])
    result["gauge_noise_vs_channel_signal"] = gauge_check

    # ------------------------------------------------------------------
    # aggregate verdict
    # ------------------------------------------------------------------
    substrate_ok = (
        d_joint_base_channel_independent
        and result["d_s6_is_hermitian_residual"] < 1e-10
        and result["d_s6_both_blocks_agree_residual"] < 1e-10
        and result["dim_kernel_matches_established_36"]
        and residual_v_round59_in_kernel < 1e-6
    )

    pt_valid = all(
        chk["max_abs_diff_actual_vs_predicted"] < 10 * chk["eps"] ** 2 for chk in pt_checks
    ) and all(chk["min_overlap_in_tracked_set"] > 0.9 for chk in pt_checks)

    channel_independent = (
        max_diff_v_s < TOL_CHANNEL_MATCH
        and max_diff_v_c < TOL_CHANNEL_MATCH
        and max_diff_s_c < TOL_CHANNEL_MATCH
    )

    v_signal_real = gauge_check["v_distinguishable_from_s_and_c"]
    s_c_signal_real = gauge_check["s_and_c_distinguishable_from_each_other"]

    if not substrate_ok:
        verdict = "SUBSTRATE-MISMATCH"
    elif not pt_valid:
        verdict = "PT-INVALID"
    elif channel_independent:
        verdict = "CHANNEL-INDEPENDENT-SPECTRUM-CONFIRMED"
    elif v_signal_real and not s_c_signal_real:
        # NOT one of the four originally pre-registered boxes -- see
        # claim.md's own kill-criterion table and decision.md for why this
        # nuanced outcome is reported honestly rather than force-fit into
        # CHANNEL-DEPENDENT or CHANNEL-INDEPENDENT.
        verdict = "PARTIAL-V-DIFFERS-S-C-INDISTINGUISHABLE"
    elif v_signal_real and s_c_signal_real:
        verdict = "CHANNEL-DEPENDENT-GENUINE-DISCOVERY"
    else:
        verdict = "GAUGE-NOISE-DOMINATED-INCONCLUSIVE"

    result["verdict"] = {
        "label": verdict,
        "substrate_ok": substrate_ok,
        "pt_valid": pt_valid,
        "channel_independent_naive": channel_independent,
        "max_diff_across_all_pairs_single_seed": max(max_diff_v_s, max_diff_v_c, max_diff_s_c),
        "v_signal_exceeds_gauge_noise": v_signal_real,
        "s_c_signal_exceeds_gauge_noise": s_c_signal_real,
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out["verdict"], indent=2))
    with open(RESULTS_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print(f"\nSaved: {RESULTS_PATH}")
