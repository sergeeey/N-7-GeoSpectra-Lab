# G48: Harland-Nölle (2011) Paper Verification — G43-B5 Closure

**Date:** 2026-06-20  
**Ladder tier:** Full  
**Type:** Literature verification — closing G43-B5 gap  
**Verified by:** Primary source reading (user) + abstract verification (arXiv:1109.3552)

---

## L0: Question Type

**Descriptive** — Does Harland & Nölle (2011) "Instantons and Killing spinors"
construct an explicit HYM bundle with c₃=6 on S⁶?

---

## Estimand

- **Population:** The paper arXiv:1109.3552 (Harland & Nölle 2011)
- **Intervention:** Read and extract: what is constructed ON S⁶ (not on cones/ℝ⁷)
- **Comparator:** G43-B5 revival condition (c₃=6 HYM on S⁶)
- **Endpoint:** Is c₃=6 bundle on S⁶ (compact) constructed? Binary: YES/NO
- **MCID:** YES → G43-B5 survives; NO → G43-B5 closes as NULL

---

## Verified Facts [VERIFIED-REAL] — Primary source reading

**A. What the paper constructs on S⁶ (base manifold, compact):**
- Connection on the TANGENT BUNDLE T(S⁶) using the nearly Kähler structure
- This connection solves the instanton equation
- It is the CANONICAL Levi-Civita-type instanton on T(S⁶)
- Chern class: c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (= G33 canonical result)
- No new c₃=6 bundle on S⁶

**B. What the paper constructs on the CONE Cone(S⁶) = ℝ⁷:**
- New instantons on ℝ⁷ with G₂ structure
- "New instantons on even-dimensional Euclidean spaces" (abstract)
- The octonionic instanton on ℝ⁸ (and related on ℝ⁷)
- These live on ℝ⁷, NOT on S⁶

**C. What the paper does NOT do:**
- Does NOT construct an explicit bundle on S⁶ with c₃=6
- Does NOT discuss fermion counting or N_gen
- Does NOT address particle physics generation problem

---

## Mathematical Fact [VERIFIED]

Cone(S⁶) = ℝ⁷ with G₂-holonomy structure.
S⁶ is the link of the G₂ cone. An instanton on ℝ⁷ ≠ instanton on S⁶.
(Standard fact: Hitchin 2000, Joyce 2000, Harland-Nölle 2011 §2.)

---

## Sub-Claims

**H_G48a:** Harland-Nölle work on CONE (ℝ⁷), not compact S⁶, for new constructions.
→ **PASS** [VERIFIED-REAL]

**H_G48b:** On S⁶ itself, they construct only the canonical T(S⁶) instanton with c₃=2.
→ **PASS** [VERIFIED-REAL] (consistent with G33)

**H_G48c:** No c₃=6 bundle on S⁶ is constructed anywhere in the paper.
→ **PASS** [VERIFIED-REAL]

**H_G48d:** No fermion generation counting in the paper.
→ **PASS** [VERIFIED-REAL]

---

## Consequence for Theorem T1

G43-B5 (Category 6) closes as **NULL**.

Theorem T1 becomes **UNCONDITIONAL**:
> No mechanism in Categories 1–6 can select N_gen=3 on S³×S⁶.

---

## What This Does NOT Mean

1. Does NOT mean no c₃=6 bundle on S⁶ exists (existence unproven either way)
2. Does NOT close the mathematical question for all possible papers
3. Does NOT mean S³×S⁶ produces N_gen=3 via some unknown mechanism

---

## Source

Harland, D. and Nölle, C. (2011).  
"Instantons and Killing spinors."  
arXiv:1109.3552 [math.DG]  
Abstract verified via https://arxiv.org/abs/1109.3552
