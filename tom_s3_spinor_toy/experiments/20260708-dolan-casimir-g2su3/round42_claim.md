---
experiment_id: 20260708-dolan-casimir-g2su3
round: 42
date: 2026-07-12
tier: Full-Ladder
status: skeptic_reviewed_promoted_with_weak_marker
parent: round41 (full 5-piece closure of Delta's decomposition); this
  round investigates the M_p-vs-Z_p L4A convention question the user
  raised in a detailed, well-reasoned follow-up message after Round 41
---

# claim.md — Round 42: M_p-vs-Z_p investigation — a genuine research
gap found and reported honestly, NOT papered over

## Background

After Round 41 closed Delta's full 5-piece decomposition, the user
sent a detailed, accurate summary of what that round achieved (a
complete algebraic accounting, NOT a resolution of the physical
question) and proposed a specific, well-reasoned Round 42 direction:
"разобраться с точной конвенцией `M_p` против `Z_p` и выяснить, какая
комбинация пяти известных частей действительно является Bochner
Laplacian... Именно это может наконец разрешить `8/45 vs ~1`."

**Investigation (before any commitment to a specific construction):**
Round 26 (Rounds 23-26 era) had already isolated `-Σ Z_p²` (Agricola's
canonical, `t=0`, connection) as a single AGGREGATE 8×8 quantity, via
subtraction from `Dslash_mat²` — established:
`(-Σ Z_p²) - (-Σ M_p²) = H - (1/2)·Id - (7/4)·Casimir_su3` (call this
`Delta_HCas`). **Individual `Z_p` matrices were NEVER constructed
anywhere in this project** — confirmed by a research agent's read of
`g2su3_round26_jach_derivation.py` and a codebase-wide `Grep`.

A "pure rescaling" hypothesis (`Z_p := 2t·M_p`, giving `Z_p=0` at
`t=0`) was tested and **computationally FALSIFIED** against Round 26's
own aggregate identity (would require `Σ M_p² == Delta_HCas`, directly
checked FALSE — `Σ M_p² = -(1/2)·Id+(1/4)·Casimir_su3` in closed form,
a completely different expression).

Two research agents then read Agricola 2002 ("Connections on Naturally
Reductive Spaces...", arXiv:math/0202094v1) and Agricola-Hofmann-Lawn
2023 ("invariant spinors") **directly** (both PDFs already sit in this
repo). Found: the connection family `∇^t_X Y = ∇^0_X Y + t·[X,Y]_m`,
with `Λ^0_m=0` (canonical) and `Λ^{1/2}_m = Λ^g` (Levi-Civita, this
project's own `LEVI_CIVITA_NOMIZU` table). **Did NOT find** an explicit
per-index spin-lift formula for the canonical connection specific to
`S^6=G2/SU(3)` — only the aggregate Dirac operator `D^0=-H` (already
established, Round 27). Building genuine individual `Z_p` matrices
would require either reading further into the primary sources (AHL2023's
own "Example 4.18", flagged but not read due to research-agent time
budget) or original derivation work with its own dedicated skeptic
review — **correctly identified as a task NOT to force within one
round.**

**Scope chosen (via `AskUserQuestion`, user chose the safer option):**
compute ONLY the piece of a hypothetical "Z_p-based `∇*∇`" that IS
expressible from the already-known aggregate `-Σ Z_p²` — leaving the
genuine `Σ_p Z_p⊗Z_p` cross-term EXPLICITLY, PROMINENTLY open (it
structurally cannot be computed from the aggregate alone — this is a
missing INGREDIENT, not a numerical gap that "just needs more compute").

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — an exact algebraic computation, verified.
NOT empirical, NOT causal. **NOTE: this round's construction is
INHERENTLY INCOMPLETE by design** (missing the cross-term entirely) —
its result is reported as suggestive/directional, explicitly NOT as
evidence resolving the underlying question.

## Core argument

1. **[VERIFIED, STEP A]** `Delta_HCas := H-(1/2)·Id-(7/4)·Casimir_su3`
   (Round 26's own established aggregate difference), cited unchanged.
2. **[VERIFIED, STEP B]** `compress(kron(Delta_HCas,Id8))` and
   `compress(kron(Id8,Delta_HCas))` on `span(w_a,w_b)` both equal
   `[[-17/6,0],[0,-1/2]]` exactly — the ONLY part of a "Z_p-based
   `∇*∇`" expressible from the aggregate alone.
3. **[VERIFIED, STEP C]** `Delta^{(Z,partial)}_2x2 := Delta_2x2 −
   cross_casimir_2x2 − shift = [[49/6,5/3],[5,7/2]]`. **This is NOT
   the true Z_p-based `Delta`** — it subtracts the M_p-based cross
   term entirely without adding back any Z_p-based replacement
   (unavailable), so it only answers "what if the aggregate shifted,
   holding the cross-term at zero" — a hypothetical, not a real
   alternative construction.
4. **[VERIFIED, STEP D, the finding]** The aggregate-only shift makes
   `Delta`'s traceless (non-scalar) part LARGER: Frobenius norm² goes
   from `160/9` (original) to `116/3` (Z-partial).
5. **Conclusion — deliberately narrow, must NOT be over-read:** this
   does NOT mean "switching to Z_p makes things worse, confirming M_p
   is correct." The missing `Σ_p Z_p⊗Z_p` cross-term could easily
   reverse this trend or dominate it entirely — we have NO way to
   know without individual `Z_p` matrices, which this round explicitly
   did NOT construct (a genuine, honestly-reported research gap, not
   a corner cut).

## Construction (code:
`g2su3_round42_mp_zp_aggregate_shift.py`)

**STEP A:** build `Delta_HCas` (cited, Round 26's own value).

**STEP B:** compress `kron(Delta_HCas,Id8)` and `kron(Id8,Delta_HCas)`
on `span(w_a,w_b)`.

**STEP C:** assemble `Delta^{(Z,partial)}_2x2` using Round 41's own
`cross_casimir_2x2` (re-derived in-script) and Round 24/25's
`Delta_2x2` (cited).

**STEP D:** compare non-scalarity magnitude (Frobenius norm² of the
traceless part) between the two versions.

## Falsifiable Claims

**C1:** `Delta_HCas = H-(1/2)·Id-(7/4)·Casimir_su3` builds without
error. RESULT: `[VERIFIED-tool]` (STEP A) — cited from Round 26, not
independently re-derived from Round 26's own STEP-5/6 construction in
this script (see Kill Conditions).

**C2:** `compress(kron(Delta_HCas,Id8))` and
`compress(kron(Id8,Delta_HCas))` both equal `[[-17/6,0],[0,-1/2]]`
exactly. RESULT: `[VERIFIED-tool]` (STEP B).

**C3:** `Delta^{(Z,partial)}_2x2 = [[49/6,5/3],[5,7/2]]` exactly.
RESULT: `[VERIFIED-tool]` (STEP C) — an explicitly INCOMPLETE
quantity, not the true Z_p-based Delta (see Core argument #3).

**C4:** Frobenius norm² of the traceless part: `160/9` (original) →
`116/3` (Z-partial), i.e. the aggregate-only shift increases
non-scalarity. RESULT: `[VERIFIED-tool]` (STEP D) — arithmetically
exact (confirmed by direct script execution) but **`[WEAK]` as a
"directional finding"** per FL Step 8a: both skeptics + synthesis
independently found the caveats originally admitted LESS incompleteness
than actually exists — see the two new bullets added to "What this does
NOT mean" below (the shift's left+right convention is unstated/
undissed against Round 41's own asymmetric decomposition, AND `M_p`
remains unswapped inside `T12+T21`/`TORSION_E`, not just the aggregate
piece — a THIRD missing ingredient, not just the cross-term).

## Kill Conditions

- C1 killed if: `Delta_HCas` does not match what Round 26's own
  script/claim actually establishes — this round CITES the value
  rather than re-deriving it from Round 26's own `Ch_tilde`/
  `degree4_term`/`scalar_term` construction (a genuine limitation,
  flagged, not fixed this round — see "What this does NOT mean").
- C2/C3 killed if: arithmetic errors in the compression or assembly —
  straightforward to check by hand (both skeptics should verify).
- C4 killed if: the Frobenius-norm comparison is computed incorrectly,
  or if `116/3 ≤ 160/9` on correct re-computation (would reverse the
  directional finding, not change the round's fundamental honesty
  requirement).
- **Overarching kill condition for this ENTIRE round:** if the
  "suggestive, not definitive" framing is found to be insufficiently
  prominent, or if any part of Core argument/Conclusion reads as
  claiming this resolves or meaningfully informs the M_p-vs-Z_p
  question — this would be a genuine overclaim requiring a fix, NOT a
  minor rhetorical nit (unlike Round 41's milder "milestone" framing
  issue — this round's construction is missing an entire structural
  ingredient, a categorically bigger gap).

## What this does NOT mean

- **Does NOT resolve the M_p-vs-Z_p L4A convention question.** The
  genuine question — which connection (or neither) is the "correct"
  object for the preprint's own `R/4` argument — remains completely
  open. This round could not even build individual `Z_p` matrices, let
  alone determine which is physically correct.
- **Does NOT establish which connection is "correct" for L4A.** Round
  26's own "What this does NOT mean" already stated this; this round
  does not change that.
- **Does NOT resolve the `8/45 vs ~1` L4A norm-bound tension** — the
  user's own hoped-for outcome. This round is explicitly a SCOUTING
  step that hit a genuine research wall (missing primary-source detail
  on the canonical connection's per-index spin-lift), reported
  honestly rather than forced past.
- **The `Delta^{(Z,partial)}` "more non-scalar" finding is NOT evidence
  that M_p is the "right" convention or that Z_p is "wrong."** The
  missing cross-term `Σ_p Z_p⊗Z_p` is not a small correction — it is a
  structurally necessary piece of comparable scale to the terms
  already computed, and its omission could reverse or dominate this
  round's directional finding entirely.
- **[POST-SKEPTIC ADDITION] The `left+right` shift convention is an
  unstated assumption, not directly justified against Round 41's own
  decomposition.** The shift `kron(Delta_HCas,Id8)+kron(Id8,Delta_HCas)`
  treats the aggregate contribution as symmetric across both tensor
  factors — matching how Round 24's `∇*∇` itself is genuinely
  symmetric (`N_p:=M_p⊗Id+Id⊗M_p` gives BOTH `kron(CASIMIR_L_plain,Id8)`
  and `kron(Id8,CASIMIR_L_plain)` with equal weight) — but Round 41's
  own decomposition of `Delta` puts the ENTIRE aggregate-type
  contribution into a LEFT-only piece (`piece_H_and_step2 =
  kron(cubic_and_curvature_L,Id8)`, no right-side counterpart, because
  the right-factor Casimir contribution algebraically CANCELS between
  `D64²` and `∇*∇` — a genuine structural fact, not an inconsistency).
  An alternative "left-only" convention (matching Round 41's own
  piece labeling literally) gives `61/2` instead of `116/3` for the
  Z-partial Frobenius norm². **The qualitative "MORE non-scalar"
  direction is robust across both conventions checked (both `116/3`
  and `61/2` exceed `160/9`) — but the specific magnitude `116/3` is
  convention-dependent and should not be quoted as a precise number
  without this caveat.**
- **[POST-SKEPTIC ADDITION] `M_p` also appears UNSWAPPED inside
  `T12+T21` and `TORSION_E` — not just inside the aggregate Casimir-type
  piece.** `T12+T21` is built from `Dslash_mat=Σ_p E_p·M_p` and
  `TERM2=Σ_p kron(E_p,M_p)` (Round 41's own construction); `TORSION_E`
  is built from `nabla_bracket(p,q)`, which itself uses `M_r` directly.
  A GENUINELY coherent `M_p→Z_p` swap would need to replace `M_p` in
  ALL of these locations, not just in the aggregate `−Σ M_p²` this
  round actually shifted — requiring the same individual `Z_p` matrices
  this round could not construct. This is a THIRD structurally missing
  ingredient (beyond the `Σ Z_p⊗Z_p` cross-term), meaning this round's
  "directional finding" carries even LESS interpretive weight than the
  original framing (missing "one piece") suggested.
- Does NOT touch `preprint.tex`.
- Does NOT resolve the Casimir_su3-vs-Jac_h identity question (Round
  39), `RHO`/`NU`'s literal AHL2023 notation question, or WHY Round
  34's intertwiner `P` is Hadamard-type — all remain untouched.
- **Concrete next step, NOT started:** read AHL2023's own "Example
  4.18" (and surrounding §2/§4 spin-lift construction method) to
  determine whether the canonical connection's per-index spin-lift
  formula for `S^6` is derivable from already-available data (the
  `ad(ν_i)|_m` table this project's own `Λ^g` construction already
  uses), or whether it requires genuinely new primary-source content.

## Skeptic Verdict (FL Step 8a)

Two context-blind skeptics (Read/Bash, no session history) + a
tool-using synthesis agent independently reviewed this round via direct
file reads of `round42_claim.md`, the script, and the two cited prior
scripts (`g2su3_round26_jach_derivation.py`, `g2su3_round41_...py`).

| Claim | Skeptic 1 | Skeptic 2 | Synthesis (tool-verified) |
|---|---|---|---|
| C1 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (ran Round 26's own script, exit 0) |
| C2 | CONFIRMED-REAL | CONFIRMED-REAL (execution-contingent) | CONFIRMED-REAL (ran Round 42's script, asserts pass) |
| C3 | CONFIRMED-REAL | CONFIRMED-REAL | CONFIRMED-REAL (matches script output exactly) |
| C4 | WEAKENED (1 unstated convention) | WEAKENED (1 unstated convention + 1 additional missing ingredient) | WEAKENED (adopts skeptic 2's fuller framing) |

**No FALSIFIED claims.** C1-C3 solid, tool-verified. **C4's arithmetic
is exact** (`160/9→116/3`, confirmed by direct script execution) — what
needed fixing was the SCOPE of the caveats around it, not the numbers.

**Both skeptics independently found the original caveats admitted LESS
incompleteness than actually exists.** Skeptic 1 found one gap: the
`left+right` shift convention is unstated and not directly derivable
from Round 41's own left-only decomposition of `Delta` (an alternative
"left-only" convention gives `61/2` instead of `116/3` — direction-
robust, magnitude-fragile). Skeptic 2 independently found the SAME gap
PLUS a second, distinct one: `M_p` also appears unswapped inside
`T12+T21` (via `Dslash_mat=Σ E_p·M_p`, `TERM2=Σ kron(E_p,M_p)`) and
`TORSION_E` (via `nabla_bracket`'s own use of `M_r`) — meaning a
genuinely coherent `M_p→Z_p` swap would need individual `Z_p` in THREE
places, not just the aggregate Casimir-type piece this round actually
shifted. The synthesis agent independently verified skeptic 2's
additional point by re-reading Round 41's own construction, confirmed
it as a real, separate incompleteness, and adopted skeptic 2's fuller
two-caveat framing as final (skeptic 1's caveat being a strict subset).

**Response: Fixed, not dismissed.** Added BOTH caveats prominently to
"What this does NOT mean" (not buried — each is a full paragraph with
the specific alternative number `61/2` and the specific code
locations for the unswapped `M_p`), and updated the script's own
CONCLUSION print statements to match, so the artifact and the claim
document say the same thing. The round's core honesty (explicit
research-gap reporting: individual `Z_p` never built, no fabricated
formula, concrete next step named) is UNCHANGED and was never in
question — what was fixed is precision about HOW incomplete the
"directional finding" actually is (three missing ingredients, not one).

**Additional synthesis-agent finding (neither skeptic could check
without Bash):** all in-script `assert`s in Rounds 26, 41, and 42
were independently RE-EXECUTED (not just read), confirming zero
cross-round symbol/import drift (`build_H_matrix`, `su3_action`, etc.
are the exact same objects across all three rounds).

**True kill? No** (both skeptics + synthesis agree). Core predicate —
the honest research-gap report and the arithmetically-exact
`Delta_HCas`-shift computation — holds. What was wrong was scope
precision on C4's caveats, now fixed.

**Overall: PROMOTE**, with C1-C3 clean `[VERIFIED-tool]` and C4
explicitly marked `[WEAK]` given its now-fully-scoped (three-ingredient)
incompleteness.
