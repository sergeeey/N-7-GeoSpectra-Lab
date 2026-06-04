# Raw Data Availability Audit — Gate 4B v0.1.24

**Date:** 2026-06-01  
**Purpose:** Identify which deeper diagnostics can run on existing v0.1.24 data WITHOUT rerun  
**Context:** Gate 4B v0.1.24 rerun attempted 2026-05-25, killed by OOM on Hetzner CPX42 15GB host after completing 216/216 cases. S³ Dirac operator corrected (commit `093573b` — added negative k₀ branch). Need to determine what analyses are possible on saved JSON before committing to memory-safe rerun.

---

## 1. Data Inventory [VERIFIED]

### Gate 4B v0.1.24
- **Location:** `reports/RUNS/gate4_fss_v0.1.24/batches/`
- **Structure:** 9 batches (batch_01 through batch_09)
- **Total cases:** 216 [VERIFIED — counted via Python across 9 results.json files]
- **Cases per batch:** 24 each
- **File format:** One `results.json` per batch containing array of case objects
- **Storage format:** JSON (aggregate metrics only, no raw arrays)

### Negative Controls v0.1.22
- **Location:** `reports/RUNS/negative_controls_v0.1.22/`
- **Structure:** 6 batches (batch_01 through batch_06)
- **Total cases:** 54 [VERIFIED — `find` command counted 54 case_*.json files]
- **Controls:** 3 types (random_hermitian, broken_wilson_term, random_eigenvectors)
- **Cases per control:** 18 (3 s1_sizes × 2 j_max values × 3 seeds)
- **File format:** One JSON file per case

### Total Files
~2282 JSON files total (includes batch config, status, summary, timing files)

---

## 2. Available Fields [VERIFIED]

Fields extracted from sample `results.json` (Gate 4B batch_01, case 0):

### Core Identifiers
- `case_id` (int) — position in batch
- `family` (str) — s1_family: "spectral_circle" or "spectral_linear"
- `disorder_strength` (int) — W ∈ {0, 20}
- `s1_size` (int) — N ∈ {16, 32, 64, 128}
- `j_max` (int) — S³ truncation cutoff ∈ {2, 3}
- `seed` (int) — random seed {123, 456, 789}

### Aggregate Metrics (Available)
- `true_ipr_mean` (float) — mean IPR across all eigenstates [VERIFIED]
- `r_stat` (float) — level spacing statistic (Oganesyan-Huse r-parameter) [VERIFIED]
- `mean_low_eigenvalue` (float) — mean eigenvalue in lowest 20% window [VERIFIED]
- `mean_low_ipr` (float) — mean IPR in lowest 20% eigenvalue window [VERIFIED]

### Metadata
- `runtime_sec` (float)
- `uses_eigenvectors` (bool) — always True for v0.1.24
- `ipr_metric_version` (str) — "v0.1.24_true_ipr_corrected_s3_dirac"
- `r_stat_available` (bool)
- `r_stat_reason` (str or null)
- `error` (str or null)

### Negative Controls Additional Fields
- `control` (str) — control type identifier
- `alpha` (float) — disorder parameter (0.0 for negative controls)
- `radius` (float) — geometry parameter
- `N` (int) — total Hilbert space dimension
- `meta` (dict) — includes construction details, s3_dimension, total_dimension

---

## 3. NOT Available (per-state data) [VERIFIED]

The following fields are **NOT present** in saved JSON:

❌ `eigenvalues` — array of per-state eigenvalues  
❌ `eigenvectors` — array of per-state eigenvector components  
❌ `per_state_ipr` — IPR for each eigenstate individually  
❌ `per_window_ipr` — IPR binned by energy windows  
❌ `ipr_vs_energy` — scatter data (E, IPR) pairs  
❌ `eigenvalue_multiplicity` — degeneracy counts  
❌ `zero_mode_count` — count of exact zero eigenvalues  
❌ `chirality_index` — n₊ − n₋ counts  
❌ `wavefunction_nulls` — zero-component counts in eigenvectors  
❌ `participation_entropy` — S = -∑ |ψᵢ|² log |ψᵢ|²  
❌ `multifractal_d2` — correlation dimension D₂

**Evidence:** [VERIFIED] Read `batch_01/results.json` line 1-100, extracted full field list via Python `sorted(batch[0].keys())` — only 16 top-level fields present, all aggregate metrics.

---

## 4. Analysis Feasibility Table

| Analysis | Required Data | Available? | Can Run Now? | Needs Rerun? | Notes |
|----------|---------------|------------|--------------|--------------|-------|
| **Aggregate Contrast by Control** | `true_ipr_mean` by family/W/control | ✅ Yes | ✅ Yes | No | Main Gate 4B claim — spectral_circle vs controls |
| **FSS Slope by Size** | `true_ipr_mean` vs `s1_size` | ✅ Yes | ✅ Yes | No | Finite-size scaling: log(IPR) ~ β log(N) |
| **r-statistic by Size/Control/W** | `r_stat` vs parameters | ✅ Yes | ✅ Yes | No | GOE/Poisson discrimination |
| **Seed Variance** | `true_ipr_mean` by seed ∈ {123, 456, 789} | ✅ Yes | ✅ Yes | No | Statistical stability check |
| **Mean Low-Energy Window IPR** | `mean_low_ipr`, `mean_low_eigenvalue` | ✅ Yes | ✅ Yes | No | Edge-state analysis (aggregate only) |
| **Disorder Comparison (W=0 vs W=20)** | `true_ipr_mean` by `disorder_strength` | ✅ Yes | ✅ Yes | No | Localization onset |
| **Energy-Resolved IPR** | per-state (E, IPR) pairs | ❌ No | ❌ No | ✅ Yes | Requires `eigenvalues[]` + `per_state_ipr[]` |
| **Eigenvalue Multiplicity** | per-state eigenvalue list | ❌ No | ❌ No | ✅ Yes | Degeneracy counts, gap detection |
| **Eigenvector Nulls** | per-state eigenvector arrays | ❌ No | ❌ No | ✅ Yes | Zero-component diagnostics |
| **Multifractal D₂** | eigenvector spatial structure | ❌ No | ❌ No | ✅ Yes | Correlation dimension, requires `eigenvectors[]` |
| **Participation Entropy** | per-state entropy -∑|ψᵢ|² log|ψᵢ|² | ❌ No | ❌ No | ✅ Yes | Alternative to IPR, needs per-state data |
| **Tail-Excised IPR** | per-state IPR with threshold cutoff | ❌ No | ❌ No | ✅ Yes | Needs `per_state_ipr[]` to excise outliers |
| **Chirality Index (n₊ − n₋)** | kernel/cokernel dimensions | ❌ No | ❌ No | ✅ Yes | Needs eigenvalue sign counts |
| **Zero-Mode Detection** | exact eigenvalue == 0 checks | ❌ No | ❌ No | ✅ Yes | Needs full eigenvalue list |
| **Spectral Gap vs Size** | min(|λᵢ - λⱼ|) for adjacent levels | ❌ No | ❌ No | ✅ Yes | Requires sorted eigenvalue array |

---

## 5. Verdict

**RAW_DATA_SUPPORTS_AGGREGATE_METRICS_ONLY**

### What CAN be done without rerun [VERIFIED]
1. **Main Gate 4B analysis:** Compare `true_ipr_mean` across spectral_circle vs negative controls (broken_wilson_term, random_hermitian, random_eigenvectors)
2. **Finite-size scaling:** Plot log(IPR) vs log(N) for s1_size ∈ {16, 32, 64, 128}, extract slope β
3. **r-statistic analysis:** GOE/Poisson discrimination by family, disorder, size
4. **Seed stability:** Variance across seeds {123, 456, 789} — confirms reproducibility
5. **Disorder onset:** W=0 vs W=20 IPR comparison
6. **Low-energy window:** Aggregate IPR and eigenvalue means in lowest 20% window

### What CANNOT be done without rerun [VERIFIED]
7. **Energy-resolved diagnostics:** IPR(E) scatter plots, energy-binned statistics
8. **Eigenvalue structure:** Multiplicity, gaps, zero-mode counts, chirality index
9. **Spatial diagnostics:** Eigenvector nulls, multifractal D₂, wavefunction localization patterns
10. **Refined IPR metrics:** Tail-excised IPR, participation entropy, per-window distributions
11. **Degeneracy analysis:** Systematic check for unexpected eigenvalue collisions
12. **Spectral flow:** Gap evolution with size/disorder (requires sorted eigenvalue lists)

### Key Limitation
**Broken_wilson_term control pattern (v0.1.21 finding) cannot be energy-resolved on current data.** The claim "broken_wilson_term reproduces spectral_circle aggregate IPR" can be verified, BUT the deeper question "does this match at ALL energies or only in aggregate?" requires per-state eigenvalues.

Harness nonspecificity hypothesis (claim that aggregate metrics miss geometry-specific structure) **cannot be tested** without energy-resolved data.

---

## 6. Implications for Memory-Safe Rerun

### If Main Claim Holds on Aggregate Data
- Gate 4B Core Result (spectral_circle mean IPR differs from all three controls) can be **finalized now** using existing v0.1.24 data
- Memory-safe rerun becomes **optional enhancement** for deeper energy-resolved diagnostics, NOT blocker for main publication claim
- Decision: analyze existing data first → if aggregate contrast is strong and statistically significant → memory-safe rerun downgrades to "future work" priority

### If Aggregate Data Is Inconclusive
- Must proceed with memory-safe rerun on ≥64 GiB host per `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`
- Add instrumentation to save `eigenvalues[]` and `per_state_ipr[]` to JSON output for energy-resolved follow-up

---

## 7. Recommended Next Steps [UNKNOWN — user decision required]

**Option A: Analyze Existing v0.1.24 Data First (Fast Path)**
1. Run aggregate analysis script on 216 Gate 4B cases + 54 negative control cases
2. Generate statistical summary: mean IPR by family/control, FSS slopes, r-stat distributions
3. If contrast is clear → write Gate 4B result section, defer energy-resolved work
4. Timeline: 1-2 days

**Option B: Memory-Safe Rerun with Extended Output (Deep Path)**
1. Provision ≥64 GiB host (Hetzner CPX51 or CCX33)
2. Modify harness to save `eigenvalues`, `eigenvectors`, `per_state_ipr` to JSON
3. Rerun heavy smoke case (N=128, j_max=3) to confirm no OOM
4. Rerun full 216-case grid with extended output
5. Timeline: 3-5 days (provisioning + rerun + storage ~50-100 MB/case)

**Option C: Hybrid (Recommended)**
1. Run Option A analysis on existing data (1-2 days)
2. If aggregate result is strong → freeze Gate 4B core claim
3. Queue Option B as separate "energy-resolved diagnostics" follow-up for referee response / extended version

---

## Appendix: File Counts [VERIFIED]

```bash
# Gate 4B batches
find reports/RUNS/gate4_fss_v0.1.24/batches/ -name "results.json" | wc -l
# → 9

# Negative controls cases
find reports/RUNS/negative_controls_v0.1.22/ -name "case_*.json" | wc -l
# → 54

# Total cases in Gate 4B
python -c "
import json
total = 0
for i in range(1, 10):
    with open(f'reports/RUNS/gate4_fss_v0.1.24/batches/batch_0{i}/results.json') as f:
        total += len(json.load(f))
print(total)"
# → 216
```

---

**Confidence:** [VERIFIED-HIGH] — all field lists extracted from actual JSON, file counts confirmed via bash tools, analysis feasibility based on documented field availability.

**Caveat:** This audit assumes JSON schema consistency across all 9 batches. Spot-checked batch_01 only. If later batches have different schema → re-verify.

**Next Artifact:** Analysis decision memo (Option A / B / C selection with justification).
