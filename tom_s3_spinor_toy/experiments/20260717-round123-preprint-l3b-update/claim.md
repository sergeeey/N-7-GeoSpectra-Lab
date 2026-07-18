# Round123 — Claim

**Gauge/Hilbert/Triality closure program, item 8 (preprint rewrite) —
final item.** Executes the single concrete punch-list item round122's
`GLOBAL_RECOMPOSITION_AUDIT.md` §5 identified: `preprint.tex`'s L3b Open
Problems entry understates the project's own progress (no mention of the
`SO(4)×SO(4)` candidate or round119's gate application).

## L0 gate (EstimandOps)

**Question type: Descriptive.** Does adding a precisely-scoped paragraph
to L3b accurately reflect the current internal state without overclaiming
beyond what `TRIALITY_DISTINGUISHABILITY_GATE.md`'s own corrected verdict
(`GATE 1 OF 7 DONE / GATES 2-6 OPEN`) supports?

## Falsifiable claim

A new paragraph can be added to `preprint.tex`'s L3b entry (between the
existing index-arithmetic-closure paragraph and its concluding
"Confirming this physical input... T. Lawrence" sentence) that:
1. Accurately states the `SO(4)×SO(4)` construction and its result.
2. Does not overclaim beyond "algebraic distinguishability established";
   explicitly separates the two remaining obstructions (physical
   identification, dynamical consistency) rather than compressing them
   into a single vague "needs checking" caveat.
3. Compiles cleanly with `pdflatex` (matching this project's own
   established practice, round59/60).

## Pre-registered check

1. Re-read the exact current L3b text (`preprint.tex` lines ~1271-1296)
   before drafting, not from memory.
2. Draft the paragraph, run mandatory context-asymmetric skeptic review
   (the new paragraph + its cited sources only, no reasoning chain) before
   finalizing — this is a public-facing document, held to at least the
   same bar as internal registry edits this session.
3. Compile with `pdflatex` twice (resolve cross-references), check for
   undefined references or errors in the log.

## Kill criterion (pre-registered)

- If skeptic review finds the paragraph overclaims relative to
  `TRIALITY_DISTINGUISHABILITY_GATE.md`'s own corrected verdict — fix
  before finalizing, do not publish an overclaim into the manuscript.
- If skeptic review finds information loss that would mislead a reader
  (e.g. euphemizing a structural obstruction as an ordinary open
  question) — add back the missing precision, even if it lengthens the
  paragraph.
- If `pdflatex` reports errors or undefined references — fix before
  committing.

## What this does NOT mean

1. Does NOT change `N_gen=3`'s `CONDITIONAL` status or any claim in
   `CLAIM_LEDGER.yaml`.
2. Does NOT claim the `SO(4)×SO(4)` candidate resolves L3b — explicitly
   the opposite, per the paragraph's own content.
3. Does NOT rebuild the arXiv submission tarball or touch any other part
   of the preprint — scoped to this one paragraph only.
4. Does NOT affect `lambda=FREE_COUPLING_PARAMETER` or
   `safe_for_runtime=False`.
