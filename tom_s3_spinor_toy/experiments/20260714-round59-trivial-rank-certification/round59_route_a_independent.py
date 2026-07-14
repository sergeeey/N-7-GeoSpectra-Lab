"""
Round 59 - Route A: INDEPENDENT from-scratch certification of the trivial-component
rank of a twisted Dirac operator on S^6 = G_2/SU(3).

Primary source (re-transcribed here directly, NOT copied from any prior code):
  Agricola, Hofmann, Lawn 2023, "Invariant spinors on homogeneous spheres",
  arXiv:2203.02961v3.
    - Section 2.1 (pages 5-7): Lagrangian-subspace spin representation, eq. (5).
    - Section 5.1 (page 42): S^6 = G_2/SU(3), Theorem 5.1, Remark 5.2.
    - Example 4.18 (page 27): confirms spin-lift tilde(e_{a,b}) = (1/2) e_a . e_b.

Exact arithmetic only (sympy).  No floats.
"""

import sympy as sp

IU = sp.I
sqrt3 = sp.sqrt(3)

# ---------------------------------------------------------------------------
# Spinor module Sigma = Lambda^bullet L',  L' = span_C{y1,y2,y3}.
# Basis indexed by sorted subsets of {1,2,3}, dim = 8.
# ---------------------------------------------------------------------------
SUBSETS = [
    (),  # 0 : 1            deg 0  (even)
    (1,),  # 1 : y1           deg 1  (odd)
    (2,),  # 2 : y2           deg 1  (odd)
    (3,),  # 3 : y3           deg 1  (odd)
    (1, 2),  # 4 : y1^y2        deg 2  (even)
    (1, 3),  # 5 : y1^y3        deg 2  (even)
    (2, 3),  # 6 : y2^y3        deg 2  (even)
    (1, 2, 3),  # 7 : y1^y2^y3     deg 3  (odd)
]
IDX = {s: k for k, s in enumerate(SUBSETS)}
EVEN_IDX = [k for k, s in enumerate(SUBSETS) if len(s) % 2 == 0]  # {0,4,5,6}
ODD_IDX = [k for k, s in enumerate(SUBSETS) if len(s) % 2 == 1]  # {1,2,3,7}


def wedge(j, S):
    """y_j ^ (y_S) -> (coeff, newS) or None if it vanishes."""
    if j in S:
        return None
    newS = tuple(sorted(S + (j,)))
    sign = (-1) ** sum(1 for a in S if a < j)
    return sign, newS


def interior(j, S):
    """x_j _| (y_S) with beta(x_j,y_k)=delta_{jk}  ->  (coeff,newS) or None."""
    if j not in S:
        return None
    a = sorted(S).index(j)  # 0-based position
    sign = (-1) ** a
    newS = tuple(x for x in S if x != j)
    return sign, newS


def op_from_action(action):
    """Build an 8x8 sympy matrix from a function action(S)->list of (coeff,newS)."""
    M = sp.zeros(8, 8)
    for col, S in enumerate(SUBSETS):
        for coeff, newS in action(S):
            M[IDX[newS], col] += coeff
    return M


def clifford_action(k, conj=False):
    """Clifford action of real orthonormal basis vector e_k (k in 1..6), eq.(5).
    e_{2j-1}.eta = i (x_j _| eta + y_j ^ eta)
    e_{2j}.eta   = y_j ^ eta - x_j _| eta
    conj=True applies global complex conjugation i -> -i.
    """
    ii = -IU if conj else IU

    def action(S):
        out = []
        if k % 2 == 1:
            j = (k + 1) // 2
            r = interior(j, S)
            if r:
                out.append((ii * r[0], r[1]))
            w = wedge(j, S)
            if w:
                out.append((ii * w[0], w[1]))
        else:
            j = k // 2
            w = wedge(j, S)
            if w:
                out.append((w[0], w[1]))
            r = interior(j, S)
            if r:
                out.append((-r[0], r[1]))
        return out

    return op_from_action(action)


def build_clifford(conj=False):
    return {k: clifford_action(k, conj=conj) for k in range(1, 7)}


def spin_lift(bivec_terms, E):
    """bivec_terms: list of (coeff, a, b) meaning coeff * e_{a,b}.
    Returns spin operator = sum coeff * (1/2) E[a] E[b]  (8x8 matrix)."""
    M = sp.zeros(8, 8)
    for coeff, a, b in bivec_terms:
        M += coeff * sp.Rational(1, 2) * (E[a] * E[b])
    return M


# ---------------------------------------------------------------------------
# Nomizu / Levi-Civita map  Lambda^g(e_i)   (Remark 5.2, page 42)
#   coefficient 1/(2 sqrt3) throughout
# ---------------------------------------------------------------------------
c = sp.Rational(1, 2) / sqrt3  # 1/(2 sqrt3)
NOMIZU = {
    1: [(c, 3, 6), (c, 4, 5)],
    2: [(c, 3, 5), (-c, 4, 6)],
    3: [(-c, 1, 6), (-c, 2, 5)],
    4: [(-c, 1, 5), (c, 2, 6)],
    5: [(c, 1, 4), (c, 2, 3)],
    6: [(c, 1, 3), (-c, 2, 4)],
}

# su(3) isotropy generators ad(nu_i)|m  (Remark 5.2, page 42)
h = sp.Rational(1, 2)
hs = sp.Rational(1, 2) / sqrt3  # 1/(2 sqrt3)
ADNU = {
    1: [(h, 1, 2), (-h, 3, 4)],
    2: [(h, 3, 5), (h, 4, 6)],
    3: [(-h, 3, 6), (h, 4, 5)],
    4: [(h, 1, 6), (-h, 2, 5)],
    5: [(-h, 1, 5), (-h, 2, 6)],
    6: [(-h, 1, 4), (h, 2, 3)],
    7: [(h, 1, 3), (h, 2, 4)],
    8: [(-hs, 1, 2), (-hs, 3, 4), (2 * hs, 5, 6)],
}


def vec(*coeffs):
    """Build an 8-vector from index:coeff pairs given as a dict-like list."""
    v = sp.zeros(8, 1)
    for k, val in coeffs:
        v[k] = val
    return v


def psi_plus():
    v = sp.zeros(8, 1)
    v[IDX[()]] = 1
    v[IDX[(1, 2, 3)]] = 1
    return v


def psi_minus():
    v = sp.zeros(8, 1)
    v[IDX[()]] = 1
    v[IDX[(1, 2, 3)]] = -1
    return v


# ---------------------------------------------------------------------------
# CALIBRATION GATE
# nabla^g_{e_i} psi_pm = +-(1/(2 sqrt3)) e_i . psi_pm  for all i=1..6
# ---------------------------------------------------------------------------
def run_calibration(E, nomizu, conj=False, killing_sign=+1):
    """killing_sign = +1 anchors on psi_+ branch (constant +1/(2 sqrt3));
    -1 anchors on psi_- branch (mirrored constant)."""
    kappa = sp.Rational(1, 2) / sqrt3
    results = []
    ok = True
    for branch_sign, psi in [(+1, psi_plus()), (-1, psi_minus())]:
        for i in range(1, 7):
            lhs = spin_lift(nomizu[i], E) * psi  # nabla_{e_i} psi
            rhs = branch_sign * kappa * (E[i] * psi)  # +-(1/2sqrt3) e_i.psi
            diff = sp.simplify(lhs - rhs)
            zero = all(sp.simplify(x) == 0 for x in diff)
            results.append((branch_sign, i, zero))
            if not zero:
                ok = False
    return ok, results


# ---------------------------------------------------------------------------
# Hermitian helpers
# ---------------------------------------------------------------------------
def hip(a, b):
    """Standard Hermitian inner product <a,b> = sum conj(a_k) b_k."""
    s = 0
    for k in range(a.rows):
        s += sp.conjugate(a[k]) * b[k]
    return sp.simplify(sp.expand(s))


def hnorm2(a):
    return hip(a, a)


def gram_schmidt(vectors):
    """Hermitian Gram-Schmidt -> orthonormal list (exact)."""
    out = []
    for v in vectors:
        w = v
        for u in out:
            w = w - hip(u, v) * u
        w = sp.Matrix([sp.simplify(x) for x in w])
        n2 = hnorm2(w)
        n = sp.sqrt(n2)
        w = sp.Matrix([sp.simplify(x / n) for x in w])
        out.append(w)
    return out


# ---------------------------------------------------------------------------
# Sigma (x) Sigma  (64-dim) with Leibniz su(3) action
# ---------------------------------------------------------------------------
def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


I8 = sp.eye(8)


def leibniz(N):
    """Leibniz action of a single-factor operator N on Sigma (x) Sigma."""
    return kron(N, I8) + kron(I8, N)


def block_indices(first_idx, second_idx):
    """Global indices i*8+j of block first_idx (x) second_idx."""
    return [I8sz * 8 + J for I8sz in first_idx for J in second_idx]  # placeholder


def block_global(first_idx, second_idx):
    return [Ii * 8 + Jj for Ii in first_idx for Jj in second_idx]


def common_nullspace_in_block(gens, block_gidx):
    """Restrict each 64x64 generator to the block, stack, return nullspace vectors
    embedded back into 64-dim."""
    dimb = len(block_gidx)
    # embedding matrix 64 x dimb
    P = sp.zeros(64, dimb)
    for col, g in enumerate(block_gidx):
        P[g, col] = 1
    stacked = sp.zeros(0, dimb)
    for G in gens:
        Gb = P.T * G * P  # dimb x dimb (block is invariant)
        stacked = stacked.col_join(Gb)
    ns = stacked.nullspace()
    return [P * v for v in ns]  # embed back to 64-dim


# ---------------------------------------------------------------------------
# Twisted Dirac operator on invariants
#   D(eta (x) xi) = sum_i (e_i . nabla_{e_i} eta)(x)xi + (e_i . eta)(x)(nabla_{e_i} xi)
# ---------------------------------------------------------------------------
def build_dirac(E, nomizu):
    NAB = {i: spin_lift(nomizu[i], E) for i in range(1, 7)}  # nabla_{e_i}
    D = sp.zeros(64, 64)
    for i in range(1, 7):
        term1 = kron(E[i] * NAB[i], I8)  # (e_i . nabla eta) (x) xi
        term2 = kron(E[i], NAB[i])  # (e_i . eta) (x) (nabla xi)
        D += term1 + term2
    return D


def certificate(E, nomizu, gens, domain_first, domain_second, target_first, target_second):
    """Compute a=<w,Du1>, b=<w,Du2>, s=|a|^2+|b|^2 and residual check."""
    D = build_dirac(E, nomizu)
    dom_g = block_global(domain_first, domain_second)
    tgt_g = block_global(target_first, target_second)

    dom_inv = common_nullspace_in_block(gens, dom_g)
    tgt_inv = common_nullspace_in_block(gens, tgt_g)

    dom_on = gram_schmidt(dom_inv)
    tgt_on = gram_schmidt(tgt_inv)

    # certificate: sum over target ON basis of |<w, D u>|^2 summed over domain ON basis
    amps = []  # per (domain u) : list of amplitudes onto each target w
    residual_zero = True
    for u in dom_on:
        Du = D * u
        comps = []
        for w in tgt_on:
            comps.append(sp.simplify(hip(w, Du)))
        # residual outside span(target invariants): subtract projections
        res = Du
        for w, cf in zip(tgt_on, comps):
            res = res - cf * w
        res = sp.Matrix([sp.simplify(x) for x in res])
        if sp.simplify(hnorm2(res)) != 0:
            residual_zero = False
        amps.append(comps)

    # s = total squared Frobenius norm of the compressed map
    s = 0
    for comps in amps:
        for cf in comps:
            s += sp.simplify(sp.Abs(cf) ** 2)
    s = sp.simplify(s)
    return amps, s, residual_zero, len(dom_on), len(tgt_on)


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print("ROUND 59 ROUTE A - INDEPENDENT TRIVIAL-RANK CERTIFICATION")
    print("S^6 = G_2/SU(3), AHL2023 conventions (re-transcribed)")
    print("=" * 78)

    E = build_clifford(conj=False)

    # sanity: e_k^2 = -1
    for k in range(1, 7):
        assert sp.simplify(E[k] * E[k] + I8) == sp.zeros(8, 8), f"e_{k}^2 != -1"
    print("[sanity] e_k^2 = -1 for k=1..6 : PASS")

    # ---- CALIBRATION GATE ----
    calib_ok, calib_res = run_calibration(E, NOMIZU)
    print("\n[CALIBRATION] nabla_{e_i} psi_pm = +-(1/(2 sqrt3)) e_i . psi_pm")
    for branch_sign, i, zero in calib_res:
        tag = "psi_+" if branch_sign == +1 else "psi_-"
        print(f"    {tag}  e_{i}: {'OK' if zero else 'FAIL'}")
    print(f"[CALIBRATION] overall: {'PASS' if calib_ok else 'FAIL'}")
    if not calib_ok:
        print("STOP: calibration failed.")
        return {"calibration_passed": False}

    # ---- su(3) annihilates psi_+ (SU(3)-invariance sanity) ----
    print("\n[SANITY] su(3) generators annihilate psi_+ (and psi_-):")
    su3_ops = [spin_lift(ADNU[a], E) for a in range(1, 9)]
    ann_plus = all(sp.simplify((N * psi_plus()).norm()) == 0 for N in su3_ops)
    ann_minus = all(sp.simplify((N * psi_minus()).norm()) == 0 for N in su3_ops)
    print(f"    annihilate psi_+ : {ann_plus}")
    print(f"    annihilate psi_- : {ann_minus}")

    # ---- Leibniz generators on 64-dim ----
    gens = [leibniz(N) for N in su3_ops]

    # ---- FULL-FIBRE invariant search ----
    dim_oe = len(common_nullspace_in_block(gens, block_global(ODD_IDX, EVEN_IDX)))
    dim_ee = len(common_nullspace_in_block(gens, block_global(EVEN_IDX, EVEN_IDX)))
    print("\n[INVARIANT SEARCH] dim of common nullspace of 8 Leibniz generators:")
    print(f"    Sigma_odd  (x) Sigma_even : {dim_oe}")
    print(f"    Sigma_even (x) Sigma_even : {dim_ee}")

    # ---- Twisted Dirac certificate (domain = odd(x)even, target = even(x)even) ----
    amps, s, res_zero, ndom, ntgt = certificate(
        E,
        NOMIZU,
        gens,
        domain_first=ODD_IDX,
        domain_second=EVEN_IDX,
        target_first=EVEN_IDX,
        target_second=EVEN_IDX,
    )
    a = amps[0][0]
    b = amps[1][0]
    print("\n[CERTIFICATE] D : (Sigma_odd(x)Sigma_even)_inv -> (Sigma_even(x)Sigma_even)_inv")
    print(f"    dim domain invariants = {ndom}, dim target invariants = {ntgt}")
    print(f"    a = <w_hat, D u_1> = {sp.nsimplify(a)}  = {a}")
    print(f"    b = <w_hat, D u_2> = {sp.nsimplify(b)}  = {b}")
    print(f"    s = |a|^2 + |b|^2  = {s}")
    print(f"    residual outside span(w_hat) is zero : {res_zero}")
    print(f"    s > 0 : {sp.simplify(s) > 0}")

    # ---- CONVENTION SWEEP ----
    print("\n" + "=" * 78)
    print("CONVENTION SWEEP")
    print("=" * 78)

    sweep = {}

    # (i) psi_- calibration branch (mirrored Killing constant): D unchanged.
    #     Same Nomizu, same Clifford -> identical operator, identical s.
    calib_i, _ = run_calibration(E, NOMIZU)  # both branches already verified
    amps_i, s_i, res_i, _, _ = certificate(E, NOMIZU, gens, ODD_IDX, EVEN_IDX, EVEN_IDX, EVEN_IDX)
    sweep["(i) psi_- branch"] = (calib_i, s_i, sp.simplify(s_i) > 0)
    print(
        f"(i)  psi_- branch     : calib_consistent={calib_i}, s={s_i}, s>0={sp.simplify(s_i) > 0}"
    )

    # (ii) global conjugation i -> -i in Clifford action.
    Ec = build_clifford(conj=True)
    calib_ii, _ = run_calibration(Ec, NOMIZU)
    if calib_ii:
        su3c = [spin_lift(ADNU[a2], Ec) for a2 in range(1, 9)]
        gens_c = [leibniz(N) for N in su3c]
        amps_ii, s_ii, res_ii, _, _ = certificate(
            Ec, NOMIZU, gens_c, ODD_IDX, EVEN_IDX, EVEN_IDX, EVEN_IDX
        )
    else:
        s_ii = None
    sweep["(ii) conj i->-i"] = (
        calib_ii,
        s_ii,
        (sp.simplify(s_ii) > 0) if s_ii is not None else None,
    )
    print(
        f"(ii) conj i->-i       : calib_consistent={calib_ii}, s={s_ii}, "
        f"s>0={(sp.simplify(s_ii) > 0) if s_ii is not None else 'n/a'}"
    )

    # (iii) overall sign flip of Nomizu map -> BREAKS calibration (excluded).
    NOM_FLIP = {i: [(-cf, a2, b2) for (cf, a2, b2) in NOMIZU[i]] for i in NOMIZU}
    calib_iii, _ = run_calibration(E, NOM_FLIP)
    sweep["(iii) Nomizu sign flip"] = (calib_iii, None, None)
    print(f"(iii) Nomizu -Lambda  : calib_consistent={calib_iii}  (excluded: breaks calibration)")

    # (iv) relabel S^+ <-> S^- : swap domain/target (adjoint of the block map).
    amps_iv, s_iv, res_iv, ndom_iv, ntgt_iv = certificate(
        E,
        NOMIZU,
        gens,
        domain_first=EVEN_IDX,
        domain_second=EVEN_IDX,
        target_first=ODD_IDX,
        target_second=EVEN_IDX,
    )
    sweep["(iv) S+/S- swap"] = (True, s_iv, sp.simplify(s_iv) > 0)
    print(
        f"(iv) S+/S- swap       : calib_consistent=True, s={s_iv}, s>0={sp.simplify(s_iv) > 0} "
        f"(domain dim {ndom_iv}, target dim {ntgt_iv})"
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"calibration_passed        : {calib_ok}")
    print(f"dim inv Sigma_odd(x)even   : {dim_oe}")
    print(f"dim inv Sigma_even(x)even  : {dim_ee}")
    print(f"a_exact                    : {a}")
    print(f"b_exact                    : {b}")
    print(f"s_exact                    : {s}")
    print(f"s positive                 : {sp.simplify(s) > 0}")
    print(f"residual outside target 0  : {res_zero}")
    for k, v in sweep.items():
        print(f"sweep {k:24s}: {v}")

    return {
        "calibration_passed": calib_ok,
        "dim_oe": dim_oe,
        "dim_ee": dim_ee,
        "a": a,
        "b": b,
        "s": s,
        "res_zero": res_zero,
        "sweep": sweep,
    }


if __name__ == "__main__":
    main()
