# Gate 4B v0.1.24 Download Summary

**Date:** 2026-05-31 20:58 UTC  
**Status:** ✅ COMPLETE

---

## Download Verification

**Server:** Hetzner CX52 (<user>@<hetzner-server-ip>)  
**Download method:** tar + scp (rsync не установлен локально)  
**Download time:** ~2 minutes

---

## Results Summary

### Batches
- **Total batches:** 9/9 ✅
- **All batches present:** batch_01 through batch_09

### Cases
- **Total cases:** 216/216 ✅
- **Success:** 216 (100%)
- **Failed:** 0 (0%)

**Breakdown by batch:**
```
Batch 1: 24 cases, 24 success, 0 failed
Batch 2: 24 cases, 24 success, 0 failed
Batch 3: 24 cases, 24 success, 0 failed
Batch 4: 24 cases, 24 success, 0 failed
Batch 5: 24 cases, 24 success, 0 failed
Batch 6: 24 cases, 24 success, 0 failed
Batch 7: 24 cases, 24 success, 0 failed
Batch 8: 24 cases, 24 success, 0 failed
Batch 9: 24 cases, 24 success, 0 failed
```

---

## Rerun Details

**Operator version:** S³ Dirac corrected (commit `093573b`)
- k=0 negative branch restored
- λ = -3/2 eigenvalue present

**IPR metric:** `v0.1.24_true_ipr_corrected_s3_dirac`
- Eigenvector-based true IPR
- Corrected from v0.1.21 eigenvalue proxy

**Grid parameters:**
- Families: spectral_circle, ring, wilson_ring (3)
- Disorder W: 0, 12, 20 (3)
- S¹ sizes: 16, 32, 64, 128 (4)
- j_max: 2, 3 (2)
- Seeds: 123, 456, 789 (3)
- **Total:** 3 × 3 × 4 × 2 × 3 = **216 cases**

**Server specs:**
- Model: Hetzner Cloud CX52
- RAM: 32 GB (peak usage ~6.7 GB)
- CPU: 16 vCPU shared
- Storage: 640 GB SSD
- OS: Ubuntu 24.04 LTS

**Runtime:**
- Started: 2026-05-31 14:28 UTC
- Finished: 2026-05-31 20:58 UTC (~16:58 local Kazakhstan)
- **Total:** ~6.5 hours wall time
- **CPU time:** ~403 minutes (6.7 hours compute)

**Performance:**
- Average per case: ~1.8 minutes
- Heavy cases (N=128 j_max=3): ~120 seconds
- Light cases (N=16 j_max=2): ~0.5 seconds
- Batches processed sequentially (no parallelization)

---

## File Structure

```
reports/RUNS/gate4_fss_v0.1.24/
├── batches/
│   ├── batch_01/
│   │   ├── results.json        (24 cases)
│   │   ├── batch_config.json
│   │   ├── timing.json
│   │   ├── status.json
│   │   └── summary.md
│   ├── batch_02/
│   │   └── ... (same structure)
│   └── ... (batch_03 through batch_09)
├── config.json                 (grid configuration)
└── gate4_fss_v0.1.24_run.log   (full run log)
```

---

## Next Steps

1. **Comparison analysis** (v0.1.21 vs v0.1.24)
   - Fill template: `reports/GATE_4B_v0.1.24_COMPARISON_TEMPLATE.md`
   - Calculate aggregate IPR contrast
   - Check FSS trend preservation
   - Determine verdict: PRESERVED / WEAKENED / DISAPPEARED

2. **IF signal PRESERVED:**
   - Resume Negative Controls batches 3-6 (~6 hours)
   - Proceed to Gate 5 planning
   - Update methodology paper

3. **IF signal WEAKENED/DISAPPEARED:**
   - Diagnostic investigation
   - Methodology paper pivot (negative result)
   - Update Zenodo DOI with caveat

4. **Server cleanup:**
   - Delete Hetzner CX52 server (Hetzner Console)
   - Cost: €29.95 (minimum 1 month billing)

---

## Data Provenance

**Location:** `E:\Проверка Гипотез\работаю над проверкой гипотез\N-7-GeoSpectra-Lab\reports\RUNS\gate4_fss_v0.1.24\`

**Excluded from git:** Yes (reports/RUNS/ in .gitignore)
- Results too large for git (~50 MB)
- Local storage only
- Backup via Zenodo DOI upload (after comparison analysis)

**Integrity:**
- All 9 batches present
- All 216 cases complete
- 0 failures recorded
- Checksums: [TODO if needed for archival]

---

**Status:** ✅ READY FOR ANALYSIS  
**Next action:** Fill comparison template and determine scientific verdict
