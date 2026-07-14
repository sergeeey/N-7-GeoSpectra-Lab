"""
Round 59 — Route B: consistency + completeness audit of the ORIGINAL
trivial-block rank computation (experiments/20260708-dolan-casimir-g2su3).

Unlike the parallel from-scratch Route A, this script IS allowed to import
from the original modules. Its job is to close two gaps left by the original
work and to self-consistency-check the rank(D+|_trivial)=1 claim:

  GAP 1 (completeness): g2su3_find_invariant.py searched ONLY the 9-dim block
        span{y1,y2,y3} (x) span{y12,y13,y23}. Here we enumerate SU(3)-invariants
        over the FULL 64-dim fibre Sigma (x) Sigma (Sigma = Lambda^bullet(C^3),
        8-dim), restricted to the two physically relevant chirality blocks:
          (a) Sigma_odd (x) Sigma_even   = S+ (x) S-   (domain)
          (b) Sigma_even (x) Sigma_even  = S- (x) S-   (target)
        odd  = span{y1,y2,y3,y123}, even = span{1,y12,y13,y23}.
        Framing is intact iff dim(a)=2 and dim(b)=1.

  GAP 2 (self-consistency): orthonormal-basis matrix elements a,b and the
        certificate s=|a|^2+|b|^2; target-complement residual; Hermiticity
        <w_hat, D u_i> = conj(<u_i, D w_hat>); basis-rotation invariance of s.

All arithmetic is exact (sympy). Every check has an explicit FAIL signature
(no tautologies): dims can come out != (2,1); <v_a,v_b> can come out != 0;
residual can be nonzero; the two Hermiticity sides can differ; s can change
under rotation. If any fires, the script says so.

Run: python round59_route_b_consistency.py
"""

import os
import sys

import sympy as sp

# ---- import the ORIGINAL modules (allowed for Route B) --------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_ORIG = os.path.abspath(os.path.join(_HERE, "..", "20260708-dolan-casimir-g2su3"))
if _ORIG not in sys.path:
    sys.path.insert(0, _ORIG)

from g2su3_explicit_clifford import DIM, SUBSETS, IDX, vec_from_subsets  # noqa: E402
from g2su3_twisted_kernel import su3_action  # noqa: E402
from g2su3_compute_crossterm import D_on_simple_tensor  # noqa: E402

sqrt = sp.sqrt
assert DIM == 8, f"expected 8-dim Sigma, got {DIM}"

# ---------------------------------------------------------------------------
# 64-dim fibre bookkeeping. index(sL,sR) = 8*IDX[sL] + IDX[sR].
# ---------------------------------------------------------------------------
N = DIM * DIM  # 64


def fidx(sL, sR):
    return DIM * IDX[sL] + IDX[sR]


# chirality split of Sigma (grade parity)
ODD_SUBSETS = [(1,), (2,), (3,), (1, 2, 3)]  # S+ : span{y1,y2,y3,y123}
EVEN_SUBSETS = [(), (1, 2), (1, 3), (2, 3)]  # S- : span{1,y12,y13,y23}
ODD_IDX = [IDX[s] for s in ODD_SUBSETS]
EVEN_IDX = [IDX[s] for s in EVEN_SUBSETS]


def herm(x, y):
    """Standard Hermitian inner product on the 64 fibre coords, CONJUGATING
    the FIRST argument: <x,y> = sum_k conj(x_k) y_k."""
    return sp.expand(sum(sp.conjugate(x[k]) * y[k] for k in range(N)))


def vec64_from_pairs(pairs):
    """pairs: dict {(sL, sR): coeff} -> 64-dim sympy column."""
    v = sp.zeros(N, 1)
    for (sL, sR), c in pairs.items():
        v[fidx(sL, sR)] += c
    return v


# ---------------------------------------------------------------------------
# su(3) generator matrices on Sigma (8x8), then Leibniz action on 64-dim fibre.
# ---------------------------------------------------------------------------
def su3_matrix_on_sigma(i):
    """8x8 matrix M with M[t, a] = <e_t | nu_i . e_a>, columns = basis order."""
    cols = []
    for s in SUBSETS:
        cols.append(su3_action(i, vec_from_subsets({s: 1})))
    M = sp.Matrix.hstack(*cols)
    return sp.simplify(M)


def leibniz64(M):
    """Leibniz action of a single su(3) generator on Sigma (x) Sigma:
    nu.(e_a (x) e_b) = (nu.e_a)(x)e_b + e_a(x)(nu.e_b).  Returns 64x64."""
    L = sp.zeros(N, N)
    for a in range(DIM):
        for b in range(DIM):
            col = DIM * a + b
            for t in range(DIM):
                mta = M[t, a]
                if mta != 0:
                    L[DIM * t + b, col] += mta
            for u in range(DIM):
                mub = M[u, b]
                if mub != 0:
                    L[DIM * a + u, col] += mub
    return L


def common_nullspace_in_block(Lmats, block_idx):
    """Common nullspace of all generators, restricted to a chirality block.
    block_idx: list of 64-indices spanning the block. Returns (dim, basis_vecs
    as full 64-dim columns). Also verifies the block is su(3)-invariant (no
    leakage) so restricting to the sub-block is legitimate."""
    # invariance check: for each generator, columns in block must have zero
    # entries in rows OUTSIDE the block.
    block_set = set(block_idx)
    for L in Lmats:
        for col in block_idx:
            for row in range(N):
                if row not in block_set and L[row, col] != 0:
                    raise AssertionError(
                        f"su(3) does NOT preserve block (leak at row {row}, col {col})"
                    )
    # stack restricted matrices and take nullspace in block coords
    subs = [L[block_idx, block_idx] for L in Lmats]
    big = sp.Matrix.vstack(*subs)
    ns_block = big.nullspace()
    # lift each block-coord nullvector back to full 64-dim
    full = []
    for nv in ns_block:
        f = sp.zeros(N, 1)
        for pos, gi in enumerate(block_idx):
            f[gi] = sp.simplify(nv[pos])
        full.append(f)
    return len(ns_block), full


def in_span(target, basis_cols):
    """True iff `target` (64-col) lies in span(basis_cols)."""
    if not basis_cols:
        return all(sp.simplify(x) == 0 for x in target)
    B = sp.Matrix.hstack(*basis_cols)
    r_before = B.rank()
    r_after = sp.Matrix.hstack(B, target).rank()
    return r_before == r_after


# ---------------------------------------------------------------------------
# General twisted-Dirac operator on the FULL 64-dim fibre, built by summing
# the original D_on_simple_tensor over simple-tensor components (rigorous;
# no linearity assumption is smuggled in — every input is decomposed into
# simple tensors and D is applied component-wise, which IS the operator).
# ---------------------------------------------------------------------------
_D_cache = {}


def _D_simple(sL, sR):
    key = (sL, sR)
    if key not in _D_cache:
        d = D_on_simple_tensor(vec_from_subsets({sL: 1}), vec_from_subsets({sR: 1}))
        _D_cache[key] = d
    return _D_cache[key]


def D_full(vec):
    """Apply the twisted Dirac operator to an arbitrary 64-dim fibre vector."""
    out = sp.zeros(N, 1)
    for sL in SUBSETS:
        for sR in SUBSETS:
            c = vec[fidx(sL, sR)]
            if c == 0:
                continue
            for (tL, tR), cc in _D_simple(sL, sR).items():
                out[fidx(tL, tR)] += c * cc
    return sp.Matrix([sp.simplify(x) for x in out])


def fmt_support(vec, tol_zero=True):
    """Human string of nonzero (sL,sR):coeff components of a 64-vec."""
    parts = []
    for sL in SUBSETS:
        for sR in SUBSETS:
            c = sp.simplify(vec[fidx(sL, sR)])
            if c != 0:
                nL = "1" if sL == () else "y" + "".join(map(str, sL))
                nR = "1" if sR == () else "y" + "".join(map(str, sR))
                parts.append(f"{nL}(x){nR}:{c}")
    return "{" + ", ".join(parts) + "}" if parts else "{0}"


def main():
    report = {}
    print("=" * 74)
    print("ROUND 59 — ROUTE B: full-fibre completeness + self-consistency audit")
    print("=" * 74)

    # -- build su(3) Leibniz matrices on the 64-dim fibre --------------------
    print("\n[0] Building su(3) Leibniz action on the 64-dim fibre Sigma(x)Sigma ...")
    Mgen = [su3_matrix_on_sigma(i) for i in range(1, 9)]
    Lmats = [leibniz64(M) for M in Mgen]
    print("    8 generators lifted to 64x64 (Leibniz). done.")

    # ======================================================================
    # STEP 1 — FULL-FIBRE INVARIANT ENUMERATION (completeness gap closure)
    # ======================================================================
    print("\n" + "-" * 74)
    print("[1] FULL-FIBRE SU(3)-invariant enumeration per chirality block")
    print("-" * 74)

    block_a_idx = [DIM * a + b for a in ODD_IDX for b in EVEN_IDX]  # S+ (x) S-
    block_b_idx = [DIM * a + b for a in EVEN_IDX for b in EVEN_IDX]  # S- (x) S-

    dim_a, ns_a = common_nullspace_in_block(Lmats, block_a_idx)
    dim_b, ns_b = common_nullspace_in_block(Lmats, block_b_idx)
    print(f"    block (a) Sigma_odd (x) Sigma_even  [S+ (x) S-] : dim invariants = {dim_a}")
    print(f"    block (b) Sigma_even (x) Sigma_even [S- (x) S-] : dim invariants = {dim_b}")

    # reference vectors from the original claim
    v_a = vec64_from_pairs({((1,), (2, 3)): 1, ((2,), (1, 3)): -1, ((3,), (1, 2)): 1})
    v_b = vec64_from_pairs({((1, 2, 3), ()): 1})
    w = vec64_from_pairs({((), ()): 1})

    match_a = in_span(v_a, ns_a) and in_span(v_b, ns_a) and dim_a == 2
    match_b = in_span(w, ns_b) and dim_b == 1
    print(f"    nullspace(a) == span(v_a, v_b) ? {match_a}")
    print(f"    nullspace(b) == span(w)        ? {match_b}")

    framing_ok = (dim_a == 2) and (dim_b == 1)
    report["dim_a"] = dim_a
    report["dim_b"] = dim_b
    report["match_a"] = match_a
    report["match_b"] = match_b
    report["framing_ok"] = framing_ok
    if not framing_ok:
        print("    *** FRAMING-COLLAPSE: block structure is NOT (2 -> 1). ***")
    else:
        print("    framing intact: (domain 2) -> (target 1).")

    # ======================================================================
    # STEP 2 — ORTHONORMALIZE + certificate s
    # ======================================================================
    print("\n" + "-" * 74)
    print("[2] Orthonormalize domain, compute a,b,s")
    print("-" * 74)

    ip_ab = herm(v_a, v_b)
    print(f"    <v_a, v_b> = {ip_ab}  (expected 0; if nonzero, Gram-Schmidt needed)")
    report["ip_va_vb"] = str(ip_ab)

    nrm_va = sp.sqrt(sp.simplify(herm(v_a, v_a)))
    nrm_vb = sp.sqrt(sp.simplify(herm(v_b, v_b)))
    nrm_w = sp.sqrt(sp.simplify(herm(w, w)))
    print(f"    ||v_a|| = {nrm_va}   ||v_b|| = {nrm_vb}   ||w|| = {nrm_w}")

    u1 = sp.Matrix([sp.simplify(x / nrm_va) for x in v_a])
    u2 = sp.Matrix([sp.simplify(x / nrm_vb) for x in v_b])
    w_hat = sp.Matrix([sp.simplify(x / nrm_w) for x in w])

    Du1 = D_full(u1)
    Du2 = D_full(u2)
    print(f"    D u1 = {fmt_support(Du1)}")
    print(f"    D u2 = {fmt_support(Du2)}")

    a = sp.simplify(herm(w_hat, Du1))
    b = sp.simplify(herm(w_hat, Du2))
    s = sp.simplify(a * sp.conjugate(a) + b * sp.conjugate(b))
    print(f"\n    a = <w_hat, D u1> = {a}")
    print(f"    b = <w_hat, D u2> = {b}")
    print(f"    s = |a|^2 + |b|^2 = {s}")
    report["a"] = str(a)
    report["b"] = str(b)
    report["s"] = str(s)

    # ======================================================================
    # STEP 3 — target-complement residual (over ALL 64 coords)
    # ======================================================================
    print("\n" + "-" * 74)
    print("[3] Residual (1 - P_target) D u_i over ALL 64 fibre coords")
    print("-" * 74)
    # P_target projects onto span(w_hat); w_hat is unit-norm.
    resid1 = sp.Matrix([sp.simplify(x) for x in (Du1 - herm(w_hat, Du1) * w_hat)])
    resid2 = sp.Matrix([sp.simplify(x) for x in (Du2 - herm(w_hat, Du2) * w_hat)])
    r1_zero = all(sp.simplify(x) == 0 for x in resid1)
    r2_zero = all(sp.simplify(x) == 0 for x in resid2)
    print(f"    (1-P) D u1 == 0 over 64 coords ? {r1_zero}   support={fmt_support(resid1)}")
    print(f"    (1-P) D u2 == 0 over 64 coords ? {r2_zero}   support={fmt_support(resid2)}")
    residual_ok = r1_zero and r2_zero
    report["residual_ok"] = residual_ok

    # ======================================================================
    # STEP 4 — Hermiticity / adjoint:  <w_hat, D u_i> = conj(<u_i, D w_hat>)
    # ======================================================================
    print("\n" + "-" * 74)
    print("[4] Hermiticity / adjoint consistency  D- = (D+)^dagger")
    print("-" * 74)
    Dw = D_full(w_hat)
    print(f"    D w_hat = {fmt_support(Dw)}")
    # project D w_hat onto domain invariants (u1,u2 orthonormal)
    c1 = sp.simplify(herm(u1, Dw))
    c2 = sp.simplify(herm(u2, Dw))
    proj = sp.Matrix([sp.simplify(x) for x in (c1 * u1 + c2 * u2)])
    resid_dom = sp.Matrix([sp.simplify(x) for x in (Dw - proj)])
    dw_in_domain = all(sp.simplify(x) == 0 for x in resid_dom)
    print(f"    <u1, D w_hat> = {c1}")
    print(f"    <u2, D w_hat> = {c2}")
    print(f"    D w_hat lies in span(u1,u2) ? {dw_in_domain}  (residual {fmt_support(resid_dom)})")
    herm1 = sp.simplify(a - sp.conjugate(c1))
    herm2 = sp.simplify(b - sp.conjugate(c2))
    h1_ok = herm1 == 0
    h2_ok = herm2 == 0
    print(f"    check i=1: <w_hat,D u1> - conj(<u1,D w_hat>) = {herm1}  -> {h1_ok}")
    print(f"    check i=2: <w_hat,D u2> - conj(<u2,D w_hat>) = {herm2}  -> {h2_ok}")
    herm_ok = h1_ok and h2_ok
    report["hermiticity_c1"] = str(c1)
    report["hermiticity_c2"] = str(c2)
    report["herm_ok"] = herm_ok

    # ======================================================================
    # STEP 5 — basis-rotation invariance of s
    # ======================================================================
    print("\n" + "-" * 74)
    print("[5] Basis-rotation invariance of s")
    print("-" * 74)

    def s_after_rotation(U):
        # rotated orthonormal domain basis: u_j' = sum_k U[k,j] u_k
        u1p = sp.Matrix([sp.simplify(x) for x in (U[0, 0] * u1 + U[1, 0] * u2)])
        u2p = sp.Matrix([sp.simplify(x) for x in (U[0, 1] * u1 + U[1, 1] * u2)])
        Du1p = D_full(u1p)
        Du2p = D_full(u2p)
        ap = sp.simplify(herm(w_hat, Du1p))
        bp = sp.simplify(herm(w_hat, Du2p))
        # sanity: rotated basis still orthonormal
        on = (
            sp.simplify(herm(u1p, u1p) - 1) == 0
            and sp.simplify(herm(u2p, u2p) - 1) == 0
            and sp.simplify(herm(u1p, u2p)) == 0
        )
        return sp.simplify(ap * sp.conjugate(ap) + bp * sp.conjugate(bp)), ap, bp, on

    c35, s45 = sp.Rational(3, 5), sp.Rational(4, 5)
    U_real = sp.Matrix([[c35, -s45], [s45, c35]])
    s_real, ar, br, on_r = s_after_rotation(U_real)
    print(f"    real rotation c=3/5,s=4/5 : orthonormal={on_r}  a'={ar}  b'={br}  s'={s_real}")

    # complex unitary: [[3/5, 4i/5],[4i/5, 3/5]]  (columns orthonormal)
    IU = sp.I
    U_cplx = sp.Matrix([[c35, s45 * IU], [s45 * IU, c35]])
    # verify unitary
    U_is_unitary = sp.simplify(U_cplx.conjugate().T * U_cplx - sp.eye(2)) == sp.zeros(2, 2)
    s_cplx, ac, bc, on_c = s_after_rotation(U_cplx)
    print(f"    cplx rotation [[3/5,4i/5],[4i/5,3/5]] unitary={U_is_unitary} orthonormal={on_c}")
    print(f"        a'={ac}  b'={bc}  s'={s_cplx}")

    rot_ok = (sp.simplify(s_real - s) == 0) and (sp.simplify(s_cplx - s) == 0)
    print(f"    s invariant under both rotations ? {rot_ok}")
    report["s_real"] = str(s_real)
    report["s_cplx"] = str(s_cplx)
    report["rot_ok"] = rot_ok

    # ======================================================================
    # SUMMARY
    # ======================================================================
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    verdict = "PASS"
    if not framing_ok:
        verdict = "FRAMING-COLLAPSE"
    elif not herm_ok:
        verdict = "HERMITICITY-FAIL"
    print(f"  full-fibre dims (domain,target) = ({dim_a},{dim_b})  [expected (2,1)]")
    print(f"  nullspaces match span(v_a,v_b)/span(w) = {match_a}/{match_b}")
    print(f"  <v_a,v_b> = {ip_ab}")
    print(f"  a = {a}   b = {b}   s = {s}")
    print(f"  residual (1-P)D u_i = 0 : {residual_ok}")
    print(f"  Hermiticity <w,Du_i>=conj(<u_i,Dw>) : {herm_ok}")
    print(f"  s rotation-invariant (real+complex) : {rot_ok}")
    print(f"\n  VERDICT: {verdict}")
    report["verdict"] = verdict
    print("\nMACHINE_REPORT " + repr(report))
    return report


if __name__ == "__main__":
    main()
