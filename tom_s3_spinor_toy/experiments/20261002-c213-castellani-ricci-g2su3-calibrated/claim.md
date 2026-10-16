# C213 Claim — S6=G2/SU(3) Ricci tensor via Castellani's formula, N^010-calibrated

**Date:** 2026-10-02
**FL tier:** [ ] Micro  [ ] Standard  [x] Full
**Question type:** [x] descriptive  [ ] predictive  [ ] causal

---

## Prior Result Gate (MANDATORY)

1. Exact claim: Castellani's general rescaled-coset Riemann/Ricci
   curvature formula (arXiv:hep-th/9912277, eq. 3.35-3.36), implemented
   via machine-verified matrix/structure-constant extraction (not hand
   transcription), calibrated against N^010's own published Ricci
   tensor at TWO independent rescaling solutions, then applied to
   G2/SU(3) using G96/C210's certified data.
2. `decision.md` grep: same hits as C212 (torsion-scaling rounds,
   Dolan-Casimir) -- none compute THIS formula or THIS tensor
   (Ricci, not torsion, not operator-norm bounds). C212 itself (same
   session) computed TORSION, not Ricci -- explicitly different object,
   named as the open next step in C212's own decision.md.
3. `null_results/`/`parked/`: 0 hits for "Castellani" + "Ricci" + "G2".
4. Primary sources re-read in full (not abstract-only, not from
   memory): Castellani hep-th/9912277 (general formula + N^010 worked
   example) and the paper's own eq. (5.72)-(5.73) (the two independent
   Einstein-rescaling solutions used as calibration targets).
5. **Status:** [x] NEW. Explicitly supersedes this session's own
   earlier decision (end of previous turn) to set this derivation aside
   as "too risky to hand-transcribe" -- the risk was specifically about
   HAND transcription of abstract index formulas; this round avoids
   that risk entirely by building actual matrices and extracting
   structure constants via machine linear algebra (lstsq), the same
   methodology already used for G96/C210/C211/C212, then validating
   the RESULT (not the transcription) against two independent published
   numbers.

---

## Estimand

**Population:** two reductive homogeneous spaces: (1) N^010=SU(3)xSU(2)/
SU(2)xU(1), built from literal Gell-Mann/Pauli matrices per eqs 4.46-4.48
of the source; (2) S6=G2/SU(3), reusing G96/C210's certified complement
(6-dim, SU(3) rep 3+3bar) and su(3) stabilizer (8-dim).
**Intervention:** evaluate Castellani's general Riemann curvature
formula (eq 3.35-3.36), specialized to isotropy-irreducible (uniform
rescaling r=1) for G2/SU(3), and to the two-block rescaling (alpha for
a=1,2,3; beta for A=4..7) for N^010.
**Comparator:** N^010's OWN published Ricci tensor (eq 4.69-4.70) at
the two specific (alpha,beta) solutions (eq 5.72-5.73) that make it
Einstein (R=12e^2) -- this IS the calibration, not a separate claim.
**Endpoint:** Ricci tensor R_bd (6x6 for G2/SU(3); 7x7 block-structured
for N^010).
**Summary measure:** Einstein constant (diag value) + off-diagonal max
(should be ~0 if Einstein) + diag spread (should be ~0 if Einstein).
**MCID:** n/a -- deterministic computation; "calibration passes" means
exact numeric match (< 1e-6) to the published target, not a statistical
threshold.

---

## Claim

Castellani's general curvature formula, implemented via machine-
verified structure-constant extraction (not hand transcription of
abstract indices), reproduces N^010's published Ricci tensor EXACTLY
(R_ab=R_AB=12.0, off-diagonal ~0) at BOTH of the paper's own independent
Einstein-rescaling solutions. Applied with the SAME code (no
modification) to G2/SU(3) with uniform rescaling (isotropy-irreducible
case), it gives Ricci_bd = (5/6) delta_bd exactly (Einstein, as the
classical isotropy-irreducible-implies-Einstein theorem predicts, but
here COMPUTED, not merely cited).

---

## Kill criterion (MANDATORY)

| Kill condition | Threshold |
|---|---|
| Calibration fails at either N^010 solution | `\|R_ab-12\|>1e-6` OR `\|R_AB-12\|>1e-6` OR off-diagonal `>1e-8`, at EITHER of the two solutions -- code STOPS and does NOT compute G2/SU(3) if this fails (hard-coded in the script itself, not just a reporting convention) |
| G2/SU(3) result not Einstein | diag spread `>1e-8` -- would contradict the classical isotropy-irreducible theorem and indicate either a bug or a surprising finding requiring independent re-verification before trusting either way |
| Structure-constant extraction residual nonzero | `>1e-8` for either N^010 or G2/SU(3) -- would mean the given generators do not actually span all needed commutators (basis/embedding error) |

If FAIL (calibration) → kills: this specific implementation's
correctness; the SCRIPT ITSELF refuses to proceed to G2/SU(3) in that
case (see code: `if not calibration_passed: ... return`).
If PASS (all) → survives: a new, doubly-calibrated number for F6, with
a non-trivial structural check (Einstein-ness) passing as a bonus
consistency signal, not merely assumed.

---

## Checks planned

| # | Check | Negative control |
|---|---|---|
| T1 | N^010 structure constants match Castellani's own abstract formulas (3 spot checks) | a wrong matrix embedding would generically NOT reproduce eps_123=1, f_147=1/2, etc. exactly |
| T2 | Calibration at N^010 solution 1 (eq 5.72) | n/a -- exact published target |
| T3 | Calibration at N^010 solution 2 (eq 5.73) -- a SECOND, independent target, not just a repeat | if T2 passed by a coincidental bug that happens to work at ONE (alpha,beta) pair, a second, differently-valued pair makes that far less likely |
| T4 [structural, not pre-registered as pass/fail] | G2/SU(3) result is Einstein | this is simultaneously a CONSEQUENCE of a correct computation (classical theorem) and a cross-check (a bug would generically break isotropy, giving a non-Einstein, asymmetric-looking tensor) |

---

## What this does NOT mean

1. Does NOT establish the absolute value 5/6 as the "true" physical
   Einstein constant of S6 in any externally fixed unit -- same
   normalization caveat as C211/C212: tied to G96's Frobenius-
   orthonormal complement basis and r=1. Only dimensionless ratios
   built consistently in this SAME convention are safe to quote without
   further normalization work (e.g. comparing to a FUTURE computation
   of the round S6's Ricci constant in the identical basis convention).
2. Does NOT independently cross-check the SPECIFIC NUMBER 5/6 against a
   second, external source -- the WebSearch-synthesized "Scal=30" claim
   from the previous turn was checked against Agricola-Borowka-Friedrich
   1707.08591 and found ABSENT there; no other primary source giving
   S6's nearly-Kahler Einstein constant in a directly comparable
   convention has been checked in this round. The calibration here
   validates the METHOD (via N^010), not this specific NUMBER via a
   second independent source for G2/SU(3) itself.
3. Does NOT relate to C212's torsion (`\|T\|^2=8/9`) by any derived
   formula in this round -- a standard relation between a naturally
   reductive space's torsion and its Ricci curvature exists in the
   literature (hinted at in C212's own decision.md as a possible cross-
   check), but was NOT used or verified here; this round's Ricci
   computation is independent of C212's torsion computation.
4. Does NOT close F6 -- gives the GRAVITY/geometry side's curvature
   content for the S6 factor alone; still no combined, self-consistent
   equations of motion for the full M4xS3xS6 background.

---

## Fence (do not change without postmortem)

- lambda = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

**PASS_CALIBRATED** — calibration passed exactly at both independent
N^010 targets; G2/SU(3) result is Einstein to machine precision
(diag spread 4.44e-16, off-diagonal 3.95e-16).

**Evidence:** [VERIFIED-numpy, double-calibrated against published
source numbers, not self-referential].

**Status:** CLOSED PASS_CALIBRATED — see `decision.md`.
