# [GATE-ID] Claim — [Short description]

**Date:** YYYY-MM-DD  
**FL tier:** [ ] Micro  [ ] Standard  [x] Full  
**Question type:** [ ] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

> Do not proceed past this section until status is NEW or OPEN.
> Full 7-step protocol: `PRIOR_RESULT_GATE.md` (this experiment dir,
> or the nearest one up the tree). One real incident motivates this:
> a round rediscovered a result a prior round had closed two days
> earlier, because the intervening round reopened it without checking
> and this one trusted that framing instead of re-verifying.

1. Exact claim: _______________________________________________
2. `decision.md` grep (formula + synonyms): [ ] done, 0 hits / hits reviewed at: ___
3. `round*_claim.md` + scripts grep: [ ] done, 0 hits / hits reviewed at: ___
4. `null_results/` + `parked/` grep: [ ] done, 0 hits / hits reviewed at: ___
5. `git log -S`/`-G` pickaxe: [ ] done, 0 hits / hits reviewed at: ___
6. Primary source re-read (not from memory): [ ] done, source/pages: ___
7. **Status:** [ ] NEW  [ ] OPEN  [ ] CLOSED  [ ] SUPERSEDED  [ ] DUPLICATE  [ ] RETRACTED  [ ] PARKED

If CLOSED/SUPERSEDED/DUPLICATE/RETRACTED/PARKED → STOP here, cite the
prior result instead of proceeding.

---

## Estimand

**Population:** [Who/what — e.g. "Rank-3 bundles on S⁶"]  
**Intervention:** [What exactly]  
**Comparator:** [vs. what baseline]  
**Endpoint:** [Measured quantity with units]  
**Summary measure:** [Population-level statistic — prefer absolute over HR/OR]  
**MCID:** [Minimum practically important difference — below this = don't act]

---

## Claim

[Falsifiable statement in one sentence. Must be pre-registered BEFORE seeing results.]

Supporting sub-claims:
1. [Sub-claim 1]
2. [Sub-claim 2]

---

## Kill criterion (MANDATORY — fill BEFORE running)

> What exact result would FALSIFY this claim and STOP the experiment?

| Kill condition | Threshold |
|---|---|
| [Condition A] | [e.g. ind ≠ 3] |
| [Condition B] | [e.g. rank(J) ≥ 3] |

If FAIL → kills: [Which hypothesis in ACH matrix / which sub-branch dies]  
If PASS → survives: [What it strengthens]

If no hypothesis is killed by FAIL → gate is not scientifically motivated. Do not run.

---

## Checks planned

- T1: [description]
- T2: [description]
- T3: [description — include at least one adversarial/edge-case check]

---

## What this does NOT mean

1. Does NOT prove [...]
2. Does NOT establish [...]
3. Does NOT apply when [boundary condition]

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER  
- GEOMETRY_AGNOSTIC = True  
- safe_for_runtime = False

---

## Verdict

[OPEN — fill after running: PASS_XXX / PARTIAL_XXX / FAIL_XXX]

**Evidence:** [VERIFIED-sympy N/N] or [VERIFIED-pytest N/N]

**Status:** [planned | CLOSED PASS_XXX | CLOSED FAIL]
