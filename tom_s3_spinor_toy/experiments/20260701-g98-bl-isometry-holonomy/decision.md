# Decision — G98: B-L isotropy vs coset

**Date:** 2026-07-01
**Verdict:** WEAK / PARTIAL — reconciliation hypothesis NOT confirmed as scoped
**Go/no-go:** NO-GO on "G97 resolved" claim; G97 status stays OPEN

## Result

10/11 checks PASS. Two findings, both honest, neither cleanly confirms the
claim.md hypothesis:

1. **T5 FAILED (unexpected, my design error, not a physics bug):** BmL does
   NOT commute with all 15 generators of so(6)=su(4) — only with the
   su(3)⊕u(1) subalgebra (9 of 15), consistent with G15's original T4 (which
   only tested the 8 su(3) generators). The claim.md estimand mis-stated the
   expectation: BmL should only commute with su(3)⊕u(1), not full su(4) —
   the remaining 6 su(4)/(su(3)⊕u(1)) generators mix quark/lepton sectors,
   which BmL is BUILT to distinguish, so non-commutation there is expected
   and correct, not a flaw in BmL.

2. **Coset test (T6) is skeptic-confirmed uninformative as a binary
   PASS/FAIL, but shows a real quantitative pattern:** BmL fails to commute
   with all 6/6 coset generators K_a. Each individual so(6) Cartan control
   (J_01, J_23, J_45) fails with only 2/6 each. BmL is a sum of exactly
   these 3 directions, and the union of their 2/6 "footprints" plausibly
   covers all 6 K_a — meaning BmL's 6/6 result is a consequence of it being
   a combined direction, not evidence that B-L specifically has a deeper
   relationship to the coset than any other so(6) Cartan generator.

## Skeptic verdict vindicated

The pre-implementation red-team (agent a9436be) flagged exactly this risk:
"the kill criterion cannot distinguish B-L is a genuine holonomy charge from
B-L happens to be diagonal, generic diagonal so(6) generators behave the
same." The computed control confirms this concern with real numbers, not
just a theoretical worry — CONTROL_cartan_gens_also_fail_coset = PASS
(all 3 controls have >=1 nonzero commutator with the coset).

## What this does NOT mean

1. Does NOT resolve G97 — the U(1)_Y/(B-L) gap in the pure-isometry route
   remains OPEN, still needs Tom Part 4/5 (or a route we have not found).
2. Does NOT invalidate G15's B-L construction — G15's own scope (commutes
   with su(3), reproduces the SM hypercharge table) is unaffected; only the
   broader "commutes with full so(6)" and "distinguishable from generic
   isotropy at the coset" claims (new in this experiment) are unconfirmed.
3. Does NOT mean the isotropy-vs-isometry distinction is wrong in general —
   it means THIS specific test (raw commutator count) is too coarse to
   demonstrate it for THIS specific B-L operator.

## Lesson

Pre-implementation skeptic review caught a real design flaw before wasted
effort on a clean-looking but uninformative "PASS." The honest outcome here
is WEAK, not a forced positive — consistent with this project's discipline
(see null_results/INDEX.md pattern). Filed as a documented WEAK result, not
a null_results REJECT, because parts of the design (T1-T4, T7) are sound
and reusable; only the T5/T6 informativeness needs a different approach
(e.g., comparing BmL against the FULL so(6) Cartan simultaneously, or using
a representation-theoretic argument instead of raw commutator counting) if
revisited.

## Next step if revisited

Retry with a proper Casimir/weight-based argument (does B-L's WEIGHT under
the coset's induced so(6)-representation differ from a generic Cartan
direction's weight spectrum?) rather than a binary "commutes or not" test.
Not scheduled now — lower priority than G91-97's other open items.
