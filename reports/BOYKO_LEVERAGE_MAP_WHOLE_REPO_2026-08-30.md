# Boyko Leverage Map — N-7-GeoSpectra-Lab (whole repo, all tracks)

**Date:** 2026-08-30
**Skill:** `boyko-leverage-map` (Meadows-style systemic analysis)
**Object:** The whole repository as a working system — not a single hypothesis, not one experiment.

---

## Step 0 — Object and boundaries

**System:** the N-7-GeoSpectra-Lab git repository as a knowledge-production process — the
combination of (a) the research content (Track A numerical, Track B algebraic, Track C
frozen), (b) the methodology scaffolding that produces and records it (FL/EstimandOps/
Perelman-audit rules, `.claude/memory/`, per-experiment folders, git branch-per-round
convention), and (c) the registries that are supposed to let a new reader reconstruct
current state without re-reading everything.

**What I have direct, verifiable access to:** the full git history (1126 commits, 290
local branches), the full working tree as of 2026-08-30, file sizes/mtimes, and the
content of the key registry files. I do **not** have access to token/cost logs, to
wall-clock time actually spent per round, or to the user's own felt experience of
friction — those are marked `[HYPOTHESIS]` below where relevant, not `[VERIFIED]`.

**Period:** full history back to the first commit (`79f8f1c`, v0.1.16 era) through
2026-08-30, with emphasis on the last 30 days (2026-07-31 → 2026-08-30) as "current
system behavior."

---

## Step 1 — System map

```
Track A (cc_toy_lab/, scripts/, tests/)     Track B (tom_s3_spinor_toy/)        Track C (paper/, frozen)
  numerical harness, S²/S¹/S³ toy geoms       algebraic, S³ spinor / N_gen=3      spectral-recoverability
  Verdict: DISCRETIZATION_SENSITIVE            314 experiment folders               null result, frozen 2026-06-30
  Entry: reports/GATE4B_SPECIFICITY_...md      303 decision.md files
  Last commit touching it: 2026-07-16          Last commit: 2026-08-30 (today)
                                                290 local branches (101 unmerged)
        │                                              │
        └──────────────┬───────────────────────────────┘
                        ▼
          21 top-level status/registry files in tom_s3_spinor_toy/ root:
          README.md, RESEARCH_STATUS_REPORT.md, CURRENT_STATE_ROUND111.md,
          OPEN_BLOCKERS.md (104KB), CLAIM_LEDGER.yaml (2432 lines / 394KB),
          ALIVE_BRANCHES.md, GLOBAL_RECOMPOSITION_AUDIT.md, DERIVATION_GRAPH.yaml,
          PARENT_ACTION_GATE.md, SUPERSEDED_RESULTS.md, THEOREM_PACK.md, ...
                        │
                        ▼
          .claude/memory/activeContext.md (tom_s3_spinor_toy) — 332,423 bytes,
          6,988 lines, spans 2026-06-17 → 2026-08-30, read by every subagent
          per context-loading.md's "Step 1 — Read activeContext" protocol
                        │
                        ▼
          Global rule stack (~/.claude/rules/): FL Full-Ladder, EstimandOps,
          Perelman audit, memory-protocol (mandates ≤200 lines for this exact
          file), audit-verification-gate, skeptic triggers — all imported,
          none of them enforced by a hook for THIS specific file's size.
```

Track A and Track C are essentially closed/dormant. Track B is the entire live system
right now, iterating at roughly one experiment round (branch → commits → merge) every
few hours during active periods (16 rounds, C96→C111, in 4 days: Aug 26–30).

---

## Step 2 — Main patterns

### Pattern 1 — Registries grow without a matching prune/archive step (write ritual, no archive ritual)

**Pattern:** every experiment round is required (by FL/Perelman/memory-protocol) to
write to several persistent artifacts — `claim.md`, `decision.md`,
`.claude/memory/activeContext.md`, `CLAIM_LEDGER.yaml`, and often `OPEN_BLOCKERS.md` —
but none of these files has an enforced size ceiling or an automatic compaction step.
This is not a one-off — it recurs identically across four independent files:

| File | Designed/prescribed scope | Actual state (2026-08-30) | Evidence |
|---|---|---|---|
| `tom_s3_spinor_toy/.claude/memory/activeContext.md` | `~/.claude/rules/memory-protocol.md`: "kept ≤200 lines by protocol" | **6,988 lines / 332,423 bytes** | `[VERIFIED]` `wc -l` |
| `CLAIM_LEDGER.yaml` | Own header: "~15-20 LOAD-BEARING claims only — NOT exhaustive" (MASTER_TZ Phase 0 spec) | **103+ entries** as of 2026-08-12, self-flagged in the file's own comment as "no longer the tightly-curated... set the original design intended," explicitly "flagged, not re-scoped" | `[VERIFIED]` — read directly from the file's own header comment |
| `OPEN_BLOCKERS.md` | Implicit: a list of *open* blockers | 104,018 bytes; only 13 `## OB` section headers but 15 occurrences of CLOSED/RESOLVED — closed items are never removed | `[VERIFIED]` `grep -c` |
| `CURRENT_STATE_ROUND111.md` | A dated snapshot | Last touched 2026-07-18 (43 days stale relative to 2026-08-30) but still actively cross-referenced by 6 other live files (`OPEN_BLOCKERS.md`, `RESEARCH_STATUS_REPORT.md`, `PARENT_ACTION_GATE.md`, `SPIN13_TO_SPIN4_DECOMPOSITION.md`, two experiment folders) | `[VERIFIED]` `grep -rl` |

**Mechanism:** the FL/Perelman/memory-protocol stack enforces the *write* side hard
(hooks like `reject_gate_guard.py`, `null_retroscan.py`, `promotion_gate_guard.py` all
check that something got written) but has no symmetric hook checking that something old
got compacted or archived. `research-methodology.md`'s own gap list (gap #1, closed
2026-06-24) shows the project *has* successfully closed exactly this kind of
write/verify asymmetry before (NULL-retroscan) — it just hasn't been applied to file
*size*, only to file *content correctness*.

**Alternative explanation considered:** this could simply be "a research project
accumulates state, that's normal and even desirable for audit trails" — and for git
history / `null_results/` / `parked/` (which are explicitly designed as permanent,
append-only archives per `falsification-ladder.md`) that is the correct and intended
behavior, not a bug. The distinguishing fact that makes `activeContext.md` and
`CLAIM_LEDGER.yaml` different is that both carry an *explicit, self-stated* target size
that the project itself set and then blew past — this isn't "accumulation is bad," it's
"the project's own stated ceiling for the file that's supposed to be cheap-to-read is
being violated by ~35x (line count) with no corrective step observed in the last 2.5
months of the file's life."

**Consequences:** every subagent invocation that follows `context-loading.md`'s Step 1
("Read activeContext.md: ~30-50 tokens") is instead reading on the order of
80,000-100,000+ tokens from this one file, silently, every time. Given the round
velocity in Track B (multiple rounds per day during active stretches), this cost
compounds every single round.

### Pattern 2 — Track A is fully dormant, but the repo's own entry points still present it as an equal, ongoing partner track

**Pattern:** 0 commits touched `cc_toy_lab/`, `scripts/`, or `tests/` in the last 30
days; last touch was 2026-07-16, i.e. 45 days ago as of 2026-08-30. `[VERIFIED]`
(`git log --since --oneline -- cc_toy_lab scripts tests` = 0). Meanwhile 107 of 207
commits in the same 30-day window touch `tom_s3_spinor_toy/`. `[VERIFIED]`

**Mechanism, and the important correction:** I initially read this as neglect. It is
not — `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md` (Track A's designated entry
point per the root `CLAUDE.md` table) states its own status as **"✅ FINAL"** twice in
the document. `[VERIFIED]` `grep`. Track A reached a terminal verdict
(`DISCRETIZATION_SENSITIVE`) and correctly stopped. This is the alternative
explanation required by HARD RULE 4, and it wins: the dormancy itself is healthy, not
a pattern to fix.

**What *is* still a real (smaller) finding:** the root `CLAUDE.md` and `README.md`
present the two tracks side-by-side with no visual distinction between "closed,
terminal verdict reached" and "actively iterating, daily commits" — a reader (human or
agent) landing on the repo root sees a parity table, not a status signal. This is the
same *pointer-staleness* pattern as `CURRENT_STATE_ROUND111.md` above (Pattern 1), just
applied to the top-level navigation instead of a mid-tree registry — one mechanism,
two instantiations.

### Pattern 3 — Branch-per-round convention with no cleanup ritual

**Pattern:** 290 local branches exist; 101 (35%) are unmerged into `main`.
`[VERIFIED]` `git branch --no-merged main | wc -l`. Sampling 10 unmerged branches
shows ages spanning 2026-05-25 to 2026-08-10 — some are 3+ months old. `[VERIFIED]`
The branch-per-experiment-round convention (`c96-...`, `c97-...`, one branch per
`experiments/YYYYMMDD-*` folder) tracks closely with the 314 experiment folders: this
is a deliberate, working convention (it gives each round an isolated, reviewable diff,
consistent with the Builder Blindness / worktree-isolation practices named in
`falsification-ladder.md`), but nothing in the observed history merges-and-deletes or
explicitly archives a branch once its round is folded into `main`.

**Alternative explanation:** kept branches could be intentional — a permanent audit
trail of every round's raw diff, parallel to `null_results/`. This is plausible and I
cannot rule it out from git alone `[HYPOTHESIS]` — but 101 branches is a heavy local
namespace to search through, and unlike `null_results/INDEX.md` (which has a curated,
readable index), there is no index of what each of the 101 unmerged branches *is* or
*why it's still open* — so even if the retention is intentional, it currently isn't
navigable.

### Pattern 4 — The heaviest parts of the FL methodology (skeptic Step 8a) are invoked far less often than the rules mandate

**Pattern:** only 20 of 303 `decision.md` files (6.6%) contain skeptic-verdict language
(`skeptic_verdict`, "Skeptic Concerns", `CONFIRMED-REAL`, `FALSIFIED`).
`[VERIFIED]` `grep -rl`. `falsification-ladder.md` Step 8a states skeptic review is
"MANDATORY" before any PROMOTE on a Full-Ladder experiment. Meanwhile, the recent
`activeContext.md` tail (last ~2 weeks) mentions "self-caught"/"self-correct" 18 times
and any form of "skeptic" 31 times total across the whole 2.5-month file — errors are
overwhelmingly caught by the same session re-checking its own work, not by an
independent-context skeptic call. `[VERIFIED]` `grep -c`

**Mechanism / honest read:** `research-methodology.md`'s own arbitration rule (stage
of research → which contour dominates) explicitly licenses lighter skepticism during
"idea scouting" / early hypothesis-shaping stages, and the C-series rounds read exactly
like fast divergent-contour scouting (many small, cheap, falsifiable numerical checks,
several explicitly reversed mid-round by the *same* session before being written down).
So this is not automatically a violation — it may be the correctly-calibrated stage
behavior the project's own rules describe. What's missing is a periodic check of
whether items are crossing from "scouting" into "promotion" (PROMOTE language does
appear in `decision.md` files) *without* picking up the mandatory skeptic step at that
transition — I did not verify this transition-boundary question directly; it would
need per-file inspection beyond this pass's budget. `[HYPOTHESIS]`, flagged as the
most actionable "critical unknown" in Step 9.

### Pattern 5 (supporting, not separately scored) — Only one CI workflow exists

`.github/workflows/` contains a single file, `lambda-identity-audit.yml`.
`[VERIFIED]` `ls`. For a codebase producing 300+ experiment rounds with dozens of
`test_*.py` files (Track A alone has 25+ visible in `tests/`), there is no general
"run pytest on push" gate. This is consistent with, and reinforces, Pattern 1's
underlying mechanism: enforcement infrastructure (hooks, CI) exists for specific named
risks (lambda identity, reject-gate, null-retroscan) but is not applied uniformly to
the two boring, structural risks found here — file-size hygiene and general test
regression.

---

## Step 3 — Feedback loops

**Loop A (reinforcing, unopposed) — "write-only registry growth":**
new round → new `claim.md`/`decision.md` → new `activeContext.md` entry (prepended) →
next round's agent reads a slightly bigger file at Step 1 of context-loading →
slightly more token budget consumed just to "catch up" → no corresponding pressure to
compact, because nothing measures or gates file size → next round repeats the cycle.
This loop has **no natural ceiling** currently: `research-methodology.md`'s "Context
Overflow (70% threshold)" rule governs a *session's* live context, not this *file's*
disk size, so it doesn't intervene here. The one observed correction — the
`boyko-project-radar` "Chain 3: fix stale status pointers" commit on 2026-08-26 — fixed
*dangling pointers*, not *file size*: `activeContext.md` and `CLAIM_LEDGER.yaml` both
grew further in the 4 days after that fix, through 2026-08-30. That is direct evidence
the loop is currently reinforcing, not balancing.

**Loop B (reinforcing) — "velocity begets more velocity in the same track":**
Track B's round-to-round structure is explicitly generative — each round's pearl,
open blocker, or NULL result seeds the next round's claim (`C109 diagnoses C108`,
`C110 tests C109's pearl`, `C111 follows C110's pearl`). This is a healthy scientific
loop *within* Track B, but it has no counterpart that ever routes attention back to a
different track — there is no "if track X has been silent for N days AND its own
verdict doc isn't marked FINAL, resurface it" rule. In Track A's case this doesn't
matter (verdict is FINAL — Pattern 2), but the *loop structure itself* would produce
the same silent-drift outcome for any future second track that is genuinely paused,
not concluded — there's no balancing mechanism, only a lucky outcome this time.

**Loop C (attempted balancing, currently periodic/manual, not continuous) —
`boyko-project-radar` self-audits:** the repo has already invoked a broader project
radar skill at least twice recently (visible in `git log`: "boyko-project-radar Chain
1/2/3" commits, 2026-08-26) that fixed test coverage gaps, stale pointers, and added
new experiment chains. This is a genuine balancing mechanism, but it fires on manual
invocation, not on a schedule or a size/staleness trigger — so its effect decays
between invocations, exactly as seen with the 4-day regrowth above.

---

## Step 4 — Leverage points (Meadows scale, highest to lowest)

1. **[HIGH — rule of the system]** Add an enforced size/age ceiling on
   `tom_s3_spinor_toy/.claude/memory/activeContext.md`, mirroring the pattern the
   project already used successfully for `reject_gate_guard.py` /
   `null_retroscan.py`: a hook (or a session-start check) that, once the file exceeds
   e.g. 200-400 lines, forces a rollup of everything older than the last N rounds into
   a dated archive file (`activeContext_archive_2026-Q3.md`) and truncates the live
   file back toward the rule's own already-stated 200-line target. **Why this is the
   top lever:** the rule already exists in prose (`memory-protocol.md`); this closes an
   enforcement gap, not a design gap — it is the cheapest possible fix (one hook,
   modeled on two hooks that already exist in this exact stack) for the single
   biggest, most frequently-triggered cost identified in this whole pass (every
   subagent invocation, many times a day).

2. **[HIGH — rule of the system, same mechanism]** Apply the identical archive/ceiling
   discipline to `CLAIM_LEDGER.yaml` (already self-diagnosed by its own header as
   having drifted from ~15-20 to 103+ entries) and `OPEN_BLOCKERS.md` (retains closed
   items indefinitely). Since the project's own header comment for `CLAIM_LEDGER.yaml`
   already names this exact problem and defers it ("deliberately left for a dedicated
   pass with explicit criteria, not done casually"), this is not a new finding — it is
   a nudge that the deferred pass is now overdue, with a second, independently-grown
   instance (`activeContext.md`) as fresh supporting evidence that the deferral cost is
   compounding, not staying flat.

3. **[MEDIUM — information flow]** Collapse the 21-file top-level registry set in
   `tom_s3_spinor_toy/` into one explicit hierarchy: exactly one file marked
   authoritative-current (`RESEARCH_STATUS_REPORT.md` is the closest existing
   candidate — README.md already points to it as "Full narrative"), with every other
   status-shaped file (`CURRENT_STATE_ROUND111.md`, `GLOBAL_RECOMPOSITION_AUDIT.md`,
   etc.) either merged in or explicitly re-labeled `HISTORICAL/SUPERSEDED` in its own
   filename or header the moment it stops being live — not left to be discovered stale
   by a later `grep`. Cheaper than #1/#2 to design, but touches more files to execute.

4. **[MEDIUM — goal-visibility]** Make the root `CLAUDE.md`/`README.md` track-status
   table show verdict state, not just directory mapping — e.g. append `[FINAL,
   2026-07-16]` / `[ACTIVE, daily]` / `[FROZEN, 2026-06-30]` next to each track so a
   fresh reader (human or agent) doesn't have to open `reports/GATE4B_...md` to learn
   Track A is done. One-line change, removes the one real (if minor) part of Pattern 2.

5. **[LOW — parameter]** The literal "≤200 lines" number, the specific CI workflow to
   add, the exact branch-pruning cadence — all real, all cheap once #1-#4 are decided,
   none of them change the system's behavior on their own without the enforcement
   mechanism above them.

---

## Step 5 — Asymmetries

- **Information asymmetry (enforcement vs. narration):** a `PostToolUse` hook, per this
  project's own `~/.claude/rules/integrity.md` note on `submission_gate_guard.py`, "can
  only inject context into the conversation — it cannot block a tool call." The
  project's memory-protocol rule for `activeContext.md`'s size is currently *pure
  narration* (a number in a markdown file) with no hook at all behind it — a strictly
  weaker position than even the soft-nudge hooks that exist for other risks. `[VERIFIED]`
  by absence: no hook matching "activeContext" size-checking was found in the rule
  cross-references reviewed (only `activeContext_hygiene.py`'s narrower job — numeric
  claims without evidence markers — is named in `memory-protocol.md`, not file size).

- **Resource/attention asymmetry:** 100% of the last 30 days of research commits are
  Track B; this is currently *correct* (Track A is FINAL), but the mechanism producing
  it (Loop B, Step 3) has no track-agnostic safeguard — it happens to be safe now by
  luck of Track A's status, not by design.

- **Behavioral/incentive asymmetry:** every gate in this stack (`reject_gate_guard.py`,
  `promotion_gate_guard.py`, `null_retroscan.py`, `pre_commit_guard.py`) fires on
  *adding* something incorrectly, never on *failing to remove* something that should be
  pruned. The path of least resistance for an agent under round-velocity pressure is
  always to append, never to compact — confirmed structurally (no counter-example hook
  found) rather than merely inferred from one file's growth.

---

## Step 6 — Paradoxes and tensions

**Immutable audit trail vs. cheap-to-read live state.** The FL/Perelman stack wants
permanent, non-deleted provenance for every claim (this is *correct* and valuable —
it's what makes a REJECT verdict trustworthy months later). The memory-protocol's own
Checkpoint Fidelity criterion wants state reconstructable *without* reading the full
transcript. Both principles are right, and they are not actually in conflict once you
separate **cold storage** (git history, `null_results/`, `parked/`, dated archive
files — append-only, rarely read end-to-end, fine to grow forever) from **hot storage**
(`activeContext.md` — read at the start of every subagent call, must stay small). The
current failure is not "wanting both" — it's that `activeContext.md` is currently
serving as *both* cold and hot storage at once, because nothing routes its old content
into a cold tier. The switch variable: does this content need to be *read by every new
agent by default*, or only *found when specifically searched for*? Anything answering
"only when searched for" belongs in cold storage, immediately.

**Fast self-correcting velocity vs. mandatory independent skepticism.** Both are
legitimate depending on research stage (per `research-methodology.md`'s own arbitration
rule) — divergent/scouting stages should lean cheap-and-fast, convergent/promotion
stages should lean skeptic-heavy. The tension only becomes a real problem at the
boundary crossing, which this pass did not verify directly (see Step 9).

---

## Step 7 — What's established vs. inferred vs. hypothesis

**High confidence, tool-verified `[VERIFIED]`:**
- `activeContext.md` size (332,423 bytes / 6,988 lines) and its stated ≤200-line target
- `CLAIM_LEDGER.yaml`'s self-documented drift from ~15-20 to 103+ entries
- Track A: 0 commits in 30 days, last touch 2026-07-16; Track B: 107/207 commits in
  same window
- Track A's own verdict document says "✅ FINAL" (twice)
- 290 local branches, 101 unmerged, sample ages back to 2026-05-25
- 20/303 (6.6%) `decision.md` files carry explicit skeptic-verdict language
- Single CI workflow file exists
- `CURRENT_STATE_ROUND111.md` stale since 2026-07-18 but still cross-referenced by 6
  live files

**Logical inference `[INFERRED]`, chain stated:**
- Every subagent invocation pays an outsized token cost reading `activeContext.md` →
  inferred from context-loading.md's own stated budget (~30-50 tokens) versus the
  file's actual size, not measured directly against real session logs (which I don't
  have access to).
- The write/no-prune asymmetry is structural, not accidental → inferred from the
  consistent recurrence across four independently-maintained files (Pattern 1's table)
  plus the absence of any counter-example hook enforcing pruning.

**Plausible but unverified `[HYPOTHESIS]`:**
- That skeptic invocation rate (6.6%) reflects a genuine gap at the scouting→promotion
  boundary rather than being fully explained by the scouting-stage exemption — I did
  not check whether any of the 20 skeptic-carrying files correspond to a
  disproportionately small or large share of the PROMOTE-labeled decisions specifically.
- That the 101 unmerged branches are unintentional clutter rather than a deliberate
  permanent-diff-trail choice — plausible given the lack of any branch index, but not
  confirmed by asking the project's own documentation, which is silent on this.

---

## Step 8 — When do these patterns stop holding?

- **Pattern 1 (registry growth)** stops being a problem the moment a hard size ceiling
  with automatic archival is added — that's the whole content of Leverage Point #1/#2.
  It would also stop mattering (without fixing it) if round velocity in Track B
  dropped sharply, since the loop's damage is proportional to reads-per-unit-time.
- **Pattern 2 (track imbalance)** stops applying entirely once the project either
  revives Track A with new data/methods, or removes the "two equal tracks" framing
  from `CLAUDE.md`/`README.md` in favor of an explicit "Track A closed, Track B active"
  framing (Leverage Point #4) — either resolves it.
- **Pattern 3 (branch sprawl)** would stop mattering if a branch index existed (turning
  clutter into a searchable, low-cost archive, same cold/hot distinction as Step 6) —
  the raw count of 290 branches is not itself the problem, the absence of any index
  into them is.
- **Pattern 4 (skeptic under-use)** would stop being concerning the moment a check
  confirms PROMOTE-labeled decisions specifically DO carry skeptic verdicts near 100%
  of the time (i.e., the 6.6% figure is fully explained by the scouting/promotion
  split) — this is exactly Step 9's flagged critical unknown.

---

## Step 9 — Map of unknowns

**Known unknowns** (we know we don't know, no data yet):
- Actual per-round token/cost spent reading `activeContext.md` in real sessions (only
  file size is measured here, not consumption).
- Whether the 101 unmerged branches are deliberately retained or simply forgotten.
- Whether Track C (`paper/`, frozen 2026-06-30) has any live cross-references that have
  gone stale the same way `CURRENT_STATE_ROUND111.md` has — not checked in this pass.

**Hidden unknowns** (not currently tracked by anyone, harder to see):
- Whether the registry-growth pattern (Pattern 1) is already silently increasing
  session-compaction frequency (`research-methodology.md`'s 70%-context-overflow
  trigger) — nobody appears to be logging *why* a given session hit compaction, so a
  causal link to file size specifically would currently be invisible even if real.
- Whether any of the 21 top-level status files in `tom_s3_spinor_toy/` actively
  contradict each other on a specific claim's status right now (this pass sampled
  staleness/cross-referencing, not full pairwise content comparison across all 21).

**Critical unknowns** (would change the next concrete action if resolved — filtered by
the skill's own "would this change my next action?" test):
1. **Does the 6.6% skeptic-invocation rate hold near-100% specifically among
   PROMOTE-labeled decisions, or is it low even there?** — Cheap test: `grep -l
   "PROMOTE" experiments/*/decision.md` intersected with the skeptic-verdict grep
   already run above. If PROMOTE∩skeptic ≈ PROMOTE (full set), Pattern 4 downgrades
   to "correctly calibrated, no action needed." If it's still a small fraction, it
   becomes a genuine FL-compliance gap worth its own fix. **This changes whether
   Leverage Point work should include a "skeptic-before-PROMOTE" hook or not** — a
   real fork in next action, hence critical, not just interesting.
2. **Is anyone actually consuming `activeContext.md`'s 332KB per subagent call today,
   or has practice already drifted to "grep it instead of reading it whole"?** — Cheap
   test: ask the user directly, or check whether any recent subagent transcript
   available in this session shows a full-file read vs. a targeted grep of
   `activeContext.md`. If practice has already informally solved this (agents
   grep instead of reading), Leverage Point #1's urgency drops from "top lever" to
   "hygiene, do eventually" — **this changes whether #1 is worth doing first**, so it
   passes the critical-unknown test.

---

## Step 10 — Synthesis

### Counterintuitive conclusions

- **More rigor (more FL artifacts per round) is not proportionally more auditability.**
  Past a certain size, `activeContext.md` and `CLAIM_LEDGER.yaml` stop being
  *readable* audit trails and become archives that must themselves be searched rather
  than read — the FL discipline that produces them is working exactly as designed;
  it's the *retention* policy, not the *production* policy, that's missing.
- **Track A's silence is a success story, not a symptom** — it's easy to mistake
  "0 commits in 45 days" for neglect, and the correct read (verdict FINAL) only comes
  from actually opening the linked entry-point document, which most status dashboards
  (including this repo's own root table) don't surface without extra digging.

### What to check next (cheap, concrete)

1. Run the PROMOTE∩skeptic grep from Step 9 (critical unknown #1) — under 5 minutes,
   directly resolves whether Pattern 4 needs a fix or is already fine.
2. Ask directly whether `activeContext.md` is being read in full or grepped in
   practice (critical unknown #2) — directly resolves urgency of Leverage Point #1.
3. `git branch --no-merged main --format='%(refname:short) %(committerdate:short)'`
   piped to a sort-by-age, to turn Pattern 3 from "290 branches, vague clutter" into
   an actual prioritized cleanup or archival-index list.

### Top 3, ranked by practical significance (not interestingness)

1. **Enforce a size/age ceiling on `activeContext.md` (and, same mechanism, on
   `CLAIM_LEDGER.yaml`/`OPEN_BLOCKERS.md`) with automatic archival — a hook, not a
   prose reminder.** This is the single highest-ROI action identified: the rule
   already exists in writing, the enforcement pattern already exists in this exact
   codebase (`reject_gate_guard.py`, `null_retroscan.py`), the cost of the fix is one
   hook, and the cost of *not* fixing it compounds every single round at the project's
   current velocity (multiple rounds/day). Cheap to act on now.
2. **Collapse/label the 21-file registry sprawl in `tom_s3_spinor_toy/` around one
   explicit authoritative-current file**, with everything else marked historical the
   moment it goes stale (fixes `CURRENT_STATE_ROUND111.md`-style dangling pointers
   structurally, not just as a one-off cleanup commit). Moderate cost, best done right
   after #1 so the archived overflow from #1 has a clean home to land in.
3. **Make track status visible at the root entry points** (`[FINAL]` / `[ACTIVE]` /
   `[FROZEN]` tags in `CLAUDE.md`/`README.md`'s track table) — cheapest of the three,
   smallest in scope, but removes the one part of Pattern 2 that's a genuine (if minor)
   navigation gap rather than a false alarm.

**Single highest-ROI action for the repo as a whole:** build and wire the
`activeContext.md` archival hook (Leverage Point #1). It is the cheapest fix, it
targets the pattern with the most independent supporting instances (4 separate files
showing the identical write-without-prune shape), and — pending confirmation of
critical unknown #2 — it is very likely already imposing a real, compounding,
currently-unmeasured cost on every subagent call in the repo's most active track.
