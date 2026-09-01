# C122 claim -- random-matrix negative control for C118's density
hypothesis (named by C118's own skeptic pass, never run)

## Question type (EstimandOps L0)
**Descriptive.** Direct comparison of a computed statistic (`s*`, the
critical removal fraction) between the real operator family and a
matched-dimension random-matrix family. No causal or predictive claim.

## Background

C118 v2 found `s*` (critical removal fraction for the corner
component) decreasing with dimension across 5 real cells
(0.639, 0.460, 0.134, 0.164, 0.073 at dims 68,130,212,314,436). FL
Step 8a skeptic found this consistent with `s* ~ 1/dim`, a pattern a
content-free extreme-value-counting null could also produce, and named
the cheapest actually-discriminating test, never run: a random-matrix
negative control at matched dimensions and matched perturbation norm.

## Falsifiable claim

Build, for each of the SAME 5 dimensions as C118's real cells
(68,130,212,314,436), a random matrix `D_rand` with a REAL spectrum
via similarity transform (`D_rand = S @ H0 @ inv(S)`, `H0` random
Hermitian, `S` random invertible -- non-Hermitian but real-spectrum,
matching the REAL construction's own defining property, not literal
Hermiticity) and a random Hermitian perturbation `Delta_rand`
normalized to `||Delta_rand||_2 = 1` (matching C117's own established
fact that the real `||Delta_H||_2 = 1` exactly at every cell). Run
C118's own `find_critical_s` UNMODIFIED via direct import.

**Pre-registered prediction:** if the real `s*` trend is a content-
free extreme-value-counting artifact (density hypothesis), the random
family should show the SAME qualitative trend (`s*` decreasing with
dimension, `s* * dim` roughly constant). If the real `s*` trend
reflects something specific to the actual operator's algebraic
structure, the random family's `s*` should NOT reproduce it.

**Kill criterion:** if the random family's `s* * dim` values fall in
the same rough range (order of magnitude) as the real family's
(`28.5` to `59.8`, per C118's decision.md), the density/extreme-value-
counting explanation is SUPPORTED and the entire C118 line is
retired as measuring dimension alone, not physics. If the random
family's `s* * dim` is systematically very different (e.g. orders of
magnitude off, or non-monotone in a qualitatively different way), the
real `s*` trend is NOT explained by density alone and may carry real
information after all -- worth the more expensive follow-up C118's own
decision.md named (`kappa(V)` measurement, fine rescan).

## SUBSTRATE FAILURE (v1, 2026-09-01) -- category error, not a
conditioning confound; corrected same session

v1 used a random **complex Hermitian** perturbation. FL Step 8a
skeptic found this a category error, not the "confounded by
conditioning" issue v1's own decision.md first proposed: the REAL
`Delta_H` (C118) is REAL SYMMETRIC (`D_PW` built entirely from
`np.float64`), so `D_PW - s*Delta_H` stays real for every `s` --
complex eigenvalues can only appear via a genuine COLLISION, a real
threshold. v1's complex perturbation made `D-s*Delta` complex
immediately for any `s&gt;0`, so `Im(eigenvalue)` grew LINEARLY from
`s=0` with no threshold at all -- v1's reported `s*` (bit-identical
`0.05/2^16` at every dimension) was a pure artifact of the search grid
and tolerance, containing zero information about the matrices drawn.
Same substrate-failure class as C118's own v1 (deleted pre-commit for
an analogous reason). **Corrected in v2:** real symmetric perturbation
(matching the real family's symmetry class exactly) plus a log-spaced,
finely-tolerant search appropriate to the much smaller collision scale
this construction implies.

## SUBSTRATE FAILURE (v2, 2026-09-01) -- comparison methodologically
broken (asymmetric instruments), not the physics; corrected same
session

v2 fixed v1's category error but FL Step 8a skeptic found the
COMPARISON itself invalid: v2 searched the random family on a fine
log-spaced grid but compared it against the REAL family's `s*` values
taken from C118's own coarser search (`np.linspace(0,1,21)`, step
0.05) -- meaning the real family was never sampled in the region
`(0,0.05)` where every one of v2's random `s*` values fell. "No
overlap" therefore compared apples to an interval the real family was
never measured in. Also found: v2's own pre-registered kill criterion
(matching power-law exponents) was actually satisfied by the random
family and unreported; v2's headline "30-300x" figure was
arithmetically wrong (true per-dimension ratios were 15-195x, computed
by mixing max/min across DIFFERENT dimensions rather than comparing at
the same one). **Corrected in v3:** rebuilds the REAL matrices via
C118's own `build_cell` (unmodified) and runs the IDENTICAL fine
search on both families -- a genuinely NOT-yet-symmetric instrument,
see below.

## SUBSTRATE FAILURE (v3, 2026-09-01) -- PARKED, not resolved, after a
third skeptic pass found two new decisive problems

v3's own "fine" log-spaced grid had a hole (`0.389` to `0.624`) WORSE
than C118's own linear grid in exactly that region -- confirmed
directly against `results_c118.json`'s own j2=3/2 coarse scan, whose
real crossing window `(0.45,0.60)` sits entirely inside v3's gap. v3's
"corrected" j2=3/2 value (88.3) was itself wrong -- a bisection landing
on the SECOND crossing, not the first; C118's ORIGINAL value (59.8)
was correct all along. Separately, v3's `kappa(V)` analysis used the
wrong variable (`s*.dim` instead of raw `s*`, per Bauer-Fike) and was
statistically underpowered (5 points; the 95% CI on the log-log slope
contains the pure-conditioning prediction). Most decisively: the
random control was never matched on distinct-eigenvalue count -- the
real family has 16-40 distinct eigenvalues (exact degeneracy from its
own `kron(I,dbar)` construction), the random family 68-436 -- a 4x-11x
mismatch GROWING with dimension, in exactly the direction that could
produce the observed gap from density alone, no representation theory
needed. **Every specific quantitative claim from v2 and v3 is
retracted.** This experiment is PARKED, not resolved -- see
`decision.md` for the full account and the concrete, specific reopen
condition (a genuinely degeneracy-matched control, per-eigenvalue
conditioning, union search grid, multi-seed averaging -- a real round
of design work, not a quick patch).

## What this round does NOT show

- Does not identify WHAT the real `s*` trend means if the negative
  control fails to reproduce it -- only whether density/counting alone
  is sufficient.
- Does not test `kappa(V)` (eigenvector conditioning) directly, the
  OTHER confound C118's skeptic named -- a random non-normal matrix's
  own conditioning is not controlled for or measured here, only
  implicitly present in whatever `s*` it produces.
- Does not change N_gen=3's CONDITIONAL status; does not touch S6/
  triality/OB1.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Reuse C118's own `find_critical_s` unmodified via direct import --
  no new statistical method, only new input matrices.
- Fixed random seed, recorded, for reproducibility.
- `ruff check` clean. Full pytest suite before commit.
- FL Step 8a skeptic pass on the result.
