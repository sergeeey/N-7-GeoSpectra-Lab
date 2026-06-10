# Decision Record — Spinor-Geometry Pivot v0.2.0

**Date:** 2026-06-10  
**Method:** HD-MAVP full audit (math_code + contradiction + decision_record)  
**Input claim:** Dirac/spinor harness distinguishes S², S³, S⁶ via spectral fingerprints  
**Known correction applied:** IPR not primary; R/4 channel closed (H→H+cI, 1e-18)

---

## Verified Atoms

| Atom | Claim | Evidence | Status |
|---|---|---|---|
| C1 | Scalar harness GEOMETRY_AGNOSTIC | v0.1.22 | VERIFIED |
| C2 | Dirac λ=±(n+d/2) | Camporesi-Higuchi PDF | VERIFIED |
| C3 | |λ_min|=d/2 distinct per sphere | analytic + tool | VERIFIED-tool |
| C4 | Degeneracy patterns distinct | [1,4,9,16,25] vs [2,6,12,20,30] | VERIFIED-tool |
| C5 | Same-n degeneracy survives discretization | Block A, Block E | VERIFIED-tool |
| C6 | IPR blind to R/4 | diff=1e-18 at N=200 | VERIFIED-tool |
| C7 | Same-n modes orthogonal under S³ weight | Block B cross-terms <0.001 | VERIFIED-tool |

## Contradictions Found and Resolved

| Contradiction | Atoms | Resolution |
|---|---|---|
| C1 | C8 × C9 | Radial-only basis incomplete; spectral path unaffected — eigenvalues don't need cross-n orthogonality |
| C2 | C9 × C11 | C11 measures same-n orthogonality only; this is expected and correct for spectral fingerprint |

**No blocking contradictions on the spectral fingerprint path.**

## Hidden Assumptions

| Assumption | Status | Action |
|---|---|---|
| HA-1: harness computes full spinor harmonics | VIOLATED | Scope to radial-only; block IPR as primary |
| HA-2: Hopf coords = standard S³ spectrum | UNVERIFIED | Required before cross-sphere comparison |
| HA-3: fingerprint survives W>0 | NO DATA | KT-3 experiment |
| **HA-4: S^d discrimination solves S³×S¹ GEOMETRY_AGNOSTIC** | **SCOPE GAP** | **Record explicitly; do not conflate** |

## Side Finding: tom_ansatz ≈ phi_{11}

**[VERIFIED-tool 2026-06-10]**

tom_ansatz = √sin(2α) has dominant projection 0.920 onto phi_{11} (n=1, l=1, λ=±2.5)
under weighted L² inner product on S³.

Pattern: phi_{ll} series (l=1: 0.92, l=2: 0.88, l=3: 0.83, l=4: 0.79)
Geometric interpretation: √(volume_measure)^{1/2} aligns with l=n boundary modes.

**This is a candidate direct answer to Tom's alpha-problem:**
Tom's ansatz IS approximately the (n=1,l=1) Dirac radial eigenmode with λ=±2.5.

Status: verified under radial weighted inner product; requires full angular confirmation
before communicating to Tom.

## Kill Tests

| Test | Status | Kill Condition |
|---|---|---|
| KT-1: discrete eigenvalue recovery | **NOT YET RUN** | >5% error at N_α=100 |
| KT-2: S²/S³ gap = 0.5 numerically | **NOT YET RUN** | gap error >50% |
| KT-3: disorder smears fingerprint | NOT YET RUN | W=0.1 wipes λ_min |
| KT-4: scalar vs Dirac on same sphere | NOT YET RUN | can't distinguish patterns |
| KT-5: tom_ansatz ↔ phi_{11} | **VERIFIED** | 0.920391 (pass) |

## Revised Controls Tier 1

OLD: max projection < 0.1 → ansatz is NOT an eigenfunction (FAILS — actual 0.92)  
NEW: compute dominant-mode decomposition; record phi_{11} as dominant (0.92); this
     is a finding about Tom's framework, not a test failure.

## Experiment Order

```
E0  discrete Dirac matrix + eigenvalue recovery     [~50 lines, can run now]
    Gate: KT-1 pass → proceed to E2
E1  tom_ansatz decomposition regression test        [already verified, write as test]
E2  Tier 2 controls (C9a, C9b, C9c)                [depends on E0 pass]
    ↓ PARALLEL after E2 pass:
E3  KT-2 cross-sphere S²/S³ gap                    [requires S² implementation]
E4  KT-3 disorder W=0.1 fingerprint survival
E5  Tier 3 negative controls (NC-1, NC-2, NC-3)
    ↓ DESIGN GATE (not experiment):
E6  HA-4: define relationship between S^d discrimination and S³×S¹ problem
```

## Decision

```
VERDICT: CONDITIONAL_GO

GREEN (proceed now):   E0 → E1 (regression) → E2
YELLOW (after E2):     E3, E4, E5 in parallel
ORANGE GATE:           HA-4 scope question — design decision before Phase 3 paper
NO-GO conditions:      KT-1 fail or KT-2 gap_error > 50%

EXPLICIT SCOPE STATEMENT:
  This pivot tests geometry discrimination on PURE spheres S², S³, S⁶.
  This is a DIFFERENT question from the original S³×S¹ GEOMETRY_AGNOSTIC verdict.
  Success here does not resolve the original scalar-harness failure.
  Connection path to original question: UNDESIGNED (HA-4 gate open).
```

---

**Linked files:**
- `estimand_v0.2.0.md` — full estimand (update §6 point 6 from HA-4 above)
- `skeptic_design_v0.2.0.md` — FT-S1/S2/S3 pre-registered falsification tests
- `controls_v0.2.0.md` — Tier 1 needs Tier 1 redesign per BLOCK C finding

**Not promoted:** no observables promoted; runtime=research_only; lambda=FREE_COUPLING_PARAMETER preserved.
