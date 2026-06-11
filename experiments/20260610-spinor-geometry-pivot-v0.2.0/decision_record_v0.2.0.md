# Decision Record — Spinor-Geometry Pivot v0.2.0

**Date:** 2026-06-10  
**Method:** HD-MAVP full audit (math_code + contradiction + decision_record)  
**Input claim:** Dirac/spinor harness distinguishes S², S³, S⁶ via spectral fingerprints  
**Known correction applied:** IPR not primary; R/4 channel closed (H→H+cI, 1e-18)

---

## Verified Atoms

| Atom | Claim | Evidence | Status |
|---|---|---|---|
| C1 | Scalar harness GEOMETRY_AGNOSTIC | v0.1.22 | VERIFIED |
| C2 | Dirac λ=±(n+d/2) | Camporesi-Higuchi PDF | VERIFIED |
| C3 | |λ_min|=d/2 distinct per sphere | analytic + tool | VERIFIED-tool |
| C4 | Degeneracy patterns distinct | [1,4,9,16,25] vs [2,6,12,20,30] | VERIFIED-tool |
| C5 | Same-n degeneracy survives discretization | Block A, Block E | VERIFIED-tool |
| C6 | IPR blind to R/4 | diff=1e-18 at N=200 | VERIFIED-tool |
| C7 | Same-n modes orthogonal under S³ weight | Block B cross-terms <0.001 | VERIFIED-tool |

## Contradictions Found and Resolved

| Contradiction | Atoms | Resolution |
|---|---|---|
| C1 | C8 × C9 | Radial-only basis incomplete; spectral path unaffected — eigenvalues don't need cross-n orthogonality |
| C2 | C9 × C11 | C11 measures same-n orthogonality only; this is expected and correct for spectral fingerprint |

**No blocking contradictions on the spectral fingerprint path.**

## Hidden Assumptions

| Assumption | Status | Action |
|---|---|---|
| HA-1: harness computes full spinor harmonics | VIOLATED | Scope to radial-only; block IPR as primary |
| HA-2: Hopf coords = standard S³ spectrum | UNVERIFIED | Required before cross-sphere comparison |
| HA-3: fingerprint survives W>0 | **VERIFIED-tool 2026-06-10** | KT-3 PASS: max shift 7.5e-4 at W=0.1, margin 335×, W*>0.5 |
| **HA-4: S^d discrimination solves S³×S¹ GEOMETRY_AGNOSTIC** | **DECIDED 2026-06-10** | ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE — see ha4_design_decision.md |

## Side Finding: tom_ansatz ≈ phi_{11}

**[VERIFIED-tool 2026-06-10]**

tom_ansatz = √sin(2α) has dominant projection 0.920 onto phi_{11} (n=1, l=1, λ=±2.5)
under weighted L² inner product on S³.

Pattern: phi_{ll} series (l=1: 0.92, l=2: 0.88, l=3: 0.83, l=4: 0.79)
Geometric interpretation: √(volume_measure)^{1/2} aligns with l=n boundary modes.

**This is a candidate direct answer to Tom's alpha-problem:**
Tom's ansatz IS approximately the (n=1,l=1) Dirac radial eigenmode with λ=±2.5.

Status: verified under radial weighted inner product; requires full angular confirmation
before communicating to Tom.

**Update 2026-06-10 (AV-1):** upgraded to [RADIAL + DICTIONARY_ROBUST] — argmax (1,1)
survives 49-mode dictionary incl. off-diagonal modes, two measures, two grids
(cos = 0.9594; legacy 0.9204 = cos²). AV-1c bilinear probe FAILED its pre-registered
10% threshold (12.38%, diagonal squares only) — constraint recorded. H-T1 (n=l boundary
family, 92.4%) stays EXPLORATORY, not promoted. Full angular check = AV-2, still pending.
See av1_angular_dictionary_report.md.

**Update 2026-06-10 (AV-1c′):** sparse H-T1 KILLED — D2 (boundary bilinears + const)
residual 13.0% > 10% pre-registered threshold; recorded in
null_results/20260610-ht1-sparse-bilinear.md. Both mechanism predictions CONFIRMED:
P1 (boundary cos-exponent obstruction, residual peaks at α/π = 0.500 exactly) and
P2 (Tom's f^(φ) constant term is load-bearing: 37.9% → 13.0%). Refined picture:
eq. 49 radial layer = constant + DENSE bilinear series (full-LS over extended
dictionary ≈ 5e-4, span contains target; no sparse truncation works).
Linear-level AV-1a finding untouched. See av1c_prime_report.md.

## Kill Tests

| Test | Status | Kill Condition |
|---|---|---|
| KT-1: discrete eigenvalue recovery | **PASS** (E0, 2026-06-10) | max rel. error 6.7e-7, margin ~75 000× |
| KT-2: S²/S³ gap = 0.5 numerically | **PASS** (proxy, 2026-06-10) | gap error 1.6e-6; separation exact |
| KT-3: disorder smears fingerprint | **PASS** (2026-06-10) | max shift 7.5e-4 at W=0.1; W*>0.5 |
| KT-4: scalar vs Dirac on same sphere | **PASS** (NC-3, proxy) | cross-match 0.0 — zero confusion |
| KT-5: tom_ansatz ↔ phi_{11} | **VERIFIED** | 0.920391 (regression-tested) |

## Revised Controls Tier 1

OLD: max projection < 0.1 → ansatz is NOT an eigenfunction (FAILS — actual 0.92)  
NEW: compute dominant-mode decomposition; record phi_{11} as dominant (0.92); this
     is a finding about Tom's framework, not a test failure.

## Experiment Order

```
E0  discrete Dirac matrix + eigenvalue recovery     [~50 lines, can run now]
    Gate: KT-1 pass → proceed to E2
E1  tom_ansatz decomposition regression test        [already verified, write as test]
E2  Tier 2 controls (C9a, C9b, C9c)                [depends on E0 pass]
    ↓ PARALLEL after E2 pass:
E3  KT-2 cross-sphere S²/S³ gap                    [requires S² implementation]
E4  KT-3 disorder W=0.1 fingerprint survival        [PASS 2026-06-10]
E5  Tier 3 negative controls (NC-1, NC-2, NC-3)    [NC-1,NC-3 PASS; NC-2 pending]
    ↓ DESIGN GATE (completed 2026-06-10):
E6  HA-4: ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE       [DECIDED — see ha4_design_decision.md]
    ↓ BRIDGE GATE (Phase 3 entry condition):
BG  NC-2 (permuted grid) → S³×S¹ Dirac harness design (BG-1/BG-2/BG-3)
```

## Decision

```
VERDICT: CONDITIONAL_GO (updated 2026-06-10 after KT-3 + HA-4)

GREEN (complete):  E0 PASS, KT-1 PASS, KT-2 PASS, KT-3 PASS, KT-4 PASS (NC-3),
                   KT-5 VERIFIED, C9a/C9b/C9c PASS, NC-1/NC-3 PASS
OPEN (next):       NC-2 (permuted grid) — last Tier-3 control
DECIDED:           HA-4 = ONE_TRACK_WITH_EXPLICIT_BRIDGE_GATE (2026-06-10)
PHASE 3 ENTRY:     NC-2 PASS → BG-GATE design (S³×S¹ Dirac harness)

NO-GO conditions (all cleared):
  KT-1 fail:         cleared (6.7e-7)
  KT-2 gap error >50%: cleared (1.6e-6)
  KT-3 wipes fingerprint: cleared (335× margin)

EXPLICIT SCOPE STATEMENT (unchanged):
  This pivot tests geometry discrimination on PURE spheres S², S³, S⁶.
  This is a DIFFERENT question from the original S³×S¹ GEOMETRY_AGNOSTIC verdict.
  Success here justifies (but does not substitute for) the S³×S¹ bridge gate.
  Connection path: ONE_TRACK via BG-1/BG-2/BG-3 gaps (see ha4_design_decision.md).
```

---

## Legacy Claim Map — 34 + 8 points (2026-06-10 audit)

Evidence levels:
- `[VT]` VERIFIED-tool — инструментально подтверждён, D:-репо
- `[VR]` VERIFIED-read — подтверждён чтением файла/коммита, D:-репо
- `[EP]` E:only — известен из предыдущих сессий, не в D:-репо до push
- `[AB]` CONFIRMED-ABSENT — явно отсутствует
- `[WK]` WEAK — один источник, без инструментального подтверждения

### Part 1 — Legacy P1–P14 (items 1–34)

| №  | Узел | Статус | Evidence | Source | Действие |
|----|------|--------|----------|--------|----------|
| 1  | Shift toward fermions/spinors | 🟢 strong | `[VT]` | D: Dirac², 75 tests | keep |
| 2  | 32-component spinor generation | 🟡 scaffold | `[EP]` | E: prior session | push E: |
| 3  | Kronecker/tensor products | 🟡 scaffold | `[EP]` | E: prior session | push E: |
| 4  | Fermions as harmonics on S³/S⁶ | 🟢 partial | `[VT]` | D: reference_spinor_harmonics.py | keep |
| 5  | DS⁴×S⁶ spacetime geometry | 🟡 not dynamics | `[EP]` | E: prior session | push E: |
| 6  | S³ ~ Spin(4) / SU(2)_L×SU(2)_R | 🟡 scaffold | `[EP]` | E: prior session; D: Hopf only | push E: |
| 7  | S⁶, SO(7), Spin(6)≅SU(4) | 🟡 scaffold | `[EP]` | E: prior session | push E: |
| 8  | S³ via Pauli/Clifford | 🟡 partial | `[EP]` | E: prior session; D: Hopf metric | push E: |
| 9  | (x^i σ_i + x^4 I) convention fix | 🟢 fixed | `[EP/WK]` | commit 7139ae1 (docs only) | push E: |
| 10 | Gamma/Clifford expression | 🟡 scaffold | `[EP]` | E: prior session | push E: |
| 11 | Hopf / Lawrence coordinates | 🟢 fixed | `[VR]` | geometry_s3_hopf.py; commit 3da1477 | keep |
| 12 | Dragging shifts in (θ, θ̃) | 🟢 tested | `[EP]` | E: prior session | push E: |
| 13 | Cartan directions (∂_θ ± ∂_θ̃) | 🟢 tested | `[EP]` | E: prior session | push E: |
| 14 | Phase dependence | 🟢 tested | `[EP]` | E: prior session | push E: |
| 15 | cot(2α) obstruction | 🟡 implicit | `[WK]` | D: implicit in V(α); no standalone proof | doc gap |
| 16 | Separable ansatz A(α)e^{i[...]} | 🟡 incomplete | `[VR]` | D: test_alpha_ansatz.py | keep |
| 17 | O(4), parity, global coord. issues | 🟡 partial | `[EP]` | E: prior session | push E: |
| 18 | Large-ρ / rotations→translations | 🔴 open | `[AB]` | absent in D: and git history | future work |
| 19 | S⁶ harmonic analysis | 🟡 partial | `[VT]` | D: d=6 eigenvalues; no SU(4) coupling | keep/extend |
| 20 | SU(3) through SU(4)/SO(6) | 🟡 norm-dep | `[EP]` | E: prior session | push E: |
| 21 | Higgs / Forgacs-Manton | 🔴 absent | `[AB]` | absent; README scope excludes SM gauge | keep fence |
| 22 | Limitations / no-promotion fence | 🟢 explicit | `[VR]` | D: scope statements all v0.2.0 files | keep |
| 23 | S³×S⁶ tensor scaffold | 🟡 partial | `[EP]` | E: prior session | push E: |
| 24 | V matrix scaffold | 🟡 scaffold | `[EP]` | E: prior session | push E: |
| 25 | External Wigner/CG oracle | 🟢 passed | `[EP]` | E: prior session | push E: |
| 26 | Robustness audit | 🟢 v0.2.0 scope | `[VT]` | D: KT-3+NC-2 (new audit, not legacy) | keep |
| 27 | Known limitations record | 🟢 explicit | `[VR]` | D: caveats.md, estimand §NOT-mean | keep |
| 28 | V-operator ansatz registry | 🟢 registered | `[EP]` | E: prior session | push E: |
| 29 | Ben Achour one-form identities | 🟢 fixed | `[VR]` | D: commits 7139ae1 + 3da1477 | keep |
| 30 | Spinor-state repair | 🟢 passed | `[EP]` | E: prior session | push E: |
| 31 | Toy-gradient reduced element | 🟡 superseded | `[EP]` | E: prior session | push E: |
| 32 | Ben Achour E/E' mode formula | 🟡 scale-dep | `[EP/WK]` | E: prior session; not in D: | push E: |
| 33 | P13H S³ normalization integral | 🟡 computed | `[EP]` | E: prior session; λ free | push E: + re-audit |
| 34 | P14 lambda-fixing feasibility | 🟡 note only | `[EP]` | E: prior session; no derivation | push E: + re-audit |

**E:-only items:** 2-3, 5-10, 12-14, 17, 20, 23-25, 28-34 (20 пунктов)  
**Verified on D::** 1, 4, 11, 15-16, 18-19, 21-22, 26-27, 29 (14 пунктов)

### Part 2 — v0.2.0 Additions (items 35–42)

| №  | Узел | Статус | Evidence | Source |
|----|------|--------|----------|--------|
| 35 | Dirac spectral fingerprint pivot | 🟢 all gates pass | `[VT]` | D: E0+KT-3+NC controls |
| 36 | R/4 → IPR channel falsified | 🟢 closed | `[VT]` | D: diff=1e-18, regression test |
| 37 | E0 discrete radial Dirac recovery | 🟢 pass | `[VT]` | D: error=6.7e-7, 16 tests |
| 38 | KT-3 weak disorder survival | 🟢 pass | `[VT]` | D: margin 335× (W=0.1), 67× (W=0.5) |
| 39 | NC-2 permuted-grid specificity | 🟢 pass | `[VT]` | D: deviation 270–460%, 14 tests |
| 40 | tom_ansatz radial → φ₁₁ (cos²=0.9204) | 🟢 **RADIAL+ANGULAR_BILINEAR_SUPPORTED** | `[VT]` | D: AV-2 G0–G2/E1–E2 all PASS; CG singlet=√2/2, C²=0.5 (2026-06-10) |
| 41 | HA-4 ONE_TRACK bridge gate | 🟢 **BG-H1 CLOSED** | `[VT]` | D: bridge-gate-1 PASS (G0+G1+E1+E2); geometry-disc step (BG-GATE §4) still open |
| 42 | Phase 3 S³×S¹ Dirac harness | 🟢 **KK harness PASS** | `[VT]` | D: BG-H1: S3XS1_KK_BRIDGE_SUPPORTED_ROBUST, 415 tests (2026-06-10) |

### Re-audit trigger

Items 33-34 (P13H, P14) will be upgraded from `[EP]` to `[VT]` or `[VR]`  
only after `git push preserve/p5-p14` from E: machine and consistency check  
against current D: Dirac operator conventions.

---

**Linked files:**
- `estimand_v0.2.0.md` — full estimand (update §6 point 6 from HA-4 above)
- `skeptic_design_v0.2.0.md` — FT-S1/S2/S3 pre-registered falsification tests
- `controls_v0.2.0.md` — Tier 1 needs Tier 1 redesign per BLOCK C finding

**Not promoted:** no observables promoted; runtime=research_only; lambda=FREE_COUPLING_PARAMETER preserved.
