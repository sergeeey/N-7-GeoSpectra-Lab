# C110 decision -- the covariance hypothesis is cleanly refuted; two
follow-on refinements are also refuted; the true criterion remains open

**Verdict:** `COVARIANCE_HYPOTHESIS_REFUTED__NO_SINGLE_CRITERION_FOUND_THIS_ROUND`
**Status:** RESOLVED -- a genuine, informative null result on a specific,
well-posed hypothesis

---

## Summary

Tested C109's own pearl: does "covariance" (a coupling corresponding to
a genuine real quaternion coordinate function, vs. an arbitrary complex
mix) predict whether the k=1 coupled spectrum stays real?

**All 5 formal predictions confirmed -- the hypothesis is refuted, cleanly
and reproducibly:**

| # | Prediction | Outcome |
|---|---|---|
| P0 | Reproduce the 4 single-coordinate + `M_sum` baseline exactly | **CONFIRMED**. |
| P1 | `aw+bw` real; `aw+i*bw` (nonzero imag_part) ALSO real | **CONFIRMED** -- direct counter-example to naive covariance. |
| P2 | Every zero-imag_part case is real (no false negatives for that direction) | **CONFIRMED**. |
| P3 | `aw+i*bw`, `i*aw` alone (nonzero imag_part) are STILL real (false positives for the hypothesis) | **CONFIRMED**. |
| P4 | `M_sum`, `(1,2,3,4)`, `(1,-1,1,-1)`, `(2,1,1,2)` (nonzero imag_part) genuinely break reality | **CONFIRMED**. |

## What this genuinely establishes

1. **The simple covariance hypothesis is false.** "Does the coupling
   correspond to a genuine real quaternion coordinate function (zero
   symbolic imaginary part in the `aw,ax,bw,bx` decomposition)?" does
   NOT predict whether the spectrum stays real. Both directions of a
   naive reading fail: some zero-imag_part cases are trivially real (as
   expected), but so are SEVERAL nonzero-imag_part cases (`i*aw`,
   `i*ax`, `i*bw` alone, `aw+i*bw`) -- while OTHER nonzero-imag_part
   cases genuinely break it (`M_sum` and three more tested variants).
2. **A second, self-noticed candidate pattern was checked and also
   refuted, before being reported as a finding.** The data table showed
   every "breaks reality" case had `imag_part` built only from `{ax,bx}`
   (never `{aw,bw}`), while every real-but-nonzero-imag_part case had
   `imag_part` built only from `{aw,bw}` (never `{ax,bx}`) -- a clean-
   looking pattern. This was directly tested against `M_pp` alone
   (`=aw+i*ax`, `imag_part=ax`) and `M_pm` alone (`=bw+i*bx`,
   `imag_part=bx`) -- both are long-established single CG components
   from C100/C101 with certified real spectra. Both stayed exactly real
   (`max|Im|=0.0`), directly refuting this second pattern before it was
   ever written up as a claim.
3. **Matrix entrywise-realness (tested informally during C109/C110's
   own scratch phase) also does not separate the groups**: `M_trace`
   and `M_sum` are both entrywise-real matrices, only one breaks
   reality; `M1_x`, `M1_z` are entrywise-imaginary matrices, both
   preserve it.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** (a) the simple covariance hypothesis (C109's own pearl,
stated form); (b) the ax/bx-vs-aw/bw refinement (noticed from this
round's own data, checked and refuted before being asserted).

**NOT killed:** C108's own finding (M_sum breaks reality at k=1, holds
at k>=2) and C109's own finding (the trigger requires the full 4-
component sum specifically) -- both fully unaffected, this round only
tested a proposed EXPLANATION for those findings, not the findings
themselves.

**What remains genuinely open:** the true criterion distinguishing
"breaks" from "preserves" among 4-component-CG linear combinations at
k=1. This round's own data (13 combinations with exact symbolic
`(real_part, imag_part)` decomposition and numeric reality status,
preserved in `results_c110.json`) is a resource for a future, more
systematic attempt -- e.g. a full parametrized sweep treating
`(c1,c2,c3,c4)` as 4 independent complex unknowns and directly solving
for the exact algebraic condition (via the characteristic polynomial or
resultant) under which `D_PW`'s spectrum stays real, rather than testing
hand-picked candidate combinations one at a time.

## What this cannot show

- Does not identify the true criterion -- explicitly out of scope for
  this round after two refuted candidates; flagged as a sharper open
  pearl below rather than force-fit a third unverified pattern.
- Does not test k>=2 (already established real under any tested
  coupling in C108).
- Does not change N_gen=3's CONDITIONAL status.
- Does not touch OB1.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260830-c110-covariance-hypothesis-tested-refuted/`
  -- clean, 0 errors.
- All symbolic decomposition via exact sympy arithmetic (no floating-
  point in the `(real_part, imag_part)` classification); numeric
  eigenvalue checks via the certified `np.linalg.eigvals` convention.
- This round's own process is itself a demonstration of the project's
  hand-algebra-is-unreliable lesson: an initial by-hand computation of
  one test case's coordinate decomposition was wrong (caught when it
  contradicted the exact sympy result), and a second candidate pattern
  noticed directly in this round's own output table was checked against
  known prior results (`M_pp`, `M_pm` from C100/C101) BEFORE being
  written up, and was also found false. Both corrections are recorded
  here transparently rather than only presenting the surviving
  narrative.
