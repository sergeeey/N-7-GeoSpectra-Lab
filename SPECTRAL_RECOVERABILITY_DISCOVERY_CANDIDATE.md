# Spectral Recoverability Discovery Candidate

**Date:** 2026-07-03  
**Status:** [VERIFIED-SYNTHETIC, n=3] · CANDIDATE — requires N-axis + AUC + more seeds  
**Evidence:** `experiments/20260629-phase4b/phase4b_results.json`  
**Hard fence:** DISCRETIZATION_SENSITIVE — signal reflects lattice product structure,
not S³×S¹ physics specifically (CLAIMS_REGISTRY final verdict)

---

## 1. Claim

> In the tested compact product geometry benchmark (S³×S¹, S²×S², T⁴),
> spectral recoverability is **pair-type-dependent and disorder-dependent**,
> exhibiting at least two distinct regimes:
>
> (R1) **Flat-vs-curved pairs** (T⁴ vs S³×S¹, T⁴ vs S²×S²): erased at zero
> disorder, recoverable across the full tested disorder window W∈[1,30].
>
> (R2) **Curved-vs-curved pair** (S³×S¹ vs S²×S²): immediately recoverable
> at zero disorder, but erases at high disorder W≥25.

One sentence version:
> **Spectral recoverability forms a pair-dependent phase structure: disorder reveals flat-vs-curved separation but destroys curved-vs-curved separation.**

---

## 2. Prior art

| Work | What they did | How this differs |
|------|--------------|----------------|
| Kac (1966) "Can you hear the shape of a drum?" | Hearing geometry from Laplacian spectrum — negative answer (Gordon 1992) | G-W-W: different drums with same spectrum exist. We ask: when is recovery possible *statistically* under disorder? |
| Reuter & Saueressig (2012) spectral geometry | Quantum gravity spectral action | Physics context; we study algorithmic recoverability as a benchmark |
| Zuk et al. (2014) diffusion maps | Geometric inference from stochastic graph | Different feature (diffusion time vs Laplacian eigs); no phase diagram |
| LabelProp / spectral clustering literature | Spectral methods for graph learning | Not focused on geometry type; no flat/curved distinction |

**Literature gap:** No prior work characterizes a phase diagram of spectral geometric *type* recoverability as a function of disorder level and geometry pair type. Kac asks "can you?"; we ask "under what conditions, and for which geometry pairs?"

---

## 3. Novel findings (current evidence)

**N1 — Pair-type asymmetry at W=0:**  
At zero disorder, curved-vs-curved (S³×S¹ vs S²×S²) is immediately separable
(sd_acc=1.00), while flat-vs-curved (T⁴ vs any) is not (sd_acc=0.33).
This suggests the mean spectral density alone separates curved geometries
but not flat-vs-curved; disorder is required to reveal the flat-vs-curved distinction.

**N2 — Disorder window: recovery of flat-vs-curved:**  
At W=1, T⁴ vs curved pairs flip from ERASED to RECOVERABLE (sd_acc=1.00).
This is a threshold effect: small disorder reveals the flat-vs-curved fingerprint.
Interpretation: disorder excites modes that differ structurally between flat and curved.

**N3 — High-disorder erasure: curved-vs-curved only:**  
At W≥25, S³×S¹ vs S²×S² erases (sd_acc=0.0), while T⁴ vs curved pairs
remain fully recoverable (sd_acc=1.00). Flat torus spectral signature is MORE robust
to high disorder than the curved-vs-curved distinction.

| Phase | W range | T4_vs_S3xS1 | T4_vs_S2xS2 | S3xS1_vs_S2xS2 |
|-------|---------|-------------|-------------|-----------------|
| Flat-erased, curved-ok | W=0 | ERASED(0.33) | ERASED(0.33) | RECOV(1.00) |
| All recoverable | W=1–20 | RECOV(1.00) | RECOV(1.00) | RECOV(1.00) |
| Curved-erased, flat-ok | W≥25 | RECOV(1.00) | RECOV(1.00) | ERASED(0.00) |

---

## 4. Kill tests

| # | Kill condition | Status |
|---|----------------|--------|
| K1 | Phase structure disappears at N≠300 (lattice artifact) | **NOT TESTED — critical** |
| K2 | Phase structure disappears with different discretization scheme | **NOT TESTED — DISCRETIZATION_SENSITIVE** |
| K3 | n_samples=3 is insufficient; results reverse at n=20+ | **HIGH RISK — n=3 is very small** |
| K4 | AUC (pre-registered metric) does not show same structure | **NOT COMPUTED — required** |
| K5 | Null baseline (random spectra) shows same structure | **NOT TESTED** |
| K6 | Phase boundary at W=15/25 is a threshold artifact of the sd_acc≥0.67 criterion | **LIKELY — criterion not pre-registered** |

**Status: K1–K6 all required before CLAIM status.** Current evidence is
[VERIFIED-SYNTHETIC, n=3] — directional signal, not statistical claim.

---

## 5. Current evidence [VERIFIED-SYNTHETIC, N=300, n=3]

### 5.1 Phase diagram (W × pair, N=300 fixed)

```
W=0 :  T4 vs S3xS1 = ERASED(0.33)   T4 vs S2xS2 = ERASED(0.33)  S3xS1 vs S2xS2 = RECOV(1.00)
W=1 :  all RECOVERABLE (1.00)
W=2 :  all RECOVERABLE (1.00)
...
W=20:  T4 pairs RECOV, S3xS1_vs_S2xS2 ERASED(0.33)
W=25:  T4 pairs RECOV, S3xS1_vs_S2xS2 ERASED(0.00)
W=30:  T4 pairs RECOV, S3xS1_vs_S2xS2 ERASED(0.00)
```

Critical gap: **only N=300 tested.** Phase diagram has no N-axis.

### 5.2 What n=3 means

Each (W, N, pair) point is estimated from 3 samples. sd_acc ∈ {0.0, 0.33, 0.67, 1.0}
are the ONLY possible values at n=3. The "transitions" at W=15,25 may be noise.
Required: n≥20 per point for meaningful sd_acc values.

### 5.3 Pre-registered metric NOT computed

RECOVERABILITY_BENCHMARK_PROTOCOL.md specifies AUC as primary metric.
The current results use sd_acc (accuracy of 3-way classification), which was
NOT the pre-registered metric. This is a protocol deviation.

---

## 6. Boundary (what this does NOT prove)

1. **Not physics.** The verdict on Track A is DISCRETIZATION_SENSITIVE / GEOMETRY_AGNOSTIC.
   The signal reflects lattice product structure, not S³×S¹ or S²×S² physics. This is a
   computational geometry benchmark, not a physics claim.

2. **Not proven at N≠300.** All data at N=300. The phase structure may be N-dependent.

3. **Not proven with n≥20.** Statistically weak at n=3.

4. **Not AUC-validated.** Pre-registered metric not computed.

5. **Not comparable to prior work.** No comparison with literature baselines (random spectra,
   known spectral geometry algorithms).

---

## 7. Predictions (if confirmed with proper statistics)

**P1 — Phase boundary shifts with N:**  
Larger N → more spectral resolution → phase boundaries may shift to higher W.
Prediction: at N=1000, curved-vs-curved erasure threshold shifts to W>40.

**P2 — AUC reproduces phase structure:**  
AUC between cross-geometry and same-geometry distances should show same 3-regime structure
(low, high, decreasing for curved-vs-curved). If AUC doesn't match sd_acc pattern → sd_acc
was measuring something other than geometry type.

**P3 — Flat torus robustness:**  
The T⁴ spectral signature should be more robust under high disorder than curved geometry pairs.
This could reflect that T⁴ has a simpler spectral density (uniform modes) that remains
identifiable even under noise, while curved geometries' spectral density differences wash out.

---

## 8. Required work to promote to CLAIM

### Priority 1 (critical, ~2 hours of compute)

Run `phase4b_phase_diagram.py` with:
- N ∈ {50, 100, 200, 300, 500, 1000}
- n_seeds = 20 per point
- Compute AUC (pre-registered metric) in addition to sd_acc

This produces a proper W×N phase diagram with statistical confidence.

### Priority 2 (statistical rigor, ~1 hour)

Bootstrap CI for each (W, N, pair) point:
- Bootstrap 1000 resamples of the n=20 seeds
- Report AUC ± 95% CI
- Phase boundary = W at which AUC drops below 0.7

### Priority 3 (null baseline, ~30 min)

Add null geometry: random Laplacian eigenvalues (not from any geometry).
- Confirms the phase structure is NOT a random artifact
- Allows comparison: "our curved/flat signal vs pure noise"

### Priority 4 (write-up, ~1 week)

If P1-P3 pass: 8-10 page benchmark paper:

```
Title: Disorder-Dependent Phase Structure of Spectral Geometric Type Recoverability
       in Compact Product Manifolds

Contribution:
  - First characterization of flat-vs-curved vs curved-vs-curved recoverability regimes
  - Phase diagram: W × N with AUC and bootstrap CI
  - Dishonest: DISCRETIZATION_SENSITIVE caveat prominent in abstract
```

---

## 9. Claim entropy (Perelman)

| Component | Count |
|-----------|-------|
| N_unsupported_HIGH | 3 (K1/K2/K3 not run) |
| N_hidden_assumptions | 2 (n=3 sufficient; sd_acc = pre-registered metric) |
| N_missing_negative_controls | 2 (null baseline; N variation) |
| N_ambiguous | 1 (phase boundary criterion) |
| **claim_entropy** | **8** |

Target for CLAIM: claim_entropy = 0.  
**Minimum viable step:** run with N∈{50,100,200,300} and n=20. Drops entropy to ~2.
