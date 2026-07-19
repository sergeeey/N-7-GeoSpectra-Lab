# Conventions (fixed vs. free) — Round59 External Verification Packet

This file states which conventions are PINNED by the calibration anchor
(you must reproduce these, they are not free choices) and which are
genuinely UNDETERMINED by it (your own consistent choice is fine, and
should not change the final rank verdict — that stability is itself part
of what you are asked to check).

**Primary source for everything below:**
`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` (arXiv:2203.02961),
specifically §5 (Theorem 5.1 and Remark 5.2). Transcribe directly from
that source — do not use any value from this project's own code or
documents as a substitute for reading the primary source yourself. This
is a hard requirement, not a suggestion: this project's own internal
"Route A" (independent reimplementation) was explicitly forbidden from
reading any of this project's prior scripts for the same reason, and its
result is only meaningful because of that discipline.

## Pinned by the calibration anchor (must match)

1. **Clifford relation sign.** The source's convention (p.6, referenced in
   §5) is `v·w + w·v = -2β(v,w)·1`, which for an orthonormal frame gives
   `eᵢ·eᵢ = -1` (negative-definite). Verify your Clifford matrix
   construction satisfies this before anything else — this is a pure
   sanity gate, independent of any project-specific result.
2. **Killing spinor definition.** Theorem 5.1 identifies two explicit
   Killing spinors on this geometry, of the schematic form
   `ψ± = 1 ± y₁₂₃` (where `y₁₂₃` is the top-degree basis element of
   `Λ•(ℂ³)` in the natural monomial basis — confirm the exact normalization
   from the source itself, not from this description). **The theorem's
   own stated Killing eigenvalue is part of what you must independently
   reproduce as your calibration gate — look it up in the source, do not
   ask this project for it.** Your calibration passes when your
   implementation reproduces the Killing equation `Dψ± = λ·ψ±` for the
   source's own stated `λ`, in all directions the theorem specifies (this
   project's own internal check required all 6 directions to match
   exactly before proceeding).
3. **Nomizu 2-forms.** The Levi-Civita connection's Nomizu tensor,
   expressed as `Λ_g(eᵢ)` (2-forms valued in `so(6) = Λ²(ℝ⁶)`), is given
   explicitly in the source's Remark 5.2 — transcribe these directly.
4. **Spinor bundle.** `Σ = Λ•(ℂ³)`, `ℤ₂`-graded into `Σ₊` (even-degree,
   dim 4) and `Σ₋` (odd-degree, dim 4) — standard exterior-algebra
   grading, not a project-specific choice.

## Genuinely free (your choice; must not change the final verdict)

1. **Overall global sign/phase of the Clifford representation** beyond
   what the calibration gate above pins — e.g. an overall sign flip
   consistent with `eᵢ·eᵢ = -1` still holding.
2. **Choice of orthonormal basis** for the domain and target invariant
   subspaces you find (any orthonormal basis is equally valid; the rank
   of the resulting matrix is basis-independent, and this project's own
   internal check verified invariance under real `O(2)` and complex
   `U(2)` basis rotations of the relevant blocks).
3. **Which specific point of `G₂/SU(3)` you compute at**, provided you use
   the isotropy `su(3)` at that same point consistently throughout (the
   construction is homogeneous; any point gives an equivalent computation
   up to the basis choice above).

## What NOT to infer from this file

This file deliberately does **not** state:
- The dimension of the domain or target invariant subspaces.
- The Killing eigenvalue's numeric value (find it in the cited theorem
  yourself — this is a public, citable fact, not a project result, but
  stating it here would remove the independence of your own calibration
  step).
- Any matrix entry, rank value, or sign of the map `D⁺` this packet asks
  you to compute.

See `expected_output_sealed.md` for when these become available, and
`verification_protocol.md` for the exact sequencing.
