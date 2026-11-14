# C146 — Decision

## Computation (symbolic, exact, SymPy — `c146_schur_forced_vanishing.py`)

Reuses round59's own Clifford/Nomizu/ADNU machinery and C139's own
domain-invariant computation, unmodified. All four checks passed exactly:

```
CHECK 1  D_Sigma SU(3)-equivariance: [D_Sigma, rho_Sigma(a)] == 0     ALL 8: True
CHECK 2  D_Sigma's y1,y2,y3 columns (Sigma_odd's "3"-part) all zero   True
CHECK 3  C139's own domain invariant has zero y123-component          True (all 6 entries)
CHECK 4  D_Sigma's y123-column reproduces round59's own b=-sqrt(3)    True
```

## Verdict: **PROMOTE.** Term1's vanishing is a forced, general theorem, not a fact about `m` specifically.

**The argument, now fully verified rather than merely plausible:**

1. `D_Σ` is `SU(3)`-equivariant (Check 1) — commutes with all 8 isotropy
   generators. This was implicit throughout round59/C139/C141's entire
   machinery (their whole invariant-sector framework presupposes it) but,
   as far as this project's registry shows, never verified as a standalone
   fact before now.
2. Given equivariance, Schur's lemma is not optional — it is a theorem:
   a nonzero `su(3)`-equivariant linear map from an irreducible `3` into a
   space with no `3`-constituent must be the zero map. `Σ_even = 1⊕3̄`
   (already-certified branching) has no `3`. So `D_Σ`'s "`3`-block" is
   forced to zero — Check 2 confirms this directly on the matrix (not
   merely inferred from the abstract argument — belt and braces).
3. C139's own domain invariant (`(Σ_odd⊗m)^{SU(3)}`, dimension 1) is forced
   to avoid `Σ_odd`'s own "1"-part, because `m` has no singlet for that "1"
   to pair with (`m`'s module type is `3⊕3̄`, zero trivial summand — already
   certified in C139's own Section 2). Check 3 confirms this directly: the
   invariant vector's `y123`-component is exactly zero, all 6 entries.
4. Combining 2+3: Term1 (`⟨target_inv, D_Σ⊗Id_W · domain_inv⟩`) can only see
   `D_Σ`'s already-zero "`3`-block" — it is FORCED to vanish, for `m` AND
   for any OTHER twist bundle whose relevant summand is a `3̄`-type
   `su(3)`-irrep pairing with `Σ_odd`'s "`3`" (the only way a non-singlet
   summand can contribute to the domain invariant at all, since `Σ_odd`'s
   own constituents are only `3` and `1`).

**This upgrades C145's finding from "true for `m`, verified once" to "true
for the entire class of zero-singlet, `3̄`-type twist bundles, provable in
advance from branching data alone, no Dirac-operator computation needed."**

## Cross-check against C141 (the "control" the user asked for) — using
## ALREADY-REGISTERED data, no new computation needed

C141's own decision.md (Section 7-8, skeptic-confirmed, already committed)
found, for `W=m⊕2·1` (three `{connection}`-invariant summands: `m`, and two
decoupled trivial singlets with zero connection):

```
Term1: 2 nonzero entries, both EXACTLY -sqrt(3)
Term2: 1 nonzero entry, EXACTLY matching C139's own c_exact = -2*sqrt(3)/3
```

This is **exactly** the two-branch prediction of this round's theorem,
already sitting in the registry, previously not connected to a general
mechanism: the `m`-channel is non-singlet (`3̄`-type) → Term1=0, Term2
carries everything (matches C139 exactly, since it IS the same `m`-channel,
re-embedded unchanged — C141's own Section 8 already established this
"direct sum" fact, skeptic-confirmed). The two singlet channels →
Term1=`-√3` each (exactly `D_Σ`'s own `y123`-column value, Check 4 of this
round), Term2=0 each (trivially, `ρ_W=0` for a 1-dim trivial representation
— no computation needed, definitionally zero). **No new computation was
required for this cross-check — it is a re-attribution of already-verified
facts under the mechanism this round establishes.**

## What this changes about how future twisted-Dirac rounds should be built

Before building ANY future twist bundle `W`'s Dirac operator numerically,
its Term1/Term2 split on each `{connection}`-invariant summand is now
**predictable in advance from pure branching data**:
- Summand is a singlet (`1`) → Term1 = round59's own `-√3` (or `+√3` for
  the other chirality), Term2 ≡ 0 identically. No computation needed at
  all — this is now definitional.
- Summand is `su(3)`-irrep `3̄` (the type pairing with `Σ_odd`'s own `3`) →
  Term1 = 0 forced, ALL signal from Term2 — but Term2's SPECIFIC value
  still requires the actual connection data (geometry-specific, not given
  by this theorem).
- Any OTHER non-singlet, non-`3̄` summand → contributes NO domain invariant
  at all (Hom-dimension 0 for that piece — a different, already-covered
  case of C143's own branching-multiplicity framework).

## What remains open (explicitly, not silently folded into "done")

1. **No general closed-form for Term2's value** across different possible
   `3̄`-type twist bundles — only its FORM (nonzero, geometry-dependent) is
   understood; a specific number still requires the connection data, as
   C139's `-2√3/3` did. Per the user's own stop-rule, this is correctly
   NOT attempted here — it would require substantially more work (general
   Clebsch-Gordan/connection-coefficient machinery) with uncertain payoff.
2. **C142's `W_cand=3⊕3̄⊕3̄` is NOT resolved by this theorem** — it has
   Hom-dimension 2 (two independent `3̄`-type constituents), a case this
   round's binary singlet/`3̄` dichotomy does not directly decide (both of
   C142's own `3̄` pieces would individually have Term1=0 by this theorem,
   but the FULL 2-dimensional Hom-space's rank behavior — C143's still-open
   Lemma 2 case — is not settled by Term1's vanishing alone).
3. **The target-side argument was not separately verified as a standalone
   check** — Check 2 (the full "`3`-block" of `D_Σ` is zero, all rows) is
   actually the STRONGER, more general statement, and already subsumes the
   target-side question for any target vector, not just C139's specific
   `target_inv` — noted here for clarity, not left as a silent gap.

## Skeptic pass (Step 8a, context-blind: claim.md + script only)

**Verdict: CONFIRMED-REAL.** No fatal concern. The skeptic (no Bash access
in that environment) independently hand-traced the Clifford algebra to
verify `D_Σ[0,7]=-√3` term-by-term (confirmed), independently confirmed
`D_Σ` is strictly parity-flipping (odd↔even only, from the Clifford×spin-lift
structure), and independently re-read C141's own decision.md Section 7-8
to confirm this round's cross-check is a faithful, non-cherry-picked
re-attribution.

### Response Matrix (per FL Step 8a)

| Concern | Skeptic severity | Response |
|---|---|---|
| Docstring cited the SPECIFIC "y1,y2,y3=3, y123=1" column assignment as "already certified in C139/C143's own registered content" — only the module TYPE and EVEN_IDX/ODD_IDX (which columns are even/odd) are actually certified there; the specific irrep-per-column assignment is standard Lagrangian-spinor rep theory (Λ¹L'=3, Λ³L'=det=1), imported not cited | scope (citation precision, not a math error) | **Fixed.** Script docstring now states this precisely: EVEN_IDX/ODD_IDX and module type are project-certified; the column-level irrep assignment is standard textbook rep theory. Noted that Check 2 verifies the matrix CONSEQUENCE directly regardless. |
| decision.md's Check 2 description doesn't distinguish which zeros are Schur-forced (the 4 `Σ_even` rows) vs. automatically parity-forced (the 4 `Σ_odd` rows, since `D_Σ` is strictly odd↔even) | minor imprecision, non-fatal | **Fixed.** Script now prints an explicit note distinguishing the two; this file's own Verdict section below is updated to match. |
| "Could `D_Σ` map `Σ_odd`'s '3' into some part of `Σ` outside `Σ_even`?" | dispelled — skeptic confirmed `D_Σ` is structurally odd↔even only (Clifford × spin-lift = parity-flipping), so no such leak is possible | No action needed |
| Faithfulness of the C141 cross-check | none found — independently re-read C141 Section 7-8, confirmed accurate, not cherry-picked | No action needed |
| Overclaim beyond what checks 1-4 establish | none found — claim.md's "what this does NOT mean" section correctly bounds the theorem (no general `f(W)` formula, C142 not resolved) | No action needed |

**Precision update to the Verdict's "argument" (step 2):** of Check 2's 24
zero entries (8 rows × 3 columns), only the 12 in `Σ_even`'s rows
(`{0,4,5,6}`) are the genuinely Schur-forced content this theorem rests
on; the 12 in `Σ_odd`'s own rows (`{1,2,3,7}`) are zero for the separate,
automatic reason that `D_Σ` is strictly parity-flipping (odd↔even only) —
both are real and both were verified, but only the first kind is the
"theorem," the second is a structural triviality of how `D_Σ` is built.
This does not change the verdict (both zero-sets are still exactly what
was claimed) — it sharpens which part of Check 2 is the actual new content.

**True kill condition (per FL): NOT met.** PROMOTE stands.
