# C213 Decision — S6=G2/SU(3) Ricci tensor via Castellani's formula, N^010-calibrated

**Date:** 2026-10-02
**Verdict:** PASS_CALIBRATED — S6's own Ricci tensor now explicit, double-calibrated; does NOT close F6.

## Results [VERIFIED-numpy, calibrated against published source numbers]

```
=== Calibration (N^010, two independent published solutions) ===
N_I^010  (eq 5.72, alpha^2=4,    beta^2=32):     R_ab=12.000000  R_AB=12.000000  off_diag=3.95e-15
N_II^010 (eq 5.73, alpha^2=100/9,beta^2=160/9):  R_ab=12.000000  R_AB=12.000000  off_diag=2.20e-15
Both match the published target (12.0) to ~1e-15.

=== G2/SU(3), same code, r=1 uniform (isotropy irreducible) ===
diag(Ricci) = [0.833333, 0.833333, 0.833333, 0.833333, 0.833333, 0.833333]  (= 5/6 exactly)
Einstein constant = 0.833333
diag spread       = 4.44e-16  (Einstein, to machine precision)
off-diagonal max  = 3.95e-16
```

`experiments/20261002-c213-castellani-ricci-g2su3-calibrated/results_c213.json`.

## What this is

This round reverses the previous turn's own decision (end of the prior
session turn) to set aside Castellani's general rescaled-coset
curvature formula (arXiv:hep-th/9912277, eq 3.35-3.36) as "too risky to
hand-transcribe." The risk identified then was specifically about
HAND-mapping Castellani's abstract epsilon/f-symbol index formulas
(eqs 4.49-4.52) onto this project's own objects by eye -- exactly the
failure mode this project has been burned by twice before (C205/C206,
matrix row/column convention bugs). This round avoids that risk
entirely by a different method: build N^010's actual Gell-Mann/Pauli
matrices, embed them as literal 5x5 matrices, and extract EVERY
structure constant via machine linear algebra (`lstsq` expansion in the
given basis) -- the SAME methodology this project already uses for
G96/C210/C211/C212. The abstract formulas are then independently
reproduced as a BYPRODUCT check (3/3 spot checks passed, e.g.
`[K_1,K_2]` landing in `H_3` with coefficient exactly `eps_123=1`), not
assumed.

**The calibration itself is the main event, not a formality:** the
generic curvature-formula code was run against TWO independent,
published (alpha,beta) solutions from the SAME paper (eq 5.72 and eq
5.73) that are supposed to make N^010 Einstein with R=12 (in units
e=1) -- both matched to ~1e-15, including the OFF-DIAGONAL vanishing
(which the formula does not force by construction; a wrong sign or
index anywhere in the 4-term curvature formula would generically break
this). Passing at TWO independently-valued points, not one, substantially
reduces the chance this is a lucky coincidental match.

**Only after that did the SAME, unmodified code run on G2/SU(3)** --
reusing G96/C210's own certified complement (6-dim, SU(3) rep 3+3bar)
and su(3) stabilizer (8-dim), with uniform rescaling r=1 (isotropy
irreducible: G2/SU(3) has only ONE independent rescaling parameter, not
two like N^010 -- a direct structural consequence of its complement
being a single irreducible real SU(3) representation, already
established by G96's own Step 5b).

## Why the Einstein result is evidence, not just an assumption

A classical theorem states ANY isotropy-irreducible homogeneous space
is automatically Einstein. This round's code does NOT encode that
theorem anywhere -- it computes the general, non-simplified Riemann
tensor and then the Ricci tensor from first principles (structure
constants + the generic formula), for the SPECIFIC G2/SU(3) data. That
the result came out Einstein to machine precision (diag spread 4.4e-16,
not merely "close") is a NONTRIVIAL cross-check: a bug in the
transcription, the structure-constant extraction, or the contraction
convention would generically produce a non-Einstein (or outright wrong)
answer, not a suspiciously-too-perfect one -- unlike a round-number
red flag from `skeptic-triggers.md` (F1=1.000-style), this is a
qualitative STRUCTURAL match (isotropy) the formula was never told to
produce, not a suspiciously clean round number from an under-constrained
fit.

## Clean-number note (research-methodology.md Principle 6)

`5/6` is exact in this basis. Same caveat as C211/C212: this is the
VALUE relative to G96's own Frobenius-orthonormal complement basis at
unit radius -- rescaling the complement generators or the ambient
radius rescales this number by the corresponding factor. The RATIO/
STRUCTURE (Einstein, isotropic, this specific rational value RELATIVE
to this convention) is the safe thing to carry forward, not the bare
number "5/6" quoted outside this convention.

## Relationship to existing project results (explicitly NOT claimed)

- Does NOT relate to C212's torsion (`\|T\|^2=8/9`) via any computed
  formula here -- flagged in C212's own decision.md as a possible
  future cross-check (naturally-reductive torsion-to-Ricci relations
  exist in the literature) but NOT attempted in this round.
- Does NOT relate to round111's S3 Ricci or C134/C207's ECSK torsion+
  metric EOM -- different coset factor / different formalism, as
  already established for C211/C212.
- Does NOT independently verify the bare number 5/6 against a second
  external source (the one candidate external number from the
  previous turn, "Scal=30", was checked against its claimed primary
  source and found absent there -- see C212's own decision.md).

## Kill Analysis

**What was killed:** nothing — calibration passed at both targets, and
the G2/SU(3) Einstein-ness check (not pre-specified as pass/fail, but
named in claim.md as a structural cross-check) also passed.
**What this does NOT establish:** see claim.md's 4-item "What this does
NOT mean" — most importantly, the ABSOLUTE number 5/6 is tied to a
specific normalization and has not been independently cross-checked
against a second external source.

## Next step this motivates (not started here)

1. A real, careful relation between this round's Ricci (5/6, this
   normalization) and C212's torsion (8/9, the SAME normalization) --
   both now computed in the IDENTICAL G96 complement basis, so a
   torsion-curvature consistency relation (if one is found in the
   literature for naturally reductive nearly-Kahler spaces) could be
   checked numerically without any new normalization bridge-building.
2. Independent cross-check of the bare value 5/6 against a second
   primary source, if one giving S6's nearly-Kahler Einstein constant
   in a comparable convention can be found and its normalization
   convention matched explicitly (not assumed).

## Status

`PARENT_ACTION_GATE.md` F6 section to be updated with this result.
