# G54-F Decision

**Date:** 2026-06-21
**Verdict:** PROMOTE — F4.1+F4.2+F4.3+F4.4+F4.5 all PASS, 1785 tests (13 new)

Closes G54-A gate F4 (open since commit feafaae, 1696 tests).

## Results

| Gate | Claim | Result | Evidence |
|------|-------|--------|----------|
| F4.1 | V_int ∝ ρ₆¹² exactly | PASS | V_int(2)/V_int(1)=4096=2^12 to 0.01 |
| F4.2 | V^EH_Cas monotone, no local min | PASS | dV/dρ₆ > 0 at ρ₆_min=0.953; monotone at 3 points |
| F4.3 | ρ₆** preserved as zero of V^EH_Cas | PASS | |V^EH_Cas(ρ₆**)| < 1e-10; sign change [1.44,1.46] |
| F4.4 | V_flux >> ζ_FP (factor ~330) | PASS | V_total_EH > 0 at all 8 test points |
| F4.5 | Dine-Seiberg runaway on [0.7,1.5] | PASS | V_total_EH monotone decreasing; ρ₆** not V_total min |

All 13 tests pass. Full suite: 1785 passed, 2 skipped.

## EH Frame Structure — Complete Map

```
10D STRING FRAME:           ζ_FP(ρ₆) along ρ₃=0.986ρ₆²
                             
  ρ₆_min≈0.953   ρ₆*≈1.090       ρ₆**≈1.447
      ↓               ↓                ↓
   most neg       UV pole=0         ζ_FP=0
←— attractive ————————————————————→ ← repulsive →

4D EH FRAME:               V^EH_Cas = ζ_FP / V_int(ρ₆¹²)

  ρ₆_min NOT     ρ₆* NOT         ρ₆** PRESERVED
  preserved       preserved       as V^EH_Cas=0
  (minimum gone)  (just a point)  (zero survives)

←— V^EH_Cas monotone increasing —————————————→
←— V_total_EH monotone decreasing (flux dom.) →
```

## What survives Weyl rescaling

| Feature of G54-D/E | Survives to 4D EH? |
|--------------------|-------------------|
| ζ_FP < 0 on [0.7, ρ₆**) | YES — V^EH_Cas also negative there |
| Local minimum at ρ₆_min | **NO** — destroyed by ρ₆¹² denominator |
| UV special point ρ₆* | Partially — still a point on the curve, but no feature |
| Zero at ρ₆** | **YES** — algebraic identity (V_int≠0) |
| Three-radius structure | **PARTIALLY** — only the zero survives |

## Physical conclusion

The Dine-Seiberg runaway is confirmed in the studied range [0.7, 1.5]:
- Casimir energy (V^EH_Cas) is negative and small (< 0.00085/V_int)
- Freund-Rubin flux (V^EH_flux) is positive and large (0.286/V_int)
- Sum V_total_EH > 0, monotone decreasing → no stabilization from these two terms alone

Additional stabilization requires:
1. Non-perturbative: gaugino condensate, instantons
2. Geometric: orientifold planes (O-planes), D-branes with tension
3. Higher-order: α' corrections, string loop corrections

The compactification window [ρ₆_min, ρ₆**] = [0.953, 1.447] from G54-E characterizes
the range where Casimir energy is attractive in 10D. This is a necessary condition
for Casimir stabilization, but is not sufficient without additional terms.

## G54 chain summary (complete)

| Experiment | Gate | Status | Key result |
|-----------|------|--------|------------|
| G54-A | F1-F3 | PASS | V_flux = g₂²/g₃² = const on SM constraint |
| G54-A | F4 | **PASS (this commit)** | V^EH_Cas monotone; Dine-Seiberg runaway |
| G54-B | B1-B4 | PASS | ζ has pole s=−1/2; c_{1/2}=const on SM constraint |
| G54-C | C1-C3 | PASS | c_{1/2}=0 at ρ₆*≈1.09; B10 non-zero |
| G54-D | D1-D6 | PASS | ζ_FP computed; sign flip → ρ₆** ∈ (1.2, 1.5) |
| G54-E | E1-E3 | PASS | Three special radii: ρ₆_min < ρ₆* < ρ₆** = 1.4469 |
| G54-F | F4.1-F4.5 | **PASS** | ρ₆** survives EH; 10D minimum does not; Dine-Seiberg |

The G54 chain is now **complete**. All gates closed.

## Pearl gate

No new pearl from G54-F. The Dine-Seiberg result is expected for Casimir+flux alone
(standard string landscape knowledge). What IS notable:
- ρ₆** survives as a structural zero (algebraic, not numerical) — correct behavior
- The 10D three-radius structure is a property of ζ_FP, not of the 4D potential
- This is a clean diagnostic: G54-F confirms the 10D analysis (G54-D/E) is self-consistent

No addition to pearl_registry/INDEX.md needed.

## Security constraints (never violate)

- λ = FREE_COUPLING_PARAMETER (G4 Fisher rank theorem) — unchanged
- sm_derivation_claimed = False — unchanged
- No Tom Lawrence endorsement claim
