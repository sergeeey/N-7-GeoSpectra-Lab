# Gate 4B IPR Contrast — No-Compute Statistical Re-analysis (2026-06-07)

> **GENERATED, NOT VALIDATED.** Numbers below come from re-analysis of the 216 already-stored `true_ipr_mean` scalars (gate4_fss_v0.1.24). No eigensolve, no operator build. Adversarial falsification of H1-H3 (skeptic / falsification-ladder) is a separate, still-pending step.

## Purpose

Address hypothesis-red-team AOS gaps (was 40/100) using only re-analysis. Replaces arithmetic-ratio-of-means with paired Wilcoxon + geometric-mean ratio, adds multiple-comparison correction and a specification curve.

## Data provenance [VERIFIED]

- Source: `reports/RUNS/gate4_fss_v0.1.24/batches/*/results.json`
- Cases: 216 | matched W=0 vs W=20 pairs: 72
- Pairing key: family, s1_size, j_max, seed
- Pre-registered threshold: contrast >= 2.0x

## A. Correct test (was: arithmetic ratio of means)

| Quantity | Value |
|---|---|
| Geometric-mean ratio (primary) | **8.386x** |
| Geometric-mean ratio 95% CI (bootstrap) | [7.019, 10.038] |
| Arithmetic ratio of means (old number) | 7.068x |
| Median of per-pair ratios | 7.653x |
| Wilcoxon signed-rank stat | 2628.0 |
| Wilcoxon p (one-sided, W20>W0) | 8.294e-14 |
| Cohen's d_z (log scale) | 2.721 |
| Common-language effect (P(W20>W0)) | 1.000 |
| Passes 2x on geometric ratio? | True |

## B. Multiple-comparison correction (subgroup claims)

Per-subgroup geometric contrast + Wilcoxon p, with BH-FDR (dependent tests) and Holm.

| Subgroup | n | geo contrast | raw p | BH-FDR | Holm | passes 2x |
|---|---:|---:|---:|---:|---:|---|
| family=ring | 24 | 10.358 | 5.96e-08 | 1.07e-07 | 4.17e-07 | True |
| family=spectral_circle | 24 | 5.112 | 5.96e-08 | 1.07e-07 | 4.17e-07 | True |
| family=wilson_ring | 24 | 11.140 | 5.96e-08 | 1.07e-07 | 4.17e-07 | True |
| size=16 | 18 | 3.545 | 3.81e-06 | 3.81e-06 | 1.53e-05 | True |
| size=32 | 18 | 6.413 | 3.81e-06 | 3.81e-06 | 1.53e-05 | True |
| size=64 | 18 | 10.530 | 3.81e-06 | 3.81e-06 | 1.53e-05 | True |
| size=128 | 18 | 20.666 | 3.81e-06 | 3.81e-06 | 1.53e-05 | True |
| j_max=2 | 36 | 8.419 | 1.46e-11 | 6.55e-11 | 1.31e-10 | True |
| j_max=3 | 36 | 8.354 | 1.46e-11 | 6.55e-11 | 1.31e-10 | True |

## C. Specification curve (multiverse over aggregation — H1)

- Specs tested: 30 (3 central tendencies x 4 groupings, all subsets)
- Specs passing 2x: 30 / 30
- **robust_fraction = 1.000**  (AOS +5 if > 0.70)
- Contrast range across specs: [3.545x, 29.855x]

> Limitation: this multiverse covers only the AGGREGATION axis. The spectrum-fraction axis (bottom 5/10/20%) needs per-state IPR, which is NOT stored — that axis remains compute-bound.

## D. Tipping point (robustness boundary — H3)

- IPR_W0 baseline would need to be ~4.19x larger (or IPR_W20 that much smaller) to drag the geometric contrast below 2.0x.

## E. Leave-one-family-out (replication PROXY — H2)

| Held-out family | geo on kept 2 | geo on held | kept passes | held passes |
|---|---:|---:|---|---|
| ring | 7.546 | 10.358 | True | True |
| spectral_circle | 10.742 | 5.112 | True | True |
| wilson_ring | 7.276 | 11.140 | True | True |

- All folds stable: **True**
> Caveat: LOGO is internal partition on the SAME codebase/machine. It softens but does NOT close T10 (true independent replication).

## Power (T6) — honest non-fix

- Observed Cohen's d_z (log) = 2.721, n = 72
- Power given OBSERVED d_z = 1.000
- This is the OBSERVED effect size, not an a-priori power analysis. Post-hoc power is a deterministic function of the p-value and does NOT recover the T6 (winner's curse) protection. A genuine a-priori power analysis requires a NEW pre-registered run.

## AOS impact (re-analysis only)

| Gap | Before | After re-analysis | Recovered |
|---|---|---|---|
| correct_test (Wilcoxon + geo-ratio) | +0 | +8 | YES |
| multiple_comparison (BH-FDR + Holm) | +0 | +8 | YES |
| robust_fraction (spec-curve > 0.70) | +0 | +5 | YES |
| multiverse (full) | +0 | partial | spectrum axis compute-bound |
| power a-priori (T6) | +0 | +0 | NO — needs new pre-reg run |
| independent_replication (T10) | +0 | +0 | NO — LOGO is proxy only |

**Estimated AOS after re-analysis: 40 + 8 + 8 + 5 = 61/100** (crosses 60 -> CONFIRMATORY WITH CAVEATS).

## What this does NOT mean

1. Does NOT validate S3xS1 as a physical geometry (S3 Dirac is a diagonal mockup).
2. Does NOT establish a thermodynamic limit (tested N <= 896).
3. Does NOT replace independent replication or a-priori power.
4. The numbers are GENERATED here; adversarial falsification is still pending.

## Provenance

- Script: `scripts/reanalyze_gate4b_stats.py` (no eigensolve)
- Companion audit: hypothesis-red-team (AOS 40/100, 2026-06-07)
