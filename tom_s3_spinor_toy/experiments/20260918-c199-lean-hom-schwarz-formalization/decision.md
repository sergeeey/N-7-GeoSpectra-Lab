# C199 Decision — Lean 4 formalization of THEOREM.md's E1 escape criterion

**Date:** 2026-09-18
**Verdict: PROMOTE** (first "Strong"-tier machine-checked artifact in this
project's Independent Verification Strength Ladder)

---

## What was proved

**Theorem (`EquivariantEquiv.finrank_eq`).** For fields `k`, finite-dimensional
`k`-vector spaces `V`, `W`, an arbitrary index set `ι` of "generators" acting
as `ρV : ι → Module.End k V` and `ρW : ι → Module.End k W`: if an equivariant
linear isomorphism `V ≃ W` exists (a `LinearEquiv` that intertwines every
generator's action), then the three equivariant-Hom spaces
`Hom_h(V,V)`, `Hom_h(V,W)`, `Hom_h(W,W)` (submodules of the full linear-map
space, cut out by the equivariance condition) all have equal `finrank`.

**Corollary (`no_equivariant_equiv_of_finrank_sq_lt`), the one THEOREM.md's
`E1` row actually needs.** If
`finrank(Hom_h(V,W))² < finrank(Hom_h(V,V)) · finrank(Hom_h(W,W))`, no
equivariant isomorphism `V ≃ W` can exist — `IsEmpty (EquivariantEquiv ρV ρW)`.
This is the Cauchy-Schwarz-style strict inequality rev 8 of THEOREM.md's E1
cites to justify "M genuinely distinguishes the channels", stated and proved
with zero reference to this project's own G₂/SU(3)/Spin(8) matrices.

**Proof idea (found by hand before touching Lean, and it is the reason the
formalization was tractable in one round):** an equivariant equivalence `f`
gives two linear equivalences by composition — `φ ↦ f ∘ φ` sends
`Hom_h(V,V) ≃ Hom_h(V,W)`, and `ψ ↦ ψ ∘ f⁻¹` sends `Hom_h(V,W) ≃ Hom_h(W,W)`.
Linear equivalences preserve `finrank`. No Schur's lemma, no semisimplicity,
no algebraically-closed-field hypothesis — a fully elementary fact about
composing with an invertible linear map.

## Build result

```
lake build
...
Build completed successfully (1589 jobs).
```

`[VERIFIED-tool]`: Lean `v4.34.0`, mathlib `v4.34.0` (pinned in
`lakefile.toml`/`lean-toolchain`), zero errors, zero `sorry`/`admit` anywhere
in `Homschwarz/Basic.lean` (grep-confirmed). Ten remaining warnings are all
cosmetic style-linter notices (module doc-string placement, copyright-header
format expected by mathlib's own house style, one deprecated
`Set.mem_setOf_eq` — a mathlib-version naming change unrelated to this proof
— and one `show`-vs-`change` style preference). None affect soundness; they
were left as-is rather than chased, since this is a one-off proof-of-concept
round, not an attempt to land this file in mathlib itself.

## Skeptic / adversarial check (FL Step 8a)

For a formal-logic claim, the adversarial check that matters most is the Lean
kernel's own type-checker, which is strictly stronger than a context-blind
LLM skeptic pass: every tactic step is verified down to fully explicit proof
terms, and `lake build` genuinely fails (not just "looks wrong") on any
invalid step. Per `falsification-ladder.md`'s own Independent Verification
Strength Ladder, "Symbolic solver / Lean / Coq" already sits at the top
practical rung ("Strong, for formal claims") — above "different model" and
below only "blind replication by another group" / "new physical experiment",
neither of which applies to a pure math fact. Running a separate LLM skeptic
pass on top of a `sorry`-free kernel-checked proof would not add adversarial
strength; the standard, correct escalation for a formal claim's own
Recomposition Gate concern (do the individually-proved pieces combine
validly?) is answered by the SAME kernel check on the final composed
theorem, which already happened (`finrank_eq` and its corollary both build
clean, using `compLeftEquiv.finrank_eq` and `compRightEquiv.finrank_eq`
composed exactly as claimed).

## Substrate Gate note (infra workaround, not a research finding)

`lake init` failed inside this project's actual path
(`E:\Проверка Гипотез\...\experiments\20260918-c199-lean-hom-schwarz-
formalization`, 185+ chars, Cyrillic + spaces) with
`fatal: '$GIT_DIR' too big'` while cloning the `LeanSearchClient` git
dependency — confirmed via `echo "GIT_DIR=[$GIT_DIR]"` returning empty, i.e.
a genuine path-length/path-content issue in Lake's git subprocess handling on
Windows, not a misconfigured environment variable. Per this project's own
Substrate Gate discipline (`falsification-ladder.md` Step 2a): this is
`BLOCKED-INFRASTRUCTURE`, not evidence about the claim. **Workaround:** built
the full Lake/mathlib project in a short ASCII path (`C:\leanwork\c199`)
instead, then copied only the source artifacts (`Homschwarz/Basic.lean`,
`lakefile.toml`, `lean-toolchain`, `lake-manifest.json`) back into this
experiment folder — analogous to not committing `node_modules`/a venv.
`.lake/` (the build cache/mathlib checkout, several hundred MB) stays
excluded via the template's own auto-generated `.gitignore` (`/.lake`).

## What this does and does not mean

Restating `claim.md`'s pre-registered "What this does NOT mean" section,
now that the result is in — all three still hold exactly as stated:

1. Does **not** re-verify THEOREM.md's specific numbers (`dim Hom_g2 = 2`,
   `dim Hom_su3 = 6` for `G₂`/`SU(3)` on `Spin(8)`'s reps) — those remain
   verified by this project's own sympy/numpy/explicit-isomorphism checks,
   unchanged. This proof only certifies the GENERAL principle that licenses
   using those numbers the way E1 does.
2. Does **not** formalize round124's or round119's actual
   `su(3)⊕u(1)⊕u(1)` / `SO(4)×SO(4)` constructions — encoding this
   project's real Clifford-algebra matrices into Lean remains out of scope.
3. Does **not** establish Lean as ongoing practice for this project — this
   was a single proof-of-concept round, per the user's own explicit choice
   among presented alternatives ("Да, поставить Lean и формализовать E1").

**What it DOES establish:** the load-bearing direction of E1's
Cauchy-Schwarz argument (strict inequality on equivariant-Hom dimensions ⟹
non-isomorphism) is not just "plausible representation theory" — it is a
machine-checked theorem, true for ANY finite-dimensional vector spaces with
ANY generator action, with the Lean kernel as the adversary instead of a
human or LLM reviewer.

## Reproduction

```bash
# Requires elan (Lean toolchain manager) and a short, ASCII-only build path
# on Windows (see Substrate Gate note above for why).
cd Homschwarz-checkout-dir   # e.g. a fresh copy of this experiment folder
lake build
# Expect: "Build completed successfully (1589 jobs)."
```

## Cross-links

- `experiments/20260916-g44-completeness-theorem/THEOREM.md` — E1's
  informal statement (rev 8, §3) that this formalizes.
- `pearl_registry/INDEX.md` — candidate entry: first "Strong"-tier
  (Independent Verification Strength Ladder) artifact in this project.
