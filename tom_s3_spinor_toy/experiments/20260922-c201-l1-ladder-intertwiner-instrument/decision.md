# C201 Decision — McMurry 6.3(a) tool-verified; T_i U = U L_i intertwiner test pre-validated on a known case

**Date:** 2026-09-22
**Verdict: PROMOTE, narrowly scoped.** Both pre-registered claims confirmed by
exact symbolic computation (`sympy`), zero approximation. One real bug was
caught and fixed during the run (see below) — a hand-typed Cartesian generator
had a sign error, diagnosed correctly as a bad control, not a physics
disagreement.

**Scope correction (added after review):** everything below is established
for the CONTROL l=1 case only. Nothing here establishes irreducibility or
representation-equivalence of any object in Tom Lawrence's own construction —
this round is instrument calibration on a known sample, not a finding about
his unseen (123)-(125). See "Scope, follow-ups, parked checks" below.

## Results

**Part 1 — McMurry 6.3(a).** All six ladder relations for l=1 hold exactly,
`[VERIFIED-tool]`:

```
L+ Y(1,-1) = sqrt(2) Y(1,0)     L- Y(1,1)  = sqrt(2) Y(1,0)
L+ Y(1,0)  = sqrt(2) Y(1,1)     L- Y(1,0)  = sqrt(2) Y(1,-1)
L+ Y(1,1)  = 0                  L- Y(1,-1) = 0
```

using ONLY McMurry's own stated definitions (`L±` from p.144, `Y_lm` from
(4.45), `P_1^0=cos(theta)`, `P_1^1=sin(theta)` from Table B1, p.91) — no
reference to Tom's own operators or conventions. This upgrades the earlier
hand-derivation (previous session) from `[INFERRED]` to `[VERIFIED-tool]` and
confirms McMurry is internally consistent: **the coefficient is sqrt(2)
throughout, no exceptions, no hidden factor.**

**Part 2 — 3x3 matrix form.** `L+`, `L-`, `Lz` built directly from Part 1's
relations; `Lx=(L++L-)/2`, `Ly=(L+-L-)/(2i)` satisfy the standard so(3) algebra
(`[Lx,Ly]=iLz` etc.) and Casimir `Lx^2+Ly^2+Lz^2=2*I` (matching `l(l+1)=2` for
l=1) exactly, symbolically.

**Part 3 — positive control for the intertwiner test.** First run FAILED
(`Cartesian generators satisfy so(3) algebra: False`) because the Cartesian
generators were typed from memory with a sign error. Per this project's own
"audit the check first" convention: since Part 2 had *already independently
verified* the spherical-harmonic-derived `Lx,Ly,Lz` satisfy the correct algebra,
the failure could not be a physics disagreement — it had to be in the freshly
introduced Cartesian side. Fixed by deriving the Cartesian generators the same
way as `L±` (by actual differentiation, `L_k = -i*epsilon_kij*x_i*d/dx_j` on the
coordinate functions themselves, not by typing a remembered matrix) rather than
patching the sign by eye. Re-run: Cartesian algebra now holds; an invertible
intertwiner `U` was found solving `T_z U = U L_z` and `T_x U = U L_x`
simultaneously, and — checked independently, not assumed — the SAME `U` also
solves `T_y U = U L_y` (the third generator, not used to find `U`). **Verdict:
EQUIVALENT_REPRESENTATIONS** — l=1 spherical harmonics and the Cartesian vector
representation of so(3) are confirmed the same representation up to basis
change, via the exact `T_i U = U L_i` test the correspondence-prep session
proposed, not by eyeballing matrix similarity.

**Part 4 — irreducibility template.** The commutant of `{Lx,Ly,Lz}` on the l=1
space has exactly 1 free parameter (scalar multiples of the identity) —
Schur's lemma confirms l=1 is genuinely irreducible under this generator set,
computed rather than assumed. This is the worked template for the
"invariant does not imply irreducible" caution raised in the correspondence
review: here is what actually checking it looks like.

## Self-caught bug (honesty note)

The first version of Part 3 asserted Cartesian `so(3)` generators
`(J_i)_{jk} = -epsilon_{ijk}` from memory and got a sign wrong, which the
script's own `[Lx,Ly]=i*Lz` assertion caught immediately (`False`). This is
recorded, not silently fixed, because it is a direct, small-scale illustration
of exactly the discipline this correspondence-prep round is built around: a
failing control must be diagnosed as a possibly-bad control before it is read
as a physics finding (`feedback-failing-check-audit-the-check-first`,
`~/.claude/memory`) — here the diagnosis was fast because Part 2 had already
independently pinned down that the spherical side was correct.

## What this means for the Tom Lawrence correspondence

1. The `sqrt(2)` result (Part 1) can be reported to Tom as tool-verified, not
   hand-derived — same content as before, higher evidence tier.
2. The `T_i U = U L_i` methodology (proposed in the correspondence review) is
   now a **validated instrument**: run on a case with a known answer (l=1
   spherical vs Cartesian), it correctly reports EQUIVALENT_REPRESENTATIONS,
   with an independent cross-check (the third generator) rather than trusting
   the two equations used to solve for `U`. When Tom's own (123)-(125) arrive,
   the identical script pattern (build his 3x3 matrices, solve for `U` against
   TWO of the three generators, verify the THIRD independently) can be reused
   directly — this is the same `hom_basis`/nullspace-intertwiner pattern
   already used in `C72`/`C199`/`C200`, just specialized to a 3-dimensional
   case.
3. Confirms the three-way outcome space the correspondence review named is
   real and distinguishable: `intertwiner_found + independently confirmed` =
   equivalent representations; `intertwiner_found` on the two solved-for
   generators only (no independent third-generator check, or it fails) = a
   spurious/partial solution, not genuine equivalence; no solution at all =
   `Hom=0`, no relation. This script demonstrates all three states are
   mechanically distinguishable, not just conceptually.

## What this does NOT mean

1. Does NOT depend on or unblock Tom's own "notes sent 7 September" — those
   remain unavailable; nothing here uses his equations.
2. Does NOT constitute, and is not intended as, a reply to Tom — purely
   internal tooling validation, per the correspondence review's own guidance
   not to send a "we found the error" message.
3. Does NOT touch this project's own G2/SU(3)/Spin(8) triality-channel
   physics (OB1, N_gen=3) — unrelated substrate (l=1 of so(3), not S3xS6).

## Scope, follow-ups, parked checks (added after review)

**The Part 3 FAIL was a genuine, unplanned negative control, not a designed
one.** It is real evidence the pipeline can say "no" to an inconsistent input
(caught its own sign error via the algebra assertion, before any equivalence
claim was made) — stronger than a test that only ever confirms formulas it was
itself built from. But it was an accident, not pre-registered as a negative
control, and should not be cited as if it were a deliberately engineered one.

**Pre-registered outcome space for when Tom's real (123)-(125) arrive**
(decision tree, not yet run against real data):

| Result of `T_i^Tom U = U L_i` | Reading |
|---|---|
| `T_i^Tom` itself fails `[Tx,Ty]=iTz` etc. | Cannot conclude anything about equivalence yet -- audit normalization, sign, `i` factors, and basis ORDER of his matrices first (this is a check on the input, same discipline as Part 3's own bug) |
| Nondegenerate `U` found, independently confirmed on the held-out third generator | Same `j=1` representation as ours, in a different basis/convention -- not representation-theoretic novelty, but not an error either |
| Only degenerate (non-invertible) intertwiners exist | Partial shared content, not full equivalence |
| `Hom=0` (no intertwiner at all), both sides independently passing their own algebra check | Genuinely different representation-theoretic objects |

**Two checks parked, NOT run in this round (no new round needed to add them
later):**

1. **Deliberate negative control.** Add a permanent unit test that injects a
   wrong sign/coefficient into one generator and asserts the equivalence gate
   rejects it -- converts Part 3's accidental FAIL into a designed one.
2. **Full-rotation element `U(2*pi)`.** The intertwiner/Hom test only checks
   whether two representations are the SAME dimension-3 object; it does not
   distinguish integer spin from genuine half-integer (spinorial, doubly-valued
   under SO(3)) content, which is the actual physical question behind Tom's
   "spinor multiplet" argument. The discriminator is exact and already
   confirmed on our own control: with `Lz=diag(1,0,-1)`,
   `U(2*pi)=exp(-2*pi*i*Lz)=diag(1,1,1)=+I` exactly (integer eigenvalues make
   this immediate, not requiring a fresh script) -- confirming l=1 is
   integer-spin, as it must be. A genuine half-integer representation would give
   `U(2*pi)=-I`, `U(4*pi)=+I`. **Trigger for building this as its own
   instrument (with its own known-case positive control on spin-1/2 Pauli
   generators, giving `U(2*pi)=-I`, before pointing it at Tom's object):**
   only once Tom's own multiplet is specified concretely enough to build its
   rotation operator, not before.

## Reproduction

```bash
cd tom_s3_spinor_toy/experiments/20260922-c201-l1-ladder-intertwiner-instrument
python c201_l1_ladder_intertwiner.py
```
No randomness, no numeric tolerance — every check is exact symbolic equality.
