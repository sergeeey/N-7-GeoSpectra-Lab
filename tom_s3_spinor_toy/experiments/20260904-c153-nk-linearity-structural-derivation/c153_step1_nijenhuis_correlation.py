r"""
C153 STEP 1 -- does non-integrability (Nijenhuis != 0) predict WHICH 2 of the
8 invariant almost-complex structures on SU(3)/T^2 satisfy the twist-
connection C-linearity c(J.grad) = i c(grad)?

Reuses, UNMODIFIED:
  - C152 Step 8's is_c_linear / acs_from_eps (the ALIGNED-basis test)
  - C151 Stage 1a's Nijenhuis computation (the RAW-basis classification)

Both are imported as modules, not re-derived, so any drift in either source
shows up as an import/assert failure rather than silently producing a
different number.

Run:  python c153_step1_nijenhuis_correlation.py
"""

import importlib.util
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
S8_PATH = HERE.parent / "20260904-c152-term2-vanishing-mechanism" / "c152_step8_falsifiability.py"
S1A_PATH = HERE.parent / "20260904-c151-stage0-su3t2-scoping" / "c151_stage1a_pin_J.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


print("=" * 78)
print("Importing C152 Step 8 (aligned-basis C-linearity test)")
print("=" * 78)
S8 = load_module("c152_step8", S8_PATH)
print()
print("=" * 78)
print("Importing C151 Stage 1a (raw-basis Nijenhuis classification)")
print("=" * 78)
S1A = load_module("c151_stage1a", S1A_PATH)

EPS_NK = S1A.EPS_NK
print(f"\nStage 1a's own pinned J_NK (raw basis) = {EPS_NK}")

# ---------------------------------------------------------------------------
# 1. Re-derive, from S1A's own raw-basis classification, the set of
#    non-integrable (Nijenhuis != 0) raw eps tuples.
# ---------------------------------------------------------------------------
def raw_nijenhuis(eps):
    J = S1A.make_J(eps)
    return S1A.nijenhuis_norm(J)


raw_non_integrable = {eps for eps in product((1, -1), repeat=3) if raw_nijenhuis(eps) > 1e-10}
print(f"\nRAW non-integrable set (Nijenhuis != 0): {sorted(raw_non_integrable)}")
assert raw_non_integrable == {(1, -1, 1), (-1, 1, -1)}, (
    f"Stage 1a's own classification drifted: got {raw_non_integrable}"
)

# ---------------------------------------------------------------------------
# 2. Re-derive, from S8's own aligned-basis test, the set of C-linear
#    aligned eps tuples (rerun cleanly here, not copy-pasted from decision.md).
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("Re-running C152 Step 8's C-linearity test for all 8 aligned eps")
print("=" * 78)
aligned_c_linear = set()
for eps in product((1, -1), repeat=3):
    ok, dev = S8.is_c_linear(S8.acs_from_eps(eps))
    tag = "C-LINEAR" if ok else "not"
    print(f"  aligned eps={eps!s:>14}  {tag:<9}  max rel. deviation = {dev:.3e}")
    if ok:
        aligned_c_linear.add(eps)
print(f"\nALIGNED C-linear set: {sorted(aligned_c_linear)}")
assert aligned_c_linear == {(1, 1, 1), (-1, -1, -1)}, (
    f"C152 Step 8 regression FAILED: got {aligned_c_linear}"
)

# ---------------------------------------------------------------------------
# 3. THE TEST: relabel the raw non-integrable set by eps_NK and compare.
# ---------------------------------------------------------------------------
def relabel(eps, by):
    return tuple(e * b for e, b in zip(eps, by))


predicted_aligned = {relabel(eps, EPS_NK) for eps in raw_non_integrable}

print()
print("=" * 78)
print("THE PREREGISTERED TEST")
print("=" * 78)
print(f"  raw non-integrable set          : {sorted(raw_non_integrable)}")
print(f"  relabelled by eps_NK={EPS_NK}     : {sorted(predicted_aligned)}")
print(f"  aligned C-linear set (Step 8)    : {sorted(aligned_c_linear)}")
match = predicted_aligned == aligned_c_linear
print(f"\n  SETS IDENTICAL: {match}")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if match:
    print("  Sets match -- but per a same-day skeptic pass, THIS SPECIFIC TEST")
    print("  IS VACUOUS: relabelling any conjugate pair {b,-b} by b itself ALWAYS")
    print("  gives {(1,1,1),(-1,-1,-1)}, regardless of what b is. This match was")
    print("  therefore guaranteed by the relabelling arithmetic, not evidence about")
    print("  Nijenhuis. See c153_step2_exact_rational_verification.py's Step 2g for")
    print("  the non-tautological version (direct aligned-basis Nijenhuis, no")
    print("  relabelling), which DOES genuinely confirm this correlation.")
else:
    print("  FALSIFIED. The 2-of-8 selection is NOT predicted by the Nijenhuis")
    print("  tensor as stated. Some other property coincides with (1,1,1)/")
    print("  (-1,-1,-1) for a different reason -- do not claim NK-equivalence.")

# =============================================================================
# CORRECTION -- 2026-09-04, same day, by a context-blind FL Step 8a skeptic
# pass on C153. The "VERDICT: CONFIRMED" text printed above is WITHDRAWN.
#
# The relabelling test this file runs (relabel(raw_non_integrable, EPS_NK)
# == aligned_c_linear) is VACUOUS: for ANY conjugate pair {b,-b} relabelled
# by b itself, the result is ALWAYS {(1,1,1),(-1,-1,-1)}, regardless of what
# b actually is. Verified directly:
#
#   relabel({(1,-1,1),(-1,1,-1)}, by=(1,-1,1))   -> {(1,1,1),(-1,-1,-1)}
#   relabel({(1,1,1),(-1,-1,-1)}, by=(1,1,1))    -> {(1,1,1),(-1,-1,-1)}
#   relabel({(1,-1,-1),(-1,1,1)}, by=(1,-1,-1))  -> {(1,1,1),(-1,-1,-1)}
#
# (Every row gives the same answer; run any small check-script over
# product((1,-1),repeat=3) and confirm.) So this test could not have
# reported FALSIFIED for ANY actual Nijenhuis classification, as long as
# that classification produces a 2-element conjugate pair (which it always
# does, since J non-integrable implies -J non-integrable). It tests an
# identity of the relabelling arithmetic, not a fact about geometry.
#
# The SUBSTANTIVE correlation this file intended to check IS real, but had
# to be established differently: c153_step2_exact_rational_verification.py
# Step 2g computes the Nijenhuis tensor DIRECTLY in the aligned basis (the
# SAME M_BASIS Stage 2a and this project's Step 2 use), with NO relabelling
# step, and compares its non-integrable set against the independently
# computed C-linear set. That version CAN fail, and was run: it confirmed
# the same {(1,1,1),(-1,-1,-1)} match, non-tautologically.
#
# This file is kept, unedited above, per this project's discipline on
# self- and skeptic-caught errors -- the arithmetic it prints is all
# correct; only the INFERENCE drawn from it ("not a coincidence of the
# alignment choice") was wrong. See claim.md and decision.md.
# =============================================================================
