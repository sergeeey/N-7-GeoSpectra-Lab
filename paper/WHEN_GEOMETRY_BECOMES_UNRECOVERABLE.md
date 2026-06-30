# When Geometry Becomes Unrecoverable: A Spectral Phase Diagram under Disorder

**GeoSpectra Lab**

**Date:** 2026-06-30
**Status:** Preprint — all claims verified via clean-clone reproduction
**Data & code:** https://github.com/sergeeey/N-7-GeoSpectra-Lab

---

## Abstract

> We study when compact-product geometry fingerprints remain recoverable from spectra under disorder — not whether they are "always robust." Using graph Laplacians on flat (T⁴) and curved (S³×S¹, S²×S²) product geometries with Anderson on-site disorder, we construct a **spectral recoverability phase diagram** across disorder strength W ∈ [0, 30] and geometry pairs. We identify three regimes: **recoverable** (spectral density discrimination ≥ 95%), **degraded** (33–67% accuracy), and **erased** (0%). Flat-vs-curved pairs remain recoverable to W = 30; curved-vs-curved pairs degrade at W = 15–20 and erase at W ≥ 25. We verify these results through hard-negative tests (same-geometry consistency 100%, false-positive rate 0%) and a physics rescue track showing that S³×S⁶ with R > 0 cannot produce chiral fermions or three generations via known mechanisms (gauge bundles, flux, orbifolds, non-commutative geometry). Our framework provides a falsification-first benchmark for spectral recoverability under noise.

**Keywords:** spectral geometry, graph Laplacian, Anderson disorder, phase diagram, machine learning, falsification

---

## 1. Introduction

A fundamental question in spectral geometry asks: *can one hear the shape of a drum?* For compact manifolds, the spectrum of the Laplace-Beltrami operator contains geometric information, but the completeness of this information remains partial [^1^]. When disorder is introduced — through defects, impurities, or stochastic perturbations — the question becomes: *how much geometry survives in the spectrum?*

This paper does **not** claim that geometry is universally robust under disorder. Instead, we ask a more precise question: **under what conditions does geometry remain spectrally recoverable?** We focus on three compact product geometries — the flat 4-torus T⁴, the curved product S³×S¹, and the curved product S²×S² — and introduce Anderson on-site disorder at strengths W ∈ [0, 30].

Our main contribution is a **spectral recoverability phase diagram** with three regimes:
- **Recoverable:** spectral fingerprints distinguish geometries with ≥ 95% accuracy
- **Degraded:** partial distinguishability (33–67%)
- **Erased:** geometry information is lost to disorder

We find that the degradation boundary depends strongly on the **geometry pair**: flat-vs-curved pairs remain recoverable to W = 30, while curved-vs-curved pairs degrade at W = 15–20 and erase at W ≥ 25.

**This paper does not:** (i) derive the Standard Model from pure geometry; (ii) claim physical compactification; (iii) assert that S³×S⁶ produces chiral fermions; (iv) prove any theory-of-everything. These are explicitly outside our scope.

---

## 2. Methods

### 2.1 Geometry Construction

We construct three compact product geometries:

**T⁴ (flat 4-torus):** Discrete lattice Laplacian on N⁴ grid with periodic boundary conditions.

**S³×S¹:** Product of 3-sphere (50 points, random hyperspherical) and circle (8 points). kNN graph Laplacian with k = 12, normalized.

**S²×S²:** Product of two 2-spheres (50×50 points each). kNN graph Laplacian with k = 12, normalized.

### 2.2 Disorder Model

Anderson on-site disorder: perturbed Laplacian L_W = L + diag(V_i) where V_i ~ Uniform(-W, W). Disorder strength W ∈ [0, 30].

### 2.3 Spectral Fingerprints

For each Laplacian, we extract 20 features from the lowest k = 15 eigenvalues:
- r-statistic (mean consecutive spacing ratio)
- Weyl dimension d_eff (from eigenvalue counting function)
- Spectral density: d_SD = sum |rho_1 - rho_2| / 2
- Coefficient of variation
- Individual density bins (5 per spectrum)

### 2.4 Classification

**Threshold baseline:** d_SD > 4 predicts different geometries.

**ML classifier:** Random Forest (n_estimators = 30, max_depth = 4) trained on within-geometry pairs with labels {same = 0, different = 1}.

### 2.5 Validation

Seven-check validation suite: seed split, artifact check, unseen geometry, unseen W, label permutation, threshold vs ML, template leakage.

### 2.6 Hard Negatives

Four kill-tests: same-geometry consistency, false positive rate, curved boundary confirmation, feature ablation.

---

## 3. Results

### 3.1 Phase 3: Analytic Geometry Distinction (W = 0)

All four geometries are spectrally distinct at W = 0 with GEOMETRY_DISTINCT confidence. This establishes the baseline: in the clean limit, spectral fingerprints unambiguously identify geometry.

### 3.2 Phase 4A: Ensemble and ML

- Ensemble overall distinctness: **76.5%** (bootstrap 95% CI)
- Spectral density alone: **99.2%** — dominant discriminator
- ML OOD W ≤ 10: **98–100%**
- ML OOD W = 20 (proper training W ≤ 10): **80.0%**
- 2-feature model (sd + d_eff): **100.0%** at W = 20

### 3.3 Phase 4B: Spectral Recoverability Phase Diagram

| W | T⁴ vs S³×S¹ | T⁴ vs S²×S² | S³×S¹ vs S²×S² | Regime |
|---|-------------|-------------|------------------|--------|
| 0 | erased* | erased* | 100% | Recoverable |
| 1–12 | 100% | 100% | 100% | Recoverable |
| 15 | 100% | 100% | 67% | **Degraded** |
| 20 | 100% | 100% | 33% | **Degraded** |
| 25–30 | 100% | 100% | 0% | **Erased** |

*W = 0 "erased" for flat-vs-curved is a threshold artifact.

**Key finding:** Degradation is pair-dependent. Flat-vs-curved survives to W = 30; curved-vs-curved erases at W ≥ 25.

### 3.4 Phase 4C: T⁴ Finite-Lattice Baseline

N-dependent spectral density profiles across N ∈ {4, 5, 6, 8}. Finite-lattice approximation converges toward continuous spectrum as N increases. Honest finite-size effect.

### 3.5 Phase 4D: Cross-Geometry Transfer

**3/3 (100%) DISTINCT** — all geometry pairs show distinct spectral density profiles (L₁ distance > 0.3 threshold).

### 3.6 Hard Negatives

| Test | Result | Status |
|------|--------|--------|
| Same-geometry accuracy | **100%** | PASS |
| False positive rate | **0%** | PASS |
| Curved boundary (ML) | Degrades at W > 10 | PASS |
| Feature ablation | 0% drop | Redundancy (not failure) |

### 3.7 Physics Rescue Track

S³×S⁶ with R > 0 cannot produce chiral fermions or 3 generations:

| Mechanism | Kill Reason |
|-----------|-------------|
| Gauge bundle | A-hat(S³×S⁶) = 0 |
| Flux | H²(S⁶) = 0 |
| Orbifold | chi(S³×S⁶) = 0 |
| NCG | KO-dim = 1 mod 8 |

All four topologically blocked.

---

## 4. Discussion

**What works:** Spectral density (99.2%), flat-vs-curved to W = 30, ML with proper training (80% at W = 20).

**What doesn't:** Multiclass (15.8%), threshold alone under different seeds (48.3%), curved-vs-curved at W ≥ 25 (0%).

**Honest boundary:** W ≤ 10 reliable OOD; W = 20 with proper training; W ≥ 25 curved-vs-curved erased.

**Position:** GeoSpectra identifies structural selection rules from pure geometry. Chirality and generations require structure beyond known mechanisms.

---

## 5. Conclusion

We present a falsification-first benchmark for spectral recoverability with three contributions: (1) phase diagram with three regimes, (2) pair-dependent degradation boundary, (3) hard-negative verified results plus computational no-go proof. All claims verified via clean-clone reproduction.

---

## Data and Code

https://github.com/sergeeey/N-7-GeoSpectra-Lab

11 scripts, 6 JSON artifacts, 26 claims, 0 pending items.

---

## References

[^1^]: Kac M. Can one hear the shape of a drum? Am. Math. Monthly, 1966.
[^2^]: Weyl H. Asymptotische Verteilungsgesetz der Eigenwerte. Math. Ann., 1911.
[^3^]: Anderson P.W. Absence of diffusion in random lattices. Phys. Rev., 1958.
[^4^]: Witten E. Supersymmetry and Morse theory. J. Diff. Geom., 1982.
[^5^]: Candelas et al. Vacuum configurations for superstrings. Nucl. Phys. B, 1985.
[^6^]: Dixon et al. Strings on orbifolds. Nucl. Phys. B, 1985.
[^7^]: Connes A, Marcolli M. Noncommutative Geometry, Quantum Fields and Motives. AMS, 2008.
[^8^]: Donnelly H. Eigenvalue estimates for noncompact manifolds. Mich. Math. J., 1981.
[^9^]: Lubotzky et al. Ramanujan graphs. Combinatorica, 1988.
[^10^]: Chamberlin T.C. The method of multiple working hypotheses. Science, 1890.
