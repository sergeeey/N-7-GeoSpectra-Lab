# Audit: is round77 (C26) or round78 (C27) vulnerable to Tom's transpose artifact?

## Question

The 2026-07-28 sign-check on Tom Lawrence's PDF found a specific bug class:
comparing a differential operator to an abstract Lie-algebra matrix via
"matrix times a combined vector of several DIFFERENT basis functions"
silently differs from the honest per-basis-function matrix decomposition,
by a transpose. Two of this project's own results were flagged as
candidates for the same vulnerability:

- (a) round78/E12 (C27, multiplicity-2: dim ker(D_S3,t) = 2, not 1)
- (b) round77/E11 (C26, SU(2)_L x SU(2)_R representation pattern)

## Method

Read both scripts in full (`e12_multiplicity_gate.py`,
`e11_su2lr_representation_check.py`) and checked whether either constructs
the specific pattern that caused Tom's issue: THREE (or more) DIFFERENT
basis functions stacked into one artificial column vector, compared against
an abstract matrix via ordinary matrix-vector multiplication.

## Finding: NEITHER is vulnerable -- both use structurally different,
inherently unambiguous methods

**round78/E12 (C27):** the multiplicity-2 claim rests on two independent
checks, neither of which has the vulnerable shape:
1. Section A diagonalizes a genuine Hermitian operator (Peter-Weyl block,
   `np.linalg.eigvalsh`) and reads off eigenvalue MULTIPLICITY directly.
   Eigenvalue multiplicity of a Hermitian operator is a basis-independent
   fact -- there is no row/column choice to get backwards.
2. Section B checks whether a FULLY GENERIC single spinor `psi=(a,b) in C^2`
   satisfies `Omega_i(0)*psi = 0` for all i, via ordinary (unambiguous)
   matrix-vector multiplication of the genuine 2x2 spin-connection matrix
   on a genuine single spinor -- not a combined vector of several different
   basis functions being compared against a differently-indexed abstract
   matrix. Since `Omega_i(0)` is identically the zero matrix, EVERY vector
   in C^2 trivially satisfies this -- there is no comparison-method
   ambiguity possible here at all.

**round77/E11 (C26):** every check (`psi0_is_SU2L_singlet`,
`psi1_is_SU2R_singlet`, etc.) tests a transformation-law identity on ONE
single spinor function under a defined group action (`ACTION_L`,
`ACTION_R`), not a matrix-vector product against a combined vector of
distinct basis functions. No row/column choice is involved.

## Verdict

**Hypotheses (a) and (b) from the 2026-07-28 goal-expansion are both
CLOSED, negative-but-valuable.** The transpose artifact found in Tom's PDF
does not apply to round77 or round78's own methodology -- not because the
underlying physics is different, but because this project's own
verification style (direct operator diagonalization; single-spinor
transformation-law checks) was already structurally immune to the specific
bug class Tom's "matrix times combined vector" comparison exhibited.

This is a genuine, if modest, POSITIVE result: it strengthens confidence
in C26 and C27 exactly as they stand -- confirms they are not silently
resting on the same kind of comparison-method artifact just discovered
elsewhere. Multiplicity-2 (C27) remains a real, unresolved physical
question (not a bug); the SU(2)_L/R pattern (C26) remains internally
certified, not independently reproduced by a second method (that specific
upgrade -- goal-expansion hypothesis (b), "re-derive via Tom's method" --
would require an actual independent re-construction from scratch, not an
audit of the existing one; not attempted here, remains open as a separate,
larger task).

## What this does NOT mean

- Does not resolve C27 (multiplicity-2 is still an open physical gap,
  requiring a genuinely new reduction mechanism -- Majorana/reality
  condition or reconciliation with the 32-state SO(4) convention, per
  round78's own Section E, unchanged).
- Does not upgrade C26's evidence tier (still internally-certified; a real
  second independent construction, not just an audit of the first one,
  would be needed for that -- goal-expansion item (b) proper, not done
  here).
- Does not mean this project's methodology is generally immune to this bug
  class going forward -- only that these TWO specific already-existing
  checks happen not to have used the vulnerable pattern. Any FUTURE
  comparison of a differential operator to an abstract matrix via a
  combined multi-basis-function vector should apply the honest
  per-basis-function decomposition check from the start (see pearl below).

## Pearl (methodological, for future rounds)

Before comparing a differential operator's action to an abstract Lie-
algebra generator matrix, check whether the comparison uses (i) a genuine
single object under a well-defined action [safe], or (ii) several distinct
basis functions combined into one artificial vector, multiplied by a
matrix built for a different abstract space [vulnerable to the
matrix-vs-transpose artifact found 2026-07-28]. If (ii), always cross-check
via honest per-basis-function decomposition before trusting a sign.

## Check (reproduces this audit)

Read-only structural review, no new computation:
```
experiments/20260717-round78-e12-multiplicity-gate/e12_multiplicity_gate.py
experiments/20260717-round77-su2lr-correspondence-test/e11_su2lr_representation_check.py
experiments/20260728-tom-so3-harmonics-sign-check/decision.md (source of the bug-class definition)
```
