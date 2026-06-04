# Negative Controls FAILURE — Diagnostic Report

**Date:** 2026-05-31  
**Status:** ❌ **HARNESS_NONSPECIFIC_PENDING_REPRODUCIBILITY_AUDIT** — 2/3 controls PASSED unexpectedly  
**Impact:** Gate 4B interpretation requires diagnostic investigation before any claims

---

## Executive Summary

**Preliminary Verdict:** ❌ **HARNESS_NONSPECIFIC_PENDING_REPRODUCIBILITY_AUDIT**

⚠️ **AUDIT STATUS:** Analysis reproduced (54/54 cases verified), but control construction requires manual review before final verdict.

Negative Controls v0.1.22 (54 cases) revealed that the validation harness **cannot distinguish** the Gate 4B S³×S¹ signal from broken/scrambled baselines:

- ✅ random_hermitian: 1.30× (FAIL as expected)
- ❌ scrambled_geometry: **4.25×** (UNEXPECTED PASS)
- ❌ broken_wilson_term: **8.20×** (UNEXPECTED PASS — stronger than Gate 4B!)

**Gate 4B baseline:** 7.07× (v0.1.24)

**Preliminary Implication:**  
The 7.07× aggregate contrast observed in Gate 4B requires diagnostic investigation. Preliminary data shows:
- S³×S¹ coupling scrambled (permutation): 4.25× remains
- Wilson term disabled: 8.20× (stronger than baseline)

**AUDIT REQUIRED:** Control construction must be manually verified against pre-registration before concluding signal is non-specific.

---

## Detailed Results

### Control A: random_hermitian — ✅ PASS (as expected)

| Metric | W=0 | W=20 | Contrast |
|--------|-----|------|----------|
| Mean IPR | 0.000797 | 0.001035 | **1.30×** |
| Cases | 9 | 9 | 18 total |

**Status:** ✅ **FAIL** (< 2.0× threshold)

**Construction:**
- Diagonal U(r) ∈ [-W, W] (disorder)
- Gaussian off-diagonal (no geometric structure)
- NO S³ Dirac operator
- NO S¹ discretization

**Assessment:** ✅ **Expected FAIL** — random matrix without geometry **cannot** reproduce Gate 4B signal. This control PASSED (failed to reproduce signal).

---

### Control B: scrambled_geometry — ❌ UNEXPECTED PASS

| Metric | W=0 | W=20 | Contrast |
|--------|-----|------|----------|
| Mean IPR | 0.005183 | 0.022026 | **4.25×** |
| Cases | 9 | 9 | 18 total |

**Status:** ❌ **PASS** (≥ 2.0× threshold) — **UNEXPECTED!**

**Construction:**
- S³×S¹ product operator
- **Permutation scramble** — S³ indices randomized
- Wilson term present but broken coupling

**Assessment:** ❌ **Unexpected PASS** — scrambled geometry **reproduced 60% of Gate 4B signal** (4.25× / 7.07×).

**Why this is a problem:**
- If scrambling S³ indices only reduces signal from 7.07× to 4.25× (not to <2.0×), the signal is **NOT geometry-specific**
- Gate 4B may be picking up **generic disorder effects**, not S³×S¹ structure

---

### Control C: broken_wilson_term — ❌ UNEXPECTED PASS (WORST RESULT)

| Metric | W=0 | W=20 | Contrast |
|--------|-----|------|----------|
| Mean IPR | 0.040043 | 0.328267 | **8.20×** |
| Cases | 9 | 9 | 18 total |

**Status:** ❌ **PASS** (≥ 2.0× threshold) — **UNEXPECTED!**

**Construction:**
- S³×S¹ product operator
- **Wilson term DISABLED** (`wilson_mode: disabled`)
- No Wilson correction in S¹ discretization

**Assessment:** ❌ **Unexpected PASS — STRONGER than Gate 4B!**

**Why this is catastrophic:**
- broken_wilson_term: **8.20×**
- Gate 4B (correct Wilson): **7.07×**
- **Δ: +16% stronger WITHOUT Wilson term!**

**Implication:**
- Wilson term is **NOT load-bearing** for the localization signal
- Disabling Wilson **enhances** the signal instead of destroying it
- Gate 4B interpretation (Wilson-dependent localization) is **WRONG**

---

## Decision Matrix

| Control | Contrast | Expected | Actual | Pass? |
|---------|----------|----------|--------|-------|
| random_hermitian | 1.30× | FAIL (< 2.0×) | FAIL | ✅ |
| scrambled_geometry | **4.25×** | FAIL (< 2.0×) | **PASS** | ❌ |
| broken_wilson_term | **8.20×** | FAIL (< 2.0×) | **PASS** | ❌ |

**Threshold:** < 2.0× contrast (controls must FAIL to reproduce signal)

**Verdict:** ❌ **2/3 controls PASSED** → harness **LACKS SPECIFICITY**

---

## Root Cause Analysis

### Why did scrambled_geometry PASS?

**Hypothesis 1: Partial scrambling**
- Permutation scramble may preserve **some** S³ structure (degeneracy groups)
- If scrambling is too weak, geometry is only partially broken

**Hypothesis 2: Disorder dominates geometry**
- Signal may come from **Anderson disorder itself**, not S³×S¹ coupling
- Geometry provides **minor modulation** (60% reduction when scrambled)

**Hypothesis 3: IPR metric artifact**
- IPR may be sensitive to Hilbert dimension, not geometry
- Same N, same disorder → similar IPR regardless of operator structure

---

### Why did broken_wilson_term PASS (and EXCEED Gate 4B)?

**Hypothesis 1: Wilson term SUPPRESSES localization**
- Removing Wilson may **increase** localization (counter-intuitive)
- Wilson correction designed to reduce lattice artifacts may also reduce signal

**Hypothesis 2: Wilson term irrelevant**
- Localization driven by S³ Dirac operator + disorder, not S¹ Wilson term
- S¹ discretization family (spectral_circle/ring/wilson_ring) may be cosmetic

**Hypothesis 3: Operator construction bug**
- Wilson term may be incorrectly implemented in BOTH Gate 4B and controls
- "Disabling" Wilson may fix an unknown bug → stronger signal

---

## Implications

### ⚠️ Gate 4B v0.1.24 interpretation PENDING AUDIT

**Initial expectation:**
> S³×S¹ finite-lattice geometry supports robust localization signal (7.07×) under Anderson disorder, distinguishable from artifacts.

**Negative Controls preliminary data:**
> - random_hermitian: 1.30× (expected FAIL ✅)
> - scrambled_geometry: 4.25× (unexpected PASS ❌)
> - broken_wilson_term: 8.20× (unexpected PASS ❌)
>
> → **REQUIRES DIAGNOSTIC INVESTIGATION** before concluding signal is non-specific.

---

### ⚠️ Claims PAUSED pending diagnostic investigation

**Forbidden claims (until audit complete):**
- ❌ "S³×S¹ signal validated" (controls show unexpected PASS)
- ❌ "Harness distinguishes geometric signals from artifacts" (controls PASSED)
- ❌ "Signal is NOT geometry-specific" (premature negative claim without diagnostic investigation)

**Allowed claims (pending audit):**
- ✅ "Gate 4B v0.1.24 detected 7.07× contrast (signal preserved from v0.1.21)"
- ✅ "Negative Controls preliminary data shows 2/3 controls PASSED unexpectedly"
- ✅ "Diagnostic investigation required before final verdict"
- ✅ "Analysis reproduced (54/54 cases verified) but control construction under manual review"

---

### ⚠️ v0.1.21 and v0.1.24 interpretation PAUSED

**Both versions under review:**
- v0.1.21: 7.15× (frozen, operator bug)
- v0.1.24: 7.07× (corrected operator, signal preserved)

**Note:**
- Negative Controls run on **v0.1.22** operator (NOT v0.1.24)
- Operator structure similar (S³ Dirac + S¹ discretization) but not identical
- v0.1.24 controls re-run may be needed after diagnostic investigation

**Action pending:**
- Manual review of control construction (scramble_mode, wilson_mode implementations)
- Verify controls match pre-registration specifications
- THEN re-run on v0.1.24 if construction confirmed correct

---

## Next Steps

### Immediate (today)

#### 1. ❌ PAUSE all external communication
- **DO NOT** email Tom Lawrence about "signal preserved"
- **DO NOT** email Thomas Buckholtz (Stanford intro)
- **DO NOT** update Zenodo DOI with "PASS" verdict

**Why:**  
Negative Controls failure changes the entire narrative from **positive result** to **negative result + methodological lessons**.

---

#### 2. ✅ Deep diagnostic investigation

**Questions to answer:**

**A. Is scrambled_geometry scrambled enough?**
```python
# Check scrambling implementation
# reports/RUNS/negative_controls_v0.1.22/batch_03/case_018.json
# "scramble_mode": "permutation"

# Verify:
# - Are S³ eigenvalues permuted or S³ operator structure?
# - Does permutation preserve degeneracy groups?
# - Is Kronecker product still separable after scramble?
```

**B. Why does broken_wilson_term EXCEED Gate 4B?**
```python
# Compare operator construction:
# Gate 4B: wilson_ring family (Wilson term enabled)
# Control C: wilson_mode: disabled

# Hypothesis test:
# - Run Gate 4B with Wilson term explicitly disabled → compare to Control C
# - If they match → Wilson term was never load-bearing
# - If they differ → Control C construction is different from Gate 4B
```

**C. Is IPR metric sensitive to geometry or just dimension?**
```python
# Test:
# - Compute IPR on random Hermitian matrix of SAME dimension as S³×S¹
# - If IPR ≈ Gate 4B → IPR is dimension-driven, not geometry-driven
# - If IPR << Gate 4B → geometry matters, but scrambling is too weak
```

---

#### 3. ✅ Re-run Negative Controls on v0.1.24 operator

**Why:**
- Current controls ran on v0.1.22 (different operator version)
- Need to confirm PASS on v0.1.24 corrected operator

**ETA:** 1 hour (36 cases, same server specs)

---

#### 4. ✅ Write honest failure report

**Document:**
- `reports/NEGATIVE_CONTROLS_FAILURE_DIAGNOSTIC_v0.1.22.md`
- Full analysis of why 2/3 controls PASSED
- Hypotheses for scrambled_geometry and broken_wilson_term
- Recommended diagnostic experiments

**Audience:** Internal only (not external until diagnostics complete)

---

### Soon (this week)

#### 5. ✅ Redesign Negative Controls (stronger versions)

**Control B v2: Fully decoupled S³×S¹**
- Instead of permutation scramble → **random Hermitian S³ block**
- Break Kronecker structure entirely
- Preserve dimension but destroy product geometry

**Control C v2: Anti-Wilson (inverted sign)**
- Instead of disabling Wilson → **invert Wilson coefficient**
- Should destroy localization if Wilson is load-bearing
- If still PASS → Wilson irrelevant

**Control D (NEW): Dimension-matched random Hermitian**
- Random matrix with **same N as Gate 4B heaviest case** (N=1728)
- NO S³ structure, NO S¹ structure, ONLY disorder
- If PASS → IPR is dimension-driven, not geometry-driven

---

#### 6. ✅ Skeptic agent review

**Invoke:**
```
Agent(skeptic, prompt="Red-team Negative Controls failure. 
Why did scrambled_geometry and broken_wilson_term PASS? 
What alternative explanations exist? 
What diagnostic experiments would falsify each hypothesis?")
```

**Output:** Independent analysis from adversarial perspective

---

### Later (next 2 weeks)

#### 7. ✅ Methodology paper pivot

**Old framing (INVALID):**
> "Falsification-first harness validated S³×S¹ localization signal"

**New framing (HONEST):**
> "Falsification-first harness DETECTED apparent signal but Negative Controls revealed lack of specificity — a methodological lesson"

**Paper sections:**
1. Introduction: motivation for Negative Controls
2. Gate 4B initial PASS (7.07×)
3. **Negative Controls FAILURE** (2/3 controls PASSED)
4. Diagnostic investigation (why controls passed)
5. **Lessons learned:** importance of adversarial controls
6. Conclusion: harness methodology improved, S³×S¹ claim retracted

**Target venue:** Same (*Computer Physics Communications*) — honest negative results are publishable

---

## Financial Impact

### Sunk costs (already spent)
- ✅ Hetzner CX52: €29.95 (1 month)
- ✅ 6 months development time
- ✅ 74 git commits, 30K lines code

**These costs remain regardless of outcome.**

---

### Future costs (affected by failure)
- ❌ Gate 5 W-sweep: **PAUSED** (until Negative Controls redesigned)
- ❌ S³×S² fork: **CANCELLED** (no point testing other geometries if harness non-specific)
- ❌ Methodology paper timeline: **+3 months** (diagnostic investigation)

---

### Career impact (mitigated by honesty)
- ❌ **Lost:** "Validated S³×S¹ signal" positive result
- ✅ **Gained:** "Honest negative result + rigorous methodology" reputation
- ✅ **Still publishable:** Negative Controls failure is a methodological contribution

**Net:** Neutral to slightly negative (publication delayed but still viable)

---

## Tom Lawrence Communication Strategy

### ❌ DO NOT send "signal preserved" email

**Why:**
- Negative Controls failure invalidates "signal preserved" interpretation
- Premature positive communication → reputation damage when retracted

---

### ✅ Honest update (after diagnostics)

**Email subject:** GeoSpectra Negative Controls Update — Diagnostic Investigation

**Draft:**
```
Hi Tom,

Quick update on GeoSpectra:

Gate 4B v0.1.24 corrected rerun showed signal preserved (7.07× vs 7.15×), 
which initially looked promising. However, Negative Controls revealed a 
critical issue:

Two of three controls PASSED unexpectedly:
- scrambled_geometry: 4.25× (should be <2.0×)
- broken_wilson_term: 8.20× (should be <2.0×, actually STRONGER than Gate 4B!)

This suggests the harness cannot distinguish the S³×S¹ signal from broken 
baselines. The 7.07× may be a generic disorder effect, not geometry-specific.

I'm running diagnostic investigations to determine:
1. Is scrambling too weak (partial S³ structure preserved)?
2. Why does disabling Wilson term ENHANCE the signal?
3. Is IPR metric dimension-driven rather than geometry-driven?

Once diagnostics complete (1–2 weeks), I'll know whether:
- Controls need redesign (stronger scrambling/breaking), OR
- Signal is genuinely non-specific (harness methodology lesson)

Either way: honest negative result, still publishable, but delays S³×S² fork.

I'll update you when diagnostics complete.

Best,
Sergey
```

**Timing:** After diagnostic experiments complete (1–2 weeks)

---

## Zenodo DOI Strategy

### ❌ DO NOT update with "PASS" verdict

**Why:**
- Current DOI shows v0.1.16
- v0.1.24 results are NOT validated by Negative Controls
- Uploading "PASS" data then retracting → reputation damage

---

### ✅ Honest data upload (after diagnostics)

**Option 1: Upload v0.1.24 + Negative Controls with CAVEAT**
- Title: "Gate 4B v0.1.24 + Negative Controls v0.1.22 (NON-SPECIFIC)"
- Description: "7.07× signal detected but Negative Controls revealed lack of specificity"

**Option 2: Wait until diagnostics complete**
- Upload AFTER redesigned controls + diagnostic experiments
- Either "redesigned controls PASS → validated" OR "still non-specific → honest negative"

**Recommendation:** Option 2 (wait)

---

## Lessons Learned

### ✅ Falsification-first methodology WORKED

**Why:**
- Negative Controls caught non-specificity BEFORE external publication
- Would have been catastrophic to claim "S³×S¹ validated" then discover controls PASS
- Honest harness design saved reputation

---

### ⚠️ Control design was too weak

**Mistakes:**
- scrambled_geometry: permutation scramble may preserve partial structure
- broken_wilson_term: disabling Wilson ≠ destroying localization mechanism

**Fix:**
- Stronger scrambling: random Hermitian S³ block (fully decoupled)
- Anti-Wilson: invert sign instead of disable
- Dimension-matched random baseline

---

### ⚠️ Pre-registered decision rules may need revision

**Current rule:**
> Contrast < 2.0× = control FAIL (harness specific)

**Problem:**
- broken_wilson_term: 8.20× (4× above threshold, STRONGER than signal!)
- This is not a "close call" — it's a catastrophic PASS

**Revised rule (proposed):**
> Control contrast must be < 0.5× of Gate 4B baseline (not absolute 2.0×)
> 
> Gate 4B: 7.07×
> Threshold: < 3.5× (50% of baseline)
>
> - scrambled_geometry: 4.25× > 3.5× → FAIL
> - broken_wilson_term: 8.20× > 3.5× → FAIL

**Status:** Proposed, not yet adopted (requires pre-registration update)

---

## Summary

**Status:** ❌ **HARNESS_NONSPECIFIC** (2/3 controls PASSED)

**Impact:**
- Gate 4B v0.1.24 signal (7.07×) **PENDING DIAGNOSTIC INVESTIGATION**
- v0.1.21 signal (7.15×) **PENDING DIAGNOSTIC INVESTIGATION**
- External communication **PAUSED**
- Gate 5 / S³×S² **PAUSED**

**Next steps:**
1. Diagnostic investigation (1–2 weeks)
2. Redesign Negative Controls (stronger versions)
3. Re-run on v0.1.24 operator
4. Methodology paper pivot (honest negative result)

**Timeline to publication:**
- **Old estimate:** 12 months (positive result)
- **New estimate:** 18–24 months (negative result + diagnostics + redesign)

**Financial:**
- Sunk: €29.95 (Hetzner)
- Future: **REDUCED** (Gate 5 / S³×S² cancelled until harness validated)

**Career:**
- **Still publishable** (honest negative result)
- **Reputation gain:** rigorous falsification-first approach
- **Reputation loss:** 6 months on non-specific signal (mitigated by honesty)

---

**Last updated:** 2026-05-31  
**Status:** CRITICAL — diagnostic investigation required  
**Next review:** After diagnostic experiments complete (1–2 weeks)
