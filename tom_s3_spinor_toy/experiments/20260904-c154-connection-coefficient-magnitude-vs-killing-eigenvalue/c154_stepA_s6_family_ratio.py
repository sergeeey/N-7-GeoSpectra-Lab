r"""
C154 STEP A -- is |c(nabla)| = (2/3)*mu(nabla) constant across S^6's WHOLE
2-dim admissible connection family, or only at the single point nabla=LC?

Reuses C147b's exact machinery unmodified: NOMIZU_A (=LC), NOMIZU_B (=LC.J,
independently verified in-family and R-independent of NOMIZU_A), and
c_exact_for(). Adds mu_exact_for(): ||D_Sigma(nabla) psi_+|| / ||psi_+||,
the full-norm amplitude of the untwisted Dirac operator's action on the
FIXED spinor psi_+ (psi_+ itself does not depend on the connection plugged
into D_Sigma), for an arbitrary connection -- new code, not previously
computed for anything but the LC point.

CORRECTED, same day, after a context-blind FL Step 8a skeptic pass (which
could not execute code) hand-derived that the FIRST version's scalarisation
-- the matrix element <psi_+,D psi_+> -- silently discards the psi_- half
of the isotropy-invariant target and gave a false FALSIFIED verdict at the
independent basis point (D_B psi_+ = i*sqrt(3)*psi_-, orthogonal to psi_+
and hence invisible to that inner product, not a genuine kernel of the
map). The full-norm version below is the structurally matched analogue of
|c(nabla)| (whose own target sector is 1-dim, so nothing is discarded
there) and is CONFIRMED on three independent points -- see the correction
note above mu_exact_for's definition.

Run:  python c154_stepA_s6_family_ratio.py
"""

import importlib.util
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
C147B_PATH = (
    HERE.parent
    / "20260904-c147-connection-coefficient-zero-locus"
    / "c147b_exact_and_complex_structure.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("=" * 78)
print("Importing C147b (exact S^6 family, c_exact_for, NOMIZU_A/B)")
print("=" * 78)
C147B = load_module("c147b", C147B_PATH)

R59 = C147B.R59
E_sym = C147B.E_sym
NOMIZU_A, NOMIZU_B = C147B.NOMIZU_A, C147B.NOMIZU_B
c_exact_for = C147B.c_exact_for

print(f"  c(NOMIZU_A) [reused, must reproduce -2*sqrt(3)/3]: {sp.nsimplify(sp.radsimp(C147B.c_A))}")
print(
    f"  c(NOMIZU_B) [reused, T_B = NOMIZU_A o J]          : {sp.nsimplify(sp.radsimp(C147B.c_B))}"
)
print(f"  in_family(NOMIZU_B)  : {C147B.in_family}")
print(f"  independent(A,B)     : {C147B.independent}")
assert C147B.in_family and C147B.independent, "C147b's own family regression drifted -- STOP"

print()
print("=" * 78)
print("STEP A1  mu(nabla) = <psi_+, D_Sigma(nabla) psi_+> -- NEW, exact")
print("=" * 78)

psi_plus, psi_minus = R59.psi_plus(), R59.psi_minus()
psi_norm2 = sp.simplify(R59.hip(psi_plus, psi_plus))
print(f"  <psi_+,psi_+> = {psi_norm2}  (psi_plus is NOT unit-normalized)")

# =============================================================================
# CORRECTION -- 2026-09-04, same day, by a context-blind FL Step 8a skeptic
# pass that could not execute code, and derived this entirely by hand from
# the round's own cited definitions. The FIRST version of this function used
# a single Rayleigh-quotient-style matrix element <psi_+,D psi_+>/<psi_+,psi_+>
# -- an ARBITRARY scalarisation choice among several equally LC-anchored
# options (verified: three different natural choices all give sqrt(3) AT the
# LC point, so the anchor does not select between them). The skeptic showed:
#   (a) for nabla != nabla_LC, psi_+ is NOT an eigenvector of D_Sigma(nabla)
#       at all -- the Killing equation holds ONLY at LC -- so "the eigenvalue"
#       has no single canonical generalisation off that point.
#   (b) the chosen scalarisation DISCARDS exactly the psi_- component:
#       D_B psi_+ = i*sqrt(3)*psi_- (hand-derived, independently confirmed
#       below), which is ORTHOGONAL to psi_+ and hence invisible to
#       <psi_+, D psi_+>. That is not a genuine kernel of the map -- it is a
#       projection discarding the entire T^2-invariant target sector's other
#       half. round59's own calibration already establishes psi_+, psi_- span
#       exactly the isotropy-invariant subspace of Sigma.
#   (c) the STRUCTURALLY matched analogue of c(nabla) -- whose own target
#       sector (u_hat/w_hat) is 1-dimensional, so |c| IS the full norm of the
#       image, nothing discarded -- is the FULL NORM of D_Sigma(nabla) psi_+
#       on the 2-dim invariant target span(psi_+,psi_-), not one component.
# Fixed accordingly. The original (wrong) function and its FALSIFIED verdict
# are recorded in this file's own git history / null_results, not hidden.
# =============================================================================


def mu_exact_for(nomizu_dict):
    """||D_Sigma(nabla) psi_+|| / ||psi_+|| -- the FULL amplitude on the
    2-dim isotropy-invariant target span(psi_+,psi_-), the structural
    analogue of |c(nabla)| (whose own target sector is already 1-dim, so no
    analogous discarding is possible there)."""
    D = sp.zeros(8, 1)
    for i in range(1, 7):
        nab_i = R59.spin_lift(nomizu_dict[i], E_sym)
        D += E_sym[i] * (nab_i * psi_plus)
    n2 = sp.simplify(R59.hip(D, D))
    return sp.simplify(sp.sqrt(n2) / sp.sqrt(psi_norm2))


mu_A = mu_exact_for(NOMIZU_A)
mu_B = mu_exact_for(NOMIZU_B)
print(
    f"  mu(NOMIZU_A) [must reproduce sqrt(3), the round59 Killing eigenvalue's magnitude]: {sp.nsimplify(mu_A)}"
)
print(
    f"  mu(NOMIZU_B)                                                                     : {sp.nsimplify(mu_B)}"
)

regression_ok = sp.simplify(mu_A - sp.sqrt(3)) == 0
print(f"  regression vs round59's own certified |Killing eigenvalue| sqrt(3): {regression_ok}")
assert regression_ok, "mu_exact_for does not reproduce the certified LC magnitude -- STOP"

print()
print("=" * 78)
print("STEP A2  THE DECISIVE RATIO, on BOTH independent basis directions")
print("=" * 78)

ratio_A = sp.simplify(sp.Abs(C147B.c_A) / mu_A)
ratio_B = sp.simplify(sp.Abs(C147B.c_B) / mu_B)
print(f"  |c(NOMIZU_A)| / mu(NOMIZU_A) = {ratio_A}   (known point, must be 2/3)")
print(
    f"  |c(NOMIZU_B)| / mu(NOMIZU_B) = {ratio_B}   (INDEPENDENT direction -- NOT known in advance)"
)

known_ok = sp.simplify(ratio_A - sp.Rational(2, 3)) == 0
new_ok = sp.simplify(ratio_B - sp.Rational(2, 3)) == 0
print(f"  ratio_A == 2/3 exactly : {known_ok}")
print(f"  ratio_B == 2/3 exactly : {new_ok}")

# =============================================================================
# STEP A3 -- a THIRD, independent point. mu is now a NORM (homogeneous
# degree 1, NOT additive/linear -- ||D(A+B)psi+|| != ||D_A psi+||+||D_B
# psi+|| in general, by the triangle inequality). So agreement at A+B is a
# genuine, non-tautological confirmation, not an algebraic consequence of
# the first two points the way it would have been under a linear functional.
# =============================================================================
print()
print("=" * 78)
print("STEP A3  a THIRD, independent point (A+B) -- NOT implied by A and B")
print("=" * 78)


def add_nomizu(d1, d2):
    return {i: d1[i] + d2[i] for i in range(1, 7)}


NOMIZU_SUM = add_nomizu(NOMIZU_A, NOMIZU_B)
mu_sum = mu_exact_for(NOMIZU_SUM)
c_sum = C147B.c_exact_for(NOMIZU_SUM)
ratio_sum = sp.simplify(sp.Abs(c_sum) / mu_sum)
print(f"  mu(A+B)         = {sp.nsimplify(mu_sum)}")
print(f"  |c(A+B)|        = {sp.nsimplify(sp.radsimp(sp.Abs(c_sum)))}")
print(f"  ratio at A+B    = {ratio_sum}")
sum_ok = sp.simplify(ratio_sum - sp.Rational(2, 3)) == 0
print(f"  == 2/3 exactly  : {sum_ok}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if known_ok and new_ok and sum_ok:
    print("  CONFIRMED, on THREE points spanning more than the 2-dim family (A, B,")
    print("  and the independent combination A+B, which homogeneity of degree 1")
    print("  alone does NOT force to match). |c(nabla)| = (2/3)*mu(nabla) across")
    print("  S^6's whole admissible connection family, where mu(nabla) is the FULL")
    print("  norm ||D_Sigma(nabla) psi_+|| -- the structural analogue of |c|, since")
    print("  c's own 1-dim target sector already captures its whole image, and")
    print("  mu must do the same on span(psi_+,psi_-) rather than project onto")
    print("  psi_+ alone (a corrected, skeptic-caught scalarisation -- see the")
    print("  correction note on mu_exact_for above; the FIRST version of this file")
    print("  projected onto psi_+ only, found FALSIFIED, and was wrong).")
else:
    print("  NOT confirmed on all three points -- report exactly which failed.")
    print(f"    ratio_A==2/3: {known_ok}   ratio_B==2/3: {new_ok}   ratio_sum==2/3: {sum_ok}")
