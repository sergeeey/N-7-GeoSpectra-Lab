# G47: The Three-Generation Exhaustion Theorem

**Date:** 2026-06-20  
**Ladder tier:** Full  
**Type:** Synthesis / theorem formalization  
**Pre-registered prediction:** PASS (theorem holds) + OPEN (one gap remains: G43-B5)

---

## L0: Question Type

**Descriptive** — After G27–G46 (19 null/weak/open results), is the collection of
negative results sufficient to constitute a THEOREM that S³×S⁶ (and its S³×S⁷ extension)
cannot give N_gen=3 by any mechanism in the established geometric categories?

---

## Estimand

- **Population:** All geometric mechanisms acting on S³×S⁶ or S³×S⁷
- **Intervention:** Systematic enumeration of 6 mechanism categories
- **Comparator:** A complete theorem vs. a collection of independent null results
- **Endpoint:** Is each category covered by at least one verified null result?
- **MCID:** Zero uncovered categories → theorem holds; ≥1 uncovered → theorem incomplete

---

## Theorem Statement (to be verified)

**Theorem T1 (Three-Generation Obstruction):**

*Let M = S³(ρ₃) × S⁶(ρ₆) be the product of a 3-sphere and a 6-sphere with their
standard round metrics, equipped with the product G₂-invariant structure.
No mechanism from Categories 1–5 below can select N_gen = 3 as the fermion
generation count on M. The theorem is conditional on Category 6 being OPEN.*

**Category 1: Topological invariants of M**
- χ(M) = χ(S³) × χ(S⁶) = 0 × 2 = 0 [G27]
- p₁(M) = 0 [G27]
- c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (unit of generation, not 3) [G33]
- K̃(S⁶) = ℤ, Adams ψ^k eigenvalue = k³ for all n (no factor 3 distinguished) [G36]
- Cobordism invariants: Ω^{Spin}_6 = 0, η(S⁶) = 0 [G34-A2]

**Category 2: Representation theory / index theory**
- ind(D_{S³×S⁶}) = 0 (even-dim S⁶ contributes ind=0 for standard Dirac) [G27]
- G₂ symmetry → instanton index = 0 (G₂ forces mult(3) = mult(3̄)) [G30]
- Lichnerowicz: ρ > 0 on S³ kills low-spin adjoint spinor modes [G31]
- NCG: rank(T^{1,0}S⁶) = 3 = color, not generation count [G35]

**Category 3: String-theory and spectral mechanisms**
- WZW level on S³ (spin connection): k_{grav} = 0 (η(D_{S³}) = 0) → SU(2)₀, 1 primary [G34-B3]
- String tadpole: dim(S³×S⁶) = 9 ≠ 6; χ=0; min tadpole → c₃=2 [G37]
- Spectral action minimum: S_{spec}(c₃) monotone → min at c₃ = 2 [G38]

**Category 4: Brane and flux mechanisms on S⁶**
- H⁴(S⁶; ℤ) = 0 → no 4-form flux quantization [G34-D1]
- H⁶(S⁶; ℤ) = ℤ allows any c₃ ∈ ℤ but doesn't force c₃ = 3 [G34-D1 WEAK]
- Green-Schwarz: H⁴(S⁶) = 0 → GS trivial; also 9D ≠ 10D [G42-B4]
- Non-equivariant bundles (Pati-Salam SO(4)): c₃ = 2 from spin geometry [G39-B1]
- G₂→SU(3) SSB: c₃ = 6 allowed but not forced (π₅ exact seq) [G40-B2 WEAK]
- 3 D6-branes: rank-3 gauge but c₃ free [G41-B3 WEAK]

**Category 5: SO(8) triality via S⁷ extension**
- S³×S⁶ (G₂): triality orbit collapses to 1 class [G44]
- S³×S⁷ (SO(8)): triality orbit = 3, but single parallelization → N_gen = 1 [G45]
- No compact geometry carries all 3 triality sectors simultaneously [G46]

**Category 6: Stable bundle instantons on S⁶ (OPEN)**
- G43-B5: Harland-Nölle-Santi (2010) S⁶ instanton class
- μ ≡ 0 (slope = 0) is consistent with any c₃ — can c₃ = 6 HYM bundle be constructed?
- Revival condition: explicit HYM bundle with c₃ = 6 on S⁶
- STATUS: OPEN — neither ruled out nor confirmed

---

## Falsifiable Sub-Claims

**H_G47a (category coverage):**  
Every mechanism category except Category 6 is covered by ≥1 verified null result.  
→ Pre-registered: PASS

**H_G47b (independence):**  
The 5 covered categories are logically independent (proof of one doesn't subsume others).  
→ Pre-registered: PASS — they target different mathematical structures

**H_G47c (theorem completeness):**  
Categories 1–5 exhaust all known geometric mechanisms for N_gen selection.  
→ Pre-registered: WEAK — "known" is bounded by literature review; novel mechanisms possible

**H_G47d (the gap):**  
Category 6 (G43-B5 Harland-Nölle-Santi) is genuinely open, not secretly resolved.  
→ Pre-registered: OPEN — requires reading the paper, not currently done

---

## What This Does NOT Mean

1. Does NOT claim S³×S⁶ has no interesting physics — it predicts SM gauge structure (G16-G29)
2. Does NOT rule out N_gen=3 from novel geometric mechanisms not in our enumeration
3. Does NOT address the Furey-Hughes algebraic program
4. Does NOT claim N_gen=3 is impossible — only that it cannot arise from the tested mechanisms
5. Does NOT establish S³×S⁶ as the correct theory of everything — only maps what it cannot do

---

## Why This Matters

A theorem by exhaustion is more valuable than individual null results because:
1. It tells future researchers what NOT to try (saves effort)
2. It identifies the EXACT remaining gap (Category 6)
3. It structures the problem space for future work
4. It's publishable: "we proved S³×S⁶ geometry can't select N_gen=3 via mechanisms 1–5"
