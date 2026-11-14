# C166 Claim — Does AHL2023 supply independent su(3)-equivariant coupling data relevant to OB14?

**Date:** 2026-09-06
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
(descriptive: "does source X contain object Y" — no causal/predictive claim about physics)

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: "AHL2023 (arXiv:2203.02961) contains a construction of
   su(3)-equivariant coupling data between two DIFFERENT geometric
   bundles/representations on S⁶=G₂/SU(3) — relevant to OB14 sub-paths
   (i')/(ii') — that has not already been tried and rejected in this
   project."
2. `decision.md` grep (formula + synonyms "AHL2023", "coupling data",
   "Agricola"): [x] done, hits reviewed at:
   `experiments/20260717-round114-ahl2023-torsion-killing-spinor-crosscheck/decision.md`
   (different question: tested whether AHL2023's S³ torsion-Killing-spinor
   formula independently reproduces round67's h_H=3 — FALSIFIED as
   non-independent, restates Friedrich 1980. Does NOT touch S⁶=G₂/SU(3),
   does NOT touch cross-bundle coupling. Genuinely different question);
   `experiments/20260906-c164-ob14-path-i-vs-ii-scoping/decision.md`
   Section 9, Concern 4 (names this exact scope gap, not yet closed);
   `experiments/20260904-c139-.../decision.md` (background, cited by C164).
3. `round*_claim.md` + scripts grep: [x] done, 0 hits for AHL2023 outside
   round114/round121 (round121 = Agricola 2002, a *different* paper,
   already NULL per `null_results/INDEX.md` Round121-Agricola2002 for an
   unrelated Casimir-gap question).
4. `null_results/` + `parked/` grep: [x] done. `null_results/INDEX.md`
   `Round114-AHL2023` (FALSIFIED, S³ Killing-constant restatement — not
   this question) and `Round121-Agricola2002` (NULL, different paper,
   different question). `pearl_registry/INDEX.md` row 2026-07-17 (the
   "one-line-reducibility test" methodological lesson from Round114 —
   applies as a discipline check on THIS round's own verdict, see below).
   `pearl_registry/INDEX.md` row 2026-07-15 (Round 65) confirms AHL2023 is
   scoped to homogeneous SPHERES only (S^n), explicitly NOT flag manifolds
   like SU(3)/T²  — consistent with, not contradicting, this round's own
   primary-source read. No hits in `parked/INDEX.md`. 0 hits for this
   exact question ("cross-bundle coupling data for OB14") anywhere.
5. `git log -S`/`-G` pickaxe: [x] done (grep-equivalent across
   experiments/, null_results/, pearl_registry/, parked/, OPEN_BLOCKERS.md
   — no prior round asked this specific question).
6. Primary source re-read (not from memory): [x] done, this round —
   arXiv:2203.02961v3, LaTeX source via `mcp__arxiv__get_paper_latex_section`
   (sections 2.3, 2.4, 4.1.1, 5.1) plus HTML abstract/intro/preliminaries
   via `mcp__arxiv__download_paper`/`read_paper`. NOT from memory, NOT
   from round114's prior partial read (round114 only used §2.1-2.2,
   Thm 3.13/Cor 3.14/Prop 3.17 for S³; this round reads §2.3 (Nomizu map
   formalism), §2.4 (torsion classes), §4.1.1 (quaternionic isotropy
   coupling example), §5.1 (S⁶=G₂/SU(3), the coset OB14 needs)).
7. **Status:** [x] NEW

Genuinely different from Round114 (S³ Killing-constant restatement) and
Round121 (different paper, different question). Proceeding.

---

## Estimand

**Population:** The published text of AHL2023 (arXiv:2203.02961v3),
specifically its treatment of `S⁶=G₂/SU(3)` (§5.1) and its general
Nomizu-map/torsion-class formalism (§2.3-2.4), plus one comparison case
with genuinely reducible isotropy (§4.1.1, quaternionic spheres) to check
whether a relevant general METHOD exists elsewhere in the paper even if
not applied to S⁶ itself.
**Intervention:** Read (not compute/re-derive) the source's own stated
constructions for objects that could supply su(3)-equivariant coupling
data between two DIFFERENT representations/bundles on `S⁶=G₂/SU(3)`.
**Comparator:** OB14's own stated need (`OPEN_BLOCKERS.md` OB14, C142/C162
sub-paths (i')/(ii')): either (i') a `W_cand`-type module avoiding `m`
entirely, or (ii') independent (non-decoupled) coupling data linking a new
summand's connection to `m`'s own tangent bundle.
**Endpoint:** Binary/categorical verdict per the kill-criterion table
below — does the source, as published, contain such a construction.
**Summary measure:** Categorical verdict (not a numeric statistic —
this is a literature-content question, not a computation).
**MCID:** N/A (descriptive/categorical, not a continuous measure).

---

## Claim

AHL2023, read directly from its own LaTeX source for `§5.1 (S⁶=G₂/SU(3))`
and its general connection/torsion formalism (`§2.3-2.4`), does **not**
contain a construction of su(3)-equivariant coupling data between two
distinct geometric bundles/representations on `S⁶=G₂/SU(3)` that OB14's
sub-paths (i')/(ii') could use — because the paper's own stated isotropy
representation for this specific coset is **irreducible** (a single real
6-dimensional SU(3)-module, complexifying to `3⊕3̄`), leaving no second,
independent invariant summand for any coupling construction to act
between.

Supporting sub-claims:
1. AHL2023 §5.1 explicitly states the isotropy representation on
   `S⁶=G₂/SU(3)` is irreducible ("the only invariant metrics are obtained
   from multiples of the Killing form").
2. Every object AHL2023 constructs for this coset (invariant spinors
   `Σ_inv`, the nearly-Kähler 2-form `J`, the Ambrose-Singer torsion
   `T^AS`) is valued in `Λ^•m` (exterior powers of the tangent
   representation itself) — none introduces an independent bundle or
   representation distinct from `m`.
3. AHL2023 DOES contain a genuine cross-summand coupling construction
   elsewhere (§4.1.1, quaternionic spheres `Sp(n)·K/Sp(n-1)·K`), but only
   because that coset's isotropy representation is reducible into
   genuinely distinct summands (`C^{2n-2}⊗C^2 ⊕ S²(C²)`) — a precondition
   `S⁶=G₂/SU(3)`'s own irreducible isotropy explicitly fails, so the
   method does not transfer without first inventing new geometric content
   this project does not currently have (which is exactly (i')/(ii')'s
   own already-named high-AOG-5-risk territory, not a shortcut around it).

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| A. Paper contains an explicit su(3)-equivariant map / connection / curvature object valued in a representation genuinely independent of `m` (not just `Λ^k m` for some k), specifically for `S⁶=G₂/SU(3)` | Direct quote/section citation required |
| B. Paper's general method (e.g. §4.1.1-style coupling) is stated as applicable to ANY coset regardless of isotropy reducibility, including irreducible cases | Direct quote required — a general theorem, not this round's own extrapolation |
| C. Paper treats a second, independent SU(3)-structure coset (nearly-Kähler 6-manifold other than the round `S⁶`) with reducible isotropy that could serve as a structural analogy | Direct section citation required |

If A, B, and C all FAIL → verdict is `NO-RELEVANT-CONTENT` (paper's own
scope, for this specific coset, does not supply what OB14 needs) — kills
the hope that this specific cheap literature check closes OB14's honest
scope gap (C164 Section 9 Concern 4) with a positive result; the gap
becomes **closed as "checked, found empty"** rather than remaining an
open, unactioned item.

If ANY of A/B/C PASS → does NOT automatically resolve OB14 (a candidate
would still need to be built and skeptic-reviewed per C162's own
branching-count-first discipline), but reopens (i')/(ii') with a concrete,
citable, external starting point — worth a follow-up round.

If FAIL on all three → kills: the specific hope (named in C164 Section 9
Concern 4) that AHL2023 itself, unread for this question until now, was
quietly sitting on the missing coupling-data construction. Does NOT kill
OB14's own BLOCKED-INTERNAL / BLOCKED-EXTERNAL-OR-THEORETICAL status,
which was never conditioned on this specific check succeeding.

---

## Checks planned

- T1: Read AHL2023 §5.1 (S⁶=G₂/SU(3)) directly from LaTeX source — check
  isotropy representation reducibility and every constructed object's
  representation type.
- T2: Read AHL2023 §2.3-2.4 (Nomizu map / torsion class formalism) —
  check whether the GENERAL machinery (not specific to one coset) could
  supply cross-bundle coupling data independent of isotropy reducibility.
- T3 (adversarial/edge case): Read AHL2023 §4.1.1 (a coset with genuinely
  reducible isotropy, quaternionic spheres) specifically to find a
  counter-example to sub-claim 1 — i.e., actively look for the pattern
  OB14 needs, to confirm it exists in the paper SOMEWHERE (ruling out
  "the paper never does this kind of thing at all") before concluding it
  is absent specifically for `S⁶=G₂/SU(3)`.

---

## What this does NOT mean

1. Does NOT establish that no such construction could ever exist for
   `S⁶=G₂/SU(3)` in principle — only that AHL2023, as published, does not
   supply one, because its own stated isotropy representation for this
   coset is irreducible.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`,
   `safe_for_runtime=False`, or any prior round's certified result
   (round59, C139-C165 all untouched).
3. Does NOT close OB14 itself — OB14 remains `BLOCKED-INTERNAL` /
   `BLOCKED-EXTERNAL-OR-THEORETICAL` regardless of this round's verdict;
   this round only closes one specific, previously-unactioned scope gap
   (C164 Section 9 Concern 4) about whether AHL2023 was quietly relevant.
4. Does NOT violate the "DO NOT INITIATE CONTACT [with Tom Lawrence]"
   constraint — reading an already-published, already-cited paper is not
   contact with its author.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

[Filled in decision.md]

**Evidence:** [VERIFIED-primary-source: arXiv:2203.02961v3 LaTeX, sections
2.3, 2.4, 4.1.1, 5.1, fetched this round via `mcp__arxiv__get_paper_latex_section`]

**Status:** [see decision.md]
