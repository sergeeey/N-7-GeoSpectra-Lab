# Reproducibility Manifest — GeoSpectra Lab

**Version:** v0.4a-paper-complete  
**Date:** 2026-06-30  
**Status:** PAPER_COMPLETE / REPRODUCIBILITY_LOCK_PENDING  
**Paper:** `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`

---

## Quick Start (one command)

```bash
git clone https://github.com/sergeeey/N-7-GeoSpectra-Lab.git
cd N-7-GeoSpectra-Lab
pip install numpy scipy scikit-learn
python experiments/hard_negatives_suite.py            # 3/4 PASS
python experiments/physics_rescue_track.py            # 4/4 KILLS
python experiments/phase4b_phase_diagram.py           # Phase diagram
```

---

## Environment

| Dependency | Version Used |
|-----------|-------------|
| Python | 3.10+ |
| numpy | 1.24+ |
| scipy | 1.11+ |
| scikit-learn | 1.3+ |

---

## Provenance Chain

| Phase | Script | JSON Artifact | Claim IDs | Status |
|-------|--------|--------------|-----------|--------|
| Phase 3 | `geometry_fingerprint_core.py` | Legacy JSON | #1 | REPRODUCED |
| Phase 4A | `phase4a_ensemble_full.py` | Legacy JSON | #2-3,5-6 | REPRODUCED |
| Phase 4A Validation | `phase4a_validation_minimal.py` | Legacy JSON | #4 | REPRODUCED |
| Phase 4A Crucial | `phase4a_crucial_experiments.py` | `20260629-crucial-experiments/crucial_results.json` | #7-10 | REPRODUCED |
| **Phase 4B** | **`phase4b_phase_diagram.py`** | **`20260629-phase4b/phase4b_results.json`** | **#12-14** | **STRUCTURE VERIFIED** |
| Phase 4C | `phase4c_t4_baseline.py` | `20260629-phase4c/phase4c_results.json` | #24 | VERIFIED |
| Phase 4D | `phase4d_cross_geometry.py` | `20260629-phase4d/phase4d_results.json` | #25 | VERIFIED |
| **Hard Negatives** | **`hard_negatives_suite.py`** | **`20260629-hard-negatives/hard_negatives_results.json`** | **#15-18** | **VERIFIED-SYNTHETIC** |
| **Physics Rescue** | **`physics_rescue_track.py`** | **`20260629-physics-rescue/physics_rescue_results.json`** | **#19-22** | **VERIFIED-DETERMINISTIC** |

---

## Claims → Evidence → Paper Section

See `CLAIMS_REGISTRY.md` for full 26-claim registry with levels and statuses.

---

## Freeze Notice

```
PUBLICATION FREEZE: v0.4a-paper-complete
No new scientific claims until REPRODUCIBILITY_LOCK.
Bug fixes and documentation OK.
```

---

## Next Milestones

| Milestone | Status |
|-----------|--------|
| REPRODUCIBILITY_LOCK | PENDING (figure generation, ML leakage checks) |
| arXiv submission | NOT STARTED |
| GitHub release v1.0 | NOT STARTED |
