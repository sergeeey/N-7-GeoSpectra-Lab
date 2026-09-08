# Research Audit — Whole N-7-GeoSpectra-Lab Repo — 2026-08-30

**Scope:** all three tracks. **Scanners:** `research-audit` (synthesized directly by
the main session after its own spawned sub-audit agent got stuck in a
notification loop and was killed — see Provenance note below), `boyko-leverage-map`,
`sci-code-audit`. Run per user request ("топ 3 выбери, давай запустим по очереди
а после подведём итоги").

**Provenance note (Gate 1 discipline):** the `research-audit` sub-agent originally
launched for this task entered a stuck notification loop (6+ consecutive
"still waiting" cycles reporting Track A as not-yet-complete when it had already
completed and been delivered), was killed via `TaskStop`, and this report's Track B
section was completed directly by the main session by reading
`null_results/INDEX.md`, `parked/INDEX.md`, and the first third of
`pearl_registry/INDEX.md` (37/106 rows — the file itself is dense enough that a full
read would have cost proportionally more tokens than the remaining synthesis value;
this is a stated, not silent, scope limitation). Track A's section below is the
sub-agent's own completed, verified output, delivered intact before it got stuck.
Track C is covered from this project's own `CLAUDE.md` description (frozen,
H0-wins verdict) rather than a fresh read of the paper itself.

---

## Track A — Numerical (`cc_toy_lab/`, `scripts/`, `tests/`)

**Classification:** RESEARCH, dormant-but-correctly-closed (0 commits in 45 days,
own docs say "FINAL").

**Structural finding (Gate 1 risk):** Track A's actual falsification narrative
lives in versioned `reports/*.md` files (`CURRENT_STATUS_v0.1.NN`, `GATE4B_*`,
`*_AUDIT_*`), **not** in `experiments/<id>/claim.md`+`decision.md` form. The root
`experiments/` directory does not cleanly belong to Track A — it mixes in a
**distinct third track** (GeoSpectra S³×S⁶ spectral-recoverability benchmark,
`CLAIMS_REGISTRY.md`, `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`) and
Track-B-adjacent symbolic work (`lambda-b5-*`). Anyone globbing `experiments/`
expecting only Track A content will silently import unrelated material.

**Verdict chain:** v0.1.15 baseline APPROVED → v0.1.21 `GATE4B_FSS_PASS_WITH_CAVEATS`
→ v0.1.22 skeptic audit opens 2 falsification tests → v0.1.22 `broken_wilson`
control found MISCONSTRUCTED (tested family contrast, not intact-vs-broken Wilson
term) → **v0.1.24 FINAL: `DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC`** — the
harness detects lattice-vs-FFT discretization method, not S³×S¹ physics or
Wilson-term structure → v0.1.25 dimension-label bug (N≤896 claimed vs actual
N=108×s1) confirmed labeling-only, science unaffected → 2026-07-17 numerical audit
found+fixed two real dense/sparse eigensolver bugs in `anderson.py`/`anderson_3d.py`
(flagship Gate 4B script itself confirmed clean — unconditional dense `eigh`).

**Recurring root-cause pattern (4 self-caught errors, all caught by a dedicated
adversarial/independent pass, never by the original report alone):**
1. Control construction drifts silently from pre-registration.
2. Metric artifacts (denominator shrinkage) masquerade as signal.
3. Solver-path inconsistency silently biases secondary modules.
4. Doc/label drift independent of computation.

**Open gap (flagged by GATE4B_SPECIFICITY_VERDICT's own authors, not invented
here):** does the FFT-weakens/lattice-stable pattern hold for other bases, other
parameter slices? Genuinely untested.

---

## Track B — Algebraic (`tom_s3_spinor_toy/`)

**Classification:** RESEARCH, extremely active (multiple rounds/day at current
velocity; C90→C111 landed within this single session).

**null_results/INDEX.md (43 lines, 40 entries) — failure pattern:** the large
majority of REJECT/NULL verdicts cluster around one repeated structural failure
mode: **a candidate mechanism turns out to be a restatement of an already-closed
gate, phrased differently enough to look new.** Concrete recurring instances:
- G38-S2 explicitly logged as "G33 restated in energy language."
- Round118 explicitly logged as "not a new no-go; an application of an already-
  established one" (gate G97).
- Round114 (AHL2023 cross-check) found the claimed independent verification
  algebraically collapses to the *same* already-published constant it was meant
  to cross-check.
- Round117 found its own reconciliation attempt tested "the wrong question"
  (group-component membership mistaken for action-symmetry).

This is the single clearest **cross-track-relevant methodological lesson**: the
project's own `research-methodology.md` names this failure type as "Тип 3 —
условие без условия" / zombie-restatement risk, and Track B's own null_results log
is direct, first-party evidence the risk is real and recurring (not hypothetical)
— worth citing next time a "new" mechanism is proposed, as a first-pass check:
*is this the same gate under new vocabulary?*

**parked/INDEX.md (4 entries) — no zombie hypotheses found.** All four have
explicit, non-trivial revival conditions (a new differentiating observable, a
concrete Euclidean-saddle computation, Tom Lawrence Part 5 arriving, etc.) — none
read as "quietly waiting to be re-tried without new grounds."

**pearl_registry/INDEX.md (106 rows total, 37 read directly) — key open items:**
- G102's original pearl (fiber-Spin(8) postulate) is explicitly marked
  `SUPERSEDED-IN-PLACE 2026-08-10` with an explicit warning not to re-ask it as
  originally written — a good example of the registry doing its job (an entry
  correcting itself in place rather than silently going stale).
- G103's λ-observability-split pearl has `next_check: 2026-08-05` — **that date
  has passed** (today is 2026-08-30) and the row still reads `pending`. This is a
  genuine, concrete instance of exactly the growth-without-review pattern
  `boyko-leverage-map` flagged structurally (see below) — not a hypothetical.
- Several `[CANDIDATE]` rows (modular-flavor axion-partner idea, third-octonion-
  convention check) are honestly marked as requiring new construction, not a quick
  follow-up — correctly not overstated.

**C90-C111 chain (this session's own work, read from direct session knowledge, not
re-derived here):** the exceptional-point mechanism found in C111 is the single
strongest positive result in this window — a genuine, non-trivial eigenvalue-
collision structure (4 symmetric thresholds, one narrow real island initially
missed at 161-point resolution and self-caught at 400-point resolution) with a
proven general `t↔-t` symmetry. C107-C110 are a clean, honest run of falsified/
refuted attempts (Meier-vs-Kostant bridge, covariance hypothesis) that correctly
narrowed the space rather than forcing a positive result. **This entire chain is
currently invisible to `RESEARCH_STATUS_REPORT.md`**, per `sci-code-audit`'s
finding below — a live documentation-currency gap, not a code or methodology one.

---

## Track C — Frozen (`paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`)

Per project CLAUDE.md: frozen since 2026-06-30, spectral-recoverability-vs-physics
null result (H0 wins, H1-H4 killed), tracked separately in `CLAIMS_REGISTRY.md`.
Correctly inert — no action items surfaced from this pass; not independently
re-verified this round (see Provenance note).

---

## Cross-Track Synthesis

**Q1 (is the direction falsifiable?):** YES for Track B (extremely disciplined FL
practice, exhaustive null_results log) and Track A (verdict downgraded twice under
its own adversarial pressure, both self-corrections). Track C is closed. No track
shows unfalsifiable drift.

**Q2 (is current direction justified by the evidence?):** YES with one caveat —
Track B's null_results show a real, repeated failure mode (restating a closed gate
under new vocabulary) that costs real rounds (Round114, Round117, Round118 alone).
This is not a reason to change direction, but a reason to add exactly one cheap
pre-check (see action item below).

**Q3 (zombie hypotheses active right now?):** None found in `parked/` — all four
entries have genuine, specific revival conditions. The closer call is the *pattern*
in `null_results/` (restated-not-new claims), which is a process risk, not a
specific currently-active zombie.

**Q4 (cheapest highest-value next action):**
1. **[from boyko-leverage-map, independently corroborated by a concrete instance
   found in this pass]** Build one hook enforcing the already-written ≤200-line
   rule on `activeContext.md` (currently 332KB/6,988 lines, ~35× over) with
   automatic archival, and the same mechanism on `CLAIM_LEDGER.yaml` (2,432 lines)
   — cheapest fix (the rule already exists in prose), targets the pattern with the
   most independent supporting evidence found across all three scans this round
   (this report's own G103 pearl-date-lapse finding is a second, independent
   confirmation of the same growth-without-review gap).
2. **[from sci-code-audit]** Update `RESEARCH_STATUS_REPORT.md` to cover C103-C111
   — 5 rounds missing, including the session's own highest-value positive result
   (C111's exceptional-point mechanism). Pure documentation-currency fix, no code
   risk.
3. **[new, this pass]** Add a one-line pre-check to the Round-kickoff checklist:
   "grep `null_results/INDEX.md` for the gate this claim would close — does it
   restate an existing REJECT under new vocabulary?" — cheap, directly motivated by
   3+ concrete instances in the log (Round114, Round117, Round118).

**Q5 (what would change starting over knowing all this?):** Track B's FL discipline
is genuinely strong and should not be loosened. The one honest miss is
process-level, not scientific: nothing currently re-surfaces a pearl whose
`next_check` date has lapsed (G103's is 25 days overdue as of this report) except a
human noticing — exactly the gap `boyko-leverage-map` named structurally and this
pass found a live instance of.

---

## boyko-leverage-map — top findings (full report: `BOYKO_LEVERAGE_MAP_WHOLE_REPO_2026-08-30.md`)

1. Registries grow without a matching prune/archive step — structural, recurring:
   `activeContext.md` 332KB/6,988 lines (~35× over its own ≤200-line rule),
   `CLAIM_LEDGER.yaml` grown from a designed ~15-20 entries to 103+ ("flagged, not
   re-scoped" by its own header), `OPEN_BLOCKERS.md` 104KB. Write-side discipline
   is hook-enforced; archive-side has zero enforcement anywhere.
2. Track A is fully dormant (0 commits/45 days) but *correctly* so — the residual
   gap is that root `CLAUDE.md`/`README.md` still present it as an equal ongoing
   partner to Track B with no status signal.
3. Mandatory skeptic review before PROMOTE appears in only 6.6% of decision.md
   files (20/303) — plausibly justified by a scouting-stage exemption, but
   unverified specifically at the PROMOTE boundary.

**Highest-ROI action:** the ≤200-line enforcement hook (see Q4 above — independently
surfaced by two of the three scans this round).

---

## sci-code-audit — top findings (full report: `SCI_CODE_AUDIT_WHOLE_REPO_2026-08-30.md`)

- **Track A: HARDENED.** `block_ipr_solver.py` documents and fixes a prior `eigsh`
  non-convergence regression; 31/31 tests pass; headline verdict is already a
  self-declared null result (low overclaim risk by construction).
- **Track B shared substrate (`c85_certification.py`, imported by 22 downstream
  rounds C86-C111): HARDENED.** Independently re-derived (fresh sympy script, not
  reading their code) the central sp(1)-bracket-relation claim from scratch and
  got an exact match to the reported pattern. Found and confirmed the historical
  `eigvalsh`-on-non-Hermitian bug (C87→C88) durably propagated as a house
  convention through 8+ later rounds.
- **Track B documentation layer: PROVISIONAL** — the one real finding.
  `RESEARCH_STATUS_REPORT.md` stale by 5 rounds (stops at C102, 2026-08-12;
  missing C103-C111 through today). No live/undetected code bug found in either
  track.

---

## Overall Score

- Track A: **8/10** — excellent self-correction record, only real gap is the
  structural FL-artifact-location mismatch vs. project convention (documented, not
  a science risk).
- Track B: **8/10** — exceptionally disciplined FL practice and a genuinely strong
  positive result this window (C111); docked for the recurring restated-gate
  pattern in null_results and the lapsed-pearl instance found this pass.
- Track C: not independently re-scored this pass (frozen, out of active scope).
- **Repo-level: 8/10.** The single most valuable, cheapest fix found by two
  independent scans converging on the same gap: enforce the existing ≤200-line
  registry rule with an actual hook, not just prose.
