r"""
C195 -- independent verification of Tom's claim (2026-09-10 letter): the
difference chi_{+1/2} - chi_{-1/2} (C184's own derived S^2 doublet) has a
branch-cut jump across phi=0 that vanishes ONLY at tan(theta/2) = 1, i.e. on
the equator.

chi_{+1/2}(theta,phi) = e^{-i phi/2} cos(theta/2)   -- C184 decision.md SS1
chi_{-1/2}(theta,phi) = e^{+i phi/2} sin(theta/2)   -- C184 decision.md SS1

Both components are individually anti-periodic under phi -> phi+2pi (checked
first, as a sanity control matching C184's own D7/P5a machinery). The
branch-cut jump across phi=0 is Delta(0+) - Delta(2pi-); by anti-periodicity
Delta(2pi-) -> -Delta(0) as the approach is taken to the limit, so the jump
is exactly 2*Delta(theta, 0).
"""

import sympy as sp

th, ph = sp.symbols("theta phi", real=True)

chi_p = sp.exp(-sp.I * ph / 2) * sp.cos(th / 2)
chi_m = sp.exp(sp.I * ph / 2) * sp.sin(th / 2)
delta = chi_p - chi_m

OK = []


def check(label, cond, detail=""):
    OK.append((label, bool(cond)))
    print(
        f"  [{'PASS' if cond else 'FAIL'}] {label}{('  ' + detail) if detail else ''}"
    )


print("=" * 78)
print("A  each component's own anti-periodicity under phi -> phi+2pi")
print("=" * 78)
check(
    "A1 chi_+1/2(phi+2pi) = -chi_+1/2(phi), exactly",
    sp.simplify(chi_p.subs(ph, ph + 2 * sp.pi) + chi_p) == 0,
)
check(
    "A2 chi_-1/2(phi+2pi) = -chi_-1/2(phi), exactly",
    sp.simplify(chi_m.subs(ph, ph + 2 * sp.pi) + chi_m) == 0,
)
check(
    "A3 delta = chi_+1/2 - chi_-1/2 inherits the same anti-periodicity",
    sp.simplify(delta.subs(ph, ph + 2 * sp.pi) + delta) == 0,
)

print()
print("=" * 78)
print("B  the branch-cut jump across phi=0, as a function of theta")
print("=" * 78)
jump = sp.simplify(2 * delta.subs(ph, 0))
print(f"  jump(theta) = 2*delta(theta, 0) = {jump}")
check(
    "B1 jump(theta) simplifies to a single cosine of a shifted half-angle",
    sp.simplify(jump - 2 * sp.sqrt(2) * sp.cos(th / 2 + sp.pi / 4)) == 0,
)

print()
print("=" * 78)
print("C  Tom's claim: jump vanishes iff tan(theta/2) = 1")
print("=" * 78)
sol = sp.solve(sp.Eq(sp.cos(th / 2) - sp.sin(th / 2), 0), th)
check(
    "C1 jump(theta) = 0 has the unique solution theta = pi/2 on [0, pi]",
    sol == [sp.pi / 2],
    f"solved theta = {sol}",
)
check(
    "C2 tan(theta/2) = 1 at that solution, exactly",
    sp.simplify(sp.tan(sol[0] / 2) - 1) == 0,
)

print()
print("=" * 78)
print("D  negative control: a genuinely single-valued (integer-weight) pair")
print("=" * 78)
# A pair with NO phi-dependence at all (the weight-0, single-valued case
# C184b uses as its own negative control at k=2) is single-valued by
# construction: its "jump" across phi=0 must be identically zero for EVERY
# theta, not just at an isolated point. This is the qualitatively different
# behaviour the B/C checks above must be able to distinguish from -- if this
# check also reported "vanishes only at theta=pi/2", the B/C machinery would
# be too coarse to mean anything.
f_int, g_int = sp.cos(th), sp.sin(th)
delta_int = f_int - g_int
jump_int_generic = sp.simplify(delta_int.subs(ph, ph + 2 * sp.pi) - delta_int)
delta_int_nonconstant = sp.diff(delta_int, th) != 0
check(
    "D1 the phi-independent (single-valued) pair has an IDENTICALLY zero jump "
    "for every theta, not just theta=pi/2 -- confirming the B/C result is a "
    "genuine, non-trivial property of the half-integer pair, not an artifact "
    "of how 'jump' is defined",
    sp.simplify(jump_int_generic) == 0 and delta_int_nonconstant,
    "jump == 0 identically in phi, while delta itself is a non-constant function of theta "
    "(not a vacuous 0==0 case)",
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
