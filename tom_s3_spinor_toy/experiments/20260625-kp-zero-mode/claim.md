---
experiment_id: 20260625-kp-zero-mode
date: 2026-06-25
tier: Full-Ladder
status: in_progress
---

# claim.md — Kostant-Parthasarathy Zero-Mode Analysis

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — derivation via representation theory

NOT empirical, NOT causal. Formal derivation check is the final gate (not Consilience Score).

## Falsifiable Claim

**C1:** The only G₂-representation that can contain zero modes of D⊗S⁻ on G₂/SU(3)=S⁶
is the trivial representation (0,0), and it contributes exactly 1 zero mode.

**C2 (structural):**  
- S⁺⊗S⁻|_{SU(3)} = (1,1) ⊕ (0,1) ⊕ (1,0) ⊕ 2×(0,0)  [dim=16, ✓ via tensor product]
- S⁻⊗S⁻|_{SU(3)} = (2,0) ⊕ (0,1) ⊕ 2×(1,0) ⊕ (0,0)  [dim=16, ✓ via tensor product]

**C3 (KP bound):**  
For any non-trivial G₂-rep ρ=(m,n)≠(0,0) appearing in Γ(S⁺⊗S⁻):  
λ²(ρ) = C₂(G₂; m,n) - C₂(SU(3); σ) ≥ C₂(G₂;1,0) - C₂(SU(3);1,1) = 4 - 3 = 1 > 0

**C4 (corollary):**  
dim ker(D^+_{S⁻}) = 1, dim coker(D^+_{S⁻}) = 0  
⟹ ind(D⊗S⁻) = 1 ✓, dim ker(D_{S⁻}) = 1

## Key Definitions

- S⁶ = G₂/SU(3): nearly Kähler 6-sphere with G₂ isometry group
- S⁻|_{SU(3)} = (1,0)⊕(0,0) = 3⊕1 (negative spinor bundle, isotropy rep under SU(3)⊂G₂)
- S⁺|_{SU(3)} = (0,1)⊕(0,0) = 3̄⊕1 (positive spinor bundle)
- These follow from SU(4)⊃SU(3) branching: 4→3⊕1, 4̄→3̄⊕1
- G₂ Casimir: C₂(G₂; m,n) = (2m²+6mn+6n²+10m+18n)/3  [Bourbaki: α₁=short, α₂=long]
- SU(3) Casimir: C₂(SU(3); p,q) = (p²+pq+q²+3p+3q)/3

## Strategy (Kostant-Parthasarathy)

D_{S⁻} is G₂-equivariant → maps G₂-isotypic components to themselves.
KP formula (characteristic connection): D²|_ρ eigenvalue = C₂(G₂;ρ) - C₂(SU(3);σ)

Zero modes require: C₂(G₂;ρ) = C₂(SU(3);σ) for some SU(3)-type σ ⊂ S⁺⊗S⁻|_{SU(3)}.

Step 1: Enumerate SU(3)-types in S⁺⊗S⁻ → {(1,1),(0,1),(1,0),(0,0),(0,0)}
Step 2: Enumerate SU(3)-types in S⁻⊗S⁻ → {(2,0),(0,1),(1,0),(1,0),(0,0)}
Step 3: For each G₂-rep ρ contributing to Γ(S⁺⊗S⁻) via G₂(ρ)|_{SU(3)} ∩ S⁺⊗S⁻|_{SU(3)}:
        compute λ²(ρ) = C₂(G₂;ρ) - C₂(SU(3); matched σ)
Step 4: Show λ²(ρ) > 0 for all ρ ≠ (0,0)
Step 5: Count trivial G₂-reps: 2 in S⁺⊗S⁻ (source), 1 in S⁻⊗S⁻ (target)
Step 6: By equivariance + ind=1: rank(D^+|_{trivial}) = 1 → dim ker = 1

## Kill Condition

C1 is FALSIFIED if:
- Any G₂-rep ρ=(m,n)≠(0,0) appears in Γ(S⁺⊗S⁻) with λ²(ρ) ≤ 0
- OR if the counting of (0,0) components is wrong (2 in S⁺⊗S⁻, 1 in S⁻⊗S⁻)

## Claim Entropy (Perelman)
- N_unsupported_HIGH = 0 (S⁺/S⁻ spinor decompositions from G₁₆/G₁₇ verified tests)
- N_hidden_assumptions = 1 (KP correction from torsion — needs careful treatment)
- N_missing_negative_controls = 0
- N_ambiguous_definitions = 0
- N_unresolved_blockers = 1 (torsion correction for D^c vs D^g)

claim_entropy = 2

## Torsion Correction Note
The KP formula above is for D^c (characteristic connection).
For D^g (Levi-Civita): D^g = D^c + (torsion operator).
On the trivial G₂-representation, the torsion operator acts as c·γ(T)|_{trivial}.
Since T is G₂-invariant (the associative 3-form), γ(T): S⁻⊗S⁻ → S⁺⊗S⁻ and vice versa.
This maps between the trivial components — it does NOT change the dimension count.
Therefore dim ker(D^g_{S⁻}) = dim ker(D^c_{S⁻}) = 1. [This step needs formal verification — marked HYPOTHESIS until independently verified]
