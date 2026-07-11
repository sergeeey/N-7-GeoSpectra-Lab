---
experiment_id: 20260708-dolan-casimir-g2su3
round: 31
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C2-C4_confirmed_C3_scope_narrowed_no_falsification
parent: round29 (derived (1,-1/2,-7/4) via pure symbolic algebra, but
  Ch_tilde/degree4_term still went through 8x8 matrix construction +
  trace-projection — flagged by both FL Step 8a skeptics as a
  code-hygiene/rigor gap in the "purely symbolic" framing)
---

# claim.md — Round 31: the Sigma-side "Phase 2" derivation chain, with
ZERO e_action/build_quartic_matrix calls in STEPs A-C (SCOPE NARROWED
post-skeptic — see "Skeptic Verdict" below)

## Background

User chose this scope explicitly (of 4 offered candidates for Round 31):
"Достроить Phase 2 до конца (degree4_term/scalar_term)" — finish Phase 2
completely. Round 29 derived `Σ_p M_p²` and `H²` via pure combinatorics
(T-table + Clifford-word reduction, zero matrix construction), but
`Ch_tilde`/`degree4_term` were still built via `build_quartic_matrix`
(which uses `e_action` to realize coefficients as an 8×8 matrix) and
THEN trace-projected onto `{Id,X}` to extract coordinates — both FL Step
8a skeptics on Round 29 flagged this as inconsistent with the "purely
symbolic" claim for the overall pipeline (C6's WEAKENED note).

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — combinatorial/symbolic derivation, verified
computationally at every step. NOT empirical, NOT causal.

## Key observation (what made this tractable)

`jach_coeff(i,j,k,l)`/`degree4_coeff(i,j,k,l)`
(`g2su3_round26_jach_derivation.py`) were ALREADY pure scalar functions
of the ordered index-quadruple `(i,j,k,l)` — built entirely from
`curv_h`/`T`-table dict lookups via `jac_h`/`jac_m` (themselves pure
dict lookups + `ad_nu_m_trusted`, zero Clifford/`e_action` dependency).
`build_quartic_matrix` only uses `e_action` to REALIZE an
already-computed scalar coefficient as an 8×8 matrix entry — the
coefficient itself is fully determined before any matrix operation
happens. Since `(1,2,3,4)`, `(1,2,5,6)`, `(3,4,5,6)` are ALREADY the
target quartic basis elements in canonical sorted order, their
coefficients are obtained by DIRECT function evaluation —
`jach_coeff(1,2,3,4)` etc. — with zero matrix construction anywhere.
Verifying "no support outside these 3 quadruples" is 12 more direct
scalar evaluations (checking they equal zero), not a trace-projection
residual check on a constructed matrix.

## Construction (code:
`g2su3_round31_full_combinatorial_derivation.py`)

**STEP A:** evaluate `jach_coeff`/`degree4_coeff` for ALL `C(6,4)=15`
ordered index-quadruples `i<j<k<l` in `1..6` — zero calls to
`build_quartic_matrix`/`e_action`/`clifford_quad` anywhere in this step.
Assert only the 3 "pair-partition" quadruples are nonzero, all 12 others
exactly zero. Extract `ch_tilde_X:=1/3`, `deg4_X:=-5/12` (both pure
scalars, matching Round 29's matrix-derived values exactly — now derived
WITHOUT ever building the matrix those values were previously read off
from).

**STEP B:** reuse Round 29's already matrix-free `Σ_p M_p²`/`H²`
derivation unchanged (`expand_quartic_sum_from_T`/
`expand_H_squared_from_T`), with explicit dict-equality assertions
wiring the values in.

**STEP C:** assemble `Diff` purely symbolically (sympy symbols `H,Id,X`
— zero numeric 8×8 matrices anywhere in this step) using ONLY STEP A+B's
pure-combinatorics outputs, substitute `X=3(Casimir_su3-Id)`, extract
`(a,b,c)` via `sp.coeff()`. Every single input feeding this step is now
derived without a single Clifford matrix construction anywhere upstream.

**STEP D (sanity cross-check, the ONLY place THIS SCRIPT builds a
Sigma-side/`e_action`-based 8×8 matrix — see "Skeptic Verdict" for why
this is narrower than "the only matrix construction in this script"):**
reconstruct `a·H+b·Id+c·Casimir_su3` and compare against the
independently-built numeric `Diff` (Round 28's `build_diff_noncircular`)
— exact match. This match is ALSO what confirms the `X=3(Cas-Id)`
substitution (imported from Round 29, see C3 below) was valid for THESE
`(a,b,c)` — not merely a redundant sanity check.

## Falsifiable Claims

**C1:** `jach_coeff`/`degree4_coeff`, evaluated directly (no matrix
construction) for all 15 ordered index-quadruples, are nonzero ONLY on
`(1,2,3,4)`, `(1,2,5,6)`, `(3,4,5,6)`, with the SAME value across all
three (`1/3` and `-5/12` respectively).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2:** `Σ_p M_p²`/`H²`'s already-established (Round 29) combinatorial
closed forms are correctly reused, verified via explicit dict-equality
assertions (not silently assumed).

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3 (the headline result; SCOPE NARROWED post-skeptic — both skeptics
independently found the original wording overclaimed, see "Skeptic
Verdict" below):** assembling `Diff` purely symbolically from STEP A+B's
outputs gives EXACTLY `(a,b,c)=(1,-1/2,-7/4)` — with `jach_coeff`/
`degree4_coeff` themselves, and the specific `build_quartic_matrix`/
`e_action`/`clifford_quad` functions, making ZERO appearances anywhere
in STEPs A-C. GIVEN the `curv_h`/`T` dicts as pre-computed inputs,
extracting `(a,b,c)` uses ONLY dict lookups, 6-vector arithmetic, and
pure sympy symbolic algebra — closing the SPECIFIC `build_quartic_matrix
+ trace-projection` pattern both FL Step 8a skeptics flagged on Round 29
for `Ch_tilde`/`degree4_term`.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP C).
**Downgraded/narrowed framing (both skeptics independently, converging
on the identical finding):** the ORIGINAL wording — "ZERO 8×8 Clifford-
matrix construction anywhere in the derivation chain" — is FALSE AS
WRITTEN. `build_curvature_h_table()` (called in STEP A to produce
`curv_h`) itself constructs 8×8 matrices: `RHO`/`NU` (Cl(7,0) generators
and their products), a `bracket_e(p,q)` matrix commutator per `(p,q)`
pair (15 pairs), and `decompose_g2`'s `Tr(nu_k.T·M)` trace-projection
(14 times per pair, 210 total) — unchanged since Round 13, and NOT
addressed by this round. This is the SAME "build a matrix, then
trace-project it" pattern Round 29 was flagged for, RELOCATED upstream
into computing `curv_h`, not eliminated. Additionally, the substitution
`X=3(Casimir_su3-Id)` (STEP C) is imported UNCHANGED from Round 29's own
matrix-verified relation (`su3_action`+squaring+trace-projection), not
independently re-derived here. What DOES genuinely hold, and is this
round's real contribution: `jach_coeff`/`degree4_coeff` and the specific
`build_quartic_matrix`/`e_action`/`clifford_quad` functions are absent
from STEPs A-C — the exact pattern flagged on Round 29 is closed, not
merely relocated, for `Ch_tilde`/`degree4_term` specifically.

**C4:** the fully-combinatorial `(a,b,c)` reconstructs the
independently-built numeric `Diff` (Round 28's construction) exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP D).

## Kill Conditions

- C1 killed if: skeptic finds `jach_coeff`/`degree4_coeff`, or the
  `jac_h`/`jac_m`/`ad_nu_m_trusted` functions they call, secretly
  construct or reference an 8×8 matrix anywhere (would undermine the
  "zero matrix construction" claim) — trace the full call chain:
  `jach_coeff` → `jac_h` → `h_bracket_action_on` → `ad_nu_m_trusted`
  (returns a 6-vector via `AD_NU_M_BIVECTOR` dict lookup, no Clifford
  algebra at all) and `curv_h.get(...)` (dict lookup). Confirm none of
  these import or call `e_action`/`clifford_quad`/`build_quartic_matrix`.
- C1 killed if: skeptic finds the "only 3 quadruples nonzero" result is
  itself somehow seeded by information from the target answer (circular)
  — verify `jach_coeff`/`degree4_coeff` are called with the SAME
  definitions Round 26 established (long before this round or Round 29's
  target formula existed), not redefined here to force the answer.
- C3 killed if: skeptic finds STEP C secretly references `Diff_numeric`
  or any matrix-derived quantity before the `(a,b,c)` extraction —
  confirm `Hs,Ids,Xs` are pure sympy symbols with no numeric substitution
  until the final `.coeff()` calls, and that `Diff_numeric`/`Ls`/`Casimir_
  su3`/`H`/`Ms` (all matrix-based) are constructed ONLY in STEP D, after
  `(a,b,c)` are already fixed.
- C4 killed if: skeptic finds `build_diff_noncircular` (imported
  unchanged from Round 28) has regressed or changed meaning since its
  own skeptic-reviewed fix — re-verify it still matches
  `round28_claim.md`'s description (no reference to the target formula
  anywhere in its body).

## What this does NOT mean

- Does NOT independently explain WHY only the 3 "pair-partition"
  quadruples `(1,2,3,4)/(1,2,5,6)/(3,4,5,6)` are ever nonzero (out of 15
  possible) — this is verified computationally but not derived from a
  deeper principle here. Plausibly connects to Round 28's proven 3-dim
  SU(3)-equivariant + Swap-symmetric space, but that connection is not
  made explicit in this round — flagged for a future round.
- Does NOT change any previously-established spectrum, index, eigenvalue,
  or `Diff` value from Rounds 4-30 — this round re-derives the SAME
  already-known numbers via a route with fewer matrix-construction steps,
  and cross-checks agreement (STEP D).
- Does NOT mean `Casimir_su3`'s OWN construction (via `su3_action` +
  matrix squaring) is now matrix-free — `Casimir_su3` still requires
  building `su3_action(k,·)` as an 8×8 matrix and squaring it (used only
  in STEP D's sanity check here, not in the STEP A-C derivation chain
  itself, which expresses everything via the ABSTRACT symbol `Cas`
  rather than needing `Casimir_su3`'s own numeric matrix at all until the
  final cross-check).
- **Does NOT mean `build_curvature_h_table()`'s OWN construction is
  matrix-free** (post-skeptic addition, symmetric to the `Casimir_su3`
  caveat above) — it internally builds 8×8 `RHO`/`NU` Clifford-matrix
  products (Cl(7,0)-side, unchanged since Round 13), a `bracket_e` matrix
  commutator per `(p,q)` pair, and `decompose_g2`'s trace-projection of
  those matrices onto the `nu(1..14)` basis. What this round closes is
  the SPECIFIC downstream pattern flagged in Round 29
  (`Ch_tilde`/`degree4_term` via `build_quartic_matrix` +
  `decompose_in_scalar_quartic_basis`) — not the upstream matrix
  operations that produce `curv_h` in the first place, which predate
  this round entirely.
- **Does NOT mean the `X=3(Casimir_su3-Id)` relation is independently
  re-derived here** — it is imported UNCHANGED from Round 29, where it
  was established via `su3_action`+matrix squaring+trace projection. Its
  own structural derivation is Round 30's separate target (`Ch_tilde=
  Casimir_su3`, not `X`'s relation to `Casimir_su3` specifically).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension or
  which of `M_p`/`Z_p` the preprint's own L4A convention intends — same
  standing open questions as Rounds 26-30.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics converging on the IDENTICAL finding + a tool-verified synthesis
pass that independently re-ran the script and re-confirmed the finding
via grep + direct code trace, not just relaying the skeptics' narrative)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both + synthesis, via direct call-chain trace + grep) | `jach_coeff→jac_h→h_bracket_action_on→ad_nu_m_trusted`/`curv_h.get(...)` contains zero references to `e_action`/`clifford_quad`/`build_quartic_matrix` — confirmed by grep returning zero matches in the relevant function bodies. All 15 quadruples genuinely enumerated (`itertools.combinations` exhaustive). Non-circular: target values never referenced before being computed. |
| C2 | CONFIRMED-REAL (both + synthesis) | Round 29's closed forms reused unchanged, wired via explicit dict-equality assertions, re-run confirms both pass. |
| C3 | **WEAKENED (both skeptics independently, converging on the SAME root cause) → scope narrowed, fixed** | The narrow claim (STEPs A-C make zero calls to `build_quartic_matrix`/`e_action`/`clifford_quad`) is CONFIRMED-REAL. The broader claim as originally written ("ZERO 8×8 Clifford-matrix construction anywhere in the derivation chain") is FALSE — `build_curvature_h_table()` (STEP A) itself builds 8×8 Cl(7,0)-side matrices (`RHO`/`NU`/`bracket_e`/`decompose_g2`, unchanged since Round 13) — the SAME "matrix + trace-projection" pattern Round 29 was flagged for, relocated upstream rather than eliminated. Independently re-confirmed by synthesis via grep (zero matches for the three Sigma-side symbols in `g2su3_appendix_a_construction.py`, but direct code read confirms its own SEPARATE 8×8 matrix machinery). Fixed: claim.md and the script's docstring/print statements narrowed to the defensible claim; symmetric caveat added (paralleling the pre-existing `Casimir_su3` caveat). |
| C4 | CONFIRMED-REAL (both + synthesis) | `build_diff_noncircular` re-read, confirmed unchanged from Round 28, no reference to the target formula anywhere in its own body (grep-confirmed). Re-run confirms the final match. |

**FL Response Matrix:** No claim was FALSIFIED. C3's WEAKENED verdict —
found INDEPENDENTLY by both context-blind skeptics converging on the
identical root cause, then independently re-confirmed by the synthesis
agent's own grep + direct code trace — was resolved as a **Fix**
(documentation/framing only; the numeric result `(1,-1/2,-7/4)` and its
non-circularity are untouched). Per the synthesis's own meta-note: this
is structurally the SAME class of issue Round 30's `/boyko-triangle-
audit` caught (a claim that sounds clean at one level of abstraction
while the actual matrix construction has been relocated rather than
removed) — but this time BOTH FL Step 8a skeptics caught it themselves,
without needing an external audit pass, suggesting the Round 30
postmortem's lesson (documented in this project's own activeContext.md)
may already be sharpening this project's own review process.

**Overall:** the round's real, narrower contribution — the specific
`build_quartic_matrix`+trace-projection pattern Round 29 was flagged for
is genuinely eliminated for `Ch_tilde`/`degree4_term` (not merely
relocated, unlike the upstream `curv_h` construction which predates this
round and was never in scope) — survives intact. The numeric result and
STEP C's non-circularity are unaffected; only the SCOPE of what was
claimed to be "matrix-free" needed narrowing.
