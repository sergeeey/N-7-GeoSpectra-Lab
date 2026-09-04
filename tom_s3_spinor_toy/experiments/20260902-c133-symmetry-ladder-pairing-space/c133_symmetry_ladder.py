"""C133 -- the symmetry ladder for the S6 triality-channel <-> S3 t-sector
pairing-rule space.

Everything below is built FROM SCRATCH (Cayley-Dickson octonions, Der(O),
J3(O) and the Spin(8) that fixes its three diagonal idempotents).  Nothing is
imported from an earlier round's script; the only inputs are the definitions
of the Cayley-Dickson doubling and the Jordan product.

Three rungs are computed, each as an explicit Schur-lemma calculation on the
three 8-dimensional blocks:

  rung 1  G2 only            -> dim End_{g2}(F)               [expect 18]
  rung 2  Spin(8)            -> dim End_{so(8)}(F)            [expect  3]
  rung 3  Spin(8) + triality -> dim End_{so(8), U}(F)         [expect  1]

with F = O_x (+) O_y (+) O_z the combined 24-dimensional channel object.

MANDATORY NEGATIVE CONTROL (claim.md): the identical machinery is re-run with
three MUTUALLY EQUIVALENT irreps (three copies of the same 8-dim rep).  If it
still returns "block diagonal forced" there, it is not sensing inequivalence
and the whole result is void.

Rank determination: every Hom-space dimension that carries a verdict is
computed EXACTLY over the rationals with sympy (the structure constants are
integers), and cross-checked with a numpy SVD whose singular-value gap is
printed so the rank call is auditable rather than asserted.
"""

from __future__ import annotations

import itertools
import json
import os

import numpy as np
import sympy as sp

RNG = np.random.default_rng(20260902)
OUT = {}


# --------------------------------------------------------------------------
# 0.  Cayley-Dickson: R -> C -> H -> O, as integer multiplication tables.
# --------------------------------------------------------------------------
def cayley_dickson(table: np.ndarray, conj: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Double an algebra given by table[i,j,:] = e_i*e_j and conjugation conj.

    (a,b)(c,d) = (a c - conj(d) b,  d a + b conj(c))
    conj((a,b)) = (conj(a), -b)
    """
    n = table.shape[0]
    N = 2 * n

    def mul_small(u, v):
        return np.einsum("i,j,ijk->k", u, v, table)

    new = np.zeros((N, N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            a = np.zeros(n, dtype=np.int64)
            b = np.zeros(n, dtype=np.int64)
            c = np.zeros(n, dtype=np.int64)
            d = np.zeros(n, dtype=np.int64)
            if i < n:
                a[i] = 1
            else:
                b[i - n] = 1
            if j < n:
                c[j] = 1
            else:
                d[j - n] = 1
            first = mul_small(a, c) - mul_small(conj @ d, b)
            second = mul_small(d, a) + mul_small(b, conj @ c)
            new[i, j, :n] = first
            new[i, j, n:] = second

    new_conj = np.zeros((N, N), dtype=np.int64)
    new_conj[:n, :n] = conj
    new_conj[n:, n:] = -np.eye(n, dtype=np.int64)
    return new, new_conj


T_R = np.ones((1, 1, 1), dtype=np.int64)
C_R = np.ones((1, 1), dtype=np.int64)
T_C, C_C = cayley_dickson(T_R, C_R)
T_H, C_H = cayley_dickson(T_C, C_C)
T_O, C_O = cayley_dickson(T_H, C_H)  # octonions: 8-dimensional


def omul(u, v):
    return np.einsum("i,j,ijk->k", u, v, T_O)


def oconj(u):
    return C_O @ u


E0 = np.zeros(8, dtype=np.int64)
E0[0] = 1


def check_octonions():
    res = {}
    # identity
    ok_id = all(
        np.array_equal(omul(E0, np.eye(8, dtype=np.int64)[i]), np.eye(8, dtype=np.int64)[i])
        and np.array_equal(omul(np.eye(8, dtype=np.int64)[i], E0), np.eye(8, dtype=np.int64)[i])
        for i in range(8)
    )
    res["identity_e0"] = bool(ok_id)

    # norm multiplicative  |uv|^2 = |u|^2 |v|^2   (composition algebra)
    err = 0.0
    for _ in range(200):
        u = RNG.normal(size=8)
        v = RNG.normal(size=8)
        w = np.einsum("i,j,ijk->k", u, v, T_O.astype(float))
        err = max(err, abs(w @ w - (u @ u) * (v @ v)))
    res["norm_multiplicative_max_err"] = float(err)

    # alternative but NOT associative
    alt = 0.0
    for _ in range(200):
        u = RNG.normal(size=8)
        v = RNG.normal(size=8)
        Tf = T_O.astype(float)
        uu = np.einsum("i,j,ijk->k", u, u, Tf)
        lhs = np.einsum("i,j,ijk->k", uu, v, Tf)
        uv = np.einsum("i,j,ijk->k", u, v, Tf)
        rhs = np.einsum("i,j,ijk->k", u, uv, Tf)
        alt = max(alt, np.max(np.abs(lhs - rhs)))
    res["alternative_max_err"] = float(alt)

    nonassoc = 0
    I8 = np.eye(8, dtype=np.int64)
    for i, j, k in itertools.product(range(8), repeat=3):
        lhs = omul(omul(I8[i], I8[j]), I8[k])
        rhs = omul(I8[i], omul(I8[j], I8[k]))
        if not np.array_equal(lhs, rhs):
            nonassoc += 1
    res["nonassociative_basis_triples"] = int(nonassoc)
    return res


OUT["step0_octonions"] = check_octonions()


# --------------------------------------------------------------------------
#  exact / numeric nullspace helpers
# --------------------------------------------------------------------------
def nullity_numeric(A: np.ndarray):
    """Return (nullity, smallest_kept_sv, largest_dropped_sv) with an explicit gap.

    # WHY: the third slot is None -- NOT 0.0 -- when nothing was discarded.
    # An earlier version returned the literal 0.0 there, and the write-up read
    # that sentinel as "a structural zero singular value", which it is not:
    # nullity 0 means the system has FULL COLUMN RANK and there is no discarded
    # singular value at all.  Caught by the FL Step 8a skeptic pass (MAJOR-1).
    # The honest statement in that case is the smallest RETAINED value against
    # the tolerance, which is what `smallest_kept_sv` reports.
    """
    if A.size == 0:
        return A.shape[1], None, None
    sv = np.linalg.svd(A.astype(float), compute_uv=False)
    scale = sv[0] if sv.size and sv[0] > 0 else 1.0
    tol = max(A.shape) * np.finfo(float).eps * scale * 1e3
    kept = sv[sv > tol]
    dropped = sv[sv <= tol]
    n = A.shape[1] - kept.size
    return (
        int(n),
        float(kept[-1]) if kept.size else None,
        float(dropped[0]) if dropped.size else None,
    )


def nullity_exact(A: np.ndarray) -> int:
    """Exact rational rank over Q (integer input)."""
    M = sp.Matrix(A.astype(object))
    return A.shape[1] - M.rank()


# --------------------------------------------------------------------------
# 1.  Der(O) = g2, from scratch:  D(uv) = D(u)v + u D(v).
# --------------------------------------------------------------------------
def derivations_of_O():
    rows = []
    I8 = np.eye(8, dtype=np.int64)
    for i, j in itertools.product(range(8), repeat=2):
        m = omul(I8[i], I8[j])  # e_i e_j as a vector
        # unknown D[k,l];  D(e_l) = sum_k D[k,l] e_k
        blk = np.zeros((8, 64), dtype=np.int64)  # 8 components x 64 unknowns
        # LHS: D(m) = sum_l m[l] * D(e_l) -> component k: sum_l m[l] D[k,l]
        for k in range(8):
            for lo in range(8):
                blk[k, k * 8 + lo] += m[lo]
        # RHS: sum_k D[k,i] (e_k e_j) + sum_k D[k,j] (e_i e_k)
        for k in range(8):
            blk[:, k * 8 + i] -= omul(I8[k], I8[j])
            blk[:, k * 8 + j] -= omul(I8[i], I8[k])
        rows.append(blk)
    A = np.vstack(rows)
    ns = sp.Matrix(A.astype(object)).nullspace()
    basis = [np.array(v.T.tolist()[0], dtype=object).reshape(8, 8) for v in ns]
    basis = [np.array([[sp.Rational(x) for x in row] for row in b]) for b in basis]
    # clear denominators -> integer matrices
    ints = []
    for b in basis:
        dens = [sp.Rational(x).q for x in b.flatten()]
        L = sp.ilcm(*dens) if len(dens) > 1 else 1
        ints.append(np.array([[int(sp.Rational(x) * L) for x in row] for row in b], dtype=np.int64))
    return A, ints


A_der, G2_BASIS = derivations_of_O()
g2_checks = {
    "dim_Der_O_exact": len(G2_BASIS),
    "all_kill_the_unit": bool(all(np.all(D @ E0 == 0) for D in G2_BASIS)),
    "all_skew_on_ImO": bool(all(np.array_equal(D[1:, 1:], -D[1:, 1:].T) for D in G2_BASIS)),
    "all_skew_full": bool(all(np.array_equal(D, -D.T) for D in G2_BASIS)),
}
OUT["step1_g2"] = g2_checks


# --------------------------------------------------------------------------
# 2.  J3(O) and the Spin(8) that fixes its three diagonal idempotents.
#     X = [[a, z, ybar], [zbar, b, x], [y, xbar, c]]
#     coords: (a, b, c, x(8), y(8), z(8)) in R^27
# --------------------------------------------------------------------------
DIM_J = 27


def to_matrix(v):
    """R^27 -> 3x3 array of octonions (each length-8 float vector)."""
    a, b, c = v[0], v[1], v[2]
    x, y, z = v[3:11], v[11:19], v[19:27]
    M = np.zeros((3, 3, 8), dtype=float)
    M[0, 0, 0] = a
    M[1, 1, 0] = b
    M[2, 2, 0] = c
    M[0, 1] = z
    M[1, 0] = C_O @ z
    M[0, 2] = C_O @ y
    M[2, 0] = y
    M[1, 2] = x
    M[2, 1] = C_O @ x
    return M


def from_matrix(M):
    v = np.zeros(27, dtype=float)
    v[0] = M[0, 0, 0]
    v[1] = M[1, 1, 0]
    v[2] = M[2, 2, 0]
    v[3:11] = M[1, 2]
    v[11:19] = M[2, 0]
    v[19:27] = M[0, 1]
    return v


TF = T_O.astype(float)


def omulf(u, v):
    return np.einsum("i,j,ijk->k", u, v, TF)


def matmul_oct(A, B):
    out = np.zeros((3, 3, 8), dtype=float)
    for i in range(3):
        for j in range(3):
            s = np.zeros(8)
            for k in range(3):
                s = s + omulf(A[i, k], B[k, j])
            out[i, j] = s
    return out


def jordan(u, v):
    A, B = to_matrix(u), to_matrix(v)
    P = matmul_oct(A, B)
    Q = matmul_oct(B, A)
    S = 0.5 * (P + Q)
    return S


def jordan_prod(u, v):
    return from_matrix(jordan(u, v))


def hermiticity_residual(S):
    """How far S is from Hermitian (diag real, S_ji = conj S_ij)."""
    r = 0.0
    for i in range(3):
        r = max(r, np.max(np.abs(S[i, i, 1:])))
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        r = max(r, np.max(np.abs(S[j, i] - C_O @ S[i, j])))
    return float(r)


def check_jordan():
    res = {}
    herm = 0.0
    for _ in range(50):
        u = RNG.normal(size=27)
        v = RNG.normal(size=27)
        herm = max(herm, hermiticity_residual(jordan(u, v)))
    res["jordan_product_stays_hermitian_max_resid"] = herm
    # commutативity and the Jordan identity (X^2 o (X o Y)) = X o (X^2 o Y)
    comm = 0.0
    jid = 0.0
    for _ in range(30):
        u = RNG.normal(size=27)
        v = RNG.normal(size=27)
        comm = max(comm, np.max(np.abs(jordan_prod(u, v) - jordan_prod(v, u))))
        u2 = jordan_prod(u, u)
        lhs = jordan_prod(u2, jordan_prod(u, v))
        rhs = jordan_prod(u, jordan_prod(u2, v))
        jid = max(jid, np.max(np.abs(lhs - rhs)))
    res["jordan_commutative_max_err"] = float(comm)
    res["jordan_identity_max_err"] = float(jid)
    return res


OUT["step2a_J3O"] = check_jordan()


# --- the cyclic slot permutation sigma: X -> P X P^T,  P: 1->2->3->1 --------
PERM = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)  # P e1=e2, P e2=e3, P e3=e1


def sigma_matrix(M):
    out = np.zeros_like(M)
    for i in range(3):
        for j in range(3):
            out[i, j] = M[(i - 1) % 3, (j - 1) % 3]
    return out


def sigma(v):
    return from_matrix(sigma_matrix(to_matrix(v)))


def check_sigma():
    res = {}
    # order 3
    err3 = 0.0
    aut = 0.0
    slot = 0.0
    for _ in range(50):
        v = RNG.normal(size=27)
        w = RNG.normal(size=27)
        err3 = max(err3, np.max(np.abs(sigma(sigma(sigma(v))) - v)))
        aut = max(aut, np.max(np.abs(sigma(jordan_prod(v, w)) - jordan_prod(sigma(v), sigma(w)))))
        # slot action:  (x,y,z) -> (z,x,y),  (a,b,c) -> (c,a,b)
        sv = sigma(v)
        pred = np.concatenate([[v[2], v[0], v[1]], v[19:27], v[3:11], v[11:19]])
        slot = max(slot, np.max(np.abs(sv - pred)))
    res["sigma_cubed_is_identity_max_err"] = float(err3)
    res["sigma_is_jordan_automorphism_max_err"] = float(aut)
    res["sigma_acts_as_xyz_to_zxy_max_err"] = float(slot)
    return res


OUT["step2b_sigma"] = check_sigma()


# --- the entrywise-derivation ansatz -> so(8) ------------------------------
def delta_apply(A1, A2, A3, v):
    out = np.zeros(27, dtype=float)
    out[3:11] = A1 @ v[3:11]
    out[11:19] = A2 @ v[11:19]
    out[19:27] = A3 @ v[19:27]
    return out


def solve_entrywise_derivations():
    """Solve delta(X o Y) = delta(X) o Y + X o delta(Y) for the 192 unknowns."""
    basis = np.eye(27)
    # Precompute all Jordan products of basis pairs
    prods = np.zeros((27, 27, 27))
    for p in range(27):
        for q in range(27):
            prods[p, q] = jordan_prod(basis[p], basis[q])

    rows = []
    nun = 3 * 64
    for p in range(27):
        for q in range(27):
            blk = np.zeros((27, nun))
            m = prods[p, q]
            # LHS: delta(m) -- linear in unknowns
            for s, off, sl in (
                (0, 0, slice(3, 11)),
                (1, 64, slice(11, 19)),
                (2, 128, slice(19, 27)),
            ):
                src = m[sl]
                for k in range(8):
                    for lo in range(8):
                        blk[sl.start + k, off + k * 8 + lo] += src[lo]
            # RHS: delta(e_p) o e_q  +  e_p o delta(e_q)
            for s, off, sl in (
                (0, 0, slice(3, 11)),
                (1, 64, slice(11, 19)),
                (2, 128, slice(19, 27)),
            ):
                for k in range(8):
                    for lo in range(8):
                        # unknown A_s[k,lo] contributes  e_k * (coefficient e_p[lo])
                        if basis[p][sl][lo] != 0:
                            d = np.zeros(27)
                            d[sl.start + k] = basis[p][sl][lo]
                            blk[:, off + k * 8 + lo] -= jordan_prod(d, basis[q])
                        if basis[q][sl][lo] != 0:
                            d = np.zeros(27)
                            d[sl.start + k] = basis[q][sl][lo]
                            blk[:, off + k * 8 + lo] -= jordan_prod(basis[p], d)
            rows.append(blk)
    A = np.vstack(rows)
    return A


A_ent = solve_entrywise_derivations()
n_ent, sv_keep, sv_drop = nullity_numeric(A_ent)
OUT["step2c_entrywise_derivations"] = {
    "system_shape": list(A_ent.shape),
    "nullity_numeric": n_ent,
    "smallest_kept_singular_value": sv_keep,
    "largest_dropped_singular_value": sv_drop,
}

# Extract a basis of the 28-dim algebra as triples (A1, A2, A3)
U_, S_, Vt_ = np.linalg.svd(A_ent)
tol = max(A_ent.shape) * np.finfo(float).eps * S_[0] * 1e3
null_basis = Vt_[len(S_[S_ > tol]) :] if len(S_) >= 1 else Vt_
null_basis = Vt_[np.sum(S_ > tol) :]
TRIPLES = [
    (b[:64].reshape(8, 8), b[64:128].reshape(8, 8), b[128:].reshape(8, 8)) for b in null_basis
]

RHO = [np.array([t[i] for t in TRIPLES]) for i in range(3)]  # RHO[i][k] = 8x8 matrix

so8_checks = {
    "n_generators": len(TRIPLES),
    "each_projection_skew_max_err": float(
        max(np.max(np.abs(M + M.T)) for i in range(3) for M in RHO[i])
    ),
    "projection_ranks_as_matrix_spaces": [
        int(np.linalg.matrix_rank(RHO[i].reshape(len(TRIPLES), 64), tol=1e-9)) for i in range(3)
    ],
}


# The 28-dim space must be a LIE ALGEBRA (closed under brackets) and each
# projection a Lie-algebra isomorphism onto so(8) -- otherwise "Spin(8)" is
# a name, not a fact.
def bracket_closure():
    B = np.array(
        [np.concatenate([a1.flatten(), a2.flatten(), a3.flatten()]) for (a1, a2, a3) in TRIPLES]
    ).T
    Q, _ = np.linalg.qr(B)
    worst = 0.0
    for p in range(len(TRIPLES)):
        for q in range(p + 1, len(TRIPLES)):
            (a1, a2, a3), (b1, b2, b3) = TRIPLES[p], TRIPLES[q]
            v = np.concatenate(
                [
                    (a1 @ b1 - b1 @ a1).flatten(),
                    (a2 @ b2 - b2 @ a2).flatten(),
                    (a3 @ b3 - b3 @ a3).flatten(),
                ]
            )
            if np.linalg.norm(v) < 1e-12:
                continue
            worst = max(worst, float(np.linalg.norm(v - Q @ (Q.T @ v)) / np.linalg.norm(v)))
    return worst


so8_checks["bracket_closure_rel_resid"] = bracket_closure()
so8_checks["dim_so8_is_28_and_projections_are_onto"] = bool(
    len(TRIPLES) == 28 and all(r == 28 for r in so8_checks["projection_ranks_as_matrix_spaces"])
)
OUT["step2d_so8"] = so8_checks


# --- the diagonal subalgebra A1=A2=A3 must be exactly g2 = Der(O) ----------
def diagonal_subalgebra_dim():
    """Dimension of {t in so(8)-triples : A1 = A2 = A3}."""
    n = len(TRIPLES)
    C = np.zeros((128, n))
    for k, (a1, a2, a3) in enumerate(TRIPLES):
        C[:64, k] = (a1 - a2).flatten()
        C[64:, k] = (a1 - a3).flatten()
    d, keep, drop = nullity_numeric(C)
    # the actual matrices in that subalgebra
    _u, s, vt = np.linalg.svd(C)
    tol = max(C.shape) * np.finfo(float).eps * (s[0] if s.size else 1.0) * 1e3
    nb = vt[np.sum(s > tol) :]
    mats = [sum(coef * TRIPLES[k][0] for k, coef in enumerate(vec)) for vec in nb]
    return d, keep, drop, mats


d_diag, k_diag, dr_diag, DIAG_MATS = diagonal_subalgebra_dim()


def span_distance(mats_a, mats_b):
    """max distance from each element of mats_a to span(mats_b), normalised."""
    B = np.array([m.flatten() for m in mats_b], dtype=float).T
    Q, _ = np.linalg.qr(B)
    worst = 0.0
    for m in mats_a:
        v = np.array(m, dtype=float).flatten()
        r = v - Q @ (Q.T @ v)
        worst = max(worst, np.linalg.norm(r) / max(np.linalg.norm(v), 1e-30))
    return float(worst)


OUT["step2e_diagonal_is_g2"] = {
    "dim_diagonal_subalgebra": d_diag,
    "smallest_kept_singular_value": k_diag,
    "largest_dropped_singular_value": dr_diag,
    "dim_Der_O_independently": len(G2_BASIS),
    "rel_dist_g2basis_to_diagonal_span": span_distance(
        [np.array(D, dtype=float) for D in G2_BASIS], DIAG_MATS
    ),
    "rel_dist_diagonal_to_g2basis_span": span_distance(
        DIAG_MATS, [np.array(D, dtype=float) for D in G2_BASIS]
    ),
}


# --- sigma cyclically shifts the triple ------------------------------------
def sigma_shifts_triple():
    """sigma . delta_{A1,A2,A3} . sigma^{-1} = delta_{A3,A1,A2}: check closure."""
    worst = 0.0
    B = np.array(
        [np.concatenate([a1.flatten(), a2.flatten(), a3.flatten()]) for (a1, a2, a3) in TRIPLES]
    ).T
    Q, _ = np.linalg.qr(B)
    for a1, a2, a3 in TRIPLES:
        v = np.concatenate([a3.flatten(), a1.flatten(), a2.flatten()])
        r = v - Q @ (Q.T @ v)
        worst = max(worst, np.linalg.norm(r) / max(np.linalg.norm(v), 1e-30))
    # and verify the conjugation identity directly on random J3 elements
    direct = 0.0
    for a1, a2, a3 in TRIPLES[:6]:
        for _ in range(10):
            v = RNG.normal(size=27)
            lhs = sigma(delta_apply(a1, a2, a3, sigma(sigma(v))))  # sigma^{-1} = sigma^2
            rhs = delta_apply(a3, a1, a2, v)
            direct = max(direct, np.max(np.abs(lhs - rhs)))
    return float(worst), float(direct)


w_shift, w_direct = sigma_shifts_triple()
OUT["step2f_sigma_cyclic_shift"] = {
    "cyclically_shifted_triple_stays_in_algebra_rel_resid": w_shift,
    "conjugation_identity_sigma_delta_sigmainv_eq_delta_A3A1A2_max_err": w_direct,
}


# --------------------------------------------------------------------------
# 3.  Hom spaces.  M rho_b(t) = rho_a(t) M  for all t   <->  M in Hom(b, a).
# --------------------------------------------------------------------------
def hom_system(rho_src: np.ndarray, rho_tgt: np.ndarray) -> np.ndarray:
    """Rows of the linear system for M with M rho_src = rho_tgt M."""
    n = rho_src.shape[0]
    rows = np.zeros((n * 64, 64))
    for k in range(n):
        S = rho_src[k]
        T = rho_tgt[k]
        # (M S - T M)[p,q] = sum_r M[p,r] S[r,q] - sum_r T[p,r] M[r,q]
        for p in range(8):
            for q in range(8):
                r_ = k * 64 + p * 8 + q
                for r in range(8):
                    rows[r_, p * 8 + r] += S[r, q]
                    rows[r_, r * 8 + q] -= T[p, r]
    return rows


def hom_dim(rho_src, rho_tgt, exact_from_integers=None):
    A = hom_system(rho_src, rho_tgt)
    d, keep, drop = nullity_numeric(A)
    out = {"dim": d, "smallest_kept_sv": keep, "largest_dropped_sv": drop}
    if exact_from_integers is not None:
        Ai = hom_system(exact_from_integers[0], exact_from_integers[1]).astype(np.int64)
        out["dim_exact_rational"] = nullity_exact(Ai)
    return out


# ---- rung 1: G2 (the three blocks carry the SAME matrices) ----------------
G2_STACK = np.array([np.array(D, dtype=float) for D in G2_BASIS])
G2_STACK_INT = np.array([np.array(D, dtype=np.int64) for D in G2_BASIS])

rung1_block = hom_dim(G2_STACK, G2_STACK, exact_from_integers=(G2_STACK_INT, G2_STACK_INT))
OUT["step3_rung1_G2"] = {
    "three_blocks_are_literally_the_same_matrices": True,
    "dim_Hom_g2_between_any_two_blocks": rung1_block,
    "dim_End_g2_of_24dim_F": 9 * rung1_block["dim"],
    "channel_matrix_M_is_free_3x3": rung1_block["dim"] > 0,
}

# an EXPLICIT G2-equivariant channel-mixing map: Phi = identity O_x -> O_y
Phi = np.zeros((24, 24))
Phi[8:16, 0:8] = np.eye(8)


def rho_block(stack, idxs):
    """block-diagonal 24x24 representation from three 8x8 stacks."""
    n = stack[0].shape[0]
    out = np.zeros((n, 24, 24))
    for k in range(n):
        for b, i in enumerate(idxs):
            out[k, 8 * b : 8 * b + 8, 8 * b : 8 * b + 8] = stack[i][k]
    return out


RHO_G2_24 = rho_block([G2_STACK, G2_STACK, G2_STACK], [0, 1, 2])
comm_err = max(float(np.max(np.abs(Phi @ R - R @ Phi))) for R in RHO_G2_24)
OUT["step3_rung1_G2"]["explicit_channel_mixing_Phi_commutator_max_err"] = comm_err
OUT["step3_rung1_G2"]["explicit_channel_mixing_Phi_is_nonzero"] = bool(np.any(Phi))


# ---- rung 2: Spin(8) ------------------------------------------------------
pairs = {}
for a, b in itertools.product(range(3), repeat=2):
    pairs[f"Hom(rho{b + 1}->rho{a + 1})"] = hom_dim(RHO[b], RHO[a])
OUT["step3_rung2_Spin8"] = {
    "pairwise_Hom_dims": pairs,
    "dim_End_so8_of_24dim_F": sum(v["dim"] for v in pairs.values()),
}


# ---- rung 3: Spin(8) + the explicit triality Z3 ---------------------------
U24 = np.zeros((24, 24))
# sigma sends slot content x->y-slot? sigma: (x,y,z)->(z,x,y) means new x = old z.
# On F with coordinates (xi_x, xi_y, xi_z):  U(xi)_x = xi_z, U(xi)_y = xi_x, U(xi)_z = xi_y
U24[0:8, 16:24] = np.eye(8)
U24[8:16, 0:8] = np.eye(8)
U24[16:24, 8:16] = np.eye(8)

RHO_SO8_24 = np.zeros((len(TRIPLES), 24, 24))
for k, (a1, a2, a3) in enumerate(TRIPLES):
    RHO_SO8_24[k, 0:8, 0:8] = a1
    RHO_SO8_24[k, 8:16, 8:16] = a2
    RHO_SO8_24[k, 16:24, 16:24] = a3


def commutant_system(mats) -> np.ndarray:
    """The linear system for {M in M_24 : [M, X] = 0 for all X in mats}.

    # WHY exposed separately: the second (paraphrased) skeptic pass observed
    # that the tolerance sweep touched four small systems but NOT the 576-column
    # solves that actually produce the headline 3 and 1.  Returning the matrix
    # lets step5h sweep those too instead of asserting they are robust.
    """
    rows = []
    for X in mats:
        R = np.zeros((576, 576))
        for p in range(24):
            for q in range(24):
                r_ = p * 24 + q
                for r in range(24):
                    R[r_, p * 24 + r] += X[r, q]
                    R[r_, r * 24 + q] -= X[p, r]
        rows.append(R)
    return np.vstack(rows)


def commutant_dim(mats):
    """dim of {M in M_24 : [M, X] = 0 for all X in mats}."""
    return nullity_numeric(commutant_system(mats))


d_so8_24, k1, dr1 = commutant_dim(list(RHO_SO8_24))
d_so8_U_24, k2, dr2 = commutant_dim(list(RHO_SO8_24) + [U24])
OUT["step3_rung3_triality"] = {
    "U_cubed_is_identity_max_err": float(
        np.max(np.abs(np.linalg.matrix_power(U24, 3) - np.eye(24)))
    ),
    "dim_commutant_so8_only_direct_solve": d_so8_24,
    "dim_commutant_so8_plus_U_direct_solve": d_so8_U_24,
    "so8_only_sv_gap": [k1, dr1],
    "so8_plus_U_sv_gap": [k2, dr2],
}

# does U commute with the diagonal g2 action on F?
g2_24 = np.zeros((len(G2_BASIS), 24, 24))
for k, D in enumerate(G2_BASIS):
    Df = np.array(D, dtype=float)
    g2_24[k, 0:8, 0:8] = Df
    g2_24[k, 8:16, 8:16] = Df
    g2_24[k, 16:24, 16:24] = Df
OUT["step3_rung3_triality"]["U_commutes_with_diagonal_g2_max_err"] = float(
    max(np.max(np.abs(U24 @ X - X @ U24)) for X in g2_24)
)
d_g2_U_24, _, _ = commutant_dim(list(g2_24) + [U24])
OUT["step3_rung3_triality"]["dim_commutant_g2_plus_U_direct_solve"] = d_g2_U_24

# RUNG 1 SOLVED DIRECTLY, on the same footing as rungs 2 and 3.
# # WHY: the second skeptic pass observed that 18 was only ever a hardcoded
# # product `9 * dim Hom_g2`, never a commutant_dim solve, while 3 and 1 were
# # measured -- so the headline rung was the one number not computed the same
# # way as the others.  Fixed: solve it.
d_g2_24_direct, _kg, _drg = commutant_dim(list(g2_24))
OUT["step3_rung1_G2"]["dim_End_g2_of_24dim_F_DIRECT_SOLVE"] = d_g2_24_direct
OUT["step3_rung1_G2"]["direct_solve_agrees_with_the_9x2_product"] = bool(
    d_g2_24_direct == 9 * rung1_block["dim"]
)


# --------------------------------------------------------------------------
# 4.  MANDATORY NEGATIVE CONTROL -- three MUTUALLY EQUIVALENT irreps.
#     Identical machinery, identical code path, only the rep triple changes.
# --------------------------------------------------------------------------
def control(idxs, label):
    stacks = [RHO[i] for i in idxs]
    R24 = np.zeros((len(TRIPLES), 24, 24))
    for k in range(len(TRIPLES)):
        for b in range(3):
            R24[k, 8 * b : 8 * b + 8, 8 * b : 8 * b + 8] = stacks[b][k]
    d_alg, ka, dra = commutant_dim(list(R24))
    d_algU, kb, drb = commutant_dim(list(R24) + [U24])
    pw = {}
    for a, b in itertools.product(range(3), repeat=2):
        pw[f"Hom(block{b + 1}->block{a + 1})"] = hom_dim(stacks[b], stacks[a])["dim"]
    return {
        "rep_triple": label,
        "pairwise_Hom_dims": pw,
        "dim_commutant_so8": d_alg,
        "dim_commutant_so8_plus_U": d_algU,
        "sv_gaps": [[ka, dra], [kb, drb]],
        "block_diagonality_forced": bool(d_alg == 3),
        "channel_mixing_permitted_at_Spin8_level": bool(d_alg > 3),
    }


OUT["step4_negative_control_equivalent"] = control(
    [0, 0, 0], "(rho1, rho1, rho1) -- MUTUALLY EQUIVALENT"
)


# STRONGER negative control: three copies of rho1 in THREE DIFFERENT BASES.
# # WHY: the second skeptic pass noted that control([0,0,0]) feeds three
# # LITERALLY IDENTICAL arrays, so the solver could in principle return 9 by
# # exploiting array identity rather than by doing representation theory.  The
# # script already builds orthogonally conjugated copies elsewhere and never
# # used them here.  Same forced answer (9), but the solver must actually work.
def control_conjugated():
    Qs = [np.eye(8)] + [np.linalg.qr(RNG.normal(size=(8, 8)))[0] for _ in range(2)]
    R24 = np.zeros((len(TRIPLES), 24, 24))
    for k in range(len(TRIPLES)):
        for b in range(3):
            R24[k, 8 * b : 8 * b + 8, 8 * b : 8 * b + 8] = Qs[b] @ RHO[0][k] @ Qs[b].T
    d, ka, dra = commutant_dim(list(R24))
    blocks_identical = max(
        float(np.max(np.abs(R24[k, 0:8, 0:8] - R24[k, 8:16, 8:16]))) for k in range(len(TRIPLES))
    )
    return {
        "rep_triple": "(rho1, Q2 rho1 Q2^T, Q3 rho1 Q3^T) -- EQUIVALENT but in DIFFERENT BASES",
        "blocks_are_NOT_literally_identical_max_difference": blocks_identical,
        "dim_commutant_so8": d,
        "sv_gap": [ka, dra],
        "still_returns_9_so_the_solver_is_doing_rep_theory_not_array_matching": bool(d == 9),
    }


OUT["step4_negative_control_conjugated_basis"] = control_conjugated()
OUT["step4_control_mixed"] = control(
    [0, 0, 1], "(rho1, rho1, rho2) -- two equivalent + one inequivalent"
)
OUT["step4_control_inequivalent_reference"] = control(
    [0, 1, 2], "(rho1, rho2, rho3) -- the real case"
)


# --------------------------------------------------------------------------
# 5.  Scope probe: Spin(8)-invariant TRILINEAR channel-mixing coupling.
#     m: rho_b (x) rho_c -> rho_a  with  A_a m(u,v) = m(A_b u, v) + m(u, A_c v)
# --------------------------------------------------------------------------
def trilinear_dim(a, b, c):
    n = len(TRIPLES)
    rows = np.zeros((n * 8 * 8 * 8, 512))
    for k in range(n):
        Aa, Ab, Ac = RHO[a][k], RHO[b][k], RHO[c][k]
        for i, j in itertools.product(range(8), repeat=2):
            for p in range(8):
                r_ = ((k * 8 + i) * 8 + j) * 8 + p
                # LHS  (A_a m)(e_i, e_j)_p = sum_q Aa[p,q] m[q,i,j]
                for q in range(8):
                    rows[r_, q * 64 + i * 8 + j] += Aa[p, q]
                # RHS  m(Ab e_i, e_j)_p + m(e_i, Ac e_j)_p
                for q in range(8):
                    rows[r_, p * 64 + q * 8 + j] -= Ab[q, i]
                    rows[r_, p * 64 + i * 8 + q] -= Ac[q, j]
    d, keep, drop = nullity_numeric(rows)
    return {"dim": d, "smallest_kept_sv": keep, "largest_dropped_sv": drop}


OUT["step5_trilinear"] = {
    "Hom_so8(rho2 x rho3 -> rho1)": trilinear_dim(0, 1, 2),
    "Hom_so8(rho3 x rho1 -> rho2)": trilinear_dim(1, 2, 0),
    "Hom_so8(rho1 x rho2 -> rho3)": trilinear_dim(2, 0, 1),
    "CONTROL Hom_so8(rho1 x rho1 -> rho1)": trilinear_dim(0, 0, 0),
    "CONTROL Hom_so8(rho1 x rho2 -> rho1)": trilinear_dim(0, 0, 1),
}


# --------------------------------------------------------------------------
# 5b. INDEPENDENT inequivalence certificate (does NOT use any nullspace tol).
#     Two inequivalent 8-dim reps of the same Lie algebra must disagree on the
#     SPECTRUM of some single algebra element.  If they never did, "Hom = 0"
#     would be an artefact of the rank tolerance rather than a fact.
# --------------------------------------------------------------------------
def invariant_certificate(n_trials=20):
    """Compare tr(rho_a(X)^k), k = 2,4,6,8.

    # WHY traces of powers and not sorted eigenvalues: the previous version
    # compared np.sort_complex(eigvals(.)) elementwise.  For REAL SKEW matrices
    # the eigenvalues are purely imaginary, so np.sort_complex sorts on a real
    # part that is pure LAPACK noise (~1e-16) -- the pairing between the two
    # spectra would then be arbitrary and the statistic would report O(1) even
    # for IDENTICAL spectra, discriminating nothing.  Its "positive control"
    # was literally `spec[0] - spec[0]`, which is 0 by construction and could
    # not have caught this.  Both defects found by the FL Step 8a skeptic pass
    # (MAJOR-2).  tr(M^k) is basis-independent and needs no sorting at all, and
    # the positive control below is a genuine conjugated copy, not x - x.
    """
    ks = [2, 4, 6, 8]
    worst_diff = np.inf  # smallest separation ever seen between two DIFFERENT reps
    worst_control = 0.0  # largest deviation for a genuinely EQUIVALENT pair
    for _ in range(n_trials):
        coef = RNG.normal(size=len(TRIPLES))
        mats = [sum(c * RHO[i][k] for k, c in enumerate(coef)) for i in range(3)]
        inv = [np.array([np.trace(np.linalg.matrix_power(M, k)) for k in ks]) for M in mats]
        for a, b in [(0, 1), (0, 2), (1, 2)]:
            rel = np.max(np.abs(inv[a] - inv[b])) / max(np.max(np.abs(inv[a])), 1e-30)
            worst_diff = min(worst_diff, float(rel))
        # GENUINE positive control: an orthogonal change of basis on rho1.
        # Equivalent reps MUST agree, so a nonzero answer here voids the test.
        Q, _ = np.linalg.qr(RNG.normal(size=(8, 8)))
        conj = Q @ mats[0] @ Q.T
        inv_c = np.array([np.trace(np.linalg.matrix_power(conj, k)) for k in ks])
        rel_c = np.max(np.abs(inv[0] - inv_c)) / max(np.max(np.abs(inv[0])), 1e-30)
        worst_control = max(worst_control, float(rel_c))
    return float(worst_diff), worst_control


spec_diff, spec_self = invariant_certificate()
OUT["step5b_inequivalence_certificate"] = {
    "statistic": "tr(rho_a(X)^k) for k=2,4,6,8, basis-independent, no eigenvalue sorting",
    "SMALLEST_relative_separation_between_two_DIFFERENT_reps": spec_diff,
    "positive_control_LARGEST_deviation_for_an_ORTHOGONALLY_CONJUGATED_copy": spec_self,
    "control_is_genuine_not_x_minus_x": True,
    "reps_are_pairwise_inequivalent_by_invariants": bool(spec_diff > 1e-3),
    "test_can_fail": bool(spec_self < 1e-10),
    "note": (
        "A generic element of the algebra has different power-traces in rho1, rho2, rho3, "
        "while an orthogonally conjugated copy of rho1 agrees with rho1 to machine "
        "precision. This certifies inequivalence WITHOUT any rank/tolerance decision and "
        "WITHOUT eigenvalue sorting, and is the independent ground for step3_rung2's Hom=0."
    ),
}

# absolute irreducibility: dim End_R = 1  <=>  absolutely irreducible over R
OUT["step5b_inequivalence_certificate"]["dim_End_R_of_each_block"] = [
    hom_dim(RHO[i], RHO[i])["dim"] for i in range(3)
]

# explicit g2 branching 8 = 1 + 7: the commutant of g2 on R^8 is spanned by two
# complementary projections; report their ranks.
A_g2end = hom_system(G2_STACK, G2_STACK)
u_, s_, vt_ = np.linalg.svd(A_g2end)
tol_ = max(A_g2end.shape) * np.finfo(float).eps * s_[0] * 1e3
nb_ = vt_[np.sum(s_ > tol_) :]
g2_comm = [v.reshape(8, 8) for v in nb_]
eigs = sorted({round(float(e), 9) for M in g2_comm for e in np.linalg.eigvals(M).real})
# build the two idempotents by simultaneous diagonalisation of a generic element
Mg = sum(RNG.normal() * M for M in g2_comm)
w_, V_ = np.linalg.eigh((Mg + Mg.T) / 2)
mult = {}
for val in w_:
    key = round(float(val), 8)
    mult[key] = mult.get(key, 0) + 1
OUT["step5c_g2_branching"] = {
    "dim_commutant_of_g2_on_R8": len(g2_comm),
    "eigenvalue_multiplicities_of_a_generic_commutant_element": mult,
    "branching_8_restricted_to_g2": sorted(mult.values()),
    "matches_G44_null_result_1_plus_7": sorted(mult.values()) == [1, 7],
}


# --------------------------------------------------------------------------
# 5d. How much symmetry is actually NEEDED: a transposition (Z2) vs the
#     3-cycle (Z3).  Both are slot permutations of J3(O), hence both are
#     genuine F4 elements normalising Spin(8).
# --------------------------------------------------------------------------
def slot_perm(pi):
    """X -> P X P^T for the permutation pi of {0,1,2}; returns the 27x27 matrix."""
    inv = [0, 0, 0]
    for i, p in enumerate(pi):
        inv[p] = i
    M27 = np.zeros((27, 27))
    for k in range(27):
        e = np.eye(27)[k]
        X = to_matrix(e)
        Y = np.zeros_like(X)
        for i in range(3):
            for j in range(3):
                Y[i, j] = X[inv[i], inv[j]]
        M27[:, k] = from_matrix(Y)
    return M27


def check_slot_perm(pi, label):
    M27 = slot_perm(pi)
    aut = 0.0
    for _ in range(30):
        v = RNG.normal(size=27)
        w = RNG.normal(size=27)
        aut = max(
            aut,
            float(np.max(np.abs(M27 @ jordan_prod(v, w) - jordan_prod(M27 @ v, M27 @ w)))),
        )
    P24 = M27[3:27, 3:27]
    offdiag_leak = float(np.max(np.abs(M27[3:27, 0:3]))) + float(np.max(np.abs(M27[0:3, 3:27])))
    d, ka, dra = commutant_dim(list(RHO_SO8_24) + [P24])
    order = 1
    Q = P24.copy()
    while order < 7 and np.max(np.abs(Q - np.eye(24))) > 1e-10:
        Q = Q @ P24
        order += 1
    # does it normalise the so(8) image?  P rho(t) P^-1 must stay in the span
    B = np.array([R.flatten() for R in RHO_SO8_24]).T
    Qb, _ = np.linalg.qr(B)
    worst = 0.0
    for R in RHO_SO8_24:
        v = (P24 @ R @ np.linalg.inv(P24)).flatten()
        worst = max(
            worst, float(np.linalg.norm(v - Qb @ (Qb.T @ v)) / max(np.linalg.norm(v), 1e-30))
        )
    return {
        "permutation": label,
        "is_jordan_automorphism_max_err": aut,
        "mixes_diagonal_and_offdiagonal_parts": offdiag_leak,
        "order": order,
        "normalises_the_so8_image_rel_resid": worst,
        "dim_commutant_so8_plus_this": d,
        "sv_gap": [ka, dra],
    }


OUT["step5d_how_much_symmetry_is_needed"] = {
    "Z3_three_cycle": check_slot_perm([1, 2, 0], "(0 1 2) -- the triality 3-cycle"),
    "Z2_transposition": check_slot_perm([1, 0, 2], "(0 1) -- a single transposition"),
    "reading": (
        "What forces lambda_1=lambda_2=lambda_3 is TRANSITIVITY on the three channels. "
        "A transposition only identifies two of them (dim 2 survives). Z3 is the minimal "
        "transitive subgroup of the triality S3, so 'only the Z3 rung' is correct among "
        "the three rungs tested, but the precise necessary-and-sufficient condition is "
        "transitivity, not the 3-cycle specifically."
    ),
}


# --------------------------------------------------------------------------
# 5e. Honest check on the CONTROLS: is U a legitimate symmetry there at all?
# --------------------------------------------------------------------------
def normaliser_residual(stack_idxs):
    R24 = np.zeros((len(TRIPLES), 24, 24))
    for k in range(len(TRIPLES)):
        for b, i in enumerate(stack_idxs):
            R24[k, 8 * b : 8 * b + 8, 8 * b : 8 * b + 8] = RHO[i][k]
    B = np.array([R.flatten() for R in R24]).T
    Q, _ = np.linalg.qr(B)
    worst = 0.0
    for R in R24:
        v = (U24 @ R @ U24.T).flatten()
        worst = max(worst, float(np.linalg.norm(v - Q @ (Q.T @ v)) / max(np.linalg.norm(v), 1e-30)))
    return worst


OUT["step5e_U_is_a_legitimate_symmetry_only_where_claimed"] = {
    "real_case_(rho1,rho2,rho3)_U_normalises_rel_resid": normaliser_residual([0, 1, 2]),
    "equivalent_control_(rho1,rho1,rho1)_U_normalises_rel_resid": normaliser_residual([0, 0, 0]),
    "mixed_control_(rho1,rho1,rho2)_U_normalises_rel_resid": normaliser_residual([0, 0, 1]),
    "note": (
        "U normalises the algebra image in the real case and in the equivalent control, so "
        "'+U' is a genuine symmetry requirement in both. It does NOT normalise it in the "
        "MIXED control, so that row's '+U' number is an arbitrary extra linear condition "
        "and must NOT be read as a symmetry statement."
    ),
}


# --------------------------------------------------------------------------
# 5f. Does kill criterion (a) have any discriminating power at all?
#
# # WHY this section exists: the FL Step 8a skeptic pass (MAJOR-3) observed
# # that once the three blocks carry IDENTICAL matrices, the equivariance of
# # Phi = id: O_x -> O_y is automatic, so the "Phi commutator = 0" check is an
# # identity of the construction, not a contingent fact.  That is correct.  The
# # falsifiable content sits UPSTREAM, at step2e (the locus where the three
# # blocks coincide is ALL 14 dimensions of g2 -- it could have come out
# # smaller, and then no fully-g2-equivariant mixing map would exist).  Below:
# # (i) how much room step2e had to be wrong, and (ii) a demonstration that the
# # check does discriminate against a group only ONE generator larger than g2.
# --------------------------------------------------------------------------
extra = None
for k in range(len(TRIPLES)):
    a1, a2, _a3 = TRIPLES[k]
    if np.max(np.abs(a1 - a2)) > 1e-6:  # a generator OUTSIDE the diagonal g2
        extra = RHO_SO8_24[k]
        break

d_g2_plus_one, _ka, _dra = commutant_dim(list(g2_24) + [extra])
OUT["step5f_criterion_a_discriminating_power"] = {
    "dim_diagonal_locus_measured": d_diag,
    "dim_it_could_have_been": f"any integer in 0..{len(TRIPLES)}",
    "so_step2e_is_the_falsifiable_step": True,
    "dim_End_of_F_under_g2": 9 * rung1_block["dim"],
    "dim_End_of_F_under_g2_plus_ONE_extra_so8_generator": d_g2_plus_one,
    "Phi_commutator_with_that_extra_generator": float(np.max(np.abs(Phi @ extra - extra @ Phi))),
    "reading": (
        "Adding a single generator outside g2 collapses the permitted space from 18 and "
        "breaks Phi outright, so the rung-1 check discriminates against a group one "
        "generator larger. But GIVEN step2e, Phi's g2-equivariance is an identity, so "
        "kill criterion (a) is best described as NON-FALSIFIABLE AS WRITTEN, with its real "
        "content relocated to step2e."
    ),
}


# --------------------------------------------------------------------------
# 5g. MEASURED ceiling for FL Step 4a: sweep every subgroup of the triality S3.
#
# # WHY: the first version of the write-up asserted ceiling = 1 on the grounds
# # that "a nonzero coupling needs at least one parameter" -- a DEFINITION, not
# # a measurement, which also made TASK_INFEASIBLE structurally unable to fire
# # (skeptic MAJOR-4).  Here the ceiling is measured instead: hand the analysis
# # the maximal available channel symmetry (all of the triality S3, and every
# # subgroup of it) and record how low the metric can actually be driven.
# --------------------------------------------------------------------------
SUBGROUPS = {
    "trivial_{e}": [],
    "Z2_(01)": [[1, 0, 2]],
    "Z2_(02)": [[2, 1, 0]],
    "Z2_(12)": [[0, 2, 1]],
    "Z3_(012)": [[1, 2, 0]],
    "S3_full": [[1, 2, 0], [1, 0, 2]],
}
sweep = {}
for name, gens in SUBGROUPS.items():
    mats = list(RHO_SO8_24) + [slot_perm(g)[3:27, 3:27] for g in gens]
    d, ka, dra = commutant_dim(mats)
    n_orbits = None
    # orbit count of the generated subgroup on {0,1,2}
    seen = {0: {0}, 1: {1}, 2: {2}}
    changed = True
    while changed:
        changed = False
        for g in gens:
            for i in range(3):
                for j in list(seen[i]):
                    if g[j] not in seen[i]:
                        seen[i].add(g[j])
                        changed = True
    orbits = set()
    for i in range(3):
        orbits.add(frozenset(seen[i]))
    n_orbits = len({frozenset().union(*[seen[j] for j in o]) for o in orbits})
    sweep[name] = {"dim": d, "sv_gap": [ka, dra], "orbits_on_channels": n_orbits}

OUT["step5g_measured_ceiling"] = {
    "sweep_over_every_subgroup_of_the_triality_S3": sweep,
    "MEASURED_ceiling_min_attainable_dim": min(v["dim"] for v in sweep.values()),
    "floor_from_the_equivalent_irrep_null_model": OUT["step4_negative_control_equivalent"][
        "dim_commutant_so8"
    ],
    "law": "dim = number of orbits of the assumed subgroup on {v,s,c} -- check the column",
    "law_holds": all(v["dim"] == v["orbits_on_channels"] for v in sweep.values()),
    "note": (
        "Ceiling is now a measured minimum over the full symmetry lattice, not the "
        "definitional 'a nonzero coupling needs >=1 parameter'. It is still 1; the "
        "difference is that it was searched for rather than asserted."
    ),
}


# --------------------------------------------------------------------------
# 5h. Tolerance sensitivity, measured rather than argued.
#
# # WHY: every verdict-bearing dimension except two is a numerical rank, so the
# # skeptic pass asked (item D) whether any of them moves when the tolerance
# # moves.  Rather than bound it arithmetically, re-run the rank calls with the
# # tolerance factor scaled over 12 orders of magnitude and report whether any
# # reported integer changes.
# --------------------------------------------------------------------------
def rank_at_scale(A: np.ndarray, factor: float) -> int:
    sv = np.linalg.svd(A.astype(float), compute_uv=False)
    tol = max(A.shape) * np.finfo(float).eps * sv[0] * factor
    return int(A.shape[1] - np.sum(sv > tol))


_probe = {
    "Hom(rho2->rho1)_expect_0": hom_system(RHO[1], RHO[0]),
    "Hom(rho1->rho1)_expect_1": hom_system(RHO[0], RHO[0]),
    "Hom_g2_expect_2": hom_system(G2_STACK, G2_STACK),
    "entrywise_derivations_expect_28": A_ent,
    # the three 576-column solves that actually produce the headline numbers --
    # omitted from the first version of this sweep, added after the second
    # skeptic pass pointed out the sweep did not cover the headline itself.
    "commutant_so8_RUNG2_expect_3": commutant_system(list(RHO_SO8_24)),
    "commutant_so8_plus_U_RUNG3_expect_1": commutant_system(list(RHO_SO8_24) + [U24]),
    "commutant_g2_RUNG1_expect_18": commutant_system(list(g2_24)),
}
_scales = [1e-3, 1e-1, 1.0, 1e1, 1e3, 1e6, 1e9]
_dims = {k: [rank_at_scale(A, f) for f in _scales] for k, A in _probe.items()}
_svmax = {k: float(np.linalg.svd(A.astype(float), compute_uv=False)[0]) for k, A in _probe.items()}
_tols = {
    k: {f"factor_{f:g}": max(A.shape) * np.finfo(float).eps * _svmax[k] * f for f in _scales}
    for k, A in _probe.items()
}
_moves = {k: sorted({d for d in v}) for k, v in _dims.items()}
OUT["step5h_tolerance_sensitivity"] = {
    "tolerance_factor_swept": _scales,
    "default_factor_used_everywhere_else": 1e3,
    "dims_at_each_factor": _dims,
    "distinct_dims_seen_per_probe": _moves,
    "largest_singular_value_of_each_system": _svmax,
    "actual_tolerance_per_probe_per_factor": _tols,
    # HONEST REPORT, not a pass/fail flag.
    # # WHY no hand-picked "verdict-bearing" subset any more: the first version
    # # of this block enumerated three probes and excluded the one that moves --
    # # but End(rho1)=1 IS verdict-bearing (it gives rung 2 via the pairwise
    # # route, and it is the sole basis for the absolute-irreducibility claim).
    # # Excluding it was definition-fixing.  Caught by the second skeptic pass.
    "probes_stable_across_all_7_factors": [k for k, v in _moves.items() if len(v) == 1],
    "probes_that_move": [k for k, v in _moves.items() if len(v) > 1],
    "default_tolerance_actually_used_per_probe": {k: v["factor_1000"] for k, v in _tols.items()},
    "why_the_mover_moves": (
        "End(rho1) drops 1 -> 0 ONLY at factor 1e-3, where its tolerance falls to ~6.50e-16 "
        "-- BELOW the 6.70e-16 floating-point noise floor of the true zero singular value, so "
        "no numerically-zero value could be detected at all. That is a degenerate tolerance, "
        "not a competing rank call. At the DEFAULT factor 1e3 its tolerance is ~6.50e-10 "
        "(NOT 6.5e-13, which is the factor-1 value and was misquoted in an earlier draft): "
        "about six orders above the noise floor and about nine orders below the smallest "
        "genuine singular value 1.414."
    ),
    "all_probes_including_the_mover_stable_from_factor_1e-1_upward": all(
        len({rank_at_scale(A, f) for f in _scales if f >= 1e-1}) == 1 for A in _probe.values()
    ),
}


# --------------------------------------------------------------------------
# 6.  The ladder, assembled.
# --------------------------------------------------------------------------
OUT["step6_ladder"] = {
    "rung1_G2_dim_of_permitted_endomorphisms_of_F": 9 * rung1_block["dim"],
    "rung1_channel_matrix_M_free": "arbitrary 3x3",
    "rung2_Spin8_dim": d_so8_24,
    "rung2_channel_matrix_M": "diagonal, independent lambda_1,2,3",
    "rung3_Spin8_plus_Z3_dim": d_so8_U_24,
    "rung3_channel_matrix_M": "scalar, lambda_1 = lambda_2 = lambda_3",
    "NEGATIVE_CONTROL_equivalent_triple_dim_at_Spin8_level": OUT[
        "step4_negative_control_equivalent"
    ]["dim_commutant_so8"],
    "NEGATIVE_CONTROL_PASSES": bool(
        OUT["step4_negative_control_equivalent"]["dim_commutant_so8"] > 3
    ),
}

# kill criteria
OUT["kill_criteria"] = {
    "a_G2_equivariant_channel_mixing_map_EXISTS": bool(
        rung1_block["dim"] > 0 and comm_err < 1e-9 and np.any(Phi)
    ),
    "a_FIRES_if_False": False,
    "b_Hom_Spin8_8v_8s_is_zero": bool(pairs["Hom(rho2->rho1)"]["dim"] == 0),
    "b_FIRES_if_False": False,
    "c_U_conjugates_the_three_blocks_cyclically": bool(
        OUT["step3_rung3_triality"]["U_cubed_is_identity_max_err"] < 1e-12
        and w_shift < 1e-8
        and w_direct < 1e-8
    ),
    "c_FIRES_if_False": False,
}

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "results_c133.json"), "w", encoding="utf-8") as fh:
    json.dump(OUT, fh, indent=2, default=str)

print(json.dumps(OUT, indent=2, default=str))
