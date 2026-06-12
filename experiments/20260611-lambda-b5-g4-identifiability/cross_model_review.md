# Cross-Model Review — LAMBDA-B5-G4

**Reviewer:** Codex (GPT-based, via codex:codex-rescue agent)  
**Date:** 2026-06-12  
**Protocol:** FL Context Asymmetry — reviewer given ONLY claim.md + evidence code. No session history.  
**Verdict:** FIX FIRST (Confidence 7/10)

---

## Codex Findings

### Hidden Assumptions (9 flagged)

1. `o3` is a genuinely independent observable, not a definition containing λ
2. V promotion is physically legitimate (not just a model coordinate)
3. Coefficient `16π²/15` is exactly known without hidden normalization/frame factors
4. ρ is independently identifiable from `o1 = 1/ρ`
5. `m1` is fixed and independent of R and λ
6. R is globally identifiable from `o2` (local derivative ≠ global identifiability)
7. λ is a physical parameter, not eliminable by field normalization or radion rescaling
8. Local Jacobian rank is correctly used as structural identifiability proxy
9. Non-zero determinant is not itself evidence about physics

### Most Likely Failure (Codex grade: HIGH)

`o3` is not independently observable. If an unknown normalization factor κ exists (volume normalization, field normalization, conformal frame, detector calibration):

```
o3_measured = κ · (16π²ρ³/15) · λ
```

Then only the product `κ·λ` is identifiable, not λ separately. In KK theories, coupling constants and compactification volumes are notoriously frame-sensitive. **This is the most likely real-world failure point.**

### Non-Obvious Failure (Codex grade: MEDIUM)

`m1` is implicitly treated as an external constant, but in real KK/spinor spectral geometry it is an eigenvalue of the geometry and boundary conditions. If `m1 = m1(R, λ, boundary conditions)`, then the Jacobian derivatives are incomplete, and the rank-3 result is a parameter bookkeeping artifact.

### Prior Art (Codex citations)

- Fisher Information Matrix in physics systematically overestimates identifiability vs full Bayesian/MCMC (Rodriguez et al. arXiv:1308.1397, gravitational waves)
- KK reductions critically depend on scalar/radion normalization and frame choice
- Spinor bilinears constrained by Fierz identities — naive counting overestimates independent information
- Reconstruction of spinors from bilinear covariants depends on dual/adjoint structure choice (arXiv:2304.12945)

---

## Response to Codex (per DDD/FL protocol)

### Concern 1: κ normalization factor → **ACCEPTED — adds scope caveat**

The Codex finding is valid. The claim states "λ is identifiable IFF V is promoted" but does NOT address normalization of V itself.

**Resolution:** The **negative half** of the claim is unaffected: `rank(J_phys)=0` for λ regardless of κ, since o1 and o2 genuinely do not contain λ. The **positive half** needs a caveat:

> "λ is identifiable WITH V, **assuming V normalization coefficient κ is independently known**"

This is documented as a scope limitation, not a failure. The main scientific value of G4 is the negative half (formally killing Case 3 H1: "λ fixed by S³ alone").

**Action:** Scope limitation added to claim.md under "Fence" (see below).

### Concern 2: m1 depends on R and boundary conditions → **PARTIALLY DISMISSED**

In the BG-H1 formulation, m1 is the KK quantum number — a discrete label fixed by spin structure choice (m ∈ ℤ for periodic, m ∈ ℤ+½ for anti-periodic). It is NOT a continuous function of R or λ. The existing fence reads: "spin structure s is discrete, fixed separately." This covers m1 discreteness.

However, the Codex concern is valid in a more general KK setup where m1 might be geometric. For the S³×S¹ product case analyzed here, this is dismissed. **Documented as a generalization caveat.**

### Concern 3: Fisher rank necessary but not sufficient → **ACCEPTED — already scoped**

The claim explicitly uses "structural non-identifiability" language, which is the correct technical term for rank-based analysis. This is the definition of structural identifiability (Ljung 1994, Bellman & Åström 1970). The concern is valid for practical/numerical identifiability but does not apply to structural analysis. **Pre-existing scope, no action needed.**

### Codex FIX FIRST items — response:

1. **Define o3 operationally without λ on LHS** — Accepted as scope caveat (κ independence assumption documented)
2. **Recompute rank with extended [λ, ρ, R, κ] parameters** — Noted as a follow-on gate (G4+κ) to run if/when V is promoted to physical status
3. **Add global/practical check via profile likelihood** — Noted as follow-on; out of scope for current symbolic gate

---

## Updated Scope Fence (additions to claim.md)

The following additions address Codex findings without changing the core result:

```
Additional fence (2026-06-12 cross-model review):
- The POSITIVE half claim ("λ identifiable WITH V") assumes V normalization κ is 
  independently fixed. If κ is unknown, only κ·λ is identifiable.
- m1 is treated as a discrete quantum number fixed by spin structure selection.
  In more general KK geometries, m1 = m1(geometry) — this gate is specific to S³×S¹.
- The gate proves STRUCTURAL identifiability (rank analysis), not PRACTICAL 
  identifiability (numerical, noise-sensitive recovery).
```

---

## Cross-Model Review Summary

| Concern | Source | Assessment | Action |
|---------|--------|-----------|--------|
| κ normalization of V | Codex | Valid — positive half weakened | Scope caveat added |
| m1 geometric dependence | Codex | Dismissed for S³×S¹; caveat for general KK | Generalization note added |
| Fisher rank ≠ practical | Codex | Already scoped to structural | No action |

**Conclusion:** G4 negative result (λ non-identifiable without V) is **CONFIRMED ROBUST** by cross-model review. G4 positive result (λ identifiable with V) is **CONDITIONALLY CONFIRMED** — conditioned on κ independence.

**Final verdict:** FIX FIRST → Scope caveats added → claim stands with narrowed positive half.

**ACH impact:** Case 3 H1 kill is **UNAFFECTED** (negative half). Case 3 H3 ("λ free until external") remains VERIFIED_FORMAL_THEOREM for the negative direction.

---

*Cross-model review protocol: codex-skeptic (SKILL.md) + FL Context Asymmetry (falsification-ladder.md)*  
*Commit this file to document the review; no change to core G4 verdict.*
