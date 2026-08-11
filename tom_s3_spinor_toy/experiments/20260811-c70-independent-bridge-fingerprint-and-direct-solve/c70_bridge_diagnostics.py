"""C70 -- independent bridge round, superseding the Cartan-Weyl root-matching
pipeline. Three sub-tests, run in the order the C69 decision.md's Kill
Analysis proposed:

1. Non-normality test on round59's ad(H) (the specific suspect C69 identified
   for why Rayleigh-quotient root extraction might read off wrong root values).
2. Bracket-structure invariant (Sum_{a,b,c} |tr(T_c^dagger [T_a,T_b])|^2) on an
   orthonormalized generator set -- basis-independent by construction, rules out
   any structure-constant normalization/scale mismatch between the two
   constructions.
3. Direct global nonlinear solve for a Lie-algebra isomorphism Phi: su(3)_r59 ->
   su(3)_g102, bypassing CSA/root-matching entirely -- parametrize Phi as the
   8x8 complex change-of-basis matrix between the two generator sets and solve
   the bracket-preservation equations via Levenberg-Marquardt with many random
   restarts. A first, unconstrained version of this (not reproduced here)
   collapsed to the trivial sink Phi=0 on every restart: the residual is
   quadratic-minus-linear in Phi, so Phi=0 is always an exact root and is not
   excluded by an unconstrained least-squares objective. This version adds a
   soft non-triviality constraint (pins ||Phi||_F^2 away from 0) to remove
   that sink.

Reuses round59/G102 construction functions unmodified from the already-committed
C68 module (to_numpy_su3_r59, su3_g102_on_channel_v) and round128's ad_matrix /
orthonormalize (unmodified, no reality assumption in either).
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c70.json"


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
C68 = load_module(
    "ob11ii_complexification_bridge",
    HERE.parent
    / "20260811-ob11ii-complexification-bridge-test"
    / "ob11ii_complexification_bridge.py",
)


# ---------------------------------------------------------------------------
# Test 1: non-normality of ad(H) on round59's side
# ---------------------------------------------------------------------------
def test_normality(gens_r59: list[np.ndarray]) -> dict:
    """C69's identified suspect: round59's complex CSA might make ad(H)
    non-normal, breaking the Rayleigh-quotient root extraction (Rayleigh
    quotients equal eigenvalues only for normal operators). Test directly via
    (a) the commutator [A, A^dagger] (zero iff normal) and (b) the residual
    of the Rayleigh-extracted "eigenvector" against the true eigen-equation."""
    H_seed = sum(0.1 * (i + 1) * gens_r59[i] for i in range(len(gens_r59)))
    _null, H1, _H2, _root_coords, _E = C68.extract_csa_and_roots_complex(gens_r59, H_seed)
    adH1 = R128.ad_matrix(H1, gens_r59)

    commutator_norm = float(np.max(np.abs(adH1 @ adH1.conj().T - adH1.conj().T @ adH1)))

    # Re-derive the complement-space eigenvectors exactly as extract_csa_and_roots_complex
    # does internally, to test the Rayleigh-quotient values against the true eigen-equation.
    n = len(gens_r59)
    comms = [H_seed @ g - g @ H_seed for g in gens_r59]
    M = np.array([c.flatten() for c in comms]).T
    _, s, vt = np.linalg.svd(M, full_matrices=True)
    rank = int(np.sum(s > 1e-8 * max(M.shape) * s[0]))
    null = vt[rank:].conj().T
    Q, _ = np.linalg.qr(np.hstack([null, np.eye(n)]))
    complement = Q[:, 2:n]
    adH1_c = complement.conj().T @ adH1 @ complement
    _evals, evecs = np.linalg.eig(adH1_c)
    m = n - 2
    eig_residuals = []
    for k in range(m):
        v = evecs[:, k]
        rayleigh = (v.conj() @ adH1_c @ v) / (v.conj() @ v)
        eig_residuals.append(float(np.linalg.norm(adH1_c @ v - rayleigh * v)))

    is_normal = commutator_norm < 1e-8 and max(eig_residuals) < 1e-8
    return {
        "commutator_norm": commutator_norm,
        "is_normal": is_normal,
        "max_eigenvector_residual": max(eig_residuals),
        "verdict": (
            "REFUTED (ad(H) is normal, Rayleigh quotients are exact eigenvalues)"
            if is_normal
            else "CONFIRMED (non-normal -- Rayleigh quotients may be inexact)"
        ),
    }


# ---------------------------------------------------------------------------
# Test 2: bracket-structure invariant
# ---------------------------------------------------------------------------
def bracket_invariant(gens_onb: list[np.ndarray]) -> float:
    """Sum_{a,b,c} |tr(T_c^dagger [T_a,T_b])|^2 over an orthonormalized
    generator set -- fully basis-independent by construction (any two
    orthonormal bases of the same Lie algebra under the same inner product
    give the same value)."""
    n = len(gens_onb)
    total = 0.0
    for a in range(n):
        for b in range(n):
            comm = gens_onb[a] @ gens_onb[b] - gens_onb[b] @ gens_onb[a]
            for c in range(n):
                coeff = np.trace(gens_onb[c].conj().T @ comm)
                total += abs(coeff) ** 2
    return float(total)


def test_bracket_invariant(gens_r59: list[np.ndarray], gens_g102: list[np.ndarray]) -> dict:
    onb_r59 = R128.orthonormalize(gens_r59)
    onb_g102 = R128.orthonormalize(gens_g102)
    inv_r59 = bracket_invariant(onb_r59)
    inv_g102 = bracket_invariant(onb_g102)
    ratio = inv_r59 / inv_g102 if inv_g102 != 0 else float("nan")
    return {
        "invariant_r59": inv_r59,
        "invariant_g102": inv_g102,
        "ratio": ratio,
        "verdict": (
            "MATCH (no structure-constant scale mismatch)"
            if abs(ratio - 1.0) < 1e-6
            else "MISMATCH"
        ),
    }


# ---------------------------------------------------------------------------
# Test 3: direct global nonlinear solve for Phi (non-triviality-constrained)
# ---------------------------------------------------------------------------
def compute_structure_tensor(gens: list[np.ndarray]) -> np.ndarray:
    """f[a,b,k] such that [Xa,Xb] = sum_k f[a,b,k] Xk, solved via the Gram
    matrix of the (in general non-orthonormal) generator set."""
    n = len(gens)
    gram = np.array([[np.trace(gens[i].conj().T @ gens[j]) for j in range(n)] for i in range(n)])
    gram_inv = np.linalg.inv(gram)
    f = np.zeros((n, n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            proj = np.array([np.trace(gens[k].conj().T @ comm) for k in range(n)])
            f[a, b, :] = gram_inv @ proj
    return f


def _unpack_phi(x: np.ndarray) -> np.ndarray:
    return (x[:64] + 1j * x[64:]).reshape(8, 8)


def residual_real(
    x: np.ndarray, struct_r59: np.ndarray, struct_g102: np.ndarray, norm_weight: float
) -> np.ndarray:
    """Phi[i,a] is the coefficient of g102-generator i in the image of
    r59-generator a: Phi(Xa_r59) := sum_i Phi[i,a] Xi_g102.
    Bracket preservation Phi([Xa,Xb]_r59) = [Phi(Xa),Phi(Xb)]_g102 becomes, in
    g102-generator coordinates:
        LHS[k] = sum_m f_r59[a,b,m] Phi[k,m]
        RHS[k] = sum_{i,j} Phi[i,a] Phi[j,b] f_g102[i,j,k]
    A soft constraint norm_weight*(||Phi||_F^2 - 8) is appended to keep the
    solve away from the trivial Phi=0 sink (always an exact root otherwise)."""
    phi = _unpack_phi(x)
    n = 8
    res = []
    for a in range(n):
        for b in range(a + 1, n):
            lhs = np.einsum("m,km->k", struct_r59[a, b, :], phi)
            rhs = np.einsum("i,j,ijk->k", phi[:, a], phi[:, b], struct_g102)
            diff = lhs - rhs
            res.append(diff.real)
            res.append(diff.imag)
    res_vec = np.concatenate(res)
    if norm_weight > 0:
        frob_sq = float(np.sum(np.abs(phi) ** 2))
        res_vec = np.concatenate([res_vec, [norm_weight * (frob_sq - 8.0)]])
    return res_vec


def run_direct_solve(
    gens_r59: list[np.ndarray],
    gens_g102: list[np.ndarray],
    n_trials: int,
    norm_weight: float,
    seed: int,
) -> dict:
    struct_r59 = compute_structure_tensor(gens_r59)
    struct_g102 = compute_structure_tensor(gens_g102)
    rng = np.random.default_rng(seed)
    trials = []
    best = None
    for t in range(n_trials):
        x0 = rng.normal(scale=0.5, size=128)
        sol = least_squares(
            residual_real,
            x0,
            args=(struct_r59, struct_g102, norm_weight),
            method="lm",
            max_nfev=8000,
        )
        phi = _unpack_phi(sol.x)
        det = abs(np.linalg.det(phi))
        max_res = float(np.max(np.abs(sol.fun))) if sol.fun.size else float("nan")
        trials.append({"trial": t, "max_residual": max_res, "det_phi": det})
        if best is None or max_res < best["max_residual"]:
            best = {"max_residual": max_res, "det_phi": det, "phi": phi}
    return {"trials": trials, "best": best}


# ---------------------------------------------------------------------------
# Controls (Gate 3 / Perelman no-collapse discipline): the clean 15/15 result
# above is exactly the shape skeptic-triggers.md flags for mandatory
# verification -- a test that cannot distinguish a known-good case from a
# known-impossible one is not a test.
# ---------------------------------------------------------------------------
def test_positive_control(gens_g102: list[np.ndarray]) -> dict:
    """Ground truth: solve g102-vs-g102 (identical structure tensor on both
    sides). Phi = identity is an EXACT solution of the bracket condition
    (trivially) AND of the norm constraint (||I_8||_F^2 = 8 exactly, matching
    the target used throughout). If the solver reliably lands on this orbit,
    the pipeline is validated the same way C69's P1 validated the old one."""
    result = run_direct_solve(gens_g102, gens_g102, n_trials=5, norm_weight=5.0, seed=7)
    return result


def test_negative_control(gens_r59: list[np.ndarray], seed: int = 123) -> dict:
    """Impossibility check: replace g102's side with 8 independent random
    anti-Hermitian matrices (no genuine Lie-algebra closure, generically NOT
    isomorphic to su(3) as a structure-constant tensor). The solver must fail
    to reach a low residual -- if it doesn't, the test has no discriminating
    power and the positive result above cannot be trusted."""
    rng = np.random.default_rng(seed)
    fake = []
    for _ in range(8):
        a = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
        fake.append(a - a.conj().T)  # anti-Hermitian, same type as r59's generators
    result = run_direct_solve(gens_r59, fake, n_trials=5, norm_weight=5.0, seed=seed)
    return result


# ---------------------------------------------------------------------------
# Test 4: does the representation-space intertwiner U exist, given Phi?
# ---------------------------------------------------------------------------
def test_representation_intertwiner(
    gens_r59: list[np.ndarray], gens_g102: list[np.ndarray], phi: np.ndarray
) -> dict:
    """Phi (found in Test 3) is an isomorphism of su(3) at the level of
    GENERATOR-INDEX coordinates (an abstract Lie-algebra map) -- it does NOT
    by itself give the representation-space intertwiner U that C71 needs to
    transport D, J, gamma. Push rho_r59 forward through Phi: for each g102
    generator index k, M_k := sum_a Phi_inv[a,k] * Xa_r59 is the r59-side
    representation matrix Phi predicts should correspond to Xk_g102. Then ask:
    does a nonzero U exist with U M_k U^-1 = Xk_g102 for all k (reusing C68's
    hom_basis/search_nonzero_intertwiner unmodified)?"""
    phi_inv = np.linalg.inv(phi)
    m_matrices = [sum(phi_inv[a, k] * gens_r59[a] for a in range(8)) for k in range(8)]
    basis = C68.hom_basis(m_matrices, gens_g102)
    hom_dim = basis.shape[1]
    u_matrix, best_det = C68.search_nonzero_intertwiner(basis, n_trials=300, seed=0)

    intertwine_residual = None
    if u_matrix is not None:
        u_inv = np.linalg.inv(u_matrix)
        residuals = [
            float(np.max(np.abs(u_matrix @ m_matrices[k] @ u_inv - gens_g102[k]))) for k in range(8)
        ]
        intertwine_residual = max(residuals)

    return {
        "hom_dim": hom_dim,
        "nonzero_intertwiner_found": u_matrix is not None,
        "best_det_found": best_det,
        "explicit_intertwining_residual": intertwine_residual,
    }


def main() -> None:
    gens_r59 = C68.to_numpy_su3_r59()
    gens_g102 = C68.su3_g102_on_channel_v()

    print("=== Test 1: non-normality of ad(H), round59 side ===")
    t1 = test_normality(gens_r59)
    print(t1)

    print("\n=== Test 2: bracket-structure invariant ===")
    t2 = test_bracket_invariant(gens_r59, gens_g102)
    print(t2)

    print("\n=== Test 3: constrained direct global solve (norm_weight=5.0) ===")
    t3 = run_direct_solve(gens_r59, gens_g102, n_trials=15, norm_weight=5.0, seed=42)
    for tr in t3["trials"]:
        print(
            f"trial {tr['trial']}: max_residual={tr['max_residual']:.4e}, "
            f"|det(Phi)|={tr['det_phi']:.4e}"
        )
    print("BEST:", t3["best"])

    print("\n=== Positive control: g102-vs-g102 ground truth ===")
    t_pos = test_positive_control(gens_g102)
    for tr in t_pos["trials"]:
        print(
            f"  trial {tr['trial']}: max_residual={tr['max_residual']:.4e}, "
            f"|det(Phi)|={tr['det_phi']:.4e}"
        )
    print("  BEST:", t_pos["best"])

    print("\n=== Negative control: r59 vs random anti-Hermitian noise ===")
    t_neg = test_negative_control(gens_r59)
    for tr in t_neg["trials"]:
        print(
            f"  trial {tr['trial']}: max_residual={tr['max_residual']:.4e}, "
            f"|det(Phi)|={tr['det_phi']:.4e}"
        )
    print("  BEST:", t_neg["best"])

    print("\n=== Test 4: representation-space intertwiner U, given Phi ===")
    t4 = test_representation_intertwiner(gens_r59, gens_g102, t3["best"]["phi"])
    print(t4)

    def strip_phi(d: dict) -> dict:
        out = dict(d)
        out["best"] = {k: v for k, v in d["best"].items() if k != "phi"}
        return out

    results = {
        "test1_normality": t1,
        "test2_bracket_invariant": t2,
        "test3_unconstrained_solve_note": (
            "A first, unconstrained version (Phi parametrized identically, no "
            "norm_weight term) collapsed to the trivial sink Phi=0 on all 15/15 "
            "random restarts (max_residual ~1e-324, det(Phi)=0.0 every trial). "
            "Not reproduced here -- deterministic given the missing constraint; "
            "see decision.md for the diagnosis."
        ),
        "test3_constrained_solve": strip_phi(t3),
        "positive_control_g102_vs_g102": strip_phi(t_pos),
        "negative_control_r59_vs_noise": strip_phi(t_neg),
        "test4_representation_intertwiner": t4,
    }
    RESULTS_PATH.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
