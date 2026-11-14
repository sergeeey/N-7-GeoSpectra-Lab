# C152 — Term2 vanishing on SU(3)/T^2 — REJECT (the phenomenon was not real)

**Date:** 2026-09-04. **Verdict:** REJECT. **Skeptic (Step 8a, context-blind):** FALSIFIED, and correct.

## The claim that died

C152 claimed to explain why `Term2` annihilates the `T^2`-invariant sector on
`SU(3)/T^2`, and offered a mechanism: exactly 2 of 6 directions live per
matrix entry, equal magnitude, opposite sign, cancelling — forced by
`T^2`-equivariance of the connection rather than by nearly-Kahler geometry.

**Term2 does not vanish there.** Every measurement above was taken on an
invariant sector built with a NON-EQUIVARIANT generator, inherited from C151.

## The defect and its adjudication

`c151_stage2_construct.py:205` pairs `spin_lift(T2_M)` with `+T2_M` on `W`;
`spin_lift(L)` generates the vector action `-L` (the scripts' own gate
measures `SPIN_VS_VEC = -1`), so the consistent pairing is `(spin_lift(L), -L)`
— which the `S^6` side always used (`C139.rho_vector = -bivec`).

Adjudicated internally, no external constant required: the twisted Dirac
operator must commute with the true generator.

```
[D,G] with +T2_M : 2.000e+00      [D,G] with -T2_M : 0.000e+00
same adjudicator on S^6: +ADNU 3.333e-01, -ADNU 1.509e-17 (= C139/C145's choice)

C151's sector    (+1): max|Term1| = 0.000e+00   max|Term2| = 0.000e+00
corrected sector (-1): max|Term1| = 0.000e+00   max|Term2| = 1.000e+00
```

## Kill Analysis

**Killed:** the whole C152 claim about `Term2` — pairwise cancellation, the
equivariance mechanism, the `S^6` contrast, the root-type-versus-fundamental
-type reading, the Step 5 `J`-scan conclusion. Not weakened; the object
described does not exist.

**NOT killed:**
- `Term1 = 0`, weight-forced, per direction, on both spaces — sign-independent,
  verified `0.000e+00` in BOTH sectors, and reproducing C146 from a different
  starting point than C146's own Schur argument.
- The elementary-transition language (6 admissible paths per space, 2 per
  domain vector, 6 of 9 entries allowed).
- C144, C145, C146, C147 on `S^6` — untouched; the `S^6` side was correct all
  along.
- C151's Stages 0, 1a, 1b and the Stage 2a construction — all sign-independent.

**Relaxation Map:** none. The claim must not be revived in weakened form; the
phenomenon was not real.

## What the round produced instead

The correction made C151's still-frozen, still-blind pre-registered prediction
live again, and it was executed and CONFIRMED: `c(J.nabla) = +i c(nabla)`
exactly, entrywise, 8/8 draws, holding for exactly `J_NK` and its conjugate
(1.8e-31) and failing for the other six invariant a.c.s., for random `J'`
(0/5) and for random real-linear maps of the same shape (0/3). See
`experiments/20260904-c152-term2-vanishing-mechanism/decision.md` and
`CLAIM_LEDGER.yaml` C152.

## Why no gate here caught it

Sector dimensions are `(3,3)` for BOTH signs, so every dimension check passed;
and C151's Stage 2a Killing-spinor calibration gate, though genuine, never
touches the `W` action — it is structurally blind to this defect. The only
sign-sensitive gate in the line was C145's `1.154701`, which exists only on the
`S^6` side. That asymmetry is the whole story.
