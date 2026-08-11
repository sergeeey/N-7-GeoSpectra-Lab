"""C81 -- redesigned non-product test with D_S6's raw kernel excluded.

C79 built a coupling term T=eps*sum Z_i(x)Leibniz(g_i) and found a
crossing; C80 completed the self-dual/anti-self-dual pair and showed BOTH
crossings are ~100% inside D_S6's already-known 36-dim raw kernel --
proving the test design itself (sweep eps, look for any crossing in the
full space) cannot discriminate genuine physics from this artifact for
ANY generic coupling. This round fixes the test design per C80's own
named next step: exclude the raw kernel BEFORE sweeping.

D_S6's spectrum has a clean gap (36 exact zeros, then |eigenvalue|>=0.8165)
-- verified directly this round. Within Delta_m (x) ker(D_S6), D_joint_base
reduces to the CONSTANT 1.5*I (D_S6 contributes nothing there), so
D_joint(eps)=1.5*I+eps*T restricted there is a straight line in eps and
crosses zero for ANY nonzero eigenvalue of T -- a mathematical certainty,
not a finding. Outside the kernel, D_S6 is genuinely nonzero and gapped,
so a crossing there would reflect real competition between D_S6 and the
coupling.

Two tests: (1) PRIMARY -- compress D_joint onto Delta_m (x) (D_S6's 28-dim
non-kernel eigenspace), sweep eps, look for crossings in this clean
56-dim space. (2) CROSS-CHECK -- on the full 128-dim spectrum (as in
C79/C80), classify every near-zero eigenvalue by raw-kernel overlap
across the whole sweep, not just at the one crossing found before.

Reuses C79's get_bridge_to_sigma/leibniz_matrix/check_su2_closure/
self_dual_anti_self_dual_triples and all of C79's own module-level
reuses, unmodified.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c81.json"


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

CROSSING_TOL = 1e-6
KERNEL_TOL = 1e-8
OVERLAP_ARTIFACT_THRESHOLD = 0.5  # >50% in raw kernel => classified as artifact


def build_t_generator(triple: np.ndarray) -> np.ndarray:
    u_v, _bridge_sanity = C79.get_bridge_to_sigma()
    u_v_inv = np.linalg.inv(u_v)
    su2_on_sigma = [u_v_inv @ g.astype(complex) @ u_v for g in triple]
    leibniz_su2 = [C79.leibniz_matrix(g) for g in su2_on_sigma]

    z_gens = [np.array(z.tolist(), dtype=complex) for z in C79.ROUND67.clifford_generators()]
    I2 = np.eye(2, dtype=complex)
    I64 = np.eye(64, dtype=complex)
    z_kron = [np.kron(z, I64) for z in z_gens]
    leib_kron = [np.kron(I2, leib) for leib in leibniz_su2]
    t_raw = sum(z_kron[i] @ leib_kron[i] for i in range(3))
    return (t_raw + t_raw.conj().T) / 2


def run_for_triple(triple: np.ndarray, label: str, d_s6: np.ndarray, d_s3_scalar: float) -> dict:
    I2 = np.eye(2, dtype=complex)
    I64 = np.eye(64, dtype=complex)
    d_joint_base = d_s3_scalar * np.kron(I2, I64) + np.kron(I2, d_s6)
    t_generator = build_t_generator(triple)

    # --- Step A: D_S6 spectral decomposition, raw kernel vs non-kernel ---
    d_s6_evals, d_s6_evecs = np.linalg.eigh(d_s6)
    kernel_mask = np.abs(d_s6_evals) < KERNEL_TOL
    nonkernel_mask = ~kernel_mask
    kernel_dim = int(np.sum(kernel_mask))
    nonkernel_dim = int(np.sum(nonkernel_mask))
    kernel_projector_s6 = d_s6_evecs[:, kernel_mask] @ d_s6_evecs[:, kernel_mask].conj().T

    # --- Step B: PRIMARY test -- compress onto Delta_m (x) non-kernel ---
    # basis for the 56-dim compressed space: Delta_m (2) tensor non-kernel eigvecs (28)
    nonkernel_evecs = d_s6_evecs[:, nonkernel_mask]  # (64, 28)
    nonkernel_evals = d_s6_evals[nonkernel_mask]  # (28,)
    compressed_basis = np.kron(I2, nonkernel_evecs)  # (128, 56)

    d_joint_base_compressed = compressed_basis.conj().T @ d_joint_base @ compressed_basis
    t_compressed = compressed_basis.conj().T @ t_generator @ compressed_basis

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

    # --- Step C: CROSS-CHECK -- full 128-dim spectrum, classify by kernel overlap ---
    full_crossings_all = []
    full_crossings_nonartifact = []
    for eps in eps_values:
        d_joint = d_joint_base + eps * t_generator
        evals, evecs = np.linalg.eigh(d_joint)
        near_zero_idx = np.where(np.abs(evals) < 1e-4)[0]  # wider net than CROSSING_TOL
        for idx in near_zero_idx:
            if abs(evals[idx]) >= CROSSING_TOL:
                continue
            v = evecs[:, idx].reshape(2, 64)
            proj = np.array([kernel_projector_s6 @ v[j] for j in range(2)])
            frac = float(np.linalg.norm(proj) / np.linalg.norm(v))
            entry = {"eps": float(eps), "eigval": float(evals[idx]), "frac_in_raw_kernel": frac}
            full_crossings_all.append(entry)
            if frac < OVERLAP_ARTIFACT_THRESHOLD:
                full_crossings_nonartifact.append(entry)

    return {
        "label": label,
        "d_s6_kernel_dim": kernel_dim,
        "d_s6_nonkernel_dim": nonkernel_dim,
        "d_s6_nonkernel_min_abs_eigenvalue": float(np.min(np.abs(nonkernel_evals))),
        "compressed_eps0_min_abs_eigval": eigval_base_compressed,
        "compressed_n_crossings": len(compressed_crossings),
        "compressed_crossings": compressed_crossings,
        "compressed_global_min": float(min_abs_compressed.min()),
        "compressed_global_min_at_eps": float(eps_values[int(np.argmin(min_abs_compressed))]),
        "full_spectrum_all_crossings": full_crossings_all,
        "full_spectrum_nonartifact_crossings": full_crossings_nonartifact,
    }


def main() -> None:
    C73 = C79.C73
    R59 = C79.R59

    E = R59.build_clifford(conj=False)
    d_s6 = C73.build_numeric_dirac(E, R59.NOMIZU)
    d_s3_scalar = float(C79.sp.Rational(1, 2) * C79.ROUND67.calibrate_h_H())

    so4_all = C79.SO4MOD.build_so4xso4_basis()
    so4_1 = so4_all[0:6]
    self_dual, anti_self_dual = C79.self_dual_anti_self_dual_triples(so4_1)

    print("=== D_S6 spectral gap check ===")
    evals = np.linalg.eigvalsh(d_s6)
    print("unique eigenvalues (rounded):", sorted(set(np.round(evals, 4))))

    print("\n=== Self-dual triple, raw-kernel-excluded ===")
    self_result = run_for_triple(self_dual, "self_dual", d_s6, d_s3_scalar)
    print(
        f"compressed: eps0_min={self_result['compressed_eps0_min_abs_eigval']:.4f}, "
        f"n_crossings={self_result['compressed_n_crossings']}, "
        f"global_min={self_result['compressed_global_min']:.6f} "
        f"at eps={self_result['compressed_global_min_at_eps']:.3f}"
    )
    print(
        f"full-spectrum: {len(self_result['full_spectrum_all_crossings'])} total near-zero "
        f"crossings, {len(self_result['full_spectrum_nonartifact_crossings'])} non-artifact "
        f"(frac_in_raw_kernel < {OVERLAP_ARTIFACT_THRESHOLD})"
    )

    print("\n=== Anti-self-dual triple, raw-kernel-excluded ===")
    anti_result = run_for_triple(anti_self_dual, "anti_self_dual", d_s6, d_s3_scalar)
    print(
        f"compressed: eps0_min={anti_result['compressed_eps0_min_abs_eigval']:.4f}, "
        f"n_crossings={anti_result['compressed_n_crossings']}, "
        f"global_min={anti_result['compressed_global_min']:.6f} "
        f"at eps={anti_result['compressed_global_min_at_eps']:.3f}"
    )
    print(
        f"full-spectrum: {len(anti_result['full_spectrum_all_crossings'])} total near-zero "
        f"crossings, {len(anti_result['full_spectrum_nonartifact_crossings'])} non-artifact "
        f"(frac_in_raw_kernel < {OVERLAP_ARTIFACT_THRESHOLD})"
    )

    no_genuine_signal = (
        self_result["compressed_n_crossings"] == 0
        and anti_result["compressed_n_crossings"] == 0
        and len(self_result["full_spectrum_nonartifact_crossings"]) == 0
        and len(anti_result["full_spectrum_nonartifact_crossings"]) == 0
    )

    results = {
        "d_s6_eigenvalue_spectrum_rounded": sorted({float(x) for x in np.round(evals, 4)}),
        "self_dual": self_result,
        "anti_self_dual": anti_result,
        "no_genuine_signal_found": no_genuine_signal,
        "conclusion": (
            "With D_S6's raw 36-dim kernel excluded by construction (compressed "
            "test) and independently cross-checked (full-spectrum overlap filter), "
            + (
                "NEITHER so(4)_1 half produces any crossing outside the raw-kernel "
                "artifact mechanism. This confirms C79/C80's crossings were the "
                "ENTIRE signal, fully explained by the artifact -- with it properly "
                "excluded, this specific non-product postulate is a clean, honest "
                "NULL, not merely 'explained away.'"
                if no_genuine_signal
                else "at least one crossing survives raw-kernel exclusion -- this is "
                "a genuinely new finding requiring the same extra scrutiny C79's "
                "original crossing received before being trusted, not immediate "
                "acceptance."
            )
        ),
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
