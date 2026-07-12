---
experiment_id: 20260708-dolan-casimir-g2su3
round: 38
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted
parent: round37 (last of the degree-4/c-value sub-arc, Rounds 29-37);
  this round pivots to the older, preprint-relevant "8/45 vs ~1.03"
  L4A norm-bound tension (preprint.tex L560-607, flagged unresolved
  since Round 23, decision.md ~L4105-4279)
---

# claim.md — Round 38: Dslash_mat² in closed form via Casimir_su3
(a new synthesis, directly relevant to but not resolving L4A)

## Background

User: "го, round 38" (no specific candidate selected via AskUserQuestion
this time — proceeded with the recommended option per this session's
established pattern: the `8/45 vs ~1.03` norm-ratio tension, Rounds
23-26, the oldest and most preprint-consequential open item).

**Investigation first (research agent, no code changes):** Round 23's
own `decision.md` analysis (~L4204-4213) already TESTED and REJECTED a
pure `ρ_6`-normalization mismatch as sufficient explanation (curvature-
type quantities scale identically under uniform rescaling — the ~5.6×
gap survives that check). The better-evidenced root cause per Round
23's own Kill Analysis: `remainder := D64² − F_{S^-}` on the 2-dim
SU(3)-invariant subspace is NOT scalar (`[[17/6,5/3],[5,7/2]]`, trace
`19/3`), so there is no clean, independently-isolated `R/4 + ∇*∇` to
compare against — Round 23 explicitly flagged `∇*∇` as "NOT YET
independently isolated/verified" on the TWISTED `Gamma(S^+⊗S^-)`
bundle, with the SAME method (matrix-coefficient-section machinery)
flagged as the natural next step, NOT attempted there.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic synthesis, verified
computationally. NOT empirical, NOT causal.

## Core argument

1. **This round does NOT attempt the full twisted-bundle `∇*∇`
   isolation** — a separate, larger undertaking (Round 23's own object
   lives on a 16-dim bundle with genuine cross-terms between chirality
   factors; correctly isolating `∇*∇` there requires care this round
   does not risk in one pass).
2. **[VERIFIED, STEP A]** Re-confirmed Round 27's own operator identity
   `Dslash_mat = −(1/2)·H` (cited unchanged, load-bearing here).
3. **[VERIFIED, STEP B, the headline result]** `Dslash_mat² = 3·Id −
   (9/4)·Casimir_su3` EXACTLY — a NEW synthesis connecting Round 27
   (`Dslash=−(1/2)H`) + Round 29 (`H²=3·Id−3·X`) + this session's own
   `Casimir_su3=Id+X/3` (Rounds 29/33/37) for the FIRST TIME.
4. **[VERIFIED, STEP C, companion synthesis]** `Σ_p M_p² = −(1/2)·Id +
   (1/4)·Casimir_su3` EXACTLY — re-expresses Round 26's own
   `CASIMIR_L_plain:=−Σ M_p²` in closed form for the first time.
5. **[VERIFIED, STEP D]** Spectral consequence, cross-checked against
   direct matrix diagonalization (not merely derived abstractly):
   `Dslash_mat²` has spectrum `{3: mult 2, 0: mult 6}` — `Dslash_mat`
   itself has a 6-dimensional KERNEL exactly on the SU(3) `(3+3̄)`
   content of `Σ`, with eigenvalues `±√3` (never `0`) on the 2 SU(3)
   singlets.
6. **Conclusion:** Round 23's own `TERM1 = Dslash_mat⊗Id_{S^-}` is now
   fully closed-form (`TERM1² = [3·Id−(9/4)·Casimir_su3]⊗Id_{S^-}`) —
   a genuinely useful building block for a FUTURE attempt to isolate
   `∇*∇` on the twisted bundle (Round 23's own flagged next step). This
   round stops here — does not attempt that isolation, does not
   reconcile the `8/45 vs ~1` ratio, does not touch `preprint.tex`.

## Construction (code: `g2su3_round38_dslash_squared_closed_form.py`)

**STEP A:** re-verify Round 27's `Dslash_mat=−(1/2)·H`.

**STEP B:** verify `Dslash_mat²=3·Id−(9/4)·Casimir_su3` exactly.

**STEP C:** verify `Σ_p M_p²=−(1/2)·Id+(1/4)·Casimir_su3` exactly.

**STEP D:** cross-check the spectral consequence against direct matrix
diagonalization.

**STEP E (post-skeptic addition):** verify `Dslash_mat` is normal
(real-symmetric) and directly diagonalize it, confirming spectrum
`{√3:1, −√3:1, 0:6}` exactly — this is what actually licenses the
narrative jump from "`Dslash_mat²` has a 6-dim 0-eigenspace" to
"`Dslash_mat` itself has a 6-dim kernel" (`ker(A²)=ker(A)` requires `A`
normal). Added in response to FL Step 8a skeptic-2's `[WEAK]` flag —
see Skeptic Verdict below.

## Falsifiable Claims

**C1:** Round 27's `Dslash_mat=−(1/2)·H` re-verifies.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2 (the headline result):** `Dslash_mat²=3·Id−(9/4)·Casimir_su3`
exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3:** `Σ_p M_p²=−(1/2)·Id+(1/4)·Casimir_su3` exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).

**C4:** `Dslash_mat²` has spectrum `{3: mult 2, 0: mult 6}`, matching
BOTH the closed-form derivation AND direct matrix diagonalization.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

**C5 (added post-skeptic):** `Dslash_mat` itself (not merely its
square) is real-symmetric with exact spectrum `{√3:1, −√3:1, 0:6}`.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP E).

## Kill Conditions

- C2/C3 killed if: skeptic finds the coefficients in the closed-form
  expressions are wrong (verify the arithmetic chain: `H²=3Id−3X`
  (Round 29) + `X=3(Casimir_su3−Id)` (Round 29/33) ⟹ `H²=3Id−9Casimir_su3
  +9Id=12Id−9Casimir_su3` ⟹ `Dslash²=(1/4)H²=3Id−(9/4)Casimir_su3`; and
  `Σ M_p²` closed form similarly from `sumM2=−1/4Id+1/12X` (Round 29)).
- C4 killed if: skeptic finds the direct-matrix and closed-form spectra
  do NOT actually match (the script's own STEP D compares them
  directly, not just asserts one route).

## What this does NOT mean

- Does NOT isolate `∇*∇` on the twisted `Gamma(S^+⊗S^-)` bundle — the
  actual object Round 23's own L4A analysis needs. That remains a
  separate, larger undertaking (Round 23's own flagged next step),
  NOT attempted this round.
- Does NOT reconcile the preprint's `8/45` norm-bound estimate against
  the exact `~1` ratio Round 23 found — this round establishes upstream
  groundwork (a closed form for `TERM1²`), not a resolution.
- Does NOT touch `preprint.tex` — no claim in the paper is affected by
  this round.
- Does NOT change any previously-established numeric value from Rounds
  4-37 — `Dslash_mat²` and `Σ M_p²` already had these exact values
  (established via raw matrix computation since Rounds 4-26); this
  round provides a NEW, more insightful closed-form expression for
  ALREADY-known objects, not new numbers.
- Does NOT resolve the `M_p`/`Z_p` L4A convention question (Rounds
  23-26), `RHO`/`NU`'s literal AHL2023 "E_{a,b}" notation question
  (Round 34), or WHY Round 34's intertwiner `P` is Hadamard-type — all
  remain open, untouched by this round.
- Does NOT establish the `(9/4)`/`(1/4)` coefficients in C2/C3 under
  any OTHER SU(3)-generator normalization — they hold as exact matrix
  equations in this project's own fixed convention (inherited from
  Round 29's own explicit caveat: "verified numerical identity in THIS
  project's specific SU(3)-generator normalization... not proven
  normalization-independent"). Every downstream use in this project
  inherits the same convention automatically, so nothing is
  misrepresented — this is a scope-hygiene flag, not a numerical gap.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Edit/Write only, no Bash in their
environment) independently audited this round via direct file reads
of `round38_claim.md`, the script, and the two cited prior scripts
(Round 27, Round 29) — NOT via session history. A synthesis agent
(full tool access) then independently re-ran all three scripts and
resolved both flags.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (tool-verified) |
|---|---|---|---|
| C1 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (exit 0) |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (exit 0) |
| C3 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (exit 0) |
| C4 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (exit 0) |

**No FALSIFIED, no NEEDS-REAL-DATA, no smuggled citations** — both
skeptics independently traced every "already-established" fact
(Round 27's `Dslash=-(1/2)H`, Round 29's `H²=3Id-3X` and
`Σ M_p²=-1/4·Id+1/12·X`, `Casimir_su3=Id+X/3`) back to an actual
assertion in the cited round's own source file, not to Round 38's
own claim about them.

**Two minor flags raised, both resolved:**
1. **Skeptic 1** — the `(9/4)`/`(1/4)` coefficients silently inherit
   Round 29's own SU(3)-normalization caveat, not re-flagged in Round
   38's original "What this does NOT mean". **Response: Accepted as a
   documentation gap, not a numerical flaw** — added the explicit line
   above.
2. **Skeptic 2** — flagged `[WEAK]`: the narrative jump from
   "`Dslash_mat²` has a 6-dim 0-eigenspace" to "`Dslash_mat` itself has
   a 6-dim kernel, eigenvalues `±√3`" requires `Dslash_mat` to be
   *normal* (`ker(A²)=ker(A)` needs this), which the original script
   never checked. **Response: Fixed, not dismissed** — added STEP E
   (real-symmetry + direct diagonalization), independently re-verified
   by me (audit-verification-gate.md: agent's `[VERIFIED]` = my
   `[INFERRED]` until I re-run it myself) via a fresh script run
   (`EXIT=0`, `Dslash_mat symmetric? True`, spectrum
   `{-sqrt(3):1, sqrt(3):1, 0:6}` exactly). C5 added to Falsifiable
   Claims. Skeptic 2's `[WEAK]` is now `CONFIRMED-REAL`.

**Overall: PROMOTE.** All 5 claims (C1-C5) `[VERIFIED-tool]`, both
skeptic flags closed with genuine artifact-level fixes (not narrative
dismissals), synthesis agent found zero new issues beyond the two
already resolved.
