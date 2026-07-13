# Round55a.1-SU3Normalization Claim — the last narrow gate before Round 56

**Date:** 2026-07-13
**FL tier:** [x] Standard (direct computation on already-built fixed matrices)
**Question type:** [x] descriptive

---

## Prior Result Gate

Direct continuation of Round 55a, per the reviewer's own explicit
narrow scope: "На четырёх fibre-типах вычислить непосредственно
-Σρ(ν_k)² и сравнить с Bourbaki-значением." Status: OPEN → this round.

---

## Claim

The SU(3) fibre Casimir, computed DIRECTLY from `build_su3_matrix64`
(the actual matrices this project's own `Ms[p]`/`su3_curvature_term`
machinery is built from — not the abstract `su3_casimir` formula in
isolation), gives exact eigenvalues `{0, 4/3, 10/3, 3}` on the full
64-dim `Σ⊗Σ` fibre — **exactly matching** the Bourbaki-self-norm
`su3_casimir` formula values for `(0,0)→0`, `(1,0)/(0,1)→4/3`,
`(2,0)/(0,2)→10/3`, `(1,1)→3`, with **no rescale needed**. Scenario A
confirmed directly, not by analogy with the G₂ side. Round 52's `-3`
is correct as originally stated.

---

## Kill criterion

| Kill condition | Threshold |
|---|---|
| Direct fibre Casimir eigenvalue ≠ any `su3_casimir` formula value (Scenario A fails) | any unmatched eigenvalue among the 4 relevant σ-types |
| `3/2` found instead of `3` (Scenario B) | `3/2 ∈` eigenvalue set |
| Fibre Casimir operator not Hermitian | non-Hermitian result |

All checked: PASS (Scenario A confirmed, Scenario B ruled out).

---

## IMPORTANT — flagged for the reviewer's own review before Round 56 is finalized

Re-deriving the exceptional set independently (not just re-stating the
reviewer's own Scenario-A arithmetic), using Round 55's own formula
`λ²_min(ρ) ≥ C₂(ρ) - 3 - K_cert·√C₂(ρ)` **exactly as it was calibrated
and empirically positive-controlled in Round 55** (K_cert was
specifically converted, dividing by `√2`, so that it pairs with
**Bourbaki** `C₂(ρ)` directly — confirmed by Round 55's own STEP 4
positive control, which used `√C₂_Bourbaki(7)=√4=2`, explicitly
commented `"K_cert (Bourbaki units)"` in the script, and passed with
real margin), gives threshold `C₂_Bourbaki(ρ) > 7.460` directly — with
**no further doubling** — yielding exceptional set **`{7}` only** (not
`{7,14,27,64}`).

This differs from the reviewer's own Scenario-A conclusion, which
applied an additional `×2` conversion on top of the `7.460` threshold.
Our reading: that additional doubling double-counts the native→Bourbaki
conversion Round 55 already performed when deriving `K_cert` — `C₂(ρ)`
in Round 55's own formula was already meant to be, and was empirically
verified to be (via the positive control), the Bourbaki value, not the
native one requiring a further conversion.

**Not asserted as final** — flagged explicitly for the reviewer's own
re-check before treating any exceptional set as settled, given the
genuine subtlety and this project's own standing discipline that
normalization claims need independent, tool-verified confirmation, not
one party's unchecked arithmetic. See `decision.md` for the full
re-derivation shown step by step.

---

## Fence

- λ = FREE_COUPLING_PARAMETER
- GEOMETRY_AGNOSTIC = True
- safe_for_runtime = False

---

## Verdict

See `decision.md`.
