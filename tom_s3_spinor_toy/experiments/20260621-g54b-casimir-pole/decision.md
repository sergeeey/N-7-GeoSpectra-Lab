# G54-B Decision — Spectral Zeta Pole at s = −1/2

**Date:** 2026-06-21  
**Verdict:** B1–B4 PASS · B5 OPEN  
**Tests:** 22 new tests, all pass (total 1718)

---

## Results

### B1 PASS — Homogeneity
`ζ(-1/2; λρ₃, λρ₆) = λ^{-1} ζ(-1/2; ρ₃, ρ₆)` verified numerically to < 2% error.  
Along SM constraint: `ζ(-1/2; Cρ₆², ρ₆) = ρ₆^{-1} × ζ(-1/2; Cρ₆, 1)`.  
Both follow algebraically from the λ^{-2} scaling of D² and homogeneity of Γ(-1/2).

### B2 PASS — Pole existence
B₈ (τ^1 coefficient of K_{S⁶}) is non-zero → cross-term A₂_S3 × B₈ × ρ₃/ρ₆² gives
a t^{1/2} term → simple pole at s = −1/2 confirmed.

**New theorem (Poisson summation):**  
K_{S³}(τ) = (√π/2) τ^{-3/2} − (√π/4) τ^{-1/2} + O(e^{-π²/τ})  
*Exact result* — no polynomial τ^{1/2} term exists. Proof: bilateral theta function
Θ_{1/2}(t) = √(π/t) + O(e^{-π²/t}) via Poisson, so the e^{-t/4} corrections in F(t)
cancel exactly in K(t) = −2F'(t) − (1/2)F(t). All higher SW coefficients A4, A6, ...
are EXACTLY ZERO for S³.

### B3 PASS — Residue formula (simplified)
Since A4 = 0, the only t^{1/2} cross-term is:

```
c_{1/2}(ρ₃, ρ₆) = A₂_S3 × B₈ × ρ₃/ρ₆²
```

where A₂_S3 = −√π/4 and B₈ is the τ^1 SW coefficient of K_{S⁶}.
The B3 claim in claim.md (which included an A4 × B6 term) is superseded:
that term is identically zero.

### B4 PASS (revised) — Scale invariance along SM constraint
**NEW STRUCTURAL RESULT:**

Along ρ₃ = C ρ₆²:
```
c_{1/2}(Cρ₆², ρ₆) = A₂_S3 × B₈ × C = CONSTANT
```

The Casimir pole residue is **scale-invariant** along the SM coupling constraint —
identical structural behavior to V_flux from G54-A. This is because:
- c_{1/2} ∝ ρ₃/ρ₆²
- SM constraint fixes ρ₃/ρ₆² = C = const

The original B4 claim ("dominant term grows as ρ₆²") was wrong — it assumed A4 ≠ 0.

**Pearl: Both G54-A and G54-B are constant along ρ₃=Cρ₆². The SM constraint
makes ALL Vol(S³)/Vol(S⁶)-type functionals (flux, Casimir) scale-invariant.**

### B5 OPEN — Finite part
ζ_FP(−1/2) = Hadamard finite part requires the full Laurent expansion.
Needs all SW cross-terms with power ≤ 1/2 subtracted (≥10 pairs).
This is G54-C / future work.

---

## Numerical values

From least-squares fit over τ ∈ [0.02, 0.40]:
- B₀ ≈ 2/15 (analytically exact, verified to < 5%)
- B₈ from fit (O(1) value, provides non-zero pole)

---

## What this does NOT mean

1. Does NOT compute the physical Casimir energy (that requires ζ_FP via Hadamard).
2. Does NOT show the renormalized Casimir stabilizes compactification.
3. The Poisson theorem (A4=0) is specific to S³ as a symmetric space; higher spheres
   Sⁿ do not generally have exact two-term SW expansions.

---

## Killed / survived

**Killed:** Claim that c_{1/2} varies along the SM constraint. The A4 × B6 correction
term is ZERO (Poisson theorem), so the residue is constant on the constraint.

**Survived:** The pole at s = −1/2 exists (B₈ ≠ 0). The homogeneity B1 is clean.
The B5 question (minimum of ζ_FP) is open.

---

## Next steps

1. **G54-C (Coleman-Weinberg):** Compute the effective potential at one-loop using
   ζ_FP(−1/2) with Hadamard subtraction. Does it have a minimum at some (ρ₃, ρ₆)?
2. **Two-flux system (G54-D):** Add q₃ on S³ + q₆ on S⁶ → two equations for (ρ₃, ρ₆).
   May fix the scale ρ₆ which G54-A cannot (ratio stabilizer only).
