# C199 Claim — machine-check THEOREM.md's E1 escape criterion in Lean 4

**Date:** 2026-09-18
**FL tier:** [x] Standard (methodology/tooling round, not a physics experiment)
**Question type:** [x] descriptive (is this general algebraic fact TRUE, machine-verified — not an empirical claim about the world)

**Source of this idea:** direct follow-up to a user-forwarded Lean/formal-
verification discussion. The project's own `falsification-ladder.md`
Independent Verification Strength Ladder already names "Symbolic solver /
Lean / Coq" as a "Strong (for formal claims)" rung, never previously used
in this project. Concrete trigger: `experiments/20260916-g44-completeness-
theorem/THEOREM.md`'s escape condition `E1` was revised THREE times in a
row (rev 6 → rev 7 → rev 8), each revision fixing a logical gap the
previous one didn't catch (`SO(7)`-exclusion only blocking 1 of 3
conjugacy classes; then `Hom=0`-for-all-pairs being sufficient but not
necessary) — exactly the class of sufficient/necessary and quantifier-
scope error a machine-checked proof kernel is built to catch on the first
try.

---

## Prior Result Gate

1. **Exact claim:** the general linear-algebra fact underlying `E1`'s
   final (rev 8) wording is TRUE and admits a complete, `sorry`-free Lean 4
   proof: for finite-dimensional vector spaces `V`, `W` with an arbitrary
   family of "generator" endomorphisms acting on each (`ρV : ι →
   Module.End k V`, `ρW : ι → Module.End k W`), if an EQUIVARIANT linear
   isomorphism `V ≃ W` exists, then the three equivariant-Hom spaces
   `Hom(V,V)`, `Hom(V,W)`, `Hom(W,W)` have equal dimension — hence a
   strict inequality `dim Hom(V,W)² < dim Hom(V,V)·dim Hom(W,W)` proves NO
   such equivariant isomorphism can exist.
2. `decision.md` grep: N/A — first Lean artifact in this project; nothing
   to collide with.
3. `round*_claim.md` + scripts grep: N/A, same reason.
4. `null_results/` + `parked/` grep: 0 hits for "Lean", "formal
   verification", "Coq", "proof assistant".
5. Primary source re-read: `experiments/20260916-g44-completeness-theorem/
   THEOREM.md` §3, `E1` row (rev 8) and §0h (documenting rev 7's
   over-strict `Hom=0` mistake) read directly, not from memory, before
   drafting the Lean statement.
6. **Status:** [x] NEW

## Estimand

**Population:** N/A (this is a formal-logic claim, not a statistical one).
**Claim:** the lemma stated above is a theorem (provable from ZFC/Lean's
type theory + mathlib's linear algebra library), with NO reference to this
project's specific `G₂`/`SU(3)`/`Spin(8)` matrices — the proof is fully
general and abstract.
**Endpoint:** does `lake build` succeed with zero `sorry`/`admit` in the
final theorem statements? (binary, unambiguous — this is exactly what a
proof assistant gives you that sympy/numpy do not.)

## Claim

**Main theorem to prove, `sorry`-free:**
`EquivariantEquiv.finrank_eq` — an equivariant linear isomorphism forces
equal dimensions across the three Hom-spaces.

**Corollary, directly citable as E1's formal justification:**
`no_equivariant_equiv_of_finrank_sq_lt` — strict inequality in the
Cauchy-Schwarz-style bound rules out equivariant isomorphism.

## Kill criterion

| Kill condition | Threshold |
|---|---|
| The stated lemma is FALSE | a `lake build` finds no valid proof exists (not just "I couldn't find one" — an actual counterexample or a mathlib lemma contradicting it) |
| Infrastructure blocks completion | `lake`/mathlib cannot be made to build at all on this machine after a genuine attempt at a workaround |

If FALSE → kills the claim that THEOREM.md's E1 criterion has a fully
general proof of the stated form; would require re-examining what
additional hypothesis (semisimplicity? algebraically closed field?) the
informal Cauchy-Schwarz argument in THEOREM.md silently assumed.
If PASS → the general fact behind E1 is now machine-verified, independent
of this project's own sympy/numpy computations — the first "Strong"-tier
verification in this project's own Independent Verification Strength
Ladder.

## What this does NOT mean

1. Does NOT re-verify THEOREM.md's SPECIFIC numerical claims (the actual
   `dim Hom_g2 = 2`, `dim Hom_su3 = 6` computations for `G₂`/`SU(3)` on
   `Spin(8)`'s 8-dim reps) — those stay verified by sympy/numpy/explicit
   isomorphism construction, as before. This Lean proof only verifies the
   GENERAL algebraic principle that licenses using those specific numbers
   the way `E1` uses them.
2. Does NOT formalize `round124`'s or `round119`'s specific constructions
   (`su(3)⊕u(1)⊕u(1)`, `SO(4)×SO(4)`) — encoding this project's actual
   Clifford-algebra matrices into Lean is a separate, much larger task,
   explicitly out of scope here.
3. Does NOT establish that Lean will be adopted as ongoing practice for
   this project — this is a single proof-of-concept round to test the
   ROI, per the user's own explicit choice among presented alternatives.

## Fence

- safe_for_runtime = False (this is a documentation/tooling artifact, not
  a runtime component of the physics pipeline)

## Verdict

**PROMOTE.** `lake build` succeeds with exit code 0, zero errors, zero
`sorry`/`admit`, on Lean 4 `v4.34.0` + mathlib `v4.34.0`
(`[VERIFIED-tool]`, `lake build` output, `Homschwarz/Basic.lean`, 185
lines). Both `EquivariantEquiv.finrank_eq` and
`no_equivariant_equiv_of_finrank_sq_lt` are complete, `sorry`-free
theorems. Remaining output is 10 cosmetic style-linter warnings only
(missing module doc-string placement, copyright-header format,
`Set.mem_setOf_eq` deprecation, `show` vs `change`) — none block the
build or affect the proof's validity. Full writeup: `decision.md`.

Status: CLOSED PROMOTE.
