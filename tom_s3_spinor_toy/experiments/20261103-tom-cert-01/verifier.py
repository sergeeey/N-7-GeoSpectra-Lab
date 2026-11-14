"""TOM-CERT-01 independent verifier.

Standard library only (fractions, json, re, sys). Exact Gaussian-rational arithmetic; the
checks never use inexact numbers. This file imports nothing from the builder and does not
reuse its algorithm: it restates the conventions below and recomputes every operator itself.

Usage:  python verifier.py certificate.json [--skip-checks ID,ID]
Exit code: 0 = ACCEPT (all selected checks pass), 1 = REJECT, 2 = malformed input.

Statement being certified (conventions are part of the statement):
  x = (x0, x1) in C^2 with |x0|^2 + |x1|^2 = 1 is a point of S^3 = SU(2) via
  g(x) = [[x0, -conj x1], [x1, conj x0]]. Formal variables z0, z1, w0, w1 = x0, x1, conj x0, conj x1.
  W = span{g00, g01, g10, g11} (order j = 2a + b).
  (L_h f)(x) = f(h^-1 x);  (R_k f)(x) = f(x.k), x.k = k00 x + k10 J x, J x = (-conj x1, conj x0).
  dL(T) f = d/dt f(exp(-tT) x), dR(T) f = d/dt f(x.exp(tT)) at t = 0; T_a = -i sigma_a / 2.
  Matrix convention: M[i][j] = coefficient of basis i in the image of basis j.
  Expected: W is closed under L and R; W = (two L-doublets, fixed column) = (two R-doublets, fixed
  row); under SU(2)_L x SU(2)_R it is irreducible with Casimirs (3/4, 3/4), i.e. (1/2, 1/2).
"""

import json
import re
import sys
from fractions import Fraction as F

QRE = re.compile(r"-?[0-9]+(/[0-9]+)?")


class Gq:
    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        self.re = F(re_)
        self.im = F(im_)

    def __add__(self, o):
        o = cv(o)
        return Gq(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return Gq(-self.re, -self.im)

    def __sub__(self, o):
        o = cv(o)
        return Gq(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return cv(o) - self

    def __mul__(self, o):
        o = cv(o)
        return Gq(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return Gq(self.re, -self.im)

    def inv(self):
        d = self.re * self.re + self.im * self.im
        return Gq(self.re / d, -self.im / d)

    def zero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        o = cv(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"({self.re}+{self.im}i)"


def cv(x):
    return x if isinstance(x, Gq) else Gq(x, 0)


ZERO = Gq(0, 0)
ONE = Gq(1, 0)
IU = Gq(0, 1)


def pq(s):
    if not isinstance(s, str) or not QRE.fullmatch(s):
        raise ValueError(f"not an exact rational literal: {s!r}")
    try:
        return F(s)
    except ZeroDivisionError:
        raise ValueError(f"zero denominator: {s!r}") from None


def pg(pair):
    return Gq(pq(pair[0]), pq(pair[1]))


# ---------- polynomials in (z0, z1, w0, w1): dict exponent-tuple -> Gq ----------
def clean(p):
    return {m: c for m, c in p.items() if not c.zero()}


def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, ZERO) + c
    return clean(r)


def pscale(p, s):
    return clean({m: c * s for m, c in p.items()})


def pmul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            r[m] = r.get(m, ZERO) + c1 * c2
    return clean(r)


def pconst(c):
    return clean({(0, 0, 0, 0): cv(c)})


def pvar(i):
    m = [0, 0, 0, 0]
    m[i] = 1
    return {tuple(m): ONE}


def plin(cs):
    r = {}
    for i, c in enumerate(cs):
        if not cv(c).zero():
            r[tuple(1 if k == i else 0 for k in range(4))] = cv(c)
    return r


def pdiff(p, i):
    r = {}
    for m, c in p.items():
        if m[i] > 0:
            mm = list(m)
            mm[i] -= 1
            r[tuple(mm)] = r.get(tuple(mm), ZERO) + c * m[i]
    return clean(r)


def ppow(p, n):
    r = pconst(1)
    for _ in range(n):
        r = pmul(r, p)
    return r


def psubs(p, sub):
    r = {}
    for m, c in p.items():
        term = pconst(c)
        for i in range(4):
            if m[i]:
                term = pmul(term, ppow(sub[i], m[i]))
        r = padd(r, term)
    return r


def parse_poly(terms):
    r = {}
    for e, re_, im_ in terms:
        key = tuple(e)
        if len(key) != 4 or any(type(k) is not int or k < 0 for k in key):
            raise ValueError(f"bad exponent vector {e!r}")
        if key in r:
            raise ValueError(f"duplicate monomial {key} in one polynomial")
        r[key] = Gq(pq(re_), pq(im_))
    return clean(r)


# ---------- linear algebra over Gaussian rationals ----------
def row_reduce(rows, ncols):
    """rows: list of lists of Gq; returns (reduced rows, pivot columns)."""
    rows = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        pr = next((i for i in range(r, len(rows)) if not rows[i][c].zero()), None)
        if pr is None:
            continue
        rows[r], rows[pr] = rows[pr], rows[r]
        iv = rows[r][c].inv()
        rows[r] = [x * iv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and not rows[i][c].zero():
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv.append(c)
        r += 1
    return rows, piv


def rank(rows, ncols):
    return len(row_reduce(rows, ncols)[1])


def express(p, basis):
    """coefficients c with p = sum c_j basis_j (exact), or None if p is not in the span."""
    monos = sorted(set(m for b in basis for m in b) | set(p))
    n = len(basis)
    rows = [[b.get(m, ZERO) for b in basis] + [p.get(m, ZERO)] for m in monos]
    red, piv = row_reduce(rows, n + 1)
    if n in piv:  # inconsistent: pivot in the augmented column
        return None
    sol = [ZERO] * n
    for i, c in enumerate(piv):
        sol[c] = red[i][n]
    return sol


# ---------- 2x2 / nxn matrices ----------
def mm(A, B):
    return [
        [sum((A[i][k] * B[k][j] for k in range(len(B))), ZERO) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def madd(A, B):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]


def msc(A, s):
    return [[a * s for a in r] for r in A]


def mcomm(A, B):
    return madd(mm(A, B), msc(mm(B, A), -1))


def mconj(A):
    return [[a.conj() for a in r] for r in A]


def mdag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def meye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def meq(A, B):
    if len(A) != len(B) or any(len(r1) != len(r2) for r1, r2 in zip(A, B)):
        return False
    return all(a == b for r1, r2 in zip(A, B) for a, b in zip(r1, r2))


def pmat(M, n):
    if not isinstance(M, list) or len(M) != n or any(not isinstance(r, list) or len(r) != n for r in M):
        raise ValueError(f"matrix is not {n}x{n}")
    return [[pg(e) for e in row] for row in M]


def pint(x):
    if type(x) is not int:
        raise ValueError(f"not an integer: {x!r}")
    return x


def commutant_dim(mats, n):
    rows = []
    for A in mats:
        for p in range(n):
            for q in range(n):
                v = [ZERO] * (n * n)
                for r in range(n):
                    v[p * n + r] = v[p * n + r] + A[r][q]
                for s in range(n):
                    v[s * n + q] = v[s * n + q] - A[p][s]
                rows.append(v)
    return n * n - rank(rows, n * n)


def restrict(M, idx):
    return [[M[i][j] for j in idx] for i in idx]


# ---------- own definitions (the statement) ----------
SIG = [
    [[ZERO, ONE], [ONE, ZERO]],
    [[ZERO, -IU], [IU, ZERO]],
    [[ONE, ZERO], [ZERO, -ONE]],
]
TGEN = [msc(s, Gq(0, F(-1, 2))) for s in SIG]  # T_a = -i sigma_a / 2
EPS_LC = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
OWN_BASIS = [pvar(0), pscale(pvar(3), -1), pvar(1), pvar(2)]  # g00, g01, g10, g11


def left_sub(A):
    c = mconj(A)
    return [
        plin([A[0][0], A[0][1], 0, 0]),
        plin([A[1][0], A[1][1], 0, 0]),
        plin([0, 0, c[0][0], c[0][1]]),
        plin([0, 0, c[1][0], c[1][1]]),
    ]


def right_sub(k):
    c = mconj(k)
    return [
        plin([k[0][0], 0, 0, -k[1][0]]),
        plin([0, k[0][0], k[1][0], 0]),
        plin([0, -c[1][0], c[0][0], 0]),
        plin([c[1][0], 0, 0, c[0][0]]),
    ]


def vf_apply(f, delta):
    r = {}
    for i in range(4):
        r = padd(r, pmul(pdiff(f, i), delta[i]))
    return r


def dleft_delta(T):
    c = mconj(T)
    return [
        plin([-T[0][0], -T[0][1], 0, 0]),
        plin([-T[1][0], -T[1][1], 0, 0]),
        plin([0, 0, -c[0][0], -c[0][1]]),
        plin([0, 0, -c[1][0], -c[1][1]]),
    ]


def dright_delta(T):
    c = mconj(T)
    return [
        plin([T[0][0], 0, 0, -T[1][0]]),
        plin([0, T[0][0], T[1][0], 0]),
        plin([0, -c[1][0], c[0][0], 0]),
        plin([c[1][0], 0, 0, c[0][0]]),
    ]


def op_matrix(op, basis):
    cols = []
    for b in basis:
        c = express(op(b), basis)
        if c is None:
            raise LookupError("image not in span(W) (closure fails)")
        cols.append(c)
    return [[cols[j][i] for j in range(len(basis))] for i in range(len(basis))]


def su2_from_quat(q):
    a, b, c, d, den = (F(x) for x in q)
    if den == 0 or a * a + b * b + c * c + d * d != den * den:
        raise ValueError("quaternion is not a unit rational quaternion")
    a, b, c, d = a / den, b / den, c / den, d / den
    return [[Gq(a, b), Gq(-c, d)], [Gq(c, d), Gq(a, -b)]]


EXPECTED_CONVENTIONS = {
    "g": "g(x) = [[x0, -conj x1], [x1, conj x0]]",
    "variables": "z0=x0, z1=x1, w0=conj x0, w1=conj x1 (formal)",
    "basis_order": "j = 2a + b: g00, g01, g10, g11",
    "L": "(L_h f)(x) = f(h^-1 x)",
    "R": "(R_k f)(x) = f(x.k), x.k = k00 x + k10 J x, J x = (-conj x1, conj x0)",
    "T": "T_a = -i sigma_a / 2",
    "dL": "d/dt f(exp(-tT) x)",
    "dR": "d/dt f(x . exp(tT))",
    "matrix": "M[i][j] = coefficient of basis i in image of basis j",
}


# ---------- checks ----------
RESULTS = []


def check(cid, fn, skip):
    if cid in skip:
        RESULTS.append((cid, None, "skipped on request"))
        return
    try:
        ok, msg = fn()
    except (LookupError, ValueError, KeyError, IndexError, TypeError, ZeroDivisionError) as e:
        ok, msg = False, f"{type(e).__name__}: {e}"
    RESULTS.append((cid, ok, msg))


def run(cert, skip):
    if not isinstance(cert["basis"], list) or len(cert["basis"]) != 4:
        raise ValueError("basis must list exactly 4 polynomials")
    basis = [parse_poly(b) for b in cert["basis"]]
    if len(cert["dL"]) != 3 or len(cert["dR"]) != 3:
        raise ValueError("dL and dR must list exactly 3 matrices")
    DL = [pmat(m, 4) for m in cert["dL"]]
    DR = [pmat(m, 4) for m in cert["dR"]]
    dec = cert["decomposition"]
    ge = cert["group_elements"]
    if not isinstance(ge, list) or len(ge) < 6:
        raise ValueError("group_elements must list at least 6 elements")
    pairs = cert["homomorphism_pairs"]
    if not isinstance(pairs, list) or len(pairs) < 4:
        raise ValueError("homomorphism_pairs must list at least 4 pairs")
    for pr in pairs:
        if not isinstance(pr, list) or len(pr) != 2:
            raise ValueError("a homomorphism pair must have two indices")
        for k in pr:
            if pint(k) < 0 or k >= len(ge):
                raise ValueError(f"homomorphism pair index out of range: {k}")
        if pr[0] == pr[1]:
            raise ValueError("homomorphism pair of equal elements")

    def v0():
        ok = cert.get("schema") == "tom-cert-01/1" and cert.get("conventions") == EXPECTED_CONVENTIONS
        return ok, "certificate declares the schema and the exact conventions this verifier implements"

    def v1():
        same = all(a == b for a, b in zip(basis, OWN_BASIS)) and len(basis) == 4
        monos = sorted(set(m for b in basis for m in b))
        r = rank([[b.get(m, ZERO) for m in monos] for b in basis], len(monos))
        return same and r == 4, f"basis equals g_ab: {same}; rank {r} of 4"

    def v2gen():
        gens = cert["generators"]
        ok = len(gens) == 3 and all(meq(pmat(g, 2), t) for g, t in zip(gens, TGEN))
        return ok, "exactly three generators, equal to -i sigma_a/2"

    def v2a():
        for a, T in enumerate(TGEN):
            op_matrix(lambda f: vf_apply(f, dleft_delta(T)), basis)
            op_matrix(lambda f: vf_apply(f, dright_delta(T)), basis)
        return (
            True,
            "dL(T_a) W and dR(T_a) W lie in W for a = 1..3 (every basis image is expressible)",
        )

    def v2b():
        bad = [
            a
            for a, T in enumerate(TGEN)
            if not meq(op_matrix(lambda f: vf_apply(f, dleft_delta(T)), basis), DL[a])
        ]
        return not bad, f"claimed dL matrices equal recomputed ones; mismatching a: {bad}"

    def v2c():
        bad = [
            a
            for a, T in enumerate(TGEN)
            if not meq(op_matrix(lambda f: vf_apply(f, dright_delta(T)), basis), DR[a])
        ]
        return not bad, f"claimed dR matrices equal recomputed ones; mismatching a: {bad}"

    for e in ge:
        if len(e["quaternion"]) != 5 or any(pint(x) != x for x in e["quaternion"]):
            raise ValueError("quaternion must be five integers")
    elems = [su2_from_quat(e["quaternion"]) for e in ge]

    def lmat(h):
        sub = left_sub(mdag(h))
        return op_matrix(lambda f: psubs(f, sub), basis)

    def rmat(k):
        sub = right_sub(k)
        return op_matrix(lambda f: psubs(f, sub), basis)

    def v3a():
        bad = [
            i
            for i, h in enumerate(elems)
            if not meq(lmat(h), pmat(ge[i]["L_matrix"], 4))
        ]
        return not bad, f"{len(elems)} group elements; L_h matrix mismatches at {bad}"

    def v3b():
        bad = [
            i
            for i, h in enumerate(elems)
            if not meq(rmat(h), pmat(ge[i]["R_matrix"], 4))
        ]
        return not bad, f"{len(elems)} group elements; R_k matrix mismatches at {bad}"

    def v3c():
        bad = []
        for i, j in pairs:
            hp = mm(elems[i], elems[j])
            if hp == mm(elems[j], elems[i]):
                bad.append((i, j, "pair commutes: not a discriminating pair"))
                continue
            if not meq(lmat(hp), mm(lmat(elems[i]), lmat(elems[j]))):
                bad.append((i, j, "L"))
            if not meq(rmat(hp), mm(rmat(elems[i]), rmat(elems[j]))):
                bad.append((i, j, "R"))
        return (
            not bad,
            f"L_(hh') = L_h L_h' and R_(kk') = R_k R_k' on non-commuting pairs; bad: {bad}",
        )

    def v3d():
        bad = [
            (i, j)
            for i in range(len(elems))
            for j in range(len(elems))
            if not meq(mm(lmat(elems[i]), rmat(elems[j])), mm(rmat(elems[j]), lmat(elems[i])))
        ]
        return not bad, f"L_h and R_k commute for all {len(elems)}^2 pairs; bad: {bad[:3]}"

    def v3e():
        bad = []
        for i, h in enumerate(elems):
            hinv = mdag(h)
            ML = pmat(ge[i]["L_matrix"], 4)
            MR = pmat(ge[i]["R_matrix"], 4)
            EL = [[ZERO] * 4 for _ in range(4)]
            ER = [[ZERO] * 4 for _ in range(4)]
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        EL[2 * c + b][2 * a + b] = hinv[a][c]  # L_h g_ab = sum_c (h^-1)_ac g_cb
                        ER[2 * a + c][2 * a + b] = h[c][b]  # R_k g_ab = sum_c g_ac k_cb
            if not meq(ML, EL):
                bad.append((i, "L closed form"))
            if not meq(MR, ER):
                bad.append((i, "R closed form"))
            for a, T in enumerate(TGEN):
                hT = mm(mm(h, T), hinv)
                DLp = op_matrix(lambda f: vf_apply(f, dleft_delta(hT)), basis)
                DRp = op_matrix(lambda f: vf_apply(f, dright_delta(hT)), basis)
                if not meq(mm(ML, DL[a]), mm(DLp, ML)):
                    bad.append((i, a, "L equivariance"))
                if not meq(mm(MR, DR[a]), mm(DRp, MR)):
                    bad.append((i, a, "R equivariance"))
        return not bad, (
            "claimed group matrices equal the closed forms (h^-1)_ac and k_cb, and satisfy "
            f"L_h dL(T) = dL(hTh^-1) L_h, R_k dR(T) = dR(kTk^-1) R_k; violations: {bad[:4]}"
        )

    def v4():
        bad = []
        for name, D in (("dL", DL), ("dR", DR)):
            for (a, b, c), s in EPS_LC.items():
                if not meq(mcomm(D[a], D[b]), msc(D[c], s)):
                    bad.append((name, a, b, c))
        for a in range(3):
            for b in range(3):
                if not meq(mcomm(DL[a], DR[b]), msc(meye(4), 0)):
                    bad.append(("dL-dR", a, b))
        return (
            not bad,
            f"[X_a,X_b] = eps_abc X_c for dL and dR, [dL_a,dR_b] = 0; violations: {bad[:4]}",
        )

    LB, RB = dec["left_blocks"], dec["right_blocks"]

    def blocks_ok(B):
        return (
            isinstance(B, list)
            and len(B) == 2
            and all(isinstance(b, list) and len(b) == 2 and all(type(i) is int for i in b) for b in B)
        )

    def v5a():
        if not (blocks_ok(LB) and blocks_ok(RB)):
            return False, "left_blocks and right_blocks must each be two lists of two integer indices"
        okp = sorted(i for blk in LB for i in blk) == [0, 1, 2, 3]
        okp &= sorted(i for blk in RB for i in blk) == [0, 1, 2, 3]
        inv = True
        for D in DL:
            for S in LB:
                inv &= all(D[i][j].zero() for j in S for i in range(4) if i not in S)
        for D in DR:
            for S in RB:
                inv &= all(D[i][j].zero() for j in S for i in range(4) if i not in S)
        return (
            okp and inv,
            f"partition ok: {okp}; blocks invariant under dL (left_blocks) and dR (right_blocks): {inv}",
        )

    def v5b():
        r0 = [restrict(D, LB[0]) for D in DL]
        r1 = [restrict(D, LB[1]) for D in DL]
        iso = all(meq(a, b) for a, b in zip(r0, r1))
        c_blk = commutant_dim(r0, 2)
        q0 = [restrict(D, RB[0]) for D in DR]
        q1 = [restrict(D, RB[1]) for D in DR]
        iso_r = all(meq(a, b) for a, b in zip(q0, q1))
        c_blk_r = commutant_dim(q0, 2)
        want = dec["commutant_dim"]
        ok = iso and iso_r and c_blk == 1 and c_blk_r == 1
        ok = ok and type(want["left_block"]) is int and want["left_block"] == 1
        ok = ok and type(want["right_block"]) is int and want["right_block"] == 1
        return ok, (
            f"two left doublets have identical generator matrices (isomorphic): {iso}; "
            f"two right doublets likewise: {iso_r}; "
            f"commutant dim of a left block {c_blk}, of a right block {c_blk_r} (1 = irreducible)"
        )

    def v5c():
        full = commutant_dim(DL + DR, 4)
        left = commutant_dim(DL, 4)
        right = commutant_dim(DR, 4)
        want = dec["commutant_dim"]
        claimed = (want["full_LR"], want["left_only"], want["right_only"])
        ok = (full, left, right) == (1, 4, 4) and all(type(x) is int for x in claimed)
        ok = ok and claimed == (1, 4, 4)
        return (
            ok,
            f"commutant dims: full L+R {full}, L only {left}, R only {right} (expected 1, 4, 4)",
        )

    def v6():
        cas = []
        for D in (DL, DR):
            tot = msc(meye(4), 0)
            for a in range(3):
                J = msc(D[a], IU)
                tot = madd(tot, mm(J, J))
            cas.append(tot)
        want = msc(meye(4), Gq(F(3, 4)))
        okc = meq(cas[0], want) and meq(cas[1], want)
        okc &= dec["casimir_L"] == "3/4" == dec["casimir_R"]
        j3l, j3r = msc(DL[2], IU), msc(DR[2], IU)
        diag = all(
            (j3l[i][j].zero() and j3r[i][j].zero()) for i in range(4) for j in range(4) if i != j
        )
        wts = [(j3l[i][i], j3r[i][i]) for i in range(4)]
        wc = dec["weights_J3L_J3R"]
        if not isinstance(wc, list) or len(wc) != 4 or any(len(p) != 2 for p in wc):
            return False, "weights_J3L_J3R must list exactly 4 pairs"
        claim = [(Gq(pq(a)), Gq(pq(b))) for a, b in wc]
        okw = diag and all(w[0] == c[0] and w[1] == c[1] for w, c in zip(wts, claim))
        pairs = {(w[0].re, w[1].re) for w in wts}
        okw &= pairs == {(F(s1, 2), F(s2, 2)) for s1 in (1, -1) for s2 in (1, -1)}
        return okc and okw, (
            f"Casimirs J_L^2 = J_R^2 = 3/4 * identity: {okc}; (J3L, J3R) weights diagonal and "
            f"equal to the claim, each of (+-1/2, +-1/2) exactly once: {okw}"
        )

    def v7():
        def inner(f, g):
            tot = ZERO
            for m1, c1 in f.items():
                for m2, c2 in g.items():
                    m = tuple(a + b for a, b in zip((m1[2], m1[3], m1[0], m1[1]), m2))
                    if sum(m) != 2:
                        raise ValueError("Gram check supports degree-1 elements only")
                    if m in ((1, 0, 1, 0), (0, 1, 0, 1)):
                        tot = tot + c1.conj() * c2 * F(1, 2)
            return tot

        G = [[inner(basis[i], basis[j]) for j in range(4)] for i in range(4)]
        okg = all(G[i][j] == (F(1, 2) if i == j else 0) for i in range(4) for j in range(4))
        gm = cert["gram"]
        if not isinstance(gm, list) or len(gm) != 4 or any(len(r) != 4 for r in gm):
            return False, "gram must be a 4x4 list"
        okg &= all(pg([x, "0"]) == G[i][j] for i, row in enumerate(gm) for j, x in enumerate(row))
        skew = all(meq(madd(mm(mdag(A), G), mm(G, A)), msc(meye(4), 0)) for A in DL + DR)
        return okg and skew, (
            f"Gram <g_ab, g_cd> = (1/2) delta (uniform measure, E[x_i conj(x_j)] = delta_ij/2, i.e. E[u_k u_l] = delta_kl/4 for real coordinates): {okg}; "
            f"all six generators skew-Hermitian w.r.t. it (unitary action): {skew}"
        )

    def v8():
        eps = pmat(dec["epsilon"], 2)
        einv = [[ZERO, -ONE], [ONE, ZERO]]
        ok = meq(mm(eps, einv), meye(2))
        conj_ok = all(meq(mm(mm(eps, T), einv), mconj(T)) for T in TGEN)
        conj_ok &= all(meq(mm(mm(eps, h), einv), mconj(h)) for h in elems)
        lb = all(meq(restrict(DL[a], LB[0]), mconj(TGEN[a])) for a in range(3))
        lb = lb and all(meq(restrict(DL[a], LB[1]), mconj(TGEN[a])) for a in range(3))
        rb = all(meq(restrict(DR[a], RB[b]), TGEN[a]) for a in range(3) for b in range(2))
        return ok and conj_ok and lb and rb, (
            f"eps T eps^-1 = conj(T) for all T_a and sampled h: {conj_ok}; left doublet block = "
            f"conj(T_a) (conjugate of the defining rep, equivalent via eps): {lb}; right block = T_a: {rb}"
        )

    for cid, fn in (
        ("V0_statement", v0),
        ("V1_basis_definition", v1),
        ("V2gen_generators", v2gen),
        ("V2a_closure", v2a),
        ("V2b_dL_matrices", v2b),
        ("V2c_dR_matrices", v2c),
        ("V3a_group_L", v3a),
        ("V3b_group_R", v3b),
        ("V3c_homomorphism", v3c),
        ("V3d_L_R_commute", v3d),
        ("V3e_convention_equivariance", v3e),
        ("V4_algebra", v4),
        ("V5a_invariant_blocks", v5a),
        ("V5b_doublets_irreducible", v5b),
        ("V5c_commutants", v5c),
        ("V6_casimir_weights", v6),
        ("V7_gram_unitarity", v7),
        ("V8_conjugate_equivalence", v8),
    ):
        check(cid, fn, skip)


def main(argv):
    if len(argv) < 2:
        print("usage: verifier.py certificate.json [--skip-checks ID,ID]")
        return 2
    skip = set()
    if "--skip-checks" in argv:
        skip = set(argv[argv.index("--skip-checks") + 1].split(","))
    try:
        with open(argv[1], encoding="utf-8") as fh:
            cert = json.load(fh)
        run(cert, skip)
    except (OSError, ValueError, KeyError, IndexError, TypeError, ZeroDivisionError) as e:
        print(f"MALFORMED: {type(e).__name__}: {e}")
        return 2
    for cid, ok, msg in RESULTS:
        tag = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print(f"{tag} {cid}: {msg}")
    failed = [cid for cid, ok, _ in RESULTS if ok is False]
    ran = sum(1 for _, ok, _ in RESULTS if ok is not None)
    if failed:
        print(f"RESULT: REJECT ({len(failed)} failed of {ran}): {','.join(failed)}")
        return 1
    print(f"RESULT: ACCEPT ({ran} checks passed, {len(RESULTS) - ran} skipped)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
