r"""
C156 STEP 4 -- tests S1-S4 of HYPOTHESIS S, all fixed in PREREGISTRATION.md
AMENDMENT 2 before this file was written.

HYPOTHESIS S: for a full flag manifold G/T and an invariant spinor psi of
definite chirality, M : v |-> D_Sigma(v) psi is SURJECTIVE onto the
opposite-chirality part of Sigma^T.

  S1  every definite-chirality invariant spinor on G_2 -> rank 4 each
  S2  same on A_2                                      -> rank 2 each
  S3  THIRD SPACE A_2 x A_2                            -> rank 4
  S4  A_2 in the POSITIVE-root orientation             -> rank 2 (orientation-free)

Run:  python c156_step4_hypothesis_S.py
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
S2M = load("c156s2", "c156_step2_g2_test.py")
S3M = load("c156s3", "c156_step3_chirality.py")


def realify_cols(vecs):
    cols = []
    for M in vecs:
        col = []
        for t in range(M.rows):
            col.append(sp.re(M[t]))
            col.append(sp.im(M[t]))
        cols.append(sp.Matrix(col))
    return sp.Matrix.hstack(*cols) if cols else None


def full_test(name, weights, expect_rank=None):
    N = len(weights)
    dim_m = 2 * N
    print("=" * 78)
    print(f"{name}   (N={N}, dim m={dim_m}, dim Sigma={2**N})")
    print("=" * 78)
    E = G.clifford(N)
    W = S3M.chirality(E, dim_m)
    gens = G.torus_gens(weights)
    inv = G.invariant_spinors(gens, E, dim_m)
    print(f"  invariant spinors: complex dim {len(inv)}")
    if not inv:
        print("  none -- cannot test here")
        return None

    # chirality-adapted basis of Sigma^T
    B = sp.Matrix.hstack(*inv)
    Wr = sp.simplify(B.pinv() * W * B)
    plus, minus = [], []
    for val, mult, vecs in Wr.eigenvects():
        for vv in vecs:
            (plus if sp.nsimplify(val) == 1 else minus).append(sp.expand(B * vv))
    print(f"  chirality split of Sigma^T: +{len(plus)} / -{len(minus)}")

    fam, pairs = G.equivariant_family(gens, dim_m)
    print(f"  equivariant family dim: {fam.cols}")

    results = []
    for chi, group, opp in ((+1, plus, minus), (-1, minus, plus)):
        opp_exp = []
        for v in opp:
            opp_exp.append(v)
            opp_exp.append(sp.expand(sp.I * v))
        opp_real = realify_cols(opp_exp)
        target_dim = opp_real.rank() if opp_real is not None else 0
        for idx, psi in enumerate(group):
            imgs = S2M.fast_images(fam, pairs, E, dim_m, psi)
            Rm = realify_cols(imgs)
            rank = Rm.rank()
            aug = sp.Matrix.hstack(opp_real, Rm) if opp_real is not None else Rm
            contained = aug.rank() == target_dim
            surj = contained and rank == target_dim
            print(
                f"    psi[chirality {chi:+d}, #{idx}] : rank(M) = {rank}, "
                f"opposite half dim = {target_dim}, contained = {contained}, SURJECTIVE = {surj}"
            )
            results.append((rank, target_dim, surj))
    all_surj = all(s for _, _, s in results)
    ranks = sorted({r for r, _, _ in results})
    print(f"  --> all spinors surjective: {all_surj}; ranks seen: {ranks}")
    if expect_rank is not None:
        ok = all(r == expect_rank for r, _, _ in results)
        print(f"  --> matches pre-registered rank {expect_rank}: {ok}")
    return {"all_surj": all_surj, "ranks": ranks}


if __name__ == "__main__":
    print()
    print("#" * 78)
    print("# S2  A_2 (C155 orientation), ALL invariant spinors")
    print("#" * 78)
    a2 = [(-2, 1), (1, 1), (1, -2)]
    r_s2 = full_test("A_2 = SU(3)/T^2", a2, expect_rank=2)

    print()
    print("#" * 78)
    print("# S4  A_2 in the POSITIVE-root orientation (orientation must not matter)")
    print("#" * 78)
    a2p = [(2, -1), (1, 1), (-1, 2)]
    r_s4 = full_test("A_2, positive-root orientation", a2p, expect_rank=2)

    print()
    print("#" * 78)
    print("# S1  G_2/T^2, ALL invariant spinors")
    print("#" * 78)
    coeffs = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
    g2 = [(2 * c1 - c2, -3 * c1 + 2 * c2) for (c1, c2) in coeffs]
    r_s1 = full_test("G_2/T^2", g2, expect_rank=4)

    print()
    print("#" * 78)
    print("# S3  THIRD SPACE: A_2 x A_2 = (SU(3)xSU(3))/T^4")
    print("#     PRE-REGISTERED PREDICTION: rank(M) = 4")
    print("#" * 78)
    # rank-4 weights: first A_2 in coords 0,1 ; second A_2 in coords 2,3
    a2a2 = [
        (-2, 1, 0, 0),
        (1, 1, 0, 0),
        (1, -2, 0, 0),
        (0, 0, -2, 1),
        (0, 0, 1, 1),
        (0, 0, 1, -2),
    ]
    r_s3 = full_test("A_2 x A_2", a2a2, expect_rank=4)

    print()
    print("=" * 78)
    print("HYPOTHESIS S -- VERDICT")
    print("=" * 78)
    for nm, r in (
        ("S2 A_2", r_s2),
        ("S4 A_2 pos-orient", r_s4),
        ("S1 G_2", r_s1),
        ("S3 A_2xA_2", r_s3),
    ):
        if r is None:
            print(f"  {nm}: not testable")
        else:
            print(f"  {nm}: surjective everywhere = {r['all_surj']}, ranks = {r['ranks']}")
