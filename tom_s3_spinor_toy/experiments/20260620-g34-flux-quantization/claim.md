# Claim — G34: Flux Quantization Gate

**Date:** 2026-06-20  
**FL tier:** Full  
**Question type:** [x] predictive  [ ] descriptive  [ ] causal

---

## Estimand

**Population:** Selection mechanisms on S⁶ that constrain c₃(V) for rank-3 bundle V  
**Intervention:** Apply flux quantization / tadpole condition from S⁶ geometry  
**Comparator:** No selection principle — c₃(V) ∈ ℤ is unconstrained topologically  
**Endpoint:** Does flux quantization independently force c₃(V) = 6?  
**Summary measure:** Is there a topological invariant of S⁶ that equals 3 independently of N_gen?  
**MCID:** "Selection" = independent equation forcing c₃=6, not merely allowing it

---

## Claim (to falsify)

**D1:** Flux quantization on S⁶ provides an independent equation that forces c₃(V) = 6
(without inputting N_gen = 3 by hand), giving ind(D_V) = 3 chiral generations.

---

## Background (inherited from G32/G33)

| Known | Status |
|-------|--------|
| c₃(T^{1,0}S⁶) = χ(S⁶) = 2 | [VERIFIED] G33 |
| ind(D_{T^{1,0}S⁶}) = 1 | [VERIFIED] G33 |
| G₂-equivariant rank-3 bundles: max c₃ = 2 | [VERIFIED] G33 |
| Non-equivariant rank-3 bundle with c₃=6 exists topologically | [VERIFIED] G32 (π₅(U(3))=ℤ) |
| c₃=6 requires N_gen=3 as input in A1 | [VERIFIED] G33 — A1 is circular |
| G27/G30/G31 kill equivariant/ℤ₃/S³ paths | [VERIFIED] null_results/INDEX.md |

Generation unit: c₃=2, ind=1.  
Open: what selects the factor 3?

---

## Kill conditions

| Condition | Kill signal |
|-----------|-------------|
| Flux quantization forces c₃=6 independently | Killed if: derives "3" without N_gen as input |
| Tadpole on S⁶ gives fixed c₃ = 6 | Killed if: tadpole value equals a topological invariant ≠ 3×something |
| No natural "3" from S⁶ geometry | NOT killed if: some G₂/SU(3) invariant gives exactly 3 |
| D1 is circular (embeds N_gen=3) | Killed if: all routes to "3" require N_gen=3 as prior |

---

## What this does NOT mean

1. Does NOT kill G32 — the non-equivariant bundle still exists, question is why c₃=6 is selected
2. Does NOT test B3 (WZW level) or C1 (NCG M₃(ℂ)) — those are separate gates
3. Does NOT require string theory — question is purely about geometric/topological selection
4. Does NOT assume tadpole exists — D1 is tested, not assumed

---

## Escape routes

- If D1 is NULL → promote G35: cobordism / global anomaly (A2)
- If D1 is WEAK → check flux + anomaly combination
- If D1 gives PROOF → prepare mathematical note on tadpole selection
