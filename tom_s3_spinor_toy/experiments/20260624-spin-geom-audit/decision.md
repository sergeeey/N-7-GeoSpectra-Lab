# Decision — Spin Geometry Audit

**Date:** 2026-06-24
**Status:** OPTION A IMPLEMENTED — preprint.tex updated 2026-06-24
**Next action:** arXiv upload (deadline 2026-06-28)

## Summary verdict
ind=1 per channel is mathematically sound. The jump from ind=1 to N_gen=3 requires filling three gaps in L3/L4A/L4B before the claim can be considered proven.

**Current status of main claim:**
- N_gen=1 (from ind=1): VALIDATED ✓
- N_gen=3 (from triality × ind=1): HYPOTHESIS — requires L3 fix

## Options

### Option A — Честный даунгрейд (Conservative)
**Action:** Rewrite §3-4 as:
- §3: "We prove ind=1 on S⁶ via L1+L2 (validated)"
- §4: "We conjecture N_gen=3 via triality (L3 is stated as conjecture, not proved)"
- §7 Open Problems: "Making the triality argument rigorous (three explicit bundles)"

**Pros:** Immediately publishable, honest, passes referee review
**Cons:** Main headline claim weakened ("N_gen=1 proved, 3 conjectured")
**Effort:** Low (1-2 days, mostly rewriting)
**Risk:** Low

### Option B — Исправить L3/L4A/L4B (Strong)
**Action:** 
1. L3 fix: Construct three explicit G₂-equivariant bundles E₀=S⁻⊗ρ₀, E₁=S⁻⊗ρ₁, E₂=S⁻⊗ρ₂ where ρ₀,ρ₁,ρ₂ are the three 1-dimensional Z₃-representations. Compute ind(D⊗Eₐ)=1 for each. This requires Tom Lawrence's input on the explicit bundle construction.
2. L4A fix: Replace "R/4 > |F| → gap" with explicit spectral calculation (Cahen-Gutt 1988, or Bär's Dirac spectrum on G₂/SU(3)).
3. L4B fix: Replace fibre-multiplicity Schur argument with G₂-equivariant index theorem + character computation.

**Pros:** Main claim N_gen=3 fully proved
**Cons:** Needs Tom's collaboration + literature dig (weeks)
**Effort:** Medium-High (requires specialist)
**Risk:** Medium (L3 fix may change the structure)

### Option C — Подождать Тома (Practical)
**Action:** Submit as-is with explicit open problems note, then:
- Email Tom with the three gaps
- Let him propose the bundle construction (his territory)
- Version 2 on arXiv with full proof

**Pros:** Meets arXiv deadline 2026-06-28, gets feedback from community
**Cons:** Risk that referee immediately flags the same gaps
**Effort:** None now
**Risk:** Medium (community may interpret claim as more certain than it is)

## Skeptic audit metadata
- Audit method: context-asymmetric (claim.md + preprint §3-4 only)
- Auditor: Claude Sonnet 4.6 skeptic agent
- Auditor had: NO session history, NO success narrative, NO reasoning chain
- Evidence level: [HYPOTHESIS] — LLM audit, needs human specialist confirmation
- Next step before treating as VERIFIED: independent review by human with spin geometry background

## Kill Analysis (per FL protocol)
**What was killed:** The claim that L3+L4A+L4B as currently written constitute a complete proof of N_gen=3
**What was NOT killed:** 
- ind=1 result (L1+L2)
- The uniqueness of S⁶ among NK6 (Butruille classification argument)
- The physical interpretation (chirality, quantum numbers, §2)
- The λ-obstruction (§6, Buckingham Pi)

## Literature Search Results (2026-06-24 — lit-search via sci-pipeline)

### Papers found and read

**Agricola, Hofmann, Lawn 2023** — "Invariant Spinors on Homogeneous Spheres"
- arXiv: 2203.02961 | DOI: 10.1016/j.difgeo.2023.102014
- **Theorem 5.1** (page 42): S⁶=G₂/SU(3) has exactly **2 G₂-invariant Killing spinors**:
  Σ_inv = span_ℂ{1, y₁∧y₂∧y₃}, with ψ± = 1 ± y₁∧y₂∧y₃, ∇^g_X ψ± = ±(1/2√3) X·ψ±
- **Relevance to L4B:** Confirms the complete SU(3)-invariant spinor structure at the fibre level.
  Supports the representation-theoretic claim. Does NOT directly compute dim ker(D_{S⁻}).
- **What it does NOT give:** Twisted Dirac spectrum; kernel of D_{S⁻} on Γ(Σ⊗S⁻).

**Agricola 2002** — "Connections on Naturally Reductive Spaces, Their Dirac Operator"
- arXiv: math/0202094 | DOI: 10.1007/s00220-002-0743-y
- **Theorem 3.3** (Kostant-Parthasarathy): general formula for (D^t)² on G/H via Casimir operators
- **Theorem 4.2:** Constant (G-invariant) spinors are eigenspinors of (D^t)² with eigenvalue
  9t²[Q(ρ_g,ρ_g) - Q(ρ_h,ρ_h)] > 0 — so they are NOT zero modes of D^{LC}
- **Relevance to L4A:** Provides the correct framework (Casimir formula) for computing D² on
  naturally reductive spaces including S⁶=G₂/SU(3). Does NOT compute ker(D_{S⁻}).
- **What it does NOT give:** Twisted Dirac spectrum; no formula for D⊗E on G/H.

### Gap status after lit-search

| Gap | Before search | After search | Remaining need |
|-----|---------------|--------------|----------------|
| L3 (triality Z₃) | OPEN | OPEN | Explicit G₂-equivariant bundles E₀,E₁,E₂ |
| L4A (Lichnerowicz) | OPEN | PARTIALLY CLARIFIED | Agricola 2002 framework exists; computation not done for D_{S⁻} |
| L4B (Schur on L²) | OPEN | PARTIALLY IMPROVED | Agricola 2023 Thm 5.1 cited; connection to ker(D_{S⁻}) still informal |

### Conclusion
**Neither paper directly computes dim ker(D_{S⁻}) = 1 on S⁶=G₂/SU(3).**

The index ind = 1 is proved. That dim ker = 1 (coker = 0) requires:
- Either explicit spectral computation of D_{S⁻} on G₂/SU(3) (representation theory)
- Or a Serre duality argument showing ker(D*_{S⁻}) = 0

This is doable but not in 4 days without Tom Lawrence's input.

**Recommended action: Option A (downgrade to honest claim) + new citations**

## Updated Options (post lit-search)

### Option A (DONE 2026-06-24) — Честный даунгрейд + новые цитаты
**Changes made:**
1. ✅ Abstract: "We prove N_gen=3 exactly" → "We prove ind=1; We conjecture N_gen=3"
2. ✅ §4 title: "Exact Kernel Count" → "Chirality and Open Kernel-Count Problem"
3. ✅ §4.1 L4A: replaced self-contradictory Lichnerowicz argument with honest open problem
4. ✅ §4.2 L4B: replaced invalid Schur argument with partial fibre result + open problem
5. ✅ Corollary: "Exact kernel" → "Exact kernel, conditional"
6. ✅ §6.3 Open Problems: added explicit items for L3, L4A, L4B
7. ✅ Bibliography: added AgrHofLawn2023 (arXiv:2203.02961) + Agricola2002 (arXiv:math/0202094)
8. ✅ date: removed \textcolor{red}{NOT FOR DISTRIBUTION}
9. ✅ CCM table: "Derived" → "Conjectured"

**Verification:** 14/14 checks passed. Tests: 2296 (no changes to .py files)
**Risk:** Very low

### Option B (MEDIUM TERM) — Full proof with Tom Lawrence
Unchanged from before. Weeks, needs Tom's bundle construction expertise.

### Option C — Submit as-is
NOT recommended after this audit. Referee will flag same gaps.

## Pearl Gate check
**Pearl:** Agricola 2002 Section 3.3 gives Kostant-Parthasarathy formula for ALL naturally
reductive spaces. This could be used for a future experiment computing the full spectrum
of D_{S⁻} on G₂/SU(3) via representation theory of G₂ (without numerical methods).
Falsifiable prediction: the formula should give eigenvalue 0 exactly for the twisted kernel
mode corresponding to our index = 1.
pearl_registry entry: G₂/SU(3) twisted Dirac spectrum via Kostant-Parthasarathy → CANDIDATE
