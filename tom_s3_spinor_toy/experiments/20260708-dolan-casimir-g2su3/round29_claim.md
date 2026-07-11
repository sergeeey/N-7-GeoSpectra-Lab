---
experiment_id: 20260708-dolan-casimir-g2su3
round: 29
date: 2026-07-11
tier: Full-Ladder
status: skeptic_reviewed_C1-C7_confirmed_no_falsification_C1_LC-consistency-framing_softened_C5_structural-interpretation_downgraded_C6_hygiene_fixed
parent: round28 (proved the 3-dim space + basis; coefficients still obtained
  by a numeric 3x3 linear solve against a precomputed Diff matrix)
---

# claim.md — Round 29: "Phase 2" — the correction coefficients
`a=1, b=-1/2, c=-7/4` derived via pure symbolic algebra on closed-form
expressions, without ever solving a linear system against a precomputed
numeric `Diff` matrix

## Background

User's explicit follow-up instruction after Round 28: "продолжай выводить
коэффициенты из первых принципов, Phase 2" — continue the derivation,
specifically the deeper step Round 28's own "Honest Scope" flagged as NOT
attempted: expand the connection via the Nomizu formula + Jacobi identities
so the coefficients "fall out" of the algebra, rather than being obtained
by solving a determined linear system against an already-computed `Diff`.

## Question Type (EstimandOps L0)
[x] Mathematical / Formal — symbolic/algebraic derivation, tested
computationally at every step. NOT empirical, NOT causal.

## Key preliminary finding (reframes the whole task)

The user's original framing ("expand `M_p = Z_p + (1/2)Λ̃^1(Z_p)` per-p,
using Agricola's abstract `Z_p` bare-derivative operator") turned out not
to be directly executable in this project's own matrix-coefficient
realization. Checked directly (STEP A of the script): `M_p` — this
project's Levi-Civita connection matrix, used unchanged since Round 4 —
equals `-Λ̃^{1/2}_m(Z_p)` **exactly**, for all `p=1..6`, where
`Λ̃^{1/2}_m(Z_p) := (1/8) Σ_{j,k} T(p,j,k) Z_j·Z_k` is built **purely from
the T-table** via Agricola's own Lemma 3.2 formula — with **zero**
additional "bare derivative" contribution. This means `M_p` is pure
algebra in this realization; there is no independent per-p "`Z_p`" matrix
to expand. Round 26-28's own "`Z_p`" (via `Ωg = -ΣZp²+C̃h`, Agricola's eq.
9) is a genuinely different, more general/abstract object — accessed only
through that closed-form identity, never as a literal per-p matrix.

This reframes what "Phase 2" can concretely mean here: derive `Σ_p M_p²`
in **closed form directly from the raw T-table combinatorics** (the same
Jacobi-identity-collapse technique Agricola uses for `H²` in Prop 3.2, but
applied to a different quartic sum specific to this project's own
construction), then combine this **algebraically** (not numerically) with
the already-established closed forms for `Ωg`/`C̃h` (Round 26/27's own
`Jac_h`/`Jac_m` machinery) to watch `(1,-1/2,-7/4)` emerge from symbol
manipulation.

## Construction (code: `g2su3_round29_clifford_reduce.py` +
`g2su3_round29_phase2_derivation.py`)

**STEP A:** verify `M_p = -Λ̃^{1/2}_fromT(Z_p)` for all `p`, built purely
from `build_T_table()`, zero use of `nabla_g`/`LEVI_CIVITA_NOMIZU`.

**STEP B:** derive `Σ_p M_p²` in closed form via a from-scratch Clifford-
word reducer (`reduce_clifford_word`, self-tested against an independently
structured recursive reference implementation + 200 random cross-checks),
applied to the raw double-sum `T(p,j,k)T(p,l,m)` — **zero use of the 8×8
`e_action` matrix representation in the derivation**. Result:
`Σ_p M_p² = -¼·Id + (1/12)·X`, `X := Z₁₂₃₄+Z₁₂₅₆+Z₃₄₅₆` (only the scalar
and these 3 quartic monomials are nonzero — everything else, including all
degree-2 bivector terms, collapses to exactly zero).

**STEP C:** derive `H²` the same way, from raw `T(i,j,k)` data (H is
cubic). Result: `H² = 3·Id - 3·X` — independently reproduces Agricola's
Prop 3.2 for this specific case, as a method check.

**STEP D:** decompose `Ch_tilde`, `degree4_term` (Round 26/27's own
`Jac_h`/`Jac_m`-built objects) and `Casimir_su3` (built independently via
`su3_action`) into the SAME `{Id, X}` basis via trace projection, with an
**explicit, asserted zero-residual check** (i.e. verified computationally
that each of these three objects has EXACTLY zero component on any of the
other 12 possible quartic monomials or any degree-2 bivector — not just
that the `{Id,X}`-projected coefficients look reasonable).

**STEP E (the core of "Phase 2"):** assemble
`Diff := Ωg_clean - Ch_tilde - (-Σ Mp²)` **purely symbolically** — using
sympy symbols `H, Id, X` (no numeric 8×8 matrices anywhere in this step),
substitute `X = 3·(Casimir_su3 - Id)`, and extract `(a,b,c)` via
`sp.coeff()`. This is qualitatively different from Round 28's STEP 2
(which solved a numeric 3×3 linear system against an already-computed
`Diff` matrix) — here `Diff` is never computed as a matrix at all before
the coefficients are read off.

**STEP F:** cross-check the symbolically-derived `(a,b,c)` against the
independently-built numeric `Diff` (Round 28's `build_diff_noncircular`) —
a sanity check only, not the source of STEP E's result.

## Falsifiable Claims

**C1 (REVISED post-skeptic — see "Skeptic Verdict" below):** `M_p =
-Λ̃^{1/2}_fromT(Z_p)` exactly, for all `p=1..6`, computed via a code path
(`lambda_tilde_half_from_T`) that never calls `nabla_g` — using only the
T-table + `e_action` (the raw Clifford generator, not the connection).

RESULT: `[VERIFIED-tool]` — confirmed exactly for all 6 indices, asserted
in-script. **Framing caveat (both skeptics independently flagged this):**
`T(p,j,k)` itself is built from `LEVI_CIVITA_NOMIZU` (via `torsion_T`/
`lambda_half`, acting on the 6-dim **vector** representation) — the SAME
underlying primitive `nabla_g`/`M_p` use (acting on the 8-dim **spinor**
representation). So this is a **cross-representation consistency check**
(Agricola's Lemma 3.2, applied to the vector-rep structure constants,
reproduces the directly spin-lifted connection) — not a proof that `M_p`
is independent of Levi-Civita geometry. The underlying finding survives
(`M_p` has no separate bare-derivative piece in this realization); only
the "zero use of Levi-Civita data" framing was overstated.

**C2:** the from-scratch `reduce_clifford_word` reducer is correct (cross-
checked against an independently-structured reference implementation over
200 random cases, plus 3 hand-derived cases).

RESULT: `[VERIFIED-tool]` — all pass.

**C3:** `Σ_p M_p²` and `H²`, each derived purely combinatorially from raw
T-table data (zero matrix representation used in the derivation), exactly
match the SAME quantities computed via direct 8×8 matrix multiplication.

RESULT: `[VERIFIED-tool]` — both exact matches, asserted in-script
(STEP B, STEP C).

**C4:** `Ch_tilde`, `degree4_term`, `Casimir_su3` each decompose EXACTLY
(zero residual) into `span{Id, X}`.

RESULT: `[VERIFIED-tool]` — asserted in-script for all three (STEP D).

**C5 (REVISED post-skeptic — see "Skeptic Verdict" below; bonus finding,
not previously noted in Rounds 26-28):** `Ch_tilde == Casimir_su3`
**exactly**, as 8×8 matrices (both equal `Id + X/3`).

RESULT: `[VERIFIED-tool]` — confirmed via direct matrix subtraction,
asserted in-script. **Downgraded interpretation (both skeptics
independently flagged this):** this is a verified numerical identity in
THIS project's specific SU(3)-generator normalization (AHL2023 Remark
5.2), not proven normalization-independent from Agricola's Prop 3.3 +
SU(3)-Casimir eigenvalues alone — that derivation is not attempted here.
The matrix identity itself is real and unaffected; only the "structural
finding" / "this is WHY Casimir_su3 appears in Diff" language was
overselling what was actually shown.

**C6 (the headline result; hygiene-fixed post-skeptic — see below):**
assembling `Diff` purely symbolically (sympy symbols, `sp.coeff()`
extraction, `X` substituted for `Casimir_su3`) gives EXACTLY
`(a,b,c) = (1, -1/2, -7/4)` — without ever constructing `Diff` as a
numeric matrix or solving a linear system against one.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP E).
**Hygiene fix (both skeptics independently flagged this):** the original
version hand-transcribed STEP B/C's own closed-form results
(`H²=3·Id-3·X`, `ΣM_p²=-¼·Id+X/12`) as literal constants in STEP E instead
of consuming `H2_coeffs`/`sumM2_coeffs` (the dicts STEP B/C actually
compute) programmatically — a code-hygiene gap (a future change to STEP
B/C could silently desync from STEP E, caught only by the final
`(a,b,c)==target` assertion, not directly). Fixed: STEP E now asserts
`H2_coeffs`/`sumM2_coeffs` equal explicit expected dicts BEFORE building
the symbolic expression, wiring the dependency in-code. Re-run confirms
the fix changes nothing numerically (the hand-transcribed values were
already exactly correct) — this was a robustness improvement, not a
correction of an error.

**C7:** the symbolically-derived `a·H + b·Id + c·Casimir_su3` matches the
independently-built numeric `Diff` (Round 28's own construction) exactly.

RESULT: `[VERIFIED-tool]` — confirmed, asserted in-script (STEP F).

## Kill Conditions

- C1 killed if: skeptic finds `lambda_tilde_half_from_T` secretly imports
  or depends on `nabla_g`/`LEVI_CIVITA_NOMIZU` data anywhere (would make
  the "pure T-table" claim false) — check `word_matrix`'s only dependency
  is `e_action` (the raw Clifford generator action), and `T` comes only
  from `build_T_table()`.
- C2 killed if: skeptic finds the reference implementation shares a bug
  with the primary implementation (e.g. both have the same sign error) —
  should hand-verify at least 2 of the 3 manually-derived test cases
  independently, not just trust the cross-check count.
- C3 killed if: skeptic finds `expand_quartic_sum_from_T`/
  `expand_H_squared_from_T` secretly uses the 8×8 matrix representation
  anywhere in the SUM itself (only the cross-check afterward should use
  it) — check `word_matrix` calls appear ONLY in `coeffs_to_matrix`
  (post-hoc reconstruction) and the STEP A/F cross-checks, never inside
  the accumulation loops of STEP B/C.
- C4 killed if: skeptic finds `decompose_in_scalar_quartic_basis`'s
  residual check is not actually exhaustive (e.g. silently skips some
  basis elements) — verify the function iterates ALL 15 possible quartic
  monomials + all 15 possible degree-2 bivectors, not just the 3 quartics
  used in the final basis. **NOTE (self-flagged before skeptic review):**
  the current `decompose_in_scalar_quartic_basis` implementation only
  explicitly projects onto `{Id, Z1234, Z1256, Z3456}` and asserts the
  RESIDUAL (M minus this reconstruction) is exactly the zero matrix — this
  IS exhaustive in effect (a zero 8×8 residual means no other basis
  element, of any degree, has any component), but a skeptic should verify
  this residual-based reasoning is correct rather than assume the
  4-element projection alone is sufficient.
- C5 killed if: skeptic finds `Ch_tilde == Casimir_su3` is an artifact of
  THIS specific numeric realization (e.g. depends on a normalization
  choice) rather than a structural fact — should check whether this
  identity is expected from Agricola's own Prop 3.3 (`C̃h`'s definition)
  combined with the known SU(3)-Casimir eigenvalues on `Σ`'s
  decomposition, or whether it looks coincidental.
- C6 killed if: skeptic finds STEP E secretly reuses numeric information
  from `Diff_numeric` (e.g. `deg4_scalar`/`ch_tilde_scalar` computed in
  STEP D are themselves derived using information that traces back to the
  target answer) — trace `ch_tilde_scalar`, `ch_tilde_X`, `deg4_scalar`,
  `deg4_X` back to their source (STEP D's trace-projection of `Ch_tilde`/
  `degree4_term`, built from `curv_h`/`jac_h`/`jac_m`, NOT from `Diff`) —
  confirm zero circular dependency.
- C7 killed if: skeptic finds `build_diff_noncircular` (imported from
  Round 28) has itself regressed or changed meaning since Round 28's own
  skeptic-reviewed fix — re-verify it still matches Round 28's
  `round28_claim.md` description.

## What this does NOT mean

- Does NOT mean "`Z_p`" (Agricola's abstract canonical/t=0 bare-derivative
  operator) has been independently constructed as a matrix — it has NOT;
  STEP A's finding is that it is NOT needed / not directly expressible as
  a per-p matrix in this project's realization at all. The "Ωg - C̃h"
  route (Round 26/27's own construction, reused unchanged here in STEP D)
  remains the only way this project accesses that quantity.
- Does NOT reprove Agricola's Theorem 3.2 in general — this is a
  computation specific to THIS S⁶=G₂/SU(3) case, using its own T-table/
  curv_h data, not a general symbolic proof for arbitrary naturally
  reductive spaces.
- Does NOT change any previously-established spectrum, index, eigenvalue,
  or Diff VALUE from Rounds 4-28 — this round re-derives the SAME already-
  known numbers via a structurally different (symbolic, not linear-solve)
  route, and cross-checks agreement (STEP F).
- Does NOT resolve the preprint's `8/45 vs ~1.03` norm-ratio tension or
  which of `M_p`/`Z_p` the preprint's own L4A convention intends — same
  standing open questions as Rounds 26-28.
- Does NOT mean this is now a "closed-form proof from Agricola's Theorem
  3.2 alone" in the fully general sense — the specific numeric values of
  `T(p,j,k)`/`curv_h` for THIS S⁶ geometry are used throughout (via
  `build_T_table()`/`build_curvature_h_table()`), not a fully abstract,
  geometry-independent symbolic argument.

## Skeptic Verdict (FL Step 8a, 2026-07-11, two independent context-blind
skeptics + a tool-verified synthesis pass that independently re-ran the
script AND independently re-traced the two most serious concerns by
reading the exact lines of code in question)

| Claim | Verdict | Note |
|---|---|---|
| C1 | CONFIRMED-REAL, framing WEAKENED (both skeptics + synthesis) | `M_p=-Λ̃^{1/2}_fromT(Z_p)` holds exactly; code-level kill condition satisfied. But `T` traces to `LEVI_CIVITA_NOMIZU` via a different representation (vector, not spinor) — a cross-representation consistency check, not an independence proof. Fixed: framing softened in-script and here. |
| C2 | CONFIRMED-REAL | Reducer hand-traced on 7 combined cases (including manual `(Z₁Z₂Z₃)²=+1`) by both skeptics + 200 random cross-checks against a structurally distinct reference implementation + end-to-end matrix validation via STEP B/C. |
| C3 | CONFIRMED-REAL | Both skeptics + synthesis independently confirmed the accumulation loops in `expand_quartic_sum_from_T`/`expand_H_squared_from_T` touch ONLY `T.get(...)` and `reduce_clifford_word` — `word_matrix`/`e_action` appear only in post-hoc cross-checks. |
| C4 | CONFIRMED-REAL | Zero-residual reasoning independently confirmed logically sound by both skeptics: a zero 8×8 residual means M IS exactly that combination, full stop, regardless of what other basis elements exist. |
| C5 | CONFIRMED-REAL (matrix identity); WEAKENED (structural interpretation) → downgraded | `Ch_tilde==Casimir_su3` holds exactly, independently re-confirmed by synthesis's own re-run. "Structural finding"/"this is WHY" language was overselling — this is a verified numerical coincidence in this project's specific SU(3)-generator normalization, not derived from Prop 3.3 + Casimir eigenvalues independent of normalization. Fixed: language downgraded. |
| C6 | CONFIRMED-REAL (technical); WEAKENED (interpretive framing) → hygiene-fixed | Non-circularity independently re-verified by both skeptics + synthesis (traced `ch_tilde_scalar/X`, `deg4_scalar/X`, `scalar_term` back to `curv_h`/T-table/`su3_action`, zero path to the target formula). Hardcoded `H2_closed_sym`/`sumM2_closed_sym` literals flagged as a code-hygiene gap by both skeptics; synthesis independently confirmed via its own fresh run that these literals exactly matched STEP B/C's actual computed output. Fixed: wired via explicit dict-equality assertions. |
| C7 | CONFIRMED-REAL | `build_diff_noncircular` re-read by both skeptics + synthesis, confirmed unchanged from Round 28's post-fix version, no reference to the target formula anywhere in its body. (Cosmetic note, Skeptic 2: the function's `Casimir_su3` parameter is accepted but unused inside the body — dead parameter, does not affect correctness.) |

**FL Response Matrix:** No claim was FALSIFIED (unlike Round 28, where
C4/C5 had a genuine circularity requiring a code fix). All issues found
here were WEAKENED (interpretive/framing overreach on claims that are
technically true) — handled per the response matrix as
**Accept-with-documented-caveat** (C1, C5 framing) or a cheap **Fix**
(C6 hygiene). None required reworking or retracting the headline result.

**Overall:** Round 29 achieves its stated goal — the coefficients
`(1,-1/2,-7/4)` emerge from `sp.coeff()` on a symbolic expression built
from independently-computed geometric quantities (`Ch_tilde`,
`degree4_term`, `scalar_term` from `curv_h`+T-table+Jacobi identities,
`Casimir_su3` from `su3_action`), NOT from a numeric linear solve against
a pre-computed `Diff` — the previous circularity mode (Round 28's fixed
bug) does not recur. The round is promotable in its corrected form.
