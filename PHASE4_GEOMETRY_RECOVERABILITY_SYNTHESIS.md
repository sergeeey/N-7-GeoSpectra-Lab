# Phase 4: Geometry Recoverability Synthesis

**Date:** 2026-06-29 | **Status:** FROZEN | **Commit:** 4fc3770

## Central Claim

> Compact product geometries show hierarchical spectral recoverability: coarse flat-vs-curved fingerprints are robust under strong disorder, while fine curved-vs-curved distinctions exhibit threshold behavior. Spectral density is the dominant robust discriminator, and clean-trained ML generalizes OOD to disordered spectra.

## Allowed Claims

- Geometry fingerprints recoverable in tested toy benchmarks
- Spectral density is primary discriminator (99% effective)
- ML learns clean fingerprints and transfers to noisy spectra
- T4 anchor is universally disorder-robust
- Curved-vs-curved has W~20 threshold

## Forbidden Claims

- Does NOT prove physical compactification
- Does NOT prove Tom's full theory
- Does NOT derive Standard Model
- Does NOT fix lambda
- Does NOT claim multiclass works (15.8% < random)

## Experiment Ladder

| Phase | Result | Status |
|-------|--------|--------|
| 3 | 4 geometries distinguishable | FROZEN |
| 4C | 18/18 distinct on lattice | FROZEN |
| 4D v2 | 83% distinct, N>=300 | FROZEN |
| 4A Ensemble | 82% distinct, 10 seeds | FROZEN |
| 4A ML | RF 92% at W=20, 6/7 checks | FROZEN |
| 4A Multiclass | 15.8%, honest boundary | FROZEN |

## Honest Boundaries

| Works | Does Not Work |
|-------|--------------|
| T4 anchor: 100% | Multiclass: 15.8% |
| Pair-based: 66-93% | Compact N=240: 67% |
| 7/7 validation checks | Curved-only: weaker |
| Disorder to W=20 | Needs N>=400 |

## Reproduction

```bash
git clone https://github.com/sergeeey/N-7-GeoSpectra-Lab.git
git checkout 4fc3770
pip install numpy scipy scikit-learn
cd experiments/
python phase4a_ensemble_full.py
python phase4a_ml_classifier_ood.py
python phase4a_validation_minimal.py
```

**This package is FROZEN for preprint.**
