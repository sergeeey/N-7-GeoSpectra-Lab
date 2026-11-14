"""Diagnose the Q2/Q3 failure: is [spin_lift(X),spin_lift(Y)] proportional
to spin_lift([X,Y]_so6) by a SINGLE consistent scale factor (a normalization
mismatch, like C192's k=-2), or a genuine structural break?
"""

import importlib.util
import random
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
R59_PATH = (
    HERE.parent / "20260714-round59-trivial-rank-certification" / "round59_route_a_independent.py"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


R59 = load_module("r59", R59_PATH)
E = R59.build_clifford(conj=False)


def matrix_to_terms(X):
    terms = []
    for a in range(1, 7):
        for b in range(a + 1, 7):
            c = X[a - 1, b - 1]
            if sp.simplify(c) != 0:
                terms.append((c, a, b))
    return terms


def terms_to_matrix(terms):
    M = sp.zeros(6, 6)
    for c, a, b in terms:
        M[a - 1, b - 1] += c
        M[b - 1, a - 1] -= c
    return M


random.seed(20260909)


def random_antisym_6x6(scale=3):
    M = sp.zeros(6, 6)
    for a in range(6):
        for b in range(a + 1, 6):
            v = sp.Rational(random.randint(-scale, scale), 1)
            M[a, b] = v
            M[b, a] = -v
    return M


X = random_antisym_6x6()
Y = random_antisym_6x6()
Xt, Yt = matrix_to_terms(X), matrix_to_terms(Y)

liftX = R59.spin_lift(Xt, E)
liftY = R59.spin_lift(Yt, E)
lhs = liftX * liftY - liftY * liftX

comm_mat = X * Y - Y * X
comm_terms = matrix_to_terms(comm_mat)
rhs = R59.spin_lift(comm_terms, E)

print("lhs == rhs?", sp.simplify(lhs - rhs) == sp.zeros(8, 8))
print("lhs == 0.5*rhs?", sp.simplify(lhs - sp.Rational(1, 2) * rhs) == sp.zeros(8, 8))
print("lhs == 2*rhs?", sp.simplify(lhs - 2 * rhs) == sp.zeros(8, 8))

# print a few nonzero entries of the ratio to eyeball
diffs = []
for i in range(8):
    for j in range(8):
        if sp.simplify(rhs[i, j]) != 0:
            ratio = sp.simplify(lhs[i, j] / rhs[i, j])
            diffs.append(ratio)
print("sample nonzero-rhs entrywise ratios lhs/rhs:", diffs[:10])
