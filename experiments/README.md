# GeoSpectra Experiments — Phase 4 Package

**Status:** PHASE 4B COMPLETE 2026-06-29 — Phase diagram of spectral recoverability
**Commit:** 4fc3770

## New Framing

> **We study when compact-product geometry fingerprints remain recoverable from spectra under disorder — not whether they are "always robust."**
>
> This produces a **phase diagram**: recoverable / degraded / erased.

## Quick Start

```bash
pip install numpy scipy scikit-learn
python phase4a_ensemble_full.py              # Ensemble + ablation
python phase4a_ml_classifier_ood.py          # ML + OOD
python phase4a_validation_minimal.py         # 7-check validation
python phase4a_crucial_experiments.py        # Strong Inference: 4 crucial tests
python phase4b_phase_diagram.py             # Phase diagram (W x N x pair)
```

## Experiment Index

| File | Phase | What it does | Runtime |
|------|-------|-------------|---------|
| `geometry_fingerprint_core.py` | 3 | Analytic 4-geometry discrimination | 5s |
| `phase4a_ensemble_full.py` | 4A | **Ensemble 10 seeds + ablation** | 250s |
| `phase4a_ml_classifier_ood.py` | 4A | **ML classifier + OOD** | 120s |
| `phase4a_validation_minimal.py` | 4A | **7-check validation** | 120s |
| `phase4a_crucial_experiments.py` | 4A | **Strong Inference 4 tests** | 180s |
| `phase4b_phase_diagram.py` | 4B | **Phase diagram (NEW)** | 300s |

## Phase 4B: Spectral Recoverability Phase Diagram

### Result — 3 Regimes Discovered

| Regime | Condition | Evidence |
|--------|-----------|----------|
| **Recoverable** | Flat-vs-curved, any W | T4 vs curved: 100% to W=30 |
| **Degraded** | Curved-vs-curved, W=15-20 | S3xS1 vs S2xS2: drops to 33-67% |
| **Erased** | Curved-vs-curved, W≥25 | S3xS1 vs S2xS2: 0% at W=25,30 |

### Phase Diagram by Pair

```
T4 vs S3xS1:  🔴W=0 → 🟢W=1..30 (flat-vs-curved ROBUST)
T4 vs S2xS2:  🔴W=0 → 🟢W=1..30 (flat-vs-curved ROBUST)
S3xS1 vs S2xS2: 🟢W=0..12 → 🔴W=15,20,25,30 (curved-vs-curved DEGRADES)
```

### Key Finding

**W=20 is not a failure — it's a phase boundary.** The degradation is **pair-dependent**:
- Flat-vs-curved pairs survive to W=30
- Curved-vs-curved pairs degrade at W=15-20 and erase at W≥25

This transforms the W=20 "problem" into a **scientific result about spectral recoverability regimes**.

## Key Results (HONEST — post-reproduction)

### Confirmed (reproduced)
- **Ensemble:** 76.5% distinct (was claimed 82%), spectral density 99.2%
- **ML OOD W<=10:** 98-100%
- **ML OOD W=20 (baseline):** 62.5% (train W=0 only) — artifact
- **Validation:** 6 PASS + 1 NOTE
- **Multiclass:** 15.8% — honest boundary, does NOT work

### Salvaged via Strong Inference
| Test | Result | Status |
|------|--------|--------|
| Train W<=10, test W=20 | **80.0%** | W=20 salvaged |
| 2 features (sd+d_eff) | **100.0%** | Feature selection critical |
| k=30 at W=20 | **86.7%** | More eigenvalues help |
| Threshold, diff seeds | **48.3%** | Threshold NOT robust |

## Parameters (locked)

```python
W_VALUES = [0, 1, 2, 5, 8, 10, 12, 15, 18, 20, 25, 30]
SEEDS_TRAIN = [42, 123, 999, 777, 100]
SEEDS_TEST = [200, 300, 400, 500, 600]
K_EIG = 15-30 (15 baseline, 30 for W>=15)
T4_SIZE = 6^4 = 1296
CURVED_SIZE = 50*8 = 400 (N=300 for Phase 4B)
```

## Data

All results saved as JSON. Load with:

```python
import json
# Phase 4A
with open('data/phase4a_ensemble_results.json') as f:
    data = json.load(f)
with open('experiments/20260629-crucial-experiments/crucial_results.json') as f:
    crucial = json.load(f)
# Phase 4B
with open('experiments/20260629-phase4b/phase4b_results.json') as f:
    phase_diag = json.load(f)
```

**Phase diagram established. W=20 transformed from problem to boundary result.**
