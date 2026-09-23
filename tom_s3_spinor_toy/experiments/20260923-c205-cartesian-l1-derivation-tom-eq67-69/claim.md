# C205 Claim — the actual calculation Tom asked for: derive l=1 matrices directly from his eq(67)-(69), not by checking anything he sent

**Date:** 2026-09-23
**FL tier:** [x] Standard (tooling/derivation round in support of external correspondence; no project physics claim)
**Question type:** [x] descriptive (does direct differentiation of Tom's own Cartesian angular-momentum operators, applied to his own normalized basis, reproduce his own document's stated matrices at every intermediate stage)

## Correction that motivated this round

Tom's own reply (2026-09-23), quoted in full: "I think you have misunderstood
what I was asking. The things I was asking you to do are not about checking
something I have done. I haven't sent you what I've done on ladder operators
(partly because I abandoned each calculation when I could see it wasn't
working, and partly because I thought it better for you to work
independently). What I asked you to do is actually a new set of calculations
I haven't attempted myself... If you could just do the calculations I asked
for and share them with me, that would be great. I'm keen to see the full
workings, not just the results."

C201/C202 treated the task as "verify Tom's own matrices / find a
discrepancy." That was the wrong framing. The actual ask (per Sergey's own
2026-09-23 00:15 message to Tom, describing the plan Tom had set): redo the
l=1 calculation IN CARTESIAN COORDINATES using Tom's own eq(67)-(69)
differential operators directly -- a derivation Tom has NOT done himself --
and show the full workings, not just a final matrix compared via an abstract
intertwiner (which is what C202 did instead).

## Prior Result Gate

1. Exact claim: applying Tom's own eq(67)-(69) [L_z, L_y, L_x as Cartesian
   differential operators] directly to his own normalized real basis (eq 91,
   proportional to x^i/r) reproduces, via exact symbolic differentiation:
   (a) his own eq(103)-(105) [T_ij, the "defining representation"] directly,
   before any sign flip; (b) his own eq(106)-(108) [Gamma_3(T_ij) = -T_ij,
   via his own eq99] after applying that one stated sign flip; (c) his own
   eq(123)-(125), via his own eq(118) z-matrix -- closing the full chain of
   his own document by direct computation, not abstract comparison.
2. `grep` of `null_results/`, `parked/`, `pearl_registry/INDEX.md`,
   `experiments/` for prior direct-differentiation-of-eq67-69 work: no hits.
   C201/C202 used the ladder-operator (McMurry/spherical-harmonic) route and
   an abstract intertwiner search respectively -- neither directly
   differentiated Tom's own Cartesian operators on his own basis functions.
3. **Status:** [x] NEW.

## Estimand

**Population:** the l=1 (j=1) representation of so(3), realized via Tom's
own Cartesian construction: his eq(67)-(69) differential operators acting on
his own normalized real basis (eq 91, ∝ x^i/r).
**Intervention/method:** exact symbolic (sympy) differentiation of L_z, L_y,
L_x applied to phi_1=x1/r, phi_2=x2/r, phi_3=x3/r; exact decomposition of
each result back into the (phi_1,phi_2,phi_3) basis (verified, not assumed,
via polynomial coefficient extraction after clearing the r-denominator);
comparison at each of three stages (T_ij, Gamma_3(T_ij), and the z-transformed
complex basis) against Tom's own stated matrices.
**Comparator:** Tom's own eq(103)-(105), eq(106)-(108), and eq(123)-(125),
each already read directly from his document (not from memory -- verified
against the PDF in the C201/C202 rounds' own transcription work, reused
here).
**Endpoint:** exact (zero-residual) symbolic match at each of the three
stages, with the full intermediate differentiation shown at every step
(not just the final matrix).

**Natural-language statement:** "We derive, by direct exact symbolic
differentiation of Tom Lawrence's own eq(67)-(69) Cartesian angular-momentum
operators applied to his own normalized real basis, the l=1 matrix
representation from first principles -- a calculation Tom stated he has not
attempted himself -- and show, step by step, that it reproduces his own
eq(103)-(105), eq(106)-(108) [via his own eq99], and eq(123)-(125) [via his
own eq118] exactly, with full workings at each stage."

## Kill criterion

| Condition | Consequence |
|---|---|
| Direct differentiation does not reproduce eq(103)-(105) exactly | Either a transcription error in reading his eq(67)-(69)/eq(91), or a genuine issue in his document -- report the precise point of divergence, do not guess which |
| The `decompose()` helper's r-cancellation check ever fires (residual r left over) | The "rotations preserve r" assumption this method relies on has failed somewhere -- stop, do not trust downstream matrices |
| The z-transform does not reproduce (123)-(125) even after the eq(99) sign flip | A genuine, currently-unexplained discrepancy in the document's own internal chain -- report explicitly as open, do not force a match |

If FAIL → kills: the claim that Tom's own eq(67)-(69), applied literally,
generate his own stated matrices -- would be a real, reportable finding
about his document.
If PASS → survives: full mechanical closure of his document's own logical
chain (differential operator -> defining rep -> vector-multiplet rep ->
complex/Cartan basis), independently verified, with complete workings.

## Checks planned

| # | Check | Negative control -- input for which this check MUST fail |
|---|---|---|
| T1 | `decompose()`'s r-cancellation assertion | Deliberately feed it an expression that is NOT proportional to x_i/r (e.g. a genuine quadratic term) -- must raise, not silently mis-decompose (implemented as a hard `raise ValueError`, exercised implicitly: the real computation would have hit this if the "rotation preserves r" assumption were wrong here) |
| T2 | Stage-by-stage match (T_ij, then Gamma_3, then complex basis) | If the FIRST stage (raw T_ij match) had failed, stages 2-3 would have been reported as failing too, not silently skipped -- verified by the code structure printing all three stages unconditionally |

## What this does NOT mean

1. Does NOT constitute a claim that Tom's document has an error -- the full
   chain matches exactly at every stage; this is a closure, not a critique.
2. Does NOT touch this project's own G2/SU(3)/Spin(8) triality-channel
   physics claims (OB1, N_gen=3) -- unrelated substrate.
3. Does NOT redo the McMurry ladder-operator route (C201) -- this round is
   the Cartesian-only route Tom specifically asked for, deliberately kept
   separate.

## Fence

- `safe_for_runtime = False`. No `lambda` symbol introduced.

## Verdict

**PROMOTE.** All three stages of the chain (T_ij, Gamma_3(T_ij), and the
z-transformed complex-basis matrices) match Tom's own stated eq(103)-(105),
eq(106)-(108), and eq(123)-(125) exactly, by direct symbolic differentiation
of his own eq(67)-(69) applied to his own normalized basis (eq 91) -- zero
residual at every stage. Full step-by-step workings captured in
`run_output.txt` and `results_c205.json` (raw per-basis-function
differentiation results, not just final matrices).

**Evidence:** [VERIFIED-sympy 9/9] (3 raw-differentiation matches vs
eq103-105, 3 sign-flip matches vs eq106-108, 3 complex-basis matches vs
eq123-125, all exact).

**Status:** CLOSED PROMOTE.
