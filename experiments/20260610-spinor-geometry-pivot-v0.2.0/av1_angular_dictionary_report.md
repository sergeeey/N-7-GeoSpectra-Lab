# AV-1 Report — Dictionary Robustness of tom_ansatz ↔ φ₁₁

**Experiment:** AV1_ANGULAR_DICTIONARY_ROBUSTNESS
**Date:** 2026-06-10
**Pre-registration:** claim_av1_angular.md (written BEFORE code ran)
**Code:** `tom_s3_spinor_toy/av1_angular_dictionary.py`
**Tests:** `tom_s3_spinor_toy/tests/test_av1_angular_dictionary.py` — **15/15, 0.43s** (suite: 90/90)
**Raw data:** `av1_angular_dictionary_results.json`
**Status:** research_only — no physical promotion

---

## Verdicts

```
AV-1a  PASS   argmax over 49-mode dictionary = (1,1); convention-robust
AV-1b  PASS   5-term residual 2.9% < 5%; first greedy pick = φ₁₁
AV-1c  FAIL   bilinear residual 12.38% > 10% pre-registered threshold
H-T1   NOT PROMOTED  signal present (92.4%) but promotion required AV-1c PASS
```

## AV-1a — φ₁₁ identification is dictionary-robust [VERIFIED-tool]

Top-5 of 49 modes (weighted L², n_grid=4000):

| (n,l) | cos | note |
|---|---|---|
| (1,1) | **0.9594** | argmax; 0.9594² = 0.9204 (legacy squared convention) |
| (0,0) | 0.9400 | |
| (2,2) | 0.9385 | |
| (3,3) | 0.9124 | |
| (4,4) | 0.8871 | |

- No off-diagonal mode (n≠l) enters top-5: **top-5 is exactly the n=l boundary family.**
- Sensitivity 1 (unweighted L²): argmax still (1,1). Sensitivity 2 (n_grid 8000): value unchanged to 6 decimals.
- **Convention note resolved:** legacy regression value 0.920391 is cos²; AV-1 reports cos = 0.959369. Same finding, two notations — no contradiction.

## AV-1c — HONEST FAIL: bilinear (eq. 49) radial probe

Pre-registered kill threshold: 5-term residual < 10%. Actual: **12.38%** (weighted), 19.76% (unweighted). Kill condition fired.

**Constraint recorded:** sin(2α) = tom_ansatz² = 2√||g|| is NOT efficiently
captured by ≤5 *diagonal* Dirac bilinears φ_{nl}². Partial signal remains:
φ₁₁² is the first greedy pick.

**Scope of the FAIL (important):** only diagonal squares φ_{nl}² were in the
dictionary. Tom's eq. (49) generically contains cross-bilinears
ψ̄_{nl}ψ_{n'l'}. The fail constrains the *diagonal-only* radial ansatz, not
eq. 49 itself. Off-diagonal bilinear dictionary = candidate AV-1c′ follow-up.

## H-T1 — exploratory observation, NOT promoted

The n=l boundary family spans 92.4% of ‖tom̂‖² (threshold was 80%), and
fills the entire top-5 of AV-1a. **Promotion blocked** by the pre-registered
rule (required AV-1c PASS). Stays recorded as:

> *H-T1 (exploratory): the radial layer of Tom's eq.-49 expansion of √||g||
> on S³ concentrates on the n=l boundary family of Dirac modes.*

Re-promotion path: pass AV-1c′ (off-diagonal bilinears) → revisit.

## Item 40 status update

| Before | After |
|---|---|
| `[RADIAL_PROJECTION_FINDING_ONLY]`, angular pending | `[RADIAL + DICTIONARY_ROBUST]`, angular pending (AV-2) |

What is now stronger for communicating to Tom:
1. φ₁₁ dominance survives a 49-mode search incl. off-diagonal modes — not an artifact of the diagonal-only scan.
2. Convention-robust (weighted/unweighted, two grids).
3. The 0.92 number clarified: cos² = 0.9204, cos = 0.9594.

What still blocks "definitive mode identification":
1. AV-2 — full angular/spinor check (half-integer Hopf weights, spin connection, 2D operator). NOT done.
2. AV-1c constraint — the bilinear layer of eq. 49 needs cross-terms.

## What This Does NOT Mean (from pre-registration, confirmed applicable)

1. No full angular/spinor verification (AV-2 pending).
2. Nothing about S⁶ factor or f^{αχ} cross-couplings.
3. No physical promotion; λ = FREE_COUPLING_PARAMETER.
