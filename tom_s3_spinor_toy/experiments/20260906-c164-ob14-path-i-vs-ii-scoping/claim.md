# C164 Claim — scoping OB14's two remaining sub-paths (i')/(ii'): is either one
# cheaper or better-motivated to attempt next, or does neither have a genuine
# independently-motivated construction available right now?

**Date:** 2026-09-06
**FL tier:** [x] Full (touches OB14's central blocker; a wrong scoping call here
could send a follow-up round down an expensive, high-AOG-5-risk construction)
**Question type:** [x] descriptive (does this project's own existing content
supply a cheap, independently-motivated next test for either sub-path — or
does it not)

**Mode:** SCOPING ONLY, per the orchestrating session's explicit instruction.
No new Dirac operator, no new connection, no new twist-bundle construction is
attempted in this round. This mirrors C142 (design-only candidate scan) and
C161 (construction scoping before commitment) — the deliverable is a
recommendation of WHICH (if either) sub-path to attempt next, and WHAT the
cheapest concrete first test would be, not the attempt itself.

---

## 0. Background — the exact target (fixed, quoted from OPEN_BLOCKERS.md OB14)

C162 (2026-09-06, `experiments/20260906-c162-ob14-w-cand-scoping/decision.md`,
tool-verified, independent-skeptic-confirmed `CONFIRMED-REAL`) found that
`W_cand=3⊕3̄⊕3̄`'s ONE currently-buildable instantiation (`m ⊕ decoupled
3̄_extra`) has `Delta_dyn=0` **forced for any connection** the decoupled
summand could carry — not a numeric accident, but a plain `su(3)` branching
fact (`Σ_even⊗3̄_extra` has zero invariants, so no decoupled connection has any
invariant target to map into). This sharpened `OPEN_BLOCKERS.md` OB14's
"Owner / next step" into exactly two named sub-paths (quoted verbatim,
`OPEN_BLOCKERS.md` lines 2405–2409):

- **(i')** find a `W_cand`-type construction that AVOIDS `m` entirely, so the
  zero-invariant obstruction C162 found does not apply (it specifically arose
  from `m`'s own presence in the module);
- **(ii')** find independent geometric coupling data (not merely a decoupled/
  zero-connection default) that COUPLES a new summand's connection to `m`'s
  own tangent bundle.

The user has authorized proceeding on "(i') or (ii')" but has NOT picked
which — this file's job is to make that choice on evidence, per this
project's Cheapest Differentiating Test (CDT) protocol and the Anti-
Overfitting Gate's AOG-5 (independent motivation) check, not to guess.

---

## Prior Result Gate (MANDATORY — filled BEFORE reaching any conclusion)

1. **Exact claim to check.** For each of (i')/(ii'): (a) does a genuinely new,
   independently-motivated candidate construction exist in this project's
   content that C142/C162 did not already consider; (b) what is the cheapest
   possible test of it; (c) does it pass the AOG-5 independent-motivation
   check.
2. **`decision.md` grep**, done this session, for `W_cand`, `3̄_extra`,
   "second copy", "avoid m", "couple.*tangent bundle", "independently-sourced"
   against every `experiments/2026090[24]-c1[3-6][0-9]*/decision.md` file and
   `OPEN_BLOCKERS.md`: [x] done — hits confined to C139/C141/C142/C143/C144/
   C145/C146/C162's own already-read rows (see Section 1 below for what was
   read in full).
3. **`null_results/INDEX.md` + `parked/INDEX.md` + `pearl_registry/INDEX.md`
   grep**, done this session, for `OB14`, `3bar`, `W_cand`, `triality`, `G44`,
   `Inn(su(3))`, `gauge freedom`, "second copy", "independently-sourced":
   [x] done, 0 hits proposing any construction for (i') or (ii') beyond what
   C142/C162 already registered (pearl_registry rows dated 2026-09-04 and
   2026-09-06, both already read in full — see Section 2).
4. **`git log --all -S"3bar_extra" -S"avoid m" -S"decoupled" -S"triality"`**:
   [x] run this session — hits confined to the C139–C162 commits themselves
   (already read) and unrelated pre-2026-09 commits (`decoupled`, `triality`
   also match older, unrelated topics, checked and confirmed irrelevant by
   inspection of commit message + diff context).
5. **Primary source re-read**, this session, in full: `experiments/20260904-
   c139-twisted-s6-alternate-representation-negative-control/decision.md`
   Section 17 (lines 951–1030, the "only buildable option is decoupled"
   reasoning, re-read directly rather than trusted from C162's own
   paraphrase); `experiments/20260904-c142-graded-floor-candidate-scan/
   decision.md` (full, 193 lines — Sections 3a/3b/3c, the two rejected
   candidates and the "no other candidate identified" closing); `experiments/
   20260906-c162-ob14-w-cand-scoping/decision.md` (full, 364 lines) and
   `claim.md` (full, 516 lines, esp. its own "Cost estimate" section);
   `OPEN_BLOCKERS.md` OB14 section in full (lines 2256–2426). Additionally,
   this session searched BEYOND what C142 checked (a genuinely new sweep, not
   a re-read): `experiments/20260902-c134-ecsk-torsion-auxiliary/decision.md`
   (the project's other named torsion-tensor construction, checked for
   relevance to an `su(3)`-equivariant coupling on `S⁶` — see Section 3
   below), and a codebase-wide grep for `ADNU`/`NOMIZU` usage sites (30+
   files) to confirm no other already-computed `su(3)`-equivariant tensor
   exists outside the ones C139/C141/C142/C162 already used.
6. **Status:** [x] NEW — this specific question (a head-to-head scoping of
   (i') vs (ii'), including a genuine extension of C142's own two-candidate
   search to the project's OTHER named torsion/curvature construction) has
   not been attempted. C162's own claim.md already contains a "Cost
   estimate" section assessing both sub-paths in passing (as part of scoping
   its own, narrower question); this file treats that assessment as a
   starting hypothesis to be checked, not as a settled prior result to cite
   uncritically — see Section 4 for where this file's own check agrees with
   it and adds the torsion-sweep as new, independent confirmation.

If either candidate turns out already `CLOSED`/`SUPERSEDED` under a stronger
reading — cite it and stop rather than re-deriving.

---

## AI-Hypothesis Pre-Gates (mandatory — any candidate construction this file
might propose would be this session's own synthesis, not primary literature)

**Step -4, Source Trace.** Every fact this file's argument depends on is this
project's own, already-certified internal result, cited at file:section:
C139 Section 17 (the "no NOMIZU-derived data, decoupled is the only buildable
option" quote); C142 Sections 3a/3b/3c (the two rejected candidate sources —
C70/C71's gauge-freedom intertwiners, G102's forced-identical triality
channels); C162 Sections 0–9 (the forced-zero result and its own named
sub-paths); C134 (the project's other torsion construction, checked fresh
this session for relevance). No external literature claim is made or needed.

**Step -3, Novelty Check.** Searched `null_results/INDEX.md`, `parked/
INDEX.md`, `pearl_registry/INDEX.md`, `OPEN_BLOCKERS.md`, and the
`experiments/` tree (Prior Result Gate items 2–4) for any prior attempt at
this specific head-to-head scoping. **0 hits.** The closest prior content is
C162's own "Cost estimate" section, which assesses both sub-paths in passing
as part of a narrower round — this file is the first to make that assessment
the round's own primary question, re-verify it independently, and extend the
search to a construction (C134's torsion) C142 never considered.

---

## Estimand

**Population:** This project's own already-certified geometric content
(`NOMIZU`/`ADNU` structure constants, `m`'s tangent/isotropy representation,
C70/C71's triality intertwiners, G102's triality channels, C134's ECSK
torsion tensor), searched for any `su(3)`-equivariant object capable of
serving as (i') an independent source for `W_cand=3⊕3̄⊕3̄` that does not use
`m`, or (ii') geometric data coupling a new summand's connection to `m`'s own
tangent bundle.

**Intervention:** A structured re-examination of (a) whether C142's own
two-candidate search (C70/C71, G102) was exhaustive over this project's
CURRENT content, or whether a construction it did not consider (specifically
C134's torsion tensor, and any other named curvature/torsion object in this
project) supplies what either sub-path needs; (b) an explicit AOG-5
independent-motivation check for any candidate that survives (a); (c) a CDT-
protocol cost/differentiation comparison between (i') and (ii').

**Comparator:** `OPEN_BLOCKERS.md` OB14's own current framing, which treats
(i') and (ii') as two symmetric, equally-unattempted options without stating
which (if either) has a cheaper or better-motivated concrete next test.

**Endpoint:** One of three outcomes: (a) one sub-path has a genuinely cheap,
independently-motivated next test that the other lacks — name it precisely
enough for a follow-up round to execute directly; (b) both sub-paths have
some test available but neither is clearly cheaper/better-motivated — name
both, let the orchestrating session choose; (c) neither sub-path has any
independently-motivated construction available in this project's current
content — an honest `BOTH-HIGH-RISK-NO-CHEAP-DIFFERENTIATOR` verdict.

**Summary measure:** Not a magnitude — a categorical verdict among (a)/(b)/(c)
above, each with its own AOG-5 disposition per sub-path.

**MCID:** Not applicable — this is a structural/feasibility question, not a
magnitude estimate.

**Intercurrent events (ICE):** If the fresh sweep (C134 torsion, or any other
construction) turns up a genuinely new candidate C142 did not consider, that
is the expected, informative outcome of doing the search — report it and its
own AOG-5 status, do not silently fold it into a pre-decided verdict.

---

## Claim

**Falsifiable statement:** Re-examining C142's search against this project's
full inventory of already-computed geometric tensors (not just the two
candidates C142 checked) will either (a) surface at least one construction
capable of supplying independent `su(3)`-equivariant data for (i') or (ii'),
in which case that construction — and only that one — gets scoped as the
next concrete test; or (b) confirm C142's search was in fact exhaustive over
current content, in which case neither sub-path has a cheap next test and
the honest verdict is that both require inventing new, currently-unmotivated
geometric structure.

**Supporting sub-claims:**
1. C134's ECSK torsion tensor `T^t` is an `so(3)`-valued (not `su(3)`-valued)
   object living on the `S³` factor, not on `S⁶`'s tangent bundle `m` — so it
   cannot supply an `su(3)`-equivariant map into `3` or `3̄` regardless of its
   own nonvanishing, structurally, not merely because nobody has tried.
2. No other already-computed tensor in this project's `NOMIZU`/`ADNU`-based
   machinery (used across 30+ scripts, `round59` through `c162`) constructs
   an `su(3)`-equivariant map between two DIFFERENT geometric objects — every
   such map found is either (a) internal to `m`'s own structure (the
   `NOMIZU`-derived connection acting on `m` itself), or (b) a basis-relabeling
   of the SAME object (C70/C71's `Inn(su(3))`-orbit intertwiners).
3. Sub-path (i') and sub-path (ii') are NOT symmetric in cost, once assessed
   honestly: (i') requires abandoning the one already-available channel (`m`)
   and finding independent sources for potentially all three of `W_cand`'s
   summands; (ii') requires inventing a NEW kind of geometric object (a
   cross-coupling between two separate bundles) that has no precedent
   anywhere in this project's history. Neither is cheap; this file's job is
   to state which is *less* expensive/more motivated, not to pretend either
   is actually cheap.

---

## Kill criterion (MANDATORY — filled BEFORE reaching a conclusion)

| Outcome | Verdict |
|---|---|
| Fresh sweep (C134 torsion + full `ADNU`/`NOMIZU` usage audit) surfaces a genuinely new, independently-motivated `su(3)`-equivariant source for (i') or (ii') that C142 did not consider | Name it, scope its cheapest test, recommend that sub-path |
| Fresh sweep confirms C142's search was exhaustive; NEITHER sub-path has an independently-motivated construction in current content | `BOTH-HIGH-RISK-NO-CHEAP-DIFFERENTIATOR` — state this plainly, do not manufacture a "recommended" path just to have one |
| Fresh sweep finds a candidate, but it fails the AOG-5 independent-motivation check on inspection (motivated only by "we need something to unblock OB14," not by independent physical/mathematical reasoning) | Name the candidate, name why it fails AOG-5, do not promote it to "recommended next test" |
| C134's torsion tensor (or another candidate) turns out, on closer reading, to actually be `su(3)`-equivariant on `S⁶` (structural claim 1 above is wrong) | `SCOPE_ERROR_IN_THIS_FILE` — re-derive from scratch, this changes the whole analysis |

**Explicit escape route:** if the verdict is `BOTH-HIGH-RISK-NO-CHEAP-
DIFFERENTIATOR`, STOP here — do not manufacture a forced choice between (i')
and (ii') to satisfy the user's authorization to "proceed on (i') or (ii')."
An honest null scoping result is a valid, informative outcome per this
project's own `research-methodology.md` ("NULL = progress").

---

## Checks planned

- T1: Re-verify C142's own claim that no independent second `3̄` (or `3`)
  source exists, by re-reading C142 Sections 3a/3b/3c directly (not from
  C162's or OPEN_BLOCKERS.md's summary) and confirming the two rejected
  candidates' rejection reasoning holds up.
- T2: Check C134's ECSK torsion tensor for `su(3)`-equivariance / relevance
  to `S⁶`'s isotropy action — a construction C142 did not consider because
  it postdates C142 by two days and lives in a different part of the
  project's history (the `S³` torsion/ECSK sub-thread, not the `S⁶` twisted-
  Dirac sub-thread).
- T3 (adversarial): actively look for a candidate that would make EITHER
  sub-path cheap — do not merely confirm the expected null; check whether
  any curvature invariant, second fundamental form, or associative/coassociative
  form data already computed in this project's `G₂`/`S⁶` content could serve
  as coupling data for (ii'), before concluding none exists.

---

## What this does NOT mean

1. Does NOT itself constitute a verified physics result about `W_cand` or
   OB14 — this is a feasibility/scoping question about what construction (if
   any) is worth attempting next.
2. Does NOT attempt or execute either sub-path (i') or (ii') — per the
   orchestrating session's explicit instruction, this round stops at the
   scoping recommendation.
3. Does NOT resolve OB14 — `Sigma` remains unexplained as the physically
   preferred twist regardless of this file's verdict.
4. Does NOT change `N_gen=3`'s CONDITIONAL status, `lambda =
   FREE_COUPLING_PARAMETER`, `sm_derivation_claimed = False`, or
   `safe_for_runtime = False`.
5. Does NOT edit `OPEN_BLOCKERS.md`, `pearl_registry/INDEX.md`,
   `null_results/INDEX.md`, or `CLAIM_LEDGER.yaml` — registry updates are the
   orchestrating session's, per C124–C163 precedent.
6. Does NOT solicit Tom Lawrence's Part 5.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

[Filled in `decision.md` — this file is the pre-registered scoping frame.]
