# P1 — Formal Theorem/Proposition Statements (pre-narrative stage)

**Purpose:** pin the exact mathematical content BEFORE any Introduction or
Discussion prose is drafted. Each statement below is deliberately dry —
assumptions, domain, conclusion, escape routes, proof dependencies — with
no narrative framing. Narrative belongs in the manuscript's prose
sections (`P1_NOGO_MANUSCRIPT_OUTLINE.md` §1, §8), built AFTER these
statements are reviewed and fixed, not before.

Every statement below cites its row(s) in `P1_CLAIM_TO_SOURCE_MATRIX.md`.

---

## Theorem 1 — Intrinsic `G₂`-equivariant obstruction

**Assumptions:** `S⁶` realized as `G₂/SU(3)` per the standard nearly-Kähler
coset construction (G0/G10-B/G11); octonion algebra `𝕆=ℝ⁸` with its
standard multiplication table; `Cl(0,8)` chirality-split into the three
representations `8_v, 8_s, 8_c` (G101's construction, reused unmodified).

**Domain of the statement:** symmetries of `so(8)` that are INDUCED by
this specific geometric construction (i.e. commute with the geometric
`G₂` action realized on the octonion fiber) — not an arbitrary subalgebra
of `so(8)` chosen without reference to the geometry.

**Conclusion:** `\dim C_{\mathfrak{so}(8)}(\mathfrak{g}_2) = 0`. No
continuous symmetry induced by the geometry is large enough to
Schur-distinguish the three representations `8_v, 8_s, 8_c` from one
another (`\dim_{\mathbb C}\mathrm{Hom}_{\mathfrak{g}_2}(8_x, 8_y) = 2` for all
`x, y \in \{v,s,c\}`, including `x=y` — i.e. the three channels are
`\mathfrak{g}_2`-isomorphic). Equivalently: triality is realized only as
an OUTER automorphism of this construction; no inner, geometry-induced
symmetry implements it.

**Escape routes (what would overturn this specific theorem):** none
found within the stated domain — the result is a dimension count
(`P3=0`), not an absence-of-search claim. The theorem does NOT rule out
symmetries external to (not induced by) this specific geometric
realization; Proposition 2 concerns exactly that wider class.

**Proof dependency:** `P1_CLAIM_TO_SOURCE_MATRIX.md` rows C1, C2; source
`tom_s3_spinor_toy/experiments/20260705-g102-spin8-fiber-obstruction/decision.md`.

---

## Proposition 2 — External algebraic distinguishability (two routes)

**Assumptions:** (2a) the octonion `H⊕Hℓ` split of `𝕆` and the resulting
`SO(4)×SO(4)` block-chirality construction, as defined in
`L3B_SPIN8_INTERFACE_SPEC.md` §1; (2b) `su(3)`'s own centralizer in
`so(8)` (a 2-dimensional abelian algebra), as computed by G102's
`centralizer_dim` and reused unmodified in round124.

**Domain of the statement:** algebras that are external to (not induced
by, and not contained in) `\mathfrak{g}_2` — this is the complement of
Theorem 1's domain, not an extension of it.

**Conclusion:** each of `SO(4)\times SO(4)` (2a) and
`\mathfrak{su}(3)\oplus\mathfrak{u}(1)\oplus\mathfrak{u}(1)` (2b), taken as
an algebra acting on `8_v \oplus 8_s \oplus 8_c`, gives
`\mathrm{Hom}(8_x,8_y)=0` for every off-diagonal pair
`x \ne y \in \{v,s,c\}` — full Schur non-isomorphism of the three
channels under either external algebra. These two algebras are genuinely
different as subspaces of `\mathfrak{so}(8)` (`\dim=12` vs `\dim=10`,
`PARTIAL_OVERLAP`, sharing an exact 3-dimensional abelian `\mathfrak{u}(1)^3`
core — see Note below) — this is two structurally distinct constructions
reaching the same milestone, not one construction described twice.

**Note (must accompany any statement of "independence" — `P1_CLAIM_TO_
SOURCE_MATRIX.md` row C5):** the shared 3-dim core means these two routes
are not fully orthogonal evidence; cite them as "structurally distinct,
sharing a non-generic common core," never as flatly "independent" without
this qualifier.

**Escape routes:** neither construction is shown to act GLOBALLY on the
actual compactification (only on the algebraic/fiber level) — this is
exactly Gate 2 of Theorem/Corollary below, not an escape route internal to
this proposition itself. Within its stated algebraic domain, no escape
route is currently known.

**Proof dependency:** `P1_CLAIM_TO_SOURCE_MATRIX.md` rows C3, C4, C5;
sources: `tom_s3_spinor_toy/experiments/20260717-round119-triality-distinguishability-gate/decision.md`,
`tom_s3_spinor_toy/experiments/20260718-round124-su3-centralizer-triality-candidate/decision.md`,
`tom_s3_spinor_toy/experiments/20260718-round125-so4xso4-vs-su3-centralizer-comparison/decision.md`.

---

## Proposition 3 — Explicit `su(3)`-module alignment

**Assumptions:** `8_v` as in Theorem 1/Proposition 2 (complexified,
`\mathbb{C}\otimes 8_v`); `\Sigma = \Lambda^\bullet(\mathbb{C}^3)`, the
`\mathrm{Spin}(6)` Dirac spinor bundle constructed via Clifford-lifting
`su(3)`'s isotropy action on `S^6`'s tangent space (G10-B→G11→G14/G15's
construction, reused unmodified).

**Domain of the statement:** representation theory of the ABSTRACT `su(3)`
Lie algebra acting on these two, independently-constructed, 8-complex-
dimensional modules. Says nothing about physical realization.

**Conclusion (in two parts, not one):**
(3a) `\mathbb{C}\otimes 8_v` and `\Sigma`, each restricted to `su(3)`, are
isomorphic AS ABSTRACT `su(3)`-MODULES — both decompose as
`1\oplus 1\oplus 3\oplus\bar3`, established via the End-dimension identity
`\mathrm{Hom}(V,V) = 4+a^2+b^2` (`a+b=2`), with both sides independently
satisfying `\mathrm{Hom}(V,V)=6`, forcing `a=b=1` uniquely.
(3b) An EXPLICIT invertible intertwiner `S` realizing this isomorphism has
been constructed and verified to `\mathrm{iso\_residual}\sim 10^{-15}`
(machine precision), exhaustively across all 12 members of
`\mathrm{Aut}(\mathfrak{su}(3)) = W(A_2)\rtimes\mathbb{Z}_2`.

**Provenance constraint (mandatory — `P1_CLAIM_TO_SOURCE_MATRIX.md` row
C10, `SUPERSEDED_RESULTS.md` SR8):** (3a) and (3b) are established by
DIFFERENT, sequential steps — (3a) by round127 alone, (3b) by round128
alone. Round127 itself never found or claimed an explicit `S`
(`results_round127.json`: `isomorphism_found=false`). Do not state or
imply that round127 independently corroborates (3b) — it does not, and
was never intended to.

**Escape routes:** none currently known against either (3a) or (3b) as
stated (both independently verified to machine precision / exhaustively
over the automorphism group). Two computational bugs were found and
fixed during the construction of (3b) — see the manuscript's planned
"Verification history" note (`P1_NOGO_MANUSCRIPT_OUTLINE.md` §5) — neither
bug survives in the final result: the exhaustive 12-candidate scan itself
is the check that would have failed had either bug persisted, and it did
not (residual at machine precision for all 12 valid `S`).

**Proof dependency:** `P1_CLAIM_TO_SOURCE_MATRIX.md` rows C8, C9, C10;
sources: `tom_s3_spinor_toy/experiments/20260718-round127-8v-vs-s6-spinor-isomorphism/decision.md`,
`tom_s3_spinor_toy/experiments/20260718-round128-cartan-weyl-alignment/decision.md`.

---

## Proposition 4 — No literal `B-L` match in the tested alignment class

**Assumptions:** the `S` of Proposition 3(3b), for each of its 12 valid
(`\mathrm{Aut}(\mathfrak{su}(3))`-related) realizations; round124's
`su(3)`-centralizer (Proposition 2, construction 2b); `G15`'s established
`B-L` operator `BmL` (an explicit `8\times8` matrix,
`\mathrm{diag}(-1,-\tfrac13,-\tfrac13,-\tfrac13,\tfrac13,\tfrac13,\tfrac13,1)`
in its own basis).

**Domain of the statement:** the specific question of whether round124's
particular algebraic candidate (2b), transported through the Proposition-3
intertwiner, coincides with the specific, previously-established `B-L`
operator. Does NOT address whether any OTHER algebraic candidate might
match `B-L`, and does not address `B-L`'s own uniqueness (see Note).

**Conclusion:** transporting round124's centralizer through each of the 12
valid intertwiners `S` and fitting the result against `BmL` by least
squares gives relative residuals in `\{0.53,\ldots,1.00\}` — zero clean
matches against a `10^{-4}` threshold, for ALL 12 valid choices of `S`,
not merely the first tested. `\mathrm{bml\_verdict} =
\mathrm{NO\_LITERAL\_MATCH\_ANY\_OF\_12}`.

**Note (independent caveat — `P1_CLAIM_TO_SOURCE_MATRIX.md` row C12, not
re-verified in this pass):** `B-L` itself is separately reported (Round61-BL)
as not unique among a `\dim\ge3` admissible family of candidate operators
— this proposition's negative result concerns the ONE specific `BmL`
construction tested, not a claim about `B-L` in full generality.

**Escape routes:** a genuinely DIFFERENT algebraic candidate (not
round124's specific construction) might still match `BmL` — not addressed
or ruled out here. Re-deriving `BmL` under a different admissible
construction (per the C12 caveat) might also change the comparison target
— not attempted here.

**Proof dependency:** `P1_CLAIM_TO_SOURCE_MATRIX.md` row C11; source
`tom_s3_spinor_toy/experiments/20260718-round128-cartan-weyl-alignment/decision.md`
(all-12 scan, added 2026-07-19).

---

## Corollary 5 — Physical generation realization does not follow (from
Propositions 2-4 and the separate product-Dirac null result)

**Assumptions:** Propositions 2, 3, 4 above; `G74A` Lemma B (an exact-
`G_2`-only proof technique for `\dim\ker=1`, cited only for its stated
domain of applicability, not for its numeric conclusion — see
`P1_CLAIM_TO_SOURCE_MATRIX.md` row C6 and the distinct-obstacles note
below); the `OPEN_BLOCKERS.md` OB1/KT-8 product-Dirac result.

**Domain of the statement:** whether the algebraic structures of
Proposition 2, given Proposition 3's alignment and Proposition 4's
negative gauge-identification result, can be shown to realize three
physical matter generations via a global (not merely fiber-level) action
on the actual `S^3\times S^6` compactification.

**Conclusion:** this does NOT follow, and is not addressed by any result
above — for three separate reasons, which must not be merged into one
"mechanism" in prose:
(5a) **Tool-level obstacle:** realizing either Proposition-2 candidate
physically requires breaking `G_2`; `G74A` Lemma B's exact-`G_2`-only
proof technique does not survive any nonzero `G_2`-breaking perturbation,
and no alternative internal spectral-gap argument is currently known.
(5b) **External-input obstacle:** whether the distinguishing algebra acts
GLOBALLY on the compactification (Gate 2 of
`L3B_SPIN8_INTERFACE_SPEC.md` §7) is explicitly named by the cited source
itself as blocked pending unpublished external input (Tom Lawrence's
"Part 5"), not solicited per this project's standing constraint.
(5c) **Separately:** the untwisted product Dirac operator on `S^3\times S^6`
has zero zero-modes (`OPEN_BLOCKERS.md` OB1/KT-8), and no internally-found
parent-action principle selects a torsion parameter `t` — four independent
internal mechanism-search attempts found none. This is `PARKED`, not
`REJECTED`.

**Escape routes:** (a) Tom Lawrence's Part 5 (not solicited); (b) a
genuinely new internal derivation map connecting geometry to the Dirac
operator, per `PARENT_ACTION_GATE.md`'s own checklist; (c) resolving
(5a)/(5b)/(5c) are three SEPARATE escape conditions, not one — satisfying
one does not automatically resolve the others.

**Explicit non-conclusion (mandatory in any manuscript use of this
Corollary):** this Corollary does NOT say "triality cannot explain
generations" as a universal claim — it says the SPECIFIC route examined in
Propositions 2-4, under the SPECIFIC obstacles (5a)-(5c), is currently
blocked, with (5a) being a proof-method limitation, (5c) being an internal
`PARKED` null result, and (5b) being an external-input block — none of the
three is a mathematical impossibility.

**Proof dependency:** `P1_CLAIM_TO_SOURCE_MATRIX.md` rows C6, C7, C13;
Propositions 2-4 above.

---

## What this file does NOT do

- Does not draft Introduction or Discussion prose (per the authoring
  instruction — those come after this file is reviewed).
- Does not introduce any claim not already present in
  `P1_CLAIM_TO_SOURCE_MATRIX.md` or `P1_FROZEN_VERDICTS_TABLE.md`.
- Does not address `N_gen=3`, `\lambda`, or `safe_for_runtime` — out of
  scope by the standing project fence and the Section-1 scope fence in
  `P1_NOGO_MANUSCRIPT_OUTLINE.md`.
