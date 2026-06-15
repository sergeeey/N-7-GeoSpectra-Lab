# G7 — Claim: S³×S⁶ Kaluza-Klein mass spectrum

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:** The Dirac mass spectrum on S³×S⁶ is given by
`M²_{mn} = (m+3/2)²/ρ₃² + (n+3)²/ρ₆²`, with no zero modes (Lichnerowicz).
The lightest KK level (m=0, n=0) carries all 32 SM states from G6.
The first S³ excitation raises M² by 4/ρ₃²; the first S⁶ excitation by 7/ρ₆².

**Check:** `python g7_kk_spectrum.py` → `PASS_G7_KK_SPECTRUM`

**Key results (exact, sympy):**
- M²(0,0) = 9/(4ρ₃²) + 9/ρ₆²    ← lightest level, all SM content
- M²(1,0) = 25/(4ρ₃²) + 9/ρ₆²   ← first S³ excitation
- M²(0,1) = 9/(4ρ₃²) + 16/ρ₆²   ← first S⁶ excitation
- ΔM²(S³) = 4/ρ₃²  |  ΔM²(S⁶) = 7/ρ₆²
- M²(1,0)/M²(0,0) = 61/45 at ρ₃=ρ₆
- S³ vs S⁶ excitation crossover: ρ₆/ρ₃ = √(7/4) ≈ 1.32

**Caveat / What this does NOT mean:**
1. NO zero modes exist on pure round S³×S⁶ (Lichnerowicz theorem — positive curvature)
2. "Lightest level carries SM content" means representation-theoretically (from G6), NOT that these are the physical massless fermions
3. Physical zero modes require additional structure: Hosotani mechanism (BG-H1), warping, or twisted gauge bundle
4. The radii ρ₃, ρ₆ are NOT fixed here — they are free parameters
5. The three-generation question is not addressed

**Correction note:** Earlier message claimed ρ₆/ρ₃ = 2 gives zero modes via eigenvalue cancellation.
This was WRONG. The product Dirac operator formula gives M² = λ₃² + λ₆² (always positive).
The "crossover at ρ₆/ρ₃ = √(7/4)" is about which KK excitation (S³ or S⁶) is lighter, not about zero modes.

**Inputs from prior gates:**
- S³ spectrum: from Tom's work (rows 5-6), verified P5/G2
- S⁶ spectrum: ±(n+3)/ρ₆ — G4 PASS [VERIFIED-sympy]
- SM state content: G6 PASS [VERIFIED-sympy 32/32]

**Status:** PASS_G7_KK_SPECTRUM [VERIFIED-sympy, 2026-06-15, 12/12 pytest]
