# G100 — ACH matrix / top-level docs coverage of G44 vs G73 relationship

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
G73's "N_gen=3 PROMOTE" verdict rests on an explicitly-flagged open gate
(G67-C3: "prove all 3 channels appear in S3xS6 action" — unproven, per G73's
own "boundary conditions" section). G44 (one day earlier) used the IDENTICAL
mathematical fact (G2=Fix(Z3) triality collapse: 8_v|G2=8_s|G2=8_c|G2=7+1)
to REJECT a related mechanism. This claim states: the top-level docs
(README.md, TOM_RECONSTRUCTION_ACH_MATRIX.md) do not surface this
relationship, giving readers an impression of more certainty than the
primary source files (G67, G73) themselves claim.

**Kill target (MANDATORY — Strong Inference):**
Does the caveat already exist prominently at top level?
- FAIL (caveat already surfaced + G44 cross-referenced somewhere top-level)
  -> no real gap, false alarm, close as NULL.
- PASS (caveat absent from README/ACH matrix, G44 never cross-referenced
  anywhere) -> real documentation-completeness gap, confirmed; fix by
  adding an ACH Case + softening README's unqualified "EXACTLY" framing.

**Checks planned:**
- T1: grep README.md for G44/G67-C3 near N_gen=3 claims
- T2: grep TOM_RECONSTRUCTION_ACH_MATRIX.md for G44/G73/G67-C3 (any case)
- T3: grep RESEARCH_STATUS_REPORT.md for cross-reference between G44's NULL
  entry and G73's PROMOTE entry
- T4: read G67 and G73 source directly to confirm the caveat is genuinely
  present in primary sources (i.e. this is a propagation gap, not a
  newly-discovered flaw)

**Verdict:** PASS — gap confirmed.
- T1: FAIL (grep) — README line 23 "N_gen = 3 **EXACTLY**", no G44/G67-C3
  nearby, no caveat anywhere in the file.
- T2: FAIL (grep) — zero matches for G44, G73, or G67-C3 in the entire ACH
  matrix file. The matrix's own stated purpose is exactly this kind of
  cross-case tracking; this case was never added.
- T3: FAIL (grep) — G44 appears only inside a flat NULL-results list
  (RESEARCH_STATUS_REPORT.md line 261), no link to G73's entry.
- T4: PASS (read) — G67 docstring line 34: "G67-C3: OPEN — prove all 3
  channels appear in S3xS6 action". G73 docstring "BOUNDARY CONDITIONS"
  section: "Geometric realization of E_v bundle... depends on G72 (Tom).
  Here we use algebraic triality argument." Caveat is genuine and honestly
  stated in primary sources -- this is a propagation/documentation gap,
  NOT a newly discovered mathematical error in G73 itself.

**Evidence:** [VERIFIED-grep 3/3 confirm absence] + [VERIFIED-read 1/1
confirm caveat exists in primary source]

**Caveat / What this does NOT mean:**
- Does NOT mean N_gen=3 is wrong -- G73's own math is untouched; this is
  about documentation propagation, not a computational refutation.
- Does NOT resolve whether "3 distinct channels genuinely appear in the
  S3xS6 action" (G67-C3 itself remains OPEN, unresolved by this audit) --
  that requires new physics/geometry work (likely Tom-dependent, per G73's
  own note about G72), not a documentation fix.
- Does NOT imply the ACH matrix or README were written in bad faith --
  most likely explanation is G44 (2026-06-20) and G73 (2026-06-21) were
  worked in adjacent but separate sessions and the connection was simply
  never drawn, an ordinary omission in a fast-moving research log.

**Fence (do not change):**
- lambda_v_operator = FREE_COUPLING_PARAMETER
- sm_derivation_claimed = False
- N_gen=3 math (G73/G74A/G74B/G75) unchanged -- only documentation updated

**Status:** CLOSED PASS
