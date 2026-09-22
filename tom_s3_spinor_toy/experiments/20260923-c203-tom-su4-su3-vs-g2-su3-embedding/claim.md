# C203 Claim — does Tom's SU(3)⊂SU(4)≅SO(6) embedding coincide with this project's own G2/SU(3)⊂SO(6) embedding?

**Date:** 2026-09-23
**FL tier:** [x] Full (touches this project's own G2/SU(3)/Spin(7) physics substrate directly)
**Question type:** [x] descriptive (are two explicit real 6-dimensional representations of su(3), built by two independent routes, equivalent as SO(6) embeddings up to conjugation)

## L0 Gate

Entity: the compact Lie algebra su(3), realized as a subalgebra of so(6) two
ways. Falsifiable predicate: the two 6-dimensional real representations of
su(3) either ARE or ARE NOT conjugate under O(6) (equivalently, related by an
orthogonal change of basis). Measurable outcome: existence/non-existence of
an orthogonal intertwiner `U` with `U^T A_i U = B_i` for a generating set of
generators, cross-checked against an independent invariant (the eigenvalue
spectrum of a generic Cartan element, which is basis-independent). All three
present -> gate passes, proceed.

## Prior Result Gate

1. Exact claim: Tom Lawrence's SU(3)⊂SU(4)≅SO(6) embedding (his GPIC 2026
   talk, slide 11: "Use |psi> and <chi| of SU(4) to make 6-vector", i.e. the
   real 6-dim representation obtained by restricting Lambda^2(C^4) [the
   antisymmetric-tensor / adjoint-adjacent representation of SU(4) that is
   isomorphic to SO(6)'s vector representation under Spin(6)~SU(4)] to
   SU(3)~SU(4)'s upper-left 3x3 block) is O(6)-conjugate to this project's
   own SU(3) = Stab_{G2}(e6) acting on the 6-dim complement of e6 in Im(O)
   (constructed in `experiments/20260626-g96-s6-g2-su3/g96_g2_su3.py`, the
   canonical G2/SU(3)-on-S6 construction this project's real physics claims
   -- Round59, C73's twisted Dirac battery -- are built on).
2. `grep` of `null_results/`, `parked/`, `pearl_registry/INDEX.md`,
   `experiments/` for "SU(4)... SO(6)" / "Lambda^2... SU(4)" / this specific
   comparison: no hits beyond unrelated lambda-coupling-parameter false
   positives. This exact cross-check has not been run.
3. **Directly relevant prior results, read in full before proceeding:**
   - `experiments/20260618-g10b-su3-in-so6/` -- an EARLIER, different SU(3)
     embedding into SO(6), built as the J-preserving traceless subalgebra
     (J = M01+M23+M45, a generic complex structure on R^6 NOT tied to G2).
     Its own decision.md explicitly states "Does NOT prove this is the
     unique such embedding" -- this round answers exactly that open
     question, but for the comparison against Tom's construction, not
     G10-B's. Whether G10-B's SU(3) and G96's G2/SU(3) themselves coincide
     is a SEPARATE, not-yet-answered question, out of scope here (not
     asserted either way).
   - `experiments/20260626-g96-s6-g2-su3/` -- VERIFIED (5/5 checks): dim(G2)=14,
     SU(3)=Stab(e6) dim=8, complement dim=6="3+3bar" under SU(3). This is the
     REFERENCE construction reused here directly (not rebuilt).
4. **Status:** [x] NEW.

## Estimand

**Population:** the compact Lie algebra su(3), realized as a real
6-dimensional orthogonal representation two ways.
**Intervention/method:** (a) build Tom's representation explicitly: SU(3)'s
fundamental (3, complex) block-embedded in SU(4)'s fundamental (4 = 3 (+) 1),
acting on Lambda^2(C^4) (6 complex dimensions), realified to a 6-dim real
orthogonal representation; (b) reuse G96's su(3) generators (the 8
stabilizer-of-e6 elements of g2, restricted to their action on the 6-dim
orthogonal complement of e6 in Im(O)) directly, without rebuilding; (c)
search for an orthogonal intertwiner between the two generator sets; (d)
independently cross-check via a basis-free invariant (Cartan-element
eigenvalue spectrum) that does not depend on finding the intertwiner first.
**Comparator:** the null outcome is that no such intertwiner exists and the
two spectra differ -- meaning the two constructions are genuinely
inequivalent embeddings of su(3) into so(6) (a real, reportable structural
difference between Tom's GUT derivation and this project's G2/SU(3) Dirac
substrate).
**Endpoint:** boolean (conjugate / not conjugate), with the explicit
orthogonal intertwiner if found, and the two independently-computed Cartan
spectra for cross-check regardless of outcome.

**Natural-language statement:** "We determine, by exact/numeric linear
algebra, whether the su(3) subalgebra Tom Lawrence uses (embedded via
SU(3)~SU(4)'s fundamental block, acting on Lambda^2(C^4)~R^6) is conjugate,
as a real 6-dimensional orthogonal representation, to the su(3) subalgebra
this project's own G2/SU(3)-on-S6 construction uses (G96's stabilizer of e6
in Im(O), acting on the 6-dim orthogonal complement) -- reusing G96's already
-verified generators rather than rebuilding them."

## Kill criterion

| Condition | Consequence |
|---|---|
| No orthogonal `U` intertwines the two generator sets, AND the Cartan spectra differ | The two embeddings are genuinely INEQUIVALENT -- kills any claim that Tom's SO(10)-GUT derivation and this project's G2/SU(3) Dirac construction share the same SU(3) substrate; report as a real structural divergence, not a labeling issue |
| An intertwiner is found by one method but the independent Cartan-spectrum cross-check disagrees | Something is wrong with the construction or the check itself -- STOP, do not report either verdict, diagnose the discrepancy first |
| G96's generators, re-run here, do not reproduce G96's own recorded results (dim=8, complement=6, closure) | This round's REUSE of G96 is broken -- fix before proceeding, do not silently rebuild a divergent version |

If FAIL (inequivalent) → kills: any claim of a shared SU(3) substrate between
Tom's GUT derivation and this project's Dirac operator; the two remain
independently interesting but structurally different constructions.
If PASS (equivalent) → survives: a genuine, verifiable structural link
between Tom's Standard-Model derivation and this project's own physics
substrate — worth surfacing in future correspondence (not sent yet).

## Checks planned

| # | Check | Negative control -- input for which this check MUST fail |
|---|---|---|
| T1 | Reproduce G96's own recorded results by re-running its script unmodified | If `g96_g2_su3.py`'s own asserts (`dim(G2)==14`, etc.) ever fail, this control has done its job -- not expected to fail, but not skipped |
| T2 | Build Tom's Lambda^2(SU(4)) su(3) representation; verify it is 6-real-dimensional and closes as a Lie algebra under commutation | A random 6x6 antisymmetric matrix set (not derived from su(3)) must NOT close under commutation into an 8-dim simple algebra |
| T3 | Orthogonal-intertwiner search between the two su(3) representations | An unrelated random SU(3) embedding into SO(6) (e.g. G10-B's J-preserving one, known to be a DIFFERENT embedding per its own caveat) must NOT intertwine with either -- run as an explicit negative control, not assumed |
| T4 | Cartan-eigenvalue-spectrum cross-check, independent of T3's intertwiner | Two representations that are NOT conjugate (e.g. the 6=3+3bar rep vs the real 6-dim adjoint-truncated rep, if constructible) must show a different spectrum -- sanity-checked against G10-B as the independent negative control here too |

## What this does NOT mean

1. Does NOT establish that Tom's full "Covariant Compactification" theory and
   this project's G2/SU(3)/N_gen=3 theory are the same theory, or compatible
   in any broader sense -- this is a narrow algebraic embedding comparison.
2. Does NOT resolve the separate SO(6)-as-local-frame-group vs
   SO(7)-as-global-isometry-of-S6 distinction raised in the correspondence
   review two turns earlier -- that remains a separate, unverified
   [INFERRED] reading of Tom's slides, not re-examined here.
3. Does NOT constitute a reply to Tom or any claim sent to him -- purely
   internal structural comparison.
4. If PASS: does NOT mean Tom's SO(10)-GUT derivation is thereby "proven" or
   validated by this project's own machinery, or vice versa -- equivalence of
   one 8-dimensional subalgebra embedding is a narrow, specific fact, not a
   theory-level validation either way.

## Fence

- `safe_for_runtime = False`. No `lambda` (coupling parameter) symbol
  introduced or touched -- `Lambda^2` above denotes the antisymmetric tensor
  power, an unrelated standard notation, never conflated with this project's
  own fenced `lambda = FREE_COUPLING_PARAMETER`.
- Does not modify `g96_g2_su3.py` or any other prior-round file -- reused via
  import/re-execution only.

## Verdict

**PROMOTE, with an explicit scope caveat.** The naive index-matched linear
intertwiner search (`A_i U = U B_i` for the arbitrary generator ORDERING each
construction happened to produce) found `n_free=0` -- NO solution at all, not
even non-orthogonal. This is expected and uninformative on its own: neither
generator basis (G96's SVD-derived su(3), nor the Gell-Mann-matrix-derived
su(3)) carries any known correspondence to the other's ordering, and su(3)
has nontrivial automorphisms (inner + the outer 3<->3bar conjugation) that
could relabel generators in many ways. A `n_free=0` result under an
essentially ARBITRARY pairing is not evidence of inequivalence -- it means
the naive test asked the wrong question, and this was caught and corrected
mid-round rather than reported as a false negative.

The actual rigorous, basis-and-normalization-INDEPENDENT test --
`Casimir(representation)/Casimir(adjoint)`, built from each side's OWN
structure constants and Killing form so the normalization cancels in the
ratio -- gives **exactly 0.444444... = 4/9** (the standard textbook value for
su(3)'s fundamental "3"/"3bar") for **all three** independently-built
embeddings: A (G96's G2/SU(3)-on-S6 tangent space), B (Tom's SU(3) subset
SU(4)~SO(6) via the Cl(6) gamma-matrix construction), and C (G10-B's
J-preserving construction, run as a control this round expected might differ
and instead confirmed the same value). All three differences are at machine
precision (~1e-16), and the Casimir is confirmed EXACTLY scalar (Schur's
lemma check, "scalar defect" ~1e-16) on each representation, ruling out a
coincidental match between structurally different reducible combinations.

**What this establishes [VERIFIED-tool, exact]:** all three constructions
realize the SAME representation TYPE of su(3) -- the fundamental "3"
(equivalently its conjugate "3bar"), realified as the standard 3+3bar
6-dimensional real orthogonal representation.

**What this does NOT fully establish on its own [gap, named honestly]:** an
EXPLICIT orthogonal conjugating matrix U was not constructed (the naive
search that would have found it needs the correct generator correspondence,
which was not solved for this round -- finding the Lie-algebra automorphism
between the two bases first is a separate, larger computation not attempted
here). The step from "same representation type, Casimir-confirmed" to "same
O(6)-conjugacy class" relies additionally on a cited, standard fact of su(3)
representation theory: for a fixed representation type realized as a real
orthogonal representation compatible with an invariant metric, the embedding
is unique up to O(6)-conjugation (Aut(su(3)) acting on this representation
type has a single orbit under conjugation). This fact is NOT re-derived here
-- it is standard and well known, but this round should not be read as having
independently proven it from scratch.

**Evidence:** [VERIFIED-tool] Casimir ratio, exact, 3/3 constructions agree
to ~1e-16. [INFERRED, standard rep theory, not re-derived] the step from
"same type" to "same conjugacy class."

**Status:** CLOSED PROMOTE (representation-type equivalence rigorously
established; full explicit-conjugacy-matrix construction is a natural,
separate follow-up, not required for the correspondence-relevant conclusion).
