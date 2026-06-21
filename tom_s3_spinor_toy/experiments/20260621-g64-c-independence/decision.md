# G64 Decision — C=0.986 Origin: Structural Independence

**Date:** 2026-06-21
**Verdict:** PROMOTE — ρ_min is independent of C; G62 is a zero-fit with no SM input

## Question

Is C=0.986 (g₂²/g₃² at M_Z) a free parameter of the G62 chain, or is the
prediction robust to changes in SM coupling constants?

## Structural Result

V_total(ρ, C) = C³ × [15/(16π)] × f(ρ, ρ*, λ) / (K_VOL·ρ¹²)

where f(ρ) = 1 − exp(λ(1/ρ*² − 1/ρ²)) is INDEPENDENT of C.

Since the C³ factor is a global multiplicative constant, the minimum condition
dV/dρ = 0 is INDEPENDENT of C. Therefore:

**ρ_min = 1.179 for ANY value of C** — including C=1 (no SM input needed).

## C Scan (23/23 tests pass)

| C      | Source         | ρ_min   | m_mod/m_KK | V_min       |
|--------|----------------|---------|-----------|-------------|
| 0.800  | unphysical     | 1.17906 | 1.48%     | −1.35×10⁻⁶ |
| 0.9865 | SM@M_Z (PDG)   | 1.17906 | 2.02%     | −2.53×10⁻⁶ |
| 1.000  | equal-radii    | 1.17906 | 2.07%     | −2.64×10⁻⁶ |
| 1.100  | intermediate   | 1.17906 | 2.39%     | −3.51×10⁻⁶ |
| 1.4964 | GUT g₂=g₃      | 1.17906 | 3.79%     | −8.83×10⁻⁶ |

**ρ_min = 1.17906 is IDENTICAL across all C (5 sig figs, numerical noise < 10⁻⁵).**

## Scaling Laws (algebraic identities)

- V_total(ρ, C) / V_total(ρ, C_SM) = (C/C_SM)³ — EXACT
- V_min(C) / V_min(C_SM) = (C/C_SM)³ — EXACT (same as above at ρ_min)
- m_mod/m_KK(C) = (C/0.9865)^{3/2} × 2.02% — EXACT (from V²∝C³, m²_KK ∝ 1/ρ²)

## Natural Zero-Fit: C=1

The "geometric" condition C=1 means ρ₃ = ρ₆² (equal-radii, no PDG input):
- ρ_min = 1.179 (IDENTICAL to G62)
- m_mod/m_KK = 2.07% (+2.1% from G62's 2.02%)

C_SM = 0.9865 differs from C=1 by only **1.35%** — essentially unity.

## Physical Meaning

**ρ_min is a PURE GEOMETRIC prediction** from UV-selection (ρ*) + non-perturbative
exponent (λ) alone. The SM coupling ratio g₂/g₃ determines only:
1. The DEPTH of the AdS pocket (V_min ∝ C³)
2. The MODULI MASS (m_mod/m_KK ∝ C^{3/2})

NOT the LOCATION of the minimum.

This makes G62's ρ_min = 1.179 a zero-fit prediction with zero observational input.

## What This Does NOT Mean

1. Does not derive m_mod/m_KK without SM input (it depends on C^{3/2})
2. Does not explain WHY C ≈ 0.986 (the coupling ratio at M_Z is still an input)
3. Does not apply when ρ* also varies with C (pending: G54-C scaling with C)

## Next Steps

The G62 chain now has the following input count:
- λ = 1/3 (geometric, from G61)
- ρ* = 1.090 (UV-selection, from G57)
- C = 0.986 (SM@M_Z, only affects m_ratio and V_min depth)

**ρ_min = 1.179 is zero-input.** To make m_mod/m_KK zero-input too, need to
derive C from first principles — or accept C=1 as the natural equal-radii value
giving m_mod/m_KK = 2.07%.

Candidate next: G65 — test whether ρ* also scales with C via G54-C formula
ρ*(C) = √(−A₂B₈/(A₀B₁₀C²)), and how this shifts ρ_min.
