# Round115 — Claim

**OB1 mechanism search, continued.** Applying round114's own lesson (check
whether a candidate reduces to something already known/circular BEFORE
building elaborate machinery) to a NEW candidate: does this project's OWN
already-established, quantized `H³(S³)` flux (Hodge corollary,
`experiments/20260622-lambda-dim-gate/decision.md`, also stated in
`preprint.tex` line 1117) supply a parent-action-level selection principle
for the torsion parameter `t`, via standard flux quantization?

## Source facts (already established in this project, cited not re-derived)

1. **Hodge corollary** (`lambda-dim-gate/decision.md`, Künneth formula):
   `H³(S³×S⁶;ℝ) = H³(S³)⊗H⁰(S⁶) ⊕ H⁰(S³)⊗H³(S⁶) = ℝ⊕0 = ℝ`. The harmonic
   3-form flux threading the compactification comes ENTIRELY from `S³`
   (topologically quantized) — `S⁶` contributes none (`b₃(S⁶)=0`).
2. **Torsion family** (round99/round111/round113, now confirmed as ONE
   unified connection): `T^t = (2t-1)·c·vol_{S³}`, `c` a fixed structure
   constant of `su(2)` in the orthonormal `{Z_i=iσ_i}` frame (round67's
   normalization, `⟨X,Y⟩=-½Tr(XY)`).
3. **Round67's own self-flagged risk** (its own `decision.md`, item 2):
   "picking `t=0` (say) specifically to kill KT-8 would be exactly the
   kind of positioning-a-minimum-rather-than-deriving-a-value pattern this
   project's own CLAUDE.md calls out" — i.e., this project has ALREADY
   identified the exact failure mode this round must guard against.

## L0 gate (EstimandOps)

**Two distinct question types, kept explicitly separate:**
- **Descriptive** (fact, verifiable now): is `T^t` (any 3-form on `S³`)
  automatically proportional to the same 1-dimensional cohomology class as
  the Hodge-corollary flux, since `H³(S³;ℝ)=ℝ` is 1-dimensional? — Yes,
  trivially, by dimension counting alone (any 3-form on a 3-manifold is a
  scalar multiple of the volume form). **Not a discovery, stated for
  completeness only.**
- **Hypothesis** (NOT established, requires independent physical
  justification): does the physical spin-connection torsion used in the
  Dirac operator (`D^t`, round67/68) correspond to an actual NS-NS-type
  flux `H`, subject to a standard Dirac-type quantization condition
  `∫_{S³}H/(unit) ∈ ℤ`? This identification (torsion ↔ physical flux) is
  standard in some string/SUGRA contexts (heterotic torsional geometries,
  Bismut-type connections) but has **not** been derived or justified for
  THIS project's specific construction — it is an assumption being tested
  here, not a fact being applied.

## Falsifiable claim

**IF** the torsion-as-flux identification holds **AND** flux quantization
fixes `(2t-1)·c·\mathrm{Vol}(S³)` to be an integer multiple of a flux
quantum unit `Q`, **THEN** check whether the specific values `t=0,1`
(where `(2t-1)=∓1`) correspond to a *natural*, independently-motivated
choice of `Q` (e.g. `Q = c·\mathrm{Vol}(S³)` exactly, the "one unit"
value) — or whether declaring `Q := c·\mathrm{Vol}(S³)` is itself a free
choice made *in order to* produce `t=0,1`, which would be the exact
circularity round67 already flagged.

## Kill criterion (pre-registered, BEFORE any computation)

- If `Q = c·\mathrm{Vol}(S³)` can be independently motivated (e.g. from a
  standard flux-quantization formula in an actual cited SUGRA/string
  reference, giving a SPECIFIC numerical value for `Q` that is not simply
  "whatever makes `t=0,1` work") → genuine candidate parent-action
  ingredient, `PARTIAL PASS`, worth a follow-up round with that reference
  read directly (not from memory).
- If no such independent motivation is found or citable, and the ONLY way
  to get `t=0,1` from this mechanism is to define `Q` after the fact to
  match → **CIRCULAR, same trap round67 self-flagged** — this round's
  conclusion should be `NULL, restates F6, does not close it`, not a
  positive result, and must say so plainly.

## What this does NOT mean (pre-registered)

1. Does NOT assume the torsion-as-flux identification is correct — this is
   the hypothesis under test, not an input.
2. Does NOT affect `N_gen=3`, `lambda=FREE_COUPLING_PARAMETER`, or
   `safe_for_runtime=False`. Note: `lambda`'s own flux-based origin was
   ALREADY exhausted (G83-G86B, same Hodge-corollary flux, different
   question — sourcing the exponential suppression coefficient, not the
   S³ Dirac-operator torsion). This round asks a DIFFERENT question about
   the SAME flux object; a null result here does not retroactively change
   the already-closed λ conclusion, and a positive result here would NOT
   reopen it either (different physical role).
3. Does NOT constitute reading a new external source — this round works
   entirely from this project's own already-cited internal facts plus
   general, textbook-level knowledge of flux quantization; if a specific
   external formula/reference becomes necessary to resolve the kill
   criterion's PASS branch, it must be read directly (pymupdf or WebFetch)
   before being cited, not pulled from training-data memory.
