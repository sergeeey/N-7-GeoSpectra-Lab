"""C86 (C84B/C) -- does C79-C83's coupling postulate connect physical n=0
and n=1 within the SAME Peter-Weyl level k=1's full Hilbert space?

Context: C85 certified an explicit representation substrate for S3's
Dirac operator at any level k (Meier's construction, repaired eq 6.3).
Re-indexing established there: physical n's sigma=-1 branch is level
k=n DIRECTLY; physical n's sigma=+1 branch is level k=n+1's "+1/2"
eigenspace. Consequence, not previously noticed: level k=1's OWN full
8-dimensional Hilbert space (q x p x r, q,p in {0,1}, r in {0,1})
contains BOTH physical n=1's sigma=-1 branch (D-bar=-1, mult 3 per
q-copy, total 6) AND physical n=0's sigma=+1 branch (D-bar=+3, mult 1
per q-copy, total 2) SIMULTANEOUSLY -- the first time these two
different physical n's coexist in one properly-normalized, certified
Hilbert space (C79-C83's own n=0 construction used an ad hoc scalar
approximation, never the genuine representation).

The question this round asks (C84B, in the reviewer's own framing):
does C79-C83's coupling operator T = sum_i Z_i (x) Leibniz(g_i) --
built from round67's LEVEL-INDEPENDENT 2x2 Clifford generator Z_i
(Clifford mult on the r/Delta_m index only) -- have nonzero matrix
elements connecting these two physical n's within k=1's own space?

This is NOT obviously zero by inspection: T is built to act as
identity on the (p,q) orbital indices (Z_i touches r only), which
might suggest "no coupling to orbital structure" -- but D-bar's own
eigenspaces (the "-1" and "+3" branches) are GENUINE (r,p)-MIXED
combinations (Meier's own basis: {e0(x)|p>, e2(x)|p-1>} pairs), not
simply "fixed p, varying r". T preserving p as a tensor index does NOT
automatically mean T preserves D-bar's own eigenspaces. This must be
checked numerically, not assumed either way -- exactly the discipline
this project's own OB10/C85 lessons established.

Reuses round67's clifford_generators/calibrate_h_H, C79's
get_bridge_to_sigma/self_dual_anti_self_dual_triples/SO4MOD/leibniz_matrix,
C81's kernel-exclusion methodology (generalized here from a scalar
d_s3_scalar to a genuine matrix block), C73's build_numeric_dirac, and
C85's certified build_l_matrices/right_mult_matrix_on_ab, all unmodified
except C81's run_for_triple which is generalized (not copy-pasted) to
accept a matrix D_S3 block instead of a bare scalar.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c86.json"


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
ROUND67 = C79.ROUND67
C85 = load_module(
    "c85_certification",
    HERE.parent / "20260812-c85-peter-weyl-representation-certification" / "c85_certification.py",
)

CROSSING_TOL = 1e-6
KERNEL_TOL = 1e-8
OVERLAP_ARTIFACT_THRESHOLD = 0.5


# ---------------------------------------------------------------------------
# Step 1: build the FULL k=1 D_S3 block (q x p x r, dim 8), certified substrate
# ---------------------------------------------------------------------------


def build_full_level_d_s3(k: int) -> tuple[np.ndarray, dict]:
    """D_S3 on the FULL level-k Hilbert space (q-copies x p x r), dimension
    (k+1)*2*(k+1) = 2*(k+1)^2. D-bar doesn't touch q (a trivial multiplicity
    label) or mix q with (p,r), so D_S3_full = I_{k+1}(q) (x) (D-bar_pr - 1.5*I).
    Uses C85's REPAIRED (certified) l-matrices, not the literal (buggy for
    k>=2) transcription."""
    right_mult = [
        C85.right_mult_matrix_on_ab(u) for u in [(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    ]
    l1, l2, l3 = C85.build_l_matrices(k, "repaired")
    dbar_pr = C85.build_dbar([l1, l2, l3], right_mult)  # (k+1)*2 dim, (p,r) basis
    dbar_pr_numeric = np.array(dbar_pr.evalf().tolist(), dtype=complex)

    dim_pr = dbar_pr_numeric.shape[0]
    # D-bar's OWN eigenvalues are already real (Meier's eq 6.4: -k, k+2),
    # NOT "i*D-bar" -- that was a leftover convention from an earlier,
    # abandoned script draft. Check D-bar itself for Hermiticity directly.
    hermiticity_of_dbar = float(np.max(np.abs(dbar_pr_numeric - dbar_pr_numeric.conj().T)))
    eigs_pr = sorted(float(np.real(v)) for v in np.linalg.eigvals(dbar_pr_numeric))

    d_s3_pr = dbar_pr_numeric - 1.5 * np.eye(dim_pr, dtype=complex)
    I_q = np.eye(k + 1, dtype=complex)
    d_s3_full = np.kron(I_q, d_s3_pr)  # (k+1)*dim_pr = 2*(k+1)^2 total

    return d_s3_full, {
        "k": k,
        "dim_pr": dim_pr,
        "dim_full": d_s3_full.shape[0],
        "dbar_pr_hermiticity_residual": hermiticity_of_dbar,
        "dbar_pr_eigenvalues_raw": sorted(round(v, 6) for v in eigs_pr),
    }


def check_d_s3_full_matches_target(d_s3_full: np.ndarray, k: int) -> dict:
    """[VERIFIED-numpy] Confirm the FULL level-k D_S3 reproduces round67's
    own target for BOTH physical n's living in this level: n=k (sigma=-1,
    D=-(k+3/2)) and n=k-1 (sigma=+1, D=+(k-1+3/2)=+(k+1/2)). D_S3's own
    eigenvalues are already real (inherited from D-bar's), no "i*" needed."""
    eigvals = sorted(float(np.real(v)) for v in np.linalg.eigvals(d_s3_full))
    grouped: list[list[float]] = []
    for v in eigvals:
        if grouped and abs(grouped[-1][0] - v) < 1e-6:
            grouped[-1][1] += 1
        else:
            grouped.append([v, 1])
    found = {round(v, 4): int(m) for v, m in grouped}

    n_minus = k  # sigma=-1 branch, D=-(n+3/2)=-(k+3/2)
    n_plus = k - 1  # sigma=+1 branch, D=+(n+3/2)=+((k-1)+3/2)=+(k+1/2)
    target_minus_val = round(-(n_minus + 1.5), 4)
    target_minus_mult = (n_minus + 1) * (n_minus + 2)
    result = {
        "n_minus": n_minus,
        "target_minus_eigenvalue": target_minus_val,
        "target_minus_multiplicity": target_minus_mult,
        "found_minus_multiplicity": found.get(target_minus_val),
        "minus_matches": found.get(target_minus_val) == target_minus_mult,
    }
    if n_plus >= 0:
        target_plus_val = round(n_plus + 1.5, 4)
        target_plus_mult = (n_plus + 1) * (n_plus + 2)
        result.update(
            {
                "n_plus": n_plus,
                "target_plus_eigenvalue": target_plus_val,
                "target_plus_multiplicity": target_plus_mult,
                "found_plus_multiplicity": found.get(target_plus_val),
                "plus_matches": found.get(target_plus_val) == target_plus_mult,
            }
        )
    else:
        result.update({"n_plus": None, "plus_matches": True})  # not applicable at k=0
    result["all_eigenvalues_with_multiplicity"] = grouped
    result["both_match"] = result["minus_matches"] and result["plus_matches"]
    return result


# ---------------------------------------------------------------------------
# Step 2: build T_1 -- C79's coupling, embedded via identity on (p,q)
# ---------------------------------------------------------------------------


def build_coupling_on_full_level(k: int, triple: np.ndarray, dim_pr: int) -> np.ndarray:
    """T_k = I_q (x) [I_p (x) Z_i] (x) Leibniz(g_i), summed over i. Z_i acts
    ONLY on the r-index within the (p,r) 4-dim block (matches C85's own
    Kronecker convention: build_dbar uses kronecker_product(l_mat, rmult),
    i.e. p slow / r fast -- Z_i here must use the SAME r-fast convention:
    kron(I_p, Z_i))."""
    z_gens = [np.array(z.tolist(), dtype=complex) for z in ROUND67.clifford_generators()]
    dim_p = dim_pr // 2  # r is 2-dim
    I_p = np.eye(dim_p, dtype=complex)
    I_q = np.eye(k + 1, dtype=complex)

    u_v, _ = C79.get_bridge_to_sigma()
    u_v_inv = np.linalg.inv(u_v)
    su2_on_sigma = [u_v_inv @ g.astype(complex) @ u_v for g in triple]
    leibniz_su2 = [C79.leibniz_matrix(g) for g in su2_on_sigma]

    t_raw = sum(np.kron(np.kron(I_q, np.kron(I_p, z_gens[i])), leibniz_su2[i]) for i in range(3))
    return t_raw


# ---------------------------------------------------------------------------
# Step 3: raw-kernel-excluded spectral flow, generalized from C81's scalar
# version to a genuine D_S3 matrix block
# ---------------------------------------------------------------------------


def run_full_level_test(d_s3_full: np.ndarray, t_generator: np.ndarray, d_s6: np.ndarray) -> dict:
    dim_orb = d_s3_full.shape[0]
    I_orb = np.eye(dim_orb, dtype=complex)
    I64 = np.eye(64, dtype=complex)
    d_joint_base = np.kron(d_s3_full, I64) + np.kron(I_orb, d_s6)

    herm_residual_base = float(np.max(np.abs(d_joint_base - d_joint_base.conj().T)))
    herm_residual_t_raw = float(np.max(np.abs(t_generator - t_generator.conj().T)))
    t_hermitized = (t_generator + t_generator.conj().T) / 2

    d_s6_evals, d_s6_evecs = np.linalg.eigh(d_s6)
    kernel_mask = np.abs(d_s6_evals) < KERNEL_TOL
    nonkernel_mask = ~kernel_mask
    kernel_dim = int(np.sum(kernel_mask))
    nonkernel_dim = int(np.sum(nonkernel_mask))
    kernel_projector_s6 = d_s6_evecs[:, kernel_mask] @ d_s6_evecs[:, kernel_mask].conj().T

    nonkernel_evecs = d_s6_evecs[:, nonkernel_mask]
    compressed_basis = np.kron(I_orb, nonkernel_evecs)
    d_joint_base_compressed = compressed_basis.conj().T @ d_joint_base @ compressed_basis
    t_compressed = compressed_basis.conj().T @ t_hermitized @ compressed_basis

    eigval_base_compressed = float(np.min(np.abs(np.linalg.eigvalsh(d_joint_base_compressed))))

    eps_values = np.linspace(-2.0, 2.0, 161)
    min_abs_compressed = []
    for eps in eps_values:
        ev = np.linalg.eigvalsh(d_joint_base_compressed + eps * t_compressed)
        min_abs_compressed.append(float(np.min(np.abs(ev))))
    min_abs_compressed = np.array(min_abs_compressed)
    compressed_crossings = [
        {"eps": float(eps_values[i]), "min_abs_eigval": float(min_abs_compressed[i])}
        for i in np.where(min_abs_compressed < CROSSING_TOL)[0]
    ]

    full_crossings_all = []
    full_crossings_nonartifact = []
    for eps in eps_values:
        d_joint = d_joint_base + eps * t_hermitized
        evals, evecs = np.linalg.eigh(d_joint)
        near_zero_idx = np.where(np.abs(evals) < 1e-4)[0]
        for idx in near_zero_idx:
            if abs(evals[idx]) >= CROSSING_TOL:
                continue
            v = evecs[:, idx].reshape(dim_orb, 64)
            proj = np.array([kernel_projector_s6 @ v[j] for j in range(dim_orb)])
            frac = float(np.linalg.norm(proj) / np.linalg.norm(v))
            entry = {"eps": float(eps), "eigval": float(evals[idx]), "frac_in_raw_kernel": frac}
            full_crossings_all.append(entry)
            if frac < OVERLAP_ARTIFACT_THRESHOLD:
                full_crossings_nonartifact.append(entry)

    return {
        "dim_orb": dim_orb,
        "dim_joint": d_joint_base.shape[0],
        "herm_residual_base": herm_residual_base,
        "herm_residual_t_raw_before_hermitizing": herm_residual_t_raw,
        "d_s6_kernel_dim": kernel_dim,
        "d_s6_nonkernel_dim": nonkernel_dim,
        "compressed_eps0_min_abs_eigval": eigval_base_compressed,
        "compressed_n_crossings": len(compressed_crossings),
        "compressed_crossings": compressed_crossings,
        "compressed_global_min": float(min_abs_compressed.min()),
        "compressed_global_min_at_eps": float(eps_values[int(np.argmin(min_abs_compressed))]),
        "full_spectrum_nonartifact_crossings": full_crossings_nonartifact,
        "full_spectrum_all_crossings_count": len(full_crossings_all),
    }


def main() -> None:
    K = 1
    print(f"=== Step 1: build FULL level k={K} D_S3 (certified substrate) ===")
    d_s3_full, d_s3_info = build_full_level_d_s3(K)
    print(d_s3_info)

    print("\n=== Step 2: verify D_S3 reproduces BOTH physical n's living in k=1 ===")
    target_check = check_d_s3_full_matches_target(d_s3_full, K)
    print(target_check)
    assert target_check["both_match"], (
        "D_S3 full-level construction does not match round67's own target -- stop"
    )

    print("\n=== Step 3: build T_1 (C79's coupling, embedded via identity on p,q) ===")
    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_1)
    dim_pr = d_s3_info["dim_pr"]
    t_self = build_coupling_on_full_level(K, self_dual, dim_pr)
    t_anti = build_coupling_on_full_level(K, anti_self_dual, dim_pr)
    print(f"T_1 (self-dual) shape: {t_self.shape}, T_1 (anti-self-dual) shape: {t_anti.shape}")

    print(
        "\n=== Step 4: build D_S6, run raw-kernel-excluded test on the FULL 512-dim joint space ==="
    )
    R59 = C79.R59
    C73 = C79.C73
    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)

    results = {}
    for label, t_gen in (("self_dual", t_self), ("anti_self_dual", t_anti)):
        r = run_full_level_test(d_s3_full, t_gen, d_s6)
        results[label] = r
        print(
            f"  {label}: compressed_n_crossings={r['compressed_n_crossings']}, "
            f"nonartifact_full_crossings={len(r['full_spectrum_nonartifact_crossings'])}, "
            f"global_min={r['compressed_global_min']:.6f} at eps={r['compressed_global_min_at_eps']:.3f}"
        )

    no_genuine_signal = all(
        r["compressed_n_crossings"] == 0 and len(r["full_spectrum_nonartifact_crossings"]) == 0
        for r in results.values()
    )
    print(f"\nno_genuine_signal_found (n=0<->n=1 coupling, this specific T): {no_genuine_signal}")

    out = {
        "k": K,
        "d_s3_full_info": d_s3_info,
        "target_crosscheck": target_check,
        "results": results,
        "no_genuine_signal_found": no_genuine_signal,
    }
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
