# GeoSpectra Recoverability Benchmark Protocol

**Version:** 2026-06-29
**Status:** PRE-REGISTERED_BENCHMARK_PROTOCOL
**Scope:** Synthetic/toy spectral recoverability benchmark, not a proof of physics.

## Objective

Measure when compact-product geometry fingerprints remain recoverable from finite
spectral samples under disorder.

The benchmark question is:

> Given geometry pair, disorder level `W`, resolution `N`, seed count, and number
> of eigenmodes `k`, how separable are spectra generated from different
> geometries relative to same-geometry seed variation?

## Claim Boundary

This protocol supports benchmark claims only.

| Claim type | Allowed status |
|---|---|
| Algorithmic recoverability under the toy generator | Allowed |
| Relative robustness of geometry pairs under the toy generator | Allowed |
| `k=30` as a benchmark rescue mechanism | Allowed if pre-registered metrics improve |
| Physical compactification or Standard Model derivation | Not supported |
| Real-world physics validation | `[NEEDS-REAL-DATA]` |

## Evidence Levels

| Level | Meaning | Minimum evidence |
|---|---|---|
| **L5** | Core benchmark claim | Script + JSON + clean rerun + bootstrap CI + negative controls |
| **L4** | Strong reproduced benchmark claim | Script + JSON + clean rerun, but missing CI or hard negatives |
| **L3** | Exploratory reproduced claim | Script + one run, no independent rerun or limited seeds |
| **L2** | Narrative/partial claim | Some artifact exists, but result is unstable or inconsistent |
| **L1** | Speculative interpretation | No decisive script/JSON evidence |

## Pre-Registered Metrics

Primary metric:

- **AUC** between cross-geometry spectral-density distances and same-geometry
  seed-to-seed spectral-density distances.

Secondary metrics:

- **Relative separation**:
  `(mean_between - mean_within) / pooled_std`.
- **Bootstrap 95% CI** for AUC and relative separation.
- **k-rescue delta**:
  `AUC(k=30) - AUC(k=15)` and `separation(k=30) - separation(k=15)`.

Why AUC:

- It avoids the old fixed threshold artifact (`sd > 4`).
- It compares against same-geometry variation, not an absolute magic number.
- It remains meaningful when raw spectral-density scales drift with `W`.

## Phase Labels

The labels are benchmark labels, not physical phases.

| Label | Pre-registered rule |
|---|---|
| **recoverable** | `AUC >= 0.90` and `relative_separation >= 1.0` |
| **degraded** | `AUC >= 0.70` or `relative_separation >= 0.5` |
| **erased** | Otherwise |

For publication-facing claims, use the bootstrap CI:

- Strong recoverable: lower 95% AUC CI >= 0.80.
- Fragile recoverable: point estimate passes, lower CI does not.
- Erased: upper 95% AUC CI <= 0.65.
- Ambiguous: CI crosses the decision boundary.

## Seed Policy

Exploratory runs may use 3 seeds.

Core benchmark runs must use:

- `seeds >= 10`
- `N >= 300`
- at least `k in {15, 30}`

Publication-quality runs should add:

- `N = 500`
- at least 20 seeds
- hard negatives: label permutation, N-shuffle, same-geometry controls, and
  unseen-W grid.

## k=30 Rescue Test

`k=30` is treated as the primary rescue mechanism only if:

1. `AUC(k=30) - AUC(k=15) >= 0.05`, or
2. `relative_separation(k=30) - relative_separation(k=15) >= 0.5`, and
3. the improvement appears on the hard curved-vs-curved pair, not only on easy
   flat-vs-curved pairs.

If the improvement is below threshold, `k=30` remains an exploratory optimization,
not a core claim.

## Kill Conditions

Downgrade or kill a recoverability claim if any of these occur:

- Label permutation exceeds real-label AUC within CI.
- Same-geometry controls look as separable as cross-geometry pairs.
- Results reverse under seed expansion from 3 to 10.
- `k=30` only helps by increasing noise scale without improving AUC/separation.
- A claimed phase boundary depends on a single W point or one seed.

## Current Interpretation

The current Phase 4B fixed-threshold script is retained as a legacy diagnostic.
It is not sufficient for L5 claims because it uses an absolute `sd > 4`
threshold and produced a documented 35/36-cell JSON mismatch.

The benchmark path is:

1. Synchronize legacy JSON to the current script output.
2. Run the AUC/separation benchmark with 10 seeds.
3. Compare `k=15` and `k=30`.
4. Add hard negatives.
5. Promote only stable benchmark claims to L5.

## Benchmark V1 Result (2026-06-29)

A full run was completed with:

```bash
python experiments/phase4b_recoverability_benchmark.py --seeds 10 --k-values 15 30
```

Observed result:

| Metric | Value |
|---|---:|
| Total cells | 72 |
| Recoverable | 6 |
| Degraded | 0 |
| Erased | 66 |
| Recoverable W values | W=0 only |
| k=30 W>0 rescues | 0 |

Interpretation:

- The old fixed-threshold diagnostic and the strict AUC-vs-within benchmark are
  measuring different questions.
- Under the strict benchmark, same-geometry seed/disorder variation dominates
  spectral-density cross-geometry separation for W>0.
- The next research target is not to defend the old threshold, but to find
  normalization, richer features, or model protocols that beat this stricter
  baseline.
