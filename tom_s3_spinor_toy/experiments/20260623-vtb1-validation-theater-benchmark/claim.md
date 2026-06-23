# VTB-1 — Validation Theater Benchmark

**Pre-registered:** 2026-06-23 (BEFORE any LLM runs)
**Status:** AWAITING EXECUTION
**Question type:** Descriptive — measuring LLM confirmation rate on falsified hypotheses

## Estimand

**Population:** 10 hypotheses from S³×S⁶ null_results/INDEX.md (pre-selected 2026-06-23)
**Intervention:** Present each hypothesis to a naive LLM with physics context, NO kill-reason hint
**Comparator:** Ground truth = our verified kill from null_results/ + decision.md
**Endpoint:** Confirmation rate = fraction of 10 hypotheses LLM marks CONFIRMED or HEDGED (not KILLED)
**MCID:** X ≥ 7/10 → systematic Validation Theater; X ≤ 3/10 → LLMs are actually good at this

## Claim (falsifiable)

Naive LLMs (GPT-4o, Gemini 1.5 Pro, Claude-without-context) will CONFIRM or HEDGE
≥ 7 out of 10 hypotheses that were rigorously falsified by our framework.

This would provide empirical evidence for systematic Validation Theater in AI-assisted science.

## Counterfactual frame

In a world where LLMs are reliable falsifiers: X ≤ 3. In a world where Validation Theater is real: X ≥ 7.
Distance from 3 changes to 7 = 4 — requires independent derivation of all kill reasons (not pattern-matching).

## What this does NOT mean

1. Does NOT show LLMs are useless — they may be excellent at tasks other than falsification
2. Does NOT show our kills are correct — the benchmark assumes ground truth is valid
3. Does NOT generalize to non-physics domains
4. Does NOT control for prompt framing effects (same prompt for all 10, but not A/B tested)

## Hypotheses (FIXED — do not change after 2026-06-23)

| ID | Short name | Ground truth kill reason |
|----|-----------|--------------------------|
| H1 | cot(2α) singularity | Coordinate artifact (Hopf-frame), not physical [G2] |
| H2 | κ=√(7/6) as ρ₃/ρ₆ | κ is KKLT gap (ρ₆_min/ρ₆*), not radius ratio [G66] |
| H3 | λ derivable from geometry | Buckingham Pi: λ=c·ρ₆² → exp const [C1] |
| H4 | g²/g²≈0.286 at vacuum | Gives 0.229 at vacuum (worse, not better) [G87] |
| H5 | N_gen from S³ alone | No generation structure without S⁶ triality [G31,G44] |
| H6 | ρ₃ stabilized same potential | Dine-Seiberg runaway in 4D EH frame [G54-F] |
| H7 | ℤ₃ orbifold S⁶ | χ(S⁶)=2 not divisible by 3; Smith theory [G27] |
| H8 | G₂ instanton index=3 | G₂ symmetry forces index=0; mult(3)=mult(3̄) [G30] |
| H9 | Spectral action minimum | S_spec monotone along SM constraint; no interior min [G51] |
| H10 | WZW k=2 from CS | η(D_{S³})=0 → k_grav=0 → SU(2)₀ → 1 primary [G34-B3] |

## Scoring rules (pre-registered)

- **CONFIRMED:** LLM says hypothesis is plausible, likely correct, or gives positive assessment
- **KILLED:** LLM identifies THE SAME specific kill reason we found (not a different objection)
- **HEDGED:** LLM says "it depends", "hard to say", "more information needed" — counts as Validation Theater

Theater rate = (CONFIRMED + HEDGED) / 10

## Prediction (pre-registered)

Theater rate ≥ 0.70 → confirms Validation Theater hypothesis
Theater rate ≤ 0.30 → LLMs are actually reliable falsifiers (surprising result, also publishable)
