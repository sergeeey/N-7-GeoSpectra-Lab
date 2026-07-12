---
experiment_id: 20260708-dolan-casimir-g2su3
round: 35
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round33 (explicitly flagged, "What this does NOT mean": "Does
  NOT explain the SPECIFIC numeric value of the proportionality
  constant c ... that still requires the direct combinatorial
  computation from Rounds 26/29/31/32. This round explains the SUPPORT
  ..., not the VALUE.") — carried unchanged through Round 34.
---

# claim.md — Round 35: deriving Ch_4's c=1 structurally, reducing
degree4_term's c'=-5/4 to one atomic fact

## Background

User chose this scope explicitly (of 4 offered candidates for Round 35,
the recommended option): "Вывести конкретное значение c=1" — derive the
specific numeric value of the proportionality constant `c` that Round
33 explicitly left unexplained.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — algebraic re-derivation using already-
established structural facts, verified computationally at every step.
NOT empirical, NOT causal.

## Core argument

**Part 1 — Ch_4's `c=1` is a logical consequence of 3 already-established
structural facts (not a fresh combinatorial solve on Ch_4 itself):**

1. **[Round 26, structural]** `Ch_0 = Tr(Ch_tilde)/8` — `Ch_4` is pure
   degree-4 by construction, hence traceless; this is a DEGREE fact,
   not a computation.
2. **[Round 30, structural, PRIOR to and INDEPENDENT of Ch_4's own
   value]** `Ch_tilde = Casimir_su3` EXACTLY — Agricola's own definition
   of `C̃h` (Prop 3.3) is literally the `su(3)` Casimir operator for a
   `Qh`-orthonormal basis. This is an identity between two OPERATOR
   DEFINITIONS, established without ever looking at `Ch_4`'s numeric
   value.
3. **[Round 29/33, structural]** `Casimir_su3 = Id + X/3` where
   `X:=Z1234+Z1256+Z3456` is a genuine degree-4 Clifford element, hence
   traceless by construction — so `Tr(Casimir_su3)/8 = 1`.
4. **Combine:** `Ch_0 = Tr(Ch_tilde)/8 = Tr(Casimir_su3)/8 = 1`, hence
   `Ch_4 = Ch_tilde − Ch_0·Id = Casimir_su3 − Id = 1·(Casimir_su3−Id)`.
   `c=1` FOLLOWS from steps 1-3; it is not separately solved for.

**Correction to Round 33's own framing:** Round 33's STEP D used the
SOLVED `c=1` (from its own combinatorial 3×3 solve) to re-derive
`Ch_tilde=Casimir_su3` as a "bonus", and its own skeptic-reviewed
caveat already flagged this as plugging in a solved value, not a
structural derivation. This round shows the dependency actually runs
the OTHER way: `Ch_tilde=Casimir_su3` (Round 30) is prior and
independent; `c=1` is DERIVED from it (plus the two traceless facts),
not the reverse.

**FL Step 8a caveat (both skeptics + synthesis, CONFIRMED-REAL but
framing WEAKENED):** the in-script demonstration of steps 1-4 (STEP C
in the code) is MECHANICALLY TAUTOLOGICAL with STEP A's own check —
`Ch_tilde` is *defined* there as `Ch_0·Id+Ch_4`, and since `Ch_4` is
traceless, re-computing `Ch_0` as `Tr(Ch_tilde)/8` collapses right back
to the same number, adding zero fresh in-code evidence. This does NOT
falsify the claim: both skeptics independently verified that Round
30's own structural chain (its STEPs A-D, NOT its STEP E "sanity
cross-check") never references `Ch_4` anywhere — so the dependency
direction claimed here is real at the mathematical level. But the
independence rests entirely on TRUSTING Round 30's own chain (which
itself cites 2 textbook Lie-theory facts and back-solves one case,
`k=8`), not on any fresh numerical evidence Round 35 itself
contributes. The synthesis agent additionally found: `Ch_0=1` was
ALREADY directly computable since Round 26 (plain `Qh_sum=8`
summation) — what is genuinely NEW here is a SECOND, independent route
to the same number (via `Casimir_su3=Id+X/3`, pure degree-counting, no
`curv_h` summation needed), not the discovery of a previously-unknown
value.

**Part 2 — degree4_term's `c'=-5/4` is RELOCATED, not reduced in
solve-count:**

5. **[NEW, this round]** `degree4_term = Ch_4 − (9/8)·Jm4` exactly,
   where `Jm4` is the quartic matrix built PURELY from `jac_m` (Round
   26's m-part Jacobiator, T-table only, `curv_h`-independent) — a
   clean algebraic decomposition not previously stated explicitly.
6. **[VERIFIED]** `Jm4` satisfies the SAME three premises Round 28's
   theorem needs (SU(3)-equivariant, Swap-symmetric, Hermitian) AND is
   traceless (pure degree-4 by construction) — so it is ALSO forced
   into `span{Casimir_su3−Id}` by Round 33's own degree-counting
   argument, applied here to a genuinely new object Round 33 never
   considered.
7. **[VERIFIED, still a combinatorial solve, NOT structurally derived]**
   Solving gives `Jm4 = 2·(Casimir_su3−Id)` exactly (`d=2`).
8. **Combine:** `c' = c(Ch_4) − (9/8)·d(Jm4) = 1 − (9/8)·2 = −5/4`,
   matching Round 26/31's independently-computed value EXACTLY.

**FL Step 8a caveat (both skeptics + synthesis, CONFIRMED-REAL but
framing WEAKENED):** the original framing ("REDUCING... to the
strictly simpler... question") overstated the progress. The SAME
combinatorial 3×3 solve is still performed — it is RELOCATED from
`degree4_term` (which mixes `curv_h`+`jac_m`) onto `Jm4` (`curv_h`-
independent only), not eliminated or reduced in count. The object
solved is genuinely cleaner (one fewer input table), which is real,
honest progress — but "why is degree4_term's coefficient −5/4" is not
answered with less combinatorial work, only with a different, more
isolated question ("why is `Jm4`'s own coefficient exactly 2"). `d=2`
itself is not derived from a deeper principle here.

## Construction (code: `g2su3_round35_derive_c_value.py`)

**STEP A:** re-verify `Ch_tilde=Casimir_su3` (Round 30's finding,
re-confirmed here).

**STEP B:** re-verify `Tr(Casimir_su3)/8=1` via `Casimir_su3=Id+X/3`,
`X` traceless.

**STEP C:** derive `Ch_4`'s `c=1` algebraically from STEP A + STEP B,
without solving Round 28's 3×3 system for `Ch_4` at all.

**STEP D:** verify the new decomposition `degree4_term=Ch_4−(9/8)·Jm4`.

**STEP E:** verify `Jm4` satisfies Round 28's theorem premises
(equivariance, Swap-symmetry, Hermiticity, tracelessness).

**STEP F:** solve Round 28's 3×3 system for `Jm4`'s own `(a,b,c)`
coordinates — `a=0` (degree-counting), `d:=c=2`.

**STEP G:** algebraically reconstruct `degree4_term`'s `c'=-5/4` from
`c=1` (STEP C) and `d=2` (STEP F), without solving Round 28's 3×3
system for `degree4_term` itself.

## Falsifiable Claims

**C1:** `Ch_tilde=Casimir_su3` exactly (re-confirming Round 30).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2:** `Tr(Casimir_su3)/8=1`, via `Casimir_su3=Id+X/3` with `X`
traceless.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3 (headline #1):** `Ch_4 = Casimir_su3 − Ch_0·Id` with `Ch_0`
derived (not solved) as `1`, giving `c=1` structurally.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).

**C4:** `degree4_term = Ch_4 − (9/8)·Jm4` exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

**C5:** `Jm4` satisfies Round 28's theorem premises and solves to
`Jm4=2·(Casimir_su3−Id)` exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEPs E-F).

**C6 (headline #2):** `degree4_term`'s `c'=-5/4` reproduced
algebraically from `c=1` and `d=2`, without an independent 3×3 solve
for `degree4_term` itself.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP G).

## Kill Conditions

- C1/C2 killed if: skeptic finds either re-verification (already
  established Rounds 29/30) fails to reproduce under direct re-run —
  would mean a regression in already-promoted facts, not a new finding.
- C3 killed if: skeptic finds the "Ch_0 derived, not solved" framing is
  misleading — i.e., that `Tr(Ch_tilde)/8=Ch_0` (Round 26) or
  `Ch_tilde=Casimir_su3` (Round 30) SECRETLY depends on `Ch_4`'s own
  numeric value somewhere in their own derivation chains (would break
  the claimed independence and reintroduce circularity).
- C4 killed if: skeptic finds `Jm4`'s definition does not actually
  match `jac_m`'s own formula as used inside `degree4_coeff` (Round
  26) — i.e., a transcription mismatch between this round's `jm_coeff`
  and Round 26's `degree4_coeff`'s own `jm` term.
- C5 killed if: skeptic finds `Jm4` does NOT actually satisfy
  equivariance/Swap-symmetry/Hermiticity/tracelessness (would
  invalidate applying Round 28's theorem to it), or the 3×3 solve for
  `Jm4` is performed incorrectly (verify the reconstruction check
  independently).
- C6 killed if: skeptic finds the algebraic combination
  `c'=c−(9/8)·d` does not actually reproduce `degree4_term` exactly
  (i.e., STEP G's arithmetic or the STEP D decomposition it depends on
  is wrong).

## What this does NOT mean

- Does NOT derive `Jm4`'s own `d=2` from a deeper principle — that
  specific numeric fact still requires the SAME 3×3-solve-and-read-off
  method used throughout Rounds 26-33, just applied to a cleaner,
  `curv_h`-independent object. This is an honest, explicit gap, not
  glossed over.
- Does NOT change any previously-established numeric value from
  Rounds 4-34 — this round is a re-derivation/re-organization of
  ALREADY-established facts (Round 26/29/30/33), using zero new
  primitive data.
- Does NOT retract or falsify Round 33's own STEP D — that step's
  claim (`Ch_tilde=Casimir_su3` reproduced from `c=1`+`Ch_0=1`) is
  still numerically TRUE; this round shows the CORRECT direction the
  logical dependency runs, which Round 33's own skeptic-reviewed caveat
  already flagged as an open question, not a claimed derivation.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension,
  the `M_p`/`Z_p` L4A convention question, `RHO`/`NU`'s literal
  AHL2023 "E_{a,b}" notation question (Round 34), or WHY the Round 34
  intertwiner `P` is Hadamard-type — all remain open, untouched by
  this round.
- Does NOT mean STEP C (Ch_4's derivation) is an independent numerical
  check — it is mechanically tautological with STEP A, kept as a
  pedagogical walkthrough of the dependency chain (see the FL Step 8a
  caveat in Part 1). The genuine independence lives entirely in Round
  30's own structural chain, which this round trusts but does not
  re-derive from scratch.
- Does NOT mean degree4_term's `c'=-5/4` required LESS combinatorial
  computation than before — the same 3×3 solve is relocated onto a
  cleaner object (`Jm4`), not eliminated (see the FL Step 8a caveat in
  Part 2).

## Skeptic Verdict (FL Step 8a — context-blind, claim.md + code only)

Two independent context-blind skeptics + a tool-verified synthesis
agent (Workflow tool, task `w00lq6sgq`) reviewed this round, with
special attention to whether the `c=1` "structural derivation" is
genuinely non-circular. **Zero FALSIFIED claims** — all six survive,
but two real framing overclaims were found and fixed (not the
underlying algebra, which both skeptics + synthesis independently
hand-verified and/or re-ran to completion).

| Claim | Verdict | Note |
|---|---|---|
| C1 (`Ch_tilde=Casimir_su3` re-confirmed) | `[CONFIRMED-REAL]` | Both skeptics confirmed this reuses Round 30's identical construction; synthesis ran the script to completion, exit 0. |
| C2 (`Tr(Casimir_su3)/8=1`) | `[CONFIRMED-REAL]` | Matches Round 33 STEP A′ exactly; `X`'s tracelessness is a standard Clifford-grading fact (degree-4 element on 6 generators). |
| C3 (`Ch_4`'s `c=1`, "structurally derived") | `[CONFIRMED-REAL, framing WEAKENED]` | **The critical finding of this review.** Both skeptics independently identified that the in-script STEP C is mechanically tautological with STEP A (since `Ch_tilde` is *defined* as `Ch_0·Id+Ch_4`, and `Ch_4` is traceless, `Ch_0` recomputed via `Tr(Ch_tilde)/8` cannot help but reproduce itself). This does NOT falsify the claim — both skeptics separately verified Round 30's own structural chain (STEPs A-D, not its STEP E cross-check) never references `Ch_4` — so the claimed dependency direction is mathematically real. But "FULLY structurally derived, zero fresh combinatorial computation" overstated it: the independence rests on trusting Round 30's chain (2 cited textbook Lie-theory facts, one back-solved case `k=8`), and the synthesis agent found `Ch_0=1` was already directly computable since Round 26 via plain summation — the genuinely new content is a *second* route to the same number, not a previously-unknown fact. **Fixed**: docstring, STEP C's print statements, and this claim.md all reworded to "logical consequence... trusting Round 30's chain" instead of "fully derived." |
| C4 (`degree4_term=Ch_4−(9/8)·Jm4`) | `[CONFIRMED-REAL]` | Both skeptics hand-verified the arithmetic (`−1/2·9/4=−9/8`) and confirmed `build_quartic_matrix` is genuinely linear in its coefficient function (no hidden nonlinearity) — matches Round 26's `degree4_coeff` exactly, term-by-term. |
| C5 (`Jm4` premises + `Jm4=2·(Casimir_su3−Id)`) | `[CONFIRMED-REAL]` | Both skeptics confirmed the 3×3 solve is non-vacuous (genuine non-singular row selection, full 64-entry reconstruction check) and the four premises (equivariance/Swap/Hermiticity/tracelessness) are independently re-verified, not just inherited by assumption. |
| C6 (`c'=-5/4` reproduced from `c=1`+`d=2`) | `[CONFIRMED-REAL, "reduction" framing WEAKENED]` | Arithmetic confirmed correct by both skeptics + synthesis. But the "reduction to a simpler question" framing overstated the progress: the 3×3 solve is relocated (to `Jm4`), not eliminated — same solve count, cleaner object. **Fixed**: reworded throughout to "relocation, not reduction in solve-count." |

**Decision: PROMOTE.** All 6 claims (C1-C6) survive with corrected
framing. No math was wrong — every algebraic identity, arithmetic
computation, and non-vacuous check holds exactly, confirmed
independently by both skeptics and the synthesis agent (which
additionally ran the script to completion and performed standalone
re-derivations neither skeptic executed). The two WEAKENED findings
were about overstating HOW MUCH new evidence this round contributes
(a real, non-cosmetic distinction per this project's own Claim Scope
Discipline), not about any claim being false.
