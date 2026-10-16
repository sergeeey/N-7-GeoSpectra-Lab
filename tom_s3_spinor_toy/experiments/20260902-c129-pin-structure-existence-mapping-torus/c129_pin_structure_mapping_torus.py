"""C129 -- does the non-orientable mapping torus M_iota = S^3 x_iota S^1 admit
a Pin structure?

This script does NOT assert the answer.  It computes, from scratch and with
negative controls, the three ingredients the answer needs:

  PART 1  the map iota(g) = g^{-1} on S^3 subset H:  involution, isometry,
          det(d iota) = -1, fixed-point set {+-1}.  Negative control: the
          SO(4) maps phi_{a,b}(x) = a x b^{-1} have det = +1.
          Also (phi_{a,b} o iota)^2 = phi_{ab, ba} != id generically -- so the
          coset representative is NOT an involution, which is exactly the
          degeneracy claim.md asks to check.

  PART 2  the clutching function of the VERTICAL tangent bundle of the mapping
          torus, computed by finite differences in the left-invariant frame.
          Reproduces C128 sec 2b independently: M_iota(x) = -Ad(x), det = -1.
          This is what makes w_1 != 0.  Negative control: M_{phi_{a,b}} = Ad(b),
          det = +1.

  PART 3  H_*(M_f) for the mapping torus of ANY cellular self-map of ANY finite
          CW complex, via the algebraic mapping cone of (f_# - id), with exact
          integer Smith normal form and with F_2 coefficients.
          Controls that the machinery can return a NONZERO H_2:  S^2 x S^1,
          the mapping torus of the antipodal map of S^2, and the Klein bottle.

  PART 4  the Pin^+ / Pin^- existence criteria, applied.  The criteria are
          validated against RP^n, whose total SW class is (1+a)^{n+1}: the
          labelling must reproduce the literature facts that RP^2 is Pin^-
          (not Pin^+) and RP^4 is Pin^+ (not Pin^-).

No project code is imported and no project code is modified.
"""

from __future__ import annotations

import json
import pathlib

import numpy as np
import sympy as sp

RNG = np.random.default_rng(20260902)
EPS = np.zeros((3, 3, 3))
for _i, _j, _k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
    EPS[_i, _j, _k] = 1.0
    EPS[_i, _k, _j] = -1.0

out: dict[str, object] = {}


# --------------------------------------------------------------------------
# quaternions:  q = (w, x, y, z)  <->  w + x i + y j + z k
# --------------------------------------------------------------------------
def qmul(p, q):
    w1, x1, y1, z1 = p
    w2, x2, y2, z2 = q
    return np.array(
        [
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        ]
    )


def qconj(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


def qrand(n=1):
    v = RNG.normal(size=(n, 4))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def iota(q):
    """iota(g) = g^{-1};  on the UNIT sphere this is quaternionic conjugation."""
    return qconj(q)


def phi(a, b, x):
    """C125's phi_{a,b}(x) = a x b^{-1}."""
    return qmul(qmul(a, x), qconj(b))


# imaginary quaternion basis, as 4-vectors, = the Lie algebra su(2) directions
IMAG = [np.array([0.0, 1, 0, 0]), np.array([0.0, 0, 1, 0]), np.array([0.0, 0, 0, 1])]


def left_frame(x):
    """X_i(x) = x * T_i  with T_i = (1/2) * imaginary unit  (so [X_i,X_j]=eps X_k).

    The overall normalisation is irrelevant to every determinant below; it is
    fixed only so the frame is orthonormal for the round metric of radius 1/2,
    matching C128's convention [X_i,X_j] = eps_{ijk} X_k.
    """
    return np.array([qmul(x, 0.5 * e) for e in IMAG])


def frame_transition(f, x, h=1e-6):
    """M_f(x) with  df_x(X_j(x)) = M_f(x)^i_j X_i(f(x)),  by central differences."""
    fx = f(x)
    tgt = left_frame(fx)  # 3 x 4
    gram = tgt @ tgt.T
    cols = []
    for j in range(3):
        # move along the flow of X_j through x, on the sphere
        xp = x + h * left_frame(x)[j]
        xm = x - h * left_frame(x)[j]
        xp /= np.linalg.norm(xp)
        xm /= np.linalg.norm(xm)
        d = (f(xp) - f(xm)) / (2 * h)
        cols.append(np.linalg.solve(gram, tgt @ d))
    return np.array(cols).T


def Ad(x):
    """Ad(x)_{ij} defined by x T_j x^{-1} = Ad(x)_{ij} T_i (C128's convention)."""
    M = np.zeros((3, 3))
    for j in range(3):
        v = qmul(qmul(x, IMAG[j]), qconj(x))
        M[:, j] = v[1:]
    return M


# ==========================================================================
# PART 1 -- the map iota
# ==========================================================================
xs = qrand(400)

out["P1_iota_is_inverse_err"] = float(
    max(np.linalg.norm(qmul(x, iota(x)) - np.array([1.0, 0, 0, 0])) for x in xs)
)
out["P1_iota_is_involution_err"] = float(
    max(np.linalg.norm(iota(iota(x)) - x) for x in xs)
)

# iota is the restriction of diag(1,-1,-1,-1) on R^4
D = np.diag([1.0, -1, -1, -1])
out["P1_iota_is_linear_err"] = float(max(np.linalg.norm(iota(x) - D @ x) for x in xs))
out["P1_det_ambient_R4"] = float(np.linalg.det(D))

# fixed points of iota on S^3:  q = q^{-1} <=> q^2 = 1 <=> q = +-1
fixed = [np.array([1.0, 0, 0, 0]), np.array([-1.0, 0, 0, 0])]
out["P1_fixed_points_are_fixed_err"] = float(
    max(np.linalg.norm(iota(q) - q) for q in fixed)
)
out["P1_min_move_of_generic_point"] = float(
    min(np.linalg.norm(iota(x) - x) for x in xs)
)
# an explicit check that NO other fixed points exist: |iota(x)-x|^2 = 4|Im x|^2
out["P1_fixedpt_identity_err"] = float(
    max(
        abs(np.linalg.norm(iota(x) - x) ** 2 - 4 * np.linalg.norm(x[1:]) ** 2)
        for x in xs
    )
)

# det of d(iota) restricted to TS^3, and the SO(4) negative control
dets_iota, dets_phi, dets_coset = [], [], []
for x in xs[:60]:
    a, b = qrand(1)[0], qrand(1)[0]
    dets_iota.append(np.linalg.det(frame_transition(iota, x)))
    dets_phi.append(
        np.linalg.det(frame_transition(lambda y, a=a, b=b: phi(a, b, y), x))
    )
    dets_coset.append(
        np.linalg.det(frame_transition(lambda y, a=a, b=b: phi(a, b, iota(y)), x))
    )
out["P1_det_dIota_TS3"] = [float(min(dets_iota)), float(max(dets_iota))]
out["P1_det_dPhi_TS3_NEGCONTROL"] = [float(min(dets_phi)), float(max(dets_phi))]
out["P1_det_dCoset_TS3"] = [float(min(dets_coset)), float(max(dets_coset))]

# (phi_{a,b} o iota)^2 = phi_{ab, ba} -- so the generic coset rep is NOT an involution
sq_err, sq_move = [], []
for _ in range(60):
    a, b = qrand(1)[0], qrand(1)[0]
    x = qrand(1)[0]

    def g(y, a=a, b=b):
        return phi(a, b, iota(y))

    sq_err.append(np.linalg.norm(g(g(x)) - phi(qmul(a, b), qmul(b, a), x)))
    sq_move.append(np.linalg.norm(g(g(x)) - x))
out["P1_coset_square_formula_err"] = float(max(sq_err))
out["P1_coset_square_min_displacement"] = float(min(sq_move))

# ==========================================================================
# PART 2 -- clutching function of the vertical tangent bundle
# ==========================================================================
err_iota, err_phi, ctrl = [], [], []
for _ in range(60):
    x = qrand(1)[0]
    a, b = qrand(1)[0], qrand(1)[0]
    err_iota.append(np.linalg.norm(frame_transition(iota, x) + Ad(x)))
    ctrl.append(np.linalg.norm(frame_transition(iota, x) - Ad(x)))  # wrong sign
    err_phi.append(
        np.linalg.norm(frame_transition(lambda y, a=a, b=b: phi(a, b, y), x) - Ad(b))
    )
out["P2_M_iota_equals_minus_Ad_err"] = float(max(err_iota))
out["P2_M_iota_wrong_sign_NEGCONTROL"] = float(min(ctrl))
out["P2_M_phi_equals_Ad_b_err"] = float(max(err_phi))


# ==========================================================================
# PART 3 -- cellular chain complex of a mapping torus, exact integer arithmetic
# ==========================================================================
def mapping_torus_complex(C, d, fdeg):
    """Algebraic mapping torus = Cone(f_# - id : C_* -> C_*).

    C[n]    = rank of the n-th cellular chain group of X
    d[n]    = integer matrix of  partial_n : C_n -> C_{n-1}   (shape C[n-1] x C[n])
    fdeg[n] = integer matrix of  f_# : C_n -> C_n             (shape C[n] x C[n])

    Cone_n = C_{n-1} + C_n,   D(a, b) = (-d a, (f_# - id) a + d b).
    Returns (ranks, boundary matrices) of the mapping torus.
    """
    N = len(C)
    MC = [0] * (N + 1)
    for n in range(N + 1):
        MC[n] = (C[n - 1] if 1 <= n <= N else 0) + (C[n] if n < N else 0)
    D = [None] * (N + 2)
    for n in range(1, N + 2):
        rows, cols = MC[n - 1] if n - 1 <= N else 0, MC[n] if n <= N else 0
        M = sp.zeros(rows, cols)
        a_dim = C[n - 1] if 1 <= n <= N else 0
        b_dim = C[n] if n < N else 0
        # target splits as C_{n-2} (+) C_{n-1}
        t_a = C[n - 2] if 2 <= n <= N + 1 else 0
        for j in range(a_dim):  # image of an 'a' generator (an (n-1)-cell x I)
            if t_a:
                for i in range(t_a):
                    M[i, j] = -d[n - 1][i, j]
            for i in range(C[n - 1]):
                M[t_a + i, j] = fdeg[n - 1][i, j] - (1 if i == j else 0)
        for j in range(b_dim):  # image of a 'b' generator (an n-cell x {0})
            for i in range(C[n - 1]):
                M[t_a + i, a_dim + j] = d[n][i, j]
        D[n] = M
    return MC, D


def homology(MC, D, mod2=False):
    """H_n from the integer (or F_2) chain complex.  Returns human-readable list."""
    res = []
    for n in range(len(MC)):
        Dn = D[n] if n < len(D) and D[n] is not None else sp.zeros(0, MC[n])
        Dn1 = (
            D[n + 1] if n + 1 < len(D) and D[n + 1] is not None else sp.zeros(MC[n], 0)
        )
        if mod2:
            # dim H_n = dim ker(D_n) - rank(D_{n+1}) = (MC[n] - rk D_n) - rk D_{n+1}
            rk_A = _rank_f2(sp.Matrix(Dn).applyfunc(lambda v: v % 2))
            rk_B = _rank_f2(sp.Matrix(Dn1).applyfunc(lambda v: v % 2))
            res.append(f"(Z/2)^{MC[n] - rk_A - rk_B}" if MC[n] - rk_A - rk_B else "0")
        else:
            rk_A = Dn.rank() if Dn.rows and Dn.cols else 0
            free = MC[n] - rk_A - (Dn1.rank() if Dn1.rows and Dn1.cols else 0)
            tors = []
            if Dn1.rows and Dn1.cols:
                sm = _smith_diagonal(Dn1)
                tors = [int(abs(v)) for v in sm if abs(v) not in (0, 1)]
            parts = ([f"Z^{free}"] if free else []) + [f"Z/{t}" for t in tors]
            res.append(" + ".join(parts) if parts else "0")
    return res


def _rank_f2(M):
    M = [[int(v) % 2 for v in M.row(i)] for i in range(M.rows)] if M.rows else []
    rank, ncols = 0, (len(M[0]) if M else 0)
    for c in range(ncols):
        piv = next((r for r in range(rank, len(M)) if M[r][c]), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        for r in range(len(M)):
            if r != rank and M[r][c]:
                M[r] = [(a + b) % 2 for a, b in zip(M[r], M[rank])]
        rank += 1
    return rank


def _smith_diagonal(M):
    """Elementary-divisor diagonal of an integer matrix (Smith normal form)."""
    A = sp.Matrix(M)
    if A.rows == 0 or A.cols == 0:
        return []
    from sympy.matrices.normalforms import smith_normal_form

    S = smith_normal_form(A)
    return [S[i, i] for i in range(min(S.rows, S.cols))]


def sphere_complex(n, deg):
    """Minimal CW structure on S^n (one 0-cell, one n-cell), self-map of degree `deg`."""
    C = [0] * (n + 1)
    C[0], C[n] = 1, 1
    if n == 0:
        C[0] = 2
    d = [sp.zeros(C[k - 1] if k else 0, C[k]) for k in range(n + 1)]
    f = [sp.zeros(C[k], C[k]) for k in range(n + 1)]
    f[0][0, 0] = 1
    f[n][0, 0] = deg
    return C, d, f


def s3_nonminimal_complex(deg):
    """A NON-minimal CW model of S^3 with C_2 != 0, and a degree-`deg` self-map.

    WHY this exists (both FL Step 8a skeptic passes proposed it independently,
    and it is the single most important addition they produced): with the
    MINIMAL structure `C = [1,0,0,1]` the mapping torus has no 2-cells, so
    `H_2 = 0` is read off the cell count before any linear algebra runs -- the
    headline is then not a computed result, and no corruption of the rank
    routine or of the boundary maps can move it.  Here `C = [1,1,1,1]` with
    `d_2 = (1)` (a 1-cell killed by a 2-cell) is simply connected with S^3's
    homology, so it is homotopy equivalent to S^3 -- but the mapping torus now
    has TWO 2-cells and `H_2 = 0` requires two genuine F_2 rank computations.

    It also exercises the two `d`-handling branches of `mapping_torus_complex`,
    which every other case in this file leaves multiplied by zero.
    """
    C = [1, 1, 1, 1]
    d = [sp.zeros(0, 1), sp.zeros(1, 1), sp.Matrix([[1]]), sp.zeros(1, 1)]
    # f_# = identity on C_0, C_1, C_2 and multiplication by `deg` on C_3.
    # Chain map check (asserted below): d_3 = 0 and f_2 d_3 = d_3 f_3 trivially;
    # d_2 f_2 = d_2 = f_1 d_2 since f_1 = f_2 = 1.
    f = [sp.eye(1), sp.eye(1), sp.eye(1), sp.Matrix([[deg]])]
    for k in range(1, 4):
        assert (d[k] * f[k] - f[k - 1] * d[k]) == sp.zeros(*d[k].shape), (
            f"f_# is not a chain map in degree {k}"
        )
    return C, d, f


cases = {}
for label, (n, deg) in {
    "S3_iota_deg_minus1": (3, -1),
    "S3_identity_deg_plus1": (3, +1),
    "S3_arbitrary_selfmap_deg_0": (3, 0),
    "S3_arbitrary_selfmap_deg_7": (3, 7),
    # WHY deg 2 is here: it is the only case in this table whose F_2 boundary map
    # has NONZERO rank (partial_4 = deg-1 = 1), so it is the only one that can
    # detect a broken F_2 rank routine.  Injection 4 of c129_injection_tests.py
    # was NOT caught before this case was added -- recorded, not hidden.
    "S3_selfmap_deg_2_F2RANK_PROBE": (3, 2),
    "CONTROL_S2_identity": (2, +1),
    "CONTROL_S2_antipodal_deg_minus1": (2, -1),
    "CONTROL_S1_reflection_KleinBottle": (1, -1),
    "CONTROL_S1_identity_torus": (1, +1),
}.items():
    C, d, f = sphere_complex(n, deg)
    MC, D = mapping_torus_complex(C, d, f)
    cases[label] = {
        "cell_ranks_by_dim": MC,
        "H_Z": homology(MC, D, mod2=False),
        "H_F2": homology(MC, D, mod2=True),
    }
# The SAME manifold, from a CW model with C_2 != 0, so that H_2 = 0 is a
# COMPUTED rank result and not a cell count.  This is the check that makes the
# headline corruptible -- see s3_nonminimal_complex's docstring.
for label, deg in {
    "NONMINIMAL_S3_iota_deg_minus1": -1,
    "NONMINIMAL_S3_identity": +1,
}.items():
    C, d, f = s3_nonminimal_complex(deg)
    MC, D = mapping_torus_complex(C, d, f)
    cases[label] = {
        "cell_ranks_by_dim": MC,
        "H_Z": homology(MC, D, mod2=False),
        "H_F2": homology(MC, D, mod2=True),
    }
out["P3_mapping_tori"] = cases

# the single load-bearing extraction
out["P3_H2_F2_of_M_iota"] = cases["S3_iota_deg_minus1"]["H_F2"][2]
out["P3_H2_F2_of_M_iota_NONMINIMAL_MODEL"] = cases["NONMINIMAL_S3_iota_deg_minus1"][
    "H_F2"
][2]
out["P3_two_CW_models_agree"] = (
    cases["S3_iota_deg_minus1"]["H_F2"]
    == cases["NONMINIMAL_S3_iota_deg_minus1"]["H_F2"]
    and cases["S3_iota_deg_minus1"]["H_Z"]
    == cases["NONMINIMAL_S3_iota_deg_minus1"]["H_Z"]
)
out["P3_nonminimal_model_has_2cells"] = cases["NONMINIMAL_S3_iota_deg_minus1"][
    "cell_ranks_by_dim"
][2]
out["P3_H2_F2_independent_of_degree"] = sorted(
    {cases[k]["H_F2"][2] for k in cases if k.startswith("S3_")}
)
out["P3_no_2cells_in_M_iota"] = cases["S3_iota_deg_minus1"]["cell_ranks_by_dim"][2] == 0
out["P3_CONTROL_nonzero_H2_exists"] = {
    k: cases[k]["H_F2"][2] for k in cases if k.startswith("CONTROL")
}


# ==========================================================================
# PART 4 -- Pin criteria, and their validation on RP^n
# ==========================================================================
def rp_sw(n):
    """Total SW class of RP^n is (1+a)^{n+1} in F_2[a]/(a^{n+1}).  Return w1, w2."""
    a = sp.symbols("a")
    poly = sp.Poly(sp.expand((1 + a) ** (n + 1)), a)
    coeff = {k: int(poly.coeff_monomial(a**k)) % 2 for k in range(n + 1)}
    return coeff.get(1, 0), coeff.get(2, 0)  # as multiples of a and a^2


def pin_verdict(w1sq, w2):
    """Kirby-Taylor: Pin^+ exists iff w2 = 0;  Pin^- exists iff w2 + w1^2 = 0.

    Source, read directly this session: R. C. Kirby and L. R. Taylor, "Pin
    structures on low-dimensional manifolds", Sec. 0 (printed p. 177):
    "The obstruction to putting a Spin structure on a bundle [xi] ... is
     w2([xi]); for Pin+ it is still w2([xi]), and for Pin- it is
     w2([xi]) + w1^2([xi])."

    WHY the arguments are CLASSES, not booleans.  The first draft took two
    booleans (`w1_sq_zero`, `w2_zero`) and tested `w2_zero == w1_sq_zero`.
    That is NOT `w2 = w1^2`: it only says "both vanish or both don't", which
    is strictly weaker as soon as dim H^2 >= 2.  Both FL Step 8a skeptic
    passes caught this independently, and both noted the caller passed the
    SAME boolean twice -- making `Pin_minus` the constant `x == x == True`,
    i.e. half the headline was not computed at all.  Counterexample that the
    boolean version gets wrong, now a gate check: RP^2 x RP^2 has
    w1 = a+b, w2 = a^2+ab+b^2, w1^2 = a^2+b^2, so w2 + w1^2 = ab != 0 and
    w2 != 0 -- NEITHER structure exists, but the boolean version returns
    Pin_minus = True.

    `w1sq` and `w2` are sympy expressions in the relevant F_2 cohomology ring
    (0 means the zero class).  Comparison is by expansion mod 2.
    """

    return {
        "Pin_plus": bool(_f2_is_zero(w2)),
        "Pin_minus": bool(_f2_is_zero(w2 + w1sq)),
    }


def _f2_reduce(x):
    """Reduce a polynomial's coefficients mod 2.  Everything here lives in F_2.

    WHY this is a separate helper and not just `sp.expand(...) == 0`: the first
    version of this repair expanded over Z, so RP^2's w2 + w1^2 = a^2 + a^2 came
    out as `2*a**2 != 0` and the RP^2 control FLIPPED TO FALSE -- gate check G23
    fired on the very commit that was meant to fix pin_verdict.  Caught by the
    gate, not by inspection; recorded rather than silently corrected.
    """
    e = sp.expand(x)
    if e == 0:
        return sp.Integer(0)
    poly = e.as_poly()
    if poly is None:  # a bare integer
        return sp.Integer(int(e) % 2)
    return sp.expand(poly.termwise(lambda m, c: c % 2).as_expr())


def _f2_is_zero(x):
    return _f2_reduce(x) == 0


def rp_classes(n):
    """w1, w2, w1^2 of RP^n as elements of F_2[a]/(a^{n+1})."""
    a = sp.symbols("a")
    poly = sp.Poly(sp.expand((1 + a) ** (n + 1)), a)
    c = {k: int(poly.coeff_monomial(a**k)) % 2 for k in range(n + 1)}
    w1 = c.get(1, 0) * a
    w2 = c.get(2, 0) * a**2 if n >= 2 else 0
    w1sq = sp.expand(w1**2) if n >= 2 else 0  # a^{n+1} = 0, and n>=2 keeps a^2
    return sp.expand(w1), sp.expand(w2), sp.expand(w1sq)


rp_checks = {}
for n in (2, 3, 4, 6):
    w1, w2, w1sq = rp_classes(n)
    rp_checks[f"RP{n}"] = {
        "w1": str(w1),
        "w2": str(w2),
        "w1sq": str(w1sq),
        "w2_plus_w1sq": str(_f2_reduce(w2 + w1sq)),
        **pin_verdict(w1sq, w2),
    }

# RP^2 x RP^2 -- the case that discriminates the CLASS test from the BOOLEAN one.
_a, _b = sp.symbols("a b")
_w1_pp = _a + _b
_w2_pp = _a**2 + _a * _b + _b**2
_w1sq_pp = sp.expand(_w1_pp**2 - 2 * _a * _b)  # (a+b)^2 = a^2+b^2 over F_2
rp_checks["RP2xRP2"] = {
    "w1": str(_w1_pp),
    "w2": str(_w2_pp),
    "w1sq": str(_w1sq_pp),
    "w2_plus_w1sq": str(_f2_reduce(_w2_pp + _w1sq_pp)),
    **pin_verdict(_w1sq_pp, _w2_pp),
}
out["P4_RP_control"] = rp_checks
# literature anchors (arXiv:2501.01848 sec 2 + Kirby-Taylor):
#   RP^2 generates Omega^{Pin^-}_2 = Z/8  ->  RP^2 must be Pin^-, not Pin^+
#   RP^4 generates Omega^{Pin^+}_4 = Z/16 ->  RP^4 must be Pin^+, not Pin^-
out["P4_RP2_matches_literature"] = (
    rp_checks["RP2"]["Pin_minus"] and not rp_checks["RP2"]["Pin_plus"]
)
out["P4_RP4_matches_literature"] = (
    rp_checks["RP4"]["Pin_plus"] and not rp_checks["RP4"]["Pin_minus"]
)

# the manifold in question
# --- the manifold in question -------------------------------------------
# w_2 and w_1^2 are computed from SEPARATE, INDEPENDENTLY DERIVED facts, and
# only then fed to pin_verdict.  The first draft passed the same boolean
# twice, which made Pin_minus the constant `x == x`; both skeptic passes
# caught it.  The two derivations are genuinely different:
#   w_2   = 0 because it lives in H^2(M;F_2), which is the ZERO GROUP (PART 3,
#           and independently the non-minimal CW model).
#   w_1^2 = 0 for a SECOND reason that does not use PART 3 at all: w_1 is the
#           pullback pi^*(a) of the generator of H^1(S^1;F_2), so w_1^2 =
#           pi^*(a^2) and a^2 lies in H^2(S^1;F_2) = 0 because S^1 is a
#           1-complex.  (It is of course also 0 by the H^2(M)=0 route.)
H2F2_zero = out["P3_H2_F2_of_M_iota"] == "0"
H2F2_zero_nonminimal = out["P3_H2_F2_of_M_iota_NONMINIMAL_MODEL"] == "0"
w2_class = 0 if (H2F2_zero and H2F2_zero_nonminimal) else sp.symbols("w2_UNKNOWN")
# S^1 is a 1-dimensional complex, so H^2(S^1;F_2) = 0 -> pi^*(a^2) = 0.
_dim_H2_of_S1 = 0
w1sq_class = 0 if _dim_H2_of_S1 == 0 else sp.symbols("w1sq_UNKNOWN")
out["P4_M_iota"] = {
    "H2_F2_minimal_model": out["P3_H2_F2_of_M_iota"],
    "H2_F2_nonminimal_model": out["P3_H2_F2_of_M_iota_NONMINIMAL_MODEL"],
    "w1_nonzero_because_det_dIota_is_minus1": max(dets_iota) < 0,
    "w2_class": str(w2_class),
    "w1sq_class": str(w1sq_class),
    "w1sq_zero_reason": "pullback of a^2 from H^2(S^1;F_2) = 0 (independent of PART 3)",
    "w2_zero_reason": "lives in H^2(M;F_2) = 0 (PART 3, two CW models)",
    **pin_verdict(w1sq_class, w2_class),
}

# ==========================================================================
# PART 5 -- CONSTRUCTIVE route, independent of PART 3's obstruction argument.
#
# M_f = (S^3 x R)/Z with the deck generator gamma(x,s) = (f(x), s+1).  S^3 x R
# is parallelizable, so upstairs the Pin^{+-}(4) bundle is trivial and a
# Pin structure on M_f is exactly a lift of gamma.  Because Z is FREE on one
# generator there is no relation to satisfy: any lift of the single map
#     u : S^3 -> O(4),   u(x) = M_f(x) (+) 1
# to the double cover Pin^{+-}(4) -> O(4) generates a Z-action, and such a lift
# always exists because S^3 is SIMPLY CONNECTED.
#
# Here we exhibit the lift explicitly for f = iota, where u(x) = -Ad(x) (+) 1,
# in BOTH Clifford signatures, and check it really covers -Ad(x).
#   lift(x) = omega * S(x),  omega = e1 e2 e3,  S(x) = the Spin(3) element of x.
# ==========================================================================
SIG = {  # e_i^2 = +1 -> Pin^+ ;  e_i^2 = -1 -> Pin^-
    "Pin_plus_Cl(3,0)": (
        +1,
        [
            np.array([[0, 1], [1, 0]], dtype=complex),
            np.array([[0, -1j], [1j, 0]], dtype=complex),
            np.array([[1, 0], [0, -1]], dtype=complex),
        ],
    ),
}
_sig_m = [1j * m for m in SIG["Pin_plus_Cl(3,0)"][1]]
SIG["Pin_minus_Cl(0,3)"] = (-1, _sig_m)

I2 = np.eye(2, dtype=complex)


def spin_elt(q, e, s):
    """The Spin(3) element of the unit quaternion q, in the even part of Cl(e).

    Even basis: 1, s*e2e3, s*e3e1, s*e1e2 -- each squares to -1 in BOTH
    signatures, so this is the quaternion algebra either way.

    WHY the sign s is a parameter and not hard-coded: the two bivector bases
    {+e_j e_k} and {-e_j e_k} are BOTH valid quaternion bases, and they give
    Ad(x) and Ad(x)^{-1} respectively.  Which one is "the" quaternion embedding
    depends on the Clifford signature (e_i = sigma_i vs e_i = i*sigma_i differ
    by exactly this sign in e_2 e_3).  Hard-coding s = +1 made the first draft
    of this check FAIL in Cl(3,0) with residual 2.82 -- caught by gate G28.
    The repair is to determine s per signature and to gate that EXACTLY ONE
    value of s works, so the determination cannot be vacuous.
    """
    b = [s * (e[1] @ e[2]), s * (e[2] @ e[0]), s * (e[0] @ e[1])]
    return q[0] * I2 + q[1] * b[0] + q[2] * b[1] + q[3] * b[2]


def twisted_adjoint(u, parity, e):
    """rho(u)(v) = alpha(u) v u^{-1};  returns the 3x3 real matrix on span(e_i).

    parity = +1 for even u (alpha(u) = u), -1 for odd u (alpha(u) = -u).
    """
    ui = np.linalg.inv(u)
    M = np.zeros((3, 3), dtype=complex)
    for j in range(3):
        w = parity * (u @ e[j] @ ui)
        # expand w in the basis e_i:  <e_i, w> = tr(e_i^{-1} w)/2 works in both sigs
        for i in range(3):
            M[i, j] = np.trace(np.linalg.inv(e[i]) @ w) / 2
    return M


pin_lift = {}
for name, (sq, e) in SIG.items():
    anti = max(
        np.linalg.norm(e[i] @ e[j] + e[j] @ e[i] - 2 * (sq if i == j else 0) * I2)
        for i in range(3)
        for j in range(3)
    )
    omega = e[0] @ e[1] @ e[2]
    om_sq = omega @ omega
    om_sq_scalar = complex(om_sq[0, 0])
    central = max(np.linalg.norm(omega @ e[i] - e[i] @ omega) for i in range(3))
    probe = qrand(12)
    # determine the quaternion embedding sign; EXACTLY ONE must work
    fit = {
        s: float(
            max(
                np.linalg.norm(twisted_adjoint(spin_elt(x, e, s), +1, e).real - Ad(x))
                for x in probe
            )
        )
        for s in (+1, -1)
    }
    good = [s for s, v in fit.items() if v < 1e-10]
    s_ok = good[0] if len(good) == 1 else None

    errs_even, errs_odd, imag = [], [], []
    for x in qrand(40):
        S = spin_elt(x, e, s_ok if s_ok else +1)
        R_even = twisted_adjoint(S, +1, e)  # should be Ad(x)
        R_odd = twisted_adjoint(omega @ S, -1, e)  # should be -Ad(x) = M_iota(x)
        imag.append(max(abs(R_even.imag).max(), abs(R_odd.imag).max()))
        errs_even.append(np.linalg.norm(R_even.real - Ad(x)))
        errs_odd.append(np.linalg.norm(R_odd.real + Ad(x)))
    pin_lift[name] = {
        "clifford_relations_err": float(anti),
        "omega_squared": [float(om_sq_scalar.real), float(om_sq_scalar.imag)],
        "omega_is_central_err": float(central),
        "quaternion_embedding_sign": s_ok,
        "embedding_fit_both_signs": fit,
        "exactly_one_sign_works": len(good) == 1,
        "rho(S)_equals_Ad_err": float(max(errs_even)),
        "rho(omega*S)_equals_MINUS_Ad_err": float(max(errs_odd)),
        "residual_imaginary_part": float(max(imag)),
    }
out["P5_explicit_pin_lift"] = pin_lift
out["P5_lift_exists_in_both_signatures"] = all(
    v["rho(omega*S)_equals_MINUS_Ad_err"] < 1e-10 for v in pin_lift.values()
)
# the two Pin groups are genuinely different here -- omega^2 has opposite signs
out["P5_omega_sq_in_Cl3"] = [
    pin_lift["Pin_plus_Cl(3,0)"]["omega_squared"],
    pin_lift["Pin_minus_Cl(0,3)"]["omega_squared"],
]
# CORRECTION forced by FL Step 8a skeptic pass 2, finding 4.  The first draft
# said "omega^2 = -1 vs +1 is PRECISELY what distinguishes the two Pin groups".
# That is true of omega = e1e2e3 in Cl(3), but the structure group of a
# 4-MANIFOLD is O(4)/Pin^{+-}(4), and there omega_4 = e1e2e3e4 has
#   omega_4^2 = (-1)^{n(n-1)/2} * prod e_i^2 = (-1)^6 * (+1)^4 = +1   in Cl(4,0)
#              = (-1)^6 * (-1)^4 = +1                                 in Cl(0,4)
# -- the SAME sign in both.  What actually distinguishes Pin^+ from Pin^- is
# the square of a VECTOR, e_i^2 = +1 vs -1, which gate G26 does test.
_om4 = {}
for name, (sq, _e3) in SIG.items():
    n4 = 4
    _om4[name] = {
        "vector_square_e_i^2": sq,
        "omega_4_squared_predicted": int((-1) ** (n4 * (n4 - 1) // 2) * (sq**n4)),
    }
out["P5_omega4_sq_is_the_SAME_in_both"] = _om4
out["P5_what_distinguishes_the_groups_is_vector_square"] = [
    SIG["Pin_plus_Cl(3,0)"][0],
    SIG["Pin_minus_Cl(0,3)"][0],
]

# --- the Cl(3) -> Cl(4) bridging step, which the first draft omitted -------
# The clutching function of TM_f is u(x) = M_iota(x) (+) 1 in O(4), not O(3).
# omega = e1e2e3 is central in Cl(3) but ANTI-commutes with e4 in Cl(4), so the
# first draft's stated reason ("omega is central in odd dimension") does NOT
# apply in Cl(4).  The correct statement, verified numerically below: omega is
# ODD, so the twisted adjoint gives rho(omega) e4 = -(omega e4 omega^-1)
# = -(-e4) = +e4, while rho(omega) e_i = -e_i for i = 1,2,3.  Hence
#   rho(omega * S(x)) = (-Ad(x)) (+) (+1) = u(x)   exactly as required.
_G = [
    np.array([[0, 1], [1, 0]]),
    np.array([[0, -1j], [1j, 0]]),
    np.array([[1, 0], [0, -1]]),
]
_G = [g.astype(complex) for g in _G]
# 4x4 gamma matrices for Cl(4,0): e_i = sigma_i (x) sigma_1 (i=1,2,3), e_4 = 1 (x) sigma_2
_s1 = np.array([[0, 1], [1, 0]], dtype=complex)
_s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
E4 = [np.kron(g, _s1) for g in _G] + [np.kron(np.eye(2), _s2)]
_anti4 = max(
    np.linalg.norm(E4[i] @ E4[j] + E4[j] @ E4[i] - 2 * (1 if i == j else 0) * np.eye(4))
    for i in range(4)
    for j in range(4)
)
OM3_in4 = E4[0] @ E4[1] @ E4[2]
out["P5_Cl4_bridge"] = {
    "clifford_relations_err_Cl(4,0)": float(_anti4),
    "omega3_anticommutes_with_e4_err": float(
        np.linalg.norm(OM3_in4 @ E4[3] + E4[3] @ OM3_in4)
    ),
    "omega3_commutes_with_e4_FALSE_control": float(
        np.linalg.norm(OM3_in4 @ E4[3] - E4[3] @ OM3_in4)
    ),
    # twisted adjoint of the ODD element omega3 on each basis vector
    "rho_omega3_on_e1e2e3_should_be_minus1": [
        float(np.linalg.norm(-(OM3_in4 @ E4[k] @ np.linalg.inv(OM3_in4)) + E4[k]))
        for k in range(3)
    ],
    "rho_omega3_on_e4_should_be_PLUS1": float(
        np.linalg.norm(-(OM3_in4 @ E4[3] @ np.linalg.inv(OM3_in4)) - E4[3])
    ),
}

# ==========================================================================
# PART 6 -- consistency controls on PART 3's answer, and the coset's fixed point
# ==========================================================================
betti2 = [
    int(s.split("^")[1]) if s.startswith("(Z/2)") else 0
    for s in cases["S3_iota_deg_minus1"]["H_F2"]
]
out["P6_F2_betti_numbers"] = betti2
out["P6_euler_characteristic"] = int(sum((-1) ** k * b for k, b in enumerate(betti2)))
out["P6_poincare_duality_mod2_symmetric"] = betti2 == betti2[::-1]

# g = phi_{a,b} o iota is the restriction of a LINEAR map G in O(4) with det=-1;
# a real 4x4 orthogonal matrix of det -1 always has +1 as an eigenvalue, so g has
# a fixed point on S^3 -- which is what lets us put the CW 0-cell at a fixed point
# and makes the PART 3 cell count valid for the coset representative too.
fix_eigs, fix_dets = [], []
for _ in range(40):
    a, b = qrand(1)[0], qrand(1)[0]
    G = np.column_stack([phi(a, b, iota(np.eye(4)[k])) for k in range(4)])
    fix_dets.append(np.linalg.det(G))
    fix_eigs.append(min(abs(np.linalg.eigvals(G) - 1.0)))
out["P6_coset_map_is_linear_det"] = [float(min(fix_dets)), float(max(fix_dets))]
out["P6_coset_map_has_eigenvalue_plus1"] = float(max(fix_eigs))

# ==========================================================================
# gate
# ==========================================================================
gate = {
    "G1_iota_is_inverse": out["P1_iota_is_inverse_err"] < 1e-12,
    "G2_iota_is_involution": out["P1_iota_is_involution_err"] < 1e-12,
    "G3_iota_is_linear_diag": out["P1_iota_is_linear_err"] < 1e-12,
    "G4_fixed_point_identity": out["P1_fixedpt_identity_err"] < 1e-12,
    "G5_det_dIota_is_minus1": max(dets_iota) < -0.999 and min(dets_iota) > -1.001,
    "G6_det_dPhi_is_plus1_NEGCONTROL": min(dets_phi) > 0.999 and max(dets_phi) < 1.001,
    "G7_det_dCoset_is_minus1": max(dets_coset) < -0.999,
    "G8_coset_square_formula": out["P1_coset_square_formula_err"] < 1e-12,
    "G9_coset_generically_not_involution": out["P1_coset_square_min_displacement"]
    > 1e-2,
    "G10_M_iota_is_minus_Ad": out["P2_M_iota_equals_minus_Ad_err"] < 1e-6,
    "G11_wrong_sign_control_fires": out["P2_M_iota_wrong_sign_NEGCONTROL"] > 1.0,
    "G12_M_phi_is_Ad_b": out["P2_M_phi_equals_Ad_b_err"] < 1e-6,
    "G13_H2F2_of_M_iota_vanishes": out["P3_H2_F2_of_M_iota"] == "0",
    "G14_H2F2_vanishes_for_every_degree": out["P3_H2_F2_independent_of_degree"]
    == ["0"],
    "G15_M_iota_has_no_2cells": bool(out["P3_no_2cells_in_M_iota"]),
    "G16_CONTROL_S2xS1_has_nonzero_H2": cases["CONTROL_S2_identity"]["H_F2"][2] != "0",
    "G17_CONTROL_S2antipodal_has_nonzero_H2": (
        cases["CONTROL_S2_antipodal_deg_minus1"]["H_F2"][2] != "0"
    ),
    "G18_CONTROL_KleinBottle_H1_is_Z_plus_Z2": (
        cases["CONTROL_S1_reflection_KleinBottle"]["H_Z"][1] == "Z^1 + Z/2"
    ),
    "G19_CONTROL_KleinBottle_H2_vanishes": (
        cases["CONTROL_S1_reflection_KleinBottle"]["H_Z"][2] == "0"
    ),
    "G20_CONTROL_torus_H2_is_Z": cases["CONTROL_S1_identity_torus"]["H_Z"][2] == "Z^1",
    "G21_M_iota_H4_Z_vanishes_nonorientable": (
        cases["S3_iota_deg_minus1"]["H_Z"][4] == "0"
    ),
    "G22_CONTROL_S3xS1_H4_Z_is_Z_orientable": (
        cases["S3_identity_deg_plus1"]["H_Z"][4] == "Z^1"
    ),
    "G23_RP2_is_Pin_minus_not_plus": bool(out["P4_RP2_matches_literature"]),
    "G24_RP4_is_Pin_plus_not_minus": bool(out["P4_RP4_matches_literature"]),
    "G25_RP3_is_spin": rp_checks["RP3"]["w1"] == "0" and rp_checks["RP3"]["w2"] == "0",
    # The case that discriminates the CLASS-valued criterion from the BOOLEAN
    # one both skeptic passes rejected: RP^2 x RP^2 has w2 != 0 AND
    # w2 + w1^2 = a*b != 0, so NEITHER structure exists.  The old boolean
    # version returned Pin_minus = True here.
    "G25b_RP2xRP2_admits_NEITHER_structure": (
        not rp_checks["RP2xRP2"]["Pin_plus"] and not rp_checks["RP2xRP2"]["Pin_minus"]
    ),
    "G25c_RP2xRP2_w2_plus_w1sq_is_nonzero": rp_checks["RP2xRP2"]["w2_plus_w1sq"] != "0",
    "G26_clifford_relations_hold_both_sigs": all(
        v["clifford_relations_err"] < 1e-12 for v in pin_lift.values()
    ),
    "G27_omega_central_both_sigs": all(
        v["omega_is_central_err"] < 1e-12 for v in pin_lift.values()
    ),
    "G28_rho_of_Spin_is_Ad": all(
        v["rho(S)_equals_Ad_err"] < 1e-10 for v in pin_lift.values()
    ),
    "G29_explicit_lift_covers_minus_Ad_both_sigs": bool(
        out["P5_lift_exists_in_both_signatures"]
    ),
    "G29b_embedding_sign_determination_is_nonvacuous": all(
        v["exactly_one_sign_works"] for v in pin_lift.values()
    ),
    # --- Cl(3) -> Cl(4) bridge (skeptic pass 2, finding 4 / pass 1, finding 8) ---
    "G30a_Cl4_relations_hold": out["P5_Cl4_bridge"]["clifford_relations_err_Cl(4,0)"]
    < 1e-12,
    "G30b_omega3_ANTIcommutes_with_e4": (
        out["P5_Cl4_bridge"]["omega3_anticommutes_with_e4_err"] < 1e-12
    ),
    "G30c_omega3_is_NOT_central_in_Cl4_CONTROL": (
        out["P5_Cl4_bridge"]["omega3_commutes_with_e4_FALSE_control"] > 1.0
    ),
    "G30d_rho_omega3_is_minus1_on_e1e2e3": all(
        v < 1e-12 for v in out["P5_Cl4_bridge"]["rho_omega3_on_e1e2e3_should_be_minus1"]
    ),
    "G30e_rho_omega3_is_PLUS1_on_e4": (
        out["P5_Cl4_bridge"]["rho_omega3_on_e4_should_be_PLUS1"] < 1e-12
    ),
    "G30f_omega4_sq_is_the_SAME_in_both_signatures": (
        _om4["Pin_plus_Cl(3,0)"]["omega_4_squared_predicted"]
        == _om4["Pin_minus_Cl(0,3)"]["omega_4_squared_predicted"]
    ),
    "G30_omega3_sq_differs_between_the_two_groups": (
        pin_lift["Pin_plus_Cl(3,0)"]["omega_squared"][0]
        * pin_lift["Pin_minus_Cl(0,3)"]["omega_squared"][0]
        < 0
    ),
    # NOTE, both skeptic passes, independently: these two are IDENTITIES of the
    # mapping-cone construction, not discriminating tests.
    #   sum (-1)^n MC[n] = sum (-1)^n (C[n-1]+C[n]) = 0  for ANY input complex,
    # and the Betti version inherits it by rank-nullity telescoping even if
    # _rank_f2 is completely broken.  The first draft claimed "neither is
    # automatic from the construction ... injection 3 breaks them"; the round's
    # OWN results_c129_injections.json shows injection 3 fired G18/G19/G21/G36/
    # G37 and NOT these.  Retained as sanity identities, renamed so no future
    # reader counts them as evidence.
    "G31_IDENTITY_euler_characteristic_is_zero": out["P6_euler_characteristic"] == 0,
    "G32_IDENTITY_poincare_duality_mod2": bool(
        out["P6_poincare_duality_mod2_symmetric"]
    ),
    "G33_coset_map_linear_det_minus1": max(out["P6_coset_map_is_linear_det"]) < -0.999,
    "G34_coset_map_has_fixed_point": out["P6_coset_map_has_eigenvalue_plus1"] < 1e-9,
    # --- checks that the F_2 rank routine itself works (injection-4 repair) ---
    "G35_f2_rank_unit_tests": (
        _rank_f2(sp.Matrix([[1, 1], [1, 1]])) == 1
        and _rank_f2(sp.Matrix([[1, 1], [1, 0]])) == 2
        and _rank_f2(sp.Matrix([[0, 0], [0, 0]])) == 0
        and _rank_f2(sp.Matrix([[2, 0], [0, 4]])) == 0
        and _rank_f2(sp.Matrix([[3, 0], [0, 4]])) == 1
    ),
    "G36_F2RANK_PROBE_deg2_H3_and_H4_vanish": (
        cases["S3_selfmap_deg_2_F2RANK_PROBE"]["H_F2"][3] == "0"
        and cases["S3_selfmap_deg_2_F2RANK_PROBE"]["H_F2"][4] == "0"
    ),
    # --- the non-minimal CW model: H_2 = 0 as a COMPUTED rank, not a cell count
    "G37a_nonminimal_model_really_has_2cells": out["P3_nonminimal_model_has_2cells"]
    >= 2,
    "G37b_nonminimal_model_gives_H2_zero": (
        out["P3_H2_F2_of_M_iota_NONMINIMAL_MODEL"] == "0"
    ),
    "G37c_two_CW_models_agree_in_every_degree": bool(out["P3_two_CW_models_agree"]),
    "G37_F2RANK_PROBE_matches_Z_computation": (
        cases["S3_selfmap_deg_2_F2RANK_PROBE"]["H_Z"][3] == "0"
    ),
}
out["GATE"] = gate
out["GATE_PASSED"] = f"{sum(gate.values())} / {len(gate)}"
out["ALL_OK"] = all(gate.values())

_verdict = pin_verdict(w1sq_class, w2_class)
out["VERDICT_INPUTS"] = {
    "w1_nonzero": bool(max(dets_iota) < 0),
    "H2_M_iota_F2_minimal_model": out["P3_H2_F2_of_M_iota"],
    "H2_M_iota_F2_nonminimal_model": out["P3_H2_F2_of_M_iota_NONMINIMAL_MODEL"],
    "w2_zero": bool(_f2_is_zero(w2_class)),
    "w1_squared_zero": bool(_f2_is_zero(w1sq_class)),
    "Pin_plus_exists": bool(_verdict["Pin_plus"]),
    "Pin_minus_exists": bool(_verdict["Pin_minus"]),
    "answer_depends_on_choice_of_relating_map": (
        out["P3_H2_F2_independent_of_degree"] != ["0"]
    ),
}

here = pathlib.Path(__file__).resolve().parent
(here / "results_c129.json").write_text(
    json.dumps(
        out, indent=2, default=lambda o: bool(o) if isinstance(o, np.bool_) else str(o)
    ),
    encoding="utf-8",
)

for k, v in out.items():
    if k in ("P3_mapping_tori",):
        for lab, val in v.items():
            print(f"  {lab:42s} cells={val['cell_ranks_by_dim']}")
            print(f"  {'':42s} H_Z ={val['H_Z']}")
            print(f"  {'':42s} H_F2={val['H_F2']}")
        continue
    print(f"{k}: {v}")
