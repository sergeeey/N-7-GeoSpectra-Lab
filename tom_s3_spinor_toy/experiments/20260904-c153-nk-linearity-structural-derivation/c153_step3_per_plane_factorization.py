r"""
C153 STEP 3 -- confirm the per-plane factorization discovered (not
pre-registered) while reading Step 2's per-direction sign output.

WHAT STEP 2 SHOWED, read closely rather than summarised
  For the 6 eps that fail the GLOBAL c(J.grad)=+-i c(grad) test, printing the
  sign PER FAMILY DIRECTION (instead of only the pass/fail verdict) revealed
  the six directions split into three CONSECUTIVE PAIRS, each pair carrying
  a single consistent sign, and that sign matched i^eps_k for root plane k
  in every one of the 6 non-uniform cases:

      eps=(1,1,-1):  signs = [+i,+i, +i,+i, -i,-i]   ==  i^(+1,+1,-1)
      eps=(1,-1,1) :  signs = [+i,+i, -i,-i, +i,+i]   ==  i^(+1,-1,+1)
      ... (all six match exactly)

  This is a STRONGER, unregistered claim: not merely "2 of 8 eps give a
  uniform global sign", but "EVERY eps gives an EXACT per-plane sign i^eps_k,
  independent of the other two planes' choices, and the 2 uniform cases are
  simply where all three plane-signs happen to agree."

THIS FILE tests that stronger claim DIRECTLY, not by re-reading Step 2's
6-direction output, but by an independent falsification attempt: hold TWO
plane signs FIXED and vary the THIRD across both signs, on a family vector
supported ONLY on ONE plane's own pair of basis directions. If the claim is
right, the measured sign on that plane must depend ONLY on that plane's own
eps_k and be COMPLETELY INSENSITIVE to the other two eps_j -- a much sharper,
more falsifiable statement than reading off a table.

Reuses Step 2's exact construction unmodified (same module, imported).

Run:  python c153_step3_per_plane_factorization.py
"""

import importlib.util
from itertools import product
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "c153_step2", HERE / "c153_step2_exact_rational_verification.py"
)
S2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S2)

family_sym, c_of_exact, acs_from_eps = S2.family_sym, S2.c_of_exact, S2.acs_from_eps

print()
print("=" * 78)
print("C153 STEP 3 -- per-plane factorization, tested directly (not read off)")
print("=" * 78)


def sign_for(k: int, eps_k: int, other_eps) -> str | None:
    """Sign found for family basis direction k, with plane k's own sign
    fixed to eps_k and the OTHER two planes' signs set by other_eps
    (a dict {plane: sign} for the remaining planes). Returns '+i', '-i',
    or None if neither matches exactly."""
    full_eps = [0, 0, 0]
    full_eps[k] = eps_k
    for j, s in other_eps.items():
        full_eps[j] = s
    Jm = acs_from_eps(tuple(full_eps))
    # BUG, caught before reporting: Step 2's printout grouped family columns
    # in CONSECUTIVE PAIRS (0,1) (2,3) (4,5) sharing a sign -- the first
    # version of this test used family column `k` directly against a.c.s.
    # position `k`, i.e. tested columns 0,1,2 against positions 0,1,2, which
    # is NOT the correspondence Step 2's own printout suggested. Use column
    # 2*k (one representative of pair k) instead.
    v = family_sym[:, 2 * k]
    Jv = Jm.T * sp.Matrix(6, 15, lambda r, c: v[r * 15 + c])
    Jv_flat = sp.zeros(90, 1)
    for r in range(6):
        for c in range(15):
            Jv_flat[r * 15 + c] = Jv[r, c]
    cv = c_of_exact(v)
    cJv = c_of_exact(Jv_flat)
    if all((cJv - sp.I * cv)[r, c] == 0 for r in range(3) for c in range(3)):
        return "+i"
    if all((cJv + sp.I * cv)[r, c] == 0 for r in range(3) for c in range(3)):
        return "-i"
    return None


falsified = False
for plane in range(3):
    others = [j for j in range(3) if j != plane]
    print(f"\n  plane {plane} (family direction index {plane}), varying the OTHER two eps:")
    seen_for_plus, seen_for_minus = set(), set()
    for eps_k in (1, -1):
        for oa, ob in product((1, -1), repeat=2):
            other = {others[0]: oa, others[1]: ob}
            s = sign_for(plane, eps_k, other)
            (seen_for_plus if eps_k == 1 else seen_for_minus).add(s)
            print(f"    eps_{plane}={eps_k:+d}, others={other} -> sign = {s}")
    ok_plus = seen_for_plus == {"+i"}
    ok_minus = seen_for_minus == {"-i"}
    print(f"    plane {plane}: eps_{plane}=+1 always gives +i, independent of others: {ok_plus}")
    print(f"    plane {plane}: eps_{plane}=-1 always gives -i, independent of others: {ok_minus}")
    if not (ok_plus and ok_minus):
        falsified = True

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if not falsified:
    print("  Per a same-day skeptic pass: this is genuinely 3 independent facts")
    print("  (one per plane, eps_k=+1), not 24. family_sym's columns are exactly")
    print("  block-local per plane, and acs_from_eps is exactly block-diagonal by")
    print("  construction -- so the other two planes' signs CANNOT affect this")
    print("  computation (forced by structure, not measured), and eps_k=-1 follows")
    print("  from eps_k=+1 by linearity + acs_from_eps(-e)=-acs_from_eps(e). The")
    print("  per-plane law c((J_eps)|_plane k . v_k) = i^{eps_k} c(v_k) is real and")
    print("  confirmed, at this correct strength -- see claim.md / decision.md.")
else:
    print("  FALSIFIED -- the per-plane sign depends on the OTHER planes' choice")
    print("  too. The pattern read off Step 2's table does not generalise; do")
    print("  NOT report a per-plane factorization law.")

# =============================================================================
# CORRECTION -- 2026-09-04, same day, by the same skeptic pass as Step 1.
#
# The docstring above claims "24 direct tests" and frames varying the OTHER
# two eps as an independent falsification attempt. It is not independent in
# the way claimed, and it is not 24 tests. Two things were verified directly
# after the skeptic flagged them (not merely asserted):
#
#   1. family_sym's 6 columns are EXACTLY block-local: column 2k and 2k+1
#      are nonzero ONLY in direction-rows {2k,2k+1} (verified by inspecting
#      every column's nonzero row support -- see the verification commands
#      in decision.md). So v = family_sym[:, 2*k] is supported ONLY on
#      plane k.
#   2. acs_from_eps(eps) is EXACTLY block-diagonal BY CONSTRUCTION -- it
#      only ever writes entries at positions (2j,2j+1)/(2j+1,2j) for each
#      plane j; there are no off-block entries for ANY eps.
#
# Given (1) and (2), Jm.T @ v for a plane-k-local v depends ONLY on Jm's
# plane-k block, which depends ONLY on eps_k. The other two planes' signs
# CANNOT affect the result -- not "were found not to affect it", but
# "cannot algebraically affect it, by the block structure alone". So the
# 4 "other-sign combinations" tested per (plane, own-sign) are the SAME
# computation repeated 4 times, not 4 independent checks: 3 planes x 2
# own-signs x (4 IDENTICAL reruns) = 6 genuinely distinct computations, not
# 24. And eps_k=-1 is not even independent of eps_k=+1: acs_from_eps(-eps)
# = -acs_from_eps(eps) exactly (verified), and c_of_exact is linear, so the
# eps_k=-1 sign follows algebraically from the eps_k=+1 sign. That leaves
# THREE genuinely independent facts -- one per plane -- not six and
# certainly not twenty-four.
#
# What survives, honestly: the per-plane law itself (i^{eps_k}, one sign per
# plane, no cross-plane coupling) IS real and IS confirmed -- but by 3 exact
# computations plus 2 structural (not computational) arguments, not by "24
# direct tests" as originally claimed. See claim.md's revised item 1 and
# decision.md's Response Matrix. This file's numeric output is unaffected
# and correct; only the evidentiary framing in the docstring above was wrong.
# =============================================================================
