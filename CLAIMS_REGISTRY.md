# Claims Registry — GeoSpectra Lab

**Version:** 2026-06-29  
**Method:** Reproduction audit + Strong Inference  
**Status:** AUDIT_COMPLETE_FOR_PHASE3_AND_PHASE4A_SUBSET, PHASE4B_COMPLETE

---

## Claim Levels

| Level | Definition | Color |
|-------|-----------|-------|
| **L1** | Confirmed core — reproduced independently, multiple checks | 🟢 |
| **L2** | Reproduced but weaker — result holds but below original claim | 🟡 |
| **L3** | Pending / unverified — script or data missing | 🟠 |
| **L4** | Speculative interpretation — not directly tested | 🔴 |

---

## Registry

| # | Claim | Value | Level | Script | JSON | Notes |
|---|-------|-------|-------|--------|------|-------|
| 1 | Phase 3: 4 geometries analytically distinct | GEOMETRY_DISTINCT (HIGH) | **L1** | `geometry_fingerprint_core.py` | ✅ | 4/4 distinct at W=0 |
| 2 | Spectral density discrimination | **99.2%** | **L1** | `phase4a_ensemble_full.py` | ✅ | Dominant feature across all W |
| 3 | Ensemble overall distinctness | **76.5%** | **L2** | `phase4a_ensemble_full.py` | ✅ | Was claimed 82%; honest bootstrap |
| 4 | Validation suite | **6 PASS + 1 NOTE** | **L1** | `phase4a_validation_minimal.py` | ✅ | 7-check independent audit |
| 5 | ML OOD W≤10 | **98-100%** | **L2** | `phase4a_ml_classifier_ood.py` | ✅ | Strong under moderate disorder |
| 6 | ML OOD W=20 (baseline) | **62.5%** | **L2** | `phase4a_ml_classifier_ood.py` | ✅ | Train W=0 only; distribution shift artifact |
| 7 | ML OOD W=20 (salvaged, W≤10 train) | **80.0%** | **L2** | `phase4a_crucial_experiments.py` | ✅ | H2 killed — ML generalizes |
| 8 | 2-feature model (sd+d_eff) | **100.0%** | **L1** | `phase4a_crucial_experiments.py` | ✅ | H4 confirmed — feature selection critical |
| 9 | k=30 at W=20 | **86.7%** | **L2** | `phase4a_crucial_experiments.py` | ✅ | H1 confirmed — more eigenvalues help |
| 10 | Threshold robustness (diff seeds) | **48.3%** | **L1** | `phase4a_crucial_experiments.py` | ✅ | H6 killed — threshold NOT robust; ML justified |
| 11 | Multiclass classification | **15.8%** | **L2** | — | — | Below random 25%; honest boundary |
| 12 | **Phase 4B: Flat-vs-curved robust to W=30** | **100%** | **L1** | `phase4b_phase_diagram.py` | ✅ | T4 vs curved: recoverable at all W |
| 13 | **Phase 4B: Curved-vs-curved degrades at W=15-20** | **33-67%** | **L1** | `phase4b_phase_diagram.py` | ✅ | S3xS1 vs S2xS2: phase boundary |
| 14 | **Phase 4B: Curved-vs-curved erased at W≥25** | **0%** | **L1** | `phase4b_phase_diagram.py` | ✅ | Erased regime confirmed |
| 15 | Phase 4C T4 baseline | — | **L3** | Missing | Missing | Script referenced but not in repo |
| 16 | Phase 4D cross-geometry | — | **L3** | Missing | Missing | Script referenced but not in repo |
| 17 | Tom theory implications | — | **L4** | — | — | Not directly testable |
| 18 | Physical compactification | — | **L4** | — | — | Not claimed |
| 19 | Quantum foam / SM derivation | — | **L4** | — | — | Explicitly NOT claimed |

---

## Phase 4B: Spectral Recoverability Phase Diagram

### Three Regimes Discovered

| Regime | Condition | Flat-vs-Curved | Curved-vs-Curved |
|--------|-----------|---------------|-----------------|
| **Recoverable** | W ≤ 12 (all pairs); W ≤ 30 (flat-vs-curved) | ✅ 100% | ✅ 100% |
| **Degraded** | W = 15-20 (curved-vs-curved only) | ✅ 100% | ⚠️ 33-67% |
| **Erased** | W ≥ 25 (curved-vs-curved) | ✅ 100% | ❌ 0% |

### Key Finding

**The W=20 "problem" is actually a phase boundary.** Degradation is **pair-dependent**, not universal:
- Flat-vs-curved pairs: ROBUST to W=30
- Curved-vs-curved pairs: DEGRADE at W=15-20, ERASE at W≥25

This transforms the original question from "Is geometry robust?" to **"Under what conditions does geometry remain spectrally recoverable?"**

---

## Strong Inference Results

| Hypothesis | Test | Result | Verdict |
|-----------|------|--------|---------|
| H1: Insufficient k | k=30 at W=20 → 86.7% | ✅ Confirmed | More eigenvalues help |
| H2: ML overfits | Train W≤10 → test W=20 = 80% | ❌ Killed | ML generalizes |
| H3: Laplacian loses signal | Indirect: k=30 helps | ⚠️ Partial | Signal recoverable |
| H4: Wrong features | 2 features → 100% | ✅ Confirmed | Feature selection critical |
| H5: Intrinsically similar | Phase 3 separation exists | ❌ Killed | Distinguishable at W=0 |
| H6: Threshold sufficient | Diff seeds → 48.3% | ❌ Killed | ML necessary |

---

## New Framing (2026-06-29)

> **We study when compact-product geometry fingerprints remain recoverable from spectra under disorder.**
>
> This produces a **phase diagram** with three regimes:
> - 🟢 **Recoverable**: geometry fingerprints distinguishable
> - 🟡 **Degraded**: partial distinguishability
> - 🔴 **Erased**: geometry information lost to disorder
>
> Not "geometry is always robust," but **regimes of spectral recoverability**.

---

## Operating Envelope

| Training | Test | Accuracy | Condition |
|----------|------|----------|-----------|
| W=0 | W ≤ 10 | 98-100% | Standard |
| W ≤ 10 | W = 20 | 80% | Conservative OOD |
| W ≤ 10 | W = 20 | 100% | Optimal (2 features) |
| Any | Flat-vs-curved, W ≤ 30 | 100% | Phase 4B confirmed |
| Any | Curved-vs-curved, W ≤ 12 | 100% | Phase 4B confirmed |
| Any | Curved-vs-curved, W ≥ 25 | 0% | Erased regime |
| Any | Multiclass | 15.8% | Fails |

---

## Reproduction Checklist

- [x] Phase 3 analytic fingerprints
- [x] Phase 4A ensemble (10 seeds, ablation)
- [x] Phase 4A ML + OOD
- [x] Phase 4A validation (7 checks)
- [x] Strong Inference crucial experiments (4 tests)
- [x] **Phase 4B phase diagram (NEW)**
- [ ] Phase 4C T4 baseline
- [ ] Phase 4D cross-geometry

---

## Files in Repo

```
experiments/
├── geometry_fingerprint_core.py              # Phase 3
├── phase4a_ensemble_full.py                  # Phase 4A ensemble
├── phase4a_ml_classifier_ood.py             # Phase 4A ML + OOD
├── phase4a_validation_minimal.py            # Phase 4A validation
├── phase4a_crucial_experiments.py           # Strong Inference 4 tests
├── phase4b_phase_diagram.py                 # Phase 4B (NEW)
├── 20260629-crucial-experiments/
│   └── crucial_results.json                 # {H2, H4, H1, H6}
└── 20260629-phase4b/
    └── phase4b_results.json                 # 35-cell phase diagram
```
