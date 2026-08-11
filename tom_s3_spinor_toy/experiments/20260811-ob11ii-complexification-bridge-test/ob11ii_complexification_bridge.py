"""OB11(ii) hard half: the complexification bridge test. Does a complex
intertwiner U in GL(8,C) exist between round59's su(3) (complex,
anti-Hermitian) and G102's su(3) (real, antisymmetric)? C65 already proved
these are the same abstract su(3)-module (Casimir exactly -4/3 both); this
round drops the real-coefficient assumption that broke the earlier attempt
(20260810-ob11ii-round59-g102-explicit-isomorphism, BLOCKED-SUBSTRATE) and
searches for the isomorphism in its native, unconstrained complex form.

Reuses round128's ad_matrix/orthonormalize unmodified (no reality
assumption in either). Does NOT reuse round128's extract_csa_and_roots
as-is -- that function asserts real CSA coefficients; this script defines
its own complex-coefficient version instead, since patching an existing
experiment's file is out of scope.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_complexification_bridge.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R128 = load_module(
    "e45_cartan_weyl_alignment",
    HERE.parent / "20260718-round128-cartan-weyl-alignment" / "e45_cartan_weyl_alignment.py",
)
R59 = load_module(
    "round59_route_a_independent",
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py",
)
G102 = load_module(
    "g102_spin8_fiber",
    HERE.parent / "20260705-g102-spin8-fiber-obstruction" / "g102_spin8_fiber.py",
)

TOL = 1e-8


def to_numpy_su3_r59() -> list[np.ndarray]:
    clifford = R59.build_clifford()
    return [
        np.array(R59.spin_lift(R59.ADNU[i], clifford).evalf(), dtype=complex) for i in range(1, 9)
    ]


def su3_g102_on_channel_v() -> list[np.ndarray]:
    der = G102.derivation_basis()
    su3 = G102.stabilizer_basis(der)
    v_out, _s_out, _c_out = G102.restrict_to_subalgebra(su3)
    return [g.astype(complex) for g in v_out]


def hom_basis(rep_a: list[np.ndarray], rep_b: list[np.ndarray]) -> np.ndarray:
    """Complex Sylvester/Kronecker nullspace: columns are vec(S), S A_k = B_k S."""
    n_a, n_b = rep_a[0].shape[0], rep_b[0].shape[0]
    rows = [np.kron(a.T, np.eye(n_b)) - np.kron(np.eye(n_a), b) for a, b in zip(rep_a, rep_b)]
    mat = np.vstack(rows)
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(mat.shape) * (s[0] if len(s) else 1.0)))
    return vt[rank:].conj().T


def search_nonzero_intertwiner(basis: np.ndarray, n_trials: int = 300, seed: int = 0):
    """Random complex combinations of the Hom-space basis, looking for a
    nondegenerate (det != 0) 8x8 intertwiner."""
    if basis.shape[1] == 0:
        return None, 0.0
    rng = np.random.default_rng(seed)
    best_det = 0.0
    for _ in range(n_trials):
        coeffs = rng.normal(size=basis.shape[1]) + 1j * rng.normal(size=basis.shape[1])
        S = (basis @ coeffs).reshape(8, 8, order="F")
        det = abs(np.linalg.det(S))
        best_det = max(best_det, det)
        if det > 1e-3:
            return S, best_det
    return None, best_det


def extract_csa_and_roots_complex(
    gens: list[np.ndarray], H_seed: np.ndarray, combo_weight: float = 0.37123
):
    """Complex-coefficient variant of round128's extract_csa_and_roots -- same
    method (generic-element centralizer -> CSA -> simultaneous diagonalization
    -> roots), WITHOUT asserting the CSA coefficients come out real. This is
    the one genuine adaptation this round makes; everything else is reused."""
    n = len(gens)
    comms = [H_seed @ g - g @ H_seed for g in gens]
    M = np.array([c.flatten() for c in comms]).T
    _, s, vt = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(M.shape) * s[0]))
    assert n - rank == 2, f"expected 2-dim CSA, got {n - rank}"
    null = vt[rank:].conj().T  # NOTE: kept complex, not forced real (the actual adaptation)
    H1 = sum(null[j, 0] * gens[j] for j in range(n))
    H2 = sum(null[j, 1] * gens[j] for j in range(n))

    adH1 = R128.ad_matrix(H1, gens)
    adH2 = R128.ad_matrix(H2, gens)
    assert np.max(np.abs(adH1 @ adH2 - adH2 @ adH1)) < 1e-6

    Q, _ = np.linalg.qr(np.hstack([null, np.eye(n)]))
    complement = Q[:, 2:n]
    adH1_c = complement.conj().T @ adH1 @ complement
    adH2_c = complement.conj().T @ adH2 @ complement

    combo = adH1_c + combo_weight * adH2_c
    _evals, evecs = np.linalg.eig(combo)
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
    E_coefs = complement @ evecs
    E_matrices = [sum(E_coefs[j, k] * gens[j] for j in range(n)) for k in range(m)]
    return null, H1, H2, root_coords, E_matrices


def find_sum_triple(roots: np.ndarray) -> tuple[int, int, int]:
    for i, j, k in itertools.permutations(range(6), 3):
        if np.max(np.abs(roots[i] + roots[j] - roots[k])) < 1e-6:
            return (i, j, k)
    raise AssertionError("no sum-relation found among roots")


def all_sum_triples(roots: np.ndarray) -> list[tuple[int, int, int]]:
    return [
        (i, j, k)
        for i, j, k in itertools.permutations(range(6), 3)
        if np.max(np.abs(roots[i] + roots[j] - roots[k])) < 1e-6
    ]


def neg_index(roots: np.ndarray, idx: int) -> int:
    target = -roots[idx]
    for k in range(len(roots)):
        if np.max(np.abs(roots[k] - target)) < 1e-6:
            return k
    raise ValueError("no negative root found")


def fit_mu_and_search(roots_a, E_a, roots_b, F_b, a_sum_triple, match_b_to_a):
    relations = []
    a_to_b = {v: b for b, v in match_b_to_a.items()}
    for i, j, k in itertools.permutations(range(6), 3):
        if i >= j:
            continue
        if np.max(np.abs(roots_a[i] + roots_a[j] - roots_a[k])) < 1e-6:
            comm_a = E_a[i] @ E_a[j] - E_a[j] @ E_a[i]
            c_a = np.vdot(E_a[k].flatten(), comm_a.flatten()) / np.vdot(
                E_a[k].flatten(), E_a[k].flatten()
            )
            if abs(c_a) < 1e-8 or i not in a_to_b or j not in a_to_b or k not in a_to_b:
                continue
            bi, bj, bk = a_to_b[i], a_to_b[j], a_to_b[k]
            comm_b = F_b[bi] @ F_b[bj] - F_b[bj] @ F_b[bi]
            c_b = np.vdot(F_b[bk].flatten(), comm_b.flatten()) / np.vdot(
                F_b[bk].flatten(), F_b[bk].flatten()
            )
            if abs(c_b) < 1e-8:
                continue
            relations.append((i, j, k, c_a, c_b))

    gauge_idx = a_sum_triple[0]
    free_idx = [k for k in range(6) if k != gauge_idx]

    def residual_vec(x):
        mu = np.empty(6, dtype=complex)
        mu[gauge_idx] = 1.0
        for pos, k in enumerate(free_idx):
            mu[k] = x[2 * pos] + 1j * x[2 * pos + 1]
        res = []
        for i, j, k, c_a, c_b in relations:
            val = mu[i] * mu[j] * c_b - mu[k] * c_a
            res.append(val.real)
            res.append(val.imag)
        return np.array(res)

    x0 = np.zeros(10)
    for pos in range(5):
        x0[2 * pos] = 1.0
    sol = least_squares(residual_vec, x0, method="lm", max_nfev=20000)
    mu = np.empty(6, dtype=complex)
    mu[gauge_idx] = 1.0
    for pos, k in enumerate(free_idx):
        mu[k] = sol.x[2 * pos] + 1j * sol.x[2 * pos + 1]
    mu_residual = float(np.max(np.abs(residual_vec(sol.x)))) if relations else None
    return mu, mu_residual, a_to_b


def main() -> None:
    su3_r59 = to_numpy_su3_r59()
    su3_g102 = su3_g102_on_channel_v()

    # --- Control (added after diagnosing hom_dim=4 in the cross-matching search):
    # Hom_su3(V,V) for EACH side alone, no cross-construction matching at all. Rules
    # out hom_basis() itself and either individual construction as the source of the
    # hom_dim=4-not-6 discrepancy found below -- isolates the gap to the
    # cross-construction correspondence pipeline specifically. ---
    control_r59_self_dim = int(hom_basis(su3_r59, su3_r59).shape[1])
    control_g102_self_dim = int(hom_basis(su3_g102, su3_g102).shape[1])
    control_both_give_6 = control_r59_self_dim == 6 and control_g102_self_dim == 6

    # --- P1: cheapest test, direct given ordering, no matching at all ---
    basis_direct = hom_basis(su3_r59, su3_g102)
    S_direct, _det_direct = search_nonzero_intertwiner(basis_direct)
    p1_direct_works = S_direct is not None
    iso_residual_direct = None
    if S_direct is not None:
        Sinv = np.linalg.inv(S_direct)
        iso_residual_direct = max(
            float(np.max(np.abs(S_direct @ su3_r59[i] @ Sinv - su3_g102[i]))) for i in range(8)
        )
        if iso_residual_direct > 1e-4:
            S_direct = None
            p1_direct_works = False

    result = {
        "control_hom_su3_r59_self_dim": control_r59_self_dim,
        "control_hom_su3_g102_self_dim": control_g102_self_dim,
        "control_both_give_predicted_6": control_both_give_6,
        "p1_hom_dim_direct": int(basis_direct.shape[1]),
        "p1_direct_ordering_works": p1_direct_works,
        "p1_iso_residual_direct": iso_residual_direct,
    }

    if p1_direct_works:
        result["verdict"] = "EXPLICIT_ISOMORPHISM_FOUND_DIRECT_ORDERING"
        print("P1 (direct ordering) SUCCEEDED -- no Cartan-Weyl matching needed.")
        print(json.dumps(result, indent=2, default=str))
        RESULTS_PATH.write_text(json.dumps(result, indent=2, default=str))
        return

    # --- P2/P3: complex-coefficient Cartan-Weyl matching ---
    r59_onb = R128.orthonormalize(su3_r59)
    g102_onb = R128.orthonormalize(su3_g102)

    rng = np.random.default_rng(1)
    c1 = rng.normal(size=8)
    H_seed_r59 = sum(ci * Ai for ci, Ai in zip(c1, r59_onb))
    _n1, H1_r59, H2_r59, roots_r59, E_r59 = extract_csa_and_roots_complex(r59_onb, H_seed_r59)

    c2 = rng.normal(size=8)
    H_seed_g102 = sum(ci * Ai for ci, Ai in zip(c2, g102_onb))
    _n2, H1_g102, H2_g102, roots_g102, E_g102 = extract_csa_and_roots_complex(g102_onb, H_seed_g102)

    p2_pass = roots_r59.shape[0] == 6 and roots_g102.shape[0] == 6
    result["p2_complex_csa_extraction_succeeded"] = p2_pass

    r59_triple = find_sum_triple(roots_r59)
    g102_triples = all_sum_triples(roots_g102)

    i1, i2, i0 = r59_triple
    candidates = []
    for j1, j2, j0 in g102_triples:
        for va, vb in [(i1, i2), (i2, i1)]:
            for sign in [1, -1]:
                A = np.stack([roots_g102[j1], roots_g102[j2]], axis=0)
                B = np.stack([sign * roots_r59[va], sign * roots_r59[vb]], axis=0)
                if abs(np.linalg.det(A)) < 1e-9:
                    continue
                T = np.linalg.solve(A, B).T
                pred0 = T @ roots_g102[j0]
                target0 = sign * roots_r59[i0]
                if np.max(np.abs(pred0 - target0)) > 1e-6:
                    continue
                match = {}
                match[j1] = va if sign == 1 else neg_index(roots_r59, va)
                match[j2] = vb if sign == 1 else neg_index(roots_r59, vb)
                match[j0] = i0 if sign == 1 else neg_index(roots_r59, i0)
                for gidx in list(match):
                    vidx = match[gidx]
                    match[neg_index(roots_g102, gidx)] = neg_index(roots_r59, vidx)
                candidates.append((T, dict(match)))

    all_candidates_results = []
    best = None
    for T, match in candidates:
        mu, mu_resid, a_to_b = fit_mu_and_search(
            roots_r59, E_r59, roots_g102, E_g102, r59_triple, match
        )
        Phi_H1 = T[0, 0] * H1_g102 + T[0, 1] * H2_g102
        Phi_H2 = T[1, 0] * H1_g102 + T[1, 1] * H2_g102
        gens_r59_ordered = [H1_r59, H2_r59] + E_r59
        gens_g102_scaled = [Phi_H1, Phi_H2] + [mu[k] * E_g102[a_to_b[k]] for k in range(6)]
        basis = hom_basis(gens_r59_ordered, gens_g102_scaled)
        if basis.shape[1] == 0:
            all_candidates_results.append({"mu_fit_residual": mu_resid, "hom_dim": 0})
            continue
        S, best_det = search_nonzero_intertwiner(basis)
        iso_resid = None
        if S is not None:
            Sinv = np.linalg.inv(S)
            iso_resid = max(
                float(np.max(np.abs(S @ gens_r59_ordered[i] @ Sinv - gens_g102_scaled[i])))
                for i in range(8)
            )
        cand_result = {
            "mu_fit_residual": mu_resid,
            "hom_dim": basis.shape[1],
            "found_S": S is not None,
            "best_det": best_det,
            "iso_residual": iso_resid,
        }
        all_candidates_results.append(cand_result)
        if best is None or (cand_result["found_S"] and not best.get("found_S")):
            best = cand_result

    result["n_candidates_tried"] = len(candidates)
    result["hom_dim_distribution"] = sorted({c["hom_dim"] for c in all_candidates_results})
    result["n_candidates_with_hom_dim_gt_0"] = sum(
        1 for c in all_candidates_results if c["hom_dim"] > 0
    )
    result["all_candidates"] = all_candidates_results
    result["best_candidate"] = best
    p3_pass = bool(
        best
        and best.get("found_S")
        and best.get("iso_residual") is not None
        and best["iso_residual"] < 1e-4
    )
    result["p3_isomorphism_found"] = p3_pass

    if not p2_pass:
        result["verdict"] = "HARNESS_SETUP_FAILED"
    elif p3_pass:
        result["verdict"] = "EXPLICIT_ISOMORPHISM_FOUND_VIA_MATCHING"
    else:
        result["verdict"] = "NO_ISOMORPHISM_FOUND_DESPITE_COMPLEX_SEARCH"

    print("=" * 92)
    print("OB11(ii) complexification bridge test")
    print("=" * 92)
    print(json.dumps(result, indent=2, default=str))

    RESULTS_PATH.write_text(json.dumps(result, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
