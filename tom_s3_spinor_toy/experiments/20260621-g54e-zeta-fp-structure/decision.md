# G54-E Decision

**Date:** 2026-06-21
**Verdict:** PROMOTE — E1+E2+E3 all PASS, 1772 tests (12 new)

## Results

| Gate | Claim | Result | Evidence |
|------|-------|--------|----------|
| E1 | ζ_FP local min at ρ₆_min ≈ 0.953 | PASS | derivative sign change (0.85,1.05) |
| E2 | ζ_FP = 0 at ρ₆** ≈ 1.4469 | PASS | brentq in (1.44,1.46), tol=1e-4 |
| E3 | ρ₆_min < ρ₆* < ρ₆** ordered | PASS | three-point summary test |

All 12 tests pass. Full suite: 1772 passed, 2 skipped.

## Three Special Radii — Complete Map

Along SM constraint ρ₃ = 0.986 ρ₆²:

```
ρ₆_min ≈ 0.953     ρ₆* ≈ 1.090          ρ₆** ≈ 1.447
    |                   |                     |
    ↓ most negative     ↓ UV pole = 0         ↓ ζ_FP = 0
ζ_FP ≈ −0.000863   ζ_FP ≈ −0.000798     ζ_FP = 0

←——— Casimir attractive ——————————————————→←repulsive→
```

- For ρ₆ < ρ₆_min: ζ_FP → −∞ as ρ₆→0 (A₂·B₁₀/ρ₆² divergence in Σ')
- Plateau [0.7, 1.2]: ζ_FP ≈ −0.00085 (roughly flat within ×1.1)
- For ρ₆ > ρ₆**: ζ_FP > 0 (repulsive Casimir regime)

## Physical Interpretation (descriptive)

- ρ₆** is the transition from attractive to repulsive Casimir. Any dynamical mechanism
  that stabilizes at Casimir zero would select ρ₆**.
- ρ₆_min is where Casimir attraction is strongest; a Casimir-dominated potential
  would prefer this radius (before any competition from flux or gravitational terms).
- ρ₆* (from G54-C) is UV-special: no counterterm needed. This means ζ_FP is the
  PHYSICAL Casimir energy (no renormalization ambiguity) at exactly this radius.

## Ratio ρ₆**/ρ₆*

ρ₆**/ρ₆* ≈ 1.328.
- Not √2 = 1.414 (diff 0.086)
- Not 4/3 = 1.333 (diff 0.005 — closest simple fraction, but ≥ B₁₂ correction needed to confirm)
- Not 3^{1/3} in the ratio; ρ₆** itself ≈ 3^{1/3} = 1.442 to 0.3% accuracy
- [WEAK] candidate: ρ₆** ≈ 3^{1/3} — within SW fit error band. Not assertable.

## Pearl gate

G54-D pearl (rho6** ∈ (1.2, 1.5)) is now PROMOTED from pending to:
- Precise value: ρ₆** = 1.4469 ± 0.001
- Three-radius structure fully characterized
- Pearl updated in pearl_registry/INDEX.md

## What this does NOT mean

- λ = FREE_COUPLING_PARAMETER (G4 Fisher rank theorem) — unchanged
- sm_derivation_claimed = False — unchanged
- No Tom Lawrence endorsement

## Next steps (open)

1. G54-A F4 (still open): 4D Einstein-Hilbert frame via Weyl rescaling
2. Tom correspondence: if/when Tom responds, G54-A through G54-E are a complete
   Casimir energy analysis — can summarize in ≤5 sentences
3. Double scale-invariance pearl G54-A+B (already in pearl registry): V_flux=const AND
   c_{1/2}≈const along SM constraint — now extended to: zeta_FP plateau also flat
   in [0.7, 1.2] (all O(10⁻³))
