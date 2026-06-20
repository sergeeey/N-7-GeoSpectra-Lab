# G51 — S_spec monotone along SM coupling ratio constraint

**Question type:** [x] descriptive  [ ] predictive  [ ] causal

**Claim:**
S_spec(ρ₃, ρ₆) has no interior minimum on the constraint curve
    ρ₃ = C × ρ₆²   where C = (g₂²/g₃²_SM × 16π/15)^{1/3} ≈ 0.986

The SM coupling ratio constraint fixes the shape of the constraint curve but
not the overall scale. S_spec is strictly monotone increasing along this curve.

**Proof (3 steps):**

1. S_spec = K_{S³}(t₃) × K_{S⁶}(t₆), with t₃ = 1/ρ₃², t₆ = 1/ρ₆²
2. K_{Sⁿ}(t) = Σ_k mult_k × exp(−t × λ_k²) is strictly decreasing in t
   (all terms positive, all derivatives negative)
3. On the constraint ρ₃ = Cρ₆²: as ρ₆ ↑, ρ₃ ↑, so t₃ ↓ AND t₆ ↓
   → K_{S³} ↑ AND K_{S⁶} ↑ → S_spec = product ↑

**Check:** `pytest tests/test_g51_sspec_constraint.py -v`

**Numerical verification:**
- 28 points sampled on (0.3, 3.0) × constraint → all monotone
- S_spec(ρ₆=0.01) < 10⁻⁵⁰ (approaches 0 from below)
- S_spec(ρ₆=2.0) ≫ S_spec(ρ₆=0.5) by factor > 10

**Caveat / What this does NOT mean:**
1. Does NOT mean the coupling ratio is wrong — 15/(16π) ≈ 0.298 at equal radii is
   still a valid geometric prediction (+4.3% from SM).
2. Does NOT close the radii stabilization problem — just rules out one mechanism.
3. The constraint ρ₃ ≈ 0.986 ρ₆² is phenomenologically correct BUT
   represents a 1D family of solutions, not an isolated minimum.

**Status:** NULL [VERIFIED-numerical]
