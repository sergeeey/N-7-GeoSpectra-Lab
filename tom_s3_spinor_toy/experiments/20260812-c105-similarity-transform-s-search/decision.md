# C105 decision — the cleanest candidate mechanism is ruled out; a real, reusable partial result survives

**Verdict:** `BLOCK_DIAGONAL_S_RULED_OUT__CROSS_LEVEL_CONDITION_GENUINELY_INCONSISTENT`
**Status:** RESOLVED — genuine negative result, with a real positive partial finding embedded

---

## Summary

Searched for the candidate similarity transform `S` (named in
C101's own pearl-registry open question) that would explain why the
coupled `D_PW` spectrum comes out exactly real across three
qualitatively different constructions (C101, C102, C103), by testing
the cleanest, most natural candidate: a block-diagonal, per-level,
`r`-untouched transform built from anti-Hermitianizing each diagonal
block `D̄_k` individually.

**Part of this candidate is confirmed correct** (P0): the binomial-
normalization `S_p(k) := diag(1/√C(k,p))` simultaneously
anti-Hermitianizes all three `p`-space generators `l_{e1}(k)`,
`l_{e2}(k)`, `l_{e3}(k)`, for `k=1,2,3` — and `rmult_i` (the
`r`-space generators) are ALREADY anti-Hermitian, needing no fix at
all. So `S_p(k)⊗I_r` genuinely Hermitianizes each diagonal block
`D̄_k` on its own, for every level.

**But the cross-level extension fails, genuinely, not ambiguously**
(P1/P2): the one remaining degree of freedom per level (an overall
positive scalar `c`, forced unique-up-to-scale by Schur's lemma since
`l_{e_i}(k)` is an irreducible `su(2)` representation) cannot be
chosen consistently across levels. The compatibility condition
`c²·P₂·M₁ = M₁·P₁` (needed for the off-diagonal `M_1` block to also
come out correctly under the same similarity transform) produces FOUR
independent nonzero constraint equations, requiring **two genuinely
different values of `c`** (`c=1` from two entries, `c=√2` from the
other two) — not underdetermined, not a rounding artifact, an actual
contradiction.

## Predictions vs outcome

| # | Prediction | Outcome |
|---|---|---|
| P0 (reuse sanity) | `S_p(k)⊗I_r` individually Hermitianizes `D̄_k` for `k=1,2,3` | **PASSES** — confirmed formally for all three, plus `rmult_i` confirmed already anti-Hermitian (no `r`-fix needed). |
| P1 (single `c` exists) | one scalar solves the cross-level condition | **FAILS.** |
| P2 (genuinely inconsistent vs underdetermined) | distinguish the failure mode | **Genuinely inconsistent** — exactly 2 distinct required values (`1`, `√2`), not an unconstrained/underdetermined system. |

## What this genuinely establishes

1. **A real, reusable, closed-form fact**: `S_p(k) = diag(1/√C(k,p))`
   is THE (unique up to overall scale, per Schur's lemma) transform
   Hermitianizing C85's own certified `l_{e_i}(k)` generators at any
   single level — connects directly to and confirms C96's own earlier,
   independently-motivated derivation of the same formula (there,
   found while trying to build a unitary basis for `build_d2_matrix`,
   then discarded for an unrelated calibration reason; here, re-found
   from a completely different starting question and kept, since it
   answers THIS round's own question).
2. **The cleanest candidate explanation for the real-spectrum property
   is RULED OUT**: no block-diagonal, `r`-untouched, per-level-scalar
   similarity transform can Hermitianize the full coupled `D_PW`. The
   real-spectrum property itself remains completely intact and true
   (C101, C102, C103 all stand unchanged) — only this SPECIFIC
   candidate mechanism for explaining it is killed.

## Kill Analysis (per this project's own Anti-Overfitting Gate discipline)

**Killed:** the hypothesis "a block-diagonal similarity transform,
built purely from within-level Hermitianization with one free scalar
per level, explains the real-spectrum property." A single, cheap,
exact symbolic computation (4 constraint equations, 2 incompatible
values) is sufficient to kill this — no ambiguity.

**NOT killed:** (a) the real-spectrum property itself — still true,
three times confirmed; (b) the general "similarity to Hermitian"
framing — only the BLOCK-DIAGONAL, `r`-untouched, single-scalar-per-
level special case was tested; a genuinely more general `S` (mixing
levels, or with more structure within each level than a single
scalar) has not been ruled out; (c) the individual-level `S_p(k)`
formula, which is confirmed correct and may still be a necessary
INGREDIENT of whatever the true, more general `S` turns out to be.

**Relaxation map (Minimal Relaxation Rule — one assumption changed
per candidate, not attempted further this round):**

| Assumption in the killed candidate | Possible relaxation |
|---|---|
| `S` is block-diagonal across levels | Allow `S` to have nonzero off-block-diagonal structure (genuinely mixes levels) |
| Per-level freedom is a single scalar `c_k` | Allow a more general per-level transform beyond scalar rescaling of `S_p(k)` (though Schur's lemma genuinely forces uniqueness-up-to-scalar for `l_{e_i}(k)` alone — any additional freedom would need to come from acting differently on `q` or `r`, not `p`, since those factors were held at `I` throughout) |
| `r` is left untouched by `S` | Revisit whether `S` needs a nontrivial `r`-component after all -- ties back to the still-open "r's role" question from C99-C104 |

None of these relaxations is pursued in this round.

## What this cannot show

- Does not identify the true mechanism (if one exists) explaining the
  real-spectrum property.
- Does not test any of the three relaxations named above.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c105-similarity-transform-s-search/`
  — clean, 0 errors.
- All computations exact symbolic (sympy), not numerical approximation
  — the "genuinely inconsistent" finding (`c=1` vs `c=√2`) is an exact
  algebraic fact, not a floating-point artifact.
- This round's formal script independently re-derives the preliminary
  scratch-exploration numbers disclosed in claim.md, from a clean
  script rather than ad hoc interactive commands -- confirms the
  scratch work was not itself in error.
