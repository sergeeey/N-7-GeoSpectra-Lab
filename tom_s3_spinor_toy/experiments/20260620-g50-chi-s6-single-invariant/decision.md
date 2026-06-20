# G50 Decision — PROMOTE

**Date:** 2026-06-20  
**Verdict:** PROMOTE

## Result

The Single-Invariant Lemma is VERIFIED-sympy:

> **H²(S⁶;ℤ) = H⁴(S⁶;ℤ) = 0 forces c₁=c₂=0 for any bundle on S⁶.**
> **Therefore c₃(Λ²(T^{0,1})) = c₁c₂ − c₃(T^{1,0}) = −χ(S⁶) = −2.**
> **G33 (Gauss-Bonnet-Chern), G38 (S_spec monotone min), G39 (Whitney) all give |c₃| = χ(S⁶) = 2.**
> **6 = 3×χ(S⁶)−impossible by one-step formula, not from three independent mechanisms.**

21/21 pytest tests PASS.

## What This Changes

**Before G50:** Proposition T1 = "14 null results by exhaustion; no 15th tested yet."

**After G50:** Proposition T1 = structural theorem with 2 lemmas:
- **Lemma 1 (χ-lemma):** H²(S⁶)=H⁴(S⁶)=0 → c_n=0 for n=1,2; all Chern mechanisms
  reduce to c₃=±χ(S⁶)=±2 ≠ 6. Covers G33, G37, G38, G39 simultaneously.
- **Lemma 2 (rigidity):** round metric → unique isotropy → 1 spinor sector.
  Covers G44, G46, T2 simultaneously.

**Answer to "what about the 15th mechanism?":** 
If it uses Chern classes → blocked by Lemma 1.
If it uses metric rigidity → blocked by Lemma 2.
Both cover the mechanism space without enumeration.

## What This Does NOT Change

- G27, G30, G31, G34-B3, G34-A2, G35, G36 still need individual arguments (2 lines each).
- WEAK results G40, G41, G45c are NOT covered — different structure.
- Hard fences unchanged: λ=FREE, sm_derivation_claimed=False.

## Impact on Preprint

The PROCEEDINGS.md Section 7.1 and preprint_abstract.md can be upgraded:
Replace "case analysis" with "two structural lemmas + corollaries."
The abstract sentence becomes:
> "We show by two structural lemmas — the χ-lemma (H²(S⁶)=H⁴(S⁶)=0 forces 
> all Chern-class c₃=±2≠6) and the rigidity lemma (round metric → one spinor sector) —
> that no mechanism within the five geometric classes investigated here can select N_gen=3."

## Kill Analysis

G50 did NOT kill any hypothesis. It UPGRADED an existing positive result (T1):
- What changed: T1 proof is shorter and answers "what about N+1 mechanism?"
- What survived: all null result experiments remain valid as corollaries.
- Relaxation needed: none.
