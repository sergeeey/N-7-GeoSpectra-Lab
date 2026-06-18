# G15 — Claim: B−L quantum number from S⁶ spinor geometry

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The B−L quantum number on the 8-dimensional S⁶ spinor is

  B−L = −(1/3)(σ₃^{(1)} + σ₃^{(2)} + σ₃^{(3)}) = (2H−3)/3

where σ₃^{(k)} is σ₃ on the k-th qubit of the Kronecker basis |i₁i₂i₃⟩ and H is the
Hamming weight operator. This operator:

1. **Commutes with all SU(3)_color generators** → U(1) quantum number
2. **Is proportional to lift_to_spinor(J)** where J = M₀₁+M₂₃+M₄₅ is the almost-complex
   structure defining SU(3) ⊂ SO(6) — i.e. B−L is the spinor representation of the U(1)
   center of u(3) = su(3) ⊕ u(1)
3. **Assigns correct SM values** by Hamming weight:

   | Hamming | Indices | SU(3) | B−L | Sector |
   |---------|---------|-------|-----|--------|
   | 0 | \|000⟩ | 1 | −1 | lepton singlet (S^+) |
   | 2 | \|011⟩,\|101⟩,\|110⟩ | **3** | **+1/3** | quarks (S^+) |
   | 1 | \|001⟩,\|010⟩,\|100⟩ | **3̄** | **−1/3** | antiquarks (S^-) |
   | 3 | \|111⟩ | 1 | +1 | G13 zero mode (S^-) |

4. **Satisfies Gell-Mann–Nishijima**: Y = T3R + (B−L)/2 with T3R = ±1/2 from S³ K-generators

## Gates summary

All 12/12 gates PASS [VERIFIED-sympy, 2026-06-19]:

| Gate | Content | Result |
|------|---------|--------|
| T1 | B−L is diagonal | PASS |
| T2 | B−L = (2H−3)/3 where H = Hamming weight operator | PASS |
| T3 | [B−L, Γ₇] = 0 (compatible with chirality) | PASS |
| T4 | [B−L, C^spin_i] = 0 for all 8 SU(3) generators | PASS |
| T5 | Quarks {3,5,6}: B−L = +1/3 | PASS |
| T6 | Antiquarks {1,2,4}: B−L = −1/3 | PASS |
| T7 | Singlets: \|000⟩ → −1, \|111⟩ → +1 | PASS |
| T8 | lift_to_spinor(J) = −(3i/2)·B−L | PASS |
| T9 | Y = (B−L)/2 for T3R=0: lepton singlet Y=−1/2 | PASS |
| T10 | Gell-Mann–Nishijima for all 4 right-handed SM fermions | PASS |
| T11 | B−L constant within each SU(3) sector (Schur), distinct across | PASS |
| T12 | B−L is Hermitian (physical observable) | PASS |

## Key geometric identity (T8)

The almost-complex structure J = M₀₁+M₂₃+M₄₅ is the U(1) center of u(3) = su(3)⊕u(1).
Its spinor lift:

  lift_to_spinor(J) = J_spin(1,2) + J_spin(3,4) + J_spin(5,6)
                    = (i/2)(σ₃^{(1)} + σ₃^{(2)} + σ₃^{(3)})
                    = −(3i/2) · B−L

So B−L = (2i/3) · lift_to_spinor(J) — the B−L charge is EXACTLY the Hermitian
observable derived from the almost-complex structure J. No separate U(1) is introduced;
it comes from the geometric structure J that already defines SU(3) ⊂ SO(6).

## Gell-Mann–Nishijima table

| Fermion | B−L | T3R | Y = T3R + (B−L)/2 |
|---------|-----|-----|-------------------|
| ν_R | −1 | +1/2 | 0 ✓ |
| e_R | −1 | −1/2 | −1 ✓ |
| u_R | +1/3 | +1/2 | +2/3 ✓ |
| d_R | +1/3 | −1/2 | −1/3 ✓ |

T3R comes from the S³ K-generators (G11). The S³ × S⁶ product structure
naturally factorises Y into a purely S³ piece (T3R) and a purely S⁶ piece (B−L/2).

## Check

`python g15_hypercharge.py` → `PASS_G15_BL_GEOMETRIC_ORIGIN` (12/12)
`pytest tests/test_g15_hypercharge.py` → 23 passed
`pytest tests/` → 850 passed, 2 skipped

## What this does NOT mean

1. Does NOT fix λ — λ = FREE_COUPLING_PARAMETER throughout.
2. Does NOT fully derive Y from first principles — T3R requires the S³ K-generators
   whose eigenvalues (±1/2 for right-handed fermions) are verified in G11 but not
   derived from a topological/index argument analogous to G13.
3. Does NOT show quarks/leptons are physical states — only their quantum numbers
   (B−L, Y) are assigned. Dynamics, masses, and couplings are not addressed.
4. Does NOT prove the SM is complete — this is one generation, without the second/third
   generation or the Higgs mechanism.
5. The proportionality B−L ∝ lift_to_spinor(J) holds in the S⁶ spinor basis;
   it is a claim about quantum numbers, not about the J-twisting of the gauge field
   (Tom's open problem, G10-B).
6. Does NOT establish whether this B−L is conserved in the full S³×S⁶ compactification
   — that requires the coupling between the two sectors (λ-dependent).
7. sm_derivation_claimed = False throughout.

## Connection to prior gates

| Gate | Result | G15 connection |
|------|--------|----------------|
| G10-B | SU(3) ⊂ SO(6) via J-preserving constraint; u(1)=span{J} | J is the B−L generator in spinor rep |
| G11 | K-generators = SU(2)_R on S³ | T3R = K₃ eigenvalues; Y=T3R+(B−L)/2 |
| G12 | Anomaly cancellation for full 32-component spinor | B−L assignments consistent with 1+3+3̄+1 anomaly cancellation |
| G13 | G13 zero mode = \|111⟩ singlet, B−L=+1 | G15 assigns B−L=+1 to this state |
| G14 | Quark triplet {3,5,6} in S^+ sector | G15 assigns B−L=+1/3 to these quarks |

**Status:** PASS_G15_BL_GEOMETRIC_ORIGIN
[VERIFIED-sympy, 2026-06-19, 12/12 gates, 23 tests]
