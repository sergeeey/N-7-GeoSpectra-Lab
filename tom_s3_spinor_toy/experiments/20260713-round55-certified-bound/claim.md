# Round55-CertifiedBound Claim — certified K_cert for the full correction operator

**Date:** 2026-07-13
**FL tier:** [x] Standard (arithmetic/eigenvalue certification on already-built fixed matrices, no new representation)
**Question type:** [x] descriptive

---

## Prior Result Gate (MANDATORY — fill BEFORE writing anything below)

1. Exact claim: does the combined correction operator
   `Q_ρ = torsion_cross_term + mixed_AB_term` admit a CERTIFIED (exact/
   symbolic, not numerical-estimate) upper bound `‖Q_ρ‖≤K_cert√C₂(ρ)`,
   via the operator Cauchy-Schwarz method the user specified, with a
   mandatory completeness audit and normalization gate run first?
2. `decision.md` grep: done — direct continuation of Round 54's own
   deferred "Round 55" recommendation.
3. `round*_claim.md` + scripts grep: done via Round 52-54's own gates.
4. `null_results/` + `parked/` grep: done, confirmed NOT the R45-Leibniz
   duplicate (same distinction re-verified in Round 53/54's own gates).
5. `git log -S`/`-G` pickaxe: done via prior rounds' gates.
6. Primary source re-read: done — Round 22's own code
   (`g2su3_nomizu_crossterms.py`, `g2su3_equivariance_check.py`,
   `g2su3_H_element.py`, `g2su3_v7_multiplicity_dirac.py`) read and
   executed directly this round, not paraphrased.
7. **Status:** [x] OPEN → this round.

---

## Estimand

**Population:** the correction operator `Q_ρ=torsion+mixed_AB` (Round
54's scope), tested for a certified bound rather than a numerical
estimate.
**Intervention:** (a) Casimir normalization gate on ρ=7; (b) full
completeness classification of all 5 of Round 22's pieces; (c) combine
`B_r^T+B_r^AB` before norming; (d) certified `K_L,K_R` via exact
symbolic eigenvalues of `H_L=ΣB_rB_r†`, `H_R=ΣB_r†B_r`; (e) positive
control, Hermiticity control, component controls.
**Comparator:** the crude triangle-inequality sum `Σ‖B_r‖`, and Round
54's own un-certified structural claim.
**Endpoint:** `K_cert`, exact and certified, in the established Bourbaki
`C₂(G₂;(1,0))=4` normalization used throughout Rounds 52-54.
**Summary measure:** a single number, `K_cert = 2√6/3 ≈ 1.633`.
**MCID:** N/A — descriptive certification.

---

## Claim

`K_cert = 2√6/3` (exact, via `min(√(max eig H_L), √(max eig H_R))`,
both certified via exact symbolic eigenvalue computation, converted
from the native `ρ_7(e_p)`-basis normalization to the established
Bourbaki `C₂=4` convention via a certified `√2` rescale factor),
satisfies `‖Q_ρ=7‖ ≤ K_cert·√C₂(ρ=7) = 2K_cert` — verified directly
against Round 22's own, unmodified `torsion_cross_term`/`mixed_AB_term`
functions as a positive control.

**Important finding from the completeness gate, reported honestly, not
resolved fully:** `casimir_term` (using only the 6 𝔪-direction
generators) does NOT by itself equal the abstract G₂-Casimir `C₂(G₂;ρ)`
— the full 14-generator Casimir requires the 8 SU(3)-direction
generators `ν_k` too (Step 0 verifies this: 14-generator sum gives 2·I
in native units, matching Bourbaki 4 after rescale; the 6-generator-only
sum alone is NOT scalar). Separately, `termB_squared` (`D64²`), while
confirmed `ρ`-independent (Round 54), was found to have a nonzero,
computable eigenvalue (4, in native units, on the `singlet_1` test
vector) — meaning it is a KNOWN, FIXED, ρ-independent additive constant
contributing to the total operator, not literally zero and not an
unbounded unknown either. Whether `CASIMIR+D64²+SU3-CURVATURE` together
reproduce the "official" cubic KP eigenvalue `C₂(G₂;ρ)-C₂(SU(3);σ)`
exactly (which would fully justify treating them as pure "baseline,
already counted in Round 52's `-3`") is NOT fully resolved in this
round — the one test vector checked (`singlet_1`, σ=(0,0)) gives
baseline value 6 (native units), and reconciling this exactly against
the abstract KP formula in a fully general way (across all σ types) is
flagged as a residual question, not asserted as closed.

---

## Kill criterion (MANDATORY — fill BEFORE running)

| Kill condition | Threshold |
|---|---|
| Normalization gate: 14-generator sum is not a clean scalar multiple of identity | any non-scalar result |
| H_L or H_R not Hermitian / not PSD | any negative or complex eigenvalue |
| Positive control: computed `‖Q_7(singlet_1)‖/‖singlet_1‖` exceeds `2K_cert` | ratio > 2K_cert |
| Component controls: torsion/mixed_AB individually absent (zero) where expected nonzero | either component identically zero where Round 22 found it nonzero |

If FAIL → kills the certified bound, STOP, do not report K_cert.
If PASS → K_cert stands as certified (all 4 conditions checked and
passed, see `decision.md` for exact values).

**All 4 conditions checked: PASS** (see script output / `decision.md`).

---

## Checks planned

- T1 (Step 0): Casimir normalization gate, 14-generator trace-form
  orthonormality + scalar check on ρ=7.
- T2 (Step 1): completeness classification of all 5 Round-22 pieces.
- T3 (Step 1b, adversarial): does baseline reproduce the naively-expected
  cubic eigenvalue? — found NO (my own expectation was wrong, not a
  bug — see Claim section), informative finding reported honestly.
- T4 (Step 2-3): build `Q_7`, compute `H_L`, `H_R`, exact eigenvalues,
  `K_cert`.
- T5 (Step 4): positive control, `‖Q_7(singlet_1)‖` vs `2K_cert`.
- T6 (Step 5): component controls (torsion, mixed_AB individually
  nonzero and distinct).
- T7 (Step 6): Hermiticity/PSD control on `H_L`, `H_R`.
- T8 (Step 7): basis-rotation control — **NOT PERFORMED**, flagged
  honestly as an open gap requiring substantial additional machinery
  (rebuilding the torsion table under a generic `SO(6)` rotation), out
  of this round's scope.

---

## What this does NOT mean

1. Does NOT fully resolve whether `CASIMIR+D64²+SU3-CURVATURE` exactly
   reproduce the abstract cubic KP formula `C₂(G₂;ρ)-C₂(SU(3);σ)` in
   general (only spot-checked on one test vector, found a nonzero,
   fixed, computable value not previously accounted for).
2. Does NOT perform the basis-rotation control (Step 7) — an honest,
   flagged gap, not silently skipped.
3. Does NOT compute the finite exceptional set (deferred to a future
   "Round 56", pending resolution of the completeness question above).
4. Does NOT touch `preprint.tex`.
5. Does NOT compute anything for ρ=27, 64, or 77 specifically.

---

## Fence (do not change without postmortem)

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
