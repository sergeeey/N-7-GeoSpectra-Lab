# Round59 External Verification Packet — Problem Statement

**Purpose of this packet:** enable an external reviewer (not previously
involved in this project) to independently reproduce a single, well-scoped
technical claim, without access to the expected numerical answer until
after they have committed to their own result. This is the "external human
review" rung this project's own internal certification (round59,
2026-07-14) explicitly named as the one outstanding step above its current
`[VERIFIED-INDEPENDENT-INTERNAL]` status.

## What you are being asked to compute

**Claim to check:** for the physical (Levi-Civita-connection) twisted
Dirac operator on `S⁶ = G₂/SU(3)`, restricted to its trivial (`SU(3)`-
invariant) isotypic sector, the map

```
D⁺|₁ : ℂ² → ℂ¹
```

has a specific rank (0, 1, or 2 are the only possibilities given the
domain/target dimensions below). You are asked to determine this rank
independently, from the primary mathematical source and your own
implementation choices — not from any code, script, or numerical output
in this project's repository.

## Precise setup (definitions only — no result content)

- Base geometry: `S⁶`, realized as the homogeneous space `G₂/SU(3)`
  (nearly-Kähler structure, standard in the literature).
- Spinor bundle: `Σ = Λ•(ℂ³)`, the rank-8 complex spinor bundle associated
  to the tangent bundle of `S⁶`, split into even/odd parts `Σ = Σ₊ ⊕ Σ₋`
  (`dim Σ₊ = dim Σ₋ = 4`) by the `ℤ₂`-grading of the exterior algebra.
- Twisted operator: the Dirac operator `D` acting on the tensor bundle
  `Σ_odd ⊗ Σ_even` (domain fibre) and `Σ_even ⊗ Σ_even` (target fibre),
  where the twisting bundle is itself a copy of `Σ_even` (`S⁻`) — this is
  the "twisted Dirac operator" of the project's own L4 chain, restricted
  here to a single fibre-algebra computation, not the global operator.
- **Domain:** the `SU(3)`-invariant subspace of `Σ_odd ⊗ Σ_even` inside the
  64-dimensional full tensor fibre (`8×8`).
- **Target:** the `SU(3)`-invariant subspace of `Σ_even ⊗ Σ_even` inside
  the same 64-dimensional full tensor fibre.
- `D⁺` denotes the restriction of the (fibre-level) Dirac action to the map
  from the domain block to the target block.
- The `su(3)` action referenced above is the isotropy representation of
  `SU(3) = \mathrm{Stab}(pt) \subset G_2` on the spinor bundle, i.e. the
  standard `G_2 \to SO(6)` embedding's induced action, NOT an arbitrarily
  chosen `su(3)` — see `conventions.md` and `bundle_definition.md` for the
  exact construction.

## What you are asked to determine

1. The dimension of the domain `SU(3)`-invariant subspace (search the FULL
   64-dimensional tensor fibre — do not assume any particular sub-block a
   priori; see `critical_blocks.md` item 1 for why this matters).
2. The dimension of the target `SU(3)`-invariant subspace (same caveat).
3. Given orthonormal bases of each (call the domain basis `u₁, ..., u_m`
   and the target basis `ŵ₁, ..., ŵ_n`, where `m, n` are whatever you find
   in steps 1-2), the explicit matrix of `D⁺` restricted to these bases.
4. The rank of that matrix.
5. Whether the rank's sign/positivity (not necessarily its exact numeric
   value) is stable under the residual convention ambiguities inherent to
   the construction (see `conventions.md` for which conventions are fixed
   by the calibration anchor and which are genuinely free).

## What is intentionally withheld until after your submission

- The dimensions found in this project's own internal computation.
- The exact numerical values of the matrix entries.
- The rank verdict itself.

See `verification_protocol.md` for exactly when and how these are revealed
(`expected_output_sealed.md`).

## Primary source

`Agricola_Hofmann_Lawn_2023_invariant_spinors.pdf` (arXiv:2203.02961,
already present in this repository's root — this is the paper this
project's own construction is calibrated against). Theorem 5.1 of that
paper is the calibration anchor referenced throughout this packet — see
`conventions.md`.

## Explicitly NOT part of this packet's scope

- This packet does **not** ask you to verify anything about the separate
  triality-distinguishability / physical-realization question addressed
  in this project's `paper/P1_FROZEN_VERDICTS_TABLE.md` — that is a
  different, independent line of work. This packet concerns only the
  `S⁶`-only trivial-sector rank computation described above.
- This packet does **not** ask you to evaluate `λ` (the project's free
  coupling parameter) or any runtime/safety claim — those are out of
  scope by the project's own standing fence.
