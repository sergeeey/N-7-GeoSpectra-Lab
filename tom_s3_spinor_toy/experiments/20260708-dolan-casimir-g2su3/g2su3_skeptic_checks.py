"""
Skeptic-requested independent checks (round 3), NOT exercised by the
calibration check or by the rep-theory forcing argument:

Check 1: Compute D on the single non-SU(3)-invariant term y1(x)y23 ALONE
(before combining into v_a = y1(x)y23 - y2(x)y13 + y3(x)y12), project onto
w=1(x)1. By the expected S3-cyclic-like symmetry of the construction, this
should come out to exactly -sqrt(3)/3 * w if the total c_a=-sqrt(3) is a
genuine symmetric sum, not a sign-cancellation artifact. Also check the
other two terms individually.

Check 2: Chirality operator gamma_7 = e1.e2.e3.e4.e5.e6 applied to "1" and
to "y123" -- must give +-1 with OPPOSITE signs (tests 6-fold iterated
Clifford product, completely unexercised by calibration).
"""

import sympy as sp
from g2su3_explicit_clifford import (
    IDX,
    e_action,
    vec_from_subsets,
    print_vec,
)
from g2su3_compute_crossterm import D_on_simple_tensor

sqrt = sp.sqrt


def check1():
    print("=" * 70)
    print("CHECK 1 (skeptic-requested): individual term contributions to c_a")
    print("=" * 70)

    y1 = vec_from_subsets({(1,): 1})
    y2 = vec_from_subsets({(2,): 1})
    y3 = vec_from_subsets({(3,): 1})
    y12 = vec_from_subsets({(1, 2): 1})
    y13 = vec_from_subsets({(1, 3): 1})
    y23 = vec_from_subsets({(2, 3): 1})

    terms = [
        ("y1(x)y23", D_on_simple_tensor(y1, y23), 1),
        ("y2(x)y13", D_on_simple_tensor(y2, y13), -1),
        ("y3(x)y12", D_on_simple_tensor(y3, y12), 1),
    ]

    total = sp.Integer(0)
    for name, d, sign in terms:
        w_coeff = d.get(((), ()), 0)
        other = {k: v for k, v in d.items() if k != ((), ())}
        print(f"\n  D({name}) coefficient of w=1(x)1: {w_coeff}")
        print(f"    (with sign {sign:+d} in v_a, contributes {sign * w_coeff})")
        print(f"    other (non-w) components: {other}")
        total += sign * w_coeff

    print(f"\n  Sum (should equal -sqrt(3), matching earlier D(v_a) result): {sp.simplify(total)}")
    expected_symmetric = -sqrt(3) / 3
    print(f"  Expected value IF perfectly symmetric per-term: {sp.simplify(expected_symmetric)}")
    print(
        f"  Actual individual (unsigned) values: {[sp.simplify(d.get(((), ()), 0)) for _, d, _ in terms]}"
    )


def check2():
    print("\n" + "=" * 70)
    print("CHECK 2 (skeptic-requested): chirality operator gamma_7 = e1.e2.e3.e4.e5.e6")
    print("=" * 70)

    one = vec_from_subsets({(): 1})
    y123 = vec_from_subsets({(1, 2, 3): 1})

    def gamma7(vec):
        out = vec
        for i in [6, 5, 4, 3, 2, 1]:  # apply e1 last (leftmost), i.e. e1.e2.e3.e4.e5.e6.vec
            out = e_action(i, out)
        return out

    g_one = gamma7(one)
    g_y123 = gamma7(y123)

    print("\n  gamma_7 . 1 =")
    print_vec(sp.simplify(g_one), "    ")
    print("\n  gamma_7 . y123 =")
    print_vec(sp.simplify(g_y123), "    ")

    c1 = sp.simplify(g_one[IDX[()]])
    c2 = sp.simplify(g_y123[IDX[(1, 2, 3)]])
    print(f"\n  gamma_7 eigenvalue on '1'    : {c1}")
    print(f"  gamma_7 eigenvalue on 'y123' : {c2}")
    print(f"  Opposite signs (as required)?: {sp.simplify(c1 + c2) == 0 and c1 != 0}")


if __name__ == "__main__":
    check1()
    check2()
