r"""
C196 -- does S^2 carry an infinite TOWER of genuine spin-weighted harmonics,
the same way S^3's harmonics form a tower by k, or is chi_{+-1/2} (C184b, k=1)
an isolated special case?

This strengthens the reply's central synthesis on Tom's question ("is the
spinor multiplet absent from harmonic decomposition on S^2, on S^3, or
both?") from a [MEMORY]/textbook citation (spin-weighted spherical harmonics
are standard, Newman-Penrose et al.) to a [VERIFIED-tool] fact produced by
THIS project's own machinery: the same fibre-descent method C184b used once
(k=1) is applied again at k=3 -- the next available half-integer level -- and
must give a SECOND, genuinely double-valued, non-proportional S^2 object if
"S^2 has spin-weighted harmonics too" is really true and not merely asserted.

Reused verbatim from c184b_descent_derivation.py:
  - HOPF dict, X3L/X3R generators, weight_sectors(), restrict_and_split()
"""

import sympy as sp

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
X = (x0, x1, x2, x3)
th, ph, ps = sp.symbols("theta phi psi", real=True)

HOPF = {
    x0: sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    x1: sp.sin(th / 2) * sp.sin((ph - ps) / 2),
    x2: -sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    x3: -sp.cos(th / 2) * sp.sin((ph + ps) / 2),
}

OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


def X3R(f):
    return sp.expand(
        -x3 * sp.diff(f, x0)
        + x2 * sp.diff(f, x1)
        - x1 * sp.diff(f, x2)
        + x0 * sp.diff(f, x3)
    )


def X3L(f):
    return sp.expand(
        -x3 * sp.diff(f, x0)
        - x2 * sp.diff(f, x1)
        + x1 * sp.diff(f, x2)
        + x0 * sp.diff(f, x3)
    )


FIBRE = X3L


def weight_sectors(basis):
    n = len(basis)
    cols = []
    for b in basis:
        img = FIBRE(b)
        lam = sp.symbols(f"L0:{n}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, basis)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.simplify(sol.get(lc, 0)) for lc in lam])
    M = sp.Rational(1, 2) * sp.I * sp.Matrix(cols).T
    out = {}
    for w, _mult, vecs in M.eigenvects():
        out[sp.nsimplify(w)] = [
            sp.expand(sum(v[i] * basis[i] for i in range(n))) for v in vecs
        ]
    return out


def restrict_and_split(vectors, op):
    n = len(vectors)
    cols = []
    for b in vectors:
        img = op(b)
        lam = sp.symbols(f"M0:{n}")
        eq = sp.expand(img - sum(lc * bb for lc, bb in zip(lam, vectors)))
        sol = sp.solve(sp.Poly(eq, *X).coeffs(), lam, dict=True)
        sol = sol[0] if sol else {}
        cols.append([sp.simplify(sol.get(lc, 0)) for lc in lam])
    M = sp.Rational(1, 2) * sp.I * sp.Matrix(cols).T
    out = []
    for w, _m, vs in M.eigenvects():
        for v in vs:
            out.append(
                (sp.nsimplify(w), sp.expand(sum(v[i] * vectors[i] for i in range(n))))
            )
    return sorted(out, key=lambda z: -sp.re(z[0]))


print("=" * 78)
print("A  build the k=3 harmonic level (degree-3, Laplacian-free) on S^3")
print("=" * 78)
MON3 = [
    x0**a * x1**b * x2**c * x3 ** (3 - a - b - c)
    for a in range(4)
    for b in range(4 - a)
    for c in range(4 - a - b)
]
cf = sp.symbols(f"z0:{len(MON3)}")
gen = sum(c * m for c, m in zip(cf, MON3))
lap = sp.expand(sum(sp.diff(gen, v, 2) for v in X))
sol = sp.solve(sp.Poly(lap, *X).coeffs(), cf, dict=True)
sol = sol[0] if sol else {}
free = [c for c in cf if c not in sol]
LEVEL3 = []
for fcv in free:
    e = sp.expand(gen.subs(sol).subs({c: (1 if c == fcv else 0) for c in cf}))
    if e != 0:
        LEVEL3.append(e)
check(
    "A1 k=3 harmonic level has dimension 16 (the (3/2,3/2) representation, dim (2*3/2+1)^2)",
    len(LEVEL3) == 16,
    f"found dim {len(LEVEL3)}",
)

print()
print("=" * 78)
print("B  diagonalise the fibre generator -- confirm HALF-integer weights at odd k")
print("=" * 78)
sectors3 = weight_sectors(LEVEL3)
print(f"  k=3 fibre weights present: {sorted(sectors3, key=lambda z: sp.re(z))}")
check(
    "B1 k=3 carries only HALF-integer fibre weights (odd k, opposite of C184b's "
    "own even-k=2 integer-weight negative control)",
    all(sp.nsimplify(w).q == 2 for w in sectors3),
)
check(
    "B2 CORRECTED: each fibre-weight sector at k=3 is 4-dimensional (degenerate, "
    "mirroring C184b's own k=1 degeneracy) -- a naive 'already split' assumption "
    "was wrong and is replaced below by the same second-generator split C184b used",
    len(sectors3[sp.Rational(3, 2)]) == 4 and len(sectors3[sp.Rational(-3, 2)]) == 4,
)

print()
print("=" * 78)
print("B'  split the degenerate weight=-3/2 sector with the second generator X3R")
print("=" * 78)
labelled3 = restrict_and_split(sectors3[sp.Rational(-3, 2)], X3R)
check(
    "B3 the second generator splits the 4-dim sector into 4 DISTINCT labels m_R = -3/2..3/2",
    sorted(sp.nsimplify(m) for m, _ in labelled3)
    == [sp.Rational(-3, 2), sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(3, 2)],
)
for m, v in labelled3:
    print(f"  fibre weight -3/2, m_R = {m!s:>4}:  {sp.simplify(v)}")

print()
print("=" * 78)
print("C  substitute Hopf, strip the psi phase, on the labelled m_R=-3/2 member")
print("=" * 78)
v_top = dict(labelled3)[sp.Rational(-3, 2)]
r = sp.simplify(sp.expand(v_top.subs(HOPF).rewrite(sp.exp)))
alpha = sp.simplify(sp.diff(r, ps) / (sp.I * r))
q_top = sp.simplify(sp.powsimp(sp.expand(r * sp.exp(-sp.I * alpha * ps)), force=True))
print(f"  psi-exponent alpha = {alpha}")
print(f"  stripped weight=-3/2 function of (theta,phi): {q_top}")
check(
    "C1 psi enters as a pure phase here too (alpha constant, independent of theta/phi)",
    sp.simplify(sp.diff(alpha, th)) == 0 and sp.simplify(sp.diff(alpha, ph)) == 0,
)
check(
    "C2 the stripped result depends on (theta, phi) only -- psi has genuinely dropped out",
    sp.simplify(sp.diff(q_top, ps)) == 0,
)

print()
print("=" * 78)
print(
    "D  is this a GENUINE new object -- double-valued, and NOT proportional to chi_{-1/2}?"
)
print("=" * 78)
check(
    "D1 q_top is double-valued under phi -> phi+2pi: q_top(phi+2pi) = -q_top(phi)",
    sp.simplify(q_top.subs(ph, ph + 2 * sp.pi) + q_top) == 0,
)
chi_minus_half = sp.exp(sp.I * ph / 2) * sp.sin(th / 2)
ratio = sp.simplify(sp.powsimp(sp.expand(q_top / chi_minus_half), force=True))
not_proportional = (
    sp.simplify(sp.diff(ratio, th)) != 0 or sp.simplify(sp.diff(ratio, ph)) != 0
)
check(
    "D2 q_top is NOT a constant multiple of C184's chi_{-1/2} -- a genuinely "
    "distinct, second member of the S^2 spin-weighted family, not a rescaled repeat",
    not_proportional,
    f"ratio depends on angles: {ratio}",
)

print()
print("=" * 78)
print("NEGATIVE CONTROL  a genuinely single-valued function cannot pass D1")
print("=" * 78)
check(
    "N1 an ordinary (integer-weight, single-valued) function does NOT satisfy "
    "f(phi+2pi) = -f(phi) -- confirms D1 is a real, failable discriminator",
    sp.simplify(sp.cos(ph).subs(ph, ph + 2 * sp.pi) + sp.cos(ph)) != 0,
)

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
print(
    "FAILED: " + "; ".join(failed)
    if failed
    else "S^2 carries a genuine second rung of the spin-weighted tower, by the "
    "same descent method that produced chi_{+-1/2} -- not an isolated case"
)
