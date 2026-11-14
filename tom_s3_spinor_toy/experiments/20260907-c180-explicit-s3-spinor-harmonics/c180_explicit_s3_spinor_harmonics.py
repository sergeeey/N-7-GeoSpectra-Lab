"""C180: explicit S^3 spinor harmonics in the parallelizing trivialization,
plus Tom Lawrence's eq (77) for the S^3 VECTOR multiplet as a control.

Answers items 2-3 of the plan built on C179's finding: spinor harmonics
cannot be a multiplet of functions carrying an SO(4) rep, but S^3 = SU(2)
is parallelizable, so in the group trivialization they ARE C^4-valued
functions carrying a Spin(4) rep.

Construction (no external library, everything built from scratch here):
  * S^3 = unit quaternions q = x0 + x1 i + x2 j + x3 k
  * left / right invariant vector fields = generators of q -> e_a q and
    q -> q e_a, written as linear vector fields V_M = sum_mu (M x)_mu d_mu
  * harmonic polynomials H_k = ker(Laplacian) on homogeneous degree-k
    polynomials in 4 variables, dim (k+1)^2
  * D_0 = -i sum_a sigma_a (x) X_a^R  acting on C^2 (x) H_k

Reference values this construction must REPRODUCE (not derive): round67's
S^3 Dirac degeneracy (n+1)(n+2), independently in c85_certification.py.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_c180.json"

S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [S1, S2, S3]


# ---------------------------------------------------------------------------
# Quaternion left/right multiplication, as 4x4 matrices on (x0,x1,x2,x3)
# ---------------------------------------------------------------------------
def quaternion_mult_matrices() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Returns (L, R): L[a] x = components of (e_a * q), R[a] x = (q * e_a),
    for e_1,e_2,e_3 = i,j,k. Derived by hand from i^2=j^2=k^2=-1, ij=k,
    jk=i, ki=j; each row is verified antisymmetric below."""
    # e_a * q
    L1 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=float)
    L2 = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]], dtype=float)
    L3 = np.array([[0, 0, 0, -1], [0, 0, -1, 0], [0, 1, 0, 0], [1, 0, 0, 0]], dtype=float)
    # q * e_a
    R1 = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]], dtype=float)
    R2 = np.array([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)
    R3 = np.array([[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0]], dtype=float)
    return [L1, L2, L3], [R1, R2, R3]


def structural_controls(L: list[np.ndarray], R: list[np.ndarray]) -> dict:
    """su(2) + su(2) closure, [L,R]=0, antisymmetry, and that L,R together
    span the same so(4) as the coordinate rotations x_mu d_nu - x_nu d_mu."""

    def comm(A, B):
        return A @ B - B @ A

    eps = np.zeros((3, 3, 3))
    for a, b, c in itertools.permutations(range(3)):
        sign = np.sign(np.linalg.det(np.eye(3)[[a, b, c]]))
        eps[a, b, c] = sign

    antisym = max(float(np.max(np.abs(M + M.T))) for M in L + R)

    l_closure = 0.0
    r_closure = 0.0
    for a in range(3):
        for b in range(3):
            target_l = 2.0 * sum(eps[a, b, c] * L[c] for c in range(3))
            target_r = -2.0 * sum(eps[a, b, c] * R[c] for c in range(3))
            l_closure = max(l_closure, float(np.max(np.abs(comm(L[a], L[b]) - target_l))))
            r_closure = max(r_closure, float(np.max(np.abs(comm(R[a], R[b]) - target_r))))

    lr_commute = max(float(np.max(np.abs(comm(L[a], R[b])))) for a in range(3) for b in range(3))

    # span check: the 6 fields must span the same space as the 6 coordinate
    # rotations E_munu (antisymmetric 4x4 matrices)
    def flat(M):
        return M.reshape(-1)

    basis_LR = np.array([flat(M) for M in L + R])
    rotations = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            E = np.zeros((4, 4))
            E[mu, nu], E[nu, mu] = 1.0, -1.0
            rotations.append(flat(E))
    rotations = np.array(rotations)
    rank_LR = int(np.linalg.matrix_rank(basis_LR, tol=1e-10))
    rank_joint = int(np.linalg.matrix_rank(np.vstack([basis_LR, rotations]), tol=1e-10))

    return {
        "max_antisymmetry_residual": antisym,
        "su2_L_closure_residual": l_closure,
        "su2_R_closure_residual": r_closure,
        "L_R_commute_residual": lr_commute,
        "rank_of_LR_span": rank_LR,
        "rank_of_LR_plus_coordinate_rotations": rank_joint,
        "LR_spans_so4": rank_LR == 6 and rank_joint == 6,
        "ok": (
            antisym < 1e-12
            and l_closure < 1e-12
            and r_closure < 1e-12
            and lr_commute < 1e-12
            and rank_LR == 6
            and rank_joint == 6
        ),
    }


# ---------------------------------------------------------------------------
# Control (item 2): Tom's eq (77) for the S^3 VECTOR multiplet
# ---------------------------------------------------------------------------
def tom_eq77_s3_vector_control() -> dict:
    """Same test as C179's control A, now in n=3 (S^3 in R^4), which Tom's
    own notes do not carry out (his section 3 stops at S^2)."""
    X = list(sp.symbols("y0 y1 y2 y3", real=True))
    r = sp.sqrt(sum(v**2 for v in X))
    phi = [X[i] / r for i in range(4)]

    def d(a, b):
        return 1 if a == b else 0

    def T_def(i, j):
        return sp.Matrix(4, 4, lambda k, ell: -sp.I * (d(j, ell) * d(k, i) - d(i, ell) * d(k, j)))

    results = {}
    for label, gamma_fn in (
        ("his_convention_Gamma_eq_minus_T_row_contraction", lambda i, j: -T_def(i, j)),
        ("transpose_variant", lambda i, j: (-T_def(i, j)).T),
        ("sign_variant_Gamma_eq_plus_T", lambda i, j: T_def(i, j)),
    ):
        all_ok = True
        for i in range(4):
            for j in range(i + 1, 4):
                M = sp.I * gamma_fn(i, j)
                for g in range(4):
                    lhs = sp.simplify(
                        -(X[j] * sp.diff(phi[g], X[i]) - X[i] * sp.diff(phi[g], X[j]))
                    )
                    rhs = sp.simplify(sum(M[g, dd] * phi[dd] for dd in range(4)))
                    if sp.simplify(lhs - rhs) != 0:
                        all_ok = False
        results[label] = all_ok
    return {
        "per_convention_satisfied": results,
        "his_stated_convention_verifies": results[
            "his_convention_Gamma_eq_minus_T_row_contraction"
        ],
        "exactly_one_convention_works": sum(results.values()) == 1,
    }


# ---------------------------------------------------------------------------
# Harmonic polynomials on S^3 and the vector fields acting on them
# ---------------------------------------------------------------------------
def monomials(k: int) -> list[tuple[int, int, int, int]]:
    out = []
    for a in range(k + 1):
        for b in range(k + 1 - a):
            for c in range(k + 1 - a - b):
                out.append((a, b, c, k - a - b - c))
    return out


def harmonic_basis(k: int) -> np.ndarray:
    """Columns = coefficient vectors (in the degree-k monomial basis) of a
    basis of ker(Laplacian). dim must be (k+1)^2 for 4 variables."""
    mons_k = monomials(k)
    idx_k = {m: i for i, m in enumerate(mons_k)}
    if k < 2:
        return np.eye(len(mons_k))
    mons_km2 = monomials(k - 2)
    idx_km2 = {m: i for i, m in enumerate(mons_km2)}
    lap = np.zeros((len(mons_km2), len(mons_k)))
    for m, col in idx_k.items():
        for v in range(4):
            if m[v] >= 2:
                tgt = list(m)
                tgt[v] -= 2
                lap[idx_km2[tuple(tgt)], col] += m[v] * (m[v] - 1)
    _, s, vh = np.linalg.svd(lap)
    null_dim = len(mons_k) - int(np.sum(s > 1e-9))
    return vh[len(mons_k) - null_dim :].T


def vector_field_matrix(M: np.ndarray, k: int, basis: np.ndarray) -> np.ndarray:
    """Matrix of V_M = sum_mu (M x)_mu d_mu on the harmonic subspace of
    degree-k polynomials, expressed in the given basis (columns)."""
    mons_k = monomials(k)
    idx_k = {m: i for i, m in enumerate(mons_k)}
    full = np.zeros((len(mons_k), len(mons_k)))
    for m, col in idx_k.items():
        for mu in range(4):
            if m[mu] == 0:
                continue
            # d_mu applied to the monomial
            base = list(m)
            base[mu] -= 1
            coeff = m[mu]
            for nu in range(4):
                if M[mu, nu] == 0:
                    continue
                tgt = list(base)
                tgt[nu] += 1  # multiply by x_nu
                full[idx_k[tuple(tgt)], col] += coeff * M[mu, nu]
    # Restrict to the harmonic subspace. NOTE (corrected after a skeptic pass
    # flagged the original wording as misleading): the SVD basis is orthonormal
    # in COEFFICIENT space, which is NOT the L^2(S^3) inner product -- so the
    # resulting matrix is generally NOT antisymmetric, and should not be
    # expected to be. Eigenvalues are similarity invariants and are unaffected;
    # this is demonstrated explicitly by basis_independence_check().
    return basis.T @ full @ basis


def spinor_level(k: int, R: list[np.ndarray]) -> dict:
    """Build D_0 = -i sum_a sigma_a (x) X_a^R on C^2 (x) H_k, diagonalise,
    and compare the eigenvalue/multiplicity structure to the reference
    (k+1)(k+2) and k(k+1)."""
    basis = harmonic_basis(k)
    dim_h = basis.shape[1]
    Xs = [vector_field_matrix(R[a], k, basis) for a in range(3)]
    D0 = -1j * sum(np.kron(PAULI[a], Xs[a].astype(complex)) for a in range(3))

    evals = np.linalg.eigvals(D0)
    max_imag = float(np.max(np.abs(evals.imag)))
    real_evals = np.sort(evals.real)

    # cluster eigenvalues
    clusters: list[list[float]] = []
    for e in real_evals:
        if clusters and abs(e - clusters[-1][0]) < 1e-6:
            clusters[-1].append(float(e))
        else:
            clusters.append([float(e)])
    spectrum = [{"eigenvalue": round(c[0], 9), "multiplicity": len(c)} for c in clusters]

    expected = sorted([(k + 1) * (k + 2), k * (k + 1)], reverse=True)
    found = sorted([s["multiplicity"] for s in spectrum], reverse=True)
    expected_nonzero = [m for m in expected if m > 0]

    return {
        "k": k,
        "dim_H_k": dim_h,
        "dim_H_k_expected": (k + 1) ** 2,
        "dim_matches": dim_h == (k + 1) ** 2,
        "total_dim_spinor_space": 2 * dim_h,
        "max_abs_imaginary_part_of_eigenvalues": max_imag,
        "eigenvalues_real": max_imag < 1e-9,
        "spectrum": spectrum,
        "multiplicities_found": found,
        "multiplicities_expected_from_round67": expected_nonzero,
        "multiplicities_match": found == expected_nonzero,
    }


# ---------------------------------------------------------------------------
# The explicit lowest harmonics, written out
# ---------------------------------------------------------------------------
def explicit_lowest_harmonics(R: list[np.ndarray]) -> dict:
    """k=0: the two constant spinors. k=1: eigenvectors written as explicit
    C^2-valued linear polynomials in (x0,x1,x2,x3)."""
    out = {}

    out["k0"] = {
        "description": "H_0 = span{1}; C^2 (x) H_0 = the two CONSTANT spinors",
        "basis": ["(1, 0)", "(0, 1)"],
        "note": "constant sections exist precisely because S^3 is parallelizable",
    }

    k = 1
    basis = harmonic_basis(k)  # 4x4 identity: monomials x0,x1,x2,x3
    Xs = [vector_field_matrix(R[a], k, basis) for a in range(3)]
    D0 = -1j * sum(np.kron(PAULI[a], Xs[a].astype(complex)) for a in range(3))
    evals, evecs = np.linalg.eig(D0)
    order = np.argsort(evals.real)
    mons = ["x0", "x1", "x2", "x3"]
    entries = []
    for idx in order:
        lam = float(evals[idx].real)
        v = evecs[:, idx]
        v = v / np.max(np.abs(v))
        comps = []
        for spin_component in range(2):
            terms = []
            for p in range(4):
                c = v[spin_component * 4 + p]
                if abs(c) > 1e-9:
                    terms.append(f"({c.real:+.3f}{c.imag:+.3f}i)*{mons[p]}")
            comps.append(" ".join(terms) if terms else "0")
        entries.append({"eigenvalue": round(lam, 6), "spinor": comps})
    out["k1"] = {
        "description": "C^2 (x) H_1, dim 8; explicit eigen-spinors of D_0",
        "eigenspinors": entries,
    }
    return out


# ---------------------------------------------------------------------------
# Added after an independent skeptic pass raised two specific concerns.
# ---------------------------------------------------------------------------
def chirality_discrimination_check(L: list[np.ndarray], R: list[np.ndarray]) -> dict:
    """SKEPTIC CONCERN (Attack 2): the multiplicity pattern (k+1)(k+2)/k(k+1)
    is forced by ANY su(2) generator set with the right algebra, so it does
    NOT distinguish the right-invariant fields X^R (which the construction
    requires) from the left-invariant X^L. Correct, and the round did not
    run it as a control.

    Resolution, computed here: run the SAME connection-constant derivation on
    an X^L-built operator. If the constant comes out with the OPPOSITE sign,
    then the constant -- unlike the multiplicities -- does discriminate, and
    the round's stronger check was never vacuous."""
    out = {}
    for label, fields in (("X_R", R), ("X_L", L)):
        levels_here = [spinor_level(k, fields) for k in (0, 1, 2, 3)]
        const = connection_constant_check(levels_here)
        out[label] = {
            "spectra": {str(lv["k"]): lv["spectrum"] for lv in levels_here},
            "multiplicities": {str(lv["k"]): lv["multiplicities_found"] for lv in levels_here},
            "solved_constant": const["solved_connection_constant"],
            "constant_is_unique": const["constant_is_unique"],
        }
    same_mult = out["X_R"]["multiplicities"] == out["X_L"]["multiplicities"]
    c_r, c_l = out["X_R"]["solved_constant"], out["X_L"]["solved_constant"]
    differ = c_r is not None and c_l is not None and abs(c_r - c_l) > 1e-9
    return {
        "per_chirality": out,
        "multiplicities_identical_across_chiralities": bool(same_mult),
        "multiplicity_check_does_NOT_discriminate": bool(same_mult),
        "constants": {"X_R": c_r, "X_L": c_l},
        "constant_check_DOES_discriminate": bool(differ),
        "constants_are_opposite_sign": bool(
            differ and c_r is not None and c_l is not None and abs(c_r + c_l) < 1e-9
        ),
    }


def basis_independence_check(R: list[np.ndarray], k: int = 2) -> dict:
    """SKEPTIC CONCERN (unrequested finding): the raw operator matrix is not
    antisymmetric in the monomial-coefficient basis, because that basis is
    NOT orthonormal for the L^2(S^3) inner product (the code comment claiming
    'orthonormal from SVD' referred only to orthonormality in coefficient
    space -- misleading, corrected here). Eigenvalues are similarity
    invariants, so the fix is to demonstrate that directly: recompute the
    spectrum in a RANDOM basis of the same harmonic subspace and compare."""
    basis = harmonic_basis(k)
    dim_h = basis.shape[1]
    mons_k = monomials(k)
    idx_k = {m: i for i, m in enumerate(mons_k)}

    def full_matrix(M: np.ndarray) -> np.ndarray:
        full = np.zeros((len(mons_k), len(mons_k)))
        for m, col in idx_k.items():
            for mu in range(4):
                if m[mu] == 0:
                    continue
                base = list(m)
                base[mu] -= 1
                coeff = m[mu]
                for nu in range(4):
                    if M[mu, nu] == 0:
                        continue
                    tgt = list(base)
                    tgt[nu] += 1
                    full[idx_k[tuple(tgt)], col] += coeff * M[mu, nu]
        return full

    def spectrum(b: np.ndarray) -> np.ndarray:
        # NOTE (second self-caught bug, recorded in decision.md): the first
        # draft called vector_field_matrix(), which restricts via b.T @ full @ b.
        # That is only a SIMILARITY transform when b is orthonormal; for a
        # general b it is a CONGRUENCE, which does not preserve eigenvalues --
        # so the first version of this very test reported a spurious failure of
        # basis independence. The general restriction needs the pseudo-inverse.
        proj = np.linalg.pinv(b)
        Xs = [proj @ full_matrix(R[a]) @ b for a in range(3)]
        D = -1j * sum(np.kron(PAULI[a], Xs[a].astype(complex)) for a in range(3))
        return np.sort(np.linalg.eigvals(D).real)

    ev_orig = spectrum(basis)
    rng = np.random.default_rng(4242)
    mix = rng.normal(size=(dim_h, dim_h))
    scrambled = basis @ mix  # same subspace, deliberately non-orthonormal basis
    ev_scrambled = spectrum(scrambled)
    max_diff = float(np.max(np.abs(ev_orig - ev_scrambled)))
    # sanity: the scrambling must actually be non-trivial, else the test is void
    non_orthonormality = float(np.max(np.abs(scrambled.T @ scrambled - np.eye(dim_h))))
    return {
        "level_k": k,
        "scrambled_basis_non_orthonormality": non_orthonormality,
        "scrambling_is_nontrivial": bool(non_orthonormality > 0.1),
        "max_eigenvalue_difference_under_random_change_of_basis": max_diff,
        "spectrum_is_basis_independent": bool(max_diff < 1e-8),
        "note": (
            "confirms the non-antisymmetry of the raw matrix in the monomial "
            "basis is a basis artefact, not a defect in the operator"
        ),
    }


def connection_constant_check(levels: list[dict]) -> dict:
    """D_0 as built carries NO spin-connection constant. round67's physical
    S^3 Dirac spectrum is +-(n+3/2) with multiplicity (n+1)(n+2) for BOTH
    signs. Ask: is there a single additive constant c such that D_0 - c has
    exactly that spectrum? c is SOLVED FOR from the data, not assumed --
    if it comes out 3/2 that is the standard connection term arriving on its
    own, which is a much stronger check than matching multiplicities alone."""
    # collect (eigenvalue, multiplicity) across all computed levels
    pairs = []
    for lv in levels:
        for s in lv["spectrum"]:
            pairs.append((float(s["eigenvalue"]), int(s["multiplicity"])))

    # METHOD (first draft used (max+min)/2, which is WRONG -- the extreme
    # eigenvalues across different levels do not pair with each other; that
    # bug was self-caught on the first run and is recorded in decision.md).
    # Correct method: round67 says multiplicity (n+1)(n+2) determines n, and
    # the magnitude must then be n+3/2. Each (eigenvalue, multiplicity) pair
    # therefore admits exactly TWO candidate constants, c = val -+ (n+3/2).
    # The true c must lie in the INTERSECTION over all pairs.
    def n_from_multiplicity(mult: int) -> int | None:
        n = 0
        while (n + 1) * (n + 2) <= mult:
            if (n + 1) * (n + 2) == mult:
                return n
            n += 1
        return None

    per_pair = []
    candidate_sets = []
    for val, mult in pairs:
        n = n_from_multiplicity(mult)
        if n is None:
            per_pair.append({"eigenvalue": val, "multiplicity": mult, "n": None})
            candidate_sets.append(set())
            continue
        mag = n + 1.5
        cands = {round(val - mag, 9), round(val + mag, 9)}
        per_pair.append(
            {
                "eigenvalue": val,
                "multiplicity": mult,
                "n_from_multiplicity": n,
                "required_magnitude": mag,
                "candidate_constants": sorted(cands),
            }
        )
        candidate_sets.append(cands)

    intersection = set.intersection(*candidate_sets) if candidate_sets else set()
    unique = len(intersection) == 1
    c_solved = next(iter(intersection)) if unique else None

    return {
        "method": "intersect per-pair candidate constants c = eigenvalue -+ (n+3/2)",
        "per_pair_analysis": per_pair,
        "intersection_of_candidates": sorted(intersection),
        "constant_is_unique": unique,
        "solved_connection_constant": c_solved,
        "equals_three_halves": bool(unique and abs(c_solved - 1.5) < 1e-9),
        "constant_was_solved_not_assumed": True,
        "full_spectrum_matches_round67": bool(
            unique
            and abs(c_solved - 1.5) < 1e-9
            and all(p.get("n_from_multiplicity") is not None for p in per_pair)
        ),
    }


def main() -> dict:
    result: dict = {}
    L, R = quaternion_mult_matrices()

    result["structural_controls"] = structural_controls(L, R)
    result["control_item2_tom_eq77_S3_vector"] = tom_eq77_s3_vector_control()

    levels = [spinor_level(k, R) for k in (0, 1, 2, 3)]
    result["spinor_levels"] = levels
    result["connection_constant_check"] = connection_constant_check(levels)
    result["skeptic_followup_chirality_discrimination"] = chirality_discrimination_check(L, R)
    result["skeptic_followup_basis_independence"] = basis_independence_check(R)
    result["explicit_lowest_harmonics"] = explicit_lowest_harmonics(R)

    substrate_ok = result["structural_controls"]["ok"] and all(
        lv["dim_matches"] and lv["eigenvalues_real"] for lv in levels
    )
    vector_ok = result["control_item2_tom_eq77_S3_vector"]["exactly_one_convention_works"]
    spinor_ok = all(lv["multiplicities_match"] for lv in levels)
    spectrum_ok = (
        result["connection_constant_check"]["equals_three_halves"]
        and result["connection_constant_check"]["full_spectrum_matches_round67"]
    )

    if not substrate_ok:
        label = "SUBSTRATE-MISMATCH"
    elif not vector_ok:
        label = "VECTOR-FAILS"
    elif not spinor_ok:
        label = "VECTOR-OK-SPINOR-FAILS"
    else:
        label = "BOTH-CONFIRMED" + ("-PLUS-CONNECTION-CONSTANT" if spectrum_ok else "")

    result["verdict"] = {
        "label": label,
        "substrate_ok": substrate_ok,
        "eq77_S3_vector_ok": vector_ok,
        "spinor_multiplicities_reproduce_round67": spinor_ok,
        "connection_constant_emerges_as_three_halves": spectrum_ok,
    }
    return result


if __name__ == "__main__":
    out = main()
    print(json.dumps(out["verdict"], indent=2))
    RESULTS_PATH.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\nSaved: {RESULTS_PATH}")
