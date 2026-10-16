r"""C210: cross-check G96's own G2 realization against the standard G2 root
system (6 short + 6 long roots, adjacent angle 30 deg, length ratio sqrt(3)).

Motivated by a MathOverflow question found via the Stack Exchange API
("Reference Request: Structure constants for G2", Q322858): its answers
point to Chevalley-basis structure constants C_{alpha,beta,i,j} indexed by
an ORDERED root system (Carter's book table after Sec 12.4; Vavilov-
Plotkin Table IV; Humphreys GTM 9 Sec 19.3). G96 never computed anything
root-indexed at all -- it only verified Lie-bracket CLOSURE (via
least-squares reconstruction residuals) among 14 arbitrary SVD-derived
basis matrices (derivations of the octonion algebra), with no Cartan
subalgebra or root system ever extracted. These are genuinely different
objects in different bases; a naive number-for-number comparison would be
meaningless.

This round extracts a basis-INDEPENDENT invariant from G96's own
generators -- the actual root system, via the ambient trace form (which
does not depend on the arbitrary SVD basis or on which generic element is
picked as the first Cartan direction) -- and checks it against the known
G2 root system. This is the closest honest thing to "compare against the
MathOverflow reference" without owning a copy of Carter's or Vavilov-
Plotkin's book to transcribe their specific table.

Method:
  1. Rebuild G96's own 14 generators verbatim (same Fano-plane derivation
     condition, same SVD null-space construction).
  2. Pick a random real Cartan element H1 = sum(c_i * gens[i]); build its
     14x14 adjoint matrix (in the gens basis) and diagonalize.
  3. The 2-dim kernel of ad(H1) is the Cartan subalgebra {H1, H2} (H1
     itself, and H2 read off as the other kernel direction).
  4. For each of the 6 nonzero conjugate eigenvalue pairs of ad(H1),
     reconstruct the complex root-vector matrix E_k, then read off its
     second root-coordinate phi_k from [H2, E_k] = i*phi_k*E_k.
  5. Convert (theta_k, phi_k) into an actual Cartan ELEMENT H_{alpha_k}
     via the ambient trace form B(X,Y) = -Tr(XY) (positive-definite on
     this compact real form), so lengths/angles are basis-independent.
  6. Check the resulting 12 root vectors (+-H_{alpha_k}, k=1..6) split
     into two length classes in ratio sqrt(3), with 30-degree spacing.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c210.json"

# --- Verbatim from G96 (experiments/20260626-g96-s6-g2-su3/g96_g2_su3.py) ---
FANO = [
    (0, 1, 3),
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 0),
    (5, 6, 1),
    (6, 0, 2),
]


def build_phi() -> np.ndarray:
    phi = np.zeros((7, 7, 7), dtype=float)
    for a, b, c in FANO:
        for i, j, k in [(a, b, c), (b, c, a), (c, a, b)]:
            phi[i, j, k] = 1.0
            phi[j, i, k] = -1.0
    return phi


def g2_condition_matrix(phi: np.ndarray) -> np.ndarray:
    rows = []
    for i in range(7):
        for j in range(7):
            row = np.zeros(49)
            row[i * 7 + j] = 1.0
            row[j * 7 + i] = 1.0
            rows.append(row)
    for i in range(7):
        for j in range(7):
            for ll in range(7):
                row = np.zeros(49)
                for k in range(7):
                    row[ll * 7 + k] += phi[i, j, k]
                for m in range(7):
                    row[m * 7 + i] -= phi[m, j, ll]
                for m in range(7):
                    row[m * 7 + j] -= phi[i, m, ll]
                rows.append(row)
    return np.array(rows)


def find_g2_generators(phi: np.ndarray) -> list[np.ndarray]:
    M = g2_condition_matrix(phi)
    _, _, Vt = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(np.linalg.svd(M, compute_uv=False) > 1e-8))
    null_basis = Vt[rank:].T
    return [col.reshape(7, 7) for col in null_basis.T]


def commutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


# --- New for C210: Cartan + root system extraction ---


def adjoint_matrix(gens: list[np.ndarray], basis_flat: np.ndarray, X: np.ndarray) -> np.ndarray:
    r"""14x14 real matrix of ad(X) restricted to span(gens), in the gens basis."""
    cols = []
    for G in gens:
        C = commutator(X, G)
        coeffs, _, _, _ = np.linalg.lstsq(basis_flat, C.flatten(), rcond=None)
        cols.append(coeffs)
    return np.column_stack(cols)


def trace_form(X: np.ndarray, Y: np.ndarray) -> float:
    r"""B(X,Y) = -Tr(XY); positive-definite on this compact real form
    (X,Y real antisymmetric => Tr(XY) <= 0, with equality only if XY=0)."""
    return float(-np.trace(X @ Y).real)


def main() -> None:
    rng = np.random.default_rng(20260927)
    checks: dict = {}

    phi = build_phi()
    gens = find_g2_generators(phi)
    checks["dim_g2"] = len(gens)
    assert len(gens) == 14, f"Expected 14, got {len(gens)}"
    basis_flat = np.column_stack([g.flatten() for g in gens])

    # Step 1: generic H1, build ad(H1) as a 14x14 real matrix.
    c1 = rng.normal(size=14)
    H1 = sum(c1[i] * gens[i] for i in range(14))
    Ad_H1 = adjoint_matrix(gens, basis_flat, H1)

    eigvals1, eigvecs1 = np.linalg.eig(Ad_H1)
    zero_mask = np.abs(eigvals1) < 1e-6
    n_zero = int(np.sum(zero_mask))
    checks["ad_H1_zero_eigenvalue_multiplicity"] = n_zero
    checks["ad_H1_zero_eigenvalue_multiplicity_is_2"] = n_zero == 2

    # should be 6 conjugate pairs -> 12 values -> 6 distinct |theta|, each x2
    checks["ad_H1_nonzero_eigenvalue_count"] = int(np.sum(~zero_mask))
    checks["ad_H1_nonzero_eigenvalue_count_is_12"] = int(np.sum(~zero_mask)) == 12
    checks["ad_H1_real_parts_of_nonzero_eigenvalues_near_zero"] = float(
        np.max(np.abs(eigvals1[~zero_mask].real))
    )

    # Step 2: the 2-dim kernel of ad(H1) IS the Cartan {H1, H2}.
    kernel_coeffs = eigvecs1[:, zero_mask].real  # 14 x 2 (real, since H1 itself is one)
    kernel_matrices = [sum(kernel_coeffs[i, k] * gens[i] for i in range(14)) for k in range(2)]
    # Re-orthogonalize against H1 to get a clean second direction H2.
    H1_norm2 = trace_form(H1, H1)
    proj_coeffs = [trace_form(km, H1) / H1_norm2 for km in kernel_matrices]
    H2_candidates = [kernel_matrices[k] - proj_coeffs[k] * H1 for k in range(2)]
    H2 = max(H2_candidates, key=lambda M: trace_form(M, M))
    checks["H2_norm2"] = trace_form(H2, H2)
    checks["H2_is_nondegenerate"] = trace_form(H2, H2) > 1e-8

    comm_H1_H2 = commutator(H1, H2)
    checks["commutator_H1_H2_max_abs"] = float(np.max(np.abs(comm_H1_H2)))
    checks["H1_H2_commute"] = float(np.max(np.abs(comm_H1_H2))) < 1e-8

    # Step 3: for each nonzero eigenvalue with positive imaginary part,
    # reconstruct the complex root vector E_k and read off phi_k from
    # [H2, E_k] = i*phi_k*E_k.
    Ad_H2 = adjoint_matrix(gens, basis_flat, H2)
    pos_imag_idx = [i for i in range(14) if (~zero_mask)[i] and eigvals1[i].imag > 0]
    root_records = []
    for idx in pos_imag_idx:
        theta_k = float(eigvals1[idx].imag)
        v = eigvecs1[:, idx]  # complex 14-vector, coefficients in gens basis
        # (the actual complex root matrix E_k = sum(v[i]*gens[i]) is never
        # needed explicitly -- everything below works directly with its
        # coefficient vector v in the gens basis.)
        comm_H2_Ek = Ad_H2 @ v  # 14-vector, coefficients of [H2, E_k] in gens basis
        # phi_k solves comm_H2_Ek = i*phi_k*v  (least-squares over the scalar i*phi_k)
        num = np.vdot(v, comm_H2_Ek)
        den = np.vdot(v, v)
        i_phi_k = num / den
        phi_k = float(i_phi_k.imag)
        residual = np.max(np.abs(comm_H2_Ek - 1j * phi_k * v))
        # Convert (theta_k, phi_k) into an actual Cartan element H_alpha
        # via the trace-form Gram matrix on {H1, H2}.
        gram = np.array(
            [[trace_form(H1, H1), trace_form(H1, H2)], [trace_form(H2, H1), trace_form(H2, H2)]]
        )
        target = np.array([theta_k, phi_k])
        ab = np.linalg.solve(gram, target)
        H_alpha = ab[0] * H1 + ab[1] * H2
        root_records.append(
            {
                "theta": theta_k,
                "phi": phi_k,
                "root_vector_residual": float(residual),
                "H_alpha": H_alpha,
                "norm2": trace_form(H_alpha, H_alpha),
            }
        )

    checks["n_root_pairs_found"] = len(root_records)
    checks["n_root_pairs_found_is_6"] = len(root_records) == 6
    checks["max_root_vector_residual"] = max(r["root_vector_residual"] for r in root_records)

    # Step 4: full 12-vector root system (+- H_alpha for each of the 6).
    all_roots = []
    for r in root_records:
        all_roots.append(r["H_alpha"])
        all_roots.append(-r["H_alpha"])
    norms2 = sorted(trace_form(a, a) for a in all_roots)
    checks["all_12_norms_squared"] = [round(n, 6) for n in norms2]

    # Cluster into 2 length classes.
    norms2_arr = np.array(norms2)
    short_norm2 = np.median(norms2_arr[:6])
    long_norm2 = np.median(norms2_arr[6:])
    ratio = long_norm2 / short_norm2 if short_norm2 > 0 else float("nan")
    checks["short_norm2_median"] = float(short_norm2)
    checks["long_norm2_median"] = float(long_norm2)
    checks["long_over_short_norm2_ratio"] = float(ratio)
    checks["ratio_matches_3_within_1pct"] = abs(ratio - 3.0) < 0.03

    # Angles: {H1,H2} is NOT generally orthonormal under the trace form
    # (theta,phi)-coordinates alone give the WRONG angle. Build a genuine
    # orthonormal basis {e1,e2} via Gram-Schmidt under trace_form, then
    # project each H_alpha onto it -- these (x,y) coordinates ARE metrically
    # correct (same inner product used for the norm2 check above).
    e1 = H1 / np.sqrt(trace_form(H1, H1))
    e2_raw = H2 - trace_form(H2, e1) * e1
    e2 = e2_raw / np.sqrt(trace_form(e2_raw, e2_raw))
    checks["e1_e2_orthonormal_check"] = {
        "trace_form(e1,e1)": trace_form(e1, e1),
        "trace_form(e2,e2)": trace_form(e2, e2),
        "trace_form(e1,e2)": trace_form(e1, e2),
    }

    coords = []
    for a in all_roots:
        x = trace_form(a, e1)
        y = trace_form(a, e2)
        coords.append((x, y))
    angles_sorted = sorted(np.arctan2(y, x) for x, y in coords)
    angles_deg = np.degrees(angles_sorted)
    gaps = np.diff(list(angles_deg) + [angles_deg[0] + 360.0])
    checks["angle_gaps_degrees"] = [round(g, 3) for g in gaps]
    checks["all_gaps_near_30deg"] = bool(np.max(np.abs(gaps - 30.0)) < 1.0)

    all_pass = (
        checks["ad_H1_zero_eigenvalue_multiplicity_is_2"]
        and checks["ad_H1_nonzero_eigenvalue_count_is_12"]
        and checks["H1_H2_commute"]
        and checks["n_root_pairs_found_is_6"]
        and checks["ratio_matches_3_within_1pct"]
        and checks["all_gaps_near_30deg"]
    )
    checks["all_pass"] = all_pass

    checks_serializable = {
        k: (v if not isinstance(v, np.ndarray) else v.tolist()) for k, v in checks.items()
    }

    print("=" * 70)
    print("C210: G96 root-system cross-check against standard G2 (6+6, sqrt3, 30deg)")
    print("=" * 70)
    for k, v in checks_serializable.items():
        print(f"  {k}: {v}")

    RESULTS_PATH.write_text(json.dumps(checks_serializable, indent=2, default=str))
    print(f"\n[{'PASS' if all_pass else 'FAIL'}] -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
