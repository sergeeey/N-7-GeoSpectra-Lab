# S6-HARM-G5: Spin Connection on S⁶ — cotβ_k Universality

**Date:** 2026-06-15
**Gate:** G5 — spin connection from Cartan structure equations; cotβ_k as universal frame artifact
**Depends on:** G1 PASS (vielbein), G2 PASS (cotβ_k in root generators), G3 PASS (cotβ_k in ODEs), G4 PASS (Dirac spectrum)

## Physical motivation

G2: The root generators L_{ij} contain cotβ_k in their φ_k-components — identified as a FRAME ARTIFACT.
G3: The same cotβ_k enters the scalar Laplacian ODEs as centrifugal terms l(l+1)/cos²β_k.
G4: The Dirac spectrum is ±(l+3)/ρ via the Lichnerowicz formula.

G5 asks: where does the +3 shift in the Dirac eigenvalue come from geometrically?
Answer: from the spin connection ω^{φ_k}_{β_k}, which contains EXACTLY the same cotβ_k structure.
Three Cartan pairs (β_k,φ_k) × (1/2 per pair) = 3/2? No — it gives exactly +3 via a different counting.

## Question type: Descriptive

## Vielbein (from G1 metric)

```
e^{β₁} = ρ dβ₁
e^{φ₁} = ρ sinβ₁ dφ₁
e^{β₂} = ρ cosβ₁ dβ₂
e^{φ₂} = ρ cosβ₁ sinβ₂ dφ₂
e^{β₃} = ρ cosβ₁ cosβ₂ dβ₃
e^{φ₃} = ρ cosβ₁ cosβ₂ sinβ₃ dφ₃
```

## Spin connection claims (Cartan: de^a + ω^a_b ∧ e^b = 0)

### C1: (β₁,φ₁) sector
```
de^{φ₁} = ρ cosβ₁ dβ₁ ∧ dφ₁

ω^{φ₁}_{β₁}(coord)  = cosβ₁ dφ₁           [coordinate form]
ω^{φ₁}_{β₁}(frame)  = (cotβ₁/ρ) e^{φ₁}    [frame form]

Cartan check: de^{φ₁} + cosβ₁ dφ₁ ∧ ρdβ₁ = ρcosβ₁ dβ₁∧dφ₁ - ρcosβ₁ dβ₁∧dφ₁ = 0 ✓
```

### C2: (β₁,β₂) cross-sector (only involves β angles)
```
de^{β₂} = -ρ sinβ₁ dβ₁ ∧ dβ₂

ω^{β₂}_{β₁}(coord)  = -sinβ₁ dβ₂           [tanβ₁ structure]
ω^{β₂}_{β₁}(frame)  = (-tanβ₁/ρ) e^{β₂}

Cartan check: de^{β₂} + (-sinβ₁ dβ₂) ∧ ρdβ₁ = -ρsinβ₁ dβ₁∧dβ₂ + ρsinβ₁ dβ₁∧dβ₂ = 0 ✓
```

### C3: (β₂,φ₂) sector
```
de^{φ₂} = -ρ sinβ₁ sinβ₂ dβ₁ ∧ dφ₂ + ρ cosβ₁ cosβ₂ dβ₂ ∧ dφ₂

Two spin connection components contribute:
ω^{φ₂}_{β₁}(coord) = -sinβ₁ sinβ₂/(cosβ₁) × dφ₂   [tanβ₁ cross-term]
ω^{φ₂}_{β₂}(coord) = cosβ₂ dφ₂                      [cotβ₂ structure]

Coordinate form: ω^{φ_k}_{β_k,φ_k} = cosβ_k  for k = 1, 2, 3
```

### C4: Universal cotβ_k law (coordinate form)
```
ω^{φ_k}_{β_k, φ_k}(coord) = cosβ_k    for k = 1, 2, 3
```
The COORDINATE spin connection components cosβ_k are the same for all three Cartan pairs.

### C5: Connection to G2 cotβ_k (frame form comparison)
```
G2 root generator L_{1j} φ₁-component: cotβ₁ × (angular factor)
G5 spin connection frame component:     cotβ₁/ρ × e^{φ₁}

Same cotβ_k coefficient — SAME frame artifact
```

### C6: Dirac spectrum shift count
```
Three cotβ_k pairs × (cotβ contribution per pair) → n/2 = 3 shift in Dirac eigenvalue
G4 result ±(l+3)/ρ confirmed by: scalar eigenvalue structure + 3/ρ spin connection shift
```

## Falsification criteria
- Any de^{φ_k} + ω^{φ_k}_{β_k} ∧ e^{β_k} ≠ 0 → FAIL (Cartan equation wrong)
- ω^{φ_k}_{β_k,φ_k}(coord) ≠ cosβ_k → FAIL
- Frame component ≠ cotβ_k/(ρ × nesting factor) → FAIL
- cotβ_k coefficient in ω differs from G2 root generator φ_k-coefficient → FAIL

## What this does NOT mean
- Does NOT complete the Killing spinor verification (requires full ∇_μψ = ±(1/2ρ)Γ_μψ check)
- Does NOT compute the off-diagonal ω components (e.g., ω^{β₂}_{β₁}, ω^{β₃}_{β₁,β₂})
  — those exist but don't carry the cotβ_k structure
- Does NOT show that spinor harmonics satisfy G3-type ODEs (they DON'T directly)
- Does NOT fix λ or select compactification
