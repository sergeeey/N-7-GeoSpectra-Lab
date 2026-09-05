---
# C160 Claim — OB12: cite a primary source for the sign-triple <-> KO-dimension table

**Date:** 2026-09-05
**FL tier:** [x] Standard (a literature-citation task, not a new physics claim)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — filled BEFORE searching anything)

1. Exact claim: this project's finite spectral triple `(A_F, H_F, D_F, J_F,
   gamma_F)` has a sign tuple `(J^2, JDJ^-1/D, JgJ^-1/g) = (+1, +1, -1)`,
   computed and verified in this repo (`docs/ko_dimension_registry.md`
   Entry 1, `[VERIFIED-sympy, C36]`). This is claimed elsewhere in the
   project (informally, not currently in preprint.tex per the claim-scope
   gate) to correspond to "KO-dimension 6," a label inherited from CCM
   (Chamseddine-Connes-Marcolli, arXiv:hep-th/0610241) without ever being
   independently derived or cited to a primary source's own stated
   sign-triple <-> KO-dimension table in THIS repo.
2. `OPEN_BLOCKERS.md` grep: [x] done — OB12 (line 676) states the gap
   precisely and names what closes it: EITHER (a) a cited primary source
   for the table with its own convention stated (which sign it calls
   epsilon, epsilon', epsilon''), since this repo's G18 docstring ordering
   may not match the literature's ordering, OR (b) an internal n-mod-8
   derivation for the model Clifford triple (harder, not this round's
   target — (a) is the cheap route).
3. `docs/ko_dimension_registry.md` re-read in full: [x] done — this is the
   canonical registry, already states exactly what's needed (Entry 1,
   "What closes it" section) and the hard rule: never write a bare "KO-dim
   N" without a RESOLVED mapping_status row here.
4. `null_results/` + `parked/` grep: [x] done, 0 hits for "KO-dimension
   table" or "sign-triple table" as a prior attempt.
5. `git log -S`/`-G` pickaxe: [ ] to be done by executing agent
   (`-S"sign-triple"`, `-S"epsilon.*epsilon"`).
6. Primary source re-read: [ ] this IS the task — see below. Do not accept
   any table from memory/training data. A real source must be fetched and
   quoted.
7. **Status:** [x] NEW.

---

## Explicit AI-Hypothesis Pre-Gate (Source Trace, mandatory here specifically)

This round's ENTIRE purpose is Source Trace (`falsification-ladder.md`
Step -4) for a fact this project has been citing informally without one.
**Hard rule for the executing agent: do not accept a sign-triple <->
KO-dimension table recalled from training data/memory as sufficient.**
The standard table (roughly: KO-0 through KO-7, some pattern of +/- for
epsilon/epsilon'/epsilon'') is extremely well-known in the NCG literature
and therefore is EXACTLY the kind of "confident because familiar" claim
this project's own rules flag as a red flag (`rules/integrity.md`:
"Package version... check in the registry" — same discipline applies to
a textbook table: check it against an actual fetched primary source, not
recollection, because different sources use different orderings/sign
conventions for which slot is called epsilon vs epsilon' vs epsilon'',
which is exactly the ambiguity OB12's own text flags).

---

## Estimand

**Population:** The specific finite spectral triple this project's Entry 1
concerns (`H_F = C^32`, one SM generation, `J_F` = 16 real transpositions,
`gamma_F = diag(-I16,+I16)`).

**Intervention:** Locate a citable primary source (a specific paper or
textbook, with author/year/arXiv-or-DOI) that states the sign-triple <->
KO-dimension correspondence table explicitly, in a form that can be quoted
verbatim (not paraphrased from memory).

**Comparator:** The current `BLOCKED_BY_EXTERNAL_INPUT` status (no source
cited anywhere in this repo).

**Endpoint:** Does a real, quotable source state a table under which
`(J^2,JDJ^-1/D,JgJ^-1/g)=(+1,+1,-1)` maps to KO-dimension 6 — using THAT
source's own stated ordering/naming of which sign is epsilon vs epsilon'
vs epsilon'' (not assumed to match this repo's own docstring ordering
without checking)?

**Summary measure:** RESOLVED (source found, table quoted, convention
matched explicitly, mapping confirmed or corrected) / STILL-BLOCKED (no
adequate primary source found this session) / CONVENTION-MISMATCH (a
source found, but its ordering doesn't obviously align with this repo's
tuple order, and reconciling requires more than this round's scope).

**MCID:** Not applicable — this is a citation/verification task, not a
magnitude estimate.

---

## Claim

**Falsifiable statement:** A specific, quotable primary source states the
sign-triple <-> KO-dimension table explicitly enough that this project's
own tuple `(+1,+1,-1)` can be checked against it (confirming, correcting,
or leaving unresolved the informally-inherited "KO-dim 6" label), with the
source's own sign-naming convention stated alongside the quote.

---

## Kill criterion (MANDATORY — filled BEFORE searching)

| Outcome | Verdict |
|---|---|
| A real, fetched (not recalled) primary source states the table with an explicit convention, and `(+1,+1,-1)` maps unambiguously to KO-dim 6 under it | RESOLVED — update `docs/ko_dimension_registry.md` Entry 1 to `mapping_status: RESOLVED`, cite the source, close OB12 |
| A real source states the table, but under its own convention `(+1,+1,-1)` maps to something OTHER than 6, or the mapping is ambiguous without further convention-matching work | CONVENTION-MISMATCH — report the discrepancy precisely, do NOT force a match, leave `mapping_status: BLOCKED` with the new information recorded |
| No adequate primary source can be located/fetched this session (e.g. paywalled, arXiv version doesn't state it explicitly enough) | STILL-BLOCKED — report exactly what was tried and what specifically is missing, stays `BLOCKED_BY_EXTERNAL_INPUT`, no change |

**Explicit escape route:** this is a one-session literature lookup. If it
turns out the "convention reconciliation" is itself nontrivial (the found
source's epsilon/epsilon'/epsilon'' ordering doesn't obviously correspond
to this repo's `(J^2, JDJ^-1/D, JgJ^-1/g)` ordering, and matching them
requires actual derivation, not just reading), STOP and report
CONVENTION-MISMATCH rather than improvising a derivation — that would
silently convert this cheap citation task into OB12's OTHER, harder
closure route (an internal n-mod-8 derivation), which is explicitly out
of scope here.

## What this does NOT mean

- A RESOLVED verdict does NOT mean anything about the geometric-side
  reality types (C32/C33) or their combination with this finite KO-number
  — `docs/ko_dimension_registry.md`'s own "Scope note" explicitly forbids
  combining them without a separate theorem; this round does not touch
  that question.
- Does NOT mean OB2's own closure (the `t=0,1` doubled construction is not
  a valid geometry, independent of this KO number) becomes more or less
  true — OB12's own text already notes this is "low-stakes as things
  currently stand" regardless of this round's outcome.
- Does NOT commit to attempting the internal n-mod-8 derivation route
  (OB12's other closure option) if this round finds STILL-BLOCKED or
  CONVENTION-MISMATCH.
