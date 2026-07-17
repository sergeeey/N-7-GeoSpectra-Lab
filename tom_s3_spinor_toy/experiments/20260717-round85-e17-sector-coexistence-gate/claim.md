# E17 (round85) — Claim: does the physical construction require BOTH the
# `t=0` and `t=1` torsion-crossing sectors simultaneously, or does it need
# only one, to supply one generation's `SU(2)_L×SU(2)_R` content?

**Date:** 2026-07-17
**FL tier:** [x] Full (research claim, per project CLAUDE.md methodology
activation; this is the specific reconciliation question E12 Section E.2 and
E14 Section E left open, and that round84/KT-14's Convention Table explicitly
scoped E17 to attempt)
**Question type:** [x] descriptive [ ] predictive [ ] causal

## Estimand (L0/L1, descriptive)

**Population:** the two 2-dimensional complex kernels `ker(D^{t=0}_{S³})` and
`ker(D^{t=1}_{S³})` (right-invariant frame, established only under `c0=-2` per
`CONVENTION_TABLE.md` row 5), each already independently tool-verified as one
irreducible `SU(2)` weak-isospin doublet (E16/round83), considered TOGETHER
against `preprint.tex`'s own "one generation" bookkeeping.

**Intervention/comparator:** none — this is a pure classification/
reconciliation task against already-established project artifacts (E9, E10,
E11/round77's representation labels, E12's multiplicity count, E13's CPT
finding, E14's Z2-isometry exploration, E15's no-further-splitting result,
E16's doublet reading, the G6 32-state bookkeeping, KT-8's zero-mode gap, and
E11/round75's Freund-Rubin exploration). No new numerical computation is
introduced; this experiment cross-references already tool-verified facts and
draws one explicit logical consequence from combining them (whether the
representation content of the union is consistent with existing bookkeeping),
which is checked directly against cited file:line content, not asserted.

**Endpoint:** a three-way categorical verdict (PASS / FAIL / BLOCKED, exact
frozen definitions below) on whether the physical construction contains
exactly the necessary `t=0` and/or `t=1` sectors realizing the required
`SU(2)_L/R` doublets of one generation, without extra family copies or
double-counting against the existing "32 states = one generation + CPT
conjugates" convention (`preprint.tex:296-298`).

**Summary measure:** categorical (PASS/FAIL/BLOCKED), not continuous.

**ICE:** none — closed-form classification against a finite set of
already-established facts; no missing-data/dropout structure.

**MCID:** not applicable to a categorical verdict.

## Natural-language statement (written before re-deriving the verdict)

*We classify, descriptively, whether this project's own already-established
artifacts (E9–E16, the G6 bookkeeping, KT-8, and E11/round75's Freund-Rubin
exploration) jointly demonstrate that the `t=0` and `t=1` torsion-crossing
sectors are BOTH required and jointly consistent as parts of ONE physical
construction supplying exactly one generation's `SU(2)_L×SU(2)_R` content
(PASS); OR that using both would duplicate an already-counted physical
multiplet (FAIL); OR that this project's existing text — lacking any stated
parent 13D action — cannot decide whether `D^{t=0}` and `D^{t=1}` are parts of
one consistent theory or two logically separate, mutually exclusive
constructions (BLOCKED). We test BOTH `SU(2)_L`/`SU(2)_R` geometric labeling
conventions throughout, per round84/KT-14's explicit finding that this
labeling is genuinely unresolved from existing project text.*

## What this result does NOT mean (written before re-deriving the verdict)

1. Will **not** establish H1c (a physical mechanism selecting `t=0`, `t=1`,
   both, or neither) — that remains exactly as open as E7/E9/E10/E11/E14 left
   it, regardless of this experiment's outcome.
2. Will **not** resolve KT-8 (whether ANY zero mode of the full, untwisted 9D
   operator `D_full` exists) — untouched; this experiment's entire object of
   study (the torsion-deformed S³ escape route) is, per `preprint.tex:1467-1495`,
   already characterized in the paper's own text as "a candidate mechanism...
   physically unmotivated, not a resolution," independent of this
   experiment's verdict.
3. A PASS verdict, if reached, would **not** certify the torsion-escape-route
   program as physically selected or complete — it would only establish that
   IF both sectors are realized, their combined representation content is
   consistent (a necessary, not sufficient, condition); physical selection
   (H1c) and the missing parent action (KT-8's own blocking gap) remain
   separately open regardless.
4. A BLOCKED verdict, if reached, would **not** mean the project's physics is
   wrong — only that the specific question of whether `t=0` and `t=1` coexist
   in one construction requires an input (a stated 13D parent action) this
   project does not currently have, exactly as KT-8 already found for the
   more basic question of whether either sector supplies an actual physical
   zero mode at all.
5. Will **not** re-derive or challenge E9/E10/E11/E12/E13/E14/E15/E16's own
   already tool-verified results — reused here by citation; this experiment's
   only new contribution is the specific cross-sector coexistence question,
   not a re-verification of any prior computation.

## Pre-registered PASS / FAIL / BLOCKED criteria (frozen verbatim, per task instructions)

| Verdict | Condition |
|---|---|
| **PASS** | There is one consistent Hilbert space where `t=0` and `t=1` together give exactly the required left/right multiplets of ONE generation (no extra copies, no double-counting). |
| **FAIL** | Both sectors give independent copies of the same physical multiplets (real doubling), or one sector must be introduced by hand with no justification. |
| **BLOCKED** | This cannot be settled without a parent 13D action — determining whether the two operators (`D^{t=0}`, `D^{t=1}`) are parts of one consistent theory or two logically separate constructions is not decidable from what this project has established. |

## Method

1. Using BOTH `SU(2)_L`/`SU(2)_R` labeling conventions (per
   `CONVENTION_TABLE.md` row 6's mandate — do not assume one), state what
   `ker D^{t=0}` and `ker D^{t=1}` transform as under each, reusing
   round77/E16's already tool-verified `T₃` eigenvalues without
   re-deriving them. Explicitly check the `c0=-2` requirement for `t=1`
   (`CONVENTION_TABLE.md` row 5) is not silently violated anywhere in this
   reasoning.
2. Search (not assume) this project's own text for any existing mechanism —
   flux quantization (E11/round75), a parent action (KT-8/KT-1), or the
   32-state bookkeeping (G6) — that would fix whether both sectors are
   simultaneously physically present.
3. Directly check the double-counting question against `preprint.tex`'s own
   "32 states = one generation + CPT conjugates" convention
   (`preprint.tex:296-298`) and G6's own S3-side state bookkeeping
   (`experiments/20260615-g6-s3xs6-spinor-content/g6_spinor_decomposition.py`).
4. Address whether E13/round79's CPT finding (B-L sign on the S6 factor,
   not the S3 factor) bears on, or is silent on, a possible charge-conjugation
   relationship between the `t=0` and `t=1` sectors specifically (a different
   axis from what E13 tested).
5. Reach one of PASS / FAIL / BLOCKED honestly, without forcing a resolution
   the cited evidence does not support.

## Kill criterion

If Step 2 finds an explicit, already-stated mechanism in `preprint.tex` or any
prior experiment's decision.md that DIRECTLY fixes (a) whether both `t=0` and
`t=1` sectors are simultaneously physically present, and (b) that this is
consistent (not double-counted) with the existing 32-state convention, this
would move the verdict to PASS. If Step 2 instead finds an explicit mechanism
that forces exactly one sector and rules out the other (e.g., an orbifold
projection, a reality condition, or a stated selection principle), with no
route to needing both, this would move the verdict toward FAIL ("one sector
introduced by hand" clause) or a narrower PASS (if the excluded sector is
positively shown unneeded, not merely absent). Absent either, BLOCKED is the
honest default per the pre-registered criterion.

## Assumptions (status)

| Assumption | Status |
|---|---|
| `D_full² = D_{S3,t}²⊗I + I⊗D_{S6,twisted}²` (exact decoupling) | [INFERRED, inherited from E2/E12's own unverified caveat] — not re-examined here |
| `t=1`'s right-invariant kernel exists only under `c0=-2` | [VERIFIED-tool, inherited from round76/CONVENTION_TABLE.md row 5] — reused, not re-derived; explicitly checked this is not silently violated |
| `SU(2)_L`=left-translation (Convention A) vs `SU(2)_L`=right-translation (Convention B) | [WEAK/AMBIGUOUS, per CONVENTION_TABLE.md row 6] — BOTH tested explicitly, per that row's own recommendation for E17 |
| E16's finding that a single-`t` doublet is irreducible (no further internal SU(2)-covariant splitting) | [VERIFIED-tool, inherited from E14/E15, not re-derived] |
| G6's 4-state S3-side bookkeeping (`T3L`,`T3R`,`chir_s3`) is the intended target the escape-route construction should match | [INFERRED] — this is the reading E12 Section E.2 itself flagged as unresolved, not an established equivalence |

## Check

This is a reconciliation/classification round against already-established
project artifacts, not a new numerical computation — there is no new script.
The "check" is: every citation in `decision.md` traces to a file:line that
exists and says what is claimed (spot-checked via direct `Read`/`Grep` during
this session, not merely trusted from prior decision.md summaries), and the
final verdict follows deductively, without gaps, from the pre-registered
criteria table above applied to those citations.
