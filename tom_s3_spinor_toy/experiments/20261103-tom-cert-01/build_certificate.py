"""TOM-CERT-01 builder: constructs certificate.json for W = span{g_ab} in L^2(S^3).

Exact arithmetic only (sympy rationals / Gaussian rationals). No floating point anywhere.
The independent checker is verifier.py; it does NOT import this file and uses no sympy.

Conventions (frozen before any run; the verifier restates them on its own):
  S^3 = SU(2) via x = (x0, x1) in C^2, |x0|^2 + |x1|^2 = 1,  g(x) = [[x0, -conj(x1)], [x1, conj(x0)]].
  Formal variables z0, z1, w0, w1 stand for x0, x1, conj(x0), conj(x1).
  g_ab, a = row, b = column; basis order j = 2a + b: g00, g01, g10, g11.
  (L_h f)(x) = f(h^-1 x)                       left regular action, a homomorphism.
  (R_k f)(x) = f(x . k),  x . k = first column of g(x) k = k00 x + k10 J x,  J x = (-conj(x1), conj(x0)).
  su(2) basis T_a = -i sigma_a / 2, [T_a, T_b] = eps_abc T_c.
  dL(T) f = d/dt f(exp(-tT) x),  dR(T) f = d/dt f(x . exp(tT)),  at t = 0.
  Matrix of an operator in the basis: M[i][j] = coefficient of basis i in the image of basis j.
  J_a = i dL(T_a) (left), i dR(T_a) (right).
"""

import json
import sys
from pathlib import Path

import sympy as sp

z0, z1, w0, w1 = sp.symbols("z0 z1 w0 w1")
VARS = (z0, z1, w0, w1)
t = sp.Symbol("t", real=True)
I = sp.I
R = sp.Rational

# basis g_ab as polynomials in the formal variables
G = sp.Matrix([[z0, -w1], [z1, w0]])
BASIS = [G[0, 0], G[0, 1], G[1, 0], G[1, 1]]

SIGMA = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
T = [-I * s / 2 for s in SIGMA]


def conj_poly(p):
    p = sp.expand(p).subs({z0: w0, z1: w1, w0: z0, w1: z1}, simultaneous=True)
    return sp.expand(p).xreplace({I: -I})


def conj_mat(M):
    return M.applyfunc(lambda e: sp.expand(e).xreplace({I: -I}))


def left_subs(A):
    """x -> A x as a substitution on (z0, z1, w0, w1)."""
    Ab = conj_mat(A)
    return {
        z0: A[0, 0] * z0 + A[0, 1] * z1,
        z1: A[1, 0] * z0 + A[1, 1] * z1,
        w0: Ab[0, 0] * w0 + Ab[0, 1] * w1,
        w1: Ab[1, 0] * w0 + Ab[1, 1] * w1,
    }


def right_subs(k):
    """x -> x . k = k00 x + k10 J x."""
    kb = conj_mat(k)
    return {
        z0: k[0, 0] * z0 + k[1, 0] * (-w1),
        z1: k[0, 0] * z1 + k[1, 0] * w0,
        w0: kb[0, 0] * w0 + kb[1, 0] * (-z1),
        w1: kb[0, 0] * w1 + kb[1, 0] * z0,
    }


def apply(p, subs):
    return sp.expand(sp.sympify(p).subs(subs, simultaneous=True))


def express(p):
    """coefficients c with p = sum c_j BASIS[j], or None."""
    cs = sp.symbols("c0:4")
    expr = sp.expand(p - sum(c * b for c, b in zip(cs, BASIS)))
    eqs = sp.Poly(expr, *VARS).coeffs() if expr != 0 else []
    sol = sp.solve(eqs, cs, dict=True)
    if not sol:
        return None
    return [sp.nsimplify(sol[0][c]) for c in cs]


def matrix_of(op):
    cols = []
    for b in BASIS:
        c = express(op(b))
        if c is None:
            raise ValueError("image not in span(W): closure fails")
        cols.append(c)
    return sp.Matrix(4, 4, lambda i, j: cols[j][i])


def left_op(h):
    hinv = h.H  # SU(2): inverse = conjugate transpose
    return lambda p: apply(p, left_subs(hinv))


def right_op(k):
    return lambda p: apply(p, right_subs(k))


def dleft_op(Ta):
    return lambda p: sp.diff(apply(p, left_subs(sp.eye(2) - t * Ta)), t).subs(t, 0)


def dright_op(Ta):
    return lambda p: sp.diff(apply(p, right_subs(sp.eye(2) + t * Ta)), t).subs(t, 0)


def su2(a, b, c, d, den):
    a, b, c, d = (R(v, den) for v in (a, b, c, d))
    assert a * a + b * b + c * c + d * d == 1
    return sp.Matrix([[a + I * b, -c + I * d], [c + I * d, a - I * b]])


QUATS = [
    (1, 2, 2, 0, 3),
    (1, 2, 2, 4, 5),
    (2, 3, 6, 0, 7),
    (0, 2, 3, 6, 7),
    (1, 1, 1, 1, 2),
    (1, 4, 8, 0, 9),
]


def cplx(e):
    e = sp.nsimplify(sp.expand(e))
    return [str(sp.re(e)), str(sp.im(e))]


def mat_json(M):
    return [[cplx(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def poly_json(p):
    out = []
    for monom, coeff in sp.Poly(sp.expand(p), *VARS).terms():
        out.append([list(monom), *cplx(coeff)])
    return out


def main(out_path):
    cert = {
        "schema": "tom-cert-01/1",
        "subject": "W = span{g_ab} in L^2(S^3), S^3 = SU(2): left/right actions, closure, decompositions",
        "conventions": {
            "g": "g(x) = [[x0, -conj x1], [x1, conj x0]]",
            "variables": "z0=x0, z1=x1, w0=conj x0, w1=conj x1 (formal)",
            "basis_order": "j = 2a + b: g00, g01, g10, g11",
            "L": "(L_h f)(x) = f(h^-1 x)",
            "R": "(R_k f)(x) = f(x.k), x.k = k00 x + k10 J x, J x = (-conj x1, conj x0)",
            "T": "T_a = -i sigma_a / 2",
            "dL": "d/dt f(exp(-tT) x)",
            "dR": "d/dt f(x . exp(tT))",
            "matrix": "M[i][j] = coefficient of basis i in image of basis j",
        },
        "basis": [poly_json(b) for b in BASIS],
        "generators": [mat_json(Ta) for Ta in T],
    }
    cert["dL"] = [mat_json(matrix_of(dleft_op(Ta))) for Ta in T]
    cert["dR"] = [mat_json(matrix_of(dright_op(Ta))) for Ta in T]

    elems = []
    for q in QUATS:
        a, b, c, d, den = q
        elems.append((q, False))
        elems.append(((a, -b, -c, -d, den), True))  # inverse = quaternion conjugate
    group = []
    for (a, b, c, d, den), is_inv in elems:
        h = su2(a, b, c, d, den)
        group.append(
            {
                "quaternion": [a, b, c, d, den],
                "L_matrix": mat_json(matrix_of(left_op(h))),
                "R_matrix": mat_json(matrix_of(right_op(h))),
            }
        )
    cert["group_elements"] = group
    cert["homomorphism_pairs"] = [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [1, 3], [0, 3], [5, 8]]

    cert["decomposition"] = {
        "left_blocks": [[0, 2], [1, 3]],
        "right_blocks": [[0, 1], [2, 3]],
        "left_blocks_note": "fixed column b: span{g_0b, g_1b}",
        "right_blocks_note": "fixed row a: span{g_a0, g_a1}",
        "casimir_L": "3/4",
        "casimir_R": "3/4",
        "weights_J3L_J3R": [["-1/2", "1/2"], ["-1/2", "-1/2"], ["1/2", "1/2"], ["1/2", "-1/2"]],
        "commutant_dim": {
            "full_LR": 1,
            "left_only": 4,
            "right_only": 4,
            "left_block": 1,
            "right_block": 1,
        },
        "epsilon": [[["0", "0"], ["1", "0"]], [["-1", "0"], ["0", "0"]]],
    }
    cert["gram"] = [["1/2" if i == j else "0" for j in range(4)] for i in range(4)]

    Path(out_path).write_text(json.dumps(cert, indent=1, sort_keys=True), encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "certificate.json"))
