r"""
C197 -- the actual second spin-1/2 S^2 harmonic, at k=3, fibre weight -1/2
(NOT the extremal -3/2 sector C196 computed, which is spin-weight 3/2).

Round-3 skeptic pass on the letter to Tom (2026-09-10) found that C196's own
run_output.txt already prints the fibre weights present at k=3:
"[-3/2, -1/2, 1/2, 3/2]" -- and that the weight=-1/2 sector, one step away in
the SAME script, is the genuine second member of the spin-1/2 tower
(_{1/2}Y_{3/2,m}), not yet computed. This experiment computes it.

Reused verbatim from c196_s2_higher_spin_weight.py (itself reusing
c184b_descent_derivation.py's HOPF dict, X3L/X3R, weight_sectors(),
restrict_and_split()).
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
print("A  rebuild the k=3 harmonic level (same as C196)")
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
check("A1 k=3 harmonic level has dimension 16", len(LEVEL3) == 16)

sectors3 = weight_sectors(LEVEL3)

print()
print("=" * 78)
print("B  split the weight=-1/2 sector (NOT the -3/2 extremal C196 used)")
print("=" * 78)
check(
    "B1 weight=-1/2 sector is 4-dimensional, like -3/2",
    len(sectors3[sp.Rational(-1, 2)]) == 4,
)
labelled = restrict_and_split(sectors3[sp.Rational(-1, 2)], X3R)
check(
    "B2 second generator splits it into 4 distinct m_R labels -3/2..3/2",
    sorted(sp.nsimplify(m) for m, _ in labelled)
    == [sp.Rational(-3, 2), sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(3, 2)],
)
for m, v in labelled:
    print(f"  fibre weight -1/2, m_R = {m!s:>4}:  {sp.simplify(v)}")

print()
print("=" * 78)
print("C  substitute Hopf, strip the psi phase, on the m_R=-1/2 member")
print("=" * 78)
v_pick = dict(labelled)[sp.Rational(-1, 2)]
r = sp.simplify(sp.expand(v_pick.subs(HOPF).rewrite(sp.exp)))
alpha = sp.simplify(sp.diff(r, ps) / (sp.I * r))
q = sp.simplify(sp.powsimp(sp.expand(r * sp.exp(-sp.I * alpha * ps)), force=True))
print(f"  psi-exponent alpha = {alpha}")
check(
    "C1 alpha = -1/2, the SAME weight as chi_{+-1/2} itself -- spin weight 1/2, not 3/2",
    sp.simplify(alpha - sp.Rational(-1, 2)) == 0,
)
check(
    "C2 psi has genuinely dropped out (algebraic sanity check on the "
    "phase-stripping step, not itself a physics claim)",
    sp.simplify(sp.diff(q, ps)) == 0,
)

# fold to closed trig form for the letter
q_folded = sp.simplify(sp.trigsimp(sp.expand_complex(q)))
print(f"  stripped, folded: {q_folded}")

closed_form = sp.exp(-sp.I * ph / 2) * sp.cos(th / 2) * (3 * sp.cos(th / 2) ** 2 - 2)
# WHY 5 points, not 1 (post-hoc hardening, 2026-09-16, per a skeptic finding
# during an unrelated harness test): this exact closed form is quoted
# verbatim in a letter sent to Tom Lawrence, so a single lucky-coincidence
# point is not enough scrutiny for it. Points chosen to span both halves of
# theta and both signs/quadrants of phi, none a special value where an
# error could cancel by symmetry.
CHECK_POINTS = [
    {th: sp.Rational(7, 10), ph: sp.Rational(11, 10)},
    {th: sp.Rational(1, 5), ph: sp.Rational(-3, 4)},
    {th: sp.Rational(13, 10), ph: sp.Rational(5, 2)},
    {th: sp.Rational(3, 4), ph: sp.Rational(-11, 3)},
    {th: sp.Rational(29, 10), ph: sp.Rational(1, 17)},
]
closed_form_diffs = [
    abs(complex(q_folded.subs(pt).evalf(30)) - complex(closed_form.subs(pt).evalf(30)))
    for pt in CHECK_POINTS
]
print(f"  closed-form residuals at {len(CHECK_POINTS)} points: {closed_form_diffs}")
check(
    "C3 closed form e^{-i phi/2} cos(theta/2) (3cos^2(theta/2)-2) matches, "
    f"numerically to 30 digits at {len(CHECK_POINTS)} points spanning both "
    "halves of theta and multiple phi quadrants (symbolic simplify does not "
    "auto-collapse this one)",
    all(d < 1e-25 for d in closed_form_diffs),
)
print("  closed form: e^(-i*phi/2) * cos(theta/2) * (3*cos(theta/2)^2 - 2)")

print()
print("=" * 78)
print("D  genuinely new: double-valued, not proportional to chi_{-1/2} or chi_{+1/2}")
print("=" * 78)
check(
    "D1 double-valued: q(phi+2pi) = -q(phi)",
    sp.simplify(q.subs(ph, ph + 2 * sp.pi) + q) == 0,
)
chi_p = sp.exp(-sp.I * ph / 2) * sp.cos(th / 2)
chi_m = sp.exp(sp.I * ph / 2) * sp.sin(th / 2)
# WHY a concrete numeric check ALONGSIDE the symbolic one (post-hoc
# hardening, 2026-09-16): "sp.diff(ratio) != 0" is only as trustworthy as
# sympy's own simplification of that derivative -- a nonzero expression
# sympy fails to reduce to a literal 0 would report as "not proportional"
# even where the true ratio IS constant, and vice versa if a genuinely
# nonzero derivative fails to simplify away spurious phase factors. This
# is a concrete, tool-independent belt-and-suspenders control: if the
# ratio is truly non-constant, it must take at least two DIFFERENT numeric
# values -- a fact no simplification bug can hide.
RATIO_POINTS = [sp.Rational(1, 5), sp.Rational(3, 2)]
for name, chi in (("chi_{+1/2}", chi_p), ("chi_{-1/2}", chi_m)):
    ratio = sp.simplify(sp.powsimp(sp.expand(q / chi), force=True))
    not_prop_symbolic = sp.simplify(sp.diff(ratio, th)) != 0
    ratio_values = [
        complex(ratio.subs({th: t0, ph: sp.Rational(9, 10)}).evalf(30))
        for t0 in RATIO_POINTS
    ]
    not_prop_numeric = abs(ratio_values[0] - ratio_values[1]) > 1e-20
    check(
        f"D2 NOT a constant multiple of {name} (genuinely new content, "
        "not merely non-proportional by construction as in C196's weight-mismatch case) "
        "-- symbolic AND numeric checks agree",
        not_prop_symbolic and not_prop_numeric,
        f"ratio = {ratio}, values at theta={RATIO_POINTS} = {ratio_values}",
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
    else "a genuine second spin-1/2 harmonic found at k=3, distinct from k=1's chi_{+-1/2}"
)
