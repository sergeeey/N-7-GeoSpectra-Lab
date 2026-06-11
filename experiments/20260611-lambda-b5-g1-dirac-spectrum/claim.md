# LAMBDA-B5-G1 — Canonical Dirac spectrum on unit S³

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**  
On the unit S³ with left-invariant Maurer-Cartan frame, the canonical (self-adjoint) Dirac operator
`D_phys = −i γ^a ∇_a` acting on spinors has spectrum `±(n + 3/2)` for `n = 0, 1, 2, ...`.
The lowest eigenvalue is `±3/2`.

**Spinorial connection derivation:**  
From G2 (T14): the MC structure constant ratio `dσ₃/(σ₁∧σ₂) = 2` (integer, frame-invariant).  
This gives `ω_{a,bc} = ε_{abc}` and therefore `Γ_a = (1/4) ω_{a,bc}[γ^b, γ^c] = (i/2) γ^a`.

**Checks performed (10/10 PASS):**
- T1: `{γ^a, γ^b} = 2δ^{ab}I` — Clifford algebra [9 entries]
- T2: `Σ(γ^a)² = 3I` — sum rule
- T3: `Γ_a = (i/2)γ^a` derived from `ω_{a,bc}[γ^b,γ^c]` [G2 k=2]
- T4: `D_raw(const) = γ^a Γ_a = (3i/2)I` — raw (skew-Hermitian) action on constant spinor
- T5: `D_phys = −i D_raw → (3/2)I` — physical eigenvalue λ₀ = +3/2
- T6: anti-Killing direction → λ₀ = −3/2
- T7: `D_phys² = (9/4)I` — Lichnerowicz lower bound
- T8: `Γ_a† = −Γ_a` — anti-Hermitian connection → `D_phys` self-adjoint
- T9: spectrum gaps `λ_{n+1}² − λ_n² = 2n+4` for n=0..4 [spectrum formula verified]
- T10: Lichnerowicz: `∇*∇ + R/4 = 3/4 + 3/2 = 9/4` [R=6, unit S³]

**Convention note:**  
`D_raw = γ^a ∇_a` gives imaginary eigenvalue `(3i/2)` for constant spinors because `Γ_a = (i/2)γ^a`
is anti-Hermitian. The physical self-adjoint operator is `D_phys = −iγ^a∇_a`.

**Connection to numerics:**  
`λ₀ = 3/2` matches `k0_disc(N=4000) = 1.4999999561` [BG-H1-E1, VERIFIED-pytest 2026-06-10].

**Verdict:** PASS_DIRAC_SPECTRUM_CONFIRMED [VERIFIED-sympy 10/10, 2026-06-11]

**Caveat / What this does NOT mean:**
- Does NOT fix λ (coupling constant) — λ = FREE_COUPLING_PARAMETER
- Does NOT select a physical spin structure (m∈ℤ vs m∈ℤ+½ fork open)
- Does NOT mean GEOMETRY_AGNOSTIC is lifted — this result holds on any S³ background
- Does NOT imply safe_for_runtime = True

**Status:** CLOSED PASS_DIRAC_SPECTRUM_CONFIRMED
