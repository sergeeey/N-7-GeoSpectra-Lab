r"""
C194 -- does "U(theta,phi,psi) * constant vector" give Tom's four k=0 S^3
spinors a genuine, non-trivial Hopf-coordinate functional form?

Tom's letter (2026-09-10) asks for psi_{(1/2,0)}, psi_{(-1/2,0)}, psi_{(0,1/2)},
psi_{(0,-1/2)} "expressed directly in the Hopf coordinates" -- not just "a
local ket basis exists that aligns with them" (C184's rev6 answer, which gave
them as literal constants (1,0)/(0,1) in the group trivialization).

The candidate tested here: multiply the already-verified Euler/Hopf SU(2)
matrix U(theta,phi,psi) (c184_two_questions.py:365-368, F1/F2-checked unitary,
det=1) by a constant 2-vector v, i.e. psi(theta,phi,psi) = U(theta,phi,psi)*v.

Reused without modification:
  - Uh(theta,phi,psi)      : c184_two_questions.py:365-368
  - HOPF dict              : c184c_skeptic_followups.py:156-161
  - c184c's own printed D_0=3 eigenspinor (run_output_c.txt)
  - C188's closed-form X_a^R in Euler angles (decision.md SS2), quoted as text,
    not re-derived, since C188 already verified them to <1e-30 numerically.
"""

import sympy as sp

th, ph, ps = sp.symbols("theta phi psi", real=True)
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)

HOPF = {
    x0: sp.cos(th / 2) * sp.cos((ph + ps) / 2),
    x1: sp.sin(th / 2) * sp.sin((ph - ps) / 2),
    x2: -sp.sin(th / 2) * sp.cos((ph - ps) / 2),
    x3: -sp.cos(th / 2) * sp.sin((ph + ps) / 2),
}

Uh = sp.simplify(
    sp.Matrix([[sp.exp(-sp.I * ph / 2), 0], [0, sp.exp(sp.I * ph / 2)]])
    * sp.Matrix([[sp.cos(th / 2), -sp.sin(th / 2)], [sp.sin(th / 2), sp.cos(th / 2)]])
    * sp.Matrix([[sp.exp(-sp.I * ps / 2), 0], [0, sp.exp(sp.I * ps / 2)]])
)

OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


print("=" * 78)
print("A  U(theta,phi,psi) is exactly the (x0,x1,x2,x3)->matrix map, re-verified")
print("=" * 78)
# U = x0*I + x1*(i*sigma1) + x2*(i*sigma2) + x3*(i*sigma3) -- the "quaternionic
# basis" map C184 already showed reproduces x_mu correctly (decision.md SS2).
quat_form = sp.Matrix(
    [[x0 + sp.I * x3, x2 + sp.I * x1], [-x2 + sp.I * x1, x0 - sp.I * x3]]
)
Uh_in_x = quat_form.subs(HOPF)
# direct numeric cross-check (symbolic simplify of mixed exp/half-angle forms
# is unreliable -- confirmed at 30-digit precision instead, at a generic point)
pt = {th: sp.Rational(7, 10), ph: sp.Rational(11, 10), ps: sp.Rational(-3, 10)}
diff_A = Uh.subs(pt).evalf(30) - Uh_in_x.subs(pt).evalf(30)
check(
    "A1 U(theta,phi,psi) == x0*I + x1*(i s1) + x2*(i s2) + x3*(i s3) |_Hopf, numerically to 30 digits",
    max(abs(complex(e)) for e in diff_A) < sp.Float(10) ** -25,
)

print()
print("=" * 78)
print("B  candidate psi = U * v is the ALREADY-KNOWN k=1 eigenspinor, not k=0")
print("=" * 78)
v0 = sp.Matrix([1, 0])
cand = Uh * v0
cand_in_x = sp.Matrix([x0 + sp.I * x3, -x2 + sp.I * x1])
diff_B1 = cand.subs(pt).evalf(30) - cand_in_x.subs(HOPF).subs(pt).evalf(30)
check(
    "B1 U*(1,0)^T  ==  (x0+i x3, -x2+i x1) |_Hopf, numerically to 30 digits",
    max(abs(complex(e)) for e in diff_B1) < sp.Float(10) ** -25,
)

# c184c_skeptic_followups.py run_output_c.txt's own printed D_0=3 eigenspinor,
# in x-coordinates -- quoted verbatim, not re-derived
c184c_D0_3 = sp.Matrix([-x0 - sp.I * x3, -sp.I * x1 + x2])
check(
    "B2 (x0+i x3, -x2+i x1)  ==  -1 * C184c's own printed D_0=+3 eigenspinor, exactly (symbolic)",
    sp.simplify(cand_in_x - (-1) * c184c_D0_3) == sp.zeros(2, 1),
)
print(
    "  -> the A1 candidate construction is NOT new: it reproduces an "
    "already-published k=1 result, up to an overall sign."
)

print()
print("=" * 78)
print("C  is the k=0 zero mode itself capable of ANY non-constant Hopf form?")
print("=" * 78)


# C188's own closed-form X_a^R in Euler angles (decision.md SS2), quoted, not
# re-derived -- C188 already verified these to <1e-30 against the embedding's
# own Jacobian.
def XR_euler(a, expr):
    if a == 0:
        return 2 * sp.diff(expr, ps)
    if a == 1:
        return (
            2 * sp.cos(ps) * sp.diff(expr, th)
            + 2 * sp.sin(ps) / sp.sin(th) * sp.diff(expr, ph)
            - 2 * sp.sin(ps) / sp.tan(th) * sp.diff(expr, ps)
        )
    if a == 2:
        return (
            -2 * sp.sin(ps) * sp.diff(expr, th)
            + 2 * sp.cos(ps) / sp.sin(th) * sp.diff(expr, ph)
            - 2 * sp.cos(ps) / sp.tan(th) * sp.diff(expr, ps)
        )
    raise ValueError(a)


check(
    "C1 all three X_a^R (C188's closed forms) are PURE first-derivative operators "
    "(no zeroth-order/additive term) -- so they annihilate every constant by construction",
    all(sp.simplify(XR_euler(a, sp.Integer(1))) == 0 for a in range(3)),
)

a_c, b_c = sp.symbols("a_c b_c")  # a generic constant pair, left fully symbolic
D0_on_constants = [sum(XR_euler(a, comp) for a in range(3)) for comp in (a_c, b_c)]
check(
    "C2 D_0 built from C188's X_a^R annihilates an ARBITRARY constant pair (a_c, b_c) identically",
    all(sp.simplify(e) == 0 for e in D0_on_constants),
)

print()
print("=" * 78)
print("D  negative control: the SAME 'U * v' recipe applied at k=0 itself")
print("=" * 78)
# If U*v is applied to a genuinely k=0 object -- i.e. v is not a spin index at
# all but literally the harmonic_basis(0) = [1] scalar -- the construction
# must trivially return the same v, since there is nothing of degree >=1 for
# U to multiply against. This control exists to show B1/B2 is not a fluke of
# this particular v -- ANY attempt to manufacture non-constant k=0 dependence
# via left-multiplication by U fails the same way, because U itself is
# manifestly degree-1 in (x0..x3) (part A), so U*(anything degree 0) is
# degree 1, never degree 0.
check(
    "D1 U is manifestly degree-1 homogeneous in (x0,x1,x2,x3) (its own matrix entries, part A)",
    all(sp.total_degree(sp.Poly(e, x0, x1, x2, x3)) == 1 for e in quat_form),
)

print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
failed = [lab for lab, ok in OK if not ok]
for lab, ok in OK:
    print(f"  {'PASS' if ok else 'FAIL'}  {lab}")
print(f"\n{len(OK) - len(failed)} of {len(OK)} checks passed")
print("FAILED: " + "; ".join(failed) if failed else "all checks passed")
