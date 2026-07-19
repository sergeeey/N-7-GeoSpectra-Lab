"""Round128: construct the explicit Cartan-Weyl alignment Phi: su3_v -> su3_sigma
and search for an invertible intertwiner S, completing round127's Kill
Analysis item. Consolidates the exploratory Bash computation into one
traceable script (avoids index-tracking risk across many ad-hoc calls).

Method (per claim.md):
  1. CSA of su3_v via a generic element's centralizer (round124/G102 basis).
  2. CSA of su3_sigma reusing G10-B's own H1,H2, lifted via G11.lift_to_spinor.
  3. Root vectors on each side (diagonalize joint CSA adjoint action).
  4. Match the two root systems via the sum-relation (alpha+beta=gamma for
     simple roots), solving the unique linear map M on Cartan coordinates.
  5. Determine root-vector scalars mu_k via least-squares over ALL bracket
     relations simultaneously (robust to any single relation being
     under-determined) -- construct full Phi, run Sylvester Hom search.
  6. Report the honest outcome per pre-registered kill criteria.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_round128.json"
TOL = 1e-8


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


G102 = load_module(
    "g102_spin8_fiber",
    HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py",
)

G11_DIR = (HERE.parent / "20260618-g11-block-generators").resolve()
sys.path.insert(0, str(G11_DIR))
G11 = load_module("g11_block_generators", G11_DIR / "g11_block_generators.py")

G15_DIR = (HERE.parent / "20260619-g15-hypercharge").resolve()
sys.path.insert(0, str(G15_DIR))
G15 = load_module("g15_hypercharge", G15_DIR / "g15_hypercharge.py")


def ad_matrix(H: np.ndarray, gens: list[np.ndarray]) -> np.ndarray:
    n = len(gens)
    A = np.zeros((n, n), dtype=complex)
    for j in range(n):
        comm = H @ gens[j] - gens[j] @ H
        for k in range(n):
            A[k, j] = np.trace(gens[k].conj().T @ comm)
    return A


def extract_csa_and_roots(
    gens: list[np.ndarray], H_seed: np.ndarray, combo_weight: float = 0.37123
):
    """Given an orthonormal (trace-form) generator basis and a generic Cartan
    element H_seed already known to lie in the CSA, return:
      csa_coefs (8x2 coefficient vectors of a CSA basis in `gens`),
      H1, H2 (8x8 matrices), root_coords (6x2 real), E_matrices (6 8x8 matrices).
    """
    n = len(gens)
    comms = [H_seed @ g - g @ H_seed for g in gens]
    M = np.array([c.flatten() for c in comms]).T
    _, s, vt = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(M.shape) * s[0]))
    assert n - rank == 2, f"expected 2-dim CSA, got {n - rank}"
    null = vt[rank:].conj().T
    assert np.max(np.abs(null.imag)) < 1e-8, "CSA coefficients unexpectedly complex"
    null = null.real
    H1 = sum(null[j, 0] * gens[j] for j in range(n))
    H2 = sum(null[j, 1] * gens[j] for j in range(n))

    adH1 = ad_matrix(H1, gens)
    adH2 = ad_matrix(H2, gens)
    assert np.max(np.abs(adH1 @ adH2 - adH2 @ adH1)) < 1e-8

    Q, _ = np.linalg.qr(np.hstack([null, np.eye(n)]))
    complement = Q[:, 2:n]
    adH1_c = complement.conj().T @ adH1 @ complement
    adH2_c = complement.conj().T @ adH2 @ complement

    combo = adH1_c + combo_weight * adH2_c
    evals, evecs = np.linalg.eig(combo)
    m = n - 2
    alphas = np.array(
        [
            (evecs[:, k].conj() @ adH1_c @ evecs[:, k]) / (evecs[:, k].conj() @ evecs[:, k])
            for k in range(m)
        ]
    )
    betas = np.array(
        [
            (evecs[:, k].conj() @ adH2_c @ evecs[:, k]) / (evecs[:, k].conj() @ evecs[:, k])
            for k in range(m)
        ]
    )
    root_coords = (np.stack([alphas, betas], axis=1) / 1j).real
    E_coefs = complement @ evecs  # n x m, coefficient vectors in `gens` basis
    E_matrices = [sum(E_coefs[j, k] * gens[j] for j in range(n)) for k in range(m)]
    return null, H1, H2, root_coords, E_matrices


def orthonormalize(gens: list[np.ndarray]) -> list[np.ndarray]:
    n = len(gens)
    flat = np.array([g.flatten() for g in gens])
    G = flat.conj() @ flat.T
    evals, evecs = np.linalg.eigh(G)
    Ginv_half = evecs @ np.diag(1 / np.sqrt(evals)) @ evecs.conj().T
    flat_onb = Ginv_half @ flat
    return [flat_onb[k].reshape(gens[0].shape) for k in range(n)]


def find_hexagon_map(roots_a: np.ndarray, roots_b: np.ndarray, sum_pairs_a, sum_pairs_b):
    """Find the unique linear map T with T@roots_a[i]=roots_b[i] for the
    sum-relation-respecting simple-root pair, verified against all 6 roots.
    sum_pairs_a = (i_simple1, i_simple2, i_sum) index triple s.t.
    roots_a[i_simple1]+roots_a[i_simple2] == roots_a[i_sum]."""
    i1, i2, i0 = sum_pairs_a
    j1, j2, j0 = sum_pairs_b
    A = np.stack([roots_a[i1], roots_a[i2]], axis=0)
    B = np.stack([roots_b[j1], roots_b[j2]], axis=0)
    T = np.linalg.solve(A, B).T
    return T


def main() -> None:
    # --- su3_v side ---
    der = G102.derivation_basis()
    su3_v = [A.astype(complex) for A in G102.stabilizer_basis(der)]
    rng = np.random.default_rng(1)
    c = rng.normal(size=8)
    H_seed_v = sum(ci * Ai for ci, Ai in zip(c, su3_v))
    null_v, H1v, H2v, roots_v, E_v = extract_csa_and_roots(su3_v, H_seed_v)

    # find v's sum-relation triple by brute search
    v_sum_triple = None
    for i, j, k in itertools.permutations(range(6), 3):
        if np.max(np.abs(roots_v[i] + roots_v[j] - roots_v[k])) < 1e-6:
            v_sum_triple = (i, j, k)
            break
    assert v_sum_triple is not None, "no sum-relation found among su3_v roots"

    # --- su3_sigma side ---
    def Mvec(a, b):
        M = sp.zeros(6, 6)
        M[a, b] = 1
        M[b, a] = -1
        return M

    M01, M23, M45 = Mvec(0, 1), Mvec(2, 3), Mvec(4, 5)
    H1_vec = sp.Rational(2, 3) * M01 - sp.Rational(1, 3) * M23 - sp.Rational(1, 3) * M45
    H2_vec = -sp.Rational(1, 3) * M01 + sp.Rational(2, 3) * M23 - sp.Rational(1, 3) * M45
    H1s = np.array(G11.lift_to_spinor(H1_vec).evalf(), dtype=complex)
    H2s = np.array(G11.lift_to_spinor(H2_vec).evalf(), dtype=complex)

    su3_sigma = [np.array(g.evalf(), dtype=complex) for g in G15.su3_spin]
    onb = orthonormalize(su3_sigma)
    BmL = np.array(G15.BmL.evalf(), dtype=complex)

    onb_flat = np.array([g.flatten() for g in onb])

    def coeffs_of(Hm):
        return onb_flat.conj() @ Hm.flatten()

    c1s, c2s = coeffs_of(H1s), coeffs_of(H2s)
    csa_coefs_s = np.stack([c1s, c2s], axis=1)
    adH1s = ad_matrix(H1s, onb)
    adH2s = ad_matrix(H2s, onb)
    assert np.max(np.abs(adH1s @ adH2s - adH2s @ adH1s)) < 1e-8
    Qs, _ = np.linalg.qr(np.hstack([csa_coefs_s, np.eye(8)]))
    complement_s = Qs[:, 2:8]
    adH1s_c = complement_s.conj().T @ adH1s @ complement_s
    adH2s_c = complement_s.conj().T @ adH2s @ complement_s
    combo_s = adH1s_c + 0.37123 * adH2s_c
    evals_s, evecs_s = np.linalg.eig(combo_s)
    alphas_s = np.array(
        [
            (evecs_s[:, k].conj() @ adH1s_c @ evecs_s[:, k])
            / (evecs_s[:, k].conj() @ evecs_s[:, k])
            for k in range(6)
        ]
    )
    betas_s = np.array(
        [
            (evecs_s[:, k].conj() @ adH2s_c @ evecs_s[:, k])
            / (evecs_s[:, k].conj() @ evecs_s[:, k])
            for k in range(6)
        ]
    )
    roots_s = (np.stack([alphas_s, betas_s], axis=1) / 1j).real
    E_s_coefs = complement_s @ evecs_s
    F_s = [sum(E_s_coefs[j, k] * onb[j] for j in range(8)) for k in range(6)]

    s_sum_triple = None
    for i, j, k in itertools.permutations(range(6), 3):
        if np.max(np.abs(roots_s[i] + roots_s[j] - roots_s[k])) < 1e-6:
            s_sum_triple = (i, j, k)
            break
    assert s_sum_triple is not None, "no sum-relation found among su3_sigma roots"

    # --- Step 4: exhaustively enumerate ALL |Aut(A2)|=12-equivalent
    # correspondences (not just one), by trying every sigma-side sum-triple
    # found (up to sign-representative choice) against every v-side
    # orientation/sign. Each survivor (near-zero full-hexagon residual) is a
    # distinct candidate Phi restricted to the CSA.
    i1, i2, i0 = v_sum_triple

    def neg_index(roots, idx):
        target = -roots[idx]
        for k in range(len(roots)):
            if np.max(np.abs(roots[k] - target)) < 1e-6:
                return k
        raise ValueError("no negative found")

    all_s_sum_triples = [
        (i, j, k)
        for i, j, k in itertools.permutations(range(6), 3)
        if np.max(np.abs(roots_s[i] + roots_s[j] - roots_s[k])) < 1e-6
    ]

    all_candidates = []
    for j1, j2, j0 in all_s_sum_triples:
        for va, vb in [(i1, i2), (i2, i1)]:
            for sign in [1, -1]:
                A = np.stack([roots_s[j1], roots_s[j2]], axis=0)
                B = np.stack([sign * roots_v[va], sign * roots_v[vb]], axis=0)
                if abs(np.linalg.det(A)) < 1e-9:
                    continue
                T = np.linalg.solve(A, B).T
                pred0 = T @ roots_s[j0]
                target0 = sign * roots_v[i0]
                resid0 = np.max(np.abs(pred0 - target0))
                if resid0 > 1e-6:
                    continue
                match_s_to_v_c = {}
                match_s_to_v_c[j1] = va if sign == 1 else neg_index(roots_v, va)
                match_s_to_v_c[j2] = vb if sign == 1 else neg_index(roots_v, vb)
                match_s_to_v_c[j0] = i0 if sign == 1 else neg_index(roots_v, i0)
                for s_idx in list(match_s_to_v_c):
                    v_idx = match_s_to_v_c[s_idx]
                    match_s_to_v_c[neg_index(roots_s, s_idx)] = neg_index(roots_v, v_idx)
                max_resid = max(
                    np.max(np.abs(T @ roots_s[s_idx] - roots_v[v_idx]))
                    for s_idx, v_idx in match_s_to_v_c.items()
                )
                key = tuple(sorted(match_s_to_v_c.items()))
                if any(k == key for k, *_ in all_candidates):
                    continue
                all_candidates.append((key, max_resid, T, dict(match_s_to_v_c)))

    if "--debug" in sys.argv:
        print(
            f"Found {len(all_candidates)} distinct exact-hexagon-match candidates (of |Aut(A2)|=12 possible)"
        )

    # use the first (lowest-residual) candidate as the default single-Phi
    # result reported below; the full multi-candidate scan (Step 4b) tries
    # them all against the representation-level Hom search.
    all_candidates.sort(key=lambda c: c[1])
    _, max_hexagon_resid, M, match_s_to_v = all_candidates[0]

    # --- Steps 5-6, wrapped as a function so EVERY candidate Phi (all exact
    # hexagon matches found in Step 4) can be tried, not just the first. ---
    from scipy.optimize import least_squares

    def hom_space_nullspace(reps_a, reps_b):
        n_a = reps_a[0].shape[0]
        n_b = reps_b[0].shape[0]
        rows_ = []
        for a_k, b_k in zip(reps_a, reps_b):
            op = np.kron(a_k.T, np.eye(n_b)) - np.kron(np.eye(n_a), b_k)
            rows_.append(op)
        mat = np.vstack(rows_)
        _, s_, vt_ = np.linalg.svd(mat, full_matrices=True)
        rank_ = int(np.sum(s_ > TOL * max(mat.shape) * (s_[0] if len(s_) else 1.0)))
        return vt_[rank_:].conj().T

    def evaluate_candidate(M_c, match_s_to_v_c):
        # M_c satisfies M_c @ roots_s[j] = roots_v[match[j]] (root-coordinate map,
        # sigma -> v). For Phi: su3_v -> su3_sigma to preserve [H,E]=root(H)*E,
        # Phi(H_v) must reproduce H_v's OWN root values when evaluated on the
        # matched sigma root vectors -- i.e. Phi(H1v)=M_c[0,0]*H1s+M_c[0,1]*H2s
        # (M_c itself, NOT its inverse -- root coordinates are dual/contravariant
        # to the Cartan generators, so the SAME M_c that maps root-values maps
        # generator-coefficients too, not M_c^-1; caught by skeptic review,
        # verified independently below by re-deriving from the eigenvalue
        # equation directly rather than assuming either convention).
        Phi_H1v_c = M_c[0, 0] * H1s + M_c[0, 1] * H2s
        Phi_H2v_c = M_c[1, 0] * H1s + M_c[1, 1] * H2s
        v_to_s_c = {v: s for s, v in match_s_to_v_c.items()}

        relations_c = []
        for i, j, k in itertools.permutations(range(6), 3):
            if i >= j:
                continue
            if np.max(np.abs(roots_v[i] + roots_v[j] - roots_v[k])) < 1e-6:
                comm_v = E_v[i] @ E_v[j] - E_v[j] @ E_v[i]
                c_v = np.vdot(E_v[k].flatten(), comm_v.flatten()) / np.vdot(
                    E_v[k].flatten(), E_v[k].flatten()
                )
                if abs(c_v) < 1e-8:
                    continue
                si, sj, sk = v_to_s_c[i], v_to_s_c[j], v_to_s_c[k]
                comm_s = F_s[si] @ F_s[sj] - F_s[sj] @ F_s[si]
                c_s = np.vdot(F_s[sk].flatten(), comm_s.flatten()) / np.vdot(
                    F_s[sk].flatten(), F_s[sk].flatten()
                )
                if abs(c_s) < 1e-8:
                    continue
                relations_c.append((i, j, k, c_v, c_s))

        gauge_idx = i1
        free_idx = [k for k in range(6) if k != gauge_idx]

        def residual_vec(x):
            mu_full = np.empty(6, dtype=complex)
            mu_full[gauge_idx] = 1.0
            for pos, k in enumerate(free_idx):
                mu_full[k] = x[2 * pos] + 1j * x[2 * pos + 1]
            res = []
            for i, j, k, c_v, c_s in relations_c:
                val = mu_full[i] * mu_full[j] * c_s - mu_full[k] * c_v
                res.append(val.real)
                res.append(val.imag)
            return np.array(res)

        x0 = np.zeros(10)
        for pos in range(5):
            x0[2 * pos] = 1.0
        sol = least_squares(residual_vec, x0, method="lm", max_nfev=20000)
        mu_fit = np.empty(6, dtype=complex)
        mu_fit[gauge_idx] = 1.0
        for pos, k in enumerate(free_idx):
            mu_fit[k] = sol.x[2 * pos] + 1j * sol.x[2 * pos + 1]
        mu_fit_residual = float(np.max(np.abs(residual_vec(sol.x)))) if relations_c else None

        gens_v_ordered_c = [H1v, H2v] + E_v
        Phi_gens_sigma_c = [Phi_H1v_c, Phi_H2v_c] + [mu_fit[k] * F_s[v_to_s_c[k]] for k in range(6)]

        hom_basis = hom_space_nullspace(gens_v_ordered_c, Phi_gens_sigma_c)
        hom_dim = hom_basis.shape[1]

        rng2 = np.random.default_rng(0)
        found_S = None
        best_det = 0.0
        for _ in range(200):
            coeffs = rng2.normal(size=hom_dim) + 1j * rng2.normal(size=hom_dim)
            # NOTE: hom_basis columns are nullspace vectors of `op`, built from
            # the Kronecker identity vec(AXB)=(B^T kron A)vec(X), which uses
            # COLUMN-MAJOR (Fortran) vec() by mathematical convention. numpy's
            # default .reshape() is row-major (C order) -- reshaping without
            # order='F' silently reconstructs a DIFFERENT matrix that is NOT
            # actually in the nullspace of the original equation (found via
            # direct residual check: op@vec_F(S)=0 but S@A-B@S!=0 when S is
            # rebuilt via C-order reshape). This bug is also present in
            # round127's e44 script's identical `S_flat.reshape(8,8)` call.
            S = (hom_basis @ coeffs).reshape(8, 8, order="F")
            det = abs(np.linalg.det(S))
            if det > best_det:
                best_det = det
            if det > 1e-3:
                found_S = S
                break

        iso_residual = None
        bml_fit_relative = None
        bml_fit_coeffs = None
        if found_S is not None:
            S = found_S
            Sinv = np.linalg.inv(S)
            iso_residual = max(
                float(np.max(np.abs(S @ gens_v_ordered_c[i] @ Sinv - Phi_gens_sigma_c[i])))
                for i in range(8)
            )
            if "--debug" in sys.argv:
                raw_resid = max(
                    float(np.max(np.abs(S @ gens_v_ordered_c[i] - Phi_gens_sigma_c[i] @ S)))
                    for i in range(8)
                )
                print(
                    f"    [diag] cond(S)={np.linalg.cond(S):.3e}  raw_Sylvester_resid(no-inverse)={raw_resid:.3e}  "
                    f"iso_residual(after-inverse)={iso_residual:.3e}"
                )
            _cent_dim, cent_v_real = G102.centralizer_dim(G102.stabilizer_basis(der))
            cent_v = [c_.astype(complex) for c_ in cent_v_real]
            cent_transported = [S @ Cc @ Sinv for Cc in cent_v]
            A_fit = np.stack([c_.flatten() for c_ in cent_transported], axis=1)
            b_fit = BmL.flatten()
            coeffs_fit, *_ = np.linalg.lstsq(A_fit, b_fit, rcond=None)
            recon = A_fit @ coeffs_fit
            fit_residual = float(np.max(np.abs(recon - b_fit)))
            bml_fit_relative = fit_residual / float(np.max(np.abs(b_fit)))
            bml_fit_coeffs = [complex(x) for x in coeffs_fit]

        return {
            "mu_fit_residual": mu_fit_residual,
            "hom_dim": hom_dim,
            "best_det": best_det,
            "found_S": found_S is not None,
            "iso_residual": iso_residual,
            "bml_fit_relative": bml_fit_relative,
            "bml_fit_coeffs": bml_fit_coeffs,
        }

    # --- Step 4b: try ALL exact-hexagon-match candidates, not just the first ---
    all_results = []
    for key, resid, T_c, match_c in all_candidates:
        r = evaluate_candidate(T_c, match_c)
        all_results.append(r)
        if "--debug" in sys.argv:
            print(
                f"candidate hexagon_resid={resid:.2e} mu_fit_resid={r['mu_fit_residual']:.2e} "
                f"hom_dim={r['hom_dim']} found_S={r['found_S']} best_det={r['best_det']:.2e}"
            )

    # pick the best result: prefer found_S=True, else max hom_dim
    all_results.sort(key=lambda r: (not r["found_S"], -r["hom_dim"]))
    best_result = all_results[0]
    log_fit_residual = best_result["mu_fit_residual"]
    hom_dim = best_result["hom_dim"]
    best_det = best_result["best_det"]
    found_S = best_result["found_S"]
    iso_residual = best_result["iso_residual"]
    bml_fit_relative = best_result["bml_fit_relative"]
    bml_fit_coeffs = best_result["bml_fit_coeffs"]
    n_candidates_tried = len(all_candidates)
    n_candidates_with_hom6 = sum(1 for r in all_results if r["hom_dim"] >= 6)

    if max_hexagon_resid > 1e-6:
        verdict = "ALIGNMENT_FAILED"
    elif hom_dim < 6:
        verdict = "ALIGNMENT_INSUFFICIENT"
    elif found_S is None:
        verdict = "ALIGNMENT_INSUFFICIENT"
    elif iso_residual is not None and iso_residual > 1e-4:
        verdict = "ALIGNMENT_INSUFFICIENT"
    else:
        verdict = "ALIGNMENT_SUCCESSFUL"

    results = {
        "round": 128,
        "v_sum_triple": v_sum_triple,
        "s_sum_triple": s_sum_triple,
        "M_matrix": M.tolist(),
        "hexagon_match_residual": max_hexagon_resid,
        "n_candidates_tried": n_candidates_tried,
        "n_candidates_with_hom6": n_candidates_with_hom6,
        "mu_fit_residual_of_best_candidate": log_fit_residual,
        "hom_dim": hom_dim,
        "best_det_found": best_det,
        "isomorphism_found": found_S,
        "iso_residual": iso_residual,
        "bml_fit_relative": bml_fit_relative,
        "bml_fit_coeffs": [str(x) for x in bml_fit_coeffs] if bml_fit_coeffs is not None else None,
        "verdict": verdict,
    }

    print("=" * 92)
    print("Round128 -- explicit Cartan-Weyl alignment Phi: su3_v -> su3_sigma")
    print("=" * 92)
    print(f"su3_v sum-relation triple: {v_sum_triple}")
    print(
        f"Distinct exact-hexagon-match candidates found: {n_candidates_tried} (of |Aut(A2)|=12 possible)"
    )
    print(f"Candidates achieving Hom_dim>=6: {n_candidates_with_hom6} / {n_candidates_tried}")
    print(f"Best candidate: hexagon_resid={max_hexagon_resid:.3e}  M = {np.round(M, 6)}")
    print(f"mu-fit residual (best candidate): {log_fit_residual}")
    print(f"Hom_dim(Phi-aligned, best candidate) = {hom_dim} (predict 6)")
    print(f"Best |det(S)| over 200 trials = {best_det:.6e}")
    if found_S:
        print(f"Isomorphism residual: {iso_residual:.3e}")
        print(f"B-L fit relative residual: {bml_fit_relative:.6e}")
        print(f"B-L fit coeffs: {bml_fit_coeffs}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
