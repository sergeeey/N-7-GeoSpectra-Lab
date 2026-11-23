#!/usr/bin/env python3
"""C248: exact sympy check of the SU(2) differential generators on C^2 (dragged scalar field).

D_a = -1/2 (sigma_a xi).d_xi + 1/2 (sigma_a* barxi).d_barxi. The doublet xi/r obeys
D_a psi = -1/2 sigma_a psi; the phased doublet (xi1, i xi2) obeys the same identity only with
sigma'_a = U sigma_a U^-1, U = diag(1, i). Not a reconstruction of any later operator of the
correspondent. Provenance: external script received 2026-11-24 (sha256 15a01cd15d98169c...),
copied with ruff fixes, this docstring, and check() exiting non-zero instead of assert.
Run: python -I verify_factor_i_basis_rotation.py
"""

import sys

import sympy as s

I = s.I
x, y, bx, by = s.symbols("xi1 xi2 barxi1 barxi2")
coords = s.Matrix([x, y, bx, by])
xi = s.Matrix([x, y])
barxi = s.Matrix([bx, by])
sigma = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -I], [I, 0]]), s.diag(1, -1)]
# Derived from dragged scalar field: D_a=-1/2(sigma_a xi).d_xi+1/2(sigma_a* barxi).d_barxi
V = [s.Matrix(list(-S * xi / 2) + list(s.conjugate(S) * barxi / 2)) for S in sigma]


def D(v, f):
    return s.expand(sum(v[k] * s.diff(f, coords[k]) for k in range(4)))


def action(v, w):
    return s.Matrix([D(v, f) for f in w])


def zero(w):
    return all(s.simplify(z) == 0 for z in w)


N = 0


def check(label, truth):
    global N
    # WHY: not assert, which python -O strips (review 2026-11-24); exit non-zero instead
    if not truth:
        print("FAIL", label)
        sys.exit(1)
    N += 1
    print("PASS", label)


for a in range(3):
    check(f"radius invariant D{a + 1}", D(V[a], x * bx + y * by) == 0)
for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    bracket = s.Matrix([D(V[a], z) - D(V[b], t) for z, t in zip(V[b], V[a])])
    check(f"Lie bracket [{a + 1},{b + 1}]", zero(bracket - I * V[c]))
Dplus = V[0] + I * V[1]
Dminus = V[0] - I * V[1]
for a, b, expect in [(Dminus, x, 0), (Dplus, x, -y), (Dminus, y, -x), (Dplus, y, 0)]:
    check(f"ladder {len(str(b))}:{expect!s}", s.simplify(D(a, b) - expect) == 0)
for a in range(3):
    check(f"unphased Pauli identity D{a + 1}", zero(action(V[a], xi) + sigma[a] * xi / 2))
U = s.diag(1, I)
phased = U * xi
for a in range(3):
    check(
        f"phased covariance with U sigma U^-1 D{a + 1}",
        zero(action(V[a], phased) + (U * sigma[a] * U.inv()) * phased / 2),
    )
check(
    "phased original Pauli identity fails D1",
    not zero(action(V[0], phased) + sigma[0] * phased / 2),
)
check(
    "phased original Pauli identity fails D2",
    not zero(action(V[1], phased) + sigma[1] * phased / 2),
)
check(
    "phased original Pauli identity holds D3",
    zero(action(V[2], phased) + sigma[2] * phased / 2),
)
check("phased original ladder D+ fails", s.simplify(D(Dplus, phased[0]) + phased[1]) != 0)
check("phased original ladder D- fails", s.simplify(D(Dminus, phased[1]) + phased[0]) != 0)
check(
    "phased original ladder zeros hold",
    D(Dminus, phased[0]) == D(Dplus, phased[1]) == 0,
)
print(f"{N} exact SymPy checks passed")
print(
    "Original ladder residuals phased:",
    [
        D(Dminus, phased[0]),
        s.expand(D(Dplus, phased[0]) + phased[1]),
        s.expand(D(Dminus, phased[1]) + phased[0]),
        D(Dplus, phased[1]),
    ],
)
print("Transformed sigma:", [str(U * S * U.inv()) for S in sigma])
