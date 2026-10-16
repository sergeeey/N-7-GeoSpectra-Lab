# A1/A2/A3 Dependency & Blast-Radius Audit

**Date:** 2026-09-04
**Type:** AUDIT, not an FL experiment round. This file carries no `Cnnn` number,
requires no `claim.md`/`decision.md` pair, and registers no PROMOTE/REJECT/ARCHIVE
verdict. It is a read-and-report exercise over already-existing project artifacts —
tracing three "untested-assumption risk" labels back to primary sources, mapping
what depends on each, and ranking them by value-of-information. Nothing here is a
new finding about the physics; everything here is a finding about the project's
own bookkeeping and about which of three already-documented gaps is cheapest and
most consequential to close next.

**Origin:** an FL-style `/research-audit` full-project meta-audit ran as a
background agent during the C123-C137 session (2026-09-02/03). Its full report was
never read in full by the orchestrating session — only a compacted summary
survived, recorded as shorthand in `.claude/memory/activeContext.md` lines 93-96:
*"three untested-assumption risks with no experiment folder yet: A1 (fiber-Spin(8)
postulate behind N_gen=3 itself), A2 (the I8=eye(8) stub in round118/G18), A3
(round59's kernel=1 lacking any valid negative control)"*. No cached copy of the
original audit's full output was found in this repo (`.claude/checkpoints/`,
`.claude/state/`, `.claude/research/` all searched) — the paraphrase above is the
only surviving trace, so it is treated as `[UNKNOWN provenance, restated below from
primary sources]`, not as ground truth.

---

## Headline correction, stated up front

Two of the three labels (A1, A3) turn out to describe assumptions that are **not**
"untested with no experiment folder" — they are the OPPOSITE: thoroughly tested,
honestly disclosed in the project's own headline status line (`README.md:3`), and
explicitly registered as open in `pearl_registry/INDEX.md`. What genuinely matches
"untested, no experiment folder yet" in each case is a narrower, specific **follow-up
test** named in the same documents, not the original assumption itself. A2 is the
one label that is close to accurate as originally stated. See each section below for
the precise distinction, and the Step 3 ranking for why this distinction changes
the priority order.

---

## A1 — the fiber-Spin(8) postulate behind N_gen=3

### Precise restatement

**What is actually un-derived:** the third of three "independent triality channels"
(`8_v`, `8_s`, `8_c`) that the headline claim `N_gen=3` requires cannot be shown to
be physically distinct using only the geometric symmetry the `S³×S⁶` compactification
actually supplies (`G₂` and its `su(3)` holonomy subalgebra). Distinguishing all
three channels requires the full `Spin(8)`/triality structure, but no continuous
symmetry that large exists inside the geometry: `dim c_{so(8)}(g₂) = 0` exactly
[VERIFIED — `experiments/20260705-g102-spin8-fiber-obstruction/decision.md:14`,
9/9 pre-registered predictions exact, residuals at machine epsilon]. So the third
channel's physical independence is not derivable from `S³×S⁶` geometry — it must be
added as an external postulate (an independent fiber `Spin(8)` symmetry, e.g. from
a larger frame/gauge structure Tom's actual framework may or may not carry).

**Primary source:**
`experiments/20260705-g102-spin8-fiber-obstruction/claim.md:37-41` (the falsifiable
predicate and its consequence, pre-registered) and `decision.md:39-49` ("Consequence
for G67-C3 / N_gen=3": *"N_gen=3 itself: valid under the fiber-Spin(8) postulate
(Path A, external input)"*).

**What is assumed vs. what would need to be true for it to be safe:** the project
assumes Tom Lawrence's actual framework carries an independent fiber `Spin(8)`
symmetry (e.g. from a frame/gauge structure beyond bare `S⁶` geometry). For the
assumption to be safe, one of two things must hold: either that independent
`Spin(8)` genuinely exists in his framework (Path A closes by Schur, `N_gen=3`
complete), or the fermion content is strictly geometric and a different, currently
unknown mechanism supplies the third channel. Neither is verifiable internally —
this is explicitly logged as `BLOCKED-EXTERNAL` pending Tom's return
(`decision.md:46-49`; the project's own hard constraint is "DO NOT INITIATE
CONTACT" per `../CLAUDE.md`).

### Why "no experiment folder yet" is the wrong description of A1-as-labeled

G102 **is** the experiment folder (`experiments/20260705-g102-spin8-fiber-obstruction/`),
it ran 9 tests to machine precision, passed FL Step 8a self-administered skeptic
review (`decision.md:79-93`, 4 pre-answered concerns), and its finding is disclosed
at the top of the project's own README: `README.md:3` — *"G67-C3 dependency: 2/3
closed via G68, 1/3 = fiber-Spin(8) postulate — G102 proved it is NOT internally
derivable"* — and again at `README.md:269,317` and `RESEARCH_STATUS_REPORT.md:149,329`.
This is a prominent, headline-level disclosure, not a hidden gap. Nothing further
can be tested internally about whether the postulate is *true* — that is
irreducibly external (Tom's answer), correctly marked `BLOCKED-EXTERNAL`, not
"untested" in the FL sense of "a cheap check was never run."

### The genuine "no experiment folder yet" item adjacent to A1

`pearl_registry/INDEX.md:141` (2026-09-02, tagged `[WEAK]`, impact_score 8) names a
**different, actually open and actually testable** question: the **Blind-Prediction-
Test**. Quote: *"was the specific triality-symmetric structure chosen BECAUSE it is
already known to give 3 stable sectors, or would a genuinely blind construction (not
selecting for the answer) independently yield exactly 3? ... G102 (an explicit,
UN-derived fiber-Spin(8)/triality postulate is needed to distinguish the three
channels at all) already show PART of N_gen=3's own credit line rests on an
assumption, not a derivation"* — and explicitly, verbatim: *"pending — impact 8 —
**no experiment folder yet, this is a flagged methodological gap, not yet scoped as
an FL round**."* This is the literal match for the original audit's "no experiment
folder yet" framing — it is about whether `N_gen=3`'s specific construction is a
selection effect (HARKing risk), a question the G102 postulate itself does not
answer and was never designed to answer.

---

## A2 — the I8=eye(8) stub in round118/G18

### Precise restatement

`round118`'s (ledger id `C20_MATTER_GENERATION_FACTORIZATION_THREE_WAY`) "necessary
condition VERIFIED" finding (a charge-formula channel-independence check, confirmed
by grepping `preprint.tex` for a channel-indexed charge formula and finding zero
hits) is built on `K3_32`/`T3L_32`/`J3_32` — the `SU(2)_L`/`SU(2)_R` generator
matrices for the 32-dimensional `S³×S⁶` spinor. These are constructed via
`kron(J_i^4, I8)` where **`I8 = eye(8)`**
[VERIFIED — `experiments/20260618-g11-block-generators/g11_block_generators.py:57`,
used at line 196 (`J3_32 = kron(J_S3[2], I8)`) and lines 226-227]. `I8` is a bare
8×8 identity matrix standing in for the `S⁶` spinor factor — a placeholder, not a
real geometric object — built 2026-06-17/18, roughly a month **before** round59's
real twisted `S⁶` Dirac operator (2026-07-14) or G102's triality channels
(2026-07-05, i.e. also before) existed as constructions in this project.

**What is assumed vs. what would need to be true for it to be safe:** the construction
implicitly assumes the SU(2)_L/SU(2)_R charge operators act identically ("trivially")
on all three triality channels — which is exactly what `I8=eye(8)` enforces by
fiat, since an identity matrix cannot distinguish anything. For this to be safe, the
real per-channel `S⁶` spinor geometry (round59's operator, transported per-channel
via C70/C71's explicit `U_v/U_s/U_c` intertwiners) would need to actually give the
same charge structure when substituted for `I8` — this has never been checked. As
recorded directly in the round's own ledger entry: *"round118's charge-uniformity
finding was never actually tested against real channel-dependent geometry ...
'uniform' only because channel-dependence was never wired in as a variable, not
because real per-channel geometry agreed"*
[VERIFIED — `.claude/memory/activeContext.md:1856-1868`, cross-checked directly
against the cited source files in that session per its own note].

**Primary source of the gap-flag itself:**
`CLAIM_LEDGER.yaml:418-421` (C20's own `notes` field, added 2026-08-11) and
`.claude/memory/activeContext.md:1852-1886` ("S6-embedding gap take stock").

### Assessment against "no experiment folder yet"

This is the one label that is close to accurate as originally stated. `round118`
itself IS an experiment folder
(`experiments/20260717-round118-matter-generation-factorization-test/`), but the
**follow-up needed to close the gap** — rebuilding `K3_32`/`T3L_32` with round59's
real `Σ` transported per-channel, reconciling G10's tangent-bundle `su(3)` (6-dim)
with round59/G102's spinor-module `su(3)` (8-dim, never bridged), and re-deriving
G18's KO-dimension-6 structure from the result — has genuinely never been attempted.
The project's own scope estimate for this follow-up: *"comparable in scope to
redoing the entire G10-G19 program (13 rounds, 2026-06-17/19) plus reconciling it
with the round59/G102/C70/C71 chain (~15 more rounds) — not a quick fix"*
[INFERRED, `.claude/memory/activeContext.md:1876-1886`, explicitly labeled as the
session's own scope estimate, not a formal one].

---

## A3 — round59's kernel=1 and its negative control

### The user's own spot-check was correct — round59 itself does not discuss this

Direct read of `experiments/20260714-round59-trivial-rank-certification/decision.md`
confirms: PASS verdict, `rank(D+|1)=1` via three independent routes (A/B/C), full FL
Step 8a skeptic response matrix with 3 skeptics, all findings mitigated or accepted
as documented limitations (e.g. shared primary source AHL2023 + shared CAS). A
`grep -i "negative control"` over round59's own folder returns **zero matches**
[VERIFIED — Grep tool, this session]. The mislabeled attribution to round59 itself
does not hold up; **do not force it**, per this task's own instruction.

### What the gap actually is, and where it actually lives

The real gap was found and honestly reported by two **later** rounds, not round59
itself: `experiments/20260811-c73-round59-real-twisted-dirac-battery/` and its
follow-up `experiments/20260811-c73b-torsion-family-genuine-deformation-and-twist-control/`
(both 2026-08-11, ledger id `C73_ROUND59_DIRAC_BATTERY_CHIRALITY_DIRECT_DEFORMATION_ROBUST_NEG_CONTROL_OPEN`).

**Primary source, the precise finding:** C73's own pre-registered prediction P5
("at least one genuinely discriminating wrong-twist test can be constructed") is
recorded as **FAILING, honestly, as anticipated**
[VERIFIED — `experiments/20260811-c73-round59-real-twisted-dirac-battery/decision.md:21`].
Three attempts within round59's own fixed construction (Nomizu sign flip, alternate
bigrading pairing, mismatched-parity pairing) each either reproduce the identical
physical result via a hidden even/odd duality in `Σ`, or vanish for purely algebraic/
structural reasons (parity preservation) unrelated to physical correctness — **none
discriminate real twist from wrong twist**. C73b added a fourth, independently-
motivated attempt (twisting by `S+` instead of `S-`): also non-discriminating
(`decision.md:47-54`, C73b). The project's own synthesis states the reason this is
structural, not a failure of effort: *"'Kernel=1 holds at every point in the
admissible torsion family' and 'no discriminating negative control exists within
that family' are two descriptions of the SAME structural fact ... nothing INSIDE
that restricted family can ever serve as a wrong-twist control"*
[VERIFIED — `experiments/20260811-c76-status-synthesis-ngen3-regrade/decision.md:103-117`].

**What is assumed vs. what would need to be true for it to be safe:** `N_gen=3`
relies on `kernel(D_{S⁶,twisted}) = 1` (ledger id `C2_ROUND59_KERNEL_DIM1`) as
evidence that the twist round59 chose is the *physically correct* one, not merely
*a* twist that happens to give kernel=1. For this to be safe on its own terms, some
twist choice OUTSIDE round59's `su(3)`-equivariant family (a genuinely different
representation, not `1+1+3+3̄`-type, or an explicitly non-`G₂`-equivariant
perturbation) would need to be shown to give kernel ≠ 1 — i.e., a real negative
control. This has not been built. What IS well-established: kernel=1 is robust
(topologically protected, not fine-tuned) across the *entire* admissible family
that respects the same equivariance — a genuinely 2-real-dimensional (one complex
parameter) family, confirmed at all 13 tested angles
[VERIFIED — `experiments/20260811-c73b-.../decision.md:15-19`]. So the *result*
(kernel=1 for this whole equivariant family) is solid; what remains unverified is
whether stepping *outside* that family (a physically wrong twist) would actually
break it.

### Assessment against "no experiment folder yet"

Same pattern as A1: the gap itself has extensive experiment folders (C73, C73b) and
is registered as an open pearl
[VERIFIED — `pearl_registry/INDEX.md:89`, includes an explicit warning: *"before
citing round59's kernel=1 result as having passed a negative control (it has not,
honestly)"*]. What genuinely has no folder yet is the specific unbuilt construction
named as the fix: *"Building D_S⁶ twisted by a DIFFERENT representation than Σ ...
and checking that the resulting invariant-sector kernel is NOT 1"*
[VERIFIED — `pearl_registry/INDEX.md:89`, and independently at
`experiments/20260811-c73b-.../decision.md:76-84`, both call this "comparable in
scope to round59's own original build effort" — i.e. substantial but bounded, not
open-ended].

---

## Step 2 — Dependency / blast-radius map

Method: `CLAIM_LEDGER.yaml` carries an explicit `depends_on:` field per claim. Ran a
small parser (`parse_deps.py`, this session) over all 123 entries that declare
`depends_on` to find direct dependents of each assumption's ledger node
[VERIFIED — tool output below, cross-checked against manual `grep -B10` on the same
three targets, identical counts].

| Assumption | Ledger node | Direct CLAIM_LEDGER dependents | Includes headline? |
|---|---|---|---|
| A1 | `C_G67C3_THIRD_CHANNEL` | **6**: `C4_NGEN3_HEADLINE`, `C19_SPINOR_DECOMPOSITION_AUDIT`, `C61_OB11II_MIXING_NOT_EXCLUDED...`, `C62_OB11III_SU3_TRIALITY_FIXED...`, `C63_THREE_CHANNELS_PROVABLY_NOT_REDUNDANT`, `C67_MCRAE_2025_CONFIRMED...` | **Yes — direct** |
| A3 | `C2_ROUND59_KERNEL_DIM1` | **6**: `C3_KT8_NO_ZERO_MODE`, `C4_NGEN3_HEADLINE`, `C15_G74A_PROOF_ROUTE_SUPERSEDED`, `C21_G74B_CHIRALITY_SIGN`, `C27_MULTIPLICITY_2_FAIL`, `C73_ROUND59_DIRAC_BATTERY...` | **Yes — direct** |
| A2 | `C20_MATTER_GENERATION_FACTORIZATION_THREE_WAY` | **0** | **No** |

`C4_NGEN3_HEADLINE` (the literal `N_gen=3` claim) itself declares
`depends_on: [C1_S6_INDEX_1, C2_ROUND59_KERNEL_DIM1, C3_KT8_NO_ZERO_MODE,
C_G67C3_THIRD_CHANNEL]` [VERIFIED — `CLAIM_LEDGER.yaml:79`]. So **A1 and A3 are
both, structurally, direct parents of the project's own single headline claim** —
not incidental side-findings. A2's node has zero downstream ledger dependents; it
sits entirely inside the separate OB11/OB2 "matter-generation-factorization" /
NCG-spectral-triple program, and `README.md`'s own chain description for `N_gen=3`
(`README.md:317`: *"G73+G74A+G74B PROMOTE ... G67-C3 dependency settled by G102"*)
never cites round118/C20 at all [VERIFIED — `grep -n "round118\|C20_MATTER"
README.md RESEARCH_STATUS_REPORT.md PARENT_ACTION_GATE.md` returns zero hits].

**Beyond the formal ledger graph (qualitative, `[CITED]` not `[VERIFIED]` via the
parser):**

- A1's postulate is explicitly named as a **shared, reused ingredient** by the
  2026-09-02 `C132`→`C133` "symmetry ladder" work: *"rungs 2-3 share N_gen=3's own
  un-derived fiber-Spin(8) credit line"* [CITED —
  `.claude/memory/activeContext.md:45`, `PARENT_ACTION_GATE.md:463-471`], and by
  round119/round124's channel-distinguishing routes, used in the *opposite*
  direction (they break the same un-derived symmetry to distinguish channels,
  where the ladder keeps it unbroken to force uniformity) [CITED —
  `pearl_registry/INDEX.md:137`]. This means the entire OB1 F4 t-selection
  pipeline (rounds C123-C137, 15 rounds in the 2026-09-02/03 session alone) is
  built on scaffolding that itself leans on A1's un-derived ingredient at least
  once, even though none of those rounds are formal ledger dependents of
  `C_G67C3_THIRD_CHANNEL`.
- A3's negative-control gap is referenced in `pearl_registry/INDEX.md` (row 89,
  with an explicit warning against over-citing round59), `OPEN_BLOCKERS.md`, and
  `predictions_before_data.md`'s own round table (P4) as the reason `N_gen=3`
  would need to be weakened if it failed — it did not fail outright, but it also
  never fully passed [CITED — `experiments/20260811-ngen3-decisive-program/
  predictions_before_data.md:77,143`].
- A2's gap is referenced only within its own ledger entry's `notes` field and one
  pearl_registry row (1 row, vs. 3 for A1's "fiber-Spin" phrase and 8 for A3's
  "wrong-twist"/"negative control" phrases — counted by grep,
  `pearl_registry/INDEX.md`) [VERIFIED — grep counts, this session]. No headline
  document (`README.md`, `RESEARCH_STATUS_REPORT.md`, `PARENT_ACTION_GATE.md`)
  cites it.

---

## Step 3 — Value-of-information ranking

Scoring basis: **blast radius (Step 2) × cost-to-test × prior risk given how the
assumption was originally justified** (a hand-built stub is higher-risk than a
theorem proven three independent ways, per this task's own instruction).

| | Blast radius | Cost to actually close the gap | Prior risk | Externally blocked? |
|---|---|---|---|---|
| **A1** (fiber-Spin(8) postulate) | Largest in principle — directly gates the headline (6 ledger deps) AND is a shared ingredient across the entire live OB1 F4 pipeline | The *postulate itself* cannot be closed internally at any cost (needs Tom). The adjacent testable item (Blind-Prediction-Test, pearl row 141) has **no scoped test yet** — open-ended, methodologically undefined at present | Medium — honestly labeled as a postulate from the start (G102), not silently assumed | **Partially** — the postulate's truth is BLOCKED-EXTERNAL; the Blind-Prediction-Test is not |
| **A2** (I8=eye(8) stub) | Smallest — 0 ledger dependents, confined to a separate side-program (OB11/OB2), never cited by any headline document | High — project's own estimate is ~28 rounds (redo G10-G19 + reconcile with round59/G102/C70/C71) | **High** — a hand-picked placeholder built before the real geometry existed, exactly the "high-risk stub" pattern this task's own scoring guidance names | No |
| **A3** (round59 negative control) | Largest, tied with A1 — directly gates the headline (6 ledger deps, includes `C3_KT8_NO_ZERO_MODE` as well as `C4`) | Bounded and internally computable — "comparable in scope to round59's own original build effort" (a concrete, named construction: twist `D_{S⁶}` by a representation outside the `1+1+3+3̄` class) | Medium — the *result* (kernel=1) is robustly deformation-tested across the whole admissible equivariant family; what's missing is specifically evidence that stepping outside that family would break it | **No** — fully internal, no external dependency |

### Recommendation: test A3 first

**A3's follow-up experiment — building `D_{S⁶}` twisted by a genuinely different,
non-`(1+1+3+3̄)`-type representation and checking whether the invariant-sector
kernel becomes ≠ 1 — is the single best next test**, for three reasons:

1. **It is the only one of the three that is both high-blast-radius AND fully
   internally computable.** A1 ties A3 on blast radius but its core postulate is
   irreducibly external (BLOCKED-EXTERNAL); no amount of internal work closes it.
   A2 is internally computable but has near-zero blast radius (0 ledger
   dependents) and costs an estimated 15-28 rounds to fix — poor value even before
   considering risk.
2. **It is concretely scoped, not open-ended.** Two independent project documents
   (the pearl and C73b's own decision.md) already name the exact construction
   needed and estimate its cost as comparable to round59's own original build —
   large but bounded, unlike A1's Blind-Prediction-Test (genuinely undefined
   methodology at present) or A2's reconciliation project (estimated ~28 rounds
   across two never-bridged representation conventions).
3. **It closes the single most-cited standing warning in the registry.**
   `pearl_registry/INDEX.md:89` explicitly warns against citing round59's kernel=1
   "as having passed a negative control (it has not, honestly)" — this is an
   active, load-bearing caveat on the headline claim's own evidence chain, not a
   speculative side-question.

**Second priority:** scope (not yet run) the A1 Blind-Prediction-Test named in
`pearl_registry/INDEX.md:141` into an actual `claim.md` — even before running it,
turning "not yet scoped as an FL round" into a pre-registered, falsifiable design
is itself cheap and directly addresses the project's single largest standing risk
(a selection-effect challenge to the headline claim itself). This is a *design*
task, not requiring new mathematics, and is a natural Step -2/-1 (EstimandOps L0 +
estimand) exercise per this project's own methodology stack.

**Lowest priority: A2.** Its blast radius is genuinely small (0 ledger dependents,
confined to a side-program already carrying its own `CONDITIONAL`/`PARTIAL`/`OPEN`
status), and the fix is disproportionately expensive relative to what it would
buy. The one thing worth doing now, cheaply, is a documentation-only check: confirm
no external-facing text (preprint, abstract, any future submission) ever cites
`round118`'s "necessary condition VERIFIED" language without the I8-stub caveat
already recorded in `CLAIM_LEDGER.yaml:418-421` — this is a Submission Gate
concern, not a new experiment, and is out of this audit's scope to execute (per
this audit's own "do not propose fixing" instruction).

---

## Evidence marker summary

All primary-source citations above are `[VERIFIED]` (Read/Grep tool output this
session) or `[CITED]` (quoted directly from an already-existing project document).
The only `[INFERRED]` items are the two cost estimates for A2's and A3's follow-up
work, both explicitly labeled as the originating session's own scope estimate, not
a formally derived figure. The one `[UNKNOWN]` item is the original `/research-audit`
report's full text — no cached copy was found in this repo; this audit's
restatement of A1/A2/A3 rests entirely on independently re-derived primary sources,
not on trusting the compacted paraphrase.
