---
experiment_id: 20260708-dolan-casimir-g2su3
round: 45
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_rejected
parent: round44 (confirmed Agricola's Z_i is never a bivector
  connection operator, closing the M_p-vs-Z_p thread); this round
  pursues a DIRECT test of Round 24's own original (i)-vs-(ii) fork
  (frame/Leibniz correction vs incomplete F_{S^-}), per the user's own
  detailed, anti-circularity-constrained specification
---

# claim.md — Round 45: blind derivation test — the trace-free residual
K is exactly the standard Leibniz/torsion cross-term forced by D64's
own already-correct twisted-Dirac-operator structure

## Background

Round 24 (2026-07-10-ish) originally found `Delta_2x2 =
[[5/2,4/3],[4,5/2]]`, with its trace-average (diagonal) EXACTLY `5/2`
(the preprint's nominal `Scal/4`) and its trace-free residual `K :=
[[0,4/3],[4,0]]` left genuinely unexplained, framed as an open fork:
**(i)** a frame/Leibniz correction the naive 3-term Weitzenböck form
doesn't capture, or **(ii)** evidence `F_{S^-}` is incomplete. Rounds
25-44 pursued (i) INDIRECTLY, via "is there a different connection
(`Z_p`) whose bivector spin-lift changes things" — Round 43/44 closed
that specific avenue completely (no bivector-type connection swap can
ever help; Agricola's own `Z_i` was never meant as such a connection
in the first place). This round tests the DIRECT, previously-untried
version of (i): using the CURRENT, already-established connection
(`M_p`), is `K` explained by the Leibniz-rule cross-terms that
NECESSARILY appear when correctly squaring the twisted Dirac operator
`D64` on a frame with `[e_p,e_q]≠0` (naturally-reductive torsion)?

**User's explicit anti-circularity protocol (honored throughout):**
FORBIDDEN to build any term as `K := Delta - (5/2)Id` (circular);
FORBIDDEN to solve coefficients to match `K` or fit signs after
comparison; REQUIRED to derive the candidate correction purely from
frame/Nomizu/connection data, comparing to `K` only at the very end.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic computation. **[POST-
SKEPTIC CORRECTION] The original falsifiability claim here was FALSE:**
"the grouping could give a DIFFERENT off-diagonal value" does not hold
— the grouping's off-diagonal outcome is FORCED by the fixed algebraic
form (`kron(X,Id8)` has off-diagonal zero on `span(w_a,w_b)` for ANY
`X`, verified with an arbitrary symbolic matrix) and cannot vary
regardless of which connection/curvature data `X` actually contains.
The test was not falsifiable in the way originally framed.

## Core argument

1. **[VERIFIED]** This project's own, several-rounds-old definition of
   `D64` (`D_on_simple_tensor`, `g2su3_compute_crossterm.py`) is,
   verbatim: `term1 = (e_i·∇_{e_i}η)⊗ξ`, `term2 = (e_i·η)⊗(∇_{e_i}ξ)`,
   summed over `i=1..6`. In matrix form this is confirmed, independent
   of any prior round's claim, to equal EXACTLY `D64 = Σ_i (e_i⊗Id)·N_i`
   where `N_i := M_i⊗Id + Id⊗M_i` — the STANDARD, textbook Leibniz-rule
   twisted Dirac operator (Clifford multiplication on the LEFT factor
   only, the usual convention for an auxiliary-bundle twist, combined
   with the FULL two-factor Leibniz connection). This is the load-
   bearing structural fact everything else rests on — verified BEFORE
   any reference to `K`, `Delta`, or the L4A tension.
2. **[VERIFIED]** The UNTWISTED single-copy remainder,
   `cubic_and_curvature_L := Dslash_mat² - Σ M_p²` (computed ENTIRELY
   on the single 8-dim copy of Σ, with ZERO reference to twisting,
   `K`, or any of `T12/T21/TORSION_E/cross_casimir`), matches Round
   39's own established closed form `(5/2)Id - 2·Casimir_su3` exactly.
3. **[VERIFIED]** The TWISTING-SPECIFIC cross-terms — `(T12+T21) +
   TORSION_E + cross_casimir` — exist ONLY because `D64`'s own
   `TERM2_mat` (the connection acting on the RIGHT factor, confirmed
   nonzero in #1) is present. Their existence is a FORCED, NECESSARY
   consequence of correctly squaring the already-verified `D64`
   formula on a frame with nonzero Lie bracket — not an ad hoc
   invention to explain `K`.
4. **[VERIFIED, sanity check]** `UNTWISTED + TWISTING_SPECIFIC`
   reconstructs `Delta` exactly (the same algebraic identity Round 41
   already verified, re-grouped by STRUCTURAL origin rather than by
   construction-order — no new arithmetic risk introduced).
5. **[VERIFIED, the actual test]** `TWISTING_SPECIFIC`'s own
   off-diagonal, compressed on `span(w_a,w_b)`, equals `K =
   [[0,4/3],[4,0]]` EXACTLY. This comparison happens ONLY after Steps
   1-4 fixed the grouping criterion — Steps 1-2 contain zero reference
   to `K` at all.
6. **Conclusion — FALSIFIED, post-skeptic (see Skeptic Verdict below):**
   this re-groups Round 41's already-established 5-piece decomposition
   into 2 buckets. The off-diagonal match to `K` is FORCED by pure
   linear algebra, not evidence of anything about Leibniz corrections
   or torsion: `UNTWISTED` is definitionally a single-tensor-factor-
   embedded operator (`kron(X,Id8)`), and any such operator has ZERO
   off-diagonal on `span(w_a,w_b)` regardless of what `X` is — `w_a`
   and `w_b` have disjoint index support in BOTH tensor factors.
   **This does NOT discriminate fork (i) from fork (ii):** a genuinely
   MISSING `F_{S^-}` term, being a two-factor-mixing operator by its
   physical nature, would land in the `TWISTING_SPECIFIC` bucket just
   as cleanly as a correct Leibniz term would. The test cannot tell
   these apart, by construction. The open fork from Round 24 remains
   genuinely open.

## Construction (code:
`g2su3_round45_leibniz_correction_blind_derivation.py`)

STEP 1: verify `D64 = TERM1_mat+TERM2_mat = Σ_i kron(e_i,Id)·N_i`
exactly (the textbook Leibniz formula). STEP 2: build `UNTWISTED`
(Round 39's own closed form, zero reference to twisting terms). STEP
3: build `TWISTING_SPECIFIC` (T12+T21+TORSION_E+cross_casimir) purely
from frame/Nomizu/curvature primitives. STEP 4: sanity-check
`UNTWISTED+TWISTING_SPECIFIC` reconstructs `Delta` exactly. STEP 5: the
actual comparison — compress both groups on `span(w_a,w_b)`, check
`TWISTING_SPECIFIC`'s off-diagonal against `K`.

## Falsifiable Claims

**C1:** `D64 = Σ_i kron(e_i,Id)·N_i` exactly (the textbook Leibniz
twisted-Dirac formula). RESULT: `[VERIFIED-tool]` (STEP 1), **but
`[WEAKENED]` post-skeptic: this is a content-free Kronecker mixed-
product identity — `(A⊗I)(B⊗I)=(AB)⊗I`, `(A⊗I)(I⊗B)=A⊗B` — true for
ANY matrices substituted for `Es`/`Ms`, verified by both skeptics via
arbitrary symbolic substitution. It confirms `D64` matches the
textbook Leibniz-formula TEMPLATE, not that the specific geometry
(connection, curvature) is correct. It cannot fail regardless of
physics content — "load-bearing... highest failure risk" was an
overclaim.**

**C2:** `UNTWISTED := kron(Dslash_mat²-ΣM_p², Id8)` matches Round 39's
own `(5/2)Id-2·Casimir_su3` closed form exactly, built with zero
reference to `K`. RESULT: `[VERIFIED-tool]` (STEP 2).

**C3:** `UNTWISTED + TWISTING_SPECIFIC` reconstructs `Delta` exactly
(no piece double-counted or dropped in this round's re-grouping).
RESULT: `[VERIFIED-tool]` (STEP 4).

**C4 (originally "the actual test"):** `TWISTING_SPECIFIC`'s own
off-diagonal, compressed on `span(w_a,w_b)`, equals `K=[[0,4/3],[4,0]]`
exactly. RESULT: `[VERIFIED-tool]` as a raw computation (the arithmetic
is exact, re-confirmed independently three times), but **`[FALSIFIED]`
as evidence for fork (i) over fork (ii)** — this is an ARITHMETIC
CONSEQUENCE, not a discriminating test. See Skeptic Verdict below: the
outcome is forced by `UNTWISTED`'s `kron(X,Id8)` form regardless of
`X`, and was additionally derivable by pure subtraction from Round 41's
already-committed individual piece values (git-timestamp confirmed to
predate this round's script).

**C5:** `TWISTING_SPECIFIC` ALSO contributes nonzero DIAGONAL content
(`8/3` at `[0,0]`, `0` at `[1,1]`) — meaning `R/4=5/2` is itself partly
twisting-sourced, not purely the untwisted answer. RESULT:
`[VERIFIED-tool]` (STEP 5) — an important caveat, not a clean win.

## Kill Conditions

- C1 killed if: `D64` does NOT match the textbook Leibniz formula —
  the entire grouping rationale collapses (this is the single point of
  highest failure risk; skeptics should attack this hardest).
- C2/C3 killed if: arithmetic errors in the untwisted/reconstruction
  steps — straightforward to check by direct re-run.
- C4 killed if: the off-diagonal comparison is wrong (compression
  convention error, sign error) — this exact failure mode already
  occurred ONCE during this round's own development (a `compress_2x2`
  row/column convention bug gave `[[5/2,4],[4/3,5/2]]` instead of
  `[[5/2,4/3],[4,5/2]]` on first run; caught by the STEP 4 sanity
  assertion, fixed, re-verified) — skeptics should independently
  re-derive the compression convention, not just trust the fixed code.
- **Overarching, highest-priority kill condition — CIRCULARITY:**
  **CONFIRMED, not just risked — this is a TRUE KILL.** Two independent
  skeptics plus the synthesis agent, all working independently,
  converged on the SAME two mutually-reinforcing findings: (1) a
  STRUCTURAL TAUTOLOGY — `UNTWISTED := kron(cubic_and_curvature_L,
  Id8)` has the form `kron(X,Id8)`, and `w_a`, `w_b` have disjoint
  index support in BOTH tensor factors (synthesis agent's own
  strengthening: not just the right factor, as first noted, but both),
  so ANY operator of the form `kron(X,Id8)` OR `kron(Id8,X)` — for
  literally ANY `X`, correct physics or not — has EXACTLY ZERO
  off-diagonal on `span(w_a,w_b)`. Given the pre-existing exact
  identity `Delta=UNTWISTED+TWISTING_SPECIFIC` (Round 41), it follows
  FOR FREE that `off-diag(TWISTING_SPECIFIC)=off-diag(Delta)=K`,
  regardless of whether `TORSION_E`/`cross_casimir` are the "correct"
  torsion terms or whether `F_{S^-}` is complete or missing something
  — a genuinely missing `F_{S^-}` term would, by its physical nature,
  be a two-factor-mixing operator too, and would land in the
  `TWISTING_SPECIFIC` bucket just as cleanly. (2) EMPIRICAL
  PRE-KNOWLEDGE — Round 41's individual piece values (git commit
  `3bf6fc2`, 2026-07-12 20:22:21) predate this round's script; the
  "blind" grouping was chosen with these exact numbers already visible
  on disk. Both findings independently doom the round's central
  inferential move; no textual fix rescues C4/Step-6 — see Skeptic
  Verdict below.

## What this does NOT mean

- **[POST-SKEPTIC, LEADING CAVEAT — the round's central finding]
  Does NOT provide evidence discriminating fork (i) from fork (ii).**
  The off-diagonal match to `K` is a structural tautology given
  `UNTWISTED`'s `kron(X,Id8)` form (verified true for arbitrary `X`,
  by two independent skeptics + synthesis) and was additionally
  derivable by pure subtraction from Round 41's already-committed
  individual piece values, predating this round's script (git-
  timestamp confirmed). The test could not have failed, for any
  connection/curvature content, correct or wrong — see Skeptic
  Verdict below for the full circularity determination.
- **Does NOT prove `F_{S^-}` is complete in any absolute sense** —
  only that THIS specific trace-free residual `K` does not require
  judging it incomplete. Other reasons to question `F_{S^-}`'s
  completeness (not explored here) could still exist.
- **Does NOT mean `R/4=5/2` is now cleanly, mechanistically derived.**
  C5 is an important caveat: `TWISTING_SPECIFIC` contributes nonzero
  diagonal content (`8/3`), meaning the `5/2` value is a SUM of
  untwisted (`-1/6`,`5/2`) and twisting-specific (`8/3`,`0`) diagonal
  parts — NOT purely "the untwisted single-copy answer." The
  preprint's own assumption that `R/4` is a clean, twisting-independent
  scalar is NOT confirmed here; if anything, this shows `R/4` itself
  has a twisting-sourced component, a new wrinkle, not a resolution.
- **Does NOT directly resolve the preprint's own `8/45 vs ~1.03`
  numerical tension** — that comparison is between the preprint's OLD,
  rho_6-parametrized norm ESTIMATE and this project's own EXACT
  calculation (a scale/units question, addressed separately in Round
  23, ruled out as a units mismatch). This round only concerns the
  INTERNAL structural question of why `Delta` is non-scalar in THIS
  project's own calculation — a necessary but not sufficient step
  toward the full tension.
- **Does NOT establish this is the ONLY valid way to group `D64²`'s
  six natural pieces** — per the Kill Conditions' own top-priority
  concern, an adversarial alternative grouping has not been
  exhaustively searched for; the skeptic review should specifically
  probe this.
- **Does NOT touch `preprint.tex`.**
- Does NOT resolve the Casimir_su3-vs-Jac_h identity question (Round
  39), `RHO`/`NU`'s literal AHL2023 notation question, or WHY Round
  34's intertwiner `P` is Hadamard-type — all remain untouched.
- **Concrete next step, NOT started:** if this survives skeptic review,
  investigate whether the SAME grouping logic (untwisted vs
  twisting-specific) applies cleanly to the FULL 16-dim `Γ(S^+⊗S^-)`
  block (not just the 2-dim SU(3)-invariant subspace), which would be
  a stronger, more general test of the same hypothesis.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics + a synthesis agent independently reviewed
this round, ALL THREE running the script themselves and, critically,
writing and executing INDEPENDENT adversarial code (arbitrary symbolic
matrix substitution) that neither the claim nor the script supplied.

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (independent 3rd check) |
|---|---|---|---|
| C1 | WEAKENED (content-free Kronecker identity) | WEAKENED (same finding) | WEAKENED (confirmed; also caught a citation error) |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C3 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL |
| C4 | **FALSIFIED as evidentiary claim** (arithmetic correct, interpretively void) | **FALSIFIED as evidentiary claim** (same) | **FALSIFIED**, confirmed via 2 independent additional routes |
| C5 | CONFIRMED-REAL, honestly handled | CONFIRMED-REAL, honestly handled | CONFIRMED-REAL |
| Step 6 Conclusion | **FALSIFIED — true kill** | **FALSIFIED — true kill** | **FALSIFIED — true kill, unanimous** |

**This is a TRUE KILL, not a fixable weakness.** Both skeptics,
working independently (without seeing each other's reports), derived
the SAME decisive structural argument: `UNTWISTED := kron(cubic_and_
curvature_L, Id8)` has the form `kron(X,Id8)` by construction. Both
independently wrote and ran a symbolic-substitution test — an
ARBITRARY 8×8 matrix `X` (64 free symbols, unrelated to this project's
actual geometry) — and confirmed `kron(X,Id8)` has EXACTLY ZERO
off-diagonal on `span(w_a,w_b)`, for ANY `X` whatsoever. The synthesis
agent independently re-ran this check AND found it is even BROADER
than either skeptic reported: `w_a` and `w_b` have disjoint index
support in BOTH tensor factors (not just the right one), so `kron(Id8,
X)` is ALSO forced to zero off-diagonal for any `X`. Given the
pre-existing identity `Delta = UNTWISTED + TWISTING_SPECIFIC` (Round
41, already established before this round), `off-diag(TWISTING_
SPECIFIC) = off-diag(Delta) = K` follows AUTOMATICALLY — the test's
outcome was forced by the choice of subspace and grouping shape, not
by anything genuine about Leibniz rules, torsion, or twisted-Dirac
structure.

**Compounding, independent confirmation of empirical circularity:**
the synthesis agent checked git timestamps directly — Round 41's file
(containing all four individual piece values needed to compute
`TWISTING_SPECIFIC`) was committed (`3bf6fc2`, 2026-07-12 20:22:21)
BEFORE this round's script was written. The "blind" derivation had
these exact numbers already visible on disk.

**Why this means the test has zero power to discriminate fork (i) vs
(ii):** a genuinely MISSING `F_{S^-}` curvature term would, by its own
physical nature, be a two-tensor-factor-mixing operator (curvature
endomorphisms act on the twisting/auxiliary bundle) — exactly the SAME
kind of object as `TORSION_E`/`cross_casimir`/`T12+T21`. Such a missing
term would land in the `TWISTING_SPECIFIC` bucket just as cleanly as
the "correct" terms do, and the test would STILL report a PASS. The
construction cannot distinguish "F_{S^-} is complete, K is a genuine
Leibniz correction" from "F_{S^-} is missing something, and THAT
missing piece is what produces K" — both scenarios are indistinguishable
under this specific grouping.

**Additional finding (Skeptic 1, independently confirmed by
synthesis):** the script's own docstring misattributes the
`D64==TERM1+TERM2` ground-truth check to `g2su3_round25_K_derivation.py`
("STEP B0b") — grep-confirmed this does NOT exist there; the actual
check is in `g2su3_Sminus_weitzenbock.py`. A minor provenance error,
corrected in the script (not present verbatim in claim.md, no claim.md
edit needed for this item specifically).

**Response: Fixed where fixable, killed where not.** Per the FL Step
8a response matrix, this is NOT a "Dismiss" or "Accept-with-caveat"
situation — the core predicate ("this test adjudicates fork i vs ii")
is false, and no textual reframing rescues it. Applied: Step 6's
Conclusion, C1, C4, the Question Type falsifiability statement, and
the Kill Conditions circularity item all corrected in place above (not
deleted — the honest record of what was tried and why it failed is
kept, per this project's own Kill Analysis discipline). A NEW leading
bullet added to "What this does NOT mean" naming the central finding
explicitly.

**What survives, solid:** Round 41's five-piece decomposition,
independently RE-verified via a different route here (C2, C3, C5) —
genuine, could-have-failed algebra, not affected by the circularity
finding. `D64`'s match to the textbook Leibniz-formula TEMPLATE (C1,
downgraded) also stands, though its informativeness is much lower than
originally claimed.

**Genuinely new gap neither skeptic caught individually, found by
synthesis:** the disjointness is NOT limited to the right tensor
factor (as first noted) — `w_a`/`w_b` are disjoint in BOTH factors,
meaning this specific 2-dim subspace is a poor testbed for ANY
single-factor-vs-remainder split, not just the one attempted here.
Recorded as a methodological lesson for any future attempt at this
fork: pick a subspace where "untwisted" and "twisting" content are NOT
separable by tensor-factor index alone.

**True kill? YES** (all three reviewers agree, unanimous, two
independent verification routes). Core predicate — that this
construction discriminates fork (i) from fork (ii) — is FALSE, not
merely weak or narrow. **Verdict: REJECT** for the discriminating
claim (Step 6 / C4-as-evidence). C2/C3/C5's honest bookkeeping and
C1's downgraded structural confirmation are NOT rejected — they are
correct, independently re-verified computations that simply don't
support the interpretive conclusion originally drawn from them.
