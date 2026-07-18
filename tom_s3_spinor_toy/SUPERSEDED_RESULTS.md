# Superseded Results Registry

**Purpose:** closes the methodology gap already flagged in this project's own
memory (`feedback-promote-staleness-gate-2026-07-17`): the null-retroscan
(`null_retroscan.py`) catches REJECT-later-revived, but not
**PROMOTE-later-superseded** — cases where the *conclusion* still holds but its
*proof route*, *status wording*, or *scope* has changed and old references no
longer point to the current, correct picture. Each entry names: what survives,
what changed, and where the stale version still lives (if anywhere) so it can
be fixed or cross-referenced.

This is a Phase 0 (Freeze) deliverable per MASTER_TZ_RDR22 Section 21. Not
exhaustive — entries limited to cases already identified this session.

---

## SR1 — G74A's proof route

**Conclusion (survives, unchanged):** `dim ker(D_{S6,twisted}) = 1` exactly.

**What changed:** G74A's own original derivation route was superseded by the
`dolan-casimir-g2su3` result + round59's own independent certification. The
NUMBER (dim ker=1) is still correct and still attributed to
`dolan-casimir-g2su3` + round59, not to G74A's original argument.

**Where the stale version might still live:** any file citing "G74A" as the
*sole* source for dim ker=1 without also citing round59/dolan-casimir-g2su3
should be treated as citing a superseded proof route, even though the number
it cites is correct. Not grep-audited across all files in this Phase 0 pass —
flagged in `OPEN_BLOCKERS.md` as a citation-consistency check still needed.

**Source:** memory record `feedback-promote-staleness-gate-2026-07-17.md`;
`reports/PROJECT_360_ROUND3_SYNTHESIS.md` E9-E17 chain section.

---

## SR2 — Y-formula / gate G97 status (round92 → round93/96)

**Conclusion (updated):** the mixed hypercharge formula question is fully
resolved: `K3≡T3R` (round93) and the mixed-Y anomaly conditions are fully
computable and show no forcing (round96, `FAIL`).

**What changed:** an earlier status (round92, "2 unreconciled hypercharge
formulas, BLOCKED") was stale by the time an external summary table (pasted by
the user, 2026-07-17) was fact-checked against the repo — the table's row 17
still described the round92 BLOCKED status, not round93/96's resolution. This
was caught and corrected during this session's own external-fact-check pass
(user instruction: "обнови строку 17 и честные оговорки в таблице").

**Where the stale version lived:** the externally-pasted summary table only
(not a repo file) — corrected in that table directly; no repo file needed
fixing since `RESEARCH_STATUS_REPORT.md` and `preprint.tex` already reflected
the round93/96-corrected status when checked.

**Source:** memory record `feedback-external-summary-factcheck-2026-07-17.md`.

---

## SR3 — Round99's "toy" curvature-norm vs round111's real scalar curvature

**Conclusion (narrowed, not reversed):** round99 computed a curvature-**norm**
toy quantity and hoped for a double well at `t=0,1`; round99's own skeptic
review already marked this `WEAKENED` (kinematic norm ≠ derived action term).
Round111 computed the actual `Scal(t)` (not a norm toy) and found it
single-humped, decomposing exactly as `Scal_LC - 6(2t-1)²` — this replaces
round99's vague hoped-for shape with a precise, well-motivated open question
(the real torsion-squared coefficient's sign), but does NOT itself settle
whether a genuine gravitational/spectral action has a double well.

**What changed:** round99 is not falsified by round111 — it is superseded as
the *right tool for the question*; round99's own honest scope (kinematic norm,
not an action term) already anticipated this. Anyone citing round99 as "the"
curvature computation for this question should be pointed to round111 instead.

**Source:** `tom_s3_spinor_toy/experiments/20260717-round99-toy-Vt-curvature-double-well/decision.md`;
`tom_s3_spinor_toy/experiments/20260717-round111-codex-item6-scalar-curvature-action/decision.md`.

---

## SR4 — Rounds 102/103/106's withdrawn first-draft claims

**Conclusion (never promoted, correctly caught pre-promotion):** three
first-draft claims this session generated were each caught by mandatory
skeptic review BEFORE being presented to the user as confident findings, and
each was narrowed/corrected in the same round's own `decision.md` (additive
correction, not silent rewrite):

- Round102: first draft "G97 imprecise via G2-holonomy substitution" —
  `FALSIFIED` (category error: G2-holonomy≠SO(7)-isometry, SU(4)≠SO(6) as
  groups) — corrected to `WEAKENED` with a narrower surviving question.
- Round103: first draft "coexistence trivially allowed via two multiplets"
  (chiral-gauge analogy) — `FALSIFIED` (t indexes the spin CONNECTION, a
  spectral-triple datum, not a gauge-representation choice) — genuinely
  unresolved, reported honestly as such.
- Round106: first draft claim about constant-spinor/eigenvalue relation
  under t/1-t — `WEAKENED` ("constant spinor" is frame-dependent; narrow
  form survives).

**Why this belongs in a superseded-results registry rather than
`null_results/`:** these are not REJECTed experiment branches — they are
same-round, same-session self-corrections that never reached PROMOTE status
in the first place. Recorded here so a reader of the raw session transcript
or `PROJECT_360_ROUND3_SYNTHESIS.md` doesn't mistake the first-draft framing
for the round's actual (corrected) conclusion.

**Source:** `reports/PROJECT_360_ROUND3_SYNTHESIS.md`, rounds 102/103/106
sections; each round's own `decision.md`.

---

## Standing pattern (not a single entry, but load-bearing for how to read the above)

Across rounds 96-111, mandatory context-asymmetric skeptic review corrected 9
of 12 rounds — almost always by narrowing an overreached PHYSICS conclusion
while leaving a correct, narrower MATH result intact (SR3, SR4 above are
instances of this). Two rounds (107, 108) saw the opposite: the claim survived
**strengthened** after correction. Treat any "first-draft"/pre-skeptic framing
found anywhere in the raw experiment logs as provisional by default — the
`decision.md`'s final verdict section, not the script's own printed headline,
is the authoritative statement.
