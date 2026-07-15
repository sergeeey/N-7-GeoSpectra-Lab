# Round62-StrongCPScoping Decision — EXPENSIVE (as expected), one cheap partial building block found

**Date:** 2026-07-15
**Verdict: EXPENSIVE (matches the pre-registered "physically heavy" expectation).**
A full resolution of the claim as scoped in the preprint's own Open Problems
text is comparable to or exceeding the multi-round L4A/L4B program, not a
bounded single round. One genuine, cheap, reusable partial building block
was found along the way (see below) — recorded, not oversold.

## Method note

Pure literature-grounding + cost re-estimation, matching
`20260713-round51-universality-scoping`'s own method — no new physics
computation attempted. All claims below are WebSearch-sourced or reused
from already-proven facts in this project's own `preprint.tex`; nothing
asserted from unaided memory.

## What "Pontryagin density analysis" would actually require

Three real literature threads found, none of which directly hands over a
ready-made formula for this project's exact geometry (S³×S⁶, gauge fields
identified with spin-connection components):

1. **Spectral-asymmetry / η-invariant θ-mechanisms are a real, if niche,
   literature area** — Khlebnikov & Shaposhnikov, *"Brane-worlds and
   theta-vacua"* (arXiv:hep-th/0412306): for odd-to-even-dimensional
   reduction (5D→4D), a change in spectral asymmetry of massive KK modes
   (an odd-dimensional APS analogue) explains a UV/IR anomaly mismatch, with
   a θ-angle relaxation mechanism as a phenomenological consequence. This
   legitimizes the preprint's own S³ η-invariant argument as standing in a
   real tradition — but it is a single-extra-dimension (odd→even) case, not
   a product 3+6 internal space; adapting it here is new work, not a lookup.
2. **G2-holonomy compactifications have their own, different θ-structure** —
   in 7D M-theory-on-G2-holonomy constructions, the analogue of the 4D θ
   angle is a *3-form* Θ (interaction term Θ∧F∧F), not a single number. This
   is a materially different, more involved structure than the simple
   picture in the current preprint paragraph, and integrating it correctly
   with the S³ factor's contribution is a nontrivial, original derivation.
3. **Nearly-Kähler G2-instanton literature on S⁶ specifically exists and is
   substantial** (Charbonneau-Harland 2016, already in this repo's own
   reference PDFs; Xu 2015 "Deformations of nearly Kähler instantons";
   Bunk-Sämann-Szabo "Yang-Mills instantons and dyons on homogeneous
   G₂-manifolds") — a real toolkit for characteristic-class/instanton-index
   computations on this exact space, but using it for a θ_QCD-relevant
   quantity is original synthesis, not extraction of an existing result.

**No paper found computes the specific quantity this project would need**
(a Pontryagin-density-type contribution to an effective 4D θ from a product
S³×S⁶ internal space with gauge fields sourced from the spin connection).

## Genuine cheap partial building block found

This project's own **χ-lemma is already directly reusable here**:
`preprint.tex` (lines 117, 177-178, 455, 473-474) already proves
$H^2(S^6;\ZZ)=H^4(S^6;\ZZ)=0 \Rightarrow c_1(S^6)=c_2(S^6)=0$ — established
for the generation-counting argument (Theorem T1), not for this purpose, but
directly applicable: since $H^4(S^6;\ZZ)=0$ for purely dimensional/topological
reasons (independent of any bundle choice), **any** degree-4 characteristic
class on $S^6$ — including a Pontryagin class $p_1$ — vanishes topologically.
Because this project's gauge fields are literally components of the spin
connection (Lawrence's mechanism, not an independent gauge bundle), the
tangent-bundle and "gauge" characteristic classes are the same object here,
so this single already-proven fact directly rules out a topologically
nontrivial (integer instanton-number-type) contribution from $S^6$ to any
such term.

**This is a real, free, zero-new-computation partial result — but it is
explicitly NOT a resolution.** $H^4(S^6)=0$ means every closed 4-form on
$S^6$ is exact; it does not by itself fix whether the corresponding LOCAL
curvature/Pontryagin density integrates to zero against whatever specific
KK-reduction structure (adiabatic limit, Chern-Simons-type boundary term,
choice of primitive) an honest derivation of an induced 4D θ-term would
actually require. Treating "topologically trivial class" as automatically
"physically zero contribution" here would be exactly the kind of unearned
shortcut this project's own audit-verification-gate exists to catch — flagged
explicitly, not asserted.

## Cost estimate

| Piece | Estimated cost |
|---|---|
| S⁶ characteristic-class vanishing (topological necessary condition) | **Already free** (χ-lemma reuse, this round) |
| Correct adiabatic-limit/KK-reduction argument turning that into an actual induced-θ statement | New original derivation, no direct precedent found — comparable to 1-2 rounds of the L4B-certification type (Round 52-56), IF a suitable technique is identified; genuinely open-ended if not |
| Combining with the S³ η-invariant piece into one coherent product-space formula | Comparable to another 1-2 rounds — no literature precedent for exactly this combination |
| "Non-perturbative effects" clause | This project's own prior experience (G83-G86B, λ-origin) found this class of question genuinely hard with no clean geometric resolution after a substantial multi-round search — treat as open-ended, not boundable in advance |

**Total: MODERATE-to-EXPENSIVE**, plausibly matching or exceeding the L4B
program's total cost (Round 52-59, ~8 rounds), with the non-perturbative
piece carrying real risk of being genuinely open-ended (no bound found).
Matches, and sharpens, the user's own prior "physically heavy" assessment.

## Recommendation

1. **Do not open a full Strong CP derivation round now.** Re-rank this item
   down, same treatment Universality received in Round 51 — informative
   demotion, not abandonment.
2. **Optional cheap preprint update** (not applied here, needs separate
   confirmation): the χ-lemma reuse above (§ "Genuine cheap partial building
   block") could be added as ONE sentence to the existing Strong CP Open
   Problems paragraph, since it costs nothing further and is honestly scoped
   (explicitly marked as a necessary-condition observation, not a partial
   resolution).
3. If ever revisited: start with thread (1) above (Khlebnikov-Shaposhnikov's
   spectral-asymmetry mechanism) as the most directly analogous starting
   point, since it already uses the same η-invariant machinery this
   project's own S³ argument is built on.

## Sources (WebSearch, this round)

- [Brane-worlds and theta-vacua (S. Khlebnikov, M. Shaposhnikov, hep-th/0412306)](https://arxiv.org/abs/hep-th/0412306)
- [Deformations of nearly Kähler instantons (arXiv:1510.07720)](https://arxiv.org/pdf/1510.07720)
- [Yang-Mills instantons and dyons on homogeneous G2-manifolds (arXiv:1006.2388)](https://arxiv.org/pdf/1006.2388)
- [M-theory on manifolds of G2 holonomy: the first twenty years](https://www.researchgate.net/publication/2052265_M-theory_on_manifolds_of_G2_holonomy_the_first_twenty_years)
- [G2-Manifolds and (arXiv:1810.12659)](https://arxiv.org/pdf/1810.12659)

## Files

- `claim.md` — frozen before this scoping investigation
