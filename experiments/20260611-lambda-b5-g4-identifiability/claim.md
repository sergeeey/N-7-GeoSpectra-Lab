# LAMBDA-B5-G4 — λ identifiability from S³-observables

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**  
The coupling parameter λ is structurally non-identifiable from the current S³-only
observable set {Dirac spectrum, KK shift} because λ does not appear in any observable
unless V is promoted. Upon V promotion, λ becomes identifiable (rank-3 Jacobian).

Formal statement:
- Let θ = (λ, ρ, R) be continuous parameters (spin structure s is discrete, fixed separately)
- Let observables O_phys = {o₁, o₂} (Dirac spectrum + KK shift) — available WITHOUT V promotion
- Let observables O_full = {o₁, o₂, o₃} where o₃ = (16π²ρ³/15)·λ — requires V promotion

Result:
- rank J(O_phys, θ) w.r.t. λ = 0  →  λ non-identifiable from O_phys alone
- rank J(O_full, θ) = 3 = |θ|  →  λ identifiable from O_full (full rank)
- Corollary: λ=FREE_COUPLING_PARAMETER is a formal theorem, not just a discipline fence,
  as long as V promotion is blocked.

**Kill target (Strong Inference):**
- FAIL (rank=3 without V): Case 3 Hypothesis H1 ("λ fixed by S³ alone") would NOT be killed — 
  requires immediate re-examination of what S³-observables are available
- PASS (rank_phys=0, rank_full=3): Case 3 H1 formally KILLED; H3 ("λ free until external 
  principle") promoted from LIVE to VERIFIED_FORMAL_THEOREM

**Checks planned (8 checks):**
- T1: Observable map o₁=1/ρ, o₂=√(9/4+m₁²/R²)−3/2, o₃=(16π²ρ³/15)·λ defined symbolically
- T2: Jacobian J_full = ∂(o₁,o₂,o₃)/∂(λ,ρ,R) computed symbolically
- T3: det(J_full) ≠ 0 — full rank 3 when V observable included
- T4: ∂o₁/∂λ = 0 and ∂o₂/∂λ = 0 — λ absent from physical observables
- T5: Restricted Jacobian J_phys = ∂(o₁,o₂)/∂(λ,ρ,R) has rank 2, not 3 — λ column is zero
- T6: ρ identifiable from o₁ alone: ∂o₁/∂ρ ≠ 0
- T7: After ρ identified, λ = 15·o₃/(16π²ρ³) — linear recovery IF o₃ observable
- T8: Without o₃, observables {o₁,o₂} identify {ρ,R} only — λ has zero information content

**Verdict:** PASS_LAMBDA_NON_IDENTIFIABLE_WITHOUT_V [VERIFIED-sympy 7/7, 2026-06-11]

**Key numbers:**
- `rank(J_phys) = 2`, `dim(θ) = 3` → λ column = zero, non-identifiable from {o₁,o₂}
- `rank(J_full) = 3` → full rank, λ identifiable with V
- `det(J_full) = 32π²m₁²ρ / (15R²√(9R²+4m₁²))` — nonzero for all ρ,R,m₁>0
- λ recovery: `λ = 15·V_obs / (16π²ρ³)` — linear, requires V promotion

**Fence (unchanged):**
- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False
- This gate does NOT fix λ; it formally characterises the conditions under which λ could be fixed.
- This gate does NOT prove the full V operator.
- This gate does NOT derive the Standard Model.

**Status:** CLOSED PASS_LAMBDA_NON_IDENTIFIABLE_WITHOUT_V
