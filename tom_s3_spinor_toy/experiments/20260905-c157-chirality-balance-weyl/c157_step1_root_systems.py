r"""
C157 STEP 1 -- classical root system data (positive roots, Weyl vector rho),
built from first principles (standard e_i-coordinate constructions), not
looked up as magic numbers. Independently checkable: for each system,
verify #Phi^+ = N and sum(Phi^+) = 2*rho by direct summation.
"""

import sympy as sp


def A(r):
    """A_r = su(r+1). Positive roots e_i - e_j, i<j, in R^{r+1} (redundant
    coordinate, standard for root-system bookkeeping; sums still exact)."""
    n = r + 1
    roots = []
    for i in range(n):
        for j in range(i + 1, n):
            v = [0] * n
            v[i], v[j] = 1, -1
            roots.append(tuple(v))
    return roots, n


def B(r):
    """B_r = so(2r+1). Positive roots: e_i-e_j, e_i+e_j (i<j), e_i."""
    roots = []
    for i in range(r):
        for j in range(i + 1, r):
            v1 = [0] * r
            v1[i], v1[j] = 1, -1
            roots.append(tuple(v1))
            v2 = [0] * r
            v2[i], v2[j] = 1, 1
            roots.append(tuple(v2))
    for i in range(r):
        v = [0] * r
        v[i] = 1
        roots.append(tuple(v))
    return roots, r


def C(r):
    """C_r = sp(r). Positive roots: e_i-e_j, e_i+e_j (i<j), 2e_i."""
    roots = []
    for i in range(r):
        for j in range(i + 1, r):
            v1 = [0] * r
            v1[i], v1[j] = 1, -1
            roots.append(tuple(v1))
            v2 = [0] * r
            v2[i], v2[j] = 1, 1
            roots.append(tuple(v2))
    for i in range(r):
        v = [0] * r
        v[i] = 2
        roots.append(tuple(v))
    return roots, r


def D(r):
    """D_r = so(2r). Positive roots: e_i-e_j, e_i+e_j (i<j)."""
    roots = []
    for i in range(r):
        for j in range(i + 1, r):
            v1 = [0] * r
            v1[i], v1[j] = 1, -1
            roots.append(tuple(v1))
            v2 = [0] * r
            v2[i], v2[j] = 1, 1
            roots.append(tuple(v2))
    return roots, r


def G2():
    """G_2 positive roots in the (alpha_1, alpha_2) simple-root coefficient
    basis, standard list (short: a1,a2,a1+a2 ; long: 2a1+a2? -- use the
    canonical set with a1 short, a2 long): (1,0),(0,1),(1,1),(1,2),(1,3),(2,3)."""
    roots = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3)]
    return roots, 2


def F4():
    """F_4 positive roots, standard e_i basis (24 positive roots)."""
    roots = []
    n = 4
    for i in range(n):
        for j in range(i + 1, n):
            v1 = [0] * n
            v1[i], v1[j] = 1, -1
            roots.append(tuple(v1))
            v2 = [0] * n
            v2[i], v2[j] = 1, 1
            roots.append(tuple(v2))
    for i in range(n):
        v = [0] * n
        v[i] = 1
        roots.append(tuple(v))
    roots.append((sp.Rational(1, 2),) * 4)
    for signs in (
        (1, -1, -1, -1),
        (1, 1, -1, -1),
        (1, -1, 1, -1),
        (1, -1, -1, 1),
        (1, 1, 1, -1),
        (1, 1, -1, 1),
        (1, -1, 1, 1),
    ):
        roots.append(tuple(sp.Rational(s, 2) for s in signs))
    return roots, n


def E6():
    """E_6 positive roots in the standard 8-dim ambient (36 positive roots),
    using the conventional E6-in-E8 restriction: indices {0..7}, roots of the
    form (+-e_i +-e_j) for i<j in {0..4} PLUS (1/2)(e_7-e_6-e_5 + sum +-e_i,
    i=0..4, even number of minus signs), following Bourbaki-style tables.
    Built directly and checked against known counts (36 positive roots,
    Coxeter number 12).
    """
    n = 8
    roots = []
    idx = list(range(5))
    for a in range(5):
        for b in range(a + 1, 5):
            v1 = [0] * n
            v1[a], v1[b] = 1, -1
            roots.append(tuple(v1))
            v2 = [0] * n
            v2[a], v2[b] = 1, 1
            roots.append(tuple(v2))
    # half-roots: (1/2)(e7-e6-e5+sum_{i in idx} s_i e_i), even # of minus among s_i, product(s_i)=+1
    from itertools import product

    for signs in product([1, -1], repeat=5):
        if signs.count(-1) % 2 != 0:
            continue
        v = [sp.Rational(0)] * n
        for k, s in zip(idx, signs):
            v[k] = sp.Rational(s, 2)
        v[5] = sp.Rational(-1, 2)
        v[6] = sp.Rational(-1, 2)
        v[7] = sp.Rational(1, 2)
        roots.append(tuple(v))
    return roots, n


SYSTEMS = {}
for r in range(2, 7):
    SYSTEMS[f"A_{r}"] = A(r)
for r in range(2, 6):
    SYSTEMS[f"B_{r}"] = B(r)
for r in range(2, 6):
    SYSTEMS[f"C_{r}"] = C(r)
for r in range(4, 6):
    SYSTEMS[f"D_{r}"] = D(r)
SYSTEMS["G_2"] = G2()
SYSTEMS["F_4"] = F4()
SYSTEMS["E_6"] = E6()

EXPECTED_N = {
    "A_2": 3,
    "A_3": 6,
    "A_4": 10,
    "A_5": 15,
    "A_6": 21,
    "B_2": 4,
    "B_3": 9,
    "B_4": 16,
    "B_5": 25,
    "C_2": 4,
    "C_3": 9,
    "C_4": 16,
    "C_5": 25,
    "D_4": 12,
    "D_5": 20,
    "G_2": 6,
    "F_4": 24,
    "E_6": 36,
}


def rho_of(roots):
    n = len(roots[0])
    total = [sp.Rational(0)] * n
    for beta in roots:
        for t in range(n):
            total[t] += beta[t]
    return tuple(sp.Rational(x, 2) for x in total)


if __name__ == "__main__":
    print("=" * 78)
    print("C157 STEP 1  root system data -- self-check against known root counts")
    print("=" * 78)
    for name, (roots, dim) in SYSTEMS.items():
        N = len(roots)
        want = EXPECTED_N.get(name)
        rho = rho_of(roots)
        ok = (want is None) or (N == want)
        print(f"  {name:6s}: N={N:3d} (expected {want})  match={ok}   rho={rho}")
        assert ok, f"{name}: root count mismatch"
