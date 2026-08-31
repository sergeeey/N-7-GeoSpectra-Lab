# C117 decision -- j2=5/2 gap filled; verdict correct but originally
mislabeled, corrected same-session by FL Step 8a skeptic

**Verdict:** `NO_SIZE_35_SUBSET_STAYS_REAL_AT_N6__RULES_VERIFIED_SUPPORT_IS_N4_N5_ONLY_BOUNDED_BOTH_SIDES`
(renamed from the script's raw `FULL_COLLAPSE` per the skeptic's own
Check 6 finding -- see "Skeptic response" below for why)
**Status:** RESOLVED for the pre-registered question; REFRAMED for what
it actually establishes about the broader "rule"

## Summary

User asked directly to resolve the j2=5/2 gap the C116-addendum skeptic
pass had named. Built and ran the cell (k_source=5, target_level=10,
n=6, 36 remove-one tests, 314x314 combined operator). Result: **every
one of the 36 remove-one tests breaks reality** (min break magnitude
4.6e-5, ten orders of magnitude above the 1e-9 threshold and the
~1e-15 scale of every confirmed-real case in this series) -- including
all 8 cases the asymmetric rule ("stays real iff |a|=j2 AND |b|<j2")
predicted would stay real. Per claim.md's own pre-registered kill
criteria, this is an unambiguous `FULL_COLLAPSE` (RULE_HOLDS and
PARTIAL are both dead).

Ran FL Step 8a skeptic (context-blind) on this result, given the
question was specifically escalated after the C116-addendum skeptic
pass found a real gap. Verdict: **WEAKENED**. The arithmetic is
airtight and the verdict is correct; the *label and interpretation*
around it overstated what was established. Full response matrix below.

## Results

- P0 (full sum stays real): True, `max_im=6.49e-15`.
- P1 (component norms identical): True (all 36 equal `11/6`, forced
  exactly by CG orthogonality -- confirmed the same identity holds at
  j2=1 (`5/3`) and j2=3/2 (`7/4`) in prior rounds' data; this is a
  positive control on the builder code, not itself evidence about
  which components matter).
- Remove-one (size-35) tests: 0/36 stay real. Smallest break magnitude
  4.6e-5, comfortably separated from the ~1e-15 real-case scale by
  ~10 decades -- not a threshold artifact.
- `|a|=j2=5/2` sector (12 entries, of which the asymmetric rule
  predicted 8 stay real): 0/12 stay real. All 8 rule-predicted cases
  broke; the 4 corner (`|b|=5/2`) cases the rule also predicted would
  break, did break.
- Rule match overall: 28/36 -- **worse than the trivial "always
  predict breaks" baseline, which would score 36/36 at this specific
  cell.** Quoting 28/36 as support for the rule, without this
  baseline, would be misleading; the rule adds negative value here.

## Skeptic response (2026-08-31, FL Step 8a, context-blind pass on
this round's result)

Verdict: **WEAKENED**. Full response per the project's own Response
Matrix (`falsification-ladder.md` Step 8a):

| Concern | Response |
|---|---|
| The construction has an exact `a<->-a, b<->-b` symmetry (CG reflection identity), partitioning the 36 remove-one tests into 9 independent orbits of size 4, not 36 independent data points -- the evidential resolution of "0/36" is really "0 of 9 orbits" | **Accepted, documented above and in the verdict rename.** This does not change the verdict (a deterministic rule is falsified by a single orbit), but it changes how strong the evidence should be presented as. |
| "FULL_COLLAPSE" as worded overstates the finding -- in this SAME run, all 36 size-1 ("single alone") subsets stay real and the full size-36 sum stays real; only size-35 (remove-one) subsets break. The window has not "fully collapsed"; reality-preservation is non-monotone in subset size, consistent with `results_c114.json`'s own structured-intermediate data at n=3 | **Accepted, fixed.** Verdict renamed above to scope it correctly to size-35 subsets specifically. |
| `claim.md`'s pre-registered kill criteria are defined over the 8 rule-predicted cases; the script's `sector_real` counts all 12 sector entries -- these happened to agree this round (all 12 broke, including the 8 predicted) but are NOT the same test, and could diverge at a future integer cell (e.g. j2=4, n=9) where fixed points under the symmetry exist | **Accepted, flagged for future rounds.** Not fixed retroactively (the divergence did not fire this round, and editing an already-run script to relabel what it measured would misrepresent what was actually tested) -- recorded as a named hazard for any j2=4 attempt. |
| The asymmetric rule itself ALREADY fails at j2=1 (n=3): `results_c114.json` shows 6/9 real removals there against the rule's own prediction of 2/9, with all 3 mismatches at `a=0` -- this was known from C114/C115 but not stated in this round's claim.md, and its absence let the framing imply the rule was solid on both approaches to the boundary | **Accepted, added.** The asymmetric rule's own VERIFIED support is `n in {4,5}` (j2 in {3/2,2}) only, bounded on BOTH sides by cells where it fails -- j2=1 (partial failure, a different symmetric rule fits better there per C115) and now j2=5/2, j2=3 (total failure). A rule holding cleanly on exactly 2 adjacent cells and failing on 3 others (one below, two above) is better described as a narrow coincidence than as a law with a "collapsing domain." |
| 28/36 "rule match" has no baseline attached -- the trivial "always predict breaks" classifier scores 36/36 at this cell, strictly better | **Accepted, added above.** Quoting rule-match fractions without the trivial baseline is misleading going forward; add it whenever this fraction is quoted for any cell where the base rate is already known to be extreme (as it now is at both j2=1's edge case and j2=3, j2=5/2's total-break cells). |
| An untested, cheaper alternative hypothesis exists: total operator dimension grows with n (68/130/242/314/338 across the 5 tested cells), a denser spectrum makes a fixed-norm perturbation (removing one component) more likely to collide two real eigenvalues into a conjugate pair -- this would produce the SAME qualitative pattern (small |Im|, monotone-decreasing real fraction, eventual total collapse) with NO representation-theoretic "rule" at all | **Accepted as a genuine open alternative, not adjudicated this round.** Recorded as a new pearl below with a concrete, cheap next check (the eigenvalues are not currently persisted in `results_*.json` -- computing and comparing min spectral gap vs. perturbation norm across n=3..7 requires a small additional script, not a re-run of the existing heavy construction). This is flagged explicitly as competing with, not confirming, the "asymmetric rule" framing used throughout C112-C117. |
| The skeptic could not execute code (no Bash tool) and re-derived every number by hand from the committed JSON -- "the JSON matches a fresh run of `run_cell`" was left as `[UNKNOWN]` from the skeptic's side | **Closed from this side.** The script was run directly by this session (not by the skeptic) and its printed console output was captured before `results_c117.json` was written; both agree with each other and with the skeptic's independent hand-recount. |
| P0/P1, the 36-entry recount, threshold robustness, the type-serialization fix | **CONFIRMED-REAL by the skeptic's own independent recomputation** -- unchanged, no fix needed. |

## What this DOES establish

- No single-component removal (size-35 subset) preserves spectral
  reality at the matched-diagonal cell j1=j2=5/2. Robust to any
  reasonable threshold choice; not a numerical artifact (values
  cluster in exact symmetry-related quadruplets agreeing to 9-11
  significant digits, not scattered noise).
- The asymmetric rule tested since C114 has verified support on
  exactly `n in {4,5}` (j2 in {3/2,2}) and fails, in different ways,
  on every other tested cell (`n in {3,6,7}`, i.e. j2 in {1,5/2,3}).
- The trivial "always breaks" baseline outperforms the rule at both
  j2=5/2 and j2=3.

## What this does NOT establish (corrected scope, per skeptic)

- Does NOT establish that "the reality-preserving window has fully
  collapsed" as a general statement -- single-component-alone subsets
  and the full sum both stay real at this same cell; only size-35
  removal breaks.
- Does NOT establish that the asymmetric rule was ever a genuine
  mechanism rather than a 2-cell coincidence -- its failure at j2=1
  (previously known but not connected to this question until this
  round) already bounds its domain on the low side; this round bounds
  it on the high side too.
- Does NOT rule out the untested eigenvalue-density alternative
  explanation named above -- genuinely open, not evidence either way
  from this round alone.
- Does NOT change `N_gen=3`'s CONDITIONAL status; stays entirely
  internal to S3, touches neither S6 nor triality.
- Does NOT solicit Tom Lawrence's Part 5.

## Verification

- `ruff check experiments/20260831-c117-j2-5-2-gap-test/` -- clean.
- Full pytest suite run before commit.
- Independently re-verified by FL Step 8a skeptic (context-blind,
  no Bash access -- hand-recomputed all 36 entries from
  `results_c117.json` directly): P0, P1, the 36-entry tally, threshold
  robustness, and the type-serialization fix all CONFIRMED-REAL.
- Reused C114's own `run_cell` unmodified via direct import, same
  method as C115/C116 (4th reuse).
