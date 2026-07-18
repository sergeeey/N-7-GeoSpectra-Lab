# Round109 — Decision

**Date:** 2026-07-17
**Verdict:** `DIAGONAL_HOMOMORPHISM_EMBEDDING_PROVEN_IMPOSSIBLE__SCOPE_HONESTLY_LIMITED_TO_LIE_ALGEBRA_HOMOMORPHISMS__SU4_SIMPLICITY_CITED_NOT_COMPUTED`
(skeptic verdict: `WEAKENED`, two honesty corrections accepted, core
argument survives)
**Go/no-go:** the MOST NATURAL reading of "diagonal `SU(4)` embedding"
(a literal Lie-algebra homomorphism `su(4)→so(4)⊕X`, exactly what the
Killing-vector algebra of a product manifold with product metric gives)
is definitively closed by a clean, general argument — not a search.
**Two scope corrections, both accepted, stated honestly below**, not
overclaimed away.

## The argument [core logic CONFIRMED by skeptic, unchanged]

**Key lemma (standard, elementary, confirmed correct without
reservation by skeptic review):** a Lie-algebra homomorphism `φ:g→h`
FROM A SIMPLE algebra `g` is either the zero map or injective (`ker(φ)`
is an ideal of `g`; a simple algebra's only ideals are `{0}` and itself).

**Application:** for any homomorphism `φ=(φ₁,φ₂):su(4)→so(4)⊕X`
(`X=so(7)`, `g₂`, or `su(3)`, per round108's own three readings),
`φ₁:su(4)→so(4)` cannot be injective (`dim(so(4))=6<15=dim(su(4))`, a
pure dimension-count fact) — so BY THE LEMMA, `φ₁=0` is FORCED, for
**every** possible homomorphism, with no case-by-case search needed.
**Consequence:** every embedding of `su(4)` into `so(4)⊕X` necessarily
projects to zero on the `so(4)` (`S³`-side) factor — there is no
genuine "diagonal" `Lie-algebra-homomorphism` embedding; every such
embedding collapses entirely to a same-factor embedding into `X` alone
(rounds 102/108).

## Correction 1 [accepted from skeptic]: `su(4)`'s simplicity is CITED,
not independently computed here

The script's own Killing-form check (`det(Killing form)≠0`) establishes
`su(4)` is **semisimple**, not simple — a genuine gap in the script's own
framing, correctly caught. **Counter-example the skeptic supplied:** a
direct sum of five copies of `su(2)` (each dim 3, total dim 15) would
ALSO be semisimple (non-degenerate Killing form) without being simple —
so the `det≠0` check alone cannot distinguish "one simple 15-dim algebra"
from "several smaller simple factors summing to 15." **`su(4)`'s actual
simplicity is a standard, well-established classification fact (`A₃` in
the Cartan classification, `[DOCS]`)** — this round explicitly
constructed `su(4)`'s defining 4-dimensional representation (15 explicit
antihermitian traceless matrices, confirmed linearly independent and
closed under commutator) and confirmed semisimplicity as a sanity check,
but the SIMPLICITY claim itself rests on citation, not this round's own
independent derivation. Stated honestly here, not smoothed over.

## Correction 2 [accepted from skeptic]: scope is Lie-algebra
homomorphisms of the STANDARD product-manifold Killing algebra, not
every conceivable physical coupling

The proof rigorously closes: "is there a Lie-algebra homomorphism
`su(4)→so(4)⊕X`" — exactly the right question for the Killing-vector
algebra of a genuine PRODUCT manifold with PRODUCT metric (which is
what `so(4)⊕so(7)` literally represents). **It does NOT address:**
field-dependent/point-dependent identifications between the `S³`- and
`S⁶`-side generators (not a Lie-algebra homomorphism at all, since such
generators would not close point-independently); bundle-TWISTED
constructions (if the `S⁶` fiber is nontrivially twisted over `S³`, the
effective symmetry algebra can genuinely differ from the raw
`so(4)⊕so(7)`); or any construction that leaves the strict `S³×S⁶`
PRODUCT ansatz. **This connects directly to round103's own finding**
(the D4 moonshot): a block-diagonal/dynamical-torsion construction that
genuinely leaves the product ansatz was shown there to be a standard,
legitimate NCG move, NOT ruled out — and this round's clean algebraic
no-go, by its own honest scope limit, does **not** automatically apply
to such a construction either.

## Applying the pre-registered criteria (claim.md Section 3)

**DIAGONAL EMBEDDING PROVEN IMPOSSIBLE, for the general Lie-algebra-
homomorphism reading** — the pre-registered primary outcome, confirmed,
but with the honest scope/simplicity corrections above explicitly
attached, per the skeptic response matrix (not dismissed, not treated
as invalidating the core result).

## Kill Analysis

- **What this kills:** the "diagonal embedding" question AS A LIE-
  ALGEBRA-HOMOMORPHISM question — fully and generally closed, for
  `so(4)⊕so(7)` and all of round108's physically-motivated
  restrictions (`so(4)⊕g₂`, `so(4)⊕su(3)`). Combined with rounds
  102/108's same-factor closure, this closes EVERY reading of "does an
  alternative `SU(4)` Killing-algebra realization exist" within the
  standard product-manifold framework.
- **What this does NOT kill:** the possibility that leaving the strict
  product ansatz (round103's own already-open fork — a twisted/
  dynamical-torsion construction) could supply a DIFFERENT kind of
  `SU(4)`-related structure not captured by a literal Killing-algebra
  homomorphism. `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`,
  `safe_for_runtime=False` — all untouched.
- **What survives, as the actual net product of rounds 102+108+109
  together:** within the standard `S³×S⁶` product-manifold framework,
  gate G97's original conclusion ("no `SU(4)` gauge-algebra realization
  exists") is now **fully, rigorously, and generally established** —
  not merely asserted, not merely checked same-factor, but closed for
  BOTH same-factor AND diagonal readings, with the honest remaining
  caveat that this framework-internal closure does not extend to
  genuinely non-product constructions (round103's own still-open fork).

## Relaxation Map (for future work, NOT attempted here)

| Option | What it would require |
|---|---|
| Pursue the non-product/twisted-bundle possibility this proof explicitly does not cover | Round103's own fork — a genuinely different geometric construction, substantially larger undertaking than this round |
| Independently verify `su(4)`'s simplicity beyond citation (close correction 1 fully) | Check indecomposability directly (e.g. verify the adjoint representation is irreducible, or that no proper subset of generators forms an ideal) — cheap, not attempted here, would fully self-contain the argument without relying on external classification |

## Assumptions carried, unresolved

- `su(4)` is simple — cited from the standard `A₃` classification, per
  Correction 1, not independently re-derived beyond confirming
  semisimplicity here.
- The Killing-vector algebra of the physical construction really IS
  `so(4)⊕so(7)` (or its `g₂`/`su(3)` restrictions) with no ADDITIONAL
  structure (e.g. a nontrivial fiber bundle connection term) not
  captured by this simple direct-sum picture — consistent with, but not
  independently re-verified against, this project's own product-ansatz
  framing (E2/E12) throughout.

## What this does NOT mean

1. Does NOT claim to have addressed non-product/twisted constructions —
   explicit scope limit, Correction 2.
2. Does NOT independently re-derive `su(4)`'s simplicity from first
   principles — explicit citation, Correction 1.
3. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Does NOT modify `preprint.tex` or any prior
   experiment folder.

## Check (reproduces this decision)

```
cd experiments/20260717-round109-diagonal-embedding-nogo
python e32_diagonal_embedding_nogo.py
```
Expect: `su4_generators_built_correctly=True`,
`killing_form_nondegenerate_su4_semisimple=True` (semisimplicity, NOT
simplicity — see Correction 1), `injective_su4_into_so4_possible_by_dimension=False`.
