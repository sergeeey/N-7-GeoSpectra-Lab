# C104 decision — summing all four D^1 components DOES produce mixing, in a clean, structured way

**Verdict:** `MIXING_FOUND_AT_ALL_K__SUMMING_COMPONENTS_PRODUCES_GENUINE_MIXING`
**Status:** RESOLVED — the exploratory alternative construction genuinely differs from C100's single-component result

---

## Summary

Built all four `M_k^{(a,b)}` matrices (`a,b ∈ {+1/2,-1/2}`) for
`k=1,2,3`, using C100's own CG-assembly method generalized to
arbitrary `(a,b)` (only the fixed `(1/2,1/2)` choice changes; the rest
of the construction is identical), summed them elementwise, and
checked the resulting `M_k^sum`'s structure — the exact test C100 used
to characterize its own single-component result as an injective
embedding.

**Mixing is found at every `k` tested, and the pattern is remarkably
clean: every column has EXACTLY 4 nonzero entries — not "some
columns show mixing, others don't," but a uniform 4-fold structure at
every single input state, every level.**

## Predictions vs outcome

| # | Prediction | Outcome |
|---|---|---|
| P0 (reuse sanity) | the already-certified `(1/2,1/2)` component still cross-checks against the independent Wigner-3j path | **PASSES** — exact match at every `k`. |
| P1 (the actual question) | `M_k^sum` has more than `dim_k^2` nonzero entries for at least one `k` | **HOLDS at every `k` tested** (`k=1`: 16 vs baseline 4; `k=2`: 36 vs 9; `k=3`: 64 vs 16 — exactly `4×dim_k^2` in every case). |
| P2 (generic vs sparse mixing) | is mixing widespread or limited to a few states? | **Fully generic** — EVERY column (every input state) shows exactly 4 nonzero entries, at every `k`. |

## The precise structure, beyond the coded P1 check

`M_k^sum` has exactly `4 × dim_k²` nonzero entries at every `k` tested
— i.e. **every single one of the four `(a,b)` components contributes
exactly one nonzero entry to every column, and no two components ever
land on the same output position.** This is confirmable directly from
the numbers: 4 components × (each individually injective, per C100's
own established pattern generalized here) = at most `4×dim_k²`
nonzero entries in the sum if no two components' images ever collide
for the same input; finding EXACTLY `4×dim_k²` (not less) confirms
zero collisions occurred, at every `k`, every input state tested.

**Physical reading:** each of the four `(a,b)` choices shifts
`(m_q,m_p)` by a different combination of `±1/2` in each coordinate —
four genuinely different target directions in the level-`(k+1)`
magnetic-number lattice. That these four shifted targets never
coincide for any tested input is a clean, checkable
consequence of the CG selection rules, not a coincidence requiring
further explanation — but it was not assumed, it was verified
directly, exactly as this round's own kill_criterion required.

## What this establishes

- `M_k^sum` is qualitatively DIFFERENT from C100's own single-component
  `M_k` — it genuinely mixes (spreads each input state across 4
  distinct outputs), not an injective embedding.
- This is NOT "generic messy mixing" — it has an exact, uniform,
  4-fold structure at every level and every state, suggesting the
  underlying mechanism (four disjoint CG-selection-rule targets) is
  itself clean and potentially provable in closed form, not merely an
  empirical pattern requiring further numerical checks.

## What this cannot show

- Does not establish `M_k^sum` (summing all four components) is the
  physically correct multiplication operator — one candidate among
  several, exactly as unverified as the single-component choice it
  replaces (see claim.md's Counterfactual Frame).
- Does not build a new `D_PW` using `M_k^sum` — a natural follow-up
  (would the exactly-real-spectrum property survive a genuinely
  mixing off-diagonal block, not just an injective one?), not
  attempted this round.
- Does not resolve `r`'s role — same untouched ansatz as C101-C103.
- Does not change `N_gen=3`'s CONDITIONAL status.
- Does not solicit or reference Tom Lawrence's unpublished Part 5.

## Verification

- `ruff check experiments/20260812-c104-summed-components-mixing-test/`
  — clean, 0 errors.
- P0 cross-checked the already-certified component against the
  independent Wigner-3j path (same method C100 used), not merely
  assumed correct by generalization.
- The "exactly 4 per column" finding was read directly from the
  computed `per_column_nonzero_counts` list for every `k`, not
  inferred from the aggregate count alone.
