---
experiment_id: 20260708-dolan-casimir-g2su3
round: 32
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C4_confirmed_no_falsification_minor_hygiene_fix_applied
parent: round31 (finished Phase 2 for Ch_tilde/degree4_term given curv_h
  as an input, but explicitly flagged build_curvature_h_table()'s OWN
  8x8 Cl(7,0)-side matrix construction as unaddressed — both FL Step 8a
  skeptics independently caught the original Round 31 wording
  overclaiming "zero matrix construction anywhere" when this piece
  still used matrices)
---

# claim.md — Round 32: `build_curvature_h_table()` rebuilt entirely
combinatorially — the last remaining Clifford-matrix construction in the
Phase 2 chain eliminated

## Background

User chose this scope explicitly (of 3 offered candidates for Round 32):
"Довести build_curvature_h_table до комбинаторики" — bring
`build_curvature_h_table` to combinatorics. Round 31 closed the
`build_quartic_matrix`+trace-projection pattern for `Ch_tilde`/
`degree4_term` GIVEN `curv_h` as an input, but both FL Step 8a skeptics
independently found (and Round 31's claim.md now explicitly documents)
that `build_curvature_h_table()` itself still builds 8×8 matrices
(`RHO`/`NU` Cl(7,0)-side generators/products, `bracket_e` matrix
commutator, `decompose_g2`'s `Tr(nu_k.T·M)` trace-projection) — unchanged
since Round 13. This round eliminates that too.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — combinatorial/symbolic derivation, verified
computationally at every step. NOT empirical, NOT causal.

## PRECISE SCOPE STATEMENT (learned directly from Round 31's skeptic-
caught overclaim — stating this UP FRONT rather than fixing it after
review)

This round's script has SEVEN steps. Exactly which use 8×8 matrices and
which do not:

| Step | Uses 8×8 matrices? | Role |
|---|---|---|
| A | **YES** (`RHO`-built bivector products) | ONE-TIME, GENERAL verification of the combinatorial trace primitive `Tr(e_S^T e_T)=8·δ_ST` — not repeated per `(p,q,k)`, just once for the whole algebra |
| B | **YES** (`nu(k)`/`e(p)` matrices) | Self-test: confirms the `{(a,b):coeff}` dict transcription of `NU`'s own literal source matches the existing matrices exactly, for all 6 `e(p)` and all 14 `nu(k)` |
| C+D (`build_curv_h_combinatorial`) | **NO** | The actual derivation — commutator + dot-product, zero matrix construction |
| E | **YES** (`build_curvature_h_table()`) | Cross-check the combinatorial result against the OLD matrix-based function — not part of the derivation itself |
| F | **NO** | Feeds the combinatorial `curv_h` into Round 31's own matrix-free pipeline to re-derive `(1,-1/2,-7/4)` |
| G | **YES** (`su3_action`/`H`/`Ms`, Σ-side) | Final numeric sanity cross-check, same role as Round 29/31's own final step |

**The claim is specifically: `build_curv_h_combinatorial()` (STEP C+D)
and everything it feeds (STEP F) construct zero 8×8 matrices. STEPs
A/B/E/G are verification/cross-check steps that NECESSARILY use
matrices (to confirm the combinatorial primitives and results against
known ground truth) — this is not a gap, it is what makes the claim
checkable, exactly as Rounds 29/31's own final sanity steps do.**

## Key observation (what made this tractable)

`e(p)`/`nu(k)` (`g2su3_appendix_a_construction.py`, Round 13) are
ALREADY, by construction, LINEAR COMBINATIONS of Cl(7,0) BIVECTORS
`ρ(a)·ρ(b)` (a<b) with EXPLICIT rational coefficients (e.g.
`nu_1=(1/4)(ρ1ρ2-ρ5ρ6)`) — exactly the type of object Round 29's
Clifford-word reducer was built to manipulate combinatorially, just for
a DIFFERENT Clifford algebra (7 generators/Cl(7,0) here vs 6 generators/
`Σ=Λ*(ℂ³)` there). `reduce_clifford_word` is fully generic (only uses
`Z_i²=-1`, `Z_iZ_j=-Z_jZ_i`) — reused UNCHANGED for 7 generators.

Two combinatorial primitives replace the matrix operations:
1. **Commutator**: `[X,Y]` for two bivector-combinations, via
   `reduce_clifford_word` on each 4-index product (both orders) —
   replaces `bracket_e(p,q)`.
2. **Trace-as-dot-product**: since `Tr(e_S^T e_T)=8·δ_ST` for Cl(7,0)
   bivectors (VERIFIED, STEP A, against direct matrices, all `C(7,2)=21`
   pairs plus `C(21,2)=210` cross pairs), `Tr(nu_k^T·M)` for a bivector-
   combination `M` reduces to `8·Σ_{(a,b)}[nu_k's coeff]·[M's coeff]` — a
   pure dot product over explicit coefficient lists — replaces
   `decompose_g2`.

## Construction (code: `g2su3_round32_curvh_combinatorial.py`)

**STEP A:** verify `Tr(e_S^T e_S)=8` (21 pairs) and `Tr(e_S^T e_T)=0`
(S≠T, all `C(21,2)=210` cross pairs) directly against `RHO`-built 8×8
matrices — a ONE-TIME primitive check.

**STEP B:** transcribe `e(p)`/`nu(k)` as `{(a,b):coeff}` dicts from the
`NU` dict's own literal source; self-test against the existing matrices
for exact agreement, all 6 `e(p)` and all 14 `nu(k)`.

**STEP C+D (`build_curv_h_combinatorial`):** compute `[e(p),e(q)]`
combinatorially for all 15 `(p,q)` pairs (asserting the commutator
collapses to PURE bivector terms, no scalar/quartic residual — a genuine
structural check), then extract `curv_h(p,q,k)` for k=1..8 via the dot-
product primitive. Zero matrix construction anywhere in this function.

**STEP E:** cross-check the full combinatorially-rebuilt `curv_h`
against `build_curvature_h_table()` — exact match required, all 17
nonzero entries.

**STEP F:** feed the combinatorial `curv_h` into Round 31's own
matrix-free pipeline (`jach_coeff`/`degree4_coeff` → symbolic `Diff`
assembly) — re-derive `(1,-1/2,-7/4)`, now with `curv_h` ITSELF also
matrix-free.

**STEP G:** final sanity cross-check against the independently-built
numeric `Diff` (Round 28's `build_diff_noncircular`) — the only
Σ-side/`e_action`-based matrix construction in this script.

## Falsifiable Claims

**C1:** `Tr(e_S^T e_S)=8` (21 pairs) and `Tr(e_S^T e_T)=0` (210 cross
pairs) hold exactly for Cl(7,0) bivectors, verified directly against
`RHO`-built matrices.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP A).

**C2:** the `{(a,b):coeff}` transcription of `e(p)`/`nu(k)` matches the
existing matrices exactly, for all 6+14=20 objects.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP B).

**C3:** `build_curv_h_combinatorial()` — using ONLY the combinatorial
commutator + dot-product primitives, ZERO calls to `RHO`/`NU` matrix
products, `bracket_e`, or `decompose_g2` — reproduces `build_curvature_
h_table()`'s full 17-entry table EXACTLY.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP E).

**C4 (the headline result):** feeding the combinatorial `curv_h` into
Round 31's own matrix-free downstream pipeline re-derives
`(1,-1/2,-7/4)` exactly — the ENTIRE derivation chain from raw `NU`-dict/
T-table data is now free of 8×8 matrix construction, except the
verification/cross-check steps (A/B/E/G) explicitly scoped above.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP F, cross-
checked STEP G).

## Kill Conditions

- C1 killed if: skeptic finds the sampled/claimed trace values don't
  actually hold for ALL 21+210 pairs (not just a subset) — verify the
  script's loops genuinely iterate `itertools.combinations(range(1,8),2)`
  (21 pairs) and ALL pairs of pairs (210), not a partial sample.
- C2 killed if: skeptic finds `NU_BIVEC_SOURCE`'s transcription doesn't
  actually match `g2su3_appendix_a_construction.py`'s own `NU` dict
  literal — compare EVERY entry (14 total) side by side against that
  file's source.
- C3 killed if: skeptic finds `build_curv_h_combinatorial()` secretly
  calls `RHO`/`nu(k)`-as-matrix/`bracket_e`/`decompose_g2`/`e_action`
  anywhere — trace every function it calls (`e_bivec_dict`,
  `commutator_combinatorial`, `bivec_product_combinatorial`,
  `dot_product_trace`, `reduce_clifford_word`, `nu_bivec_dict`) and
  confirm none reference an 8×8 matrix.
- C3 killed if: skeptic finds the "commutator collapses to pure bivector
  terms" assertion is not actually checked exhaustively (e.g. silently
  ignores a nonzero non-bivector residual) — verify the `assert len(key)
  == 2` check fires for EVERY key in EVERY commutator, all 15 (p,q)
  pairs, not just a sample.
- C4 killed if: skeptic finds STEP F secretly references the ALREADY-
  KNOWN target values (`1/3`, `-5/12`, `(1,-1/2,-7/4)`) anywhere BEFORE
  they are asserted — the asserts (`ch_tilde_X == sp.Rational(1,3)`
  etc.) are checks on independently-computed values, not the source of
  those values; confirm this ordering in the code.
- C4 killed if: skeptic finds the Round 31 functions this reuses
  (`jach_coeff`, `degree4_coeff`, `expand_quartic_sum_from_T`,
  `expand_H_squared_from_T`) have themselves regressed or secretly
  changed meaning — re-verify against `round31_claim.md`'s own
  description.

## What this does NOT mean

- Does NOT mean STEPs A/B/E/G are matrix-free — they explicitly are NOT,
  and are not claimed to be (see "PRECISE SCOPE STATEMENT" above,
  written specifically to avoid Round 31's own skeptic-caught overclaim
  pattern). The claim is scoped to `build_curv_h_combinatorial()` (STEP
  C+D) and its downstream consumption (STEP F).
- Does NOT independently re-derive `RHO`/`NU`'s own construction from
  octonion multiplication rules or Remark A.2/Lemma A.1's own source —
  the `NU_BIVEC_SOURCE` dict is a direct transcription of ALREADY-
  ESTABLISHED (Round 13) data, not a re-derivation from the primary
  source PDF.
- Does NOT change any previously-established spectrum, index, eigenvalue,
  or `Diff` value from Rounds 4-31 — re-derives the SAME already-known
  numbers via a route with `curv_h`'s own construction ALSO matrix-free,
  cross-checked at every step against the pre-existing matrix-based
  ground truth.
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension or
  which of `M_p`/`Z_p` the preprint's own L4A convention intends — same
  standing open questions as Rounds 26-31.
- Does NOT explain WHY only 3 of the 15 possible index-quadruples are
  ever nonzero in `jach_coeff`/`degree4_coeff` (Round 31's own flagged
  open question) — unaffected by this round, still open.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics + a tool-verified synthesis pass that independently re-ran the
script and independently grepped every matrix-construction symbol by
line number across the whole file, not trusting either skeptic's prose)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL (both + synthesis) | The trace primitive `Tr(e_S^T e_S)=8`, `Tr(e_S^T e_T)=0` verified exhaustively over all `21` diagonal + `C(21,2)=210` off-diagonal bivector pairs (not sampled), hard asserts, independently re-run. |
| C2 | CONFIRMED-REAL (both, hand-verified all 14 entries independently, converging) | `NU_BIVEC_SOURCE`'s transcription matches `g2su3_appendix_a_construction.py`'s own `NU` dict exactly for all 14 generators, confirmed both by manual side-by-side comparison and by STEP B's runtime self-test (matrix reconstruction) for all 6 `e(p)` + 14 `nu(k)`. |
| C3 | CONFIRMED-REAL (both + synthesis, via independent full call-chain trace + grep) | `build_curv_h_combinatorial()` traced to its leaves (`e_bivec_dict→nu_bivec_dict`, `commutator_combinatorial→bivec_product_combinatorial→reduce_clifford_word`, `dot_product_trace`) — zero references to `RHO`/`nu(k)`-as-matrix/`e(p)`-as-matrix/`bracket_e`/`decompose_g2`/`e_action` anywhere. Synthesis independently grepped these symbols by line number across the WHOLE file and confirmed all code-level (non-docstring/print) hits are confined to STEP A/B, none inside the STEP C+D call chain. Commutator-collapse assertion confirmed exhaustive (fires on every nonzero non-bivector residual, all 15 `(p,q)` pairs). |
| C4 | CONFIRMED-REAL (both + synthesis); one non-falsifying test-quality regression found and FIXED | No target-value leakage — `1/3`, `-5/12`, `(1,-1/2,-7/4)` appear ONLY in post-computation assert statements, confirmed by tracing the derivation order. **Both skeptics independently found the SAME regression**: Round 32 originally dropped Round 31's `assert len(ch_tilde_X_values)==1`/`assert len(deg4_X_values)==1` guards before `.pop()`, and dropped the `expected_sumM2`/`expected_H2` dict-equality asserts — a real but non-falsifying hygiene gap (transitively covered by STEP E's exact 17-entry match + STEP G's exhaustive 64-entry matrix check, both of which passed, but weaker standalone diagnosability). **Fixed**: both guards restored, plus `Qm_sum` changed from a hardcoded literal to a genuine T-table computation with an assert (per skeptic 1's suggestion), strengthening the "from raw T-table" framing. |

**Precise Scope Statement table (this round's up-front defense against
Round 31's overclaim pattern): CONFIRMED ACCURATE by both skeptics AND
the synthesis agent independently** — all 7 rows (A/B/C+D/E/F/G) match
what the code actually does, verified via direct code trace, not just
accepting the claim doc's own table. Both reviewers explicitly noted
this round's framing genuinely learned from Round 31's skeptic-caught
overclaim, rather than repeating it.

**FL Response Matrix:** No claim was FALSIFIED. The one real finding
(missing uniformity/equality guards in STEP F) was resolved as a
**Fix** — cheap (9 lines), mechanical, does not touch the numeric result
or its non-circularity, and was applied and re-verified (full re-run,
`EXIT=0`, all values unchanged) before this claim.md was finalized.

**Overall:** combined with Rounds 29 and 31, the entire derivation chain
from raw `NU`-dict/T-table data to `(1,-1/2,-7/4)` is now free of 8×8
Clifford-matrix construction, except explicitly-scoped verification/
cross-check steps (this round's A/B/E/G, matching the same role Rounds
29/31's own final sanity steps already play).
