# GeoSpectra Experiments — Phase 4 Package

**Status:** RESOLVED 2026-06-29 (Strong Inference complete, W=20 salvaged)
**Commit:** 4fc3770

## Quick Start

```bash
pip install numpy scipy scikit-learn
python phase4a_ensemble_full.py              # Ensemble + ablation
python phase4a_ml_classifier_ood.py          # ML + OOD
python phase4a_validation_minimal.py         # 7-check validation
python phase4a_crucial_experiments.py        # Strong Inference: 4 crucial tests
```

## Experiment Index

| File | Phase | What it does | Runtime |
|------|-------|-------------|---------|
| `geometry_fingerprint_core.py` | 3 | Analytic 4-geometry discrimination | 5s |
| `phase4a_ensemble_full.py` | 4A | **Ensemble 10 seeds + ablation** | 250s |
| `phase4a_ml_classifier_ood.py` | 4A | **ML classifier + OOD** | 120s |
| `phase4a_validation_minimal.py` | 4A | **7-check validation** | 120s |
| `phase4a_crucial_experiments.py` | 4A | **Strong Inference 4 tests** ← NEW | 180s |

## Key Results (HONEST — post-reproduction)

### Confirmed (reproduced)
- **Ensemble:** 76.5% distinct (was claimed 82%), spectral density 99.2%
- **ML OOD W<=10:** 98-100%
- **ML OOD W=20 (baseline):** 62.5% (train W=0 only) — artifact
- **Validation:** 6 PASS + 1 NOTE
- **Multiclass:** 15.8% — honest boundary, does NOT work

### Salvaged via Strong Inference (crucial experiments)
| Test | Result | Status |
|------|--------|--------|
| **H2:** Train W<=10, test W=20 | **80.0%** | ✅ W=20 salvaged |
| **H4:** 2 features (sd+d_eff) | **100.0%** | ✅ Feature selection critical |
| **H1:** k=30 at W=20 | **86.7%** | ✅ More eigenvalues help |
| **H6:** Threshold, diff seeds | **48.3%** | ❌ Threshold NOT robust |

### Interpretation
- W=20 degradation was **training artifact** (train W=0 → test W=20 unrealistic)
- With proper training (W<=10), ML achieves **80-100% at W=20**
- Threshold baseline **fails** under realistic different-seed conditions (48.3%)
- **ML is necessary** for robustness

## Parameters (locked)

```python
W_VALUES = [0, 0.5, 1.0, 2.0, 5.0, 10.0, 15.0, 20.0]
SEEDS_TRAIN = [42, 123, 999, 777, 100]
SEEDS_TEST = [200, 300, 400, 500, 600]
K_EIG = 15-30 (15 baseline, 30 for W>=15)
T4_SIZE = 6^4 = 1296
CURVED_SIZE = 50*8 = 400
```

## Data

All results saved as JSON in `../data/phase4_*` and `20260629-crucial-experiments/`. Load with:

```python
import json
with open('data/phase4a_ensemble_results.json') as f:
    data = json.load(f)
with open('experiments/20260629-crucial-experiments/crucial_results.json') as f:
    crucial = json.load(f)
```

**Strong Inference complete. Honest boundary established.**
