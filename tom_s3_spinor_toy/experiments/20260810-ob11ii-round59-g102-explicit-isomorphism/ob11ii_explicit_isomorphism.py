"""OB11(ii) hard half, step 2: find the explicit intertwiner between round59's
su(3)-on-Sigma and G102's su(3)-on-channel_v -- C65 already proved these are
the same abstract su(3)-module (Casimir exactly -4/3 both), so existence is
not in question; this constructs it explicitly.

Reuses round128's generic Cartan-Weyl alignment helpers (ad_matrix,
extract_csa_and_roots, orthonormalize, find_hexagon_map) unmodified, plus
this project's own Sylvester/Kronecker Hom-space technique (as in C63/C61),
adapted into a fresh orchestration for THIS pair (round128's own main() is
specific to its original su3_v/su3_sigma pair and is not itself reusable as
a function).
"""

from __future__ import annotations

import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_explicit_isomorphism.json"


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


def hom_basis(rep_a: list[np.ndarray], rep_b: list[np.ndarray]) -> np.ndarray:
    n_a, n_b = rep_a[0].shape[0], rep_b[0].shape[0]
    rows = [np.kron(a.T, np.eye(n_b)) - np.kron(np.eye(n_a), b) for a, b in zip(rep_a, rep_b)]
    mat = np.vstack(rows)
    _, s, vt = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(mat.shape) * (s[0] if len(s) else 1.0)))
    return vt[rank:].conj().T


def evaluate_candidate(
    roots_a: np.ndarray,
    E_a: list[np.ndarray],
    roots_b: np.ndarray,
    F_b: list[np.ndarray],
    M: np.ndarray,
    match_b_to_a: dict,
    a_sum_triple: tuple[int, int, int],
) -> dict:
    """Given a root-coordinate map M (b->a) and index correspondence, fit
    root-vector scalars via least squares over ALL bracket relations, then
    search for the representation-level intertwiner S via the Sylvester
    nullspace (adapted from round128's own evaluate_candidate)."""
    relations = []
    for i, j, k in itertools.permutations(range(6), 3):
        if i >= j:
            continue
        if np.max(np.abs(roots_a[i] + roots_a[j] - roots_a[k])) < 1e-6:
            comm_a = E_a[i] @ E_a[j] - E_a[j] @ E_a[i]
            c_a = np.vdot(E_a[k].flatten(), comm_a.flatten()) / np.vdot(
                E_a[k].flatten(), E_a[k].flatten()
            )
            if abs(c_a) < 1e-8:
                continue
            a_to_b = {v: b for b, v in match_b_to_a.items()}
            if i not in a_to_b or j not in a_to_b or k not in a_to_b:
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
    mu_fit = np.empty(6, dtype=complex)
    mu_fit[gauge_idx] = 1.0
    for pos, k in enumerate(free_idx):
        mu_fit[k] = sol.x[2 * pos] + 1j * sol.x[2 * pos + 1]
    mu_residual = float(np.max(np.abs(residual_vec(sol.x)))) if relations else None

    a_to_b = {v: b for b, v in match_b_to_a.items()}
    return {
        "mu_fit_residual": mu_residual,
        "mu_fit": mu_fit,
        "a_to_b": a_to_b,
        "M": M,
    }


def main() -> None:
    su3_r59 = to_numpy_su3_r59()
    su3_g102 = su3_g102_on_channel_v()

    r59_onb = R128.orthonormalize(su3_r59)
    g102_onb = R128.orthonormalize(su3_g102)

    rng = np.random.default_rng(1)
    c1 = rng.normal(size=8)
    H_seed_r59 = sum(ci * Ai for ci, Ai in zip(c1, r59_onb))
    _null_r59, H1_r59, H2_r59, roots_r59, E_r59 = R128.extract_csa_and_roots(r59_onb, H_seed_r59)

    c2 = rng.normal(size=8)
    H_seed_g102 = sum(ci * Ai for ci, Ai in zip(c2, g102_onb))
    _null_g102, H1_g102, H2_g102, roots_g102, E_g102 = R128.extract_csa_and_roots(
        g102_onb, H_seed_g102
    )

    p1_pass = roots_r59.shape[0] == 6 and roots_g102.shape[0] == 6

    r59_triple = find_sum_triple(roots_r59)
    g102_triples = all_sum_triples(roots_g102)
    p2_pass = len(g102_triples) > 0

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
                resid0 = np.max(np.abs(pred0 - target0))
                if resid0 > 1e-6:
                    continue
                match = {}
                match[j1] = va if sign == 1 else neg_index(roots_r59, va)
                match[j2] = vb if sign == 1 else neg_index(roots_r59, vb)
                match[j0] = i0 if sign == 1 else neg_index(roots_r59, i0)
                for gidx in list(match):
                    vidx = match[gidx]
                    match[neg_index(roots_g102, gidx)] = neg_index(roots_r59, vidx)
                max_resid = max(
                    np.max(np.abs(T @ roots_g102[g_] - roots_r59[v_])) for g_, v_ in match.items()
                )
                candidates.append((max_resid, T, dict(match)))

    candidates.sort(key=lambda c: c[0])

    best_result = None
    for hexagon_resid, T, match in candidates[:12]:
        ev = evaluate_candidate(roots_r59, E_r59, roots_g102, E_g102, T, match, r59_triple)
        mu_fit = ev["mu_fit"]
        a_to_b = ev["a_to_b"]
        Phi_H1 = T[0, 0] * H1_g102 + T[0, 1] * H2_g102
        Phi_H2 = T[1, 0] * H1_g102 + T[1, 1] * H2_g102
        gens_r59_ordered = [H1_r59, H2_r59] + E_r59
        gens_g102_scaled = [Phi_H1, Phi_H2] + [mu_fit[k] * E_g102[a_to_b[k]] for k in range(6)]

        basis = hom_basis(gens_r59_ordered, gens_g102_scaled)
        hom_dim = basis.shape[1]
        if hom_dim == 0:
            continue

        rng2 = np.random.default_rng(0)
        found_S, best_det = None, 0.0
        for _ in range(200):
            coeffs = rng2.normal(size=hom_dim) + 1j * rng2.normal(size=hom_dim)
            S = (basis @ coeffs).reshape(8, 8, order="F")
            det = abs(np.linalg.det(S))
            best_det = max(best_det, det)
            if det > 1e-3:
                found_S = S
                break

        iso_residual = None
        if found_S is not None:
            Sinv = np.linalg.inv(found_S)
            iso_residual = max(
                float(np.max(np.abs(found_S @ gens_r59_ordered[i] @ Sinv - gens_g102_scaled[i])))
                for i in range(8)
            )

        candidate_result = {
            "hexagon_residual": float(hexagon_resid),
            "mu_fit_residual": ev["mu_fit_residual"],
            "hom_dim": hom_dim,
            "best_det": best_det,
            "found_S": found_S is not None,
            "iso_residual": iso_residual,
        }
        if best_result is None or (
            candidate_result["found_S"]
            and (not best_result["found_S"] or hom_dim > best_result["hom_dim"])
        ):
            best_result = candidate_result

    p3_pass = bool(best_result and best_result["found_S"] and best_result["iso_residual"] < 1e-4)

    if not (p1_pass and p2_pass):
        verdict = "HARNESS_SETUP_FAILED"
    elif p3_pass:
        verdict = "EXPLICIT_ISOMORPHISM_FOUND"
    else:
        verdict = "NO_ISOMORPHISM_FOUND_PROCEDURE_BUG_SUSPECTED"

    results = {
        "experiment": "ob11ii_round59_g102_explicit_isomorphism",
        "p1_both_have_6_roots": p1_pass,
        "n_g102_sum_triples": len(g102_triples),
        "p2_pass": p2_pass,
        "n_candidates_tried": len(candidates),
        "best_result": best_result,
        "p3_isomorphism_found_clean": p3_pass,
        "verdict": verdict,
    }

    print("=" * 92)
    print("OB11(ii) hard half, step 2: explicit round59<->G102 su(3) intertwiner")
    print("=" * 92)
    print(f"P1 (both 6 roots)?  {p1_pass}")
    print(f"n_g102_sum_triples = {len(g102_triples)}   P2 pass? {p2_pass}")
    print(f"n_candidates_tried = {len(candidates)}")
    print(f"best_result = {best_result}")
    print(f"P3 (clean isomorphism found)?  {p3_pass}")
    print()
    print(f"VERDICT: {verdict}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults -> {RESULTS_PATH}")


if __name__ == "__main__":
    main()
