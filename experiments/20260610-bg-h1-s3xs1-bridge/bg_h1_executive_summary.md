# BG-H1 Executive Summary

**Date:** 2026-06-11  
**Verdict:** `S3XS1_KK_BRIDGE_SUPPORTED_ROBUST`  
**Status:** COMPLETE — all 4 gates PASS. BG-GATE sub-items 1–3 closed.

---

## What Was Tested

BG-H1 verified that the Kaluza-Klein product formula for the S³×S¹ Dirac spectrum is:
1. Analytically consistent (G0: cross-term cancellation from Camporesi-Higuchi)
2. Numerically exact (G1: λ²=(n+3/2)²+(m/R)², max error = 0.0, machine precision)
3. Accurately discretizable (E1: finite-difference proxy, δ(R) max rel error = 2.93e-08)
4. Robust under disorder (E2: W=0.5, 30 seeds, fragility ratio ≤ 1 analytically and numerically)

This is a proxy evaluation — the full S³×S¹ Dirac lattice was NOT built. Instead, BG-H1 uses the Kronecker-sum structure: if the S³ and S¹ Dirac operators are exact, their product eigenvalues satisfy λ²=k²+p² by algebra alone.

## Key Numbers

| Gate | Metric | Value | Kill threshold | Margin |
|---|---|---|---|---|
| G0 | Source trace (C-H eqs verified) | PASS | n/a | — |
| G1 | D4² − (−(k²+p²)I₄) max error | 0.0 | n/a | machine precision |
| E1 | δ(R) max relative error | 2.93e-08 | >1e-02 | 340,000× |
| E2 | fragility ratio (product vs S³) | 0.998 max | >10.0 | 10× |
| E2 | mean relative error | 2.54e-04 | >0.05 | 197× |

**S³ fingerprint at W=0.5:** mean rel fragility 0.23%, max 0.66%. Highly robust.

**Spin structures computed:**
- Periodic: m₁=1, m∈ℤ, δ₁(R=1)=0.303
- Antiperiodic (NS): m₁=½, m∈ℤ+½, δ₁(R=1)=0.081

No spin structure selected. Both carry forward.

## What This Closes

BG-GATE sub-items 1, 2, 3 from `ha4_design_decision.md` are satisfied. The proxy Kronecker-sum check passes to numerical precision and is robust under diagonal disorder at the S³ level.

## What Remains Open

**BG-GATE sub-item 4:** Show at least one geometry pair that Dirac discriminates but scalar cannot. This is the Phase 3 research objective and the remaining Phase 3 entry criterion.

## What This Does NOT Mean

1. PASS ≠ "true geometry is S³×S¹" — GEOMETRY_AGNOSTIC intact throughout
2. PASS ≠ R is a physical compactification radius
3. No claim about S⁶, SU(4)/SU(3) sectors, or Tom's full compactification
4. No physical promotion: lambda = FREE_COUPLING_PARAMETER, safe_for_runtime = False
5. No spin structure selected

## Test Coverage

| Module | Tests | Verified |
|---|---|---|
| bg_h1_product_dirac_check.py | 58 | [VERIFIED-pytest 2026-06-10] |
| bg_h1_e1_product_proxy.py | 72 | [VERIFIED-pytest 2026-06-10] |
| bg_h1_e2_disorder_proxy.py | 67 | [VERIFIED-pytest 2026-06-10] |
| Total main branch | 415 | [VERIFIED-pytest 2026-06-10] |

## Phase Transition

```
Phase 2 (v0.2.0 proxy justification):  COMPLETE ✓
  - AV-2: tom_ansatz angular bilinear supported
  - BG-H1: KK bridge mechanism verified

Phase 3 (S³×S¹ full harness):  NEXT
  Entry condition: BG-GATE §4 (geometry discrimination)
  First task: show one geometry pair Dirac discriminates, scalar cannot
```
