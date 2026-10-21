# Provenance of the FSS slope −0.4844 ± 0.0546 and "48σ" — status

**Status:** `PARTIALLY_TRACED — NUMBER REPRODUCED, ERROR AND 48σ NOT REPRODUCED`

Read-only trace, 2026-10-21. No repository file was modified. Environment: Python 3.13.2, numpy 2.3.4, scipy 1.16.3.

## 1. Where the data lives

- `reports/RUNS/` is listed in `.gitignore` (line 26). The per-case data were therefore **never committed**. This is why the GitHub branch shows no `gate4_fss_v0.1.24/batches/`. The data exist only on the machine where they were produced: `reports/RUNS/gate4_fss_v0.1.24/` (216 records, 9 batches, 0 errors) and `reports/RUNS/spectral_circle_extended_v0.1.22/` (18 records).
- Input checksums (sha256 over sorted per-file hashes): extended v0.1.22 folder `446123fc…5179`; v0.1.24 batch results `07afbd8d…b74`.

## 2. Which dataset produced −0.4844

The report `SPECTRAL_CIRCLE_EXTENDED_ANALYSIS_v0.1.24.md` (commit `82850a6`) cites an "18-case extended grid" for spectral_circle. Those 18 cases are in `reports/RUNS/spectral_circle_extended_v0.1.22/`, and **every record has `ipr_metric_version = v0.1.22_spectral_circle_extended`**. The report labels them v0.1.24. That is a version mix, which the project's own warning (`do not confuse historical versions`) forbids.

Reproduction at W = 20, j_max = 3, sizes 16/64/128, seeds 123/456/789:

| Estimator | Slope | Matches report |
|---|---|---|
| log(mean over seeds of IPR), OLS | −0.4900 | no |
| **mean over seeds of log(IPR), OLS** | **−0.4844** | **yes, exact to 4 d.p.** |
| average of per-seed slopes | −0.4844 | yes (identical here) |
| log(median), OLS | −0.4695 | no |

So −0.4844 is the **mean of log IPR** estimator applied to v0.1.22 data. The report's own appendix, which says "mean(log IPR)" and gives the IPR table, does not use that formula consistently: the table's values are not in this dataset (see §4).

## 3. Error ±0.0546 and "48σ"

- Seed-level standard error of the slope (3 per-seed slopes −0.4095, −0.5080, −0.5357; sd 0.0663; SE = sd/√3): **0.0383**. Not 0.0546.
- The 0.0546 is also not reproduced by a regression SE over sizes on the printed means (df = 1; `RESEARCH_AUDIT_REPORT.md` §1 gives 0.024 on the printed IPR values).
- Therefore the ±0.0546 is **not traced**. The "48σ" is not derivable from the displayed uncertainties (z ≈ 8.07 under independence; ≤ 18.6 under any correlation; `EVIDENCE_LEDGER.md` E1–E2).

## 4. The IPR table in the report does not match the data

Report appendix, spectral_circle W = 20: N = 16 → 0.267, N = 64 → 0.172, N = 128 → 0.129.
Raw v0.1.22 (identical to raw v0.1.24 at j_max = 3): N = 16 → 0.1879, N = 64 → 0.0871, N = 128 → 0.0694.

The printed IPR values are **not in either dataset**. Their origin is unknown. This is the second, independent reporting inconsistency.

## 5. A useful control already present in the data

Clean system (W = 0), extended v0.1.22: mean IPR 0.0625, 0.0156, 0.0078 at N = 16, 64, 128. Slope **−1.000** exactly, as expected for extended states (IPR ∝ 1/N). The W = 20 slope −0.49 lies between the extended limit (−1) and the flat localized limit (0). This is the correct relative comparison. Reading a falling IPR as "increasing localization" is not supported (`RESEARCH_AUDIT_REPORT.md`, §1; the IPR-definition point in the follow-up audit).

## 6. Consequences for the verdict

- The **direction and magnitude** of the spectral_circle slope (≈ −0.49 at W = 20) are reproduced from raw data by two estimators, within about 5 %.
- The **printed error bars**, the **48σ**, the **HIGH confidence**, and the **"reproduced on 2 independent grids"** claim are not supported. The 18-case and the 54-case runs share code and an old metric version, so they are not independent.
- The ring comparator (+0.016 at j_max = 3, v0.1.24 raw) is stable in sign and small in size, consistent with the report.

## 7. Open items

1. Find the script that wrote the report's IPR table (0.267/0.172/0.129). Check `reports/SPECTRAL_CIRCLE_EXTENDED_ANALYSIS_v0.1.24.md` git history and any other RUNS folder.
2. Find the source of ±0.0546 (regression on which dataset, which estimator).
3. Decide on the estimand before any new run: IPR, N·IPR, or the scaling exponent (plan item 1 of the approved plan).
4. Any new v0.1.24 spectral_circle data for the decision must use the corrected metric `v0.1.24_true_ipr_corrected_s3_dirac` and be pre-registered.

## Reproduction

Scratch scripts (outside the repository): `provenance_scripts/` (recompute_fss.py, recompute_ext022.py, estimators.py, se_check.py). Run with `python -I` from the repository root.
