# AV-1 — Pre-registered Claim: Dictionary Robustness of tom_ansatz ↔ φ₁₁

**Experiment:** AV1_ANGULAR_DICTIONARY_ROBUSTNESS
**Date pre-registered:** 2026-06-10 (BEFORE running AV-1a off-diagonal / AV-1c bilinear code)
**Question type:** [x] descriptive  [ ] predictive  [ ] causal
**Status:** research_only — no physical promotion

---

## Context and Connection to Tom's Framework

Tom's lecture eq. (49) expands the metric density into spinor-harmonic products:

```
√||g|| = f^(φ) + Σ_{α,χ} f^{(ψ)α} ψ^χ(y^Z) ψ^α(y^i) + ...
```

On S³ in Hopf coordinates: √||g|| = sinα·cosα = sin(2α)/2  [VERIFIED, geometry_s3_hopf.py].
Therefore `tom_ansatz = √sin(2α) = √2·(√||g||)^{1/2}` and
`tom_ansatz² = sin(2α) = 2·√||g||` — the LHS of Tom's eq. (49) up to constant.

The existing finding [VERIFIED-tool, RADIAL_PROJECTION_FINDING_ONLY]:
⟨tom̂, φ̂₁₁⟩_w = 0.9204 in weighted L²(sinα cosα dα).

## Prior Knowledge Declared (anti-HARKing)

Already known BEFORE this experiment (from prior session, regression-tested):
- φ_{ll} diagonal series: l=1: 0.92, l=2: 0.88, l=3: 0.83, l=4: 0.79
- NOT yet computed: off-diagonal modes (n > l), bilinear decomposition

New data produced by AV-1: off-diagonal projection table + bilinear fit.

---

## Claims (falsifiable, pre-registered)

### AV-1a — Global argmax over full dictionary

**Claim:** Over the dictionary D = {φ̂_{nl} : 0 ≤ l ≤ 6, l ≤ n ≤ l+6} (49 modes),
the global argmax of |⟨tom̂, φ̂_{nl}⟩_w| is (n,l) = (1,1) with value 0.9204 ± 0.0005.

**Kill condition:** any off-diagonal mode (n ≠ l) exceeds 0.9204 →
φ₁₁ identification is an artifact of the diagonal-only search → downgrade
finding to [DICTIONARY_ARTIFACT], notify decision record.

### AV-1b — Least-squares dominance (secondary)

**Claim:** In the Gram least-squares decomposition of tom̂ over D, the φ₁₁
coefficient is the largest in absolute value, and a 5-term approximation
reaches residual < 5% of ‖tom̂‖.

**Caveat (pre-declared):** dictionary D is non-orthogonal in L²(α-weighted)
(angular orthogonality is absent in the radial-only inner product), so the
LS coefficients are basis-dependent. This claim is supportive, not decisive.

### AV-1c — Bilinear (eq. 49) radial probe

**Claim:** sin(2α) = tom_ansatz² lies in the span of diagonal bilinears
{φ̂_{nl}² : 0 ≤ l ≤ 4, l ≤ n ≤ l+4} with residual < 10% using ≤ 5 terms,
and φ₁₁² is among the dominant terms.

**Kill condition:** residual > 10% with 5 terms → the radial part of Tom's
eq. (49) is NOT efficiently captured by low (n,l) Dirac bilinears →
record as constraint on eq. 49 interpretation.

### Exploratory (no claim, observation only)

H-T1 candidate: eq.-49 radial coefficients concentrate on the n = l
boundary family (suggested by the φ_{ll} series pattern). To be PROMOTED to
a registered hypothesis only if AV-1a/1c pass AND the n=l family carries
> 80% of the explained norm in AV-1b.

---

## Sensitivity Checks (≥1 required; 2 planned)

1. Repeat AV-1a/1c in UNWEIGHTED L²(dα) — convention robustness.
2. Grid refinement: n_grid 2000 → 8000 — discretization robustness.

---

## Natural Language Statement

*We estimate the projection coefficients of tom_ansatz (resp. tom_ansatz²)
onto the radial Dirac eigenmode dictionary (resp. its diagonal bilinears)
on S³ in Hopf coordinates, in weighted L², comparing the (1,1) mode against
all (n,l) with n,l ≤ 12, with no intercurrent events (deterministic
numerics).*

## What This Does NOT Mean (pre-declared)

1. Does NOT verify the full angular/spinor structure (half-integer Hopf
   weights, spin connection) — that requires the 2D (α,θ) operator (AV-2,
   not in this experiment). Item 40 stays "full angular pending" even if
   AV-1 passes; it upgrades to [RADIAL+DICTIONARY_ROBUST].
2. Does NOT verify Tom's S⁶ factor or the f^{αχ} cross-couplings of eq. 49.
3. Does NOT promote any physical claim; λ = FREE_COUPLING_PARAMETER.
4. AV-1b coefficients are basis-dependent (non-orthogonal dictionary).
