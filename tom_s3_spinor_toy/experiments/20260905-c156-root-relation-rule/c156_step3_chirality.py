r"""
C156 STEP 3 -- the pre-registered rule died; test the MECHANISM the data suggest.

Step 2 falsified  rank(M) = 2 dim R  out of sample (G_2 gave 4, not 8).
The two data points instead satisfy

    A_2 : dim_C Sigma^T = 2, dim_R Sigma^T = 4, rank(M) = 2
    G_2 : dim_C Sigma^T = 4, dim_R Sigma^T = 8, rank(M) = 4

i.e. rank(M) = (1/2) dim_R Sigma^T in both. That is a POST-HOC fit on two
points and is worth nothing by itself. What makes it worth testing is that
there is a candidate REASON:

    D_Sigma(v) is an ODD operator (it anticommutes with the chirality
    operator omega), so it maps Sigma^+ to Sigma^-. If psi has definite
    chirality, image(M) is confined to the OPPOSITE-chirality part of the
    invariant subspace Sigma^T. If Sigma^T splits evenly under chirality,
    that part has real dimension (1/2) dim_R Sigma^T -- the observed rank.

So the "half" would be FORCED by chirality, and the real content would be
that M is SURJECTIVE onto that half. This file tests each link separately:

  H1  omega anticommutes with every E_a (so D is odd)                 [forced?]
  H2  psi has definite chirality
  H3  Sigma^T splits evenly into chirality halves
  H4  image(M) is contained in the opposite-chirality half of Sigma^T
  H5  image(M) EQUALS that half (surjectivity -- the actual content)

Run:  python c156_step3_chirality.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


G = load("c156g", "c156_general.py")
S2 = load("c156s2", "c156_step2_g2_test.py")


def chirality(E, dim_m):
    """omega = i^{dim_m/2} E_1 E_2 ... E_{dim_m}; omega^2 = 1 in even dim."""
    n = dim_m // 2
    W = sp.eye(E[1].rows)
    for a in range(1, dim_m + 1):
        W = W * E[a]
    W = sp.expand((sp.I**n) * W)
    return W


def realify_cols(vecs):
    cols = []
    for M in vecs:
        col = []
        for t in range(M.rows):
            col.append(sp.re(M[t]))
            col.append(sp.im(M[t]))
        cols.append(sp.Matrix(col))
    return sp.Matrix.hstack(*cols) if cols else None


def study(name, weights):
    N = len(weights)
    dim_m = 2 * N
    print("=" * 78)
    print(f"{name}")
    print("=" * 78)
    E = G.clifford(N)
    W = chirality(E, dim_m)
    sq = sp.expand(W * W)
    print(f"  H1a omega^2 == I : {sq == sp.eye(E[1].rows)}")
    anti = all(sp.expand(W * E[a] + E[a] * W) == sp.zeros(E[1].rows) for a in range(1, dim_m + 1))
    print(f"  H1b omega anticommutes with every E_a (D is ODD): {anti}")

    gens = G.torus_gens(weights)
    inv = G.invariant_spinors(gens, E, dim_m)
    print(f"  invariant spinors: complex dim {len(inv)}  (real dim {2 * len(inv)})")

    # chirality decomposition of Sigma^T
    plus, minus = [], []
    for v in inv:
        wv = sp.expand(W * v)
        if sp.expand(wv - v) == sp.zeros(v.rows, 1):
            plus.append(v)
        elif sp.expand(wv + v) == sp.zeros(v.rows, 1):
            minus.append(v)
    # if the given basis is not chirality-adapted, project instead
    if len(plus) + len(minus) != len(inv):
        B = sp.Matrix.hstack(*inv)
        Wr = sp.simplify(B.pinv() * W * B)
        plus, minus = [], []
        for val, mult, vecs in Wr.eigenvects():
            for vv in vecs:
                tgt = plus if sp.nsimplify(val) == 1 else minus
                tgt.append(sp.expand(B * vv))
    print(f"  H3 chirality split of Sigma^T : dim_C(+) = {len(plus)}, dim_C(-) = {len(minus)}")
    even_split = len(plus) == len(minus)
    print(f"     splits EVENLY: {even_split}")

    fam, pairs = G.equivariant_family(gens, dim_m)
    psi = inv[0]
    wpsi = sp.expand(W * psi)
    chi = None
    if sp.expand(wpsi - psi) == sp.zeros(psi.rows, 1):
        chi = +1
    elif sp.expand(wpsi + psi) == sp.zeros(psi.rows, 1):
        chi = -1
    print(f"  H2 psi has definite chirality: {chi is not None} (chirality {chi})")
    if chi is None:
        psi = (plus + minus)[0]
        wpsi = sp.expand(W * psi)
        chi = 1 if sp.expand(wpsi - psi) == sp.zeros(psi.rows, 1) else -1
        print(f"     -> switched to a chirality-adapted invariant spinor (chirality {chi})")

    imgs = S2.fast_images(fam, pairs, E, dim_m, psi)
    Rm = realify_cols(imgs)
    rank = Rm.rank()
    opp = minus if chi == 1 else plus
    # BUG FIX (found because H4 returned False although the chirality argument
    # FORCES it true): the real span of a COMPLEX subspace spanned by v is
    # span_R{v, i*v}, two real dimensions -- realify_cols(v) alone gives one.
    opp_expanded = []
    for v in opp:
        opp_expanded.append(v)
        opp_expanded.append(sp.expand(sp.I * v))
    opp_real = realify_cols(opp_expanded) if opp_expanded else None
    dim_opp_real = 2 * len(opp)
    print(f"  rank(M) = {rank};  opposite-chirality half of Sigma^T has real dim {dim_opp_real}")

    # H4: is every image inside the opposite half?
    inside = None
    if opp_real is not None:
        aug = sp.Matrix.hstack(opp_real, Rm)
        inside = aug.rank() == opp_real.rank()
        print(f"  H4 image(M) contained in the opposite-chirality half: {inside}")
        print(f"  H5 image(M) EQUALS that half (surjective): {inside and rank == opp_real.rank()}")
    return {
        "rank": rank,
        "dim_opp_real": dim_opp_real,
        "inside": inside,
        "invC": len(inv),
        "chi": chi,
        "plus": len(plus),
        "minus": len(minus),
    }


if __name__ == "__main__":
    a2 = [(-2, 1), (1, 1), (1, -2)]
    r1 = study("A_2 = SU(3)/T^2", a2)
    print()
    coeffs = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
    g2 = [(2 * c1 - c2, -3 * c1 + 2 * c2) for (c1, c2) in coeffs]
    r2 = study("G_2/T^2", g2)
    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for nm, r in (("A_2", r1), ("G_2", r2)):
        print(
            f"  {nm}: dim_C Sigma^T = {r['invC']} (+:{r['plus']}, -:{r['minus']}), "
            f"rank(M) = {r['rank']}, opposite half real dim = {r['dim_opp_real']}, "
            f"contained = {r['inside']}"
        )
