# GeoSpectra Experiments

**Current Status:** `PAPER_COMPLETE / REPRODUCIBILITY_LOCK_PENDING`

**Preprint:** `paper/WHEN_GEOMETRY_BECOMES_UNRECOVERABLE.md`
**Claims Registry:** `CLAIMS_REGISTRY.md`
**Reproducibility Manifest:** `REPRODUCE.md` (this repo root)

---

## What is GeoSpectra?

GeoSpectra is a falsification-first computational benchmark for testing when compact product geometries remain spectrally recoverable under finite resolution and disorder.

The current preprint reports a verified phase diagram of geometry recoverability across analytic, finite-lattice, cross-geometry, disorder, ML-OOD, hard-negative, and physics-rescue protocols.

**This repository does not** claim to derive the Standard Model, prove physical compactification, or validate quantum gravity. It provides a reproducible spectral-geometry benchmark with explicit claims governance.

---

## Quick Start

```bash
git clone https://github.com/sergeeey/N-7-GeoSpectra-Lab.git
cd N-7-GeoSpectra-Lab
pip install numpy scipy scikit-learn

# Core results (3 commands, all deterministic except Phase 4B)
python experiments/hard_negatives_suite.py          # 3/4 PASS
python experiments/physics_rescue_track.py          # 4/4 KILLS
python experiments/phase4d_cross_geometry.py        # 3/3 DISTINCT
```

---

## Experiment Index

| Script | Phase | Runtime | Status |
|--------|-------|---------|--------|
| `geometry_fingerprint_core.py` | 3 | 5s | REPRODUCED |
| `phase4a_ensemble_full.py` | 4A | 250s | REPRODUCED |
| `phase4a_ml_classifier_ood.py` | 4A | 120s | REPRODUCED |
| `phase4a_validation_minimal.py` | 4A | 120s | REPRODUCED |
| `phase4a_crucial_experiments.py` | 4A | 180s | REPRODUCED |
| `phase4b_phase_diagram.py` | 4B | 300s | **STRUCTURE VERIFIED** |
| `phase4c_t4_baseline.py` | 4C | 60s | VERIFIED |
| `phase4d_cross_geometry.py` | 4D | 30s | VERIFIED |
| `hard_negatives_suite.py` | Kill-tests | 60s | **VERIFIED-SYNTHETIC** |
| `physics_rescue_track.py` | No-go | 2s | **VERIFIED-DETERMINISTIC** |

---

## Key Results

- **Phase diagram:** 3 regimes (recoverable / degraded / erased)
- **Flat-vs-curved:** recoverable to W=30
- **Curved-vs-curved:** degrades at W=15-20, erases at W>=25
- **Hard negatives:** 3/4 PASS (no hallucination)
- **Physics rescue:** 4/4 KILLS (no-go confirmed for S³×S⁶)
- **Cross-geometry:** 3/3 DISTINCT

---

## Freeze Notice

```
PUBLICATION FREEZE: v0.4a-paper-complete
No new scientific claims until REPRODUCIBILITY_LOCK.
Bug fixes and documentation OK.
```

**Next milestones:** REPRODUCIBILITY_LOCK → arXiv → GitHub release v1.0 → journal submission.
