# G102 — Does c_S3 (G94) reduce to a prediction for the string coupling g_s?

**Question type:** [ ] descriptive  [x] predictive  [ ] causal
(predictive in the sense of: does fixing c_S3 from brane-tension theory
predict/constrain g_s, rather than just describing existing G94 output)

**Claim:**
Substituting the standard Euclidean D2-brane tension formula
T_2 = 1/((2*pi)^2 * alpha'^(3/2) * g_s) into G94's instanton action ansatz,
using this repo's own rho3-to-string-length convention (GA2), gives
c_S3 = f(g_s) for some specific f -- my preliminary hand-derivation
(NOT yet verified) suggests f(g_s) = 1/(2*g_s), which would translate
G94's empirically-valid window c_S3 in (0.248, 0.372) into a predicted
g_s in (1.34, 2.02) -- i.e. a STRONGLY COUPLED regime (g_s > 1), which
would need explicit caveat/discussion, not silent acceptance.

**Kill target (MANDATORY — Strong Inference):**
No existing ACH case covers this (new question, S3-side analog of the
lambda_np/parameter_registry OPEN status). Kill target is whether the
GA2-vs-standard-formula convention mismatch (identified during source
trace) can be honestly reconciled.

- FAIL (convention mismatch cannot be cleanly reconciled -- e.g. GA2's
  missing 2*pi factors mean rho3 in G94 is NOT literally "radius in
  string-length units" in the sense the tension formula requires, or the
  reconciliation introduces an arbitrary extra free parameter to absorb
  the discrepancy) -> document as NEEDS-CONVENTION-RECONCILIATION, do not
  claim a g_s prediction. This would be analogous to G98/G101's category
  mismatches -- a real methodological block, not a computation failure.
- FAIL (g_s prediction comes out but requires g_s >> 1 or g_s < 0 or other
  physically absurd values with no honest caveat available) -> report as
  WEAK: brane-instanton picture gives a formally derivable c_S3-g_s
  relation but the implied coupling regime is in tension with perturbative
  string theory; flag as an open physics problem, not swept under the rug.
- PASS (a clean, convention-consistent relation c_S3=f(g_s) is derived,
  and the implied g_s range is at least DISCUSSABLE, even if strongly
  coupled) -> new result: c_S3 is not a free parameter, it is FIXED (up to
  g_s) by string-theoretic brane tension -- G94's scan becomes a genuine
  prediction for g_s, not a fitting exercise.

**Checks planned:**
- T1: source trace -- confirm Dp-brane tension formula via >=2 independent
  citations (done: WebSearch cross-confirmed, [WEAK-MEDIUM]; direct PDF
  fetch of arXiv:2310.20559 FAILED to parse cleanly, not used as citation)
- T2: explicitly reconcile GA2's "no 2*pi factors" convention against the
  standard tension formula's explicit (2*pi)^p -- track EVERY factor of
  2*pi through the derivation symbolically (sympy), do not hand-wave
- T3: derive c_S3 = f(g_s) symbolically, cross-check against my
  preliminary hand-derivation f(g_s)=1/(2*g_s) (do NOT assume it is
  correct -- rederive independently in code)
- T4 (control, per G98/G99/G101 lesson): redo the SAME derivation using
  the STANDARD KK formula (WITH 2*pi factors, ignoring GA2's simplification)
  and compare the resulting f(g_s) -- if the two conventions give
  DIFFERENT answers (they should, given GA2's explicit deviation), this
  confirms which convention is actually being tested and prevents
  silently using the wrong one
- T5: map the empirical c_S3 window (0.248, 0.372) to a g_s window under
  the repo's OWN convention (not the standard one) and report both,
  labeled clearly

**Verdict:** STRUCTURAL_RELATION_CONFIRMED — c_S3 = 1/(2*g_s) [VERIFIED-sympy
5/5 + pytest 6/6]. G94's empirical window (0.248, 0.372) implies g_s in
(1.344, 2.016) — strongly coupled. Exact prefactor (1/2) is [WEAK-MEDIUM];
proportionality c_S3~1/g_s is more robust. See decision.md.

**Evidence:** [VERIFIED-sympy 5/5] + [VERIFIED-pytest 6/6] + [WEAK-MEDIUM:
WebSearch cross-confirmed Dp-brane tension formula (2 queries), primary
source PDF fetch (arXiv:2310.20559) failed/discarded]

**Caveat / What this does NOT mean:**
- Does NOT measure g_s independently -- only shows what G94's window implies
- Does NOT resolve lambda_np (S6-side) -- separate parameter, separate gate
- Does NOT change sm_derivation_claimed=False or safe_for_runtime=False

**Fence (do not change):**
- lambda_v_operator = FREE_COUPLING_PARAMETER (unaffected -- different parameter)
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

**Status:** CLOSED PASS (STRUCTURAL_RELATION_CONFIRMED) — see decision.md.
Exact numeric prefactor flagged [WEAK-MEDIUM], follow-up literature check
recommended before treating g_s=[1.344,2.016] as a hard number.
