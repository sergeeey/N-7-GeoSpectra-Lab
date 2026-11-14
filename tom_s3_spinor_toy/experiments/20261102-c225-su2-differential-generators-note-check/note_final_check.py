"""Check of the sent note SU2_differential_generators_note_final.pdf (29 Oct 2026).

N1. D_a from the definition: U(g_a(t)) f = f + i t D_a f + O(t^2), with
    (U f)(xi, xibar) = f(g^{-1} xi, conj(g^{-1} xi)) and g_a(t) = exp(i t sigma_a / 2).
    Computed by differentiating in t at t = 0 for a GENERIC function F(xi1, xi2, xib1, xib2).
N2. The three operators of the note equal the expressions derived in N1.
N3. Commutators [D1,D2] = i D3, [D2,D3] = i D1, [D3,D1] = i D2 for a GENERIC function F
    (not polynomials), using xi and xibar as independent symbols (Wirtinger calculus).
N4. Eigenvalues of D3 on xi^1, xi^2, xib^1, xib^2 as stated: -1/2, +1/2, +1/2, -1/2.
N5. Monomial formula D3[(xi1)^p (xi2)^q (xib1)^r (xib2)^s] = (-p+q+r-s)/2 * monomial, checked symbolically
    for p,q,r,s up to 3 (a formula check, not a proof for all exponents).
"""

import sympy as sp

x1, x2, y1, y2 = sp.symbols(
    "x1 x2 y1 y2"
)  # xi^1, xi^2, conj xi^1, conj xi^2 as independent symbols
F = sp.Function("F")(x1, x2, y1, y2)
I = sp.I


def d(f, v):
    return sp.diff(f, v)


def D1(f):
    return -sp.Rational(1, 2) * (x2 * d(f, x1) + x1 * d(f, x2)) + sp.Rational(1, 2) * (
        y2 * d(f, y1) + y1 * d(f, y2)
    )


def D2(f):
    return I / 2 * (x2 * d(f, x1) - x1 * d(f, x2) + y2 * d(f, y1) - y1 * d(f, y2))


def D3(f):
    return sp.Rational(1, 2) * (-x1 * d(f, x1) + x2 * d(f, x2) + y1 * d(f, y1) - y2 * d(f, y2))


fails = []


def check(name, expr):
    s = sp.simplify(sp.expand(expr))
    ok = s == 0
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  residual=%s" % s))
    if not ok:
        fails.append(name)


# N1: definition-based derivative. Work with the matrix exponential to first order in t.
t = sp.symbols("t", real=True)
xi = sp.Matrix([x1, x2])
xib = sp.Matrix([y1, y2])


def first_order_D(sigma):
    # g^{-1} = exp(-i t sigma/2) ~ 1 - i t sigma/2 (first order)
    ginv = sp.eye(2) - I * t * sigma / 2
    newxi = ginv * xi
    newxib = (ginv.conjugate()) * xib  # conj(g^{-1} xi) = conj(g^{-1}) conj(xi)
    # F(new) to first order in t
    sub = {x1: newxi[0], x2: newxi[1], y1: newxib[0], y2: newxib[1]}
    Fnew = F.subs(sub, simultaneous=True)
    # d/dt at t=0 of F(new)  =  sum over variables of dF * d(new)/dt
    dFdt = sp.diff(Fnew, t).subs(t, 0)
    return sp.simplify(dFdt / I)  # U f = f + i t D f  => D f = (1/i) d/dt


s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])

D1def = first_order_D(s1)
D2def = first_order_D(s2)
D3def = first_order_D(s3)

check("N1a D1 from definition equals the note's D1", D1def - D1(F))
check("N1b D2 from definition equals the note's D2", D2def - D2(F))
check("N1c D3 from definition equals the note's D3", D3def - D3(F))

# N3 commutators on a generic function
check("N3a [D1,D2] F - i D3 F = 0", D1(D2(F)) - D2(D1(F)) - I * D3(F))
check("N3b [D2,D3] F - i D1 F = 0", D2(D3(F)) - D3(D2(F)) - I * D1(F))
check("N3c [D3,D1] F - i D2 F = 0", D3(D1(F)) - D1(D3(F)) - I * D2(F))

# N4 eigenvalues
check("N4a D3 xi1 = -1/2 xi1", D3(x1) + sp.Rational(1, 2) * x1)
check("N4b D3 xi2 = +1/2 xi2", D3(x2) - sp.Rational(1, 2) * x2)
check("N4c D3 conj(xi1) = +1/2 conj(xi1)", D3(y1) - sp.Rational(1, 2) * y1)
check("N4d D3 conj(xi2) = -1/2 conj(xi2)", D3(y2) + sp.Rational(1, 2) * y2)

# N5 monomial formula
ok5 = True
for p in range(4):
    for q in range(4):
        for r in range(4):
            for s in range(4):
                mono = x1**p * x2**q * y1**r * y2**s
                lhs = D3(mono)
                rhs = sp.Rational(-p + q + r - s, 2) * mono
                if sp.expand(lhs - rhs) != 0:
                    ok5 = False
check(
    "N5 D3 monomial formula (-p+q+r-s)/2 for p,q,r,s <= 3", sp.Integer(0) if ok5 else sp.Integer(1)
)

print("\nFAILS:", fails if fails else "none")
