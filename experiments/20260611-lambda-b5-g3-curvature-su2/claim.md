# LAMBDA-B5-G3 — Spinorial curvature generates su(2) on unit S³

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**  
On unit S³ (K=+1), the spinorial curvature operator `F_{ab} = [∇_a, ∇_b]` satisfies:
```
F_{ab} = (1/4) R_{abcd} γ^c γ^d = (1/4)[γ_a, γ_b] = (i/2) ε_{abc} γ^c
```
The generators `J_a = F_{bc} ε_{abc}` form the Lie algebra su(2) with Casimir `−(3/4)I` (spin-1/2 rep).

**Connection to G2:**  
Curvature `R_{abcd} = δ_{ac}δ_{bd} − δ_{ad}δ_{bc}` (K=+1) confirmed by G2 T11–T13 via `R^{ab} = e^a ∧ e^b`.

**Checks performed (9/9 PASS):**
- T1: `[γ^a, γ^b] = 2i ε^{abc} γ^c` — Clifford commutators [9 entries]
- T2: `R_{1212} = 1` — sectional curvature K=+1 consistent with G2
- T3a: `F_{12} = (1/4)R_{12cd}γ^cγ^d = (i/2)γ^3` — explicit component
- T3b: `F_{ab} = (1/4)[γ^a, γ^b]` for all a,b [9 entries]
- T4: `F_{ab} = −F_{ba}` — antisymmetry
- T5: `[J_a, J_b] = −ε_{abc}J_c` — anti-Hermitian su(2) algebra (`J_a = (i/2)σ_a`)
- T6: `J_a† = −J_a` — anti-Hermitian generators of su(2)_L
- T7: `ΣJ_a² = −(3/4)I` — Casimir value for j=1/2 spin-1/2 rep
- T8: `[∇₁, ∇₂] = (i/2)γ^3` — explicit spinorial curvature component

**Convention note:**  
The generators `J_a = (i/2)σ_a` are anti-Hermitian (mathematician's convention).
Their algebra is `[J_a, J_b] = −ε_{abc}J_c`, which is su(2) in the anti-Hermitian basis.
Equivalent to physicist's convention `[T_a, T_b] = iε_{abc}T_c` via `T_a = iJ_a`.

**Verdict:** PASS_SU2_CURVATURE_CONFIRMED [VERIFIED-sympy 9/9, 2026-06-11]

**Caveat / What this does NOT mean:**
- Does NOT fix λ (coupling constant) — λ = FREE_COUPLING_PARAMETER
- Does NOT select a physical spin structure
- Does NOT mean GEOMETRY_AGNOSTIC is lifted
- Does NOT imply safe_for_runtime = True
- Curvature is purely geometric (K=+1 unit S³); no dynamical statement

**Status:** CLOSED PASS_SU2_CURVATURE_CONFIRMED
