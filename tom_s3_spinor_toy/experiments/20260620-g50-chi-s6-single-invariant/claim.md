# G50 — Single-Invariant Lemma: T1 from χ(S⁶), not from exhaustion

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
The null results G33, G37, G38, G39 are not four independent failures.
They are four routes to one root cause:

> **H²(S⁶;ℤ) = H⁴(S⁶;ℤ) = 0**
> forces c₁=c₂=0 for ANY bundle on S⁶,
> collapsing ALL Chern-class mechanisms to c₃ = ±χ(S⁶) = ±2.
> Since N_gen=3 requires c₃=6, and 6 ≠ ±2, no such mechanism can work.

This upgrades Proposition T1 from "14 null results by exhaustion" to "2 structural
lemmas + corollaries." The key algebraic identity (Whitney via Chern roots):

    c₃(Λ²(T^{0,1}E)) = c₁(E)·c₂(E) − c₃(E)

On S⁶: c₁=c₂=0 → c₃(Λ²) = −c₃(T^{1,0}) = −χ(S⁶) = −2.

**Check:** `pytest tests/test_g50_single_invariant_lemma.py -v`

**Key results:**
- χ(S⁶) = 2 (Betti: b₀=b₆=1, all others 0)
- H²(S⁶)=H⁴(S⁶)=0 → c₁=c₂=0 for any bundle (cohomological constraint)
- G33: c₃(T^{1,0}S⁶) = χ(S⁶) = 2 (Gauss-Bonnet-Chern)
- G39: c₃(Λ²(T^{0,1})) = c₁c₂−c₃ = 0−2 = −2 → |.| = χ(S⁶)
- G38: S_spec monotone → min at c₃=χ(S⁶)=2 (G38 IS G33 in energy language)
- G37: per-generation tadpole = χ(S⁶) = 2 (each gen contributes c₃=2)

**Structural form of T1 (2-lemma proof):**

Lemma 1 (χ-lemma): H²(S⁶)=H⁴(S⁶)=0 → any Chern-class mechanism gives c₃=±χ(S⁶)=±2 ≠ 6.
  → Covers G33, G37, G38, G39 simultaneously.

Lemma 2 (rigidity): round metric → unique isotropy → one spinor sector.
  → Covers G44, G46, T2 simultaneously.

**Caveat / What this does NOT mean:**
1. Does NOT cover G27 (ℤ₃ orbifold, Smith theory), G30 (G₂ symmetry), G31 (Lichnerowicz).
   Those require separate arguments — but each takes 2 lines, not new machinery.
2. Does NOT close the WEAK results (G40, G41, G45c). Those have a different structure.
3. "T1 from 2 lemmas" means the PROOF is shorter; the experiments G33-G39 remain valid.

**Status:** PASS [VERIFIED-sympy]
