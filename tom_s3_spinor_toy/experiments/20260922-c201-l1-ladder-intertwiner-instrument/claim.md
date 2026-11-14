# C201 Claim — verify the McMurry 6.3(a) l=1 ladder-operator result by tool, and pre-validate the T_i U = U L_i intertwiner test on a KNOWN case before Tom's matrices arrive

**Date:** 2026-09-22
**FL tier:** [x] Standard (tooling/instrument-validation round in support of external correspondence; no project physics claim)
**Question type:** [x] descriptive (is a specific textbook computation correct, and does a known-answer positive control validate the planned intertwiner test)

**Source:** direct follow-up to the Tom Lawrence correspondence-prep session (2026-09-19/22).
Tom asked (McMurry 6.3(a)) for the l=1 ladder-operator relations on spherical
harmonics, then to build 3x3 matrices and compare with his own (unseen)
matrices (123)-(125) via "do they relate as linear combinations." The user's
own review sharpened this to the correct test: does an invertible intertwiner
`U` exist with `T_i U = U L_i` for all three generators `i` (equivalence of
representations), rather than "do the matrices look similar."

## Prior Result Gate

1. Exact claim: (a) McMurry's own l=1 ladder relations, computed with ONLY
   McMurry's own stated definitions (L± differential operators, (4.45),
   P_1^0=cos(theta), P_1^1=sin(theta) with no extra Condon-Shortley factor),
   give a clean sqrt(2) for all four non-zero actions, symbolically, exactly.
   (b) the resulting 3x3 matrix representation is equivalent (via an explicit,
   found intertwiner) to the standard real Cartesian vector representation of
   so(3) -- i.e. this instrument, applied to a case whose answer is already
   known (l=1 spherical harmonics ARE linear combinations of x,y,z/r), returns
   the correct verdict (EQUIVALENT, nonzero U found) rather than a false
   NO_INTERTWINER or a wrong U.
2. `grep` of `null_results/INDEX.md`, `parked/INDEX.md`, `pearl_registry/INDEX.md`,
   and `experiments/` for "ladder operator", "Y_{1,", "McMurry": zero hits.
   Genuinely new; nothing to collide with.
3. **Status:** [x] NEW.

## Estimand

**Population:** the single l=1 (j=1) representation of so(3)/SU(2), realized two
ways: (i) complex spherical harmonics Y_{1,-1,0,1} under McMurry's L± operators,
(ii) the real Cartesian vector rep (x,y,z) under the standard so(3) generators.
**Intervention/method:** symbolic (sympy, exact, not numeric-approximate)
computation of L±Y_{1,m}; construction of the 3x3 matrix form; construction of
the standard Cartesian so(3) generators; search for an intertwiner `U` with
`T_i U = U L_i` for i=x,y,z (equivalently via L± <-> Lx,Ly).
**Comparator:** the well-known textbook answer (l=1 ladder coefficients = sqrt(2)
throughout; l=1 spherical harmonics are proportional to x,y,z/r) -- this round's
job is to confirm a TOOL reproduces the known answer, not to discover new physics.
**Endpoint:** (a) symbolic residual of each L±Y_{1,m} vs the predicted sqrt(2)
multiple -- must be exactly 0 after `sympy.simplify`; (b) existence and rank of
`U` solving `T_i U = U L_i` for all i simultaneously; (c) 1-dimensionality of
the commutant of {Lx,Ly,Lz} (Schur/irreducibility check), as a worked template
for the "invariant does not imply irreducible" caution raised in the same
correspondence-prep discussion.

*Natural-language statement:* "We verify, by exact symbolic computation using
only McMurry's own stated definitions, that the four non-zero l=1 ladder-operator
actions each carry coefficient sqrt(2), and that the resulting 3x3 matrix
representation is equivalent, via an explicitly found invertible intertwiner, to
the standard Cartesian vector representation of so(3) -- validating the
T_i U = U L_i test methodology on a case with a known answer, before applying it
to Tom Lawrence's own (123)-(125) matrices once received."

## Kill criterion

| Condition | Consequence |
|---|---|
| Any of the four symbolic L±Y_{1,m} computations does NOT simplify to exactly sqrt(2) times the expected neighbour | McMurry-internal-consistency claim FALSIFIED; report exact discrepancy instead of asserting sqrt(2) |
| No invertible `U` found solving `T_i U = U L_i` for the KNOWN l=1-vs-Cartesian case | The intertwiner-test METHOD itself is broken (wrong generator convention, sign, or normalization) -- do NOT trust it on Tom's real matrices until fixed |
| Commutant of {Lx,Ly,Lz} is NOT exactly 1-dimensional (up to numerical/symbolic tolerance) | l=1 is not irreducible under this generator set as constructed -- a convention bug, not a physics finding |

## What this does NOT mean

1. Does NOT depend on, or wait for, Tom's own "notes sent 7 September"
   (equations (67)-(69), (123)-(125), (136)) -- those remain unavailable; this
   round validates the METHOD on a substitute known case only.
2. Does NOT constitute a reply to Tom or any claim about his own calculation's
   error -- purely internal tooling validation.
3. Does NOT touch this project's own G2/SU(3)/Spin(8) triality-channel physics
   claims (OB1, N_gen=3) -- unrelated substrate (l=1 of SO(3), not S3xS6).

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced.

## Verdict

**PROMOTE, narrowly scoped.** All pre-registered checks pass by exact symbolic
computation (`sympy`, zero approximation), on the CONTROL l=1 case only. One
real bug was caught and fixed during the run: a hand-typed Cartesian generator
had a sign error, correctly diagnosed as a bad control (Part 2 had already
independently verified the spherical side), not a physics disagreement --
recorded as a genuine but UNPLANNED negative control, not a designed one. Two
follow-up checks (a deliberate negative-control unit test; a `U(2*pi)` full-
rotation discriminator for genuine half-integer/spinorial content, which the
Hom/intertwiner test alone cannot distinguish from ordinary integer spin) are
parked with explicit trigger conditions in `decision.md`, not run this round.
Nothing here establishes anything about Tom Lawrence's own (123)-(125) --
those remain unseen.

Status: CLOSED PROMOTE (instrument calibration only).
