"""
Decisive check for the Round 9 open question: is D_on_simple_tensor (built
from nabla_g, using ONLY the Nomizu-map/Lambda term, no explicit true-
derivative term) a mathematically valid operator?

NECESSARY (not sufficient, but DECISIVE if it fails) condition: D must be
SU(3)-equivariant, i.e. commute with the su(3) action on Sigma(x)Sigma,
REGARDLESS of any subtlety about what "vec" represents for non-invariant
inputs. SU(3) is the isotropy/gauge symmetry at the basepoint -- ANY
correctly-constructed geometric Dirac-type operator MUST respect it. If
D built from nabla_g does NOT commute with su(3), that is definitive
proof something in the construction is wrong (not just a subtle
interpretation issue). If it DOES commute, that is strong (though not
100% conclusive on its own) evidence the construction is sound, since a
broken "missing true-derivative term" would generically NOT preserve
this symmetry (the true-derivative term itself is built from LEFT-
invariant vector fields, unrelated to the RIGHT su(3) action, so omitting
it does not generically preserve equivariance by accident).
"""

import sympy as sp
from g2su3_explicit_clifford import DIM, SUBSETS, IDX, vec_from_subsets
from g2su3_twisted_kernel import su3_action
from g2su3_compute_crossterm import D_on_simple_tensor

sqrt = sp.sqrt


def su3_twisted_action(i, vec64):
    """su(3) generator i acting on Sigma(x)Sigma via Leibniz rule."""
    out = sp.zeros(64, 1)
    for row in range(64):
        c = vec64[row]
        if c == 0:
            continue
        sL = SUBSETS[row // 8]
        sR = SUBSETS[row % 8]
        eta = vec_from_subsets({sL: 1})
        xi = vec_from_subsets({sR: 1})
        out1 = su3_action(i, eta)
        for r2 in range(DIM):
            v = out1[r2]
            if v != 0:
                out[8 * r2 + (row % 8)] += c * v
        out2 = su3_action(i, xi)
        for r2 in range(DIM):
            v = out2[r2]
            if v != 0:
                out[8 * (row // 8) + r2] += c * v
    return out


def build_D_matrix64():
    """Build the full 64x64 matrix of D^{1/2}_twisted via D_on_simple_tensor
    applied to each of the 64 basis vectors of Sigma(x)Sigma."""
    D = sp.zeros(64, 64)
    for col in range(64):
        sL = SUBSETS[col // 8]
        sR = SUBSETS[col % 8]
        eta = vec_from_subsets({sL: 1})
        xi = vec_from_subsets({sR: 1})
        res = D_on_simple_tensor(eta, xi)
        for (rL, rR), c in res.items():
            row = 8 * IDX[rL] + IDX[rR]
            D[row, col] = c
    return D


def build_su3_matrix64(i):
    M = sp.zeros(64, 64)
    for col in range(64):
        e = sp.zeros(64, 1)
        e[col] = 1
        out = su3_twisted_action(i, e)
        for row in range(64):
            M[row, col] = out[row]
    return M


def main():
    print("=" * 70)
    print("Building D^{1/2}_twisted as a 64x64 matrix (via D_on_simple_tensor)")
    print("=" * 70)
    D = build_D_matrix64()
    print("D matrix built.")

    print("\n" + "=" * 70)
    print("Checking [D, su3_i] = 0 for all 8 su(3) generators")
    print("=" * 70)
    all_commute = True
    for i in range(1, 9):
        S = build_su3_matrix64(i)
        comm = sp.simplify(D * S - S * D)
        is_zero = comm == sp.zeros(64, 64)
        print(f"  [D, su3_{i}] == 0 ? {is_zero}")
        if not is_zero:
            all_commute = False
            nz = [
                (r, c, comm[r, c])
                for r in range(64)
                for c in range(64)
                if sp.simplify(comm[r, c]) != 0
            ]
            print(f"    Nonzero entries ({len(nz)} total), first 10:")
            for r, c, v in nz[:10]:
                sL_r, sR_r = SUBSETS[r // 8], SUBSETS[r % 8]
                sL_c, sR_c = SUBSETS[c // 8], SUBSETS[c % 8]
                print(f"      [{sL_r},{sR_r}] <- [{sL_c},{sR_c}]: {v}")

    print("\n" + "=" * 70)
    print(f"OVERALL: D is SU(3)-equivariant? {all_commute}")
    print("=" * 70)


if __name__ == "__main__":
    main()
