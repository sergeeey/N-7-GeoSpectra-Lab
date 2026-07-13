---
experiment_id: 20260708-dolan-casimir-g2su3
round: 48
date: 2026-07-13
tier: Standard-Ladder
status: complete
parent: round47b (mandatory Prior Result Gate + RHO/NU notation closed);
  this round is the user's own P2 step — a full open-claims audit of
  preprint.tex before selecting a new major research target, using the
  priority formula (impact+kill_power+reusability+publication_value)/
  (cost+assumption_debt+continuity_risk)
---

# claim.md — Round 48: full open-claims audit of preprint.tex — 14
non-proved claims classified, priority-ranked shortlist for Round 49

## Question Type (EstimandOps L0)
[x] Descriptive — classifying existing claims by evidentiary status
against this project's own experiment history. Not a new falsifiable
physics derivation; Standard tier (not Full) is appropriate — no FL
Step 8a adversarial math-skeptic review applies to a classification
task in the same sense it does to an operator identity.

## Method

Read `preprint.tex` in full (1327 lines). Extracted every claim NOT
already fully proved (proved claims — L1, L1a, L2, Â-genus, c3
computation, E-L3-PARTIAL, family universality G75, Theorem E-L3B,
NK6 uniqueness, topological identity remark, λ-dimensional obstruction
Buckingham Pi, G66/G62 zero-fit radius, Lemma L5 chirality — 12 claims
— needed no re-audit). Identified 14 remaining claims (conditional /
open / hypothesis-labeled per the paper's own text). Dispatched one
verification agent per claim (pipeline, tool-verified via `decision.md`
grep, `null_results`/`parked` grep, and — where relevant — reading
other experiment directories beyond `20260708-dolan-casimir-g2su3`),
classifying each into: доказано / условно / вычислительно подтверждено
/ открыто / противоречиво / требует внешней проверки. For genuinely
OPEN, non-Tom-dependent candidates, ran a second pass scoring the
user's own priority formula.

## Findings

**0/14 claims are "доказано"** — expected and honest for a
pre-submission preprint, not a red flag.

**8/14 claims (57%) have `paper_label_stale=true`** — the preprint's
own text does not reflect work already done in LATER rounds. This is a
pure documentation-debt finding, separate from selecting a new research
target. 6 of the 8 can be fixed with citation-only edits, no new
research, no Tom-Lawrence contact needed:

| Claim | Current text | Stale because |
|---|---|---|
| L4A | "left as an open problem" | Round 22-23 already computed F_{S^-}'s explicit spectrum {1/6:15, -5/2:1} |
| Integrability of J | "must be verified" | Round 22 already gives the explicit closed-form D₇² decomposition, reviewer+skeptic CONFIRMED-REAL |
| G88E | "gate G88E, open... order-of-magnitude" | G91 (same day as the cited gate) gives an explicit 4D action (`CONSTRAINED_PHYSICAL_RATIO`) |
| Weinberg angle | "pending complete Pati-Salam spectral action" | G97 found `SU(4)` is not even in `Iso(S³×S⁶)` — a sharper open question than the current text states |
| ρ3 stabilization | "requires additional contribution... (D-term, flux, brane)" | G91-G94/G102 already built a working brane-instanton mechanism (4% precision) |
| λ=1/3 [HYPOTHESIS] | "unknown and left for future work" | **G103 already tested and REJECTED this exact hypothesis** (`null_results/INDEX.md`, "G103-UV \| NULL") — the preprint states as an OPEN QUESTION something already CLOSED (negatively) in this same repo |

The remaining 2 stale claims (L3b, λ non-perturbative/G72) need a
STRONGER citation (G102's fiber-obstruction NULL result, more
decisive than the currently-cited E-L3B) but their actual resolution
still requires Tom Lawrence's input — per the project's own **DO NOT
INITIATE CONTACT** constraint, only the citation can be fixed now, not
the underlying claim.

**1/14 claims is genuinely CONTRADICTORY** — the λ=1/3 hypothesis
(above) is the most significant finding of this round: the preprint
presents as a live open question something this project's own
Round G103 (2026-07-05) already falsified.

**2/14 claims are NEEDS-EXTERNAL-VERIFICATION** (L3b, L4B trivial-
component rank) — both genuinely blocked on external input (Tom
Lawrence for L3b; an independent human sign-off for L4B rank, already
calibrated + stress-tested 3 independent ways since Round 11, status
has not changed since — confirmed NOT stale, honestly stalled awaiting
review).

**Full classification table, priority-scored shortlist, and the
Round 49 recommendation are in the synthesis report** (reproduced in
`decision.md`'s own Round 48 entry — this document does not duplicate
the full table to avoid drift between two copies).

## What this does NOT mean

- Does NOT constitute new physics or a new falsifiable claim about the
  paper's own subject matter — it is a status audit of EXISTING claims.
- Does NOT recommend touching L4A's own norm-bound tension (`8/45 vs
  ~1.03`) — explicitly excluded per the user's own standing instruction;
  the L4A stale-text fix is scoped ONLY to citing the already-computed
  F_{S^-} spectrum, not to reopening or resolving the tension itself.
- Does NOT recommend new `Z_i` constructions or re-investigating
  `Casimir_su3=C~h` (closed, Round 30/46) — both explicitly excluded by
  the user, confirmed absent from the priority shortlist.
- Does NOT initiate any contact with Tom Lawrence — L3b and the λ
  non-perturbative question remain flagged as blocked on his input,
  citation-only fixes proposed for the meantime.
- **Concrete next steps, NOT started:** (a) apply the 6 no-Tom-needed
  citation fixes to `preprint.tex` — cheap, low-risk, arguably urgent
  given the λ=1/3 contradiction and the pending arXiv submission
  (`arxiv_submission_20260708.tar.gz` already exists in the repo); (b)
  Round 49, per the priority-ranked shortlist: RGE-matching/M_KK
  threshold corrections (priority 2.11 of the formula, ~30 min, no new
  derivation — arithmetic on already-computed G29/GA2 numbers).

## Skeptic Verdict

Not applicable in the FL Step 8a mathematical-adversarial sense (no
operator identity or physics claim is being promoted by this round
itself). Each individual sub-claim's classification was independently
tool-verified (grep + read, not narrative-trusted) by its own dispatch
agent per this project's own `audit-verification-gate.md` discipline.
