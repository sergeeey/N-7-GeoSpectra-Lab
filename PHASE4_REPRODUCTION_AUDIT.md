# Phase 4: Reproduction Audit

**Status:** PARTIALLY_REPRODUCED — ML OOD W=20 = 62.5% (not 92%)  
**Date:** 2026-06-29  
**Scripts commit:** 06d0d48

## Reproduced Results

| # | Claim | Script | Reproduced | Verdict |
|---|-------|--------|-----------|---------|
| 1 | Phase 3: distinct | `geometry_fingerprint_core.py` | **GEOMETRY_DISTINCT (HIGH)** | ✅ |
| 2 | Ensemble: overall | `phase4a_ensemble_full.py` | **76.5%** (101/132) | ⚠️ lower |
| 3 | Ensemble: spec dens | `phase4a_ensemble_full.py` | **99.2%** (131/132) | ✅ |
| 4 | Ensemble: S3xS1vsS2xS2 all | `phase4a_ensemble_full.py` | **64.4%** (29/45) | ⚠️ weak |
| 5 | Ensemble: S3xS1vsS2xS2 spec | `phase4a_ensemble_full.py` | **97.8%** (44/45) | ✅ |
| 6 | ML OOD: W=1 | `phase4a_ml_classifier_ood.py` | **100.0%** (n=60) | ✅ |
| 7 | ML OOD: W=5 | `phase4a_ml_classifier_ood.py` | **100.0%** (n=60) | ✅ |
| 8 | ML OOD: W=10 | `phase4a_ml_classifier_ood.py` | **98.1%** (n=54) | ✅ |
| 9 | **ML OOD: W=20** | `phase4a_ml_classifier_ood.py` | **62.5%** (n=40) | ⚠️ **WEAK** |
| 10 | Validation: 6 checks | `phase4a_validation_minimal.py` | **6 PASS + 1 NOTE** | ✅ |
| 11 | Permutation | `phase4a_validation_minimal.py` | **77.3% vs 46.4%±10.9%** | ✅ p<0.05 |
| 12 | Threshold vs ML | `phase4a_validation_minimal.py` | **sd>4: 90.9%, ML: 77.3%** | ⚠️ note |

## ML OOD Honest Picture

```
W=1:   100%  ← perfect
W=5:   100%  ← perfect  
W=10:   98%  ← near-perfect
W=20:   63%  ← degraded
```

**Verdict:** Strong transfer for moderate disorder (W<=10). W=20 substantially weakens.

## Central Claim (revised)

> Spectral density is the dominant robust discriminator (~99%). ML learns clean fingerprints and transfers to moderate disorder (W<=10: 98-100%), but strong disorder W=20 degrades to 62.5%. The signal is simple and interpretable — threshold-based classification often outperforms ML.

## Unverified

- Phase 4C: 18/18 [UNVERIFIED] — no script
- Phase 4D v1: 74% [UNVERIFIED] — no script
- Phase 4D v2: 83% [UNVERIFIED] — no script
- Multiclass: 15.8% [UNVERIFIED] — no script

## To AUDIT_COMPLETE

1. [x] ML fixed, real numbers obtained
2. [ ] Add 4C/4D scripts OR mark [UNVERIFIED]
3. [ ] Commit JSON to repo
4. [ ] Finalize synthesis
