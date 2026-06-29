# Phase 4: Geometry Recoverability Synthesis

**Date:** 2026-06-29 | **Status:** PARTIALLY_REPRODUCED  
**Audit:** `PHASE4_REPRODUCTION_AUDIT.md`

## ⚠️ Honest Status

This package is **NOT frozen**. Partial reproduction completed.

## Reproduced Claims (verified)

| Claim | Reproduced | Target | Verdict |
|-------|-----------|--------|---------|
| Phase 3: 4 geometries distinct | **GEOMETRY_DISTINCT (HIGH)** | DISTINCT | ✅ |
| Ensemble overall | **76.5%** (101/132) | 82% | ⚠️ lower |
| Spectral density | **99.2%** (131/132) | 99% | ✅ |
| Validation: 6 checks | **6 PASS + 1 NOTE** | 6/7 | ✅ |
| Permutation baseline | **77.3% vs 46.4%±10.9%** | p<0.05 | ✅ |

## Unverified Claims

| Claim | Status |
|-------|--------|
| Phase 4C: 18/18 | [UNVERIFIED] — no script |
| Phase 4D v1: 74% | [UNVERIFIED] — no script |
| Phase 4D v2: 83% | [UNVERIFIED] — no script |
| ML OOD: W=20 acc | [FIXED, needs re-run] |
| Multiclass: 15.8% | [UNVERIFIED] — no script |

## Key Insight (confirmed)

> Spectral density is the dominant geometry discriminator (~99%). The signal is simple and interpretable. ML confirms learnability but threshold often suffices.

## Scripts in Repo

- `geometry_fingerprint_core.py` → ~5s
- `phase4a_ensemble_full.py` → ~250s
- `phase4a_validation_minimal.py` → ~120s
- `phase4a_ml_classifier_ood.py` → ~120s (fixed)

## To Reach AUDIT_COMPLETE

1. [ ] Re-run ML script → get OOD accuracy
2. [ ] Add 4C/4D scripts or mark [UNVERIFIED]
3. [ ] Update with final numbers

## Forbidden Claims

- Does NOT prove compactification
- Does NOT derive SM
- Does NOT fix lambda
