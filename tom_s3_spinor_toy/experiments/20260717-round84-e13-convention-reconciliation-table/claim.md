# Round 84 — Claim: convention reconciliation table for the S³ torsion-connection family

**Date:** 2026-07-17
**FL tier:** [x] Full (research-support / documentation task; methodology per project
CLAUDE.md — reconciliation of already-established facts, not a new derivation)
**Question type:** [x] descriptive [ ] predictive [ ] causal

> **Naming note:** this folder's slug carries the tag "e13" only because that was the
> label supplied in the task description that spawned this round. It is **not** the
> project's own `E13` — that label is already assigned to
> `experiments/20260717-round79-multiplicity-reconciliation-attempt/` (see its
> `decision.md:1`, "# E13 (round79) — Decision"). This round produces no new
> `E`-numbered physics result; it is a cross-reference document consumed by the next
> physics round in the chain, `E17` (sector-coexistence gate, per the task brief).
> To avoid clashing with the real E13, this document is cited elsewhere as **KT-14**
> or **"the Round 84 convention table"**, never as "E13."

---

## Prior Result Gate

1. Exact claim: does a single, internally-consistent reconciliation of this project's
   own already-established sign/orientation/labeling conventions (S³ orientation,
   structure-constant sign, Clifford convention, spin lift, t=0/t=1 ↔ left/right
   correspondence, `SU(2)_L`/`SU(2)_R` physical identification) exist, using only
   facts already tool-verified in E2/E7/E9/E10/E11/E12/E14/E15/E16 and `preprint.tex`
   — and if not, exactly what is missing?
2. `decision.md` grep across `experiments/20260717-round7*` and `round8*`: done —
   0 prior reconciliation attempt found; round76/round77/round80/round83 each
   independently *flagged* pieces of this problem (see "Context" in the task brief)
   but none *resolved* them into a single table.
3. `round*_claim.md` + scripts grep: done — same result, the c=+2/c0=-2 gap and the
   `SU(2)_L`-convention gap are each raised in exactly one place (round76 Part
   1/round77 §1) and never subsequently closed.
4. `null_results/` + `parked/` grep: done — 0 hits (this project's `null_results/`
   and `parked/` directories, checked at the `tom_s3_spinor_toy/` root, contain no
   convention-reconciliation entries).
5. `git log -S`/`-G` pickaxe: not run — out of scope for a same-day documentation
   task; the relevant prior-round decision.md files were read directly instead
   (stronger evidence than a pickaxe search for a same-session lineage).
6. Primary source re-read: `preprint.tex` re-grepped directly this round (not from
   memory) for `SU}(2)_L`, `SU}(2)_R`, "left-invariant", "right-invariant",
   "translation" — confirms round77/round83's counts exactly (12 and 9 occurrences
   of the representation-label macros, 0 occurrences of any geometric
   left/right-translation phrase). See CONVENTION_TABLE.md row 6.
7. **Status:** [x] NEW (no prior reconciliation artifact exists; individual pieces
   are OPEN in their originating decision.md files and are consumed, not re-derived,
   here).

---

## Estimand

**Population:** this project's own already-published/already-tool-verified
conventions governing the S³=SU(2) torsion-connection family (E2, E7, E9, E10, E11,
E12, E14, E15, E16) and `preprint.tex`'s stated isometry/gauge-group construction.

**Intervention:** none (no new computation is performed on any of items 1-5; item 6
performs one final, explicit attempt at resolution using only text already present
in `preprint.tex`, per the task's explicit instruction — this is a targeted
literature/grep exercise, not a new derivation).

**Comparator:** the scattered, per-experiment ad hoc statements of the same
conventions across round76, round77, round80, round83's decision.md files (the
status quo this table replaces).

**Endpoint:** for each of the 6 topics named in the task brief, one of three states:
`FIXED` (single, unambiguous convention, cite file:line), `CONVENTION CHOICE — both
valid` (two conventions coexist validly, a rule for which to use when is stated), or
`AMBIGUOUS — needs resolution` (genuinely unresolved from existing project text,
what would resolve it is stated explicitly).

**Summary measure:** count of the 6 topics landing in each of the three endpoint
categories, plus the full table itself (the actual deliverable).

**MCID:** not applicable in the usual numeric sense — the practical threshold is
"does E17 now have a single citable reference for each of these 6 conventions,
instead of needing to re-read 5+ separate decision.md files and re-derive the same
cross-references." Any reconciliation that achieves this for ≥5 of 6 topics is
useful; a table that leaves all 6 as vague or re-opens settled questions would not
meet the bar.

---

## Claim (falsifiable)

For 5 of the 6 topics in the task brief (orientation, structure-constant sign,
Clifford convention, spin lift, t=0/t=1 correspondence), this project's own existing
text (E2/E7/E9/E10/E11/E12/E14/E15/E16 + `preprint.tex`) already contains everything
needed to state a single, precise, non-contradictory convention (or an explicit,
statable rule for converting between two coexisting valid conventions) — the
reconciliation task is genuinely one of cross-referencing and stating clearly, not
resolving a real unknown. For the 6th topic (`SU(2)_L`/`SU(2)_R` physical
identification), the claim is the opposite: this project's own text does **not**
contain enough to fix the geometric left/right-translation identification, and this
is reported as a genuine, currently-unresolvable (from existing text)
ambiguity — not forced to a false resolution.

Supporting sub-claims:
1. `Z_i=i·σ_i`, `{Z_i,Z_j}=-2δ_ij` is used identically, without exception, in every
   one of E2/E9/E10/E11/E12/E14/E15/E16's own Clifford-generator functions
   (grep-verified this round, not merely cited from a prior report).
2. The abstract `c=+2` (physics-calibrated) and concrete `c0=-2` (literal Pauli
   commutator) are DIFFERENT, both-legitimate quantities serving different roles
   (scalar/algebraic bookkeeping vs. concrete directional-derivative computation),
   not an error — round76 Part 1 already tool-verified they differ only in sign, and
   this round states the operational rule for which one to use when.
3. `preprint.tex` contains zero occurrences of "left-invariant", "right-invariant",
   or any geometric translation-direction phrase (re-verified this round by direct
   grep) — so no textual anchor exists, in this project's own primary source, for
   the geometric half of the `SU(2)_L`=left-translation identification. The single
   candidate anchor (`preprint.tex:331-334`, `ν_R` = `SU(2)_L` singlet) fixes only
   the SM/Pati-Salam *representation-content* meaning of the label, not which
   physical S³ translation direction realizes it geometrically.

---

## Kill criterion (MANDATORY — fill BEFORE running)

Since this is a reconciliation/cross-referencing task rather than a new physics
computation, the "kill" condition is reframed as: what would show the claim above
is FALSE (i.e., that more than one of topics 1-5 is *also* genuinely unresolvable,
or that topic 6 is *actually* resolvable and this round simply failed to find the
anchor)?

| Kill condition | Threshold |
|---|---|
| Any of topics 1-5 turns out to have a genuine internal contradiction in existing project text (not just an unstated-but-derivable convention) | A second, incompatible statement of the SAME convention is found in a DIFFERENT experiment's decision.md/script, with no reconciling rule possible |
| Topic 6 turns out to be resolvable after all | A grep or direct read finds an explicit statement in `preprint.tex` (or an equally authoritative already-tool-verified experiment) fixing which of {left-translation, right-translation} on S³ is called `SU(2)_L`, geometrically — not merely which representation content the label carries |
| The table itself introduces a NEW convention not already established somewhere in the project | Any table cell whose "source" column cannot be traced to an existing file:line |

If FAIL on kill condition 1 → the affected topic is downgraded from FIXED/CONVENTION
CHOICE to AMBIGUOUS, with the contradiction stated explicitly.
If FAIL on kill condition 2 → topic 6 is upgraded to FIXED, citing the found anchor,
and E17 no longer needs the dual-labeling-convention approach recommended below.
If FAIL on kill condition 3 → that table row is removed; only reconciliation of
EXISTING conventions is in scope for this round (per the task's explicit
constraint).

If no topic can fail → the gate is not scientifically idle: 5/6 topics converging to
FIXED/CONVENTION-CHOICE while 1/6 stays genuinely AMBIGUOUS is itself the informative,
falsifiable structure of this claim (a table that came back either "all 6 fixed" or
"all 6 ambiguous" would itself be suspicious and would trigger re-verification, per
the project's skeptic-trigger discipline for suspiciously clean or suspiciously
uniform results).

---

## Checks planned

- T1: grep every `clifford_generators`/`pauli_matrices` definition across
  `experiments/20260717-round6[7-9]*`, `round7*`, `round8*` and confirm byte-identical
  convention (`Z_i=i·σ_i`, `{Z_i,Z_j}=-2δ_ij`) in all of them — done, see
  CONVENTION_TABLE.md row 3.
- T2: re-grep `preprint.tex` directly for `SU}(2)_L`, `SU}(2)_R`,
  "left-invariant"/"right-invariant"/"translation" — done, see CONVENTION_TABLE.md
  row 6 (12 / 9 / 0 occurrences respectively — matches round77/round83's own counts
  exactly, an independent reconfirmation, not merely a citation of their claim).
- T3 (adversarial): actively search for a DIFFERENT candidate anchor in
  `preprint.tex` beyond the one round77 already found (line 331-334) — checked
  `preprint.tex:273-287` (the `Iso(S³×S⁶)=SO(4)×SO(7)` passage itself) and
  `preprint.tex:884-912` (Lemma L5) for any left/right-translation language — none
  found; both passages state which SU(2) pairs with which representation content,
  never which geometric translation direction generates which factor.

---

## What this does NOT mean

1. Does NOT re-derive or challenge any of E2/E7/E9/E10/E11/E12/E14/E15/E16's own
   tool-verified results — this round only cross-references and states conventions
   already established there.
2. Does NOT resolve H1c (physical selection between t=0/t=1), KT-8 (existence of
   any zero mode of the full untwisted 9D operator), or E12/E13's multiplicity
   question beyond what round83/E16 already settled — those are independent open
   items, untouched here.
3. Does NOT claim topic 6's ambiguity is a defect in `preprint.tex` — the paper
   simply never needed to make this distinction for its own stated purposes (its
   `SU(2)_L`/`SU(2)_R` usage is entirely representation-content-level, e.g. electric
   charge formula, anomaly cancellation, `ν_R` identification — none of which
   requires knowing which S³ translation direction is which).
4. Does NOT prescribe a specific resolution for topic 6 — per the task's explicit
   instruction, an honest "still ambiguous, here is exactly what's missing" is the
   valid, correct outcome if that is what the evidence shows (see decision.md).

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False
- This document creates no new physics convention — every entry in
  CONVENTION_TABLE.md must trace to an existing file:line, per kill condition 3.

---

## Verdict

See `decision.md`. Summary: 5/6 topics reconciled (2 FIXED unconditionally, 2
FIXED-with-caveat, 1 CONVENTION CHOICE with an explicit conversion rule); 1/6
(`SU(2)_L`/`SU(2)_R` physical identification) confirmed genuinely AMBIGUOUS, not
resolvable from existing project text — recommendation for E17 stated in
`decision.md`.

**Evidence:** [VERIFIED-tool/grep] for all 6 rows (see CONVENTION_TABLE.md sources
column); no new sympy/numeric computation was needed or performed this round.

**Status:** CLOSED — `PASS_5_OF_6_RECONCILED__1_CONFIRMED_AMBIGUOUS`
