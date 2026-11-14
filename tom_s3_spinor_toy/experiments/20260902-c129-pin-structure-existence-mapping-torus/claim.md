# C129 claim -- does the non-orientable mapping torus admit a Pin structure?
# (C127/C128's Relaxation Map item Y1, the re-specified form of C127's X6)

## Question type (EstimandOps L0)

**Descriptive/existence.** Not causal, not predictive. Does a specific
closed non-orientable 4-manifold, built entirely from this project's own
frozen `S³` geometry, admit a `Pin^+` structure, a `Pin^-` structure,
neither, or both -- checked directly via Stiefel-Whitney classes, not
looked up as a group value.

## Background, stated honestly before any computation

C128 (2026-09-02) proved: any diffeomorphism `f` of `S³` with
`f_*∇⁰ = ∇¹` is automatically an isometry of the round metric with
`det M_f = -1`, i.e. orientation-reversing (§4, proven algebraically AND
by an independent exact symbolic/Groebner computation). C125 had already
identified the concrete candidates: `ι(g) = g^{-1}` (quaternionic
conjugation restricted to `S³ ⊂ ℍ`, an involution, `ι² = id`, fixed-point
set `{±1}`), and the coset `f_{a,b} ∘ ι` for `a,b ∈ SU(2)`.

C128 §6b showed: the mapping torus of an orientation-reversing
diffeomorphism of an oriented manifold is non-orientable (the same
mechanism as the Klein bottle being the mapping torus of a reflection of
`S¹`). C127's original X6 asked for a class in `Ω^{Spin}_4`, which
presupposes orientability/spin structure and is therefore the WRONG
functor for this object (C128 §6b, §7 Y1). This round asks the question
one level down: does the manifold even admit ANY of the structures
(`Pin^+`, `Pin^-`) that would let a Dai-Freed-style anomaly argument be
posed on it at all -- before asking what the fermion content requires
(that second step is round95's still-missing S⁶-S³ link, C127's
ingredient 2, and is explicitly OUT OF SCOPE here).

**C128 also flagged, and this round must respect:** a skeptic pass
supplied `Ω^{Pin^+}_4 = ℤ/16`, `Ω^{Pin^-}_4 = 0` from memory, explicitly
marked `[MEMORY, unverified, LOW]`, and two arXiv searches in that round
failed to confirm them. **Do not reuse those numbers here without your
own independent verification** -- if you need them, re-derive or
re-verify from a primary or citable secondary source, tagged honestly.

## The Zero-Signal Gate check, required before proceeding

Per `falsification-ladder.md` Step -5: `(∃ entity) ∧ (∃ falsifiable
predicate) ∧ (∃ measurable outcome)`, all three required.

- **Entity:** the mapping torus `M_ι = S³ ×_ι S¹` of the specific
  isometry `ι(g) = g^{-1}` on `S³` (round99/111/113's actual candidate,
  not an arbitrary orientation-reversing map) -- a fully concrete,
  named, closed 4-manifold. If `ι` itself turns out to be degenerate or
  special in some way that makes its own mapping torus a bad
  representative (e.g. because `ι` is an involution, its mapping torus
  may have extra structure, e.g. relate to a `ℤ₂`-quotient or a flat
  bundle -- check and state this explicitly, do not gloss over it), also
  compute for the coset representative `f_{a,b} ∘ ι` for generic `a,b`
  and note whether the answer depends on the choice.
- **Falsifiable predicate:** "`w₂(M_ι) = 0`" (Pin^- exists) and,
  separately, "`w₂(M_ι) + w₁(M_ι)² = 0`" (Pin^+ exists) -- each is a
  yes/no question computable from the manifold's actual characteristic
  classes, not a lookup.
- **Measurable outcome:** an explicit computation or citation-backed
  derivation of `w₁` and `w₂` for this specific mapping torus (e.g. via
  the Wang sequence / Leray-Hirsch for a mapping torus's cohomology, or
  via an explicit handle/CW structure, or via citing a known classification
  of mapping tori of finite-order isometries of `S³` if one exists in the
  literature -- search before assuming none does), and the resulting
  Pin^+/Pin^- yes-or-no.

**If the Stiefel-Whitney classes cannot be computed or cited with real
confidence from available tools, this round should return `BLOCKED
(missing ingredient named)` -- NOT guess, NOT reuse the unverified
`[MEMORY]` bordism-group values from C128 as a substitute for actually
checking existence, and NOT silently narrow the question to "assume Pin^-
because that is the more common case."** This is explicitly permitted and
is not a failure of the round.

## Falsifiable claim (only if the Zero-Signal Gate passes)

The mapping torus `M_ι` admits `Pin^-`, admits `Pin^+`, admits both, or
admits neither -- stated with an explicit `w₁`, `w₂` computation or
citation, and with the answer's dependence (or independence) on which
specific orientation-reversing relating map (`ι` vs a coset
representative) was used made explicit.

**Kill criterion:** the round fails its own purpose if it (a) asserts a
Pin-type answer without exhibiting `w₁`/`w₂` or a directly applicable
citation, (b) reuses C128's flagged `[MEMORY, unverified]` bordism-GROUP
values as if they were evidence about STRUCTURE EXISTENCE (a category
error C128 itself warned against -- group values answer a different,
later question), or (c) silently assumes the answer is the same for `ι`
and for `f_{a,b}∘ι` without checking.

## What this round does NOT show

- Does not compute any bordism group or evaluate any anomaly -- existence
  of the structure is the entire scope (C127's own X6, C128's Y1, both
  explicitly separate "does the structure exist" from "does the anomaly
  force the pair").
- Does not touch round95's missing S⁶-S³ link (C127's ingredient 2) --
  that determines which Pin type the FERMION CONTENT needs, a separate,
  later question this round does not attempt.
- Does not reopen C125's `FALSIFIED`, C126's `WEAKENED`, C127's
  `BLOCKED`, or C128's verdict -- builds on all four as given.
- Does not change `N_gen=3`'s CONDITIONAL status, `lambda=
  FREE_COUPLING_PARAMETER`, or `safe_for_runtime=False`.
- Does not solicit Tom Lawrence's Part 5.

## Verification plan

- Read C127's `decision.md` §6 and C128's `decision.md` §6 (both, in
  full) before doing anything else -- the object this round studies is
  defined there, not here.
- Literature-first for any classification of mapping tori of `S³` under
  finite-order isometries, or standard Stiefel-Whitney formulas for
  mapping tori (Wang exact sequence route) -- cite what is found, do not
  assume it does not exist without searching.
- Compute `w₁`, `w₂` explicitly if the geometry permits a direct
  argument (e.g. `ι`'s fixed-point structure, its action on `H^*(S³)`,
  or an explicit local computation), or state precisely why it cannot be
  determined with available tools.
- FL Step 8a skeptic pass (or, given this project's `C127`/`C128`
  precedent for a load-bearing conclusion, TWO independent passes with
  differently-worded prompts per the Paraphrase-Sensitivity Probe if the
  first pass's verdict is anything other than a clean, unqualified
  confirmation) before this round's finding enters the permanent record.
