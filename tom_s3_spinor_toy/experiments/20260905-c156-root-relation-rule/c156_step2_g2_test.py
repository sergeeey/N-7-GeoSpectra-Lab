r"""
C156 STEP 2 -- the OUT-OF-SAMPLE test on G_2/T^2.

Prediction fixed in PREREGISTRATION.md before this file was written:

    rank(M) = 2 * dim R = 2 * (N - r) = 2 * (6 - 2) = 8

G_2 positive roots in (alpha_1, alpha_2) coefficients:
    (1,0), (0,1), (1,1), (2,1), (3,1), (3,2)
paired against the two simple coroots via the G_2 Cartan matrix
[[2,-1],[-3,2]] to give the torus weights used below.

Gates before the prediction is allowed to be evaluated:
  G1  the weights really are 6 distinct roots spanning a rank-2 space
  G2  Clifford relations hold on 12 generators
  G3  an invariant spinor exists (equivalently R contains a +-1 vector)
  G4  the FAST image routine reproduces the A_2 answer of the slow one

Run:  python c156_step2_g2_test.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c156g", HERE / "c156_general.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)


def fast_images(fam, pairs, E, dim_m, psi):
    """M(v) = sum_k E_{k+1} spin_lift(Lambda_k(v)) psi, applied to psi directly.

    Precomputes (E_a E_b) psi once per pair, so each family vector costs only
    vector arithmetic plus dim_m matrix-vector products. Needed because on
    G_2 the naive route is 12*66 matrix-matrix products of 64x64 per vector.
    """
    EEpsi = {}
    for a in range(dim_m):
        for b in range(a + 1, dim_m):
            EEpsi[(a, b)] = sp.expand(E[a + 1] * (E[b + 1] * psi))
    npair = len(pairs)
    out = []
    for c in range(fam.cols):
        vec = fam[:, c]
        total = sp.zeros(psi.rows, 1)
        for k in range(dim_m):
            acc = sp.zeros(psi.rows, 1)
            nonzero = False
            for p, (i, j) in enumerate(pairs):
                val = vec[k * npair + p]
                if val != 0:
                    acc += sp.Rational(1, 2) * val * EEpsi[(i, j)]
                    nonzero = True
            if nonzero:
                total += E[k + 1] * acc
        out.append(sp.expand(total))
    return out


def run(name, weights, expect_family=None, expect_rank=None):
    N = len(weights)
    r = len(weights[0])
    dim_m = 2 * N
    print("=" * 78)
    print(f"{name}: N={N}, r={r}, dim m={dim_m}, dim Sigma={2**N}")
    print("=" * 78)

    Rel, A = G.relation_space(weights)
    print(f"  G1 rank of the weight matrix = {A.rank()} (must be {r}); dim R = {len(Rel)}")
    assert A.rank() == r
    for v in Rel:
        print(f"     relation: {tuple(sp.nsimplify(x) for x in v)}")

    E = G.clifford(N)
    ok, bad = G.verify_clifford(E, dim_m)
    print(f"  G2 Clifford relations on {dim_m} generators verified: {ok}")
    assert ok, f"Clifford failed at {bad}"

    gens = G.torus_gens(weights)
    inv = G.invariant_spinors(gens, E, dim_m)
    print(f"  G3 invariant spinors: complex dim {len(inv)}")
    assert inv, "no invariant spinor -- cannot test here"

    fam, pairs = G.equivariant_family(gens, dim_m)
    print(f"  equivariant connection family: dim {fam.cols}")
    if expect_family is not None:
        assert fam.cols == expect_family

    psi = inv[0]
    imgs = fast_images(fam, pairs, E, dim_m, psi)
    Rm = G.realify(imgs)
    rank = Rm.rank()
    print()
    print(f"  >>> rank(M) = {rank}")
    print(f"  >>> rule predicts 2*dim R = {2 * len(Rel)}")
    print(f"  >>> dim ker(M) = {fam.cols - rank}")
    verdict = rank == 2 * len(Rel)
    print(f"  >>> PREDICTION CONFIRMED: {verdict}")
    if expect_rank is not None:
        assert rank == expect_rank, f"regression: expected rank {expect_rank}, got {rank}"
    return {
        "rank": rank,
        "dimR": len(Rel),
        "family": fam.cols,
        "inv": len(inv),
        "fam": fam,
        "pairs": pairs,
        "E": E,
        "psi": psi,
        "Rel": Rel,
        "imgs": imgs,
    }


if __name__ == "__main__":
    print()
    print("#" * 78)
    print("# G4  FAST-ROUTINE REGRESSION on A_2 (must reproduce rank 2)")
    print("#" * 78)
    run("A_2 (C155 orientation)", [(-2, 1), (1, 1), (1, -2)], expect_family=6, expect_rank=2)

    print()
    print("#" * 78)
    print("# OUT-OF-SAMPLE TEST: G_2/T^2   (prediction fixed: rank(M) = 8)")
    print("#" * 78)
    # G_2 Cartan matrix [[2,-1],[-3,2]]; beta = c1 a1 + c2 a2 pairs as
    #   (<beta,a1^v>, <beta,a2^v>) = (2c1 - c2, -3c1 + 2c2)
    coeffs = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
    g2 = [(2 * c1 - c2, -3 * c1 + 2 * c2) for (c1, c2) in coeffs]
    print(f"  G_2 positive roots (c1,c2) : {coeffs}")
    print(f"  their torus weights        : {g2}")
    run("G_2/T^2", g2)
