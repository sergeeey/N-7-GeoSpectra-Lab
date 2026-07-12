---
experiment_id: 20260708-dolan-casimir-g2su3
round: 37
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round36 (explicitly isolated Ch_4's own c=1, resting on Round
  30's structural chain, as "the SOLE remaining gap for this whole
  [degree-4] story" — Round 30's chain cites 2 textbook Lie-theory
  facts (S2, S7) + has a back-solved case, k=8)
---

# claim.md — Round 37: closing BOTH of Round 30's remaining gaps —
(S2)'s citation AND the k=8 back-solve caveat

## Background

User chose this scope explicitly (of 4 offered candidates for Round 37,
the recommended option): "Закрыть Ch_4's c=1 полностью" — fully close
the SOLE remaining gap Round 36 isolated for the entire degree-4 story.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — a direct linear-algebra verification,
computed exactly at every step. NOT empirical, NOT causal.

## Core argument

1. **[VERIFIED, STEP A]** Built the FULL adjoint action `ad(nu_i)`,
   `i=1..14`, as `14×14` matrices in the `{nu_1,...,nu_14}` basis, via
   matrix commutators `[nu_i,nu_j]` decomposed back into the `g2` basis
   using `decompose_g2` — existing Round 13 machinery, never previously
   used to build the FULL 14×14 adjoint representation.
2. **[VERIFIED, STEP B, sanity check]** Each `ad(nu_i)` is
   antisymmetric in this basis (necessary consequence if an invariant
   form exists and this basis is orthonormal w.r.t. it).
3. **[VERIFIED, STEP C, the headline result]** Solved
   `ad(nu_i)ᵀQ + Q·ad(nu_i) = 0` for ALL `i=1..14` simultaneously, over
   symmetric `14×14` `Q` (105 free entries, 1362 nonzero linear
   equations after expansion) — the DEFINING condition for an
   `Ad(g2)`-invariant symmetric bilinear form. RESULT: the solution
   space is EXACTLY 1-dimensional, verified via `sympy.linsolve`'s own
   free-parameter count, not assumed.
4. **[VERIFIED, STEP D]** The unique (up to scale) solution, normalized,
   is EXACTLY the identity matrix in the `{nu_1,...,nu_14}` basis —
   i.e. EXACTLY `B_0` (Round 30's own trace form, already verified
   `B_0`-orthonormal in Round 30 STEPs A/B).
5. **Conclusion:** Round 30's `(S2)` — "g2 is SIMPLE ⟹ the space of
   `Ad(G2)`-invariant symmetric bilinear forms is exactly
   1-dimensional (Schur's lemma)" — previously CITED as a standard
   textbook Lie-theory fact — is now DIRECTLY VERIFIED for this
   project's own concrete 14-generator matrix realization, closing that
   citation with a project-specific computational proof.

**Second investigation (post-skeptic: FIXED into a real closure — see
STEP E):** attempted to ALSO close Round 30's other remaining caveat —
that `nu_8` (unlike `nu_1..nu_7`, verbatim page transcriptions) was
BACK-SOLVED from the SAME calibration equation Round 30's `S6'`
checks.

6. **First attempt (Approach A), VERIFIED VACUOUS:** re-derive `nu_8`
   as "the `B_0`-orthogonal complement of `span{nu_1..nu_7}` within
   `h=su(3)`." `B_0`-orthonormality of ALL of `{nu_1..nu_14}`
   (including `nu_8`'s own row/column) was ALREADY established USING
   `nu_8`'s own concrete matrix formula (Round 30 STEP A/B, full 196
   pairs) — circular.
7. **[VERIFIED, STEP E, post-skeptic fix]** Both FL Step 8a skeptics
   independently proposed, and this round then implemented and
   verified, a genuinely different, ALREADY-project-native Approach B
   ("bracket-closure"): `su(3)` has NO 7-dimensional subalgebra
   (standard classification: dims 0,1,2,3,4,8 only), so `{nu_1..nu_7}`
   (mutually `B_0`-orthonormal, `nu_8`-FREE, 28 pairs) CANNOT be
   bracket-closed. Computing all `C(7,2)=21` raw matrix commutators
   `[nu_i,nu_j]` and `B_0`-projecting each onto `span{nu_1..nu_7}`
   (using ONLY `i,j≤7`, `nu_8`-free) finds the escaping residual —
   EXACTLY 2 of 21 pairs escape (`(2,3)` and `(4,5)`, both
   `norm²=3/4`). Normalizing either gives a vector `hbar_8` that
   equals `nu_8` EXACTLY (up to overall sign) — a COMPLETE, independent
   re-derivation using ZERO reference to `nu_8`'s own formula.
   Cross-checked both escaping pairs agree, and verified
   `{nu_1..nu_7, hbar_8}` is genuinely bracket-closed (a real Lie
   subalgebra).
8. **Conclusion:** the `k=8` back-solve caveat is now FULLY CLOSED.
   Round 34's octonion route (originally flagged in this round's first
   version as "necessary") was NEVER needed for this — an overclaim,
   caught by both FL Step 8a skeptics independently and fixed here.

## Construction (code: `g2su3_round37_invariant_form_uniqueness.py`)

**STEP A:** build `ad(nu_i)` for all 14 generators as `14×14` matrices.

**STEP B:** sanity-check antisymmetry.

**STEP C:** solve the invariance linear system; verify the solution
space is 1-dimensional.

**STEP D:** normalize and verify the solution equals `B_0` exactly.

**STEP E (post-skeptic fix):** independently re-derive `nu_8` from
`nu_1..nu_7` alone via bracket-closure; verify it matches Appendix A's
`nu_8` exactly and that the resulting subalgebra is genuinely
bracket-closed.

## Falsifiable Claims

**C1 (the headline result):** the space of `Ad(g2)`-invariant symmetric
bilinear forms, for Appendix A's own 14-generator matrix realization,
is EXACTLY 1-dimensional.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).

**C2:** the unique (normalized) solution equals `B_0` (the identity
matrix in the `{nu_k}` basis) exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

**C3 (fixed, post-skeptic):** `nu_8` is independently re-derivable from
`nu_1..nu_7` alone via bracket-closure, matching Appendix A's `nu_8`
exactly, with zero reference to its own formula.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP E):
`nu_1..nu_7` mutually `B_0`-orthonormal (nu_8-free), exactly 2 of 21
commutators escape `span{nu_1..nu_7}`, both agree up to sign, the
normalized residual equals `nu_8` exactly, and `{nu_1..nu_7, hbar_8}`
is genuinely bracket-closed.

## Kill Conditions

- C1 killed if: skeptic finds the linear system in STEP C is set up
  incorrectly (e.g. `ad(nu_i)` built with a wrong sign/ordering
  convention for the commutator, or `decompose_g2` misapplied), or that
  `linsolve`'s free-parameter count is not a reliable way to determine
  solution-space dimension (verify by independently checking the rank
  of the coefficient matrix of the linear system).
- C2 killed if: skeptic finds the normalization step or the
  `Qconcrete == sp.eye(N)` comparison is flawed (e.g. comparing after
  an incorrect substitution).
- C3 killed if: skeptic finds `hbar_8` does NOT actually match `nu_8`
  (a sign/normalization bug), or that the bracket-closure check is
  performed incorrectly (e.g. `{nu_1..nu_7, hbar_8}` is NOT actually
  closed, meaning `hbar_8` is not really a full generator of `h`), or
  that the escaping-pair count is wrong (not exactly 2 of 21).

## What this does NOT mean

- Does NOT close Round 30's `(S7)` citation (uniqueness of the 8-dim
  irreducible Clifford module) — Round 30's own docstring already marks
  `S7` as "not independently load-bearing" for the `S9` conclusion, so
  it does not require closing.
- Does NOT change any previously-established numeric value from Rounds
  4-36 — this round only STRENGTHENS the justification for
  ALREADY-established facts (`Q=B_0`, and `nu_8`'s own value), using
  zero new primitive data.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension,
  the `M_p`/`Z_p` L4A convention question, `RHO`/`NU`'s literal
  AHL2023 "E_{a,b}" notation question (Round 34), or WHY Round 34's
  intertwiner `P` is Hadamard-type — all remain open, untouched by
  this round.
- **Original version of this claim.md/script overclaimed** that closing
  the `k=8` caveat would "require Round 34's octonion-native `g2=Der(O)`
  characterization... a separate, larger undertaking, not attempted
  this round." This was FALSIFIED by both FL Step 8a skeptics — the
  bracket-closure approach (STEP E) closes it directly, using only
  already-available project data, no octonion machinery needed. Fixed
  throughout (script, this claim.md).

## Skeptic Verdict (FL Step 8a — context-blind, claim.md + code only)

Two independent context-blind skeptics + a tool-verified synthesis
agent (Workflow tool, task `wup8mwo6w`) reviewed this round.

| Claim | Verdict | Note |
|---|---|---|
| C1 (invariant-form space is 1-dim) | `[CONFIRMED-REAL]` | Both skeptics independently verified the setup (Lie-closure of `g2` rules out `decompose_g2` truncation; `ad(X)ᵀQ+Qad(X)=0` is the standard infinitesimal invariance condition). The synthesis agent went further: rebuilt the full 1362×105 coefficient matrix from scratch via a DIFFERENT code path (`sp.diff` extraction, not `linsolve`'s internal machinery) and independently computed `rank=104` ⟹ `nullity=1` — an algorithmically distinct cross-check neither skeptic executed, closing the one residual `[NEEDS-REAL-DATA]` gap both skeptics flagged. |
| C2 (unique solution = `B_0`) | `[CONFIRMED-REAL]` | Both skeptics hand-verified the normalization logic; synthesis independently extracted the nullspace basis via `A.nullspace()` (a third, distinct code path) and confirmed exact structural equality to the identity, regardless of which symbol the original script happened to pick as free. |
| C3 (original: "orthogonal complement is vacuous, Round 34 needed") | `[FALSIFIED — then FIXED]` | **The central finding of this review.** Both skeptics, independently, proposed the SAME counter-approach (bracket-closure of `nu_1..nu_7`, using the standard fact that `su(3)` has no 7-dim subalgebra). The synthesis agent implemented it from scratch and found `hbar_8 == -nu_8` EXACTLY, plus verified genuine bracket-closure of the resulting subalgebra (a robustness check neither skeptic's argument-only treatment included). This is a textbook example of why FL Step 8a's context asymmetry works: a claim marked `[VERIFIED-tool]` for a REASONING-only argument (no in-script assertion backing it) was exactly the kind of gap two independent adversarial reviews are meant to catch — and did. **Fixed**: implemented as new STEP E, re-verified independently by me (not just trusted from the agent reports) before accepting. |

**Decision: PROMOTE.** C1/C2 were correct from the start. C3 was
genuinely wrong as originally written (an avoidable overclaim, not a
math error in the core result) — and the fix makes Round 37 stronger
than originally submitted: it now closes BOTH of Round 30's remaining
gaps, not just one. Per this project's own `integrity.md`: a
reasoning-only claim marked `[VERIFIED-tool]` without a computational
assertion behind it is exactly the failure mode this round
demonstrates in miniature — now corrected to carry a real, in-script
`[VERIFIED-tool]` assertion (STEP E) instead.
