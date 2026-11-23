# S6-HARM-G5: Decision

**Date:** 2026-06-15
**Verdict:** PROMOTE
**Evidence:** 17/17 sympy checks + 14/14 pytest + 507 total PASS

## Result summary

Cartan structure equations verified for all three (β_k,φ_k) pairs on S⁶.

Universal coordinate spin connection law confirmed:
```
ω^{φ_k}_{β_k, φ_k}(coord) = cosβ_k    for k = 1, 2, 3
```

Frame forms (dividing by h_{φ_k}):
| k | h_{φ_k} | ω^{φ_k}_{β_k}(coord) | ω^{φ_k}_{β_k}(frame) |
|---|---------|----------------------|----------------------|
| 1 | ρ sinβ₁ | cosβ₁ | cotβ₁/ρ |
| 2 | ρ cosβ₁ sinβ₂ | cosβ₂ | cotβ₂/(ρ cosβ₁) |
| 3 | ρ cosβ₁ cosβ₂ sinβ₃ | cosβ₃ | cotβ₃/(ρ cosβ₁ cosβ₂) |

## cotβ_k universality chain — S6-HARM closure

| Gate | cotβ_k appears as | Role |
|------|-------------------|------|
| G2 | Root generator L_{1j}: φ_k-component = cotβ_k × (factor) | Frame artifact in SO(6) harmonics |
| G3 | Scalar ODE centrifugal term: l_k(l_k+1)/cos²β_k | Drives eigenvalue nesting |
| G4 | Lichnerowicz ±(l+3)/ρ shift; 3 = n/2 = #(β_k,φ_k) pairs | Dirac ground state |
| G5 | ω^{φ_k}_{β_k}(coord) = cosβ_k → frame cotβ_k/ρ | Spin connection source |

The same cotβ_k coefficient appears at every level: algebra (G2), analysis (G3), spectral theory (G4),
and Riemannian geometry (G5). This is a structural feature of the Hopf-type nested coordinate system,
not specific to any one computation.

## What this does NOT mean

- Does NOT complete the Killing spinor check (∇_μψ = ±(1/2ρ)Γ_μψ requires off-diagonal ω)
- Does NOT compute the off-diagonal spin connection components
  ω^{β_k}_{β_{k'}} (tanβ_k cross-terms) or ω^{φ_k}_{β_{k'}} (cross-nesting)
- Does NOT show that spinor harmonics satisfy the same ODE structure as G3 scalar harmonics
- Does NOT fix λ or select any compactification
- Does NOT connect this to Tom Lawrence S³ (different dimension, different Killing count)

## Next steps (open, not committed)

- Close S6-HARM branch (G0→G5 complete) and summarize for Tom update
- Tom Lawrence correspondence: await reply on rows 17+19 before S³ structure changes
- ACH matrix: G4/G5 close λ-identifiability evidence chain

---

## Addendum 2026-11-03: strength of the evidence (registry audit; the text above is unchanged)

Re-read of `s6_harm_g5_spin_connection.py` ([VERIFIED-tool], by reading the code, not by rerunning):

- T1-T5 (13 of the 17 checks) test the Cartan structure equations for the three (beta_k, phi_k) pairs and the coordinate/frame forms of omega. These support the stated
  law omega^{phi_k}_{beta_k}(coord) = cos beta_k and its frame form, for the diagonal pairs only.
- T6 (3 checks) compares the frame coefficient with cot beta_k, which T5 already established; it does not compute the G2 root-generator expression.
  It therefore does not establish "same coefficient as G2" (claim C5) as an independent result.
- T7 (1 check) is `dirac_shift == cotbk_pair_count` with `dirac_shift = 6 // 2` and `cotbk_pair_count = 3` both fixed in the script, i.e. a tautology.
  It does not derive the +3 shift of the Dirac spectrum (claim C6); that shift rests on G4.
- So "17/17" is 13 independent checks plus 4 that restate or assume. The "cot beta_k universality chain" across G2-G5 is a statement about the form of one coefficient, not a derivation linking the four levels.
- No later experiment cites this result (searched `experiments`, `tests`, `scripts`).

Ledger: none-because: single-script result, not carried into CLAIM_LEDGER (add a claim only with the strength above)
Follow-ups: none
