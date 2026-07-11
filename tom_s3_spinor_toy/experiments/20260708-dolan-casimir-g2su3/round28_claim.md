---
experiment_id: 20260708-dolan-casimir-g2su3
round: 28
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C3_confirmed_C2_naming_fixed_C4-C5_circularity_fixed
parent: round27 (Dslash_mat=-H/2 exact identity, awaiting skeptic review in parallel)
---

# claim.md — Round 28: proving Round 26/27's correction coefficients are
UNIQUE (not fitted) via SU(3)-Schur + Hodge-duality symmetry

## Background

User (explicit methodological critique, in Russian) objected to Round
26/27 treating `H - (1/2)Id - (7/4)Casimir_su3` as verified-by-matching
rather than derived-from-first-principles, and proposed the correct
order: FIRST prove the space of admissible corrections is low-
dimensional (via SU(3)-equivariance + Clifford-algebra structure), THEN
derive the coefficients — not the reverse. This round executes exactly
that first step, rigorously, and shows it determines the coefficients
via a well-posed linear system rather than an 8×8 eyeball-match.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — representation-theoretic uniqueness
argument (Schur's lemma + an explicit symmetry), tested computationally.
NOT empirical, NOT causal.

## Construction (code: `g2su3_round28_coefficient_uniqueness.py`)

**Step 1a-1b (the priority per the user's critique):** Σ=Λ*(ℂ³)
decomposes under SU(3) as `1⊕3⊕3̄⊕1` (degrees 0,1,2,3). By Schur's
lemma, any SU(3)-equivariant Hermitian operator on Σ is forced scalar
on the single copies of `3`/`3̄` (zero between them, inequivalent
irreps), and an arbitrary Hermitian 2×2 matrix on the 2-dim trivial-
multiplicity space `{0,7}` — 6 real parameters. An additional involution
— a duality pairing degree `k` ↔ degree `3-k` (index pairs
`(0,7),(1,6),(2,5),(3,4)`, `Swap`) — is verified (not assumed) to commute
with `-ΣM_p²`, `H`, and `Casimir_SU(3)` independently. Requiring
commutation with `Swap` too collapses the 6-parameter space to exactly
**3**. **(REVISED post-skeptic:** this is NOT claimed to be the
canonical Hodge-star — the standard Hodge-star on Λ*(ℂ³) has signs
`(+,-,+,+)`, not this file's `(+,+,+,+)`. Verified directly that the
sign pattern is NOT privileged: an alternating-sign variant collapses
the space identically — the PAIRING structure does the constraining
work, not the specific signs.)**

**Step 1c:** `{Id, Casimir_SU(3), H}` are shown linearly independent
inside this 3-dim space via a nonzero 3×3 determinant (using 3
independent matrix-entry coordinates, not a full 64-entry comparison) —
hence a **basis**. Any operator meeting the Step 1a-1b constraints is
therefore a UNIQUE combination of these three.

**Step 2:** `Diff` (Round 26/27's actual `M_p`-vs-`Z_p` correction) is
verified to commute with `Swap` (i.e. genuinely lies in the proven 3-dim
space), then its coefficients are obtained by solving a DETERMINED 3×3
linear system (3 equations, 3 unknowns) using 3 independent matrix
entries — not by comparing all 64 entries and noticing a match.

**Step 3:** the solved coefficients are used to reconstruct the FULL 8×8
`Diff` matrix, confirmed to match exactly — verifying no information was
lost by reducing to 3 coordinates.

## Falsifiable Claims

**C1:** `-ΣM_p²`, `H`, `Casimir_SU(3)` are each genuinely SU(3)-
equivariant (commute with all 8 su(3) generators).

RESULT: `[VERIFIED-tool]` — all three confirmed, asserted in-script.

**C2 (REVISED post-skeptic — see "Skeptic Verdict" below):** The `Swap`
involution (`+1`-sign pairing) satisfies `Swap²=Id` and commutes with
all three objects in C1.

RESULT: `[VERIFIED-tool]` — confirmed exactly for all three, asserted.
**Downgraded**: this was originally framed as "the Hodge-star duality"
and the `+1`-sign choice was implied to be meaningful. Both skeptics,
and an independent tool-verified symbolic test (16 sign patterns × 3
different `3↔3̄` bijections), confirmed this is WRONG — the standard
Hodge-star has signs `(+,-,+,+)`, and EVERY tested sign/bijection
variant collapses the space identically. The real content of C2 is:
**a** duality-type involution with this PAIRING structure exists and
commutes with `H`/`Casimir`/`-ΣM_p²` — not that this specific `Swap` is
canonical or privileged. The structural conclusion (3-dim space) is
unaffected; only the naming/emphasis was wrong.

**C3 (the structural theorem — the actual answer to "why 3-dimensional"):**
`{Id, Casimir_SU(3), H}` are linearly independent (nonzero 3×3
determinant `= -8√3/3`), hence form a basis of the Schur+Swap-
constrained space.

RESULT: `[VERIFIED-tool]` — confirmed exactly, asserted.

**C4 (REWRITTEN post-skeptic — the original version was FALSIFIED, a
real circularity, not a naming issue):** `Diff` commutes with `Swap`
(lies in the proven space), and the resulting DETERMINED 3×3 linear
system yields exactly `(a,b,c) = (1, -1/2, -7/4)`.

**Original bug**: the first version of this claim/code DEFINED `Diff :=
H - (1/2)Id - (7/4)Casimir_su3` DIRECTLY using the target coefficients,
then "solved" a system that was mathematically guaranteed to return
exactly those numbers back — a pure tautology. Both skeptics caught
this independently ("the code never independently constructs Diff from
the Mp/Zp machinery — it writes the target formula directly").

RESULT (post-fix): `[VERIFIED-tool]` — `Diff` is now rebuilt in
`build_diff_noncircular` from Round 26/27's ACTUAL pipeline (`Ch_tilde`,
`degree4_term`, `scalar_term` — built from `curv_h`/T-table only, zero
`M_p` dependence — combined via Round 27's `H²/4`-based route for
`Ω_g`), with ZERO reference to the target formula anywhere. Solving the
resulting genuine 3×3 system NOW gives `(1,-1/2,-7/4)` as an actual
result, not an assumed one — re-verified in-script.

**C5 (same fix applies):** the solved `(a,b,c)` reconstruct the
INDEPENDENTLY-REBUILT `Diff` exactly over the FULL 8×8 matrix.

RESULT: `[VERIFIED-tool]` — confirmed exactly, asserted. No longer
tautological now that C4's `Diff` is genuinely, independently computed.

## Kill Conditions

- C1/C2's ORIGINAL kill condition (below, struck through) was INVERTED —
  discovered by both skeptics AND independently confirmed by a
  tool-verified symbolic test (16 sign patterns, 3 bijections): the
  alternative sign patterns DO commute, harmlessly, with all three
  objects. This does NOT kill C1-C3's structural conclusion (the 3-dim
  space is real) — it only kills the claim that the `+1`-sign choice or
  "Hodge-star" naming was meaningful. ~~C1/C2 killed if: skeptic finds
  `Swap` is NOT actually the standard Hodge-star operator, or that its
  commutation... is a coincidence of THIS specific sign choice... skeptic
  should try at least one alternative sign pattern... and confirm it does
  NOT commute.~~ (This is what actually happened, and it does NOT kill
  C1-C3 — see Skeptic Verdict below for the corrected reading.)
- C3 killed if: skeptic finds the determinant computation uses a
  DEPENDENT (not independent) set of coordinates, or that a 4th natural
  SU(3)-equivariant+Swap-symmetric object exists that `{Id,Casimir,H}`
  cannot reach (would mean the space is NOT actually spanned by just
  these three, even if 3-dimensional by coincidence of the SPECIFIC
  count — skeptic should check whether a genuinely different operator,
  e.g. `H²`'s own degree-4 part alone, also lies in this space and
  whether it's independent of `{Id,Casimir,H}` or expressible in terms
  of them).
- C4/C5's ORIGINAL kill condition (checking whether C5 is tautological
  given C3+C4) correctly anticipated HALF the problem but missed the
  deeper one: C4 ITSELF was circular (`Diff` was defined as the target
  formula), not just C5. Both skeptics found this independently, from
  code inspection alone. Fixed — see C4/C5 above and Skeptic Verdict
  below.

## What this does NOT mean

- Does NOT derive the coefficients `1, -1/2, -7/4` WITHOUT ever
  computing `Diff` — `Diff` is still built from the already-established
  `M_p`/`Z_p` machinery (Rounds 24-27). What is newly proven is that,
  GIVEN `Diff` lies in this space (itself now proven, not assumed), its
  coefficients are UNIQUELY forced — a genuine rigidity/uniqueness
  result, one level short of a full from-scratch symbolic derivation.
- Does NOT explain WHY `Diff` lies in the 3-dim space in the first place
  from an even deeper principle (i.e. WHY `M_p-Z_p`'s squared-sum is
  built only from degree ≤3, SU(3)-invariant, Swap-symmetric Clifford
  data) — this is highly plausible given the general theory (Agricola's
  own Theorem 3.2 only ever produces degree ≤4 Clifford elements plus
  scalars), but not independently re-derived here from that theorem.
- Does NOT supply the full "expand `M_p`, `Z_p` via the Nomizu formula
  and watch the coefficients fall out of Jacobi identities" derivation
  the user's critique ultimately asks for (Phase 2 in their own
  framing) — flagged explicitly as the next, deeper step, requiring
  essentially specializing Agricola 2002's own Theorem 3.2 proof
  technique to isolate the `M_p`-vs-`Z_p` piece specifically.
- Does NOT change any previously-established spectrum, index, or
  eigenvalue result — this round is a structural/uniqueness argument
  about an already-existing, unchanged quantity.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics + a tool-verified synthesis pass that independently re-ran the
code AND independently symbolically tested the load-bearing structural
question)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both) | equivariance checks are real, structural |
| C2 | WEAKENED (both) → naming/framing fixed | "Hodge-star" claim wrong (real Hodge-star has signs `(+,-,+,+)`); "+1-sign privileged" claim wrong — ANY sign pattern with the same pairing works. Does NOT affect C1/C3's structural conclusion. |
| C3 | CONFIRMED-REAL (both, + independently re-confirmed by the synthesis agent's own symbolic test across 16 sign patterns × 3 bijections × 1 degenerate pairing) | the genuinely real result of this round: the 3-dim space and `{Id,Casimir,H}` basis are correctly derived |
| C4 | **FALSIFIED (both)** → real circularity found and fixed | `Diff` was defined directly as the target formula in the original code; the "solve" was mathematically guaranteed to return the coefficients it was given. Rebuilt non-circularly from `curv_h`/T-table via Round 27's own pipeline; genuinely re-solves to `(1,-1/2,-7/4)` now. |
| C5 | FALSIFIED (both, same root cause as C4) → fixed alongside C4 | no longer tautological once C4's `Diff` is genuine |

**Synthesis agent's own independent verification** (not just relaying
the two skeptics): built a generic 6-parameter Schur-admissible
Hermitian operator symbolically and tested `[M, Swap]=0` against 16 sign
variants, 3 different `3↔3̄` bijections, and 1 degenerate pairing — EVERY
variant produced the identical 3 constraints (`a=d`, `c` real, `λ=μ`),
confirming the "duality collapses 6→3" claim is genuinely structural,
not an artifact of this round's specific `Swap` choice.

**Overall**: the round's real content (C1, C3 — a genuine, non-trivial
representation-theoretic rigidity theorem answering the "prove low-
dimensionality first" part of the user's critique) survives intact and
independently re-confirmed. What did NOT survive as originally stated:
the "Hodge-star" naming (C2, cosmetic) and — more seriously — the claim
that Round 26/27's coefficients were shown unique via a genuine
computation (C4/C5, a real circularity, now fixed). Per FL's response
matrix: FALSIFIED ≠ KILLED — a viable fix existed (rebuild `Diff`
non-circularly) and was applied; the round is promotable in its
corrected form.
