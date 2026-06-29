# GeoSpectra Experiments - Phase 4 Package

**Status:** BENCHMARK_HARDENING_COMPLETE_FOR_PHASE4B_V1
**Date:** 2026-06-29

## Framing

> We study when compact-product geometry fingerprints remain recoverable from
> finite spectra under disorder.

This is a synthetic/toy **recoverability benchmark**, not a proof of physical
compactification or Standard Model derivation.

## Quick Start

```bash
pip install numpy scipy scikit-learn
python phase4a_ensemble_full.py                 # Phase 4A ensemble + ablation
python phase4a_ml_classifier_ood.py             # ML + OOD
python phase4a_validation_minimal.py            # 7-check validation
python phase4a_crucial_experiments.py           # Strong Inference tests
python phase4b_phase_diagram.py                 # Legacy fixed-threshold diagnostic
python phase4b_recoverability_benchmark.py --quick
python phase4b_recoverability_benchmark.py --seeds 10 --k-values 15 30
```

Run commands from the `experiments/` directory or pass the paths from the repo root.

## Experiment Index

| File | Phase | What it does | Evidence role |
|---|---|---|---|
| `geometry_fingerprint_core.py` | 3 | Analytic 4-geometry discrimination | L4 synthetic benchmark |
| `phase4a_ensemble_full.py` | 4A | Ensemble 10 seeds + ablation | Spectral-density legacy core evidence |
| `phase4a_ml_classifier_ood.py` | 4A | ML classifier + OOD | Moderate-disorder check |
| `phase4a_validation_minimal.py` | 4A | 7-check validation suite | Audit support |
| `phase4a_crucial_experiments.py` | 4A | Strong Inference tests | Exploratory; rerun-inconsistent values |
| `phase4b_phase_diagram.py` | 4B | Legacy `sd > 4` phase diagnostic | Synced diagnostic, not final proof |
| `phase4b_recoverability_benchmark.py` | 4B | AUC/separation/bootstrap/k benchmark | Primary strict benchmark |

## Current Honest Results

### Positive Legacy Claim

Spectral density is the dominant discriminator inside the original Phase 4A/4B
protocols.

- Current level: **L4 CORE, protocol-bound**.
- It remains useful, but it is not an L5 physical or universal recoverability
  claim.

### New Strict Benchmark Boundary

The strict benchmark asks a harder question:

> Are cross-geometry spectral-density distances larger than same-geometry
> seed/disorder variation?

Full run:

```bash
python experiments/phase4b_recoverability_benchmark.py --seeds 10 --k-values 15 30
```

Result:

| Quantity | Value |
|---|---:|
| Cells | 72 |
| Recoverable | 6 |
| Degraded | 0 |
| Erased | 66 |
| Recoverable W values | W=0 only |
| k=30 W>0 rescues | 0 |

Interpretation:

- Under strict AUC-vs-within variation, the current spectral-density distance is
  **not recoverable for W>0**.
- `k=30` does **not** rescue W>0 in this benchmark version.
- The failure mode is not "no signal exists"; it is that same-geometry disorder
  variation is as large as or larger than cross-geometry separation.

## Phase 4B Legacy Diagnostic

The old fixed-threshold script is retained for continuity, but it should not be
used as publication-grade evidence by itself.

Clean rerun diagnostic output:

| Quantity | Value |
|---|---:|
| Grid cells | 36 |
| Recoverable | 30 |
| Degraded | 0 |
| Erased | 6 |

Important corrections:

- The old committed JSON/documentation said 35 cells; the script now emits and
  saves 36 cells.
- The current threshold rules produce **0 degraded cells**, so "three regimes
  discovered" is downgraded.
- `T4_vs_S2xS2` at W=20 is present and recoverable in the legacy rerun.
- Curved-vs-curved high-W behavior is fragile and non-monotonic: W=15,20,25,30
  are weak/erased in the legacy grid, while W=18 is recoverable.

## Benchmark Metrics

Primary metric:

- AUC of cross-geometry spectral-density distances versus same-geometry
  seed-to-seed spectral-density distances.

Secondary metrics:

- Relative separation.
- Bootstrap 95% CI.
- k-rescue delta: `k=30` versus `k=15`.

Pre-registered labels:

| Label | Rule |
|---|---|
| recoverable | `AUC >= 0.90` and `relative_separation >= 1.0` |
| degraded | `AUC >= 0.70` or `relative_separation >= 0.5` |
| erased | otherwise |

## k=30 Rescue Mechanism

`k=30` was tested as the main rescue mechanism in the strict benchmark.

Current result:

- `k=30` did not promote any W>0 cell to recoverable or degraded.
- It remains an exploratory direction only if paired with better normalization or
  richer features.

## Claim Boundary

Allowed:

- Benchmark recoverability under a toy generator.
- Pair-dependent robustness or fragility under disorder.
- Algorithmic comparison of `k`, AUC, and spectral-density features.
- Negative benchmark boundaries.

Not allowed from this evidence alone:

- Physical compactification proof.
- Standard Model derivation.
- Quantum-foam or real-physics claims.

Those remain `[NEEDS-REAL-DATA]`.

## Data

```python
import json

with open('experiments/20260629-phase4b/phase4b_results.json') as f:
    legacy = json.load(f)

with open('experiments/20260629-phase4b/phase4b_benchmark_results.json') as f:
    benchmark = json.load(f)
```

## Next Gates

1. Add hard negatives: label permutation, N-shuffle, same-geometry controls,
   unseen-W grid.
2. Test normalization/alignment that reduces same-geometry disorder variation.
3. Test richer feature vectors beyond spectral-density distance alone.
4. Re-run with N=500 and at least 20 seeds.
5. Promote only cells whose lower 95% AUC CI stays above 0.80.

## Phase 4B Feature Benchmark V2

V2 implements the next rescue mechanisms:

- better normalization/alignment,
- relative spectra,
- heat-kernel/zeta/moments,
- multi-feature fingerprints,
- pair-calibrated metrics,
- AUC against same-geometry variation,
- 20 seeds,
- disorder-invariant spacing features,
- unfolded spacing spectra.

Run:

```bash
python experiments/phase4b_feature_benchmark.py --seeds 20 --n-values 300 --k-values 15 30 --bootstrap 100
```

Result:

| Metric | Value |
|---|---:|
| Best-by-cell entries | 72 |
| Recoverable | 14 |
| Degraded | 11 |
| Erased | 47 |
| W>0 recoverable cells | 8 |
| W>=25 recoverable/degraded cells | 0 |

Main findings:

- `moments` rescue flat-vs-curved at W=1/2.
- `heat_zeta` and `unfolded_spacing` give degraded flat-vs-curved cells at
  W=5/8/18/20.
- Curved-vs-curved is not rescued.
- High disorder W>=25 remains erased.
- `k=30` is not the main rescue in V2: it has the same recoverable count as
  k=15 and fewer degraded cells.
- Pair calibration is not the dominant winning mechanism in this run.

Evidence status: **L3 exploratory positive**. Because V2 chooses the best feature
mode per cell, it needs held-out feature selection and hard negatives before any
L4/L5 promotion.

Next expensive gates:

```bash
python experiments/phase4b_feature_benchmark.py --seeds 20 --n-values 500 --k-values 15 30 --bootstrap 100
python experiments/phase4b_feature_benchmark.py --seeds 20 --n-values 800 --k-values 15 30 --bootstrap 100
```
