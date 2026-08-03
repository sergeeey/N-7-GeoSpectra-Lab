"""OB11, condition (i): is the internal SU(3)_c x SU(2)_L x SU(2)_R block
structure of H_matter IDENTICAL across the three triality channels 8_v/8_s/8_c?

Scope correction (grounded via Explore agent, 2026-08-03): SU(2)_L x SU(2)_R
lives entirely on the S3 factor (round90, preprint.tex:292-310) and never
acts on the S6-side octonion fiber where 8_v/8_s/8_c live at all (round119
corrected an earlier false SU(3)xSU(2)xSU(2)-in-SO(6) embedding claim). So:
  - the S3-side factor of H_matter (4-dim SU(2)_L x SU(2)_R spinor) is the
    SAME for every channel by construction -- condition (i) is VACUOUSLY
    satisfied for SU(2)_L x SU(2)_R (there is nothing per-channel to compare).
  - the ONLY non-trivial part of condition (i) is whether the S6-side factor
    (8_v vs 8_s vs 8_c, carrying su(3)_c) has IDENTICAL representation
    content across the three channels.

G102 already computed Hom_su3(a,b)=6 for all pairs a,b in {v,s,c} (Schur-type
dimension count) and round127 already argued Hom(V,V)=4+a^2+b^2=6 => a=b=1,
i.e. each channel decomposes as 1+1+3+3bar under su(3) -- but this conclusion
was never explicitly verified per-channel via direct diagonalization. This
script does that explicit check, reusing G102's own already-verified su(3)
generators and restrict_to_subalgebra machinery (not re-derived).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_ob11.json"

G102_PATH = HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py"
_spec = importlib.util.spec_from_file_location("g102_spin8_fiber", G102_PATH)
assert _spec and _spec.loader
G102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(G102)

TOL = 1e-8


def casimir(rep: list[np.ndarray]) -> np.ndarray:
    """Quadratic Casimir sum_a T_a^2 for a representation given as a list of
    generator matrices (each anti-Hermitian, as produced by G102's own
    restrict_to_subalgebra -- real antisymmetric matrices acting on R^n)."""
    n = rep[0].shape[0]
    c2 = np.zeros((n, n))
    for t in rep:
        c2 += t @ t
    return c2


def eigenvalue_multiplicities(mat: np.ndarray, tol: float = 1e-6) -> list[tuple[float, int]]:
    """Group eigenvalues of a symmetric-in-practice matrix into (value, multiplicity)
    clusters within `tol`, sorted by value."""
    evals = np.linalg.eigvalsh(0.5 * (mat + mat.T))
    evals_sorted = np.sort(evals)
    groups: list[tuple[float, int]] = []
    for val in evals_sorted:
        if groups and abs(val - groups[-1][0]) < tol:
            v, c = groups[-1]
            groups[-1] = ((v * c + val) / (c + 1), c + 1)
        else:
            groups.append((float(val), 1))
    return groups


def main() -> None:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    assert len(su3) == 8, f"expected su(3), dim 8, got {len(su3)}"

    reps_su3 = G102.restrict_to_subalgebra(su3)  # (v_out, s_out, c_out), each 8 matrices
    labels = ("v", "s", "c")

    print("=== OB11 (i): SU(3)_c internal block structure across the 3 triality channels ===")
    print(f"su(3) generator count: {len(su3)} (predict 8, reconfirms G102 S2)\n")

    spectra = {}
    for label, rep in zip(labels, reps_su3):
        c2 = casimir(rep)
        asym_residual = float(np.max(np.abs(c2 - c2.T)))
        groups = eigenvalue_multiplicities(c2)
        spectra[label] = groups
        print(f"channel 8_{label}: Casimir symmetry residual = {asym_residual:.2e}")
        print(f"  Casimir eigenvalue groups (value, multiplicity): {groups}")

    # --- verify each channel matches the predicted 1+1+3+3bar pattern ---
    # predicted shape: exactly 2 zero-eigenvalue singlets + 6 eigenvectors at ONE
    # shared nonzero value (3 and 3bar share the same quadratic Casimir eigenvalue).
    pattern_ok = {}
    for label, groups in spectra.items():
        zero_mult = sum(m for v, m in groups if abs(v) < 1e-6)
        nonzero_groups = [(v, m) for v, m in groups if abs(v) >= 1e-6]
        nonzero_mult = sum(m for v, m in nonzero_groups)
        single_nonzero_value = len(nonzero_groups) == 1
        pattern_ok[label] = zero_mult == 2 and nonzero_mult == 6 and single_nonzero_value
        print(
            f"channel 8_{label}: zero_mult={zero_mult} (predict 2), "
            f"nonzero_mult={nonzero_mult} (predict 6), "
            f"single_nonzero_Casimir_value={single_nonzero_value} "
            f"-> matches_1_1_3_3bar={pattern_ok[label]}"
        )

    # --- verify the three channels' spectra are IDENTICAL to each other ---
    v_val = next(v for v, m in spectra["v"] if abs(v) >= 1e-6)
    s_val = next(v for v, m in spectra["s"] if abs(v) >= 1e-6)
    c_val = next(v for v, m in spectra["c"] if abs(v) >= 1e-6)
    cross_channel_identical = abs(v_val - s_val) < 1e-6 and abs(v_val - c_val) < 1e-6
    print(
        f"\nnonzero Casimir eigenvalue: v={v_val:.6f}, s={s_val:.6f}, c={c_val:.6f} "
        f"-> IDENTICAL across all 3 channels: {cross_channel_identical}"
    )

    all_match = all(pattern_ok.values()) and cross_channel_identical
    print(f"\nVERDICT: condition (i) [SU(3)_c part] = {'VERIFIED' if all_match else 'FAILED'}")
    print(
        "SU(2)_L x SU(2)_R part of condition (i): VACUOUSLY satisfied -- this gauge "
        "factor lives entirely on S3 (preprint.tex:292-310) and never acts on the "
        "S6-side channels at all (round119), so there is no per-channel difference "
        "possible to check for that factor; the S3-side 4-dim spinor is identical "
        "for every channel by construction."
    )

    results = {
        "ob": "OB11_condition_i",
        "su3_generator_count": len(su3),
        "spectra_by_channel": {k: v for k, v in spectra.items()},
        "pattern_ok_by_channel": pattern_ok,
        "cross_channel_casimir_identical": cross_channel_identical,
        "verdict": "VERIFIED" if all_match else "FAILED",
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
