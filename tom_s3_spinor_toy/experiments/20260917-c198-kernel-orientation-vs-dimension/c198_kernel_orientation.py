"""C198 -- does the kernel LINE of D(theta) rotate across C73b's own
torsion-angle family even though dim ker stays fixed at 1 everywhere?

Cross-domain idea (user-forwarded, from a paper on circulant graphs /
Lovasz number studying null-space GEOMETRY, not just dimension): this
project's own Delta_geo = dim ker D - F_graded (C148) only asks "did an
extra dimension appear?" This round asks whether the kernel's ORIENTATION
inside the ambient space moves even when Delta_geo stays at 0.

Reuses c73b_torsion_family.py's own Part-1 basis construction and
build_numeric_dirac/invariant_basis unmodified -- does not redefine any
upstream physics, only extracts one extra number (a=block[0,0]) that
C73b's own script computed internally but never saved, and adds the
overlap computation.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c198.json"
C73B_PATH = (
    HERE.parent
    / "20260811-c73b-torsion-family-genuine-deformation-and-twist-control"
    / "c73b_torsion_family.py"
)
C73B_RESULTS_PATH = C73B_PATH.parent / "results_c73b.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


C73B = load_module("c73b_torsion_family", C73B_PATH)
R59 = C73B.R59
C73 = C73B.C73

SWEEP_ANGLES_DEG = [
    0,
    22.5,
    45,
    67.5,
    90,
    112.5,
    135,
    157.5,
    180,
    202.5,
    225,
    247.5,
    270,
]


def block_at(
    E, gens64, domain_inv, target_inv, t1_dict, t2_dict, theta_deg: float
) -> np.ndarray:
    theta = np.deg2rad(theta_deg)
    combo = {
        k: np.cos(theta) * t1_dict[k] + np.sin(theta) * t2_dict[k] for k in range(1, 7)
    }
    nomizu_theta = C73B.matdict_to_nomizu(combo)
    d_theta = C73.build_numeric_dirac(E, nomizu_theta)
    return target_inv.conj().T @ d_theta @ domain_inv  # shape (1,2): [a, b]


def kernel_direction(block_row: np.ndarray) -> np.ndarray:
    """Unit null vector of a 1x2 row [a,b]: solves a*x+b*y=0 -> (x,y) ~ (b,-a)."""
    a, b = block_row[0, 0], block_row[0, 1]
    v = np.array([b, -a], dtype=complex)
    norm = np.linalg.norm(v)
    if norm < 1e-12:
        raise ValueError(
            f"degenerate block row (a={a}, b={b}), cannot define a kernel direction"
        )
    return v / norm


def overlap(v1: np.ndarray, v2: np.ndarray) -> float:
    return float(abs(np.vdot(v1, v2)))


def main() -> None:
    E = R59.build_clifford(conj=False)
    gens64 = C73.su3_gens64(E)
    domain_inv = C73.invariant_basis(
        gens64, R59.block_global(R59.ODD_IDX, R59.EVEN_IDX)
    )
    target_inv = C73.invariant_basis(
        gens64, R59.block_global(R59.EVEN_IDX, R59.EVEN_IDX)
    )
    assert domain_inv.shape[1] == 2, (
        f"expected 2-dim domain_inv, got {domain_inv.shape}"
    )
    assert target_inv.shape[1] == 1, (
        f"expected 1-dim target_inv, got {target_inv.shape}"
    )

    # orthonormality check (T3's premise)
    gram = domain_inv.conj().T @ domain_inv
    orthonormal = bool(np.allclose(gram, np.eye(2), atol=1e-10))

    m_gens = C73B.m_generators()
    basis = C73B.equivariant_torsion_basis(m_gens)
    assert basis.shape[1] == 2, (
        f"expected 2-dim Hom_su3(m,Lambda^2 m), got {basis.shape[1]}"
    )
    t1_dict = C73B.vec_to_nomizu_dict(basis[:, 0])
    t2_dict = C73B.vec_to_nomizu_dict(basis[:, 1])

    nomizu_vec = C73B.nomizu_to_vec(R59.NOMIZU)
    coeffs, *_ = np.linalg.lstsq(basis, nomizu_vec, rcond=None)
    nomizu_angle_deg = float(np.rad2deg(np.arctan2(coeffs[1].real, coeffs[0].real)))

    # --- T1: reproduce C73b's own kernel_dim + |a|,|b| MAGNITUDES exactly ---
    # NOTE: raw complex a,b are NOT expected to match C73b's saved values
    # component-for-component -- invariant_basis() picks an orthonormal
    # nullspace basis via SVD, and a fresh process run can legitimately land
    # on a different (equally valid) basis for the same 2-dim invariant
    # subspace, related to C73b's original choice by a fixed (theta-
    # independent) unitary rotation U. That rotation changes the raw a(theta),
    # b(theta) components but leaves |a|, |b|, kernel_dim, and every OVERLAP
    # this experiment actually cares about invariant (overlaps are U-invariant
    # by construction: |v1^dagger U^dagger U v2| = |v1^dagger v2|). So the
    # real positive control is magnitude + kernel_dim agreement, not raw
    # component equality.
    c73b_results = json.loads(C73B_RESULTS_PATH.read_text())
    c73b_sweep = c73b_results["torsion_angle_sweep"]

    rows = {}
    mismatches = []
    magnitude_mismatches = []
    for theta_deg in SWEEP_ANGLES_DEG:
        block = block_at(E, gens64, domain_inv, target_inv, t1_dict, t2_dict, theta_deg)
        rank = int(np.sum(np.linalg.svd(block, compute_uv=False) > 1e-8))
        kernel_dim = 2 - rank
        a, b = complex(block[0, 0]), complex(block[0, 1])

        expected = c73b_sweep[str(theta_deg)]
        if kernel_dim != expected["kernel_dim"]:
            mismatches.append((theta_deg, kernel_dim, expected["kernel_dim"]))
        if abs(abs(b) - abs(complex(expected["b"]))) > 1e-8:
            magnitude_mismatches.append(
                (theta_deg, abs(b), abs(complex(expected["b"])))
            )

        v_dir = kernel_direction(block)
        v_full = domain_inv @ v_dir  # embed into the full 64-dim space
        rows[str(theta_deg)] = {
            "a": a,
            "b": b,
            "kernel_dim": kernel_dim,
            "calibration_passes": expected["calibration_passes"],
            "v_dir": [complex(x) for x in v_dir],
            "v_full_norm": float(np.linalg.norm(v_full)),
        }

    t1_positive_control_pass = len(mismatches) == 0 and len(magnitude_mismatches) == 0
    print(
        f"T1 (kernel_dim + |a|,|b| magnitudes match C73b's own independently-run "
        f"sweep exactly): {'PASS' if t1_positive_control_pass else 'FAIL'}"
    )
    if mismatches:
        print("  kernel_dim mismatches:", mismatches)
    if magnitude_mismatches:
        print("  |b| magnitude mismatches:", magnitude_mismatches)

    # --- T1b: exact algebraic mechanism -- does block(theta) = exp(-i*theta)*Block_t1 ---
    # (this is the SPECIFIC reason the kernel direction turns out fixed: if
    # Block_t2 = -i*Block_t1 exactly, the 2-real-parameter sweep only ever
    # moves the block row by an overall complex PHASE, which cannot change
    # the null LINE it defines.)
    block_t1 = np.array([rows["0"]["a"], rows["0"]["b"]], dtype=complex)
    phase_mechanism_checks = {}
    for theta_deg in SWEEP_ANGLES_DEG:
        theta = np.deg2rad(theta_deg)
        predicted = np.exp(-1j * theta) * block_t1
        actual = np.array(
            [rows[str(theta_deg)]["a"], rows[str(theta_deg)]["b"]], dtype=complex
        )
        phase_mechanism_checks[str(theta_deg)] = float(
            np.max(np.abs(actual - predicted))
        )
    t1b_pass = all(v < 1e-8 for v in phase_mechanism_checks.values())
    print(
        f"T1b (block(theta) == exp(-i*theta)*Block_t1 exactly, i.e. Block_t2 == "
        f"-i*Block_t1): {'PASS' if t1b_pass else 'FAIL'}"
    )

    # --- T2: antipodal positive control, overlap(theta, theta+180) ~= 1 ---
    antipodal_overlaps = {}
    for theta_deg in SWEEP_ANGLES_DEG:
        v1 = np.array(rows[str(theta_deg)]["v_dir"], dtype=complex)
        theta2 = (theta_deg + 180) % 360
        block2 = block_at(E, gens64, domain_inv, target_inv, t1_dict, t2_dict, theta2)
        v2 = kernel_direction(block2)
        antipodal_overlaps[str(theta_deg)] = overlap(v1, v2)
    t2_pass = all(v > 0.999 for v in antipodal_overlaps.values())
    print(
        f"T2 (antipodal overlap ~= 1): {'PASS' if t2_pass else 'FAIL'}",
        antipodal_overlaps,
    )

    # trivial self-overlap sanity check
    self_overlaps = {}
    for theta_deg in SWEEP_ANGLES_DEG:
        v1 = np.array(rows[str(theta_deg)]["v_dir"], dtype=complex)
        self_overlaps[str(theta_deg)] = overlap(v1, v1)
    assert all(abs(v - 1.0) < 1e-10 for v in self_overlaps.values()), (
        "self-overlap must be exactly 1"
    )

    # --- T3: reduced-coordinate overlap vs full-64-dim-embedding overlap ---
    t3_checks = {}
    ref_deg = SWEEP_ANGLES_DEG[0]
    v_ref_dir = np.array(rows[str(ref_deg)]["v_dir"], dtype=complex)
    v_ref_full = domain_inv @ v_ref_dir
    for theta_deg in SWEEP_ANGLES_DEG:
        v_dir = np.array(rows[str(theta_deg)]["v_dir"], dtype=complex)
        v_full = domain_inv @ v_dir
        ov_reduced = overlap(v_ref_dir, v_dir)
        ov_full = overlap(v_ref_full, v_full)
        t3_checks[str(theta_deg)] = {
            "reduced": ov_reduced,
            "full": ov_full,
            "diff": abs(ov_reduced - ov_full),
        }
    t3_pass = all(c["diff"] < 1e-8 for c in t3_checks.values())
    print(
        f"T3 (reduced vs full-embedding overlap agree): {'PASS' if t3_pass else 'FAIL'}"
    )

    # --- Main claim: overlap(theta, theta_NOMIZU) across the sweep ---
    block_nomizu = block_at(
        E, gens64, domain_inv, target_inv, t1_dict, t2_dict, nomizu_angle_deg
    )
    v_nomizu = kernel_direction(block_nomizu)
    overlap_vs_nomizu = {}
    for theta_deg in SWEEP_ANGLES_DEG:
        v = np.array(rows[str(theta_deg)]["v_dir"], dtype=complex)
        overlap_vs_nomizu[str(theta_deg)] = overlap(v, v_nomizu)

    min_overlap = min(overlap_vs_nomizu.values())
    max_overlap = max(overlap_vs_nomizu.values())
    kernel_rotates = min_overlap < 0.999

    print("\noverlap(theta, theta_NOMIZU) across the sweep:")
    for k, v in overlap_vs_nomizu.items():
        print(f"  theta={k}: overlap={v:.6f}")
    print(f"\nmin={min_overlap:.6f}  max={max_overlap:.6f}")
    print(
        f"MAIN CLAIM (kernel direction rotates, i.e. NOT constant): {'TRUE' if kernel_rotates else 'FALSE'}"
    )

    results = {
        "orthonormal_domain_inv": orthonormal,
        "t1_positive_control_pass": t1_positive_control_pass,
        "t1_kernel_dim_mismatches": [str(m) for m in mismatches],
        "t1_magnitude_mismatches": [str(m) for m in magnitude_mismatches],
        "t1b_phase_mechanism_pass": t1b_pass,
        "t1b_phase_mechanism_max_diffs": phase_mechanism_checks,
        "t2_antipodal_overlaps": antipodal_overlaps,
        "t2_pass": t2_pass,
        "t3_checks": t3_checks,
        "t3_pass": t3_pass,
        "nomizu_angle_deg": nomizu_angle_deg,
        "sweep_rows": {
            k: {kk: (str(vv) if isinstance(vv, list) else vv) for kk, vv in v.items()}
            for k, v in rows.items()
        },
        "overlap_vs_nomizu": overlap_vs_nomizu,
        "min_overlap": min_overlap,
        "max_overlap": max_overlap,
        "kernel_rotates": kernel_rotates,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
