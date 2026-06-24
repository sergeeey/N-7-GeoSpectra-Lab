# G91 Claim — Full 4D Reduced Action Analysis

**Date:** 2026-06-24
**Type:** Descriptive + Physical (closes G88F gap)

## Claim

The physical mass ratio m_mod/m_KK for the S³×S⁶ toy model is
frame-independent (Einstein frame = string frame), and can be computed
from the canonical Hessian (G88A) combined with the verified KK spectrum
(S³: G4, S⁶: G73), given the path constraint ρ₃ = ρ₆².

## Falsifiable sub-claims

1. **C1:** dV/d(ln ρ₃) = −3V identically → σ₃ (S³ radius) is a runaway direction
   in the 2D potential. [ANALYTICAL]

2. **C2:** The conformal factor Ω² = ρ₃³ρ₆⁶ cancels exactly in the mass ratio.
   Both m²_mod and m²_KK scale as 1/Ω² → ratio is frame-independent.
   [ANALYTICAL]

3. **C3:** With ρ₃ = ρ₆² (path constraint, C=1), the lightest KK mode at ρ₆_min
   is from S³: m_KK = (3/2)/ρ₃ = 3/(2ρ₆²), using the verified spectrum
   λ_k = (k+3/2)/ρ₃. [VERIFIED-pytest, G4]

4. **C4:** The corrected physical ratio (on-path, canonical, correct KK) differs
   from G88A proxy by a factor of ~√(ρ₆²/PATH_K×m²_KK_correct).

## What this does NOT mean

- Does NOT prove ρ₃ = ρ₆² from the potential (it is an external constraint)
- Does NOT identify physical units (M_s still unmapped to M_Pl)
- Does NOT claim the constraint path is a mass eigenstate of the full 2D Hessian
- Does NOT close the flat σ₃ direction without external stabilization
