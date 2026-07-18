# Claim — Round108 (Codex item 1): Stabilizer of the FULL Background
(Metric + G₂-Structure), Not Just the Round Metric

**Question type:** Descriptive (a direct Lie-algebra stabilizer
computation — "which of the 21 `so(7)` Killing vectors of round `S⁶`
ALSO preserve the associative 3-form `φ` that defines the `G₂`-structure
used to build `SU(3)_c`?").

## Section 1 — Background

Gate G97 (`preprint.tex:280-286`) states "no `SU(4)` subgroup in
`Iso(S³×S⁶)=SO(4)×SO(7)`" — checked against the round-metric isometry
group `SO(7)` (21-dim). But `preprint.tex:195-196,274-277` states
`SU(3)_c` is actually derived from "the `G₂` holonomy of `S⁶=G₂/SU(3)`" —
a DIFFERENT, smaller (14-dim) group. Codex/round105's item 1 (its own
top-ranked "decisive calculation neither round97 nor round102
performed"): compute the actual stabilizer of the FULL background
(metric + torsion + almost-complex structure `J` + twist field) — not
just the round metric alone — to determine whether the physically
relevant ambient group for gate G97's question is `SO(7)` (21-dim,
metric only) or `G₂` (14-dim, full background), or something else
entirely.

## Section 2 — Method

The `G₂`-structure on `S⁶` is standard-defined by a single associative
3-form `φ ∈ Λ³(ℝ⁷)*` (the octonion cross-product structure); `G₂` is,
BY DEFINITION/construction, exactly the stabilizer of `φ` in `GL(7,ℝ)`
(intersected with `SO(7)` for the compact real form — automatic here).
Concretely:
1. Build the standard, citable associative 3-form `φ₀` (explicit
   antisymmetric 3-tensor, standard convention e.g. Bryant 2005/Karigiannis
   surveys: `φ₀=e^{123}+e^{145}+e^{167}+e^{246}−e^{257}−e^{347}−e^{356}`).
2. Build all 21 `so(7)` generators (standard antisymmetric basis).
3. Compute the induced Lie-algebra action of each generator on `φ`
   (infinitesimal `GL(7)` action on a `(0,3)`-tensor) via a formula
   validated FIRST against a known case (the metric `g=δ`, which ALL 21
   `so(7)` generators must preserve by definition — a mandatory sanity
   check before trusting the same formula on `φ`, per this session's own
   established discipline for exactly this kind of tensor-index
   computation).
4. Determine the dimension and (if feasible) basic structural properties
   of `{X∈so(7) : X·φ=0}` — the stabilizer subalgebra.

## Section 3 — Pre-registered criteria

- **STABILIZER = 14-DIM, CONSISTENT WITH `G₂`:** confirms the physically
  relevant ambient group for `SU(3)_c`'s own derivation (and hence for
  checking `SU(4)`-completion consistently with it) is `G₂` (14-dim), not
  the full `SO(7)` (21-dim) — sharpening, via direct computation rather
  than citation, exactly what Codex's item 1 asked for. This does NOT
  automatically resolve gate G97 either way (still needs `dim(su(4))=15
  >14=dim(G₂)`, already noted in round102, now on a directly-computed,
  not merely cited, footing).
- **STABILIZER ≠ 14-DIM:** a genuinely new, unexpected finding — would
  require re-examining whether `φ₀`'s standard form was used correctly,
  or whether this project's actual `J`/torsion differs from the standard
  associative-3-form convention.
- **BLOCKED:** the sanity check (metric preserved by all 21 generators)
  itself fails, indicating an error in the tensor-action formula — stop
  before trusting anything about `φ`.

## Section 4 — Escalation note

Per this session's established practice for exactly this kind of
Lie-theory/tensor computation (rounds 102, 106, 107 all required
skeptic-driven correction or validation-strengthening in adjacent
territory), this round's conclusion goes through mandatory
context-asymmetric skeptic review before being reported as more than a
hypothesis.
