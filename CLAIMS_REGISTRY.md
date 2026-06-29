# Claims Registry - GeoSpectra Lab

**Version:** 2026-06-29
**Method:** Reproduction audit + recoverability benchmark protocol
**Status:** BENCHMARK_HARDENING_COMPLETE_FOR_PHASE4B_V1

This registry tracks benchmark evidence only. It does not promote toy spectral
recoverability into a physical compactification claim.

## Evidence Levels

| Level | Definition |
|---|---|
| **L5** | Core benchmark claim: script + JSON + clean rerun + bootstrap CI + hard negatives |
| **L4** | Strong reproduced benchmark claim: script + JSON + clean rerun, but missing CI or hard negatives |
| **L3** | Exploratory reproduced claim: script + one run, limited seeds or no independent rerun |
| **L2** | Partial/unstable claim: artifact exists, but results are inconsistent or weaker than stated |
| **L1** | Speculative interpretation: narrative only or outside current benchmark scope |

## Registry

| # | Claim | Current value | Level | Artifact | Notes |
|---|---|---:|---|---|---|
| 1 | Phase 3: four geometries analytically distinct | GEOMETRY_DISTINCT (HIGH) | **L4** | `geometry_fingerprint_core.py` | Reproduced benchmark fact, still synthetic/toy |
| 2 | Spectral density is the dominant legacy discriminator | 99.2% legacy ensemble | **L4 CORE** | `phase4a_ensemble_full.py` | Core legacy claim, but not L5 under stricter AUC benchmark |
| 3 | Ensemble overall distinctness | 76.5% | **L3** | `phase4a_ensemble_full.py` | Weaker than original 82% claim |
| 4 | Validation suite | 6 PASS + 1 NOTE | **L4** | `phase4a_validation_minimal.py` | Good audit evidence, still toy/synthetic |
| 5 | ML OOD for W <= 10 | 98-100% | **L3** | `phase4a_ml_classifier_ood.py` | Moderate-disorder benchmark result under that protocol |
| 6 | ML OOD at W=20, clean train only | 62.5% | **L3** | `phase4a_ml_classifier_ood.py` | Documents distribution shift weakness |
| 7 | W=20 salvaged by training on W <= 10 | 70-80% rerun-inconsistent | **L2** | `phase4a_crucial_experiments.py` | Prior committed value and clean rerun differ |
| 8 | Two-feature model rescues W=20 | 96.7-100% rerun-inconsistent | **L2** | `phase4a_crucial_experiments.py` | Promising but not stable enough for L4/L5 |
| 9 | k=30 improves W=20 in old protocol | 86.7-90.0% rerun-inconsistent | **L2** | `phase4a_crucial_experiments.py` | Not confirmed by strict AUC benchmark |
| 10 | Fixed threshold is robust | 48.3-50.0% | **L2** | `phase4a_crucial_experiments.py` | Fixed threshold is not a core method |
| 11 | Multiclass classification works | 15.8% | **L2** | Missing script | Boundary/failure result |
| 12 | Phase 4B legacy fixed-threshold grid | 36 cells: 30 recoverable, 0 degraded, 6 erased | **L3** | `phase4b_phase_diagram.py` | Diagnostic only; now synced to script output |
| 13 | Flat-vs-curved robust to W=30 under legacy threshold | W >= 1 only | **L3** | `phase4b_phase_diagram.py` | Killed by stricter AUC-vs-within benchmark |
| 14 | Curved-vs-curved high-W fragility under legacy threshold | W=15/20/25/30 weak, W=18 outlier | **L3** | `phase4b_phase_diagram.py` | Not a clean phase boundary |
| 15 | AUC/relative-separation benchmark | 72 cells: 6 recoverable, 0 degraded, 66 erased | **L4 NEGATIVE** | `phase4b_recoverability_benchmark.py` | Only W=0 recoverable; W>0 erased under same-geometry variation baseline |
| 16 | k=30 as main rescue mechanism | Not supported in AUC benchmark | **L4 NEGATIVE** | `phase4b_recoverability_benchmark.py` | k=30 did not promote any W>0 cell to recoverable/degraded |
| 17 | Phase 4C T4 baseline | Unknown | **L2** | Missing | Needs script + JSON |
| 18 | Phase 4D cross-geometry transfer | Unknown | **L2** | Missing | Needs script + JSON |
| 19 | Physical compactification claim | Not supported | **L1** | None | `[NEEDS-REAL-DATA]` |
| 20 | Standard Model / quantum foam derivation | Not supported | **L1** | None | Explicitly outside benchmark scope |

## Core Claim

The strongest surviving positive claim is:

> Spectral density is the dominant discriminator inside the original legacy
> Phase 4A/4B protocols.

Evidence status: **L4 CORE, protocol-bound**.

The stricter benchmark adds a new negative claim:

> When recoverability is measured as cross-geometry separation against
> same-geometry seed/disorder variation, all W>0 cells are erased in the current
> N=300, 10-seed, k in {15,30} run.

Evidence status: **L4 NEGATIVE benchmark boundary**.

## Phase 4B Results

### Legacy fixed-threshold diagnostic

- 36 total cells, not 35.
- 30 recoverable cells.
- 0 degraded cells.
- 6 erased cells.
- `T4_vs_S2xS2` at W=20 is present and recoverable in the rerun.

### Strict AUC-vs-within benchmark

- 72 total cells: 12 W values x 3 pairs x 2 k values.
- 6 recoverable cells: all at W=0.
- 0 degraded cells.
- 66 erased cells.
- k=30 does not rescue any W>0 cell under the pre-registered rule.

## Updated Interpretation

The project should now be framed as a recoverability benchmark with two layers:

1. **Legacy absolute-separation layer:** spectral density can separate some
   geometry pairs by a fixed threshold, but this is threshold-sensitive.
2. **Strict relative-recoverability layer:** once same-geometry seed/disorder
   variation is the baseline, geometry information is not recoverable for W>0 in
   the current setup.

This is valuable because it identifies the real failure mode: disorder-induced
within-geometry variation dominates cross-geometry spectral-density separation.

## Benchmark Path To L5

L5 positive claims now require a method that beats the strict benchmark:

1. Add hard negatives: label permutation, N-shuffle, same-geometry controls,
   unseen-W grid.
2. Test richer features beyond spectral-density distance alone.
3. Test whether alignment/normalization reduces within-geometry disorder
   variation.
4. Re-run with N=500 and at least 20 seeds.
5. Promote only cells whose lower 95% AUC CI stays above 0.80.

## Files

```text
RECOVERABILITY_BENCHMARK_PROTOCOL.md
experiments/phase4b_phase_diagram.py
experiments/phase4b_recoverability_benchmark.py
experiments/20260629-phase4b/phase4b_results.json
experiments/20260629-phase4b/phase4b_benchmark_results.json
```
