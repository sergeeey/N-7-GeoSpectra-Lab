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

## SR5 — Round96's three `t=1_alone` zeros, reread as one shared fact (round112)

**Conclusion (unchanged, re-explained):** round96's `t=1_alone` zeros for
`[SU(3)_c]²U(1)_Y`, `[U(1)_Y]³`, and `[grav]²U(1)_Y` are all still correctly
zero — nothing computational is retracted.

**What changed:** round112 (closing OB8) found, via mandatory skeptic
review, that all `t=1_alone` mixed-`U(1)_Y` anomaly zeros — round96's three
plus round112's own two (`[SU(2)_L]²U(1)_Y`, `[SU(2)_R]²U(1)_Y`) — trace to
a **single shared structural fact**: `Y=T3R+(B-L)/2` is identically zero at
`t=1` given round94's own `B-L=0`. Reading round96's three `t=1` zeros as
three independent confirmations (as the original framing implicitly
suggested) overstates the evidence; they are one fact, computed five times.

**Where the stale framing might still live:** any file or summary describing
round96's `t=1_alone` results as "three separate FAIL confirmations" rather
than "one shared structural zero, computed in three (now five) different
anomaly channels" is using the pre-round112 framing. `CLAIM_LEDGER.yaml`'s
`C10`/`C16` entries and `OPEN_BLOCKERS.md`'s OB8 entry already carry the
corrected framing as of this entry's date.

**Source:** `tom_s3_spinor_toy/experiments/20260717-round112-remaining-mixed-y-anomaly-channels/decision.md`.

---

## SR6 — This registry's own Phase 0 error: OB3 claimed something round94 already did

**What changed:** `OPEN_BLOCKERS.md`'s original OB3 entry (written during
this session's own Phase 0 pass, before round112) stated "no construction
of B-L directly on the twisted kernel exists." **This was false at the
time it was written** — round94 (E24), already committed to this repo
before Phase 0's registry files were created, constructs exactly that:
`BL_64=leibniz64(BmL)` on the 64-dim twisted `Σ⊗Σ` fibre, with the physical
kernel vector confirmed an exact eigenvector, `B-L=0`.

**Root cause:** OB3 was written from a recollection of an earlier
in-session `/multi-lens` exercise on this same question, without
re-verifying that recollection against round94's own `decision.md` at
write time — an `audit-verification-gate.md` lapse in the registry's own
construction (agent's own [MEMORY] treated as [VERIFIED] without a fresh
Read/Grep check).

**Caught by:** direct re-reading of round94's `decision.md` while
formalizing OB3 per the user's own recommended next step ("завершить OB3
как дешёвую формализацию") — the act of writing the formal canonical
statement surfaced the registry's own error.

**Fix:** `OPEN_BLOCKERS.md` OB3 and `CLAIM_LEDGER.yaml`'s `C9` caveat both
corrected in place (not silently rewritten — the original wrong text is
struck through / marked CORRECTED, not deleted). New file
`BL_TWISTED_KERNEL_CANONICAL_STATEMENT.md` supplies the accurate,
consolidated statement.

**Generalizable lesson:** a registry built to consolidate "what's already
known" is itself a claim that needs the same verification discipline as
any other — writing consolidation files from session memory without a
fresh grep/read pass against the underlying decision.md files can
introduce exactly the kind of error the registry exists to prevent.

**Source:** `tom_s3_spinor_toy/BL_TWISTED_KERNEL_CANONICAL_STATEMENT.md`;
`tom_s3_spinor_toy/experiments/20260717-round94-bl-twisted-kernel-eigenvalue/decision.md`.

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

---

## SR7 — Second Phase-0 registry omission: round80/E14 was missing entirely

**What changed:** while searching OB1 for a genuinely new candidate
mechanism (a `Z2` left-right isometry forcing `t=0,1` coexistence), found
that round80 (E14) — a substantial, already-completed, honest exploration
of EXACTLY this idea, done earlier in this same long session, before the
Phase 0 registry was written — was **entirely absent** from
`CLAIM_LEDGER.yaml`, `PARENT_ACTION_GATE.md`, and every other Phase 0
file. This is the SECOND such omission this session (see SR6, round94/OB3).

**Root cause (same as SR6):** Phase 0 was written from session memory of
"what's been tried" without a systematic grep/read pass over every
existing `experiments/` folder against the specific question each Phase 0
field addresses. Rounds done earlier in a long session, before the
registry itself was written, are exactly the ones most likely to be missed
this way.

**Fix:** added `CLAIM_LEDGER.yaml` `C18` and a `PARENT_ACTION_GATE.md` F4
entry, both citing round80/E14 directly.

**Generalizable lesson (sharpens SR6's, doesn't just repeat it):** the
risk isn't random — it specifically targets **substantial results
completed before the registry-writing pass itself**, which won't appear
in the registry-writer's own recent-session memory the way freshly-run
rounds do. **Before starting a NEW attempt at any open item (OB1-OB4),
grep `experiments/` for related keywords FIRST** (as was done here,
finding round80 before building a duplicate `Z2`-isometry round) — this
is now the third time in this session a grep-before-build step caught
something a memory-only check would have missed (see also OB6 item 8's
premise check, and OB3's own discovery).

**Source:** `tom_s3_spinor_toy/experiments/20260717-round80-z2-left-right-symmetry-search/decision.md`.

---

## SR8 — Round127's explicit-`S` search: provenance clarified, not
invalidated (2026-07-19, P1 hardening pass)

**Conclusion (survives, unchanged):** round127's `STRUCTURE_MISMATCH`
verdict for the naive (unaligned-generator) pairing — `Hom_ℂ(ℂ⊗8_v,Σ)=4`,
no invertible intertwiner found — is correct and **not** affected by the
reshape-order bug found in round128 (below). Round127's SEPARATE abstract-
isomorphism argument (`Hom(V,V)=6` on both `8_v` and `Σ` individually,
forcing the `1⊕1⊕3⊕3̄` decomposition via the End-dimension identity) is
also unaffected — it is a pure nullspace-rank computation, which is
basis/vec-convention-independent by construction.

**What was clarified (not "fixed", because nothing was wrong in round127's
own reported result):** round128 found that its OWN Sylvester-equation
code (`hom_space_nullspace`, copied unmodified from round127's
`e44_8v_vs_s6_spinor_isomorphism.py`) reconstructs candidate intertwiner
matrices via `S_flat.reshape(8, 8)` — row-major (C order) — when the
underlying Kronecker-product identity requires column-major (Fortran)
vectorization. This bug matters ONLY when an invertible element must be
*reconstructed and its determinant/residual checked* from a Hom space of
dimension ≥6ish (large enough that the ambiguity can flip a genuine
solution into a spurious non-solution or vice versa). **Round127's own
`results_round127.json` shows `hom_dim=4`, `isomorphism_found=false`,
`iso_residual=null`** — no candidate `S` was ever found or reconstructed
there, so the reshape convention was never load-bearing for round127's
actual reported conclusion. `best_det_found=4.96e-91` (genuinely no
invertible element in a 4-dimensional space, matching round128's own
pre-fix diagnostic on an equally-too-small Hom space) is consistent
regardless of reshape convention.

**Provenance rule for citation (this is the actual, actionable fix):**
round127 must never be cited as an **independent corroboration** of
round128's explicit intertwiner `S` — round127 never found or claimed
one. Round127's sole surviving, independent contribution to the `ℂ⊗8_v≅Σ`
claim is the abstract End-dimension argument; the explicit, machine-
precision-verified `S` is round128's alone. Any manuscript or summary
citing "round127 and round128 independently confirm the isomorphism" is
imprecise — write instead: "round127 establishes the abstract isomorphism
type (End-dimension argument); round128 constructs and verifies the
explicit intertwiner (a distinct, later step, not a second confirmation
of the same fact)."

**Where the imprecise version might still appear:** `paper/P1_FROZEN_
VERDICTS_TABLE.md` row 4 and `paper/P1_NOGO_MANUSCRIPT_OUTLINE.md`
Section 5 were checked during this same hardening pass and already state
the roles correctly (round127 = abstract argument only, round128 = the
explicit `S`) — flagged here so future citations elsewhere in the project
inherit the same discipline, not because those two files were found to
have the error.

**Source:** `tom_s3_spinor_toy/experiments/20260718-round127-8v-vs-s6-spinor-isomorphism/results_round127.json`;
`tom_s3_spinor_toy/experiments/20260718-round128-cartan-weyl-alignment/decision.md`
("Bug history", bug 2).
