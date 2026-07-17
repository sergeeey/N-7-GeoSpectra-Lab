# Round 84 — Decision

**Date:** 2026-07-17
**Verdict:** `PASS_5_OF_6_RECONCILED__1_CONFIRMED_AMBIGUOUS`
**Go/no-go:** `CONVENTION_TABLE.md` is promotable as the single reference for all
future rounds in this line of work (starting with E17). 5 of 6 topics are now
reconciled into one citable statement each (2 unconditionally FIXED, 1 FIXED with a
usage rule, 1 FIXED-with-an-explicit-caveat, 1 CONVENTION CHOICE with an explicit
conversion rule). The 6th (`SU(2)_L`/`SU(2)_R` physical/geometric identification)
is confirmed, after one final active search, to be genuinely unresolvable from
existing project text — reported honestly as AMBIGUOUS rather than picked
arbitrarily, per the task's explicit instruction. This determines how E17 must be
scoped (see "Recommendation for E17" below).

---

## What is now fixed

1. **S³ orientation** — implicitly fixed by universal reuse of the same concrete
   frame `{Z_i=i·σ_i}` in the same order across every experiment; never explicitly
   labeled "right-handed"/"left-handed" anywhere in the project, but this creates no
   internal inconsistency since nothing ever diverges from it. `CONVENTION_TABLE.md`
   row 1.
2. **Clifford algebra convention** — confirmed, by direct grep this round (not
   merely cited from a prior report), to be byte-identical (`Z_i=i·σ_i`,
   `{Z_i,Z_j}=-2δ_ij`) across all 8 scripts that define Clifford generators
   (E2, E9, E10, E11, E12, E14, E15, E16). Zero divergent instances found anywhere
   in the project. `CONVENTION_TABLE.md` row 3.
3. **Structure-constant sign gap (`c=+2` vs `c0=-2`)** — confirmed NOT to be an
   error: round76 Part 1 tool-verified these differ only in sign, serving two
   different roles (abstract physics calibration vs. concrete literal realization).
   This round adds the operational rule that was previously only implicit: use
   `c0=-2` for any computation requiring an actual concrete directional derivative
   / vector field; reserve `c=+2` for purely scalar/algebraic statements tied to the
   original Kostant-element calibration. `CONVENTION_TABLE.md` row 2.
4. **Spin lift `Ω_i(t)=-(tc/2)Z_i`** — confirmed as the single formula used
   throughout E9/E10/E11/E12; the c=+2-vs-c0=-2 ambiguity is confirmed to propagate
   directly into this formula's numeric outputs (round76 gives DIFFERENT parallel-
   spinor existence results depending on which value is substituted) — this is now
   explicitly flagged, governed by item 2's rule rather than left as a silent trap.
   `CONVENTION_TABLE.md` row 4.
5. **`t=0`/`t=1` ↔ left/right-invariant correspondence** — `t=0`'s correspondence to
   the left-invariant frame is FIXED unconditionally (holds for any sign of `c`).
   `t=1`'s correspondence to the right-invariant frame is real and tool-verified,
   but ONLY under `c0=-2` — this round states the single, caveat-carrying sentence
   to cite going forward (`CONVENTION_TABLE.md` row 5, "Definitive single-entry
   statement"), replacing the shorter, caveat-free version that had already caused
   one near-overcloak (round77 had to re-flag it after the fact).

## What remains genuinely open

**Item 6 — `SU(2)_L`/`SU(2)_R` physical (geometric) identification — CONFIRMED
AMBIGUOUS, not resolvable from existing project text.**

This round performed one final, explicit attempt at resolution, per the task's
instruction to make one last try using only what's already in the project's own
text, before declaring it unresolved:

- Re-grepped `preprint.tex` directly (not reusing round74/round77's cached counts)
  for `SU}(2)_L` (12 hits), `SU}(2)_R` (9 hits), and every geometric
  left/right-translation phrase ("left-invariant", "right-invariant", "left
  translation", "right translation", "acts on the left/right") — **0 hits** for
  all of the latter, confirming round74/round77's finding independently.
- Directly re-read the two passages most likely to carry a hidden anchor —
  `preprint.tex:273-287` (the `Iso(S³×S⁶)=SO(4)×SO(7)` construction itself) and
  `preprint.tex:884-912` (Lemma L5, the chirality-fixing lemma) — both state
  representation-content pairings (`SU(2)_L` doublet = left-handed content,
  `SU(2)_L` singlet = `ν_R`) but at no point specify which geometric translation
  direction on S³ generates the `SU(2)_L` factor.
- Confirmed the one candidate anchor round77 found (`preprint.tex:331-334`+Lemma
  L5) really is representation-content-level only, and that adopting it as a
  geometric anchor would require importing an EXTRA, unstated convention (`SU(2)_L`
  = left-translation) that flips every downstream label if wrong, with nothing in
  this project able to distinguish the two possibilities (round77
  `decision.md:122-129`, reconfirmed round83 `decision.md:271-275`).

**This is a genuine ambiguity, not a gap in this round's search.** Three
independent reasons block resolution simultaneously (stated in full in
`CONVENTION_TABLE.md` row 6): the geometric labeling convention is imported, not
derived; the one spinor for which the "match" was checked (`ψ⁽¹⁾`, the `t=1`
candidate) does not currently exist under this project's own `c=+2` calibration;
and no physical principle requires the S³-factor zero mode to match S⁶'s label at
all — compounded by KT-8's independent finding that no zero mode of the full
untwisted 9D operator exists at present regardless.

## Recommendation for E17

Given item 6 stays unresolved, **E17 (sector-coexistence gate, comparing `t=0` and
`t=1` kernels against required `SU(2)_L`/`SU(2)_R` representation content) should
proceed as follows:**

1. **Do not assume either geometric labeling convention as "the" answer.** Test
   BOTH: (a) `SU(2)_L`=left-translation, `SU(2)_R`=right-translation, and (b) the
   reverse. Report which convention was used for every stated result, and whether
   the sector-coexistence conclusion is convention-INDEPENDENT (holds either way —
   the strong, useful outcome) or convention-DEPENDENT (flips under (a) vs (b) —
   itself an informative finding, since it would show the physical conclusion
   secretly rests on an unstated bookkeeping choice).
2. **State explicitly which value of `c` is used wherever `Ω_i(t)` or any concrete
   spin-connection computation appears**, per `CONVENTION_TABLE.md` row 2's rule —
   default to `c0=-2` for any concrete/differentiated computation unless there is a
   specific, stated reason to use `c=+2` instead.
3. **Do not silently assume `t=1`'s right-invariant parallel spinor exists under
   this project's own `c=+2` calibration** — per row 5, it is currently known to
   exist ONLY under `c0=-2`. If E17's construction needs the `t=1` sector under
   `c=+2` specifically, that is an open sub-problem (constructing a new candidate
   spinor under that sign) that must be flagged, not assumed solved.
4. **Treat KT-8's blocking gap as a prior, structural caveat** that applies to the
   entire torsion-escape-route program, independent of whatever E17 finds about
   sector coexistence — cite it (`preprint.tex:1421-1495`) rather than re-deriving
   it, exactly as round77/round83 already do.
5. If E17's own results turn out to distinguish between conventions (a) and (b)
   above — e.g. only one of the two labelings gives an internally consistent
   physical picture — that itself may be the first real evidence toward resolving
   item 6, and should be reported explicitly as such (a possible route to closing
   this table's one open row, not merely a byproduct).

## Kill Analysis (per this project's Anti-Overfitting Gate)

- **What this result kills:** the possibility that the c=+2/c0=-2 gap or the
  t=0/t=1 correspondence were silently-inconsistent artifacts requiring a
  re-derivation — both are now confirmed to be legitimate, reconcilable
  conventions with clear usage rules, not errors. It also kills any temptation to
  silently pick ONE `SU(2)_L`/`SU(2)_R` geometric convention for E17 without
  flagging it — this round's search actively confirms no textual basis exists for
  picking one over the other.
- **What this result does NOT kill:** none of H1c, KT-8, or the E12/E13/E16
  multiplicity findings — all untouched, cited by reference only. It also does not
  kill the possibility that the `SU(2)_L`=left-translation convention IS in fact
  the physically correct one (round77's "clean pattern match" with S⁶'s
  independently-fixed left-handed label remains a real, if SPECULATIVE-ONLY, signal
  in its favor) — only that this project's own text cannot currently distinguish
  it from its mirror-image alternative.
- **What survives, confirmed stronger than before:** every one of the 5 reconciled
  conventions is now backed by an explicit, single-sentence citable statement
  (`CONVENTION_TABLE.md`) instead of requiring a fresh re-derivation from 3-5
  separate decision.md files each time a future round needs to cite it. This is a
  genuine reduction in future re-litigation cost, even though it resolves no new
  physics.

## Assumptions carried, unresolved

- Everything already flagged as open in round74/76/77/80/83 remains open: H1c
  (physical selection of `t`), KT-8 (full-operator zero-mode existence), and
  whether BOTH `t=0` and `t=1` sectors are simultaneously required for a complete
  generation (E12 Section E.2 / E14 Reading 3) — none of these is addressed by a
  reconciliation-only round, and E17 is exactly the round tasked with the last of
  these.
- This table's row 1 (S³ orientation) leaves an explicit label ungiven — flagged
  as low-priority (no current inconsistency), but noted so a future round does not
  need to reconstruct the `det(J)=-1` derivation from scratch if the label is ever
  needed.

## What this does NOT mean

1. Does **not** resolve H1c, KT-8, or any open physical-selection question in this
   project — untouched, exactly as before.
2. Does **not** certify the torsion-escape-route program as complete or physically
   selected — unaffected by a documentation round.
3. Does **not** claim the `SU(2)_L`=left-translation convention is wrong — only
   that it is unverifiable from existing project text, and its mirror image is
   exactly as consistent with everything checked so far.
4. Does **not** introduce any new physics computation, sign convention, or
   numerical result not already present somewhere in E2/E7/E9/E10/E11/E12/E14/E15/
   E16 or `preprint.tex` — every cell in `CONVENTION_TABLE.md` traces to an
   existing file:line, per this round's own kill condition 3 (`claim.md`).
5. Does **not** claim this is the project's own `E13` — see the naming note in
   `claim.md`'s header; the real `E13` is `round79-multiplicity-reconciliation-
   attempt`. This document should be cited as "the Round 84 convention table" or
   "KT-14," never "E13."

## Pearl-registry candidate

One transferable methodological insight, concrete enough to state as a
falsifiable lesson for future rounds: **whenever a project accumulates multiple
"the paper never states X explicitly" caveats scattered across several
experiments' decision.md files (as this project did with the abstract-c/concrete-c0
gap and the SU(2)_L/R geometric-labeling gap), the caveats do not resolve
themselves by accumulation — they need one dedicated reconciliation pass that
either (a) states a definitive usage rule if the ambiguity is benign (rows 1-5
here), or (b) confirms genuine unresolvability and states exactly what evidence
would close it (row 6 here).** Impact score ~3 (narrow, project-internal
methodological point; useful mainly if this project's torsion-connection line of
work continues to accumulate scattered caveats faster than it resolves them) — not
registered to the global `pearl_registry/INDEX.md`, fully captured in this
decision.md and claim.md, project-internal rather than cross-domain.

## Check (reproduces this decision)

This is a documentation/reconciliation round — there is no script to run. The
"check" is: (1) every row of `CONVENTION_TABLE.md` cites a file:line that exists
and says what the table claims it says (spot-checked during this session via
direct `Read`/`Grep`, not merely trusted from prior decision.md summaries); (2) the
`preprint.tex` grep counts stated in row 6 (`SU}(2)_L`: 12, `SU}(2)_R`: 9,
left/right-invariant-translation phrases: 0) are reproducible by
`grep -c "SU}(2)_L" preprint.tex`, `grep -c "SU}(2)_R" preprint.tex`, and
`grep -n "left-invariant\|right-invariant\|left translation\|right translation\|acts on the left\|acts on the right" preprint.tex`
(the last should return no matches / exit code 1).
