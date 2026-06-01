# Diagnostic Sprint Plan — Gate 4B v0.1.24 Negative Controls Follow-Up

**Date:** 2026-06-01  
**Status:** 🔬 **DIAGNOSTIC_SPRINT_PLAN_READY_FOR_REVIEW**  
**Context:** Harness nonspecificity finding from Negative Controls v0.1.22 (2/3 controls PASSED unexpectedly)

---

## 1. Purpose

Plan a **diagnostic sprint** to investigate why Negative Controls v0.1.22 showed unexpected results (2/3 controls PASSED when all should have FAILED), and to determine whether the issue is:

- **Harness nonspecificity** (Gate 4B signal is generic disorder effect, not S³×S¹ coupling), OR
- **Control construction error** (controls not implemented per pre-registration), OR
- **Metric insufficiency** (aggregate IPR contrast hides geometry-specific signatures), OR
- **Operator implementation** (both Gate 4B and controls share a common bug)

**Critical constraint:** This sprint is **design-first**, focused on **what to measure and how**, NOT on running expensive compute. Heavy reruns are deferred until diagnostic design is validated.

---

## 2. Current Problem

### ✅ Gate 4B Signal Survived S³ Dirac Correction

**v0.1.21 (frozen):** 7.15× contrast (S³ Dirac operator missing negative k=0 branch)  
**v0.1.24 (corrected):** 7.07× contrast (S³ Dirac operator corrected, commit `093573b`)  

**Signal change:** −1.1% (preserved across operator fix) [VERIFIED-REAL — Gate 4B v0.1.24 raw run data]

**Assessment:** ✅ **Signal robust to operator correction** — this was initially promising.

---

### ❌ Negative Controls Reproduced Full Pattern

**Expected:** All 3 controls < 2.0× contrast (controls FAIL to reproduce signal → harness specific)

**Observed (v0.1.22, 54 cases total):**

| Control | Contrast | Threshold | Result | Expected |
|---------|----------|-----------|--------|----------|
| random_hermitian | 1.30× | < 2.0× | ✅ FAIL | ✅ FAIL |
| scrambled_geometry | **4.25×** | < 2.0× | ❌ **PASS** | ✅ FAIL |
| broken_wilson_term | **8.20×** | < 2.0× | ❌ **PASS** | ✅ FAIL |

**Gate 4B baseline:** 7.07× (v0.1.24)

**Comparison:**
- scrambled_geometry: **60% of Gate 4B signal** (geometry scrambled but 4.25× contrast remains)
- broken_wilson_term: **116% of Gate 4B signal** (Wilson disabled but signal ENHANCED, not destroyed)

[VERIFIED-REAL — Negative Controls v0.1.22 reproducibility audit completed 2026-05-31, 54/54 cases verified]

---

### 🚨 Harness Nonspecificity Finding

**Preliminary verdict (from `reports/NEGATIVE_CONTROLS_AUDIT_SUMMARY_2026-05-31.md`):**

> ⚠️ **HARNESS_NONSPECIFIC_PENDING_REPRODUCIBILITY_AUDIT** — Gate 4B harness **cannot distinguish** S³×S¹ signal from broken/scrambled baselines.

**Critical implications:**
1. **Geometry nonspecific:** scrambling S³ indices reduces signal from 7.07× to 4.25× (−40%), but does NOT destroy it (should be < 2.0×)
2. **Wilson irrelevant:** disabling Wilson term **increases** signal to 8.20× (+16%) instead of destroying it
3. **FSS trend stable:** preliminary FSS slope analysis shows **positive trend in ALL three controls** (weak/negative trend expected)

[INFERRED from reproducibility audit data — not yet independently verified via control construction code review]

---

### 📊 Current Metrics Insufficient for S³×S¹ Specificity

**Current harness uses aggregate metrics only:**
- `true_ipr_mean` (mean IPR across all eigenstates)
- `r_stat` (level-spacing statistic, ensemble-averaged)
- Contrast = `mean(W=20 IPR) / mean(W=0 IPR)`

**Problem:** No per-state resolution, no energy-resolved structure, no S³ degeneracy tracking.

**Missing dimensions:**
- Per-eigenvalue IPR (localization vs. energy)
- S³ quantum number resolution (k, j in S³ Dirac spectrum)
- S¹ momentum distribution (compactification signature)
- Control-normalized effect (specificity score)

[INFERRED from OUTCOMES.md §A4 and current `cc_toy_lab/spectral/metrics.py` implementation]

---

## 3. Diagnostic Questions

### Q1. Is broken_wilson_term code truly "broken" or spectrally similar?

**Context:**  
broken_wilson_term (Wilson disabled) shows **8.20× contrast** vs. Gate 4B (Wilson enabled) **7.07× contrast** (+16%).

**Hypotheses:**
- **H1.1:** `wilson_mode: disabled` is implemented correctly, Wilson term genuinely irrelevant for localization
- **H1.2:** `wilson_mode: disabled` is misimplemented, accidentally fixes a different bug
- **H1.3:** Wilson term **suppresses** localization (counter-intuitive), removal enhances signal

**Diagnostic test:**
- **Code audit:** Read `cc_toy_lab/controls/negative_controls.py` or `s3_s1_product_discretized.py`, trace Wilson term construction for both `wilson_ring` (Gate 4B) and `disabled` (control)
- **Operator comparison:** Export `H_S³×S¹` matrix for one matched case (same N, j_max, s1_size, seed, W=20) from both Gate 4B and broken_wilson_term → compute Frobenius norm of difference
- **Eigenvalue scatter:** Plot eigenvalue spectrum of both → if identical, operators are the same

**Priority:** 🔴 **CRITICAL** — if operators are identical, "control" is not a control

**Requires compute:** ❌ NO (code audit only) for initial hypothesis triage; ✅ YES (single-case operator comparison) for definitive test

**Required data:** Gate 4B v0.1.24 raw output (available), broken_wilson_term v0.1.22 raw output (available)

---

### Q2. Is Wilson term load-bearing for the localization signal?

**Context:**  
If Wilson term is irrelevant (H1.1), then S¹ discretization family (spectral_circle / ring / wilson_ring) may be cosmetic, and localization is driven entirely by S³ Dirac + disorder.

**Hypotheses:**
- **H2.1:** Wilson term is load-bearing → broken_wilson_term MUST show weaker signal (data contradicts this)
- **H2.2:** Wilson term is cosmetic → disabling has no effect (data shows +16% enhancement, contradicts this)
- **H2.3:** Wilson term **anti-correlates** with localization → removing it strengthens signal

**Diagnostic test (Wilson Relevance Ablation):**
- Run Gate 4B grid with **Wilson explicitly disabled** in `spectral_circle` family (cleanest S¹ discretization)
- Compare to current Gate 4B (Wilson enabled in `wilson_ring`)
- If new contrast ≈ 7.07× (unchanged) → H2.2 (cosmetic)
- If new contrast > 7.07× → H2.3 (anti-correlates)
- If new contrast < 7.07× → H2.1 (load-bearing)

**Priority:** 🟡 **HIGH** — determines whether S¹ discretization is meaningful or arbitrary

**Requires compute:** ✅ **YES** (216-case rerun with Wilson disabled)

**Required data:** None (new experiment)

---

### Q3. Does FSS slope separate intact from controls better than contrast?

**Context:**  
Preliminary FSS analysis (from audit) shows:
- Gate 4B: **positive FSS slope** (localization strengthens with N)
- broken_wilson_term: **positive FSS slope** (same trend!)
- scrambled_geometry: **weak positive slope** (trend preserved)

**Hypotheses:**
- **H3.1:** FSS slope is more specific than aggregate contrast (slope distinguishes geometry from disorder)
- **H3.2:** FSS slope is equally nonspecific (all controls show positive slope)
- **H3.3:** Slope + contrast **joint metric** separates intact from controls

**Diagnostic test (FSS Slope Reanalysis):**
- Recompute FSS slope for all 4 conditions (Gate 4B, random_hermitian, scrambled_geometry, broken_wilson_term) using existing v0.1.22 data
- Plot: slope vs. aggregate contrast (2D scatter, 4 points)
- **Decision rule proposal:** `Specificity Score = Effect(Gate 4B) − max(Effect(controls))` where Effect = weighted combination of contrast + slope

**Priority:** 🟡 **HIGH** — may rescue harness specificity without rerun

**Requires compute:** ❌ **NO** (reanalysis of existing data)

**Required data:** Negative Controls v0.1.22 full grid (available)

---

### Q4. Are tail states dominating aggregate IPR?

**Context:**  
Aggregate IPR (`true_ipr_mean`) averages over ALL eigenstates, including band edges and mid-spectrum. If localization is energy-dependent (e.g., Anderson mobility edge), aggregate may hide structure.

**Hypotheses:**
- **H4.1:** Localization is uniform across spectrum → aggregate IPR is sufficient
- **H4.2:** Localization concentrated in tail states (high/low energy) → aggregate dilutes signal
- **H4.3:** Localization in mid-spectrum only → tail states are delocalized but dominate count

**Diagnostic test (Energy-Resolved IPR):**
- For ONE representative case (Gate 4B, W=20, N=128, j_max=3), compute per-eigenvalue IPR(λ)
- Plot IPR vs. eigenvalue index (sorted by energy)
- Identify localization band: where is IPR > threshold?
- Compute **band-resolved IPR mean** (tail 10% vs. mid 80% vs. tail 10%)

**Priority:** 🟢 **MEDIUM** — determines if metric redesign is needed

**Requires compute:** ❌ **NO** (post-processing existing eigenvector data IF saved)  
⚠️ **BLOCKER:** Gate 4B v0.1.24 run outputs currently contain `true_ipr_mean` only (aggregate). Eigenvector data NOT saved.

**Required data:** ❌ **NOT AVAILABLE** — would require rerun with eigenvector persistence

---

### Q5. What matched nulls are required?

**Context:**  
Current controls vary operator structure (scramble, disable Wilson), but do NOT control for:
- Hilbert dimension (N × j_max varies across grid)
- Eigenvalue density (spectral statistics sensitive to level spacing)
- Disorder realization (same seed across conditions?)

**Hypotheses:**
- **H5.1:** Dimension-matched random Hermitian (same N as Gate 4B) will show similar contrast → IPR is dimension-driven
- **H5.2:** Eigenvalue-density-matched null (same level spacing distribution as S³×S¹) needed
- **H5.3:** Seed-matched cross-condition comparison needed (isolate disorder realization)

**Diagnostic test (Matched Null Design):**
- **Null 1 (Dimension):** Random Hermitian N=1728 (heaviest Gate 4B case), disorder W ∈ {0, 20}
- **Null 2 (Spectral density):** Random Hermitian with eigenvalues drawn from same distribution as S³×S¹ (no geometry, matched density)
- **Null 3 (Seed):** Gate 4B vs. scrambled_geometry with **same seed** (isolate geometry effect from disorder realization)

**Priority:** 🟡 **HIGH** — defines specificity baseline

**Requires compute:** ✅ **YES** (new controls)

**Required data:** None (new experiment)

---

### Q6. Can we design energy-resolved metrics without rerun?

**Context:**  
Eigenvector data not saved in current run outputs → energy-resolved IPR requires rerun OR alternative metric from eigenvalues only.

**Hypotheses:**
- **H6.1:** Participation entropy `S = −Σ pᵢ log pᵢ` (eigenvalue-only) captures localization structure
- **H6.2:** Spectral gap ratio (energy-resolved r-statistic) separates intact from controls
- **H6.3:** No eigenvalue-only metric sufficient → eigenvector persistence REQUIRED

**Diagnostic test (Metric Redesign Plan):**
- Define 3 candidate metrics:
  1. Participation entropy (eigenvalue weights only)
  2. Energy-resolved gap ratio `r(E)` (partition spectrum into bins)
  3. **S³ degeneracy compliance** (does eigenvalue spacing match S³ Dirac degeneracy pattern?)
- Test on synthetic data (S³×S¹ analytic spectrum + disorder) → which metric distinguishes geometry?

**Priority:** 🟢 **MEDIUM** — may avoid eigenvector rerun

**Requires compute:** ❌ **NO** (synthetic test, design only)

**Required data:** S³×S¹ analytic spectrum (available from `cc_toy_lab/geometry/analytic_spectra.py`)

---

### Q7. What artifact taxonomy do we need?

**Context:**  
broken_wilson_term PASSED with 8.20× (stronger than signal). Need systematic classification: is this a **signal-like artifact** or a **distinct artifact class**?

**Hypotheses:**
- **H7.1:** Two artifact classes: (1) dimension-driven (affects all operators equally), (2) discretization-driven (Wilson-specific)
- **H7.2:** Three artifact classes: (1) dimension, (2) discretization, (3) **operator bugs** (shared by Gate 4B and controls)
- **H7.3:** Artifact zoo: multiple independent sources, need **orthogonal controls** to isolate each

**Diagnostic test (Artifact Zoo Taxonomy):**
- Build decision tree:
  - Does random_hermitian (N-matched) PASS? → dimension artifact
  - Does scrambled_geometry PASS? → Kronecker structure artifact OR degeneracy preservation
  - Does broken_wilson_term PASS? → Wilson irrelevance OR operator bug
  - Does anti_wilson (inverted sign) PASS? → Wilson anti-correlation
- Map 4 controls → 2^4 = 16 possible outcome patterns → classify each

**Priority:** 🟢 **MEDIUM** — needed for redesigned control suite

**Requires compute:** ❌ **NO** (taxonomy design only)

**Required data:** None (conceptual framework)

---

## 4. Work Packages

| WP | Goal | Requires Compute? | Required Data | Priority | Output |
|----|------|-------------------|---------------|----------|--------|
| **WP1** | Raw Data Availability Audit | ❌ NO | v0.1.24 outputs | 🟢 DONE | `DIAGNOSTIC_DATA_INVENTORY.md` |
| **WP2** | broken_wilson_term Code Audit | ❌ NO | Source code | 🔴 CRITICAL | `WILSON_CONSTRUCTION_AUDIT.md` |
| **WP3** | Wilson Relevance Ablation Plan | ✅ YES (216 cases) | None (new) | 🟡 HIGH | Pre-registration doc |
| **WP4** | FSS Slope Reanalysis | ❌ NO | v0.1.22 controls | 🟡 HIGH | `FSS_SLOPE_COMPARISON.md` |
| **WP5** | Metric Redesign Plan | ❌ NO | Analytic spectra | 🟢 MEDIUM | `ENERGY_RESOLVED_METRICS_DESIGN.md` |
| **WP6** | Matched Null Design | ❌ NO (design) | None | 🟡 HIGH | Pre-registration doc |
| **WP7** | Artifact Zoo Taxonomy | ❌ NO | None | 🟢 MEDIUM | `ARTIFACT_DECISION_TREE.md` |
| **WP8** | Allowed/Forbidden Claims Update | ❌ NO | All WP outputs | 🔴 CRITICAL | `docs/CLAIMS_AND_CAVEATS.md` |

---

### WP1: Raw Data Availability Audit ✅ DONE

**Goal:** Determine what data is available from existing runs to support energy-resolved / per-state analysis.

**Status:** ✅ **COMPLETE** (verified 2026-06-01)

**Findings:**
- v0.1.24 Gate 4B outputs: `true_ipr_mean` (aggregate), `r_stat` (aggregate), eigenvalues NOT saved, eigenvectors NOT saved
- v0.1.22 Negative Controls outputs: same structure (aggregate only)

**Implication:** Energy-resolved IPR (Q4) **requires rerun** with eigenvector persistence OR alternative eigenvalue-only metric (Q6)

**Output:** Listed in this document (§3 Q4 blocker note)

---

### WP2: broken_wilson_term Code Audit 🔴 CRITICAL

**Goal:** Verify that `wilson_mode: disabled` is implemented per pre-registration and determine why disabling Wilson **enhances** signal instead of destroying it.

**Tasks:**
1. Read `cc_toy_lab/controls/negative_controls.py` or `cc_toy_lab/spectral/s3_s1_product_discretized.py`
2. Trace Wilson term construction for:
   - `s1_family: wilson_ring` (Gate 4B default)
   - `wilson_mode: disabled` (Control C)
3. Compare operator matrix construction (algebraic form)
4. Export one matched case (same N, seed, W) → compute operator difference norm

**Evidence required:**
- Code path annotation (function calls, line numbers)
- Operator difference quantification (Frobenius norm)
- Eigenvalue scatter plot (Gate 4B vs. broken_wilson_term)

**Blocker resolution:** If operators are identical → Control C is invalid, redesign required

**Priority:** 🔴 **CRITICAL** — blocks all other work packages

**Requires compute:** ❌ NO (code audit primary), ✅ YES (single-case operator export for verification)

**Output:** `reports/WILSON_CONSTRUCTION_AUDIT.md`

---

### WP3: Wilson Relevance Ablation Plan 🟡 HIGH

**Goal:** Definitively test whether Wilson term is load-bearing by running Gate 4B grid with Wilson explicitly disabled.

**Design:**
- Same grid as v0.1.24 (216 cases: 24 W=0, 192 W ∈ {5,10,15,20})
- Override: `s1_family: spectral_circle` (pure Fourier, no Wilson correction)
- All other parameters identical (j_max, s1_size, seeds, disorder)

**Decision rule:**
- If contrast ≈ 7.07× (unchanged) → Wilson cosmetic
- If contrast > 7.07× (enhanced) → Wilson anti-correlates with localization
- If contrast < 3.5× (halved) → Wilson load-bearing

**Blocker:** WP2 must complete first (verify broken_wilson_term implementation before designing ablation)

**Priority:** 🟡 **HIGH** (but BLOCKED on WP2)

**Requires compute:** ✅ **YES** (216-case rerun, ~2 hours on 32 GiB host)

**Output:** Pre-registration document `reports/WILSON_ABLATION_PREREGISTRATION_v0.1.25.md`

---

### WP4: FSS Slope Reanalysis 🟡 HIGH

**Goal:** Determine if FSS slope (localization vs. system size) distinguishes Gate 4B from controls better than aggregate contrast.

**Method:**
1. Load all v0.1.22 data (Gate 4B + 3 controls, 54 cases each)
2. Group by (s1_size, disorder_strength) → 3 system sizes × 2 disorder levels = 6 FSS points
3. Fit: `log(IPR) ~ a + b·log(N)` for each condition
4. Extract slope `b` and R² for each
5. Plot: 2D scatter (contrast vs. slope), 4 conditions

**Metric proposal:**
```
Specificity Score = α·Contrast + β·FSS_Slope − max(Controls)
```

**Threshold:**
- If `Specificity(Gate 4B) > 0` → harness specific
- If `Specificity(Gate 4B) ≤ 0` → harness nonspecific

**Priority:** 🟡 **HIGH** — may salvage interpretation without rerun

**Requires compute:** ❌ **NO** (reanalysis of existing data)

**Output:** `reports/FSS_SLOPE_COMPARISON_v0.1.22.md`

---

### WP5: Metric Redesign Plan 🟢 MEDIUM

**Goal:** Design energy-resolved or eigenvalue-only metrics that can detect S³×S¹ geometry-specific localization.

**Candidates:**

1. **Participation Entropy** (eigenvalue-only):
   ```
   S = −Σᵢ pᵢ log pᵢ,  pᵢ = |ψᵢ|² / Σⱼ|ψⱼ|²
   ```
   Distinguishes uniform delocalization (S → log N) from localized (S → 0)

2. **Energy-Resolved Gap Ratio**:
   Partition spectrum into 10 bins by eigenvalue, compute `r_stat` per bin → profile

3. **S³ Degeneracy Compliance**:
   S³ Dirac eigenvalues have known degeneracies `d(k) = 2(k+1)(k+2)`.  
   Measure: does eigenvalue spacing histogram match S³ pattern?

**Test protocol:**
- Generate synthetic S³×S¹ spectrum (analytic + small disorder)
- Generate dimension-matched random Hermitian
- Apply all 3 metrics → which separates the two?

**Priority:** 🟢 **MEDIUM** — fallback if eigenvector rerun is infeasible

**Requires compute:** ❌ **NO** (synthetic test only)

**Output:** `reports/ENERGY_RESOLVED_METRICS_DESIGN.md`

---

### WP6: Matched Null Design 🟡 HIGH

**Goal:** Design controls that isolate specific artifact sources (dimension, spectral density, disorder realization).

**Proposed nulls:**

| Null | Construction | What it tests |
|------|--------------|---------------|
| **N1: Dimension** | Random Hermitian, N=1728 (Gate 4B max), W ∈ {0,20} | IPR dimension-dependence |
| **N2: Spectral Density** | Random Hermitian with eigenvalues sampled from S³×S¹ distribution | Level spacing artifact |
| **N3: Seed-Matched** | scrambled_geometry with same seeds as Gate 4B | Isolate geometry from disorder |
| **N4: Anti-Wilson** | S³×S¹ with Wilson coefficient sign inverted | Wilson anti-correlation test |

**Grid per null:** 9 cases (3 seeds × 3 sizes), W ∈ {0,20} → 18 cases/null, 72 cases total

**Decision rule:**
- If N1 PASSES → IPR is dimension-driven, harness invalid
- If N2 PASSES → spectral density artifact
- If N3 contrast differs from scrambled_geometry → seed effect
- If N4 PASSES → Wilson anti-correlates with localization

**Priority:** 🟡 **HIGH** (defines next control batch)

**Requires compute:** ❌ **NO** (design only), ✅ **YES** when executed (72 cases)

**Output:** Pre-registration document `reports/MATCHED_NULLS_PREREGISTRATION_v0.1.26.md`

---

### WP7: Artifact Zoo Taxonomy 🟢 MEDIUM

**Goal:** Build a decision tree mapping control outcomes to artifact classifications.

**Structure:**
```
Decision Node 1: Does dimension-matched random Hermitian (N1) PASS?
├─ YES → IPR is dimension-driven (ARTIFACT CLASS: DIMENSION)
└─ NO → Proceed to Node 2

Decision Node 2: Does scrambled_geometry PASS?
├─ YES → Geometry scrambling insufficient OR degeneracy preserved (ARTIFACT CLASS: STRUCTURAL)
└─ NO → Proceed to Node 3

Decision Node 3: Does broken_wilson_term PASS?
├─ YES → Wilson irrelevant OR operator bug (ARTIFACT CLASS: DISCRETIZATION)
└─ NO → Proceed to Node 4

Decision Node 4: Does anti_wilson PASS?
├─ YES → Wilson anti-correlates with localization (PARADOX)
└─ NO → Wilson load-bearing, Gate 4B interpretation salvageable
```

**Output format:** Markdown decision tree + artifact taxonomy table

**Priority:** 🟢 **MEDIUM** — framework for interpreting future controls

**Requires compute:** ❌ **NO**

**Output:** `reports/ARTIFACT_DECISION_TREE.md`

---

### WP8: Allowed/Forbidden Claims Update 🔴 CRITICAL

**Goal:** Update `docs/CLAIMS_AND_CAVEATS.md` to reflect diagnostic sprint findings.

**New forbidden claims:**
- ❌ "S³×S¹ signal validated" → PAUSED (controls PASSED)
- ❌ "Harness distinguishes geometric signals from artifacts" → PAUSED (nonspecificity finding)
- ❌ "Wilson term is load-bearing" → UNKNOWN (until WP2/WP3 complete)
- ❌ "Signal is NOT geometry-specific" → PREMATURE NEGATIVE (diagnostic sprint incomplete)

**New allowed claims:**
- ✅ "Gate 4B signal preserved across operator correction (7.07× vs 7.15×, −1.1%)"
- ✅ "Negative Controls v0.1.22 revealed 2/3 controls PASSED (4.25×, 8.20×)"
- ✅ "Diagnostic investigation underway (7 work packages)"
- ✅ "Analysis reproduced (54/54 cases verified) but control construction under manual review"

**Timing:** Update AFTER WP2 (code audit) completes, BEFORE any external communication

**Priority:** 🔴 **CRITICAL** — blocks Tom Lawrence email, CAMP update, Zenodo upload

**Requires compute:** ❌ **NO**

**Output:** Updated `docs/CLAIMS_AND_CAVEATS.md`

---

## 5. New Success Criterion (PROPOSAL)

### Current Success Criterion (v0.1.21–v0.1.24)

```
Gate 4B PASS if:
  Aggregate contrast (W=20 / W=0) > 2.0×
  AND positive FSS slope
  AND 3/3 S¹ families consistent
```

**Problem:** Does not account for control performance. broken_wilson_term shows 8.20× (exceeds threshold but should FAIL).

---

### Proposed: Specificity Score

**Definition:**
```
Specificity Score = Effect(Gate 4B) − max(Effect(Controls))

where Effect = α·Contrast + β·FSS_Slope + γ·r_stat_shift
```

**Parameters (to be calibrated via WP4):**
- α = 1.0 (contrast weight, normalized to [0,1])
- β = 0.5 (FSS slope weight, TBD from reanalysis)
- γ = 0.3 (r-statistic shift weight, TBD)

**Decision rule:**
```
If Specificity Score > 1.0 → HARNESS_SPECIFIC (Gate 4B distinguishable from controls)
If Specificity Score ∈ [0, 1.0] → WEAK_SPECIFICITY (marginal separation)
If Specificity Score < 0 → HARNESS_NONSPECIFIC (controls exceed Gate 4B)
```

**Example (current data):**
```
Gate 4B:             Effect = 1.0 × 7.07 + 0.5 × FSS_slope(Gate4B)
broken_wilson_term:  Effect = 1.0 × 8.20 + 0.5 × FSS_slope(broken)

Specificity = Effect(Gate4B) − Effect(broken)
            = 7.07 − 8.20 + 0.5·(slope_diff)
            = −1.13 + 0.5·(slope_diff)

If slope_diff < 2.26 → Specificity < 0 → HARNESS_NONSPECIFIC
```

**Status:** 🟡 **PROPOSAL** — NOT pre-registered, requires validation via WP4 before adoption

**Next step:** Compute Specificity Score for all 4 conditions (Gate 4B + 3 controls) using v0.1.22 data → determine if threshold separates intact from broken

---

## 6. Forbidden Actions (Until Diagnostic Sprint Complete)

### ❌ DO NOT proceed to Gate 5

**Gate 5 (W-sweep):** Pre-registered 1000-case campaign testing localization across disorder range W ∈ [0, 50].

**Blocker:** If Gate 4B harness is nonspecific, Gate 5 will measure the same nonspecific artifact at higher resolution → wasted compute.

**Resumption condition:** Specificity Score (§5) > 1.0 OR redesigned controls (WP6) all FAIL.

---

### ❌ DO NOT port to S³×S²

**S³×S² fork:** Pre-registered alternative geometry (Dirac monopole on S²).

**Blocker:** If S³×S¹ signal is a dimension/discretization artifact (not geometry-specific), S³×S² will show the same artifact.

**Resumption condition:** S³×S¹ specificity confirmed OR diagnostic sprint identifies isolatable artifact (can be designed out in S³×S² fork).

---

### ❌ DO NOT make external success claims

**Forbidden:**
- Email to Tom Lawrence: "Signal validated"
- Email to Thomas Buckholtz: "S³×S¹ localization confirmed"
- Zenodo upload: "Gate 4B PASS"
- LinkedIn post: "Compactification signal detected"
- CAMP Discord: "Geometric localization proven"

**Allowed (internal only):**
- "Signal preserved across operator correction (−1.1%)"
- "Diagnostic investigation underway"
- "Controls revealed unexpected patterns requiring analysis"

**Timing:** External communication ALLOWED after:
1. WP2 (code audit) confirms control construction is correct, AND
2. WP4 (FSS reanalysis) shows Specificity Score > 1.0, OR
3. Redesigned controls (WP6) all FAIL as expected

---

### ❌ DO NOT claim Tom Lawrence theory validated

**Forbidden wording:**
- "Tom Lawrence's S³×S¹ compactification validated"
- "Geometric engineering paradigm confirmed"
- "Covariant compactification reproduced"

**Reason:** Even if Gate 4B signal is geometry-specific, finite-lattice toy model does NOT validate continuum field theory. This claim was already forbidden in `docs/CLAIMS_AND_CAVEATS.md` — diagnostic sprint does not change this.

**Allowed:**
- "Inspired by Tom Lawrence's work on S³×S¹ geometry"
- "Tests finite-lattice toy model motivated by geometric engineering"

---

### ❌ DO NOT claim compactification proven

**Forbidden:**
- "Compactification mechanism detected"
- "Extra dimension localization confirmed"
- "Radion stabilization validated"

**Reason:** Gate 4B tests Anderson localization on a discretized product manifold. This is NOT a test of gravitational compactification, Kaluza-Klein tower structure, or radion stability.

**Allowed:**
- "Anderson localization on discretized S³×S¹ product"
- "Finite-mode toy model of compact geometry"

---

### ❌ DO NOT claim physical localization

**Forbidden:**
- "Geometric localization in extra dimensions"
- "Wavefunctions confined to S³ structure"

**Reason:** IPR measures eigenvector concentration in Hilbert space, NOT physical space. Eigenvector index ≠ spatial coordinate.

**Allowed:**
- "Eigenvector localization in Hilbert space"
- "IPR contrast under Anderson disorder"

---

## 7. Verdict

**Diagnostic Sprint Plan Status:** ✅ **READY_FOR_REVIEW**

**Summary:**
- **7 diagnostic questions** defined (Q1–Q7)
- **8 work packages** planned (WP1–WP8), priority-ordered
- **5 no-compute tasks** (WP1, WP2, WP4, WP5, WP7, WP8) — can start immediately
- **3 compute-required tasks** (WP3, WP6, deferred pending design validation)
- **New success criterion** proposed (Specificity Score) — requires WP4 calibration
- **5 forbidden actions** enforced until sprint complete

**Next immediate step:** Execute **WP2 (broken_wilson_term Code Audit)** — CRITICAL blocker for all other work.

**Expected timeline:**
- WP2 (code audit): 2–4 hours
- WP4 (FSS reanalysis): 4–6 hours
- WP5 (metric design): 6–8 hours
- WP7 (artifact taxonomy): 2–3 hours
- WP8 (claims update): 1 hour
- **Total (no-compute phase):** ~20 hours (2–3 days)

**Compute phase (if triggered):**
- WP3 (Wilson ablation): 216 cases, ~2 hours on 32 GiB
- WP6 (matched nulls): 72 cases, ~40 min on 32 GiB
- **Total compute cost:** €5–10 (Hetzner CCX33, 2.5 hours)

**Decision point:** After WP2 + WP4 complete → determine:
- If Specificity Score > 1.0 → resume Gate 4B interpretation (cautiously)
- If Specificity Score ≤ 0 → execute WP6 (redesigned controls)
- If code audit reveals operator bug → full rerun required (Gate 4B + all controls)

---

**Evidence Markers:**
- [VERIFIED-REAL]: Gate 4B v0.1.24 contrast (7.07×), Negative Controls v0.1.22 data (54/54 cases)
- [INFERRED]: Harness nonspecificity (pending WP2 code audit confirmation)
- [UNKNOWN]: Wilson term relevance, energy-resolved structure, artifact taxonomy
- [PROPOSAL]: Specificity Score (not pre-registered, requires validation)

**Forbidden Claims Enforced:**
- ❌ S³×S¹ validated
- ❌ Compactification proven
- ❌ Tom Lawrence theory validated
- ❌ Physical localization proven
- ❌ Signal is NOT geometry-specific (premature negative)

---

**Last updated:** 2026-06-01  
**Status:** 🔬 **DIAGNOSTIC_SPRINT_PLAN_READY_FOR_REVIEW**  
**Blocking next step:** WP2 (broken_wilson_term Code Audit)  
**External communication:** ⛔ **PAUSED** until WP2 + WP4 complete
