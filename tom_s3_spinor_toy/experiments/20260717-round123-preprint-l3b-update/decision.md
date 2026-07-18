# Round123 — Decision

**Date:** 2026-07-17
**Verdict:** `APPLIED — L3b paragraph added, skeptic-corrected once,
compiled clean` (final item of the gauge/Hilbert/triality closure program)

**Go/no-go:** `preprint.tex`'s L3b Open Problems entry now accurately
reflects the `SO(4)×SO(4)` finding and round119's `GATE 1 OF 7 DONE /
GATES 2-6 OPEN` verdict, with the two specific remaining obstructions
(physical identification, dynamical consistency) named precisely rather
than compressed into a vague caveat. Compiled clean, `pdflatex` ×2, exit 0
both passes, 30 pages, no undefined references.

## Single skeptic pass — one substantive finding, fixed

Ran the mandatory context-asymmetric skeptic review (the new paragraph +
`L3B_SPIN8_INTERFACE_SPEC.md` + `TRIALITY_DISTINGUISHABILITY_GATE.md` as
cited sources, no reasoning chain) — held to the SAME bar as internal
files this session, arguably a higher one since this is public-facing.
Verdict: `WEAKENED`. Every mathematical claim checked out accurate against
source (the `H⊕Hℓ` split, the `SO(4)×SO(4)` group, the `Γ_A,Γ_B`
block-chirality values, the rank-4-cannot-embed-in-rank-3-`SO(7)`
argument, the triality-invariance claim) — no factual error found. But
the first draft **compressed two nuances the source material itself
flags as load-bearing**, in a way that would mislead a careful reader:

1. **The "physical Dirac operator remains consistent" caveat read as an
   ordinary future-work item, when the source is sharper:** `G74A`'s
   Lemma B (the proof of the EXACT kernel dimension, `dim ker=1` not just
   `≥1`) uses Schur's lemma on EXACT `G₂` symmetry — a technique that does
   not merely need re-checking once `G₂` breaks, it **structurally no
   longer applies at any nonzero breaking**, and no `Spin(4)×Spin(4)`-
   equivariant analogue exists with current tools (this candidate acts
   only on the fiber, not the base, so the original proof's
   base-transitivity argument has no counterpart). Skeptic: "promoting a
   structural obstruction... to a procedural caveat... these read the
   same to a skimming reader but mean different things to a careful one,
   and preprints get read carefully."
2. **The physical-identification gap was compressed to vagueness:** first
   draft said "act globally on the physical compactification" — the
   source is more concrete: nothing fixes WHICH (if either) `SO(4)` factor
   is `S³`'s actual `SU(2)_L×SU(2)_R`, and what the OTHER factor would even
   represent is entirely unaddressed.

**Fixed directly**, not deferred: rewrote the paragraph's final section to
name both obstructions explicitly and precisely, per skeptic's own
recommended wording (adapted, not copied verbatim). Also defined `H` and
`ℓ` parenthetically on first use (skeptic's third, minor finding — the
internal spec's context is too thin for a standalone public reader).

## What was actually verified this round

- Re-read `preprint.tex`'s exact current L3b text before drafting.
- Compiled with `pdflatex -interaction=nonstopmode preprint.tex`, twice
  (resolves cross-references) — exit 0 both times, 30 pages, output
  byte-identical page count between runs, `grep -i "undefined"
  preprint.log` returns no undefined-reference warnings.
- Skeptic re-verified every mathematical claim in the new paragraph
  directly against `L3B_SPIN8_INTERFACE_SPEC.md` and
  `TRIALITY_DISTINGUISHABILITY_GATE.md` line-by-line, not from paraphrase.

## Kill Analysis

- **What this kills:** the understatement gap round122 found (L3b
  previously had no mention of the `SO(4)×SO(4)` candidate at all).
- **What this does NOT kill:** L3b's own open status — the paragraph
  explicitly does not claim resolution, only that a candidate exists with
  two named, unresolved obstructions.
- **What survives as a scoped next step:** round122's OTHER punch-list
  item (`docs/gates_tracker.md` extension through `G97`/rounds 102-122) —
  explicitly not attempted this round, remains an accepted, documented lag.

## What this does NOT mean

1. Does NOT change `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
2. Does NOT claim L3b is resolved — the added text is explicit that it is
   not.
3. Does NOT rebuild the arXiv submission tarball — scoped to the LaTeX
   source only; a tarball rebuild is a separate, mechanical follow-up if
   the user intends to actually resubmit somewhere.
4. Does NOT touch any other section of `preprint.tex`.

## Standing lesson (sixth consecutive round, 118-123)

**Compressing a nuanced internal audit into public-facing prose has its
own specific failure mode: promoting a structural obstruction to a
procedural one.** "Needs to be checked" and "the standard tool cannot be
applied here at all" read identically to a skimming reader but license
very different confidence levels to a careful one — and a preprint's
readers are, by construction, the careful kind. Sixth consecutive round
where mandatory skeptic review caught something a first draft missed —
this time in the one place (the actual manuscript) where the stakes of
missing it are highest.

## Check (reproduces the compile verification)

```
cd tom_s3_spinor_toy
pdflatex -interaction=nonstopmode preprint.tex
pdflatex -interaction=nonstopmode preprint.tex
grep -i "undefined" preprint.log
```
Expect: exit 0 both passes, "Output written on preprint.pdf (30 pages...)"
both times, no undefined-reference hits.
