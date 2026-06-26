# [GATE-ID] Claim — [Short description]

**Date:** YYYY-MM-DD  
**FL tier:** [ ] Micro  [ ] Standard  [x] Full  
**Question type:** [ ] descriptive  [ ] predictive  [ ] causal

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
