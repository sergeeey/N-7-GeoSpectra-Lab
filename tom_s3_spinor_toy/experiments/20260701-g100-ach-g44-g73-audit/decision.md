# Decision — G100: ACH matrix / docs coverage of G44 vs G73

**Date:** 2026-07-01
**Verdict:** PASS — real documentation-completeness gap, confirmed and fixed
**Go/no-go:** GO on documentation fix; NO-GO on any change to N_gen=3 math

## Result

Confirmed via grep (T1-T3) + direct read of primary sources (T4):

1. README.md states "N_gen = 3 **EXACTLY**" with zero mention of G67-C3
   (the open gate G73's own docstring says its argument depends on) or G44
   (the prior REJECT that used the identical G2-triality-collapse fact).
2. TOM_RECONSTRUCTION_ACH_MATRIX.md -- whose stated purpose is exactly this
   kind of competing-hypothesis tracking -- has NO case covering G44/G73/
   G67-C3 at all (6 cases exist, none touch N_gen=3).
3. RESEARCH_STATUS_REPORT.md lists G44 only inside a flat NULL-results
   table, never cross-referenced against G73's PROMOTE entry.
4. The caveat itself is genuine and HONESTLY stated in the primary source
   files (G67 docstring: "G67-C3: OPEN"; G73 docstring: "boundary
   conditions... depends on G72 (Tom)"). This is not a hidden flaw -- it
   is an UNPROPAGATED one. The authors of G67/G73 were transparent; the
   summary docs simply never carried that transparency forward.

## Fix applied

1. Added **Case 7** to TOM_RECONSTRUCTION_ACH_MATRIX.md, explicitly stating
   the G44-vs-G73/G67 relationship, the shared mathematical fact, and the
   current status (OPEN pending G67-C3 / G72-Tom).
2. Softened README.md's "N_gen = 3 **EXACTLY**" framing to note the
   dependency on G67-C3 (still unresolved), without removing the (correct,
   verified) math claim itself.
3. Added a cross-reference note in RESEARCH_STATUS_REPORT.md's G44 entry
   pointing to G73/G67-C3 and Case 7.

## What this does NOT mean

1. Does NOT change N_gen=3's mathematical content (G73/G74A/G74B/G75
   PROMOTE verdicts stand, verified 31/31 + other test suites, unaffected).
2. Does NOT resolve G67-C3 -- "do 3 distinct octonion channels (L_p, R_p,
   T_p) genuinely appear in the physical S3xS6 Dirac action" remains OPEN,
   same as before this audit. Resolving it would need new geometric work
   (possibly requiring Tom's G72 input per G73's own note), not a
   documentation exercise.
3. Does NOT mean the project's transparency culture failed -- the opposite:
   primary-source authors flagged the caveat correctly; this audit closes
   the gap between "flagged in the detail files" and "visible at a glance."

## Lesson

Grep-based documentation audits (does the top-level story match what the
detail files actually say) are cheap, low-risk, and can surface real gaps
that a purely mathematical/computational review (like G98/G99's skeptic
rounds) would not catch -- those check whether a NEW claim holds; this
checks whether an EXISTING, correctly-caveated claim is being represented
faithfully one level up. Worth doing periodically as the project scales
past ~100 gates, since transparency at the leaf level does not
automatically propagate to summary documents.
