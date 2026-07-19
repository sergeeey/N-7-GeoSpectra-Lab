# P1 — Claim-to-Source Matrix

**Purpose:** one row per sentence-level claim the eventual manuscript
prose is licensed to make. Built BEFORE prose drafting specifically to
prevent scope drift — every sentence in the future manuscript should trace
to exactly one row here; any sentence that doesn't fit a row is either an
overclaim or a missing row (fix the row, don't stretch the sentence).

**Verification note:** every "Computation" and "Independent check" column
below was re-confirmed against the cited source during this pass (not
copied from `P1_FROZEN_VERDICTS_TABLE.md` without re-checking) — this
matrix is more granular than that table, splitting some rows there into
multiple claim-level rows here.

| # | Claim (sentence-level) | Scope | Primary evidence | Computation | Independent check | Status |
|---|---|---|---|---|---|---|
| C1 | No continuous symmetry inside `so(8)`, induced by the `S³×S⁶` geometry itself, commutes with the geometric `G₂` action on the octonion fiber. | `G₂`-equivariant, intrinsic/induced symmetries only | G102 `decision.md`, P3 result (`dim c_{so(8)}(g₂)=0`) | 9 pre-registered tests (8 predictions + 1 control), residuals at machine epsilon | Internal cross-check (skeptic-pre-answered, 4 anticipated objections addressed) | `[ESTABLISHED]` |
| C2 | Triality is realized as an outer automorphism only; no inner symmetry induced by the geometry permutes the three channel labels. | Same as C1 | G102 `decision.md`, P4 result (2-dim abelian centralizer, inner) | Same 9-test suite | Same | `[ESTABLISHED]` |
| C3 | `SO(4)×SO(4)` (from the octonion `H⊕Hℓ` split) algebraically distinguishes all three triality channels (`Hom=0` pairwise). | External to `g₂`; a specified algebra, not a physical claim | Round119 `decision.md`, `L3B_SPIN8_INTERFACE_SPEC.md` §1, §7 | Explicit block-chirality matching (source document) | Mandatory skeptic review (3 issues found and fixed) | `[ESTABLISHED, algebraically]` |
| C4 | `su(3)⊕u(1)⊕u(1)` (the centralizer construction) also gives `Hom=0` for all three off-diagonal channel pairs — a second, structurally distinct route to the same milestone. | External to `g₂`; same caveat as C3 | Round124 `decision.md` | Direct Schur-lemma non-isomorphism (`Hom` table) | Skeptic review (`CONFIRMED-REAL`) + independent re-run with 2 basis-rotation checks by the author | `[ESTABLISHED, algebraically]` |
| C5 | `SO(4)×SO(4)` and `su(3)⊕u(1)⊕u(1)` are genuinely different structures (`PARTIAL_OVERLAP`, 12-dim vs 10-dim), but share an exact, non-generic 3-dim abelian `u(1)³` core. | Comparison of C3 and C4's underlying algebras only | Round125 `decision.md` | Two independent SVD methods, tolerance-swept 1e-4→1e-12 | Skeptic-reviewed `CONFIRMED` | `[ESTABLISHED]` — **must accompany any use of "independent" re: C3/C4** |
| C6 | Both C3 and C4 require breaking `G₂` to be realized physically, and `G74A` Lemma B's exact-`G₂`-only proof technique for `dim ker=1` does not survive any nonzero `G₂`-breaking perturbation. | The proof-METHOD's domain of applicability, not a claim about the physics itself | Round119 `decision.md` (citing `G74A`'s own re-read) | N/A — a re-read/rubric-application audit, no new computation | Mandatory skeptic review | `[ESTABLISHED, re: proof-method limitation]` |
| C7 | Whether `K` (either candidate algebra) acts *globally* on the actual compactification (not just the fiber) is unresolved and depends on unpublished external input (Tom Lawrence's "Part 5"). | Gate 2 of the `L3B_SPIN8_INTERFACE_SPEC.md` §7 gate table | Source document §7, read directly | N/A | N/A — explicitly named by the source itself as external-dependent | `[OPEN — blocked on external input, not falsified]` |
| C8 | `ℂ⊗8_v` and `Σ` are isomorphic as complex `su(3)`-representations (abstract type: `1⊕1⊕3⊕3̄`). | Pure representation theory of two objects constructed elsewhere in the project | Round127 `decision.md` | End-dimension identity `Hom(V,V)=4+a²+b²`, `a+b=2`, both sides `Hom=6` forces `a=b=1` | `[C₂,Xᵢ]=0` verified to machine precision; skeptic review (found and required the End-dim argument over a weaker Casimir-only argument) | `[ESTABLISHED]` |
| C9 | An explicit, invertible intertwiner `S` realizing the C8 isomorphism exists and has been constructed. | Same objects as C8 | Round128 `decision.md` | Cartan-Weyl root alignment + nonlinear least-squares `μ`-fit + Sylvester-equation Hom search, exhaustive over all 12 members of `Aut(su(3))` | `iso_residual~1e-15` for every one of the 12 candidates; two bugs found and fixed (skeptic-caught `Minv`/`M` inversion; self-caught reshape-order mismatch) | `[ESTABLISHED]` |
| C10 | Round127 itself never found or claimed an explicit `S` — it is not independent corroboration of C9. | Provenance/citation discipline for C8+C9 | `results_round127.json` (`isomorphism_found=false`, `iso_residual=null`) | N/A — direct read of the JSON output | `SUPERSEDED_RESULTS.md` SR8 | `[ESTABLISHED — citation constraint, not a physics claim]` |
| C11 | Transporting round124's `su(3)`-centralizer (C4) through the C9 intertwiner and comparing to `G15`'s established `BmL` operator gives no clean match, for any of the 12 valid choices of `S`. | Specifically round124's centralizer vs. `BmL` — not a claim about any other structure or about `B-L`'s uniqueness | Round128 `decision.md` (all-12 scan) | 12 least-squares fits, relative residuals `{0.53,...,1.00}`, threshold `1e-4` | Exhaustive by construction (all 12 valid `S` checked, not a sample) | `[ESTABLISHED — negative, exhaustive within its stated scope]` |
| C12 | `B-L` itself is not uniquely defined among a `dim≥3` admissible family of candidate operators. | An independent caveat on C11's target object, not on C11's method | Round61-BL (cited in round124 `decision.md` Relaxation Map) | Not re-verified in this pass — cited, not re-derived | Not independently re-checked this pass | `[CITED, not re-verified this pass — flag if used as a load-bearing premise]` |
| C13 | The untwisted (Levi-Civita) `S³` connection gives the full internal `S³×S⁶` Dirac operator zero zero-modes; no selection principle is known for the torsion parameter `t`. | The FULL product operator on `S³×S⁶` — explicitly NOT the `S⁶`-only operator of the separate round59/`N_gen=3` chain | `OPEN_BLOCKERS.md` OB1/KT-8 | Confirmed 3×, cross-checked against literature | 4 independent internal mechanism-search attempts (rounds 114-117), all null or falsified | `[ESTABLISHED — negative, PARKED not REJECTED]` |

## Explicitly out of scope for this matrix (belongs to a different chain)

- `N_gen=3` and its own kernel-rank/index chain (G73/G74A/G74B, round59) —
  tracked in the separate `ROUND59_EXTERNAL_VERIFICATION_PACKET/`, not
  here. No row above depends on it (verified by direct grep of both
  `P1_FROZEN_VERDICTS_TABLE.md` and `P1_NOGO_MANUSCRIPT_OUTLINE.md` during
  this same hardening pass — every "round59" mention in those files is
  either the scope-fence statement or an explicit non-conflation
  instruction, never a premise).
- `λ` (free coupling parameter) and `safe_for_runtime` — standing project
  fences, not addressed by any claim above.

## How to use this matrix when drafting prose

1. Before writing a sentence, find its row number here.
2. If no row fits, do not write the sentence yet — either it's an
   overclaim (drop it) or the matrix is missing a row (add the row here
   first, with its own evidence/computation/check columns filled in).
3. Every `[ESTABLISHED]` claim in prose must carry the same scope
   qualifier shown in this matrix's Scope column — do not let the scope
   qualifier get lost in translation from table to sentence.
