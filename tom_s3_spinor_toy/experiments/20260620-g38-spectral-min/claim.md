# Claim — G38: Spectral Action Minimum on Bundle Space

**Date:** 2026-06-20  
**Question type:** Predictive  
**Ladder tier:** Full

---

## Estimand

- **Population:** All rank-3 gauge bundles V on S⁶ with c₁=c₂=0 (forced by H²=H⁴=0), c₃ ∈ {2, 4, 6, 8, ...}
- **Intervention:** Minimize spectral action S = Tr[f(D_V²/Λ²)] over this bundle space
- **Comparator:** Compare S(c₃=6) vs S(c₃=2), the canonical minimum from G33
- **Endpoint:** Which c₃ minimizes S?
- **Summary measure:** ΔS = S(c₃=6) − S(c₃=2). Positive → S2 NULL
- **MCID:** ΔS > 0 by any positive mechanism → spectral action does NOT select c₃=6

---

## Falsifiable Claim (S2)

> The spectral action functional Tr[f(D_V²/Λ²)], minimized over rank-3 gauge bundles V
> on S⁶ with c₃ varying, achieves its global minimum at c₃=6 (N_gen=3),
> NOT at c₃=2 (N_gen=1).

**Kill conditions:**

| Condition | If true → verdict |
|-----------|------------------|
| Zero mode contribution = ch₃(V)×f(0) is monotone in c₃ | S2 NULL |
| Seeley-DeWitt a₄ gauge term ||F||² increases with c₃ | S2 NULL |
| No term in S_spec decreases with c₃ | S2 NULL |
| S_spec minimum is at c₃=2 (T^{1,0}S⁶) | S2 NULL |
| G38 reduces to G33 restated in energy language | S2 NULL (redundant) |

---

## What This Does NOT Mean

1. Does NOT mean the spectral action framework is wrong
2. Does NOT kill spectral action for SM gauge kinetic terms (G28 confirmed this)
3. Does NOT close the three-generation problem via other mechanisms
4. Does NOT prove N_gen=3 is impossible — only that S³×S⁶ spectral action minimum ≠ selection mechanism

---

## Assumptions

| Assumption | Evidence | Falsifiable? |
|------------|----------|--------------|
| H²(S⁶;ℤ)=H⁴(S⁶;ℤ)=0 → c₁=c₂=0 | Homotopy groups of S⁶ | Yes: find c₁≠0 bundle on S⁶ |
| ind(D_V) = ch₃(V) = c₃/2 on S⁶ | Atiyah-Singer (G33) | No (theorem) |
| f(0) > 0 for physical cutoff | By definition of spectral action | No |
| ||F||² increases with ch₃(V) | YM lower bound (Cauchy-Schwarz) | Yes: find exception |
| No non-monotone cross-term | Seeley-DeWitt structure | Yes: find negative a₄ term |
