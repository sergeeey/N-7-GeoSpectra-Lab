# Phase 4: Geometry Recoverability Synthesis

**Date:** 2026-06-29 | **Status:** PARTIALLY_REPRODUCED  
**Audit:** `PHASE4_REPRODUCTION_AUDIT.md` | **Scripts:** 06d0d48

## ⚠️ Honest Status

NOT frozen. Partial reproduction with **ML OOD W=20 weakened to 62.5%** (was claimed 92%).

## Verified Results

| Result | Value | Verdict |
|--------|-------|---------|
| Phase 3: 4 geometries | GEOMETRY_DISTINCT (HIGH) | ✅ |
| Ensemble: overall | **76.5%** (not 82%) | ⚠️ |
| Ensemble: spectral density | **99.2%** | ✅ |
| Validation: 6 checks | 6 PASS + 1 NOTE | ✅ |
| Permutation | p < 0.05 | ✅ |
| ML OOD: W<=10 | 98-100% | ✅ |
| **ML OOD: W=20** | **62.5%** (not 92%) | ⚠️ **WEAK** |

## Revised Central Claim

> Spectral density is the dominant robust discriminator (~99%). ML learns clean fingerprints and transfers to **moderate disorder** (W<=10: 98-100%), but **strong disorder W=20 degrades** OOD performance to 62.5%. The signal is simple and interpretable — threshold-based classification often outperforms ML.

## Key Insight (confirmed)

The geometry signal is **real but bounded**: it survives moderate disorder, weakens at strong disorder, and is best captured by spectral density distance — a simple, interpretable metric.

## Unverified Claims

- Phase 4C: 18/18 [UNVERIFIED] — no script
- Phase 4D v1: 74% [UNVERIFIED] — no script  
- Phase 4D v2: 83% [UNVERIFIED] — no script
- Multiclass: 15.8% [UNVERIFIED] — no script

## Scripts Verified

- `geometry_fingerprint_core.py` → ✅
- `phase4a_ensemble_full.py` → ✅ (76.5%)
- `phase4a_validation_minimal.py` → ✅ (6/7)
- `phase4a_ml_classifier_ood.py` → ✅ (W=20: 62.5%)

## To AUDIT_COMPLETE

1. [x] ML fixed, real numbers obtained
2. [ ] Add 4C/4D scripts or mark [UNVERIFIED]
3. [ ] Commit JSON data to repo
4. [ ] Final update

## Forbidden Claims

- Does NOT prove compactification
- Does NOT derive SM
- Does NOT fix lambda_v_operator or lambda_np
