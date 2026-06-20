# Claim — G36: K-Theory Gate

**Date:** 2026-06-20  
**FL tier:** Full  
**Question type:** [x] predictive  [ ] descriptive  [ ] causal

---

## Estimand

**Population:** Topological classification of rank-3 bundles on S⁶ via K-theory  
**Intervention:** Apply K-theory stability conditions and Adams operations  
**Comparator:** No K-theory condition — all c₃ ∈ ℤ equally allowed  
**Endpoint:** Does any intrinsic K̃(S⁶) condition force [V]-3 = 3β (c₃=6) over [V]-3 = β (c₃=2)?  
**Summary measure:** Is there a K-theory eigenvalue, twist, or stability condition that selects n=3?  
**MCID:** "Selection" = condition that distinguishes 3β from β without embedding N_gen=3

---

## Claim K1 (to falsify)

**K1:** K-theory on S⁶ provides a natural condition (stability, Adams operation, 
charge quantization, or twist) that independently forces the physical bundle to 
satisfy [V]-3 = 3β in K̃(S⁶), giving c₃=6 and N_gen=3 chiral generations.

---

## Background

| Known | Status |
|-------|--------|
| K̃(S⁶) = ℤ | [VERIFIED] AHSS: H⁶(S⁶;ℤ)=ℤ, no extension issues |
| Generator β: ch₃(β) = c₃(β)/2 = 1 | [VERIFIED] by construction |
| T^{1,0}S⁶: [T^{1,0}S⁶]-3 = β (c₃=2) | [VERIFIED] G33 |
| c₃=6 bundle: [V]-3 = 3β | [INFERRED] ch₃ = c₃/2 = 3 |
| π₅(U(3))=ℤ: c₃=6 bundle exists | [VERIFIED] G32 |
| No natural "3" in K̃(S⁶)=ℤ | [HYPOTHESIS] — to verify |

---

## Kill conditions

| Condition | Kill signal |
|-----------|-------------|
| K̃(S⁶)=ℤ has no distinguished element at n=3 | HARD_KILL if no condition selects n=3 |
| Adams operations: ψ^k scales nβ → k³nβ (no new structure) | HARD_KILL — ψ^k doesn't select n |
| "3 copies of β" embeds N_gen=3 as prior | CIRCULAR — same as A1/C1-B |
| No B-field twist on S⁶ (H³(S⁶;ℤ)=0) | NULL for twisted K-theory |

---

## What this does NOT mean

1. Does NOT kill K-theory as a tool for classifying SM D-brane charges (separate question)
2. Does NOT kill string tadpole route (RR-charges in compact 10D require bulk)
3. Does NOT close G32 — topological bundle remains valid
4. Does NOT rule out twisted K-theory in compact geometry beyond S⁶
