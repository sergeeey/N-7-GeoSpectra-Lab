# Round102 (A1) — Decision

**Date:** 2026-07-17
**Verdict:** `WEAKENED__NARROW_ALGEBRA_LEVEL_OPEN_QUESTION__NOT_A_REOPENING__ORIGINAL_G2_ARGUMENT_WAS_A_CATEGORY_ERROR`
(skeptic verdict, Step 8a, context-asymmetric review — claim + code only)
**Go/no-go:** does **NOT** reopen gate G97, does **NOT** supply an
alternative `SU(4)` realization, and does **NOT** license any downstream
physics conclusion to be revisited. What survives is a narrow, genuine,
previously-unflagged algebra-level question worth a dedicated follow-up —
correctly separated here from my own first-draft "fix," which the skeptic
correctly identified as a category error.

## What happened, stated honestly (including my own mistake, per this
project's audit-verification-gate discipline of never silently smoothing
over a self-caught or skeptic-caught error)

I initially proposed: (1) `so(6)⊂so(7)` genuinely exists (tool-verified,
correct), (2) since `so(6)≅su(4)` (D₃=A₃), gate G97's literal wording ("no
`SU(4)` subgroup in `Iso(S³×S⁶)=SO(4)×SO(7)`") is imprecise, (3) but the
PHYSICAL conclusion is likely still fine because `SU(3)_c` actually comes
from **`G₂`-holonomy** (`preprint.tex:195-196,274-277`), not the full
`SO(7)` isometry, and `dim(G₂)=14<15=dim(su(4))` rules out `SU(4)` fitting
in `G₂` alone.

**The skeptic (Step 8a, context-asymmetric) found two real problems with
this, both accepted here, not dismissed:**

1. **Group vs. algebra conflation [ACCEPTED, my error]:** `SO(6)` and
   `SU(4)` are **not the same group** — `SU(4)` is the double cover
   (`Spin(6)`), `SO(6)=SU(4)/ℤ₂`. Gate G97's literal wording says "no
   `SU(4)` **subgroup**" — read strictly at the GROUP level, this is
   actually TRUE and defensible (`SU(4)` itself, as opposed to `SO(6)`,
   genuinely is not a subgroup of `SO(7)`). I had the direction of the
   imprecision backwards: the group-level statement survives; the
   ALGEBRA-level question (`su(4)` as a Lie algebra, which is what
   actually counts Killing-vector generators / gauge bosons) is the one
   left genuinely open, not obviously settled either way by G97's existing
   citations.

2. **Category error in my own proposed "fix" [ACCEPTED, my error]:**
   substituting `G₂`-holonomy for `SO(7)`-isometry as "the relevant
   ambient group" is **not a precision correction, it is swapping in a
   different mathematical object.** Isometries (Killing vectors of the
   metric) and holonomy (parallel-transport structure group) are
   logically distinct notions. "`SU(3)_c` happens to be derived from
   `G₂`-holonomy" does NOT license "therefore `G₂` is the right ambient
   group to check `SU(4)`-completion against" — that inference does not
   follow, and my dimension argument (`dim(G₂)=14<15`) only rules out
   `SU(4)` fitting inside `G₂` ALONE. It does **not** address the group
   gate G97 actually cites (`SO(4)×SO(7)`), where — at the pure ALGEBRA
   level — `so(6)⊂so(7)` still sits, unaddressed by my "fix."

## What genuinely survives, narrowly and honestly stated

The skeptic's own words: *"the core observation (G97 as literally worded
needs re-examination) survives"* — specifically, at the Lie-ALGEBRA level
(not the group level), `so(6)≅su(4)` is a genuine 15-dimensional
subalgebra of `so(7)`, hence of `so(4)⊕so(7)`. **Whether this algebra-level
fact corresponds to an ACTUALLY REALIZED, physically meaningful `SU(4)`
gauge symmetry — i.e., whether the specific Killing vectors generating
this `so(6)` subalgebra are consistent with (act correctly on) this
project's already-fixed fermion content, `SU(3)_c` embedding, and
`B-L`-preservation requirements (gate G98) — is a SEPARATE, HARDER, and
genuinely UNRESOLVED question.** This experiment does not resolve it
either way, and no prior round in this project appears to have addressed
it at the pure-algebra (as opposed to pure-group, or pure-holonomy) level
specifically.

## Applying the pre-registered criteria (claim.md Section 2)

**WORDING IMPRECISE, PHYSICS CONCLUSION LIKELY UNCHANGED** was the
pre-registered middle option — but even this must be stated more
narrowly than originally drafted: it is the ALGEBRA-level wording (not
literally present as a separate claim anywhere this project cites) that
has a genuine open question attached, NOT gate G97's actual, literal,
GROUP-level statement, which the skeptic confirms is defensible as
written. **GATE G97 GENUINELY REOPENED does NOT apply** — no working
alternative `SU(4)` construction was found or even attempted at the level
of actual Killing vectors on `S³×S⁶`.

## Kill Analysis

- **What this kills:** my own first-draft "G₂-holonomy dimension
  argument" as a valid repair or replacement for anything — it is
  withdrawn here as a category error, not carried forward.
- **What this does NOT kill:** gate G97 itself (untouched, still the
  correct, standing blocker for all downstream purposes); round90's
  `SU(4)³` cubic-anomaly finding (untouched); any of rounds 90-101's own
  conclusions (all correctly treated G97 as blocking, and remain correct
  to do so).
- **What this narrows, as a genuine (if modest) product of this round:**
  a previously-unasked, well-defined follow-up question, precisely
  stated: **is the algebra-level `so(6)⊂so(7)` embedding realized by
  actual Killing vectors of `S⁶` that are consistent with this project's
  fixed `SU(3)_c`/fermion content?** — distinct from, and not addressed
  by, either the group-level statement (G97, defensible as written) or
  the holonomy-level statement (`G₂`, a different object entirely). This
  question is flagged, not answered.

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Resolve the algebra-level question directly | Explicitly construct the `so(6)` Killing-vector fields on `S⁶` (round-metric isometries fixing a point) and check whether they act consistently with the already-fixed `SU(3)_c⊂G₂` embedding and fermion representation content — NOT attempted here, substantially harder than this round's dimension-counting/closure check |
| Check the "diagonal embedding" possibility the skeptic flagged | Whether `su(4)` could embed into `so(4)⊕so(7)` via a MIXED (not purely `so(7)`-internal) construction combining `S³`-side and `S⁶`-side generators — not addressed by either my original argument or this correction |

## Assumptions carried, unresolved

- `so(6)≅su(4)` at the Lie-ALGEBRA level (`D₃=A₃`) — standard classical
  fact, `[DOCS]`, not independently re-derived here beyond citing it.
- Whether "Killing vectors of the round `S⁶` metric" is even the correct
  notion of "isometry" to use given this project's ACTUAL construction
  uses the nearly-Kähler (not necessarily round) `G₂`-compatible metric —
  flagged by the skeptic's point 5 as a further open subtlety, not
  resolved here.

## What this does NOT mean

1. Does **NOT** reopen gate G97 — the standing blocker for the Pati-Salam
   /anomaly route remains exactly as established by rounds 90-101.
2. Does **NOT** supply, or claim to supply, a working alternative `SU(4)`
   geometric realization.
3. Does **NOT** license revisiting any downstream conclusion in this
   project (round90's `BLOCKED` verdict, round92/96's `FAIL`/no-forcing
   findings, etc.) — all remain correct and untouched.
4. Does **NOT** affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does **NOT** modify `preprint.tex` or any
   prior experiment folder — this round's own first-draft error is
   corrected WITHIN this same, newly-created folder, not propagated
   anywhere else.
5. **Explicitly logged as a self-correction, per this project's own
   established discipline (additive, not silent):** my first-draft
   verdict (before the mandatory skeptic review) would have overclaimed a
   "precision fix" that the skeptic correctly identified as a category
   error. This is recorded here in full, not smoothed over, exactly
   matching the pattern already used for round90's own Witten-anomaly
   self-correction and round93's K3/T3R documentation-bug correction.

## Check (reproduces the computational part of this decision)

```
cd experiments/20260717-round102-a1-su4-isometry-precision-check
python e28_su4_isometry_precision_check.py
```
Expect: `so6_is_genuine_subalgebra_of_so7=True`,
`su4_fits_in_g2_alone_by_dimension=False`. **Note:** the script's own
printed "PART 2" framing (treating the `G₂`-dimension argument as a
repair) is exactly the category error identified above — the script's
raw computational outputs (Part 1 and Part 2's bare numbers) are correct
and reproducible; the INTERPRETIVE framing printed alongside them is
superseded by this decision.md, not by a script edit (per this project's
practice of correcting interpretation via decision.md rather than
silently rewriting a script's own printed narrative after the fact).
