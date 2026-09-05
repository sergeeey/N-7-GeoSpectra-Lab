# C152 — Decision. Verdict: **REJECT** (own claim falsified) — and the round's real yield

**Date:** 2026-09-04. **Tier:** FL Full. **L0:** descriptive.
**Skeptic (Step 8a, context-blind, code-only): FALSIFIED — and correct.**

## Headline

C152 set out to explain why `Term2` annihilates the invariant sector on
`SU(3)/T²`. **It does not.** There was nothing to explain. The zero was an
artifact of an invariant sector built from a non-equivariant group action — a
defect inherited from C151, which C152 reproduced faithfully and therefore
inherited too.

Two consequences, both larger than this round's own claim:

1. **The C151 verdict "c is identically zero, VACUOUS" is RETRACTED.**
2. **The C151 pre-registered question is ANSWERED, and it is CONFIRMED.**

## How it was caught

The FL Step 8a skeptic, given only `claim.md` and the scripts, no session
history, could not execute anything (no Bash) and reasoned from the code:

> `c151_stage2_construct.py:205` pairs `spin_lift(T2_M)` with `+T2_M` on `W`,
> while the S6 side pairs `spin_lift(ADNU)` with `-bivec(ADNU)`. The scripts
> own gate measures `[spin_lift(L), e_j] = -(L e_j)`, so the consistent
> pairing is `(spin_lift(L), -L)`. SU(3)/T2 uses the wrong one.

Per this project audit-verification-gate, an agent `[DERIVED]` is my
`[HYPOTHESIS]`. I adjudicated it with an internal test needing no external
constant: **the twisted Dirac operator must commute with the true generator.**

```
[D,G] with C151's  +T2_M  : 2.000e+00    <- D is NOT equivariant
[D,G] with         -T2_M  : 0.000e+00    <- exact

same adjudicator on S^6, where C145's 1.154701 fixes the answer independently:
    +ADNU : 3.333e-01        -ADNU : 1.509e-17   = C139/C145's own choice
```

The adjudicator picks the convention S6 already uses, on the space where an
externally calibrated number exists. It then rules against C151 on the flag
manifold. Consequence:

```
C151's sector    (+1): dims (3,3)  max|Term1| = 0.000e+00  max|Term2| = 0.000e+00
corrected sector (-1): dims (3,3)  max|Term1| = 0.000e+00  max|Term2| = 1.000e+00
```

Sector dimensions are (3,3) **either way** — which is exactly why every
dimension check in C151 and C152 passed, and why the Killing-spinor
calibration gate (which never touches the W action) passed too. The only
sign-sensitive gate in the whole line lived on the S6 side.

## What survives

- **Term1 = 0, weight-forced, per direction, on both spaces.** Sign-independent
  (it uses only Sigma-weights), and verified `0.000e+00` in **both** sectors.
  Step 1 also reproduces C146 from a different starting point than C146 own
  Schur argument. This clause of `claim.md` is CONFIRMED.
- The elementary-transition language itself (Step 1): 6 admissible paths on
  each space, 2 per domain vector, 6 of 9 entries allowed.

## What is withdrawn

- Every C152 statement about Term2 on SU(3)/T2: the pairwise cancellation, the
  equivariance mechanism, the S6 contrast, the root-type-versus-fundamental
  -type reading, and the Step 5 J-scan conclusion. All were measured on the
  wrong sector.
- The Step 5b vacuity check was correct in its own terms and did refute my
  suspicion — but it checked the wrong vacuity, exactly as the skeptic said.

## The real yield: the C151 pre-registered question, answered

The prediction was frozen in `PREREGISTRATION.md` **before any c existed**, and
the CORRECTED c had never been computed by anyone, so the test was still
blind. Run on the corrected sector, vacuity gate first and dominant:

```
GATE  equivariance of D for the corrected generator : max|[D,G]| = 0.000e+00
GATE  corrected sector dims                         : (3, 3)
VACUITY GATE  max|c| on the 6 family basis vectors  : all 1.0000  -> NONZERO

  draw 0: max|c| = 1.4142   max|c(Jv)| = 1.4142   C-LINEAR (+i)
  ... 8 draws, all C-LINEAR (+i), entrywise, as matrices
```

**c(J.nabla) = +i . c(nabla) exactly**, on every draw, as matrices entry by
entry — the form the pre-registration froze, explicitly not weakened to norms.

### Is that confirmation falsifiable? (run BEFORE reporting it)

C151 has already produced one false PREDICTION CONFIRMED here, so this was
gated rather than trusted.

```
N2  the 8 invariant a.c.s.:  C-linear for exactly 2
       eps=( 1, 1, 1)  True    max rel. deviation = 1.813e-31
       eps=(-1,-1,-1)  True    max rel. deviation = 1.799e-31
       the other six   False   deviations 1.6 - 2.0
N1  5 random J' (J'^2=-1)       : 0/5 hold  (deviations 0.83 - 1.32)
N3  3 random real-linear maps   : 0/3 hold  (deviations 1.48 - 1.95)
N4  the OLD (wrong-sign) sector : max|c| ~ 1e-16 -> vacuous, as expected
```

Stage 2a had already aligned J_NK to the standard J_0, so eps=(1,1,1) IS J_NK
in that basis and (-1,-1,-1) is its conjugate. **The identity holds precisely
for the nearly-Kahler almost-complex structure and its conjugate, and for
nothing else** — machine-exact (1.8e-31) where it holds, order-unity where it
fails. N4 confirms it was the sign correction that made the test live.

### Verdict on the C151 frozen prediction

**CONFIRMED.** The C-linearity found on S6 (C147, exact) recurs on SU(3)/T2,
the only independent homogeneous nearly-Kahler space on which this project
construction is well-posed (C140). It is therefore **not** a G2/SU(3)
accident. Per the pre-registration own outcome table this "substantially
raises the value of the whole E_W / connection-coefficient line".

## Kill Analysis (mandatory for REJECT)

**What the null result killed:** the C152 claim, entirely — every clause about
Term2 on SU(3)/T2. Not weakened; the object it described does not exist.

**What was NOT killed:**
- Term1 weight-forced vanishing on both spaces (independent of the defect).
- C146, C147, C145, C144 on S6 — untouched. The defect is in the SU(3)/T2
  sector construction only, and the S6 side was correct all along.
- C151 Stages 0, 1a, 1b (family dimension 6, J pinned by Nijenhuis, sectors
  (3,3)) — all sign-independent, all still valid.
- The C151 Stage 2a calibration gate — still valid, but now known to be
  **blind to this defect**, since it never uses the W action.

**Relaxation Map:** none needed. The claim is not to be revived in a weakened
form; the phenomenon it described was not real.

## Process record — five defects in one round, and the one that mattered

| # | defect | caught by |
|---|---|---|
| 1 | family built in raw basis, operator in J-aligned basis | the script own CONTRADICTS-C151 guard |
| 2 | +ADNU_M where C139 uses -bivec | the C145 1.154701 regression |
| 3 | -t2 plus wrong projection when rebuilding Stage 2a | the reproduce-C151 gate |
| 4 | my guess that Step 5 was vacuous | Step 5b — **refuted my guess** |
| 5 | **the C151 sector non-equivariant generator** | **the context-blind skeptic, from code alone, without running anything** |

Defects 1-3 were mine and were caught by gates I had built. Defect 5 was **not
mine to catch that way** — every gate I had was blind to it, because each was
calibrated on the S6 side or on sign-insensitive dimensions. It took an
outside reader with no access to my reasoning. This is the strongest single
vindication of the Context Asymmetry Rule in this project record: the skeptic
could not run one line of code and still overturned two rounds.

Note what the same event says about the S6 regression: it is the only reason
defect 2 was caught, and its absence on the SU(3)/T2 side is exactly why
defect 5 survived. **An externally calibrated number on each side of a
comparison is not redundancy; it is the gate.**

## Reproduce

```
python c152_step1_paths.py             # weight paths (survives)
python c152_step6_sign_adjudication.py # THE correction: [D,G] adjudicator
python c152_step7_c151_rerun.py        # C151 frozen prediction, corrected sector
python c152_step8_falsifiability.py    # N1-N4 controls on that confirmation
```

Steps 2-5b are retained unmodified as the record of the falsified line; their
outputs are measurements on the wrong sector and must not be cited.

pytest 2524 passed / 4 skipped; ruff clean.
