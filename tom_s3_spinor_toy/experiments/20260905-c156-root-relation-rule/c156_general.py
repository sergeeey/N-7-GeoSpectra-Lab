r"""
C156 -- general machinery: build the mu-map on ANY full flag manifold G/T from
the positive-root weights alone, and compare its rank/structure against the
relation space R.

WHY ONLY THE WEIGHTS ARE NEEDED (checked against C153/C155's own code, which is
what the A_2 regression below re-verifies):
  * the equivariant connection family is the nullspace of the T-equivariance
    conditions, which involve only the torus generators acting on m;
  * invariant spinors are the common nullspace of spin_lift(T_j), again torus
    only;
  * D_Sigma(v) = sum_i E_i spin_lift(Lambda_i(v)) needs Clifford + Lambda only.
The Levi-Civita connection (which WOULD need structure constants) entered C155
solely to NAME one invariant spinor psi_+, and C155 Step 6 showed the rank
result does not depend on that choice (rank(v -> (D psi_+, D psi_-)) = 2, the
same as either alone). So no structure constants, hence no free convention.

Run:  python c156_general.py
"""


import sympy as sp

# ---------------------------------------------------------------------------
# Clifford algebra on 2n generators, acting on a 2^n-dimensional spinor space.
# E_a E_b + E_b E_a = -2 delta_ab.  Built by the standard tensor construction
# and VERIFIED, not assumed.
# ---------------------------------------------------------------------------
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
ID2 = sp.eye(2)


def kron(*mats):
    out = sp.Matrix([[1]])
    for m in mats:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def clifford(n):
    """Return E[1..2n], each 2^n x 2^n, with E_a E_b + E_b E_a = -2 delta."""
    E = {}
    for k in range(1, n + 1):
        pre = [S3] * (k - 1)
        post = [ID2] * (n - k)
        E[2 * k - 1] = sp.I * kron(*(pre + [S1] + post))
        E[2 * k] = sp.I * kron(*(pre + [S2] + post))
    return E


def verify_clifford(E, dim_m):
    for a in range(1, dim_m + 1):
        for b in range(a, dim_m + 1):
            anti = sp.simplify(E[a] * E[b] + E[b] * E[a])
            want = -2 * sp.eye(E[a].rows) if a == b else sp.zeros(E[a].rows)
            if anti != want:
                return False, (a, b)
    return True, None


# ---------------------------------------------------------------------------
def torus_gens(weights):
    """T_j acting on m: on plane k it is the rotation with coefficient w_k[j].
    Convention fixed to match C153/C155: T[2k+1, 2k] = +w, T[2k, 2k+1] = -w."""
    N = len(weights)
    r = len(weights[0])
    gens = []
    for j in range(r):
        T = sp.zeros(2 * N, 2 * N)
        for k in range(N):
            w = weights[k][j]
            T[2 * k, 2 * k + 1] = -w
            T[2 * k + 1, 2 * k] = w
        gens.append(T)
    return gens


def spin_lift(L, E, dim_m):
    out = sp.zeros(E[1].rows, E[1].rows)
    for a in range(dim_m):
        for b in range(a + 1, dim_m):
            if L[a, b] != 0:
                out += L[a, b] * sp.Rational(1, 2) * (E[a + 1] * E[b + 1])
    return out


# ---------------------------------------------------------------------------
def equivariant_family(gens, dim_m):
    """Nullspace of  Lambda(T e_k) = [T, Lambda(e_k)]  over all torus gens.

    Same index logic as C153's equivariant_torsion_basis_exact, generalised.
    Solved block-by-block over connected components of the coupling graph so
    it stays tractable when dim_m grows (792 unknowns for G_2).
    """
    pairs = [(i, j) for i in range(dim_m) for j in range(i + 1, dim_m)]
    pidx = {p: t for t, p in enumerate(pairs)}
    npair = len(pairs)

    def unk(k, p):
        return k * npair + p

    rows = []
    for T in gens:
        for k in range(dim_m):
            for i, j in pairs:
                row = {}
                p = pidx[(i, j)]
                for ell in range(dim_m):
                    if T[ell, k] != 0:
                        row[unk(ell, p)] = row.get(unk(ell, p), 0) + T[ell, k]
                for mm in range(dim_m):
                    if mm == i or T[i, mm] == 0:
                        continue
                    ii, jj, sgn = mm, j, 1
                    if ii == jj:
                        continue
                    if ii > jj:
                        ii, jj, sgn = jj, ii, -1
                    key = unk(k, pidx[(ii, jj)])
                    row[key] = row.get(key, 0) - sgn * T[i, mm]
                for mm in range(dim_m):
                    if mm == j or T[j, mm] == 0:
                        continue
                    ii, jj, sgn = i, mm, 1
                    if ii == jj:
                        continue
                    if ii > jj:
                        ii, jj, sgn = jj, ii, -1
                    key = unk(k, pidx[(ii, jj)])
                    row[key] = row.get(key, 0) - sgn * T[j, mm]
                row = {c: v for c, v in row.items() if v != 0}
                if row:
                    rows.append(row)

    n_unk = dim_m * npair
    # connected components over columns
    parent = list(range(n_unk))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx

    for row in rows:
        cols = list(row)
        for c in cols[1:]:
            union(cols[0], c)

    comp_cols = {}
    for c in range(n_unk):
        comp_cols.setdefault(find(c), []).append(c)
    comp_rows = {}
    for row in rows:
        comp_rows.setdefault(find(next(iter(row))), []).append(row)

    basis = []
    for root, cols in comp_cols.items():
        rws = comp_rows.get(root, [])
        if not rws:
            # unconstrained columns: each is its own free direction
            for c in cols:
                v = sp.zeros(n_unk, 1)
                v[c] = 1
                basis.append(v)
            continue
        cmap = {c: t for t, c in enumerate(cols)}
        A = sp.zeros(len(rws), len(cols))
        for ri, row in enumerate(rws):
            for c, val in row.items():
                A[ri, cmap[c]] = val
        for ns in A.nullspace():
            v = sp.zeros(n_unk, 1)
            for c, t in cmap.items():
                v[c] = ns[t]
            basis.append(v)
    return sp.Matrix.hstack(*basis) if basis else sp.zeros(n_unk, 0), pairs


def lam_of(vec, pairs, dim_m):
    npair = len(pairs)
    lam = {}
    for k in range(dim_m):
        M = sp.zeros(dim_m, dim_m)
        for p, (i, j) in enumerate(pairs):
            val = vec[k * npair + p]
            if val != 0:
                M[i, j] += val
                M[j, i] -= val
        lam[k] = M
    return lam


def D_of(vec, pairs, E, dim_m):
    lam = lam_of(vec, pairs, dim_m)
    D = sp.zeros(E[1].rows, E[1].rows)
    for k in range(dim_m):
        if any(lam[k][i, j] != 0 for i in range(dim_m) for j in range(dim_m)):
            D += E[k + 1] * spin_lift(lam[k], E, dim_m)
    return D


def relation_space(weights):
    N = len(weights)
    r = len(weights[0])
    A = sp.Matrix(r, N, lambda i, k: weights[k][i])
    return A.nullspace(), A


def invariant_spinors(gens, E, dim_m):
    blocks = [spin_lift(T, E, dim_m) for T in gens]
    return sp.Matrix.vstack(*blocks).nullspace()


def realify(vecs):
    cols = []
    for M in vecs:
        col = []
        for t in range(M.rows):
            col.append(sp.re(M[t]))
            col.append(sp.im(M[t]))
        cols.append(sp.Matrix(col))
    return sp.Matrix.hstack(*cols) if cols else None


def analyse(name, weights, expect_family=None):
    N = len(weights)
    r = len(weights[0])
    dim_m = 2 * N
    n = N
    print("=" * 78)
    print(f"{name}:  N={N} positive roots, rank r={r}, dim m={dim_m}, dim Sigma={2**n}")
    print("=" * 78)
    R, _A = relation_space(weights)
    print(f"  relation space R = ker[beta_1..beta_N] : dim {len(R)}  (predicted N-r = {N - r})")
    for v in R:
        print(f"    relation: {tuple(sp.nsimplify(x) for x in v)}")

    E = clifford(n)
    ok, bad = verify_clifford(E, dim_m)
    print(f"  Clifford relations verified: {ok}" + ("" if ok else f" FAILED at {bad}"))
    assert ok

    gens = torus_gens(weights)
    inv = invariant_spinors(gens, E, dim_m)
    print(f"  invariant spinors: complex dim {len(inv)}")
    if not inv:
        print("  NO invariant spinor -- mu-map undefined here, cannot test. STOP.")
        return None

    fam, pairs = equivariant_family(gens, dim_m)
    print(
        f"  equivariant connection family: dim {fam.cols}"
        + (f"  (A_2 regression expects {expect_family})" if expect_family else "")
    )
    if expect_family is not None:
        assert fam.cols == expect_family, "family dimension regression FAILED"

    psi = inv[0]
    imgs = [sp.simplify(D_of(fam[:, c], pairs, E, dim_m) * psi) for c in range(fam.cols)]
    Rm = realify(imgs)
    rank = Rm.rank()
    print(f"  rank(M) = {rank}    [rule predicts 2*dim R = {2 * len(R)}]")
    print(f"  dim ker(M) = {fam.cols - rank}")
    return {
        "N": N,
        "r": r,
        "dimR": len(R),
        "family": fam.cols,
        "rank": rank,
        "fam": fam,
        "pairs": pairs,
        "E": E,
        "psi": psi,
        "inv": inv,
        "R": R,
    }


if __name__ == "__main__":
    # ---- A_2 REGRESSION GATE: must reproduce C153/C155's own numbers --------
    print()
    print("#" * 78)
    print("# A_2 REGRESSION -- the weights C155 actually measured on SU(3)/T^2")
    print("#" * 78)
    a2_c155 = [(-2, 1), (1, 1), (1, -2)]
    res = analyse("A_2 (C155 orientation)", a2_c155, expect_family=6)
    assert res is not None
    assert res["rank"] == 2, "A_2 rank regression FAILED -- expected 2 (C155 measured)"
    print("  A_2 REGRESSION PASSED: family dim 6 and rank(M) = 2, matching C155.")
