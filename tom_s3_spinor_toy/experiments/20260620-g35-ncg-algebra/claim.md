# Claim — G35: NCG Finite Algebra Gate (C1)

**Date:** 2026-06-20  
**FL tier:** Full  
**Question type:** [x] predictive  [ ] descriptive  [ ] causal

---

## Estimand

**Population:** Generation-selection mechanisms on S⁶ via NCG finite spectral triple  
**Intervention:** Derive A_F = M₃(ℂ) from End(T^{1,0}S⁶) without inputting N_gen=3  
**Comparator:** A_F postulated (Connes-Chamseddine-Marcolli), not derived  
**Endpoint:** Does the M₃(ℂ) structure of End(T^{1,0}S⁶) independently force N_gen=3?  
**Summary measure:** Does the geometric derivation of A_F produce H_F = ℂ^96 (3 gen) or H_F = ℂ^32 (1 gen)?  
**MCID:** "Independent derivation" = N_gen drops out WITHOUT embedding N_gen=3 as prior

---

## Claim C1 (to falsify)

**C1:** The endomorphism algebra End(T^{1,0}S⁶) = M₃(ℂ) provides a non-circular derivation
of the NCG finite spectral triple algebra A_F that independently forces N_gen = 3 chiral generations.

---

## Subhypotheses

| Label | Claim | Status to check |
|-------|-------|-----------------|
| C1-A | End(T^{1,0}S⁶) = M₃(ℂ) gives SU(3)_c color gauge algebra | Plausible — color, not generations |
| C1-B | dim(M₃(ℂ)-module) = 3 → N_gen = 3 | Circular check needed |
| C1-C | Two independent M₃(ℂ) factors on S⁶ → one for color, one for generations | Available on S⁶? |

---

## Background

| Known | Status |
|-------|--------|
| rank(T^{1,0}S⁶) = dim_ℂ(S⁶) = 3 | [VERIFIED] geometric fact, G₂/SU(3) |
| End(T^{1,0}S⁶) = M₃(ℂ) | [VERIFIED] endomorphism of rank-3 bundle |
| G18: A_F = ℂ⊕ℍ⊕M₃(ℂ) assumed, not derived | [VERIFIED] G18 claim.md §"What this does NOT mean" |
| G18: H_F = ℂ^32 for 1 generation | [VERIFIED] G18 |
| G18: three generations require H_F = ℂ^96 | [VERIFIED] G18 §"What this does NOT mean" |
| c₃(T^{1,0}S⁶) = 2, ind = 1 | [VERIFIED] G33 |
| N_gen input required for H_F = ℂ^96 | [HYPOTHESIS] — to check in G35 |

---

## Kill conditions

| Condition | Kill signal |
|-----------|-------------|
| C1-A only: M₃(ℂ) explains color, not generations | SOFT_KILL — valid but off-topic for three-generation question |
| C1-B circular: dim=3 from rank=3 = N_gen=3 | HARD_KILL — same as A1 revisited |
| C1-C not available: only one M₃(ℂ) on S⁶ | HARD_KILL — color and generation cannot be simultaneously derived |
| C1 requires N_gen input for H_F = ℂ^96 | HARD_KILL — C1 does not independently select 3 generations |

---

## What this does NOT mean

1. Does NOT kill End(T^{1,0}S⁶) = M₃(ℂ) as the origin of SU(3)_c color — that remains valid
2. Does NOT close G32 — the topological bundle c₃=6 remains available
3. Does NOT rule out a DIFFERENT NCG approach (e.g., spectral action minimum on bundle space)
4. Does NOT kill K-theory or string tadpole routes

---

## Escape routes

- If C1 NULL → record M₃(ℂ) as COLOR-only (non-circular) derivation, separate from generation count
- If C1 PASS (bridge found) → write detailed mathematical note + G36 stress test
- If C1-C requires new geometry → check S³×S⁶ combined NCG (two factors, two algebras)
