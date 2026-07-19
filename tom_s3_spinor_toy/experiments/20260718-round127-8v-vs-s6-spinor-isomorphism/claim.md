# Round127 — Claim

**User-requested:** "resolve the `8_v` vs `S⁶` spinor basis-identification
gap" — the prerequisite flagged in round126's own Relaxation Map, needed
before any literal (not just ratio-based) comparison between round124's
`su(3)`-centralizer charges and this project's established `B-L`/`Y`
formulas can be made.

## Prior Result Gate — precise statement of what the two objects actually are

Read the exact construction of both objects (not assumed from memory):

- **`8_v`** (round124/G102): the octonion **vector** representation of
  `SO(8)` — literally `𝕆=ℝ⁸`, a **real** 8-dimensional vector space.
  `su(3)` acts via `G102.stabilizer_basis`, 8 real antisymmetric 8×8
  matrices (the isotropy algebra of a point in `Der(𝕆)`).
- **`Σ`** (G14/G15's "`S⁶` spinor"): built via `G10-B → G11 → G14/G15` as
  the `Spin(6)` **Dirac spinor** representation, constructed by Clifford-
  lifting `su(3)`'s action on the 6-dimensional **tangent space** of `S⁶`
  (`so(6)` generators) into an 8×8 action on `Λ•(ℂ³)` via
  `J_spinor(a,b)=[Γ_a,Γ_b]/4` — a genuinely **complex** 8-dimensional
  vector space (`ℂ⁸`, matching `2³=8` for 3 fermionic modes).

**These are categorically different kinds of object** (real 8-dim vs.
complex 8-dim) — not merely "the same space in a different basis." A
literal, naive comparison is not well-posed as stated.

## L0 gate (EstimandOps)

**Question type: Descriptive.** Is `ℂ⊗8_v` (the complexification of
round124's octonion vector representation, restricted to `su(3)`)
isomorphic, as a **complex** `su(3)`-representation, to `Σ` (G14/G15's
`Spin(6)` spinor, restricted to the same `su(3)`)? If so, construct the
explicit isomorphism and use it to directly compare round124's
centralizer generators against G15's established `B-L` matrix — a
literal matrix comparison, not the flawed ratio-scan of round126.

## Falsifiable claim

1. `ℂ⊗8_v|su(3)` and `Σ|su(3)` both decompose as `3⊕3̄⊕1⊕1` (complex
   dimension 8) — an abstract representation-theory fact checkable via
   Hom-space dimension (expect `Hom_ℂ(ℂ⊗8_v, Σ) = 6`, matching G102's own
   `Hom_su(3)=6` self-intertwiner count, since isomorphic-type reps have
   the same-dimensional intertwiner space regardless of real/complex
   working field).
2. Within this 6-complex-dimensional Hom space, an **invertible** element
   `S` exists (a genuine isomorphism, not just an intertwiner) — generic
   elements of a Hom space between isomorphic irreducible-type modules are
   expected to be invertible; this must be checked, not assumed.
3. Transporting round124's 2 centralizer generators through `S` into
   `Σ`'s basis and comparing against G15's explicit `B-L` matrix (`BmL`,
   diagonal, entries `{-1,-1/3,-1/3,-1/3,1/3,1/3,1/3,1}`) gives either a
   literal proportionality match, a non-match, or an ambiguous result (`S`
   not unique — see kill criteria).

## Pre-registered kill criteria

| Outcome | Verdict |
|---|---|
| `Hom_ℂ(ℂ⊗8_v, Σ) ≠ 6` | **STRUCTURE_MISMATCH** — the two objects are NOT abstractly isomorphic `su(3)`-modules as expected; stop, do not force an isomorphism |
| `Hom` is 6-dim but no element is invertible (all singular) | **NO_ISOMORPHISM_IN_HOM_SPACE** — genuinely surprising, would need investigation, not expected |
| An invertible `S` is found, but round124's centralizer transported through it does NOT match any linear combination of `BmL` (residual large) | **NO_LITERAL_MATCH** — report honestly; the abstract isomorphism exists but the specific centralizer direction isn't `B-L` |
| An invertible `S` is found and a linear combination of the transported centralizer generators matches `BmL` (or a scalar multiple) to high precision | **LITERAL_MATCH_FOUND** — the strongest possible result; report the exact combination and scalar |
| Multiple linearly-independent invertible `S` exist with different induced matches (the 6-dim Hom space has more than a 1-dim family of invertible elements up to scale, giving genuinely different transported results) | **S_NOT_UNIQUE_UP_TO_SCALE** — report the ambiguity honestly; the isomorphism is not canonical, so which specific `S` to trust needs its own justification (e.g. compatibility with a natural additional structure, not just `su(3)`-equivariance alone) |

## What this does NOT mean (pre-registered)

1. Even a `LITERAL_MATCH_FOUND` does NOT prove this project's construction
   "derives" `B-L` from `8_v` — it would show the two independently-built
   objects are compatible under a natural `su(3)`-equivariant
   identification, which is itself a nontrivial, informative fact, but
   `S`'s own canonicity (see kill criteria) must be addressed honestly.
2. Does NOT resolve round124's Gates 2-6 physical-realization obstruction
   even if a match is found.
3. Does NOT affect `N_gen=3`'s `CONDITIONAL` status, `lambda=FREE_
   COUPLING_PARAMETER`, or `safe_for_runtime=False`.
4. Does NOT re-derive any of G10-B/G11/G14/G15's or G102's own
   computations — reuses all of them by direct import.
