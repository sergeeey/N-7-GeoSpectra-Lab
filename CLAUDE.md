# CLAUDE.md — N-7-GeoSpectra-Lab (project-level)

## Project type
**RESEARCH** — falsification-first numerical/algebraic physics harness.
Resolves dispatcher ambiguity (was: research=6, production=5, tie).
README + activeContext.md use VERIFIED/KILLED/PASS/FAIL evidence markers,
ACH falsification matrices, kill_criterion gates — this is not production code,
methodology = **FL Full + EstimandOps** for every experiment (per global dispatcher rule).

## Two tracks (do not conflate)
| | Track A — Numerical | Track B — Algebraic |
|---|---|---|
| Dir | `cc_toy_lab/`, `scripts/`, `tests/` | `tom_s3_spinor_toy/` |
| Verdict | `DISCRETIZATION_SENSITIVE` | N_gen=3 via Atiyah-Singer |
| Entry | `reports/GATE4B_SPECIFICITY_VERDICT_v0.1.24.md` | `tom_s3_spinor_toy/RESEARCH_STATUS_REPORT.md` |

Third, independent track (frozen 2026-06-30): `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`
— spectral-recoverability-vs-physics null result (H0 wins, H1-H4 killed). See `CLAIMS_REGISTRY.md`.

## Hard constraints (do not violate — carried from activeContext.md)
- Tom Lawrence: **DO NOT INITIATE CONTACT** — he reaches out when Part 4/5 ready
- `lambda = FREE_COUPLING_PARAMETER` — never claim derived/fixed (LAMBDA-B5-G4 theorem)
- `sm_derivation_claimed = False`; "tom_ansatz solved" phrasing FORBIDDEN
- `safe_for_runtime = False`, `runtime = research_only`
- DO NOT merge `preserve/*` → main without explicit audit/cherry-pick decision
- New code: bare `lambda` FORBIDDEN — use `lambda_v`/`lambda_v_operator` or `lambda_np` explicitly
  (lambda_v_operator vs lambda_np — see `tom_s3_spinor_toy/experiments/20260622-g79a-lambda-identity-audit/lambda_separation_plan.md`)

## Methodology activation (per global ~/.claude/CLAUDE.md dispatcher)
Every new experiment/claim in this repo goes through, in order:
1. `~/.claude/rules/estimand-ops.md` — L0 gate (descriptive/predictive/causal) before design
2. `~/.claude/rules/falsification-ladder.md` — Full tier: claim.md + estimand.md + kill_criterion
   → use `tom_s3_spinor_toy/experiments/_template/claim.md` (has mandatory kill_criterion section)
3. `~/.claude/rules/doubt-driven-development.md` — skeptic red-team before non-trivial builds
4. `~/.claude/rules/audit-verification-gate.md` — tool-verify any HIGH/MEDIUM finding before reporting
5. `~/.claude/rules/integrity.md` evidence markers on every numeric/factual claim

## Experiment naming
`experiments/YYYYMMDD-<gN>-<slug>/` with `claim.md` + `decision.md` (+ script + `results_gN.json`).
Rejected → `null_results/<id>.md` + INDEX. Deprioritized → `parked/<id>.md` + INDEX.

## Memory
`.claude/memory/activeContext.md` — current focus, updated after each commit (auto-logged).
