# GeoSpectra Experiments — Phase 4 Package

**Status:** FROZEN 2026-06-29  
**Commit:** 4fc3770  

## Quick Start

```bash
pip install numpy scipy scikit-learn
python phase4a_ensemble_full.py              # Main result: ensemble + ablation
python phase4a_ml_classifier_ood.py          # ML + OOD robustness
python phase4a_validation_minimal.py         # 7-check validation
```

## Experiment Index

| File | Phase | What it does | Runtime |
|------|-------|-------------|---------|
| `geometry_fingerprint_core.py` | 3 | Analytic 4-geometry discrimination | 5s |
| `phase4c_t4_baseline.py` | 4C | T4 finite-lattice vs S3xS1 | 120s |
| `phase4d_cross_geometry_transfer.py` | 4D v1 | Cross-geometry, N=100-300 | 300s |
| `phase4d_v2_enhanced_metrics.py` | 4D v2 | 6 metrics, N>=300 | 300s |
| `phase4a_w_sweep_curved_only.py` | 4A | W-sweep S3xS1 vs S2xS2 | 120s |
| `phase4a_w_sweep_with_t4.py` | 4A | W-sweep all 3 geometries | 180s |
| `phase4a_ensemble_full.py` | 4A | **Ensemble 10 seeds + ablation** | 250s |
| `phase4a_ml_classifier_ood.py` | 4A | **ML classifier + OOD** | 120s |
| `phase4a_validation_minimal.py` | 4A | **7-check validation** | 120s |
| `phase4a_multiclass_compact.py` | 4A | Multiclass (honest boundary) | 120s |

## Key Results

- **Ensemble:** 82% distinct, spectral density 99%, bootstrap CI [79%, 85%]
- **ML OOD:** RF 92% at W=20, trained on clean only
- **Validation:** 6/7 PASS, 1/7 explained
- **Multiclass:** 15.8% — honest boundary, future work

## Parameters (locked)

```python
W_VALUES = [0, 0.5, 1.0, 2.0, 5.0, 10.0, 15.0, 20.0]
SEEDS = [42, 123, 999, 777, 100, 200, 300, 400, 500, 600]
K_EIG = 12-15
T4_SIZE = 6**4 = 1296
CURVED_SIZE = 50*8 = 400
```

## Data

All results saved as JSON in `../data/phase4_*`. Load with:

```python
import json
with open('data/phase4a_ensemble_results.json') as f:
    data = json.load(f)
```

**Frozen. No new experiments without justification.**
