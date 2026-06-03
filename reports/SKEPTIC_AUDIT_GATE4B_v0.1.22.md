# Skeptic Audit — Gate 4B Claim (FL Context-Asymmetric Review)
# Pre-input for Estimand v0.1.22

**Date:** 2026-06-03
**Protocol:** FL Falsification Ladder — Context Asymmetry Rule
**Input given to skeptic:** claim.md text + raw JSON artifacts only (no success narrative)
**Input withheld:** session history, "PASS_WITH_CAVEATS" verdict prose, success logs
**Source artifacts:**
- `reports/S3_S1_GATE4B_FSS_RESULTS_v0.1.21.md`
- `reports/RUNS/gate4_fss_v0.1.21/merged/true_ipr_contrast_summary.json`
- `reports/RUNS/gate4_fss_v0.1.21/merged/r_stat_summary.json`
- `reports/RUNS/gate4_fss_v0.1.21/merged/size_scaling_summary.json`

---

## Claim Under Review

> "S³×S¹ Gate 4B supports finite-lattice robustness of the W=20 Anderson disorder localization
> signal under finite-size scaling from s1_size=16 to 128 (N = 112 to 896), with true
> eigenvector-based IPR contrast ≥2.0× and family consistency ≥2/3."

---

## Falsification Tests Generated

### FT-1: r(W=0) = 0.606 — anomalous baseline

**Hypothesis to falsify:** "r-statistic diagnostic consistent with localization interpretation."

**Raw finding from r_stat_summary.json:**

| Family | W=0 r_stat (all sizes) | Expected GOE |
|--------|------------------------|--------------|
| spectral_circle | **1.0000** (exact, all 4 sizes) | ≈0.530 |
| ring | 0.334, 0.493, 0.517, 0.410 | ≈0.530 |
| wilson_ring | 0.448, 0.378, 0.428, 0.258 | ≈0.530 |

**Aggregate r(W=0) = 0.606** is dominated by spectral_circle r=1.000.
Without spectral_circle: r(W=0) ≈ 0.41 — BELOW GOE, close to Poisson.

**Explanation:** spectral_circle at W=0 produces an exactly equidistant spectrum
(r=1.000 is the theoretical value for perfectly uniform level spacing). This is a
structural property of the discretization, not a physical ergodic state.

**Consequence for Δr = -0.163 claim:** The aggregate r-shift is predominantly driven
by spectral_circle going from 1.000 → ~0.44 under disorder. A r-shift from a
degenerate baseline to near-GOE under ANY perturbation is trivially expected and
carries no localization-specific information. The ring and wilson_ring r-shift
does not show a clean GOE→Poisson transition (non-monotone by size).

**Verdict:** `[CLOSED-REVEALS-DEEPER]`
- Cause identified: spectral_circle structural degeneracy.
- Deeper issue opened: r-statistic diagnostic is contaminated by spectral_circle.
  r-stat is NOT a reliable secondary confirmation for this grid without
  per-family analysis.

---

### FT-2: spectral_circle IPR(W=20) decreases with N

**Hypothesis to falsify:** "All three discretization families independently confirm
W=20 localization signal."

**Raw IPR(W=20) extracted from true_ipr_contrast_summary.json (mean over seeds × j_max):**

| s1_size | ring IPR(W=20) | wilson_ring IPR(W=20) | spectral_circle IPR(W=20) |
|---------|---------------|----------------------|--------------------------|
| 16      | 0.326         | 0.252                | 0.175                    |
| 32      | 0.322         | 0.241                | 0.150                    |
| 64      | 0.320         | 0.235                | 0.087                    |
| 128     | 0.339         | 0.266                | 0.070                    |
| **Trend** | **FLAT** ✓  | **FLAT** ✓           | **DECREASING ↓ 2.5×** ✗ |

**spectral_circle W=0 IPR = exactly 1/s1_size** (independent of j_max):
0.0625, 0.03125, 0.015625, 0.0078125 — precisely 1/N_s1.

**Three convergent signals that spectral_circle is structurally anomalous:**
1. r(W=0) = 1.000 → equidistant spectrum (not ergodic/GOE)
2. IPR(W=0) = 1/s1_size exactly (independent of j_max) → block-diagonal structure,
   eigenstates confined to S¹ sector, not spread over full (2j+1)×s1_size Hilbert space
3. IPR(W=20) decreases 2.5× as N grows 8× → NO localization plateau

**Consequence:** spectral_circle passes the pre-registered contrast threshold (2.8–8.9×
ratio) because the denominator IPR(W=0) = 1/s1_size shrinks exactly as 1/N.
The contrast strengthening is driven by denominator mechanics, NOT by a
numerator plateau that would indicate localization.

**For ring and wilson_ring:** IPR(W=20) is flat (0.32–0.34 and 0.24–0.27
respectively). Their FSS strengthening is a genuine localization signature.

**Verdict:** `[OPEN]`
The "3/3 families independently confirm" claim is technically correct by the
pre-registered ≥2.0× threshold, but is physically misleading. spectral_circle
and ring/wilson_ring show qualitatively different behavior. The claim should be
qualified: "2/3 families show genuine IPR plateau (ring, wilson_ring);
spectral_circle passes threshold via denominator scaling."

**Minimum required to close:** Run spectral_circle on scrambled/random geometry
with same W=20. If spectral_circle shows the same decreasing IPR(W=20) pattern
regardless of geometry → structural artifact confirmed, not geometry-specific.

---

### FT-3: FSS "STRENGTHENING" — artifact for spectral_circle

**Hypothesis to falsify:** "FSS trend STRENGTHENING (3.76× → 24.90×) indicates
localization signal is NOT a finite-size artifact."

**Raw contrast by s1_size from reports (pre-registered aggregate):**

| s1_size | N (j_max=3) | Contrast | ring IPR(W=20) | w_ring IPR(W=20) | sc IPR(W=20) |
|---------|-------------|----------|---------------|-----------------|-------------|
| 16      | 112         | 3.76×    | 0.326 (flat)  | 0.252 (flat)    | 0.175 (↓)   |
| 32      | 224         | 6.73×    | 0.322 (flat)  | 0.241 (flat)    | 0.150 (↓)   |
| 64      | 448         | 11.93×   | 0.320 (flat)  | 0.235 (flat)    | 0.087 (↓)   |
| 128     | 896         | 24.90×   | 0.339 (flat)  | 0.266 (flat)    | 0.070 (↓)   |

**Verdict — split by family:**

| Family | FT-3 status | Reason |
|--------|-------------|--------|
| ring | `[CLOSED]` | IPR(W=20) flat 0.326→0.339 — genuine localization plateau |
| wilson_ring | `[CLOSED]` | IPR(W=20) flat 0.252→0.266 — genuine localization plateau |
| spectral_circle | `[OPEN]` | IPR(W=20) decreases 0.175→0.070 — contrast driven by 1/N denominator |

The aggregate FSS "STRENGTHENING" claim is valid for ring and wilson_ring.
It is NOT valid for spectral_circle as a localization claim.

---

## Summary for Estimand v0.1.22

| FT | Status | Action required |
|----|--------|-----------------|
| FT-1 r anomaly | `[CLOSED-REVEALS]` | Per-family r-stat analysis; r-stat reliability caveat to CLAIMS doc |
| FT-2 spectral_circle artifact | `[OPEN]` | **Primary target for v0.1.22**: negative control for spectral_circle |
| FT-3 FSS ring/wilson_ring | `[CLOSED]` | No action needed |
| FT-3 FSS spectral_circle | `[OPEN]` | Scrambled geometry test for spectral_circle |

**Key question for v0.1.22 estimand:**
> Is spectral_circle a valid discretization showing weaker localization,
> or a structural artifact that passes the ≥2.0× threshold by a different mechanism?

If ARTIFACT → Gate 4B "3/3 PASS" should be qualified to "2/3 PASS (ring + wilson_ring),
spectral_circle structurally indeterminate."
If VALID → must explain why IPR(W=20) decreases with N despite disorder.

---

**Status:** FINAL — input to ESTIMAND_v0.1.22.md
**Date:** 2026-06-03
