# Critical Blocks — known methodological pitfalls from this project's own history

This file lists specific, documented ways this project's own internal work
got the computation wrong (or nearly did) before correcting it — not to
bias your answer, but because these are genuine methodological traps in
this exact computation, and re-discovering them independently is a good
sign, while missing them is a real risk to your result's validity. None of
the entries below reveal the final rank, matrix entries, or dimensions.

## 1. Invariant-subspace search completeness (the most important one)

**Historical fact (this project's own record):** an earlier internal
attempt at a structurally similar invariant search (predating this
packet's calibration round) searched only a pre-selected 9-dimensional
sub-block of a larger fibre space, rather than the full space, and had to
hand-supply one invariant vector that turned out to lie OUTSIDE that
sub-block. A later, independent completeness audit (full search over the
entire fibre, no pre-selection) confirmed the correct invariant dimension
but only by searching exhaustively — the original narrower search would
have silently missed a genuine invariant had it not been separately
supplied.

**What this means for you:** when finding the `SU(3)`-invariant subspaces
of the domain and target blocks (`bundle_definition.md`), search the FULL
16-dimensional block for each as a joint nullspace of all 8 isotropy
generators. Do not restrict to a smaller sub-block chosen by "which basis
vectors look plausibly invariant" — that is exactly the failure mode
documented above.

## 2. Hermiticity / adjoint consistency

The domain-to-target map `D⁺` and its formal adjoint `D⁻` (target-to-
domain) should satisfy the standard inner-product adjoint relation:
`⟨D⁺u, ŵ⟩ = ⟨u, D⁻ŵ⟩` for all `u` in the domain invariant subspace and
`ŵ` in the target invariant subspace, using the natural Hermitian inner
product on the tensor bundle. Treat a failure of this relation as a signal
of a construction error (sign, normalization, or basis mismatch)
somewhere upstream — not as a property of the geometry itself.

## 3. Residual-coordinate leakage

After projecting onto the invariant subspaces and applying `D⁺`, check
that the result lies ENTIRELY within the target invariant subspace — i.e.
the component of `D⁺u` orthogonal to the target invariant subspace should
vanish exactly, for every `u` in the domain invariant subspace. A nonzero
residual here indicates either an error in the invariant-subspace
computation or a genuine inconsistency worth flagging explicitly (do not
silently discard the residual).

## 4. Convention-sweep discipline

Once your calibration gate (`conventions.md` item 2) passes, you should
find that certain residual convention choices — genuinely free ones, per
`conventions.md`'s "free" list — do not change your qualitative verdict
(e.g., whether the map is zero or nonzero), while at least one candidate
"convention flip" that might seem equally plausible actually FAILS the
calibration gate itself and should be excluded on those grounds, not
because it gives an inconvenient answer. If you find a convention that
changes your verdict AND passes calibration, that is a significant,
reportable finding — do not paper over it.

## 5. Basis-choice invariance

Your final rank verdict must be invariant under any change of orthonormal
basis within the domain and target invariant subspaces (a change of basis
is a similarity/congruence transformation on the matrix and does not
change its rank). If you find your answer depends on which orthonormal
basis you picked, that indicates a computational error, not a genuine
basis-dependence — rank is a basis-independent property of a linear map
between fixed vector spaces.

## What this file does NOT tell you

- Whether the domain and target dimensions found in this project's own
  work were 1, 2, or something else.
- What the "one narrower sub-block" from pitfall #1 actually was, or how
  many dimensions it had.
- The rank verdict itself, or any matrix entry.
